#!/bin/zsh
# B6.1, tanda 1, T3, punto 4: las métricas intrínsecas de generación 3, informativas (laudo de la release r2, §3, punto 3), sobre los
# cuatro grafos nuevos, con la E0 de cada grafo (como el gate final del laudo, gate_final_laudo_r2_mesa.sh:52-56) y, aparte, con la E0
# con las partes por corte (como U-REEXT-T0 T3, reext_t0/t3/e0_con_partes.py). Sobre la copia. USD 0, sin API.
# Uso: zsh intrinsecas_t3.sh <python> <copia> <E0 tanda 1 con partes> <E0 acumulado con partes> <dir de salida>
set -u
PY="$1"; C="$2"; P1="$3"; PA="$4"; O="$5"
export PYTHONDONTWRITEBYTECODE=1; unset ANTHROPIC_API_KEY
X=data/experiment/reextraccion_v2; A=data/experiment/tanda1/t3/acumulado; MAN=$X/manifiestos
corre() {  # <nombre> <kg> <e0> <manifiesto> <variante>
  local d="$O/$5"; mkdir -p "$d"
  ( cd "$C" && "$PY" -B scripts/metricas_intrinsecas.py --gen3 --kg "$2" --nombre "$1" --e0 "$3" --manifiesto "$4" \
      --sha256-esperado "$(shasum -a 256 "$2" | cut -c1-64)" --out-dir "$d" > "$d/consola_$1.txt" 2>&1; print -r -- "rc=$?" >> "$d/consola_$1.txt" )
}
for v in e0_del_grafo con_partes; do
  E1=$X/e0_chunking/salida_tanda1_r2b; EA=$A/e0_acumulado_r2b
  [ "$v" = con_partes ] && { E1="$P1"; EA="$PA"; }
  corre KG-Tanda1-Veinte-r2b $X/corpus_tanda1/ens_veinte_r2b/r2/kg.json "$E1" $MAN/tanda1_ens_veinte_r2b.json $v
  corre KG-Tanda1-Veinte-r2b-sincola $X/corpus_tanda1/ens_veinte_r2b_sincola/r2/kg.json "$E1" $MAN/tanda1_ens_veinte_r2b_sincola.json $v
  corre KG-Acumulado-Tandas0y1-r2b $A/ens_treinta_r2b/r2/kg.json "$EA" $A/manifiestos/acumulado_ens_treinta_r2b.json $v
  corre KG-Acumulado-Tandas0y1-r2b-sincola $A/ens_treinta_r2b_sincola/r2/kg.json "$EA" $A/manifiestos/acumulado_ens_treinta_r2b_sincola.json $v
done
