"""U-R2-CODIGO, R3.d — controles de las remisiones del perfil r2 sobre los
grafos sellados (solo lectura, en memoria; USD 0).

Usa `r1_referencias.detectar_y_resolver_r2` (cadena r2) sobre una copia de cada
grafo sin sus aristas `referencia` con `rol_fuente = referencia_cruzada`, con
las rutas y el inventario de cada ensamblado redirigidos en memoria (como
ensamblar_tanda0.plan_redirecciones). Controles:

  A. simulación de U-AUDIT-TIPOS-V3 sobre KG-Tanda0-Desarrollo-r1: con la
     variante de la cadena r1 (paráfrasis, procedencia primaria, puntos propios
     del nodo, sin `termino`) y los cuatro tipos de origen, los pares origen →
     destino son los de las 4.242 aristas selladas; con los siete tipos de
     contenido, +3.687 pares y 0 perdidos (p2_referencias_sim.json);
  B. pasos de la regla firmada, cada uno contra el anterior: `termino` (H4),
     cada procedencia, texto de E0 con atribución D1;
  C. casos: cla::5.1.1.1 → cla::3.7; cap::8.2.3.3 → cla::6.5.1 y cla::7.2.1 sin
     la remisión interna falsa; en diez, pares (origen, unidad de destino) que
     cambian entre la paráfrasis y el texto de E0;
  D. alcance de las aristas selladas recontado con la regla de §3 de la
     enmienda 2 (r1: 5.456 / 183 / 6);
  E. las 35 Condicion aisladas de desarrollo (U-AUDIT-TIPOS-V3, punto 3) y
     cuántas reciben remisión; los seis puntos de ext que solo figuran en
     `provenances` (laudo de r2, §4) como procedencia de alguna cita en r1;
  F. registro de citas a Comunicaciones sobre la E0 de la tanda 0 y de r1.

Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/r2_codigo/r3d_remisiones.py --out <json>
"""

from __future__ import annotations

import argparse
import contextlib
import copy
import json
import sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
for p in (REX / "corpus_v2", REX, REPO / "data" / "experiment" / "grafo_v2" / "code",
          REX / "e2_reduce", REX / "e1_extractor", REX / "e3_verificador"):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))
import r1_comun as C  # noqa: E402
import r1_referencias as REF  # noqa: E402
import r1_provenance as PROV  # noqa: E402
import r1_cola_flaggeada as COLA  # noqa: E402
import manifiesto_corpus as MC  # noqa: E402

T0 = REX / "corpus_tanda0"
GRAFOS = {
    "desarrollo": {"kg": T0 / "ens_desarrollo" / "r1" / "kg.json",
                   "man": REX / "manifiestos" / "tanda0_ens_desarrollo.json", "entrada": T0 / "salida_dirigida"},
    "diez": {"kg": T0 / "ens_diez" / "r1" / "kg.json",
             "man": REX / "manifiestos" / "tanda0_ens_diez.json", "entrada": T0 / "salida_dirigida"},
    "r1": {"kg": REX / "corpus_v2" / "salida_r1" / "kg.json", "man": None,
           "entrada": REX / "corpus_v2" / "salida"},
}
SHA = {"desarrollo": "eab2fdd0", "diez": "dd42d6d9", "r1": "0226e947"}
ORIG4 = ("Obligacion", "Restriccion", "Excepcion", "Operacion")
SEIS_EXT = ("3.18.1.1", "3.18.1.2", "4.5.3", "4.6.1.3", "4.7.2", "7.1.4")


@contextlib.contextmanager
def redirigido(nombre: str):
    cfg = GRAFOS[nombre]
    orig = (C.TOS_ORDEN, C.E0_ENM01, C.SALIDA, REF.INVENTARIO_TOS)
    try:
        if cfg["man"] is not None:
            man = MC.cargar(cfg["man"])
            C.TOS_ORDEN = tuple(man.orden_corrida)
            C.E0_ENM01 = Path(man.e0_salida)
            REF.INVENTARIO_TOS = {t["id"]: tuple(t["nombres_remision"])
                                  for t in sorted(man.tos, key=lambda t: t["id"])}
        C.SALIDA = cfg["entrada"]
        yield
    finally:
        C.TOS_ORDEN, C.E0_ENM01, C.SALIDA, REF.INVENTARIO_TOS = orig


def emisores() -> dict:
    por_to = {}
    for to in C.TOS_ORDEN:
        regs = C.cargar_extracciones_finales(to)
        regs, _ = COLA.inyectar_cola(to, regs)
        por_to[to] = {"registros": regs}
    return PROV._emisores(por_to)


def cargar(nombre: str) -> tuple[dict, dict, set]:
    kg = json.loads(GRAFOS[nombre]["kg"].read_text(encoding="utf-8"))
    sellados = {(e["source"], e["target"]) for e in kg["edges"]
                if e.get("rol_fuente") == "referencia_cruzada"}
    base = {"nodes": kg["nodes"], "edges": [e for e in kg["edges"]
                                            if e.get("rol_fuente") != "referencia_cruzada"]}
    return kg, base, sellados


