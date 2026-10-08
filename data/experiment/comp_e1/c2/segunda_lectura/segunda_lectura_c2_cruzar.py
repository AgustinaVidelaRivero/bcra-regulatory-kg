"""Cruce de la segunda lectura (mesa) con la primera (instancia) por (unidad, ítem, código).
Uso: python3 cruzar.py <primera_lectura.jsonl> <segunda_lectura.jsonl> <dir_salida>
Escribe divergencias_c2.jsonl, acuerdo_c2.json, adjudicacion_c2_worksheet.json y adjudicacion_c2_worksheet.md.
No lee el archivo cerrado de códigos: todo se reporta por código."""
import collections
import json
import sys
from pathlib import Path


def fino(med, d, primera):
    if med == "M1":
        sub = d.get("subtipo") if primera else d.get("subtipo_sin_relacion")
        return d["clase"] + (":" + sub if sub else "")
    cat = d.get("categoria") if primera else d.get("categoria_omision")
    return d["clase"] + (":" + cat if cat else "")


def kappa(pares):
    n = len(pares)
    if not n:
        return None
    po = sum(1 for a, b in pares if a == b) / n
    ca = collections.Counter(a for a, _ in pares)
    cb = collections.Counter(b for _, b in pares)
    pe = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / (n * n)
    return {"n": n, "po": round(po, 4), "pe": round(pe, 4), "kappa": round((po - pe) / (1 - pe), 4) if pe < 1 else None}


