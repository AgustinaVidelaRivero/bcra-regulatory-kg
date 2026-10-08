#!/usr/bin/env bash
# U-ALCANCE-E1, A1: batería de controles sobre copias sin enlaces (USD 0, sin API), con la foto sha256 del repo antes y
# después (CLAUDE.md §4.l). Uso: bash bateria_a1.sh REPO TRABAJO, con TRABAJO fuera del repo y armado así:
#   rsync -a --copy-links --exclude='.git' --exclude='.venv' REPO/ TRABAJO/copia/
#   python3 -I -B foto_repo.py TRABAJO/copia TRABAJO/foto_copia_inicial.txt
#   cp -cR TRABAJO/copia TRABAJO/copia_head                  (clon APFS: copia, no enlace)
#   cd TRABAJO/copia && git apply REPO/data/experiment/alcance_e1/parche_UALCANCE_E1_A1.diff
# Los scripts se toman del directorio de este archivo; la salida va a TRABAJO/med/bateria.
set -u
REPO="$1"; T="$2"; PY="$REPO/.venv/bin/python"; H="$(cd "$(dirname "$0")" && pwd)"; M="$T/med/bateria"
export PYTHONDONTWRITEBYTECODE=1
rm -rf "$M"; mkdir -p "$M"
log() { printf '%s\n' "$*" | tee -a "$M/bateria.log"; }
igual() { if cmp -s "$1" "$2"; then log "$3: iguales byte a byte"; else log "$3: DISTINTOS"; fi; }
cuenta_pyc() { find "$REPO" \( -path "$REPO/.git" -o -path "$REPO/.venv" \) -prune -o -name '*.pyc' -print | wc -l | tr -d ' '; }
log "inicio $(date '+%Y-%m-%d %H:%M:%S %z'); HEAD $(git -C "$REPO" rev-parse HEAD)"
python3 -I -B "$H/foto_repo.py" "$REPO" "$M/foto_repo_antes.txt" > /dev/null
log "foto del repo antes: $(wc -l < "$M/foto_repo_antes.txt" | tr -d ' ') archivos; .pyc: $(cuenta_pyc)"

log "--- 0. las copias: copia_head = copia inicial; la copia nueva difiere solo en los archivos de A1"
python3 -I -B "$H/foto_repo.py" "$T/copia_head" "$M/foto_copia_head.txt" > /dev/null
python3 -I -B "$H/foto_repo.py" "$T/copia" "$M/foto_copia_nueva.txt" > /dev/null
igual "$T/foto_copia_inicial.txt" "$M/foto_copia_head.txt" "foto de copia_head y foto de la copia inicial"
log "$(python3 -I -B -c "
import sys
def leer(p): return dict(reversed(l.rstrip('\\n').split('  ', 1)) for l in open(p, encoding='utf-8'))
a, b = leer(sys.argv[1]), leer(sys.argv[2])
print('copia nueva contra la inicial: cambian', sorted(r for r in a if r in b and a[r] != b[r]), '| nuevos', sorted(r for r in b if r not in a), '| faltan', sorted(r for r in a if r not in b))
" "$T/foto_copia_inicial.txt" "$M/foto_copia_nueva.txt")"

log "--- 1. derivado: dos corridas y la de la copia"
for i in 1 2; do
  (cd "$T/copia" && "$PY" -B data/experiment/catalogo_unico/code/derivar_registro_alcance_r2b.py --tandas 1 \
      --salida "$M/derivado_corrida$i.json" --reporte "$M/reporte_derivado_corrida$i.json" > /dev/null); log "corrida $i rc=$?"
done
igual "$M/derivado_corrida1.json" "$M/derivado_corrida2.json" "derivado, corridas 1 y 2"
igual "$M/reporte_derivado_corrida1.json" "$M/reporte_derivado_corrida2.json" "reporte del derivado, corridas 1 y 2"
igual "$M/derivado_corrida1.json" "$T/copia/data/experiment/catalogo_unico/registro_alcance_r2b.json" "derivado de la copia y corrida 1"
log "sha256 del derivado: $(shasum -a 256 "$M/derivado_corrida1.json" | cut -d' ' -f1)"

