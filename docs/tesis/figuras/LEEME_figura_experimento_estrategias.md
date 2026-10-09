# figura_experimento_estrategias — registro de generación

Figura del experimento que comparó cinco estrategias de esquema (capítulo 3,
sección 3.7), como diagrama de flujo de izquierda a derecha en dos filas.
Arriba, la construcción: el conjunto de desarrollo (5 Textos Ordenados), las
cinco estrategias con sus nombres y los cinco grafos, uno por estrategia; a la
derecha, las 23 preguntas con su reparto por tipo. Abajo, la evaluación: el
agente, al que llegan los grafos y las preguntas; las 3 respuestas por pregunta
y grafo; el juez; y las 4 medidas. Debajo del juez, en una caja discontinua,
las afirmaciones que la referencia no decide, revisadas contra los Textos
Ordenados, con una flecha a «correctas», la única medida que esa revisión
cambia. La figura no lleva nombres de archivo, commits, ids de preguntas ni
nombres de run, y el generador lo controla.

Las anclas de las cifras parten de la verificación VERIF-SEC37 (02/10/2026,
solo lectura; su paquete quedó fuera del repo). En esta unidad volví a leer
cada ancla en el árbol y todas coinciden. Los seis archivos de los que el
generador lee cifras están sin cambios respecto de HEAD (`2a76276`), y el último
commit de cada uno es el que figura en la tabla de §2.

## 1. Cómo regenerar

