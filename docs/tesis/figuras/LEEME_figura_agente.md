# figura_agente — figura del agente y sus 2 servidores de herramientas

`figura_agente.png`, dibujada por `fig_agente.py` con el estilo de la Figura 5.4
(`figura_comparacion.png`). Archivos:

| Archivo | Qué es |
|---|---|
| `fig_agente.py` | El script. No lee ningún archivo: usa solo sus constantes y escribe el PNG junto a él. |
| `figura_agente.png` | La figura. |
| `figura_agente.svg` | El SVG del que sale el PNG (§9). |
| `LEEME_figura_agente.md` | Este archivo. |

Regenerar, desde la carpeta del script:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B fig_agente.py
```

Necesita Python 3 (biblioteca estándar) y `rsvg-convert` (se usó la 2.62.3).

## 1. El script del que se tomó el estilo

- Ruta: la última copia de trabajo de `fig_comparacion.py`, fuera del repositorio.
- sha256: `1b75dd15c61dc769524f6c2ec508b4a0061f697d897b35a8f44f07cec9247511`

Cómo se identificó:

- Por el nombre: el script se llama `fig_comparacion.py` y escribe `figura_comparacion.png`.
- Por el sha256 de la imagen: en la misma carpeta, `figura_comparacion.png` tiene
  sha256 `c02cfeba81270ecd6266bc69d94ffe4b3a1a4ae8735e33d7bcfeda7e9215d174`, el de la
  Figura 5.4. El `LEEME_figura_comparacion.md` de esa carpeta (renglón 11) registra
  que el script con sha256 `1b75dd15…9247511` genera ese PNG, igual en 2 corridas.
  El script del estilo no se corrió en esta unidad.
- Se descartó la copia anterior de `fig_comparacion.py` (sha256
  `05e6bae0c08c5f4092cd48a87d01a0c0355d07bdd0e9fba5106076a4ae74a79c`): junto a él, el
  `figura_comparacion.png` tiene sha256 `820309dd0c1c717816a5161ec5dd0c5bda96954406100ef9e485b70bec0f3d90`,
  que no es el de la Figura 5.4.
- En el repositorio, `docs/tesis/figuras/` no tiene `fig_comparacion.py` ni
  `figura_comparacion.png`, ni en `HEAD` ni en la copia de trabajo.

El script del estilo no importa nada del proyecto: solo la biblioteca estándar, y
llama a `rsvg-convert` para pasar el SVG a PNG.

## 2. Qué se copió

### Constantes de estilo, sin cambios

`C` es `fig_comparacion.py`. Cada línea de `fig_agente.py` copiada lleva al lado
`# C:<renglón>`. Un cotejo renglón por renglón dio
42 iguales y una sola diferencia de forma: el renglón de «Datos» cierra ahí la
tupla `LEYENDA`, porque esta figura no lleva la entrada «Resultado».

| Constante | Valor | Renglón en C | Renglón en `fig_agente.py` |
|---|---|---|---|
| `W` | 760 | 136 | 125 |
| `TIPOGRAFIA` | `"Helvetica,Arial,sans-serif"` | 137 | 126 |
| `MODELO` | relleno `#fbe3d3`, borde `#e07b39` | 138 | 127 |
| `DETERMINISTICA` | relleno `#e1e7ee`, borde `#4a5a6a` | 139 | 128 |
| `NEUTRO` | relleno `#fafafa`, borde `#999999` | 140 | 129 |
| `TINTA, TINTA_SUB` | `#1f1f1f`, `#444444` | 141 | 130 |
| `FLECHA` | `#555555` | 142 | 131 |
| `FS_TITULO, FS_TEXTO` | 14, 13 | 143 | 132 |
| `IL` | 18 y 17 | 144 | 133 |
| `SEP_TITULO` | 5 | 145 | 134 |
| `PAD_X, PAD_Y` | 9, 11 | 146 | 135 |
| `GROSOR_CAJA` | 1,6 | 147 | 136 |
| `GROSOR_FLUJO` | 1,8 | 148 | 137 |
| `RADIO` | 9 | 149 | 138 |
| `RX` | 8 | 150 | 139 |
| `MARGEN` | 12 | 151 | 140 |
| `LEYENDA_MARCO` | blanco, borde `#e2e2e2` de 1, esquinas de 5 | 152 | 141 |
| `MUESTRA_W, MUESTRA_H, FILA_LEY` | 24, 16, 22 | 153 | 142 |
| `MARCADOR_A`, `MARCADOR_B`, `MARCADOR` | la punta de flecha | 154, 155, 172 | 143, 144, 160 |
| `LEYENDA` | las 3 primeras entradas | 156-158 | 145-147 |
| `ANCHO_CM` | 15,0 | 160 | 148 |
| `DPI` | 300 | 161 | 149 |
| `PT_MINIMO` | 7,0 | 162 | 150 |
| `MARGEN_MM` | 2,0 | 163 | 151 |
| `DISTANCIA_MIN` | 3,0 | 164 | 152 |
| `SEP_CAJAS` | 8,0 | 165 | 153 |
| `HOLGURA_TEXTO` | 1,5 | 166 | 154 |
| `HUECO_PUNTA` | 2,0 | 167 | 155 |
| `ASC, DESC` | 0,78, 0,22 | 168 | 156 |
| `GRUPO_LEYENDA` | 10 | 169 | 157 |
| `RX_MUESTRA` | 3 | 170 | 158 |
| `LEJOS_ESQUINA` | `RX + 4` | 171 | 159 |
| `PALETA` | modelo, código y datos (sin «resultado») | 173 | 161 |
| `PT_POR_CM` | 72 / 2,54 | 175 | 162 |
| `ANCHO_PNG_PX` | 1772 | 176 | 163 |
| `MARGEN_MIN` | 10,1 unidades | 177 | 164 |
| `SEP_FLECHA` | 20 | 353 | 165 |
| `SOBRE_LEYENDA` | 10 | 355 | 166 |
| `SEP_SIN_FLECHA` | `ceil(SEP_CAJAS + GROSOR_CAJA)` = 10 | 356 | 167 |
| `_CARS`, `_AFM` | anchos AFM de Helvetica y Helvetica-Bold | 256-270 | 179-193 |

