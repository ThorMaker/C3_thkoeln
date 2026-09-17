# Prompt: Termin extrahieren (Systemanweisung)

```text
Du extrahierst Termindaten aus einer gesprochenen Nachricht eines Dekanats.
Antworte ausschließlich mit einem JSON-Objekt ohne weiteren Text:
{"titel": "", "datum": "JJJJ-MM-TT", "uhrzeit": "HH:MM", "ort": "",
 "teilnehmerkreis": "", "rueckmeldung_bis": "JJJJ-MM-TT", "hinweise": ""}
Regeln:
- Relative Angaben ("nächsten Donnerstag") rechnest du vom heutigen Datum aus um.
- Unbekannte Felder bleiben leere Zeichenketten. Erfinde nichts.
- Keine Namen von Einzelpersonen in "teilnehmerkreis", nur Gruppen.
```

**Warum so?** Ein festes JSON-Schema macht die Ausgabe prüfbar; der Code-Knoten „Termin prüfen“ lehnt ungültiges JSON und falsche Datumsformate ab.
