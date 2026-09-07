# Adjudicación de causa del 16,9 % de PR-4

Unidad U-COB-A. **USD 0** — todo sobre material ya extraído. Criterio de
clasificación sellado **antes** de abrir un solo caso:
`criterio_destinatario.md`, sha
`f5066c12a906b2e3720e2b62d1cb9db2cb45bdcfc91bb91d46c77d3ab843204a`.

Recomputable: `python3 code/adjudicar_pr4.py` → `adjudicacion_pr4.json`.

---

## 1. Partición manual de los 24 casos (medición a)

**Los 22 de PRIORIDAD 2**, cada uno con su cita en `particion_24_casos.json`:

| clase | casos | fracción |
|---|--:|--:|
| **(B) la mención NO es destinatario → falla de la MARCA** | **18** | **81,8 %** |
| **(A) destinatario no emitido → falla del MODELO** | **4** | **18,2 %** |

Subclases de (B): **B2 definición/descripción 10** · B1 remisión normativa 3 ·
B3 objeto o contraparte 2 · B5 el BCRA como receptor 2 · **B4 mención de paso
1**, que es además un **falso positivo léxico puro**: `ri_con::p2.b1` casó
`Sujeto_deudor` contra «saldo **deudor**» — la marca casa una palabra, no un rol.

Los **4 de clase (A)** no son homogéneos:
- **2 son CHAPEAUX HUÉRFANOS**: `ri_tii::p5.b0` «Para entidades financieras:» y
  `ri_tii::p5.b7` «Para PSPCP:». El corte por página los separó de las partidas
  que encabezan. Es el defecto que A.1 anticipó en §2.d, ahora medido.
- **2 son ambigüedades resueltas contra el instrumento** (`ri_tii::p1.b1`,
  `ri_fcem::p1.b3`), por la regla de desempate del criterio, que ante duda
  anota (A) para no absolver al modelo.

**Los 2 de PRIORIDAD 1: ambos (C) inferencia legítima, cero (D) invención.**
Y los dos son **falsos negativos de la marca**. El más claro,
`ri_fcem::p1.b1`:

> «**Las entidades que corresponda** deberán remitir diariamente las
> novedades…»

Sujeto gramatical de un verbo deóntico — destinatario inequívoco. La marca no
lo vio porque «las entidades que corresponda» no es una forma del catálogo.

---

## 2. Las 14 de `ri_tii` contra el censo de forma (medición b)

**Las 14 caen TODAS en páginas de clase `prosa` SIN tabla lógica** (p.1, p.5,
p.6). Las páginas con tabla de `ri_tii` son la 3 y la 4, y **ninguno** de los
14 casos está ahí. **La contaminación tabular no explica nada de la caída.**

Nueve de las 14 están en p.5, que es la lista de definiciones de códigos de
partida — el mismo material que la partición clasifica B2.

---

## 3. El arnés (medición c), con sus DOS mecanismos separados

### 3.a (iii-a) SEÑAL FALTANTE — rehecha, y su conclusión es otra

**Tres mediciones daban distinto y DOS ESTABAN MAL.** La definición correcta
—mención en el título, ausente **tanto del cuerpo (sin la línea 1) como de la
herencia**— se escribió antes de correrla (`code/iii_a_rehecha.py`) y da:

| definición | resultado | estado |
|---|--:|---|
| título sí / `texto` completo no | 25/1.763 = 1,4 % | **SUPERSEDED** — `texto` **contiene** el título, así que la condición es casi autocontradictoria y lo que sobrevive son artefactos de guionado |
| título sí / cuerpo sin línea 1 no | 187/1.763 = 10,6 % | **SUPERSEDED** — ignora la **herencia**, que también viaja al modelo |
| **título sí / ausente del cuerpo Y de la herencia** | **44/1.763 = 2,5 %** | **VIGENTE** |

**La cifra vieja de 1,4 % era mía y era defectuosa.** No viaja al registro.

