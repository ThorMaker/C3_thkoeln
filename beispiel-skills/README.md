<!-- AI-assisted: Claude (Fable 5.1), human-reviewed: ausstehend, Stand 18.09.2026 -->
# Beispiel-Skills aus der Vorbereitung dieser Reihe

Skills, die beim Bauen des Kick-offs wirklich im Einsatz waren. Jeder ist eine Textdatei
`SKILL.md` mit Kopf (Name, wann er greift) und Anleitung. Zum Ausprobieren einen Ordner nach
`~/.claude/skills/` kopieren, neue Sitzung starten, fertig.

| Skill | Wofür | Entstanden aus |
|---|---|---|
| `vortrag-sparring` | zerpflückt eine Idee für Vortrag oder Kurs, bevor Folien entstehen; widerspricht statt zuzustimmen | dem Wunsch nach einem Sparringspartner statt Ja-Sager |
| `js-folien-schreiben` | die Fallstricke beim Bauen von Folien als Code | drei Fehlern, die je zweimal Zeit gekostet haben |
| `folien-pruefen` | rendert geänderte Folien und sieht sie als Bild an, bevor sie als fertig gelten | Textüberläufen, die niemand im Code sieht |
| `folien-nachziehen` | prüft, welche Dateien mitziehen müssen, wenn eine Folie sich ändert | Dokumenten, die nach einem Umbau veraltet waren |
| `vortragssprache` | Sprachregeln für Folien und Sprechtext: erst erklären, dann benutzen | dem Publikum, das keine Programmierer sind |
| `umfrage` | legt eine anonyme Umfrage mit QR-Code auf dem eigenen Server an | der Bedarfsabfrage des Kick-offs (braucht die Strecke aus `n8n/umfrage/`) |
| `umfrage-auswerten` | wertet aus, mit Regeln für die Deutung: Streuung nennen, unter fünf Antworten keine Aussage | dem Wunsch, dass Zahlen nicht schöngeredet werden |

Die vier Folien-Skills verweisen auf Werkzeuge des Dozenten-Repositorys, die hier nicht enthalten
sind; lesenswert sind sie trotzdem, weil sie zeigen, wie aus einem wiederholten Fehler eine Regel
wird. Die beiden Umfrage-Skills brauchen einen eigenen Server mit NocoDB, siehe `n8n/umfrage/`.
