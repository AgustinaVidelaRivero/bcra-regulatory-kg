# figura_ensamblado_ejemplo — registro de generación (versión 3)

Figura «el ejemplo después del ensamblado» para la sección 4.5 de la tesis:
el fragmento de grafo del punto 5.1.1.1 de Clasificación de deudores que
muestra la figura de la salida del extractor (sección 4.2, versión 3), leído
ahora del grafo sellado de la re-extracción de la tanda 0 con el perfil r2b,
con lo que el ensamblado le agrega y sin lo que el validador rechaza.

- **Lo que ya estaba** en la figura del extractor (cinco cajas y seis de sus
  siete flechas, con sus rótulos) conserva disposición, estilo y textos: baja
  entero 134 unidades, sin otro cambio, para dejar arriba una franja nueva.
- **Lo que sale**: la `exceptua` de la excepción a la operación, que el
  validador rechaza por firma; no está en el grafo y no se dibuja (§4).
- **Lo nuevo**:
  - la caja del nodo de destino de la remisión al punto 3.7 (`Definicion`,
    «Importe de referencia — nivel máximo de ventas anuales»), en la franja
    de arriba, sobre la operación;
  - las dos `remite_a` que llegan a ella, en línea discontinua gris y
    rotuladas;
  - el umbral de la condición del monto, arriba de su caja, con la marca «≤» y
    sus campos valor, unidad, comparación y base, la comparación leída en
    castellano (§3).
- **Excluidas a propósito**: ninguna. La regla de la versión 2 sigue (no se
  dibujan las `establecida_en` derivadas de la procedencia), pero en este
  grafo no hay ninguna en el vecindario: el extractor devolvió las cuatro.
- **Sin color ni leyenda.**

Alto impreso a 15 cm de ancho: **9,35 cm** (lienzo 850 × 530; PDF
425,2 × 265,1 pt; PNG 1772 × 1105 px a 300 dpi). Cruces entre flechas: **0**.

## Versiones

- **Versión 1** (04/10/2026, sin commit, aprobada con 2 correcciones):
  dibujaba las dos `establecida_en` derivadas (con un cruce) y la comparación
  con su valor interno. sha256 del generador
  `4d8c9064776e6708252ac3635ff9ca98058604aa52a5a29060c72904ae2d0cb9`; el
  resto, en el LEEME de la versión 2.
- **Versión 2** (04/10/2026, commit `ef70976`): sobre KG-Tanda0-Desarrollo-r2a
  (sha256 `93a7af7279a415ee72cfec547bcd080d4c85a96746e219ed94dea4239007e8dd`)
  y la figura del extractor versión 2; 7 nodos, 9 aristas, 2 excluidas, 0
  cruces, 8,93 cm. sha256: generador
  `77801c9598efd1e3ec53602c0742f7bfe5b8db23a2ee96d3b2bfe7c695b1d434`, SVG
  `c1078dc3716b1aaf70a75146d807b56f9fc9a886663250a8c0ccd53a20e0f67b`, PNG
  `0b487134f3f251c344994879226e0d727aecb8024ccb8be31ce3a4fbe8d468c0`, PDF
  `c10295ed83e3c686edd7ed4e87b43a15f0d7fa48ca6ea58a548919d0669899f4`, LEEME
  `7397d13b8c2fb81e1eaab7c48c4642e30b591342ff2f1c849e8a91bd586eb63a`
  (`git show ef70976:docs/tesis/figuras/<archivo>`). **En HEAD ese generador
  ya no corre**: frena porque `reglas_comparacion.py` cambió después
  (`9f6361e`; §3).
- **Versión 3** (06/10/2026). Qué cambió:
  - **el grafo**: KG-Tanda0-Diez-r2b (§1) en lugar de
    KG-Tanda0-Desarrollo-r2a;
  - **la figura de la que parte**: la del extractor versión 3 (§2), con otra
    disposición; lo nuevo se acomoda a ella (§6): el nodo del 3.7 pasa a la
    izquierda, sobre la operación, y el umbral queda en el centro, sobre la
    condición del monto;
  - **lo que cambia en el grafo respecto de la figura del extractor**: una
    relación retirada (la `exceptua`), ninguna etiqueta cambiada (§4);
  - **ninguna relación excluida** (`EXCLUIDAS` vacía) y, en consecuencia, la
    prueba negativa `excluida_dibujada` pasa a ser `retirada_dibujada`:
    dibuja la `exceptua` retirada y tiene que hacer fallar el inventario
    (§8);
  - **`reglas_comparacion.py`** entra con el candado de la versión con la que
    se ensambló el grafo y la tabla de lecturas cita sus líneas nuevas (§3);
  - las pruebas negativas heredadas de la figura del extractor usan sus
    relaciones nuevas (`EX.RELACION_DE_MAS`, `EX.perturbar_ruta`,
    `EX.ROTULO_SOBRE_CAJA`);
  - estilo, el resto de los controles, letra, márgenes y determinismo, sin
    cambios.

