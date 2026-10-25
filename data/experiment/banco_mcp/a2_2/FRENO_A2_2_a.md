# FRENO A2.2-a — tramo 1 de A2.2: la corrida preparada y probada en seco

Despacho: el «seguí» del tramo 1 de A2.2 (25/10/2026). Rige el pre-registro FIRMADO, `docs/preregistro_A2_2_sistema_por_fragmentos.md`,
leído en el commit de la firma (`a78ead7b`, HEAD; sha256 del archivo `b113ed43…`). USD 0: ninguna sesión llegó al modelo, ninguna
llamada a la API, ningún comando con el `.env`. En el repo escribí solo en `data/experiment/banco_mcp/a2_2/`, una carpeta nueva; el
volumen de Neo4j, que vive dentro del repo e ignorado por git, cambió por la carga autorizada del grafo (§9). Nada commiteado,
ningún mensaje de commit preparado, nada en la memoria.

**En corto:**

- **La corrida, lista:** la plantilla nueva (un renglón de diff), la configuración de A2.2 con R5 (32, 30 y 1,80), el lanzador, el
  runner (`pruebas`, `n1`, `recorridas` y `orden`), el juez de EV2 envuelto, la población de N = 3, el enmascarado, el análisis, los
  controles y los cinco comandos de los pasos pagos, con sus topes: 93 y 69,75 el agente, 25 y 18,75 el juez.
- **Las pruebas:** el selftest da 34 de 34 y la corrida en seco 30 de 30 ramas, en la copia de trabajo y en la copia final.
- **El grafo y los índices:** el grafo de desarrollo re-sellado, cargado en Neo4j (6.962 nodos y 23.311 aristas, huellas idénticas en
  dos cargas) con su índice full-text en línea; los 9 archivos de `mcp_vector/indice/`, iguales a su respaldo.
- **El aislamiento:** (a) a (d) en PASS en los tres brazos, con el positivo del brazo del grafo (`acb26dca…` desde Neo4j).
- **EV2, por código:** 40 preguntas, 164 criterios, 40 anclas (ninguna fuera de la E0 del grafo) y 0 preguntas con un ancla en la
  cola.
- **Lo que declaro sin arreglar** (§2): la numeración de las repeticiones, el orden del juez por respuesta y las otras decisiones de
  aplicación que el pre-registro no fija; y que en el repo cambió, además de `a2_2/`, el volumen de Neo4j.

## 0. Paso 0 (25/10/2026, 11:54 -0300, con `$HOME`)

```
$ pwd
$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg
$ git log --format='%h %s' -8
a78ead7b Preregistro de la comparacion del grafo contra el sistema por fragmentos FIRMADO por la autora el 25/10/2026 (version para firmar en 562f1c55)
562f1c55 Registro de decisiones y preregistro de la comparacion con los fragmentos: la version para firmar, con el tope del agente y el del juez por la regla del alto, la medida confirmada y la cola por anclas
3b6f63c1 Registro de decisiones y preregistro de la comparacion con los fragmentos: el tope, la plantilla, las semillas y la medida decididos, la cola del grafo de desarrollo ubicada y la revision de B6.3 por olas
206c3f59 Banco del brazo de fragmentos: el borrador del preregistro de la comparacion del grafo contra los fragmentos y el FRENO del tramo 3, tal como los entrego la ejecutora
9826b625 Registro de decisiones: los 13 lugares sin pregunta de B6.3 en el documento siguiente de su clase con menos de 4, la generacion y la etapa b del juez v2 en marcha y la revision de las tres olas
ecc7a02b Registro de decisiones y nota del banco: R5, el tope y las sesiones de A2.2 decididos, la iteracion 1 del juez v2, las olas 2 y 3 de B6.3 y las sesiones enmascaradas desde el tramo 2
af4dab8e Registro de decisiones: la primera ola de preguntas de B6.3 decidida, los pasos pagos del tramo 2 del banco verificados con sus sesiones enmascaradas, el tope de turnos y la etapa T revisada
7a9fe8ca Banco del brazo de fragmentos: el humo de las dos configuraciones y la caracterizacion del tope de turnos del tramo 2, con las transcripciones y los streams enmascarados
$ git rev-parse --abbrev-ref HEAD
main
$ git status --porcelain --untracked-files=no
$ git status --porcelain --untracked-files=all -- data/experiment/banco_mcp
$ ls -d data/experiment/banco_mcp/a2_2
ls: $HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg/data/experiment/banco_mcp/a2_2: No such file or directory
$ git diff --name-only HEAD~1 HEAD
docs/preregistro_A2_2_sistema_por_fragmentos.md
$ git show HEAD~1:docs/preregistro_A2_2_sistema_por_fragmentos.md | shasum -a 256
2a75f40000c1647e567d58db08b52735dcc5e0ac898d93786b98fe6cda2ac0b1  -
$ git show HEAD:docs/preregistro_A2_2_sistema_por_fragmentos.md | sed -n 1,3p
# Pre-registro de A2.2: el grafo contra el sistema por fragmentos, sobre EV2

**FIRMADO por la autora el 25/10/2026** (versión para firmar commiteada en `562f1c55`; no sellado como medición: ningún número
$ git show HEAD:<ruta> | shasum -a 256
1d58733699c325c90510e1ead5f18eac6c3cd970ee3b0ab7ff141da539162b40  data/experiment/exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json
b4a74ba536dd5938aa0935ee088e8327bbad411229679887177653a698421236  data/experiment/ev2_juez/juez.py
fd446f8e61f46033d7de9b862121c698b2c52dcc2696b7f10993f44e509f5455  data/experiment/ev2_juez/prompt_juez_v1.md
c905dd1a510925bad7a324722ff593ded09a95e77629e0a7e90fa13d5f3e6660  data/experiment/ev2_juez/mapping.py
acb26dca0885e9ea83ab02637f15c1dac57885f0cf017c5fb16173ac7dfcac31  data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo_r2b_rs1/r2/kg.json
a7342c262b4b90a5b8adb65bacaa93983f1e2c478c80761ca06b8b7bcf38a55d  data/experiment/controles_a2_2/cola_grafo_desarrollo_r2b_rs1_mesa.json
9c5aaab54f8f7e4c18d95cb6233af1e99399f0f695fbf0a5946afdf56758d013  data/experiment/banco_mcp/agentes/plantilla_prompt.txt
```

