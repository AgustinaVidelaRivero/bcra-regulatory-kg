#!/bin/bash
# U-SINCOLA-T0, SC1 (mandato 723680e; enmienda 1 en 1f7c159): SC1.3 (comparación de las dos corridas), SC1.4 (shapes),
# SC1.5 (suite con una copia de la fixture), SC1.6 a SC1.8 (controles_sc1.py y las 15 preguntas), sobre una COPIA del
# repo con el código nuevo y los dos ensamblados sin la cola ya corridos (ens_<g>_r2b_sincola y _corrida2). USD 0.
# Uso: comandos_sc1.sh <repo> <copia> <salida> <controles_sc1.py>   (la salida, fuera del repo)
set -u
R="$1"; C="$2"; O="$3"; CTRL="$4"; mkdir -p "$O"; cd "$C" || exit 1
PY="$R/.venv/bin/python"; export PYTHONDONTWRITEBYTECODE=1; unset ANTHROPIC_API_KEY
X=data/experiment/reextraccion_v2; T=$X/corpus_tanda0; E0=$X/e0_chunking/salida_tanda0_r2b
EXC=data/experiment/catalogo_unico/generados_r2/entrada_esqueleto_r2.json
CAT=data/experiment/catalogo_unico/generados_r2/catalogo_suite_r2.json
# la copia de la fixture con las dos entradas nuevas (decisión 4: las expectativas de la entrada r2b sellada, sin cambiar ninguna)
"$PY" -B - "$O" <<'EOF'
import copy, hashlib, json, sys
from pathlib import Path
O = Path(sys.argv[1])
fx = json.loads(Path("scripts/regression_kg_esperado.json").read_text(encoding="utf-8"))
ee = fx["estado_esperado"]
for g, G in (("diez", "Diez"), ("desarrollo", "Desarrollo")):
    kg = Path(f"data/experiment/reextraccion_v2/corpus_tanda0/ens_{g}_r2b_sincola/r2/kg.json")
    e = copy.deepcopy(ee[f"KG-Tanda0-{G}-r2b"])
    e["_rotulo"] = (f"COPIA DE SC1 DE U-SINCOLA-T0 (no es la fixture del repo; la entrada la sella la autora en SC2): copia de la entrada "
                    f"KG-Tanda0-{G}-r2b con el kg y el kg_sha256 del ensamblado sin la cola y sus expectativas sin cambiar ninguna (decisión 4 "
                    f"del mandato). Rótulo heredado: " + e["_rotulo"])
    e["kg"] = str(kg)
    e["kg_sha256"] = hashlib.sha256(kg.read_bytes()).hexdigest()
    e["_kg_sha256"] = "sha256 del kg.json de SC1.3 (doble corrida byte a byte), U-SINCOLA-T0"
    ee[f"KG-Tanda0-{G}-r2b-sincola"] = e
