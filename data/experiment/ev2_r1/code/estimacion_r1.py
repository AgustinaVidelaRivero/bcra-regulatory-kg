"""
estimacion_r1.py — Estimación de costo de la fase B de U-B1.8 (fase A, $0),
calculada desde los archivos sellados de la corrida base de EV2 (ningún número
inventado; cada insumo se cita con su archivo).

Insumos:
  - costo por traza de agente en fidelidad: las 40 filas eje=="fidelidad" de
    ev2_corrida/trazas/ev2_base_v2/resumen_ev2_base_v2.json (KG-Reextraído,
    el pariente directo de r1) — y las de v3/run3 como referencia;
  - costo por llamada del juez base: ev2_fidelidad_eval/out/resumen_corrida.json;
  - costo por re-corrida §7 del agente: ev2_encadenamiento/reporte/resumen_agente.json;
  - costo por llamada del juez §7: ev2_encadenamiento/juez_out/resumen_corrida_juez.json.

Escenarios por número de parciales (el §7 es proporcional a los parciales) y
margen por tamaño de r1 (6.529 nodos / 17.772 aristas vs 6.178 / 11.415 del
sellado: outputs de ver_vecinos más grandes → tokens de entrada mayores).

Salida: estimacion/estimacion_fase_b_r1.{json,md}.

Uso:  .venv/bin/python -B data/experiment/ev2_r1/code/estimacion_r1.py
"""

from __future__ import annotations

import json
import math
import sys
from datetime import datetime
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_r1 as cr    # noqa: E402

ESCENARIOS_PARCIALES = [10, 15, 20, 23, 28]     # 23 = los de KG-Reextraído en la base
CORRECTOS_SUPUESTOS = 4                          # los de KG-Reextraído en la base
MARGENES = [1.0, 1.2]                            # tamaño de r1 vs sellado
TOPE_PROPUESTO_USD = 6.0                         # mandato U-B1.8


def insumos() -> dict:
    exp = cr.EXP_DIR
    out = {}
    res_v2 = json.loads((exp / "ev2_corrida" / "trazas" / "ev2_base_v2"
                         / "resumen_ev2_base_v2.json").read_text(encoding="utf-8"))
    fid = [c for c in res_v2["casos"] if c["eje"] == "fidelidad"]
    out["agente_fidelidad_v2"] = {
        "fuente": "ev2_corrida/trazas/ev2_base_v2/resumen_ev2_base_v2.json (casos eje=fidelidad)",
        "n_trazas": len(fid),
        "usd_total": round(sum(c["costo_usd"] for c in fid), 4),
        "usd_por_traza": round(sum(c["costo_usd"] for c in fid) / len(fid), 5),
        "usd_max_traza": round(max(c["costo_usd"] for c in fid), 5),
    }
    for lbl in ("ev2_base_v3", "ev2_base_run3"):
        res = json.loads((exp / "ev2_corrida" / "trazas" / lbl
                          / f"resumen_{lbl}.json").read_text(encoding="utf-8"))
        f2 = [c for c in res["casos"] if c["eje"] == "fidelidad"]
        out[f"agente_fidelidad_{lbl}"] = {
            "n_trazas": len(f2),
            "usd_por_traza": round(sum(c["costo_usd"] for c in f2) / len(f2), 5)}
    rj = json.loads((exp / "ev2_fidelidad_eval" / "out" / "resumen_corrida.json")
                    .read_text(encoding="utf-8"))
    out["juez_base"] = {
        "fuente": "ev2_fidelidad_eval/out/resumen_corrida.json",
        "llamadas": rj["llamadas_hechas"], "usd": rj["gasto_real"]["usd"],
        "usd_por_llamada": round(rj["gasto_real"]["usd"] / rj["llamadas_hechas"], 5)}
    ra = json.loads((exp / "ev2_encadenamiento" / "reporte" / "resumen_agente.json")
                    .read_text(encoding="utf-8"))
    filas_enc = ra["gasto_dbs"]["total"]["filas"]
    out["agente_s7"] = {
        "fuente": "ev2_encadenamiento/reporte/resumen_agente.json",
        "corridas": ra["indice"]["n_persistidas"],
        "usd": ra["gasto_dbs"]["total"]["usd"],
        "usd_por_corrida": round(ra["gasto_dbs"]["total"]["usd"]
                                 / ra["indice"]["n_persistidas"], 5),
        "filas_db": filas_enc}
    rje = json.loads((exp / "ev2_encadenamiento" / "juez_out" / "resumen_corrida_juez.json")
                     .read_text(encoding="utf-8"))
    out["juez_s7"] = {
        "fuente": "ev2_encadenamiento/juez_out/resumen_corrida_juez.json",
        "llamadas_nominales": rje["llamadas_totales"],
        "usd": rje["gasto_real"]["usd"],
        "usd_por_llamada_nominal": round(rje["gasto_real"]["usd"]
                                         / rje["llamadas_totales"], 5)}
    return out