Todo dio lo esperado: `main`; sin cambios rastreados; `banco_mcp/` limpio; `a2_2/` no existía; el último commit es el de la firma
y el anterior, la versión para firmar; el diff de la firma trae solo el pre-registro; el sha256 de HEAD~1 del pre-registro y los
siete de HEAD son los del despacho. La foto del repo de antes es de las 11:55:57 (§9).

## 1. Lo que leí y lo que no abrí

- **Del repo, en HEAD:** el pre-registro firmado; el banco de A2.1 (`correr_a2_1.py`, `lanzar_agente_a2_1.py`,
  `corrida_en_seco_a2_1.py`, `enmascarar_cwd_a2_1.py`, `test_aislamiento_a2_1.py`, `sonda_auditoria.py`, `con_clave_del_entorno.py`,
  los zsh del tramo 2 y su configuración); el banco de U-A2.0 (`agentes/lanzar_agente.py`, las configuraciones y los JSON de MCP,
  `cliente_falso.py`, `aislamiento/test_aislamiento.py`, la plantilla); los servidores de los dos brazos (su arranque y sus sellos);
  `scripts/control_sdk_anthropic_juez_y_banco.py`; `data/experiment/neo4j/` (README, docker-compose, `conexion.py`, `cargar_kg.py`,
  `indices.py`, `grafos.py`); `evaluacion/llm_cache.py` (su interfaz); la lista de la cola y su script; la E0 r2b de desarrollo; los
  manifiestos de los índices; y el registro (§9, §16, §50, §51, §72, §76, §79, §94, §96, §99, §105 y §106).
- **De las carpetas `ev2_*`, solo código `.py`:** `ev2_juez/juez.py` y `mapping.py`; `ev2_encadenamiento/code/` (`agregacion_enc.py`,
  `comun_enc.py`, `juez_enc.py`); `ev2_fidelidad_eval/code/` (`comun_fidelidad.py`, `pipeline_fidelidad.py`); `ev2_corrida/code/comun_ev2.py`
  (sus líneas de nivel de módulo); y, para el formato de las anclas, `banco_mcp/smoke/verificar_territorio.py` y
  `bakeoff_embeddings/code/mapeo_gold_chunk.py`. Una vez, por error, más que eso (§10, error 1).
- **EV2:** `preguntas_ev2_fidelidad.json` lo leyó solo mi código (el orden, el control del punto i y la carga de las preguntas), sin
  imprimir nada de su contenido: la salida del orden da la cuenta y la del control, solo cuentas.
- **Fuera del repo:** el respaldo de los índices (`fuera_del_repo/indices_banco/…/manifest_respaldo.txt`, sus sha256) y, por código, el
  `.claude.json` de las carpetas de configuración de las sesiones (solo `tengu_velvet_ibis`, como en el tramo 2).
- No abrí ningún `.env`, `.claude.json` a mano ni `NO_ABRIR_*`, ni las carpetas vedadas (§10, error 2: una ruta de una de ellas
  apareció en la línea de comando de un proceso).

## 2. Lo ya decidido, cómo lo apliqué y lo que fijé yo

El pre-registro manda; el despacho no lo contradice en nada. Lo que el pre-registro no fija y tuve que fijar para escribir el código
va acá, declarado; ninguna de estas decisiones cambia lo que se mide:

1. **Las repeticiones:** r1 es N = 1 y r2, r3 y r4 son las tres re-corridas; el orden de los brazos de cada repetición sale de
   `random.Random(f"A22:orden_corridas:v1:{id}:r{r}")` con esa r (§4). Los ids de sesión: `PRB-<brazo>`, `N1-<pregunta>-<brazo>` y
   `RC1…RC3-<pregunta>-<brazo>`.
2. **Las pruebas de A-D5:** con la pregunta SMK-01 del smoke del tramo 2, los tres brazos en el orden de sus nombres.
3. **El juez, por respuesta:** sus tres repeticiones corren seguidas, cada una con su caché y su etiqueta (como EV2), porque el corte
   del juez del §6 se mide «antes de cada respuesta». EV2 corría por pasada.
4. **Los ids opacos del juez:** `A22J-` + sha256(`A22:id_opaco_juez:v1`|pregunta|brazo|repetición|sha256 de la respuesta)[:10], con la
   repetición en la clave como `comun_enc.py`. El orden ciego, por etapa, con `A22:orden_juez:v1`.
5. **«El costo mayor de una respuesta ya juzgada»** es la suma de sus tres llamadas, desde sus tokens y los precios del juez
   (3,00 y 15,00 por millón: `run_1_cookbook/code/common.py:207`, igual que la tabla de modelos de la referencia de la API); 0,0378
   mientras ninguna respuesta tenga las tres.
6. **Lo que se juzga:** las sesiones completas por R3 con una respuesta en su JSON final. Una respuesta sin veredicto (una salida mal
   formada del juez) no dispara N = 3 y queda sin veredicto final, con su sensibilidad (§5 del pre-registro).
