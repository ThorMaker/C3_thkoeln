# Ein Ablauf mit Prüfschleife

**Kür** · etwa 60 Minuten · bis Folge 2

## Ziel

Ein Ablauf, der sein eigenes Ergebnis prüft und bei einem Fehler noch einmal ansetzt, statt ihn durchzureichen.

## Warum das lohnt

Das ist der Unterschied zwischen einer netten Spielerei und etwas, dem man im Betrieb trauen kann. Solange nur ein Mensch am Ende schaut, skaliert nichts.

## Wegweiser

Hier stehen Hinweise, keine Lösung. Der Weg ist die Aufgabe.

1. Suchen Sie einen Schritt in Ihrem Alltag, den heute **ein Mensch kontrolliert**. Genau dort sitzt die Prüfschleife.
2. Übersetzen Sie das weiche Kriterium in ein hartes. Aus „die Zusammenfassung ist vollständig“ wird „jede Rückmeldungs-ID kommt im Text vor“. Das ist der eigentliche Denkschritt dieser Aufgabe.
3. Die Prüfung soll **kein zweites Modell** machen, sondern Programmcode. Sie ist dadurch kostenlos, schnell und irrt sich nicht.
4. Bauen Sie eine Abbruchbedingung ein: nach drei Versuchen geht es an einen Menschen. Ohne Abbruch läuft eine Schleife im Zweifel ewig.
5. Ob Sie das in n8n bauen oder als Skill, ist gleichgültig. Der Dekanats-Workflow unter `n8n/` zeigt das Muster; schauen Sie sich die Knoten „Prüfen“ und „Vollständig?“ an.

## Fertig, wenn

- Es gibt ein Kriterium, das ein Programm prüfen kann.
- Bei einem Fehlschlag passiert etwas anderes als beim Erfolg.
- Es gibt eine Obergrenze für die Versuche.
- **Die Prüffrage:** Könnten Sie jemandem in einem Satz sagen, woran der Ablauf merkt, dass er fertig ist?

## Häufige Stolpersteine

- Weiches Kriterium: „gut“, „vollständig“, „sinnvoll“ kann kein Programm prüfen. Suchen Sie etwas Zählbares.
- Kein Abbruch: Eine Schleife ohne Obergrenze ist ein Fehler, kein Feature.
- Zu groß angefangen: Ein Prüfschritt reicht für diese Aufgabe.

## Zum Nachlesen

Skript, Kapitel 4.5 und 7. Folie „Der Trick: Vollständigkeit prüfbar machen“.

---

Kommen Sie nicht weiter? Machen Sie ein Issue im Repository auf oder bringen Sie die Frage mit in die Sprechstunde vor Folge 2. Eine steckengebliebene Lösung ist ein guter Gesprächsanlass, keine Blamage.
