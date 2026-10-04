# figura_extractor_ejemplo — registro de generación (versión 2)

Figura «la salida del extractor para el ejemplo» para la sección 4.2 de la
tesis: lo que devolvió el extractor para la unidad del punto 5.1.1.1 de
Clasificación de deudores, dibujado como un fragmento de grafo.

- **Una caja por entidad** de la salida cruda (cinco), con su tipo en negrita
  y su etiqueta debajo, y **una caja por sujeto** al que llega una relación
  (uno), con borde discontinuo, el tipo `Sujeto` y el nombre legible de su
  entrada en el catálogo.
- **Una flecha por relación** (cinco), de origen a destino, rotulada con su
  nombre; solo tramos horizontales y verticales, **sin cruces (0)**.
- **Estilo** de la figura del esquema final (sección 3.10, versión 3): el
  mismo relleno, borde y grosor para cada tipo, la discontinua del sujeto, el
  gris de las flechas y de los rótulos y la tipografía de tipos y rótulos.
- **Sin panel de la unidad** (el texto de entrada está en la figura de las
  unidades de la sección 3.2), **sin marcas** de deformaciones ni errores y
  **sin leyenda**: cada caja dice su tipo.

Alto impreso a 15 cm de ancho: **6,56 cm** (lienzo 850 × 372, la escala de la
figura del esquema final; PDF 425,2 × 186,1 pt; PNG 1772 × 776 px a 300 dpi).
Cruces entre flechas: **0**.

## Versiones

- **Versión 1** (03/10/2026, sin commit, reemplazada): el formato de la
  figura de la ficha (sección 3.8), con la unidad a la izquierda (cadena
  estructural en gris y texto recuadrado) y, a la derecha, cada entidad con
  su identificador local, su tipo y su etiqueta, y cada relación con su
  origen, su nombre y su destino. Alto 8,06 cm. sha256: generador
  `a20c997ec0bcea6a9c9cafa502dd5862a3cc3f6ef900818df4e4f99f6661ff51`, SVG
  `9d6c33d21943aec7608b7f9ee8cbeabe426a15298e248b4927fefd039a7caf27`, PNG
  `ef6fee9efea168b8dcb31764e4fad1a78a2cf62b9029abf672335efc5132b888`, PDF
  `fc75747126a88d5307864f3bcec07e0e4859b89f65c98154a511670cab23d63f`, LEEME
  `7f86e7b42212c14a0af45ee0d15e9c94a2a1a1a92456d544d99a52bb631c6119`. Los
  archivos quedaron en el paquete de revisión de esa versión, fuera del repo.
- **Versión 2** (04/10/2026). Qué cambió:
  - sale el panel de la unidad (la unidad ya está dibujada en la figura de la
    sección 3.2), y con él la lectura del artefacto de unidades y del PDF del
    documento y los controles del texto de la unidad;
  - la extracción pasa de dos listas a un fragmento de grafo: cajas y
    flechas rotuladas;
  - el estilo pasa del de la figura de la ficha al de la figura del esquema
    final, leído de su SVG con candado;
  - salen los identificadores locales (`to`, `e1` … `e4`): las flechas unen
    cajas y no hacen falta;
  - el sujeto pasa de su identificador interno
    (`Sujeto_rol_obligado_a_clasificar_clasificacion`) al nombre de su entrada
    en el catálogo, leído con candado;
  - el lienzo pasa de 720 a 850 unidades para 15 cm, la escala de la figura
    del esquema final, para que cajas, letras y trazos impriman igual que
    allí;
  - entran el control de flechas (extremos, tramos y puntas), el de cruces y
    una prueba negativa nueva, el cruce de flechas (las otras cuatro siguen,
    sobre cajas y flechas: la entidad de menos ahora quita una caja); el
    control de inventario relee cajas y flechas del SVG en lugar de la
    lista.

## 1. Fuente de la extracción

Sin cambios respecto de la versión 1.

**El registro.** `data/experiment/reextraccion_v2/corpus_tanda0/salida/cla/extracciones_e1.jsonl:61`,
sha256 `1d3baa2349a1298e68748126522b78b079d1b4569cbaa6789624c4399273f1f1`
(último commit que toca el archivo: `ad6d5ad`). La figura dibuja su campo
`tool_input_crudo`: la salida de la tool tal como la devolvió el modelo, antes
del validador. Registro sin error, `stop_reason` `tool_use`, 967 tokens de
salida.

