# Kapitel 3: Selbst ausprobiert

Dieses Kapitel gehört zu **Block 3** des Vortrags. Es enthält die Übungen, die Sie im Raum oder später am eigenen Schreibtisch nachvollziehen können. Jede Übung nennt Zeitbedarf, Ziel, Schritte, das erwartete Ergebnis und typische Stolpersteine.

**Lernziel:** Sie haben Claude Code einmal selbst benutzt, ein Repository erkundet und einen eigenen Skill angelegt und getestet.

**Kernaussage:** In 15 Minuten zum ersten eigenen Skill, ohne Programmierkenntnisse.

## 3.1 Vorbereitung (vor der Übung)

| Punkt | Prüfen |
|----|----|
| Claude Desktop | aktuelle Version installiert, mit Pro-Konto angemeldet |
| Code-Tab | Oben in der App gibt es den Tab „Code“. Fehlt er, App aktualisieren und Plan prüfen. |
| Windows | Git for Windows installiert, App danach neu gestartet |
| Handout-Repository | als ZIP heruntergeladen und entpackt (siehe 3.2) |
| Datenschutz | Einstellungen aus Kapitel 1 gesetzt, Modelltraining aus |

## 3.2 Übung A: Das Handout-Repository erkunden (5 Minuten)

**Ziel:** erleben, dass Claude selbst die Dateien öffnet, die es für eine Antwort braucht.

1.  Handout-Repository auf GitHub öffnen, „Code“ und „Download ZIP“ wählen, ZIP entpacken.
2.  In Claude Desktop den Tab **Code** öffnen.
3.  Umgebung **Local** wählen, als Projektordner den entpackten Ordner `claude-hochschule-2026` auswählen.
4.  Berechtigungsmodus **Manual** wählen. So fragt Claude vor jeder Änderung.
5.  Ersten Auftrag eingeben:

```
Erkläre mir dieses Repository in fünf Sätzen. Ändere nichts.
```

6.  Nachfragen:

```
Welche Übung passt zu mir als Einsteigerin oder Einsteiger, und warum?
```

**Was Sie beobachten sollten:** Niemand kopiert Inhalte in einen Chat. Claude liest die `CLAUDE.md`, schaut sich die Ordnerstruktur an und öffnet gezielt einzelne Dateien. In der ausführlichen Ansicht (Transkript-Ansicht „Verbose“) sehen Sie jeden Lesezugriff.

**Weiterführend:** Bitten Sie den mitgelieferten Skill um eine Lernkontrolle:

```
/skript-tutor Prüfe mein Verständnis von Kapitel 1 mit drei Fragen.
```

## 3.3 Übung B: Ihr erster Skill (10 Minuten)

**Ziel:** eine wiederkehrende Aufgabe aus Ihrem Alltag als Skill festhalten und testen.

**Schritt 1, Aufgabe wählen.** Nehmen Sie etwas, das Sie regelmäßig tun und das einem Muster folgt. Vorschläge:

- eine Mail an Dekanat oder Prüfungsamt aus Stichpunkten,
- eine Rückmeldung auf eine Abschlussarbeits-Gliederung nach festem Raster,
- eine Ankündigung für die Lernplattform aus Terminangaben,
- eine Zusammenfassung eines Fachartikels nach Ihrem Schema.

**Schritt 2, Skill anlegen lassen.** Geben Sie im Code-Tab ein (Beispiel für die Dekanats-Mail, passen Sie die Aufgabe an):

```
Lege einen Projekt-Skill namens "mail-dekanat" an. Er soll aus meinen
Stichpunkten eine sachliche E-Mail an das Dekanat formulieren.
Fehlende Angaben (Anlass, Frist) soll er nachfragen.
Keine personenbezogenen Daten Dritter in Beispielen.
Zeige mir die SKILL.md, bevor du sie speicherst.
```

**Schritt 3, prüfen.** Lesen Sie die vorgeschlagene `SKILL.md`. Achten Sie besonders auf die Beschreibung im Kopfbereich: Sie entscheidet, ob Claude den Skill später von selbst erkennt. Gute Beschreibungen nennen, **was** der Skill tut und **wann** er verwendet werden soll.

**Schritt 4, speichern und testen.** Bestätigen Sie das Speichern. Der Skill liegt nun unter `.claude/skills/mail-dekanat/SKILL.md`. Starten Sie eine neue Sitzung im selben Ordner und testen Sie:

```
/mail-dekanat Raumwechsel Seminar Datenbanken, ab nächster Woche Raum 2.110,
Bitte um Aktualisierung im Vorlesungsverzeichnis bis Freitag
```

**Schritt 5, verbessern.** Wenn Ihnen etwas nicht gefällt, sagen Sie es Claude und lassen Sie die `SKILL.md` anpassen, zum Beispiel: „Betreffzeilen immer mit dem Kürzel der Lehrveranstaltung beginnen.“

**Erwartetes Ergebnis:** eine knappe Mail mit Betreff, Anliegen, Details, Bitte mit Frist und Gruß. Eine Musterlösung liegt im Repository unter `.claude/skills/mail-dekanat/SKILL.md`.

> **Merksatz:** Ein Skill ist nichts anderes als Ihre eigene Arbeitsanweisung, einmal sauber aufgeschrieben. Der Wert entsteht durch Wiederverwendung.

## 3.4 Übung C (zu Hause): Globale CLAUDE.md und Datenschutz-Profil (10 Minuten)

1.  Öffnen Sie `vorlagen/CLAUDE-global-nachher.md` und passen Sie die Abschnitte „Über mich“, „So arbeite ich“ und „Niemals“ an.
2.  Speichern Sie die Datei als `~/.claude/CLAUDE.md` (unter Windows `C:\Users\<Name>\.claude\CLAUDE.md`). Den Ordner `.claude` im Benutzerverzeichnis legt Claude Code beim ersten Start an; er ist versteckt.
3.  Übernehmen Sie die Einträge aus `vorlagen/settings-datenschutz.json` in `~/.claude/settings.json`. Existiert die Datei schon, ergänzen Sie nur die Einträge.
4.  Einfacher Weg: Bitten Sie Claude Code darum, mit Vorschau vor dem Speichern:

```
Lege mit der Vorlage vorlagen/CLAUDE-global-nachher.md meine globale
CLAUDE.md an. Frage mich vorher nach Fach, Rolle und Stilvorlieben.
Ergänze außerdem die Einträge aus vorlagen/settings-datenschutz.json in
~/.claude/settings.json, ohne bestehende Einträge zu löschen.
Zeige mir beide Dateien vor dem Speichern.
```

## 3.5 Übung D (zu Hause): Ein Plugin installieren (10 Minuten)

Das Handout-Repository ist zugleich ein **Plugin-Marketplace** [1] mit dem Plugin `hochschul-toolkit` (Skills für Gremienprotokolle und die Auswertung von Lehrveranstaltungs-Feedback sowie ein Befehl für Kurzfassungen).

**Weg 1, Kommandozeile** (wenn die CLI installiert ist):

``` bash
claude plugin marketplace add ThorMaker/c3_claudeCodeClub
claude plugin install hochschul-toolkit@hochschule-2026
```

Innerhalb einer CLI-Sitzung funktionieren dieselben Befehle mit vorangestelltem Schrägstrich: `/plugin marketplace add …` und `/plugin install …`.

**Weg 2, Claude Desktop:** „+“ neben dem Eingabefeld, „Plugins“, „Add plugin“. Der Plugin-Browser zeigt Plugins aus allen eingerichteten Marketplaces. Ist der Handout-Marketplace dort noch nicht eingerichtet, fügen Sie ihn einmalig über Weg 1 hinzu.

**Weg 3, ohne Plugin-System:** Kopieren Sie die Ordner aus `plugins/hochschul-toolkit/skills/` nach `~/.claude/skills/`. Die Skills stehen dann in allen Projekten zur Verfügung.

**Testen:**

```
Hier sind meine Stichpunkte aus der Institutssitzung: ... Mach daraus ein Protokoll.
```

Claude sollte den Skill `gremien-protokoll` von selbst erkennen.

## 3.6 Übung E (zu Hause): Übergabe und /clear (10 Minuten)

**Ziel:** erleben, wie eine Übergabedatei einen Neustart ohne Gedächtnisverlust ermöglicht.

1.  Arbeiten Sie im Handout-Repository ein paar Minuten an einer kleinen Aufgabe, zum Beispiel: „Erstelle aus Kapitel 1 einen Glossar-Entwurf mit zehn Begriffen als glossar-entwurf.md.“
2.  Brechen Sie mittendrin ab und geben Sie ein: `/handover`
3.  Lesen Sie die entstandene `HANDOVER.md`. Stimmen Stand und nächste Schritte? Korrigieren Sie, was fehlt.
4.  Geben Sie `/clear` ein (in der App: neue Sitzung mit Cmd+N bzw. Strg+N).
5.  Starten Sie mit dem Startprompt aus der Übergabe, etwa: `Lies @HANDOVER.md, prüfe kurz den Stand und setze mit Schritt 1 fort.`

