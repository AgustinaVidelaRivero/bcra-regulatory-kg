#!/bin/zsh
set -eu
: "U-UNION-ESTRECHA, U2-a: reproduce las fichas sobre un directorio nuevo, sin escribir en el repo."
: "Uso: zsh comandos_u2a.sh <raiz_del_repo> <directorio_de_trabajo_nuevo> [commit]"
: "Arma la copia con git show (sin enlaces), verifica el sello de las fichas, del criterio y del script, genera las"
: "fichas dos veces y las compara entre sí y con las de data/experiment/union_estrecha/u2/. No abre la lectura."
REPO="$1"
TRABAJO="$2"
COMMIT="${3:-HEAD}"
U2="${0:A:h}"
PY="${REPO}/.venv/bin/python"
export PYTHONDONTWRITEBYTECODE=1
if [[ -e "${TRABAJO}" ]]; then echo "el directorio de trabajo ya existe: ${TRABAJO}"; exit 2; fi
git -C "${REPO}" status --porcelain > "${TRABAJO}.git_status_antes.txt"
F="${TRABAJO}/fuentes"
mkdir -p "${F}/u1" "${F}/ens_diez" "${F}/e0_r2b" "${TRABAJO}/codigo"
E0="data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b"
git -C "${REPO}" show "${COMMIT}:data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2b/r2/kg.json" > "${F}/ens_diez/kg.json"
git -C "${REPO}" show "${COMMIT}:data/experiment/neo4j/grafos.py" > "${F}/grafos.py"
for t in pro cla ric cap ext ctacte lingob polcre pagjub docvig; do
  git -C "${REPO}" show "${COMMIT}:${E0}/chunks_${t}.json" > "${F}/e0_r2b/chunks_${t}.json"
done
for f in marco_u2_diez.json registro_u1_diez.json; do
  git -C "${REPO}" show "${COMMIT}:data/experiment/union_estrecha/salida/${f}" > "${F}/u1/${f}"
done
cp "${U2}/fichas_u2.py" "${TRABAJO}/codigo/fichas_u2.py"
: "El script copiado, el criterio y las fichas del repo tienen que ser los sellados."
for s in criterio_u2.md fichas_u2.py fichas_u2.json fichas_u2.md; do
  sellado="$(awk -v f="${s}" '$2 == f {print $1}' "${U2}/sello_fichas_u2.txt")"
  if [[ "${s}" == "fichas_u2.py" ]]; then actual="$(shasum -a 256 "${TRABAJO}/codigo/${s}" | cut -d' ' -f1)"; else actual="$(shasum -a 256 "${U2}/${s}" | cut -d' ' -f1)"; fi
  if [[ "${sellado}" != "${actual}" ]]; then echo "sello distinto: ${s}"; exit 3; fi
  echo "sello igual: ${s}"
done
echo "enlaces en la copia: $(find "${TRABAJO}" -type l | wc -l | tr -d ' ')"
cd "${TRABAJO}/codigo"
"${PY}" -I -B fichas_u2.py "${F}" "${TRABAJO}/salida_1"
"${PY}" -I -B fichas_u2.py "${F}" "${TRABAJO}/salida_2"
for f in fichas_u2.json fichas_u2.md; do
  cmp "${TRABAJO}/salida_1/${f}" "${TRABAJO}/salida_2/${f}" && echo "${f}: dos corridas iguales"
  cmp "${TRABAJO}/salida_1/${f}" "${U2}/${f}" && echo "${f}: igual a la del repo"
done
echo ".pyc en la copia: $(find "${TRABAJO}" -name '*.pyc' | wc -l | tr -d ' ')"
git -C "${REPO}" status --porcelain > "${TRABAJO}.git_status_despues.txt"
cmp "${TRABAJO}.git_status_antes.txt" "${TRABAJO}.git_status_despues.txt" && echo "git status del repo: igual antes y después"
