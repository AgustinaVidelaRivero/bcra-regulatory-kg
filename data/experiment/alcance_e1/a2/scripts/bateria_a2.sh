#!/bin/zsh
# U-ALCANCE-E1, A2: batería de controles sobre copias sin enlaces (USD 0, sin API), con la foto sha256 del repo antes y
# después (CLAUDE.md §4.l). Sigue a bateria_a1.sh de A1.
# Uso: zsh bateria_a2.sh REPO TRABAJO, con TRABAJO fuera del repo y armado así:
#   - TRABAJO/copia_head: el rsync de los despachos (sin .env ni NO_ABRIR_), controlado por nombre;
#   - TRABAJO/copia_a2: clon APFS de copia_head (cp -cR: copia, no enlace) con el parche de A1 aplicado (git apply) y los
#     cambios de A2;
#   - TRABAJO/copia_a1: clon de copia_a2 tomado después del parche y antes de los cambios de A2;
#   - TRABAJO/e0t/e0_152: la E0 corregida de los 152, regenerada con correr_lote_e0_a2.sh (lote_tramo1_S2.sh de S2).
# Los scripts se toman del directorio de este archivo; la salida va a TRABAJO/med/bateria.
R="$1"; T="$2"; PY="$R/.venv/bin/python"; H="${0:A:h}"; M="$T/med/bateria"
export PYTHONDONTWRITEBYTECODE=1
rm -rf "$M"; mkdir -p "$M"
log() { print -r -- "$*" | tee -a "$M/bateria.log"; }
igual() { if cmp -s "$1" "$2"; then log "$3: iguales byte a byte"; else log "$3: DISTINTOS"; fi; }
cuenta_pyc() { find "$R" \( -path "$R/.git" -o -path "$R/.venv" \) -prune -o -name '*.pyc' -print | wc -l | tr -d ' '; }
cuenta_env() { find "$1" \( -name '.env' -o -name '.env.*' -o -name '*.env' -o -name 'NO_ABRIR_*' \) | wc -l | tr -d ' '; }
E1="data/experiment/reextraccion_v2/e1_extractor"
LISTA="data/experiment/segmentacion_oficial_e0r2/s2/lista_tanda1_S2.json"
log "inicio $(date '+%Y-%m-%d %H:%M:%S %z'); HEAD $(git -C "$R" rev-parse HEAD)"
python3 -I -B "$H/foto_repo_a2.py" "$R" "$M/foto_repo_antes.json" | tee -a "$M/bateria.log"
log ".pyc antes: $(cuenta_pyc)"
log "control por nombre (.env, .env.*, *.env, NO_ABRIR_*): copia_head $(cuenta_env "$T/copia_head"), copia_a2 $(cuenta_env "$T/copia_a2"), e0t $(cuenta_env "$T/e0t")"
log "enlaces simbólicos: copia_head $(find "$T/copia_head" -type l | wc -l | tr -d ' '), copia_a2 $(find "$T/copia_a2" -type l | wc -l | tr -d ' ')"

log "--- 0. las copias: copia_head sigue igual a la foto tomada al copiarla; copia_a2 difiere solo en las escrituras"
python3 -I -B "$H/foto_repo_a2.py" "$T/copia_head" "$M/foto_copia_head.json" > /dev/null
python3 -I -B "$H/foto_repo_a2.py" "$T/copia_a2" "$M/foto_copia_a2.json" > /dev/null
python3 -I -c "
import json, sys
a, b = (json.load(open(p))['archivos'] for p in sys.argv[1:3])
print('copia_head contra la foto inicial: iguales' if a == b else 'copia_head contra la foto inicial: DISTINTA')
" "$T/med/foto_copia_head.json" "$M/foto_copia_head.json" | tee -a "$M/bateria.log"
python3 -I -B "$H/foto_repo_a2.py" --comparar "$M/foto_copia_head.json" "$M/foto_copia_a2.json" "$M/comp_copias.json" | tee -a "$M/bateria.log"
log "$(python3 -I -c "import json,sys; d=json.load(open(sys.argv[1])); print('nuevos', d['nuevos'], '| cambiados', d['cambiados'], '| quitados', d['quitados'])" "$M/comp_copias.json")"

log "--- 1. derivado: dos corridas (--tandas 1) y el archivo de copia_a2"
for i in 1 2; do
  (cd "$T/copia_a2" && "$PY" -B data/experiment/catalogo_unico/code/derivar_registro_alcance_r2b.py --tandas 1 \
      --salida "$M/derivado_corrida$i.json" --reporte "$M/reporte_derivado_corrida$i.json" > /dev/null); log "corrida $i rc=$?"
