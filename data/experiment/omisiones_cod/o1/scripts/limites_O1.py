"""U-OMISIONES-COD, O1 — los límites y residuos que deja el diseño, caso por caso, con su unidad, sus páginas (de E0) y
su mecanismo, o «sin leer». Lee las salidas de O1 y la E0 r2b de la copia; solo escribe --out.
Uso, desde la raíz de la copia con el código nuevo:
  python -B limites_O1.py --salidas <dir salidas O1> --nuevo <dir r2 nuevo diez> --head <dir r2 HEAD diez> --out <json>
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from collections import OrderedDict
from pathlib import Path


def jl(p: Path) -> list[dict]:
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]


def sin_art(s: str) -> str:
    return re.sub(r"^\s*(el|la|los|las)\s+", "", s or "", flags=re.I)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salidas", type=Path, required=True)
    ap.add_argument("--nuevo", type=Path, required=True)
    ap.add_argument("--head", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    raiz = Path.cwd().resolve()
    assert not (raiz / ".git").exists()
    sys.path.insert(0, str(raiz / "data/experiment/pyd_r2/code"))
    import validador_r2 as V  # noqa: PLC0415
    assert Path(V.__file__).resolve().is_relative_to(raiz)
    E0 = raiz / "data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b"
    chunks = {}
    for p in sorted(E0.glob("chunks_*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        chunks.update({c["id"]: c for c in (d["chunks"] if isinstance(d, dict) else d)})
    base = lambda cid: chunks.get(cid) or chunks.get(re.sub(r"::parte\d+$", "", cid or "")) or {}  # noqa: E731
    pag = lambda cid: base(cid).get("paginas")  # noqa: E731
    res = OrderedDict()

    # L: los elementos que conservan la cuantía
    rep = json.loads((a.nuevo / "reporte_ensamblado_r2.json").read_text(encoding="utf-8"))
    kg = json.loads((a.nuevo / "kg.json").read_text(encoding="utf-8"))
    nodos = {n["id"]: n for n in kg["nodes"]}
    filas = []
    for x in rep["umbrales"]["tramo_de_e1"].get("conservan_la_cuantia", []):
        cid = nodos[x["id"]]["provenance"].get("chunk_id")
        textos = [V.texto_completo(base(c)) for c in {p.get("chunk_id") for p in nodos[x["id"]]["provenances"]} if base(c)]
        nivel = max((V.verificar_tramo(x["tramo_e1"], t, 2)[0] for t in textos), key=V._ORDEN_NIVEL.__getitem__, default="no")
        filas.append({"unidad": cid, "paginas": pag(cid), "nodo": x["id"], "cuantia": x["cuantia"], "tramo_e1": x["tramo_e1"],
                      "mecanismo": ("el tramo de E1 no es literal: no verifica contra el texto de E0 del nodo"
                                    if nivel == "no" else f"el tramo de E1 verifica «{nivel}» y su literal mínimo pierde "
                                                         f"la cuantía (o su valor y unidad)")})
    res["L_conservan_la_cuantia"] = filas

    # f: del conjunto de 51 (mención que verifica sin el artículo inicial), las que siguen sin verificar
    rh = {(f["chunk_id"], f["indice_relacion"]): f for f in jl(a.head / "resolucion_sujetos.jsonl")}
    rn = {(f["chunk_id"], f["indice_relacion"]): f for f in jl(a.nuevo / "resolucion_sujetos.jsonl")}
    conj, quedan = [], []
    for k, f in rh.items():
        if f["mencion"] and f["mencion_verificada"] == "no":
            texto = V.texto_completo(base(f["chunk_id"]))
            if V.verificar_tramo(sin_art(f["mencion"]), texto, 2)[0] != "no":
                conj.append(k)
                if rn[k]["mencion_verificada"] == "no":
                    quedan.append({"unidad": f["chunk_id"], "paginas": pag(f["chunk_id"]), "indice_relacion": k[1],
                                   "mencion": f["mencion"], "mecanismo": "sin leer"})
    res["f_conjunto_de_51"] = {"n": len(conj), "pasan": len(conj) - len(quedan), "quedan": quedan}

    # (d) y (e): lo que no detectan dentro del conjunto de diseño de T4
    ga = json.loads((a.salidas / "grupo_A.json").read_text(encoding="utf-8"))
    tasas = json.loads((raiz / "data/experiment/reext_t0/t4/salida/tasas_t4.json").read_text(encoding="utf-8"))
    sup = {(s["chunk_id"]): [] for s in tasas["punto_7"]["por_supuesto"]["supuestos"]}
    for s in tasas["punto_7"]["por_supuesto"]["supuestos"]:
        sup[s["chunk_id"]].append(s)
    res["d_positivas_T4_no_detectadas"] = [
        {"unidad": x.split("#")[0], "entidad": x.split("#")[1], "paginas": pag(x.split("#")[0]),
         "supuestos_de_T4": [s["fragmento_fase_a"] for s in sup.get(x.split("#")[0], []) if x.split("#")[1] in s["donde"]],
         "mecanismo": "el supuesto no lleva un conector de la lista cerrada en la descripción ni en el tramo"}
        for x in ga["d_validacion_t4_punto7"]["positivas_no_detectadas"]]
    cal = json.loads((a.salidas / "e_calibracion_T4.json").read_text(encoding="utf-8"))
    t4 = {c["n"]: c for c in json.loads((raiz / "data/experiment/reext_t0/t4/salida/clasificacion_copia_nota_t4.json")
                                        .read_text(encoding="utf-8"))["casos"]}
    res["e_copias_reales_de_T4_no_detectadas"] = [
        {"caso_T4": c["n"], "unidad": t4[c["n"]]["chunk_id"], "paginas": pag(t4[c["n"]]["chunk_id"]),
         "entidad": t4[c["n"]]["local_id"], "campo": t4[c["n"]]["campo"], "razon_T4": t4[c["n"]]["razon"],
         "mecanismo": "la palabra que trae la nota es una derivación que la tolerancia de flexión toma como presente"}
        for c in cal["casos_T4_por_variante"]["ventana3+flexion"] if c["clase_T4"] == "copia real" and not c["detectado"]]
    res["e_falsos_positivos_de_T4"] = [
        {"caso_T4": c["n"], "unidad": t4[c["n"]]["chunk_id"], "clase_T4": c["clase_T4"], "razon_T4": t4[c["n"]]["razon"]}
        for c in cal["casos_T4_por_variante"]["ventana3+flexion"] if c["clase_T4"] != "copia real" and c["detectado"]]

    # (a): las omisiones con el tramo en el orden de lectura, que no se marcan
    om = jl(a.nuevo / "omisiones.jsonl")
    res["a_orden_de_lectura_sin_marca"] = []
    for o in om:
        t = o.get("tramo_modelo") or o.get("tramo")
        ch = base(o["chunk_id"])
        if t and ch and V.verificar_tramo(t, ch.get("texto") or "", 2)[0] == "no" and V._mini_a_mitad(ch):
            n_c = V.verificar_tramo(t, V.texto_completo(ch), 2)[0]
            n_l = V.verificar_tramo(t, V.texto_en_orden_de_lectura(ch), 2)[0]
            if V._ORDEN_NIVEL[n_l] > V._ORDEN_NIVEL[n_c]:
                res["a_orden_de_lectura_sin_marca"].append({"unidad": o["chunk_id"], "paginas": pag(o["chunk_id"]),
                                                            "categoria": o["categoria"], "tramo": o["tramo"][:160],
                                                            "mecanismo": "el tramo cruza el título y el texto propio del "
                                                                         "mini-chunk; no está solo en el heredado"})

    # H: las 26 con la marca
    res["H_tipo_no_derivable"] = [{"nodo": n["id"], "codigo": n["properties"].get("codigo"), "label": n.get("label"),
                                   "unidades": sorted({p.get("chunk_id") for p in n.get("provenances", []) if p.get("chunk_id")}),
                                   "mecanismo": "el código y la etiqueta no nombran una Comunicación ni una norma externa: "
                                                "remisión a un punto o una sección, o el nombre de un TO u otro documento"}
                                  for n in kg["nodes"] if n["type"] == "Comunicacion"
                                  and (n.get("properties_no_definidas") or {}).get("tipo_no_derivable")]
    a.out.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print({k: (len(v) if isinstance(v, list) else {kk: (len(vv) if isinstance(vv, list) else vv) for kk, vv in v.items()})
           for k, v in res.items()})
    return 0


if __name__ == "__main__":
    sys.exit(main())
