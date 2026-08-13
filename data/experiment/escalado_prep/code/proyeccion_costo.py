"""Inventario de unidades del escalado + proyección de costo E1/E3.

Las tarifas NO se escriben a mano: se derivan del único registro de gasto
commiteado de la corrida del corpus v2,
data/experiment/reextraccion_v2/corpus_v2/salida/estado_corpus.json
(clave `fases_cerradas`, entradas '<to>:e1' / '<to>:e3', cada una con
`gasto_usd` y `resumen.n` = unidades facturadas en esa fase).

Advertencia que el script aplica solo: `pro` fue el TO de calibración de E0-E3,
así que sus dos fases entraron a la corrida del corpus con la caché ya
poblada. Se ve en el propio registro: `pro:e1` = USD 0,0 sobre 101 unidades
(caché total) y `pro:e3` = USD 0,2066 sobre 101 unidades = 0,00205 USD/unidad,
seis veces por debajo del siguiente TO más barato. Tomar esas tarifas como
representativas subestimaría el escalado, porque los TOs nuevos no tienen
caché previa. `pro` queda EXCLUIDO del cálculo de tarifas en ambas fases y se
reporta aparte con sus números.

Contraste independiente: además de USD/unidad se calcula USD/carácter propio
sobre los mismos TOs pagos, y se proyecta por las dos vías. Si las dos
proyecciones caen cerca, la tarifa por unidad no está siendo arrastrada por
una diferencia de tamaño de unidad entre el corpus v2 y el universo nuevo.

Salidas: ../proyeccion_costo.json, ../inventario_unidades.csv
"""

from __future__ import annotations

import csv
import json
import statistics
from pathlib import Path

AQUI = Path(__file__).resolve().parent
PREP = AQUI.parent
REPO = PREP.parents[2]
ESTADO = REPO / "data" / "experiment" / "reextraccion_v2" / "corpus_v2" / "salida" / "estado_corpus.json"
E0_DRY = PREP / "e0_dry"

TOS_SUBSET = ["pro", "cla", "ric", "cap", "ext"]
TO_CALIBRACION = "pro"          # entró al corpus con la caché ya poblada
E0_SELLADA = REPO / "data" / "experiment" / "reextraccion_v2" / "e0_chunking" / "salida_enm01"


def chars_subset() -> dict[str, int]:
    """Caracteres propios por TO del subset, desde los chunks sellados de E0."""
    out = {}
    for to in TOS_SUBSET:
        ch = json.loads((E0_SELLADA / f"chunks_{to}.json").read_text(encoding="utf-8"))
        out[to] = sum(c["chars_propio"] for c in ch)
    return out


def tarifas() -> dict:
    est = json.loads(ESTADO.read_text(encoding="utf-8"))["fases_cerradas"]
    chars = chars_subset()
    detalle = {}
    for to in TOS_SUBSET:
        for fase in ("e1", "e3"):
            k = f"{to}:{fase}"
            if k not in est:
                continue
            gasto = est[k]["gasto_usd"]
            n = est[k]["resumen"]["n"]
            detalle[k] = {"gasto_usd": gasto, "n": n,
                          "chars_propio_to": chars[to],
                          "usd_por_unidad": (gasto / n) if n else None,
                          "usd_por_char": gasto / chars[to],
                          "to_de_calibracion": to == TO_CALIBRACION}
    out = {"detalle_por_to_fase": detalle,
           "fuente_gasto": str(ESTADO.relative_to(REPO)),
           "fuente_chars": str(E0_SELLADA.relative_to(REPO)),
           "to_excluido_de_tarifas": TO_CALIBRACION}
    for fase in ("e1", "e3"):
        usadas = {k: v for k, v in detalle.items()
                  if k.endswith(f":{fase}") and not v["to_de_calibracion"]}
        excl = sorted(k for k in detalle
                      if k.endswith(f":{fase}") and detalle[k]["to_de_calibracion"])
        gasto = sum(v["gasto_usd"] for v in usadas.values())
        n = sum(v["n"] for v in usadas.values())
        ch = sum(v["chars_propio_to"] for v in usadas.values())
        rates = sorted(v["usd_por_unidad"] for v in usadas.values())
        out[fase] = {
            "fases_incluidas": sorted(usadas),
            "fases_excluidas": excl,
            "gasto_usd": round(gasto, 6),
            "unidades": n,
            "chars_propio": ch,
            "usd_por_unidad_agregado": gasto / n,
            "usd_por_unidad_min_to": rates[0],
            "usd_por_unidad_max_to": rates[-1],
            "usd_por_unidad_mediana_to": statistics.median(rates),
            "usd_por_char_agregado": gasto / ch,
        }
    return out


