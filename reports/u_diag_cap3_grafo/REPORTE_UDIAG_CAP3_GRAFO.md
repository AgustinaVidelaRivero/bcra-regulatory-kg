# U-DIAG-CAP3-GRAFO — reporte (tareas a, b y e; propuesta para U-OMISIONES-COD v2; clasificación D1)

Diagnóstico de solo lectura, USD 0, sin API ni Neo4j. HEAD `d007be8` al inicio y `f96ab49` al cierre: cinco commits
ajenos en el medio (`c957089`, `803623a`, `2185807`, `571de44`, `f96ab49`), que no cambian ningún dato leído. Del código
leído cambian `ensamblar_tanda0.py` y una línea de `runner_corpus.cerrar_e2_r2`, los dos por R2-3, `803623a`. No cambia
`entrada_r2`, que es lo que usé. Leí todo en `d007be8`. Fuentes extraídas con `git show d007be8:<ruta>`
a una copia en el scratchpad, sin enlaces. Grafos: KG-Tanda0-Diez-r2b `a9631a64…` (8.816 nodos) y su sin cola
`e22fae1a…`, con el sha comprobado por cada script. Punto de partida: los cuatro scripts de VERIF-CAP3-COHERENCIA
(su regla de la tarea d está copiada en `udiag_b_procedencia.clase_verif` y reproduce 109/61/23/7/22).

Cifras principales sobre el diez; las del sin cola, en las tablas. Comandos: `scripts/comandos_udiag_cap3_grafo.sh`.

## Método de la tarea a, y quién leyó

1. **Código** (`udiag_a_casos.py`). Para cada Excepcion sin `exceptua`/`exceptua_obligacion` saliente (256) y cada
   Condicion sin `condicion_de` saliente (331) reconstruyo su origen: el id que E2 r2b da a cada entidad validada
   (`e2_lib.entity_slug_r2`, tomado por AST) mapea los 8.510 nodos de contenido sin faltantes ni sobrantes. Leo el
   crudo que entra a E2 (`runner_corpus.entrada_r2`: el del intento que aceptó E3), los rechazos guardados y los
   índices que vio E3. Si la relación hacia la regla se emitió, la causa sale del rechazo; si no, la unidad decide
   si hay que leer.
2. **Lectura**, con un criterio escrito antes de leer (`lecturas/criterio_lectura_a.md`, sha `e11a035b…`):
   - los 255 que el código no decide: cuatro instancias lectoras, una parte cada una;
   - los 138 que el código mandaba a la causa (i) porque la unidad no extrajo ningún nodo de un tipo admisible.
     El control de 30 confirmó (i) solo en 13 (Wilson [0,274; 0,608]); por eso leí los 108 restantes y la cifra
     final sale de la lectura de los 138.
3. **Concordancia.** Releí a ciegas 25 de los 255 (semilla 20261008): mismo código 20/25 [0,609; 0,911], misma causa
   22/25 [0,700; 0,958]. En los tres desacuerdos, el código de duda de cada lector es el del otro.

Es lectura asistida (instancias de modelo de esta sesión) y queda para la revisión de la autora.

**Declaro tres cosas.**
- Los dos ejemplos de calibración del pedido a los lectores (casos 1 y 2) estaban en la parte 1, aunque el pedido
  decía que no: esas dos lecturas no son independientes.
- Dos lectores escribieron un script auxiliar en el scratchpad, fuera de su archivo de salida. Uno lo borró. El otro
  quedó en `scratchpad/arma_lectura_a_parte3.py`, fuera del repo.
- Una copia de respaldo mía falló por una ruta mal escrita. La comparación se hizo igual, por sha: la unión por script
  de las cuatro lecturas da el mismo `c5133855…` que la unión a mano.

## Tarea a.1 — desglose por causa (diez)

| | (i) regla en otra unidad | (ii) la regla es una Operacion | (iii) emitida, cayó por otro rechazo | (iv) nunca emitida, regla en la unidad | (v) otra | total |
|---|---:|---:|---:|---:|---:|---:|
| Excepcion | 77 | 48 | 31 | 49 | 51 | 256 |
| Condicion | 89 | 0 | 122 | 49 | 71 | 331 |

