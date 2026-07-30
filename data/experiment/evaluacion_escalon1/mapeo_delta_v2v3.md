# Mapeo del delta v2→v3 contra las fichas del escalón 1 — pre-registro del escalón 1b

**Estado:** pre-registro. Este documento se sella por commit ANTES de correr una sola
llamada del escalón 1b. Todo lo que contiene es análisis determinístico de archivos
existentes (fichas, kg.json de v2 y v3, caché de extracción, trazas cacheadas del
escalón 1): **cero llamadas a API, cero modificaciones a grafos o instrumentos**.
Las predicciones de la sección C quedan apostadas de antemano; la sección D define
cuándo la lectura del 1b se detiene.

Método y reproducibilidad: los números salen de scripts de solo lectura en el
scratchpad de la sesión (`/private/tmp/claude-501/…/scratchpad/`):
`u1_extract_traces.py` (extracción de tool calls desde `cache/calls.db`),
`u1_screen_b2.py` (réplica del índice + screen de queries, con su intermedio
`u1_screen_b.py`), `u1_fichas.py` (sondas de contenido en ambos grafos + mapeo a los
53 chunks recuperados) y `u1_checks_puntuales.py` (verificaciones citadas una a una).
Réplica del índice validada contra la realidad: las 220 queries re-ejecutadas sobre
v2 devuelven **listas idénticas** a los `tool_result` que el agente vio en el
escalón 1 (220/220, 0 desajustes; `u1_screen_b2.py`).

Insumos leídos: `corridas/fichas_fallas_v2.json` (9 fichas), `EV1_runtime.json`
(las 36 preguntas efectivas, con `respuesta_esperada`), `grafo_v2/kg.json` (3.872
nodos), `reensamblado_v3/kg.json` (4.458), `cache_v2/chunks_all.json` +
`chunk_roles.py` (roles 48/368/92), la replicación del dedup v2 (102 descartados:
35 índice / 14 tabla / 53 cuerpo, mismo método que la auditoría de custodia),
`reensamblado_v3/cuarentena.json` (11 propuestos), `harness.py:98-176`
(implementación real de `buscar_nodos`: tokens `[a-z0-9]+` sobre lowercase sin
acentos, índice sobre label+id, score = |intersección|, orden `(-score,
len(label), id)`, corte en `limite`, default 10), y las 254 filas del namespace
`agent|gfp=64294e016163a4fb|cv=aa15d9c9b5b7|think=0` de `cache/calls.db` (sqlite ro).

Nota metodológica previa (afecta todo el documento): los ids de
Restriccion/Obligacion/Excepcion cambian en v3 (sufijo hash de 6 hex) y los de
Operacion cambian de slug (label en vez de `properties.tipo`). Comparar listas de
ids crudos confunde renombre con entierro: un screen ingenuo da 117 "diluidas" de
220. Todo lo que sigue usa un mapa de contrapartes v2→v3 (id exacto → prefijo sin
sufijo hash → (type, label)); con ese mapa, de los 88 nodos que el agente consultó
(`ver_nodo`/`ver_vecinos`) en el escalón 1, 86 tienen contraparte en v3 y **2 no**
(ver B.6).

---

## A. Mecanismo por ficha

Convenciones: "clave" = `respuesta_esperada` de `EV1_runtime.json`; "recuperado" =
nodo cuya provenance corresponde a uno de los 53 chunks de articulado descartados
por el dedup v2 (`u1_fichas.py` los recomputa: 53). Los veredictos v2 de cada ficha
son 3-0 incorrecta salvo EV1-029 y EV1-042 (2-1). La clasificación sale de los
archivos; donde la narrativa de la ficha difiere, lo señalo.

