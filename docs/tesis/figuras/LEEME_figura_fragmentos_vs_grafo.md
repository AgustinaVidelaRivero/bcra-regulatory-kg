# figura_fragmentos_vs_grafo — registro de generación (Figura 1.2), versión 2

Figura «la misma pregunta con dos formas de consultar» para la Introducción,
con el ejemplo del préstamo: el punto 5.1.1.1 del Texto Ordenado de
Clasificación de deudores, que remite al punto 3.7 («importe de referencia»).

- Arriba, la pregunta común.
- Izquierda, «Recuperación por fragmentos», **igual que en la versión 1**: el
  punto 5.1.1.1 con su texto completo, la frase de remisión resaltada y la
  marca «recuperado · puesto 2»; el punto 3.7 en gris, con la marca «fuera de
  lo recuperado · puesto 1.523»; la línea «resto del top-5: 5.1.1.2 · 5.1.2.2
  · 5.1.2.1 · 7.4»; y debajo la respuesta que se puede redactar con lo
  recuperado y la marca de lo que falta.
- Derecha, «Consulta del grafo», sobre el grafo de desarrollo r2b: «1 ·
  Buscar» con la pregunta y la línea «BM25 sobre las etiquetas y las
  descripciones de los nodos: la Operacion queda en el puesto 3.»; «2 · Abrir
  el nodo encontrado», la `Operacion` del 5.1.1.1; «3 · Seguir las aristas»:
  la `remite_a` hasta la `Definicion` del 3.7 y las dos `condicion_de` que le
  llegan desde las `Condicion` del 5.1.1.1. Debajo, la respuesta con lo que
  esos nodos dicen.

**El lado derecho muestra el camino que el grafo pone al alcance desde el nodo
encontrado; no es la traza de una corrida del agente.** Qué nodo se abre y qué
aristas se siguen es una decisión de la figura (`NODO_ENCONTRADO`,
`ARISTAS_CONSULTA`); lo que se lee del grafo es que esos nodos y esas aristas
existen y el puesto de la búsqueda.

Tamaño impreso: **12,75 × 14,77 cm** (lienzo 860 × 996). Cruces entre
aristas: **0**.

## Versiones

- **Versión 1** (28/09/2026, U-FIG-EJEMPLO y U-FIG-EJEMPLO-AJUSTE):
  generador y PNG en `fbe69d4`; este LEEME, en `e6e6021`. Sobre KG-Reextraído-r1;
  abría la `Restriccion` del monto y seguía `referencia` hasta la
  `Obligacion` del 3.7 y `limita` hasta la `Operacion`; la búsqueda de nodos
  era la del índice de texto completo de Neo4j, copiada de
  `reports/u_med_ejemplo/` (LEEME de la versión 1, §4). sha256 en `fbe69d4`:
  generador `0e7c379d71e4cda0192e26320d4f24ad4a26dc35a3da047bcbac8309412d43ad`,
  PNG `b5306b2fbf146e20d005ce469d7de86c78c03ac3bcc95e645597760c85954533`
  (1506 × 1829 px); SVG intermedio, no versionado,
  `9b0574b7ecadcfac8675c03f64c704993238d2ec202671df2c9eab6ae5a0f706`
  (860 × 1044). En FIG-INTRO-R2B regeneré la versión 1 con su generador de
  HEAD sobre una copia y dio esos dos sha256.
- **Versión 2** (07/10/2026, FIG-INTRO-R2B). Qué cambió:
  - **la columna del grafo**: grafo de desarrollo r2b; se abre la `Operacion`
    y se siguen la `remite_a` y las dos `condicion_de` (§3);
  - **la búsqueda de nodos**: BM25 con la función de la columna de
    fragmentos, sobre etiqueta, descripción e id (§4), en lugar del índice de
    Neo4j, que esta unidad no usa;
  - **la respuesta de la derecha**: ajustada a las etiquetas de los nodos
    dibujados (§5);
  - **los nodos**: «Tipo · punto N» y la etiqueta, con los colores de tipo
    de la figura del esquema final (los de la figura 1.1, versión 2); la
    franja de cada fila de la respuesta, en el borde de ese color;
  - **la leyenda**: solo las dos clases de arista (como en la figura 1.1);
  - **las salidas**: se guardan el SVG y el PDF además del PNG;
  - **los controles**: inventario, geometría, alto máximo y pruebas
    negativas (§7).
  La pregunta, la columna de fragmentos, la respuesta de la izquierda,
  anchos, tamaños de letra y paleta no cambian (§2).

## 1. Comandos

