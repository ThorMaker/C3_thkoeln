# C3: Claude Code Club an der TH Köln

Unterlagen zur Reihe **„Claude Code, Automatisierung, Wissen“**. Kick-off am 18. September 2026,
weitere Termine nach Bedarf der Teilnehmenden.

Dieses Repository ist Skript, Folien, Übungsprojekt und Werkzeugkasten zugleich. Öffnen Sie es in
Claude Code, und Claude erklärt Ihnen die Inhalte, stellt Verständnisfragen und begleitet die
Übungen. Sie müssen dafür nicht programmieren können.

## Schnellstart in drei Minuten

1. **Herunterladen:** oben auf „Code“ und „Download ZIP“ klicken, ZIP entpacken.
   Mit Git: `git clone https://github.com/ThorMaker/C3_thkoeln.git`
2. **Öffnen:** Claude Desktop starten, Tab **Code**, Umgebung **Local**, den entpackten Ordner als
   Projektordner wählen, Modus **Manual**.
3. **Loslegen:** eingeben: `Erkläre mir dieses Repository in fünf Sätzen. Ändere nichts.`

Voraussetzungen: Claude Desktop mit Pro-Konto (oder höher). Unter Windows zusätzlich Git for Windows.

## Wenn Sie nur eines lesen

`vorlagen/konzepte.md`: **41 Konzepte der KI-Technik**, jedes mit Bild, wofür es gut ist, wann es sich
lohnt, wo die Grenze liegt, und mit Quellen. Vier Teile: wie man damit arbeitet, wie ein Modell rechnet,
wie es das Richtige findet, wie man es anbindet. Auch als PDF: `vorlagen/Konzepte.pdf`.

## Folien

Alle Foliensätze liegen in `folien/`, als PowerPoint und als PDF, ohne Sprechtext.

| Datei | Inhalt |
|---|---|
| `Kickoff_2026-09-18` | der Kick-off, so wie er gehalten wurde (ausgeblendete Folien sind Reserve, die nicht dran war) |
| `Alle_Folien_Gesamt` | der komplette Satz aller Themen, mit Kapiteln je Thema in der Foliensortierung |
| `Folge1_…`, `Folge2_…`, `Folge3_…` | die drei Vormittage der Reihe: verstehen und anfangen, selber bauen, vertiefen |
| `Ideenkatalog_Hochschule` | zwölf durchgerechnete Vorhaben für Lehre und Verwaltung, mit Aufwand und Nutzen |
| `Konzepte_Anhang` | die 41 Konzepte als Folien |

Zu jeder Inhaltsfolie gehört eine Quellenzeile, das Verzeichnis steht am Ende jedes Satzes.

## Empfohlener Weg durch die Unterlagen

Wer die Reihe allein nachvollziehen will, arbeitet in dieser Reihenfolge; jeder Schritt baut auf dem
vorigen auf und ist in unter einer Stunde machbar.

| # | Schritt | Wo | Dauer |
|---|---|---|---|
| 1 | Einstellungen richtig setzen | `vorlagen/Datenschutz_in_5_Minuten.pdf`, `vorlagen/datenschutz-checkliste.md` | 10 Min |
| 2 | Skript Kapitel 1 lesen: Agent, Daten, Ampel | `skript/01_grundlagen_und_datenschutz.md` | 30 Min |
| 3 | Eigene Regeldatei anlegen | `vorlagen/CLAUDE-global-vorher.md` und `-nachher.md`, `vorlagen/CLAUDE-projekt-vorlage.md` | 20 Min |
| 4 | Repository erkunden, erster Fehler im Plan-Modus | `diy/01_…`, `diy/04_…`, `beispiele/literaturliste/` | 20 Min |
| 5 | Ersten eigenen Skill bauen | `diy/02_eigener-skill.md`, `vorlagen/skill-vorlage/` | 30 Min |
| 6 | Plugin installieren und ausprobieren | `plugins/hochschul-toolkit/README.md` | 10 Min |
| 7 | Einen Ablauf in n8n importieren | `n8n/README.md`, `diy/05_…`, Sandbox in `n8n/sandbox/` | 45 Min |
| 8 | Wissensgraph aus eigenen Unterlagen | `diy/06_…`, `second-brain-demo/` | 20 Min |
| 9 | Eigenen Fall finden: Prozessinventur | `diy/07_…`, `tools/`, Kapitel 8 | 20 Min |
| 10 | Aufgaben, die länger laufen: Loop | `diy/08_…`, `loop-demo/`, Kapitel 7 | 20 Min |

Die Aufgaben zwischen den Terminen stehen in `aufgaben/`, mit Hinweisen, aber bewusst ohne Lösung.

## Beispiel-Workflows

| Ordner | Was drin ist |
|---|---|
| `n8n/dekanat-live-klammer.json` | der durchgehende Fall aus Folge 1: Termin per Sprachnachricht anlegen, Rückmeldungen sammeln, Zusammenfassung mit Prüfschleife (Airtable) |
| `n8n/dekanat-serienbrief.json` | Serienbrief als PDF mit QR-Code, über kleine Dienste (Gotenberg, QR) |
| `n8n/umfrage/` | die Strecke hinter dem QR-Code des Kick-offs: Umfrage anlegen, Türsteher, Live-Bild in Grafana, Zusammenfassung auf Knopfdruck, alles auf eigenem Server |
| `n8n/claude-auftrag-einrichten.md` | fertiger Auftrag an Claude Code, einen Workflow über die Schnittstelle einzurichten |
| `n8n/sandbox/` | abgeschottete n8n-Instanz mit Docker, in der Claude alles ausprobieren darf |

