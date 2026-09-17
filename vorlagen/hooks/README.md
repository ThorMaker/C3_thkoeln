# Leitplanken-Vorlage: Berechtigungsregeln und Hook

Beispiel aus dem Skript, Kapitel 2.9. Nicht aktiv, solange Sie es nicht in ein Projekt kopieren.

1. `settings-leitplanken.json` als `.claude/settings.json` in Ihr Projekt übernehmen (bestehende Einträge ergänzen, nicht überschreiben).
2. `schuetze_ordner.py` nach `.claude/hooks/` im Projekt kopieren.
3. Unter Windows im Befehl `python3` durch `python` ersetzen.
4. Prüfen: im Terminal `/permissions` und `/hooks` aufrufen; dann Claude bitten, eine Datei in `pruefungen/` zu ändern. Die Änderung muss mit der Meldung des Hooks abgelehnt werden.

**Wirkung:** Die Deny-Regeln sperren Lesen und Bearbeiten von `personendaten/`. Der Hook blockiert zusätzlich jede Dateiänderung in `pruefungen/` und `personendaten/`. Pushes nach GitHub fragen immer nach.
