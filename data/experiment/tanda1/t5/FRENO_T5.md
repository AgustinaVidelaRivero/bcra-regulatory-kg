# FRENO T5 — tanda 1 de B6.1: el reporte de cierre (USD 0, sin API, sin commit)

Rigen el pre-registro firmado (`docs/preregistro_tanda1.md`, firma en `95b18217`, con su nota al pie en `ca5b39fd`): el §3, «Al
cerrar»; el §5.5; el §5.6, y el §6 donde el reporte lo cita. HEAD `bd60f6c0`. El reporte es `data/experiment/tanda1/t5/reporte_tanda1.md`.

**Resultado:**
- **El costo** (sección 2): real USD 70,991032 contra el estimado de 69,659193 (razón 1,0191). E1, 35,529339 contra 33,534993 (1,0595); E3, con los reintentos adentro, 35,461693 contra 36,124200 (0,9817).
- **Los ids de modelo** (sección 3): E1 claude-haiku-4-5-20251001; E3 claude-sonnet-5; iguales a lo esperado y a lo que dio el freno por modelo de T2: True y True.
- **El catálogo** (sección 4): no crece en la tanda 1, declarado como desvío del §5.5; una sola versión.
- **Los hallazgos** (sección 5): 19 (incorrecta de una lectura de T4, 10; la cola, con la regla del 25 % disparada, 1; regresión declarada de T3, 2; vigilancia fuera de su línea de base, 3; fila del tablero que no cumple su meta, 3), con 11 propuestas del backlog en `t5/propuestas_backlog_t5.jsonl`.
- **El selftest de claves** (sección 6), tal cual y dos veces sobre una copia: OK, con los dos JSON iguales.
- **Las dos corridas de `cifras_t5.py`** dan los mismos bytes: True (sección 9).
- **El `NO_ABRIR_conteos_t5.json`:** `13e65dcc24c3057a5a815ea09d3c9101d7ae229f8050d0b8c7f8a2658badea7f`. `unidades_a_la_vista_T5.json`: no hizo falta (sección 8).
- Toda cifra sale por script de sus archivos. Las tablas que copio de una salida van tal cual; mis aclaraciones van fuera de las tablas.
- Nada commiteado y ningún mensaje de commit preparado: los commits son de la autora y quedan PENDIENTES.

## 1. Paso 0 (18/10/2026, 18:19)

```
$ pwd
$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg
$ git log -1 --format='%h %s'
bd60f6c0 Registro de decisiones y mandato del cableado: el cableado del alcance corre en paralelo con la primera tanda, sobre una copia
$ git log --format=%s -4
Registro de decisiones y mandato del cableado: el cableado del alcance corre en paralelo con la primera tanda, sobre una copia
Primera tanda: las tasas, la atencion y el freno de la cuarta etapa, segundo tramo, sin ampliacion
Pre-registro de la tanda final: version para firmar, con sus scripts, sus pruebas y los huecos que se completan por momento
Mandato firmado: la correccion de la procedencia de los tramos heredados, y el registro de decisiones con la regla de las dudosas
$ git status --porcelain --untracked-files=no | wc -l
       0
$ ls -d data/experiment/tanda1/t5
ls: data/experiment/tanda1/t5: No such file or directory
$ pgrep -fl "runner_corpus.py|ensamblar_tanda0.py|regression_kg.py|shapes_validator.py"
(rc=1)
$ git diff --name-status b4c42ebd HEAD | wc -l
      25
$ python3 -B data/experiment/tanda1/t2/foto_repo_tanda1_t2.py . <scratchpad>/t5/foto_repo_antes_T5_cruda.json
2026-10-18 18:19:21 2026-10-18 18:19:32 52586 entradas
$ python3 -B data/experiment/tanda1/t2/foto_repo_tanda1_t2.py --comparar <foto de 17:23:48 del segundo tramo> <esta foto>
antes 52572, después 52586; nuevos 14, borrados 0, cambiados 2
$ python3 -I -B <scratchpad>/t5/verif_paso0_commits_t5.py . <esa comparación> b4c42ebd
nuevos o cambiados en la foto, sin .DS_Store: 16; fuera de los commits: 0 []
archivos de los commits y de la foto comparados con HEAD: 25; distintos: 0 []
borrados en la foto: 0
.DS_Store nuevos o cambiados: 0
$ python3 -B data/experiment/tanda1/t2/foto_repo_tanda1_t2.py --comparar <foto final del segundo tramo, 17:24:35> <esta foto>
antes 52573, después 52586; nuevos 13, borrados 0, cambiados 2
$ python3 -I -B <scratchpad>/t5/verif_paso0_commits_t5.py . <esa comparación> b4c42ebd
nuevos o cambiados en la foto, sin .DS_Store: 15; fuera de los commits: 0 []
archivos de los commits y de la foto comparados con HEAD: 25; distintos: 0 []
borrados en la foto: 0
.DS_Store nuevos o cambiados: 0
$ find . -path ./.git -prune -o \( -name '*.pyc' -o -name '__pycache__' \) -print | sort | wc -l
   11236
```

- **El orden de los cuatro commits,** de abajo hacia arriba, es el del mandato: el mandato firmado de la corrección de la procedencia
  (`6a071bf3`), el pre-registro de la tanda final para firmar (`5289b02f`), el segundo tramo de T4 (`d728e7b0`) y el del cableado (`bd60f6c0`).
- **Lo que trajeron los commits:** `git diff --name-only b4c42ebd HEAD` da 25 archivos, y los 25 son iguales a `git show HEAD:` byte a
  byte. La foto ve 16 como nuevos o cambiados contra la de las 17:23:48; los otros 9 son los que escribí en el segundo tramo de T4, que
  ya estaban en el disco con los mismos bytes. Nada se borró, nada cambió fuera de los commits y no hay ningún `.DS_Store` nuevo.
- **Qué foto es la de comparación:** el mandato nombra la del segundo tramo de 17:23:48 a 17:24:00, que es mi foto de después de escribir,
  anterior a su FRENO (`foto_repo_despues_T4t2_cruda.json`). Comparé también contra la final (`foto_repo_final_T4t2_cruda.json`, de
  17:24:35 a 17:24:48, con el FRENO): da 15 en lugar de 16, porque el FRENO del segundo tramo ya estaba en ella. Las dos van en el paquete,
  con `verif_paso0_commits_t5.py` y sus salidas.