**La corrida.** La de la tanda 0 sobre el conjunto de desarrollo, perfil
`v3_b54`: `data/experiment/reextraccion_v2/manifiestos/tanda0_10tos.json:123`
(`"perfil_e1": "v3_b54"`; sha256 `5299340cc5fb8bd22c9a382cf8daf320fc57d7c7441e6748a8bdf49ab32461c7`),
`tanda0_ens_desarrollo.json:18` y `:65` (`cla` entre los cinco documentos de
desarrollo, mismo perfil; sha256
`bfe7c7b0912c990996b802c785e565741468d5cef49e67ba4a80beca06c0468f`),
`corpus_tanda0/salida/cla/resumen_e1.json:24` (namespace
`e1_extraccion|cv=e1-extractor-v1-p54a111e2175f|think=0`) y
`corpus_tanda0/salida_dirigida/reextraccion_dirigida.json:4-5` (ese namespace
es el de `v3_b54`). Sin reintento: `corpus_tanda0/salida/cla/finales.jsonl:61`,
`"n_reintentos": 0`.

**Es el único registro de esa corrida para la unidad.** Seis líneas de
`data/experiment` tienen un `tool_input_crudo` de `cla::5.1.1.1`: cuatro de la
tanda 0, en archivos byte-idénticos (`salida/cla/extracciones_e1.jsonl`, su
`_compact` y las dos copias de `salida_dirigida/cla`), y dos de la E1 de r1
(`corpus_v2/salida/cla/`, 11/08/2026, otro perfil, namespace
`p4793d6152608`). La caché de la API (no versionada:
`data/experiment/reextraccion_v2/e1_extractor/.gitignore:1`; leída con
`immutable=1`, sha256 `7b331d82adf9e4c2cfe0799971e6935189dd88095488c5201026f225bcaf2082`
igual antes y después) tiene una sola llamada del punto con el namespace de
`v3_b54` (clave `60d835fb84ee8d25…`), cuyo `tool_use.input` es igual al
`tool_input_crudo` de la línea 61, con el mismo orden de claves.

```
grep -rl --include="*.jsonl" '"chunk_id": "cla::5.1.1.1"' data/experiment | xargs grep -n '"chunk_id": "cla::5.1.1.1".*"tool_input_crudo"' | cut -c1-140
```

## 2. Fuente del nombre del sujeto

`data/experiment/catalogo_unico/catalogo_sujetos_v3.json`, sha256
`9a2522e41e1086d26bb73a37070efd9913f98ec36e2f957e198b460d21ca6c58` (commit
`12f3f74`, el único que toca el archivo; sin cambios en el árbol). La entrada
de `Sujeto_rol_obligado_a_clasificar_clasificacion` (línea 2655) tiene
`"label": "Obligados a clasificar deudores (Clasificación)"` (línea 2657),
nivel `rol`, estado `vigente`. El generador busca la entrada por el
`sujeto_id` de la relación, frena si no hay exactamente una, si no tiene
`label` o si no está vigente, y dibuja el `label`; el identificador interno
no aparece en la figura (`PROHIBIDOS` incluye `Sujeto_`).

Por qué este catálogo:

- es el del perfil `v3_b54`: la entrada declara su alta en el «catálogo del
  prefijo congelado (`data/experiment/esq/code/prompt_congelado.py`,
  `SUJETOS_CATALOGO`; laudo de esquema congelado, commit `2593d4d`)»;
- el prompt de sistema de la llamada que produjo el registro (caché, clave
  `60d835fb84ee8d25…`) lista
  `Sujeto_rol_obligado_a_clasificar_clasificacion — Obligados a clasificar deudores (Clasificación)`:
  es el nombre que el modelo tenía a la vista;
- el catálogo r2 (`data/experiment/catalogo_unico/catalogo_sujetos_r2.json:3211`)
  da el mismo `label`.

