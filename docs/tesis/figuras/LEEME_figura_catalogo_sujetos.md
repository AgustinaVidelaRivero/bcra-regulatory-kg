# figura_catalogo_sujetos (F2) — registro de generación

Figura F2 del capítulo del esquema: el **catálogo de sujetos** —el árbol de
clases, sus instancias y la indirección por rol de alcance que permite que
una norma alcance a una subclase que no nombra—. Generada POR SCRIPT desde
los artefactos sellados, nunca dibujada a mano, como F1 y F1b.

Este LEEME describe la **tercera versión**. La primera mostraba fielmente el
catálogo pero no destacaba lo que la figura existe para mostrar: el camino
norma → rol → clase → subclase se leía igual que el resto del dibujo; los
tres cambios que lo corrigieron están en el §8. La tercera saca los rótulos a
una capa final y agrega la guarda de trazos sobre texto: §7.

## 1. Comando de generación

```bash
python3 docs/tesis/figuras/generar_figura_catalogo_sujetos.py
```

Escribe `figura_catalogo_sujetos.svg` (1410,8 × 1261). De ahí salen las dos
versiones para insertar, el PDF vectorial y el PNG:

```bash
rsvg-convert -f pdf -o docs/tesis/figuras/figura_catalogo_sujetos.pdf docs/tesis/figuras/figura_catalogo_sujetos.svg
rsvg-convert -z 2 -f png -o docs/tesis/figuras/figura_catalogo_sujetos.png docs/tesis/figuras/figura_catalogo_sujetos.svg
```

`rsvg-convert` (2.62.3) es la única herramienta externa, y solo para esas dos
exportaciones. El SVG se produce con Python de la biblioteca estándar, sin
dependencias.

| Archivo | Medida propia | Peso |
|---|---|---|
| `figura_catalogo_sujetos.svg` (fuente) | 1410,8 × 1261 px | 27,9 KiB |
| `figura_catalogo_sujetos.pdf` (vectorial) | 1058,10 × 945,75 pt = 373,27 × 333,64 mm | 62,0 KiB |
| `figura_catalogo_sujetos.png` (rasterizado) | 2822 × 2522 px = 478 dpi a 150 mm de ancho | 629,3 KiB |

**Sobre los 1058,10 × 945,75 pt del PDF.** No son los 1410,8 × 1261 del SVG
porque el punto PDF y el píxel SVG no son la misma unidad: `rsvg-convert`
lee las unidades de usuario del SVG como píxeles CSS (1/96 de pulgada) y las
escribe como puntos (1/72), de modo que el número queda multiplicado por
0,75 —1410,8 × 0,75 = 1058,10 y 1261 × 0,75 = 945,75, exacto—. **El tamaño
físico es el mismo**: 373,27 mm de ancho en las dos unidades. Como el bloque
LaTeX inserta con `width=\linewidth`, la figura se escala a 150 mm venga de
donde venga, así que la medida propia no afecta a la maqueta. Recomputable:

```bash
pdfinfo docs/tesis/figuras/figura_catalogo_sujetos.pdf | grep 'Page size'
```

**El PDF es vectorial de verdad**: cero objetos `/Subtype /Image` y las
fuentes embebidas y subsetadas (`pdffonts` lista Menlo-Regular,
Helvetica/-Bold/-Oblique y Arial-ItalicMT, todas `emb yes`). Rasterizado a
192 dpi y comparado píxel a píxel contra el PNG, el 1,75 % de los píxeles
difiere en más de 32/255, todo en bordes de glifo: es el antialiasing de dos
rasterizadores distintos (cairo directo para el PNG, poppler sobre el PDF)
más una diferencia de métrica tipográfica de hasta **2,85 %**, medida sobre
las líneas en itálica —las de negrita y redonda difieren menos del 0,2 %—.
Esa diferencia no puede desbordar ninguna caja: la línea más ancha de la
figura mide 277 px y el 2,85 % de 277 son 7,9 px, contra los 26 px de
relleno que cada caja tiene por delante (13 px por lado).

