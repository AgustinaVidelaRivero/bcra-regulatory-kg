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
  F. registro de citas a Comunicaciones sobre la E0 de la tanda 0 y de r1;
  G. reglas (a) a (i) del detector r2 (decisiones sobre el freno posterior a
     R3), acumuladas en orden: aristas, citas resueltas e irresolubles antes y
     después de cada regla, en desarrollo y en diez; las remisiones falsas
     ric::3.1.6 → ric::4.2.1.3 y ric::9.1.1 → cap::S2 ausentes y
     cla::5.1.2.3 → cla::3.7 presente; las citas que cambian de resolución con
     la regla (g), en cada sentido; las citas nuevas de las reglas (c), (d) y
     (i), para su lectura.

«Regla firmada» es, desde las decisiones sobre el freno posterior a R3, la
regla con las nueve reglas del detector y, con `--e0-r2`, el texto de e0-r2.

Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/r2_codigo/r3d_remisiones.py --out <json> \
      [--e0-r2 <salida de correr_e0.py --version-e0 e0-r2 de la tanda 0>]
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
    orig = (C.TOS_ORDEN, C.E0_ENM01, C.SALIDA, REF.INVENTARIO_TOS, REF.TITULOS_TOS)
    try:
        if cfg["man"] is not None:
            man = MC.cargar(cfg["man"])
            C.TOS_ORDEN = tuple(man.orden_corrida)
            C.E0_ENM01 = Path(man.e0_salida)
            REF.INVENTARIO_TOS = {t["id"]: tuple(t["nombres_remision"])
                                  for t in sorted(man.tos, key=lambda t: t["id"])}
        C.SALIDA = cfg["entrada"]
        REF.TITULOS_TOS = REF.titulos_de_inventario(sorted(C.TOS_ORDEN))
        yield
    finally:
        C.TOS_ORDEN, C.E0_ENM01, C.SALIDA, REF.INVENTARIO_TOS, REF.TITULOS_TOS = orig


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


PASOS_REGLAS = ("", "a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg", "abcdefgh", "abcdefghi")


def chunks_e0_r2(d: Path | None) -> dict | None:
    if d is None:
        return None
    out = {}
    for to in C.TOS_ORDEN:
        p = Path(d) / f"chunks_{to}.json"
        if p.exists():
            x = json.loads(p.read_text(encoding="utf-8"))
            for c in x["chunks"] if isinstance(x, dict) else x:
                out[c["id"]] = c
    return out


def _origen(c: dict) -> str:
    return c.get("chunk_id") or C.prov_key(c["procedencia"])


def citas_de(r: dict) -> tuple[set, set]:
    """Citas comparables entre reglas (la evidencia cambia con la ventana):
    resueltas = (chunk, unidad de destino); irresolubles = (chunk, clase,
    norma nombrada, unidad de destino, causa)."""
    res = {(_origen(c), d["destino"]) for c in r["registro"] for d in c["destinos"]}
    irr = {(_origen(c), c["clase"], c["norma_nombrada"], x["destino"], x["causa"])
           for c in r["registro"] for x in c["irresolubles"]}
    return res, irr


