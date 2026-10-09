# Mandato U-OMISIONES-COD — la release de código del ensamblado antes de la tanda 1

**VERSIÓN PARA FIRMAR (v7, mesa, 09/10/2026). Firma PENDIENTE de la autora.** USD 0, sin API.

Reemplaza a los borradores v1 a v6 de la mesa (fuera del repo, en el paquete `hoja_de_ruta_tanda1_mesa/`).

Qué agrega la v7, por las decisiones de la autora del 09/10/2026:
- en el grupo B, el ítem **f′**: el singular «entidad» en la lista de R3 (decisión 1, con la explicación de las 15 marcas de desacuerdo);
- el grupo C reescrito como **g, g1, g2 y g3** (decisión 2). La regla «la definición de la misma sección» va al grupo 2 y no entra acá;
- en cada ítem, su alcance, el selftest con casos positivos y negativos, el criterio de aceptación y la **cifra esperada sobre
  `a9631a64`** (KG-Tanda0-Diez-r2b, `data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2b/r2/kg.json`).

Lo que sigue igual que en la v6:
- el grupo E no entra (07/10/2026, noche), y el F sale porque la enmienda 8 a L-ESQ-R2 quedó NO FIRMADA (09/10/2026);
- G es G-r, H es `Comunicacion.tipo`, e I, J y K entran.

**El límite 2 del esquema final** (el destino de cada valor de un umbral) no está en esta versión: su decisión es PENDIENTE de la
autora.

## 0. Qué es

Las correcciones «solo código sobre lo guardado» (principio 12; filas F14b, F15 y F15c/F15d de la tabla de reprocesamiento), aplicadas
juntas en una release del código del ensamblado y del validador r2.
- **De dónde salen:** de T4 de U-REEXT-T0, de R2-1 de U-RERESOL-CAT, de VERIF-ENSAMBLADO-45-R2B y de U-DIAG-LIMITES.
- **Desde cuándo rigen:** para la tanda 1 en adelante. Entran al grafo de la tanda 0 en el **re-sellado único**, que es una etapa propia,
  no de esta unidad: acá se aplica el código y se mide.
- **Qué no cambia:** ningún pedido a E1 ni a E3, así que ninguna clave de caché se mueve (control con el selftest de claves).

## 1. Dónde entra en la ruta crítica

Cadena 3 del laudo de la release r2 (`docs/laudo_release_r2_pipeline.md`, §2 y nota del 09/10/2026):
1. la firma de este mandato;
2. O1, el diseño con su medición previa, con su FRENO y la revisión de la mesa;
3. O2, la implementación, con su FRENO y la revisión de la mesa;
4. R0: E3-01, con API y un tope de USD 1,50 (enmienda 7, nota del 09/10/2026);
5. el re-sellado único de la tanda 0;
6. la re-medición de la columna r2b del tablero (condición 4 de la tanda 1);
7. los sellos del laudo de la release y su gate final;
8. el pre-registro de la tanda 1.

**Estimación de la mesa** (NO VERIFICADA; días hábiles; hoja de ruta, §21):
- firma, el lunes 12/10;
- O1, el martes 13/10;
- O2, del miércoles 14 al jueves 15/10;
- R0 y el re-sellado, el viernes 16/10.

**Relación con la ruta crítica:** la cadena de E0 (S0-5a → S0-5b → S1-ter → S2 → lista) es la ruta crítica de hoy. Esta unidad corre en
paralelo, y pasa a ser la crítica si el re-sellado no llega antes del pre-registro de la tanda 1. En ese caso rige la opción III ya
decidida: re-sellar después y declarar la diferencia.

## 2. Las correcciones

Las cifras «hoy» son de `a9631a64`, con su fuente. Las cifras «esperadas» son la pre-medición de la mesa o de la unidad que la midió.
Donde nadie la midió, dice **NO MEDIDA** y la fija O1.

### Grupo A — registro de omisiones (T4 de U-REEXT-T0)

