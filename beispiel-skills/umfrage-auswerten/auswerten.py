#!/usr/bin/env python3
# AI-assisted: Claude, human-reviewed ausstehend, Stand 2026-09-17
"""Liest Antworten einer Umfrage und steuert sie (Schutz, offen/zu, Nummern)."""
import argparse, json, re, statistics, subprocess, sys, urllib.error, urllib.request

NC = "https://nocodb.vibe-cortex.com"
STEUER = "mxnrok36754lt25"
UNSICHTBAR = {"Id", "CreatedAt", "UpdatedAt", "nc_order", "eingang"}


def token():
    r = subprocess.run(["ssh", "n8n-server", "cat ~/.nocodb_api_token"],
                       capture_output=True, text=True, timeout=30)
    if not r.stdout.strip():
        sys.exit("Kein NocoDB-Token erreichbar.")
    return r.stdout.strip()


def api(tok, pfad, daten=None, methode=None):
    req = urllib.request.Request(
        NC + pfad, data=json.dumps(daten).encode() if daten is not None else None,
        headers={"xc-token": tok, "Content-Type": "application/json"},
        method=methode or ("POST" if daten is not None else "GET"))
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"NocoDB {e.code} auf {pfad}: {e.read().decode()[:300]}")


def alle_zeilen(tok, tabelle):
    aus, seite = [], 0
    while True:
        teil = api(tok, f"/api/v2/tables/{tabelle}/records?limit=1000&offset={seite*1000}")
        aus += teil.get("list", [])
        if len(teil.get("list", [])) < 1000:
            return aus
        seite += 1


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--liste", action="store_true")
    p.add_argument("--kennung")
    p.add_argument("--schutz", choices=["an", "aus"])
    p.add_argument("--zu", action="store_true")
    p.add_argument("--auf", action="store_true")
    p.add_argument("--nummern-datei")
    a = p.parse_args()
    tok = token()
    umfragen = api(tok, f"/api/v2/tables/{STEUER}/records?limit=200").get("list", [])

    if a.liste or not a.kennung:
        print("Umfragen auf dem Server:\n")
        for u in umfragen:
            print(f"  {u['kennung']:34} {u['titel']}")
            print(f"  {'':34} Schutz: {'an' if u.get('geschuetzt') else 'aus'}"
                  f"   Status: {'offen' if u.get('offen') else 'zu'}")
        if not a.kennung:
            return

    u = next((x for x in umfragen if x["kennung"] == a.kennung), None)
    if not u:
        sys.exit(f"Keine Umfrage mit der Kennung {a.kennung}. Mit --liste nachsehen.")

    # --- Steuern
    aenderung = {}
    if a.schutz:
        aenderung["geschuetzt"] = (a.schutz == "an")
    if a.zu:
        aenderung["offen"] = False
    if a.auf:
        aenderung["offen"] = True
    if aenderung:
        api(tok, f"/api/v2/tables/{STEUER}/records", {"Id": u["Id"], **aenderung}, methode="PATCH")
        print("Geaendert:", ", ".join(f"{k}={v}" for k, v in aenderung.items()))
        print("Der QR-Code bleibt gueltig.")
    if a.nummern_datei:
        text = open(a.nummern_datei, encoding="utf-8").read()
        da = {z["matrikelnummer"] for z in alle_zeilen(tok, u["zulassung_tabelle"])}
        neu = []
        for s in re.split(r"[\n,;]+", text):
            n = s.strip().strip("\"'")
            if re.fullmatch(r"[0-9]{3,20}", n) and n not in da:
                da.add(n)
                neu.append({"matrikelnummer": n})
        if neu:
            api(tok, f"/api/v2/tables/{u['zulassung_tabelle']}/records", neu)
        print(f"{len(neu)} neue Nummern eingetragen.")
    if aenderung or a.nummern_datei:
        return

    # --- Auswerten
    zeilen = alle_zeilen(tok, u["antwort_tabelle"])
    print(f"\n{u['titel']}")
    print(f"Kennung {u['kennung']} | Schutz {'an' if u.get('geschuetzt') else 'aus'} | "
          f"{'offen' if u.get('offen') else 'geschlossen'}")
    print(f"\nAntworten: {len(zeilen)}")

    if u.get("zulassung_tabelle"):
        zul = alle_zeilen(tok, u["zulassung_tabelle"])
        if zul:
            fertig = sum(1 for z in zul if z.get("abgestimmt"))
            print(f"Beteiligung: {fertig} von {len(zul)} zugelassenen "
                  f"({round(100 * fertig / len(zul))} Prozent)")
    if not zeilen:
        print("\nNoch keine Antwort eingegangen.")
        return

    felder = [k for k in zeilen[0] if k not in UNSICHTBAR and not k.startswith("__")]
    for f in felder:
        werte = [z[f] for z in zeilen if z.get(f) not in (None, "")]
        if not werte:
            continue
        print(f"\n--- {f}  ({len(werte)} Angaben)")
        if all(isinstance(w, (int, float)) and not isinstance(w, bool) for w in werte):
            print(f"    Durchschnitt {statistics.mean(werte):.2f}"
                  f" | Mitte {statistics.median(werte)}"
                  f" | Streuung {statistics.pstdev(werte):.2f}"
                  f" | von {min(werte)} bis {max(werte)}")
            for w in sorted(set(werte)):
                n = werte.count(w)
                print(f"    {w}: {'#' * n} {n}")
        elif len(set(map(str, werte))) <= 12:
            for w, n in sorted(((w, list(map(str, werte)).count(w)) for w in set(map(str, werte))),
                               key=lambda x: -x[1]):
                print(f"    {w}: {'#' * n} {n}")
        else:
            for w in werte:
                print(f"    - {str(w)[:300]}")


if __name__ == "__main__":
    main()
