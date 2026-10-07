# figura_proceso_extraccion — registro de generación (Figura 1.3), versión 2

Figura «del documento al grafo» para la Introducción: el Texto Ordenado de
entrada, las cinco etapas del proceso y el grafo de salida, en dos filas
unidas por una flecha de continuidad, con la leyenda al pie.

- Fila 1: Texto Ordenado → «Segmentación en puntos» → «Extracción de
  entidades y relaciones» → «Validación contra el esquema» (**nueva**, «en
  código»).
- Fila 2: «Revisión contra el texto de origen» → «Ensamblado en un único
  grafo» («une las partes y deriva las remisiones») → «Grafo».
- Salidas laterales de la revisión, como en la versión 1: «vuelve a extraer»,
  hacia el extractor, y «marcado para revisión humana».
- El recuadro «Grafo» dibuja tres nodos de la figura 1.1 versión 2: la
  `Condicion` del monto y la `Operacion` del 5.1.1.1, unidas por
  `condicion_de`, y la `Definicion` del 3.7, con la `remite_a` resaltada.

Tamaño impreso: **12,75 × 10,93 cm** (lienzo 720 × 618). Cruces entre
flechas: **0**.

## Versiones

- **Versión 1** (28/09/2026, U-FIG-EJEMPLO y U-FIG-EJEMPLO-AJUSTE):
  generador, SVG y PNG en `fbe69d4`; este LEEME, en `e6e6021`. Cinco etapas:
  segmentación, extracción, revisión, ensamblado y «Resolución de
  remisiones»; el recuadro «Grafo», del grafo r1: `Restriccion` del 5.1.1.1
  con `limita` hacia la `Operacion` y `referencia` hacia la `Obligacion` del
  3.7. sha256 en `fbe69d4`: generador
  `6a91931abeb9927842f76fa50471497e926c69fc56617c62ef7f05ddf6c010d6`, SVG
  `168700921fa74b6b5449989408f09551372e5aee8ba0af9b4bcd44d70fe8ee5c`, PNG
  `edb4db9ee37d05f96d33bdfff6a7103e802c16caa462ce159ade8332733bc7db`;
  lienzo 720 × 665 (12,75 × 11,78 cm).
- **Versión 2** (07/10/2026, FIG-INTRO-R2B). Qué cambió:
  - **la caja del validador**, entre el extractor y el revisor, en el color de
    las etapas determinísticas: «Validación contra el esquema», «en código»;
  - **la resolución de las remisiones** deja de ser una caja propia y pasa al
    ensamblado, cuyo subtexto es «une las partes y deriva las remisiones» (en
    la versión 1, «determinístico»; el color ya lo dice);
  - **la disposición**: con una caja más, la primera fila llega hasta el
    validador y el revisor abre la segunda; sus dos salidas laterales se
    dibujan desde allí: «vuelve a extraer» sale por arriba de la revisión, a
    la izquierda de la flecha de continuidad, y entra por abajo al extractor;
    «marcado para revisión humana», debajo de la revisión (§4);
  - **el recuadro «Grafo»**: los tres nodos y las dos aristas de arriba, con
    los colores de tipo de la figura del esquema final (relleno claro, borde
    del tipo y texto oscuro; en la versión 1, color pleno con texto blanco);
  - **los controles** corren siempre (en la versión 1, la medición de textos
    corría con `--verificar`, que la versión 2 ya no acepta) y se suman el
    inventario del recuadro y la geometría de la figura 1.1 (§5);
  - **las salidas**: se agrega el PDF.
  Rótulos y subtextos de las demás etapas, salidas laterales, leyenda,
  tipografía, tamaños de letra, anchos de caja y paleta de las etapas no
  cambian.

## 1. Comando

```
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_proceso_extraccion.py
```

Escribe `figura_proceso_extraccion.svg`, `.png` y `.pdf` en
`docs/tesis/figuras/` (`--salida DIR` para otro directorio). Importa, sin
modificarlo, `generar_figura_norma_a_grafo.py` (versión 2: subgrafo y sus
candados, colores de tipo, controles y exportación).

## 2. Fuentes

| Papel | Archivo | sha256 | Ancla |
|---|---|---|---|
| grafo y estilo | los de la figura 1.1 versión 2 (grafo de desarrollo r2b, comprobado en el de diez documentos; figura del esquema final) | ver su LEEME, §2 | `generar_figura_norma_a_grafo.py:105-119` |
| esquema r2 | `data/experiment/pyd_r2/code/modelos_r2.py` | `e67f15ae13dd5419ea0ce1a08dbef63c86cbdf9c269772a0b02a4e27b4c3a2ca` | último commit `4aa92c7`; el mismo sha256 en `bbc38dc`, el commit de los dos grafos |

