<!-- AI-assisted: Claude, human-reviewed ausstehend, Stand 16.09.2026 -->
# Rückmeldung zur Vorlesung: Anleitung

Für Lehrende und Mitarbeitende. Keine Programmierkenntnisse nötig.
Eine neue Umfrage dauert etwa zwei Minuten.

---

## In Kürze

1. Formular in n8n öffnen, Titel und Fragen eintippen, Knopf drücken.
2. QR-Code herunterladen und auf die letzte Folie kleben.
3. Nach der Vorlesung in NocoDB nachsehen.

Das war es. Der Rest dieser Anleitung ist für Sonderfälle.

---

## 1. Neue Umfrage anlegen

Öffnen Sie `https://n8n.vibe-cortex.com`, wählen Sie den Workflow
**„Umfrage anlegen (NocoDB, QR-Code)"** und starten Sie das Formular.

### Titel

Frei wählbar, zum Beispiel `Rückmeldung Vorlesung 5`. Er steht später
über dem Formular, das die Studierenden sehen.

### Fragen

**Eine Zeile je Frage.** Hinter dem senkrechten Strich steht, welche Art
von Antwort Sie wollen:

```
Wie verständlich war die Vorlesung? | Bewertung
Das Tempo war | Auswahl: zu langsam, genau richtig, zu schnell
Was sollen wir vertiefen? | Text
Wie viele Stunden haben Sie vorbereitet? | Zahl
Ich möchte die Folien per Mail | JaNein
```

Diese fünf Arten gibt es:

| Sie schreiben | Die Studierenden sehen |
|---|---|
| `Bewertung` | fünf Sterne zum Anklicken |
| `Auswahl: a, b, c` | Auswahlknöpfe mit genau diesen Möglichkeiten |
| `Text` | ein großes Feld für freie Antworten |
| `Zahl` | ein Zahlenfeld |
| `JaNein` | ein Häkchen |

Schreiben Sie nichts hinter den Strich, wird es ein einzeiliges Textfeld.

### Schutz

**„nein, offen für alle"** reicht in den meisten Fällen. Jeder, der den
QR-Code scannt, kann antworten.

**„ja, geschützt"** verlangt vorher eine Matrikelnummer. Tragen Sie die
zugelassenen Nummern in das letzte Feld ein, eine je Zeile. Sie können
auch eine CSV-Datei hineinkopieren: Kopfzeilen, Namen und doppelte
Einträge werden von allein aussortiert.

**Sie können sich hier ruhig falsch entscheiden.** Der Schutz lässt sich
später mit einem Häkchen umlegen, und der QR-Code bleibt gültig
(siehe Abschnitt 4).

---

## 2. Der QR-Code

Nach dem Absenden zeigt n8n Ihnen zwei Adressen: eine für die
Studierenden und eine für Ihre Auswertung. Der QR-Code liegt als Bild im
Ergebnis des Laufs (in n8n links unten auf den letzten Schritt klicken,
dann auf die Datei).

Der Code zeigt auf eine Adresse der Form
`https://nocodb.vibe-cortex.com/u/rueckmeldung-vorlesung-5-a7f3`.

**Diese Adresse ändert sich nie wieder.** Sie können den QR-Code in Ihre
Unterlagen einbauen, auch wenn Sie den Schutz später noch umstellen.

---

## 3. Die Auswertung ansehen

### Live-Dashboard (das Schnelle)

`https://grafana.vibe-cortex.com` → Ordner *Lehrveranstaltungen* →
**Umfrage-Auswertung**.

Oben zwei Auswahlfelder:

| Feld | Wirkung |
|---|---|
| **Umfrage** | welche Vorlesung |
| **Frage** | welche Frage ausgewertet wird |

Sie sehen dann: Anzahl der Antworten, wann die letzte kam, die Beteiligung
(bei geschützten Umfragen), ein Balkendiagramm der gewählten Frage, den
zeitlichen Verlauf und alle Antworten im Klartext.

**Die Seite aktualisiert sich alle zehn Sekunden von allein.** Sie können
sie während der Vorlesung auf den Beamer legen und zusehen, wie die
Antworten hereinkommen.

Steht bei „Beteiligung" der Text *keine Liste*, ist die Umfrage offen für
alle. Das ist kein Fehler.

### Tabelle ansehen (das Genaue)

Öffnen Sie `https://nocodb.vibe-cortex.com` und melden Sie sich an.
Links stehen Ihre Tabellen. Jede Umfrage hat ihre eigene. Hier können Sie
auch einzelne Antworten löschen, etwa Unsinn.

**Nach Gruppen sortieren:** Oben auf *Group By* klicken und ein Feld
wählen, zum Beispiel `Das Tempo war`. NocoDB zeigt dann, wie viele
Antworten auf jede Möglichkeit entfallen.

**Durchschnitt einer Bewertung:** Ganz unten in der Spalte auf das Feld
klicken und *Avg* wählen.