- **`pgrep` salió vacío**, `t5/` no existía y los `.pyc` dan 11.236 líneas, la misma lista que al cierre del segundo tramo (`cmp` sin
  diferencias).

## 2. El costo por etapa y por TO, con la desviación

La sección 2 del reporte, tal cual:

De `t5/salidas/costo_t5.json`. El real es el `gasto_usd` de las 40 fases de estado_corpus.json, que el runner calcula con la fórmula de caching (decisión 2 de docs/decisiones_caching_extraccion.md; data/experiment/reextraccion_v2/e1_extractor/cliente_e1.py:328-331, e3_verificador/cliente_e3.py:194-197; precios en corpus_v2/runner_corpus.py:91-96); de cada fase se leen solo gasto_usd y resumen.n. E3 va como una sola cifra por TO, con los reintentos adentro. El estimado por TO es el del manifiesto 818a62cf… (repartido por caracteres de E0); el estimado por etapa es U × tarifa (E1 0,010135 y E3 0,010980) más las líneas de alcance en E1, repartidas por TO como en T1 (t1/t1_manifiesto.py:124-129).

| etapa | real USD | estimado con la tarifa | razón | estimado del manifiesto | razón |
|---|---:|---:|---:|---:|---:|
| E1 | 35,529339 | 33,534993 | 1,0595 | 33,575979 | 1,0582 |
| E3 (con los reintentos adentro) | 35,461693 | 36,124200 | 0,9817 | 36,083214 | 0,9828 |
| total | 70,991032 | 69,659193 | 1,0191 | 69,659193 | 1,0191 |

- **Contra el tope:** 70,991032 de 100,7291 (0,7048). `presupuesto_compartido.json` da 70,991031; la suma de las 40 fases menos ese valor, 0,000001.
- **Las líneas de alcance** en E1: USD 0,190843, repartidas por TO así: ri_gerc 0,002740, ri_pgn 0,003837, ri_rml 0,008404, nmcief 0,011109, ri_dcpc 0,013114, snp_tr 0,019558, ri_mmsef 0,023385, manori 0,026577, ri_ccna 0,028942, snp_cheq 0,053177 (en E1, por TO, `usd_agregados` de alcance_e1/a2/salidas/medicion_tanda1_a2.json (como T1)).
- **La desviación**, por etapa, por TO y total, va a: el re-presupuesto de la tanda final (docs/protocolo_entre_tandas.md:65-69).
- **La tarifa observada** (U = 3.290): E1 0,010799, E3 0,010779, juntas 0,021578, contra la de referencia 0,010135, 0,010980 y 0,021115. Es propuesta para el §5 de la tabla de reprocesamiento; T5 no la escribe en la tabla.
- **Para el pre-registro de la tanda final** (`para_el_preregistro_tanda_final`): «E1: real USD 35,5293, estimado USD 33,5350, razón 1,0595; E3: real USD 35,4617, estimado USD 36,1242, razón 0,9817; total: real USD 70,9910, estimado USD 69,6592, razón 1,0191».
- **Los pasos sin API, en 0:** E0 (T1 la generó con el código del gate, dentro del repo); la corrida en seco de T1 (clientes stub); E2 y el ensamblado de los cuatro grafos (T2 y T3); el gate, la suite, shapes, las intrínsecas y Neo4j (T3); lo contado sin leer (T3); los sorteos, el material y la lectura asistida (T4, primer tramo; lectura de la ejecutora, sin API); las tasas (T4, segundo tramo); este reporte (T5).

| TO | U | E1 real | E3 real | total real | estimado del manifiesto | razón | estimado con la tarifa | razón |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| ri_gerc | 15 | 0,198871 | 0,154028 | 0,352899 | 0,408570 | 0,8637 | 0,319465 | 1,1047 |
| ri_pgn | 21 | 0,413535 | 0,382629 | 0,796164 | 0,807453 | 0,9860 | 0,447252 | 1,7801 |
| ceninf | 39 | 0,422018 | 0,386163 | 0,808181 | 1,142938 | 0,7071 | 0,823485 | 0,9814 |
| ri_rml | 46 | 1,707480 | 1,343525 | 3,051005 | 3,550498 | 0,8593 | 0,979694 | 3,1142 |
| nmcief | 55 | 1,020646 | 0,747021 | 1,767667 | 2,872825 | 0,6153 | 1,172434 | 1,5077 |
| adrei | 70 | 0,625080 | 0,651006 | 1,276086 | 1,239473 | 1,0295 | 1,478050 | 0,8634 |
| opefci | 74 | 0,609494 | 0,567516 | 1,177010 | 0,588646 | 1,9995 | 1,562510 | 0,7533 |
| ri_dcpc | 75 | 1,167431 | 0,985663 | 2,153094 | 2,154167 | 0,9995 | 1,596739 | 1,3484 |
| snp_tr | 103 | 1,200508 | 1,241520 | 2,442028 | 2,638181 | 0,9256 | 2,194403 | 1,1128 |
| efemin | 119 | 1,233886 | 1,709581 | 2,943467 | 2,527026 | 1,1648 | 2,512685 | 1,1714 |
| ri_mmsef | 128 | 0,783223 | 1,127163 | 1,910386 | 1,730887 | 1,1037 | 2,726105 | 0,7008 |
| manori | 152 | 2,292106 | 1,834569 | 4,126675 | 5,601643 | 0,7367 | 3,236057 | 1,2752 |
| expaef | 165 | 1,268476 | 1,366561 | 2,635037 | 1,437583 | 1,8330 | 3,483975 | 0,7563 |
| ri_ccna | 169 | 1,695671 | 1,823056 | 3,518727 | 3,489889 | 1,0083 | 3,597377 | 0,9781 |
| ayccef | 196 | 1,677119 | 1,955994 | 3,633113 | 2,297370 | 1,5814 | 4,138540 | 0,8779 |
| cirmo3 | 256 | 2,748674 | 2,538137 | 5,286811 | 5,157540 | 1,0251 | 5,405440 | 0,9781 |
| snp_cheq | 265 | 3,225459 | 2,838037 | 6,063496 | 7,586441 | 0,7993 | 5,648652 | 1,0734 |
| cajasc | 287 | 2,754479 | 2,979378 | 5,733857 | 4,646787 | 1,2339 | 6,060005 | 0,9462 |
| depaho | 442 | 4,003951 | 4,241745 | 8,245696 | 5,466447 | 1,5084 | 9,332830 | 0,8835 |
| lingeef | 613 | 6,481232 | 6,588401 | 13,069633 | 14,314829 | 0,9130 | 12,943495 | 1,0097 |

