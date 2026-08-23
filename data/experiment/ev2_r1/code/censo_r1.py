"""
censo_r1.py — Censo de las 40 anclas del gold de fidelidad de EV2 sobre
KG-Reextraído-r1 (U-B1.8, fase A, $0; pre-registro ev2_r1/preregistro_ev2_r1.md §3).

Regla de resolución: LA regla sellada del censo EV2 (`resolucion.AnclaIndex`:
match EXACTO de punto normalizado, sin descendientes, contenedores >10 anclas
excluidos — `regla_atribucion.md` §2, commit 40603a9). La regla NO se cambia.
Por ancla se agregan dos columnas INFORMATIVAS (diagnóstico de granularidad,
H24, mismo formato que `atribucion_fallas.md` §4): `crudo_incl_contenedores`
(la regla sin excluir contenedores) y `con_descendientes` (sub-puntos del
punto ancla, contenedores excluidos).

Las filas de KG-Base / KG-Refinado / KG-Reextraído se CITAN de la salida
sellada `ev2_reporte/salida/atribucion_fallas.json` (commit 85d9fdb, campos
censo_anclas_fidelidad y diagnostico_ausencias_fidelidad): no se recomputan
sobre esos grafos (sus tablas están selladas); el recómputo corre SOLO sobre r1.

Salida: censo/censo_anclas_fidelidad_r1.{json,md} + propuesta de umbral P1.
Determinismo: doble corrida interna y comparación byte-idéntica (salvo `generado`).

Uso:  .venv/bin/python -B data/experiment/ev2_r1/code/censo_r1.py
"""

from __future__ import annotations

import json
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_r1 as cr        # noqa: E402  (registra r1 al importarse)
import comun_ev2 as ce       # noqa: E402

ATRIBUCION_JSON = cr.EXP_DIR / "ev2_reporte" / "salida" / "atribucion_fallas.json"

# Referencia sellada para la propuesta de umbral P1 (atribucion_fallas.md §4,
# commit 85d9fdb): KG-Reextraído (8e2eadee) tiene 10 anclas no resueltas.
NO_RESUELTAS_V2_SELLADO = 10


def parse_ancla(s: str) -> tuple[str, str]:
    """'ext:6.11' -> ('ext', '6.11') — la misma regla de atribucion_fallas.parse_ancla."""
    to, punto = s.split(":", 1)
    return to, punto


def diagnostico(n: int, crudo: int, desc: int) -> str | None:
    """Mismas tres categorías de atribucion_fallas (§4 del reporte sellado)."""
    if n > 0:
        return None
    if crudo == 0 and desc > 0:
        return "crudo=0,desc>0 (solo sub-puntos: granularidad de ancla)"
    if crudo == 0:
        return "crudo=0,desc=0 (ausencia total)"
    return "crudo>=1 (portador es contenedor >10 anclas)"


def censar_r1() -> dict:
    aidx = cr.indice_anclas_r1()
    gold = {p["id"]: p["gold"]["ancla"] for p in ce.cargar_fidelidad()}
    if len(gold) != 40:
        raise ValueError(f"gold inesperado: {len(gold)} preguntas")
    filas = []
    for q in sorted(gold):
        for a in gold[q]:
            to, punto = parse_ancla(a)
            n = len(aidx.resolver(to, punto))
            crudo = len(aidx.resolver(to, punto, incluir_contenedores=True))
            desc = len(aidx.resolver(to, punto, incluir_descendientes=True))
            filas.append({"id_pregunta": q, "ancla": a, "n": n,
                          "crudo_incl_contenedores": crudo,
                          "con_descendientes": desc,
                          "diagnostico": diagnostico(n, crudo, desc)})
    no_res = [f for f in filas if f["n"] == 0]
    return {
        "grafo": "KG-Reextraído-r1",
        "kg_path": cr.rel_repo(cr.R1["path"]),
        "kg_sha256": cr.R1["sha256"],
        "regla": ("resolucion.AnclaIndex: match exacto de punto normalizado, sin "
                  "descendientes, contenedores >10 anclas excluidos "
                  "(regla sellada del censo EV2; columnas crudo/desc informativas, H24)"),
        "n_anclas": len(filas),
        "n_presentes": sum(1 for f in filas if f["n"] > 0),
        "n_no_resueltas": len(no_res),
        "diagnostico_no_resueltas": dict(Counter(f["diagnostico"] for f in no_res)),
        "n_contenedores_grafo": len(aidx.contenedores),
        "n_provenances_sin_parsear": len(aidx.sin_parsear),
        "anclas": filas,
    }


