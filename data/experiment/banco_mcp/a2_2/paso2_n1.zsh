#!/bin/zsh
# A2.2, paso 2 (PAGO): N = 1 de las 40 preguntas de EV2 en los tres brazos (120 sesiones), en el orden de
# orden_corridas_a2_2.json. Pide las tres pruebas completas y en verde. Corte del agente: tope 93 y freno 69,75.
# Lo corre la autora desde la Terminal, en la raíz del repo:  zsh data/experiment/banco_mcp/a2_2/paso2_n1.zsh
# Costo estimado (pre-registro, §6; costos por sesión de la nota de la mesa, el del grafo NO VERIFICADO): 120 sesiones: USD 5,24 central, 9,09 medio, 16,80 alto.
# Frena si un archivo del tramo o una entrada cambió, si hay otro paso pago corriendo (guardas_a2_2.zsh) o si el paso anterior no
# está completo. Imprime solo cuentas y costos.
set -euo pipefail
R="${0:A:h:h:h:h:h}"
cd "$R"
source data/experiment/banco_mcp/a2_2/guardas_a2_2.zsh
env -i "${ENTORNO[@]}" "$PY" -I -B data/experiment/banco_mcp/a2_1/con_clave_del_entorno.py \
  --entorno "${A22_ENTORNO:-data/experiment/evaluacion/.env}" -- \
  "$PY" -B "$A/correr_a2_2.py" n1 --autorizado-tope 93 --freno 69.75 --modo "${A22_MODO:-real}" "${EXTRA[@]}"
