# figura_esquema_final — registro de generación

Figura de la sección 3.10: el esquema final con que se construye el grafo del
corpus, que es el esquema congelado más L-ESQ-R2 y su enmienda 2. Dibuja los 9
tipos de entidad más `Sujeto`, las 13 relaciones que emite el extractor con sus
28 firmas, `remite_a` (la relación que se deriva de las citas del texto) y la
marca de los 4 tipos con la propiedad `umbrales`. La figura presenta el esquema
final sin referirse al esquema de partida: todas las líneas y todos los
rótulos de relación van en gris, y cada caja lleva sus colores de tipo, que
otras figuras de la tesis leen de esta (§11).

Este LEEME describe la **versión 4**: la versión 3 sin la fila de la leyenda
«tipo o relación agregados respecto del esquema de partida», con los rótulos de
`condicion_de` y `remite_a` en el gris de los demás rótulos y con la leyenda de
`remite_a` nueva. Cajas (con sus colores de relleno y de borde), grupos,
trazado, cruces, rótulos y marcas no cambian. La versión 3 está en `8edd732`;
las versiones 1 y 2 (sin commit, reemplazadas) quedaron en el paquete de
revisión de cada una; el §8 detalla qué cambió en cada paso.

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
`rotulo_no_gris`, `rotulo_sobre_caja` y `tramo_diagonal`). Las siete corren
además en cada ejecución normal, antes de escribir (§6).

## 2. Fuentes y sellos

Fuentes que el script lee, con candado de sha256 (`FUENTES` en el script; sin
cambios desde la versión 3):

| Fuente | sha256 | Último commit que la tocó |
|---|---|---|
| `data/experiment/pyd_r2/generados/enums_r2.json` | `abd197ac8bbb818f680dc80d1b9c9df3e1f1f733fce3fd46b35e7440e7ce4241` | `eb277ce` |
| `scripts/remisiones.py` | `1da7464195875b1206ee9b1d1a15ac10f5976e5ce3700ccb230c7410bb9fde6d` | `92b45d6` |
| `data/experiment/grafo_v2/code/schema.py` (esquema de partida) | `cc98e4354cf2ad507954f7fa99f12b8445e6157c9a0bcb026a13908e63de7eab` | `fac503f` |
| `docs/tesis/figuras/figura_esquema_partida.svg` (figura de partida, v3) | `be98b797e3f6338818055cac12ed4308acb9a48df012177a923e45021f3b4a3a` | `c3bba5b` |

Los cuatro sha son los de la corrida (el script los comprueba antes de
dibujar). `remisiones.py` se ejecuta desde el texto verificado (`exec`), sin
importarlo; `schema.py` se lee con `ast`, sin ejecutarlo (importa pydantic).

Las 28 firmas de `enums_r2.json` son las de `FIRMAS_R2`
(`data/experiment/pyd_r2/code/modelos_r2.py:144`, armada por `_matriz_r2`,
`:136-141`, con `FIRMAS_CONGELADAS`, `:113`, y `AMPLIACION_R2`, `:130`):
`data/experiment/pyd_r2/code/generar_r2.py:42` escribe el JSON con
`enums_r2()`, que las toma de ese módulo (`modelos_r2.py:934`), y
`data/experiment/pyd_r2/generados/manifest_generados_r2.json` registra el
módulo (`:4-5`, sha256 `e67f15ae…`, el del archivo al 08/10/2026, HEAD
`4dba33f`; último commit, `4aa92c7`) y el JSON (`:18`, sha256 `abd197ac…`). El
contraste independiente del §8.1 lee `FIRMAS_R2` con `ast`, sin importar el
módulo, y da las mismas 28.

Documentos firmados que fijan el esquema final (no los lee el script; leídos en
el commit de la firma, regla k):

| Documento | Commit | sha256 en ese commit | Qué fija |
|---|---|---|---|
| `data/experiment/esq/laudo_esquema_congelado.md` | `2593d4d` | `64c5da88…` | 9 tipos y 13 predicados (líneas 106-107) |
| `data/experiment/esq/enmienda_L-ESQ-R2_2026-09-30.md` (L-ESQ-R2) | `4ef7650` | `66c4a1b9…` | umbrales en Restriccion, Obligacion, Condicion y Excepcion (§1.3 a, líneas 242-243); `condicion_de` → Operacion y → Potestad (§6.3, X1 opción ii, línea 787) |
| `data/experiment/esq/enmienda2_L-ESQ-R2_remite_a_2026-10-02.md` (enmienda 2) | `5f9a731` | `e779bd70…` | `remite_a`: origen en los 7 tipos de contenido (§2, líneas 63-64), destino en esos 7 o TextoOrdenado (líneas 65-68), 56 firmas (línea 73); la cita del texto del punto de origen como lo que la relación afirma (§1, líneas 54-55) |

