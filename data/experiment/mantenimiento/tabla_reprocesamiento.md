# Qué obliga a reprocesar y qué no

U-MANT, etapa M1. Tabla de mantenimiento del pipeline: para cada tipo de cambio,
en qué paso entra, qué obliga a recomputar y cuánto cuesta. La verifiqué contra
la clave de la caché local de E1 y de E3 con un selftest que arma los requests
con el código del pipeline y no llama a la API
(`data/experiment/mantenimiento/code/selftest_clave_cache.py`). Costo de esta
etapa: USD 0, sin red.

## 1. Cómo se forma la clave

La clave de la caché local es sha256 del namespace, un salto de línea y el
request canónico, que serializa todos los kwargs del request con las claves
ordenadas (`data/experiment/evaluacion/llm_cache.py:110-126`). Un cambio obliga
a pagar una unidad solo si mueve alguna de las dos cosas.

**Namespace.** E1: dominio, `CODE_VER` manual (`e1-extractor-v1`) más el hash
del prefijo (system y tools) y la marca de thinking
(`reextraccion_v2/e1_extractor/cliente_e1.py:50`, `:63-81`); en la tanda 0,
`e1_extraccion|cv=e1-extractor-v1-p54a111e2175f|think=0`. E3: lo mismo con
`e3-verificador-v1` y el hash de su prefijo
(`reextraccion_v2/e3_verificador/cliente_e3.py:49`, `:55-62`);
`e3_verificacion|cv=e3-verificador-v1-p21a836c7de6d|think=0`.

**Request de E1** (perfil `v3_b54`, `b54_catalogo_v3/code/prompt_v3_b54.py:524`):
modelo, `max_tokens`, el prefijo de sistema con el bloque de catálogo
(`:505-520`), el tool schema con los enums de sujeto (`:411-414`),
`tool_choice` y el mensaje de usuario. El mensaje lleva archivo, TO, tipo de
unidad, número y título, puntos admitidos, la línea de alcance del TO, toda la
herencia (encabezados y bloques de prosa), las marcas de E0 con su evidencia y
el texto (`reextraccion_v2/e1_extractor/prompt_e1.py:441-522`,
`prompt_v3_b54.py:459-502`). No lleva el id de la unidad, sus páginas, sus
sha256 ni sus conteos de caracteres.

**Request de E3** (`reextraccion_v2/e3_verificador/prompt_e3.py:266-283`):
modelo, `max_tokens`, thinking deshabilitado, prefijo (instrucciones y
calibradores), tool schema y un mensaje con archivo, TO, unidad, título, la
nota de marcas de E0, el texto fuente (solo los encabezados heredados más el
texto propio, `comun_e3.py:111-137`) y la salida validada de E1
(`comun_e3.py:140`). E3 no recibe los bloques de prosa heredados.

**Archivos de datos que entran a los prefijos al importar** (inventario del
selftest, proceso hijo con registro de aperturas):
`data/experiment/grafo_v2/esquema_v2_clases.json` (catálogo v2, `schema.py:86-113`,
del que salen el enum de la cadena congelada y la línea de alcance de los cinco
TOs de desarrollo) y, para el prefijo de E3, los calibradores
(`calibradores_e3.py:82-84`), que se arman desde
`reextraccion_v2/e0_chunking/salida/chunks_{cla,pro,ric}.json` y
`reextraccion_v2/e1_extractor/salida/faseB_pro/extracciones.jsonl`.

**Candados.** El perfil `v3_b54` recomputa el sha y el hash del prefijo v3 y
frena si no son los sellados (`perfil_e1.py:154-160`); la cadena congelada
frena si el prefijo v2 no es el sellado (`esq/code/prompt_congelado.py:156-160`).
El prefijo de E3 no tiene candado en el código: su hash solo se nombra en un
docstring (`e3_verificador/runner_faseB_e3_enm01.py:13`).

## 2. Las cuatro clases y el principio de cada fila