def falsas_y_caso(r: dict, nodos: dict) -> dict:
    """Las remisiones falsas del freno posterior a R3 se controlan como citas
    (resueltas o irresolubles) del registro: en R3, ric::3.1.6 → ric::4.2.1.3
    era una cita interna irresoluble («punto inexistente en E0»), ric::3.1.2 →
    ric::4.1.1 otra («punto_sin_nodos») y la cita de ric::9.1.1 a las normas
    sobre «Incumplimientos de capitales mínimos…» resolvía a cap::S2. La
    arista ric::9.1.1 → cap::S2 se informa con la evidencia de sus citas."""
    def destinos_de(to: str, punto: str) -> list[str]:
        return sorted({e["properties"]["destino"] for e in r["nuevas"]
                       if any(p.get("to") == to and p.get("punto") == punto for p in e["provenances"])})

    def citas(to: str, punto: str) -> list[dict]:
        return [c for c in r["registro"] if c["procedencia"]["to"] == to and c["procedencia"]["punto"] == punto]

    def destinos_cita(c: dict) -> list[str]:
        return [d["destino"] for d in c["destinos"]] + [x["destino"] for x in c["irresolubles"] if x["destino"]]
    d316, d911, d5123 = destinos_de("ric", "3.1.6"), destinos_de("ric", "9.1.1"), destinos_de("cla", "5.1.2.3")
    incumpl = [c for c in citas("ric", "9.1.1")
               if C.norm(c.get("norma_nombrada") or "").startswith("incumplimientos")]
    return {"ric_3_1_6_destinos": d316,
            "ric_3_1_6_cita_a_ric_4_2_1_3_ausente": not any("ric::4.2.1.3" in destinos_cita(c)
                                                             for c in citas("ric", "3.1.6")),
            "ric_3_1_2_cita_a_ric_4_1_1_ausente": not any("ric::4.1.1" in destinos_cita(c)
                                                           for c in citas("ric", "3.1.2")),
            "ric_9_1_1_destinos": d911,
            "ric_9_1_1_cita_incumplimientos_a_cap_S2_ausente": not any("cap::S2" in destinos_cita(c) for c in incumpl),
            "ric_9_1_1_cita_incumplimientos": [{"destinos": destinos_cita(c), "irresolubles": c["irresolubles"]}
                                               for c in incumpl],
            "ric_9_1_1_a_cap_S2_evidencias": sorted({c["evidencia"] for c in citas("ric", "9.1.1")
                                                     if "cap::S2" in [d["destino"] for d in c["destinos"]]}),
            "cla_5_1_2_3_destinos": d5123, "cla_5_1_2_3_a_cla_3_7_presente": "cla::3.7" in d5123}


def en_el_texto(r: dict, chunks: dict) -> dict:
    """Control «remisiones que no están en el texto»: cada cita resuelta tiene
    su evidencia como tramo literal del texto de E0 de su chunk (texto propio
    o heredado) y la unidad de destino sale de la evidencia (los números de
    sus menciones de puntos, con rangos y paréntesis, o de sus secciones; para
    el TO entero, el nombre de la norma)."""
    malas_ev, malas_unidad, n = [], [], 0
    for c in r["registro"]:
        if not c["destinos"]:
            continue
        n += 1
        ch = chunks.get(c.get("chunk_id")) or {}
        partes = [h["texto"] for h in ch.get("herencia", [])] + [ch.get("texto") or ""]
        propio = REF._texto_e0_de(c["procedencia"], ch) if ch else ""
        if not (any(c["evidencia"] in t for t in partes) or c["evidencia"] in propio):
            malas_ev.append({"chunk_id": c.get("chunk_id"), "evidencia": c["evidencia"]})
        ev = REF.normalizar_e0(c["evidencia"], tolerar_linea_suelta=True)[0]
        unidades = set()
        for m in REF._re_puntos_r2(REF.REGLAS_R2).finditer(ev):
            unidades |= set(REF._expandir_puntos_r2(m.group(1), REF.REGLAS_R2))
        for m in REF.RE_SECCION.finditer(ev):
            unidades |= {f"S{x}" for x in m.groups() if x}
        for d in c["destinos"]:
            u = d["destino"].split("::", 1)[1]
            if u == "TO" or u in unidades:
                continue
            malas_unidad.append({"chunk_id": c.get("chunk_id"), "destino": d["destino"], "evidencia": c["evidencia"]})
    return {"citas_resueltas_registradas": n, "evidencia_no_literal": len(malas_ev),
            "unidad_fuera_de_la_evidencia": len(malas_unidad),
            "ejemplos": (malas_ev + malas_unidad)[:20]}


def citas_por_regla(base: dict, em: dict, e0r2: dict | None) -> dict:
    """G: pasos acumulados; cada paso contra el anterior. Devuelve también las
    citas de cada paso para el detalle de (c), (d), (g) e (i)."""
    pasos, prev, detalle = [], None, {}
    legado = {c["id"]: c for to in C.TOS_ORDEN for c in C.cargar_chunks_enm01(to)}
    for reglas in PASOS_REGLAS:
        r = correr(base, em, reglas=frozenset(reglas), chunks_e0_r2=e0r2)
        res, irr = citas_de(r)
        fila = {"reglas": reglas or "ninguna (regla de R3)", "aristas": len(r["nuevas"]),
                "citas_resueltas": len(res), "citas_irresolubles": len(irr),
                "citas_resueltas_resumen": r["resumen"]["citas_resueltas"],
                "citas_irresolubles_resumen": r["resumen"]["citas_irresolubles"],
                "irresolubles_por_causa": r["resumen"]["irresolubles_por_causa"],
                "texto_de_e0": r["resumen"]["texto_de_e0"], "texto_heredado": r["resumen"]["texto_heredado"],
                "en_el_texto": en_el_texto(r, {**legado, **(e0r2 or {})} if "b" in reglas else legado),
                "d1_con_limite_estricto_distinto_informativo":
                    r["resumen"]["d1_con_limite_estricto_distinto_informativo"]}
        if prev is not None:
            fila["contra_el_paso_anterior"] = {
                "pares": delta(prev[0]["pares"], r["pares"]),
                "citas_resueltas": delta(prev[1], res), "citas_irresolubles": delta(prev[2], irr),
                "citas_que_cambian": len(prev[1] ^ res) + len(prev[2] ^ irr)}
        pasos.append(fila)
        detalle[reglas] = (r, res, irr)
        prev = (r, res, irr)
    return {"pasos": pasos, "_detalle": detalle}


