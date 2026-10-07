#!/bin/zsh
set -eu
: "U-DIAG-CAP3-GRAFO: reproduce las salidas de la unidad sobre un directorio nuevo, sin escribir en el repo."
: "Uso: zsh comandos_udiag_cap3_grafo.sh <raiz_del_repo> <directorio_de_trabajo_nuevo> [commit]"
REPO="$1"
TRABAJO="$2"
COMMIT="${3:-d007be8}"
PAQ="${0:A:h:h}"
PY="${REPO}/.venv/bin/python"
export PYTHONDONTWRITEBYTECODE=1
git -C "${REPO}" status --porcelain > "${TRABAJO}.git_status_antes.txt"
mkdir -p "${TRABAJO}/src/salida_r2b" "${TRABAJO}/src/e0_r2b" "${TRABAJO}/src/code" "${TRABAJO}/src/ens_diez" "${TRABAJO}/src/ens_sincola" "${TRABAJO}/src/grafos_tablero" "${TRABAJO}/salida"
R2B="data/experiment/reextraccion_v2/corpus_tanda0"
E0="data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b"
git -C "${REPO}" show "${COMMIT}:${R2B}/ens_diez_r2b/r2/kg.json" > "${TRABAJO}/src/ens_diez/kg.json"
git -C "${REPO}" show "${COMMIT}:${R2B}/ens_diez_r2b_sincola/r2/kg.json" > "${TRABAJO}/src/ens_sincola/kg.json"
for t in pro cla ric cap ext ctacte lingob polcre pagjub docvig; do
  mkdir -p "${TRABAJO}/src/salida_r2b/${t}"
  for f in extracciones_e1.jsonl reintentos_e3.jsonl finales.jsonl "extracciones_finales_r2_${t}.jsonl" cola_humana.jsonl; do
    if git -C "${REPO}" cat-file -e "${COMMIT}:${R2B}/salida_r2b/${t}/${f}" 2>/dev/null; then
      git -C "${REPO}" show "${COMMIT}:${R2B}/salida_r2b/${t}/${f}" > "${TRABAJO}/src/salida_r2b/${t}/${f}"
    fi
  done
  git -C "${REPO}" show "${COMMIT}:${E0}/chunks_${t}.json" > "${TRABAJO}/src/e0_r2b/chunks_${t}.json"
done
for p in data/experiment/pyd_r2/code/modelos_r2.py data/experiment/pyd_r2/code/validador_r2.py data/experiment/reextraccion_v2/e1_extractor/comun_e1.py data/experiment/reextraccion_v2/e1_extractor/prompt_r2b.py data/experiment/reextraccion_v2/e2_reduce/e2_lib.py data/experiment/tanda0/code/ensamblar_tanda0.py scripts/metricas_intrinsecas.py docs/tablero_correcciones.md; do
  git -C "${REPO}" show "${COMMIT}:${p}" > "${TRABAJO}/src/code/${p:t}"
done
G="${TRABAJO}/src/grafos_tablero"
git -C "${REPO}" show "${COMMIT}:data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json" > "${G}/kg_r1.json"
git -C "${REPO}" show "${COMMIT}:${R2B}/ens_cinco/r1/kg.json" > "${G}/kg_cinco_r1.json"
git -C "${REPO}" show "${COMMIT}:${R2B}/ens_desarrollo/r1/kg.json" > "${G}/kg_desarrollo_r1.json"
git -C "${REPO}" show "${COMMIT}:${R2B}/ens_diez/r1/kg.json" > "${G}/kg_diez_r1.json"
git -C "${REPO}" show "${COMMIT}:${R2B}/ens_desarrollo_r2a/r2/kg.json" > "${G}/kg_desarrollo_r2a.json"
git -C "${REPO}" show "${COMMIT}:${R2B}/ens_diez_r2a/r2/kg.json" > "${G}/kg_diez_r2a.json"
git -C "${REPO}" show "${COMMIT}:${R2B}/ens_desarrollo_r2b/r2/kg.json" > "${G}/kg_desarrollo_r2b.json"
git -C "${REPO}" show "${COMMIT}:${R2B}/ens_desarrollo_r2b_sincola/r2/kg.json" > "${G}/kg_desarrollo_r2b_sincola.json"
git -C "${REPO}" show "7e72051:reports/u_estudio_matriz/uestmat_muestra_60.csv" > "${TRABAJO}/src/uestmat_muestra_60_7e72051.csv"
cp "${TRABAJO}/src/ens_diez/kg.json" "${G}/kg_diez_r2b.json"
cp "${TRABAJO}/src/ens_sincola/kg.json" "${G}/kg_diez_r2b_sincola.json"
for s in udiag_comun udiag_a_casos udiag_a_union udiag_a_controles udiag_a_tablas udiag_b_procedencia udiag_be_tablas udiag_e_aisladas udiag_h_tipo_operacion udiag_a_fichas41 udiag_a_control_anclas41; do
  cp "${PAQ}/scripts/${s}.py" "${TRABAJO}/${s}.py"
