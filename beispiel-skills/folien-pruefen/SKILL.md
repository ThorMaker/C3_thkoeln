---
name: folien-pruefen
description: Rendert geänderte PowerPoint-Folien nach PDF und sieht sie als Bild an, um Textüberläufe, abgeschnittene Überschriften und Überlappungen zu finden. Verwenden nach jeder Änderung an foliensatz/*.js, bevor eine Folie als fertig gilt. Auch verwenden, wenn ein Text "nicht passt", eine Karte zu voll wirkt oder jemand fragt, ob die Folie gut aussieht.
---

# Folien ansehen, nicht nur bauen

Die Generatoren melden keinen Fehler, wenn Text aus seinem Kasten läuft. PowerPoint
zeigt ihn einfach über dem nächsten Element an. Am 15.09.2026 sind so neun Folien mit
Überläufen entstanden, alle erst beim Ansehen aufgefallen, keine davon durch einen Test.

**Eine Folie gilt erst als fertig, wenn sie jemand als Bild gesehen hat.**

## Der Ablauf

```bash
# 1. Bauen
node foliensatz/folge1.js

# 2. Nach PDF rendern (LibreOffice läuft im Container, nicht auf dem Mac)
docker cp foliensatz/Foliensatz_Folge1.pptx n8n-sandbox-gotenberg-1:/tmp/f.pptx
docker exec n8n-sandbox-gotenberg-1 sh -c \
  "curl -s -o /tmp/f.pdf -F 'files=@/tmp/f.pptx' http://localhost:3000/forms/libreoffice/convert"
docker cp n8n-sandbox-gotenberg-1:/tmp/f.pdf /tmp/f.pdf

# 3. Nur die geänderten Folien als Bild, 90 dpi reicht
pdftoppm -png -r 90 -f 9 -l 11 /tmp/f.pdf /tmp/folie
```

Dann jedes Bild einzeln ansehen. Läuft der Container nicht:
`docker ps | grep goten`. Ist keiner da, entfällt die Sichtprüfung, und das muss
ausdrücklich gesagt werden, statt sie stillschweigend zu überspringen.

## Worauf zu achten ist

| Fehlerbild | Ursache | Abhilfe |
|---|---|---|
| Überschrift zweizeilig, läuft in die Karten | Titel länger als etwa 48 Zeichen | Titel kürzen, nicht die Karten verschieben |
| Letzter Stichpunkt ragt unter der Karte heraus | Kartenhöhe zu knapp für die Zeilen | Karte höher **oder** Stichpunkt auf eine Zeile kürzen |
| Zwei Textblöcke berühren sich | Abstand unter 0,25 Zoll | mindestens 0,3 Zoll Luft lassen |
| Kartentitel bricht um | `titleSize` zu groß für die Kartenbreite | `titleSize` senken oder Titel kürzen |

## Die Maße, die man ständig braucht

Folie ist 13,333 mal 7,5 Zoll.

| Bereich | von | bis |
|---|---|---|
| Kicker | 0,50 | 0,85 |
| Überschrift | 0,90 | 1,75 |
| **Inhalt** | **1,85** | **6,45** |
| Quellenzeile | 6,55 | 6,83 |
| Fußzeile und Logo | 6,62 | 7,24 |

Linker Rand 0,6, nutzbare Breite 12,13. Zwei Spalten: 5,9 breit, rechte beginnt bei 6,83.
Drei Karten: 3,9 breit im Abstand 4,12. Fünf Spalten: 2,3 breit im Abstand 2,45.

**Faustregel für Text:** Bei 15 pt passen rund 55 Zeichen auf eine Zeile von 5,3 Zoll
Breite, und eine Zeile ist etwa 0,21 Zoll hoch. LibreOffice setzt etwas weiter als
PowerPoint: Was im Rendern gerade eben passt, ist zu knapp.

## Was `card()` von der Höhe verbraucht

Ab der Kartenoberkante: 0,25 Luft, dann Kicker 0,4, dann Titel 0,68, dann der Text,
und unten bleiben 0,15. Eine Karte mit Kicker, Titel und drei zweizeiligen Stichpunkten
bei 15 pt braucht also mindestens 2,9 Zoll Höhe.

## Prüffrage

**Habe ich jede geänderte Folie als Bild gesehen?** Nicht den Foliensatz, nicht die
Nachbarfolien: jede geänderte. Wer nur baut und nicht ansieht, liefert Überläufe aus.
