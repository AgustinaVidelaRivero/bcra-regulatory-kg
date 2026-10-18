# FRENO T4 — tanda 1 de B6.1, primer tramo: los sorteos de (1) y (3), la (12) rehecha, el material, lo que queda a la vista y la lectura asistida (USD 0, sin API, sin commit)

Rigen el pre-registro firmado (`docs/preregistro_tanda1.md`, firma en `95b18217`, con su nota del 17/10/2026 en `ca5b39fd`), el «seguí» de
T4 y lo que decidió la autora el 18/10/2026 sobre el FRENO T3 (va a la §29 del registro de decisiones). HEAD `764768a4`.

**Resultado:**
- **Las poblaciones y los sorteos** (secciones 3 y 4): (1), 1.401 nodos Condicion; (3), 181 grupos; la (12), 18.483 aristas con el universo de la decisión 1.2 (A4.1 tal cual daba 28.062). Tres muestras de 30, en dos corridas iguales.
- **El material** (sección 5): 90 fichas, con el control en 0 claves vedadas.
- **Lo que queda a la vista** (sección 6), con la regla de la decisión 1.1: 216 unidades en las ocho muestras que se leen (primera 30, final 186). Con la regla de T3 serían 2.983.
- **La lectura asistida** (sección 7) de las 8 muestras, con una propuesta y una justificación que cita el texto por elemento. Doy solo cuántas propuestas hay de cada respuesta (tabla 5). Sin tasas, sin atención y sin ampliación: son del segundo tramo.
- **Las planillas de la autora** (sección 8): 8, con el `LEEME` y el convertidor, probado sobre una copia. El sello es de la autora.
- Toda cifra sale por script de sus archivos. Las tablas que copio de una salida van tal cual; mis aclaraciones van fuera de las tablas.
- Nada commiteado y ningún mensaje de commit preparado: los commits son de la autora y quedan PENDIENTES.

## 1. Paso 0 (18/10/2026, 11:46)

```
$ pwd
$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg
$ git log -1 --format='%h %s'
764768a4 Alcance de la tanda final: la lectura de la autora, sellada y controlada, en el registro
$ git log --format='%h %s' -4
764768a4 Alcance de la tanda final: la lectura de la autora, sellada y controlada, en el registro
c0d3ab17 Mandato firmado: el sorteo y las fichas de la medicion del verificador, a ciegas para la autora
050940b0 Primera tanda: el sello de sus dos grafos, segundo commit
eb0711a1 Primera tanda: el gate, el registro de sus dos grafos, lo contado sin leer y la preparacion de sus lecturas
$ git status --porcelain --untracked-files=no | wc -l
       0
$ shasum -a 256 <los cuatro kg.json>
22e83a62cb88e5bbe31b64a0f2322194bc2ffd2622ea7adc2c07310d8a02c7c7  data/experiment/reextraccion_v2/corpus_tanda1/ens_veinte_r2b/r2/kg.json
384a6d5bc139cd7b74d86840c68e7034b7a9bcb4bc26da7c61567f3f053e624e  data/experiment/reextraccion_v2/corpus_tanda1/ens_veinte_r2b_sincola/r2/kg.json
e63536d15bd8f575f1b7680921e3ca0d4956bdc5e38dc3f2fea27bb67bd71769  data/experiment/tanda1/t3/acumulado/ens_treinta_r2b/r2/kg.json
0435d41f9c7b45ea10cc87e8121fcfb8b3d2b089af837fff377a3460ced9636c  data/experiment/tanda1/t3/acumulado/ens_treinta_r2b_sincola/r2/kg.json
$ grep -n "commit_sellado" data/experiment/neo4j/grafos.py | tail -2
253:        "commit_sellado": "eb0711a",
267:        "commit_sellado": "eb0711a",
$ pgrep -fl "runner_corpus.py|ensamblar_tanda0.py|regression_kg.py|shapes_validator.py"
(rc=1)
$ python3 -B data/experiment/tanda1/t2/foto_repo_tanda1_t2.py . <scratchpad>/t4t1/foto_repo_antes_T4t1_cruda.json
2026-10-18 11:46:06 2026-10-18 11:46:18 52450 entradas
$ python3 -B data/experiment/tanda1/t2/foto_repo_tanda1_t2.py --comparar <foto de después de T3> <esta foto>
antes 52448 despues 52450
nuevos: data/experiment/tanda1/t3/FRENO_T3.md, docs/mandatos/UMED_VERIF_FICHAS_armado_de_las_fichas.md
borrados: ninguno
cambiados: .DS_Store, data/backlog/backlog.jsonl, data/experiment/catalogo_unico/registro_alcance_por_tanda.md,
  data/experiment/escalado_prep/.DS_Store, data/experiment/neo4j/grafos.py, docs/.DS_Store, docs/tesis/.DS_Store
$ git diff --name-status 0c927ebb 764768a4 (fuera de corpus_tanda1/ y de tanda1/t3/)
M data/backlog/backlog.jsonl
M data/experiment/catalogo_unico/registro_alcance_por_tanda.md
M data/experiment/neo4j/grafos.py
A docs/mandatos/UMED_VERIF_FICHAS_armado_de_las_fichas.md
M scripts/regression_kg_esperado.json
$ shasum -a 256 <cada archivo nuevo o cambiado que trajeron los commits> y git show HEAD:<el mismo>
iguales los cinco: FRENO_T3.md (9c474341…), UMED_VERIF_FICHAS_armado_de_las_fichas.md (396847ce…), backlog.jsonl (200855b6…),
  registro_alcance_por_tanda.md (a4b52cd2…), grafos.py (cec1ec71…)
$ stat (sin abrirlos) de los cuatro .DS_Store; git check-ignore -v
2026-10-18 11:11:36  12292 bytes  .DS_Store                                .gitignore:25
2026-10-18 11:42:43   8196 bytes  data/experiment/escalado_prep/.DS_Store   .gitignore:25
2026-10-18 11:11:36  26628 bytes  docs/.DS_Store                           .gitignore:25
2026-10-18 11:12:36  12292 bytes  docs/tesis/.DS_Store                     .gitignore:172
```

