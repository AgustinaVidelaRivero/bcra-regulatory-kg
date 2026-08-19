# Propuesta de actualización de `docs/plan_tesis.md`

Propuesta, no aplicada: esta unidad solo escribe bajo `data/experiment/banco_mcp/gate/`.
El plan lo edita la autora.

## 1. Checkbox de la línea 158 (carril A, bloque A2)

Reemplazar `- [ ] **A2.0-gate**` por `- [x] **A2.0-gate**` y agregar al final de esa entrada:

> **Cerrada en FASE A (USD 0)**: veredicto **PASA CON CONDICIONES**
> (`data/experiment/banco_mcp/gate/veredicto_gate.md`). Las cuatro clases se reconstruyen desde
> una sesión real de Claude Code y el replay determinístico (estándar y fuerte) pasa: 10/11
> casos PASS, con el código de A0.2 **importado**. Los dos hallazgos que condicionan A2.0-banco:
> (i) el output íntegro de una tool solo sobrevive por un archivo de derrame fuera del repo
> (cap medido de 30.000 chars en el transcript) → **R1: log de llamadas del lado del servidor
> MCP, y la sesión pasa a ser índice, no fuente de verdad**; (ii) con tools v2 (laudo C11) el
> driver de replay congelado **no** replaya → **R2: driver de replay propio del contrato v2, o
> exponer la firma v1 por MCP**. Un corte de sesión no rompe la atribución: la **falsifica en
> silencio** (`generacion` → `vista_no_consultada`), de ahí R3. FASE B (smoke con `claude -p`,
> tope propuesto USD 2) queda **pendiente de autorización**.

## 2. Entrada de A2.0-banco (línea 159)

Agregar como dependencia explícita, después de «**Depende de A2.0-gate**»:

> Los requisitos **R1..R7** del veredicto del gate son parte del diseño de los servidores, no
> parches posteriores: R1 (log de llamadas server-side con output íntegro), R2 (driver de
> replay del contrato efectivamente usado, o firma v1 por MCP), R3 (marca de completitud por
> sesión y descarte contado de las trazas cortadas), R4 (contrato de salida JSON en el prompt),
> R5 (criterio de corte declarado que reemplace `hit_tool_limit`), R6 (aislamiento por
> capacidad — confirma lo ya previsto, y el filtrado que quede debe ser ruidoso), R7 (mapa
> `n → tool_use_id` por traza).

## 3. Nota sobre el transporte MCP

Agregar a A2.0-banco: la demostración por clase del gate corrió sobre el transporte **Bash**;
la rama MCP del adaptador está escrita a partir del formato observado pero **no ejecutada**, y
el cap de resultados MCP **no está medido** (máximo observado 24.063 chars sin truncado).
A2.0-banco debe repetir la demostración por clase sobre MCP antes de confiar en él.

## 4. M-21 (tabla de méritos)

En la fila M-21, la columna de evidencia puede citar ya
`data/experiment/banco_mcp/gate/corrida/demostracion_gate.md` para la parte «adaptador de
trazas que preserva el replay y la atribución causal», con la condición declarada de que la
preservación vale para el contrato v1 y exige R2 para v2.
