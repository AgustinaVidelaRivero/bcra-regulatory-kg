"""
comparar_a1.py — U-ALCANCE-E1, A1: compara, unidad por unidad, los mensajes de E1 de la corrida en seco con el código de
HEAD y con el nuevo (mensajes_runner_a1.py). Uso: comparar_a1.py DIR_SECO SALIDA.json
Por origen y por documento: unidades, mensajes distintos y si la única diferencia es la línea de alcance (el mensaje nuevo,
sin «línea + salto + salto», es el de HEAD). Sin tokens ni costo: la lista final de la tanda 1 sale de S2 (A2).
"""
import json
import sys
from collections import OrderedDict
from pathlib import Path

d = Path(sys.argv[1])


def leer(et):
    """Clave (origen, archivo, posición, id): la partición legada repite ids en algunos documentos (BKL-0037), así que la
    unidad se identifica por su posición dentro del documento, que es la misma en las dos corridas."""
    out, pos = OrderedDict(), {}
    for l in (d / f"mensajes_{et}.jsonl").open(encoding="utf-8"):
        f = json.loads(l)
        i = pos[(f["origen"], f["archivo"])] = pos.get((f["origen"], f["archivo"]), -1) + 1
        out[(f["origen"], f["archivo"], i, f["id"])] = f
    return out


h, n = leer("head"), leer("nuevo")
solo_n = [k for k in n if k not in h]
solo_h = [k for k in h if k not in n]
por = OrderedDict()
for k, fn in n.items():
    if k not in h:
        continue
    fh = h[k]
    o, a = k[0], k[1]
    r = por.setdefault(o, OrderedDict()).setdefault(a, OrderedDict(
        [("unidades", 0), ("distintos", 0), ("solo_la_linea", 0), ("linea_head", set()), ("linea_nuevo", set())]))
    r["unidades"] += 1
    r["linea_head"].add(fh["linea_alcance"])
    r["linea_nuevo"].add(fn["linea_alcance"])
    if fn["mensaje"] != fh["mensaje"]:
        r["distintos"] += 1
        ln = fn["linea_alcance"]
        if (fh["linea_alcance"] is None and ln is not None and fn["mensaje"].count(ln + "\n\n") == 1
                and fn["mensaje"].replace(ln + "\n\n", "") == fh["mensaje"]):
            r["solo_la_linea"] += 1
res = OrderedDict()
for o, docs in por.items():
    filas = OrderedDict()
    for a, r in docs.items():
        lh, ln = sorted(r["linea_head"], key=str), sorted(r["linea_nuevo"], key=str)
        filas[a] = OrderedDict([("unidades", r["unidades"]), ("distintos", r["distintos"]),
                                ("solo_la_linea_de_alcance", r["solo_la_linea"]),
                                ("con_linea_head", lh != [None]), ("con_linea_nuevo", ln != [None]),
                                ("linea_nueva", ln[0] if r["distintos"] and len(ln) == 1 else None),
                                ("caracteres_agregados_por_unidad", len(ln[0]) + 2 if r["distintos"] and len(ln) == 1 else 0)])
    res[o] = OrderedDict([("unidades", sum(x["unidades"] for x in filas.values())),
                          ("distintos", sum(x["distintos"] for x in filas.values())),
                          ("documentos_que_cambian", [a for a, x in filas.items() if x["distintos"]]),
                          ("por_documento", filas)])
out = OrderedDict([("solo_en_nuevo", [list(k) for k in solo_n]), ("solo_en_head", [list(k) for k in solo_h]),
                   ("por_origen", res)])
Path(sys.argv[2]).write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for o, r in res.items():
    print(o, "unidades", r["unidades"], "distintos", r["distintos"], "documentos que cambian", len(r["documentos_que_cambian"]))
    if o.startswith("tanda1"):
        for a, x in r["por_documento"].items():
            print(f"   {a:14s} u={x['unidades']:4d} dist={x['distintos']:4d} solo_linea={x['solo_la_linea_de_alcance']:4d} "
                  f"head_linea={x['con_linea_head']} nuevo_linea={x['con_linea_nuevo']} +{x['caracteres_agregados_por_unidad']}")
print("solo en nuevo:", out["solo_en_nuevo"], "solo en head:", len(solo_h))
