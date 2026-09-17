# Muster 2: n8n-Workflows als Werkzeuge für Claude Code

Claude Code soll nicht selbst in Systeme greifen, sondern freigegebene Workflows aufrufen (Skript, Kapitel 4.3).

## Weg A: MCP Server Trigger in einem Workflow

1. Neuen Workflow mit dem Knoten **MCP Server Trigger** anlegen, Authentifizierung einschalten (Bearer).
2. Einen Workflow als Werkzeug anhängen, zum Beispiel „Termin eintragen“ mit klaren Eingabefeldern.
3. Workflow aktivieren und die *Production URL* kopieren.
4. In Claude Code anbinden:

```bash
claude mcp add --transport http n8n-dekanat <production-url> --header "Authorization: Bearer <token>"
```

5. In Claude Code mit `/mcp` prüfen, ob die Werkzeuge sichtbar sind, und testen: „Trage den Termin aus termin.md über das n8n-Werkzeug ein.“

## Weg B: MCP-Zugang für die ganze Instanz

In den Einstellungen von n8n den instanzweiten MCP-Zugang einschalten, die Server-URL kopieren und einzelne Workflows freigeben. Ab n8n 2.13 können Clients darüber auch Workflows bauen und bearbeiten (Muster 3).

## Sicherheit

- Nur Workflows freigeben, die ein Agent auslösen darf; alle verbundenen Clients sehen alle freigegebenen Workflows.
- Token nie in eine geteilte `.mcp.json` schreiben.
- Workflows, die schreiben oder Mails senden, mit einer menschlichen Freigabe versehen.