done
igual "$M/derivado_corrida1.json" "$M/derivado_corrida2.json" "derivado, corridas 1 y 2"
igual "$M/reporte_derivado_corrida1.json" "$M/reporte_derivado_corrida2.json" "reporte del derivado, corridas 1 y 2"
igual "$M/derivado_corrida1.json" "$T/copia_a2/data/experiment/catalogo_unico/registro_alcance_r2b.json" "derivado de copia_a2 y corrida 1"
log "sha256 del derivado: $(shasum -a 256 "$M/derivado_corrida1.json" | cut -d' ' -f1)"
log "sha256 del registro: $(shasum -a 256 "$T/copia_a2/data/experiment/catalogo_unico/registro_alcance_por_tanda.md" | cut -d' ' -f1)"
log "$(python3 -I -c "
import json, sys
d = json.load(open(sys.argv[1]))
print('filas por tanda', d['filas_por_tanda_del_registro'], '| entradas', d['entradas'], '| con alcance', [f['to'] for f in d['filas_con_alcance']],
      '| sin alcance', [f['to'] for f in d['sin_alcance_declarado']], '| otras tandas', [(f['tanda'], f['to']) for f in d['filas_de_otras_tandas']])
" "$M/reporte_derivado_corrida1.json")"
log "derivado de A1 (copia_a1, el del parche) contra el de A2: $(diff "$T/copia_a1/data/experiment/catalogo_unico/registro_alcance_r2b.json" "$M/derivado_corrida1.json" | grep -c '^>') líneas agregadas, $(diff "$T/copia_a1/data/experiment/catalogo_unico/registro_alcance_r2b.json" "$M/derivado_corrida1.json" | grep -c '^<') quitadas"

log "--- 2. valores del candado del mensaje: dos procesos y verificación"
for i in 1 2; do "$PY" -B "$H/sellar_a2.py" --raiz "$T/copia_a2" --salida "$M/sellos_proceso$i" > /dev/null; log "proceso $i rc=$?"; done
igual "$M/sellos_proceso1/sellos_a2.json" "$M/sellos_proceso2/sellos_a2.json" "valores del candado, procesos 1 y 2"
"$PY" -B "$H/sellar_a2.py" --raiz "$T/copia_a2" --salida "$M/sellos_verificacion" --verificar > /dev/null; log "verificación rc=$?"
log "$(python3 -I -B -c "import json,sys; d=json.load(open(sys.argv[1])); print('coinciden', d['coinciden'], d['constantes'], 'unidades de la fixture', d['unidades_de_la_fixture'])" "$M/sellos_verificacion/verificacion_sellos_a2.json")"

log "--- 3. selftest_prompt_r2b: HEAD sobre HEAD, A2 sobre copia_a2, el de A2 con el código de HEAD"
(cd "$T/copia_head" && "$PY" -B $E1/selftest_prompt_r2b.py > "$M/selftest_prompt_r2b_HEAD_sobre_HEAD.txt" 2>&1); log "HEAD sobre HEAD rc=$? $(tail -1 "$M/selftest_prompt_r2b_HEAD_sobre_HEAD.txt")"
(cd "$T/copia_a2" && "$PY" -B $E1/selftest_prompt_r2b.py > "$M/selftest_prompt_r2b_a2.txt" 2>&1); log "A2 sobre copia_a2 rc=$? $(tail -1 "$M/selftest_prompt_r2b_a2.txt")"
rm -rf "$T/control_neg"; cp -cR "$T/copia_head" "$T/control_neg"
for f in $E1/selftest_prompt_r2b.py data/experiment/catalogo_unico/code/derivar_registro_alcance_r2b.py data/experiment/catalogo_unico/registro_alcance_r2b.json; do cp "$T/copia_a2/$f" "$T/control_neg/$f"; done
for f in $E1/prompt_r2b.py $E1/candado_mensaje_r2b.json $E1/perfil_e1.py; do igual "$T/control_neg/$f" "$R/$f" "control negativo, $f contra el repo"; done
(cd "$T/control_neg" && "$PY" -B $E1/selftest_prompt_r2b.py > "$M/selftest_prompt_r2b_a2_con_codigo_HEAD.txt" 2>&1); log "A2 con el código de HEAD rc=$? $(tail -1 "$M/selftest_prompt_r2b_a2_con_codigo_HEAD.txt")"
python3 -I -B "$H/control_negativo_a2.py" "$M/selftest_prompt_r2b_HEAD_sobre_HEAD.txt" "$M/selftest_prompt_r2b_a2.txt" "$M/selftest_prompt_r2b_a2_con_codigo_HEAD.txt" "$M/control_negativo.json" > /dev/null
log "$(python3 -I -B -c "import json,sys; d=json.load(open(sys.argv[1])); print('exactamente los nuevos', d['exactamente_los_nuevos'], '| nuevos', d['casos_nuevos'], '| reescritos', len(d['casos_reescritos']), '| por atributo', d['fallan_por_atributo_que_falta'], '| totales', d['head_sobre_head'], d['nuevo_sobre_la_copia'], d['nuevo_con_codigo_head'])" "$M/control_negativo.json")"

