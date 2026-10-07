# figura_tripleta — registro de generación (Figura 2.1), versión 2

Figura «anatomía de una tripleta» del capítulo 2 (Figura 2.1 en el mensaje de
`fbe69d4`), con el ejemplo del préstamo: la `Condicion` del monto del punto
5.1.1.1 del Texto Ordenado de Clasificación de deudores —`condicion_de`→ la
`Operacion` de la inclusión en la cartera comercial, del mismo punto, en el
grafo de la tanda 0 con el perfil r2b (el de la figura 1.1 versión 2,
`88bfe89`).

- Dos nodos con el formato de la figura 1.1 versión 2: primera línea en
  negrita con el tipo y el punto («Condicion · punto 5.1.1.1», «Operacion ·
  punto 5.1.1.1») y debajo la etiqueta tal como está en el grafo, completa.
- La arista con el nombre de la relación tal como está en el grafo, en trazo
  continuo.
- Tres llamadas en gris: «nodo de origen» y «nodo de destino», centradas
  sobre su caja, y «relación · nombre y dirección», debajo de la arista. Sin
  leyenda.

Tamaño impreso: **12,75 × 3,59 cm** (lienzo 720 × 203). Cruces entre trazos:
**0**.

## Versiones

- **Versión 1** (28/09/2026, U-FIG-EJEMPLO y U-FIG-EJEMPLO-AJUSTE): generador,
  SVG y PNG en `fbe69d4`; su LEEME, en `e6e6021`. Sobre KG-Reextraído-r1
  (`data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json`, sha256
  `0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a`): la
  `Restriccion` del monto —`limita`→ la `Operacion` (`kg['edges'][15772]`),
  leídas de `ejemplo_prestamo_datos.json`; nodos con la etiqueta y debajo
  «punto N», relleno saturado de su tipo, borde negro y texto blanco; el tipo
  y el punto, en las llamadas de los nodos («nodo de origen · tipo
  Restriccion · punto 5.1.1.1»). sha256 en `fbe69d4`: generador
  `0bd7ba14c8460d8c033f57511b4ccefef051f7b81743309cea49ef9809ba5c4f`, SVG
  `709f1e30e7588742d9a41b6bb0b0e73fa46442acbdda9221866ee2cd50785b80`, PNG
  `bb97e7b6dc295abda2fed97df60acc36b1c58a4b06b8ddaa27f0d9cb32edd503`
  (`git show fbe69d4:docs/tesis/figuras/<archivo> | shasum -a 256`).
  El generador de la versión 1 importaba constantes de
  `generar_figura_norma_a_grafo.py` y `generar_figura_proceso_extraccion.py`;
  desde `88bfe89`, que cambió los dos, ya no se importa (`AttributeError`:
  `generar_figura_proceso_extraccion` sin `DPI`, en su línea 74). Con los tres
  archivos de `865a5b2` se importa (comprobado en FIG-TRIPLETA-R2B sobre una
  copia, con `git show <commit>:docs/tesis/figuras/<archivo>` y
  `python -B -c "import generar_figura_tripleta"`).
