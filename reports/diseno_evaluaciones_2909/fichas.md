# Fichas de diseño de las evaluaciones — U-DISENO-EVAL (29/09/2026)

Insumo para la escritura de los capítulos 4, 5 y 6 con la estructura fijada el
29/09. No es prosa de la tesis. Base: HEAD `8e0597c`. Unidad de solo lectura:
las únicas escrituras están en `reports/diseno_evaluaciones_2909/`.

**Convenciones.**
- `:n` es la línea n de `docs/plan_tesis.md` en `8e0597c`.
- Estados: **(a)** decidido y registrado como está; **(b)** decidido de otra
  forma; **(c)** no registrado o pendiente; **(d)** descartado.
- Donde una fuente nombra a personas, cito la ruta y escribo «los mentores».
- Toda cifra lleva su comando en la sección «Comandos» o la marca NO VERIFICADO.
- Registro de las reuniones del 18/08 y del 19/08: no hay minuta propia en el
  repo (búsqueda: `grep -rl -E "18/08|19/08" docs --include='*.md'`). Lo
  acordado quedó en el changelog v2 del plan (`:34-39`, 18/08), en
  `docs/tesis/esqueleto_intro.md:208-212` (dos versiones, reunión del 19/08) y
  en `docs/tesis/esqueleto_intro.md:438-439` (diseño del 18 y 19/08). Esa
  tabla es insumo de reunión, no decisión sellada.

## Parte 1 — Estado de H1 a H13

**H1 · Claude Code (`claude -p`) con contextos aislados, para esta evaluación y para todas — (b).**
- Registrado para la comparación contra fragmentos. El banco de Claude Code con
  servidores MCP (A2.0-gate `:327`, A2.0-banco `:328`) usa `claude -p` no
  interactivo, en modo `--bare`, sin herramientas incorporadas y con MCP
  estricto (`data/experiment/banco_mcp/README.md:146-150`).
- El aislamiento está configurado y verificado de punta a punta: «aislamiento
  end-to-end (a)–(d) con `respondible:false` y 0 llamadas ante pedidos fuera de
  capacidad» (`:328`). Es una precondición de A2.1 (`:331`).
- Qué cambió: la recomendación de usarlo «para todas» no se adoptó. El
  principio 8 (`:268-274`) declara dos instrumentos no intercambiables: el
  **harness congelado** (Haiku 4.5, tres herramientas, 15 llamadas) sostiene
  todo lo sellado (Fase 2.3, escalón 1, EV2, A1.4) y el **banco** sostiene la
  comparación. Sus resultados no se cruzan en una misma tabla.

**H2 · Brazo como variable declarada: un agente, un prompt; cambia solo el servidor MCP — (a).**
- Fuentes: changelog v2 (`:35-37`); A2.0-banco (`:328`: «el brazo de evaluación
  pasa a ser una variable declarada (qué servidor MCP se enchufa)»); A2.1
  (`:331`).
- El prompt es una plantilla más el bloque de herramientas del brazo, pasado
  como argumento de `claude -p`. El diff entre brazos es solo ese bloque
  (`data/experiment/banco_mcp/README.md:162-165`).
- Configuración sellada con sha en cada traza (R10): modelo `claude-sonnet-5`,
  CLI 2.1.241 (`data/experiment/banco_mcp/agentes/config_agentes.json`).

**H3 · Embeddings elegidos del ranking MTEB con filtros y configurados según la model card; candidato Qwen3-Embedding-0.6B — (b).**
- Filtros de entrada iguales a los acordados: retrieval, español o
  multilingüe, licencia abierta, ≤ 1B (`docs/decision_modelo_embeddings.md:42-44`).
- Qué cambió: el ranking MTEB sirvió solo como criterio de entrada, y la
  elección se hizo por un bake-off propio sobre el corpus (`:16-38` del laudo,
  conclusión en `:37-38`). Qwen3-Embedding-0.6B entró al bake-off (`:88`) y no
  fue elegido; se eligió `microsoft/harrier-oss-v1-0.6b` (`:119`).
