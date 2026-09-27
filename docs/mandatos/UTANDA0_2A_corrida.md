FIRMADO por la autora — 2026-09-27 (fase 2a de la tanda 0; ok escrito de la autora para correr)

MANDATO — U-TANDA0-2A: FASE 2a DE LA TANDA 0, CORRIDA Y LECTURA.
Repo bcra-regulatory-kg. Leé CLAUDE.md antes de empezar. Unidad en SEIS
ETAPAS con FRENO obligatorio al final de cada una: al frenar, reporte corto
(no más de 40 líneas) y espera de la revisión y del «seguí» escrito de la
autora; ninguna etapa arranca sin él. Tope de gasto de la unidad: USD 100
(decisión 7); estimación A7 para 2a: USD 69,18. Costo de API 0 en E1, E3,
E4 y E6; gasto solo en E2 y E5, cada uno con su tope parcial declarado
abajo.

CONTEXTO. Pre-registro docs/preregistro_tanda0.md (sellado c80b03f) con sus
dos enmiendas: observación (12) (8e13be3) y partición 2a/2b
(docs/enmienda_preregistro_tanda0_2026-09-27_fase2a2b.md, firmada;
COMMIT: a551c57 · SHA256: 2b19460f734b1913b1cc2d0b248236668ecc74a45c06afde79a4830c5e91c97a — la autora completa estos dos huecos al
despachar). Este mandato ejecuta la fase 2a tal como la enmienda la define.
Leé los tres documentos completos, la fila B6.0 del plan con sus gates
técnicos, docs/laudo_esquema_congelado.md §1 y §7, y los módulos que cada
etapa nombra, antes de escribir una línea.

DECISIONES YA TOMADAS (A1 a A8 y las dos enmiendas). No se re-deciden.
1. Conjunto de la tanda 0: ctacte, lingob, polcre, pagjub, docvig (671
   unidades, 172 páginas, A2.2); desarrollo: pro, cla, ric, cap, ext
   (1.763 unidades, A3.1). Diez TOs en total, 2.434 unidades.
2. Pipeline: E0 a E5 con el mismo código que produjo r1, perfil v3_b54,
   esquema congelado (1be8304e3d77 / e69feaaa…), sin anotación manual
   (A1). E1 sin temperatura fijada, como corrió r1 (decisión 7); no se
   edita cliente_e1.py ni nada del pipeline.
3. Una sola extracción y tres ensamblados determinísticos (A3.5):
   desarrollo solo (para C3 y C4), tanda 0 sola (observación (10) y sorteo
   de (12)), los diez (observación (11); C5 o 2b).
4. Celdas: C2 = r1 con Neo4j fulltext; C3 = desarrollo re-extraído con
   GraphIndex en memoria; C4 = desarrollo re-extraído con Neo4j fulltext;
   C1 se agrega desde 774acac (A3.1). C5, condicional (enmienda 2a/2b §2.3):
   las preguntas nuevas sobre los cinco, si están selladas por commit antes
   de E5, sobre ens_diez/r1/kg.json con GraphIndex en memoria; si no, 2b.
   Protocolo de C1 completo en cada celda: corrida base de las preguntas en
   el orden sellado (para C2 a C4, las 40 de EV2 en el orden de C1; para
   C5, el orden que su sellado fije), juez v1 fd446f8e… N=3 voto modal,
   re-corridas de encadenamiento del §7 del pre-registro de r1 con su juez,
   ids opacos con sal propia por celda. Una corrida por celda, sin repetir
   (principio 7).
