# Backend Neo4j (experimental) — migración del índice de grafo

Migración experimental del backend de las 3 tools del agente KG-RAG
(`buscar_nodos` / `ver_nodo` / `ver_vecinos`) del índice in-memory del
harness a Neo4j Community, con índice full-text Lucene sobre las
descripciones. Referencia: issue #5.

**Estado: NO inyectado.** El pipeline de evaluación sigue usando el
`GraphIndex` in-memory del harness. El adaptador de este directorio queda
listo para inyección futura; el cuarteto hasheado
(`loader.py`/`harness.py`/`judge.py`/`llm_cache.py`) no se tocó — toda la
integración es por módulos nuevos que lo importan.

## Setup reproducible

Requisitos: Docker; el `.venv` del repo con el driver `neo4j` (6.2.0):

```bash
.venv/bin/pip install neo4j
```

1. Levantar Neo4j Community 5.26.9 (GPLv3; sin Aura, sin Enterprise):

```bash
docker run -d --name neo4j-bcra-kg \
  -p 7474:7474 -p 7687:7687 \
  -e NEO4J_AUTH=neo4j/bcra-kg-local \
  neo4j:5.26.9-community
```

   (5.26 es la serie LTS. `bcra-kg-local` es password de desarrollo local,
   configurable por `NEO4J_PASSWORD`; ver `conexion.py`. Sin volumen: la db
   se repuebla entera desde el kg.json en cada carga — el kg.json sellado es
   la única fuente de verdad, el contenedor es descartable.)

2. Cargar el grafo vigente (verifica sha256 sellado antes de cargar; aborta
   si difiere):

```bash
.venv/bin/python data/experiment/neo4j/cargar_kg.py
```

3. Crear el índice full-text y correr los tests de alcanzabilidad:

```bash
.venv/bin/python data/experiment/neo4j/indices.py
```

4. (Opcional) equivalencia contra el in-memory y benchmark:

```bash
.venv/bin/python data/experiment/neo4j/test_equivalencia.py
.venv/bin/python data/experiment/neo4j/benchmark_latencia.py
```

## Módulos

| Archivo | Qué hace |
|---|---|
| `conexion.py` | Driver compartido (env vars + defaults del contenedor local). |
| `cargar_kg.py` | Carga `reensamblado_v3/kg.json` (vía `load_graph_from_path`, adaptador nulo) + verificación de conteos y muestreo campo por campo. |
| `indices.py` | Índice full-text `nodos_fulltext` + tests dirigidos BKL-0003 / BKL-0027. |
| `neo4j_index.py` | `Neo4jIndex`: misma interfaz y formato que `GraphIndex` del harness, contra Neo4j. |
| `test_equivalencia.py` | 30 consultas adaptador vs in-memory (paridad exacta en ver_nodo/ver_vecinos; divergencias documentadas en buscar_nodos). |
| `benchmark_latencia.py` | Latencia con 50 consultas reales de las trazas × 50 reps × 3 backends. |

## Decisiones y su porqué

1. **Adaptador nulo del loader** (`adapter_key=None`): misma convención con
   la que la app registra `reensamblado_v3` — el loader pliega solo la
   `provenance` primaria; la lista acumulada `provenances` del JSON crudo y
   `rol_fuente` no llegan al harness (paridad de interfaz). Neo4j almacena
   exactamente la vista del loader para que la comparación con el
   `GraphIndex` sea 1:1.
2. **Modelo de datos**: label común `:Nodo` (constraint de unicidad de `id`,
   queries globales) + un label por `type` (7 tipos); relationship type =
   `relation` (16 tipos). Properties aplanadas con su nombre original (sin
   colisiones, tipos nativos) para indexación/consulta + `props_json` /
   `provenances_json` como fuente canónica de reconstrucción exacta en
   `ver_nodo`/`ver_vecinos`.
3. **`r.orden`** (posición de la arista en `kg.edges`): reproduce en
   `ver_vecinos` el orden de inserción del in-memory — Neo4j no garantiza
   orden sin `ORDER BY`; sin esto la paridad exacta sería incomprobable.
4. **Índice full-text sobre `label` + `descripcion` + `description`** con
   analyzer `spanish` (stemming + stopwords). El grafo usa AMBAS claves de
   descripción (1.863 `descripcion`, 1.101 `description`): indexar una sola
   dejaría ~25 % del grafo sin cobertura semántica. El analyzer default no
   stemmea ("asociación mutual" no matchearía "asociaciones mutuales").