Desde la raíz del repo:

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_experimento_estrategias.py
```

El generador escribe `figura_experimento_estrategias.svg`, `.png` y `.pdf`
junto a sí mismo; con `--salida <directorio>` los escribe en otro lugar, y así
corrí las pruebas de determinismo de §6. Requiere `rsvg-convert` 2.62.3, PIL
12.3.0 y pypdf 6.10.2 (los del `.venv`) y la Helvetica del sistema
(`/System/Library/Fonts/Helvetica.ttc`): sin las métricas reales de Helvetica
no compone la figura. Importa de `generar_figura_proceso_extraccion.py` la
paleta, la tipografía y la leyenda, y de `generar_figura_norma_a_grafo.py` el
escape y el formato del SVG y, desde el 08/10/2026, el medidor y la densidad
del PNG (§8). No usa red ni API.

## 2. Fuente de cada cifra

El generador lee seis fuentes con candado de sha256 (`FUENTES`); si una cambia,
frena antes de dibujar.

| Fuente | sha256 | Último commit |
|---|---|---|
| `data/experiment/evaluacion/queries/eval_set_v1.json` | `aabe36d2b6b519dc82a56841fe315db9600e669115d7efa170978f96ea9c1931` | `7d118ee` (09/06/2026) |
| `data/experiment/evaluacion/harness.py` | `fd267e833866f86850e43130e627b08d78e05523b97484696de0ab0c8c9fba9e` | `7e8b91e` (10/06/2026) |
| `data/experiment/evaluacion/judge.py` | `7169145aaeb3f2d90a7e3873964378aa6520c5688fed136cf5a79ea63b589eaa` | `1910df5` (09/06/2026) |
| `data/experiment/evaluacion/run_frozen.py` | `b460a4455bb1e9a6b512c9acd99bde6e7720229e113451b6ed59c8155fb6b067` | `d56020e` (23/06/2026) |
| `data/experiment/evaluacion/adjudicacion_FIRMADO.json` | `9f1bd89e1bbb1e669c50d654e75bd1df9ba17f61b1bc740a9a0c61166c25abda` | `d56020e` |
| `data/experiment/evaluacion/frozen_run/reporte_final.md` | `a91291f9d02c35fd5c54251bc558b4a380b1c9f19e9cc6b871c33c00c2d7f0f0` | `d56020e` |

Rutas abreviadas en la tabla siguiente: `eval_set_v1.json`, `harness.py`,
`judge.py`, `run_frozen.py`, `adjudicacion_FIRMADO.json` y `reporte_final.md`
son las de arriba; `run_etapa2.py` es
`data/experiment/evaluacion/runners/run_etapa2.py` (commit `7acd022`, que lo
movió desde `d56020e`).

| Texto de la figura | Fuente | Control del generador |
|---|---|---|
| «Conjunto de desarrollo», «5 Textos Ordenados» | `eval_set_v1.json:8-14` (los cinco TOs del bloque `corpus`) y `:5` («sobre 5 Textos Ordenados»); los cinco extractores leen `data/experiment/subset/` (`run_1_cookbook/code/common.py:27`, `run_2_papers/code/run_full.py:71`, `run_3_ppf_core/code/chunker.py:30`, `run_4_schema_light/code/chunk.py:30`, `run_5_hybrid/code/extract.py:56`) | `corpus` tiene 5 entradas |
| «5 estrategias de esquema» y los nombres «Receta genérica», «Vocabulario controlado», «Esquema cerrado», «Emergente», «Híbrida» | tesis, sección 3.7, tabla de las cinco estrategias (Overleaf); cada estrategia con el grafo que construyó: receta genérica, `data/experiment/run_1_cookbook/` (`schema.md:1`); vocabulario controlado, `run_2_papers/` (`schema.md:4`); esquema cerrado, `run_3_ppf_core/` (`schema.md:3`); emergente, `run_4_schema_light/` (`schema.md:1`, `:4`); híbrida, `run_5_hybrid/` (`schema.md:1`) | cinco estrategias, cada una con su `kg.json` y con la carpeta de trazas de su prefijo |
| «5 grafos» | `data/experiment/run_{1_cookbook,2_papers,3_ppf_core,4_schema_light,5_hybrid}/kg.json`, commits `e4de649` (25/05/2026), `9e363a9`, `58581b6`, `9d27d51` (27/05/2026) y `199649c` (03/06/2026); los cinco evaluados: carpetas de `frozen_run/traces/` y `reporte_final.md:3` («× 5 grafos») | 5 carpetas de trazas |
| «23 preguntas» | `eval_set_v1.json:21` (`"total": 23`) | 23 preguntas en el archivo, igual al total declarado |
| «10 de dato directo, 5 de varias normas, 4 de restricción hasta su excepción, 4 sin respuesta» | `eval_set_v1.json:23-26` (`distribucion`); las categorías, en `:16-19` (`factual_directa`, `multi_norma`, `cadena_restriccion_excepcion`, `unanswerable`, en ese orden) | el conteo de `categoria` de las 23 es `distribucion`, y el texto se coteja con ese conteo |
| «3 herramientas: buscar, abrir, listar vecinos» | `harness.py:242`, `:259`, `:271` (herramientas `buscar_nodos`, `ver_nodo`, `ver_vecinos`), descriptas en `:10-15` | las tres herramientas, en ese orden |
| «tope de 15 llamadas» | `harness.py:50` (`MAX_TOOL_CALLS = 15`) y `:21`; el control, en `:527-528` | la constante, y que el control sea el de `:527` |
| «3 respuestas por pregunta y grafo» | `run_frozen.py:829` (`--N`, 3 por defecto) y `:5`; `reporte_final.md:3` («N=3») | `--N` vale 3 y los 115 archivos de trazas (5 × 23) tienen las repeticiones 1, 2 y 3: 345 corridas |
| «2 pasos: descompone en afirmaciones y las verifica contra la referencia» | `judge.py:95` (paso 1, descomposición sin ver la referencia; instrucciones en `:97`) y `:127` (paso 2, verificación contra la referencia; `:129`) | exactamente dos bloques `# Paso N` |
| «Afirmaciones que la referencia no decide» | `judge.py:57-62`: la afirmación que la referencia no soporta no baja la correctitud, y la traza con afirmaciones centrales no soportadas va a la cola de adjudicación; la cola tiene solo centrales (`run_etapa2.py:10`) | el juez declara la cola (`requiere_adjudicacion_humana=true`) |
| «revisadas contra los Textos Ordenados» | `adjudicacion_FIRMADO.json:11` (método: «verificación afirmación-por-afirmación contra los 5 PDFs del subset»), `:10` (2026-06-10) y `:22` (`firmado`); 200 afirmaciones únicas (`:5`) | método con «contra los 5 PDFs del subset» y estado firmado |
| flecha de la revisión a «correctas» | `reporte_final.md:45` (estabilidad, límite y citas, «no afectadas por la adjudicación»); `run_etapa2.py:5` (la adjudicación recomputa la correctitud) | la línea `:45`, tal cual |
| «4 medidas»: «correctas», «estables», «citas a nivel de punto», «límite agotado» | correctas, `reporte_final.md:35-43` (sobre 19 preguntas con respuesta); estables, límite agotado y citas a nivel de punto, columnas «Estabilidad», «hit_limit» y «prec punto» de `reporte_final.md:47-53`; definiciones en `run_frozen.py:352` (moda y unanimidad), `:441` (estabilidad), `run_etapa2.py:255` (precisión de cita modal) y `harness.py:527-528` (límite) | las líneas `:35` y `:47`, tal cual; cuatro medidas |

