# n8n-Sandbox: eine Umgebung, in der Claude alles darf

Ziel: Claude Code soll Workflows bauen, ändern, ausführen und wieder löschen dürfen, ohne dass etwas Echtes passieren kann. Die Sicherheit kommt nicht aus Vertrauen in das Modell, sondern aus der Umgebung (Skript, Kapitel 2.9 und 4.6).

## Was die Sandbox abschottet

| Schicht | Umsetzung |
|---|---|
| Eigene Instanz | eigener Container, eigene Datenbank, eigener Verschlüsselungsschlüssel; getrennt von der Produktivinstanz |
| Keine echten Zugangsdaten | nur Testschlüssel mit Ausgabenlimit; SMTP zeigt auf Mailpit, dort landen alle Mails |
| Kein Zugriff aufs eigene Netz | SSRF-Schutz sperrt private Adressen, localhost und Cloud-Metadaten; Port nur auf 127.0.0.1 |
| Riskante Knoten gesperrt | Befehle ausführen, Dateien lesen und schreiben, SSH, FTP |
| Wegwerfbar | `docker compose down -v` löscht alles; danach frisch starten |
| Getrennte Rechte in Claude Code | eigener MCP-Server `n8n-sandbox` ohne Rückfrage, die Produktivinstanz `n8n-mcp` nur mit Rückfrage |

## Einrichten (Mac mit Docker Desktop)

```bash
cd ~/projekte/claude-hochschule-2026/n8n/sandbox
cp env.beispiel .env
sed -i '' "s/bitte-ersetzen/$(openssl rand -hex 32)/" .env
docker compose up -d
```

1. http://localhost:5679 öffnen, Konto anlegen.
2. SMTP-Zugangsdaten anlegen: Host `mailpit`, Port `1025`, ohne SSL, ohne Anmeldung. Mails ansehen: http://localhost:8025
3. Einen Testschlüssel für das Sprachmodell hinterlegen, am besten mit Ausgabenlimit.
4. Unter Settings > Instance-level MCP den Zugang einschalten und einen Token erzeugen.
5. In Claude Code als zweiten Server eintragen:
   ```bash
   bash ~/n8n-mcp-einrichten.sh n8n-sandbox http://localhost:5679/mcp-server/http
   ```
6. Im Projektordner der Experimente `claude-berechtigungen.json` als `.claude/settings.json` übernehmen: Die Sandbox braucht keine Rückfragen, die Produktivinstanz schon.

## Dienste in der Sandbox

| Dienst | Zweck | Erreichbar |
|---|---|---|
| `n8n` | Workflows bauen und ausführen | http://localhost:5679 |
| `mailpit` | fängt alle Mails ab | http://localhost:8025 |
| `gotenberg` | HTML und Office-Dateien nach PDF (Chromium und LibreOffice eingebaut) | nur im Sandbox-Netz: `http://gotenberg:3000` |
| `qr-dienst` | QR-Codes als PNG, eigener Mini-Dienst aus `qr-dienst/` (Python, ohne Root) | nur im Sandbox-Netz: `http://qr-dienst:8080/qr.png?text=…` |

n8n darf diese Namen trotz SSRF-Schutz ansprechen (`N8N_SSRF_ALLOWED_HOSTNAMES`). Beispiel dazu: `../dekanat-serienbrief.json`. Weitere Dienste nach demselben Muster: ein Container, ein Name, eine Zeile in der Freigabe.

## Auf dem eigenen Server statt lokal

Dieselbe Datei funktioniert auf dem Server. Dann eine eigene Subdomain (z.B. `sandbox.…`) mit Zugangsschutz im Reverse Proxy, `N8N_HOST`, `N8N_PROTOCOL=https`, `WEBHOOK_URL` und `N8N_SECURE_COOKIE=true` in `.env` setzen und den Port nicht öffentlich freigeben. Wichtig: nicht in dasselbe Docker-Netz wie die Produktivinstanz hängen.

## Grenzen

- Der SSRF-Schutz ist eine zusätzliche Schicht; die eigentliche Grenze ist das Netz (Firewall, getrenntes Docker-Netz).
- Ein Testschlüssel für das Sprachmodell kostet echtes Geld: Ausgabenlimit setzen.
- Was in der Sandbox gebaut ist, kommt nur nach menschlicher Prüfung in die Produktivinstanz (Export, Import, Zugangsdaten neu wählen).
