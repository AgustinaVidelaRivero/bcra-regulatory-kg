#!/bin/zsh
# B6.1, tanda final, T3, punto 4: las métricas intrínsecas de generación 3, informativas (laudo de la release r2, §3, punto 3), sobre los
# ocho grafos, con la E0 de cada grafo y, aparte, con la E0 con las partes por corte. Es data/experiment/tanda1/t3/scripts/intrinsecas_t3.sh
# con los ocho grafos. Sobre la copia; las E0 con las partes, dentro de la copia y con ruta relativa. USD 0, sin API.
# Uso: zsh intrinsecas_tf.sh <python> <copia> <E0 de la tanda final con partes> <E0 del 128 con partes> <E0 del 60 con partes> <dir de salida>
#        [<variante: e0_del_grafo | con_partes | ambas> [<nombre del grafo> ...]]   (sin variante, o «ambas», las dos, una detrás de
#        otra; con una, se pueden correr las dos a la par; con nombres, solo esos grafos)
#   El tramo 1 va con los manifiestos de la variante con la raya (decisión de la autora sobre el FRENO T3 parcial).
#   <dir de salida>: absoluto (el mkdir va antes del cd a la copia).
set -u
PY="$1"; C="$2"; PF="$3"; P128="$4"; P60="$5"; O="$6"; VARS="${7:-ambas}"; shift $(( $# < 7 ? $# : 7 )); SOLO=("$@")
[ "$VARS" = ambas ] && VARS="e0_del_grafo con_partes"
[[ "$O" = /* ]] || { print -r -- "FRENO: <dir de salida> tiene que ser absoluto"; exit 2; }
export PYTHONDONTWRITEBYTECODE=1; unset ANTHROPIC_API_KEY
X=data/experiment/reextraccion_v2; T=$X/corpus_tanda_final; A=data/experiment/tanda_final/t3/acumulado
M1=data/experiment/tanda_final/t1/ensamblado/manifiestos; MA=$A/manifiestos; MR=data/experiment/tanda_final/t3/prueba_raya_tramo1/manifiestos
corre() {  # <nombre> <kg> <e0> <manifiesto> <variante>
  (( ${#SOLO} == 0 )) || (( ${SOLO[(Ie)$1]} )) || return 0
  local d="$O/$5"; mkdir -p "$d"
  ( cd "$C" && "$PY" -B scripts/metricas_intrinsecas.py --gen3 --kg "$2" --nombre "$1" --e0 "$3" --manifiesto "$4" \
      --sha256-esperado "$(shasum -a 256 "$2" | cut -c1-64)" --out-dir "$d" > "$d/consola_$1.txt" 2>&1; print -r -- "rc=$?" >> "$d/consola_$1.txt" )
}
for v in ${=VARS}; do
  EF=$X/e0_chunking/salida_tanda_final_r2b; E128=$A/e0_acumulado_128_r2b; E60=$A/e0_acumulado_60_r2b
  [ "$v" = con_partes ] && { EF="$PF"; E128="$P128"; E60="$P60"; }
  corre KG-TandaFinal-r2b $T/ens_98_r2b/r2/kg.json "$EF" $M1/tanda_final_ens_98_r2b.json $v
  corre KG-TandaFinal-r2b-sincola $T/ens_98_r2b_sincola/r2/kg.json "$EF" $M1/tanda_final_ens_98_r2b_sincola.json $v
  corre KG-TandaFinal-Tramo1-r2b $T/ens_tramo1_r2b/r2/kg.json "$EF" $MR/tanda_final_ens_tramo1_r2b_raya.json $v
  corre KG-TandaFinal-Tramo1-r2b-sincola $T/ens_tramo1_r2b_sincola/r2/kg.json "$EF" $MR/tanda_final_ens_tramo1_r2b_raya_sincola.json $v
  corre KG-Acumulado-Tandas0y1yFinal-r2b $A/ens_128_r2b/r2/kg.json "$E128" $MA/tanda_final_acumulado_ens_128_r2b.json $v
  corre KG-Acumulado-Tandas0y1yFinal-r2b-sincola $A/ens_128_r2b_sincola/r2/kg.json "$E128" $MA/tanda_final_acumulado_ens_128_r2b_sincola.json $v
  corre KG-Acumulado-Tandas0y1yTramo1-r2b $A/ens_60_tramo1_r2b/r2/kg.json "$E60" $MA/tanda_final_acumulado_ens_60_tramo1_r2b.json $v
  corre KG-Acumulado-Tandas0y1yTramo1-r2b-sincola $A/ens_60_tramo1_r2b_sincola/r2/kg.json "$E60" $MA/tanda_final_acumulado_ens_60_tramo1_r2b_sincola.json $v
done
