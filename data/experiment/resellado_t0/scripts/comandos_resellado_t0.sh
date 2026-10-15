#!/bin/bash
# Re-sellado único de los grafos r2b de la tanda 0 (mandato firmado el 15/10/2026, 67fe5b14): los comandos, en el orden en que
# corrieron el 15/10/2026. USD 0, sin API. <repo> es la raíz del repo; <S> el scratchpad; PY=<repo>/.venv/bin/python;
# SC=<S>/rs/scripts (= data/experiment/resellado_t0/scripts). Ningún generador corre sobre el repo: todo corre sobre la copia
# <S>/copia_rs (o sobre clones APFS de ella, cp -c) y escribe ahí o en <S>; el repo recibe después los mismos bytes (paso 12).
# La excepción es Neo4j: su base vive en <repo>/data/experiment/neo4j/volumen (fuera de git), y el contenedor se levanta
# desde ese directorio; el cargador corre desde la copia.
set -eu
PY="<repo>/.venv/bin/python"; S="<S>"; SC="$S/rs/scripts"; C="$S/copia_rs"; K="$S/rs/corridas"
T=data/experiment/reextraccion_v2/corpus_tanda0
# 0. texto firmado, paso 0 y precondiciones (salidas/paso0_y_precondiciones.txt)
(cd <repo> && bash $SC/paso0_precondiciones.sh)
# 1. foto del repo, .pyc y git status (los .env y los NO_ABRIR_ se registran sin abrir)
python3 -I -B $SC/foto_repo_rs1.py <repo> $S/rs/foto/foto_antes.json
# 2. la copia, con el rsync de la cláusula (más el volumen de Neo4j, que no es insumo de nada que corra en la copia)
rsync -a --no-links --exclude=/.git --exclude=/.venv --exclude=/.venv-app --exclude=.DS_Store --exclude=__pycache__ \
  --exclude='.env' --exclude='.env.*' --exclude='*.env' --exclude='NO_ABRIR_*' --exclude=/data/experiment/neo4j/volumen <repo>/ $C/
find $C \( -name '.env' -o -name '.env.*' -o -name '*.env' -o -name 'NO_ABRIR_*' \) | wc -l      # 0
find $C -type l | wc -l                                                                       # 0
python3 -I -B $SC/control_copia_vs_foto.py $S/rs/foto/foto_antes.json $C salidas/control_copia_vs_foto_antes.json
# 3. los cuatro manifiestos nuevos (decisión 1), en la copia
python3 -I -B $SC/manifiestos_rs1.py $C
# 4. las variantes de control: sin R0 (los 8 archivos de salida_r2b/ en 1d690df3) y, encima, sin O2 (el código en ded41d50^)
cp -cR $C $S/c_preR0
for f in ext/finales.jsonl ext/veredictos.jsonl ext/reintentos_e3.jsonl ext/cola_humana.jsonl ext/copias_nota_e3.jsonl \
         docvig/finales.jsonl docvig/veredictos.jsonl docvig/cola_humana.jsonl; do
  git -C <repo> show "1d690df3:$T/salida_r2b/$f" > "$S/c_preR0/$T/salida_r2b/$f"; done
cp -cR $S/c_preR0 $S/c_preO2
for f in data/experiment/pyd_r2/code/validador_r2.py data/experiment/reextraccion_v2/corpus_v2/r1_e4.py \
         data/experiment/reextraccion_v2/corpus_v2/r1_referencias.py data/experiment/tanda0/code/ensamblar_tanda0.py \
         data/experiment/pyd_r2/code/selftest_pyd_r2.py data/experiment/r2_codigo/selftest_r3.py scripts/metricas_intrinsecas.py \
         data/experiment/med_umbrales/p/code/comun_P.py data/experiment/med_umbrales/p/code/armador_fichas_P.py \
         data/experiment/med_umbrales/p/code/selftest_comparador_P.py; do
  git -C <repo> show "ded41d50^:$f" > "$S/c_preO2/$f"; done
# 5. las cadenas: la primera r2b de diez sola (para medir tiempo y memoria), después las otras 17 de a cuatro (xargs -P 4)
python3 -I -B $SC/foto_repo_rs1.py $C $S/rs/foto/foto_copia_antes_cadenas.json
$SC/cadena_rs1.sh $PY $C r2b_diez $T/ens_diez_r2b_rs1 $K/run1/consola_r2b_diez.txt
#    lote (una línea por corrida: copia, grafo, --salida, consola):
#    $C   r2b_sincola_diez | r2b_desarrollo | r2b_sincola_desarrollo   -> $T/ens_<g>_rs1            (primera corrida, en la copia)
#    $C   los cuatro r2b                                                -> $K/run2/<g>               (segunda corrida, otro proceso)
#    $C   r2a_diez | r2a_desarrollo                                     -> $K/r2a/<g>
#    $S/c_preR0  los cuatro r2b                                         -> $K/o2/<g>                 (O2: código ded41d50, sin R0)
#    $S/c_preO2  los cuatro r2b                                         -> $K/preO2/<g>              (antes de O2)
xargs -P 4 -L 1 $SC/cadena_rs1.sh $PY < lote_cadenas.txt
python3 -I -B $SC/doble_corrida_rs1.py $C $K salidas/doble_corrida_rs1.json salidas/cadenas_sha256_rs1.tsv
# 6. las unidades de R0, el diff contra O2 y el diff contra los sellados
python3 -I -B $SC/unidades_r0.py <repo> salidas/unidades_r0.json
for p in "r2b_diez ens_diez_r2b" "r2b_sincola_diez ens_diez_r2b_sincola" "r2b_desarrollo ens_desarrollo_r2b" \
         "r2b_sincola_desarrollo ens_desarrollo_r2b_sincola"; do set -- $p
  python3 -I -B $SC/diff_r0.py $K/o2/$1/r2 $C/$T/$2_rs1/r2 --unidades-r0 <lista de unidades_r0.json> \
    --out salidas/diff_contra_O2/diff_declarado_contra_O2_$1.json
  python3 -I -B $SC/diff_contra_sellado.py --s $C/$T/$2/r2 --p $K/preO2/$1/r2 --o $K/o2/$1/r2 --n $C/$T/$2_rs1/r2 \
    --diff-o2 $C/data/experiment/omisiones_cod/o2/salidas/diff_declarado_$1.json \
    --diff-r0 salidas/diff_contra_O2/diff_declarado_contra_O2_$1.json --out salidas/diff_contra_sellado/diff_declarado_contra_sellado_$1.json
