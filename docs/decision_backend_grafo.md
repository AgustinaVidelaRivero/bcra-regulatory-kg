# Decisión: backend de grafo para el harness KG-RAG (post-extracción-v2)

> Documento de decisión. La mitad forense — de dónde viene el algoritmo de búsqueda
> actual, con qué justificación y con qué limitaciones medidas — está en
> [docs/trazabilidad_algoritmo_busqueda.md](trazabilidad_algoritmo_busqueda.md); este
> documento la da por leída y decide qué lo reemplaza, bajo qué criterio, y cuándo.
> Registro en primera persona. Fecha: 2026-07-25.

## 1. Contexto y problema

El retrieval del harness (`GraphIndex.buscar_nodos`,
[harness.py:148](../data/experiment/evaluacion/harness.py:148)) es una **heurística
ad-hoc**: matching booleano por intersección de tokens de la consulta contra los tokens
de label+id de cada nodo, sin ponderación de ningún tipo — sin TF-IDF, sin BM25, sin
pesos por rareza, sin normalización por largo, sin stemming, sin sinónimos. El informe de
trazabilidad ([trazabilidad_algoritmo_busqueda.md](trazabilidad_algoritmo_busqueda.md)
§3-§4) estableció que fue introducido en el commit `7e8b91e` (2026-06-10) sin
justificación documentada del scoring, que su pariente más cercano en la literatura es el
*coordination-level ranking* de los sistemas booleanos pre-ponderación, y que el hallazgo
honesto es que se trata de la primera versión naive que cualquiera escribe.

El proyecto ya midió tres limitaciones que se derivan directamente de ese diseño (detalle
y evidencia en [trazabilidad_algoritmo_busqueda.md](trazabilidad_algoritmo_busqueda.md) §4):

1. **Indexación label+id solamente → "existe pero inalcanzable" (el tercer estado).**
   Hallazgo H6 sobre CQ-031 ([hallazgos_tesis.md:70-86](hallazgos_tesis.md:70)): nodo con
   la description verbatim del PDF, 0 hits en las 10 búsquedas reales del agente porque
   `buscar_nodos` no indexa description. Elevado a categoría propia de la taxonomía
   (`alcanzabilidad_kg`,
   [taxonomia.md:48](../.claude/skills/kg-refinement/references/taxonomia.md)) y a prueba
   determinística ex ante (módulo D1,
   [especificacion_capa_deterministica.md:38](especificacion_capa_deterministica.md:38)).
2. **Entierro por ranking (mecanismo B′).** CQN2-015: portador existente y fiel, con
   match léxico positivo, en rank global 11 de 50 contra el corte top-10 — "match léxico
   positivo, nunca visible" ([casos_gate_cqn2.md:358-372](casos_gate_cqn2.md:358);
   medición verbatim en
   [evidencia_gate_cqn2/cqn2_015.md:299](evidencia_gate_cqn2/cqn2_015.md:299); la laguna
   de instrumento — D2 no distingue B′ de la inalcanzabilidad léxica — en
   [lectura_ciclo2.md:105-107](lectura_ciclo2.md:105)).
3. **Sin sinónimos ni morfología.** Singular/plural sin stemming medido en la validación
   (`deudor_en_situacion_normal` vs "deudores",
   [casos_validacion.md:253](../.claude/skills/kg-refinement/references/casos_validacion.md));
   la ausencia de capa semántica es consistente con el hallazgo MiniLM del Run 4
   ([run_4_schema_light/schema.md:199-201](../data/experiment/run_4_schema_light/schema.md:199)).

**Criterio de adopción.** Adopto el criterio de que cualquier backend de recuperación
nuevo debe usar **algoritmos open source o descriptos a nivel pseudocódigo/paper
citable**: en una tesis cuyo instrumento de medición es el propio sistema de
recuperación, no puedo defender resultados producidos por un componente que no puedo
inspeccionar ni citar. Nada que facilite oscureciendo. Este criterio es el filtro de todo
lo que sigue.

## 2. Investigación de licenciamiento y transparencia (estado 2026)

- **(a) Neo4j Community Edition:** licencia **GPLv3**, código público
  (github.com/neo4j/neo4j). Incluye índices **full-text** y **vectoriales** en el tier
  Community.
- **(b) Full-text = Apache Lucene** (licencia **Apache 2.0**), con **BM25 por defecto**.
  El método tiene paper canónico citable — Robertson et al., *Okapi at TREC-3* (1994) —
  y la fórmula con sus constantes (k1=1.2, b=0.75) está publicada en el Javadoc de
  `BM25Similarity` de Lucene. Es exactamente lo que el algoritmo actual no tiene: pesos
  por rareza de término (IDF) y normalización por largo, con procedencia citable.
- **(c) Índice vectorial = HNSW de Lucene.** Paper citable: Malkov & Yashunin. Regla de
  reporte: **declararlo siempre como recuperación aproximada** (ANN), nunca como
  búsqueda exacta.
- **(d) Planner de Cypher:** cost-based, auditable con `EXPLAIN`/`PROFILE`. La heurística
  de estimación de cardinalidad no tiene pseudocódigo completo público, pero afecta **el
  plan de ejecución, no qué se recupera**: el conjunto resultado de una query declarativa
  es el mismo con cualquier plan. Compatible con el criterio, con esa salvedad
  documentada.
- **(e) GDS (Graph Data Science):** los algoritmos completos están disponibles en el tier
  Community como **OpenGDS** (GPLv3).