5. Instrumentos en verde y sus commits: shapes con perfil congelado f4c8e93
   (scripts/shapes_validator.py --perfil congelado); regression suite
   2012832 (scripts/regression_kg.py, fixture 696f3f94…); intrínsecas
   --gen3 e indicadores de cita parametrizados a48d229; sorteo de (12)
   d3f7d2e (scripts/muestra_aristas_obs12.py); runner de EV2 sobre
   GraphAgentNeo4j 271f324 (data/experiment/ev2_tanda0/code/runner_ev2_neo4j.py).
   Instrumentos PENDIENTES que esta unidad cierra: 1 (cableado de r1), 5
   (registro y carga en Neo4j), 7 (manifiesto), 9 (registro en memoria de
   los grafos nuevos para C3 y C5), 10 (juez y §7 parametrizados), todos
   USD 0 y cada uno probado en seco antes de la etapa que lo usa.
6. Regla de la suite en la fase 2 (fila B2.1 del plan): sobre los grafos de
   la tanda 0 corre sin --esperado la primera vez y su salida se registra
   como línea de base observada.
7. Observaciones (10) y (11) y vigilancias (1) a (9) se leen contra las
   líneas de base de A4, sin umbral (decisión 6). Observación (12): sorteo
   con semilla 20260927 sobre el ensamblado de la tanda 0 sola, sellado por
   commit antes de E5; la lectura queda en 2b. Vigilancia del hallazgo S20:
   el contador tipo_obligacion_normalizados de E1 en el chunk
   ext::10.4.3.1.
8. Registro de modelos por llamada en cada etapa que gasta: id devuelto por
   la API, temperatura (fijada o «default del proveedor»), vía, tomados de
   las dbs de caché, nunca de memoria (A6, regla C1.9). Se acumula en
   reports/tanda0/registro_modelos_2a.json.
9. Toda salida que el plan vaya a citar se escribe en el repo, en las rutas
   de abajo; el scratchpad solo para copias de trabajo y checkpoints.
   Ningún módulo sellado se edita: extensiones por módulo nuevo bajo
   data/experiment/tanda0/code/ (patrón comun_r1), con los sha de los
   sellados verificados al inicio y al cierre de cada etapa.
10. Rutas: manifiestos en data/experiment/reextraccion_v2/manifiestos/
   (tanda0_10tos.json para extracción; tanda0_ens_desarrollo.json,
   tanda0_ens_cinco.json, tanda0_ens_diez.json para los ensamblados, con
   las mismas entradas y rutas); E0 en
   data/experiment/reextraccion_v2/e0_chunking/salida_tanda0/; E1 a E3 en
   data/experiment/reextraccion_v2/corpus_tanda0/salida/ (--salida de
   runner_corpus.py); ensamblados en
   data/experiment/reextraccion_v2/corpus_tanda0/ens_{desarrollo,cinco,diez}/
   con kg.json (E5) y r1/kg.json (tras el cableado de r1); EV2 en
   data/experiment/ev2_tanda0/{trazas,juez_out,cache}/; reportes en
   reports/tanda0/. Las dbs de caché no se versionan: la autora agrega los
   .gitignore al commitear, como en 271f324.

TAREA, EN ETAPAS.

E1 — Manifiesto y cableado de r1, en seco sobre desarrollo, USD 0 (gates 7
y 1).
a. Manifiesto tanda0_10tos.json con el formato de desarrollo_5tos.json
   (manifiesto_corpus.py:55-119): los diez TOs con id, archivo, pdf bajo
   data/experiment/subset/ o el directorio donde estén los cinco nuevos
   (declaralo), sha256_pdf, rol_alcance según el catálogo v3 (rol_alcance
   null para docvig, A2.4; manifiesto_corpus.py:151-152 lo valida),
   perfil_e1: "v3_b54", orden_corrida con desarrollo primero en el orden
   de r1 y después los cinco nuevos por unidades descendentes,
   rutas.e0_salida = la de E0 de esta tanda, oraculo con el mapa de
   territorio para los cinco de desarrollo y el modo sin oráculo que
   manifiesto_corpus.py admita para los nuevos (mostrá la línea que lo
   admite), limites con tope_global_usd 47,31 más el margen que el cargador
   exija, estimado_usd por TO derivado de A7.3 por unidades,
   tests_respuesta_conocida null, sellos vacíos hasta E3. Tres manifiestos
   de ensamblado derivados con las mismas entradas.
   manifiesto_corpus.cargar debe aceptar los cuatro; pegá la salida.
