#!/bin/zsh
# B6.1, tanda 1, T3, punto 4: los selftests de la cadena y el de claves, los del gate final del laudo
# (data/experiment/laudo_release_r2/gate_final/gate_final_laudo_r2_mesa.sh:60-72), sobre un clon de la copia (nunca el repo): pueden
# reescribir archivos. USD 0, sin API.
# Uso: zsh selftests_t3.sh <python del repo> <clon> <dir de salida>
set -u
PY="$1"; C="$2"; S="$3"; mkdir -p "$S"
export PYTHONDONTWRITEBYTECODE=1; unset ANTHROPIC_API_KEY
st() { local n="$1"; shift; ( cd "$C" && print -r -- "inicio $(date '+%Y-%m-%d %H:%M:%S')" > "$S/$n.txt" && "$PY" -B "$@" >> "$S/$n.txt" 2>&1; print -r -- "rc=$?" >> "$S/$n.txt"; print -r -- "fin $(date '+%Y-%m-%d %H:%M:%S')" >> "$S/$n.txt" ); }
st regression_kg_1 scripts/selftest_regression_kg.py
st regression_kg_2 scripts/selftest_regression_kg.py
st shapes_congelado scripts/selftest_shapes_congelado.py
st clave_cache data/experiment/mantenimiento/code/selftest_clave_cache.py --out "$S/selftest_clave_cache_t3.json"
st pyd_r2 data/experiment/pyd_r2/code/selftest_pyd_r2.py
st r3 data/experiment/r2_codigo/selftest_r3.py
st ensamblado_omisiones data/experiment/omisiones_cod/selftest_ensamblado_omisiones.py
st metrica_condiciones data/experiment/omisiones_cod/selftest_metrica_condiciones.py
st catalogo_unico data/experiment/catalogo_unico/code/selftest_catalogo_unico.py
st e0 data/experiment/reextraccion_v2/e0_chunking/selftest_e0.py
print -r -- "fin del lote $(date '+%Y-%m-%d %H:%M:%S')" > "$S/fin.txt"
