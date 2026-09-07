"""Recomputo del alcance del bloque A tras el laudo 2 (07/09): `ri_spi` SALE.

Alcance final: NUEVE documentos. Recomputa paginas, bloques por clase de
forma, senales por brazo, la composicion del piloto A.2 y la fila del conteo
exigido — todo contra los artefactos, con la cuenta mostrada (regla i).

Uso:  python3 recomputo_nueve.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import comun_coba as C  # noqa: E402
import censo_forma as CF  # noqa: E402
import senal_sujeto as SS  # noqa: E402
from e0_lib import separar_encabezado_pie  # noqa: E402

NUEVE = tuple(t for t in C.DIEZ if t != "ri_spi")
FUERA = "ri_spi"

# Composicion v1 del brazo planilla (MUESTRA de 4 paginas). Se conserva SOLO
# para documentar el sesgo de composicion que motivo el re-sello: el laudo del
# 07/09 ordeno los dos brazos COMPLETOS, de modo que ya no es la composicion
# de A.2.
MUESTRA_V1_PLANILLA = (("ri_tii", 3), ("ri_tii", 4), ("ri_rem", 2), ("ri_con", 13))

RE_PARTIDA = re.compile(r"[a-záéíóúüñ]- [a-záéíóúüñ]")
TARIFAS = C.EXPERIMENT / "escalado_prep/proyeccion_costo.json"
TOPE_USD = 4.00   # laudo del 07/09: sube de 2,00 y los dos brazos van COMPLETOS


def medir(tos):
    """Por (to, pagina): clase de forma, bloques, caracteres y senales."""
    det = {}
    pats = SS.formas_de_superficie()
    for to in tos:
        paginas, roles, modal, bloques, _d = C.leer_documento(to)
        for i, (lineas, rol) in enumerate(zip(paginas, roles), start=1):
            if rol != C.E0.ROL_CUERPO:
                continue
            cont, _x, _y = separar_encabezado_pie(lineas)
            bs = bloques[i]
            det[(to, i)] = {
                "clase": CF.clase_forma(CF.densidad_prosa(cont)),
                "bloques": len(bs),
                "chars": sum(b.n_chars for b in bs),
                "con_sujeto": sum(1 for b in bs
                                  if any(p.search(b.texto) for p in pats.values())),
                "con_palabra_partida": sum(1 for b in bs if RE_PARTIDA.search(b.texto)),
            }
    return det


def agrega(det, filtro):
    campos = ("bloques", "chars", "con_sujeto", "con_palabra_partida")
    out = {c: 0 for c in campos}
    out["paginas"] = 0
    for k, v in det.items():
        if not filtro(k, v):
            continue
        out["paginas"] += 1
        for c in campos:
            out[c] += v[c]
    return out


def main() -> int:
    t = json.loads(TARIFAS.read_text(encoding="utf-8"))["tarifas"]
    usd_u = t["e1"]["usd_por_unidad_agregado"] + t["e3"]["usd_por_unidad_agregado"]
    usd_c = t["e1"]["usd_por_char_agregado"] + t["e3"]["usd_por_char_agregado"]

    det = medir(NUEVE)
    det_spi = medir((FUERA,))
    part = json.loads(C.PARTICION.read_text(encoding="utf-8"))
    ns = {k: v for k, v in part["por_to"].items()
          if v["clase"] == "no_segmentable_declarado"}
    recurso_hoy = sum(v["unidades"] for v in part["agregados"].values())
    degen_nueve = sum(v["unidades"] for k, v in ns.items() if k in NUEVE)

    brazos = {
        "prosa": agrega(det, lambda k, v: v["clase"] == "prosa"),
        "planilla_ficha": agrega(det, lambda k, v: v["clase"] == "planilla_ficha"),
        "mixta": agrega(det, lambda k, v: v["clase"] == "mixta"),
    }
    piloto = {
        "prosa": agrega(det, lambda k, v: v["clase"] == "prosa"),
        "planilla_ficha": agrega(det, lambda k, v: v["clase"] == "planilla_ficha"),
    }
    for d in (brazos, piloto):
        for b in d.values():
            b["usd_via_caracter"] = round(b["chars"] * usd_c, 4)
            b["usd_via_unidad_COTA_SUPERIOR"] = round(b["bloques"] * usd_u, 4)

    pil_u = sum(b["bloques"] for b in piloto.values())
    pil_c = sum(b["chars"] for b in piloto.values())

    # sesgo de composicion de la muestra v1 — registro del motivo del re-sello
    pobl = {to: sum(v["bloques"] for k, v in det.items()
                    if k[0] == to and v["clase"] == "planilla_ficha")
            for to in ("ri_con", "ri_tii", "ri_rem")}
    mues = {to: sum(det[k]["bloques"] for k in MUESTRA_V1_PLANILLA if k[0] == to)
            for to in pobl}
    tp, tm = sum(pobl.values()), sum(mues.values())
    sesgo_v1 = {to: {"poblacion": pobl[to], "frac_poblacion": round(pobl[to] / tp, 3),
                     "muestra_v1": mues[to], "frac_muestra": round(mues[to] / tm, 3),
                     "cobertura_propia": round(mues[to] / pobl[to], 3),
                     "sobrerrepresentacion": round((mues[to] / tm) / (pobl[to] / tp), 2)}
                for to in pobl}
    pags_con = [v["bloques"] for k, v in det.items()
                if k[0] == "ri_con" and v["clase"] == "planilla_ficha"]

    out = {
        "_meta": {
            "laudo": "laudo 2 (07/09): ri_spi SALE del bloque A, declarado caso "
                     "propio (tiene espina; el parser vigente no la reconoce)",
            "alcance_final": {"documentos": len(NUEVE), "lista": list(NUEVE)},
            "tarifas": {"usd_por_unidad": round(usd_u, 6), "usd_por_char": usd_c,
                        "fuente": "escalado_prep/proyeccion_costo.json §tarifas"},
            "tope_aprobado_usd": TOPE_USD,
        },
        "cuenta_del_alcance": {
            "paginas_de_los_diez": 41,
            "paginas_de_ri_spi": ns[FUERA]["paginas"],
            "paginas_de_los_nueve": 41 - ns[FUERA]["paginas"],
            "control_particion": sum(v["paginas"] for k, v in ns.items()
                                     if k in NUEVE),
            "unidades_degeneradas_que_reemplaza": degen_nueve,
        },
        "por_to": {to: {"paginas": sum(1 for k in det if k[0] == to),
                        "bloques": sum(det[k]["bloques"] for k in det if k[0] == to),
                        "prosa": sum(det[k]["bloques"] for k in det
                                     if k[0] == to and det[k]["clase"] == "prosa"),
                        "planilla": sum(det[k]["bloques"] for k in det
                                        if k[0] == to
                                        and det[k]["clase"] == "planilla_ficha")}
                   for to in NUEVE},
        "brazos_completos": brazos,
        "A2": {
            "nota": "A.2 absorbe a A.3: las 191 unidades son TODO el material "
                    "de los nueve. No queda fase de masa pendiente.",
            "brazo_prosa": {"criterio": "COMPLETO — los 77 bloques de las 13 "
                                        "paginas de prosa de los nueve",
                            **piloto["prosa"]},
            "brazo_planilla": {"criterio": "COMPLETO (CENSO) — los 114 bloques "
                                           "de las 17 paginas de planilla de "
                                           "los nueve; PL-2 y PL-4 son tasas "
                                           "censales, no inferencia sobre muestra",
                               **piloto["planilla_ficha"]},
            "total_unidades": pil_u,
            "total_chars": pil_c,
            "usd_via_caracter": round(pil_c * usd_c, 4),
            "usd_via_unidad_COTA_SUPERIOR": round(pil_u * usd_u, 4),
            "bajo_tope": round(pil_u * usd_u, 4) < TOPE_USD,
        },
        "sesgo_composicion_muestra_v1": {
            "_nota": "por que la muestra v1 no servia para PL-2/PL-4: seleccion "
                     "propositiva de maxima informacion, correcta para las "
                     "predicciones de existencia e incorrecta para las de tasa",
            "por_to": sesgo_v1,
            "ri_con_paginas_planilla": {"n": len(pags_con),
                                        "media_bloques": round(sum(pags_con) / len(pags_con), 1),
                                        "max": max(pags_con),
                                        "pagina_elegida_v1": det[("ri_con", 13)]["bloques"]},
        },
        "senal_sujeto_brazo_prosa_por_to": {
            to: {"con_sujeto": sum(v["con_sujeto"] for k, v in det.items()
                                   if k[0] == to and v["clase"] == "prosa"),
                 "bloques": sum(v["bloques"] for k, v in det.items()
                                if k[0] == to and v["clase"] == "prosa")}
            for to in NUEVE},
        "ri_spi_fuera": {
            "paginas": ns[FUERA]["paginas"],
            "bloques": sum(v["bloques"] for v in det_spi.values()),
            "unidad_degenerada_que_conserva": ns[FUERA]["unidades"],
        },
        "fila_del_conteo_MEDICION_en_unidades": {},
    }

    for nombre, n in (("todos_los_bloques",
                       brazos["prosa"]["bloques"] + brazos["planilla_ficha"]["bloques"]),
                      ("solo_prosa", brazos["prosa"]["bloques"])):
        total = recurso_hoy - degen_nueve + n
        out["fila_del_conteo_MEDICION_en_unidades"][nombre] = {
            "unidades_con_granularidad_pagina": n,
            "unidades_totales_del_recurso": total,
            "cuenta": f"{recurso_hoy} - {degen_nueve} + {n} = {total}",
            "fraccion": round(n / total, 4),
            "frase_para_la_tesis": f"{n} unidades de {total}",
        }

    salida = C.UNIDAD / "alcance_nueve.json"
    salida.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n",
                      encoding="utf-8")
    print(f"escrito: {salida.relative_to(C.REPO)}\n")
    print("CUENTA:", json.dumps(out["cuenta_del_alcance"], ensure_ascii=False))
    print("\nBRAZOS COMPLETOS:", json.dumps(brazos, ensure_ascii=False, indent=1))
    print("\nA.2 (brazos completos):", json.dumps(
        {k: v for k, v in out["A2"].items() if not isinstance(v, dict)},
        ensure_ascii=False))
    print("\nSESGO de la muestra v1:", json.dumps(sesgo_v1, ensure_ascii=False))
    print("\nFILA DEL CONTEO:", json.dumps(
        out["fila_del_conteo_MEDICION_en_unidades"], ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