```
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_fragmentos_vs_grafo.py
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_fragmentos_vs_grafo.py --observacion-harness
```

Escribe `figura_fragmentos_vs_grafo.svg`, `.png` y `.pdf` en
`docs/tesis/figuras/` (`--salida DIR` para otro directorio). Recalcula las dos
búsquedas en cada corrida (sin Neo4j ni API). Con `--observacion-harness`
informa además lo de §6. Importa, sin modificarlo,
`generar_figura_norma_a_grafo.py` (versión 2: textos, subgrafo, candados,
colores, nodos, leyenda, controles y exportación).

## 2. Fuentes

| Papel | Archivo | sha256 | Ancla |
|---|---|---|---|
| grafo, textos, estilo | los de la figura 1.1 versión 2 | ver su LEEME, §2 | `generar_figura_norma_a_grafo.py:105-119` |
| búsqueda BM25 | `docs/tesis/figuras/busqueda_lexica_fragmentos.py` | `13caa596ad25b9aae3e19ab5e1c4cf30821cf853418320090e2b5ed4cdbcf9d3` | `fbe69d4`; `tok_bm25` y `bm25` (:35-67), k1 = 1,2 y b = 0,75 (:30) |
| índice de la versión 1 | `data/experiment/reextraccion_v2/e0_chunking/salida_enm01/chunks_{cap,cla,ext,pro,ric}.json` | `1931138d…`, `98808886…`, `cbcd1a86…`, `d8717d1c…`, `fafebb82…` | los de `ejemplo_prestamo_datos.json` → `busqueda_fragmentos.sha256_insumos`; el generador los lee con esos candados |
| observación (§6) | `data/experiment/evaluacion/harness.py` | `fd267e833866f86850e43130e627b08d78e05523b97484696de0ab0c8c9fba9e` | `7e8b91e` |
| observación (§6) | `data/experiment/evaluacion/loader.py` | `5aba8b7a0aa46e8d5c4c83b33884b8cae7d0a099884a7d3bc935de4d3097af8b` | `2698f6f` |

Candados en el generador: `generar_figura_fragmentos_vs_grafo.py:75-84`.

**Lo que no cambia, comprobado.** Los 28 elementos del SVG de la pregunta
común y de la columna de fragmentos (x < 420, y < 657) son, uno por uno, los
del SVG de la versión 1 regenerado (comparación hecha en FIG-INTRO-R2B, fuera
del repositorio): el texto de los fragmentos sale ahora de
`salida_tanda0_r2b/chunks_cla.json`, idéntico al de la versión 1 (LEEME de la
figura 1.1, §3).

## 3. Columna de la consulta

- **Paso 1**: la pregunta y el resultado de la búsqueda de §4: la `Operacion`
  del 5.1.1.1 en el puesto 3. Si quedara fuera del top-5
  (`LIMITE_RECUPERACION`, :89, el umbral de la columna de fragmentos), el
  script frena (`busqueda_nodos`, :212-238).
- **Paso 2**: la `Operacion` «Inclusión en cartera comercial — créditos
  consumo/vivienda», punto 5.1.1.1 (`NODO_ENCONTRADO`, :98).
- **Paso 3** (`ARISTAS_CONSULTA`, :99-103; `NODOS_ALCANZADOS`, :104): la
  `remite_a` de la `Operacion` a la `Definicion` «Importe de referencia —
  nivel máximo de ventas anuales» (punto 3.7), resaltada; la `condicion_de`
  de la `Condicion` «Superar dos veces importe referencia punto 3.7» y la de
  la `Condicion` «Repago vinculado a actividad productiva/comercial» (punto
  5.1.1.1), que llegan a la `Operacion`. Cada arista sale del nodo abierto o
  llega a él por un tronco a la izquierda (`TRONCOS`, :366); el nodo de más
  arriba usa el tronco de más adentro, y por eso no se cruzan.

Las tres aristas son del subgrafo de la figura 1.1 (índices 17765, 5540 y 5161
en `kg['edges']` del grafo de desarrollo; LEEME de la figura 1.1, §5).

**El primer nodo del 5.1.1.1 que devuelve la búsqueda no es la `Operacion`**
sino la `Excepcion` «Excepción cartera comercial — créditos
consumo/vivienda», en el puesto 1, cuya única arista en el grafo es su
`establecida_en` hacia el Texto Ordenado: desde ella no se llega ni a la
`Operacion` ni al 3.7. La figura no la dibuja; el script comprueba que es la
declarada (`PRIMERO_NO_DIBUJADO`, :107) y que no tiene otra arista. Es el caso
de las excepciones sin unir del hallazgo (a) de VERIF-CAP3-COHERENCIA
(verificación de solo lectura del 07/10/2026; su paquete no está en el
repositorio). Por qué la `Excepcion` quedó sin unir: LEEME de la figura 1.1,
§6.

