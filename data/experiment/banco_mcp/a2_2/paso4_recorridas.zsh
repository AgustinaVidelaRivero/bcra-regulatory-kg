#!/bin/zsh
# A2.2, paso 4 (PAGO): las tres re-corridas (r2, r3 y r4) de cada par de la población de N = 3, por repetición y en el
# orden de N = 1. Pide las 120 de N = 1 y la población del paso 3. Corte del agente: tope 93 y freno 69,75.
# Lo corre la autora desde la Terminal, en la raíz del repo:  zsh data/experiment/banco_mcp/a2_2/paso4_recorridas.zsh
# Costo estimado (pre-registro, §6; costos por sesión de la nota de la mesa, el del grafo NO VERIFICADO): 3 × P sesiones por brazo; con P = 40 (la cota), 360 sesiones: USD 15,71 central, 27,28 medio, 50,40 alto.
# Frena si un archivo del tramo o una entrada cambió, si hay otro paso pago corriendo (guardas_a2_2.zsh) o si el paso anterior no
# está completo. Imprime solo cuentas y costos.
set -euo pipefail
R="${0:A:h:h:h:h:h}"
cd "$R"
source data/experiment/banco_mcp/a2_2/guardas_a2_2.zsh
env -i "${ENTORNO[@]}" "$PY" -I -B data/experiment/banco_mcp/a2_1/con_clave_del_entorno.py \
  --entorno "${A22_ENTORNO:-data/experiment/evaluacion/.env}" -- \
  "$PY" -B "$A/correr_a2_2.py" recorridas --autorizado-tope 93 --freno 69.75 --modo "${A22_MODO:-real}" "${EXTRA[@]}"
