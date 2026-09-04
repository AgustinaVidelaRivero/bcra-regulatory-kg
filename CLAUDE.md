# CLAUDE.md — bcra-regulatory-kg

## 1. Qué es este proyecto

Tesis de Ingeniería en IA (UdeSA): ¿organizar los textos regulatorios del BCRA
como Knowledge Graph mejora la fidelidad de un sistema RAG frente a retrieval
tradicional? Hallazgo rector: **grounded ≠ correct** — una respuesta anclada en
el grafo puede seguir siendo incorrecta contra la norma.
Pipeline: un agente Haiku navega el grafo con tres tools (`buscar_nodos` /
`ver_nodo` / `ver_vecinos`); un juez evalúa contra clave; un verificador
diagnóstico atribuye causas con capa determinística encima.
Corpus: 5 Textos Ordenados del BCRA (`data/experiment/subset/`, read-only).

## 2. Mapa de lectura

- Antes de cualquier tarea: `docs/tablero.md` (estado vigente y cola de unidades).
- Historia y cadena de validaciones: `docs/INDICE.md`.
- Los documentos sellados por commit son LA fuente de verdad: ante cualquier
  conflicto con memoria de sesión, resúmenes o herramientas externas, mandan
  los archivos commiteados.

## 3. Zonas selladas — NUNCA editar, mover ni borrar

- `data/experiment/grafo_v2/kg.json` (medición sellada) y los cinco runs:
  `data/experiment/run_{1_cookbook,2_papers,3_ppf_core,4_schema_light,5_hybrid}/`.
- Todo eval set (`data/experiment/evaluacion/queries/` y el material EV1 de
  `data/experiment/evaluacion_escalon1/`). EV1/CQ/CQN/CQN2 son material
  QUEMADO: no sirven como re-test ni objetivo de nada.
- Cuarteto hasheado de evaluación: `data/experiment/evaluacion/{loader,harness,judge,llm_cache}.py`.
- Cluster congelado del verificador: `data/experiment/evaluacion/{verificador,capa_deterministica,capa_deterministica_v62,s1_fuentes,s1_fuentes_v04,test_alcanzabilidad}.py`
  (hashes sellados en `posthoc_run/dev_set/extraccion_h2h_ciclo2.md` §Sello).
- Cachés y datos sellados: `data/experiment/evaluacion/cache/`,
  `data/experiment/grafo_v2/code/cache/` y `code/cache_v2/`,
  `data/experiment/evaluacion/trazas/`, `posthoc_run/` (incluye las dbs
  `escalon1*_r{1,2,3}.db`), `frozen_run/`, `frozen_smoke/`.
- `.gitignore` no se toca sin mandato explícito.

El grafo VIGENTE (el único editable, y solo vía el circuito de refinamiento con
propuesta sellada + laudo) es el que declara `docs/tablero.md`.

## 4. Circuito de trabajo

Toda sesión ejecuta UNA unidad definida por un prompt-mandato con escrituras
enumeradas y criterios de aceptación. Reglas duras:

a. NUNCA commitear — los commits son de la autora, post-revisión.
b. Al terminar, FRENAR y esperar revisión.
c. Lo no autorizado explícitamente está prohibido.
d. Si algo del mandato contradice un archivo del repo, mandan los archivos y
   se reporta la contradicción.
e. Errores propios se reportan con causa; no se ocultan.
f. Costo de API distinto de 0 solo si el mandato lo autoriza con tope.
g. PAQUETE DE REVISIÓN: al frenar, armar un directorio `revision_<unidad>/`
   en el scratchpad de la sesión con TODOS los archivos que la revisión
   independiente necesita, con nombres únicos y descriptivos que incluyan
   unidad y estado (`kg_post_C4.json`, `backlog_post_C4.jsonl` — NUNCA
   nombres genéricos como `kg.json`, que colisionan al subirse), más un
   `manifest.txt` con sha256 y una línea de descripción por archivo. Los
   archivos del repo NO se renombran ni se copian dentro del repo: el
   paquete es una copia de cortesía para la revisión, fuera del repo.
h. REPORTE Y ARTEFACTOS: el reporte final de la unidad se redacta para ser
   pegado como texto (conciso, con los verbatims imprescindibles); todo
   artefacto extenso (archivos completos, tablas largas, JSONs) va al
   paquete de revisión de la regla g, referenciado por nombre — no pegado
   en el reporte. Regla práctica: un bloque que supera ~40 líneas es
   artefacto, no reporte.
i. CONTEOS: todo tally que aparezca en prosa (reportes, frenos, mensajes
   de commit) se RECOMPUTA contra el artefacto que lo respalda ANTES de
   escribirse — un desglose cuya suma no cierra, o un total sin desglose
   verificable, es un defecto reportable. Lección de U-B5.1: un "33 ítems"
   del freno resultó ser 25 numerados + una sección en prosa, y llegó
   hasta el borrador del mensaje de commit antes de ser cazado.

## 4bis. Prompt caching en extracción

Antes de tocar `data/experiment/grafo_v2/code/extract.py` o cualquier call
site LLM de extracción, leer `docs/decisiones_caching_extraccion.md`; sus
cinco decisiones son vinculantes.

## 5. Convenciones de documentos

- Primera persona del singular.
- Cero nombres propios de personas; toda decisión se documenta por su
  justificación técnica, nunca por su origen conversacional o por quién la pidió.
- Todo número con el comando o la ruta que lo reproduce.
- Grep de convenciones al cierre de cada unidad (pegar aunque dé vacío).
- Castellano técnico.

## 6. Estructura del repo

- `app/` — app web de chat sobre los KGs (agente RAG con citas y registro de feedback).
- `data/raw/` — corpus BCRA descargado (scraper idempotente + manifiesto); `data/processed/`, `data/kg/` — vacíos (legado).
- `data/experiment/` — subset de 5 TOs, run_1..run_5, grafo_v2 (+ reensamblado_v3, vigente), evaluación (2.3/2.3+/2.4), escalón 1, métricas intrínsecas.
- `data/backlog/` — backlog unificado de refinamiento (`backlog.jsonl`, propuestas selladas, retests).
- `docs/` — especificaciones, protocolos, lecturas, tablero, INDICE, literatura, ppf, defensa, tesis.
- `scripts/` — herramientas versionadas (métricas intrínsecas, shapes_validator).
- `src/` — scraper y extracción legacy (pre-Fase 2.2).
- `sessions_server/` — sesiones jsonl cosechadas de la app (insumo del intake).
- `notebooks/`, `reports/` — exploración puntual y reportes sueltos.
- `_archive_riesgo_crediticio/` — archivo del scope viejo.