Sin cola (e22fae1a): Excepcion 75 / 48 / 31 / 47 / 51 = 252; Condicion 86 / 0 / 121 / 46 / 69 = 322.

**Excepcion.**
- (i): 19 con la regla en un bloque heredado (I-ENC) y 58 fuera de la herencia (I-OTRA).
- (ii): 41 emitidas y rechazadas por firma hacia Operacion, más 7 que el modelo no emitió con la regla Operacion en la
  unidad.
- (iii): 26 rechazadas por firma hacia otro tipo (12 `exceptua → Condicion`) y 5 con el destino no emitido.
- (iv): 30 IV-OMI y 19 IV-NOEXT; IV-NOEXT es la regla extraída como Condicion u otro tipo sin firma.
- (v): 37 acotan una definición (V-DEF) y 14 son otra cosa (V-OTRA).

**Condicion.**
- (i): 67 I-ENC y 22 I-OTRA.
- (iii): 85 por firma. Se reparten en 37 `condicion_de → Definicion`, 30 `condiciona` hacia Obligacion, Operacion o
  Restriccion, 12 `condicion_de → Condicion` y 6 más. Otras 37 tienen el destino no emitido (`ref_colgante`: apuntan
  a un `local_id` que no existe, lo que P3C-d1 prohíbe).
- (iv): 37 IV-OMI y 12 IV-NOEXT.
- (v): 43 V-DEF y 28 V-OTRA.

Nada cae en «emitida y validada pero perdida» ni en «no la vio E3»: toda relación emitida que falta se rechazó.
En 6 Excepcion y 5 Condicion la relación aparece en un intento no aceptado.

**Cruce con los rechazos de VERIF.**
- Las 41 `(Excepcion, exceptua, Operacion)` están todas en las 256: 40 nodos, uno con dos.
- De las 33 otras firmas con origen Excepcion, 31 caen en las 256 y 2 en Excepcion que sí tienen su vínculo.
- De las 95 firmas rechazadas con origen Condicion, 87 caen en las 331.

**Por tipo de unidad** (Excepcion / Condicion; ítem = `prompt_r2b.es_item`):

| | ítem | punto no ítem | intro | cierre | otros | total |
|---|---:|---:|---:|---:|---:|---:|
| Excepcion | 133 | 93 | 19 | 9 | 2 | 256 |
| Condicion | 165 | 123 | 34 | 7 | 2 | 331 |

La causa (i) está concentrada en los ítems: 49 de 77 en Excepcion y 60 de 89 en Condicion. La tabla completa, por
causa × tipo de unidad y por causa × TO, está en `salidas/tabla_a.md`: ext concentra 139 de 256 y 149 de 331.

## Tarea a.2 — ¿se puede unir en código, sin re-extraer?

**(i), regla E** (`udiag_a_union.py`). Une el nodo del ítem con el único nodo admisible del mini-chunk que abre su
lista.

| | sin vínculo, en ítems | uniones | ambiguas | sin norma en el encabezado | sin mini-chunk (lista abierta por la línea de título) |
|---|---:|---:|---:|---:|---:|
| Excepcion | 133 | 35 | 4 | 79 | 15 |
| Condicion | 165 | 61 | 56 | 44 | 4 |

Variantes:
- Con la firma F, las Excepcion se vuelven ambiguas: 16 uniones y 27 ambiguas.
- Si en la Condicion manda la Excepcion única del encabezado: 80 uniones.
- La variante estricta (solo si el ítem no extrajo ningún destino admisible) da 18 y 45 uniones.

**Lectura de control de 30 uniones** (semilla 20261007, leídas por mí): 18 correctas, 10 incorrectas y 2 dudosas;
Wilson [0,423; 0,754]. **No llega al piso de 0,75 de L-ESQ-R2 §6.3** (con 30, 28 correctas). Por tipo: Condicion
13 de 16, Excepcion 5 de 14. Hay tres formas de error:
- la Excepcion exceptúa una parte del ítem (un plazo, un cómputo, una condición), no la norma del encabezado;
- el encabezado trae dos normas y la única admisible es la equivocada (el deber de nominar una entidad, frente a la
  facultad de certificar);
- el nodo acota una definición.

Las uniones no caen solo sobre la causa (i): de las 35 de Excepcion, 15 son (i); de las 61 de Condicion, 20 son (i)
y 36 son (iii).

