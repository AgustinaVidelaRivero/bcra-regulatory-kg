# FRENO A2.1-a — tramo 1 de A2.1: el BM25 de fragmentos, el índice denso r2b, el aislamiento y el diseño de H-B2

Mandato: `docs/mandatos/A2_1_sistema_por_fragmentos_preregistro_A2_2.md`, FIRMADO el 15/10/2026 a las 15:54:12; texto
firmado leído en `c2b6cb60`, sha256 `b311859c…` (§0). Rigen el §1, el §2, el §3 (tramo 1), el §6, el §7, el §8 y el §9, con
las notas posteriores a la firma leídas en HEAD. Este FRENO es el del tramo 1: los tramos 2 y 3 esperan otro «seguí».

USD 0, sin API. Nada commiteado, ningún mensaje de commit preparado, nada escrito en la memoria, en `.claude/` ni en
`.gitignore`. EV2 no se abrió: `preguntas_ev2_fidelidad.json` se cita solo por ruta y sha (`1d587336…`).

**En corto:**

- El servidor de fragmentos tiene la configuración BM25 (analizador `spanish` de Lucene 9.11.1 replicado pieza por pieza, con
  su fuente; k1 = 1,2 y b = 0,75) y acota `limite` a 5 en las dos configuraciones de A2.1. La config vieja da byte a byte lo
  mismo que en U-A2.0-banco.
- Índices: BM25 r2b `6b5da8b0…` y denso r2b `828caeff…`, cada uno igual en sus dos construcciones; con la E0 vieja, la matriz
  da el sha sellado `12d284d5…`.
- El venv 3.12 del servidor lo había borrado el limpiador de la carpeta temporal: es un entorno nuevo, con exactamente
  `requirements_vector.txt` (§3), validado con ese `12d284d5…`.
- Las dos configuraciones del brazo del grafo (sellado y re-sellado) están escritas y verificadas contra `grafos.py`, sin
  Neo4j.
- Tests: todos en PASS en la copia de trabajo y en la copia final (§8). Aislamiento del BM25: (a) a (d) en PASS, con una
  corrida auditada que muestra que el servidor no importa neo4j, no carga el modelo y no abre sockets de red.
- El diseño de H-B2 y los dos comandos pagos del tramo 2 (cota USD 1,1305) quedan escritos.

## 0. Paso 0 (16/10/2026, antes de cualquier otra cosa), con la carpeta personal reemplazada por `$HOME`

```
$ pwd
$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg
$ git log --format=%s -5
Registro de decisiones: los valores del alcance confirmados, la revision entre tandas y la tanda final en dos tramos
Segmentacion oficial: la tanda final de 98 documentos, su control de salud y el re-censo de la release de la segmentacion
Mantenimiento: las anclas al codigo de la resolucion y del ensamblado, puestas al dia
Mandatos firmados: el resultado del re-sellado unico y la variante del alcance por seccion que se mide al derivar
Alcance en el mensaje del extractor: el registro de alcance de la primera tanda llega a sus documentos
$ git status --porcelain -- data/experiment/banco_mcp
$ claude --version
2.1.241 (Claude Code)
$ ls data/experiment/banco_mcp
README.md
__pycache__
adaptador
agentes
aislamiento
cliente_falso.py
comun_banco.py
gate
logs
mcp_kg
mcp_vector
requirements_kg.txt
requirements_vector.txt
smoke
$ git rev-parse --abbrev-ref HEAD
main
$ git status --porcelain --untracked-files=no
$ git show --stat --format=%s HEAD~1
Segmentacion oficial: la tanda final de 98 documentos, su control de salud y el re-censo de la release de la segmentacion

 .../segmentacion_oficial_e0r2/s2/FRENO_S2.md       |  130 +
 .../segmentacion_oficial_e0r2/s2/REPORTE_S2.md     |   50 +
 .../resumen_healthcheck_tanda_final_S2c.json       | 2627 ++++++++++
 .../s2/cifras/tanda_final_S2c.json                 | 5132 ++++++++++++++++++++
 .../s2/cifras_segmentacion_oficial.md              |  140 +
 .../s2/controles/grep_convenciones_S2c.txt         |    3 +
 .../s2/scripts/generar_cifras_S2.py                |  105 +
 .../s2/scripts/lote_tramo3_S2c.sh                  |   28 +
 .../s2/scripts/tanda_final_S2.py                   |  160 +
 9 files changed, 8375 insertions(+)
```

- Los cinco títulos, en el orden esperado: el 84 arriba, el FRENO final de S2 segundo (toca
  `data/experiment/segmentacion_oficial_e0r2/s2/`) y los tres siguientes tal cual. `git status` no da nada en `banco_mcp/`;
  la rama es `main`; no hay cambios rastreados. `claude --version` da la sellada, 2.1.241.
- `ls` muestra un `__pycache__/` en la raíz del banco (`cliente_falso` y `comun_banco`, del 23/08/2026); el `.gitignore` local
  del banco lo excluye. No lo toqué.
- **El texto firmado:** el commit más viejo de `git log --format=%h -- docs/mandatos/A2_1_sistema_por_fragmentos_preregistro_A2_2.md`
  es `c2b6cb60`; el sha256 de los bytes de `git show c2b6cb60:<mandato>` hasta antes de `\n## Firma` (17.543 de 17.946
  bytes) da `b311859c0cf90ad6581cd4e639b37a7498bd8daad0ac8475e83ce604ddf7076d`. Las notas posteriores a la firma, en HEAD
  (`git diff c2b6cb60 HEAD` del mandato: 18 líneas agregadas, dos notas del 15/10/2026: el juez y la muestra simétrica de
  A2.2, y el re-sellado único).

## 1. Lo que leí y lo que no abrí

- **Del repo:** el mandato (texto firmado en `c2b6cb60` y notas en HEAD), `banco_mcp/README.md`, el código y las configs de
  `mcp_vector/`, `mcp_kg/` (config), `agentes/`, `aislamiento/` y `smoke/`, `comun_banco.py`, `cliente_falso.py`, el adaptador,
  `data/experiment/neo4j/grafos.py`, `neo4j_index.py`, su README y su `docker-compose.yml` (solo lectura), `_tokens` de
  `evaluacion/harness.py` (solo lectura), las metas, streams y logs R1 de la corrida 2 de la fase B (material propio),
  `docs/plan_tesis.md:339-340` y el bloque del 07/10/2026 de `docs/checklist_pre_escalado.md`.
- **De la web** (16/10/2026, solo lectura, sin descargar a disco): el `pom.xml` del tag 5.26.9 de neo4j/neo4j; de Lucene 9.11.1,
  `SpanishAnalyzer`, `SpanishLightStemmer`, `spanish_stop.txt`, `StandardTokenizer`, `StandardTokenizerImpl.jflex`,
  `BM25Similarity` y `SmallFloat`; la página de índices full-text del Cypher Manual 5; la referencia TypeScript del Agent SDK
  (`maxTurns`, `SDKResultMessage`).
- **Fuera del repo:** del scratchpad de la mesa, solo `con_clave_del_entorno.py`, por su ruta (sha256 `83527b33…`, igual al
  esperado). Nada de las carpetas vedadas.
- **No abrí:** EV2 (ni `preguntas_ev2_fidelidad.json`, ni sus trazas, ni el juez, ni la tabla); ningún `.env`; ningún
  `NO_ABRIR_*`. No corrí `smoke/verificar_territorio.py`, porque lee las anclas del gold de EV2.

## 2. Diferencias con el mandato y decisiones que tomé (con su razón)

**Diferencias con el mandato, declaradas:**