7. **La cola (A-D11):** un ancla «to:punto» se resuelve sobre la E0 r2b de desarrollo como en el bake-off (la unidad igual al punto,
   o las que descienden de él). La lista de la cola trae una parte de la extracción, `cap::4.2.1.2::parte1`; la cuento como su unidad
   de E0, `cap::4.2.1.2`.
8. **Las adjudicaciones de la autora** (A-D8) entran al análisis por id opaco, en un JSON aparte.
9. **El análisis no imprime resultados** ni el juez imprime veredictos, ni siquiera su distribución: la autora lee a ciegas las 20 de
   verificación (Q8, `:61-63`). El análisis corre después de los pasos pagos; no es uno de ellos.
10. **El intérprete del servidor del grafo** va en la sesión como `BANCO_PYTHON_KG`, igual que `BANCO_VENV_VECTOR` en los de fragmentos:
    en el repo es el `.venv` del repo, el mismo que fija `agentes/mcp_kg.json`; solo una copia sin `.venv` lo toma del entorno.
11. **El entorno:** cada paso corre desde `env -i`, con PATH, HOME, el venv de fragmentos, el modo sin red del modelo y, si la Terminal
    la trae, NEO4J_URI. `MAX_MCP_OUTPUT_TOKENS` no pasa nunca (A-D6) y `JUEZ_PROMPT_VERSION` frena el juez.
12. **El tiempo por sesión:** 1.800 s (A2.1 usaba 900, con 12 rondas); con R5 una sesión puede tener 32.
13. **Las sesiones init del aislamiento** corren fuera del repo, como la de A2.1 (registro, §16, decisión 6): al repo van sus metas,
    comandos, prompts, logs y stderr, y el test frena si alguno trae una ruta de la máquina.
14. **Las copias del repo** llevan, además de las exclusiones de la cláusula, la del volumen de Neo4j (`data/experiment/neo4j/volumen`,
    1,8 GB de base de datos).
15. **La corrida en seco** tiene variables que solo existen para ella (`A22_*`); la del patrón de `pgrep` rige solo con `A22_MODO=init`.

## 3. Los archivos de `a2_2/`

**El código y la configuración** (los de `sha256_tramo1_a2_2.txt`, que controlan las guardas de los cinco pasos):

| archivo | sha256 | qué hace |
|---|---|---|
| `analizar_a2_2.py` | `230f0c897fcafd838712256442ae543c71056ac8b9bd416952c68e909031b6d2` | el análisis del §5: el veredicto final por pregunta y brazo, la prueba exacta de signos de dos colas con Holm, la cifra sin la cola, los pares discordantes, c_agente, las predicciones y lo operativo de R5; escribe analisis/analisis_a2_2.json y no imprime resultados |
| `comun_a2_2.py` | `81dcc23c7121186bf2df03361eace0a4b480d657f4926dd3bd643f33816fb64e` | rutas, brazos, semillas, topes y precios del juez; la carga de EV2 por código; el orden y la secuencia de cada etapa; el control de las entradas |
| `config_agentes_a2_2.json` | `fd4ce4e4ce7d4c7cd0550af1ed2ba7d2cbd3d1a2301ee82060ba7d6eba4697c0` | la configuración de A2.2 (R10): la de A2.1 con el brazo del grafo re-sellado, la plantilla nueva y R5 (32, 30 y 1,80) |
| `control_ev2_a2_2.py` | `e32acad69984e6ab2b1b2b02b244470256ef48581ceb79778557af5be8fce143` | el control del punto i: solo cuentas de EV2 (preguntas, criterios, anclas, anclas fuera de la E0, preguntas en la cola) |
| `controles_a2_2.py` | `c96b586ceebe9769d98670437f6e29104cc74abcf535150ae0818a64d0851b7e` | los controles externos: los 9 archivos de mcp_vector/indice/ contra su respaldo y sus configuraciones, y el grafo en Neo4j |
| `correr_a2_2.py` | `2cdc10fbcced5d382d3b524a8d63e7729cc2444de81d7046a9b4775f58839c6d` | el runner del agente: pruebas, n1, recorridas y orden; el corte del agente; el control del disco y el valor remoto de A2.1 |
| `corrida_en_seco_a2_2.py` | `acc43f4616b4bf2fd94234a8f046e458681094a3d5c9f17f6db652a1d1d5feed` | la corrida en seco: las ramas del runner, del juez, de la población, del análisis y del enmascarado, y los cinco comandos; el cliente falso del juez |
| `enmascarar_cwd_a2_2.py` | `1c24f71f01afe72f27ef07ee2317d646c94d684931e530a1da89200b70b6b34e` | el enmascarado de las sesiones (A-D4): el de A2.1 con las carpetas de A2.2; al aplicar, resguarda antes los originales fuera del repo |
| `guardas_a2_2.zsh` | `f38fde9576eeebc68caff5f6c7de7b51e1d8772c673401885269c056c100802c` | las guardas de los cinco pasos: los sha256 del tramo, pgrep, la lista cerrada y el control del SDK |
| `juez_a2_2.py` | `3efa06c068ae60adb10334dd2f563b2043b16cf37722ff72b48a0d9d03a5dac3` | el juez de EV2 envuelto: la entrada ciega, el orden con A22:orden_juez:v1, N = 3 con una caché por repetición, el corte del juez y el control del SDK |
| `lanzar_agente_a2_2.py` | `c498271e7f2a163f78ab5b789c01773bdd8ef80789807e4c0ccc18b2d927f662` | el lanzador de una sesión de A2.2: el de A2.1 con la configuración de A2.2, los tres brazos y BANCO_PYTHON_KG |
| `mcp_kg_rs1.json` | `0951dec39f5d06db2649133bba1bde5754203f8f8c177e5a3981d19de68ade44` | el JSON de MCP del brazo del grafo, con la configuración del grafo re-sellado |
| `orden_corridas_a2_2.json` | `0d77a499aa7a85f7093ec2bf91f5559d5b379d0b0afb50d0b2772332723a21bf` | el orden del §4, escrito antes de correr: solo ids de EV2 y nombres de brazos |
| `paso1_pruebas.zsh` | `0032d472c678984296bf34f89b9070a86163410375a4092014d97174d0562312` | paso 1 (pago): las tres sesiones de prueba de A-D5 |
| `paso2_n1.zsh` | `9098e8d8fe109e644bf338bd27853bb06ca57f7be38d7fa2b351601afcbbe7f2` | paso 2 (pago): N = 1 de las 40 preguntas en los tres brazos |
| `paso3_juez_n1.zsh` | `bc9d8adffc4520636d6680db358f62528371129f4a9c7fd8af8af31d3b667082` | paso 3 (pago): el juez de N = 1 y la población de N = 3 |
| `paso4_recorridas.zsh` | `9894f24eabe280b5916639995ac9b639ba38504f03e896d03534298d86bc4b42` | paso 4 (pago): las tres re-corridas de cada par de la población |
| `paso5_juez_recorridas.zsh` | `a9c42d506fdf09ed41ae9a33d433bc070f2366f4a63cf1de33542b0da14c58f1` | paso 5 (pago): el juez de las re-corridas |
| `plantilla_prompt_a2_2.txt` | `ff6c3d0a46c1ef5348bb824d93062658e8137374e3d0d5c2772af4fdc5372ab9` | la plantilla nueva (A-D5): la de HEAD sin el paréntesis de los cinco TOs |
| `poblacion_a2_2.py` | `c74ac60bf0bcf7531384ae54b7e500aadfb7b4cf2af43973f038fce51359f2c3` | la población de N = 3 (el disparo por «parcial», la auditoría con A22:auditoria:v1) y la agregación de las re-corridas con agregacion_enc.py de EV2 |
| `selftest_a2_2.py` | `8881ac0694694c72c2dbe70178269a82c34c5d4f7e9424356ff067f267d47192` | el selftest de las funciones que no lanzan sesiones |
| `sellos_entrada_a2_2.json` | `540fe1edc8b44c60e12e97d0483b2bc342ba63a3e468c3d8e679d86412da2894` | las 41 entradas que A2.2 usa sin editar, con su sha256 de HEAD |
| `test_aislamiento_a2_2.py` | `813b38236789cd9bb5476a89f8fab8015c90514538f93f81036450e2daffa7f3` | el aislamiento (a) a (d) de los tres brazos, en modo init y con el cliente falso |
| `sha256_tramo1_a2_2.txt` | `4722dac9fb408abd4dfbc58bb71b7a4a4bab1b8815917d47158ad21b4c26695c` | la lista de los sha256 de los 23 archivos de arriba (no se incluye a sí misma) |

