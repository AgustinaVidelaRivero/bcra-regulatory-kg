# Lectura del escalón 1b — PARTE MECÁNICA + declaración de válvula (2026-07-31)

Rige el pre-registro: mapeo sellado `mapeo_delta_v2v3.md` (commit `6c24009`,
§C y §D) y `docs/protocolo_escalon1b.md` §6. Esta unidad cruza resultados
contra ramas, arma la evidencia y DECLARA la válvula. **No contiene conclusión
causal alguna**; la única prosa causal admitida es la transcripción de
predicciones ya selladas donde el caso las confirma.

Insumos (sellados en `fe4cfa9` y `6c24009`): `resultados_1b_FINALES_2026-07-31.json`,
`adjudicacion_humana_1b.json`, `queries_v3_2026-07-30.json`, trazas
`escalon1b_r{1,2,3}`, el mapeo, las 9 fichas. Desvío menor de precondición,
registrado: 9 archivos `summary_escalon1b_*.json` de la corrida quedaron sin
commitear en `posthoc_run/` (whitelisteados por gitignore); no son insumo de
esta unidad. Scripts de esta unidad en el scratchpad de sesión
(`lectura_mecanica_1b.py`); réplica del índice v3 con el `GraphIndex` real.

## A. Cruce contra el pre-registro

### A.1 Global

| Métrica | Valor | Pre-registro | Declaración |
|---|---|---|---|
| v3 final | **29/36** | banda dura [19, 30] | **DENTRO** |
| v3 final | 29/36 | rama central 28–29 (techo 30) | **DENTRO** |

(v2 = 27/36 reproducido exacto; run_3 = 31/36 como referencia descriptiva con
su caveat del protocolo §6.)

### A.2 Las 9 fichas — predicción sellada vs resultado final

| Ficha | Predicción sellada (§C) | Resultado final v3 | Declaración |
|---|---|---|---|
| EV1-005 | sin_cambio_esperado | sin cambio (3-0 incorrecta) | DENTRO_DE_RAMA |
| EV1-011 | sin_cambio_esperado | sin cambio (3-0 incorrecta) | DENTRO_DE_RAMA |
| EV1-015 | sin_cambio_esperado | sin cambio (3-0 incorrecta, por laudo) | DENTRO_DE_RAMA |
| EV1-018 | mejora_posible_no_garantizada | no convirtió (3-0 incorrecta, por laudo) | DENTRO_DE_RAMA |
| EV1-028 | sin_cambio_esperado | sin cambio (3-0 incorrecta) | DENTRO_DE_RAMA |
| **EV1-029** | sin_cambio_esperado | **CONVIRTIÓ** (2-1 correcta) | **FUERA_DE_RAMA** |
| EV1-031 | acierto_nuevo_esperado | convirtió (3-0 correcta) | DENTRO_DE_RAMA |
| EV1-039 | sin_cambio_esperado | sin cambio (3-0 incorrecta) | DENTRO_DE_RAMA |
| EV1-042 | acierto_nuevo_esperado | convirtió (3-0 correcta) | DENTRO_DE_RAMA |

**Verificación mecánica de las dos predicciones convertidas** (¿el agente usó
los nodos que el mapeo predijo?):

- **EV1-031**: el nodo predicho
  `Restriccion_la_exposicion_maxima_frente_a_una_misma_contraparte_individual_no_debera_superar_61edfb`
  fue consultado vía `ver_nodo` en **las 3 réplicas** de v3 (trazas
  `escalon1b_r{1,2,3}/reensamblado_v3/EV1-031.json`) y aparece en las citas.
  **SÍ — mecanismo predicho observado.**
- **EV1-042**: el nodo predicho `Operacion_acceso_al_mercado_de_cambios_b8c486`
  fue consultado vía `ver_nodo` en **las 3 réplicas** (el segundo nodo
  predicho, `Restriccion_limite_temporal_acceso_mercado_cambios_b53a4f`, no
  aparece en `ver_nodo`; el dato de la clave es el mismo en ambos).
  **SÍ — mecanismo predicho observado.**

