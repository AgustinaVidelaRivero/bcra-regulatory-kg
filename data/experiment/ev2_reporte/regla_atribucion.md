# Regla de atribución determinística de fallas — EV2 (U-A0 / A0.2, Fase A)

Estado: **PROPUESTA A LAUDO** — nada de lo que sigue se computó sobre datos
reales. Este documento fija las definiciones operativas con las que la Fase B
atribuirá cada falla de EV2 a una de cuatro clases; el módulo que las
implementa (`code/atribucion_fallas.py`) se niega a correr sobre datos reales
mientras este archivo no tenga un commit (`regla_sellada()`), de modo que el
laudo queda sellado antes de la primera atribución. Cualquier cambio posterior
es enmienda de este documento, nunca ajuste silencioso del código.

Costo USD 0: la atribución es replay determinístico sobre trazas persistidas
y grafos verificados por sha256; ninguna llamada a API.

Grafos (nomenclatura canónica, `docs/nomenclatura_grafos.md`): **KG-Base
(`12c226e2`)** = `run_3`, **KG-Refinado (`26fac8b4`)** = `v3`, **KG-Reextraído
(`8e2eadee`)** = `v2`. Las claves internas de los archivos EV2 siguen siendo
`run_3` / `v3` / `v2`.

---

## 1. Unidad de atribución y veredicto contra el que se atribuye

- **Unidad: la TRAZA** — una respuesta del agente sobre un grafo, con sus
  `steps` persistidos. No el par (pregunta, grafo) ni el veredicto definitivo.
- **Población principal (obligatoria): las 120 trazas de la corrida base**
  (`data/experiment/ev2_corrida/trazas/ev2_base_{run3,v3,v2}/EV2F-*.json`,
  commit `bb89a8e`), 40 por grafo.
- **Veredicto de referencia de cada traza base = el veredicto de ESA
  respuesta:**
  - el veredicto por pregunta del juez v1 sobre la respuesta base
    (`data/experiment/ev2_fidelidad_eval/out/veredictos_agregados_ciego.json`
    → `veredicto_pregunta`, cruzado por `desanonimizacion/tabla_id_opaco.json`,
    commit `b624865`);
  - si ese veredicto fue `requiere_adjudicacion` (21 casos), el veredicto
    definitivo por vía `adjudicacion_base`
    (`data/experiment/ev2_adjudicacion/adjudicacion/veredictos_definitivos_ciego.json`
    → `definitivo` con `via == "adjudicacion_base"`, commit `64de678`), que es
    la adjudicación humana de la MISMA respuesta base;
  - **NUNCA** el definitivo del par cuando ese vino de las re-corridas §7
    (vías `juez_enc` / `adjudicacion_s7`): esos veredictos juzgan otras
    respuestas (otras trazas), no la traza base.

  Verificación estructural ya hecha (sin abrir trazas ni atribuir; comando
  `.venv/bin/python -B data/experiment/ev2_reporte/code/atribucion_fallas.py --verificar-estructura`):
  base 120 = parcial 81 / incorrecto 28 / correcto 11 (fuente: juez_base 99 +
  adjudicacion_base 21); atribuibles (parcial + incorrecto) **109**; por grafo
  KG-Base 23/14/3, KG-Refinado 30/6/4, KG-Reextraído 28/8/4
  (parcial/incorrecto/correcto).

- **Los veredictos `correcto` NO se atribuyen**: la traza queda con
  `clase = null` y se reporta en el denominador (columna "correcto (no
  atribuible)" de toda tabla).
- **Población secundaria (OPCIONAL, tabla separada, declarada acá):** las 198
  re-corridas §7 (`data/experiment/ev2_encadenamiento/trazas/ev2_enc_*_r{1,2,3}/`,
  commit `9044a04`), cada una contra SU PROPIO veredicto: el del juez v1
  sobre esa re-corrida (`juez_out/veredictos_agregados_ciego.json`), o la
  adjudicación humana de esa re-corrida cuando la hubo (vía
  `adjudicacion_s7`, `resoluciones[rep].veredicto_humano`). Los votos
  `requiere_adjudicacion` que quedaron sin ficha porque el par se decidió por
  invariancia (**7**, verificación estructural: `sin_veredicto_propio`) no
  tienen veredicto propio y quedan FUERA, contados. Se corre solo con
  `--incluir-enc`; propongo incluirla en la Fase B (es determinística y
  gratuita) pero es decisión del laudo. Sus resultados nunca se suman a la
  tabla base: son una tabla aparte con su propio denominador (191 = 198 − 7).