```
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B -c "import json,sqlite3;D='data/experiment/reextraccion_v2/e1_extractor/cache/e1_extraccion.db';c=sqlite3.connect('file:'+D+'?mode=ro&immutable=1',uri=True);r=json.loads(c.execute(\"select request_json from cache where key like '60d835fb84ee8d25%'\").fetchone()[0]);s=r['system'] if isinstance(r['system'],str) else ''.join(b.get('text','') for b in r['system']);print('Sujeto_rol_obligado_a_clasificar_clasificacion — Obligados a clasificar deudores (Clasificación)' in s)"
```

## 3. Estilo

Se lee de `docs/tesis/figuras/figura_esquema_final.svg` (versión 3, commit
`8edd732`, sha256
`dfdb16d471bb93c6351aa03b1e609452b75c428baa354c52354ce1dfe9797bb3`): el
estilo de cada caja sale de su `<rect data-caja="…">`; el de los nombres de
tipo, de sus textos en negrita; el de los rótulos, de sus textos con halo; el
de las flechas, de sus caminos y puntas. El generador frena si alguno no es
único en esa figura. Para los tipos de este registro:

| Tipo | Relleno | Borde | Grosor | Otro |
|---|---|---|---|---|
| `Condicion` | `#f8e8f5` | `#b5179e` | 2,6 | |
| `Definicion` | `#f8e8f5` | `#b5179e` | 2,6 | |
| `Operacion` | `#eaefee` | `#52796f` | 2 | |
| `TextoOrdenado` | `#e8e8e8` | `#3d3d3d` | 2 | |
| `Sujeto` | `white` | `#6d597a` | 2 | discontinua `7 5` |

Esquinas de 6. Tipos en Menlo negrita de 19 (9,50 pt), tinta `#1f1f1f`;
rótulos en Menlo de 15 (7,50 pt), gris `#6f6f6f`, con halo blanco; flechas
`#8a8a8a` de 1,6, con las puntas de su generador (`triangulo`, 9 × 10).
Etiquetas en Helvetica de 15 (7,50 pt, el cuerpo de los rótulos y las notas
de esa figura), tinta `#1f1f1f`, centradas y envueltas por palabras en el
ancho de la caja.

Dos cosas de esa figura que esta no toma:

- **El rótulo en magenta.** Allí `condicion_de` y `remite_a` llevan el rótulo
  en magenta (`#b5179e`) porque son relaciones agregadas respecto del esquema
  de partida. Esta figura no marca nada: todos los rótulos van en el gris de
  los demás.
- **El significado del magenta de las cajas.** `Condicion` y `Definicion`
  llevan allí el magenta de los tipos agregados respecto de la partida; acá
  conservan ese relleno y ese borde porque son el estilo de su tipo, sin
  leyenda que les dé otro sentido.

## 4. Disposición

Tres filas sobre tres columnas de cajas de 230 × 76 (las cajas tienen el
tamaño común de la que más líneas necesita; todas las etiquetas ocupan una o
dos):

- arriba, las dos `Condicion` y la `Definicion`;
- al medio, la `Operacion`, entre las dos condiciones, y el `TextoOrdenado`,
  debajo de la definición;
- abajo, el `Sujeto`, debajo de la operación.

Las dos `condicion_de` bajan rectas a la operación; las dos `establecida_en`
llegan rectas al Texto Ordenado, una desde arriba y otra desde la izquierda;
`aplica_a` baja recta al sujeto. Ninguna flecha dobla, así que no hay cruces.
Los rótulos van al costado de las flechas verticales y arriba de la
horizontal, a 4 unidades de su línea.

La disposición es la de este registro (`DISPOSICION` y `RUTAS`, por
identificador local): si el registro trae una entidad, un sujeto o una
relación sin lugar declarado, el generador frena. Regenerar con otra corrida
pide declarar una disposición nueva; los controles comprueban la que se
declare.

## 5. Qué se dibuja y qué no

Se dibujan, de cada entidad, su tipo y su etiqueta; de cada relación, su
origen, su destino y su nombre; del sujeto, su tipo y su nombre del catálogo.
No se dibujan los identificadores locales, las propiedades (`properties`) ni
el `punto` de cada elemento (todos «5.1.1.1»). `omisiones_no_prosa` está
vacío; si no lo estuviera, el generador frena. Esta versión no prevé
`sujeto_propuesto`: una relación con ese campo frena el generador. Ninguna
etiqueta se abrevia.