b. E0 sobre los diez con correr_e0.py --manifiesto tanda0_10tos.json
   --salida salida_tanda0: los cinco de desarrollo deben salir
   byte-idénticos a salida_enm01 (cmp de chunks_<to>.json y
   estructura_<to>.json); los cinco nuevos con 671 unidades en total y los
   conteos de A2.2 por TO; health-check de E0 (B5.2) sobre los cinco nuevos
   con el resultado de A2.4 (tres sanos, lingob y pagjub con cid). Si E0 no
   es byte-idéntico sobre desarrollo, FRENO: el pipeline no es el de r1.
c. Cableado de r1: módulo data/experiment/tanda0/code/ensamblar_tanda0.py
   que, para un manifiesto de ensamblado, corre ensamblar_corpus.ensamblar
   con --salida propia y esqueleto v3 por perfil, y después
   ensamblar_r1.correr con SALIDA y SALIDA_R1 redirigidas en memoria
   (r1_comun.py:27-28; precedente del gate 6, custodia por re-ensamblado
   sin editar) hasta hasta="final", salteando con nota los pasos de r1 que
   leen artefactos propios de r1 (muestra inspeccionada y tests,
   ensamblar_r1.py:213-222) cuando el manifiesto declara
   tests_respuesta_conocida null. Prueba en seco: sobre el manifiesto de
   desarrollo actual (desarrollo_5tos.json, perfil produccion_dev) el
   módulo debe reproducir salida/kg.json (8e2eadee…) y salida_r1/kg.json
   (0226e947…) byte a byte en un directorio del scratchpad. Sin esa
   reproducción, FRENO.
FRENO E1: reporte con los cuatro manifiestos y sus sha, los cmp de E0, el
health-check, la reproducción byte a byte de 8e2eadee… y 0226e947…, y git
status --short. Commit de la autora de manifiestos, E0 y módulo antes de
E2.

E2 — Extracción E1 a E3 de los diez TOs. Tope parcial USD 60 (A7.3 da
47,31; margen declarado).
a. runner_corpus.py --manifiesto tanda0_10tos.json --salida
   corpus_tanda0/salida --autorizado-tope <tope> (gating propio del runner,
   runner_corpus.py:17-21,48: tope global duro y freno por proyección al
   cierre de cada TO). Precios del día verificados y pegados antes de
   correr; si la proyección con los volúmenes reales de E0 supera el tope
   parcial, FRENO y preguntar antes de gastar (A7.4).
b. Al cierre: gasto real por TO y por fase desde las dbs; resumen_e1 y
   resumen_e3; contadores de E1 en modo v3 (tipo_obligacion_normalizados,
   tipo_obligacion_requisito_de_estructura) por TO y en ext::10.4.3.1
   (decisión 7); registro de modelos de E1 y E3 por llamada desde las dbs
   (id de la API, temperatura «default del proveedor» para E1, vía API).
FRENO E2: reporte con gasto real contra estimado, contadores, incidencias,
registro de modelos. Commit de la autora de las salidas de E1 a E3 antes
de E3.

E3 — Tres ensamblados, registro y carga en Neo4j, gate de release. USD 0.
a. Los tres ensamblados con el módulo de E1c y sus manifiestos:
   ens_desarrollo, ens_cinco, ens_diez, cada uno con kg.json y r1/kg.json,
   sha256 y conteos de nodos y aristas. Doble corrida byte-idéntica de cada
   uno.
b. FRENO interno: commit de la autora de los tres ensamblados (el registro
   de Neo4j exige commit_sellado).
