"""Erzeugt einen Markdown-Bericht."""


def bericht(titel, mittel, themen, beispiele):
    zeilen = [f"# {titel}", "", f"Mittlere Bewertung: {mittel}", "", "| Thema | Anzahl |", "|---|---|"]
    zeilen += [f"| {t} | {n} |" for t, n in themen.items()]
    zeilen += ["", "## Anonymisierte Beispiele", ""] + [f"- {b}" for b in beispiele[:3]]
    return "\n".join(zeilen) + "\n"