1. **Dónde corren los tests al final** (decisión de la autora del 15/10/2026, punto 1.5 del despacho). El §3 del mandato
   dice «con los tests corridos de nuevo en el repo» y CLAUDE.md §4.l dice que los selftests corren sobre una copia; por la
   regla d de CLAUDE.md mandan los archivos. La corrida final va sobre una copia nueva hecha desde el repo después de
   escribir, con la foto sha256 del repo antes y después (0 cambios), como en la reproducción final de A2. En el repo no corrí
   nada que escriba.
2. **El entorno del servidor de fragmentos es nuevo** (decisión de la autora del 16/10/2026, en esta sesión). El venv 3.12 del
   bake-off, que usaba el banco, lo borró el limpiador de la carpeta temporal del sistema (`com.apple.tmp_cleaner`): quedaba
   solo `bin/`, sin torch, transformers, sentence-transformers, tokenizers ni mcp. Lo reemplacé por uno nuevo en `~/INGENIERIA IA/TESIS/venvs/banco_vector_py312`,
   con el Python 3.12.13 de miniforge y exactamente `requirements_vector.txt`, con pip, sin otros paquetes de primer nivel
   (§3 de este FRENO). El `.venv` del repo no se tocó. El modelo no se descargó: se usó la caché local, con
   `HF_HUB_OFFLINE=1` y `TRANSFORMERS_OFFLINE=1` en todo lo que lo carga.

**Decisiones mías, por lo que la §6 permite escribir.** `agentes/`, `aislamiento/test_aislamiento.py` y
`smoke/correr_smoke.py` quedan fuera de la §6, así que no los edité: los importo.

3. **La configuración de los agentes de A2.1 y su lanzador van en `a2_1/`** (`config_agentes_a2_1.json`,
   `bloque_tools_fragmentos_bm25.txt`, `lanzar_agente_a2_1.py`). El lanzador sellado acepta solo los brazos `kg` y `vector`
   y fija la config del servidor vectorial viejo. El de A2.1 importa sus funciones (prompt, flags, vía de credenciales, modo
   init, parseo, metadata) y replica su `main` con tres diferencias: los brazos de fragmentos, `--max-turns` para H-B2 y el
   cwd de cada brazo en `a2_1/cwd/<brazo>/` (vacío). El diff contra el sellado está en el paquete.
4. **Los JSON de MCP de los dos brazos van en `mcp_vector/`** (`mcp_fragmentos_bm25.json`, `mcp_fragmentos_denso.json`),
   como «configuraciones nuevas» del servidor de fragmentos. Son el de `agentes/mcp_vector.json` con otro nombre de servidor
   y otra config, más `TRANSFORMERS_OFFLINE=1`.

**Decisiones sobre lo que ve el agente.** [DECIDE LA AUTORA] en cada una, antes del smoke del tramo 2:

5. **El nombre del servidor MCP es `fragmentos` en los dos brazos**, así que la tool se llama igual en los dos:
   `mcp__fragmentos__buscar_pasajes`. Alternativa: `vector` en el denso (como en la fase B) y otro nombre en el BM25.
6. **La descripción de la tool cambia solo en la medida de afinidad:** «Búsqueda léxica (BM25)» en el BM25 y «Búsqueda
   semántica (embeddings)» en el denso (la de U-A2.0-banco). Lo mismo en el bloque del prompt (diff de una línea). Alternativa:
   una descripción neutra en los dos («Búsqueda de pasajes…»), para que el agente no sepa qué medida tiene.
7. **La descripción de `limite` dice el tope en las configuraciones de A2.1:** «Máximo de resultados (def. 5, máx. 5).». En la
   config vieja sigue «(def. 10)», byte a byte. Alternativa: dejar «(def. 10)» también en A2.1, que sería falso con D-D.

**Decisiones sobre el código.**

8. **`limite_max` sale de la config** (50 si no lo declara): la config vieja sigue acotando a 50, y por eso la regresión del
   denso da byte a byte; las dos de A2.1 declaran 5 (D-D). Un `limite` que no es entero cae a `min(10, limite_max)`.
9. **El índice BM25 se persiste** (`indice/e0_r2b_desarrollo_bm25/indice_bm25.json`, bytes canónicos) para tener su sha, y el
   servidor lo re-deriva al arrancar desde los pasajes: si el analizador del proceso no lo reproduce, aborta.
10. **Los índices nuevos van dentro de `mcp_vector/indice/`**, en subcarpetas, porque esa es la ruta que el `.gitignore` local
    del banco deja fuera de git (y el mandato pide que el `indice/` siga fuera de git); el `.gitignore` no se toca. El índice
    viejo, en la raíz de `indice/`, no cambia.
11. **El aislamiento admite dos subprocesos del servidor BM25, `uname` y `file`:** los lanza `platform.platform()` de la
    biblioteca estándar al registrar el entorno en el log R1 (`comun_banco.versiones_entorno`, el mismo de los otros
    servidores). Y admite sockets AF_UNIX: el par que crea el loop de asyncio. Ninguno toca la red ni el grafo.
12. **Las preguntas de H-B2 son las de `smoke/preguntas_smoke.json`, solas o juntas.** No escribí preguntas nuevas porque su
    chequeo de territorio (`smoke/verificar_territorio.py`) lee las anclas del gold de EV2, que no se abre. Una pregunta
    compuesta lleva las mismas anclas, ya verificadas.
13. **La guarda de modo del runner:** una meta de otro modo (init frente a real) en la carpeta de salida aborta la corrida,
    para que una sesión de la corrida en seco nunca se tome por real al reanudar.

## 3. El entorno nuevo del servidor de fragmentos (reemplaza al del bake-off)

**Por qué.** `banco_mcp/README.md` («Entornos») fija el servidor vectorial en Python 3.12 con `requirements_vector.txt`, «el
entorno de referencia del bake-off» (`bakeoff_embeddings/resultados/e3_entorno.json`, cuyo `venv` estaba en el scratchpad de
otra sesión, en la carpeta temporal del sistema). Al empezar este tramo ese venv tenía solo `bin/`: el resto lo borró el
limpiador de la carpeta temporal del sistema (`com.apple.tmp_cleaner`, CLAUDE.md §4.g). Ningún otro entorno local tenía las
versiones, ni la caché de uv. La autora decidió recrearlo (16/10/2026, en esta sesión), con condiciones.

**Qué hice:**

- Intérprete base: `~/miniforge3/bin/python3.12` (3.12.13, conda-forge, «main, Mar 5 2026»): el mismo Python que registra el
  bake-off (`e3_entorno.json`: 3.12.13).
- Venv: `~/INGENIERIA IA/TESIS/venvs/banco_vector_py312` (fuera del repo y de la carpeta temporal del sistema), con
  `python -m venv` y su pip (25.0.1), sin actualizarlo.
- Requisitos: `data/experiment/banco_mcp/requirements_vector.txt` del repo (último commit que lo toca: `1fa79de3`), copiado al
  paquete; sha256 `50a7da51a5a37a988d13146a0dbb0354c7043cb93fed8a5218b376f256da80f3`.
- Descarga: `pip download --no-cache-dir -d ruedas -r requirements_vector.txt` a una carpeta vacía del scratchpad: **62
  ruedas, 187.833.394 bytes** (suma de los tamaños; `du -sk` da 183.552 KB). El sha256 de cada rueda está en el paquete
  (`sha256_ruedas_A2_1a.txt`).
- Instalación sin red: `pip install --no-index --find-links ruedas -r requirements_vector.txt`. Sin paquetes de primer nivel
  fuera de los seis; pip trae las dependencias que esos seis declaran.
- `pip freeze --all`: 63 líneas (62 paquetes y pip), en el paquete (`pip_freeze_banco_vector_py312_A2_1a.txt`). Los seis
  pinneados: `torch==2.13.0`, `transformers==5.15.1`, `sentence-transformers==6.0.0`, `tokenizers==0.22.2`,
  `numpy==2.5.2`, `mcp==1.29.0`. `import neo4j` falla en el venv (`ModuleNotFoundError`).