Colores y leyenda. La leyenda es la de `generar_figura_proceso_extraccion.py:137-138`,
importada con su texto. Van en naranja (etapa que ejecuta un modelo de
lenguaje) las cinco extracciones, el agente y el juez. Las cinco extracciones
usan Haiku 4.5 (`run_1_cookbook/code/02_extract.py:49`,
`run_2_papers/code/extract.py:40`, `run_3_ppf_core/code/extract.py:46`,
`run_4_schema_light/code/extract.py:40`, `run_5_hybrid/code/extract.py:39`), y
la receta genérica usó además Sonnet 4.6 para resolver entidades y resumir
nodos (`run_1_cookbook/report.md:14`, `:16`; `run_1_cookbook/code/03_resolve.py:46`).
El agente es Haiku 4.5 (`harness.py:47`) y el juez, Sonnet 4.6 (`judge.py:87`).
Va en gris azulado (etapa determinística) el cálculo de las medidas, que se
hace en código (`run_frozen.py:363`, `run_etapa2.py`). Las cajas neutras son lo
que entra y sale, y la discontinua es la de la salida lateral de la figura
hermana.

## 3. Lo que la figura agrega a la lista de contenidos

La lista de contenidos y sus textos estaban fijados; la figura agrega, como
decisiones de dibujo para revisar:

1. los encabezados de columna «5 estrategias de esquema» y «5 grafos», y los
   rótulos en negrita «Conjunto de desarrollo», «23 preguntas», «Agente»,
   «3 respuestas», «Juez», «Afirmaciones que la referencia no decide» y
   «4 medidas»;
2. las flechas: del conjunto a cada estrategia, de cada estrategia a su grafo,
   de los grafos y de las preguntas al agente, el flujo de la fila de abajo,
   del juez a la revisión y de la revisión a «correctas»;
3. el color por clase de etapa y la leyenda de la figura hermana;
4. los cortes de línea (`CORTES`), que el generador comprueba que no cambien el
   texto.

De estos, la flecha a «correctas» y la leyenda afirman algo más que la lista;
sus fuentes están en §2.

## 4. Controles

En cada corrida, el generador frena sin escribir nada si alguno falla. Salida
de la corrida que escribió los archivos del repo:

```
CONTENIDO: 35 textos; fallas: 0
TEXTOS (métricas reales de Helvetica) contra 35 textos, 20 cajas, 35 marcas y 21 trazos (17 con punta); fallas: 0
  distancias mínimas: texto-texto 4.0; texto-trazo 10.4; texto-marca 12.5; texto-borde de su caja 7.5
TRAZOS: 0 trazos o puntas en el interior de una caja; distancia mínima entre trazos de grupos distintos 12.0 (de los grafos al agente / de las preguntas al agente), exigida 3.0; fallas: 0
MARGEN (128 elementos): mínimo a cada borde izquierdo 11.2 u = 2.21 mm, superior 14.0 u = 2.76 mm, derecho 11.2 u = 2.21 mm, inferior 11.4 u = 2.24 mm; exigido 2.0 mm (10.1 u); fallas: 0
REGISTRO: 111 elementos del SVG, todos registrados; fallas: 0
```

- Contenido: lo dibujado reconstruye el texto fijado, pieza por pieza, y ningún
  texto lleva extensiones de archivo, rutas, `::`, guiones bajos, hashes, ids
  de preguntas, «run» ni los nombres de las carpetas de los grafos
  (`PROHIBIDOS`). Además, cada número del texto se coteja con su fuente (§2).