def main():
    p1 = [json.loads(l) for l in open(sys.argv[1], encoding="utf-8")]
    p2 = [json.loads(l) for l in open(sys.argv[2], encoding="utf-8")]
    out = Path(sys.argv[3])
    k1 = {}
    for d in p1:
        item = d["i"] if d["medida"] == "M1" else d["ficha"]
        k = (d["medida"], d["chunk_id"], str(item), d["codigo"])
        assert k not in k1, k
        k1[k] = d
    k2 = {}
    for d in p2:
        k = (d["medicion"], d["unidad"], str(d["item"]), d["codigo"])
        assert k not in k2, k
        k2[k] = d
    assert set(k1) == set(k2), (len(set(k1) - set(k2)), len(set(k2) - set(k1)))
    orden_u = []
    for d in p2:
        if d["unidad"] not in orden_u:
            orden_u.append(d["unidad"])
    ou = {u: i for i, u in enumerate(orden_u)}

    def clave_orden(k):
        med, u, item, cod = k
        return (ou[u], med, item.zfill(4) if item.isdigit() else item, cod)

    keys = sorted(k2, key=clave_orden)
    acuerdo = {}
    pares = {"M1": {"clase": [], "fino": []}, "M2": {"clase": [], "fino": []}}
    por = collections.defaultdict(lambda: {"n": 0, "acuerdo_clase": 0, "acuerdo_fino": 0})
    div = []
    for k in keys:
        med, u, item, cod = k
        a, b = k1[k], k2[k]
        ca, cb = a["clase"], b["clase"]
        fa, fb = fino(med, a, True), fino(med, b, False)
        pares[med]["clase"].append((ca, cb))
        pares[med]["fino"].append((fa, fb))
        r = por[(med, cod)]
        r["n"] += 1
        r["acuerdo_clase"] += ca == cb
        r["acuerdo_fino"] += fa == fb
        if fa != fb:
            div.append({
                "medicion": med, "unidad": u, "item": b["item"], "codigo": cod,
                "difiere_la_clase": ca != cb,
                "primera_lectura": {"clase": ca, "subtipo_o_categoria": fa.partition(":")[2] or None, "ancla_salida": a["donde"]},
                "segunda_lectura": {"clase": cb, "subtipo_o_categoria": fb.partition(":")[2] or None, "ancla_salida": b["ancla_salida"],
                                    "caso_de_borde": b["caso_de_borde"],
                                    "cobertura_segun_solapamiento_del_material": b["cobertura_segun_solapamiento_del_material"],
                                    "leida_antes_de_las_reglas": b["leida_antes_de_las_reglas"]},
                "ancla_texto": b["ancla_texto"],
                "fragmento_fase_a": b.get("fragmento_fase_a"), "miembro": b.get("miembro"),
                "omision_t4": b.get("omision_t4"),
            })
    for (med, cod), r in sorted(por.items()):
        acuerdo.setdefault(med, {})[cod] = {
            "n": r["n"], "acuerdo_clase": r["acuerdo_clase"], "acuerdo_fino": r["acuerdo_fino"],
            "fraccion_clase": f"{r['acuerdo_clase']}/{r['n']}", "fraccion_fino": f"{r['acuerdo_fino']}/{r['n']}"}
    res = {"unidad": "U-COMP-E1, C2, segunda lectura a ciegas de la mesa: acuerdo con la primera lectura",
           "nota": "acuerdo_clase = misma clase (cinco de M1, cuatro de M2); acuerdo_fino = además mismo subtipo de sin_relacion (M1) o misma categoría de omision_otra_vez (M2). Divergencias = desacuerdo fino. Por código, sin abrir la tabla código-brazo.",
           "por_medicion_y_codigo": acuerdo, "totales": {}, "kappa_cohen": {},
           "matriz_confusion_clase": {}}
    for med in ("M1", "M2"):
        pc, pf = pares[med]["clase"], pares[med]["fino"]
        res["totales"][med] = {"n": len(pc), "acuerdo_clase": sum(a == b for a, b in pc), "acuerdo_fino": sum(a == b for a, b in pf),
                               "divergencias_fino": sum(a != b for a, b in pf), "divergencias_clase": sum(a != b for a, b in pc)}
        res["kappa_cohen"][med] = {"clase": kappa(pc), "fino": kappa(pf)}
        mc = collections.Counter(pc)
        res["matriz_confusion_clase"][med] = {f"{a} | {b}": n for (a, b), n in sorted(mc.items())}
    res["totales"]["global"] = {"n": len(keys), "divergencias_fino": len(div), "divergencias_clase": sum(d["difiere_la_clase"] for d in div)}
    (out / "acuerdo_c2.json").write_text(json.dumps(res, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    with open(out / "divergencias_c2.jsonl", "w", encoding="utf-8") as f:
        for d in div:
            f.write(json.dumps(d, ensure_ascii=False, sort_keys=True) + "\n")
    ws = []
    for i, d in enumerate(div, 1):
        e = dict(d)
        e["n"] = i
        e["veredicto_autora"] = {"clase": None, "subtipo_o_categoria": None, "nota": None}
        ws.append(e)
    (out / "adjudicacion_c2_worksheet.json").write_text(json.dumps(
        {"unidad": "U-COMP-E1, C2: adjudicación de la autora sobre las divergencias entre la primera lectura (instancia) y la segunda (mesa)",
         "instrucciones": "Completar veredicto_autora en cada entrada; el material completo de cada unidad está en data/experiment/comp_e1/c2/material/<unidad con :: reemplazado por __>.md, ordenado por código.",
         "n_divergencias": len(ws), "entradas": ws}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    L = ["# U-COMP-E1, C2 — hoja de adjudicación de divergencias (primera lectura contra segunda lectura)", "",
         f"{len(ws)} divergencias (M1 {sum(1 for d in ws if d['medicion']=='M1')}, M2 {sum(1 for d in ws if d['medicion']=='M2')}), en orden de unidad. Por código, sin el brazo. "
         "El material completo de cada unidad está en `data/experiment/comp_e1/c2/material/` (archivo `<unidad>.md` con `::` → `__`). Veredicto: clase (y subtipo o categoría) y, si hace falta, una nota.", ""]
    ult = None
    for e in ws:
        if e["unidad"] != ult:
            ult = e["unidad"]
            L += ["", f"## `{ult}`", ""]
        it = e["item"]
        cab = f"### {e['n']}. {e['medicion']} · ítem {it} · código {e['codigo']}"
        if e["medicion"] == "M1":
            cab += f" · supuesto «{e['fragmento_fase_a']}»" + (f" (miembro {e['miembro']})" if e.get("miembro") else "")
        else:
            cab += f" · omisión [{e['omision_t4']['atributos']}]"
        L += [cab, "", f"- Texto: {e['ancla_texto']}"]
        p, s = e["primera_lectura"], e["segunda_lectura"]
        L.append(f"- Primera lectura: **{p['clase']}**" + (f" ({p['subtipo_o_categoria']})" if p["subtipo_o_categoria"] else "") + f" — {p['ancla_salida']}")
        marcas = [m for m, v in (("caso de borde", s["caso_de_borde"]), ("cobertura según el solapamiento del material", s["cobertura_segun_solapamiento_del_material"]), ("leída antes de las reglas, reclasificada sin cambio", s["leida_antes_de_las_reglas"])) if v]
        L.append(f"- Segunda lectura: **{s['clase']}**" + (f" ({s['subtipo_o_categoria']})" if s["subtipo_o_categoria"] else "") + f" — {s['ancla_salida']}" + (f" [{'; '.join(marcas)}]" if marcas else ""))
        L += ["- Veredicto de la autora: ______", ""]
    (out / "adjudicacion_c2_worksheet.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(json.dumps(res["totales"], ensure_ascii=False))
    print(json.dumps(res["kappa_cohen"], ensure_ascii=False))


main()
