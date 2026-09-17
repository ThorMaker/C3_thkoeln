#!/usr/bin/env python3
"""Baut das Eingabeformular des Workflows „Umfrage anlegen (NocoDB, QR-Code)“ neu.

Warum: Das erste Formular erklärte nichts (nur Platzhalter, die beim Tippen verschwinden).
Lehrende müssen ohne Anleitung wissen, wie eine Frage geschrieben wird, was der senkrechte
Strich bedeutet und welche Antwortarten es gibt. Deshalb steht die Erklärung jetzt als
fester Text zwischen den Feldern, im Auftritt der TH Köln (dasselbe CSS wie die
Formulare des Dekanats-Ablaufs).

Das Skript ändert nur den Formular-Knoten, die Feldzuordnung in „Konfiguration“ und die
Ergebnisseite in `n8n-umfrage-anlegen.json`. Alles andere bleibt, wie es aus n8n kam.

Aufruf:  /usr/bin/python3 n8n-umfrage-anlegen-formular.py
Danach:  Datei in n8n über den offenen Workflow importieren („Import from file“).

AI-assisted: Claude (Fable 5.1), human-reviewed: ausstehend, Stand 17.09.2026
"""
import json
import re
from pathlib import Path

HIER = Path(__file__).resolve().parent
DATEI = HIER / "n8n-umfrage-anlegen.json"
CSS_QUELLE = HIER / "n8n_formular_css.txt"   # das TH-CSS liegt hier als eigene Datei

# Das TH-CSS liegt im Dekanats-Generator; nur den String holen, nicht das Modul ausführen.
FORM_CSS = re.search(r'^FORM_CSS = """(.*?)^"""', CSS_QUELLE.read_text(encoding="utf-8"), re.S | re.M).group(1)
FORM_CSS += """
/* Erklärkästen zwischen den Feldern. n8n entfernt aus eigenem HTML class-Attribute und
   auch blockquote; Tabellen, Listen, pre, code und Überschriften bleiben (im Formular
   geprüft). Der Kasten ist deshalb eine einzellige Tabelle, die Typenliste darin eine
   verschachtelte Tabelle. Alles mit !important gegen die n8n-eigenen Regeln. */
table { width: 100% !important; border-collapse: separate !important; border-spacing: 0 !important;
  margin: 4px 0 20px !important; background: #F5F5F5 !important; border-left: 5px solid #C81E0F !important; }
table td { padding: 16px 18px 12px !important; font-size: 14.5px !important; line-height: 1.55 !important;
  color: #333333 !important; vertical-align: top !important; text-align: left !important; }
table table { margin: 10px 0 12px !important; background: #FFFFFF !important; border: 1px solid #DADADA !important; border-left: 1px solid #DADADA !important; }
table table td { padding: 7px 10px !important; border-bottom: 1px solid #E4E4E4 !important; font-size: 13.5px !important; line-height: 1.45 !important; }
table table tr:last-child td { border-bottom: 0 !important; }
table table td:first-child { width: 38% !important; white-space: nowrap !important; }
h3 { margin: 0 0 10px !important; font-size: 17px !important; font-weight: 700 !important; color: #000000 !important; line-height: 1.3 !important; }
td p { margin: 0 0 10px !important; font-size: 14.5px !important; line-height: 1.55 !important; color: #333333 !important; }
td ol { margin: 0 0 10px 20px !important; padding: 0 !important; }
td li { margin: 0 0 5px !important; font-size: 14.5px !important; line-height: 1.5 !important; }
td strong { color: #000000 !important; font-weight: 700 !important; }
td code { font-family: Menlo, Consolas, 'Courier New', monospace !important; font-size: 12.5px !important;
  background: #FFFFFF !important; border: 1px solid #C8C8C8 !important; border-radius: 3px !important;
  padding: 1px 6px !important; color: #C81E0F !important; white-space: nowrap !important; }
td pre { font-family: Menlo, Consolas, 'Courier New', monospace !important; font-size: 12.5px !important;
  background: #FFFFFF !important; border: 1px solid #DADADA !important; border-radius: 3px !important;
  padding: 10px 12px !important; margin: 8px 0 12px !important; white-space: pre-wrap !important;
  word-break: break-word !important; overflow-wrap: anywhere !important; line-height: 1.5 !important;
  color: #333333 !important; max-width: 100% !important; box-sizing: border-box !important; }
label { margin-top: 6px !important; }
"""

# Labels sind zugleich die Schlüssel, unter denen n8n die Eingaben weitergibt.
L_TITEL = "Titel der Umfrage"
L_FRAGEN = "Fragen, eine je Zeile"
L_SCHUTZ = "Wer darf antworten?"
L_NUMMERN = "Matrikelnummern (nur bei geschützter Umfrage)"
OFFEN = "alle, die den QR-Code haben"
GESCHUETZT = "nur Personen auf der Matrikelnummernliste"


def kasten(name, inhalt):
    # einzellige Tabelle als Kasten, weil n8n div-Klassen und blockquote entfernt
    return {"fieldType": "html", "elementName": name, "html": f"<table><tr><td>{inhalt}</td></tr></table>"}


