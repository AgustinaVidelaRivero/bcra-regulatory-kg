#!/bin/bash
# U-OMISIONES-COD, O2: los selftests de la cadena sobre una COPIA (nunca sobre el repo).
# Uso: bateria_selftests_O2.sh <python> <copia> <salida> <scripts> <git_dir_solo_lectura> [<r2 diez> <r2 sin cola diez>]
set -u
PY="$1"; CP="$2"; OUT="$3"; SC="$4"; GD="$5"; R2="${6:-}"; R2S="${7:-}"
export PYTHONDONTWRITEBYTECODE=1; unset ANTHROPIC_API_KEY
mkdir -p "$OUT"; cd "$CP" || exit 2
corre() { local n="$1"; shift; "$PY" -B "$@" > "$OUT/$n.txt" 2>&1; echo "rc=$?" >> "$OUT/$n.txt"; }
corre selftest_pyd_r2 data/experiment/pyd_r2/code/selftest_pyd_r2.py
corre selftest_r3 data/experiment/r2_codigo/selftest_r3.py
corre selftest_e2 data/experiment/reextraccion_v2/e2_reduce/selftest_e2.py
corre selftest_reresolver_catalogo data/experiment/reresolucion_catalogo/selftest_reresolver_catalogo.py
corre selftest_regression_kg scripts/selftest_regression_kg.py
corre selftest_prompt_r2b data/experiment/reextraccion_v2/e1_extractor/selftest_prompt_r2b.py
corre pruebas_t3bis data/experiment/reext_t0/t3bis/pruebas_t3bis.py --out "$OUT/pruebas_t3bis.json"
GIT_DIR="$GD" GIT_OPTIONAL_LOCKS=0 corre selftest_catalogo_unico data/experiment/catalogo_unico/code/selftest_catalogo_unico.py
corre selftest_clave_cache data/experiment/mantenimiento/code/selftest_clave_cache.py --out "$OUT/selftest_clave_cache.json"
corre selftest_comparador_P data/experiment/med_umbrales/p/code/selftest_comparador_P.py
corre gate6_ii "$SC/gate6_ii_en_copia.py" "$PY"
if [ -f data/experiment/omisiones_cod/selftest_ensamblado_omisiones.py ]; then
  corre selftest_ensamblado_omisiones data/experiment/omisiones_cod/selftest_ensamblado_omisiones.py ${R2:+--salida-r2 "$R2"} ${R2S:+--salida-r2-sincola "$R2S"}
  corre selftest_metrica_condiciones data/experiment/omisiones_cod/selftest_metrica_condiciones.py --kg-a9631a64 data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2b/r2/kg.json
fi
echo fin