| Ficha | Qué faltó/falló (evidencia) | Dónde vive en v3 | Clasificación |
|---|---|---|---|
| **EV1-005** (7.1 RI, esquema posición mes n) | El nodo del esquema existe en ambos grafos pero con los calificadores amputados: `Obligacion_para_el_calculo_del_importe_correspondiente_al_mes_n_procedera_tenerse_en_cuenta_425…` (v3, prov "Punto 7.1. Normas de procedimiento") lista los componentes pero la sonda "calculada segun datos del mes" da **0 hits en v2 y 0 en v3** (`u1_fichas.py`). La amputación está en la extracción, no en el ensamblado. | Mismo nodo, mismo texto amputado. | **no_recuperable_por_v3** |
| **EV1-011** (niveles 6.5, cartera comercial) | La clave exige la enumeración nominada (normal / **seguimiento especial** con sus situaciones / con problemas / alto riesgo / irrecuperable). Sonda "seguimiento especial": **0 hits en v2 y 0 en v3**; "en negociacion o con acuerdos": 0 y 0. El 6.5 se extrajo partido (RX-06) y la enumeración no se nodificó. El hit nuevo de v3 (`Operacion_clasificacion_en_nivel_riesgo_bajo_en_tratamiento_especial_a3a9d8`, prov 7.2) es otro régimen, no la clave. | Sigue ausente. | **no_recuperable_por_v3** |
| **EV1-015** (criterio general 1.1, residentes en el exterior) | v2 SÍ tenía el texto de la clave: `Obligacion_clasificar_deudores_por_calidad`, `properties.description` = "Los clientes de la entidad, tanto residentes en el país … como residentes en el exterior, … deberán ser clasificados desde el punto de vista de la calidad…" (prov desplazada: "Punto 10.4…"). Su chunk creador es `TO_clasificacion_deudores_actual.pdf::10.4` con **rol índice** — un chunk mixto que arranca en la última línea del índice y cruza al cuerpo de la Sección 1 (su texto contiene "1.1. Criterio general. Los clientes de la entidad (ta…"; `u1_checks_puntuales.py` [2]). v3 excluye el rol índice → la sonda "clasificados desde el punto de vista" da **0 hits en todo v3** ([1]). v3 agrega un nodo secundario recuperado (`Obligacion_en_los_casos_de_clientes_residentes_en_el_exterior_…_3d2968`, prov "Punto 6.2. Criterio de clasificación.", de chunk recuperado), que es un complemento (gestión de riesgos), no el criterio general. | **El texto de la clave desaparece de v3** (única fuente = chunk excluido; el 1.1 no tiene chunk propio — RX-04). Queda solo el secundario 6.2. | **no_recuperable_por_v3** (con pérdida de material respecto de v2 — ver F.1) |
| **EV1-018** (lista 4.1.4, conformidad previa tarjetas) | Los 3 ítems están nodificados idénticos en ambos grafos (`Restriccion_la_participacion_en_juegos_de_azar…`, `Restriccion_la_adquisicion_de_criptoactivos…`, `Restriccion_la_adquisicion_de_tarjetas_de_regalo…`, prov "Punto 4.1…"). Verificación mecánica de alcanzabilidad: en v2, **ninguna de las 2 queries históricas** del caso los traía dentro del corte de 10; en v3 **ambas** traen ≥1 ítem al corte ([4]: 2/2 en v3, 0/2 en v2). Coincide con la adjudicación ("no alcanzado por ningún agente"). | Mismos nodos; entran al corte del índice v3. | **alcanzabilidad** |
| **EV1-028** (salvedad mutuales 1.1.2.5) | Sonda "mutuales o cooperativas" y "mutual": **0 hits en v2 y 0 en v3** (`u1_fichas.py`). La salvedad nunca se extrajo. | Sigue ausente. | **no_recuperable_por_v3** |
| **EV1-029** (deudor cedido a fideicomiso, 1.1.1 + 3.1.1.1) | El componente 3.1.1.1 existe en ambos: `Obligacion_las_consultas_o_reclamos_originados_en_cuestiones_suscitadas_con_deudores_de_fid_997…` ("…deudores de fideicomisos financieros que no fueron notificados fehacientemente…", prov "Punto 3.1. Requisitos mínimos. (parte 1)"). El componente 1.1.1 de la clave ("hayan sido o no notificados" como parte de la definición de usuario) da 0 hits en ambos. v2 ya logró 1/3 correcta con este material. | Mismo material parcial. | **no_recuperable_por_v3** (parcial: lo presente no cambia, lo ausente sigue ausente) |
| **EV1-031** (75 SMVM, 2.8.3.3) | v2: "salario" **0 hits en todo el grafo**. v3: aparece `Restriccion_la_exposicion_maxima_frente_a_una_misma_contraparte_individual_no_debera_superar_61edfb` — "…los límites especificados para personas humanas en cartera de consumo (75 [veces el] Salario Mínimo…", **nuevo en v3 y proveniente de un chunk recuperado** (prov "Punto 2.10. A los fines de calcular el límite definido en el párrafo precedente," — location de falso header RX-03; el GT es 2.8.3.3). Alcanzabilidad verificada: **7 de las 11 queries históricas** del caso lo traen dentro del corte en v3 (0/11 en v2; [4]). | Nodo nuevo desde chunk recuperado, alcanzable. | **recuperable_por_v3** |
| **EV1-039** (exigencia básica 1.2) | El material existe y el agente lo usó en v2 (p. ej. `Restriccion_las_companias_financieras_que_realicen_en_forma_directa_operaciones_de_comercio__7b…`). El defecto es de contenido: los nodos dicen "Bancos … exigencia básica de **2.500** millones" y "Restantes entidades … **5.000** millones" — la clave adjudicada dice lo inverso (bancos 5.000, restantes 2.500). Causa visible en el texto crudo del chunk `TO_capitales_minimos_actual.pdf::1.2`: la tabla se linealizó como "Restantes entidades Bancos (salvo Cajas de Crédito Cooperativas) -En millones de pesos- 5.000 2.500" — encabezados en un orden y valores en otro ([3]). El extractor emparejó según esa linealización. Idéntico en v3 (mismo caché). | Mismos nodos con los mismos montos. | **no_recuperable_por_v3** (defecto congelado en el texto del chunk) |
| **EV1-042** (anterioridad 3 días hábiles, 3.5.3) | v2: "anterioridad no mayor" 0 hits. v3: **2 nodos, ambos de chunks recuperados**, con el dato exacto de la clave: `Operacion_acceso_al_mercado_de_cambios_b8c486` y `Restriccion_limite_temporal_acceso_mercado_cambios_b53a4f` — "El acceso al mercado de cambios se produce con una anterioridad no mayor a los 3 (tres) días hábiles…". Locations imperfectas (falsos headers RX-03: "Punto 1.2. Las entidades podrán…" y "Punto 3.17. ii)…"; GT 3.5.3). Alcanzabilidad: **3 de las 7 queries históricas** traen ≥1 de los 2 al corte en v3 (0/7 en v2; [4]). v2 ya tenía 1/3 correcta. | Nodos nuevos desde chunks recuperados, alcanzables. | **recuperable_por_v3** |