- Textos: ninguno por debajo de 7 pt impresos, fuera del lienzo, fuera de su
  caja (holgura mínima: medio grosor del borde más 1,5 unidades), cortado por
  otra caja, superpuesto a otro texto, ni tocado por una marca (renglones,
  pliegue, nodos y aristas de los grafos), un trazo o una punta de flecha. Las
  cajas de texto se miden con las métricas reales de Helvetica; los trazos se
  controlan con su geometría real, con cada esquina redondeada muestreada en
  diez puntos, y las puntas de flecha con su triángulo.
- Trazos: ninguno entra en el interior de una caja, y dos trazos de grupos
  distintos no pasan a menos de 3 unidades.
- Margen: ningún texto ni elemento dibujado a menos de 2 mm de un borde.
- Registro: el SVG se relee y sus 111 elementos (35 textos, 19 rectángulos, 42
  trazados y 15 círculos) se cotejan uno a uno, en orden, con lo registrado en
  los controles anteriores; nada se dibuja fuera de ellos.

Prueba de que el control detecta lo que debe. Corrí tres mutaciones sobre una
copia espejo en el scratchpad (con `data/` enlazado, solo para leer), y las
tres frenaron sin escribir nada:

| Mutación | Resultado |
|---|---|
| grafos 86 unidades más a la izquierda, encimados sobre las estrategias | 28 fallas de textos (entre ellas, «'5 estrategias de esquema' se superpone con '5 grafos'» y cuatro nombres de estrategia sobre una caja de grafo) y 25 de trazos |
| cajas de estrategia de 120 en lugar de 170 de ancho | 4 fallas de textos («Vocabulario controlado» se sale de su caja y lo tocan dos trazos y una punta) |
| conector de las preguntas al agente desviado a la altura de la tercera estrategia | 4 fallas de textos («Esquema cerrado» y tres líneas del reparto tocadas por el trazo) y 9 de trazos (3 entradas en cajas) |

Control independiente: `docs/tesis/figuras/verificar_geometria_svg.py` sobre
el SVG del repo da «35 textos, 0 nodos, 17 trazos con flecha; fallas: 0». Ese
script busca nodos de grafo con `rx="7"`, que esta figura no tiene, así que
aquí controla solo la superposición entre textos.

## 5. Composición

Lienzo de 760 unidades de ancho, impreso a 15 cm (el ancho de texto de la
página): la letra de 13 unidades queda en 7,27 pt y la de 14 en 7,83 pt, por
encima del mínimo de 7 pt de las figuras hermanas a 15 cm. Alto: 483 unidades,
9,53 cm impresos. Las dos filas leen de izquierda a derecha. En la de arriba,
el conjunto reparte en las cinco estrategias, y cada estrategia lleva a su
grafo. Los grafos convergen en un colector que baja al agente, y la caja de las
preguntas, a la derecha, baja al agente por un segundo conector, 12 unidades
más abajo, que entra al agente más a la derecha; así los dos no se cruzan. En la de abajo, el agente, las
respuestas, el juez y las medidas tienen el mismo alto, con 30 unidades entre
cajas. La leyenda va abajo a la izquierda. La revisión va debajo del juez, a 24
unidades de la leyenda, y su flecha a «correctas» sube por un carril a la
derecha de las medidas y entra a la caja a la altura de esa línea.

## 6. Salidas y reproducibilidad

| Archivo | sha256 |
|---|---|
| `generar_figura_experimento_estrategias.py` | `71831ab9feab1cb8bd06cd714c4185a4e3d21f1fb02b60a2a69ef6dddd968b6a` (§9; antes, `f889c4bf…`, §8, y hasta el 08/10/2026, `d68e1d87ba09bdb8faa7904400d042a7674cbd6ae5b8deb11dbfcf8163aa9755`) |
| `figura_experimento_estrategias.svg` (760 × 483) | `cba5166e6c0c7a781094aae4e11dd84b9257ed495776b9233c736fff8c2b476b` (hasta el 08/10/2026, `734a712e4d89053f8302bd173f7129d77073dac3d6565e1e005a430b6a3bab27`; §9) |
| `figura_experimento_estrategias.png` (1772 × 1126 px, 300 dpi) | `240b12701173e5a51c02690aa54e22ce3894619588e8bbbb7c0d734cef760fca` (hasta el 08/10/2026, `d3e00a7ca44bf0f572124655bbcabaf2d3a74f38476b3b97a0d4f1e546ea5109`; §9) |
| `figura_experimento_estrategias.pdf` (425,2 × 270,1 pt) | `d93a46561193bb2bc8bf989b3dc37853eeeca583476f9fd7e03e61f1da4f6c68` (hasta el 08/10/2026, `29146d497f63e24d662a3c4331b9cbabd60169abcb7d506cc0fadefac32656ea`; §9) |