## 2. Ancla presente: primaria, regla sellada del censo

- **Ancla de la traza = SOLO el ancla primaria de la pregunta**
  (`gold.ancla` de `data/experiment/exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json`,
  commit `9c44516`; las 40 preguntas tienen exactamente 1 ancla, formato
  `to:punto`, p. ej. `ext:6.11`). **NO se usan anclas secundarias derivadas de
  las citas de los criterios**: el gold sellado no porta un punto por criterio
  (cada criterio tiene solo `criterio` + `cita_textual`) y, por diseño, cada
  cita "debe anclar a texto real del PDF en el punto declarado"
  (`docs/diseno_ev2.md` §5), es decir, las citas viven en el punto del ancla
  primaria. Declaración explícita: la ancla secundaria "pre-declarada" que
  menciona el mandato no existe como dato en el set sellado; derivarla ahora
  sería construir gold post-hoc. Si el laudo la quisiera, requeriría un
  archivo nuevo sellado por commit antes de la Fase B (enmienda de esta regla).
- **Resolución del ancla en cada grafo = la regla sellada del censo**:
  `resolucion.AnclaIndex.resolver(to, punto)` (`data/experiment/exploracion/sinteticas/resolucion.py`,
  sha256 `afe66ee9…`): match EXACTO de punto normalizado (`'2.7' != '2.7.1'`),
  sin descendientes, y **excluyendo contenedores** (nodos que portan más de
  `CONTENEDOR_MAX_ANCLAS = 10` anclas distintas, línea 37). El índice se
  construye sobre la vista de censo de cada grafo
  (`comun_ev2.indice_anclas(grafo)`, `data/experiment/ev2_corrida/code/comun_ev2.py`
  sha256 `a397e94d…`: provenances completas, adaptadores de shape v2/run_3
  documentados en su docstring — los mismos que usó el censo de 5b02d22).
- **`ancla_presente`** = el ancla resuelve a ≥ 1 nodo en ese grafo. La lista
  de nodos resueltos son los **nodos-ancla** de la traza. (Con una sola ancla
  por pregunta la regla multi-ancla es teórica; queda definida por
  completitud: presente si ALGUNA ancla resuelve; vista/consultada si ALGUNA
  ancla lo está — misma agregación por ancla que `metrica.evaluar_por_anclas`.)
- El censo de anclas de fidelidad por grafo (40 anclas × 3 grafos → n nodos)
  se computa y persiste en la Fase B (`censo_anclas_fidelidad` de la salida);
  no existe en el repo, porque el censo de 5b02d22 cubrió solo el eje
  sintético (`ev2_corrida/code/censo_ev2.py`).

## 3. "Vista" y "consultada": campos exactos de traza y re-ejecución

Las trazas persisten `trace.steps[*]` con `n`, `tool`, `input`,
`output_truncado` (1.200 chars, `harness.TRUNC_TOOL_OUTPUT`) y `output_chars`,
más `steps_full[*]` con `n`, `tool`, `input`, `output` íntegro. El agente
recibió el output ÍNTEGRO de cada tool (`harness.py` líneas 509–525:
`result_str` completo va al `tool_result`); lo truncado es solo el log. Por
eso "vista"/"consultada" se computan sobre la RE-EJECUCIÓN determinística de
cada step con `harness.GraphIndex` sobre el mismo `kg.json` (sha256 verificado
por `comun_ev2.verificar_grafos`), exactamente como la métrica de
navegabilidad de 5b02d22: se importa `metrica.evaluar_traza`
(`data/experiment/exploracion/sinteticas/metrica.py`, sha256 `059f411b…`,
sin editar) — la MISMA función, no una copia.