## 4. Las dos búsquedas

**Fragmentos** (BM25 de `busqueda_lexica_fragmentos.py` sobre los 1.763
fragmentos de `salida_enm01`, el índice de la versión 1; `busqueda_fragmentos`,
:185-202). Recalculada en cada corrida: **los puestos no cambian** respecto de
la versión 1.

| Puesto | Fragmento | Puntaje |
|---|---|---|
| 1 | cla::5.1.1.2 | 28,1501 |
| 2 | cla::5.1.1.1 | 26,1982 |
| 3 | cla::5.1.2.2 | 23,0787 |
| 4 | cla::5.1.2.1 | 22,6035 |
| 5 | cla::7.4 | 21,7776 |
| 1.523 | cla::3.7 | 1,4976 |

**Nodos** (`busqueda_nodos`, :212-238): la misma función `bm25`, con los
mismos parámetros, sobre el texto de cada nodo del grafo de desarrollo
(6.990 nodos; 6.477 con puntaje): su etiqueta, su `descripcion` y su id,
unidos por saltos de línea (`CAMPOS_NODO`, :109; `texto_nodo`, :205-209).
Ningún nodo tiene `descripcion` y `description` a la vez (el script lo
comprueba). Desempate por id ascendente, el de `bm25`.

| Puesto | Tipo | Etiqueta | Puntaje |
|---|---|---|---|
| 1 | Excepcion | Excepción cartera comercial — créditos consumo/vivienda | 48,2101 |
| 2 | Operacion | Suma de créditos para consumo o vivienda a cartera comercial para encuadramiento | 43,7280 |
| **3** | **Operacion** | **Inclusión en cartera comercial — créditos consumo/vivienda** | 40,0347 |
| 4 | Condicion | Cartera comercial o para consumo o vivienda | 40,0154 |
| 5 | Operacion | Clasificación de deudores de créditos fideicomitidos | 32,6526 |

Puestos de los demás nodos dibujados: `Condicion` del repago 666,
`Definicion` del 3.7 2.656, `Condicion` del monto 6.364. El Texto Ordenado,
que también tiene al 5.1.1.1 entre sus 143 procedencias, no tiene puntaje.
Los diez primeros, en la salida del generador.

## 5. Respuestas

Escritas a mano (`RESPUESTA_*`, :114-128); son también decisiones de
composición el umbral del top-5, el nodo que se abre, las tres aristas y la
sangría de la fila del 3.7.

- Izquierda, igual que en la versión 1: «Pasan a la cartera comercial si
  superan dos veces el importe de referencia establecido en el punto 3.7 y su
  repago depende de la actividad productiva o comercial del cliente (punto
  5.1.1.1).», con la marca «✗ el importe de referencia (punto 3.7): no
  recuperado». Lo dice el texto del 5.1.1.1, que es lo recuperado.
- Derecha: «Pasan a la cartera comercial si se cumplen las dos condiciones del
  punto 5.1.1.1:» y tres filas, cada una de la etiqueta de un nodo dibujado:
  «5.1.1.1 · superan dos veces el importe de referencia» (`Condicion` del
  monto); con sangría debajo, «3.7 · el importe de referencia es el nivel
  máximo de ventas anuales» (`Definicion`; en la versión 1 seguía «de la
  categoría Micro del sector Comercio (Ley 24.467)», que no está en la
  etiqueta); «5.1.1.1 · su repago está vinculado a la actividad productiva o
  comercial» (`Condicion` del repago; en la versión 1, «depende de la
  actividad productiva o comercial, no de ingresos fijos»). El número de
  cada fila se lee del punto del nodo.

## 6. Observación para el diseño de la navegación del agente (no se dibuja)

Con `--observacion-harness`, el generador corre `buscar_nodos` del harness
congelado (`data/experiment/evaluacion/harness.py:148-176`) con la misma
pregunta sobre el grafo de desarrollo, cargado con
`loader.load_graph_from_path` (`observacion_harness`, :241-270). Esa búsqueda
cuenta los tokens de la pregunta que están en la etiqueta o el id del nodo
(`harness.py:106-107`, `:137-139`), ordena por ese conteo, el largo de la
etiqueta y el id (`:157`) y devuelve 10 por omisión (`:148`, `:158-161`;
descripción de la tool, `:253`). El script comprueba que su orden es el de
`GraphIndex.buscar_nodos`.