FELDER = [
    kasten("einleitung", """<h3>In drei Schritten zur Umfrage</h3>
<ol>
<li><strong>Titel</strong> eintragen.</li>
<li><strong>Fragen</strong> schreiben, eine je Zeile. Die Schreibweise steht direkt über dem Feld.</li>
<li>Sagen, <strong>wer antworten darf</strong>.</li>
</ol>
<p>Am Ende bekommen Sie den Link für die Studierenden, den QR-Code für die Folie und die Live-Auswertung. Dauert etwa eine Minute. Nichts davon ist endgültig: Schutz und Fragen lassen sich später ändern.</p>"""),
    {"fieldLabel": L_TITEL, "fieldType": "text", "requiredField": True, "placeholder": "zum Beispiel: Rückmeldung Vorlesung 5"},
    kasten("fragen-anleitung", """<h3>So schreiben Sie eine Frage</h3>
<p>Jede Zeile ist eine Frage. Hinter dem senkrechten Strich steht, welche Antwort Sie wollen:</p>
<pre>Fragetext | Antwortart</pre>
<p>Den senkrechten Strich <code>|</code> tippen Sie auf dem Mac mit <code>alt</code> + <code>7</code>, unter Windows mit <code>AltGr</code> + <code>&lt;</code>.</p>
<table>
<tr><td><code>Bewertung</code></td><td>fünf Sterne zum Anklicken</td></tr>
<tr><td><code>Auswahl: a, b, c</code></td><td>Auswahlknöpfe mit genau diesen Möglichkeiten. Nach <code>Auswahl</code> ein Doppelpunkt, zwischen den Möglichkeiten Kommas.</td></tr>
<tr><td><code>Text</code></td><td>großes Feld für freie Antworten</td></tr>
<tr><td><code>Zahl</code></td><td>Zahlenfeld</td></tr>
<tr><td><code>JaNein</code></td><td>ein Häkchen</td></tr>
<tr><td><em>nichts</em></td><td>ohne Strich und Angabe: einzeiliges Textfeld</td></tr>
</table>
<p>Groß- und Kleinschreibung ist egal, Umlaute sind erlaubt. Im Fragetext selbst keinen senkrechten Strich verwenden.</p>
<p><strong>Beispiel zum Kopieren:</strong></p>
<pre>Wie verständlich war die Vorlesung? | Bewertung
Das Tempo war | Auswahl: zu langsam, genau richtig, zu schnell
Was sollen wir vertiefen? | Text
Wie viele Stunden haben Sie vorbereitet? | Zahl
Ich möchte die Folien per Mail | JaNein</pre>"""),
    {"fieldLabel": L_FRAGEN, "fieldType": "textarea", "requiredField": True,
     "placeholder": "Wie verständlich war die Vorlesung? | Bewertung"},
    kasten("schutz-anleitung", """<h3>Wer darf antworten?</h3>
<p><strong>Offen:</strong> Jede Person, die den QR-Code scannt, kann antworten. Reicht in den meisten Fällen.</p>
<p><strong>Geschützt:</strong> Vor dem Formular wird eine Matrikelnummer verlangt und mit Ihrer Liste verglichen. Die Antwort bleibt trotzdem anonym: Die Nummer wird nur abgehakt, sie wird nie zusammen mit der Antwort gespeichert.</p>
<p>Sie können sich hier ruhig falsch entscheiden: Der Schutz lässt sich später in der Tabelle „Umfragen“ mit einem Haken umlegen, der QR-Code bleibt gültig.</p>"""),
    {"fieldLabel": L_SCHUTZ, "fieldType": "dropdown", "requiredField": True,
     "fieldOptions": {"values": [{"option": OFFEN}, {"option": GESCHUETZT}]}},
    kasten("nummern-anleitung", """<h3>Matrikelnummern</h3>
<p>Nur nötig bei „geschützt“. Eine Nummer je Zeile, oder eine ganze CSV-Datei hineinkopieren: Kopfzeilen, Namen und doppelte Einträge werden von allein aussortiert. Nachtragen geht später jederzeit.</p>"""),
    {"fieldLabel": L_NUMMERN, "fieldType": "textarea", "placeholder": "1234567\n2345678"},
]