No se copiaron, porque esta figura no los usa: `GROSOR_RAMA`, la entrada
«Resultado» de la leyenda y de la paleta, `GROSOR_DESTACADO`, `ALTO_MAX_CM`,
`SEP_VERTICAL` y el cotejo con el script de la figura del proceso (`FORMATO`).

### Código reproducido

Además de las constantes, `fig_agente.py` reproduce, adaptadas, funciones de `C`
(no las importa): la medida del texto con las tablas AFM, la partición en
renglones, la poligonal con esquinas redondeadas, la emisión del SVG, el bloque
`pHYs` que graba los 300 dpi y la geometría de los controles.

### Agregados de esta figura

| Agregado | Renglón | Motivo |
|---|---|---|
| Anchos AFM de `\|` (260 y 280 en negrita) y `_` (556) | 196-197 | La tabla de C no los trae. `_` aparece en ver_remisiones. Ningún texto usa ya `\|`: solo aparecía en el texto anterior de la caja 7. Su ancho queda en el script, sin uso. |
| `MARCADOR_INICIO` | 172 | La punta del comienzo de las flechas de doble punta: la de `MARCADOR`, en espejo. |
| `SEP_DOBLE` = 32 | 234 | Entre cada servidor y su fuente: con 20 unidades las 2 puntas se tocaban. |
| `ANCHO_TEXTO`, `COLUMNAS`, `SEPARACIONES`, `ARRIBA`/`ABAJO`, `PUENTE`, `SUBIDA`, `BAJADA`, `LIBRE`, `SEP_ANOTACION`, `SOBRE_FLECHA`, `LADO_ROTULO` | 222-248 | Medidas de la disposición de esta figura. |

La comparación no usa letra monoespaciada: `ver_remisiones` va en la letra normal.

## 3. Huellas

| Archivo | sha256 |
|---|---|
| `fig_agente.py` | `348cd25cae99238d445323dc83f4326fa65fef73561d528523227fa8c6875a46` |
| `figura_agente.png` | `49a34d47fcd89059f5bf26745cf11bd4f2b666f3683004113907f5ac6f266be9` |
| `figura_agente.svg` | `7a51c1a47f41d7bb5c5bee52e84239b98d066ec30cbba70c6759ce1b0b42917d` |

Corrido 2 veces, el PNG y el SVG dieron el mismo sha256.

## 4. Tamaño y resolución

| Imagen | Píxeles | Resolución grabada | Impresa |
|---|---|---|---|
| `figura_agente.png` (esta unidad) | 1772 × 1181 | 300 dpi (`pHYs` 11811 px/m) | 15,00 × 9,99 cm (lienzo 760 × 506) |
| `figura_comparacion.png` (el estilo) | 1772 × 1040 | 300 dpi (`pHYs` 11811 px/m) | 15,00 × 8,80 cm (lienzo 760 × 446) |

El ancho coincide: 1772 px.

## 5. Los textos y su renglón en `fig_agente.py`

Cajas (título en negrita y, debajo, el texto en letra normal y gris):

