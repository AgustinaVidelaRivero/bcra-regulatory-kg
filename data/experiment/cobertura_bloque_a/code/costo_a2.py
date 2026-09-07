"""Proyeccion de costo de la extraccion del bloque A, con el tamano MEDIDO.

La adenda 2 §2 proyecto USD 1,10 por densidad supuesta (41 pag × 1,38
unidades/pagina = 57 unidades × 0,019437 USD/unidad). Esta fase reemplaza la
densidad supuesta por el conteo real y agrega la via por caracter, que es la
pertinente porque los bloques del bloque A son mucho mas cortos que las
unidades sobre las que se calibro la tarifa por unidad.

Tarifas ancladas en `escalado_prep/proyeccion_costo.json` (bloque `tarifas`),
derivadas del gasto real de la corrida corpus_v2 sobre 4 de los 5 TOs de
desarrollo (`pro` excluido por ser el TO de calibracion, gasto 0).

Uso:  python3 costo_a2.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import comun_coba as C  # noqa: E402
import censo_forma as CF  # noqa: E402
from e0_lib import separar_encabezado_pie  # noqa: E402

TARIFAS = C.EXPERIMENT / "escalado_prep/proyeccion_costo.json"


def main() -> int:
    t = json.loads(TARIFAS.read_text(encoding="utf-8"))["tarifas"]
    usd_unidad = t["e1"]["usd_por_unidad_agregado"] + t["e3"]["usd_por_unidad_agregado"]
    usd_char = t["e1"]["usd_por_char_agregado"] + t["e3"]["usd_por_char_agregado"]

    filas, agg = {}, {}
    for to in C.DIEZ:
        paginas, roles, modal, bloques, _d = C.leer_documento(to)
        por_clase = {"prosa": [0, 0], "mixta": [0, 0], "planilla_ficha": [0, 0]}
        for i, (lineas, rol) in enumerate(zip(paginas, roles), start=1):
            if rol != C.E0.ROL_CUERPO:
                continue
            cont, _x, _y = separar_encabezado_pie(lineas)
            cl = CF.clase_forma(CF.densidad_prosa(cont))
            por_clase[cl][0] += len(bloques[i])
            por_clase[cl][1] += sum(b.n_chars for b in bloques[i])
        filas[to] = {k: {"unidades": v[0], "chars": v[1]}
                     for k, v in por_clase.items()}
        for k, v in por_clase.items():
            a = agg.setdefault(k, {"unidades": 0, "chars": 0})
            a["unidades"] += v[0]
            a["chars"] += v[1]

    escenarios = {
        "solo_prosa": ["prosa"],
        "prosa_y_mixta": ["prosa", "mixta"],
        "todos_los_bloques": ["prosa", "mixta", "planilla_ficha"],
    }
    out = {
        "_meta": {
            "fuente_tarifas": "data/experiment/escalado_prep/proyeccion_costo.json"
                              " (bloque `tarifas`; gasto real de corpus_v2, "
                              "`pro` excluido por ser TO de calibracion)",
            "usd_por_unidad_e1_mas_e3": round(usd_unidad, 6),
            "usd_por_char_e1_mas_e3": usd_char,
            "nota": "la via POR CARACTER es la pertinente: los bloques del "
                    "bloque A tienen mediana 93,5 caracteres contra 321 de las "
                    "unidades sobre las que se calibro la tarifa por unidad. "
                    "La via por unidad queda como COTA SUPERIOR.",
            "proyeccion_previa_de_la_adenda": {
                "unidades_supuestas": 57, "usd": 1.10,
                "metodo": "densidad 1,38 unidades/pagina (supuesta, no medida)"},
        },
        "medido_por_clase_de_forma": agg,
        "escenarios": {},
        "por_to": filas,
    }
    for nombre, clases in escenarios.items():
        u = sum(agg[c]["unidades"] for c in clases)
        ch = sum(agg[c]["chars"] for c in clases)
        out["escenarios"][nombre] = {
            "unidades": u, "chars": ch,
            "usd_via_unidad_COTA_SUPERIOR": round(u * usd_unidad, 4),
            "usd_via_caracter": round(ch * usd_char, 4),
        }

    salida = C.UNIDAD / "costo_a2.json"
    salida.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n",
                      encoding="utf-8")
    print(f"escrito: {salida.relative_to(C.REPO)}\n")
    print(json.dumps(out["escenarios"], ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
