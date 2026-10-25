# FRENO A2.1-c — tramo 3 de A2.1: el borrador del pre-registro de A2.2

Mandato: `docs/mandatos/A2_1_sistema_por_fragmentos_preregistro_A2_2.md` (texto firmado en `c2b6cb60`, `b311859c…`), §5 y §6, con el
«seguí» del tramo 3 del 24/10/2026 y el insumo v2 de la mesa. USD 0: no corrí nada pago ni usé el `.env`. Escribí en el repo solo el
borrador y este FRENO, los dos nuevos; nada commiteado, ningún mensaje de commit preparado, nada en la memoria. El pre-registro lo firma
la autora.

**En corto:**

- **El borrador:** `docs/preregistro_A2_2_sistema_por_fragmentos.md`, 297 líneas, sha256 `c87b78f235c7266bfc18c2060a8da843cbd37e72cff51f9cdd389cfe28721985`, con
  «BORRADOR» en el encabezado. Va en el orden del insumo: los huecos, los brazos, lo común, EV2 y el juez, el análisis, el tope y lo que no
  se decide, y las sesiones en el repo; suma lo que falta antes de correr y la lista de las decisiones.
- **Las anclas del insumo:** las 56 que llevan línea dan en HEAD, con la sección que citan (§2). Las fuentes de A2.1, U-NAV, Q8, el plan
  y las cuatro configuraciones son iguales en `2db79462`, el HEAD que declara el insumo, y en HEAD; el registro solo creció al final.
- **Las 113 anclas que agrega el borrador** también dan en HEAD, controladas por código (`controlar_anclas_borrador_a22.py`, en el
  paquete).
- **Cuatro cosas del insumo que el repo no sostiene como están** (§3): la salida de las herramientas (la §72 quedó atrás); la plantilla
  nueva, que no está en HEAD y con la que no corrió el tramo 2; P, que no se conoce antes de correr; y el costo del brazo del grafo, que
  no está en el repo.
- **Ocho [DECIDE LA AUTORA]** (§5): R5, A-D2 y A-D4, que pedía el «seguí», y cinco que encontré al aplicar las fuentes (A-D5 a
  A-D9).

## 0. Paso 0 (24/10/2026, con `$HOME`)

```
$ pwd
$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg
$ git log --format='%h %s' -8
af4dab8e Registro de decisiones: la primera ola de preguntas de B6.3 decidida, los pasos pagos del tramo 2 del banco verificados con sus sesiones enmascaradas, el tope de turnos y la etapa T revisada
7a9fe8ca Banco del brazo de fragmentos: el humo de las dos configuraciones y la caracterizacion del tope de turnos del tramo 2, con las transcripciones y los streams enmascarados
084499c6 Registro de decisiones: la medicion del reintento del verificador cerrada sin medir, los pasos pagos del tramo 2 del banco y la primera ola de preguntas de B6.3 revisada
f7d7877d Registro de decisiones: los contaminados de B6.3 con la regla del 09/10, los sorteos de B6.3 sellados y el cegamiento de la etapa T de tripletas
6c6dcad9 Banco del brazo de fragmentos: el control del disco y la lectura acotada del valor remoto por tool en el runner del tramo 2, y los logs de su test con nombre por corrida
0a6374ba Registro de decisiones: el grafo evaluado revisado y sellado, la contaminacion de B6.3 por documento, la etapa a-ter del juez v2 y la validacion por expertos
fde70c67 Grafo evaluado: el acumulado de las tres tandas con la reaplicacion unica, sellado con sus dos versiones comprimidas, la correspondencia de ids y el paquete de su medicion
c6565aa4 Registro de decisiones: la reaplicacion unica pegada, la regla del label con el articulo inicial de E4, un caso fuera de la iteracion 1 del juez v2 y las decisiones de la autora sobre los preregistros de B6.3 y A2.2
$ git rev-parse --abbrev-ref HEAD
main
$ git status --porcelain --untracked-files=no
$ git status --porcelain --untracked-files=all -- data/experiment/banco_mcp
$ ls docs/preregistro_A2_2_sistema_por_fragmentos.md
ls: docs/preregistro_A2_2_sistema_por_fragmentos.md: No such file or directory
$ shasum -a 256 <insumo> <nota>
d786544e4f8f0bd174ce1f4994dfebfdad19e64856cb0a74c0c7b4dff2f2108a  $HOME/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/d0348a29-aaa4-4292-82f3-0c0149e3787e/scratchpad/hoja_de_ruta_tanda1_mesa/decisiones_253_mesa/a22/INSUMO_PREREGISTRO_A2_2_PARA_EL_TRAMO_3_v2_mesa.md
01214f042f2c8714f24b4a05e2a6341f05230d128b907d7fcf6cb34d6bb8ad97  $HOME/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/d0348a29-aaa4-4292-82f3-0c0149e3787e/scratchpad/hoja_de_ruta_tanda1_mesa/decisiones_264_mesa/r5/R5_y_tope_A2_2_para_la_firma_mesa.md
```

