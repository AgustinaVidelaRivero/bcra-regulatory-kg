# Diseño de la caracterización de H-B2 (A2.1, tramo 1; escrito antes de correrla)

Mandato: `docs/mandatos/A2_1_sistema_por_fragmentos_preregistro_A2_2.md`, §3, punto 5 (texto firmado `b311859c…`, leído en
`c2b6cb60`). Las sesiones las lista `a2_1/diseno_HB2.json`; las corre `a2_1/correr_a2_1.py --fase hb2` en el tramo 2, con el
«seguí» de la autora (`a2_1/tramo2_paso2_hb2.zsh`). Las reglas de decisión de §4 están implementadas en
`correr_a2_1.evaluar_hb2` y se ejercitaron sobre casos sintéticos en la corrida en seco (`a2_1/corrida_en_seco_a2_1.py`).

## 1. Qué es H-B2

En la corrida 2 de la fase B del banco (CLI 2.1.241, `--max-turns 12`), la sesión SMK-04-kg terminó con `subtype` `success`
y `num_turns` 14: el corte no disparó (README del banco, «Fase B»). El criterio de corte R5 de A2.2 tiene que fijarse sobre
una señal verificada (Q1). La documentación no define `num_turns` y describe el límite de dos maneras:

- CLI, `--max-turns`: «Limit the number of agentic turns» (`agentes/config_agentes.json`, flag `--max-turns 12`);
- Agent SDK (TypeScript), `Options.maxTurns`: «Maximum agentic turns (tool-use round trips)»; `AgentDefinition.maxTurns`:
  «Maximum number of agentic turns (API round-trips)»; `SDKResultMessage` trae `num_turns` sin definirlo, y su `subtype`
  de error incluye `error_max_turns` (code.claude.com/docs/en/agent-sdk/typescript, leída el 16/10/2026).

## 2. Lo que ya está medido (antecedente)

`a2_1/antecedente_HB2_faseB.py` cuenta, sobre las 12 sesiones de la corrida 2 de la fase B y con la misma función del
lanzador de A2.1 (`conteos_hb2`), los mensajes del asistente, los `tool_use`, los `tool_result` y las llamadas del log R1
(`a2_1/controles/antecedente_HB2_faseB.json`):

- `num_turns` = `tool_result` + 1 en 12 de 12 sesiones; = mensajes del asistente en 8 de 12. Las 4 que difieren son las del
  brazo del grafo con llamadas paralelas (más de un `tool_use` en un mismo mensaje): SMK-01-kg, SMK-02-kg, SMK-03-kg y
  SMK-04-kg.
- SMK-04-kg: 9 mensajes del asistente, 13 `tool_use`, 13 llamadas en el log R1 y `num_turns` 14, con `--max-turns 12` y sin
  corte.
- Ninguna sesión cortó, y el brazo vectorial no hizo llamadas paralelas en ninguna.

## 3. Hipótesis y lo que se registra

- **H-a:** `num_turns` cuenta `tool_result` + 1 (una vuelta por resultado de tool, más la primera), no mensajes del
  asistente.
- **H-b:** `--max-turns N` acota los mensajes del asistente (las llamadas del modelo principal a la API), no `num_turns`: con
  llamadas paralelas, `num_turns` puede pasar de N sin que el corte dispare.
- Alternativas que el diseño puede separar: el límite acota `num_turns`, los `tool_use` o las llamadas del log R1.

Por sesión, en `meta_<id>.json["hb2"]` (lanzador de A2.1, `conteos_hb2`): `max_turns_efectivo`, `num_turns`, `subtype`,
`is_error`, `stop_reason`, mensajes del asistente (`message.id` distintos), `tool_use`, `tool_result`, eventos `user`,
mensajes con `tool_use`, máximo de `tool_use` por mensaje, llamadas del log R1, si el log R1 tiene `fin`, si el corte disparó
(`subtype` = `error_max_turns`) y si hubo `result`. Además, la meta completa del banco (R3, R7, R9).

## 4. Sesiones

