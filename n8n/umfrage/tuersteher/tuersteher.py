#!/usr/bin/env python3
# AI-assisted: Claude, human-reviewed ausstehend, Stand 16.09.2026
"""Türsteher: geschützte Umfragen für Lehrveranstaltungen.

Zeigt das Formular selbst, statt auf NocoDB weiterzuleiten. Deshalb gibt es
keinen Link, den man im Kurschat weitergeben kann.

    GET  /u/<kennung>            Matrikelnummer abfragen (oder direkt Fragen, wenn offen)
    POST /u/<kennung>/pruefen    Nummer gegen die Zulassungsliste prüfen
    POST /u/<kennung>/senden     Antwort speichern
    GET  /health

Die Matrikelnummer landet NIE in der Antworttabelle. Sie wird nur in der
Zulassungsliste abgehakt. Wie im Wahllokal: Verzeichnis und Urne sind getrennt.

Umgebung: NOCODB_URL, NOCODB_TOKEN, STEUER_TABELLE, TICKET_SCHLUESSEL
"""
import hashlib
import hmac
import html
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

NC = os.environ.get("NOCODB_URL", "http://nocodb:8080").rstrip("/")
TOKEN = os.environ.get("NOCODB_TOKEN", "")
STEUER = os.environ.get("STEUER_TABELLE", "")
SCHLUESSEL = os.environ.get("TICKET_SCHLUESSEL", "").encode() or os.urandom(32)
TICKET_GUELTIG = 45 * 60          # Sekunden
ANTWORT_FELDER_AUS = {"Id", "CreatedAt", "UpdatedAt", "nc_order", "eingang"}


# ---------------------------------------------------------------- NocoDB

def nc(pfad, daten=None, methode=None):
    req = urllib.request.Request(
        NC + pfad,
        data=json.dumps(daten).encode() if daten is not None else None,
        headers={"xc-token": TOKEN, "Content-Type": "application/json"},
        method=methode or ("POST" if daten is not None else "GET"))
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)


def umfrage_holen(kennung):
    """Zeile aus der Steuertabelle. Gibt None zurück, wenn es sie nicht gibt."""
    q = urllib.parse.quote(f"(kennung,eq,{kennung})")
    treffer = nc(f"/api/v2/tables/{STEUER}/records?where={q}&limit=1").get("list", [])
    return treffer[0] if treffer else None


def felder_holen(tabelle):
    """Die Fragen, so wie sie in NocoDB stehen. Eine Wahrheit, kein zweites Formular."""
    spalten = nc(f"/api/v2/meta/tables/{tabelle}")["columns"]
    aus = []
    for c in spalten:
        if c.get("system") or c["title"] in ANTWORT_FELDER_AUS:
            continue
        if c["uidt"] in ("ID", "CreatedTime", "LastModifiedTime", "Formula", "Rollup", "Lookup", "LinkToAnotherRecord", "Links"):
            continue
        werte = []
        if c["uidt"] == "SingleSelect":
            roh = (c.get("colOptions") or {}).get("options") or []
            werte = [o["title"] for o in roh]
        aus.append({"name": c["title"], "art": c["uidt"], "werte": werte})
    return aus


# ---------------------------------------------------------------- Tickets

def ticket_machen(kennung, nummer):
    nutzlast = f"{kennung}|{nummer}|{int(time.time())}"
    sig = hmac.new(SCHLUESSEL, nutzlast.encode(), hashlib.sha256).hexdigest()[:32]
    return f"{nutzlast}|{sig}"


def ticket_pruefen(ticket, kennung):
    """Gibt die Matrikelnummer zurück oder None. Gültig 45 Minuten."""
    try:
        k, nummer, zeit, sig = ticket.split("|")
    except ValueError:
        return None
    nutzlast = f"{k}|{nummer}|{zeit}"
    erwartet = hmac.new(SCHLUESSEL, nutzlast.encode(), hashlib.sha256).hexdigest()[:32]
    if not hmac.compare_digest(sig, erwartet):
        return None
    if k != kennung or time.time() - int(zeit) > TICKET_GUELTIG:
        return None
    return nummer


