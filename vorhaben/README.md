<!-- AI-assisted: Claude (Fable 5.1), human-reviewed: ausstehend, Stand 18.09.2026 -->
# Vorhaben für die Hochschule: was man mit Claude, n8n und kleinen Diensten bauen kann

Ein Katalog zum Aussuchen, nicht zum Abarbeiten. Jedes Vorhaben hat dieselbe Bauform:
**Claude formuliert und ordnet, Code prüft, ein Mensch gibt frei.** Die Ampel sagt, welche
Daten im Spiel sind: grün (eigene und öffentliche Inhalte, jedes Konto), gelb (interne
Hochschulinformationen, nur THKI oder eigener Server), rot (personenbezogene Daten, nur mit
Vertrag, Freigabe und eigener Infrastruktur, oft besser gar nicht).

Spalte „Stand“: **gebaut** liegt in diesem Repository und läuft, **ausgearbeitet** ist mit Aufwand
und Bausteinen durchgerechnet (Foliensatz `folien/Ideenkatalog_Hochschule`), **Idee** ist eine
begründete Skizze.

## A: Für den eigenen Arbeitsplatz

| # | Vorhaben | Was es tut | Ampel | Bausteine | Stand, im Repository |
|---|---|---|---|---|---|
| 1 | **Persönlicher Assistent für den Posteingang** | Mails des Tages zusammenfassen, Fristen und Aufgaben herausziehen, Entwürfe für Antworten und eine kurze Statusmail schreiben; nichts wird ohne Klick verschickt | rot, weil Mails Personen betreffen: nur mit eigenem Server und lokalem Modell oder THKI, nie mit einem Verbraucherkonto | n8n (Mail lesen, Zeitplan), KI-Knoten, Freigabe per Knopf | Idee; Muster dazu: `n8n/dekanat-live-klammer.json` (Prüfschleife), Ideenkatalog „Posteingangs-Sortierer“ |
| 2 | **Second Brain: eigene Unterlagen als Wissensgraph** | Ordner mit Notizen, Skripten, Ordnungen wird zu einem Graphen, den man befragen kann: „Was hängt mit Prüfungsordnung §12 zusammen?“ | grün bis gelb, je nach Inhalt; läuft lokal | Graphify, Obsidian, Claude Code | gebaut als Demo: `second-brain-demo/`, Übung `diy/06_wissensgraph-bauen.md`, Kapitel 5 |
| 3 | **Folien nach eigenen Standards erzeugen** | Folien entstehen als Code mit festem Design, Quellenzeile je Folie, Tests, die fehlende Belege melden; der Sprechtext bleibt getrennt | grün | Claude Code, pptxgenjs, Skills mit den Regeln, Bauskript | gebaut, so entstand diese Reihe: `beispiel-skills/js-folien-schreiben`, `folien-pruefen`, `vortragssprache`; Folien in `folien/` |
| 4 | **Skills aufbauen, Plugins bauen und nutzen** | wiederkehrende Arbeit als Textdatei festhalten, im Team teilen, als Plugin installieren | grün | Claude Code | gebaut: `beispiel-skills/`, `plugins/hochschul-toolkit/`, Übung B und D, Kapitel 2 |
| 5 | **Nutzerstrategien: Regeln, Kontext, Tokens** | eigene CLAUDE.md, Skills und Regeln so aufbauen, dass Antworten besser und Sitzungen günstiger werden: was ins Regelwerk gehört, was in Skills, was man weglässt | grün | Claude Code | gebaut: `vorlagen/CLAUDE-global-vorher.md` und `-nachher.md`, Kapitel 1.8 (vier Schichten), Kapitel 1.9 (Kontext pflegen), Kapitel 8 |

## B: Für Lehre und Studierende

