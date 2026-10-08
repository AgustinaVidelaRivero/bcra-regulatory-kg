#!/bin/zsh
set -eu
: "U-UNION-ESTRECHA, U1: reproduce la pre-medición sobre un directorio nuevo, sin escribir en el repo."
: "Uso: zsh comandos_u1.sh <raiz_del_repo> <directorio_de_trabajo_nuevo> [commit]"
: "Arma la copia con git show (sin enlaces), verifica el sello del código, corre el selftest y dos veces la"
: "pre-medición, y compara las salidas entre sí y con las de data/experiment/union_estrecha/salida/."
REPO="$1"
TRABAJO="$2"
COMMIT="${3:-HEAD}"
UE="${0:A:h}"
PY="${REPO}/.venv/bin/python"
export PYTHONDONTWRITEBYTECODE=1
if [[ -e "${TRABAJO}" ]]; then echo "el directorio de trabajo ya existe: ${TRABAJO}"; exit 2; fi
git -C "${REPO}" status --porcelain > "${TRABAJO}.git_status_antes.txt"
F="${TRABAJO}/fuentes"
mkdir -p "${F}/code" "${F}/e0_r2b" "${F}/ens_diez" "${F}/ens_sincola" "${TRABAJO}/control" "${TRABAJO}/codigo"
R2B="data/experiment/reextraccion_v2/corpus_tanda0"
E0="data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b"
git -C "${REPO}" show "${COMMIT}:${R2B}/ens_diez_r2b/r2/kg.json" > "${F}/ens_diez/kg.json"
git -C "${REPO}" show "${COMMIT}:${R2B}/ens_diez_r2b_sincola/r2/kg.json" > "${F}/ens_sincola/kg.json"
for t in pro cla ric cap ext ctacte lingob polcre pagjub docvig; do
  git -C "${REPO}" show "${COMMIT}:${E0}/chunks_${t}.json" > "${F}/e0_r2b/chunks_${t}.json"
done
for p in data/experiment/pyd_r2/code/modelos_r2.py data/experiment/reextraccion_v2/e1_extractor/comun_e1.py data/experiment/reextraccion_v2/e1_extractor/prompt_r2b.py; do
  git -C "${REPO}" show "${COMMIT}:${p}" > "${F}/code/${p:t}"
done
for p in union_e.json muestra_union_e.md; do
  git -C "${REPO}" show "${COMMIT}:reports/u_diag_cap3_grafo/salidas/${p}" > "${TRABAJO}/control/${p}"
done
for s in regla_u1.py premedicion_u1.py selftest_regla_u1.py; do
  cp "${UE}/${s}" "${TRABAJO}/codigo/${s}"
done
: "El código copiado tiene que ser el sellado."
for s in regla_u1.md regla_u1.py premedicion_u1.py selftest_regla_u1.py comandos_u1.sh; do
  sellado="$(awk -v f="${s}" '$2 == f {print $1}' "${UE}/sello_regla_u1.txt")"
  if [[ "${s}" == "regla_u1.md" || "${s}" == "comandos_u1.sh" ]]; then actual="$(shasum -a 256 "${UE}/${s}" | cut -d' ' -f1)"; else actual="$(shasum -a 256 "${TRABAJO}/codigo/${s}" | cut -d' ' -f1)"; fi
  if [[ "${sellado}" != "${actual}" ]]; then echo "sello distinto: ${s}"; exit 3; fi
  echo "sello igual: ${s}"
done
echo "enlaces en la copia: $(find "${TRABAJO}" -type l | wc -l | tr -d ' ')"
cd "${TRABAJO}/codigo"
"${PY}" -B selftest_regla_u1.py "${F}"
"${PY}" -B premedicion_u1.py "${F}" "${TRABAJO}/control" "${TRABAJO}/salida_1" > "${TRABAJO}/log_1.txt"
"${PY}" -B premedicion_u1.py "${F}" "${TRABAJO}/control" "${TRABAJO}/salida_2" > "${TRABAJO}/log_2.txt"
for f in premedicion_u1.json premedicion_u1.md registro_u1_diez.json registro_u1_sincola.json encabezados_u1.json marco_u2_diez.json; do
  cmp "${TRABAJO}/salida_1/${f}" "${TRABAJO}/salida_2/${f}" && echo "${f}: dos corridas iguales"
  if [[ -e "${UE}/salida/${f}" ]]; then cmp "${TRABAJO}/salida_1/${f}" "${UE}/salida/${f}" && echo "${f}: igual a la del repo"; fi
done
echo ".pyc en la copia: $(find "${TRABAJO}" -name '*.pyc' | wc -l | tr -d ' ')"
git -C "${REPO}" status --porcelain > "${TRABAJO}.git_status_despues.txt"
cmp "${TRABAJO}.git_status_antes.txt" "${TRABAJO}.git_status_despues.txt" && echo "git status del repo: sin cambios durante la reproducción"