**Alcance:** `omisiones.jsonl` y el reporte del ensamblado. **`kg.json` no cambia.**

**Hoy:** 1.137 omisiones `meta_normativo` en `a9631a64` (recuento de la mesa sobre `ens_diez_r2b/r2/omisiones.jsonl`). De ellas, 404 con
marca del contador y 390 con el tramo solo en el texto heredado (`data/experiment/reext_t0/reporte_u_reext_t0.md:90`).

- **a. Tramo heredado.**
  - **Qué hace:** marcar `tramo_en_heredado` en la omisión cuyo tramo está solo en el texto heredado, y contarla fuera de la pérdida
    propia de la unidad.
  - **Esperado:** 390 marcadas.
  - **Selftest:** positivo, una omisión de T4 con el tramo solo en la herencia; negativo, una con el tramo en el texto propio, que no se
    marca.
- **b. Marca «revisar».**
  - **Qué hace:** la marca va en las omisiones con marca del contador y en las de recomendación.
  - **Esperado:** 404 por el contador, más las de recomendación (NO MEDIDA).
  - **Selftest:** positivo, una con marca del contador; negativo, una sin marca y que no es de recomendación.
- **c. Unidad o ítem entero registrado como omisión,** detectado y contado aparte.
  - **Esperado:** al menos 2: `ext::5.8.2.2` (unidad entera) y `ctacte::2.1.1.4` (ítem); el total, NO MEDIDO.
  - **Selftest:** los dos positivos; negativo, una unidad con una omisión entre nodos extraídos.
- **d. `supuesto_en_norma`.**
  - **Qué hace:** marca en código. Mide y no corrige.
  - **Esperado:** el total en diez, NO MEDIDO. Referencia: 77 de 137 supuestos dentro de una norma en las 30 unidades de T4 (`:79-87`).
  - **Selftest:** positivo, un supuesto de T4 dentro de una norma; negativo, una Condicion con su relación.
- **e. El clasificador determinístico de `copia_nota_e3`** (E1-12 del barrido): entra solo si su pre-medición en O1 muestra una precisión
  aceptable (decisión de la autora del 08/10/2026).
  - **Propuesta de la mesa para «aceptable»:** límite inferior de Wilson al 95 % de 0,75 o más, sobre una muestra leída de sus
    detecciones. Si no llega, queda como límite declarado.
  - **Referencia** (T4, `be6b074`): la marca del contador acierta 29 copias reales en 86 casos, y el cotejo mecánico acierta 29 de 37
    sin dejar afuera ninguna copia real.

**Aceptación del grupo A:** 0 diferencias en `kg.json`; cada marca con su cifra; (d) con su precisión y su cobertura contra T4.

### Grupo B — menciones de sujeto

- **f. Contracciones en `verificar_tramo`** (`pyd_r2/code/validador_r2.py:209-230`). «del» pasa a «de» «el» y «al» pasa a «a» «el», en la
  tokenización de la mención y en la del texto.
  - **Hoy:** 257 menciones no verifican en diez; 51 fallan por el artículo, con «del» o «al»
    (`data/experiment/reresolucion_catalogo/freno_r2_1.md:139-146`).
  - **Esperado:** hasta 51 pasan a verificar. Cuántas relaciones cambian de método o de destino, NO MEDIDO: lo fija la pre-medición de
    O1.
  - **Selftest:**
    - positivos: «el cuentacorrentista» contra «Obligaciones del cuentacorrentista», y «el Comité de auditoría» contra «del Comité de
      auditoría»;
    - negativo: una mención que no está en el texto sigue sin verificar.
  - **Aceptación:** la pre-medición en O1, y 0 cambios fuera de las menciones afectadas.