- **Versión 2** (07/10/2026, FIG-TRIPLETA-R2B). Qué cambió:
  - **la tripleta y el grafo**: (`Condicion` del monto, `condicion_de`,
    `Operacion`) de KG-Tanda0-Desarrollo-r2b, comprobada igual en
    KG-Tanda0-Diez-r2b (§2 a §4);
  - **los nodos**: el formato de la figura 1.1 versión 2, con «Tipo · punto
    N» en negrita arriba y la etiqueta debajo (en la versión 1, la etiqueta y
    «punto N» al pie); los colores de su tipo (relleno, borde y grosor) y el
    texto en `#1f1f1f`, también los de la figura 1.1 versión 2 (§3 y §6);
  - **las llamadas de los nodos**: «nodo de origen» y «nodo de destino», sin
    el tipo ni el punto, que pasan a la caja; centradas sobre su caja (en la
    versión 1, alineadas con el borde exterior de la caja: `text-anchor`
    `start` en x = 24 y `end` en x = 696); la línea de llamada no cambia;
  - **el alto de los nodos**: 108 → 87 unidades, porque cada caja lleva tres
    líneas en vez de cuatro; con él bajan la arista, su rótulo y la llamada de
    la relación, y el lienzo pasa de 720 × 224 a 720 × 203;
  - **las fuentes**: el generador ya no lee `ejemplo_prestamo_datos.json` ni
    importa `generar_figura_proceso_extraccion.py`; lee los grafos, el estilo,
    el esquema r2 y la figura 1.1 con candado de sha256 (§2);
  - **las salidas**: se agrega el PDF; el PNG sigue a 300 dpi con la densidad
    grabada (§9);
  - **los controles**: corren siempre (en la versión 1, con `--verificar`) y
    se suman el inventario, las líneas de llamada y las pruebas negativas
    (§7 y §8).
  No cambian: el lienzo de 720 unidades a 12,75 cm de ancho, la posición y el
  ancho de las dos cajas, las líneas de las llamadas de los nodos, la arista
  en trazo continuo `#4a5a6a` de 2,6 con su flecha y su rótulo en negrita, el
  texto de la llamada de la relación y los tamaños de letra (§6).

## 1. Comando

```
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_tripleta.py
```

Escribe `figura_tripleta.svg`, `.png` y `.pdf` en `docs/tesis/figuras/`
(`--salida DIR` para otro directorio). Herramientas: `rsvg-convert` 2.62.3
(lo informa el generador al terminar), PIL de `.venv` y
`/System/Library/Fonts/Helvetica.ttc` para medir los textos; sin red ni API.
Con `--perturbar <caso>` compone la figura con un defecto (§8) y no escribe
nada.

Del generador de la figura 1.1 (`generar_figura_norma_a_grafo.py`, sha256
`89dfc2a3d85e2abe1a28b3517d3e6817d73af8feb5b4b37ee4fb73978b5e3298` en
`88bfe89`) se importan, sin modificarlos: los candados de los dos grafos y del
estilo (`GRAFO`, `GRAFO_DIEZ`, `ESTILO`, :105-119) con `leer_con_candado`
(:122-129); la carga del subgrafo (`cargar_subgrafo`, :398-459, y
`comparar_grafos`, :462-477); los colores de tipo (`leer_colores_tipo`,
:480-491); las líneas del nodo (`lineas_nodo`, :518-529, con
`encabezado_nodo`, :497-499, y `envolver_etiqueta`, :502-515); los controles
de geometría (`controlar_geometria`, :929-982); y la exportación (`exportar`,
:1079-1094).

## 2. Fuentes

Cada una con candado de sha256 (`generar_figura_tripleta.py:105-115`); si una
no coincide, el generador frena.

| Papel | Archivo | sha256 | Ancla |
|---|---|---|---|
| grafo dibujado | `data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo_r2b/r2/kg.json` | `6e7560433148cfe0c476cdd61199c32278187c4196d6f90dc0a38976a6d8e9a2` | último commit `bbc38dc`; KG-Tanda0-Desarrollo-r2b, 6.990 nodos y 23.445 aristas (`data/experiment/neo4j/grafos.py:120-133`) |
| grafo de comprobación | `data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2b/r2/kg.json` | `a9631a64b422bdae634fb05135373c6f04c6272cdf7acd43a1be9f5b6c1f5f57` | último commit `bbc38dc`; KG-Tanda0-Diez-r2b, 8.816 nodos y 27.632 aristas (`grafos.py:134-147`) |
| colores de tipo | `docs/tesis/figuras/figura_esquema_final.svg` | `dfdb16d471bb93c6351aa03b1e609452b75c428baa354c52354ce1dfe9797bb3` | `8edd732`; cajas `data-caja` en :110 (`Condicion`) y :118 (`Operacion`) |
| esquema r2 | `data/experiment/pyd_r2/code/modelos_r2.py` | `e67f15ae13dd5419ea0ce1a08dbef63c86cbdf9c269772a0b02a4e27b4c3a2ca` | último commit `4aa92c7`; igual en `bbc38dc`; `PREDICADOS` :106-108, `AMPLIACION_R2` :130-133, `PREDICADOS_DERIVADOS` :165 |
| figura 1.1 versión 2 | `docs/tesis/figuras/figura_norma_a_grafo.svg` | `874292f54e3c5d70b036b070b6beb7e8ce4c568a2aa6862fde23d865588f3e9b` | `88bfe89`; cajas `condicion_monto` (:33-36) y `operacion` (:41-44) |