c. Gate 5: entradas nuevas en data/experiment/neo4j/grafos.py (edición de
   registro, no del cuarteto) para ens_desarrollo/r1/kg.json y
   ens_diez/r1/kg.json con nombre_canonico, label, path, sha256,
   commit_sellado, n_nodos, n_aristas, vista_runtime e indice_fulltext
   propio; carga con cargar_kg.py e índice con indices.py (CAMPOS_FULLTEXT
   y analizador sin cambios, A3.2); test_equivalencia.py sobre el grafo
   nuevo si su interfaz lo admite (mostralo), o la verificación que
   indices.py ofrezca. KG_Meta.kg_sha256 en Neo4j igual al sha del
   archivo.
d. Gate de release (A9 paso 5) sobre los tres r1/kg.json:
   shapes_validator.py --perfil congelado --excepciones
   esquema_v3_clases.json --out reports/tanda0/shapes_<ens>.md (S15 debe
   dar PASS sobre grafos con perfil v3_b54; si falla, el release no sale:
   FRENO); ausencia de las tres aplica_a adjudicadas como falsedad (fila
   del plan que las lista); regression_kg.py sin --esperado sobre cada
   uno, generación 3, catálogo v3, política flaggeada, --out
   reports/tanda0/regression_<ens>.md (línea de base observada, decisión
   6); metricas_intrinsecas.py --gen3 sobre cada uno con --reensamblar-r1
   si el módulo de E1c lo permite y si no por sha256 declarado, salida en
   data/experiment/metricas_intrinsecas/tanda0_<ens>.json; contador de
   vocabulario retirado = 0.
FRENO E3: reporte con sha y conteos de los tres, resultado de cada
instrumento del gate, entradas de grafos.py y verificación de carga.
Commit de la autora antes de E4.

E4 — Sorteo de la observación (12). USD 0.
scripts/muestra_aristas_obs12.py --kg ens_cinco/r1/kg.json --semilla
20260927 --out reports/tanda0/obs12_sorteo/ --e0 salida_tanda0 (universo
de A4.1 sobre la tanda 0 sola); doble corrida byte-idéntica del JSON;
textos_no_encontrados = 0. La autora NO lee el .md: la lectura es de 2b.
FRENO E4: reporte con n, índices y sha. Commit de la autora del sorteo
antes de E5 (enmienda (12) §2.3). En este FRENO la autora declara además si
las preguntas nuevas sobre los cinco están selladas por commit (ruta, sha,
commit, cantidad, clasificación con la regla v2): si sí, C5 entra en E5 y
el tope parcial de E5 pasa a USD 40; si no, C5 queda en 2b y el tope
parcial de E5 es USD 30.

E5 — Celdas C2, C3 y C4, y C5 si corresponde, con juez. Tope parcial
USD 30 (A7.3 da 21,87) o USD 40 con C5.
a. Instrumentos 9 y 10 antes de gastar: comun_tanda0.py (registro en
   memoria de ens_desarrollo/r1/kg.json y, si hay C5, de ens_diez/r1/kg.json
   en GRAFOS de comun_ev2 con la vista runtime de provenance mapeada,
   patrón comun_r1.py:106-158) y juez_tanda0.py / enc_tanda0.py (juez v1 y
   §7 con trazas, labels, dbs y sales por celda, reutilizando juez_r1.py y
   enc_r1.py por import). Selftest en seco de los tres con cliente falso,
   sin API; pegá la salida.
b. C2: runner_ev2_neo4j.py --grafo KG_Reextraido_r1 --modo fulltext --label
   ev2_c2_r1_neo4j --autorizado-fase-b --tope <tope>; C3:
   runner_ev2.correr_grafo sobre el grafo registrado en memoria, label
   ev2_c3_dev_mem; C4: runner_ev2_neo4j.py --grafo <clave nueva> --modo
   fulltext --label ev2_c4_dev_neo4j; C5, si corresponde:
   runner_ev2.correr_grafo sobre ens_diez/r1/kg.json registrado en memoria,
   label ev2_c5_diez_mem, con --casos apuntando al JSON sellado de las
   preguntas nuevas y su orden. Cada celda: sus trazas (40 en C2 a C4; las
   selladas en C5), 0 hits de caché exigidos (db nueva), freno por
   proyección, luego juez N=3 y §7 con su juez. Precios del día verificados
   antes de cada corrida.
