---
name: js-folien-schreiben
description: Die Fallstricke der Foliengeneratoren im Vortragsprojekt, also der Dateien foliensatz/*.js mit pptxgenjs. Verwenden vor jeder Änderung an paket1.js bis paket3.js, folge1.js bis folge3.js, sitzung.js oder stil.js. Auch verwenden bei einem Syntaxfehler beim Bauen, bei Zeilenumbrüchen, die nicht ankommen, oder wenn Sternchen statt Fettdruck auf der Folie landen.
---

# Foliengeneratoren ändern, ohne hineinzufallen

Die Foliensätze entstehen aus JavaScript. Drei Fehler passieren immer wieder, alle drei
haben am 15.09.2026 Zeit gekostet.

## 1. Niemals gerade Anführungszeichen in einer Zeichenkette

Der häufigste Fehler, und er sieht harmlos aus:

```js
// FALSCH: das gerade " beendet die Zeichenkette mitten im Satz
s.addNotes("Wenn die Antwort „niemand" lautet, gebe ich es nicht ab.");

// RICHTIG
s.addNotes("Wenn die Antwort „niemand“ lautet, gebe ich es nicht ab.");
```

Deutsche Anführungszeichen sind ohnehin Vorschrift: unten „ und oben “. Das gilt auch
für Fragezeichen davor: `zusammen?“` und nicht `zusammen?"`.

**Niemals mit einer Suchen-und-Ersetzen-Aktion über die ganze Datei reparieren.** Ein
Muster wie „das erste gerade Anführungszeichen nach einem „ ersetzen" zerstört alle
bereits korrekten Stellen. Immer die eine gemeldete Zeile anfassen, die Zeilennummer
steht in der Fehlermeldung.

## 2. Zeilenumbrüche in Notizen doppelt schreiben

Notizen enthalten `\n`. Wird die Datei aus Python heraus geschrieben, muss dort `\\n`
stehen, sonst landet ein echter Umbruch im JS-String und die Datei ist kaputt.

```python
# FALSCH: echter Umbruch im JS-String
neu = 's.addNotes("Erster Satz.\nZweiter Satz.");'
# RICHTIG
neu = 's.addNotes("Erster Satz.\\nZweiter Satz.");'
```

Nach jeder Änderung `node foliensatz/<datei>.js` aufrufen. Der Syntaxfehler kommt sofort.

## 3. Fettdruck nur mit Sternchen, nie direkt

`addNotes()` von pptxgenjs kann nur reinen Text. Fettdruck wird als `**so**` geschrieben
und von `werkzeuge/notizen.py` nachträglich in echte Textläufe verwandelt. Auf der Folie
selbst dagegen gibt es kein Markdown: Dort wird Fettdruck über `{ bold: true }` gesetzt.
Sternchen auf einer Folie sind immer ein Fehler, ein Test wacht darüber.

## Wie die Bausteine heißen

```js
content(kicker, farbe, titel)                  // Standardfolie, gibt die Folie zurück
section(nr, kicker, titel, untertitel, f, t)   // Blocktrenner mit Fortschrittsbalken
card(s, x, y, w, h, kicker, titel, zeilen, o)  // graue oder farbige Karte
takeaway(s, fett, rest, o)                     // Merksatz unten, Standard y 5.6
code(s, x, y, w, h, text, size)                // grauer Kasten in Schreibmaschinenschrift
chip(s, x, y, w, label, farbe)                 // kleines farbiges Etikett
live(s, farbe, minuten, schritte, falls, auftrag)  // Demo-Folie
quellen(s, ["schluessel"])                     // Quellenzeile, Nummern entstehen automatisch
```

`quellen()` bricht ab, wenn ein Schlüssel nicht in `skript/zitation/quellen.json` steht.
Das ist Absicht: Erst die Quelle eintragen, dann zitieren.

## Wo etwas hingehört

| Inhalt | Datei |
|---|---|
| Folien eines Blocks | `paket1.js` bis `paket3.js`, als benannte Funktion exportiert |
| Folien nur einer Sitzung | `folge1.js` bis `folge3.js` |
| Pause und Fragerunde | `sitzung.js`, nehmen ihren Text als Parameter |
| Farben, Maße, Bausteine | `stil.js` |

Eine Folie, die in mehreren Sitzungen vorkommt, gehört in ein Paket, nie kopiert.

## Nach jeder Änderung

1. `node foliensatz/<datei>.js` für den Syntaxfehler
2. `./vortrag.sh bauen`, dann `./vortrag.sh tests`
3. Sichtprüfung nach dem Skill **folien-pruefen**
4. Mitziehende Stellen nach dem Skill **folien-nachziehen**

## Prüffrage

**Läuft `node` auf der geänderten Datei fehlerfrei durch, und habe ich die Folie danach
als Bild gesehen?** Beides ist nötig. Das eine findet Syntax, das andere findet Layout.