- La foto de comparación es la de después de T3 (`foto_repo_despues_T3f_cruda.json`, 10:26:08), que va en el paquete. Los commits
  `eb0711a1`, `050940b0`, `c0d3ab17` y `764768a4` trajeron, además, archivos que ya estaban en el disco con los mismos bytes (las
  salidas de `corpus_tanda1/` y de `tanda1/t3/`): la foto no los ve como cambios.
- **Los cuatro `.DS_Store`** no vienen de ningún commit: cambiaron entre las 11:11:36 y las 11:42:43, después del cierre de T3, y están
  ignorados por git. Son archivos de metadatos de carpeta de macOS; qué los cambió: NO VERIFICADO. No los abrí.
  - Lo pregunté antes de escribir nada, como pide el mandato si algo da otra cosa. La autora indicó seguir y declararlos, sin abrirlos, y
    que otro `.DS_Store` que aparezca durante la unidad tampoco frena.
- `pgrep` salió vacío. Los `.pyc`: 11.236 líneas, iguales a las del cierre de T3.

## 2. Lo decidido el 18/10/2026 y cómo lo apliqué

1. **La lista de exclusión de U-MED-VERIF, con los nodos compartidos** (punto 1.1). `unidades_a_la_vista_t4t1.py` suma la unidad de cada ficha de unidad (versión final) o de cola (versión primera), y las unidades de procedencia de todo otro nodo que muestra una ficha. No suma un TextoOrdenado ni un Sujeto con más de una unidad de procedencia. Un Sujeto con una sola unidad suma.
   - Los nodos que muestra una ficha: en una de unidad, los suyos y los dos extremos de cada arista; en una de arista, sus dos nodos; en una de (1), el nodo y el otro nodo de cada arista; en una de (3), los nodos del grupo.
   - Las aristas que muestran las fichas de (1) y de la (12) tienen su unidad de procedencia en la lista en todas las muestras (tabla 4, información): ninguna arista queda a la vista sin su unidad.
2. **El universo de la observación (12)** (punto 1.2). `poblaciones_t4t1.py` resta de todas las aristas del grafo evaluado las `referencia`, las de `rol_fuente = esqueleto`, las `establecida_en` con `rol_fuente = derivada_de_procedencia` y las `remite_a`. Da 18.483, igual a las aristas de extracción de la (10) del grafo evaluado (18.483, `t3/conteos_sin_leer/contado_sin_leer_t3f.json`): True. Las `establecida_en` sin `rol_fuente` quedan. La muestra de T3, con A4.1 tal cual, queda en `t3/muestras/` sin cambios y no se lee.
3. **La vigilancia (2)** (punto 1.3). Su población es la de T3, la extracción final (198 aceptadas sin relaciones), y su muestra es la de T3. La del primer intento no se sortea ni se reporta: `no_abrir_t4t1.py` escribe su cuenta por TO solo en `t4/NO_ABRIR_conteos_t4.json`, sin imprimir ninguna cifra, y de él doy solo el sha256 (tabla 6).
4. **Las definiciones de (1) y (3)** (punto 1.4): las del FRENO T3, sección 6, con los dos agregados. En (1), `no decidible` queda fuera de la tasa y se declara con su cuenta (hoy, 1 propuesta de 30). En (3), el grupo por tramo igual no ve duplicaciones con tramos distintos. Lo declaro en la sección 9.

## 3. Las poblaciones (punto 3)

Script: `poblaciones_t4t1.py`, sobre una copia del repo. La tabla, tal cual:

