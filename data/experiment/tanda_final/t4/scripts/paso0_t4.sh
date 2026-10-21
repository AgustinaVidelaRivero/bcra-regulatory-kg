#!/bin/zsh
# B6.1, tanda final, T4, primer tramo: el paso 0, con la carpeta personal reemplazada por $HOME en toda la salida. Solo lee.
# Uso: zsh paso0_t4.sh <repo> <scratchpad>/t4
set -u; setopt pipefail
R="$1"; W="$2"; cd "$R" || exit 2
{
print -r -- "== pwd"; pwd
print -r -- "== git log --format=%s -3"; git --no-optional-locks log --format=%s -3
print -r -- "== git log --format='%h %H' -3"; git --no-optional-locks log --format='%h %H' -3
print -r -- "== git status --porcelain --untracked-files=no (entre las dos rayas)"; print -r -- "--"; git --no-optional-locks status --porcelain --untracked-files=no; print -r -- "--"
print -r -- "== commit_sellado de la tanda final en grafos.py"
grep -n -A6 '"KG_TandaFinal_r2b' data/experiment/neo4j/grafos.py | grep -E 'KG_TandaFinal|commit_sellado'
print -r -- "== sha256 de las muestras, del material y de la derivada"; .venv/bin/python -I -B "$W/scripts/paso0_sha_muestras_t4.py" . "$W/paso0/sha_muestras_T4.json"; print -r -- "rc=$?"
print -r -- "== la foto nueva contra la de después de T3 y los tres commits"
.venv/bin/python -I -B "$W/scripts/paso0_foto_contra_commits_t4.py" . "$W/../t3/final/foto_repo_despues_T3.json" "$W/paso0/foto_repo_antes_T4.json" "$W/paso0/foto_contra_commits_T4.json" | grep -v '"sha256"\|foto_\|^ }'; print -r -- "rc=$?"
print -r -- "== .pyc: líneas y diff contra el cierre de T3"; wc -l < "$W/paso0/pyc_antes_T4.txt"; diff "$W/../t3/final/pyc_despues_T3.txt" "$W/paso0/pyc_antes_T4.txt" && print -r -- "iguales"
print -r -- "== pgrep -fl \"runner_corpus.py|lanzar_t|correr_tanda\""; pgrep -fl "runner_corpus.py|lanzar_t|correr_tanda"; print -r -- "rc=$?"
print -r -- "== pgrep -fl ensamblar_tanda0.py"; pgrep -fl ensamblar_tanda0.py; print -r -- "rc=$?"
print -r -- "== hora"; date '+%Y-%m-%d %H:%M:%S'
} 2>&1 | sed "s|$HOME|\$HOME|g"
