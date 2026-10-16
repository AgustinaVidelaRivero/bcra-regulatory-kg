#!/bin/zsh
# Mesa, §120: el gate final del laudo de la release r2 (laudo, §3), sobre una copia nueva del repo y con el código de HEAD. USD 0, sin
# API, nunca EV2. Decisión 2 de la autora del 15/10/2026 (§115): la mesa lo corre sobre copias, sin turno en el repo.
# Los pasos y los argumentos son los del re-sellado único (paquete revision_URESELLADO_T0: cadena_rs1.sh y gate_rs1.sh), sin cambios:
#   1. las cuatro cadenas r2b re-selladas, dos veces cada una, y las dos r2a, una vez;
#   2. shapes (perfil r2, fase r2b) y suite (perfil r2, con la fixture de HEAD) sobre los cuatro de la primera corrida;
#   3. métricas intrínsecas (--gen3) sobre los cuatro;
#   4. los selftests de la cadena y el de claves.
# Uso: zsh <este> <repo> <trabajo nuevo> <python del repo> <herramienta de foto>
set -u
R="$1"; W="$2"; PY="$3"; FOTO="$4"
[ ! -e "$W" ] || { echo "el trabajo ya existe"; exit 1; }
mkdir -p "$W"; C="$W/copia"; L="$W/consolas"; mkdir -p "$L"
export PYTHONDONTWRITEBYTECODE=1; unset ANTHROPIC_API_KEY
paso() { print -r -- "$1 $(date '+%Y-%m-%d %H:%M:%S')" >> "$W/tiempos.txt"; }
paso "foto antes"; python3 -I -B "$FOTO" "$R" "$W/foto_antes.json" > /dev/null
paso "HEAD"; git -C "$R" --no-optional-locks rev-parse HEAD > "$W/head.txt"
paso "copia"
rsync -a --no-links --exclude=/.git --exclude=/.venv --exclude=/.venv-app --exclude=.DS_Store --exclude=__pycache__ \
  --exclude='.env' --exclude='.env.*' --exclude='*.env' --exclude='NO_ABRIR_*' --exclude=/data/experiment/neo4j/volumen "$R/" "$C/"
