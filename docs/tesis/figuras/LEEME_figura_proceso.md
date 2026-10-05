# figura_proceso — registro de generación

Figura del proceso de construcción del grafo, para la introducción del
capítulo 4. Muestra de un vistazo las cinco piezas en el orden en que se
ejecutan, en dos filas a 15 cm de ancho. Arriba están el Texto Ordenado (PDF),
la Segmentación y las unidades de extracción. Abajo, el Extractor, el
Validador, el Verificador, el Ensamblado y el grafo. Entre las dos filas entran,
como datos, el esquema final (al Extractor y al Validador) y el catálogo de
sujetos (al Extractor, al Validador y al Ensamblado). Debajo está el ciclo del
Verificador: una flecha de vuelta al Extractor, rotulada «re-extracción, 1 vez»,
y una flecha discontinua a la revisión humana, rotulada «si no se resuelve».
Salen dos registros: los elementos rechazados (del Validador) y los sujetos
sin asignar, en cuarentena (del Ensamblado). La figura no lleva identificadores
internos, nombres de archivo, nombres de modelos ni cifras, salvo el «1» del
rótulo, y el generador lo controla.

Las piezas, su orden y qué hace cada una parten de VERIF-PIEZAS-ESCALADO
(03/10/2026, solo lectura, sobre HEAD `c50b094`), tareas 1, 4 y 8. Su reporte
quedó fuera del repo: `reporte_completo_VERIF_PIEZAS_ESCALADO.md`, sha256
`2f55f952b900a4b8cd28a13cd5d3bf707c1f6b48802da11e09f5b7d3444cacbb`, en el
paquete `revision_VERIF_PIEZAS_ESCALADO/`. Abajo lo cito como `VERIF:línea`.
Volví a leer en el código cada ancla que uso, en HEAD `4244028` (`git show
HEAD:<ruta>`). Entre `c50b094` y `4244028` no cambió ninguno de los archivos de
código citados (`git diff --stat c50b094 4244028 --` sobre
`data/experiment/{reextraccion_v2,pyd_r2,tanda0,esq,b54_catalogo_v3}` da
vacío). En la versión 2 repetí ese control hasta HEAD `5493f75`, también vacío.

## 1. Comandos

