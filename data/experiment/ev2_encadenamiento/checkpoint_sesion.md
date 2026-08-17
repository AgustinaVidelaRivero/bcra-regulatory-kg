# checkpoint_sesion — encadenamiento §7 EV2 (re-corridas N=3 + auditoría + juez ciego)

## Fase A (offline, USD 0) — HECHA, esperando revisión (2026-08-16)

- Branch `main`; nada fuera de `data/experiment/ev2_encadenamiento/`; cero commits.
- Contradicción reportada: el mandato dice "corrida base commiteada" pero
  `data/experiment/ev2_fidelidad_eval/` está SIN commitear (`??` en git status);
  se usaron sus archivos en disco, sellados por sha en `sellos/sellos_inicio_faseA.txt`
  (agregados `9f1046c6…`, tabla `e219b2fb…`).
- Sellos verificados: prompt v1 `fd446f8e61f4…`, juez.py `b4a74ba5…`, mapping.py
  `c905dd1a…`, cuarteto 4/4, grafos 3/3, gold `1d587336…`.
- Población: 63 parciales (v2 23 / v3 22 / run_3 18) + auditoría 3 (v2 EV2F-035,
  v3 EV2F-033, run_3 EV2F-035; semilla auditoria-ev2-v1, 1 por grafo por laudo)
  = 66 pares → 198 corridas de agente → 594 llamadas al juez.
- Regla declarada (sujeta a laudo): voto `requiere_adjudicacion` en la mayoría
  por par → decidido solo si invariante; si no, `requiere_adjudicacion`.
- Selftest 67/67 PASS; tests_agregacion 32/32; tests_mapping 20/20.
- Estimación (sin precios) en `estimacion/estimacion_fase_b.{json,md}`.
- Nada llamado a la API. `cache/` no existe. `trazas/`, `juez_out/` no existen.

## Fase B — PENDIENTE de autorización explícita (dos etapas, topes propios)

1. Agente: `runner_enc.py --autorizado-fase-b --tope-agente <USD> [--precio-in
   --precio-out --precio-cw --precio-cr]` (retomable; freno por proyección).
   Al terminar: incompletas = 0 o detalle y FRENO antes del juez.
2. Juez: `juez_enc.py --autorizado-fase-b --precio-in <in> --precio-out <out>
   --tope-juez <USD>` (retomable; `--solo-agregados` recomputa). Al terminar:
   gasto desde dbs, 0 cross-hits, distribución, flips de auditoría, veredictos
   finales ciegos. NO cruzar por grafo. FRENAR.

## Reglas vivas

Cero commits; nada fuera de la unidad; cuarteto + juez + mapping + base
intocables; nombres jamás.

## Fase B — AUTORIZADA (2026-08-16); base commiteada en b624865
- Laudos: regla de agregación por invariancia RATIFICADA; auditoría mínimo 1 por grafo RATIFICADA.
- Etapa AGENTE lanzada: runner_enc.py --autorizado-fase-b --tope-agente 9.00
  --precio-in 1.00 --precio-out 5.00 --precio-cw 1.25 --precio-cr 0.10 (log reporte/log_fase_b_agente.txt).
  Retomable: re-lanzar el mismo comando. Si incompletas > 0: FRENO antes del juez.
- Etapa JUEZ (solo si agente 198/198 sin incompletas): juez_enc.py --autorizado-fase-b
  --precio-in 3.00 --precio-out 15.00 --tope-juez 12.00 (log reporte/log_fase_b_juez.txt).
- Etapa AGENTE TERMINADA: 198/198 trazas, 0 incompletas, 0 hits en 9 dbs, USD 6,4732 desde dbs
  (harness 6,4731; estimación 6,44), sellos inicio==fin. 16 grupos de textos duplicados por pregunta
  (20 respuestas extra → 60 hits intra-db esperados en el juez); 20 respuestas idénticas a la base.
- Etapa JUEZ LANZADA: juez_enc.py --autorizado-fase-b --precio-in 3.00 --precio-out 15.00 --tope-juez 12.00
  (log reporte/log_fase_b_juez.txt). Retomable con el mismo comando; --solo-agregados recomputa.
- Etapa JUEZ TERMINADA (2026-08-16): 594/594 llamadas (534 pagadas + 60 hits intra-db == esperados por
  duplicados), 0 errores, 0 incompletas, sin freno; gasto USD 6,7441 desde dbs (tope 12,00; estimación
  central 7,32); 0 cross-hits (keys disjuntas); sellos inicio A == fin B juez.
- Por respuesta (198, ciego): parcial 148 / correcto 12 / incorrecto 14 / requiere_adjudicacion 24.
- Por PAR (66): disparados 63 → parcial 49 / incorrecto 4 / requiere_adjudicacion 9 / correcto 1;
  auditoría 3 → correcto 2 / parcial 1 (flip 1/3, todos unánimes).
- Salidas: juez_out/ (ciego), reporte/{reporte_final_ciego.md, veredictos_finales_ciego.json,
  resumen_agente.json, indice_trazas_agente.json, logs}, desanonimizacion_SOLO_MESA/. El cruce por
  grafo NO se computó: lo hace la mesa. Cero commits. FRENADA, esperando revisión.