**Y la conclusión es más fuerte que «efecto chico»: (iii-a) NO ES UN DÉFICIT
DE ARNÉS, ES UNA PROPIEDAD DE POBLACIÓN.** El dato que lo cierra, verificado:
de las **1.477** unidades de dev que pasan por la **misma rama del prompt** que
A.2 (1.475 `punto_terminal` + 2 `seccion_sin_puntos`), **las 1.477 —el 100 %—
tienen su título CONTENIDO en su `texto`**. Vaciar la línea «Punto del chunk»
**no le quita al modelo nada que no siga viendo**.

La diferencia real no es un campo del arnés: **las unidades de dev son puntos
numerados cuyo encabezado nombra al sujeto, y los bloques de A.2 son fragmentos
de página que pueden empezar a mitad de frase.** Eso no se arregla poblando dos
campos.

- **Descartada para los 22 de Prioridad 2, por construcción**: la marca es
  léxica sobre el texto de la unidad y el título de A.2 va vacío, de modo que
  las 33 menciones marcadas están **todas en el cuerpo**, a la vista del
  extractor.

### 3.b (iii-b) EFECTO DE RÓTULO — el mecanismo NO aplica como estaba formulado

El laudo lo enuncia como «la unidad se anunció como “chunk de punto”, **un tipo
que no existe en el vocabulario de dev**». **Medido, eso no es así:**

- `chunk de punto` **no es un valor del campo `tipo`** en ningún corpus. Los
  valores de dev son `punto_terminal` (1.475), `mini_chunk` (286),
  `seccion_sin_puntos` (2).
- «Tipo de unidad: chunk de punto» es lo que **el prompt de producción imprime
  para todo chunk no-mini**, y por lo tanto **dev imprime exactamente el mismo
  rótulo** para sus 1.475 `punto_terminal`. Verificado corriendo
  `build_user_message` sobre un chunk real de dev.

**Los rótulos son idénticos: (iii-b) no es un diferencial y no puede explicar
los 22.** Lo que sí difiere entre los dos arneses es el **contenido** de la
línea siguiente: dev imprime «Punto del chunk: 1.1 — Exigencia.» y A.2 «Punto
del chunk: p1.b0 — » (dirección sin semántica normativa, y título vacío). Ese
diferencial existe, pero es distinto del que el laudo describe, y esta unidad
no encontró evidencia de que explique los 22 casos de Prioridad 2 — los 18 de
clase (B) tienen su causa identificada en la marca, y los 4 de clase (A) en el
corte por página y en la ambigüedad.

---

## 4. El reparto, sin redondear a una sola causa

| explicación | veredicto | evidencia |
|---|---|---|
| **(ii) falla de la MARCA** | **causa PRINCIPAL, en las DOS direcciones** | sobrecuenta: 18 de 22 casos de Prioridad 2 (81,8 %) no eran destinatarios · subcuenta: **4 falsos negativos** (2 en Prioridad 1 + 2 en el censo de silencios) |
| **(i) falla del MODELO** | **causa MENOR pero MAYOR de lo que parecía** | **6 omisiones sobre 18 destinatarios = 33,3 %**: 4 de Prioridad 2 (2 de ellas chapeaux huérfanos) + 2 del censo de silencios. El censo la empujó hacia arriba: antes se contaban 4 |
| **(iii-a) señal faltante** | **descartada para los 22**; material al 1,4 % para el nivel de la marca | la marca es sobre el cuerpo; el título de A.2 va vacío |
| **(iii-b) efecto de rótulo** | **no aplica como estaba formulado** | los rótulos de dev y A.2 son idénticos |

## 5. Qué se concluye, con todas las letras

**La conclusión NO es «el modelo de página pierde el sujeto».** Es que **el
piso de 42,9 % nunca fue el piso**: contaba 33 unidades como «tienen sujeto que
anclar» cuando **18 de esas menciones no eran destinatarios**.

Recálculo sobre destinatarios **identificados** —11 CONCORDANTE (no revisados
por el criterio, contados a favor del piso) + 4 de clase (A) + 2 de clase (C),
estos últimos fuera de la marca:

> **ETAPA 1 de 3 — cifras SUPERSEDED.** Las de esta tabla son previas a
> revisar los 11 CONCORDANTE y a censar los 42 silencios. Se conservan para
> mostrar la trayectoria; **las vigentes están en §5.ter**.

