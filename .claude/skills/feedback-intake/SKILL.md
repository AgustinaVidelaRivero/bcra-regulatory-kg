---
name: feedback-intake
description: Circuito de intake del feedback de la app de chat al backlog unificado de refinamiento (spec docs/spec_backlog_refinamiento.md, §3.b) — convierte sesiones jsonl cosechadas del server en entradas diagnosticadas de data/backlog/backlog.jsonl, pasando cada 👎 por el adaptador jsonl→traza, el juez congelado (con muestreo humano obligatorio de veredictos flaggeados) y el verificador, con etiqueta de confianza según el grafo de la sesión. Usá esta skill SIEMPRE que el trabajo sea: procesar/triagear los jsonl de la app, convertir 👎 en entradas del backlog, "¿qué hago con el feedback de los tutores?", correr el circuito de intake, o poblar el backlog desde app_feedback. NO la uses para proponer o aplicar cambios al grafo (eso es kg-refinement) ni para las fuentes de entrada directa (vara, escalón 1, triage de extracción — esas no pasan por este circuito).
---

# feedback-intake — de jsonl crudo a entrada diagnosticada del backlog

**Estado: v1.0 — revisada y aprobada (2026-07-28).**

Implementa el flujo §3(b) de `docs/spec_backlog_refinamiento.md` (EL CONTRATO — ante
cualquier conflicto entre esta skill y la spec, manda la spec y el conflicto se
reporta). Esta skill gobierna el circuito completo de señal cruda a entrada
diagnosticada. **No propone ni aplica cambios; nunca toca ningún grafo.**

## Frontera (spec §4) — qué hace y qué no

Hace: jsonl→traza · juez congelado · orquestar el muestreo humano de flags · correr
el verificador sobre síntomas confirmados · escribir entradas al backlog.
NO hace: consumir entradas `triaged`, proponer cambios, aplicar sobre copias de
trabajo, verificar arreglos, registrar eventos `aplicado`/`verificado` (todo eso es
`kg-refinement`). Cero código compartido entre skills: el único acople es el esquema
de la entrada (spec §2).

## Invariantes (valen para todos los pasos)

- **El núcleo congelado no se edita.** `loader.py`, `harness.py`, `judge.py`,
  `llm_cache.py` y el cluster congelado se importan, jamás se modifican (regla del
  cuarteto: la caché hashea sus bytes). Todo lo nuevo — el adaptador incluido — es
  módulo aparte.
- **NO commits** — los hace la autora. Esto incluye `data/backlog/backlog.jsonl`
  (tracked): la skill lo escribe en el working tree y frena; el commit es de ella.
- **Backlog append-only** (spec §5): entradas y eventos como líneas nuevas; nunca se
  edita una línea escrita. Los `id` (`BKL-NNNN`) se continúan leyendo el último del
  archivo real, no de memoria.
- **Catálogos cerrados:** ni especies nuevas, ni filas nuevas del mapeo
  causa→especie, ni diagnósticos nuevos. Lo que no encaja → válvula (freno +
  reporte), jamás improvisación.
- **Evidencia por punteros** (spec §2): `session_id` + `turno` + punteros a los
  artefactos del intake. Nada entra "porque me acuerdo".
- **Números parseados, nunca estimados.** Y el costo de las líneas con
  `backend: bedrock` es **nominal** (precios de harness ≠ precios Bedrock): se puede
  registrar como está, prohibido reportarlo como costo real (choque C4).

## Cuándo se detiene la skill (válvulas — parar ES el comportamiento correcto)

1. **Juez con flags** → el lote va a muestreo humano y la skill FRENA (Paso 4). Sin
   excepciones: el hallazgo del escalón 1 es que el juez bajo sus propios flags
   aprueba evasivas (`lectura_P1P5_escalon1.md`, acta EV1, `muestreo_flags.json`).
2. **Causa del verificador sin fila en el mapeo** (hoy: `provenance_imprecisa`,
   `frontera_no_determinada`, o cualquier valor imprevisto) → freno + reporte a
   metodología. El mapeo es parte del contrato; ampliarlo es decisión de spec.
3. **El juez o el verificador exigen un insumo que la sesión no porta** (p. ej.
   ground truth / vara de una pregunta libre) → freno + reporte. **Prohibido adaptar
   el juez o el verificador** para que "funcione": son instrumentos congelados/
   calibrados; cualquier modo nuevo se decide en metodología.
4. **Línea de sesión malformada o incompleta** (turno sin tools, feedback huérfano
   sin turno correspondiente) → esa unidad se descarta-con-motivo en el log y se
   sigue con el resto; si el patrón es masivo (>10% del lote), freno total.