log "--- 2. valores del candado del mensaje: dos procesos y verificación"
for i in 1 2; do "$PY" -B "$H/sellar_a1.py" --raiz "$T/copia" --salida "$M/sellos_proceso$i" > /dev/null; log "proceso $i rc=$?"; done
igual "$M/sellos_proceso1/sellos_a1.json" "$M/sellos_proceso2/sellos_a1.json" "valores del candado, procesos 1 y 2"
"$PY" -B "$H/sellar_a1.py" --raiz "$T/copia" --salida "$M/sellos_verificacion" --verificar > /dev/null; log "verificación rc=$?"
log "$(python3 -I -B -c "import json,sys; d=json.load(open(sys.argv[1])); print('coinciden', d['coinciden'], d['constantes'])" "$M/sellos_verificacion/verificacion_sellos_a1.json")"

log "--- 3. selftest_prompt_r2b: HEAD sobre HEAD, nuevo sobre la copia, nuevo con el código de HEAD"
(cd "$T/copia_head" && "$PY" -B data/experiment/reextraccion_v2/e1_extractor/selftest_prompt_r2b.py > "$M/selftest_prompt_r2b_HEAD_sobre_HEAD.txt" 2>&1); log "HEAD sobre HEAD rc=$? $(tail -1 "$M/selftest_prompt_r2b_HEAD_sobre_HEAD.txt")"
(cd "$T/copia" && "$PY" -B data/experiment/reextraccion_v2/e1_extractor/selftest_prompt_r2b.py > "$M/selftest_prompt_r2b_nuevo.txt" 2>&1); log "nuevo sobre la copia rc=$? $(tail -1 "$M/selftest_prompt_r2b_nuevo.txt")"
rm -rf "$T/control_neg"; cp -cR "$T/copia_head" "$T/control_neg"
for f in data/experiment/reextraccion_v2/e1_extractor/selftest_prompt_r2b.py data/experiment/catalogo_unico/code/derivar_registro_alcance_r2b.py data/experiment/catalogo_unico/registro_alcance_r2b.json; do cp "$T/copia/$f" "$T/control_neg/$f"; done
for f in data/experiment/reextraccion_v2/e1_extractor/prompt_r2b.py data/experiment/reextraccion_v2/e1_extractor/candado_mensaje_r2b.json; do igual "$T/control_neg/$f" "$REPO/$f" "control negativo, $f contra el repo"; done
(cd "$T/control_neg" && "$PY" -B data/experiment/reextraccion_v2/e1_extractor/selftest_prompt_r2b.py > "$M/selftest_prompt_r2b_nuevo_con_codigo_HEAD.txt" 2>&1); log "nuevo con el código de HEAD rc=$? $(tail -1 "$M/selftest_prompt_r2b_nuevo_con_codigo_HEAD.txt")"
python3 -I -B "$H/control_negativo_a1.py" "$M/selftest_prompt_r2b_HEAD_sobre_HEAD.txt" "$M/selftest_prompt_r2b_nuevo.txt" "$M/selftest_prompt_r2b_nuevo_con_codigo_HEAD.txt" "$M/control_negativo.json" > /dev/null
log "$(python3 -I -B -c "import json,sys; d=json.load(open(sys.argv[1])); print('exactamente los nuevos', d['exactamente_los_nuevos'], '| nuevos', d['casos_nuevos'], '| reescritos', len(d['casos_reescritos']), '| por atributo', d['fallan_por_atributo_que_falta'])" "$M/control_negativo.json")"