print -r -- "por nombre: $(find "$C" \( -name '.env' -o -name '.env.*' -o -name '*.env' -o -name 'NO_ABRIR_*' \) | wc -l | tr -d ' ')" >> "$W/tiempos.txt"
print -r -- "enlaces: $(find "$C" -type l | wc -l | tr -d ' ')" >> "$W/tiempos.txt"
X=data/experiment/reextraccion_v2; T=$X/corpus_tanda0; MAN=$X/manifiestos
E0A=$X/e0_chunking/salida_tanda0_r2; E0B=$X/e0_chunking/salida_tanda0_r2b
ENS=data/experiment/tanda0/code/ensamblar_tanda0.py
args_de() {
  case "$1" in
    r2b_diez)               print -r -- "--manifiesto $MAN/tanda0_ens_diez_r2b_rs1.json --entrada $T/salida_r2b --e0-r2 $E0B" ;;
    r2b_sincola_diez)       print -r -- "--manifiesto $MAN/tanda0_ens_diez_r2b_sincola_rs1.json --entrada $T/salida_r2b --e0-r2 $E0B --sin-cola" ;;
    r2b_desarrollo)         print -r -- "--manifiesto $MAN/tanda0_ens_desarrollo_r2b_rs1.json --entrada $T/salida_r2b --e0-r2 $E0B" ;;
    r2b_sincola_desarrollo) print -r -- "--manifiesto $MAN/tanda0_ens_desarrollo_r2b_sincola_rs1.json --entrada $T/salida_r2b --e0-r2 $E0B --sin-cola" ;;
    r2a_diez)               print -r -- "--manifiesto $MAN/tanda0_ens_diez.json --entrada $T/salida_dirigida --e0-r2 $E0A --perfil-r2" ;;
    r2a_desarrollo)         print -r -- "--manifiesto $MAN/tanda0_ens_desarrollo.json --entrada $T/salida_dirigida --e0-r2 $E0A --perfil-r2" ;;
  esac
}
cadena() {  # <grafo> <salida absoluta> <consola>
  ( cd "$C" && { print -r -- "inicio $(date '+%Y-%m-%d %H:%M:%S') grafo=$1"; "$PY" -B $ENS ${=$(args_de "$1")} --salida "$2"; print -r -- "rc=$?"; print -r -- "fin $(date '+%Y-%m-%d %H:%M:%S')"; } > "$3" 2>&1 )
}
paso "cadenas, primera corrida y r2a"
for g in r2b_diez r2b_sincola_diez r2b_desarrollo r2b_sincola_desarrollo; do cadena $g "$W/run1/$g" "$L/run1_$g.txt" & done; wait
for g in r2a_diez r2a_desarrollo; do cadena $g "$W/r2a/$g" "$L/r2a_$g.txt" & done
paso "cadenas, segunda corrida"
for g in r2b_diez r2b_sincola_diez r2b_desarrollo r2b_sincola_desarrollo; do cadena $g "$W/run2/$g" "$L/run2_$g.txt" & done; wait
paso "shapes y suite"
EXC=data/experiment/catalogo_unico/generados_r2/entrada_esqueleto_r2.json
CAT=data/experiment/catalogo_unico/generados_r2/catalogo_suite_r2.json
for g in r2b_diez r2b_sincola_diez r2b_desarrollo r2b_sincola_desarrollo; do
  N="$W/run1/$g"; O="$W/gate/$g"; mkdir -p "$O"
  ( cd "$C" && "$PY" -B scripts/shapes_validator.py --kg "$N/r2/kg.json" --perfil r2 --fase r2b --e0 $E0B --registro-dir "$N/r2" \
      --excepciones $EXC --out "$O/shapes_perfil_r2_fase_r2b.md" > "$O/consola_shapes.txt" 2>&1; print -r -- "rc=$?" >> "$O/consola_shapes.txt" )
  ( cd "$C" && "$PY" -B scripts/regression_kg.py --kg "$N/r2/kg.json" --perfil r2 --generacion 3 --catalogo $CAT \
      --politica-cuarentena flaggeada --registro-dir "$N/r2" --esperado scripts/regression_kg_esperado.json \
      --out "$O/suite_perfil_r2.md" > "$O/consola_suite.txt" 2>&1; print -r -- "rc=$?" >> "$O/consola_suite.txt" )
done
paso "métricas intrínsecas"
for g in r2b_diez r2b_sincola_diez r2b_desarrollo r2b_sincola_desarrollo; do
  O="$W/metricas/$g"; mkdir -p "$O"
  ( cd "$C" && "$PY" -B scripts/metricas_intrinsecas.py --gen3 --kg "$W/run1/$g/r2/kg.json" --nombre "gate_final_$g" --e0 $E0B --out-dir "$O" > "$O/consola.txt" 2>&1; print -r -- "rc=$?" >> "$O/consola.txt" )
done
paso "selftests"
S="$W/selftests"; mkdir -p "$S"
st() { local n="$1"; shift; ( cd "$C" && "$PY" -B "$@" > "$S/$n.txt" 2>&1; print -r -- "rc=$?" >> "$S/$n.txt" ); }
st regression_kg_1 scripts/selftest_regression_kg.py
st regression_kg_2 scripts/selftest_regression_kg.py
st shapes_congelado scripts/selftest_shapes_congelado.py
st clave_cache data/experiment/mantenimiento/code/selftest_clave_cache.py --out "$S/selftest_clave_cache_gate_final.json"
st pyd_r2 data/experiment/pyd_r2/code/selftest_pyd_r2.py
st r3 data/experiment/r2_codigo/selftest_r3.py
st ensamblado_omisiones data/experiment/omisiones_cod/selftest_ensamblado_omisiones.py
st metrica_condiciones data/experiment/omisiones_cod/selftest_metrica_condiciones.py
st catalogo_unico data/experiment/catalogo_unico/code/selftest_catalogo_unico.py
st e0 data/experiment/reextraccion_v2/e0_chunking/selftest_e0.py
paso "foto después"; python3 -I -B "$FOTO" "$R" "$W/foto_despues.json" > /dev/null
python3 -I -B "$FOTO" --comparar "$W/foto_antes.json" "$W/foto_despues.json" > "$W/comparacion_foto.json"
paso "fin"
