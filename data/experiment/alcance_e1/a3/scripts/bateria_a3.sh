#!/bin/zsh
# U-ALCANCE-E1, A3: batería de los once criterios del mandato (§5) sobre copias sin enlaces (USD 0, sin API), con la foto
# sha256 del repo antes y después de cada paso (CLAUDE.md §4.l). Sigue a bateria_a2.sh de A2. No escribe en el repo.
# Uso: zsh bateria_a3.sh REPO TRABAJO SALIDA [LECTURAS HOOK]
#   - TRABAJO/copia_head: el rsync del despacho de A3 (sin .env ni NO_ABRIR_, sin tanda1/t4/ ni t5/), con los blobs
#     controlados contra la base;
#   - TRABAJO/copia_a3: clon de copia_head (cp -cR: copia, no enlace) con las escrituras de A3;
#   - TRABAJO/e0t/e0_152: la E0 corregida de los 152, regenerada con correr_lote_e0_a3.sh (los pasos de lote_tramo1_S2.sh);
#   - SALIDA: carpeta nueva fuera del repo;
#   - LECTURAS y HOOK (opcionales): con ellos, cada proceso de Python del .venv anota lo que abre (sitecustomize de HOOK,
#     por PYTHONPATH) en LECTURAS; sin ellos, la corrida es la oficial.
# Los scripts se toman del directorio de este archivo.
R="$1"; T="$2"; M="$3"; LEC="$4"; HOOK="$5"
PY="$R/.venv/bin/python"; H="${0:A:h}"; CH="$T/copia_head"; CA="$T/copia_a3"; E0="$T/e0t/e0_152"
BASE=5289b02f6457aabba5c4d15e50236cde240f2536
export PYTHONDONTWRITEBYTECODE=1; unset ANTHROPIC_API_KEY
[ -n "$LEC" ] && { mkdir -p "$LEC"; export A3_LOG_LECTURAS="$LEC" PYTHONPATH="$HOOK"; }
rm -rf "$M"; mkdir -p "$M/fotos"
L="$M/bateria_a3.log"
log() { print -r -- "$*" | tee -a "$L"; }
igual() { if cmp -s "$1" "$2"; then log "$3: iguales byte a byte"; else log "$3: DISTINTOS"; fi; }
cuenta_pyc() { find "$R" \( -path "$R/.git" -o -path "$R/.venv" -o -path "$R/.venv-app" \) -prune -o -name '*.pyc' -print | wc -l | tr -d ' '; }
cuenta_env() { find "$1" \( -name '.env' -o -name '.env.*' -o -name '*.env' -o -name 'NO_ABRIR_*' \) | wc -l | tr -d ' '; }
E1="data/experiment/reextraccion_v2/e1_extractor"
LISTA="data/experiment/segmentacion_oficial_e0r2/s2/lista_tanda1_S2.json"
TF="data/experiment/segmentacion_oficial_e0r2/s2/cifras/tanda_final_S2c.json"
DER="data/experiment/catalogo_unico/registro_alcance_r2b.json"
REG="data/experiment/catalogo_unico/registro_alcance_por_tanda.md"
GEN="data/experiment/catalogo_unico/code/derivar_registro_alcance_r2b.py"
paso=0; previa=""
foto() {   # foto del repo con la comparación contra la anterior, y el conteo de .pyc
  local f="$M/fotos/foto_repo_$(printf %02d $paso)_$1.json"
  python3 -I -B "$H/foto_repo_a3.py" "$R" "$f" > /dev/null
  if [ -n "$previa" ]; then
    log "foto del repo, $1: $(python3 -I -B "$H/foto_repo_a3.py" --comparar "$previa" "$f" "${f%.json}_comparacion.json")"
  else
    log "foto del repo, $1: $(python3 -I -B -c "import json,sys; print(len(json.load(open(sys.argv[1]))['archivos']), 'renglones')" "$f")"
  fi
  log ".pyc, $1: $(cuenta_pyc)"
  previa="$f"; paso=$((paso + 1))
}
log "inicio $(date '+%Y-%m-%d %H:%M:%S %z'); HEAD $(git --no-optional-locks -C "$R" rev-parse HEAD); base $BASE; registro de lecturas: ${LEC:+sí}${LEC:-no}"
foto inicio
touch "$M/marca_git_antes"

