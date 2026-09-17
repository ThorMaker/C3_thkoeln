# n8n-Workflow: Dekanat, Termine per Sprache

Der durchgehende Fall aus dem Vortrag (Skript, Kapitel 4) als importierbarer Workflow: Termin per Sprachnachricht anlegen, Rückmeldungen per Formular sammeln, Zusammenfassung mit Prüfschleife per Mail verschicken.

## Voraussetzungen

- Eine n8n-Instanz mit **Data Tables** (selbst betrieben oder n8n Cloud). Die Formulare müssen für Teilnehmende erreichbar sein; bei einer lokalen Instanz etwa über einen Tunnel.
- Ein API-Schlüssel für ein OpenAI-kompatibles Sprachmodell: Claude (Anthropic) oder THKI bzw. KI:connect.nrw.
- Optional ein Schlüssel für Transkription (OpenAI-Format, Cloud oder eigener Whisper-Server). Ohne Transkription funktioniert der Workflow mit Texteingabe.
- Ein SMTP-Zugang für den Mailversand.

## Einrichtung in zehn Schritten

1. **Data Tables anlegen** (Menü „Data tables“), alle Spalten vom Typ Text:
   - `termine`: `termin_id`, `titel`, `datum`, `uhrzeit`, `ort`, `teilnehmerkreis`, `rueckmeldung_bis`, `hinweise`, `transkript`, `erstellt_am`
   - `rueckmeldungen`: `rueckmeldung_id`, `termin_id`, `antwort`, `kommentar`, `erfahrung`, `bereich`, `hindernis`, `thema`, `anzahl_aufgaben`, `sonstiges`, `name`, `eingang`

     `erfahrung`, `thema` und `sonstiges` kamen im September 2026 dazu, als aus dem Feedbackbogen die
     Bedarfsabfrage wurde. In der **Data Table** reichen einzeilige Textfelder.

   - `Ideen` (nur Airtable, nicht als Data Table nötig): `idee_id`, `aufgabe`, `Rückmeldung`, `bereich`, `erfahrung`, `thema`, `eingang`

     Diese Tabelle ist der **Ideenspeicher**: Der Workflow schreibt je genannter Aufgabe eine eigene Zeile,
     zusätzlich zu den Aufgaben als Textzeilen am Rückmeldungssatz. Damit lässt sich einzeln filtern, gruppieren
     und zählen, welche Aufgabe wie oft genannt wurde. `idee_id` ist das Primärfeld, `Rückmeldung` ein
     *Link to another record* auf die Tabelle Rückmeldungen, `aufgabe` ein einzeiliges Textfeld.
     Fehlt die Tabelle, läuft der Workflow trotzdem durch: Der Knoten ist auf Weiterlaufen gestellt.
     `bereich`, `erfahrung` und `thema` tragen dieselben Werte wie in der Tabelle Rückmeldungen,
     die Optionen stehen in der Tabelle weiter unten.

     **In Airtable lohnt sich mehr:** Legen Sie `erfahrung`, `thema` und `antwort` als *Single Select* an,
     dann lässt sich im Interface danach gruppieren und die Verteilung entsteht von selbst. Die Optionen
     müssen **wörtlich** so heißen, am besten in dieser Reihenfolge, weil Airtable Auswahllisten in der
     Anlegereihenfolge sortiert:

     | Feld | Optionen, in dieser Reihenfolge |
     |---|---|
     | `erfahrung` | Noch nicht · Ausprobiert · Regelmäßig · Baue selbst |
     | `bereich` | Lehre · Verwaltung · Service · Leitung · Forschung · Sonstiges |
     | `hindernis` | Kein Einstieg · Datenschutz unklar · Keine Zeit · Zweifel an Qualität · Erlaubnis unklar · Schon dabei |
     | `thema` | Grundlagen und Datenschutz · Claude einstellen · Eigene Skills · Abläufe automatisieren · Dokumente durchsuchbar · Team-Zusammenarbeit · Eigener Fall |
     | `antwort` | Hat gereicht · Ein weiterer Termin · Zwei bis drei Blöcke · Regelmäßige Reihe · Noch unklar |

     `kommentar` wird ein **Long-Text-Feld**: Wer mehrere Aufgaben nennt, bekommt eine Zeile je Aufgabe.
     `anzahl_aufgaben` ist eine **Zahl**. Beides zusammen macht auswertbar, wer wie viel mitgebracht hat.

     Der Knoten **Rückmeldung aufbereiten** bildet die langen Formulartexte auf genau diese Werte ab.
     Achtung: Der Airtable-Knoten läuft mit `typecast`, und Airtable legt damit **jede unbekannte Option
     automatisch neu an**. Ein Leerzeichen Unterschied erzeugt also ein Duplikat statt eines Fehlers.
     Stehen in Airtable plötzlich zwei ähnliche Optionen nebeneinander, ist das die Ursache.