#### Tabla 1. La población por celda (`muestras/poblaciones_t4_tramo1.json`, 2026-10-18T12:00:56-03:00)

| muestra | elemento | N | RI:sin_raiz | RI:resto | NG:sin_raiz | NG:resto | sha256 de los ids por celda |
|---|---|---:|---:|---:|---:|---:|---|
| vigilancia:1 | nodo Condicion | 1.401 | 94 | 102 | 42 | 1.163 | `64a9b482efd887cc51d29944492e2bb7f951f6baeabf361ef7592299ba6ec963` |
| vigilancia:3 | grupo de nodos | 181 | 5 | 42 | 1 | 133 | `e7180cc286d6a16ffe9c64df54c0156ce8667c860d05e2edb321a699b0a5c16f` |
| observacion:12 | arista | 18.483 | 960 | 1.743 | 770 | 15.010 | `b5ce3010d6645cee6a2850a63b158bee35c044dade8753cbcf2084c1bab38ab0` |
| observacion:12, A4.1 tal cual (información) | arista | 28.062 | 1.021 | 5.030 | 830 | 21.181 | `908e4c42b8bc95e537e858a0349fe92013cfdb0b3a9d0a1422a664eebc70aefd` |

- **Lo que la decisión 1.2 resta de A4.1:** remite_a / rol_fuente None, 8.838; establecida_en / rol_fuente derivada_de_procedencia, 741.
- **La (12) nueva, por relación:** establecida_en 11.159, aplica_a 4.233, condicion_de 1.295, regula 572, limita 351, padre_sugerido 280, requiere 184, ejecuta 141, condiciona 105, prohibe 63, exceptua 52, exceptua_obligacion 48.
- **Los controles de `poblaciones_t4t1.py`:** A41_igual_a_T3: True; vigilancia_1_igual_a_T3_tabla_T8: True; vigilancia_3_igual_a_T3_tabla_T8: True; observacion_12_igual_a_la_extraccion_de_la_10: True.

- La celda de un nodo es la de su unidad de procedencia primaria; la de un grupo de (3), la de su nodo de id menor; la de una arista, la de su nodo de origen (§5.4 bis, punto 2, v8c).
- El id de un grupo de (3) son sus ids de nodo ordenados y unidos con «|»; el de una arista, la tripla (source, relation, target).

## 4. Los sorteos

Script: `sorteos_t4t1.py`, con `celdas_t4_t3f.asignar` de T3 sin cambios. Cada cadena se controla contra las del texto firmado (`95b18217:1019-1062`). La tabla, tal cual:

#### Tabla 2. Los sorteos (`muestras/sorteos_t4_tramo1.json`; base `33a3c34b…`; poblaciones `df560e10…`)

| muestra | RI:sin_raiz | RI:resto | NG:sin_raiz | NG:resto | total | cómo, por celda | notas | archivo | sha256 | hora |
|---|---:|---:|---:|---:|---:|---|---|---|---|---|
| vigilancia:1 | 10 | 5 | 5 | 10 | 30 | RI:sin_raiz sorteo, RI:resto sorteo, NG:sin_raiz sorteo, NG:resto sorteo | — | `muestras/vigilancia_1.json` | `484cf14e8bf66bc1013a85b7d35782e44448e3b69cb39514b494c2adc9032360` | 2026-10-18T12:01:47-03:00 |
| vigilancia:3 | 5 | 10 | 1 | 14 | 30 | RI:sin_raiz entran todos, RI:resto sorteo, NG:sin_raiz entran todos, NG:resto sorteo | la celda RI:sin_raiz tiene 5 de su cuota de 10: entran todos; RI:resto sortea 5 más; la celda NG:sin_raiz tiene 1 de su cuota de 5: entran todos; NG:resto sortea 4 más | `muestras/vigilancia_3.json` | `0058421f2d2e24b37b8b00af6f380a2e2caf5fbc52a12058c66888a1c9ab9722` | 2026-10-18T12:01:47-03:00 |
| observacion:12 | 10 | 5 | 5 | 10 | 30 | RI:sin_raiz sorteo, RI:resto sorteo, NG:sin_raiz sorteo, NG:resto sorteo | — | `muestras/observacion_12.json` | `bdce1bdaca85d8ff2c1cb9652fb2f5a13990a3884c1edd670f635925750914c4` | 2026-10-18T12:01:47-03:00 |

La segunda corrida (`muestras/segunda_corrida_de_los_sorteos/`): las tres muestras byte a byte iguales, True; el índice igual salvo las horas, True. `celdas_t4_t3f.py`: `f0082e3cd588e855…`, el de T3.

- Las cadenas: `tanda1:vigilancia:1:<celda>:<base>`, `tanda1:vigilancia:3:<celda>:<base>` y `tanda1:observacion:12:<celda>:<base>`. Las cadenas de la ampliación no se usan. Las otras cinco muestras no se tocaron.

