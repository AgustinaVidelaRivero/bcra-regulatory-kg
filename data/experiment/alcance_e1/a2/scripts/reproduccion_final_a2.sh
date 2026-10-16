#!/bin/zsh
# U-ALCANCE-E1, A2: reproducción desde cero sobre una copia nueva del repo, después de escribir en él las escrituras de A2
# (USD 0, sin API), con la foto sha256 del repo antes y después (CLAUDE.md §4.l). Controla que lo que quedó en el repo es
# lo que probó la batería: el derivado se regenera igual, el candado coincide, los selftests dan lo mismo, el JSON de
# selftest_clave_cache sale igual al del repo y los mensajes de la corrida en seco son, byte a byte, los de la batería.
# Uso: zsh reproduccion_final_a2.sh REPO TRABAJO (TRABAJO con med/bateria y e0t/e0_152 de la batería)
R="$1"; T="$2"; PY="$R/.venv/bin/python"; H="${0:A:h}"; M="$T/med/reproduccion"; C="$T/repro/copia"
export PYTHONDONTWRITEBYTECODE=1; unset ANTHROPIC_API_KEY
rm -rf "$M" "$T/repro"; mkdir -p "$M" "$T/repro"
log() { print -r -- "$*" | tee -a "$M/reproduccion.log"; }
igual() { if cmp -s "$1" "$2"; then log "$3: iguales byte a byte"; else log "$3: DISTINTOS"; fi; }
cuenta_pyc() { find "$R" \( -path "$R/.git" -o -path "$R/.venv" \) -prune -o -name '*.pyc' -print | wc -l | tr -d ' '; }
E1="data/experiment/reextraccion_v2/e1_extractor"
LISTA="data/experiment/segmentacion_oficial_e0r2/s2/lista_tanda1_S2.json"
log "inicio $(date '+%Y-%m-%d %H:%M:%S %z'); HEAD $(git -C "$R" rev-parse HEAD)"
python3 -I -B "$H/foto_repo_a2.py" "$R" "$M/foto_repo_antes.json" | tee -a "$M/reproduccion.log"
log ".pyc antes: $(cuenta_pyc)"
rsync -a --no-links --exclude=/.git --exclude=/.venv --exclude=/.venv-app --exclude=.DS_Store --exclude=__pycache__ \
  --exclude='.env' --exclude='.env.*' --exclude='*.env' --exclude='NO_ABRIR_*' "$R/" "$C/" > "$M/rsync.log" 2>&1
n=$(find "$C" \( -name '.env' -o -name '.env.*' -o -name '*.env' -o -name 'NO_ABRIR_*' \) | wc -l | tr -d ' ')
log "control por nombre de la copia nueva (.env, .env.*, *.env, NO_ABRIR_*): $n"
[ "$n" = "0" ] || { log "FRENO: $n archivos de entorno o NO_ABRIR_ en la copia"; exit 1; }
log "enlaces simbólicos en la copia: $(find "$C" -type l | wc -l | tr -d ' ')"

(cd "$C" && "$PY" -B data/experiment/catalogo_unico/code/derivar_registro_alcance_r2b.py --tandas 1 --salida - > "$M/derivado.json"); log "derivado rc=$?"
igual "$M/derivado.json" "$R/data/experiment/catalogo_unico/registro_alcance_r2b.json" "derivado regenerado y el del repo"
"$PY" -B "$H/sellar_a2.py" --raiz "$C" --salida "$M/sellos" --verificar > /dev/null; log "verificación del candado rc=$?"
log "$(python3 -I -c "import json,sys; d=json.load(open(sys.argv[1])); print('coinciden', d['coinciden'], '| unidades de la fixture', d['unidades_de_la_fixture'])" "$M/sellos/verificacion_sellos_a2.json")"
(cd "$C" && "$PY" -B $E1/selftest_prompt_r2b.py > "$M/selftest_prompt_r2b.txt" 2>&1); log "selftest_prompt_r2b rc=$? $(tail -1 "$M/selftest_prompt_r2b.txt")"
igual "$M/selftest_prompt_r2b.txt" "$T/med/bateria/selftest_prompt_r2b_a2.txt" "consola de selftest_prompt_r2b y la de la batería"
(cd "$C" && "$PY" -B data/experiment/mantenimiento/code/selftest_clave_cache.py --salida-r2b data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b --out "$M/selftest_clave_cache.json" > "$M/consola_clave_cache.txt" 2>&1); log "selftest_clave_cache rc=$? $(tail -1 "$M/consola_clave_cache.txt")"
igual "$M/selftest_clave_cache.json" "$R/data/experiment/mantenimiento/selftest_clave_cache.json" "selftest_clave_cache y el JSON del repo"
(cd "$C" && GIT_DIR="$R/.git" GIT_OPTIONAL_LOCKS=0 "$PY" -B data/experiment/catalogo_unico/code/selftest_catalogo_unico.py > "$M/selftest_catalogo_unico.txt" 2>&1); log "selftest_catalogo_unico rc=$? $(tail -1 "$M/selftest_catalogo_unico.txt")"
"$PY" -B "$H/mensajes_runner_a2.py" --raiz "$C" --e0-tanda1 "$T/e0t/e0_152" --lista "$C/$LISTA" --salida "$M/seco" --etiqueta a2 > /dev/null; log "corrida en seco rc=$?"
igual "$M/seco/mensajes_a2.jsonl" "$T/med/bateria/seco/mensajes_a2.jsonl" "mensajes de la corrida en seco y los de la batería"
igual "$M/seco/resumen_a2.json" "$T/med/bateria/seco/resumen_a2.json" "resumen de la corrida en seco y el de la batería"

python3 -I -B "$H/foto_repo_a2.py" "$R" "$M/foto_repo_despues.json" | tee -a "$M/reproduccion.log"
log ".pyc después: $(cuenta_pyc)"
python3 -I -B "$H/foto_repo_a2.py" --comparar "$M/foto_repo_antes.json" "$M/foto_repo_despues.json" "$M/comparacion_foto_repo.json" | tee -a "$M/reproduccion.log"
log "fin $(date '+%Y-%m-%d %H:%M:%S %z')"
