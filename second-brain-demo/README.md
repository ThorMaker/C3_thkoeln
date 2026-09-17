# Second-Brain-Demo: Graphify und Graft

Fiktives Beispielmaterial zu Kapitel 5 des Skripts. Alle Personen, Gremien und Entwürfe sind erfunden; die Paper-Exzerpte fassen veröffentlichte Arbeiten in eigenen Worten zusammen.

## Inhalt

- `unterlagen/`: zwölf kurze Notizen (Vorlesung, Paper-Exzerpte, Gremienprotokoll, Richtlinienentwurf, Lehrprojekt), verknüpft mit `[[Wikilinks]]`
- `code-beispiel/`: kleines Python-Projekt `lehreval` (anonymisiert und wertet Evaluationsfreitexte aus) zum Ausprobieren von Graft

## Graphify ausprobieren (Unterlagen)

```bash
uv tool install graphifyy      # oder: pipx install graphifyy
graphify install               # Skill in Claude Code registrieren
```

In Claude Code, Handout-Repository geöffnet:

```text
/graphify second-brain-demo/unterlagen
```

Danach:

1. `second-brain-demo/unterlagen/graphify-out/graph.html` im Browser öffnen und die Themengruppen ansehen.
2. `GRAPH_REPORT.md` lesen: Welche Begriffe sind zentral, welche Verbindungen überraschen?
3. Fragen stellen:

```text
/graphify query "Welche Unterlagen betreffen die KI-Richtlinie der Fakultät?"
/graphify path "Zettelkasten" "KI-Richtlinie"
/graphify explain "Prüfungsformate"
```

**Beobachten:** Die Antworten nennen Pfade durch den Graphen und die Notizen, aus denen sie stammen. Kanten mit `EXTRACTED` stehen so in den Notizen, `INFERRED` wurde erschlossen.

## Graft ausprobieren (Code)

```bash
npm install -g @nanonets/graft
cd second-brain-demo/code-beispiel
graft init --dry-run           # zuerst ansehen, was angelegt würde
graft init
graft viz
graft ask "Wo werden Namen und Matrikelnummern entfernt?"
```

Zum Aufräumen: `graft uninstall`. Graft sendet anonyme Nutzungsstatistiken; abschalten mit `graft telemetry disable`.

## Datenschutz

Die Unterlagen sind fiktiv. Für echte Unterlagen gilt die Ampel aus Kapitel 1.12; bei Graphify gehen Dokumente an das Modell Ihrer Sitzung, alternativ an ein lokales oder institutionelles Modell.
