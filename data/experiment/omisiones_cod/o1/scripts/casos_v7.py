"""U-OMISIONES-COD, O1 — los casos positivos y negativos que la v7 fija para cada selftest, comprobados sobre las
salidas de la corrida en seco: la cadena r2b de diez (y la sin cola, para K) con el código de HEAD y con el código de
O1, sobre copias. Para f, I, (h) y J, además, casos sintéticos con las funciones del código de O1 (importadas de la
copia con el código nuevo). Solo escribe --out.
Uso, desde la raíz de la copia con el código nuevo:
  python -B casos_v7.py --head <dir r2 HEAD diez> --nuevo <dir r2 nuevo diez> --nuevo-sincola <dir r2 nuevo sin cola>
      --out <json>
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import OrderedDict
from pathlib import Path


def jl(p: Path) -> list[dict]:
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--head", type=Path, required=True)
    ap.add_argument("--nuevo", type=Path, required=True)
    ap.add_argument("--nuevo-sincola", dest="sincola", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    raiz = Path.cwd().resolve()
    assert not (raiz / ".git").exists(), "correr en una copia"
    casos = []

    def caso(grupo, nombre, ok, detalle=""):
        casos.append({"grupo": grupo, "caso": nombre, "pasa": bool(ok), "detalle": str(detalle)[:300]})

    kg_h = json.loads((a.head / "kg.json").read_text(encoding="utf-8"))
    kg_n = json.loads((a.nuevo / "kg.json").read_text(encoding="utf-8"))
    nh = {n["id"]: n for n in kg_h["nodes"]}
    nn = {n["id"]: n for n in kg_n["nodes"]}

    # ---------------- A
    om = jl(a.nuevo / "omisiones.jsonl")
    fichas = json.loads((raiz / "data/experiment/reext_t0/t4/salida/fichas_punto8_omisiones.json").read_text(
        encoding="utf-8"))["fichas"]

    def omision(cid, tramo):
        import unicodedata, re  # noqa: E401, PLC0415
        f = lambda s: " ".join(re.sub(r"[^a-z0-9]+", " ", "".join(  # noqa: E731
            c for c in unicodedata.normalize("NFKD", s or "") if not unicodedata.combining(c)).lower()).split())
        xs = [o for o in om if o["chunk_id"] == cid and f(o["tramo"]) == f(tramo)]
        return xs[0] if len(xs) == 1 else None
    her = next(x for x in fichas if x["en"] == "heredado")
    pro = next(x for x in fichas if x["en"] == "propio")
    o_her, o_pro = omision(her["chunk_id"], her["tramo"]), omision(pro["chunk_id"], pro["tramo"])
    caso("A.a", f"positivo T4 {her['chunk_id']} (tramo en el heredado) marcado", o_her and o_her.get("tramo_en_heredado"))
    caso("A.a", f"negativo T4 {pro['chunk_id']} (tramo en el propio) sin marca", o_pro and not o_pro.get("tramo_en_heredado"))
    con = next(x for x in fichas if x["grupo"] == "con_marca")
    sin = next(x for x in fichas if x["grupo"] == "sin_marca" and "recomend" not in (x.get("clase") or ""))
    o_con, o_sin = omision(con["chunk_id"], con["tramo"]), omision(sin["chunk_id"], sin["tramo"])
    caso("A.b", f"positivo {con['chunk_id']} con marca del contador: revisar", o_con and any(
        m.startswith("contador:") for m in o_con.get("revisar", [])), o_con and o_con.get("revisar"))
    caso("A.b", f"negativo {sin['chunk_id']} sin marca y sin recomendación: sin revisar", o_sin and not o_sin.get("revisar"))
    for cid in ("ext::5.8.2.2", "ctacte::2.1.1.4"):
        xs = [o for o in om if o["chunk_id"] == cid]
        caso("A.c", f"positivo {cid}: texto propio entero", any(o.get("texto_propio_entero") for o in xs),
             [o.get("texto_propio_entero") for o in xs])
    neg_c = next((o for o in om if o["chunk_id"] == "pro::1.1.1"), None)
    caso("A.c", "negativo pro::1.1.1 (una omisión entre nodos extraídos): sin la marca",
         neg_c is not None and not neg_c.get("texto_propio_entero"), neg_c and neg_c["tramo"])
    sup = jl(a.nuevo / "supuestos_en_norma.jsonl")
    caso("A.d", "positivo T4 ext::10.5.5.2 e7 Obligacion (supuesto dentro de la norma) marcado",
         any(x["chunk_id"] == "ext::10.5.5.2" and x["local_id"] == "e7" for x in sup))
    caso("A.d", "negativo T4 ext::10.5.5.2 e2 Condicion con su relación: sin la marca",
         not any(x["chunk_id"] == "ext::10.5.5.2" and x["local_id"] == "e2" for x in sup))

    # ---------------- B (f′ sobre la resolución)
    k = lambda f: (f["chunk_id"], f["indice_relacion"])  # noqa: E731
    rh = {k(f): f for f in jl(a.head / "resolucion_sujetos.jsonl")}
    rn = {k(f): f for f in jl(a.nuevo / "resolucion_sujetos.jsonl")}
    def cambia_a(cid, destino):
        fs = [(rh[x], rn[x]) for x in rn if x[0] == cid and rn[x]["metodo_resolucion"] == "R3"
              and rh[x]["metodo_resolucion"] == "cuarentena"]
        return len(fs), all(b["resuelto_a"] == destino for _, b in fs)
    for cid, dest, n_esp in (("ext::7.9.4", "Sujeto_rol_entidad_autorizada_exterior", 4),
                             ("cap::6.7.2.2", "Sujeto_rol_alcance_capmin", 3), ("ctacte::1.5.2.9", "Sujeto_banco", 1)):
        n, ok = cambia_a(cid, dest)
        caso("B.f′", f"positivo {cid}: {n_esp} relación(es) de cuarentena a R3 → {dest}", n == n_esp and ok, n)
    for cid, idx_, men in (("ext::4.4.2", 8, "la/s entidad/es encargada/s…"), ("ext::11.1.1.10", 1, "la entidad nominada"),
                           ("ext::7.3.7", 6, "la entidad nominada por el exportador"),
                           ("ext::4.4.2", 16, "la mencionada entidad")):
        caso("B.f′", f"negativo {cid}#{idx_} «{men}»: sin cambio",
             rh[(cid, idx_)]["metodo_resolucion"] == rn[(cid, idx_)]["metodo_resolucion"] == "cuarentena")
    sys.path.insert(0, str(raiz / "data/experiment/reextraccion_v2/corpus_v2"))
    sys.path.insert(0, str(raiz / "data/experiment/pyd_r2/code"))
    import r1_e4 as E4  # noqa: E402, PLC0415
    import validador_r2 as V  # noqa: E402, PLC0415
    assert Path(E4.__file__).resolve().is_relative_to(raiz) and Path(V.__file__).resolve().is_relative_to(raiz)
    idx = {("label_exacto", "entidad financiera"): "Sujeto_entidad_financiera"}
    pref = E4._prefijos(idx)
    r = E4.resolver_mencion_r2("la entidad financiera", None, idx, pref, "Sujeto_rol_x")
    caso("B.f′", "negativo sintético «la entidad financiera»: R1, sin cambio", r["regla"] == "R1", r)
    r = E4.resolver_mencion_r2("esta entidad", None, idx, pref, "Sujeto_rol_x")
    caso("B.f′", "negativo sintético «esta entidad»: sin_match", r["regla"] is None and r["motivo"] == "sin_match", r)
    r = E4.resolver_mencion_r2("la entidad", None, idx, pref, None)
    caso("B.f′", "opción (ii): «la entidad» en un TO sin rol da sin_match", r["motivo"] == "sin_match", r)
    r = E4.resolver_mencion_r2("las entidades", None, idx, pref, None)
    caso("B.f′", "opción (ii), negativo: «las entidades» en un TO sin rol sigue en colectivo_sin_sujeto_por_defecto",
         r["motivo"] == "colectivo_sin_sujeto_por_defecto", r)
    reg = lambda men, modelo: {"chunk_id": "doc::1", "to": "doc", "archivo": "SIN_ALCANCE.pdf", "validacion": {  # noqa: E731
        "entidades": [{"local_id": "e1", "type": "Obligacion", "label": "x"}],
        "relaciones": [{"predicate": "aplica_a", "source": "e1", "target": None, "punto": "1", "indice_crudo": 0,
                        "sujeto_mencion": men, "mencion_verificada": "exacta", "sujeto_id_modelo": modelo}]}}
    vers = {"catalogo_sha256": "x"}
    for men, modelo, esperado in (("la entidad", "Sujeto_banco", ("R4_sugerencia_modelo", None)),
                                  ("la entidad", None, ("cuarentena", "sin_match")),
                                  ("las entidades", "Sujeto_banco", ("cuarentena", "colectivo_sin_sujeto_por_defecto"))):
        res = E4.resolver_relaciones_r2([reg(men, modelo)], idx, {}, vers, parte_a=True)
        got = (res["resolucion"][0]["metodo_resolucion"], (res["registro"][0]["motivo"] if res["registro"] else None))
        caso("B.f′", f"sintético sin alcance: «{men}» con sugerencia {modelo} → {esperado}", got == esperado, got)

    # ---------------- B (f) sintético
    for men, texto in (("el cuentacorrentista", "Obligaciones del cuentacorrentista"),
                       ("el Comité de auditoría", "las funciones del Comité de auditoría")):
        caso("B.f", f"positivo «{men}» contra «{texto}»: verifica",
             V.verificar_tramo(men, texto, 2, contracciones=True)[0] == "exacta"
             and V.verificar_tramo(men, texto, 2)[0] == "no")
    caso("B.f", "negativo: una mención que no está en el texto sigue sin verificar",
         V.verificar_tramo("el directorio", "Obligaciones del cuentacorrentista", 2, contracciones=True)[0] == "no")

    # ---------------- C y L sobre los elementos
    def elems(nodos, chunk):
        return [(n["id"], i, el) for n in nodos.values() if (n.get("provenance") or {}).get("chunk_id") == chunk
                for i, el in enumerate((n.get("properties") or {}).get("umbrales") or [])]
    def estado(el):
        return ("sin_base" if not el.get("base") else "resuelta" if el.get("base_destino") else
                "marcada" if el.get("base_no_resuelta") else "sin_destino_ni_marca")
    for cid, dest in (("ext::3.14.4", "ext::3.8"), ("ext::14.2.3", "ext::14.2.2"), ("ext::3.18.2.4", "ext::3.18.3")):
        caso("C.g", f"positivo {cid}: la base del validador resuelve a {dest}",
             any(el.get("base_destino") == dest for _, _, el in elems(nn, cid)))
    neg = [el for _, _, el in elems(nn, "cla::6.5::intro") if el.get("base")]
    caso("C.g", "negativo cla::6.5::intro («no superen el importe resultante de aplicar…»): marcada, sin destino",
         neg and all(estado(el) == "marcada" for el in neg), [estado(el) for el in neg])
    for cid in ("ext::3.3.3.4", "pro::3.2.1.3", "polcre::5.2", "docvig::3.5"):
        antes = [el for _, _, el in elems(nh, cid) if el.get("base") and str(el.get("regla_comparacion", "")).startswith("limite_relativo:")]
        despues = [el for _, _, el in elems(nn, cid) if str(el.get("regla_comparacion", "")).startswith("limite_relativo:")]
        caso("C.g1", f"positivo {cid}: base vacía, sin marca", antes and any(not el.get("base") and not el.get(
            "base_no_resuelta") for el in despues), [el.get("base") for el in antes][:2])
    for cid in ("ext::8.4.4", "cla::6.5::intro"):
        b = [el.get("base") for _, _, el in elems(nn, cid) if el.get("base")]
        caso("C.g1", f"negativo {cid}: conserva la base", bool(b), b[:1])
    g2 = [el for _, _, el in elems(nn, "cap::2.3.1") if el.get("base")]
    caso("C.g2", "positivo cap::2.3.1: deja de resolver a cap::6.5.1, marcada",
         g2 and all(estado(el) == "marcada" for el in g2) and any(
             el.get("base_destino") == "cap::6.5.1" for _, _, el in elems(nh, "cap::2.3.1")))
    cla37 = [el for n in nn.values() for el in (n.get("properties") or {}).get("umbrales") or []
             if el.get("base_destino") == "cla::3.7"]
    caso("C.g2", "negativos: las 4 de cla::3.7 siguen resueltas (con cla::5.1.2.3)", len(cla37) == 4, len(cla37))
    apr = [el for _, _, el in elems(nn, "cap::8.3.2.12") if el.get("base") == "APR"]
    caso("C.g3", "positivo: las dos «APR» de cap::8.3.2.12 marcadas, sin destino",
         len(apr) == 2 and all(estado(el) == "marcada" for el in apr), len(apr))
    for cid in ("cap::4.2.1.2::parte1", "cap::3.2.1.1", "polcre::2.1.9"):
        caso("C.g3", f"negativo {cid}: sigue resuelta a su Definicion",
             any(str(el.get("base_destino") or "").startswith("Definicion_") for _, _, el in elems(nn, cid)))
    l12 = [el for _, _, el in elems(nn, "cap::12.3") if el.get("valor") == "17" and el.get("origen") == "e1"]
    caso("L", "positivo cap::12.3: el 17 % guarda «El 17% en el caso de entidades del grupo B»",
         any("17%" in el["tramo"] and "grupo B" in el["tramo"] for el in l12), [el["tramo"] for el in l12])
    l65 = [el for _, _, el in elems(nn, "cla::6.5.4.7") if el.get("origen") == "e1"
           and el.get("tramo") == "entre el 5 % y menos del 20 % del patrimonio"]
    caso("L", "positivo cla::6.5.4.7: el 5 % y el 20 % guardan el mismo tramo compartido",
         sorted(el.get("valor") for el in l65) == ["20", "5"], [(el.get("valor"), el["tramo"]) for el in l65])
    def tramos(nodos, pred):
        return {(nid, i): el["tramo"] for nid, n in nodos.items() for i, el in enumerate(
            (n.get("properties") or {}).get("umbrales") or []) if pred(el)}
    desc_h, desc_n = tramos(nh, lambda el: el.get("origen") == "descripcion"), tramos(nn, lambda el: el.get("origen") == "descripcion")
    caso("L", "negativo: los elementos de origen descripción no cambian el tramo", desc_h == desc_n, len(desc_h))
    es_v = lambda el: str(el.get("regla_comparacion") or "").startswith("limite_relativo:")  # noqa: E731
    v_h, v_n = tramos(nh, es_v), tramos(nn, es_v)
    caso("L", "negativo: los elementos del validador no cambian el tramo",
         all(v_n.get(k2) == t for k2, t in v_h.items() if k2 in v_n), len(v_h))

    # ---------------- G-r
    g = json.loads((a.nuevo / "procedencia_g_r.json").read_text(encoding="utf-8"))
    for cid, pto in (("ctacte::2.1.1.4", "2.1.1.4"), ("ext::3.16.3.4", "3.16.3.4")):
        caso("G-r", f"positivo {cid}: el punto pasa a {pto}", any(x["chunk_id"] == cid and x["punto_g_r"] == pto
                                                                 and x["punto"] != pto for x in g))
    neg = [n for i, n in nn.items() if i.startswith("Excepcion_no_se_requiere_el_sello_de_la_casa_receptora")]
    caso("G-r", "negativo: la Excepcion de ctacte::2.1.1.6 con punto en su unidad no cambia",
         len(neg) == 1 and neg[0]["id"] in nh and neg[0]["provenance"] == nh[neg[0]["id"]]["provenance"]
         and not any(x["chunk_id"] == "ctacte::2.1.1.6" and x["type"] == "Excepcion" for x in g),
         neg and neg[0]["provenance"].get("punto"))

    # ---------------- H
    com_n = {i: n for i, n in nn.items() if n["type"] == "Comunicacion"}
    caso("H", "positivo norma externa (Decreto 28/23): tipo externa",
         com_n.get("Comunicacion_decreto_28_23", {}).get("properties", {}).get("tipo") == "externa")
    caso("H", "positivo «A-7000»: tipo A", com_n.get("Comunicacion_a_7000", {}).get("properties", {}).get("tipo") == "A")
    normales = [i for i, n in nh.items() if n["type"] == "Comunicacion" and n["properties"].get("tipo") == "A"]
    caso("H", "negativo: una «Comunicación A NNNN» con tipo de hoy no cambia",
         normales and all(nn[i]["properties"] == nh[i]["properties"] for i in normales if i in nn), len(normales))

    # ---------------- J
    ea = [e for e in kg_n["edges"] if e["relation"] == "remite_a"]
    por_punto: dict = {}
    for e in ea:
        p = e["provenance"]
        por_punto.setdefault((p.get("to"), p.get("punto"), p.get("chunk_id"), e["properties"]["evidencia"]), set()).add(
            p.get("tramo"))
    caso("J", "positivo: dos orígenes del mismo punto y la misma cita con tramos distintos dan dos procedencias",
         any(len({t for t in ts if t}) > 1 for ts in por_punto.values()))
    her_j = [e for e in ea if (e["provenance"].get("rol_documental") or "").startswith("herencia_")
             and e["provenance"].get("tramo") is None]
    caso("J", "positivo: la cita del texto heredado lleva la procedencia de su unidad con la marca sin tramo",
         her_j and all(e["provenance"].get("tramo_verificado") == "ausente" for e in her_j), len(her_j))

    # ---------------- K
    reg_s = json.loads((a.sincola / "remisiones_registro.json").read_text(encoding="utf-8"))
    causas = [x["causa"] for c in reg_s for x in c["irresolubles"]]
    caso("K", "positivo: en el sin cola, citas a una unidad de la cola con la causa propia",
         "destino_en_unidad_excluida" in causas, causas.count("destino_en_unidad_excluida"))
    caso("K", "negativo: la cita a un punto inexistente conserva su causa", "punto inexistente en E0" in causas)

    # ---------------- I y (h), sintéticos
    sys.path.insert(0, str(raiz / "scripts"))
    import metricas_intrinsecas as MI  # noqa: E402, PLC0415
    assert Path(MI.__file__).resolve().is_relative_to(raiz)
    kg_i = {"nodes": [{"id": "c1", "type": "Condicion"}, {"id": "c2", "type": "Condicion"}, {"id": "o", "type": "Obligacion"},
                      {"id": "t", "type": "TextoOrdenado"}],
            "edges": [{"source": "c1", "relation": "establecida_en", "target": "t"},
                      {"source": "c2", "relation": "condicion_de", "target": "o"}]}
    m = MI.condiciones_sin_regla(kg_i)
    caso("I", "sintético: la Condicion con solo establecida_en cuenta y la que tiene condicion_de no",
         m["nodos_sin_arista_de_contenido"] == ["c1"] and m["sin_condicion_de_saliente"] == 1, m)
    sys.path.insert(0, str(raiz / "data/experiment/tanda0/code"))
    import ensamblar_tanda0 as ENS  # noqa: E402, PLC0415
    assert Path(ENS.__file__).resolve().is_relative_to(raiz)
    kg_h2 = {"edges": [{"source": "a", "relation": "aplica_a", "target": "b"},
                       {"source": "a", "relation": "remite_a", "target": "c"},
                       {"source": "a", "relation": "establecida_en", "target": "t", "rol_fuente": "derivada_de_procedencia"},
                       {"source": "t", "relation": "referencia", "target": "x"},
                       {"source": "t", "relation": "contiene", "target": "s", "rol_fuente": "esqueleto"}]}
    caso("D.h", "sintético: una arista de cada clase", ENS.aristas_por_origen(kg_h2) == {
        "extraccion": 1, "remite_a": 1, "establecida_en_derivada": 1, "referencia_texto_ordenado_comunicacion": 1,
        "esqueleto": 1}, ENS.aristas_por_origen(kg_h2))

    res = OrderedDict([("casos", len(casos)), ("pasan", sum(c["pasa"] for c in casos)),
                       ("no_pasan", [c for c in casos if not c["pasa"]]), ("detalle", casos)])
    a.out.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{res['pasan']}/{res['casos']}")
    for c in casos:
        print(("PASA " if c["pasa"] else "FALLA"), c["grupo"], "|", c["caso"], "|", c["detalle"][:120] if not c["pasa"] else "")
    return 0


if __name__ == "__main__":
    sys.exit(main())