## 3. Los ids de modelo

La sección 3 del reporte, tal cual:

De `t5/salidas/modelos_t5.json`. Fuente: las bases de la caché del runner (data/experiment/reextraccion_v2/e1_extractor/cache/e1_extraccion.db, e3_verificador/cache/e1_reintentos.db, e3_verificador/cache/e3_verificacion.db), ignoradas por git; copiadas con sus -wal y -shm fuera del repo, como en t2/freno_modelo_t2.py; cache.model por access_log.run_label.

| etapa | ids | respuestas distintas | esperado | igual |
|---|---|---|---|---|
| E1 | claude-haiku-4-5-20251001 | claude-haiku-4-5-20251001 3.347 | claude-haiku-4-5-20251001 | True |
| reintentos de E1 de la fase de E3 | claude-haiku-4-5-20251001 | en NO_ABRIR_conteos_t5.json: cuentan los reintentos | claude-haiku-4-5-20251001 | True |
| E3 | claude-sonnet-5 | en NO_ABRIR_conteos_t5.json: cuentan los reintentos | claude-sonnet-5 | True |

- Lo que cuenta la columna de E1: las claves distintas de la caché de E1 con las etiquetas corpus_<TO>_e1 de los 20 TOs (incluye los reintentos por corte y por forma de la fase E1).
- El manifiesto 818a62cf… no fija el id de modelo: sus sellos no tienen esa clave (solo temperaturas y namespaces).
- El freno por modelo de T2: 29 eventos en `avance_t2.jsonl`, con OK; ids de E1 claude-haiku-4-5-20251001 y de E3 claude-sonnet-5; iguales a los de las bases: True.
- Fuentes del esperado: E1, pre-registro, §2 (el freno por id); el código pide el alias claude-haiku-4-5 (runner_corpus.py:91); E3, runner_corpus.py:94 y pre-registro, §2.

## 4. El alcance y el catálogo

La sección 7 del reporte, tal cual:

De `t5/salidas/alcance_catalogo_t5.json`, desde `t3/conteos_sin_leer/contado_sin_leer_t3f.json`.

| registro | filas | en cuarentena | verificadas en cuarentena | claves | con 2 unidades o más | con 3 o más | en 2 TOs o más |
|---|---:|---:|---:|---:|---:|---:|---:|
| veinte | 908 | 703 | 570 | 237 | 38 | 12 | 8 |
| veinte_sincola | 896 | 693 | 561 | 233 | 37 | 12 | 8 |
| acumulado | 1.186 | 851 | 713 | 320 | 56 | 19 | 13 |
| acumulado_sincola | 1.169 | 839 | 702 | 315 | 54 | 19 | 12 |

- **El umbral:** 2 unidades distintas (enmienda 4, §1, punto 2, y decisión 1 al firmar). Las claves: solo cuántas: son menciones de unidades que no están todas en unidades_a_la_vista_T4.json; la lista está en t3/conteos_sin_leer/contado_sin_leer_t3f.json (catalogo_al_cierre), commiteada.
- **Desvío del §5.5, declarado:** el catálogo no crece en la tanda 1; la lectura de sus claves se hace una sola vez, sobre el acumulado de las tres tandas (pre-registro de la tanda final, versión para firmar v3, §9, decisión 4); se declara como desvío del §5.5 del pre-registro de la tanda 1.
- **Cuántas relaciones resolvió cada versión del catálogo:** hubo 1, la de la release (catálogo del request c3ad1581…, sin ampliaciones del catálogo de resolución). En el evaluado, E1 dio 3.950 relaciones con `sujeto_id` y 434 con `sujeto_propuesto`; el registro de no mapeados tiene 896 filas (cuarentena 693, resuelto_a_clase 201, descartado 2). Fuente: t3/conteos_sin_leer/contado_sin_leer_t3f.json, grafos.veinte_sincola (vigilancias.8 y f65_sujetos.registro_no_mapeados). La cuenta por versión de la enmienda 4 (§1, punto 5) sigue a una re-resolución, que en la tanda 1 no corre.
- **El ensamblado de la tanda 1 corrió sin catálogo de resolución:** True (ningún script de `t3/scripts/` lo nombra).
- **El alcance que leyó E1:** `data/experiment/catalogo_unico/registro_alcance_r2b.json`, `e06933e77a1ae819…`, igual al sello del manifiesto: True. Las líneas de alcance: 1.029 unidades, 190.841 tokens, USD 0,190841.

## 5. Los hallazgos en los dos ejes y las propuestas del backlog

La sección 8 del reporte, tal cual:

De `t5/salidas/hallazgos_t5.json`. Cuántos: incorrecta de una lectura de T4, 10; la cola, con la regla del 25 % disparada, 1; regresión declarada de T3, 2; vigilancia fuera de su línea de base, 3; fila del tablero que no cumple su meta, 3. Propuestas del backlog: 11, en `t5/propuestas_backlog_t5.jsonl` (no se escriben en el backlog).