def correr(base: dict, em: dict, **op) -> dict:
    kg = copy.deepcopy(base)
    r = REF.detectar_y_resolver(kg, perfil="r2", emisores=em, **op)
    r["pares"] = {(e["source"], e["target"]) for e in r["nuevas"]}
    return r


def delta(a: set, b: set) -> dict:
    return {"agregados": len(b - a), "perdidos": len(a - b), "comunes": len(a & b)}


def anclas(n: dict) -> set[str]:
    return {f"{p.get('to')}::{p.get('punto')}" for p in n.get("provenances", [])}


def caso_ejemplo(kg: dict, r: dict) -> dict:
    nodos = {n["id"]: n for n in kg["nodes"]}
    filas = [e for e in r["nuevas"]
             if "cla::5.1.1.1" in anclas(nodos[e["source"]]) and "cla::3.7" in anclas(nodos[e["target"]])]
    return {"aristas": len(filas),
            "cumple_criterio_par9": any(e["properties"]["destino"] == "cla::3.7"
                                        and e["properties"]["alcance"] == "interna"
                                        and "punto 3.7" in e["properties"]["evidencia"] for e in filas),
            "detalle": [{"source": e["source"], "source_type": nodos[e["source"]]["type"],
                         "target": e["target"], "target_type": nodos[e["target"]]["type"],
                         "properties": e["properties"], "provenance": e["provenance"]} for e in filas]}


def caso_cap_8233(kg: dict, r: dict) -> dict:
    nodos = {n["id"]: n for n in kg["nodes"]}
    filas = [e for e in r["nuevas"] if "cap::8.2.3.3" in anclas(nodos[e["source"]])]
    destinos = Counter(e["properties"]["destino"] for e in filas)
    return {"destinos": dict(sorted(destinos.items())),
            "llega_a_cla_6_5_1": "cla::6.5.1" in destinos, "llega_a_cla_7_2_1": "cla::7.2.1" in destinos,
            "remision_interna_falsa": sorted(d for d in destinos if d in ("cap::6.5.1", "cap::7.2.1")),
            "citas": [{k: c[k] for k in ("procedencia", "clase", "norma_nombrada", "to_destino", "puntos",
                                         "evidencia", "destinos", "irresolubles")}
                      for c in r["registro"] if c["procedencia"]["punto"] == "8.2.3.3"
                      and c["procedencia"]["to"] == "cap"]}


def pares_unidad(r: dict, tipos: dict, solo_tipos=None) -> set:
    out = set()
    for e in r["nuevas"]:
        if solo_tipos and tipos[e["source"]] not in solo_tipos:
            continue
        out.add((e["source"], e["properties"]["destino"]))
    return out


