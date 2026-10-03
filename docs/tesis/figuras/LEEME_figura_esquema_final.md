# figura_esquema_final — registro de generación

Figura de la sección 3.10: el esquema final con que se construye el grafo del
corpus, que es el esquema congelado más L-ESQ-R2 y su enmienda 2. Dibuja los 9
tipos de entidad más `Sujeto`, las 13 relaciones que emite el extractor con sus
28 firmas, `remite_a` (la relación que deriva el código) y la marca de los 4
tipos con la propiedad `umbrales`. Lo que el esquema final agrega respecto del
esquema de partida va en magenta solo en las cajas de los tipos nuevos y en los
rótulos de las relaciones nuevas; todas las líneas de relación van en el gris
de la figura de partida.

Este LEEME describe la **versión 3**: la versión 2 con todas las líneas en gris,
el magenta solo en cajas y rótulos nuevos, un segundo rótulo de `condicion_de`
y la leyenda nueva. Cajas, grupos, trazado y cruces no cambian. Las versiones 1
y 2 (sin commit, reemplazadas) quedaron en el paquete de revisión de cada una;
el §8 detalla qué cambió en cada paso.

GENERADA POR SCRIPT, nunca a mano. El script lee cada dato del código, con
candado de sha256 sobre cada fuente, y hereda de la figura del esquema de
partida el tamaño y el estilo de cajas y grupos, la paleta, la tipografía y los
trazos que unen cajas que se desplazan juntas. Usa solo la biblioteca estándar
(más `rsvg-convert` para el PNG y el PDF). Estado: FRENO, sin commit (commit
PENDIENTE de la autora). Este LEEME cae en `.gitignore:180` y entra solo con
`git add -f`, como sus hermanos.

## 1. Comandos

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_esquema_final.py
```

Escribe `figura_esquema_final.svg`, `.png` y `.pdf` en `docs/tesis/figuras/`
(con `--salida <dir>`, en otro directorio) e imprime el reporte de los
controles. Si un control falla, imprime `FRENO [control] motivo` y no escribe
nada.

Pruebas negativas por línea de comandos (cada una tiene que terminar con
código 1 y sin escribir archivos):

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_esquema_final.py --mutacion caja_fuera_de_grupo --salida /tmp/no_escribe
```

(ídem con `firma_de_mas`, `firma_de_menos`, `linea_no_gris`,
`rotulo_sobre_caja` y `tramo_diagonal`). Las seis corren además en cada
ejecución normal, antes de escribir (§6).

## 2. Fuentes y sellos

Fuentes que el script lee, con candado de sha256 (`FUENTES` en el script):

| Fuente | sha256 | Último commit que la tocó |
|---|---|---|
| `data/experiment/pyd_r2/generados/enums_r2.json` | `abd197ac8bbb818f680dc80d1b9c9df3e1f1f733fce3fd46b35e7440e7ce4241` | `eb277ce` |
| `scripts/remisiones.py` | `1da7464195875b1206ee9b1d1a15ac10f5976e5ce3700ccb230c7410bb9fde6d` | `92b45d6` |
| `data/experiment/grafo_v2/code/schema.py` (esquema de partida) | `cc98e4354cf2ad507954f7fa99f12b8445e6157c9a0bcb026a13908e63de7eab` | `fac503f` |
| `docs/tesis/figuras/figura_esquema_partida.svg` (figura de partida, v3) | `be98b797e3f6338818055cac12ed4308acb9a48df012177a923e45021f3b4a3a` | `c3bba5b` |

Los cuatro sha son los de la corrida (el script los comprueba antes de
dibujar). `remisiones.py` se ejecuta desde el texto verificado (`exec`), sin
importarlo; `schema.py` se lee con `ast`, sin ejecutarlo (importa pydantic).

Documentos firmados que fijan el esquema final (no los lee el script; leídos en
el commit de la firma, regla k):

