# lehreval: Evaluationsfreitexte anonymisieren und auswerten

Kleines Beispielprojekt für Graft (Skript, Kapitel 5.4). Es liest Evaluationsfreitexte, entfernt Mailadressen, Matrikelnummern und bekannte Namen, zählt Themen und schreibt einen Markdown-Bericht.

```bash
python3 main.py daten/evaluation_beispiel.csv
python3 -m unittest -v
```

Die Beispieldaten sind vollständig erfunden.
