# ev2_encadenamiento — encadenamiento §7 del protocolo EV2

Ejecuta lo que la corrida base de fidelidad dispara según
`docs/protocolo_corrida_ev2.md` §3 y `docs/preregistro_evaluacion_fidelidad_ev2.md`
§7 (ambos sellados por commit): re-corrida **N=3 del agente** sobre cada par
(pregunta, grafo) con veredicto base **"parcial"** (trigger mecánico único) y
**auditoría simétrica** N=3 sobre una muestra del 10 % de los "correcto" por
grafo (semilla `auditoria-ev2-v1`; con 3/4/2 correctos el 10 % redondea a cero
→ laudo: mínimo 1 por grafo, ceil), y evaluación de las respuestas nuevas con
el **mismo juez congelado y el mismo pipeline ciego** de la base.

Población (derivada de `ev2_fidelidad_eval/out/` + `desanonimizacion/`):
parciales v2 23 / v3 22 / run_3 18 = 63; auditoría 1 + 1 + 1 = 3 → **66 pares
× 3 = 198 corridas de agente; × 3 reps del juez = 594 llamadas.**

## Reglas de agregación (protocolo §3, en código con tests)

- Por par: mayoría de las 3 re-corridas juzgadas; empate triple
  correcto/parcial/incorrecto → parcial (mediana categórica). La corrida base
  es disparador: no vota.
- Voto `requiere_adjudicacion` (mapping §2 del juez, no contemplado en §3):
  el par queda decidido solo si el resultado es invariante a la adjudicación
  pendiente; si no, `requiere_adjudicacion`. **Regla declarada por esta unidad,
  sujeta a laudo de la mesa** (`code/agregacion_enc.py`, tests 32/32).
- Auditoría: tasa de flip descendente = agregado de las 3 ∈ {parcial,
  incorrecto} sobre base correcto; se reporta también por re-corrida individual.

## Anti-cache (protocolo §4, patrón rt_c6_n3)

- Agente: label `ev2_enc_<grafo>_r{n}` y db `cache/ev2_enc_<grafo>_r{n}.db` por
  (grafo, rep). El primer turno de una pregunta es idéntico en toda repetición:
  compartir db replayaría la conversación desde caché; por eso db propia y
  exigencia de **0 hits** en el access_log de cada db.
- Juez: label `ev2_enc_juez_r{n}` y db `cache/ev2_enc_juez_r{n}.db` por rep
  (namespace por rep → keys disjuntas → 0 cross-hits). Dos re-corridas de un
  mismo par pueden dar texto idéntico: el request al juez es idéntico → hit
  intra-db por never-pay-twice; se declara el número esperado y se compara.

## Ceguera

Esta unidad conoce el grafo de cada par (inevitable). El juez NO: cada
respuesta nueva recibe id opaco `EV2E-` + sha256(`juez-ev2-enc-v1|id_pregunta|
grafo|rep|sha256(respuesta)`)[:10]; su input es exactamente prompt +
(pregunta, respuesta, criterios) (`juez_enc.verificar_ceguera_requests` aborta
ante cualquier marcador). Tabla id → (id_pregunta, grafo, rep) en
`desanonimizacion_SOLO_MESA/`; salidas del juez en `juez_out/` (ciegas);
reporte final en `reporte/` por id opaco de par (`EV2R-` de la base). El
cruce por grafo lo hace la mesa.

## Archivos

- `code/comun_enc.py` — sellos (instrumento, cuarteto, grafos, insumos base),
  población, orden, ids opacos, vista ciega, tabla SOLO_MESA, vínculo de pares.
- `code/poblacion_enc.py` → `poblacion/`, `orden/`, `sellos/sellos_inicio_faseA.txt`.
- `code/runner_enc.py` — re-corridas del agente envolviendo `runner_ev2.correr_grafo`
  (fase B: `--autorizado-fase-b --tope-agente`; `--solo-resumen` offline) →
  `trazas/ev2_enc_*`, `reporte/{resumen,indice_trazas}_agente.json`.
- `code/juez_enc.py` — juez ciego envolviendo `pipeline_fidelidad` (fase B:
  `--autorizado-fase-b --precio-in --precio-out --tope-juez`; `--solo-agregados`
  offline) → `juez_out/`, `juez_orden/`, `desanonimizacion_SOLO_MESA/`,
  `reporte/{reporte_final_ciego.md, veredictos_finales_ciego.json}`.
- `code/agregacion_enc.py` + `code/tests_agregacion.py` — regla por par y tests.
- `code/selftest_enc.py` — selftest offline (67 checks) → `selftest_out/`.
- `code/estimacion_enc.py` → `estimacion/` (tokens medidos, sin precios).
- `checkpoint_sesion.md` — estado de la unidad.

Nada de `ev2_corrida/`, `ev2_fidelidad_eval/`, `ev2_juez/` ni del cuarteto se
edita: sha verificados al inicio y al fin de cada etapa (`sellos/`).

## Reproducción offline (USD 0)

```
.venv/bin/python -B data/experiment/ev2_encadenamiento/code/poblacion_enc.py
.venv/bin/python -B data/experiment/ev2_encadenamiento/code/tests_agregacion.py
.venv/bin/python -B data/experiment/ev2_encadenamiento/code/selftest_enc.py
.venv/bin/python -B data/experiment/ev2_encadenamiento/code/estimacion_enc.py
```
