"""Literaturliste: sortiert und formatiert Literaturangaben.

Beispielprojekt für den Vortrag. Es enthält absichtlich zwei Fehler,
die Claude Code in der Live-Demo findet und im Plan-Modus behebt.
Aufruf: python3 literaturliste.py daten/literatur.json
"""
import json
import sys
from pathlib import Path


def lade(pfad):
    """Liest Literaturangaben aus einer JSON-Datei."""
    return json.loads(Path(pfad).read_text(encoding="utf-8"))


def sortiere(eintraege):
    """Sortiert nach Autor und Jahr (ABC-Regeln nach DIN 5007-1)."""
    return sorted(eintraege, key=lambda e: (e["autor"], e.get("jahr", 0)))


def formatiere(eintrag):
    """Formatiert einen Eintrag: Autor (Jahr). Titel."""
    return f"{eintrag['autor']} ({eintrag['jahr']}). {eintrag['titel']}."


def main(pfad):
    for eintrag in sortiere(lade(pfad)):
        print(formatiere(eintrag))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "daten/literatur.json")