- La configuración se tomó de la card, con una decisión propia declarada:
  `float32` en lugar del `bfloat16` de `config.json` (`:125-158`, en especial
  `:150-152`).
- Contradicción (regla d): `docs/tesis/esqueleto_intro.md:438` dice «modelo de
  embeddings elegido desde MTEB leyendo la model card», y el laudo dice que los
  rankings «no deciden esta elección» (`:16`).

**H4 · Embeddings sobre los nodos del grafo, con el mismo motor, para la comparación — (a).**
- B1.10 (`:365`): índice denso HNSW en Neo4j y retriever híbrido BM25 + denso
  con `harrier-oss-v1-0.6b`; «si gana entra como configuración del brazo KG en
  A2». El laudo A2.0b lo prevé (`docs/decision_modelo_embeddings.md:10-11`).
- Estado de ejecución: B1.10 sin marcar `[PENDIENTE]`. A1.8 lo lista como
  mejora candidata («búsqueda híbrida con el modelo denso del bake-off», `:323`).

**H5 · Misma fragmentación (E0) para los dos sistemas — (a).**
- A2.1 (`:331`): «Baseline BM25 sobre los chunks de E0 (unidades estructurales
  + herencia; mismo texto que vio el extractor)». Laudo 2 del 20/09: sistema por
  fragmentos definido por fragmentos de E0 con herencia, top-k=5 y el mismo
  agente (`:331`). B6.3 (f) lo reusa (`:750`; D-h2 `:981`).

**H6 · Reportes de las evaluaciones armados desde las trazas, más allá de las métricas — (a).**
- A2.0-reportes (`:329`): «Agente de reportes sobre trazas ya adaptadas: arma el
  informe con las tablas del repo desde las trazas del banco». Sin marcar
  `[PENDIENTE]` y declarado recortable (`:877`).
- Ya hecho, en otra forma: la atribución A0.2 por replay determinístico de
  trazas (`:307`; clases en `data/experiment/ev2_reporte/regla_atribucion.md:152-159`).

**H7 · Preguntas sintéticas desde párrafos: un modelo propone la pregunta, otro redacta la respuesta de referencia; instancia sin contexto; revisión una por una — (b).**
- Qué se conserva: la generación por instancia aislada, que leyó solo los PDF y
  el mapa de territorio (`data/experiment/exploracion/ev2_fidelidad/registro_generacion_ev2_fidelidad.md:8-21`);
  en la tanda 0, aprobadas por la autora tras revisión contra los PDF (`:729`).
- Qué cambió: no hay respuesta de referencia ni un segundo modelo. Una misma
  instancia redacta la pregunta y el gold, que son el ancla y de 2 a 5
  criterios verificables, cada uno con su cita textual del PDF
  (`registro_generacion_ev2_fidelidad.md:61-65`).
- Para el conjunto final, B6.3 (a) pide «preguntas nuevas con gold por
  criterios» (`:750`).

**H8 · Precisión intrínseca: 100 tripletas nodo–relación–nodo con evidencia, dos juicios, de a 10, adjudicación de la autora como referencia — (a).**
- B4.1 (a) (`:403-408`); calibración de a 10 hasta 100 (`:415-416`); B4.2 en
  tandas de 10 con freno tras la primera (`:424-426`).
- Agregados al diseño: muestra estratificada por tipo de relación y por TO
  (`:404-405`); Wilson para toda proporción y precisión por etapa del pipeline
  (`:396-402`).
- Secuencia, laudo D-f (`:393`; `docs/laudo_D-f_secuencia_tripletas.md`): el
  instrumento se valida sobre KG-Reextraído-r1 y la medición que cuenta es
  B6.3 (d).
- `[PENDIENTE]`: el pre-registro que cita B4.1,
  `docs/preregistro_evaluacion_tripletas.md`, es NO ENCONTRADO (no existe);
  inconsistencia registrada entre B4.2 y B6.3 (d) (`:424`).

**H9 · Juez de tripletas calibrado contra las primeras adjudicaciones, con acuerdo medido antes de usarlo — (a).**
- B4.1 (c) y (d) (`:414-418`): prompt congelado por sha, N=3 modal, ciego;
  acuerdo juez–humana en las dos direcciones; escala solo si el acuerdo lo
  habilita, con umbral declarado. B4.3 (`:427`). `[PENDIENTE]` de ejecución.