Salidas de esta corrida (versión 4):

| Archivo | sha256 |
|---|---|
| `figura_esquema_final.svg` | `d550719599872f47fc8a7dbee261a6c11e5ab186e0e8fad76f281e3c220eedfa` |
| `figura_esquema_final.png` | `f703e515877c6f786ceb989c91f953852228860bc7b114d61c14bfc20a627a0b` |
| `figura_esquema_final.pdf` | `9ce68dc1c178721bc19bcb96119098715a0499700d4cf2b43ca4376ddf331cd4` |
| `generar_figura_esquema_final.py` (script, versionado junto a la figura) | `4ab76a71dae84f29f246b1ee5b27af5b143565a78d62962918335aa3ca1a086d` |

Versiones reemplazadas: la 3 (`8edd732`), SVG `dfdb16d4…`, PNG `cfc5cc61…`,
PDF `e9b6650f…`, script `0d6274fe…`; la 2, SVG `30d6682c…`, PNG `fa0d92d3…`,
PDF `bdfc1880…`, script `50b8e714…`; la 1, SVG `658e7c2f…`, PNG `abb01c41…`,
PDF `7d1c4bd9…`, script `9c6deec8…`.

Recomputo: `shasum -a 256 docs/tesis/figuras/figura_esquema_final.{svg,png,pdf}`.
Determinismo: corridas con `PYTHONHASHSEED` 1, 2 y 3 dan los mismos tres sha;
el PDF se fija con `SOURCE_DATE_EPOCH=0`.

## 3. Fuente de cada dato de la figura

| Dato | Fuente |
|---|---|
| Las 9 cajas de tipo | `enums_r2.json:8` (`tipo_entidad`) |
| La caja `Sujeto` | extremo de `aplica_a` y `ejecuta`: `enums_r2.json:34` (`predicados_sujeto`) y los rangos de `firmas_r2` |
| Las 13 relaciones del extractor | `enums_r2.json:19` (`predicado`) |
| Sus 28 firmas | `enums_r2.json:169` (`firmas_r2`), que son las de `FIRMAS_R2` (§2); el script asserta que son las 26 de `firmas_congeladas` (`:38`) más las 2 de `ampliacion_r2` (`:157`) |
| `remite_a` y sus 56 firmas | `scripts/remisiones.py:16` (`PREDICADO_REMISION`), `:21` (`TIPOS_CONTENIDO`), `:22` (`TIPO_TEXTO_ORDENADO`) y `:41-44` (`firma_remite_a_ok`, evaluada sobre los 10 × 10 pares de tipos y Sujeto) |
| Los 7 tipos que nombra la leyenda de `remite_a` | los mismos `TIPOS_CONTENIDO` (`remisiones.py:21`), en el orden en que aparecen en la figura (grupo de la izquierda de arriba abajo, luego Operacion y Definicion); el script asserta que coinciden con el dominio de `establecida_en` en `firmas_r2` |
| Texto de la leyenda de `remite_a` («se deriva de las citas del texto», «o hacia un Texto Ordenado») | texto de la figura (`LEYENDA_REMITE_ANTES` y `LEYENDA_REMITE_DESPUES` en el script), que dice lo de la enmienda 2 (§2): la relación sale de la cita del texto del punto de origen y su destino es un tipo de contenido o TextoOrdenado |
| La marca de umbrales | `enums_r2.json:340` (`tipos_con_umbrales`), cotejada con `claves_por_tipo` (`:290`) |
| Qué cajas llevan `#b5179e` (Potestad, Condicion, Definicion) | los tipos de `enums_r2.json:8` que no están en `ENTITY_TYPES` (`schema.py:24-31`); la figura no lo dice; sin cambios desde la versión 3 |
| Tamaño y estilo de las 7 cajas y de los grupos de la partida, nota de Sujeto, paleta, tipografía y cuerpos de letra | `figura_esquema_partida.svg` (`c3bba5b`), leído elemento por elemento |
| Los 24 tramos conservados de la partida (10 firmas, §8) | los `<path>` de `figura_esquema_partida.svg`, trasladados con sus cajas |
| Colores de las cajas de Potestad, Condicion y Definicion (`#b5179e`, borde de 2,6 px y relleno al 90 % de blanco) | el de la figura del esquema congelado: `generar_figuras_esquema.py:147` (`RESALTE`) y `:161` (`ANCHO_RESALTE`); sin cambios desde la versión 3 |
| Gris y grosor de todas las líneas de relación y sus puntas (`#8a8a8a`, 1,6 px) | los de los `<path>` de `figura_esquema_partida.svg` |
| Gris de todos los rótulos de relación (`#6f6f6f`) | el de los rótulos de `figura_esquema_partida.svg` (sus 14 rótulos con halo y sus 5 textos en cursiva llevan `fill="#6f6f6f"`) |
| Rótulos de los grupos nuevos, demás textos de la leyenda y marca «≤» | texto de la figura, no dato |
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

