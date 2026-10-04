# Lectura asistida de las fichas de P4

04/10/2026. **Estado: revisada por la autora el 04/10/2026** (P4.c del mandato), con las correcciones de la sección
«Revisión de la autora», al final, ya aplicadas en las secciones que tocan. La pareada compara release contra
release: el prefijo sellado `v3_b54` con la E0 legada frente al prefijo nuevo `3817de475c93` con la e0-r2. Las
diferencias no se atribuyen al prompt o a E0 por separado, salvo donde la ficha lo permite (la tabla de `cap::1.2`,
que solo existe serializada en la e0-r2).

**De dónde sale cada marca.**
- Las fichas están en `salida/fichas_p4.md`, cegadas: sin grupo, estrato ni origen, en el orden de la semilla.
- Las marcas las genera `marcas_p4.py`, que escribe `salida/marcas_lectura_p4.json`.
- Los extractos que leí para cada dimensión están en `salida/apoyo_lectura_p4.md`.
- Las reglas de D1 a D3 son mecánicas y las fijé antes de marcar. D4 a D6 son por lectura.
- La tabla con Wilson está en `salida/tabla_pareada_p4.json`.

## D1, umbral con tramo literal verificado

**Cuándo aplica.** La ficha aplica si su texto propio tiene una cuantía que es umbral de una norma.
- **El sellado** no cumple por construcción: el crudo v3 no trae tramo de umbral, y el umbral lo arma el ensamblado
  desde la descripción.
- **Cuantías que no son umbral, por lectura:**
  - `ric::4.3.3`: bandas de plazo de códigos de informe;
  - `ric::9.2.1`: porcentajes en el nombre de conceptos;
  - `ric::4.5.1`: ejemplos;
  - `cap::7.1.3.2`: el período de un dato a publicar;
  - `ric::3.1.6`: el coeficiente de una fórmula;
  - `ric::11.1.1`: sus dos no cubiertas son rótulos de columna.

**El nuevo no cumple en tres fichas**, porque falta algún umbral:
- `cap::4.3.3.2`: el MPOR y los períodos mínimos de 10 y 20 días hábiles;
- `cap::6.2.2.4`: los 17 ponderadores de su tabla; el nuevo declara la tabla como omisión;
- `cap::7.1.2`: el límite de la categoría 1, €1.000 millones.

**Además, `cap::6.2.2.6`** cubre las 15 cuantías, pero asocia mal una. Ata la desestimación «entre zonas 1 y 3» a la
banda 2-3 de la zona 2: «Desestimación horizontal zona 2, 2-3 años entre zonas 1 y 3». Es la asociación que prevé la
nota del 03/10/2026 al mandato (`docs/mandatos/UPROMPT_R2_prefijo_nuevo.md:345-347`). Según esa nota, `cap::tabla037`
sale al tratamiento residual por la lista en código (`prompt_r2b.TABLAS_RESIDUALES_FORZADAS`), que no está entre las
escrituras de P4.

## D2, mención verificada

**El sellado** no trae mención para un sujeto del catálogo (`mencion_verificada` = ausente). Solo los propuestos
llegan como mención.

**El nuevo deja 15 menciones sin verificar en 11 fichas.**
- 14 son «las entidades» o «Las entidades», un sujeto que el texto no nombra.
- La otra es una paráfrasis larga, en `cap::4.3.3.2`.

## D3, omisiones con categoría y tramo

**El sellado** no tiene categoría ni tramo: las `omisiones_no_prosa` de v3 se leen como notas.

**El nuevo declara 70 omisiones con tramo.**
- 48 verifican contra el texto propio.
- 7 verifican solo contra el texto completo. Son tramos copiados del bloque heredado: `adrei::4.3.1.2`,
  `cap::7.1.3.2`, `cap::8.5.1` a `8.5.3` (el cierre de la lista), `cla::5.1.1.1` (el encabezado) y `ext::13.4.8`. El validador verifica el
  tramo de la omisión solo contra el texto propio (`pyd_r2/code/validador_r2.py:1316`), y el de la entidad contra el
  propio y el heredado: es un límite del validador.