- Diferencia con el bake-off: `e3_entorno.json` registra además `peft 0.20.0`, que no está en `requirements_vector.txt` y
  no instalé. Las versiones de las dependencias del bake-off no están registradas, así que no se pueden comparar.
- El modelo no se descargó: `microsoft/harrier-oss-v1-0.6b` @ `f9b9dc8d…` desde `~/.cache/huggingface/hub`, con
  `HF_HUB_OFFLINE=1` y `TRANSFORMERS_OFFLINE=1` en cada comando que lo carga, en los JSON de MCP de los dos brazos y en los
  scripts del tramo 2.

**La validación:** con este venv, `construir_indice.py --manifiesto manifiestos_e0/e0_enm01.json` da la matriz
`12d284d5bce0d1d58f1e4437c47f2177b3145813586069ca72f9103309b28b65`, el sha sellado (`banco_mcp/README.md:95`) y el
`sha_docs` de harrier en el bake-off: 93 grupos, 0 truncados, pasaje más largo de 8.233 tokens, 434,8 s.

## 4. El analizador y el BM25: cada pieza con su fuente, y las diferencias con el `spanish` de Lucene (Q2)

Versión de Lucene: la imagen del backend del grafo es `neo4j:5.26.9-community` (`data/experiment/neo4j/docker-compose.yml:34`),
y el `pom.xml` del tag 5.26.9 de neo4j/neo4j fija `lucene.version` = 9.11.1. Todas las fuentes de abajo son de Lucene
9.11.1 (tag `releases/lucene/9.11.1` de apache/lucene), leídas en la web el 16/10/2026, sin descargar nada a disco. La
implementación está en `mcp_vector/bm25_fragmentos.py`, con la fuente de cada pieza en su docstring.

