# evaluacion/ — pipeline de evaluación y refinamiento (Fases 2.3 → 2.5)

## Por qué los módulos viven en la raíz (leer antes de "ordenar")
`llm_cache.code_version()` hashea `harness.py`, `judge.py` y `loader.py` EN ESTE
DIRECTORIO: mover o editar cualquiera de los cuatro invalida la caché pagada
(`cache/*.db`) y rompe la reproducibilidad. `loader.EVAL_DIR` (= este directorio)
ancla todas las rutas de datos. El resto del núcleo está congelado/sellado por
las lecturas de los ciclos (versiones manuales: v6.1-D, v0.3.1, v0.4b, v5.7).
La raíz ES el src/ de este pipeline. No mover, no editar, ni "solo un import".

**Regla del cuarteto (reafirmada tras el evento de los dos namespaces):** el cuarteto
`loader.py` / `harness.py` / `judge.py` / `llm_cache.py` NO se edita — extensiones para
consumidores nuevos (como la app) van en un módulo aparte que importe al loader, nunca adentro.

**El evento de los dos namespaces:** el commit `2698f6f` (17/07/2026, +58 líneas aditivas
en `loader.py` para la app) rotó `code_version` de `6769297e2d25` a `aa15d9c9b5b7`; los
gates CQN/CQN2 quedaron cacheados bajo el namespace viejo. Ambos namespaces persisten
intactos en `cache/calls.db`; el replay-con-LLM de los gates sigue siendo reproducible vía
checkout del código a la fecha de los gates (mismo hash de fuentes → la caché responde).

## Módulos (raíz — importables, congelados o sellados)
- loader.py — adaptador de los 5 kg.json congelados (Node/Edge, merges run_5). Congelado 2.3.
- harness.py — agente KG-RAG (Haiku, 3 tools, contrato JSON). Congelado 2.3.
- judge.py — juez v2.1.1 dos pasos (Sonnet, ciego al grafo). Congelado 2.3.
- llm_cache.py — caché SQLite + captura del crudo. Namespace = dominio|cv|gfp|think.
- run_frozen.py — pipeline de la corrida congelada 2.3 (evidencia ejecutable).
- test_alcanzabilidad.py — módulo D1 (¡no es un test! quirk de nombre histórico).
- capa_deterministica.py / capa_deterministica_v62.py — capa D v6.1-D (congelada) y v6.2-D (+D7).
- s1_fuentes.py / s1_fuentes_v04.py — S1 v0.3.1 (congelada) y v0.4b. Instrumento del proyecto: v7-v0.4b.
- verificador.py — verificador agéntico v5.7 (espec sellada v57).
- verifier_pilot.py — piloto; vivo como dependencia (load_rep/recover_seen).
- pdf_locate.py — localización de pasajes en los PDFs del subset.

## runners/ (ejecutables vivos; correr desde evaluacion/)
- run_posthoc.py — runner instrumentado con caché (--selftest/--preflight/--verify-replay/--run).
- validate_loader.py — checks C1-C8; reescribe 01_validacion_loader.md (en raíz).
- run_etapa2.py — re-emite frozen_run/reporte_final.md desde la adjudicación firmada.
- reporte_verificador_html.py — HTML por corrida del verificador → posthoc_run/reportes_html/.

## tests/ (+ 2 en raíz)
`python -m pytest tests/ capa_deterministica_test.py test_alcanzabilidad_test.py`
(los 2 de raíz no se mueven: comando normativo en docs/especificacion_capa_deterministica.md).
tests/: test_llm_cache.py (correrlo también como script: `python tests/test_llm_cache.py`),
s1_fuentes_test.py, test_d7_camino_c.py, test_s1v04_fundamento.py.

## analisis/ (experimentos concluidos de 2.3 — históricos, re-ejecutables)
ab_caching.py, ab_control.py, ab_investigate_cq029.py (A/B de caching y control),
adjudicacion_worksheet.py (generó el worksheet), gen_demo_html.py (demo HTML), run_manual.py.

## Zonas de datos (NO SE MUEVEN, NO SE EDITAN)
- queries/ — eval sets sellados (v1, v2, CQN, CQN2 + runtime) e insumos de generación ciega.
- frozen_run/, frozen_smoke/ — evidencia de la corrida congelada 2.3 (selección de run_3).
- trazas/ — trazas históricas del loop manual 2.3.
- posthoc_run/ — trazas post-hoc, gates (gate_cqn/gate_cqn2), head-to-heads, expedientes dev_set/.
- cache/ — calls.db, verificador.db, verifier_pilot.db: crudos pagados. Borrar = re-pagar.
- logs/ — run5_merges.json (log del merge determinístico de run_5).
- Raíz: 00-04_*.md (reportes 2.3), adjudicacion_* (adjudicación humana firmada),
  demo_evaluacion.html, .env (credenciales; EVAL_DIR/.env hardcodeado).
