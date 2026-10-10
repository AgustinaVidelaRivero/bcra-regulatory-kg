#!/bin/bash
# Las cuatro cadenas r2b (diez y desarrollo, con y sin cola) sobre una copia. Uso: cadenas_r2b_cuatro.sh <python> <copia> <salida>
set -u
PY="$1"; CP="$2"; OUT="$3"
export PYTHONDONTWRITEBYTECODE=1; unset ANTHROPIC_API_KEY
cd "$CP" || exit 2
X=data/experiment/reextraccion_v2; T=$X/corpus_tanda0; MAN=$X/manifiestos; E0B=$X/e0_chunking/salida_tanda0_r2b
ENS=data/experiment/tanda0/code/ensamblar_tanda0.py
corre() { local n="$1" m="$2"; shift 2; "$PY" -B $ENS --manifiesto "$m" --entrada $T/salida_r2b --e0-r2 $E0B --salida "$OUT/$n" "$@" > "$OUT/consola_$n.txt" 2>&1; echo "rc=$?" >> "$OUT/consola_$n.txt"; }
corre r2b_diez $MAN/tanda0_ens_diez_r2b.json
corre r2b_sincola_diez $MAN/tanda0_ens_diez_r2b_sincola.json --sin-cola
corre r2b_desarrollo $MAN/tanda0_ens_desarrollo_r2b.json
corre r2b_sincola_desarrollo $MAN/tanda0_ens_desarrollo_r2b_sincola.json --sin-cola
echo fin
