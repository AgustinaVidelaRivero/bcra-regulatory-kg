"""Mesa, §120: junta el resultado del gate final del laudo de la release r2 en un JSON (y una tabla corta para el laudo), desde el
trabajo del gate (gate_final_laudo_r2_mesa.sh), las métricas intrínsecas corridas con el comando del tablero (la E0 con las dos partes de
cap::4.2.1.2, en el trabajo de la condición 4) y el selftest del catálogo corrido en un clon de HEAD.
Uso: python3 -I -B <este> --gate <trabajo del gate> --metricas <copia de la condición 4> --out <json>"""
import argparse, hashlib, json, re
from pathlib import Path
ap = argparse.ArgumentParser(); ap.add_argument("--gate", type=Path, required=True); ap.add_argument("--metricas", type=Path, required=True)
ap.add_argument("--out", type=Path, required=True); A = ap.parse_args(); W = A.gate
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
ESP = {"r2b_diez": "fda6c07dbb95602f5992f7e1ad9bf148ff1c2a72b9f69ff2ebbce891c15740ea",
       "r2b_sincola_diez": "61dd1b69ba03e40499845c40a6a8bec4c22d892ebe95823c7d5a569110f08738",
       "r2b_desarrollo": "acb26dca0885e9ea83ab02637f15c1dac57885f0cf017c5fb16173ac7dfcac31",
       "r2b_sincola_desarrollo": "66e745f57397ab754cde09eb641e9f0d9ef6259ea7e6445d086ecbf1c36dcc6c",
       "r2a_diez": "70d51e429b0e2cc1", "r2a_desarrollo": "fa4c1043d859081e"}
out = {"head": (W / "head.txt").read_text().strip(), "tiempos": (W / "tiempos.txt").read_text().splitlines(), "cadenas": {}}
for corrida in ("run1", "run2", "r2a"):
    for d in sorted((W / corrida).iterdir()):
        k = d / "r2" / "kg.json"
        s = sha(k); e = ESP[d.name]
        rc = [l for l in (W / "consolas" / f"{corrida}_{d.name}.txt").read_text().splitlines() if l.startswith("rc=")]
        out["cadenas"][f"{corrida}/{d.name}"] = {"sha256": s, "esperado": e, "igual": s.startswith(e), "rc": rc[-1] if rc else None}
out["shapes_y_suite"] = {}
for d in sorted((W / "gate").iterdir()):
    sh = json.loads((d / "shapes_perfil_r2_fase_r2b.json").read_text(encoding="utf-8"))
    md = (d / "shapes_perfil_r2_fase_r2b.md").read_text(encoding="utf-8")
    su = json.loads((d / "suite_perfil_r2.json").read_text(encoding="utf-8"))
    bloq = md.split("## Informativas")[0]
    out["shapes_y_suite"][d.name] = {
        "shapes_veredicto": re.search(r"Veredicto global: \**([A-Z]+)", md).group(1),
        "bloqueantes_fail": len(re.findall(r"^### \S+ — FAIL", bloq, flags=re.M)),
        "bloqueantes_pass": len(re.findall(r"^### \S+ — PASS", bloq, flags=re.M)),
        "informativas_fail": re.findall(r"^### (\S+) — FAIL", md.split("## Informativas")[1], flags=re.M),
        "informativas_warn": re.findall(r"^### (\S+) — WARN", md.split("## Informativas")[1], flags=re.M),
        "suite_items": len(su["items"]), "suite_regresiones": [x["item"] for x in su["regresion"]["regresiones"]],
        "suite_fixture_sha256": su["regresion"]["fixture_sha256"], "suite_entrada": su["regresion"]["entrada"]}
DECL = {"RT-C5-3", "RT-C6-1", "RT-C6-2"}
out["regresiones_no_declaradas"] = sorted({r for v in out["shapes_y_suite"].values() for r in v["suite_regresiones"]} - DECL)
out["selftests"] = {}
for f in sorted((W / "selftests").glob("*.txt")):
    L = f.read_text(encoding="utf-8").splitlines()
    res = [l.strip() for l in L if re.search(r"(\d+/\d+|VEREDICTO|casos|PASS$|ok, \d+ fallas)", l)]
    out["selftests"][f.stem] = {"rc": next((l for l in reversed(L) if l.startswith("rc=")), None), "resumen": res[-1] if res else None}
met = {}
for k in A.metricas.glob("data/experiment/reextraccion_v2/corpus_tanda0/ens_*_rs1/intrinsecas_gen3/*.json"):
    d = json.loads(k.read_text(encoding="utf-8"))
    m10 = d["metricas"]["M10_chunks_mudos"]
    met[k.stem] = {"sha256_medido": d["custodia"][0]["sha256_medido"], "custodia": d["custodia"][0]["custodia"],
                   "M10": f'{m10["numerador"]} de {m10["denominador"]}'}
out["metricas_intrinsecas"] = met
cf = json.loads((W / "comparacion_foto.json").read_text(encoding="utf-8"))
out["repo_durante_el_gate"] = {k: (v if isinstance(v, int) else len(v)) for k, v in cf.items()}
todos = cf["nuevos"] + cf["borrados"] + cf["cambiados"]
fuera = [p for p in todos if not p.startswith("data/experiment/banco_mcp/")]
out["repo_durante_el_gate"]["fuera_de_banco_mcp"] = fuera
out["repo_durante_el_gate"]["nota"] = ("los cambios en data/experiment/banco_mcp/ son escrituras de A2.1, que corrió en paralelo en su "
                                       "sesión; el gate corrió sobre una copia y no escribe en el repo")
out["veredicto"] = {
    "cadenas_r2b_dos_corridas_iguales_a_los_sellos": all(v["igual"] for k, v in out["cadenas"].items() if not k.startswith("r2a")),
    "cadena_r2a": all(v["igual"] for k, v in out["cadenas"].items() if k.startswith("r2a")),
    "shapes_bloqueantes_en_pass": all(v["bloqueantes_fail"] == 0 and v["shapes_veredicto"] == "PASA" for v in out["shapes_y_suite"].values()),
    "suite_0_regresiones_no_declaradas": not out["regresiones_no_declaradas"],
    "metricas_con_el_comando_del_tablero": len(met) == 4,
    "repo_sin_cambios_fuera_de_banco_mcp": not fuera}
json.dump(out, open(A.out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps(out["veredicto"], ensure_ascii=False)); print(json.dumps({k: v["rc"] for k, v in out["selftests"].items()}, ensure_ascii=False))
