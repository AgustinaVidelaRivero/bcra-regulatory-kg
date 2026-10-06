#!/bin/bash
# U-REEXT-T0, T5: los comandos de las cifras del reporte, sobre una COPIA del repo (sin enlaces simbólicos), USD 0.
# Uso: comandos_t5.sh <repo> <copia> <salida>   (la salida, fuera del repo)
# Escribe en la copia solo lo que los comandos escriben por diseño (intrínsecas en ens_<g>_r2b/intrinsecas_gen3/ y el
# grafo simulado en data/experiment/reext_t0/t5/tmp_sim/); en el repo no escribe nada.
set -u
R="$1"; C="$2"; O="$3"; mkdir -p "$O"; cd "$C" || exit 1
PY="$R/.venv/bin/python"; export PYTHONDONTWRITEBYTECODE=1; unset ANTHROPIC_API_KEY
X=data/experiment/reextraccion_v2; T=$X/corpus_tanda0; E0=$X/e0_chunking/salida_tanda0_r2b
# bloque 1: gate de T3-bis (shapes con la E0 r2b, suite con la fixture sellada)
for g in diez desarrollo; do
  "$PY" -B scripts/shapes_validator.py --kg $T/ens_${g}_r2b/r2/kg.json --perfil r2 --fase r2b --e0 $E0 --out "$O/shapes_${g}_r2b.md" > "$O/consola_shapes_${g}.txt" 2>&1
  "$PY" -B scripts/regression_kg.py --kg $T/ens_${g}_r2b/r2/kg.json --generacion 3 --catalogo data/experiment/catalogo_unico/generados_r2/catalogo_suite_r2.json --politica-cuarentena flaggeada --esperado scripts/regression_kg_esperado.json --perfil r2 --out "$O/suite_${g}_r2b.md" > "$O/consola_suite_${g}.txt" 2>&1
done
# bloque 1: controles de T3 (a–r) y la columna r2b del tablero
"$PY" -B data/experiment/reext_t0/t3/controles_t3.py --out "$O/controles_t5.json" > "$O/consola_controles.txt" 2>&1
cmp "$O/controles_t5.json" data/experiment/reext_t0/t3bis/salida/controles_t3bis.json > "$O/cmp_controles.txt" 2>&1 && echo "igual byte a byte a controles_t3bis.json" >> "$O/cmp_controles.txt"
"$PY" -B data/experiment/reext_t0/t3/e0_con_partes.py $E0 $T/salida_r2b "$O/e0_r2b_con_partes" > "$O/consola_e0_con_partes.txt" 2>&1
for p in "diez:Diez" "desarrollo:Desarrollo"; do g=${p%%:*}; N=${p#*:}
  S=$(shasum -a 256 $T/ens_${g}_r2b/r2/kg.json | cut -c1-64)
  "$PY" -B scripts/metricas_intrinsecas.py --gen3 --kg $T/ens_${g}_r2b/r2/kg.json --nombre KG-Tanda0-$N-r2b --e0 "$O/e0_r2b_con_partes" --manifiesto $X/manifiestos/tanda0_ens_${g}_r2b.json --sha256-esperado $S --out-dir $T/ens_${g}_r2b/intrinsecas_gen3 > "$O/consola_intrinsecas_${g}.txt" 2>&1
done
"$PY" -B data/experiment/reext_t0/t3/medicion_tablero_r2b.py --out "$O/medicion_tablero_t5.json" > "$O/consola_medicion.txt" 2>&1
git -C "$R" show "bbc38dc^:docs/tablero_correcciones.md" > "$O/tablero_antes_t3bis.md"
"$PY" -B data/experiment/reext_t0/t3bis/escribir_columna_r2b_t3bis.py --tablero "$O/tablero_antes_t3bis.md" --salida "$O/tablero_derivado_t5.md" --medicion data/experiment/reext_t0/t3bis/salida/medicion_tablero_r2b.json --controles data/experiment/reext_t0/t3bis/salida/controles_t3bis.json > "$O/consola_tablero.txt" 2>&1
cmp "$O/tablero_derivado_t5.md" docs/tablero_correcciones.md > "$O/cmp_tablero.txt" 2>&1 && echo "la columna del repo es la derivación de la medición y los controles commiteados" >> "$O/cmp_tablero.txt"
# bloque 1: la reparación acotada
"$PY" -B data/experiment/reext_t0/t2ter/cifra_reparacion.py --estado final=$T/salida_r2b --out "$O/cifra_reparacion_t5.json" > "$O/consola_cifra_reparacion.txt" 2>&1
# bloque 5: claves de la caché con el anclaje r2b
"$PY" -B data/experiment/mantenimiento/code/selftest_clave_cache.py --salida-r2b $T/salida_r2b --out "$O/selftest_clave_cache_t5.json" > "$O/consola_selftest_clave_cache.txt" 2>&1
# bloque 6: el grafo de diez sin lo que sale con la cola (simulación) y las 15 preguntas sobre él
mkdir -p data/experiment/reext_t0/t5/tmp_sim
"$PY" -B -c "
import json
kg=json.load(open('$T/ens_diez_r2b/r2/kg.json'))
s=json.load(open('data/experiment/reext_t0/t4/salida/sorteos_t4.json'))['punto_1_cola_humana']
cola={m['chunk_id'] for m in s['muestra_en_orden_del_sorteo']}|set(s['fuera_de_la_muestra'])
ch=lambda x:[p.get('chunk_id') for p in (x.get('provenances') or [x.get('provenance') or {}])]
f={x['id'] for x in kg['nodes'] if ch(x) and all(c in cola for c in ch(x))}
json.dump({'nodes':[x for x in kg['nodes'] if x['id'] not in f],'edges':[x for x in kg['edges'] if x['source'] not in f and x['target'] not in f]},open('data/experiment/reext_t0/t5/tmp_sim/kg.json','w'),ensure_ascii=False)"
"$PY" -B data/experiment/reext_t0/t1_preguntas_control.py --kg data/experiment/reext_t0/t5/tmp_sim/kg.json --e0 $E0 --out "$O/preguntas_sin_cola_simulado.json" > "$O/consola_preguntas_sin_cola.txt" 2>&1
# las cifras del reporte
"$PY" -B data/experiment/reext_t0/t5/cifras_t5.py --gate "$O" --out "$O/anexo_cifras_t5.json" --md "$O/anexo_cifras_t5.md" > "$O/consola_cifras_t5.txt" 2>&1
echo "fin: $(cat "$O/consola_cifras_t5.txt" | tail -1)"
