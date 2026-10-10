"""U-OMISIONES-COD, O1 — grupo A, marcas (a) a (d): qué detecta cada una sobre el diez r2b y cómo se compara con
las lecturas de T4 de U-REEXT-T0 (USD 0, sin API ni Neo4j).

Corre desde la raíz de una COPIA del repo. Reconstruye los registros de `entrada_r2` con el ensamblado de la copia
(las mismas redirecciones que `ensamblar_manifiesto_r2`) y aplica, sobre ellos, las reglas de diseño de este O1
(`reglas_grupo_A.py`, que O2 lleva al ensamblado). Controla que las omisiones reconstruidas sean byte a byte las de
`ens_diez_r2b/r2/omisiones.jsonl` (el registro de `a9631a64`).

Uso: PYTHONDONTWRITEBYTECODE=1 <python> -B <scripts>/medir_grupo_A.py --out <json>
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, OrderedDict
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import o1_comun as OC  # noqa: E402
import reglas_grupo_A as RA  # noqa: E402

T4 = Path("data/experiment/reext_t0/t4/salida")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    ENS, man, perfil, plan, M, V, RCMP, RC = OC.contexto("diez")
    with ENS.redirigido(plan):
        regs, chunks = OC.registros(ENS, perfil, RC, con_cola=True)
    omis = [{"chunk_id": r["chunk_id"], "to": to, **o} for to in regs for r in regs[to]
            for o in (r.get("validacion") or {}).get("omisiones", [])]
    guardado = (OC.T / "ens_diez_r2b" / "r2" / "omisiones.jsonl").read_text(encoding="utf-8")
    reconstruido = "".join(json.dumps(o, ensure_ascii=False) + "\n" for o in omis)
    res = OrderedDict()
    res["control_omisiones_iguales_al_registro_de_a9631a64"] = reconstruido == guardado
    res["omisiones"] = len(omis)
    res["por_categoria"] = dict(Counter(o["categoria"] for o in omis))

    # (a), (b) y (c) sobre cada omisión
    extr = {r["chunk_id"]: RA.con_extraccion(r.get("validacion")) for to in regs for r in regs[to]}
    filas = []
    for o in omis:
        ch = chunks[o["chunk_id"]]
        m = RA.marcas_omision(o, ch, V, extraccion=extr.get(o["chunk_id"], False))
        filas.append({**{k: o[k] for k in ("chunk_id", "to", "categoria")}, **m})
    meta = [f for f in filas if f["categoria"] == "meta_normativo"]

    def cuenta(fs, k):
        return sum(1 for f in fs if f.get(k))
    res["a_tramo_en_heredado"] = OrderedDict([
        ("todas_las_categorias", cuenta(filas, "tramo_en_heredado")),
        ("por_categoria", dict(Counter(f["categoria"] for f in filas if f["tramo_en_heredado"]))),
        ("meta_normativo", cuenta(meta, "tramo_en_heredado")),
        ("orden_de_lectura_aparte", dict(Counter(f["categoria"] for f in filas if f["donde_tramo"] == "orden_de_lectura"))),
        ("contador_del_validador_tramo_solo_heredado", sum(
            ((r.get("validacion") or {}).get("contadores") or {}).get("omisiones", {}).get("tramo_solo_heredado", 0)
            for to in regs for r in regs[to]))])
    rec_sin_contador = [f for f in meta if f["recomendacion"] and not f["marca_contador"]]
    res["b_revisar"] = OrderedDict([
        ("meta_normativo_con_marca_del_contador", cuenta(meta, "marca_contador")),
        ("meta_normativo_de_recomendacion", cuenta(meta, "recomendacion")),
        ("de_recomendacion_sin_marca_del_contador", len(rec_sin_contador)),
        ("de_recomendacion_por_patron", dict(Counter(p for f in meta for p in f["recomendacion"]))),
        ("revisar_total", cuenta(meta, "revisar")),
        ("recomendacion_en_otras_categorias", cuenta([f for f in filas if f["categoria"] != "meta_normativo"],
                                                      "recomendacion")),
        ("lista_de_recomendacion_sin_marca_del_contador", [{k: f[k] for k in ("chunk_id", "to", "tramo")}
                                                           for f in rec_sin_contador])])
    ent = [f for f in filas if f["unidad_entera"]]
    res["c_unidad_o_item_entero"] = OrderedDict([
        ("total", len(ent)), ("por_atributos", {f"es_item={i}|con_extraccion={x}": n for (i, x), n in
                                               sorted(Counter((f["es_item"], f["con_extraccion"]) for f in ent).items())}),
        ("por_categoria", dict(Counter(f["categoria"] for f in ent))),
        ("cobertura_por_tramo", dict(sorted(Counter(f"{f['cobertura']:.1f}" for f in filas
                                                   if f["cobertura"] is not None).items()))),
        ("lista", [{k: f[k] for k in ("chunk_id", "to", "categoria", "es_item", "con_extraccion", "tramo")} for f in ent]),
        ("ejemplos_v7", {c: [[f["categoria"], f["unidad_entera"], f["es_item"], f["con_extraccion"]] for f in filas
                             if f["chunk_id"] == c]
                         for c in ("ext::5.8.2.2", "ctacte::2.1.1.4")})])

    # validación de (a) y (b) contra las 60 fichas del punto 8 de T4
    fichas = json.loads((T4 / "fichas_punto8_omisiones.json").read_text(encoding="utf-8"))["fichas"]
    por_unidad = {}
    for f in filas:
        por_unidad.setdefault(f["chunk_id"], []).append(f)
    val = Counter()
    difs = []
    for fi in fichas:
        cands = [f for f in por_unidad.get(fi["chunk_id"], []) if f["categoria"] == "meta_normativo"
                 and RA.norm(f["tramo"]) == RA.norm(fi["tramo"])]
        if len(cands) != 1:
            val["sin_pareja_unica"] += 1
            difs.append({"chunk_id": fi["chunk_id"], "n": fi["n"], "grupo": fi["grupo"], "parejas": len(cands)})
            continue
        f = cands[0]
        t4_her = fi["en"] == "heredado"
        val[f"a:t4_{'heredado' if t4_her else 'propio'}:codigo_{'marca' if f['tramo_en_heredado'] else 'sin_marca'}"] += 1
        if t4_her != f["tramo_en_heredado"]:
            difs.append({"chunk_id": fi["chunk_id"], "n": fi["n"], "grupo": fi["grupo"], "t4_en": fi["en"],
                         "codigo_donde": f["donde_tramo"], "tramo": fi["tramo"][:200]})
        val[f"b:grupo_{fi['grupo']}:contador_{'si' if f['marca_contador'] else 'no'}"] += 1
        rec_t4 = "recomendaci" in (fi.get("clase") or "")
        val[f"b:recomendacion_t4_{'si' if rec_t4 else 'no'}:codigo_{'si' if f['recomendacion'] else 'no'}"] += 1
    res["validacion_t4_punto8"] = OrderedDict([("fichas", len(fichas)), ("cruce", dict(sorted(val.items()))),
                                               ("diferencias", difs)])

    # (d) supuesto_en_norma sobre las entidades de los registros
    dn = []
    for to in regs:
        for r in regs[to]:
            for e in (r.get("validacion") or {}).get("entidades", []):
                mk = RA.supuesto_en_norma(e, V)
                if mk:
                    dn.append({"chunk_id": r["chunk_id"], "to": to, "local_id": e.get("local_id"), "type": e["type"],
                               "label": e.get("label"), "marcadores": mk, "cola_humana": bool(r.get("cola_humana"))})
    res["d_supuesto_en_norma"] = OrderedDict([
        ("entidades_marcadas", len(dn)), ("por_tipo", dict(Counter(x["type"] for x in dn))),
        ("por_to", dict(Counter(x["to"] for x in dn))), ("unidades", len({x["chunk_id"] for x in dn})),
        ("por_marcador", dict(Counter(m for x in dn for m in x["marcadores"])))])
    t4 = json.loads((T4 / "tasas_t4.json").read_text(encoding="utf-8"))["punto_7"]["por_supuesto"]["supuestos"]
    positivos = set()
    for s in t4:
        if s["clase"] != "dentro_de_norma":
            continue
        for tipo, ids in RA.entidades_de_donde(s["donde"]):
            positivos |= {(s["chunk_id"], i) for i in ids}
    unidades_t4 = {s["chunk_id"] for s in t4}
    det = {(x["chunk_id"], x["local_id"]) for x in dn if x["chunk_id"] in unidades_t4}
    tp = det & positivos
    res["d_validacion_t4_punto7"] = OrderedDict([
        ("unidades", len(unidades_t4)), ("entidades_positivas_t4", len(positivos)),
        ("detectadas_en_esas_unidades", len(det)), ("detectadas_y_positivas", len(tp)),
        ("precision_aprox", f"{len(tp)}/{len(det)}"), ("wilson_precision", OC.wilson(len(tp), len(det))),
        ("cobertura", f"{len(tp)}/{len(positivos)}"), ("wilson_cobertura", OC.wilson(len(tp), len(positivos))),
        ("positivas_no_detectadas", sorted(f"{c}#{i}" for c, i in positivos - det)),
        ("detectadas_no_positivas", sorted(f"{c}#{i}" for c, i in det - positivos)),
        ("nota", "positivas: entidades nombradas en «dentro de la(s) <Tipo> eN» de los supuestos «dentro_de_norma» de "
                 "T4 (tasas_t4.json); «como <Tipo>» y «cada X como <Tipo>» no se cuentan (el supuesto pasó a ser la "
                 "entidad, sin marcador en su texto). Una detectada no positiva puede llevar un supuesto que la fase "
                 "A de T4 no separó: la precisión es aproximada")])
    res["d_lista"] = dn
    sha = OC.escribir_json(a.out, res)
    print(json.dumps({k: v for k, v in res.items() if k not in ("d_lista",)}, ensure_ascii=False)[:6000])
    print("sha256", sha)
    return 0


if __name__ == "__main__":
    sys.exit(main())
