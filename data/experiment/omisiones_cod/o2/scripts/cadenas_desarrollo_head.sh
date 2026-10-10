#!/bin/bash
# Cadenas r2b de desarrollo (con y sin cola) con el código de HEAD, sobre la copia. Uso: cadenas_desarrollo_head.sh <python> <copia> <salida>
set -u
PY="$1"; CP="$2"; OUT="$3"
export PYTHONDONTWRITEBYTECODE=1; unset ANTHROPIC_API_KEY
cd "$CP" || exit 2
X=data/experiment/reextraccion_v2; T=$X/corpus_tanda0; MAN=$X/manifiestos; E0B=$X/e0_chunking/salida_tanda0_r2b
ENS=data/experiment/tanda0/code/ensamblar_tanda0.py
"$PY" -B $ENS --manifiesto $MAN/tanda0_ens_desarrollo_r2b.json --entrada $T/salida_r2b --e0-r2 $E0B --salida "$OUT/r2b_desarrollo" > "$OUT/consola_r2b_desarrollo.txt" 2>&1; echo "rc=$?" >> "$OUT/consola_r2b_desarrollo.txt" &
"$PY" -B $ENS --manifiesto $MAN/tanda0_ens_desarrollo_r2b_sincola.json --entrada $T/salida_r2b --e0-r2 $E0B --sin-cola --salida "$OUT/r2b_sincola_desarrollo" > "$OUT/consola_r2b_sincola_desarrollo.txt" 2>&1; echo "rc=$?" >> "$OUT/consola_r2b_sincola_desarrollo.txt" &
wait
echo fin
