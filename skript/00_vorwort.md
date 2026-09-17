# Vorwort und Lesehinweise

Dieses Skript begleitet den Vortrag **„Claude Code, Automatisierung, Wissen: Wie KI-Agenten den Hochschulalltag erleichtern“** an der TH Köln am 18. September 2026. Es ist so geschrieben, dass Sie es auch ohne den Vortrag verstehen: Jedes Kapitel erklärt, **was** ein Werkzeug ist, **wie** man es benutzt, **wofür** es im Hochschulalltag taugt, **warum** es funktioniert und **wo seine Grenzen** liegen.

## Worum es geht

Sprachmodelle wie Claude haben sich in kurzer Zeit vom Chatfenster zum Arbeitswerkzeug entwickelt. Der entscheidende Schritt ist nicht ein klügeres Modell, sondern die Umgebung, in der es arbeitet: Ein Modell, das Dateien lesen, Befehle ausführen, Abläufe anstoßen und seine eigenen Ergebnisse prüfen kann, erledigt Aufgaben statt nur Fragen zu beantworten. Genau diese Entwicklung zeichnet das Skript nach.

Die Kapitelnummern entsprechen den Blöcken des Vortrags. Die Farben folgen dem Dreiklang der TH Köln: **Technology** für die Werkzeuge, **Arts** für die Gestaltung von Abläufen, **Sciences** für Wissen und Theorie, dazu der **Transfer** in Ihren Alltag.

| Kapitel | Thema                                      | Dreiklang  |
|---------|--------------------------------------------|------------|
| 1       | Grundlagen und Datenschutz                 | Technology |
| 2       | Claude Code und Arbeitsweise               | Technology |
| 3       | Selbst ausprobiert                         | Technology |
| 4       | Abläufe, die ohne Sie weiterlaufen         | Arts       |
| 5       | Wie Ihr Wissen zur KI kommt                | Sciences   |
| 6       | Zu mehreren am selben Stand arbeiten       | Sciences   |
| 7       | Wenn die KI sich selbst korrigiert         | Sciences   |
| 8       | Effizienz und nächste Schritte             | Transfer   |
| 9       | Anhang: Glossar, Befehle, Prompts, Quellen |            |

Das Skript gibt es als Gesamtausgabe und in drei Teilen passend zu den Vortragsabschnitten: Teil 1 mit den Kapiteln 1 bis 3, Teil 2 mit den Kapiteln 4 und 5, Teil 3 mit den Kapiteln 6 bis 10. Kapitel 10, das Glossar mit Fachbegriffen und Quellen, gibt es zusätzlich als eigenes PDF zum Weitergeben.

## Wie Sie mit dem Material arbeiten

Das Skript gibt es in zwei Formen:

- **Als PDF** zum Lesen und Nachschlagen.
- **Als GitHub-Repository** mit denselben Texten als Markdown, dazu alle Vorlagen, Beispielprojekte, Skills, ein Plugin, einen n8n-Workflow und Übungen.

Das Repository ist absichtlich so gebaut, dass Claude Code damit arbeiten kann. Wenn Sie den Ordner in Claude Code öffnen, liest Claude die mitgelieferte `CLAUDE.md` und kann Ihnen jedes Kapitel erklären, Verständnisfragen stellen oder die Übungen mit Ihnen durchgehen. Das Handout ist also zugleich das erste Übungsprojekt.

> **Merksatz:** Lesen Sie ein Kapitel, und fragen Sie danach Claude im Repository: „Prüfe mein Verständnis von Kapitel 2 mit fünf Fragen.“ So lernen Sie das Werkzeug mit dem Werkzeug.

## Kennzeichnungen

- **Merksatz:** die Kernaussage eines Abschnitts.
- **Praxis:** eine konkrete Anleitung zum Nachmachen.
- **Achtung:** eine Grenze, ein Risiko oder eine häufige Fehlerquelle.
- `Schreibmaschinenschrift`: Befehle, Dateinamen und Code, die Sie genau so eingeben.

## Quellen und Zitierweise

Im Hochschulkontext gilt: Jede Tatsachenbehauptung braucht einen Beleg. Das Skript zitiert deshalb nummeriert nach dem IEEE-Stil; jedes Kapitel hat sein eigenes Quellenverzeichnis. Webquellen tragen ein Abrufdatum, weil sich Produktdokumentationen laufend ändern. Wo möglich, werden Primärquellen zitiert (Originaldokumentation, Gesetzestext, Studie); Sekundärquellen wie Anleitungen Dritter sind als solche erkennbar und nur dort verwendet, wo keine Primärquelle vorlag. Mit dem Unteragenten `quellen-pruefer` aus dem Handout-Repository können Sie eigene Texte auf dieselbe Weise prüfen lassen (Kapitel 2.6).

## Stand und Gültigkeit

Stand dieses Skripts ist der **11. September 2026**. Produkte in diesem Feld ändern sich im Wochentakt: Menüpfade, Standardeinstellungen, Modellnamen und Preise können sich nach Redaktionsschluss verschoben haben. Wo eine Angabe für Ihre Arbeit entscheidend ist, prüfen Sie bitte die verlinkte Originaldokumentation.

> **Achtung:** Die Hinweise zu Datenschutz und Recht sind eine fachliche Einordnung, **keine Rechtsberatung**. Maßgeblich sind die KI-Richtlinie Ihrer Hochschule und die Einschätzung Ihrer bzw. Ihres Datenschutzbeauftragten.

## Voraussetzungen

Für die Übungen genügt ein Laptop mit der **Claude Desktop App** und einem **Pro-Konto** (oder höher). Im Code-Tab der App läuft Claude Code ohne separate Installation. Unter Windows braucht der Code-Tab zusätzlich **Git for Windows**. Für die weiterführenden Kapitel (n8n, Graphify, Graft) sind optionale Installationen beschrieben; sie sind für das Verständnis nicht nötig. Als Angehörige der TH Köln haben Sie außerdem kostenlos Zugang zu **THKI** (Kapitel 1).

## Autor

Der Referent ist Process & Solution Architect und leitet ein Team für NoCode und Prozessautomatisierung. Sein Arbeitsschwerpunkt sind selbst betriebene, datenschutzkonforme Automatisierungslösungen mit n8n, Datenbanken und KI-Werkzeugen wie Claude Code.