Todo dio lo esperado: `main`; sin cambios rastreados; `7a9fe8ca` entre los ocho; `banco_mcp/` limpio; el borrador no existía; el sha256
del insumo v2 (`d786544e…`) y el de la nota de R5 (`01214f04…`) son los del «seguí». La foto del repo de antes es de las 09:47:23 (§6).

## 1. Lo que leí y lo que no abrí

- **Del paquete de la mesa, solo los dos archivos del «seguí»:** el insumo v2 y la nota de R5 y el tope. No leí
  `controles_preregistros_250_mesa.py` ni `regla_del_N_B63_s94_mesa.py`, que el insumo nombra.
- **Del repo, en HEAD (`git show`):** A2.1, el registro, U-NAV, Q8 y el plan; del protocolo de EV2 (`docs/protocolo_corrida_ev2.md`), sus
  encabezados (el `grep '^#'` mostró también dos comentarios de su §1 con la cuenta de preguntas y criterios) y sus §3 y §5
  (`:95-148`); del método de EV2 (`docs/preregistro_evaluacion_fidelidad_ev2.md`), `:1-58` y `:77-99`, sin su
  §5 (la calibración); los FRENOs
  A2.1-a y A2.1-b, las configuraciones del banco, la plantilla del prompt, partes de `servidor_mcp_kg.py`, `servidor_mcp_vector.py`,
  `lanzar_agente.py`, `correr_a2_1.py`, `enmascarar_cwd_a2_1.py` y `grafos.py`, las metas, los comandos y los prompts del tramo 2, y el
  JSON de la asimetría de la consulta (`data/experiment/controles_a2_2/`).
- **EV2, sin abrir:** `preguntas_ev2_fidelidad.json`, solo su sha256 con `shasum`. Del juez de EV2 leí, con `grep`, las líneas de `juez.py` que
  nombran el modelo, la versión y el sha256 del prompt (`:17`, `:37`, `:41-48`, `:78`, `:138` y `:143`), y tomé el sha256 de `juez.py` y de `prompt_juez_v1.md`; no abrí el prompt ni ninguna salida del juez,
  traza o tabla de EV2, ni `ev2_reporte/reporte_ev2.md`. Para ubicar el prompt listé con `git ls-files` los nombres de los primeros 20
  archivos de `data/experiment/ev2_juez/`, entre ellos los de `gold_q12_ajuste/`: no abrí ninguno.
- **Lo que salió en la consola sin buscarlo:** el mensaje del commit del sello de EV2 (`9c445167`), al listar la historia del protocolo,
  trae la cantidad de preguntas por documento; no trae ninguna pregunta.
- **Otros:** el `pip freeze --all` del venv del servidor de fragmentos, que solo lee (63 líneas, sha256 `24f4c064…`, el mismo del FRENO
  A2.1-a); y la transcripción de esta sesión, para recuperar la salida del paso 0 y el punto del «seguí» del tramo 2 sobre
  `MAX_MCP_OUTPUT_TOKENS`.
- No abrí ningún `.env`, `.claude.json` ni `NO_ABRIR_*`, ni las carpetas vedadas; no hice copias del repo.

## 2. Las anclas del insumo

«Da» quiere decir que el texto en HEAD dice lo que el insumo dice que dice (`controles/anclas_insumo_a22.txt`, impreso por
`anclas_insumo_a22.py`, leído ancla por ancla) y que la sección es la que cita (`anclas_secciones_a22.txt`, por código). Las cuatro
anclas de configuraciones JSON no tienen sección.