El sha256 de cada fuente en el commit de la columna «Ancla» es el del candado
(`git show <commit>:<ruta> | shasum -a 256`). Los tres primeros son los
candados de la figura 1.1 (`generar_figura_norma_a_grafo.py:105-119`).

## 3. Nodos dibujados (2)

Declarados en `NODOS` (`generar_figura_tripleta.py:124-127`) por clave, tipo,
chunk y etiqueta; `cargar_subgrafo` frena si no hay exactamente uno o si su
única procedencia `punto_propio` no es ese chunk. Las claves son las de la
figura 1.1.

| Clave | Papel | Tipo | Punto | Etiqueta en el grafo | id |
|---|---|---|---|---|---|
| condicion_monto | origen | Condicion | 5.1.1.1 | Superar dos veces importe referencia punto 3.7 | `Condicion_superar_dos_veces_importe_referencia_punto_3_7__el_credito_debe_superar_el_equiv_22a312` |
| operacion | destino | Operacion | 5.1.1.1 | Inclusión en cartera comercial — créditos consumo/vivienda | `Operacion_inclusion_en_cartera_comercial_creditos_consumo_vivienda__cla_5_1_1_1_8f5956` |

Mismos ids, tipos, etiquetas, puntos y propiedades en los dos grafos
(`comparar_grafos`). Tipo, punto, etiqueta, relleno, borde y grosor, iguales
a los de las cajas de la figura 1.1 (`controlar_figura_1_1`,
`generar_figura_tripleta.py:246-259`, que lee el SVG con `leer_figura_1_1`,
:224-243).

Formato de la caja: las líneas las arma `lineas_nodo` de la figura 1.1
(`lineas_nodo` de esta figura, :280-288): «Tipo · punto N» en negrita y
debajo la etiqueta completa, sin abreviar, envuelta al ancho de la caja y a 40
caracteres por línea como máximo (`MAX_ETIQUETA`,
`generar_figura_norma_a_grafo.py:192`); el generador base frena si lo
dibujado, unido, no es la etiqueta del grafo, y este, si la etiqueta pasa de
tres líneas (`LINEAS_ETIQUETA`, :142). El encabezado es el mismo texto que en
la figura 1.1 (`figura_norma_a_grafo.svg:34` y :42); el corte de la etiqueta
cambia con el ancho de la caja y el tamaño de letra. Tipos escritos como en el
código, sin tildes.

## 4. Arista dibujada (1)

Declarada en `ARISTA` (`generar_figura_tripleta.py:131`); existe una sola vez
en cada grafo y, entre los dos nodos, el grafo no tiene otra en ningún sentido
(`cargar_subgrafo`; `controlar_firma`, :200-221).

| `kg['edges']` desarrollo / diez | Origen | Relación | Destino | Procedencia |
|---|---|---|---|---|
| 5540 / 6179 | condicion_monto | `condicion_de` | operacion | `cla::5.1.1.1`, página 16 |

