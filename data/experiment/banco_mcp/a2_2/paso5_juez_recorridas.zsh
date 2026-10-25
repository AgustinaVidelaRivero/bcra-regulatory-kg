#!/bin/zsh
# A2.2, paso 5 (PAGO): el juez de EV2 sobre las respuestas de las re-corridas (N = 3 por respuesta). Primero, el
# control del SDK. El corte del juez: tope 25 y freno 18,75, sobre el acumulado del juez de toda A2.2.
# Lo corre la autora desde la Terminal, en la raíz del repo:  zsh data/experiment/banco_mcp/a2_2/paso5_juez_recorridas.zsh
# Costo estimado (pre-registro, §6; costos por sesión de la nota de la mesa, el del grafo NO VERIFICADO): 3 × P respuestas por brazo × 3 llamadas × 0,0126; con P = 40, USD 13,61 (NO VERIFICADO).
# Frena si un archivo del tramo o una entrada cambió, si hay otro paso pago corriendo (guardas_a2_2.zsh) o si el paso anterior no
# está completo. Imprime solo cuentas y costos.
set -euo pipefail
R="${0:A:h:h:h:h:h}"
cd "$R"
source data/experiment/banco_mcp/a2_2/guardas_a2_2.zsh
control_sdk
env -i "${ENTORNO[@]}" "$PY" -B "$A/juez_a2_2.py" recorridas --autorizado-tope 25 --freno 18.75 --modo "${A22_JUEZ_MODO:-real}" "${EXTRA[@]}"
