# Loop-Demo: /goal mit ehrlicher Prüfung

Beispiel zu Kapitel 7 des Skripts. Aus 14 fiktiven Rückmeldungen soll eine Zusammenfassung entstehen, die ein deterministisches Prüfskript besteht.

## Ablauf

1. Prüfskript ausführen, es scheitert:
   ```bash
   python3 loop-demo/pruefe_zusammenfassung.py
   ```
2. In Claude Code die Bedingung aus `ziel.md` eingeben.
3. Beobachten: Claude schreibt `zusammenfassung.md`, führt das Prüfskript aus, bessert nach, bis es besteht.
4. Kontrolle: `git diff --stat` zeigt, dass nur `zusammenfassung.md` geändert wurde.
5. Zurücksetzen: `git checkout -- loop-demo/zusammenfassung.md`.

## Was geprüft wird

| Prüfung | Stufe |
|---|---|
| Pflichtabschnitte „Überblick“, „Anmerkungen“, „Offene Punkte“ | Regel |
| Zahlen im Überblick in der Form „Zusage: 3“ stimmen | deterministisch |
| jede ID belegt, keine erfunden | deterministisch |
| höchstens 300 Wörter | deterministisch |
| Datendatei unverändert (Prüfsumme) | deterministisch |

## Variante für Fortgeschrittene

Ersetzen Sie das Prüfskript gedanklich durch „ein zweites Modell bewertet die Qualität“. Was ändert sich an der Verlässlichkeit? (Stichwort: Stufe 4 der Verifikationsleiter, Reward Hacking.)