Desde la raíz del repo:

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_proceso.py
```

El generador escribe `figura_proceso.svg`, `.png` y `.pdf` junto a sí mismo.
Con `--salida <directorio>` los escribe en otro lugar, y así corrí las pruebas
de determinismo de §7. Con `--mutacion <nombre>` inyecta un defecto y tiene que
frenar sin escribir nada (§6). Usa solo la biblioteca estándar de Python (lo
corrí con el Python 3.10.13 del `.venv`) y `rsvg-convert` 2.62.3 para el PNG y
el PDF, como las figuras hermanas. No importa otros módulos del repo: los lee
como texto. No usa red ni API.

## 2. Fuentes y sellos

| Fuente | Qué toma la figura | Candado | Último commit |
|---|---|---|---|
| `docs/tesis/figuras/generar_figura_proceso_extraccion.py` | la paleta: `MODELO`, `DETERMINISTICA`, `NEUTRO`, `TINTA`, `TINTA_SUB`, `FLECHA` y `GRIS_ARISTA` (:91-97) | sha256 `6a91931abeb9927842f76fa50471497e926c69fc56617c62ef7f05ddf6c010d6` | `fbe69d4` |
| `docs/tesis/figuras/generar_figura_norma_a_grafo.py` | la tipografía `TIPOGRAFIA` (:80) | sha256 `9b0e45a299a0a078d250ccc999d192cbb83038bd8c00baa6bd8972d021b73f3d` | `fbe69d4` |
| `docs/tesis/figuras/generar_figura_experimento_estrategias.py` | el lienzo `W` (:186), el margen `MARGEN` (:194), la caja discontinua `DISCONTINUA` (:207, con grosor :676), los cuerpos y las interlíneas (:214-217), los márgenes internos (:219), los grosores (:220-222), el radio de los trazos (:223), las esquinas de caja (:407), los guiones (:408, :453), la leyenda (:654, :658) y el marcador de las puntas (:697-698) | sha256 `d68e1d87ba09bdb8faa7904400d042a7674cbd6ae5b8deb11dbfcf8163aa9755` | `0056841` |
| `data/experiment/reextraccion_v2/e3_verificador/ratchet_e3.py` | el tope de re-extracciones `TOPE_REINTENTOS = 1` (:70 en HEAD) | la línea del tope: una sola, y que valga 1 | `924ef4d` |

El generador coteja cada valor de estilo que usa contra la línea de la fuente
que lo declara (`ESTILO`), y la consola imprime esa línea. Si una fuente con
candado cambia, frena antes de dibujar.

Por qué `ratchet_e3.py` no lleva candado de sha256. Es código en desarrollo, y
la figura solo toma de él el tope. Durante esta unidad otra sesión de trabajo
lo modificó en el árbol, sin commitear, con un cambio que el docstring agregado
atribuye a la enmienda a LAUDO B, implementada en U-PROMPT-R2 P2 (`git diff --
data/experiment/reextraccion_v2/e3_verificador/ratchet_e3.py`). El generador lo había leído con el sha de HEAD (`e683f547…`) en la
corrida que escribió las salidas del repo (el SVG tiene hora de modificación
20:02:14). La última modificación del archivo es de las 20:02:21 (`stat`), y
su sha en el árbol ya no es el de HEAD. Con un candado de archivo entero, el
generador frenaría por un cambio que no toca nada de lo que dibuja. El candado es la línea `^TOPE_REINTENTOS = (\d+)$`: tiene que haber
una sola, con el valor 1. Si dice 2, el generador frena en `[contenido]`. Si
está dos veces, frena en `[fuentes]`. La revisión de la versión 1 aceptó este
candado. Lo probé sobre una copia en el
scratchpad, sin enlaces al repo. Con el `ratchet_e3.py` de HEAD, la copia
reproduce el SVG del repo byte a byte. En el árbol de hoy el tope está en :81 y
también vale 1.

Métrica de texto. Los anchos salen de las tablas AFM de Helvetica y
Helvetica-Bold (Adobe Core 14) copiadas en el script (`_AFM`). Las tomé de
`Helvetica.afm` (sha256 `db772f2830fb6d000907791d8d26a12524d96943a9a739e520ee855c6b25c96f`)
y `Helvetica-Bold.afm` (sha256 `8b697881c8ee617a177f6f2e2bbc88570b9fd2b9f0e89ecfc0f5507878f988fc`),
dos copias de las métricas de Adobe que trae matplotlib y que están fuera del
repo. Contra la Helvetica del sistema (`/System/Library/Fonts/Helvetica.ttc`,
medida con PIL en el scratchpad, que es como mide la figura hermana), la mayor
diferencia en que la real es más ancha es de +0,04 unidades. El resto son
reducciones por interletraje, de hasta 1,04 unidades en «Texto Ordenado», que
juegan a favor del control.

## 3. Fuente de cada afirmación que dibuja la figura

Rutas cortas: `rex/` = `data/experiment/reextraccion_v2/`, `t0/` =
`data/experiment/tanda0/code/` y `pyd/` = `data/experiment/pyd_r2/code/`. Las
líneas son las de HEAD `4244028`.

### 3.1 El orden de las piezas

| Tramo de la línea principal | Código | VERIF |
|---|---|---|
| Texto Ordenado (PDF) → Segmentación | `rex/e0_chunking/correr_e0.py:1043` (`correr`), `:1065` (el PDF de cada TO sale del manifiesto) | :26 |
| Segmentación → unidades de extracción | `rex/e0_chunking/correr_e0.py:14` (`chunks_<to>.json`, chunks terminales) | :33 |
| unidades → Extractor | `rex/corpus_v2/runner_corpus.py:514` (E1 carga los chunks de E0), `:540` (un pedido por chunk), `:544-546` (la llamada) | :27, :49-50 |
| Extractor → Validador | `rex/corpus_v2/runner_corpus.py:567-569` (cada salida pasa por `validador_e1.validar_salida`) | :28 |
| Validador → Verificador | `rex/e3_verificador/comun_e3.py:75-80` (a E3 llega solo la unidad que el validador no rechazó entera); `rex/corpus_v2/runner_corpus.py:1097-1141` (por TO, E1 en :1098-1115 y después E3 en :1116-1137) | :21, :167 |
| Verificador → Ensamblado | `rex/corpus_v2/runner_corpus.py:903-909` (el ensamblado toma el crudo del intento que E3 aceptó); `t0/ensamblar_tanda0.py:823` | :21-22, :204-209 |
| Ensamblado → grafo | `t0/ensamblar_tanda0.py:1028` (`<salida>/r2/kg.json`) | :36 |

### 3.2 Qué es modelo y qué es código

| Pieza | Color | Fuente | VERIF |
|---|---|---|---|
| Segmentación | azul (código) | `rex/e0_chunking/correr_e0.py:1043`; lee el PDF con `pdfplumber` (`rex/e0_chunking/e0_lib.py:181`) | :26 |
| Extractor | naranja (modelo) | `rex/corpus_v2/runner_corpus.py:89` (`MODEL_E1`), `:540`, `:544-546` | :27 |
| Validador | azul (código) | `rex/e1_extractor/validador_e1.py:89`; `pyd/validador_r2.py:437` | :28 |
| Verificador | naranja (modelo) | `rex/corpus_v2/runner_corpus.py:92` (`MODEL_E3`); `rex/e3_verificador/ratchet_e3.py:383` (la verificación con ese modelo) | :29 |
| Ensamblado | azul (código) | `t0/ensamblar_tanda0.py:804`, `:1001`, `:1097` | :31 |

Precisión. El Verificador tiene además una capa determinística en código, que
decide la aceptación (`rex/e3_verificador/ratchet_e3.py:121`; VERIF :170). La
figura lo pinta entero de naranja (decisión 6 del mandato).

### 3.3 Entradas laterales

| Flecha | Fuente | VERIF |
|---|---|---|
| esquema → Extractor | el prefijo de E1 declara los tipos y los predicados (`rex/e1_extractor/prompt_e1.py:57`, `:79`); el prefijo congelado (`data/experiment/esq/code/prompt_congelado.py:150-176`) y el del perfil vigente (`data/experiment/b54_catalogo_v3/code/prompt_v3_b54.py:382-394`); el tool schema (`:411-414`) | :63-68, :75-79 |
| esquema → Validador | `rex/e1_extractor/validador_e1.py:112-116` (tipos, predicados y firmas del esquema del perfil), que le pasa `rex/corpus_v2/runner_corpus.py:567-568`; en r2, la firma del esquema final (`pyd/validador_r2.py:784`, `pyd/modelos_r2.py:149-153`) | :103, :118-125 |
| catálogo → Extractor | la sección del catálogo cerrado en el prefijo (`rex/e1_extractor/prompt_e1.py:98`), el bloque del catálogo v3 (`data/experiment/b54_catalogo_v3/code/prompt_v3_b54.py:382-391`) y el enum de `sujeto_id` (`:409-414`) | :64-65, :77 |
| catálogo → Validador | `rex/e1_extractor/validador_e1.py:115`, `:304-307`; `rex/e1_extractor/perfil_e1.py:166`; en r2, `pyd/validador_r2.py:789-795` con el catálogo r2 bajo candado (`pyd/modelos_r2.py:54-61`) | :108-109, :136 |
| catálogo → Ensamblado | `t0/ensamblar_tanda0.py:813` (carga el catálogo r2), `:824` (resolución de sujetos con su índice), `:582-589` (redirección del catálogo) | :210-212, :225 |

Estado del esquema que recibe el Extractor. En HEAD `4244028` el extractor
recibe el esquema congelado con el catálogo v3: el perfil vigente es `v3_b54`
(`rex/e1_extractor/perfil_e1.py:56`, `:162-168`; VERIF :40, :84). El prefijo con
el esquema final es tarea de U-PROMPT-R2, P2.a
(`docs/mandatos/UPROMPT_R2_prefijo_nuevo.md@b901f6d:86-90`, `:214-217`), y en
HEAD no está. La flecha «esquema final → Extractor» describe el proceso tal
como va a escalar, no el código de HEAD (§9, observación 1).

### 3.4 El ciclo del Verificador

| Lo que dibuja | Fuente | VERIF |
|---|---|---|
| vuelta al Extractor | `rex/e3_verificador/ratchet_e3.py:408-412` (re-extrae con el modelo de E1), `:217` (el chunk completo, desde cero) | :177, :183 |
| «1 vez» | `rex/e3_verificador/ratchet_e3.py:70` (`TOPE_REINTENTOS = 1`), `:396` (el ciclo hasta el tope) | :182 |
| la re-extracción vuelve a pasar por el Validador y el Verificador (lo dibuja la línea principal) | `rex/e3_verificador/ratchet_e3.py:279-281` (valida con `validador_e1`), `:424-426` (re-verifica) | :28, :177 |
| revisión humana, «si no se resuelve» | `rex/e3_verificador/ratchet_e3.py:397-404` (veredicto sin cita verificable, sin re-extraer), `:414-420` (re-extracción inválida), `:433-437` (tope agotado); el registro con el pendiente de revisión humana, `:313-330` | :176-179, :280-281, :290-294 |

Lo que la figura no dibuja (decisión 3), con su fuente: la cola humana entra
al grafo marcada (`rex/corpus_v2/runner_corpus.py:906-907`, `:937-938`;
`rex/e2_reduce/e2_lib.py:807-812`), contra el pendiente de
`rex/e3_verificador/ratchet_e3.py:325-329`, que dice que no ingresa hasta
resolverse (VERIF :306-307). Quién revisa la cola en el escalado: NO ENCONTRADO
(VERIF :294).

### 3.5 Salidas registradas

| Salida | Fuente | VERIF |
|---|---|---|
| elementos rechazados, del Validador | rechazos con motivo de unidades enteras (`rex/e1_extractor/validador_e1.py:136-152`), de entidades (`:172-200`) y de relaciones (`:265-351`), registrados en el campo `validacion` de `extracciones_e1.jsonl` (`rex/corpus_v2/runner_corpus.py:512`, `:570-573`); en r2, unidades (`pyd/validador_r2.py:469-489`), entidades (`:507-534`) y relaciones (`:725-787`) | :104-110, :115-116, :121-126, :143-147 |
| sujetos sin asignar, en cuarentena, del Ensamblado | `rex/corpus_v2/r1_e4.py:438-443` (el sujeto sin resolver queda en cuarentena), `:446-455` (su fila en el registro); `t0/ensamblar_tanda0.py:909` (escribe `no_mapeados_sujetos.jsonl`) | :210-212, :241-242 |

Precisiones. El rótulo «Elementos rechazados» cubre los tres niveles en que
rechaza el Validador (unidad entera, entidad y relación), que se registran en el
mismo campo. En la versión 1 decía «Relaciones rechazadas» (§10). El sujeto en
cuarentena, además de quedar registrado, entra al grafo como sujeto propuesto
con la marca de cuarentena (`rex/e2_reduce/e2_lib.py:938-951`).

### 3.6 El Validador, un solo bloque

El validador corre en dos momentos (VERIF :28). Corre dentro de E1 y en la
re-extracción (`rex/corpus_v2/runner_corpus.py:567-569`;
`rex/e3_verificador/ratchet_e3.py:279-281`) y, en r2, a la entrada del
ensamblado (`t0/ensamblar_tanda0.py:814`, `:823`;
`rex/corpus_v2/runner_corpus.py:935`). La figura lo dibuja como un solo bloque,
entre el Extractor y el Verificador (decisión 5).

### 3.7 Lo que queda afuera

Nada de lo dibujado queda sin fuente. Quedan afuera, por el mandato o por no
ser piezas del proceso:
- la re-extracción dirigida, que fue un paso aparte y que el protocolo no
  menciona (VERIF :278-279);
- la partición por corte, que solo existe en el perfil r2
  (`rex/corpus_v2/runner_corpus.py:582-591`; VERIF :276);
- la E2 por TO del perfil de E1, que no es el grafo r2
  (`rex/corpus_v2/runner_corpus.py:1138-1141`; VERIF :30);
- el gate, que corre después, fuera de las piezas (VERIF :37).

## 4. Controles (todos en el script; el primero que falla FRENA y no se escribe nada)

Valores de la consola del generador (comando de §1):

1. contenido: 21 textos, exactamente los fijados (`TEXTO`, `ROTULOS`,
   `LEYENDA`). Ninguno lleva identificadores internos, nombres de archivo,
   nombres de modelos ni cifras, salvo el «1» del rótulo, que es el tope del
   código. Cada una de las 13 cajas tiene su clase (`CLASE`).
2. trazado: 16 flechas y 22 tramos, ningún tramo diagonal ni nulo. Cada flecha
   sale del borde de su caja (o de un tramo de su flecha madre, en la rama del
   catálogo al Validador) y llega al borde de su caja de destino, a 12 unidades
   o más de las esquinas. Las flechas son exactamente las de `CONEXIONES`.
3. cajas: 14 con la leyenda, sin superposiciones, con 20,4 unidades como
   mínimo entre bordes. Ningún trazo ni punta entra en una caja.
4. cruces: 0 cruces y 0 contactos entre flechas. La distancia mínima entre dos
   flechas es 22,3 unidades («Unidades → Extractor» / «Catálogo → Extractor»),
   con 3,0 exigidas. Ninguna punta toca otra flecha.
5. textos: ninguno superpuesto. Las distancias mínimas son 4,0 entre textos,
   4,0 de texto a trazo, 7,4 de texto a marca y 8,0 de texto al borde de su
   caja. La letra es de 13 unidades (7,27 pt) y de 14 unidades (7,83 pt)
   impresas a 15 cm.
6. rótulos: «re-extracción, 1 vez» queda a 4,0 de su tramo y a 66,0 de la flecha
   ajena más cercana; «si no se resuelve», a 4,0 y a 49,9.
7. margen: 76 elementos, todos a 2 mm o más del borde (izquierdo, superior y
   derecho 2,21 mm; inferior 2,27 mm).
8. registro y colores: el SVG se relee. Sus 63 elementos están registrados, en
   orden, y se controla el color de las 13 cajas, las 3 muestras de la leyenda
   y las 16 flechas.

## 5. Convenciones de dibujo

- Línea principal en flechas de `FLECHA` de 1,8. Entradas, salidas y la
  vuelta al Extractor en `FLECHA` de 1,6. La flecha a la revisión humana,
  discontinua en `GRIS_ARISTA`, como la de la revisión de la figura hermana.
- La revisión humana es la caja blanca de borde discontinuo de la figura
  hermana (`generar_figura_experimento_estrategias.py:207`, `:676`). No es una
  pieza de modelo ni de código, ni un dato, así que no entra en la leyenda de
  tres entradas. La tiene que explicar el epígrafe.
- El Texto Ordenado es la hoja con la esquina plegada y el grafo lleva el glifo
  de tres nodos, como en la figura hermana.
- Los nombres de las cajas van con inicial mayúscula, como las cajas de la
  figura hermana. Los rótulos de las flechas van en minúscula.

## 6. Pruebas negativas

Corren en cada ejecución, antes de escribir, sobre una copia del modelo de la
figura. Cada una tiene que frenar en su control y con su motivo, y si no frena,
el generador frena en `[pruebas]`. Con `--mutacion` se ve cada una sola, con
salida 1 y sin escribir nada:

```
rotulo_sobre_caja    [textos] «re-extracción, 1 vez» se superpone con la caja «validador»
tramo_diagonal       [trazado] tramo diagonal en «Validador → Verificador»: (327.0, 248.0) → (364.0, 258.0)
cruce_entre_flechas  [cruces] 1 cruce(s) entre flechas: «Verificador → Extractor» × «Verificador → Revisión humana» en (378, 356)
```

## 7. Composición, tamaño y salidas

Dos filas, porque las ocho cajas de la línea principal no entran en una. Con
los anchos de esta figura (`ancho_caja` del generador) suman 958 unidades sin
separaciones: hoja 128, Segmentación 116, unidades 178, cuatro piezas de 116 y
grafo 72. El ancho útil es de 736 unidades (760 menos 2 × 12 de margen). Con
las unidades en dos renglones suman 884, y con los nombres en negrita de 13
unidades (7,27 pt) y las unidades en dos renglones, 835: tampoco entran.

Lienzo de 760 × 486 unidades, impreso a 15,00 × 9,59 cm. El PNG mide
1772 × 1133 px a 300 dpi y el PDF, 425,20 × 271,84 pt.

| Archivo | sha256 |
|---|---|
| `generar_figura_proceso.py` | `8667c219fe5586466e3cad04bc81843a8b39025d59b443edbacf79740349cbbf` |
| `figura_proceso.svg` | `dac1d7bccce47b2cc6de928b6e1d374c89fbb73bebf66202f9ba90157648cd82` |
| `figura_proceso.png` | `f4e878b9e1ee407f68c3f13934032bc51d6828f182ad0a1c68b5285df7f96422` |
| `figura_proceso.pdf` | `edb11765a629b9d34bd1cd519f652146e09410b2d36f56cf226782eb17b01e45` |

Determinismo: corrí el generador tres veces con `--salida` en el scratchpad,
con `PYTHONHASHSEED` 0, 1 y 4242. Los tres SVG, PNG y PDF son idénticos entre
sí y a los del repo (`cmp`), y las tres consolas también. El PDF es
reproducible porque `rsvg-convert` corre con `SOURCE_DATE_EPOCH=0`.

## 8. Epígrafe

Lo redacta la autora. El epígrafe que propuse en la versión 1 quedó fuera de
este registro.

## 9. Observaciones para el texto del capítulo 4

1. El esquema final todavía no entra al Extractor en HEAD (§3.3). La figura
   dibuja el proceso tal como va a escalar. Si el texto describe el código de
   hoy, para el Extractor vale el esquema congelado hasta que se commitee
   U-PROMPT-R2 P2.
2. El Ensamblado también recibe el esquema final: le pasan la firma, los tipos
   y los predicados de r2 (`t0/ensamblar_tanda0.py:825-826`) y valida el grafo
   contra el modelo r2 (VERIF :238). Siguiendo la decisión 2 del mandato, la
   figura no dibuja esa entrada.
3. Resuelta en la versión 2: la caja dice «Elementos rechazados» y cubre las
   unidades enteras, las entidades y las relaciones que el Validador rechaza y
   registra (§3.5).
4. La caja de revisión humana no tiene salida. El código ingresa la cola al
   grafo con una marca, y el sujeto en cuarentena también entra al grafo como
   sujeto propuesto (§3.4, §3.5).
5. La paleta de la figura hermana llama «gris azulado» al color del código
   (`generar_figura_experimento_estrategias.py:20`); el mandato de la figura lo
   llama «azul».

## 10. Versiones

| Versión | Cambio | sha256 del generador / SVG / PNG / PDF |
|---|---|---|
| 1 (03/10/2026, FRENO) | primera versión; la caja de salida del Validador dice «Relaciones rechazadas» (175 × 40) | `e81378b3…` / `997721ff…` / `8822448a…` / `bd150822…` |
| 2 (03/10/2026) | la caja dice «Elementos rechazados» (172 × 40, centrada bajo el Validador como antes); en el generador cambian también la clave interna (`rechazados`) y el nombre de la flecha («Validador → Elementos rechazados»). Las demás cajas, flechas, rótulos y controles no cambian | `8667c219…` / `dac1d7bc…` / `f4e878b9…` / `edb11765…` |