**H10 · Clasificación por dificultad: autora frente a experto; etiqueta sugerida por un modelo y confirmada por una persona con información o enlaces — (b).**
- Registrado como «categorización asistida por LLM de dificultad/experticia
  para priorizar qué adjudica la autora» (B4.1 (f), `:420-421`).
- Qué no está: la confirmación humana de la etiqueta con la información o los
  enlaces para verificarla, y la derivación a un experto.

**H11 · Recall intrínseco: fragmentos chicos, tripleta más importante, ranking por otro modelo, top-100 calibradas por lectura humana, recall@k, ausentes adjudicadas después — (a).**
- B4.1 (b) (`:409-414`), orden de las top-100 validado por la autora
  (`:416`), ausentes post hoc (`:419-420`); métricas recall@10/50/100 (B4.3,
  `:429-430`). Material: fragmentos frescos; EV2 no se abre (`:421-422`).

**H12 · Dos versiones del grafo: la evaluada, sin cambios; la posterior, con las correcciones — (a).**
- Principio 9 (`:275-282`) y su registro del 20/09 (nombres «el grafo
  evaluado» y «el grafo corregido», `:282`); reunión del 19/08 en
  `docs/tesis/esqueleto_intro.md:208-212`; ciclo de releases B2.6 (`:378`) y
  release r2 (`:382`). Coincide con la decisión 2 del mandato.

**H13 · El grafo evaluado también en tareas extrínsecas — (a).**
- Principio 9: «Toda evaluación (extrínseca o intrínseca)» (`:275-276`);
  fidelidad EV2 (desarrollo) y B6.3 (b), (e) y (f) sobre el grafo escalado
  (`:750`).

## Parte 2 — Preguntas Q1 a Q6

**Q1 · Harness y modelo de la medición final (B6.3) y de la comparación (A2).**
- A2: banco de Claude Code con MCP, `claude-sonnet-5`, el mismo agente y prompt
  en los dos brazos (`:331`; `config_agentes.json`, clave `modelo`). No usa el
  harness congelado.
- B6.3 (f): el sistema por fragmentos «definido por A2.1 (… mismo agente con una
  sola herramienta de recuperación)» (`:750`), sobre el banco (M-15, `:1246`).
- B6.3 (b), fidelidad del grafo: **NO ENCONTRADO**. Ninguna fila declara qué
  instrumento usa.
- Desarrollo: EV2 y las celdas de la tanda 0 usaron el harness congelado
  (`data/experiment/evaluacion/harness.py:47`, Haiku `claude-haiku-4-5-20251001`;
  `:50`, 15 llamadas) y su variante sobre Neo4j (`GraphAgentNeo4j`, `:323`).
- A1.8 congela la configuración del agente antes del pre-registro de B6.3
  (`:323`).
- Ver la contradicción C-4.

**Q2 · Conjunto de preguntas de la comparación.**
- El plan dice «mismo juez de fidelidad EV2, mismas 40 preguntas» (A2.1 `:331`;
  P-2 `:1254`).
- El «documento de cobertura del 01/09» es NO ENCONTRADO con ese nombre. La
  frase está también en `docs/tesis/inventario_recurso.md:340` y `:816`
  (generado el 31/08 sobre `6cb0121`; alta en `2f511ba`, 04/09).
- Para B6.3 (f), el conjunto es el del test final (D-h2, `:981`), fresco y sin EV2
  (`:750` (a)).
- Contradicción reportada, no resuelta: ver C-2.

**Q3 · Brazos de la comparación y embeddings en los nodos.**
- Laudo 2 del 20/09 (`:331-333`): el grafo, fragmentos con BM25 (principal) y
  fragmentos con denso `harrier-oss-v1-0.6b` (secundaria). El híbrido B1.9 es
  exploración sobre el conjunto de desarrollo, no entra a B6.3 y se reporta
  aparte.
- El brazo del grafo usa hoy BM25 en `buscar_nodos` (firma v1, `:328`).
  Embeddings en nodos solo si B1.10 gana (`:365`), `[PENDIENTE]`.