## 1. Fuente: el grafo

`data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2b/r2/kg.json`,
sha256 `a9631a64b422bdae634fb05135373c6f04c6272cdf7acd43a1be9f5b6c1f5f57`
(8.816 nodos, 27.632 aristas). **Sellado**: lo commitea `bbc38dc` (T3-bis de
U-REEXT-T0), el último de los dos commits que tocan el archivo (el anterior,
`c499eb3`, es el ensamblado de T3, rehecho en T3-bis), y lo registra
`data/experiment/neo4j/grafos.py:134-147` (KG-Tanda0-Diez-r2b, `sha256` y
`commit_sellado` `bbc38dc`; sello en `c9540c0`). Su reporte de ensamblado
(`ens_diez_r2b/r2/reporte_ensamblado_r2.json`) declara `"fase": "r2b"`,
`"perfil_e1_del_crudo": "r2b"`, `"prefijo_hash": "322c5a23e9b7"` y como
entrada `corpus_tanda0/salida_r2b`, la corrida que dibuja la figura del
extractor.

**El vecindario** (las aristas que tienen a `cla::5.1.1.1` entre sus
procedencias y sus extremos): **6 nodos y 8 aristas**, las 8 dibujadas. El
generador frena en los mismos casos que la versión 2 (nodo solo de la unidad
con aristas fuera del vecindario, nodo de la unidad sin aristas, extremo
ajeno que no es solo destino de una `remite_a` con ese `destino`, excluidas
distintas de las declaradas); en este grafo no se da ninguno.

| Rol | Nodo | Procedencias |
|---|---|---|
| `e1` | `Operacion` «Inclusión en cartera comercial — créditos consumo/vivienda» | 1, solo la unidad |
| `e2` | `Excepcion` «Excepción cartera comercial — créditos consumo/vivienda» | 1, solo la unidad |
| `e3` | `Condicion` «Superar dos veces importe referencia punto 3.7» | 1, solo la unidad |
| `e4` | `Condicion` «Repago vinculado a actividad productiva/comercial» | 1, solo la unidad |
| nodo del 3.7 | `Definicion` «Importe de referencia — nivel máximo de ventas anuales» | 1, `cla::3.7` |
| `to` | `TextoOrdenado` «Texto Ordenado Clasificación de Deudores» | 143 |

**El mismo vecindario en el grafo de desarrollo.** En KG-Tanda0-Desarrollo-r2b
(`ens_desarrollo_r2b/r2/kg.json`, sha256
`6e7560433148cfe0c476cdd61199c32278187c4196d6f90dc0a38976a6d8e9a2`) el
vecindario de la unidad tiene los mismos 6 nodos y 8 aristas, con los mismos
tipos, etiquetas y propiedades: la figura sería la misma con cualquiera de
los dos.

## 2. Fuente: la figura del extractor

El generador recompone la figura del extractor con su generador,
`generar_figura_extractor_ejemplo.py` (sha256
`1cc39e337a0137e7910f65c6ee109592a3a09d289c7a3b02b7a36f55d6755c2a`), que lee
su registro con su candado (su LEEME, §1). El SVG recompuesto tiene que ser
byte a byte el registrado en su LEEME §9,
`9a393b325cae953f3da697658cb435fdace001cf91cb8eee1ea28980b7dfe64d`; si no lo
es, el generador frena.

## 3. Qué agrega el ensamblado y el umbral

De las 8 aristas del vecindario, 6 son de la figura del extractor
(conservadas) y 2 son nuevas, las `remite_a`, ambas con `properties`
`alcance` `interna`, `destino` `cla::3.7` y la misma `evidencia`. Ninguna
arista del vecindario lleva `rol_fuente` (no hay derivadas) ni
`no_verificada_e3`. `derivar_establecida_en`
(`data/experiment/tanda0/code/ensamblar_tanda0.py:592-608`, igual en
`bbc38dc`) solo deriva la `establecida_en` de un nodo de contenido que no
tiene ninguna.

