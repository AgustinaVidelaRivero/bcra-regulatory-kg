# U-INSUMOS-CAP · I1 — Estadísticas descriptivas del corpus

Insumo citable para los capítulos 3 y 4 (mesa de escritura). No es prosa de la tesis.
Todas las cifras salen de artefactos del repo; ninguna llamada a la API.

Regenerar (desde la raíz del repo; doble corrida byte a byte idéntica):

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B reports/u_insumos_cap/u_insumos_i1.py
```

Cada cifra de este documento está en `reports/u_insumos_cap/estadisticas_corpus.json`; la línea «Claves» debajo de cada tabla da la ruta dentro de `conjuntos.<conjunto>` (o la raíz indicada). Consulta de una clave:

```bash
python3 -c "import json; d=json.load(open('reports/u_insumos_cap/estadisticas_corpus.json')); print(json.dumps(d['conjuntos']['corpus_152']['R2_paginas_por_rol'], ensure_ascii=False))"
```

Conjuntos: **corpus_152** = los 152 TOs de la partición del segmentador (`particion_152.json`, clave `por_to`; no incluye a los cinco de desarrollo, `inventario_resumen.json` → `subset_excluido`); **desarrollo_5** = `cap`, `cla`, `ext`, `pro`, `ric` (`manifiestos/desarrollo_5tos.json`); **tanda0_5** = el conjunto de la tanda 0 en la convención de `docs/preregistro_tanda0.md` (A2.2): `ctacte`, `lingob`, `polcre`, `pagjub`, `docvig`, que también están dentro de corpus_152.

## 0. Cifras publicadas de la partición, reproducidas

Fila publicada: `data/experiment/segmentacion_84/b584_particion/reporte_b584.md:20`. Resultado: **coinciden las cuatro por todas las vías**.

| vía | TOs | páginas | unidades | tablas lógicas |
|---|--:|--:|--:|--:|
| publicada (`reporte_b584.md:20`) | 152 | 6.757 | 9.324 | 559 |
| `particion_152.json` → `agregados` (suma de clases) | 152 | 6.757 | 9.324 | 559 |
| `particion_152.json` → suma de `por_to` | 152 | 6.757 | 9.324 | 559 |
| `conteos_b584.json` (`paginas`, `unidades_extraccion`, `tabular.parseadas`) | 152 | 6.757 | 9.324 | 559 |
| chunks_<to>.json (cantidad) y suma de `roles_pagina` | 152 | 6.757 | 9.324 | — |

Clave: `cifras_publicadas`. Recómputo independiente de una línea:

```bash
python3 -c "import json; p=json.load(open('data/experiment/segmentacion_84/b584_particion/particion_152.json')); a=p['agregados']; print({k: sum(v[k] for v in a.values()) for k in ('tos','paginas','unidades','tablas_logicas')})"
```

Matiz de nomenclatura: en `particion_152.json` la clave `tablas_logicas` cuenta tablas **parseadas** (559); en `conteos_b584.json`, `tabular.tablas_logicas` cuenta las **detectadas** (563 = 559 parseadas + 4 declaradas sin parsear, en `ri_niif` y `snp_tr`).

## 1. Reglas declaradas (antes de aplicarlas)

Las reglas se fijaron en el checkpoint de la unidad antes de escribir el script; el script las implementa con el mismo número.

- **R0.** Conjuntos y fuentes. corpus_152 y tanda0_5: `data/experiment/segmentacion_84/b584_particion/<to>/{chunks,estructura}_<to>.json`, `conteos_b584.json`, `particion_152.json`. desarrollo_5: `data/experiment/reextraccion_v2/e0_chunking/salida_tanda0/{chunks,estructura}_<to>.json` y `conteos.json` (byte-idénticos a `salida_enm01`, la E0 que lee el ensamblado de KG-Reextraído-r1: `corpus_v2/r1_comun.py:29` y `corpus_v2/ensamblar_r1.py:56`; control en §6).
- **R1.** Clase = `particion_152.json` → `por_to.<to>.clase`. Categoría = `escalado_prep/inventario_tos.csv`, campo `categoria`. Desarrollo: regla de `escalado_prep/code/construir_inventario.py:34-45` (la lista del índice oficial `indice_oficial_raw.json` donde figura el archivo: `textos_ordenados` → normativa_general; `regimenes_informativos` → regimen_informativo); la clase de la partición no aplica (los cinco no están en `particion_152.json`).
- **R2.** Páginas por rol = suma de `roles_pagina` por conjunto; denominador = páginas del conjunto.
- **R3.** Unidad = cada elemento de `chunks_<to>.json` (las partes de sub-chunking cuentan como unidades, igual que `unidades_extraccion`); tipo = campo `tipo` (`punto_terminal`, `mini_chunk`, `seccion_sin_puntos`).
- **R4.** Profundidad de una unidad, desde su campo `unidad`: si empieza con `S` (sección) vale 1; si no, la cantidad de componentes separados por punto (`1.2` → 2, `1.2.3` → 3). Los mini-chunks (`::intro`, `::cierre`, `::intersticial`, `::chapeau_seccion`) llevan en `unidad` el número del padre, así que toman la profundidad del padre.
- **R5.** Tablas lógicas = `particion_152.json` → `por_to.<to>.tablas_logicas` (parseadas por B5.8.3) y, aparte, `conteos_b584.json` → `<to>.tabular` (detectadas y declaradas). Chunks marcados = `flags.contenido_tabular` y `flags.formula` de E0. Desarrollo: no hay archivos `tablas_*` en `salida_enm01/` ni en `salida_tanda0/` (control en §6); solo `cap` tiene el testigo de B5.8.3 (`b583_tablas/testigo_capmin/tablas_capmin.json`).
- **R6.** Largo de unidad = `chars_propio` (igual a `len(texto)`, verificado) y, aparte, `chars_completo` (con encabezados heredados). Mediana = `statistics.median`; p10, p25, p75, p90 y p99 por rango más cercano (posición ⌈p/100·n⌉ de la lista ordenada, desde 1); máximo.
- **R7.** Normalización del texto para R8 y R9: se quita cada guion de fin de línea (`-\n`) y todo blanco consecutivo pasa a un espacio.
- **R8.** Remisiones: `RE_NORMA`, `RE_DICHO`, `RE_PUNTOS` y `RE_SECCION` copiadas de `data/experiment/reextraccion_v2/corpus_v2/r1_referencias.py:63-69`, ventanas de 120 y 90 caracteres (`:49-50`) y separación de `detectar_menciones` (`:139-197`), aplicadas al texto de E0 de cada unidad (no a la paráfrasis del grafo). Cada mención de norma (`RE_NORMA`) cuenta como una remisión **externa** y consume los puntos y secciones de sus 120 caracteres previos; cada «de dicho/ese/este ordenamiento» (`RE_DICHO`) cuenta como una externa anafórica; cada mención de punto o sección no consumida y sin norma en sus 90 caracteres siguientes cuenta como una remisión **interna** (al mismo TO). No se cuenta la mención de sección en el offset 0 del texto (el encabezado propio de la unidad). Unidad de conteo: la mención (una lista «puntos 1.1. y 1.2.» es una). Límites: la norma nombrada no se resuelve contra el inventario, así que «externa» es «hacia una norma nombrada», que puede ser el mismo TO; `RE_NORMA` no reconoce «normas de» (plan, fila B2.10, punto 3): la sensibilidad `internas_con_normas_de` cuenta las internas con `\b[Nn]ormas?\s+de\b` en sus 90 caracteres siguientes.
- **R9.** Marcadores deónticos, sin distinguir mayúsculas, sobre el texto normalizado (R7): «deberán» `\bdeber[áa]n\b`; «no podrán» `\bno\s+podr[áa]n\b`; «salvo» `\bsalvo\b`; «excepto» `\bexcepto\b`. Se reportan ocurrencias y unidades con al menos una; denominadores: unidades y caracteres del conjunto.
- **R10.** Páginas por TO: mínimo, mediana (`statistics.median`) y máximo de `paginas`.
- **R11.** Profundidad máxima de la numeración por TO, desde `estructura_<to>.json`: un punto vale la cantidad de componentes de su `numero`; una sección vale 1.
- **R12.** Puntos de la estructura (`tipo` = `punto`; las secciones no cuentan): **terminal** si no tiene hijos, **contenedor** si tiene. Proporción sobre los puntos del conjunto.
- **R13.** TO con tablas: (a) al menos una tabla lógica parseada; (b) al menos un chunk con `contenido_tabular`. TO con fórmulas: al menos un chunk con `formula`. TO con anexo: al menos una línea del texto crudo de sus chunks que matchea la regex de encabezado de anexo de `data/experiment/segmentacion_84/code/medir_84.py:54` (`^\s*(ANEXO|Anexo)\s*(\d+|[IVXLC]+)?\s*[.:—–-]?\s*$`); es cota inferior: un anexo fuera de los chunks de E0 no se ve.
- **R14.** Tabla de origen de las disposiciones presente si `roles_pagina.tabla_norma_origen` > 0.
- **R15.** Procedencia: `sonda_procedencia.json` → `por_to.<to>.portada_comunicacion` («Última comunicación incorporada», forma P) y `texto_ordenado_al`; no se infiere desde el pie de página (`job_actualizacion/diseno_job_actualizacion.md`, §4). Cobertura = TOs con el campo no nulo sobre los TOs del conjunto.
- **R16.** Grafos: sha256 del archivo; conteo de `nodes[].type` y de `edges[].relation`.
- **R17.** Cifras publicadas: cuatro vías independientes contra `reporte_b584.md:20` (§0).

## 2. Estadísticas por conjunto

Clave base: `conjuntos.<conjunto>.<clave>`. «—» = no aplica o sin artefacto (ver notas).

### 2.1 TOs por clase de la partición y por categoría (R1)

| clase · categoría | corpus_152 | desarrollo_5 | tanda0_5 |
|---|--:|--:|--:|
| no_aplica · normativa_general | 0 | 4 | 0 |
| no_aplica · regimen_informativo | 0 | 1 | 0 |
| no_segmentable_declarado · normativa_general | 1 | 0 | 0 |
| no_segmentable_declarado · regimen_informativo | 11 | 0 | 0 |
| parcial_declarado · regimen_informativo | 2 | 0 | 0 |
| reconocido_pleno · normativa_general | 98 | 0 | 5 |
| reconocido_pleno · regimen_informativo | 40 | 0 | 0 |
| **total** | 152 | 5 | 5 |

Claves: `R1_tos_por_clase_y_categoria`, `R1_tos_por_clase`, `R1_tos_por_categoria`. Control: `inventario_resumen.json` → `por_categoria` da normativa_general 99 y regimen_informativo 53 para los 152.

### 2.2 Páginas por rol (R2) y páginas por TO (R10)

| rol | corpus_152 | desarrollo_5 | tanda0_5 |
|---|--:|--:|--:|
| cuerpo | 3.522 de 6.757 (52,1 %) | 481 de 564 (85,3 %) | 116 de 172 (67,4 %) |
| ficha_registro | 2.281 de 6.757 (33,8 %) | 0 de 564 (0,0 %) | 0 de 172 (0,0 %) |
| historial | 431 de 6.757 (6,4 %) | 43 de 564 (7,6 %) | 27 de 172 (15,7 %) |
| indice | 146 de 6.757 (2,2 %) | 12 de 564 (2,1 %) | 8 de 172 (4,7 %) |
| portada | 202 de 6.757 (3,0 %) | 4 de 564 (0,7 %) | 5 de 172 (2,9 %) |
| tabla_norma_origen | 175 de 6.757 (2,6 %) | 24 de 564 (4,3 %) | 16 de 172 (9,3 %) |
| **páginas** | 6.757 | 564 | 172 |
| páginas por TO: mínimo | 1 | 40 | 14 |
| páginas por TO: mediana | 21 | 60 | 24 |
| páginas por TO: máximo | 2.037 | 204 | 86 |

Claves: `R2_paginas_por_rol`, `R2_paginas_total`, `R10_paginas_por_to`.

### 2.3 Unidades por tipo y por profundidad (R3, R4)

| | corpus_152 | desarrollo_5 | tanda0_5 |
|---|--:|--:|--:|
| tipo punto_terminal | 7.430 de 9.324 (79,7 %) | 1.475 de 1.763 (83,7 %) | 577 de 671 (86,0 %) |
| tipo mini_chunk | 1.550 de 9.324 (16,6 %) | 286 de 1.763 (16,2 %) | 90 de 671 (13,4 %) |
| tipo seccion_sin_puntos | 344 de 9.324 (3,7 %) | 2 de 1.763 (0,1 %) | 4 de 671 (0,6 %) |
| · mini_chunk chapeau_seccion | 121 | 8 | 2 |
| · mini_chunk cierre | 173 | 57 | 18 |
| · mini_chunk intersticial | 446 | 3 | 0 |
| · mini_chunk intro | 810 | 218 | 70 |
| unidades de sub-chunking (incluidas arriba) | 55 | 0 | 0 |
| profundidad 1 | 562 de 9.324 (6,0 %) | 10 de 1.763 (0,6 %) | 6 de 671 (0,9 %) |
| profundidad 2 | 2.470 de 9.324 (26,5 %) | 218 de 1.763 (12,4 %) | 113 de 671 (16,8 %) |
| profundidad 3 | 3.514 de 9.324 (37,7 %) | 627 de 1.763 (35,6 %) | 283 de 671 (42,2 %) |
| profundidad 4 | 2.763 de 9.324 (29,6 %) | 908 de 1.763 (51,5 %) | 269 de 671 (40,1 %) |
| profundidad 5 | 15 de 9.324 (0,2 %) | 0 de 1.763 (0,0 %) | 0 de 671 (0,0 %) |
| **unidades** | 9.324 | 1.763 | 671 |

Claves: `R3_unidades_por_tipo`, `R3_mini_chunks_por_rol`, `R3_unidades_sub_chunk`, `R4_unidades_por_profundidad`; el cruce tipo × profundidad está en `R4_unidades_por_tipo_y_profundidad`.

### 2.4 Tablas y fórmulas (R5, R13)

| | corpus_152 | desarrollo_5 | tanda0_5 |
|---|--:|--:|--:|
| tablas lógicas parseadas | 559 | — | 0 |
| tablas lógicas detectadas (`conteos_b584`) | 563 | — | 0 |
| chunks con `contenido_tabular` | 230 de 9.324 (2,5 %) | 31 de 1.763 (1,8 %) | 0 de 671 (0,0 %) |
| chunks con `formula` | 123 de 9.324 (1,3 %) | 48 de 1.763 (2,7 %) | 5 de 671 (0,7 %) |
| TOs con tabla lógica parseada (a) | 29 de 152 (19,1 %) | — | 0 de 5 |
| TOs con chunk `contenido_tabular` (b) | 57 de 152 (37,5 %) | 3 de 5 | 0 de 5 |
| TOs con chunk `formula` | 39 de 152 (25,7 %) | 2 de 5 | 3 de 5 |
| TOs con línea de encabezado de anexo | 8 de 152 (5,3 %) | 0 de 5 | 0 de 5 |

Desarrollo: no hay archivos `tablas_*` en la E0 de r1 ni en la de la tanda 0 (§6); el testigo de B5.8.3 sobre `cap` tiene 42 tablas lógicas, 42 parseadas (`data/experiment/segmentacion_84/b583_tablas/testigo_capmin/tablas_capmin.json` → `conteos`); para `cla`, `ext`, `pro` y `ric`: NO ENCONTRADO. Claves: `R5_tablas`, `R13_*`.

- corpus_152, TOs con fórmula: `adfsp`, `ceninf`, `ctacte`, `ctavis`, `depaho`, `depinv`, `dmrd`, `efemin`, `fclef`, `finsec`, `inspag`, `jafip`, `lingeef`, `manori`, `manual`, `pagjub`, `polcre`, `raapal`, `ratio`, `ratiofn`, `rdbcra`, `ri2_pm`, `ri_ai`, `ri_ao`, `ri_cc`, `ri_gerc`, `ri_itme`, `ri_msrl`, `ri_oc`, `ri_pgn`, `ri_pnp`, `ri_psp`, `ri_rcl`, `ri_rml`, `ri_tar`, `ri_tsa`, `seggar`, `snp_cheq`, `tasint`.
- desarrollo_5, TOs con fórmula: `cap`, `ric`.
- tanda0_5, TOs con fórmula: `ctacte`, `pagjub`, `polcre`.
- corpus_152, TOs con encabezado de anexo: `adfsp`, `nmaeef`, `nmcief`, `ordcom`, `ri_iepsp`, `ri_laft`, `ri_spi`, `ri_transpa`.
- desarrollo_5, TOs con encabezado de anexo: ninguno.
- tanda0_5, TOs con encabezado de anexo: ninguno.

### 2.5 Largo de unidad en caracteres (R6)

| medida | corpus_152 | desarrollo_5 | tanda0_5 |
|---|--:|--:|--:|
| propio: minimo | 2 | 2 | 5 |
| propio: p10 | 54 | 91 | 72 |
| propio: p25 | 121 | 167 | 132 |
| propio: mediana | 254 | 321 | 237 |
| propio: p75 | 545 | 659 | 417 |
| propio: p90 | 1.161 | 1.239 | 773 |
| propio: p99 | 8.923 | 4.661 | 1.565 |
| propio: maximo | 266.075 | 26.182 | 2.870 |
| completo: minimo | 12 | 96 | 82 |
| completo: p10 | 174 | 311 | 250 |
| completo: p25 | 304 | 566 | 347 |
| completo: mediana | 547 | 1.028 | 522 |
| completo: p75 | 1.118 | 1.699 | 893 |
| completo: p90 | 2.186 | 2.500 | 1.421 |
| completo: p99 | 18.701 | 5.953 | 2.264 |
| completo: maximo | 283.635 | 29.589 | 3.059 |
| n (unidades) | 9.324 | 1.763 | 671 |

Claves: `R6_largo_chars_propio`, `R6_largo_chars_completo`, `R6_largo_chars_propio_por_tipo`.

### 2.6 Estructura de la numeración (R11, R12)

| | corpus_152 | desarrollo_5 | tanda0_5 |
|---|--:|--:|--:|
| profundidad máxima del conjunto | 5 | 4 | 4 |
| TOs con profundidad máxima 0 | 1 de 152 (0,7 %) | 0 de 5 | 0 de 5 |
| TOs con profundidad máxima 1 | 29 de 152 (19,1 %) | 0 de 5 | 0 de 5 |
| TOs con profundidad máxima 2 | 21 de 152 (13,8 %) | 0 de 5 | 0 de 5 |
| TOs con profundidad máxima 3 | 20 de 152 (13,2 %) | 0 de 5 | 0 de 5 |
| TOs con profundidad máxima 4 | 79 de 152 (52,0 %) | 5 de 5 | 5 de 5 |
| TOs con profundidad máxima 5 | 2 de 152 (1,3 %) | 0 de 5 | 0 de 5 |
| puntos terminales | 7.413 de 9.105 (81,4 %) | 1.475 de 1.810 (81,5 %) | 577 de 710 (81,3 %) |
| puntos contenedores | 1.692 de 9.105 (18,6 %) | 335 de 1.810 (18,5 %) | 133 de 710 (18,7 %) |

Claves: `R11_profundidad_maxima_por_to_distribucion`, `R11_profundidad_maxima_del_conjunto`, `R12_*`; por TO, `por_to.<to>.profundidad_maxima`.

### 2.7 Remisiones (R8)

| | corpus_152 | desarrollo_5 | tanda0_5 |
|---|--:|--:|--:|
| internas (al mismo TO) | 2.561 | 875 | 141 |
| externas (norma nombrada) | 1.464 | 197 | 51 |
| externas anafóricas («dicho ordenamiento») | 3 | 1 | 0 |
| sensibilidad: internas con «normas de» después | 13 | 4 | 0 |
| unidades con alguna remisión | 2.180 de 9.324 (23,4 %) | 625 de 1.763 (35,5 %) | 138 de 671 (20,6 %) |
| internas por TO: minimo | 0 | 28 | 9 |
| internas por TO: mediana | 8,5 | 43 | 17 |
| internas por TO: maximo | 141 | 472 | 80 |
| TOs con alguna interna | 123 de 152 (80,9 %) | 5 de 5 | 5 de 5 |
| externas por TO: minimo | 0 | 5 | 2 |
| externas por TO: mediana | 4 | 41 | 6 |
| externas por TO: maximo | 110 | 81 | 21 |
| TOs con alguna externa | 130 de 152 (85,5 %) | 5 de 5 | 5 de 5 |

Claves: `R8_remisiones_total`, `R8_unidades_con_remision`, `R8_remisiones_por_to`, `R8_internas_por_to_resumen`, `R8_externas_por_to_resumen`.

### 2.8 Marcadores deónticos (R9)

| marcador | corpus_152 | desarrollo_5 | tanda0_5 |
|---|--:|--:|--:|
| «deberán»: ocurrencias | 2.724 | 363 | 100 |
| «deberán»: unidades con ≥ 1 | 1.587 de 9.324 (17,0 %) | 240 de 1.763 (13,6 %) | 79 de 671 (11,8 %) |
| «no podrán»: ocurrencias | 179 | 27 | 14 |
| «no podrán»: unidades con ≥ 1 | 168 de 9.324 (1,8 %) | 27 de 1.763 (1,5 %) | 13 de 671 (1,9 %) |
| «salvo»: ocurrencias | 138 | 29 | 9 |
| «salvo»: unidades con ≥ 1 | 116 de 9.324 (1,2 %) | 26 de 1.763 (1,5 %) | 9 de 671 (1,3 %) |
| «excepto»: ocurrencias | 329 | 72 | 17 |
| «excepto»: unidades con ≥ 1 | 234 de 9.324 (2,5 %) | 59 de 1.763 (3,3 %) | 17 de 671 (2,5 %) |
| caracteres (`chars_propio`) | 6.432.648 | 1.070.995 | 230.994 |

Claves: `R9_deonticos_ocurrencias`, `R9_deonticos_unidades_con_al_menos_una`, `R9_chars_propio_total`.

### 2.9 Tabla de origen de las disposiciones (R14) y procedencia (R15)

| | corpus_152 | desarrollo_5 | tanda0_5 |
|---|--:|--:|--:|
| TOs con tabla de origen | 90 de 152 (59,2 %) | 4 de 5 | 5 de 5 |
| TOs con «última comunicación incorporada» legible | 90 de 152 (59,2 %) | 4 de 5 | 4 de 5 |
| TOs con «texto ordenado al» | 68 de 152 (44,7 %) | 4 de 5 | 4 de 5 |
| TOs con portada ilegible por glifos | 7 de 152 (4,6 %) | 0 de 5 | 1 de 5 |

Claves: `R14_tos_con_tabla_norma_origen`, `R15_procedencia_cobertura`; por TO, `por_to.<to>.{portada_comunicacion,texto_ordenado_al}`. La sonda leyó los PDF de `escalado_prep/pdfs/` y los del subset (`data/experiment/subset/`): `job_actualizacion/code/sonda_procedencia.py`, función `objetivo`.

## 3. Por TO: conjunto de desarrollo y conjunto de la tanda 0

| TO | categoría | pág. | tabla de origen (pág.) | unidades | prof. máx. | puntos term./cont. | remisiones int./ext. | deberán | no podrán | salvo | excepto | última com. incorporada | texto ordenado al |
|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|---|
| `cap` | normativa_general | 204 | 9 | 462 | 4 | 401/106 | 292/50 | 191 | 10 | 14 | 23 | A 8418 | 09/04/26 |
| `cla` | normativa_general | 60 | 6 | 143 | 4 | 127/25 | 28/41 | 24 | 1 | 5 | 1 | A 8378 | 19/12/2025 |
| `ext` | normativa_general | 201 | 7 | 973 | 4 | 783/165 | 472/5 | 82 | 10 | 10 | 34 | A 8307 | 25/08/2025 |
| `pro` | normativa_general | 40 | 2 | 101 | 4 | 87/21 | 40/20 | 51 | 5 | 0 | 3 | A 8433 | 06/05/26 |
| `ric` | regimen_informativo | 59 | 0 | 84 | 4 | 77/18 | 43/82 | 15 | 1 | 0 | 11 | sin dato | sin dato |
| `ctacte` | normativa_general | 86 | 10 | 388 | 4 | 336/83 | 80/21 | 65 | 9 | 9 | 13 | A 8444 | 04/06/26 |
| `docvig` | normativa_general | 14 | 1 | 31 | 4 | 28/10 | 9/4 | 5 | 0 | 0 | 1 | A 8338 | 01/10/2025 |
| `lingob` | normativa_general | 24 | 1 | 139 | 4 | 117/21 | 9/6 | 10 | 0 | 0 | 0 | A 7465 | 25/02/2022 |
| `pagjub` | normativa_general | 16 | 2 | 52 | 4 | 43/11 | 17/2 | 11 | 1 | 0 | 0 | ilegible (glifos) | sin dato |
| `polcre` | normativa_general | 32 | 2 | 61 | 4 | 53/8 | 26/18 | 9 | 4 | 0 | 3 | A 8446 | 11/06/2026 |

Clave: `conjuntos.<conjunto>.por_to.<to>`. «ext.» suma externas y anafóricas. Los 152, por TO, están en `conjuntos.corpus_152.por_to`.

## 4. Grafos (R16)

| | KG-Tanda0-Desarrollo-r1 | KG-Reextraído-r1 |
|---|--:|--:|
| sha256 | `eab2fdd01dec4dad…` | `0226e9477baee02d…` |
| nodos | 6.378 | 6.529 |
| aristas | 15.007 | 17.772 |
| tipos de nodo | 10 | 7 |
| tipos de relación | 17 | 16 |

Nodos por tipo:

| tipo | KG-Tanda0-Desarrollo-r1 | KG-Reextraído-r1 |
|---|--:|--:|
| Comunicacion | 17 | 36 |
| Condicion | 1.178 | 0 |
| Definicion | 531 | 0 |
| Excepcion | 329 | 539 |
| Obligacion | 1.626 | 2.484 |
| Operacion | 1.555 | 1.957 |
| Potestad | 381 | 0 |
| Restriccion | 632 | 1.397 |
| Sujeto | 124 | 111 |
| TextoOrdenado | 5 | 5 |

Aristas por predicado:

| predicado | KG-Tanda0-Desarrollo-r1 | KG-Reextraído-r1 |
|---|--:|--:|
| aplica_a | 2.898 | 3.254 |
| condicion_de | 448 | 0 |
| condiciona | 61 | 234 |
| ejecuta | 121 | 87 |
| establecida_en | 5.862 | 5.082 |
| exceptua | 60 | 184 |
| exceptua_obligacion | 94 | 236 |
| instancia_de | 7 | 7 |
| limita | 284 | 1.041 |
| miembro_de | 51 | 17 |
| padre_sugerido | 18 | 41 |
| parte_de | 1 | 1 |
| prohibe | 98 | 176 |
| referencia | 4.256 | 5.680 |
| regula | 369 | 1.300 |
| requiere | 321 | 375 |
| subclase_de | 58 | 57 |

Rutas: `data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo/r1/kg.json`, `data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json`. Clave: `grafos`. Sha completos en el JSON. Recómputo de una línea:

```bash
python3 -c "import json,collections; g=json.load(open('data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json')); print(len(g['nodes']), len(g['edges']), dict(collections.Counter(n['type'] for n in g['nodes'])))"
```

## 5. Fuentes principales (sha256)

| archivo | sha256 |
|---|---|
| `data/experiment/segmentacion_84/b584_particion/particion_152.json` | `8f4012e4d95cbd8ea35128c4915becdff5314a731516d6ad30b18a7b74d7ee43` |
| `data/experiment/segmentacion_84/b584_particion/conteos_b584.json` | `761e4d90c006de3d07e39fadf69c27252e3721ce404ee143f5165cf39a6c4084` |
| `data/experiment/segmentacion_84/b584_particion/reporte_b584.md` | `f223b3be8976fdd7c615a3b2da56459cd2218e1b23cfc8d07688c389a7ea59a8` |
| `data/experiment/reextraccion_v2/e0_chunking/salida_tanda0/conteos.json` | `f6dfc7df1e74bc20bfb051b2523cb772f3e61532b68ca9a3270eadad1487c574` |
| `data/experiment/escalado_prep/inventario_resumen.json` | `d60e65abda005433ac5d13c367b55fd40efa3124b1c698e1633f6fc1bd306f82` |
| `data/experiment/escalado_prep/inventario_tos.csv` | `a1db24fd2beaed2110349f295e7928bc0cd9d18333cce527773233a156a37e1f` |
| `data/experiment/escalado_prep/indice_oficial_raw.json` | `91dc9f864f0822ce363eef6159869194c0c2f51ac878979ab62ff8b47f89fec4` |
| `data/experiment/reextraccion_v2/manifiestos/desarrollo_5tos.json` | `868b301fe800961804b58bf381e925ae76e442863aea8afb432ef4949e1f5ffc` |
| `data/experiment/job_actualizacion/sonda_procedencia.json` | `1a8c2b33fe223ebbb4e1c640cd02b04cee047e2affdf1814decda9397627a243` |
| `data/experiment/segmentacion_84/b583_tablas/testigo_capmin/tablas_capmin.json` | `4c486b3314faef1302cd5fa2913d182de6d05222305d9a71d233188d783c2a02` |
| `data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo/r1/kg.json` | `eab2fdd01dec4dad026d596a793919e666920fab127d7efb14b5b00857ae64ef` |
| `data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json` | `0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a` |

Los sha256 de los 314 archivos `chunks_<to>.json` y `estructura_<to>.json` leídos están en la clave `fuentes_por_to`.

## 6. Controles de consistencia

- tanda0_5: `b584_particion/<to>/` y `salida_tanda0/` byte-idénticos (chunks y estructura): sí.
- desarrollo_5: `salida_tanda0/` y `salida_enm01/` (E0 de KG-Reextraído-r1) byte-idénticos: sí.
- Unidades contadas distintas de `unidades_extraccion` / `chunks` de los conteos: 0 TOs.
- `chars_propio` == `len(texto)` en todas las unidades: sí.
- TOs del grupo `inventariado_152` de la sonda iguales a los 152 de la partición: sí.
- Páginas de la sonda distintas de las de E0: 0 TOs.
- Puntos sin hijos de la estructura contra chunks `punto_terminal`: difieren en 5 TOs (`manori` 10 contra 12, `nmaeef` 24 contra 31, `ri2_ae` 3 contra 5, `ri_ccna` 11 contra 14, `snp_dd` 45 contra 48); todos con partes de sub-chunking: sí. Contra las unidades distintas de esos chunks (las partes de una misma unidad cuentan una vez), esos TOs coinciden: sí; difieren en cambio otros 4 TOs (`adfsp` 96 contra 87, `ceninf` 36 contra 32, `cirmo3` 215 contra 163, `ri_niif` 9 contra 5), explicados en el punto siguiente. Por eso R12 (estructura) y R3 (chunks) no dan el mismo número de terminales en corpus_152. Claves `controles.puntos_terminales_estructura_vs_chunks` y `controles.puntos_terminales_estructura_vs_unidades_distintas`.
- Ids de chunk repetidos dentro de un mismo TO: 4 TOs, 69 chunks de más (`adfsp` 9, `ceninf` 4, `cirmo3` 52, `ri_niif` 4); con el mismo texto: 0. Son colisiones de numeración (texto distinto bajo el mismo `id`), no chunks duplicados; las 9.324 unidades las incluyen. La diferencia que queda entre puntos sin hijos de la estructura y unidades distintas es igual, TO por TO, a esos chunks de más: sí. Claves `controles.ids_de_chunk_repetidos` y `controles.diferencia_terminales_explicada_por_ids_repetidos`.
- Archivos `tablas_*` en `salida_enm01/` y `salida_tanda0/`: 0.

## 7. Límites y NO ENCONTRADO

- Clase de la partición para desarrollo_5: no aplica (no están en `particion_152.json`).
- Tablas lógicas de `cla`, `ext`, `pro` y `ric`: NO ENCONTRADO (sin archivos `tablas_*` en la E0 de r1; solo `cap` tiene testigo de B5.8.3).
- Remisiones: detector por regex sobre el texto de E0, sin resolución del destino; «externa» no garantiza otro TO. No es el conteo de aristas `referencia` de los grafos.
- Anexos: cota inferior (solo encabezados de anexo que quedaron dentro de chunks de E0).
- Procedencia: TOs sin portada legible quedan sin dato; no se infiere desde el pie.

