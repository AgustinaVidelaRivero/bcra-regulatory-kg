# Figura de la resolución de entidades y sujetos en el ensamblado

Generador: `fig_resolucion.py`. Salidas: `figura_resolucion.svg`,
`figura_resolucion.png` (300 dpi) y `figura_resolucion.pdf`.

## 1. Qué muestra

Qué pasa en el ensamblado con una entidad desde que la devuelve el extractor
hasta que llega a su nodo, y qué pasa con el sujeto de una relación. Dos
carriles a 15 cm de ancho:

- **Carril de la entidad** (izquierda), cinco cajas en orden: la entidad que
  devolvió el extractor (gris); el control del tipo; el identificador; la
  unión por identificador; la unión entre documentos (azul).
- **Carril del sujeto** (derecha), dos cajas: la mención y la entrada
  sugerida (gris); el orden en que el ensamblado asigna una entrada (azul).
  De esta caja sale una flecha a la de la unión por identificador.

En cada caja, la línea general arriba (texto fijo, `TEXTO_GENERAL` del
generador, con sus cortes de renglón en `PARRAFOS`) y, debajo, en cursiva y
sobre un recuadro blanco, el ejemplo leído de los artefactos: la condición
del monto del punto 5.1.1.1 de Clasificación de deudores en el carril de la
entidad y las relaciones de sujeto del punto 5.1.1.2 en el del sujeto. Los
tipos van en una pastilla con el color de su tipo en las figuras del
ejemplo. La caja de la unión entre documentos no lleva ejemplo. La leyenda
dice qué es azul («Pieza de código»), qué es gris («Datos») y cómo se
distingue el ejemplo.

Tamaño: lienzo de 850 × 638 unidades, impreso a 15,00 × 11,26 cm; PNG de
1772 × 1331 px a 300 dpi. Letra de 15 unidades (7,50 pt impresos a 15 cm)
en todos los textos.

## 2. Cómo se regenera

Desde la raíz del repositorio, con el generador en `docs/tesis/figuras/`:

```
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/fig_resolucion.py --commit 3b6f63c1d6523e97ec9efac9b36b2d7ade064265 --grafo data/experiment/reaplicacion_unica/acumulado/ens_128_r2b_sincola/r2/kg.json.gz --sha256-grafo 576c97256185a0d5741cb2c35a2a85e91412f3e1119ad7a85d960b7d60c35ad3
```

Escribe las tres salidas junto al generador (o en `--salida <dir>`). Todo se
lee del commit de `--commit` con `git show <commit>:<ruta>`, nunca del árbol
de trabajo; por eso la figura no cambia aunque el árbol cambie. Un grafo
`.gz` se descomprime en memoria, y `--sha256-grafo` es el sha256 del
`kg.json` descomprimido. Necesita `git`, `rsvg-convert`, PIL y
`/System/Library/Fonts/Helvetica.ttc` (las mismas herramientas que las demás
figuras del capítulo 4). Dos corridas seguidas dieron los mismos sha256 en
las tres salidas (sección 8).

Sobre otro grafo: `--commit <commit> --grafo <ruta del kg.json o del
kg.json.gz> --sha256-grafo <sha256 del kg.json>`, y `--extraccion <jsonl>`
si la extracción validada del documento está en otra ruta
(`--unidad-entidad` y `--unidad-sujeto`, si cambian los identificadores de
las unidades). El generador se detiene sin escribir nada si el ejemplo no se
sostiene en ese grafo: si no hay exactamente una condición con umbral en la
unidad, si el identificador recalculado de la condición no es un nodo, si las
aristas de sujeto de la unidad no traen el mismo punto, la misma mención y la
misma sugerencia, si la entrada sugerida no es un nodo `Sujeto` con etiqueta
o si las aristas no se resolvieron todas igual.

## 3. Fuentes del ejemplo

En el commit `3b6f63c1d6523e97ec9efac9b36b2d7ade064265`:

| Fuente | Ruta | sha256 |
|---|---|---|
| grafo | `data/experiment/reaplicacion_unica/acumulado/ens_128_r2b_sincola/r2/kg.json.gz` | del `kg.json`: `576c97256185a0d5741cb2c35a2a85e91412f3e1119ad7a85d960b7d60c35ad3`; del `.gz`: `8a448e9185ee950d6157fb0a02ca88caba2b645f6220a210fdcd81609cd860f9` |
| sello del grafo | `data/experiment/reaplicacion_unica/sello_grafo_evaluado.json`, campos `grafos.ens_128_r2b_sincola.kg_json_sha256` y `gz_sha256` | `f44492f9d0e9c0b1271543c74b99f931463b4fa3af54c39fde08a914e12e91d3` |
| extracción validada | `data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b/cla/extracciones_finales_r2_cla.jsonl` | `65f9858a6b188cb7dab89831131fabafe40c27d627a2650898f0fedbaf46d141` |
| los nueve tipos | `data/experiment/pyd_r2/code/modelos_r2.py:104` (`TIPOS_ENTIDAD`, leído con `ast`) | `e67f15ae13dd5419ea0ce1a08dbef63c86cbdf9c269772a0b02a4e27b4c3a2ca` |

El grafo es el grafo evaluado: el ensamblado sin la cola, en la fase r2b,
con la unión de las comunicaciones por código. Los dos sha256 del grafo son
los de su sello. Lo armó el código del commit
`2db79462ef58d9d8e406ee631fd77c3e7758e25d`; `modelos_r2.py` tiene el mismo
blob en ese commit y en el de arriba.

## 4. Las líneas generales en el código

En el commit `2db79462`:

| Caja | Dónde |
|---|---|
| entidad que devolvió el extractor | `data/experiment/pyd_r2/code/modelos_r2.py:756-764` (`_EntidadE1`: `label`, `punto`) y `:811-814` (`CondicionE1`: `type`, `properties`, con la `descripcion` de `:730-731`) |
| control del tipo | `data/experiment/pyd_r2/code/validador_r2.py:874-884` (validador) y `data/experiment/reextraccion_v2/e2_reduce/e2_lib.py:1005-1007` (ensamblado), contra `TIPOS_ENTIDAD` de `modelos_r2.py:104-105` |
| identificador | `e2_lib.py:845-871` (`entity_slug_r2`) y `:1011` (el prefijo del tipo) |
| unión por identificador | `e2_lib.py:1016-1027` |
| unión entre documentos | `data/experiment/reextraccion_v2/corpus_v2/r1_invariantes.py:113-171` (`merge_grafos_guardado`: los sujetos del catálogo no se renombran) y `:174-202` (`_unir_comunicaciones_c1`: las comunicaciones de documentos distintos con el mismo código normalizado); la cadena la corre con la unión de las comunicaciones en `data/experiment/tanda0/code/ensamblar_tanda0.py:1965-1969` |
| mención y entrada sugerida | `modelos_r2.py:840-844` (`sujeto_mencion` y `sujeto_id` del extractor) y `e2_lib.py:801-803` (las marcas que la arista conserva) |
| orden de asignación | `data/experiment/reextraccion_v2/corpus_v2/r1_e4.py:391-487` (`resolver_relaciones_r2`, el orden en `:435-452`) |

## 5. Formato: de dónde sale cada valor

El generador comprueba, en el commit dado, que cada declaración esté una sola
vez en su fuente y escribe su número de línea (`ESTILO`, `leer_estilo`).
Líneas en el commit `3b6f63c1` (los archivos de estilo tienen el mismo blob
que en el commit de la versión anterior de la figura, así que el formato no
cambió):