- 15 no verifican: son resúmenes de tablas y fórmulas, no copias.

La marca D3 sigue al validador de la release.

## D4, la tabla de `cap::1.2`

- **El sellado invierte la tabla.** Da 5.000 a las restantes entidades y 2.500 a los bancos, y agrega una Excepcion
  («Cajas de Crédito Cooperativas exoneradas») que el texto no dice: «salvo» excluye a esas cajas de la columna, no de
  la exigencia.
- **El nuevo copia bien:** bancos 5.000, restantes 2.500 y compañías financieras con comercio exterior igual que los
  bancos. Lo hace con tramos de umbral «5.000» y «2.500».

## D5, `condicion_de` con firma nueva (Condicion → Operacion o Potestad)

Leí las relaciones del crudo de cada brazo. Una relación que el validador de su brazo rechaza no llega al grafo y se
marca «no emite» (revisión de la autora, a y a′). El validador v3 del sellado rechaza por la firma las seis
`condicion_de` de Condicion a Operacion o Potestad que el sellado emite en estas fichas: en el sellado, D5 es
estructural, como D1 a D3.

| Ficha | Sellado | Nuevo | Razón |
|---|---|---|---|
| `cap::2.5.7` | no emite | no emite | la condición de incumplimiento → la aplicación del tratamiento; el sellado la emite y su validador la rechaza por la firma |
| `cap::6.2.2.6` | no emite | no cumple | la regla de imputación a bandas no condiciona las compensaciones horizontales |
| `cla::5.1.1.1` | no emite | cumple | el sellado emite las dos condiciones y su validador las rechaza por la firma. La condición → la inclusión en la cartera comercial: la relación existe y apunta bien. En el nuevo, la condición del monto no se pierde: está en el umbral de e2. Aparte, e2 funde dos condiciones de forma incoherente (revisión de la autora, b) |
| `cla::6.5.4.8` | no emite | cumple | el indicador → la clasificación en la categoría |
| `ctacte::5.1.2.2` | no emite | cumple | operaciones del fideicomiso → el endoso; en el sellado, rechazada por la firma |
| `ext::10.2.5` | no emite | cumple | grupo económico → las dos potestades; en el sellado, rechazadas por la firma |
| `ext::13.4.8` | no emite | cumple | las cuatro condiciones → el pago. Aparte, una Obligacion con `condicion_de`, que no es la firma nueva |
| `ext::3.3.3.3` | no emite | no cumple | en el sellado, rechazada por la firma. El nuevo ata la condición a «emisión de la certificación», no al pago |
| `ext::3.5.6.9` | no emite | no emite | la certificación → el pago de capital; en el sellado, rechazada por la firma |

## D6, destino de `limita`

La regla de L-ESQ-R2 §1.4: el destino es el acto o la magnitud que el tope acota o, si es un ponderador, la exposición
que pondera.

| Ficha | Sellado | Nuevo | Razón |
|---|---|---|---|
| `cap::1.2` | no cumple | no emite | el capital mínimo no acota el comercio exterior |
| `cap::10.1` | cumple | cumple | la elegibilidad acota el uso de las calificaciones |
| `cap::2.12.2.4` | no cumple | cumple | ponderador: el sellado apunta a la asignación (el acto de ponderar) y el nuevo, a la exposición. El sellado, además, corre las bandas de calificación de la tabla |
| `cap::2.12.3.2` | cumple | cumple | la exposición a BMD |
| `cap::4.2.1::intro` | cumple | cumple | la EAD acotada |
| `cap::4.3.3.2` | no cumple | cumple | el sellado apunta al capital hipotético de la CCP y el nuevo, al requisito del miembro compensador |
| `cap::5.1.1` | no cumple | no emite | un ajuste no es un tope |
| `cap::5.4.4` | no emite | no emite | ponderador al 1250 %: las franquicias. El nuevo emite el `limita` hacia un nodo Definicion; el validador lo rechaza por la firma (Restriccion → Definicion) y no llega al grafo (revisión de la autora, a) |
| `cap::6.2.2.6` | cumple | cumple | las compensaciones horizontales; los valores aparte (D1) |
| `cap::8.4.1.19` | no cumple | no cumple | deducciones, no topes, en los dos |
| `cap::8.4.1.6` | no cumple | no emite | condiciones de alcance, no topes |
| `cap::8.5.3` | no emite | cumple | el RPC |
| `ext::13.4.4` | no emite | cumple | el acceso al mercado de cambios |
| `ext::2.7::cierre` | no cumple | no emite | el límite mensual acota el uso del mecanismo, no la confección de boletos |
| `ext::7.1.1.3` | no emite | cumple | la operación de exportación |

