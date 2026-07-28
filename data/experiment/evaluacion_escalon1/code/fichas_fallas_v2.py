#!/usr/bin/env python3
"""PASO 6 — fichas de las fallas del brazo grafo_v2 (protocolo §6).

Sobre las fallas de v2 el verificador NO se corre como evidencia (calibración
intra-run_3; lección 0/6 fuera de familia). Cada falla se lista con su traza y
su tos_fuente para la ficha de adjudicación manual, SIN veredicto causal.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
TRACES = HERE.parent / "evaluacion" / "posthoc_run" / "traces"
RUNTIME = HERE / "EV1_runtime.json"
RES = HERE / "corridas" / "resultados_2026-07-26.json"
OUT = HERE / "corridas" / "fichas_fallas_v2.json"

rt = {q["id"]: q for q in json.load(open(RUNTIME, encoding="utf-8"))["preguntas"]}
res = json.load(open(RES, encoding="utf-8"))
det = res["detalle_mayorias"]
fallas = [q for q in rt
          if not det[f"grafo_v2|{q}"]["correcto_mayoria"]]

fichas = []
for q in sorted(fallas):
    reps = []
    for k in (1, 2, 3):
        r = json.load(open(TRACES / f"escalon1_r{k}" / "grafo_v2" / f"{q}.json",
                           encoding="utf-8"))[0]
        t = r["trace"]
        v = (r.get("judge") or {}).get("verdict") or {}
        s2 = (r.get("judge") or {}).get("step2") or {}
        claims_fallidos = [
            {"verdict": x.get("verdict"), "central": x.get("central"),
             "enunciado": x.get("enunciado")}
            for x in (s2.get("verificaciones") or [])
            if x.get("verdict") in ("falso", "no_soportado")]
        reps.append({
            "replica": k,
            "failed_trace": r["failed_trace"],
            "correctitud": v.get("correctitud"),
            "completitud": v.get("completitud"),
            "respuesta_final": t.get("final_json"),
            "claims_fallidos_del_juez": claims_fallidos,
            "pasos": t.get("tool_calls_used"),
            "hit_tool_limit": t.get("hit_tool_limit"),
            "traza_tools": [
                {"n": s.get("n"), "tool": s.get("tool"), "input": s.get("input")}
                for s in (t.get("steps") or [])],
        })
    fichas.append({
        "id": q,
        "pregunta": rt[q]["pregunta"],
        "familia": rt[q]["familia"],
        "tos_fuente": rt[q]["tos_fuente"],
        "ground_truth_secciones": rt[q]["ground_truth_secciones"],
        "veredictos_mayoria": det[f"grafo_v2|{q}"],
        "replicas": reps,
        "veredicto_causal": None,  # adjudicación humana (protocolo §6)
    })

out = {"fecha": "2026-07-26",
       "nota": "Fichas para adjudicación manual de la autora. Sin veredicto "
               "causal: el verificador no se corrió sobre este brazo (guarda "
               "de calibración intra-esquema del protocolo §6).",
       "n_fallas": len(fichas), "fichas": fichas}
json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"OK: {len(fichas)} fichas en {OUT}")
for f in fichas:
    print(f"  {f['id']} [{f['familia']}] tos={f['tos_fuente']} "
          f"veredictos={[r['correctitud'] for r in f['replicas']]}")
