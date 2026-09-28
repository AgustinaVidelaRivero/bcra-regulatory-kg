# U-AUDIT-TIPOS-V3 — inventario de supuestos de vocabulario (solo lectura)

Fecha de ejecución: 28/09/2026. HEAD `2f0b174`. Referencia: `data/experiment/esq/code/prompt_congelado.py`
(9 tipos / 13 predicados; `DOMAIN_RANGE_CONGELADO` = `DOMAIN_RANGE_V2` de `prompt_esq3b_v2.py`).
Grafo de medición: `data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo/r1/kg.json`
(sha256 `eab2fdd0…64ef`, 6.378 nodos / 15.007 aristas; perfil `v3_b54`).

Nota de nomenclatura: el «esquema v2» de este inventario es el de producción de
`grafo_v2/code/schema.py` (6 tipos / 12 predicados). No confundir con `prompt_esq3b_v2.py`
(la «vuelta 2» de ESQ-3b, que ya tiene los 9 tipos y es la base del congelado).

Vocabulario congelado (impreso con `prompt_congelado`):
- Tipos: Comunicacion, TextoOrdenado, Operacion, Restriccion, Excepcion, Obligacion, Potestad, Condicion, Definicion.
- Predicados: establecida_en, referencia, modificada_por, aplica_a, regula, exceptua, exceptua_obligacion,
  prohibe, limita, ejecuta, requiere, condiciona, condicion_de.
- `condicion_de`: Condicion → {Excepcion, Obligacion, Restriccion} (rango SIN Operacion, Potestad, Definicion).
- `condiciona`: Obligacion → Operacion. `aplica_a`: {Excepcion, Obligacion, Operacion, Potestad, Restriccion} → Sujeto.
- `establecida_en`: {Condicion, Definicion, Excepcion, Obligacion, Operacion, Potestad, Restriccion} → TextoOrdenado.

## Método

- Barrido literal: `barrido.py` sobre 242 archivos .py de los directorios del mandato
  (lista en `py_files.txt`) → 729 líneas con literales de tipo o predicado en 73 archivos
  (`barrido_lineas.json`).
- Barrido de constantes con nombre (`TIPOS*`, `*TYPES`, `PRED*`, `FIRMAS*`, …) y de comparaciones
  no literales (`.type ==`, `startswith("Sujeto_")`, `split("_",1)[0]`).
- Lectura de cada archivo productivo con hits. Los selftests enumeran fixtures: quedan en
  `barrido_lineas.json`, no se tabulan.

## Tabla 1 — enumeraciones que EXCLUYEN algo del congelado

