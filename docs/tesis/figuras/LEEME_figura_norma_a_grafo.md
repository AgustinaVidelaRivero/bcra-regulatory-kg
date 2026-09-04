# figura_norma_a_grafo — registro de generación

Figura «de la norma al grafo» para la Introducción. Caso: candidato 1 de la
sección I de `docs/tesis/inventario_recurso.md` — pregunta EV2F-013, par de
puntos `ext:3.17.1.4 → ext:3.4.3` del Texto Ordenado de Exterior y Cambios.

Generada el 2026-09-01 en unidad de SOLO LECTURA sobre los datos; las únicas
escrituras son el script, el SVG, el PNG y este archivo. Esta versión corrige
la anterior en tres cosas: la correspondencia texto↔nodo del punto 3.4.2, la
composición (paneles apilados) y el número de aristas dibujadas.

## 1. Comando de generación

```bash
python3 docs/tesis/figuras/generar_figura_norma_a_grafo.py
```

Escribe `figura_norma_a_grafo.svg` (860 × 1035). El PNG se exporta aparte:

```bash
rsvg-convert -z 2 -f png -o docs/tesis/figuras/figura_norma_a_grafo.png docs/tesis/figuras/figura_norma_a_grafo.svg
```

`rsvg-convert` es la única herramienta externa, y solo para el PNG (1720 × 2070
px). El SVG se produce con Python de la biblioteca estándar, sin dependencias:
el script escribe el marcado a mano, igual que el de la figura de la cláusula
del 125 %, del que copia tipografía (`Helvetica,Arial,sans-serif`), paleta por
tipo de nodo y estilo de leyenda.

## 2. Fuentes y sellos

| Archivo | sha256 |
|---|---|
| `data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json` | `0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a` |
| `data/experiment/reextraccion_v2/e0_chunking/salida/chunks_ext.json` | `ef910fd589a4a5540d8b7b7e23cbbcc983292c9eb272df36f46ed22aafcbd9c4` |

Salidas de esta corrida:

| Archivo | sha256 |
|---|---|
| `figura_norma_a_grafo.svg` | `a2d85ec100407fab760e05798538fcbc15428532703ffc72b8fa923169c1ecfc` |
| `figura_norma_a_grafo.png` | `eca4edfe298b94c4ca94810a443c0f39a8a358155ea1bdddd75ee3adf8825631` |

Generación determinística verificada: dos corridas consecutivas producen el
mismo SVG, y también lo hacen tres corridas con `PYTHONHASHSEED` distinto
(1, 2, 3), de modo que el resultado no depende del orden de iteración de
diccionarios ni conjuntos.

## 3. El punto 3.4.2 contiene dos disposiciones

Texto completo de la unidad de extracción `ext::3.4.2`
(`TO_exterior_cambios_actual.pdf`, página 17, 452 caracteres):

```
3.4.2. El monto total abonado por este concepto a accionistas no residentes, incluido el pago
cuyo curso se está solicitando, no supere el monto en moneda local que les
corresponda según la distribución determinada por la asamblea de accionistas.
La entidad deberá contar con una declaración jurada firmada por el representante legal
de la empresa residente o un apoderado con facultades suficientes para asumir este
compromiso en nombre de la empresa.
```

Son **dos disposiciones**, y la extracción produjo un nodo de contenido por
cada una:

| Oración | Nodo extraído |
|---|---|
| (1) «El monto total abonado por este concepto… según la distribución determinada por la asamblea de accionistas.» | **Restricción** «Monto total no supere distribución asamblea» (`…459761`) |
| (2) «La entidad deberá contar con una declaración jurada firmada por el representante legal… en nombre de la empresa.» | **Obligación** «Declaración jurada representante legal» (`…ed6cf9`) |

Nodos con procedencia de rol `punto_propio` en `ext:3.4.2` — los cinco, con la
oración de la que provienen:

