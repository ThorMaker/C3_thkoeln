# Zusammenarbeit über mehrere Claude-Instanzen

Material zu Kapitel 6 des Skripts.

| Weg | Wann | Material |
|---|---|---|
| Gemeinsames Repository | sofort, für jedes Projekt | `team-repo-vorlage/` |
| Parallele Sitzungen | unabhängige Aufgaben gleichzeitig | Claude Desktop legt Worktrees automatisch an; CLI: `claude --worktree` |
| GitHub-App im Team | Issues und Pull Requests mit `@claude` | `/install-github-app` im Terminal |
| Wissenslandkarte im Repository | wenn das Projekt wächst | Graphify, `graphify-out/` einchecken |
| GraphRAG | Pilot mit klarer Frage über viele Quellen | Kapitel 6.6, Governance zuerst |

## Start mit der Vorlage

```bash
cp -r zusammenarbeit/team-repo-vorlage ~/projekte/mein-projekt
cd ~/projekte/mein-projekt && git init
```

Dann in Claude Code: „Passe die CLAUDE.md an mein Projekt an. Frage mich nach Ziel, Begriffen und Grenzen.“