Discrepancia fichas-vs-archivos a registrar: la adjudicación de EV1-018 lo llama
"alcanzabilidad compartida" y los archivos lo confirman; pero en EV1-015 la ficha
("el 1.1 no alcanzado") describe v2, y los archivos agregan algo que la ficha no
sabía: en v3 ese material directamente **no existe**.

## B. Screen de regresión por entierro

1. **Réplica del índice** (`u1_screen_b2.py`): mismo código real (`GraphIndex` de
   `harness.py` + `loader.load_graph_from_path`, `adapter_key=None`) sobre
   `grafo_v2/kg.json` (3.872 nodos) y `reensamblado_v3/kg.json` (4.458).
   Fidelidad: 220/220 queries reproducen exactamente los `tool_result` cacheados.
2. **Cobertura**: de las 254 filas del namespace se extrajeron **348 tool calls**
   (220 `buscar_nodos` + 90 `ver_nodo` + 38 `ver_vecinos`), 0 turnos sin caso
   mapeado, los 36 casos presentes. Las 220 queries de `buscar_nodos` (todas
   distintas como par consulta+límite) se re-ejecutaron contra ambos índices: 100%.
3. **Clasificación** (consciente de contrapartes; el screen ingenuo por ids crudos
   queda registrado en `u1_screen_b.py` como control metodológico):

   | Clase | Queries |
   |---|---|
   | IDENTICA | 36 |
   | REORDENADA | 1 |
   | AMPLIADA | 167 |
   | **DILUIDA** | **16** |

   DILUIDA = algún nodo que el agente consultó (`ver_nodo`/`ver_vecinos`) en ese
   caso estaba en el top de esa query en v2 y su contraparte v3 queda fuera del
   corte en v3.
