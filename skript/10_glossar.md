# Kapitel 10: Glossar Künstliche Intelligenz

Dieses Glossar erklärt die wichtigsten Fachbegriffe rund um generative KI, Sprachmodelle und Agenten, von den Grundlagen bis zu Recht und Hochschulpraxis. Es ist zum Nachschlagen gedacht und kann unabhängig vom Vortrag weitergegeben werden.

**So ist es aufgebaut:** Jeder Eintrag enthält eine kurze Erklärung, Verweise auf verwandte Begriffe (→) und, wo es passt, das Kapitel dieses Skripts. Die Quellen in eckigen Klammern führen zum Nachlesen; sie stehen vollständig im Quellenverzeichnis am Ende.

**Zur Qualität der Quellen:** Bevorzugt zitiert werden begutachtete Veröffentlichungen (Fachzeitschriften und Konferenzen wie NeurIPS, ICLR, ACL), Standardlehrbücher und Rechtstexte. Viele grundlegende Arbeiten der KI-Forschung erscheinen zuerst als Vorabveröffentlichung auf arXiv; solche Einträge sind im Quellenverzeichnis mit „arXiv“ gekennzeichnet und noch nicht oder nicht in dieser Fassung begutachtet. Produktbegriffe wie Skill oder Plugin sind mit der Herstellerdokumentation belegt. Zwei Lehrbücher eignen sich als Einstieg für fast alle Grundbegriffe: Russell und Norvig für KI allgemein [1], Jurafsky und Martin für Sprachverarbeitung [2].

### A

**Agent (KI-Agent).** Ein System, das seine Umgebung wahrnimmt und selbstständig handelt, um ein Ziel zu erreichen. Bei Sprachmodellen heißt das: Das Modell arbeitet in einer Schleife aus Lesen, Planen, Handeln und Beobachten und entscheidet selbst über den nächsten Schritt. Der Begriff stammt aus der klassischen KI-Forschung [3]; einen Überblick über Agenten auf Basis von Sprachmodellen gibt Wang et al. [4]. → Workflow, ReAct, Harness. Kapitel 1.4 und 1.8.

**Agent Team.** Mehrere Instanzen von Claude Code, die sich über getrennte Sitzungen abstimmen; experimentell und nur in der Kommandozeile [5]. → Unteragent. Kapitel 6.3.

**AI Act (KI-Verordnung).** Verordnung (EU) 2024/1689, der europäische Rechtsrahmen für KI. Sie ordnet KI-Systeme nach Risiko ein, verbietet bestimmte Praktiken, stellt Anforderungen an Hochrisiko-Systeme und an Modelle mit allgemeinem Verwendungszweck und verpflichtet Anbieter und Betreiber zur Förderung von KI-Kompetenz [6]. → Hochrisiko-KI-System, KI-Kompetenz, GPAI-Modell. Kapitel 1.13.

**Alignment (Ausrichtung).** Die Frage, wie sich erreichen lässt, dass KI-Systeme im Sinne menschlicher Absichten und Werte handeln. Gabriel ordnet die philosophischen Dimensionen [7]; Amodei et al. benennen konkrete technische Problemfelder wie unerwünschte Nebenwirkungen und Reward Hacking [8]. → RLHF, Constitutional AI.

**Attention (Aufmerksamkeitsmechanismus).** Rechenverfahren, mit dem ein neuronales Netz für jedes Element einer Eingabe gewichtet, welche anderen Elemente dafür wichtig sind. Zuerst für die maschinelle Übersetzung eingeführt [9], ist Attention der Kern der Transformer-Architektur [10]. → Transformer, Kontextfenster.

**Automatisierungsbias (Automation Bias).** Die Neigung von Menschen, automatisierten Empfehlungen zu stark zu vertrauen und eigene Prüfungen zu vernachlässigen [11]. Relevant, sobald KI-Ausgaben ungeprüft übernommen werden. → Human in the Loop.

### B

**Benchmark.** Standardisierte Aufgabensammlung, mit der Modelle verglichen werden, etwa MMLU mit Fragen aus 57 Fachgebieten [12]. Einzelne Benchmarks messen nur Ausschnitte; HELM plädiert deshalb für eine ganzheitliche Bewertung über viele Szenarien und Kriterien [13]. → Evaluation, Goodharts Gesetz.

**Bias (Verzerrung).** Systematische Schieflagen in Daten, Modellen oder ihrer Anwendung, die zu unfairen oder fehlerhaften Ergebnissen führen können. Mehrabi et al. geben einen Überblick über Arten und Gegenmaßnahmen [14]; Bender et al. diskutieren, wie große Textkorpora gesellschaftliche Vorurteile übernehmen [15]. → Model Card.

### C

**Chain-of-Thought (Gedankenkette).** Aufforderung an ein Sprachmodell, Zwischenschritte auszuformulieren, bevor es antwortet. Das verbessert bei großen Modellen die Leistung in mehrstufigen Aufgaben [16]. → Reasoning-Modell, Prompt Engineering.

**CLAUDE.md.** Datei mit dauerhaften Anweisungen, die Claude Code zu Beginn jeder Sitzung liest, global, pro Projekt oder pro Unterordner [17]. → Context Engineering. Kapitel 2.4.

**Compaction (Zusammenfassen des Verlaufs).** Automatisches oder mit `/compact` ausgelöstes Verdichten einer langen Sitzung, damit das Kontextfenster wieder Platz hat [18]. → Kontextfenster, Handover. Kapitel 1.3.

**Constitutional AI.** Trainingsverfahren von Anthropic, bei dem ein Modell anhand schriftlich formulierter Grundsätze (einer „Verfassung“) eigene Antworten bewertet und verbessert, um die Abhängigkeit von menschlichen Bewertungen zu verringern [19]. → RLHF, Alignment.

**Context Engineering.** Gestaltung dessen, was ein Modell zu einem Zeitpunkt sieht: Anweisungen, Dateien, Werkzeuge, Verlauf. Grundlage ist die Beobachtung, dass Modelle Informationen je nach Position im Kontext unterschiedlich gut nutzen [20]. → Kontextfenster, RAG. Kapitel 1.5 und 1.8.