| Tipo | Etiqueta | id | Proviene de |
|---|---|---|---|
| Obligacion | Declaración jurada representante legal | `Obligacion_la_entidad_debera_contar_con_una_declaracion_jurada_firmada_por_el_representante_ed6cf9` | oración (2) |
| Restriccion | Monto total no supere distribución asamblea | `Restriccion_el_monto_total_abonado_por_este_concepto_a_accionistas_no_residentes_incluido_el_459761` | oración (1) |
| Operacion | Giro divisas utilidades dividendos exterior | `Operacion_giro_divisas_utilidades_dividendos_exterior_c53c4e` | ninguna en particular: nombra la operación que el punto regula, y su id no cita el texto |
| Sujeto | Entidades autorizadas a operar en cambios (Exterior) | `Sujeto_rol_entidad_autorizada_exterior` | nodo de catálogo (aparece en 478 puntos) |
| TextoOrdenado | Texto Ordenado de Exterior y Cambios | `TextoOrdenado_to_exterior_cambios_actual_pdf` | nodo de estructura (aparece en 782 puntos) |

**Consecuencia y corrección.** El nodo que la figura dibuja para 3.4.2 es la
obligación de la declaración jurada, que proviene de la oración (2). La versión
anterior de la figura mostraba en el recuadro la primera línea del punto, que
pertenece a la oración (1): el texto y el nodo no se correspondían. Ahora el
recuadro muestra la oración (2) completa, precedida de `[…]` para señalar que el
punto tiene texto anterior que no se muestra.

## 4. Verificación de correspondencia texto ↔ nodo, para los cuatro puntos

El script comprueba, antes de dibujar, que el fragmento mostrado en cada
recuadro corresponde al nodo rotulado con ese número y no a otra disposición del
mismo punto. La medida es la fracción de las palabras del id del nodo —que el
extractor deriva del texto de la disposición— presentes en el fragmento
mostrado. Se exige cobertura ≥ 0,75 y que supere a la de cualquier otra
disposición del mismo punto; si no, el script se detiene y no escribe la figura.

| Punto | Nodo dibujado | Cobertura del nodo dibujado | Mejor de las otras disposiciones | Resultado |
|---|---|---|---|---|
| 3.17.1.4 | Restricción `…8355c7` | 1,00 | 0,00 | OK |
| 3.4.1 | Obligación `…999fbd` | 0,82 | 0,00 (no hay otra) | OK |
| 3.4.2 | Obligación `…ed6cf9` | 1,00 | 0,31 (restricción `…459761`) | OK |
| 3.4.3 | Obligación `…6514f0` | 0,93 | 0,00 (no hay otra) | OK |

La cobertura de 3.4.1 es 0,82 y no 1,00 porque el extractor reformuló el verbo
al construir el nodo: la norma dice «correspondan» y la etiqueta del nodo dice
«deben corresponder». El texto mostrado es el de la norma, sin cambios.

Fragmento mostrado en cada recuadro:

- **3.17.1.4** — el punto completo (una sola disposición, la que origina la
  restricción dibujada; contiene la frase de remisión resaltada).
- **3.4.1** — el punto completo: tiene una sola oración y una sola disposición,
  de modo que la línea mostrada ya es la que origina el nodo dibujado.
- **3.4.2** — la oración (2), precedida de `[…]`. El recorte es por el comienzo,
  no por el final: lo que se omite es la disposición anterior.
- **3.4.3** — el punto completo (una sola disposición de contenido normativo).

## 5. Composición y tamaño de letra impreso

Paneles apilados a ancho completo: arriba «En el texto», abajo «En el grafo», y
la leyenda al pie. La figura es más alta que ancha.

| Magnitud | Valor |
|---|---|
| Ancho del SVG | 860 px |
| Alto del SVG | 1035 px |
| Relación alto/ancho | 1,20 |
| PNG exportado | 1720 × 2070 px |

Cálculo del tamaño de letra impreso. A 15 cm de ancho de página, el ancho
disponible es 15 cm × 28,3465 pt/cm = **425,2 pt**, de modo que un texto de
`N` píxeles en un SVG de 860 px de ancho se imprime a `N × 425,2 / 860` puntos:

| Elemento | Tamaño en el SVG | Tamaño impreso a 15 cm |
|---|---|---|
| **Texto de los recuadros** | **17 px** | **8,41 pt** (mínimo exigido: 8 pt) |
| Encabezado de recuadro («Punto 3.4.2») | 15 px | 7,42 pt |
| Etiqueta de nodo | 15 px | 7,42 pt |
| Rótulo de arista | 13 px | 6,43 pt |
| Leyenda | 13 px | 6,43 pt |

El ancho de 860 px es el que hace que el texto de los recuadros supere los 8 pt:
con la misma letra de 17 px, cualquier ancho mayor que 903 px lo dejaría por
debajo del mínimo.

## 6. Nodos dibujados (6)

Se quitó el nodo del Texto Ordenado.

| Ref. | Tipo | Punto rotulado | id |
|---|---|---|---|
| R | Restriccion | 3.17.1.4 | `Restriccion_pagos_de_utilidades_y_dividendos_a_accionistas_no_residentes_en_la_medida_que_se_8355c7` |
| O1 | Obligacion | 3.4.1 | `Obligacion_las_utilidades_y_dividendos_deben_corresponder_a_balances_cerrados_y_auditados_999fbd` |
| O2 | Obligacion | 3.4.2 | `Obligacion_la_entidad_debera_contar_con_una_declaracion_jurada_firmada_por_el_representante_ed6cf9` |
| O3 | Obligacion | 3.4.3 | `Obligacion_la_entidad_debera_verificar_que_el_cliente_haya_dado_cumplimiento_en_caso_de_cor_6514f0` |
| OP | Operacion | 3.17.1.4 | `Operacion_pagos_utilidades_dividendos_accionistas_no_residentes_59fccf` |
| SU | Sujeto | (sin punto) | `Sujeto_rol_entidad_autorizada_exterior` |

Tres de los cinco nodos de contenido están anclados además en otro punto del
Texto Ordenado: la restricción `…8355c7` en 3.18.1.2, la obligación `…ed6cf9` en
9.3.12.2 y la obligación `…6514f0` en 9.3.12.3. El mismo elemento normativo
aparece literalmente en más de un lugar y el ensamblado lo representa con un
solo nodo de procedencia múltiple; la figura rotula cada uno con el punto que
corresponde a este caso. El sujeto no lleva número de punto porque figura con
rol `punto_propio` en 478 puntos: es un nodo de catálogo, no un elemento
extraído de un punto.

## 7. Aristas dibujadas (5)

Cada una se comprueba contra `kg.json` antes de dibujar: si alguna no existiera
en el grafo, el script se detiene.

| Clase | Origen | Predicado (en la figura) | Destino |
|---|---|---|---|
| **resaltada** | R | remite a | O1 |
| **resaltada** | R | remite a | O2 |
| **resaltada** | R | remite a | O3 |
| gris | R | limita | OP |
| gris | R | se aplica a | SU |

Quedaron fuera, respecto de la versión anterior: las cuatro `establecida en`
hacia el Texto Ordenado (junto con ese nodo) y tres de las cuatro `se aplica a`
—las de las tres obligaciones al sujeto—, de modo que del contexto queda una
sola arista de cada clase. Todas siguen existiendo en el grafo; no se muestran.
Traducción de predicados: `referencia` → «remite a», `aplica_a` → «se aplica
a», `limita` → «limita».

## 8. Etiquetas acortadas

Máximo 40 caracteres por línea visible. La línea más larga de la figura
terminada tiene 38 caracteres.

