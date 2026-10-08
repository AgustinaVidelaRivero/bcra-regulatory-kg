# figura_extractor_ejemplo — registro de generación (versión 3)

Figura «la salida del extractor para el ejemplo» para la sección 4.2 de la
tesis: lo que devolvió el extractor para la unidad del punto 5.1.1.1 de
Clasificación de deudores en la re-extracción de la tanda 0 con el perfil
final (r2b), antes del validador, dibujado como un fragmento de grafo.

- **Una caja por entidad** de la salida cruda (cinco), con su tipo en negrita
  y su etiqueta debajo.
- **Una flecha por relación** (siete), de origen a destino, rotulada con su
  nombre; solo tramos horizontales y verticales, **sin cruces (0)**. Entre
  ellas está la `exceptua` de la excepción a la operación, que el validador
  rechaza (§2): se dibuja como las demás, sin marca.
- **Sin sujeto**: la salida no trae ninguna relación con un sujeto, así que
  no hay caja de sujeto y el catálogo no se lee.
- **Estilo** de la figura del esquema final (sección 3.10, versión 3), como
  en la versión 2. **Sin panel de la unidad, sin marcas y sin leyenda.**

Alto impreso a 15 cm de ancho: **6,99 cm** (lienzo 850 × 396; PDF
425,2 × 198,1 pt; PNG 1772 × 826 px a 300 dpi). Cruces entre flechas: **0**.

## Versiones

- **Versión 1** (03/10/2026, sin commit, reemplazada): el formato de la figura
  de la ficha. sha256 del generador
  `a20c997ec0bcea6a9c9cafa502dd5862a3cc3f6ef900818df4e4f99f6661ff51`; el
  resto, en el LEEME de la versión 2.
- **Versión 2** (04/10/2026, commit `5582c41`): el fragmento de grafo sobre la
  salida del perfil del esquema congelado (`v3_b54`), registro
  `corpus_tanda0/salida/cla/extracciones_e1.jsonl:61` (sha256
  `1d3baa2349a1298e68748126522b78b079d1b4569cbaa6789624c4399273f1f1`): seis
  cajas (cinco entidades y un sujeto), cinco flechas, 0 cruces, 6,56 cm.
  sha256: generador
  `7cc8cc1106412e79c99a23c70887d46cf5b5e85354766f8c734d1fcb021bd5a5`, SVG
  `46e6cb24bd397eaa8d6d6a1ba3a83ba329ff8a0739e2cf319bd10feea6e9fac5`, PNG
  `f01d64cdc6919353919e9c55026a663cf7df60f158d67d27d0ce04d9defd6086`, PDF
  `6b6073a579e2273cdd8fd136cddf793d424d2ab810981a133ab3637b136b9ff1`, LEEME
  `397854b45c2c4c480d58461221b89c22bad3693e3465b6f93c8e999d83c61f1f`
  (`git show 5582c41:docs/tesis/figuras/<archivo>`).
- **Versión 3** (06/10/2026). Qué cambió:
  - **la fuente**: el registro de E1 de la re-extracción de la tanda 0 con el
    perfil r2b (§1) en lugar del de `v3_b54`;
  - **el contenido**, porque cambió la salida: cinco entidades (entra una
    `Excepcion`, sale la `Definicion`), siete relaciones (cuatro
    `establecida_en`, dos `condicion_de` y una `exceptua`) y ningún sujeto;
  - **la disposición** (§4): la operación y el Texto Ordenado, a los que
    llegan las otras tres entidades, en la fila del medio; las rutas pasan a
    tener codos y su rótulo un lugar declarado (`rutas_declaradas`);
  - **los cambios mínimos del generador para leer el registro r2b**: las
    claves de la forma r2 (`omisiones` en la salida; `tramo` y `umbrales` en
    las entidades) se aceptan, no se dibujan y el script las informa
    (`NO_DIBUJADAS_SALIDA`, `NO_DIBUJADAS_ENTIDAD`); el catálogo se lee solo
    si alguna relación llega a un sujeto; el alto del lienzo cuenta también
    los puntos de las flechas (la `establecida_en` de la excepción corre por
    debajo de la fila de abajo); el script imprime el sha256 de la línea del
    registro;
  - **las pruebas negativas** son las mismas cinco, sobre relaciones de este
    registro (§8): las de la versión 2 usaban la `aplica_a` del sujeto, que
    esta salida no tiene;
  - estilo, controles, letra, márgenes y determinismo, sin cambios.

