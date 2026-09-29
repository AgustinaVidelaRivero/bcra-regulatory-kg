# Reporte de la fase 2a de la tanda 0 (B6.0): validación de diseño

Unidad U-TANDA0-2A (mandato `docs/mandatos/UTANDA0_2A_corrida.md`, `e738cdd`), con el
anexo E5.c (`docs/mandatos/UTANDA0_2A_E5c_adjudicacion.md`, `0488a9b`). Pre-registro
`docs/preregistro_tanda0.md` (`c80b03f`) con sus enmiendas de la observación (12)
(`8e13be3`) y de la partición 2a/2b (`a551c57`). Este documento es el paso 8 de A9 en su
emisión de 2a: validación de diseño, sin umbral (decisión 6); las bandas de A4 son ayudas
de lectura, no criterios de retiro. Redactado el 29/09/2026; commit PENDIENTE de la autora.

Fuentes de todos los números (cada una se regenera con el comando indicado, USD 0):

| archivo | comando |
|---|---|
| `reports/tanda0/lectura_e6_tanda0.{json,md}` | `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/tanda0/code/lectura_e6_tanda0.py` |
| `reports/tanda0/atribucion_tanda0.{json,md}`, `atribucion_por_traza_tanda0.md` | `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/ev2_tanda0/code/atribucion_tanda0.py` (lee Neo4j en solo lectura) |
| `reports/tanda0/ucita2_indicadores_C{2,3,4}.{json,md}` | `PYTHONDONTWRITEBYTECODE=1 python3 -B scripts/ucita2_indicadores.py --manifiesto data/experiment/reextraccion_v2/manifiestos/tanda0_10tos.json --e0 data/experiment/reextraccion_v2/e0_chunking/salida_tanda0 --trazas data/experiment/ev2_tanda0/trazas --tandas <label> <label>_enc_r1 <label>_enc_r2 <label>_enc_r3 --out-json … --out-md …` |
| `reports/tanda0/ucita2_indicadores_C5.{json,md}` | `PYTHONDONTWRITEBYTECODE=1 python3 -B data/experiment/ev2_tanda0/code/ucita2_c5_tanda0.py` |
| `reports/tanda0/tabla_celdas_definitiva_E5c.{json,md}` | `cierre_adj_tanda0.py --commit-marcas 8e0597c` (`ecd102c`) |
| `reports/tanda0/tabla_celdas_E5.json`, `registro_modelos_2a.json`, `registro_modelos_2a_dirigida.json` | cierres de E5 y de la re-extracción dirigida (`7f3b207`, `5fc7d3a`) |

## 0. Desvíos declarados que condicionan la lectura

- **Adjudicación de C2 a C5.** La ejecutó una instancia de modelo, la instancia
  adjudicadora, con calibración parcial de la autora sobre 20 de los 174 criterios
  (declaración de la autora; mensaje del commit `8e0597c`; las cifras no tienen otro
  artefacto en el repo: NO VERIFICADAS). Es un
  desvío del pre-registro (`docs/preregistro_tanda0.md:308-309`, protocolo de C1 con
  adjudicación ciega) y del anexo E5.c (decisión 5). Modelo y versión de la instancia
  adjudicadora: a confirmar por la autora. Detalle en
  `data/experiment/ev2_tanda0/adjudicacion/nota_episodios_adjudicacion_tanda0.md`.
  Consecuencia: los definitivos de C2 a C5 descansan en marcas de la instancia
  adjudicadora, y la muestra de control mide el **acuerdo entre el juez y la instancia
  adjudicadora**, no una validación del juez contra lectura humana.
- **Lecturas de (12) y de la matriz.** Son lecturas asistidas: las hizo una instancia de
  modelo y la autora las revisó (`reports/tanda0/obs12_lectura/fila_obs12.md`, «Desvío
  declarado»; `reports/u_estudio_matriz/lectura/resultado_lectura_matriz.md`; commit
  `aa7ee11`). El protocolo y el umbral de la matriz los fijó la autora antes de abrir la
  muestra. Modelo y versión de la instancia: a confirmar por la autora.

## 1. Qué corrió