**Q4 · Modelo de embeddings (laudo A2.0b).**
- Elegido `microsoft/harrier-oss-v1-0.6b` (`docs/decision_modelo_embeddings.md:119`).
- Criterio: bake-off propio sobre el corpus, con el MTEB solo como entrada (`:16-38`;
  razones `:96-117`).
- Configuración leída de la fuente: revisión `f9b9dc8d…`; instrucción
  `web_search_query` solo en consultas; documentos sin instrucción; pooling por
  último token; L2; coseno; 1.024 dimensiones; `max_seq_length` 32.768;
  `float32` por decisión propia (`:125-158`).

**Q5 · ¿El harness comprueba que el punto citado sea el que responde?**
- En el harness, no. Solo registra si cada cita sale de procedencias que el
  agente vio (`data/experiment/evaluacion/harness.py:323-345`, definición
  congelada de «cita fiel»; control en `:551-560`).
- La existencia de la cita y que caiga en el ancla se miden después, con
  `scripts/ucita2_indicadores.py:9-20` (indicadores 2 y 3), sin juez ni API.
  Son el componente (e) de B6.3 (`:750`).

**Q6 · ¿Las «12 trazas» y las «26 celdas, 25 acuerdos, 1 desacuerdo» son el mismo material?**
- Sí: es el mismo material, `data/experiment/evaluacion/02_calibracion_juez.md`
  (un solo commit, `d56020e`), con 12 filas = 12 trazas (6 preguntas × 2
  corridas; `:13-24`) y el diccionario `HUMAN` de
  `data/experiment/evaluacion/judge.py:309-325` (12 trazas).
- Pero «26 celdas, 25 acuerdos, 1 desacuerdo» (P-5, `:1257`) no se reproduce.
  Las celdas con veredicto humano son 20, con 20 acuerdos y 0 desacuerdos.
- El 25 y el 1 son los símbolos ✅ y ❌ de todo el archivo:
  - la línea 7 (título del resultado): 1 ✅;
  - la línea 9 (leyenda): 1 ✅ y 1 ❌;
  - la tabla, `:13-24`: 20 ✅;
  - las metas, `:32-34`: 3 ✅.
- `docs/tesis/mapa_fuentes_cap_esquema.md:107` dice «25 celdas comparadas, 0 ❌»,
  que es otra lectura del mismo conteo.
- Ver la contradicción C-3.

## Contradicciones encontradas (regla d: se reportan, no se resuelven)

- **C-1 · Estructura del informe.** El plan conserva la numeración anterior al
  29/09:
  - el grafo evaluado en la sección 4.5 y medido en el capítulo 8 (`:282`);
  - promesas a los capítulos 5, 6, 7 y 8 (`:1253-1258`);
  - «El agente y el sistema de consulta» como primera sección del capítulo 5
    (`:826`).
  La estructura del mandato ubica el agente en 4.7, las evaluaciones en el
  capítulo 5 y la actualización en 6.4.
- **C-2 · Conjunto de la comparación de desarrollo.** Hay tres textos que chocan:
  - A2.1 usa las 40 de EV2 (`:331`, `:1254`);
  - A1.8 fija que «EV2 se usa solo para ajustar, y ninguna medición nueva sobre
    EV2 se reporta como resultado» (`:323`);
  - el principio 7 admite una evaluación única por sistema con pre-registro
    (`:264-267`).
  A2 se reporta como validación de diseño (D-h, `:976-977`).
- **C-3 · Calibración del juez de la Fase 2.3.** Chocan P-5 (`:1257`) y
  `mapa_fuentes_cap_esquema.md:107` con el archivo fuente: 20 celdas, 20
  acuerdos, 0 desacuerdos (ver Q6).
- **C-4 · Instrumento de B6.3.**
  - (f) corre en el banco (Sonnet 5, MCP; `:1246`), mientras que (b) no tiene
    instrumento declarado.
  - A1.8 afina `GraphAgentNeo4j`, que es la familia del harness congelado
    (Haiku), «antes del pre-registro de B6.3» (`:323`).
  - El principio 8 prohíbe cruzar los dos instrumentos en una tabla (`:271-272`).
