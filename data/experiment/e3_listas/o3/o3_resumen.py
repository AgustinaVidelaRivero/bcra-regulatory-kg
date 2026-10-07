"""U-E3-LISTAS, O3: resumen de (a), (b) y (c), recomputado de sus salidas, y el cruce de (b) con (c). Sin API.
Uso: python o3_resumen.py <dir_o3>"""
import json, sys
from pathlib import Path
O3 = Path(sys.argv[1]).resolve()
a = json.loads((O3 / "a" / "cifras_a.json").read_text(encoding="utf-8"))
d1 = json.loads((O3 / "a" / "d1_citas.json").read_text(encoding="utf-8"))
b = json.loads((O3 / "b" / "b_intento0_vs_final.json").read_text(encoding="utf-8"))
c = json.loads((O3 / "c" / "d3_repite_norma.json").read_text(encoding="utf-8"))
p = json.loads((O3 / "a" / "presupuesto.json").read_text(encoding="utf-8"))
reint_final = {u for u, x in b["unidades"].items() if x["origen_de_la_final"] != "e1"}
repite_final = {u for u, x in c["unidades"].items() if x["final"]}
repite_i0 = {u for u, x in c["unidades"].items() if x["intento_0"]}
res = {
    "gasto_usd": p["gasto_usd"], "llamadas": len(p["llamadas"]),
    "a": {k: a[k] for k in ("reclamos_viejos_intento_0", "por_categoria_vieja", "totales", "persisten_por_la_regla",
                            "persisten_por_la_lectura", "faltantes_nuevos", "bloqueantes_nuevos", "unidades_completo_ok")},
    "a_nuevos_PCB": a["nuevos_PCB"], "a_D1": d1["totales"], "a_D1_bloqueantes_en": d1["unidades_con_bloqueante_solo_por_D1"],
    "b": b["resumen"],
    "c": {"intento_0": sorted(repite_i0), "final": sorted(repite_final),
          "final_entre_las_del_reintento": sorted(repite_final & reint_final),
          "introducidas_por_el_reintento": sorted((repite_final & reint_final) - repite_i0)},
}
(O3 / "resumen_o3.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps(res, ensure_ascii=False, indent=1))