**Las salidas del tramo** (no están en la lista; son resultado):

| archivo | sha256 |
|---|---|
| `aislamiento/aislamiento_a2_2.json` | `a1aa253d44bb4a2447708f6b2e22193d3d0ea779ccb78a47597615bf3a1d8158` |
| `aislamiento/init/comando_AISL-fragmentos_bm25.json` | `d2780251b412e658ee25fe277d34223c3d3a969d7fa31c375cbb27609f2b0bec` |
| `aislamiento/init/comando_AISL-fragmentos_denso.json` | `16793fa2077dcb14ce19d039388666567c48103081fb808725edd56bbc6d0531` |
| `aislamiento/init/comando_AISL-kg.json` | `e765d4bc9ef832f735d452b0878882d33abf45778c7f8f63d0a27054488a0e74` |
| `aislamiento/init/log_r1_AISL-fragmentos_bm25.jsonl` | `cf9665ec0e39a8916d0d5fb477d12193edab7f7b6be2ce2b59ec19fb50872c2b` |
| `aislamiento/init/log_r1_AISL-fragmentos_denso.jsonl` | `5a212402b9dce85e11b1db73312c9cc64f2b596634286ed7ad799b00f92f5b16` |
| `aislamiento/init/log_r1_AISL-kg.jsonl` | `c7a3e6ddb1037e04f08f8c8bb0ceadea8958b3e4ea4ba0e518c4382a32b551e9` |
| `aislamiento/init/meta_AISL-fragmentos_bm25.json` | `fe22366dc38660c52a5307543a5c49fd8c612adfe06db04b10bce2408736be80` |
| `aislamiento/init/meta_AISL-fragmentos_denso.json` | `e0f77753114c5d9f87cca36696343476151334420acd7850fcb73492eb51b8bf` |
| `aislamiento/init/meta_AISL-kg.json` | `9342c1eb61a5b695072e4f76b4a20555d5a4dfa31c355cf2998c0fec9b964f47` |
| `aislamiento/init/prompt_AISL-fragmentos_bm25.txt` | `56e72dce510b8c5121bde4176e14a076b636f08f1e4e2adcc357791dfd693f45` |
| `aislamiento/init/prompt_AISL-fragmentos_denso.txt` | `119d44b72cd0e5bc6735b9c091e01d1c977b25070c597f3302d210b3f843815a` |
| `aislamiento/init/prompt_AISL-kg.txt` | `b27a2ac242a8acb9cf29c7a9cf32d3463f2f784bb8eef0fccb68416317c9ba63` |
| `aislamiento/init/stderr_AISL-fragmentos_bm25.txt` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `aislamiento/init/stderr_AISL-fragmentos_denso.txt` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `aislamiento/init/stderr_AISL-kg.txt` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `aislamiento/log_r1_auditada_fragmentos_bm25.jsonl` | `b06707d8458f1de0b385baa1ec71ca4e27dc350b6c95f7f34328cedae902680a` |
| `aislamiento/log_r1_auditada_fragmentos_denso.jsonl` | `fef0ff7ae4ec3da6b13096c55584d53be03cacacb09f94515b5958b39067ff28` |
| `aislamiento/log_r1_auditada_kg.jsonl` | `57bf9f6c5b73132a4020c046179a653f9bfafebb26cf09d1523c09d5e36a0fdc` |
| `aislamiento/log_r1_positivo_fragmentos_bm25.jsonl` | `2d9708f6d0e811c1774ff30947d9efb5ee1946d02ccede502f86a15b9eb04c47` |
| `aislamiento/log_r1_positivo_fragmentos_denso.jsonl` | `2cd7a5812587726f3990852a84a83111ce2bfc02ac62bd25813aea4ed1380837` |
| `aislamiento/log_r1_positivo_kg.jsonl` | `85d1290855711631356330e3cb5465a73a6055775600711e92c322ad3df38751` |
| `controles/control_ev2_a2_2.json` | `de31558f778706d31952ab2700a1087df4b6d6d46bdfd05945a6880ecc7bec04` |
| `controles/controles_externos_a2_2.txt` | `de81b5be0246ef0b8a40ff6b268cbef18b980750b77a1896da175f230926f2d6` |