def filas_selladas() -> dict:
    """Cita (no recomputa) el censo sellado de los tres grafos de EV2."""
    at = json.loads(ATRIBUCION_JSON.read_text(encoding="utf-8"))
    censo, diag = at["censo_anclas_fidelidad"], at["diagnostico_ausencias_fidelidad"]
    out = {}
    for g, nombre in (("run_3", "KG-Base"), ("v3", "KG-Refinado"), ("v2", "KG-Reextraído")):
        anclas = [x for q in censo[g].values() for x in q.values()]
        out[nombre] = {
            "fuente": cr.rel_repo(ATRIBUCION_JSON) + " (sellado, commit 85d9fdb)",
            "n_anclas": len(anclas),
            "n_presentes": sum(1 for x in anclas if x["n"] > 0),
            "n_no_resueltas": diag[g]["n_anclas_no_resueltas"],
            "diagnostico_no_resueltas": diag[g]["diagnostico"],
        }
    return out


def render_md(res: dict, base: dict, propuesta: dict) -> str:
    L = ["# Censo de las 40 anclas de fidelidad de EV2 sobre KG-Reextraído-r1 (U-B1.8, fase A)",
         "",
         f"Generado {res['generado']}. Regla sellada del censo EV2 (sin cambios); "
         "columnas crudo/desc informativas (H24). Las filas de los tres grafos de "
         "EV2 se citan de la salida sellada de A0.2 (`85d9fdb`), no se recomputan.",
         "",
         f"- r1: `{res['r1']['kg_path']}`, sha256 `{res['r1']['kg_sha256']}`",
         f"- contenedores (>10 anclas) en r1: {res['r1']['n_contenedores_grafo']}; "
         f"provenances sin parsear: {res['r1']['n_provenances_sin_parsear']}",
         "", "## Tabla comparativa (40 anclas por grafo)", "",
         "| grafo | presentes | no resueltas | diagnóstico de las no resueltas |",
         "|---|---|---|---|"]
    for nombre, d in base.items():
        L.append(f"| {nombre} (sellado) | {d['n_presentes']} | {d['n_no_resueltas']} | {d['diagnostico_no_resueltas']} |")
    r = res["r1"]
    L.append(f"| **KG-Reextraído-r1** | **{r['n_presentes']}** | **{r['n_no_resueltas']}** | {r['diagnostico_no_resueltas']} |")
    L += ["", "## Anclas no resueltas en r1 (detalle)", ""]
    no_res = [f for f in r["anclas"] if f["n"] == 0]
    if no_res:
        L += ["| id_pregunta | ancla | crudo | desc | diagnóstico |", "|---|---|---|---|---|"]
        for f in no_res:
            L.append(f"| {f['id_pregunta']} | {f['ancla']} | {f['crudo_incl_contenedores']} "
                     f"| {f['con_descendientes']} | {f['diagnostico']} |")
    else:
        L.append("(ninguna)")
    L += ["", "## Cambios de estado respecto de KG-Reextraído (sellado)", ""]
    for c in res["cambios_vs_v2"]:
        L.append(f"- {c}")
    L += ["", "## Propuesta de umbral P1 (pre-registro §5; a laudo de la autora)", "",
          f"- Umbral pre-registrado: presentes(r1) ≥ 31/40 (no-resueltas ≤ 9, "
          f"estrictamente menos que las {NO_RESUELTAS_V2_SELLADO} de KG-Reextraído).",
          f"- Observado: presentes(r1) = {r['n_presentes']}/40 (no-resueltas "
          f"{r['n_no_resueltas']}).",
          f"- Lectura mecánica contra el umbral: **{propuesta['lectura']}**. "
          "El veredicto formal de P1 se asienta en la tabla P1–P5 del cierre.",
          ""]
    return "\n".join(L)


