"""U-OMISIONES-COD, O1 — grupo B, ítems f y f′: cambios en la resolución de sujetos entre la cadena con el código de
HEAD y la cadena con los dos cambios (corridas sobre copias; ninguna escribe en el repo). Solo lee.

Atribución por fila de `resolucion_sujetos.jsonl` (clave: chunk_id, indice_relacion, predicado):
  f  : cambia `mencion_verificada` (la mención pasa a verificar por las contracciones);
  f′ : no cambia la verificación y la mención, sin el artículo, es «entidad» (R3 en singular).
Uso: python -B medir_grupo_B.py <dir r2 HEAD> <dir r2 con B> --out <json>
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from collections import Counter, OrderedDict
from pathlib import Path


def norm(s) -> str:
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s]", " ", s)).strip()


def sin_art(s) -> str:
    w = norm(s).split()
    return " ".join(w[1:] if w and w[0] in ("el", "la", "los", "las") else w)


def jl(p: Path) -> list[dict]:
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("antes", type=Path)
    ap.add_argument("despues", type=Path)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    k = lambda f: (f["chunk_id"], f["indice_relacion"], f["predicado"])  # noqa: E731
    A = {k(f): f for f in jl(a.antes / "resolucion_sujetos.jsonl")}
    B = {k(f): f for f in jl(a.despues / "resolucion_sujetos.jsonl")}
    assert set(A) == set(B), "las relaciones de sujeto no son las mismas"
    campos = ("mencion", "mencion_verificada", "regla_texto", "id_regla_texto", "resuelto_a", "metodo_resolucion",
              "desacuerdo_regla_modelo")
    cambios = []
    for key in sorted(A):
        fa, fb = A[key], B[key]
        d = [c for c in campos if fa.get(c) != fb.get(c)]
        if not d:
            continue
        item = "f" if "mencion_verificada" in d else ("f′" if sin_art(fa["mencion"]) == "entidad" else "otro")
        cambios.append({"item": item, "to": fa["to"], "chunk_id": fa["chunk_id"], "indice_relacion": fa["indice_relacion"],
                        "predicado": fa["predicado"], "campos": d, **{f"{c}_antes": fa.get(c) for c in campos},
                        **{f"{c}_despues": fb.get(c) for c in campos if c != "mencion"}})
    dec = lambda c: c["resuelto_a_antes"] != c["resuelto_a_despues"] or c["metodo_resolucion_antes"] != c["metodo_resolucion_despues"]  # noqa: E731
    rep = lambda p: json.loads((p / "reporte_ensamblado_r2.json").read_text(encoding="utf-8"))  # noqa: E731
    ra, rb = rep(a.antes), rep(a.despues)
    no_ver = lambda X: [f for f in X.values() if f["mencion"] and f["mencion_verificada"] == "no"]  # noqa: E731
    res = OrderedDict()
    res["relaciones_de_sujeto"] = len(A)
    res["filas_que_cambian"] = len(cambios)
    res["por_item"] = dict(Counter(c["item"] for c in cambios))
    res["f"] = OrderedDict([
        ("menciones_que_no_verifican", [len(no_ver(A)), len(no_ver(B))]),
        ("pasan_a_verificar", sum(1 for c in cambios if c["item"] == "f" and c["mencion_verificada_antes"] == "no"
                                  and c["mencion_verificada_despues"] in ("exacta", "tokens"))),
        ("cambian_de_nivel_sin_pasar", sum(1 for c in cambios if c["item"] == "f" and c["mencion_verificada_antes"] != "no")),
        ("de_ellas_cambian_metodo_o_destino", sum(1 for c in cambios if c["item"] == "f" and dec(c))),
        ("de_ellas_cambian_destino", sum(1 for c in cambios if c["item"] == "f"
                                         and c["resuelto_a_antes"] != c["resuelto_a_despues"])),
        ("por_transicion", dict(Counter(f"{c['metodo_resolucion_antes']} -> {c['metodo_resolucion_despues']}"
                                        for c in cambios if c["item"] == "f")))])
    fp = [c for c in cambios if c["item"] == "f′"]
    res["f_prima"] = OrderedDict([
        ("decisiones_que_cambian", sum(1 for c in fp if dec(c))),
        ("por_to", dict(Counter(c["to"] for c in fp if dec(c)))),
        ("por_destino", dict(Counter(c["resuelto_a_despues"] for c in fp if dec(c)))),
        ("marcas_de_desacuerdo_nuevas", sum(1 for c in fp if c["desacuerdo_regla_modelo_despues"]
                                            and not c["desacuerdo_regla_modelo_antes"])),
        ("marcas_por_to", dict(Counter(c["to"] for c in fp if c["desacuerdo_regla_modelo_despues"]
                                       and not c["desacuerdo_regla_modelo_antes"]))),
        ("filas_sin_cambio_de_decision_ni_marca", sum(1 for c in fp if not dec(c) and not (
            c["desacuerdo_regla_modelo_despues"] and not c["desacuerdo_regla_modelo_antes"])))])
    res["reporte"] = OrderedDict([
        ("desacuerdos_regla_modelo", [ra["resolucion_sujetos"]["desacuerdos_regla_modelo"],
                                      rb["resolucion_sujetos"]["desacuerdos_regla_modelo"]]),
        ("registro_no_mapeados_filas", [ra["registro_no_mapeados"]["filas"], rb["registro_no_mapeados"]["filas"]]),
        ("registro_por_estado", [ra["registro_no_mapeados"]["por_estado"], rb["registro_no_mapeados"]["por_estado"]]),
        ("propuestos", [ra["validacion_modelos_r2"]["nodos"], rb["validacion_modelos_r2"]["nodos"]]),
        ("por_metodo", [ra["resolucion_sujetos"]["por_metodo"], rb["resolucion_sujetos"]["por_metodo"]]),
        ("sujetos_por_nivel", None)])
    for nom, p in (("antes", a.antes), ("despues", a.despues)):
        kg = json.loads((p / "kg.json").read_text(encoding="utf-8"))
        res["reporte"][f"sujetos_propuestos_{nom}"] = sum(1 for n in kg["nodes"] if n["type"] == "Sujeto"
                                                         and n["properties"].get("nivel") == "propuesto")
        res["reporte"][f"padre_sugerido_{nom}"] = sum(1 for e in kg["edges"] if e["relation"] == "padre_sugerido")
    res["cambios"] = cambios
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k2: v for k2, v in res.items() if k2 != "cambios"}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