## Estrato de listas de excepciones (regla f)

**Qué pide la regla:** cada ítem es una Excepcion compuesta con la norma del encabezado, sin `exceptua` cuando esa
norma está en otra unidad.

**Excepcion compuesta:** el nuevo la emite en 4 de 8 (`ext::3.5.6.1`, `ext::13.4.4`, `ext::3.3.3.1` y
`ctacte::6.2.4`); las descripciones componen con la norma del encabezado. El sellado la emite en 2 de 8.
- **Las 4 del nuevo emiten igual una `exceptua`.** En tres va a un `local_id` que no existe: queda colgante y el
  validador la descarta. En `ext::13.4.4`, el nuevo vuelve a emitir la Restriccion del encabezado dentro del ítem y
  la exceptúa.
- **Los otros 4 quedan como Condicion u Operacion:**
  - `ext::3.5.6.9`: Condicion sin relación;
  - `ext::13.4.8`: Operacion con sus condiciones;
  - `ext::3.3.3.3`: Condicion → «emisión de la certificación»;
  - `ctacte::5.1.2.2`: Operacion con su condición.
- **Además, el nuevo de `ext::3.3.3.1`** trae una entidad sin `type` (un TextoOrdenado con la clave `tipo`), que el
  validador rechaza.

## Casos fijos y F1

- **`cap::8.5.1` a `8.5.3`** (ítems que reconoce g): el nuevo compone con el encabezado y emite la Restriccion del
  límite mínimo en los tres (4,5 %, 6 % y 8 % de los APR). El sellado no emite ningún límite. En `cap::8.5.1` el nuevo
  expande COn1 como «capital operacional computable», que es incorrecto.
- **`ric::9.2.1`:** el nuevo extrae los conceptos del cuadro de códigos (salida de 5.986 tokens contra 503 del
  sellado). Ninguna cuantía es umbral (D1).
- **`pro::1.1.2.5`:** los dos brazos emiten la Definicion y la Excepcion de mutuales y cooperativas. El sellado las une
  con una `exceptua_obligacion` hacia la Definicion; el nuevo no las une.
- **F1:**
  - `ayccef::3.4.1`: el sellado no emite nada y el nuevo compone la Obligacion con el encabezado, bien;
  - `ayccef::4.2.7.2`: condiciones conjuntas («en todos los siguientes aspectos»), así que corresponde una
    Condicion. El sellado no emite nada y el nuevo, una Definicion;
  - `expaef::6.6.2` y `expaef::1.1.2.5`: los dos componen;
  - `adrei::4.3.1.1` a `.3`: los dos componen;
  - `adrei::4.3.1::intro`: ninguno de los dos emite nodo de contenido (regla 1).

## a, la modalidad, contra una lectura de muestra

- **Lo que clasificó el código:** 2 recomendaciones, las dos bien: `lingob::6.2.4.3` («se consideran buenas prácticas
  que») y `adrei::4.3.1.2` («se espera»). Ninguna consecuencia.
