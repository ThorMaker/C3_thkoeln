# Aufgabenkarte F: Ein echter Fehler im Plan-Modus

**Ziel:** die Schleife lesen, planen, handeln, beobachten an einem echten Fehler erleben. **Dauer:** 15 Minuten. **Ausführlich:** Skript, Kapitel 2.2 und 3.7.

## Schritte
1. Handout-Repository im Code-Tab öffnen, Modus **Manual**.
2. Eingeben: „In beispiele/literaturliste schlagen Tests fehl. Finde die Ursache. Ändere noch nichts.“
3. Modus **Plan**: Lösung vorschlagen lassen. Prüfen: Sortierregel genannt? Tests unverändert?
4. Plan freigeben; Claude ändert `literaturliste.py` und führt die Tests erneut aus.
5. Diff ansehen.

## Erwartetes Ergebnis
Alle vier Tests bestehen; `python3 literaturliste.py daten/literatur.json` sortiert „Özdemir“ zwischen „Luhmann“ und „TH Köln“ ein.

## Zurücksetzen
Mit Git: `git checkout -- beispiele/literaturliste`. Ohne Git: ZIP erneut entpacken.
