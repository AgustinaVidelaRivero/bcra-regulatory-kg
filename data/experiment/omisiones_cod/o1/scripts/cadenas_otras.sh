#!/bin/bash
# Las otras cuatro cadenas de controles_r2_1.sh (r2a diez y desarrollo; r2b desarrollo con y sin cola), sobre una copia.
# Uso: cadenas_otras.sh <python> <copia> <salida>
set -u
PY="$1"; CP="$2"; OUT="$3"
export PYTHONDONTWRITEBYTECODE=1; unset ANTHROPIC_API_KEY
cd "$CP" || exit 2
X=data/experiment/reextraccion_v2; T=$X/corpus_tanda0; MAN=$X/manifiestos
E0A=$X/e0_chunking/salida_tanda0_r2; E0B=$X/e0_chunking/salida_tanda0_r2b
ENS=data/experiment/tanda0/code/ensamblar_tanda0.py
corre() {
  local n="$1" m="$2" e="$3" z="$4"; shift 4
  "$PY" -B $ENS --manifiesto "$m" --entrada "$e" --e0-r2 "$z" --salida "$OUT/$n" "$@" > "$OUT/consola_$n.txt" 2>&1
  echo "rc=$?" >> "$OUT/consola_$n.txt"
}
corre r2a_diez $MAN/tanda0_ens_diez.json $T/salida_dirigida $E0A --perfil-r2
corre r2a_desarrollo $MAN/tanda0_ens_desarrollo.json $T/salida_dirigida $E0A --perfil-r2
corre r2b_desarrollo $MAN/tanda0_ens_desarrollo_r2b.json $T/salida_r2b $E0B
corre r2b_sincola_desarrollo $MAN/tanda0_ens_desarrollo_r2b_sincola.json $T/salida_r2b $E0B --sin-cola
echo fin