## 5. El material

Script: `material_t4t1.py`, sobre la copia, con la E0 con las partes rearmada en la copia (`reext_t0/t3/e0_con_partes.py`). La tabla, tal cual:

#### Tabla 3. El material (`muestras/material/material_t4_tramo1.json`, 2026-10-18T12:03:34-03:00)

| muestra | fichas | fichas (.jsonl) | fichas (.md) |
|---|---:|---|---|
| vigilancia:1 | 30 | `237a2c5b5c586958cf65f49e713e07b897b5df446e3fe5745ce41470d4219599` | `8cabad77cf7095df37e7c41a880868ec0978fac8ad47c7ef2ba016eac3a7d84c` |
| vigilancia:3 | 30 | `b29a93d87506f095bb2f7e2e78433a6d3126a23d89879f88ffaaf3520a5074b8` | `4cf1a30222a79b0e6ba00c260418c54d652a1136ed932fed27144cf322322544` |
| observacion:12 | 30 | `8528dce6ab8c5e27ed5560336b38d983cdfc77ceb51831cc939c0588fc8bff64` | `bcc0b4ff78ade7e9ec17bd3724e59ea5818e379bb18b24bb3a6fd616de0d22d4` |

El control, que relee lo escrito: 90 fichas, 0 claves vedadas, '"estado' en los .md 0 veces, texto de {'e0': 89, 'e0_con_las_partes': 1}, 0 sin texto. La E0 con las partes es la de T3 (conjunto `f079c1ff1b680eb7…`).

- **(1):** el nodo Condicion con sus propiedades y su procedencia, el texto de su unidad y sus aristas, con la relación y el id, el tipo y el label del otro nodo.
- **(3):** los nodos del grupo con sus propiedades y su procedencia, y el texto de su unidad.
- **La (12):** como en T3, la arista, sus dos nodos y el texto de su unidad de procedencia.
- El texto de cada unidad es el que vio E3 (`comun_e3.fuente_integro`). Sin el estado de E3 ni sus marcas. La hora del material es posterior a la de los sorteos.
- No armé planillas en el material: las que valen son las de `lectura_autora/` (sección 8). Las planillas en blanco del material de T3 (`t3/muestras/material/*/planilla_*.csv`) quedan como están y no se usan.

## 6. Lo que queda a la vista (punto 5)

Script: `unidades_a_la_vista_t4t1.py`. Reescribí `t3/muestras/unidades_a_la_vista_T4.json`, el único archivo de `t3/` que cambia. Antes copié la versión de T3, tomada del T3a (`git show eb0711a1`), a `t4/muestras/unidades_a_la_vista_T4_regla_de_T3.json`. Por muestra, el archivo da el `chunk_id` de cada unidad, la versión que muestra y por qué suma: la ficha o el tipo del nodo. La tabla, tal cual:

#### Tabla 4. Lo que queda a la vista (`t3/muestras/unidades_a_la_vista_T4.json`, 2026-10-18T12:04:54-03:00)

| muestra | material | fichas | unidades a la vista (regla 1.1) | por versión | nodos mostrados que no suman | con la regla de T3 (información) |
|---|---|---:|---:|---|---|---:|
| cola | `tanda1/t3/muestras/material` | 30 | 30 | {'primera': 30} | — | 30 |
| aceptadas:items | `tanda1/t3/muestras/material` | 30 | 34 | {'final': 34} | TextoOrdenado 30, Sujeto (más de una unidad) 19 | 2.189 |
| aceptadas:no_items | `tanda1/t3/muestras/material` | 30 | 35 | {'final': 35} | TextoOrdenado 30, Sujeto (más de una unidad) 27 | 2.579 |
| vigilancia:2 | `tanda1/t3/muestras/material` | 30 | 30 | {'final': 30} | TextoOrdenado 30 | 2.161 |
| vigilancia:7 | `tanda1/t3/muestras/material` | 4 | 4 | {'final': 4} | Sujeto (más de una unidad) 4 | 156 |
| vigilancia:1 | `tanda1/t4/muestras/material` | 30 | 40 | {'final': 40} | TextoOrdenado 30 | 2.130 |
| vigilancia:3 | `tanda1/t4/muestras/material` | 30 | 25 | {'final': 25} | — | 25 |
| observacion:12 | `tanda1/t4/muestras/material` | 30 | 30 | {'final': 30} | TextoOrdenado 19, Sujeto (más de una unidad) 3 | 1.975 |
| todas | — | — | 216 | {'primera': 30, 'final': 186} | — | 2.983 |

