"""U-SEG-OFICIAL, S1-quater: cifras de la lectura de la E0 corregida, desde las planillas adjudicadas (mesa, 13/10/2026; USD 0).
Sellado antes de que la autora abra la pasada 1 (`sello_scripts_adjudicacion_S1quater_mesa.txt`).

Adaptado de `s1ter/scripts/cifras_lectura_S1ter.py`, que no corre tal cual sobre S1-quater: exige las 30 y las 36 fichas de la 1.16
en la etapa 2 (`:131`), y la etapa 2 de S1-quater es solo la regresión. El diseño sellado de S1-quater (§8) nombra ese script: usar
esta copia es un desvío del diseño, declarado por decisión de la autora del 13/10/2026 (hoja de ruta de la mesa, §93).
Regla de la autora del 13/10/2026 (hoja de ruta de la mesa, §92): rige todo lo del criterio final de S1-ter que dice cómo se juzga
una unidad o cómo se cuenta la cifra; no rige lo que dependía de poblaciones o de incidentes de S1-ter que S1-quater no tiene.

Uso: python3 -B cifras_lectura_S1quater.py --orden <orden de lectura de S1-quater> --sha-orden <sha256 sellado>
       --poblaciones <poblaciones de S1-quater> --sha-poblaciones <sha256 sellado>
       --limites <poblaciones_S1ter.json> --sha-limites <sha256>
       --planilla-1 <planilla adjudicada de la etapa 1> --planilla-2 <de la etapa 2> --out <json nuevo>

Lo que queda igual que en S1-ter:
- error de corte: `marca` = error y `clase` = corte; de limpieza: `clase` = limpieza o columna `limpieza` con `restos_encabezado` o
  `restos_pie`; dudosa: `marca` = dudosa. Las mismas marcas, clases y subclases válidas.
- La cifra del piso: límite inferior de Wilson al 95 % de las unidades sin error de corte sobre las 90 de la etapa 1, sin ponderar, con
  las dudosas como correctas y como error; decide la versión con las dudosas como error (diseño de S1-quater, §1); pasa con 0,90 o más.
- Por estrato, como fracción; la del corpus: Σ peso × fracción, con los pesos de las poblaciones de S1-quater, y Wilson sobre el tamaño
  efectivo 1 / Σ(peso² / leídas).
- La limpieza, aparte. Los errores de corte en TOs de la tanda 0, aparte (mandato, `:327-328`; en S1-quater no debería haber ninguno,
  porque la tanda 0 quedó fuera de la población por la adenda 1).
- Los límites declarados que caen en la muestra, con su marca: una unidad con límite declarado cuenta como error si lo es (decisión del
  09/10/2026). La lista es la de S1-ter (`poblaciones_S1ter.json`, `cortes.limites_declarados`), comparada por id con las unidades de la
  E0 corregida: un límite cuyo id cambió en la corrección no se encuentra, y eso se declara.
- La regresión, sin cifra: solo la lista de sus marcas. Las unidades que se califican en las dos etapas, con sus dos marcas.
Lo que no rige en S1-quater (dependía de poblaciones de S1-ter): la 1.16 (a) y (b), las listas de (b) y su reversión por lista, los dos
mixtos y las reglas de la sección 3 de ri_oc y de `ri_oc::S2`.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from collections import Counter
from pathlib import Path

Z = 1.959963984540054
PISO = 0.90
TANDA0 = ("ctacte", "lingob", "polcre", "pagjub", "docvig")
ESTRATOS = {"vigente": 40, "marcadores": 10, "sin_raiz": 40}
SUBCLASES_CORTE = {"empieza_fuera", "termina_fuera", "falta_texto_propio", "trae_texto_de_otro_punto", "numero_equivocado"}
SUBCLASES_LIMPIEZA = {"restos_encabezado", "restos_pie"}
COLS = ("ficha", "paginas", "marca", "clase", "subclase", "subclase_adicional", "limpieza", "nota")


class Freno(Exception):
    pass


def wilson(k: int, n: float) -> list[float] | None:
    if n == 0:
        return None
    p = k / n
    c = 1 + Z * Z / n
    m = p + Z * Z / (2 * n)
    r = Z * math.sqrt(p * (1 - p) / n + Z * Z / (4 * n * n))
    return [(m - r) / c, (m + r) / c]


def wilson_p(p: float, n: float) -> list[float]:
    c = 1 + Z * Z / n
    m = p + Z * Z / (2 * n)
    r = Z * math.sqrt(p * (1 - p) / n + Z * Z / (4 * n * n))
    return [(m - r) / c, (m + r) / c]


def leer(p: Path) -> list[dict]:
    texto = p.read_text(encoding="utf-8")
    with open(p, encoding="utf-8", newline="") as fh:
        r = csv.DictReader(fh, delimiter="\t")
        if tuple(r.fieldnames or ()) != COLS:
            raise Freno(f"{p.name}: no tiene las columnas de la planilla")
        filas = list(r)
    if any(None in f or any(v is None for v in f.values()) for f in filas) or len(filas) != texto.count("\n") - 1:
        raise Freno(f"{p.name}: un renglón no tiene las columnas del encabezado")
    return filas


def validar(filas: list[dict]) -> list[str]:
    err = []
    for f in filas:
        if f["marca"] not in ("correcta", "error", "dudosa"):
            err.append(f"{f['ficha']}: marca «{f['marca']}»")
        if f["marca"] == "error":
            if f["clase"] not in ("corte", "limpieza"):
                err.append(f"{f['ficha']}: error sin clase")
            subs = {s for s in (f["subclase"], f["subclase_adicional"]) if s}
            validas = SUBCLASES_CORTE if f["clase"] == "corte" else SUBCLASES_LIMPIEZA
            if not subs or not subs <= (SUBCLASES_CORTE | SUBCLASES_LIMPIEZA) or f["subclase"] not in validas:
                err.append(f"{f['ficha']}: subclase «{f['subclase']}»")
        if f["limpieza"] and f["limpieza"] not in SUBCLASES_LIMPIEZA:
            err.append(f"{f['ficha']}: limpieza «{f['limpieza']}»")
    return err


def es_corte(f: dict) -> bool:
    return f["marca"] == "error" and f["clase"] == "corte"


def es_limpieza(f: dict) -> bool:
    return (f["marca"] == "error" and f["clase"] == "limpieza") or bool(f["limpieza"])


def marca(f: dict) -> dict:
    return {k: f[k] for k in ("ficha", "marca", "clase", "subclase", "subclase_adicional", "limpieza", "nota")}


def piso(filas: list[dict]) -> dict:
    n = len(filas)
    out = {}
    for nombre, dudosa_error in (("dudosas_como_correctas", False), ("dudosas_como_error", True)):
        e = sum(1 for f in filas if es_corte(f) or (dudosa_error and f["marca"] == "dudosa"))
        w = wilson(n - e, n)
        out[nombre] = {"leidas": n, "errores_de_corte": e, "sin_error_de_corte": n - e, "wilson95": w,
                       "llega_al_piso": bool(w and w[0] >= PISO)}
    out["decide"] = "dudosas_como_error"
    return out


def calcular(orden: dict, pob: dict, limites: list[dict], p1: list[dict], p2: list[dict]) -> dict:
    f1 = {x["id_opaco"]: x for x in orden["etapa_1"]["fichas"]}
    f2 = {x["id_opaco"]: x for x in orden["etapa_2"]["fichas"]}
    if sorted(f["ficha"] for f in p1) != sorted(f1) or sorted(f["ficha"] for f in p2) != sorted(f2):
        raise Freno("las planillas no traen las fichas del orden sellado")
    if len(p1) != 90 or Counter(x["estrato"] for x in f1.values()) != Counter(ESTRATOS):
        raise Freno("la etapa 1 no tiene las 90 fichas con los estratos 40 / 10 / 40")
    if any(x["poblacion"] != "cortes" for x in f1.values()) or any(x["poblacion"] != "regresion" for x in f2.values()):
        raise Freno("una ficha no es de la población que corresponde a su etapa")
    if set(pob["cortes"]) != set(ESTRATOS):
        raise Freno("las poblaciones no traen los tres estratos")
    errores = validar(p1) + validar(p2)
    if errores:
        return {"planillas_validas": False, "errores": errores}
    por_estrato, est, sum_w2n = {}, 0.0, 0.0
    for e, g in pob["cortes"].items():
        fs = [f for f in p1 if f1[f["ficha"]]["estrato"] == e]
        ok = sum(1 for f in fs if not es_corte(f))
        por_estrato[e] = {"sin_error": ok, "leidas": len(fs), "fraccion": ok / len(fs), "peso": g["peso"]}
        est += g["peso"] * ok / len(fs)
        sum_w2n += g["peso"] ** 2 / len(fs)
    n_eff = 1 / sum_w2n
    lim = {d["id"]: d for d in limites}
    uid1 = {f["ficha"]: f1[f["ficha"]]["id"] for f in p1}
    cal1 = {uid1[f["ficha"]]: f for f in p1}
    dos = [{"unidad": u, "etapa_1": marca(cal1[u]), "etapa_2": marca(f)}
           for f in p2 for u in f2[f["ficha"]]["unidades_calificadas"] if u in cal1]
    return {"planillas_validas": True,
            "etapa_1": {"cifra_del_piso": piso(p1), "por_estrato": por_estrato,
                        "cifra_del_corpus": {"estimacion": est, "n_efectivo": n_eff, "wilson95": wilson_p(est, n_eff),
                                             "nota": "aproximación: trata la muestra ponderada como simple de tamaño n_efectivo"},
                        "errores_de_corte": [marca(f) | {"unidad": uid1[f["ficha"]], "estrato": f1[f["ficha"]]["estrato"]}
                                             for f in p1 if es_corte(f)],
                        "errores_de_corte_por_subclase": dict(Counter(s for f in p1 if es_corte(f)
                                                                      for s in (f["subclase"], f["subclase_adicional"]) if s)),
                        "dudosas": [f["ficha"] for f in p1 if f["marca"] == "dudosa"],
                        "limpieza": sum(es_limpieza(f) for f in p1),
                        "tanda0_con_error_de_corte": [uid1[f["ficha"]] for f in p1
                                                      if uid1[f["ficha"]].split("::")[0] in TANDA0 and es_corte(f)],
                        "limites_declarados_en_la_muestra": {
                            "criterio": "lista de S1-ter comparada por id con las unidades de la E0 corregida",
                            "lista_de_S1ter": len(lim),
                            "en_la_muestra": [marca(f) | {"unidad": uid1[f["ficha"]], "fuentes": lim[uid1[f["ficha"]]]["fuentes"]}
                                              for f in p1 if uid1[f["ficha"]] in lim]}},
            "etapa_2": {"regresion_sin_cifra": [marca(f) | {"unidad": f2[f["ficha"]]["id"]} for f in p2],
                        "limpieza": sum(es_limpieza(f) for f in p2)},
            "unidades_en_las_dos_etapas": dos}


def main() -> None:
    ap = argparse.ArgumentParser()
    for k in ("orden", "sha_orden", "poblaciones", "sha_poblaciones", "limites", "sha_limites", "planilla_1", "planilla_2", "out"):
        ap.add_argument(f"--{k.replace('_', '-')}", dest=k, required=True)
    a = ap.parse_args()
    out = Path(a.out)
    try:
        if out.exists():
            raise Freno("la salida ya existe")
        crudo = {}
        for k in ("orden", "poblaciones", "limites"):
            crudo[k] = Path(getattr(a, k)).read_bytes()
            if hashlib.sha256(crudo[k]).hexdigest() != getattr(a, f"sha_{k}"):
                raise Freno(f"{k}: no da su sha256 sellado")
        limites = json.loads(crudo["limites"])["cortes"]["limites_declarados"]["unidades"]
        res = calcular(json.loads(crudo["orden"]), json.loads(crudo["poblaciones"]), limites,
                       leer(Path(a.planilla_1)), leer(Path(a.planilla_2)))
    except Freno as ex:
        raise SystemExit(f"FRENO: {ex}")
    out.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"planillas_validas": res["planillas_validas"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
