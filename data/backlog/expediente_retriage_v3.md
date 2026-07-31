# Expediente de re-triage del backlog de nodos contra reensamblado_v3 (2026-07-31)

Unidad de EXTRACCIÓN Y VERIFICACIÓN mecánica: verifico contra archivos y
PROPONGO estados; **los laudos son de la adjudicadora**. Precondición
verificada: working tree limpio; promoción de v3 commiteada en `e129473`.
Grafos leídos: `grafo_v2/kg.json` (v2, sellado) y
`grafo_v2/reensamblado_v3/kg.json` (v3, vigente). Scripts de verificación en
el scratchpad de sesión (`u3_retriage.py`); mapeo de contrapartes v2→v3 por
id exacto / prefijo sin sufijo hash / (type, label), el mismo del mapeo del 1b.

## Tarea 1 — El registro

- `data/backlog/backlog.jsonl` **no existe** — la propia spec lo declara:
  `docs/spec_backlog_refinamiento.md:4` "no existe todavía — se crea al
  poblar".
- El registro de las entradas adjudicadas contra v2 es la **población inicial
  planificada de la spec §6** ("plan — no ejecutado"): **16 entradas = 8 del
  escalón 1** (`§6.1`, fuente `fichas_fallas_v2.json` + deslinde
  `deslinde_fallas_v2_2026-07-27.md` + laudos `adjudicacion_humana_2026-07-26.json`;
  EV1-029 excluida-con-motivo) **+ 8 correcciones agrupadas del triage U5**
  (`§6.2`, fuente `grafo_v2/triage_sospechosas_U5.json`: 75 filas adjudicadas,
  31 VP = 10 `VP` + 21 `VP-menor`). Conteo coincide con el esperado (16).

## Tarea 2 — Re-triage de las 16 entradas

### Grupo escalón 1 (8 entradas, spec §6.1)

**E1 · EV1-031** — registro v2 (verbatim §6.1): "extracción/completitud — 75
SMVM (2.8.3.3) ausente", especie `ausencia`.
Verificación v3: el material **existe** —
`Restriccion_la_exposicion_maxima_frente_a_una_misma_contraparte_individual_no_debera_superar_61edfb`,
descripción: "La exposición máxima frente a una misma contraparte individual
no deberá superar, al momento del acuerdo, los límites especificados para
personas humanas en cartera de consumo (75 veces el Salario Mínimo Vital y
Móvil)…" (v2: 0 hits para "salario mínimo"). Convertida 3-0 en el 1b con el
nodo consultado en las 3 réplicas (`lectura_1b_parte_mecanica.md` §A.2).
**Estado propuesto: `resuelta_por_v3`.** Caveat de cita: la location del nodo
es "Punto 2.10. A los fines de calcular…" (falso header RX-03), no el GT
2.8.3.3.
Vía de cierre: **chunk-contra-PDF** (el 2.8.3.3 contra el nodo); la pregunta
EV1-031 está QUEMADA y no sirve como re-test.

**E2 · EV1-042** — registro v2: "extracción/completitud — ventana del 3.5.3
ausente", `ausencia`.
Verificación v3: el dato **existe en 2 nodos** —
`Operacion_acceso_al_mercado_de_cambios_b8c486` y
`Restriccion_limite_temporal_acceso_mercado_cambios_b53a4f`, ambos con
"El acceso al mercado de cambios se produce con una anterioridad no mayor a
los 3 (tres) días hábiles a la fecha de vencimiento del servicio de capital o
interés a pagar." (v2: 0 hits). Convertida 3-0 en el 1b, nodo predicho
consultado en las 3 réplicas.
**Estado propuesto: `resuelta_por_v3`.** Caveat de cita: locations "Punto
1.2. Las entidades podrán dar acceso…" y "Punto 3.17. ii)…" (RX-02/RX-03), no
el GT 3.5.3.
Vía de cierre: **chunk-contra-PDF** (3.5.3); EV1-042 quemada.

**E3 · EV1-028** — registro v2: "extracción/completitud — salvedad
mutuales/cooperativas (1.1.2.5) ausente", `ausencia`.
Verificación v3: "mutual" da **0 hits en v3 y 0 en v2** (doc Protección). El
1b la mantuvo 3-0 incorrecta.
**Estado propuesto: `vigente_sin_cambios`** (misma ausencia).
Vía de cierre post-corrección: **chunk-contra-PDF** (1.1.2.5); EV1-028 quemada.