### D

**Data Table.** Einfache Tabelle direkt in der Automatisierungsplattform n8n, die Workflows lesen und beschreiben [21]. Kapitel 4.

**Datenschutz-Grundverordnung (DSGVO).** Verordnung (EU) 2016/679; regelt die Verarbeitung personenbezogener Daten, einschließlich der Rollen Verantwortlicher und Auftragsverarbeiter. Artikel 22 schränkt ausschließlich automatisierte Einzelentscheidungen ein [22]. Kapitel 1.13.

**Datasheet für Datensätze.** Standardisierte Dokumentation eines Datensatzes: Entstehung, Zusammensetzung, empfohlene Verwendung, Grenzen [23]. → Model Card.

**Deep Learning.** Teilgebiet des maschinellen Lernens mit vielschichtigen neuronalen Netzen, die Merkmale aus Rohdaten selbst lernen [24], [25]. → Neuronales Netz, Maschinelles Lernen.

**Destillation (Knowledge Distillation).** Verfahren, bei dem ein kleines Modell lernt, die Ausgaben eines großen Modells nachzuahmen, um mit weniger Rechenaufwand ähnlich gut zu sein [26]. → Quantisierung.

**Deterministisch und probabilistisch.** Ein deterministisches Verfahren liefert bei gleicher Eingabe immer das gleiche Ergebnis (Regeln, Code). Sprachmodelle sind probabilistisch: Sie ziehen die nächste Ausgabe aus einer Wahrscheinlichkeitsverteilung [27]. Für Prüfungen in Abläufen sind deterministische Verfahren vorzuziehen. → Sampling, Prüfschleife. Kapitel 4.1.

**Diffusionsmodell.** Generatives Modell, das lernt, schrittweise Rauschen aus Daten zu entfernen; Grundlage vieler Bildgeneratoren [28]. → Multimodales Modell.

### E

**Embedding (Einbettung).** Darstellung von Wörtern, Sätzen oder Dokumenten als Zahlenvektoren, bei denen inhaltlich Ähnliches nahe beieinander liegt [2], [29]. Grundlage der Ähnlichkeitssuche. → Vektordatenbank, RAG.

**Emergenz.** Die Beobachtung, dass bestimmte Fähigkeiten erst ab einer gewissen Modellgröße sprunghaft auftreten [30]. Umstritten: Schaeffer et al. zeigen, dass solche Sprünge teils ein Effekt der gewählten Messgröße sind [31]. → Scaling Laws.

**Erklärbarkeit (Explainable AI, XAI).** Forschungsfeld, das Entscheidungen von KI-Systemen für Menschen nachvollziehbar machen will. Doshi-Velez und Kim schlagen vor, Interpretierbarkeit systematisch und aufgabenbezogen zu evaluieren [32]. → Mechanistische Interpretierbarkeit.

**Evaluation.** Systematische Bewertung von Modellen oder Anwendungen anhand definierter Kriterien und Daten. → Benchmark, LLM als Richter, Prüfschleife.

### F

**Feinabstimmung (Fine-Tuning).** Weitertrainieren eines vortrainierten Modells mit eigenen Daten für eine bestimmte Aufgabe. Parameter-effiziente Verfahren wie LoRA passen nur kleine Zusatzmatrizen an und senken den Aufwand stark [33]. → Vortraining, RLHF.

**Few-Shot- und Zero-Shot-Lernen (In-Context-Lernen).** Große Sprachmodelle können neue Aufgaben lösen, wenn im Prompt einige Beispiele (few-shot) oder nur eine Beschreibung (zero-shot) stehen, ohne dass das Modell neu trainiert wird [34]. → Prompt Engineering.

**Foundation Model (Basismodell).** Großes, auf breiten Daten vortrainiertes Modell, das an viele Aufgaben angepasst werden kann. Der Begriff und seine Chancen und Risiken gehen auf eine Studie der Stanford University zurück [35]. → GPAI-Modell, Sprachmodell.

### G

**Goodharts Gesetz.** Wird eine Kennzahl zum Ziel, taugt sie nicht mehr als Kennzahl; die geläufige Formulierung stammt von Strathern nach Goodhart [36], [37]. Für KI heißt das: Jede Prüfung ist eine Kennzahl, auf die ein System optimiert. → Reward Hacking, Specification Gaming. Kapitel 7.4.

**GPAI-Modell (KI-Modell mit allgemeinem Verwendungszweck).** Begriff des AI Act für Modelle, die für viele verschiedene Aufgaben einsetzbar sind, etwa große Sprachmodelle; ihre Anbieter haben eigene Pflichten, etwa zu Dokumentation und Urheberrecht [6]. → Foundation Model.

**GraphRAG.** Retrieval-Verfahren, das aus Dokumenten einen Wissensgraphen mit zusammengefassten Themengruppen baut und damit auch Fragen über ganze Sammlungen beantwortet [38]. → Wissensgraph, RAG. Kapitel 5.2 und 6.6.

### H

**Halluzination.** Plausibel klingende, aber falsche oder nicht belegte Ausgabe eines Modells. Ji et al. geben einen Überblick über Ursachen, Arten und Messverfahren [39]. → RAG, Kalibrierung. Kapitel 1.1.

**Handover (Übergabe).** Datei mit Ziel, Stand, Entscheidungen und nächsten Schritten, die vor einem Neustart des Kontexts geschrieben wird, damit eine neue Sitzung nahtlos weiterarbeitet. Kapitel 1.3.

**Harness.** Die Umgebung, die einem Sprachmodell Werkzeuge, Rechte, Gedächtnis und Grenzen gibt; Claude Code ist ein solcher Harness [40]. → Agent, Loop Engineering. Kapitel 1.4 und 1.8.

**Hochrisiko-KI-System.** Kategorie des AI Act für KI-Systeme mit erheblichen Risiken für Gesundheit, Sicherheit oder Grundrechte, darunter Systeme zur Bewertung von Lernergebnissen oder zur Zulassung zu Bildung (Anhang III) [6]. Für sie gelten strenge Pflichten; der Digital Omnibus hat die Fristen verschoben [41]. Kapitel 1.13.

