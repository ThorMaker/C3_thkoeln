---
name: folien-nachziehen
description: Prüft nach einer Änderung an Folien, Blocknamen oder der Reihenfolge, welche anderen Dateien im Vortragsprojekt mitziehen müssen. Verwenden, sobald eine Folie hinzukommt, wegfällt, umbenannt oder verschoben wird, ein Block anders heißt, oder eine Sitzung neu zusammengesetzt wird. Auch verwenden, wenn nach einem Umbau etwas "nicht mitgekommen" ist oder ein Dokument veraltet wirkt.
---

# Was mitziehen muss, wenn sich eine Folie ändert

Im Vortragsprojekt hängen an jeder Folie sieben andere Stellen. Sie werden nicht alle
automatisch erzeugt, und die gefährlichen fallen still aus: Ein Dokument wird weiter
gebaut, nur ohne die neue Folie. Genau das ist am 15.09.2026 passiert, als das
Sprechskript weiter aus dem Gesamtfoliensatz erzeugt wurde und die Folien, die nur in
den Sitzungen stehen, darin komplett fehlten.

## Die Liste

Nach jeder Änderung diese Liste von oben nach unten durchgehen. Was nicht zutrifft,
ausdrücklich abhaken, nicht überspringen.

| Nr | Stelle | Wann betroffen | Was passiert sonst |
|---|---|---|---|
| 1 | `werkzeuge/uebergabe.py`, Liste `WARUM` | Folie kommt, geht oder wandert | Der Bau bricht ab und nennt die Folie. Gutmütig. |
| 2 | `foliensatz/paket1.js`, Ablauf-Folie | Blockname oder Sitzungsschnitt ändert sich | Die Agenda widerspricht den Trennern. Fällt niemandem auf. |
| 3 | `skript/quelle/0N_*.md`, Kapitelüberschrift | Blockname ändert sich | Folie und Skript laufen auseinander. |
| 4 | `skript/quelle/00_vorwort.md`, Kapiteltabelle | Blockname ändert sich | dito |
| 5 | `leitfaden/leitfaden_paket*.py`, `SECTIONS` und Minutenplan | Folien in einem Paket verschieben sich | Der Leitfaden nummeriert falsch. |
| 6 | `leitfaden/sprechskript_gesamt.py`, Liste `SITZUNGEN` | eine Sitzung kommt dazu oder heißt anders | **Der Sprechtext fehlt, ohne Fehlermeldung.** |
| 7 | `werkzeuge/word.py`, Liste der Dokumente | ein neues PDF entsteht | Ein Test meckert, aber erst am Ende. |
| 8 | `bauen.sh` | ein neuer Generator oder ein neues PDF | Das Dokument wird nie gebaut. |
| 9 | `tests/e2e_handout.py` | neue Folie, die in keinem Paket steht | Ihr Verlust fällt erst im Vortrag auf. |

## Reihenfolge der Prüfung

1. **Quelle ändern**, dann `./vortrag.sh bauen`. Punkt 1 meldet sich von selbst, wenn er betroffen ist.
2. **Nach Resten suchen**, mit dem alten Wortlaut, und die Ergebnisordner ausklammern:
   ```
   grep -rn "<alter Text>" . | grep -vE "node_modules|fassungen/|\.pptx|\.pdf|\.docx"
   ```
   Treffer in `leitfaden/L*_*.md`, `Sprechskript_*.md` und `Aufbau_und_Begruendung.md` sind
   erzeugte Dateien und verschwinden beim nächsten Bau von selbst. Alles andere ist Handarbeit.
3. **Zeiten prüfen:** `./vortrag.sh bauen` nennt je Sitzung die Endzeit. Keine darf nach 11:30 liegen.
4. **`./vortrag.sh tests`**, danach `./vortrag.sh word`, wenn ein PDF dazugekommen ist.

## Woran man merkt, dass etwas fehlt

- Eine Sitzung endet plötzlich früher oder später als vorher, ohne dass jemand Zeiten geändert hat.
- Ein erzeugtes Dokument hat weniger Folien als der Foliensatz, aus dem es stammen soll.
- Ein Blockname steht an einer Stelle noch alt und an der anderen schon neu.

## Prüffrage

**Wenn ich jetzt nur die neuen Folien suche: Stehen sie in jedem Dokument, das sie
enthalten müsste?** Sprechskript, Übergabefassung, Leitfaden, Word-Fassung. Wenn die
Antwort nicht für jedes einzelne Dokument ja ist, ist die Änderung nicht fertig.