Por qué suman, por muestra (una unidad puede sumar por más de una razón): cola: ficha de cola 30; aceptadas:items: ficha de unidad 30, Obligacion 18, Operacion 12, Condicion 9, Definicion 4, Comunicacion 4, Restriccion 3, Excepcion 1; aceptadas:no_items: ficha de unidad 30, Obligacion 20, Operacion 15, Condicion 9, Restriccion 6, Potestad 6, Definicion 5, Sujeto 4, Excepcion 2, Comunicacion 1; vigilancia:2: ficha de unidad 30; vigilancia:7: Operacion 4; vigilancia:1: Condicion 31, Obligacion 22, Operacion 12, Restriccion 8, Potestad 7, Excepcion 2, Definicion 1; vigilancia:3: Operacion 20, Obligacion 17, Definicion 3, Potestad 2, Condicion 2, Restriccion 1; observacion:12: Obligacion 16, Operacion 9, Condicion 6, Restriccion 4, Sujeto 1, Potestad 1, Definicion 1.
Aristas de las fichas de (1) y de la (12) con su unidad de procedencia fuera de la lista (información): cola 0, aceptadas:items 0, aceptadas:no_items 0, vigilancia:2 0, vigilancia:7 0, vigilancia:1 0, vigilancia:3 0, observacion:12 0.

- Las muestras de T3, con la regla de T3, dan las mismas cifras que su versión del T3a (tabla T7 del FRENO T3): True. El cálculo de información reproduce el de entonces.
- No calculé si quedan 30 en la población de U-MED-VERIF: lo controla la mesa.

## 7. La lectura asistida (punto 6)

La leí yo: Claude Opus 5.5 (`claude-opus-5-5`), sobre las fichas del material, sin API. Las propuestas de entrada están en `t4/lectura_asistida/propuestas/`; `planillas_t4t1.py` las controla contra el material (los mismos ids, en el mismo orden, una respuesta válida y una cita del texto por elemento) y arma el JSON y las planillas. La tabla, tal cual:

#### Tabla 5. La lectura asistida: cuántas propuestas hay de cada respuesta (`lectura_asistida/lectura_asistida_t4_tramo1.json`, 2026-10-18T12:28:35-03:00)

| muestra | elementos | propuestas | con omisiones (aparte) | con observaciones (aparte) |
|---|---:|---|---:|---:|
| cola | 30 | con error 10, sin error 17, dudosa 3 | 8 | 6 |
| aceptadas_items | 30 | con error 5, sin error 21, dudosa 4 | 6 | 5 |
| aceptadas_no_items | 30 | con error 2, sin error 28 | 6 | 11 |
| vigilancia_2 | 30 | vaciamiento 15, no vaciamiento 14, no decidible 1 | 0 | 0 |
| vigilancia_7 | 4 | con apoyo 2, sin apoyo 2 | 0 | 0 |
| vigilancia_1 | 30 | sí 3, no 26, no decidible 1 | 0 | 0 |
| vigilancia_3 | 30 | duplicación 9, distintos 21 | 0 | 0 |
| observacion_12 | 30 | correcta 27, no decidible 1, incorrecta (E1-prompt) 2 | 0 | 2 |

Modelo: Claude Opus 5.5 (`claude-opus-5-5`); lectura propia de la ejecutora en su sesión de Claude Code, sobre las fichas del material; sin API y USD 0. Es una propuesta: adjudica la autora (D2, lectura asistida con revisión de la autora, como en la tanda 0).

**Los criterios que apliqué** (`criterios_de_la_propuesta` del JSON):
- **Cola y aceptadas:** un tipo cercano con la descripción fiel es lectura laxa, sin error, como en la lectura de las aceptadas de la tanda 0. Es error una facultad o un fin leído como deber, un supuesto o una regla invertidos, un sujeto que no es el del texto, una relación que el texto no sostiene o un contenido que no está. Es dudosa si el contenido viene de otro punto del documento y no está en el texto de la unidad, o si el texto admite las dos lecturas. Los tipos documentales y las `remite_a` no entran en el veredicto.
- **(2):** vaciamiento si el ítem fija un dato, una medida, un concepto o un sujeto del régimen, o el texto fija una regla o una tabla del modelo de información, y la unidad no tiene relaciones. No lo es si el texto propio solo abre una lista, es un título o es un formulario.
- **(1):** sí, solo si el texto formula el deber y la Condicion lo lleva; el «debe» que pone la descripción del extractor no cuenta.
- **(3):** duplicación si el mismo contenido normativo está en dos nodos del grupo. Son distintos si cada nodo dice algo que el otro no, incluido el par deber y acto regulado (`Obligacion —regula→ Operacion`, `e1_extractor/prompt_e1.py:67` y `:184-189`), cuando la descripción del acto no repite el deber.
- **La (12):** una `establecida_en` es correcta si el nodo de origen está en el texto de su unidad y es de ese TO; en las demás, decide la relación contra el texto.
- Las omisiones y las observaciones van aparte, en `t4/lectura_asistida/omisiones_y_observaciones_t4_tramo1.md`.

