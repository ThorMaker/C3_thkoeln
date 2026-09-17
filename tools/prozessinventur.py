#!/usr/bin/env python3
"""Sortiert eine Prozessinventur nach Netto-Nutzen im ersten Jahr (Skript, Kapitel 8.3).

Aufruf: python3 tools/prozessinventur.py vorlagen/prozessinventur.csv
Potenzial pro Monat = Häufigkeit × Dauer × Automatisierbarkeit
Netto Jahr 1        = 12 × Potenzial − Einrichtung − 12 × Pflege
"""
import csv
import sys


def auswerten(pfad):
    zeilen = []
    with open(pfad, encoding="utf-8", newline="") as datei:
        for z in csv.DictReader(datei):
            potenzial = float(z["haeufigkeit_pro_monat"]) * float(z["dauer_minuten"]) * float(z["automatisierbarkeit"])
            netto = 12 * potenzial - float(z["einrichtung_minuten"]) - 12 * float(z["pflege_minuten_pro_monat"])
            hinweis = []
            if z["ampel"].strip().lower() == "rot":
                hinweis.append("rot: nicht mit Verbraucherdiensten")
            if z["risiko"].strip().lower() == "hoch":
                hinweis.append("hohes Risiko: nur mit menschlicher Freigabe")
            if z["pruefbarkeit"].strip().lower() == "schwer":
                hinweis.append("schwer prüfbar: Nutzen unsicher")
            zeilen.append((netto, potenzial, z["aufgabe"], "; ".join(hinweis) or "geeignet"))
    return sorted(zeilen, reverse=True)


def main():
    pfad = sys.argv[1] if len(sys.argv) > 1 else "vorlagen/prozessinventur.csv"
    print("| Rang | Aufgabe | Potenzial (Min./Monat) | Netto Jahr 1 (Std.) | Hinweis |")
    print("|---|---|---|---|---|")
    for rang, (netto, potenzial, aufgabe, hinweis) in enumerate(auswerten(pfad), 1):
        print(f"| {rang} | {aufgabe} | {potenzial:.0f} | {netto / 60:.1f} | {hinweis} |")


if __name__ == "__main__":
    main()
