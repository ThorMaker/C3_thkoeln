# C3: Claude Code Club

Unterlagen zur Reihe **„Claude Code, Automatisierung, Wissen“** an der TH Köln.
Erster Termin am 18. September 2026.

Dieses Repository ist Skript, Übungsprojekt und Werkzeugkasten zugleich. Öffnen Sie es in Claude Code, und Claude erklärt Ihnen die Inhalte, stellt Verständnisfragen und begleitet die Übungen. Sie müssen dafür nicht programmieren können.

## Die Reihe

Drei Vormittage, jeweils 09:30 bis 11:30 Uhr. Jeder Termin steht für sich; wer einen verpasst, kommt über das Skript mit.

| Termin | Thema | Worum es geht |
|---|---|---|
| **1** | Verstehen und fragen | Was ein Agent ist, was mit Ihren Daten passiert, wie Sie Claude auf Ihre Arbeit einstellen |
| **2** | Selber bauen | Ihr erster eigener Skill, danach eine offene Werkstatt an Ihrem echten Fall |
| **3** | Vertiefen und übertragen | Wie Ihr Wissen zur KI kommt, Zusammenarbeit im Team, was es wirklich spart |

**Zwischen Termin 1 und 2 gibt es Aufgaben.** Sie stehen in `aufgaben/`, mit Hinweisen, aber bewusst ohne fertige Lösung.

## Schnellstart in drei Minuten

1. **Herunterladen:** oben auf „Code“ und „Download ZIP“ klicken, ZIP entpacken.
   Mit Git: `git clone https://github.com/ThorMaker/c3_claudeCodeClub.git`
2. **Öffnen:** Claude Desktop starten, Tab **Code**, Umgebung **Local**, den Ordner `claude-hochschule-2026` als Projektordner wählen, Modus **Manual**.
3. **Loslegen:** eingeben: `Erkläre mir dieses Repository in fünf Sätzen. Ändere nichts.`

Voraussetzungen: Claude Desktop mit Pro-Konto (oder höher). Unter Windows zusätzlich Git for Windows.

## Inhalt

| Ordner | Inhalt |
|---|---|
| `aufgaben/` | die Aufgaben zwischen den Terminen, mit Prüffrage statt Lösung |
| `skript/` | das Skript als Markdown; Kapitelnummer = Block im Vortrag |
| `demo-ordner/` | zweimal derselbe Ordner, einmal mit und einmal ohne `CLAUDE.md`: der Vergleich aus Termin 1 zum Nachspielen |
| `diy/` | Aufgabenkarten für die Übungen |
| `vorlagen/Glossar_KI.pdf` | Glossar mit Fachbegriffen und Quellen zum Weitergeben |
| `vorlagen/Konzepte.pdf` | Anhang „Konzepte der KI-Technik“: je Konzept ein Bild, wofür es gut ist, wann es sich lohnt, wo die Grenze liegt (41 Konzepte, auch als `vorlagen/konzepte.md`) |
| `vorlagen/Weiterlernen.pdf` | zwölf geprüfte Kursempfehlungen in fünf Stufen, mit Aufwand, Sprache, Kosten und der Angabe, für wen ein Angebot nichts ist (auch als `vorlagen/weiterlernen.md`) |
| `vorlagen/` | CLAUDE.md vorher und nachher, Datenschutz-Profil, Leitplanken (Berechtigungsregeln und Hook), Checkliste, Einstellungs-Handout „Datenschutz in 5 Minuten“ (PDF), Skill-Vorlage, Starter-Prompts |
| `.claude/skills/` | Projekt-Skills: `skript-tutor` (Lernbegleitung), `mail-dekanat` (Musterlösung der Übung), `handover` (Übergabe vor `/clear`), `prozessinventur` (Automatisierungskandidaten bewerten) |
| `.claude/agents/` | eigener Unteragent `quellen-pruefer` (prüft Texte auf Belege, nur lesend) |
| `beispiele/literaturliste/` | kleines Python-Projekt mit zwei absichtlichen Fehlern und eigener `CLAUDE.md` für den Unterordner |
| `plugins/hochschul-toolkit/` | Beispiel-Plugin mit Skills für Gremienprotokolle und Lehrveranstaltungs-Feedback |
| `.claude-plugin/marketplace.json` | macht dieses Repository zu einem Plugin-Marketplace |
| `n8n/` | Workflow des durchgehenden Falls zum Importieren, Einrichtungsanleitung, Prompts, Muster 2 mit MCP |
| `n8n/claude-auftrag-einrichten.md` | fertiger Auftrag an Claude Code, den Workflow über MCP einzurichten |
| `n8n/sandbox/` | abgeschottete n8n-Instanz mit Docker, in der Claude alles ausprobieren darf |
| `second-brain-demo/` | fiktiver Notizkorpus für Graphify und Code-Beispiel für Graft |
| `loop-demo/` | Loop mit `/goal` und deterministischem Prüfskript |
| `zusammenarbeit/` | Team-Repository-Vorlage mit ADRs und gemeinsamen Leitplanken |
| `tools/` | QR-Code-Erzeuger, Prozessinventur-Auswertung |
| `diagramme/` | Abbildungen aus Skript und Vortrag |

Enthalten sind alle Kapitel mit ihren Beispielprojekten. Die Kapitelnummer entspricht dem Block im Vortrag.

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
claude plugin marketplace add ThorMaker/c3_claudeCodeClub
claude plugin install hochschul-toolkit@hochschule-2026
```

## Quellen

Jedes Skriptkapitel hat ein eigenes Quellenverzeichnis im IEEE-Stil; Webquellen tragen das Abrufdatum. Der Unteragent `quellen-pruefer` prüft eigene Texte nach demselben Maßstab.

## Datenschutz

Bitte lesen Sie vor der ersten Nutzung Kapitel 1. Kurzfassung: Modelltraining ausschalten, keine personenbezogenen Daten Dritter und keine urheberrechtlich geschützten Fremdtexte eingeben, bei internen Hochschulinformationen THKI nutzen. Die Hinweise sind keine Rechtsberatung; maßgeblich sind die Handreichungen der TH Köln.

## Wenn etwas hakt

Fragen gern als Issue in diesem Repository, dann haben alle etwas davon. Vor dem zweiten Termin gibt es eine halbe Stunde Sprechstunde.

## Stand und Lizenz

Stand: 15. September 2026. Produkte in diesem Feld ändern sich schnell; prüfen Sie im Zweifel die verlinkten Originalquellen, sie sind überall verlinkt.

Texte, Skript und Aufgaben stehen unter **CC BY 4.0**, der Code unter **MIT**. Nutzen Sie beides für Ihre eigene Lehre, gern mit Nennung der Quelle.

Nicht enthalten sind die Foliensätze und die Dozentenunterlagen; die liegen in einem getrennten, privaten Repository.