| # | Vorhaben | Was es tut | Ampel | Bausteine | Stand, im Repository |
|---|---|---|---|---|---|
| 6 | **Umfrage, datenschutzkonform, mit Auswertung** | anonyme Rückmeldung per QR-Code auf eigenem Server, Live-Bild, Zusammenfassung auf Knopfdruck, Zahlen von Code, Freitexte von der KI | gelb; kein Namensfeld, nichts beim Anbieter | n8n, NocoDB, Türsteher, Grafana | gebaut: `n8n/umfrage/`, Ablaufbild `n8n/umfrage/ablauf.svg` |
| 7 | **Vorlesungsfolien und Videos übersetzen** | Folien in eine zweite Sprache, Untertitel aus der Tonspur (Whisper), Fachbegriffe aus einem Glossar einheitlich; Ergebnis als zweite Datei, die ein Mensch gegenliest | grün, solange keine Studierenden zu sehen oder zu hören sind; sonst gelb | Whisper lokal, Claude, pptx-Werkzeuge, Glossar als Datei | Idee; Baustein: Transkription wie in `n8n/dekanat-live-klammer.json` (Sprachnachricht) |
| 8 | **Übungsblätter mit Musterlösung aus Lernzielen** | aus den Lernzielen eines Kapitels Aufgaben in drei Schwierigkeiten, dazu Musterlösung und Bewertungsraster, in der Vorlage der Lehrperson | grün | Claude Code, Skill mit Vorlage | ausgearbeitet: Ideenkatalog, Folie „Wofür an einer Hochschule“ |
| 9 | **Evaluationsfreitexte bündeln, jede Aussage belegt** | Freitexte einer Lehrevaluation zu Themen, je Thema Anzahl und Belegstellen, keine Zitate ohne Nummer | gelb; anonymisiert vorher | Code (Zahlen), KI (Themen), Prüfschleife | ausgearbeitet, dieselbe Prüfschleife wie in `n8n/umfrage/` |
| 10 | **Sprechstunden-Planer** | Anfragen per Formular, Vorschlag freier Zeiten aus dem Kalender, Bestätigung nach Klick | gelb (Namen der Studierenden), eigener Kalender | n8n, Kalender, Formular | ausgearbeitet: Ideenkatalog |
| 11 | **Auskunft mit Paragraf** | Fragen zur Prüfungsordnung beantworten, jede Antwort mit Paragraf und Zitat; was nicht in der Ordnung steht, wird nicht beantwortet | grün (Ordnung ist öffentlich) | RAG über die Ordnung, Belegprüfung durch Code | ausgearbeitet: Ideenkatalog; Unteragent `quellen-pruefer` in `.claude/agents/` |
| 12 | **Barrierefreiheit: Alternativtexte und Struktur** | Bildbeschreibungen für Folien und PDFs, Überschriftenstruktur prüfen, Kontraste melden | grün | Claude (Bild), Prüfskript | Idee |

## C: Für Verwaltung, Dekanat und Gremien

| # | Vorhaben | Was es tut | Ampel | Bausteine | Stand, im Repository |
|---|---|---|---|---|---|
| 13 | **Dokumentenvergleich: Modulhandbücher** | zwei Versionen eines Modulhandbuchs vergleichen, Unterschiede farbig markiert als PDF; Inhalte aus Jira oder Tabellen einsammeln und als Modulhandbuch in der Hochschulvorlage ausgeben | grün | Claude (Vergleich, Struktur), Code (Diff), Gotenberg (PDF), Jira-Anbindung über MCP | ausgearbeitet: Ideenkatalog „Modulhandbuch erzeugen“; PDF-Weg gebaut in `n8n/dekanat-serienbrief.json` |
| 14 | **Serienbrief als PDF mit QR-Code** | aus einer Tabelle je Zeile ein Brief in der Vorlage, als PDF, mit QR-Code zum Formular | grün bis gelb | n8n, Gotenberg, QR-Dienst | gebaut: `n8n/dekanat-serienbrief.json`, Sandbox in `n8n/sandbox/` |
| 15 | **Protokoll-Assistent für Gremien** | aus Aufnahme oder Stichpunkten ein Protokollentwurf in der Vorlage, Beschlüsse hervorgehoben, Aufgaben mit Verantwortlichen; der Entwurf geht an den Protokollführer, nie direkt ins Umlaufverfahren | gelb bis rot (Namen, Personalangelegenheiten): Whisper und Modell lokal | Whisper, Claude, Skill `gremien-protokoll` | gebaut als Skill: `plugins/hochschul-toolkit/skills/gremien-protokoll`; Ideenkatalog |
| 16 | **Antragsstraße** | Anträge per Formular statt Mail, Pflichtfelder prüft Code, unvollständige gehen mit Hinweis zurück, vollständige landen mit Zusammenfassung beim Sachbearbeiter | gelb | n8n, Formular, Code | ausgearbeitet: Ideenkatalog |
| 17 | **Anerkennung von Leistungen vorbereiten** | Modulbeschreibung der anderen Hochschule neben die eigene legen, Überschneidung in Prozent, Vorschlag mit Begründung; Entscheidung bleibt beim Ausschuss | gelb | Claude, Vorlage | ausgearbeitet: Ideenkatalog |
| 18 | **Kennzahlen-Cockpit** | Zahlen aus mehreren Quellen in einem Live-Bild, automatisch aktualisiert, mit Hinweis, woher jede Zahl kommt | gelb | Grafana, Postgres, n8n | Baustein gebaut: Grafana in `n8n/umfrage/grafana/`; Ideenkatalog |
| 19 | **Fristen- und Förderwächter** | Ausschreibungen und Fristen aus Newslettern und Seiten sammeln, nach Passung zum Fachbereich sortieren, wöchentliche Übersicht | grün | n8n (Zeitplan, Quellen), Claude (Passung) | Idee |
| 20 | **Onboarding neuer Kolleginnen und Kollegen** | ein Skill, der die ersten Wochen begleitet: wo was liegt, wen man fragt, welche Regeln gelten; aus den Unterlagen des Fachbereichs gebaut | gelb | Claude Code, Skill, Wissensgraph | Idee; Muster: `skript-tutor` in `.claude/skills/` |

