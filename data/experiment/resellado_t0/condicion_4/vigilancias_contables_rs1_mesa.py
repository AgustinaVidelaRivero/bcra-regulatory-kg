"""Mesa, §120: las líneas de base de las vigilancias contables (4), (5), (8) y (9) con el perfil r2b, sobre los cuatro grafos
re-sellados de la tanda 0 (pendiente 16 de la v7; aceptado por la autora el 10/10/2026). USD 0, sin API. Las reglas son las de
la tanda 0 (data/experiment/tanda0/code/lectura_e6_tanda0.py:221-321), sin cambios:
  (4) nodos TextoOrdenado por TO, por la procedencia del nodo: tiene que ser 1 por TO;
  (5) el contador tipo_obligacion_requisito_de_estructura del resumen de E1 de cada TO (y tipo_obligacion_normalizados);
  (8) en las relaciones aceptadas de E1 (validacion.relaciones de extracciones_finales_<to>.jsonl): sujeto_propuesto
      contra sujeto_id, y la tasa;
  (9) emisiones de Sujeto_entidad_originante_de_transferencia en esas relaciones, y aristas del kg que lo tocan.
Uso: python3 -I -B <este> --salida <salida_r2b> --kg grafo=ruta [--kg …] --esperado grafo=sha256 [...] --out <json>"""
import argparse, hashlib, json, sys
from collections import Counter
from pathlib import Path
ap = argparse.ArgumentParser()
ap.add_argument("--salida", type=Path, required=True)
ap.add_argument("--kg", action="append", required=True)
ap.add_argument("--esperado", action="append", required=True)
ap.add_argument("--out", type=Path, required=True)
A = ap.parse_args()
TOS_DEV = ("pro", "cla", "ric", "cap", "ext"); TOS_NUEVOS = ("ctacte", "lingob", "polcre", "pagjub", "docvig")
TOS = {"diez": TOS_DEV + TOS_NUEVOS, "desarrollo": TOS_DEV}
ID_V9 = "Sujeto_entidad_originante_de_transferencia"
esp = dict(x.split("=", 1) for x in A.esperado)
kgs = {}
for x in A.kg:
    g, ruta = x.split("=", 1)
    b = open(ruta, "rb").read()
    if hashlib.sha256(b).hexdigest() != esp[g]: sys.exit(f"FRENO: {g} no da su sha256")
    kgs[g] = json.loads(b)
lineas = lambda p: [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]
docs_de = lambda n: frozenset(p.get("to") for p in (n.get("provenances") or []) if p.get("to"))
def tos_de(g): return TOS["diez" if "diez" in g else "desarrollo"]
out = {"reglas": "data/experiment/tanda0/code/lectura_e6_tanda0.py:221-321", "grafos": esp, "vigilancias": {}}
v4 = {}
for g, kg in kgs.items():
    cnt = Counter()
    for n in kg["nodes"]:
        if n["type"] == "TextoOrdenado":
            for d in docs_de(n) or {"(sin to)"}: cnt[d] += 1
    v4[g] = {"por_to": dict(sorted(cnt.items())), "uno_por_to": set(cnt.values()) == {1} and set(cnt) == set(tos_de(g))}
out["vigilancias"]["4"] = {"nombre": "un nodo TextoOrdenado por TO", "linea_de_base_tanda0": "2 archivos afectados en lecturas", "por_grafo": v4}
res = {to: json.load(open(A.salida / to / "resumen_e1.json", encoding="utf-8")) for to in TOS["diez"]}
out["vigilancias"]["5"] = {"nombre": "emisiones residuales de requisito_de_estructura", "linea_de_base_tanda0": "0 por construcción",
    "tipo_obligacion_requisito_de_estructura": {to: res[to].get("tipo_obligacion_requisito_de_estructura") for to in TOS["diez"]},
    "tipo_obligacion_normalizados": {to: res[to].get("tipo_obligacion_normalizados") for to in TOS["diez"]},
    "nota": "se mide sobre la salida de E1 (salida_r2b), que es la misma para los cuatro grafos"}
def cont8(tos):
    prop = sid = 0
    for to in tos:
        for x in lineas(A.salida / to / f"extracciones_finales_{to}.jsonl"):
            for r in (x.get("validacion") or {}).get("relaciones") or []:
                if r.get("sujeto_propuesto"): prop += 1
                elif r.get("sujeto_id"): sid += 1
    return {"sujeto_propuesto": prop, "sujeto_id": sid, "tasa_pct": round(100 * prop / (prop + sid), 2) if prop + sid else None}
out["vigilancias"]["8"] = {"nombre": "tasa de sujeto_propuesto", "linea_de_base_tanda0": {"sujeto_id": 3905, "sujeto_propuesto": 124, "tasa_pct": 3.08},
    "diez": cont8(TOS["diez"]), "desarrollo": cont8(TOS["desarrollo"]),
    "nota": "relaciones aceptadas de E1 (salida_r2b); la cola no cambia la salida de E1, así que el sin cola da lo mismo"}
em = {to: sum(1 for x in lineas(A.salida / to / f"extracciones_finales_{to}.jsonl")
              for r in (x.get("validacion") or {}).get("relaciones") or [] if r.get("sujeto_id") == ID_V9) for to in TOS["diez"]}
out["vigilancias"]["9"] = {"nombre": f"emisiones de {ID_V9}", "linea_de_base_tanda0": "13 menciones / 5 TOs en fase 1; 2→1 en la unidad adversarial",
    "emisiones_E1_por_to": em, "aristas_en_kg": {g: sum(1 for e in kg["edges"] if ID_V9 in (e["source"], e["target"])) for g, kg in kgs.items()}}
json.dump(out, open(A.out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps({k: (v.get("por_grafo") and {g: x["uno_por_to"] for g, x in v["por_grafo"].items()}) or
                  (k == "5" and sum(x or 0 for x in v["tipo_obligacion_requisito_de_estructura"].values())) or
                  (k == "8" and (v["diez"]["tasa_pct"], v["desarrollo"]["tasa_pct"])) or (k == "9" and v["aristas_en_kg"])
                  for k, v in out["vigilancias"].items()}, ensure_ascii=False))