def alcance_sellado(kg: dict) -> dict:
    nodos = {n["id"]: n for n in kg["nodes"]}
    cuenta, cap_externa = Counter(), []
    for e in kg["edges"]:
        if e.get("rol_fuente") != "referencia_cruzada":
            continue
        d = e["properties"]["destino"]
        td = d.split("::")[0]
        a = REF.alcance_remision(td, e["provenance"]["to"], nodos[e["target"]]["type"] == "TextoOrdenado")
        cuenta[a] += 1
        if e["properties"]["clase"].startswith("externa") and a == "interna":
            cap_externa.append(d)
    return {"por_alcance": dict(sorted(cuenta.items())),
            "clase_externa_que_queda_interna": dict(sorted(Counter(cap_externa).items()))}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    out: dict = {"unidad": "U-R2-CODIGO", "etapa": "R3.d", "grafos": {k: SHA[k] for k in GRAFOS}}

    variante_r1 = dict(fuente="parafrasis", por_procedencia=False, propios="nodo", leer_termino=False)
    with redirigido("desarrollo"):
        kg, base, sellados = cargar("desarrollo")
        em = emisores()
        tipos = {n["id"]: n["type"] for n in kg["nodes"]}
        r4 = correr(base, em, tipos_origen=ORIG4, **variante_r1)
        r7 = correr(base, em, **variante_r1)
        out["A_simulacion_desarrollo"] = {
            "sellados": len(sellados), "cuatro_tipos_igual_a_sellados": r4["pares"] == sellados,
            "siete_tipos": delta(r4["pares"], r7["pares"]),
            "siete_tipos_por_tipo_origen": dict(sorted(Counter(tipos[s] for s, _ in r7["pares"] - r4["pares"]).items())),
            "esperado": {"agregados": 3687, "perdidos": 0}}
        rt = correr(base, em, fuente="parafrasis", por_procedencia=False, propios="nodo", leer_termino=True)
        rp = correr(base, em, fuente="parafrasis", por_procedencia=True, propios="procedencia", leer_termino=True)
        re0 = correr(base, em)
        out["B_pasos_desarrollo"] = {
            "termino_H4": delta(r7["pares"], rt["pares"]),
            "cada_procedencia_y_punto_propio_de_la_procedencia": delta(rt["pares"], rp["pares"]),
            "texto_de_E0_con_D1": delta(rp["pares"], re0["pares"]),
            "regla_firmada_contra_sellado": delta(sellados, re0["pares"]),
            "resumen_regla_firmada": re0["resumen"]}
        out["C_ejemplo_cla_5_1_1_1_desarrollo"] = caso_ejemplo(kg, re0)
        out["C_cap_8_2_3_3_desarrollo"] = caso_cap_8233(kg, re0)
        isl = json.loads((REPO / "reports" / "u_audit_tipos_v3" / "p3_filas.json").read_text(encoding="utf-8"))
        ids35 = sorted({f["id"] for f in isl})
        con = lambda pares: [i for i in ids35 if any(i in par for par in pares)]  # noqa: E731
        out["E_condiciones_aisladas_desarrollo"] = {
            "condiciones_aisladas_en_p3": len(ids35),
            "criterio": "alguna remisión, saliente o entrante (p3b_cruce.json: 8 salientes y 1 entrante)",
            "con_remision_siete_tipos_parafrasis": len(con(r7["pares"])),
            "con_remision_regla_firmada": len(con(re0["pares"])),
            "esperado_con_H1": 9}

    with redirigido("diez"):
        kg, base, sellados = cargar("diez")
        em = emisores()
        tipos = {n["id"]: n["type"] for n in kg["nodes"]}
        rpar = correr(base, em, tipos_origen=ORIG4, **variante_r1)
        re0_4 = correr(base, em, tipos_origen=ORIG4, fuente="e0", por_procedencia=False, propios="nodo",
                       leer_termino=False)
        re0 = correr(base, em)
        pa, pe = pares_unidad(rpar, tipos), pares_unidad(re0_4, tipos)
        origenes = {s for s, _ in pa} | {s for s, _ in pe}
        cambian = [o for o in sorted(origenes) if {d for s, d in pa if s == o} != {d for s, d in pe if s == o}]
        out["C_diez_cambio_de_destino"] = {
            "criterio": "pares (nodo de origen, unidad de destino) de los cuatro tipos de la cadena r1, "
                        "procedencia primaria: paráfrasis (cadena r1) contra texto de E0 (regla firmada)",
            "pares_cuatro_tipos_parafrasis_igual_a_sellados": rpar["pares"] == sellados,
            "pares_solo_parafrasis": len(pa - pe), "pares_solo_e0": len(pe - pa), "pares_en_ambos": len(pa & pe),
            "nodos_de_origen_con_destinos_distintos": len(cambian),
            "ejemplos_solo_parafrasis": sorted(pa - pe)[:15], "ejemplos_solo_e0": sorted(pe - pa)[:15]}
        out["C_cap_8_2_3_3_diez"] = caso_cap_8233(kg, re0)
        out["C_ejemplo_cla_5_1_1_1_diez"] = caso_ejemplo(kg, re0)
        out["B_regla_firmada_diez"] = {"contra_sellado": delta(sellados, re0["pares"]), "resumen": re0["resumen"]}
        out["F_comunicaciones_tanda0_diez"] = {k: v for k, v in re0["comunicaciones"].items() if k != "filas"}

    with redirigido("r1"):
        kg, base, sellados = cargar("r1")
        em = emisores()
        out["D_alcance_sellados"] = {"r1": alcance_sellado(kg)}
        rpar = correr(base, em, tipos_origen=ORIG4, **variante_r1)
        re0 = correr(base, em)
        procs = Counter((c["procedencia"]["punto"]) for c in re0["registro"]
                        if c["procedencia"]["to"] == "ext" and c["destinos"])
        out["E_seis_puntos_ext_r1"] = {
            "cuatro_tipos_parafrasis_igual_a_sellados": rpar["pares"] == sellados,
            "procedencia_de_citas_resueltas": {f"ext::{p}": procs.get(p, 0) for p in SEIS_EXT}}
        out["B_regla_firmada_r1"] = {"contra_sellado": delta(sellados, re0["pares"]), "resumen": re0["resumen"]}
        out["C_ejemplo_cla_5_1_1_1_r1"] = caso_ejemplo(kg, re0)
        out["F_comunicaciones_r1"] = {k: v for k, v in re0["comunicaciones"].items() if k != "filas"}
    for nombre in ("desarrollo", "diez"):
        kg = json.loads(GRAFOS[nombre]["kg"].read_text(encoding="utf-8"))
        out["D_alcance_sellados"][nombre] = alcance_sellado(kg)
    out["D_alcance_esperado_enmienda2"] = {"r1": {"interna": 5456, "externa": 183, "to_entero": 6},
                                           "desarrollo": {"interna": 4118, "externa": 120, "to_entero": 4},
                                           "diez": {"interna": 4631, "externa": 174, "to_entero": 14}}

    def conv(x):
        if isinstance(x, set):
            return sorted(x)
        if isinstance(x, tuple):
            return list(x)
        raise TypeError(type(x))
    Path(a.out).write_text(json.dumps(out, ensure_ascii=False, indent=1, default=conv) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