| id | ancla en HEAD | lo que dice el insumo | sección en HEAD | da |
|---|---|---|---|---|
| intro-1 | A2.1, `:128-154` | A2.1, §5: el borrador del pre-registro | §5 | sí |
| intro-2 | A2.1, `:165` | A2.1, §6: el borrador en docs/ | §6 | sí |
| A-1a | A2.1, `:51-52` | versión del CLI; si es otra se declara | §2 | sí |
| A-1b | A2.1, `:121-124` | re-validar el grafo de la fase B si cambió el CLI | §4 | sí |
| A-2 | A2.1, `:119-120` | H-B2: num_turns, si --max-turns corta y cuándo; propuesta R5 | §4 | sí |
| 1-a | A2.1, `:191-192` | D-A: el grafo de desarrollo re-sellado | §8 | sí |
| 1-b | A2.1, `:253` | nota del 15/10: acb26dca, rs1 | Notas posteriores a la firma | sí |
| 1-c | `mcp_kg/config_mcp_kg_a2_desarrollo_r2b_rs1.json`, `:5-7` | config del grafo: clave y sha | — | sí |
| 1-d | A2.1, `:80-81` | carga y test positivo al principio de A2.2 | §3 | sí |
| 1-e | A2.1, `:82-83` | comentario «r2b no se evalúa con EV2» | §3 | sí |
| 1-f | registro, `:2138-2140` | §61: A2.2 no usa ver_punto | §61 | sí |
| 1-g | registro, `:1738-1739` | §50: A2.2 no usa desde | §50 | sí |
| 1-h | `mcp_vector/config_fragmentos_bm25_r2b.json`, `:5-10` | BM25: índice, analizador, k1 y b | — | sí |
| 1-i | A2.1, `:66-68` | diferencias con el analizador del grafo | §3 | sí |
| 1-j | `mcp_vector/config_fragmentos_denso_r2b.json`, `:5-7` | denso: matriz y harrier | — | sí |
| 1-k | A2.1, `:195` | D-D: top-k = 5 | §8 | sí |
| 1-l | A2.1, `:193` | D-B: el híbrido fuera | §8 | sí |
| 2-a | `a2_1/config_agentes_a2_1.json`, `:8-10` | claude-sonnet-5, --bare, CLI 2.1.241 | — | sí |
| 2-b | U-NAV, `:202-211` | U-NAV §5: la plantilla sin los cinco TOs | §5 | sí |
| 2-c | U-NAV, `:217` | U-NAV: A2.2 sin la parte común de la estrategia | §5 | sí |
| 2-d | U-NAV, `:196-198` | U-NAV: diff entre brazos | §5 | sí |
| 2-e | A2.1, `:103-114` | A2.1 §4: el envoltorio | §4 | sí |
| 2-f | registro, `:1750-1751` | §50 punto 4: R5 | §50 | sí |
| 2-g | registro, `:2555-2557` | §72: MAX_MCP_OUTPUT_TOKENS 70.000 y control de referencias | §72 | sí |
| 2-h | registro, `:3697-3699` | §96: control del disco | §96 | sí |
| 2-i | registro, `:2933-2936` | §82: desde la Terminal | §82 | sí |
| 2-j | registro, `:2972-2974` | §83: lista cerrada | §83 | sí |
| 2-k | registro, `:3035-3046` | §84: carpeta de configuración, cwd, lanzador | §84 | sí |
| 2-l | registro, `:3761-3762` | §97: tengu_velvet_ibis | §97 | sí |
| 2-m | registro, `:1686` | §49: venv y pip freeze | §49 | sí |
| 3-a | A2.1, `:34-36` | EV2 por ruta y sha | §1 | sí |
| 3-b | A2.1, `:139-140` | N = 1 + N = 3 parciales y auditoría | §5 | sí |
| 3-c | plan, `:340` | plan :340 (A2.2) | A2 · Baseline RAG tradiciona | sí |
| 3-d | registro, `:3313-3314` | §89: el orden de B6.3 | §89 | sí |
| 3-e | A2.1, `:241-244` | nota: el juez congelado | Notas posteriores a la firma | sí |
| 3-f | Q8, `:36-37` | Q8 decisión 1 | §2 | sí |
| 3-g | registro, `:3558-3567` | §93: control del SDK | §93 | sí |
| 3-h | A2.1, `:245-246` | nota: la muestra simétrica | Notas posteriores a la firma | sí |
| 3-i | Q8, `:61-63` | Q8: semilla de la muestra | §4 | sí |
| 3-j | Q8, `:64-65` | Q8: el material lo arma la mesa | §4 | sí |
| 3-k | A2.1, `:247-248` | nota: el criterio del juez | Notas posteriores a la firma | sí |
| 3-l | Q8, `:77` | Q8 decisión 3 | §5 | sí |
| 3-m | registro, `:1011-1012` | §28: la columna de errores fuera de criterios | §28 | sí |
| 4-a | A2.1, `:142` | cifra principal y sin la cola | §5 | sí |
| 4-b | A2.1, `:145` | Holm | §5 | sí |
| 4-c | plan, `:339` | plan :339 | A2 · Baseline RAG tradiciona | sí |
| 4-d | A2.1, `:143-144` | predicciones | §5 | sí |
| 4-e | A2.1, `:146` | pares discordantes y c_agente | §5 | sí |
| 4-f | A2.1, `:147` | no comparabilidad | §5 | sí |
| 5-a | A2.1, `:148-149` | tope ~15; EV2 14,88 | §5 | sí |
| 5-b | registro, `:919-923` | §26: el carril pago | §26 | sí |
| 5-c | A2.1, `:150-151` | no al lado de la tanda 1 | §5 | sí |
| 5-d | A2.1, `:152` | lo que no se decide | §5 | sí |
| 5-e | plan, `:341` | plan :341 | A2 · Baseline RAG tradiciona | sí |
| 5-f | registro, `:3442` | §91: la prioridad del viernes | §91 | sí |
| 5-g | U-NAV, `:282-283` | U-NAV §7 reglas 1 y 2 | §7 | sí |