- **C-5 · H3.** `docs/tesis/esqueleto_intro.md:438` contra
  `docs/decision_modelo_embeddings.md:16-38`.
- **C-6 · Marcas de la adjudicación de la tanda 0.**
  - `8e0597c` (29/09): «las 174 marcas las puso una instancia de modelo, no la
    autora», y el cierre debe recomputarse.
  - El anexo E5.c, decisión 5 (`docs/mandatos/UTANDA0_2A_E5c_adjudicacion.md`,
    `0488a9b`), pide que la sesión de marcado sea de la autora y que ningún
    modelo proponga marcas.
  - El pre-registro de la tanda 0 fija la adjudicación ciega del protocolo de C1
    (`docs/preregistro_tanda0.md:308-309`), donde la marca humana es la
    definitiva.
  - Afecta los ítems 5.2 y 5.3 (ver los bloques).
- **C-7 · Documento de cobertura del 01/09:** NO ENCONTRADO con ese nombre (ver Q2).
- **C-8 · Quién adjudica las tripletas (agregado de U-DISENO-EVAL-2).** Cuatro
  fuentes, todas en `8e0597c`:
  - plan, bloque B4: «la autora adjudica primero **de a 10** hasta 100
    (correctitud + importancia)» (`:415-416`) y «Reemplaza el diseño anterior
    de anotación ciega de tripletas gold sobre 25 unidades» (`:393-394`);
  - registro del 04/09, §3: «si un experto del dominio actúa de anotador sobre
    un **subsample**, y se reportan métricas de performance con estadística
    sobre esa muestra» (`docs/registro_reunion_mentores_2026-09-04.md:81-83`),
    con destino «alimenta **B4**» (`:94`);
  - propuesta: «contra un \textit{gold standard} construido por anotación
    manual sobre una muestra representativa del corpus» (`docs/ppf/main.tex:134`)
    y «Un \textit{gold standard} de tripletas anotadas manualmente» (`:166`);
  - plan, promesas del PPF sin cumplir: «(a) gold standard de tripletas anotado
    a mano — declarado "no negociable"» (`:236-238`); el encabezado de B4 la
    repite: «(promesa "no negociable" del PPF)» (`:391`).
  - El choque: B4 pone a la autora como referencia y reemplaza el gold anotado;
    el registro del 04/09 pone a un experto del dominio como anotador de una
    submuestra y lo destina a B4; la propuesta y el plan sostienen el gold
    anotado a mano como promesa. Ninguna línea del bloque B4 (`:391-439`) nombra
    al experto; el plan lo registra solo en U-PREP-CONTACTO (`:1152-1153`), y
    C2.1 sigue listando el «gold de tripletas» como entregable (`:836`).
  - Nota de búsqueda: `grep -n "no negociable"` da solo `:391`, porque en
    `:237-238` la frase está partida entre dos líneas; `:236` sale con
    `grep -n "Promesas del PPF sin cumplir"`.
  - Relación: H10 y F-3 tratan al experto solo como destino de las tripletas
    difíciles (B4.1 (f), `:420-421`); C-8 es previa, porque pregunta quién es la
    referencia de la adjudicación.