(O / "regression_kg_esperado_sc1_copia.json").write_text(json.dumps(fx, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("fixture copia:", O / "regression_kg_esperado_sc1_copia.json", {k: v["kg_sha256"][:12] for k, v in ee.items() if k.endswith("sincola")})
EOF
for g in diez desarrollo; do
  N=$T/ens_${g}_r2b_sincola; N2=${N}_corrida2; S=$T/ens_${g}_r2b
  # SC1.3: las dos corridas, byte a byte (la ruta de salida, normalizada)
  { echo "## SC1.3 $g: diff -r de las dos corridas (sin normalizar)"; diff -rq "$N" "$N2"; echo "(rc=$?)";
    echo "## kg.json: cmp"; cmp "$N/r2/kg.json" "$N2/r2/kg.json" && echo "kg.json byte a byte igual";
    echo "## reporte: diff con la ruta de salida normalizada"; diff <(sed "s#${N2}#<SALIDA>#g" "$N2/r2/reporte_ensamblado_r2.json") <(sed "s#${N}#<SALIDA>#g" "$N/r2/reporte_ensamblado_r2.json") && echo "reporte igual con la ruta normalizada";
    echo "## archivos en r2/: $(find "$N/r2" -type f | wc -l | tr -d ' ') y $(find "$N2/r2" -type f | wc -l | tr -d ' ')";
    echo "## sha256"; shasum -a 256 "$N/r2/kg.json" "$N2/r2/kg.json"; } > "$O/sc1_3_doble_corrida_${g}.txt" 2>&1
  # SC1.4: shapes
  "$PY" -B scripts/shapes_validator.py --kg "$N/r2/kg.json" --perfil r2 --fase r2b --e0 $E0 --registro-dir "$N/r2" --excepciones $EXC --out "$O/shapes_${g}_sincola.md" > "$O/consola_shapes_${g}.txt" 2>&1; echo "rc=$?" >> "$O/consola_shapes_${g}.txt"
  # SC1.5: suite con la copia de la fixture
  "$PY" -B scripts/regression_kg.py --kg "$N/r2/kg.json" --perfil r2 --generacion 3 --catalogo $CAT --politica-cuarentena flaggeada --registro-dir "$N/r2" --esperado "$O/regression_kg_esperado_sc1_copia.json" --out "$O/suite_${g}_sincola.md" > "$O/consola_suite_${g}.txt" 2>&1; echo "rc=$?" >> "$O/consola_suite_${g}.txt"
  # SC1.6: las 15 preguntas sobre el grafo nuevo
  "$PY" -B data/experiment/reext_t0/t1_preguntas_control.py --kg "$N/r2/kg.json" --e0 $E0 --out "$O/preguntas_${g}_sincola.json" > "$O/consola_preguntas_${g}.txt" 2>&1; echo "rc=$?" >> "$O/consola_preguntas_${g}.txt"
  # la línea de base de las 15 preguntas: el r2b sellado del mismo grafo (para diez tiene que coincidir con t4/salida/preguntas_r2b.json)
  "$PY" -B data/experiment/reext_t0/t1_preguntas_control.py --kg "$S/r2/kg.json" --e0 $E0 --out "$O/preguntas_${g}_r2b_sellado.json" > "$O/consola_preguntas_${g}_sellado.txt" 2>&1; echo "rc=$?" >> "$O/consola_preguntas_${g}_sellado.txt"
  # SC1.6 a SC1.8: controles
  "$PY" -B "$CTRL" --grafo $g --kg-nuevo "$N/r2/kg.json" --kg-sellado "$S/r2/kg.json" --preguntas-nuevo "$O/preguntas_${g}_sincola.json" --preguntas-sellado "$O/preguntas_${g}_r2b_sellado.json" --out "$O/controles_sc1_${g}.json" > "$O/consola_controles_${g}.txt" 2>&1; echo "rc=$?" >> "$O/consola_controles_${g}.txt"
  # comparación del gate: shapes y suite, nuevo vs sellado
  "$PY" -B - "$O" "$g" "$S" <<'EOF'
import json, sys
from collections import Counter, OrderedDict
from pathlib import Path
O, g, S = Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3])
sh_s = json.loads((S / "shapes_perfil_r2_fase_r2b.json").read_text(encoding="utf-8"))
sh_n = json.loads((O / f"shapes_{g}_sincola.json").read_text(encoding="utf-8"))
su_s = json.loads((S / "suite_perfil_r2.json").read_text(encoding="utf-8"))
su_n = json.loads((O / f"suite_{g}_sincola.json").read_text(encoding="utf-8"))
res = OrderedDict()
res["shapes"] = OrderedDict([
    ("veredicto", [sh_s.get("veredicto"), sh_n.get("veredicto")]),
    ("bloqueantes_en_fail", [sh_s.get("bloqueantes_en_fail"), sh_n.get("bloqueantes_en_fail")]),
    ("bloqueantes_no_computables", [sh_s.get("bloqueantes_no_computables"), sh_n.get("bloqueantes_no_computables")]),
    ("por_resultado", [dict(Counter(v.get("result") for v in sh_s["shapes"].values())), dict(Counter(v.get("result") for v in sh_n["shapes"].values()))]),
    ("bloqueantes", {k: [sh_s["shapes"][k].get("result"), sh_n["shapes"][k].get("result")] for k in sh_n["shapes"] if sh_n["shapes"][k].get("severidad") == "bloqueante"}),
    ("cambian_de_resultado", {k: [sh_s["shapes"].get(k, {}).get("result"), sh_n["shapes"][k].get("result")] for k in sh_n["shapes"]
                              if sh_s["shapes"].get(k, {}).get("result") != sh_n["shapes"][k].get("result")}),
    ("informativas_con_cifras_que_cambian", {k: {"severidad": sh_n["shapes"][k].get("severidad"), "antes": sh_s["shapes"].get(k, {}).get("resumen"),
                                                 "despues": sh_n["shapes"][k].get("resumen"), "conteos_antes": sh_s["shapes"].get(k, {}).get("conteos"),
                                                 "conteos_despues": sh_n["shapes"][k].get("conteos")}
                                             for k in sh_n["shapes"] if sh_n["shapes"][k].get("severidad") != "bloqueante"
                                             and sh_s["shapes"].get(k, {}).get("conteos") != sh_n["shapes"][k].get("conteos")}),
    ("bloqueantes_con_cifras_que_cambian", {k: {"antes": sh_s["shapes"].get(k, {}).get("resumen"), "despues": sh_n["shapes"][k].get("resumen")}
                                            for k in sh_n["shapes"] if sh_n["shapes"][k].get("severidad") == "bloqueante"
                                            and sh_s["shapes"].get(k, {}).get("conteos") != sh_n["shapes"][k].get("conteos")})])
