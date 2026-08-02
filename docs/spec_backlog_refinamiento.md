# Spec — Backlog unificado de refinamiento del grafo

**Estado:** especificación (diseño aprobado; población inicial planificada, no ejecutada).
**Almacenamiento:** `data/backlog/backlog.jsonl` (no existe todavía — se crea al poblar).
**Escrituras de esta spec:** solo este archivo.

---

## 1. Propósito

Un solo backlog de refinamiento del grafo. Hoy los defectos detectados viven dispersos:
en fichas de fallas del escalón 1, en filas de triage de la extracción, en notas
"backlog" dentro de varas de adjudicación, y pronto en el feedback de la app. Cada
fuente tiene su propio formato y su propio nivel de confianza, y la etapa cara del
ciclo — corregir el grafo y demostrar la corrección — no tiene una cola única de la
cual tirar.

El backlog resuelve eso con entradas tipadas que portan cuatro cosas:

1. **Fuente** — de qué circuito salió el defecto.
2. **Diagnóstico con jerarquía de confianza** — no toda detección vale lo mismo: una
   adjudicación humana no es un veredicto exploratorio de un verificador sin calibrar.
3. **Evidencia con punteros** — cada entrada rastrea a su ficha, fila de triage o
   traza; nada entra "porque me acuerdo".
4. **Verificación obligatoria** — ninguna entrada se declara aplicada sin definir
   antes qué pregunta o chunk re-testea el arreglo.

El objetivo operativo: que la etapa cara (corregir) se gaste primero en lo mejor
diagnosticado. La priorización fina es humana (ver §7), pero el contrato garantiza que
la información para priorizar esté siempre presente y comparable entre fuentes.

---

## 2. Contrato de datos

Cada entrada es un objeto JSON (una línea del jsonl). Esquema:

```json
{
  "id": "BKL-0001",
  "fuente": "vara | escalon1_fallas | triage_extraccion | verificador | app_feedback | auditoria_ensamblado",
  "diagnostico": "adjudicado_humano | verificador_validado | verificador_exploratorio | sin_diagnostico",
  "especie": "amputacion | provenance_desplazada | fabricacion | quimera | descenso_sujeto | ausencia | alcanzabilidad | estrechamiento_sujeto | sujeto_termino_ajeno | clase_forzada | contenido_sin_subespecie | duplicacion | hub_contaminado | cascara",
  "grafo": "grafo_v2",
  "nodos_objetivo": ["Restriccion_..."],
  "evidencia": ["data/experiment/.../fichas_fallas_v2.json#EV1-031"],
  "propuesta": "texto libre: el cambio candidato, si ya hay uno",
  "verificacion": "EV1-031 (re-corrida N=3) | chunk TO_capitales_minimos_actual.pdf::2.8__pN",
  "estado": "nuevo | triaged | aplicado | verificado | descartado",
  "aplicado_en": null
}
```

Descripción por campo:

- **`id`** — identificador estable de la entrada (`BKL-NNNN`, correlativo). Los eventos
  posteriores de cambio de estado lo referencian (ver §5); nunca se reutiliza.
- **`fuente`** — el circuito de detección:
  - `vara`: adjudicaciones de vara sellada (p. ej. los ítems "backlog" de
    `docs/casos_gate_cqn2.md` — gemelos duplicados, provenance desplazada, hub
    contaminado).
  - `escalon1_fallas`: las fallas adjudicadas de la medición del escalón 1
    (`data/experiment/evaluacion_escalon1/`).
  - `triage_extraccion`: filas VP del triage de aristas sospechosas de la extracción
    (`data/experiment/grafo_v2/triage_sospechosas_U5.json`).
  - `verificador`: salidas del verificador automático ({síntoma, causa}). Legitimados
    por U5 como fuente de entrada al backlog (`docs/lectura_gate_u5.md`).
  - `app_feedback`: el circuito de la app de chat (§3.b).
  - `auditoria_ensamblado`: hallazgos de auditorías de pipeline y re-ensamblados
    (p. ej. los defectos detectados por el mapeo del delta v2→v3 y el re-triage
    contra el grafo promovido). Enmienda 2026-07-31.