El script FRENA con `AssertionError` antes de dibujar si el catálogo deja de
tener 58 clases / 7 instancias / 5 roles, si la cadena que cita la prosa deja
de ser la del artefacto, si el camino resaltado deja de ser una cadena
conexa, si lo dibujado más lo colapsado no suma 58, si alguna arista
dibujada no está en el grafo vigente, si algún texto desborda su caja, si dos
cajas se solapan, si **algún trazo entra en el interior de una caja o cruza
el rectángulo de un rótulo** (§7), si algún rótulo no encuentra lugar libre,
o si **algún cuerpo tipográfico cae por debajo de 8 pt impresos** a
`width=\linewidth`.

## 2. Fuentes y sellos

| Archivo leído | sha256 | Commit |
|---|---|---|
| `data/experiment/grafo_v2/esquema_v2_clases.json` (catálogo v2.0) | `2672af5216e095bee2a4888e18d85930d7b0149263b87763daacc5fd21814d4d` | `43f241e` |
| `data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json` (grafo vigente) | `0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a` | `185e042` |

El catálogo es el **v2.0**, no el v3: la figura ilustra la versión con la que
corrió la validación. Ambos archivos están en el árbol byte-idénticos a su
commit (verificado con `git diff --stat HEAD -- <archivo>`, vacío).

Salidas de esta corrida:

| Archivo | sha256 |
|---|---|
| `figura_catalogo_sujetos.svg` | `0d1821c52dc4f976fab99374b1b6c8094c17b0852e7df54ec2d8110a4954d449` |
| `figura_catalogo_sujetos.pdf` | `ad11e630f14b8b2883647d486b4df5f904097a6bf58c54d974f2e3691a7aeeb8` |
| `figura_catalogo_sujetos.png` | `c83b8392c23b8910bd4c4cc50dae2a412ff6b32b71fcc520a403a9a87a9478fe` |
| `generar_figura_catalogo_sujetos.py` (script, versionado junto a la figura) | `354d2358b491ea2ba13d2d0c60c7d4444573e26098f4f70b77998dbc5089fd33` |

Generación determinística verificada: corridas repetidas y tres corridas con
`PYTHONHASHSEED` distinto (1, 2, 3) producen el mismo SVG, y una corrida
desde un directorio de trabajo ajeno produce el mismo archivo (el script no
usa rutas absolutas: resuelve el repositorio desde `Path(__file__)`). El PNG
también es reproducible byte a byte con el mismo `rsvg-convert`.

**El PDF NO es byte-reproducible, y es esperable**: cairo le estampa la
fecha de generación. Dos corridas seguidas dan archivos del mismo tamaño
(63.499 bytes) que difieren en unos 140 bytes, cerca del 0,2 %, al final del
archivo, y la única diferencia es el campo `/CreationDate`
(`D:20260907184722-03'00` contra `D:20260907185014-03'00`); quitado ese
campo, el stream que lo contiene es idéntico. Es decir: el contenido gráfico
sí es reproducible, el sello de tiempo no. **Por eso el sha256 del PDF de la
tabla vale para el archivo que entra al repositorio con este commit, no como
comprobación de una regeneración**: para verificar una regeneración hay que
comparar el SVG, que sí es byte-idéntico, o el render del PDF.

## 3. El camino resaltado

Es la pieza que la figura existe para mostrar y la que gobierna el dibujo:
**cinco nodos y cuatro aristas** en trazo grueso y relleno saturado, con todo
el resto atenuado.

| | |
|---|---|
| Nodos | `Documentación en sistema Braille` · `Sujetos obligados (Protección de usuarios)` · `Entidades financieras` · `Bancos` · `Bancos comerciales` |
| Aristas | norma `--aplica_a-->` rol · `Entidades financieras --miembro_de-->` rol · `Bancos --subclase_de--> Entidades financieras` · `Bancos comerciales --subclase_de--> Bancos` |