**(ii), firma F.**
- Son 41 relaciones, 40 nodos, 21 unidades (cla 7, ext 7, ctacte 4, cap 3) y 0 en la cola.
- **E3 no vio ninguna de las 41:** `validador_e1` ya las había rechazado por firma, porque usa la misma matriz
  (`perfil_e1.py:225`, `firma_valida=M.firma_r2`).
- Habilitar la firma solo en `validador_r2` (F14b) no recupera ninguna: la firma pasaría y la relación caería en el
  filtro de lo no visto por E3 (`validador_r2.py:1301-1304`).
- Recuperarlas pide F14: re-sellar la política (la ampliación de la matriz está en `politica_campos_r2.json`, con
  candado en `validador_r2.py:120-121`, `validador_e1.py:102` y `r1_e4.py:536`) y volver a correr E3 en las 21
  unidades. A la tarifa de E3 de la tabla §5, son 21 × 0,010226 ≈ USD 0,21, más los reintentos que dispare.
- **Condición de la enmienda 8.** La lectura de las 41 que pide su §2 está en la sección final (agregado a la
  tarea a): criterio sellado, fichas sin veredicto y primera lectura en un archivo aparte. La cifra sale después de la
  segunda lectura a ciegas de la mesa y de la adjudicación de la autora.
- **Una lectura previa de esta unidad no cuenta.** Antes del agregado leí las 41 como control de F, con un criterio de
  «correcta» opuesto al del §2: para mí, que la Operacion fuera lo que queda afuera era incorrecto. Queda en
  `lecturas/previa_criterio_distinto/`, con un aviso para que la mesa no la abra antes de su segunda lectura, y sin
  cifras en este reporte ni en el FRENO.

**Contradicción con el despacho (mandan los archivos).** El despacho supone que F puede ser F14b si toca solo la
matriz del validador r2. No puede: la matriz es una sola y la comparten los dos validadores.

## Tarea a.3 — clasificación D1

Umbral de D1 (protocolo entre tandas §6 (c), `a304b89`): falsedad en campo estructurado en material fresco. Una
omisión visible con tasa medida queda como residuo declarado y no abre el procedimiento.

| parte | cifra (diez) | fila | D1 |
|---|---|---|---|
| G-r, procedencia por tramo | 22 puntos y 173 roles, 0 fusiones, 22/22 coherentes | F15 | **corregir antes** (grupo G): la procedencia es un campo estructurado con valor falso, y G-r lo corrige sin cambiar prefijo ni esquema |
| H, `tipo_normalizado` | 1.050 → 942 valores | F15 | opcional; no toca la evaluación |
| E, unión ítem–encabezado | 35 + 61 uniones; 18/30 [0,423; 0,754] | F15 | **no entra como está**: bajo el piso. **Límite declarado** de la causa (i): 77 Excepcion y 89 Condicion, de ellas 49 y 60 en ítems |
| F, firma Excepcion→Operacion | 41 relaciones, 0 vistas por E3 | F14 y cambio de esquema | **en la tanda 0, límite declarado** de (ii): 48 Excepcion. Recuperarlas pide E3 de 21 unidades. Es omisión, no falsedad: no llega al umbral de (c). Por la letra de la regla (a), el cambio de esquema va después de B6.3, salvo la enmienda de la autora: el borrador 8 propone que rija desde la tanda 1, con la condición de su §2 pendiente |
| (iii) firma hacia otro tipo, destino no emitido | Excepcion 26 + 5; Condicion 85 + 37 | prompt o esquema | **límite declarado**. Los 30 `condiciona` desde Condicion son un predicado equivocado: corregirlos en el validador es F14, como F. Los 37 `condicion_de → Definicion` piden una firma que no existe |
| (iv) omisión del modelo | 49 + 49 | prompt | **límite declarado** (regla (a)) |
| (v) no une a una regla | 51 + 71 (V-DEF 37 + 43) | — | **límite declarado**. No es un defecto de unión: las condiciones y exclusiones de una definición no tienen firma en la matriz |

