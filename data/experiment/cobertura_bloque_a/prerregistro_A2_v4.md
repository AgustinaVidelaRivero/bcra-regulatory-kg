# Pre-registro de la fase A.2 — predicciones por brazo · **v4**

Unidad U-COB-A. **Sellado ANTES de la corrida**: su sha256 se imprime en el
freno y ninguna prediccion se edita despues de ese sello. Alcance: **NUEVE**
documentos (laudo 2 del 07/09; `ri_spi` fuera, declarado caso propio).

## 0. Por qué hay una v4, y qué se conserva

Las **cuatro** versiones se conservan integras en el paquete de revision, con
su sha; ninguna se edita:

| versión | sha256 | estado |
|---|---|---|
| v1 | `3aef54c9d27589c3d249cbcfa126c816cd48bf5ae1489507c2993389892d2e7d` | conservada |
| v2 | `fa7fdf52e2dedb98f912f206b15391985c994631e9ec3aa74e712bf42bc0cd1e` | conservada |
| v3 | `8e112189369bfccc5a2010c4d4780abbbb8d2c840076be4a8cd8ea2888611cbe` | conservada |
| **v4** | *(sha impreso en el freno)* | **vigente** |

Que cuatro versiones se sucedan **antes** de medir no debilita el
pre-registro: lo que lo destruiria es editarlo **despues** de ver resultados.
Nada se ha corrido todavia.

### 0.a-bis Por qué hay una v4 (dos celdas y una línea)

**Residuo de propagacion de la v3.** Las filas 1 y 2 de §6 son las unicas que
deciden el **brazo planilla**, y las dos arrancaban con «PR-2 y PR-4 se
cumplen». Esa precondicion venia de cuando fallar PR-4 por el piso significaba
**excluir** documentos. Reescrita la fila del piso en la v3, quedaba un hueco:
**si PR-4 fallaba por abajo, ninguna fila decia que pasa con la planilla** — y
la rama del piso es el resultado **modal** de la tabla (cinco de los nueve
documentos caen bajo el piso del brazo por construccion, §6.a), no el
excepcional.

La v4 corrige **dos celdas y agrega una linea de alcance**:

1. **Fila 1** — precondicion: «PR-2 y PR-4 se cumplen» → «**PR-2 se cumple y
   PR-4 no falla por el techo**».
2. **Fila 2** — la misma correccion.
3. **Linea de alcance** debajo de la tabla: las filas 1 y 2 deciden unicamente
   el brazo planilla. Razon: con la correccion anterior, bajo la rama del piso
   disparan **a la vez** la fila 1 y la fila 5, y la obligacion de declarar
   residuo por documento vive **solo en la 5**.

**Nada mas se mueve**: §1 a §5, §7 y §8 viajan byte-identicas, y de §6 solo
cambian esas dos celdas y se agrega esa linea.

### 0.a Por qué hubo una v3 (cambio ANGOSTO sobre la v2)

**La fila del piso que la v2 agrego a §6 no resiste el calculo.** Decia que si
PR-4 falla por abajo entra la prosa «salvo el o los documentos que sostengan
la falla». Medido, ese criterio excluiria material por construccion y no por
desempeño — ver §6.a, donde la medicion queda escrita. Ademas contradecia el
principio §1 del laudo del esquema congelado, que la propia v2 cita para
justificar la fila del techo.

La v3 corrige **tres cosas y agrega una linea de cierre**; **todo el resto de
la v2 viaja intacto**, incluido el factor de longitud de §7, que no se toca.

1. **§4** — el desglose por TO es **diagnostico**, y su base de comparacion es
   la **tasa propia de cada documento**, no el 42,9 % del brazo.
2. **§6, fila del piso** — reescrita: **entra la prosa con residuo declarado
   por documento**, sin exclusion.
3. **§6, fila nueva para PR-1 / PL-1** — vocabulario fuera de lista: **freno
   de ingreso** con los rechazos citados uno por uno.
4. **§6, linea de cierre** — las predicciones de caracterizacion no gatean
   ingreso.

### 0.b Por qué hubo una v2 (se conserva el registro)

