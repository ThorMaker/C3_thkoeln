#!/usr/bin/env python3
"""PreToolUse-Hook für Claude Code: blockiert Änderungen in geschützten Ordnern.

Claude Code übergibt die geplante Aktion als JSON auf der Standardeingabe.
Exit-Code 2 blockiert die Aktion; die Meldung auf stderr geht an Claude zurück.
Achtung: Exit-Code 1 blockiert NICHT, er gilt als nicht blockierender Fehler.
"""
import json
import sys

GESCHUETZT = ("personendaten/", "pruefungen/")

daten = json.load(sys.stdin)
pfad = str(daten.get("tool_input", {}).get("file_path", "")).replace("\\", "/")

if any(ordner in pfad for ordner in GESCHUETZT):
    print(f"Blockiert: {pfad} liegt in einem geschützten Ordner. "
          "Diese Dateien bearbeitet nur ein Mensch.", file=sys.stderr)
    sys.exit(2)
sys.exit(0)