**El umbral** de `e3`, la única entrada de `properties.umbrales` del
vecindario:

| Campo en el grafo | Rótulo en la figura | Valor interno | En la figura |
|---|---|---|---|
| `valor` | valor | `2` | 2 |
| `unidad` | unidad | `veces` | veces |
| `comparacion` | comparación | `minimo_estricto` | mayor que |
| `base` | base | `importe de referencia establecido en el punto 3.7` | ídem, en dos líneas |

No se dibujan `tramo` («dos veces»), `regla_comparacion`
(`simple:raiz_super`), `origen` (`e1`), `tramo_verificado` (`exacta`),
`base_destino` (`cla::3.7`) ni `base_via` (`remision`).

**Tabla de lecturas** (`LECTURA_COMPARACION`). Sale del docstring de
`data/experiment/pyd_r2/code/reglas_comparacion.py`, sha256
`69c48d24387bcb788925cd1513496e015b7594f0469124f45f5082f3465b9d79` (último
commit `9f6361e`; igual en `bbc38dc`, el commit del grafo, y en el árbol). La
versión 2 lo leía en `57a8dd2`
(`0cd2afbf7356e3674cbe54daf367ea5c55353b8be326551fea28ed1ece3db821`). Las
lecturas no cambian; cambian las líneas:

| Valor interno | Lectura | Definición (`reglas_comparacion.py`) |
|---|---|---|
| `minimo_estricto` | mayor que | :15-18 |
| `maximo_estricto` | menor que | :18 |
| `minimo_inclusivo` | mayor o igual que | :40-42 |
| `maximo_inclusivo` | menor o igual que | :42-43 |
| `igual` | igual a | :52-53 |
| `coeficiente` | coeficiente | :11-12 |
| `no_determinada` | no determinada | :68 |

```
for c in $(git log --format=%h -- data/experiment/pyd_r2/code/reglas_comparacion.py); do echo "$c $(git show "${c}:data/experiment/pyd_r2/code/reglas_comparacion.py" | shasum -a 256 | cut -c1-12)"; done
```

## 4. Qué cambió de lo que ya estaba

- **Una relación retirada**: `e2` `exceptua` `e1`. El validador la rechaza
  por firma (`firma_invalida`, `Excepcion --exceptua--> Operacion`; LEEME de
  la figura del extractor, §2) y el grafo no la tiene. El control de
  conservación la declara y descuenta su camino, su punta y su rótulo.
- **Ninguna etiqueta cambiada**: las cinco cajas que comparten las dos figuras
  tienen la misma etiqueta en la salida del extractor y en el grafo, también
  el Texto Ordenado.
- **Lo que no se dibuja** del nodo del 3.7: sus otras 33 aristas (32
  `remite_a` desde otras unidades y 1 `establecida_en`, de `cla::3.7`); del
  Texto Ordenado, sus otras 564 aristas (568 en total, 4 de la unidad). El
  nodo del Texto Ordenado lleva además en sus `properties` la marca de la
  cola humana del documento (`cola_humana`, con tres unidades en
  `cola_chunks`, ninguna de ellas `cla::5.1.1.1`); no se dibuja.

## 5. Estilo

Sin cambios respecto de la versión 2: lo que ya estaba, con el estilo de la
figura del extractor; `remite_a` en `#8a8a8a`, grosor 1,6, discontinuo `7 5`;
la marca de umbrales (18 × 18, `#3d3d3d`, «≤» blanco); el panel con nombres
en Menlo y valores en Helvetica de 15 (7,50 pt). Todo leído de
`figura_esquema_final.svg` (sha256
`dfdb16d471bb93c6351aa03b1e609452b75c428baa354c52354ce1dfe9797bb3`).

## 6. Disposición

**Lo que ya estaba baja 134** (alto de caja 76 más la calle de 58). Arriba:

- **el nodo del 3.7**, en (14, 14), sobre la operación (`LUGAR_NUEVOS`);
- **el panel del umbral**, arriba de la condición del monto: la marca en
  (310, 27), los nombres en x = 336 y los valores en x = 445,33; la base en
  dos líneas; la última línea a 35 del borde superior de la caja (el panel
  queda a 31,7 de ella).