| Documento | Commit | sha256 en ese commit | Qué fija |
|---|---|---|---|
| `data/experiment/esq/laudo_esquema_congelado.md` | `2593d4d` | `64c5da88…` | 9 tipos y 13 predicados (líneas 106-107) |
| `data/experiment/esq/enmienda_L-ESQ-R2_2026-09-30.md` (L-ESQ-R2) | `4ef7650` | `66c4a1b9…` | umbrales en Restriccion, Obligacion, Condicion y Excepcion (§1.3 a, líneas 242-243); `condicion_de` → Operacion y → Potestad (§6.3, X1 opción ii, línea 787) |
| `data/experiment/esq/enmienda2_L-ESQ-R2_remite_a_2026-10-02.md` (enmienda 2) | `5f9a731` | `e779bd70…` | `remite_a`, 56 firmas (§2, línea 73) |

Salidas de esta corrida (versión 3):

| Archivo | sha256 |
|---|---|
| `figura_esquema_final.svg` | `dfdb16d471bb93c6351aa03b1e609452b75c428baa354c52354ce1dfe9797bb3` |
| `figura_esquema_final.png` | `cfc5cc61c64b6f0942b76c19fe49da4da1c2de61d834623b9ff1f55e274d698f` |
| `figura_esquema_final.pdf` | `e9b6650fd7fc1245053682b75172e54794e36f59a2a68facddc004350a9dbac1` |
| `generar_figura_esquema_final.py` (script, versionado junto a la figura) | `0d6274fe2d3a870ff8776b29f9d69195867ffbced767355a5a2fa20ee756bb15` |

Versiones reemplazadas: la 2, SVG `30d6682c…`, PNG `fa0d92d3…`, PDF
`bdfc1880…`, script `50b8e714…`; la 1, SVG `658e7c2f…`, PNG `abb01c41…`, PDF
`7d1c4bd9…`, script `9c6deec8…`.

Recomputo: `shasum -a 256 docs/tesis/figuras/figura_esquema_final.{svg,png,pdf}`.
Determinismo: corridas con `PYTHONHASHSEED` 1, 2 y 3 dan los mismos tres sha;
el PDF se fija con `SOURCE_DATE_EPOCH=0`.

## 3. Fuente de cada dato de la figura

| Dato | Fuente |
|---|---|
| Las 9 cajas de tipo | `enums_r2.json:8` (`tipo_entidad`) |
| La caja `Sujeto` | extremo de `aplica_a` y `ejecuta`: `enums_r2.json:34` (`predicados_sujeto`) y los rangos de `firmas_r2` |
| Las 13 relaciones del extractor | `enums_r2.json:19` (`predicado`) |
| Sus 28 firmas | `enums_r2.json:169` (`firmas_r2`); el script asserta que son las 26 de `firmas_congeladas` (`:38`) más las 2 de `ampliacion_r2` (`:157`) |
| `remite_a` y sus 56 firmas | `scripts/remisiones.py:16` (`PREDICADO_REMISION`), `:21` (`TIPOS_CONTENIDO`), `:22` (`TIPO_TEXTO_ORDENADO`) y `:41-44` (`firma_remite_a_ok`, evaluada sobre los 10 × 10 pares de tipos y Sujeto) |
| Los 7 tipos que nombra la leyenda de `remite_a` | los mismos `TIPOS_CONTENIDO` (`remisiones.py:21`), en el orden en que aparecen en la figura (grupo de la izquierda de arriba abajo, luego Operacion y Definicion); el script asserta que coinciden con el dominio de `establecida_en` en `firmas_r2` |
| La marca de umbrales | `enums_r2.json:340` (`tipos_con_umbrales`), cotejada con `claves_por_tipo` (`:290`) |
| Qué es nuevo respecto de la partida | `schema.py:24-31` (`ENTITY_TYPES`, 6 tipos) y `schema.py:167-180` (`DOMAIN_RANGE`, 12 relaciones, 17 firmas); las 17 están contenidas en las 28 |
| Tamaño y estilo de las 7 cajas y de los grupos de la partida, nota de Sujeto, paleta, tipografía y cuerpos de letra | `figura_esquema_partida.svg` (`c3bba5b`), leído elemento por elemento |
| Los 24 tramos conservados de la partida (10 firmas, §8) | los `<path>` de `figura_esquema_partida.svg`, trasladados con sus cajas |
| Color de lo agregado (`#b5179e`; en las cajas nuevas, borde de 2,6 px y relleno al 90 % de blanco) | el de la figura del esquema congelado: `generar_figuras_esquema.py:147` (`RESALTE`) y `:161` |
| Gris y grosor de todas las líneas de relación y sus puntas (`#8a8a8a`, 1,6 px) | los de los `<path>` de `figura_esquema_partida.svg` |
| Qué relaciones son nuevas (rótulo en magenta) | `condicion_de`: las relaciones de `enums_r2.json:19` (`predicado`) que no están en `DOMAIN_RANGE` (`schema.py:167-180`); `remite_a`: `remisiones.py:16` |
| Rótulos de los grupos nuevos, textos de la leyenda y marca «≤» | texto de la figura, no dato |
| Desplazamientos, cajas nuevas, trazos nuevos y grupos nuevos | diseño de esta figura (`DESPLAZAMIENTO`, `CAJAS_NUEVAS`, `TRAZOS_NUEVOS`, `TRAZOS_REMITE`, `GRUPO_IZQUIERDA`, `GRUPO_DEFINICION` en el script) |