- **nada**: ningún paso se vuelve a correr; el grafo guardado sigue valiendo.
- **solo código sobre lo guardado**: se re-aplican pasos determinísticos sobre
  la salida guardada de E1 y E3, sin llamadas a la API.
- **E1 y E3 de las afectadas**: llaman a la API solo las unidades cuyo request
  cambia; el resto sale de la caché.
- **todo**: llaman a la API todas las unidades del corpus en al menos una de
  las dos etapas.

Principio 12 (plan, `docs/plan_tesis.md:299`): rige las filas en las que el
cambio vive en código y se re-aplica sobre lo guardado a USD 0. Principio 9
(`docs/plan_tesis.md:277`): rige las filas que obligan a llamar a la API o que
vienen de la fuente; el resultado es otra versión del grafo, declarada como
release, y el grafo evaluado no se corrige.

Lectura de las columnas de clave: **Clave E1** y **Clave E3** dicen el efecto
directo del cambio sobre el request de cada etapa, con todo lo demás fijo. E1
corre sin temperatura fijada (`docs/laudo_release_r2_pipeline.md:310-311`), de
modo que toda unidad que se vuelve a llamar en E1 trae una salida nueva y,
con ella, un request de E3 nuevo: eso va en la columna «Qué obliga a recomputar»,
no en la de la clave de E3.

## 3. La tabla