def citas_nuevas(antes: tuple, despues: tuple, limite: int = 400) -> dict:
    """Citas resueltas que aparecen y desaparecen entre dos pasos, con su
    evidencia (para leer si están en el texto)."""
    ra, rb = antes[0], despues[0]
    ev_b = {}
    for c in rb["registro"]:
        for d in c["destinos"]:
            ev_b.setdefault((_origen(c), d["destino"]), []).append(
                {"clase": c["clase"], "atribucion": c.get("atribucion"), "evidencia": c["evidencia"]})
    ev_a = {}
    for c in ra["registro"]:
        for d in c["destinos"]:
            ev_a.setdefault((_origen(c), d["destino"]), []).append(
                {"clase": c["clase"], "atribucion": c.get("atribucion"), "evidencia": c["evidencia"]})
    nuevas = sorted(despues[1] - antes[1])
    quitadas = sorted(antes[1] - despues[1])
    return {"nuevas": len(nuevas), "quitadas": len(quitadas),
            "detalle_nuevas": [{"cita": list(k), "evidencias": ev_b[k][:3]} for k in nuevas[:limite]],
            "detalle_quitadas": [{"cita": list(k), "evidencias": ev_a[k][:3]} for k in quitadas[:limite]]}


def formas_e(r: dict) -> dict:
    """(e): cada cita con anáfora de la norma o con la marca del propio TO
    («de las presentes normas»…), con su forma y cómo queda resuelta; conteo
    por forma. Sin las citas del texto heredado (i), que repiten las del bloque."""
    filas = []
    for c in r["registro"]:
        if c.get("atribucion") == "texto_heredado" or not (c.get("forma_anafora") or c.get("marca_propio_to")):
            continue
        filas.append({"chunk": _origen(c), "forma": c.get("forma_anafora") or c.get("marca_propio_to"),
                      "clase": c["clase"], "to_destino": c["to_destino"], "puntos": c["puntos"],
                      "secciones": c["secciones"], "destinos": [d["destino"] for d in c["destinos"]],
                      "irresolubles": [{"destino": x["destino"], "causa": x["causa"]} for x in c["irresolubles"]],
                      "evidencia": c["evidencia"][-160:]})
    filas.sort(key=lambda f: (f["forma"], f["chunk"], f["evidencia"]))
    return {"por_forma": dict(sorted(Counter(f["forma"] for f in filas).items())), "citas": filas}