| Relación | Puntos | Rótulo |
|---|---|---|
| operación `remite_a` 3.7 | (60, 282) → (60, 90) | derecha, en la calle de arriba |
| condición del monto `remite_a` 3.7 | (310, 164) → (277, 164) → (277, 52) → (244, 52) | izquierda, en la calle de arriba |

La `remite_a` de la operación sube recta, a la izquierda de la `condicion_de`
que le llega; la de la condición del monto sale por su lado izquierdo, 22 por
encima de su `condicion_de`, sube por el hueco entre columnas y entra de
costado al nodo del 3.7. **Cruces: 0** (`CRUCES_DECLARADOS` vacío).

## 7. Controles

Salida de la corrida que escribió las salidas del repo (extracto):

```
INVENTARIO (releído del SVG): 6 cajas y 8 relaciones contra 6 y 8 del vecindario (8 aristas, 0 excluidas a propósito); fallas: 0
CONTENIDO: 36 textos, 29 piezas; fallas: 0
TEXTOS: 36 textos contra 6 cajas y 8 flechas; distancias mínimas texto-texto 3.0; rótulo-su flecha 4.0; rótulo-otra flecha 39.8; texto-borde de su caja 9.0; fallas: 0
CAJAS: 6 cajas; fallas: 0
TRAZOS: 16 tramos en el SVG; fallas: 0
FLECHAS: 8 flechas; fallas: 0
CRUCES: 0 cruce(s) entre flechas, declarados 0; fallas: 0
MARGEN: 50 elementos y la marca del umbral; mínimo a cada borde izquierdo 12.7 u = 2.24 mm, superior 12.7 u = 2.24 mm, derecho 13.0 u = 2.29 mm, inferior 14.0 u = 2.47 mm; marca 27.0 u; exigido 2.0 mm (11.3 u); fallas: 0
CONSERVACION: 38 de 41 elementos de la figura del extractor iguales (bajados 134); cambios declarados 1; fallas: 0
REMISIONES: 2 flechas discontinuas; fallas: 0
UMBRAL: campos [['valor', '2'], ['unidad', 'veces'], ['comparación', 'mayor que'], ['base', 'importe de referencia establecido en el punto 3.7']]; a 31.7 de su caja; a 33.7 de la flecha más cercana; fallas: 0
REGISTRO: 49 elementos de primer nivel del SVG; fallas: 0
LETRA 15 unidades -> 7.50 pt impresos a 15 cm
LETRA 19 unidades -> 9.50 pt impresos a 15 cm
ALTO: lienzo 850 x 530, impreso a 15.00 x 9.35 cm
```

Conteos:

- conservación: 41 elementos de la figura del extractor, 38 iguales; los 3 que
  faltan son el camino, la punta y el rótulo de la `exceptua` retirada;
- 49 elementos de primer nivel = 8 caminos + 8 puntas + 6 cajas + 26 textos (6
  tipos, 12 líneas de etiqueta, 8 rótulos) + el grupo del umbral;
- 36 textos controlados = esos 26 + 10 del panel (la marca, 4 nombres, 5
  líneas de valor); 29 piezas = 6 tipos + 6 etiquetas + 8 rótulos + la marca +
  4 nombres + 4 valores;
- 16 tramos = 13 de la figura del extractor − 1 de la `exceptua` + 1 de la
  `remite_a` de la operación + 3 de la de la condición;
- 50 elementos del margen = 36 textos + 6 cajas + 8 flechas.

## 8. Pruebas negativas