log "--- 0. las copias"
log "control por nombre (.env, .env.*, *.env, NO_ABRIR_*): copia_head $(cuenta_env "$CH"), copia_a3 $(cuenta_env "$CA"), e0t $(cuenta_env "$T/e0t")"
log "enlaces simbólicos: copia_head $(find "$CH" -type l | wc -l | tr -d ' '), copia_a3 $(find "$CA" -type l | wc -l | tr -d ' '), e0t $(find "$T/e0t" -type l | wc -l | tr -d ' ')"
for c in head a3; do
  python3 -I -B "$H/blobs_contra_base_a3.py" "$R" $BASE "$T/copia_$c" "$M/blobs_copia_${c}_contra_base.json" > /dev/null
  log "blobs de copia_$c contra la base: $(python3 -I -B -c "import json,sys; d=json.load(open(sys.argv[1])); print(d['comparados_iguales'], 'iguales | distintos o faltantes', [x[0] for x in d['distintos_o_faltantes']], '| sin comparar', d['sin_comparar'])" "$M/blobs_copia_${c}_contra_base.json")"
done
python3 -I -B "$H/pdfs_contra_manifiesto_a3.py" "$CH" "$M/pdfs_copia_head.json" > /dev/null; log "PDFs de copia_head contra sus manifiestos rastreados rc=$?"
foto copias

log "--- 1. el derivado (criterio 4): dos corridas con --tandas 1,final, el archivo de copia_a3 y el de HEAD"
for i in 1 2; do
  (cd "$CA" && "$PY" -B $GEN --tandas 1,final --salida "$M/derivado_corrida$i.json" --reporte "$M/reporte_derivado_corrida$i.json" > /dev/null); log "corrida $i rc=$?"
done
igual "$M/derivado_corrida1.json" "$M/derivado_corrida2.json" "derivado, corridas 1 y 2"
igual "$M/reporte_derivado_corrida1.json" "$M/reporte_derivado_corrida2.json" "reporte del derivado, corridas 1 y 2"
igual "$M/derivado_corrida1.json" "$CA/$DER" "derivado de copia_a3 y corrida 1"
(cd "$CA" && "$PY" -B $GEN --tandas 1 --salida - > "$M/derivado_tandas_1.json"); log "corrida con --tandas 1 rc=$?"
igual "$M/derivado_tandas_1.json" "$CH/$DER" "derivado con --tandas 1 (registro de la base) y el de HEAD"
log "sha256 del derivado: $(shasum -a 256 "$M/derivado_corrida1.json" | cut -d' ' -f1); el de HEAD: $(shasum -a 256 "$CH/$DER" | cut -d' ' -f1)"
log "sha256 del registro: $(shasum -a 256 "$CA/$REG" | cut -d' ' -f1)"
diff "$CH/$DER" "$M/derivado_corrida1.json" > "$M/diff_derivado_head_a3.txt"
log "diff contra el de HEAD: $(grep -c '^>' "$M/diff_derivado_head_a3.txt") renglones agregados, $(grep -c '^<' "$M/diff_derivado_head_a3.txt") quitados; bloques: $(grep -E '^[0-9]' "$M/diff_derivado_head_a3.txt" | tr '\n' ' ')"
"$PY" -B "$H/filas_tanda_final_a3.py" "$CA/$REG" "$M/reporte_derivado_corrida1.json" "$M/derivado_corrida1.json" "$CH/$DER" "$M/filas_tanda_final_a3.json" | tee -a "$L"
foto derivado

