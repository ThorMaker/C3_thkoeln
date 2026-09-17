#!/usr/bin/env python3
"""Erzeugt den n8n-Workflow „Umfrage zusammenfassen (NocoDB, KI)“ als n8n-umfrage-zusammenfassen.json.

Warum: Am Ende eines Termins drückt ein Mensch in Grafana auf „Zusammenfassen“. Erst dann
liest der Ablauf die Antworten aus NocoDB, lässt die KI zusammenfassen, prüft per Code, dass
jede Antwort mit ihrer Nummer belegt ist (sonst bis zu drei Versuche), legt das Ergebnis in
der NocoDB-Tabelle `zusammenfassungen` ab und zeigt es als Seite an. Grafana liest dieselbe
Tabelle, das Ergebnis erscheint also auch im Dashboard.

Der Knopf ist ein Link auf den Webhook (GET), weil ein Link in Grafana ohne Zusatzmodul und
ohne CORS-Freigabe funktioniert. Der Webhook-Pfad ist offen (kein 401, geprüft am 17.09.).

Aufruf:  /usr/bin/python3 n8n-umfrage-zusammenfassen.py     schreibt die JSON-Datei
Import:  in n8n „Import from file“, danach aktivieren. Zugangsdaten (NocoDB API Token,
         th-assist) sind im Export bereits zugeordnet, weil sie in der Instanz existieren.

AI-assisted: Claude (Fable 5.1), human-reviewed: ausstehend, Stand 17.09.2026
"""
import json
import uuid
from pathlib import Path

ZIEL = Path(__file__).with_suffix(".json")
NOCODB = {"nocoDbApiToken": {"id": "GhAnCXTtzgWiLOYE", "name": "NocoDB API Token"}}
OPENAI = {"openAiApi": {"id": "DMUo3dukcG9RCfVp", "name": "th-assist"}}
PFAD = "umfrage-zusammenfassen"


def uid(name):
    return str(uuid.uuid5(uuid.NAMESPACE_URL, "zusammenfassen/" + name))


def node(name, typ, version, pos, params, **extra):
    n = {"id": uid(name), "name": name, "type": typ, "typeVersion": version, "position": pos, "parameters": params}
    n.update(extra)
    return n


def code(name, pos, js):
    return node(name, "n8n-nodes-base.code", 2, pos, {"jsCode": js.strip("\n")})


def nocodb_get(name, pos, url):
    return node(name, "n8n-nodes-base.httpRequest", 4.2, pos, {
        "method": "GET", "url": url, "authentication": "predefinedCredentialType",
        "nodeCredentialType": "nocoDbApiToken", "options": {}}, credentials=NOCODB)


def sticky(name, pos, w, h, text, color):
    return node(name, "n8n-nodes-base.stickyNote", 1, pos, {"content": text, "width": w, "height": h, "color": color})


def cond_bool(expr, cid):
    return {"conditions": {"options": {"caseSensitive": True, "leftValue": "", "typeValidation": "strict", "version": 2},
                           "conditions": [{"id": uid(cid), "leftValue": expr, "rightValue": "",
                                           "operator": {"type": "boolean", "operation": "true", "singleValue": True}}],
                           "combinator": "and"}, "options": {}}


KI_TEXT = r"""
function kiText(j) {
  if (typeof j === 'string') return j;
  for (const k of ['content', 'text', 'output_text', 'message']) {
    const v = j?.[k];
    if (typeof v === 'string') return v;
    if (v && typeof v === 'object' && typeof v.content === 'string') return v.content;
  }
  if (Array.isArray(j?.output)) {
    const t = j.output.flatMap(o => (o.content || [])).map(c => c?.text).filter(Boolean).join('\n');
    if (t) return t;
  }
  return JSON.stringify(j);
}
"""

# Spalten, die NocoDB selbst pflegt und die nicht in den Prompt gehören
SYSTEM = "['Id','CreatedAt','UpdatedAt','nc_created_by','nc_updated_by','nc_order','__nc_deleted','nc_row_meta']"

