"""Entfernt personenbezogene Angaben aus Freitexten."""
import re

MAIL = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")
MATRIKEL = re.compile(r"\b\d{7,8}\b")


def anonymisiere(text, namen=()):
    """Ersetzt Mailadressen, Matrikelnummern und bekannte Namen durch Platzhalter."""
    text = MAIL.sub("[MAIL]", text)
    text = MATRIKEL.sub("[MATRIKEL]", text)
    for name in namen:
        text = re.sub(rf"\b{re.escape(name)}\b", "[NAME]", text)
    return text
