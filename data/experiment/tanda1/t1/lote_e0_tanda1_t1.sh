#!/bin/zsh
# T1 de la tanda 1 de B6.1, punto 2.2: la E0 de los 20 TOs con el código del gate, sobre una copia (USD 0, sin API).
# Uso: zsh lote_e0_tanda1_t1.sh <repo> <trabajo>
#   <repo>: la raíz del repo (solo se lee); <trabajo>: una carpeta nueva fuera del repo.
# Pasos (el modelo es s2/scripts/lote_tramo1_S2.sh y lote_cifras_S2b.sh:20-21):
#   1. copia sin .env ni NO_ABRIR_ (la cláusula del despacho) y control por nombre y de enlaces;
#   2. raíz mínima con el código de E0 de la copia (s0_4/scripts/raiz_minima.sh) y sus tres sha256 contra S0-6b;
#   3. la corrida de los 152, una vez, y el control de S2 contra el manifiesto de S0-6b (768 de 768);
#   4. la corrida de los 20, dos veces, y el control adaptado (control_e0_tanda1_t1.py e0);
#   5. el health-check de los 20 y su resumen, comparado con el de S2b.
set -e
R="$1"; T="$2"
[ -e "$T" ] && { print -r -- "FRENO: $T ya existe"; exit 1; }
mkdir -p "$T"
SEG="data/experiment/segmentacion_oficial_e0r2"
M_REL="$SEG/s0_6/b/manifiestos/manifest_salida_e0_152_S0-6b.json"
PY="$R/.venv/bin/python"
export PYTHONDONTWRITEBYTECODE=1
print -r -- "inicio $(date '+%Y-%m-%d %H:%M:%S')"

rsync -a --no-links --exclude=/.git --exclude=/.venv --exclude=/.venv-app --exclude=.DS_Store --exclude=__pycache__ \
  --exclude='.env' --exclude='.env.*' --exclude='*.env' --exclude='NO_ABRIR_*' "$R/" "$T/copia/" > "$T/rsync.log" 2>&1
C="$T/copia"
n=$(find "$C" \( -name '.env' -o -name '.env.*' -o -name '*.env' -o -name 'NO_ABRIR_*' \) | wc -l | tr -d ' ')
l=$(find "$C" -type l | wc -l | tr -d ' ')
print -r -- "copia: env_y_no_abrir=$n enlaces=$l"
[ "$n" = "0" ] && [ "$l" = "0" ] || { print -r -- "FRENO: la copia trae $n .env o NO_ABRIR_ y $l enlaces"; exit 1; }

M="$C/$M_REL"
K="$C/data/experiment/tanda1/t1"
L="$C/$SEG/s2/lista_tanda1_S2.json"
nl=$(zsh "$C/$SEG/s0_4/scripts/raiz_minima.sh" "$C" "$T/raiz" "$C/data/experiment/reextraccion_v2/e0_chunking")
print -r -- "raiz: enlaces=$(print -r -- $nl | tr -d ' ')"
RZ="$T/raiz"
"$PY" -B "$K/control_e0_tanda1_t1.py" codigo --raiz "$RZ" --manifiesto "$M" --out "$T/control_codigo_raiz_t1.json"

print -r -- "inicio c152 $(date '+%Y-%m-%d %H:%M:%S')"
"$PY" -B "$C/$SEG/s0_1/scripts/correr_152.py" --codigo "$RZ" --salida "$T/e0_152" --workers 9
print -r -- "fin c152 $(date '+%Y-%m-%d %H:%M:%S')"
"$PY" -B "$C/$SEG/s2/scripts/control_e0_contra_manifiesto_S2.py" --e0 "$T/e0_152" --manifiesto "$M" \
  --out "$T/control_e0_152_t1.json"

TOS=$("$PY" -B -c "import json,sys; print(','.join(f['to'] for f in json.load(open(sys.argv[1]))['filas']))" "$L")
for k in 1 2; do
  print -r -- "inicio c20_$k $(date '+%Y-%m-%d %H:%M:%S')"
  "$PY" -B "$C/$SEG/s0_1/scripts/correr_152.py" --codigo "$RZ" --salida "$T/e0_20_$k" --workers 9 --tos "$TOS"
  print -r -- "fin c20_$k $(date '+%Y-%m-%d %H:%M:%S')"
done
"$PY" -B "$K/control_e0_tanda1_t1.py" e0 --e0 "$T/e0_20_1" --e0-bis "$T/e0_20_2" --e0-152 "$T/e0_152" \
  --manifiesto "$M" --manifiesto-s1ter "$C/$SEG/s1ter/manifiesto/segmentacion_oficial_e0r2_152.json" --lista "$L" \
  --pdfs "$R/data/experiment/escalado_prep/pdfs" --pdfs "$RZ/data/experiment/escalado_prep/pdfs" \
  --out "$T/control_e0_20_t1.json"

mkdir -p "$T/hc"
args=()
for t in ${(s:,:)TOS}; do args+=(--pdf "$RZ/data/experiment/escalado_prep/pdfs/$t.pdf"); done
"$PY" -B "$RZ/data/experiment/reextraccion_v2/e0_chunking/healthcheck_e0.py" "${args[@]}" \
  --salida "$T/hc/healthcheck_tanda1_t1.json" > "$T/hc/stdout.txt"
"$PY" -B "$C/$SEG/s2/scripts/resumen_healthcheck_S2.py" --hc "$T/hc/healthcheck_tanda1_t1.json" --e0 "$T/e0_20_1" \
  --manifiesto "$M" --out "$T/hc/resumen_healthcheck_tanda1_t1.json" > /dev/null
"$PY" -B "$K/control_e0_tanda1_t1.py" hc --resumen "$T/hc/resumen_healthcheck_tanda1_t1.json" \
  --referencia "$C/$SEG/s2/cifras/resumen_healthcheck_tanda1_S2b.json" --out "$T/hc/comparacion_resumen_hc_t1.json"
print -r -- "fin $(date '+%Y-%m-%d %H:%M:%S')"