**Freitexte lesen:** Die Spaltenbreite lässt sich am rechten Rand
ziehen, oder Sie klicken eine Zeile auf.

---

## 4. Schutz nachträglich ein- oder ausschalten

Öffnen Sie in NocoDB die Tabelle **`Umfragen`**. Dort steht eine Zeile je
Umfrage.

| Spalte | Bedeutung |
|---|---|
| `geschuetzt` | Häkchen an: Matrikelnummer wird verlangt. Häkchen aus: offen für alle. |
| `offen` | Häkchen aus: die Umfrage nimmt nichts mehr an. So schließen Sie sie. |

Die Änderung wirkt **sofort** und der QR-Code bleibt gültig.

---

## 5. Matrikelnummern nachtragen

Öffnen Sie die Tabelle **`Zugelassen <Titel Ihrer Umfrage>`**.

**Einzeln:** unten auf `+` klicken und die Nummer eintippen.

**Viele auf einmal:** In NocoDB oben rechts auf die drei Punkte, dann
*Upload CSV*. Die Datei braucht eine Spalte `matrikelnummer`.

Die Spalte `abgestimmt` setzt das System selbst. Wenn jemand seine
Antwort noch einmal abgeben soll, nehmen Sie dort das Häkchen heraus.

---

## 6. Was mit den Daten passiert

- Alles liegt auf dem eigenen Server. Kein Airtable, kein Google, keine
  Übermittlung ins Ausland.
- **Namen werden nicht erhoben.** Es gibt kein Namensfeld, außer Sie
  legen selbst eines an. Tun Sie das nicht.
- **Auch bei geschützten Umfragen bleibt die Antwort anonym.** Die
  Matrikelnummer wird nur in der Zulassungsliste abgehakt. In der
  Antworttabelle steht sie nicht, und es gibt keine Verbindung zwischen
  beiden. Das ist wie im Wahllokal: Wählerverzeichnis und Urne sind
  getrennte Behälter.
- Diesen Satz können Sie den Studierenden so sagen. Er steht auch unter
  dem Formular.

---

## 7. Wenn etwas nicht geht

| Beobachtung | Ursache | Abhilfe |
|---|---|---|
| „Diese Umfrage gibt es nicht" | Kennung stimmt nicht | QR-Code neu scannen, Tabelle `Umfragen` prüfen |
| „Diese Umfrage ist geschlossen" | Häkchen `offen` ist weg | in `Umfragen` wieder setzen |
| „Diese Matrikelnummer steht nicht auf der Teilnehmerliste" | Nummer fehlt in der Zulassungsliste | dort nachtragen |
| „Ihre Eintrittskarte ist abgelaufen" | länger als 45 Minuten gebraucht | Seite neu laden, Nummer erneut eingeben |
| Formular zeigt keine Fragen | Tabelle hat noch keine Spalten | Umfrage neu anlegen |

---

## 8. Schneller Weg über Claude Code

Wer Claude Code benutzt, braucht n8n gar nicht zu öffnen:

- **„Leg mir eine Rückmeldung für Vorlesung 5 an"** → Claude fragt nach
  Fragen und Schutz und liefert den QR-Code als Bild zurück.
- **„Was kam bei der Rückmeldung zu Vorlesung 5 raus?"** → Claude holt die
  Antworten, rechnet die Zahlen aus und fasst die Freitexte zusammen.
- **„Mach die Umfrage zu"** oder **„Schalt den Schutz ein"** → sofort erledigt.

---

## Für Technikinteressierte

- **Was tauschbar ist:** Die Fragen stehen nur an einer Stelle, nämlich
  als Spalten der Antworttabelle. Das Formular wird daraus erzeugt.
  Wer eine Spalte hinzufügt, hat die Frage hinzugefügt.
- **Warum n8n nicht im Weg steht:** n8n legt die Umfrage an und ist
  danach raus. Beim Absenden reden die Studierenden mit dem Türsteher,
  der direkt in die Datenbank schreibt. Deshalb halten auch mehrere
  hundert gleichzeitig.
- **Beteiligte Dienste:** NocoDB (Tabellen), Türsteher (Formular und
  Zugangsprüfung), Grafana (Live-Auswertung), QR-Dienst, Gotenberg (PDF).
  Alle in Containern auf demselben Server. Aus dem Internet erreichbar sind
  nur NocoDB, Türsteher und Grafana.
- **Grafana liest nur mit**, mit einem eigenen Datenbankbenutzer ohne
  Schreibrecht. Es kann an den Antworten nichts verändern.
- **Im n8n-Workflow steckt genau ein Baustein mit Code**
  („Eingaben verstehen"), der getippte Zeilen in Tabellenspalten übersetzt.
  Alles andere sind Klickbausteine.
- **Test:** `/usr/bin/python3 test-umfrage-e2e.py` prüft die ganze Kette
  gegen die laufende Anlage und räumt hinter sich auf.