| etapa | contenido | commit |
|---|---|---|
| E1 | manifiestos, E0 de los diez TOs, cableado de r1 en seco | `47c9283` |
| E2 | extracción E1–E3 de los diez TOs | `ad6d5ad` |
| re-extracción dirigida | tres unidades de cap a 16.384 (U-TANDA0-2A-DIR) | `6592fb6`, `5fc7d3a` |
| E3 | tres ensamblados; gate 5 (Neo4j) y gate de release | `1b8916c`, `cf6ca42` |
| E4 | sorteo sellado de (12) | `e6a3169` |
| E5 | celdas C2 a C5 con juez v1 N=3 y §7 | `4b91902` (instrumentos), `7f3b207` |
| E5.c | planillas ciegas, marcas, cierre de la adjudicación | `f425657`, `2e4280c` → `8e0597c`, `ecd102c` |
| E6 | lecturas, atribución, cita y este reporte | PENDIENTE (commit de la autora) |

Grafos: KG-Tanda0-Desarrollo-r1 (`eab2fdd0…`, cinco TOs de desarrollo, 1.763 unidades),
`ens_cinco/r1` (`4097d4fd…`, los cinco nuevos, 671 unidades) y KG-Tanda0-Diez-r1
(`dd42d6d9…`, los diez, 2.434 unidades), todos en
`data/experiment/reextraccion_v2/corpus_tanda0/ens_*/r1/kg.json`.

## 2. Tabla de las celdas

Definitivas tras la adjudicación de la instancia adjudicadora
(`reports/tanda0/tabla_celdas_definitiva_E5c.json`); C1 citada de `774acac`. Intervalos de
Wilson al 95 %.

| celda | grafo | índice | n | correcto | parcial | incorrecto | Wilson correcto | Wilson incorrecto |
|---|---|---|---|---|---|---|---|---|
| C1 (`774acac`) | KG-Reextraído-r1 | GraphIndex en memoria | 40 | 6 | 26 | 8 | 0,071–0,291 | 0,105–0,348 |
| C2 | KG-Reextraído-r1 | Neo4j fulltext | 40 | 9 | 24 | 7 | 0,123–0,375 | 0,088–0,320 |
| C3 | KG-Tanda0-Desarrollo-r1 | GraphIndex en memoria | 40 | 10 | 23 | 7 | 0,142–0,402 | 0,088–0,320 |
| C4 | KG-Tanda0-Desarrollo-r1 | Neo4j fulltext | 40 | 11 | 21 | 8 | 0,161–0,428 | 0,105–0,348 |

Comparaciones pre-registradas (A3.3), una fila por par, en el formato de A3.4:

| par | variable | correcto | incorrecto | intervalos | ¿el n alcanza? |
|---|---|---|---|---|---|
| C1 vs C2 | índice | 6 → 9 | 8 → 7 | solapados | no |
| C3 vs C4 | índice | 10 → 11 | 7 → 8 | solapados | no |
| C1 vs C3 | esquema | 6 → 10 | 8 → 7 | solapados | no |
| C2 vs C4 | esquema | 9 → 11 | 7 → 8 | solapados | no |

Con n = 40, las diferencias de 1 a 3 preguntas no se leen como señal (A3.4). La de C1
contra C3 en correctas es de 4; los intervalos se solapan y tampoco alcanza para leerla
como señal. Además, C1 y C3 difieren en algo más que el esquema: la diferencia conocida de
`cap::4.2.1.2`, con 0 nodos en r1 y 57 en el desarrollo de la tanda 0 (plan, fila B6.0
fase 2a, «Diferencia conocida entre C1 y C3»). Ninguna de las 40 preguntas ancla ahí; el
punto suma candidatos al retrieval de las preguntas de cap. Lo mismo vale para C2 contra
C4. Y C1 fue adjudicada por la autora, mientras que C2 a C4 lo fueron por la instancia
adjudicadora (sección 0).

Vías de los definitivos (juez base / juez §7 / adjudicación base / adjudicación §7): C2
11 / 21 / 5 / 3; C3 13 / 20 / 7 / 0; C4 14 / 20 / 5 / 1.

