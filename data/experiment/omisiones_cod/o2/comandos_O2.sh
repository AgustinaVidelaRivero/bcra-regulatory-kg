#!/bin/bash
# U-OMISIONES-COD, O2: los comandos de la implementación y sus controles, en el orden en que corrieron (10/10/2026). USD 0, sin
# API. <repo> es la raíz del repo; <S> el scratchpad; PY=<repo>/.venv/bin/python; SC=<S>/o2/scripts (= o2/scripts de acá).
# Ninguna corrida escribe en el repo salvo el paso 9 (las escrituras autorizadas) y la carpeta o2/. Las copias se arman con
# rsync (sin .git, sin .venv, sin enlaces) o con clones de APFS (cp -c), y todo lo demás escribe en <S>.
set -eu
PY="<repo>/.venv/bin/python"; S="<S>"; SC="$S/o2/scripts"; O1="<repo>/data/experiment/omisiones_cod/o1"
# 0. entrada: commits, texto firmado, archivos base, foto y .pyc
git -C <repo> log --oneline -8
for c in c90d3d9 3c5f003 521e220 HEAD; do git -C <repo> show "$c:docs/mandatos/UOMISIONES_COD_release_codigo_ensamblado.md" | sed '/^## Firma$/,$d' | shasum -a 256; done
python3 -I $SC/foto_repo.py <repo> $S/o2/foto/antes.tsv          # 49.173 archivos, 07:56:39–07:56:50
find <repo> -path <repo>/.venv -prune -o -name '*.pyc' -print | sort > $S/o2/foto/pyc_antes.txt   # 2.213
# 1. copias (del árbol de trabajo, que trae el código de E0 de S0-5b sin commit, el mismo en todas)
rsync -a --copy-links --exclude='/.git/' --exclude='/.venv/' <repo>/ $S/c2_head/
rsync -a $S/c2_head/ $S/c2_o2/ && (cd $S/c2_o2 && patch -p1 < $O1/parche/parche_O1_completo.diff)
# (el código de O2 se escribió directo en c2_o2: es parche/parche_O2_sobre_O1.diff)
rsync -a $S/c2_o2/ $S/c2_e/ && (cd $S/c2_e && patch -p1 < pieza_e/parche_pieza_e_sobre_O2.diff)
cp -cR $S/c2_o2 $S/c2_sinJ && sed -i '' 's/procedencia_propia=r2b, agrupar_sin_rol=r2b/procedencia_propia=False, agrupar_sin_rol=r2b/' \
  $S/c2_sinJ/data/experiment/tanda0/code/ensamblar_tanda0.py
# 2. cadenas (el ensamblado no corre E0: lee salida_tanda0_r2b/ y salida_tanda0_r2/)
$SC/cadenas_base_head.sh $PY $S/c2_head $S/o2/corridas/head
$SC/cadenas_desarrollo_head.sh $PY $S/c2_head $S/o2/corridas/head
$SC/cadenas_base_head.sh $PY $S/c2_o2 $S/o2/corridas/o2_1 && $SC/cadenas_otras.sh $PY $S/c2_o2 $S/o2/corridas/o2_1
$SC/cadenas_r2b_cuatro.sh $PY $S/c2_o2 $S/o2/corridas/o2_2          # segunda corrida, en otro proceso
(cd $S/c2_e && $PY -B data/experiment/tanda0/code/ensamblar_tanda0.py --manifiesto data/experiment/reextraccion_v2/manifiestos/tanda0_ens_diez_r2b.json \
  --entrada data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b --e0-r2 data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b \
  --salida $S/o2/corridas/pieza_e/r2b_diez > $S/o2/corridas/pieza_e/consola_r2b_diez.txt 2>&1)
$SC/cadenas_base_head.sh $PY $S/c2_sinJ $S/o2/corridas/sin_J && $SC/cadenas_desarrollo_head.sh $PY $S/c2_sinJ $S/o2/corridas/sin_J
# 3. controles de las cadenas y de E0
python3 -I $SC/cadenas_y_doble_corrida.py $S/o2/corridas --tsv salidas/cadenas_sha256.tsv --out salidas/doble_corrida.json
#    salida de la tanda 0 de E0 en c2_head, c2_o2 y c2_e contra el repo (diff -rq) y el código de E0 de cada copia: salidas/e0_tanda0_en_las_copias.txt
# 4. el diff declarado y los registros (G = r2b_diez, r2b_sincola_diez, r2b_desarrollo, r2b_sincola_desarrollo)
for G in r2b_diez r2b_sincola_diez r2b_desarrollo r2b_sincola_desarrollo; do
  python3 -I $SC/diff_declarado.py $S/o2/corridas/head/$G/r2 $S/o2/corridas/o2_1/$G/r2 --out $S/o2/salidas/diff_declarado_$G.json
  python3 -I $SC/registros_declarados.py $S/o2/corridas/head/$G/r2 $S/o2/corridas/o2_1/$G/r2 --out salidas/registros_declarados_$G.json
  python3 -I $SC/j_aislado.py $S/o2/corridas/sin_J/$G/r2 $S/o2/corridas/o2_1/$G/r2 --out salidas/j_aislado_$G.json
  python3 -I $SC/j_descomposicion.py $S/o2/salidas/diff_declarado_$G.json salidas/j_aislado_$G.json $S/o2/corridas/head/$G/r2 \
    $S/o2/corridas/sin_J/$G/r2 --out salidas/j_descomposicion_$G.json
  python3 -I $SC/diff_final.py $S/o2/salidas/diff_declarado_$G.json salidas/j_descomposicion_$G.json --out salidas/diff_declarado_$G.json
  # O1 = las salidas de la cadena con el código de O1 (HEAD + o1/parche/parche_O1_completo.diff), las de O1: etapas/TODO y TODO_otras
  python3 -I $SC/remite_a_caso_por_caso.py $S/o2/corridas/head/$G/r2 <salida O1 de $G>/r2 $S/o2/corridas/o2_1/$G/r2 --out salidas/remite_a_caso_por_caso_$G.json