**Hook.** Skript, das Claude Code an einem festen Punkt automatisch ausführt, etwa vor jedem Werkzeugaufruf. Ein Hook kann eine Aktion mit Exit-Code 2 blockieren und so Regeln deterministisch durchsetzen [42]. → Leitplanke. Kapitel 2.9.

**Human in the Loop.** Gestaltungsprinzip, bei dem Menschen an entscheidenden Stellen prüfen, freigeben oder korrigieren. Amershi et al. formulieren 18 Richtlinien für die Zusammenarbeit von Menschen und KI [43]. → Automatisierungsbias.

### I

**Inferenz.** Die Nutzung eines fertig trainierten Modells, also das Erzeugen von Ausgaben für neue Eingaben, im Unterschied zum Training [25]. → Parameter, Quantisierung.

### J

**Jailbreak.** Eingabe, die Sicherheitsvorkehrungen eines Modells umgeht, sodass es Ausgaben erzeugt, die es verweigern soll. Wei, Haghtalab und Steinhardt analysieren, warum Sicherheitstraining dabei versagt [44]. → Prompt Injection, Red Teaming.

### K

**Kalibrierung.** Übereinstimmung zwischen der Zuversicht eines Modells und seiner tatsächlichen Trefferquote. Moderne neuronale Netze sind oft überzuversichtlich [45]. → Halluzination.

**KI (Künstliche Intelligenz).** Teilgebiet der Informatik, das Systeme entwickelt, die Aufgaben lösen, für die üblicherweise menschliche Intelligenz nötig ist: wahrnehmen, schließen, lernen, handeln. Das Standardlehrbuch strukturiert das Feld über das Konzept rationaler Agenten [1]. → Maschinelles Lernen, Agent.

**KI-Kompetenz (AI Literacy).** Fähigkeiten, Kenntnisse und Verständnis, um KI sachkundig einzusetzen und Chancen wie Risiken zu erkennen. Der AI Act verpflichtet Anbieter und Betreiber, Maßnahmen dafür zu ergreifen [6], [41]. Leitlinien für Bildung und Forschung hat die UNESCO veröffentlicht [46]. Kapitel 1.13.

**Kontextfenster.** Die Textmenge, die ein Sprachmodell in einer Anfrage gleichzeitig verarbeiten kann: Anweisung, Dateien, Verlauf, Werkzeugausgaben. Mehr ist nicht automatisch besser, weil Informationen in der Mitte langer Kontexte schlechter genutzt werden [20]. → Token, Context Engineering. Kapitel 1.1.

### L

**Leitplanke (Guardrail).** Technische Grenze, die unabhängig vom Wohlverhalten eines Modells greift, etwa Berechtigungsregeln, Hooks oder eine Sandbox. Deny-Regeln in Claude Code blockieren Werkzeuge selbst im Modus ohne Rückfragen [47]. → Hook, Prompt Injection. Kapitel 2.9.

**LLM als Richter (LLM-as-a-Judge).** Ein Sprachmodell bewertet die Ausgaben eines anderen. Zheng et al. zeigen hohe Übereinstimmung mit menschlichen Urteilen, aber auch Verzerrungen, etwa zugunsten der eigenen Antworten oder längerer Texte [48]. → Evaluation, Reward Hacking. Kapitel 7.4.

**Loop Engineering.** Entwurf von Schleifen aus Auslöser, Ziel, Ausführung, Prüfung, Abbruchregel und Gedächtnis, die einen Agenten mit wenig menschlichem Eingreifen zu einem prüfbaren Ziel führen [40], [49]. → Prüfschleife, Harness. Kapitel 1.8 und 7.

### M

**Maschinelles Lernen.** Verfahren, bei denen Computer aus Daten lernen, statt explizit programmiert zu werden; unterschieden werden überwachtes, unüberwachtes und bestärkendes Lernen [1], [25]. → Deep Learning.

**MCP (Model Context Protocol).** Offener Standard, über den KI-Assistenten externe Werkzeuge und Datenquellen anbinden, etwa Ticketsysteme, Datenbanken oder n8n-Workflows [50], [51]. → Tool Use. Kapitel 2.8 und 4.3.

**Mechanistische Interpretierbarkeit.** Forschungsrichtung, die die inneren Rechenwege neuronaler Netze Schritt für Schritt nachvollziehen will, etwa als „Schaltkreise“ aus Neuronen und Gewichten [52]. → Erklärbarkeit.

**Mixture of Experts.** Architektur, bei der für jede Eingabe nur ein Teil spezialisierter Teilnetze („Experten“) aktiv wird; so wachsen Modelle ohne proportional steigende Rechenkosten [53]. → Parameter.

**Model Card.** Standardisierte Kurzdokumentation eines Modells: Zweck, Trainingsdaten, Leistung für verschiedene Gruppen, Grenzen, ethische Aspekte [54]. → Datasheet, Bias.

**Multimodales Modell.** Modell, das mehrere Arten von Daten verarbeitet, etwa Text, Bild und Ton. Ein wichtiger Schritt war das gemeinsame Lernen von Bild- und Textrepräsentationen [55]. → Spracherkennung, Diffusionsmodell.

### N

**Neuronales Netz.** Rechenmodell aus vielen einfachen, verbundenen Einheiten, deren Gewichte beim Training angepasst werden; Grundlage moderner KI [25]. → Deep Learning, Parameter.

### O

**Open Weight und Open Source KI.** Bei Open-Weight-Modellen sind die trainierten Gewichte frei verfügbar, nicht unbedingt aber Trainingsdaten und Code. Die Open Source Initiative hat definiert, was ein KI-System als quelloffen gelten lässt [56]. Open-Weight-Modelle lassen sich auf eigener Infrastruktur betreiben, wie bei Inferenz NRW [57]. → Inferenz, Quantisierung.

### P

**Parameter.** Die lernbaren Gewichte eines neuronalen Netzes; ihre Anzahl ist ein grobes Maß für die Modellgröße [25]. → Scaling Laws.