---

## PASO 0 — Cosecha e inventario

Insumo: los jsonl bajo `sessions_server/` (cosechados del server con el rsync del
runbook, `app/deploy/reporte_frente_hosting.md`) o `app/sessions/` locales. Formato:
`app/README.md`, §"Dónde quedan las sesiones" — líneas `tipo: "turno"` (con
`pregunta`, `respuesta`, `tools_llamadas` con resultados completos sin truncar,
`run_id`, `backend`, `modelo`, `usuario`, `ts`) y `tipo: "feedback"` (`voto` up/down,
`comentario`, referencia por `session_id`+`turno`).

**Qué hace:** parsea todo el lote y produce el inventario: sesiones, turnos, votos
por tipo, por `usuario` y por `run_id`. Cruza cada feedback con su línea de turno
(clave: `session_id`+`turno`).

**Fijo (y por qué):**
- **Los 👍 se cuentan y se conservan como denominador — jamás generan entrada**
  (spec §3.b). Registrá en el reporte del intake las tasas 👎/(👍+👎) por `run_id` y,
  si el volumen lo permite, por territorio (TO citado en la respuesta): esa tasa
  informa la priorización humana. Descartar los 👍 sesgaría toda tasa hacia arriba.
- **Los comentarios de los 👍 se preservan en el log del intake** (señal cualitativa),
  sin entrada.
- **Idempotencia:** antes de procesar un 👎, verificá contra el backlog y el log de
  intake que ese `session_id`+`turno` no fue procesado en una corrida anterior. El
  circuito se corre periódicamente (semanal/mensual); reprocesar duplicaría entradas.

## PASO 1 — Selección

Unidad de trabajo: **cada 👎** con su línea de turno correspondiente. Nada más entra
al circuito (los 👍 quedaron en el Paso 0; los turnos sin feedback no se juzgan).

## PASO 2 — Adaptador jsonl→traza (choque C4: no existe; es la primera pieza)

