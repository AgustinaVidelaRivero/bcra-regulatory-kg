# U-COB-A · fase A.1 — diagnóstico y diseño del bloque A

**FRENO.** Costo API: **USD 0** (ninguna llamada; no se instancio ningun
cliente LLM). Directorio propio de la unidad, unica zona escrita:
`data/experiment/cobertura_bloque_a/`.

Verificador independiente de todo lo que sigue:
`python3 data/experiment/cobertura_bloque_a/code/verificar_a1.py`
→ **29 comprobaciones, cero fallas**, corrido desde un cwd ajeno (`/tmp`).

---

## 1. La cuenta del alcance, re-recomputada (entregable 1)

Primer paso del mandato. **Coincide exactamente; no hay freno por este lado.**

```
python3 -c "import json;d=json.load(open('data/experiment/segmentacion_84/b584_particion/particion_152.json'));\
ns={k:v for k,v in d['por_to'].items() if v['clase']=='no_segmentable_declarado'};\
print(len(ns), sum(v['paginas'] for v in ns.values()));\
print({k:v['paginas'] for k,v in ns.items() if k not in ('optico','plandecuentas')})"
```

| TO | páginas |  | TO | páginas |
|---|--:|---|---|--:|
| `ri_con` | 16 |  | `ri_fcem` | 1 |
| `ri_spi` | 11 |  | `ri_itme` | 1 |
| `ri_tii` | 6 |  | `ri_pfmipyme` | 1 |
| `ri_rem` | 2 |  | `ri_pscpp` | 1 |
| `ri_chr` | 1 |  | `ri_pspii` | 1 |
| | | | **total (10)** | **41** |

**Control**: 161 − 43 (`optico`) − 77 (`plandecuentas`) = **41**. Los 12 no
segmentables suman 161 paginas y 12 unidades; el recurso hoy son **9.324 =
9.266 + 46 + 12**.

**Imprecision del mandato, registrada (regla i).** La nota del mandato dice que
las 12 unidades degeneradas son «una por documento». **No lo son**:
`plandecuentas` aporta **0** y `ri_pspii` aporta **2** (verificado contra
`particion_152.json`). El total de 12 es correcto y ningun control se mueve,
pero la consecuencia si importa para el entregable 5: **el bloque A reemplaza
11 unidades, no 12** — la duodecima es de `optico`, que no se extrae. Los
denominadores de §5 usan 11.

---

## 2. Censo de forma de los diez (entregable 2)

`python3 code/censo_forma.py` → `censo_forma.json`; muestras citadas por
documento en `muestras/<to>.txt`.

**Modelo de unidad aplicado en seco**, tal como lo lauda la adenda §3.3:
bloque de prosa contiguo dentro de una pagina, corte mecanico donde el salto
vertical entre lineas supera **1,5 × el interlineado modal del documento**
(la «linea en blanco» del PDF), sobre el contenido que queda tras separar
encabezado y pie con el instrumento vigente. **No se fabrica numeracion.**

### 2.a El hallazgo mayor: la mitad del bloque A no es prosa

| clase de forma | páginas | bloques |
|---|--:|--:|
| `prosa` | 17 | 110 |
| `mixta` | 3 | 37 |
| **`planilla_ficha`** | **21** | **185** |
| **total** | **41** | **332** |

La adenda §1 y el diseno §1 caracterizan el bloque A como *«prosa sin
numeracion»* cuyo problema es de procedencia. **La medicion lo desmiente para
la mitad de sus paginas**: 21 de 41 son planilla o ficha de registro — el
material que el diseno §1 define como bloque B («su unidad natural no es el
parrafo sino la fila o el bloque de campos»). `ri_con` es el caso extremo:
**14 de sus 16 paginas son la planilla del regimen informativo**, con
encabezados de columna, y solo p.1–2 son instrucciones en prosa.

Muestra citada de una pagina `planilla_ficha` (`ri_con` p.5), donde se ve por
que el modelo de prosa no le aplica — el bloque linealiza una grilla:

```
Balance de las filiales Total casa Balance de subsidiarias Balance Balance de
casa operativas en el exterior Elimina- matriz significativas a consolidar
```

