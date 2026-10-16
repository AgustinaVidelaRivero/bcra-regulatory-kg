"""Mesa, §120: compara, hoja por hoja, la medición de la columna r2b de T3-bis (grafos sellados a9631a64 y 6e756043) con la de los
grafos re-sellados (rs1). Por cada clave f<n> de diez y de desarrollo dice si cambia y qué hojas cambian. Ignora las rutas y los sha256
de los grafos (cambian por construcción). Uso: python3 -I -B <este> <medicion T3-bis> <medicion rs1> <salida.json>"""
import json, sys
a, b = json.load(open(sys.argv[1], encoding="utf-8")), json.load(open(sys.argv[2], encoding="utf-8"))
IGN = ("ruta", "sha256", "sha256_medido", "custodia", "kg", "reporte", "manifiesto", "nombre", "entrada")
def plano(x, p=""):
    if isinstance(x, dict):
        for k, v in x.items():
            yield from plano(v, f"{p}.{k}" if p else k)
    elif isinstance(x, list):
        yield p, json.dumps(x, ensure_ascii=False, sort_keys=True)
    else:
        yield p, x
out = {"fuentes": {"t3bis": sys.argv[1].split("/")[-1], "rs1": sys.argv[2].split("/")[-1]}, "por_grafo": {}}
for g in ("diez", "desarrollo"):
    A, B = a.get(g, {}), b.get(g, {})
    res = {}
    for k in sorted(set(A) | set(B)):
        if not k.startswith("f"): continue
        pa, pb = dict(plano(A.get(k))), dict(plano(B.get(k)))
        cambios = {h: [pa.get(h), pb.get(h)] for h in sorted(set(pa) | set(pb))
                   if pa.get(h) != pb.get(h) and not any(s in h.split(".")[-1] for s in IGN)}
        res[k] = {"cambia": bool(cambios), "hojas_que_cambian": len(cambios), "cambios": dict(list(cambios.items())[:12])}
    out["por_grafo"][g] = res
json.dump(out, open(sys.argv[3], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for g, r in out["por_grafo"].items():
    print(g, "claves:", len(r), "cambian:", [k for k, v in r.items() if v["cambia"]])