**Relación con T4 y con la forma A.**
- **Forma A.** En los ítems, la causa (i) de Condicion es 60 de 953 Condicion de ítem (0,063). Es del mismo orden que
  la forma A declarada LÍMITE: 42 de 715 (0,059, `data/experiment/reext_t0/t3bis/salida/controles_t3bis.json`, `e_forma_A`). Las bases son distintas: T3
  cuenta entidades validadas y define el ítem por el último bloque terminado en «:»; acá cuento nodos y uso
  `bloque_lista`. La decisión del 06/10 (límite, sin mandato) se sostiene: E tampoco pasa el piso, como VU-B.
- **T4, punto 6.** La causa (i) es la conducta que el prompt pide: P3C-b1 manda que la Excepcion vaya sin `exceptua`
  cuando la norma está en otra unidad, y P3C-d1 y P3C-d2 prohíben re-emitir la norma en el ítem. En b2, la regla E
  con destino Excepcion acertó 3 de 3 en la muestra (U9, U12, U19), pero son pocas para medir.
- **T4, grupo c.** Lo que acá es Condicion sin `condicion_de` corresponde a «sin relación» (8 de 137). «Dentro de una
  norma» (77 de 137, `data/experiment/reext_t0/reporte_u_reext_t0.md:80`) no aparece en las 331, porque no hay nodo Condicion.

## Tarea b — procedencia hacia un ancestro

Reproduje la regla de VERIF: 222 nodos = 109 en el párrafo + 61 que cruzan título y párrafo + 23 en el título + 7 en
el texto propio + 22 no ubicados. Los 113 de afuera del párrafo, con `verificar_tramo` del validador (holgura 2;
tramo compuesto «encabezado […] ítem» por su segmento del ítem):

| diagnóstico | cruza título y párrafo | título | texto propio | no ubicado (VERIF) | total |
|---|---:|---:|---:|---:|---:|
| rol mal (debería ser el párrafo heredado) | 61 | 3 | 0 | 0 | 64 |
| punto y rol coherentes (tramo en el título del ancestro) | 0 | 20 | 0 | 0 | 20 |
| punto mal atribuido: a la unidad | 0 | 0 | 7 | 11 | 18 |
| punto mal atribuido: a otro ancestro | 0 | 0 | 0 | 4 | 4 |
| no ubicado | 0 | 0 | 0 | 7 | 7 |

- De los 18 «a la unidad», 11 son la norma compuesta del ítem: tramo «encabezado […] ítem», que VERIF no ubicaba.
- Los 7 no ubicados tienen `tramo_verificado = no` en el grafo: tampoco los verificó el validador (guion sin salto
  de línea, paráfrasis entre corchetes, tramos que cruzan bloques).
- Los 20 casos están en `salidas/casos_b_20.md`, estratificados con la semilla 20261007.

**Corrección G-r.** Solo para los elementos que el modelo anclaba en un ancestro: `punto` por el tramo y `rol` por el
bloque que lo contiene.
- En los 222: cambia el punto en 22 (18 al ítem, 4 a otro ancestro; Operacion 9, Obligacion 8, Potestad 4,
  Restriccion 1), solo el rol en 173 (139 a `herencia_intro`, 28 a `herencia_cierre`, 6 a `herencia_intersticial`) y
  nada en 27.
- 0 ids se fusionan con otro nodo.
- Leí los 22 cambios de punto: 22 de 22 son coherentes con el tramo; Wilson [0,851; 1,0].

**G literal sobre los 8.510.** Cambiaría el punto de 149 nodos y fusionaría 7 ids. 127 de esos cambios van de la
unidad a un ancestro, y 113 de ellos son de ítems: la norma compuesta con el tramo copiado del encabezado. No la
recomiendo, porque contradice P3C-d2.

**Efecto en la acreditación.**
- Por `punto` exacto (A0.2), G-r cambia la unidad acreditable de 22 nodos: Operacion 9, Obligacion 8, Potestad 4,
  Restriccion 1. En el sin cola son 19.
- Con el subgrafo del pre-registro de tripletas (§5.6), que incluye ancestros y descendientes, la pregunta sobre el
  ítem ya veía esos nodos. Lo que cambia es que dejan de entrar en los subgrafos de las unidades hermanas: 145
  pertenencias menos.
- Fila: F15 («procedencia»), solo código.
- Sitio: sobre los registros de `entrada_r2`, antes de E2, porque la clave de fusión incluye el punto. No en
  `comun_e1.rol_documental_de_punto`, que también usa `validador_e1`: tocarla movería lo que ve E3 (F14).

