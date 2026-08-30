# U-RW — Bitácora de consultas de búsqueda (auditable y repetible)

Motor: herramienta WebSearch de la sesión (índice web, resultados US).
Fecha de la barrida: 2026-08-27. Costo de API del proyecto: USD 0.
Los strings están tal cual se enviaron.

## Consultas WebSearch (8)

| # | String exacto | Dónde | Qué rindió |
|---|---|---|---|
| Q1 | `2025 knowledge graph resource paper LLM-based construction release dataset descriptor` | WebSearch | NLP-AKG (R4), pistas de JMIR y Frontiers |
| Q2 | `"resource paper" knowledge graph 2025 ISWC resource track LLM constructed evaluation quality` | WebSearch | TextMineX (R5), ACL Findings (R10), pista de ODKE+ |
| Q3 | `LLM knowledge graph extraction failure modes bias hallucination relation extraction systematic errors 2025` | WebSearch | GraphMERT (R11) |
| Q4 | `legal knowledge graph release 2025 regulations LLM extraction ontology published resource evaluation` | WebSearch | R1, R2, R3 (las tres entradas legales) |
| Q5 | `food science agriculture materials knowledge graph 2025 2026 LLM built released dataset paper human expert validation` | WebSearch | Sin candidato que sobreviviera al triage: predominan aplicaciones GraphRAG y reviews, no releases de recurso |
| Q6 | `evaluating quality of LLM-generated knowledge graph triples human annotation study errors ontology drift 2025` | WebSearch | R8 (CKD multi-view), R9 (GenAIK curator) |
| Q7 | `arXiv 2025 LLM information extraction bias prompt sensitivity schema drift study knowledge base construction reliability` | WebSearch | R12 (sensibilidad prompt/modelo/esquema) |
| Q8 | `Scientific Data 2026 knowledge graph large language model construction data descriptor technical validation` | WebSearch | R6 (MedKGent), R13 (GraphJudge) |
| Q9 | `ODKE+ ontology-guided open domain knowledge extraction production knowledge graph 2025 arXiv` | WebSearch | R7 (confirmación del arXiv id) |
| Q10 | `arXiv 2025 2026 how reliable are LLMs as annotators for relation extraction systematic evaluation errors under-extraction recall` | WebSearch | R14, R15 |

## Verificaciones (WebFetch / lectura de PDF) — 17 accesos

Exitosas (16):
- arxiv.org/abs/2508.06368 · arxiv.org/abs/2508.06368v1 (re-verificación de la línea de autoría)
- arxiv.org/abs/2607.24551
- arxiv.org/abs/2509.15098
- arxiv.org/abs/2502.14192
- arxiv.org/abs/2606.05970
- arxiv.org/abs/2510.09580
- arxiv.org/abs/2508.12393
- arxiv.org/abs/2411.17388
- arxiv.org/abs/2509.04696
- arxiv.org/abs/2506.00777
- arxiv.org/abs/2407.19568
- aclanthology.org/2025.genaik-1.10/
- aclanthology.org/2025.findings-acl.602/
- pmc.ncbi.nlm.nih.gov/articles/PMC12689688/
- vldb.org/2025/Workshops/VLDB-Workshops-2025/LLM+Graph/LLMGraph-2.pdf (PDF descargado; leídas pp. 1 y 6–8)

Fallidas (3, declaradas):
- sciencedirect.com/science/article/pii/S030645732500086X → HTTP 403
- pubs.rsc.org/en/content/articlehtml/2026/dd/d5dd00275c → HTTP 403
- jmir.org/2025/1/e65537/ y /PDF → cuerpo vacío en ambos intentos

## Nota de repetibilidad

El índice de búsqueda devolvió trabajos con identificadores arXiv de 2026 (p. ej. 2606.*,
2607.*), consistentes con la fecha de la sesión. Quien repita la barrida más adelante debe
esperar resultados distintos en las franjas B y C, que son las de mayor rotación.