**Plan-Modus.** Arbeitsmodus von Claude Code, in dem erkundet und ein Plan vorgeschlagen, aber nichts geändert wird [58]. Kapitel 2.2.

**Plugin und Marketplace.** Ein Plugin bündelt Skills, Befehle, Unteragenten, Hooks und MCP-Server zu einem installierbaren Paket; ein Marketplace ist ein Katalog solcher Plugins [59]. Kapitel 2.7.

**Prompt, System-Prompt.** Der Prompt ist die Eingabe an ein Sprachmodell. Der System-Prompt legt Rolle, Regeln und Rahmen fest und gilt für das ganze Gespräch [60]. → Prompt Engineering.

**Prompt Engineering.** Gestaltung von Eingaben, damit ein Modell zuverlässig die gewünschte Ausgabe liefert: Rolle, Kontext, Aufgabe, Beispiele, prüfbare Kriterien [34], [60]. → Chain-of-Thought, Context Engineering. Kapitel 1.7 und 1.8.

**Prompt Injection.** Angriff, bei dem versteckte Anweisungen in Inhalte eingeschleust werden, die ein Modell verarbeitet, etwa in Webseiten, Mails oder Dokumente. Greshake et al. zeigen, dass solche indirekten Angriffe reale Anwendungen kompromittieren können [61]. → Jailbreak, Leitplanke. Kapitel 2.8.

**Prüfschleife.** Rückführung eines Prüfergebnisses in den nächsten Durchlauf, bis ein Ziel erfüllt ist oder eine Grenze erreicht wird; ein Regelkreis im Kleinen. Anthropic beschreibt das Muster als Evaluator-Optimizer [62]. → Loop Engineering. Kapitel 4.4 und 7.

### Q

**Quantisierung.** Speichern der Modellgewichte mit weniger Bits, etwa 8 statt 16, um Speicher und Rechenzeit zu sparen; wichtig für den Betrieb auf eigener Hardware [63]. → Inferenz, Open Weight.

### R

**RAG (Retrieval-Augmented Generation).** Ein Modell bekommt zur Frage passende Textstellen aus einer Wissensbasis und stützt seine Antwort darauf [64]. Mindert Halluzinationen und erlaubt aktuelle, eigene Inhalte. → Embedding, Vektordatenbank, GraphRAG. Kapitel 5.2.

**ReAct.** Verfahren, bei dem ein Sprachmodell Denken und Handeln abwechselt: überlegen, Werkzeug nutzen, Ergebnis beobachten [65]. Grundmuster heutiger Agenten. → Agent, Tool Use.

**Reasoning-Modell und Test-Time Compute.** Modelle, die vor der Antwort länger „nachdenken“, also mehr Rechenaufwand zur Laufzeit einsetzen. Snell et al. zeigen, dass zusätzlicher Rechenaufwand bei der Antwort unter Umständen wirksamer ist als ein größeres Modell [66]. → Chain-of-Thought.

**Red Teaming.** Gezieltes Suchen nach Schwachstellen und schädlichen Verhaltensweisen eines Modells, auch automatisiert mit anderen Modellen [67]. → Jailbreak, Alignment.

**Reward Hacking.** Ein System optimiert auf die Bewertung statt auf das eigentliche Ziel. Bei iterativer Selbstverbesserung steigt dann die Selbstbewertung, während die tatsächliche Qualität stagniert [8], [68]. → Specification Gaming, Goodharts Gesetz. Kapitel 7.4.

**Risikomanagement für KI.** Systematisches Erkennen, Bewerten und Steuern von KI-Risiken über den Lebenszyklus; ein verbreiteter Rahmen ist das AI Risk Management Framework des NIST [69]. → AI Act.

**RLHF (Reinforcement Learning from Human Feedback).** Training mit menschlichen Präferenzurteilen: Menschen vergleichen Antworten, ein Belohnungsmodell lernt daraus, das Sprachmodell wird darauf optimiert [70], [71]. → Alignment, Constitutional AI.

### S

**Sampling und Temperatur.** Sprachmodelle wählen das nächste Token aus einer Wahrscheinlichkeitsverteilung. Die Temperatur steuert, wie stark wahrscheinliche Tokens bevorzugt werden; niedrige Werte machen Ausgaben vorhersagbarer, hohe vielfältiger. Holtzman et al. untersuchen Auswahlverfahren wie Nucleus Sampling [27]. → Deterministisch und probabilistisch.

**Sandbox (Sandkasten).** Abgeschotteter Bereich, in dem ein Programm arbeitet, ohne auf den Rest des Systems zugreifen zu können. In Claude Code begrenzt das Betriebssystem, welche Dateien und welche Netzverbindungen ein Vorgang erreicht. Der Unterschied zu Berechtigungsregeln ist wesentlich: Hier entscheidet nicht das Modell, sondern das System [47]. → Berechtigungsmodus, Hook. Kapitel 2.7.

**Scaling Laws (Skalierungsgesetze).** Empirische Zusammenhänge zwischen Modellgröße, Datenmenge, Rechenaufwand und Leistung [72]. Hoffmann et al. zeigen, dass viele Modelle im Verhältnis zu ihrer Größe mit zu wenig Daten trainiert waren [73]. → Parameter, Emergenz.

**Selbstkorrektur (Self-Refine).** Ein Modell überarbeitet eigene Ausgaben anhand eigener Rückmeldung [74]. Ohne äußere Rückmeldung verbessern Modelle ihr Schlussfolgern jedoch nicht zuverlässig [75]. → Prüfschleife, Reward Hacking.

**Skill.** Ordner mit einer Datei `SKILL.md`, der Claude eine wiederholbare Fähigkeit beibringt und nur bei Bedarf geladen wird [76]. Kapitel 2.5.

**Specification Gaming.** Ein System erfüllt den Wortlaut einer Aufgabe oder Prüfung und verfehlt ihren Sinn, etwa indem es einen Test verändert statt den Fehler zu beheben [77]. → Reward Hacking. Kapitel 7.4.

**Spracherkennung (Speech-to-Text).** Umwandlung gesprochener Sprache in Text. Whisper wurde mit großen, schwach annotierten Audiodaten trainiert und ist mehrsprachig robust; es lässt sich auch lokal betreiben [78]. Kapitel 4.4.