# ---------------------------------------------------------------- HTML

STIL = """<style>
:root{--rot:#C81E0F;--grau:#4a4a4a}
*{box-sizing:border-box}
body{font-family:'Source Sans 3','Segoe UI',system-ui,sans-serif;background:#f4f4f4;margin:0;padding:24px;color:#1a1a1a}
main{max-width:34rem;margin:0 auto;background:#fff;padding:32px;border-radius:10px;box-shadow:0 2px 12px rgba(0,0,0,.07)}
h1{font-size:1.5rem;margin:0 0 4px;color:var(--rot)}
p.unter{color:var(--grau);margin:0 0 24px;font-size:.95rem}
label{display:block;font-weight:600;margin:20px 0 6px}
input[type=text],textarea,select{width:100%;padding:11px;font-size:1rem;border:1px solid #ccc;border-radius:6px;font-family:inherit}
textarea{min-height:5.5rem;resize:vertical}
button{margin-top:26px;width:100%;padding:13px;font-size:1.05rem;font-weight:600;color:#fff;background:var(--rot);border:0;border-radius:6px;cursor:pointer}
button:hover{background:#a81809}
.sterne{display:flex;gap:6px;margin-top:4px}
.sterne input{display:none}
.sterne label{font-size:2rem;color:#d8d8d8;cursor:pointer;margin:0;font-weight:400;line-height:1}
.sterne input:checked ~ label{color:#d8d8d8}
.sterne:hover label{color:#f0b400}
.fehler{background:#fdeceb;border-left:4px solid var(--rot);padding:12px 14px;border-radius:4px;margin-bottom:18px}
.gut{text-align:center;padding:26px 0}
.gut .haken{font-size:3rem;color:#2d8a3e}
.hinweis{margin-top:26px;padding-top:16px;border-top:1px solid #eee;color:var(--grau);font-size:.85rem}
.wahl label{display:block;font-weight:400;margin:8px 0;cursor:pointer}
</style>"""


def seite(titel, inhalt, status=200):
    return status, "text/html; charset=utf-8", (
        f"<!doctype html><html lang=de><meta charset=utf-8>"
        f"<meta name=viewport content='width=device-width,initial-scale=1'>"
        f"<title>{html.escape(titel)}</title>{STIL}<main>{inhalt}</main></html>").encode()


def feld_html(f, i):
    name = html.escape(f["name"])
    kennung = f"f{i}"
    if f["art"] == "Rating":
        sterne = "".join(
            f'<input type=radio id="{kennung}_{n}" name="{kennung}" value="{n}">'
            f'<label for="{kennung}_{n}">&#9733;</label>' for n in range(1, 6))
        return f'<label>{name}</label><div class="sterne">{sterne}</div>'
    if f["art"] == "SingleSelect":
        opt = "".join(f'<label><input type=radio name="{kennung}" value="{html.escape(w)}"> {html.escape(w)}</label>'
                      for w in f["werte"])
        return f'<label>{name}</label><div class="wahl">{opt}</div>'
    if f["art"] == "LongText":
        return f'<label for="{kennung}">{name}</label><textarea id="{kennung}" name="{kennung}"></textarea>'
    if f["art"] == "Checkbox":
        return f'<label class="wahl"><input type=checkbox name="{kennung}" value="1"> {name}</label>'
    art = "number" if f["art"] == "Number" else ("date" if f["art"] == "Date" else "text")
    return f'<label for="{kennung}">{name}</label><input type="{art}" id="{kennung}" name="{kennung}">'


# ---------------------------------------------------------------- Handler

