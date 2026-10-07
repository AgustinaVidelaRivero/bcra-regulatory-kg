# FRENO — U-DIAG-CAP3-GRAFO

Solo lectura, USD 0, sin API ni Neo4j. HEAD `d007be8` al inicio y `f96ab49` al cierre: cinco commits ajenos. No
cambian ningún dato leído; del código, solo el ensamblado por R2-3, y leí todo en `d007be8`. Nada commiteado: el commit queda PENDIENTE de la autora.
Escribí solo en `reports/u_diag_cap3_grafo/` y en el scratchpad. Detalle en `REPORTE_UDIAG_CAP3_GRAFO.md`; cifras del
diez `a9631a64…` (sin cola `e22fae1a…`, en las tablas).

**a.1. Causas** (código sobre el crudo y los rechazos; lectura de 393 casos con criterio escrito antes, sha `e11a035b…`;
concordancia de una relectura a ciegas 22/25 en la causa):

| | (i) otra unidad | (ii) Operacion | (iii) otro rechazo | (iv) omisión | (v) otra | total |
|---|---:|---:|---:|---:|---:|---:|
| Excepcion | 77 | 48 | 31 | 49 | 51 | 256 |
| Condicion | 89 | 0 | 122 | 49 | 71 | 331 |

En el sin cola, Excepcion 252 y Condicion 322.
- Ninguna relación emitida se perdió después de validarse, y no hay casos «no visto por E3».
- La causa (i) está en los ítems: 49 de 77 y 60 de 89.
- El grupo que el código mandaba a (i) se confirmó solo en 78 de 138: 46 acotan una definición.
- Desglose por TO y por tipo de unidad: `salidas/tabla_a.md`.

**a.2.**
- **Regla E** (ítem → única norma admisible del encabezado): 35 uniones de Excepcion y 61 de Condicion. Precisión
  18/30, Wilson [0,423; 0,754]: **bajo el piso de 0,75**. Condicion 13/16, Excepcion 5/14.
- **Firma F:** 41 relaciones, 40 nodos, 21 unidades, **0 vistas por E3**, porque `validador_e1` usa la misma matriz.
  F14b no recupera ninguna. Recuperarlas pide F14: re-sellar la política y correr E3 en 21 unidades (≈ USD 0,21).
  La condición de la enmienda 8 se lee en el agregado (abajo). Una lectura previa mía, con el criterio opuesto, no
  cuenta: queda en `lecturas/previa_criterio_distinto/`, sin cifras acá, para que la mesa lea a ciegas.

**a.3. D1** (umbral: falsedad en campo estructurado; nada de esto lo alcanza salvo la procedencia, que se corrige
en código):
- **Corregir antes, en U-OMISIONES-COD:** G-r. H es opcional.
- **Límite declarado, con su cifra:**
  - E, causa (i): 77 + 89;
  - F, causa (ii): 48 en la tanda 0, que coincide con la opción (a) del borrador de la enmienda 8; regir desde la
    tanda 1 es decisión de la autora por esa enmienda;
  - causa (iii): 31 + 122;
  - causa (iv): 49 + 49;
  - causa (v): 51 + 71.
- **Forma A:** 60/953 Condicion de ítem en (i), del orden de 42/715 (la base es distinta, declarada). El límite del
  06/10 se sostiene.

**b.**
- De los 113, el rol está mal en 64; punto y rol son coherentes en 20 (tramo en el título); el punto apunta mal a la
  unidad en 18 (11 son normas compuestas del ítem) y a otro ancestro en 4; 7 no se ubican.
- **G-r** (solo cuando el modelo anclaba en un ancestro, antes de E2, fila F15): cambia el punto de 22 nodos
  (Operacion 9, Obligacion 8, Potestad 4, Restriccion 1) y solo el rol de 173; 0 fusiones. Leí los 22: 22/22
  coherentes.
- Acreditación: con A0.2 cambian 22 nodos; con §5.6, 145 pertenencias de unidades hermanas.
- G aplicada a todos los nodos movería 127 nodos de la unidad al ancestro: no la recomiendo (P3C-d2).

**e.**
- Con la definición vigente, el tablero se reproduce (35, 7, 42 y 0).
- Redefinida (sin `establecida_en` ni remisión; igual a «sin `condicion_de`»): r1 desarrollo 783 de 1.178, cinco
  101 de 205, diez r1 884 de 1.383; r2a 232 y 199; r2b 331 y 300; sin cola 322 y 292.
