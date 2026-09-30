# figura_norma_a_grafo — registro de generación (Figura 1.1)

Figura «de la norma al grafo» para la Introducción, con el ejemplo del préstamo:
el punto 5.1.1.1 del Texto Ordenado de Clasificación de deudores, que remite al
punto 3.7 («importe de referencia»). Arriba, «En el texto»: en gris, la frase de
la unidad 5.1.1 que encabeza la lista de excepciones; debajo y con sangría, el
punto 5.1.1.1 completo, con resaltada la frase «dos veces el importe de
referencia establecido en el punto 3.7.»; una línea «[…]»; y, de nuevo al nivel
de la frase, el punto 3.7 completo. Abajo, «En el grafo»: los cinco nodos y las
cuatro aristas que la extracción produjo a partir de esos dos puntos.

Historia: generada el 2026-09-28 en U-FIG-EJEMPLO, que reemplazó la versión del
ejemplo de los dividendos (Exterior y Cambios, puntos 3.17.1.4 y 3.4.1 a 3.4.3:
SVG, PNG y LEEME del commit `2f511ba`, generador del commit `f050fcd`); ajustada
el mismo día en U-FIG-EJEMPLO-AJUSTE (§6). La versión de U-FIG-EJEMPLO no llegó a
commitearse: al cierre del ajuste, `git status` mostraba estos archivos como
modificados respecto de esos commits.

## 1. Comandos de generación

```bash
PYTHONDONTWRITEBYTECODE=1 python3 docs/tesis/figuras/extraer_datos_ejemplo_prestamo.py
PYTHONDONTWRITEBYTECODE=1 python3 docs/tesis/figuras/generar_figura_norma_a_grafo.py
rsvg-convert -z 2 -f png -o docs/tesis/figuras/figura_norma_a_grafo.png docs/tesis/figuras/figura_norma_a_grafo.svg
```

El primero escribe `ejemplo_prestamo_datos.json` (común a las figuras 1.1, 1.2,
1.3 y 2.1); el segundo escribe `figura_norma_a_grafo.svg` (860 × 973); el
tercero exporta el PNG (1720 × 1946 px). `rsvg-convert` 2.62.3 es la única
herramienta externa. El generador no tiene valores del ejemplo escritos a mano:
textos, nodos y aristas se leen del JSON, y el script comprueba contra `kg.json`
(sha256 declarado en el JSON) que cada nodo (id, tipo, etiqueta, punto) y cada
arista (índice, origen, relación, destino) estén en el grafo; si algo falta, se
detiene sin dibujar.

## 2. Grafo, pregunta y fuentes

- Grafo: KG-Reextraído-r1,
  `data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json`, sha256
  `0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a`.
- Pregunta del ejemplo (no aparece en esta figura; es la de la Figura 1.2): «Para
  una entidad financiera, ¿qué condiciones hacen que los créditos para consumo o
  vivienda deban clasificarse en la cartera comercial?»

| Archivo | Papel | sha256 |
|---|---|---|
| `data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json` | nodos y aristas | `0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a` |
| `data/experiment/reextraccion_v2/e0_chunking/salida_enm01/chunks_cla.json` | textos de la norma | `98808886a406d8321c678836a55f92eea983d594d95358dd21ceb537487ac0b1` |
| `docs/tesis/figuras/extraer_datos_ejemplo_prestamo.py` | escribe el JSON | `4c3a441972d27304b6d58d0664dbc15b893bce7ad3e7d2d49afad947f51eeea7` |
| `docs/tesis/figuras/ejemplo_prestamo_datos.json` | datos de la figura | `25ab7b4c0d76fd735244fe0fecc17ceaba1b0e8bfd2312e7aa3cbd5c849672a2` |
| `docs/tesis/figuras/generar_figura_norma_a_grafo.py` | generador | `9b0e45a299a0a078d250ccc999d192cbb83038bd8c00baa6bd8972d021b73f3d` |

Mediciones del ejemplo, versionadas en `reports/` (ver §7): `reports/u_inv_ejemplo/`
(commit `24e0116`), `reports/u_med_ejemplo/` (commit `200462f`) y
`reports/u_inv_candidatos/` (commit `791166d`; según el mensaje de ese commit,
la búsqueda sistemática del ejemplo conductor que eligió cla::5.1.1.1 → cla::3.7).
Antes de versionarse estaban en `/tmp/u_inv_ejemplo/`, `/tmp/u_med_ejemplo/` y
`/tmp/u_inv_candidatos/`; esas rutas quedan solo como historia.

Salidas:

| Archivo | sha256 |
|---|---|
| `figura_norma_a_grafo.svg` | `d43f7247d2c06bda27dd64f1d34fcd3ec56401b511b7cfa60a7817ef3940e251` |
| `figura_norma_a_grafo.png` | `7d26338468810ebc4b1c88f98dcc6cd616f62fe8b0b8cb3137bffb56619dc65c` |

Generación determinística verificada: el JSON, el SVG y el PNG dan el mismo
sha256 con `PYTHONHASHSEED` 0, 1, 2 y 3.

## 3. Textos de la norma

Del campo `texto` de los fragmentos E0 de `chunks_cla.json`, con los cortes de
línea quitados y las palabras partidas por guion al final de línea reunidas
(una sola en los tres textos: «pro-ductiva» → «productiva», en 5.1.1.1). Nada
más se cambia: el texto empieza con su número de punto y su título, tal como
está en el fragmento. El extractor guarda en el JSON, para cada punto, el campo
original (`texto_campo`) junto al texto de la figura.

- **5.1.1** (en gris, sin recuadro): «5.1.1. Cartera comercial. Abarca todas las
  financiaciones comprendidas, con excepción de las siguientes:». No hay un
  fragmento `cla::5.1.1`: la frase se compone con el encabezado heredado
  «5.1.1. Cartera comercial.» y el texto del bloque intro `cla::5.1.1::intro`
  («Abarca todas las financiaciones comprendidas, con excepción de las
  siguientes:»), que en el texto completo del fragmento son dos líneas. El
  extractor comprueba que esas dos piezas son las mismas que encabezan, en su
  herencia, a `cla::5.1.1.1`.
- **5.1.1.1** (recuadro con borde de acento, con sangría): texto completo, 4 líneas.
- **«[…]»** (en gris): marca de texto del documento que no se muestra; no sale
  del JSON, es un elemento de la composición (`OMISION`).
- **3.7** (recuadro, al nivel de la frase de 5.1.1): texto completo, 3 líneas.

## 4. Nodos dibujados (5)

| Clave en el JSON | Tipo | Punto rotulado | Etiqueta en el grafo | id |
|---|---|---|---|---|
| restriccion_monto | Restriccion | 5.1.1.1 | Créditos consumo/vivienda — monto supera dos veces importe referencia | `Restriccion_los_creditos_para_consumo_o_vivienda_que_superen_el_equivalente_a_dos_veces_el_i_f682b1` |
| obligacion_3_7 | Obligacion | 3.7 | Considerar importe de referencia — ventas anuales Micro Comercio | `Obligacion_el_importe_a_considerar_sera_el_nivel_maximo_del_valor_de_ventas_totales_anuales_7f1ae2` |
| operacion | Operacion | 5.1.1.1 | Inclusión en cartera comercial — créditos consumo/vivienda | `Operacion_inclusion_en_cartera_comercial_creditos_consumo_vivienda_2644e8` |
| sujeto | Sujeto | (sin número) | Obligados a clasificar deudores (Clasificación) | `Sujeto_rol_obligado_a_clasificar_clasificacion` |
| restriccion_repago | Restriccion | 5.1.1.1 | Crédito — repago no vinculado a ingresos fijos, vinculado a actividad productiva | `Restriccion_creditos_cuyo_repago_no_se_encuentre_vinculado_a_ingresos_fijos_o_periodicos_del_a5e44e` |

Los cuatro nodos de contenido tienen una sola procedencia con rol
`punto_propio`, la del punto con que se rotulan (el extractor se detiene si no).
El sujeto se dibuja sin número: es un nodo de catálogo con 91 procedencias
`punto_propio` distintas (primaria `cla::1.1`; 3.7 entre ellas), recuento del
extractor sobre las claves (documento, punto, rol) sin repetir. El Paso 2 de
U-MED-EJEMPLO-2 registra 102 procedencias para el mismo nodo porque cuenta
todas las entradas de su lista `provenances`, de cualquier rol: 91
`punto_propio` + 7 `bloque_intro` + 2 `bloque_cierre` + 1
`herencia_encabezado` + 1 `esqueleto` = 102.

Etiquetas: las del grafo, completas y sin traducir, envueltas a 40 caracteres
por línea como máximo (la más larga dibujada tiene 40). Tipos en la leyenda
escritos como en el código, sin tildes. Foco: los nodos Restriccion y
Obligacion, opacos con texto blanco; la Operacion y el Sujeto, translúcidos con
texto oscuro, como contexto.

## 5. Aristas dibujadas (4)

Cada una se comprueba en `kg.json` por su índice en `kg['edges']`.

| Índice | Origen | Relación | Destino | Clase en la figura |
|---|---|---|---|---|
| 15773 | restriccion_monto | referencia | obligacion_3_7 | resaltada («remisión de un punto a otro»); `rol_fuente = referencia_cruzada` |
| 15772 | restriccion_monto | limita | operacion | gris |
| 12389 | restriccion_repago | limita | operacion | gris |
| 3941 | obligacion_3_7 | aplica_a | sujeto | gris |