def main() -> None:
    t = tarifas()
    r_e1 = t["e1"]["usd_por_unidad_agregado"]
    r_e3 = t["e3"]["usd_por_unidad_agregado"]
    lo_e1, hi_e1 = t["e1"]["usd_por_unidad_min_to"], t["e1"]["usd_por_unidad_max_to"]
    lo_e3, hi_e3 = t["e3"]["usd_por_unidad_min_to"], t["e3"]["usd_por_unidad_max_to"]

    conteos = json.loads((E0_DRY / "conteos_e0_dry.json").read_text(encoding="utf-8"))
    inv = {f["id"]: f for f in csv.DictReader((PREP / "inventario_tos.csv").open(encoding="utf-8"))}

    filas = []
    for ident in sorted(conteos):
        c = conteos[ident]
        u = c["unidades_extraccion"]
        filas.append({
            "id": ident,
            "categoria": inv[ident]["categoria"],
            "titulo_oficial": inv[ident]["titulo_oficial"],
            "paginas": c["paginas"],
            "paginas_cuerpo": c["paginas_cuerpo"],
            "secciones": c["secciones"],
            "chunks_terminales": c["chunks_terminales"],
            "mini_chunks": c["mini_chunks"],
            "unidades_extraccion": u,
            "chars_propio_total": c["diagnostico"]["escala"]["chars_propio_total"],
            "usd_e1": round(u * r_e1, 4),
            "usd_e3": round(u * r_e3, 4),
            "usd_total": round(u * (r_e1 + r_e3), 4),
        })

    ver = json.loads((PREP / "veredictos_generalizacion.json").read_text(
        encoding="utf-8"))["por_to"]
    for f in filas:
        f["veredicto"] = ver[f["id"]]["veredicto"]
    filas.sort(key=lambda f: -f["unidades_extraccion"])
    with (PREP / "inventario_unidades.csv").open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(filas[0].keys()))
        w.writeheader()
        w.writerows(filas)

    U = sum(f["unidades_extraccion"] for f in filas)
    T = sum(f["chunks_terminales"] for f in filas)
    M = sum(f["mini_chunks"] for f in filas)
    C = sum(f["chars_propio_total"] for f in filas)
    c_e1, c_e3 = t["e1"]["usd_por_char_agregado"], t["e3"]["usd_por_char_agregado"]
    agregado = {
        "tos_procesados": len(filas),
        "chunks_terminales_total": T,
        "mini_chunks_total": M,
        "unidades_extraccion_total": U,
        "paginas_total": sum(f["paginas"] for f in filas),
        "chars_propio_total": C,
        "usd_e1_central": round(U * r_e1, 2),
        "usd_e3_central": round(U * r_e3, 2),
        "usd_total_central": round(U * (r_e1 + r_e3), 2),
        "usd_total_banda_baja": round(U * (lo_e1 + lo_e3), 2),
        "usd_total_banda_alta": round(U * (hi_e1 + hi_e3), 2),
        "contraste_por_caracter": {
            "usd_e1": round(C * c_e1, 2),
            "usd_e3": round(C * c_e3, 2),
            "usd_total": round(C * (c_e1 + c_e3), 2),
        },
        "referencia_corpus_v2": {
            "unidades_e1": t["e1"]["unidades"], "unidades_e3": t["e3"]["unidades"],
            "gasto_e1_usd": t["e1"]["gasto_usd"], "gasto_e3_usd": t["e3"]["gasto_usd"],
            "gasto_total_corpus_5tos_usd": round(
                sum(v["gasto_usd"] for v in t["detalle_por_to_fase"].values()), 6),
        },
    }

    # desglose por veredicto: la proyección de arriba cuenta las unidades que el
    # parser ve HOY, y los TOs sin estructura aportan 0. Sin este desglose la
    # cifra se leería como el costo del universo completo, que no es.
    dig = [f for f in filas if f["veredicto"] == "digerible"]
    nec = [f for f in filas if f["veredicto"] != "digerible"]
    sin_u = [f for f in filas if f["unidades_extraccion"] == 0]
    u_dig = sum(f["unidades_extraccion"] for f in dig)
    pag_dig = sum(f["paginas"] for f in dig)
    pag_sin = sum(f["paginas"] for f in sin_u)
    # la densidad se aplica POR CATEGORÍA: los TOs de régimen informativo son
    # mucho menos densos que los de normativa general (medido tanto en los
    # digeribles de esta corrida como en el subset: ric da 84 unidades en 59
    # páginas = 1,42/pág contra 3-5/pág de los TOs de normativa general).
    # Ningún TO de régimen informativo del universo nuevo resulta digerible, así
    # que su densidad no puede estimarse de esta corrida: se toma del único TO
    # de régimen informativo que el pipeline sí digirió, `ric` del subset.
    ref = json.loads((PREP / "referencia_subset.json").read_text(encoding="utf-8"))
    dens_ric = ref["ric"]["unidades_extraccion"] / ref["ric"]["paginas"]
    dens_cat, origen_dens = {}, {}
    for cat in {f["categoria"] for f in filas}:
        d_c = [f for f in dig if f["categoria"] == cat]
        p_c = sum(f["paginas"] for f in d_c)
        if p_c:
            dens_cat[cat] = sum(f["unidades_extraccion"] for f in d_c) / p_c
            origen_dens[cat] = f"{len(d_c)} TOs digeribles de esta corrida"
        else:
            dens_cat[cat] = dens_ric
            origen_dens[cat] = "ric del subset congelado (único TO de RI digerido)"
    u_oculto = sum(f["paginas"] * dens_cat.get(f["categoria"], 0.0) for f in sin_u)
    dens = u_dig / pag_dig if pag_dig else 0.0
    agregado["por_veredicto"] = {
        "digerible": {
            "tos": len(dig), "paginas": pag_dig, "unidades": u_dig,
            "usd_total": round(u_dig * (r_e1 + r_e3), 2)},
        "necesita_reglas": {
            "tos": len(nec), "paginas": sum(f["paginas"] for f in nec),
            "unidades_visibles_hoy": sum(f["unidades_extraccion"] for f in nec),
            "usd_total_visible_hoy": round(
                sum(f["unidades_extraccion"] for f in nec) * (r_e1 + r_e3), 2)},
    }
    agregado["volumen_oculto"] = {
        "tos_con_0_unidades": len(sin_u),
        "paginas_de_esos_tos": pag_sin,
        "densidad_unidades_por_pagina_en_digeribles": round(dens, 4),
        "densidad_por_categoria": {k: {"unidades_por_pagina": round(v, 4), "origen": origen_dens[k]}
                                    for k, v in sorted(dens_cat.items())},
        "unidades_estimadas_si_se_recuperan": round(u_oculto),
        "usd_estimado_si_se_recuperan": round(u_oculto * (r_e1 + r_e3), 2),
        "nota": ("extrapolación por densidad de página POR CATEGORÍA, no medición: "
                 "esos TOs no producen unidades hoy, así que su volumen real solo "
                 "se conoce después de escribir las reglas de parseo"),
    }
    out = {"tarifas": t, "agregado": agregado, "por_to": filas}
    (PREP / "proyeccion_costo.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps({"tarifas_resumen": {k: t[k] for k in ("e1", "e3")},
                      "agregado": agregado}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