def cambios_vs_v2(res_r1: dict) -> list[str]:
    """Por ancla no resuelta en el censo SELLADO de KG-Reextraído: su estado en
    r1 (cita del detalle sellado + recómputo r1). Y viceversa: nuevas no
    resueltas de r1 que estaban presentes en KG-Reextraído."""
    at = json.loads(ATRIBUCION_JSON.read_text(encoding="utf-8"))
    det_v2 = {x["ancla"]: x for x in at["diagnostico_ausencias_fidelidad"]["v2"]["detalle"]}
    por_ancla_r1 = {f["ancla"]: f for f in res_r1["anclas"]}
    lineas = []
    for a, x in sorted(det_v2.items()):
        f = por_ancla_r1[a]
        estado = (f"RESUELTA en r1 (n={f['n']})" if f["n"] > 0
                  else f"sigue no resuelta en r1 ({f['diagnostico']})")
        lineas.append(f"`{a}` ({x['id_pregunta']}): no resuelta en KG-Reextraído "
                      f"[{x['diagnostico']}] → {estado}")
    nuevas = [f for f in res_r1["anclas"]
              if f["n"] == 0 and f["ancla"] not in det_v2]
    for f in nuevas:
        lineas.append(f"`{f['ancla']}` ({f['id_pregunta']}): presente en KG-Reextraído "
                      f"→ NO resuelta en r1 ({f['diagnostico']}) — REGRESIÓN, se reporta")
    if not nuevas:
        lineas.append("Sin regresiones: ninguna ancla presente en KG-Reextraído dejó de resolver en r1.")
    return lineas


def main() -> int:
    print("== Censo de anclas de fidelidad sobre r1 (fase A, $0) ==")
    cr.verificar_sellos(verbose=True)
    r1a = censar_r1()
    r1b = censar_r1()   # determinismo: doble corrida interna
    if r1a != r1b:
        raise RuntimeError("censo no determinístico entre dos corridas")
    base = filas_selladas()
    res = {"generado": datetime.now().isoformat(timespec="seconds"),
           "unidad": "U-B1.8 fase A", "r1": r1a,
           "filas_selladas_ev2": base}
    res["cambios_vs_v2"] = cambios_vs_v2(r1a)
    cumple = r1a["n_presentes"] >= 31
    propuesta = {"umbral": "presentes(r1) >= 31/40 (no-resueltas <= 9)",
                 "observado": f"{r1a['n_presentes']}/40",
                 "lectura": "dentro del umbral" if cumple else "FUERA del umbral"}
    res["propuesta_umbral_p1"] = propuesta

    cr.CENSO_DIR.mkdir(parents=True, exist_ok=True)
    (cr.CENSO_DIR / "censo_anclas_fidelidad_r1.json").write_text(
        json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
    (cr.CENSO_DIR / "censo_anclas_fidelidad_r1.md").write_text(
        render_md(res, base, propuesta), encoding="utf-8")
    print(f"  r1: presentes {r1a['n_presentes']}/40, no resueltas {r1a['n_no_resueltas']} "
          f"{r1a['diagnostico_no_resueltas']}")
    for nombre, d in base.items():
        print(f"  {nombre} (sellado): presentes {d['n_presentes']}/40, "
              f"no resueltas {d['n_no_resueltas']}")
    print(f"  P1: {propuesta['lectura']} ({propuesta['observado']} vs {propuesta['umbral']})")
    print(f"  -> {cr.CENSO_DIR / 'censo_anclas_fidelidad_r1.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