- **C-9 · Costo de cada corrida de evaluación (agregado de U-DISENO-EVAL-2).**
  Registro PARCIAL: hay costo real por corrida en desarrollo, pero ninguna fila
  declara dónde y cómo se reporta el costo de cada corrida en el informe.
  - Fidelidad en desarrollo, registrado:
    - EV2: el protocolo fija un tope por corrida, declarado en la autorización
      con estimación previa (`docs/protocolo_corrida_ev2.md:143-147`); el
      pre-registro de fidelidad no menciona costo
      (`docs/preregistro_evaluacion_fidelidad_ev2.md`, búsqueda vacía). El
      reporte da el costo por línea con archivo y campo: USD 35,62 en total
      (`data/experiment/ev2_reporte/reporte_ev2.md:380-398`).
    - C1, r1: estimación y tope en el pre-registro
      (`data/experiment/ev2_r1/preregistro_ev2_r1.md:191`); costo real USD 7,29
      (`:361`) = agente base 1,409 + juez base 1,4415 + agente §7 2,4632 + juez
      §7 1,9746 (`data/experiment/ev2_r1/reporte/gasto_etapa1_r1.json:26`,
      `:99-100`; `gasto_s7_r1.json:75`, `:147-148`).
    - Tanda 0, E5: costo por celda, con agente y juez, base y §7, en
      `reports/tanda0/tabla_celdas_E5.json` (`gasto_total` en `:93`, `:198`,
      `:302` y `:406`): C2 6,6585, C3 6,2182, C4 6,1359 y C5 2,2451, total
      21,2577 (`gasto_E5`, `:526`; plan `:724`). Estimación y tope en el
      pre-registro (`docs/preregistro_tanda0.md:704`, `:738-768`, `:819-823`).
  - Comparación: sin corrida. A2.1 pone «costo por pregunta» entre las
    predicciones (`:331`); A2.3 pide «latencia p50/p95, costo/pregunta, costo de
    construcción → **gráfico Pareto fidelidad-vs-costo**» (`:333`); A2.2 está
    estimada en ~USD 15 (`:332`); «el banco computa costo desde tokens con
    precios sellados» (`:327`). Pre-registro de A2.1: NO ENCONTRADO (ninguno de
    los nueve archivos `preregistro` del árbol es de A2).
  - Medición final, B6.3 (b) y (f): tope de costo en el pre-registro y fórmula
    de estimación marcada ESTIMACIÓN NO VERIFICADA (`:750`); ninguna fila dice
    cómo se reporta el costo medido.
  - Propuesta y plan: «Se reportará adicionalmente costo y latencia de
    inferencia» (`docs/ppf/main.tex:134`); el plan registra «(d) latencia
    p50/p95 — no medida» (`:240`).
  - Contradicción (se reporta, no se resuelve): B6.3 dice «juez de fidelidad
    USD 7,29 por 40 preguntas sobre r1 = USD 0,18 por pregunta» y usa
    `c_juez ≈ 0,18` junto a un `c_agente` aparte (`:750`); según los archivos de
    gasto, los 7,29 incluyen agente base y §7, y el juez suma 1,4415 + 1,9746 =
    3,4161 (`docs/preregistro_tanda0.md:741-742` y `:766-768`).
  - Comandos de C-8 y C-9 (regla i), todos contra `8e0597c`:
    ```bash
    git show 8e0597c:docs/plan_tesis.md | grep -n "la autora adjudica\|Reemplaza el diseño anterior"
    git show 8e0597c:docs/registro_reunion_mentores_2026-09-04.md | grep -n "anotador\|experto"
    git show 8e0597c:docs/ppf/main.tex | grep -n "gold standard"
    git show 8e0597c:docs/plan_tesis.md | grep -n "no negociable\|Promesas del PPF sin cumplir"
    git show 8e0597c:docs/plan_tesis.md | awk 'NR>=391 && NR<=439' | grep -c -i 'experto\|experta\|anotador\|industria'
    git ls-tree -r --name-only 8e0597c | grep -i preregistro
    git show 8e0597c:docs/preregistro_evaluacion_fidelidad_ev2.md | grep -c -i 'costo\|USD\|tope\|gasto'
    PYTHONDONTWRITEBYTECODE=1 python3 -c "import json,subprocess;d=json.loads(subprocess.check_output(['git','show','8e0597c:data/experiment/ev2_reporte/salida/recomputo_ev2.json']));print(round(sum(x['usd'] for x in d['costos']['lineas']),4))"
    PYTHONDONTWRITEBYTECODE=1 python3 -c "import json,subprocess;g=lambda p:json.loads(subprocess.check_output(['git','show','8e0597c:data/experiment/ev2_r1/reporte/'+p]));e=g('gasto_etapa1_r1.json');s=g('gasto_s7_r1.json');print(e['agente_base']['usd'],e['juez_base_usd'],s['agente_s7_usd'],s['juez_s7_usd'],round(e['total_etapa1_usd']+s['total_s7_usd'],4),round(e['juez_base_usd']+s['juez_s7_usd'],4))"
    PYTHONDONTWRITEBYTECODE=1 python3 -c "import json,subprocess;d=json.loads(subprocess.check_output(['git','show','8e0597c:reports/tanda0/tabla_celdas_E5.json']));print({k:v['gasto_total'] for k,v in d['celdas'].items()},d['gasto_E5'])"
    ```
    Salidas: bloque B4 `0`; nueve archivos `preregistro`, ninguno de A2;
    pre-registro de fidelidad `0`; EV2 `35.6214`; r1
    `1.409 1.4415 2.4632 1.9746 7.2883 3.4161`; E5 `C2 6.658455`,
    `C3 6.218223`, `C4 6.135934`, `C5 2.245114`, total `21.257726`.

