# Plugin: hochschul-toolkit

Beispiel-Plugin zum Vortrag an der TH Köln. Es zeigt, wie man eigene Arbeitsanweisungen im Kollegium verteilt.

| Baustein | Typ | Aufruf |
|---|---|---|
| `gremien-protokoll` | Skill | automatisch bei Protokoll-Aufgaben oder `/hochschul-toolkit:gremien-protokoll` |
| `lv-feedback-auswerten` | Skill | automatisch bei Evaluations-Freitexten |
| `kurzfassung` | Befehl | `/hochschul-toolkit:kurzfassung <Datei oder Text>` |

## Installation

```bash
claude plugin marketplace add ThorMaker/c3_claudeCodeClub
claude plugin install hochschul-toolkit@hochschule-2026
```

In Claude Desktop: „+“ neben dem Eingabefeld, „Plugins“, „Add plugin“. Ohne Plugin-System: die Ordner aus `skills/` nach `~/.claude/skills/` kopieren.

## Aufbau

```text
hochschul-toolkit/
├── .claude-plugin/plugin.json   Name, Version, Beschreibung
├── skills/                      je ein Ordner mit SKILL.md
└── commands/                    Befehle als Markdown-Datei
```

## Eigenes Plugin daraus machen

Ordner kopieren, `plugin.json` anpassen, Skills austauschen, in einem eigenen Repository mit `.claude-plugin/marketplace.json` veröffentlichen. Kolleginnen und Kollegen installieren es dann mit zwei Befehlen.
