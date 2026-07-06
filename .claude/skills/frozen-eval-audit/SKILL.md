---
name: frozen-eval-audit
description: Audita y reproduce (determinísticamente, sin API) la evaluación congelada de la Fase 2.3 que seleccionó a run_3 — regeneración de checkpoints y reportes desde los datos persistidos, validación de integridad de los 5 kg.json, y trazabilidad dato crudo → agregado → reporte de cualquier veredicto. Usala SIEMPRE que aparezca: "verificá/auditá los resultados del frozen", "regenerá el checkpoint/el reporte final", "¿de dónde sale el veredicto de CQ-X para run_Y?", "reproducí la evaluación congelada", "¿los kg.json siguen intactos?", "defendé la selección del ganador ante mentores". TAMBIÉN disparala si piden "re-corré el frozen" o "re-corré la comparación de los 5 grafos": la respuesta correcta de esta skill es NEGARSE y explicar por qué (re-correr no reproduce — genera datos nuevos, paga todo de nuevo y requiere orden explícita de la autora). Reproducir = regenerar desde lo persistido, nunca re-ejecutar el modelo.
---

# Auditoría de la evaluación congelada (Fase 2.3)

La selección de `run_3` como ganador está **congelada** y tiene que ser defendible:
todo reporte debe poder regenerarse desde los datos persistidos, y todo veredicto
debe poder rastrearse hasta su traza. Esta skill hace eso — y define qué significa
"reproducir" para que nadie lo confunda con "re-correr".

## La guarda anti-re-corrida (comportamiento central)

**`python run_frozen.py --mode graph` NO se ejecuta sin orden explícita de la
autora.** Si el pedido es "re-corré el frozen", negarse y explicar estas cuatro
razones (todas verificadas):

1. El propio pipeline lo prohíbe: "NO ejecutar sobre el eval_set hasta orden
   explícita" (`data/experiment/evaluacion/run_frozen.py:29-30`).
2. **No reproduce nada**: el sistema tiene no-determinismo run-to-run documentado
   (commit `7e8b91e`: divergencias off-vs-off atribuidas a no-determinismo vía
   control off-vs-off2). Una re-corrida produce datos NUEVOS, no confirma los
   existentes.
3. **Paga todo de nuevo**: `run_frozen.py` no usa la caché SQLite de `llm_cache.py`
   (es anterior; su "caching ON" es prompt-caching de la API). Cada `--mode graph`
   re-paga 23 preguntas × N=3 × agente+juez de ese grafo.
4. Contaminaría el dataset: los agregados congelados en `frozen_run/` son la base
   de la selección; datos nuevos mezclados ahí romperían la trazabilidad.

Lo mismo aplica a `--mode smoke` (gasta API; solo con orden explícita).

**La distinción que gobierna todo** (ruling 2026-06-10,
`data/experiment/evaluacion/run_frozen.py:33-45`): la **capa de reporting**
(checkpoints, reportes) es instrumentación de lectura y puede regenerarse o
corregirse con registro; el **sistema bajo evaluación** (harness, juez, eval_set,
trazas, agregados) no se toca bajo ninguna circunstancia.

## Qué SÍ es reproducible (determinístico, sin API, gratis)

Desde `data/experiment/evaluacion/`, con el venv de la raíz:

```bash
# Checkpoint de un grafo, desde su agregado persistido:
python run_frozen.py --mode regen --graph run_X     # run_frozen.py:833-847

# Reporte etapa 1 (draft, con pendientes retenidos), desde aggs + cola:
python run_frozen.py --mode report                  # run_frozen.py:849-851

# Reporte etapa 2 (final), desde la adjudicación humana firmada:
python run_etapa2.py                                # run_etapa2.py:41 → reporte_final.md

# Integridad de los 5 kg.json + loader (checks C1–C8, exit 0/1):
python validate_loader.py                           # validate_loader.py:12-21
```

**⚠ Los tres primeros escriben EN EL LUGAR** (`checkpoint_run_X.md`,
`reporte_final_draft.md`, `reporte_final.md` dentro de `frozen_run/`;
`validate_loader` escribe `01_validacion_loader.md`). Eso habilita el chequeo de
reproducibilidad: regenerar y correr `git diff` sobre el archivo — **diff vacío =
el reporte es re-derivable byte a byte de los datos persistidos** (la afirmación
que se defiende ante mentores). Si el diff NO es vacío, no pisar nada más:
reportar la diferencia a la autora (restaurar o no es decisión de ella).

## Trazabilidad: dato crudo → agregado → reporte

La cadena completa, con la estructura de cada eslabón parseada, está en
`references/artefactos.md`. El esqueleto:

```
frozen_run/traces/run_X/CQ-YYY.json   (3 reps: respuesta, citas, verdict, costos)
  → frozen_run/agg_run_X.json         (23 celdas: modal/unánime/distribución por dimensión)
    → frozen_run/checkpoint_run_X.md  (revisión por grafo)
    → frozen_run/reporte_final_draft.md            (etapa 1: multi_norma retenida)
      + adjudicacion_pendiente.json → adjudicacion_FIRMADO.json   (humano, firmado)
        → frozen_run/reporte_final.md              (etapa 2: correctitud resuelta)
```

Para auditar UN veredicto puntual (qid × run × dimensión), el walkthrough de 4
pasos está en `references/artefactos.md` — de la distribución de reps al reporte,
pasando por la cola de adjudicación si la celda estuvo retenida.

**Limitación conocida (documentada, no un hallazgo nuevo):** las trazas congeladas
NO tienen los steps de tool calls — la trayectoria por repetición es irrecuperable
por decisión registrada (`data/experiment/evaluacion/run_frozen.py:46-58`). Las
trayectorias están en la capa post-hoc (`posthoc_run/traces/{off,on}/`), que es
ILUSTRATIVA y está fuera del dataset congelado.

## Non-goals

- **NO re-ejecuta el modelo** (`--mode graph`/`--mode smoke`) sin orden explícita
  de la autora — es el comportamiento central de arriba, no una omisión.
- **NO re-adjudica ni edita** `adjudicacion_FIRMADO.json` (firmado por la autora)
  ni la cola `adjudicacion_pendiente.json`.
- **NO edita trazas ni agregados** de `frozen_run/` — sistema bajo evaluación.
- **NO reabre la selección del ganador** (congelada; tampoco la reabre el mapa de
  defectos del verificador — hallazgo abierto es de los mentores, no de esta skill).
- **NO toca los `kg.json`** — los 5 siguen congelados (el refinamiento trabaja
  sobre la copia, skill `kg-refinement`).
- **NO commits** — los maneja la autora.

## Self-check (ejecutable, sin API)

```bash
cd data/experiment/evaluacion
python validate_loader.py     # C1–C8 × 5 grafos; exit 0 y "TODOS PASAN"
```

Verifica que los 5 `kg.json` congelados cargan intactos con los conteos esperados
(`data/experiment/evaluacion/validate_loader.py:179-201`). Para verificar además
la reproducibilidad de la capa de reporting: regenerar un artefacto (`--mode regen
--graph run_1`) y confirmar `git diff` vacío sobre él, como se describe arriba.
