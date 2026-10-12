# Mandato de S0-6a de U-SEG-OFICIAL: la corrección de E0 con reglas generales, sobre los errores confirmados de S1-ter

**PREPARADO (mesa, 12/10/2026). Despacho PENDIENTE de la autora.** Etapa del mandato FIRMADO de U-SEG-OFICIAL
(`docs/mandatos/USEG_OFICIAL_segmentacion_e0r2.md`, `e543cb2`), por el plan B del 11/10/2026 (notas al pie de
`docs/mandatos/USEG_OFICIAL_S0-5a_reglas_de_corte_E0.md`, `7150c1a5…`). USD 0, sin API. **Este archivo nombra unidades con error de
corte y de herencia: ninguna lectura a ciegas lo abre, tampoco la de S1-quater.**

## 0. De dónde sale

- **Las decisiones de la autora,** selladas, fuera del repo, en `~/INGENIERIA IA/TESIS/fuera_del_repo/correccion_E0/`. Cada una tiene su
  sello en la misma carpeta:
  - **la nota** `decisiones_correccion_E0.md` (`713751b379b7102e82a4b7eeb1571ca6629392a4a98ee2e796b4dab710e13271`, sellada el
    11/10/2026 a las 19:46:18). Rige tal cual (decisión de la autora del 11/10/2026):
    - qué cuenta como regla general (§1);
    - que no se revierte ninguna lista de (b) (§2);
    - las reglas A a K (§3);
    - lo que lleva este mandato (§4);
    - lo que se espera de cada fila en la regresión de S1-quater (§5);
  - **la adenda 1** `decisiones_correccion_E0_adenda_1.md` (`8af5401b06fa160de159e3b61fe21da58359dce86846981c1dccdb312e0e2346`,
    sellada el 12/10/2026 a las 09:01:30). Rigen su §1 (E2-007 y E2-058) y su §4. Sus §2 y §3 están revocados;
  - **la adenda 2** `decisiones_correccion_E0_adenda_2.md` (`1a25529306e6118bfa9696e1b6e7512e7190356c038f977f57c64770a119d9f1`,
    sellada el 12/10/2026 a las 09:39:57). Revoca los §2 y §3 de la adenda 1, y rige su §2: la tanda 0 sigue excluida.
  - **Donde se contradicen, rige la adenda 2.** Dos puntos de la nota quedan reemplazados por ella:
    - el renglón «Tanda 0» del §4 de la nota («sin excepción por documento») lo reemplaza el §2, punto 1, de la adenda 2: la tanda 0
      sigue excluida, con el control «igual byte a byte»;
    - en la tabla del §5 de la nota, la fila de la tanda 0 se espera «sigue con error: la tanda 0 queda fuera de S0-6a» (la adenda 2,
      §2, punto 3).
- **Los errores confirmados de S1-ter:** `errores_confirmados_S1ter.tsv`, en la misma carpeta
  (`5fe8a7ddda7c97dc6e37ec763778edb2f78df6fb340ad4238d195321abcb9def`). Son 40 filas:
  - 16 de corte: 12 en la unidad y 4 en la que sigue;
  - 1 de limpieza;
  - 23 de herencia.

  Es el TSV que cita el registro de la adjudicación de S1-ter (`s1ter/adjudicacion/registro_pasada_1_y_seleccion_S1ter.md`, §7).
- **Ni la nota, ni las adendas, ni el TSV entran al repo** (decisión de la autora del 11/10/2026). Este mandato los cita por ruta y
  sha256.
- **Lo que recibe la ejecutora** (decisiones de la autora del 11/10 y del 12/10/2026): los §3 a §5 de la nota, el §1 de la adenda 1,
  el §2 de la adenda 2 y las filas del TSV.
  - Van en `para_la_ejecutora_S0-6a/`, dentro del paquete de la mesa:
    `~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/d0348a29-aaa4-4292-82f3-0c0149e3787e/scratchpad/hoja_de_ruta_tanda1_mesa/correccion_E0_mandato_mesa/para_la_ejecutora_S0-6a/`.
  - Cada extracto va copiado tal cual de su fuente:
    - `secciones_3_a_5_decisiones_correccion_E0.md` (`096cd54f6f5ec9c0aaed464dfd567a43674eec22a2575b56893f82d5eca6268f`);
    - `adenda_1_seccion_1_decisiones_correccion_E0.md` (`767ac8bdc19f8f54567ade63e8e9818d0e349f31861abd42cfcd2721f857db2b`);
    - `adenda_2_seccion_2_decisiones_correccion_E0.md` (`6e880ab143f304bec13dc1495535bbe75dd8cc02abf3a70e5b9d2e0166e081bf`);
    - `errores_confirmados_S1ter.tsv` (`5fe8a7dd…`).
  - Cada vez que este mandato dice «la nota, §N», «la adenda 1, §1» o «la adenda 2, §2», se lee en esos extractos.
  - La ejecutora no abre la nota ni las adendas enteras, ni otra carpeta del paquete de la mesa.