El generador exige en `modelos_r2.py` cinco líneas literales
(`LITERALES_R2`, `generar_figura_proceso_extraccion.py:81-87`):

| Línea | Qué respalda |
|---|---|
| :131 `("condicion_de", "Condicion", "Operacion"),` | la firma de la `condicion_de` del recuadro, en la ampliación r2 de la matriz (`AMPLIACION_R2`, :130-133) |
| :165 `PREDICADOS_DERIVADOS = ("remite_a",)` | `remite_a` es un predicado que deriva el código del ensamblado, no el extractor |
| :166-167 `TIPOS_CONTENIDO` | `Condicion` y `Definicion` están entre los tipos de su firma |
| :171 `"remite_a": (TIPOS_CONTENIDO, TIPOS_CONTENIDO + ("TextoOrdenado",)),` | la firma derivada |
| :175 `PROPIEDADES_REMISION = ("alcance", "destino", "evidencia")` | las propiedades de la arista, que el script comprueba |

La derivación de `remite_a` en el ensamblado: `git show bbc38dc:data/experiment/tanda0/code/ensamblar_tanda0.py`,
línea 1272. El validador entre el extractor y el revisor, y en código:
`docs/tesis/figuras/LEEME_figura_proceso.md:97-98` y `:108` (commit
`552e61f`), que dan sus fuentes en el código del pipeline.

## 3. Recuadro «Grafo»

Nodos (`NODOS_FIGURA`, :158-162) y aristas (`ARISTAS_FIGURA`, :166-167),
tomados del subgrafo de la figura 1.1 (`cargar_grafo`, :183-211):

| Clave | Nodo | Rótulo dibujado | id |
|---|---|---|---|
| C | condicion_monto | Condicion / punto 5.1.1.1 | `Condicion_superar_dos_veces_importe_referencia_punto_3_7__el_credito_debe_superar_el_equiv_22a312` |
| D | definicion_3_7 | Definicion / punto 3.7 | `Definicion_importe_de_referencia_nivel_maximo_de_ventas_anuales__el_nivel_maximo_del_valor__a855af` |
| OP | operacion | Operacion / punto 5.1.1.1 | `Operacion_inclusion_en_cartera_comercial_creditos_consumo_vivienda__cla_5_1_1_1_8f5956` |

| `kg['edges']` (desarrollo) | Arista | Clase | Comprobación |
|---|---|---|---|
| 5540 | C `condicion_de` OP | extracción, gris | firma en `modelos_r2.py:131`; sin `properties` |
| 5542 | C `remite_a` D | remisión, resaltada | `modelos_r2.py:165`, `:171`; `properties` `alcance`, `destino`, `evidencia` |

La `remite_a` dibujada es la de la `Condicion` del monto, la que nombra al
3.7 en su etiqueta; el grafo tiene otra, de la `Operacion` (figura 1.1). Así
las dos aristas salen del nodo de arriba, como en la composición de la
versión 1. Cada nodo se rotula con su tipo, escrito como en el código, y
«punto N» en negrita; cada arista, con el nombre de la relación tal como está
en el grafo.

## 4. Composición

- Fila 1: el documento (104 de ancho) y tres cajas de 168 (`W_DOC, W_PROC`,
  :324), separadas 22; fila 2: dos cajas de 168 y el recuadro «Grafo», de 320
  (en la versión 1, cajas de 168 y 192 y recuadro de 296).
- Flecha de continuidad: del costado derecho del validador al borde derecho,
  abajo y a la izquierda hasta la revisión (como en la versión 1, del revisor
  al ensamblado).
- «vuelve a extraer»: sale por arriba de la revisión a 30 de su borde
  izquierdo (`x_vuelta`, :464), sube entre las filas (`y_lazo`, :452), corre
  en horizontal por encima del tramo de la continuidad (`y_cont`, :453) y
  entra por abajo al extractor. La continuidad llega a la revisión más a la
  derecha, así que no se cruzan (la prueba negativa `salida_cruza` lo
  comprueba, §5).
- Recuadro «Grafo»: los dos nodos de abajo, centrados y separados 12
  (`GAP_NODOS`, :386, la separación de la versión 1); cada diagonal llega a 30
  del centro de su nodo (`ENTRADA`, :387; 16 en la versión 1), para que
  «condicion_de», más largo que «limita», entre a la derecha de su trazo
  dentro del recuadro.