4. **Candidatos a regresión por entierro** — casos CORRECTOS en v2 (fuera de las 9
   fichas) con ≥1 query DILUIDA. Son **8**, nombrados con su query y mitigación
   medida (rango de la contraparte con límite 50, y si otras queries del caso la
   siguen trayendo al corte):

   | Caso | Query diluida | Nodo v2 fuera del corte en v3 | Mitigación |
   |---|---|---|---|
   | EV1-001 | "código 9 no presenta información consolidada mensual" | `Obligacion_las_entidades_financieras_controlantes_sujetas_a_supervision_consolidada_observa` | rank 11 en v3; otras 2 queries del caso la traen |
   | EV1-007 | "36000001 informar" | `Obligacion_informar_una_sola_partida_3600000y` | rank 12; otra query la trae |
   | EV1-012 | "conceptos por intermediación financiera excluidos no comprendidos" | `Operacion_clasificacion_de_deudores_por_conceptos_de_intermediacion_financiera` | fuera de top-50 para esa query; otras 2 queries traen su contraparte |
   | EV1-013 | "crédito consumo vivienda cartera clasificación" | `Operacion_clasificacion_de_credito` | rank 21; otra query trae su contraparte |
   | EV1-021 | "plazo ingreso liquidación fondos mercado cambios no residente" y "VPU Vehículo Proyecto Único RIGI artículo 198 Ley 27.742" | `Restriccion_los_cobros_por_la_prestacion_de_servicios_…` / `Excepcion_los_cobros_…_vpu_` | ranks 11; 1 y 3 queries alternativas |
   | EV1-023 | "precancelación total operación comisión" | `Restriccion_en_el_caso_de_precancelacion_total_no_se_admitira_la_aplicacion_de_comisiones_cu` | rank 14; otra query la trae |
   | **EV1-032** | "DvP fallida contraprestación capital exposición", "demora liquidación DvP cargo capital mora", "punto 4.1.1 entrega contra pago demora 31 45 días" | `Operacion_calculo_del_cargo_de_capital_ajustado_por_mora` (contraparte por label `Operacion_calculo_de_variable_ka_649aa7`: fuera de top-50, **0 queries alternativas la traen**) y `Operacion_liquidacion_de_operacion_con_entrega_contra_pago` | la peor mitigación del screen; además ver B.6 |
   | EV1-036 | "grupo 2 deberán clasificar exposiciones hipotecaria" y "exposiciones hipotecaria grupo 2 ponderador" | `Restriccion_exposiciones_en_situacion_de_incumplimiento_con_garantia_hipotecaria_normativas_` | rank 18; otras 4 queries traen su contraparte |

   Los restantes 17 casos correctos sin queries DILUIDAS quedan **declarados
   estables** (su material alcanzado en v2 sigue dentro del corte con las mismas
   queries). Las fichas con DILUIDAs (EV1-011, EV1-029, EV1-031) ya eran fallas:
   no son candidatos a regresión.
