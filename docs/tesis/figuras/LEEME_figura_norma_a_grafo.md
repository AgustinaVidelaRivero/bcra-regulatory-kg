# figura_norma_a_grafo — registro de generación (Figura 1.1), versión 2

Figura «de la norma al grafo» para la Introducción, con el ejemplo del
préstamo: el punto 5.1.1.1 del Texto Ordenado de Clasificación de deudores,
que remite al punto 3.7 («importe de referencia»).

- Arriba, «En el texto», **igual que en la versión 1**: en gris, la frase de la
  unidad 5.1.1 que encabeza la lista de excepciones; debajo y con sangría, el
  punto 5.1.1.1 completo, con resaltada la frase «dos veces el importe de
  referencia establecido en el punto 3.7.»; una línea «[…]»; y el punto 3.7.
- Abajo, «En el grafo», lo que el grafo de la tanda 0 con el perfil r2b tiene
  de esos dos puntos: la `Operacion` de la inclusión en la cartera comercial,
  las dos `Condicion` del 5.1.1.1 con su `condicion_de` hacia ella y la
  `Definicion` del importe de referencia del 3.7, con las dos `remite_a`
  (desde la `Condicion` del monto y desde la `Operacion`) resaltadas. Cada
  nodo lleva su tipo, su punto y su etiqueta tal como está en el grafo. Sin la
  `Excepcion` y sin sujeto (§6).
- Al pie, la leyenda de las dos clases de arista.

Tamaño impreso: **15,00 × 16,34 cm** (lienzo 860 × 937). Cruces entre
aristas: **0**.

## Versiones

- **Versión 1** (28/09/2026, U-FIG-EJEMPLO y U-FIG-EJEMPLO-AJUSTE): generador,
  SVG y PNG en `fbe69d4`; este LEEME, en `e6e6021`. Sobre KG-Reextraído-r1
  (`data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json`, sha256
  `0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a`): cinco
  nodos (dos `Restriccion` con `limita` hacia la `Operacion`, la `Obligacion`
  del 3.7 con `referencia` y un `Sujeto`) y cuatro aristas; leía todo de
  `ejemplo_prestamo_datos.json`. sha256 en `fbe69d4`: generador
  `9b0e45a299a0a078d250ccc999d192cbb83038bd8c00baa6bd8972d021b73f3d`, SVG
  `d43f7247d2c06bda27dd64f1d34fcd3ec56401b511b7cfa60a7817ef3940e251`, PNG
  `7d26338468810ebc4b1c88f98dcc6cd616f62fe8b0b8cb3137bffb56619dc65c`
  (`git show fbe69d4:docs/tesis/figuras/<archivo> | shasum -a 256`).
- **Versión 2** (07/10/2026, FIG-INTRO-R2B). Qué cambió:
  - **el grafo**: KG-Tanda0-Desarrollo-r2b (§2), y el script comprueba que lo
    dibujado está igual en KG-Tanda0-Diez-r2b;
  - **el panel del grafo**: los nodos y las aristas de arriba; la arista
    resaltada pasa de `referencia` a `remite_a`;
  - **los nodos**: primera línea en negrita con «Tipo · punto N» y debajo la
    etiqueta (en la versión 1, el número de punto y la etiqueta; el tipo solo
    por el color);
  - **los colores de tipo**: los de la figura del esquema final (§7);
  - **la leyenda**: solo las dos clases de arista (§7);
  - **las fuentes**: el generador lee el grafo, la segmentación y el estilo
    con candado de sha256, y compara los textos con los de la versión 1
    (`ejemplo_prestamo_datos.json` queda solo como referencia de esa
    comparación);
  - **las salidas**: el SVG declara su tamaño en cm (15 cm de ancho), el PNG
    sale a 300 dpi con la densidad grabada (en la versión 1, `rsvg-convert -z
    2`, 1720 px) y se agrega el PDF;
  - **los controles**: inventario, geometría y pruebas negativas (§8 y §9).
  El panel del texto, el trazado del panel del grafo (dos columnas y filas,
  tamaños de caja, separaciones) y la paleta de acento y grises no cambian.

