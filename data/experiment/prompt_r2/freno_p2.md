# U-PROMPT-R2 — FRENO P2

03/10/2026, HEAD `fca019d`. USD 0: ninguna llamada a la API. Sin commit: el commit es de la autora.

Fuentes:
- mandato: `git show b901f6d:docs/mandatos/UPROMPT_R2_prefijo_nuevo.md`, P2, con sus notas fechadas (la última
  en `0061244`);
- enmienda a LAUDO B: `git show 0061244:docs/enmienda_laudo_B_guarda_ratchet_2026-10-03.md`, firmada,
  sha256 `7009d7d0…`.

Decisiones del FRENO P1 (la autora, 03/10/2026):
- texto aprobado, con dos ajustes;
- frecuencia: variante B;
- topes: USD 2 para la pareada y USD 69 para U-REEXT-T0;
- puntos 1, 2, 3, 5, 8 y 10, confirmados;
- sin la marca `guarda_ampliada`.
Detalle en el diseño (`data/experiment/prompt_r2/diseno_prefijo_r2.md`).

## 1. Las dos oraciones, tal como quedaron

**R8** (TIPOS · Condicion, destino de `condicion_de`), al final del párrafo:

> «Si lo que el supuesto condiciona no está en tu unidad (por ejemplo, la norma de un encabezado con unidad propia,
> cuando tu unidad es uno de sus ítems), emití la Condicion sin condicion_de: no la conectes con otro elemento del
> chunk.»

En R30 (COMPOSICIÓN CON EL ENCABEZADO DE UNA LISTA), en los supuestos con encabezado con unidad propia, la remisión
a esa regla:

> «…el ítem es una Condicion (ver Condicion) y la norma queda en la unidad del encabezado; como esa norma no está en
> tu unidad, la Condicion va sin `condicion_de` (ver Condicion).»

**R14** (PREDICADOS · remisiones). La fila `| referencia | TextoOrdenado → Comunicacion |` sigue en la tabla de
predicados del prefijo, así que la oración entra sin cambiar la redacción, después de la oración de las remisiones:

> «Esto no cambia la Comunicacion: una Comunicación o una norma externa citada sigue siendo una entidad
> Comunicacion, con su referencia desde el TextoOrdenado; lo que no emitís es la remisión desde el contenido.»

Con los dos ajustes se re-corrieron la no-filtración y los hashes:
- en las instrucciones nuevas y en el texto fijo del mensaje y de las NOTAS: 0;
- en el bloque de catálogo: las 19 ventanas de 5 palabras y los 10 bigramas o trigramas de control ya declarados
  (`p1/salida/nofiltracion_B.json` y `nofiltracion_mensaje.json`).
Lado a lado, en el §2 del diseño. En P4 se cuentan las Condicion de ítems sin `condicion_de`.

## 2. El prefijo congelado

| | Valor |
|---|---|
| Módulo y perfil | `data/experiment/reextraccion_v2/e1_extractor/prompt_r2b.py`; perfil `r2b` en `perfil_e1.py` |
| Variante | B |
| Caracteres del system | 51.780 |
| sha256 del system | `cdb374508523e7f2308b1e3dd9790cdcfbb4000f2f1616279504af9475c6e227` |
| Hash canónico (system + tools) | `14d6b63b508e` |
| Namespace de E1 | `e1_extraccion\|cv=e1-extractor-v1-p14d6b63b508e\|think=0` |
| Tool schema (archivo) | `data/experiment/pyd_r2/generados/tool_schema_r2.json`, sha256 `0c391f2b23bb7c94ec2606bd0315f3e4589c16a3571eaaa210a27babaa0f8ba2` |
| Enums r2 | sin cambios: `abd197ac…` |
| `modelos_r2.py` | sha256 `9a3fe3ec…`, con las decisiones 15 a 17 (las 16 de `p1/espejo_tool_schema.py`) |
| Reemplazos | `e1_extractor/prompt_r2b_reemplazos.json`, sha256 `810ad645…`: 30 reemplazos, R0 a R26 y R28 a R30 |
| Bloque de catálogo (R27) | `catalogo_unico/generados_r2/bloque_catalogo_r2.txt`, sha256 `c4005485…` |
| Prefijo de E3 | sin cambio: `21a836c7de6d` |

