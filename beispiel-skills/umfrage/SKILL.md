---
name: umfrage
description: Legt eine neue Lehrveranstaltungs-Umfrage an (Tabelle, Formular, optionaler Matrikelnummern-Schutz, QR-Code) auf Thors eigenem Server. Trigger - "/umfrage", "neue Umfrage", "Rueckmeldung fuer Vorlesung", "QR-Code fuer Feedback", "Abstimmung anlegen".
---

<!-- AI-assisted: Claude, human-reviewed ausstehend, Stand 2026-09-17 -->

# Umfrage anlegen

Legt in etwa einer Minute eine vollstaendige, DSGVO-konforme Umfrage an:
Tabelle in NocoDB, Formular hinter dem Tuersteher, optional geschuetzt durch
eine Matrikelnummernliste, dazu den fertigen QR-Code als PNG.

Alles laeuft auf Thors Server. Kein Airtable, kein Google, keine Uebermittlung
ins Ausland.

## Wann dieser Skill

- „Mach mir eine Rueckmeldung fuer Vorlesung 5"
- „Ich brauche einen QR-Code fuer Feedback am Freitag"
- „Umfrage anlegen, nur fuer die Teilnehmenden aus meinem Kurs"

Nicht fuer: Auswertung bestehender Umfragen, dafuer ist `umfrage-auswerten`.

## Was du zuerst klaeren musst

Frage nur nach, was fehlt. Rate nichts.

1. **Titel** der Umfrage.
2. **Fragen**, eine je Zeile, in dieser Schreibweise:
   ```
   Wie verstaendlich war die Vorlesung? | Bewertung
   Das Tempo war | Auswahl: zu langsam, genau richtig, zu schnell
   Was sollen wir vertiefen? | Text
   ```
   Arten: `Bewertung` (fuenf Sterne), `Auswahl: a, b, c`, `Text`, `Zahl`,
   `JaNein`. Ohne Angabe wird es ein einzeiliges Textfeld.
   Schlaegt Thor keine Fragen vor, biete drei passende an und lass ihn kuerzen.
3. **Geschuetzt oder offen?** Geschuetzt heisst: nur wer seine Matrikelnummer
   auf der Liste hat, kommt zum Formular. Wenn geschuetzt, brauchst du die
   Nummern (Liste, CSV-Text oder Dateipfad).

**Sag dazu:** Die Entscheidung ist nicht endgueltig. Der Schutz laesst sich
spaeter per Haken umlegen, der QR-Code bleibt gueltig.

## Ablauf

Nutze das Skript, nicht einzelne curl-Aufrufe:

```bash
/usr/bin/python3 ~/.claude/skills/umfrage/anlegen.py \
  --titel "Rueckmeldung Vorlesung 5" \
  --fragen-datei /tmp/fragen.txt \
  --geschuetzt \
  --nummern-datei /tmp/matrikel.csv \
  --qr /tmp/qr-vl5.png
```

Ohne `--geschuetzt` entfaellt `--nummern-datei`. Das Skript legt die
Zulassungsliste trotzdem an, damit der Schutz spaeter nachruestbar ist.

Danach:
1. Den QR-Code mit `SendUserFile` an Thor schicken.
2. Die drei Adressen nennen: Formular, Live-Auswertung, Tabelle.
3. Den QR-Code gegenpruefen (macht das Skript selbst, wenn `cv2` da ist).

## Grenzen, die du nennen musst

- **Kein Namensfeld anlegen.** Auch wenn Thor danach fragt: erst darauf
  hinweisen, dass damit die Anonymitaet faellt und sein bester Satz zum
  Datenschutz verloren geht.
- Die Kennung in der Adresse ist zufaellig und **nicht erratbar**, aber die
  Adresse selbst ist nicht geheim. Der Schutz kommt aus der Matrikelnummer,
  nicht aus der Adresse.
- Bei mehreren hundert Teilnehmenden gilt: alles haelt, weil n8n beim
  Absenden nicht beteiligt ist.

## Wenn etwas schiefgeht

| Meldung | Ursache | Abhilfe |
|---|---|---|
| `Auswahl ohne Werte` | `Auswahl:` ohne Moeglichkeiten dahinter | Werte ergaenzen |
| `Keine Frage erkannt` | Fragenliste leer | mindestens eine Zeile |
| HTTP 401 von NocoDB | Token abgelaufen oder falsch | `ssh n8n-server 'cat ~/.nocodb_api_token'` |
| Tabelle existiert schon | gleicher Titel zweimal | Titel aendern, z.B. Datum anhaengen |

## Hintergrund

Es gibt **einen** n8n-Workflow („Umfrage anlegen (NocoDB, QR-Code)",
`vo0OZr9aI4KXHzaj`) fuer alle Umfragen. Er wird nie kopiert. Dieser Skill
macht dasselbe direkt ueber die Schnittstelle, ohne n8n zu oeffnen.

Vollstaendige Beschreibung fuer Menschen:
`~/projekte/hochschulreferent/ANLEITUNG-umfrage.md`