Es una arista de extracción, no de las que deriva el ensamblado
(`controlar_firma`): `condicion_de` está en `PREDICADOS`
(`modelos_r2.py:106-108`) y no en `PREDICADOS_DERIVADOS`, que es
`("remite_a",)` (:165); la firma (`condicion_de`, `Condicion`, `Operacion`)
es la de la ampliación de la matriz r2 (`AMPLIACION_R2`, :130-133; la matriz
congelada admite `condicion_de` solo hacia `Excepcion`, `Obligacion` y
`Restriccion`, :127); y la arista no lleva `rol_fuente` ni `properties` en
ninguno de los dos grafos. La procedencia, del índice de la arista en los dos
grafos (consulta de solo lectura sobre una copia, FIG-TRIPLETA-R2B:
`kg['edges'][5540]['provenance']` y `kg['edges'][6179]['provenance']`).

Qué está escrito a mano: las declaraciones de §3 y §4, que el generador busca
y comprueba en el grafo, y los textos fijos de las tres llamadas (`LLAMADA`,
:139-141).

## 5. Lo que no se dibuja

Lo cuenta el generador en cada corrida (salida «NO DIBUJADO»), igual en los
dos grafos:

- **Los otros dos nodos del 5.1.1.1**: la `Condicion` del repago, con su
  `condicion_de` hacia la `Operacion` (la figura 1.1 la dibuja), y la
  `Excepcion`, cuya única arista es su `establecida_en`
  (`LEEME_figura_norma_a_grafo.md`, §6). `NO_DIBUJADOS`
  (`generar_figura_tripleta.py:133-134`) los declara y el script frena si los
  nodos de la unidad que no se dibujan son otros.
- **Las otras aristas de los dos nodos**: una `establecida_en` de cada uno
  hacia el Texto Ordenado y una `remite_a` de cada uno hacia la `Definicion`
  del 3.7 (las dos que dibuja la figura 1.1).

## 6. Colores, composición y tamaño

Colores de tipo, leídos de `figura_esquema_final.svg` (`leer_colores_tipo`) e
iguales a los de las cajas de la figura 1.1 versión 2:

| Tipo | Relleno | Borde | Grosor | Línea en el esquema final / en la figura 1.1 |
|---|---|---|---|---|
| Condicion | `#f8e8f5` | `#b5179e` | 2.6 | :110 / :33 |
| Operacion | `#eaefee` | `#52796f` | 2 | :118 / :41 |

Texto de los nodos en `#1f1f1f` (`TINTA`, `generar_figura_tripleta.py:152`),
como en la figura 1.1. Llamadas en `#6f6f6f` con líneas en `#8a8a8a`, los
grises de la figura 1.1 (:153-154). Arista y rótulo en el gris oscuro
`#4a5a6a` (`TRAZO_ARISTA`, :159), en trazo continuo, como en la versión 1.

- Composición (`componer`, :301-367): los dos nodos en una fila, a 24
  unidades de los bordes del lienzo (`MARGEN`, :166) y de 260 de ancho
  (`W_NODO`, :167); las llamadas de los nodos arriba, centradas sobre su
  caja, con una línea vertical hasta el borde superior de la caja; la arista
  del borde derecho del origen al borde izquierdo del destino, a 2 unidades de
  cada uno, con el rótulo encima; la llamada de la relación abajo, con su
  línea desde la arista.
- Respecto de la versión 1, el SVG conserva iguales las líneas de las dos
  llamadas de los nodos, la y de sus textos, la posición (x, y) y el ancho de
  las cajas, el color, el grosor y la flecha de la arista y el formato de su
  rótulo; cambian el contenido, el formato de los nodos, los colores de las
  cajas, la x y el anclaje de los textos de llamada de nodo, y las y que
  dependen del alto de los nodos (arista, rótulo y llamada de la relación). Comparación papel por papel hecha en FIG-TRIPLETA-R2B fuera del
  repositorio, entre `git show 88bfe89:docs/tesis/figuras/figura_tripleta.svg`
  y el SVG de §9.