## 1. Comando

```
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_norma_a_grafo.py
```

Escribe `figura_norma_a_grafo.svg`, `.png` y `.pdf` en `docs/tesis/figuras/`
(`--salida DIR` para otro directorio). Herramientas: `rsvg-convert` 2.62.3
(lo informa el generador al terminar), PIL 12.3.0 de `.venv` y
`/System/Library/Fonts/Helvetica.ttc` para medir los textos; sin red ni API.
Con `--perturbar <caso>` compone la figura con un defecto (§9) y no escribe
nada.

## 2. Fuentes

Cada una con candado de sha256 en el generador
(`generar_figura_norma_a_grafo.py:105-119`); si una no coincide, frena.

| Papel | Archivo | sha256 | Ancla |
|---|---|---|---|
| grafo dibujado | `data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo_r2b/r2/kg.json` | `6e7560433148cfe0c476cdd61199c32278187c4196d6f90dc0a38976a6d8e9a2` | último commit `bbc38dc`; registro KG-Tanda0-Desarrollo-r2b, 6.990 nodos y 23.445 aristas (`data/experiment/neo4j/grafos.py:120-133`) |
| grafo de comprobación | `data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2b/r2/kg.json` | `a9631a64b422bdae634fb05135373c6f04c6272cdf7acd43a1be9f5b6c1f5f57` | último commit `bbc38dc`; registro KG-Tanda0-Diez-r2b, 8.816 nodos y 27.632 aristas (`grafos.py:134-147`) |
| textos | `data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b/chunks_cla.json` | `98808886a406d8321c678836a55f92eea983d594d95358dd21ceb537487ac0b1` | único commit `9f6361e` (`git log --format=%h -- <ruta>`) |
| textos de la versión 1 | `docs/tesis/figuras/ejemplo_prestamo_datos.json` | `25ab7b4c0d76fd735244fe0fecc17ceaba1b0e8bfd2312e7aa3cbd5c849672a2` | `fbe69d4` |
| composición de los textos | `docs/tesis/figuras/extraer_datos_ejemplo_prestamo.py` | `4c3a441972d27304b6d58d0664dbc15b893bce7ad3e7d2d49afad947f51eeea7` | `fbe69d4`; se importan `texto_de_figura` (:117-124), `PUNTOS_TEXTO`, `INTRO_5_1_1`, `FRASE_5_1_1` y `FRASE_RESALTADA` (:66-70), sin modificarlos |
| colores de tipo | `docs/tesis/figuras/figura_esquema_final.svg` | `dfdb16d471bb93c6351aa03b1e609452b75c428baa354c52354ce1dfe9797bb3` | `8edd732`; cajas `data-caja` en :110, :112 y :118 |

Los dos grafos tienen los mismos ids, tipos, etiquetas, puntos y propiedades
en los cuatro nodos dibujados, las mismas cuatro aristas con las mismas
propiedades y la misma `Excepcion` sin dibujar con la misma arista
(`comparar_grafos`, `generar_figura_norma_a_grafo.py:462-477`). Cambian los
índices de las aristas en `kg['edges']` (§5).

## 3. Textos

Del campo `texto` de los fragmentos de
`salida_tanda0_r2b/chunks_cla.json`, compuestos como en la versión 1 (cortes
de línea quitados, «pro-ductiva» reunida en «productiva» en el 5.1.1.1; la
frase de 5.1.1, con el encabezado heredado «5.1.1. Cartera comercial.» y el
texto de `cla::5.1.1::intro`). El generador comprueba que los tres textos y la
frase resaltada son, carácter por carácter, los de la versión 1
(`cargar_textos`, `generar_figura_norma_a_grafo.py:342-377`).

El archivo es el mismo, byte a byte, que leía la versión 1:
`shasum -a 256 data/experiment/reextraccion_v2/e0_chunking/salida_enm01/chunks_cla.json data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b/chunks_cla.json`
da `98808886…` para los dos.

