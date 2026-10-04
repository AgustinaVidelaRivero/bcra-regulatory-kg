"""
candados_p3c.py — U-PROMPT-R2, P3c-1 (USD 0, sin API): diseño del punto h, los candados de los insumos que no entran al
hash del prefijo (hallazgos de U-TABLA-REPROC: filas F04b, F22, F22b y F23 de
`data/experiment/mantenimiento/tabla_reprocesamiento.md`).

Calcula, sobre la E0 que lee U-REEXT-T0 (`e0_chunking/salida_tanda0_r2b`, 2.439 unidades) y con `cap::tabla037` ya
forzada a residual (punto f), el conjunto fijo de unidades que ejercita cada rama del mensaje de E1
(`prompt_r2b.build_user_message_r2b`: rótulos de la herencia, línea del ítem con y sin cierres, mini-chunk a mitad de
oración, recorte, línea de alcance por rol, por clase y sin alcance, y cada variante del bloque de tablas y de los
FLAGS E0) y cada NOTA del mensaje de E3 (`prompt_e3.build_user_message`: la de siempre, sin la marca r2, y las de
`notas_r2`). Cada rama es una «marca»; el conjunto se elige por cobertura voraz (la unidad que cubre más marcas
nuevas, y ante empate la de id menor), así que es reproducible.

La NOTA de las omisiones de esquema depende de la salida de E1: el candado la ejercita con una validación sintética
(declarada abajo), no con una unidad.

No calcula ningún sha256 de candado: se sellan en P3c-2, sobre el texto final del ajuste.

Escribe solo en --salida (candados_p3c.json). Sobre una copia del repo (regla l).
Uso (desde la raíz de la copia):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p3c/candados_p3c.py --salida DIR
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

P3C = Path(__file__).resolve().parent
REPO = P3C.parents[3]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
for sub in ("e1_extractor", "e3_verificador"):
    sys.path.insert(0, str(REX / sub))
import comun_e1  # noqa: E402
import prompt_r2b as P  # noqa: E402

E0_R2B = REX / "e0_chunking" / "salida_tanda0_r2b"
TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
FORZADAS = frozenset({"cap::tabla037"})          # con el punto f aplicado
VALIDACION_SINTETICA = {
    "forma_salida": "r2", "entidades": [], "relaciones": [],
    "omisiones_no_prosa": ["[meta_normativo] (tramo del candado) — (nota del candado)"]}


def n1(k: int) -> str:
    return "1" if k == 1 else "n"


def marcas_e1(c: dict) -> set[str]:
    m: set[str] = set()
    mini = comun_e1.es_mini_chunk(c)
    m.add("unidad:mini" if mini else "unidad:punto")
    her = c.get("herencia") or []
    if not her:
        m.add("herencia:ninguna")
    elif mini:
        m.add("herencia:mini_a_mitad" if P.mini_a_mitad(c) else "herencia:mini_titulos")
    else:
        i = P.bloque_lista(c)
        if i is None:
            m.add("herencia:punto_contexto")
        else:
            m.add("herencia:item_con_cierres" if i < len(her) - 1 else "herencia:item")
    if her and c.get("herencia_recortada"):
        m.add("herencia:recorte")
    rol = P.ROL_POR_TO_R2.get(c["archivo"])
    m.add("alcance:ninguno" if rol is None else ("alcance:rol" if rol.get("rol_id") else "alcance:clase"))
    f = c.get("flags") or {}
    if not (f.get("contenido_tabular") or f.get("formula")):
        return m
    ser, forz, noser, hay_res = P.estado_tablas(f, FORZADAS)
    for t in ser:
        m.add(f"tabla:modo:{t['modo']}")
        det = False
        for k in ("celdas_propagadas", "celdas_con_alcance", "filas_subtitulo", "combinadas_sin_propagar"):
            if t.get(k):
                m.add(f"tabla:{k}:{n1(t[k])}")
                det = det or k in ("celdas_propagadas", "celdas_con_alcance")
        if not det and t["modo"] != "posicional":
            m.add("tabla:confiable_sin_detalle")
    hay_form = bool(f.get("formula"))
    if hay_res or hay_form:
        m.add("flags:" + "+".join(x for x, s in (("tabular_fuera" if ser else "tabular", hay_res),
                                                  ("formula", hay_form)) if s))
    if noser:
        m.add("flags:no_serializadas")
    if forz:
        m.add("flags:forzadas")
    if P.evidencia_tabular_vigente(c, FORZADAS):
        m.add("flags:evidencia_tabular")
    if f.get("evidencia_formula") and (hay_res or hay_form):
        m.add("flags:evidencia_formula")
    return m


def marcas_e3(c: dict) -> set[str]:
    m: set[str] = set()
    f = c.get("flags") or {}
    if f.get("contenido_tabular") or f.get("formula"):
        m.add("v3:nota_flags:" + "+".join(x for x, s in (("tabular", f.get("contenido_tabular")),
                                                        ("formula", f.get("formula"))) if s))
    ser, _forz, _noser, res = P.estado_tablas(f, FORZADAS)
    if not ser:
        if f.get("contenido_tabular") or f.get("formula"):
            m.add("r2:nota_flags:" + "+".join(x for x, s in (("tabular", f.get("contenido_tabular")),
                                                            ("formula", f.get("formula"))) if s))
    else:
        m.add("r2:tablas_confiables")
        riesgo = [t for t in ser if P.tiene_riesgo(t)]
        if riesgo:
            m.add(f"r2:riesgo_tablas:{n1(len(riesgo))}")
            for t in riesgo:
                for k in ("combinadas_sin_propagar", "filas_subtitulo"):
                    if t.get(k):
                        m.add(f"r2:riesgo:{k}:{n1(t[k])}")
        tipos = [x for x, s in (("residual", res), ("formula", f.get("formula"))) if s]
        if tipos:
            m.add("r2:ademas:" + "+".join(tipos))
    if P.es_encabezado_de_lista(c):
        m.add("r2:encabezado_de_lista")
    return m


def cobertura(marcas: dict[str, set[str]]) -> tuple[list[str], dict]:
    falta = set().union(*marcas.values())
    elegidas = []
    while falta:
        cid = min(marcas, key=lambda k: (-len(marcas[k] & falta), k))
        elegidas.append(cid)
        falta -= marcas[cid]
    return elegidas, {cid: sorted(marcas[cid]) for cid in elegidas}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", type=Path, required=True)
    sal = ap.parse_args().salida.resolve()
    if REPO in sal.parents or sal == REPO:
        raise SystemExit("--salida no puede estar dentro del repo")
    chunks = []
    for to in TOS:
        chunks += json.loads((E0_R2B / f"chunks_{to}.json").read_text(encoding="utf-8"))
    m1 = {c["id"]: marcas_e1(c) for c in chunks}
    m3 = {c["id"]: marcas_e3(c) for c in chunks}
    m3 = {k: v for k, v in m3.items() if v}
    e1, cob1 = cobertura(m1)
    e3, cob3 = cobertura(m3)
    out = {
        "comando": "data/experiment/prompt_r2/p3c/candados_p3c.py --salida DIR",
        "e0": str(E0_R2B.relative_to(REPO)), "unidades": len(chunks), "forzadas": sorted(FORZADAS),
        "e1": {"marcas": dict(sorted(Counter(x for v in m1.values() for x in v).items())),
               "conjunto_fijo": e1, "cobertura": cob1},
        "e3": {"marcas": dict(sorted(Counter(x for v in m3.values() for x in v).items())),
               "conjunto_fijo": e3, "cobertura": cob3,
               "validacion_sintetica_de_las_omisiones": VALIDACION_SINTETICA},
    }
    sal.mkdir(parents=True, exist_ok=True)
    (sal / "candados_p3c.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("E1:", len(out["e1"]["marcas"]), "marcas;", len(e1), "unidades:", e1)
    print("E3:", len(out["e3"]["marcas"]), "marcas;", len(e3), "unidades:", e3)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
