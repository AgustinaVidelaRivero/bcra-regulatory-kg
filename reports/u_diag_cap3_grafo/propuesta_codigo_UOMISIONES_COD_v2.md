# Propuesta de código para U-OMISIONES-COD v2: grupos E, F, G y H (U-DIAG-CAP3-GRAFO)

Propuesta, no implementación: nada de esto se escribió en el código del repo. Las anclas son de `d007be8`, el HEAD con
que trabajé. Durante la unidad entró R2-3 de U-RERESOL-CAT (`803623a`): en `f96ab49`, el HEAD al cierre,
`correr_cadena_r2` está 41 líneas más abajo. Equivalencias de `d007be8` → `f96ab49`: `:1234-1238` → `:1275-1279`,
`:1268` → `:1309`, `:1308` → `:1349`, `:1318` → `:1359`, `:1336` → `:1377`. La implementación de referencia de cada regla es la del script de esta unidad que se cita: lo que mide
el diagnóstico es lo que haría el código.

## Grupo E: unión de la Excepcion o la Condicion de un ítem con la norma del encabezado de su lista

- **Regla.** `udiag_a_union.py`, docstring y `medir()`. Para cada Excepcion sin `exceptua`/`exceptua_obligacion`
  saliente y cada Condicion sin `condicion_de` saliente cuya procedencia principal es un ítem (`prompt_r2b.es_item`),
  el destino es el único nodo de un tipo admisible con procedencia en el mini-chunk del bloque que abre la lista
  (`prompt_r2b.bloque_lista`): Excepcion → Restriccion (`exceptua`) u Obligacion (`exceptua_obligacion`);
  Condicion → Excepcion, Obligacion, Restriccion, Operacion o Potestad (`condicion_de`). Arista derivada con
  `rol_fuente = union_item_encabezado`, sin las marcas de E3 (no la vio E3). Con dos o más candidatos, ambigua; sin
  candidatos o sin mini-chunk (lista abierta por la línea de título), sin unión. Todas al registro.
- **Dónde.** `ensamblar_tanda0.correr_cadena_r2`, después del merge entre TOs (`:1268`) y antes de las aristas
  derivadas (`remite_a`, `:1308`; `establecida_en`, `:1318`). Necesita los chunks de E0 r2b (ya los carga la cadena).
- **Medido en a9631a64.** Excepcion de ítem sin vínculo 133: 35 uniones, 4 ambiguas, 79 sin norma en el encabezado,
  15 sin mini-chunk. Condicion de ítem sin vínculo 165: 61 uniones, 56 ambiguas, 44 sin norma, 4 sin mini-chunk.
  En e22fae1a: 34 / 4 / 78 / 15 y 58 / 55 / 44 / 4.
- **Precisión.** 30 uniones sorteadas (semilla 20261007): 18 correctas, 10 incorrectas, 2 dudosas; Wilson al 95 %
  [0,423; 0,754] (correctas). Por tipo: Condicion 13 de 16, Excepcion 5 de 14. **No llega al piso de 0,75 de
  L-ESQ-R2 §6.3** (con 30, 28 correctas). Fallas: la Excepcion exceptúa una parte del ítem (plazo, cómputo,
  condición), no la norma del encabezado (U1, U3, U27); el encabezado trae dos normas y la única de tipo admisible
  es la equivocada (U17, U22, U24); el nodo acota una definición (U6, U15, U21).
- **Fila de la tabla.** F15 (ensamblado, solo código sobre lo guardado). No mueve claves de E1 ni de E3.
- **Recomendación.** No entra con esta regla. Si la autora la quiere, una regla más estrecha (por ejemplo, solo
  Condicion, con destino Potestad, Excepcion u Operacion y encabezado que anuncia «las siguientes condiciones» o
  «requisitos») se fija por escrito antes de medir y se lee sobre una muestra nueva de 30 con el mismo piso. La
  observación de que las Condicion acertaron 13 de 16 es posterior al resultado y no sirve de evidencia.

## Grupo F: firma (Excepcion, exceptua, Operacion)

- **Cambio.** Agregar `("exceptua", "Excepcion", "Operacion")` a `AMPLIACION_R2` (`modelos_r2.py:130`) y a
  `campos.firma.ampliacion` de `politica_campos_r2.json` (el validador exige que coincidan, `validador_r2.py:120-121`).
- **Alcance real.** La matriz la usan los dos validadores: `validador_r2` y `validador_e1`, por
  `perfil_e1.py:225` (`firma_valida=M.firma_r2`). Los 41 rechazos `(Excepcion, exceptua, Operacion)` cayeron ya en
  `validador_e1`, antes de E3: **0 de 41 los vio E3**. Con solo el validador r2 (F14b), la firma pasaría y la
  relación caería después en el filtro de «lo que E3 no vio no entra» (`validador_r2.py:1301-1304`): **no recupera
  ninguna**. Recuperarlas pide F14: re-sellar la política (candados `validador_e1.py:102` y `r1_e4.py:536`; la tabla de reprocesamiento cita `:499` en sus líneas 98, 169 y 273,
  también en `f96ab49`: ancla vieja) y
  volver a correr E3 en las unidades afectadas, o una excepción escrita a la regla de lo no visto por E3.