def main():
    w = json.loads(DATEI.read_text(encoding="utf-8"))
    knoten = {n["name"]: n for n in w["nodes"]}

    # Ohne webhookId registriert n8n das Formular unter „<workflow>/<knoten>/<pfad>“ statt unter „/form/<pfad>“
    knoten["Formular: Neue Umfrage"]["webhookId"] = (str(__import__("uuid").uuid5(__import__("uuid").NAMESPACE_URL, "umfrage-anlegen/formular")))
    f = knoten["Formular: Neue Umfrage"]["parameters"]
    f["formTitle"] = "Neue Umfrage anlegen"
    f["formDescription"] = "Für Lehrende und Mitarbeitende der TH Köln. Anonyme Rückmeldung auf dem eigenen Server, kein Konto für die Studierenden nötig."
    f["formFields"] = {"values": FELDER}
    f["options"].update({"customCss": FORM_CSS, "buttonLabel": "Umfrage anlegen", "appendAttribution": False, "ignoreBots": True})

    for a in knoten["Konfiguration"]["parameters"]["assignments"]["assignments"]:
        if a["name"] == "titel":
            a["value"] = f"={{{{ $json['{L_TITEL}'] }}}}"
        elif a["name"] == "fragen":
            a["value"] = f"={{{{ $json['{L_FRAGEN}'] }}}}"
        elif a["name"] == "geschuetzt":
            a["value"] = f"={{{{ $json['{L_SCHUTZ}'] === '{GESCHUETZT}' }}}}"
        elif a["name"] == "nummern":
            a["value"] = f"={{{{ $json['{L_NUMMERN}'] || '' }}}}"

    e = knoten["Ergebnis zeigen"]["parameters"]
    z = "$('Ergebnis zusammenstellen').first().json"
    e["completionTitle"] = f"={{{{ {z}.titel + ' ist angelegt' }}}}"
    e["completionMessage"] = ("={{ 'Link für die Studierenden (dahin zeigt der QR-Code):\\n' + " + z + ".link + "
        "'\\n\\nLive-Auswertung in Grafana:\\n' + " + z + ".auswertung + "
        "'\\n\\nTabelle mit den Antworten:\\n' + " + z + ".tabelle_url + '\\n\\n' + "
        "(" + z + ".geschuetzt ? 'Geschützt, ' + " + z + ".anzahl_nummern + ' Matrikelnummern eingetragen.' "
        ": 'Offen für alle. Der Schutz lässt sich später in der Tabelle „Umfragen“ per Haken einschalten, der QR-Code bleibt gültig.') + "
        "'\\n\\nQR-Code für die Folie: hängt als Bild an dieser Umfrage in der Tabelle „Umfragen“ (Spalte qr_code), dort herunterladen.' }}")

    # QR-Code als Anhang an die Umfragezeile: hochladen, dann an die Steuerzeile hängen.
    # Beide Knoten dürfen scheitern, ohne die Ergebnisseite zu verhindern (continueOnFail).
    cred = knoten["NocoDB: Steuerzeile anlegen"]["credentials"]
    cfg = "$('Eingaben verstehen').first().json"
    hochladen = {"id": "qr-hochladen-0001", "name": "NocoDB: QR hochladen", "type": "n8n-nodes-base.httpRequest", "typeVersion": 4.2,
                 "position": [1900, 300], "credentials": cred, "onError": "continueRegularOutput",
                 "parameters": {"method": "POST",
                                "url": f"={{{{ {cfg}.nocodb_url }}}}/api/v2/storage/upload?path=noco/{{{{ {cfg}.base_id }}}}/{{{{ {cfg}.steuer_id }}}}/qr_code",
                                "authentication": "predefinedCredentialType", "nodeCredentialType": "nocoDbApiToken",
                                "sendBody": True, "contentType": "multipart-form-data",
                                "bodyParameters": {"parameters": [{"parameterType": "formBinaryData", "name": "file", "inputDataFieldName": "qr"}]},
                                "options": {"timeout": 20000}}}
    eintragen = {"id": "qr-eintragen-0001", "name": "NocoDB: QR an Umfragezeile", "type": "n8n-nodes-base.httpRequest", "typeVersion": 4.2,
                 "position": [2140, 300], "credentials": cred, "onError": "continueRegularOutput",
                 "parameters": {"method": "PATCH",
                                "url": f"={{{{ {cfg}.nocodb_url }}}}/api/v2/tables/{{{{ {cfg}.steuer_id }}}}/records",
                                "authentication": "predefinedCredentialType", "nodeCredentialType": "nocoDbApiToken",
                                "sendBody": True, "specifyBody": "json",
                                "jsonBody": "={{ JSON.stringify([{ Id: $('NocoDB: Steuerzeile anlegen').first().json.Id, qr_code: $('NocoDB: QR hochladen').all().map(i => i.json).filter(j => j && j.path) }]) }}",
                                "options": {"timeout": 20000}}}
    w["nodes"] = [n for n in w["nodes"] if n["name"] not in (hochladen["name"], eintragen["name"])] + [hochladen, eintragen]
    w["connections"]["QR-Code holen"] = {"main": [[{"node": hochladen["name"], "type": "main", "index": 0}]]}
    w["connections"][hochladen["name"]] = {"main": [[{"node": eintragen["name"], "type": "main", "index": 0}]]}
    w["connections"][eintragen["name"]] = {"main": [[{"node": "Ergebnis zeigen", "type": "main", "index": 0}]]}

    DATEI.write_text(json.dumps(w, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"ok {DATEI.name}: Formular mit {len(FELDER)} Feldern ({sum(1 for x in FELDER if x['fieldType'] == 'html')} Erklärkästen), Zuordnung und Ergebnisseite angepasst")


if __name__ == "__main__":
    main()