Ocho sesiones en los dos brazos de fragmentos, con las preguntas propias de `smoke/preguntas_smoke.json` (anclas `cap:1.3`,
`pro:2.7`, `ric:1.1` y `ext:8.1`, territorio verificado el 23/08/2026 con 0 solapes). No escribo preguntas nuevas: una
pregunta compuesta es la unión de preguntas propias ya verificadas, con sus mismas anclas, en la plantilla «Respondé estas
{n} preguntas:» seguida de una por línea numerada. No abro EV2 ni corro el chequeo de territorio, que lee sus anclas.

| id | brazo | preguntas | `--max-turns` | para qué |
|---|---|---|---|---|
| HB2-01 | BM25 | SMK-04 | 1 | corte con el k más chico |
| HB2-02 | BM25 | SMK-04 | 2 | corte con k = 2 |
| HB2-03 | BM25 | SMK-01 + SMK-03 | 2 | inducir llamadas paralelas y cortar |
| HB2-04 | BM25 | SMK-01 + SMK-03 | 12 | control sin corte de HB2-03 |
| HB2-05 | BM25 | SMK-01 a SMK-04 | 3 | más temas que k |
| HB2-06 | denso | SMK-04 | 1 | réplica de HB2-01 |
| HB2-07 | denso | SMK-01 + SMK-03 | 2 | réplica de HB2-03 |
| HB2-08 | denso | SMK-01 a SMK-04 | 12 | control sin corte, el caso más parecido a SMK-04-kg |

Controles: las 12 sesiones del smoke de A2.1 (`--max-turns 12`), si ya corrieron. El resto de la configuración es la del
banco (prompt, tope de 10 llamadas en el prompt, `--max-budget-usd 0.30`).

## 5. Reglas de decisión (implementadas en `evaluar_hb2`)

Se evalúan sobre las sesiones con `result` (las que no lo tienen se excluyen y se declaran), dos veces: solo con las de A2.1
(H-B2 más el smoke) y con el antecedente de la fase B sumado.

- **R-a (qué cuenta `num_turns`):** un candidato (`tool_result` + 1, mensajes del asistente, eventos `user` + 1, llamadas del
  log R1 + 1) queda VERIFICADO si coincide con `num_turns` en todas las sesiones, con corte y sin corte.
- **R-b (qué acota `--max-turns`):** un conteo candidato (mensajes del asistente, `num_turns`, `tool_use`, llamadas del log
  R1) es compatible si en toda sesión sin corte vale a lo sumo k, y en toda sesión con corte vale k o k + 1. Resultado:
  CARACTERIZADO si queda uno solo; INDISTINGUIBLE si quedan varios (se declaran); NO CARACTERIZADO si no queda ninguno o si
  ninguna sesión cortó.
- **R-c (qué pasa al cortar):** por cada corte, el `subtype`, `is_error`, los conteos, si el log R1 tiene `fin` y si hay JSON
  final. Una sesión cortada no tiene el `result` de éxito: por R3 queda incompleta y fuera de la métrica.

Lo que cada resultado implica para R5 lo propone el FRENO A2.1-b con sus alternativas; el criterio lo fija la autora al firmar
el pre-registro (mandato, §4).

## 6. Costo y guardas

Cota de `a2_1/estimacion_tramo2.json` (`a2_1/estimar_tramo2.py`, desde los costos R9 medidos en la fase B en el brazo
vectorial): USD 0,7478 para las 8 sesiones de H-B2 y USD 1,1305 para el tramo 2 entero. Guardas del banco: tope autorizado
USD 3, freno en 2 sobre el acumulado de los dos pasos del tramo 2, freno por proyección en 2,4 y `--max-budget-usd 0.30` por
sesión.

## 7. Intérpretes

El runner, el lanzador y el envoltorio corren con `.venv/bin/python` del repo (Python 3.10.13); el servidor de fragmentos,
en los dos brazos, con el venv 3.12 recreado en A2.1 (`~/INGENIERIA IA/TESIS/venvs/banco_vector_py312`), con
`HF_HUB_OFFLINE=1` y `TRANSFORMERS_OFFLINE=1`.