Definiciones exactas (líneas de `metrica.evaluar_traza`):

- **VISTA** — algún nodo-ancla aparece con su `id` en `resultados[*].id` del
  output re-ejecutado de un step con `tool == "buscar_nodos"` (líneas 88–92;
  input `{"consulta", "limite"}` con `limite` acotado a [1, 50] por el
  harness). Se registra `vista_en_step` = menor `n` en que ocurre.
- **CONSULTADA** — algún nodo-ancla (a) recibió `ver_nodo` sin error: el output
  re-ejecutado trae `id` (líneas 93–96; un `ver_nodo` con id inexistente
  devuelve `{"error": …}` sin `id` y NO cuenta), o (b) apareció como
  `vecino_id` en `salientes[*]` o `entrantes[*]` del output re-ejecutado de un
  `ver_vecinos` (líneas 97–102), dentro del cap de 40 por dirección del
  harness (`ver_vecinos(id, direccion, limite=40)`, ningún caller pasa
  `limite`). Se registran `consultada_en_step` (menor `n`) y
  `consultada_via` ∈ {`ver_nodo`, `ver_vecinos`}.
- **Bordes heredados de la métrica (declarados, no corregidos):** un
  `ver_vecinos` sobre el PROPIO nodo-ancla no lo hace "consultado" (su output
  trae solo `id`/`label` del nodo y sus vecinos, no su contenido; metrica.py
  solo cuenta `vecino_id`); un vecino listado SÍ cuenta como consultado aunque
  el agente solo haya visto `vecino_label` + provenances. Ambos bordes están
  cubiertos por el selftest y se mantienen para que la atribución sea
  conmensurable con la navegabilidad de 5b02d22.
- **Replay obligatorio:** (i) replay estándar de `metrica._check_replay`
  contra `output_truncado`/`output_chars` de cada step; (ii) replay FUERTE
  `metrica_ev2.verificar_steps_full` (`data/experiment/ev2_corrida/code/metrica_ev2.py`
  sha256 `5c629c00…`, línea 44) con igualdad exacta contra `steps_full[*].output`.
  Una divergencia marca `replay_ok = false` / `replay_fuerte_ok = false` en la
  traza y se reporta; la corrida completa se declara inválida si alguna traza
  diverge (en la corrida base de navegabilidad fue 336/336 sin divergencias;
  la Fase B lo verificará para las 120 de fidelidad).
- Los `raw_turns_agent` y `trace.messages` NO se usan: la atribución es
  puramente por tools (steps), como la métrica.

## 4. Las cuatro clases y su precedencia

Sobre una traza con veredicto ∈ {parcial, incorrecto}, exactamente UNA clase,
evaluando en este orden y deteniéndose en la primera que aplica:

| orden | clase | condición operativa |
|---|---|---|
| 1 | **ausencia_kg** | `ancla_presente == false` (el ancla no resuelve a ningún nodo en ese grafo bajo la regla del censo). Es la misma noción de "ausencia" del censo de 5b02d22 (protocolo `docs/protocolo_corrida_ev2.md` §2): al grafo le falta el contenido; nada que el agente haga cambia la clase. |
| 2 | **generacion** | `ancla_presente && ancla_consultada`: el agente tuvo el contenido del ancla (ver_nodo) o llegó a él por vecindad, y la respuesta igual salió parcial/incorrecta. |
| 3 | **vista_no_consultada** | `ancla_presente && !ancla_consultada && ancla_vista`: un nodo-ancla apareció en resultados de `buscar_nodos` y el agente no lo abrió ni lo alcanzó (la "brecha vista-sin-consultar" de la métrica; mecanismo de selección post-búsqueda). |
| 4 | **alcanzabilidad** | `ancla_presente && !ancla_vista && !ancla_consultada`: el ancla está en el grafo pero ningún nodo-ancla apareció jamás en un `buscar_nodos` ni fue alcanzado por navegación. |

Tabla de verdad completa (presente, vista, consultada → clase):
(F,·,·)→ausencia_kg; (V,F,F)→alcanzabilidad; (V,V,F)→vista_no_consultada;
(V,F,V)→generacion; (V,V,V)→generacion.

