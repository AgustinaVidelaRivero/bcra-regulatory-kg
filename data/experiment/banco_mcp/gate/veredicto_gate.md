# Entregable 6 — VEREDICTO DEL GATE

# **PASA CON CONDICIONES**

La atribución causal de A0.2 **sobrevive** al harness de Claude Code: las cuatro clases se
reconstruyen desde una sesión real, el replay determinístico (estándar y fuerte) pasa, y todo
es reproducible byte a byte. Pero sobrevive **por cuatro apoyos que hoy no son parte del
instrumento** y que A2.0-banco tiene que convertir en requisitos explícitos de los servidores
MCP. Con el contrato de tools que el laudo C11 dejó elegido (tools v2), el replay **no**
sobrevive tal cual: necesita un driver nuevo.

FRENO acá: la autora lauda antes de construir el banco.

---

## 1. Qué quedó demostrado

Evidencia: `corrida/demostracion_gate.md` y `corrida/demostracion_gate.json`.
Comando que lo reproduce entero, sin API y sin red:

```
python3 -B data/experiment/banco_mcp/gate/code/adaptador_cc.py adaptar
python3 -B data/experiment/banco_mcp/gate/code/demostracion_gate.py
```

| caso | qué prueba | clase esperada | obtenida | replay | replay fuerte | resultado |
|---|---|---|---|---|---|---|
| GATE-01 | `ausencia_kg` por ausencia total | ausencia_kg | ausencia_kg | ok | ok | PASS |
| GATE-02 | `ausencia_kg` por portador contenedor | ausencia_kg | ausencia_kg | ok | ok | PASS |
| GATE-03 | `alcanzabilidad` | alcanzabilidad | alcanzabilidad | ok | ok | PASS |
| GATE-04 | `vista_no_consultada` | vista_no_consultada | vista_no_consultada | ok | ok | PASS |
| GATE-05 | `generacion` vía `ver_nodo` | generacion | generacion | ok | ok | PASS |
| GATE-06 | `generacion` vía `ver_vecinos` (precedencia V,F,V) | generacion | generacion | ok | ok | PASS |
| GATE-07 | borde: sesión sin tool calls | alcanzabilidad | alcanzabilidad | ok | ok | PASS |
| GATE-08 | borde: tools vacías y `ver_nodo` con error | alcanzabilidad | alcanzabilidad | ok | ok | PASS |
| GATE-09 | borde: corte de sesión | generacion | **vista_no_consultada** | ok | ok | PASS *por detección* |
| GATE-10 | borde: output por encima del cap del transporte | generacion | generacion | ok | ok | PASS |
| GATE-11 | contrato v2 (laudo C11) | generacion | generacion | **falla** | **falla** | FAIL |

Además:

- **Determinismo de la atribución**: dos corridas de `atribuir_payload` por caso, comparadas
  byte a byte → idénticas en los 11 casos.
- **Determinismo del adaptador**: re-adaptar la rebanada cruda a un directorio temporal produce
  las 11 trazas byte a byte iguales a las persistidas (salvo `meta.generado`).
- **Código de A0.2 importado, no reimplementado**: `demostracion_gate.py` hace
  `from atribucion_fallas import atribuir_payload, clasificar, resolver_anclas`, que arrastra
  `metrica.evaluar_traza` y `metrica_ev2.verificar_steps_full`. Ningún archivo sellado se editó
  (sha256 verbatim al inicio y al cierre en el reporte de la unidad).
- **Ruido rechazado ruidosamente**: de 24 comandos candidatos de la sesión, 3 eran comandos de
  construcción de la propia unidad (heredocs, pipes) y fueron rechazados con motivo explícito;
  los 21 restantes son exactamente los steps de los 10 casos con navegación
  (12 + 3 + 2 + 2 + 2 = 21). Ningún step legítimo se perdió.

## 2. Los cuatro apoyos que hoy no son parte del instrumento

### A1 — El output íntegro sobrevivió por un archivo de derrame fuera del repo

`toolUseResult.stdout` está **capeado a 30.000 chars** (medición: `corrida/medicion_transporte.json`,
máximo exacto 30.000 sobre 5.783 resultados de Bash). GATE-10 devolvió 42.248 chars: en el
jsonl solo hay 30.000. El replay fuerte pasó **únicamente** porque Claude Code derramó el output
completo a `<session_dir>/tool-results/<id>.txt` y lo declaró en `persistedOutputPath` /
`persistedOutputSize`, y el adaptador lo siguió.

Qué se pierde si ese apoyo falta: `output_chars` y `steps_full[*].output` quedan
irrecuperables → **el replay fuerte se vuelve imposible** y el estándar también (compara contra
`output_chars` exacto). La clase se sigue computando (§4), pero **deja de ser auditable**, que
es exactamente el diferencial de la tesis.

