#!/bin/zsh
# Mesa §131: la E0 de los 152 con el código del gate, sobre una copia con la cláusula (sin bases), para medir la tanda final.
set -e
R="$1"; T="$2"
PY="$R/.venv/bin/python"; export PYTHONDONTWRITEBYTECODE=1
SEG=data/experiment/segmentacion_oficial_e0r2
rm -rf "$T"; mkdir -p "$T"
date '+copia %H:%M:%S'
rsync -a --no-links --exclude=/.git --exclude=/.venv --exclude=/.venv-app --exclude=.DS_Store --exclude=__pycache__ \
  --exclude='.env' --exclude='.env.*' --exclude='*.env' --exclude='NO_ABRIR_*' --exclude=/data/experiment/neo4j/volumen \
  --exclude='*.db' --exclude='*.db-wal' --exclude='*.db-shm' "$R/" "$T/copia/" 2>/dev/null || true
echo "nombres vedados en la copia: $(find "$T/copia" \( -name '.env' -o -name '.env.*' -o -name '*.env' -o -name 'NO_ABRIR_*' \) | wc -l | tr -d ' ')"
echo "enlaces en la copia: $(find "$T/copia" -type l | wc -l | tr -d ' ')"
C="$T/copia"
echo "enlaces en la raíz: $(zsh "$C/$SEG/s0_4/scripts/raiz_minima.sh" "$C" "$T/raiz" "$C/data/experiment/reextraccion_v2/e0_chunking" | tr -d ' ')"
date '+152 %H:%M:%S'
"$PY" -B "$C/$SEG/s0_1/scripts/correr_152.py" --codigo "$T/raiz" --salida "$T/e0_152" --workers 9 > "$T/e0_152.log" 2>&1
tail -1 "$T/e0_152.log"
date '+fin %H:%M:%S'
