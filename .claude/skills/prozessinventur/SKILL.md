---
name: prozessinventur
description: Führt durch eine Prozessinventur für Lehre, Forschung oder Verwaltung, bewertet Aufgaben nach Häufigkeit, Dauer, Automatisierbarkeit, Prüfbarkeit, Risiko und Datenklasse und berechnet den Netto-Nutzen. Verwenden, wenn jemand Automatisierungskandidaten finden, Zeitgewinne abschätzen oder priorisieren möchte.
---

# Prozessinventur

1. Bitte um bis zu zehn wiederkehrende Aufgaben. Frage je Aufgabe nach: Häufigkeit pro Monat, Dauer in Minuten, Anteil Muster statt Urteil (0 bis 1), Prüfbarkeit (leicht, mittel, schwer), Risiko bei Fehlern (gering, mittel, hoch), Datenklasse nach der Ampel (grün, gelb, rot), geschätzte Einrichtung und Pflege in Minuten.
2. Trage alles in eine Kopie von `vorlagen/prozessinventur.csv` ein und zeige sie.
3. Führe `python3 tools/prozessinventur.py <datei>` aus und zeige die sortierte Tabelle.
4. Empfiehl die drei besten Kandidaten mit je einem Werkzeug (Skill, n8n-Workflow, Loop) und einer prüfbaren Erfolgsbedingung.
5. Weise auf rote Datenklassen und hohe Risiken ausdrücklich hin.

Rechne nicht im Kopf; nutze das Werkzeug. Keine personenbezogenen Daten in die Tabelle.