**Lo que el insumo cita sin línea, o fuera del repo:**

| ancla | lo que encontré |
|---|---|
| las fuentes «en HEAD `2db79462`» (`:10`) | `2db79462` es ancestro de HEAD. A2.1, U-NAV, Q8, el plan y las cuatro configuraciones tienen el mismo sha256 en los dos. El registro pasó de 3.776 a 4.225 líneas con un solo bloque agregado al final (`git diff -U0 2db79462 HEAD`: `@@ -3776,0 +3777,449 @@`), así que las anclas hasta `:3776` no cambian |
| sus sha256 en `controles_preregistros_250_mesa.py` (`:11`) | no lo leí (no está entre los dos archivos autorizados): no comparé los sha256 de la mesa |
| registro, §99 (`:7`, `:62`, `:72`, `:91`, `:96` y `:104`) | está en `:3842`, posterior a `2db79462`; sus decisiones 2, 14, 15, 16 y 17 dicen lo que el insumo les atribuye (`:3850`, `:3874`, `:3875-3877`, `:3878-3879` y `:3880`) |
| registro, §94 (`:84`) | sin línea en el insumo; el N de B6.3 está en `:3625-3627` |
| `regla_del_N_B63_s94_mesa.py` (`:85`) | en el paquete de la mesa; no lo leí (NO VERIFICADO) |
| `ev2_reporte/reporte_ev2.md:388-390` y `:403` (A2.1, `:148-149`) | no lo abrí: trae los resultados de EV2 |
| EV2, `1d587336…` (`:58`) | da: el sha256 completo de HEAD empieza así |
| el prompt del juez, `fd446f8e…` (`:65`) | da: es el sha256 de `prompt_juez_v1.md`, el que `juez.py` usa si no se fija `JUEZ_PROMPT_VERSION` |
| `B63:orden_corridas:v1` (`:64`) | da: registro, §99, decisión 7 (`:3856-3857`) |
| `mcp_kg/servidor_mcp_kg.py` y sus tres herramientas (`:30`) | da: `:70` |
| los 1.768 pasajes (`:35`) | da: A2.1, `:70`; `config_fragmentos_bm25_r2b.json:10` y `config_fragmentos_denso_r2b.json:16` |
| el grafo `acb26dca…` (`:26`) | da, y está sellado: `commit_sellado` `4fe6ece` (`grafos.py:188-193`), y el `kg.json` de HEAD da ese sha256 |

## 3. Lo que el repo no sostiene como está en el insumo (declarado, sin arreglarlo)