## Aparte: decisiones de diseño de evaluación que no están en H1 a H13

No es exhaustivo. Estado entre paréntesis.
- Principio 7, EV2 es examen: una evaluación por sistema, con pre-registro (`:264-267`) (a).
- Principio 10, desarrollo contra test (`:283-295`), y disjunción del conjunto
  final con desarrollo y con los diez de ESQ
  (`data/experiment/esq/documentos_excluidos_esq.json`, `:750` (a)) (a).
- Juez de fidelidad de EV2 (P-5, `:1257`) (a):
  - `claude-sonnet-4-6`, temperatura 0, N=3 con voto modal, ciego al grafo;
  - mapping fijo §2 (`data/experiment/ev2_juez/mapping.py:40-54`);
  - prompt `fd446f8e…`;
  - tres validaciones.
- Encadenamiento §7: re-corridas N=3 de las parciales y agregación sellada
  (`data/experiment/ev2_encadenamiento/code/agregacion_enc.py`, `9044a04`) (a).
- Adjudicación ciega con muestra de control simétrica, protocolo de C1
  (`data/experiment/ev2_r1/code/worksheet_r1.py:6-19`; nota de episodios de C1) (a).
- Atribución causal A0.2, cuatro clases (`regla_atribucion.md:152-159`; P-4
  `:1256`) (a).
- Indicadores de cita, B6.3 (e) (`:750`; `reports/ucita2_indicadores.md`) (a).
- Tipos de pregunta, regla v2 (`41abf18`) y cuotas de varios puntos y
  abstención en el conjunto final (`:751-753`): cuotas `[DECIDE LA AUTORA]` (c).
- Tamaño del conjunto final por potencia y análisis pareado (`:750`, asentado el 29/09) (a); cálculo (c).
- Mismo analizador y modo en las búsquedas léxicas de los dos brazos, o
  diferencia declarada (`:331`, `:750`) (a).
- Control del tope de llamadas por turno (`:825`; cifras en la decisión 3 del
  mandato, no rehechas) (a).
- Wilson para toda proporción y precisión por etapa del pipeline, B4.1
  (`:396-402`) (a).
- Observación (12), 30 aristas leídas contra el texto (enmienda `8e13be3`;
  25 de 30, `reports/tanda0/obs12_lectura/fila_obs12.md`) (a).
- Protocolo de lectura de la matriz congelada (`:727`) (a); la enmienda `[DECIDE LA AUTORA]`.
- Regla de admisibilidad de la comparación: confirmatoria solo si está en el
  pre-registro (D-h2, `:981`) (a).
- Registro de modelos por medición y por etapa (`:832`) (a); `docs/registro_modelos.md` NO ENCONTRADO (c).
- Intrínsecas informativas en el gate hasta el laudo B3.1 (`:378`); regression
  suite y shapes como gate, nunca EV2 (a).

## Propuestas de filas nuevas (el plan no se edita)

- **F-1** Declarar el instrumento de B6.3 (b) (harness con la configuración de
  A1.8, o banco con MCP) y cómo se reporta al lado de (f) bajo el principio 8
  (Q1, C-4). `[DECIDE LA AUTORA]`
- **F-2** Resolver el conjunto de preguntas de A2 frente a la regla de A1.8
  (C-2). `[DECIDE LA AUTORA]`