| # | ruta:línea | qué enumera / para qué | incluye Cond/Pot/Def y condicion_de | cableada / perfil | efecto medido sobre ens_desarrollo/r1 | capa |
|---|---|---|---|---|---|---|
| H1 | `reextraccion_v2/corpus_v2/r1_referencias.py:51` (aplicada en `:243`) | `TIPOS_ORIGEN` = Obligacion, Restriccion, Excepcion, Operacion: tipos cuyo texto se escanea buscando remisiones para crear aristas `referencia` | NO (excluye los 3) | cableada; `ensamblar_tanda0.py:131-143` redirige `INVENTARIO_TOS` pero NO `TIPOS_ORIGEN` (y su docstring `:25-41` enumera 4 puntos cableados sin este) | 2.090 nodos excluidos como origen (1.178 Cond + 381 Pot + 531 Def). Simulación en memoria (control 4.242/4.242 idéntico): +3.687 aristas `referencia` (Cond 2.535, Pot 616, Def 536) desde 343 nodos (230/56/57); 426 nodos con remisión detectada, 606 menciones, 119 irresolubles. 0 aristas perdidas. | ensamblado r1 (referencias B1.3) |
| H2 | `reextraccion_v2/e2_reduce/e2_lib.py:122` (copia textual de `grafo_v2/code/assemble_v3.py:127`; `assemble.py:105` igual) | `entity_slug_v3`: Restriccion/Obligacion/Excepcion se deduplican por `descripcion`; el resto (incluye los 3 nuevos) por `label` | NO (los 3 caen a la rama por label, como Operacion) | cableada; el selftest de E2 exige que la copia sea idéntica a `assemble_v3.py` | Conflictos de properties en E4 (`r1/e4_conflictos.json`, `reales_por_tipo_property`): `Condicion.descripcion` 27 en 19 nodos, `Definicion.descripcion` 13 en 10 nodos, `Potestad.descripcion` 3 en 3 nodos, `Definicion.termino` 8. Primera escritura gana: la variante descartada no queda en el nodo. | E2 (ensamblado por TO) |
| H3 | `data/experiment/neo4j/indices.py:78` | `CAMPOS_FULLTEXT` = label, descripcion, description, id_texto (enumera PROPIEDADES, no tipos) | no indexa `termino`, propiedad propia de Definicion | cableada | 111 de 531 Definiciones tienen algún token de `termino` ausente de label+descripcion+id (medido por tokens, sin analyzer) | agente / búsqueda Neo4j fulltext |
| H4 | `reextraccion_v2/corpus_v2/r1_referencias.py:52` | `PROPS_TEXTO` (descripcion, condicion, alcance, umbral, plazo, detalle): texto escaneado | no incluye `termino` | cableada | 4 Definiciones con patrón de remisión en `termino`; efecto sujeto a H1 (hoy Definicion no es origen) | ensamblado r1 |
| H5 | `evaluacion/verificador.py:440-466` | inyecta en el prompt del verificador diagnóstico el esquema de `run_3_ppf_core/code/schema.py` con assert 7 tipos / 12 predicados | NO | cableada (cluster sellado) | no aplica a la tanda 0: no lo invocan `tanda0/code` ni `ev2_tanda0/code` (grep); si se usara sobre un grafo gen 3 describiría un esquema sin los 3 tipos | evaluación (verificador) |
| H6 | `grafo_v2/code/schema.py:24-39, 41-69, 167-180` | `ENTITY_TYPES` (6), `PREDICATES` (12), `DOMAIN_RANGE` v2 | NO | cableada, pero es solo el DEFAULT de `validador_e1.py:112-118`, `e2_lib.py:258-262` y `ratchet_e3.py:246-280` cuando el perfil no trae esquema | 0 en la tanda 0: la validación usó el esquema congelado (los 982 rechazos se reproducen con `firma_valida` congelada; el kg contiene 1.178/381/531 nodos de los tipos nuevos) | E1/E3/E2 (default dev) |
| H7 | `scripts/shapes_validator.py:96-118, 476` | perfil v0: `RELACIONES_12`, `FIRMAS` (con EntidadFinanciera), `UNIDADES_REGULATORIAS`, default de S11 | NO | v0 cableado; `--perfil congelado` (`:128`, `:594-660`, `:937-957`) lee `prompt_congelado.py` → parametrizado | 0 con `--perfil congelado`. Sin perfil, todo grafo gen 3 falla S1/S3 por construcción | validación (shapes) |
| H8 | `grafo_v2/code/shapes_v2.py:36-63` | `RELACIONES_16`, `FIRMAS_V2`, `UNIDADES_REGULATORIAS` | NO | cableada | no está en la cadena de la tanda 0 | validación legado |
| H9 | `scripts/metricas_intrinsecas.py:386` | `A2.ENTITY_TYPES` (v2) en `mapear_menciones` | NO | cableada | 0 en `--gen3`: `mapear_menciones` solo se llama en la ruta gen 2 (`:1086`, `:1110`); en gen 3 M3 es no computable | métricas intrínsecas |
| H10 | `grafo_v2/code/visualize.py:20-27, 68` | `TYPE_COLOR` (v1, con EntidadFinanciera) | NO | cableada | los 3 tipos caen al color por defecto `#7f8c8d` (`:51`) | visualización legado |
| H11 | `esq/code/descubrimiento_cal.py:53-57`, `disparadores_esq2.py:87`, `comun_control_esq.py:102`, `prompt_esq3b.py:111-160` | listas históricas de diseño ESQ (TIPOS_6/PREDICADOS_12, TIPOS_NORMATIVOS, FIRMAS_B, RETOCADO 9/14 con `exceptua_operacion`) | NO / parcial | cableadas, instrumentos cerrados | fuera del pipeline productivo | diseño ESQ |

