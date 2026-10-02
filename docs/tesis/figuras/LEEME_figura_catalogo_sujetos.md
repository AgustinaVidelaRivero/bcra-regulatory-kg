# figura_catalogo_sujetos (F2) — registro de generación

Figura F2 del capítulo del esquema: el **catálogo de sujetos** —el árbol de
clases, sus instancias y la indirección por rol de alcance que permite que
una norma alcance a una subclase que no nombra—. Generada POR SCRIPT desde
los artefactos sellados, nunca dibujada a mano, como F1 y F1b.

Este LEEME describe la **cuarta versión**. El árbol, las cuatro ramas, los
nodos colapsados y la leyenda son los de la tercera; cambia el **camino
resaltado**, que pasa al ejemplo de Clasificación de deudores (el que recorre
la tesis):

| | Versión 3 | Versión 4 |
|---|---|---|
| Norma | `Documentación en sistema Braille` (Protección de usuarios, punto 2.2.2) | `Clasificación de clientes según calidad de obligados` (Clasificación de deudores, punto 1.1) |
| Subtítulo de la norma | «Obligación · punto 2.2.2» | «Obligacion · punto 1.1» (el tipo como identificador del esquema, sin tilde, igual que en F1) |
| Rol | `Sujetos obligados (Protección de usuarios)`, 7 miembros, 5 dibujados | `Obligados a clasificar deudores (Clasificación)`, 6 miembros, 3 dibujados |
| Resto del camino | `miembro_de` → Entidades financieras → Bancos → Bancos comerciales | igual |

La historia de las versiones 1 a 3 está en el §8.

