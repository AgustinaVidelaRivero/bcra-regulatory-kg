"""
cerrar_adjudicacion.py — Cierra la adjudicación humana de EV2: toma el worksheet
COMPLETADO (.json, marcas cumplido/no_cumplido por criterio), re-aplica el
mapping §2 (ev2_juez/mapping.py) para el veredicto de pregunta de cada ficha y
`agregar_par` (ev2_encadenamiento/code/agregacion_enc.py) donde el par pendiente
del §7 tenía votos requiere_adjudicacion, y emite:

  adjudicacion/veredictos_definitivos_ciego.json / .md
      veredicto DEFINITIVO por par, por id opaco de par (EV2R- de la base), sin
      grafo: fuente = juez (base o §7) / adjudicacion_base / adjudicacion_s7;
      pares aún incompletos quedan requiere_adjudicacion y se listan.
  adjudicacion/reporte_muestra_simetrica.md / .json
      muestra §6: veredicto del juez vs veredicto humano por ficha (ciego),
      matriz y tasa de error del juez en AMBAS direcciones; acuerdo por criterio.
  adjudicacion_SOLO_MESA/cruce_definitivo_por_grafo_SOLO_MESA.json / .md
      el cruce definitivo × grafo (SOLO_MESA: revela grafo).

Regla para la muestra §6 (pre-registro): la adjudicación de la muestra MIDE la
tasa de error del juez y se reporta junto al resultado principal; NO reemplaza
el veredicto del juez en esos pares (los definitivos de la muestra siguen
siendo los del juez, con la discrepancia marcada). Cambiar eso requiere laudo.

Todo determinístico y offline. Lógica pura en `cerrar(...)` (testeada en
tests_cerrar.py sobre casos sintéticos); la CLI solo lee/escribe archivos.

Uso:
  .venv/bin/python -B data/experiment/ev2_adjudicacion/code/cerrar_adjudicacion.py \
      --worksheet data/experiment/ev2_adjudicacion/adjudicacion/worksheet_adjudicacion_completado.json
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

import comun_adj as ca

MARCAS_VALIDAS = ("cumplido", "no_cumplido")
RESUELTOS = ("correcto", "parcial", "incorrecto")


# --------------------------------------------------------------------------- #
# Validación del worksheet completado contra la tabla SOLO_MESA               #
# --------------------------------------------------------------------------- #
def validar_worksheet(ws: dict, tabla: dict) -> dict:
    """Devuelve {id_ficha: {"marcas": [...] | None, "completa": bool, "observaciones"}}.
    Levanta ante ids desconocidos/faltantes, número de criterios distinto,
    respuesta alterada (sha256) o marca inválida. Una ficha con alguna marca
    en null es 'incompleta' (no levanta: se reporta)."""
    por_id = {f["id_ficha"]: f for f in tabla["fichas"]}
    vistos = set()
    out = {}
    for f in ws["fichas"]:
        fid = f.get("id_ficha")
        if fid not in por_id:
            raise ValueError(f"ficha desconocida en el worksheet: {fid!r}")
        if fid in vistos:
            raise ValueError(f"ficha repetida en el worksheet: {fid}")
        vistos.add(fid)
        t = por_id[fid]
        if ca.sha256_texto(f["respuesta"]) != t["sha256_respuesta"]:
            raise ValueError(f"{fid}: la respuesta de la ficha fue alterada (sha256 distinto)")
        crits = f.get("criterios") or []
        if len(crits) != t["n_criterios"]:
            raise ValueError(f"{fid}: {len(crits)} criterios en la ficha vs {t['n_criterios']} en la tabla")
        marcas = []
        for j, c in enumerate(crits, start=1):
            if c.get("indice") != j:
                raise ValueError(f"{fid}: criterio {j} con índice {c.get('indice')!r}")
            v = c.get("veredicto")
            if v is None or v == "":
                marcas.append(None)
            elif isinstance(v, str) and v.strip().lower() in MARCAS_VALIDAS:
                marcas.append(v.strip().lower())
            else:
                raise ValueError(f"{fid} C{j}: marca inválida {v!r} (válidas: {MARCAS_VALIDAS})")
        completa = all(m is not None for m in marcas)
        out[fid] = {"marcas": marcas, "completa": completa, "observaciones": f.get("observaciones")}
    faltan = sorted(set(por_id) - vistos)
    if faltan:
        raise ValueError(f"fichas de la tabla ausentes del worksheet: {faltan}")
    return out


def veredicto_humano(marcas: list[str]) -> str:
    """Mapping §2 sobre marcas humanas (sin dudoso → nunca requiere_adjudicacion)."""
    v = ca.mapping.veredicto_pregunta(marcas)
    if v == ca.ADJ:
        raise AssertionError("marcas humanas no pueden producir requiere_adjudicacion")
    return v


# --------------------------------------------------------------------------- #
# Cierre                                                                        #
# --------------------------------------------------------------------------- #
def cerrar(ws: dict, tabla: dict, finales: list[dict]) -> dict:
    """ws: worksheet completado; tabla: tabla_fichas_SOLO_MESA; finales: un
    registro por par (id_opaco_base, id_pregunta, grafo, final, fuente_final,
    veredictos_reps, ids_reps, re_corrido). Devuelve dict con 'definitivos'
    (por par, ciego), 'muestra', 'cruce_por_grafo' (SOLO_MESA), 'resueltos_dudosos'."""
    marcas = validar_worksheet(ws, tabla)
    fichas = {f["id_ficha"]: f for f in tabla["fichas"]}

    # veredicto humano por ficha y por id de respuesta cubierta
    humano_por_ficha, humano_por_respuesta = {}, {}
    for fid, f in fichas.items():
        m = marcas[fid]
        vh = veredicto_humano(m["marcas"]) if m["completa"] else None
        humano_por_ficha[fid] = vh
        for r in f["respuestas"]:
            humano_por_respuesta[r["id_opaco_respuesta"]] = (vh, fid)

    # ficha(s) por par y origen
    fichas_por_par = defaultdict(list)
    for fid, f in fichas.items():
        fichas_por_par[f["id_opaco_base"]].append(fid)

    definitivos, incompletos = [], []
    for x in finales:
        idb = x["id_opaco_base"]
        fids = sorted(fichas_por_par.get(idb, []))
        origenes = {fichas[f]["origen"] for f in fids}
        rec = {"id_opaco_base": idb, "final_juez": x["final"], "fuente_final_juez": x["fuente_final"],
               "fichas": fids}
        if x["final"] != ca.ADJ:
            rec.update({"definitivo": x["final"], "via": f"juez_{x['fuente_final']}", "completo": True})
        elif not x["re_corrido"]:
            if origenes != {"heredado_base"} or len(fids) != 1:
                raise ValueError(f"{idb}: heredado sin ficha única de origen heredado_base ({fids})")
            vh = humano_por_ficha[fids[0]]
            if vh is None:
                rec.update({"definitivo": ca.ADJ, "via": "adjudicacion_base_incompleta", "completo": False})
            else:
                rec.update({"definitivo": vh, "via": "adjudicacion_base", "completo": True,
                            "marcas_humanas": marcas[fids[0]]["marcas"]})
        else:
            if origenes != {"s7_pendiente"}:
                raise ValueError(f"{idb}: pendiente §7 con fichas de origen {origenes}")
            votos, faltantes, resol = [], [], []
            for rep, (ide, v) in enumerate(zip(x["ids_reps"], x["veredictos_reps"]), start=1):
                if v != ca.ADJ:
                    votos.append(v)
                    continue
                if ide not in humano_por_respuesta:
                    raise ValueError(f"{idb}: respuesta {ide} (r{rep}) sin ficha en la tabla")
                vh, fid = humano_por_respuesta[ide]
                if vh is None:
                    faltantes.append(ide)
                    votos.append(ca.ADJ)
                else:
                    votos.append(vh)
                    resol.append({"rep": rep, "id_opaco_respuesta": ide, "id_ficha": fid, "veredicto_humano": vh})
            rec["votos_originales"] = list(x["veredictos_reps"])
            rec["votos_resueltos"] = votos
            rec["resoluciones"] = resol
            # agregar_par tolera votos requiere_adjudicacion (regla de invariancia):
            # con faltantes el par puede igualmente quedar decidido si el resultado no
            # depende de lo que falta adjudicar
            definitivo = ca.ag.agregar_par(votos)
            if not faltantes:
                rec.update({"definitivo": definitivo, "via": "adjudicacion_s7", "completo": True})
            elif definitivo != ca.ADJ:
                rec.update({"definitivo": definitivo, "via": "adjudicacion_s7_invariante_con_faltante",
                            "completo": True, "respuestas_sin_adjudicar": faltantes})
            else:
                rec.update({"definitivo": ca.ADJ, "via": "adjudicacion_s7_incompleta",
                            "completo": False, "respuestas_sin_adjudicar": faltantes})
        if not rec["completo"]:
            incompletos.append(idb)
        definitivos.append(rec)

    # muestra §6
    muestra = []
    for fid, f in fichas.items():
        if not f["origen"].startswith("muestra_"):
            continue
        r = f["respuestas"][0]
        vh = humano_por_ficha[fid]
        acuerdo_crit = None
        if vh is not None:
            acuerdo_crit = sum(1 for a, b in zip(marcas[fid]["marcas"], r["modales_juez"]) if a == b)
        muestra.append({"id_ficha": fid, "id_opaco_base": f["id_opaco_base"], "estrato": f["origen"],
                        "veredicto_juez": f["final_juez_par"], "veredicto_humano": vh,
                        "coincide": (vh == f["final_juez_par"]) if vh is not None else None,
                        "n_criterios": f["n_criterios"], "criterios_en_acuerdo": acuerdo_crit,
                        "modales_juez": r["modales_juez"], "marcas_humanas": marcas[fid]["marcas"]})
    muestra.sort(key=lambda m: m["id_ficha"])
    muestra_resumen = resumen_muestra(muestra)

    # cómo resolvió la humana los criterios que el juez dejó dudoso/sin_consenso
    # (una vez por ficha: los textos idénticos que comparten ficha tienen modales
    # idénticos por construcción — mismo request al juez)
    res_dud = Counter()
    for fid, f in fichas.items():
        if not marcas[fid]["completa"]:
            continue
        for a, b in zip(marcas[fid]["marcas"], f["respuestas"][0]["modales_juez"]):
            if b in ("dudoso", "sin_consenso"):
                res_dud[a] += 1
    resueltos_dudosos = dict(res_dud)

    dist_def = Counter(d["definitivo"] for d in definitivos)
    dist_via = Counter(d["via"] for d in definitivos)
    n_completas = sum(1 for m in marcas.values() if m["completa"])

    # cruce por grafo (SOLO_MESA)
    grafo_por_par = {x["id_opaco_base"]: x["grafo"] for x in finales}
    cruce = {g: {v: 0 for v in RESUELTOS + (ca.ADJ,)} for g in sorted({x["grafo"] for x in finales})}
    for d in definitivos:
        cruce[grafo_por_par[d["id_opaco_base"]]][d["definitivo"]] += 1
    cruce_muestra = defaultdict(lambda: {"n": 0, "coinciden": 0, "sin_adjudicar": 0})
    for m in muestra:
        g = grafo_por_par[m["id_opaco_base"]]
        cruce_muestra[g]["n"] += 1
        if m["coincide"] is None:
            cruce_muestra[g]["sin_adjudicar"] += 1
        elif m["coincide"]:
            cruce_muestra[g]["coinciden"] += 1

    return {"n_fichas": len(fichas), "n_fichas_completas": n_completas,
            "fichas_incompletas": sorted(fid for fid, m in marcas.items() if not m["completa"]),
            "definitivos": sorted(definitivos, key=lambda d: d["id_opaco_base"]),
            "distribucion_definitivos": dict(dist_def), "vias": dict(dist_via),
            "pares_incompletos": sorted(incompletos),
            "muestra": muestra, "muestra_resumen": muestra_resumen,
            "resueltos_dudosos": resueltos_dudosos,
            "cruce_por_grafo": cruce, "cruce_muestra_por_grafo": dict(cruce_muestra),
            "veredicto_humano_por_ficha": humano_por_ficha}


def resumen_muestra(muestra: list[dict]) -> dict:
    """Tasa de error del juez en ambas direcciones sobre la muestra §6:
      - dirección A (sobre-acreditación): juez 'correcto' y humana ≠ correcto;
      - dirección B (sub-acreditación): juez parcial/incorrecto y humana 'correcto';
      - además: desacuerdo de grado (parcial ↔ incorrecto) y matriz completa."""
    adj = [m for m in muestra if m["veredicto_humano"] is not None]
    matriz = defaultdict(Counter)
    for m in adj:
        matriz[m["veredicto_juez"]][m["veredicto_humano"]] += 1
    corr = [m for m in adj if m["veredicto_juez"] == "correcto"]
    pi = [m for m in adj if m["veredicto_juez"] in ("parcial", "incorrecto")]
    errA = sum(1 for m in corr if m["veredicto_humano"] != "correcto")
    errB = sum(1 for m in pi if m["veredicto_humano"] == "correcto")
    grado = sum(1 for m in pi if m["veredicto_humano"] in ("parcial", "incorrecto")
                and m["veredicto_humano"] != m["veredicto_juez"])
    crit_tot = sum(m["n_criterios"] for m in adj)
    crit_ok = sum(m["criterios_en_acuerdo"] for m in adj)
    return {"n_muestra": len(muestra), "n_adjudicadas": len(adj),
            "n_sin_adjudicar": len(muestra) - len(adj),
            "matriz_juez_x_humano": {k: dict(v) for k, v in matriz.items()},
            "acuerdo_exacto": sum(1 for m in adj if m["coincide"]),
            "direccion_A_sobre_acreditacion": {"n_juez_correcto": len(corr), "errores": errA,
                                               "tasa": (errA / len(corr)) if corr else None},
            "direccion_B_sub_acreditacion": {"n_juez_parcial_incorrecto": len(pi), "errores": errB,
                                             "tasa": (errB / len(pi)) if pi else None},
            "desacuerdo_de_grado_parcial_incorrecto": grado,
            "acuerdo_por_criterio": {"n_criterios": crit_tot, "en_acuerdo": crit_ok,
                                     "tasa": (crit_ok / crit_tot) if crit_tot else None}}


# --------------------------------------------------------------------------- #
# Render                                                                        #
# --------------------------------------------------------------------------- #
def md_definitivos(res: dict) -> str:
    L = ["# Veredictos DEFINITIVOS por par — CIEGO (id opaco de par; el cruce por grafo lo hace la mesa)\n",
         f"- fichas: {res['n_fichas']}; completas: {res['n_fichas_completas']}; incompletas: {res['fichas_incompletas']}",
         f"- distribución definitiva (120 pares): {res['distribucion_definitivos']}",
         f"- vías: {res['vias']}",
         f"- pares aún incompletos (siguen requiere_adjudicacion): {res['pares_incompletos']}",
         f"- criterios que el juez dejó dudoso/sin_consenso, resueltos por la adjudicación como: {res['resueltos_dudosos']}",
         "\n| id_opaco_base | final juez | fuente juez | definitivo | vía | votos resueltos | fichas |",
         "|---|---|---|---|---|---|---|"]
    for d in res["definitivos"]:
        L.append(f"| {d['id_opaco_base']} | {d['final_juez']} | {d['fuente_final_juez']} | {d['definitivo']} | "
                 f"{d['via']} | {'/'.join(d['votos_resueltos']) if d.get('votos_resueltos') else '-'} | "
                 f"{', '.join(d['fichas']) or '-'} |")
    return "\n".join(L) + "\n"


def md_muestra(res: dict) -> str:
    r = res["muestra_resumen"]
    L = ["# Muestra simétrica §6 — juez vs adjudicación humana (CIEGO)\n",
         "La muestra mide la tasa de error del juez en ambas direcciones; no reemplaza el veredicto "
         "del juez en esos pares (pre-registro §6).\n",
         f"- fichas en la muestra: {r['n_muestra']}; adjudicadas: {r['n_adjudicadas']}; sin adjudicar: {r['n_sin_adjudicar']}",
         f"- acuerdo exacto: {r['acuerdo_exacto']} / {r['n_adjudicadas']}",
         f"- matriz juez × humano: {r['matriz_juez_x_humano']}",
         f"- dirección A (juez correcto, humana ≠ correcto): {r['direccion_A_sobre_acreditacion']}",
         f"- dirección B (juez parcial/incorrecto, humana correcto): {r['direccion_B_sub_acreditacion']}",
         f"- desacuerdo de grado (parcial ↔ incorrecto): {r['desacuerdo_de_grado_parcial_incorrecto']}",
         f"- acuerdo por criterio (marca humana vs modal del juez): {r['acuerdo_por_criterio']}",
         "\n| id_ficha | id_opaco_base | estrato | juez | humano | coincide | criterios en acuerdo |",
         "|---|---|---|---|---|---|---|"]
    for m in res["muestra"]:
        L.append(f"| {m['id_ficha']} | {m['id_opaco_base']} | {m['estrato']} | {m['veredicto_juez']} | "
                 f"{m['veredicto_humano']} | {m['coincide']} | "
                 f"{m['criterios_en_acuerdo']}/{m['n_criterios']} |")
    return "\n".join(L) + "\n"


def md_cruce(res: dict) -> str:
    L = ["# Cruce DEFINITIVO × grafo (SOLO_MESA)\n",
         "| grafo | correcto | parcial | incorrecto | req.adj. |", "|---|---|---|---|---|"]
    for g, c in res["cruce_por_grafo"].items():
        L.append(f"| {g} | {c['correcto']} | {c['parcial']} | {c['incorrecto']} | {c[ca.ADJ]} |")
    L += ["\n## Muestra §6 por grafo\n", "| grafo | n | coinciden | sin adjudicar |", "|---|---|---|---|"]
    for g, c in sorted(res["cruce_muestra_por_grafo"].items()):
        L.append(f"| {g} | {c['n']} | {c['coinciden']} | {c['sin_adjudicar']} |")
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--worksheet", required=True, help="worksheet_adjudicacion COMPLETADO (.json)")
    ap.add_argument("--tabla", default=str(ca.TABLA_FICHAS))
    ap.add_argument("--out-dir", default=str(ca.ADJ_DIR))
    ap.add_argument("--solo-mesa-dir", default=str(ca.SOLO_MESA_DIR))
    a = ap.parse_args()

    ws = json.loads(Path(a.worksheet).read_text(encoding="utf-8"))
    tabla = json.loads(Path(a.tabla).read_text(encoding="utf-8"))
    ins = ca.cargar_insumos()
    finales = ca.finales_por_par(ins)
    # la tabla debe corresponder a estos insumos
    if tabla.get("sellos_insumos") != ca.sellos_insumos():
        raise RuntimeError("la tabla SOLO_MESA no corresponde a los insumos actuales (sellos distintos)")

    res = cerrar(ws, tabla, finales)
    out, sm = Path(a.out_dir), Path(a.solo_mesa_dir)
    out.mkdir(parents=True, exist_ok=True)
    sm.mkdir(parents=True, exist_ok=True)
    meta = {"generado": datetime.now().isoformat(timespec="seconds"), "worksheet": str(Path(a.worksheet).name),
            "sha256_worksheet": ca.sha256_path(Path(a.worksheet)), "sellos_insumos": ca.sellos_insumos()}
    ciego = {k: v for k, v in res.items() if k not in ("cruce_por_grafo", "cruce_muestra_por_grafo",
                                                        "veredicto_humano_por_ficha")}
    (out / "veredictos_definitivos_ciego.json").write_text(
        json.dumps({**meta, **{k: v for k, v in ciego.items() if k not in ("muestra", "muestra_resumen")}},
                   ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out / "veredictos_definitivos_ciego.md").write_text(md_definitivos(res), encoding="utf-8")
    (out / "reporte_muestra_simetrica.json").write_text(
        json.dumps({**meta, "muestra": res["muestra"], "muestra_resumen": res["muestra_resumen"]},
                   ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out / "reporte_muestra_simetrica.md").write_text(md_muestra(res), encoding="utf-8")
    (sm / "cruce_definitivo_por_grafo_SOLO_MESA.json").write_text(
        json.dumps({**meta, "SOLO_MESA": True, "cruce_por_grafo": res["cruce_por_grafo"],
                    "cruce_muestra_por_grafo": res["cruce_muestra_por_grafo"]}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8")
    (sm / "cruce_definitivo_por_grafo_SOLO_MESA.md").write_text(md_cruce(res), encoding="utf-8")
    print(json.dumps({"n_fichas": res["n_fichas"], "completas": res["n_fichas_completas"],
                      "distribucion_definitivos": res["distribucion_definitivos"], "vias": res["vias"],
                      "pares_incompletos": res["pares_incompletos"],
                      "muestra_resumen": res["muestra_resumen"]}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
