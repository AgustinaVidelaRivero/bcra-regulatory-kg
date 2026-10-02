"""U-R2-CODIGO, R1.a — censo de la detección de tablas de la versión e0-r2.

Lee dos salidas de E0 de la tanda 0 (la legada, sellada en
`e0_chunking/salida_tanda0/`, y una e0-r2 corrida sobre una copia) y escribe
`r1a_deteccion_tablas.json`: tablas por origen, estado, guarda de recuadro y
asignación; chunks que la versión e0-r2 marca y que la legada no marcaba;
cruce con la medición 2 de U-UMBRAL (`reports/u_umbral/u1_mediciones.json`);
detecciones de R-TC2 con su lectura; y tablas sin chunk con el rol de su
página. USD 0, sin LLM, determinístico.

Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B \\
    data/experiment/r2_codigo/r1a_deteccion_tablas.py \\
    --e0-legada data/experiment/reextraccion_v2/e0_chunking/salida_tanda0 \\
    --e0-r2 <salida e0-r2> --out <ruta del json>
"""

from __future__ import annotations

import argparse
import collections
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
U1 = REPO / "reports" / "u_umbral" / "u1_mediciones.json"

# Lectura de las detecciones de R-TC2 (criterio declarado antes de leerlas:
# verdadero positivo = la región es una tabla de contenido del articulado,
# con una fila de rótulos de columna y una fila de valores alineados a ellos;
# falso positivo = cualquier otra cosa: recuadro, banner, fórmula, prosa).
# La lectura se hizo sobre las celdas que imprime este censo.
LECTURA_RTC2 = {
    "cap::tabla2f000": "verdadero positivo: cuadro de ponderadores por calificación (2.12.2.4)",
    "cap::tabla2f001": "verdadero positivo: cuadro de ponderadores por calificación (2.12.2.5)",
    "cap::tabla2f002": "verdadero positivo: cuadro de ponderadores por calificación (2.12.2.6)",
    "cap::tabla2f003": "verdadero positivo: cuadro de ponderadores por calificación (2.12.2.8)",
    "cap::tabla2f004": "verdadero positivo: cuadro de ponderadores por calificación (2.12.3.2)",
}