**Erwartetes Ergebnis:** Claude macht dort weiter, wo Sie aufgehört haben, obwohl der Kontext leer war. Hintergrund und Entscheidungsregeln zu `/compact` und `/clear` stehen in Kapitel 1.3 [2].

## 3.7 Übung F (zu Hause): Ein echter Fehler im Plan-Modus (15 Minuten)

**Ziel:** die Agenten-Schleife (lesen, planen, handeln, beobachten) an einem echten Fehler erleben und den Plan-Modus als Sicherung nutzen (Kapitel 2.2).

1.  Öffnen Sie das Handout-Repository im Code-Tab, Modus **Manual**.
2.  Geben Sie ein: „In beispiele/literaturliste schlagen Tests fehl. Finde die Ursache. Ändere noch nichts.“
3.  Wechseln Sie in den Modus **Plan** und bitten Sie um einen Lösungsvorschlag. Prüfen Sie: Nennt der Plan die Sortierregel? Bleiben die Tests unverändert?
4.  Geben Sie den Plan frei. Claude ändert `literaturliste.py` und führt die Tests erneut aus.
5.  Sehen Sie sich die Änderung im Diff-Bereich an.

**Erwartetes Ergebnis:** Alle vier Tests bestehen, und `python3 literaturliste.py daten/literatur.json` gibt eine korrekt sortierte Liste aus, in der „Özdemir“ zwischen „Luhmann“ und „TH Köln“ steht.

**Beobachten Sie:** Sobald Claude im Unterordner arbeitet, liest es die dortige `CLAUDE.md` mit den Regeln für dieses Teilprojekt.

## 3.8 Wenn es hakt

Die folgenden Hinweise stützen sich auf die Fehlerhilfe der Dokumentation [3].

| Problem | Ursache | Lösung |
|----|----|----|
| Tab „Code“ fehlt | alte App-Version oder kein bezahlter Plan | App aktualisieren (macOS: Claude, Check for Updates; Windows: Help, Check for Updates), Plan prüfen |
| Meldung „Git is required“ (Windows) | Git for Windows fehlt | Git for Windows installieren, App komplett beenden und neu starten |
| Fehler 403 | Anmeldung abgelaufen | abmelden und neu anmelden |
| „Failed to load session“ | Ordner verschoben oder keine Rechte | anderen Ordner wählen, App neu starten |
| Skill wird nicht gefunden | falscher Pfad oder Kopfbereich fehlerhaft | Pfad muss `.claude/skills/<name>/SKILL.md` lauten; Kopfbereich zwischen zwei Zeilen mit `---`; neue Sitzung starten |
| Claude ändert zu viel | Modus zu offen | Modus „Manual“ oder „Plan“ wählen |
| Nutzungsgrenze erreicht | Kontingent des Pro-Plans für den Zeitraum verbraucht | Anzeige am Nutzungsring prüfen, später fortsetzen |

## 3.9 Zum Weiterdenken

1.  Welche drei Aufgaben aus Ihrem Alltag kommen häufig vor und folgen einem Muster? Wären sie grün, gelb oder rot nach der Ampel aus Kapitel 1?
2.  Was müsste ein Skill für Ihren Lehrstuhl oder Ihr Institut enthalten, damit neue Mitarbeitende ihn ohne Einweisung nutzen können?
3.  Wo würden Sie bewusst **keinen** Skill einsetzen, weil das menschliche Urteil der eigentliche Kern der Aufgabe ist?

## Quellen

[1] Anthropic, „Discover and install prebuilt plugins through marketplaces“, Claude Code Docs. Zugegriffen: 11. September 2026. [Online]. Verfügbar unter: <https://code.claude.com/docs/en/discover-plugins>

[2] Anthropic, „Manage costs effectively“, Claude Code Docs. Zugegriffen: 11. September 2026. [Online]. Verfügbar unter: <https://code.claude.com/docs/en/costs>

[3] Anthropic, „Desktop application“, Claude Code Docs. Zugegriffen: 11. September 2026. [Online]. Verfügbar unter: <https://code.claude.com/docs/en/desktop>