## 4. Firmas dibujadas, red por red

El control de firmas no usa las etiquetas del dibujo: arma las redes de trazos
conectados de cada relación, toma como fuentes las cajas donde una red empieza
y como destinos las cajas donde tiene una punta, y compara el producto con las
firmas del código.

| Relación | Fuentes → destinos | Firmas |
|---|---|---|
| `establecida_en` (peine izquierdo) | Obligacion, Restriccion, Excepcion, Potestad, Condicion → TextoOrdenado | 5 |
| `establecida_en` (bus derecho) | Operacion, Definicion → TextoOrdenado | 2 |
| `aplica_a` (un bus) | Obligacion, Restriccion, Excepcion, Potestad, Operacion → Sujeto | 5 |
| `condicion_de` (un bus) | Condicion → Obligacion, Restriccion, Excepcion, Operacion, Potestad | 5 |
| `regula` (dos flechas) | Obligacion → Operacion; Restriccion → Operacion | 2 |
| `referencia`, `modificada_por`, `ejecuta`, `exceptua`, `exceptua_obligacion`, `prohibe`, `limita`, `requiere`, `condiciona` | una flecha cada una | 9 |
| **Relaciones del extractor** | | **28** |
| `remite_a` (discontinua) | lazo que sale del grupo de la izquierda y vuelve a él, y flecha a TextoOrdenado; la leyenda nombra los 7 tipos de contenido | 7 × 8 = **56** |

Suma: 5 + 2 + 5 + 5 + 2 + 9 = 28. De las 28, 11 son nuevas respecto de la
partida: `establecida_en` desde Potestad, Condicion y Definicion (3),
`aplica_a` desde Excepcion, Operacion y Potestad (3) y las 5 de `condicion_de`.
17 + 11 = 28.

Para `remite_a`, el control exige que la red discontinua salga del borde del
grupo de la izquierda, vuelva a él y llegue a TextoOrdenado; que la leyenda
nombre exactamente los tipos de contenido del código; y que los tipos del
grupo de la izquierda estén entre ellos. Las firmas que la figura afirma son
entonces 7 × (7 + 1) = 56, las del código.

El SVG emitido se relee: sus atributos `data-firmas` dan las mismas 28; el de
`remite_a` da «grupo>grupo» y «grupo>TextoOrdenado»; cada grupo declara sus
cajas (`data-grupo`, `data-cajas`); la leyenda declara y nombra los 7 tipos
(`data-tipos` y sus nombres en monoespaciada); y las marcas, los 4 tipos con
umbrales (`data-umbrales`).

## 5. Cruces

**6 cruces**, los mismos de la versión 2 (y 6 en número, como en la versión
1), todos en X entre flechas de redes distintas y exactamente los de
`CRUCES_DECLARADOS`:

| Punto | Trazos |
|---|---|
| (64, 308) | tronco de `aplica_a` × diente `establecida_en` de Restriccion |
| (64, 408) | tronco de `aplica_a` × diente `establecida_en` de Excepcion |
| (78, 308) | `exceptua_obligacion` × diente `establecida_en` de Restriccion |
| (78, 340) | `exceptua_obligacion` × diente `aplica_a` de Restriccion |
| (40, 224) | `condicion_de` hacia Obligacion × tronco izquierdo de `establecida_en` |
| (292, 513) | `condicion_de` hacia Restriccion, Excepcion y Operacion × `aplica_a` hacia Sujeto |

Los cuatro primeros son los de la figura de partida, trasladados 48 px: los
dos peines de la izquierda y el rodeo de `exceptua_obligacion` (su LEEME, §7,
explica por qué no bajan con esas cajas). Los otros dos son de `condicion_de`:
Obligacion queda encerrada entre el peine de `establecida_en` y el corredor
hacia Operacion, y la rama derecha cruza una vez el bus de `aplica_a` donde
este sale de la columna hacia Sujeto.

Tres decisiones del trazado mantienen el número en 6 con Potestad y Condicion
en la columna:

- Los dientes de `establecida_en` de Potestad y Condicion quedan por debajo
  del tronco de `aplica_a`, que termina en el hueco entre Excepcion y
  Potestad. Si `aplica_a` siguiera por la izquierda hasta un Sujeto ubicado
  debajo de la columna, esos dos dientes lo cruzarían, y serían 2 cruces más.
- Por eso Sujeto pasa debajo de Operacion, y `aplica_a` es un solo bus: el
  tronco izquierdo gira por ese hueco hasta Sujeto, Potestad sube a él desde
  su borde superior y Operacion baja a él.
- La rama de `condicion_de` hacia Restriccion, Excepcion y Operacion corre por
  la derecha de la columna, donde no hay dientes. La rama hacia Obligacion
  rodea la columna por fuera, por la izquierda.

## 6. Controles (todos en el script; el primero que falla FRENA)

0. **Grupos**: cada caja dentro de su grupo (`MIEMBROS`) y fuera de los
   demás; Sujeto, fuera de todos; grupos a 6 px o más entre sí.
1. **Firmas**, sobre la geometría (§4): las 28 del código, ni una de más ni
   una de menos. `condicion_de` es un solo bus con 5 puntas, y `remite_a`
   cumple lo del §4. Además, la relectura del SVG.
2. **Trazado**: ningún tramo diagonal ni de largo cero; ningún extremo suelto;
   ningún trazo atraviesa una caja ni corre sobre su borde; los puntos por los
   que las flechas llegan a una caja o salen de ella están a 10 px o más entre
   sí; ninguna punta toca otra red; ningún par de tramos paralelos de redes
   distintas a menos de 10 px; cajas a 10 px o más entre sí; ningún tramo sin
   firma.
3. **Cruces**: entre redes distintas solo cruces en X (un toque en T o un tramo
   superpuesto frena), y el conjunto exacto de `CRUCES_DECLARADOS`.
4. **Textos** (42): ningún texto toca un trazo, una punta, una caja, el borde
   de un grupo, una muestra de la leyenda ni otro texto. Los rótulos se miden
   con su halo (1,75 px) más 1 px de luz; el texto, con el avance de Menlo
   (0,602 em) y los anchos AFM de Helvetica. La única excepción es la punta de
   la propia relación, que puede rozar el halo pero no el texto, que es como
   está `exceptua_obligacion` en la figura de partida. Cada rótulo de relación
   queda a 6 px o menos de su red y al menos 5 px más cerca de ella que de
   cualquier otra, con un rótulo por red (dos en `condicion_de`). Ningún texto
   baja de 7 pt impresos. El segundo rótulo de `condicion_de` tiene tope de
   14 px en lugar de 6: va a la derecha del grupo de la izquierda, junto al
   tramo vertical (x = 292) que corre 8 px adentro del borde del grupo; del
   lado de adentro, las cajas y el bus de `aplica_a` no dejan lugar, y del de
   afuera el rótulo no puede tocar el borde, así que queda a 13,1 px del
   tramo, sin otra red a menos de 57,8 px.
