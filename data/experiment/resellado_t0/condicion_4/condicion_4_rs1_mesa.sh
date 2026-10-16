#!/bin/zsh
# Mesa, §120: la condición 4 de la tanda 1 sobre una copia nueva del repo: la re-medición de la columna r2b del tablero de
# correcciones sobre los grafos re-sellados (diez y desarrollo, rs1) y las líneas de base de las vigilancias contables (4), (5), (8)
# y (9) sobre los cuatro re-sellados. Los pasos son los de U-REEXT-T0 (reext_t0/t5/comandos_t5.sh, bloque 1) con los grafos rs1.
# USD 0, sin API. Uso: zsh <este> <repo> <trabajo nuevo> <python del repo> <carpeta de los scripts de la mesa>
set -u
R="$1"; W="$2"; PY="$3"; M="$4"
[ ! -e "$W" ] || { echo "el trabajo ya existe"; exit 1; }
mkdir -p "$W"; C="$W/copia"; O="$W/salida"; mkdir -p "$O"
export PYTHONDONTWRITEBYTECODE=1; unset ANTHROPIC_API_KEY
paso() { print -r -- "$1 $(date '+%Y-%m-%d %H:%M:%S')" >> "$W/tiempos.txt"; }
paso "copia"
rsync -a --no-links --exclude=/.git --exclude=/.venv --exclude=/.venv-app --exclude=.DS_Store --exclude=__pycache__ \
  --exclude='.env' --exclude='.env.*' --exclude='*.env' --exclude='NO_ABRIR_*' --exclude=/data/experiment/neo4j/volumen "$R/" "$C/"
print -r -- "por nombre: $(find "$C" \( -name '.env' -o -name '.env.*' -o -name '*.env' -o -name 'NO_ABRIR_*' \) | wc -l | tr -d ' ') enlaces: $(find "$C" -type l | wc -l | tr -d ' ')" >> "$W/tiempos.txt"
cd "$C" || exit 2
X=data/experiment/reextraccion_v2; T=$X/corpus_tanda0; E0=$X/e0_chunking/salida_tanda0_r2b
paso "E0 con las partes"
"$PY" -B data/experiment/reext_t0/t3/e0_con_partes.py $E0 $T/salida_r2b "$O/e0_r2b_con_partes" > "$O/consola_e0_con_partes.txt" 2>&1
paso "M10"
for p in "diez:Diez" "desarrollo:Desarrollo"; do g=${p%%:*}; N=${p#*:}
  S=$(shasum -a 256 $T/ens_${g}_r2b_rs1/r2/kg.json | cut -c1-64)
  "$PY" -B scripts/metricas_intrinsecas.py --gen3 --kg $T/ens_${g}_r2b_rs1/r2/kg.json --nombre KG-Tanda0-$N-r2b-rs1 --e0 "$O/e0_r2b_con_partes" \
    --manifiesto $X/manifiestos/tanda0_ens_${g}_r2b_rs1.json --sha256-esperado $S --out-dir $T/ens_${g}_r2b_rs1/intrinsecas_gen3 > "$O/consola_intrinsecas_${g}.txt" 2>&1
  print -r -- "rc=$?" >> "$O/consola_intrinsecas_${g}.txt"
done
paso "medición rs1"
cp "$M/medicion_tablero_r2b_rs1_mesa.py" data/experiment/reext_t0/t3/medicion_tablero_r2b_rs1_mesa.py
"$PY" -B data/experiment/reext_t0/t3/medicion_tablero_r2b_rs1_mesa.py --out "$O/medicion_tablero_r2b_rs1.json" > "$O/consola_medicion_rs1.txt" 2>&1
print -r -- "rc=$?" >> "$O/consola_medicion_rs1.txt"
paso "vigilancias"
python3 -I -B "$M/vigilancias_contables_rs1_mesa.py" --salida $T/salida_r2b \
  --kg diez=$T/ens_diez_r2b_rs1/r2/kg.json --kg diez_sincola=$T/ens_diez_r2b_sincola_rs1/r2/kg.json \
  --kg desarrollo=$T/ens_desarrollo_r2b_rs1/r2/kg.json --kg desarrollo_sincola=$T/ens_desarrollo_r2b_sincola_rs1/r2/kg.json \
  --esperado diez=fda6c07dbb95602f5992f7e1ad9bf148ff1c2a72b9f69ff2ebbce891c15740ea \
  --esperado diez_sincola=61dd1b69ba03e40499845c40a6a8bec4c22d892ebe95823c7d5a569110f08738 \
  --esperado desarrollo=acb26dca0885e9ea83ab02637f15c1dac57885f0cf017c5fb16173ac7dfcac31 \
  --esperado desarrollo_sincola=66e745f57397ab754cde09eb641e9f0d9ef6259ea7e6445d086ecbf1c36dcc6c \
  --out "$O/vigilancias_contables_rs1.json" > "$O/consola_vigilancias.txt" 2>&1
print -r -- "rc=$?" >> "$O/consola_vigilancias.txt"
paso "fin"
