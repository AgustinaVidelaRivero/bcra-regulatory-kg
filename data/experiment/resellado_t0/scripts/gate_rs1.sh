#!/bin/bash
# Re-sellado único de la tanda 0, §3.1 y §3.2: shapes (perfil r2, fase r2b) y suite (perfil r2, con la fixture de la raíz)
# sobre un ensamblado, con los mismos argumentos que U-SINCOLA-T0 (sincola_t0/sc2/comandos_sc2_repo.sh). Corre sobre una
# COPIA del repo, nunca sobre el repo. USD 0, sin API.
# Uso: gate_rs1.sh <python> <copia> <dir del ensamblado (con r2/)> <dir de salida> <que: shapes|suite|ambas>
#   las salidas se llaman como en los ensamblados sellados: shapes_perfil_r2_fase_r2b.{md,json} y suite_perfil_r2.{md,json}
set -u
PY="$1"; CP="$2"; N="$3"; OUT="$4"; QUE="$5"
export PYTHONDONTWRITEBYTECODE=1; unset ANTHROPIC_API_KEY
cd "$CP" || exit 2
X=data/experiment/reextraccion_v2; E0=$X/e0_chunking/salida_tanda0_r2b
EXC=data/experiment/catalogo_unico/generados_r2/entrada_esqueleto_r2.json
CAT=data/experiment/catalogo_unico/generados_r2/catalogo_suite_r2.json
mkdir -p "$OUT"
if [ "$QUE" = shapes ] || [ "$QUE" = ambas ]; then
  "$PY" -B scripts/shapes_validator.py --kg "$N/r2/kg.json" --perfil r2 --fase r2b --e0 $E0 --registro-dir "$N/r2" \
    --excepciones $EXC --out "$OUT/shapes_perfil_r2_fase_r2b.md" > "$OUT/consola_shapes.txt" 2>&1
  echo "rc=$?" >> "$OUT/consola_shapes.txt"
fi
if [ "$QUE" = suite ] || [ "$QUE" = ambas ]; then
  "$PY" -B scripts/regression_kg.py --kg "$N/r2/kg.json" --perfil r2 --generacion 3 --catalogo $CAT \
    --politica-cuarentena flaggeada --registro-dir "$N/r2" --esperado scripts/regression_kg_esperado.json \
    --out "$OUT/suite_perfil_r2.md" > "$OUT/consola_suite.txt" 2>&1
  echo "rc=$?" >> "$OUT/consola_suite.txt"
fi