class Handler(BaseHTTPRequestHandler):
    server_version = "Tuersteher"

    def do_GET(self):
        weg = urllib.parse.urlparse(self.path).path
        if weg == "/health":
            return self.raus(200, "application/json", b'{"ok": true}')
        teile = weg.strip("/").split("/")
        if len(teile) == 2 and teile[0] == "u":
            return self.zeigen(teile[1])
        return self.raus(*seite("Nicht gefunden", "<h1>Nicht gefunden</h1>", 404))

    def do_POST(self):
        weg = urllib.parse.urlparse(self.path).path
        teile = weg.strip("/").split("/")
        if len(teile) == 3 and teile[0] == "u":
            laenge = min(int(self.headers.get("Content-Length") or 0), 100_000)
            daten = urllib.parse.parse_qs(self.rfile.read(laenge).decode("utf-8", "replace"))
            if teile[2] == "pruefen":
                return self.pruefen(teile[1], daten)
            if teile[2] == "senden":
                return self.senden(teile[1], daten)
        return self.raus(*seite("Nicht gefunden", "<h1>Nicht gefunden</h1>", 404))

    # ---- Ansichten

    def zeigen(self, kennung, fehler=""):
        u = umfrage_holen(kennung)
        if not u:
            return self.raus(*seite("Unbekannt", "<h1>Diese Umfrage gibt es nicht</h1>"
                                    "<p class=unter>Bitte den QR-Code noch einmal scannen.</p>", 404))
        if not u.get("offen"):
            return self.raus(*seite("Geschlossen", f"<h1>{html.escape(u['titel'])}</h1>"
                                    "<p class=unter>Diese Umfrage ist geschlossen.</p>", 403))
        if u.get("geschuetzt"):
            hinweis = f'<div class=fehler>{html.escape(fehler)}</div>' if fehler else ""
            return self.raus(*seite(u["titel"], f"""
<h1>{html.escape(u['titel'])}</h1>
<p class=unter>Diese Rueckmeldung ist nur fuer Teilnehmende dieser Veranstaltung.</p>
{hinweis}
<form method=post action="/u/{html.escape(kennung)}/pruefen">
  <label for=nr>Ihre Matrikelnummer</label>
  <input type=text id=nr name=matrikelnummer inputmode=numeric autocomplete=off required autofocus>
  <button type=submit>Weiter</button>
</form>
<p class=hinweis>Ihre Matrikelnummer wird <strong>nicht</strong> zusammen mit Ihrer Antwort
gespeichert. Sie dient nur als Eintrittskarte und wird in einer getrennten Liste abgehakt.
Ihre Antwort bleibt anonym.</p>"""))
        return self.fragen_zeigen(kennung, u, ticket="")

    def fragen_zeigen(self, kennung, u, ticket, fehler=""):
        felder = felder_holen(u["antwort_tabelle"])
        if not felder:
            return self.raus(*seite("Leer", "<h1>Diese Umfrage hat noch keine Fragen</h1>", 500))
        hinweis = f'<div class=fehler>{html.escape(fehler)}</div>' if fehler else ""
        eingaben = "".join(feld_html(f, i) for i, f in enumerate(felder))
        verstecktes = f'<input type=hidden name=ticket value="{html.escape(ticket)}">' if ticket else ""
        return self.raus(*seite(u["titel"], f"""
<h1>{html.escape(u['titel'])}</h1>
<p class=unter>Anonym. Es wird weder Name noch Matrikelnummer gespeichert.</p>
{hinweis}
<form method=post action="/u/{html.escape(kennung)}/senden">
{verstecktes}{eingaben}
  <button type=submit>Antwort abgeben</button>
</form>"""))

    # ---- Aktionen

    def pruefen(self, kennung, daten):
        u = umfrage_holen(kennung)
        if not u or not u.get("offen"):
            return self.raus(*seite("Geschlossen", "<h1>Diese Umfrage ist geschlossen</h1>", 403))
        nummer = (daten.get("matrikelnummer") or [""])[0].strip()
        if not nummer:
            return self.zeigen(kennung, "Bitte eine Matrikelnummer eingeben.")
        q = urllib.parse.quote(f"(matrikelnummer,eq,{nummer})")
        treffer = nc(f"/api/v2/tables/{u['zulassung_tabelle']}/records?where={q}&limit=1").get("list", [])
        if not treffer:
            return self.zeigen(kennung, "Diese Matrikelnummer steht nicht auf der Teilnehmerliste.")
        if treffer[0].get("abgestimmt"):
            return self.raus(*seite("Schon abgestimmt", f"<h1>{html.escape(u['titel'])}</h1>"
                                    "<div class=gut><div class=haken>&#10003;</div>"
                                    "<p>Unter dieser Matrikelnummer wurde bereits abgestimmt.</p></div>", 200))
        return self.fragen_zeigen(kennung, u, ticket_machen(kennung, nummer))

    def senden(self, kennung, daten):
        u = umfrage_holen(kennung)
        if not u or not u.get("offen"):
            return self.raus(*seite("Geschlossen", "<h1>Diese Umfrage ist geschlossen</h1>", 403))

        nummer = None
        if u.get("geschuetzt"):
            nummer = ticket_pruefen((daten.get("ticket") or [""])[0], kennung)
            if not nummer:
                return self.zeigen(kennung, "Ihre Eintrittskarte ist abgelaufen. Bitte noch einmal eingeben.")
            q = urllib.parse.quote(f"(matrikelnummer,eq,{nummer})")
            treffer = nc(f"/api/v2/tables/{u['zulassung_tabelle']}/records?where={q}&limit=1").get("list", [])
            if not treffer:
                return self.zeigen(kennung, "Diese Matrikelnummer steht nicht mehr auf der Liste.")
            if treffer[0].get("abgestimmt"):
                return self.raus(*seite("Schon abgestimmt", f"<h1>{html.escape(u['titel'])}</h1>"
                                        "<div class=gut><div class=haken>&#10003;</div>"
                                        "<p>Unter dieser Matrikelnummer wurde bereits abgestimmt.</p></div>"))

        felder = felder_holen(u["antwort_tabelle"])
        zeile = {}
        for i, f in enumerate(felder):
            wert = (daten.get(f"f{i}") or [""])[0].strip()
            if not wert:
                continue
            if f["art"] == "Rating" or f["art"] == "Number":
                try:
                    zeile[f["name"]] = int(wert)
                except ValueError:
                    continue
            elif f["art"] == "Checkbox":
                zeile[f["name"]] = True
            else:
                zeile[f["name"]] = wert[:5000]
        if not zeile:
            return self.fragen_zeigen(kennung, u, (daten.get("ticket") or [""])[0],
                                      "Bitte mindestens eine Frage beantworten.")

        # Erst die Antwort in die Urne, dann im Verzeichnis abhaken.
        # Diese Reihenfolge: lieber eine Stimme mehr als eine verlorene.
        nc(f"/api/v2/tables/{u['antwort_tabelle']}/records", zeile)
        if nummer:
            nc(f"/api/v2/tables/{u['zulassung_tabelle']}/records",
               {"Id": treffer[0]["Id"], "abgestimmt": True}, methode="PATCH")

        return self.raus(*seite("Danke", f"<h1>{html.escape(u['titel'])}</h1>"
                                "<div class=gut><div class=haken>&#10003;</div>"
                                "<p>Danke, Ihre Antwort ist angekommen.</p></div>"
                                "<p class=hinweis>Ihre Antwort wurde ohne Kennung gespeichert "
                                "und laesst sich Ihnen nicht zuordnen.</p>"))

    # ---- Ausgabe

    def raus(self, status, typ, koerper):
        self.send_response(status)
        self.send_header("Content-Type", typ)
        self.send_header("Content-Length", str(len(koerper)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Frame-Options", "DENY")
        self.send_header("Referrer-Policy", "no-referrer")
        self.end_headers()
        self.wfile.write(koerper)

    def log_message(self, fmt, *args):   # ohne Matrikelnummern, die stehen im Rumpf
        print(f"{self.command} {urllib.parse.urlparse(self.path).path}", flush=True)


if __name__ == "__main__":
    if not TOKEN or not STEUER:
        raise SystemExit("NOCODB_TOKEN und STEUER_TABELLE muessen gesetzt sein")
    print("Tuersteher auf Port 8080", flush=True)
    ThreadingHTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