La v1 fue reemplazada por **un cambio de diseño, no por una reinterpretacion**: el laudo del 07/09 subio el tope a
**USD 4,00** y ordeno que **los dos brazos vayan COMPLETOS**, de modo que el
brazo planilla pasa de muestra de 24 unidades a **censo de las 114**.

El motivo del laudo corrige el diagnostico de la v1. La v1 declaro la
limitacion del brazo planilla como **falta de poder** («no alcanza para una
estimacion fina»). Medida, era **sesgo de composicion**, que es peor porque
mas unidades del mismo tipo no lo arreglan:

| documento | población del brazo | muestra v1 | cobertura propia | sobrerrepresentación |
|---|--:|--:|--:|--:|
| `ri_con` | 102 / 114 = **89,5 %** | 12 / 24 = 50,0 % | 12/102 = **11,8 %** | 0,56× |
| `ri_tii` | 11 / 114 = 9,6 % | 11 / 24 = 45,8 % | 11/11 = 100 % | **4,75×** |
| `ri_rem` | 1 / 114 = 0,9 % | 1 / 24 = 4,2 % | 1/1 = 100 % | 4,75× |

Y la unica pagina de `ri_con` que la v1 elegia (p.13, 12 bloques) es su
**maximo** entre catorce paginas de media 7,3 — el extremo, no lo tipico. Los
cuatro criterios de seleccion de la v1 eran criterios de **maxima
informacion**: correctos para las predicciones de existencia (PL-1, PL-3,
PL-5) e **incorrectos para las de tasa** (PL-2, PL-4), que son las dos que
alimentan el laudo de escala. Una tasa sobre una seleccion propositiva no es
la tasa de nada.

Con el brazo completo, **PL-2 y PL-4 dejan de ser inferencia sobre muestra y
pasan a ser censo** del material de planilla de los nueve.

## 0.bis A.2 absorbe a A.3 — las guardas cambian de objeto

Las **191 unidades son TODO** el material de los nueve documentos: no queda
fase de masa pendiente y **A.3 sale del tablero**. La consecuencia, escrita y
no absorbida: **las guardas de este pre-registro ya no gatean el GASTO, gatean
el INGRESO AL RECURSO**. Ninguna prediccion decide si se paga —se paga
todo junto, antes— sino **que se queda en el grafo y que se retira**.

**Por que es aceptable gastar antes de la guarda**: el costo total esperado
por la via calibrada es **USD 0,97**, apenas **USD 0,36** mas que el piloto
muestreado de la v1. A ese precio, comprar el censo completo y decidir despues
que ingresa es mas barato y mas honesto que comprar una muestra sesgada y
tener que volver a comprar.

---

## 1. Definiciones operativas (comunes a los dos brazos)

**RINDE**: la unidad produce **≥1 entidad de tipo normativo**, es decir de
`{Operacion, Restriccion, Excepcion, Obligacion, Potestad, Condicion,
Definicion}`, contada por su procedencia **PRIMARIA** (campo `provenance`).

**NO RINDE**: la unidad produce 0 entidades, **o** produce unicamente
`TextoOrdenado`, `Comunicacion` y/o `Sujeto` — andamiaje documental o de
catalogo, no contenido normativo de la unidad.

**Entidades del brazo**: la union de las entidades de tipo normativo emitidas
por sus unidades. Las fracciones por tipo se calculan sobre ese total, no
sobre el total del grafo.

**Por que la procedencia PRIMARIA y no la lista completa** (convencion
laudada; las cuatro cifras viven en `code/ancla_pr2.py` →
`ancla_pr2.json`, no sueltas en prosa):

1. una unidad rinde si **genero** contenido normativo, no si aparece listada
   entre las procedencias de un nodo generado en otra unidad;
2. el ancla de PR-2 se midio con ese mismo campo, de modo que usar la lista
   completa **compararia dos cosas medidas con reglas distintas**.

---

## 2. BRAZO PROSA — 77 unidades · 13 páginas · 9 documentos (COMPLETO)

**PR-1 — el vocabulario congelado alcanza.** Cero emisiones de tipo o de
predicado fuera de los 9 y los 13.
*Falsable*: ≥1 emision fuera de lista.
*Ancla*: guarda 2 de A.1 — 10 de 10 muestras cubiertas, 0 no cabe.

