---
name: vortragssprache
description: Die Sprachregeln für Folien, Sprechtexte und Referentennotizen im Vortragsprojekt: Fachbegriffe erst erklären, dann benutzen, jeder Block sagt zuerst wofür er gut ist, und der Sprechtext folgt der Folie ohne sie vorzulesen. Verwenden beim Schreiben oder Ändern von Folientexten, Überschriften, Blocktiteln und Sprechtexten. Auch verwenden, wenn ein Text "zu technisch" wirkt oder jemand fragt, ob das Publikum das versteht.
---

# Wie im Vortrag gesprochen und geschrieben wird

Im Raum sitzen Lehrende und Verwaltung, keine Entwickler. Die Regeln stammen aus
Korrekturen von Thor, jede hat einen Anlass.

## 1. Kein Fachbegriff vor seiner Erklärung

**Erst sagen, was es ist und wofür es gut ist. Dann den Namen nennen. Nie umgekehrt.**

Das Glossar rettet das nicht: Im Vortrag schlägt niemand nach. Wer ein Wort hört, das er
nicht einordnen kann, hört bei den nächsten zwei Sätzen nicht zu.

Richtig ist die Reihenfolge von Block 5: erst „passende Stellen werden gesucht und nur die
mitgegeben", danach der Satz „das heißt im Fachjargon RAG". Falsch war die Fassung davor,
in der der Block nach zwei Produkten hieß, bevor jemand das Problem kannte.

Zwei erlaubte Ausnahmen:

- **Ratemuster:** eine Folie fragt, die nächste löst auf (Begriffs-Bingo, Vier Bausteine).
  Genau eine Folie Abstand, nicht mehr.
- **Fußzeile:** Der Fachbegriff steht klein unter der Folie als Anschluss für die, die ihn
  kennen, und fällt im Vortrag nicht. So gelöst beim Kontextfenster.

Der Test `kein Fachbegriff steht auf einer Folie vor seiner Erklärung` bewacht die Begriffe
aus der Liste `EINFUEHRUNG` in `tests/e2e_handout.py`. **Neuer Begriff heißt: neuer Eintrag dort.**

## 2. Jeder Begriff ist nachlesbar, und die Folie sagt wo

Es gibt zwei Sammlungen, und beide gehören ins Handout:

| Sammlung | Was drinsteht | Wo |
|---|---|---|
| **Glossar** | rund 85 Einträge von A bis Z, mit Quellen und Kapitelverweis | `skript/quelle/10_glossar.md` |
| **Konzeptkarten** | 41 ausführliche Karten in fünf Teilen, mit Herkunft und Abgrenzung | `foliensatz/konzepte_daten.json` |

Regel: **Jeder Fachbegriff, der auf einer Folie steht, muss in mindestens einer der beiden
stehen.** Fehlt er, wird er dort ergänzt, nicht von der Folie gestrichen.

In den Referentennotizen der Folie am Ende der Stichpunkte vermerken, wo er erklärt ist,
etwa `Nachlesen: Glossar „Embedding“, Konzeptkarte „Kontextfenster und Compaction“.`
Ein klickbarer Verweis auf der Folie bringt nichts, im Hörsaal klickt niemand.

## 3. Jeder Block sagt zuerst, wofür er gut ist

Der **Titel** eines Blocktrenners nennt die Frage oder den Nutzen, **nie ein Produkt**.
Der **Untertitel** sagt in einem Satz ohne Fachwort, was das Publikum davon hat.

| statt | besser |
|---|---|
| Second Brain, Graphify und Graft | Wie Ihr Wissen zur KI kommt |
| Ausblick: Loop Engineering | Wenn die KI sich selbst korrigiert |
| Zusammenarbeit über Claude-Instanzen | Zu mehreren am selben Stand arbeiten |

Dasselbe gilt innerhalb eines Blocks: erst eine Folie „was ist das und wofür", dann die
Einzelheiten, ganz zuletzt die Werkzeugnamen. Ein Test bewacht die Trenner.

## 4. Der Sprechtext folgt der Folie, liest sie aber nicht vor

Vier Regeln, von Thor in dieser Reihenfolge korrigiert:

1. **Alle Folienpunkte abdecken, in der Reihenfolge der Folie.** Nicht daran vorbeireden.
2. **Freie Rede, kein Vorlesen.** Nie „kommen wir zu Kasten drei". Die Karte soll
   wiedererkennbar sein, ohne dass ihr Name fällt. Also: „Natürlich möchte ich auch
   verstehen, was ich da tue" statt „Karte zwei behandelt das Lernen".
3. **Ein Absatz je Folienpunkt**, und zwei bis vier fette Anker je Folie, nicht mehr.
4. **Am Ende jeder Folie eine Überleitung** zur nächsten. Ohne sie ist es ein harter Schnitt.

Format der Notiz:

```
HH:MM bis HH:MM Uhr. <Stichpunkte für die Vortragende, Ablauf, Fallstricke, Rückfragen>

WORTLAUT
<ausformulierter Text mit Absätzen, endet mit der Überleitung>
```

Die Zeile `WORTLAUT` wird beim Bauen durch das rote **„So könnte es klingen"** ersetzt.
Relative Zeiten schreiben, `werkzeuge/uhrzeiten.py` rechnet sie in Uhrzeiten um.

## 5. Zahlen tragen ihre Herkunft auf der Folie

Eine Zahl braucht entweder eine Quelle im Verzeichnis oder eine sichtbare Zeile, dass sie
geschätzt ist. In den Notizen reicht nicht: Folien werden weitergereicht.

Formulierung, die sich bewährt hat: *„Schätzungen aus vergleichbaren Projekten, keine
Messwerte. Gebaut und im Betrieb ist bisher nur der Serienbrief."*

## 6. Stil

- Deutsch, Kernaussage zuerst, knapp und konkret.
- **Keine Gedankenstriche** (— und –). Komma, Doppelpunkt oder neuer Satz.
- Anführungszeichen „…“, auch in Code-Zeichenketten.
- Kein Wort, das die Zuhörenden nicht kennen, ohne dass es vorher fällt.

## Prüffrage

**Würde jemand aus der Verwaltung, der heute zum ersten Mal hier sitzt, bei jedem Wort
auf dieser Folie wissen, wovon die Rede ist?** Wenn nicht, fehlt eine Folie davor.
