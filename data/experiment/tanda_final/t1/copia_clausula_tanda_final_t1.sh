#!/bin/zsh
# Copia del repo con la cláusula del despacho de T1 de la tanda final de B6.1 (sin .env, sin NO_ABRIR_, sin *_SOLO_MESA*,
# sin enlaces, sin data/experiment/tanda1/t4/, data/experiment/tanda1/t5/ ni data/experiment/tanda_final/), más
# data/experiment/tanda_final/preregistro/, que sí va a la copia porque la usan el lanzador y el control entre tramos.
# Uso: zsh copia_clausula_tanda_final_t1.sh <repo> <copia>
#   <repo>: la raíz del repo (solo se lee); <copia>: una carpeta nueva fuera del repo.
# Después de copiar y antes de correr nada: el control por nombre y el de enlaces, que tienen que dar 0. Si no, FRENO, con
# las rutas encontradas (sin abrirlas). La salida de rsync (los enlaces que saltea) va a <copia>.rsync.log, al lado de la
# copia, y no a la pantalla.
set -e
R="$1"; C="$2"
[ -e "$C" ] && { print -r -- "FRENO: $C ya existe"; exit 1; }
rsync -a --no-links --exclude=/.git --exclude=/.venv --exclude=/.venv-app --exclude=.DS_Store --exclude=__pycache__ \
  --exclude='.env' --exclude='.env.*' --exclude='*.env' --exclude='NO_ABRIR_*' --exclude='*_SOLO_MESA*' \
  --exclude=/data/experiment/tanda1/t4/ --exclude=/data/experiment/tanda1/t5/ --exclude=/data/experiment/tanda_final/ "$R/" "$C/" \
  > "$C.rsync.log" 2>&1
mkdir -p "$C/data/experiment/tanda_final"
rsync -a --no-links --exclude=.DS_Store --exclude=__pycache__ \
  --exclude='.env' --exclude='.env.*' --exclude='*.env' --exclude='NO_ABRIR_*' --exclude='*_SOLO_MESA*' \
  "$R/data/experiment/tanda_final/preregistro/" "$C/data/experiment/tanda_final/preregistro/" >> "$C.rsync.log" 2>&1
n=$(find "$C" \( -name '.env' -o -name '.env.*' -o -name '*.env' -o -name 'NO_ABRIR_*' -o -name '*_SOLO_MESA*' \) | wc -l | tr -d ' ')
l=$(find "$C" -type l | wc -l | tr -d ' ')
print -r -- "copia: env_no_abrir_solo_mesa=$n enlaces=$l"
if [ "$n" != "0" ] || [ "$l" != "0" ]; then
  find "$C" \( -name '.env' -o -name '.env.*' -o -name '*.env' -o -name 'NO_ABRIR_*' -o -name '*_SOLO_MESA*' -o -type l \) \
    | sed "s|$HOME|\$HOME|"
  print -r -- "FRENO: la copia trae $n archivos por nombre y $l enlaces"
  exit 1
fi
