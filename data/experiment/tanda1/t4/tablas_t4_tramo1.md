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

#### Tabla 2. Los sorteos (`muestras/sorteos_t4_tramo1.json`; base `33a3c34b…`; poblaciones `df560e10…`)

| muestra | RI:sin_raiz | RI:resto | NG:sin_raiz | NG:resto | total | cómo, por celda | notas | archivo | sha256 | hora |
|---|---:|---:|---:|---:|---:|---|---|---|---|---|
| vigilancia:1 | 10 | 5 | 5 | 10 | 30 | RI:sin_raiz sorteo, RI:resto sorteo, NG:sin_raiz sorteo, NG:resto sorteo | — | `muestras/vigilancia_1.json` | `484cf14e8bf66bc1013a85b7d35782e44448e3b69cb39514b494c2adc9032360` | 2026-10-18T12:01:47-03:00 |
| vigilancia:3 | 5 | 10 | 1 | 14 | 30 | RI:sin_raiz entran todos, RI:resto sorteo, NG:sin_raiz entran todos, NG:resto sorteo | la celda RI:sin_raiz tiene 5 de su cuota de 10: entran todos; RI:resto sortea 5 más; la celda NG:sin_raiz tiene 1 de su cuota de 5: entran todos; NG:resto sortea 4 más | `muestras/vigilancia_3.json` | `0058421f2d2e24b37b8b00af6f380a2e2caf5fbc52a12058c66888a1c9ab9722` | 2026-10-18T12:01:47-03:00 |
| observacion:12 | 10 | 5 | 5 | 10 | 30 | RI:sin_raiz sorteo, RI:resto sorteo, NG:sin_raiz sorteo, NG:resto sorteo | — | `muestras/observacion_12.json` | `bdce1bdaca85d8ff2c1cb9652fb2f5a13990a3884c1edd670f635925750914c4` | 2026-10-18T12:01:47-03:00 |

La segunda corrida (`muestras/segunda_corrida_de_los_sorteos/`): las tres muestras byte a byte iguales, True; el índice igual salvo las horas, True. `celdas_t4_t3f.py`: `f0082e3cd588e855…`, el de T3.

#### Tabla 3. El material (`muestras/material/material_t4_tramo1.json`, 2026-10-18T12:03:34-03:00)

| muestra | fichas | fichas (.jsonl) | fichas (.md) |
|---|---:|---|---|
| vigilancia:1 | 30 | `237a2c5b5c586958cf65f49e713e07b897b5df446e3fe5745ce41470d4219599` | `8cabad77cf7095df37e7c41a880868ec0978fac8ad47c7ef2ba016eac3a7d84c` |
| vigilancia:3 | 30 | `b29a93d87506f095bb2f7e2e78433a6d3126a23d89879f88ffaaf3520a5074b8` | `4cf1a30222a79b0e6ba00c260418c54d652a1136ed932fed27144cf322322544` |
| observacion:12 | 30 | `8528dce6ab8c5e27ed5560336b38d983cdfc77ceb51831cc939c0588fc8bff64` | `bcc0b4ff78ade7e9ec17bd3724e59ea5818e379bb18b24bb3a6fd616de0d22d4` |

El control, que relee lo escrito: 90 fichas, 0 claves vedadas, '"estado' en los .md 0 veces, texto de {'e0': 89, 'e0_con_las_partes': 1}, 0 sin texto. La E0 con las partes es la de T3 (conjunto `f079c1ff1b680eb7…`).

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