log "--- 2. los valores del candado del mensaje (criterios 3.3 y 8): el método de sellar_a2.py, dos procesos y la verificación"
S="$CA/data/experiment/alcance_e1/a2/scripts/sellar_a2.py"
log "sellar_a2.py de la copia: $(shasum -a 256 "$S" | cut -d' ' -f1)"
for i in 1 2; do "$PY" -B "$S" --raiz "$CA" --salida "$M/sellos_a3_proceso$i" > /dev/null; log "A3, proceso $i rc=$?"; done
igual "$M/sellos_a3_proceso1/sellos_a2.json" "$M/sellos_a3_proceso2/sellos_a2.json" "valores del candado de A3, procesos 1 y 2"
"$PY" -B "$S" --raiz "$CH" --salida "$M/sellos_head" > /dev/null; log "HEAD, mismo método rc=$?"
"$PY" -B "$S" --raiz "$CA" --salida "$M/sellos_a3_verificacion" --verificar > /dev/null; log "verificación sobre copia_a3 rc=$?"
log "$(python3 -I -B -c "
import json, sys
a, h, v = (json.load(open(p)) for p in sys.argv[1:4])
print('A3:', {k: a[k] for k in ('CANDADO_MENSAJE_JSON_SHA256_ESPERADO', 'MENSAJE_R2B_SHA256_ESPERADO', 'sha256_derivado', 'derivado_igual_al_literal', 'unidades_de_la_fixture', 'prefijo_hash')})
print('   HEAD:', {k: h[k] for k in ('CANDADO_MENSAJE_JSON_SHA256_ESPERADO', 'MENSAJE_R2B_SHA256_ESPERADO', 'sha256_derivado', 'derivado_igual_al_literal')})
print('   los dos del candado, iguales a los de HEAD:', a['CANDADO_MENSAJE_JSON_SHA256_ESPERADO'] == h['CANDADO_MENSAJE_JSON_SHA256_ESPERADO'] and a['MENSAJE_R2B_SHA256_ESPERADO'] == h['MENSAJE_R2B_SHA256_ESPERADO'])
print('   verificación:', 'coinciden', v['coinciden'], v['constantes'], '| unidades de la fixture', v['unidades_de_la_fixture'], '| importa sin frenar', v['importa_sin_frenar'])
" "$M/sellos_a3_proceso1/sellos_a2.json" "$M/sellos_head/sellos_a2.json" "$M/sellos_a3_verificacion/verificacion_sellos_a2.json")"
log "la fixture del candado: $(python3 -I -B -c "
import json, sys
fx = json.load(open(sys.argv[1])); nuevos = set(json.load(open(sys.argv[2]))) - set(json.load(open(sys.argv[3])))
print(len(fx['chunks']), 'unidades; documentos', sorted({c['archivo'] for c in fx['chunks']}), '| con entrada nueva en el derivado:', sorted({c['archivo'] for c in fx['chunks']} & nuevos))
" "$CA/$E1/candado_mensaje_r2b.json" "$CA/$DER" "$CH/$DER")"
igual "$CA/$E1/candado_mensaje_r2b.json" "$CH/$E1/candado_mensaje_r2b.json" "candado_mensaje_r2b.json de A3 y el de HEAD"
foto candado