Suma: 5 + 2 + 5 + 5 + 2 + 9 = 28. El script imprime además las 11 firmas que
no están en el esquema de partida (17 + 11 = 28); la figura no las distingue.

Para `remite_a`, el control exige que la red discontinua salga del borde del
grupo de la izquierda, vuelva a él y llegue a TextoOrdenado; que la leyenda
nombre exactamente los tipos de contenido del código; y que los tipos del
grupo de la izquierda estén entre ellos. Las firmas que la figura afirma son
entonces 7 × (7 + 1) = 56, las del código y las de la enmienda 2 (§8.1).

El SVG emitido se relee: sus atributos `data-firmas` dan las mismas 28; el de
`remite_a` da «grupo>grupo» y «grupo>TextoOrdenado»; cada grupo declara sus
cajas (`data-grupo`, `data-cajas`); la leyenda declara y nombra los 7 tipos
(`data-tipos` y sus nombres en monoespaciada); las marcas, los 4 tipos con
umbrales (`data-umbrales`); y ningún texto visible dice «partida» ni
«agregad» (versión 4).

## 5. Cruces

**6 cruces**, los mismos de las versiones 2 y 3, todos en X entre flechas de
redes distintas y exactamente los de `CRUCES_DECLARADOS`:

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
4. **Textos** (41): ningún texto toca un trazo, una punta, una caja, el borde
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
6. **Colores**, sobre el SVG que se emitiría: las 75 líneas de relación, las
   21 puntas y los 17 rótulos de relación, en el gris de la partida (líneas y
   puntas `#8a8a8a`, 1,6 px; rótulos `#6f6f6f`); cajas con `#b5179e` solo
   Potestad, Condicion y Definicion, como en la versión 3.

Cercanía medida de los 17 rótulos (salida del script; la misma de la versión
3):

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
| `rotulo_no_gris`: el rótulo de `remite_a` en magenta (versión 4) | `[colores] el rótulo «remite_a» va en #b5179e, no en #6f6f6f` |

Por línea de comandos (`--mutacion`), las siete terminan con código 1 y no
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
- **Líneas y rótulos**: todas las líneas de relación, sus puntas y sus
  rótulos van en el gris de la figura de partida, también los de
  `condicion_de` y `remite_a`. Cada línea se sigue por su trazado y su rótulo,
  como en la figura de partida. `condicion_de` lleva dos rótulos: abajo, junto
  al tramo que rodea la columna, y junto a su tramo vertical, a la derecha del
  grupo de la izquierda.
- **Colores de las cajas**: cada caja lleva su color de tipo. Potestad,
  Condicion y Definicion van con `#b5179e` (borde de 2,6 px y fondo al 90 % de
  blanco), como en la versión 3 y como las leen otras figuras de la tesis
  (§11); la figura no explica el color en la leyenda.
- **Discontinuo**, en gris: `remite_a`. Se dibuja una sola vez, en la franja
  entre el tramo superior de `establecida_en` y el borde superior del grupo
  de la izquierda: un lazo que sale del grupo y vuelve a él, y una flecha
  hacia TextoOrdenado, con un solo rótulo. La leyenda dice que se deriva de
  las citas del texto y que vale entre cualquier par de los 7 tipos de
  contenido, que nombra en monoespaciada, o hacia un Texto Ordenado.