## 4. La plantilla y R5

**El diff de la plantilla** contra la de HEAD (`agentes/plantilla_prompt.txt`, `9c5aaab5…` → `a2_2/plantilla_prompt_a2_2.txt`,
`ff6c3d0a…`): un solo renglón, el primero, que pasa al texto de U-NAV, §5 (`:203-204`). El tope sigue en `{{TOPE_TOOL_CALLS}}`.

```
1c1
< Sos un agente que responde preguntas sobre la normativa del BCRA (Textos Ordenados: capitales mínimos, clasificación de deudores, exterior y cambios, protección de usuarios de servicios financieros y régimen informativo contable mensual), usando EXCLUSIVAMENTE la evidencia que recuperes con las tools disponibles en esta sesión.
---
> Sos un agente que responde preguntas sobre la normativa del BCRA (sus Textos Ordenados), usando EXCLUSIVAMENTE la evidencia que recuperes con las tools disponibles en esta sesión.
```

**R5 en `config_agentes_a2_2.json`** (`corte_R5`): `max_turns` 32, `tope_tool_calls_en_prompt` 30 y `max_budget_usd_por_sesion` 1,8,
iguales en los tres brazos; la configuración nueva tiene sha256 `fd4ce4e4…` (la de A2.1, su base, `2f6b60e2…`).

## 5. Los tests y la corrida en seco

**El selftest** (`selftest_a2_2.py`), en la copia final, 34 de 34:

1. orden: determinista e independiente del orden de entrada
2. orden: cada repetición de cada pregunta es una permutación de los tres brazos
3. orden: las preguntas con random.Random('A22:orden_corridas:v1').shuffle sobre los ids ordenados
4. orden: los brazos con random.Random(f'A22:orden_corridas:v1:{id}:r{r}')
5. secuencia: 3 pruebas (una por brazo, ordenadas) y 30 de N = 1
6. secuencia de re-corridas: por repetición (r2, r3, r4), 2 pares × 3 = 6, ids RC1..RC3
7. auditoría: la misma muestra que la función de EV2 con la semilla de A2.2 (4 casos)
8. auditoría: max(ceil(10 % · n), 1) y 0 sin correctos
9. población: dispara solo «parcial» del código (requiere_adjudicacion no)
10. población: la auditoría por brazo y P = parciales + auditadas
11. agregación (agregacion_enc): mayoría, empate triple a parcial, pendiente invariante y dependiente, incompleto
12. prueba exacta: 10 discordantes a favor → p = 2/1024
13. prueba exacta: 5 a favor y 0 en contra con ceros → p = 2/32
14. prueba exacta: sin discordantes → 1; 1 y 1 → 1; 8 contra 2 → 0,109375
15. Holm: la primera a 0,025, la segunda a 0,05; se detiene en la primera que no rechaza
16. Wilson: 0 de 10 → [0; 0,2775] y 5 de 10 → [0,2366; 0,7634] — [0.0, 0.277533] [0.236593, 0.763407]
17. resolución de anclas: exacta, por descendientes y ninguna
18. cola: sale una pregunta si alguna de sus anclas cae en la cola; una parte cuenta como su unidad
19. análisis: el grafo supera a BM25 (10 a 0, p = 0,00195) y no al denso (2 a 0): sin afirmación general
20. análisis: con los dos en 10 a 0, el grafo supera a las dos y vale la afirmación general
21. análisis: lo sin veredicto final sale (n = 10) y la sensibilidad lo cuenta como 0 (n = 12)
22. análisis: una adjudicación de la autora reemplaza a la requiere_adjudicacion
23. análisis: un par de la población toma el agregado de sus re-corridas, no el de N = 1
24. predicciones: el sentido observado de incorrectos, latencia y costo
25. R5 operativo: al tope (≥ 30) 2, pasan de 30 1, cortadas 1, de 4
26. juez: el orden ciego es determinista, con ids opacos únicos
27. juez: la ceguera da 0 fugas en la vista ciega y frena con un campo de más
28. juez: las marcas de brazo en las respuestas se cuentan, sin editarlas
29. juez: modal por criterio y mapping de EV2; una respuesta sin sus tres repeticiones queda incompleta
30. juez: el costo de la primera respuesta, 0,0378; después, el mayor de las juzgadas
31. enmascarado: calcular, probar y aplicar; la carpeta personal pasa a $HOME y el original queda afuera — 2 archivos, 3 reemplazos | 2 archivos enmascarados, cada uno con el sha256 revisado; sus originales, fuera de la raíz
32. enmascarado: después de aplicar, probar frena (los archivos ya no son los originales)
33. control de EV2: cuenta preguntas, criterios, anclas fuera de la E0 y preguntas en la cola — {"a": 2, "b": 0, "ninguna": 1}
34. EV2: la corrida real no acepta otro archivo