**PR-2 — rendimiento alto pero por debajo del corpus de desarrollo.**
**≥ 80 %** de las 77 unidades rinden (≥ 62 de 77). **Se reporta agregado Y por
TO** (§4).
*Falsable*: < 80 % agregado.
*Ancla, verificada independientemente en esta unidad*: **96,2 %** = 1.696 de
1.763 unidades E0 con ≥1 nodo normativo de procedencia primaria en el grafo
vigente `0226e947`. **Hallazgo del recomputo**: bajo procedencia primaria,
restringir a tipos normativos **no mueve una sola unidad** — los conjuntos
«≥1 nodo de cualquier tipo» y «≥1 nodo normativo» son **identicos**. La
ambiguedad del ancla no era el filtro de tipo sino que campo de procedencia
cuenta: con la lista completa (`provenances`) las cifras serian 99,9 % y
97,05 %, y su brecha de 51 unidades esta sostenida **integramente** por nodos
`TextoOrdenado`. Se predice por debajo del 96,2 % porque el brazo incluye
rotulos de una linea («Instrucciones generales») que no portan norma.

**PR-3 — la Obligacion domina, y mas que en el corpus general.** `Obligacion`
es el tipo mas frecuente del brazo y representa **≥ 45 %** de sus entidades.
*Falsable*: no es el mas frecuente, o < 45 %.
*Ancla*: **38,0 %** en el grafo vigente (2.484 de 6.529). Se predice por
encima porque este material es regimen informativo, cuyo contenido es
precisamente el deber de presentar.

**PR-4 — `aplica_a` se degrada de forma acotada.** La fraccion de unidades con
≥1 arista `aplica_a` cae en el intervalo **(42,9 % ; 53,1 %)**. **Se reporta
agregado Y por TO** (§4).
*Falsable*: fuera del intervalo, por cualquiera de los dos lados.
*Anclas, y por que cada extremo importa*: **42,9 %** son las 33 de 77 unidades
del brazo que nombran literalmente un sujeto del catalogo congelado — por
debajo de ese piso el extractor no recupera ni los sujetos que estan escritos,
y la procedencia de pagina rompe el predicado; **53,1 %** son las 936 de 1.763
del corpus de desarrollo — por encima de ese techo esta **inventando** sujetos
donde el texto no los nombra, que por el principio §1 del laudo del esquema
congelado (falsedad en campo estructurado) es **peor** que omitirlos.

**PR-5 — la palabra partida se paga.** ≥1 entidad emitida tiene una palabra
cortada por guion de particion («obli- gacion») en su `label` o en su texto.
*Falsable*: cero casos.
*Ancla*: **30 de las 77** unidades del brazo (39,0 %) contienen al menos una
palabra partida, porque el modelo de unidad de pagina no hereda
`e0_lib.corregir_fronteras_intra_palabra`.

---

## 3. BRAZO PLANILLA — 114 unidades · 17 páginas · 3 documentos (**CENSO**)

`ri_con` 102 unidades / 14 paginas · `ri_tii` 11 / 2 · `ri_rem` 1 / 1.
**Es la poblacion completa de material de planilla de los nueve**, no una
muestra: PL-2 y PL-4 son tasas censales y no admiten pregunta de
representatividad.

**PL-1 — el vocabulario congelado alcanza.** Identica a PR-1, medida por
separado sobre este brazo.
*Falsable*: ≥1 emision fuera de lista.

**PL-2 — la planilla rinde mucho menos que la prosa.** **< 50 %** de las 114
unidades rinden (< 57 de 114).
*Falsable*: ≥ 50 %.
*Ancla*: **no hay ancla de material de planilla en este repositorio** — esa
ausencia es la razon de ser del brazo. El 50 % es una **convencion declarada,
no calibrada**, elegida como punto medio entre «rinde como prosa» (≥80 %,
PR-2) y «no rinde nada» (0 %); su virtud es ser anterior a la medicion. El
umbral **no cambia** respecto de la v1: lo que cambia es el denominador, de 24
a 114.

**PL-3 — testigo RX-10.** ≥1 unidad del brazo emite una entidad cuyo texto
mezcla el encabezado de una columna con el valor de otra.
*Falsable*: cero casos.
*Ancla*: RX-10 (`docs/backlog_reextraccion.md:267`) y el bloque de `ri_con`
p.5 citado en el reporte de A.1 §2.a.