| | valor (ETAPA 1) |
|---|--:|
| piso declarado en el pre-registro | 33/77 = **42,9 %** |
| piso recalculado sobre destinatarios identificados | 17/77 = 22,1 % |
| emitido | 13/77 = 16,9 % |
| recuperación sobre destinatarios identificados | 13/17 = 76,5 % |

Leído así, el extractor **recuperó tres de cada cuatro** destinatarios
identificables, y lo que queda es **una falla localizada y con mecanismo
conocido: el chapeau huérfano** (2 de los 4 casos de clase A).

### 5.bis Los 11 CONCORDANTE, revisados — y lo único que ingresa

Toda la adjudicación anterior miró unidades donde el extractor **calló**, y
**ninguna ingresa al grafo**. Lo que ingresa son las **13 aristas `aplica_a`**,
y once salían de unidades sin testear. Revisadas con el criterio sellado y la
**regla de desempate INVERTIDA** (adenda `b610151c…`: ante duda sobre un
CONCORDANTE se anota (B) y la arista se retira, porque retirar de más produce
omisión —que §1 acepta— y dejar de más produce falsedad —que §1 manda retirar):

| clase | casos |
|---|--:|
| **(A)** destinatario en el pasaje y la arista apunta a él | **8** |
| **(C)** inferencia legítima (destinatario deducible del documento) | **2** |
| **(B)** no hay destinatario → **la arista se retira** | **1** |

**El caso (B) es `ri_tii::p5.b9`**, y confirma la consistencia del criterio: es
una **definición de código de partida** —«2010100 - De CVU a CVU dentro del
mismo CBU recaudador: transferencias enviadas a…»—, el **gemelo exacto** de los
diez casos B2 de Prioridad 2. Mismo material, misma clase; la diferencia es que
acá el extractor **sí emitió**, poniendo `aplica_a` sobre algo que no obliga a
nadie. **Es la única falsedad en campo estructurado que encontró esta unidad.**

**TRES ARISTAS SE RETIRAN** (esta unidad las lista; **no retira nada** — el
ingreso es acto del ensamblado de la tanda):

1. `Operacion «Transferencias entre cuentas CVU mismo PSPCP» → Sujeto_pspcp` (`ri_tii::p5.b9`)
2. `Operacion «Transferencias entre cuentas CVU mismo PSPCP» → Sujeto_entidad_financiera` (`ri_tii::p5.b9`)
3. `Operacion «Presentación de informaciones al BCRA» → Sujeto_pscpp` (`ri_pscpp::p1.b0`) — **clasificación positiva, no duda**: el extractor convirtió «Presentación de informaciones al Banco Central de la República Argentina» —que es el **nombre de la norma citada**— en una `Operacion` y le colgó un `aplica_a`. Es el **patrón B1 (remisión normativa)** del criterio sellado, aplicado **a la arista**. La regla de desempate invertida **no interviene** acá. Las otras cuatro aristas de esa unidad quedan.

**Corrección del motivo (regla i)**: la versión anterior de este reporte
fundaba este retiro en «duda genuina → regla invertida», lo que **contradecía
el propio artefacto**, que clasifica la unidad como (C) — y en (C) el desempate
no aplica, como decía mi propia nota de defecto. **La acción era correcta; el
motivo escrito no reproducía.** La clasificación corre en **dos niveles**: la
unidad y cada arista. Una unidad (C) puede portar una arista (B) —es
exactamente este caso—, y por eso la unidad **no cuenta en k** mientras la
arista **sí se retira**.

**Defecto propio de mi adenda, declarado**: preveía solo (A) y (B) para los
CONCORDANTE, y dos casos exigen la clase **(C)** del criterio original —
obligación real cuyo destinatario se deduce del documento sin estar nombrado
en el pasaje. Usé (C) y lo declaro: no es duda genuina, así que la regla de
desempate no aplica ahí.

### 5.ter Cifras recomputadas — trayectoria completa

Se cumplió el **Caso 2** de la declaración previa (uno o más falsos negativos):
cada uno es una unidad con destinatario y sin arista, o sea **una omisión del
extractor**, que sube el denominador y baja la recuperación.