### A.3 Los 8 candidatos a regresión por entierro — cierre del circuito del screen B

Método: para cada candidato, replay de TODAS sus queries de `buscar_nodos` del
1b (de `queries_v3_2026-07-30.json`) contra el índice v3 replicado, buscando
las contrapartes v3 del material que el screen B marcó en riesgo, más el
`ver_nodo` directo de las trazas.

| Candidato | Final v3 | ¿Material del screen alcanzado en el 1b? |
|---|---|---|
| EV1-001 | correcta (3-0) | SÍ — 4 queries 1b lo traen al corte (p. ej. r1 "consolidación 9 código información mensual") |
| EV1-007 | correcta (3-0) | SÍ — 3 queries lo traen (`Obligacion_informar_una_sola_partida_3600000y_95c147`) |
| EV1-012 | correcta (3-0) | SÍ — `ver_nodo` directo + 13 queries lo traen |
| EV1-013 | correcta (3-0) | SÍ — `ver_nodo` directo + 3 queries |
| EV1-021 | correcta (3-0) | SÍ — `ver_nodo` directo de las 2 contrapartes + 7 queries |
| EV1-023 | correcta (3-0) | SÍ — `ver_nodo` directo + 3 queries |
| EV1-032 | correcta (3-0) | SÍ — 3 queries traen las contrapartes al corte (sin `ver_nodo` directo) |
| EV1-036 | correcta (**2-1**) | SÍ — 15 queries las traen (cambio de patrón: ver A.4; mayoría intacta) |

**Resultado: 0 de 8 caídos** — dentro de lo esperado del mapeo (las regresiones
en candidatos estaban dentro de las ramas; no se materializó ninguna).

**EV1-035 — caso declarado ESTABLE en el screen (fuera de los 8): REGRESÓ.**
v2 final: correcta 2-1 (`correcta, parcial, correcta`) → v3 final: no-correcta
2-1 (`incorrecta, correcta, parcial`). **FUERA_DE_RAMA** — condición de válvula
(sección C). La evidencia mecánica de sus trazas está en su ficha
(`fichas_delta_1b.json`), incluidos los ranks de sus nodos v2 en el índice v3:
`Restriccion_exposicion_garantizada_por_inmueble_terminado` (contraparte
`…_e4a6e8`) rank 5 — dentro del corte — para la query principal de las 3
réplicas; `Excepcion_excepcion_para_inmuebles_en_construccion` (contraparte
`…_362c92`) rank 28 / fuera de top-50 según la query — fuera del corte de 10
en todas las queries del 1b — aunque la contraparte SÍ aparece consultada en
las trazas v3 (vía otro camino de la traza; constancia mecánica, sin lectura).

### A.4 Cambios de patrón (3-0 ↔ 2-1) sin cambio de mayoría

| Pregunta | Patrón v2→v3 | Mayoría | Réplica que difiere |
|---|---|---|---|
| EV1-002 | 3-0 → 2-1 | correcta (sin cambio) | r2 (correcta → incorrecta) |
| EV1-010 | 2-1 → 3-0 | correcta (sin cambio) | r2 (failed acarreada §8 en v2 → correcta en v3) |
| EV1-012 | 2-1 → 3-0 | correcta (sin cambio) | r3 (incorrecta → correcta) |
| EV1-016 | 2-1 → 3-0 | correcta (sin cambio) | r3 (failed acarreada §8 en v2 → correcta en v3) |
| EV1-036 | 3-0 → 2-1 | correcta (sin cambio) | r3 (correcta → incorrecta por laudo humano 1b) |

## B. Fichas nuevas

`fichas_delta_1b.json` (deja de ser esqueleto) contiene:

- **4 fichas completas** — EV1-029, EV1-031, EV1-035, EV1-042 — en el formato
  de las 9 selladas (id, pregunta, familia, tos_fuente, ground_truth,
  veredictos_mayoria, réplicas con respuesta/claims/traza_tools,
  veredicto_causal), extendido con: `delta_v2_v3`, réplicas de ambos brazos,
  `cruce_trazas_v2_v3` (ids verbatim de nodos consultados por brazo),
  `evidencia_prediccion` (EV1-031/042) y `ranks_nodos_v2_en_indice_v3`
  (EV1-035). Los `veredicto_causal` de EV1-031/EV1-042 transcriben la
  predicción sellada + su verificación mecánica, nada más; los de EV1-029 y
  EV1-035 dicen **"PENDIENTE — condición de válvula; se resuelve en discusión
  pre-registrada"** y no se completan acá.
- **5 fichas breves** de cambio de patrón sin cambio de mayoría (tabla A.4),
  en sección aparte del mismo JSON.

## C. Declaración de válvula

Transcripción del §D del mapeo sellado (`mapeo_delta_v2v3.md`, commit `6c24009`):

> "Si el resultado del escalón 1b cae fuera de las ramas de C — un acierto
> nuevo en una ficha clasificada `no_recuperable_por_v3`, una regresión en
> cualquiera de los 17 casos declarados estables, o un global fuera de
> [19, 30] — la lectura se DETIENE y vuelve a discusión antes de escribir
> conclusión alguna. Un acierto nuevo en EV1-018 (mejora_posible) y una
> regresión en cualquiera de los 8 candidatos nombrados están DENTRO de las
> ramas."

**Declaro formalmente que se cumplen DOS condiciones de válvula:**

1. **EV1-029** — acierto nuevo (2-1 correcta) en una ficha clasificada
   `no_recuperable_por_v3` (mapeo §A: "material parcial idéntico en ambos; el
   2-1 de v2 es varianza sobre el mismo sustrato" — predicción
   sin_cambio_esperado).
2. **EV1-035** — regresión (correcta → no-correcta) en un caso declarado
   estable por el screen B (no estaba entre los 8 candidatos nombrados).

**Consecuencia (transcripta del pre-registro, no interpretada): la lectura SE
DETIENE. Ninguna conclusión se escribe hasta que la discusión pre-registrada
resuelva las dos condiciones.** El global (29 ∈ [19, 30]) y el resto de los
casos quedan cruzados arriba como registro mecánico; ninguna frase de este
documento constituye lectura causal de EV1-029 ni de EV1-035.

### Inventario de evidencia disponible para la discusión

- Fichas completas de los 4 deltas: `corridas/fichas_delta_1b.json` (con cruce
  de trazas por brazo, ids verbatim, ranks de EV1-035, evidencia de predicción
  de EV1-031/042).
- Trazas crudas: `posthoc_run/traces/escalon1b_r{1,2,3}/{grafo_v2,run_3,reensamblado_v3}/`
  (+ crudos por turno en las dbs `escalon1b_r{1,2,3}.db`).
- Expediente y laudos: `corridas/expediente_adjudicacion_1b.md/.json`,
  `corridas/adjudicacion_humana_1b.json`,
  `adjudicacion_humana_2026-07-26.json` (sellado).
- Resultados: `corridas/resultados_1b_FINALES_2026-07-31.json` (+ mecánicos
  `resultados_1b_2026-07-30.json`).
- Queries del brazo v3: `corridas/queries_v3_2026-07-30.json` (907 tool calls).
- Pre-registro: `mapeo_delta_v2v3.md` (6c24009) §A-§F; protocolo + §8;
  las 9 fichas selladas (`fichas_fallas_v2.json`); deslinde
  `informes/deslinde_fallas_v2_2026-07-27.md`.
- Para EV1-029 en particular, constancia mecánica del cruce (sin lectura): los
  conjuntos de nodos consultados difieren entre brazos — v2:
  `Operacion_cesion_de_derechos_de_credito` + 4; v3:
  `Obligacion_las_consultas_o_reclamos_originados_en_cuestiones_suscitadas_con_deudores_de_fid_997afd`,
  `Operacion_cesion_de_creditos_df1276`,
  `Operacion_cesion_de_creditos_sin_responsabilidad_e74f77` + 4 (detalle en la
  ficha).

— Fin de la parte mecánica. La lectura queda DETENIDA por válvula. —