- **Marca de umbrales**: un cuadro oscuro con «≤» en el extremo derecho de la
  caja, igual en los 4 tipos, explicado en la leyenda (sin cambios desde la
  versión 1).
- **Sujeto**: borde discontinuo y la nota «se elige de un catálogo», como en la
  partida. Las relaciones de pertenencia del catálogo no se dibujan.
- **Leyenda**, con 2 entradas: la línea discontinua gris, con el texto de
  `remite_a` en tres líneas (la segunda nombra los 7 tipos); y la marca «≤» de
  los umbrales.

## 8. Qué cambió en cada versión

### 8.1 De la versión 3 a la 4

| Elemento | Versión 3 | Versión 4 |
|---|---|---|
| Leyenda, fila de lo agregado | caja y rótulo de ejemplo («relación») en magenta, «tipo o relación agregados respecto del esquema de partida» (y = 768) | eliminada |
| Rótulos de `condicion_de` (dos) y de `remite_a` | `#b5179e` | `#6f6f6f`, el gris de los demás rótulos |
| Líneas y puntas de relación | gris `#8a8a8a`, 1,6 px | sin cambios (ya iban en gris) |
| Leyenda de `remite_a` | «la deriva el código y vale entre cualquier par de los 7 tipos de contenido,» y los 7 tipos, en dos líneas (y = 794) | «se deriva de las citas del texto y vale entre cualquier par de los 7 tipos de contenido,», los 7 tipos y «o hacia un Texto Ordenado», en tres líneas (y = 768, el lugar de la fila eliminada) |
| Fila de umbrales | y = 838 | y = 830, a 21 px de la última línea de `remite_a`, como en la versión 3 |
| Cajas, con sus colores de relleno y de borde | — | sin cambios |
| Lienzo e impresión | 850 × 860; 15,00 × 15,18 cm | 850 × 852; 15,00 × 15,035 cm (sale una fila de 26 px y la de `remite_a` suma una línea de 18 px) |
| Textos | 42 | 41 |
| Controles | colores: rótulos en magenta solo los de las relaciones nuevas; 6 pruebas negativas | colores: todos los rótulos en gris; la relectura frena si un texto visible dice «partida» o «agregad»; + prueba `rotulo_no_gris` (7) |

Contraste independiente (`verificar_v4_contra_v3_FIG-ESQUEMA-FINAL-SOLO.py`,
script del paquete de revisión de esta versión, que no importa el generador;
34 controles en verde). El paquete tiene copia permanente fuera del repo, en
`fuera_del_repo/scratchpads/0d38ab0c-d027-43fc-94f1-1d61fb80c00e/scratchpad/reports/verificaciones_tesis/FIG-ESQUEMA-FINAL-SOLO/`
(carpeta `INGENIERIA IA/TESIS/`, junto al repo):

- las 28 firmas de `FIRMAS_R2` (`modelos_r2.py:144`, leída con `ast`) son las
  de `firmas_r2` de `enums_r2.json` y las de los `data-firmas` del SVG, en la
  versión 4 y en la 3;
- la firma de `remite_a` de la enmienda 2, leída en `5f9a731` (sha256
  `e779bd70…`; origen en las líneas 63-64, destino en las 65-68, «Son 56
  firmas» en la 73), es la que dibuja la figura en la versión 4 y en la 3: los
  7 tipos de la leyenda × (esos 7 y TextoOrdenado) = 56;
- los 75 trazos (mismo `d`, color, relación y firmas), las 21 puntas, las 10
  cajas (mismo relleno, borde y grosor), sus 10 nombres, los 4 grupos y sus 5
  rótulos, la nota de Sujeto y las 4 marcas de umbrales son idénticos y van en
  el mismo orden; el fondo cambia solo de alto (860 → 852);
- los 17 rótulos tienen el mismo texto, lugar, letra, halo y orden; cambia
  solo el color de 3 (`condicion_de` en (98, 738) y en (316,5, 625), y
  `remite_a` en (430, 117)), de `#b5179e` a `#6f6f6f`;
- 6 cruces, los mismos de la versión 3;
- ningún texto visible de la versión 4 dice «partida», «agregad», «deriva el
  código» ni «magenta» (la versión 3 decía los tres primeros);
- lo que leen de la figura los generadores del §11 (lógica de
  `leer_colores_tipo`, `leer_estilo` y `leer_estilo_nuevo`, replicada) es
  igual en la versión 4 y en la 3.

