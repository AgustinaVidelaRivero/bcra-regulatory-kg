#!/bin/zsh
# U-ALCANCE-E1, A3: reproducción desde cero (USD 0, sin API), con la foto sha256 del repo antes y después (CLAUDE.md §4.l). No
# escribe en el repo. Arma una copia nueva del repo con el rsync del despacho de A3, controla sus blobs contra la base, le
# aplica el parche del paquete (git apply sobre la copia, que no tiene .git) y corre bateria_a3.sh entera con el registro de
# lecturas (el hook de PYTHONPATH). Después compara, salida por salida, con la batería oficial: lo que va al repo y al
# paquete es lo que probó la batería, y el registro de lecturas no cambia ninguna salida.
# Uso: zsh reproduccion_a3.sh REPO TRABAJO_OFICIAL TRABAJO_NUEVO PARCHE HOOK
#   TRABAJO_OFICIAL: el de la batería oficial (med/bateria, e0t/ con la E0 regenerada); TRABAJO_NUEVO: carpeta nueva.
setopt pipefail
R="$1"; T0="$2"; T="$3"; P="$4"; HOOK="$5"; H="${0:A:h}"
BASE=5289b02f6457aabba5c4d15e50236cde240f2536
export PYTHONDONTWRITEBYTECODE=1; unset ANTHROPIC_API_KEY
rm -rf "$T"; mkdir -p "$T/med"
L="$T/med/reproduccion_a3.log"
log() { print -r -- "$*" | tee -a "$L"; }
cuenta_pyc() { find "$R" \( -path "$R/.git" -o -path "$R/.venv" -o -path "$R/.venv-app" \) -prune -o -name '*.pyc' -print | wc -l | tr -d ' '; }
cuenta_env() { find "$1" \( -name '.env' -o -name '.env.*' -o -name '*.env' -o -name 'NO_ABRIR_*' \) | wc -l | tr -d ' '; }
log "inicio $(date '+%Y-%m-%d %H:%M:%S %z'); HEAD $(git --no-optional-locks -C "$R" rev-parse HEAD)"
python3 -I -B "$H/foto_repo_a3.py" "$R" "$T/med/foto_repo_antes.json" | tee -a "$L"
log ".pyc antes: $(cuenta_pyc)"
rsync -a --no-links --exclude=/.git --exclude=/.venv --exclude=/.venv-app --exclude=.DS_Store --exclude=__pycache__ \
  --exclude='.env' --exclude='.env.*' --exclude='*.env' --exclude='NO_ABRIR_*' --exclude=/data/experiment/tanda1/t4/ \
  --exclude=/data/experiment/tanda1/t5/ "$R/" "$T/copia_head/" > "$T/med/rsync.log" 2>&1
log "rsync rc=$?; renglones de su salida: $(wc -l < "$T/med/rsync.log" | tr -d ' ') (enlaces salteados)"
n=$(cuenta_env "$T/copia_head")
log "control por nombre de la copia nueva (.env, .env.*, *.env, NO_ABRIR_*): $n; enlaces: $(find "$T/copia_head" -type l | wc -l | tr -d ' ')"
[ "$n" = "0" ] || { log "FRENO: $n archivos de entorno o NO_ABRIR_ en la copia"; exit 1; }
python3 -I -B "$H/blobs_contra_base_a3.py" "$R" $BASE "$T/copia_head" "$T/med/blobs_copia_nueva_contra_base.json" > /dev/null
log "blobs de la copia nueva contra la base rc=$? $(python3 -I -B -c "import json,sys; d=json.load(open(sys.argv[1])); print(d['comparados_iguales'], 'iguales | distintos o faltantes', [x[0] for x in d['distintos_o_faltantes']])" "$T/med/blobs_copia_nueva_contra_base.json")"
python3 -I -B "$H/pdfs_contra_manifiesto_a3.py" "$T/copia_head" "$T/med/pdfs_copia_nueva.json" > /dev/null; log "PDFs de la copia nueva rc=$?"
cp -cR "$T/copia_head" "$T/copia_a3"
(cd "$T/copia_a3" && git apply --check -p1 "$P" && git apply -p1 "$P"); log "git apply del parche del paquete sobre el clon rc=$? (parche $(shasum -a 256 "$P" | cut -d' ' -f1))"
for f in data/experiment/catalogo_unico/registro_alcance_r2b.json data/experiment/reextraccion_v2/e1_extractor/prompt_r2b.py \
         data/experiment/reextraccion_v2/e1_extractor/selftest_prompt_r2b.py data/experiment/mantenimiento/tabla_reprocesamiento.md; do
  if cmp -s "$T/copia_a3/$f" "$T0/copia_a3/$f"; then log "con el parche, igual a la copia de la batería oficial: $f"; else log "DISTINTO de la copia oficial: $f"; fi
done
mkdir -p "$T/e0t"; cp -cR "$T0/e0t/e0_152" "$T/e0t/e0_152"; cp "$T0/e0t/control_e0_S2a.json" "$T0/e0t/lista_tanda1_S2.json" "$T/e0t/"
log "la E0 regenerada de la batería oficial, clonada (cp -cR) en $T/e0t"
zsh "$H/bateria_a3.sh" "$R" "$T" "$T/med/bateria" "$T/lec/bateria" "$HOOK" > "$T/med/bateria_consola.txt" 2>&1; log "batería con el registro de lecturas rc=$?"
python3 -I -B "$H/comparar_corridas_a3.py" "$T0/med/bateria" "$T0" "$T/med/bateria" "$T" "$T/med/comparacion_con_la_oficial.json" | tee -a "$L"
log "lecturas anotadas: $(cat "$T/lec/bateria"/*.tsv | wc -l | tr -d ' ') aperturas en $(ls "$T/lec/bateria" | wc -l | tr -d ' ') procesos"
python3 -I -B "$H/foto_repo_a3.py" "$R" "$T/med/foto_repo_despues.json" | tee -a "$L"
log ".pyc después: $(cuenta_pyc)"
python3 -I -B "$H/foto_repo_a3.py" --comparar "$T/med/foto_repo_antes.json" "$T/med/foto_repo_despues.json" "$T/med/comparacion_foto_repo.json" | tee -a "$L"
log "fin $(date '+%Y-%m-%d %H:%M:%S %z')"