**Acuerdo entre el juez y la instancia adjudicadora en la muestra de control** (no es una
validación del juez contra lectura humana): C2, C3 y C4 con 4 de 4 fichas en acuerdo
exacto cada una; agregado, 12 de 12 fichas y 54 de 54 criterios, sin sobre-acreditación
ni sub-acreditación, y 0 de 3 correctos auditados caídos.

### C5, aparte (no se cruza con C1 a C4)

| celda | grafo | índice | n | correcto | parcial | incorrecto | Wilson correcto | Wilson incorrecto |
|---|---|---|---|---|---|---|---|---|
| C5 | KG-Tanda0-Diez-r1, 20 preguntas nuevas | GraphIndex en memoria | 20 | 8 | 8 | 4 | 0,219–0,613 | 0,081–0,416 |

- Vías: 8 / 8 / 4 / 0. Acuerdo entre el juez y la instancia adjudicadora en la muestra de
  control: 1 de 2 fichas, 5 de 6 criterios, 1 sub-acreditación.
- **T0F-008 y T0F-013 quedan fuera del dominio de calibración del juez.** Tienen tres
  criterios sin cita textual: T0F-008 criterios 1 y 3, T0F-013 criterio 1. Pasaron al
  juez tal como están sellados, por la decisión (a) de la autora. En la base el juez
  marcó «cumplido» en los 9 veredictos de esos tres criterios, con tres repeticiones
  (`reports/tanda0/tabla_celdas_E5.json`). Las dos preguntas quedaron fuera del marco de la
  muestra de control (anexo E5.c, decisión 2).

## 3. Predicciones de A4, una fila por predicción

Fuente: `reports/tanda0/lectura_e6_tanda0.json`. Sin umbral: una observación fuera de
banda es un hecho a explicar, no un retiro.

| predicción | línea de base | predicho | observado | veredicto |
|---|---|---|---|---|
| (10) aristas de extracción por unidad, desarrollo (1.763) | 6,81 (r1) | 6,81 a 8,0 | 6,03 (10.634 aristas) | debajo de la banda |
| (10) aristas de extracción por unidad, tanda 0 sola (671) | 6,81 | 5,0 a 8,0 | 4,99 (3.345 aristas) | debajo de la banda, por 0,01 |
| (11) menciones «fuera del inventario» que pasan a resolverse al entrar los cinco | 0 de 106 | 4 (2 de polcre, 2 de docvig) | 4 remisiones de desarrollo fuera del inventario nombran a polcre (2) y docvig (2); en diez, las 4 resueltas y 0 siguen fuera | coincide con la predicción, contada sobre las menciones de esta extracción (ver nota) |
| (11) `aristas_cross_to`, diez TOs | 188 | mayor que 188 | 186 | no cumple |
| (11) `aristas_cross_to`, desarrollo | 188 | 188 ± 20 | 124 | fuera de la banda |
| (1) Condicion contra la guarda de modalidad | 1/12 | sin umbral | no medida: muestreo no definido; población 1.178 Condicion en desarrollo, 205 en cinco | no medida |
| (2) vaciamientos | 2/43 · 2/27 | sin umbral | 46 unidades con 0 relaciones aceptadas en la versión final de E1 (77 en el primer intento), de 2.434; sin lectura de muestra | medida parcialmente |
| (3) duplicación entre cajas | 5 casos v1 | sin umbral | no medida: sin instrumento definido | no medida |
| (4) un TextoOrdenado por TO | 2 archivos afectados | 1 por TO | 1 por TO en los tres ensamblados | medida |
| (5) `requisito_de_estructura` | 0 | 0 | 0 en los diez; `tipo_obligacion_normalizados` 2 en ctacte y 1 en lingob; `ext::10.4.3.1` con 0 y 0 (hallazgo S20) | medida |
| (6) unidades propias vacías | sin línea de base | sin umbral | health-check de E0 sobre los cinco: 0 avisos de página de cuerpo sin sección; señales de cid en lingob y pagjub (A2.4) | medida |
| (7) roles de alcance en `ejecuta` | n = 1 | sin umbral | población: 21 de 121 aristas `ejecuta` con origen `Sujeto_rol_alcance_*` en desarrollo, 0 de 36 en cinco; tasa sin apoyo textual no medida | medida parcialmente |
| (8) tasa de `sujeto_propuesto` | 3,08 % | sin umbral | 1,39 % en desarrollo (42 / 3.019), 1,90 % en cinco (19 / 1.000), 1,52 % en diez | medida |
| (9) emisiones de `Sujeto_entidad_originante_de_transferencia` | 13 menciones en fase 1 | sin umbral | 5 emisiones en E1 (cap 4, ext 1), 0 en los cinco nuevos; 5 aristas en desarrollo y en diez | medida |
| (12) aristas de extracción correctas, tanda 0 sola | sin línea de base | sin predicción | 25 de 30 (Wilson 0,664–0,927), lectura asistida revisada por la autora; 5 incorrectas: 4 `E1-prompt`, 1 `catálogo` | sin veredicto (fila de 2b, `fila_obs12.md`) |