El texto es el del borrador B aprobado: `p1/salida/prefijo_r2_borrador_B.txt`, byte a byte. El módulo frena al
importar si cambia el sellado `v3_b54`, cualquiera de sus insumos o el texto armado.

## 3. Qué se implementó

| Archivo | Qué |
|---|---|
| `pyd_r2/code/modelos_r2.py`, `pyd_r2/generados/` | decisiones 15 a 17; tool schema y manifiesto regenerados (los enums, iguales) |
| `pyd_r2/code/selftest_pyd_r2.py` | generación vigente y 5 controles nuevos (decisiones 15 a 17, y el tramo antes de P3) |
| `e1_extractor/prompt_r2b.py`, `prompt_r2b_reemplazos.json`, `tablas_residuales_forzadas_r2b.json` | módulo del prefijo con sus candados; mensaje de E1 r2b (el del borrador); lista de tablas forzadas a residual, vacía |
| `e1_extractor/perfil_e1.py` | perfil `r2b`; `EsquemaValidacion.forma_salida`, con default `"v3"` |
| `e1_extractor/validador_e1.py` | `proyectar_r2` y la marca `forma_salida`, solo con «r2» y sobre una copia; el tramo de evidencia no se traduce |
| `e3_verificador/prompt_e3.py` | `notas_r2` (NOTA de tablas r2 y de encabezados de lista) solo con la marca; sin la marca, la NOTA de siempre |
| `e3_verificador/ratchet_e3.py` | la enmienda a LAUDO B: `ampliacion_activa` (forma «r2» y sin Obligacion, Restriccion ni Potestad) y la guardia sin exigir el tipo |
| `corpus_v2/runner_corpus.py` | el perfil de forma «r2» activa el camino r2; `FORMA_CRUDO_POR_PERFIL["r2b"] = "r2"`; `:862` pasa la validación; `resumen_e3.json` de r2b lista las exenciones de la ampliación |
| `tanda0/code/ensamblar_tanda0.py` | un manifiesto r2b corre la cadena r2, con las tablas de su E0 |
| `manifiestos/tanda0_10tos_r2b.json`, `tanda0_ens_diez_r2b.json`, `tanda0_ens_desarrollo_r2b.json` | perfil r2b sobre la e0-r2; el de extracción, con tope USD 69 |
| `selftest_e1.py`, `selftest_e3.py`, `selftest_manifiesto.py`, `e1_extractor/selftest_prompt_r2b.py` | casos de la traducción, la NOTA y la guarda; P10 (r2b) y P11 (sellado v3); selftest del perfil |

Los sha256 de cada archivo están en el manifiesto del paquete de revisión.

## 4. Los sellados reproducidos

El control corrió sobre una copia del repo sin enlaces (0 enlaces), con el código de P2: `control_reproduccion_p2.py`,
en el paquete. El repo no cambió durante el control: sha256 de 12.582 archivos, iguales antes y después.

| Qué | Resultado |
|---|---|
| E0 legada de la tanda 0 | 34/34 byte a byte |
| `ens_cinco`, `ens_diez` y `ens_desarrollo` (r1) | 10 de 13 archivos byte a byte en cada uno, `kg.json` incluido; los otros 3, iguales con la ruta normalizada |
| KG-Tanda0-Diez-r2a | `99fe2bfa…`, el sellado; 30 archivos byte a byte; el reporte, igual con la ruta normalizada |
| KG-Tanda0-Desarrollo-r2a | `93a7af72…`, el sellado; 20 archivos byte a byte; el reporte, igual con la ruta normalizada |
| Prefijo sellado `v3_b54` y su tool schema | sin cambio: las claves de E1 de las 2.434 unidades de la tanda 0 están en la caché (`selftest_manifiesto`, P11) |
| Mensaje de E3 con el perfil existente | sin cambio: las claves de E3 de los 2.427 pares de la salida sellada están en la caché (P11) |
| `validador_e1` en v3 | la validación recomputada del crudo de la tanda 0 es la guardada, 2.431/2.431 (P11) |
| Prefijo de E3 | `21a836c7de6d` |