nodes = [
    sticky("Notiz Überblick", [-200, -420], 720, 300, """## Umfrage zusammenfassen (NocoDB, KI)

**User Story:** Als Lehrende drücke ich am Ende des Termins in Grafana auf „Zusammenfassen“ und bekomme eine Seite mit der Auswertung: wer im Raum war, welche Aufgaben sich wiederholen, was gewünscht wird. Nichts läuft von allein, der Knopf ist die Entscheidung.

**Ablauf:** Link aus Grafana (GET, `?kennung=…`) → Steuertabelle liefert die Antworttabelle → Antworten lesen → Prompt mit Nummern R-1, R-2 … → KI → Code prüft, ob jede Nummer belegt ist (höchstens drei Versuche) → Ergebnis nach NocoDB `zusammenfassungen` → Seite anzeigen. Grafana zeigt dieselbe Tabelle.

**Nur zwei Code-Bausteine**, und beide sind unvermeidbar: „Prompt bauen“ (nummerierte Zeilen aus beliebigen Spalten) und „Prüfen“ (der Sinn des Ablaufs). Alles andere sind Klickbausteine. Einstellungen nur in „Konfiguration“.

Quelle: `n8n-umfrage-zusammenfassen.py` (Generator). AI-assisted: Claude, human-reviewed ausstehend, 17.09.2026""", 4),
    sticky("Notiz Prüfschleife", [1400, -420], 620, 220, """## Warum die Schleife

Die KI muss jede Antwort mit ihrer Nummer belegen. Fehlt eine Nummer oder ist eine erfunden, geht der Entwurf mit dem Befund zurück, höchstens dreimal. Danach wird gespeichert, aber als unvollständig markiert, und die Seite sagt es. Unter fünf Antworten sagt die KI ausdrücklich, dass sich nichts ableiten lässt.

Modell und Grenzen stehen in „Konfiguration“, nicht im Code.""", 5),

    node("Knopf: Zusammenfassen", "n8n-nodes-base.webhook", 2.1, [-200, 0], {
        "httpMethod": "GET", "path": PFAD, "responseMode": "responseNode", "options": {}},
        webhookId=uid("webhook")),
    node("Konfiguration", "n8n-nodes-base.set", 3.4, [40, 0], {"mode": "manual", "assignments": {"assignments": [
        {"id": uid("k1"), "name": "nocodb_url", "value": "https://nocodb.vibe-cortex.com", "type": "string"},
        {"id": uid("k2"), "name": "steuer_id", "value": "mxnrok36754lt25", "type": "string"},
        {"id": uid("k3"), "name": "ziel_id", "value": "TABELLE_ZUSAMMENFASSUNGEN", "type": "string"},
        {"id": uid("k4"), "name": "llm_model", "value": "gpt-4.1", "type": "string"},
        {"id": uid("k5"), "name": "max_versuche", "value": 3, "type": "number"},
        {"id": uid("k6"), "name": "max_worte", "value": 700, "type": "number"},
        {"id": uid("k7"), "name": "kennung", "value": "={{ $json.query.kennung || '' }}", "type": "string"},
    ]}, "options": {}}),
    # Die Kennung filtert NocoDB selbst (where=), ein Klickbaustein übernimmt die Felder: kein Code nötig.
    nocodb_get("NocoDB: Umfrage finden", [280, 0],
               "={{ $json.nocodb_url }}/api/v2/tables/{{ $json.steuer_id }}/records?where=(kennung,eq,{{ $json.kennung }})&limit=1"),
    node("Umfrage gefunden?", "n8n-nodes-base.if", 2.2, [520, 0], {
        "conditions": {"options": {"caseSensitive": True, "leftValue": "", "typeValidation": "strict", "version": 2},
                       "conditions": [{"id": uid("if-gefunden"), "leftValue": "={{ ($json.list || []).length }}",
                                       "rightValue": 0, "operator": {"type": "number", "operation": "gt"}}],
                       "combinator": "and"}, "options": {}}),
    node("Seite: Kennung unbekannt", "n8n-nodes-base.respondToWebhook", 1.1, [760, 200], {
        "respondWith": "text",
        "responseBody": "={{ '<!doctype html><html lang=\"de\"><meta charset=\"utf-8\"><body style=\"font-family:sans-serif;max-width:700px;margin:40px auto\"><h1>Umfrage nicht gefunden</h1><p>Zur Kennung „' + $(\'Konfiguration\').first().json.kennung + '“ gibt es keine Zeile in der Steuertabelle „Umfragen“. In Grafana oben die Umfrage wählen, dann erneut klicken.</p></body></html>' }}",
        "options": {"responseHeaders": {"entries": [{"name": "Content-Type", "value": "text/html; charset=utf-8"}]}}}),
    node("Umfrage wählen", "n8n-nodes-base.set", 3.4, [760, 0], {"mode": "manual", "assignments": {"assignments": [
        {"id": uid("u1"), "name": "titel", "value": "={{ $json.list[0].titel }}", "type": "string"},
        {"id": uid("u2"), "name": "kennung", "value": "={{ $json.list[0].kennung }}", "type": "string"},
        {"id": uid("u3"), "name": "antwort_tabelle", "value": "={{ $json.list[0].antwort_tabelle }}", "type": "string"},
    ]}, "options": {}}),
    nocodb_get("NocoDB: Antworten lesen", [1000, 0],
               "={{ $('Konfiguration').first().json.nocodb_url }}/api/v2/tables/{{ $json.antwort_tabelle }}/records?limit=1000"),
    code("Prompt bauen", [1240, 0], r"""
const cfg = $('Konfiguration').first().json;
const umfrage = $('Umfrage wählen').first().json;
const rows = ($('NocoDB: Antworten lesen').first().json.list || []).filter(r => !r.__nc_deleted);
const SYSTEM = """ + SYSTEM + r""";
const fragen = rows.length ? Object.keys(rows[0]).filter(k => !SYSTEM.includes(k)) : [];
const versuch = $runIndex + 1;              // jeder Durchlauf der Schleife erhöht den Zähler
const vorher = versuch > 1 ? $json : null;  // beim Wiederholen: Ergebnis der Prüfung
const zeilen = rows.map(r => `[R-${r.Id}] ` + fragen.map(f => `${f}: ${String(r[f] ?? '').replace(/\s+/g, ' ').trim() || '(leer)'}`).join(' | '));
const system = `Du wertest die anonyme Rückmeldung zu einem Weiterbildungstermin aus. Ziel ist eine Tagesordnung für das nächste Mal, keine Lobhudelei.
Pflicht: Jede Antwort wird mindestens einmal mit ihrer Nummer in eckigen Klammern belegt, z.B. [R-12]. Erfinde keine Nummern.
Aufbau als HTML ohne <html>-Rahmen:
<h3>Wer im Raum war</h3> Verteilung nach Bereich und Vorkenntnissen in zwei Sätzen.
<h3>Was sich wiederholt</h3> Die genannten Aufgaben zu Gruppen zusammengefasst, größte Gruppe zuerst, jede mit Nummern belegt.
<h3>Gewünschte Themen und Hürden</h3> Nach Häufigkeit, mit Anzahl.
<h3>Wie es weitergehen soll</h3> Verteilung der Antworten und daraus eine Empfehlung in einem Satz.
<h3>Alle Antworten, je eine Zeile</h3> Eine Liste mit jeder Nummer genau einmal: [R-n] und die Freitextangaben dieser Antwort in höchstens zwölf Wörtern. Keine weglassen, das ist der Beleg. Diese Liste zählt nicht zur Wortgrenze.
Sachlich, höchstens ${cfg.max_worte} Wörter, keine Wertungen über Personen, keine Namen. Wenn eine Angabe fehlt, sag das, statt sie zu ergänzen.
Bei weniger als fünf Antworten beginnst du mit dem Satz: „Bei ${rows.length} Antworten lässt sich daraus nichts ableiten.“ und bleibst danach kurz.`;
let user = `Umfrage: ${umfrage.titel}\nFragen: ${fragen.join(' | ')}\n\nAntworten, eine je Zeile, ${rows.length} Stück:\n${zeilen.join('\n') || '(keine)'}`;
if (vorher) user += `\n\nKorrektur, Versuch ${versuch}: Im letzten Entwurf fehlten diese Nummern: ${vorher.fehlend.join(', ') || 'keine'}. Erfunden waren: ${vorher.erfunden.join(', ') || 'keine'}. Schreibe die Zusammenfassung vollständig neu.`;
return [{ json: { versuch, anzahl: rows.length, system, user } }];
"""),
    node("KI: Zusammenfassen", "@n8n/n8n-nodes-langchain.openAi", 2.3, [1480, 0], {
        "resource": "text", "operation": "response",
        "modelId": {"__rl": True, "mode": "id", "value": "={{ $('Konfiguration').first().json.llm_model }}"},
        "responses": {"values": [{"type": "text", "role": "system", "content": "={{ $json.system }}"},
                                 {"type": "text", "role": "user", "content": "={{ $json.user }}"}]},
        "simplify": True, "options": {"maxTokens": 2500, "temperature": 0.2, "store": False}}, credentials=OPENAI),
    code("Prüfen: Nummern vollständig?", [1720, 0], KI_TEXT + r"""
const cfg = $('Konfiguration').first().json;
const umfrage = $('Umfrage wählen').first().json;
const rows = ($('NocoDB: Antworten lesen').first().json.list || []).filter(r => !r.__nc_deleted);
const erwartet = rows.map(r => `R-${r.Id}`);
const text = kiText($json).replace(/```html|```/g, '').trim();
const gefunden = [...new Set(text.match(/R-\d+/g) || [])];
const fehlend = erwartet.filter(id => !gefunden.includes(id));
const erfunden = gefunden.filter(id => !erwartet.includes(id));
const versuch = $runIndex + 1;
const vollstaendig = fehlend.length === 0 && erfunden.length === 0;
return [{ json: { vollstaendig, fehlend, erfunden, versuch, max_versuche: cfg.max_versuche,
  kennung: umfrage.kennung, titel: umfrage.titel, anzahl: erwartet.length, text } }];
"""),
    node("Vollständig?", "n8n-nodes-base.if", 2.2, [1960, 0], cond_bool("={{ $json.vollstaendig }}", "if-voll")),
    node("Noch ein Versuch?", "n8n-nodes-base.if", 2.2, [2200, 160], {
        "conditions": {"options": {"caseSensitive": True, "leftValue": "", "typeValidation": "strict", "version": 2},
                       "conditions": [{"id": uid("if-versuch"), "leftValue": "={{ $json.versuch }}",
                                       "rightValue": "={{ $json.max_versuche }}", "operator": {"type": "number", "operation": "lt"}}],
                       "combinator": "and"}, "options": {}}),
    node("NocoDB: Zusammenfassung speichern", "n8n-nodes-base.httpRequest", 4.2, [2440, 0], {
        "method": "POST",
        "url": "={{ $('Konfiguration').first().json.nocodb_url }}/api/v2/tables/{{ $('Konfiguration').first().json.ziel_id }}/records",
        "authentication": "predefinedCredentialType", "nodeCredentialType": "nocoDbApiToken",
        "sendBody": True, "specifyBody": "json",
        "jsonBody": "={{ JSON.stringify({ kennung: $json.kennung, titel: $json.titel, text: $json.text, anzahl: $json.anzahl, versuch: $json.versuch, vollstaendig: $json.vollstaendig, fehlende: ($json.fehlend || []).join(', ') }) }}",
        "options": {}}, credentials=NOCODB),
    node("Seite anzeigen", "n8n-nodes-base.respondToWebhook", 1.1, [2680, 0], {
        "respondWith": "text",
        "responseBody": "={{ (() => { const p = $('Prüfen: Nummern vollständig?').first().json; const hinweis = p.vollstaendig ? '' : `<p style=\"background:#fde7e4;padding:10px\">Nach ${p.versuch} Versuchen unvollständig, fehlende Nummern: ${(p.fehlend||[]).join(', ') || 'keine'}, erfunden: ${(p.erfunden||[]).join(', ') || 'keine'}. Bitte selbst prüfen.</p>`; return `<!doctype html><html lang=\"de\"><head><meta charset=\"utf-8\"><title>Zusammenfassung: ${p.titel}</title><style>body{font-family:'Source Sans 3',Helvetica,Arial,sans-serif;max-width:820px;margin:40px auto;padding:0 20px;color:#333;line-height:1.5}h1{color:#C81E0F}h3{color:#EA5A00;margin-top:1.4em}small{color:#767676}</style></head><body><h1>${p.titel}</h1><small>${p.anzahl} Antworten, Versuch ${p.versuch}, jede Antwort mit Nummer belegt: ${p.vollstaendig ? 'ja' : 'nein'}. Gespeichert in NocoDB, sichtbar in Grafana.</small>${hinweis}${p.text}</body></html>`; })() }}",
        "options": {"responseHeaders": {"entries": [{"name": "Content-Type", "value": "text/html; charset=utf-8"}]}}}),
]


