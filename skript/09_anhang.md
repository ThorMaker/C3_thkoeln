# Kapitel 9: Anhang

Das Glossar mit Fachbegriffen und Quellen zum Nachlesen steht in Kapitel 10.

## 9.1 Befehlsreferenz

### Claude Code

| Befehl | Wirkung |
|----|----|
| `claude`, `claude doctor` | starten, Installation prüfen |
| `claude -p "Auftrag"` | ohne Dialog ausführen, etwa in Skripten |
| `/init`, `/memory` | CLAUDE.md-Entwurf erzeugen, Gedächtnisdateien anzeigen |
| `/clear`, `/compact <Fokus>` | neu beginnen, Verlauf zusammenfassen |
| `/rename`, `/resume` | Sitzung benennen, später fortsetzen |
| `/rewind` oder zweimal Esc | Code und Gespräch zurücksetzen (Terminal) |
| `/handover` | Übergabe schreiben (Skill aus dem Handout-Repository) |
| `/model <alias>`, `/effort` | Modell wählen (`opus`, `sonnet`, `haiku`, `opusplan`), Denkaufwand einstellen |
| `/usage`, `/context` | Verbrauch und Kontextbelegung ansehen |
| `/plugin`, `/plugin install <name>@<marketplace>` | Plugins verwalten und installieren |
| `/mcp`, `claude mcp add --transport http <name> <url>` | MCP-Server verwalten und anbinden |
| `/permissions`, `/hooks` | Regeln und Hooks prüfen (Terminal) |
| `/goal <Bedingung>`, `/goal clear` | bis zur erfüllten Bedingung weiterarbeiten, Ziel aufheben |
| `/loop <Intervall> <Auftrag>` | Auftrag in einer offenen Sitzung wiederholen |
| `/install-github-app` | GitHub-App und Actions einrichten |
| `/desktop` | Terminal-Sitzung in Claude Desktop fortsetzen |
| `claude --worktree` | Sitzung in eigener Arbeitskopie starten |

### Graphify und Graft

| Befehl | Wirkung |
|----|----|
| `uv tool install graphifyy`, `graphify install` | Graphify installieren, Skill registrieren |
| `/graphify <ordner>`, `--update` | Graph bauen, nur Geändertes neu lesen |
| `graphify query`, `path`, `explain` | Graph befragen, Verbindung zeigen, Begriff erklären |
| `graphify hook install`, `graphify claude install` | automatische Aktualisierung, Claude den Graphen zuerst nutzen lassen |
| `npm install -g @nanonets/graft`, `graft init` | Graft installieren und verdrahten |
| `graft viz`, `graft ask`, `graft uninstall` | ansehen, befragen, entfernen |

### Handout-Werkzeuge

| Befehl | Wirkung |
|----|----|
| `python3 tools/qr_erzeugen.py <URL>` | QR-Code erzeugen |
| `python3 tools/prozessinventur.py vorlagen/prozessinventur.csv` | Prozessinventur nach Netto-Nutzen sortieren |
| `python3 loop-demo/pruefe_zusammenfassung.py` | Prüfskript der Loop-Demo |

## 9.2 Prompt-Sammlung für den Hochschulalltag

**Überblick über einen Ordner:**

```
Verschaffe dir einen Überblick über diesen Ordner. Erkläre in fünf Stichpunkten,
was hier liegt, und nenne drei Aufgaben, bei denen du mir helfen könntest.
Ändere nichts.
```

**Übungsaufgaben:**

```
Erstelle auf Basis von kapitel-3.md fünf Übungsaufgaben mit steigendem
Schwierigkeitsgrad, jeweils mit Musterlösung und einem typischen Fehler.
Prüfe am Ende, ob jede Aufgabe mit dem Stoff aus kapitel-3.md lösbar ist.
```

**Protokoll vorstrukturieren:**

```
Strukturiere diese Stichpunkte als Protokoll mit Tagesordnungspunkten,
Beschlüssen und Aufgaben (Wer? Bis wann?). Markiere Unklarheiten mit [KLÄREN].
Erfinde nichts, was nicht in den Stichpunkten steht.
```

**Belege prüfen:**

```
Prüfe kapitel-2.md mit dem quellen-pruefer. Markiere jede Tatsachenbehauptung
ohne Beleg und jede Webquelle ohne Abrufdatum.
```

**Prüfbare Zielbedingung formulieren:**

```
Hilf mir, für diese Aufgabe eine prüfbare Zielbedingung zu formulieren:
<Aufgabe>. Schlage ein kleines Prüfskript vor, das mit Exit-Code 0 endet,
wenn die Aufgabe erfüllt ist, und nenne, was der Agent nicht verändern darf.
```

## 9.3 Wichtige Links

- Claude herunterladen: https://claude.com/download
- Claude Code Dokumentation: https://code.claude.com/docs
- Anthropic Privacy Center: https://privacy.claude.com
- THKI der TH Köln: https://ki.th-koeln.de
- n8n Dokumentation: https://docs.n8n.io
- Graphify: https://github.com/Graphify-Labs/graphify
- Graft: https://github.com/trailhq/Graft