Fragilidad concreta: ese directorio **no está en el repo**, no está versionado, y su
permanencia no está garantizada por nada que la autora controle.

### A2 — El corte de sesión no rompe la atribución: la falsifica en silencio

GATE-09 es la misma navegación de GATE-05 (que da `generacion`) con la sesión cortada entre el
`tool_use` del paso 2 y su `tool_result`. La atribución computada sobre esa traza incompleta da
**`vista_no_consultada`**: una clase **plausible, distinta y falsa**. No hay ninguna señal en la
traza que lo delate; lo único que lo delata es la guarda que este adaptador implementa
(`gate.corte_sesion = true`, `gate.atribuible = false` cuando hay un `tool_use` sin su
`tool_result`).

Esto generaliza al riesgo estructural ya anticipado en el inventario §3: `alcanzabilidad` y
`vista_no_consultada` se afirman **por negación**, así que **cualquier step perdido migra la
clase hacia arriba en el embudo** sin error visible.

### A3 — El contrato v1 y el driver de replay congelado son la misma cosa

`metrica._reejecutar_step` (módulo congelado, se importa y no se edita) despacha exactamente
`buscar_nodos(consulta, limite)` / `ver_nodo(id)` / `ver_vecinos(id, direccion)`. Las tools v2
de A1.2 —las que el laudo C11 de A1.4 dejó elegidas para el banco— cambian la firma de
`ver_vecinos` (`relacion`, `pagina`, `por_pagina`) y su payload (bloques paginados).

Resultado medido en GATE-11: la **semántica** de la atribución sobrevive intacta (el ancla
aparece como `vecino_id` en `salientes`, la clase computada es la correcta), pero el replay
falla en el step de `ver_vecinos`, en las dos verificaciones:
`replay_fallas = [{"n": 2, "tool": "ver_vecinos", "motivo": "prefijo_distinto"}]`,
`replay_fuerte_fallas = [{"n": 2, "tool": "ver_vecinos", "motivo": "output_completo_distinto"}]`.

**El juguete subestima el daño**: acá `buscar_nodos` v2 delega en el mismo índice léxico, así
que replaya. En el banco real `buscar_nodos` v2 es BM25 sobre Neo4j y el driver congelado lo
re-ejecutaría con el índice léxico de `GraphIndex` → **también divergiría**. Con tools v2 sobre
Neo4j, el replay congelado falla en **todos** los steps, no en uno.

### A4 — Tres campos del formato de traza no existen en Claude Code

| campo | estado | consecuencia |
|---|---|---|
| `trace.final_json` (y `respondible`) | **no existe**: Claude Code no impone el contrato de salida JSON del harness | el metadato `respondible_flag` de la regla §5 queda en `null` |
| `trace.hit_tool_limit` | **no existe**: no hay `MAX_TOOL_CALLS` | no se puede distinguir «el agente terminó» de «el agente se quedó sin llamadas» — que es una de las lecturas de A1.4 |
| `n` (ordinal del step) | **es una convención de esta unidad**, no un dato | se persiste el mapa `n → tool_use_id / línea / uuid / timestamp` en `gate.mapa_steps` para que la renumeración sea auditable |

## 3. Requisitos que esto le impone a A2.0-banco

Este es el entregable de valor del gate. Los requisitos R1 y R2 son **bloqueantes**: sin ellos
el banco produce veredictos pero no atribución auditable, y el diferencial de la tesis se cae.

**R1 (bloqueante) — Log de llamadas del lado del servidor.**
Cada servidor MCP persiste su propio registro, una entrada por llamada, con: `tool`, `input`
íntegro, `output` íntegro **sin truncar**, timestamp, versión del servidor, sha256 del `kg.json`
(o del índice vectorial), y el `tool_use_id` de la llamada. La traza del banco se arma **desde
ese log**; la sesión de Claude Code pasa a ser el **índice** (qué llamó el agente, en qué orden,
en qué sesión), no la fuente de verdad del contenido. Esto elimina A1 de raíz: ni el cap de
30.000 chars ni la permanencia del directorio de derrames vuelven a importar.

**R2 (bloqueante) — Driver de replay para el contrato efectivamente usado.**
Si el banco enchufa tools v2, A2.0-banco debe entregar un **módulo nuevo** de replay (jamás una
edición de `metrica.py`) que re-ejecute cada step con la firma v2 contra el **mismo backend**
que usó el agente (Neo4j, mismo grafo, misma config de retriever), y alimente los conjuntos
`vista` / `consultada` a la `clasificar()` importada de A0.2 — la regla no se toca, se toca el
mecanismo de observación. Ese módulo necesita su propio selftest con la misma cobertura que el
de A0.2 (4 clases + bordes + tabla de verdad). Alternativa admisible y más barata: **que el
servidor MCP exponga exactamente la firma v1**, y entonces todo el aparato congelado se reusa
verbatim; el costo es renunciar a la paginación de `ver_vecinos` que A1.4 midió como capacidad
presente pero **no operante** (0/275 paginaciones), lo que hace la renuncia mucho menos cara de
lo que parece.