| Fila | Cambio | Dónde entra | Qué obliga a recomputar | Clave E1 | Clave E3 | Clase | Principio | Ancla | Variación del selftest |
|---|---|---|---|---|---|---|---|---|---|
| F01 | Texto propio de una unidad de E0 | E0; texto del mensaje de E1 y texto propio del fuente de E3 | E1 y E3 de esa unidad; E2 y ensamblado en código | cambia (esa unidad) | cambia (esa unidad) | E1 y E3 de las afectadas | 9 | `prompt_e1.py:514`; `comun_e3.py:111-137` | V01 |
| F02 | Texto de un bloque heredado de tipo encabezado (título de un ancestro) | E0; herencia del mensaje de E1 y del fuente de E3 de cada unidad que lo hereda | E1 y E3 de todas las unidades que heredan ese encabezado | cambia (las que lo heredan) | cambia (las que lo heredan) | E1 y E3 de las afectadas | 9 | `prompt_e1.py:473-486`; `comun_e3.py:123-127` | V02 |
| F03 | Texto de un bloque heredado de prosa (intro, cierre, chapeau de sección, intersticial) | E0; mini-chunk del bloque (fila F01) y herencia del mensaje de E1 de los descendientes; no entra a E3 de los descendientes | E1 del mini-chunk y de los descendientes que lo heredan; E3 de esas unidades porque cambia su salida de E1 | cambia (los descendientes que lo heredan) | no cambia (descendientes, con la salida de E1 fija) | E1 y E3 de las afectadas | 9 | `prompt_e1.py:473-486`; `comun_e3.py:123-125` | V03 |
| F04 | Marcas de E0 (contenido tabular, fórmula y su evidencia) sin cambio de texto, por ejemplo la detección de tablas de RX-10 | E0; línea de marcas del mensaje de E1 y nota de E3 | E1 y E3 de las unidades re-marcadas | cambia (las re-marcadas) | cambia (las re-marcadas) | E1 y E3 de las afectadas | 9 | `prompt_e1.py:488-505`; `prompt_e3.py:233-245` | V04 |
| F05 | Páginas, id, sha256 y conteos de caracteres de una unidad sin cambio de texto (corrimiento de páginas; ids desambiguados de `BKL-0037`) | E0; provenance que arma E2 e identidad de los registros persistidos | E2 y ensamblado en código | no cambia | no cambia | solo código sobre lo guardado | 12 | `e2_reduce/e2_lib.py:104-113`; `prompt_e1.py:441-522` no lee esos campos | V05, V06 |
| F06 | Prefijo de E1 (texto de sistema) | E1; system del request y hash del prefijo en el namespace | E1 de todas las unidades; E3 de todas por la salida nueva de E1; re-sello del perfil | cambia (todas, con namespace nuevo) | no cambia (con la salida de E1 fija) | todo | 9 | `prompt_v3_b54.py:505-520`; `cliente_e1.py:63-81`; candado `perfil_e1.py:154-160` | V08 |
| F07 | Tool schema de E1 | E1; tools del request y hash del prefijo | igual que F06 | cambia (todas, con namespace nuevo) | no cambia (con la salida de E1 fija) | todo | 9 | `prompt_v3_b54.py:411-414`, `:516-520` | V09 |
| F08 | Modelo o parámetros del request de E1 (modelo, max_tokens, temperatura) | E1; request | E1 de todas; E3 de todas por la salida nueva. Los techos de reintento (32.768 por corte, 16.384 del ratchet) solo entran a los requests que los usan | cambia (todas) | no cambia (con la salida de E1 fija) | todo | 9 | `runner_corpus.py:87-89`; `cliente_e1.py:60`, `:281-305`; `ratchet_e3.py:248-250` | V12, V13, V14 |
| F09 | Versión de código del namespace (`CODE_VER` de E1), con el request idéntico. Fila agregada: no está en la lista del mandato | namespace de la caché | igual que F06, sin cambiar un byte del request | cambia (todas) | no cambia | todo | 9 | `cliente_e1.py:50`, `:77-81` | V15 |
| F10 | Prompt de E3 (instrucciones, calibradores o tool schema) o su modelo | E3; system, tools y modelo del request, y hash del prefijo en el namespace. Los calibradores se arman al importar desde cuatro archivos de datos (sección 1) | E3 de todas las unidades; E1 base sale de la caché; los reintentos del ratchet cambian donde cambie el feedback | no cambia | cambia (todas, con namespace nuevo si cambia el prefijo) | todo | 9 | `prompt_e3.py:138-145`, `:213-217`, `:266-283`; `calibradores_e3.py:82-84`; `cliente_e3.py:55-62` | V16, V17 |
| F11 | Catálogo de sujetos en el bloque del prompt de E1 (líneas del bloque o enum de `sujeto_id`) | E1; system y tools | igual que F06; el candado del perfil frena hasta el re-sello | cambia (todas, con namespace nuevo) | no cambia (con la salida de E1 fija) | todo | 9 | `prompt_v3_b54.py:326-392`, `:411-414`; `perfil_e1.py:154-160` | V10, V10b |
| F11b | Clases del catálogo en `esquema_v2_clases.json` (por ejemplo, un alias) | llega al bloque y al enum por la cadena congelada (`schema.py:86-100` → `prompt_congelado.py:64`) | igual que F11, después de re-sellar la cadena | frena (candado v2 al construir el perfil) | no aplica | todo | 9 | `prompt_congelado.py:156-160`; `schema.py:86-100` | V22 |
| F12 | Tabla TO→rol de alcance (línea «Alcance de este TO» del mensaje de usuario). En los cinco TOs de desarrollo sale de los roles de `esquema_v2_clases.json` y ningún candado la cubre | E1; mensaje de usuario de las unidades de ese TO | E1 y E3 de todas las unidades de ese TO | cambia (las del TO) | no cambia (con la salida de E1 fija) | E1 y E3 de las afectadas | 9 | `prompt_e1.py:463-471`; `prompt_v3_b54.py:428-456`; `schema.py:103-113` | V11, V21 |
| F13 | Catálogo de sujetos solo en el JSON que leen E4, el esqueleto y S19 (`esquema_v3_clases.json`), que el armado del request no abre | E4 y esqueleto, sobre lo guardado | E4, esqueleto y lo que sigue del ensamblado, en código | no cambia | no cambia | solo código sobre lo guardado | 12 | `tanda0/code/ensamblar_tanda0.py:138-142`; `ensamblar_corpus.py:83` | V20 |
| F14 | Validador de E1 y política por campo | sobre la salida cruda de E1 guardada | validación y ensamblado en código; si además se re-verifica en E3, E3 de las unidades cuya salida validada cambia | no cambia | cambia (las unidades cuya salida validada cambia) | solo código sobre lo guardado | 12 | `runner_corpus.py:495-501`; `comun_e3.py:140`; `ratchet_e3.py:256-290` | V18 |
| F15 | E2 y ensamblado (fan-in, merge, cola flaggeada, referencias, provenance) | después de E3, sobre `extracciones_finales_<to>.jsonl` y `finales.jsonl` | E2 y ensamblado en código | no cambia | no cambia | solo código sobre lo guardado | 12 | `runner_corpus.py:665-709`; `tanda0/code/ensamblar_tanda0.py` | V19 |
| F16 | E4 y esqueleto | después del merge | E4, esqueleto y lo que sigue, en código | no cambia | no cambia | solo código sobre lo guardado | 12 | `corpus_v2/r1_e4.py:121`; `ensamblar_corpus.py:83` | V19, V20 |
| F17 | Un TO nuevo | E0 sobre su PDF; E1 y E3 de sus unidades; ensamblado | E0, E1 y E3 de todas sus unidades; los demás TOs salen de la caché. Más F12 si necesita línea de alcance y F11 si necesita un sujeto nuevo | cambia (todas las del TO nuevo: sin clave previa) | cambia (todas las del TO nuevo; no verificable en el selftest: no hay salida de E1 previa) | E1 y E3 de las afectadas | 9 | `runner_corpus.py:444-470`; `prompt_v3_b54.py:428-456` | V23 |
| F18a | Un TO modificado en el sitio, con el cambio solo en páginas que E0 no convierte en unidades (portada, índice, tabla de origen, historial) | E0 sobre el PDF nuevo, dentro de una release declarada | ninguna llamada si E0 devuelve las mismas unidades byte a byte; se re-sella el sha del PDF en la release | no cambia (unidades idénticas) | no cambia (unidades idénticas) | nada | 9 | `e0_chunking/e0_lib.py:344-389`, `:678-679` | A1, A3 |
| F18b | Un TO modificado en el sitio, con cambio en páginas de cuerpo | E0 sobre el PDF nuevo, dentro de una release declarada | E1 y E3 de las unidades cuyo request cambia (filas F01 a F05 y F19); el resto sale de la caché | cambia (las unidades cuyo request cambia) | cambia (las unidades cuyo request cambia) | E1 y E3 de las afectadas | 9 | `e0_lib.py:678-679`; `prompt_e1.py:441-522` | V01, V02, V04, V07 |
| F19 | Una unidad agregada o retirada por un cambio de numeración | E0; la unidad nueva y las renumeradas cambian su número, el numeral del texto y la herencia de sus descendientes | E1 y E3 de la unidad nueva, de las hermanas renumeradas y de sus descendientes; una unidad retirada no llama a la API y sale del ensamblado en código | cambia (nueva, renumeradas y descendientes) | cambia (renumeradas y descendientes) | E1 y E3 de las afectadas | 9 | `prompt_e1.py:457-459`, `:473-486`; `comun_e1.py:63-87` | V24, V07 |