def _cargar(d: Path, patron: str) -> dict[str, object]:
    return {p.stem.split("_", 1)[1]: json.loads(p.read_text(encoding="utf-8"))
            for p in sorted(d.glob(patron))}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--e0-legada", required=True)
    ap.add_argument("--e0-r2", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    leg = _cargar(Path(a.e0_legada), "chunks_*.json")
    r2 = _cargar(Path(a.e0_r2), "chunks_*.json")
    tablas = _cargar(Path(a.e0_r2), "tablas_*.json")
    version = json.loads((Path(a.e0_r2) / "version_e0.json").read_text(encoding="utf-8"))

    por_to: dict[str, dict] = {}
    nuevos: list[dict] = []
    ya_marcados_con_tabla: list[str] = []
    texto_distinto: list[str] = []
    sin_chunk: list[dict] = []
    recuadros: list[dict] = []
    rtc2: list[dict] = []
    for to in sorted(r2):
        cl = {c["id"]: c for c in leg[to]}
        conteo = collections.Counter()
        for c in r2[to]:
            v = cl[c["id"]]
            if c["texto"] != v["texto"] or c["herencia"] != v["herencia"]:
                texto_distinto.append(c["id"])
            if c["flags"].get("tablas_e0"):
                if v["flags"]["contenido_tabular"]:
                    ya_marcados_con_tabla.append(c["id"])
                else:
                    nuevos.append({"chunk": c["id"],
                                   "tablas": [t["tabla"] for t in c["flags"]["tablas_e0"]]})
        for t in tablas[to]["tablas"]:
            asignada = bool(t["chunks"])
            rec = t["recuadro_prosa"]["es_recuadro"]
            conteo[f"{t['origen']}|{t['estado']}|"
                   f"{'asignada' if asignada else 'sin_chunk'}|"
                   f"{'recuadro' if rec else 'tabla'}"] += 1
            if not asignada:
                s0 = t["segmentos"][0]
                sin_chunk.append({
                    "tabla": t["id"],
                    "paginas": [s["pagina"] for s in t["segmentos"]],
                    "roles_pagina": sorted({s["rol_pagina"] for s in t["segmentos"]}),
                    "primera_celda": (s0["filas"][0][0] or "") if s0["filas"] else ""})
            if rec:
                recuadros.append({"tabla": t["id"], "chunks": t["chunks"],
                                  "fraccion": t["recuadro_prosa"]["fraccion"]})
            if t["origen"] == "r_tc2":
                rtc2.append({"tabla": t["id"], "chunks": t["chunks"],
                             "pagina": t["segmentos"][0]["pagina"],
                             "filas": t["segmentos"][0]["filas"],
                             "lectura": LECTURA_RTC2.get(t["id"], "SIN LECTURA")})
        por_to[to] = dict(sorted(conteo.items()))

    fr = [r["fraccion"] for r in recuadros]
    no_rec = [t["recuadro_prosa"]["fraccion"] for to in tablas for t in tablas[to]["tablas"]
              if t["chunks"] and not t["recuadro_prosa"]["es_recuadro"]]

    # cruce con la medición 2 de U-UMBRAL (13 chunks no marcados por E0 con
    # tabla de e0_tablas: los 12 sin disparo del patrón + cap::1.2) y los 4
    # de ponderadores que no detecta ninguno de los dos
    m2 = json.loads(U1.read_text(encoding="utf-8"))["medicion_2"]
    doce = [c["chunk_id"] for c in m2["no_marcados_con_tabla_e0_tablas_sin_disparo"]]
    cuatro = [c["chunk_id"] for c in m2["chunks_que_disparan"] if not c["tablas_e0_tablas"]]
    marcados_nuevos = {n["chunk"] for n in nuevos}
    tabla_de_chunk: dict[str, list[dict]] = collections.defaultdict(list)
    for to in tablas:
        for t in tablas[to]["tablas"]:
            for cid in t["chunks"]:
                tabla_de_chunk[cid].append({"tabla": t["id"], "origen": t["origen"],
                                            "recuadro": t["recuadro_prosa"]["es_recuadro"],
                                            "fraccion": t["recuadro_prosa"]["fraccion"]})
    cruce = {cid: {"marcado_e0_r2": cid in marcados_nuevos, "tablas": tabla_de_chunk.get(cid, [])}
             for cid in doce + ["cap::1.2"] + cuatro}

    out = {
        "unidad": "U-R2-CODIGO",
        "etapa": "R1.a",
        "version_e0": version,
        "entradas": {"e0_legada": a.e0_legada, "e0_r2": "salida e0-r2 (fuera del repo)",
                     "u1_mediciones": str(U1.relative_to(REPO))},
        "chunks_total": sum(len(v) for v in r2.values()),
        "chunks_con_texto_o_herencia_distintos": texto_distinto,
        "tablas_por_to": por_to,
        "tablas_total": sum(sum(v.values()) for v in por_to.values()),
        "chunks_nuevos_marcados": nuevos,
        "n_chunks_nuevos_marcados": len(nuevos),
        "chunks_ya_marcados_con_tabla": ya_marcados_con_tabla,
        "recuadros": recuadros,
        "recuadros_fraccion_minima": min(fr) if fr else None,
        "tablas_asignadas_no_recuadro_fraccion_maxima": max(no_rec) if no_rec else None,
        "tablas_sin_chunk": sin_chunk,
        "rtc2": rtc2,
        "rtc2_falsos_positivos": sum(1 for r in rtc2 if not r["lectura"].startswith("verdadero")),
        "cruce_medicion_2": cruce,
        "medicion_2_doce": doce,
        "medicion_2_cuatro": cuatro,
    }
    Path(a.out).write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n",
                           encoding="utf-8")


if __name__ == "__main__":
    main()