Notas de lectura:

- (10) queda debajo de la banda en los dos ensamblados. El conteo coincide con la
  extracción más magra que muestran los rechazos de E1 por `firma_invalida` (982, punto 2
  de la sección 4) y las intrínsecas (grado medio 4,71 en desarrollo contra 5,44 en r1).
  No llega a los 6,0 que el pre-registro señalaba como vaciamiento sistemático en
  desarrollo.
- (11), menciones: salen de la extracción (E1), no del texto de E0. Desarrollo tiene 783
  contra 1.089 de r1, así que las 106 de r1 no se siguen una por una. El conteo
  comparable es el de las remisiones de esta extracción:
  `obs11.menciones_desarrollo_a_los_cinco` del JSON.
- (11), `aristas_cross_to`: las 124 de desarrollo y las 186 de diez coinciden con el conteo
  de aristas `referencia` entre documentos distintos del punto 6 de la sección 4. La baja
  respecto de 188 acompaña la baja de menciones (783 contra 1.089).
- (1), (3) y la parte de lectura de (2) y (7): A4.3 dejó el muestreo «a definir en fase 2»
  y el mandato no lo definió. Quedan como población contada; su lectura es una decisión
  pendiente.

## 4. Lecturas agregadas pedidas por el plan (fila B6.0 fase 2a, «LECTURA DE E6»)

1. **Aristas `referencia` por tipo de origen.** En los tres ensamblados ninguna sale de
   Condicion, Potestad ni Definicion (hallazgo H1, confirmado). En desarrollo: Operacion
   1.805, Obligacion 1.409, Restriccion 518, Excepcion 510, TextoOrdenado 14.
2. **Rechazos de E1 por par.** 982 `firma_invalida` en 65 pares
   (`reports/u_audit_tipos_v3/p4_resumen.json`, sha256 `e63e2618…`). Los mayores:
   Condicion `condicion_de` Operacion 424, Condicion `condicion_de` Potestad 231, Condicion
   `aplica_a` Sujeto 45. Sobre la matriz: la lectura asistida revisada por la autora da
   que → Operacion cumple el criterio (27 de 29, Wilson 0,780–0,981) y que → Potestad no
   (27 de 30, Wilson 0,744–0,965). La decisión sigue abierta, con los mentores.
3. **Respuestas parciales o incorrectas: ¿estaba la información en el grafo?** Clase A0.2
   de la traza representativa de cada par definitivo parcial o incorrecto
   (`reports/tanda0/atribucion_tanda0.json`):

   | celda | no estaba en el grafo (ausencia_kg) | estaba y no se navegó (alcanzabilidad + vista_no_consultada) | se consultó y la respuesta falló (generacion) |
   |---|---|---|---|
   | C1 (`774acac`) | 8 | 8 | 18 |
   | C2 | 6 | 2 | 23 |
   | C3 | 8 | 7 | 15 |
   | C4 | 9 | 3 | 17 |
   | C5 | 0 | 4 | 8 |

   La clase modal sigue siendo generación: grounded ≠ correct. El cruce de las ausencias
   con los candidatos 1 a 3 del §4 del laudo de r2 y con la matriz pide lectura y no se
   hizo en esta unidad. El detalle de los incorrectos, uno por uno, está en
   `reports/tanda0/atribucion_tanda0.md`.