def c(*targets):
    return {"main": [[{"node": t, "type": "main", "index": 0} for t in grp] for grp in targets]}


connections = {
    "Knopf: Zusammenfassen": c(["Konfiguration"]),
    "Konfiguration": c(["NocoDB: Umfrage finden"]),
    "NocoDB: Umfrage finden": c(["Umfrage gefunden?"]),
    "Umfrage gefunden?": c(["Umfrage wählen"], ["Seite: Kennung unbekannt"]),
    "Umfrage wählen": c(["NocoDB: Antworten lesen"]),
    "NocoDB: Antworten lesen": c(["Prompt bauen"]),
    "Prompt bauen": c(["KI: Zusammenfassen"]),
    "KI: Zusammenfassen": c(["Prüfen: Nummern vollständig?"]),
    "Prüfen: Nummern vollständig?": c(["Vollständig?"]),
    "Vollständig?": c(["NocoDB: Zusammenfassung speichern"], ["Noch ein Versuch?"]),
    "Noch ein Versuch?": c(["Prompt bauen"], ["NocoDB: Zusammenfassung speichern"]),
    "NocoDB: Zusammenfassung speichern": c(["Seite anzeigen"]),
}

workflow = {
    "id": "gOQMWHJmghfLE5k8",   # ID in der Instanz: Import ersetzt die laufende Fassung, statt sie zu verdoppeln
    "name": "Umfrage zusammenfassen (NocoDB, KI)",
    "nodes": nodes, "connections": connections, "active": True,
    "settings": {"executionOrder": "v1"},
    "meta": {"instanceId": "c3-kickoff"},
}


def demo():
    namen = {n["name"] for n in nodes}
    for quelle, ziele in connections.items():
        assert quelle in namen, quelle
        for grp in ziele["main"]:
            for z in grp:
                assert z["node"] in namen, z["node"]
    assert sum(1 for n in nodes if n["type"].endswith(".code")) == 2, "genau zwei Code-Bausteine: Prompt und Prüfung"
    assert "TABELLE_ZUSAMMENFASSUNGEN" not in json.dumps(nodes) or "--platzhalter" in __import__("sys").argv, \
        "Tabellen-ID der Zusammenfassungen fehlt, mit --ziel <id> aufrufen"


if __name__ == "__main__":
    import sys
    if "--ziel" in sys.argv:
        ziel = sys.argv[sys.argv.index("--ziel") + 1]
        for n in nodes:
            if n["name"] == "Konfiguration":
                for a in n["parameters"]["assignments"]["assignments"]:
                    if a["name"] == "ziel_id":
                        a["value"] = ziel
    demo()
    ZIEL.write_text(json.dumps(workflow, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"ok {ZIEL.name}: {len(nodes)} Knoten, Webhook GET /webhook/{PFAD}?kennung=…")
