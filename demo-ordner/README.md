# Demo-Ordner: derselbe Auftrag, zweimal

Zwei Ordner mit **identischem Inhalt**, bis auf eine Datei: In `demo-mit-claude-md`
liegt zusätzlich eine `CLAUDE.md`. Das ist der ganze Unterschied.

```
demo-ordner/
├─ demo-ohne-claude-md/
│  └─ stichpunkte.md
└─ demo-mit-claude-md/
   ├─ stichpunkte.md      (dieselbe Datei)
   └─ CLAUDE.md           (der Unterschied)
```

## Zum Nachspielen

Öffnen Sie beide Ordner in Claude Code, am besten nebeneinander, und geben Sie in
beiden denselben Auftrag:

> Schreibe aus stichpunkte.md eine Mail an das Prüfungsamt.

Achten Sie auf vier Dinge:

| | ohne CLAUDE.md | mit CLAUDE.md |
|---|---|---|
| **Ton** | freundlich, aber beliebig | Sie-Form, kollegial, ohne Floskeln |
| **Aufbau** | Fließtext | Anlass, dann nummerierte Fragen |
| **Frist** | „zeitnah“ oder gar keine | ein Datum |
| **Studierendendaten** | werden übernommen, wie sie dastehen | bleiben draußen, die Regeldatei verbietet es |

Der letzte Punkt ist der wichtigste: Die `CLAUDE.md` enthält ein ausdrückliches
**Niemals**. Ohne sie gibt es keinen Grund, warum das Modell etwas weglassen sollte.

## Warum die Datei so aussieht, wie sie aussieht

Nur was vom Standard abweicht. „Sei hilfreich“ steht dort schon von selbst; was dort
hineingehört, sind die Dinge, die Sie sonst jedes Mal von Hand korrigieren würden.
Fünf bis zehn Regeln reichen, ab etwa 200 Zeilen lässt die Wirkung nach.

Zwei weitere Fassungen zum Vergleichen liegen in `vorlagen/`:
`CLAUDE-global-vorher.md` zeigt die typischen Fehler, `CLAUDE-global-nachher.md`
dieselbe Datei brauchbar gemacht.

## Nach einer Probe

Wenn Claude in diesen Ordnern Dateien angelegt oder geändert hat, stellt
`./vortrag.sh zuruecksetzen` im Dozenten-Ordner den Ausgangszustand wieder her.