log "--- 3. selftest_prompt_r2b (criterio 5): HEAD sobre HEAD, A3 sobre copia_a3, el de A3 con el código de HEAD"
(cd "$CH" && "$PY" -B $E1/selftest_prompt_r2b.py > "$M/selftest_prompt_r2b_HEAD_sobre_HEAD.txt" 2>&1); log "HEAD sobre HEAD rc=$? $(tail -1 "$M/selftest_prompt_r2b_HEAD_sobre_HEAD.txt")"
(cd "$CA" && "$PY" -B $E1/selftest_prompt_r2b.py > "$M/selftest_prompt_r2b_a3.txt" 2>&1); log "A3 sobre copia_a3 rc=$? $(tail -1 "$M/selftest_prompt_r2b_a3.txt")"
rm -rf "$T/control_neg"; cp -cR "$CH" "$T/control_neg"; cp "$CA/$E1/selftest_prompt_r2b.py" "$T/control_neg/$E1/selftest_prompt_r2b.py"
for f in $E1/prompt_r2b.py $DER $E1/candado_mensaje_r2b.json $E1/perfil_e1.py $GEN $REG; do igual "$T/control_neg/$f" "$CH/$f" "control negativo, $f contra copia_head"; done
(cd "$T/control_neg" && "$PY" -B $E1/selftest_prompt_r2b.py > "$M/selftest_prompt_r2b_a3_con_codigo_HEAD.txt" 2>&1); log "A3 con el código de HEAD rc=$? $(tail -1 "$M/selftest_prompt_r2b_a3_con_codigo_HEAD.txt")"
python3 -I -B "$H/control_negativo_a3.py" "$M/selftest_prompt_r2b_HEAD_sobre_HEAD.txt" "$M/selftest_prompt_r2b_a3.txt" "$M/selftest_prompt_r2b_a3_con_codigo_HEAD.txt" "$M/control_negativo_selftest_prompt_r2b_a3.json" > /dev/null
log "$(python3 -I -B -c "import json,sys; d=json.load(open(sys.argv[1])); print('exactamente el caso nuevo', d['exactamente_el_caso_nuevo'], '| totales', d['head_sobre_head'], d['a3_sobre_su_copia'], d['a3_con_codigo_head'], '| nuevos', len(d['casos_nuevos']), '| reescritos', len(d['casos_reescritos']), '| de HEAD que ya no están', len(d['de_head_que_ya_no_estan']), '| detalle con HEAD', d['detalle_del_fallo_con_head'])" "$M/control_negativo_selftest_prompt_r2b_a3.json")"
rm -rf "$T/control_candado"; cp -cR "$CH" "$T/control_candado"; cp "$CA/$DER" "$T/control_candado/$DER"
(cd "$T/control_candado" && "$PY" -B -c "import sys; sys.path.insert(0, 'data/experiment/reextraccion_v2/e1_extractor'); import prompt_r2b" > "$M/candado_del_derivado_con_codigo_HEAD.txt" 2>&1); log "control del candado del derivado (prompt_r2b de HEAD con el derivado de A3) rc=$? $(tail -1 "$M/candado_del_derivado_con_codigo_HEAD.txt")"
foto selftest_prompt_r2b

log "--- 4. corrida en seco por el camino del runner (criterios 1 a 3 y 10): HEAD y A3, en las tres tandas y la fixture"
"$PY" -B "$H/mensajes_runner_a3.py" --raiz "$CH" --e0 "$E0" --lista "$CH/$LISTA" --tanda-final "$CH/$TF" --salida "$M/seco" --etiqueta head > /dev/null; log "head rc=$?"
"$PY" -B "$H/mensajes_runner_a3.py" --raiz "$CA" --e0 "$E0" --lista "$CA/$LISTA" --tanda-final "$CA/$TF" --salida "$M/seco" --etiqueta a3 > /dev/null; log "a3 rc=$?"
for e in head a3; do log "$e: $(python3 -I -B -c "import json,sys; d=json.load(open(sys.argv[1])); print('prompt_r2b', d['prompt_r2b'], '| derivado', d['derivado_en_el_modulo'], d['derivado_sha256_en_el_modulo'][:12], '| tanda 0', d['tanda0_unidades'], d['tanda0_sha256_mensajes'][:12], '| tanda 1', d['tanda1_unidades'], len(d['tanda1_tos']), 'TOs | tanda final', d['tandafinal_unidades'], len(d['tandafinal_tos']), 'TOs | fixture', d['fixture_unidades'], d['fixture_sha256_mensajes'][:12], '| manifiesto de la tanda 1 carga', d['manifiesto_tanda1_carga_con_sus_20'], '| ajenos', d['modulos_de_data_experiment_fuera_de_la_copia'])" "$M/seco/resumen_$e.json")"; done
"$PY" -B "$H/comparar_a3.py" "$M/seco" "$CA" "$CA/$LISTA" "$CA/$TF" "$CH/$DER" "$CA/$DER" "$M/reporte_derivado_corrida1.json" "$M/medicion_a3.json" > "$M/comparacion_consola.txt"; log "comparación rc=$?"
tee -a "$L" < "$M/comparacion_consola.txt" > /dev/null
foto corrida_en_seco