**La corrida en seco** (`corrida_en_seco_a2_2.py`), en la copia final, 30 de 30 (las ramas en Python, con sesiones sintéticas y el
cliente falso del juez; los comandos, con el CLI en modo init y el juez en seco):

1. pruebas: las tres en verde (R3 y R6)
2. pruebas: una que falla R6 frena con FrenoPruebas (código 4)
3. N = 1 sin las pruebas: FrenoPrecondicion (código 5)
4. N = 1 con las pruebas de otra carpeta en rojo: FrenoPrecondicion
5. N = 1: las 12 sesiones, en el orden del pre-registro
6. una meta de otro modo aborta la corrida
7. el corte del agente: 68,00 + 1,80 > 69,75 frena sin lanzar, sumando las metas de las tres carpetas
8. el corte del agente: con 67,92 la primera se lanza (69,72 ≤ 69,75) y frena la segunda (69,77) — 1 lanzadas
9. el freno del disco: una referencia a disco frena (código 3), y al reanudar vuelve a frenar sin lanzar
10. juez N = 1: la cortada y la mal formada del agente quedan fuera (incompletas por R3)
11. juez N = 1: una salida mal formada del juez queda incompleta y una dudosa da requiere_adjudicacion — {"correcto": 3, "requiere_adjudicacion": 2, "parcial": 2}
12. juez N = 1: el control del SDK corrió primero y dio OK
13. juez N = 1: la tabla de desanonimización aparte y el orden ciego sin brazos ni preguntas
14. el corte del juez: con freno 0,05 frena antes de pasarlo (acumulado más el mayor juzgado, 0,0378 sin ninguno) — 6 llamadas, USD 0.036
15. el juez sigue desde lo hecho: la reanudación no repite ninguna llamada
16. población: derivada del juez de N = 1 — 5 pares
17. re-corridas: 3 por par de la población, por repetición
18. re-corridas: un voto requiere_adjudicacion entre dos correctos deja el par decidido (invariante)
19. análisis: corre sobre la salida sintética, con lo sin veredicto final listado y R5 por brazo — 7 sin final
20. enmascarado de las sesiones: calcular, probar y aplicar con los originales fuera de la raíz
21. guardas: un sha256 que no da frena con el código 6 — 2/analizar_a2_2.py: FAILED
22. guardas: otro paso pago corriendo frena con el código 7
23. paso 1 (init): las tres pruebas sin resultado fallan R3 y el comando frena con el código 4 —  acumulado 0.0000
24. paso 2 con las pruebas en rojo: frena con el código 5 — FRENO DE PRECONDICIÓN: una sesión de prueba falla R3 o R6: el paso 1 frenó
25. paso 2 (init): las 6 sesiones de N = 1 de las 2 preguntas sintéticas — sesiones nuevas, 0 completas; gasto de A2.2 R9 0.0000 (CLI 0.0000); freno 69.75, tope 93.0
26. paso 3 (seco): el control del SDK, el juez de N = 1 y la población — o del juez 0.0720
27. paso 3: no imprime ningún veredicto ni brazo
28. paso 4 (init): las re-corridas de la población, 3 por par — 15 sesiones; LI 0.0000); freno 69.75, tope 93.0
29. paso 5 (seco): el control del SDK y el juez de las re-corridas — umulado del juez 0.0720
30. enmascarado de las sesiones init de los comandos: calcular y probar — 24 archivos, 24 reemplazos | PRUEBA: 24 de 24 originales y sus versiones enmascaradas dan lo revisado; no esc

Las veces anteriores que corrió, con lo que la hizo fallar, están en el §10 y en el paquete.

## 6. La carga, el aislamiento y los índices

- **Neo4j:** el contenedor `neo4j-bcra-kg-compose` estaba detenido; lo levanté con `docker compose -f data/experiment/neo4j/docker-compose.yml
  up -d --wait` (12:18:37 a 12:18:57, sano). El grafo de desarrollo re-sellado ya estaba cargado (el control dio OK antes de cargar).
  La carga (`cargar_kg.py --grafo KG_Tanda0_Desarrollo_r2b_rs1 --verificar-idempotencia`, desde la copia de trabajo, 12:19:18 a 12:19:33):
  sha256 verificado; 6.962 nodos y 23.311 aristas, 0 colgantes, 0 hacia otro grafo; el muestreo de 20 nodos; las huellas de estado de
  las dos cargas, idénticas; la de contenido, igual a la del loader; VERIFICACIÓN OK. `indices.py --grafo KG_Tanda0_Desarrollo_r2b_rs1`:
  el índice `nodos_fulltext_kg_tanda0_desarrollo_r2b_rs1` en línea (sus tests dirigidos son de otro grafo: BKL-0003 N/A, BKL-0027 OK).
  El contenedor queda levantado para los pasos pagos; si se lo baja, el paso 1 frena por la precondición del grafo.