## Tabla 2 — enumeraciones revisadas SIN exclusión del congelado

| ruta:línea | qué enumera | por qué no excluye |
|---|---|---|
| `reextraccion_v2/e1_extractor/perfil_e1.py:146-180` | `EsquemaValidacion` del perfil `v3_b54` | toma tipos, predicados, firmas y enum de `prompt_congelado` |
| `reextraccion_v2/e1_extractor/validador_e1.py:112-118, 212, 294-326` | vocabulario por perfil; enum de Obligacion.tipo; sujeto_predicates | parametrizado por perfil |
| `reextraccion_v2/e2_reduce/e2_lib.py:80` | `TIPOS_NO_CONTENIDO` = TextoOrdenado, Sujeto | lista negativa: los 3 nuevos cuentan como contenido |
| `reextraccion_v2/e2_reduce/e2_lib.py:258-262, 328, 426, 439-441, 476` | tipos, predicados, firma | parametrizado por perfil |
| `reextraccion_v2/e3_verificador/ratchet_e3.py:246-280` | re-validación de reintentos | usa `perfil.esquema` |
| `reextraccion_v2/e3_verificador/comun_e3.py:165` | ("aplica_a","ejecuta") | igual a `SUJETO_PREDICATES` congelado |
| `reextraccion_v2/corpus_v2/r1_referencias.py:212` | destino excluye Sujeto, Comunicacion | lista negativa: los 3 nuevos SÍ son destino (p. ej. Operacion→Condicion 367) |
| `reextraccion_v2/corpus_v2/r1_e4.py:134, 220, 265, 275` | Sujeto propuesto, TextoOrdenado | casos específicos, no vocabulario |
| `reextraccion_v2/corpus_v2/r1_e5_esqueleto.py:32, 67, 96`; `tanda0/code/ensamblar_tanda0.py:244, 272` | Sujeto / padre_sugerido | esqueleto solo Sujeto |
| `reextraccion_v2/corpus_v2/r1_invariantes.py:101` | Sujeto del catálogo | guarda cross-TO, no por tipo de contenido |
| `grafo_v2/code/schema.py:76-81` | `RELACIONES_ESQUELETO` | Sujeto→Sujeto, fuera del vocabulario del LLM |
| `reextraccion_v2/corpus_v2/ensamblar_corpus.py:273` | Excepcion en tests de respuesta conocida | el manifiesto de la tanda 0 declara `tests_respuesta_conocida: null` |
| `scripts/regression_kg.py:512-612, 722-725, 1051-1253` | búsquedas puntuales por tipo en checks C1–C7/E4 (`:547` admite EntidadFinanciera como fallback) | no enumera vocabulario |
| `scripts/muestra_aristas_obs12.py:111` | excluye `relation == "referencia"` | universo A4.1 declarado, no por tipo |
| `data/experiment/neo4j/cargar_kg.py:142-149` | label por `n.type` | genérico; verificado en Neo4j |
| `data/experiment/neo4j/neo4j_index.py` (3 tools) | — | Cypher sin condición sobre type ni relation |
| `evaluacion/harness.py:61-91, 110-124, 130-237, 240-286` | SYSTEM_PROMPT, `_short_props`, GraphIndex, TOOLS | sin lista de tipos; `_short_props` usa description/descripcion (los 3 tipos tienen descripcion en 100 %) |
| `evaluacion/loader.py:180-239` | `_merge_nodes` | genérico por id |
| `tanda0/code/comun_tanda0.py`, `ev2_corrida/code/comun_ev2.py:201-211`, `ev2_r1/code/comun_r1.py:117-127` | vista runtime | genérica |
| `b54_catalogo_v3/code/prompt_v3_b54.py`, `comparar_pareada_b54.py:56-61` | prefijo v3; sujeto predicates | importa el congelado |
| `app/` | NO ENCONTRADO | ninguna enumeración de tipos o predicados |
| `ev2_tanda0/code/` (6 archivos) | NO ENCONTRADO | sin referencias a type ni relation |