- **f′. El singular «entidad» en la lista de R3** (decisión 1 de la autora del 09/10/2026). Ejecuta la ampliación que L-ESQ-R2 decidió
  el 30/09 (`4ef7650`: «se amplía en código con las menciones de r2b»).
  - **Alcance:** solo agregar «entidad» a `EXPRESIONES_COLECTIVAS_R3` (`reextraccion_v2/corpus_v2/r1_e4.py:306`). R3 compara la mención
    entera sin el artículo, así que una mención con calificador no es «entidad». `_sin_articulo` no cambia, y los determinantes («esta
    entidad», «la mencionada entidad») no entran.
  - **Esperado en `a9631a64`** (pre-medición de la mesa, igual a la de R2-1, `freno_r2_1.md:147-150`):
    - R3 alcanza 435 relaciones. En 401, la sugerencia del modelo ya daba el rol y no cambian.
    - Cambian **19 decisiones**, de cuarentena a R3: ext 14 (→ `Sujeto_rol_entidad_autorizada_exterior`), cap 4
      (→ `Sujeto_rol_alcance_capmin`) y ctacte 1 (→ `Sujeto_banco`).
    - En el grafo: las 19 `aplica_a` dejan `Sujeto_propuesto_la_entidad` (cap), `…__ext` y `…__ctacte`. Hay 17 aristas nuevas hacia el
      rol, y 2 que ya existían y se funden. Los 3 nodos propuestos, con sus 3 `padre_sugerido`, salen: los propuestos pasan de 98 a 95.
    - El registro de no mapeados pasa de 294 a 275 filas (en cuarentena, de 164 a 145).
    - Aparecen **15 marcas de desacuerdo** nuevas (cap 8 y ext 7), sin cambio de destino, porque la sugerencia del modelo va antes que
      R3: los desacuerdos del reporte pasan de 150 a 165. Ninguna es un destino equivocado (explicación de la mesa del 09/10/2026, en
      el paquete `hoja_de_ruta_tanda1_mesa/R3_singular_15_marcas/`).
    - En los documentos sin alcance con la parte A: 0 filas cambian en diez.
  - **Efecto a declarar desde la tanda 1:** en un documento sin alcance, «la entidad» queda en cuarentena aunque el modelo sugiera un
    sujeto. Es la regla de la parte A de la enmienda 6 para las expresiones de R3.
  - **Selftest:**
    - positivos: `ext::7.9.4` (4 relaciones, al rol de exterior), `cap::6.7.2.2` (al rol de cap) y `ctacte::1.5.2.9` (a
      `Sujeto_banco`);
    - negativos, que no cambian (los tres de la autora): `ext::4.4.2` («la/s entidad/es encargada/s del seguimiento…»),
      `ext::11.1.1.10` («la entidad nominada») y `ext::7.3.7` («la entidad nominada por el exportador»), y además «la entidad
      financiera», sintético (R1, sin cambio), y «esta entidad», sintético (sin cambio);
    - uno sintético de un documento sin alcance: «la entidad» con sugerencia del modelo va a cuarentena.
  - **Aceptación:** las cifras de arriba, con la lista de las 19 y de las 15. Una diferencia con la pre-medición se explica caso por
    caso.

### Grupo C — umbrales: la base (decisión 2 de la autora del 09/10/2026; U-DIAG-LIMITES)

**Hoy, en los 264 elementos con base:** 11 resueltas, 96 marcadas y 157 sin destino ni marca (los límites relativos del validador). Fuente:
`UDIAGLIMITES_FRENO_l1_bases_264.json`, reproducido por la mesa byte a byte.

Los cuatro ítems van juntos: (g) sin (g1) marcaría como «base no resuelta» 76 elementos que no tienen base.

- **g. `resolver_base` sobre los elementos del validador** con base y sin destino (en `ensamblar_tanda0.py`, sobre los que conserva el
  punto o). Escribe `base_destino`, `base_via` y `base_no_resuelta`, y los cuenta por origen en el reporte.
  - **Selftest:**
    - positivos: «monto admitido para el uso de efectivo en los puntos 3.8.» (ext) → `ext::3.8`; y los otros dos que resuelve,
      `ext::14.2.2` y `ext::3.18.3`;
    - negativo: una magnitud sin cita (`cla::6.5::intro`, «no superen el importe resultante de aplicar…») queda marcada, sin destino.