Notas a filas:

- **F03.** El mini-chunk del bloque cambió su propio texto: para él rige F01.
- **F05.** Como el id no entra al request, desambiguar los ids repetidos de la
  partición del corpus escalado (69 en cuatro TOs,
  `docs/tablero_correcciones.md:70`) no cambia ninguna clave; lo que cambia es
  la identidad de los registros persistidos, que el runner indexa por id
  (`runner_corpus.py:280-290`).
- **F08.** El docstring de `ratchet_e3.py:234-239` dice que cambiar
  `max_tokens` no invalida el caché: se refiere al caché de prefijo de la API.
  La clave de la caché local sí cambia, porque hashea `max_tokens`. Prueba con
  datos: la re-extracción dirigida de tres unidades de cap a 16.384 creó tres
  claves nuevas (anclaje A1).
- **F09 y F10.** `CODE_VER` se sube a mano «si cambia la lógica sin cambiar el
  prompt» (`cliente_e1.py:16-19`): es un cambio de solo código que, a propósito,
  obliga a pagar todo.
- **F12.** Hallazgo: los roles de `esquema_v2_clases.json` llegan al request de
  los cinco TOs de desarrollo sin pasar por ningún candado (V21: la clave de la
  unidad de cla cambia y el perfil se construye igual). Un cambio en ese JSON
  hace pagar en silencio todas las unidades del TO.
