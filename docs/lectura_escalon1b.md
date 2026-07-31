# Lectura final del escalón 1b — v3 (re-ensamblado) vs v2 sobre EV1

**Fecha:** 2026-07-31. **Pre-registro:** mapeo `mapeo_delta_v2v3.md` (commit
`6c24009`, §A–§F) + `docs/protocolo_escalon1b.md` (commit `d235342`, secciones
1–7; Enmienda §8 en `605de79`). **Medición y adjudicación:** commit `fe4cfa9`
(`resultados_1b_FINALES_2026-07-31.json`, `adjudicacion_humana_1b.json`,
expediente). **Parte mecánica de esta lectura:** commit `7da72dc`
(`corridas/lectura_1b_parte_mecanica.md` + 4 fichas delta). Todo número de este
documento está copiado de esas fuentes o de los chequeos determinísticos de la
Tarea 0/0' (scripts en el scratchpad de sesión; réplica del índice validada
220/220 contra los tool_result reales, como en el mapeo §B). Los dos veredictos
causales que este documento persiste salen VERBATIM de las resoluciones
laudadas de la discusión de válvula; ninguna hipótesis es mía.

## 1. Resultado

Sobre EV1 sellado (36 preguntas, **último uso del set**), N=3, juez v2.1.1
ciego, mayoría ≥2/3, post-adjudicación humana:

| | grafo_v2 | reensamblado_v3 | run_3 (referencia) |
|---|---|---|---|
| **Global** | **27/36** (75.0%) | **29/36** (80.6%) | 31/36 (86.1%) |
| puntual (10) | 7 | 9 | 9 |
| enumerativa (12) | 9 | 9 | 10 |
| condicional (8) | 8 | 7 | 7 |
| sujeto (6) | 3 | 4 | 5 |

Pares discordantes finales v2→v3: **b (v2✗→v3✓) = EV1-029, EV1-031, EV1-042 ·
c (v2✓→v3✗) = EV1-035** (nota registrada en el JSON de resultados: computados
contra los finales adjudicados de ambos brazos). Las 2 combinaciones acarreadas
de la Enmienda §8 (`grafo_v2/EV1-010·r2`, `grafo_v2/EV1-016·r3`,
`origen=sellado_escalon1_hueco_cache`) están marcadas en los resultados.

Caveat de run_3, transcripto del protocolo §6: "run_3 exhibe el mismo síntoma
de provenance imprecisa, su mecanismo interno no fue verificado con la
profundidad con que se auditó v2/v3, y su baseline sellado (31/36
post-adjudicación) vale como medido — la referencia es descriptiva, no un
tercer brazo en disputa."

## 2. Contra el pre-registro

- **Global: DENTRO de la banda dura [19, 30] y DENTRO de la rama central
  28–29** (mapeo §C).
- **Las 9 fichas** (tabla completa en `lectura_1b_parte_mecanica.md` §A.2):
  **8 dentro de rama** — EV1-005, 011, 015, 028, 039 sin cambio esperado y sin
  cambio; EV1-018 mejora_posible que no convirtió; EV1-031 y EV1-042
  acierto_nuevo_esperado que convirtieron — y **1 fuera de rama** (EV1-029,
  válvula resuelta, sección 3).
- **Las dos predicciones de acierto convirtieron con el mecanismo verificado
  en trazas** (§A.2 de la parte mecánica): EV1-031 — el nodo predicho
  `Restriccion_la_exposicion_maxima_frente_a_una_misma_contraparte_individual_no_debera_superar_61edfb`
  consultado vía `ver_nodo` en las 3 réplicas y presente en las citas;
  EV1-042 — el nodo predicho `Operacion_acceso_al_mercado_de_cambios_b8c486`
  consultado vía `ver_nodo` en las 3 réplicas.
- **0 de los 8 candidatos a regresión por entierro cayeron** (EV1-001, 007,
  012, 013, 021, 023, 032, 036 — todos correctos por mayoría en v3). El
  circuito del screen B quedó cerrado con evidencia: para cada candidato, el
  material marcado en riesgo fue alcanzado en el 1b (replay de sus queries
  contra el índice v3 replicado + `ver_nodo` de las trazas — §A.3 de la parte
  mecánica). Incluye a EV1-032, el único sin mitigación medida, que terminó
  correcta 3-0.