| id | tipo | qué | cifra o veredicto | capa_pipeline | eje A | eje B | backlog |
|---|---|---|---|---|---|---|---|
| H01 | incorrecta de una lectura de T4 | aceptadas, ítems: `ri_ccna::D1F2::3.5` | con error | no dicha por la lectura | sin fila: la lectura no da la capa ni la fila, ni la causa | se difiere: las incorrectas van al backlog con capa_pipeline (protocolo entre tandas, :97-100) | propuesta |
| H02 | incorrecta de una lectura de T4 | aceptadas, ítems: `ri_dcpc::3.4.4.1` | con error | no dicha por la lectura | sin fila: la lectura no da la capa ni la fila, ni la causa | se difiere: las incorrectas van al backlog con capa_pipeline (protocolo entre tandas, :97-100) | propuesta |
| H03 | incorrecta de una lectura de T4 | aceptadas, ítems: `nmcief::A6::Sbloque12` | con error | no dicha por la lectura | sin fila: la lectura no da la capa ni la fila, ni la causa | se difiere: las incorrectas van al backlog con capa_pipeline (protocolo entre tandas, :97-100) | propuesta |
| H04 | incorrecta de una lectura de T4 | aceptadas, ítems: `nmcief::A6::Sbloque8` | con error | no dicha por la lectura | sin fila: la lectura no da la capa ni la fila, ni la causa | se difiere: las incorrectas van al backlog con capa_pipeline (protocolo entre tandas, :97-100) | propuesta |
| H05 | incorrecta de una lectura de T4 | aceptadas, ítems: `lingeef::3.1.2.2` | con error | no dicha por la lectura | sin fila: la lectura no da la capa ni la fila, ni la causa | se difiere: las incorrectas van al backlog con capa_pipeline (protocolo entre tandas, :97-100) | propuesta |
| H06 | incorrecta de una lectura de T4 | aceptadas, no ítems: `ri_ccna::D1A3L2::S7` | con error | no dicha por la lectura | sin fila: la lectura no da la capa ni la fila | se difiere: las incorrectas van al backlog con capa_pipeline (protocolo entre tandas, :97-100) | propuesta |
| H07 | incorrecta de una lectura de T4 | aceptadas, no ítems: `depaho::3.15::intro` | con error | no dicha por la lectura | sin fila: la lectura no da la capa ni la fila | se difiere: las incorrectas van al backlog con capa_pipeline (protocolo entre tandas, :97-100) | propuesta |
| H08 | incorrecta de una lectura de T4 | observación (12): `ri_rml::Sbloque11` | incorrecta (E1-prompt) | E1-prompt | F06 todo: la capa la da la lectura (E1-prompt): la corrige el prefijo de E1 (tabla de reprocesamiento, F06) | se difiere: un cambio de prompt queda fuera del grafo que evalúa B6.3 (pre-registro, §6.1; protocolo entre tandas, :93-95), y las incorrectas van al backlog con capa_pipeline (:97-100) | propuesta |
| H09 | incorrecta de una lectura de T4 | observación (12): `nmcief::A3::S2` | incorrecta (E1-prompt) | E1-prompt | F06 todo: la capa la da la lectura (E1-prompt): la corrige el prefijo de E1 (tabla de reprocesamiento, F06) | se difiere: un cambio de prompt queda fuera del grafo que evalúa B6.3 (pre-registro, §6.1; protocolo entre tandas, :93-95), y las incorrectas van al backlog con capa_pipeline (:97-100) | propuesta |
| H10 | incorrecta de una lectura de T4 | observación (12): `efemin::7.7` | incorrecta (E1-prompt) | E1-prompt | F06 todo: la capa la da la lectura (E1-prompt): la corrige el prefijo de E1 (tabla de reprocesamiento, F06) | se difiere: un cambio de prompt queda fuera del grafo que evalúa B6.3 (pre-registro, §6.1; protocolo entre tandas, :93-95), y las incorrectas van al backlog con capa_pipeline (:97-100) | propuesta |
| H11 | la cola, con la regla del 25 % disparada | `cola` | 14 de 30; ponderada 0,4386, Wilson [0,2751; 0,6166]; sin las dudosas, 12 de 28 | no dicha por la lectura | sin fila: la regla, si se dispara, re-procesa las unidades de la cola o las saca del grafo evaluado (enmienda de la cola humana, §1, punto 6); el evaluado ya es el sin cola | la investigación de su causa, antes de la tanda final y sin cambiar el grafo sin cola (pre-registro, 95b18217:634-635); la diseña la mesa, no es de T5 | no: queda para la investigación de la causa |
| H12 | regresión declarada de T3 | `E4-a1` | persiste | E1-prompt (la de BKL-0048) | F06 todo: por la capa de BKL-0048, E1-prompt | se difiere: decisión de la autora del 18/10/2026, opción (ii) (registro de decisiones, §29) | ya está: BKL-0048 |
| H13 | regresión declarada de T3 | `E4-a4` | persiste | E1-prompt (la de BKL-0048) | F06 todo: por la capa de BKL-0048, E1-prompt | se difiere: decisión de la autora del 18/10/2026, opción (ii) (registro de decisiones, §29) | ya está: BKL-0048 |
| H14 | vigilancia fuera de su línea de base | `(5)` | requisito_de_estructura 0, tipo_obligacion_normalizados 1 | no dicha: es un conteo, sin lectura | nada: requisito_de_estructura da 0, como su línea de base; el contador de normalizados da 1 contra 0: el validador ya normalizó el valor, y se declara como residuo | no se corrige: residuo declarado | no |
| H15 | vigilancia fuera de su línea de base | `(8)` | sujeto_propuesto 434 de sujeto_id 3950 (9,90 %) | catálogo (la del remedio previsto: el crecimiento del catálogo de resolución, enmienda 4) | F13 solo código sobre lo guardado: el catálogo de resolución crece al cierre y actúa sobre la mención guardada | se corrige antes del sello del grafo evaluado, con la lectura única de las claves sobre las tres tandas (pre-registro de la tanda final, v3, §9, decisión 4), si la autora la aprueba a tiempo | no: va por la lectura de las claves |
| H16 | vigilancia fuera de su línea de base | `(9)` | 7 emisiones en E1 (snp_tr 7); 20 aristas en el grafo | no dicha: es un conteo, sin lectura | sin fila: hace falta leer las emisiones (el instrumento de la vigilancia es un muestreo) | se difiere: la lectura de las emisiones no está despachada | propuesta |
| H17 | fila del tablero que no cumple su meta | `fila 64` | Comunicacion.tipo sin marca ni original 32: el residuo que la meta declara (Comunicacion sin `tipo`; L-04) | no dicha: es un conteo, sin lectura | F14b solo código sobre lo guardado: si la lectura de L-04 llega al piso, la corrige su código previsto (la marca tipo_no_derivable de validador_r2; §6.7) | se corrige entre tandas solo por la regla de L-04 (§6.7), que no está despachada (registro de decisiones, §29); si no llega al piso, queda el residuo declarado | no |
| H18 | fila del tablero que no cumple su meta | `fila 67` | 6 sin campo de 663 con cuantía: el residuo que la meta declara (4 en diez) | no dicha: es un conteo, sin lectura | nada: se declara como residuo, como en la tanda 0 (tablero:67) | no se corrige: residuo declarado | no |
| H19 | fila del tablero que no cumple su meta | `fila 68` | sin categoría 2, sin tramo 5: el residuo que la meta declara (1 sin tramo por grafo) | no dicha: es un conteo, sin lectura | nada: se declara como residuo, como en la tanda 0 (tablero:68) | no se corrige: residuo declarado | no |