Nota sobre el orden del mandato ("ausencia_kg / alcanzabilidad /
vista_no_consultada / generacion"): es el embudo de lectura (¿está? → ¿se
vio? → ¿se consultó? → ¿se generó mal?). Operativamente lo implemento con
`consultada` evaluada ANTES que `vista`, porque el único caso en que difieren
— consultada por `ver_vecinos` sin haber aparecido nunca en `buscar_nodos`
(V,F,V) — es un caso en que el agente SÍ tuvo el contenido, y llamarlo
"alcanzabilidad" sería falso. Con esa salvedad ambos órdenes coinciden.

## 5. Columna cruzada y cruces obligatorios

- **Clasificación auxiliar abstención/contenido** = `clasificacion_respuesta_modal`
  del juez sobre esa respuesta (`veredictos_agregados_ciego.json`, base o §7).
  Es COLUMNA CRUZADA de toda tabla; **no** es una quinta clase ni altera la
  precedencia. Se agrega además, como metadato, el flag `respondible` que el
  agente escribió en `trace.final_json.respondible` (no viaja al juez).
- **Criterios no cumplidos**: por traza, `n_no_cumplidos` = marcas
  `no_cumplido` de la MISMA fuente que el veredicto (modales del juez, o
  marcas humanas de la ficha si la respuesta fue adjudicada); cruce
  clase × grafo con suma, media por traza y tasa sobre criterios.
- Tablas de salida obligatorias: clase × grafo; clase × grafo × veredicto;
  clase × grafo × auxiliar; criterios no cumplidos × grafo × clase; perfil de
  clase por pregunta en los tres grafos (¿los empates 9-9 de incorrectos
  esconden perfiles de falla distintos?); tabla por traza (paquete).
- Salidas: `salida/atribucion_fallas.{json,md}` + `salida/atribucion_por_traza.md`;
  `censo_anclas_fidelidad` (40 × 3) dentro del JSON. Determinismo probado por
  corrida repetida byte-idéntica (salvo `generado`).

## 6. Selftest sintético (Fase A, hecho: 24/24 PASS)

`.venv/bin/python -B data/experiment/ev2_reporte/code/atribucion_fallas.py --selftest`
→ `selftest_out/selftest_atribucion.json` (gitignorado). Mini-grafo de 5
nodos con provenances PDF parseables (incluye un contenedor con 11 anclas) y
trazas construidas EJECUTANDO las tools (así el replay pasa). Casos:

- las 4 clases (ausencia_kg ×2 — ancla inexistente y ancla portada solo por
  contenedor —, alcanzabilidad, vista_no_consultada, generacion vía `ver_nodo`
  y vía `ver_vecinos`);
- bordes: `ver_nodo` con id inexistente no consulta; `ver_vecinos` sobre el
  propio nodo-ancla no consulta (con y sin vista previa); `ver_vecinos` en la
  dirección opuesta no alcanza; `limite` de `buscar_nodos` que deja el ancla
  fuera del top-k → no vista, y con top-k+1 → vista;
- correcto → `clase = null`; veredicto no atribuible → error;
- multi-ancla (una ausente + una consultada → generacion);
- replay: traza manipulada → divergencia detectada en estándar y fuerte;
- determinismo: dos corridas idénticas byte a byte;
- tabla de verdad completa de la precedencia.

## 7. Qué NO decide esta regla

No re-abre veredictos, no toca el juez ni el mapping, no edita nada bajo
`ev2_corrida/` (el replay se IMPORTA: `replay_navegabilidad_ev2.py` es el
driver del eje sintético y filtra las EV2F-* por nombre; acá se aplica su
misma métrica a las EV2F-* desde un módulo nuevo). No promedia grafos entre sí.
No propone causas finas dentro de `generacion` (eso es del verificador causal
del proyecto, con laudo humano — `docs/tablero.md` §5, piloto U6): la clase
`generacion` es "el contenido estuvo a la vista del agente"; el sub-diagnóstico
queda fuera de esta unidad.