- **El código de partida** es el de E0 del repo, el de S0-5b:
  - `e0_lib.py` `bd2190ad…`, `correr_e0.py` `68bd74b5…`, `e0_tablas.py` `ab300a22…` y `selftest_e0.py` `789630b5…`;
  - su salida de los 152 es la de S0-5b (`s0_5/b/manifiestos/manifiesto_salida_e0_152_S0-5b.json`, `28494c3a…`), la misma que leyó
    S1-ter (`s1ter/e0/`, sin rastrear en git, controlada contra `s1ter/manifest_salida.json`, `5e63dff2…`).
- **Lo que la mesa verificó antes de preparar este mandato** (11 y 12/10/2026; comandos y salidas en su paquete,
  `correccion_E0_mandato_mesa/`):
  - la unidad de la ficha E2-033 es `cryl::4.2.2` (`s1ter/tramo_b/orden_lectura_S1ter.json`, `acd57e37…`);
  - el «6.» de seggar: E0 lo rechazó con el motivo `raiz_en_columna_profunda_83.7_vs_76.6` (p. 6; `rechazos_header` de
    `estructura_seggar.json` en la E0 de S1-ter). Es el motivo de la regla E;
  - dos filas están entre las claves que cambiaron R5-b a R5-g en S0-5a y S0-5a-bis: E2-007 (R5-g) y E2-058 (R5-c). Las resuelve la
    adenda 1, §1;
  - una sola de las 40 filas es de un documento de la tanda 0: E2-055, de polcre, en la herencia.

## 1. Escrituras y prohibiciones

- **Escrituras:**
  - `data/experiment/segmentacion_oficial_e0r2/s0_6/` (se crea);
  - el scratchpad y el paquete de revisión;
  - el código de E0, solo en una copia: el parche se aplica al repo en S0-6b, una sola vez, después de la revisión.
- **PROHIBIDO:**
  - la API;
  - el repo fuera de `s0_6/`;
  - la salida sellada de la tanda 0 (`reextraccion_v2/e0_chunking/salida_tanda0_r2b/`);
  - cambiar la salida de la tanda 0: ninguna regla nueva corre en sus diez documentos, salvo en el selftest (§2);
  - abrir `~/INGENIERIA IA/TESIS/fuera_del_repo/correccion_E0/` (la ejecutora recibe los extractos del §0),
    `fuera_del_repo/adjudicacion_s1ter/`, `fuera_del_repo/lecturas_ciegas/` y `fuera_del_repo/lectura_lote2/`;
  - tocar el diseño sellado de S1-quater y su adenda (`s1quater/diseno/`). Solo se importa, sin cambios, la función `mostradas_S1ter`
    (§4);
  - diseñar una regla con unidades que no sean las 40 filas: no se agrega ningún caso de diseño nuevo;
  - cambiar el criterio de la lectura de cortes;
  - commitear.
- **Reglas:** CLAUDE.md §4 (a a l).

## 2. Cómo se escribe cada regla

- **Regla general** (la nota, §1, que la ejecutora recibe resumida acá): se escribe por un rasgo del texto o del formato, nunca por
  nombre de documento, número de unidad ni lista, y corre sobre los 152.
- **La tanda 0 queda fuera** (la adenda 2, §2; el mandato firmado de U-SEG-OFICIAL).
  - Las reglas A a K no corren en sus diez documentos, como las de S0-4 y S0-5, que los dejan fuera por lista
    (`correr_e0.py:138` y `:156`).
  - La exclusión de A a K es por la misma lista de diez documentos. Ese es el único lugar donde una regla nombra documentos.
  - La salida de la tanda 0 no cambia.