Esto es exactamente el defecto **RX-10** que el repositorio ya declaro
(`docs/backlog_reextraccion.md:267`, «Linealización de tablas dentro del
articulado») y que B5.8.3 evita preservando filas y columnas.

### 2.b El instrumento tabular sellado no ve este material

Corri `e0_tablas` (B5.8.3) sobre los diez, como lectura pura:

- **Ninguno de los 12 no segmentables entro nunca en B5.8.3** — sus 30 TOs
  objetivo son otros (`conteos_b583.json` §`_meta.objetivo`). Su material
  tabular **nunca fue medido**.
- Corrido ahora: **8 tablas logicas en total** (`ri_tii` 5, `ri_spi` 2,
  `ri_pspii` 1). `ri_con` da **0**: sus 46 grillas se descartan por
  `min_filas`, porque **las planillas del bloque A no tienen bordes
  dibujados** — son columnas por alineacion de espacio.

Consecuencia: esas 21 paginas son invisibles para el parser de prosa (0
unidades hasta hoy) **y** para el parser de tablas. Por eso el censo necesito
un criterio propio de clase de forma, declarado en §2.c.

### 2.c El criterio de clase de forma, y su calibracion

`densidad de prosa` de una pagina = fraccion de lineas de contenido **sin
frontera de columna** y de **≥60 caracteres**. Cortes: `planilla_ficha` <0,20;
`mixta` [0,20 – 0,45); `prosa` ≥0,45.

Los dos cortes caen en **los dos huecos mas anchos de la distribucion medida**
(0,16→0,25 y 0,33→0,44), no en valores elegidos a conveniencia; la
distribucion es bimodal (20 paginas ≤0,16 contra 18 ≥0,44). Valide los cortes
**a mano** contra las cuatro paginas frontera (`ri_spi` p.9 / p.2 / p.11 y
`ri_con` p.5): las cuatro quedaron bien clasificadas.

### 2.d Sensibilidad del conteo, y de donde viene su unica inestabilidad

| factor de corte | prosa | mixta | planilla | total |
|---|--:|--:|--:|--:|
| 1,3 | 110 | 41 | 185 | 336 |
| 1,4 | 110 | 41 | 185 | 336 |
| **1,5 (declarado)** | **110** | **37** | **185** | **332** |
| 1,6 | 87 | 26 | 125 | 238 |
| 2,0 | 77 | 24 | 90 | 191 |

El salto 332→238 se concentra **entero en `ri_spi`**: sin ese documento el
conteo es **identico (191) en 1,3, 1,4 y 1,5**. La causa esta medida: el gap
de **19,5 pt aparece 77 veces, 75 de ellas en `ri_spi`**, justo entre los
umbrales 18,75 (factor 1,5) y 20,0 (factor 1,6). Es el interlineado de su
listado de campos, un segundo modo propio de ese documento. **El conteo de los
otros nueve es robusto; `ri_spi` es un caso aparte, y §4 explica por que.**

---

## 3. Guarda 2 — encaje en el esquema congelado (entregable 3)

Documento completo: **`guarda2_encaje.md`**. Muestra: `guarda2_muestra.json`,
seleccionada con **regla fija declarada antes de mirar el contenido** (el
primer bloque de ≥150 caracteres de la primera pagina de clase `prosa` o
`mixta`, uno por documento — cubre los diez por construccion y no permite
elegir el pasaje).

**VEREDICTO: EL MATERIAL CABE. No corresponde reabrir el esquema, y esta
unidad no lo pide.**

**10 = 3 cabe + 7 cabe con salvedad + 0 no cabe.** Ninguna muestra exigio un
tipo o predicado que los 9 / 13 / enum de 6 no tengan.

De las tres salvedades, **dos no son nuevas**: el valor del plazo sin campo
(limite «hechos con valor», ya diferido a ESQ-RI-3/C1.7 por el laudo del
esquema §2) y la remision normativa sin arista (residuo ya declarado en el
laudo §3, con destino «B5 la hereda como criterio de aceptacion»).

**La tercera es nueva y quedo cuantificada**: la unidad no nombra a su sujeto
obligado, y `aplica_a` se queda sin rango. Medido con el catalogo de sujetos
del propio esquema congelado (70 entradas), **mismo instrumento sobre los dos
corpus** (`python3 code/senal_sujeto.py`):