Las cuatro son aristas reales del grafo vigente y están entre las 19 que la
figura dibuja una a una (no son agregados de un nodo colapsado). El script
asserta además que el camino es una **cadena conexa**: cada arista une dos
nodos consecutivos de la lista, en un sentido o en el otro. Si dejara de
serlo, el resalte estaría afirmando un recorrido que el grafo no tiene, y la
generación frena.

**El tramo compartido.** El tronco de `miembro_de` lo recorren los cinco
miembros dibujados, pero el camino solo lo usa desde el rol hasta el diente
de `Entidades financieras`. El resalte cubre exactamente ese tramo y el
tronco sigue atenuado por debajo. Que el corte caiga justo ahí depende de que
`Entidades financieras` sea el miembro más alto del dibujo: el script lo
asserta, porque si dejara de serlo el resalte cubriría tramo que el camino no
recorre. (Es la misma disciplina de F1b, donde el resalte va en el tramo de
origen y no en el tronco compartido; acá el tramo compartido sí forma parte
del recorrido, y por eso se resalta.)

**El sentido de las flechas no cambió.** Es el del artefacto: el `source` es
el hijo, el miembro o la norma, y el `target` el padre o el rol. Recorrer el
camino con el dedo va dos pasos a favor de las flechas (`aplica_a` de la
norma al rol) y dos en contra (`subclase_de` hacia abajo del árbol); lo que
esta versión agrega es la marca de que es **un solo recorrido**, no la
alineación de las puntas.

## 4. Qué se dibujó y qué se colapsó

### Clases — 12 dibujadas + 46 colapsadas = 58

Dibujadas (una caja cada una, con el `label` del artefacto):

`Sujetos`, `Sujetos regulados`, `Contrapartes`, `Organismos públicos`,
`Estructuras y vehículos`, `Entidades financieras`, `Bancos`,
`Bancos comerciales`, `Entidades cambiarias`,
`Proveedores no financieros de crédito`,
`Empresas no financieras emisoras de tarjetas de crédito y/o compra`,
`Fiduciarios de fideicomisos financieros`.

Colapsadas — cada rama no expandida es **un** nodo que declara cuántas clases
contiene. El grupo de un nodo colapsado es, por construcción, el conjunto de
clases cuyo **ancestro dibujado más cercano** es el padre de ese nodo; los
grupos son disjuntos y su unión es exactamente el complemento de lo dibujado
(asertado por el script):

| Nodo colapsado | Cuelga de | Clases que contiene | Aristas `subclase_de` directas que representa su trazo |
|---|---|---|---|
| `+15 clases` | Sujetos regulados | 15 | 8 |
| `+3 clases` | Entidades financieras | 3 | 3 |
| `+2 clases` | Entidades cambiarias | 2 | 2 |
| `+17 clases` | Contrapartes | 17 | 11 |
| `+5 clases` | Organismos públicos | 5 | 4 |
| `+4 clases` | Estructuras y vehículos | 4 | 3 |
| | | **46** | **31** |

Los dos números de cada fila son distintos y miden cosas distintas: el
cardinal del nodo cuenta **todas** las clases del subárbol colapsado
(incluidas las de segundo y tercer nivel), y el trazo que llega a ese nodo
representa solo las aristas `subclase_de` **directas** hacia el padre
dibujado. Ambos se verifican contra el artefacto y contra el grafo.

### Instancias — 2 dibujadas + 5 declaradas = 7

Dibujadas: **BCRA** y **SEFyC**, colgando de `Organismos públicos` por
`instancia_de`. En la caja entra solo la sigla; los nombres desplegados
—Banco Central de la República Argentina y Superintendencia de Entidades
Financieras y Cambiarias— van al epígrafe. La sigla no se inventa: es el
prefijo literal del `label` del artefacto antes del paréntesis, y el script
lo asserta (`label.startswith(sigla)`). El SVG conserva la etiqueta completa
en `data-label-artefacto`, de modo que la abreviatura es recomputable:

```bash
python3 -c "import re;print(re.findall(r'data-label-artefacto=\"([^\"]+)\"', open('docs/tesis/figuras/figura_catalogo_sujetos.svg',encoding='utf-8').read()))"
```