- **F14.** «Solo código» exige el crudo de E1 de cada unidad. El de la primera
  pasada está en `extracciones_e1.jsonl` (`runner_corpus.py:501`); el de las
  unidades aceptadas tras un reintento del ratchet, solo en
  `e3_verificador/cache/e1_reintentos.db` (en la tanda 0, 220 de 2.430
  unidades sobre `salida_dirigida/`, `docs/tablero_correcciones.md:69`). Esa db
  no se versiona: si se pierde, esas unidades pasan a la clase de las
  afectadas.
- **F18a.** E0 solo arma unidades con páginas de cuerpo (`e0_lib.py:678-679`).
  Caso a la vista: en la corrida del 2026-09-07, `ctacte` (TO de la tanda 0)
  cambió solo en la página 85 de 86, y el reporte muestra una lista de
  Comunicaciones «C» (`job_actualizacion/corridas/2026-09-07/reporte.md:80`).
  En la E0 de la tanda 0 esa página no pertenece a ninguna unidad: las
  unidades de ctacte usan las páginas 5 a 64, y E0 clasificó 60 páginas de
  cuerpo, 12 de historial y 10 de tabla de origen
  (`e0_chunking/salida_tanda0/conteos.json`, clave `ctacte`). Que E0 sobre el
  PDF nuevo devuelva las mismas unidades byte a byte es NO VERIFICADO: requiere
  correr E0 sobre ese PDF, que es de U-SUBGRAFO.
- **F19.** El selftest incorpora un punto antes de `pro::2.3`: se renumeran
  2.3 a 2.7 y cambian las claves de 42 de las 101 unidades de pro, en E1 y en
  E3. La caché no reconoce «mismo contenido, otro número».

## 4. El selftest