- Tamaño: lienzo 720 × 203 → **12,75 × 3,59 cm** (`ANCHO_FIGURA_CM`, :149:
  0,85 del ancho de texto de 15 cm, como en la versión 1 y en
  `generar_figura_proceso_extraccion.py:91-95`). PNG 1506 × 425 px a 300 dpi;
  PDF 361,4 × 101,9 pt (`pdfinfo figura_tripleta.pdf`).
- Letra impresa a 12,75 cm (`FS_NODO` a `FS_LLAMADA`, :161-163): encabezados,
  etiquetas y rótulo de la arista 17 → 8,53 pt; llamadas 15 → 7,53 pt;
  mínimo 7 pt (`PT_MINIMO`, :151). Los mismos tamaños que la versión 1.
- Inclusión en la tesis: a `0.85\linewidth` (dato de la autora del
  07/10/2026; el texto de Overleaf, NO VERIFICADO). Con el ancho de texto de
  15 cm son 12,75 cm, el ancho que declara el SVG: letra mínima 7,53 pt; a
  13 cm, 7,68 pt. La letra de 15 unidades llega a 7 pt con 11,85 cm de ancho
  (7 × 720 / (15 × 28,3465)). Cálculo hecho en FIG-TRIPLETA-R2B sobre el SVG
  de §9, fuera del repositorio.

## 7. Controles

Extracto de la salida de la corrida que escribió las salidas de §9:

```
PRUEBAS NEGATIVAS: 6 de 6 hacen fallar su control
INVENTARIO (releído del SVG): 2 nodos, 1 arista, 3 llamadas; fallas: 0
  nodo de origen  caja condicion_monto: ('Condicion', '5.1.1.1', 'Superar dos veces importe referencia punto 3.7')
  nodo de destino caja operacion: ('Operacion', '5.1.1.1', 'Inclusión en cartera comercial — créditos consumo/vivienda')
  arista ('Condicion', '5.1.1.1', 'Superar dos veces importe referencia punto 3.7') --condicion_de--> ('Operacion', '5.1.1.1', 'Inclusión en cartera comercial — créditos consumo/vivienda')
  llamada 'nodo de origen' -> caja condicion_monto
  llamada 'nodo de destino' -> caja operacion
  llamada 'relación · nombre y dirección' -> arista 0
GEOMETRÍA: 10 textos, 2 cajas, 1 trazo con flecha; 4 trazos con las llamadas; cruces 0; fallas: 0
TAMAÑO: lienzo 720 x 203.0, impreso a 12.75 x 3.59 cm
```

- **Inventario** (`inventario_svg` y `controlar_inventario`,
  `generar_figura_tripleta.py:379-513`): solo desde el SVG, cada caja de nodo
  con su encabezado «Tipo · punto N», su etiqueta y sus colores; la arista
  con la caja en cuyo borde empieza y la caja en cuyo borde termina, que es la
  de la flecha, y su rótulo; cada línea de llamada con el texto junto a un
  extremo y la caja o la arista junto al otro. La tripleta rearmada (tipo,
  punto y etiqueta de cada caja, rótulo y sentido de la arista) tiene que ser
  la del grafo; la llamada «nodo de origen» tiene que apuntar a la caja donde
  la arista empieza y «nodo de destino», a la caja donde termina; y cada caja
  tiene que tener los colores del tipo que escribe su encabezado.
- **Geometría** (`controlar_geometria` de la figura 1.1): textos medidos con
  las métricas reales de Helvetica; ningún texto superpuesto con otro, sobre
  una caja que no lo contiene, sobre un trazo que no es el suyo ni fuera del
  lienzo; ningún trazo con flecha que atraviese una caja; letra de 7 pt o más.
- **Líneas de llamada** (`controlar_llamadas`, :519-552), que el control
  anterior no mira porque no llevan flecha: ninguna toca una caja ni un texto,
  y entre los cuatro trazos (la arista y las tres llamadas) hay **0 cruces**.
- **Carga** (`cargar`, :262-273): los candados de §2, los controles del
  subgrafo de §3 a §5, la firma de §4 y la igualdad con la figura 1.1.