- Las locations imperfectas de los nodos de EV1-031/042 (RX-03) se leyeron
  como calidad de cita esperada por debajo del GT, ya predicha (protocolo §6)
  — sin descuento sorpresivo.

## 3. La válvula: dos condiciones, dos rondas de discusión, el diseño funcionando dos veces

La parte mecánica declaró formalmente **dos condiciones de válvula** (mapeo
§D) y detuvo la lectura (`7da72dc`):

1. **EV1-029** — acierto nuevo (2-1) en ficha clasificada `no_recuperable_por_v3`.
2. **EV1-035** — regresión (correcta→no-correcta) en un caso declarado estable
   por el screen.

**Ronda 1 (discusión pre-registrada).** Resolvió EV1-035 (veredicto laudado,
abajo) y propuso para EV1-029 una atribución por material recuperado /
des-colisión, sujeta a un chequeo determinístico bloqueante de provenance
(Tarea 0).

**El freno de rama 3.** El chequeo refutó la atribución propuesta con archivos:
el nodo `…997afd` existía en v2 con descripción idéntica, misma provenance y
mismo chunk productor (`proteccion::3.1__p0`, sobreviviente del desempate de
v2 — no descartado, no colisionado), pero bajo las 11 queries reales del
agente v2 nunca entró al corte de 10 (mejores ranks 16 y 19; nunca consultado).
La lectura volvió a frenarse sin escribir conclusión. **La discusión se reabrió
y reclasificó EV1-029 a `alcanzabilidad`** (la tercera clase taxonómica del
proyecto: existe pero inalcanzable), cuya predicción del mapeo era
mejora_posible_no_garantizada — el fuera-de-rama era un error de casillero del
mapeo, no un fenómeno nuevo.