c. Registro de modelos por llamada de agente y juez desde las dbs;
   meta.model_segun_api en las trazas de C2 y C4.
FRENO E5: reporte con la tabla de las celdas (correcto / parcial /
incorrecto, con N, intervalos y declaración de si el n alcanza; C5 en tabla
aparte, sin cruzar con C1 a C4), gasto real por celda contra 7,29,
incidencias. Commit de la autora de trazas y salidas del juez antes de E6.

E6 — Lectura de observaciones y vigilancias, reporte. USD 0.
a. Observación (10): aristas de extracción por unidad con el comando de
   A4.1 sobre ens_desarrollo/r1/kg.json (1.763) y ens_cinco/r1/kg.json
   (671), contra las bandas de A4.1. Observación (11): comando de A4.2
   sobre el reporte de ensamblado de ens_diez: cuántas de las 106
   remisiones «fuera del inventario» pasan a resolverse y aristas_cross_to
   contra 188. Vigilancias (1) a (9) con los instrumentos de A4.3 y la (5)
   del hallazgo S20 con el contador de E1.
b. Indicadores de cita (ucita2_indicadores.py con --trazas, --tandas, --e0,
   --manifiesto de esta tanda) sobre C2, C3, C4 y C5 si corrió; atribución
   A0.2 sobre C3 y C4 con la regla sellada.
c. Reporte reports/tanda0/reporte_fase2a.md como validación de diseño (A9
   paso 8): tabla de las cuatro celdas con C1 agregada desde 774acac, y C5
   aparte si corrió; una fila por predicción de A4 (predicho / observado /
   veredicto), sin umbral; costo real desde las dbs contra 69,18; registro
   de modelos completo; incidencias; posición sobre la ventana del §7 por
   la vía de A8; y la lista de lo que queda para 2b (preguntas nuevas si
   no entraron como C5, lectura de (12), evaluación sobre ens_diez).
FRENO E6, final. La autora revisa, commitea y decide la posición sobre A8.

REQUISITOS TRANSVERSALES (CLAUDE.md §4 a–j), en todas las etapas.
- Escrituras: solo las rutas de la decisión 10, grafos.py (entradas
  nuevas, E3c), los módulos nuevos bajo data/experiment/tanda0/code/ y
  data/experiment/ev2_tanda0/code/, y tu scratchpad. Ningún sellado de
  CLAUDE.md §3 ni del cuarteto se edita; corpus_v2/salida/ y salida_r1/ son
  solo lectura. No commitees. Costo de API solo en E2 y E5 con sus topes;
  el gasto real se lee de las dbs.
- PYTHONDONTWRITEBYTECODE=1 en todo Python; .venv/bin/python salvo
  ucita2_indicadores.py, que corre con python3 3.12 (nota de intérprete
  del gate 6). Ningún __pycache__ ni .pyc nuevo.
- Toda afirmación con path:línea o comando; conteos recomputados antes de
  escribirse (§4.i); lo que no esté en un artefacto es NO ENCONTRADO. Los
  mentores solo por rol; cero nombres propios.
- Paquete de revisión por etapa revision_TANDA0_2A_E<n>/ con manifest.txt;
  checkpoint checkpoint_TANDA0_2A.md en el scratchpad actualizado al cierre
  de cada etapa y antes de cualquier compactación, con etapa, piezas
  hechas, gasto acumulado y rutas.

CRITERIO DE ACEPTACIÓN por etapa: el reporte corto con las salidas
pedidas, git status --short con solo las rutas de la etapa como nuevas o
modificadas, sha de los sellados iguales al inicio y al cierre, grep de
convenciones pegado. Criterio final: los seis frenos cerrados con «seguí»
de la autora, gasto total ≤ USD 100, el reporte de 2a en el repo.

FRENO al final de cada etapa; FRENO final tras E6.