## 1. Comando de generación

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_catalogo_sujetos.py
```

Escribe `figura_catalogo_sujetos.svg` (1410,8 × 1295) e imprime el reporte de
verificación. De ahí salen las dos versiones para insertar, el PDF vectorial
y el PNG:

```bash
SOURCE_DATE_EPOCH=0 rsvg-convert -f pdf -o docs/tesis/figuras/figura_catalogo_sujetos.pdf docs/tesis/figuras/figura_catalogo_sujetos.svg
```

```bash
rsvg-convert -z 2 -f png -o docs/tesis/figuras/figura_catalogo_sujetos.png docs/tesis/figuras/figura_catalogo_sujetos.svg
```

`rsvg-convert` (2.62.3, cairo 1.18.4) es la única herramienta externa, y solo
para esas dos exportaciones. El SVG se produce con Python de la biblioteca
estándar, sin dependencias; corre con el `.venv` del repositorio (Python
3.10.13).

| Archivo | Medida propia | Peso |
|---|---|---|
| `figura_catalogo_sujetos.svg` (fuente) | 1410,8 × 1295 px | 28.241 bytes |
| `figura_catalogo_sujetos.pdf` (vectorial) | 1058,1 × 971,25 pt = 373,27 × 342,63 mm | 63.311 bytes |
| `figura_catalogo_sujetos.png` (rasterizado) | 2822 × 2590 px = 478 dpi a 150 mm de ancho | 665.403 bytes |

Recomputo: `stat -f '%N %z' docs/tesis/figuras/figura_catalogo_sujetos.*`,
`pdfinfo docs/tesis/figuras/figura_catalogo_sujetos.pdf | grep 'Page size'` y
`file docs/tesis/figuras/figura_catalogo_sujetos.png`.

**Sobre los 1058,1 × 971,25 pt del PDF.** `rsvg-convert` lee las unidades de
usuario del SVG como píxeles CSS (1/96 de pulgada) y las escribe como puntos
(1/72): 1410,8 × 0,75 = 1058,1 y 1295 × 0,75 = 971,25. El tamaño físico es el
mismo en las dos unidades; como el bloque LaTeX inserta con
`width=\linewidth`, la figura se escala a 150 mm venga de donde venga.

**El PDF es vectorial**: `pdfimages -list` no lista ninguna imagen, y
`pdffonts` lista las mismas fuentes embebidas que la versión 3 (Helvetica,
-Bold, -Oblique, Menlo-Regular, Arial-ItalicMT, más los Type 3 que cairo
arma para los glifos fuera de WinAnsi).

El script FRENA con `AssertionError` antes de dibujar si el catálogo deja de
tener 58 clases / 7 instancias / 5 roles, si la cadena que cita la prosa deja
de ser la del artefacto, si el rol deja de tener 6 miembros o sus
`miembro_de` en el grafo dejan de ser exactamente los que declara el
catálogo, si la norma deja de ser la obligación del punto 1.1 de
Clasificación de deudores con la etiqueta «Clasificación de clientes según
calidad de obligados», si el camino resaltado deja de ser una cadena conexa,
si lo dibujado más lo colapsado no suma 58, si alguna arista dibujada no está
en el grafo vigente, si algún texto desborda su caja, si dos cajas se
solapan, si algún trazo entra en el interior de una caja o cruza el
rectángulo de un rótulo, si algún rótulo no encuentra lugar libre, o si algún
cuerpo tipográfico cae por debajo de 8 pt impresos a `width=\linewidth`.

## 2. Fuentes y sellos

| Archivo leído | sha256 | Commit |
|---|---|---|
| `data/experiment/grafo_v2/esquema_v2_clases.json` (catálogo v2.0, 70 entradas: 58 clases + 7 instancias + 5 roles) | `2672af5216e095bee2a4888e18d85930d7b0149263b87763daacc5fd21814d4d` | `43f241e` |
| `data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json` (grafo vigente) | `0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a` | `185e042` |

El catálogo es el **v2.0** (`esquema_v2_clases.json:2`), no el v3: la figura
ilustra la versión con la que corrió la validación. Ambos archivos están en
el árbol byte-idénticos a su commit: `git diff --stat HEAD --` sobre los dos
da vacío, y `git show 43f241e:data/experiment/grafo_v2/esquema_v2_clases.json | shasum -a 256`
y `git show 185e042:data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json | shasum -a 256`
dan los sha de la tabla.

Salidas de esta corrida:

| Archivo | sha256 |
|---|---|
| `figura_catalogo_sujetos.svg` | `120af34c12506439557e7dc67ed19b249a89423ae69726070de36ad37dc38769` |
| `figura_catalogo_sujetos.pdf` | `551af15225644db476b6fbed034c8f4349491c4cbae767341f747d4c42681533` |
| `figura_catalogo_sujetos.png` | `890178555591fb3138eb956bd51b154e39bd854f0389c9b9967bb36064e31a4d` |
| `generar_figura_catalogo_sujetos.py` (script, versionado junto a la figura) | `bba878ce1328fc5e3b8e7bd9759e2f5b9db6c5375c48b4e027c4d6c3c22483ee` |

Generación determinística verificada: tres corridas con `PYTHONHASHSEED`
distinto (1, 2, 3) y una desde un directorio de trabajo ajeno producen el
mismo SVG (`120af34c…`); el script no usa rutas absolutas. El PNG es
reproducible byte a byte con el mismo `rsvg-convert`.

**El PDF, con fecha fija.** En la versión 3 cairo le estampaba la fecha de
generación en `/CreationDate`, y dos exportaciones daban archivos distintos.
Con `SOURCE_DATE_EPOCH=0` cairo toma una fecha fija (el PDF declara
`CreationDate: Wed Dec 31 21:00:00 1969 -03`, el instante 0 en hora local), y
**doce exportaciones seguidas dieron el mismo sha** (`551af152…`); seis sin
esa variable dieron dos sha distintos. `LEEME_figura_controles.md` §1
documenta, para el PDF de F3, un orden de empaquetado del `/ObjStm` que cairo
no fija y afirma el mismo comportamiento en F2; en estas doce corridas no se
manifestó, pero eso no lo descarta. El sello firme de la figura sigue siendo
el del SVG.

**Discrepancia previa, registrada.** Antes de esta versión, el PNG
commiteado (`d4d83462…`, 643.559 bytes, reemplazado en `ed389c4` del
11/09/2026) no coincidía con el sha que declaraba este LEEME (`c83b8392…`) ni
se reproducía desde el SVG commiteado; el PNG de `bf4a22c` sí
(`git show bf4a22c:docs/tesis/figuras/figura_catalogo_sujetos.png | shasum -a 256`
da `c83b8392…`, igual que exportar el SVG de la versión 3). La regeneración
de esta versión lo reemplaza.

## 3. El camino resaltado

Es la pieza que la figura existe para mostrar y la que gobierna el dibujo:
**cinco nodos y cuatro aristas** en trazo grueso y relleno saturado, con todo
el resto atenuado.

| Nodo | Fuente en `kg.json` | Fuente en el catálogo |
|---|---|---|
| `Clasificación de clientes según calidad de obligados` (tipo `Obligacion`, punto 1.1, página 4 de `TO_clasificacion_deudores_actual.pdf`) | `kg.json:99844` (id `Obligacion_los_clientes_de_la_entidad_tanto_residentes_en_el_pais_de_los_sectores_publico_y_e1946e`) | — (el catálogo no tiene normas) |
| `Obligados a clasificar deudores (Clasificación)` | `kg.json:288632` | `esquema_v2_clases.json:889-890` |
| `Entidades financieras` | `kg.json:267291` | `esquema_v2_clases.json:69-70` |
| `Bancos` | `kg.json:264951` | `esquema_v2_clases.json:89-90` |
| `Bancos comerciales` | `kg.json:265063` | `esquema_v2_clases.json:104-105` |

| Arista | Objeto en `kg.json` (source/target/relation) | En el catálogo |
|---|---|---|
| norma `--aplica_a-->` rol | `kg.json:657505-657537` (`:657506-657508`) | — (el catálogo no tiene normas: guarda el rol, `:889-890`) |
| `Entidades financieras --miembro_de-->` rol | `kg.json:1013875-1013900` (`:1013876-1013878`) | `miembros` del rol, `esquema_v2_clases.json:893-900`, con la entidad en `:894` |
| `Bancos --subclase_de--> Entidades financieras` | `kg.json:1012372-1012397` (`:1012373-1012375`) | `"padre"`, `esquema_v2_clases.json:92` |
| `Bancos comerciales --subclase_de--> Bancos` | `kg.json:1012433-1012458` (`:1012434-1012436`) | `"padre"`, `esquema_v2_clases.json:107` |

Cada arista aparece **una sola vez** en `kg.json`. Para verlas:
`sed -n '657506,657508p;1013876,1013878p;1012373,1012375p;1012434,1012436p' data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json`.

Las cuatro son aristas reales del grafo vigente y están entre las 17 que la
figura dibuja una a una (no son agregados de un nodo colapsado). El script
asserta además que el camino es una **cadena conexa**: cada arista une dos
nodos consecutivos de la lista, en un sentido o en el otro.

**El tramo compartido.** El tronco de `miembro_de` lo recorren los tres
miembros dibujados, pero el camino solo lo usa desde el rol hasta el diente
de `Entidades financieras`. El resalte cubre exactamente ese tramo y el
tronco sigue atenuado por debajo. Que el corte caiga justo ahí depende de que
`Entidades financieras` sea el miembro más alto del dibujo: el script lo
asserta.

**El sentido de las flechas** es el del artefacto: el `source` es el hijo,
el miembro o la norma, y el `target` el padre o el rol. Recorrer el camino
con el dedo va dos pasos a favor de las flechas (`aplica_a`, `miembro_de`) y
dos en contra (`subclase_de` hacia abajo del árbol).

## 4. Qué se dibujó y qué se colapsó

### Clases — 12 dibujadas + 46 colapsadas = 58

Dibujadas (una caja cada una, con el `label` del artefacto; línea del `id`
en `esquema_v2_clases.json` entre paréntesis): `Sujetos` (:5),
`Sujetos regulados` (:17), `Contrapartes` (:31), `Organismos públicos` (:43),
`Estructuras y vehículos` (:57), `Entidades financieras` (:69), `Bancos`
(:89), `Bancos comerciales` (:104), `Entidades cambiarias` (:152),
`Proveedores no financieros de crédito` (:239),
`Empresas no financieras emisoras de tarjetas de crédito y/o compra` (:253),
`Fiduciarios de fideicomisos financieros` (:281).

Colapsadas — cada rama no expandida es **un** nodo que declara cuántas clases
contiene. El grupo de un nodo colapsado es el conjunto de clases cuyo
**ancestro dibujado más cercano** es el padre de ese nodo, derivado del campo
`padre` del catálogo; los grupos son disjuntos y su unión es exactamente el
complemento de lo dibujado (asertado por el script). Sin cambios respecto de
la versión 3:

| Nodo colapsado | Cuelga de | Clases que contiene | Aristas `subclase_de` directas que representa su trazo |
|---|---|---|---|
| `+15 clases` | Sujetos regulados | 15 | 8 |
| `+3 clases` | Entidades financieras | 3 | 3 |
| `+2 clases` | Entidades cambiarias | 2 | 2 |
| `+17 clases` | Contrapartes | 17 | 11 |
| `+5 clases` | Organismos públicos | 5 | 4 |
| `+4 clases` | Estructuras y vehículos | 4 | 3 |
| | | **46** | **31** |

Suma: 15 + 3 + 2 + 17 + 5 + 4 = 46, y 12 + 46 = 58. La tabla sale del
reporte del script (bloque «BIYECCIÓN») y se recomputa desde el SVG con el
comando del §5 (`clases 12 + 46`).

### Instancias — 2 dibujadas + 5 declaradas = 7

Dibujadas: **BCRA** (`esquema_v2_clases.json:771`) y **SEFyC** (`:782`),
colgando de `Organismos públicos` por `instancia_de`. En la caja entra solo
la sigla, prefijo literal del `label` antes del paréntesis (el script lo
asserta y el SVG conserva la etiqueta completa en `data-label-artefacto`).
Las 5 restantes van en el nodo colapsado `+5 instancias`. Recomputo desde el
SVG (devuelve `2 ['5']`: 2 dibujadas y un nodo que declara 5):
`python3 -c "import re;svg=open('docs/tesis/figuras/figura_catalogo_sujetos.svg',encoding='utf-8').read();print(len(re.findall(r'data-forma=\"instancia\"',svg)),re.findall(r'data-nodo=\"INSTCOL\" data-forma=\"colapsada\" data-colapsa=\"(\d+)\"',svg))"`.

### Rol — 1 de los 5 del catálogo; 3 de sus 6 miembros

Se dibuja `Obligados a clasificar deudores (Clasificación)`
(`esquema_v2_clases.json:889-890`; procedencia declarada en el catálogo:
«Secciones 1 y 10» del TO de Clasificación de deudores). La caja lleva la
etiqueta completa del artefacto, con el paréntesis que lo distingue de los
roles de los otros TOs. El rol tiene **6 miembros** (`:893-900`) y el grafo
le da exactamente esos seis `miembro_de` (asertado). La figura dibuja los
**3 que ya son clases dibujadas del árbol** —`Entidades financieras`,
`Proveedores no financieros de crédito` y
`Fiduciarios de fideicomisos financieros`— y **declara los otros 3 en la
propia caja del rol** («6 miembros · 3 dibujados»): `Sociedades de garantía
recíproca`, `Fondos de garantía de carácter público` y `Proveedores de
servicios de créditos entre particulares a través de plataformas (PSCPP)`.
Los tres cuelgan directamente de `Sujetos regulados` y caen dentro del nodo
`+15 clases`: la figura no los pierde, los cuenta y los declara.

`Entidades cambiarias` y `Empresas no financieras emisoras de tarjetas de
crédito y/o compra` siguen dibujadas como parte del árbol, pero no son
miembros de este rol y ya no reciben un diente `miembro_de`.

Los otros 4 roles del catálogo no se dibujan: la figura ilustra el mecanismo
de la indirección, no el inventario de roles.

### La norma

`Clasificación de clientes según calidad de obligados` (tipo `Obligacion`,
punto 1.1, página 4 del Texto Ordenado de Clasificación de deudores). Es un
nodo real del grafo vigente, una de las **239** aristas `aplica_a` que
apuntan a ese rol, y se dibuja con su `label` tomado del propio grafo. Su
subtítulo es «Obligacion · punto 1.1»: el tipo se escribe como identificador
del esquema, sin tilde, igual que en F1; las etiquetas en castellano llevan
tilde. Recomputo del 239:
`python3 -c "import json;kg=json.load(open('data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json'));print(sum(1 for e in kg['edges'] if e['relation']=='aplica_a' and e['target']=='Sujeto_rol_obligado_a_clasificar_clasificacion'))"`.

En el grafo, el nodo de la norma tiene dos aristas salientes y ninguna
entrante: `aplica_a` al rol y `establecida_en` al Texto Ordenado; ninguna
apunta a una clase del catálogo. Su texto (unidad `cla::1.1` de
`data/experiment/reextraccion_v2/e0_chunking/salida/chunks_cla.json`) dice
«Los clientes de la entidad (...) deberán ser clasificados», y «Clientes» es
la etiqueta de una clase del catálogo (`Sujeto_cliente`, hija de
Contrapartes, `esquema_v2_clases.json:437-440`): el punto nombra a quiénes
se clasifica, no a quién está obligado a clasificar. No menciona «bancos» ni
«entidades financieras». Por eso el epígrafe de
`bloque_latex_figura_catalogo.tex` no dice que el deber «no nombra a ninguna
clase» —lo que contradecía ese «Clientes»— sino que «no nombra a quién
obliga, sino que apunta con \texttt{aplica\_a} al rol de alcance del
documento»: la objeción quedó resuelta con ese cambio de redacción.

## 5. Aristas — 53 representadas, todas verificadas contra el grafo vigente

Conteos globales del grafo vigente, asertados por el script antes de dibujar:
`subclase_de` 57, `instancia_de` 7, `miembro_de` 17, `parte_de` 1.

| | Trazos | Aristas del grafo que representan |
|---|---|---|
| Explícitos (un trazo = una arista) | 17 | 17 |
| Agregados (un trazo = N aristas hacia un nodo colapsado) | 7 | 36 |
| | **24** | **53** |

Las 17 explícitas: 11 `subclase_de` (el árbol dibujado), 2 `instancia_de`
(BCRA y SEFyC), 3 `miembro_de` (los miembros dibujados) y 1 `aplica_a` (la
norma al rol): 11 + 2 + 3 + 1 = 17. Las 36 agregadas: 31 `subclase_de` de los
seis nodos colapsados de clases (tabla del §4) y 5 `instancia_de` del nodo
`+5 instancias`. Respecto de la versión 3 (55 = 19 + 36) bajan 2: el rol
nuevo tiene dos miembros dibujados menos.

La capa del camino **no agrega aristas**: repite cuatro de las 17 explícitas
con la otra intensidad, encima. Por eso sus trazos llevan `data-camino` y no
`data-rel`. La muestra de la leyenda tampoco lleva `data-camino`, para que
el recuento del camino desde el SVG dé 4.

**Recómputo desde el SVG**, sin volver a correr el script:

```bash
python3 -c "import re,collections;svg=open('docs/tesis/figuras/figura_catalogo_sujetos.svg',encoding='utf-8').read();print(dict(sorted(collections.Counter(re.findall(r'data-forma=\"([^\"]+)\"',svg)).items())));print('clases',sum(1 for _ in re.finditer(r'data-nodo=\"(?!COL:|INSTCOL)[^\"]+\" data-forma=\"clase\"',svg)),'+',sum(int(x) for x in re.findall(r'data-clases=\"(\d+)\"',svg)));print(dict(sorted(collections.Counter(re.findall(r'data-rel=\"([^\"]+)\"',svg)).items())));print('aristas',len(re.findall(r'data-src=',svg)),'+',sum(int(x) for x in re.findall(r'data-agrega=\"(\d+)\"',svg)));print('camino: nodos',len(re.findall(r'<g [^>]*data-camino=\"1\"',svg)),'trazos',len(re.findall(r'<path [^>]*data-camino=\"1\"',svg)))"
```

devuelve `{'clase': 12, 'colapsada': 7, 'instancia': 2, 'norma': 1, 'rol': 1}`,
`clases 12 + 46`, `{'aplica_a': 1, 'instancia_de': 3, 'miembro_de': 3,
'subclase_de': 17}`, `aristas 17 + 36` y `camino: nodos 5 trazos 4`. (Los 17
trazos `subclase_de` son 11 explícitos + 6 agregados; los 3 `instancia_de`,
2 explícitos + 1 agregado.)

Y que esas aristas existen en el grafo:

```bash
python3 -c "import re,json;svg=open('docs/tesis/figuras/figura_catalogo_sujetos.svg',encoding='utf-8').read();kg=json.load(open('data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json'));E={(e['source'],e['relation'],e['target']) for e in kg['edges']};tr=[m.groups() for m in re.finditer(r'data-dst=\"([^\"]+)\" data-rel=\"([^\"]+)\" data-src=\"([^\"]+)\"',svg)];print(len(tr),sum(1 for d,r,s in tr if (s,r,d) in E))"
```

devuelve `17 17`.

## 6. Fuente de cada dato de la figura

| Dato | Fuente |
|---|---|
| Las 12 clases dibujadas y sus etiquetas | campo `label` de cada entrada, `esquema_v2_clases.json` (líneas del §4) |
| Los conteos `+N clases` | campo `padre` del catálogo, agrupado por ancestro dibujado más cercano (script, §2 del código; reporte «BIYECCIÓN») |
| BCRA, SEFyC y `+5 instancias` | `esquema_v2_clases.json:771`, `:782` y las 7 entradas `"nivel": "instancia"` |
| El rol, su etiqueta y «6 miembros · 3 dibujados» | `esquema_v2_clases.json:889-900` |
| La norma y «Obligacion · punto 1.1» | `kg.json:99844` (`label`, `type` y `provenance.punto` del nodo) |
| Cada trazo explícito | una arista de `kg.json` (comando del §5; las cuatro del camino, con línea, en el §3) |
| Cada trazo agregado | las aristas `subclase_de`/`instancia_de` directas hacia el padre dibujado, verificadas una por una contra `kg.json` |
| Rótulos de relación | nombre de la relación en `kg.json` (`subclase_de`, `instancia_de`, `miembro_de`, `aplica_a`) |
| Leyenda | texto de la figura, no dato |

## 7. Convenciones de dibujo (declaradas)

- **Dos intensidades, legibles en blanco y negro.** El camino va con borde de
  4,0 px y relleno al 34 % del color del tipo; el resto, con borde de 1,9 px
  y relleno al 6 %. Las aristas: 4,6 px el camino, 1,9 px el resto, con el
  color mezclado un 42 % con el fondo fuera del camino y con la punta un 45 %
  más grande sobre el camino. El mecanismo es el de la versión 3, que se
  verificó en escala de grises; esta versión no lo cambia.
- **El texto no se atenúa.** La atenuación vive en el borde y el relleno de
  las cajas; las etiquetas quedan todas al mismo negro.
- **Cinco formas, distinguibles sin color**: clase = rectángulo de trazo
  continuo; rama no expandida = rectángulo apilado de trazo discontinuo;
  instancia = píldora; rol de alcance = hexágono de trazo raya-punto; norma =
  rectángulo con la esquina superior derecha plegada.
- **Cuatro relaciones, distinguibles por patrón de línea Y por forma de
  punta**: `subclase_de` continua con punta de triángulo hueco;
  `instancia_de` discontinua con punta llena chica; `miembro_de` raya-punto
  con punta llena de cola cóncava; `aplica_a` continua con punta llena
  grande. Las cuatro llevan su nombre sobre el trazo.
- **Peines**: cuando varias aristas de la misma relación terminan en la misma
  caja, los trazos confluyen en un tronco con una única punta y un único
  rótulo, como en F1/F1b.
- **Los rótulos van en una capa final**, al costado de su tronco, nunca
  encima: cada rótulo prueba una lista de candidatos y se queda con el
  primero que no toca ninguna caja, ningún otro rótulo ni ningún trazo; si
  ninguno pasa, la generación FRENA. En esta versión el rótulo `miembro_de`
  quedó en el mismo candidato que en la versión 3 (el 8 de 60), 17 px más
  abajo porque la banda superior creció.
- **Etiquetas** en castellano y tomadas del campo `label` del artefacto,
  nunca del `id`, con la única abreviatura de las dos siglas de instancia.
  Los identificadores del esquema (`Obligacion`, las cuatro relaciones) van
  sin tilde, como en el código.
- **Sin conteos de uso**: los únicos números de la figura son estructurales.
- **La leyenda va dentro del dibujo**, en el cuadrante inferior derecho que
  el árbol deja libre.
- **`parte_de` no se dibuja**: el grafo tiene una sola arista de esa
  relación (`SEFyC parte_de BCRA`).
- **Cruces de línea**: 3 puntos, todos entre trazos finos y ninguno sobre una
  caja: el tronco de `miembro_de` (x = 757) cruza los tres tramos
  horizontales que llevan la punta de `subclase_de` a `Entidades
  financieras` (y = 303,5), a `Entidades cambiarias` (y = 428) y a
  `Proveedores no financieros de crédito` (y = 562). Son los mismos tres de
  la versión 3, 34 px más abajo. Medido sobre el SVG con
  `cruces_catalogo.py` (paquete de revisión de esta versión), que es el
  comando de la versión 3 pasado a archivo:
  `[(757.0, 303.5), (757.0, 428.0), (757.0, 562.0)] 3`.
- La guarda de trazos sobre texto corre sobre las 23 cajas y los 47
  segmentos del dibujo (49 en la versión 3: dos dientes `miembro_de` menos):
  0 trazos dentro de una caja y 0 trazos sobre un rótulo.

## 8. Historial de versiones

- **Versión 1**: el catálogo fiel, sin destacar el camino.
- **Versión 2**: tres cambios — el camino resaltado (cinco nodos y cuatro
  aristas en trazo grueso, con el resto atenuado y una entrada propia en la
  leyenda); las instancias por su sigla; y el piso tipográfico de 8 pt
  asertado por el script. Para pagar el piso se podaron los subtítulos
  internos de las cajas y se acortaron las notas de la leyenda.
- **Versión 3**: corrección de trazos sobre texto. El rótulo `subclase_de`
  del peine de «Sujetos regulados» se leía «subclase_ae» porque una caja
  dibujada después le pintaba encima los últimos caracteres; la búsqueda de
  huecos no fusionaba bandas solapadas. Se corrigió con la fusión de bandas y
  con la capa final de rótulos más la guarda de trazos contra cajas y
  rótulos, que se comprobó no vacua rompiendo la figura a propósito.
- **Versión 4** (esta): el camino pasa al ejemplo de Clasificación de
  deudores (norma del punto 1.1, rol de 6 miembros con 3 dibujados), el
  subtítulo de la norma lleva el tipo como identificador del esquema, y el
  PDF pasa a exportarse con `SOURCE_DATE_EPOCH=0`. Árbol, ramas colapsadas y
  leyenda sin cambios.

## 9. Tamaño de impresión

El informe es `a4paper` con márgenes laterales de 3 cm (`main.tex:9`), es
decir `\linewidth` = 210 − 30 − 30 = **150 mm**; con márgenes superior e
inferior de 2 cm, la caja de texto mide **257 mm** de alto.

Insertada con `width=\linewidth`, la figura mide **150 × 137,7 mm**
(137,7 = 1295 ⁄ 1410,8 × 150; en la versión 3, 134,1). Crece 3,6 mm porque la
etiqueta de la norma ocupa tres líneas en vez de dos y la banda superior
gana 34 px de alto; el ancho del lienzo no cambia, de modo que la tipografía
tampoco:

| Cuerpo | px | pt impresos |
|---|---|---|
| etiqueta de nodo | 29 | **8,74** |
| subtítulo de caja | 27 | **8,14** |
| rótulo de relación | 27 | **8,14** |
| leyenda | 27 | **8,14** |

(Valores del reporte del script, bloque «TIPOGRAFÍA».) El piso de 8 pt es un
`assert` del script.

**Qué archivo toma LaTeX.** El bloque inserta sin extensión, de modo que
`pdflatex` toma el **PDF vectorial**; el PNG queda como respaldo. Por eso el
PDF se regenera junto con el PNG: si quedara el de la versión 3, el informe
seguiría mostrando el camino anterior.

**Epígrafe.** `bloque_latex_figura_catalogo.tex` lleva el epígrafe de esta
versión (camino del punto 1.1 de Clasificación de deudores, «El rol tiene 6
miembros y se dibujan 3»), de 710 caracteres; el de la versión 3 describía el
camino de Protección de usuarios. Los comentarios de cabecera de ese bloque
(150 × 134,1 mm, 194 a 199 mm) siguen con las medidas de la versión 3.

**NO VERIFICADO**: el alto del bloque completo con epígrafe no se midió por
compilación (en el entorno donde se generó la figura no hay LaTeX). La
estimación de la versión 3 (194 a 199 mm, para un epígrafe de 770
caracteres) sube a lo sumo los 3,6 mm de la figura; el epígrafe nuevo es algo
más corto, así que la cuenta no debería crecer por ese lado, pero eso también
es estimación.

## 10. Layout

Árbol de izquierda a derecha, una columna por nivel de profundidad (5
columnas: raíz, primer nivel, segundo, tercero, cuarto). Las filas se
asignan a las hojas dibujadas en el orden del artefacto, y cada padre se
ubica en el punto medio entre su primer y su último hijo. Los anchos de
columna se calculan del texto ya envuelto, con un tope por columna (189, 245,
259, 303 y 192 px).

La banda superior lleva la norma (apoyada en el margen izquierdo, que el
árbol deja libre) y el rol, centrado sobre el tronco de `miembro_de` que baja
hacia sus miembros; el tramo de `aplica_a` entre las dos se asserta lo
bastante largo como para que su rótulo entre. El camino se recorre de arriba
a la izquierda hacia abajo y a la derecha: `aplica_a` de la norma al rol,
`miembro_de` del rol a `Entidades financieras`, `subclase_de` a `Bancos` y a
`Bancos comerciales`.