5. **Margen**: nada a menos de 2 mm del borde (mínimo medido: 2,29 mm).
6. **Colores**, sobre el SVG que se emitiría: las 75 líneas de relación y las
   21 puntas, en el gris de la partida (`#8a8a8a`, 1,6 px); rótulos en magenta
   solo los de las relaciones nuevas (`condicion_de`, sus dos rótulos, y
   `remite_a`); cajas con borde magenta solo las de los tipos nuevos
   (Potestad, Condicion, Definicion).

Cercanía medida de los 17 rótulos (salida del script):

| Rótulo | A su red | A la red ajena más cercana |
|---|---|---|
| `aplica_a` (170, 505) | 4,4 px | 24,1 px (`condicion_de`) |
| `condicion_de` (98, 738) | 4,6 px | 76,6 px (`establecida_en`) |
| `condicion_de` (316,5, 625), rotado | 13,1 px | 57,8 px (`aplica_a`) |
| `condiciona` | 4,6 px | 28,6 px (`regula`) |
| `ejecuta` | 4,6 px | 57,6 px (`aplica_a`) |
| `establecida_en` (330, 76), peine | 3,4 px | 21,4 px (`remite_a`) |
| `establecida_en` (826, 273), bus derecho | 6,0 px | 71,6 px (`modificada_por`) |
| `exceptua` | 6,0 px | 24,0 px (`condicion_de`) |
| `exceptua_obligacion` | 6,0 px | 16,6 px (`condiciona`) |
| `limita` | 4,6 px | 12,4 px (`condicion_de`) |
| `modificada_por` | 6,0 px | 21,6 px (`referencia`) |
| `prohibe` | 4,6 px | 13,4 px (`limita`) |
| `referencia` | 6,0 px | 32,3 px (`remite_a`) |
| `regula` (385, 296) | 4,4 px | 21,4 px (`prohibe`) |
| `regula` (418, 202) | 4,4 px | 14,6 px (`requiere`) |
| `remite_a` (430, 117) | 4,6 px | 22,6 px (`establecida_en`) |
| `requiere` | 4,4 px | 38,4 px (`regula`) |

**Pruebas negativas** (`MUTACIONES`). Cada ejecución las corre sobre una copia
del modelo antes de escribir, y exige que cada una frene en su control:

| Mutación | Freno |
|---|---|
| `caja_fuera_de_grupo`: Potestad 240 px a la derecha, fuera del grupo de la izquierda | `[grupos] la caja Potestad está fuera de su grupo «izquierda»` |
| `rotulo_sobre_caja`: el rótulo `limita` al centro de Operacion | `[textos] nombre «Operacion» toca rotulo «limita»` |
| `tramo_diagonal`: el diente de `establecida_en` de Potestad sale 20 px más abajo | `[trazado] tramo diagonal de establecida_en: (90.0, 570.0) → (40.0, 550.0)` |
| `firma_de_mas`: una punta de `condicion_de` hacia Definicion | `[firmas] firmas de más en el dibujo: [('condicion_de', 'Condicion', 'Definicion')]` |
| `firma_de_menos`: sin el diente de `aplica_a` de Excepcion | `[firmas] firmas de menos en el dibujo: [('aplica_a', 'Excepcion', 'Sujeto')]` |
| `linea_no_gris`: las líneas de `condicion_de` en magenta | `[colores] la línea de condicion_de no es gris: #b5179e, 1.6 px` |

Por línea de comandos (`--mutacion`), las seis terminan con código 1 y no
escriben archivos.

## 7. Convenciones de dibujo

- **Ubicación de las cajas**, la de la figura del esquema congelado: Potestad y
  Condicion en el grupo de la izquierda, debajo de Excepcion; Definicion en su
  grupo, a la derecha y debajo del acto regulado.
- **Grupos**: el de la izquierda se rotula «lo que manda, prohíbe, exime / o
  permite la norma, y cuándo», en dos líneas. Es un rótulo equivalente al del
  mandato, porque el del mandato no entra en dos líneas: su primera línea
  posible, «lo que la norma manda, prohíbe,», mide 216,8 px (anchos AFM de
  Helvetica a 15 px), y el grupo, de 224 px, deja 216 px desde donde empieza
  el rótulo. El grupo de Definicion se rotula «lo que la norma define».
