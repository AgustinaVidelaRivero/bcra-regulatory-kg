# Barrida: releases de KG como recurso post-LLM (tarea mentor 26/08)

Hecha el 03/09 contra fuentes primarias (arXiv, Nature, ACL Anthology,
Springer, Zenodo). Las entradas biblatex correspondientes están en
docs/tesis/bibliografia.bib; la prosa, en el movimiento de releases de
1.4 Estado del arte del main.tex. Este archivo registra el respaldo.

## Recursos relevados que entran en el Estado del arte

| Recurso | Dominio | LLM en construcción | Procedencia por hecho | Evaluación de contenido | Publicación |
|---|---|---|---|---|---|
| DBpedia 2007 (auer2007dbpedia) | enciclopédico | no | no | ninguna formal | dumps + SPARQL, GFDL |
| DBpedia 2015 (lehmann2015dbpedia) | enciclopédico multilingüe | no | no | sin evaluación intrínseca | releases regulares, 111 ediciones |
| PrimeKG (chandak2023primekg, Sci Data 2023) | biomedicina, 20 bases curadas | no | — | validación técnica vs. otros recursos | Harvard Dataverse, DOI |
| iKraph (zhang2025ikraph, Nat MI 2025) | biomedicina, 34M abstracts | PLMs tipo BERT, no LLM generativo | a nivel artículo | muestra 50 abstracts vs. humanos | Zenodo DOI, CC BY 4.0 |
| PlantConnectome (lim2025plantconnectome, Plant Cell 2025) | biología vegetal, >71.000 artículos | GPT-4o extrae, GPT-4o-mini anota | sí: arista -> PubMed ID | muestreo manual, 85 %/93 % | web + descarga + GitHub |
| MDKG (gao2025mdkg, Nat Comms 2025) | salud mental, 234.087 abstracts | GPT-4 extrae, GPT-4o refina | a nivel publicación | 200 tripletas, 4 expertos, 79 % | portal + corpus Zenodo CC BY |
| Disaster Storylines (ronco2026disaster, Sci Data 2026) | noticias de desastres, 3.158 eventos | Llama-3-70B con RAG | parcial (back-mapping determinístico) | 1.000 tripletas, 6 expertos | Zenodo DOI, CC BY-NC-ND |
| FinDKG (li2024findkg, ICAIF 2024) | noticias financieras WSJ | Mistral 7B destilado de GPT-4 | no | sin evaluación de contenido | GitHub GPL-3.0, sin DOI de datos |
| GPTKB (hu2025gptkb, ACL 2025) | conocimiento interno de GPT-4o-mini | el LLM es la fuente | no (declarado como limitación) | muestreo por entailment: 31 % True | gptkb.org, dump TTL, CC BY-NC |

## Punteros de la reunión del 26/08, resueltos

1. Nature s41597-023-01960-3 = PrimeKG. Citado. Verificado que NO usa LLM
   generativo (border, como advirtió el mentor): va como tradición
   biomédica, no como caso post-LLM.
2. PMC12995551 = survey de KGs en salud (Cui et al., J Biomed Informatics
   169:104861, 2025, doi 10.1016/j.jbi.2025.104861). No construye, no usa
   LLM, no publica recurso. Candidato opcional para el Marco teórico.
3. Scholar ymKWDvoAAAAJ = Simon Razniewski (TU Dresden, ex MPI). Su paper
   principal post-LLM es GPTKB, ya citado. Derivación clave: Razniewski
   et al., "Completeness, Recall, and Negation in Open-world Knowledge
   Bases: A Survey", ACM CSUR 56(6), 2024, doi 10.1145/3639563 ->
   lectura para el capítulo de evaluación intrínseca (recall sin verdad
   de referencia). GPTKB v1.5 (AAAI 2026) aún sin actas: no citable.
4. arXiv 2510.20345 = Bian, "LLM-empowered knowledge graph construction:
   A survey" (preprint de autor único, oct 2025). Taxonomía en tres capas.
   No trata evaluación, procedencia ni publicación de recursos -> encuadre
   para el Marco teórico, citar con cautela.
5. Scholar INQwsQkAAAAJ = Christian Bizer (Mannheim, cofundador de
   DBpedia). Trabajo reciente: entity matching con LLMs (Peeters & Bizer,
   ADBIS 2023 / EDBT 2025) -> material para el capítulo de construcción
   (anti-fusión, canonización).
6. DBpedia "más nuevo" = Lehmann et al. 2015, SWJ 6(2):167-195,
   doi 10.3233/SW-140134. Citado.

## Descartados con razón

SPOKE (no descargable) · CKG y AlzKB (sin LLM) · NLP-AKG (no publica el
grafo) · Tem-DocRED (benchmark, no recurso) · ISWC 2024 resources track
(ningún KG con LLM).

## Caveats de verificación

- FinDKG: páginas y DOI tomados del journal-ref de arXiv (ACM DL dio 403).
- GPTKB: día exacto de la v1 no confirmado (mes sí: nov 2024).
- Disaster Storylines: precisión desagregada por tipo de desastre, sin
  agregado único; no citar un número global.
- MDKG: el DOI de Zenodo es del corpus de anotación, no del grafo.
- PMC12995551: PMC bloquea fetchers; identificado vía Europe PMC y
  verificado contra el preprint arXiv:2306.04802.

## Ejecución pendiente que esta barrida refuerza

El depósito con identificador permanente y licencia ya está especificado
en el plan (C2.1, docs/plan_tesis.md:648: release etiquetado + Zenodo/DOI
con grafos, sets sellados, gold, scripts y README). Lo pendiente es
únicamente ejecutarlo; el checklist FAIR ya forma parte del entregable
por decisión de la autora. Cuando se ejecute, la
contribución 1 de la Introducción suma "publicado con depósito permanente
y licencia".