En el SVG, las 15 líneas del panel «En el texto» (de su título al título «En
el grafo») son las de la versión 1 (`git show fbe69d4:docs/tesis/figuras/figura_norma_a_grafo.svg`):
sha256 de las 15 líneas `7c81f5e0e1008a7d8900aa316c798821d7d7a64dcc7dea32edae59d7b1a9037b`
en las dos versiones (comparación hecha en FIG-INTRO-R2B, fuera del repositorio).

## 4. Nodos dibujados (4)

Declarados en `NODOS` (`generar_figura_norma_a_grafo.py:157-162`) por tipo,
chunk y etiqueta; el script frena si no hay exactamente uno o si su única
procedencia `punto_propio` no es ese chunk.

| Clave | Tipo | Punto | Etiqueta en el grafo | id |
|---|---|---|---|---|
| condicion_monto | Condicion | 5.1.1.1 | Superar dos veces importe referencia punto 3.7 | `Condicion_superar_dos_veces_importe_referencia_punto_3_7__el_credito_debe_superar_el_equiv_22a312` |
| operacion | Operacion | 5.1.1.1 | Inclusión en cartera comercial — créditos consumo/vivienda | `Operacion_inclusion_en_cartera_comercial_creditos_consumo_vivienda__cla_5_1_1_1_8f5956` |
| condicion_repago | Condicion | 5.1.1.1 | Repago vinculado a actividad productiva/comercial | `Condicion_repago_vinculado_a_actividad_productiva_comercial__el_repago_del_credito_no_debe_0856b5` |
| definicion_3_7 | Definicion | 3.7 | Importe de referencia — nivel máximo de ventas anuales | `Definicion_importe_de_referencia_nivel_maximo_de_ventas_anuales__el_nivel_maximo_del_valor__a855af` |

Etiquetas completas, sin abreviar, envueltas a 40 caracteres por línea como
máximo (`MAX_ETIQUETA`, :192). Tipos escritos como en el código, sin tildes.

## 5. Aristas dibujadas (4)

Declaradas en `ARISTAS` (:164-169); cada una existe una sola vez en los dos
grafos y, entre los cuatro nodos, el grafo no tiene otras
(`cargar_subgrafo`, :398-459).

| `kg['edges']` desarrollo / diez | Origen | Relación | Destino | En la figura |
|---|---|---|---|---|
| 5542 / 6181 | condicion_monto | `remite_a` | definicion_3_7 | resaltada; `properties` `alcance` `interna`, `destino` `cla::3.7` |
| 5540 / 6179 | condicion_monto | `condicion_de` | operacion | gris discontinua |
| 5161 / 5771 | condicion_repago | `condicion_de` | operacion | gris discontinua |
| 17765 / 21013 | operacion | `remite_a` | definicion_3_7 | resaltada; mismas `properties` |

Las cuatro tienen como procedencia `cla::5.1.1.1`. `remite_a` es un predicado
que deriva el código del ensamblado, no el extractor
(`data/experiment/pyd_r2/code/modelos_r2.py:165`, `PREDICADOS_DERIVADOS`; la
llamada, en `git show bbc38dc:data/experiment/tanda0/code/ensamblar_tanda0.py`,
línea 1272).

## 6. Lo que no se dibuja

Lo cuenta el generador en cada corrida (salida «NO DIBUJADO»):

- **La `Excepcion` del 5.1.1.1** («Excepción cartera comercial — créditos
  consumo/vivienda»): en los dos grafos su única arista es su
  `establecida_en` hacia el Texto Ordenado. La `exceptua` hacia la
  `Operacion` que devolvió el extractor la rechazó el validador por firma
  (`docs/tesis/figuras/LEEME_figura_extractor_ejemplo.md:107-111`, commit
  `04df086`; la matriz admite `exceptua` solo hacia `Restriccion`,
  `modelos_r2.py:120`). Es el caso de las excepciones sin unir del hallazgo
  (a) de VERIF-CAP3-COHERENCIA (verificación de solo lectura del
  07/10/2026; su paquete no está en el repositorio). `NO_DIBUJADOS` (:172)
  la declara y el script frena si los nodos de la unidad que no se dibujan
  son otros.