4. **Patrones de navegación de A1.8.** (a) Un nodo que porta el ancla aparece como vecino
   por `referencia` y nunca recibe `ver_nodo`: 4 trazas en C2 (20 nodos), 2 en C4 (5
   nodos), 0 en C3 y C5. (b) `ver_vecinos` con dirección «salientes» sobre una Operacion
   con aristas entrantes desde Restriccion: 22 llamadas en 19 trazas en C2, 12 en 11 en
   C3, 16 en 12 en C4 y 4 en 4 en C5. El patrón (b) aparece en las cuatro celdas; el (a)
   solo en las dos de Neo4j. Si alguno se considera sistemático, queda como DECISIÓN
   ABIERTA de la autora: instrucciones del agente o comportamiento de la herramienta de
   vecinos.
5. **Respuesta invertida del ejemplo del préstamo.** No aplica a EV2 ni a C5: ninguna
   pregunta ancla en `cla:5.1.1.1` ni en `cla:3.7`.
6. **Aristas entre documentos distintos.** Regla: el documento de un nodo es el conjunto
   de `to` de sus provenances; los nodos con más de un documento, como el Sujeto del
   catálogo o los nodos fundidos, se cuentan aparte. En desarrollo hay 124 aristas
   `referencia` entre documentos y 0 de extracción; 303 de extracción tocan un nodo
   multidocumento. En cinco hay 3 `referencia` y 2 de extracción (`padre_sugerido`); en
   diez, 186 `referencia` y 2 de extracción.

## 5. Atribución A0.2 y exactitud de cita (mandato, E6 b)

Atribución con la regla sellada (`data/experiment/ev2_reporte/regla_atribucion.md`,
`40603a9`; funciones de `atribucion_fallas.py`, `85d9fdb`, sin editar), con el índice de
cada celda: GraphIndex en C3 y C5, Neo4jIndex fulltext en C2 y C4.

| celda | trazas base | ausencia_kg | alcanzabilidad | vista_no_consultada | generacion | correcto | replay / replay fuerte |
|---|---|---|---|---|---|---|---|
| C1 (`774acac`) | 40 | 8 | 7 | 1 | 19 | 5 | 40 / 40 |
| C2 | 40 | 6 | 0 | 2 | 23 | 9 | 40 / 40 |
| C3 | 40 | 8 | 2 | 4 | 17 | 9 | 40 / 40 |
| C4 | 40 | 9 | 0 | 2 | 18 | 11 | 40 / 40 |
| C5 | 20 | 0 | 4 | 0 | 8 | 8 | 20 / 20 |

- Re-corridas del §7: replay y replay fuerte completos en las cuatro celdas (72, 56, 61 y
  23 trazas), con 0, 4, 2 y 1 votos excluidos por invariancia.
- En C2 y C4 el replay fuerte contra Neo4j reproduce exactamente las salidas capturadas.
- **Extensión declarada en C5:** el parser de anclas (`sinteticas/comun.py`, `DOC2TO`)
  solo conoce los cinco PDF de desarrollo. Sin extensión, toda falla de C5 salía
  ausencia_kg por construcción. Para C5 el mapa archivo → TO se amplía en memoria con los
  cinco del manifiesto de la tanda 0.

Exactitud de cita, respuestas de contenido de la corrida base (fracciones crudas):

| celda | N | cita fundada | cita existente | cita al ancla |
|---|---|---|---|---|
| C1 (`fb6ef69`) | 31 | 30 | 31 | 28 |
| C2 | 33 | 31 | 33 | 32 |
| C3 | 32 | 32 | 32 | 29 |
| C4 | 33 | 33 | 33 | 31 |
| C5, lectura extendida | 18 | 18 | 18 | 15 (alguna ancla) · 14 (todas las anclas) |

