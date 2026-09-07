"""Censo de forma de los DIEZ del bloque A + censo de los DOS de referencia.

Fase A.1 de U-COB-A. Sin API, sin escrituras fuera de la unidad.
Uso:  python3 censo_forma.py        (desde cualquier cwd)

Produce, en el directorio de la unidad:
  censo_forma.json        — la medición completa, por documento y por página
  muestras/<to>.txt       — muestra citada por documento (para el reporte)

MODELO DE UNIDAD (decisión laudada por la autora, adenda 2 §3.3): unidad =
bloque de prosa contiguo dentro de una página, delimitado mecánicamente
(línea en blanco / cambio de bloque de layout), con la página como
contenedor; procedencia = documento + página + offset. No se fabrica espina.

CLASE DE FORMA DE LA PÁGINA (criterio propio, declarado y calibrado en §2 del
reporte): densidad de prosa = fracción de líneas de contenido SIN frontera de
columna y de ≥ LARGO_PROSA caracteres. Cortes en los dos huecos medidos de la
distribución (0,16→0,25 y 0,33→0,44), validados a mano contra cuatro páginas
frontera. El criterio es propio porque el instrumento sellado de B5.8.3
(e0_tablas) NO ve este material: las planillas del bloque A no tienen bordes
dibujados y sus grillas se descartan por `min_filas` — hallazgo del censo.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import comun_coba as C  # noqa: E402
from e0_lib import separar_encabezado_pie  # noqa: E402
import e0_tablas as T  # noqa: E402

LARGO_PROSA = 60          # caracteres mínimos de una línea de prosa llena
CORTE_PLANILLA = 0.20     # densidad de prosa por debajo → planilla/ficha
CORTE_PROSA = 0.45        # densidad de prosa por encima → prosa
FACTORES_SENSIBILIDAD = (1.3, 1.4, 1.5, 1.6, 1.8, 2.0)


def densidad_prosa(contenido) -> float:
    if not contenido:
        return 0.0
    n = sum(1 for l in contenido
            if l.ngaps == 0 and len(l.texto) >= LARGO_PROSA)
    return n / len(contenido)


def clase_forma(dens: float) -> str:
    if dens < CORTE_PLANILLA:
        return "planilla_ficha"
    if dens < CORTE_PROSA:
        return "mixta"
    return "prosa"


def censar(to: str) -> dict:
    paginas, roles, modal, bloques, descartadas = C.leer_documento(to)
    tablas = T.parsear_to(C.PDFS / f"{to}.pdf", to)

    pag_out, totales = [], {"prosa": 0, "mixta": 0, "planilla_ficha": 0}
    n_bloques = {"prosa": 0, "mixta": 0, "planilla_ficha": 0}
    chapeau = viñeta = solo_may = 0
    paginas_con_tabla = sorted({s["pagina"]
                                for t in tablas["tablas_logicas"]
                                for s in t.get("segmentos", [])})

    for i, (lineas, rol) in enumerate(zip(paginas, roles), start=1):
        if rol != C.E0.ROL_CUERPO:
            pag_out.append({"pagina": i, "rol": rol, "n_lineas_contenido": 0,
                            "densidad_prosa": None, "clase_forma": None,
                            "n_bloques": 0, "tabla_b583": i in paginas_con_tabla})
            continue
        contenido, _desc, _sec = separar_encabezado_pie(lineas)
        d = densidad_prosa(contenido)
        cl = clase_forma(d)
        bs = bloques[i]
        totales[cl] += 1
        n_bloques[cl] += len(bs)
        chapeau += sum(1 for b in bs if b.termina_en_dos_puntos)
        viñeta += sum(1 for b in bs if b.viñeta_inicial)
        solo_may += sum(1 for b in bs if b.solo_mayusculas)
        pag_out.append({
            "pagina": i, "rol": rol,
            "n_lineas_contenido": len(contenido),
            "densidad_prosa": round(d, 3),
            "clase_forma": cl,
            "n_bloques": len(bs),
            "n_bloques_1_linea": sum(1 for b in bs if b.n_lineas == 1),
            "n_bloques_con_linea_tabular": sum(1 for b in bs
                                               if b.n_lineas_tabulares > 0),
            "tabla_b583": i in paginas_con_tabla,
        })

    # sensibilidad del conteo al umbral de corte de bloque
    sens = {}
    for f in FACTORES_SENSIBILIDAD:
        _p, _r, _m, bl_f, _d = C.leer_documento(to, factor=f)
        sens[f"{f:.1f}"] = sum(len(v) for v in bl_f.values())

    total = sum(n_bloques.values())
    return {
        "to": to,
        "paginas": len(paginas),
        "interlineado_modal_pt": modal,
        "roles": {r: roles.count(r) for r in sorted(set(roles))},
        "paginas_por_clase_forma": totales,
        "bloques_por_clase_forma": n_bloques,
        "bloques_total": total,
        "bloques_utiles_prosa_y_mixta": n_bloques["prosa"] + n_bloques["mixta"],
        "senales": {
            "bloques_terminados_en_dos_puntos": chapeau,
            "bloques_con_viñeta_inicial": viñeta,
            "bloques_solo_mayusculas": solo_may,
        },
        "b583_tablas_logicas": len(tablas["tablas_logicas"]),
        "b583_paginas_con_tabla": paginas_con_tabla,
        "b583_descartes": tablas["descartadas_por_regla"]["conteos"],
        "sensibilidad_factor_blanco": sens,
        "paginas_detalle": pag_out,
    }


def muestra(to: str, max_bloques: int = 6) -> str:
    """Muestra citada: los primeros bloques de la primera página de cada
    clase de forma presente en el documento. Criterio fijo, no a elección."""
    paginas, roles, modal, bloques, _d = C.leer_documento(to)
    vistas, out = set(), [f"# muestra citada — {to}\n"]
    for i, (lineas, rol) in enumerate(zip(paginas, roles), start=1):
        if rol != C.E0.ROL_CUERPO:
            continue
        contenido, _x, _y = separar_encabezado_pie(lineas)
        cl = clase_forma(densidad_prosa(contenido))
        if cl in vistas:
            continue
        vistas.add(cl)
        out.append(f"\n## {to} p.{i} — clase_forma={cl} "
                   f"(densidad_prosa={densidad_prosa(contenido):.3f}, "
                   f"{len(bloques[i])} bloques)\n")
        for b in bloques[i][:max_bloques]:
            out.append(f"[p.{b.pagina} off.{b.offset} · {b.n_lineas} líneas · "
                       f"{b.n_chars} car.] {b.texto}\n")
    return "".join(out)


def main() -> int:
    (C.UNIDAD / "muestras").mkdir(exist_ok=True)
    censo = {"_meta": {
        "unidad": "U-COB-A fase A.1",
        "modelo_unidad": "bloque de prosa contiguo en una página; corte = salto "
                         "vertical > FACTOR_BLANCO x interlineado modal del documento",
        "factor_blanco": C.FACTOR_BLANCO,
        "largo_prosa": LARGO_PROSA,
        "cortes_clase_forma": {"planilla_ficha": f"<{CORTE_PLANILLA}",
                               "mixta": f"[{CORTE_PLANILLA},{CORTE_PROSA})",
                               "prosa": f">={CORTE_PROSA}"},
        "camino_lectura": "e0_lib.clasificar_paginas(marcadores_b582=True) -> "
                          "roles_para_modo_sin_raiz -> separar_encabezado_pie "
                          "(el mismo que corrio B5.8.4 sobre estos documentos)",
        "esquema_congelado_sha": "e69feaaa04779bd6347cc9e3974d2c1749519f1230e70a0459e66f46517cd720",
    }, "bloque_a_extraccion": {}, "bloque_a_referencia": {}}

    for to in C.DIEZ:
        censo["bloque_a_extraccion"][to] = censar(to)
        (C.UNIDAD / "muestras" / f"{to}.txt").write_text(muestra(to), encoding="utf-8")
    for to in C.REFERENCIA:
        censo["bloque_a_referencia"][to] = censar(to)
        (C.UNIDAD / "muestras" / f"{to}.txt").write_text(muestra(to), encoding="utf-8")

    d = censo["bloque_a_extraccion"]
    censo["agregados_diez"] = {
        "documentos": len(d),
        "paginas": sum(v["paginas"] for v in d.values()),
        "paginas_por_clase_forma": {
            k: sum(v["paginas_por_clase_forma"][k] for v in d.values())
            for k in ("prosa", "mixta", "planilla_ficha")},
        "bloques_por_clase_forma": {
            k: sum(v["bloques_por_clase_forma"][k] for v in d.values())
            for k in ("prosa", "mixta", "planilla_ficha")},
        "bloques_total": sum(v["bloques_total"] for v in d.values()),
        "bloques_utiles_prosa_y_mixta":
            sum(v["bloques_utiles_prosa_y_mixta"] for v in d.values()),
        "b583_tablas_logicas": sum(v["b583_tablas_logicas"] for v in d.values()),
    }
    r = censo["bloque_a_referencia"]
    censo["agregados_referencia"] = {
        "documentos": len(r),
        "paginas": sum(v["paginas"] for v in r.values()),
        "bloques_total": sum(v["bloques_total"] for v in r.values()),
    }

    salida = C.UNIDAD / "censo_forma.json"
    salida.write_text(json.dumps(censo, ensure_ascii=False, indent=1) + "\n",
                      encoding="utf-8")
    print(f"escrito: {salida.relative_to(C.REPO)}")
    print(json.dumps(censo["agregados_diez"], ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