**La causa de cada hallazgo**, tal cual (la de las lecturas es la nota de la autora; sin nota, «causa: no dicha por la lectura»):

- **H01** (`ri_ccna::D1F2::3.5`): causa: no dicha por la lectura
- **H02** (`ri_dcpc::3.4.4.1`): causa: no dicha por la lectura
- **H03** (`nmcief::A6::Sbloque12`): causa: no dicha por la lectura
- **H04** (`nmcief::A6::Sbloque8`): causa: no dicha por la lectura
- **H05** (`lingeef::3.1.2.2`): causa: no dicha por la lectura
- **H06** (`ri_ccna::D1A3L2::S7`): N1 (la valuación debe seguir las normas del BCRA) es el criterio que la revisión controla, no un supuesto de ella; condicion_de hacia N3 lo invierte, como en items 17 y 19
- **H07** (`depaho::3.15::intro`): aplica_a al rol de todas las entidades intervinientes, pero el texto obliga solo a las del Grupo A (regla de cola 10)
- **H08** (`ri_rml::Sbloque11`): el 9.1.4 resta del control de la partida 210100 los saldos del 210105, que son justamente los bonos depositados en la CRyL y aplicados al incremento de exigencia; esos bonos quedan fuera del límite, así que la arista invierte el efecto (el tope sobre su aplicación es otro: 210105 ≤ 824000/001, en la tabla). La firma es válida, el error es de lectura del modelo
- **H09** (`nmcief::A3::S2`): el chapeau presenta la verificación como procedimiento que debe cumplir el auditor interno («independientemente del análisis de riesgos que efectúe el auditor interno, se deberán cumplimentar…»); en el texto la entidad aparece como auditada, no como quien verifica, y el modelo tomó esa mención como sujeto del deber (R-a: el texto nombra otro sujeto)
- **H10** (`efemin::7.7`): el 7.7 no prohíbe otorgar esas financiaciones, que son justamente las que reducen la exigencia; prohíbe computarlas además en las deducciones de otros puntos; la descripción del origen es fiel, pero la arista afirma que la financiación está prohibida (como cola 18, destino equivocado de la restricción); firma válida, error de lectura del modelo
- **H11** (`cola`): por unidad, en `unidades`: la nota de la autora, o «causa: no dicha por la lectura»; la causa de que se dispare la regla es la que investiga la mesa
  - `ri_ccna::D1F2::3.7` (RI:sin_raiz, dudosa): causa: no dicha por la lectura
  - `ri_ccna::D1F2::S1` (RI:sin_raiz, con error): causa: no dicha por la lectura
  - `ri_ccna::D2A2::S1` (RI:sin_raiz, con error): causa: no dicha por la lectura
  - `ri_dcpc::3.1.1` (RI:resto, con error): causa: no dicha por la lectura
  - `ri_rml::Sbloque10` (RI:resto, con error): causa: no dicha por la lectura
  - `ri_rml::Sbloque14::parte1` (RI:resto, con error): e4 aplica_a al rol de todas las entidades comprendidas, pero el punto 11.1 rige solo para las de Grupo A y el texto da otra regla a las B y C
  - `ri_rml::Sbloque14::parte4` (RI:resto, con error): e9 convierte en tope de las financiaciones la TNA del 24 %, que el texto usa solo para definir cuáles computan en la partida 712000/001
  - `lingeef::3.5.4.3` (NG:resto, con error): causa: no dicha por la lectura
  - `lingeef::5.4.2.3` (NG:resto, con error): causa: no dicha por la lectura
  - `depaho::3.8.3.4` (NG:resto, con error): causa: no dicha por la lectura
  - `efemin::6.4.3.1` (NG:resto, con error): causa: no dicha por la lectura
  - `lingeef::11.1.2` (NG:resto, con error): causa: no dicha por la lectura
  - `cajasc::3.7.3` (NG:resto, dudosa): causa: no dicha por la lectura
  - `depaho::4.19.4` (NG:resto, con error): causa: no dicha por la lectura
- **H12** (`E4-a1`): la de BKL-0048: la relación aplica_a de su unidad trae una mención que no está en el texto de la unidad, no verifica y va a cuarentena; la suite lo cuenta porque mira la etiqueta con la regla de E4 de r1 (data/backlog/backlog.jsonl, BKL-0048)
- **H13** (`E4-a4`): la de BKL-0048: la relación aplica_a de su unidad trae una mención que no está en el texto de la unidad, no verifica y va a cuarentena; la suite lo cuenta porque mira la etiqueta con la regla de E4 de r1 (data/backlog/backlog.jsonl, BKL-0048)
- **H14** (`(5)`): no dicha: es un conteo, sin lectura
- **H15** (`(8)`): no dicha: es un conteo, sin lectura
- **H16** (`(9)`): no dicha: es un conteo, sin lectura. La vigilancia pregunta por las emisiones fuera del dominio de pagos; si las de snp_tr lo están no lo leí: NO VERIFICADO
- **H17** (`fila 64`): no dicha: es un conteo de T3, sin lectura
- **H18** (`fila 67`): no dicha: es un conteo de T3, sin lectura
- **H19** (`fila 68`): no dicha: es un conteo de T3, sin lectura

**Las dudosas de las aceptadas, aparte** (5): la lectura no las decidió: cuentan como error para la tasa, la atención y el freno (regla de las dudosas), y no van como hallazgo ni al backlog; quedan para la mesa.

- `ri_mmsef::2.2.10.2` (aceptadas, ítems, RI:sin_raiz; propuesta dudosa): causa: no dicha por la lectura
- `ri_mmsef::2.2.13.1` (aceptadas, ítems, RI:sin_raiz; propuesta dudosa): causa: no dicha por la lectura
- `ri_dcpc::3.2.2.1` (aceptadas, ítems, RI:resto; propuesta dudosa): causa: no dicha por la lectura
- `expaef::9.6.4` (aceptadas, ítems, NG:resto; propuesta dudosa): causa: no dicha por la lectura
- `ri_ccna::D1A3L2::S33` (aceptadas, no ítems, RI:sin_raiz; propuesta con error): aplica_a a las cajas de crédito sigue el alcance del TO, pero es una prueba sustantiva sobre «la entidad», que apunta al auditor externo; el texto no nombra al obligado