log "--- 5. selftest_clave_cache --salida-r2b (criterio 6): HEAD, y A3 en dos corridas"
CC="data/experiment/mantenimiento/code/selftest_clave_cache.py"; SR="data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b"
(cd "$CH" && "$PY" -B $CC --salida-r2b $SR --out "$M/selftest_clave_cache_head.json" > "$M/consola_clave_cache_head.txt" 2>&1); log "head rc=$? $(tail -1 "$M/consola_clave_cache_head.txt")"
for i in 1 2; do
  (cd "$CA" && "$PY" -B $CC --salida-r2b $SR --out "$M/selftest_clave_cache_a3_$i.json" > "$M/consola_clave_cache_a3_$i.txt" 2>&1); log "a3 corrida $i rc=$? $(tail -1 "$M/consola_clave_cache_a3_$i.txt")"
done
igual "$M/selftest_clave_cache_head.json" "$CH/data/experiment/mantenimiento/selftest_clave_cache.json" "selftest_clave_cache de HEAD y el JSON de la base"
# Las cuentas de claves de la caché (campos «claves_db…») incluyen las llamadas de la tanda 1: se comparan sin mirarlas.
log "HEAD y el JSON de la base, $(python3 -I -B "$H/clave_cache_sin_cuentas_a3.py" comparar "$CH/data/experiment/mantenimiento/selftest_clave_cache.json" "$M/selftest_clave_cache_head.json")"
igual "$M/selftest_clave_cache_head.json" "$M/selftest_clave_cache_a3_1.json" "selftest_clave_cache de HEAD y de A3 (corrida 1)"
igual "$M/consola_clave_cache_head.txt" "$M/consola_clave_cache_a3_1.txt" "consolas de selftest_clave_cache de HEAD y de A3 (corrida 1)"
igual "$M/selftest_clave_cache_a3_1.json" "$M/selftest_clave_cache_a3_2.json" "selftest_clave_cache de A3, corridas 1 y 2"
igual "$M/consola_clave_cache_a3_1.txt" "$M/consola_clave_cache_a3_2.txt" "consolas de selftest_clave_cache de A3, corridas 1 y 2"
log "$(python3 -I -B -c "
import json,sys
h=json.load(open(sys.argv[1])); n=json.load(open(sys.argv[2]))
vh, vn = h['perfil_r2b']['variaciones'], n['perfil_r2b']['variaciones']
print('variaciones r2b', len(vh), '->', len(vn), '| nuevas', [v['id'] for v in vn if v['id'] not in {x['id'] for x in vh}],
      '| A1r igual', h['perfil_r2b']['anclaje']['e1']==n['perfil_r2b']['anclaje']['e1'], n['perfil_r2b']['anclaje']['e1']['estado'],
      '| A3r igual', h['perfil_r2b']['anclaje']['e3']==n['perfil_r2b']['anclaje']['e3'], n['perfil_r2b']['anclaje']['e3'].get('estado'),
      '| tokens iguales', [(v['id'],v['e1']['token'],v['e3']['token']) for v in vh]==[(v['id'],v['e1']['token'],v['e3']['token']) for v in vn],
      '| contraste', n['contraste_tabla']['estado'], len(n['contraste_tabla']['filas']), 'filas', '| veredicto', h['veredicto'], '->', n['veredicto'])
" "$M/selftest_clave_cache_head.json" "$M/selftest_clave_cache_a3_1.json")"
log "HEAD y A3 (corrida 1), $(python3 -I -B "$H/clave_cache_sin_cuentas_a3.py" comparar "$M/selftest_clave_cache_head.json" "$M/selftest_clave_cache_a3_1.json")"
foto selftest_clave_cache

