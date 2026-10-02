# figura_esquema_partida (F1) — registro de generación

Figura F1 del capítulo del esquema: tipos de entidad y matriz dominio/rango
del **esquema de partida** de la extracción v2 — 6 tipos de entidad más el
pseudo-tipo `Sujeto`, cuyo extremo se elige de un catálogo, y 12 relaciones.

GENERADA POR SCRIPT desde el artefacto sellado, nunca dibujada a mano: el
script IMPORTA `data/experiment/grafo_v2/code/schema.py` y dibuja exactamente
lo que declaran `ENTITY_TYPES` y `DOMAIN_RANGE`; si los conteos no son los
sellados (6 tipos, 12 firmas, 17 pares), el script FRENA con AssertionError
antes de escribir. Comparte script y posiciones de caja con la figura F1b
(`figura_esquema_congelado.svg`, mismo directorio).

Este LEEME describe la **versión 3**. En ninguna versión cambia el
contenido: las mismas 7 cajas y las mismas 17 flechas.

La **versión 3** corrige los tres textos que en la versión 2 tocaban un trazo
o una caja fuera del corredor (§8) y extiende a TODA la figura la guarda de
cruces y rótulos que la versión 2 aplicaba al corredor (§4). La **versión 2**
cambió tres cosas respecto de la versión 1:

1. Las seis flechas entre `Obligacion`, `Restriccion` y `Operacion`
   (`regula` ×2, `condiciona`, `prohibe`, `limita`, `requiere`) dejan de ser
   diagonales que convergían en los 46 px del borde izquierdo de `Operacion`
   —con rótulos superpuestos entre sí— y pasan a trazos ortogonales
   separados, cada uno con su rótulo del lado libre (§3).
2. La zona que agrupa `Obligacion`, `Restriccion` y `Excepcion` se rotula
   «lo que la norma manda, prohíbe o exime» (antes «contenido deóntico»).
3. La nota bajo `Sujeto` dice «se elige de un catálogo» (antes «catálogo
   cerrado (no lo emite el extractor)»): la figura describe el esquema, no el
   proceso que lo usa.

**F1b no cambia.** El script la sigue emitiendo, y sale byte-idéntica a su
versión anterior (sha256 `4be96296…`, §2): rutas nuevas, rótulos de zona,
nota de `Sujeto` y posiciones de rótulo de la versión 3 están condicionados a
F1. Consecuencia declarada: F1 y F1b
siguen teniendo las cajas en las mismas posiciones, pero ya no el mismo
trazado del corredor ni los mismos rótulos.