**Lo que no es hallazgo por estas reglas:**
- las vigilancias (1), (2), (3) y (7): (1) sí 3, no 27, no decidible 0; (2) vaciamiento 15, no vaciamiento 15, no decidible 0; (3) duplicación 9, distintos 21; (7) con apoyo 2, sin apoyo 2, no decidible 0 (la tanda 0 no las leyó (pre-registro, §5.3): no hay una línea de base que pasar);
- la vigilancia (4): un TextoOrdenado por TO, True; las aceptadas: sin atención ni freno (tasas_t4_tramo2.json);
- las filas del tablero, por la lectura de su meta (mía, en `REGLA_FILAS` de `cifras_t5.py`): 49 sin meta numérica; 50 no medida; 51 no aplica; 52 no medida; 53 cumple; 54 cumple; 55 cumple; 56 residuo declarado; 57 residuo declarado; 58 residuo declarado; 59 hallazgos por la lectura; 60 residuo declarado; 61 cumple; 62 cumple; 63 cumple; 65 cumple; 66 cumple; 69 no medida; 70 cumple; 71 cumple; 72 no aplica; 73 cumple; 74 cumple.

**Las propuestas del backlog** (`t5/propuestas_backlog_t5.jsonl`, 11):

| hallazgo | tipo | qué | capa_pipeline | eje A | estado |
|---|---|---|---|---|---|
| H01 | incorrecta de una lectura de T4 | `ri_ccna::D1F2::3.5` | no dicha por la lectura | sin fila | PROPUESTA: no está en el backlog |
| H02 | incorrecta de una lectura de T4 | `ri_dcpc::3.4.4.1` | no dicha por la lectura | sin fila | PROPUESTA: no está en el backlog |
| H03 | incorrecta de una lectura de T4 | `nmcief::A6::Sbloque12` | no dicha por la lectura | sin fila | PROPUESTA: no está en el backlog |
| H04 | incorrecta de una lectura de T4 | `nmcief::A6::Sbloque8` | no dicha por la lectura | sin fila | PROPUESTA: no está en el backlog |
| H05 | incorrecta de una lectura de T4 | `lingeef::3.1.2.2` | no dicha por la lectura | sin fila | PROPUESTA: no está en el backlog |
| H06 | incorrecta de una lectura de T4 | `ri_ccna::D1A3L2::S7` | no dicha por la lectura | sin fila | PROPUESTA: no está en el backlog |
| H07 | incorrecta de una lectura de T4 | `depaho::3.15::intro` | no dicha por la lectura | sin fila | PROPUESTA: no está en el backlog |
| H08 | incorrecta de una lectura de T4 | `ri_rml::Sbloque11` | E1-prompt | F06 todo | PROPUESTA: no está en el backlog |
| H09 | incorrecta de una lectura de T4 | `nmcief::A3::S2` | E1-prompt | F06 todo | PROPUESTA: no está en el backlog |
| H10 | incorrecta de una lectura de T4 | `efemin::7.7` | E1-prompt | F06 todo | PROPUESTA: no está en el backlog |
| H16 | vigilancia fuera de su línea de base | `(9)` | no dicha: es un conteo, sin lectura | sin fila | PROPUESTA: no está en el backlog |

## 6. El selftest de claves

`scripts/selftest_t5.py` corre `data/experiment/mantenimiento/code/selftest_clave_cache.py` (sha256 `71522b1d4119475a491b3493c9785cef6e57f59343eb2a1c7fb3be0bf999581c`) tal cual, sobre la copia y dos veces (`salidas/selftest_t5.json`). Sus conteos van al `NO_ABRIR_`.

| bloque | veredicto |
|---|---|
| A, anclaje del perfil sellado (v3_b54), E1 | OK |
| A, anclaje del perfil sellado (v3_b54), E3 | OK |
| B, variaciones del perfil sellado | OK |
| inventario del armado del perfil sellado | OK |
| A', anclaje del perfil r2b, E1 | OK |
| A', anclaje del perfil r2b, E3 | OK |
| B', variaciones del perfil r2b | OK |
| inventario del armado del perfil r2b | OK |
| C, contraste con la tabla de reprocesamiento | OK |
| **general** | **OK** |

- Las dos corridas dan el mismo JSON byte a byte: True; códigos de salida [0, 0].
- Es el selftest de la tanda 0, tal cual: controla que la tanda 1 no tocó sus claves; para la tanda 1 no se adaptó.

## 7. El reporte y los demás archivos de T5

- **El reporte:** `data/experiment/tanda1/t5/reporte_tanda1.md`, que genera `scripts/reporte_t5.py` desde `salidas/`.
- **La columna «Tanda 1», como propuesta aparte:** `t5/columna_tanda1_tablero_PROPUESTA.md`. No escribí en `docs/tablero_correcciones.md`.
- **Las propuestas del backlog:** `t5/propuestas_backlog_t5.jsonl`. No escribí en el backlog.
- **El `NO_ABRIR_`:** `t5/NO_ABRIR_conteos_t5.json`, sha256 `13e65dcc24c3057a5a815ea09d3c9101d7ae229f8050d0b8c7f8a2658badea7f`. Lo arma `scripts/no_abrir_t5.py` desde las dos partes que escriben `cifras_t5.py` y `selftest_t5.py`; ninguno imprime su contenido, y no lo abrí.
- **La tarifa observada** es una propuesta para el §5 de la tabla de reprocesamiento (`salidas/costo_t5.json`, `tarifa_observada`). No la escribí en la tabla.

## 8. El cegamiento de U-MED-VERIF