| corpus | unidades | nombran sujeto | fracción | mediana de caracteres |
|---|--:|--:|--:|--:|
| bloque A (prosa + mixta) | 147 | 41 | **27,9 %** | 93,5 |
| desarrollo (los 1.763 de E0) | 1.763 | 936 | **53,1 %** | 321 |

Lectura honesta: **el sujeto ausente no lo inventa el bloque A** — casi la
mitad de las unidades del corpus sobre el que se valido el esquema tampoco lo
nombran, y el grafo vigente se construyo igual. El bloque A **duplica la tasa
de ausencia** (72,1 % contra 46,9 %), con causa conocida: unidades 3,4× mas
cortas. Es diferencia de grado, no incompatibilidad. Ambas cifras son cota
inferior por superficie lexica.

---

## 4. Hallazgo que toca la decisión 1 laudada: tres de los diez SÍ tienen espina

La decision 1 y el diseno §2 se apoyan en que estos documentos **no tienen
punto**. Lo medi, contando bloques que arrancan con un token de numeracion:

| documento | bloques | con numeración | fracción |
|---|--:|--:|--:|
| **`ri_spi`** | 141 | **100** | **71 %** |
| **`ri_pspii`** | 5 | 2 | 40 % |
| **`ri_tii`** | 36 | 7 | 19 % |
| los otros siete | 150 | **0** | **0 %** |

**Siete de los diez no tienen numeracion alguna**: para ellos el modelo de
procedencia `pagina` es exactamente correcto. Pero `ri_spi` numera el 71 % de
sus bloques (`A.1.`, `B.5.8.3.`, `A.1.5.`) — es un **diccionario de campos con
direcciones propias**, y asignarle procedencia de pagina **degradaria una
granularidad que el documento si tiene**. Concuerda con la particion sellada,
que ya registro `ri_pspii` con 2 raices y `hallazgo_rinde_tecnico: true`.

**Esto es laudo de la autora, no de esta unidad.** No modifique nada; lo
reporto. Opciones que veo, sin elegir por usted:

- **(a)** `ri_spi` sale del bloque A y espera una regla de espina que reconozca
  la numeracion letra-punto (`A.1.5.`). Es el unico documento afectado y
  concentra el 42 % de los bloques del bloque A.
- **(b)** entra con procedencia `pagina` como los demas, declarando en el
  registro que su granularidad natural era mas fina. Mas simple, menos fiel.
- **(c)** entra con `granularidad_procedencia = punto` usando su propia
  numeracion, sin fabricar nada — pero eso pide codigo que hoy no existe.

El diseno de A.2 **deja `ri_spi` fuera del piloto** hasta ese laudo.

---

## 5. Conteo exigido por la autora (entregable 5)

`python3 code/proyeccion_procedencia.py` → `proyeccion_procedencia.json`.

### 5.a MEDICIÓN — en unidades, hoy

Denominador: 9.324 − 11 (las degeneradas que el bloque A reemplaza) + N.

| escenario | unidades con `granularidad_procedencia = pagina` | total del recurso | fracción | frase para la tesis |
|---|--:|--:|--:|---|
| todos los bloques | **332** | 9.645 | **3,44 %** | «332 unidades de 9.645» |
| solo prosa + mixta | **147** | 9.460 | **1,55 %** | «147 unidades de 9.460» |
| solo prosa | **110** | 9.423 | **1,17 %** | «110 unidades de 9.423» |

Cuál de las tres filas es la que la tesis escribe **depende del laudo sobre la
planilla** (§2.a) y sobre `ri_spi` (§4). Las tres estan recomputadas.

### 5.b PROYECCIÓN — en elementos del grafo: **NO VERIFICADA**

**Marca explicita: NO VERIFICADA.** Nada se extrajo en esta fase; no existe un
solo elemento con `granularidad_procedencia = pagina`.

Denominador y tasa declarados: **6.510 nodos con `chunk_id` de los 6.529 del
grafo vigente KG-Reextraido-r1** (sha `0226e947…`, verificado en sesion con
`shasum -a 256`) sobre **1.763 unidades E0** del corpus de desarrollo →
**3,6926 nodos/unidad**. Aplicada al escenario prosa + mixta: ~543 elementos
sobre ~34.930.