1. **La salida de las herramientas** (insumo, `:49-51`). El insumo cita la §72 (`:2555-2557`): `MAX_MCP_OUTPUT_TOKENS` en 70.000. Después
   vinieron la anotación de 200.000 caracteres en los dos servidores, con la variable en 70.000 (§79, `:2824-2828`); la anotación en el
   código (§94, `:3617-3620`; `mcp_kg/servidor_mcp_kg.py:68` y `mcp_vector/servidor_mcp_vector.py:74`); y la §96 (`:3688-3690`): con la
   anotación, ni la variable ni el presupuesto por mensaje actúan. La §76 (`:2729-2732`) decía que el humo y H-B2 corrían con la variable
   en 70.000; el «seguí» del tramo 2 dijo que no se fija (`a2_1/config_agentes_a2_1.json:57`), y ninguna de las 20 sesiones pagas la tuvo
   en su entorno (`entorno_de_la_sesion` de los `comando_*.json`: 20 de 20 sin la variable). En el borrador: §3 y A-D6.
2. **La plantilla del prompt** (insumo, `:42-44`). U-NAV decía que el tramo 2 validaba la plantilla sin los cinco TOs (`:210`) y que el
   cambio iba en su despacho (`:212`); el registro la pone en lo común de A2.2 (§29, `:1080-1081`). La plantilla de HEAD
   (`agentes/plantilla_prompt.txt:1`, sin cambios desde `1fa79de3`) nombra los cinco TOs, y los 20 `prompt_*.txt` del tramo 2 traen el
   paréntesis y «Tope de 10 llamadas». La plantilla de A2.2 no está en el repo ni la validó ninguna sesión. En el borrador: §3 y A-D5.
3. **P** (insumo, `:60-61`; nota, §3). La regla de EV2 que elige las parciales está en el protocolo de EV2 (`:104-110`) y su auditoría en
   `:115-122`; el método la encadena (`:90-94`). P no lo fija ninguna fuente antes de correr: sale de los veredictos de N = 1, por brazo,
   y cuenta las parciales y las auditadas (a lo sumo 40). La nota define P solo con las parciales, y su cuenta, (40 + 2P), lee
   «re-corrida N = 3» como dos sesiones más la base; el protocolo dice «las 3 re-corridas» (`:106`), que se puede leer como tres nuevas,
   (40 + 3P). Tampoco fija cómo se redondea el 10 %. En el borrador: §4 y A-D2, con las dos lecturas.
4. **El costo del brazo del grafo** (nota, §3): sale del modelo de la §181 de la mesa, que no está en el repo; también el alto de
   fragmentos, 0,1086 (NO VERIFICADO). El costo de fragmentos sí da: media y máximo de las 8 sesiones de pregunta del smoke, desde
   `a2_1/hb2/analisis_tramo2_A2_1.json` (0,034021 y 0,039881 en BM25; 0,032908 y 0,044986 en el denso). Rehice la tabla de la nota con
   los valores que la nota da con cuatro decimales (`tope_A2_2_recomputo.py`): 9 de las 12 celdas dan igual y 3 difieren en un centavo
   (P = 0, alto: 21,34 contra 21,33; P = 20, medio: 27,25 contra 27,26; P = 40, alto: 64,01 contra 64,00), lo que se explica por el
   redondeo de esas entradas. En el borrador va la tabla de la nota.

**Lo que el registro decide para este pre-registro y el insumo no trae** (lo sumé al borrador): las seis decisiones de A2.1 y la
asimetría de la consulta con sus cifras (§16, `:526-539`), verificadas contra
`data/experiment/controles_a2_2/consulta_pre_tokenizada_bm25_mesa.json`; el control de los índices al empezar A2.2 (§16, `:545`) y su
respaldo (§51, `:1799-1801`); que las 20 de verificación son también la muestra simétrica (§9, `:295-303`); A2.2 sin `desde` en ningún
brazo (§54, `:1875`); el mismo tope en los dos brazos (§49, `:1712-1713`); y lo que la autora pidió a la mesa antes de la firma (§51,
`:1802-1804`).

**Lo que no ubiqué:** la lista de ids de la cola sellada con el grafo (plan, `:339`), que pide la cifra sin la cola. Queda PENDIENTE en
el borrador (§5 y §8).

## 4. Los huecos, con su sección del FRENO A2.1-b

Sin cifras nuevas: cada hueco cita la sección del FRENO A2.1-b (o, para el venv, del FRENO A2.1-a) donde está su valor.

