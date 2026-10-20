#!/bin/bash
# B6.1, tanda final, T3, punto 4: shapes (perfil r2, fase r2b) y suite (perfil r2, con la fixture de la raíz) sobre un ensamblado, con
# data/experiment/tanda1/t3/scripts/gate_t3.sh copiado sin cambiar los argumentos (los del re-sellado). Corre sobre una COPIA del repo,
# nunca sobre el repo. USD 0, sin API.
# Uso: gate_tf.sh <python> <copia> <dir del ensamblado (con r2/)> <E0 del grafo> <dir de salida> <que: shapes|suite|ambas>
#   las salidas se llaman como en los ensamblados sellados: shapes_perfil_r2_fase_r2b.{md,json} y suite_perfil_r2.{md,json}
set -u
PY="$1"; CP="$2"; N="$3"; E0="$4"; OUT="$5"; QUE="$6"
export PYTHONDONTWRITEBYTECODE=1; unset ANTHROPIC_API_KEY
cd "$CP" || exit 2
EXC=data/experiment/catalogo_unico/generados_r2/entrada_esqueleto_r2.json
CAT=data/experiment/catalogo_unico/generados_r2/catalogo_suite_r2.json
mkdir -p "$OUT"
if [ "$QUE" = shapes ] || [ "$QUE" = ambas ]; then
  "$PY" -B scripts/shapes_validator.py --kg "$N/r2/kg.json" --perfil r2 --fase r2b --e0 "$E0" --registro-dir "$N/r2" \
    --excepciones $EXC --out "$OUT/shapes_perfil_r2_fase_r2b.md" > "$OUT/consola_shapes.txt" 2>&1
  echo "rc=$?" >> "$OUT/consola_shapes.txt"
fi
if [ "$QUE" = suite ] || [ "$QUE" = ambas ]; then
  "$PY" -B scripts/regression_kg.py --kg "$N/r2/kg.json" --perfil r2 --generacion 3 --catalogo $CAT \
    --politica-cuarentena flaggeada --registro-dir "$N/r2" --esperado scripts/regression_kg_esperado.json \
    --out "$OUT/suite_perfil_r2.md" > "$OUT/consola_suite.txt" 2>&1
  echo "rc=$?" >> "$OUT/consola_suite.txt"
fi
