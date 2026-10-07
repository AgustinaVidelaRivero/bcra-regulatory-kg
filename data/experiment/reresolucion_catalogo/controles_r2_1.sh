#!/bin/bash
# U-RERESOL-CAT, R2-1 — controles de reproducción del código nuevo (W1 a W3) sin parámetros (decisiones 3 y 4 del
# despacho de R2): las cadenas r2a, los r2b sellados sin la bandera y los dos sin cola con la bandera, byte a byte; la
# cadena con --catalogo-resolucion y el catálogo sin ampliaciones (con y sin la bandera); y la suite sobre las entradas
# selladas. USD 0. Se corre desde la raíz de una COPIA del repo, nunca sobre el repo (CLAUDE.md §4.k y §4.l).
# Uso: controles_r2_1.sh <python> <dir de salida relativo a la copia> <fase: suite|cadenas|catalogo_vacio> [viejo|nuevo]
#   suite viejo|nuevo  la suite sobre las seis entradas selladas (diez y desarrollo; r2a, r2b y r2b sin cola), con el
#                      código que haya en la copia: se corre una vez con el de HEAD y otra con el nuevo, y se comparan.
#   cadenas            las seis cadenas por la línea de comando, sin --catalogo-resolucion.
#   catalogo_vacio     r2b diez con --catalogo-resolucion <generados sin ampliaciones>, sin y con --sin-cola.
set -u
PY="$1"; OUT="$2"; FASE="$3"; COD="${4:-nuevo}"
export PYTHONDONTWRITEBYTECODE=1; unset ANTHROPIC_API_KEY
X=data/experiment/reextraccion_v2; T=$X/corpus_tanda0; MAN=$X/manifiestos
E0A=$X/e0_chunking/salida_tanda0_r2; E0B=$X/e0_chunking/salida_tanda0_r2b
ENS=data/experiment/tanda0/code/ensamblar_tanda0.py
SUITE=(scripts/regression_kg.py --perfil r2 --generacion 3 --catalogo data/experiment/catalogo_unico/generados_r2/catalogo_suite_r2.json
       --politica-cuarentena flaggeada --esperado scripts/regression_kg_esperado.json)
mkdir -p "$OUT"
case "$FASE" in
suite)
  for g in diez desarrollo; do
    for v in r2a r2b r2b_sincola; do
      "$PY" -B "${SUITE[@]}" --kg $T/ens_${g}_${v}/r2/kg.json --registro-dir $T/ens_${g}_${v}/r2 \
        --out "$OUT/suite_${COD}_${g}_${v}.md" > "$OUT/consola_suite_${COD}_${g}_${v}.txt" 2>&1
      echo "rc=$?" >> "$OUT/consola_suite_${COD}_${g}_${v}.txt"
    done
  done ;;
cadenas)
  corre() {  # nombre, manifiesto, entrada, e0, extra...
    local n="$1" m="$2" e="$3" z="$4"; shift 4
    "$PY" -B $ENS --manifiesto "$m" --entrada "$e" --e0-r2 "$z" --salida "$OUT/$n" "$@" > "$OUT/consola_$n.txt" 2>&1
    echo "rc=$?" >> "$OUT/consola_$n.txt"
  }
  corre r2a_diez $MAN/tanda0_ens_diez.json $T/salida_dirigida $E0A --perfil-r2 &
  corre r2a_desarrollo $MAN/tanda0_ens_desarrollo.json $T/salida_dirigida $E0A --perfil-r2 &
  corre r2b_diez $MAN/tanda0_ens_diez_r2b.json $T/salida_r2b $E0B &
  wait
  corre r2b_desarrollo $MAN/tanda0_ens_desarrollo_r2b.json $T/salida_r2b $E0B &
  corre r2b_sincola_diez $MAN/tanda0_ens_diez_r2b_sincola.json $T/salida_r2b $E0B --sin-cola &
  corre r2b_sincola_desarrollo $MAN/tanda0_ens_desarrollo_r2b_sincola.json $T/salida_r2b $E0B --sin-cola &
  wait ;;
catalogo_vacio)
  G="$COD"
  "$PY" -B $ENS --manifiesto $MAN/tanda0_ens_diez_r2b.json --entrada $T/salida_r2b --e0-r2 $E0B \
    --catalogo-resolucion "$G" --salida "$OUT/vacio_r2b_diez" > "$OUT/consola_vacio_r2b_diez.txt" 2>&1 &
  "$PY" -B $ENS --manifiesto $MAN/tanda0_ens_diez_r2b_sincola.json --entrada $T/salida_r2b --e0-r2 $E0B \
    --catalogo-resolucion "$G" --sin-cola --salida "$OUT/vacio_r2b_sincola_diez" > "$OUT/consola_vacio_r2b_sincola_diez.txt" 2>&1 &
  wait ;;
esac
echo "fin $FASE $COD"
