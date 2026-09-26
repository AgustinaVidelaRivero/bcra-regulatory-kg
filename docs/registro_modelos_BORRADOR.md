# Registro de modelos por medición sellada — BORRADOR de la mesa (25/09/2026)

Estado: BORRADOR, pendiente de aprobación de la autora; destino previsto
`docs/registro_modelos.md` (fila de C1.9 del plan). Regla: el «id según la API»
se toma únicamente de la traza que lo guardó; donde no esté, la celda dice
NO ENCONTRADO con el archivo sondeado. «Id en el código» es la constante del
runner, con archivo y línea. Vía: API directa salvo indicación. Temperatura:
la fijada en el código; «sin fijar» = ninguna línea `temperature` en el cliente
(rige el default del proveedor).

| Medición sellada | Componente | Id en el código (archivo:línea) | Id según la API (traza sondeada) | Temperatura | Vía |
|---|---|---|---|---|---|
| Fase 2.3, cinco estrategias de esquema (frozen_run) | agente | `evaluacion/harness.py:47` `claude-haiku-4-5-20251001` | NO ENCONTRADO en `evaluacion/frozen_run/agg_run_1.json` (lista sin campo de modelo); trazas individuales no sondeadas | 0 (`harness.py:48`) | API |
| Fase 2.3 | juez v2.1.1 (dos pasos) | `evaluacion/judge.py:87` `claude-sonnet-4-6` | NO ENCONTRADO (no sondeado) | 0 (`judge.py:88`) | API |
| Extracción grafo_v2 (gen. 2) | extractor | `grafo_v2/code/extract.py:57` `claude-haiku-4-5-20251001` | NO ENCONTRADO (no sondeado) | sin fijar (`extract.py` sin `temperature`) | API |
| Re-extracción v2, corpus de desarrollo (E1) | extractor E1 | `corpus_v2/runner_corpus.py:89` `claude-haiku-4-5` (sin fecha) | NO ENCONTRADO en `corpus_v2/salida/cap/resumen_e1.json` (`cliente`: llamadas y costos, sin modelo) | sin fijar (`cliente_e1.py`, `comun_e1.py`, `runner_corpus.py` sin `temperature`) | API |
| Re-extracción v2, corpus de desarrollo (E3) | verificador E3 | `corpus_v2/runner_corpus.py:92` `claude-sonnet-5` (sin fecha) | NO ENCONTRADO en `corpus_v2/salida/cap/resumen_e3.json` (`cliente_e3` sin modelo) | no sondeado en el cliente de E3 | API |
| ESQ-1 / ESQ-2 / controles (dopadas, descubrimiento) | extractor E1 y modo descubrir | `esq/code/comun_control_esq.py:85`, `comun_cobertura_esq2.py:86`, `descubrimiento_cal.py:46` `claude-haiku-4-5` | NO ENCONTRADO en `esq/control/dopadas_p1bis.json` (sin campo de modelo); resúmenes de corrida no sondeados | sin fijar (`comun_control_esq.py` sin `temperature`) | API |
| EV2 corrida base (3 grafos, 456 trazas) | agente | `harness.py:47` `claude-haiku-4-5-20251001` | `claude-haiku-4-5-20251001` en `ev2_corrida/trazas/ev2_base_run3/EV2F-001.json` (`meta.model` y `raw_turns_agent[].raw.model`) | 0 | API |
| EV2 re-corridas §7 (encadenamiento) | agente | ídem | no sondeado (mismo runner; verificar sobre `ev2_encadenamiento/trazas/`) | 0 | API |
| EV2 sobre r1 (base + 3 re-corridas) | agente | ídem | `claude-haiku-4-5-20251001` en `ev2_r1/trazas/ev2_r1_base/EV2F-001.json` (`meta.model`) | 0 | API |
| EV2 (todas) | juez de fidelidad v1 (prompt `fd446f8e…`) | `ev2_juez/juez.py:37` `claude-sonnet-4-6` (sin fecha) | NO ENCONTRADO en `ev2_juez/out/acuerdo_juez_humana.json` (agregado sin modelo); caché de llamadas no sondeada | 0.0 (`juez.py:38`) | API |
| A1.4 ablación de retrieval (400 trazas) | agente | `harness.py:47` (mismo harness) | NO ENCONTRADO en `ablacion_retrieval/corrida/resultados/analisis_ablacion.json` (agregado); trazas por celda no sondeadas | 0 | API |
| A2.0 gate y banco MCP | agente Claude Code | `banco_mcp/gate/code/faseB_runner.py:38` `claude-sonnet-5` (declarado en la pre-declaración de fase B) | NO ENCONTRADO en `banco_mcp/gate/sesiones/manifiesto_captura.json`; el plan registra que el banco guarda inventario de modelos por traza (R8) — verificar en las sesiones | no aplica (harness de Claude Code) | Claude Code `claude -p`; CLI 2.1.196 (gate) y 2.1.241 (banco), según A2.0-banco |
| Verificador diagnóstico (Motor 3) | verificador / mapeo | `evaluacion/verificador.py:55` `claude-opus-4-8`; `verifier_pilot.py:38-40` (`claude-haiku-4-5-20251001`, `claude-opus-4-8`, `claude-sonnet-4-6`) | NO ENCONTRADO (no sondeado) | «rechaza temperatura» según comentario de `verificador.py:55` — verificar | API |
| U-EV2-TIPO control de clasificación | modelo de control | `scripts/ev2_tipo_control.py:32` `claude-sonnet-4-6` | `claude-sonnet-4-6` en `exploracion/ev2_fidelidad/tipo_pregunta_control.json` (`modelo_segun_api`) | 0.0 | API |
| U-EV2-TIPO-V2b control bajo la regla v2 (`b6e5b4d`, 26/09/2026) | modelo de control | `scripts/ev2_tipo_control_v2.py` (importa `MODELO` de `ev2_tipo_control.py:32`) `claude-sonnet-4-6` | `claude-sonnet-4-6` en las 40 llamadas, `exploracion/ev2_fidelidad/control_v2_2026-09-26/tipo_pregunta_control_v2.json` (`modelo_segun_api`; también `stop_reason` y `captura`) | 0.0 (campo `temperatura`; `thinking` false) | API directa (SDK anthropic 0.100.0, Python 3.10.13 del `.venv`, según el reporte de la ejecutora; NO VERIFICADO contra artefacto). Costo USD 0,3981 en el JSON (`costo_usd_calculado`), 113.676 / 3.805 tokens |
| B5.4 catálogo v3 (pareada), U-COB-A (A.2) | extractor E1 | `b54_catalogo_v3/code/runner_pareada_b54.py:52`, `cobertura_bloque_a/code/correr_a2.py:44` `claude-haiku-4-5` | no sondeado | sin fijar (a verificar en sus clientes) | API |

## Hallazgos para el documento final

1. Los ids del código son mixtos: con fecha (`claude-haiku-4-5-20251001`) en el
   harness y en el extractor de la generación 2; sin fecha (`claude-haiku-4-5`,
   `claude-sonnet-5`, `claude-sonnet-4-6`, `claude-opus-4-8`) en E1, E3, los dos
   jueces, el verificador y el banco. Un id sin fecha no fija por sí solo la
   versión: el registro debe apoyarse en el id devuelto por la API por traza.
2. Solo las trazas de EV2 (base y r1) y el control de U-EV2-TIPO guardan hoy el
   id devuelto por la API. El resto queda NO ENCONTRADO hasta un sondeo por
   traza, que es una unidad de solo lectura (I, $0).
3. E1 corrió sin temperatura fijada en todas sus campañas (cliente sin
   `temperature`); el harness y los dos jueces corrieron a 0.
4. Vía: todo por API directa salvo A2.0 gate y banco (Claude Code, `claude -p`,
   versiones de CLI registradas en el plan).

Todo lo marcado «no sondeado» es verificable con un recorrido por traza;
ninguna celda de este borrador afirma más de lo que el archivo citado contiene.