**Ronda 2 (mecanismo del alcance, Tarea 0').** El camino real de la traza
v3·r2: paso 3, `buscar_nodos('responsable consultas reclamos deudor cedido',
lim 10)` expone el nodo en **rank 6**; paso 4, `ver_nodo` directo. El 2×2
contrafáctico (queries de v2 y de v3·r2 × índices v2 y v3, réplica validada):
la query decisiva habría rendido **rank 7 (≤10) también sobre el índice de
v2**, y la recomposición del índice deja los ranks del nodo esencialmente
iguales entre brazos (16/19→16/21 en las queries de v2; 7→6 en la decisiva).
**RAMA C.**

**Veredictos causales persistidos** (verbatim de las resoluciones laudadas, en
`fichas_delta_1b.json`):

> **EV1-029:** Acierto real; caso de ALCANZABILIDAD, la tercera clase
> taxonómica del proyecto (existe pero inalcanzable): el nodo …997afd existía
> en v2 con descripción idéntica y provenance idéntica, pero bajo las 11
> queries reales del agente v2 nunca entró al corte de 10 (mejores ranks 16 y
> 19). En v3 fue alcanzado; mecanismo verificado en la traza de r2: RAMA C —
> exposición por query directa en el paso 3 ('responsable consultas reclamos
> deudor cedido', rank 6 de 10; ver_nodo directo del nodo en el paso 4); el
> 2×2 contrafáctico muestra que la misma query habría rendido rank 7 (≤10)
> sobre el índice de v2, y que la recomposición del índice deja los ranks del
> nodo esencialmente iguales entre brazos (16/19→16/21 en las queries de v2;
> 7→6 en la decisiva) — la query es nueva de la trayectoria de v3, no un
> desentierro del índice. La conversión no es atribuible al fix; se registra
> como varianza de trayectoria sobre material presente en ambos brazos. El
> mapeo la había clasificado no_recuperable_por_v3; la válvula atrapó el error
> de casillero (correspondía alcanzabilidad, cuya predicción era
> mejora_posible_no_garantizada). Caveat registrado: las réplicas r1 de AMBOS
> brazos son abstenciones aprobadas como correcta por el juez (patrón 'evasiva
> aprobada', precedente run_3/EV1-007), no flaggeadas y no re-abiertas por
> simetría; defecto del juez registrado para U5.

> **EV1-035:** Regresión NO atribuible al delta de ensamblado; el grafo queda
> exonerado por sus propias trazas: mismos nodos consultados en ambos brazos,
> alcanzabilidad intacta (la Excepcion consultada en v3 pese a rank 28), seis
> respuestas casi idénticas que comparten el mismo defecto de borde
> (condiciones de la excepción del 2.9.2.2 mal enunciadas). Mecanismo:
> varianza de descomposición del juez sobre un caso frontera — la misma
> familia de claims fue tallada como central-falsa (r1), no-central (r3) o no
> tallada, y el veredicto final dependió del tallado; canal explícitamente
> declarado fuera del alcance del screen en §E del mapeo. Nota: el laudo
> sellado run_3/EV1-035 ('excepción enunciada sin sus condiciones esenciales —
> sobre-ampliación') indica que las correctas de v2 en este caso eran suerte
> del tallado. Vocabulario del screen afinado: 'estable' declara
> alcanzabilidad estable, no veredicto estable. Caso completo registrado como
> insumo de calibración del juez (U5).

La válvula y el freno funcionaron como diseño, dos veces: atraparon un error
de clasificación del mapeo (EV1-029, casillero equivocado y atribución
propuesta refutada por archivos antes de escribirse) y una regresión de canal
no-grafo (EV1-035).

## 4. Titular

**Del déficit 27-vs-31 del escalón 1, el defecto de ensamblado explica +2
puntos netos medidos (27→29) sobre el mismo caché de extracción y el mismo
instrumento congelado. Dos de las tres conversiones son atribuibles al
re-ensamblado por material recuperado (EV1-031, EV1-042, predichas y
selladas); la tercera (EV1-029) convirtió por varianza de trayectoria sobre
material presente en ambos brazos, y la única regresión (EV1-035) queda
exonerada del grafo por sus trazas.**

## 5. Deudas que el 1b deja registradas (sin resolver acá)

- **Dos defectos del juez documentados**, como expediente de entrada para la
  re-calibración (U5): (i) abstención-aprobada — réplicas r1 de ambos brazos
  de EV1-029 aprobadas como correcta siendo abstenciones (patrón 'evasiva
  aprobada', precedente sellado run_3/EV1-007); (ii) varianza de tallado —
  EV1-035, la misma familia de claims tallada distinto entre réplicas con el
  veredicto dependiendo del tallado.
- **El residuo RX-02 / RX-05 / RX-06** (locations desplazadas por coalescing,
  chunks con roles mezclados, contexto cortado por hard cap) que ningún
  re-ensamblado arregla: queda en `docs/backlog_reextraccion.md` para la
  decisión de re-extracción única, junto con RX-10 (tablas linealizadas) y la
  precisión de RX-07 (chunk mixto `clasificacion::10.4`).
- **EV1 queda quemado por completo** (protocolo §2: este era el último uso).
  La próxima medición requiere EV2 por generación ciega (procedimiento del
  proyecto).

## 6. Costo y evidencia

- **Costo total del 1b: USD 4.6283 de 14** (tracker por filas nuevas de caché;
  desglose en `logs/corridas_1b_2026-07-30.log`: fase 1 $1.4972 + v3·r2
  $1.1248 + reparación de las 8 fallas de conexión $0.3884 + v3·r3 $1.6179).
- Evidencia: pre-registro `6c24009` (mapeo) y `d235342`/`605de79`
  (protocolo + §8); corrida y adjudicación `fe4cfa9`
  (`resultados_1b_FINALES_2026-07-31.json`, `adjudicacion_humana_1b.json`,
  `expediente_adjudicacion_1b.md/.json`, 324 copias por corrida, queries_v3,
  anti-fuga 0/324); parte mecánica `7da72dc`
  (`lectura_1b_parte_mecanica.md`, `fichas_delta_1b.json` con las 4 fichas
  delta — EV1-029 y EV1-035 completadas por esta unidad — y las 5 breves de
  cambio de patrón); trazas `posthoc_run/traces/escalon1b_r{1,2,3}/` + dbs
  `escalon1b_r{1,2,3}.db`; chequeos de esta unidad (Tarea 0/0') en el
  scratchpad de sesión, reproducibles desde los archivos citados.

— Fin de la lectura del escalón 1b. —