## Tarea e — condiciones aisladas

Con la definición vigente (grado 0, `scripts/metricas_intrinsecas.py:243`), las cifras del tablero se reproducen
igual: 35, 7, 42 y 0. En r2 la cifra es 0 por construcción. La meta del laudo de r2 §4 (`docs/laudo_release_r2_pipeline.md:332`)
dice «cero nodos de contenido sin `establecida_en`» y la derivación la implementó la decisión 11 de U-R2-CODIGO
(`docs/mandatos/UR2CODIGO_correcciones_en_codigo.md:204`).

| grafo | Condicion | vigente | redefinida (A) = sin `condicion_de` (B) |
|---|---:|---:|---:|
| desarrollo r1 | 1.178 | 35 | 783 |
| cinco r1 | 205 | 7 | 101 |
| diez r1 | 1.383 | 42 | 884 |
| diez r2a / desarrollo r2a | 1.409 / 1.203 | 0 / 0 | 232 / 199 |
| diez r2b / desarrollo r2b | 1.952 / 1.668 | 0 / 0 | 331 / 300 |
| sin cola diez / desarrollo | 1.868 / 1.588 | 0 / 0 | 322 / 292 |

KG-Reextraído-r1 no tiene Condicion. (A) y (B) coinciden en los diez grafos.

Para que la columna del perfil r1 sea comparable, (A) excluye también la remisión en su forma anterior: `referencia`
con `rol_fuente = referencia_cruzada`. Sin esa exclusión, en los grafos r1 da 560, 79 y 639 (`salidas/tabla_e.md`).

**Texto propuesto para la fila** (no aplicado; `docs/tablero_correcciones.md:52`):

> **Condiciones sin regla** (antes «Condiciones aisladas») | Nodos Condicion sin ninguna arista de contenido: no se
> cuentan `establecida_en` ni la remisión (`remite_a`; en los grafos del perfil r1, `referencia` con `rol_fuente =
> referencia_cruzada`). Con la matriz vigente es lo mismo que «sin `condicion_de` saliente». Al lado, aislados por
> tipo, de grado 0 [c3] | No aplica: 0 Condicion; aislados 105 | desarrollo 783 de 1.178 (aislados 94, de ellos 35
> Condicion); cinco 101 de 205 (38; 7); diez 884 de 1.383 (120; 42) | Laudo de r2 §4: cero nodos de contenido sin
> `establecida_en` (cumplida); el resto, declarado por causa (U-DIAG-CAP3-GRAFO, tarea a) | … | r2a: 232 de 1.409 en
> diez y 199 de 1.203 en desarrollo | r2b: 331 de 1.952 y 300 de 1.668; sin cola, 322 de 1.868 y 292 de 1.588 | |

**Agregado a [c3]:** «Condiciones sin regla: nodos Condicion cuyas aristas únicas, entrantes y salientes, son todas
`establecida_en`, `remite_a` o `referencia` con `rol_fuente = referencia_cruzada`; comando
`reports/u_diag_cap3_grafo/scripts/udiag_e_aisladas.py`».

## Otras observaciones

1. Ancla vieja: la tabla de reprocesamiento cita el candado de la política en `r1_e4.py:499` (líneas 98, 169 y 273,
   en `d007be8` y en `f96ab49`). El candado está en `:536`.
2. El despacho pone las 33 otras firmas con origen Excepcion en la causa (ii). Las cuento en (iii), porque su
   destino no es una Operacion.
3. `ensamblar_tanda0.py` cambió durante la unidad (R2-3, `803623a`). La propuesta cita las líneas en `d007be8` y su
   equivalencia en `f96ab49`.

## Agregado a la tarea a — condición del §2 de la enmienda 8 a L-ESQ-R2

Enmienda leída entera en `f96ab49`: `data/experiment/esq/enmienda8_L-ESQ-R2_exceptua_operacion_2026-10-07.md`, 66
líneas, sha `13d13f0d…`, igual en el árbol.

