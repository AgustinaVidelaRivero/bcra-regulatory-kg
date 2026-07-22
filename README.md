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

## Estado (julio 2026)

- **Corpus descargado** (Textos Ordenados vigentes e históricos, marco legal,
  Comunicaciones A/B/C/P, complementarios) con scraper idempotente y manifiesto.
- **Fase 2.2:** 5 KGs construidos en paralelo sobre el mismo subset de 5 TOs, cada uno
  con una estrategia de schema distinta (`data/experiment/run_1..run_5`).
- **Fase 2.3 (congelada):** evaluación comparativa de los 5 grafos con harness KG-RAG
  uniforme (agente Haiku + juez LLM v2.1.1 de dos pasos, calibrado contra adjudicación
  humana firmada). Ganador: **run_3 (PPF Core)**. Evidencia completa en el repo.
- **Fases 2.4-2.5 (ciclo 2 cerrado, 19/07/2026):** verificador de calidad del KG +
  capa determinística + segunda pasada con fuentes forzadas. **El instrumento del
  proyecto es v7' = v6.2-D + S1 v0.4b**, validado contra cuatro varas humanas selladas
  (v3, gate CQN, dev-v7, gate CQN2). En el último gate fresco (CQN2, 15 preguntas
  generadas a ciegas y selladas antes de la corrida): las tres columnas comparadas
  dieron 6 aciertos / 1 miss-con-flag / 1 triage sobre las primarias, con **cero misses
  silenciosos** — todo miss salió con flag y todo triage con motivo. Límites
  caracterizados y documentados (fuente: `docs/lectura_ciclo2.md`).
- **En rama (`extraccion-schema-v2`):** pipeline de extracción v2 con catálogo cerrado
  de sujetos (U1-U4e completas; U5 = subset completo, pendiente de OK).

## Mapa del repo

- `data/experiment/` — el laboratorio: `subset/` (5 TOs fuente, read-only),
  `run_1..run_5/` (los 5 KGs congelados), y `evaluacion/` (pipeline de evaluación y
  refinamiento — **ver su `README.md`**, que documenta el núcleo congelado, las zonas
  `runners/`, `tests/` y `analisis/`, y por qué nada del núcleo se mueve ni se edita).
- `docs/` — diseño, especificaciones, lecturas selladas y evidencia de auditoría.
  Punto de entrada: **`docs/INDICE.md`**; arquitectura del repo: `docs/ARQUITECTURA.md`.
- `src/` — librería. Hoy: `src/scraper/` (descargador del corpus y satélites).
  `src/extraction/` y `src/kg/` son los hogares previstos para la extracción escalada
  al corpus completo (pipeline v2, hoy en rama).
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