- El texto propuesto para la fila y para [c3] está en el reporte. No lo apliqué.

**Agregado a la tarea a: condición de la enmienda 8** (detalle en la sección final del reporte):
- Criterio sellado antes de generar las fichas: `criterio_41_exceptua_operacion.md`, sha `92688681…`, a las
  2026-10-07 18:39:26 -0300.
- 45 fichas sin veredicto (`fichas_41_exceptua_operacion.{json,md}`): las 41 del crudo, más M21, M23, M24 y M25 de
  U-ESTUDIO-MATRIZ, tomadas de su muestra sellada sin leer. M22 ya está entre las 41.
- Las 41 son de unidades aceptadas (0 de la cola) y E3 no vio ninguna (0 de 41): las rechazó `validador_e1`,
  `:506-510`.
- Primera lectura en un archivo aparte (`lectura1_41_exceptua_operacion.json`, sha `faed869a…`), con el
  ancla de cada veredicto en el texto. La hizo un lector que no vio la lectura previa.
- Horas: fichas a las 18:41:34; lectura a las 18:54:35. 45 de 45 anclas literales y 45 veredictos válidos.
- El denominador (41 o 45) queda PENDIENTE de la autora, según una nota posterior en la enmienda (ajena, sin
  commit). Las fichas EO01–EO41 son las del crudo, para que sirva cualquiera de los dos.
- **Sin cifra:** la cifra sale de la segunda lectura a ciegas de la mesa y de la adjudicación.

**Contradicciones (mandan los archivos).**
1. F no puede ser F14b: la matriz es una sola, la comparten los dos validadores y la fija la política con candado.
2. Las 33 otras firmas con origen Excepcion van a (iii), no a (ii).
3. La tabla de reprocesamiento cita el candado en `r1_e4.py:499`, también en `f96ab49`; está en `:536`.
4. Durante la unidad entró, ajeno, el borrador de la enmienda 8 a L-ESQ-R2 (esta misma firma; `f96ab49`). Ya
   dice F14 y F14b a la vez, coherente con lo medido acá; su definición de «correcta» es la opuesta a la mía (punto
   a.2).

**Errores y desvíos propios.**
1. Los dos ejemplos de calibración estaban en la parte 1 de los lectores.
2. Dos lectores escribieron un script auxiliar en el scratchpad (uno quedó, fuera del repo).
3. Una cifra de ext del primer borrador del reporte estaba sin computar. La corregí contra `tabla_a.json`: 139 y 149.
4. Un conteo por TO dependía de la semilla de hash. Lo corregí, y la reproducción da 26/26 iguales en dos corridas.
5. Esta sesión ya conocía una lectura previa de las 41, hecha con el criterio opuesto al de la enmienda. Por eso la
   primera lectura la hizo un lector nuevo, y la previa queda aislada y sin cifras.

**Para decidir:**
- si E entra con una regla más estrecha, que necesitaría una lectura nueva de 30 con piso 28;
- G-r y H en U-OMISIONES-COD;
- el texto de la fila e;
- la segunda lectura a ciegas de la mesa sobre `fichas_41_exceptua_operacion.*` y la adjudicación de las
  divergencias, que dan la cifra de la condición de la enmienda 8.

**Controles** (archivos en el paquete `revision_UDIAG_CAP3_GRAFO/`, con `manifest.txt`):
- sha256 de todo el repo (sin .git), antes y después: 61 archivos nuevos, todos en `reports/u_diag_cap3_grafo/`. Lo
  demás es ajeno: los cinco commits, la enmienda 8 y su nota posterior, los archivos de R2-3 bis y otros cambios
  sin commit, y los `.DS_Store` que desaparecieron sin que los tocara.
- `.pyc`: 2.213, la misma lista.
- Grep de convenciones: sin nombres ni rutas absolutas; 2 coincidencias de «correo», que son texto normativo citado
  en las fichas.
- Reproducción desde el repo, con las fichas y el control de anclas: 29/29 salidas iguales en dos corridas. En la
  primera, el git status cambió por archivos nuevos de R2-3 bis, ajenos; en la segunda no cambió.