- **(f) A evitar por opacidad o licencia:** **AuraDB** (servicio propietario; los ToS
  prohíben la inspección), **Enterprise Edition** y su runtime *pipelined* — además de
  opacos, innecesarios para este caso de uso (un grafo chico, un solo usuario, sin HA).

## 3. Alternativas evaluadas

| Alternativa | Licencia / estado (2026) | Veredicto según el criterio |
|---|---|---|
| Memgraph | BSL 1.1 — source-available, **no** open source OSI | Descartada por licencia |
| ArangoDB | BSL 1.1 — source-available, **no** open source OSI | Descartada por licencia |
| Kùzu | MIT, pero repo **archivado** tras su adquisición (oct-2025) | Descartada por mantenimiento |
| SQLite FTS5 + grafo propio | Dominio público; BM25 nativo con fórmula publicada; cero infraestructura | **Alternativa minimalista legítima** |
| Neo4j Community Edition | GPLv3, código público; Lucene BM25 + HNSW incluidos | **Adoptada** (§4) |

SQLite FTS5 es la alternativa que me tomo en serio: cumple el criterio (BM25 con fórmula
publicada) con cero infraestructura, y sería **preferible si el corpus final queda chico**
— umbral orientativo: **<10k nodos y solo travesía 1-hop**. Por encima de eso, el grafo
propio sobre SQLite empieza a reimplementar lo que Neo4j ya trae (adyacencia, travesías
multi-hop, planner).

Dos cosas bajan el costo de equivocarse acá: el **contrato de tools del harness
(`buscar_nodos`/`ver_nodo`/`ver_vecinos`) es backend-agnóstico** — ninguna de las tres
firmas expone el motor —, y la decisión fina entre candidatos que cumplen el criterio
**puede tomarla el benchmark del plan (§5.3), no la opinión**.

## 4. Decisión y timing

**Adopto Neo4j Community Edition, self-hosted, con la migración post-extracción-v2.**

Razones del timing (después de que la extracción v2 estabilice el esquema, no antes):

1. **Modelar una sola vez.** Migrar ahora obligaría a re-modelar el grafo cuando la
   extracción v2 cambie el esquema; sobre el esquema estable, el modelado a Neo4j se hace
   una vez.
2. **Migración incremental de bajo riesgo.** El harness actual sobre JSON en memoria
   queda como fallback funcionando durante toda la migración; ninguna etapa del plan (§5)
   rompe lo existente.
3. **Habilita el benchmark.** El baseline booleano y el retador BM25 corriendo sobre el
   mismo grafo y las mismas consultas es material de tesis directo (§5.3).

**Analyzer de Lucene para español: elegir y documentar explícitamente.** La tokenización
y el stemming del analyzer afectan los resultados tanto como la fórmula BM25 — dejar el
default sin declararlo sería repetir el patrón que la trazabilidad documentó (parámetros
con consecuencias medibles y sin rationale escrito).

## 5. Plan de migración en etapas

1. **Full-text primero.** Índice full-text sobre label + id + propiedades textuales
   (incluida `description` — cierra de raíz la limitación 1 de §1) y reimplementación de
   `buscar_nodos` vía `db.index.fulltext.queryNodes`. Misma firma, mismo contrato de
   salida.
2. **Cypher para las otras dos tools.** `ver_nodo` y `ver_vecinos` como queries Cypher;
   planes verificados con `PROFILE` (la salvedad (d) de §2 se audita acá).
3. **Benchmark pre-registrado.** Recall@K con verdad-terreno, **matching booleano actual
   vs BM25, mismo grafo y mismas consultas**. Los casos ya medidos (CQ-031, CQN2-015)
   entran como casos de verdad-terreno: si BM25 no desentierra al portador de rank 11 ni
   alcanza al nodo de CQ-031 con description indexada, el reemplazo no se justifica.
   Material de tesis directo.
4. **Opcional, solo si el benchmark lo pide:** índice vectorial (declarado como
   recuperación aproximada, regla (c) de §2) o algoritmos de OpenGDS.

**Mecanismo de implementación: la modularización del harness.** Este documento es el
primer registro escrito de esa modularización (no hay doc previo que la registre): una
interfaz de estrategia de recuperación intercambiable — baseline booleana (la actual) /
retadora BM25 — detrás del contrato de tools. La restricción operativa ya está
documentada y se respeta: el cuarteto `loader/harness/judge/llm_cache` **no se edita** —
las extensiones van en módulos aparte que importan al núcleo congelado, y cualquier
edición del cuarteto rota el `code_version` de la caché (namespace bump), como quedó
demostrado en el evento de los dos namespaces
([evaluacion/README.md:11-19](../data/experiment/evaluacion/README.md:11)). La estrategia
retadora se implementa entonces como módulo nuevo, con bump de namespace explícito y
documentado si alguna vez se decide tocar el cuarteto.

## 6. Referencias citables

- Robertson, S. E. et al. (1994). *Okapi at TREC-3*. — paper canónico de BM25.
- Javadoc de `BM25Similarity` (Apache Lucene) — fórmula y constantes k1=1.2, b=0.75.
- Malkov, Y. & Yashunin, D. — *Efficient and robust approximate nearest neighbor search
  using Hierarchical Navigable Small World graphs* (HNSW).
- Documentación oficial de Neo4j: full-text indexes, vector indexes, query tuning
  (`EXPLAIN`/`PROFILE`).
- Repositorios públicos: neo4j/neo4j (GPLv3), OpenGDS (GPLv3), apache/lucene
  (Apache 2.0).
- Documentación de SQLite FTS5 (BM25 nativo).