Jeder Workflow trägt seine Beschreibung als Notiz im Workflow selbst (User Story und Technik).

## Inhalt im Überblick

| Ordner | Inhalt |
|---|---|
| `folien/` | alle Foliensätze, PowerPoint und PDF, ohne Sprechtext |
| `skript/` | das Skript als Markdown; Kapitelnummer = Block im Vortrag, jedes Kapitel mit Quellenverzeichnis |
| `vorlagen/` | Konzepte (41, mit Quellen), Glossar, Kursempfehlungen, CLAUDE.md vorher und nachher, Datenschutz-Profil, Leitplanken, Skill-Vorlage, Starter-Prompts |
| `aufgaben/` | die Aufgaben zwischen den Terminen |
| `diy/` | Aufgabenkarten für die Übungen |
| `demo-ordner/` | zweimal derselbe Ordner, einmal mit und einmal ohne `CLAUDE.md` |
| `beispiele/literaturliste/` | kleines Python-Projekt mit zwei absichtlichen Fehlern |
| `beispiel-skills/` | sieben Skills, die beim Bauen dieser Reihe im Einsatz waren, zum Kopieren und Lesen: Sparringspartner, Folienregeln, Umfrage anlegen und auswerten |
| `.claude/skills/`, `.claude/agents/` | Projekt-Skills (`skript-tutor`, `mail-dekanat`, `handover`, `prozessinventur`) und der Unteragent `quellen-pruefer` |
| `plugins/hochschul-toolkit/` | Beispiel-Plugin mit Skills für Gremienprotokolle und Lehrveranstaltungs-Feedback |
| `.claude-plugin/marketplace.json` | macht dieses Repository zu einem Plugin-Marketplace |
| `n8n/` | die Beispiel-Workflows, siehe oben |
| `second-brain-demo/` | fiktiver Notizkorpus für Graphify und Code-Beispiel für Graft |
| `loop-demo/` | Loop mit `/goal` und deterministischem Prüfskript |
| `zusammenarbeit/` | Team-Repository-Vorlage mit ADRs und gemeinsamen Leitplanken |
| `tools/` | QR-Code-Erzeuger, Prozessinventur-Auswertung |
| `diagramme/` | Abbildungen aus Skript und Vortrag |

## Übungen

| Übung | Dauer | Karte | Skript |
|---|---|---|---|
| A: Repository erkunden | 5 Min | `diy/01_claude-code-in-10-minuten.md` | Kapitel 3.2 |
| B: Erster eigener Skill | 10 Min | `diy/02_eigener-skill.md` | Kapitel 3.3 |
| C: Globale CLAUDE.md und Datenschutz-Profil | 10 Min | `vorlagen/` | Kapitel 3.4 |
| D: Plugin installieren | 10 Min | `plugins/hochschul-toolkit/README.md` | Kapitel 3.5 |
| E: Übergabe und `/clear` | 10 Min | `diy/03_uebergabe-und-clear.md` | Kapitel 3.6 |
| F: Ein echter Fehler im Plan-Modus | 15 Min | `diy/04_fehler-im-planmodus.md` | Kapitel 3.7 |
| G: Dekanats-Workflow in n8n | 30 Min | `diy/05_n8n-workflow-importieren.md` | Kapitel 4 |
| H: Wissensgraph bauen | 20 Min | `diy/06_wissensgraph-bauen.md` | Kapitel 5 |
| I: Prozessinventur | 20 Min | `diy/07_prozessinventur.md` | Kapitel 8 |
| J: Loop mit `/goal` | 15 Min | `diy/08_loop-mit-goal.md` | Kapitel 7 |
| K: Team-Repository | 20 Min | `diy/09_team-repo.md` | Kapitel 6 |

## Plugin aus diesem Repository installieren

```bash
claude plugin marketplace add ThorMaker/C3_thkoeln
claude plugin install hochschul-toolkit@hochschule-2026
```

## Quellen

Jedes Skriptkapitel hat ein eigenes Quellenverzeichnis im IEEE-Stil; Webquellen tragen das Abrufdatum.
Der Unteragent `quellen-pruefer` prüft eigene Texte nach demselben Maßstab.

## Datenschutz

Bitte lesen Sie vor der ersten Nutzung Kapitel 1. Kurzfassung: Modelltraining ausschalten, keine
personenbezogenen Daten Dritter und keine urheberrechtlich geschützten Fremdtexte eingeben, bei
internen Hochschulinformationen THKI nutzen. Die Hinweise sind keine Rechtsberatung; maßgeblich sind
die Handreichungen der TH Köln.

## Wenn etwas hakt

Fragen gern als Issue in diesem Repository, dann haben alle etwas davon.

## Stand und Lizenz

Stand: 18. September 2026. Produkte in diesem Feld ändern sich schnell; prüfen Sie im Zweifel die
verlinkten Originalquellen.

Texte, Skript, Folien und Aufgaben stehen unter **CC BY 4.0**, der Code unter **MIT**. Nutzen Sie beides
für Ihre eigene Lehre, gern mit Nennung der Quelle.