- 4.804 nodos con coincidencia;
- la `Excepcion` del 5.1.1.1, en el puesto 1 (9 tokens en común);
- la `Operacion` del 5.1.1.1, en el **puesto 12** (6 tokens): **fuera de los
  10 que devuelve por omisión**;
- la `Condicion` del repago, en el 3.698 (1 token);
- la `Condicion` del monto y la `Definicion` del 3.7, **sin coincidencia**.

Queda registrado como observación para U-NAV-DISENO.

## 7. Controles y pruebas negativas

Extracto de la salida de la corrida que escribió las salidas de §9:

```
PRUEBAS NEGATIVAS: 3 de 3 hacen fallar su control
  arista_de_mas -> inventario: arista de la figura que no está en el grafo: (('Operacion', ...), 'condicion_de', ('Condicion', ...)) (fallan también: geometria)
  cruce -> geometria: 3 cruce(s) entre trazos, declarados 0: [('0', None), ('1', None), ('2', None)]
  rotulo_sobre_caja -> geometria: texto sobre la caja condicion_monto: 'remite_a' (fallan también: inventario)
INVENTARIO (releído del SVG): 4 nodos y 3 aristas; fallas: 0
GEOMETRÍA: 67 textos, 4 cajas, 10 trazos con flecha; cruces 0; fallas: 0
TAMAÑO: lienzo 860 x 996.0, impreso a 12.75 x 14.77 cm; alto de las columnas: fragmentos 528, consulta 486
```

- Inventario y geometría: los de la figura 1.1 (`controlar_inventario` y
  `controlar_geometria` de `generar_figura_norma_a_grafo.py`); 0 cruces entre
  los diez trazos con flecha (tres aristas y siete flechas de flujo y de
  leyenda).
- Alto máximo del PNG: 1850 px, el de la versión 1 (`ALTO_MAX_PNG_PX`, :153);
  la figura mide 1745.
- Pruebas negativas: `PRUEBAS_NEGATIVAS`, :556-558. Con `--perturbar <caso>`,
  sobre una copia, las tres terminan con código 1 y ningún archivo escrito;
  con `busqueda_lexica_fragmentos.py` alterado en una copia, el generador
  frena por el candado.
- Verificación geométrica de la versión 1 (`verificar_geometria_svg.py`, no
  rastreado, sha256 `fd8d062d…`): 67 textos, 4 nodos, 10 trazos con flecha;
  fallas: 0.

## 8. Tamaño

- Lienzo 860 × 996 → **12,75 × 14,77 cm** (versión 1: 860 × 1044 → 15,49 cm).
  PNG 1506 × 1745 px a 300 dpi; PDF 361,4 × 418,6 pt.
- Letra impresa a 12,75 cm: texto corrido, títulos, encabezados y nodos 17 →
  7,14 pt; marcas, pasos, rótulos, pregunta de la búsqueda y leyenda 15 →
  6,30 pt. Los mismos tamaños que la versión 1.
- Columna de la consulta: el nodo abierto, de 320 de ancho; los alcanzados,
  de 246 (`X_NODO, ANCHO_NODO`, :365), para que «condicion_de» entre en el
  tramo horizontal entre su tronco y el nodo.

## 9. Salidas (versión 2)

| Archivo | sha256 |
|---|---|
| `generar_figura_fragmentos_vs_grafo.py` | `7329c3a8e210f3106ce3eafb7be56ea0932deaee6ee575fa27dfd02f2b8874c8` |
| `figura_fragmentos_vs_grafo.svg` | `9d47fd54810f121812c590ead103116d9c86bd8004774c29708fa4ca05dbb756` |
| `figura_fragmentos_vs_grafo.png` | `15293be290b8f61aa61f0252fae04d1e8c58bae6a56ccac974866fc72ef0b49c` |
| `figura_fragmentos_vs_grafo.pdf` | `2aad5fee3747443c1c3b7ecfd15de974fc7434db8b0ecd5afa88e001f7eb5408` |

Generación determinística: las mismas salidas con `PYTHONHASHSEED` 0, 1 y
4242, sobre una copia de las fuentes.

## 10. Observaciones

- La búsqueda de nodos de la versión 2 no es la del agente evaluado: el
  servidor del grafo del banco usa el índice Lucene de Neo4j
  (`data/experiment/banco_mcp/mcp_kg/config_mcp_kg.json:4-6`, `backend`
  `neo4j`, `modo` `fulltext`) y esta unidad no usa Neo4j. Es BM25 con la misma
  función que la columna de fragmentos, sin el analizador en castellano del
  índice de Neo4j.
- **Impreso**: NO VERIFICADO.