- **El aislamiento** (`test_aislamiento_a2_2.py`, en el repo, 12:40:49 a 12:41:18): en los tres brazos, (a) a (d) en PASS. (a) el inventario de cada uno es el suyo (las tres tools del grafo, o `mcp__fragmentos__buscar_pasajes`), su servidor connected, dontAsk y el CLI 2.1.241; (b) ningún servidor importa los módulos ni abre los archivos del otro brazo, `import neo4j` falla en el venv de fragmentos y el BM25 no abre el modelo (el denso abre 62 archivos de su modelo, desde la caché local); (c) los servidores de fragmentos crean solo sockets AF_UNIX, y el del grafo resuelve `localhost` y se conecta solo a `127.0.0.1:7687`; los únicos subprocesos son `uname` y `file`; (d) el positivo de cada brazo por el mismo JSON de MCP: 3 resultados, el del grafo desde Neo4j con `acb26dca…`, el BM25 con su índice `6b5da8b0…` y el denso con su matriz `828caeff…`. Las sesiones init corrieron fuera del repo (`~/INGENIERIA IA/TESIS/fuera_del_repo/banco_sesiones/aislamiento_a2_2/20261025T124050/`). En la copia de trabajo había dado lo mismo (12:22:45), después de corregir el criterio de (a) (§10).
- **Los índices y el grafo** (`controles_a2_2.py`, en `a2_2/controles/controles_externos_a2_2.txt`): los 9 archivos de
  `mcp_vector/indice/` dan el sha256 de su respaldo y el manifiesto del respaldo es el que copia el control; el índice BM25 es el de
  su configuración (`6b5da8b0…`) y la matriz densa, en float32, la de la suya (`828caeff…`); en Neo4j, KG_Meta con `acb26dca…`,
  6.962 nodos con su label y 23.311 aristas, y el índice full-text en línea. El runner los repite antes de cada paso.

## 7. Las cuentas de EV2 (el punto i)

`control_ev2_a2_2.py`, en el repo (salida en `a2_2/controles/control_ev2_a2_2.json`):

```
preguntas 40; criterios 164
anclas: 40 (distintas 40); por vía, instancias {'a': 33, 'b': 7, 'ninguna': 0}, distintas {'a': 33, 'b': 7, 'ninguna': 0}
anclas que no están en la E0 del grafo: 0 (distintas 0); ids de la cola 54, de ellos partes 1; ids de la cola que no están en la E0 1, unidades 0
preguntas con alguna ancla en la cola: 0; sin ninguna: 40
control de EV2: OK
```

Las 40 anclas se resuelven en la E0 del grafo (33 por la unidad igual al punto y 7 por sus descendientes); ninguna pregunta tiene un
ancla en la cola, así que la cifra sin la cola va a ser la de las 40.

## 8. Los cinco comandos

Los corre la autora desde la Terminal, en la raíz del repo, uno después del otro y nunca al lado de otro paso pago. Cada uno controla
el sha256 de todo lo de este tramo y frena (código 6) si algo cambió; frena (código 7) si ve otro paso pago con `pgrep`; corre desde
`env -i` con la lista cerrada; frena (código 5) si el paso anterior no está completo; e imprime solo cuentas y costos. Los costos,
con los de la nota de la mesa (el del grafo, del modelo de la §181: NO VERIFICADO):

| comando | qué hace | tope y freno | costo estimado (central / medio / alto) |
|---|---|---|---|
| `paso1_pruebas.zsh` | las tres sesiones de prueba; frena además (código 4) si una falla R3 o R6 | agente: 93 y 69,75 | 0,13 / 0,23 / 0,42 |
| `paso2_n1.zsh` | N = 1: 40 preguntas × 3 brazos | agente: 93 y 69,75 | 5,24 / 9,09 / 16,80 |
| `paso3_juez_n1.zsh` | el control del SDK, el juez de N = 1 (N = 3) y la población | juez: 25 y 18,75 | 4,54 (120 × 3 × 0,0126) |
| `paso4_recorridas.zsh` | las tres re-corridas de cada par de la población | agente: 93 y 69,75 | con P = 40: 15,71 / 27,28 / 50,40 |
| `paso5_juez_recorridas.zsh` | el control del SDK y el juez de las re-corridas | juez: 25 y 18,75 | con P = 40: 13,61 |

En total, en el peor caso, el agente 67,62 (161 × 0,42; con el margen de 1,80, 69,42) y el juez 18,14, como el §6 del pre-registro.
Después de los cinco: el enmascarado de las sesiones (`enmascarar_cwd_a2_2.py --calcular`, `--probar` y `--aplicar`, con los
originales en `fuera_del_repo/banco_mcp_originales_A2_2/`), la lectura a ciegas de las 20 (Q8), las adjudicaciones y el análisis
(`analizar_a2_2.py`). Ninguno de esos cuatro es pago.

## 9. La foto del repo, los `.pyc` y el grep

- **La foto** (`foto_repo.py`: el sha256 de cada archivo del repo, sin `.git`; los `.env` y los `NO_ABRIR_*`, solo por su tamaño y su fecha): antes, 25/10/2026 11:55:57 (59.086 entradas); antes de escribir este FRENO, 12:44:00 (59.132). La diferencia (`comparar_fotos_a22.py`): 48 archivos nuevos en `a2_2/` (los 24 del §3, los 22 del aislamiento y los 2 de controles); en el volumen de Neo4j, 18 nuevos, 20 borrados y 86 cambiados, por levantar el contenedor y por la carga; fuera de eso, 0. Ningún archivo rastreado cambió (`git status --porcelain --untracked-files=no`, vacío). El despacho pedía que cambiara solo `a2_2/`: el volumen es la única diferencia, ignorada por git, y es consecuencia de la carga autorizada. Una foto más, tomada después de escribir este FRENO, difiere de la de las 12:44:00 solo en él y en el volumen (en el paquete).
- **Los `.pyc`:** 10.158 antes y después, 243 fuera de los venvs; ninguno nuevo.
- **El grep de convenciones** (`segmentacion_oficial_e0r2/s0_4/scripts/grep_convenciones.py`, con `LC_ALL=en_US.UTF-8`, sobre copias de los 48 archivos de `a2_2/` y de este FRENO en la carpeta temporal): control positivo 16 de 16; total 0. Antes había dado 1: el literal de la carpeta temporal del sistema en el control de rutas de `test_aislamiento_a2_2.py`, que reescribí (§10).

