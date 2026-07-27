#!/usr/bin/env python3
"""PASOS 4-5 — veredicto por mayoría y tablas primaria/secundaria.

Mayoría (protocolo §3): por pregunta×grafo, correcto si `correctitud ==
"correcta"` en ≥2 de las 3 réplicas (el veredicto por réplica es el del juez
v2.1.1, mapping determinístico). Una réplica con `failed_trace` cuenta como
no-correcta (comportamiento del sistema bajo evaluación; se lista aparte).

Tabla primaria: % correcto por mayoría, global y por familia; pares
discordantes run_3✗→v2✓ vs run_3✓→v2✗ (McNemar descriptivo: b vs c, sin test
de significancia — N=36 busca dirección y concentración).
Tabla secundaria: mayorías 3-0 vs 2-1; pasos promedio (tool_calls_used); uso
del esqueleto en trazas v2 (tool calls con nodos Sujeto_ en input y trazas
cuyas salidas exhiben subclase_de/miembro_de).

Además: réplicas con requiere_adjudicacion_humana, fallas técnicas, costos
reales sumados de las trazas.
"""
import json
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
TRACES = HERE.parent / "evaluacion" / "posthoc_run" / "traces"
RUNTIME = HERE / "EV1_runtime.json"
OUT = HERE / "corridas" / "resultados_2026-07-26.json"

rt = json.load(open(RUNTIME, encoding="utf-8"))["preguntas"]
familia = {q["id"]: q["familia"] for q in rt}
qids = [q["id"] for q in rt]
GRAFOS = ("run_3", "grafo_v2")

# ---- carga de las 216 réplicas -------------------------------------------- #
reps = defaultdict(dict)          # (grafo, qid) -> {rep: registro}
for g in GRAFOS:
    for rep in (1, 2, 3):
        for f in sorted((TRACES / f"escalon1_r{rep}" / g).glob("EV1-*.json")):
            r = json.load(open(f, encoding="utf-8"))[0]
            reps[(g, r["qid"])][rep] = r

falta = [(g, q) for g in GRAFOS for q in qids if len(reps[(g, q)]) != 3]
assert not falta, f"réplicas incompletas: {falta}"

def corr(r):
    if r["failed_trace"] or not r.get("judge"):
        return "failed"
    return (r["judge"].get("verdict") or {}).get("correctitud")

# ---- mayoría por pregunta×grafo ------------------------------------------- #
may = {}                          # (grafo, qid) -> dict
for g in GRAFOS:
    for q in qids:
        vs = [corr(reps[(g, q)][k]) for k in (1, 2, 3)]
        n_corr = sum(v == "correcta" for v in vs)
        may[(g, q)] = {
            "veredictos": vs,
            "correcto_mayoria": n_corr >= 2,
            "patron": "3-0" if n_corr in (0, 3) else "2-1",
            "n_correcta": n_corr,
        }

# ---- tabla primaria -------------------------------------------------------- #
def pct(n, d):
    return f"{100*n/d:.1f}%"

primaria = {}
for g in GRAFOS:
    ok = sum(may[(g, q)]["correcto_mayoria"] for q in qids)
    por_fam = {}
    for fam in ("puntual", "enumerativa", "condicional", "sujeto"):
        fq = [q for q in qids if familia[q] == fam]
        por_fam[fam] = {"n": len(fq),
                        "correctas": sum(may[(g, q)]["correcto_mayoria"] for q in fq)}
    primaria[g] = {"correctas_global": ok, "n": len(qids),
                   "pct_global": pct(ok, len(qids)), "por_familia": por_fam}

disc_v2_gana = [q for q in qids
                if not may[("run_3", q)]["correcto_mayoria"]
                and may[("grafo_v2", q)]["correcto_mayoria"]]
disc_r3_gana = [q for q in qids
                if may[("run_3", q)]["correcto_mayoria"]
                and not may[("grafo_v2", q)]["correcto_mayoria"]]
