"""
cifras_c3.py — U-COMP-E1, C3: cifras finales con la lectura adjudicada, criterio aplicado tal cual está sellado, tabla por
brazo y corrida, cifra complementaria del texto propio (fuera del criterio), M3 y M4 descriptivos y costo real. USD 0, sin API.

Orden obligatorio (mandato, etapas :105 y notas al pie hasta la adjudicación):
  1. Control previo: la lectura adjudicada es la primera lectura (sha256 esperado) con exactamente las líneas adjudicadas cambiadas
     y nada más: mismas 804 líneas, las no adjudicadas byte a byte iguales, y en cada adjudicada el campo `adjudicacion` con la
     primera lectura igual a la línea original y el veredicto igual a la clase y el subtipo de la línea. Si falla, no se abre nada.
  2. Apertura de la tabla de códigos (archivo cerrado, sha256 igual al sello), con la hora de apertura declarada.
  3. Criterio sellado (c0/criterio_c0.md), en la peor de las dos corridas de cada brazo: C1 ≥ 113 de 137 supuestos con Condicion
     con su relación; C2 ≥ 41 de las 46 omisiones normativas extraídas con tramo verificado. Haiku como referencia (T4: 43; 0).
  4. Al lado, la cifra complementaria (texto propio / heredado), declarada posterior al resultado: no entra al criterio.
  5. M3 y M4 descriptivos (c1/salida) y costo real (presupuesto.json, resúmenes de C1).
  PYTHONDONTWRITEBYTECODE=1 <venv>/bin/python -B data/experiment/comp_e1/c3/cifras_c3.py --primera … --adjudicada … \
      --sha-primera f00a8b15… --codigos DIR --c1-salida DIR --presupuesto … --salida DIR
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "c2"))
import comun_c2 as C  # noqa: E402

UMBRAL_C1 = 113   # de 137 supuestos
UMBRAL_C2 = 41    # de 46 omisiones normativas
N_M1 = 137
N_M2 = 46
HAIKU_T4 = {"m1_condicion_con_relacion": 43, "m2_extraidas_tramo_verificado": 0}   # criterio sellado; recomputado abajo desde T4
BRAZOS = {"S": ("S1", "S2"), "O": ("O1", "O2")}


def ahora() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def wilson_inferior(k: int, n: int, z: float = 1.959964) -> float:
    if n == 0:
        return 0.0
    p = k / n
    den = 1 + z * z / n
    centro = p + z * z / (2 * n)
    radio = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (centro - radio) / den


# ------------------------------------------------------------------------------------------------ 1. control previo
def control_previo(p_primera: Path, p_adj: Path, sha_primera: str) -> dict:
    s1 = sha(p_primera)
    assert s1 == sha_primera, f"la primera lectura no tiene el sha esperado: {s1} ≠ {sha_primera}"
    A = [x for x in p_primera.read_text(encoding="utf-8").split("\n") if x]
    B = [x for x in p_adj.read_text(encoding="utf-8").split("\n") if x]
    assert len(A) == len(B) == 804, f"líneas: primera {len(A)}, adjudicada {len(B)} (esperadas 804)"
    distintas = [i for i in range(len(A)) if A[i] != B[i]]
    con_adj = [i for i in range(len(B)) if "adjudicacion" in json.loads(B[i])]
    assert distintas == con_adj, f"líneas distintas {distintas} ≠ líneas con adjudicación {con_adj}"
    detalle = []
    for i in distintas:
        a = json.loads(A[i]); b = json.loads(B[i]); adj = b["adjudicacion"]
        bb = {k: v for k, v in b.items() if k != "adjudicacion"}
        cambiados = sorted(k for k in set(a) | set(bb) if a.get(k) != bb.get(k))
        assert set(cambiados) <= {"clase", "subtipo", "categoria"}, f"línea {i + 1}: cambió algo más que la clase/subtipo: {cambiados}"
        pl, ver = adj["primera_lectura"], adj["veredicto_autora"]
        assert pl["clase"] == a["clase"], f"línea {i + 1}: la primera lectura registrada no es la original"
        if a["medida"] == "M1":
            assert (pl.get("subtipo") or "") == (a.get("subtipo") or ""), f"línea {i + 1}: subtipo de la primera lectura ≠ original"
            assert ver["clase"] == b["clase"] and (ver.get("subtipo_o_categoria") or "") == (b.get("subtipo") or ""), f"línea {i + 1}: veredicto ≠ línea"
        else:
            assert ver["clase"] == b["clase"], f"línea {i + 1}: veredicto ≠ línea"
            if b["clase"] == "omision_otra_vez":
                assert b.get("categoria"), f"línea {i + 1}: omision_otra_vez sin categoría"
        detalle.append({"linea": i + 1, "n_adjudicacion": adj["n"], "chunk_id": a["chunk_id"], "codigo": a["codigo"], "medida": a["medida"],
                        "campos_cambiados": cambiados, "primera": {"clase": a["clase"], "subtipo": a.get("subtipo")},
                        "veredicto": {"clase": b["clase"], "subtipo": b.get("subtipo"), "categoria": b.get("categoria")},
                        "ratifica_la_primera": not cambiados})
    ns = sorted(d["n_adjudicacion"] for d in detalle)
    assert ns == list(range(1, len(ns) + 1)), f"números de adjudicación no consecutivos: {ns}"
    return {"sha256_primera": s1, "sha256_adjudicada": sha(p_adj), "lineas": len(A), "lineas_adjudicadas": len(distintas),
            "lineas_iguales_byte_a_byte": len(A) - len(distintas), "cambian_contra_la_primera": sum(not d["ratifica_la_primera"] for d in detalle),
            "ratifican_la_primera": sum(d["ratifica_la_primera"] for d in detalle), "detalle": detalle, "resultado": "OK"}


# ------------------------------------------------------------------------------------------------ 2. apertura
def abrir_tabla(d: Path) -> tuple[dict, dict]:
    cerrado = d / "codigos_c2_cerrado.json"
    sello = json.loads((d / "sello_codigos_c2.json").read_text(encoding="utf-8"))
    s = sha(cerrado)
    assert s == sello["sha256_archivo_cerrado"], "el archivo cerrado no coincide con su sello"
    mapa = json.loads(cerrado.read_text(encoding="utf-8"))["codigo_a_etiqueta"]
    hora = ahora()
    return mapa, {"hora_apertura_utc": hora, "archivo": cerrado.name, "sha256": s, "sello": sello, "codigo_a_etiqueta": mapa,
                  "etiqueta_a_codigo": {v: k for k, v in mapa.items()}}


# ------------------------------------------------------------------------------------------------ 3. cifras
def cargar(p: Path) -> list[dict]:
    return [json.loads(x) for x in p.read_text(encoding="utf-8").split("\n") if x]


def contar_m1(recs: list[dict], cod: str) -> dict:
    m1 = [r for r in recs if r["medida"] == "M1" and r["codigo"] == cod]
    cl = collections.Counter(r["clase"] for r in m1)
    sub = collections.Counter(r["subtipo"] for r in m1 if r["clase"] == "sin_relacion")
    return {"n": len(m1), "clases": {k: cl.get(k, 0) for k in C.CLASES_M1}, "subtipos_sin_relacion": {k: sub.get(k, 0) for k in C.SUBTIPOS_SR}}


def contar_m2(recs: list[dict], cod: str, oms: list[dict]) -> dict:
    info = {(o["chunk_id"], f"{o['grupo']}:{o['n']}"): o for o in oms}
    m2 = [r for r in recs if r["medida"] == "M2" and r["codigo"] == cod]

    def cuenta(sel):
        return {k: sum(r["clase"] == k for r in sel) for k in C.CLASES_M2}

    norm = [r for r in m2 if info[(r["chunk_id"], r["ficha"])]["normativo_adjudicado"]]
    nonorm = [r for r in m2 if not info[(r["chunk_id"], r["ficha"])]["normativo_adjudicado"]]
    remis = [r for r in norm if info[(r["chunk_id"], r["ficha"])]["remision_pura"]]
    propio = [r for r in norm if info[(r["chunk_id"], r["ficha"])]["en"] == "propio"]
    hered = [r for r in norm if info[(r["chunk_id"], r["ficha"])]["en"] == "heredado"]
    cats = collections.Counter(r["categoria"] for r in m2 if r["clase"] == "omision_otra_vez")
    return {"n": len(m2), "normativas": {"n": len(norm), "clases": cuenta(norm)}, "no_normativas": {"n": len(nonorm), "clases": cuenta(nonorm)},
            "remisiones_puras_dentro_de_las_normativas": {"n": len(remis), "clases": cuenta(remis)},
            "complementaria_texto_propio": {"n": len(propio), "clases": cuenta(propio)},
            "complementaria_texto_heredado": {"n": len(hered), "clases": cuenta(hered)},
            "categorias_omision_otra_vez": dict(cats)}


def referencia_haiku_t4(sup: dict, oms: list[dict]) -> dict:
    todos = [s for ss in sup.values() for s in ss]
    cl = collections.Counter(s["clase"] for s in todos)
    sub = collections.Counter(s.get("subtipo_sin_relacion") or "(sin subtipo en T4)" for s in todos if s["clase"] == "sin_relacion")
    norm = [o for o in oms if o["normativo_adjudicado"]]
    return {"fuente": "reext_t0/t4/salida/tasas_t4.json (punto 7) y fichas_punto8_omisiones.json con la adjudicación de la autora",
            "m1": {"n": len(todos), "clases": {k: cl.get(k, 0) for k in C.CLASES_M1}, "subtipos_sin_relacion": dict(sub)},
            "m2": {"normativas": {"n": len(norm), "clases": {"extraida_tramo_verificado": 0, "extraida_tramo_no_verificable": 0,
                                                             "omision_otra_vez": len(norm), "ausente": 0}},
                   "nota": "0 por definición: en el intento 0 de Haiku las 46 están registradas como omisión (criterio sellado)",
                   "en_propio": sum(o["en"] == "propio" for o in norm), "en_heredado": sum(o["en"] == "heredado" for o in norm)}}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--primera", type=Path, required=True)
    ap.add_argument("--adjudicada", type=Path, required=True)
    ap.add_argument("--sha-primera", type=str, required=True)
    ap.add_argument("--codigos", type=Path, required=True)
    ap.add_argument("--c1-salida", type=Path, required=True)
    ap.add_argument("--presupuesto", type=Path, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()
    a.salida.mkdir(parents=True, exist_ok=True)

    # 1. control previo (si falla, AssertionError antes de abrir nada)
    ctrl = control_previo(a.primera, a.adjudicada, a.sha_primera)
    (a.salida / "control_previo_c3.json").write_text(json.dumps(ctrl, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    # 2. apertura de la tabla
    mapa, apertura = abrir_tabla(a.codigos)
    (a.salida / "apertura_codigos_c3.json").write_text(json.dumps(apertura, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    inv = apertura["etiqueta_a_codigo"]
    cod_h0 = inv[C.ETIQUETA_HAIKU]

    # 3. cifras con la lectura adjudicada
    recs = cargar(a.adjudicada)
    sup = C.supuestos_t4()
    oms = C.omisiones_t4()
    haiku = referencia_haiku_t4(sup, oms)
    assert haiku["m1"]["clases"]["condicion_con_relacion"] == HAIKU_T4["m1_condicion_con_relacion"], "la referencia de Haiku en M1 no da 43"
    corridas = {}
    for et in C.ETIQUETAS:
        cod = inv[et]
        m1 = contar_m1(recs, cod)
        m2 = contar_m2(recs, cod, oms)
        assert m1["n"] == N_M1 and m2["normativas"]["n"] == N_M2 and m2["n"] == 60
        corridas[et] = {"codigo": cod, "brazo": et[0], "corrida": int(et[1]), "m1": m1, "m2": m2,
                        "c1_criterio": {"condicion_con_relacion": m1["clases"]["condicion_con_relacion"], "de": N_M1,
                                        "wilson_inferior_95": round(wilson_inferior(m1["clases"]["condicion_con_relacion"], N_M1), 4)},
                        "c2_criterio": {"extraidas_tramo_verificado": m2["normativas"]["clases"]["extraida_tramo_verificado"], "de": N_M2,
                                        "wilson_inferior_95": round(wilson_inferior(m2["normativas"]["clases"]["extraida_tramo_verificado"], N_M2), 4)}}
    quinto = {"codigo": cod_h0, "etiqueta": C.ETIQUETA_HAIKU, "nota": "intento 0 de Haiku en las 8 unidades con reintento (relecturas); descriptivo",
              "m1": contar_m1(recs, cod_h0), "m2": contar_m2(recs, cod_h0, oms)}
    brazos = {}
    for b, (e1, e2) in BRAZOS.items():
        c1 = [corridas[e1]["c1_criterio"]["condicion_con_relacion"], corridas[e2]["c1_criterio"]["condicion_con_relacion"]]
        c2 = [corridas[e1]["c2_criterio"]["extraidas_tramo_verificado"], corridas[e2]["c2_criterio"]["extraidas_tramo_verificado"]]
        peor1, peor2 = min(c1), min(c2)
        brazos[b] = {"modelo": json.load(open(a.c1_salida / f"resumen_{e1}.json", encoding="utf-8"))["modelo"], "corridas": [e1, e2],
                     "C1": {"por_corrida": c1, "peor": peor1, "umbral": UMBRAL_C1, "cumple": peor1 >= UMBRAL_C1,
                            "wilson_inferior_95_peor": round(wilson_inferior(peor1, N_M1), 4)},
                     "C2": {"por_corrida": c2, "peor": peor2, "umbral": UMBRAL_C2, "cumple": peor2 >= UMBRAL_C2,
                            "wilson_inferior_95_peor": round(wilson_inferior(peor2, N_M2), 4)}}
        brazos[b]["cumple_el_criterio"] = brazos[b]["C1"]["cumple"] or brazos[b]["C2"]["cumple"]
    ninguno = not any(v["cumple_el_criterio"] for v in brazos.values())

    # 4. M3, M4 y costo (descriptivos, de C1)
    m3 = json.load(open(a.c1_salida / "m3_c1.json", encoding="utf-8"))
    m4 = json.load(open(a.c1_salida / "m4_c1.json", encoding="utf-8"))
    pres = json.load(open(a.presupuesto, encoding="utf-8"))
    m3_res = {b: {k: m3[b][k] for k in ("modelo", "unidades_en_las_dos", "misma_clave", "iguales_byte_a_byte", "iguales_byte_a_byte_ids",
                                         "ambas_sin_error", "iguales_sobre_ambas_sin_error", "corrida_1", "corrida_2")} for b in ("S", "O")}
    m3_res["marcas_intento0_haiku"] = m3["S"]["marcas_intento0_haiku"]
    m4_res = {et: {k: m4[et][k] for k in ("modelo", "unidades", "con_error", "elementos_emitidos", "tramo_entidades", "tramo_omisiones",
                                           "fuera_del_esquema_o_del_tool_schema", "tokens", "costo_usd", "costo_usd_por_unidad",
                                           "salida_total_haiku_intento0")} for et in C.ETIQUETAS}
    resum = {et: json.load(open(a.c1_salida / f"resumen_{et}.json", encoding="utf-8")) for et in C.ETIQUETAS}
    costo = {"tope_usd": pres["tope_usd"], "gasto_usd": pres["gasto_usd"], "por_corrida": pres["por_corrida"],
             "suma_por_corrida": round(sum(pres["por_corrida"].values()), 6),
             "usage_por_corrida": {et: resum[et]["usage_total"] for et in C.ETIQUETAS},
             "por_brazo": {b: round(sum(pres["por_corrida"][e] for e in es), 6) for b, es in BRAZOS.items()},
             "segundos_por_corrida": {et: resum[et]["segundos"] for et in C.ETIQUETAS}, "fuente": "presupuesto.json y c1/salida/resumen_*.json"}
    assert abs(costo["suma_por_corrida"] - costo["gasto_usd"]) < 1e-6 and costo["gasto_usd"] <= costo["tope_usd"]

    cifras = {"unidad": "U-COMP-E1, C3", "criterio": {"fuente": "c0/criterio_c0.md (sellado en C0)", "C1": f"≥ {UMBRAL_C1} de {N_M1}", "C2": f"≥ {UMBRAL_C2} de {N_M2}",
                                                       "regla": "en la peor de las dos corridas de cada brazo; cumple al menos una",
                                                       "wilson_inferior_95_de_los_umbrales": {"113_de_137": round(wilson_inferior(UMBRAL_C1, N_M1), 4),
                                                                                              "41_de_46": round(wilson_inferior(UMBRAL_C2, N_M2), 4)}},
              "control_previo": {k: ctrl[k] for k in ctrl if k != "detalle"}, "apertura_hora_utc": apertura["hora_apertura_utc"],
              "referencia_haiku_t4": haiku, "corridas": corridas, "quinto_codigo_intento0": quinto, "brazos": brazos,
              "ningun_brazo_cumple": ninguno, "m3": m3_res, "m4": m4_res, "costo": costo}
    (a.salida / "cifras_c3.json").write_text(json.dumps(cifras, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    # 5. tablas
    K2 = list(C.CLASES_M2)
    md = ["# Cifras finales de U-COMP-E1 (C3) — criterio sellado aplicado con la lectura adjudicada", "",
          f"Control previo: {ctrl['lineas']} líneas, {ctrl['lineas_adjudicadas']} adjudicadas ({ctrl['cambian_contra_la_primera']} cambian, "
          f"{ctrl['ratifican_la_primera']} ratifican), {ctrl['lineas_iguales_byte_a_byte']} iguales byte a byte. Tabla de códigos abierta a las "
          f"{apertura['hora_apertura_utc']}: " + ", ".join(f"{c} = {e}" for c, e in sorted(mapa.items())) + ".", "",
          "## Criterio (peor de las dos corridas de cada brazo)", "",
          "| brazo | modelo | C1: Condicion con relación (corrida 1, corrida 2) | peor | ≥ 113 | Wilson inf. 95 % (peor) | C2: omisiones normativas extraídas con tramo verificado (c1, c2) | peor | ≥ 41 | Wilson inf. 95 % (peor) | cumple |",
          "|---|---|---|---|---|---|---|---|---|---|---|"]
    for b, v in brazos.items():
        md.append(f"| {b} | {v['modelo']} | {v['C1']['por_corrida'][0]}, {v['C1']['por_corrida'][1]} de {N_M1} | {v['C1']['peor']} | {'sí' if v['C1']['cumple'] else 'no'} | "
                  f"{v['C1']['wilson_inferior_95_peor']:.4f} | {v['C2']['por_corrida'][0]}, {v['C2']['por_corrida'][1]} de {N_M2} | {v['C2']['peor']} | "
                  f"{'sí' if v['C2']['cumple'] else 'no'} | {v['C2']['wilson_inferior_95_peor']:.4f} | {'SÍ' if v['cumple_el_criterio'] else 'NO'} |")
    md += [f"| Haiku (referencia T4) | claude-haiku-4-5 | {haiku['m1']['clases']['condicion_con_relacion']} de {N_M1} | — | no | "
           f"{wilson_inferior(haiku['m1']['clases']['condicion_con_relacion'], N_M1):.4f} | 0 de {N_M2} (por definición) | — | no | 0.0000 | NO |", "",
           f"**Resultado: {'ningún brazo cumple el criterio' if ninguno else 'al menos un brazo cumple el criterio'}.**", "",
           "## M1 por corrida (137 supuestos del grupo c, lectura adjudicada)", "",
           "| corrida (código) | modelo | con relación | dentro de norma | fusionado | omitido | sin relación | subtipos (presente / heredado / no emitida) |",
           "|---|---|---|---|---|---|---|---|",
           f"| Haiku, T4 | claude-haiku-4-5 | " + " | ".join(str(haiku['m1']['clases'][k]) for k in C.CLASES_M1) + f" | {haiku['m1']['subtipos_sin_relacion']} |"]
    for et, v in corridas.items():
        c = v["m1"]["clases"]; s = v["m1"]["subtipos_sin_relacion"]
        md.append(f"| {et} ({v['codigo']}) | {m4[et]['modelo']} | " + " | ".join(str(c[k]) for k in C.CLASES_M1) +
                  f" | {s['norma_presente']} / {s['norma_en_heredado']} / {s['norma_no_emitida']} |")
    md += ["", "## M2 por corrida (las 46 omisiones normativas de T4; las 14 no normativas aparte)", "",
           "| corrida (código) | normativas: verificado / no verificable / omisión otra vez / ausente | no normativas (14) | remisiones puras (5, dentro de las 46) | categorías de «omisión otra vez» |",
           "|---|---|---|---|---|",
           f"| Haiku, T4 | 0 / 0 / 46 / 0 (por definición) | — | — | meta_normativo 46 |"]
    for et, v in corridas.items():
        n, nn, rm = v["m2"]["normativas"]["clases"], v["m2"]["no_normativas"]["clases"], v["m2"]["remisiones_puras_dentro_de_las_normativas"]["clases"]
        md.append(f"| {et} ({v['codigo']}) | " + " / ".join(str(n[k]) for k in K2) + " | " + " / ".join(str(nn[k]) for k in K2) + " | " +
                  " / ".join(str(rm[k]) for k in K2) + f" | {v['m2']['categorias_omision_otra_vez']} |")
    md += ["", "## Cifra complementaria del texto propio (declarada posterior al resultado; NO entra al criterio)", "",
           f"De las 46 omisiones normativas, {haiku['m2']['en_propio']} tienen su oración en el texto propio y {haiku['m2']['en_heredado']} en el heredado (campo `en` de T4).", "",
           "| corrida (código) | texto propio (26): verificado / no verificable / omisión otra vez / ausente | texto heredado (20): verificado / no verificable / omisión otra vez / ausente |",
           "|---|---|---|"]
    for et, v in corridas.items():
        p, h = v["m2"]["complementaria_texto_propio"]["clases"], v["m2"]["complementaria_texto_heredado"]["clases"]
        md.append(f"| {et} ({v['codigo']}) | " + " / ".join(str(p[k]) for k in K2) + " | " + " / ".join(str(h[k]) for k in K2) + " |")
    q1, q2 = quinto["m1"], quinto["m2"]
    md += ["", f"## Quinto código ({cod_h0} = intento 0 de Haiku en las 8 unidades con reintento; descriptivo)", "",
           f"M1 ({q1['n']} supuestos): " + ", ".join(f"{k} {v}" for k, v in q1["clases"].items()) + f"; subtipos {q1['subtipos_sin_relacion']}.",
           f"M2 ({q2['n']} omisiones; {q2['normativas']['n']} normativas): normativas " + " / ".join(str(q2["normativas"]["clases"][k]) for k in K2) +
           "; no normativas " + " / ".join(str(q2["no_normativas"]["clases"][k]) for k in K2) + ".", "",
           "## M3 — variación entre corridas (descriptivo, c1/salida/m3_c1.json)", "",
           "| brazo | modelo | en las dos | misma clave | iguales byte a byte | ambas sin error | cortes c1/c2 | sin herramienta c1/c2 | mal formadas c1/c2 | refusals c1/c2 |",
           "|---|---|---|---|---|---|---|---|---|---|"]
    for b in ("S", "O"):
        v = m3_res[b]; c1, c2 = v["corrida_1"], v["corrida_2"]
        md.append(f"| {b} | {v['modelo']} | {v['unidades_en_las_dos']} | {v['misma_clave']} | {v['iguales_byte_a_byte']} ({', '.join(v['iguales_byte_a_byte_ids'])}) | "
                  f"{v['ambas_sin_error']} | {c1['cortes']}/{c2['cortes']} | {c1['sin_herramienta']}/{c2['sin_herramienta']} | {c1['mal_formadas']}/{c2['mal_formadas']} | {c1['refusals']}/{c2['refusals']} |")
    md += ["", "## M4 y costo real (descriptivo, c1/salida/m4_c1.json, presupuesto.json)", "",
           "| corrida | modelo | entidades / relaciones / omisiones | tramo de entidad no verificable | tramo de omisión no verificable | rechazos r2 | entrada | cache read | cache write | salida | USD | USD/unidad |",
           "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for et in C.ETIQUETAS:
        v = m4_res[et]; e = v["elementos_emitidos"]; t = v["tokens"]
        rech = sum(v["fuera_del_esquema_o_del_tool_schema"]["rechazos_validador_r2_por_motivo"].values())
        md.append(f"| {et} | {v['modelo']} | {e['entidades']} / {e['relaciones']} / {e['omisiones']} | {v['tramo_entidades']['no_verificable']} | "
                  f"{v['tramo_omisiones']['no_verificable']} | {rech} | {t['input_tokens']} | {t['cache_read_tokens']} | {t['cache_write_tokens']} | "
                  f"{t['output_tokens']} | {pres['por_corrida'][et]:.6f} | {v['costo_usd_por_unidad']} |")
    md += ["", f"**Gasto real: USD {costo['gasto_usd']:.6f} de {costo['tope_usd']:.0f}** (S {costo['por_brazo']['S']:.6f}, O {costo['por_brazo']['O']:.6f}); "
           f"salida del intento 0 de Haiku sobre las mismas 87 unidades: {m4_res['S1']['salida_total_haiku_intento0']} tokens. C2 y C3 sin API.", ""]
    (a.salida / "tabla_c3.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    sellos = {"unidad": "U-COMP-E1, C3", "hora_sello_utc": ahora(),
              "lectura_c2.jsonl": ctrl["sha256_primera"], "lectura_c2_adjudicada.jsonl": ctrl["sha256_adjudicada"],
              "codigos_c2_cerrado.json": apertura["sha256"], "hora_apertura_utc": apertura["hora_apertura_utc"],
              "cifras_c3.json": sha(a.salida / "cifras_c3.json"), "tabla_c3.md": sha(a.salida / "tabla_c3.md"),
              "control_previo_c3.json": sha(a.salida / "control_previo_c3.json")}
    (a.salida / "sellos_c3.json").write_text(json.dumps(sellos, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"control_previo": cifras["control_previo"], "apertura": apertura["hora_apertura_utc"], "codigos": mapa,
                      "brazos": {b: {"C1_peor": v["C1"]["peor"], "C2_peor": v["C2"]["peor"], "cumple": v["cumple_el_criterio"]} for b, v in brazos.items()},
                      "ningun_brazo_cumple": ninguno, "gasto_usd": costo["gasto_usd"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