- **Cada regla lleva, como en S0-5a:**
  - **su interruptor,** en un prototipo aparte (`parche/interruptor_prototipo_S0-6a.diff`, con una variable `S0_6_REGLAS` como la
    `S0_5_REGLAS` de S0-5a). No entra en el parche de S0-6b;
  - **sus casos positivos,** solo de las 40 filas: las de su letra en el §3;
  - **sus casos negativos en `selftest_e0`:**
    - lo que la nota dice que la regla no hace;
    - unidades leídas en S1-ter que tienen su rasgo y cuyo corte y herencia eran correctos (§4).

    Cada negativo va con su origen.
- **Las filas de documentos de la tanda 0** (la adenda 2, §2, punto 2) se prueban como casos positivos solo en `selftest_e0`, con la
  exclusión apagada ahí.
  - La forma de apagarla vive solo en el selftest, no en el camino de `correr_e0` que produce la salida.
  - La salida de la tanda 0 no cambia.
- **Las reglas por lista que se reemplazan** (la nota, §1, punto 4: donde una regla general cubre lo que antes se corrigió por lista, la
  reemplaza). La lista sale del código:
  - C reemplaza a R5-a por lista (`LISTAS_R5A_S0_5`, 43 listas);
  - A reemplaza a R5-a′, que hoy es por lista, solo en ri_oc;
  - E reemplaza a la raíz por lista de la Sección 3 de ri_oc (R5-g), y tiene que dar su mismo resultado;
  - H reemplaza a R5-f por lista (ri_ccna).

  Por cada una, el FRENO muestra qué da la regla general en las unidades que tocaba la lista. Los documentos que salieron de la bolsa
  por esas correcciones siguen afuera.
- **Siguen como están:** R5-b, R5-c, R5-d y R5-e.
  - K actualiza la aceptación de R5-e.
  - **R5-g y R5-c no se revierten** en E2-007 y E2-058: rigen A para E2-007, y A y D para E2-058. Se declara como reemplazo por
    regla general (la adenda 1, §1; nota al pie del 11/10/2026 del mandato de S0-5a).
- **La generalidad** (la nota, §1, punto 3). Por cada regla, el censo dice si cambia algo en al menos un documento donde no se vio el
  error.
  - Si solo cambia documentos donde se vio, esos documentos salen de la bolsa de la evaluación final (`docs/plan_tesis.md:782`, punto 4),
    y se declara.
  - Lo mismo vale para G con lingeef.
- **No se fuerza:** si una regla no cumple su aceptación sin romper otra cosa, FRENO.
- **Las unidades que no son de diseño** (decisión de la autora del 12/10/2026). Una corrección se mide sobre unidades que no se usaron
  para diseñarla, y las que la ejecutora ve en el censo pueden salir en el sorteo de S1-quater. Rige esta regla, tal cual:

  > «La ejecutora no diseña, ajusta ni descarta ninguna regla por lo que vea en unidades que no son las 40 filas ni las 286 leídas en S1-ter. Si algo en esas unidades le parece un error de una regla, lo informa en el FRENO solo con su id y la regla, sin cambiar la regla. Si la autora decide cambiar una regla por una de esas unidades, la unidad pasa a ser de diseño y sale de la población de S1-quater, con una adenda sellada antes del sorteo.»

## 3. Las reglas A a K

La regla de cada letra es la del §3 de la nota, tal cual. Acá van su interruptor, sus filas y lo que la nota deja en manos de la
ejecutora.

- **Aceptación común:** la pregunta de cada fila deja de dar error con el criterio de S1-ter. Es lo que pide la tabla del §5 de la nota,
  fila por fila.
- **La excepción:** la fila de la tanda 0, que se espera «sigue con error: la tanda 0 queda fuera de S0-6a» (la adenda 2, §2, punto 3).
- **Y además:** nada de lo que cuidan el §4 y el §6 cambia sin su regla y sin ir al FRENO.

**A. Títulos sin número** (interruptor `a`).
- **Positivos:**
  - E1-008 y E1-010;
  - E2-007, en la herencia;
  - E2-039 y E2-056, en la unidad y en la herencia;
  - E2-057, en la herencia;
  - E2-058, en la unidad;
  - E2-099, en la que sigue.
  - Es segunda causa en E2-002, E2-006, E2-008 y E2-096.