Las 5 instancias restantes (ARCA, Ministerio de Economía y las secretarías de
Energía, de Comercio y de Transporte) van en el nodo colapsado
`+5 instancias`, que declara cuántas quedan.

### Rol — 1 de los 5 del catálogo; 5 de sus 7 miembros

Se dibuja `Sujetos obligados (Protección de usuarios)`, el rol de 7 miembros.
La figura dibuja **5** miembros (`Entidades financieras`,
`Entidades cambiarias`, `Proveedores no financieros de crédito`,
`Empresas no financieras emisoras de tarjetas de crédito y/o compra`,
`Fiduciarios de fideicomisos financieros`) y **declara los 2 restantes en la
propia caja del rol** («7 miembros · 5 dibujados»). Los dos no dibujados son
`Proveedores de servicios de pago que ofrecen cuentas de pago (PSPCP)` y
`Proveedores de servicios de pago iniciadores que prestan el servicio de
billetera digital (PSI)`; ambos caen dentro del nodo `+15 clases`, de modo que
la figura no los pierde: los cuenta y los declara. La poda se hizo por la
regla de podar antes que achicar la tipografía: sus dos etiquetas (68 y 94
caracteres) obligaban a una columna mucho más ancha.

Los otros 4 roles del catálogo no se dibujan: la figura ilustra el mecanismo
de la indirección, no el inventario de roles.

### La norma

`Documentación en sistema Braille` (tipo `Obligacion`, punto 2.2.2, páginas
5-6 del Texto Ordenado de Protección de los usuarios de servicios
financieros). Es un nodo real del grafo vigente, elegido entre las 243
aristas `aplica_a` que apuntan a ese rol, y se dibuja con su `label` tomado
del propio grafo. Nada en la figura es de ejemplo.

## 5. Aristas — 55 representadas, todas verificadas contra el grafo vigente

Conteos globales del grafo vigente, asertados por el script antes de dibujar:
`subclase_de` 57, `instancia_de` 7, `miembro_de` 17, `parte_de` 1.

| | Trazos | Aristas del grafo que representan |
|---|---|---|
| Explícitos (un trazo = una arista) | 19 | 19 |
| Agregados (un trazo = N aristas hacia un nodo colapsado) | 7 | 36 |
| | **26** | **55** |

Las 19 explícitas: 11 `subclase_de` (el árbol dibujado), 2 `instancia_de`
(BCRA y SEFyC), 5 `miembro_de` (los miembros dibujados) y 1 `aplica_a` (la
norma al rol). Las 36 agregadas: 31 `subclase_de` de los seis nodos
colapsados de clases (tabla del §4) y 5 `instancia_de` del nodo
`+5 instancias`. Las 55 están presentes en `salida_r1/kg.json`; el script
frena si alguna falta.

La capa del camino **no agrega aristas**: repite cuatro de las 19 explícitas
con la otra intensidad, encima. Por eso sus trazos llevan `data-camino` y no
`data-rel`, y el recuento de aristas no se duplica. La muestra de la leyenda
usa la misma intensidad pero tampoco lleva `data-camino`, para que el
recuento del camino desde el SVG dé 4 y no 5.

**Recómputo desde el SVG**, sin volver a correr el script (el SVG lleva
anotaciones `data-*`, como F1):

```bash
python3 -c "import re,collections;svg=open('docs/tesis/figuras/figura_catalogo_sujetos.svg',encoding='utf-8').read();print(dict(sorted(collections.Counter(re.findall(r'data-forma=\"([^\"]+)\"',svg)).items())));print('clases',sum(1 for _ in re.finditer(r'data-nodo=\"(?!COL:|INSTCOL)[^\"]+\" data-forma=\"clase\"',svg)),'+',sum(int(x) for x in re.findall(r'data-clases=\"(\d+)\"',svg)));print(dict(sorted(collections.Counter(re.findall(r'data-rel=\"([^\"]+)\"',svg)).items())));print('aristas',len(re.findall(r'data-src=',svg)),'+',sum(int(x) for x in re.findall(r'data-agrega=\"(\d+)\"',svg)));print('camino: nodos',len(re.findall(r'<g [^>]*data-camino=\"1\"',svg)),'trazos',len(re.findall(r'<path [^>]*data-camino=\"1\"',svg)))"
```