| pieza | fuente | en `bm25_fragmentos.py` |
|---|---|---|
| cadena | `es/SpanishAnalyzer.createComponents`: StandardTokenizer → LowerCaseFilter → StopFilter → SpanishLightStemFilter (SetKeywordMarkerFilter solo con un conjunto de exclusión, que el default no tiene) | `analizar` |
| tokenizador | `standard/StandardTokenizer` (UAX #29, `%unicode 12.1` en `StandardTokenizerImpl.jflex`; largo máximo 255, `StandardAnalyzer.DEFAULT_MAX_TOKEN_LENGTH`) | `tokenizar` (subconjunto) |
| minúsculas | `LowerCaseFilter` = `Character.toLowerCase` por punto de código (mapeo simple) | `minusculas` |
| palabras vacías | `SpanishAnalyzer.getDefaultStopSet()` = `WordlistLoader.getSnowballWordSet` sobre `snowball/spanish_stop.txt` (Snowball, BSD): 308 palabras | `STOP_ES` (308, mismo orden; sha256 de la lista unida por `\n`: `653a4f50…`) |
| stemmer | `es/SpanishLightStemmer.stem` (Savoy, «Report on CLEF-2001 Experiments») | `stem` |
| BM25 | `search/similarities/BM25Similarity`, constructor sin argumentos: k1 = 1,2, b = 0,75; idf = ln(1 + (docCount − df + 0,5)/(df + 0,5)); s = idf · tf/(tf + k1 · (1 − b + b · dl/avgdl)), sin el factor (k1 + 1); avgdl = sumTotalTermFreq/docCount | `Buscador` |
| norma de largo | `util/SmallFloat.intToByte4` / `byte4ToInt` (un byte, con pérdida desde 24) | `int_to_byte4`, `byte4_to_int` |
| parámetros en Neo4j | la doc de índices full-text de Neo4j 5 (Cypher Manual) no fija similitud, k1 ni b: solo expone `fulltext.analyzer` y `fulltext.eventually_consistent` | k1 y b de Lucene |

Diferencias que quedan:

1. **Tokenizador, subconjunto de UAX #29.** Implemento WB4 (Extend y Format se pegan al carácter anterior), WB5, WB8 a
   WB10, WB13a y WB13b (letras, dígitos y ExtendNumLet se unen), WB6 y WB7 (letra (MidLetter | MidNumLet | ') letra) y
   WB11 y WB12 (dígito (MidNum | MidNumLet | ') dígito); todo lo demás corta. No implemento las reglas de letras hebreas,
   de indicadores regionales ni de secuencias de emoji, ni los tipos de token IDEOGRAPHIC, HIRAGANA, KATAKANA,
   SOUTHEAST_ASIAN y EMOJI (Lucene emite cada ideograma como un token; acá se trataría como letra). ALetter se aproxima con
   `str.isalpha()` y Numeric con la categoría Nd. Medido sobre el corpus r2b (inventario de caracteres de los 1.768
   pasajes, `a2_1/controles/`): 142 caracteres distintos, ninguno fuera del plano básico, ninguna marca combinante, ningún
   carácter de formato, ningún espacio fino ni guion blando; las únicas letras no latinas son α, σ, Σ, ᶲ y º. Ninguna de las
   reglas que faltan aplica al corpus.
2. **Unicode.** Lucene usa las tablas de UAX #29 de Unicode 12.1 y las de mayúsculas de su JDK; acá, `unicodedata` de
   Python (15.0.0 en el venv 3.12, 13.0.0 en el `.venv` 3.10). Para los caracteres del corpus no cambia nada: el índice se
   re-deriva igual con las dos versiones (el servidor lo re-deriva al arrancar y exige el mismo sha; corrió con las dos).
3. **Largo en unidades UTF-16.** El stemmer de Lucene cuenta caracteres Java (UTF-16) y acá se cuentan puntos de código: es
   lo mismo en el plano básico, que es todo el corpus.
4. **Aritmética.** Lucene calcula el BM25 en float32 (pesos, la caché de normas y el score); acá se calcula en float64. Los
   rankings solo pueden diferir en casi-empates, por debajo del épsilon de float32. El score que se expone va redondeado a
   6 decimales, como en el denso.
5. **La consulta.** Lucene, vía Neo4j, interpreta la sintaxis del QueryParser clásico (operadores, comillas, comodines,
   `campo:`); acá la consulta se analiza con el mismo analizador que los documentos y sus términos se suman con su
   multiplicidad (equivale a las cláusulas SHOULD del QueryParser sobre texto sin operadores). El brazo del grafo hace
   otra cosa antes de Lucene: `Neo4jIndex` pre-tokeniza la consulta con `_tokens` del harness (minúsculas, sin acentos,
   `[a-z0-9]+`) y une los tokens con espacios (`data/experiment/neo4j/neo4j_index.py:121-128` y `:169-170`). Eso le quita
   los acentos a la consulta antes del analizador (y las palabras vacías con tilde, como «más» o «también», dejan de serlo)
   y parte «1.234,56» en tres tokens. Acá no lo replico: el BM25 de fragmentos analiza la consulta como analiza los
   documentos. [DECIDE LA AUTORA]: (a) así, simétrico, como Lucene con el mismo analizador en las dos puntas; (b) replicar
   la pre-tokenización del brazo del grafo.
6. **La unidad de documento.** El índice del grafo es de varios campos por nodo (label, descripcion, description, id); el de
   fragmentos es de un campo, el texto del pasaje con su herencia. No es una diferencia del analizador sino del sistema, y
   es la que el experimento compara.
7. **Sin verificación contra Lucene en ejecución.** No hay Lucene local (búsqueda sin resultados de jars de
   lucene-analysis en la carpeta personal, con las carpetas vedadas excluidas) y el contenedor no se toca: la réplica está
   verificada contra las fuentes y contra lo esperado a mano de 41 entradas (`bm25_analizador`), no contra la salida de
   Lucene. NO VERIFICADA contra Lucene en ejecución.
8. **La norma.** Replico la cuantización de un byte de Lucene (`SmallFloat`), que cambia el score de los pasajes largos.
   [DECIDE LA AUTORA]: (a) así, como Lucene; (b) largo exacto.
9. **Una consulta solo de palabras vacías** devuelve 0 pasajes (`de la que el en y a los del se`), igual que el full-text
   del grafo (`neo4j_index.py`, docstring del modo fulltext); el denso devuelve siempre `limite`.

## 5. Los cambios de código, con su diff

Los diffs completos contra HEAD están en el paquete (`diff_servidor_mcp_vector_A2_1a.txt`, `diff_construir_indice_A2_1a.txt`);
el del cuerpo del lanzador de A2.1 contra el `main` sellado, en `diff_lanzador_a2_1_vs_sellado_A2_1a.txt`.

**Modificados (2):**

- `mcp_vector/servidor_mcp_vector.py`:
  - clave `afinidad` de la config: `denso` (default; el comportamiento de U-A2.0-banco) o `bm25` (clase nueva `IndiceBM25`,
    sin numpy ni modelo; verifica el sha de `pasajes.json` y del índice contra su manifiesto y la config, y re-deriva el
    índice desde los pasajes al arrancar);
  - clave `limite_max` (50 si falta): `_limite(limite, limite_max)` = `max(1, min(int(limite), limite_max))`, o
    `min(10, limite_max)` si no es entero;
  - `definicion_tool(afinidad, limite_max)`: con (denso, 50) devuelve la definición de U-A2.0-banco tal cual; si no, cambia
    solo la descripción de la medida de afinidad y, con `limite_max` < 10, la de `limite` (§2, decisiones 6 y 7);
  - `_fila` arma cada pasaje con los mismos campos y el mismo orden en los dos modos; el desempate es el mismo (score desc,
    id asc);
  - el log R1 registra en `fuente` el índice, su sha y su manifiesto de E0; en modo BM25, además, el analizador, la versión
    de Lucene, el sha de las palabras vacías, k1, b, la versión de `unicodedata` y el sha de `bm25_fragmentos.py`; y el
    entorno, solo con `mcp` (en modo BM25 no se consultan las versiones de torch y compañía);
  - `fuente.sha_docs_bakeoff` y `coincide_con_bakeoff` se leen con `.get` (los índices nuevos no tienen bake-off).
- `mcp_vector/construir_indice.py`:
  - `--manifiesto` (default `manifiestos_e0/e0_enm01.json`, la E0 vieja): directorio, TOs, sha de cada `chunks_<to>.json`,
    cantidad de pasajes y sha del corpus esperados; con la E0 vieja, además, las verificaciones contra el bake-off de
    U-A2.0-banco;
  - `--afinidad bm25`: construye el índice BM25 de los mismos pasajes, sin importar torch;
  - `--out` obligatorio salvo con la E0 vieja y el denso (que sigue yendo a `indice/`, el índice de U-A2.0-banco), para no
    pisar el índice viejo por accidente;
  - el manifiesto del índice registra el manifiesto de E0 usado (ruta, sha y cantidad) y el sha esperado de la matriz con
    su comparación.

**Nuevos en `mcp_vector/` (8, más los índices fuera de git):** `bm25_fragmentos.py`, `test_fragmentos_a2_1.py`,
`config_fragmentos_bm25_r2b.json`, `config_fragmentos_denso_r2b.json`, `mcp_fragmentos_bm25.json`,
`mcp_fragmentos_denso.json`, `manifiestos_e0/e0_enm01.json` y `manifiestos_e0/e0_tanda0_r2b_desarrollo.json`; índices en
`indice/e0_r2b_desarrollo_bm25/` y `indice/e0_r2b_desarrollo_denso/` (3 archivos cada uno).

**Nuevos en `mcp_kg/` (2):** `config_mcp_kg_a2_desarrollo_r2b.json` y `config_mcp_kg_a2_desarrollo_r2b_rs1.json` (§7).

**Nuevos en `a2_1/`:** el envoltorio copiado tal cual; la config de agentes, el bloque de prompt del BM25, el lanzador, el
runner del tramo 2 y su corrida en seco; la prueba del envoltorio, el test de aislamiento y su sonda; el antecedente de
H-B2, el inventario de caracteres y el estimador; el diseño de H-B2 (JSON y documento), la estimación, los dos scripts
`zsh`; este FRENO; y `controles/` (las salidas de las pruebas y sus logs R1). En `aislamiento/resultados/a2_1/`, la salida
del aislamiento.

Sin cambios: `gate/`, `agentes/`, `mcp_kg/servidor_mcp_kg.py`, `aislamiento/test_aislamiento.py`, `smoke/`,
`comun_banco.py`, `cliente_falso.py`, `config_mcp_vector.json`, `test_mcp_vector.py`, sus resultados y el índice viejo
(§13: la foto lo muestra).

## 6. Los índices (§3, puntos 1 y 2; D5)

Los dos sobre la E0 r2b de desarrollo (`manifiestos_e0/e0_tanda0_r2b_desarrollo.json`, sha `118bf0b2…`): los cinco
`chunks_<to>.json` de `reextraccion_v2/e0_chunking/salida_tanda0_r2b/` con su sha; 1.768 pasajes (462 + 143 + 973 + 101 +
89), propio + herencia = `sha256_completo` en los 1.768, sha del corpus `c41ef288…`. Los dos sirven el mismo `pasajes.json`
(`d8faf4d2…`). Fuera de git, en `mcp_vector/indice/` (gitignore local del banco), con su sha en el manifiesto y en la config.

| índice | dónde | sha | construcciones | detalle |
|---|---|---|---|---|
| BM25 r2b | `indice/e0_r2b_desarrollo_bm25/indice_bm25.json` | `6b5da8b0940e6ae46214b93c541b384a710eb35688264c0138df2e7b4773fc25` | 2 iguales byte a byte en cada corrida de `bm25_determinismo` (y una con el Python base 3.12.13, otra con el venv nuevo y otra con el `.venv` 3.10, todas iguales) | 1.768 documentos, vocabulario 8.378, 207.948 términos, 2.026.832 bytes |
| denso r2b | `indice/e0_r2b_desarrollo_denso/embeddings_docs.npy` | matriz `828caeffe528a5cfd584c14fc81de7b168faf83ea731ba7bd4a2d390afc05889` | la servida y dos más en cada corrida de `denso_r2b_dos`, iguales byte a byte | 1.768 × 1024, float32; 95 grupos; 0 truncados; pasaje más largo 8.464 tokens |
| denso, E0 vieja | reconstrucción en directorio temporal | `12d284d5bce0d1d58f1e4437c47f2177b3145813586069ca72f9103309b28b65` | en el scratchpad y en cada corrida de `denso_e0_vieja` | = el sha sellado (`banco_mcp/README.md:95`) y el `sha_docs` del bake-off; 93 grupos, 0 truncados |

- **D5, las unidades que superan la ventana:** ninguna. El pasaje más largo de la E0 r2b tiene 8.464 tokens y la ventana del
  índice es de 32.768 (`max_seq_length`), así que no hay unidades que partir ni que declarar.
- **Sin descargas del modelo:** `harrier-oss-v1-0.6b` @ `f9b9dc8d…` estaba en la caché local, y todo lo que lo carga corrió
  con `HF_HUB_OFFLINE=1` y `TRANSFORMERS_OFFLINE=1`.
- El índice viejo (`indice/` en la raíz) no se tocó: sigue siendo `12d284d5…` y lo sirve la config vieja.

## 7. Las dos configuraciones del brazo del grafo (§3, punto 3; D-A)

Con el formato de `mcp_kg/config_mcp_kg.json` (backend `neo4j`, modo `fulltext`, firma v1), una por cada grafo posible:

| archivo | clave de `grafos.py` | sha esperado | `commit_sellado` en `grafos.py` | sha del `kg.json` (medido) |
|---|---|---|---|---|
| `mcp_kg/config_mcp_kg_a2_desarrollo_r2b.json` | `KG_Tanda0_Desarrollo_r2b` | `6e756043…d8e9a2` | `bbc38dc` | `6e756043…d8e9a2` |
| `mcp_kg/config_mcp_kg_a2_desarrollo_r2b_rs1.json` | `KG_Tanda0_Desarrollo_r2b_rs1` | `acb26dca…dcac31` | `4fe6ece` | `acb26dca…dcac31` |

- El re-sellado único está sellado: primer commit del sello `4fe6ece1` («…el re-sellado unico, primer commit del sello»,
  15/10/2026 20:16:26) y segundo `45786ec0` (20:16:40), que es el que escribe `"commit_sellado": "4fe6ece"` en `grafos.py`
  (`git log -S'"commit_sellado": "4fe6ece"' -- data/experiment/neo4j/grafos.py` da `45786ec0`). Por eso armé las dos en
  este tramo.
- El test `config_grafo` (`mcp_vector/test_fragmentos_a2_1.py`) las compara con `grafos.py` (importado, solo lectura) y con
  el sha del `kg.json`, sin Neo4j: PASS en las dos corridas.
- No cargué nada en Neo4j ni toqué el contenedor. La carga y el test positivo del brazo del grafo van al principio de A2.2,
  como precondición declarada; el servidor del grafo (`servidor_mcp_kg.py`, sin cambios) verifica `KG_Meta.kg_sha256` contra
  el archivo y contra la config antes de exponer una tool.
- **Declaración (§3, punto 3):** en `grafos.py`, el campo `vista_runtime` de las ocho entradas r2b dice «r2b no se evalúa
  con EV2»: las dos selladas en `bbc38dc` (líneas 131 y 145), las dos sin cola (165 y 179) y las cuatro `_rs1` (199, 213, 227
  y 241). Según el mandato (§3, punto 3), ese texto viene de U-REEXT-T0 (06/10/2026) y es anterior a D5 (07/10/2026), que
  fija el grafo de desarrollo r2b como brazo del grafo de A2 (`docs/plan_tesis.md:339`). No edité `grafos.py`.
- No armé la configuración de agente del brazo del grafo para A2 (JSON de MCP y brazo en la config de agentes): `mcp_kg/` solo
  admite el archivo de configuración del servidor (§6), y la carga del grafo es de A2.2. Queda para A2.2 o el tramo 3.

## 8. Los tests (§3, punto 4), con su salida

Dos corridas completas, con `scripts/correr_tests.zsh` del scratchpad (en el paquete, la salida de consola de las dos):

- **en la copia de trabajo** (`copia_trabajo`, hecha a las 00:52:23 con el rsync de la cláusula), donde escribí y probé; sus
  salidas son las que llevé al repo (`a2_1/controles/` y `aislamiento/resultados/a2_1/`);
- **en la copia final** (`copia_final`, hecha desde el repo a las 08:59:45, después de escribir, con el rsync de la
  cláusula), con la foto sha256 del repo antes y después (§13). Sus salidas quedan en la copia y en el paquete; el repo no se toca.

| grupo | criterio | copia de trabajo | copia final |
|---|---|---|---|
| `bm25_analizador` | 41 entradas con lo esperado a mano y la pieza de Lucene que lo fija; lista de 308 palabras vacías | PASS: 41 de 41 | PASS: 41 de 41 |
| `bm25_determinismo` | dos construcciones = el sha servido = el de la config; mismos rankings | PASS: `6b5da8b0…` las dos; rankings iguales en 12 consultas | PASS: `6b5da8b0…` las dos; rankings iguales en 12 consultas |
| `bm25_transporte` | 13 consultas por MCP byte a byte contra el cálculo directo; definición de la tool; todo pasaje cita `to` y `unidad`; log R1; `limite` > 5 devuelve 5 | PASS: 13 de 13 iguales; máx. 9984 chars; `limite` 9 de 9 | PASS: 13 de 13 iguales; máx. 9984 chars; `limite` 9 de 9 |
| `regresion_denso` | test (d) de `test_mcp_vector.py` con el índice y la config viejos, y sus 10 salidas con el mismo sha256 que en la corrida sellada | PASS: 10 de 10 con el sha de la corrida sellada; (a) PASS, (c) PASS, (d) PASS | PASS: 10 de 10 con el sha de la corrida sellada; (a) PASS, (c) PASS, (d) PASS |
| `denso_e0_vieja` | la matriz de la E0 vieja da `12d284d5…` | PASS: `12d284d5…` | PASS: `12d284d5…` |
| `denso_r2b` | 13 consultas por MCP byte a byte; sha del manifiesto = config; `limite` > 5 devuelve 5 | PASS: 13 de 13 iguales; máx. 13667 chars; `limite` 9 de 9; mismos pasajes que el BM25 | PASS: 13 de 13 iguales; máx. 13667 chars; `limite` 9 de 9; mismos pasajes que el BM25 |
| `denso_r2b_dos` | dos construcciones más de la matriz r2b, iguales byte a byte y = la servida | PASS: `828caeff…` las dos, `.npy` byte a byte | PASS: `828caeff…` las dos, `.npy` byte a byte |
| `config_grafo` | las dos configuraciones del grafo = `grafos.py` = sha del `kg.json` | PASS: 2 de 2 | PASS: 2 de 2 |
| aislamiento (a) | inventario en `system/init` (modo init) | PASS: mcp__fragmentos__buscar_pasajes; dontAsk | PASS: mcp__fragmentos__buscar_pasajes; dontAsk |
| aislamiento (b) | sin tools de archivos; código sin módulos ni rutas del grafo; corrida auditada | PASS: módulos prohibidos 0, archivos del modelo 0, del grafo 0; `import neo4j` rc 1 | PASS: módulos prohibidos 0, archivos del modelo 0, del grafo 0; `import neo4j` rc 1 |
| aislamiento (c) | sin red: código sin sockets ni bolt; corrida auditada | PASS: sockets 2 (AF_UNIX), eventos de red 0, subprocesos file, uname | PASS: sockets 2 (AF_UNIX), eventos de red 0, subprocesos file, uname |
| aislamiento (d) | positivo por el mismo JSON de MCP | PASS: 3 pasajes, primero `cap::2.12.1.4` | PASS: 3 pasajes, primero `cap::2.12.1.4` |
| envoltorio | archivo falso: llega la clave, 3, 4 y 2 de salida, nada se imprime | PASS: 5 de 5 casos; archivos falsos borrados: True | PASS: 5 de 5 casos; archivos falsos borrados: True |
| corrida en seco, ramas | freno, proyección, tope, modo, corte, paralelas, sin `result`, línea mal formada, H-B2, pregunta compuesta | PASS: 11 de 11 ramas | PASS: 11 de 11 ramas |
| corrida en seco, `zsh` | los dos scripts de punta a punta con un archivo falso y modo init, y la reanudación | PASS: 12 + 8 sesiones init, 12 tras reanudar; USD 0 | PASS: 12 + 8 sesiones init, 12 tras reanudar; USD 0 |

Las dos corridas dan lo mismo: los sha256 de las 13 salidas por MCP del BM25 y de las 13 del denso r2b, el sha de los
rankings del BM25 (`54146ece…`), los 10 de la regresión y los JSON deterministas (estimación, inventario de caracteres y
antecedente de H-B2, idénticos byte a byte). En la copia de trabajo el aislamiento corrió dos veces: la primera, (b) dio FAIL
por un falso positivo de mi criterio (§12, error 7); la segunda, con el criterio corregido, PASS. La tabla muestra la segunda.

Salida de consola de la copia final (08:59:53 a 09:23:22), sin las barras de progreso del modelo ni las líneas por sesión de
la corrida en seco:

```
== copia: copia_final | 2026-10-16 08:59:53 -0300
== 1 mcp_vector/test_fragmentos_a2_1.py (venv nuevo)
bm25_analizador: PASS
bm25_determinismo: PASS
bm25_transporte: PASS
config_grafo: PASS
regresion_denso: PASS
denso_e0_vieja: PASS
denso_r2b: PASS
denso_r2b_dos: PASS
TOTAL: PASS -> data/experiment/banco_mcp/a2_1/controles/tests_fragmentos_a2_1.json
rc=0
== 2 a2_1/test_aislamiento_a2_1.py (.venv del repo; servidor con el venv nuevo) | 09:22:44
a_inventario: PASS
b_artefactos_grafo: PASS
c_puerto_neo4j: PASS
d_positivo: PASS
TOTAL: PASS -> data/experiment/banco_mcp/aislamiento/resultados/a2_1/aislamiento_a2_1.json
rc=0
== 3 a2_1/prueba_envoltorio_a2_1.py (.venv del repo) | 09:22:52
OK  1 archivo con la variable (el padre trae otra)
OK  2 archivo inexistente
OK  3 archivo sin la variable
OK  4 uso incorrecto (sin --)
OK  5 el valor no aparece en ninguna salida
TOTAL: PASS -> data/experiment/banco_mcp/a2_1/controles/prueba_envoltorio.json
rc=0
== 4 a2_1/corrida_en_seco_a2_1.py (.venv del repo; scripts zsh en modo init) | 09:22:52
OK    freno por acumulado (1,75 + 0,30 > 2)
OK    sin freno (1,65 + 0,30 <= 2)
OK    el acumulado suma smoke y H-B2
OK    meta de otro modo en la carpeta
OK    freno por proyección
OK    tope 0
OK    conteos: paralelas, línea mal formada y corte
OK    conteos: stream sin result
OK    evaluación de H-B2 (sintética)
OK    evaluación de H-B2 sin cortes
OK    pregunta compuesta
zsh init: PASS
TOTAL: PASS
rc=0
== 5 a2_1/antecedente_HB2_faseB.py (.venv del repo) | 09:23:21
{'n_sesiones': 12, 'num_turns_igual_a_tool_result_mas_1': 12, 'num_turns_igual_a_mensajes_asistente': 8, 'sesiones_con_num_turns_mayor_que_max_turns': ['SMK-04-kg'], 'sesiones_con_corte': [], 'sesiones_con_llamadas_paralelas': ['SMK-01-kg', 'SMK-02-kg', 'SMK-03-kg', 'SMK-04-kg']}
rc=0
== 6 a2_1/inventario_caracteres_e0.py (venv nuevo)
{'n_pasajes': 1768, 'n_caracteres': 2375390, 'n_distintos': 142, 'fuera_del_plano_basico': 0, 'marcas_y_formato': {'Mn': 0, 'Mc': 0, 'Me': 0, 'Cf': 0}, 'guion_blando_U+00AD': 0, 'espacio_fino_U+202F': 0} | letras no latinas: ['º', 'Σ', 'α', 'σ', 'ᶲ'] -> data/experiment/banco_mcp/a2_1/controles/inventario_caracteres_e0_tanda0_r2b_desarrollo.json
rc=0
== 7 a2_1/estimar_tramo2.py (.venv del repo)
{"paso1_smoke": 0.3827, "paso2_hb2": 0.7478, "total_tramo2": 1.1305} | P0 ref 2728
rc=0
== fin | 2026-10-16 09:23:22 -0300
```

## 9. Los comandos del tramo 2, con su costo estimado (§4 del mandato)

Los corre la autora en su terminal, desde la raíz del repo, con el «seguí»; uno por paso pago:

```
zsh data/experiment/banco_mcp/a2_1/tramo2_paso1_smoke.zsh
```

```
zsh data/experiment/banco_mcp/a2_1/tramo2_paso2_hb2.zsh
```

Cada script corre, en un solo comando,
`"$R/.venv/bin/python" -I -B data/experiment/banco_mcp/a2_1/con_clave_del_entorno.py --entorno data/experiment/evaluacion/.env -- "$R/.venv/bin/python" -B data/experiment/banco_mcp/a2_1/correr_a2_1.py --fase <smoke|hb2> --autorizado-tope 3 --freno 2 --modo real`,
con `BANCO_VENV_VECTOR` en el venv nuevo (salvo que la autora lo exporte con otro valor) y `HF_HUB_OFFLINE=1` y
`TRANSFORMERS_OFFLINE=1`. La terminal guarda solo la línea `zsh …`. El envoltorio es el de la mesa, copiado tal cual
(`83527b33…`).

| paso | qué corre | sesiones | cota (USD) |
|---|---|---|---|
| 1 | smoke: P0 de cada brazo, SMK-01 a SMK-04 en los dos brazos, E2E de cada brazo; adaptación (R7, R3) y contabilidad R9 | 12 | 0,3827 |
| 2 | H-B2: las 8 sesiones de `diseno_HB2.json` y su evaluación (§5 del diseño), con el smoke como control | 8 | 0,7478 |
| | total del tramo 2 | 20 | 1,1305 |

La cota sale de `a2_1/estimar_tramo2.py` (`a2_1/estimacion_tramo2.json`): los costos R9 medidos en la corrida 2 de la fase B
en el brazo vectorial (misma tool, mismo agente), sin descontar que `limite` pasa de 10 a 5 ni que las sesiones con
`--max-turns` chico cortan antes. Guardas (D-C): tope autorizado 3; antes de cada sesión, si el acumulado R9 de los dos pasos
más 0,30 (el `--max-budget-usd` por sesión) supera 2, FRENO sin lanzar; tras los dos P0, freno por proyección en 2,4; y
`--max-budget-usd 0.30` por sesión en el CLI. Una sesión ya corrida no se relanza (reanudación), y una meta de otro modo en
la carpeta aborta.

Salidas: el paso 1 en `smoke/resultados/a2_1/` (carpeta nueva de A2.1, §6) y el paso 2 en `a2_1/hb2/`. El brazo del grafo
no entra en el tramo 2: el CLI sigue en la versión sellada (2.1.241), así que no hay que re-validar el KG-Refinado de la fase
B (mandato, §4).

## 10. El diseño de H-B2 (§3, punto 5), escrito antes de correrlo

Documento: `a2_1/diseno_HB2.md`; sesiones: `a2_1/diseno_HB2.json`; reglas implementadas en `correr_a2_1.evaluar_hb2`. En
corto:

- **Antecedente medido** (`a2_1/antecedente_HB2_faseB.py` → `a2_1/controles/antecedente_HB2_faseB.json`): en las 12
  sesiones de la corrida 2 de la fase B, `num_turns` = `tool_result` + 1 en 12 de 12, y = mensajes del asistente en 8 de 12;
  las 4 que difieren son las del grafo con llamadas paralelas. SMK-04-kg: 9 mensajes del asistente, 13 `tool_use`, 13
  llamadas en el log R1, `num_turns` 14, `--max-turns 12`, sin corte. Ninguna sesión cortó; el brazo vectorial nunca hizo
  llamadas paralelas.
- **Hipótesis:** H-a, `num_turns` = `tool_result` + 1; H-b, `--max-turns` acota los mensajes del asistente (llamadas del
  modelo a la API), no `num_turns`. La doc no lo define: `maxTurns` es «tool-use round trips» en un lugar y «API
  round-trips» en otro (Agent SDK, TypeScript).
- **Sesiones:** 8, en los dos brazos de fragmentos, con `--max-turns` 1, 2, 3 y 12, sobre SMK-04 sola y sobre SMK-01 + SMK-03
  y SMK-01 a SMK-04 juntas (para inducir llamadas paralelas); más las 12 del smoke como controles. Preguntas: solo las de
  `smoke/preguntas_smoke.json`.
- **Lo registrado por sesión:** `num_turns`, llamadas del log R1, mensajes del asistente, `tool_use`, `tool_result`, máximo
  de `tool_use` por mensaje, `subtype`, `is_error`, si el corte disparó (`error_max_turns`), si el log R1 tiene `fin` y si hay
  `result`.
- **Cómo se decide:** R-a (un conteo queda VERIFICADO como `num_turns` si coincide en todas las sesiones), R-b (un conteo es
  compatible con lo que acota `--max-turns` si nunca pasa de k sin corte y vale k o k + 1 al cortar; CARACTERIZADO,
  INDISTINGUIBLE o NO CARACTERIZADO) y R-c (qué deja cada corte). Dos lecturas, declaradas antes: solo con lo de A2.1 y con
  el antecedente de la fase B sumado. Sobre el antecedente solo, la evaluación ya da R-a VERIFICADO y R-b NO CARACTERIZADO
  (sin cortes), con un solo conteo compatible: los mensajes del asistente.
- **Costo:** cota USD 0,7478 (8 sesiones); guardas del banco.

## 11. Qué intérprete usa cada script y cada prueba (incluido el tramo 2)

«venv nuevo» = `~/INGENIERIA IA/TESIS/venvs/banco_vector_py312/bin/python` (3.12.13, §3); «`.venv` del repo» =
`.venv/bin/python` (3.10.13, conda-forge), sin tocarlo. Todo con `-B`; lo que carga el modelo, con `HF_HUB_OFFLINE=1` y
`TRANSFORMERS_OFFLINE=1`.

| script o prueba | intérprete | por qué |
|---|---|---|
| `mcp_vector/servidor_mcp_vector.py`, modo denso y modo BM25 | venv nuevo (por `BANCO_VENV_VECTOR` en los JSON de MCP, o el del test que lo lanza) | el entorno del servidor de fragmentos; sin el driver del grafo |
| `mcp_vector/construir_indice.py` (denso y BM25) | venv nuevo | el del índice sellado |
| `mcp_vector/test_fragmentos_a2_1.py` y lo que lanza (`construir_indice.py`, `test_mcp_vector.py`, el servidor) | venv nuevo | como `test_mcp_vector.py` («venv del bake-off») |
| `a2_1/sonda_auditoria.py` | venv nuevo | corre el servidor auditado |
| `a2_1/inventario_caracteres_e0.py` | venv nuevo | importa `construir_indice` |
| `a2_1/test_aislamiento_a2_1.py` | `.venv` del repo; el servidor, con el venv nuevo | como `aislamiento/test_aislamiento.py` |
| `a2_1/con_clave_del_entorno.py` y `a2_1/prueba_envoltorio_a2_1.py` | `.venv` del repo, con `-I` el envoltorio | trae `python-dotenv`; la forma del §4 del mandato |
| `a2_1/correr_a2_1.py`, `a2_1/lanzar_agente_a2_1.py` (tramo 2 y corrida en seco) | `.venv` del repo; el servidor, con el venv nuevo | como `smoke/correr_smoke.py` |
| `a2_1/corrida_en_seco_a2_1.py` | `.venv` del repo (los scripts `zsh`, con `A21_PYTHON` = ese mismo intérprete, porque la copia no lleva `.venv`) | |
| `a2_1/tramo2_paso1_smoke.zsh`, `a2_1/tramo2_paso2_hb2.zsh` | `zsh`; adentro, `.venv` del repo para el envoltorio y el runner, y el venv nuevo para el servidor | |
| `a2_1/antecedente_HB2_faseB.py`, `a2_1/estimar_tramo2.py` | `.venv` del repo | solo leen metadata |
| `claude` (modo init en el aislamiento y en la corrida en seco; real en el tramo 2) | Claude Code 2.1.241 | la versión sellada |

## 12. Errores propios, con su causa

1. **Usé `sleep` una vez**, en un comando de control mientras esperaba la reconstrucción del índice viejo (`sleep 1;` antes de
   leer el log). El despacho lo prohíbe («sin esperas programadas ni `sleep`»). Causa: quise dar un respiro antes de leer el
   log en vez de esperar el aviso de la tarea en segundo plano. No cambió nada (un segundo, sin escribir), pero es una
   violación de la regla. Después esperé solo por los avisos y por controles sin espera.
2. **Una búsqueda de un jar de Lucene en la carpeta personal superó los 300 s** y quedó en segundo plano. Excluía, por
   `-prune`, `fuera_del_repo/` entero, `~/Desktop/traspaso_etapa2/`, `~/Library/Containers`, la papelera y todo
   `NO_ABRIR_*`; no encontró nada (por eso las fuentes de Lucene se leyeron en la web). Causa: recorrí la carpeta personal
   entera en vez de lugares acotados.
3. **Criterios de (c) demasiado estrictos en la primera versión del test de aislamiento**: exigía cero subprocesos y comparaba
   la familia de socket como texto cuando la sonda la registraba como número. La corrida preliminar (con el `.venv` del repo,
   no oficial) lo mostró; corregí la sonda (nombre de la familia, solo el nombre del ejecutable) y el criterio (§2,
   decisión 11). No cambia el código del servidor.
4. **Dos defectos del runner y del test detectados antes de correrlos**: una expresión mal armada para detectar llamadas
   paralelas (ahora se cuenta el máximo de `tool_use` por mensaje en el lanzador) y una cadena sin `f` en el fixture del
   analizador. Ninguno llegó a una corrida.
5. **El fixture del analizador usaba como entrada una palabra con guion que es uno de los términos del grep de
   convenciones**; la cambié por «co-deudores», que prueba la misma regla (el guion corta).
6. **Mi primer comando de lectura del banco cambió el directorio de trabajo de la sesión** (un `cd` dentro del comando). No
   escribió nada; desde ahí usé rutas absolutas.
7. **El criterio de (b) del aislamiento dio un falso positivo en la primera corrida de la copia de trabajo** (08:55:22): marcó
   como «archivo del modelo» el `entry_points.txt` del `dist-info` de `huggingface_hub`, porque buscaba «huggingface» en
   cualquier ruta abierta. Ese archivo es metadato de un paquete instalado y no importado: lo lee el recorrido de los entry
   points de todos los paquetes del venv (se leen los 63 `dist-info`). En el `.venv` de la corrida preliminar ese paquete no
   existe, por eso no apareció antes. El servidor no importó ningún módulo prohibido ni abrió nada de la caché del modelo.
   Corregí el criterio (archivos del modelo: la caché de Hugging Face, `harrier`, `.npy` y `.safetensors`; los `dist-info`
   leídos se listan aparte, en `metadatos_dist_info_leidos`) y re-corrí el test (08:57:00): (a) a (d) en PASS. La salida que
   falló está en el paquete (`aislamiento_a2_1_copia_trabajo_primera_FAIL_b_A2_1a.json`).

## 13. La foto del repo, los `.pyc` y el grep de convenciones

Foto sha256 del repo entero sin `.git` (`scripts/foto_repo.py` del scratchpad, en el paquete con las fotos): cada archivo por
su sha256, salvo los `.env` y los `NO_ABRIR_*`, que van solo por tamaño y fecha (`os.lstat`, sin abrirlos), y los enlaces
simbólicos, por su destino. El comparador (`scripts/comparar_fotos.py`) falla si algún cambio cae fuera de la §6 o toca lo
de U-A2.0-banco que no cambia (la config y el test del denso viejo, sus resultados y el índice viejo).

| foto | hora | entradas | `.pyc` (fuera de los venvs) |
|---|---|---|---|
| antes (`foto_antes`) | 16/10/2026 00:51:32 | 50.909 | 10.158 (243) |
| justo antes de escribir | 08:57:52 | 50.909 | 10.158 (243) |
| después de escribir, sin el FRENO | 08:58:28 | 50.959 | 10.158 (243) |
| antes de la copia final | 08:58:55 | 50.959 | 10.158 (243) |
| después de la corrida final | 09:23:43 | 50.959 | 10.158 (243) |
| al frenar, con este FRENO | después de escribirlo (`foto_repo_despues_A2_1a.json`) | 50.959 | 10.158 (243) |

- **Antes de escribir contra al frenar:** de las 00:51:32 a las 08:57:52, 0 cambios (las corridas preliminares con el
  `.venv` del repo no escribieron nada en él); después de escribir (08:58:28), 50 nuevos y 2 modificados, los 52 de
  `lista_al_repo_A2_1a.txt`: 25 en `a2_1/`, 14 en `mcp_vector/` (8 archivos y los 6 de los dos índices), 9 en
  `aislamiento/resultados/a2_1/` y 2 en `mcp_kg/`; modificados, `mcp_vector/servidor_mcp_vector.py` y
  `mcp_vector/construir_indice.py`; 0 borrados; 0 fuera de la §6. Después saqué del repo uno de los 50 (el stream de init,
  abajo) y escribí este FRENO: al frenar, 50 nuevos (los 49 que quedan y este FRENO) y los mismos 2
  modificados, 0 fuera de la §6 (`comparacion_fotos_antes_despues_A2_1a.json`). Esa última foto se toma después de escribir
  este archivo: su resultado va en el mensaje del FRENO.
- **Alrededor de la corrida final** (foto justo antes de hacer la copia final y justo después de terminar sus tests):
  de las 08:58:55 a las 09:23:43, 0 nuevos, 0 borrados, 0 cambiados.
- **Los `.pyc`:** 10.158 en todas las fotos, 243 fuera de los dos venvs, siempre los mismos; ningún `.pyc` en las dos copias
  (todo corrió con `-B`).
- **Las copias:** las dos con el rsync de la cláusula; en las dos, `find … .env/.env.*/*.env/NO_ABRIR_* | wc -l` = 0 y
  `find -type l | wc -l` = 0, controlados antes de correr nada. rsync saltó, por `--no-links`, 336 enlaces simbólicos en
  `data/experiment/ev2_corrida/navegabilidad/trazas_nav/` (120 en `ev2_base_run3`, 88 en `ev2_base_v2` y 128 en
  `ev2_base_v3`); no se abrieron. Las copias quedan sin el `.env.example` de `run_2_papers/code/` y sin el `NO_ABRIR_` del repo
  (excluidos por la cláusula); ningún control de este tramo compara la copia con el repo archivo por archivo fuera de
  `data/experiment/banco_mcp/`.
- **Carpetas vedadas:** no abrí, listé ni copié nada de ellas; la única búsqueda que podía recorrerlas (la del jar de Lucene)
  las excluía. Del scratchpad de la mesa abrí solo el envoltorio, por su ruta.
- **Grep de convenciones** (`data/experiment/segmentacion_oficial_e0r2/s0_4/scripts/grep_convenciones.py`, corrido sobre una
  copia de esos archivos en el scratchpad, sin escribir en el repo; salida en el paquete): control positivo 16 de 16 términos;
  46 archivos revisados (los 45 de texto que llevé al repo, sin los 6 de los índices, y este FRENO); total 0. Una primera pasada, con el stream de init todavía en el repo, dio 5
  coincidencias, todas en ese archivo (abajo).
- **El stream de init del aislamiento no queda en el repo.** `aislamiento/resultados/a2_1/init/stream_AISL-fragmentos_bm25.jsonl`
  es la salida literal de `claude -p` y su evento `system/init` trae el `cwd` absoluto de la copia, que contiene la carpeta
  personal (el grep lo marcó por eso). En U-A2.0-banco esos streams quedaron en el repo, declarados (README del banco, «Nota
  de confidencialidad»); acá lo saqué, por la regla de no dejar nombres en artefactos que persisten. Su sha256 era
  `3e0d55d6ae8d14383cdf41f22a82dc5b6a768891e18993484a0448f2d1d0da70` (2.023 bytes); el original queda en el scratchpad de la
  sesión hasta que lo borre el limpiador, y al paquete va una copia con el `cwd` enmascarado. Lo que el aislamiento usa del
  stream (tools, servidores, permisos) está en `meta_AISL-fragmentos_bm25.json`, con el `cwd` relativo, y se regenera a USD 0
  corriendo el test. [DECIDE LA AUTORA]: dejarlo así o restaurar el literal, como en U-A2.0-banco.
- **En el paquete, las fotos van enmascaradas** (`enmascarar_paquete_A2_1a.py`, que va con ellas): la carpeta personal, como
  `$HOME`, en los destinos de los enlaces simbólicos del repo (338 por foto: los 336 de `trazas_nav/`, el `.venv` y el
  `.venv-app`), y las palabras del nombre de la cuenta, como `<nombre>`, en las 3 claves preexistentes del repo que las
  contienen; la cantidad de entradas no cambia. Lo mismo en la copia del checkpoint y en la primera pasada del grep. El
  grep sobre el paquete da después solo nombres de archivos preexistentes del repo (en las claves de las fotos), palabras del
  texto de las normas (en los pasajes del corpus) y el patrón de la carpeta temporal dentro del propio script de enmascarado.

## 14. Lo que queda abierto

- **[DECIDE LA AUTORA], antes del smoke del tramo 2** (§2 y §4): el nombre del servidor MCP (decisión 5), la descripción de la
  tool y del bloque del prompt (6), la descripción de `limite` (7), la consulta del BM25 simétrica o con la pre-tokenización
  del brazo del grafo (§4, diferencia 5) y la norma de largo cuantizada o exacta (§4, diferencia 8). Si alguna cambia, cambian
  el sha de la config o del índice BM25 y hay que correr de nuevo sus tests (USD 0) antes del tramo 2.
- **El brazo del grafo de A2:** sus dos configuraciones están listas; la carga en Neo4j, su test positivo y su configuración
  de agente (JSON de MCP y brazo) van a A2.2 o al tramo 3.
- **La réplica del `spanish` de Lucene** está verificada contra las fuentes y contra lo esperado a mano, no contra Lucene en
  ejecución (§4, diferencia 7).
- **El tramo 2** (los dos scripts `zsh`, §9) y **el tramo 3** (el pre-registro de A2.2 en BORRADOR) esperan su «seguí».
- **Nada commiteado** y ningún mensaje de commit preparado: los archivos nuevos del repo quedan sin rastrear y los dos
  modificados, sin commitear, hasta que la autora decida.

## 15. Cierre

- **Checkpoint:** `checkpoint_A2_1.md`, en el scratchpad de la sesión `94968c98-6fa5-449c-954b-42ee7ee26062`; una copia va en el
  paquete.
- **El paquete:** `revision_A2_1_FRENO_a/`, en el scratchpad de la sesión, con su `manifest.txt` (sha256 y una línea por
  archivo): el FRENO, el código y las configuraciones con nombres únicos, los diffs, los índices, las salidas de las dos
  corridas de tests con sus logs R1, el entorno nuevo (pip freeze, requisitos, sha de las ruedas y salidas de pip), las fotos
  del repo, el grep de convenciones y los controles de las copias.
- **La copia permanente:** con `ditto`, a
  `~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/94968c98-6fa5-449c-954b-42ee7ee26062/scratchpad/revision_A2_1_FRENO_a/`.
  La verificación contra el manifiesto va en el mensaje del FRENO.
- Nada commiteado, ningún mensaje de commit preparado, nada escrito en la memoria.

FRENO A2.1-a. Espero el «seguí» para el tramo 2.