- **Buses.** Las firmas de una misma relación comparten tramo y punta.
- **Líneas**: todas las líneas de relación y sus puntas van en el gris de la
  figura de partida, también `condicion_de`, las ramas nuevas de `aplica_a` y
  `establecida_en` y `remite_a`. Cada línea se sigue por su trazado y su
  rótulo, como en la figura de partida.
- **Magenta** (`#b5179e`): solo en el borde y el fondo de los 3 tipos nuevos y
  en los rótulos de las 2 relaciones nuevas (`condicion_de` y `remite_a`). Los
  rótulos de las demás relaciones van en gris aunque tengan firmas nuevas.
  `condicion_de` lleva dos rótulos: abajo, junto al tramo que rodea la
  columna, y junto a su tramo vertical, a la derecha del grupo de la izquierda.
- **Discontinuo**, en gris: lo que deriva el código, es decir `remite_a`. Se dibuja una
  sola vez, en la franja entre el tramo superior de `establecida_en` y el
  borde superior del grupo de la izquierda: un lazo que sale del grupo y
  vuelve a él, y una flecha hacia TextoOrdenado, con un solo rótulo. La
  leyenda dice que la deriva el código y que vale entre cualquier par de los 7
  tipos de contenido, y los nombra en monoespaciada.
- **Marca de umbrales**: un cuadro oscuro con «≤» en el extremo derecho de la
  caja, igual en los 4 tipos, explicado en la leyenda (sin cambios desde la
  versión 1).
- **Sujeto**: borde discontinuo y la nota «se elige de un catálogo», como en la
  partida. Las relaciones de pertenencia del catálogo no se dibujan.
- **Leyenda**, con 3 entradas: una caja y un rótulo de ejemplo («relación»)
  en magenta, «tipo o relación agregados respecto del esquema de partida»; la
  línea discontinua gris, con el texto de `remite_a` y los 7 tipos; y la marca
  «≤» de los umbrales.

## 8. Qué cambió en cada versión

### 8.1 De la versión 2 a la 3

| Elemento | Versión 2 | Versión 3 |
|---|---|---|
| Líneas de relación y puntas | magenta lo nuevo (`condicion_de`, ramas nuevas de `aplica_a` y `establecida_en`, `remite_a`), gris lo de la partida | todas en gris `#8a8a8a`, 1,6 px; `remite_a`, discontinua gris |
| Rótulos | magenta los de redes enteramente nuevas | magenta los de las relaciones nuevas (`condicion_de`, `remite_a`), regla tomada del código; los demás en gris |
| `condicion_de` | un rótulo, abajo | dos rótulos: abajo y junto a su tramo vertical, a la derecha del grupo de la izquierda |
| Cajas nuevas | borde y fondo magenta | sin cambios |
| Leyenda | caja y flecha magenta «agregado respecto del esquema de partida»; marca de umbrales en la misma fila | caja y rótulo de ejemplo en magenta, «tipo o relación agregados respecto del esquema de partida»; discontinua gris de 1,6 px; marca de umbrales en su propia fila |
| Lienzo e impresión | 850 × 834; 15,00 × 14,72 cm | 850 × 860; 15,00 × 15,18 cm (la fila nueva de la leyenda) |
| Controles | 6 grupos y 5 pruebas negativas | + control de colores y prueba `linea_no_gris` |

Comparación elemento por elemento del SVG de la versión 2 con el de la 3
(script del paquete de revisión): los 75 trazos (mismo `d`, relación y
firmas), las 10 cajas, los 4 grupos y los 16 rótulos de la versión 2 son
idénticos; la versión 3 suma el segundo rótulo de `condicion_de` y pierde la
punta de la flecha de ejemplo de la leyenda.

### 8.2 De la versión 1 a la 2

