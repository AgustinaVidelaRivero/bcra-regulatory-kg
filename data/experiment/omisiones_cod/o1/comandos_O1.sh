#!/bin/bash
# U-OMISIONES-COD, O1: los comandos de la medición previa y de la prueba en seco, en el orden en que corrieron (09/10/2026).
# USD 0, sin API. <repo> es la raíz del repo; <S> el scratchpad; PY=<repo>/.venv/bin/python. Ningún comando escribe en el
# repo: las copias se arman con rsync (sin .git, sin .venv, sin enlaces) y todo lo demás escribe en <S>.
set -eu
PY="<repo>/.venv/bin/python"; S="<S>"; SC="$S/o1/scripts"
# 0. foto del repo (antes y después) y .pyc
python3 -I $SC/foto_repo.py <repo> $S/foto/antes.tsv
# 1. copias: la de HEAD y la del código de O1 (= la de HEAD + parche/parche_O1_completo.diff)
rsync -a --copy-links --exclude='/.git/' --exclude='/.venv/' <repo>/ $S/copia/
rsync -a $S/copia/ $S/copia_o2/ && (cd $S/copia_o2 && patch -p1 < $S/o1/parche/parche_O1_completo.diff)
# (en O1 el código se escribió directo en copia_o2; el parche, aplicado así sobre los archivos de HEAD, da los mismos archivos)
# 2. cadenas r2b de diez (con y sin cola): HEAD y cada etapa acumulada (B; B+C+L; +G-r; +H; completa); y las otras cuatro
$SC/cadenas_base_head.sh $PY $S/copia $S/base_head
$SC/cadenas_base_head.sh $PY $S/copia_o2 $S/etapas/TODO
$SC/cadenas_otras.sh $PY $S/copia_o2 $S/etapas/TODO_otras
$SC/cadenas_otras.sh $PY $S/copia $S/base_head_otras
# 3. mediciones (desde la raíz de la copia que corresponde)
(cd $S/copia && $PY -B $SC/medir_grupo_A.py --out $S/o1/salidas/grupo_A.json)
(cd $S/copia && $PY -B $SC/medir_e.py --modo calibrar --out $S/o1/salidas/e_calibracion_T4.json)
(cd $S/copia && $PY -B $SC/medir_e.py --modo lista --variante "ventana3+flexion" --out $S/o1/salidas/e_lista_sellada/detecciones_e_copia_nota_diez.json)
python3 -B $SC/medir_grupo_B.py $S/base_head/r2b_diez/r2 $S/etapas/B/r2b_diez/r2 --out $S/o1/salidas/grupo_B_diez.json
(cd $S/copia_o2 && $PY -B $SC/medir_grupos_C_L.py $S/etapas/B/r2b_diez/r2 $S/etapas/BCL/r2b_diez/r2 --out $S/o1/salidas/grupos_C_L_diez.json --premedicion-L <premedicion_tramo_e1_mesa.json> --detector $S/copia_o2/data/experiment/pyd_r2/code)
python3 -B $SC/medir_J_A_h_K.py $S/etapas/BCLGH/r2b_diez/r2 $S/etapas/TODO/r2b_diez/r2 --out $S/o1/salidas/J_A_h_K_diez.json
python3 -B $SC/medir_h_i.py --kg a9631a64=<ens_diez_r2b/r2/kg.json> --kg nuevo_diez=$S/etapas/TODO/r2b_diez/r2/kg.json --out $S/o1/salidas/h_i.json
python3 -B $SC/medir_I.py --kg r2b_diez_a9631a64=<ens_diez_r2b/r2/kg.json> --out $S/o1/salidas/I_condiciones.json
python3 -B $SC/diff_grafos.py <dir antes> <dir después> --out $S/o1/salidas/diff_<etapa>.json
# 4. prueba en seco: casos de la v7, suite y shapes, selftests, fichas del lote 1, métricas gen 3, límites
(cd $S/copia_o2 && $PY -B $SC/casos_v7.py --head $S/base_head/r2b_diez/r2 --nuevo $S/etapas/TODO/r2b_diez/r2 --nuevo-sincola $S/etapas/TODO/r2b_sincola_diez/r2 --out $S/o1/salidas/casos_v7.json)
(cd $S/copia_o2 && $PY -B $SC/suite_y_shapes.py --par diez=... --par sincola_diez=... --par desarrollo=... --par sincola_desarrollo=... --out-dir $S/o1/salidas/suite_shapes)
$SC/bateria_selftests.sh $PY $S/copia $S/o1/salidas/selftests_head $SC
$SC/bateria_selftests.sh $PY $S/copia_o2 $S/o1/salidas/selftests_nuevo $SC
(cd $S/copia_o2 && GIT_DIR=<repo>/.git GIT_OPTIONAL_LOCKS=0 $PY -B data/experiment/catalogo_unico/code/selftest_catalogo_unico.py)
(cd $S/copia_o2 && $PY -B $SC/fichas_lote1_L.py --referencia $S/copia/data/experiment/med_umbrales/p/lote1 --salida $S/o1/salidas/fichas_L/e22fae1a)
(cd $S/copia_o2 && $PY -B $SC/fichas_lote1_L.py --referencia $S/copia/data/experiment/med_umbrales/p/lote1 --salida $S/o1/salidas/fichas_L/sincola_BCL --kg $S/etapas/BCL/r2b_sincola_diez/r2/kg.json)
(cd $S/copia_o2 && $PY -B scripts/metricas_intrinsecas.py --gen3 --kg <kg> --nombre I_<grafo> --e0 <e0> --out-dir $S/o1/salidas/I_gen3)
(cd $S/copia_o2 && $PY -B $SC/limites_O1.py --salidas $S/o1/salidas --nuevo $S/etapas/TODO/r2b_diez/r2 --head $S/base_head/r2b_diez/r2 --out $S/o1/salidas/limites_O1.json)
python3 -B $SC/limites_md.py $S/o1/salidas $S/o1/limites_O1.md