- **Lo que no miré ni reporto:** el desglose por estado de E3, `n_reintentos`, `reintentos_e3.jsonl`, `copias_nota_e3.jsonl`, las `marcas_e3` y el gasto de los reintentos aparte.
- **De `estado_corpus.json`** el script lee solo `gasto_usd` y `resumen.n` de cada fase: el resumen de E3 trae además el desglose por estado, que no se lee. Las aceptadas y la cola salen de `t2/resumen_t2.json`, con los tres estados juntos; de `finales.jsonl` no se lee nada.
- **E3 va como una sola cifra por TO,** con los reintentos adentro. No recalculé el costo con los tokens, porque los registros de E3 separan los reintentos.
- **Los ids de modelo:** de E1, su cuenta; de E3 y de los reintentos de E1 de la fase de E3, solo los ids, porque sus cuentas incluyen los reintentos. Esas cuentas van al `NO_ABRIR_`, con los conteos del selftest.
- **El contenido de extracciones:** el reporte y este FRENO muestran solo unidades de `t3/muestras/unidades_a_la_vista_T4.json`; `cifras_t5.py` lo controla para cada unidad que nombra. Las claves del catálogo, que son menciones de unidades que no están todas a la vista, van solo como cuántas. Por eso `unidades_a_la_vista_T5.json` no hizo falta, y no lo escribí.
- **Los `NO_ABRIR_` de T2, T3 y T4** no se tocaron ni se abrieron (sección 12). La copia del repo los excluye.

## 9. Las dos corridas de `cifras_t5.py`

`scripts/dos_corridas_t5.py` compara la corrida que va al repo (`salidas/`) con la segunda, a otra salida (en el paquete), archivo por archivo, y las dos partes del `NO_ABRIR_` solo por su sha256 (`salidas/dos_corridas_t5.json`):

| archivo | sha256 | igual en la segunda corrida |
|---|---|---|
| `alcance_catalogo_t5.json` | `1b70c08926506c2bfcb510290104190c008c60bf29d3705df4958784705e210f` | True |
| `columna_tanda1_t5.json` | `db84d95264c56c673a43f9228e2e7951adb2a65f29afed906e5e1ba731da300c` | True |
| `consola_cifras_t5.txt` | `d6fd5f4b9c3429cd31b66575b5549205f1b2022985b8fae9afb99b1d024dd8eb` | True |
| `costo_t5.json` | `5c6c58b2bec9c8dcb7284f769eb0bf23edd385fc51af5445f1835229ac77b9a4` | True |
| `fuentes_t5.json` | `323b0f952b8ac56b9135466760e927fd7e15011423dda4e91bfb61b0066e446b` | True |
| `hallazgos_t5.json` | `bc2d2a6fd8d2d4b5a30bdd35f19cc93388601c1eb1fdb00f70b48d5008ae044e` | True |
| `incidencias_t5.json` | `4ebaaccd881807bd087b06943d5b9782f65bfa7c38dcbbf7b685ca38868c6b2b` | True |
| `modelos_t5.json` | `12dcb0c43b74c97a785f52f89f327f2bddb6be6e5902475222871475537a6607` | True |
| `volumenes_t5.json` | `7468c0014a4a0fc05f63fbd2d12d55eb921756ef97a4ac39ba167ba141d77189` | True |
| `../propuestas_backlog_t5.jsonl` | `c92fed88b8cf78b9f332cc79637ae220cf2afb5fd56eb9d2fc4ff9e93f8865cb` | True |

Mismos nombres: True. La parte del `NO_ABRIR_` de cada corrida, igual por sha256: True. Todo igual: True.

## 10. Para la autora y la mesa

1. **Las metas del tablero:** la lectura de cada meta es mía (`REGLA_FILAS` en `cifras_t5.py`, y la última columna de la propuesta). No cumplen las filas 64, 67, 68, las tres con el mismo residuo que su meta ya declara para la tanda 0.
2. **Las incorrectas de las lecturas:** 5 no tienen nota de la autora, así que su causa va «no dicha por la lectura». Ninguna de las 7 de las aceptadas trae su capa, así que su propuesta del backlog lleva «no dicha por la lectura» en `capa_pipeline`: la fija quien la triage.
3. **Las dudosas de las aceptadas** (5) no van como hallazgo ni al backlog: la lectura no las decidió.
4. **La vigilancia (9):** la vigilancia pregunta por las emisiones fuera del dominio de pagos; si las de snp_tr lo están no lo leí: NO VERIFICADO.
5. **La cola:** la investigación de la causa queda para la mesa, como dice el mandato. No la empecé.
6. **El catálogo:** la lectura de las claves va una sola vez, sobre las tres tandas. El reporte declara el desvío del §5.5.
7. **La foto del paso 0:** las horas que da el mandato (17:23:48 a 17:24:00) son las de mi foto de después del segundo tramo, anterior a su FRENO. La comparé con esa y con la final (17:24:35): las dos dan lo que trajeron los commits (sección 1).

## 11. El script de cada cifra

| cifras | script (`t5/scripts/`) | salida |
|---|---|---|
| el costo, los ids de modelo, los volúmenes, el alcance y el catálogo, los hallazgos, la columna, las incidencias y las propuestas | `cifras_t5.py` | `salidas/` (`costo_t5.json`, `modelos_t5.json`, `volumenes_t5.json`, `alcance_catalogo_t5.json`, `hallazgos_t5.json`, `columna_tanda1_t5.json`, `incidencias_t5.json`, `fuentes_t5.json`, `consola_cifras_t5.txt`) y `propuestas_backlog_t5.jsonl` |
| las dos corridas iguales | `dos_corridas_t5.py` | `salidas/dos_corridas_t5.json` |
| el selftest de claves | `selftest_t5.py` | `salidas/selftest_t5.json` (su consola es ese mismo JSON, byte a byte: no la guardé aparte) |
| el `NO_ABRIR_` | `no_abrir_t5.py` | `NO_ABRIR_conteos_t5.json` (aquí, solo su sha256) |
| el reporte y la columna propuesta | `reporte_t5.py` | `reporte_tanda1.md`, `columna_tanda1_tablero_PROPUESTA.md` |
| la foto (sección 12) | `freno_t5_foto.py` | la sección 12 |
| el texto de este FRENO | `freno_t5_armar.py` | este archivo |
| la escritura en el repo | `escribir_en_el_repo_t5.py` | `escrituras_en_el_repo_t5.json`, en el paquete |
| el paso 0 (sección 1) | sus comandos y `verif_paso0_commits_t5.py` | sus salidas, pegadas; el script, en el paquete |

## 12. La foto del repo, los .pyc y el grep de convenciones

Lo genera `scripts/freno_t5_foto.py` desde la foto del paso 0 y la de después (las dos van en el paquete).