- **Negativos:** los tres casos en que, según la nota, el renglón no abre división:
  - un renglón entre una madre y sus hijos numerados (D18);
  - una fila de tabla serializada;
  - una página de índice (D15).
- **Reemplaza a R5-a′:** se mantiene su aceptación de S0-5a. C.1 a C.11 de ri_oc no heredan el bloque de validaciones.

**B. Encabezado de un punto con hijos** (interruptor `b`).
- **Positivos:**
  - E1-081 y E1-090, en la unidad;
  - en la herencia, E2-002, E2-011, E2-016, E2-028, E2-034, E2-040, E2-043, E2-045 y E2-046;
  - **E2-055, de la tanda 0 (polcre), en la herencia: solo en el selftest,** con la exclusión apagada ahí. En la salida queda como
    está.
- **De dónde parte:** de las condiciones de R5-c para los títulos de sección.
- **Negativos:**
  - la entrada que hoy sale entera, cuando el título entra en un renglón, no cambia;
  - si el número va seguido de un párrafo, sin título corto, no se fabrica encabezado.
- **A cargo de la ejecutora:** si «Ello, siempre que…» de E1-081 (`seguef::2.13::intro`) está en un bloque de cierre declarado. Lo
  verifica en la salida y lo informa. No se diseña ninguna regla para esa parte.

**C. Párrafo sin número** (interruptor `c`).
- **Positivos:**
  - E2-033 y E2-045, en la que sigue;
  - E2-006, en la unidad, junto con A y K;
  - E2-008, E2-096 y E2-097, en la herencia.
- **La tolerancia de columna, a cargo de la ejecutora:**
  - se fija antes de correr el censo;
  - es una sola para los 152;
  - va en el FRENO;
  - no se ajusta después.
- **Reemplaza a R5-a por lista.** Las 34 listas de (b) que leyó S1-ter son negativos del §4, salvo en las preguntas que tienen fila
  en el TSV.

**D. Rótulo reescrito** (interruptor `d`).
- **Positivos:** E2-058, E2-098 y E2-099, en la herencia. E2-058 va con D, y no se revierte R5-c (la adenda 1, §1).

**E. Número que E0 rechaza por la columna** (interruptor `e`).
- **Positivos:**
  - E2-002, en la unidad, junto con A;
  - E2-065.
- **Cómo se diseña:** desde el motivo `raiz_en_columna_profunda_…` que registra E0, con las tres condiciones de la nota.
- **Aceptación propia:**
  - da el mismo resultado que R5-g en ri_oc, que reemplaza: «3. Aclaraciones» abre la sección 3 y sale de `ri_oc::S2`, y las 51
    unidades de 3.1 a 3.51 heredan «3. Aclaraciones»;
  - el censo muestra cuáles abre de los rechazos con ese motivo que registra E0 (`rechazos_header` de cada `estructura_<to>.json`).
    Según la mesa, fuera de ri_oc son 87, en 7 documentos fuera de la tanda 1 y de la tanda 0
    (`lista_88_rechazos_columna_profunda_mesa.json`, `cf6796e7…`, en su paquete). La ejecutora los saca de E0 y no recibe esa lista.
- **E2-065, a cargo de la ejecutora:** confirma el motivo en su salida de partida. Si es otro, FRENO con el motivo, para la decisión
  de la autora.

**F. Encabezado de tabla** (interruptor `f`).
- **Positivos:**
  - E2-046, en la limpieza de la unidad;
  - E2-066, en la herencia.
  - Es segunda causa en la herencia de E2-046.
- **Negativo:** la primera aparición del encabezado de columnas queda con su tabla.

**G. Número partido por el extractor** (interruptor `g`).
- **Positivos:** E2-094, en la que sigue y en la herencia.
- Si solo cambia lingeef, lingeef sale de la bolsa (la nota, §1, punto 3).

**H. Número sin espacio** (interruptor `h`).
- **Positivo:** E2-005.
- **Reemplaza a R5-f por lista.** Los 11 saltos de ri_ccna que cerró R5-f siguen cerrados (control de continuidad).

**I. Recuadro de encabezado de dos columnas** (interruptor `i`).
- **Positivo:** E2-006, en la herencia.
- **Negativo:** el membrete institucional nunca es madre.
- El censo dice si alcanza los límites declarados de ri_iepsp y ri_ieccm (S0-5a, §3).