done
cp "${PAQ}/lecturas/criterio_lectura_a.md" "${TRABAJO}/criterio_lectura_a.md"
for f in lectura_a_parte1.json lectura_a_parte2.json lectura_a_parte3.json lectura_a_parte4.json lectura_union_e.json relectura_25_sesion.json lectura_control_i.json lectura_resto_i_parte1.json lectura_resto_i_parte2.json lectura_g_r_22.json; do
  cp "${PAQ}/lecturas/${f}" "${TRABAJO}/salida/${f}"
done
cd "${TRABAJO}"
"${PY}" -B udiag_a_casos.py > salida/log_a_casos.txt
"${PY}" -B udiag_a_union.py > salida/log_a_union.txt
"${PY}" -B -c "import udiag_a_controles as C; C.main(); C.resto_i(); C.partir_fichas(); C.unir_lecturas()" > salida/log_a_controles.txt
"${PY}" -B udiag_a_tablas.py > salida/log_a_tablas.txt
"${PY}" -B udiag_b_procedencia.py > salida/log_b.txt
"${PY}" -B udiag_e_aisladas.py > salida/log_e.txt
"${PY}" -B udiag_h_tipo_operacion.py > salida/log_h.txt
"${PY}" -B udiag_be_tablas.py > salida/log_be.txt
"${PY}" -B -c "import udiag_be_tablas as T; T.g_r_22()"
"${PY}" -B udiag_a_fichas41.py > salida/log_fichas41.txt
cp "${PAQ}/lectura1_41_exceptua_operacion.json" "${TRABAJO}/salida/lectura1_41_exceptua_operacion.json"
"${PY}" -B udiag_a_control_anclas41.py > salida/log_anclas41.txt
cmp salida/control_anclas_lectura1_41.json "${PAQ}/salidas/control_anclas_lectura1_41.json" && echo "control_anclas_lectura1_41.json: igual a la del paquete"
for f in fichas_41_exceptua_operacion.json fichas_41_exceptua_operacion.md; do
  cmp "salida/${f}" "${PAQ}/${f}" && echo "${f}: igual a la del paquete"
done
for f in casos_a.json fichas_lectura_a.md union_e.json firma_f.json muestra_union_e.md fichas_control_i.md fichas_control_f.md fichas_relectura_25.md muestra_control_i.json fichas_resto_i_parte1.md fichas_resto_i_parte2.md fichas_lectura_a_parte1.md fichas_lectura_a_parte2.md fichas_lectura_a_parte3.md fichas_lectura_a_parte4.md muestra_resto_i.json lectura_a.json tabla_a.json tabla_a.md procedencia_b.json casos_b_20.md aisladas_e.json tipo_operacion_h.json tabla_b.md tabla_e.md g_r_22_cambios_de_punto.md; do
  cmp "salida/${f}" "${PAQ}/salidas/${f}" && echo "${f}: igual a la del paquete"
done
git -C "${REPO}" status --porcelain > "${TRABAJO}.git_status_despues.txt"
cmp "${TRABAJO}.git_status_antes.txt" "${TRABAJO}.git_status_despues.txt" && echo "git status del repo: sin cambios durante la reproducción"
