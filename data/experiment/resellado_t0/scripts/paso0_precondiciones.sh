#!/bin/bash
# Re-sellado único de la tanda 0: el paso 0 (§1 y §1 bis del mandato) y las precondiciones a–e, con su salida. Solo lee.
# Uso, desde la raíz del repo: paso0_precondiciones.sh   (la carpeta personal se imprime como $HOME)
set -u
echo "## texto firmado del mandato (líneas 1-254, antes de «## Firma»), en el commit de la firma y en el árbol"
F=docs/mandatos/URESELLADO_T0_resellado_unico_grafos_r2b.md
git show "67fe5b14:$F" | head -n 254 | shasum -a 256
head -n 254 "$F" | shasum -a 256
echo "## paso 0"
echo '$ pwd'; pwd | sed "s#$HOME#\$HOME#"
echo '$ git rev-parse --abbrev-ref HEAD'; git rev-parse --abbrev-ref HEAD
echo '$ git log --oneline -3'; git log --oneline -3
echo '$ git log --format=%s -5'; git log --format=%s -5
echo '$ git status --porcelain -- data/experiment/segmentacion_oficial_e0r2/s2'; git status --porcelain -- data/experiment/segmentacion_oficial_e0r2/s2; echo '(vacío si no hay renglones arriba)'
echo '$ git status --short -- data/experiment/tanda0 data/experiment/reextraccion_v2/corpus_v2 scripts data/experiment/neo4j'
git status --short -- data/experiment/tanda0 data/experiment/reextraccion_v2/corpus_v2 scripts data/experiment/neo4j; echo '(vacío si no hay renglones arriba)'
echo "## a. el código"
for c in ded41d50 1d690df3 2d0f5277; do git merge-base --is-ancestor $c HEAD && echo "$c en la historia: $(git log -1 --format='%h %s' $c)"; done
echo '$ git diff --stat ded41d50 HEAD -- <las ocho rutas del §1.a>'
git diff --stat ded41d50 HEAD -- data/experiment/tanda0/code data/experiment/reextraccion_v2/corpus_v2 data/experiment/reextraccion_v2/e2_reduce data/experiment/reextraccion_v2/e1_extractor data/experiment/reextraccion_v2/e3_verificador data/experiment/pyd_r2/code scripts/shapes_validator.py scripts/regression_kg.py; echo '(vacío si no hay renglones arriba)'
echo "## b. la E0 de la tanda 0"
git diff --quiet 9f6361e HEAD -- data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b/; echo "git diff --quiet 9f6361e HEAD: rc=$?"
echo "archivos rastreados: $(git ls-files data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b/ | wc -l | tr -d ' ')"
echo "## c. los grafos sellados, intactos"
T=data/experiment/reextraccion_v2/corpus_tanda0
shasum -a 256 $T/ens_diez_r2b/r2/kg.json $T/ens_desarrollo_r2b/r2/kg.json $T/ens_diez_r2b_sincola/r2/kg.json $T/ens_desarrollo_r2b_sincola/r2/kg.json
for p in "bbc38dc:$T/ens_diez_r2b/r2/kg.json" "bbc38dc:$T/ens_desarrollo_r2b/r2/kg.json" "dde9f44:$T/ens_diez_r2b_sincola/r2/kg.json" "dde9f44:$T/ens_desarrollo_r2b_sincola/r2/kg.json"; do
  echo "$p $(git show "$p" | shasum -a 256 | cut -c1-64)"; done
for s in a9631a64 6e756043 e22fae1a 2922b72d; do echo "$s: grafos.py $(grep -c $s data/experiment/neo4j/grafos.py), fixture $(grep -c $s scripts/regression_kg_esperado.json)"; done
echo "## d. las salidas de R0: los sha256 de salida_r2b/{ext,docvig}/*.jsonl, contra 2d0f5277 y contra lo declarado (r0/corrida/anexo_r0.json)"
python3 -I -B - <<'EOF'
import hashlib, json, subprocess, pathlib
d = json.load(open("data/experiment/reextraccion_v2/r0/corrida/anexo_r0.json"))
decl = {(x["to"], x["archivo"]): x["sha256_despues"] for x in d["archivos"]}
base = pathlib.Path("data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b")
n = ok = 0
for to in ("ext", "docvig"):
    for f in sorted((base / to).glob("*.jsonl")):
        n += 1
        cur = hashlib.sha256(f.read_bytes()).hexdigest()
        c2 = hashlib.sha256(subprocess.run(["git", "show", f"2d0f5277:{f}"], capture_output=True).stdout).hexdigest()
        dd = decl.get((to, f.name))
        bueno = cur == c2 and (dd is None or dd == cur)
        ok += bueno
        print(f"{to}/{f.name}: {cur[:16]} | igual a 2d0f5277: {cur == c2} | declarado: {'-' if dd is None else dd == cur}")
print(f"{ok} de {n} OK; los 8 del anexo, iguales a lo declarado: {sum(1 for (t, a), v in decl.items() if hashlib.sha256((base / t / a).read_bytes()).hexdigest() == v)} de {len(decl)}")
EOF
echo "## e. git status --short en tanda0/, corpus_v2/, scripts/ y neo4j/: arriba, en el paso 0"