### 8.2 De la versión 2 a la 3

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

### 8.3 De la versión 1 a la 2

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
| Lienzo | 850 × 852 |
| Impresa | 15,00 × 15,035 cm (SVG con `width="15cm"` y `height="15.035cm"`) |
| PNG | 1772 × 1777 px, 300 dpi grabados en el bloque pHYs |
| PDF | 425,20 × 426,19 pt = 15,00 × 15,035 cm |

A 15 cm, un píxel del lienzo mide 425,2 / 850 = 0,50 pt:

| Elemento | En el lienzo | Impreso |
|---|---|---|
| Nombre de tipo (Menlo, negrita) | 19 px | 9,50 pt |
| Rótulos de relación, de grupo, nota, leyenda y marca | 15 px | 7,50 pt |

El lienzo tiene el ancho de la figura de partida (850 px), así que la escala a
15 cm es la de la partida a 15 cm.

## 10. Epígrafe propuesto

Tipos de entidad y relaciones del esquema final con que se construye el grafo
del corpus. Las relaciones que salen de varios tipos o llegan a varios se
dibujan con un tramo común. El grupo de la izquierda reúne lo que la norma
manda, prohíbe, exime o permite, y cuándo, y Definicion forma el grupo de lo
que la norma define. La línea discontinua marca remite_a, que se deriva de las
citas del texto y vale entre cualquier par de los siete tipos de contenido o
hacia un Texto Ordenado; la marca ≤ señala los tipos que llevan la propiedad
umbrales, y el borde discontinuo de Sujeto indica que se elige de un catálogo.

## 11. Figuras que leen esta como estilo

Seis generadores toman de `figura_esquema_final.svg` los colores de tipo y
otros rasgos de estilo, con candado de sha256 sobre el SVG:

| Generador | Cómo lo lee | Qué lee |
|---|---|---|
| `generar_figura_norma_a_grafo.py` | `ESTILO` (`:118-119`), `leer_con_candado` (`:122-129`) | `leer_colores_tipo` (`:480-491`): relleno, borde y grosor de cada caja |
| `generar_figura_tripleta.py` | `ESTILO = base.ESTILO` (`:107`) | ídem, por `base.leer_colores_tipo` (`:268`) |
| `generar_figura_proceso_extraccion.py` | `base.ESTILO` (`:645`) | ídem (`:643`) |
| `generar_figura_fragmentos_vs_grafo.py` | `base.ESTILO` (`:686`) | ídem (`:675`) |
| `generar_figura_extractor_ejemplo.py` | `ESTILO` (`:127-128`), `leer_con_candado` (`:223-230`); importa este script (`:107`) | `leer_estilo` (`:233-267`): cajas, letra de los nombres, rótulos que no van en `#b5179e`, gris de líneas y puntas |
| `generar_figura_ensamblado_ejemplo.py` | `EX.ESTILO` (`:282`); importa este script (`:116`) | `leer_estilo_nuevo` (`:279-305`): discontinuo de `remite_a` y marca de umbrales |

Lo que leen es igual en la versión 4 y en la 3 (§8.1). Junto con esta
versión, los dos candados (`generar_figura_norma_a_grafo.py:119` y
`generar_figura_extractor_ejemplo.py:128`) pasan del sha de la versión 3
(`dfdb16d4…`) al de la 4 (`d5507195…`). En el mismo cambio,
`extractor_ejemplo` y `ensamblado_ejemplo` dejan de llamar a
`proc.medidor()` (`:861` y `:867`), que fallaba desde que `88bfe89` pasó esa
función a `generar_figura_norma_a_grafo.py:806`, y la llaman en ese lugar
(`base.medidor()`, con `generar_figura_norma_a_grafo.py` importado en `:108`
y `:118`). Sobre una copia del árbol con todos esos cambios, sin otros
arreglos, este generador da la versión 4 y los seis dan sus figuras idénticas
byte a byte a las commiteadas (SVG, PNG y PDF). Los LEEME de las cuatro
figuras que nombran el SVG o los scripts cambiados lo registran en una nota
del 08/10/2026. La prueba está en el paquete de revisión de esta versión
(`prueba_ajuste1_FIG-ESQUEMA-FINAL-SOLO.zsh`, con su resumen y sus
registros).
