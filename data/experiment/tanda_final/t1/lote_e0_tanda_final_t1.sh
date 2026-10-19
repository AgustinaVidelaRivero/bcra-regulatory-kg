#!/bin/zsh
# T1 de la tanda final de B6.1, punto 2.2: la E0 de los 98 TOs con el código del gate, sobre una copia (USD 0, sin API).
# Uso: zsh lote_e0_tanda_final_t1.sh <repo> <trabajo>
#   <repo>: la raíz del repo (solo se lee); <trabajo>: una carpeta nueva fuera del repo.
# Pasos (el modelo es tanda1/t1/lote_e0_tanda1_t1.sh, que sigue los pasos de s2/scripts/lote_tramo1_S2.sh; no se corre
# ese lote entero, porque su rsync no excluye las carpetas de la cláusula):
#   1. copia con la cláusula (copia_clausula_tanda_final_t1.sh) y sus controles por nombre y de enlaces;
#   2. raíz mínima con el código de E0 de la copia (s0_4/scripts/raiz_minima.sh) y sus tres sha256 contra S0-6b;
#   3. la corrida de los 152, una vez, y el control de S2 contra el manifiesto de S0-6b (768 de 768);
#   4. la corrida de los 98, dos veces, y el control adaptado (control_e0_tanda_final_t1.py e0);
#   5. el health-check de los 98 y su resumen, comparado con el de S2c.
# Los scripts de tanda_final/t1/ no van a la copia (la cláusula excluye tanda_final/): corren desde una copia suya en
# <trabajo>/scripts_t1/.
set -e
R="$1"; T="$2"
[ -e "$T" ] && { print -r -- "FRENO: $T ya existe"; exit 1; }
mkdir -p "$T/scripts_t1"
SEG="data/experiment/segmentacion_oficial_e0r2"
M_REL="$SEG/s0_6/b/manifiestos/manifest_salida_e0_152_S0-6b.json"
PY="$R/.venv/bin/python"
export PYTHONDONTWRITEBYTECODE=1
print -r -- "inicio $(date '+%Y-%m-%d %H:%M:%S')"
cp "$R/data/experiment/tanda_final/t1/control_e0_tanda_final_t1.py" "$R/data/experiment/tanda_final/t1/copia_clausula_tanda_final_t1.sh" "$T/scripts_t1/"
K="$T/scripts_t1"

zsh "$K/copia_clausula_tanda_final_t1.sh" "$R" "$T/copia"
C="$T/copia"
M="$C/$M_REL"
L="$C/$SEG/s2/cifras/tanda_final_S2c.json"
nl=$(zsh "$C/$SEG/s0_4/scripts/raiz_minima.sh" "$C" "$T/raiz" "$C/data/experiment/reextraccion_v2/e0_chunking")
print -r -- "raiz: enlaces=$(print -r -- $nl | tr -d ' ')"
RZ="$T/raiz"
"$PY" -B "$K/control_e0_tanda_final_t1.py" codigo --raiz "$RZ" --manifiesto "$M" --out "$T/control_codigo_raiz_t1.json"

print -r -- "inicio c152 $(date '+%Y-%m-%d %H:%M:%S')"
"$PY" -B "$C/$SEG/s0_1/scripts/correr_152.py" --codigo "$RZ" --salida "$T/e0_152" --workers 9
print -r -- "fin c152 $(date '+%Y-%m-%d %H:%M:%S')"
"$PY" -B "$C/$SEG/s2/scripts/control_e0_contra_manifiesto_S2.py" --e0 "$T/e0_152" --manifiesto "$M" \
  --out "$T/control_e0_152_t1.json"

TOS=$("$PY" -B -c "import json,sys; print(','.join(json.load(open(sys.argv[1]))['tanda_final']['lista']))" "$L")
for k in 1 2; do
  print -r -- "inicio c98_$k $(date '+%Y-%m-%d %H:%M:%S')"
  "$PY" -B "$C/$SEG/s0_1/scripts/correr_152.py" --codigo "$RZ" --salida "$T/e0_98_$k" --workers 9 --tos "$TOS"
  print -r -- "fin c98_$k $(date '+%Y-%m-%d %H:%M:%S')"
done
"$PY" -B "$K/control_e0_tanda_final_t1.py" e0 --e0 "$T/e0_98_1" --e0-bis "$T/e0_98_2" --e0-152 "$T/e0_152" \
  --manifiesto "$M" --manifiesto-s1ter "$C/$SEG/s1ter/manifiesto/segmentacion_oficial_e0r2_152.json" --lista "$L" \
  --pdfs "$R/data/experiment/escalado_prep/pdfs" --pdfs "$RZ/data/experiment/escalado_prep/pdfs" \
  --out "$T/control_e0_98_t1.json"

mkdir -p "$T/hc"
args=()
for t in ${(s:,:)TOS}; do args+=(--pdf "$RZ/data/experiment/escalado_prep/pdfs/$t.pdf"); done
"$PY" -B "$RZ/data/experiment/reextraccion_v2/e0_chunking/healthcheck_e0.py" "${args[@]}" \
  --salida "$T/hc/healthcheck_tanda_final_t1.json" > "$T/hc/stdout.txt"
"$PY" -B "$C/$SEG/s2/scripts/resumen_healthcheck_S2.py" --hc "$T/hc/healthcheck_tanda_final_t1.json" --e0 "$T/e0_98_1" \
  --manifiesto "$M" --out "$T/hc/resumen_healthcheck_tanda_final_t1.json" > /dev/null
"$PY" -B "$K/control_e0_tanda_final_t1.py" hc --resumen "$T/hc/resumen_healthcheck_tanda_final_t1.json" \
  --referencia "$C/$SEG/s2/cifras/resumen_healthcheck_tanda_final_S2c.json" --out "$T/hc/comparacion_resumen_hc_t1.json"
print -r -- "fin $(date '+%Y-%m-%d %H:%M:%S')"