def cambios_g(antes: dict, despues: dict) -> dict:
    """(g): por mención (chunk, clase, evidencia), el TO de destino o la causa
    antes y después de la regla; se listan los cambios en cada sentido."""
    def mapa(r):
        out = {}
        for c in r["registro"]:
            if c["clase"] not in ("externa", "externa_anaforica"):
                continue
            k = (_origen(c), c["clase"], c["evidencia"])
            out[k] = {"norma_nombrada": c["norma_nombrada"], "to_destino": c["to_destino"],
                      "causa": [x["causa"] for x in c["irresolubles"] if x["destino"] is None]}
        return out
    a, b = mapa(antes), mapa(despues)
    filas = {"resuelta_a_irresoluble": [], "irresoluble_a_resuelta": [], "cambia_de_to": []}
    for k in sorted(set(a) & set(b)):
        ta, tb = a[k]["to_destino"], b[k]["to_destino"]
        if ta == tb:
            continue
        f = {"chunk": k[0], "clase": k[1], "evidencia": k[2], "norma_nombrada": b[k]["norma_nombrada"],
             "antes": ta, "despues": tb, "causa_despues": b[k]["causa"]}
        filas["resuelta_a_irresoluble" if tb is None else "irresoluble_a_resuelta" if ta is None
              else "cambia_de_to"].append(f)
    return {"menciones_comparadas": len(set(a) & set(b)), "solo_antes": len(set(a) - set(b)),
            "solo_despues": len(set(b) - set(a)), **{k: v for k, v in filas.items()},
            "conteo": {k: len(v) for k, v in filas.items()}}


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
    ap.add_argument("--e0-r2", type=Path, default=None,
                    help="salida de correr_e0.py --version-e0 e0-r2 de la tanda 0 (regla b)")
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
        e0r2 = chunks_e0_r2(a.e0_r2)
        g = citas_por_regla(base, em, e0r2)
        det = g.pop("_detalle")
        re0 = det["abcdefghi"][0]
        out["B_pasos_desarrollo"] = {
            "termino_H4": delta(r7["pares"], rt["pares"]),
            "cada_procedencia_y_punto_propio_de_la_procedencia": delta(rt["pares"], rp["pares"]),
            "texto_de_E0_con_D1_regla_de_R3": delta(rp["pares"], det[""][0]["pares"]),
            "texto_de_E0_con_D1": delta(rp["pares"], re0["pares"]),
            "regla_firmada_contra_sellado": delta(sellados, re0["pares"]),
            "resumen_regla_firmada": re0["resumen"]}
        nodos = {n["id"]: n for n in kg["nodes"]}
        out["G_reglas_desarrollo"] = {
            **g, "controles": falsas_y_caso(re0, nodos),
            "controles_regla_de_R3": falsas_y_caso(det[""][0], nodos),
            "g_cambios_de_resolucion": cambios_g(det["abcdef"][0], det["abcdefg"][0]),
            "c_citas": citas_nuevas(det["ab"], det["abc"]), "d_citas": citas_nuevas(det["abc"], det["abcd"]),
            "e_citas": citas_nuevas(det["abcd"], det["abcde"]), "f_citas": citas_nuevas(det["abcde"], det["abcdef"]),
            "a_citas": citas_nuevas(det[""], det["a"]), "b_citas": citas_nuevas(det["a"], det["ab"]),
            "h_citas": citas_nuevas(det["abcdefg"], det["abcdefgh"]),
            "i_citas": citas_nuevas(det["abcdefgh"], det["abcdefghi"]),
            "e_formas": formas_e(re0)}
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
                       leer_termino=False, reglas=frozenset())
        e0r2 = chunks_e0_r2(a.e0_r2)
        g = citas_por_regla(base, em, e0r2)
        det = g.pop("_detalle")
        re0 = det["abcdefghi"][0]
        nodos = {n["id"]: n for n in kg["nodes"]}
        out["G_reglas_diez"] = {
            **g, "controles": falsas_y_caso(re0, nodos),
            "controles_regla_de_R3": falsas_y_caso(det[""][0], nodos),
            "g_cambios_de_resolucion": cambios_g(det["abcdef"][0], det["abcdefg"][0]),
            "a_citas": citas_nuevas(det[""], det["a"]), "b_citas": citas_nuevas(det["a"], det["ab"]),
            "c_citas": citas_nuevas(det["ab"], det["abc"]), "d_citas": citas_nuevas(det["abc"], det["abcd"]),
            "e_citas": citas_nuevas(det["abcd"], det["abcde"]), "f_citas": citas_nuevas(det["abcde"], det["abcdef"]),
            "h_citas": citas_nuevas(det["abcdefg"], det["abcdefgh"]),
            "i_citas": citas_nuevas(det["abcdefgh"], det["abcdefghi"]),
            "e_formas": formas_e(re0)}
        out["B_regla_de_R3_diez"] = {"contra_sellado": delta(sellados, det[""][0]["pares"])}
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
        re0 = correr(base, em, reglas=REF.REGLAS_R2, chunks_e0_r2=chunks_e0_r2(a.e0_r2))
        out["G_reglas_r1"] = {"reglas": "a a i (la E0 de r1 es byte-idéntica a la de la tanda 0 en los cinco TOs: "
                                        "e0_chunking/salida_enm01 y salida_tanda0)",
                              "controles": falsas_y_caso(re0, {n["id"]: n for n in kg["nodes"]})}
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