## 1. Fuente de la extracción

**El registro.** `data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b/cla/extracciones_e1.jsonl:61`,
archivo con sha256
`47bf7b584902fe396cc14a291f56fb61237c21a4ab8bd546422eb0a63d5fde59` (commit
`3d793aa`, T2 de U-REEXT-T0, el único que toca el archivo; sin cambios en el
árbol); la línea 61, con su salto de línea, tiene sha256
`9f60ec6e7246112aa68bb0a7f0b31fbb14b791d50369aa31c7d749d89d336c32`. La
figura dibuja su campo `tool_input_crudo`: la salida de la tool tal como la
devolvió el modelo, antes del validador. Registro sin error, `stop_reason`
`tool_use`, 1.353 tokens de salida.

**La corrida.** Namespace
`e1_extraccion|cv=e1-extractor-v1-p322c5a23e9b7|think=0`
(`corpus_tanda0/salida_r2b/cla/resumen_e1.json:24`); el reporte del grafo que
se ensambla con esta salida declara `"perfil_e1_del_crudo": "r2b"` y
`"prefijo_hash": "322c5a23e9b7"`
(`corpus_tanda0/ens_diez_r2b/r2/reporte_ensamblado_r2.json`). Sin reintento:
`corpus_tanda0/salida_r2b/cla/finales.jsonl:61`, `"n_reintentos": 0`, estado
`aceptado_con_residuales`.

**Es el único registro de esa corrida para la unidad.** En
`corpus_tanda0/salida_r2b/` hay dos líneas con un `tool_input_crudo` de
`cla::5.1.1.1`: esta y la de `extracciones_e1_compact.jsonl`, con el mismo
`tool_input_crudo` y el mismo orden de claves.

```
shasum -a 256 data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b/cla/extracciones_e1.jsonl
sed -n 61p data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b/cla/extracciones_e1.jsonl | shasum -a 256
grep -rc '"chunk_id": "cla::5.1.1.1".*"tool_input_crudo"' data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b/cla/
```

## 2. Qué trae la salida y qué rechaza el validador

| Local | Tipo | Etiqueta | Tramo |
|---|---|---|---|
| `to` | `TextoOrdenado` | Texto Ordenado Clasificación de Deudores | (sin tramo) |
| `e1` | `Operacion` | Inclusión en cartera comercial — créditos consumo/vivienda | «Los créditos de esta clase que superen […] se incluirán dentro de la cartera comercial.» (el párrafo entero) |
| `e2` | `Excepcion` | Excepción cartera comercial — créditos consumo/vivienda | «Los créditos para consumo o vivienda.» |
| `e3` | `Condicion` | Superar dos veces importe referencia punto 3.7 | «superen el equivalente a dos veces el importe de referencia establecido en el punto 3.7» |
| `e4` | `Condicion` | Repago vinculado a actividad productiva/comercial | «cuyo repago no se encuentre vinculado a ingresos fijos o periódicos del cliente sino a la evolución de su actividad productiva o comercial» |

Relaciones, en el orden de la salida: `e1`, `e2`, `e3` y `e4`
`establecida_en` `to`; `e3` y `e4` `condicion_de` `e1`; `e2` `exceptua` `e1`.

**El rechazo.** El validador rechaza una, la última:
`validacion.rechazos` de la línea 61 = `firma_invalida`, «relations[6]:
Excepcion --exceptua--> Operacion». La matriz de firmas del perfil r2 admite
`exceptua` solo de `Excepcion` a `Restriccion`
(`data/experiment/pyd_r2/code/modelos_r2.py:120`); la ampliación r2 agrega
solo `condicion_de` hacia `Operacion` y `Potestad` (`:130-133`), y por eso
las dos `condicion_de`, que la versión 2 veía rechazadas con `v3_b54`, ahora
pasan. Métricas de la validación: 5 entidades y 7 relaciones de entrada, 5 y
6 de salida.

**Lo que no se dibuja** (el script lo imprime en cada corrida): la omisión
`meta_normativo` sobre «Los créditos para consumo o vivienda.», los `tramo`,
el `punto` («5.1.1.1» en todas), las `properties` y la lista `umbrales` de
`e3` (un elemento con solo su tramo; `e2` y `e4` la traen vacía). Ninguna
etiqueta se abrevia.