Cuatro corridas del generador final: tres sobre el scratchpad de la sesión con
`--salida`, con `PYTHONHASHSEED` 0, 1 y 42, y la que escribió los archivos del
repo, con `PYTHONHASHSEED` 0. El SVG, el PNG y el PDF salieron idénticos byte a
byte en las cuatro, y la salida de consola (28 líneas) también, salvo las rutas
de salida. El PDF es reproducible porque el script fija `SOURCE_DATE_EPOCH=0`
al llamar a `rsvg-convert`, como las figuras hermanas: `/CreationDate`
01/01/1970. El stream de contenido de su página tiene sha256
`2f250f5fa1332f4c70dbc649f738c6f9814d265b587901a6628998465f734a5a` (hasta el 08/10/2026, `55edb90f…`; §9). Las fuentes
del PDF siguen el patrón de los PDF hermanos: Helvetica y Helvetica-Bold
embebidas, cada una con su Type 3 de cairo (`pdffonts`).

Este LEEME cae bajo `.gitignore:180` (`docs/tesis/figuras/*`), sin excepción que
lo libere, así que entra a git solo forzado, con `git add -f`, como los LEEME
hermanos. El generador, el PNG, el SVG y el PDF entran por las excepciones
`.gitignore:208`, `:186`, `:187` y `:188` (`git check-ignore -v --no-index`).

## 7. Observaciones para el texto de la sección 3.7

1. «Híbrida». La figura usa el nombre fijado. En la copia de la tesis del repo
   (`docs/tesis/main.tex`, desactualizada respecto de Overleaf), la fila de la
   tabla de la sección 3.7 dice «Híbrido» y la prosa, «híbrida». En Overleaf:
   NO VERIFICADO. La tabla y la figura deberían usar el mismo nombre.
2. Tope de 15 llamadas. Es la constante del agente, pero el control corre al
   cerrar cada turno (`harness.py:527-528`), así que 46 de las 345 repeticiones
   pasaron de 15 llamadas: 13, 7, 2, 17 y 7, en el orden de las estrategias. Se
   reproduce con:

   ```bash
   PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B -c "import json,glob; t={g: [r for f in sorted(glob.glob('data/experiment/evaluacion/frozen_run/traces/'+g+'/*.json')) for r in json.load(open(f))] for g in ['run_1','run_2','run_3','run_4','run_5']}; print([sum((r.get('tool_calls_used') or 0) > 15 for r in v) for v in t.values()], sum(len(v) for v in t.values()))"
   ```

   La salida es `[13, 7, 2, 17, 7] 345`. El epígrafe puede decir «tope de 15
   llamadas por pregunta, controlado al cerrar cada turno».
3. La revisión de las afirmaciones cambia solo «correctas»: las otras tres
   medidas se calculan antes de la adjudicación (`reporte_final.md:45`). La
   flecha lo muestra; el epígrafe puede decirlo.

## 8. Nota del 08/10/2026: el medidor, `DPI` y la densidad, de `generar_figura_norma_a_grafo.py`

Un cambio en el generador, ninguno en la figura:

- **Qué fallaba.** Desde `88bfe89`, `generar_figura_proceso_extraccion.py` ya no
  tiene `DPI`, `grabar_densidad` ni `medidor`. El generador fallaba al
  importarse, con `AttributeError` en `DPI = proc.DPI` (:189), antes de llegar a
  la llamada `proc.medidor()` (:971): no corría en HEAD.