**PL-4 — la modalidad no se alucina sobre un formulario.** `Obligacion`
representa **< 25 %** de las entidades de este brazo — muy por debajo del
≥45 % predicho para prosa. Umbral **sin cambios** respecto de la v1.
*Falsable*: ≥ 25 %.
*Interpretacion PRE-DECLARADA*: si la planilla produce `Obligacion` en
proporcion de prosa, el extractor esta atribuyendo modalidad deontica a un
formulario. Eso es falsedad en campo estructurado, y por el principio §1 del
laudo del esquema congelado **se retira**, no se acepta con residuo.

**PL-5 — contraste con la lectura tabular sellada.** Las 2 paginas de `ri_tii`
del brazo (p.3 y p.4) tienen **5 tablas logicas** detectadas por B5.8.3. Para
esas 2 paginas, la lectura de prosa emitira **menos** entidades bien formadas
que filas tiene la lectura tabular.
*Falsable*: emite mas o igual.
*Ancla*: `censo_forma.json` → `ri_tii.b583_tablas_logicas = 5`,
`b583_paginas_con_tabla = [3, 4]`. Enunciado **sin cambios** respecto de la
v1; ahora vive dentro de un brazo completo.

---

## 4. Reporte POR TO obligatorio de PR-2 y PR-4 — es DIAGNÓSTICO

PR-2 y PR-4 se reportan **agregados por brazo Y desglosados por documento**.

**El desglose por TO es DIAGNOSTICO: sirve para localizar donde vive una
falla, no es un umbral por documento.** El umbral es uno solo y es el agregado
del brazo (PR-2 ≥80 %; PR-4 en el intervalo). Ningun documento aprueba ni
reprueba por separado.

**Base de comparacion de cada documento: SU PROPIA TASA LITERAL**, es decir el
denominador de su fila en la tabla de abajo — **no** el 42,9 % del brazo. Un
documento cuya emision se acerca a su propia tasa literal **CONFORMA**, este
donde este respecto del promedio. El caso limite lo fija el registro: **`ri_rem`,
con 0 de 11 bloques que nombren sujeto, CONFORMA emitiendo cero aristas
`aplica_a`** — ahi no hay sujeto que recuperar, y exigirle el 42,9 % del brazo
seria pedirle que invente uno.

*Razon por la que el desglose es obligatorio*: de los **33** bloques del brazo
prosa que nombran sujeto, **19 son de `ri_tii`** (76,0 % de sus 25). **Sin
`ri_tii` el brazo da 14/52 = 26,9 %.** El piso de PR-4 lo sostiene **un solo
documento**, y si PR-4 falla por abajo un numero agregado esconderia donde
vive la causa.

Desglose de la señal de sujeto en el brazo prosa (`python3 code/recomputo_nueve.py`):

| TO | con sujeto / bloques | TO | con sujeto / bloques |
|---|--:|---|--:|
| `ri_tii` | 19/25 = 76,0 % | `ri_itme` | 3/11 = 27,3 % |
| `ri_pscpp` | 1/1 = 100 % | `ri_chr` | 1/4 = 25,0 % |
| `ri_fcem` | 2/4 = 50,0 % | `ri_rem` | **0/11 = 0 %** |
| `ri_pfmipyme` | 1/2 = 50,0 % | | |
| `ri_pspii` | 2/5 = 40,0 % | **total** | **33/77 = 42,9 %** |
| `ri_con` | 4/14 = 28,6 % | **sin `ri_tii`** | **14/52 = 26,9 %** |

---

## 5. Observación a reportar (NO es una predicción)

**`ri_pspii` p.1 es la unica pagina de los nueve que el censo de forma
clasifica `prosa` y que ademas tiene una tabla logica detectada por B5.8.3.**
Ya esta pagada dentro del brazo prosa y ofrece un **segundo punto de
contraste** entre las dos lecturas, independiente del de PL-5. Se reporta lo
que se observe; **no se predice nada sobre ella** y su resultado no confirma
ni falsa ninguna prediccion.

---

## 6. Qué se QUEDA en el recurso y qué se retira (decidido ANTES de medir)