## 1. Comando de generación

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figuras_esquema.py
```

Escribe `figura_esquema_partida.svg` (850 × 590) y también
`figura_esquema_congelado.svg`, e imprime el reporte de la guarda geométrica
de F1 (§4). En la versión 3 no corrí este comando sobre el repositorio, para
no reescribir F1b: lo corrí sobre una copia en el directorio de trabajo y
copié al repositorio el script y `figura_esquema_partida.svg`; el SVG de F1b
del repositorio no se tocó (mismo sha y misma fecha de modificación). El PNG
se exporta aparte:

```bash
rsvg-convert -z 2 -f png -o docs/tesis/figuras/figura_esquema_partida.png docs/tesis/figuras/figura_esquema_partida.svg
```

`rsvg-convert` (2.62.3) es la única herramienta externa, y solo para el PNG
(1700 × 1180 px). El SVG se produce con Python de la biblioteca estándar más
la cadena importada; corre con el `.venv` del repositorio (Python 3.10.13).

## 2. Fuentes y sellos

| Archivo leído (importado) | sha256 |
|---|---|
| `data/experiment/grafo_v2/code/schema.py` | `cc98e4354cf2ad507954f7fa99f12b8445e6157c9a0bcb026a13908e63de7eab` |

(El script también importa la cadena del esquema congelado para F1b; esos
sellos constan en `LEEME_figura_esquema_congelado.md`.)

Salidas de esta corrida:

| Archivo | sha256 |
|---|---|
| `figura_esquema_partida.svg` | `be98b797e3f6338818055cac12ed4308acb9a48df012177a923e45021f3b4a3a` |
| `figura_esquema_partida.png` | `13c94182eb4c8dbd25cad4d3c7f746b0cdcc807d2d6ac13f6f8208fca78ad144` |
| `figura_esquema_congelado.svg` (sin cambios) | `4be96296a64f7243b1b47facf80bbee678668fb302be2b5225110c2477edd30a` |
| `generar_figuras_esquema.py` (script, versionado junto a la figura) | `464f757f14e3e8a45a024f654e7b3ac5208907e988ddb050b0b1d5acc92fc8a6` |

(Versión 2, sin commit: SVG `cbc5cede…`, PNG `052b0444…`.)

Recomputo: `shasum -a 256 docs/tesis/figuras/figura_esquema_partida.{svg,png}`.

Generación determinística verificada: corridas con `PYTHONHASHSEED` 1, 2 y 3
producen el mismo SVG (`be98b797…`) y el mismo F1b (`4be96296…`); el PNG se
reproduce byte a byte con el mismo `rsvg-convert`. Antes de tocar el script
reproduje la versión 1 desde el commit vigente: SVG `6dce982c…` y PNG
`af4adf18…`, idénticos a los de la tabla de la versión 1.

## 3. El corredor Obligacion / Restriccion / Operacion

| Flecha | Trazado (coordenadas del SVG) | Rótulo |
|---|---|---|
| `requiere` Operacion → Obligacion | sale del borde superior de `Operacion` (x = 580), sube a y = 128 y entra a `Obligacion` por arriba (x = 262) | encima del tramo horizontal |
| `regula` Obligacion → Operacion | sale del borde derecho de `Obligacion` (y = 162) y baja al borde superior de `Operacion` (x = 555) | encima del tramo horizontal |
| `condiciona` Obligacion → Operacion | sale del borde derecho (y = 186) y baja al borde superior (x = 530) | debajo del tramo horizontal |
| `regula` Restriccion → Operacion | escalera: y = 256 → baja en x = 490 → entra al borde izquierdo en y = 338 | encima del primer tramo |
| `prohibe` Restriccion → Operacion | y = 273 → baja en x = 420 → entra en y = 353 | debajo del primer tramo, entre las bajadas de sus vecinas |
| `limita` Restriccion → Operacion | y = 290 → baja en x = 330 → entra en y = 368 | debajo del último tramo |

Las escuadras de `Obligacion` están anidadas (la que sale más arriba baja más
a la derecha) y la escalera de `Restriccion` también (la que sale más arriba
gira más a la derecha): por construcción ninguna se cruza con otra. Las tres
bajadas al borde superior quedan a la izquierda de x = 606, donde empieza la
zona «anclaje documental».

Dos ajustes que ese trazado obliga:

- **`exceptua_obligacion` pasa por la izquierda de `Restriccion`.** Una
  flecha de `Excepcion` (abajo) a `Obligacion` (arriba) que pase por la
  derecha de `Restriccion` cruza, por topología, toda flecha que salga de
  `Restriccion` hacia `Operacion`. Por la izquierda cruza en cambio los dos
  dientes izquierdos de `Restriccion` (`establecida_en` y `aplica_a`), que no
  forman parte del corredor: sale del borde superior de `Excepcion`, rodea a
  `Restriccion` por x = 78 y entra a `Obligacion` por abajo, con el rótulo al
  costado del último tramo.
- **El rótulo «acto regulado» pasa a la derecha** del borde superior de su
  zona (x = 604, con la zona alargada hacia arriba hasta y = 286): en la
  esquina izquierda lo atravesarían las tres bajadas.

## 4. Verificaciones ejecutadas (todas dentro del script; cualquier falla FRENA)

- 12 firmas y 6 tipos en la fuente importada; 17 pares en la expansión.
- Biyección exacta entre las rutas dibujadas y la expansión de la matriz,
  re-verificada sobre el marcado emitido vía los atributos `data-*`.
- Sin nombres internos en el texto visible del SVG: `sha`, `test`, `.py`,
  `.json`, `congelado`, `retocado` (por palabra completa).
- **Guarda geométrica de F1** (`verificar_geometria_f1`), sobre las
  coordenadas de los 40 trazos y los 19 textos de la figura (14 rótulos de
  relación, 4 líneas de rótulo de zona y la nota de `Sujeto`):
  1. **cruces**: los puntos donde una flecha toca o cruza otra tienen que ser
     EXACTAMENTE los 4 de `CRUCES_DECLARADOS` (§7), y ninguno puede tocar una
     de las seis flechas del corredor; uno de más o de menos frena;
  2. ningún trazo atraviesa una caja (llegar o salir por el borde no cuenta);
  3. **ningún texto** toca un trazo, una caja u otro texto, con el halo de
     1,75 px más 1 px de luz; el texto se mide con el avance de Menlo
     (0,602 em) y los anchos AFM de Helvetica;
  4. **«junto a su flecha», para los 14 rótulos de relación**: cada uno está a
     no más de 6 px de su flecha y la flecha ajena más cercana queda al menos
     5 px más lejos. En un peine (`establecida_en` desde la izquierda,
     `aplica_a`) la flecha del rótulo es el peine entero, dientes y tronco,
     porque el rótulo es uno solo.

En la versión 2 los controles 1, 3 y 4 cubrían solo el corredor y los rótulos
que esa versión colocaba; los otros textos se medían y se reportaban, sin
frenar.

Medido en esta corrida (salida del script):

| Rótulo | A su flecha | A la flecha ajena más cercana |
|---|---|---|
| `aplica_a` | 4,4 px | 33,9 px (peine de `establecida_en`) |
| `condiciona` | 4,6 px | 28,6 px (`regula` Obligacion) |
| `ejecuta` | 4,6 px | 140,6 px (`limita`) |
| `establecida_en` (peine izquierdo) | 3,4 px | 48,4 px (`requiere`) |
| `establecida_en` (desde Operacion) | 6,0 px | 71,6 px (`modificada_por`) |
| `exceptua` | 6,0 px | 44,2 px (`limita`) |
| `exceptua_obligacion` | 6,0 px | 16,6 px (`condiciona`) |
| `limita` | 4,6 px | 19,6 px (`prohibe`) |
| `modificada_por` | 6,0 px | 21,6 px (`referencia`) |
| `prohibe` | 4,6 px | 13,4 px (`limita`) |
| `referencia` | 6,0 px | 47,1 px (peine de `establecida_en`) |
| `regula` (Obligacion) | 4,4 px | 14,6 px (`requiere`) |
| `regula` (Restriccion) | 4,4 px | 21,4 px (`prohibe`) |
| `requiere` | 4,4 px | 25,6 px (peine de `establecida_en`) |

Para que el umbral de 6 px fuera el mismo de la versión 2 en toda la figura,
los rótulos que van al costado de un trazo vertical quedan a 6 px de él:
`exceptua` (antes a 8 px) y `exceptua_obligacion` (antes a 8 px), además de
los tres que la versión 3 recoloca.

**La guarda no es vacua.** Versión 2, sobre una copia del script en el
directorio de trabajo: devolver `exceptua_obligacion` a la ruta de la versión
1 frena con sus cruces contra `regula`, `prohibe` y `limita` de
`Restriccion`; bajar el rótulo `prohibe` sobre su línea, llevar `limita`
sobre la caja `Restriccion`, llevar `regula` (Restriccion) a un punto
equidistante entre su flecha y la de `prohibe` (7,9 / 7,9 px) o alejar
`condiciona` 22,6 px de su flecha frenan cada uno con su mensaje. Versión 3,
igual: devolver el rótulo `establecida_en` (desde Operacion) a su lugar de la
versión 2 frena porque toca la caja `Operacion` y su propio trazo; devolver
la línea de base de `aplica_a` a x = 60 frena porque toca su tronco; devolver
`modificada_por` a su posición de la versión 2 frena porque queda a 13,0 px
de su flecha y a 14,6 de `referencia`; alejar `referencia` 24 px de su línea
frena; y quitar un cruce de `CRUCES_DECLARADOS` frena con «sobran
[(78.0, 292.0)]».

## 5. Flechas contra la matriz, par por par

Contraste independiente del generador: un script de verificación que no se
versiona (queda en el paquete de revisión de esta versión, `contraste_f1.py`)
lee el SVG emitido y el TEXTO de `schema.py` con su número de línea
(`DOMAIN_RANGE` abre en `schema.py:167` y cierra en `schema.py:180`). El
conteo por relación se reproduce sin él con el comando de abajo.

| `schema.py` | Relación | Dominio → Rango | Flechas en el SVG |
|---|---|---|---|
| :168 | `establecida_en` | Excepcion → TextoOrdenado | 1 |
| :168 | `establecida_en` | Obligacion → TextoOrdenado | 1 |
| :168 | `establecida_en` | Operacion → TextoOrdenado | 1 |
| :168 | `establecida_en` | Restriccion → TextoOrdenado | 1 |
| :169 | `referencia` | TextoOrdenado → Comunicacion | 1 |
| :170 | `modificada_por` | TextoOrdenado → Comunicacion | 1 |
| :171 | `aplica_a` | Obligacion → Sujeto | 1 |
| :171 | `aplica_a` | Restriccion → Sujeto | 1 |
| :172 | `regula` | Obligacion → Operacion | 1 |
| :172 | `regula` | Restriccion → Operacion | 1 |
| :173 | `exceptua` | Excepcion → Restriccion | 1 |
| :174 | `exceptua_obligacion` | Excepcion → Obligacion | 1 |
| :175 | `prohibe` | Restriccion → Operacion | 1 |
| :176 | `limita` | Restriccion → Operacion | 1 |
| :177 | `ejecuta` | Sujeto → Operacion | 1 |
| :178 | `requiere` | Operacion → Obligacion | 1 |
| :179 | `condiciona` | Obligacion → Operacion | 1 |
| | **12 firmas** | | **17** |

Biyección exacta: 17 pares en `schema.py`, 17 elementos `<path>` con
`data-pred` en el SVG, cada par una sola vez. En el dibujo hay **14 puntas**
y **2 troncos**: los 3 dientes izquierdos de `establecida_en` comparten una
punta y los 2 de `aplica_a` otra (17 − 2 − 1 = 14). Recomputo rápido del
conteo por relación:
`python3 -c "import re; print(sorted(__import__('collections').Counter(re.findall(r'data-pred=\"([^\"]+)\"', open('docs/tesis/figuras/figura_esquema_partida.svg').read())).items()))"`

Cajas: **7** = 6 tipos de `ENTITY_TYPES` (`schema.py:24-31`) + pseudo-tipo
`Sujeto` (comentario de `DOMAIN_RANGE`, `schema.py:164-166`).

## 6. Fuente de cada dato de la figura

| Dato | Fuente |
|---|---|
| Las 6 cajas de tipo | `ENTITY_TYPES`, `schema.py:24-31` |
| La caja `Sujeto` (borde discontinuo) | pseudo-tipo del extremo sujeto de `aplica_a`/`ejecuta`, `schema.py:164-166` |
| Las 17 flechas | `DOMAIN_RANGE`, `schema.py:168-179` (una línea por firma, tabla del §5) |
| Rótulos de zona y nota de `Sujeto` | texto de la figura, no dato: describen el agrupamiento y la forma de elegir el sujeto |
| Paleta por tipo | heredada de `generar_figura_norma_a_grafo.py`; `Comunicacion` recibe `#6c584c`, declarado en el script |