devuelve `{'clase': 12, 'colapsada': 7, 'instancia': 2, 'norma': 1, 'rol': 1}`,
`clases 12 + 46`, `{'aplica_a': 1, 'instancia_de': 3, 'miembro_de': 5,
'subclase_de': 17}`, `aristas 19 + 36` y `camino: nodos 5 trazos 4`. (Los 17
trazos `subclase_de` son 11 explícitos + 6 agregados; los 3 `instancia_de`,
2 explícitos + 1 agregado.)

Y que esas aristas existen en el grafo:

```bash
python3 -c "import re,json;svg=open('docs/tesis/figuras/figura_catalogo_sujetos.svg',encoding='utf-8').read();kg=json.load(open('data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json'));E={(e['source'],e['relation'],e['target']) for e in kg['edges']};tr=[m.groups() for m in re.finditer(r'data-dst=\"([^\"]+)\" data-rel=\"([^\"]+)\" data-src=\"([^\"]+)\"',svg)];print(len(tr),sum(1 for d,r,s in tr if (s,r,d) in E))"
```

devuelve `19 19`.

## 6. Convenciones de dibujo (declaradas)

- **Dos intensidades, legibles en blanco y negro.** El camino va con borde de
  4,0 px y relleno al 34 % del color del tipo; el resto, con borde de 1,9 px
  y relleno al 6 %. Las aristas: 4,6 px el camino, 1,9 px el resto, con el
  color mezclado un 42 % con el fondo fuera del camino y con la punta un 45 % más grande
  sobre el camino. Trazo y saturación son dos señales, ninguna dependiente
  del color; se verificó convirtiendo el PNG a escala de grises.
- **El texto no se atenúa.** La atenuación vive en el borde y el relleno de
  las cajas; las etiquetas quedan todas al mismo negro, porque el piso de
  8 pt es una restricción de legibilidad y bajarles el contraste la
  contradiría. Los rótulos de relación conservan el color de su relación.
- **Cinco formas, distinguibles sin color**: clase = rectángulo de trazo
  continuo; rama no expandida = rectángulo apilado de trazo discontinuo;
  instancia = píldora (extremos redondeados); rol de alcance = hexágono de
  trazo raya-punto; norma = rectángulo con la esquina superior derecha
  plegada.
- **Cuatro relaciones, distinguibles por patrón de línea Y por forma de
  punta**: `subclase_de` continua con punta de triángulo hueco (la
  generalización de UML); `instancia_de` discontinua con punta llena chica;
  `miembro_de` raya-punto con punta llena de cola cóncava; `aplica_a`
  continua con punta llena grande. Las cuatro llevan su nombre sobre el
  trazo, con halo blanco.
- **Sentido de las flechas**: la punta señala al padre / al rol, como en la
  generalización UML. La nota al pie de la leyenda lo dice, y la entrada
  «camino resaltado» nombra el recorrido.
- **Peines**: cuando varias aristas de la misma relación terminan en la misma
  caja, los trazos confluyen en un tronco con una única punta y un único
  rótulo, como en F1/F1b. El rótulo se coloca en el mayor hueco **libre** del
  tronco, medido entre los bordes de las cajas conectadas —con el aire que el
  propio cuerpo tipográfico necesita— y no entre sus centros.
- **Los rótulos van en una capa final**, emitida después de todas las aristas
  y de todas las cajas, y **al costado de su tronco, nunca encima**. Su
  posición no está fijada a mano: cada rótulo trae una lista de candidatos —a
  un lado y otro del tronco, recorriéndolo— y se queda con el primero cuyo
  rectángulo no toca ninguna caja, ningún otro rótulo ni ningún trazo. Si
  ninguno pasara, la generación FRENA. Los rótulos se posicionan por su
  centro óptico, no por su línea de base, y todos los desplazamientos son
  proporcionales al cuerpo tipográfico.