| etapa | destinatarios | emitido | recuperación | estado |
|---|--:|--:|--:|---|
| 1 · antes de revisar los CONCORDANTE | 17 | 13 | 76,5 % | SUPERSEDED |
| 2 · tras los 11 (k = 1) | 16 | 12 | 75,0 % | SUPERSEDED |
| **3 · tras el censo de 42 (j = 2)** | **18** | **12** | **66,7 %** | **VIGENTE** |

*(El 75,0 % de la etapa 2 y el extremo superior del intervalo coinciden en
valor por casualidad aritmética y son cosas distintas: aquél sale de k = 1 con
16 destinatarios sin censar los silencios; éste, de 18 destinatarios menos las
dos ambigüedades.)*

**Cifra final: 12/18 = 66,7 %**, con **6 omisiones del extractor sobre 18
destinatarios identificados**. Piso 18/77 = 23,4 %; emitido 12/77 = 15,6 %.

### La etiqueta correcta: **MEDICIÓN SOBRE CENSO**, no cota superior

Las versiones anteriores de este reporte rotulaban el número «cota superior», y
**la razón que daban argumentaba al revés**. Corregido:

1. **El denominador está completo.** Las **77** unidades del brazo prosa están
   clasificadas: 11 concordantes + 22 Prioridad 2 + 2 Prioridad 1 + 42
   silencios = 77. **La razón que sí lo hacía cota superior —denominador
   incompleto— desapareció con el censo.**
2. **El desempate conservador sesga a la BAJA, no a la alta.** Retirar por duda
   a un CONCORDANTE lo saca **del numerador y del denominador**: si
   `ri_tii::p5.b9` estuviera mal retirado sería **13/19 = 68,4 %**, *más alto*
   que 66,7 %. La regla invertida **empuja el cociente hacia abajo**.

**Etiqueta vigente: MEDICIÓN SOBRE CENSO, con desempate conservador declarado
que la sesga a la baja.**

### El intervalo, cerrado por los dos extremos

Ninguna cota abierta: los dos extremos son computables y trazables a **casos
nombrados**.

| extremo | valor | de qué depende |
|---|--:|---|
| **inferior** | **12/18 = 66,7 %** | las dos ambigüedades declaradas cuentan como destinatarios (lectura vigente) |
| **superior** | **12/16 = 75,0 %** | si esas dos se resolvieran al revés y salieran del denominador |

Los dos casos, nombrados:
- **P2.04 · `ri_tii::p1.b1`** — «…abiertas en la misma entidad o proveedor de
  servicios de pago **informante**».
- **P2.19 · `ri_fcem::p1.b3`** — «…remitidos **a través de la entidad
  financiera** por medio de la cual opere habitualmente».

**Se publica 66,7 % – 75,0 %.**

### 5.quater CENSO de los 42 silencios — la muestra de 15 queda SUPERSEDED

**La muestra de 15 estaba sesgada por composición.** Su regla —los 15 primeros
por `chunk_id` ascendente— es **orden alfabético por documento**, de modo que
salían de `ri_chr` (3), `ri_con` (9), `ri_fcem` (1) e `ri_itme` (2), y
**excluía por construcción a cinco de los nueve**: `ri_pfmipyme`, `ri_pscpp`,
`ri_pspii`, `ri_rem` y `ri_tii`. Es **el mismo sesgo de composición** que se
corrigió en el brazo planilla al pasar del pre-registro v1 al v2: una regla
mecánica no evita el sesgo si su orden está correlacionado con el documento.

**Leídas las 42.** Censo, no muestra. Declaración previa sellada antes de leer:
`declaracion_censo_silencios.md`, sha `7cc0ac9a…`.

**Falsos negativos: 2 de 42 = 4,8 %.** Por documento:

| TO | silencios | falsos negativos | tasa |
|---|--:|--:|--:|
| `ri_pspii` | 3 | **1** | **33,3 %** |
| `ri_rem` | 11 | **1** | **9,1 %** |
| `ri_con` | 9 | 0 | 0 % |
| `ri_itme` | 8 | 0 | 0 % |
| `ri_tii` | 6 | 0 | 0 % |
| `ri_chr` | 3 | 0 | 0 % |
| `ri_fcem` · `ri_pfmipyme` | 1 c/u | 0 | 0 % |
| **total** | **42** | **2** | **4,8 %** |

