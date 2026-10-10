"""U-OMISIONES-COD, O2 — los archivos de la salida `r2/` del ensamblado (salvo `kg.json`), HEAD contra el código nuevo,
con su causa. Solo lee.
  - omisiones.jsonl: las mismas filas en el mismo orden; sin las claves de A (`tramo_en_heredado`, `revisar`,
    `texto_propio_entero`), byte a byte las de HEAD;
  - remisiones_registro.json: citas cuya causa de irresoluble cambia (K: `destino_en_unidad_excluida`, solo sin la
    cola), y citas que salen, entran o cambian de orígenes, destinos o atribución (G-r y el agrupamiento sin el rol),
    cita por cita y con su causa (`citas_cita_por_cita`);
  - resolucion_sujetos.jsonl y no_mapeados_sujetos.jsonl (también por TO): filas que cambian, con su causa (f y f′);
  - archivos nuevos: supuestos_en_norma.jsonl (A, d) y procedencia_g_r.json (G-r);
  - reporte_ensamblado_r2.json: claves nuevas y claves que cambian de valor.
Uso: python -B registros_declarados.py <dir r2 HEAD> <dir r2 nuevo> --out <json>
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter, OrderedDict
from pathlib import Path

CLAVES_A = ("tramo_en_heredado", "revisar", "texto_propio_entero")


def jl(p: Path) -> list[dict]:
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]


def citas_cita_por_cita(rh: list[dict], rn: list[dict], ren: dict, dir_nuevo: Path) -> dict:
    """Cada cita del registro de remisiones que cambia, con su causa:
      G-r              la cita sale o entra porque el grupo (chunk, punto) pierde o gana el nodo que G-r cambió de punto
                       (`procedencia_g_r.json`); o sus orígenes, sus destinos, su atribución D1 o el rol de su procedencia
                       cambian porque el grupo gana o pierde ese nodo, porque G-r corrige el rol de sus nodos o porque un
                       nodo de G-r entra o sale de los destinos;
      re-tecleada      igual con los ids nuevos de G-r;
      agrupamiento     el mismo texto, leído antes por dos grupos partidos por el rol y ahora por uno (nota del 10/10/2026);
      K                la causa del irresoluble pasa de `punto_sin_nodos` a `destino_en_unidad_excluida`.
    Todo lo demás, «sin_causa»."""
    gr = json.loads((dir_nuevo / "procedencia_g_r.json").read_text(encoding="utf-8"))
    mov = [x for x in gr if x["punto"] != x["punto_g_r"]]
    claves_viejas = {(x["chunk_id"], x["punto"]) for x in mov}
    claves_nuevas = {(x["chunk_id"], x["punto_g_r"]) for x in mov}
    claves_rol = {(x["chunk_id"], x["punto_g_r"]) for x in gr if x["rol"] != x["rol_g_r"]}
    ids_gr = set(ren) | set(ren.values())
    m = lambda x: ren.get(x, x)  # noqa: E731
    clave = lambda c: (c.get("chunk_id"), c["evidencia"], json.dumps(c.get("puntos")), json.dumps(c.get("secciones")),  # noqa: E731
                       c.get("procedencia", {}).get("punto"))

    def forma(c: dict, mapear: bool) -> str:
        f = (lambda x: m(x)) if mapear else (lambda x: x)
        return json.dumps({"atribucion": c.get("atribucion"), "origenes": sorted(map(f, c["origenes"])),
                           "destinos": [{**d, "nodos": sorted(map(f, d.get("nodos") or []))} for d in c["destinos"]],
                           "irresolubles": c["irresolubles"]}, sort_keys=True, ensure_ascii=False)
    gh, gn = {}, {}
    for c in rh:
        gh.setdefault(clave(c), []).append(c)
    for c in rn:
        gn.setdefault(clave(c), []).append(c)
    filas, causas = [], Counter()
    for k in sorted(set(gh) | set(gn), key=str):
        h, n = gh.get(k, []), gn.get(k, [])
        if sorted(json.dumps(x, sort_keys=True, ensure_ascii=False) for x in h) == sorted(
                json.dumps(x, sort_keys=True, ensure_ascii=False) for x in n):
            continue
        fila = {"chunk_id": k[0], "punto": k[4], "evidencia": k[1][:120], "registros_head": len(h), "registros_nuevo": len(n)}
        if not n:
            causa = "G-r" if (k[0], k[4]) in claves_viejas else "sin_causa"
        elif not h:
            causa = "G-r" if (k[0], k[4]) in claves_nuevas else "sin_causa"
        elif sorted(forma(x, True) for x in h) == sorted(forma(x, False) for x in n):
            causa = "re-tecleada"
        else:
            cz = set()
            if len(h) != len(n):
                cz.add("agrupamiento")
            ih = Counter(json.dumps(i, sort_keys=True) for x in h for i in x["irresolubles"])
            inn = Counter(json.dumps(i, sort_keys=True) for x in n for i in x["irresolubles"])
            if ih != inn:
                k_ = Counter(json.dumps({**json.loads(i), "causa": "destino_en_unidad_excluida"}, sort_keys=True)
                             if json.loads(i)["causa"] == "punto_sin_nodos" else i for i in ih.elements())
                if k_ == inn or Counter(json.dumps({**json.loads(i), "causa": "destino_en_unidad_excluida"}, sort_keys=True)
                                        if json.loads(i)["causa"] == "punto_sin_nodos" and inn.get(json.dumps(
                                            {**json.loads(i), "causa": "destino_en_unidad_excluida"}, sort_keys=True))
                                        else i for i in ih.elements()) == inn:
                    cz.add("K")
            # el grupo (chunk, punto) de la cita gana o pierde un nodo que G-r cambió de punto, o G-r corrige el rol
            # de sus nodos: sus orígenes, la atribución D1 y el rol de la procedencia se recalculan
            grupo_gr = (k[0], k[4]) in claves_viejas | claves_nuevas
            oh = {m(o) for x in h for o in x["origenes"]} | {m(i) for x in h for d in x["destinos"] for i in d.get("nodos") or []}
            on = {o for x in n for o in x["origenes"]} | {i for x in n for d in x["destinos"] for i in d.get("nodos") or []}
            if oh != on:
                cz.add("G-r" if (oh ^ on) <= ids_gr or grupo_gr else "sin_causa")
            om = sorted(sorted(map(m, x["origenes"])) for x in h)
            if oh == on and om != sorted(sorted(x["origenes"]) for x in n):
                cz.add("G-r" if grupo_gr else "sin_causa")
            if {x["procedencia"].get("rol_documental") for x in h} != {x["procedencia"].get("rol_documental") for x in n}:
                cz.add("G-r" if (k[0], k[4]) in claves_rol | claves_viejas | claves_nuevas else "sin_causa")
            if len(h) == len(n) and {x.get("atribucion") for x in h} != {x.get("atribucion") for x in n}:
                cz.add("G-r" if grupo_gr else "sin_causa")
            if not cz:
                cz.add("sin_causa")
            causa = " y ".join(sorted(cz))
        fila["causa"] = causa
        causas[causa] += 1
        filas.append(fila)
    return OrderedDict([("por_causa", dict(sorted(causas.items()))), ("sin_causa", [f for f in filas if "sin_causa" in f["causa"]]),
                        ("lista", filas)])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("head", type=Path)
    ap.add_argument("nuevo", type=Path)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    res = OrderedDict()
    fh = {str(p.relative_to(a.head)) for p in a.head.rglob("*") if p.is_file()}
    fn = {str(p.relative_to(a.nuevo)) for p in a.nuevo.rglob("*") if p.is_file()}
    sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()  # noqa: E731
    res["archivos"] = OrderedDict([("solo_en_head", sorted(fh - fn)), ("nuevos", sorted(fn - fh)),
                                   ("iguales", sorted(f for f in fh & fn if sha(a.head / f) == sha(a.nuevo / f))),
                                   ("distintos", sorted(f for f in fh & fn if sha(a.head / f) != sha(a.nuevo / f)))])
    oh, on = jl(a.head / "omisiones.jsonl"), jl(a.nuevo / "omisiones.jsonl")
    sin_a = [{k: v for k, v in o.items() if k not in CLAVES_A} for o in on]
    res["omisiones"] = OrderedDict([("filas", [len(oh), len(on)]), ("sin_las_claves_de_A_iguales_a_head", sin_a == oh),
                                    ("con_cada_clave", {k: sum(1 for o in on if k in o) for k in CLAVES_A})])
    rh = json.loads((a.head / "remisiones_registro.json").read_text(encoding="utf-8"))
    rn = json.loads((a.nuevo / "remisiones_registro.json").read_text(encoding="utf-8"))
    k = lambda c: (c.get("chunk_id"), c["evidencia"], json.dumps(c.get("puntos")), json.dumps(c.get("secciones")),  # noqa: E731
                   c.get("procedencia", {}).get("punto"))
    mh, mn = Counter(map(k, rh)), Counter(map(k, rn))
    causas_h = Counter(x["causa"] for c in rh for x in c["irresolubles"])
    causas_n = Counter(x["causa"] for c in rn for x in c["irresolubles"])
    res["remisiones_registro"] = OrderedDict([
        ("citas", [len(rh), len(rn)]), ("citas_por_clave_solo_en_head", sum((mh - mn).values())),
        ("citas_por_clave_solo_en_nuevo", sum((mn - mh).values())),
        ("irresolubles_por_causa_head", dict(sorted(causas_h.items()))),
        ("irresolubles_por_causa_nuevo", dict(sorted(causas_n.items()))),
        ("con_la_causa_de_K", causas_n.get("destino_en_unidad_excluida", 0))])
    # causa por fila: f si cambia la verificación de la mención de esa relación (`mencion_verificada` en
    # resolucion_sujetos); si no, f′ si cambia la regla del texto (R3 en singular) o el método pasa a R3
    cl = lambda f: (f["chunk_id"], f.get("indice_relacion"), f.get("predicado"))  # noqa: E731
    rsh = {cl(f): f for f in jl(a.head / "resolucion_sujetos.jsonl")}
    rsn = {cl(f): f for f in jl(a.nuevo / "resolucion_sujetos.jsonl")}

    def causa_suj(x) -> str:
        fh, fn = rsh.get(x, {}), rsn.get(x, {})
        if fh.get("mencion_verificada") != fn.get("mencion_verificada"):
            return "f"
        if (fh.get("regla_texto"), fh.get("id_regla_texto")) != (fn.get("regla_texto"), fn.get("id_regla_texto")) \
                or fn.get("metodo_resolucion") == "R3" != fh.get("metodo_resolucion"):
            return "f′"
        return "sin_causa"
    for nombre in ("resolucion_sujetos.jsonl", "no_mapeados_sujetos.jsonl"):
        h, n = jl(a.head / nombre), jl(a.nuevo / nombre)
        dh, dn = {cl(f): f for f in h}, {cl(f): f for f in n}
        cambian = [x for x in set(dh) & set(dn) if dh[x] != dn[x]]
        todas = [("sale", x) for x in set(dh) - set(dn)] + [("entra", x) for x in set(dn) - set(dh)] + [("cambia", x) for x in cambian]
        cz = Counter(f"{lado}|{causa_suj(x)}" for lado, x in todas)
        res[nombre] = OrderedDict([("filas", [len(h), len(n)]), ("salen", len(set(dh) - set(dn))),
                                   ("entran", len(set(dn) - set(dh))), ("cambian", len(cambian)),
                                   ("por_causa", dict(sorted(cz.items()))),
                                   ("sin_causa", sorted("|".join(map(str, x)) for lado, x in todas if causa_suj(x) == "sin_causa"))])
    # ids de G-r (los nodos que cambian de punto), por tipo y etiqueta
    kh = json.loads((a.head / "kg.json").read_text(encoding="utf-8"))["nodes"]
    kn0 = json.loads((a.nuevo / "kg.json").read_text(encoding="utf-8"))["nodes"]
    ih0, in0 = {x["id"]: x for x in kh}, {x["id"]: x for x in kn0}
    por0 = {}
    for i in set(ih0) - set(in0):
        por0.setdefault((ih0[i]["type"], ih0[i]["label"]), []).append(i)
    ren0 = {por0[(in0[j]["type"], in0[j]["label"])][0]: j for j in set(in0) - set(ih0)
            if len(por0.get((in0[j]["type"], in0[j]["label"]), [])) == 1}
    res["remisiones_registro"]["citas_cita_por_cita"] = citas_cita_por_cita(rh, rn, ren0, a.nuevo)
    kn = json.loads((a.nuevo / "kg.json").read_text(encoding="utf-8"))["nodes"]
    ih, inn = {x["id"]: x for x in kh}, {x["id"]: x for x in kn}
    por = {}
    for i in set(ih) - set(inn):
        por.setdefault((ih[i]["type"], ih[i]["label"]), []).append(i)
    ren = {por[(inn[j]["type"], inn[j]["label"])][0]: j for j in set(inn) - set(ih)
           if len(por.get((inn[j]["type"], inn[j]["label"]), [])) == 1 and inn[j]["type"] != "Sujeto"}
    m = lambda x: ren.get(x, x)  # noqa: E731
    dc_h = json.loads((a.head / "aristas_derivadas_cola_humana.json").read_text(encoding="utf-8"))
    dc_n = json.loads((a.nuevo / "aristas_derivadas_cola_humana.json").read_text(encoding="utf-8"))
    kc_h = {(m(x["source"]), x["relation"], m(x["target"])) for x in dc_h}
    kc_n = {(x["source"], x["relation"], x["target"]) for x in dc_n}
    eh = {(m(e["source"]), e["relation"], m(e["target"])) for e in json.loads((a.head / "kg.json").read_text(encoding="utf-8"))["edges"]}
    en = {(e["source"], e["relation"], e["target"]) for e in json.loads((a.nuevo / "kg.json").read_text(encoding="utf-8"))["edges"]}
    res["aristas_derivadas_cola_humana"] = OrderedDict([
        ("filas", [len(dc_h), len(dc_n)]), ("ids_de_G_r", len(ren)),
        ("con_los_ids_de_G_r_solo_en_head", sorted("|".join(x) for x in kc_h - kc_n)),
        ("con_los_ids_de_G_r_solo_en_nuevo", sorted("|".join(x) for x in kc_n - kc_h)),
        ("todas_son_aristas_que_entran_o_salen_del_kg", (kc_h - kc_n) <= (eh - en) and (kc_n - kc_h) <= (en - eh))])
    ad_h = json.loads((a.head / "adjudicacion_cross_to.json").read_text(encoding="utf-8"))
    ad_n = json.loads((a.nuevo / "adjudicacion_cross_to.json").read_text(encoding="utf-8"))
    res["adjudicacion_cross_to"] = OrderedDict([("filas", [len(ad_h), len(ad_n)]),
                                                ("ids_solo_en_head", sorted({x["id"] for x in ad_h} - {x["id"] for x in ad_n})),
                                                ("ids_solo_en_nuevo", sorted({x["id"] for x in ad_n} - {x["id"] for x in ad_h}))])
    ph = json.loads((a.head / "reporte_ensamblado_r2.json").read_text(encoding="utf-8"))
    pn = json.loads((a.nuevo / "reporte_ensamblado_r2.json").read_text(encoding="utf-8"))
    res["reporte"] = OrderedDict([("claves_nuevas", sorted(set(pn) - set(ph))),
                                  ("claves_que_cambian", sorted(x for x in set(ph) & set(pn) if ph[x] != pn[x] and x != "redirecciones"))])
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(res, ensure_ascii=False)[:3000])
    return 0


if __name__ == "__main__":
    sys.exit(main())