**Qué hace:** convierte la línea de turno al formato de traza que el juez congelado
consume. La conversión es **determinística y completa**: la línea porta pregunta,
respuesta estructurada (o `respuesta_cruda` si el parse falló), y las tools íntegras
con argumentos y resultados sin truncar — **no se re-corre nada** (spec §3.b.1: "sin
re-correr").

**Fijo (y por qué):**
- **Módulo nuevo que importa, jamás edita** — ubicación sugerida:
  `data/experiment/evaluacion/adapters/app_session_adapter.py` (fuera del cuarteto;
  la ubicación final la decide la autora). Antes de escribirlo, **leer con citas** la
  estructura real que `judge.py` consume (¿dict de traza? ¿campos obligatorios?
  ¿exige `ground_truth`/vara?) y la de la línea de turno — el mapeo campo a campo se
  documenta en el docstring del adaptador. Si `judge.py` exige un insumo que la
  sesión no porta → **válvula 3**.
- **Verificación del adaptador antes del primer uso a escala:** round-trip sobre una
  línea de turno conocida (p. ej. una sesión propia de la autora), mostrando la traza
  resultante y que ningún resultado de tool se truncó (longitudes comparadas contra
  la línea original).
- **`respuesta_cruda` (parse fallido del agente):** se adapta igual — el juez debe
  poder juzgar el texto crudo; si su formato lo impide, válvula 3, no maquillaje.

## PASO 3 — Juez congelado

**Qué hace:** pasa cada traza por `data/experiment/evaluacion/judge.py` (v2.1.1, dos
pasos), sin modificarlo, para responder UNA pregunta: **¿la respuesta era
efectivamente mala?** Un 👎 puede ser insatisfacción sin defecto (pregunta fuera de
corpus con abstención correcta, expectativa errada del usuario).

**Fijo (y por qué):**
- **El juez se corre tal cual está.** Su semántica es la de la evaluación formal; si
  no aplica a preguntas libres en algún modo, eso se reporta (válvula 3), no se
  parchea.
- **Salida clasificada en tres:** (a) **veredicto limpio: respuesta correcta** → el
  👎 se descarta-con-motivo ("insatisfacción sin defecto según juez") en el log, con
  el comentario del usuario preservado; (b) **veredicto limpio: respuesta mala** →
  sigue al Paso 5; (c) **veredicto CON flags** → Paso 4, sin excepción.

**Pendiente de decisión (modo sin-gold — espejo de la spec §3.b):** las sesiones de
la app no portan respuesta esperada; hasta que se laude el modo sin-gold, este paso
frena por válvula (válvula 3) en preguntas libres. La resolución candidata (laudo
humano obligatorio como síntoma + verificador como diagnóstico) queda registrada en
la spec, no implementada — no la implementes acá.

## PASO 4 — Muestreo humano de veredictos flaggeados (freno obligatorio)

**Regla heredada del escalón 1** (spec §3.b.2): todo veredicto emitido bajo flags va
a laudo humano antes de generar (o descartar) entrada — el muestreo del escalón 1
movió 4 mayorías, incluidas evasivas aprobadas por el juez bajo flag.

**Qué hace la skill:** prepara el **lote de muestreo** — por caso: la pregunta, la
respuesta, el veredicto del juez, sus flags, y el puntero `session_id`+`turno` — en
un archivo del log de intake, y **FRENA**. No hay heurística que permita seguir: ni
"el flag es menor", ni "la mayoría de N réplicas es clara". El laudo es de la autora;
al retomar, cada caso laudado sigue por (a) o (b) del Paso 3 según el laudo.

## PASO 5 — Verificador y mapeo a especie

**Qué hace:** sobre cada respuesta confirmada como mala (limpia o laudada), corre el
verificador para obtener {síntoma, causa}, y traduce la causa a `especie` con la
tabla del contrato — **cerrada**:

| Causa | Especie |
|---|---|
| `completitud_kg` | `ausencia` |
| `alcanzabilidad_kg` | `alcanzabilidad` |
| `estructural` | `hub_contaminado` |
| `contenido_kg` | `contenido_sin_subespecie` (provisional; el triage humano la refina) |
| `aplicacion_erronea` | **sin entrada** — descartada-con-motivo en el log (capa agente, regla de exclusión §2) |
| cualquier otra causa | **válvula 2** — freno + reporte (sin fila = sin entrada automática) |

**Fijo (y por qué):**
- **Etiqueta de diagnóstico por el grafo de la sesión** (choque C5, regla de frontera
  §2): `run_id` de la línea → campo `grafo` de la entrada; si el grafo es run_3 →
  `verificador_validado`; **cualquier otro** (grafo_v2, sucesores) →
  `verificador_exploratorio`. El verificador solo es `validado` en el esquema donde
  fue calibrado contra vara humana.
- **Parámetro N del verificador:** tiene dueño (la autora) — default del proyecto:
  N=3 con veredicto modal para todo lo que termine en una entrada (regla anti-ruido
  establecida en la fase); N=1 solo para exploración sin escritura.
- **Toda causa de capa agente** (`aplicacion_erronea` y equivalentes de la taxonomía
  vigente) → sin entrada, descartada-con-motivo; su destino es el frente de co-diseño
  (spec §2), no este backlog.

## PASO 6 — Escritura de entradas

**Qué hace:** por cada caso con especie, apenda a `data/backlog/backlog.jsonl` una
entrada del esquema §2, completa:

- `id`: siguiente `BKL-NNNN` (leído del archivo real; si el archivo no existe, esta
  corrida lo crea con la primera entrada).
- `fuente: "app_feedback"` · `diagnostico`: según Paso 5 · `especie`: según mapeo ·
  `grafo`: el `run_id` de la sesión · `estado: "nuevo"` · `aplicado_en: null`.
- `nodos_objetivo`: los ids citados por el verificador si los emite; vacío si la
  especie es `ausencia`.
- `evidencia`: `session_id` + `turno` (identifican unívocamente la línea del jsonl)
  + punteros a los artefactos de esta corrida del intake (veredicto del juez, salida
  del verificador, laudo del muestreo si lo hubo).
- `propuesta`: vacía (las formula `kg-refinement` al consumir) salvo que el
  comentario del usuario contenga una propuesta explícita — en ese caso se transcribe
  citándolo.
- `verificacion`: default natural — re-corrida de la misma pregunta (la de la sesión)
  N=3 veredicto modal; si el verificador ancló un chunk fuente, también el chunk.
  **Sin este campo la entrada no puede llegar nunca a `aplicado`** (candado §2).

**Log de intake** (misma corrida, ubicación sugerida `data/backlog/intake/` —
decisión de la autora): descartes-con-motivo (👎 sin defecto, capa agente, líneas
malformadas), lote de muestreo y laudos, conteos de 👍 y tasas por `run_id`.

## PASO 7 — Reporte de cierre y freno

Reporte de la corrida: procesados / entradas creadas (por especie y diagnóstico) /
descartes por motivo / pendientes de muestreo / tasas 👎 por grafo — todos los
números parseados de los archivos escritos. La skill **frena para revisión de la
autora**; los commits (backlog + log) son de ella.