log "--- 4. corrida en seco por el camino del runner (HEAD y A2): tanda 0, lista final de la tanda 1 y fixture"
"$PY" -B "$H/mensajes_runner_a2.py" --raiz "$T/copia_head" --e0-tanda1 "$T/e0t/e0_152" --lista "$T/copia_head/$LISTA" --salida "$M/seco" --etiqueta head > /dev/null; log "head rc=$?"
"$PY" -B "$H/mensajes_runner_a2.py" --raiz "$T/copia_a2" --e0-tanda1 "$T/e0t/e0_152" --lista "$T/copia_a2/$LISTA" --salida "$M/seco" --etiqueta a2 > /dev/null; log "a2 rc=$?"
for e in head a2; do log "$e: $(python3 -I -B -c "import json,sys; d=json.load(open(sys.argv[1])); print('derivado', d['derivado_en_el_modulo'], '| tanda 0', d['tanda0_unidades'], d['tanda0_sha256_mensajes'], '| tanda 1', d['tanda1_unidades'], len(d['tanda1_tos']), 'TOs | fixture', d['fixture_unidades'], d['fixture_sha256_mensajes'], '| ajenos', d['modulos_de_data_experiment_fuera_de_la_copia'])" "$M/seco/resumen_$e.json")"; done
python3 -I -B "$H/comparar_a2.py" "$M/seco" "$T/copia_a2" "$T/copia_a2/$LISTA" "$T/copia_a2/data/experiment/catalogo_unico/registro_alcance_r2b.json" "$M/medicion_tanda1_a2.json" > "$M/comparacion_consola.txt"; log "comparación rc=$?"
tee -a "$M/bateria.log" < "$M/comparacion_consola.txt"
log "fixture: las 13 de P3c-2 con el código de A2 dan $(python3 -I -B -c "
import json, sys, hashlib
fs = [json.loads(l) for l in open(sys.argv[1], encoding='utf-8') if json.loads(l)['origen'] == 'fixture_candado']
print(hashlib.sha256('\n\x1e\n'.join(f['mensaje'] for f in fs[:13]).encode('utf-8')).hexdigest()[:12], 'de', len(fs))
" "$M/seco/mensajes_a2.jsonl")"

log "--- 5. selftest_clave_cache --salida-r2b: HEAD, y A2 en dos corridas"
(cd "$T/copia_head" && "$PY" -B data/experiment/mantenimiento/code/selftest_clave_cache.py --salida-r2b data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b --out "$M/selftest_clave_cache_head.json" > "$M/consola_clave_cache_head.txt" 2>&1); log "head rc=$? $(tail -1 "$M/consola_clave_cache_head.txt")"
for i in 1 2; do
  (cd "$T/copia_a2" && "$PY" -B data/experiment/mantenimiento/code/selftest_clave_cache.py --salida-r2b data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b --out "$M/selftest_clave_cache_a2_$i.json" > "$M/consola_clave_cache_a2_$i.txt" 2>&1); log "a2 corrida $i rc=$? $(tail -1 "$M/consola_clave_cache_a2_$i.txt")"