**R3 — Marca de completitud por sesión.**
El servidor (o el runner) escribe un registro de cierre por sesión con el `stop_reason` del
modelo y el conteo de llamadas. Toda traza sin ese registro, o con un `tool_use` sin
`tool_result`, se marca **no atribuible** y queda fuera del denominador, contada. Sin esto, un
corte produce una clase falsa y creíble (A2).

**R4 — Contrato de salida en el prompt del banco.**
El prompt del agente debe exigir el mismo JSON final del harness (`respuesta`, `citas`,
`respondible`), para que `final_json` exista y el metadato de la regla §5 sea comparable con
EV2. Sin esto la columna existe pero está vacía en un brazo.

**R5 — Criterio de corte declarado y registrado.**
Reemplazo explícito de `hit_tool_limit`: un tope de tool calls por sesión, declarado antes de
correr y persistido por traza, con un flag equivalente. Si no hay tope, se declara que no lo hay
y la comparación con EV2 en esa dimensión no se hace.

**R6 — Aislamiento por capacidad, verificado (ya previsto en A2.0-banco: se confirma).**
En esta captura convivieron tools del grafo con Bash, Read y demás; el adaptador tuvo que
filtrar y rechazó 3 comandos. En el banco, el agente debe tener **solo** las tools de su brazo:
así el adaptador no filtra nada y no hay superficie donde perder un step. Mientras el filtrado
exista, tiene que seguir siendo **ruidoso**: rechazo con motivo, nunca descarte silencioso.

**R7 — Trazabilidad de la renumeración.**
Persistir por traza el mapa `n → tool_use_id / uuid / timestamp` (implementado acá en
`gate.mapa_steps`). Sin él, `vista_en_step` y `consultada_en_step` son números sin origen.

## 4. Qué NO probó esta unidad (limitaciones declaradas)

1. **El transporte MCP no se ejercitó.** El mandato excluye exponer MCP en esta unidad, así que
   la captura usó el transporte Bash. La rama MCP del adaptador está escrita a partir del
   formato **observado** en sesiones reales (`toolUseResult` como lista de bloques `{type:"text",
   text: …}` con el `input` estructurado verbatim) pero **no está ejecutada**. A2.0-banco debe
   correr esta misma demostración por clase sobre el transporte MCP antes de confiar en él. En
   particular, el cap de resultados MCP **no fue alcanzado** en la evidencia disponible (máximo
   24.063 chars observados, sin marca de truncado): no está medido, y no se puede afirmar que
   no exista.
2. **La navegación está puesta en escena.** Las secuencias de tool calls fueron elegidas para
   producir una clase por caso. Lo que se midió es el **adaptador y la atribución**, no la
   calidad del agente. La Fase B reemplaza la puesta en escena por `claude -p` de verdad.
3. **El mini-grafo es de juguete** (9 nodos): no dice nada sobre escala, latencia ni sobre el
   comportamiento del retriever real.
4. **No se ejercitó la contabilidad de costos ni la vía de credenciales**: son de A2.0-banco.

## 5. Qué pasa si el laudo decide no cumplir R1 o R2

Es la pregunta que el gate existe para contestar, así que queda escrita:

- **Sin R1**: el banco produce veredictos comparables (la tabla de correcto/parcial/incorrecto
  sigue en pie) pero la atribución causal deja de ser **auditable por replay**: se podría
  computar la clase desde `(tool, input, orden)`, y habría que declarar en la tesis que en ese
  brazo la atribución no está verificada por replay determinístico. El head-to-head cambia de
  forma: pasa a ser una comparación de resultados, no de mecanismos de falla.
- **Sin R2 y con tools v2**: mismo efecto que sin R1, pero peor, porque además el output
  persistido no se puede contrastar contra nada re-ejecutable. La salida barata es exponer la
  firma v1 por MCP.
- **Con R1 y R2**: el head-to-head mantiene su forma actual y la atribución causal por clase se
  reporta igual que en EV2, con la misma regla sellada y el mismo código.

## 6. Recomendación

Autorizar la FASE B (smoke) **solo para confirmar el transporte con `claude -p`** — lo caro ya
está resuelto offline — y laudar R1..R7 **antes** de escribir una línea de los servidores MCP.
El orden importa: R1 y R2 son decisiones de **diseño de los servidores**, no parches
posteriores, y esa es exactamente la razón por la que el gate va primero.