| N.º | Clase | Título | Texto | Renglón |
|---|---|---|---|---|
| 1 | Datos | El pedido | La plantilla, igual para los 2 sistemas, con la pregunta, el tope de 30 llamadas y el bloque de las herramientas del servidor | 85 |
| 2 | Pieza que ejecuta un modelo de lenguaje | Agente | Claude Sonnet 5 en Claude Code, con sus herramientas propias apagadas | 86 |
| 3 | Reglas fijas | Servidor del grafo | 3 herramientas sobre los nodos y 7 de navegación por los puntos | 87 |
| 4 | Reglas fijas | Servidor de los fragmentos | Una herramienta, que devuelve los 5 fragmentos más afines, en 2 configuraciones, la combinada y la densa | 88 |
| 5 | Datos | El grafo evaluado | El sellado, en Neo4j | 89 |
| 6 | Datos | Los fragmentos | Todas las unidades de extracción, también las apartadas | 90 |
| 7 | Datos | La respuesta | El texto, las citas con su documento y su punto, y si encontró con qué responder | 91 |
| 8 | Datos | La traza | Cada llamada, con su entrada y su salida, que guarda el servidor | 92 |

Textos sin caja, en el gris del texto de las cajas (`TINTA_SUB`):

| Texto | Dónde va | Renglón |
|---|---|---|
| Un servidor por corrida | Entre las 2 flechas del agente a los servidores | 108 |
| En el ejemplo del préstamo, ver_remisiones lleva del 5.1.1.1 al 3.7 | Debajo de la caja 3 | 109 |

El rótulo de flecha «llamadas», sobre la flecha agente ↔ servidor de los
fragmentos, está en el renglón 106.

Leyenda, abajo a la izquierda:

| Entrada | Renglón |
|---|---|
| Pieza que ejecuta un modelo de lenguaje | 145 |
| Reglas fijas | 146 |
| Datos | 147 |

## 6. Disposición

De izquierda a derecha: el pedido; el agente, del alto de los 2 servidores; los
servidores, uno arriba del otro; sus fuentes, cada una a la altura de su
servidor, con la traza entre las 2; y, arriba a la derecha, la respuesta, a la
que llega una flecha que sale de arriba del agente y pasa por encima de los
servidores y las fuentes. Cada servidor manda su flecha a la traza por debajo
o por encima de su fuente. La figura no lleva título.

Decisiones:

- El servidor de los fragmentos va arriba y el del grafo abajo. Con el del grafo
  arriba, su anotación quedaba entre los 2 servidores, al lado de «Un servidor
  por corrida», y los 2 textos se leían como uno solo. Abajo, la anotación queda
  sola debajo de la caja 3.
- «llamadas» va sobre la flecha de arriba (agente ↔ servidor de los fragmentos),
  para no juntarse con «Un servidor por corrida», que va entre las 2 flechas.

## 7. Verificación

Los controles del script pasan (si uno falla, no se escribe nada): las 8 cajas
y sus textos, letra por letra, son los de `CAJAS`; los textos sin caja y la
leyenda, también; las columnas van de izquierda a derecha, los servidores uno
arriba del otro y cada fuente a la altura de su servidor; las 8 flechas son las
de `FLECHAS` (4 de doble punta), sin tramos diagonales ni hacia la izquierda;
ninguna flecha ni punta entra en una caja; no hay cruces entre flechas
(distancia mínima 43,2 unidades); ningún texto sale de su caja, se superpone con
otro ni toca una flecha (distancia mínima texto-texto 4,0 y texto-flecha 7,0);
nada queda a menos de 2 mm del borde; el SVG releído tiene el color, el grosor y
las puntas de cada clase; el PNG mide 1772 px y graba 300 dpi.

La figura se miró después de cada corrida. Las condiciones de la disposición se
cumplen en la versión final.

## 8. Archivos leídos fuera de la carpeta del script

Solo para encontrar el script del estilo:

- El listado de las carpetas de trabajo de las figuras.
- El sha256 de los `figura_comparacion*.png` y de los `*comparacion*.py` de esas carpetas.
- `LEEME_figura_comparacion.md` de la última copia de trabajo (solo los renglones con sha256).
- `fig_comparacion.py` de esa copia, completo.
- `figura_comparacion.png` de esa copia, para mirarla y medirla.
- La lista de `docs/tesis/figuras/` del repositorio, en `HEAD` y en la copia de trabajo.

## 9. Cambio de texto de la caja 4

- `fig_agente.py:88`: «la principal y la densa» pasa a «la combinada y la densa».
  Es el único cambio del script. Antes: script `3ff8bdd4e519f38cb660eb38d22568a8d0d0171e2d214cf9ab25ac3ae1f9023c`,
  PNG `3e8d20bb6b74afc5cd88e526ef8d4e8ea07149b1d21d4c14a7aa40718b804b33`.
- El script parte los renglones solo, y el texto de la caja ocupa ahora 7 en vez
  de 6. La caja pasa de 165 a 182 unidades de alto, su flecha al agente baja de
  124,5 a 133,0, «llamadas» de 113,7 a 122,2 y «Un servidor por corrida» 4,3
  unidades. El resto de la figura queda donde estaba: el lienzo sigue en
  760 × 506 y el PNG en 1772 × 1181 px.
- El script no tiene una opción para guardar el SVG. `figura_agente.svg` se
  obtiene cargándolo y escribiendo `verificar(armar())["svg"]`, el mismo SVG que
  `main` pasa a PNG.