est_s = {i["id"]: i["estado"] for i in su_s["items"]}
est_n = {i["id"]: i["estado"] for i in su_n["items"]}
det_n = {i["id"]: i.get("detalle") for i in su_n["items"]}
det_s = {i["id"]: i.get("detalle") for i in su_s["items"]}
fx = json.loads((O / "regression_kg_esperado_sc1_copia.json").read_text(encoding="utf-8"))
G = "Diez" if g == "diez" else "Desarrollo"
esp = {k: v.get("estado") for k, v in fx["estado_esperado"][f"KG-Tanda0-{G}-r2b"]["items"].items()}
res["suite"] = OrderedDict([
    ("items", [len(est_s), len(est_n)]),
    ("resumen", [su_s.get("resumen"), su_n.get("resumen")]),
    ("por_estado", [dict(sorted(Counter(est_s.values()).items())), dict(sorted(Counter(est_n.values()).items()))]),
    ("regresion_segun_la_suite", su_n.get("regresion")),
    ("cambian_respecto_del_r2b_sellado", {k: {"antes": est_s.get(k), "despues": est_n.get(k), "detalle_antes": det_s.get(k), "detalle_despues": det_n.get(k)}
                                          for k in est_n if est_s.get(k) != est_n.get(k)}),
    ("difieren_de_la_expectativa_sellada (null = NO VERIFICADA)", {k: {"esperado": esp.get(k), "observado": est_n.get(k), "detalle": det_n.get(k)}
                                                                   for k in est_n if esp.get(k) is not None and esp.get(k) != est_n.get(k)}),
    ("coinciden_con_la_expectativa_sellada", sum(1 for k in est_n if esp.get(k) is not None and esp.get(k) == est_n.get(k))),
    ("null_en_la_expectativa", sum(1 for k in est_n if esp.get(k) is None))])
(O / f"comparacion_gate_{g}.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(g, "shapes:", res["shapes"]["veredicto"], res["shapes"]["bloqueantes_en_fail"], "cambian:", res["shapes"]["cambian_de_resultado"],
      "| suite:", res["suite"]["por_estado"], "cambian:", list(res["suite"]["cambian_respecto_del_r2b_sellado"]),
      "difieren de la expectativa:", list(res["suite"]["difieren_de_la_expectativa_sellada (null = NO VERIFICADA)"]))
EOF
done
echo "fin comandos_sc1.sh"