- Verificación geométrica de la versión 1, con
  `docs/tesis/figuras/verificar_geometria_svg.py` (archivo no rastreado,
  sha256 `fd8d062df7b7529131f466df628298e02dd079517aa66624caeea6a8b722df19`):
  10 textos, 2 nodos, 1 trazo con flecha; fallas: 0.

## 8. Pruebas negativas

Corren antes de componer (`PRUEBAS_NEGATIVAS`, :559-564); cada una tiene que
hacer fallar su control con su propia falla:

```
direccion_invertida -> inventario: arista de la figura que no está en el grafo: (None, 'condicion_de', None)
llamadas_intercambiadas -> inventario: la arista origen en la caja condicion_monto; la llamada de origen, en operacion
etiqueta_distinta -> inventario: nodo de la figura que no está en el grafo: ('Operacion', '5.1.1.1', 'Inclusión en cartera comercial — créditos de consumo o vivienda')
tipo_cambiado -> inventario: la caja condicion_monto dice Restriccion y no tiene los colores de Restriccion
rotulo_sobre_caja -> geometria: texto sobre la caja operacion: 'condicion_de'
cruce -> llamadas: 1 cruce(s) entre trazos, declarados 0: [('arista 0', 'relacion')] (fallan también: inventario)
```

Con `--perturbar <caso>`, sobre una copia, los seis terminan con «FALLA: la
figura tiene defectos; no se escribe nada», código 1 y ningún archivo
escrito. Con cualquiera de las cinco fuentes de §2 alterada en una copia (un
salto de línea agregado al final), el generador frena por el candado, código
1, sin archivos. Con las fuentes intactas, cinco alteraciones en memoria de
lo ya cargado (una etiqueta y un color distintos de los de la figura 1.1; la
firma fuera de `AMPLIACION_R2`; `condicion_de` entre los derivados; y
`condicion_de` fuera de `PREDICADOS`) hacen frenar a `controlar_figura_1_1`
y a `controlar_firma` con su propio mensaje. Las tres comprobaciones se
hicieron en FIG-TRIPLETA-R2B sobre copias, fuera del repositorio.

## 9. Salidas y reproducibilidad

| Archivo | sha256 |
|---|---|
| `generar_figura_tripleta.py` | `318fa90734ef9b9519c52ada382aefae23568f4434cdc17285c222151ae17515` |
| `figura_tripleta.svg` | `2b900b1de5030ae80a75d86b65753f2598d3dc9f37a54caec2f830e02bcaf440` |
| `figura_tripleta.png` | `0998d4a0f433849f90c717a0140359aaaa12feea663569f6613fb5620efee85c` |
| `figura_tripleta.pdf` | `5c69c29af2c480a86600684d03bdece63c99e5e1ddfcb5102128dd735988b674` |

Tres corridas sobre una copia de las fuentes (copiadas, sin enlaces), con
`PYTHONHASHSEED` 0, 1 y 4242 y `--salida`: el mismo SVG, el mismo PNG, el
mismo PDF y la misma salida de texto; la corrida sin `--salida` escribe junto
al generador los mismos tres archivos. El PDF lleva la fecha de creación
fijada por `SOURCE_DATE_EPOCH=0` (`generar_figura_norma_a_grafo.py:220`, que
usa `exportar`).

## 10. Observaciones

- **Estilo de la arista**: la figura 1.1 dibuja esta misma `condicion_de` en
  gris discontinuo `#8a8a8a` de 1,5, con el rótulo sin negrita
  (`figura_norma_a_grafo.svg:24-26`); esta figura la dibuja en trazo
  continuo `#4a5a6a` de 2,6, como la versión 1. La versión 1 tenía la misma
  diferencia con su figura 1.1 (`limita`).
- **Impreso**: NO VERIFICADO; la letra y las distancias se controlan sobre la
  geometría, a 12,75 cm de ancho.