5. **`nota_fuente` excluida del índice**: 2 nodos, contenido
   meta-editorial sobre la extracción ("descripcion verbatim del inciso…"),
   no contenido normativo; indexarla mete ruido léxico sin ganar
   alcanzabilidad.
6. **Paridad de payload estricta en `buscar_nodos`**: el score de Lucene NO
   se expone; `tokens_matcheados` se calcula con la fórmula del harness
   (helpers importados, no reimplementados). Un hit con `tokens_matcheados=0`
   es señal honesta de que ese nodo era inalcanzable con el índice viejo.
7. **Agregación server-side en `buscar_nodos`**: el conteo total se resuelve
   en Cypher y solo el top-K viaja al cliente. Sin esto la mediana era
   ~12.4 ms (todos los hits + `props_json` al cliente); con esto, ~1.7 ms.

## Resultados (2026-08-06, MacBook local, Docker)

- **E2 carga**: 4.469 nodos / 8.073 aristas exactos; muestreo de 20 nodos
  (seed 20260806) campo por campo: 20/20 ✓.
- **E3 alcanzabilidad**:
  - BKL-0003: "asociación mutual" y 3 variantes → nodo
    `Excepcion_…_5f95b9` en posición 1/10 en todas. Nota: en el grafo
    vigente el label de ese nodo ya fue enriquecido en capa KG
    (recuperación léxica, laudo C6), así que el índice de label+id también
    lo encuentra hoy; la mejora estructural se demostró con fragmentos
    verbatim que viven solo en la `descripcion` ("excepto que se trate de
    asociaciones mutuales…"): full-text pos 1 con 111 matches vs in-memory
    pos 5 entre 3.080 matches (los tokens "que/se/de" matchean sin señal).
    El full-text vuelve innecesario el parche de labels como mecanismo de
    alcanzabilidad.
  - BKL-0027: los 7 `miembro_de` entrantes a
    `Sujeto_rol_sujeto_obligado_proteccion` se recuperan completos con
    query dirigida (`(m)-[:miembro_de]->(rol)`) y bidireccional
    (`(rol)-[:miembro_de]-(m)`), mismo conjunto.
- **E4 equivalencia** (30 consultas): `ver_nodo` 10/10 y `ver_vecinos`
  10/10 idénticos (incluye errores de id inexistente, dirección inválida,
  hub con truncamiento >40). `buscar_nodos`: 10/10 divergen — esperado y
  deseado; detalle en `test_equivalencia_resultados.json`.
- **E5 latencia** (50 consultas reales × 50 reps, ms):

  | backend | N | mediana | p95 |
  |---|---|---|---|
  | in-memory (`GraphIndex`) | 2500 | 0.529 | 1.040 |
  | Neo4j full-text (`Neo4jIndex`) | 2500 | 2.479 | 4.199 |
  | Neo4j label exacto (RANGE) | 2500 | 0.346 | 0.777 |

  Los números de la tabla corresponden a la MISMA corrida que persistió
  `benchmark_resultados.json`. Varianza run-to-run observada: la mediana
  del full-text osciló ~±20 % entre corridas sucesivas (1.7–2.5 ms) —
  los decimales no deben sobre-interpretarse; el orden de magnitud es el
  dato. El overhead del full-text (~2 ms de mediana sobre el in-memory) es
  despreciable frente a la latencia de cada llamada LLM del agente
  (segundos). El baseline por label exacto muestra que el round-trip bolt
  no es el costo dominante.

## Limitaciones conocidas

- El `id` NO está en el índice full-text (el alcance definido fue
  label+descripcion): consultas estilo lookup ("comunicacion a 6312") que
  el in-memory resuelve 1º vía tokens del id pueden rankear más abajo
  (pos 3 en ese caso). Para la inyección conviene evaluar sumar `id` como
  campo del índice o un fallback de lookup exacto.
- El ranking de Lucene (TF-IDF/BM25 con stemming) reordena los top-10
  respecto del conteo de tokens del in-memory: `total_con_match` cambia de
  semántica (hits Lucene vs nodos con ≥1 token). Cualquier comparación de
  métricas de evaluación pre/post inyección debe tener esto presente.
- La db no persiste entre recreaciones del contenedor (decisión: el
  kg.json sellado es la fuente; recargar toma segundos).
- El benchmark corre contra localhost en la misma máquina; latencias de red
  reales serían mayores.
- `neo4j==6.2.0` (driver) quedó instalado en el `.venv` local; no hay
  requirements versionado en este directorio.
