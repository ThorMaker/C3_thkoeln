# Graph Report - .  (2026-09-12)

## Corpus Check
- Corpus is ~659 words - fits in a single context window. You may not need a graph.

## Summary
- 56 nodes · 138 edges · 8 communities (7 shown, 1 thin omitted)
- Extraction: 90% EXTRACTED · 9% INFERRED · 1% AMBIGUOUS · INFERRED: 13 edges (avg confidence: 0.85)
- Token cost: 127,886 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Zettelkasten und Second Brain|Zettelkasten und Second Brain]]
- [[_COMMUNITY_RAG, Wissensgraph und KI-Labor|RAG, Wissensgraph und KI-Labor]]
- [[_COMMUNITY_GraphRAG und Verdichten|GraphRAG und Verdichten]]
- [[_COMMUNITY_ReAct und KI-Agenten|ReAct und KI-Agenten]]
- [[_COMMUNITY_KI-Richtlinie der Fakultät|KI-Richtlinie der Fakultät]]
- [[_COMMUNITY_Fakultätsrat und Beschlüsse|Fakultätsrat und Beschlüsse]]
- [[_COMMUNITY_Prüfungsformate mit KI|Prüfungsformate mit KI]]
- [[_COMMUNITY_Kennzeichnung und Reflexion|Kennzeichnung und Reflexion]]

## God Nodes (most connected - your core abstractions)
1. `Lehrprojekt KI-Labor` - 13 edges
2. `Graph RAG (Edge et al., 2024)` - 12 edges
3. `Vorlesungsnotiz: Wissensgraph-Grundlagen` - 11 edges
4. `Wissensgraph` - 11 edges
5. `Retrieval-Augmented Generation (RAG)` - 10 edges
6. `Protokoll Fakultätsrat, Juli 2026` - 9 edges
7. `Prüfungsformate mit KI` - 9 edges
8. `Entwurf: KI-Richtlinie der Fakultät` - 9 edges
9. `Vorlesungsnotiz: Zettelkasten-Prinzip` - 8 edges
10. `Arbeitsnotiz: Literatur verdichten mit KI` - 8 edges

## Surprising Connections (you probably didn't know these)
- `Verweise zwischen Notizen (feste Adressen)` --semantically_similar_to--> `Kanten (Beziehungen)`  [INFERRED] [semantically similar]
  zettelkasten-prinzip.md → wissensgraph-grundlagen.md
- `Gezielt laden statt alles in den Kontext kippen` --semantically_similar_to--> `Distill (verdichten)`  [INFERRED] [semantically similar]
  paper-lost-in-the-middle.md → second-brain-code-methode.md
- `Entitäts- und Beziehungsextraktion durch ein Modell` --semantically_similar_to--> `Exzerpt-Schema: Kernaussage, Methode, Ergebnis, Grenzen`  [INFERRED] [semantically similar]
  paper-graphrag.md → notiz-literatur-verdichten.md
- `Mündliche Reflexion` --semantically_similar_to--> `Kennzeichnungspflicht`  [INFERRED] [semantically similar]
  pruefungsformate-mit-ki.md → ki-richtlinie-entwurf.md
- `Arbeitsnotiz: Literatur verdichten mit KI` --references--> `Datenschutz-Regel`  [INFERRED]
  notiz-literatur-verdichten.md → ki-richtlinie-entwurf.md

## Hyperedges (group relationships)
- **Lehrprojekt KI-Labor: RAG und Wissensgraph im Vergleich** — unterlagen_idee_ki_labor, unterlagen_idee_ki_labor_vergleich_rag_graph, unterlagen_rag_grundlagen_rag, unterlagen_wissensgraph_grundlagen_wissensgraph, unterlagen_paper_graphrag, unterlagen_paper_react, unterlagen_pruefungsformate_mit_ki_agenten_projekt [EXTRACTED 1.00]
- **CODE-Methode: Capture, Organize, Distill, Express** — unterlagen_second_brain_code_methode_code_methode, unterlagen_second_brain_code_methode_capture, unterlagen_second_brain_code_methode_organize, unterlagen_second_brain_code_methode_distill, unterlagen_second_brain_code_methode_express [EXTRACTED 1.00]
- **Muster: Nur das Relevante laden und verdichten** — unterlagen_paper_lost_in_the_middle_gezielt_laden, unterlagen_rag_grundlagen_rag, unterlagen_wissensgraph_grundlagen_wissensgraph, unterlagen_paper_graphrag_community_zusammenfassung, unterlagen_notiz_literatur_verdichten_exzerpt_schema, unterlagen_second_brain_code_methode_distill [INFERRED 0.75]

## Communities (8 total, 1 thin omitted)

