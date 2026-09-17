# Kapitel 8: Effizienz und nächste Schritte

Dieses Kapitel gehört zu **Block 8** des Vortrags (Transfer: Ihr Alltag).

**Lernziele:**

- Sie kennen die wichtigsten Studien zu Produktivitätsgewinnen durch KI und verstehen, warum ihre Ergebnisse so weit auseinanderliegen.
- Sie können eigene Automatisierungskandidaten mit einer Prozessinventur bewerten und den Effekt messen.
- Sie haben einen konkreten nächsten Schritt für die kommende Woche.

**Kernaussage:** Effizienz entsteht bei häufigen, klar prüfbaren Aufgaben. Messen Sie sie selbst, statt Studien pauschal zu glauben.

## 8.1 Die Evidenzlage

| Studie | Setting | Ergebnis | Einschränkung |
|----|----|----|----|
| Tamkin und McCrory, Anthropic [1] | 100.000 reale Claude-Gespräche, geschätzte Aufgabendauer | Aufgaben, die ohne KI im Schnitt rund 90 Minuten dauern würden, werden um etwa 80 % beschleunigt | Zeiten vom Modell geschätzt; Prüfaufwand außerhalb des Chats nicht erfasst |
| Becker et al., METR [2] | randomisiert kontrolliert: 16 erfahrene Open-Source-Entwickler, 246 Aufgaben in eigenen Codebasen | mit KI rund 19 % **langsamer**, obwohl sich die Beteiligten etwa 20 % schneller fühlten | Werkzeugstand Anfang 2025, Experten in vertrautem Code |
| Noy und Zhang [3] | Experiment mit beruflichen Schreibaufgaben | etwa 40 % weniger Zeit, höhere bewertete Qualität | kurze, klar umrissene Aufgaben |
| Brynjolfsson, Li und Raymond [4] | Feldstudie im Kundenservice | im Mittel rund 14 % mehr gelöste Anfragen pro Stunde, deutlich mehr bei Neulingen | ein Unternehmen, ein Aufgabentyp |
| Dell'Acqua et al. [5] | Experiment mit Beratenden | innerhalb der „Fähigkeitsgrenze“ schneller und besser; außerhalb deutlich häufiger falsche Lösungen | die Grenze ist für Nutzende unsichtbar |

Tamkin und McCrory weisen selbst darauf hin, dass große Produktivitätsgewinne historisch meist nicht durch das Werkzeug allein, sondern durch den **Umbau von Abläufen** entstanden sind [1].

## 8.2 Warum die Zahlen so weit auseinanderliegen

1.  **Aufgabentyp:** Formulieren, Zusammenfassen und Strukturieren profitieren stark [3]; tiefes Fachurteil in vertrautem Terrain kaum [2].
2.  **Vorwissen:** Neulinge gewinnen mehr als Erfahrene [4].
3.  **Prüfaufwand:** Jede KI-Ausgabe erzeugt eine Prüfpflicht. Ist das Prüfen so aufwendig wie das Selbermachen, schrumpft der Gewinn.
4.  **Wahrnehmung:** Menschen überschätzen ihren Zeitgewinn systematisch [2]. Gefühlte Effizienz ist keine gemessene Effizienz.
5.  **Unsichtbare Grenze:** Außerhalb dessen, was das Modell gut kann, verschlechtern sich Ergebnisse, ohne dass man es sofort merkt [5].

> **Merksatz:** Der größte Hebel ist selten „schneller schreiben“, sondern „Arbeit, die gar nicht mehr anfällt“.

## 8.3 Methode: die Prozessinventur

Ein bewährtes Vorgehen aus der Prozessautomatisierung: Jede Einheit schreibt ihre Alltagsprozesse auf und bewertet, wie oft sie vorkommen. Daraus lassen sich Kandidaten ableiten.

**Schritt 1, sammeln:** zehn wiederkehrende Aufgaben aus Lehre, Forschung und Verwaltung notieren.

**Schritt 2, bewerten:**

| Merkmal | Frage | Skala |
|----|----|----|
| Häufigkeit | Wie oft pro Monat? | Anzahl |
| Dauer | Wie lange jeweils? | Minuten |
| Automatisierbarkeit | Wie viel davon ist Muster statt Urteil? | 0 bis 1 |
| Prüfbarkeit | Lässt sich das Ergebnis leicht prüfen? | leicht, mittel, schwer |
| Risiko | Was passiert bei einem Fehler? | gering, mittel, hoch |
| Datenklasse | Ampel aus Kapitel 1.12 | grün, gelb, rot |

**Schritt 3, rechnen:**

```
Potenzial pro Monat (Minuten) = Häufigkeit × Dauer × Automatisierbarkeit
Netto-Nutzen im ersten Jahr    = 12 × Potenzial − Einrichtung − 12 × Pflege
```