1. **Criterio sellado antes de generar ninguna ficha.** Archivo `criterio_41_exceptua_operacion.md`, sha
   `92688681fbc59bf0caf1875e43d315bc6a610130e34f452064cd135728692fbf`, sellado el 2026-10-07 a las 18:39:26 -0300
   (`sello_criterio_41_exceptua_operacion.txt`). Es el criterio del mandato, transcripto:
   - correcta: la Excepcion exime a esa Operacion, que es lo que queda afuera;
   - incorrecta: el texto alcanza y la relación no es correcta;
   - no decidible: el texto no alcanza.
   Cada veredicto lleva su ancla en el texto. Piso: Wilson inferior ≥ 0,75 sobre las decididas (37 de 41) y no
   decidibles ≤ 6.
2. **Población: 45 fichas.**
   - EO01 a EO41 son las 41 del crudo de KG-Tanda0-Diez-r2b, con su unidad, la Excepcion, la Operacion y el índice de
     la relación en el crudo.
   - EO42 a EO45 son M21, M23, M24 y M25 de U-ESTUDIO-MATRIZ. Las tomé de la muestra sellada sin leer (`7e72051`,
     sha `09efc7e5…`, el mismo que declara su resultado), sin veredictos. Vienen de la réplica de
     KG-Tanda0-Desarrollo-r1 (`eab2fdd0`) y no tienen tramo.
   - M22 no entra: es la misma relación que una de las 41, en `cla::6.5.5.8` (Excepcion de los pases activos en
     dólares → Operacion de clasificación en Irrecuperable).
3. **Estado de las 41.**
   - Las 41 unidades son aceptadas, ninguna de la cola: 29 `aceptado_con_residuales`, 10 `completo_ok_directo` y 2
     `aceptado_tras_reintento`.
   - El crudo que entra a E2 es el intento 0 en 39 y el reintento en 2.
   - **E3 no vio ninguna (0 de 41).** Las 41 caen en `validador_e1` por `firma_invalida` (`validador_e1.py:506-510`
     en `d007be8`; el mandato cita `:505-510`).
4. **Fichas sin veredicto.** `fichas_41_exceptua_operacion.json` (sha `08fe64a2…`) y `.md` (sha `d332228f…`). Cada
   ficha trae:
   - el texto propio y el heredado de la unidad, con ⟦E: …⟧ y ⟦O: …⟧ marcados (41 de 41 tramos de Excepcion y 41 de
     41 de Operacion, ubicados con la verificación de tramo del validador);
   - la Excepcion y la Operacion con descripción, tramo y punto;
   - la relación rechazada, con su índice y los rechazos de los dos validadores;
   - la instrucción del prefijo: P3B-c1 con P3C-d1, el texto que aparece literal en los pedidos guardados en las
     cachés de C1 de U-COMP-E1.
   Generador: `scripts/udiag_a_fichas41.py`. La versión vigente es de las 18:41:34. Hubo una generación previa en el
   mismo minuto, sin la clave `crudo_que_entra_a_e2` en las 4 de la muestra; las 41 fichas del crudo son iguales en
   las dos.
5. **Primera lectura**, en un archivo aparte: `lectura1_41_exceptua_operacion.json`, sha `faed869acd008ea05cd576f3de4bc5092c166f38800937c05da605e7b7d264d9`. Cada
   veredicto lleva su ancla literal en el texto de la ficha (comprobado por código: 45 de 45 anclas literales y 45 veredictos válidos, `salidas/control_anclas_lectura1_41.json`).
   - Escrita a las 18:54:35, después de las fichas.
   - **La hizo un lector nuevo.** Esta sesión ya conocía la lectura previa hecha con el criterio opuesto. El lector
     nuevo tuvo acceso solo al criterio y a las fichas.
   - **Sin cifra en este reporte ni en el FRENO.** La cifra sale después de la segunda lectura a ciegas de la mesa y
     de la adjudicación de la autora sobre las divergencias, como en T4.
6. **Nota posterior, ajena y sin commit, en la enmienda 8** (árbol de trabajo, sha `2093f6c9…`; «Decisiones de la
   autora (07/10/2026, noche)»).
   - Ratifica el circuito y cita este criterio con su sha.
   - Deja PENDIENTE de la autora el denominador: las 41 del crudo o las 45 fichas.
   - Las fichas separan EO01–EO41 (crudo r2b) de EO42–EO45 (matriz), así que la cifra se puede computar con
     cualquiera de los dos.