| Valor | En la figura | Fuente |
|---|---|---|
| tipografía | `Helvetica,Arial,sans-serif` | `generar_figura_proceso.py:164` |
| azul (pieza de código) | relleno `#e1e7ee`, borde `#4a5a6a` | `generar_figura_proceso.py:166` |
| gris (datos) | relleno `#fafafa`, borde `#999999` | `generar_figura_proceso.py:167` |
| tintas | `#1f1f1f` (línea general, leyenda, tipos) y `#444444` (ejemplo) | `generar_figura_proceso.py:168` |
| flechas | `#555555`, grosor 1,8, esquinas de radio 9 | `generar_figura_proceso.py:169`, `:176`, `:177` |
| cajas | grosor 1,6, esquinas 8 | `generar_figura_proceso.py:175`, `:178` |
| recuadro del ejemplo y marco de la leyenda | `fill="white" stroke="#e2e2e2" stroke-width="1" rx="5"` | `generar_figura_proceso.py:181` |
| muestras de la leyenda | 24 × 16, filas de 22, esquinas 3 | `generar_figura_proceso.py:182`; `rx="3"` en `:1123` |
| punta de flecha | marcador de 10 × 10 | `generar_figura_proceso.py:183-184` |
| textos de la leyenda | «Pieza de código», «Datos» | `generar_figura_proceso.py:279-280` |
| aire de la leyenda | 10 arriba | `generar_figura_proceso.py:420` |
| flechas: hueco a la caja y distancia a las esquinas | 2,0 y `RX + 4` | `generar_figura_proceso.py:324-325` |
| ancho impreso y resolución | 15,0 cm, 300 dpi | `generar_figura_proceso.py:311`, `:313` |
| PDF reproducible | `SOURCE_DATE_EPOCH = "0"` | `generar_figura_proceso.py:1187` |
| lienzo | 850 unidades de ancho | `generar_figura_esquema_final.py:399` |
| letra mínima admitida | 7,0 pt | `generar_figura_esquema_final.py:404` |
| Menlo: avance y caja | 0,602 em; 0,76 y 0,24 em | `generar_figura_esquema_final.py:863-864` |
| margen | 14 | `generar_figura_extractor_ejemplo.py:155` |
| cuerpo e interlínea | 15 y 18 | `generar_figura_extractor_ejemplo.py:156-157` |
| caja del texto en Helvetica | 0,78 y 0,22 em | `generar_figura_extractor_ejemplo.py:158` |
| aire interior de las cajas | 12 y 9 | `generar_figura_extractor_ejemplo.py:160` |
| medida del texto | Helvetica real con PIL | `generar_figura_norma_a_grafo.py:803` (`FUENTE_SISTEMA`) |
| pastilla `Condicion` | relleno `#f8e8f5`, borde `#b5179e` | `figura_esquema_final.svg:110` |
| pastilla `TextoOrdenado` | relleno `#e8e8e8`, borde `#3d3d3d` | `figura_esquema_final.svg:126` |
| pastilla `Sujeto` | relleno `white`, borde `#6d597a`, discontinuo `7 5` | `figura_esquema_final.svg:124` |
| nombre del tipo | `Menlo,Consolas,'Courier New',monospace` en negrita | `figura_esquema_final.svg:111` |
| ejemplo en cursiva | la cursiva de las notas | `figura_esquema_final.svg:4` |

Valores propios de esta figura (no están en otra): anchos de carril (474 y
314, con 34 entre carriles), 28 entre cajas de un carril, recuadro del
ejemplo a 7 del borde de la caja con 8 y 4 de aire, interlínea del ejemplo
de 21 (la pastilla mide 19), pastillas con 4 y 2 de aire, esquinas de 3 y el
grosor de caja 1,6 en lugar del de su tipo, y la muestra del ejemplo en la
leyenda (una caja azul con su recuadro blanco). La leyenda va en el carril
del sujeto, debajo de la flecha, con su borde de abajo en el de la última
caja del carril de la entidad.

## 6. Valores del ejemplo, con su campo

Los lee `leer_ejemplo`. De la unidad del 5.1.1.1 se leen solo entidades (de
la extracción validada); de la del 5.1.1.2, solo sus aristas de sujeto (del
grafo); del nodo de un sujeto, solo su etiqueta.