## 6. Reutilización

`generar_figura_esquema_final.py` (commit `8edd732`, sha256
`0d6274fe2d3a870ff8776b29f9d69195867ffbced767355a5a2fa20ee756bb15`) se
importa sin modificarlo: el lienzo de 850 unidades para 15 cm, el texto con
halo (`texto_svg`), las puntas (`punta_svg`, `triangulo`), la medida de Menlo
(`rect_texto`), la geometría de rectángulos y tramos (`crecer`, `se_solapan`,
`toca`, `largo_dentro`, `dist_rect_tramo`, `bbox`), las distancias de los
rótulos (`JUNTO`, `MARGEN_AJENA`, `HALO`, `AIRE`), la de paralelas, el conteo
de cruces (`cruces`) y la exportación (`exportar`, `png_dimensiones`). De
`generar_figura_proceso_extraccion.py` (sha256
`6a91931abeb9927842f76fa50471497e926c69fc56617c62ef7f05ddf6c010d6`), el
medidor con las métricas reales de Helvetica para las etiquetas. La versión
2 ya no importa `generar_figura_ficha.py`.

## 7. Controles

Salida de la corrida que escribió las salidas del repo (extracto):

```
INVENTARIO (releído del SVG): 6 cajas y 5 relaciones contra 6 y 5 del registro; fallas: 0
CONTENIDO: 22 textos, 17 piezas; fallas: 0
TEXTOS: 22 textos contra 6 cajas y 5 flechas; distancias mínimas texto-texto 3.0; rótulo-su flecha 4.0; rótulo-otra flecha 59.5; texto-borde de su caja 9.0; fallas: 0
CAJAS: 6 cajas; fallas: 0
TRAZOS: 5 tramos en el SVG; fallas: 0
FLECHAS: 5 flechas; fallas: 0
CRUCES: 0 cruce(s) entre flechas, declarados 0; fallas: 0
MARGEN: 33 elementos; mínimo a cada borde izquierdo 12.7 u = 2.24 mm, superior 12.7 u = 2.24 mm, derecho 12.7 u = 2.24 mm, inferior 13.0 u = 2.29 mm; exigido 2.0 mm (11.3 u); fallas: 0
REGISTRO: 38 elementos del SVG; fallas: 0
LETRA 15 unidades -> 7.50 pt impresos a 15 cm
LETRA 19 unidades -> 9.50 pt impresos a 15 cm
```

- **Inventario.** Relee el SVG y rearma, solo desde su geometría, una caja
  por rectángulo (el texto en negrita es el tipo; el resto, la etiqueta) y
  una relación por camino (la caja en cuyo borde empieza, la caja en cuyo
  borde está su punta y el rótulo más cercano, que tiene que estar al menos
  5 más cerca que el de cualquier otra flecha). Las 6 cajas y las 5
  relaciones son exactamente las del registro con su sujeto.
- **Cruces.** Cuenta los cruces en X entre tramos de flechas distintas con la
  función de la figura del esquema final; cualquier toque o tramo
  superpuesto es defecto. Resultado: 0, los declarados.
- **22 textos** = 6 tipos + 11 líneas de etiqueta (las seis etiquetas en dos
  líneas salvo la del Texto Ordenado, en una) + 5 rótulos. **38 elementos**
  = 5 caminos + 5 puntas + 6 cajas + 22 textos.

## 8. Pruebas negativas

Cada corrida planta cinco defectos antes de componer la figura y frena si
alguno no hace fallar su control:

```
PRUEBAS NEGATIVAS: 5 de 5 hacen fallar su control
  relacion_de_mas -> inventario: relación de la figura que no está en el registro: (('Condicion', 'Monto supera dos veces importe referencia 3.7'), 'regula', ('Condicion', 'Repago vinculado a actividad productiva/comercial')) (fallan también: contenido, textos)
  entidad_de_menos -> inventario: flecha de (721.0, 90.0) a (721.0, 148.0): 0 caja(s) de origen y 1 de destino (fallan también: contenido, flechas)
  rotulo_sobre_caja -> textos: 'aplica_a': se superpone con la caja de sujeto:Sujeto_rol_obligado_a_clasificar_clasificacion
  tramo_diagonal -> trazos: tramo diagonal de (277, 224) a (307, 282) (fallan también: textos)
  cruce_de_flechas -> cruces: 1 cruce(s) entre flechas, declarados 0: [('condicion_de (2)', 'condicion_de (3)')] en (203.0, 119.0) (fallan también: inventario, textos)
```