## 7. Convenciones de dibujo (declaradas)

- **Una flecha por par (tipo del dominio → tipo del rango)** de cada
  relación. Cada par es un `<path>` propio del SVG con atributos
  `data-pred`/`data-dom`/`data-ran`, contable mecánicamente.
- **Troncos compartidos**: las flechas de una misma relación que comparten
  destino confluyen en un tronco con UNA punta y UN rótulo (`establecida_en`
  hacia `TextoOrdenado` desde la zona de la izquierda; `aplica_a` hacia
  `Sujeto`). El tramo de origen de cada flecha (el «diente») es el trazo
  propio de ese par. Las seis flechas del corredor no usan tronco: cada una
  lleva su punta y su rótulo.
- **Zonas**: «lo que la norma manda, prohíbe o exime» (`Obligacion`,
  `Restriccion`, `Excepcion`), en dos líneas; «acto regulado» (`Operacion`);
  «anclaje documental» (`TextoOrdenado`, `Comunicacion`).
- **Sujeto**: caja de borde discontinuo con la nota «se elige de un
  catálogo».
- **Rótulos** de relación en monoespaciada (equivalente de `\texttt`);
  identificadores del esquema tal cual, sin tilde, como en el código; el
  resto del texto en castellano, con tilde.
- **Cruces de línea**: 4 puntos, ninguno con una flecha del corredor,
  declarados en el script (`CRUCES_DECLARADOS`) con su causa y controlados
  por la guarda (§4). Recomputados también sobre el SVG por el contraste del
  §5:

  | Punto | Trazos |
  |---|---|
  | (64, 260) | tronco de `aplica_a` × diente `establecida_en` de Restriccion |
  | (64, 360) | tronco de `aplica_a` × diente `establecida_en` de Excepcion |
  | (78, 260) | `exceptua_obligacion` × diente `establecida_en` de Restriccion |
  | (78, 292) | `exceptua_obligacion` × diente `aplica_a` de Restriccion |

  Los dos primeros ya estaban en la versión 1; los dos últimos reemplazan a
  los 3 cruces de `exceptua_obligacion` con las diagonales del corredor. Total
  de la versión 1: 5. Ninguna flecha pasa por encima de una caja.

  **Por qué no se llega a cero con estas cajas.** Los dos peines salen por la
  izquierda de la columna, uno sube (`establecida_en`, hacia `TextoOrdenado`)
  y otro baja (`aplica_a`, hacia `Sujeto`); el tronco de `aplica_a` arranca
  en `Obligacion` y los dientes de `establecida_en` de `Restriccion` y de
  `Excepcion` nacen más abajo, así que tienen que cortarlo (o, con los
  troncos al revés, los dientes de `aplica_a` cortan el de `establecida_en`).
  Sacar uno de los peines por la derecha lo haría cruzar el corredor.
  `exceptua_obligacion` une una caja de abajo con una de arriba y tiene que
  pasar por un costado de `Restriccion`: por la derecha corta las tres
  flechas de `Restriccion` a `Operacion`, por la izquierda sus dos dientes.
  Bajar de 4 exigiría mover cajas, y con eso F1 dejaría de compartir
  posiciones con F1b.

