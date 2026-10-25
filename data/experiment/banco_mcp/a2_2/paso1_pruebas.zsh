#!/bin/zsh
# A2.2, paso 1 (PAGO): las tres sesiones de prueba de A-D5, una por brazo, con la pregunta SMK-01 del smoke del tramo 2
# de A2.1, antes de la primera de EV2. Frena además si una falla R3 (la sesión completa) o R6 (el inventario de tools): código 4.
# El corte del agente (§6): tope 93 y freno 69,75, sobre el acumulado R9 de todas las sesiones de A2.2 más 1,80 por sesión.
# Lo corre la autora desde la Terminal, en la raíz del repo:  zsh data/experiment/banco_mcp/a2_2/paso1_pruebas.zsh
# Costo estimado (pre-registro, §6; costos por sesión de la nota de la mesa, el del grafo NO VERIFICADO): 3 sesiones: USD 0,13 central, 0,23 medio, 0,42 alto.
# Frena si un archivo del tramo o una entrada cambió, si hay otro paso pago corriendo (guardas_a2_2.zsh) o si el paso anterior no
# está completo. Imprime solo cuentas y costos.
set -euo pipefail
R="${0:A:h:h:h:h:h}"
cd "$R"
source data/experiment/banco_mcp/a2_2/guardas_a2_2.zsh
env -i "${ENTORNO[@]}" "$PY" -I -B data/experiment/banco_mcp/a2_1/con_clave_del_entorno.py \
  --entorno "${A22_ENTORNO:-data/experiment/evaluacion/.env}" -- \
  "$PY" -B "$A/correr_a2_2.py" pruebas --autorizado-tope 93 --freno 69.75 --modo "${A22_MODO:-real}"