**Los dos caen en documentos que la muestra excluía por construcción.** El
sesgo era real y mordió exactamente donde se anticipó.

**Y los dos son gemelos de casos donde el extractor SÍ ancló** — que es el
hallazgo, no el número:

> **Aviso de lectura — la etiqueta (A) está sobrecargada entre las dos
> revisiones, y significa cosas OPUESTAS según la columna.** En **Prioridad 2**,
> (A) = destinatario real **NO emitido** → **omisión del modelo**. En los
> **CONCORDANTE**, (A) = destinatario real **con la arista correcta** →
> **emisión buena**. La letra marca lo mismo —que el destinatario existe—; la
> implicación sobre el extractor es inversa. Abajo se nombra la columna de cada
> caso.

- `ri_pspii::p1.b1` «Se deberán presentar los Estados Contables anuales…» es el
  **gemelo textual exacto** de `ri_pscpp::p1.b0` (**C05, columna CONCORDANTE**),
  donde el extractor emitió cinco aristas por inferencia legítima. Acá **no
  emitió ninguna**.
- `ri_rem::p1.b3` «Se informarán, respecto de las cuentas… **en la entidad**…»
  es gemelo de **dos casos de columnas opuestas**: `ri_tii::p1.b1` (**P2.04,
  columna Prioridad 2** — destinatario real **no emitido**, omisión) y
  `ri_tii::p2.b0` (**C08, columna CONCORDANTE** — destinatario real **con su
  arista correcta**, emisión buena). Ambos llevan (A), pero por lo dicho arriba
  eso significa cosas opuestas. **Ese contraste es exactamente lo que la
  observación registra**: ante un patrón textual muy parecido el extractor
  ancló en un caso y no en el otro. La marca no vio ninguno de los dos porque
  dicen «la entidad» a secas.

**Lo MEDIDO, y es lo que va**: **6 de los 18 destinatarios identificados
quedaron sin arista.**

**OBSERVACIÓN, con su n — no diagnóstico.** Los dos falsos negativos parecen
gemelos de casos donde el extractor sí ancló. **Son dos pares**, y quien los
juzgó gemelos es la misma instancia que saca la conclusión. **«No encontré una
propiedad que los distinga» no es «no hay ninguna»**: nadie miró posición en la
página, longitud del bloque ni contexto previo. Por eso **no se afirma varianza
del extractor**: eso exigiría agrupar las 77 ya clasificadas por patrón de
sujeto y ver si el resultado varía **dentro** de los grupos. **Es otra unidad,
no esta.**

### Barrido de cifras — registro

Este número tuvo cuatro formas (76,5 → 75,0 → 66,7 → el intervalo 66,7–75,0).
Barrido de todos los artefactos de la unidad buscando `76,5 · 75,0 · 66,7 · 17
· 16 · 18 destinatarios · 13 · 12 emitido · 22,1 · 20,8 · 23,4 · «cota
superior» · «varianza del extractor»`:

| archivo | apariciones tocadas | qué se hizo |
|---|--:|---|
| `adjudicacion_pr4.md` | **7** | 2 rotuladas ETAPA 1 · 3 filas de trayectoria rotuladas SUPERSEDED/VIGENTE · «cota superior» reemplazada por la etiqueta correcta + intervalo · «varianza del extractor» reemplazada por observación con su n |
| `code/verificar_a2.py` | **4** | 2 checks rotulados ETAPA 1 · 1 rotulado ETAPA 2 · 1 reescrito a la etiqueta correcta (más 5 checks nuevos de intervalo y etiqueta) |
| `code/recomputo_concordantes.py` | **1** | bloque de etiqueta reemplazado (regenera 8 apariciones del JSON) |
| `adjudicacion_pr4.json` | **2** | rótulos `_ETAPA` = «1 de 3 — SUPERSEDED» |
| `code/adjudicar_pr4.py` | **1** | rótulo `_ETAPA` en `_meta` |
| **total** | **15** | |

