"""Kommandozeile: python3 main.py <csv>"""
import sys

from lehreval.anonymisieren import anonymisiere
from lehreval.auswerten import mittelwert, zaehle_themen
from lehreval.bericht import bericht
from lehreval.laden import lade_evaluation

BEKANNTE_NAMEN = ["Erika Musterfrau", "Max Mustermann"]


def main(pfad):
    zeilen = lade_evaluation(pfad)
    texte = [anonymisiere(z["freitext"], BEKANNTE_NAMEN) for z in zeilen]
    print(bericht("Lehrevaluation (Beispiel)", mittelwert(z["bewertung"] for z in zeilen), zaehle_themen(texte), texte))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "daten/evaluation_beispiel.csv")
