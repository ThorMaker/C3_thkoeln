#!/usr/bin/env python3
"""Messglied der Loop-Demo (Stufe 1 der Verifikationsleiter, Skript Kapitel 7).

Prüft loop-demo/zusammenfassung.md gegen loop-demo/daten/rueckmeldungen.json:
Pflichtabschnitte, Zahlen im Überblick, alle IDs, keine erfundenen IDs, Länge,
und ob die Daten unverändert sind. Exit-Code 0 = bestanden, 1 = nicht bestanden.
"""
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

BASIS = Path(__file__).resolve().parent
DATEN = BASIS / "daten" / "rueckmeldungen.json"
ZIEL = BASIS / "zusammenfassung.md"
ABSCHNITTE = ["## Überblick", "## Anmerkungen", "## Offene Punkte"]
ARTEN = ["Zusage", "Absage", "Vielleicht", "Feedback"]
MAX_WORTE = 300
DATEN_SHA256 = "e50c8610c3264a5ac7164fb561b493dc670fef974b5380eb836a26d4f93b4a6d"


def pruefe(text, roh):
    fehler = []
    if hashlib.sha256(roh.encode("utf-8")).hexdigest() != DATEN_SHA256:
        fehler.append("Die Datendatei wurde verändert. Das ist nicht erlaubt.")
    daten = json.loads(roh)
    for abschnitt in ABSCHNITTE:
        if abschnitt not in text:
            fehler.append(f"Abschnitt fehlt: {abschnitt}")
    erwartet = {d["id"] for d in daten}
    gefunden = set(re.findall(r"R-[A-Z0-9]{5}", text))
    fehler += [f"ID fehlt: {i}" for i in sorted(erwartet - gefunden)]
    fehler += [f"ID erfunden: {i}" for i in sorted(gefunden - erwartet)]
    zaehlung = Counter(d["antwort"] for d in daten)
    for art in ARTEN:
        treffer = re.search(rf"{art}:\s*(\d+)", text)
        if not treffer:
            fehler.append(f"Zahl fehlt im Überblick, erwartet wird die Form '{art}: <Anzahl>'")
        elif int(treffer.group(1)) != zaehlung.get(art, 0):
            fehler.append(f"Zahl falsch: {art} ist {zaehlung.get(art, 0)}, nicht {treffer.group(1)}")
    worte = len(re.findall(r"\w+", text))
    if worte > MAX_WORTE:
        fehler.append(f"Zu lang: {worte} Wörter, erlaubt sind {MAX_WORTE}")
    return fehler, len(erwartet), len(gefunden & erwartet)


def main():
    if not ZIEL.exists():
        print(f"NICHT BESTANDEN: {ZIEL.name} fehlt.")
        return 1
    fehler, soll, ist = pruefe(ZIEL.read_text(encoding="utf-8"), DATEN.read_text(encoding="utf-8"))
    print(f"IDs belegt: {ist} von {soll}")
    if fehler:
        print("NICHT BESTANDEN:")
        for f in fehler:
            print("  -", f)
        return 1
    print("BESTANDEN: alle Prüfungen erfüllt.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