Los 3 archivos de cada ensamblado r1 que difieren son `e5_esqueleto.json`, `reporte_ensamblado_r1.json` y
`reporte_ensamblado.json`. Difieren solo en rutas absolutas: la raíz del repo contra la de la copia, la entrada y
el directorio de salida. El reporte de U-R2-CODIGO registraba lo mismo: 10 de 13 y los reportes iguales con la ruta
normalizada.

## 5. Selftests

| Selftest | Resultado |
|---|---|
| `selftest_prompt_r2b` (perfil nuevo) | 23/23 |
| `selftest_manifiesto` | 49/49: P1 a P9 37/37, P10 9/9 y P11 3/3 |
| `selftest_pyd_r2` | 301/301 |
| `selftest_e1` | 65/65 (53 de antes y 12 nuevos) |
| `selftest_e3` | 80/80 (71 de antes y 9 nuevos) |
| `selftest_cablev3` | 45/45 |
| E0: `selftest_e0`, `b52`, `b581`, `b582` y `b583` | 57/57, 39/39, 34/34, 59/59 y 33/33 (33 [PASS] y 0 [FAIL]; no imprime total) |
| `selftest_e0r2` | 48/48 |
| `selftest_ub53`, `selftest_corpus`, `selftest_e2` y `selftest_dirigida_tanda0` | 40/40, 21/21, 35/35 y 28/28 |
| `selftest_r2`, `selftest_r3` y `selftest_r4` (con `--e0-r2`) | 18/18, 96/96 y 26/26 |

En el cierre de U-R2-CODIGO, `selftest_manifiesto` daba 32/37, con 5 fallos ambientales en P5. Hoy esos 5 pasan;
no investigué por qué.

## 6. Los cuatro requests (P2.d)

`data/experiment/prompt_r2/p2/prueba_en_seco_p2d.py`, en doble corrida idéntica, escribe en
`p2/salida/prueba_en_seco/` el request completo de cada caso, el resumen y el mensaje de usuario
(`requests.md`):
- `cap::1.2` y `ric::9.2.1`, con tabla serializada;
- `cla::6.5.5.7`, la primera unidad con `sujeto_propuesto` en el crudo de la tanda 0, en el orden de la corrida;
- `cla::5.1.1.1`.

Los cuatro tienen el system congelado (`cdb37450…`), `max_tokens` 8.192, la herramienta forzada y la clave de la
caché en el namespace `p14d6b63b508e`. El sha256 de `tools` del resumen es el de su JSON canónico, no el del
archivo del tool schema.

## 7. Error propio, con su causa

Corrí `selftest_corpus` sobre el repo, no sobre una copia, y el selftest reescribe sus 11 checkpoints rastreados
en `data/experiment/reextraccion_v2/corpus_v2/salida_selftest/`. Los detecté con el control de sha posterior
a los selftests y los restauré a HEAD (`git checkout --`). Los 22 archivos de ese directorio quedaron iguales a la
foto previa. Ningún otro archivo cambió por mis corridas.

## 8. Pendiente

- **P3:** `validador_r2` lee la forma «r2» completa:
  - el tramo de evidencia y el `termino` literal, con su marca;
  - las `otras_propiedades` de las relaciones;
  - `source` y `destino` de la omisión;
  - las derivaciones de la decisión 16;
  - el elemento sin valor del límite relativo.
  Hasta P3, el tramo de evidencia queda en `campos_no_definidos`, sin rechazo, y un control de
  `selftest_pyd_r2` lo deja explícito.
- **P4:** la pareada, con la pata de E3, los casos de control y el conteo de las Condicion de ítems sin
  `condicion_de`.
- **Commit de P1 (ajustes) y de P2:** PENDIENTE de la autora.