**E4 · EV1-011** — registro v2: "extracción/completitud — enumeración de
niveles del 6.5 ausente", `ausencia`.
Verificación v3: "seguimiento especial" y "en negociación o con acuerdos" dan
**0 hits en ambos grafos**. La ausencia persiste, y v3 agrega un agravante
nuevo: la fuente de confabulación del 7.2 (candidata d).
**Estado propuesto: `vigente_sin_cambios`** (con la candidata d como anexo).
Vía de cierre post-corrección: **chunk-contra-PDF** (6.5); EV1-011 quemada.

**E5 · EV1-005** — registro v2: "extracción/completitud — calificadores del
7.1 RI amputados en nodo existente", `amputacion`.
Verificación v3: mismo nodo con nueva clave —
`Obligacion_para_el_calculo_del_importe_correspondiente_al_mes_n_procedera_tenerse_en_cuenta_425c6b`
— descripción idéntica a la amputada de v2 ("…Responsabilidad Patrimonial
Computable…", "calculada según datos del mes" sigue en **0 hits**).
**Estado propuesto: `vigente_sin_cambios`** (id v3 mapeado: `…_425c6b`).
Vía de cierre post-corrección: **chunk-contra-PDF** (7.1 RI); EV1-005 quemada.

**E6 · EV1-039** — registro v2: "extracción/contenido — nodos con la tabla del
1.2 cruzada (sonda pre-registrada confirmada)", `quimera`.
Verificación v3: la inversión está **intacta** —
`Restriccion_bancos_salvo_cajas_de_credito_cooperativas_deberan_observar_exigencia_basica_de__2d3063`
("…exigencia básica de 2.500 millones de pesos") y
`Restriccion_restantes_entidades_deberan_observar_exigencia_basica_de_5_000_millones_de_pesos_50658f`
("…5.000 millones de pesos") — invertidos contra la key sellada (bancos
5.000 / restantes 2.500). Tercer nodo del grupo:
`Restriccion_las_companias_financieras_que_realicen_en_forma_directa_operaciones_de_comercio__7bb7bb`
(correcto en sí). El 1b la mantuvo 3-0 incorrecta.
**Estado propuesto: `vigente_sin_cambios`** (ids v3 mapeados; es la misma
candidata a / RX-10, elegible para corrección post-1b).
Vía de cierre: **chunk-contra-PDF** — con la salvedad de que el CHUNK MISMO
porta la linealización invertida (candidata a): el cierre necesita el PDF
como árbitro, no el chunk solo.

**E7 · EV1-015** — registro v2: "índice/alcance (H1) — el dato EXISTE, no
rankea; provenance anclada en 10.4", `alcanzabilidad`.
Verificación v3: **el portador desapareció** — el nodo v2
`Obligacion_clasificar_deudores_por_calidad` (prov "Punto 10.4…", descripción
"Los clientes de la entidad, tanto residentes en el país… como residentes en
el exterior… deberán ser clasificados…") **no tiene contraparte en v3** (ni
id, ni prefijo, ni type+label); "tanto residentes en el pais" da v3=0 / v2=1.
El único hit v3 de "deberán ser clasificados" es otra regla
(`Obligacion_los_deudores_excluidos_precedentemente_deberan_ser_clasificados_y_sus_deudas_pre_9c9e81`,
6.5 parte 5). Mecanismo documentado: el chunk portador
(`clasificacion::10.4`, mixto índice→cuerpo) quedó excluido por rol
(precisión RX-07; mapeo §F.1).
**Estado propuesto: `modificada_por_v3`** — la especie empeoró de
`alcanzabilidad` a `ausencia` (es la candidata b).
Vía de cierre: restauración candidata (candidata b) + **chunk-contra-PDF**
(1.1 contra el cuerpo del PDF); EV1-015 quemada.

**E8 · EV1-018** — registro v2: "índice/alcance (H1) — los 3 ítems del 4.1.4
EXISTEN; falla compartida con run_3", `alcanzabilidad`.
Verificación v3: los 3 ítems **siguen existiendo** con ids renombrados:
`Restriccion_la_participacion_en_juegos_de_azar_y_apuestas_de_distinto_tipo_requiere_conformi_c06f33`,
`Restriccion_la_adquisicion_de_criptoactivos_en_sus_distintas_modalidades_requiere_conformida_b0f0a5`,
`Restriccion_la_adquisicion_de_tarjetas_de_regalo_o_equivalentes_de_tiendas_o_locales_radicad_e9ac6b`.
El 1b la mantuvo 3-0 incorrecta (no-respuesta, laudo por consistencia).
**Estado propuesto: `vigente_sin_cambios`** (ids v3 mapeados).
Vía de cierre: es defecto de alcance/comportamiento, no de contenido; el
re-test exigiría **pregunta con gold NO quemada** (EV1-018 quemada).

### Grupo triage U5 (8 correcciones agrupadas, 31 aristas VP — spec §6.2)

Verificación mecánica: para cada una de las 31 filas VP, mapeé el nodo
`norma` de v2 a su contraparte v3 y busqué la arista con el mismo `sujeto`.
**Resultado: 31/31 aristas presentes en v3** (todas `aplica_a`; los endpoints
R/O/E cambiaron de id por el sufijo hash — mapeo por prefijo). Era lo
esperable: el re-ensamblado consume la misma extracción y la misma resolución
de sujetos; no toca asignaciones.

| Entrada (spec §6.2) | Filas VP | Verificación v3 | Estado propuesto |
|---|---|---|---|
| T1 · descenso `banco` CapMin 2.5 (×2 aristas) | 2 | presentes | `vigente_sin_cambios` |
| T2 · descenso Exterior 14.5__p1 (×4) | 4 | presentes | `vigente_sin_cambios` |
| T3 · descenso RI 3.1__p0 (×2) | 2 | presentes | `vigente_sin_cambios` |
| T4 · `sujeto_termino_ajeno` (usuario SF en Exterior 13.4, ×2) | 2 | presentes | `vigente_sin_cambios` |
| T5 · estrechamiento colectivo→EF Exterior (×18, corrección sistemática) | 18 | presentes | `vigente_sin_cambios` |
| T6 · clase forzada VPU→`exportador` (14.1) | 1 | presente | `vigente_sin_cambios` |
| T7 · clase forzada "residentes"→`persona_humana` (3.17__p1) | 1 | presente | `vigente_sin_cambios` |
| T8 · clase forzada "clientes"→`exportador` (3.18__p0) | 1 | presente | `vigente_sin_cambios` |

Vía de cierre de las 8 (la natural de la spec §6.2): **chunk-contra-PDF** con
el `chunk_id` de cada fila del triage (material no quemado; no depende de EV1).

## Tarea 3 — Candidatas nuevas (estado propuesto: `candidata_nueva`)

### a) RX-10 — montos invertidos del 1.2 de capitales mínimos

Nodos v3 (des-colapso/renombre de los citados en el mapeo §A):
- `Restriccion_bancos_salvo_cajas_de_credito_cooperativas_deberan_observar_exigencia_basica_de__2d3063` —
  "Bancos (salvo Cajas de Crédito Cooperativas) deberán observar exigencia
  básica de 2.500 millones de pesos"
- `Restriccion_restantes_entidades_deberan_observar_exigencia_basica_de_5_000_millones_de_pesos_50658f` —
  "Restantes entidades deberán observar exigencia básica de 5.000 millones de
  pesos"

Evidencia del defecto — chunk crudo del caché
(`TO_capitales_minimos_actual.pdf::1.2`, 343 chars, `cache_v2/full`):
«Restantes entidades / Bancos / (salvo Cajas de Crédito Cooperativas) / -En
millones de pesos- / 5.000 2.500 / Las compañías financieras que realicen, en
forma directa, operaciones de comercio exterior / deberán observar las
exigencias establecidas para los bancos.» — la linealización de la tabla trae
encabezados y valores en órdenes distintos (RX-10, `docs/backlog_reextraccion.md`);
la key sellada del caso EV1 correspondiente dice bancos 5.000 / restantes
2.500. **Ya es post-1b: elegibles para corrección** (misma entrada que E6).

### b) Pérdida del criterio general 1.1 (precisión RX-07)

Confirmado que el texto **no existe en ningún nodo de v3**: "tanto residentes
en el pais" → 0 hits (v2 → 1); el único "deberán ser clasificados" de v3 es
la regla de deudores excluidos del 6.5 parte 5 (`…_9c9e81`), otra cosa.
Fuente de la restauración candidata: el nodo v2
`Obligacion_clasificar_deudores_por_calidad` (descripción completa arriba,
E7) y su chunk `TO_clasificacion_deudores_actual.pdf::10.4` (mixto
índice→cuerpo, excluido por rol en v3 — precisión RX-07 del backlog, mapeo
§A EV1-015/§F.1).

### c) Los 11 sujetos de cuarentena (`reensamblado_v3/cuarentena.json`)

Los 11 existen como nodos en v3; **ninguno tiene aristas de jerarquía**
(subclase_de/miembro_de = 0); todas sus aristas son `aplica_a` entrantes desde
las normas que los mencionan:

| Sujeto propuesto | Aristas in | padre_sugerido (propuesta de `subclase_de`, pendiente de laudo) |
|---|---|---|
| `Sujeto_propuesto_inversor` | 4 | `Sujeto_contraparte` |
| `Sujeto_propuesto_entidades_financieras_del_grupo_1` | 2 | `Sujeto_entidad_financiera` |
| `Sujeto_propuesto_beneficiarios_de_radpip_y_o_radpign` | 1 | `Sujeto_contraparte` |
| `Sujeto_propuesto_entidad_nominada_por_el_importador_para_realizar_seguimiento_de_oficializaciones` | 1 | (sin sugerencia) |
| `Sujeto_propuesto_entidades_del_grupo_a` | 1 | `Sujeto_entidad_financiera` |
| `Sujeto_propuesto_entidades_financieras_del_grupo_2` | 1 | `Sujeto_entidad_financiera` |
| `Sujeto_propuesto_inversores_y_tenedores_de_titulizacion` | 1 | `Sujeto_contraparte` |
| `Sujeto_propuesto_originante` | 1 | (sin sugerencia) |
| `Sujeto_propuesto_originante_acreedor_inicial` | 1 | `Sujeto_rol_alcance_capmin` |
| `Sujeto_propuesto_originante_fiduciario` | 1 | `Sujeto_fiduciario_de_fideicomiso_financiero` |
| `Sujeto_propuesto_personas_juridicas_beneficiarias_del_regimen_de_economia_del_conocimiento` | 1 | `Sujeto_beneficiario_economia_conocimiento` |

Huérfano léxico (mapeo §B.5): `Sujeto_propuesto_entidades_financieras_del_grupo_2`
— ninguno de sus tokens propios lo trae al top-10 del índice v3.

### d) Fuente de la confabulación de EV1-011 (régimen del 7.2)

El laudo del 1b para EV1-011: "enumeración de 6 niveles de otro régimen (7.2)
en lugar de los 5 de la key". Verificado en v3: **33 nodos** con provenance en
el "Punto 7.2. Niveles de clasificación" de Clasificación, incluidos los
niveles nominados como nodos `Operacion` **nuevos en v3** (des-colapso):
`Operacion_clasificacion_en_nivel_situacion_normal_94ca1a`,
`Operacion_clasificacion_en_nivel_riesgo_bajo_en_observacion_48fdc5`,
`Operacion_clasificacion_en_nivel_riesgo_bajo_en_tratamiento_especial_a3a9d8`,
`Operacion_clasificacion_en_nivel_riesgo_medio_61a12e`, más las categorías
descriptas en `Restriccion_comprende_a_los_clientes_con_atrasos_de_mas_de_180_dias_hasta_un_ano_41d23c`
y `Restriccion_comprende_a_los_clientes_insolventes_o_en_quiebra_con_nula_o_escasa_posibilidad__38…`.
**La enumeración del 6.5 sigue ausente** (E4: 0 hits de sus niveles
nominados). Candidata de **anotación/deslinde** (los nodos del 7.2 son
legítimos de su régimen; el defecto es que sin el 6.5 el agente los toma como
respuesta para la cartera comercial).

## Tarea 4 — Tabla resumen para el laudo

| id | origen | estado_propuesto | evidencia (puntero) | vía_de_cierre_propuesta |
|---|---|---|---|---|
| E1 · EV1-031 | escalon1_fallas (spec §6.1) | resuelta_por_v3 | nodo `…_61edfb`; 1b 3-0 | chunk-contra-PDF (2.8.3.3) |
| E2 · EV1-042 | escalon1_fallas | resuelta_por_v3 | nodos `…_b8c486`/`…_b53a4f`; 1b 3-0 | chunk-contra-PDF (3.5.3) |
| E3 · EV1-028 | escalon1_fallas | vigente_sin_cambios | "mutual" 0 hits v2/v3 | chunk-contra-PDF (1.1.2.5) post-corrección |
| E4 · EV1-011 | escalon1_fallas | vigente_sin_cambios | "seguimiento especial" 0 hits v2/v3 | chunk-contra-PDF (6.5) post-corrección |
| E5 · EV1-005 | escalon1_fallas | vigente_sin_cambios | id v3 `…_425c6b`, misma amputación | chunk-contra-PDF (7.1 RI) post-corrección |
| E6 · EV1-039 | escalon1_fallas | vigente_sin_cambios | nodos `…_2d3063`/`…_50658f` invertidos | PDF como árbitro (chunk viciado, RX-10) |
| E7 · EV1-015 | escalon1_fallas | modificada_por_v3 | portador v2 sin contraparte; "tanto residentes…" 0 hits v3 | restauración (cand. b) + chunk-contra-PDF (1.1) |
| E8 · EV1-018 | escalon1_fallas | vigente_sin_cambios | 3 ids v3 `…_c06f33`/`…_b0f0a5`/`…_e9ac6b` | pregunta con gold NO quemada |
| T1 · descenso CapMin 2.5 | triage_extraccion (§6.2) | vigente_sin_cambios | 2/2 aristas en v3 | chunk-contra-PDF (chunk del triage) |
| T2 · descenso Exterior 14.5__p1 | triage_extraccion | vigente_sin_cambios | 4/4 aristas en v3 | chunk-contra-PDF |
| T3 · descenso RI 3.1__p0 | triage_extraccion | vigente_sin_cambios | 2/2 aristas en v3 | chunk-contra-PDF |
| T4 · usuario SF en Exterior 13.4 | triage_extraccion | vigente_sin_cambios | 2/2 aristas en v3 | chunk-contra-PDF |
| T5 · estrechamiento colectivo→EF | triage_extraccion | vigente_sin_cambios | 18/18 aristas en v3 | chunk-contra-PDF (corrección sistemática) |
| T6 · VPU→exportador 14.1 | triage_extraccion | vigente_sin_cambios | 1/1 arista en v3 | chunk-contra-PDF |
| T7 · residentes→persona_humana 3.17__p1 | triage_extraccion | vigente_sin_cambios | 1/1 arista en v3 | chunk-contra-PDF |
| T8 · clientes→exportador 3.18__p0 | triage_extraccion | vigente_sin_cambios | 1/1 arista en v3 | chunk-contra-PDF |
| a · RX-10 montos 1.2 | mapeo/backlog RX (post-1b) | candidata_nueva | chunk crudo 343c + nodos `…_2d3063`/`…_50658f` | PDF como árbitro (== E6) |
| b · criterio 1.1 perdido | precisión RX-07 / mapeo §F.1 | candidata_nueva | 0 hits v3; portador v2 + chunk `clasificacion::10.4` | restauración + chunk-contra-PDF |
| c · 11 sujetos de cuarentena | reensamblado (cuarentena.json) | candidata_nueva | 11 nodos sin jerarquía; tabla con padres_sugeridos | laudo de aristas `subclase_de` por sujeto |
| d · confabulación 7.2 (EV1-011) | ficha delta 1b / laudo | candidata_nueva | 33 nodos del 7.2, niveles nominados nuevos en v3 | anotación/deslinde + corrección E4 |

**Conteo por estado propuesto:** `resuelta_por_v3` 2 · `vigente_sin_cambios`
13 (5 escalón 1 + 8 triage) · `modificada_por_v3` 1 · `candidata_nueva` 4 ·
`no_verificable` 0. (La entrada a y la E6 son el mismo defecto visto desde dos
orígenes; la adjudicadora decide si se fusionan.)

— Fin del expediente. Los laudos y la población efectiva del backlog son de la
adjudicadora; ningún nodo fue tocado. —