| Elemento | Versión 1 | Versión 2 |
|---|---|---|
| Potestad, Condicion | debajo de todo, fuera de los grupos | en el grupo de la izquierda, debajo de Excepcion |
| Definicion | abajo a la derecha, sin grupo | grupo propio «lo que la norma define», debajo del acto regulado |
| Grupo de la izquierda | el de la partida, «lo que la norma manda, prohíbe o exime» | mismo ancho (224 px) y estilo, alto de 306 a 574 px, rótulo en dos líneas que incluye a Potestad y Condicion |
| Fondo «tipos de contenido» | polígono gris azulado | eliminado |
| `remite_a` | salía del fondo, volvía a su borde y subía por la derecha hasta TextoOrdenado | lazo sobre el grupo de la izquierda y flecha a TextoOrdenado, en la franja sobre el grupo; la leyenda nombra los 7 tipos |
| Cajas de la partida | en su lugar | mismo tamaño y estilo; Obligacion, Restriccion, Excepcion y Operacion bajan 48 px; Sujeto pasa debajo de Operacion (+235, +20) |
| Trazos de la partida | los 40 tramos en su lugar | se conservan, trasladados, los de las 10 firmas cuyas dos cajas se desplazan juntas (el corredor hacia Operacion, `exceptua`, `exceptua_obligacion`, `referencia` y `modificada_por`): 24 tramos |
| `establecida_en` | peine de 3 y bus derecho con Operacion, Potestad, Definicion y Condicion | peine de 5 (Potestad y Condicion se suman) y bus derecho con Operacion y Definicion |
| `aplica_a` | peine de 4 y acceso propio desde Operacion | un solo bus de 5 |
| `condicion_de` | rodeo largo desde abajo | rama por la izquierda hasta Obligacion y rama por la derecha de la columna |
| Cruces | 6 | 6 |
| Lienzo e impresión | 890 × 804; 15,00 × 13,55 cm; letra mínima 7,17 pt | 850 × 834; 15,00 × 14,72 cm; letra mínima 7,50 pt |
| Controles | 5 grupos de controles y 4 pruebas negativas | + control de grupos y prueba `caja_fuera_de_grupo` |

Contraste independiente (script del paquete de revisión, que lee el SVG final
y el de partida sin usar el generador):

- sobre el SVG final, 6 cruces, 0 tramos diagonales y 28 firmas;
- los 4 grupos contienen exactamente las cajas que declaran, y Sujeto queda
  fuera de todos;
- las 7 cajas de la partida conservan su estilo;
- «acto regulado» y «anclaje documental» conservan tamaño y estilo; el grupo
  de la izquierda cambia de alto, como se declara arriba;
- los 24 tramos de partida de las firmas cuyas cajas se desplazan juntas
  aparecen, trasladados, en la figura final.

## 9. Composición y tamaño impreso

| Magnitud | Valor |
|---|---|
| Lienzo | 850 × 860 |
| Impresa | 15,00 × 15,18 cm (SVG con `width="15cm"`) |
| PNG | 1772 × 1793 px, 300 dpi grabados en el bloque pHYs |
| PDF | 425,20 × 430,19 pt = 15,00 × 15,18 cm |

A 15 cm, un píxel del lienzo mide 425,2 / 850 = 0,50 pt:

| Elemento | En el lienzo | Impreso |
|---|---|---|
| Nombre de tipo (Menlo, negrita) | 19 px | 9,50 pt |
| Rótulos de relación, de grupo, nota, leyenda y marca | 15 px | 7,50 pt |

El lienzo tiene el ancho de la figura de partida (850 px), así que la escala a
15 cm es la de la partida a 15 cm.

## 10. Epígrafe propuesto

Tipos de entidad y relaciones del esquema final con que se construye el grafo
del corpus, con el trazado de la figura del esquema de partida y las relaciones
que salen de varios tipos o llegan a varios dibujadas con un tramo común.
Potestad y Condicion entran en el grupo de lo que la norma manda, prohíbe,
exime o permite, y cuándo, y Definicion forma el grupo de lo que la norma
define. Los tipos y las relaciones que el esquema final agrega respecto del
esquema de partida se marcan en magenta, en la caja de Potestad, Condicion y
Definicion y en el rótulo de condicion_de y de remite_a. La línea discontinua
marca remite_a, que deriva el código y vale entre cualquier par de los siete
tipos de contenido y hacia TextoOrdenado, y la marca ≤ señala los tipos que
llevan la propiedad umbrales. El borde discontinuo de Sujeto indica que se
elige de un catálogo.
