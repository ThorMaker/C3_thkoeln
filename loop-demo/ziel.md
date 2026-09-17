# Zielbedingung für /goal

In Claude Code (Handout-Repository geöffnet) genau so eingeben, unter Windows `python` statt `python3`:

```text
/goal Das Prüfskript `python3 loop-demo/pruefe_zusammenfassung.py` endet mit Exit-Code 0, und seine vollständige Ausgabe steht im Verlauf. Schreibe dafür ausschließlich loop-demo/zusammenfassung.md auf Basis von loop-demo/daten/rueckmeldungen.json. Die Daten und das Prüfskript dürfen nicht verändert werden. Stoppe spätestens nach 8 Durchläufen.
```

**Warum so formuliert?**

- **Prüfbar:** Das Prüfmodell von `/goal` führt selbst nichts aus; es beurteilt die Ausgabe im Verlauf. Deshalb soll Claude die Ausgabe des Skripts zeigen.
- **Stufe 1:** Die eigentliche Prüfung ist deterministisch (Exit-Code), nicht das Urteil eines Modells.
- **Schutz vor Specification Gaming:** Daten und Prüfskript sind tabu; das Skript prüft zusätzlich eine Prüfsumme der Daten.
- **Budget:** höchstens 8 Durchläufe.
