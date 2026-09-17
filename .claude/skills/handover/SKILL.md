---
name: handover
description: Schreibt eine Übergabe (HANDOVER.md) mit Ziel, Stand, Entscheidungen, verworfenen Wegen, nächsten Schritten und Startprompt, damit nach /clear, nach einer Pause oder in einer neuen Sitzung nahtlos weitergearbeitet werden kann. Verwenden, wenn der Nutzer eine Übergabe oder einen Handover möchte, den Kontext aufräumen, die Sitzung abschließen, eine Pause machen oder die Arbeit an eine Kollegin oder einen Kollegen weitergeben will.
---

# Übergabe vorbereiten (vor /clear)

## Ziel
Eine neue Sitzung ohne jedes Vorwissen soll allein mit `HANDOVER.md` weiterarbeiten können. Schreibe für diese Leserin, nicht für dich.

## Vorgehen
1. Nennt der Nutzer beim Aufruf einen Fokus (etwa `/handover Fokus Literaturliste`), richte die Übergabe darauf aus.
2. Sammle aus der bisherigen Sitzung: Auftrag, erledigte Schritte, Entscheidungen mit Begründung, verworfene Wege, offene Punkte, geänderte Dateien.
3. **Prüfe den tatsächlichen Stand, statt dich auf den Verlauf zu verlassen:** In einem Git-Repository `git status` und `git diff --stat` ausführen, sonst die geänderten Dateien auflisten. Vorhandene Prüfbefehle (Tests, Prüfskripte) ausführen und das Ergebnis notieren.
4. Gibt es schon eine `HANDOVER.md`, verschiebe sie nach `docs/uebergaben/` mit Datum im Dateinamen, falls der Ordner existiert; sonst überschreibe sie.
5. Schreibe `HANDOVER.md` in den Projektordner, zeige sie vollständig und bitte um Prüfung.
6. Nenne am Ende den Startprompt und erinnere daran, dass der Mensch `/clear` selbst eingibt oder in der App eine neue Sitzung startet.

## Aufbau von HANDOVER.md (höchstens 80 Zeilen)

```markdown
# Übergabe: <Thema> (<JJJJ-MM-TT>)

## Ziel
<ein bis zwei Sätze>

## Stand
<was erledigt ist, was halb fertig ist>

## Entscheidungen
- <Entscheidung>: <Begründung>

## Verworfene Wege
- <Ansatz>: <warum verworfen>

## Nächste Schritte
1. <erster Schritt, so konkret, dass man sofort beginnen kann>
2. <…>

## Relevante Dateien
- `<pfad>`: <wofür>

## Prüfen
- `<Befehl>`: <aktuelles Ergebnis>

## Offene Fragen an den Menschen
- <Frage>

## Startprompt
Lies @HANDOVER.md, prüfe kurz den Stand mit <Befehl> und setze mit Schritt 1 der nächsten Schritte fort.
```

## Regeln
- Fakten statt Erzählung; nur, was die nächste Sitzung wirklich braucht.
- Unsicheres als unsicher kennzeichnen; nichts erfinden.
- Keine Zugangsdaten und keine personenbezogenen Daten Dritter in die Übergabe.
- Dauerhafte Erkenntnisse (Regeln, Stolperfallen) zusätzlich als Vorschlag für die `CLAUDE.md` nennen, aber nicht ungefragt eintragen.