2. **Workflow importieren:** `dekanat-live-klammer.json` über „Import from File“.
   Danach in den drei **Airtable-Knoten** die eigene Base und die eigenen Tabellen auswählen.
   In der Datei stehen dort Platzhalter (`appIHREBASEID`), weil sie öffentlich liegt und niemand
   versehentlich in eine fremde Base schreiben soll. Die Auswahl ist ein Dropdown, kein Tippen.
3. **Credential „KI-Anbieter“** anlegen: Typ *Header Auth*, Name `Authorization`, Wert `Bearer <API-Schlüssel>`. In den Knoten **KI: Termin extrahieren** und **KI: Zusammenfassen** auswählen.
4. **Credential „Transkription“** analog anlegen und im Knoten **Transkribieren** auswählen (entfällt bei reiner Texteingabe).
5. **SMTP-Credential** anlegen und in **Mail: Zusammenfassung** und **Mail: Bitte prüfen** auswählen.
6. **Konfiguration** öffnen und anpassen: Modell, Mailadressen, Kalender. Basis-Adresse und Schlüssel der KI stehen in der Zugangsdatei des KI-Knotens, nicht hier.
7. **Data-Table-Knoten prüfen:** Die Tabellen sind über ihren Namen verknüpft. Zeigt ein Knoten eine Warnung, die Tabelle einmal aus der Liste auswählen.
8. **Workflow aktivieren** (veröffentlichen), damit die Produktions-URLs der Formulare gelten.
9. **Formular-URLs notieren:** In den drei Formular-Knoten die *Production URL* kopieren.
10. **QR-Code erzeugen** für das Rückmeldeformular: `python3 tools/qr_erzeugen.py <Production-URL>`.

## Testen

1. Formular **Termin anlegen** mit Text: „Vortrag Claude Code am 18. September um 14 Uhr, Rückmeldung bis zum Ende der Veranstaltung.“ In der Tabelle `termine` erscheint eine Zeile.
2. Drei Rückmeldungen über das Formular **Ihre Rückmeldung** abgeben.
3. Formular **Jetzt zusammenfassen** absenden. In den *Executions* sehen Sie jeden Schritt; die Mail kommt beim Empfänger an.
4. Prüfschleife testen: im Knoten **Prompt bauen** die Pflicht zu IDs entfernen und erneut auslösen. Die Execution zeigt den zweiten Versuch mit Korrekturhinweis.

Vor dem Echtbetrieb Testzeilen in beiden Tabellen löschen.

## Modellwechsel

| Feld in „Konfiguration“ | Claude | THKI bzw. KI:connect.nrw |
|---|---|---|
| Basis-URL | in der Zugangsdatei des KI-Knotens | laut THKI-Oberfläche; KI:connect: `https://chat.kiconnect.nrw/api/v1` |
| `llm_model` | `gpt-4.1` | laut Modellliste, z.B. `inferenz-mistral-small-4-119b` |

Dazu im Knoten **KI: …** die passende Credential wählen. Anthropic empfiehlt für den Produktivbetrieb die eigene Messages-Schnittstelle; das OpenAI-kompatible Format dient hier dem einfachen Wechsel.

## Datenschutz

Name ist freiwillig und geht nie an das Modell. Für den Echtbetrieb mit personenbezogenen Daten gelten die Ampel aus Kapitel 1.12 und die Handreichung der TH Köln. Transkription lokal betreiben, wenn Sprachaufnahmen den eigenen Rechner nicht verlassen sollen.

## Zweites Beispiel: Serienbrief als PDF (Gotenberg und QR-Dienst)

`dekanat-serienbrief.json` zeigt Muster 1 mit zwei kleinen Diensten, die in der Sandbox mitlaufen: Gotenberg macht aus HTML ein PDF, ein eigener QR-Dienst liefert QR-Codes als Bild. Je Empfänger entsteht ein Brief mit persönlichem QR-Code, das PDF geht als Mailanhang raus. Nichts verlässt das Sandbox-Netz.

1. Sandbox starten: `docker compose up -d` in `n8n/sandbox/` (zieht Gotenberg, baut den QR-Dienst) oder `./vortrag.sh sandbox-start` im Dozenten-Ordner.
2. http://localhost:5679 öffnen, Konto anlegen, SMTP-Credential anlegen: Host `mailpit`, Port `1025`, ohne SSL, ohne Anmeldung.
3. `dekanat-serienbrief.json` über „Import from File“ laden und im Knoten **Mail: Brief versenden** die Credential wählen.
4. **Start (manuell)** ausführen. Unter http://localhost:8025 liegen drei Mails mit `Brief_<Aktenzeichen>.pdf`.

Anpassen: Empfänger im Knoten **Empfänger (Beispieldaten)** (im Echtbetrieb eine Data Table oder eine Excel-Liste mit *Extract from File*), Text und Layout im Knoten **Brief als HTML**, Absender und Dienste in **Konfiguration**. Für den Echtbetrieb laufen Gotenberg und QR-Dienst auf dem eigenen Server, die Mail geht über das Postfach des Dekanats.

## Muster 2: den Workflow als Werkzeug für Claude Code

Siehe `mcp-muster2.md`.