- **g1. Base vacía cuando la «base» no es una base.** En `validador_r2.elemento_umbral_relativo` (`:405-442`), o en el ensamblado antes
  de (g), donde lo fije O1.
  - **La regla:** las reglas cerradas de U-DIAG-LIMITES (`UDIAGLIMITES_l1_clasificar_relativas.py`), en su orden, sobre la base
    plegada (minúsculas, sin tildes). La primera que aplica gana. Si gana una de estas cuatro, la base queda vacía, sin marca y sin
    valor nuevo:
    1. **fecha:** `^\d{1,2}[/.]\d{1,2}[/.]\d{2,4}\b`;
    2. **periodicidad:** `^(trimestral|semestral|mensual|anual|con periodicidad|una vez al ano)`;
    3. **cantidad:** `^(NUM\b|"|“|que \d)`, con NUM = `(\d+|un|una|uno|dos|tres|cuatro|cinco|seis|doble|triple|cuarta|tercera|mitad|tercio|otras? (dos|tres))`;
    4. **evento o plazo:** `^(fecha|dia|plazos?|mes|vencimiento)\b`.

    La regla de «recorte que empieza mal» (`^(que |tanto |en la |asignado |alcanzar |dar |previsto )`) va **antes** que la cuarta y no
    vacía la base.
  - **Selftest:**
    - positivos: «04/07/24» (`ext::3.3.3.4`), «una vez al año» (`pro::3.2.1.3`), «"AA"» (`polcre::5.2`) y «fecha de entrega de la
      primera chequera» (`docvig::3.5`);
    - negativos: «alcanzar el total del monto…» (`ext::8.4.4`, recorte) y la magnitud de `cla::6.5::intro`, que conservan la base.