| Caja | Valor dibujado | Campo |
|---|---|---|
| entidad que devolvió el extractor | `Condicion` | extracción validada, registro `chunk_id = "cla::5.1.1.1"`, `validacion.entidades[].type` de la condición del monto |
| | «Superar dos veces importe referencia punto 3.7» | ídem, `label` (igual al `label` de su nodo en el grafo) |
| | punto 5.1.1.1 | ídem, `punto` |
| control del tipo | `Condicion` está en la lista | `type` ∈ `TIPOS_ENTIDAD` de `modelos_r2.py` (9 tipos) |
| identificador | tipo, etiqueta, descripción, documento y punto | los campos de la clave de una `Condicion` (`CAMPOS_CLAVE`): `type`, `label`, `properties.descripcion`, `provenance.to` (`cla`) y `punto`; el generador recalcula el identificador con ellos (`id_de_contenido`) y comprueba que es un nodo del grafo |
| unión por identificador | `Condicion` es un nodo nuevo | el nodo de la condición tiene 1 procedencia, de una sola unidad: `cla::5.1.1.1` (`provenances[].chunk_id`) |
| | `TextoOrdenado` del 5.1.1.1: se une al nodo de 140 unidades de Clasificación de deudores | la entidad `TextoOrdenado` del 5.1.1.1 (`punto`); su nodo, el único `TextoOrdenado` con esa procedencia: 140 `chunk_id` distintos en `provenances`, todas del documento `cla`, y `properties.materia` |
| mención y entrada sugerida | Del 5.1.1.2: mención «la entidad»; entrada sugerida: `Sujeto` Obligados a clasificar deudores (Clasificación) | grafo, aristas `aplica_a` y `ejecuta` con procedencia `cla::5.1.1.2`: el `punto` de esa procedencia, `sujeto_mencion` y `sujeto_id_modelo`; la etiqueta es el `label` del nodo de ese id |
| orden de asignación | Las relaciones del 5.1.1.2, por el 2: `Sujeto` Obligados a clasificar deudores (Clasificación) | las mismas aristas: `metodo_resolucion` (`R4_sugerencia_modelo` → 2) y el `label` del nodo del sujeto (`target` de `aplica_a`, `source` de `ejecuta`) |

Cómo se lee el método de resolución como número del orden de la caja
(`numero_de_metodo`): `R1_…` (nombre o alias de la entrada) → 1;
`R4_sugerencia_modelo` → 2; `R2_…`, `R2_calificador` y `R3` (reglas sobre la
mención) → 3; `cuarentena` → 4. Es el orden de
`data/experiment/reextraccion_v2/corpus_v2/r1_e4.py`, `resolver_relaciones_r2`.

En este grafo, las relaciones de sujeto del 5.1.1.2 son 4 aristas `aplica_a`,
las 4 con el mismo punto, la misma mención, la misma sugerencia, el mismo
método y la misma entrada asignada, que es la sugerida.

## 7. Etiquetas abreviadas

Ninguna. Todas las etiquetas y valores se dibujan completos, envueltos por
palabras al ancho de su recuadro.

## 8. Salidas

| Archivo | sha256 |
|---|---|
| `figura_resolucion.svg` | `8688ae2bc239b9b6d19b3768bf6898b5809552a3a395ec9ec8dabb8571f4df1f` |
| `figura_resolucion.png` | `844a642fdd23cf0508d26b8a4fe75dd30af836def19d2e5a140e2cdc3af15f15` |
| `figura_resolucion.pdf` | `41cf3000f13d434b71f90a7b6c8662a755e6fcb22e77d60dacd107a8b0fc5261` |

Con el comando de la sección 2, corrido dos veces seguidas: mismos sha256.

## 9. Controles

En cada corrida, antes de escribir; el primero que falla detiene el
generador:

- contenido: cada línea general dibujada es el texto fijado, y ningún texto
  lleva identificadores internos, nombres de archivo ni comillas angulares
  simples;
- textos: 47, todos a 7,50 pt; cada uno dentro de su caja, recuadro, pastilla
  o leyenda, con 2,0 de holgura como mínimo; ninguno superpuesto a otro ni a
  una pastilla;
- cajas: 8 con la leyenda, sin superposición, a 26,4 como mínimo;
- flechas: 6, con 7 tramos, todos horizontales o verticales; cada una sale
  del borde de abajo de su caja y llega al borde de la de destino, lejos de
  las esquinas; ninguna atraviesa una caja ni toca un texto, y dos flechas
  sin caja en común no se tocan;
- margen: 14 unidades (2,47 mm) a cada borde, para un mínimo de 2 mm;
- alto: 11,26 cm, para un tope de 12,85 cm (la mitad de la caja de texto de
  una página A4 con 2 cm de margen arriba y abajo);
- registro: el SVG se relee; sus textos son los del modelo, en orden; cada
  caja tiene el relleno y el borde de su clase, y cada pastilla, el borde de
  su tipo.