- **El halo blanco quedó redundante** y se conserva solo como cama del texto:
  ya no tiene que interrumpir ningún trazo, porque ningún trazo pasa por
  debajo. Como efecto lateral, los troncos quedaron continuos.
- **Puertos**: los dos peines que terminan en `Organismos públicos`
  (`subclase_de` e `instancia_de`) entran por puntos distintos del mismo
  borde, separados proporcionalmente al cuerpo.
- **Etiquetas**: en castellano y tomadas del campo `label` del artefacto,
  nunca del `id` — con la única abreviatura de las dos siglas del §4, que es
  prefijo literal del label y queda registrada en el SVG. El texto se
  envuelve al ancho de su columna y el constructor de la caja asserta que
  ninguna línea desborda: una etiqueta cortada frena la generación.
- **Sin conteos de uso**: ninguna clase lleva cuántas veces se usa en el
  grafo. Los únicos números de la figura son estructurales.
- **La leyenda va dentro del dibujo**, en el cuadrante inferior derecho que el
  árbol deja libre.
- **`parte_de` no se dibuja**: el grafo tiene una sola arista de esa relación
  (`SEFyC parte_de BCRA`) y la figura enumera cuatro relaciones. Dibujarla
  habría agregado una quinta convención de trazo para un solo caso.
- **Cruces de línea**: 3 puntos distintos, todos entre trazos finos y ninguno
  sobre una caja. El tronco de `miembro_de` (x = 757) cruza los tres tramos
  horizontales que llevan la punta de `subclase_de` a `Entidades financieras`
  (y = 269,5), a `Entidades cambiarias` (y = 394) y a `Proveedores no
  financieros de crédito` (y = 528). Medidos sobre el SVG y deduplicados por
  posición —la capa del camino repite dos de esos trazos, de modo que un
  conteo ingenuo por pares informa 6 donde hay 3—:

  ```bash
  python3 -c "import re,itertools;svg=open('docs/tesis/figuras/figura_catalogo_sujetos.svg',encoding='utf-8').read();T=[[*zip(P,P[1:])] for m in re.finditer(r'<path d=\"([^\"]+)\"[^>]*stroke-linejoin[^>]*/>',svg) for P in [[tuple(map(float,q.split(','))) for q in re.findall(r'[ML]([-\\d.]+,[-\\d.]+)',m.group(1))]]];h=lambda s:abs(s[0][1]-s[1][1])<.01;v=lambda s:abs(s[0][0]-s[1][0])<.01;pts=set()
  for sa,sb in itertools.combinations(T,2):
      for x in sa:
          for y in sb:
              a,b=(x,y) if h(x) and v(y) else ((y,x) if v(x) and h(y) else (None,None))
              if a and sorted([a[0][0],a[1][0]])[0]+.01<b[0][0]<sorted([a[0][0],a[1][0]])[1]-.01 and sorted([b[0][1],b[1][1]])[0]+.01<a[0][1]<sorted([b[0][1],b[1][1]])[1]-.01: pts.add((round(b[0][0],1),round(a[0][1],1)))
  print(sorted(pts), len(pts))"
  ```

  Ninguna flecha pasa por encima de una caja, y ninguna caja se solapa con
  otra: el script lo asserta sobre todos los pares antes de escribir el SVG.

## 7. Corrección de trazos sobre texto (tercera vuelta)

Dos defectos reportados sobre el PDF ya compilado. **El primero era real; el
segundo se descartó midiendo.**