### Community 0 - "Zettelkasten und Second Brain"
Cohesion: 0.27
Nodes (14): Vorlesungsnotiz: Second Brain und CODE-Methode, Capture (erfassen), CODE-Methode, Express (nutzen), Mischform für Lehrende: Projektordner je Lehrveranstaltung plus Querverweise, Organize (ordnen), Second Brain, Tiago Forte (+6 more)

### Community 1 - "RAG, Wissensgraph und KI-Labor"
Cohesion: 0.35
Nodes (14): Lehrprojekt KI-Labor, Vergleich RAG vs. Wissensgraph (Antworten und Nachvollziehbarkeit), Lost in the Middle (Liu et al., 2024), Gezielt laden statt alles in den Kontext kippen, Positionseffekt im langen Kontext, Vorlesungsnotiz: RAG-Grundlagen, Retrieval-Augmented Generation (RAG), Retrieval (Ähnlichkeitssuche) (+6 more)

### Community 2 - "GraphRAG und Verdichten"
Cohesion: 0.46
Nodes (8): Arbeitsnotiz: Literatur verdichten mit KI, Exzerpt-Schema: Kernaussage, Methode, Ergebnis, Grenzen, Graph RAG (Edge et al., 2024), Vorab zusammengefasste Communities, Entitäts- und Beziehungsextraktion durch ein Modell, Globale Fragen an eine Dokumentsammlung („Welche Hauptthemen gibt es?“), Distill (verdichten), Communities (Themengruppen)

### Community 3 - "ReAct und KI-Agenten"
Cohesion: 0.70
Nodes (5): ReAct (Yao et al., 2023), KI-Agenten, Claude Code, Denken und Handeln im Wechsel, Agenten-Projekt

### Community 4 - "KI-Richtlinie der Fakultät"
Cohesion: 0.50
Nodes (5): Entwurf: KI-Richtlinie der Fakultät, Datenschutz-Regel, Kompetenz: Fortbildungen für Lehrende und Studierende, Beschluss TOP 1: KI-Richtlinie bis Wintersemester überarbeiten, Studiengangsteam

### Community 5 - "Fakultätsrat und Beschlüsse"
Cohesion: 0.70
Nodes (5): Protokoll Fakultätsrat, Juli 2026, Arbeitsgruppe Prüfung, Beschluss TOP 3: Antrag auf Lehrförderung KI-Labor unterstützt, Beschluss TOP 2: Pilot mündliche Reflexionsgespräche in zwei Modulen, Fakultätsrat

### Community 6 - "Prüfungsformate mit KI"
Cohesion: 0.67
Nodes (3): Prüfungsgrundsatz: Mensch entscheidet, KI assistiert, Prüfungsformate mit KI, Prozessportfolio (Versionsverlauf mit Git)

## Ambiguous Edges - Review These
- `Datenschutz-Regel` → `Beschluss TOP 1: KI-Richtlinie bis Wintersemester überarbeiten`  [AMBIGUOUS]
  protokoll-fakultaetsrat-2026-07.md · relation: references

## Knowledge Gaps
- **3 isolated node(s):** `Capture (erfassen)`, `Express (nutzen)`, `Prozessportfolio (Versionsverlauf mit Git)`
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Datenschutz-Regel` and `Beschluss TOP 1: KI-Richtlinie bis Wintersemester überarbeiten`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **Why does `Lehrprojekt KI-Labor` connect `RAG, Wissensgraph und KI-Labor` to `Zettelkasten und Second Brain`, `GraphRAG und Verdichten`, `ReAct und KI-Agenten`, `Fakultätsrat und Beschlüsse`, `Prüfungsformate mit KI`?**
  _High betweenness centrality (0.304) - this node is a cross-community bridge._
- **Why does `Arbeitsnotiz: Literatur verdichten mit KI` connect `GraphRAG und Verdichten` to `Zettelkasten und Second Brain`, `RAG, Wissensgraph und KI-Labor`, `ReAct und KI-Agenten`, `KI-Richtlinie der Fakultät`?**
  _High betweenness centrality (0.180) - this node is a cross-community bridge._
- **Why does `Vorlesungsnotiz: Second Brain und CODE-Methode` connect `Zettelkasten und Second Brain` to `GraphRAG und Verdichten`?**
  _High betweenness centrality (0.132) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `Retrieval-Augmented Generation (RAG)` (e.g. with `Positionseffekt im langen Kontext` and `Graph RAG (Edge et al., 2024)`) actually correct?**
  _`Retrieval-Augmented Generation (RAG)` has 3 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Capture (erfassen)`, `Express (nutzen)`, `Kompetenz: Fortbildungen für Lehrende und Studierende` to the rest of the system?**
  _4 weakly-connected nodes found - possible documentation gaps or missing edges._