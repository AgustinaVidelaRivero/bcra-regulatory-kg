#!/bin/bash
# Re-sellado único de la tanda 0: una cadena de ensamblado sobre una copia del repo (nunca sobre el repo). USD 0, sin API.
# Uso: cadena_rs1.sh <python> <copia> <grafo> <salida> <consola>
#   <grafo>: r2b_diez | r2b_sincola_diez | r2b_desarrollo | r2b_sincola_desarrollo (manifiestos _rs1)
#            r2a_diez | r2a_desarrollo (manifiestos r2a de siempre, --perfil-r2, salida_dirigida y la E0 r2)
#   <salida>: el --salida del ensamblado; si es relativa, es relativa a la raíz de la copia.
set -u
PY="$1"; CP="$2"; G="$3"; OUT="$4"; CON="$5"
export PYTHONDONTWRITEBYTECODE=1; unset ANTHROPIC_API_KEY
cd "$CP" || exit 2
X=data/experiment/reextraccion_v2; T=$X/corpus_tanda0; MAN=$X/manifiestos
E0A=$X/e0_chunking/salida_tanda0_r2; E0B=$X/e0_chunking/salida_tanda0_r2b
ENS=data/experiment/tanda0/code/ensamblar_tanda0.py
case "$G" in
  r2b_diez)               set -- --manifiesto $MAN/tanda0_ens_diez_r2b_rs1.json --entrada $T/salida_r2b --e0-r2 $E0B ;;
  r2b_sincola_diez)       set -- --manifiesto $MAN/tanda0_ens_diez_r2b_sincola_rs1.json --entrada $T/salida_r2b --e0-r2 $E0B --sin-cola ;;
  r2b_desarrollo)         set -- --manifiesto $MAN/tanda0_ens_desarrollo_r2b_rs1.json --entrada $T/salida_r2b --e0-r2 $E0B ;;
  r2b_sincola_desarrollo) set -- --manifiesto $MAN/tanda0_ens_desarrollo_r2b_sincola_rs1.json --entrada $T/salida_r2b --e0-r2 $E0B --sin-cola ;;
  r2a_diez)               set -- --manifiesto $MAN/tanda0_ens_diez.json --entrada $T/salida_dirigida --e0-r2 $E0A --perfil-r2 ;;
  r2a_desarrollo)         set -- --manifiesto $MAN/tanda0_ens_desarrollo.json --entrada $T/salida_dirigida --e0-r2 $E0A --perfil-r2 ;;
  *) echo "grafo desconocido: $G"; exit 2 ;;
esac
{
  echo "inicio $(date '+%Y-%m-%d %H:%M:%S') grafo=$G"
  /usr/bin/time -l "$PY" -B $ENS "$@" --salida "$OUT"
  echo "rc=$?"
  echo "fin $(date '+%Y-%m-%d %H:%M:%S')"
} > "$CON" 2>&1