**Schritt 4, priorisieren:** oben Aufgaben mit hohem Potenzial, leichter Prüfbarkeit, geringem Risiko und grüner Datenklasse. Rote Datenklasse schließt eine Umsetzung mit Verbraucherdiensten aus.

Im Handout-Repository gibt es dafür eine Tabellenvorlage (`vorlagen/prozessinventur.csv`), ein Rechenwerkzeug (`tools/prozessinventur.py`, das die Tabelle nach Netto-Nutzen sortiert) und den Skill `prozessinventur`, der Sie im Gespräch durch die Bewertung führt.

## 8.4 Rechenbeispiel: die Dekanats-Zusammenfassung

Annahmen: 4 Termine pro Monat, je 60 Minuten für Einsammeln, Abgleichen und Zusammenfassen, Automatisierbarkeit 0,75 (Prüfung und Rückfragen bleiben beim Menschen).

```
Potenzial     = 4 × 60 × 0,75            = 180 Minuten pro Monat
Einrichtung   = 8 Stunden                = 480 Minuten (einmalig)
Pflege        = 20 Minuten pro Monat
Netto Jahr 1  = 12 × 180 − 480 − 12 × 20 = 1.440 Minuten, also rund 24 Stunden
```

Ab dem zweiten Jahr entfällt die Einrichtung. Wichtiger als die Zahl ist die Qualität: Keine Rückmeldung geht mehr verloren, weil die Prüfschleife Vollständigkeit erzwingt.

## 8.5 Selbst messen

- **Vorher und nachher:** eine Aufgabe dreimal ohne und dreimal mit KI stoppen, einschließlich der Prüfzeit.
- **Fehler zählen:** Wie viele Korrekturen waren nötig? Fehler, die erst später auffallen, sind die teuersten.
- **Kosten pro akzeptiertem Ergebnis:** Zeit und Geld geteilt durch die Zahl der Ergebnisse, die Ihre Prüfung bestanden haben (Kapitel 7.8).
- **Nach einem Monat bilanzieren:** behalten, anpassen oder aufgeben.

## 8.6 Anregungen für den Hochschulalltag

| Bereich | Aufgabe | Werkzeug | Ampel |
|----|----|----|----|
| Lehre | Übungsaufgaben mit Musterlösung und Varianten | Chat oder Skill | grün |
| Lehre | Folien und Skript aus Stichpunkten aktualisieren | Claude Code im Materialordner | grün |
| Lehre | Evaluationsfreitexte thematisch bündeln | Skill, nur anonymisierte Daten | gelb |
| Forschung | Literatur verdichten und verknüpfen | Graphify, Second Brain | grün |
| Forschung | Auswertungsskripte schreiben und prüfen | Claude Code mit Tests | grün bis gelb |
| Verwaltung | Gremienprotokolle vorstrukturieren | Skill `gremien-protokoll` | gelb |
| Verwaltung | Terminabfragen einsammeln und zusammenfassen | n8n-Workflow mit Prüfschleife | gelb bis rot |

## 8.7 Ihre nächsten Schritte

| Zeitraum | Schritt |
|----|----|
| diese Woche | Einstellungen aus Kapitel 1 prüfen, einen eigenen Skill anlegen |
| diesen Monat | Prozessinventur mit zehn Aufgaben, THKI für eine interne Aufgabe testen |
| dieses Semester | einen Ablauf mit Prüfschleife bauen, ein Team-Repository für ein Projekt aufsetzen |

## Quellen

[1] A. Tamkin und P. McCrory, „Estimating AI productivity gains from Claude conversations“, Anthropic Research. Zugegriffen: 11. September 2026. [Online]. Verfügbar unter: <https://www.anthropic.com/research/estimating-productivity-gains>

[2] J. Becker, N. Rush, E. Barnes, und D. Rein, „Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity“, 2025, 2507.09089. Verfügbar unter: <https://arxiv.org/abs/2507.09089>

[3] S. Noy und W. Zhang, „Experimental evidence on the productivity effects of generative artificial intelligence“, *Science*, Bd. 381, Nr. 6654, S. 187-192, 2023, doi: [10.1126/science.adh2586](https://doi.org/10.1126/science.adh2586).

[4] E. Brynjolfsson, D. Li, und L. Raymond, „Generative AI at Work“, National Bureau of Economic Research, NBER Working Paper 31161, 2023. doi: [10.3386/w31161](https://doi.org/10.3386/w31161).

[5] F. Dell’Acqua *u. a.*, „Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of AI on Knowledge Worker Productivity and Quality“, Harvard Business School, Working Paper 24-013, 2023.