done
# 7. la cola, la población de L2 y la línea de base del pre-registro (desde la copia; «antes» por git show de 1d690df3)
(cd $C && $PY -I -B $SC/cola_y_poblacion_rs1.py $C <repo> salidas/cola_y_poblacion_rs1.json)
# 8. shapes de los cuatro nuevos (salidas en su ensamblado, en la copia) y de los cuatro de O2; fixture, grafos.py y registro;
#    suite de los cuatro nuevos; tablas contra O2 y contra los sellados; selftests; corrida en seco
for g in diez_r2b diez_r2b_sincola desarrollo_r2b desarrollo_r2b_sincola; do $SC/gate_rs1.sh $PY $C $T/ens_${g}_rs1 $T/ens_${g}_rs1 shapes; done
python3 -I -B $SC/editar_fixture_grafos_rs1.py $C
for g in diez_r2b diez_r2b_sincola desarrollo_r2b desarrollo_r2b_sincola; do $SC/gate_rs1.sh $PY $C $T/ens_${g}_rs1 $T/ens_${g}_rs1 suite; done
for g in r2b_diez r2b_sincola_diez r2b_desarrollo r2b_sincola_desarrollo; do $SC/gate_rs1.sh $PY $C $K/o2/$g salidas/gate_o2/$g ambas; done
python3 -I -B $SC/tablas_gate_rs1.py --par diez=$C/$T/ens_diez_r2b_rs1,salidas/gate_o2/r2b_diez,$C/$T/ens_diez_r2b [...los otros tres] \
  --out salidas/tablas_gate_rs1.json
(cd $C && for i in 1 2; do $PY -B scripts/selftest_regression_kg.py; done; $PY -B scripts/selftest_shapes_congelado.py)
(cd $C && $PY -B $SC/dry_registro_rs1.py $C <git show HEAD de la fixture> <git show HEAD de grafos.py> --out salidas/dry_registro_copia.json)
# 9. los controles del §4: selftest de claves (A3r), U-CONF-MATRIZ, laudo B2.4 y condición 10; las figuras
(cd $C && $PY -B data/experiment/mantenimiento/code/selftest_clave_cache.py --out salidas/selftests/selftest_clave_cache_rs1.json)
(cd $C && python3 -I -B $SC/controles_s4_rs1.py --corridas $K --out salidas/controles_s4_rs1.json)
cp -cR $C $S/c_fig_base; cp -cR $C $S/c_fig_rs1
#    base: los cuatro generadores tal cual, con --salida en <S>/rs/salidas/figuras/base/<figura>
#    rs1: (cd $S/c_fig_rs1/docs/tesis/figuras && python3 $SC/figuras_rs1_parche_clon.py <sha diez nuevo> <sha desarrollo nuevo>);
#         4.5 con --grafo $T/ens_diez_r2b_rs1/r2/kg.json --sha256-grafo <sha diez nuevo>; y la 4.5 también con el de desarrollo
#         (sellado en el clon base, re-sellado en el clon rs1)
python3 -I -B $SC/figuras_rs1_resumen.py <S>/rs/salidas/figuras <repo> salidas/figuras_rs1.json
# 10. Neo4j: Docker Desktop, el contenedor del repo, la carga desde la copia (una vez por grafo) y el control de la cola
open -a Docker
(cd <repo>/data/experiment/neo4j && docker compose up -d --wait --wait-timeout 240)
(cd $C && for k in KG_Tanda0_Diez_r2b_rs1 KG_Tanda0_Desarrollo_r2b_rs1 KG_Tanda0_Diez_r2b_sincola_rs1 KG_Tanda0_Desarrollo_r2b_sincola_rs1; do
  $PY -B data/experiment/tanda0/code/cargar_neo4j_tanda0.py --grafo $k --out-dir data/experiment/resellado_t0/salida/neo4j/$k; done)
(cd $C && $PY -B data/experiment/resellado_t0/control_cola_neo4j_rs1.py --out data/experiment/resellado_t0/salida/control_cola_neo4j_rs1.json)
(cd <repo>/data/experiment/neo4j && docker compose stop); osascript -e 'quit app "Docker"'
#    después, en la copia: data/experiment/resellado_t0/salida/ pasa a llamarse salidas/ (mv)
# 11. las notas del §6 (16 documentos firmados) y del §4 (4 LEEME de figuras), en la copia
python3 -I -B $SC/notas_s6_rs1.py $C salidas/notas_s6_rs1.json
# 12. al repo: primero, cada archivo que cambia es el de HEAD y cada ruta nueva no existe; después, copia archivo por archivo
#     desde la copia y control de sha256 (salidas/escrituras_en_el_repo.json); al final, foto, .pyc, git status y grep
python3 -I -B $SC/escribir_en_el_repo_rs1.py $C <repo> salidas/escrituras_en_el_repo.json
