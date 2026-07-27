# Informe — Deslinde existencia-vs-alcance de las fallas adjudicadas de v2 (2026-07-27)

**Resultado: de los 7 datos-clave examinados en `grafo_v2/kg.json` (EV1-039 omitida, ya confirmada), 2 EXISTEN en el grafo (EV1-015, EV1-018 → capa índice/alcance) y 5 están AUSENTES o amputados (EV1-031, EV1-042, EV1-028, EV1-011, EV1-005 → capa extracción/completitud). En la falla compartida EV1-018 el dato existe en AMBOS brazos; en EV1-011 el contenido es asimétrico (run_3 tiene el nivel definido, v2 no). Los 5 nodos rol del esqueleto tienen grado ≫ 40; en las trazas fallidas de 015/031 el agente nunca consultó un nodo rol (5/6 trazas agotaron el límite de 15 tools).** Solo lectura, sin API, sin commits. Números sin lectura contra predicciones.

Método: búsqueda normalizada (NFD sin diacríticos, minúsculas) sobre label + todas las properties string de cada nodo; grado = aristas incidentes (in+out).

## 1. Existencia por dato-clave

| Falla | Dato-clave buscado | Veredicto | Capa |
|---|---|---|---|
| EV1-015 | "residentes en el exterior" + clasificar (criterio 1.1) | **EXISTE** | índice/alcance |
| EV1-031 | 75 × Salario Mínimo (2.8.3.3) | **AUSENTE** | extracción/completitud |
| EV1-042 | "anterioridad no mayor" / "3 (tres) días hábiles" (3.5.3) | **AUSENTE** | extracción/completitud |
| EV1-018 | lista del 4.1.4 (juegos de azar / criptoactivos / tarjetas de regalo) | **EXISTE (los 3)** | índice/alcance |
| EV1-028 | salvedad "mutuales o cooperativas" (1.1.2.5) | **AUSENTE** | extracción/completitud |
| EV1-011 | niveles nominados del 6.5 | **AUSENTE como enumeración** (2 nombres solo incidentales) | extracción/completitud |
| EV1-005 | calificadores "informada en el mes n" / "calculada según datos del mes n" (7.1 RI) | **PARCIAL** (nodo existe, calificadores amputados) | extracción/completitud |

### Detalle con nodos y excerpts

**EV1-015 — EXISTE.** `Obligacion_clasificar_deudores_por_calidad`: "…tanto residentes en el país de los sectores público y privado, financieros y no financieros, como **residentes en el exterior**, por las financiaciones comprendidas, **deberán ser clasificados** desde el punto de vista de la c…". Observación de registro: su provenance ancla en **Punto 10.4** (Proveedores de servicios de créditos entre particulares…), no en el 1.1. Segundo hit (`Excepcion_se_excluyen_de_clasificacion_como_deficientes…`, 6.5 parte 5) es otro instituto (compraventa de títulos con residentes en el exterior), no el criterio general.

**EV1-031 — AUSENTE.** 0 hits para "salario mínimo"; la sonda ampliada "salario" da **0 hits en todo el grafo**: el límite de 75 SMVM del 2.8.3.3 no está en ningún nodo.

**EV1-042 — AUSENTE.** 0 hits para "anterioridad no mayor" y para "3 (tres) días hábiles": la ventana del 3.5.3 no está. (Consistente con la falla ratificada; el dato de la key fue verificado verbatim contra el PDF en la adjudicación.)

**EV1-018 — EXISTE (los 3 ítems).** `Restriccion_la_participacion_en_juegos_de_azar_…requiere_conformi…`, `Restriccion_la_adquisicion_de_criptoactivos_…` y `Restriccion_la_adquisicion_de_tarjetas_de_regalo_…`, los tres con provenance "Punto 4.1. Operaciones con débito en una cuenta…". La lista del 4.1.4 está nodificada ítem por ítem.

**EV1-028 — AUSENTE.** "mutuales o cooperativas": 0 hits. Sondas de control: "mutual" **0 hits en todo el grafo**; "cooperativa" solo aparece en CapMin (cajas de crédito cooperativas, 1.2). La salvedad del 1.1.2.5 no está. (Coincide con lo que el verificador halló en run_3: tampoco allá hay nodo con la salvedad.)