- **La foto** (`t2/foto_repo_tanda1_t2.py`). Paso 0: 18:19:21 a 18:19:32 del 2026-10-18, 52.586 entradas. Después: 18:50:10 a 18:50:21 del 2026-10-18, 52.609 entradas, 17 sin abrir y 342 enlaces.
  - **23 nuevos:** 4 en `tanda1/t5/, lo demás`; 11 en `tanda1/t5/salidas/`; 8 en `tanda1/t5/scripts/`.
  - **0 borrados:** ninguno.
  - **0 cambiados:** ninguno.
  - **Fuera de lo admitido:** 0.
  - **Los `NO_ABRIR_` de T2, T3 y T4** (4), sin abrirlos: tamaño y hora iguales en las dos fotos: True (`NO_ABRIR_conteos_reextracciones_tanda1.json`, `NO_ABRIR_salida_e3_tanda1.txt`, `NO_ABRIR_conteos_t3.json`, `NO_ABRIR_conteos_t4.json`).
- **Los `.pyc`:** 11.236 líneas en el paso 0 y 11.236 después; listas iguales: True.

**El sha256 de los archivos de T5** (de la foto de después; el del `NO_ABRIR_`, de la escritura, porque la foto no lo abre):

| archivo | sha256 |
|---|---|
| `NO_ABRIR_conteos_t5.json` | `13e65dcc24c3057a5a815ea09d3c9101d7ae229f8050d0b8c7f8a2658badea7f` |
| `columna_tanda1_tablero_PROPUESTA.md` | `ed17aec19aa8a159d777b1b6824599f0043f2b18388c2355b4dede35ca7e40ff` |
| `propuestas_backlog_t5.jsonl` | `c92fed88b8cf78b9f332cc79637ae220cf2afb5fd56eb9d2fc4ff9e93f8865cb` |
| `reporte_tanda1.md` | `29bcc98a539ddf6f44e87a315d72dd42d31937986204c54eb47cc358db702ed2` |
| `salidas/alcance_catalogo_t5.json` | `1b70c08926506c2bfcb510290104190c008c60bf29d3705df4958784705e210f` |
| `salidas/columna_tanda1_t5.json` | `db84d95264c56c673a43f9228e2e7951adb2a65f29afed906e5e1ba731da300c` |
| `salidas/consola_cifras_t5.txt` | `d6fd5f4b9c3429cd31b66575b5549205f1b2022985b8fae9afb99b1d024dd8eb` |
| `salidas/costo_t5.json` | `5c6c58b2bec9c8dcb7284f769eb0bf23edd385fc51af5445f1835229ac77b9a4` |
| `salidas/dos_corridas_t5.json` | `bbd5f48ef86562c571ff31f6b99c442b3442fa54a55189f911f3433aa0cfb8d1` |
| `salidas/fuentes_t5.json` | `323b0f952b8ac56b9135466760e927fd7e15011423dda4e91bfb61b0066e446b` |
| `salidas/hallazgos_t5.json` | `bc2d2a6fd8d2d4b5a30bdd35f19cc93388601c1eb1fdb00f70b48d5008ae044e` |
| `salidas/incidencias_t5.json` | `4ebaaccd881807bd087b06943d5b9782f65bfa7c38dcbbf7b685ca38868c6b2b` |
| `salidas/modelos_t5.json` | `12dcb0c43b74c97a785f52f89f327f2bddb6be6e5902475222871475537a6607` |
| `salidas/selftest_t5.json` | `ff8a3e739328c3a8474959a0e467a70090ec05ca74f5f17d281887ccbe9406a0` |
| `salidas/volumenes_t5.json` | `7468c0014a4a0fc05f63fbd2d12d55eb921756ef97a4ac39ba167ba141d77189` |
| `scripts/cifras_t5.py` | `d80b680859064773a5841dce6e4fe8c84ee72ab76d3363ed027e85dfc84c5403` |
| `scripts/dos_corridas_t5.py` | `9d88fb518a6a5b3f2bd5ac8d4ed005b8f5e91b121615e4a4c8adaa7450d2052d` |
| `scripts/escribir_en_el_repo_t5.py` | `6509381d3c6046ed531cfce4200b6e23d7727a3c2e3a60f09cf9d4bfa6788e21` |
| `scripts/freno_t5_armar.py` | `a9a7d4e553823ddfb5c5811116f0fe80da2208045dbf1a96e0c19c200795ca35` |
| `scripts/freno_t5_foto.py` | `95013b5c1dbacd7390a86470e3b56401867e61926ce33b39a2742f48eb020a26` |
| `scripts/no_abrir_t5.py` | `db56757b1ef37ee16a2e109d45deda88802cffe631019c36a4f40f5c2816c3d9` |
| `scripts/reporte_t5.py` | `85706bf921d5e300ba3f09f806c4b36ceae99056a04d3211a1231efe9a9ee2ed` |
| `scripts/selftest_t5.py` | `e7eab54e39572df02039fe3cc9234c945d90c705f9438ee3ced3107d5b1bda6c` |

- **El grep de convenciones** (`grep_convenciones_t5.py` y su salida, en el paquete) busca las palabras del `user.name` de git y las de origen conversacional (Slack, mail, correo, «como dijo», «pedido por», …) en los 22 archivos nuevos o cambiados de la foto, sin los `.DS_Store` ni el `NO_ABRIR_`. El control positivo da la línea 2. Con el patrón, en los archivos que redacté: `freno_t5_armar.py`, 1 línea(s): son las líneas de un script que describen el patrón del grep. Las palabras del nombre, en ningún archivo: True. Rutas con la carpeta personal o el scratchpad: 0 archivo(s). El grep del FRENO va en el mensaje de cierre.
- **La copia** del repo es la del `rsync` de la cláusula, más la exclusión del volumen de Neo4j, y su control dio 0 (`rsync_copia_t5.log` en el paquete). Ningún `git clone`, ningún heredoc sin el delimitador entre comillas, y no abrí ninguna carpeta vedada. No abrí ni usé la sesión ni la copia de A3.

## 13. Errores propios, con su causa

1. **El hallazgo de la cola salió sin el campo `causa`** en la primera versión de `cifras_t5.py`.
   - La causa: en la cola puse la causa de cada unidad dentro de `unidades` y no la del hallazgo.
   - Lo vi al revisar la salida, antes de escribir nada en el repo, y lo agregué: apunta a la nota de cada unidad.

FRENO T5. Espero la revisión de la mesa.