## 10. Errores propios, con su causa

1. **Un grep que leyó de más en EV2:** al buscar el ancla del precio del juez, mi patrón incluyó archivos `.md` de carpetas `ev2_*` e imprimió una línea de cada uno de varios reportes y checkpoints de EV2 (precios, topes, el modelo y el sha256 del prompt del juez; ningún veredicto, tabla ni traza). El despacho dice que de esas carpetas leo solo código `.py`. Causa: armé el patrón de búsqueda sin restringirlo a `.py`.
2. **Una línea de comando de un proceso ajeno:** para entender por qué la guarda de `pgrep` frenaba, corrí `pgrep -fl` con el patrón y vi la línea de comando de tres procesos del juez v2 de otra unidad, que corrían en la máquina: su ruta, dentro de una carpeta vedada, y sus argumentos. No abrí la carpeta. Causa: `pgrep -fl` muestra la línea entera; bastaba con `pgrep -f` y la cuenta.
3. **El criterio (a) del aislamiento, mal planteado:** la primera corrida (12:21:39) dio (a) FAIL en los dos brazos de fragmentos porque comparé cada configuración contra la otra, y las dos comparten su tool por diseño (registro, §16, decisión 1). Lo corregí: el otro brazo del grafo son los fragmentos, y viceversa.
4. **Una expectativa mal en el selftest:** la prueba de Holm esperaba que p = 0,03 no rechazara en segundo lugar, cuando a 0,05 rechaza. El código estaba bien; corregí la prueba.
5. **El control del SDK con un intérprete que la copia no tiene:** el juez lo llamaba con el `.venv` de la raíz, que una copia no lleva; ahora usa el intérprete con que corre el juez, que en el paso pago es el del `.venv` del repo.
6. **Una corrida en seco mal planteada:** le di a los comandos una raíz de sesiones temporal y el enmascarado, con razón, rechazó sus streams (el `cwd` no era el del banco). Saqué esa variable: los comandos de la corrida en seco usan la raíz real, como en A2.1.
7. **Edité un archivo mientras la corrida en seco corría sobre él:** cambié `test_aislamiento_a2_2.py` en la copia de trabajo durante la tercera corrida en seco; su sha256 dejó de dar y el paso 5 frenó con el código 6. Rearmé la lista y la volví a correr entera, sin tocar nada.
8. **Un literal que el grep marca:** el control de rutas que agregué al aislamiento escribía la carpeta temporal del sistema; el grep dio 1. Lo reescribí, rearmé la lista, lo llevé al repo, corrí otra vez el aislamiento en el repo y las pruebas en una copia final nueva.
9. **El aislamiento sobre la copia, con rutas de la máquina:** con `--init-dir` en la carpeta temporal, las metas y los comandos init traían esa ruta; el test no lo vio porque solo buscaba la carpeta personal. Solo pasó en la copia; lo vio el grep previo y reforcé el control.
10. **Detalles de zsh antes de correr:** un `xargs print` (no es un programa), un `${VAR:+…}` que zsh no parte en palabras y un `rm` con un patrón vacío. Los dos primeros, en los comandos, los vi al releerlos y los corregí antes de la primera corrida en seco; el tercero cortó un grep previo, que repetí.
11. **Como registro de la corrida en seco:** la primera vez que corrió (12:2x), la guarda de `pgrep` frenó los comandos por los procesos reales del juez v2 (el error 2): la guarda funcionó con el patrón real; para poder seguir sin esperar, la corrida en seco usa desde entonces su propio patrón (`A22_PATRON_PGREP`, solo con `A22_MODO=init`).

## 11. Lo que queda abierto

- Los cinco pasos pagos (de la autora) y lo que viene después de ellos (§8).
- El contenedor de Neo4j queda levantado (§6).
- Las carpetas que dejé fuera del repo: 109 carpetas de configuración nuevas en `fuera_del_repo/banco_sesiones/config/` (de 79 a 188), todas de sesiones init: 13 de los cinco aislamientos y 96 de las cuatro corridas en seco de los comandos que lanzaron sesiones; y 3 carpetas de sesiones init del aislamiento en `fuera_del_repo/banco_sesiones/aislamiento_a2_2/`. La carpeta de originales `banco_mcp_originales_A2_2/` todavía no existe: la crea el enmascarado después de los pasos pagos.

## 12. Cierre

- **En el repo:** `data/experiment/banco_mcp/a2_2/`, nueva (49 archivos con este FRENO), y el volumen de Neo4j (§9).
- **El paquete:** `revision_A2_2_FRENO_a/` en la carpeta temporal de la sesión, copiado con `ditto` a
  `~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/94968c98-6fa5-449c-954b-42ee7ee26062/scratchpad/revision_A2_2_FRENO_a/` y verificado
  en la copia contra su `manifest.txt`.
- **El checkpoint:** `checkpoint_A2_2.md`, en la carpeta temporal y en
  `~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/94968c98-6fa5-449c-954b-42ee7ee26062/scratchpad/checkpoint_A2_2.md`.
- **FRENO A2.2-a.** Espero la revisión de la mesa.