Los nombres de relación se escriben como en el grafo (`referencia`, `limita`,
`aplica_a`), sin traducir.

## 6. Composición y tamaño de letra

- Paneles apilados a ancho completo, leyenda al pie. Sin título, subtítulo, pie
  de fuente ni nombres internos en el texto visible.
- **Panel de texto (ajuste U-FIG-EJEMPLO-AJUSTE).** La frase de 5.1.1 termina en
  «con excepción de las siguientes:»; con los dos recuadros debajo y al mismo
  nivel, un lector que no conoce la numeración leería el 3.7 como una segunda
  excepción. La composición lo impide (tabla `COMPOSICION_TEXTO`): el recuadro
  de 5.1.1.1 va con 32 px de sangría bajo la frase, como elemento de la lista; el
  de 3.7 vuelve al nivel de la frase, precedido por la línea «[…]», que marca
  texto del documento no mostrado. Textos, resaltado y panel del grafo no
  cambian; el panel del grafo baja 31 px porque el de texto crece (SVG 942 → 973
  px de alto).
- Panel del grafo en dos columnas y tres filas (tabla `DISPOSICION`): la
  restricción del monto y la obligación del 3.7 arriba, unidas por la arista
  resaltada; la operación en el medio, limitada desde arriba y desde abajo por
  las dos restricciones; el sujeto debajo de la obligación.
- El número de punto va en negrita al comienzo de cada texto, donde el texto lo
  trae; los recuadros no llevan encabezado «Punto N».
- La negrita (número de punto y frase resaltada) se mide con la tabla de anchos
  de Helvetica Bold al envolver y al ubicar el rectángulo del resaltado.
- Tamaños: a 15 cm de ancho, texto de los recuadros 17 px → 8,41 pt; etiqueta
  de nodo 15 px → 7,42 pt; rótulo de arista y leyenda 13 px → 6,43 pt.
- Verificación geométrica con `docs/tesis/figuras/verificar_geometria_svg.py` (sha256
  `fd8d062df7b7529131f466df628298e02dd079517aa66624caeea6a8b722df19`; métricas reales de
  Helvetica): 38 textos, 5 nodos, 6 trazos con flecha; ningún texto se
  superpone con otro ni pisa un nodo, ningún trazo atraviesa un nodo. Comando:
  `PYTHONDONTWRITEBYTECODE=1 python3 docs/tesis/figuras/verificar_geometria_svg.py docs/tesis/figuras/figura_norma_a_grafo.svg`.

## 7. Búsquedas del ejemplo (contexto, no dibujadas en esta figura)

Resultados copiados en `ejemplo_prestamo_datos.json` desde `reports/u_med_ejemplo/`
(commit `200462f`; antes en `/tmp/u_med_ejemplo/`):

- Búsqueda léxica sobre los 1.763 fragmentos, variante A (la de la Figura 1.2,
  recalculada por el extractor con `busqueda_lexica_fragmentos.py`): 5.1.1.1 en
  el puesto 2 y 3.7 en el 1.523; reproduce
  `reports/u_med_ejemplo/umed2_analista_paso1_resultado.json` (sha256
  `a69c44b00a7f4920d1a4e5224167e6edacf4b7153d004d2185050cb2387f5408`, línea 11
  de `reports/u_med_ejemplo/umed_manifest.txt`).
- Variante B (palabras vacías y raíces de Snowball para español), del mismo
  archivo: 5.1.1.1 en el puesto 5; 3.7 sin puntaje (ningún término en común).
  La lista de palabras vacías que usó está en
  `reports/u_med_ejemplo/umed2_analista_nltk_data/corpora/stopwords/spanish`
  (sha256 `6125eadf28ba664a60bf4296147bcbd40b80be93670056fdb229960ac15e2310`,
  igual a la línea 30 de `reports/u_med_ejemplo/umed2_analista_nltk_data_listado.sha256`).
- Búsqueda sobre nodos (índice de texto completo
  `nodos_fulltext_kg_reextraido_r1`, 2.346 nodos con coincidencia), de
  `reports/u_med_ejemplo/umed2_analista_paso3_resultado.json` (sha256
  `047e6f6e80b6b88e300cfb090bd2223ea967de8c9cbea9e10f9c04a9c168a3cd`, línea 18
  del mismo manifiesto): nodos de 5.1.1.1 en los puestos 2 (operación), 4
  (restricción del monto) y 156 (restricción del repago); ningún nodo de 3.7
  tiene coincidencia.
