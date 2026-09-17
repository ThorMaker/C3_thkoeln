#!/usr/bin/env python3
"""Erzeugt einen QR-Code als PNG, zum Beispiel für das Rückmeldeformular auf Folie 4.

Aufruf: python3 tools/qr_erzeugen.py <URL> [ausgabe.png]
Benötigt: pip install qrcode pillow
"""
import sys

try:
    import qrcode
except ImportError:
    sys.exit("Bitte zuerst installieren: pip install qrcode pillow")

if len(sys.argv) < 2:
    sys.exit("Aufruf: python3 tools/qr_erzeugen.py <URL> [ausgabe.png]")

url = sys.argv[1]
ziel = sys.argv[2] if len(sys.argv) > 2 else "qr_rueckmeldung.png"
bild = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=20, border=2)
bild.add_data(url)
bild.make(fit=True)
bild.make_image(fill_color="black", back_color="white").save(ziel)
print(f"QR-Code für {url} gespeichert als {ziel}")