- El control del indicador 1 da 0 discrepancias en todas las tandas.
- **Extensión declarada en C5:** el script sellado toma solo trazas `EV2F-*`, aborta con
  dos anclas y declara no parseables los PDF `ctacte.pdf` a `docvig.pdf`.
  `ucita2_c5_tanda0.py` lo importa sin editarlo y reporta dos lecturas del parseo:
  estricta, con indicadores 2 y 3 en 0 por esa causa, y extendida, con los archivos del
  manifiesto. También reporta dos lecturas del indicador 3 con dos anclas: alguna ancla y
  todas las anclas.

## 6. Gate de release, suite e intrínsecas

- **Shapes con perfil congelado** (`reports/tanda0/shapes_ens_*.json`): «NO PASA» en los
  tres ensamblados solo por S19, que es bloqueante. La causa son los seis ids del bloque
  v3 ausentes de `esquema_v3_clases.json`; por la decisión pre-registrada del 27/09 se
  reporta aparte y no bloquea el release, y completar el catálogo queda para r2. S7, S10 y
  S12 están en FAIL no bloqueante; S8, S11, S21 y S23, en WARN.
- **Control de las tres `aplica_a`** del checklist del gate: 0 de 3 en los tres
  ensamblados. Es un control vacuo en la tanda 0, porque ri_tii y ri_pscpp no están en
  ningún ensamblado; recién significa algo en la tanda 1.
- **Suite de regresión, sin `--esperado`** (línea de base observada, resuelto / persiste /
  no aplicable): desarrollo 22 / 16 / 8; cinco 11 / 22 / 13 y diez 20 / 18 / 8,
  informativos. De los 46 ítems, contra la entrada KG-Reextraido-r1 de la fixture
  `696f3f94…`, cambian 10: 6 pasan de resuelto a persiste, 1 de persiste a resuelto, 1 de
  persiste a no aplicable y 2 de no aplicable a persiste. Los ítems son BKL-0006,
  BKL-0028, BKL-0029, E4-a7, E4-a8, RT-C5-3, T2, T4, T5 y T7; la tabla completa está en
  `reports/tanda0/lectura_e6_tanda0.md`.
- **Intrínsecas de generación 3** (r1 / desarrollo / cinco / diez): M1 0,542 / 0,493 /
  0,343 / 0,491; M4 grado medio 5,44 / 4,71 / 4,03 / 4,59; M7 0 en los cuatro; M10 chunks
  mudos 1 / 3 de 1.763 / 1 de 671 / 4 de 2.434, que son las unidades rechazadas en E1. M3
  queda no computable en generación 3 (limitación declarada del gate 6).

## 7. Costo real contra la estimación

| etapa | USD | tope |
|---|---|---|
| E2 (E1 18,07 + E3 22,28, reintentos de E1 incluidos) | 40,35 | 60 |
| re-extracción dirigida | 0,46 | 1 |
| E5 (C2 6,66 · C3 6,22 · C4 6,14 · C5 2,25) | 21,26 | 40 |
| E5.c y E6 | 0 | |
| **total 2a** | **62,07** | 100 (estimación A7: 69,18) |

Fuentes: `corpus_tanda0/salida/presupuesto_compartido.json` y `estado_corpus.json`,
`salida_dirigida/presupuesto_reextraccion_dirigida.json` y `reports/tanda0/tabla_celdas_E5.json`
(este último, desde las dbs de `ev2_tanda0/cache/`); bloque `costos` de
`lectura_e6_tanda0.json`.

## 8. Registro de modelos

| etapa | modelo según la API | pedido | temperatura | llamadas |
|---|---|---|---|---|
| E2, E1 y reintentos | `claude-haiku-4-5-20251001` | `claude-haiku-4-5` | default del proveedor | 2.434 + 254 misses |
| E2, E3 | `claude-sonnet-5` | `claude-sonnet-5` | default del proveedor | 2.678 misses |
| E2, total | | | | 5.375 = 5.366 misses + 9 hits |
| re-extracción dirigida | `claude-haiku-4-5-20251001` (E1 3, reintento 1) y `claude-sonnet-5` (E3 4) | ídem | default del proveedor | 8 misses |
| E5, agente | `claude-haiku-4-5-20251001` | ídem | 0 | incluidas en 3.630 misses |
| E5, juez | `claude-sonnet-4-6` | ídem | 0.0 | incluidas en 3.630 misses; 228 hits del juez del §7 por textos duplicados |
| E5.c, adjudicación | instancia de modelo fuera de la API del repo | | | a confirmar por la autora (modelo y versión) |
| E6 | sin llamadas | | | 0 |