def escenarios(ins: dict) -> list[dict]:
    xs = []
    a_fid = ins["agente_fidelidad_v2"]["usd_por_traza"]
    j_base = ins["juez_base"]["usd_por_llamada"]
    a_s7 = ins["agente_s7"]["usd_por_corrida"]
    j_s7 = ins["juez_s7"]["usd_por_llamada_nominal"]
    auditoria = max(math.ceil(0.1 * CORRECTOS_SUPUESTOS), 1)
    for m in MARGENES:
        for p in ESCENARIOS_PARCIALES:
            pares = p + auditoria
            etapas = {
                "agente_base": round(40 * a_fid * m, 3),
                "juez_base": round(120 * j_base, 3),
                "agente_s7": round(pares * 3 * a_s7 * m, 3),
                "juez_s7": round(pares * 9 * j_s7, 3),
            }
            xs.append({"parciales": p, "auditoria": auditoria, "pares_s7": pares,
                       "margen_tamano": m, "etapas": etapas,
                       "total_usd": round(sum(etapas.values()), 2),
                       "dentro_de_tope_6": sum(etapas.values()) <= TOPE_PROPUESTO_USD})
    return xs


def render_md(ins: dict, esc: list[dict]) -> str:
    L = ["# Estimación de costo — fase B de U-B1.8 (desde archivos sellados)", "",
         f"Generado {datetime.now().isoformat(timespec='seconds')}. Tope propuesto "
         f"por el mandato: **USD {TOPE_PROPUESTO_USD:.2f}**. La auditoría simétrica "
         f"se supone {CORRECTOS_SUPUESTOS} correctos → ceil(10 %) = 1 par (regla min. 1).",
         "", "## Insumos (todos citados de archivos sellados)", ""]
    a = ins["agente_fidelidad_v2"]
    L += [f"- agente por traza de fidelidad (KG-Reextraído, pariente de r1): "
          f"USD {a['usd_por_traza']} ({a['fuente']}, {a['n_trazas']} trazas, "
          f"total {a['usd_total']}); v3 {ins['agente_fidelidad_ev2_base_v3']['usd_por_traza']}, "
          f"run3 {ins['agente_fidelidad_ev2_base_run3']['usd_por_traza']}",
          f"- juez base por llamada: USD {ins['juez_base']['usd_por_llamada']} "
          f"({ins['juez_base']['fuente']}: {ins['juez_base']['usd']} / {ins['juez_base']['llamadas']})",
          f"- agente §7 por re-corrida: USD {ins['agente_s7']['usd_por_corrida']} "
          f"({ins['agente_s7']['fuente']}: {ins['agente_s7']['usd']} / {ins['agente_s7']['corridas']})",
          f"- juez §7 por llamada nominal: USD {ins['juez_s7']['usd_por_llamada_nominal']} "
          f"({ins['juez_s7']['fuente']}: {ins['juez_s7']['usd']} / {ins['juez_s7']['llamadas_nominales']})",
          "",
          "Margen de tamaño: r1 tiene 6.529 nodos / 17.772 aristas contra "
          "6.178 / 11.415 del sellado (+5,7 % nodos, +55,7 % aristas): los outputs "
          "de `ver_vecinos` crecen → escenario 1,2× sobre las etapas de agente.",
          "", "## Escenarios (el §7 es proporcional a los parciales de la corrida base de r1)", "",
          "| parciales | pares §7 | margen | agente base | juez base | agente §7 | juez §7 | TOTAL USD | ≤ tope 6 |",
          "|---|---|---|---|---|---|---|---|---|"]
    for x in esc:
        e = x["etapas"]
        L.append(f"| {x['parciales']} | {x['pares_s7']} | {x['margen_tamano']} "
                 f"| {e['agente_base']} | {e['juez_base']} | {e['agente_s7']} "
                 f"| {e['juez_s7']} | **{x['total_usd']}** | {'sí' if x['dentro_de_tope_6'] else 'NO'} |")
    # breakeven por margen: máximo de parciales cuyo total entra en el tope
    a_fid = ins["agente_fidelidad_v2"]["usd_por_traza"]
    j_base = ins["juez_base"]["usd_por_llamada"]
    a_s7 = ins["agente_s7"]["usd_por_corrida"]
    j_s7 = ins["juez_s7"]["usd_por_llamada_nominal"]
    aud = max(math.ceil(0.1 * CORRECTOS_SUPUESTOS), 1)
    brk = {}
    for m in MARGENES:
        fijo = 40 * a_fid * m + 120 * j_base + aud * (3 * a_s7 * m + 9 * j_s7)
        por_parcial = 3 * a_s7 * m + 9 * j_s7
        brk[m] = int((TOPE_PROPUESTO_USD - fijo) / por_parcial)
    base_fija = {m: round(40 * a_fid * m + 120 * j_base, 2) for m in MARGENES}
    esc23 = [x["total_usd"] for x in esc if x["parciales"] == 23]
    L += ["",
          "## Lectura para el laudo del tope (la decisión es de la autora)", "",
          f"- Con los parciales de KG-Reextraído en la base (23) el total central "
          f"es USD {min(esc23)}–{max(esc23)}: supera el tope propuesto de USD 6 "
          f"en ambos márgenes.",
          f"- El tope de USD 6 entra solo si los parciales de r1 son ≤ {brk[1.0]} "
          f"(margen 1,0) / ≤ {brk[1.2]} (margen 1,2).",
          f"- Alternativas para el laudo: mantener USD 6 (freno por proyección "
          f"activo; riesgo de detención a mitad del §7, retomable), subir el "
          f"tope, o autorizar por etapas (agente base + juez base ≈ USD "
          f"{base_fija[1.0]}–{base_fija[1.2]}; el §7 con tope propio una vez "
          f"conocidos los parciales — la opción que evita frenos a ciegas).", ""]
    return "\n".join(L)


def main() -> int:
    print("== Estimación fase B U-B1.8 (desde archivos sellados, $0) ==")
    ins = insumos()
    esc = escenarios(ins)
    cr.ESTIMACION_DIR.mkdir(parents=True, exist_ok=True)
    res = {"generado": datetime.now().isoformat(timespec="seconds"),
           "tope_propuesto_usd": TOPE_PROPUESTO_USD, "insumos": ins,
           "escenarios": esc}
    (cr.ESTIMACION_DIR / "estimacion_fase_b_r1.json").write_text(
        json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
    (cr.ESTIMACION_DIR / "estimacion_fase_b_r1.md").write_text(
        render_md(ins, esc), encoding="utf-8")
    for x in esc:
        print(f"  parciales={x['parciales']:>2} margen={x['margen_tamano']}: "
              f"USD {x['total_usd']}  ({'<= 6' if x['dentro_de_tope_6'] else '> 6'})")
    print(f"  -> {cr.ESTIMACION_DIR / 'estimacion_fase_b_r1.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