## 8. Las planillas, el LEEME y el convertidor (punto 7)

#### Tabla 6. Los archivos de la lectura de la autora y de la lectura asistida

| archivo | sha256 |
|---|---|
| `t4/lectura_autora/cola.csv` | `5f1fefe1887fd999a989a7414790018b6dc3390f3f4c256423cb84cd358f799a` |
| `t4/lectura_autora/aceptadas_items.csv` | `4932f4a80c8ae43d9667d280647e13bbc9f8f174f1d16da356961864d92fe439` |
| `t4/lectura_autora/aceptadas_no_items.csv` | `cc830b718cb13ccb595f95d1b0d0cc229f79802c1600c6f2665255d6ffec1e8a` |
| `t4/lectura_autora/vigilancia_2.csv` | `580e4b047d839b5f6a4528544645fe66b87037b5daee2505fbb2e8d311b55045` |
| `t4/lectura_autora/vigilancia_7.csv` | `b047d9ed7992ebc315eea8e55fe16a85233e8fa38d47cda5a85419649e17d7a1` |
| `t4/lectura_autora/vigilancia_1.csv` | `609577900a2522faf14fe0ba1fc6808ab89e58a352bb49028b2170bbcd52a52b` |
| `t4/lectura_autora/vigilancia_3.csv` | `099ab7e227a93d5ca0075f4e9286ef82139018c9bc74f86edd6e29462e50a3ae` |
| `t4/lectura_autora/observacion_12.csv` | `f4ba30e1831c1221d9f7b40214f01c437590182792ec85e096983853aeaf04a5` |
| `t4/lectura_autora/LEEME_lectura_T4.md` | `04c9c41a7453fa0ab0f527cefa11c4f20262bd4aca52c9645e83face754ab947` |
| `t4/lectura_autora/convertir_lectura_T4.py` | `e3e1150a92c5b712e258b4348cddfb1d329aafb09c81510526a4133d5d971a24` |
| `t4/lectura_asistida/lectura_asistida_t4_tramo1.json` | `f273f0944954c9d47d58627329370355a8d7e4c6d4ef23ab127e9fbdf19cff91` |
| `t4/lectura_asistida/omisiones_y_observaciones_t4_tramo1.md` | `d6e84c6cd3ec5a23d17dff9c83abcaa96c82c54da4b8ed47ce34ee13334b98a6` |
| `t4/NO_ABRIR_conteos_t4.json` (no se abre) | `1646dfea31ce1e701dd6c88da9164046a1b590f1508bb1126f9b221675c78dba` |