**No tocadas, con su razón** (verificadas una por una):

- **3 líneas en 2 documentos SELLADOS** — `adenda_criterio_concordantes.md`
  (cita el 76,5 % vigente en su momento) y `declaracion_censo_silencios.md`
  (describe el Caso 1, que **no** se cumplió). **Son el registro de lo que se
  declaró antes de medir: no se editan.** Sus cifras pertenecen a su momento y
  el sello lo prueba.
- **9 apariciones de «cota superior» que se refieren al COSTO por unidad**, no
  a la recuperación (`diseno_A2.md`, `reporte_A1.md`, `code/costo_a2.py` y los
  pre-registros v2/v3/v4). Otra magnitud, sin cambio.
- **1 aparición de «75,0 %» en `reporte_A2.md`** que es la **tasa de rinde de
  `ri_fcem`**, no la recuperación. Otra magnitud.

## 6. La conclusión entera: LOS DOS ANCLAJES ESTABAN MAL ESPECIFICADOS, POR LA MISMA RAZÓN

**El piso de 42,9 % contaba menciones LÉXICAS como destinatarios** — y 18 de
las 22 revisadas no lo eran. **El techo de 53,1 % se midió sobre una población
que nombra a su destinatario EN EL ENCABEZADO** — las 1.477 unidades de dev de
la rama de A.2 tienen, el 100 %, su título dentro de su texto. **El intervalo
entero, tal como se pre-registró, no era aplicable a bloques de página.**

Los dos extremos fallan por lo mismo: **se construyeron sobre una población
cuyas unidades son puntos numerados con encabezado propio, y se aplicaron a
fragmentos de página que pueden empezar a mitad de frase.** No es que el
instrumento midiera mal; es que medía otra cosa.

**Y ESO NO DEBILITA EL PRE-REGISTRO: ES SU PRODUCTO.** Y no por una vía sino
por **dos**, que este material documenta:

**(a) Por PREDICCIÓN.** El ancla mal especificada se descubrió porque una
**predicción sellada falló contra guarda**. Con un umbral elegido después de
ver los datos, nadie se habría enterado de que la marca contaba definiciones de
códigos de partida como destinatarios. La falla de PR-4 no es un resultado
adverso: es el mecanismo funcionando.

**(b) Por PROCEDIMIENTO.** La muestra sesgada de silencios se descubrió porque
la **regla de muestreo estaba declarada y era auditable**: nadie corrió una
guarda contra ella —**no había número que pudiera fallar**—, se vio **leyendo
la regla** y notando que «los 15 primeros por `chunk_id` ascendente» es orden
alfabético por documento, y por lo tanto excluía a cinco de los nueve.

**El mecanismo común, y es más general que cualquiera de los dos, es DECLARAR
ANTES DE MIRAR.** Una predicción sellada se audita cuando falla; un
procedimiento declarado se audita aunque nada falle. El segundo cubre
exactamente el caso en que no hay cifra que pueda dispararse — y fue el que
encontró el sesgo que movió la recuperación de 75,0 % a 66,7 %.

**Esta es la línea de método que va al capítulo, y vale más que cualquier
resultado de la corrida.**

## 7. Consecuencias, y qué NO hace esta unidad

1. **PR-4 y su medición quedan como están, selladas contra ESTE arnés.** La
   adjudicación explica el número; no lo cambia.
2. **La re-medición de PR-4 no es de esta unidad.** Rehacerla en otras
   condiciones —recalibrando la marca, o con título y punto poblados— es una
   unidad nueva con su propio pre-registro y su propia autorización de gasto.
   **Esta unidad concluye y frena; no vuelve a correr nada.**
3. **No se tocó el módulo de producción ni el prefijo.** Poblar el bloque de
   unidad es una unidad propia con su laudo.
4. **La entrada de la prosa al recurso no se mueve**: la fila 5 de §6 manda
   entrar con residuo declarado por documento, y la adjudicación de causa no
   la altera — la refuerza, porque el residuo ahora tiene mecanismo.
