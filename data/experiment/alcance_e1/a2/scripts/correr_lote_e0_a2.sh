#!/bin/zsh
# U-ALCANCE-E1, A2: la E0 corregida de los 152 regenerada con lote_tramo1_S2.sh de S2 de U-SEG-OFICIAL (USD 0, sin API),
# con la foto sha256 del repo antes y después (CLAUDE.md §4.l).
# Uso: zsh correr_lote_e0_a2.sh <repo> <trabajo> <scripts_a2>
# Antes de que el lote corra nada, siembra <trabajo>/copia con el rsync de los despachos y cuenta por nombre los .env y
# los NO_ABRIR_ (tiene que dar 0). El rsync del lote encuentra la copia al día y no la cambia; su control propio cuenta
# solo los .env, así que la cuenta completa se repite al final.
set -e
R="$1"; T="$2"; H="$3"
S2="data/experiment/segmentacion_oficial_e0r2/s2/scripts"
mkdir -p "$T"
L="$T/lote_a2.log"
log() { print -r -- "$*" | tee -a "$L"; }
cuenta() { find "$1" \( -name '.env' -o -name '.env.*' -o -name '*.env' -o -name 'NO_ABRIR_*' \) | wc -l | tr -d ' '; }
log "inicio $(date '+%Y-%m-%d %H:%M:%S %z'); HEAD $(git -C "$R" rev-parse HEAD)"
python3 -I -B "$H/foto_repo_a2.py" "$R" "$T/foto_repo_antes_lote.json" | tee -a "$L"
rsync -a --no-links --exclude=/.git --exclude=/.venv --exclude=/.venv-app --exclude=.DS_Store --exclude=__pycache__ \
  --exclude='.env' --exclude='.env.*' --exclude='*.env' --exclude='NO_ABRIR_*' "$R/" "$T/copia/" > "$T/rsync_siembra.log" 2>&1
n=$(cuenta "$T/copia")
log "control por nombre tras la siembra (.env, .env.*, *.env, NO_ABRIR_*): $n"
[ "$n" = "0" ] || { log "FRENO: $n archivos de entorno o NO_ABRIR_ en la copia"; exit 1; }
log "lote_tramo1_S2.sh (de la copia), $(shasum -a 256 "$T/copia/$S2/lote_tramo1_S2.sh" | cut -d' ' -f1)"
zsh "$T/copia/$S2/lote_tramo1_S2.sh" "$R" "$T" 2>&1 | tee -a "$L"
log "lote rc=${pipestatus[1]}"
log "control por nombre al final: copia $(cuenta "$T/copia"), raíz mínima $(cuenta "$T/raiz"), salida $(cuenta "$T/e0_152")"
log "enlaces simbólicos: copia $(find "$T/copia" -type l | wc -l | tr -d ' '), raíz mínima $(find "$T/raiz" -type l | wc -l | tr -d ' ')"
python3 -I -B "$H/foto_repo_a2.py" "$R" "$T/foto_repo_despues_lote.json" | tee -a "$L"
python3 -I -B "$H/foto_repo_a2.py" --comparar "$T/foto_repo_antes_lote.json" "$T/foto_repo_despues_lote.json" \
  "$T/comparacion_foto_lote.json" | tee -a "$L"
log "fin $(date '+%Y-%m-%d %H:%M:%S %z')"