**EV1-011 — AUSENTE como enumeración.** "seguimiento especial": **0 hits en v2**. "con problemas" y "alto riesgo de insolvencia" aparecen solo como referencias incidentales dentro de nodos de recategorización del 6.5 partes 2-3 (`Obligacion_los_deudores_que_incurran_en_atrasos_de_mas_de_31_dias…` → "recategorizados en el nivel inmediato inferior 'con problemas'"; `Restriccion_mantenga_arreglos_privados…` → "niveles 'con alto riesgo de insolvencia' o 'irrecuperable'"). La enumeración nominada del 6.5 no existe como dato.

**EV1-005 — PARCIAL (amputación dentro de nodo existente).** `Obligacion_para_el_calculo_del_importe_correspondiente_al_mes_n_procedera_tenerse_en_cuenta` (7.1 RI) porta el esquema con "…Responsabilidad Patrimonial Computable, **Franquicia informada en el mes n**" — pero "calculada según datos del mes n" da 0 hits: los calificadores por componente quedaron amputados en la descripción (solo la franquicia conserva el suyo).

## 2. Falla compartida (EV1-018, EV1-011): ¿ausente en ambos brazos?

- **EV1-018 — NO es ausencia en ninguno.** En run_3 los 3 ítems también existen (`Operacion_participacion_en_juegos_de_azar`, criptoactivos en 3 nodos del 3.16/4.1, `Operacion_adquisicion_de_tarjetas_de_regalo`, todos anclados en el 4.1). El dato existe en AMBOS brazos y ambos fallaron por no-respuesta (laudo: repiten la premisa sin listar operación alguna).
- **EV1-011 — contenido asimétrico.** run_3 SÍ tiene el nivel "seguimiento especial (en observación)" definido (`Obligacion_para_clasificacion_con_seguimiento_especial_en_observacion_…`, 6.5 parte 1) además de las mismas referencias incidentales a "con problemas" y "alto riesgo de insolvencia"; v2 no tiene ninguna definición nominada. La falla es compartida pero el sustrato difiere: en v2 falta más contenido que en run_3.

## 3. Nodos rol y límite-40 (dato solicitado como evidencia P4 — sin lectura de la predicción)

**Grado de los 5 nodos rol del esqueleto (límite de ver_vecinos = 40):**

| Nodo rol | Grado |
|---|---|
| Sujeto_rol_alcance_capmin | **655** |
| Sujeto_rol_entidad_autorizada_exterior | **523** |
| Sujeto_rol_obligado_a_clasificar_clasificacion | **174** |
| Sujeto_rol_sujeto_obligado_proteccion | **162** |
| Sujeto_rol_entidad_comprendida_reginf | **142** |

Los 5 superan el límite 40: cualquier `ver_vecinos` sobre un rol trunca (devuelve 40 de N vecinos).

**Trazas fallidas de EV1-015 y EV1-031 (v2, 6 trazas):** el agente **no consultó ningún nodo rol** (input) en ninguna de las 6; el único nodo Sujeto consultado fue `Sujeto_cliente` (nivel clase, grado 15; EV1-015 r1). En EV1-015 el rol `Sujeto_rol_obligado_a_clasificar_clasificacion` (grado 174) **apareció en outputs de búsqueda en las 3 réplicas y el agente nunca lo abrió**; en EV1-031 ningún rol apareció siquiera en outputs. `hit_tool_limit` (15 tools agotadas): EV1-015 r1/r2 sí, r3 no; EV1-031 las 3 → **5/6 trazas al límite**.

## Alcance

`kg.json` de ambos brazos solo lectura; búsquedas reproducibles (normalización NFD + lowercase sobre label+properties); trazas leídas de `posthoc_run/traces/escalon1_r{1,2,3}/grafo_v2/`. Sin veredicto de capa final para EV1-039 (omitida por mandato, ya confirmada como nodos cruzados).

**FRENO acá.**