5. **Cuarentena** (inventario, sin predicción): de los 11 sujetos propuestos de
   `reensamblado_v3/cuarentena.json`, 10 son alcanzables en el índice v3 por al
   menos un token propio de su label en el top-10 (p. ej. "inversor",
   "originante", "radpip"); **1 es léxicamente huérfano en esa prueba**:
   `Sujeto_propuesto_entidades_financieras_del_grupo_2` (todos sus tokens quedan
   fuera del top-10 por frecuencia). (`u1_screen_b2.py`, bloque cuarentena.)
6. **Fuera de la taxonomía de queries, y más grave que una dilución**: 2 nodos que
   el agente consultó en v2 **no tienen contraparte alguna en v3** — ambos son
   cáscaras de origen índice que v3 elimina:
   `Restriccion_deudores_que_no_deben_ser_objeto_de_clasificacion` (usado 2 veces
   en EV1-015, caso ya fallido) y
   `Restriccion_exigencia_de_capital_por_riesgo_de_credito_de_contraparte_en_operaciones_con_ent`
   (usado en **EV1-032**, caso correcto — se suma a sus 3 queries diluidas). A eso
   se agrega la pérdida de material de EV1-015 descripta en A (nodo no consultado
   por el agente, pero portador del texto de la clave).

## C. Predicciones pre-registradas para el escalón 1b

Derivación mecánica de A y B. Por ficha:

| Ficha | Predicción | Mecanismo (una línea) |
|---|---|---|
| EV1-005 | sin_cambio_esperado | calificadores amputados en la extracción; idénticos en v3 |
| EV1-011 | sin_cambio_esperado | enumeración del 6.5 ausente en ambos grafos |
| EV1-015 | sin_cambio_esperado | ya fallaba con el material presente; en v3 el texto de la clave no existe (no puede mejorar por re-ensamblado) |
| EV1-018 | mejora_posible_no_garantizada | clasificada alcanzabilidad: los 3 ítems entran al corte de 10 en v3 para las 2 queries históricas; la conversión depende del agente |
| EV1-028 | sin_cambio_esperado | salvedad nunca extraída; ausente en ambos |
| EV1-029 | sin_cambio_esperado | material parcial idéntico en ambos; el 2-1 de v2 es varianza sobre el mismo sustrato |
| EV1-031 | acierto_nuevo_esperado | dato de la clave nuevo en v3 desde chunk recuperado, alcanzable por 7/11 queries históricas |
| EV1-039 | sin_cambio_esperado | montos invertidos por linealización de tabla, congelados en el chunk; idénticos en v3 |
| EV1-042 | acierto_nuevo_esperado | dato de la clave en 2 nodos nuevos de chunks recuperados, alcanzables por 3/7 queries históricas (cita imperfecta: locations RX-03) |

Chequeo de consistencia con la regla: ninguna ficha clasificada `alcanzabilidad`
(EV1-018) ni `ajena_al_grafo` (ninguna) predice acierto_nuevo por el re-ensamblado.

Por candidato a regresión (nombrados en B.4): EV1-001, EV1-007, EV1-012, EV1-013,
EV1-021, EV1-023, EV1-032 y EV1-036, cada uno con su query diluida en la tabla.
**EV1-032 es el único sin mitigación medida** (contraparte fuera de top-50, sin
queries alternativas que la traigan, más un nodo consultado que v3 elimina); los
otros 7 tienen el material a rank 11–21 o recuperable por otras queries del caso.

**Global.** v2 midió 27/36. Aciertos nuevos: mínimo 0 (la conversión pasa por
agente y juez), esperados 2 (EV1-031, EV1-042), máximo 3 (si EV1-018 convierte).
Regresiones candidatas: 0 a 8 (las 8 nombradas).