- **Sujeto**: el 5.1.1.1 no tiene nodo de sujeto en el grafo (el único nodo
  de la unidad que no se dibuja es la `Excepcion`).
- **Las `establecida_en`**: cuatro, una de cada nodo dibujado hacia el Texto
  Ordenado.
- **Las otras `remite_a` que llegan a la `Definicion` del 3.7**: 32, desde
  12 `Condicion`, 7 `Obligacion`, 6 `Operacion`, 2 `Excepcion`, 2 `Potestad`,
  2 `Restriccion` y 1 `Definicion` (grafo de desarrollo).
- **El umbral de la `Condicion` del monto** (`valor` 2, `unidad` veces,
  `comparacion` `minimo_estricto`, `base` «importe de referencia establecido
  en el punto 3.7»): lo dibuja la figura del ensamblado (sección 4.5).

## 7. Colores, composición y tamaño

Colores de tipo, leídos de `figura_esquema_final.svg` (`leer_colores_tipo`,
:480-491):

| Tipo | Relleno | Borde | Grosor | Línea del SVG |
|---|---|---|---|---|
| Condicion | `#f8e8f5` | `#b5179e` | 2.6 | :110 |
| Definicion | `#f8e8f5` | `#b5179e` | 2.6 | :112 |
| Operacion | `#eaefee` | `#52796f` | 2 | :118 |

En la figura del esquema final, `Condicion` y `Definicion` comparten el
estilo (son dos de los tipos agregados respecto del esquema de partida, en
magenta). Acá se distinguen por el tipo escrito en cada nodo, y por eso la
leyenda ya no lleva la fila «Tipo de nodo» (dos muestras iguales con dos
nombres distintos); queda la de «Tipo de arista», con los mismos textos que
en la versión 1. Texto de los nodos en `#1f1f1f`.

- Panel del grafo en dos columnas y tres filas (`DISPOSICION`, :178-183): la
  `Condicion` del monto y la `Definicion` del 3.7 arriba, unidas por la
  `remite_a` horizontal; la `Operacion` en el medio de la columna izquierda,
  con las dos `condicion_de` verticales; la `Condicion` del repago abajo. La
  `remite_a` de la `Operacion` sale por su costado derecho, sigue en
  horizontal hasta la vertical de la `Definicion` y sube hasta su borde
  inferior (`RUTAS`, :185-190; `ruta_arista`, :706-729).
- Columnas, anchos de caja, separación entre filas, márgenes y paleta de
  acento y grises: los de la versión 1.
- Tamaño: lienzo 860 × 937 → **15,00 × 16,34 cm** (versión 1: 860 × 973 →
  15,00 × 16,97 cm). PNG 1772 × 1931 px a 300 dpi; PDF 425,2 × 463,3 pt.
- Letra impresa a 15 cm: texto de los recuadros 17 → 8,41 pt (mínimo 8, como
  en la versión 1); nodos 15 → 7,42 pt; rótulos de arista y leyenda 13 →
  6,43 pt. Los mismos tamaños que la versión 1.

## 8. Controles

Extracto de la salida de la corrida que escribió las salidas de §11:

```
PRUEBAS NEGATIVAS: 4 de 4 hacen fallar su control
INVENTARIO (releído del SVG): 4 nodos y 4 aristas; fallas: 0
  arista Condicion 5.1.1.1 --remite_a--> Definicion 3.7
  arista Condicion 5.1.1.1 --condicion_de--> Operacion 5.1.1.1
  arista Condicion 5.1.1.1 --condicion_de--> Operacion 5.1.1.1
  arista Operacion 5.1.1.1 --remite_a--> Definicion 3.7
GEOMETRÍA: 31 textos, 4 cajas, 6 trazos con flecha; cruces 0; fallas: 0
TAMAÑO: lienzo 860 x 937.0, impreso a 15.00 x 16.34 cm
```