Comando, desde la raíz del repo:

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/mantenimiento/code/selftest_clave_cache.py --out data/experiment/mantenimiento/selftest_clave_cache.json
```

Qué hace (detalle en el docstring del script):

- **A1 y A3, anclaje.** Recalcula la clave de E1 de las 2.434 unidades de E0
  de la tanda 0 y la de la primera verificación de E3 de las 2.430 unidades
  aceptadas por E1 (`salida_dirigida/`), y las busca en las dbs de caché,
  abiertas en solo lectura (`mode=ro&immutable=1`).
- **V01 a V24, variaciones.** Una entrada por vez, sobre una muestra fija de
  diez unidades de la tanda 0, una por TO (`MUESTRA` en el script). V20 a V22
  corren en un proceso hijo que sirve el JSON alterado desde memoria; ningún
  archivo se escribe. V23 usa `snp_psp::1.3.1.1` de la partición. V24 recorre
  todo pro.
- **Contraste.** Lee esta tabla, toma de cada fila las columnas «Clave E1» y
  «Clave E3» y las variaciones, y las compara con lo observado. Una
  discrepancia hace que el selftest salga con código 1 (FRENO).

Resultado (salida en `selftest_clave_cache.json`):

- A1: 2.434 de 2.434 claves de E1 presentes en la db; la db tiene 2.437 en el
  namespace, y las 3 que sobran son exactamente las de la re-extracción
  dirigida de `cap::3.1.14.1`, `cap::4.2.1.2` y `cap::4.3.3.1` con
  `max_tokens` 16.384.
- A3: 2.430 de 2.430 claves de E3 presentes (la db tiene 5.013 en el
  namespace: también guarda re-verificaciones y corridas anteriores).
- V01 a V24: las 25 variaciones dan lo esperado, unidad por unidad.
- Inventario: el proceso hijo sin alteración reproduce las claves del padre, y
  ninguno de los módulos de validación, E2, ensamblado, E4 o esqueleto se
  carga al armar los requests.
- Contraste con esta tabla: OK, las 21 filas.

## 5. Costo de referencia por clase

| Clase | Costo de referencia | Ancla |
|---|---|---|
| nada | USD 0 | — |
| solo código sobre lo guardado | USD 0. Si se elige re-verificar en E3 las unidades cuya salida validada cambia, ese costo aparte; referencia para la matriz: cota del orden de USD 4 | principio 12, `docs/plan_tesis.md:299`; `docs/tablero_correcciones.md:49` |
| E1 y E3 de las afectadas | Promedio por unidad en la tanda 0: E1 USD 0,007425 (18,07154 / 2.434) y E3, con los reintentos del ratchet, USD 0,009179 (22,277978 / 2.427). Es un promedio, no una estimación: la re-extracción dirigida de tres unidades largas de cap costó USD 0,461274 (E1 0,1898, E3 0,2096, reintento 0,0618) | comando 1; `reextraccion_v2/corpus_tanda0/salida_dirigida/reextraccion_dirigida.json`, comando 2 |
| todo | E1 a E3 de los diez TOs de la tanda 0: USD 40,35 (recomputado: 40,349518) | `docs/plan_tesis.md:92` (ESTADO 28/09); comando 1 |

Comando 1 (gasto de E1 y E3 de la tanda 0, por fase cerrada):

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B -c "import json;d=json.load(open('data/experiment/reextraccion_v2/corpus_tanda0/salida/estado_corpus.json'))['fases_cerradas'];e1=[v for k,v in d.items() if k.endswith(':e1')];e3=[v for k,v in d.items() if k.endswith(':e3')];g1=sum(v['gasto_usd'] for v in e1);g3=sum(v['gasto_usd'] for v in e3);n1=sum(v['resumen']['n'] for v in e1);n3=sum(v['resumen']['n'] for v in e3);print(round(g1,6),n1,round(g1/n1,6),round(g3,6),n3,round(g3/n3,6),round(g1+g3,6))"
```

Salida: `18.07154 2434 0.007425 22.277978 2427 0.009179 40.349518`.

Comando 2 (gasto de la re-extracción dirigida):

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B -c "import json;d=json.load(open('data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida/reextraccion_dirigida.json'));print(d['gasto_combinado_usd'],{k:v['gasto_usd_real'] for k,v in d['clientes'].items()},sorted(d['casos']),d['max_tokens'])"
```

Salida: `0.461274 {'e1': 0.1898, 'e3': 0.2096, 'reint': 0.0618} ['cap::3.1.14.1', 'cap::4.2.1.2', 'cap::4.3.3.1'] 16384`.

## 6. Límites

- La tabla cubre el pipeline de la tanda 0 (perfil `v3_b54`, runner
  `corpus_v2/runner_corpus.py`). El perfil `produccion_dev`, con el que se
  construyó r1, arma otro request (`prompt_e1.build_request_kwargs`) y no lo
  verifiqué.
- El selftest prueba el efecto de cada cambio sobre la clave. Cuántas unidades
  afecta un cambio real de la fuente depende de cómo E0 extrae el texto del
  PDF nuevo (cortes de línea, guiones, pies de página); eso no lo mide esta
  etapa.
- Las dbs de caché no se versionan (`docs/laudo_release_r2_pipeline.md:307-312`):
  sin ellas el anclaje queda NO_VERIFICABLE y toda unidad pasa a pagarse.
