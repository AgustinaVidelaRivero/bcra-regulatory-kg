#!/bin/zsh
# A2.2, paso 3 (PAGO): el juez de EV2 sobre las respuestas de N = 1 (N = 3 por respuesta) y la población de N = 3.
# Primero, el control del SDK y de la versión de la API (registro, §93). El corte del juez (§6): tope 25 y freno 18,75.
# Lo corre la autora desde la Terminal, en la raíz del repo:  zsh data/experiment/banco_mcp/a2_2/paso3_juez_n1.zsh
# Costo estimado (pre-registro, §6; costos por sesión de la nota de la mesa, el del grafo NO VERIFICADO): 120 respuestas × 3 llamadas × 0,0126 = USD 4,54 (la cuenta de U-NAV, :243, NO VERIFICADA).
# Frena si un archivo del tramo o una entrada cambió, si hay otro paso pago corriendo (guardas_a2_2.zsh) o si el paso anterior no
# está completo. Imprime solo cuentas y costos.
set -euo pipefail
R="${0:A:h:h:h:h:h}"
cd "$R"
source data/experiment/banco_mcp/a2_2/guardas_a2_2.zsh
control_sdk
env -i "${ENTORNO[@]}" "$PY" -B "$A/juez_a2_2.py" n1 --autorizado-tope 25 --freno 18.75 --modo "${A22_JUEZ_MODO:-real}" "${EXTRA[@]}"
env -i "${ENTORNO[@]}" "$PY" -B "$A/poblacion_a2_2.py" --calcular "${EXTRA_POB[@]}"