Reemplaza la tabla §3 de la v1, que estaba redactada para un mundo con A.3
posterior. Con A.3 absorbida, cada fila decide **ingreso al recurso**, no
gasto. **Las diez predicciones tienen consecuencia pre-declarada**: siete en
las filas, tres en la linea de cierre.

| resultado | qué queda en el recurso |
|---|---|
| PR-2 se cumple y PR-4 no falla por el techo · PL-2 y PL-4 se cumplen | **entra el brazo prosa** (77 unidades, con `granularidad_procedencia = pagina`); **el brazo planilla NO entra**: se declara, con su medicion, y su tratamiento pasa al bloque B |
| PR-2 se cumple y PR-4 no falla por el techo · falla PL-2 **o** PL-4 (la planilla rinde como prosa) | entra el brazo prosa; **el brazo planilla queda EN ESPERA de laudo** — su material esta extraido y medido, pero no ingresa hasta que la autora se pronuncie sobre si una planilla contable pertenece a un grafo de normativa prescriptiva |
| **falla PR-2** | **no entra nada**, ni siquiera la prosa: si el modelo de unidad de pagina no rinde sobre el material mas favorable, lo extraido se conserva como evidencia y el modelo vuelve a diseño |
| falla PR-4 por el **techo** (>53,1 %) | **freno de ingreso**: señal de **invencion** de sujetos. Nada entra hasta un muestreo manual de las aristas `aplica_a` emitidas |
| falla PR-4 por el **piso** (<42,9 %) | **ENTRA la prosa, CON RESIDUO DECLARADO POR DOCUMENTO**: se publica la tasa emitida de cada TO contra su propia tasa literal (§4), documento por documento. **No hay exclusion de ningun documento.** Ver §6.a |
| **PR-1 o PL-1 falla** (emision de tipo o predicado fuera del vocabulario congelado) | **FRENO DE INGRESO: no entra NADA**, ni prosa ni planilla, y se reporta con **los rechazos citados uno por uno**. Reabrir el esquema es laudo de la autora y **nunca** efecto de esta unidad. Ver §6.b |
| PL-3 se cumple | no bloquea ningun ingreso: es la evidencia que sostiene **declarar** la planilla en vez de extraerla |

**Linea de alcance de las filas.** Las filas **1 y 2 deciden unicamente el
brazo planilla**; el **brazo prosa lo deciden las filas 3, 4 y 5**.

**Linea de cierre — predicciones de caracterizacion.** `PR-3`, `PR-5` y `PL-5`
**no gatean ingreso**, ni a favor ni en contra: su resultado se reporta y
alimenta el registro. Con esta linea, **las diez predicciones tienen
consecuencia pre-declarada** —PR-1, PR-2, PR-4, PL-1, PL-2, PL-3 y PL-4 en las
filas de la tabla; PR-3, PR-5 y PL-5 aqui— que es lo que evita tener que
interpretar la tabla despues de ver los resultados.

### 6.a Por qué la falla por el piso NO excluye documentos

Dos razones, y la primera es una medicion que va escrita aqui para que la
regla no se pueda leer de otro modo.

**(1) El 42,9 % es el PROMEDIO del brazo, y las tasas propias van de 0 % a
100 %.** Cinco de los nueve documentos caen bajo el piso del brazo **por
construccion, antes de extraer una sola entidad**:

| documento | tasa literal propia | unidades |
|---|--:|--:|
| `ri_pspii` | 40,0 % | 5 |
| `ri_con` | 28,6 % | 14 |
| `ri_itme` | 27,3 % | 11 |
| `ri_chr` | 25,0 % | 4 |
| `ri_rem` | **0 %** | 11 |
| **bajo el piso** | | **45 de 77 = 58,4 %** |

Excluir «los documentos que sostengan la falla» dejaria fuera del recurso al
**58,4 % del brazo prosa** por una propiedad de su texto y no por el
desempeño del extractor — y dejaria fuera, entre otros, **al documento que
estaria acertando**: `ri_rem` emitiendo cero aristas `aplica_a` sobre 0/11
bloques con sujeto es exactamente el resultado correcto.

**(2) Contradecia el principio §1 del laudo del esquema congelado**
(`2593d4d`), que la v2 cita para justificar la fila del techo. Textual:

> «Se retira lo que produce falsedad en campo estructurado en material fresco;
> se acepta con residuo declarado lo que produce omision visible o error con
> tasa medida y balance favorable»

Una falla de PR-4 **por el piso es omision con tasa medida** — el caso que el
principio manda **aceptar con residuo declarado**. Una falla por el **techo**
es invencion de sujetos, es decir falsedad en campo estructurado, y ahi el
mismo principio manda **retirar**: por eso esa fila queda igual.

Esta unidad **no adopta una postura mas estricta que el principio**. Si se
quisiera adoptarla, se escribiria como apartamiento deliberado con su razon; no
es el caso.

### 6.b Por qué la fila de PR-1 / PL-1 no es un re-chequeo

La **guarda 2** de la adenda 2 al laudo B5.5 dice textual:

> «se verifica sobre muestra pequeña que el material nuevo cabe en el
> vocabulario del laudo `2593d4d` (9 tipos / 13 relaciones / enum de 6) ANTES
> de extraer a escala. Si no cabe, FRENO y reporte: reabrir el esquema es
> laudo de la autora, nunca efecto colateral»

Esa verificacion **ya se hizo sobre muestra** en la fase A.1 (10 de 10
cubiertas, cero no cabe) y **precedia a una fase de masa que ya no existe**,
porque A.2 absorbio a A.3. Esta fila aplica **la misma guarda al momento que
quedo sin cubrir: la corrida real**. Y el freno es de **ingreso**, no de
gasto, por la misma razon que el resto de §6 — a esa altura ya se pago.

---

## 7. Factor de longitud — cifra corregida con su definición

La v1 y el freno exprés arrastraron **3,4×** desde `reporte_A1.md` §5.b, que
es la cifra de los **DIEZ** y viajo al brazo prosa sin recomputarse contra el
alcance vigente (regla i). Recomputado (`python3 code/factor_longitud.py` →
`factor_longitud.json`), con el estadistico declarado porque el factor cambia
con el:

| población | n | mediana | media | factor por **mediana** | factor por media |
|---|--:|--:|--:|--:|--:|
| brazo prosa | 77 | 178,0 | 214,3 | **1,80×** | 2,84× |
| brazo planilla | 114 | 47,0 | 119,3 | 6,83× | 5,09× |
| los 191 de A.2 | 191 | 109,0 | 157,6 | **2,94×** | 3,85× |
| los diez (publicado en A.1) | 332 | 93,5 | 144,0 | 3,43× | 4,22× |

Corpus de desarrollo: mediana **321**, media **607,5** (n=1.763).

**CONVENCION DE ESTA UNIDAD: medianas** — por coherencia con `reporte_A1.md`
§5.b, donde el factor se publico como «mediana 93,5 contra 321», y porque la
mediana es robusta a la cola larga del corpus de desarrollo, cuya media casi
duplica su mediana. Con esa convencion las cifras son **1,80× el brazo prosa**
y **2,94× los 191 de A.2**.

**Discrepancia declarada (regla i):** el laudo enuncia «2,8× el brazo prosa y
3,2× el piloto completo». El **2,8× reproduce exactamente con MEDIAS**
(2,84×), no con medianas. El **3,2× no reproduce con ninguna** de las ocho
combinaciones de estadistico × poblacion: los valores vecinos son 2,94×
(medianas, los 191) y 3,85× (medias, los 191). **No cambia ninguna decision**
—la cota superior por unidad queda floja con cualquiera de las cifras, que es
todo lo que se le pedia al factor— pero la cifra queda corregida y anclada en
lugar de repetida.

---

## 8. Alcance y costo sellados junto con las predicciones

| brazo | unidades | páginas | caracteres |
|---|--:|--:|--:|
| prosa | 77 | 13 | 16.498 |
| planilla | 114 | 17 | 13.603 |
| **A.2 total** | **191** | **30** | **30.101** |

**Costo**: **USD 0,9711** por la via de caracter (la calibrada) · **USD
3,7126** por la cota superior por unidad. **Ambas bajo el tope laudado de USD
4,00.** Tarifas ancladas en `escalado_prep/proyeccion_costo.json` §`tarifas`.