```
sed -n 61p data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b/cla/extracciones_e1.jsonl | PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B -c "import json,sys;r=json.loads(sys.stdin.read());print(r['validacion']['rechazos']);print(r['validacion']['metricas'])"
```

## 3. Estilo

Sin cambios respecto de la versión 2: se lee de
`docs/tesis/figuras/figura_esquema_final.svg` (versión 4, sha256
`d550719599872f47fc8a7dbee261a6c11e5ab186e0e8fad76f281e3c220eedfa`; hasta el
08/10/2026, la versión 3, commit `8edd732`, sha256 `dfdb16d4…`, con el mismo
estilo de cajas, tipos, rótulos y flechas, §12). Para los tipos de este registro:

| Tipo | Relleno | Borde | Grosor |
|---|---|---|---|
| `Condicion` | `#f8e8f5` | `#b5179e` | 2,6 |
| `Excepcion` | `#fbefe7` | `#e07b39` | 2 |
| `Operacion` | `#eaefee` | `#52796f` | 2 |
| `TextoOrdenado` | `#e8e8e8` | `#3d3d3d` | 2 |

Esquinas de 6. Tipos en Menlo negrita de 19 (9,50 pt); rótulos en Menlo de 15
(7,50 pt), gris `#6f6f6f`, con halo blanco; flechas `#8a8a8a` de 1,6;
etiquetas en Helvetica de 15 (7,50 pt). Todos los rótulos en gris: la figura
no marca nada.

## 4. Disposición

Tres filas sobre tres columnas de cajas de 230 × 76, más un canal de 24 debajo
de la fila de abajo:

- arriba, en el centro, la condición del monto;
- al medio, la operación (izquierda) y el Texto Ordenado (derecha), unidos por
  su `establecida_en`, recta;
- abajo, la excepción (debajo de la operación) y la condición del repago (en
  el centro).

La operación y el Texto Ordenado son los dos extremos a los que llegan las
otras tres entidades. Cada una llega a los dos por lados distintos, así que
ninguna flecha cruza otra:

| Relación | Puntos | Rótulo |
|---|---|---|
| condición del monto `condicion_de` operación | (310, 52) → (129, 52) → (129, 148) | derecha, en la calle |
| condición del monto `establecida_en` Texto Ordenado | (540, 52) → (721, 52) → (721, 148) | izquierda, en la calle |
| operación `establecida_en` Texto Ordenado | (244, 186) → (606, 186) | arriba |
| condición del repago `condicion_de` operación | (330, 282) → (330, 206) → (244, 206) | derecha, en la calle |
| condición del repago `establecida_en` Texto Ordenado | (520, 282) → (520, 206) → (606, 206) | derecha, en la calle |
| excepción `exceptua` operación | (129, 282) → (129, 224) | derecha |
| excepción `establecida_en` Texto Ordenado | (129, 358) → (129, 382) → (721, 382) → (721, 224) | izquierda, a la altura de la fila de abajo |

La disposición es la de este registro (`DISPOSICION` y `rutas_declaradas`,
por identificador local): si el registro trae una entidad, un sujeto o una
relación sin lugar declarado, el generador frena.

**La lee la figura del ensamblado**: lo que comparten las dos figuras está en
el mismo lugar, para que se lean una contra otra (su LEEME, §6).

## 5. Reutilización

`generar_figura_esquema_final.py` (versión 4, sha256
`4ab76a71dae84f29f246b1ee5b27af5b143565a78d62962918335aa3ca1a086d`; hasta el
08/10/2026, la versión 3, `0d6274fe…`) y, de `generar_figura_norma_a_grafo.py`
(sha256 `618789ae333e17e0cb7ba1d9baf0d3d006e3f50745869de8bcffd5b487dde67c`,
`medidor`, :806), el medidor de Helvetica, importados sin modificarlos. Hasta
el 08/10/2026 el medidor se pedía a `generar_figura_proceso_extraccion.py`
(sha256 `6a91931a…`), que lo dejó de tener en `88bfe89` (§12).

## 6. Controles

Salida de la corrida que escribió las salidas del repo (extracto):

