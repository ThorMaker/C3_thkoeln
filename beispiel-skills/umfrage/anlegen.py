#!/usr/bin/env python3
# AI-assisted: Claude, human-reviewed ausstehend, Stand 2026-09-17
"""Legt eine Umfrage an: Tabelle, Formular, Zulassungsliste, Steuerzeile, QR-Code.

Macht dasselbe wie der n8n-Workflow, nur ohne n8n zu oeffnen.
Das Token holt es sich per SSH vom Server, es steht nie in dieser Datei.
"""
import argparse, json, re, subprocess, sys, urllib.error, urllib.parse, urllib.request

NC = "https://nocodb.vibe-cortex.com"
BASE = "p6jz2gyuwlapqqe"
STEUER = "mxnrok36754lt25"
GRAFANA = "https://grafana.vibe-cortex.com/d/umfragen-auswertung/umfrage-auswertung"
TYPEN = {"text": "LongText", "bewertung": "Rating", "zahl": "Number",
         "datum": "Date", "janein": "Checkbox"}


def token():
    r = subprocess.run(["ssh", "n8n-server", "cat ~/.nocodb_api_token"],
                       capture_output=True, text=True, timeout=30)
    t = r.stdout.strip()
    if not t:
        sys.exit("Kein NocoDB-Token erreichbar. Laeuft der SSH-Zugang zu n8n-server?")
    return t


def api(tok, pfad, daten=None, methode=None):
    req = urllib.request.Request(
        NC + pfad, data=json.dumps(daten).encode() if daten is not None else None,
        headers={"xc-token": tok, "Content-Type": "application/json"},
        method=methode or ("POST" if daten is not None else "GET"))
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"NocoDB antwortet {e.code} auf {pfad}\n{e.read().decode()[:400]}")


def schluessel(s):
    s = s.lower()
    for a, b in (("ä", "ae"), ("ö", "oe"), ("ü", "ue"), ("ß", "ss")):
        s = s.replace(a, b)
    return re.sub(r"_+", "_", re.sub(r"[^a-z0-9_]", "_", s)).strip("_") or "feld"


def spalten_aus(text):
    """Eine Zeile je Frage:  Name | Art"""
    aus = []
    for zeile in text.splitlines():
        roh = zeile.strip()
        if not roh:
            continue
        name, _, art = (t.strip() for t in roh.partition("|"))
        if not name:
            continue
        if art.lower().startswith("auswahl"):
            werte = [w.strip() for w in art.split(":", 1)[-1].split(",") if w.strip()]
            if not werte:
                sys.exit(f'Auswahl ohne Werte: "{roh}"')
            aus.append({"title": name, "column_name": schluessel(name), "uidt": "SingleSelect",
                        "dtxp": ",".join("'%s'" % w.replace("'", "''") for w in werte)})
        else:
            aus.append({"title": name, "column_name": schluessel(name),
                        "uidt": TYPEN.get(art.lower(), "SingleLineText")})
    if not aus:
        sys.exit("Keine Frage erkannt. Mindestens eine Zeile eintragen.")
    return aus


def nummern_aus(text):
    """Nimmt Textwiese oder CSV. Wirft Kopfzeilen, Namen und Dubletten weg."""
    gesehen, aus = set(), []
    for stueck in re.split(r"[\n,;]+", text or ""):
        n = stueck.strip().strip("\"'")
        if not re.fullmatch(r"[0-9]{3,20}", n) or n in gesehen:
            continue
        gesehen.add(n)
        aus.append({"matrikelnummer": n})
    return aus


def lies(pfad, direkt):
    if pfad:
        return open(pfad, encoding="utf-8").read()
    return direkt or ""