**J. Carátula** (interruptor `j`, si es regla general).
- **Positivo:** E1-047.
- **A cargo de la ejecutora:** busca la causa en el código, sin leer otras unidades.
  - Si es un comportamiento general, va como regla general.
  - Si es propio de ceninf, queda como límite declarado, y la fila, como error declarado (la nota, §5).

**K. Pie de formulario** (interruptor `k`).
- **Positivo:** E2-006, en la unidad, como segunda causa.
- **La aceptación de R5-e se actualiza, y se declara:** `ri_ccna::D1F3::S0` ya no termina en el código de formulario, que sale como
  pie. Sigue sin la «C» suelta, y `D1F4::S0` sigue sin letras sueltas.

## 4. Los negativos de S1-ter: las unidades leídas

- **Cuáles son.** Las que da `comun_S1quater.mostradas_S1ter` del diseño sellado de S1-quater (`s1quater/diseno/scripts/comun_S1quater.py`,
  `ade9df93…`), importada sin cambios, con el orden sellado de S1-ter y la E0 que leyó S1-ter:
  - en la etapa 1, la unidad;
  - en la etapa 2, la unidad (o sus partes), sus unidades calificadas y la que le sigue.
- **Cuántas son.** 286: 90 de la etapa 1 y 196 de la etapa 2, en 77 documentos (cuenta de la mesa, con su salida en el paquete). 9 son
  de documentos de la tanda 0, que no cambian.
- **Cuáles estaban correctas.** La adjudicación final de S1-ter no tiene dudosas. Por eso, toda pregunta que se juzgó en S1-ter y no tiene
  fila en el TSV estaba correcta:
  - el corte de la unidad de cada ficha;
  - el corte de la que sigue;
  - la herencia de la unidad de cada ficha de la etapa 2.
- **El control.** Para cada unidad leída, la ejecutora compara la E0 corregida con la de S1-ter:
  - **corte:** si hay una unidad con el mismo id, el mismo `sha256_propio` y las mismas páginas;
  - **herencia:** si su `herencia` es la misma.
- **Qué va al FRENO.** Todo cambio de corte o de herencia en una unidad leída va al FRENO, con la regla que lo causa (por su
  interruptor) y con lo que se juzgó de esa unidad en S1-ter. Lo decide la autora. Quedan fuera solo las preguntas con fila en el TSV,
  donde el cambio es el que se busca.

## 5. El censo por regla

- **Qué es:** sobre los 152, por regla, con su interruptor apagado y prendido, la lista de unidades que cambian.
  - Va por documento, con la regla que causa cada cambio.
  - Para cada clave dice si se creó, se quitó o cambió, y qué campo cambió. Es el formato de `s0_5/bis/censos/claves_S0-5a-bis.json`
    (`filas`, con `reglas`, `atribucion_exacta` y `campos`).
- **En la tanda 0, el censo tiene que dar 0 cambios.**
- **Por regla:** los documentos que cambia, si cambia alguno donde no se vio el error, y las filas que corrige.
- **Qué texto va en el FRENO** (decisión de la autora del 11/10/2026, porque ella adjudica S1-quater):
  - el texto de unidades va solo para las 40 filas y para las 286 unidades leídas en S1-ter;
  - de las demás, ids y cuentas por documento y por regla;
  - el antes y el después de las demás unidades va en archivos con el prefijo `NO_ABRIR_`, en el paquete de revisión, fuera del repo
    (decisión de la autora del 12/10/2026). El FRENO da su sha256, y los revisa la mesa.
  - Lo mismo vale para el informe y para todo lo que quede en `s0_6/`.

## 6. Controles duros (los del §4 de S0-5a y los del mandato firmado)

- **Antes de aplicar:** el censo por regla (§5).
- **La tanda 0, fuera** (mandato firmado de U-SEG-OFICIAL, `e543cb2`, `:121`, `:128` y `:150-152`; la adenda 2, §2, punto 1):
  - 57 de 57 archivos iguales byte a byte a `salida_tanda0_r2b/`, con el script secuencial (`s0_1/scripts/correr_tanda0.py`);
  - los 25 de la tanda 0 dentro de los 152, iguales byte a byte (`s0_4/scripts/control_tanda0_en_152.py`);
  - el selftest de claves, sin mover ninguna clave de la tanda 0.