done
igual "$M/selftest_clave_cache_head.json" "$R/data/experiment/mantenimiento/selftest_clave_cache.json" "selftest_clave_cache de HEAD y el JSON del repo"
igual "$M/selftest_clave_cache_a2_1.json" "$M/selftest_clave_cache_a2_2.json" "selftest_clave_cache de A2, corridas 1 y 2"
igual "$M/selftest_clave_cache_a2_1.json" "$T/copia_a2/data/experiment/mantenimiento/selftest_clave_cache.json" "selftest_clave_cache de A2 y el JSON de copia_a2"
log "$(python3 -I -B -c "
import json,sys
h=json.load(open(sys.argv[1])); n=json.load(open(sys.argv[2]))
vh, vn = h['perfil_r2b']['variaciones'], n['perfil_r2b']['variaciones']
print('variaciones r2b', len(vh), '->', len(vn), '| nuevas', [v['id'] for v in vn if v['id'] not in {x['id'] for x in vh}],
      '| A1r igual', h['perfil_r2b']['anclaje']['e1']==n['perfil_r2b']['anclaje']['e1'], n['perfil_r2b']['anclaje']['e1']['estado'],
      '| A3r igual', h['perfil_r2b']['anclaje']['e3']==n['perfil_r2b']['anclaje']['e3'],
      '| tokens de las 44 iguales', [(v['id'],v['e1']['token'],v['e3']['token']) for v in vh]==[(v['id'],v['e1']['token'],v['e3']['token']) for v in vn if v['id']!='R34'],
      '| R34', [(v['e1']['token'], v['e1']['observadas_que_cambian'], v['e3']['token']) for v in vn if v['id']=='R34'],
      '| contraste', n['contraste_tabla']['estado'], len(n['contraste_tabla']['filas']), 'filas', '| veredicto', n['veredicto'])
" "$M/selftest_clave_cache_head.json" "$M/selftest_clave_cache_a2_1.json")"
(cd "$M" && diff selftest_clave_cache_head.json selftest_clave_cache_a2_1.json > diff_clave_cache_head_a2.txt); log "diff head/A2: $(grep -c '^[<>]' "$M/diff_clave_cache_head_a2.txt") líneas"

log "--- 6. selftests vecinos sobre las dos copias"
for e in head a2; do
  (cd "$T/copia_$e" && "$PY" -B data/experiment/catalogo_unico/code/selftest_catalogo_unico.py > "$M/selftest_catalogo_unico_$e.txt" 2>&1); log "catalogo_unico $e rc=$? $(tail -1 "$M/selftest_catalogo_unico_$e.txt")"
  (cd "$T/copia_$e" && "$PY" -B data/experiment/reresolucion_catalogo/selftest_reresolver_catalogo.py > "$M/selftest_reresolver_catalogo_$e.txt" 2>&1); log "reresolver_catalogo $e rc=$? $(tail -1 "$M/selftest_reresolver_catalogo_$e.txt")"
  (cd "$T/copia_$e" && "$PY" -B data/experiment/reextraccion_v2/selftest_cablev3.py > "$M/selftest_cablev3_$e.txt" 2>&1); log "cablev3 $e rc=$? $(tail -1 "$M/selftest_cablev3_$e.txt")"
  (cd "$T/copia_$e" && "$PY" -B data/experiment/reextraccion_v2/selftest_manifiesto.py > "$M/selftest_manifiesto_$e.txt" 2>&1); log "manifiesto $e rc=$? $(tail -1 "$M/selftest_manifiesto_$e.txt")"
done
for s in catalogo_unico reresolver_catalogo cablev3 manifiesto; do igual "$M/selftest_${s}_head.txt" "$M/selftest_${s}_a2.txt" "selftest_$s, consola de HEAD y de A2"; done

log "--- 7. manifiestos de los 152 de S1, S1-bis y S1-ter contra el registro y el perfil r2b"
for e in head a2; do
  "$PY" -B "$H/manifiestos_a2.py" --raiz "$T/copia_$e" --etiqueta $e --salida "$M/manifiestos_$e.json" > "$M/manifiestos_$e.txt" 2>&1; log "$e rc=$?"
  sed 's/^/   /' "$M/manifiestos_$e.txt" | tee -a "$M/bateria.log" > /dev/null
done

log "--- 8. la E0 corregida contra el manifiesto de S0-6b y la lista regenerada"
log "$(python3 -I -c "import json,sys; d=json.load(open(sys.argv[1])); print({k: d[k] for k in d if not isinstance(d[k], (list, dict))})" "$T/e0t/control_e0_S2a.json" 2>&1 | cut -c1-600)"

python3 -I -B "$H/foto_repo_a2.py" "$R" "$M/foto_repo_despues.json" | tee -a "$M/bateria.log"
log ".pyc después: $(cuenta_pyc)"
python3 -I -B "$H/foto_repo_a2.py" --comparar "$M/foto_repo_antes.json" "$M/foto_repo_despues.json" "$M/comparacion_foto_repo.json" | tee -a "$M/bateria.log"
log "fin $(date '+%Y-%m-%d %H:%M:%S %z')"
