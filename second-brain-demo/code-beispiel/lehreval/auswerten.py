"""Zählt Themen in Freitexten und berechnet Mittelwerte."""
from statistics import mean

THEMEN = {
    "Tempo": ["schnell", "tempo", "zeit"],
    "Material": ["folien", "skript", "unterlagen"],
    "Praxis": ["übung", "beispiel", "praxis"],
}


def zaehle_themen(texte):
    """Zählt, wie viele Freitexte ein Thema ansprechen (Stichwortliste)."""
    ergebnis = {thema: 0 for thema in THEMEN}
    for text in texte:
        klein = text.lower()
        for thema, woerter in THEMEN.items():
            if any(w in klein for w in woerter):
                ergebnis[thema] += 1
    return ergebnis


def mittelwert(werte):
    """Mittelwert der Bewertungen (1 bis 5), gerundet auf eine Nachkommastelle."""
    zahlen = [int(w) for w in werte if str(w).strip()]
    return round(mean(zahlen), 1) if zahlen else None