```
INVENTARIO (releído del SVG): 5 cajas y 7 relaciones contra 5 y 7 del registro; fallas: 0
CONTENIDO: 22 textos, 17 piezas; fallas: 0
TEXTOS: 22 textos contra 5 cajas y 7 flechas; distancias mínimas texto-texto 3.0; rótulo-su flecha 4.0; rótulo-otra flecha 39.8; texto-borde de su caja 9.0; fallas: 0
CAJAS: 5 cajas; fallas: 0
TRAZOS: 13 tramos en el SVG; fallas: 0
FLECHAS: 7 flechas; fallas: 0
CRUCES: 0 cruce(s) entre flechas, declarados 0; fallas: 0
MARGEN: 34 elementos; mínimo a cada borde izquierdo 13.0 u = 2.29 mm, superior 12.7 u = 2.24 mm, derecho 13.0 u = 2.29 mm, inferior 14.0 u = 2.47 mm; exigido 2.0 mm (11.3 u); fallas: 0
REGISTRO: 41 elementos del SVG; fallas: 0
LETRA 15 unidades -> 7.50 pt impresos a 15 cm
LETRA 19 unidades -> 9.50 pt impresos a 15 cm
ALTO: lienzo 850 x 396, impreso a 15.00 x 6.99 cm (cajas de 230 x 76)
```

Conteos:

- 22 textos = 5 tipos + 10 líneas de etiqueta (las cinco en dos líneas) + 7
  rótulos; 17 piezas = 5 tipos + 5 etiquetas + 7 rótulos;
- 41 elementos = 7 caminos + 7 puntas + 5 cajas + 22 textos;
- 13 tramos = 2 + 2 (condición del monto) + 1 (operación) + 2 + 2 (condición
  del repago) + 1 + 3 (excepción);
- 34 elementos del margen = 22 textos + 5 cajas + 7 flechas.

## 7. Pruebas negativas

```
PRUEBAS NEGATIVAS: 5 de 5 hacen fallar su control
  relacion_de_mas -> inventario: relación de la figura que no está en el registro: (('Excepcion', 'Excepción cartera comercial — créditos consumo/vivienda'), 'regula', ('Condicion', 'Repago vinculado a actividad productiva/comercial')) (fallan también: contenido, textos)
  entidad_de_menos -> inventario: flecha de (244.0, 186.0) a (606.0, 186.0): 0 caja(s) de origen y 1 de destino (fallan también: contenido, flechas)
  rotulo_sobre_caja -> textos: 'establecida_en': se superpone con la caja de to (fallan también: inventario)
  tramo_diagonal -> trazos: tramo diagonal de (244, 186) a (606, 216) (fallan también: inventario, textos)
  cruce_de_flechas -> cruces: 1 cruce(s) entre flechas, declarados 0: [('condicion_de (6)', 'establecida_en (1)')] en (330.0, 186.0)
```

Las relaciones que plantan (`RELACION_DE_MAS`, `RUTA_CON_CRUCE`,
`RUTA_DIAGONAL`, `ROTULO_SOBRE_CAJA`, `perturbar_ruta`) las reutiliza la
figura del ensamblado. Con `--perturbar <caso>`, sobre una copia, los cinco
casos terminan con «FALLA: la figura tiene defectos; no se escribe nada»,
código de salida 1 y ningún archivo en el directorio de salida. Con un
`--sha256` que no es el del archivo, el generador frena («no es el
verificado»), código 1, sin escribir nada.

## 8. Reproducibilidad

Tres corridas sobre copias en el scratchpad de los ocho archivos que usan
este generador y el de la figura del ensamblado (los cuatro generadores,
`figura_esquema_final.svg`, el registro, el grafo y `reglas_comparacion.py`;
copiados, sin enlaces: 0 enlaces en cada copia), con
`PYTHONHASHSEED` 0, 1 y 4242: las tres dan los mismos SVG, PNG y PDF,
idénticos a los del repo, y la misma salida salvo la ruta. sha256 de los
archivos rastreados del repo iguales antes y después de las tres corridas; la
corrida que escribió en el repo cambió solo los tres archivos de la figura.

## 9. Salidas (versión 3)