**Sprachmodell (Large Language Model, LLM).** Modell, das die Wahrscheinlichkeit der nächsten Tokens vorhersagt und dadurch Text erzeugt. Große Sprachmodelle werden mit sehr großen Textmengen vortrainiert [34], [79]. Kritische Perspektiven auf Risiken, Kosten und Verzerrungen formulieren Bender et al. [15] und Weidinger et al. [80]. → Transformer, Token.

### T

**Text und Data Mining.** Automatisierte Analyse von Texten und Daten, um Muster und Zusammenhänge zu gewinnen. In Deutschland erlaubt § 44b UrhG Vervielfältigungen dafür, sofern Rechteinhaber nicht maschinenlesbar widersprochen haben [81]. Relevant für Training und Wissensgraphen. → GPAI-Modell.

**Token und Tokenisierung.** Sprachmodelle verarbeiten Text in Tokens, meist Wortteile. Verfahren wie Byte-Pair-Encoding zerlegen Wörter in häufige Teilstücke [82]. Tokens sind auch die Abrechnungseinheit von KI-Diensten. → Kontextfenster. Kapitel 1.1.

**Tool Use (Werkzeugnutzung, Function Calling).** Fähigkeit eines Modells, externe Werkzeuge aufzurufen, etwa Suche, Rechner oder Programmierschnittstellen. Toolformer zeigt, dass Modelle das selbst lernen können [83]. → Agent, MCP.

**Transformer.** Architektur neuronaler Netze, die ausschließlich auf Attention beruht und Eingaben parallel verarbeitet; Grundlage fast aller heutigen Sprachmodelle [10]. → Attention, Sprachmodell.

### U

**Unteragent (Subagent).** Spezialisierter Assistent mit eigenem Kontextfenster, eigenen Werkzeugrechten und eigenem Modell innerhalb einer Claude-Code-Sitzung; er liefert nur das Ergebnis zurück [84]. → Agent Team. Kapitel 2.6.

### V

**Vektordatenbank und Ähnlichkeitssuche.** Speicher für Embeddings, der zu einer Anfrage die ähnlichsten Vektoren findet; effiziente Verfahren dafür beschreiben Johnson, Douze und Jégou [85]. Baustein von RAG. → Embedding, RAG.

**Vortraining (Pretraining).** Erste, sehr aufwendige Trainingsphase eines Sprachmodells auf großen Textmengen, in der es die Vorhersage des nächsten Tokens lernt; danach folgen Feinabstimmung und Ausrichtung [71], [79]. → Feinabstimmung, RLHF.

### W

**Wissensgraph.** Darstellung von Wissen als Knoten (Begriffe, Dokumente, Personen) und Kanten (Beziehungen). Hogan et al. geben einen umfassenden Überblick über Modelle, Methoden und Anwendungen [86]. → GraphRAG. Kapitel 5.

**Workflow.** Fest vorgegebene Schrittfolge, in der ein Modell einzelne Schritte übernimmt, im Unterschied zu einem Agenten, der die Schritte selbst wählt; für viele Verwaltungsaufgaben die robustere Bauform [62]. → Agent. Kapitel 1.6 und 4.

**Worktree.** Isolierte Arbeitskopie eines Git-Repositorys, mit der mehrere Sitzungen gleichzeitig am selben Projekt arbeiten, ohne sich zu stören [58]. Kapitel 6.3.

### Weiterführend

- **Zum Einstieg:** Russell und Norvig [1], Jurafsky und Martin [2], der Überblick zu großen Sprachmodellen von Zhao et al. [79].
- **KI in Bildung und Hochschule:** Leitlinien der UNESCO [46] und die Übersicht zu Chancen und Herausforderungen von Kasneci et al. [87].
- **Risiken und Verantwortung:** Weidinger et al. [80], NIST AI RMF [69], der AI Act [6].

## Quellen

[1] S. Russell und P. Norvig, *Artificial Intelligence: A Modern Approach*, 4. Aufl. Hoboken, NJ: Pearson, 2021.

[2] D. Jurafsky und J. H. Martin, *Speech and Language Processing*, 3 (Entwurf). Stanford University, 2025. Zugegriffen: 11. September 2026. [Online]. Verfügbar unter: <https://web.stanford.edu/~jurafsky/slp3/>