ambos_fallan = [q for q in qids
                if not may[("run_3", q)]["correcto_mayoria"]
                and not may[("grafo_v2", q)]["correcto_mayoria"]]

# ---- tabla secundaria ------------------------------------------------------ #
secundaria = {}
for g in GRAFOS:
    pat = Counter(may[(g, q)]["patron"] for q in qids)
    pasos = [reps[(g, q)][k]["trace"].get("tool_calls_used") or 0
             for q in qids for k in (1, 2, 3)]
    tool_limit = sum(1 for q in qids for k in (1, 2, 3)
                     if reps[(g, q)][k]["trace"].get("hit_tool_limit"))
    secundaria[g] = {"mayorias_3_0": pat["3-0"], "mayorias_2_1": pat["2-1"],
                     "pasos_promedio": round(sum(pasos) / len(pasos), 2),
                     "reps_hit_tool_limit": tool_limit}

# uso del esqueleto en trazas v2
esq = {"tool_calls_con_input_Sujeto": 0, "trazas_con_input_Sujeto": 0,
       "trazas_con_subclase_o_miembro_en_output": 0, "trazas_total": 0}
for q in qids:
    for k in (1, 2, 3):
        t = reps[("grafo_v2", q)][k]["trace"]
        esq["trazas_total"] += 1
        in_suj = [s for s in (t.get("steps") or [])
                  if "Sujeto_" in json.dumps(s.get("input") or {}, ensure_ascii=False)]
        esq["tool_calls_con_input_Sujeto"] += len(in_suj)
        if in_suj:
            esq["trazas_con_input_Sujeto"] += 1
        if any(("subclase_de" in (s.get("output_truncado") or "")
                or "miembro_de" in (s.get("output_truncado") or ""))
               for s in (t.get("steps") or [])):
            esq["trazas_con_subclase_o_miembro_en_output"] += 1

# ---- registros auxiliares -------------------------------------------------- #
fallas_tecnicas = [{"id": q, "grafo": g, "replica": k}
                   for g in GRAFOS for q in qids for k in (1, 2, 3)
                   if reps[(g, q)][k]["failed_trace"]]
req_adj = [{"id": q, "grafo": g, "replica": k}
           for g in GRAFOS for q in qids for k in (1, 2, 3)
           if (reps[(g, q)][k].get("judge") or {}).get("verdict", {})
              .get("requiere_adjudicacion_humana")]
costo = {g: round(sum(reps[(g, q)][k]["harness_cost"] + reps[(g, q)][k]["judge_cost"]
                      for q in qids for k in (1, 2, 3)), 4) for g in GRAFOS}

res = {
    "fecha": "2026-07-26",
    "regla_mayoria": "correcto si correctitud=='correcta' en >=2 de 3 réplicas; "
                     "failed_trace cuenta como no-correcta",
    "primaria": primaria,
    "pares_discordantes": {
        "run3_falla_v2_acierta (b)": disc_v2_gana,
        "run3_acierta_v2_falla (c)": disc_r3_gana,
        "ambos_fallan": ambos_fallan,
        "mcnemar_descriptivo": {"b": len(disc_v2_gana), "c": len(disc_r3_gana)},
    },
    "secundaria": secundaria,
    "esqueleto_v2": esq,
    "fallas_tecnicas": fallas_tecnicas,
    "requiere_adjudicacion_humana": req_adj,
    "costo_real_usd": costo,
    "detalle_mayorias": {f"{g}|{q}": may[(g, q)] for g in GRAFOS for q in qids},
}
OUT.parent.mkdir(parents=True, exist_ok=True)
json.dump(res, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

print(json.dumps({k: res[k] for k in
                  ("primaria", "pares_discordantes", "secundaria",
                   "esqueleto_v2", "costo_real_usd")},
                 ensure_ascii=False, indent=1))
print(f"\nfallas técnicas: {len(fallas_tecnicas)} | requiere_adjudicacion: "
      f"{len(req_adj)}")
print(f"registro completo en {OUT}")