**1. El rótulo `subclase_de` del peine de «Sujetos regulados» se leía
«subclase_ae».** La causa NO era una línea: era la **caja** «Proveedores no
financieros de crédito», que se superponía al rectángulo del rótulo en
44,1 × 10,5 px y —al dibujarse las cajas después de los rótulos— le pintaba
encima los últimos caracteres. Debajo había un defecto de cálculo propio:
`y_mayor_hueco` buscaba huecos entre bandas consecutivas **sin fusionar las
que se solapan**, y eligió un hueco fantasma de 5,8 px entre el final de la
banda de «Sujetos regulados» y el comienzo de la de «Fiduciarios», cuando la
banda de «Proveedores no financieros de crédito» (445,1–611,0) lo cubría
entero. Corregido en dos frentes: la fusión de bandas, y —lo que de verdad
lo cierra— la capa final de rótulos con búsqueda de posición y guarda.

**2. «Empresas no financieras emisoras de tarjetas de crédito y/o compra»
NO tiene ningún trazo sobre su texto.** Medido: cero segmentos entran en el
interior de esa caja, y cero entran siquiera en su rectángulo envolvente. Lo
que hay es el trazo `subclase_de` y el `miembro_de` que **llegan hasta su
borde izquierdo y se detienen ahí**, a la altura de la tercera línea de
texto; a tamaño de impresión eso puede leerse como un trazo sobre el texto,
pero no lo es.

La guarda nueva no encontró ningún caso además del primero.

### La guarda

La anterior solo comparaba caja contra caja, y por eso ninguno de los dos
casos podía detectarse. La nueva mide, sobre los 49 segmentos del dibujo y
las 23 cajas:

- **ningún trazo entra en el interior de una caja** más de 3 px. La medida es
  de *longitud*, no de contacto: casi todos los trazos terminan sobre el
  borde de una caja —ahí va la punta de flecha, ahí arranca un diente— y eso
  es correcto; lo que es defecto es atravesarla. La posición perpendicular se
  compara contra el interior encogido por medio grosor de trazo, de modo que
  se mide la tinta y no la línea ideal;
- **ningún trazo toca el rectángulo de un rótulo**, con 3 px de aire;
- **ningún rótulo se superpone a una caja**, a otro rótulo o al panel de la
  leyenda, ni se sale del lienzo.

Que la guarda no es vacua se comprobó rompiendo la figura a propósito:
forzando el rótulo sobre su tronco (`SEP_ROTULO = 0`) frena con «no hay lugar
libre para el rótulo «subclase_de»: ninguno de sus 400 candidatos…», y
alargando un trazo 120 px dentro de una caja frena con «trazo … entra
120,0 px en la caja Sujeto_banco_comercial».

Nota sobre el reparto de responsabilidades: desactivando la fusión de bandas
—el defecto de cálculo original— la figura sale **idéntica**, porque la
guarda rechaza los candidatos malos y la búsqueda llega al mismo lugar. La
fusión mejora el orden de preferencia; lo que garantiza la corrección es la
guarda.

## 8. Los tres cambios de la segunda versión

1. **El camino resaltado** (§3): cinco nodos y cuatro aristas en trazo grueso
   y relleno saturado, con el resto atenuado, más una entrada propia en la
   leyenda que lo nombra. Antes el recorrido no se distinguía del resto del
   dibujo.
2. **Las instancias, por su sigla** (§4): `BCRA` y `SEFyC` en lugar de sus
   nombres desplegados, que pasaron al epígrafe. Antes esas dos cajas eran de
   lo más alto del dibujo siendo el punto menos importante de la subsección:
   de cuatro líneas cada una pasaron a una.
3. **Piso tipográfico de 8 pt** (§9), asertado por el script.

Para pagar el punto 3 se podó, en el orden previsto: primero los subtítulos
internos de las cajas —«rama no expandida» ya lo dice la leyenda por la
forma, y la procedencia de la norma y del rol pasó al epígrafe, de donde
quedan solo dos líneas cortas y estructurales («Obligación · punto 2.2.2» y
«7 miembros · 5 dibujados»)—; y después se acortaron las dos notas de la
leyenda. No hizo falta llegar a podar ramas colapsadas: los conteos
12 + 46 = 58, 2 + 5 = 7 y 5 + 2 = 7 siguen cerrando iguales, y las 55 aristas
también.

## 9. Tamaño de impresión