- **La muestra que leí:** las 11 fichas cuyo texto propio tiene una forma de `MODALIDAD_FORMAS` y cuyo brazo nuevo no
  copió nada (`apoyo_lectura_p4.md`, sección a).
  - Ninguna es una recomendación.
  - `ext::10.4.2.7` es una consecuencia dudosa: la conformidad previa para quien tiene condenas cambiarias.
  - Las otras 10 no son consecuencias: «incumpl» aparece como palabra descriptiva en 5, «suspen» en 2, y
    «inhabilit», «sancion» y «cargo» en 1 cada una.

## b, Condicion de un ítem sin `condicion_de`

Son 6.
- **`ext::3.5.6.9` (1):** la norma está en otra unidad, el encabezado. Va sin `condicion_de`, como manda R8; la regla f
  pedía una Excepcion.
- **`ext::3.16.3.6` (5):** la norma («no deberán tenerse en cuenta») está en la misma unidad, y las Condicion quedan
  sin vínculo.

## d, el ejemplo de la tesis (`cla::5.1.1.1` y `cla::5.1.1::intro`)

- **No hay Excepcion.** El nuevo no emite la Excepcion de los créditos para consumo o vivienda: emite dos Operacion
  y una Condicion, y declara el encabezado «Abarca todas las financiaciones comprendidas, con excepción de las
  siguientes» como omisión `meta_normativo`.
- **`cla::5.1.1::intro`** no emite nodo de contenido y declara la misma cláusula como `meta_normativo`. Pierde la
  Definicion de alcance que el sellado emitía («Cartera comercial — alcance»). La cláusula es normativa, no
  `meta_normativo` (revisión de la autora, c).
- **La exclusión** de los créditos para consumo o vivienda de la cartera comercial no está en ninguna entidad de los
  dos chunks del brazo nuevo: solo en el tramo de la omisión `meta_normativo`.
- **Lo que sigue (mandato):** la condición 10 de la tanda 1 vuelve a la autora antes de U-REEXT-T0.

## Pata de E3 (NOTA y guarda)

Cuatro encabezados de lista con la extracción del brazo nuevo.
- **`ctacte::8.3::intro` y `8.4::intro`:** E3 reclama la omisión `meta_normativo`, pero como mal categorizada («fija
  una modalidad»), que es lo que la NOTA admite. La guarda la exime y la unidad queda aceptada con residuales, sin
  reintento.
- **`ctacte::6.4.7::intro`:** aceptada tras el reintento.
- **`adrei::4.3.1::intro`:** `completo_ok`.
- **Copia de la nota:** ningún reintento dejó la marca `copia_nota_e3`, así que no hay caso para releer con la regla de
  P3b-2.

## Revisión de la autora (04/10/2026)

Las correcciones a, a′, b y c ya están aplicadas en las tablas y secciones de arriba. La a′ es un agregado posterior
de la autora (04/10/2026), que extiende la a a los dos brazos.

**a. `cap::5.4.4`, D6.** El `limita` del nuevo va de Restriccion a Definicion. El validador lo rechaza por la firma y
no llega al grafo, así que la marca pasa a «no emite» (`marcas_p4.py`, `LECTURA`).
- `cap::5.4.4` está entre los 40 sorteados (estrato `con_cuantia`), así que recalculé la tabla pareada (`tabla_p4.py`
  sobre las marcas nuevas).
- **La tabla no cambia:** D6 sigue en sellado 3/6 y nuevo 5/6. El par cuenta solo las fichas en que los dos brazos
  emiten la relación, y en `cap::5.4.4` el sellado no la emite.
- Con solo esta corrección, `salida/tabla_pareada_p4.json` quedaba igual byte a byte. `salida/marcas_lectura_p4.json`
  cambia en esa marca y en su estado.

**a′. El mismo criterio, en los dos brazos (D5).** El validador del sellado rechaza por la firma las seis
`condicion_de` de Condicion a Operacion o Potestad que el crudo sellado emite: `cap::2.5.7`, `cla::5.1.1.1`,
`ctacte::5.1.2.2`, `ext::10.2.5`, `ext::3.3.3.3` y `ext::3.5.6.9`. Las seis pasan de «cumple» a «no emite».
- **Dónde está la lista:** `data/experiment/prompt_r2/p3c/insumos_p4_p3c.py`, clave
  `relaciones_d5_d6_rechazadas_por_el_validador`.