## Punto 3 — las 35 Condiciones aisladas (`p3_resumen.json`, `p3_filas.json`, `p3b_cruce.json`)

- 35 = aisladas por tipo en el kg (Condicion 35, Operacion 30, Definicion 13, Sujeto 12, Comunicacion 3, Obligacion 1). Neo4j da los mismos conteos.
- Traza de cada nodo a su entidad del registro final (`salida_dirigida/<to>/extracciones_finales_<to>.jsonl`):
  - 33: todas sus relaciones fueron rechazadas por `firma_invalida` con la matriz congelada (34 rechazos: `Condicion --condicion_de--> Operacion` 20, `--> Definicion` 9, `--> Potestad` 3; `Condicion --condiciona--> Operacion` 1; `Excepcion --exceptua_obligacion--> Condicion` 1; uno de los nodos tiene dos).
  - 2: el extractor no emitió ninguna relación para la Condicion (`cla::10.4`; `ext::3.5.3.4`, final tras reintento).
  - En ningún caso el extractor emitió `establecida_en` (31 verificadas en el crudo de E1, las 4 restantes en la validación final tras reintento).
- La causa NO es una lista del punto 1: es la matriz congelada (rango de `condicion_de`) más la omisión de `establecida_en` por el extractor. Con H1 corregido, 9 de las 35 recibirían alguna `referencia` (8 salientes, 1 entrante); 26 seguirían aisladas.

## Punto 4 — rechazos `firma_invalida` de E1 (`p4_resumen.json`, `p4_filas.json`)

- 2.437 registros E1 en 10 TOs; 982 rechazos (870 en los 5 TOs de desarrollo). 65 pares distintos; suma por par = 982.
- Los 3 chunks re-extraídos (cap::3.1.14.1, 4.2.1.2, 4.3.3.1) tienen su primer registro con error de API y 0 rechazos: sin doble conteo.
- Revalidación desde el crudo: 982/982 con `tool_input_crudo` presente, `relations[i]` del detalle presente e igual al `elemento`, tipos resueltos desde las entidades crudas iguales a los del detalle, y firma recomputada con `prompt_congelado.firma_valida` = inválida.
- Estado E3 del registro que entró al grafo: completo_ok_directo 460, aceptado_con_residuales 388, aceptado_tras_reintento 110, cola_humana 14, cola_humana_veredicto_inutilizable 10. En los 110 con reintento, el grafo se construyó con la salida del reintento, cuyo crudo NO está en el jsonl: vive en `e3_verificador/cache/e1_reintentos.db` (namespace `…p54a111e2175f`, 255 filas; leído con `immutable=1`).
- Nota: la validación final (`extracciones_finales_*.jsonl`, lo que ensambla E2) registra 1.039 `firma_invalida` en 10 TOs; es otra población (post-reintento) y no se desglosa acá.

## Punto 5 — agente

GraphAgent (`harness.py`) y GraphAgentNeo4j (`agente_neo4j.py` + `neo4j_index.py`): ninguna tool filtra ni trata distinto por tipo o predicado; el prompt del sistema no enumera tipos; TOOLS no tiene enum de tipo. Neo4j (`KG_Tanda0_Desarrollo_r1`, solo MATCH/RETURN): 1.178 Condicion / 531 Definicion / 381 Potestad, todas con su label de tipo y con `descripcion`; 448 `condicion_de`. Única diferencia por tipo: H3 (`termino` fuera del índice fulltext).
