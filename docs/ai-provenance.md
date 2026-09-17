# AI-Provenienz

Welche Dateien mit KI-Unterstützung entstanden sind, wofür, und ob ein Mensch sie geprüft hat. Einzelne Änderungen stehen in den Commits (`Co-Authored-By: Claude`), `git log --follow <datei>` zeigt sie.

| Datum | Pfad | Wofür | Review-Status |
|---|---|---|---|
| 2026-09-11 | `live-monitor/buero.html` | Büro-Ansicht neu: ein Raum je Projekt, Kamera mit Zoom, Rollen, Barista, Prüf-Krabbe, anklickbare Blasen, Verlauf, Kennzahlen (Claude Fable 5.1) | entfernt 12.09.2026, der Monitor bleibt beim Dozenten (vorher: ausstehend) |
| 2026-09-12 | `live-monitor/buero.html` (zweite Fassung) | Gebäude in Seitenansicht, ein Stockwerk je Projekt, Pixel-Figuren und Pixel-Möbel aus `pixel.py`, Feuer und Debugger, Orchestrator, Hochkant-Modus, Verlauf nach Arbeitsart (Claude Fable 5.1) | entfernt 12.09.2026, der Monitor bleibt beim Dozenten (vorher: ausstehend) |
| 2026-09-11 | `live-monitor/server.py`, Funktion `tokens_zaehlen` und `/api/tokens` | Tokens je Sitzung aus den lokalen Transkripten (Claude Fable 5.1) | entfernt 12.09.2026, der Monitor bleibt beim Dozenten (vorher: ausstehend) |
| 2026-09-11 | `live-monitor/demo_sitzung.jsonl`, drittes Projekt „forschung-auswertung“ | Demo mit drei Räumen, Daten-Rolle, Außenkontakt und Prüf-Helfer (Claude Fable 5.1) | entfernt 12.09.2026, der Monitor bleibt beim Dozenten (vorher: ausstehend) |
| 2026-09-11 | `live-monitor/server.py`, `POST /demo`, und `live-monitor/start.py` | Demo im laufenden Dienst abspielen, damit `./vortrag.sh monitor-demo` neben der App funktioniert (Claude Fable 5.1) | entfernt 12.09.2026, der Monitor bleibt beim Dozenten (vorher: ausstehend) |
| 2026-09-11 | `live-monitor/installieren.py`, App-Startskript | App öffnet direkt das Büro (Claude Fable 5.1) | entfernt 12.09.2026, der Monitor bleibt beim Dozenten (vorher: ausstehend) |
| 2026-09-11 | `live-monitor/app.swift` und `installieren.py`, Funktion `app_kompilieren` | eigene Mac-App mit WebKit-Fenster, Menü, „Immer im Vordergrund“ (Claude Fable 5.1) | entfernt 12.09.2026, der Monitor bleibt beim Dozenten (vorher: ausstehend) |
| 2026-09-11 | `docs/ai-provenance.md` | diese Liste (Claude Fable 5.1) | ausstehend |
| 2026-09-12 | `live-monitor/buero.html` (dritte Fassung) | Nachtpalette, sechs Raumtypen mit Pixel-Materialien, Außenwelt mit Himmel, Skyline, Dach und Straße (Claude Fable 5.1) | entfernt 12.09.2026, der Monitor bleibt beim Dozenten (vorher: ausstehend) |
| 2026-09-12 | `live-monitor/index.html` (zweite Fassung) | Detailansicht nach Projekt, Datei und Änderung: Dateiliste, Diff-Verlauf je Datei, Sitzungen (Claude Fable 5.1) | entfernt 12.09.2026, der Monitor bleibt beim Dozenten (vorher: ausstehend) |
| 2026-09-12 | `n8n/dekanat-serienbrief.json` (erzeugt aus `werkzeuge/n8n_serienbrief.py` im Dozenten-Repo) | Beispiel-Workflow: Serienbrief als PDF mit QR-Code über Gotenberg und QR-Dienst, Haftnotizen mit User Story und Technik (Claude Fable 5.1) | ausstehend |
| 2026-09-12 | `n8n/sandbox/qr-dienst/qr_dienst.py`, `Dockerfile`; `n8n/sandbox/docker-compose.yml` (Dienste gotenberg, qr-dienst) | QR-Dienst als Mini-Dienst der Sandbox, Gotenberg als PDF-Dienst (Claude Fable 5.1) | ausstehend |
| 2026-09-13 | `skript/01_grundlagen_und_datenschutz.md`, Abschnitt 1.14 (erzeugt aus dem Dozenten-Repo) | Vier Schichten Prompt, Kontext, Harness, Loop mit Beispielen aus dem Hochschulalltag (Claude Opus 5) | ausstehend |
| 2026-09-13 | `diagramme/k01_tokenisierung.png` bis `k20_llm_as_a_judge.png` | 20 Diagramme zum Konzept-Anhang, eigene Entwürfe im TH-Stil (Claude Opus 5) | ausstehend |
| 2026-09-13 | `vorlagen/konzepte.md`, `vorlagen/Konzepte.pdf` | Anhang „Konzepte der KI-Technik“ zum Mitnehmen: je Konzept Bild, Wofür, Wann sinnvoll, Grenze, Quellen im IEEE-Stil (Claude Opus 5) | ausstehend |
| 2026-09-13 | `vorlagen/konzepte.md`, `vorlagen/Konzepte.pdf` (zweite Fassung) | je Konzept zusätzlich Herkunft, Wirkweise, Belegstand und Abgrenzung; 26 statt 16 Seiten (Claude Opus 5) | ausstehend |
| 2026-09-13 | `vorlagen/konzepte.md`, `vorlagen/Konzepte.pdf` (dritte Fassung) | von 20 auf 39 Konzepte erweitert, fünf Gruppen, Seitenumbruch je Konzept; umbenannt von `20-konzepte`, weil die Zahl wächst (Claude Opus 5) | ausstehend |
| 2026-09-13 | `diagramme/k21` bis `k39` | 15 weitere Diagramme; vier Konzepte nutzen vorhandene Abbildungen aus dem Skript (Claude Opus 5) | ausstehend |
| 2026-09-13 | `vorlagen/weiterlernen.md`, `vorlagen/Weiterlernen.pdf` | Kursempfehlungen: Elements of AI, AI for Everyone, Google, Claude Academy, KI-Campus, Hochschulforum, THKI, Andrew Ng, Stanford CS329A; je Eintrag Aufwand, Sprache, Kosten und Abgrenzung (Claude Opus 5) | ausstehend |
| 2026-09-13 | `vorlagen/konzepte.md`, `Konzepte.pdf` (vierte Fassung) | 40 Konzepte, Lesereihenfolge nach Abhängigkeit, Querverweise mit Kartennummer, korrigierte Abbildungen (Claude Opus 5) | ausstehend |
| 2026-09-13 | `vorlagen/konzepte.md`, `Konzepte.pdf` | 41. Konzept „Lesen auslagern“ (Claude Opus 5) | ausstehend |
| 2026-09-13 | `skript/01_grundlagen_und_datenschutz.md` | Teil A und Teil B getauscht, Abschnitte neu nummeriert; alle Verweise im Handout mitgezogen (Claude Opus 5) | ausstehend |