- **F-3** Confirmación humana, con información o enlaces, de la etiqueta de
  dificultad de B4.1 (f), y la vía a un experto (H10). `[DECIDE LA AUTORA]`
- **F-4** Alinear la numeración de capítulos del plan con la estructura del
  29/09 (C-1).
- **F-5** Corregir la cifra de calibración del juez de la Fase 2.3 en P-5 y en
  el mapa de fuentes (C-3).
- **F-6** Adjudicación de C2 a C5 con marcas de la autora, o declaración del
  marcador de modelo como desvío del protocolo y del anexo E5.c (C-6). `[DECIDE LA AUTORA]`
- **F-7** Definir quién adjudica la muestra de tripletas de B4 (la autora, un
  experto del dominio o los dos, y con qué rol cada uno), qué lugar tiene el
  experto del dominio (anotador de una submuestra, en modo literal o
  conversacional, según el registro del 04/09, §3) y cómo se declara el cambio
  respecto del gold standard de tripletas anotado manualmente de la propuesta
  (C-8; se relaciona con F-3). `[DECIDE LA AUTORA]`
- **F-8** Declarar dónde y cómo se reporta el costo de cada corrida de fidelidad
  y de comparación: unidad (por pregunta o por corrida), desglose (agente y
  juez, base y §7), fuente del cálculo (dbs de caché, `trace.cost_usd` o tokens
  con precios sellados) y lugar en el informe, para el desarrollo y para B6.3
  (b) y (f); incluye qué hacer con la diferencia sobre `c_juez` en la fórmula
  de B6.3 (C-9).
  `[DECIDE LA AUTORA]`

## Comandos (regla i)

```bash
# EV2: 40 preguntas y 164 criterios
python3 -c "import json;d=json.load(open('data/experiment/exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json'));P=d['preguntas'];print(len(P),sum(len(p['gold']['criterios']) for p in P))"
# C1 definitiva 6/26/8
git show 774acac:data/experiment/ev2_r1/cierre/cierre_r1.json | grep -A4 '"tabla_definitiva_r1"' | head -5
# Q6: filas, celdas con H, acuerdos y símbolos
grep -c '^| CQ-\|^| dev_unans' data/experiment/evaluacion/02_calibracion_juez.md
awk '/^\|/{n=gsub(/H:/,"&");ok=gsub(/✅/,"&");b=gsub(/❌/,"&");if(n>0){t+=n;o+=ok;x+=b}}END{print t,o,x}' data/experiment/evaluacion/02_calibracion_juez.md
grep -o '✅' data/experiment/evaluacion/02_calibracion_juez.md | wc -l; grep -o '❌' data/experiment/evaluacion/02_calibracion_juez.md | wc -l
# Harness y banco
grep -n 'MAX_TOOL_CALLS = \|^MODEL' data/experiment/evaluacion/harness.py
grep -n '"modelo"\|max_turns\|tope_tool_calls_en_prompt' data/experiment/banco_mcp/agentes/config_agentes.json
# «mismas 40 preguntas» en el plan (3 apariciones: :331, :345, :1254)
grep -c 'mismas 40 preguntas' docs/plan_tesis.md
# Observación (12) y matriz
python3 -c "import csv,collections;r=list(csv.DictReader(open('reports/tanda0/obs12_lectura/veredictos_obs12.csv',encoding='utf-8')));print(collections.Counter(x['veredicto'] for x in r))"
```

Cifras no recomputadas en esta unidad:
- **Dadas por el mandato (decisión 3), no se rehacen:** 80 de 456 con máximo 18;
  99 de 430 con máximo 17; 30 a adjudicación = 21 (2/18/1) + 9 (1/5/3).
- **Topes de herramientas de la tanda 0 (23, 27, 17 y 11; 28 en C1)** (`:323`):
  NO VERIFICADO en esta unidad, porque el mandato excluye `data/experiment/ev2_tanda0/`.
- **Tablas definitivas de E5.c:** NO VERIFICADO en esta unidad, y deben
  recomputarse por `8e0597c`.
- **Cifras del bake-off de embeddings:** tomadas del laudo, NO VERIFICADO en esta unidad.