Con `--perturbar <caso>` el generador compone la figura con el defecto: en
los cinco casos termina con «FALLA: la figura tiene defectos; no se escribe
nada», código de salida 1 y ningún archivo en el directorio de salida. En la
de la entidad de menos, el inventario informa además la caja y la relación
faltantes.

## 9. Reproducibilidad

Tres corridas sobre una copia de los seis archivos que usa el generador en el
scratchpad (copiados, sin enlaces), con `PYTHONHASHSEED` 0, 1 y 4242: las
tres dan los mismos SVG, PNG y PDF, idénticos a los del repo, y la misma
salida salvo la ruta. sha256 de los archivos del repo (sin `.venv` ni `.git`)
iguales antes y después de las tres corridas; la corrida que escribió en el
repo cambió solo los tres archivos de la figura.

## 10. Salidas (versión 2)

| Archivo | sha256 |
|---|---|
| `generar_figura_extractor_ejemplo.py` | `7cc8cc1106412e79c99a23c70887d46cf5b5e85354766f8c734d1fcb021bd5a5` |
| `figura_extractor_ejemplo.svg` | `46e6cb24bd397eaa8d6d6a1ba3a83ba329ff8a0739e2cf319bd10feea6e9fac5` |
| `figura_extractor_ejemplo.png` | `f01d64cdc6919353919e9c55026a663cf7df60f158d67d27d0ce04d9defd6086` |
| `figura_extractor_ejemplo.pdf` | `6b6073a579e2273cdd8fd136cddf793d424d2ab810981a133ab3637b136b9ff1` |

PDF con `/CreationDate` fijada por `SOURCE_DATE_EPOCH=0`; stream de contenido
sha256 `b273d8b4718df981980b694f50be9605ec7fe93f2da8abde6e07dcd893e22440`.

```
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_extractor_ejemplo.py
```

Este LEEME cae en `.gitignore:180` y entra solo con `git add -f`.

## 11. Regenerar con otra corrida

```
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_extractor_ejemplo.py --registro <extracciones_e1.jsonl> --sha256 <sha256> --catalogo <catalogo.json> --sha256-catalogo <sha256>
```

Una ruta distinta de la de omisión sin su sha256 frena. El generador frena
también si el archivo tiene cero o más de un registro de `cla::5.1.1.1`, si
el registro tiene error, si la salida trae claves que esta versión no conoce
(las del tool schema r2, `tramo`, `otras_propiedades` o `sujeto_mencion`, o
un `sujeto_propuesto`), si `omisiones_no_prosa` no está vacío, si dos cajas
tendrían el mismo tipo y la misma etiqueta, o si una entidad, un sujeto o una
relación no tiene lugar en `DISPOSICION` y `RUTAS`. Los conteos del epígrafe
y de este LEEME son de este registro.

## 12. Epígrafe propuesto

> Salida del extractor para el punto 5.1.1.1 de Clasificación de deudores en
> la corrida de la tanda 0, tal como la devolvió el modelo y antes del
> validador. El texto de entrada es la unidad que muestra la figura de la
> sección 3.2. Cada caja es una entidad, con su tipo en negrita y su etiqueta
> debajo, y cada flecha es una relación rotulada con su nombre. El sujeto, en
> la caja de borde discontinuo, se muestra con el nombre de su entrada en el
> catálogo.

Si el capítulo 4 nombra la tanda 0 de otra manera, el epígrafe toma ese
nombre; la remisión a la figura de la sección 3.2 va con su `\ref` en el
`.tex`.

## 13. Observaciones

- **Impreso**: NO VERIFICADO; la letra mínima (7,50 pt) y el margen
  (2,24 mm) se controlan sobre la geometría.
- **La medida de Menlo** es la de la figura del esquema final (avance de
  0,602 em por carácter); la de Helvetica, la del medidor con las métricas
  reales de la fuente.
