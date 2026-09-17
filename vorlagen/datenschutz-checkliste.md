# Datenschutz-Checkliste für Claude an der Hochschule

Stand: 11.09.2026. Menüpfade und Bezeichnungen können sich ändern. Keine Rechtsberatung.

## In der Claude-App (Web, Desktop, Mobil)
Wege: unten links auf Ihren Namen, dann **Einstellungen**. Mobil: Name bzw. Menü, dann Einstellungen.

- [ ] **Einstellungen › Datenschutz:** „Help improve Claude“ (Modelltraining) **aus**
- [ ] **Einstellungen › Datenschutz:** „Location metadata“ **aus**, auf **jedem** Gerät
- [ ] **Einstellungen › Memory:** „Generate memory from chat history“ bewusst ein- oder ausgeschaltet
- [ ] **Einstellungen › Memory:** „Search and reference chats“ bewusst ein- oder ausgeschaltet
- [ ] **Neuer Chat › Geist-Symbol oben rechts:** Incognito-Chat für sensible Einzelfragen bekannt (nicht im Verlauf, aber 30 Tage gespeichert)
- [ ] **Unter Antworten:** keine Daumen-Bewertungen bei sensiblen Chats (Feedback wird bis zu fünf Jahre aufbewahrt)
- [ ] **Einstellungen › Konnektoren:** nur benötigte Dienste verbunden, dienstliche Konten nur nach Freigabe

## In Claude Code
- [ ] `~/.claude/settings.json` mit Datenschutz-Profil (siehe `settings-datenschutz.json`). Der Ordner `.claude` ist versteckt: im Finder mit Cmd+Shift+Punkt einblenden, unter Windows im Explorer „Ansicht“, „Ausgeblendete Elemente“.
- [ ] Bei der Frage „Can Anthropic look at your session transcript?“ mit **No** antworten, wenn vertrauliches Material im Spiel ist
- [ ] Auf gemeinsam genutzten Rechnern: lokale Sitzungsprotokolle unter `~/.claude/projects/` beachten

## Vor jeder Eingabe: die Ampel
- **Grün** (Claude Pro, Training aus): eigene Texte, öffentliche Quellen, Lehrmaterial ohne Personenbezug
- **Gelb** (THKI, nach Handreichung): interne Hochschulinformationen ohne Personenbezug
- **Rot** (nur mit Vertrag und Freigabe oder lokal, im Zweifel gar nicht): Daten von Studierenden und Beschäftigten, Noten, Gutachten, Forschungsdaten Dritter, Verlagstexte, Zugangsdaten

## TH Köln
- [ ] Handreichung für Lehrende zu THKI gelesen (Lehrpfade der TH Köln)
- [ ] THKI unter https://ki.th-koeln.de ausprobiert (Anmeldung mit campusID)
- [ ] Ansprechstelle bekannt: Zentrum für Lehrentwicklung, digitalelehre@th-koeln.de
