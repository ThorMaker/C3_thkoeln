---
name: umfrage-auswerten
description: Wertet eine laufende oder beendete Lehrveranstaltungs-Umfrage aus, fasst Freitexte zusammen und schaltet Schutz oder Umfrage auf und zu. Trigger - "/umfrage-auswerten", "Auswertung der Umfrage", "was kam bei der Rueckmeldung raus", "Umfrage schliessen", "Schutz einschalten".
---

<!-- AI-assisted: Claude, human-reviewed ausstehend, Stand 2026-09-17 -->

# Umfrage auswerten und steuern

Holt die Antworten einer Umfrage vom eigenen Server, rechnet aus was
zaehlbar ist, und fasst Freitexte zusammen. Ausserdem: Schutz umlegen,
Umfrage schliessen, Matrikelnummern nachtragen.

## Wann dieser Skill

- „Was kam bei der Rueckmeldung zu Vorlesung 5 raus?"
- „Mach die Umfrage zu."
- „Schalt den Schutz ein, da stimmen Fremde ab."
- „Trag noch fuenf Matrikelnummern nach."

Fuer eine **neue** Umfrage ist `umfrage` zustaendig.

## Auswerten

```bash
/usr/bin/python3 ~/.claude/skills/umfrage-auswerten/auswerten.py --liste
/usr/bin/python3 ~/.claude/skills/umfrage-auswerten/auswerten.py --kennung vorlesung-5-a7f3
```

Das Skript liefert Zahlen, keine Deutung. **Die Deutung ist deine Aufgabe:**

1. Beginne mit dem Ergebnis in zwei bis vier Zeilen. Thor hat ADHS, das
   Wichtigste nie unten.
2. Nenne bei Bewertungen den **Durchschnitt und die Streuung**. Ein Schnitt
   von 3,0 aus lauter Dreien bedeutet etwas voellig anderes als 3,0 aus
   Einsen und Fuenfen. Sag, welcher der beiden Faelle vorliegt.
3. Fasse Freitexte zu **Themen** zusammen, nicht zu einer Liste von Zitaten.
   Nenne je Thema, wie viele es genannt haben.
4. Zitiere hoechstens drei Freitexte woertlich, und nur wenn sie etwas
   zeigen, was die Zahlen nicht hergeben.
5. **Bei weniger als fuenf Antworten: sag, dass man daraus nichts ableiten
   kann.** Auch wenn Thor eine Aussage will.
6. Bei geschuetzten Umfragen die Beteiligung nennen (abgestimmt von
   zugelassen). Niedrige Beteiligung entwertet die Aussage.

**Nie:** einzelne Antwortende erraten oder zuordnen, auch nicht scherzhaft.
Die Anonymitaet ist der Grund, warum die Leute ehrlich geantwortet haben.

## Steuern

```bash
# Schutz an oder aus, der QR-Code bleibt gueltig
auswerten.py --kennung vl5-a7f3 --schutz an
auswerten.py --kennung vl5-a7f3 --schutz aus

# Umfrage schliessen oder wieder oeffnen
auswerten.py --kennung vl5-a7f3 --zu
auswerten.py --kennung vl5-a7f3 --auf

# Nummern nachtragen
auswerten.py --kennung vl5-a7f3 --nummern-datei /tmp/nachzuegler.csv
```

## Grafana

Fuer Balken und Verlauf:
`https://grafana.vibe-cortex.com/d/umfragen-auswertung/umfrage-auswertung`

Oben zwei Auswahlfelder: **Umfrage** und **Frage**. Aktualisiert sich alle
zehn Sekunden von allein. Der direkte Link zu einer Umfrage endet auf
`?var-umfrage=<tabellenname>`.

Verweise Thor auf Grafana, wenn er waehrend der Vorlesung zuschauen will.
Deine Textauswertung ist fuer danach.

## Fallstricke

- **Geloeschte Zeilen bleiben in der Datenbank** (NocoDB markiert nur). Das
  Skript filtert sie heraus, eigene SQL-Abfragen muessen das auch tun:
  `WHERE "__nc_deleted" IS NOT TRUE`.
- Die Spalte `eingang` ist meist leer, die echte Zeit steht in `created_at`.
- Mehrere Umfragen koennen aehnlich heissen. Bei Zweifel `--liste` zeigen
  und Thor waehlen lassen, statt zu raten.

## Dashboards: es gibt nichts zu bauen

**Für eine neue Umfrage muss kein Dashboard angelegt werden.** Beide
Dashboards sind generisch und finden neue Umfragen von allein. Wer nach
einem Skill zum Dashboard-Bauen fragt, bekommt diese Erklaerung, nicht ein
neues Dashboard.

Wie sie sich anpassen:

| Was | Woher es kommt |
|---|---|
| Die Umfrage in der Auswahlliste | aus NocoDBs Tabellenverzeichnis, sobald die Tabelle existiert |
| Eine Kachel je Frage | aus dem Feldtyp: Auswahl, Bewertung, Zahl, Ja/Nein werden Balken; Freitext wird Tabelle |
| Die Ueberschrift der Kachel | der Fragetext aus NocoDB, nicht der Spaltenname |
| Die Beteiligung | aus der Tabelle `zugelassen_<tabellenname>` |

Daraus folgt: **Eine Frage hinzufuegen heisst, eine Spalte hinzufuegen.**
Die Kachel erscheint beim naechsten Laden.

### Die zwei Dashboards

- **Umfrage-Überblick** (`/d/umfragen-ueberblick/umfrage-ueberblick`)
  Alle Fragen auf einmal. Der Normalfall.
- **Umfrage-Auswertung** (`/d/umfragen-auswertung/umfrage-auswertung`)
  Eine Frage genau ansehen, mit Klartextspalte daneben.

Direkt zu einer Umfrage: `?var-umfrage=<tabellenname>` anhaengen.

### Fuer den Beamer

`&kiosk` an die Adresse haengen, dann verschwinden Menues und Kopfzeile:

```
https://grafana.vibe-cortex.com/d/umfragen-ueberblick/umfrage-ueberblick?var-umfrage=<tabelle>&kiosk
```

Aktualisiert sich alle zehn Sekunden. Bietet Thor das an, wenn er waehrend
einer Sitzung mitlesen will.

### Wann man doch Hand anlegen muss

Nur in drei Faellen, und alle drei sind selten:

1. **Mehrere Vorlesungen vergleichen.** Die Dashboards zeigen immer genau
   eine Umfrage. Ein Vergleichs-Dashboard waere neu zu bauen.
2. **Eine Frage soll anders dargestellt werden** als Balken oder Tabelle,
   etwa eine Bewertung als Tortendiagramm.
3. **Eine eigene Rechnung**, etwa Verstaendlichkeit nach Vorwissen getrennt.

In diesen Faellen: die Vorlage
`~/projekte/hochschulreferent/dienste/grafana/umfrage-ueberblick.json`
kopieren, neue `uid` und neuen `title` vergeben, nach
`~/infra/grafana/dashboards/` auf den Server legen. Grafana liest den Ordner
alle 30 Sekunden neu, ein Neustart ist nicht noetig.

**Zwei Fallen dabei:**
- `WHERE "__nc_deleted" IS NOT TRUE` gehoert in jede Abfrage, sonst zaehlen
  geloeschte Antworten mit.
- Der Grafana-Benutzer darf **nur lesen**. Das ist Absicht, nicht reparieren.
