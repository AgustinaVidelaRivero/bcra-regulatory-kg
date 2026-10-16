#!/bin/zsh
# A2.1, tramo 2, paso 2 (PAGA): la caracterización de H-B2 (8 sesiones; cota USD 0,7478).
# Lo corre la autora desde la raíz del repo:  zsh data/experiment/banco_mcp/a2_1/tramo2_paso2_hb2.zsh
# Guardas del banco (D-C): tope autorizado USD 3 y freno en 2, para todo el tramo 2 (el acumulado
# suma las sesiones de los dos pasos). La clave la toma el envoltorio del .env del repo, dentro de
# este comando: no se escribe, no se imprime y no queda en el historial de la terminal.
# A21_ENTORNO, A21_MODO y A21_PYTHON existen solo para la corrida en seco (archivo falso, modo
# init, intérprete del .venv del repo desde una copia, que no lleva .venv); sin ellos, el script
# usa data/experiment/evaluacion/.env, el modo real y el .venv del repo.
set -euo pipefail
R="${0:A:h:h:h:h:h}"
cd "$R"
# El venv 3.12 del servidor de fragmentos (requirements_vector.txt), recreado en A2.1 en reemplazo del
# del bake-off; el modelo se usa solo desde la caché local.
export BANCO_VENV_VECTOR="${BANCO_VENV_VECTOR:-$HOME/INGENIERIA IA/TESIS/venvs/banco_vector_py312}"
export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1
PY="${A21_PYTHON:-$R/.venv/bin/python}"
"$PY" -I -B data/experiment/banco_mcp/a2_1/con_clave_del_entorno.py \
  --entorno "${A21_ENTORNO:-data/experiment/evaluacion/.env}" -- \
  "$PY" -B data/experiment/banco_mcp/a2_1/correr_a2_1.py \
  --fase hb2 --autorizado-tope 3 --freno 2 --modo "${A21_MODO:-real}"
