# Nota de re-etiquetado (laudo C3) — corrida 1 de fase B

Los archivos de esta carpeta NO se editan: son evidencia de la corrida 1 bajo Claude Code 2.1.196.
Con la regla R3 aprobada en el laudo C3 (`completa` exige `inventario_tools_R6.coincide == true` y
todos los servidores MCP `connected` en el `system/init`), las dos sesiones que `meta_*.json`
marca `completa: true` pasan a **incompletas**:

| sesión | `completa` en el archivo | `completa` según C3 | motivo |
|---|---|---|---|
| P0-kg | true | **false** | `tools_en_init = []`, `mcp_servers = [{kg: pending}]` |
| E2E-kg | true | **false** | ídem |

Las otras 10 ya eran `false`. Resultado de la corrida 1 bajo C3: **0/12 completas**; ninguna traza
se atribuye. El P0 medido (2.162 tokens, kg) queda declarado como **cota inferior** sin definiciones
de tools (laudo C5).