- **Las planillas** (`t4/lectura_autora/<muestra>.csv`): UTF-8, «;» y «\n», con `id`, `celda`, `ficha` (la ruta del `.md` y, tras «#», el número de la ficha), `propuesta`, `justificacion`, y `veredicto_autora` y `nota_autora` vacías.
- **El `LEEME_lectura_T4.md`:** el orden de lectura (cola, aceptadas ítems, aceptadas no ítems, (2), (7), (1), (3) y la (12)), las respuestas válidas de cada muestra, que el veredicto puede repetir la propuesta o cambiarla con la razón en la nota, que la (12) que vale es la de `t4/` y nunca la de `t3/`, cómo se convierte y cómo se sella.
- **El convertidor** (`convertir_lectura_T4.py`, generado por `planillas_t4t1.py` desde `convertir_lectura_T4_plantilla.py` con el sha256 de cada planilla adentro): toma `id`, `celda`, `ficha`, `propuesta` y `justificacion` de la planilla y de la exportación solo las dos columnas de la autora. Controla los códigos, que los ids y su orden sean los de la muestra y que un cambio de la propuesta traiga su razón; frena si algo no cierra, no cambia ninguna marca y no pisa una marcada.
- **La prueba**, sobre una copia de `lectura_autora/` con exportaciones simuladas (`lectura_asistida/consolas/prueba_convertidor_t4t1.txt`): 3 conversiones pasan (separadores «,», «;» y tabulador, con y sin BOM, una con un cambio con su nota) y 4 frenan como deben (un cambio sin razón, un código mal escrito, dos filas reordenadas y una marcada que ya existe).
- **El sello lo hace la autora:** el sha256 y la hora de cada marcada, en `t4/lectura_autora/sello_lectura_T4.txt` (el `LEEME` trae el comando). Queda PENDIENTE.

## 9. Lo declarado por los puntos 1.2 a 1.4

1. **La (12) se rehízo con el universo de la decisión 1.2** (18.483 aristas); la muestra de T3, con A4.1 tal cual (28.062), queda en `t3/muestras/observacion_12.json` sin cambios y no se lee. Lo que la decisión resta de A4.1: remite_a / rol_fuente None, 8.838; establecida_en / rol_fuente derivada_de_procedencia, 741.
2. **La vigilancia (2)** se lee sobre la población de la extracción final (198 unidades). La del primer intento no se sortea ni se reporta: su cuenta por TO está solo en `t4/NO_ABRIR_conteos_t4.json`.
3. **En la vigilancia (1), `no decidible` queda fuera de la tasa** y se declara con su cuenta: hoy 1 propuesta; la cuenta que vale es la de la lectura de la autora.
4. **En la vigilancia (3), el grupo por tramo igual no ve duplicaciones con tramos distintos.** Una duplicación entre nodos cuyos tramos difieren no entra en la población.

## 10. Para la autora y la mesa

1. **Dudosas por contenido de otro punto:** `ri_mmsef::2.2.10.2`, `ri_mmsef::2.2.13.1`, `ri_dcpc::3.2.2.1`. Sus nodos traen texto que no está en el texto de la unidad que vio E3: en ri_mmsef, «Se informará el cumplimiento…» y los parámetros «Si / No / Eximida / No Aplicable». Que E1 lo haya visto en su mensaje: NO VERIFICADO. Si se confirma, es un rasgo del contexto de E1 frente al de E3, no un error de una unidad.
2. **Una observación de `remite_a`** (`ceninf::4.1.3`): las aristas hacia `ceninf::2.1` se apoyan en la cita «punto 2.1 del apartado A del T.O.», que es de otro texto ordenado. Va como observación porque las `remite_a` se cuentan aparte.
3. **En la (3), 15 de los grupos son el par deber y acto regulado** (`Obligacion —regula→ Operacion`) con la descripción del acto sin el deber: los propuse distintos, por el diseño del esquema. Si la autora lee ese par como duplicación, la cifra cambia mucho.
4. **La (12) tiene un no decidible por un texto incompleto** (`Obligacion_las_autoridades_de_la_entidad_deben_tomar_conocimiento_del_contenido_de_los_info_13980b | establecida_en | TextoOrdenado_ri_ccna_pdf`): la oración «Para que las autoridades de la entidad tomen conocimiento…» termina en la lista, sin el verbo principal.
5. **En la (2), 10 de los vaciamientos son ítems de ri_mmsef**, datos o medidas del régimen informativo sin relaciones.
6. **Lo que queda a la vista** (sección 6): la mesa controla si quedan 30 en la población de U-MED-VERIF, sin abrir nada.

## 11. La foto del repo, los .pyc y el grep de convenciones

Lo genera `scripts/freno_t4t1_foto.py` desde la foto del paso 0 y la de después (las dos van en el paquete).

- **La foto** (`t2/foto_repo_tanda1_t2.py`). Paso 0: 11:46:06 a 11:46:18 del 2026-10-18, 52.450 entradas. Después: 12:42:32 a 12:42:43 del 2026-10-18, 52.509 entradas, 16 sin abrir y 342 enlaces.
  - **59 nuevos:** 2 en `tanda1/t4/, lo demás`; 12 en `tanda1/t4/lectura_asistida/`; 10 en `tanda1/t4/lectura_autora/`; 24 en `tanda1/t4/muestras/`; 11 en `tanda1/t4/scripts/`.
  - **0 borrados:** ninguno.
  - **1 cambiados:** 1, el archivo del punto 5.
  - **Fuera de lo admitido:** 0.
  - `unidades_a_la_vista_T4.json`: `1e775850e94457c4…` (HEAD, el del T3a) → `5ec9753dc9f8caa5…`.
- **Los `.pyc`:** 11.236 líneas en el paso 0 y 11.236 después; listas iguales: True.

**El sha256 de los archivos clave, de la foto de después** (el del `NO_ABRIR_`, de la escritura):

| archivo | sha256 |
|---|---|
| `data/experiment/tanda1/t3/muestras/unidades_a_la_vista_T4.json` | `5ec9753dc9f8caa51a37a884c542efe38416a41d575a030b24ababbf9c60b17d` |
| `data/experiment/tanda1/t4/muestras/unidades_a_la_vista_T4_regla_de_T3.json` | `1e775850e94457c4d5e356c27bd247dbb8ba76731f302580ab7b2762306bfc12` |
| `data/experiment/tanda1/t4/muestras/poblaciones_t4_tramo1.json` | `df560e10b49d4694c8048262bbb9bbc2d474132caae352754defcc602a3af3e1` |
| `data/experiment/tanda1/t4/muestras/sorteos_t4_tramo1.json` | `984c56efcfee251b75ec179e537db88f8f5964b0dfbd101de81e423615d436c4` |
| `data/experiment/tanda1/t4/muestras/material/material_t4_tramo1.json` | `cb0673db338486ecf4a1be7e22708ffb4217af9cc3490960bcf73861430f03d6` |
| `data/experiment/tanda1/t4/lectura_asistida/lectura_asistida_t4_tramo1.json` | `f273f0944954c9d47d58627329370355a8d7e4c6d4ef23ab127e9fbdf19cff91` |
| `data/experiment/tanda1/t4/tablas_t4_tramo1.md` | `a6fa39565f03932ed380abb0d2a2059de8c7909a21b9956d73d18c20b73a9e8d` |
| `data/experiment/tanda1/t4/NO_ABRIR_conteos_t4.json` | `1646dfea31ce1e701dd6c88da9164046a1b590f1508bb1126f9b221675c78dba` |

**Los scripts de este tramo** (`t4/scripts/`, sha256 de la foto de después):

| script | sha256 |
|---|---|
| `convertir_lectura_T4_plantilla.py` | `e1c1e36080192b2f7e9eb5ee5b2fd1770e36d20ae38cbc7f56424888b385e74a` |
| `escribir_en_el_repo_t4t1.py` | `d691504e3ef786ea81f63d65c7d55d10d4e66c47e6c319718fbf867711086e1b` |
| `freno_t4t1_armar.py` | `01ba412556de741f2ac11ebc9df591aa236794d06e31df5c04df882ac16f5a9d` |
| `freno_t4t1_foto.py` | `8490354931b3cf452cc799380467dfab06d9ad916363f13af75d6b5050330d3e` |
| `material_t4t1.py` | `5b719bdb0ba9d2b7261f8ccdccc2dd11b79107d0813df5139bf8b5fbe5c3340c` |
| `no_abrir_t4t1.py` | `84742ac01ffcad2f7ba2f1541e117bb6e3a5bae5c9a4c287a8ccdb35c428fb27` |
| `planillas_t4t1.py` | `6844605867b23cb6a07feaf5364f96d0b7ddcdb530ce0df33de3dba9521c1feb` |
| `poblaciones_t4t1.py` | `9fb96294bf7f54bac3c60c9b9d0cc7fabd35589e52e211eaa843d7a043e5f337` |
| `sorteos_t4t1.py` | `b23174ee874089048c4bb7485f33879ec8a3c677b6977f30e85cc2894f9bb23a` |
| `tablas_t4t1.py` | `06f0f3337ac2ba14890f7df9e6b0bbc316a219ab90006da069e0d0c56803a60d` |
| `unidades_a_la_vista_t4t1.py` | `ed5fca28bc7501aab2c54d3c910547e1b9e5221cb0a831e50b8063c2f43d679e` |

- **El grep de convenciones** (`grep_convenciones_t4t1.py` y su salida, en el paquete) busca las palabras del `user.name` de git y las de origen conversacional (Slack, mail, correo, «como dijo», «pedido por», …) en los 60 archivos nuevos o cambiados de la foto, sin el `NO_ABRIR_`. El control positivo da la línea 2. Con el patrón, en los archivos que redacté: `freno_t4t1_armar.py`, 2 línea(s): son las líneas de este script que describen el patrón del grep. Las palabras del nombre, en ningún archivo: True. En las salidas de los generadores, las coincidencias son texto de la norma (como «correo electrónico» en ids de nodo): `poblaciones_t4_tramo1.json`. Rutas con la carpeta personal o el scratchpad: 1 archivo(s) (`escribir_en_el_repo_t4t1.py`: son los controles que buscan esas cadenas). El grep del FRENO va en el mensaje de cierre.
- **Las copias** del repo son con el `rsync` de la cláusula, más la exclusión del volumen de Neo4j, y su control dio 0 (`rsync_copia_t4t1.log` en el paquete). Ningún `git clone`. No abrí ninguna carpeta vedada.

## 12. Errores propios, con su causa

1. **Dos constantes de sha256 escritas de memoria.** En `poblaciones_t4t1.py` y `sorteos_t4t1.py` puse primero un sha256 inventado para `t3/muestras/poblaciones_t4.json` y un prefijo inventado para `celdas_t4_t3f.py`.
   - La causa: escribí la constante antes de calcularla.
   - Lo vi antes de correr: las reemplacé por el sha256 que da `shasum -a 256` sobre el archivo y sobre `git show HEAD:`, y los controles las comparan enteras.
2. **12 justificaciones sin cita** (`justificaciones_completadas_t4t1.json`, en el paquete). En las unidades sin contenido y en otras escribí la justificación sin citar el texto.
   - La causa: di por obvia la cita cuando la unidad no tiene nodos.
   - El control de `planillas_t4t1.py` frenó antes de escribir nada, y las completé con la cita del texto.
3. **La primera prueba del convertidor no probó nada.** El bucle de zsh pasó la muestra y la exportación como un solo argumento, y todas las corridas dieron el error de uso.
   - La causa: zsh no parte las variables en palabras.
   - La repetí con los dos argumentos separados; la consola que va al repo es la de esa segunda corrida.

FRENO T4, primer tramo. Espero la revisión de la mesa y la lectura de la autora.