log "--- 4. corrida en seco por el camino del runner (HEAD y nuevo) y comparación"
"$PY" -B "$H/mensajes_runner_a1.py" --raiz "$T/copia_head" --salida "$M/seco" --etiqueta head > /dev/null; log "head rc=$?"
"$PY" -B "$H/mensajes_runner_a1.py" --raiz "$T/copia" --salida "$M/seco" --etiqueta nuevo > /dev/null; log "nuevo rc=$?"
for e in head nuevo; do log "$e: $(python3 -I -B -c "import json,sys; d=json.load(open(sys.argv[1])); print(d['tanda0_unidades'], d['tanda0_sha256_mensajes'], d['fixture_unidades'], d['fixture_sha256_mensajes'], d['modulos_de_data_experiment_fuera_de_la_copia'])" "$M/seco/resumen_$e.json")"; done
python3 -I -B "$H/comparar_a1.py" "$M/seco" "$M/comparacion_mensajes_a1.json" > "$M/comparacion_consola.txt"; log "comparación rc=$?"
head -1 "$M/comparacion_consola.txt" | tee -a "$M/bateria.log"; grep "^tanda1\|^fixture" "$M/comparacion_consola.txt" | tee -a "$M/bateria.log"

log "--- 5. selftest_clave_cache --salida-r2b (HEAD y nuevo)"
for e in head nuevo; do
  d="$T/copia"; [ "$e" = head ] && d="$T/copia_head"
  (cd "$d" && "$PY" -B data/experiment/mantenimiento/code/selftest_clave_cache.py --salida-r2b data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b --out "$M/selftest_clave_cache_$e.json" > "$M/consola_clave_cache_$e.txt" 2>&1); log "$e rc=$? $(tail -1 "$M/consola_clave_cache_$e.txt")"
done
igual "$M/selftest_clave_cache_head.json" "$REPO/data/experiment/mantenimiento/selftest_clave_cache.json" "selftest_clave_cache de HEAD y el JSON del repo"
log "$(python3 -I -B -c "
import json,sys
h=json.load(open(sys.argv[1])); n=json.load(open(sys.argv[2]))
print('A1r igual', h['perfil_r2b']['anclaje']['e1']==n['perfil_r2b']['anclaje']['e1'], n['perfil_r2b']['anclaje']['e1']['estado'], n['perfil_r2b']['anclaje']['e1']['claves_calculadas'], '| A3r igual', h['perfil_r2b']['anclaje']['e3']==n['perfil_r2b']['anclaje']['e3'], '| tokens iguales', [(v['id'],v['e1']['token'],v['e3']['token']) for v in h['perfil_r2b']['variaciones']]==[(v['id'],v['e1']['token'],v['e3']['token']) for v in n['perfil_r2b']['variaciones']], '| contraste', n['contraste_tabla']['estado'], '| veredicto', n['veredicto'])
" "$M/selftest_clave_cache_head.json" "$M/selftest_clave_cache_nuevo.json")"
(cd "$M" && diff selftest_clave_cache_head.json selftest_clave_cache_nuevo.json > diff_clave_cache_head_nuevo.txt); log "diff head/nuevo: $(grep -c '^[<>]' "$M/diff_clave_cache_head_nuevo.txt") líneas"

log "--- 6. K2 de selftest_catalogo_unico con el derivado fuera de generados_r2/"
"$PY" -B "$H/k2_generados_r2.py" "$T/copia" | tee -a "$M/bateria.log"

python3 -I -B "$H/foto_repo.py" "$REPO" "$M/foto_repo_despues.txt" > /dev/null
log "foto del repo después: $(wc -l < "$M/foto_repo_despues.txt" | tr -d ' ') archivos; .pyc: $(cuenta_pyc)"
if cmp -s "$M/foto_repo_antes.txt" "$M/foto_repo_despues.txt"; then log "repo: sin cambios (sha256 de todos los archivos iguales)"; else log "repo: CAMBIOS"; diff "$M/foto_repo_antes.txt" "$M/foto_repo_despues.txt" | tee -a "$M/bateria.log"; fi
log "fin $(date '+%Y-%m-%d %H:%M:%S %z')"
