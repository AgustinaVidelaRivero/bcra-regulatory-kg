# figura_catalogo_sujetos (F2) — registro de generación

Figura F2 del capítulo del esquema: el **catálogo de sujetos** —el árbol de
clases, sus instancias y la indirección por rol de alcance que permite que
una norma alcance a una subclase que no nombra—. Generada POR SCRIPT desde
los artefactos sellados, nunca dibujada a mano, como F1 y F1b.

Este LEEME describe la **quinta versión**: el mismo trazado de la cuarta
(las mismas 12 clases dibujadas, ramas colapsadas en nodos que declaran
cuántas clases contienen, instancias por su sigla y el camino del deber del
punto 1.1 de Clasificación de deudores en trazo grueso hasta los bancos
comerciales), con el **catálogo final** y el **grafo de la tanda 0 con el
perfil final**, y con `miembro_de` reruteado para que la figura no tenga
cruces de línea:

| | Versión 4 | Versión 5 |
|---|---|---|
| Catálogo | `esquema_v2_clases.json` v2.0: 58 clases, 7 instancias, 5 roles | `catalogo_sujetos_r2.json` r2: 70 clases, 5 instancias, 35 roles (+ 5 lápidas) |
| Grafo | `salida_r1/kg.json` | `corpus_tanda0/ens_diez_r2b/r2/kg.json` |
| Clases | 12 dibujadas + 46 colapsadas = 58 | 12 dibujadas + 58 colapsadas = 70 |
| Instancias | 2 dibujadas + 5 en «+5 instancias» = 7 | 2 dibujadas + 2 en «+2 instancias» + 1 declarada en la rama colapsada de Organismos públicos = 5 |
| Norma | «Clasificación de clientes según calidad de obligados» | «Clasificar clientes por calidad de obligados» (la etiqueta del grafo r2b) |
| Rol | `Obligados a clasificar deudores (Clasificación)`, 6 miembros, 3 dibujados | igual |
| Trazos / aristas representadas | 24 / 53 | 24 / 59 |
| Cruces de línea | 3 | **0** |
| Lienzo | 1410,8 × 1295 px; 15 × 13,77 cm | 1428,8 × 1328 px; **15 × 13,94 cm** |

La historia de las versiones está en el §11.