- **g2. Guarda de la cita a otro documento.**
  - **La regla:** una base que resuelve por remisión a un punto N no se resuelve, y se marca `base_no_resuelta`, si en el texto de E0 de
    su unidad la cita «punto(s) N» va seguida inmediatamente, después de su enumeración («N. y M.», «N., M.»), de «del TO sobre», «de
    las normas sobre», «del Texto Ordenado», «de la Ley», «del Decreto» o «de la Comunicación».
  - **Selftest:**
    - positivo: `cap::2.3.1` (nodo `…84bc1f`; la base termina en «(puntos 6.5.1», y E0 dice «–puntos 6.5.1. y 7.2.1. del TO sobre
      Clasificación de Deudores–») deja de estar resuelta a `cap::6.5.1`;
    - negativos: las 4 de `cla::3.7` siguen resueltas, incluida `cla::5.1.2.3`, cuya oración cita después otra norma («…punto
      1.1.3.4. de las normas sobre “Gestión crediticia”»). Ese caso hizo fallar la primera versión de la guarda de la mesa, que miraba
      80 caracteres.
- **g3. Homónimos.**
  - **La regla:** si la base resuelve por definición y en el TO hay dos o más Definicion con ese término normalizado, no se toma la
    primera (`setdefault`, `ensamblar_tanda0.py:696-700`): se marca `base_no_resuelta`, sin valor nuevo.
  - **Selftest:**
    - positivo: las dos «APR» de `cap::8.3.2.12`, porque en cap hay 3 Definicion con ese término;
    - negativos: la EPF (`cap::4.2.1.2`), el ponderador (`cap::3.2.1.1`) y la capacidad de préstamo (`polcre::2.1.9`), que tienen una
      sola Definicion y siguen resueltas.

**Esperado en `a9631a64`** (pre-medición de la mesa sobre el espejo de `resolver_base` de U-DIAG-LIMITES, 107 de 107 iguales al grafo;
`premedicion_grupo_C_mesa.py` en el paquete de la mesa):
- de 11 resueltas, 96 marcadas y 157 sin destino ni marca, se pasa a **11 resueltas, 177 marcadas y 76 sin base**;
- las 11 resueltas de después son 8 de hoy (las 11 menos `cap::2.3.1` y las dos «APR») más 3 nuevas (`ext::3.8`, `ext::14.2.2` y
  `ext::3.18.3`);
- las 177 marcadas son las 96 de hoy, 78 relativas, `cap::2.3.1` y las 2 «APR»;
- **cambian 160 elementos**: 76 (g1), 78 + 3 (g), 1 (g2) y 2 (g3).

**Aceptación del grupo C:**
- las cifras de arriba, sobre `a9631a64`;
- `cap::2.3.1` sin destino y marcada;
- **las 76 sin base y sin marca**;
- el diff de `kg.json` limitado a `base`, `base_destino`, `base_via` y `base_no_resuelta` de esos 160 elementos;
- las 7 resueltas correctas de hoy, iguales (las 4 de `cla::3.7`, el ponderador, la capacidad de préstamo y la EPF);
- las cifras sobre el grafo sin cola (`e22fae1a`), medidas en O1 y declaradas.

**El marco de la etapa T de U-MED-UMBRALES** (enmienda 1, §4.1) se recuenta al sellar el grafo evaluado, como manda su §4.2.

### Grupo D — `remite_a`: lo derivado y la navegación

**Alcance:** el reporte del ensamblado y el tablero. **`kg.json` no cambia.**

- **h. Separar las aristas de extracción de las derivadas** (`remite_a`, `establecida_en`), en el reporte y en el tablero, y citar las
  tres cifras.
  - **Esperado en diez:** 13.301 de extracción, 13.380 `remite_a` y 746 `establecida_en` derivadas
    (`data/experiment/reext_t0/t3bis/salida/medicion_tablero_r2b.json`; `docs/tablero_correcciones.md`, fila de la observación 10).
- **i. Navegación:** los nodos que pasan de la ventana de 40 vecinos, con `remite_a` y sin ella, con la lista. Es insumo para
  U-NAV-DISENO.
  - **Esperado:** 43 y 22 en `a9631a64` (v6).
- **Selftest:** un grafo de prueba con una arista de cada clase.
- **Aceptación:** las cifras reproducidas, y 0 diferencias en `kg.json`.

### Grupo G — procedencia por tramo, variante G-r (U-DIAG-CAP3-GRAFO, `df59e79`)

- **La regla:** solo para los elementos cuyo `punto` es un ancestro de su unidad. Con `verificar_tramo` (holgura 2), el `punto` pasa a ser
  la unidad si su texto propio contiene el tramo, o el segmento del ítem de un tramo compuesto. Si no, pasa al ancestro cuyo bloque
  heredado lo contiene, con su `rol_documental`. Si el tramo no se ubica, no cambia.
- **Dónde:** sobre los registros de `entrada_r2`, antes de E2.
- **Esperado en `a9631a64`:** cambia el punto de 22 nodos (Operacion 9, Obligacion 8, Potestad 4, Restriccion 1) y solo el rol de
  173, con 0 fusiones; en la lectura, 22 de 22 coherentes (`reports/u_diag_cap3_grafo/propuesta_codigo_UOMISIONES_COD_v2.md`, grupo
  G).
- **Selftest:** positivos, dos de los 22; negativo, un nodo cuyo punto ya es su unidad.
- **Aceptación:** esas cifras; ninguna fusión; la suite de procedencia en verde.

### Grupo H — `Comunicacion.tipo`

- **La regla:** diagnosticar y corregir la derivación de «externa» desde `codigo` (`modelos_r2.py:700`; casos en
  `selftest_pyd_r2.py:292-296`), y marcar `tipo_no_derivable` en el resto.
- **Hoy en diez:** 34 Comunicacion sin `tipo`: 7 normas externas, 1 «A-7000», y 26 de tipo equivocado (12 remisiones a puntos o
  secciones y 14 nombres de TOs u otros documentos) (`docs/tablero_correcciones.md:64`).
- **Esperado:** 8 con `tipo` derivado, 26 con la marca, **0 sin tratar**. Los 26 quedan como error de extracción declarado.
- **Selftest:** positivos, una norma externa y «A-7000»; negativo, una «Comunicación "A" NNNN» normal, que no cambia.
- **Aceptación:** 0 sin tratar en diez y en desarrollo (24 hoy).

### Grupo I — «Condiciones sin regla» en las métricas

- **La regla:** `scripts/metricas_intrinsecas.py` mide «Condicion sin ninguna arista de contenido» (sin `establecida_en` ni `remite_a`),
  con la variante «sin `condicion_de` saliente», en lugar del grado 0 (`:243`).
- **Esperado en `a9631a64`:** 331 de 1.952, con 18 aislados (Comunicacion 8 y Sujeto 10) (`docs/tablero_correcciones.md:52`).
- **Selftest:** una Condicion con solo `establecida_en` cuenta; una con `condicion_de` no cuenta.
- **Aceptación:** la cifra reproducida en r1, r2a y r2b, y 0 diferencias en `kg.json`.

### Grupo J — la procedencia de `remite_a` (TRAMO-REMITE-A)

- **La regla:** cada arista lleva la procedencia de su propio origen. Las citas del texto heredado llevan la procedencia de la unidad
  heredada, con su tramo, o se marcan sin tramo de forma explícita. La regla de destinos (D1) y la detección no cambian.
- **Hoy en `a9631a64`:** 13.380 `remite_a`. De ellas, 13.280 llevan el tramo del primer nodo de su punto y 100 no llevan tramo
  (`r1_referencias.py:1192-1206`, `:1272-1276`).
- **Esperado:** las mismas 13.380 aristas, con el mismo origen, el mismo destino y la misma evidencia; cambia solo la procedencia. Cuántas
  cambian, NO MEDIDO: hasta 13.380, contadas y con su causa en O2.
- **Selftest:** dos nodos del mismo punto con tramos distintos dan dos procedencias; una cita heredada lleva la procedencia de su unidad.
- **Aceptación:** esas invariantes, y la lista de cambios por causa.

### Grupo K — la causa «destino en unidad excluida» del detector de citas (ENS-05)

- **La regla:** una categoría propia en el registro de remisiones y en el reporte. No cambia aristas.
- **Esperado:**
  - en `a9631a64`, el grafo completo, 0, porque no excluye unidades;
  - en el sin cola de diez (`e22fae1a`), 43 de 255 irresolubles, que dejan 212 netas;
  - en desarrollo sin cola, 41 de 215 (`data/experiment/sincola_t0/sc1/salida/gate/consola_controles_diez.txt:1`; mandato de U-SINCOLA-T0,
    `:236-239`).
- **Selftest:** una cita a una unidad de la cola en un grafo sin cola; negativo, una cita a un punto inexistente.
- **Aceptación:** esas cifras, y 0 diferencias en las aristas.

## 3. Etapas

- **O1. Diseño con medición previa** (USD 0, sobre una copia):
  - qué detecta cada marca del grupo A, validado contra las lecturas de T4;
  - la pre-medición de (f) y (f′);
  - la corrida en seco del grupo C sobre `a9631a64` y `e22fae1a`, con la lista de los 160 elementos que cambian y su motivo;
  - las cifras de (h), (i), G-r, H, I, J y K;
  - **FRENO O1:** el diseño de cada cambio y su selftest, y toda diferencia con las cifras esperadas de arriba, explicada caso por caso.
- **O2. Implementación:**
  - un selftest por cambio;
  - doble corrida byte a byte sobre la copia;
  - el diff de los grafos r2b con el código nuevo, acotado y declarado por campo: la lista exacta de nodos, aristas y elementos que
    cambian, con su causa;
  - los selftests de la cadena en verde y el selftest de claves en OK;
  - filas y notas en la tabla de reprocesamiento;
  - las medidas sobre la tanda 0, reportadas, no selladas;
  - **FRENO O2**, final.

## 4. Criterios de aceptación de la unidad

- **Qué puede cambiar:** en los grafos sellados, con el código nuevo, `kg.json` cambia solo por f, f′, g a g3, G-r, H y J. Va la lista
  de las diferencias, con su causa. Los grupos A, D, I y K dan 0 diferencias.
- **Cifras:** cada ítem, con su cifra esperada reproducida o con la diferencia explicada caso por caso.
- **Límites:** todo límite o residuo, listado caso por caso, con su unidad (regla de la autora del 09/10/2026).
- **Controles:** el selftest de claves con el contraste en OK y ninguna clave movida; 2.213 `.pyc`; grep de convenciones.

## 5. Escrituras y prohibiciones

**ESCRITURAS:**
- `data/experiment/tanda0/code/ensamblar_tanda0.py` y su selftest (A, g, g2, g3, G-r);
- `reextraccion_v2/corpus_v2/r1_e4.py`, solo `EXPRESIONES_COLECTIVAS_R3` (f′), y el selftest de la resolución
  (`data/experiment/r2_codigo/selftest_r3.py`);
- `reextraccion_v2/corpus_v2/r1_referencias.py`, solo la procedencia de las aristas (J), y su selftest;
- la derivación del `tipo` de la Comunicacion y su marca (H, donde viva hoy esa derivación);
- `scripts/metricas_intrinsecas.py` (I);
- `data/experiment/pyd_r2/code/validador_r2.py`, solo la tokenización de `verificar_tramo` (f) y `elemento_umbral_relativo` (g1, si O1
  lo ubica ahí), y su selftest;
- `data/experiment/mantenimiento/tabla_reprocesamiento.md`, filas y notas, sin mover claves;
- `docs/tablero_correcciones.md`, la fila de las tres cifras;
- `data/experiment/omisiones_cod/`, que se crea;
- el scratchpad.

**PROHIBIDO:**
- el prefijo, el tool schema, E1, E3 y `validador_e1`;
- los grafos sellados y sus registros, la fixture y `grafos.py`;
- EV2;
- el código y los datos de U-MED-UMBRALES (`data/experiment/med_umbrales/`);
- la API;
- la regla de destinos de `remite_a`;
- commitear.

**REQUISITOS:** CLAUDE.md §4 (a a l). Mensajes de commit sin unidades, documentos ni mecanismos, mientras haya una lectura a ciegas
pendiente.

**La tesis:** la versión vigente está en Overleaf; `docs/tesis/main.tex` puede estar desactualizado y no se usa como fuente sin
declararlo.

**CONVIVENCIA:** en paralelo con S0-5a, S0-5b y S1-ter de U-SEG-OFICIAL, que tocan el código de E0, no estos archivos. Va antes de U3 de
U-UNION-ESTRECHA, que toca `ensamblar_tanda0.py` después de esta unidad (su mandato, `:71`).

## 6. Decisiones

**Ya tomadas por la autora:**
- E no entra; G es G-r; H es la `Comunicacion.tipo`; I y J entran (07/10/2026, noche);
- K entra (08/10/2026);
- F sale, y el re-sellado lleva solo E3-01 (09/10/2026);
- f′ entra, y el grupo C es g a g3, con «la misma sección» en el grupo 2 (09/10/2026).

**PENDIENTES al firmar:**
1. el umbral de (e), con la propuesta de la mesa de Wilson ≥ 0,75;
2. si las medidas sobre la tanda 0 van al reporte de U-SINCOLA-T0 o quedan en el FRENO;
3. si (i) se hace acá o en U-NAV-DISENO;
4. el límite 2, que no está en esta versión.

## Firma

PENDIENTE de la firma de la autora (versión para firmar del 09/10/2026, v7).