log "--- 6. los vecinos sobre las dos copias (criterio 7); selftest_catalogo_unico con el .git del repo en solo lectura"
for e in head a3; do
  (cd "$T/copia_$e" && GIT_DIR="$R/.git" GIT_OPTIONAL_LOCKS=0 "$PY" -B data/experiment/catalogo_unico/code/selftest_catalogo_unico.py > "$M/selftest_catalogo_unico_$e.txt" 2>&1); log "catalogo_unico $e rc=$? $(tail -1 "$M/selftest_catalogo_unico_$e.txt")"
  (cd "$T/copia_$e" && "$PY" -B data/experiment/reresolucion_catalogo/selftest_reresolver_catalogo.py > "$M/selftest_reresolver_catalogo_$e.txt" 2>&1); log "reresolver_catalogo $e rc=$? $(tail -1 "$M/selftest_reresolver_catalogo_$e.txt")"
  (cd "$T/copia_$e" && "$PY" -B data/experiment/reextraccion_v2/selftest_cablev3.py > "$M/selftest_cablev3_$e.txt" 2>&1); log "cablev3 $e rc=$? $(tail -1 "$M/selftest_cablev3_$e.txt")"
  (cd "$T/copia_$e" && "$PY" -B data/experiment/reextraccion_v2/selftest_manifiesto.py > "$M/selftest_manifiesto_$e.txt" 2>&1); log "manifiesto $e rc=$? $(tail -1 "$M/selftest_manifiesto_$e.txt")"
done
for s in catalogo_unico reresolver_catalogo cablev3 manifiesto; do igual "$M/selftest_${s}_head.txt" "$M/selftest_${s}_a3.txt" "selftest_$s, consola de HEAD y de A3"; done
for e in head a3; do log "selftest_manifiesto $e, los fallos (los de P5 fuera de la raíz del repo, CLAUDE.md §4.l): $(grep -c 'FALLO' "$M/selftest_manifiesto_$e.txt") renglones con FALLO, $(grep -c 'FALLO P5 paridad E2 .*reporte=False' "$M/selftest_manifiesto_$e.txt") de P5 con reporte=False"; done
foto vecinos

log "--- 7. la E0 regenerada: el control contra S0-6b, y la lista que regenera contra la commiteada"
log "$(python3 -I -B -c "import json,sys; d=json.load(open(sys.argv[1])); print({k: d[k] for k in d if not isinstance(d[k], (list, dict))})" "$T/e0t/control_e0_S2a.json" 2>&1 | cut -c1-600)"
python3 -I -B "$CH/data/experiment/alcance_e1/a2/scripts/comparar_lista_a2.py" "$T/e0t/lista_tanda1_S2.json" "$CH/$LISTA" "$M/comparacion_lista_tanda1_a3.json" | tee -a "$L"
"$PY" -B "$H/cadena_78_a3.py" "$R" $BASE "$CH" "$CA" "$M/cadena_78_a3.json" > /dev/null; log "las 78 rutas de la cadena rc=$? $(python3 -I -B -c "import json,sys; d=json.load(open(sys.argv[1])); print('copia_head igual a la base en las 78:', d['copia_head_igual_a_la_base_en_las_78'], '| cambian con A3:', d['cambian_con_a3'], '| en la base, distintas del sello de 47c9f1b3:', d['en_la_base_distintas_del_sellado'])" "$M/cadena_78_a3.json")"
foto e0_y_cadena

log "archivos de .git más nuevos que la marca del inicio: $(find "$R/.git" -type f -newer "$M/marca_git_antes" | wc -l | tr -d ' ')"
log "git status --porcelain --untracked-files=no del repo: [$(git --no-optional-locks -C "$R" status --porcelain --untracked-files=no | tr '\n' ' ')]"
log "HEAD al final: $(git --no-optional-locks -C "$R" rev-parse HEAD)"
log "fin $(date '+%Y-%m-%d %H:%M:%S %z')"