- **La tabla pareada recalculada:** D5 queda sin pares firmes en todos los grupos.
  - En los sorteados, de 1/1 y 1/1 a 0.
  - En los fijos, de 1/1 y 1/1 a 0.
  - En las listas, de 2/2 y 1/2 a 0.
  - Las demás dimensiones no cambian.
- **El brazo nuevo solo:** cumple en 5 de las 7 fichas en que emite la relación (`cla::5.1.1.1`, `cla::6.5.4.8`,
  `ctacte::5.1.2.2`, `ext::10.2.5` y `ext::13.4.8`) y no cumple en 2 (`cap::6.2.2.6` y `ext::3.3.3.3`). En los
  sorteados cumple en las 2 en que la emite.
- **Fuente:** `salida/marcas_lectura_p4.json`.
- **D6 no cambia:** el único `limita` rechazado de las fichas de D6 es el de `cap::5.4.4`.

**b. `cla::5.1.1.1`, D5.** La marca del nuevo queda en «cumple»: la relación existe y apunta bien (la del sellado
pasa a «no emite» por a′). La fila de la tabla de D5 se
corrigió: la condición del monto no se pierde, está en el umbral de e2.
- Aparte, e2 funde dos condiciones de forma incoherente:
  - la etiqueta y el umbral son del monto (dos veces el importe de referencia del punto 3.7);
  - la descripción y el tramo son del repago (no vinculado a ingresos fijos o periódicos del cliente).

**c. `cla::5.1.1::intro`.** El nuevo pierde la Definicion de alcance que emitía el sellado («Cartera comercial —
alcance»).
- «Abarca todas las financiaciones comprendidas, con excepción de las siguientes» es normativa, no `meta_normativo`.
- La exclusión de los créditos para consumo o vivienda no está en ninguna entidad.

**d. Omisiones `meta_normativo` que son contenido normativo**, confirmadas por la autora. Con texto propio son 8:
`adrei::S5`, `ext::10.4.2.7`, `expaef::2.2.6.5`, `ctacte::4.2.1`, `ctacte::5.1.2.2`, `cla::5.1.1::intro`,
`ctacte::8.3::intro` y `ctacte::8.4::intro`. Se suma la conformidad previa del encabezado en `ext::13.4.8`, cuyo
tramo está en el texto heredado.

| Omisiones `meta_normativo` en el brazo nuevo | Total | Normativas |
|---|---|---|
| Con tramo en el texto propio | 16 | 8 |
| Con tramo copiado del texto heredado | 6 | 1 (`ext::13.4.8`) |
| Con tramo que cruza del título al cuerpo (`ctacte::6.4.7::intro`) | 1 | 0 |
| Con tramo que no verifica (`cap::4.3.3.2`, un resumen) | 1 | 0 |
| **Total** (una por ficha, en 24 fichas) | **24** | **9** |

- **Las otras 8 con tramo en el texto propio** no están en la lista de la autora: `adrei::4.3.1::intro`,
  `ayccef::2.4.8.1`, `ayccef::4.2.7.2`, `cap::3.1.14::intro`, `cap::7.1.2`, `ext::13.4.4`, `polcre::7.1::intro` y
  `ric::3.1.8`.
- **Las 6 del heredado** son `adrei::4.3.1.2`, `cap::7.1.3.2`, `cap::8.5.2`, `cap::8.5.3`, `cla::5.1.1.1` y
  `ext::13.4.8`.
- **Cómo se reproduce:** `data/experiment/prompt_r2/p3c/insumos_p4_p3c.py`, clave `meta_normativo`. El tramo se
  verifica contra el texto propio con `validador_r2.verificar_tramo`, como en el análisis; si no verifica ahí, contra
  el texto completo y, en un mini-chunk a mitad de oración, en el orden de lectura.