- **Qué cambió.** Los tres salen ahora de `generar_figura_norma_a_grafo.py`
  (sha256 `618789ae…`), que el generador ya importaba como `base`: `base.DPI`
  (:189; vale 300, como antes), `base.grabar_densidad` (:932; la función de
  :1049 de ese archivo, igual a la que tenía
  `generar_figura_proceso_extraccion.py` en `fbe69d4`) y `base.medidor()` (:971;
  la función de :806). El comentario de `MEDIR` (:390) dice `base.medidor`; el
  docstring no nombra el medidor. De `generar_figura_proceso_extraccion.py`
  (sha256 `f4842a6a…`) sigue tomando `ANCHO_TEXTO_CM`, `PT_POR_CM`, `LEYENDA`,
  `MODELO`, `DETERMINISTICA`, `NEUTRO`, `TINTA`, `TINTA_SUB`, `FLECHA` y
  `GRIS_ARISTA`, con los mismos valores que en `fbe69d4`.
- **El medidor.** `base.medidor()` difiere del de `fbe69d4` en dos cosas: si
  faltan PIL o la fuente del sistema, frena en lugar de devolver `None`, así que
  el freno propio de :972-973 ya no se alcanza; y carga la fuente a
  `int(round(fs * 10))` en lugar de `fs * 10`. Ninguna de las dos cambia esta
  figura.

El script tiene las mismas líneas (1029) y su sha256 pasó de `d68e1d87…` a
`f889c4bf…` (§6). Sobre una copia del repo, con `PYTHONHASHSEED` 0, 1 y 4242, el
SVG, el PNG y el PDF salen idénticos byte a byte a los commiteados; registros en
el paquete de revisión de FIX-MEDIDOR-8.

## 9. Nota del 08/10/2026: «3 herramientas» en la caja del agente

La caja del agente dice «3 herramientas: buscar, abrir, listar vecinos» en lugar
de «3 operaciones: buscar, abrir, listar vecinos». La figura no tiene otro cambio.

- **Generador.** Cambian el texto (`TEXTO`, :142), su corte de línea (`CORTES`,
  :159) y el texto que arma el control que lo coteja con el número de
  herramientas del agente (:369-370). Las dos líneas del docstring que describen
  esa caja (:10 y :31) dicen «herramientas». La clave `agente_operaciones`, la
  tupla `OPERACIONES` (:131) y su comentario (:129-130) quedan como estaban: no
  se dibujan. El script tiene las mismas líneas (1029) y su sha256 pasó de
  `f889c4bf…` a `71831ab9…` (§6).
- **SVG.** Cambia una sola línea, la 85: el contenido del `<text>` de la
  primera línea de la caja (x 92,0, y 318,6, centrado, cuerpo 13), con los mismos
  atributos. El viewBox sigue en 760 × 483. La línea pasa de 130,8 a 135,9
  unidades de ancho, medida con el medidor de Helvetica, y cabe en la caja con
  12,1 unidades de holgura a cada lado.
- **PNG y PDF.** El PNG mantiene 1772 × 1126 px y la misma densidad; el PDF,
  425,2 × 270,1 pt, rasterizado a 4 px/pt. En los dos, todos los píxeles
  distintos caen dentro del rectángulo de ese texto. Las 99 palabras que
  pdfplumber extrae del PDF son las mismas, salvo «operaciones:» →
  «herramientas:».
- **Controles.** La consola del generador da las mismas 28 líneas; solo cambian
  los sha256 de las salidas. Los controles de §4 dan los mismos valores.
- **Corridas.** Sobre una copia del repo, con `PYTHONHASHSEED` 0, 1 y 4242, el
  SVG, el PNG y el PDF salen iguales en las tres corridas (§6). Registros y
  verificación en el paquete de revisión del ajuste 1 de FIX-MEDIDOR-8.
- **PENDIENTE: el generador de la figura del proceso.**
  `generar_figura_proceso.py` tiene un candado de sha256 sobre este generador
  (`hermana`, :125-126), que sigue en `d68e1d87…`, el sha anterior a §8. Ese
  generador no corre desde `88bfe89`: frena antes, en sus candados sobre
  `generar_figura_proceso_extraccion.py` y `generar_figura_norma_a_grafo.py`
  (:121-124).