- **`diagnostico`** — la jerarquía de confianza, de mayor a menor:
  - `adjudicado_humano`: un humano miró la evidencia y laudó. Techo de confianza.
  - `verificador_validado`: veredicto automático de un verificador **calibrado contra
    vara humana sobre el mismo esquema de grafo que está juzgando**. Legitimado para
    BKL-0023 por gate U5 sobre familia v2/v3 (`docs/lectura_gate_u5.md`).
  - `verificador_exploratorio`: veredicto automático fuera de su dominio de
    calibración.
  - `sin_diagnostico`: síntoma registrado sin causa atribuida (p. ej. un 👎 de la app
    que aún no pasó por el circuito de intake).

  **Regla de frontera del verificador:** el verificador es `validado` solo sobre el
  esquema en que fue calibrado — hoy, run_3 (calibración de la Fase 2.5 y varas de los
  gates CQN/CQN2). Sobre `grafo_v2` y esquemas sucesores, todo veredicto suyo entra
  como `verificador_exploratorio` hasta que exista una re-calibración con vara propia
  de ese esquema (pre-requisito registrado en §7).
- **`especie`** — el tipo de defecto, tomado del bestiario de extracción de
  `docs/casos_gate_cqn2.md` §(a).1 más dos especies medidas después:
  - `amputacion` — cláusulas hermanas o antecedentes cortados de un nodo existente
    (ej.: CQN2-005, CQN2-014; EV1-005).
  - `provenance_desplazada` — contenido fiel con ubicación de otro punto (ej.:
    CQN2-002 paso 9).
  - `fabricacion` — texto inventado por el extractor, 0 hits en corpus (ej.: CQN2-011,
    "sujetas a arancel").
  - `quimera` — label de un punto con description de otro, o nodos con contenido
    cruzado (ej.: CQN2-013; EV1-039).
  - `descenso_sujeto` — sujeto asignado más específico que el que el texto licencia
    (ej.: `banco_comercial` donde el texto dice "entidades" — grupo VP-A del triage).
  - `ausencia` — el dato no existe en ningún nodo del grafo (ej.: EV1-031, el límite
    de 75 SMVM).
  - `alcanzabilidad` — el dato existe en el grafo pero no rankea o no se alcanza
    léxicamente (capa índice/alcance, H1; ej.: EV1-015, EV1-018 del deslinde).
  - `estrechamiento_sujeto` — un colectivo asignado a una clase más estrecha que
    omite miembros (ej.: grupo B del triage U5 — solo EF donde "la(s) entidad(es)"
    de Exterior = EF∪EC).
  - `sujeto_termino_ajeno` — vocabulario de otro TO trasplantado como clase (ej.:
    grupo VP-B del triage U5 — `usuario_de_servicios_financieros` de Protección en
    Exterior 13.4).
  - `clase_forzada` — término fuera de catálogo forzado a una clase cercana en lugar
    de `sujeto_propuesto` (ej.: grupo C VP-menor del triage U5 — VPU→`exportador`).
  - `contenido_sin_subespecie` — especie provisional que emite el intake automático
    cuando el verificador atribuye `contenido_kg` — el instrumento no distingue
    sub-especies (límite documentado en `docs/lectura_ciclo2.md`, §3(iv) "sub-especie
    de defecto KG mal nombrada" y §6 "la frontera fina de sub-especies del lado KG");
    el triage humano la refina a una especie definitiva.
  - `duplicacion` — nodos gemelos con description idéntica bajo ids distintos
    (mecanismo: id = tipo_slug; ej.: los gemelos de CQN2-005 y CQN2-014,
    `docs/casos_gate_cqn2.md` §(a).3).
  - `hub_contaminado` — entidad-clase que atrae relaciones de múltiples TOs (ej.:
    `EntidadFinanciera_sujeto_obligado`, 991 entrantes de los cinco documentos,
    `docs/casos_gate_cqn2.md` §(a).4).
  - `cascara` — nodo sin description con provenance correcta (ej.: CQN2-006,
    `Operacion_calculo_mensual_de_exigencia_operacional`).

  El catálogo sigue siendo cerrado a propósito (agregación entre fuentes): ampliarlo
  es una decisión registrada en esta spec, nunca improvisación del intake.
- **`grafo`** — sobre qué grafo se detectó y se corregiría el defecto (`grafo_v2`,
  `run_3`, o el identificador del sucesor). Determina además qué vale como
  `verificador_validado` (regla de frontera).
- **`nodos_objetivo`** — ids de los nodos/aristas a tocar. Puede ser vacío cuando la
  especie es `ausencia` (no hay nodo: hay que crearlo) — en ese caso la evidencia
  porta el chunk fuente.
- **`evidencia`** — lista de punteros verificables, nunca prosa suelta. Formatos
  aceptados: ruta de ficha o informe (`archivo#ancla`), fila de triage
  (`triage_sospechosas_U5.json` + sujeto + chunk_id + norma), traza
  (`posthoc_run/traces/...`), o sesión de la app (`session_id` + número de `turno`,
  que identifican unívocamente una línea del jsonl de sesiones).
- **`propuesta`** — el cambio candidato, si ya existe (texto libre). Muchas entradas
  nacen sin propuesta; la formula la skill `kg-refinement` al consumirlas.
- **`verificacion`** — **obligatoria para pasar a `aplicado`**: la pregunta de eval
  (id de EV/CQ) o el chunk del PDF contra el que se re-testea el arreglo. Sin este
  campo definido, una corrección no puede declararse aplicada — es el candado que
  impide "arreglos" indefendibles.
- **`estado`** — máquina de estados:
  `nuevo → triaged → aplicado → verificado`, con `descartado` como salida terminal
  desde cualquier estado. `triaged` = un humano confirmó que la entrada es real y
  corregible (para fuentes con `adjudicado_humano` de origen, el intake puede crear
  la entrada directamente en `triaged`); `aplicado` = el cambio está en la copia de
  trabajo del grafo; `verificado` = la verificación declarada se corrió y pasó.
- **`aplicado_en`** — identificador de la copia/versión del grafo donde se aplicó el
  cambio (ej. la carpeta de la copia de trabajo + fecha). `null` hasta `aplicado`.

**Regla de exclusión:** las fallas de capa agente no generan entrada — destino:
frente de co-diseño; se registran como descartadas-con-motivo en el log de intake.
Ejemplo: EV1-029 (el 3.1.1.1 esquivo con varianza de réplica — comportamiento del
agente, no contenido ni estructura del grafo) no entra al backlog; su intervención
natural es el co-diseño agente-estructura, no una edición del grafo.

---

## 3. Flujo de intake por fuente

El corazón del diseño: cada fuente tiene su circuito, y el circuito determina el
`diagnostico` con que la entrada nace.

### (a) Vara / adjudicación humana → entrada directa

Las adjudicaciones de vara (p. ej. `docs/casos_gate_cqn2.md`) y las fallas adjudicadas
de mediciones selladas ya pasaron por el laudo humano: generan entrada directa con
`diagnostico: adjudicado_humano`, evidencia apuntando a la ficha/vara, y estado
inicial `triaged` (el triage humano ya ocurrió en la adjudicación).

### (b) App feedback → el circuito largo (skill `feedback-intake`, nueva)

El único flujo que arranca de señal cruda de usuarios. Pipeline:

1. **jsonl → traza.** Las sesiones viven en `app/sessions/<usuario>/<session_id>.jsonl`
   (formato en `app/README.md`, §"Dónde quedan las sesiones"): líneas `tipo: "turno"`
   (con `pregunta`, `respuesta`, `tools_llamadas` con resultados completos sin
   truncar, `run_id`, `backend`, `modelo`) y líneas `tipo: "feedback"` (`voto`
   up/down, `comentario`, referenciando `session_id` + `turno`). Cada 👎 se convierte
   a una traza en el formato del harness — las tools están íntegras en la línea de
   turno, así que la conversión es determinística, sin re-correr nada.
2. **Juez congelado.** La traza pasa por el juez de la evaluación
   (`data/experiment/evaluacion/judge.py`, v2.1.1 dos pasos): ¿la respuesta era
   efectivamente mala? Un 👎 puede ser insatisfacción sin defecto (pregunta fuera de
   corpus, expectativa errada).
   **Salvedad documentada del escalón 1:** los veredictos del juez emitidos bajo sus
   propios flags **no son confiables** — el muestreo humano del escalón 1 movió 4
   mayorías, incluyendo evasivas aprobadas por el juez bajo flag
   (`lectura_P1P5_escalon1.md`, §"Hallazgo no previsto — el juez bajo flag no es
   confiable"; registro en `acta_adjudicacion_EV1.md` y `muestreo_flags.json`). Regla
   heredada acá: **todo veredicto con flags va a muestreo humano antes de generar
   entrada**; solo los veredictos limpios siguen automáticos.
3. **Verificador.** Sobre las respuestas confirmadas como malas, el verificador emite
   {síntoma, causa}. El `diagnostico` resultante se etiqueta según el grafo de la
   sesión (regla de frontera de §2): sobre run_3 → `verificador_validado`; sobre
   grafo_v2 o sucesores → `verificador_exploratorio`.

   **Mapeo causa→especie** (cómo el intake automático traduce la causa del
   verificador al campo `especie` de la entrada):

   | Causa del verificador | Especie de la entrada |
   |---|---|
   | `completitud_kg` | `ausencia` |
   | `alcanzabilidad_kg` | `alcanzabilidad` |
   | `estructural` | `hub_contaminado` |
   | `contenido_kg` | `contenido_sin_subespecie` |
   | `provenance_imprecisa` | `provenance_desplazada` (especie ya existente del bestiario) |
   | `aplicacion_erronea` | sin entrada — descartada-con-motivo en el log de intake (defecto del agente, regla de exclusión de §2) |
   | `frontera_no_determinada` | sin entrada automática — deriva a triage humano, registrada en el log de intake |

4. **Entrada.** Se escribe con `fuente: app_feedback`, evidencia = `session_id` +
   `turno` (+ el veredicto del juez y la salida del verificador), estado `nuevo`.

**Los 👍 no generan entrada.** Se conservan como denominador: permiten calcular tasas
de defecto por territorio (¿qué fracción del uso de la sección X termina en 👎?), que
informan la priorización humana. Descartarlos sesgaría toda tasa hacia arriba.

**Pendiente de decisión (modo sin-gold):** las sesiones de la app no portan respuesta
esperada; hasta que se laude el modo sin-gold, el Paso-juez de `feedback-intake` frena
por válvula en preguntas libres — la resolución candidata (laudo humano obligatorio
como síntoma + verificador como diagnóstico) queda registrada acá, no implementada.

### (c) Triage de extracción → entrada directa

Las filas con veredicto VP del triage de la extracción (hoy:
`data/experiment/grafo_v2/triage_sospechosas_U5.json`, adjudicado a mano el
2026-07-26) generan entradas con `diagnostico: adjudicado_humano` y evidencia
apuntando a la fila (sujeto + chunk_id + norma). Las FP no generan nada — son
calibración del detector, no defectos del grafo.

---

## 4. Frontera de skills

| Responsabilidad | `kg-refinement` (existente) | `feedback-intake` (nueva) |
|---|---|---|
| jsonl crudo de la app → traza formato harness | — | ✔ |
| Pasar la traza por el juez congelado | — | ✔ |
| Muestreo humano de veredictos flaggeados | — | ✔ (lo orquesta: prepara el lote y frena) |
| Correr el verificador sobre el síntoma confirmado | — | ✔ |
| Escribir la entrada diagnosticada al backlog | — | ✔ |
| Consumir entradas `triaged` | ✔ | — |
| Proponer el cambio (palanca, riesgo) | ✔ | — |
| Aplicar sobre la copia de trabajo | ✔ | — |
| Verificar (re-corrida de la pregunta/chunk declarado) | ✔ | — |
| Registrar eventos de estado (`aplicado`, `verificado`) | ✔ | — |

- `kg-refinement` (`.claude/skills/kg-refinement/SKILL.md`) gobierna
  proponer/aplicar/verificar: sus Pasos 4 y 5 (palancas, enrutamiento por riesgo,
  candado anti-entrenar-contra-el-test, side-by-side contra baseline) quedan intactos;
  lo que cambia es el **origen** del trabajo — entradas `triaged` del backlog en lugar
  de (solo) fallas recién atribuidas en su Paso 3. Ver choque C2 en §7.
- **Cambio requerido en `.claude/skills/kg-refinement/SKILL.md` (tarea posterior, no
  cubierta por esta spec):** declarar el punto de entrada = entradas `triaged` del
  backlog, y una vía para entradas con `diagnostico: adjudicado_humano` que **no
  re-atribuya desde cero** — el Paso 3 se salta (el laudo humano ya es la atribución)
  o se reduce a verificación puntual de la evidencia.
- `feedback-intake` gobierna el flujo (b) completo: de jsonl crudo a entrada
  diagnosticada. No propone ni aplica cambios, nunca toca el grafo.
- **Cero código compartido salvo el contrato de datos** (§2). Las dos skills se
  acoplan únicamente por el esquema de la entrada; ninguna importa código de la otra.
  Esto permite evolucionar el circuito de intake (juez, verificador, muestreo) sin
  tocar el pipeline de corrección, y viceversa.

---

## 5. Almacenamiento

`data/backlog/backlog.jsonl` — **tracked en git, append-only**.

- **Append-only:** los cambios de estado son eventos nuevos que referencian el `id`
  (p. ej. `{"evento": "cambio_estado", "id": "BKL-0001", "estado": "aplicado",
  "aplicado_en": "...", "ts": "..."}`), nunca ediciones de líneas ya escritas. Es el
  mismo patrón que el registro de sesiones de la app (`app/README.md`: "una línea JSON
  por turno y una por feedback, nunca se edita una línea ya escrita"). El estado
  vigente de una entrada se reconstruye plegando sus eventos en orden.
- **Evento `retriage_<grafo>` (enmienda 2026-07-31):** cuando el grafo vigente
  cambia (p. ej. una promoción), el re-triage de las entradas existentes se
  registra con eventos `{"evento": "retriage_<grafo>", "id": "BKL-NNNN",
  "estado_retriage": "...", "grafo": "...", "nota": "...", "evidencia": "...",
  "adjudicacion": "...", "ts": "..."}`. Enum de `estado_retriage`:
  `resuelta_por_<grafo>` · `vigente_sin_cambios` · `modificada_por_<grafo>`
  (para el re-triage del 31-07: `resuelta_por_v3` / `vigente_sin_cambios` /
  `modificada_por_v3`). Este evento **no altera la máquina de estados
  principal** (`nuevo → triaged → aplicado → verificado` / `descartado`): es un
  anexo de contexto por grafo; una entrada `resuelta_por_<grafo>` sigue en su
  estado formal hasta que su verificación declarada se corra y la lleve a
  `verificado` (o la adjudicadora la cierre).
- **Política de aplicación (laudada, 2026-07-31):** las correcciones se aplican
  **in-place sobre el grafo vigente** (hoy
  `data/experiment/grafo_v2/reensamblado_v3/kg.json`), **un commit por
  corrección aplicada**. Convención de SHA: **el SHA de una aplicación es el
  commit que introduce su evento de aplicación en este jsonl** — auto-resoluble
  por `git log --follow data/backlog/backlog.jsonl`, sin campo circular dentro
  del evento.
- **Por qué tracked** (a diferencia de las sesiones de la app, que están fuera de
  git): el backlog **dirige ediciones del grafo**. Cada cambio que la fase de
  refinamiento aplique debe rastrear a una entrada, y esa cadena
  (defecto → diagnóstico → propuesta → aplicación → verificación) es trazabilidad de
  primera clase de la tesis: tiene que viajar con el repo, poder citarse por commit y
  sobrevivir a cualquier máquina. Las sesiones crudas, en cambio, son datos de
  usuarios (quedan fuera de git; al backlog solo llegan los punteros
  `session_id`+turno).
- Los commits del archivo los hace la autora, como todo en el repo (NO commits
  automáticos).

---

## 6. Población inicial (plan — no ejecutado)

Dos fuentes con adjudicación humana ya completa. Números leídos de los archivos
reales, no estimados.

### 6.1 Las 9 fallas adjudicadas del escalón 1

Fuente: `data/experiment/evaluacion_escalon1/corridas/fichas_fallas_v2.json`
(`n_fallas: 9`), deslinde causal en
`data/experiment/grafo_v2/informes/deslinde_fallas_v2_2026-07-27.md`, lectura en
`data/experiment/evaluacion_escalon1/lectura_P1P5_escalon1.md`, laudos en
`data/experiment/evaluacion_escalon1/adjudicacion_humana_2026-07-26.json`.

| Falla | Capa (deslinde) | Especie | Genera entrada de grafo |
|---|---|---|---|
| EV1-031 | extracción/completitud — 75 SMVM (2.8.3.3) ausente | `ausencia` | ✔ |
| EV1-042 | extracción/completitud — ventana del 3.5.3 ausente | `ausencia` | ✔ |
| EV1-028 | extracción/completitud — salvedad mutuales/cooperativas (1.1.2.5) ausente | `ausencia` | ✔ |
| EV1-011 | extracción/completitud — enumeración de niveles del 6.5 ausente (asimétrica: run_3 la tiene parcial) | `ausencia` | ✔ |
| EV1-005 | extracción/completitud — calificadores del 7.1 RI amputados en nodo existente | `amputacion` | ✔ |
| EV1-039 | extracción/contenido — nodos con la tabla del 1.2 cruzada (sonda pre-registrada confirmada) | `quimera` | ✔ |
| EV1-015 | índice/alcance (H1) — el dato EXISTE, no rankea; provenance anclada en 10.4 | `alcanzabilidad` | ✔ |
| EV1-018 | índice/alcance (H1) — los 3 ítems del 4.1.4 EXISTEN; falla compartida con run_3 | `alcanzabilidad` | ✔ |
| EV1-029 | comportamiento del agente / varianza de réplica (el 3.1.1.1 esquivo); sin deslinde de existencia en el informe | — (capa agente) | ✗ — regla de exclusión de §2: al frente de co-diseño, descartada-con-motivo en el log de intake |

**Conteo:** 8 entradas (4 `ausencia`, 1 `amputacion`, 1 `quimera`, 2
`alcanzabilidad`), todas `fuente: escalon1_fallas`, `diagnostico: adjudicado_humano`,
`grafo: grafo_v2`, estado inicial `triaged`. EV1-029 no genera entrada (regla de
exclusión de §2).

Campo `verificacion` natural de las 8: la re-corrida de la propia pregunta EV1-NNN
(N=3, veredicto modal — regla anti-ruido del juez ya establecida en la fase).

### 6.2 Los VP del triage U5

Fuente: `data/experiment/grafo_v2/triage_sospechosas_U5.json` — 75 filas adjudicadas,
de las cuales **31 son VP** (10 `VP` + 21 `VP-menor`; las 38 `FP` y 6 `FP-defendible`
no generan entrada). Por grupo del triage:

| Grupo del triage | Filas VP | Especie | Entradas si se agrupa por corrección |
|---|---|---|---|
| VP-A descenso probable (`banco`/`banco_comercial` donde el texto dice "entidad") | 8 | `descenso_sujeto` | 3 (CapMin 2.5 ×2 aristas; Exterior 14.5__p1 ×4; RI 3.1__p0 ×2) |
| VP-B término de otro TO (`usuario_de_servicios_financieros` de Protección trasplantado a Exterior 13.4) | 2 | `sujeto_termino_ajeno` | 1 (×2 aristas) |
| B estrechamiento colectivo→EF ("la(s) entidad(es)" de Exterior = EF∪EC; asignar solo EF omite a las cambiarias; corrección candidata única: re-apuntar al rol) | 18 | `estrechamiento_sujeto` | 1 corrección sistemática (×18 aristas) |
| C clase forzada (VPU→`exportador` 14.1; "residentes"→`persona_humana` 3.17__p1; "clientes"→`exportador` 3.18__p0) | 3 | `clase_forzada` | 3 |

**Conteo:** 31 aristas defectuosas. Granularidad a decidir: 1 entrada = 1 arista da
**31 entradas**; 1 entrada = 1 corrección propuesta (con `nodos_objetivo` listando
todas sus aristas) da **8 entradas**. Recomiendo la segunda — la unidad de trabajo de
`kg-refinement` es la corrección, no la arista, y el estrechamiento B es
manifiestamente una sola corrección sistemática — dejando la evidencia por-arista
dentro de cada entrada. Todas nacen `fuente: triage_extraccion`,
`diagnostico: adjudicado_humano`, `grafo: grafo_v2`, estado `triaged`.

Campo `verificacion` natural: el chunk fuente de cada fila (`chunk_id` del triage) —
re-extraer o inspeccionar la arista corregida contra ese chunk; para las que tengan
pregunta de eval que las cubra, también la pregunta.

**Total de la población inicial: 8 entradas del escalón 1 + 8 del triage = 16
entradas** (más la alternativa 31-por-arista del triage si se descarta el
agrupamiento; EV1-029 descartada-con-motivo, fuera del backlog).

---

## 7. Fuera de alcance

1. **Priorización automática.** El backlog porta la información para priorizar
   (diagnóstico, especie, tasas por territorio vía los 👍); el orden de ataque lo
   decide un humano.
2. **UI.** Ni visor ni editor; el jsonl se consulta con herramientas estándar.
3. **Re-calibración del verificador para v2.** Registrada acá como **pre-requisito**
   para que la fuente `verificador` pueda emitir `diagnostico: verificador_validado`
   sobre grafo_v2 y sucesores: requiere una vara propia de ese esquema (adjudicación
   humana sellada sobre fallas de v2, análoga a las varas CQN/CQN2 sobre run_3) y la
   medición de acuerdo contra ella. Hasta entonces, todo veredicto del verificador
   sobre v2 entra como `verificador_exploratorio`.

---

## Choques detectados con lo existente (a decidir, no resueltos por esta spec)

- **C1 — RESUELTO.** La versión inicial de esta spec registraba casos adjudicados sin
  especie; la extensión del enum de §2 (`alcanzabilidad`, `estrechamiento_sujeto`,
  `sujeto_termino_ajeno`, `clase_forzada`, `contenido_sin_subespecie`, `duplicacion`,
  `hub_contaminado`, `cascara`) más la regla de exclusión de capa agente los cubren, y
  el destino `estructural→hub_contaminado` del mapeo de §3(b) quedó consistente con el
  enum. Se conserva la entrada solo para no renumerar C2–C5.
- **C2 — `kg-refinement` hoy no conoce el backlog.** Su SKILL.md define el origen del
  trabajo como el dataset del Paso 1 + la atribución del Paso 3; consumir entradas
  `triaged` es un cambio de contrato de la skill (nuevo modo de entrada) que hay que
  editar en la skill misma. Esta spec lo registra; no lo asume hecho. Ojo además con
  el Paso 3: cuando una entrada ya llega `adjudicado_humano`, la skill no debe
  re-atribuir desde cero — necesita una vía "diagnóstico ya laudado" que hoy no tiene.
- **C3 — Dos vocabularios de causa.** El verificador de `kg-refinement` emite causas
  de su taxonomía cerrada (`contenido_kg`, `completitud_kg`, `alcanzabilidad_kg`,
  etc.); el backlog clasifica por `especie` del bestiario. Hay que definir el mapeo
  causa→especie (o que la entrada porte ambos campos) antes de que `feedback-intake`
  escriba entradas con paso 3 automático — si no, la agregación entre fuentes se rompe.
- **C4 — El adaptador jsonl→traza no existe.** El juez congelado consume el formato
  de traza del harness; las líneas de sesión de la app portan todo lo necesario
  (tools íntegras, `app/README.md`) pero la conversión hay que construirla — es la
  primera pieza de `feedback-intake`. Nota menor: bajo backend Bedrock el costo
  registrado en la línea es nominal (README, "Limitaciones conocidas"), irrelevante
  para el juez pero a no reportar como costo real.
- **C5 — El grafo de la app vs el grafo del backlog.** La app recomienda
  `run_3_ppf_core`; el refinamiento activo es sobre grafo_v2. El campo `grafo` de la
  entrada resuelve la ambigüedad (cada sesión registra su `run_id`), pero al priorizar
  hay que recordar que el feedback sobre run_3 no siempre traduce a defectos de v2 —
  la falla compartida EV1-018 muestra que a veces sí.