def main():
    p = argparse.ArgumentParser(description="Umfrage anlegen")
    p.add_argument("--titel", required=True)
    p.add_argument("--fragen"); p.add_argument("--fragen-datei")
    p.add_argument("--geschuetzt", action="store_true")
    p.add_argument("--nummern"); p.add_argument("--nummern-datei")
    p.add_argument("--qr", default="/tmp/umfrage-qr.png")
    a = p.parse_args()

    tok = token()
    spalten = spalten_aus(lies(a.fragen_datei, a.fragen))
    nummern = nummern_aus(lies(a.nummern_datei, a.nummern))
    if a.geschuetzt and not nummern:
        sys.exit("Geschuetzt verlangt mindestens eine Matrikelnummer.")

    name = schluessel(a.titel)
    kennung = f"{name[:28]}-{abs(hash(a.titel + str(len(spalten)))) % 46656:04x}".replace("_", "-")

    print(f"1. Antworttabelle: {len(spalten)} Fragen")
    tab = api(tok, f"/api/v2/meta/bases/{BASE}/tables",
              {"title": a.titel, "table_name": name, "columns": spalten})

    print("2. Formular-Ansicht und Freigabe")
    sicht = api(tok, f"/api/v2/meta/tables/{tab['id']}/forms",
                {"title": "Formular", "heading": a.titel,
                 "subheading": "Anonym. Es wird kein Name und keine Kennung gespeichert.",
                 "success_msg": "Danke! Ihre Antwort ist angekommen."})
    geteilt = api(tok, f"/api/v2/meta/views/{sicht['id']}/share", {})

    print("3. Zulassungsliste (auch wenn offen, damit Schutz nachruestbar bleibt)")
    zul = api(tok, f"/api/v2/meta/bases/{BASE}/tables",
              {"title": "Zugelassen " + a.titel, "table_name": "zugelassen_" + name,
               "columns": [{"title": "matrikelnummer", "column_name": "matrikelnummer", "uidt": "SingleLineText"},
                           {"title": "abgestimmt", "column_name": "abgestimmt", "uidt": "Checkbox"}]})
    if nummern:
        api(tok, f"/api/v2/tables/{zul['id']}/records", nummern)
        print(f"   {len(nummern)} Nummern eingetragen")

    print("4. Steuerzeile")
    api(tok, f"/api/v2/tables/{STEUER}/records",
        {"titel": a.titel, "kennung": kennung, "antwort_tabelle": tab["id"],
         "formular_uuid": geteilt.get("uuid"), "geschuetzt": bool(a.geschuetzt),
         "zulassung_tabelle": zul["id"], "offen": True})

    link = f"{NC}/u/{kennung}"
    print("5. QR-Code")
    enc = urllib.parse.quote(link, safe="")
    subprocess.run(["ssh", "n8n-server",
                    f"docker exec n8n sh -c 'wget -qO /tmp/qr.png \"http://qr-dienst:8080/qr.png?text={enc}&groesse=10\"'"],
                   check=True, timeout=60)
    subprocess.run(["ssh", "n8n-server", "docker cp n8n:/tmp/qr.png /tmp/qr.png"], check=True, timeout=60)
    subprocess.run(["scp", "-q", "n8n-server:/tmp/qr.png", a.qr], check=True, timeout=60)

    try:
        import cv2
        gelesen, _, _ = cv2.QRCodeDetector().detectAndDecode(cv2.imread(a.qr))
        print("   gegengeprueft:", "stimmt" if gelesen == link else f"ABWEICHUNG {gelesen!r}")
    except ImportError:
        print("   nicht gegengeprueft (cv2 fehlt)")

    print(f"""
Fertig: {a.titel}

  Formular (QR zeigt hierhin): {link}
  Live-Auswertung:             {GRAFANA}?var-umfrage={name}
  Tabelle:                     {NC}/dashboard
  QR-Code:                     {a.qr}

  Schutz: {'an, ' + str(len(nummern)) + ' Nummern' if a.geschuetzt else 'aus, offen fuer alle'}
  Umschaltbar in der Tabelle "Umfragen", der QR-Code bleibt gueltig.""")


if __name__ == "__main__":
    main()