- **Banda dura pre-registrada: v3 ∈ [27 + 0 − 8, 27 + 3 − 0] = [19, 30] sobre 36.**
- Rama central (aciertos esperados 2; regresión materializada a lo sumo la no
  mitigada, EV1-032): **28 a 29**, con techo 30 si EV1-018 convierte.

Declaración: estas predicciones se derivan de análisis determinístico de presencia
de material y alcanzabilidad léxica; la conversión a aciertos pasa por el agente y
el juez, que no son determinísticos a nivel de frase (motivo del N=3). Son ramas,
no certezas.

## D. Válvula

Si el resultado del escalón 1b cae fuera de las ramas de C — un acierto nuevo en
una ficha clasificada `no_recuperable_por_v3`, una regresión en cualquiera de los
17 casos declarados estables, o un global fuera de [19, 30] — la lectura se
DETIENE y vuelve a discusión antes de escribir conclusión alguna. Un acierto nuevo
en EV1-018 (mejora_posible) y una regresión en cualquiera de los 8 candidatos
nombrados están DENTRO de las ramas.

## E. Límites del mapeo

- No cubre la no-determinismo de frase del agente: las queries del 1b serán otras;
  las 220 históricas son el mejor proxy disponible, no el comportamiento futuro.
  (Motivo del N=3.)
- No cubre fallas nuevas que v3 pueda introducir por mecanismos no enumerados
  (p. ej. efectos de los 586 nodos y 813 aristas adicionales sobre `ver_vecinos`,
  o cambios de `properties` por diferente primer avistaje entre órdenes de
  ensamblado).
- No cubre nada que dependa del juez (estabilidad de veredicto, gate de citas
  sobre las locations imperfectas de EV1-031/042).
- La alcanzabilidad medida es del top-k léxico; el agente puede formular queries
  mejores o peores que las históricas.

## F. Observaciones fuera de alcance (no accionadas en esta unidad)

1. **La exclusión del rol índice puede tirar contenido real.** El chunk
   `TO_clasificacion_deudores_actual.pdf::10.4` (rol índice por su offset inicial)
   es mixto: cruza al cuerpo de la Sección 1 y era la única fuente del criterio
   general 1.1 (clave de EV1-015). v3 lo excluye y el texto desaparece del grafo.
   Matiza la afirmación de RX-07 ("el índice no aporta un solo hecho normativo"):
   vale para páginas de índice puras, no para chunks mixtos RX-05. Candidata a
   precisión en el backlog de re-extracción.
2. **Inversión de montos del 1.2 de capitales mínimos** (EV1-039): la tabla se
   linealiza con encabezados y valores en órdenes distintos y el extractor
   empareja mal (bancos 2.500 / restantes 5.000, invertido contra la clave
   adjudicada). Es una especie de defecto de instrumento no listada en el backlog
   (linealización de tablas dentro del articulado); además, los dos nodos
   (`Restriccion_bancos_salvo_cajas_de_credito_cooperativas_…`,
   `Restriccion_restantes_entidades_…`) son candidatos naturales a entrada del
   backlog de refinamiento con `nodos_objetivo`.
3. **Locations RX-03 en los nodos que fundan las dos predicciones de acierto**
   (EV1-031: "Punto 2.10. A los fines de calcular…"; EV1-042: "Punto 1.2. Las
   entidades podrán…" y "Punto 3.17. ii)…"): el dato es correcto, la cita es
   imprecisa; si el 1b convierte los aciertos, la calidad de cita quedará por
   debajo del GT (2.8.3.3 y 3.5.3).
4. **`Sujeto_propuesto_entidades_financieras_del_grupo_2`** queda léxicamente
   huérfano en el top-10 del índice v3 (B.5).
5. Las dos cáscaras de índice que el agente usó en v2 (B.6) muestran que el agente
   sí consumía nodos-título; si el 1b regresa en EV1-032, el primer lugar donde
   mirar es esa eliminación.

— Fin del pre-registro. Sellar por commit antes de correr el escalón 1b. —