| Archivo | sha256 |
|---|---|
| `generar_figura_extractor_ejemplo.py` | `ca7d45568b212998d423e62680edafa6bf61956630b8d3090af666f1ef0dca9d` (hasta el 08/10/2026, `1cc39e337a0137e7910f65c6ee109592a3a09d289c7a3b02b7a36f55d6755c2a`; §12) |
| `figura_extractor_ejemplo.svg` | `9a393b325cae953f3da697658cb435fdace001cf91cb8eee1ea28980b7dfe64d` |
| `figura_extractor_ejemplo.png` | `328d55fa6713a0a34d1abecd1a29ce89882333fddada019d3e2f221c828b4e13` |
| `figura_extractor_ejemplo.pdf` | `ce27d103b75093e582fc0247438043efee26edb7e163d16f9477527742da22b0` |

PDF con `/CreationDate` fijada por `SOURCE_DATE_EPOCH=0`; stream de contenido
sha256 `437f55096f30b4fd2e43335d42af78155673955d0c4f92be6f8ad604b4cb9ace`.

```
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_extractor_ejemplo.py
```

Este LEEME cae en `.gitignore:180` y entra solo con `git add -f`.

## 10. Regenerar con otra corrida

```
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_extractor_ejemplo.py --registro <extracciones_e1.jsonl> --sha256 <sha256> [--catalogo <catalogo.json> --sha256-catalogo <sha256>]
```

Una ruta distinta de la de omisión sin su sha256 frena. El generador frena
también si el archivo tiene cero o más de un registro de `cla::5.1.1.1`, si el
registro tiene error, si la salida trae claves que esta versión no conoce
(por ejemplo `sujeto_propuesto` o `otras_propiedades`), si dos cajas tendrían
el mismo tipo y la misma etiqueta, o si una entidad, un sujeto o una relación
no tiene lugar en `DISPOSICION` y `rutas_declaradas`. Los conteos de este
LEEME son de este registro.

## 11. Observaciones

- **Impreso**: NO VERIFICADO; la letra mínima (7,50 pt) y el margen
  (2,24 mm) se controlan sobre la geometría.
- **La excepción.** El verificador de la corrida (E3) dejó sobre la unidad un
  residual de severidad media que objeta esa entidad: la norma establece una
  regla de inclusión condicionada, no una excepción
  (`corpus_tanda0/salida_r2b/cla/finales.jsonl:61`, `residuales`). La figura
  dibuja la salida del extractor tal como vino y no lo marca.

## 12. Nota del 08/10/2026: estilo de la versión 4 del esquema final y medidor

Dos cambios en el generador, ninguno en la figura:

- **Estilo.** La figura del esquema final pasó a su versión 4
  (`LEEME_figura_esquema_final.md`, §8.1): sin la fila de la leyenda de lo
  agregado respecto del esquema de partida y con todos los rótulos de relación
  en gris. El candado `ESTILO` (:127-128) pasó de `dfdb16d4…` a `d5507195…`,
  y el docstring (:37) y el comentario de :126 dicen «versión 4». Lo que lee
  `leer_estilo` (:233-267) es igual en las dos versiones; el comentario de los
  rótulos (:250-251) dice ahora que desde la versión 4 ningún rótulo va en
  magenta. De `generar_figura_esquema_final.py` se importan 29 nombres: 28
  son iguales en las dos versiones (comparados con `ast`), y `W` vale 850 en
  las dos (su asignación comparte línea con el alto, que pasó de 860 a 852);
  `rect_texto` mide con los anchos AFM, que en la versión 4 suman «T» y «O».
- **Medidor.** Desde `88bfe89`, `generar_figura_proceso_extraccion.py` ya no
  tiene `medidor`, y la llamada `proc.medidor()` (:861) fallaba con
  `AttributeError`: el generador no corría en HEAD. Ahora importa
  `generar_figura_norma_a_grafo.py` (:108, en lugar de
  `generar_figura_proceso_extraccion.py`) y llama a `base.medidor()` (:861),
  la función de :806 de ese archivo. Si faltan PIL o la fuente del sistema,
  esa función frena en lugar de devolver `None`.

El script tiene las mismas líneas (944) y su sha256 pasó de `1cc39e33…` a
`ca7d4556…` (§9). Sobre una copia de las fuentes, la figura sale idéntica byte
a byte (los SVG, PNG y PDF de §9), y también la del ensamblado, que recompone
esta; registros en el paquete de revisión de FIG-ESQUEMA-FINAL-SOLO.