done
# (las versiones del repo de j_aislado y j_descomposicion llevan los conteos; sus listas por arista están en diff_declarado_<G>.json)
# 5. medidas sobre la tanda 0, (h) e (i), límites
python3 -B $SC/medidas_tanda0_O2.py --grafo diez=$S/o2/corridas/o2_1/r2b_diez/r2 --grafo diez_sin_cola=$S/o2/corridas/o2_1/r2b_sincola_diez/r2 \
  --grafo desarrollo=$S/o2/corridas/o2_1/r2b_desarrollo/r2 --grafo desarrollo_sin_cola=$S/o2/corridas/o2_1/r2b_sincola_desarrollo/r2 --out salidas/medidas_tanda0_O2.json
python3 -I $SC/medir_h_i.py --kg sellado_diez=<ens_diez_r2b/r2/kg.json> --kg head_diez=... --kg o2_diez=... (los doce: sellado, HEAD y O2 de los cuatro) --out salidas/h_i_sellado_head_O2.json
(cd $S/c2_o2 && $PY -B $O1/scripts/limites_O1.py --salidas <copia de o1/salidas> --nuevo $S/o2/corridas/o2_1/r2b_diez/r2 --head $S/o2/corridas/head/r2b_diez/r2 --out salidas/limites_O2.json)
python3 -I -B $SC/limites_C_O2.py $S/o2/corridas/head/r2b_diez/r2 $S/o2/corridas/o2_1/r2b_diez/r2 --o1-scripts $O1/scripts --out salidas/limites_C_O2_diez.json
python3 -I $SC/limites_md_O2.py salidas limites_O2.md
# 6. suite y shapes, selftests, fichas, pieza (e)
M=data/experiment/reextraccion_v2/manifiestos; H=$S/o2/corridas/head; N=$S/o2/corridas/o2_1
(cd $S/c2_o2 && $PY -B $SC/suite_y_shapes.py --par diez=$H/r2b_diez/r2,$N/r2b_diez/r2,$M/tanda0_ens_diez_r2b.json \
  --par sincola_diez=$H/r2b_sincola_diez/r2,$N/r2b_sincola_diez/r2,$M/tanda0_ens_diez_r2b_sincola.json \
  --par desarrollo=$H/r2b_desarrollo/r2,$N/r2b_desarrollo/r2,$M/tanda0_ens_desarrollo_r2b.json \
  --par sincola_desarrollo=$H/r2b_sincola_desarrollo/r2,$N/r2b_sincola_desarrollo/r2,$M/tanda0_ens_desarrollo_r2b_sincola.json --out-dir salidas/suite_shapes)
$SC/bateria_selftests_O2.sh $PY $S/c2_head salidas/selftests_head $SC <repo>/.git
$SC/bateria_selftests_O2.sh $PY $S/c2_o2 salidas/selftests_nuevo $SC <repo>/.git $N/r2b_diez/r2 $N/r2b_sincola_diez/r2
(cd $S/c2_o2 && $PY -B data/experiment/mantenimiento/code/selftest_clave_cache.py --out salidas/selftests_nuevo/selftest_clave_cache_tabla_combinada.json)   # con la tabla final
REF=$S/c2_head/data/experiment/med_umbrales/p/lote1
(cd $S/c2_o2 && $PY -B $SC/fichas_lote1_L.py --referencia $REF --salida salidas/fichas_L/e22fae1a)
(cd $S/c2_o2 && $PY -B $SC/fichas_lote1_L.py --referencia $REF --salida salidas/fichas_L/sincola_O2 --kg $N/r2b_sincola_diez/r2/kg.json)
(cd $S/c2_e && $PY -B pieza_e/selftest_pieza_e.py --salida-r2 $S/o2/corridas/pieza_e/r2b_diez/r2 --lista-sellada $O1/salidas/e_lista_sellada/detecciones_e_copia_nota_diez.json)
(cd $S/c2_o2 && $PY -B pieza_e/selftest_pieza_e.py)                 # sin la pieza: rc=2
# 7. la tabla de reprocesamiento: anclas por texto y la combinación con el cambio de las 08:02:39 de otra sesión
python3 $SC/anclas_tabla.py $S/c2_head $S/c2_o2
git merge-file -p <tabla de c2_o2> <tabla de HEAD> <tabla del árbol a las 08:02:39> > tabla_merge.md   # un conflicto (F16 y F16b), resuelto con el lado de O2
# 8. parches: parche/ (HEAD → O2 y O1 → O2), con su control de aplicación sobre copias
# 9. escrituras en el repo (08:24:11): primero, cada archivo del repo igual a su base (c2_head; la tabla, a la del árbol); después
#    cp de los 14 archivos desde c2_o2 y cmp contra c2_o2
# 10. cierre: foto después, .pyc, grep de convenciones (sobre o2/ y las escrituras), paquete con su manifest y su copia permanente