Fuentes: `reports/tanda0/registro_modelos_2a.json` (etapas E2 y E5) y
`registro_modelos_2a_dirigida.json`. Todos los datos salen de las dbs de caché, nunca de
memoria (A6).

## 9. Incidencias

1. E2: el reintento por corte a 32.768 lo rechazó la guarda del SDK antes de enviarlo, y
   tres unidades de cap quedaron sin extraer. Las recuperó la re-extracción dirigida.
2. E2: el checkpoint de cierre de cada fase suma dos veces la fase recién cerrada
   (`runner_corpus.py:356-372`). No afectó el freno; va a r2.
3. E3: S19 da FAIL solo por los seis ids ausentes del catálogo JSON, discrepancia conocida
   y pre-registrada.
4. E3: `grafos.py` sumó el campo `requiere_registro_modulo` (opción B), autorizado por la
   autora el 28/09.
5. E5: la primera versión del cierre dejó veredictos por pregunta en
   `reports/tanda0/tabla_celdas_E5.json` entre las 18:48:34 y las 18:55:50 del 28/09, sin
   commit. Las exposiciones de veredictos anteriores a la adjudicación y las declaraciones
   sobre ellas están en la nota de episodios.
6. E5.c: la versión del cierre sellada en `f425657` levantaba antes de escribir, porque
   comparaba los CSV marcados con su render en blanco. Se corrigió en E5.c.3.
7. E5.c: la adjudicación la ejecutó una instancia de modelo (desvío, sección 0). La
   calibración de la autora encontró una inconsistencia, corregida en `8e0597c` en el
   criterio 3 de dos fichas, sin efecto en ningún agregado.
8. E6: el script de cita sellado y el parser de anclas no conocen los nombres de archivo
   de los cinco documentos nuevos. C5 se midió con extensiones declaradas, sin editar los
   sellados (secciones 5 y 3).
9. Higiene para r2: rutas absolutas en los reportes de ensamblado y en el campo `db` de
   los resúmenes de las corridas Neo4j.

## 10. Posición sobre la ventana del §7 (A8)

Propuesta; la decisión es de la autora.

- A8 abre la ventana única solo ante una falla de esquema que el principio de gobierno
  del §1 obligue a retirar, es decir, una falsedad en campo estructurado en material
  fresco. Toda otra falla, de pipeline, catálogo o índice, va a su destino de siempre.
- En 2a no encuentro una falla de esquema de ese tipo:
  - las cinco incorrectas de (12) son de capa `E1-prompt` (4) y `catálogo` (1), y van a
    r2 y al backlog (BKL-0032 a BKL-0036);
  - la observación (10) debajo de la banda y los 982 rechazos por firma son omisión, que
    el §1 acepta con residuo declarado;
  - el control de las tres `aplica_a` es vacuo en esta tanda.
- La ampliación del rango de `condicion_de` no es un retiro. Si cabe en la ventana es
  parte de la decisión abierta sobre la matriz, que la autora toma con los mentores (plan,
  fila B6.0 fase 2a).
- Posición propuesta: la tanda 0 se publica como validación de diseño; la ventana del §7
  sigue intacta para la tanda 1, salvo que la decisión sobre la matriz la use; los cinco
  documentos siguen fuera del conjunto que informó el esquema.

## 11. Lo que queda para 2b

- **Preguntas nuevas sobre los cinco:** entraron como C5 en 2a (sección 2); no quedan
  pendientes.
- **Evaluación sobre `ens_diez`:** es C5, corrida en 2a.
- **Lectura de (12):** hecha en 2b (`f51bb1f`), con su fila en `c671b52`, como lectura
  asistida revisada por la autora (desvío declarado en `aa7ee11`).
- **Pendiente de 2b:** la segunda emisión del paso 8 de A9 (reporte de 2b) con la fila de
  (12). No queda nada por correr.
