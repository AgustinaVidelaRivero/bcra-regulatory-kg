#!/bin/bash
# U-SINCOLA-T0, SC2.4: suite y shapes sobre el repo tal como queda, con la fixture del repo, para los dos grafos sin la
# cola; las salidas van dentro de cada ensamblado (ens_<g>_r2b_sincola/{shapes_perfil_r2_fase_r2b,suite_perfil_r2}.{md,json}),
# como en los r2b sellados (T3-bis). Después compara cada salida con la de la copia (gate_copia/), normalizando las rutas.
# Uso: comandos_sc2_repo.sh <repo> <copia> <gate_copia> <salida_comparacion.txt>
set -u
R="$1"; C="$2"; GC="$3"; OUT="$4"; cd "$R" || exit 1
PY="$R/.venv/bin/python"; export PYTHONDONTWRITEBYTECODE=1; unset ANTHROPIC_API_KEY
X=data/experiment/reextraccion_v2; T=$X/corpus_tanda0; E0=$X/e0_chunking/salida_tanda0_r2b
EXC=data/experiment/catalogo_unico/generados_r2/entrada_esqueleto_r2.json
CAT=data/experiment/catalogo_unico/generados_r2/catalogo_suite_r2.json
{
echo "# U-SINCOLA-T0, SC2.4: suite y shapes sobre el repo (fixture del repo) y comparación con la copia"
for g in diez desarrollo; do
  N=$T/ens_${g}_r2b_sincola
  echo; echo "## $g"
  "$PY" -B scripts/shapes_validator.py --kg "$N/r2/kg.json" --perfil r2 --fase r2b --e0 $E0 --registro-dir "$N/r2" --excepciones $EXC --out "$N/shapes_perfil_r2_fase_r2b.md" > "$N/../consola_shapes_${g}_sincola_tmp.txt" 2>&1; rc_sh=$?
  mv "$N/../consola_shapes_${g}_sincola_tmp.txt" "$GC/../consola_shapes_${g}_repo.txt"
  echo "shapes rc=$rc_sh: $(grep -i 'VEREDICTO' "$GC/../consola_shapes_${g}_repo.txt" | tail -1)"
  "$PY" -B scripts/regression_kg.py --kg "$N/r2/kg.json" --perfil r2 --generacion 3 --catalogo $CAT --politica-cuarentena flaggeada --registro-dir "$N/r2" --esperado scripts/regression_kg_esperado.json --out "$N/suite_perfil_r2.md" > "$GC/../consola_suite_${g}_repo.txt" 2>&1; rc_su=$?
  echo "suite rc=$rc_su (1 = hay regresiones respecto de la expectativa; las 3 declaradas de siempre): $(grep 'regresiones:' "$GC/../consola_suite_${g}_repo.txt" | tail -1 | cut -c1-200)"
  "$PY" -B - "$N" "$GC" "$g" <<'EOF'
import json, sys
from pathlib import Path
N, GC, g = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3]
sh_r = json.loads((N / "shapes_perfil_r2_fase_r2b.json").read_text(encoding="utf-8"))
sh_c = json.loads((GC / f"shapes_{g}.json").read_text(encoding="utf-8"))
su_r = json.loads((N / "suite_perfil_r2.json").read_text(encoding="utf-8"))
su_c = json.loads((GC / f"suite_{g}.json").read_text(encoding="utf-8"))
res_sh = {k: v.get("result") for k, v in sh_r["shapes"].items()}
print("shapes: veredicto", sh_r["veredicto"], "| bloqueantes en fail", sh_r["bloqueantes_en_fail"], "| por resultado", {r: sum(1 for v in res_sh.values() if v == r) for r in ("PASS", "FAIL", "WARN")},
      "| igual a la copia (resultados y conteos):", all(sh_r["shapes"][k].get("result") == sh_c["shapes"][k].get("result") and sh_r["shapes"][k].get("conteos") == sh_c["shapes"][k].get("conteos") for k in sh_r["shapes"]))
reg = su_r["regresion"]
est_r = {i["id"]: i["estado"] for i in su_r["items"]}; est_c = {i["id"]: i["estado"] for i in su_c["items"]}
print("suite: entrada", reg.get("entrada"), "| fixture sha", reg.get("fixture_sha256", "")[:12], "| n_regresiones", reg.get("n_regresiones"), [x["item"] for x in reg.get("regresiones", [])],
      "| coinciden", reg.get("coinciden"), "| NO VERIFICADAS", len(reg.get("no_verificadas", [])), "| resumen", su_r["resumen"], "| estados iguales a la copia:", est_r == est_c)
EOF
done
echo; echo "## archivos escritos en los ensamblados"
ls -1 $T/ens_diez_r2b_sincola $T/ens_desarrollo_r2b_sincola | sed 's#^#  #'
} > "$OUT" 2>&1
cat "$OUT"