```
PRUEBAS NEGATIVAS: 10 de 10 hacen fallar su control
  relacion_de_mas -> inventario: relación de la figura que no está en el grafo o está excluida: (('Excepcion', 'Excepción cartera comercial — créditos consumo/vivienda'), 'regula', ('Condicion', 'Repago vinculado a actividad productiva/comercial')) (fallan también: textos)
  entidad_de_menos -> inventario: flecha de (60.0, 282.0) a (60.0, 90.0): 1 caja(s) de origen y 0 de destino (fallan también: contenido, flechas)
  rotulo_sobre_caja -> textos: 'establecida_en': se superpone con la caja de to (fallan también: conservacion, inventario)
  tramo_diagonal -> trazos: tramo diagonal de (244, 320) a (606, 350) (fallan también: conservacion, inventario, textos)
  cruce_de_flechas -> cruces: 1 cruce(s) entre flechas, declarados 0: [(('e1', 'establecida_en', 'to'), ('e4', 'condicion_de', 'e1'))] en (330.0, 320.0) (fallan también: conservacion)
  remite_continua -> remisiones: camino 8 (M 310 164 L 277 164 L 277 52 L 244 52): discontinuo None, rótulo ['remite_a']
  umbral_campo_de_menos -> umbral: campos del panel [...] ≠ del grafo [...] (fallan también: contenido)
  umbral_lejos -> umbral: el panel no está junto a su caja: debajo de su centro [], esperada ('Condicion', 'Superar dos veces importe referencia punto 3.7') a 40 o menos (fallan también: margen, textos)
  caja_movida -> conservacion: elemento de la figura del extractor que no está (bajado 134): rect '' {... 'x': '310', 'y': '148'} (fallan también: flechas, inventario)
  retirada_dibujada -> inventario: relación de la figura que no está en el grafo o está excluida: (('Excepcion', 'Excepción cartera comercial — créditos consumo/vivienda'), 'exceptua', ('Operacion', 'Inclusión en cartera comercial — créditos consumo/vivienda')) (fallan también: conservacion)
```

`retirada_dibujada` reemplaza a `excluida_dibujada`: sin relaciones excluidas
en el grafo, la de la versión 2 no tenía qué dibujar; la nueva dibuja la
relación retirada con su recorrido de la figura del extractor, y el
generador frena si esa relación no es una retirada. Con `--perturbar <caso>`,
sobre una copia, los diez casos terminan con «FALLA: la figura tiene
defectos; no se escribe nada», código 1 y ningún archivo en el directorio de
salida. Con un `--sha256-grafo` que no es el del archivo, el generador frena,
código 1.

## 9. Reproducibilidad

Tres corridas sobre copias en el scratchpad de los ocho archivos que usan
este generador y el de la figura del extractor (los cuatro generadores,
`figura_esquema_final.svg`, el registro, el grafo y `reglas_comparacion.py`;
copiados, sin enlaces), con `PYTHONHASHSEED` 0, 1 y 4242: los mismos SVG, PNG
y PDF, iguales a los del repo, y la misma salida salvo la ruta. sha256 de los
archivos rastreados del repo iguales antes y después de esas corridas; la
corrida que escribió en el repo cambió solo los tres archivos de la figura.

## 10. Salidas (versión 3)

| Archivo | sha256 |
|---|---|
| `generar_figura_ensamblado_ejemplo.py` | `3d377e81cad060f2265fa0b08914f7adcc26dde1342fd63973566ea44ace808d` |
| `figura_ensamblado_ejemplo.svg` | `992fce81078cbf7162ab36c6f84e926f9726e66e4f24bf55e1f8ff513f5e0b53` |
| `figura_ensamblado_ejemplo.png` | `b95fe22932ae9c972ca43f9dc75406a51b0d76cf02821861244ccc32456b7773` |
| `figura_ensamblado_ejemplo.pdf` | `026f11c1b5b6356cbca903404483baf61c612f3d670d9af8ca2e94a53a6bd961` |

PDF con `/CreationDate` fijada por `SOURCE_DATE_EPOCH=0`; stream de contenido
sha256 `0055289af3d09128adf527acd6421fd69122c82f38bcb1a0bce7c0f9c8b0f816`.

```
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_ensamblado_ejemplo.py
```

Este LEEME cae en `.gitignore:180` y entra solo con `git add -f`.

## 11. Regenerar con otro grafo

```
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_ensamblado_ejemplo.py --grafo <kg.json> --sha256-grafo <sha256>
```

Una ruta distinta de la de omisión sin su sha256 frena. Con otro grafo, lo
esperable es declarar de nuevo roles (`NUEVOS`, `LUGAR_NUEVOS`), rutas
(`rutas_nuevas`), relaciones excluidas y cruces; los controles comprueban lo
que se declare. Los conteos de este LEEME son de este grafo.

## 12. Observaciones

- **Impreso**: NO VERIFICADO; la letra mínima (7,50 pt) y el margen (2,24 mm)
  se controlan sobre la geometría.
- **Grafo de diez o de desarrollo**: la figura lee el de diez documentos; el
  vecindario es el mismo en el de desarrollo (§1).