El informe es `a4paper` con márgenes laterales de 3 cm (`main.tex:9`), es
decir `\linewidth` = 210 − 30 − 30 = **150 mm**; con márgenes superior e
inferior de 2 cm, la caja de texto mide **257 mm** de alto.

Insertada con `width=\linewidth`, la figura mide **150 × 134,1 mm**
(134,1 = 1261 ⁄ 1410,8 × 150) y su tipografía queda en:

| Cuerpo | px | pt impresos |
|---|---|---|
| etiqueta de nodo | 29 | **8,74** |
| subtítulo de caja | 27 | **8,14** |
| rótulo de relación | 27 | **8,14** |
| leyenda | 27 | **8,14** |

El piso de 8 pt es un `assert` del script, no una comprobación a ojo: si el
lienzo creciera de ancho hasta hacer caer cualquiera de esos cuerpos por
debajo, la generación frena.

**Qué archivo toma LaTeX.** El bloque inserta sin extensión
(`\includegraphics[width=\linewidth]{figuras/figura_catalogo_sujetos}`), de
modo que `pdflatex` resuelve por su orden de extensiones por omisión —`.pdf`
antes que `.png`— y toma el **PDF vectorial**: la figura sale con el texto
como texto (seleccionable y buscable en el PDF de la tesis) y sin
dependencia de la resolución. El PNG queda como respaldo, y lo toma solo si
el PDF no está. Las figuras hermanas F1 y F1b sí llevan `.png` explícito.

**Por qué a ancho pleno y no al 0,85 de las figuras hermanas**: a
`width=0.85\linewidth` la figura bajaría a 114 mm de alto, pero su tipografía
caería a 7,4 pt las etiquetas y 6,9 pt el resto — por debajo del piso. El
ancho pleno es el único que satisface las dos condiciones.

**Cómo se llegó a estos números.** El alto impreso es `alto ⁄ ancho × 150`,
así que ensanchar las columnas lo baja: las etiquetas se envuelven en menos
líneas y el dibujo se achata. Sobre esa relación se corrió una búsqueda por
coordenadas del ancho máximo de cada columna, eligiendo en cada punto el
menor cuerpo tipográfico que cumple el piso de 8 pt y quedándose con el
mínimo alto impreso. El óptimo hallado —columnas de 189, 245, 259, 303 y
192 px— deja la figura en 134,1 mm; la versión anterior, con columnas
angostas, medía 188,5 mm con tipografía de 5,8 pt.

**El bloque completo, con epígrafe**, ocupa del orden de 194 a 199 mm de los
257 mm de caja de texto, de modo que entra con `[H]` junto al párrafo que lo
llama —como F1 y F1b— y deja unos 60 mm de texto en esa página. **NO
VERIFICADO**: esa cuenta del epígrafe es una estimación aritmética (770
caracteres a 12 pt en 150 mm dan 11 o 12 líneas), no una medición — en el
entorno donde se generó la figura no hay LaTeX instalado (`which pdflatex
xelatex lualatex tectonic` no devuelve nada), de modo que el bloque no se
compiló. Conviene mirar la primera compilación.

## 10. Layout

Árbol de izquierda a derecha, una columna por nivel de profundidad (5
columnas: raíz, primer nivel, segundo, tercero, cuarto). Las filas se
asignan a las hojas dibujadas en el orden del artefacto, y cada padre se
ubica en el punto medio entre su primer y su último hijo. Los anchos de
columna no son fijos: se calculan del texto ya envuelto, con un tope por
columna que es el que la búsqueda del §9 fijó.

La banda superior lleva la norma (apoyada en el margen izquierdo, que el
árbol deja libre) y el rol, centrado sobre el tronco de `miembro_de` que baja
hacia sus miembros; el tramo de `aplica_a` entre las dos se asserta lo
bastante largo como para que su rótulo entre. El camino que la figura existe
para mostrar se recorre de arriba a la izquierda hacia abajo y a la derecha:
`aplica_a` de la norma al rol, `miembro_de` del rol a `Entidades
financieras`, `subclase_de` a `Bancos` y a `Bancos comerciales`.
