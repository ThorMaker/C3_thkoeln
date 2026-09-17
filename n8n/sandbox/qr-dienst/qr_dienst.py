#!/usr/bin/env python3
# AI-assisted: Claude (Fable 5.1), human-reviewed: ausstehend, Stand 12.09.2026
"""QR-Dienst für die n8n-Sandbox: ein winziger HTTP-Dienst, der QR-Codes als PNG liefert.

    GET /qr.png?text=<Inhalt>&groesse=8&rand=2   -> image/png
    GET /health                                  -> ok

Läuft nur im Sandbox-Netz (kein Port nach außen). n8n ruft ihn im Workflow
„Dekanat: Serienbrief als PDF“ auf; der Brief bekommt den QR-Code als Bild eingebettet.
Grenzen: höchstens 2000 Zeichen, Größe 2 bis 20 Bildpunkte je Modul.
"""
import io
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

import qrcode


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = urlparse(self.path)
        if url.path == "/health":
            return self.senden(200, "application/json", json.dumps({"ok": True}).encode())
        if url.path != "/qr.png":
            return self.senden(404, "text/plain", b"nur /qr.png?text=... und /health")
        q = parse_qs(url.query)
        text = (q.get("text") or [""])[0]
        if not text or len(text) > 2000:
            return self.senden(400, "text/plain", b"text fehlt oder ist laenger als 2000 Zeichen")
        try:
            groesse = min(20, max(2, int((q.get("groesse") or ["8"])[0])))
            rand = min(8, max(0, int((q.get("rand") or ["2"])[0])))
        except ValueError:
            return self.senden(400, "text/plain", b"groesse und rand muessen Zahlen sein")
        qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=groesse, border=rand)
        qr.add_data(text)
        qr.make(fit=True)
        puffer = io.BytesIO()
        qr.make_image(fill_color="black", back_color="white").save(puffer, format="PNG")
        self.senden(200, "image/png", puffer.getvalue())

    def senden(self, status, typ, daten):
        self.send_response(status)
        self.send_header("Content-Type", typ)
        self.send_header("Content-Length", str(len(daten)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(daten)

    def log_message(self, fmt, *args):   # eine Zeile je Anfrage, ohne den QR-Inhalt
        print(f"{self.address_string()} {self.command} {urlparse(self.path).path} -> {args[1] if len(args) > 1 else ''}", flush=True)


if __name__ == "__main__":
    print("QR-Dienst auf Port 8080", flush=True)
    ThreadingHTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