| hueco | en el borrador | sección del FRENO |
|---|---|---|
| A-1, la versión del CLI y la re-validación del grafo de la fase B | §1, `:23-24` | A2.1-b, §0 (`:29`) y §3 (`:100`); la re-validación no correspondía porque el CLI no cambió (A2.1, `:121-124`); el FRENO no lo dice con esas palabras |
| A-2, la señal de H-B2 | §1, `:25` | A2.1-b, §4 (`:122-140`), §5 (`:144-155`) y §6 (`:159-161`) |
| A-3, el costo por sesión | §1, `:26` | A2.1-b, §3 (`:78-93`), §4 (`:108-117`) y §8 (`:191-199`) |
| A-4, el lanzador, lo que corrió y el venv | §1, `:27` | A2.1-b, §0 (`:29-30`) y §1 (`:39-41`), más `harness_R10` de las metas para el segundo archivo del lanzador y la configuración; el venv, A2.1-a, §3 (`:167-176`), con el sha256 del `pip freeze` de la §49 (`:1686`) |
| A-5, el control del disco y `tengu_velvet_ibis` | §1, `:28` | A2.1-b, §2 (`:70-71`) y §7 (`:183-185`) |

## 5. Las [DECIDE LA AUTORA] del borrador

| decisión | opciones, en corto |
|---|---|
| R5 (§3) | (1) R5 como está, con «al tope» en llamadas del log R1, informado por brazo (la recomienda la mesa); (2) lo mismo con un tope duro de 30 llamadas en los servidores, código nuevo; (3) lo mismo, excluyendo las sesiones de más de 30 llamadas. `--max-turns` 12 solo si cambia R5 |
| A-D2, el tope (§6) | (a) para P = 40: 41 con freno 30,75 (55 y 41,25 con tres re-corridas); (b) para un P menor, con freno por proyección antes de las re-corridas; (c) dos topes, el de N = 1 (14 y 10,50) al firmar y el de las re-corridas después de N = 1. Y la lectura de «re-corrida N = 3»: dos más la base o tres nuevas |
| A-D4, las sesiones en el repo (§7) | (a) enmascaradas como las del tramo 2, con el script adaptado; (b) tal cual, como las de la fase B |
| A-D5, la plantilla nueva (§3) | (a) una unidad USD 0 antes de A2.2 que la escriba junto con la configuración de R5, más una sesión corta paga por brazo, con tope de la autora, que la valide; (b) que la validen las primeras sesiones de A2.2 (una de prueba por brazo, sin pregunta de EV2), con freno si fallan R3 o R6; (c) A2.2 con la plantilla de HEAD, declarado como desvío de U-NAV, §5 |
| A-D6, `MAX_MCP_OUTPUT_TOKENS` (§3) | (a) sin fijar, como en el tramo 2, con la anotación de 200.000 caracteres como tope y declarado frente a la §72 y la §79; (b) en 70.000, como dicen la §72 y la §79: según la §96 no actúa con la anotación, y A2.2 corre con una variable que el tramo 2 no tuvo |
| A-D7, las semillas (§4) | el orden de las corridas: `A22:orden_corridas:v1`, aplicada como en el §4, u otra; la auditoría y el orden del juez: (a) las de EV2 tal cual (`auditoria-ev2-v1` y `juez-ev2-v1`); (b) propias con la forma de B6.3 (`A22:auditoria:v1` y `A22:orden_juez:v1`) |
| A-D8, `requiere_adjudicacion` y N = 3 (§4) | (a) la autora las adjudica entre N = 1 y las re-corridas, y una adjudicada «parcial» va a N = 3; (b) el disparo usa solo el veredicto del código, y las `requiere_adjudicacion` se adjudican al final, sin re-corrida, declarado |
| A-D9, la medida y la prueba (§5) | (a) las del pre-registro de B6.3, para que las tasas de Q5 salgan de la misma medida; (b) fijarlas acá: el veredicto por pregunta en dos clases (correcto contra no correcto) y la prueba exacta de McNemar sobre los pares discordantes, unilateral a favor del grafo, con Holm sobre las dos |

El borrador las detalla en su §3 (R5, A-D5 y A-D6), §4 (A-D7 y A-D8), §5 (A-D9), §6 (A-D2) y §7 (A-D4). Las decididas (A-D0, A-D1, A-D3 y
la decisión 3 de Q8) van con su ancla en su §9. Lo que propuse yo, sin decidirlo: la semilla `A22:orden_corridas:v1` y cómo se aplica
(§4 del borrador), y las predicciones (§5 del borrador).