## 1. Comando de generación

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_catalogo_sujetos.py
```

Escribe `figura_catalogo_sujetos.svg` (1428,8 × 1328) junto al script e
imprime el reporte de verificación. Con `--salida <ruta>` escribe el SVG en
otra ruta (`generar_figura_catalogo_sujetos.py:97-101`): así se regenera para
verificar sin escribir en el repositorio. De ahí salen el PDF vectorial y el
PNG:

```bash
SOURCE_DATE_EPOCH=0 rsvg-convert -f pdf -o docs/tesis/figuras/figura_catalogo_sujetos.pdf docs/tesis/figuras/figura_catalogo_sujetos.svg
```

```bash
rsvg-convert -z 2 -f png -o docs/tesis/figuras/figura_catalogo_sujetos.png docs/tesis/figuras/figura_catalogo_sujetos.svg
```

`rsvg-convert` (2.62.3, cairo 1.18.4; `rsvg-convert --version`) es la única
herramienta externa, y solo para esas dos exportaciones. El SVG se produce
con Python de la biblioteca estándar, sin dependencias; corre con el `.venv`
del repositorio.

| Archivo | Medida propia | Peso |
|---|---|---|
| `figura_catalogo_sujetos.svg` (fuente) | 1428,8 × 1328 px | 28.596 bytes |
| `figura_catalogo_sujetos.pdf` (vectorial) | 1071,6 × 996 pt = 378,04 × 351,37 mm | 63.632 bytes |
| `figura_catalogo_sujetos.png` (rasterizado) | 2858 × 2656 px = 484 dpi a 150 mm de ancho | 668.430 bytes |

Recomputo: `stat -f '%N %z' docs/tesis/figuras/figura_catalogo_sujetos.*`,
`pdfinfo docs/tesis/figuras/figura_catalogo_sujetos.pdf | grep 'Page size'` y
`file docs/tesis/figuras/figura_catalogo_sujetos.png`.

`rsvg-convert` lee las unidades de usuario del SVG como píxeles CSS (1/96 de
pulgada) y las escribe como puntos (1/72): 1428,8 × 0,75 = 1071,6 y
1328 × 0,75 = 996. Como el bloque LaTeX inserta con `width=\linewidth`, la
figura se escala a 150 mm venga de donde venga.

**El PDF es vectorial**: `pdfimages -list` no lista ninguna imagen, y
`pdffonts` lista las mismas familias que la versión 4 (Helvetica, -Bold,
-Oblique, Menlo-Regular, Arial-ItalicMT, más los Type 3 que cairo arma para
los glifos fuera de WinAnsi).

El script FRENA con `AssertionError` antes de escribir el SVG si:

- el sha256 de alguna de las dos fuentes no es el del candado (`:109-110`,
  comprobado sobre los bytes en `:113-118`, antes de interpretar el JSON);
- el catálogo deja de tener 70 clases, 5 instancias, 35 roles, 110 vigentes
  y 5 lápidas (`:136-140`), deja de tener raíz única (`:150`), o las cuatro ramas de la raíz dejan
  de medir 38, 20, 6 y 5 clases (`:161-166`);
- las relaciones de pertenencia del catálogo dejan de ser 69 `subclase_de`,
  5 `instancia_de`, 51 `miembro_de` y 1 `parte_de` (`:179-183`), o las del
  grafo dejan de ser **exactamente las mismas aristas**, una por una
  (`:291-299`);
- la cadena Sujetos → … → Bancos comerciales deja de ser la del catálogo
  (`:191-197`); el rol deja de tener 6 miembros o sus `miembro_de` en el
  grafo dejan de ser los del catálogo (`:202`, `:302-304`); la norma deja de
  ser la única Obligacion del punto 1.1 de Clasificación de deudores, con la
  etiqueta «Clasificar clientes por calidad de obligados» (`:384-390`); o la
  etiqueta de una clase o instancia dibujada difiere entre el grafo y el
  catálogo (`:374-376`);
- lo dibujado más lo colapsado no suma 70, los grupos colapsados se solapan
  o no cubren el resto (`:251-255`), o alguna instancia o miembro no
  dibujado queda sin declarar (`:266-281`);
- el camino resaltado deja de ser una cadena conexa de aristas explícitas
  del grafo (`:347-360`), alguna arista dibujada no está en el grafo o
  aparece dos veces (`:363-368`);
- algún texto desborda su caja (`:539`), dos cajas se solapan (`:1133`),
  algún rótulo no encuentra lugar libre (`:1409`), algún trazo entra en una
  caja o cruza un rótulo (`:1443`), o algún cuerpo tipográfico cae por
  debajo de 8 pt impresos a `width=\linewidth` (`:1111`);
- **nuevo en esta versión**: hay algún cruce de línea, algún contacto o
  solape entre trazos de peines distintos (`:1497-1499`), o la capa del
  camino resalta un tramo que no está dibujado debajo (`:1503-1513`).

(Las referencias `:N` de este LEEME sin archivo son líneas de
`generar_figura_catalogo_sujetos.py`.)

## 2. Fuentes y sellos

| Archivo leído | sha256 | Commit |
|---|---|---|
| `data/experiment/catalogo_unico/catalogo_sujetos_r2.json` (catálogo r2, `"version": "r2"` en `:3` del archivo) | `c3ad15811c7ea5fa2d0f6cbd56dc775c38dcffd0ae8874c22f5f45c1e82d3a83` | `bd2122d` |
| `data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2b/r2/kg.json` (grafo KG-Tanda0-Diez-r2b) | `a9631a64b422bdae634fb05135373c6f04c6272cdf7acd43a1be9f5b6c1f5f57` | `bbc38dc` |

Los dos sha son el candado del script (`:109-110`). El del grafo y su
commit son los del registro de grafos (`data/experiment/neo4j/grafos.py:138`
y `:139`, entrada `KG_Tanda0_Diez_r2b`). Los dos archivos están en el árbol
byte-idénticos a su commit:

```bash
git show bd2122d:data/experiment/catalogo_unico/catalogo_sujetos_r2.json | shasum -a 256
```

```bash
git show bbc38dc:data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2b/r2/kg.json | shasum -a 256
```

dan los sha de la tabla, y `git log --oneline -1 -- <ruta>` da esos dos
commits como el último que tocó cada archivo.

Salidas de esta corrida:

| Archivo | sha256 |
|---|---|
| `figura_catalogo_sujetos.svg` | `a058a56d24a7d87d0436a2fce68a527acae91fdbf013000cb6fd92e87943f4da` |
| `figura_catalogo_sujetos.pdf` | `a36060b5a845370ec1938d6490a242e6b8820116147ce349977cbdb89e78fb0c` |
| `figura_catalogo_sujetos.png` | `72208ab6e5b985bc4199c23c728cc0b3c622bbd32651a78035d795afbbd88002` |
| `generar_figura_catalogo_sujetos.py` (script, versionado junto a la figura) | `6df047deb1df1c2807635923ed078cd5d526ddb738fdc373b06dfa7ae36af862` |

**Generación determinística**: tres corridas con `PYTHONHASHSEED` 1, 2 y 3
y una desde un directorio de trabajo ajeno dan el mismo SVG (`a058a56d…`); el
script no usa rutas absolutas. Doce exportaciones seguidas del PDF con
`SOURCE_DATE_EPOCH=0` dieron el mismo sha (`a36060b5…`) y tres del PNG,
el mismo (`72208ab6…`). El PDF declara `CreationDate: Wed Dec 31 21:00:00
1969 -03` (`pdfinfo`), el instante 0 en hora local. Como en la versión 4,
el sello firme es el del SVG (`LEEME_figura_controles.md` §1 documenta un
orden de empaquetado del `/ObjStm` que cairo no fija).

## 3. El camino resaltado

Es la pieza que la figura existe para mostrar: **cinco nodos y cuatro
aristas** en trazo grueso y relleno saturado, con todo el resto atenuado.
Las líneas son de `ens_diez_r2b/r2/kg.json` (`kg.json`) y de
`catalogo_sujetos_r2.json` (el catálogo):

| Nodo | `kg.json` | Catálogo |
|---|---|---|
| `Clasificar clientes por calidad de obligados` (tipo `Obligacion`, punto 1.1, página 4 de `TO_clasificacion_deudores_actual.pdf`) | `:237780` (id `Obligacion_los_clientes_de_la_entidad_tanto_residentes_en_el_pais_de_los_sectores_publico_y_8b3c06`), procedencia `:237787-237801` (punto en `:237790`, página en `:237796`) | — (el catálogo no tiene normas) |
| `Obligados a clasificar deudores (Clasificación)` | `:427886` | `:3209`, etiqueta `:3211` |
| `Entidades financieras` | `:406954` | `:872`, etiqueta `:874` |
| `Bancos` | `:401063` | `:943`, etiqueta `:945` |
| `Bancos comerciales` | `:403340` | `:983`, etiqueta `:985` |

| Arista | Objeto en `kg.json` (source/target/relation) | En el catálogo |
|---|---|---|
| norma `--aplica_a-->` rol | `:1145167-1145203` (`:1145168-1145170`) | — (el catálogo no tiene normas) |
| `Entidades financieras --miembro_de-->` rol | `:1609831-1609856` (`:1609832-1609834`) | `miembros` del rol, `:3225-3232`, con la entidad en `:3226` |
| `Bancos --subclase_de--> Entidades financieras` | `:1607238-1607263` (`:1607239-1607241`) | `"padre"`, `:948` |
| `Bancos comerciales --subclase_de--> Bancos` | `:1607290-1607315` (`:1607291-1607293`) | `"padre"`, `:988` |

Para verlas:
`sed -n '1145168,1145170p;1609832,1609834p;1607239,1607241p;1607291,1607293p' data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2b/r2/kg.json`.

Las cuatro son aristas reales del grafo y están entre las 17 que la figura
dibuja una a una (`:356-357`). El script asserta además que el camino es una
**cadena conexa** (`:347-353`).

**El tramo de `miembro_de`.** En la versión 4 el camino subía por el tronco
común de los tres miembros dibujados. En esta, el diente de `Entidades
financieras` sube recto desde el centro de su borde superior hasta el lado
inferior del rol (`:680`, `:688-689`), y el resalte cubre exactamente ese
diente más el tramo común que lleva la punta; el canal de los otros dos
miembros (§8) sigue atenuado. La guarda de `:1503-1513` comprueba que cada
tramo resaltado cae entero sobre tramos dibujados de la misma relación.

**El sentido de las flechas** es el del artefacto: el `source` es el hijo,
el miembro o la norma, y el `target` el padre o el rol. Recorrer el camino
con el dedo va dos pasos a favor de las flechas (`aplica_a`, `miembro_de`) y
dos en contra (`subclase_de` hacia abajo del árbol).

**Dos marcas del grafo sobre este camino, que la figura no dibuja.**

1. La arista `aplica_a` se resolvió por la sugerencia del modelo
   (`"metodo_resolucion": "R4_sugerencia_modelo"`, `kg.json:1145202`), con la
   mención «los sujetos obligados» (`:1145199`) marcada como no verificada
   (`"mencion_verificada": "no"`, `:1145200`). El texto del punto
   (`provenance.tramo`, `kg.json:237792`) no contiene esa frase:
   `python3 -c "import json;kg=json.load(open('data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2b/r2/kg.json'));n=[x for x in kg['nodes'] if x['id'].endswith('_8b3c06') and x['type']=='Obligacion'][0];t=n['provenance']['tramo'].lower();print('sujetos obligados' in t,'banco' in t,'entidades financieras' in t,'clientes' in t)"`
   da `False False False True`. Es coherente con lo que el epígrafe dice
   del punto (no nombra a quién obliga; nombra a los clientes, que es una
   clase de Contrapartes).
2. El nodo del rol lleva la marca de la cola humana: `"cola_humana": "true"`,
   `"cola_chunks": ["cla::6.5.3.1"]` y
   `"estado_e3": "cola_humana_veredicto_inutilizable"` (`kg.json:427891-427895`).
   La marca viene de la unidad `cla::6.5.3.1`, no del punto 1.1.

## 4. Qué se dibujó y qué se colapsó

### Clases — 12 dibujadas + 58 colapsadas = 70

Dibujadas (una caja cada una, con el `label` del catálogo; línea del `id`
en `catalogo_sujetos_r2.json` entre paréntesis): `Sujetos` (:678),
`Sujetos regulados` (:716), `Contrapartes` (:756), `Organismos públicos`
(:794), `Estructuras y vehículos` (:834), `Entidades financieras` (:872),
`Bancos` (:943), `Bancos comerciales` (:983), `Entidades cambiarias`
(:1138), `Proveedores no financieros de crédito` (:1383),
`Empresas no financieras emisoras de tarjetas de crédito y/o compra`
(:1425), `Fiduciarios de fideicomisos financieros` (:1507). Son las mismas
12 de la versión 4 (`CLASES_DIBUJADAS`, `:212-225`), y el script comprueba
que su etiqueta en el grafo es la del catálogo (`:374-376`).

Colapsadas — cada rama no expandida es **un** nodo que declara cuántas
clases contiene. El grupo de un nodo colapsado es el conjunto de clases cuyo
**ancestro dibujado más cercano** es el padre de ese nodo, derivado del campo
`padre` del catálogo; los grupos son disjuntos y su unión es exactamente el
complemento de lo dibujado (`:251-255`).

| Nodo colapsado | Cuelga de | Clases que contiene | Aristas `subclase_de` directas que representa su trazo | Versión 4 |
|---|---|---|---|---|
| `+25 clases` | Sujetos regulados | 25 | 15 | +15 (8) |
| `+3 clases` | Entidades financieras | 3 | 3 | +3 (3) |
| `+2 clases` | Entidades cambiarias | 2 | 2 | +2 (2) |
| `+19 clases` | Contrapartes | 19 | 13 | +17 (11) |
| `+5 clases` · `+1 instancia` | Organismos públicos | 5 | 4 | +5 (4) |
| `+4 clases` | Estructuras y vehículos | 4 | 3 | +4 (3) |
| | | **58** | **40** | 46 (31) |

Suma: 25 + 3 + 2 + 19 + 5 + 4 = 58, y 12 + 58 = 70. Las aristas directas:
15 + 3 + 2 + 13 + 4 + 3 = 40. La tabla sale del reporte del script (bloque
«BIYECCIÓN») y se recomputa desde el SVG con el comando del §5
(`clases 12 + 58`). Por rama de la raíz (la clase de la rama incluida, como las cuenta el
script en `:161-166`): Sujetos regulados, 8 dibujadas (Sujetos regulados,
Entidades financieras, Bancos, Bancos comerciales, Entidades cambiarias,
Proveedores no financieros de crédito, Empresas no financieras emisoras de
tarjetas de crédito y/o compra, Fiduciarios de fideicomisos financieros)
+ 3 + 2 + 25 colapsadas = 38; Contrapartes 1 + 19 = 20; Organismos públicos
1 + 5 = 6; Estructuras y vehículos 1 + 4 = 5. Y 38 + 20 + 6 + 5 = 69, más
la raíz, 70.

### Instancias — 2 dibujadas + 2 en su nodo + 1 en una rama = 5

Dibujadas: **BCRA** (`catalogo_sujetos_r2.json:2921`) y **SEFyC** (`:2958`),
colgando de `Organismos públicos` por `instancia_de` (`:2966` para SEFyC).
En la caja entra solo la sigla, prefijo literal del `label` antes del
paréntesis (el script lo asserta y el SVG conserva la etiqueta completa en
`data-label-artefacto`).

El nodo `+2 instancias` agrupa las dos que son instancia **directa** de
`Organismos públicos` y no se dibujan: ARCA (`:2997`) y Ministerio de
Economía (`:3037`). Su trazo representa esas dos aristas `instancia_de`.

La quinta, **FMI** (`:3626`), es instancia de `Organismos internacionales`
(`"instancia_de": "Sujeto_organismo_internacional"`, `:3634`), una clase que
cae dentro del nodo colapsado de `Organismos públicos`. Ese nodo la declara
en su subtítulo («+1 instancia»; `data-instancias="1"` en el SVG), y su
arista `instancia_de` queda dentro de la rama, sin trazo, como las
`subclase_de` internas de cualquier grupo colapsado (`:263-274`). En la
versión 4 las 7 instancias eran de `Organismos públicos` y el nodo decía
«+5 instancias» (`git show 43f241e:data/experiment/grafo_v2/esquema_v2_clases.json`: las 7
entradas de `"nivel": "instancia"` tienen `"instancia_de":
"Sujeto_organismo_publico"`); de ellas, las tres Secretarías (de Energía,
de Comercio y de Transporte) son lápidas en el catálogo r2.

Recomputo desde el SVG (devuelve `2 ['2'] ['1']`: 2 dibujadas, un nodo que
declara 2 y una rama que declara 1):
`python3 -c "import re;svg=open('docs/tesis/figuras/figura_catalogo_sujetos.svg',encoding='utf-8').read();print(len(re.findall(r'data-forma=\"instancia\"',svg)),re.findall(r'data-nodo=\"INSTCOL\" data-forma=\"colapsada\" data-colapsa=\"(\d+)\"',svg),re.findall(r'data-instancias=\"(\d+)\"',svg))"`.

### Rol — 1 de los 35 del catálogo; 3 de sus 6 miembros

Se dibuja `Obligados a clasificar deudores (Clasificación)`
(`catalogo_sujetos_r2.json:3209-3211`; procedencia declarada en el catálogo:
«Secciones 1 y 10» de `TO_clasificacion_deudores_actual.pdf`, `:3220-3221`).
El rol tiene **6 miembros** (`:3225-3232`) y el grafo le da exactamente esos
seis `miembro_de` (`:302-304`). La figura dibuja los **3 que ya son clases
dibujadas del árbol** —`Entidades financieras`,
`Proveedores no financieros de crédito` y
`Fiduciarios de fideicomisos financieros`— y **declara los otros 3 en la
propia caja del rol** («6 miembros · 3 dibujados»): `Sociedades de garantía
recíproca`, `Fondos de garantía de carácter público` y `Proveedores de
servicios de créditos entre particulares a través de plataformas (PSCPP)`.
Los tres cuelgan directamente de `Sujetos regulados` y caen dentro del nodo
`+25 clases` (reporte del script, bloque «BIYECCIÓN»). La lista de miembros
es la misma de la versión 4.

Los otros 34 roles del catálogo no se dibujan: la figura ilustra el
mecanismo de la indirección, no el inventario de roles.

### La norma

`Clasificar clientes por calidad de obligados` (tipo `Obligacion`, punto
1.1, página 4 del Texto Ordenado de Clasificación de deudores;
`kg.json:237780-237801`). Es la única Obligacion de ese punto en el grafo
(`:388-390`), una de las **68** aristas `aplica_a` que apuntan a ese rol, y se
dibuja con su `label` tomado del propio grafo. Su subtítulo es «Obligacion ·
punto 1.1»: el tipo se escribe como identificador del esquema, sin tilde,
igual que en F1. Recomputo del 68:
`python3 -c "import json;kg=json.load(open('data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2b/r2/kg.json'));print(sum(1 for e in kg['edges'] if e['relation']=='aplica_a' and e['target']=='Sujeto_rol_obligado_a_clasificar_clasificacion'))"`.
(En el grafo de la versión 4, `salida_r1/kg.json`, eran 239 según su
LEEME; no comparo las dos cifras.)

En el grafo, el nodo de la norma tiene dos aristas salientes y ninguna
entrante: `aplica_a` al rol y `establecida_en` al Texto Ordenado; ninguna
apunta a una clase del catálogo:
`python3 -c "import json;kg=json.load(open('data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2b/r2/kg.json'));i=[x['id'] for x in kg['nodes'] if x['id'].endswith('_8b3c06') and x['type']=='Obligacion'][0];print([(e['relation'],e['target']) for e in kg['edges'] if e['source']==i],[e['relation'] for e in kg['edges'] if e['target']==i])"`
devuelve `[('aplica_a', 'Sujeto_rol_obligado_a_clasificar_clasificacion'),
('establecida_en', 'TextoOrdenado_to_clasificacion_deudores_actual_pdf')] []`.

## 5. Aristas — 59 representadas, todas verificadas contra el grafo

Conteos globales del grafo, asertados por el script antes de dibujar y
comparados arista por arista con el catálogo (`:291-299`): `subclase_de` 69,
`instancia_de` 5, `miembro_de` 51, `parte_de` 1.

| | Trazos | Aristas del grafo que representan |
|---|---|---|
| Explícitos (un trazo = una arista) | 17 | 17 |
| Agregados (un trazo = N aristas hacia un nodo colapsado) | 7 | 42 |
| | **24** | **59** |

Las 17 explícitas: 11 `subclase_de` (el árbol dibujado), 2 `instancia_de`
(BCRA y SEFyC), 3 `miembro_de` (los miembros dibujados) y 1 `aplica_a` (la
norma al rol): 11 + 2 + 3 + 1 = 17. Las 42 agregadas: 40 `subclase_de` de
los seis nodos colapsados de clases (tabla del §4) y 2 `instancia_de` del
nodo `+2 instancias`.

Lo que no tiene trazo: 18 `subclase_de` internas de las ramas colapsadas
(69 − 11 − 40), la `instancia_de` de FMI (5 − 2 − 2), 48 `miembro_de`
(51 − 3: los otros 3 miembros de este rol y los 45 de los demás roles) y la
única `parte_de` (`SEFyC parte_de BCRA`, `catalogo_sujetos_r2.json:2967`).

La capa del camino **no agrega aristas**: repite tramos de cuatro de las 17
explícitas con la otra intensidad, encima. Por eso sus trazos llevan
`data-camino` y no `data-rel`. La muestra de la leyenda tampoco lleva
`data-camino`, para que el recuento del camino desde el SVG dé 4.

**Recómputo desde el SVG**, sin volver a correr el script:

```bash
python3 -c "import re,collections;svg=open('docs/tesis/figuras/figura_catalogo_sujetos.svg',encoding='utf-8').read();print(dict(sorted(collections.Counter(re.findall(r'data-forma=\"([^\"]+)\"',svg)).items())));print('clases',sum(1 for _ in re.finditer(r'data-nodo=\"(?!COL:|INSTCOL)[^\"]+\" data-forma=\"clase\"',svg)),'+',sum(int(x) for x in re.findall(r'data-clases=\"(\d+)\"',svg)));print(dict(sorted(collections.Counter(re.findall(r'data-rel=\"([^\"]+)\"',svg)).items())));print('aristas',len(re.findall(r'data-src=',svg)),'+',sum(int(x) for x in re.findall(r'data-agrega=\"(\d+)\"',svg)));print('camino: nodos',len(re.findall(r'<g [^>]*data-camino=\"1\"',svg)),'trazos',len(re.findall(r'<path [^>]*data-camino=\"1\"',svg)))"
```

devuelve `{'clase': 12, 'colapsada': 7, 'instancia': 2, 'norma': 1, 'rol': 1}`,
`clases 12 + 58`, `{'aplica_a': 1, 'instancia_de': 3, 'miembro_de': 3,
'subclase_de': 17}`, `aristas 17 + 42` y `camino: nodos 5 trazos 4`. (Los 17
trazos `subclase_de` son 11 explícitos + 6 agregados; los 3 `instancia_de`,
2 explícitos + 1 agregado.)

Y que esas aristas existen en el grafo:

```bash
python3 -c "import re,json;svg=open('docs/tesis/figuras/figura_catalogo_sujetos.svg',encoding='utf-8').read();kg=json.load(open('data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2b/r2/kg.json'));E={(e['source'],e['relation'],e['target']) for e in kg['edges']};tr=[m.groups() for m in re.finditer(r'data-dst=\"([^\"]+)\" data-rel=\"([^\"]+)\" data-src=\"([^\"]+)\"',svg)];print(len(tr),sum(1 for d,r,s in tr if (s,r,d) in E))"
```

devuelve `17 17`.

## 6. Cruces de línea — 0

La versión 4 tenía 3 cruces: el tronco de `miembro_de` (x = 757) cortaba
las tres flechas `subclase_de` que entran por la derecha a `Entidades
financieras`, `Entidades cambiarias` y `Proveedores no financieros de
crédito`. Esta versión tiene **0**, medido de dos maneras independientes:

1. **La guarda del script** (`:1445-1499`), sobre los tramos que dibuja,
   sin la capa del camino ni la leyenda: 0 cruces, 0 contactos y 0 solapes
   entre peines, sobre 44 tramos de 12 peines (reporte, bloque «CAPA DE
   RÓTULOS»). Un cruce es un par de tramos que se cortan en un punto
   interior a los dos; un contacto, el extremo de un tramo apoyado sobre un
   tramo de otro peine.
2. **Sobre el SVG**, sin el script:

```bash
python3 -c "import re;svg=open('docs/tesis/figuras/figura_catalogo_sujetos.svg',encoding='utf-8').read();T=[];[T.extend(zip(p,p[1:])) for p in ([tuple(map(float,q.split(','))) for q in re.findall(r'[ML]([-\d.]+,[-\d.]+)',re.search(r'd=\"([^\"]+)\"',a).group(1))] for a in re.findall(r'<path ([^>]*)/>',svg) if 'stroke-linejoin=\"round\"' in a and 'data-camino=\"1\"' not in a)];H=[s for s in T if abs(s[0][1]-s[1][1])<.01];V=[s for s in T if abs(s[0][0]-s[1][0])<.01];C=sorted({(v[0][0],h[0][1]) for h in H for v in V if min(h[0][0],h[1][0])+.5<v[0][0]<max(h[0][0],h[1][0])-.5 and min(v[0][1],v[1][1])+.5<h[0][1]<max(v[0][1],v[1][1])-.5});print(len(T),len(C),C)"
```

devuelve `49 0 []` (los 44 tramos del dibujo más los 5 de las muestras de la
leyenda). El mismo comando sobre el SVG de la versión 4
(`git show c3bba5b:docs/tesis/figuras/figura_catalogo_sujetos.svg`) devuelve
`45 3 [(757.0, 303.5), (757.0, 428.0), (757.0, 562.0)]`, los tres cruces
que declaraba su LEEME: el comando no es vacuo.

La guarda del script tampoco es vacua. Sobre copias del script rotas a
propósito: el canal de `miembro_de` reemplazado por el tronco vertical de la
versión 4 FRENA con `AssertionError: 3 cruces de línea`, en x = 757 y sobre
los mismos tres peines; la vertical resaltada de `Entidades financieras`
corrida 6 px FRENA con «el camino resalta un tramo que no está dibujado»; y
un sha del grafo alterado en un carácter FRENA en el candado.

## 7. Fuente de cada dato de la figura

| Dato | Fuente |
|---|---|
| Las 12 clases dibujadas y sus etiquetas | campo `label` de cada entrada de `catalogo_sujetos_r2.json` (líneas del §4) |
| Los conteos `+N clases` | campo `padre` del catálogo, agrupado por ancestro dibujado más cercano (`:234-255`; reporte «BIYECCIÓN») |
| `+1 instancia` de la rama de Organismos públicos | campo `instancia_de` de FMI, `catalogo_sujetos_r2.json:3634`, y `:263-274` del script |
| BCRA, SEFyC y `+2 instancias` | `catalogo_sujetos_r2.json:2921`, `:2958`, `:2997`, `:3037` y el campo `instancia_de` de cada una |
| El rol, su etiqueta y «6 miembros · 3 dibujados» | `catalogo_sujetos_r2.json:3209-3232` |
| La norma y «Obligacion · punto 1.1» | `kg.json:237780-237782` (`id`, `type` y `label`) y `:237790` (`provenance.punto`) |
| Cada trazo explícito | una arista de `kg.json` (comando del §5; las cuatro del camino, con línea, en el §3) |
| Cada trazo agregado | las aristas `subclase_de`/`instancia_de` directas hacia el padre dibujado, verificadas una por una contra `kg.json` (`:363-368`) |
| Rótulos de relación | nombre de la relación en `kg.json` (`subclase_de`, `instancia_de`, `miembro_de`, `aplica_a`) |
| Leyenda | texto de la figura, no dato |

## 8. Convenciones de dibujo (declaradas)

- **Dos intensidades, legibles en blanco y negro.** El camino va con borde de
  4,0 px y relleno al 34 % del color del tipo; el resto, con borde de 1,9 px
  y relleno al 6 %. Las aristas: 4,6 px el camino, 1,9 px el resto, con el
  color mezclado un 42 % con el fondo fuera del camino y con la punta un 45 %
  más grande sobre el camino. Es el mecanismo de las versiones 3 y 4, sin
  cambios; miré esta versión convertida a escala de grises (perfil «Generic
  Gray» de macOS) y el camino y el canal raya-punto se distinguen.
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
- **Ruteo de `miembro_de` (nuevo en esta versión)**: un solo peine con una
  sola punta. El diente de `Entidades financieras` sube recto desde el centro
  de su borde superior (x = 579,3) hasta el lado inferior del rol. Los
  dientes de `Proveedores no financieros de crédito` y de `Fiduciarios de
  fideicomisos financieros` salen por la derecha hasta x = 757 (el primero
  baja ahí hasta el segundo), y desde y = 706 el tronco corre a la derecha
  por debajo de la última caja de las columnas 3 y 4, sube por fuera de
  `Bancos comerciales` (x = 1402,8) y vuelve a la izquierda por el hueco
  entre la banda superior y el árbol (y = 171) hasta unirse a la vertical de
  `Entidades financieras` antes de la punta (`:736-762`, `:1175-1202`;
  coordenadas del reporte, bloque «RUTEO DE miembro_de»). Es el único
  ruteo sin cruces que deja el trazado: la fila de arriba está cerrada a la
  izquierda por los peines de la raíz y de `Sujetos regulados` y a la derecha
  por la flecha `Bancos comerciales → Bancos`, que es del camino, así que el
  canal tiene que pasar por fuera de `Bancos comerciales`.
- **Los rótulos van en una capa final**, al costado de su tronco, nunca
  encima: cada rótulo prueba una lista de candidatos y se queda con el
  primero que no toca ninguna caja, ningún otro rótulo ni ningún trazo; si
  ninguno pasa, la generación FRENA. El de `miembro_de` va a la izquierda de
  la vertical de `Entidades financieras`, en su primer candidato.
- **Etiquetas** en castellano y tomadas del campo `label` del artefacto,
  nunca del `id`, con la única abreviatura de las dos siglas de instancia.
  Los identificadores del esquema (`Obligacion`, las cuatro relaciones) van
  sin tilde, como en el código.
- **Sin conteos de uso**: los únicos números de la figura son estructurales.
- **La leyenda va dentro del dibujo**, en el cuadrante inferior derecho que
  el árbol deja libre, por debajo del tramo bajo del canal de `miembro_de`
  (`:1087`).
- **`parte_de` no se dibuja**: el grafo tiene una sola arista de esa
  relación (`SEFyC parte_de BCRA`).
- La guarda de trazos sobre texto corre sobre las 23 cajas y los 50
  segmentos del dibujo: 0 trazos dentro de una caja y 0 trazos sobre un
  rótulo (reporte, bloque «CAPA DE RÓTULOS»).

## 9. Tamaño de impresión

El informe es `a4paper` con márgenes laterales de 3 cm
(`docs/tesis/main.tex:13`), es decir `\linewidth` = 210 − 30 − 30 =
**150 mm**; con márgenes superior e inferior de 2 cm, la caja de texto mide
**257 mm** de alto. (La versión 4 citaba `main.tex:9` para ese dato; la
línea es la 13, también en `c3bba5b`: `git show c3bba5b:docs/tesis/main.tex | grep -n geometry`.)

Insertada con `width=\linewidth`, la figura mide **15,0 × 13,94 cm**
(139,4 mm = 1328 ⁄ 1428,8 × 150; en la versión 4, 137,7 mm). El ancho
crece 18 px, los del canal de `miembro_de` por fuera de `Bancos
comerciales`. El alto crece 33 px, y ahora lo fija la leyenda y no el
árbol: el panel baja hasta quedar 40 px por debajo del tramo bajo del canal
(`:1087`), y su borde inferior pasa de y = 1247 a y = 1302. El árbol, en
cambio, empieza 20 px más arriba (la norma ocupa dos líneas y no tres, y
la banda superior se acorta 34 px; el hueco entre la banda y el árbol
crece 14) y termina 11 px más abajo (el subtítulo «+1 instancia» suma
31 px), en y = 1280. Medido sobre los dos SVG: banda hasta y = 177 y árbol
de 219 a 1269 en la versión 4; banda hasta y = 143 y árbol de 199 a 1280 en
esta (cajas de los elementos `data-nodo`, medidas con
`medidas_svg_FIG-CATALOGO-R2B.py` del paquete de revisión de esta
versión, que no se versiona).

| Cuerpo | px | pt impresos |
|---|---|---|
| etiqueta de nodo | 29 | **8,63** |
| subtítulo de caja | 27 | **8,04** |
| rótulo de relación | 27 | **8,04** |
| leyenda | 27 | **8,04** |

(Valores del reporte del script, bloque «TIPOGRAFÍA».) El piso de 8 pt es un
`assert` del script (`:1110-1113`). El margen sobre el piso queda más chico
que en la versión 4 (8,14 pt): con el ancho actual, el lienzo admite a lo
sumo 1435 px antes de que 27 px impriman menos de 8 pt
(27 × 150 ⁄ 25,4 × 72 ⁄ 8 = 1435,0).

**Qué archivo toma LaTeX.** El bloque inserta sin extensión, de modo que
`pdflatex` toma el **PDF vectorial**; el PNG queda como respaldo. Por eso el
PDF se regenera junto con el PNG.

**NO VERIFICADO**: el alto del bloque completo con epígrafe no se midió por
compilación (en el entorno donde se generó la figura no hay LaTeX).

## 10. Lo que esta versión deja desactualizado fuera de este directorio

La regeneración cambia cifras que otros archivos citan; ninguno se tocó en
esta unidad:

- `docs/tesis/figuras/bloque_latex_figura_catalogo.tex:31` (epígrafe): dice
  «Las 58 clases […] la figura dibuja 12 y colapsa las 46 restantes»; con
  esta versión, 70 clases, 12 dibujadas y 58 colapsadas. El resto del
  epígrafe (el deber del punto 1.1 que no nombra a quién obliga, `aplica_a`
  al rol, `miembro_de` de las entidades financieras, «El rol tiene 6
  miembros y se dibujan 3», las siglas BCRA y SEFyC) sigue valiendo. Sus
  comentarios de cabecera (150 × 134,1 mm; 8,7 / 8,1 pt) son de la versión 3.
- `docs/tesis/main.tex:739-749` (copia del informe en el repositorio): el
  epígrafe es todavía el de la versión 3 (Protección de usuarios, 58 / 12 /
  46, «siete miembros y se dibujan cinco»).
- `docs/tesis/mapa_fuentes_cap_esquema.md:152` (fila 51): conteos y sha de la
  versión 4 (58 / 12 / 46, 7 = 2 + 5, 24 trazos / 53 aristas, `120af34c…`).

## 11. Historial de versiones

- **Versión 1**: el catálogo fiel, sin destacar el camino.
- **Versión 2**: el camino resaltado (cinco nodos y cuatro aristas en trazo
  grueso, con el resto atenuado y una entrada propia en la leyenda); las
  instancias por su sigla; y el piso tipográfico de 8 pt asertado por el
  script.
- **Versión 3**: corrección de trazos sobre texto (fusión de bandas, capa
  final de rótulos y guarda de trazos contra cajas y rótulos).
- **Versión 4** (`c3bba5b`): el camino pasa al ejemplo de Clasificación de
  deudores (norma del punto 1.1, rol de 6 miembros con 3 dibujados), el
  subtítulo de la norma lleva el tipo como identificador del esquema, y el
  PDF pasa a exportarse con `SOURCE_DATE_EPOCH=0`. 3 cruces.
- **Versión 5** (esta): catálogo r2 y grafo de diez documentos r2b, con
  candado de sha256 sobre las dos fuentes y la pertenencia comparada arista
  por arista; 70 clases (12 + 58) y 5 instancias (2 + 2 + 1 declarada en
  una rama); la etiqueta nueva de la norma; `miembro_de` reruteado y guarda
  de cruces, contactos y solapes: 0 cruces; opción `--salida`.

## 12. Layout

Árbol de izquierda a derecha, una columna por nivel de profundidad (5
columnas: raíz, primer nivel, segundo, tercero, cuarto). Las filas están
declaradas en `FILAS` (`:694-707`), las mismas 12 de la versión 4, y cada
padre se ubica en el punto medio entre su primer y su último hijo. Los
anchos de columna se calculan del texto ya envuelto, con un tope por
columna (189, 245, 259, 303 y 192 px); el tope de la norma sube de 300 a
310 px para que «Clasificar clientes por calidad de obligados» entre en dos
líneas (`:546-550`).

La banda superior lleva la norma (apoyada en el margen izquierdo, que el
árbol deja libre) y el rol, que se ubica sobre la vertical de `Entidades
financieras` tan a la izquierda como lo permite el rótulo de `aplica_a`
(`:680-689`). El camino se recorre de arriba a la izquierda hacia abajo y a
la derecha: `aplica_a` de la norma al rol, `miembro_de` del rol a `Entidades
financieras`, `subclase_de` a `Bancos` y a `Bancos comerciales`.
