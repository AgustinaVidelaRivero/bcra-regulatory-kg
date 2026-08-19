# Laudo — gate de trazabilidad del banco de evaluación (requisitos R1–R7)

Fecha: 2026-08-18. Unidad laudada: **A2.0-gate** (`docs/plan_tesis.md` v3), fase A.
Evidencia sobre la que decido: `data/experiment/banco_mcp/gate/` — `veredicto_gate.md`
(veredicto **PASA CON CONDICIONES**, demostración por clase 10/11 PASS, atribución con doble
corrida byte-idéntica en los 11 casos), `inventario_campos.md`, `corrida/`, `sesiones/`.
Costo de la unidad: USD 0. Este laudo gobierna el diseño de **A2.0-banco**: sus decisiones se
toman antes de escribir una línea de los servidores MCP, porque son decisiones de diseño y no
parches posteriores.

## 1. Qué quedó demostrado y qué no

Demostrado: la atribución causal de A0.2 (`data/experiment/ev2_reporte/regla_atribucion.md`,
commit `40603a9`) se reconstruye desde una sesión del harness de Claude Code para las cuatro
clases, con el código de atribución **importado** y el replay determinístico en verde,
reproducible byte a byte.

No demostrado, y declarado como límite de esta unidad: (a) el transporte **MCP** no se
ejercitó — la demostración corrió sobre tool calls de sesión, no sobre servidores MCP; (b) el
tope de tamaño de los resultados por MCP no está medido; (c) la navegación de las sesiones fue
escenificada para producir una clase por caso (lo medido es el adaptador, no la calidad del
agente).

## 2. Decisión por requisito

**R1 — Log de llamadas del lado del servidor MCP, con entrada y salida íntegras. ACEPTADO,
bloqueante.** La sesión de Claude Code pasa a ser **índice**, no fuente de verdad: el registro
del servidor es la evidencia. Motivo medido: el registro de sesión trunca el resultado de una
tool a 30.000 caracteres, y el único caso que excedió ese tope (42.248 chars) sobrevivió porque
el harness derramó el texto completo a un archivo fuera del repo. Depender de ese derrame es
depender de un detalle de implementación de un tercero, no versionado.

**R2 — Driver de replay para el contrato efectivamente usado. ACEPTADO, bloqueante, con la
OPCIÓN B: el banco expone la firma v1 de las tools.** Fundamento medido, no de conveniencia: en
la ablación A1.4 (commit `ffc6ff6`) las tools v2 no produjeron mejora atribuible (P4 no
cumplida) y **el agente no paginó en ninguna de las 275 llamadas**; escribir y validar un driver
de replay nuevo para conservar una capacidad sin efecto medido no es una buena asignación del
tiempo restante. Consecuencias que declaro acá y que se registran en el plan:

- el puente de calibración **A1.7 pasa a usar C10 {BM25, tools v1}** como base congelada en
  lugar de C11: sigue siendo una comparación de una sola variable (agente), con la base también
  medida en la tabla sellada de A1.4;
- el brazo `contexto_de` de A1.7 queda del lado del **harness congelado**, no del banco;
- si en el futuro hiciera falta medir tools v2 en el banco, se escribe el driver como **módulo
  nuevo**. En ningún escenario se edita `metrica.py` ni ninguna pieza del cuarteto congelado.

**R3 — Marca de completitud por sesión. ACEPTADO.** Es la condición para que un corte no se
convierta en un dato falso: dos de las cuatro clases (`alcanzabilidad`, `vista_no_consultada`)
se afirman por ausencia, de modo que un paso perdido migra la clase en silencio. Toda traza sin
marca de completitud se excluye de la métrica y se declara; nunca se atribuye.

**R4 — Contrato de salida en el prompt del banco. ACEPTADO.** El formato de traza del repo
espera una respuesta final estructurada; el harness nuevo no la trae de fábrica. El contrato de
salida se fija en el prompt, es idéntico en los dos brazos y se sella con el resto de la
configuración del banco.

**R5 — Criterio de corte declarado y registrado. ACEPTADO.** Reemplaza al tope de 15 llamadas
del harness congelado. Se declara antes de correr, se registra por traza (turnos y llamadas), y
se reporta como métrica propia del banco; no se compara numéricamente con `hit_tool_limit`.

**R6 — Aislamiento por capacidad. ACEPTADO** (ya estaba previsto en A2.0-banco; el gate lo
confirma).

**R7 — Trazabilidad de la numeración de pasos a identificadores de llamada. ACEPTADO.**

## 3. Fase B del gate

**Autorizada**, con tope de **USD 2** y precios verificados contra documentación oficial antes
de correr. Alcance: reemplazar las sesiones escenificadas por corridas reales con `claude -p` y
modelo fijo, repetir la demostración por clase y el replay, y **medir el consumo del prompt de
sistema del harness** (primer paso: una sesión descartable que reporte uso), número que hoy no
tenemos y que hace falta para estimar A2.

## 4. Pendientes que este laudo traslada a A2.0-banco

1. **Repetir la demostración por clase sobre el transporte MCP** — es condición de aceptación de
   A2.0-banco, no un extra: lo demostrado hasta acá vale para tool calls de sesión.
2. Medir el tope de tamaño de resultados por MCP y declararlo.
3. Implementar R1–R7 como parte del diseño de los servidores.

## 5. Regla que no cambia

Nada de lo anterior toca el cuarteto congelado ni las zonas selladas. Los resultados del banco
no se cruzan en una misma tabla con los del harness congelado (principio 8 del plan); el puente
entre instrumentos es A1.7.