**Tres supuestos que la invalidan si no se cumplen, declarados en el
artefacto:**
1. **Tasa uniforme — y la medicion dice que NO lo es.** La mediana de un bloque
   del bloque A es **93,5 caracteres** contra **321** de un chunk del dev
   (razon 0,291). Una unidad 3,4× mas corta no rinde los mismos elementos: la
   proyeccion **sobre-estima**.
2. El grafo vigente corrio con el esquema **v2 de 7 tipos**; el congelado tiene
   9 (`Potestad`, `Condicion`, `Definicion` no existen en el vigente). Por ese
   lado la tasa es **cota inferior**. Los dos sesgos van en direcciones
   opuestas y no se cancelan de forma conocida.
3. **El denominador del recurso escalado en elementos no existe**: la
   extraccion sobre los 152 no corrio (B5.7 pendiente). El «~34.930» es
   aritmetica sobre un supuesto, no un recurso medido.

**Recomendacion para el capitulo: escribir la fila en UNIDADES (§5.a), que es
medicion, y no la de elementos, que es proyeccion.** La frase «N elementos de
M» que pide la exigencia solo se puede escribir con verdad **despues de A.2/A.3**.

---

## 6. Censo de los dos declarados referencia (entregable 4)

Documento completo: **`censo_referencia.md`**. **No se extraen.**

| documento | páginas | roles de página | páginas de prosa | bloques |
|---|--:|---|--:|--:|
| `optico` | 43 | 38 historial · 4 índice · 1 cuerpo | 0 | 2 |
| `plandecuentas` | 77 | 76 ficha_registro · 1 cuerpo | 0 | 0 |

Evidencia de la adjudicacion citada desde la fuente sellada
(`docs/adenda2_laudo_B5.5_cobertura.md` §1, FIRMADA, commit `1ae387e`):
densidad deontica **0,000 en las tres variantes** y lectura a ciegas de 32
paginas con pre-registro sellado. No busque los paquetes de U-COB-EXCL.

**Convergencia de dos instrumentos independientes**: la adjudicacion de la
autora es por **contenido**; este censo es por **forma**, y concluye lo mismo —
**2 bloques en 120 paginas** contra **332 en 41** (0,017 contra 8,1
bloques/pagina), cero paginas de prosa en los dos. La medicion por forma
**respalda** la adjudicacion por contenido sin depender de ella.

---

## 7. Diseño de la fase A.2 (entregable 6)

Documento completo: **`diseno_A2.md`**.

- **Documentos**: `ri_tii` (6 pag, 36 unidades — prosa + planilla, y el unico
  con tablas que B5.8.3 si detecta), `ri_itme` (1 pag, 11 — prosa pura) y
  `ri_con` p.1–2 (14 — prosa dentro del documento mas planillero).
  **Total 61 unidades / 13.661 caracteres.** `ri_spi` queda fuera hasta el
  laudo de §4.
- **Tope propuesto: USD 2,00** — sobre una proyeccion de **USD 0,44** por
  caracter (la via pertinente) y **USD 1,19** por unidad (cota superior, con
  tarifa calibrada sobre unidades 3,4× mas largas). Tarifas ancladas en
  `escalado_prep/proyeccion_costo.json` §`tarifas`.
- **Cinco predicciones pre-registradas y falsables**, entre ellas: `aplica_a`
  caera en el intervalo (27,9 % ; 53,1 %) — por debajo significa que la
  procedencia de pagina rompe el predicado, por encima que el extractor
  inventa sujetos; y el **testigo RX-10** sobre las 11 unidades de planilla de
  `ri_tii`, que es la prediccion que decide si la planilla se extrae o se
  declara.

**Nota sobre la proyeccion previa**: la adenda §2 proyecto **57 unidades ≈ USD
1,10** por densidad supuesta (1,38 u/pagina). El conteo real da **332 brutas /
147 utiles**: la densidad subestimo el numero de unidades **2,6× sobre las
utiles y 5,8× sobre las brutas**, y sobrestimo su tamano. El costo total queda en el mismo orden (USD 0,87–2,86 para prosa +
mixta), de modo que **la conclusion economica de la adenda se sostiene**.

---

## 8. Guarda 1 — regresión de no-cambio