| Nodo | Etiqueta original en el grafo (largo) | Etiqueta dibujada (largo) |
|---|---|---|
| R | `Requisitos puntos 3.4.1 a 3.4.3 — utilidades dividendos` (55) | `Requisitos para pagar dividendos` (32) |
| O3 | `Verificación de cumplimiento declaración de activos y pasivos externos` (70) | `Verificación del Relevamiento externo` (37) |
| OP | `Pagos utilidades dividendos accionistas no residentes` (53) | `Pago de dividendos a no residentes` (34) |
| SU | `Entidades autorizadas a operar en cambios (Exterior)` (52) | `Entidades autorizadas en cambios` (32) |
| O1 | `Balances cerrados y auditados` (29) | sin cambio |
| O2 | `Declaración jurada representante legal` (38) | sin cambio |

Lo que la abreviatura de R deja fuera («puntos 3.4.1 a 3.4.3») sigue visible en
la figura por otras dos vías: las tres aristas «remite a» hacia los nodos
rotulados 3.4.1, 3.4.2 y 3.4.3, y la frase resaltada del panel de texto.

## 9. Otras decisiones de composición

- **Sin título general ni subtítulo** dentro de la imagen: el caption del `.tex`
  los reemplaza. Tampoco hay pie de fuente, nombres de archivo, sellos ni
  nombres internos de grafos en ninguna parte visible.
- **Orden de los recuadros**: numérico —3.17.1.4, 3.4.1, 3.4.2, 3.4.3— para que
  coincida con el orden vertical de los nodos del panel del grafo.
- **Verbatim**: el texto sale del campo `texto` de las unidades de extracción de
  `chunks_ext.json`, sin cambiar ninguna palabra ni signo. Lo único que se
  altera es el punto de corte de línea: los saltos del PDF se unen y el texto se
  vuelve a envolver al ancho del recuadro. El número de punto se muestra como
  encabezado del recuadro en lugar de repetirse dentro del párrafo. Cada
  fragmento se verifica carácter por carácter contra el texto de la unidad antes
  de dibujar.
- **Resaltado**: la frase «en la medida que se verifiquen los requisitos
  previstos en los puntos 3.4.1. a 3.4.3.» va sobre fondo de acento y en
  negrita, y el recuadro de 3.17.1.4 lleva borde del mismo color. Las tres
  aristas de remisión usan ese mismo acento (`#e07b39`, el naranja de la paleta
  compartida). El rectángulo del resaltado se ubica con las métricas de ancho de
  Helvetica incluidas en el script, sin librerías de tipografía.
- **Trazado de las aristas**: qué aristas existen se lee del grafo; cómo se
  dibujan es decisión de la figura, declarada en la tabla `RUTAS` del script.
  Con cinco aristas y seis nodos ninguna cruza por encima de una caja.
- **Formas**: los nodos son cajas redondeadas y no círculos como en la figura de
  la cláusula del 125 %: las etiquetas de dos líneas de hasta 40 caracteres no
  entran en un círculo legible. Tipografía, paleta por tipo de nodo, convención
  de foco (nodos del caso opacos con texto blanco, contexto translúcido con
  texto oscuro) y formato de leyenda se mantienen iguales a esa figura.
- **Leyenda**: banda propia al pie, en dos filas —tipos de nodo y clases de
  arista—, con los cuatro tipos de nodo que aparecen. Ya no incluye el tipo
  Texto Ordenado, ausente de esta versión.

## 10. Verificaciones ejecutadas

- Correspondencia texto↔nodo comprobada para los cuatro puntos (tabla de §4); el
  script aborta si alguna falla.
- Seis cajas de nodo y cinco aristas en el SVG (contadas sobre el marcado, sin
  contar las dos muestras de la leyenda); tres de las cinco son remisiones
  resaltadas.
- Sin nombres internos en el texto visible del SVG: `Reextra`, `sha`, `test` y
  `.json` dan cero coincidencias sobre el contenido de los elementos `<text>` y
  `<tspan>`.
- Línea de etiqueta más larga: 38 caracteres (máximo admitido 40).
- Texto de los recuadros a 15 cm de ancho: 8,41 pt (mínimo exigido 8 pt).
- Dos corridas consecutivas y tres con distinta semilla de hash producen el
  mismo SVG (sha256 `a2d85ec1…`).