## 6. La foto del repo, los `.pyc` y el grep de convenciones

- **La foto** (`foto_repo.py`: sha256 de cada archivo del repo, sin `.git`; los `.env` y los `NO_ABRIR_*` solo por tamaño y fecha):
  antes, 24/10/2026 09:47:23 (59.082 entradas); después del borrador, 10:11:29 (un nuevo, el borrador, en una versión anterior a las correcciones del §7: sha256 `0b3ea8be…`);
  al frenar, 10:16:07, con este FRENO escrito y sin estas cifras (59.084 entradas: 2 nuevos, el borrador con su sha256 final y este
  FRENO; 0 cambiados, 0 borrados, 0 fuera de las rutas autorizadas).
  `comparar_fotos_c.py` acepta solo las dos rutas nuevas del «seguí».
- **Los `.pyc`:** 10.158 antes y al frenar, 243 fuera de los venvs en las dos; ninguno nuevo fuera de los venvs.
- **El grep de convenciones** (`segmentacion_oficial_e0r2/s0_4/scripts/grep_convenciones.py`, con `LC_ALL=en_US.UTF-8`, sobre copias de
  los dos archivos en la carpeta temporal de la sesión): control positivo 16 de 16; total 0 en el borrador y total 0 en este FRENO.
- Después de escribir estas cifras tomé una foto más: difiere de la de las 10:16:07 solo en este FRENO (está en el paquete).

## 7. Errores propios, con su causa

1. **Un conteo mal en el checkpoint:** escribí «51 anclas» sin contarlas; son 56. Lo vi al recontar con `grep -c '^### '` antes de
   escribir el borrador, y lo corregí en el checkpoint y en su copia permanente.
2. **Tres anclas mal en el primer texto del borrador,** puestas de memoria: la decisión 7 de la §99 (`:3858-3859`, es `:3856-3857`), las
   seis decisiones de A2.1 (`:527-535`, es `:526-535`, y no eran «de esa sección y del §2» sino las de la §14 del FRENO A2.1-a) y el
   máximo de llamadas por sesión, que anclé en la tabla por mensaje del §5 del FRENO A2.1-b en lugar de las del §3 y del §4. Las vi al
   imprimir esas líneas, antes del control por código, y las corregí; los puntos 5 y 6 de la §50 no tenían línea y se la agregué.
3. **Una implicación mal en A-D2:** escribí que con la opción (a) la corrida «no frena» en el escenario medio, sin tener en cuenta que el
   freno del banco es un corte duro (`a2_1/correr_a2_1.py:214-215`) y que en el 75 % del medio corta antes. La corregí después de leer
   esas líneas.
4. **Un `cd` en un comando compuesto** dejó el directorio de trabajo del shell en `data/experiment/banco_mcp/`. No escribió nada; desde
   ahí usé rutas absolutas.
5. **Lo que no detecté en el tramo 2:** no leí U-NAV ni la §76 del registro, así que no vi que la plantilla nueva tenía que ir en el
   despacho del tramo 2 (U-NAV, `:210-212`) ni que el humo y H-B2 tenían que correr con la variable en 70.000 (§76, `:2729-2732`). El
   «seguí» del tramo 2 no traía la plantilla y decía que la variable no se fija. Las 20 sesiones corrieron con la plantilla vieja y sin la
   variable. No lo arreglo: va a la autora (A-D5 y A-D6).

## 8. Cierre

- **En el repo:** dos archivos nuevos, `docs/preregistro_A2_2_sistema_por_fragmentos.md` y este FRENO. Ningún otro cambio (§6).
- **El paquete:** `revision_A2_1_FRENO_c/` en la carpeta temporal de la sesión, con el borrador, este FRENO, las salidas de los
  controles, las fotos enmascaradas, los scripts y su `manifest.txt`; copiado con `ditto` a
  `~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/94968c98-6fa5-449c-954b-42ee7ee26062/scratchpad/revision_A2_1_FRENO_c/`, y verificado
  en la copia contra su `manifest.txt`.
- **El checkpoint:** `checkpoint_A2_1.md`, en la carpeta temporal y en
  `~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/94968c98-6fa5-449c-954b-42ee7ee26062/scratchpad/checkpoint_A2_1.md`.
- **FRENO A2.1-c.** Espero la revisión de la mesa. La firma del pre-registro es de la autora (PENDIENTE).