- **Inventario** (`inventario_svg` y `controlar_inventario`, :988-1043): solo
  desde el SVG, cada caja de nodo con su encabezado y su etiqueta, y cada
  trazo con la caja en cuyo borde empieza, la caja en cuyo borde termina y su
  rótulo; tiene que dar exactamente los cuatro nodos y las cuatro aristas del
  grafo.
- **Geometría** (`controlar_geometria`, :929-982, que usan también las
  figuras 1.2 y 1.3): textos medidos con las métricas reales de Helvetica;
  ningún texto superpuesto con otro, sobre una caja que no lo contiene, sobre
  un trazo que no es el suyo ni fuera del lienzo; ningún trazo que atraviese
  una caja; **0 cruces entre trazos** (los seis con flecha: cuatro aristas y
  dos de la leyenda).
- Verificación geométrica de la versión 1, con
  `docs/tesis/figuras/verificar_geometria_svg.py` (archivo no rastreado,
  sha256 `fd8d062df7b7529131f466df628298e02dd079517aa66624caeea6a8b722df19`):
  31 textos, 4 nodos, 6 trazos con flecha; fallas: 0.

## 9. Pruebas negativas

Corren antes de componer (`PRUEBAS_NEGATIVAS`, :1109-1112); cada una tiene
que hacer fallar su control con su propia falla:

```
arista_de_mas -> inventario: arista de la figura que no está en el grafo: (('Condicion', '5.1.1.1', 'Repago vinculado a actividad productiva/comercial'), 'remite_a', ('Operacion', ...)) (fallan también: geometria)
etiqueta_distinta -> inventario: nodo de la figura que no está en el grafo: ('Operacion', '5.1.1.1', 'Inclusión en cartera comercial — créditos de consumo o vivienda')
cruce -> geometria: 2 cruce(s) entre trazos, declarados 0: [('1', '4'), ('2', '4')] (fallan también: inventario)
rotulo_sobre_caja -> geometria: texto sobre la caja operacion: 'limita' (fallan también: inventario)
```

Con `--perturbar <caso>`, sobre una copia, los cuatro terminan con «FALLA:
la figura tiene defectos; no se escribe nada», código 1 y ningún archivo
escrito. Con `chunks_cla.json` o `figura_esquema_final.svg` alterados en una
copia, el generador frena por el candado, código 1.

## 10. Reproducibilidad

Tres corridas sobre una copia de las fuentes (copiadas, sin enlaces), con
`PYTHONHASHSEED` 0, 1 y 4242: el mismo SVG, el mismo PNG, el mismo PDF y la
misma salida de texto. El PDF lleva `/CreationDate` fijada por
`SOURCE_DATE_EPOCH=0` (:220).

## 11. Salidas (versión 2)

| Archivo | sha256 |
|---|---|
| `generar_figura_norma_a_grafo.py` | `89dfc2a3d85e2abe1a28b3517d3e6817d73af8feb5b4b37ee4fb73978b5e3298` |
| `figura_norma_a_grafo.svg` | `874292f54e3c5d70b036b070b6beb7e8ce4c568a2aa6862fde23d865588f3e9b` |
| `figura_norma_a_grafo.png` | `8dbfb2da6e528f9b8076cba527ed5ada49c02669a4055f62db60f0799f5c1148` |
| `figura_norma_a_grafo.pdf` | `c27cfbdee26f2441af770619d5ef237cb25f23423d6238bea35a2dbde9b7054f` |

## 12. Observaciones

- **Procedencia de las `remite_a`**: en los dos grafos, el `tramo` de la
  procedencia de las dos `remite_a` es el del repago («cuyo repago no se
  encuentre vinculado a ingresos fijos o periódicos del cliente sino a la
  evolución de su actividad productiva o comercial»), mientras su
  `evidencia` es el pasaje de la remisión («equivalente a dos veces el
  importe de referencia establecido en el punto 3.7. y cuyo repago no se»).
  No se dibuja y no cambia la figura; queda para quien revise la derivación
  de `remite_a`.
- **Impreso**: NO VERIFICADO; la letra y las distancias se controlan sobre la
  geometría.
