"""
cierre_adj_tanda0.py — U-TANDA0-2A, anexo E5.c (docs/mandatos/UTANDA0_2A_E5c_adjudicacion.md,
0488a9b): cierre de la adjudicación ciega de C2 a C5. Escrito en E5.c.1; corre
en E5.c.3 sobre las marcas de la autora selladas por commit. USD 0, sin API.

Molde: ev2_r1/code/cierre_r1.py (774acac): cargar marcas, humanos_por_ficha,
resolver_definitivos (:110-159) y evaluar_muestra (:194-224); validación de
marcas de ev2_adjudicacion/code/cerrar_adjudicacion.py (03ebe83).

  1. Marcas: planilla_mezclada_marcas.csv y planilla_c5_marcas.csv (columnas
     id_ficha, indice, veredicto, observacion). El sha de cada CSV se verifica
     contra el commit de la autora (git show <commit>:<ruta>), igual que las
     planillas y los SOLO_MESA, que además se re-derivan con
     planillas_tanda0.construir(). Completitud: cada (id_ficha, indice) de la
     planilla una sola vez, con veredicto cumplido | no_cumplido
     (cierre_r1.py:83-91). Una falta levanta: no se completa.
  2. Veredicto humano por ficha: mapping.veredicto_pregunta sobre sus marcas,
     en código.
  3. Definitivos por celda (anexo, decisión 6): las marcas de
     planilla_mezclada se reparten por celda con la tabla SOLO_MESA. Lo no
     adjudicado conserva su final (vías juez_base y juez_enc); un heredado
     toma el veredicto humano (adjudicacion_base); un pendiente del §7
     reemplaza cada voto requiere_adjudicacion por el veredicto humano de su
     ficha y re-agrega con agregar_par (adjudicacion_s7). Un par que siga en
     requiere_adjudicacion levanta (FRENO).
  4. Tabla definitiva de C2, C3 y C4 al lado de la definitiva de C1 (774acac,
     cierre_r1.json, 6/26/8) con Wilson al 95 % para correcto e incorrecto;
     C5 aparte, sin cruzar con C1 a C4.
  5. Tasa de error del juez desde la población B (molde evaluar_muestra):
     acuerdo exacto por ficha, acuerdo por criterio, sobre-acreditación y
     sub-acreditación, caída de correctos; por celda y agregada para C2 a C4;
     C5 aparte. La muestra no reemplaza veredictos.

Salidas: reports/tanda0/tabla_celdas_definitiva_E5c.{json,md} (agregados,
sin veredictos por pregunta ni pertenencias) y
adjudicacion_SOLO_MESA/definitivos_por_par_tanda0_SOLO_MESA.json (por par y
por ficha de la muestra). Doble cómputo byte-idéntico antes de agregar la fecha.

Uso (E5.c.3):  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B \
    data/experiment/ev2_tanda0/code/cierre_adj_tanda0.py --commit-marcas <hash>
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
import subprocess
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import planillas_tanda0 as pt              # noqa: E402

ADJ = pt.ADJ
ag, mapping = pt.ag, pt.mapping
REPO_DIR = pt.REPO_DIR
CELDAS_NUCLEO = ("C2", "C3", "C4")
Z95 = 1.959963984540054

C1_CIERRE = pt.EXP_DIR / "ev2_r1" / "cierre" / "cierre_r1.json"
C1_DEFINITIVA_ESPERADA = {"correcto": 6, "parcial": 26, "incorrecto": 8}
OUT_JSON = REPO_DIR / "reports" / "tanda0" / "tabla_celdas_definitiva_E5c.json"
OUT_MD = REPO_DIR / "reports" / "tanda0" / "tabla_celdas_definitiva_E5c.md"
DEFINITIVOS_SM = pt.SOLO_MESA_DIR / "definitivos_por_par_tanda0_SOLO_MESA.json"


# --------------------------------------------------------------------------- #
# Marcas                                                                       #
# --------------------------------------------------------------------------- #
def leer_marcas_csv(texto: str, nombre: str) -> dict[tuple[str, int], dict]:
    filas = list(csv.reader(io.StringIO(texto)))
    if not filas or filas[0] != pt.COLUMNAS_CSV:
        raise ValueError(f"{nombre}: encabezado distinto de {pt.COLUMNAS_CSV}")
    out: dict[tuple[str, int], dict] = {}
    for i, fila in enumerate(filas[1:], start=2):
        if not fila:
            continue
        if len(fila) != len(pt.COLUMNAS_CSV):
            raise ValueError(f"{nombre}: fila {i} con {len(fila)} columnas")
        fid, idx, ver, obs = fila
        try:
            j = int(idx)
        except ValueError:
            raise ValueError(f"{nombre}: fila {i} con índice no entero") from None
        v = ver.strip().lower()
        if not v:
            raise ValueError(f"{nombre}: fila {i} sin veredicto (FRENO: no se completa)")
        if v not in pt.MARCAS_VALIDAS:
            raise ValueError(f"{nombre}: fila {i} con marca fuera del dominio {pt.MARCAS_VALIDAS}")
        clave = (fid.strip(), j)
        if clave in out:
            raise ValueError(f"{nombre}: fila {i} repite una marca ya dada")
        out[clave] = {"veredicto": v, "observacion": obs}
    return out


def validar_completitud(marcas: dict, pj: dict, nombre: str) -> None:
    esperadas = {(f["id_ficha"], c["indice"]) for f in pj["fichas"] for c in f["criterios"]}
    faltan, sobran = esperadas - set(marcas), set(marcas) - esperadas
    if faltan or sobran:
        raise ValueError(f"{nombre}: {len(faltan)} marcas faltantes y {len(sobran)} ajenas a la "
                         "planilla (FRENO: no se completa)")


def humanos_por_ficha(pj: dict, marcas: dict) -> dict[str, dict]:
    out = {}
    for f in pj["fichas"]:
        m = [marcas[(f["id_ficha"], c["indice"])]["veredicto"] for c in f["criterios"]]
        v = mapping.veredicto_pregunta(m)
        if v == ADJ:
            raise AssertionError("marcas humanas no pueden dar requiere_adjudicacion")
        out[f["id_ficha"]] = {"marcas": m, "veredicto_humano": v}
    return out


# --------------------------------------------------------------------------- #
# Definitivos por celda (cierre_r1.resolver_definitivos, por celda)            #
# --------------------------------------------------------------------------- #
def resolver_definitivos(fin: list[dict], fichas_celda: list[dict], hum: dict) -> dict:
    ficha_de_resp = {}
    for m in fichas_celda:
        for r in m["respuestas"]:
            ficha_de_resp[r["id_opaco_respuesta"]] = m["id_ficha"]
    definitivos = []
    for x in fin:
        rec = {"id_pregunta": x["id_pregunta"], "id_opaco_base": x["id_opaco_base"],
               "final_pre_adjudicacion": x["final"], "re_corrido": x["re_corrido"],
               "tipo_enc": x["tipo_enc"], "veredictos_reps": x["veredictos_reps"],
               "ids_reps": x["ids_reps"]}
        if x["final"] != ADJ:
            rec.update({"definitivo": x["final"],
                        "via": "juez_enc" if x["fuente_final"] == "s7" else "juez_base"})
        elif not x["re_corrido"]:
            fid = ficha_de_resp.get(x["id_opaco_base"])
            if fid is None:
                raise ValueError("heredado sin ficha")
            rec.update({"definitivo": hum[fid]["veredicto_humano"], "via": "adjudicacion_base",
                        "id_ficha": fid, "marcas_humanas": hum[fid]["marcas"]})
        else:
            votos, resol = [], []
            for rep, (ide, v) in enumerate(zip(x["ids_reps"], x["veredictos_reps"]), start=1):
                if v == ADJ:
                    fid = ficha_de_resp.get(ide)
                    if fid is None:
                        raise ValueError("voto requiere_adjudicacion sin ficha")
                    v = hum[fid]["veredicto_humano"]
                    resol.append({"rep": rep, "id_opaco_respuesta": ide, "id_ficha": fid,
                                  "veredicto_humano": v, "marcas_humanas": hum[fid]["marcas"]})
                votos.append(v)
            defin = ag.agregar_par(votos)
            if defin == ADJ:
                raise RuntimeError("un par sigue en requiere_adjudicacion tras adjudicar (FRENO)")
            rec.update({"definitivo": defin, "via": "adjudicacion_s7",
                        "votos_resueltos": votos, "resoluciones": resol})
        definitivos.append(rec)
    return {"definitivos": definitivos,
            "tabla_definitiva": {k: sum(1 for d in definitivos if d["definitivo"] == k)
                                 for k in ("correcto", "parcial", "incorrecto")},
            "vias": {k: sum(1 for d in definitivos if d["via"] == k)
                     for k in ("juez_base", "juez_enc", "adjudicacion_base", "adjudicacion_s7")}}


# --------------------------------------------------------------------------- #
# Tasa de error del juez (cierre_r1.evaluar_muestra, por celda)                #
# --------------------------------------------------------------------------- #
def evaluar_muestra(fichas_celda: list[dict], hum: dict) -> dict:
    filas = []
    for m in fichas_celda:
        if m["origen"] not in ("muestra_correcto", "muestra_parcial_incorrecto"):
            continue
        h = hum[m["id_ficha"]]
        modales = m["respuestas"][0]["modales_juez"]
        por_crit = list(zip(h["marcas"], modales))
        filas.append({"id_ficha": m["id_ficha"], "origen": m["origen"],
                      "veredicto_juez": m["final_juez_par"], "veredicto_humano": h["veredicto_humano"],
                      "acuerdo_exacto": m["final_juez_par"] == h["veredicto_humano"],
                      "n_criterios": m["n_criterios"],
                      "criterios_acuerdo": sum(1 for a, b in por_crit if a == b),
                      "juez_sobre_acredita": sum(1 for a, b in por_crit if a == "no_cumplido" and b == "cumplido"),
                      "juez_sub_acredita": sum(1 for a, b in por_crit if a == "cumplido" and b == "no_cumplido")})
    return resumir_muestra(filas)


def resumir_muestra(filas: list[dict]) -> dict:
    corr = [f for f in filas if f["origen"] == "muestra_correcto"]
    return {"n_fichas": len(filas),
            "acuerdo_exacto": sum(f["acuerdo_exacto"] for f in filas),
            "criterios": sum(f["n_criterios"] for f in filas),
            "criterios_acuerdo": sum(f["criterios_acuerdo"] for f in filas),
            "sobre_acreditacion_criterios": sum(f["juez_sobre_acredita"] for f in filas),
            "sub_acreditacion_criterios": sum(f["juez_sub_acredita"] for f in filas),
            "flip_descendente_correctos": sum(1 for f in corr if f["veredicto_humano"] != "correcto"),
            "n_correctos_auditados": len(corr),
            "filas": sorted(filas, key=lambda f: f["id_ficha"])}


def sin_filas(m: dict) -> dict:
    return {k: v for k, v in m.items() if k != "filas"}


def wilson(k: int, n: int) -> list[float]:
    if n == 0:
        return [0.0, 0.0]
    p = k / n
    den = 1 + Z95 ** 2 / n
    centro = p + Z95 ** 2 / (2 * n)
    radio = Z95 * math.sqrt(p * (1 - p) / n + Z95 ** 2 / (4 * n ** 2))
    return [round(max(0.0, (centro - radio) / den), 4), round(min(1.0, (centro + radio) / den), 4)]


def c1_definitiva() -> dict:
    t = json.loads(C1_CIERRE.read_text(encoding="utf-8"))["tabla_definitiva_r1"]
    t = {k: t.get(k, 0) for k in ("correcto", "parcial", "incorrecto")}
    if t != C1_DEFINITIVA_ESPERADA:
        raise RuntimeError("la definitiva de C1 en cierre_r1.json no es 6/26/8")
    return t


# --------------------------------------------------------------------------- #
# Cómputo (puro: recibe textos de marcas, planillas y la re-derivación)        #
# --------------------------------------------------------------------------- #
def computar(csv_por_planilla: dict[str, str], pjs: dict[str, dict], res: dict,
             c1: dict | None = None) -> dict:
    hum, obs = {}, 0
    for nom, pj in pjs.items():
        marcas = leer_marcas_csv(csv_por_planilla[nom], f"{nom}_marcas.csv")
        validar_completitud(marcas, pj, f"{nom}_marcas.csv")
        obs += sum(1 for v in marcas.values() if v["observacion"].strip())
        hum.update(humanos_por_ficha(pj, marcas))
    mesa = [m for p in res["planillas"].values() for m in p["mesa"]]
    if {m["id_ficha"] for m in mesa} != set(hum):
        raise ValueError("fichas marcadas distintas de las de la tabla SOLO_MESA")
    celdas, sm = {}, {}
    for c, pc in res["por_celda"].items():
        fc = [m for m in mesa if m["celda"] == c]                 # reparto por celda
        d = resolver_definitivos(pc["fin"], fc, hum)
        mu = evaluar_muestra(fc, hum)
        n = len(pc["fin"])
        t = d["tabla_definitiva"]
        celdas[c] = {"n": n, "tabla_definitiva": t, "vias": d["vias"],
                     "wilson95": {"correcto": wilson(t["correcto"], n),
                                  "incorrecto": wilson(t["incorrecto"], n)},
                     "tasa_error_juez": sin_filas(mu)}
        sm[c] = {"definitivos": d["definitivos"], "muestra_por_ficha": mu["filas"]}
    agregada = resumir_muestra([f for c in CELDAS_NUCLEO for f in sm[c]["muestra_por_ficha"]])
    c1 = c1 if c1 is not None else c1_definitiva()
    return {"c1_definitiva_774acac": {**c1, "n": 40,
                                      "wilson95": {"correcto": wilson(c1["correcto"], 40),
                                                   "incorrecto": wilson(c1["incorrecto"], 40)}},
            "celdas": celdas,
            "tasa_error_juez_agregada_C2_C4": sin_filas(agregada),
            "n_observaciones_en_marcas": obs,
            "solo_mesa": sm}


# --------------------------------------------------------------------------- #
# Verificación contra el commit de la autora                                   #
# --------------------------------------------------------------------------- #
def git_show(commit: str, ruta_rel: str) -> bytes:
    r = subprocess.run(["git", "-C", str(REPO_DIR), "show", f"{commit}:{ruta_rel}"],
                       capture_output=True)
    if r.returncode != 0:
        raise RuntimeError(f"{ruta_rel} no está en el commit {commit}")
    return r.stdout


def verificar_commit(commit: str, rutas: list[Path], mostrar=git_show) -> dict:
    out = {}
    for p in rutas:
        rel = pt.rel_repo(p)
        en_commit = mostrar(commit, rel)
        if pt.sha256_path(p) != hashlib.sha256(en_commit).hexdigest():
            raise RuntimeError(f"{rel}: el archivo difiere del sellado en {commit}")
        out[rel] = pt.sha256_path(p)
    return out


def render_md(r: dict) -> str:
    c1 = r["c1_definitiva_774acac"]
    L = ["# Tabla definitiva de las celdas C2 a C5 (anexo E5.c de U-TANDA0-2A)", "",
         f"Generado {r['generado']}. Marcas de la autora selladas en `{r['commit_marcas']}`; veredicto "
         "por ficha con el mapping §2 en código; pendientes del §7 re-agregados con agregar_par; "
         "doble cómputo byte-idéntico. Comando: `cierre_adj_tanda0.py --commit-marcas "
         f"{r['commit_marcas']}`.", "",
         "## 1. C2, C3 y C4 al lado de C1", "",
         "| celda | grafo, backend | n | correcto | parcial | incorrecto | Wilson 95 % correcto | Wilson 95 % incorrecto |",
         "|---|---|---|---|---|---|---|---|",
         f"| C1 (`774acac`, citada) | r1, memoria | 40 | {c1['correcto']} | {c1['parcial']} | {c1['incorrecto']} | "
         f"{c1['wilson95']['correcto'][0]}–{c1['wilson95']['correcto'][1]} | "
         f"{c1['wilson95']['incorrecto'][0]}–{c1['wilson95']['incorrecto'][1]} |"]
    nombres = {"C2": "r1, Neo4j", "C3": "desarrollo tanda 0, memoria", "C4": "desarrollo tanda 0, Neo4j",
               "C5": "diez, memoria (20 preguntas nuevas)"}
    for c in CELDAS_NUCLEO:
        x = r["celdas"][c]
        t, w = x["tabla_definitiva"], x["wilson95"]
        L.append(f"| {c} | {nombres[c]} | {x['n']} | {t['correcto']} | {t['parcial']} | {t['incorrecto']} | "
                 f"{w['correcto'][0]}–{w['correcto'][1]} | {w['incorrecto'][0]}–{w['incorrecto'][1]} |")
    L += ["", "Vías de los definitivos (juez_base / juez_enc / adjudicacion_base / adjudicacion_s7):"]
    for c in CELDAS_NUCLEO + ("C5",):
        v = r["celdas"][c]["vias"]
        L.append(f"- {c}: {v['juez_base']} / {v['juez_enc']} / {v['adjudicacion_base']} / {v['adjudicacion_s7']}")
    x = r["celdas"]["C5"]
    t, w = x["tabla_definitiva"], x["wilson95"]
    L += ["", "## 2. C5 aparte (no se cruza con C1 a C4)", "",
          "| celda | grafo, backend | n | correcto | parcial | incorrecto | Wilson 95 % correcto | Wilson 95 % incorrecto |",
          "|---|---|---|---|---|---|---|---|",
          f"| C5 | {nombres['C5']} | {x['n']} | {t['correcto']} | {t['parcial']} | {t['incorrecto']} | "
          f"{w['correcto'][0]}–{w['correcto'][1]} | {w['incorrecto'][0]}–{w['incorrecto'][1]} |", "",
          "## 3. Tasa de error del juez desde la población B (no reemplaza veredictos)", "",
          "| alcance | fichas | acuerdo exacto | criterios en acuerdo | sobre-acreditación | sub-acreditación | caída de correctos |",
          "|---|---|---|---|---|---|---|"]
    filas = [(c, r["celdas"][c]["tasa_error_juez"]) for c in CELDAS_NUCLEO] \
        + [("C2 a C4 agregada", r["tasa_error_juez_agregada_C2_C4"]), ("C5 (aparte)", r["celdas"]["C5"]["tasa_error_juez"])]
    for nom, m in filas:
        L.append(f"| {nom} | {m['n_fichas']} | {m['acuerdo_exacto']}/{m['n_fichas']} | "
                 f"{m['criterios_acuerdo']}/{m['criterios']} | {m['sobre_acreditacion_criterios']} | "
                 f"{m['sub_acreditacion_criterios']} | {m['flip_descendente_correctos']}/{m['n_correctos_auditados']} |")
    L += ["", "Salvedades: muestras de una a cuatro fichas por celda; en C5, las dos preguntas con "
          "criterios sin cita quedan fuera del marco de la muestra (anexo, decisión 2); episodios en "
          "`data/experiment/ev2_tanda0/adjudicacion/nota_episodios_adjudicacion_tanda0.md`.", ""]
    return "\n".join(L)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--commit-marcas", required=True)
    a = ap.parse_args()
    print("== Cierre de la adjudicación de C2 a C5 (anexo E5.c, E5.c.3, USD 0) ==")
    res = pt.construir()
    pub, sm_files = pt.publicables(res), pt.solo_mesa(res)
    for p, t in {**pub, **sm_files}.items():
        if p.read_text(encoding="utf-8") != t:
            raise RuntimeError(f"{pt.rel_repo(p)} difiere de su re-derivación")
    sellos = verificar_commit(a.commit_marcas, list(pub) + list(sm_files))
    pjs = {n: json.loads(pt.planilla_json_path(n).read_text(encoding="utf-8")) for n in pt.PLANILLAS}
    csvs = {n: pt.marcas_csv_path(n).read_text(encoding="utf-8") for n in pt.PLANILLAS}
    r1, r2 = computar(csvs, pjs, res), computar(csvs, pjs, res)
    if json.dumps(r1, ensure_ascii=False, sort_keys=True) != json.dumps(r2, ensure_ascii=False, sort_keys=True):
        raise RuntimeError("doble cómputo NO byte-idéntico")
    sm = r1.pop("solo_mesa")
    r1.update({"unidad": "U-TANDA0-2A anexo E5.c, cierre (USD 0)", "commit_marcas": a.commit_marcas,
               "sellos_verificados_contra_commit": sellos, "doble_computo_byte_identico": True,
               "generado": datetime.now().isoformat(timespec="seconds")})
    OUT_JSON.write_text(json.dumps(r1, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_md(r1), encoding="utf-8")
    DEFINITIVOS_SM.write_text(json.dumps({"SOLO_MESA": True, "commit_marcas": a.commit_marcas,
                                          "celdas": sm}, ensure_ascii=False, indent=2) + "\n",
                              encoding="utf-8")
    for c, x in r1["celdas"].items():
        print(f"  {c}: definitiva {x['tabla_definitiva']} | vías {x['vias']}")
    print(f"  tasa de error del juez C2 a C4: {r1['tasa_error_juez_agregada_C2_C4']}")
    for p in (OUT_JSON, OUT_MD, DEFINITIVOS_SM):
        print(f"  -> {pt.rel_repo(p)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
