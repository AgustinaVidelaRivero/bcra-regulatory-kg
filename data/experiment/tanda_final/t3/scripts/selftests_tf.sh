#!/bin/zsh
# B6.1, tanda final, T3, punto 4: los selftests de la cadena, los del gate final del laudo
# (data/experiment/laudo_release_r2/gate_final/gate_final_laudo_r2_mesa.sh:60-72), con data/experiment/tanda1/t3/scripts/selftests_t3.sh
# copiado, sobre un clon de la copia (nunca el repo): pueden reescribir archivos. USD 0, sin API. Dos cambios, por lo que aprendió el T3
# de la tanda 1:
#   - el de claves (selftest_clave_cache) no corre acá: cuenta las claves de las bases de la caché, bajo el cegamiento, y corre aparte,
#     con su salida a archivos y el retiro de cuentas de A3 (selftest_claves_sin_cuentas_tf.py; registro de decisiones, §38);
#   - el del catálogo pide `git show 4ef7650:<ruta>` (derivar_catalogo_r2.py:103): corre con GIT_DIR en el .git del repo, que git solo
#     lee con `show` (GIT_OPTIONAL_LOCKS=0), en lugar de un `git clone`, que trae archivos `.env` y `NO_ABRIR_` (error propio 1 del
#     parcial de la tanda 1).
# Uso: zsh selftests_tf.sh <python del repo> <clon> <dir de salida> <.git del repo>
set -u
PY="$1"; C="$2"; S="$3"; G="$4"; mkdir -p "$S"
export PYTHONDONTWRITEBYTECODE=1; unset ANTHROPIC_API_KEY
st() { local n="$1"; shift; ( cd "$C" && print -r -- "inicio $(date '+%Y-%m-%d %H:%M:%S')" > "$S/$n.txt" && "$PY" -B "$@" >> "$S/$n.txt" 2>&1; print -r -- "rc=$?" >> "$S/$n.txt"; print -r -- "fin $(date '+%Y-%m-%d %H:%M:%S')" >> "$S/$n.txt" ); }
st regression_kg_1 scripts/selftest_regression_kg.py
st regression_kg_2 scripts/selftest_regression_kg.py
st shapes_congelado scripts/selftest_shapes_congelado.py
st pyd_r2 data/experiment/pyd_r2/code/selftest_pyd_r2.py
st r3 data/experiment/r2_codigo/selftest_r3.py
st ensamblado_omisiones data/experiment/omisiones_cod/selftest_ensamblado_omisiones.py
st metrica_condiciones data/experiment/omisiones_cod/selftest_metrica_condiciones.py
( export GIT_DIR="$G" GIT_OPTIONAL_LOCKS=0; st catalogo_unico data/experiment/catalogo_unico/code/selftest_catalogo_unico.py )
st e0 data/experiment/reextraccion_v2/e0_chunking/selftest_e0.py
print -r -- "fin del lote $(date '+%Y-%m-%d %H:%M:%S')" > "$S/fin.txt"
