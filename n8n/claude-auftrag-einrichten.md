# Auftrag an Claude Code: Dekanats-Workflow in n8n einrichten

**So verwenden:** Claude Code im Handout-Repository starten (Code-Tab: Ordner `claude-hochschule-2026`), Modus **Plan** oder **Manual**, dann den Text unten einfügen. Voraussetzung: Der MCP-Server `n8n-mcp` ist verbunden (`claude mcp list`). Für die Sandbox `n8n-mcp` durch `n8n-sandbox` ersetzen; dort sind die Grenzen unten lockerer (siehe Variante am Ende).

---

```text
Ziel: Richte den Dekanats-Workflow aus diesem Repository in meiner n8n-Instanz ein,
über den MCP-Server „n8n-mcp“.

Kontext
- Workflow: n8n/dekanat-live-klammer.json (31 Knoten, getestet mit n8n 2.38)
- Tabellen, Spalten und manuelle Schritte: n8n/README.md
- Die Data-Table-Knoten verweisen per Name auf die Tabellen „termine“ und „rueckmeldungen“.

Vorgehen
1. Bestandsaufnahme, noch ohne Änderungen: Welche Werkzeuge bietet n8n-mcp
   (Workflows anlegen, Data Tables anlegen)? Welche n8n-Version läuft? Gibt es bereits
   Tabellen „termine“ oder „rueckmeldungen“ oder einen Workflow mit dem Namen aus der
   JSON-Datei? Berichte kurz und warte auf mein OK.
2. Lege die Data Tables „termine“ und „rueckmeldungen“ mit genau den Spalten aus
   n8n/README.md an, alle vom Typ Text. Existiert eine Tabelle schon, lege nichts doppelt an,
   sondern melde Abweichungen bei den Spalten.
3. Lege den Workflow aus n8n/dekanat-live-klammer.json an: Knoten, Verbindungen,
   Code und Einstellungen unverändert, Workflow inaktiv. Wenn dein Werkzeug die JSON-Datei
   nicht übernehmen kann und du den Workflow nachbauen müsstest, brich an dieser Stelle ab
   und sag es mir; dann importiere ich die Datei selbst über „Import from File“.
4. Prüfe das Ergebnis in n8n: 31 Knoten, alle Verbindungen wie in der Datei, drei
   Formular-Auslöser, die Data-Table-Knoten finden ihre Tabellen.
5. Gib mir eine Checkliste, was ich selbst erledigen muss: Zugangsdaten für KI-Anbieter,
   Transkription und SMTP anlegen und in den betroffenen Knoten auswählen (nenne die
   Knoten), Knoten „Konfiguration“ anpassen (Adressen, Modell), Workflow aktivieren,
   Formular-URLs notieren.

Grenzen
- Ändere, aktiviere, lösche oder starte keine anderen Workflows.
- Lege keine Zugangsdaten an und frage mich nicht nach Schlüsseln oder Passwörtern.
- Führe den neuen Workflow nicht aus und verschicke keine Mails.
- Ändere keine Dateien in diesem Repository.

Fertig, wenn beide Tabellen und der Workflow in n8n existieren, der Workflow inaktiv ist,
die Prüfung aus Schritt 4 bestanden ist und die Checkliste vorliegt.
```

---

## Variante für die Sandbox

In der Sandbox (`n8n-sandbox`) darf Claude mehr. Ersetzen Sie den Abschnitt „Grenzen“ durch:

```text
Grenzen
- Arbeite ausschließlich über n8n-sandbox, niemals über n8n-mcp.
- Du darfst den Workflow aktivieren und mit den Beispieldaten aus
  n8n/beispieldaten/ testen; Mails landen im Test-Mailserver.
- Lege keine echten Zugangsdaten an; nutze nur, was in der Sandbox schon eingerichtet ist.
- Ändere keine Dateien in diesem Repository.
Fertig, wenn ein Probelauf mit drei Rückmeldungen eine Zusammenfassung erzeugt hat,
in der alle IDs vorkommen, und du mir die Execution-ID nennst.
```

## Warum dieser Ordner

Claude braucht die Workflow-Datei und die Anleitung aus diesem Repository; lokal ändert es nichts. Der Ordner begrenzt aber nicht, was auf dem n8n-Server passiert. Dort schützen die Freigabe einzelner Workflows für MCP, die Rückfragen vor jedem Werkzeugaufruf und, für freie Experimente, die Sandbox (`n8n/sandbox/`).