- **Medido.** 41 rechazos `exceptua`, 40 nodos Excepcion, 21 unidades (cla 7, ext 7, ctacte 4, cap 3;
  `salidas/tabla_a.json`, `firma_f.solo_exceptua`); 0 en la cola. Con F14, E3 de esas 21 unidades: 21 × 0,010226 ≈
  USD 0,21 a la tarifa de E3 de la tabla §5 (`tabla_reprocesamiento.md:419`), más los reintentos que dispare. Además 1 `exceptua_obligacion → Operacion` y 1 `condicion_de → Operacion` con origen Excepcion.
- **Fila.** F14, y cambio del esquema (L-ESQ-R2 fija la matriz): necesita enmienda firmada.
- **Condición de la enmienda 8.** La lectura de las 41 con su criterio sigue su protocolo: fichas
  `fichas_41_exceptua_operacion.*`, primera lectura de esta unidad, y luego la segunda lectura de la mesa y la
  adjudicación de la autora. Una lectura previa de esta unidad, con el criterio opuesto, no cuenta
  (`lecturas/previa_criterio_distinto/`).
- **Recomendación.** En la tanda 0, límite declarado: E3 no las vio. Regir desde la tanda 1 es decisión de la autora
  por la enmienda 8, que ya la clasifica como F14 y F14b a la vez (ver la clasificación D1 del reporte).

## Grupo G: procedencia por tramo

- **Regla (G-r, la recomendada).** `udiag_b_procedencia.correccion_g(p, ch, restringida=True)` y `ubicar()`. Solo
  para los elementos cuyo `punto` es un ancestro de su unidad: con `verificar_tramo` del validador (holgura 2 de la
  política), `punto` = la unidad si su texto propio contiene el tramo (o el segmento del ítem de un tramo compuesto
  «encabezado […] ítem»: la norma compuesta del ítem, P3C-d2); si no, el ancestro cuyo bloque heredado lo contiene,
  con `rol_documental` = el tipo de ese bloque (`herencia_intro`, `herencia_cierre`, `herencia_intersticial`,
  `herencia_encabezado`; en el cruce de título y párrafo, el del párrafo); si el tramo no se ubica, sin cambio.
- **Dónde.** Sobre los registros de `entrada_r2`, antes de E2 (`ensamblar_tanda0.py:1235-1238`), para que el id
  (la clave de fusión r2b incluye el punto, `e2_lib.entity_slug_r2`) y la procedencia queden de acuerdo. No en
  `comun_e1.rol_documental_de_punto`: esa función la usa también `validador_e1`, y cambiarla tocaría la salida que ve
  E3 (F14).
- **Medido en a9631a64.** Cambian el punto 22 nodos (18 al ítem, 4 a otro ancestro; Operacion 9, Obligacion 8,
  Potestad 4, Restriccion 1), solo el rol 173 (139 a `herencia_intro`, 28 a `herencia_cierre`, 6 a
  `herencia_intersticial`), 0 ids que se fusionen con un nodo existente. Lectura de los 22 cambios de punto: 22 de
  22 coherentes con el tramo.
- **Variante literal (G aplicada a todos los nodos).** Cambiaría el punto de 149 nodos, 127 de la unidad a un
  ancestro (113 de ítems: la norma compuesta del ítem con el tramo copiado del encabezado), y fusionaría 7 ids. No se
  recomienda: contradice P3C-d2 (la norma compuesta es del ítem).
- **Fila.** F15 («procedencia», entre lo que cubre). Solo código.

## Grupo H: `tipo_normalizado` de la Operacion

- **Regla.** `udiag_h_tipo_operacion.tipo_normalizado`: minúsculas, sin diacríticos (NFKD, como `validador_r2.fold`),
  todo lo que no es letra o dígito a espacio, espacios colapsados. Se agrega `tipo_normalizado` y se conserva
  `tipo`.
- **Dónde.** En el ensamblado, junto con el resto de las propiedades derivadas (por ejemplo, después de
  `enriquecer_procedencias_r2`, `:1336`).
- **Medido en a9631a64.** 1.824 Operacion con `tipo`: 1.050 valores distintos; 943 en minúsculas; 942 sin
  diacríticos; 942 con la normalización entera. 704 de los 942 aparecen en un solo nodo. La grafía explica 108 de
  los 1.050; el resto es la variedad del texto libre.
- **Fila.** F15. No cambia la navegación del agente (busca en etiqueta y descripción).
- **Recomendación.** Barata y sin riesgo, pero casi no reduce la variedad: entra solo si la autora quiere la
  propiedad para las cifras del capítulo 3; la lista cerrada de tipos es cambio de tool schema (F07) y queda para la
  release posterior a la evaluación.
