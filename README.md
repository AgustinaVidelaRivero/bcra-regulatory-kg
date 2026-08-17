# BCRA Regulatory Knowledge Graph

Proyecto Final de Ingeniería en Inteligencia Artificial (UdeSA): diseño, construcción,
evaluación y refinamiento de un Knowledge Graph sobre la regulación del Banco Central
de la República Argentina (BCRA), con trazabilidad documental de cada afirmación y
evaluación bajo custodia (varas humanas selladas antes de cada corrida).

## Pregunta de investigación

¿La organización explícita del corpus regulatorio del BCRA en un Knowledge Graph
mejora la fidelidad y la precisión de citas de un sistema de respuesta regulatoria
(KG-RAG) frente a un RAG tradicional sobre el mismo corpus? En torno a esa pregunta,
el proyecto investiga además qué estrategia de schema produce el mejor grafo, y si un
pipeline de diagnóstico y refinamiento basado en evidencia puede mejorar el grafo
ganador de forma medible.

## Estado (agosto 2026)

Qué es hoy el proyecto: un pipeline que convierte los Textos Ordenados del BCRA en un
Knowledge Graph con provenance por elemento; un agente RAG (Haiku, tres tools:
`buscar_nodos` / `ver_nodo` / `ver_vecinos`) que navega ese grafo; y una evaluación
bajo custodia — sets generados a ciegas y sellados por commit antes de toda corrida,
juez LLM calibrado contra adjudicación humana, atribución determinística de fallas
por replay de trazas. Hallazgo rector: **grounded ≠ correct** — una respuesta anclada
en el grafo puede seguir siendo incorrecta contra la norma.

**Los tres grafos** (nombres canónicos y shas en `docs/nomenclatura_grafos.md`):

| Grafo | Qué es | Path |
|---|---|---|
| **KG-Base** (`12c226e2`) | ganador de la Fase 2.3 entre 5 estrategias de schema (7 entidades / 12 relaciones), baseline congelado | `data/experiment/run_3_ppf_core/kg.json` |
| **KG-Refinado** (`26fac8b4`) | extracción con esquema v2 + re-ensamblado + siete correcciones selladas (C1–C7); **grafo vigente** de la app | `data/experiment/grafo_v2/reensamblado_v3/kg.json` |
| **KG-Reextraído** (`8e2eadee`) | re-extracción desde los PDFs con el pipeline E0–E3 (Enmienda 01), sin heredar C1–C7 | `data/experiment/reextraccion_v2/corpus_v2/salida/kg.json` |

**Resultado central de EV2** (40 preguntas ciegas × 3 grafos, 164 criterios con cita
verbatim, juez validado 11/12 contra adjudicación humana; commit `64de678`, reporte
`data/experiment/ev2_reporte/reporte_ev2.md`):

- Fidelidad (correcto / parcial / incorrecto): KG-Base 3 / 20 / **17**; KG-Refinado
  5 / 26 / 9; KG-Reextraído 4 / 27 / 9.
- Ambos grafos del pipeline refinado reducen los incorrectos casi a la mitad respecto
  del baseline (9 y 9 contra 17); el esquema v2 es el factor común. Entre sí quedan en
  empate técnico, pero fallan distinto: KG-Refinado por navegación con el ancla
  presente, KG-Reextraído por granularidad de ancla.
- La generación es la clase modal de fallas en los tres grafos (17 / 25 / 21 sobre 40):
  grounded ≠ correct cuantificado. Ningún grafo cubre la mitad de los criterios de la
  norma; la brecha literal vs anti-léxica de navegación se confirma en los tres.

Estado detallado y cola de trabajo: `docs/tablero.md`. Mapa de lectura y cadena de
validación: `docs/INDICE.md`.

## Mapa del repo

- `data/experiment/` — el laboratorio: `subset/` (5 TOs fuente, read-only),
  `run_1..run_5/` (los 5 KGs congelados), y `evaluacion/` (pipeline de evaluación y
  refinamiento — **ver su `README.md`**, que documenta el núcleo congelado, las zonas
  `runners/`, `tests/` y `analisis/`, y por qué nada del núcleo se mueve ni se edita).
- `docs/` — diseño, especificaciones, lecturas selladas y evidencia de auditoría.
  Punto de entrada: **`docs/INDICE.md`**; arquitectura del repo: `docs/ARQUITECTURA.md`.
- `src/` — librería. Hoy: `src/scraper/` (descargador del corpus y satélites).
  `src/extraction/` y `src/kg/` son los hogares previstos para la extracción escalada
  al corpus completo (el pipeline v2 vive hoy en `data/experiment/reextraccion_v2/`).
- `scripts/` — `shapes_validator.py` (validador determinístico de shapes sobre los
  kg.json; su reporte vive en `reports/`) y `adhoc/` (históricos).
- `app/` — frente de consulta (consume el grafo vía el loader, sin tocarlo).
- `reports/`, `notebooks/` — reportes generados y exploración.

## Cómo reproducir

Desde `data/experiment/evaluacion/` (ver su README para el detalle):

```bash
python -m pytest tests/ capa_deterministica_test.py test_alcanzabilidad_test.py
```

```bash
python runners/run_posthoc.py --selftest        # cadena agente+juez+caché, offline
```

```bash
python runners/validate_loader.py               # integridad de los 5 grafos (C1-C8)
```

```bash
python runners/run_etapa2.py                    # re-emite el reporte final del frozen
```

Descarga del corpus (idempotente, subcomandos B1..B9):

```bash
python src/scraper/download_bcra.py B1
```

## Convenciones del repo

- **Evidencia y auditoría:** toda corrida que sustenta una conclusión queda congelada
  en el repo (trazas, crudos de API en caché SQLite, reportes); los documentos de
  lectura citan rutas y números de parseo real, nunca estimaciones.
- **Zonas congeladas:** los 5 `kg.json`, el harness/juez/loader de la Fase 2.3 y los
  módulos sellados del instrumento no se editan (el detalle, en
  `data/experiment/evaluacion/README.md`). Las varas se commitean ANTES de cada
  corrida (sellado por inexistencia).
- **Setup:** Python 3.11+, `python3 -m venv .venv && pip install -r requirements.txt`,
  credenciales de API en `data/experiment/evaluacion/.env` (no versionado).

## Autora

Agustina Videla Rivero — Ingeniería en Inteligencia Artificial, UdeSA.