**No toque ningun modulo de segmentacion.** La no-alteracion es **estructural**:
el modelo de unidad vive entero en el codigo propio de la unidad, y `e0_lib` /
`e0_tablas` se importan como bibliotecas de solo lectura. Verificado igual:

| control | valor | estado |
|---|--:|---|
| desarrollo, con desglose (cap 462 · cla 143 · ext 973 · pro 101 · ric 84) | 1.763 | OK |
| ESQ-2 (`resumen_cobertura_esq2.json` §`unidades_universo`) | 762 | OK |
| los 68 digeribles (`proyeccion_costo.json` §`por_veredicto.digerible`) | 6.340 | OK |
| los 138 plenos (`particion_152.json` §`agregados`) | 9.266 | OK |
| `e0_lib.py`, `e0_tablas.py`, `prompt_congelado.py` idénticos a HEAD | — | OK |
| `git status --porcelain` sobre las zonas selladas | vacío | OK |

---

## 9. Defecto propio, declarado con causa (regla e)

**El interlineado modal se calculaba sobre todas las lineas de la pagina, y
debia calcularse solo sobre las de contenido.** En `ri_pfmipyme` —1 pagina, 3
lineas de prosa contra 6 de encabezado y pie— los gaps del aparato (6,5 pt)
ganaban la moda por mayoria, el umbral caia de 18,75 a 9,75 pt y **el unico
parrafo del documento se partia en tres unidades**. Detectado porque su modal
(6,5) desentonaba con el de los otros nueve (11,5–12,5).

Corregido: la moda se toma sobre el contenido que queda tras separar encabezado
y pie. **Efecto: `ri_pfmipyme` 4 → 2 unidades; total 334 → 332.** Ningun otro
documento cambio. El censo, la muestra de la guarda 2 y toda cifra publicada
estan regenerados **despues** de la correccion; la muestra de `ri_pfmipyme`
existe gracias a ella (con la version defectuosa el documento quedaba «sin
muestra» por no alcanzar los 150 caracteres).

---

## 10. Cambio en el árbol que no es mío, registrado

El `git status` del arranque mostraba `CLAUDE.md`, `docs/plan_tesis.md`,
`docs/adenda2_laudo_B5.5_cobertura.md` y `docs/diseno_B5.9_ampliacion_cobertura.md`
pendientes; a mitad de sesion dejaron de estarlo. **HEAD paso de `9278923` a
`1ae387e`** (dos commits: `49358e3` de la ampliacion de la regla i y `1ae387e`
de la adenda 2 firmada). **Yo no commitee nada.** La spec que lei es la que
quedo commiteada, y su contenido no entra en conflicto con nada de este
reporte. Lo registro por la regla j: la accion es de la autora y no la afirmo
mas alla de lo que muestra `git log`.

---

## 11. Escrituras de esta unidad

Todo bajo `data/experiment/cobertura_bloque_a/`, nada fuera:

```
code/       comun_coba.py · censo_forma.py · muestra_guarda2.py · senal_sujeto.py
            palabra_partida.py · proyeccion_procedencia.py · costo_a2.py · verificar_a1.py
muestras/   <to>.txt  (12 archivos: los diez + los dos de referencia)
            censo_forma.json · guarda2_muestra.json · senal_sujeto.json
            palabra_partida.json · proyeccion_procedencia.json · costo_a2.json
            guarda2_encaje.md · censo_referencia.md · diseno_A2.md · reporte_A1.md
```

Los scripts resuelven sus rutas desde su propia ubicacion: corren desde
cualquier cwd, sin rutas absolutas (verificado ejecutando desde `/tmp`).

---

## 12. Lo que queda para el laudo de la autora

1. **La planilla del bloque A** (21 de 41 paginas, 185 de 332 bloques): se
   extrae como prosa —con el riesgo RX-10 medido—, se difiere al bloque B, o
   se declara. §2.a.
2. **`ri_spi`** (141 bloques, 71 % con numeracion propia): (a) sale, (b) entra
   con procedencia de pagina, (c) entra con su propia numeracion. §4.
3. **Cuál de las tres filas del conteo exigido escribe la tesis**, y si se
   escribe en unidades (medicion) o en elementos (proyeccion). §5.
4. **El piloto A.2 y su tope de USD 2,00.** §7.
