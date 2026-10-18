#!/bin/zsh
# U-ALCANCE-E1, A3: la E0 corregida de los 152 regenerada con los pasos de lote_tramo1_S2.sh de S2 de U-SEG-OFICIAL, el lote
# de A2 (USD 0, sin API), con la foto sha256 del repo antes y después (CLAUDE.md §4.l).
# Uso: zsh correr_lote_e0_a3.sh <repo> <copia_controlada> <trabajo> <scripts_a3> [<registro de lecturas> <carpeta del hook>]
#
# Una sola diferencia con correr_lote_e0_a2.sh: el renglón 11 de lote_tramo1_S2.sh siembra <trabajo>/copia con un rsync que
# toma el repo y no excluye data/experiment/tanda1/t4/ ni t5/, donde T4 y T5 de la tanda 1 escriben mientras A3 corre (la
# precisión de la autora del 18/10/2026 a la condición 1 del mandato de A3). Acá <trabajo>/copia es un clon (cp -cR: copia,
# no enlace) de <copia_controlada>, la copia del rsync del despacho cuyos blobs se controlaron contra la base; los renglones
# 13 a 24 del lote corren tal cual, con el código de E0 y los scripts de esa copia. El resultado se controla igual que en
# A2: contra el manifiesto de S0-6b (control_e0_contra_manifiesto_S2.py) y con la lista regenerada.
set -e
setopt pipefail   # que un paso que falla frene aunque su salida vaya por tee
R="$1"; C="$2"; T="$3"; H="$4"; LEC="$5"; HOOK="$6"
S2="data/experiment/segmentacion_oficial_e0r2/s2/scripts"
PY="$R/.venv/bin/python"
mkdir -p "$T"
L="$T/lote_a3.log"
log() { print -r -- "$*" | tee -a "$L"; }
cuenta() { find "$1" \( -name '.env' -o -name '.env.*' -o -name '*.env' -o -name 'NO_ABRIR_*' \) | wc -l | tr -d ' '; }
log "inicio $(date '+%Y-%m-%d %H:%M:%S %z'); HEAD $(git --no-optional-locks -C "$R" rev-parse HEAD)"
python3 -I -B "$H/foto_repo_a3.py" "$R" "$T/foto_repo_antes_lote.json" | tee -a "$L"
rm -rf "$T/copia"; cp -cR "$C" "$T/copia"
n=$(cuenta "$T/copia")
log "control por nombre del clon (.env, .env.*, *.env, NO_ABRIR_*): $n; enlaces: $(find "$T/copia" -type l | wc -l | tr -d ' ')"
[ "$n" = "0" ] || { log "FRENO: $n archivos de entorno o NO_ABRIR_ en la copia"; exit 1; }
log "lote_tramo1_S2.sh (de la copia), $(shasum -a 256 "$T/copia/$S2/lote_tramo1_S2.sh" | cut -d' ' -f1); renglones 13 a 24, tal cual:"
sed -n '13,24p' "$T/copia/$S2/lote_tramo1_S2.sh" | sed 's/^/   | /' | tee -a "$L"
if [ -n "$LEC" ]; then mkdir -p "$LEC"; export A3_LOG_LECTURAS="$LEC" PYTHONPATH="$HOOK"; fi
# --- renglones 13 a 24 de lote_tramo1_S2.sh, con R := la copia controlada (solo para el rsync, que acá es el clon) ---
n=$(find "$T/copia" \( -name '.env' -o -name '.env.*' -o -name '*.env' \) | wc -l | tr -d ' ')
[ "$n" = "0" ] || { print -r -- "FRENO: $n .env en la copia"; exit 1; }
zsh "$T/copia/data/experiment/segmentacion_oficial_e0r2/s0_4/scripts/raiz_minima.sh" "$T/copia" "$T/raiz" \
  "$T/copia/data/experiment/reextraccion_v2/e0_chunking" | tee -a "$L"
export PYTHONDONTWRITEBYTECODE=1
"$PY" -B "$T/copia/data/experiment/segmentacion_oficial_e0r2/s0_1/scripts/correr_152.py" --codigo "$T/raiz" \
  --salida "$T/e0_152" --workers 8 2>&1 | tee -a "$L"
"$PY" -B "$T/copia/$S2/control_e0_contra_manifiesto_S2.py" --e0 "$T/e0_152" \
  --manifiesto "$T/copia/data/experiment/segmentacion_oficial_e0r2/s0_6/b/manifiestos/manifest_salida_e0_152_S0-6b.json" \
  --out "$T/control_e0_S2a.json" 2>&1 | tail -5 | tee -a "$L"
"$PY" -B "$T/copia/$S2/lista_tanda1_S2.py" --e0 "$T/e0_152" --raiz "$T/copia" --out "$T/lista_tanda1_S2.json" 2>&1 | tail -5 | tee -a "$L"
# --- fin de los renglones del lote ---
unset A3_LOG_LECTURAS PYTHONPATH
log "control por nombre al final: copia $(cuenta "$T/copia"), raíz mínima $(cuenta "$T/raiz"), salida $(cuenta "$T/e0_152")"
log "enlaces simbólicos: copia $(find "$T/copia" -type l | wc -l | tr -d ' '), raíz mínima $(find "$T/raiz" -type l | wc -l | tr -d ' ')"
python3 -I -B "$H/foto_repo_a3.py" "$R" "$T/foto_repo_despues_lote.json" | tee -a "$L"
python3 -I -B "$H/foto_repo_a3.py" --comparar "$T/foto_repo_antes_lote.json" "$T/foto_repo_despues_lote.json" \
  "$T/comparacion_foto_lote.json" | tee -a "$L"
log "fin $(date '+%Y-%m-%d %H:%M:%S %z')"
