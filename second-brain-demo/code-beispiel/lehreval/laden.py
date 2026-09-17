"""Liest Evaluationsdaten aus einer CSV-Datei."""
import csv
from pathlib import Path


def lade_evaluation(pfad):
    """Gibt eine Liste von Dictionaries mit den Spalten der CSV zurück."""
    with Path(pfad).open(encoding="utf-8", newline="") as datei:
        return list(csv.DictReader(datei))
