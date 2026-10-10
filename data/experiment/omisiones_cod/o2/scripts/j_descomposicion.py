"""U-OMISIONES-COD, O2 — las `remite_a` que siguen entre HEAD y O2 y cambian de procedencia (causa «J» del diff declarado),
separadas en: las que cambia J aislado (sin J → O2, `j_aislado_<grafo>.json`) y las que cambian sin J (HEAD → sin J: la
procedencia del primer nodo del grupo, que cambia porque G-r corrige el rol o el punto de un nodo del grupo, o porque el
agrupamiento sin el rol junta grupos). Control: toda arista de la causa «J» cae en uno de los dos conjuntos, y las de HEAD →
sin J cambian solo en `provenance`/`provenances`. Escribe las tres listas («solo_J», «J_y_G_r», «solo_G_r»), que
`diff_final.py` usa para separar la causa. Solo lee.
Uso: python3 -I j_descomposicion.py <diff_declarado.json> <j_aislado.json> <r2 HEAD> <r2 sin J> --out <json>"""
import json, sys
from collections import Counter
from pathlib import Path
dd, ja, dh, ds, out = sys.argv[1], sys.argv[2], Path(sys.argv[3]), Path(sys.argv[4]), Path(sys.argv[6])
A = {x["clave"] for x in json.load(open(dd, encoding="utf-8"))["lista"] if x["objeto"] == "arista" and x["causa"] == "J"}
B = {x["arista"] for x in json.load(open(ja, encoding="utf-8"))["lista"]}
kh = json.loads((dh / "kg.json").read_text(encoding="utf-8")); ks = json.loads((ds / "kg.json").read_text(encoding="utf-8"))
ih, i2 = {n["id"]: n for n in kh["nodes"]}, {n["id"]: n for n in ks["nodes"]}
por = {}
for i in set(ih) - set(i2):
    por.setdefault((ih[i]["type"], ih[i]["label"]), []).append(i)
ren = {por[(i2[j]["type"], i2[j]["label"])][0]: j for j in set(i2) - set(ih) if len(por.get((i2[j]["type"], i2[j]["label"]), [])) == 1}
m = lambda x: ren.get(x, x)
eh = {(m(e["source"]), e["relation"], m(e["target"])): e for e in kh["edges"] if e["relation"] == "remite_a"}
es = {(e["source"], e["relation"], e["target"]): e for e in ks["edges"] if e["relation"] == "remite_a"}
C, fuera, causa = set(), [], Counter()
gr = {(x["chunk_id"], x["punto_g_r"]) for x in json.loads((ds / "procedencia_g_r.json").read_text(encoding="utf-8"))}
for k in set(eh) & set(es):
    x, y = eh[k], es[k]
    if x == y:
        continue
    cs = {f for f in set(x) | set(y) if x.get(f) != y.get(f)}
    if cs - {"provenance", "provenances"}:
        fuera.append("|".join(k)); continue
    C.add("|".join(k))
    p = y["provenance"]
    causa["el grupo tiene un nodo de G-r (punto o rol)" if (p.get("chunk_id"), p.get("punto")) in gr else "sin nodo de G-r en el grupo"] += 1
entran = {"|".join(k) for k in set(es) - set(eh)}
res = {"J_del_diff_HEAD_O2": len(A), "J_aislado_sin_J_O2": len(B), "HEAD_sin_J_cambia_la_procedencia": len(C),
       "J_del_diff_tambien_en_J_aislado": len(A & B), "J_del_diff_no_en_J_aislado": len(A - B),
       "de_esas_cambian_de_HEAD_a_sin_J": len((A - B) & C), "J_del_diff_sin_explicar": sorted(A - B - C),
       "J_aislado_fuera_del_diff": len(B - A), "de_esas_entran_de_HEAD_a_O2": len((B - A) & entran),
       "de_esas_siguen_y_J_deshace_el_cambio_de_HEAD_a_sin_J": len((B - A) & C),
       "J_aislado_fuera_del_diff_sin_explicar": sorted(B - A - entran - C),
       "HEAD_sin_J_por_grupo": dict(causa), "HEAD_sin_J_fuera_de_la_procedencia": fuera,
       "listas": {"solo_J": sorted((A & B) - C), "J_y_G_r": sorted(A & B & C), "solo_G_r": sorted(A - B)}}
out.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps({k: (v if k != "listas" else {kk: len(vv) for kk, vv in v.items()}) for k, v in res.items()}, ensure_ascii=False))