[3] M. Wooldridge und N. R. Jennings, „Intelligent agents: theory and practice“, *The Knowledge Engineering Review*, Bd. 10, Nr. 2, S. 115-152, 1995, doi: [10.1017/S0269888900008122](https://doi.org/10.1017/S0269888900008122).

[4] L. Wang *u. a.*, „A survey on large language model based autonomous agents“, *Frontiers of Computer Science*, Bd. 18, 2024, doi: [10.1007/s11704-024-40231-1](https://doi.org/10.1007/s11704-024-40231-1).

[5] Anthropic, „Agent teams“, Claude Code Docs. Zugegriffen: 11. September 2026. [Online]. Verfügbar unter: <https://code.claude.com/docs/en/agent-teams>

[6] *Verordnung (EU) 2024/1689 (Verordnung über künstliche Intelligenz)*. 2024. Verfügbar unter: <https://eur-lex.europa.eu/eli/reg/2024/1689/oj>

[7] I. Gabriel, „Artificial Intelligence, Values, and Alignment“, *Minds and Machines*, Bd. 30, S. 411-437, 2020, doi: [10.1007/s11023-020-09539-2](https://doi.org/10.1007/s11023-020-09539-2).

[8] D. Amodei, C. Olah, J. Steinhardt, P. Christiano, J. Schulman, und D. Mané, „Concrete Problems in AI Safety“, 2016, 1606.06565. Verfügbar unter: <https://arxiv.org/abs/1606.06565>

[9] D. Bahdanau, K. Cho, und Y. Bengio, „Neural Machine Translation by Jointly Learning to Align and Translate“, in *International Conference on Learning Representations (ICLR)*, 2015. Verfügbar unter: <https://arxiv.org/abs/1409.0473>

[10] A. Vaswani *u. a.*, „Attention Is All You Need“, in *Advances in Neural Information Processing Systems 30 (NeurIPS 2017)*, 2017. Verfügbar unter: <https://arxiv.org/abs/1706.03762>

[11] R. Parasuraman und D. H. Manzey, „Complacency and Bias in Human Use of Automation: An Attentional Integration“, *Human Factors*, Bd. 52, Nr. 3, S. 381-410, 2010, doi: [10.1177/0018720810376055](https://doi.org/10.1177/0018720810376055).

[12] D. Hendrycks *u. a.*, „Measuring Massive Multitask Language Understanding“, in *International Conference on Learning Representations (ICLR)*, 2021. Verfügbar unter: <https://arxiv.org/abs/2009.03300>

[13] P. Liang *u. a.*, „Holistic Evaluation of Language Models“, *Transactions on Machine Learning Research*, 2023, Verfügbar unter: <https://arxiv.org/abs/2211.09110>

[14] N. Mehrabi, F. Morstatter, N. Saxena, K. Lerman, und A. Galstyan, „A Survey on Bias and Fairness in Machine Learning“, *ACM Computing Surveys*, Bd. 54, Nr. 6, 2021, doi: [10.1145/3457607](https://doi.org/10.1145/3457607).

[15] E. M. Bender, T. Gebru, A. McMillan-Major, und S. Shmitchell, „On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?“, in *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency (FAccT)*, 2021, S. 610-623. doi: [10.1145/3442188.3445922](https://doi.org/10.1145/3442188.3445922).

[16] J. Wei *u. a.*, „Chain-of-Thought Prompting Elicits Reasoning in Large Language Models“, in *Advances in Neural Information Processing Systems 35 (NeurIPS 2022)*, 2022. Verfügbar unter: <https://arxiv.org/abs/2201.11903>

[17] Anthropic, „How Claude remembers your project“, Claude Code Docs. Zugegriffen: 11. September 2026. [Online]. Verfügbar unter: <https://code.claude.com/docs/en/memory>

[18] Anthropic, „Manage costs effectively“, Claude Code Docs. Zugegriffen: 11. September 2026. [Online]. Verfügbar unter: <https://code.claude.com/docs/en/costs>

[19] Y. Bai *u. a.*, „Constitutional AI: Harmlessness from AI Feedback“, 2022, 2212.08073. Verfügbar unter: <https://arxiv.org/abs/2212.08073>

[20] N. F. Liu *u. a.*, „Lost in the Middle: How Language Models Use Long Contexts“, *Transactions of the Association for Computational Linguistics*, Bd. 12, S. 157-173, 2024, doi: [10.1162/tacl_a_00638](https://doi.org/10.1162/tacl_a_00638).

[21] n8n, „Data Table node: Row operations“, n8n Docs. Zugegriffen: 11. September 2026. [Online]. Verfügbar unter: <https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.datatable/rows>

[22] *Verordnung (EU) 2016/679 (Datenschutz-Grundverordnung)*, Bd. L 119. 2016, S. 1-88. Verfügbar unter: <https://eur-lex.europa.eu/eli/reg/2016/679/oj>

[23] T. Gebru *u. a.*, „Datasheets for Datasets“, *Communications of the ACM*, Bd. 64, Nr. 12, S. 86-92, 2021, doi: [10.1145/3458723](https://doi.org/10.1145/3458723).

[24] Y. LeCun, Y. Bengio, und G. Hinton, „Deep learning“, *Nature*, Bd. 521, S. 436-444, 2015, doi: [10.1038/nature14539](https://doi.org/10.1038/nature14539).

[25] I. Goodfellow, Y. Bengio, und A. Courville, *Deep Learning*. Cambridge, MA: MIT Press, 2016. Verfügbar unter: <https://www.deeplearningbook.org>

[26] G. Hinton, O. Vinyals, und J. Dean, „Distilling the Knowledge in a Neural Network“, 2015, 1503.02531. Verfügbar unter: <https://arxiv.org/abs/1503.02531>

[27] A. Holtzman, J. Buys, L. Du, M. Forbes, und Y. Choi, „The Curious Case of Neural Text Degeneration“, in *International Conference on Learning Representations (ICLR)*, 2020. Verfügbar unter: <https://arxiv.org/abs/1904.09751>

[28] J. Ho, A. Jain, und P. Abbeel, „Denoising Diffusion Probabilistic Models“, in *Advances in Neural Information Processing Systems 33 (NeurIPS 2020)*, 2020. Verfügbar unter: <https://arxiv.org/abs/2006.11239>

[29] T. Mikolov, K. Chen, G. Corrado, und J. Dean, „Efficient Estimation of Word Representations in Vector Space“, 2013, 1301.3781. Verfügbar unter: <https://arxiv.org/abs/1301.3781>

[30] J. Wei *u. a.*, „Emergent Abilities of Large Language Models“, *Transactions on Machine Learning Research*, 2022, Verfügbar unter: <https://arxiv.org/abs/2206.07682>

[31] R. Schaeffer, B. Miranda, und S. Koyejo, „Are Emergent Abilities of Large Language Models a Mirage?“, in *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*, 2023. Verfügbar unter: <https://arxiv.org/abs/2304.15004>

[32] F. Doshi-Velez und B. Kim, „Towards A Rigorous Science of Interpretable Machine Learning“, 2017, 1702.08608. Verfügbar unter: <https://arxiv.org/abs/1702.08608>

[33] E. J. Hu *u. a.*, „LoRA: Low-Rank Adaptation of Large Language Models“, in *International Conference on Learning Representations (ICLR)*, 2022. Verfügbar unter: <https://arxiv.org/abs/2106.09685>

[34] T. B. Brown *u. a.*, „Language Models are Few-Shot Learners“, in *Advances in Neural Information Processing Systems 33 (NeurIPS 2020)*, 2020. Verfügbar unter: <https://arxiv.org/abs/2005.14165>

[35] R. Bommasani *u. a.*, „On the Opportunities and Risks of Foundation Models“, 2021, 2108.07258. Verfügbar unter: <https://arxiv.org/abs/2108.07258>

[36] M. Strathern, „Improving ratings: audit in the British University system“, *European Review*, Bd. 5, Nr. 3, S. 305-321, 1997.

[37] C. A. E. Goodhart, „Problems of Monetary Management: The U.K. Experience“, in *Papers in Monetary Economics, Vol. I*, Sydney: Reserve Bank of Australia, 1975.

[38] D. Edge *u. a.*, „From Local to Global: A Graph RAG Approach to Query-Focused Summarization“, 2024, 2404.16130. Verfügbar unter: <https://arxiv.org/abs/2404.16130>

[39] Z. Ji *u. a.*, „Survey of Hallucination in Natural Language Generation“, *ACM Computing Surveys*, Bd. 55, Nr. 12, S. 1-38, 2023, doi: [10.1145/3571730](https://doi.org/10.1145/3571730).

[40] S. Macedo, „Stop Hand-Holding Your Coding Agent: Engineering the Loops that Replace Step-by-Step Prompting“, 2026, 2607.00038. Verfügbar unter: <https://arxiv.org/abs/2607.00038>

[41] *Verordnung (EU) 2026/1744 (Digital Omnibus zur KI-Verordnung)*. 2026. Verfügbar unter: <https://eur-lex.europa.eu/eli/reg/2026/1744/oj>

[42] Anthropic, „Hooks reference“, Claude Code Docs. Zugegriffen: 11. September 2026. [Online]. Verfügbar unter: <https://code.claude.com/docs/en/hooks>

[43] S. Amershi *u. a.*, „Guidelines for Human-AI Interaction“, in *Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems*, 2019. doi: [10.1145/3290605.3300233](https://doi.org/10.1145/3290605.3300233).

[44] A. Wei, N. Haghtalab, und J. Steinhardt, „Jailbroken: How Does LLM Safety Training Fail?“, in *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*, 2023. Verfügbar unter: <https://arxiv.org/abs/2307.02483>

[45] C. Guo, G. Pleiss, Y. Sun, und K. Q. Weinberger, „On Calibration of Modern Neural Networks“, in *Proceedings of the 34th International Conference on Machine Learning (ICML)*, 2017. Verfügbar unter: <https://arxiv.org/abs/1706.04599>

[46] F. Miao und W. Holmes, „Guidance for generative AI in education and research“, UNESCO, Paris, 2023. doi: [10.54675/EWZM9535](https://doi.org/10.54675/EWZM9535).

[47] Anthropic, „Configure permissions“, Claude Code Docs. Zugegriffen: 11. September 2026. [Online]. Verfügbar unter: <https://code.claude.com/docs/en/permissions>

[48] L. Zheng *u. a.*, „Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena“, in *Advances in Neural Information Processing Systems 36 (NeurIPS 2023), Datasets and Benchmarks Track*, 2023. Verfügbar unter: <https://arxiv.org/abs/2306.05685>

[49] IBM, „What Is Loop Engineering?“, IBM Think. Zugegriffen: 11. September 2026. [Online]. Verfügbar unter: <https://www.ibm.com/think/topics/loop-engineering>

[50] Anthropic, „Introducing the Model Context Protocol“, Anthropic News. Zugegriffen: 11. September 2026. [Online]. Verfügbar unter: <https://www.anthropic.com/news/model-context-protocol>

[51] Anthropic, „Connect Claude Code to tools via MCP“, Claude Code Docs. Zugegriffen: 11. September 2026. [Online]. Verfügbar unter: <https://code.claude.com/docs/en/mcp>

[52] C. Olah, N. Cammarata, L. Schubert, G. Goh, M. Petrov, und S. Carter, „Zoom In: An Introduction to Circuits“, *Distill*, 2020, doi: [10.23915/distill.00024.001](https://doi.org/10.23915/distill.00024.001).

[53] N. Shazeer *u. a.*, „Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer“, in *International Conference on Learning Representations (ICLR)*, 2017. Verfügbar unter: <https://arxiv.org/abs/1701.06538>

[54] M. Mitchell *u. a.*, „Model Cards for Model Reporting“, in *Proceedings of the Conference on Fairness, Accountability, and Transparency (FAT\*)*, 2019, S. 220-229. doi: [10.1145/3287560.3287596](https://doi.org/10.1145/3287560.3287596).

[55] A. Radford *u. a.*, „Learning Transferable Visual Models From Natural Language Supervision“, in *Proceedings of the 38th International Conference on Machine Learning (ICML)*, 2021. Verfügbar unter: <https://arxiv.org/abs/2103.00020>

[56] Open Source Initiative, „The Open Source AI Definition 1.0“. Zugegriffen: 11. September 2026. [Online]. Verfügbar unter: <https://opensource.org/ai/open-source-ai-definition>

[57] TU Dortmund, ITMC, „„Inferenz NRW“ ist gestartet: Souveräne KI-Modelle für die Hochschulen in Nordrhein-Westfalen“. April 2026. Zugegriffen: 11. September 2026. [Online]. Verfügbar unter: <https://itmc.tu-dortmund.de/storages/itmc/Bilder/News/2026/Info-Inferenz-NRW-Start.pdf>

[58] Anthropic, „Desktop application“, Claude Code Docs. Zugegriffen: 11. September 2026. [Online]. Verfügbar unter: <https://code.claude.com/docs/en/desktop>

[59] Anthropic, „Discover and install prebuilt plugins through marketplaces“, Claude Code Docs. Zugegriffen: 11. September 2026. [Online]. Verfügbar unter: <https://code.claude.com/docs/en/discover-plugins>

[60] Anthropic, „Prompt engineering overview“, Claude Docs. Zugegriffen: 11. September 2026. [Online]. Verfügbar unter: <https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview>

[61] K. Greshake, S. Abdelnabi, S. Mishra, C. Endres, T. Holz, und M. Fritz, „Not What You’ve Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection“, in *Proceedings of the 16th ACM Workshop on Artificial Intelligence and Security (AISec)*, 2023. Verfügbar unter: <https://arxiv.org/abs/2302.12173>

[62] E. Schluntz und B. Zhang, „Building effective agents“, Anthropic Research. Zugegriffen: 11. September 2026. [Online]. Verfügbar unter: <https://www.anthropic.com/research/building-effective-agents>

[63] T. Dettmers, M. Lewis, Y. Belkada, und L. Zettlemoyer, „LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale“, in *Advances in Neural Information Processing Systems 35 (NeurIPS 2022)*, 2022. Verfügbar unter: <https://arxiv.org/abs/2208.07339>

[64] P. Lewis *u. a.*, „Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks“, in *Advances in Neural Information Processing Systems 33 (NeurIPS 2020)*, 2020, S. 9459-9474. Verfügbar unter: <https://arxiv.org/abs/2005.11401>

[65] S. Yao *u. a.*, „ReAct: Synergizing Reasoning and Acting in Language Models“, in *International Conference on Learning Representations (ICLR)*, 2023. Verfügbar unter: <https://arxiv.org/abs/2210.03629>

[66] C. Snell, J. Lee, K. Xu, und A. Kumar, „Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters“, 2024, 2408.03314. Verfügbar unter: <https://arxiv.org/abs/2408.03314>

[67] E. Perez *u. a.*, „Red Teaming Language Models with Language Models“, in *Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, 2022. Verfügbar unter: <https://arxiv.org/abs/2202.03286>

[68] J. Pan, H. He, S. R. Bowman, und S. Feng, „Spontaneous Reward Hacking in Iterative Self-Refinement“, 2024, 2407.04549. Verfügbar unter: <https://arxiv.org/abs/2407.04549>

[69] National Institute of Standards and Technology, „Artificial Intelligence Risk Management Framework (AI RMF 1.0)“, NIST, Gaithersburg, MD, NIST AI 100-1, 2023. doi: [10.6028/NIST.AI.100-1](https://doi.org/10.6028/NIST.AI.100-1).

[70] P. F. Christiano, J. Leike, T. B. Brown, M. Martic, S. Legg, und D. Amodei, „Deep Reinforcement Learning from Human Preferences“, in *Advances in Neural Information Processing Systems 30 (NeurIPS 2017)*, 2017. Verfügbar unter: <https://arxiv.org/abs/1706.03741>

[71] L. Ouyang *u. a.*, „Training language models to follow instructions with human feedback“, in *Advances in Neural Information Processing Systems 35 (NeurIPS 2022)*, 2022. Verfügbar unter: <https://arxiv.org/abs/2203.02155>

[72] J. Kaplan *u. a.*, „Scaling Laws for Neural Language Models“, 2020, 2001.08361. Verfügbar unter: <https://arxiv.org/abs/2001.08361>

[73] J. Hoffmann *u. a.*, „Training Compute-Optimal Large Language Models“, in *Advances in Neural Information Processing Systems 35 (NeurIPS 2022)*, 2022. Verfügbar unter: <https://arxiv.org/abs/2203.15556>

[74] A. Madaan *u. a.*, „Self-Refine: Iterative Refinement with Self-Feedback“, in *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*, 2023. Verfügbar unter: <https://arxiv.org/abs/2303.17651>

[75] J. Huang *u. a.*, „Large Language Models Cannot Self-Correct Reasoning Yet“, in *International Conference on Learning Representations (ICLR)*, 2024. Verfügbar unter: <https://arxiv.org/abs/2310.01798>

[76] Anthropic, „Extend Claude with skills“, Claude Code Docs. Zugegriffen: 11. September 2026. [Online]. Verfügbar unter: <https://code.claude.com/docs/en/skills>

[77] A. Bondarenko, D. Volk, D. Volkov, und J. Ladish, „Demonstrating Specification Gaming in Reasoning Models“, 2025, 2502.13295. Verfügbar unter: <https://arxiv.org/abs/2502.13295>

[78] A. Radford, J. W. Kim, T. Xu, G. Brockman, C. McLeavey, und I. Sutskever, „Robust Speech Recognition via Large-Scale Weak Supervision“, in *Proceedings of the 40th International Conference on Machine Learning (ICML)*, 2023. Verfügbar unter: <https://arxiv.org/abs/2212.04356>

[79] W. X. Zhao *u. a.*, „A Survey of Large Language Models“, 2023, 2303.18223. Verfügbar unter: <https://arxiv.org/abs/2303.18223>

[80] L. Weidinger *u. a.*, „Ethical and social risks of harm from Language Models“, 2021, 2112.04359. Verfügbar unter: <https://arxiv.org/abs/2112.04359>

[81] *§ 44b UrhG: Text und Data Mining*. Zugegriffen: 11. September 2026. [Online]. Verfügbar unter: <https://www.gesetze-im-internet.de/urhg/__44b.html>

[82] R. Sennrich, B. Haddow, und A. Birch, „Neural Machine Translation of Rare Words with Subword Units“, in *Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (ACL)*, 2016, S. 1715-1725. doi: [10.18653/v1/P16-1162](https://doi.org/10.18653/v1/P16-1162).

[83] T. Schick *u. a.*, „Toolformer: Language Models Can Teach Themselves to Use Tools“, in *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*, 2023. Verfügbar unter: <https://arxiv.org/abs/2302.04761>

[84] Anthropic, „Create custom subagents“, Claude Code Docs. Zugegriffen: 11. September 2026. [Online]. Verfügbar unter: <https://code.claude.com/docs/en/sub-agents>

[85] J. Johnson, M. Douze, und H. Jégou, „Billion-scale similarity search with GPUs“, *IEEE Transactions on Big Data*, Bd. 7, Nr. 3, S. 535-547, 2021, Verfügbar unter: <https://arxiv.org/abs/1702.08734>

[86] A. Hogan *u. a.*, „Knowledge Graphs“, *ACM Computing Surveys*, Bd. 54, Nr. 4, 2021, doi: [10.1145/3447772](https://doi.org/10.1145/3447772).

[87] E. Kasneci *u. a.*, „ChatGPT for good? On opportunities and challenges of large language models for education“, *Learning and Individual Differences*, Bd. 103, 2023, doi: [10.1016/j.lindif.2023.102274](https://doi.org/10.1016/j.lindif.2023.102274).
