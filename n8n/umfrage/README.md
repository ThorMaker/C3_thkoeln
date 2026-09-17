<!-- AI-assisted: Claude (Fable 5.1), human-reviewed: ausstehend, Stand 17.09.2026 -->
# Umfragen auf dem eigenen Server: anlegen, Live-Bild, Zusammenfassung auf Knopfdruck

Das ist die Strecke hinter dem QR-Code aus dem Kick-off. Alles läuft auf einem eigenen Server:
NocoDB als Tabelle und Formular, ein kleiner Türsteher-Dienst vor dem Formular, n8n zum Anlegen
und Zusammenfassen, Grafana als Live-Bild. Kein Airtable, kein Google, kein Namensfeld.

| Datei | Was sie tut |
|---|---|
| `n8n-umfrage-anlegen.json` | n8n-Workflow „Umfrage anlegen“: Formular für Lehrende, legt Tabelle, Formular, Zulassungsliste und QR-Code an |
| `n8n-umfrage-anlegen-formular.py` | erzeugt das erklärende Eingabeformular dieses Workflows (TH-Auftritt, CSS in `n8n_formular_css.txt`) |
| `n8n-umfrage-zusammenfassen.py`, `.json` | Workflow „Umfrage zusammenfassen“: Knopf in Grafana → KI fasst zusammen → Code prüft, dass jede Antwort belegt ist → Ergebnisseite |
| `tuersteher/` | der Dienst vor dem Formular: zeigt die Fragen, prüft optional die Matrikelnummer, speichert die Antwort ohne Kennung (Python, Standardbibliothek, Dockerfile) |
| `grafana/` | zwei Dashboards: Auswertung je Umfrage mit Knopf, Überblick über alle Umfragen |
| `ANLEITUNG-umfrage.md` | Bedienung für Lehrende, ohne Fachsprache |

**Zum Nachbauen** ersetzen Sie die Adressen (`nocodb.vibe-cortex.com`, `grafana.vibe-cortex.com`,
`n8n.vibe-cortex.com`) durch Ihre eigenen, legen in NocoDB eine Base an und tragen deren Kennung in
den Knoten „Konfiguration“ ein. Zugangsdaten stehen nirgends in diesen Dateien; die Workflows
verweisen nur auf Namen von Zugangsdateien in n8n („NocoDB API Token“, „th-assist“).

Warum so gebaut, mit Datenfluss und Entscheidungen: Kapitel 4 des Skripts und die Folie
„Der QR-Code: was dahinter läuft“ im Kick-off-Foliensatz (`folien/`).