## D: Für Forschung und Qualität

| # | Vorhaben | Was es tut | Ampel | Bausteine | Stand, im Repository |
|---|---|---|---|---|---|
| 21 | **Wissenschaftliche Veröffentlichungen bewerten** | Struktur, Belegdichte, Methodik und Reproduzierbarkeit nach einem festen Raster prüfen, jede Bewertung mit Textstelle; ersetzt kein Gutachten, bereitet es vor | grün (veröffentlichte Texte); bei Einreichungen gelb und Vertraulichkeit beachten | Claude, Raster als Skill, Unteragent `quellen-pruefer` | Idee; Bausteine: `.claude/agents/quellen-pruefer`, Kapitel 5 |
| 22 | **Literaturrecherche mit Belegpflicht** | Suchbegriffe, Treffer sichten, Zusammenfassung je Quelle, keine Aussage ohne DOI; Halluzinationen fallen an der Belegprüfung auf | grün | Claude, Code (DOI prüfen), Zitierstil | Idee; Zitierweg gebaut im Skript (`skript/`, IEEE mit Prüfung) |
| 23 | **Akkreditierungs- und Berichtsunterlagen zusammenstellen** | aus Modulhandbuch, Kennzahlen und Protokollen die Kapitel eines Berichts vorbereiten, Lücken markieren | gelb | Claude, Wissensgraph, Gotenberg | Idee |
| 24 | **Miro-Skill** | Ergebnisse eines Workshops vom Miro-Board holen, ordnen, als Protokoll oder Aufgabenliste ausgeben, oder umgekehrt Vorlagen auf das Board legen | gelb (Namen auf Klebezetteln) | Miro-Anbindung über MCP, Claude | Idee |

## E: Für Entwickler und Hackathons

| # | Vorhaben | Was es tut | Ampel | Bausteine | Stand |
|---|---|---|---|---|---|
| 25 | **Chatbot schneller und günstiger machen** | Zwischenspeicher für gleiche Fragen (Caching), kleinere Modelle für einfache Anfragen, große nur bei Bedarf, Messung vorher und nachher | grün | Claude API, Prompt-Caching, Messskript | Idee für einen Hackathon; Grundlagen in Kapitel 8 und im Konzeptanhang (Prompt Caching, Modellwahl) |
| 26 | **Loop mit Prüfschleife für längere Aufgaben** | eine Aufgabe, die viele Runden braucht, läuft mit Ziel, Prüfung und Abbruchregel von allein | grün | Claude Code, `/goal`, Prüfskript | gebaut: `loop-demo/`, Kapitel 7 |

## Wie man eines davon anfängt

1. **Prozessinventur** (`diy/07_prozessinventur.md`, Skill `prozessinventur`): Häufigkeit, Dauer,
   Prüfbarkeit, Datenklasse. Was selten ist oder nicht prüfbar, fällt raus.
2. **Ampel klären**, bevor irgendetwas gebaut wird. Rot heißt meistens: anders lösen oder lassen.
3. **Kleinster Schritt, der schon nützt**, mit einer Prüfung, die Code macht. Der Serienbrief war
   ein halber Tag und läuft seitdem.
4. **Sparring vor dem Bau**: `beispiel-skills/vortrag-sparring` für Lehrformate, `grilling` für alles
   andere. Widerspruch vor dem ersten Klick ist billiger als danach.