- Colores de tipo de los nodos (de la figura del esquema final, como en la
  figura 1.1): `Condicion` y `Definicion` `#f8e8f5` con borde `#b5179e`,
  `Operacion` `#eaefee` con borde `#52796f`.

## 5. Controles y pruebas negativas

Extracto de la salida de la corrida que escribió las salidas de §7:

```
PRUEBAS NEGATIVAS: 2 de 2 hacen fallar su control
  arista_de_mas -> inventario: arista de la figura que no está en el grafo: (('Condicion', '5.1.1.1'), 'remite_a', ('Operacion', '5.1.1.1')) (fallan también: geometria, medidas)
  salida_cruza -> geometria: 1 cruce(s) entre trazos, declarados 0: [(None, 'vuelta')]
MEDIDAS: 42 textos medidos con las métricas reales de Helvetica; fallas: 0
INVENTARIO (releído del SVG): nodos [('Condicion', '5.1.1.1'), ('Definicion', '3.7'), ('Operacion', '5.1.1.1')]; aristas [(('Condicion', '5.1.1.1'), 'condicion_de', ('Operacion', '5.1.1.1')), (('Condicion', '5.1.1.1'), 'remite_a', ('Definicion', '3.7'))]; fallas: 0
GEOMETRÍA: 42 textos, 9 cajas, 11 trazos con flecha; cruces 0; fallas: 0
TAMAÑO: lienzo 720 x 618, impreso a 12.75 x 10.93 cm
```

- **Medidas** (`verificar_medidas`, :532-554): cada texto, con las métricas
  reales de Helvetica, entra en su caja, no sale del lienzo, no queda por
  debajo de 9 pt impresos y no se superpone con otro.
- **Inventario** (`inventario` y `controlar_inventario`, :557-602): nodos
  (tipo, punto) y aristas releídos solo del SVG contra los del grafo.
- **Geometría**: la de la figura 1.1 (`controlar_geometria`); 0 cruces entre
  los once trazos con flecha (ocho de flujo, las dos aristas y el de la
  leyenda); ningún trazo atraviesa una de las nueve cajas (las cinco etapas,
  la de revisión humana y los tres nodos; el documento y el recuadro «Grafo»
  no cuentan como cajas).
- **Pruebas negativas** (`PRUEBAS_NEGATIVAS`, :605-606). Con `--perturbar
  <caso>`, sobre una copia, terminan con código 1 y ningún archivo escrito;
  con `modelos_r2.py` alterado en una copia, el generador frena por el
  candado.
- Verificación geométrica de la versión 1 (`verificar_geometria_svg.py`, no
  rastreado, sha256 `fd8d062d…`): 42 textos, 3 nodos, 11 trazos con flecha;
  fallas: 0.

## 6. Tamaño

- Lienzo 720 × 618 → **12,75 × 10,93 cm** (versión 1: 720 × 665 → 11,78 cm).
  PNG 1506 × 1292 px a 300 dpi; PDF 361,4 × 309,8 pt.
- Letra impresa a 12,75 cm: rótulos de etapa 19 → 9,54 pt; subtextos,
  salidas, nodos y leyenda 18 → 9,04 pt (mínimo 9). Los de la versión 1.

## 7. Salidas (versión 2)

| Archivo | sha256 |
|---|---|
| `generar_figura_proceso_extraccion.py` | `f4842a6a45b624d7a123da0c423caea1fcc81c1073254d3b1fef63ab1edc5f8c` |
| `figura_proceso_extraccion.svg` | `32236e3ddcc40834b7f07d0e95a2cc0387ff5926277fc418011c3bb47cc989d5` |
| `figura_proceso_extraccion.png` | `c12808a50d76e7aae02e2a90acb96e16e3fe5d915e6699848c3e42e9e7cb9af4` |
| `figura_proceso_extraccion.pdf` | `8b2f4ea4f8ef1a994cc9e405dad51035042157acb1163f1165e9bee7cf00cd87` |

Generación determinística: las mismas salidas con `PYTHONHASHSEED` 0, 1 y
4242, sobre una copia de las fuentes.

## 8. Observaciones

- La figura de la introducción simplifica el proceso de la figura del capítulo
  4 (`figura_proceso`): no dibuja los registros de rechazos del validador ni
  la vuelta de la re-extracción por el validador; las salidas laterales de la
  revisión son las de la versión 1.
- **Impreso**: NO VERIFICADO.