## 8. Textos corregidos en la versión 3

En la versión 2 la guarda medía también los rótulos que esa versión no había
movido y reportaba tres que tocaban un trazo o una caja. La versión 3 los
corrige (`rotulos_f1` en el script):

| Rótulo | Defecto en la versión 2 | Corrección |
|---|---|---|
| `modificada_por` | a la izquierda de su línea (x = 785), lo atravesaba la de `referencia` (x = 700); el halo la interrumpía | las dos bajadas se separan (`referencia` en x = 636, `modificada_por` en x = 790) y cada rótulo va del lado de adentro de su propia línea, a 6 px, uno arriba del otro |
| `referencia` | asomaba 4,3 px fuera de la zona «anclaje documental» por la izquierda | queda dentro de la zona, a la derecha de su línea |
| `establecida_en` (desde Operacion) | el tramo horizontal (122 px) es más corto que el rótulo (126,4 px): la caja de texto se montaba 2,2 px sobre la esquina de `Operacion` y su último carácter pisaba el tramo vertical (x = 832) | pasa a la izquierda del tramo vertical, a 6 px, en la franja libre entre la zona documental (termina en y = 250) y la de acto regulado (empieza en y = 286) |
| `aplica_a` (rotado) | el texto llegaba al borde de su tronco (x = 64) y el halo lo pisaba | la línea de base pasa de x = 60 a x = 56: el texto queda a 4,4 px del tronco |

(El caso de `referencia` no lo detectaba la guarda, que no mide bordes de
zona; se resolvió con la misma recolocación.)

## 9. Composición y tamaño de letra impreso

| Magnitud | Valor |
|---|---|
| Ancho del SVG | 850 px |
| Alto del SVG | 590 px |
| PNG exportado | 1700 × 1180 px |

A 0,85`\linewidth` con 15 cm de ancho de texto: 0,85 × 15 cm × 28,3465 pt/cm
= **361,4 pt**, de modo que `N` px se imprimen a `N × 361,4 / 850` puntos:

| Elemento | Tamaño en el SVG | Tamaño impreso a 0,85\linewidth |
|---|---|---|
| Nombre de tipo (mono, bold) | 19 px | 8,08 pt |
| Rótulo de relación (mono) | 15 px | 6,38 pt |
| Rótulo de zona / nota de Sujeto | 15 px | 6,38 pt |

Sin cambios respecto de la versión 1: el lienzo y los cuerpos son los mismos.