- **Los 152, dos veces:** iguales entre sí. La diferencia contra la salida de S0-5b (`28494c3a…`) se explica unidad por unidad por las
  reglas.
- **Selftests:**
  - `selftest_e0` (188 de 188 en S0-5b) y los de las reglas anteriores: b52, b581, b582 y b583 (39, 34, 59 y 33);
  - un caso positivo por regla, de las 40 filas, con la fila de la tanda 0 corrida con la exclusión apagada solo ahí;
  - un chequeo de que A a K no corren en la tanda 0, como los que ya hay para S0-4 y S0-5 (`selftest_e0.py:723-726` y
    `:1113-1119`);
  - los negativos del §3 y del §4;
  - los selftests de las reglas por lista que se reemplazan, actualizados, y cada cambio declarado.
- **Claves,** como en el §4 de S0-5a:
  - las de las unidades que ninguna regla toca no cambian;
  - una unión conserva la clave de la primera unidad y no renumera las siguientes;
  - las claves nuevas siguen la convención de E0;
  - el FRENO lista toda clave creada, quitada o cambiada, con la regla que la causa;
  - el selftest de claves compara contra esa lista y da OK solo si los cambios son exactamente esos;
  - el selftest de claves de la caché da su veredicto.
- **Continuidad de la numeración:** el control fijo desde S0-5b (88 saltos en S0-5b, selftest 14 de 14) corre antes y después de las
  reglas, con su lista al FRENO.
- **El manifiesto de la salida de los 152,** con el formato de `s1ter/manifest_salida.json`: un `sha256` con una entrada `e0/<archivo>`
  por archivo. Lo pide el diseño sellado de S1-quater (§2), que lo sella antes de correr nada.
- **Tabla de reprocesamiento:** una fila nueva, porque el código de E0 cambia, fuera de la tanda 0.
- **Repo:** sha256 antes y después. Solo cambia `s0_6/`.
- **Convenciones:** los `.pyc` (2.213 en S0-5b) y el grep de convenciones.

## 7. FRENO S0-6a

Lleva:
- el diseño aplicado de cada regla, con lo que cambió de este mandato y por qué;
- el parche y el prototipo con el interruptor;
- los censos por regla, con la generalidad de cada una y los documentos que salen de la bolsa;
- los controles, con sus salidas, y la tanda 0: 57 de 57, 25 de 25 y ninguna clave movida;
- la evidencia de cada aceptación, fila por fila, con la tabla del §5 de la nota: si la pregunta quedó corregida, y si no, por qué. La
  fila de la tanda 0 sale del selftest;
- los cambios en las unidades leídas en S1-ter (§4), con su regla, para la decisión de la autora;
- lo que la nota deja en manos de la ejecutora:
  - la tolerancia de columna de C;
  - el motivo de E2-065;
  - la causa de J;
  - «Ello, siempre que…» de E1-081;
  - la aceptación de R5-e actualizada por K;
- la declaración del reemplazo por regla general en E2-007 y E2-058 (la adenda 1, §1);
- las claves creadas, quitadas o cambiadas, con su regla;
- las unidades que no son las 40 filas ni las 286 leídas en S1-ter y que le parecen un error de una regla: solo su id y la regla,
  sin cambiar la regla (§2);
- los archivos `NO_ABRIR_`, con su sha256.

Cierre:
- el paquete `revision_USEG_OFICIAL_FRENO_S0-6a/` con su `manifest.txt`. Se copia con `ditto` a
  `~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/<sesión>/scratchpad/revision_USEG_OFICIAL_FRENO_S0-6a/` y se verifica contra su
  `manifest.txt` (CLAUDE.md §4.g);
- el mensaje de commit PREPARADO, sin nombres de unidades, documentos ni mecanismos;
- nada commiteado.

FRENO.

Después (no es de esta sesión):
- la revisión de la mesa;
- S0-6b, con el parche aplicado una sola vez y el manifiesto de la salida;
- S1-quater, en el orden de su diseño (§9), con su adenda 1: la población deja fuera a la tanda 0;
- la tanda 0 del grafo principal queda en su E0, y se declara. Si pasa a la E0 final, y cuándo, lo decide la autora después del
  despacho de la tanda 1 (la adenda 2, §2, punto 6).
