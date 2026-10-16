#!/bin/zsh
# U-ALCANCE-E1, A2: selftest_catalogo_unico sobre las dos copias (HEAD y A2), con el .git del repo en solo lectura
# (GIT_DIR y GIT_OPTIONAL_LOCKS=0, como O1 y O2 de U-OMISIONES-COD: el selftest lee con git show archivos de commits
# viejos, y las copias no llevan .git), y la foto sha256 del repo antes y después (CLAUDE.md §4.l).
# Uso: zsh catalogo_unico_con_git_a2.sh REPO TRABAJO
R="$1"; T="$2"; PY="$R/.venv/bin/python"; H="${0:A:h}"; M="$T/med/catalogo_con_git"
export PYTHONDONTWRITEBYTECODE=1; unset ANTHROPIC_API_KEY
rm -rf "$M"; mkdir -p "$M"
log() { print -r -- "$*" | tee -a "$M/catalogo_con_git.log"; }
cuenta_pyc() { find "$R" \( -path "$R/.git" -o -path "$R/.venv" \) -prune -o -name '*.pyc' -print | wc -l | tr -d ' '; }
log "inicio $(date '+%Y-%m-%d %H:%M:%S %z'); HEAD $(git -C "$R" rev-parse HEAD)"
python3 -I -B "$H/foto_repo_a2.py" "$R" "$M/foto_repo_antes.json" | tee -a "$M/catalogo_con_git.log"
log ".pyc antes: $(cuenta_pyc)"
touch "$M/marca_antes"
for e in head a2; do
  (cd "$T/copia_$e" && GIT_DIR="$R/.git" GIT_OPTIONAL_LOCKS=0 "$PY" -B data/experiment/catalogo_unico/code/selftest_catalogo_unico.py > "$M/selftest_catalogo_unico_$e.txt" 2>&1)
  log "$e rc=$? $(tail -1 "$M/selftest_catalogo_unico_$e.txt")"
  log "   K2: $(grep -n 'K2' "$M/selftest_catalogo_unico_$e.txt" | head -3 | tr '\n' ' ')"
done
if cmp -s "$M/selftest_catalogo_unico_head.txt" "$M/selftest_catalogo_unico_a2.txt"; then log "consolas de HEAD y de A2: iguales byte a byte"; else log "consolas de HEAD y de A2: DISTINTAS"; diff "$M/selftest_catalogo_unico_head.txt" "$M/selftest_catalogo_unico_a2.txt" | tee -a "$M/catalogo_con_git.log"; fi
python3 -I -B "$H/foto_repo_a2.py" "$R" "$M/foto_repo_despues.json" | tee -a "$M/catalogo_con_git.log"
log ".pyc después: $(cuenta_pyc)"
log "archivos de .git más nuevos que la marca de antes: $(find "$R/.git" -type f -newer "$M/marca_antes" | wc -l | tr -d ' ')"
python3 -I -B "$H/foto_repo_a2.py" --comparar "$M/foto_repo_antes.json" "$M/foto_repo_despues.json" "$M/comparacion_foto_repo.json" | tee -a "$M/catalogo_con_git.log"
log "git status --porcelain (rastreados): [$(git -C "$R" status --porcelain --untracked-files=no | tr '\n' ' ')]"
log "fin $(date '+%Y-%m-%d %H:%M:%S %z')"
