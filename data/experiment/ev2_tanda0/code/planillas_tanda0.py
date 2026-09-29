"""
planillas_tanda0.py — U-TANDA0-2A, anexo E5.c (docs/mandatos/UTANDA0_2A_E5c_adjudicacion.md,
firmado en 0488a9b), etapa E5.c.1: poblaciones A y B, fichas y las dos
planillas CIEGAS de adjudicación humana de las celdas C2 a C5. USD 0, ninguna
llamada a la API.

Molde: ev2_r1/code/worksheet_r1.py (774acac), a su vez molde de
ev2_adjudicacion/code/comun_adj.py y construir_worksheet.py (03ebe83).

Reutiliza por import, sin editar:
  - agregacion_enc.agregar_par (regla sellada 9044a04);
  - mapping.veredicto_modal / veredicto_pregunta (mapping fijo §2);
  - celdas_tanda0 (registro de celdas, rutas y preguntas de C5 con sha
    verificado, celdas_tanda0.py:71-73; criterios sin cita autorizados, :84-85);
  - enc_tanda0.derivar_poblacion (población del §7 derivada de la base, solo
    lectura: verifica que los pares re-corridos sean los que manda la regla).
Replica parametrizado por celda lo que el molde cablea a r1 (finales por par,
población A, muestra B, fichas por texto idéntico, render): worksheet_r1 lee
sus rutas, semillas y esperados de comun_r1.

Reglas (anexo, decisiones 1 a 3):
  - Población A por celda: los pares con final requiere_adjudicacion. Un par
    heredado de la base (no re-corrido) da una ficha sobre la respuesta base;
    un par pendiente del §7 da una ficha por cada voto requiere_adjudicacion
    de sus re-corridas, y dos re-corridas con texto idéntico comparten ficha;
    el par decidido por invariancia no da ficha (worksheet_r1.py:6-12).
  - Población B por celda: ceil(10 %) del estrato correcto y ceil(10 %) del
    estrato parcial + incorrecto sobre los finales post-§7, con generador nuevo
    por estrato (random.Random(semilla de la celda)) sobre ids ordenados; par
    re-corrido → la re-corrida de menor rep cuyo veredicto coincide con el
    final; no re-corrido → la base (worksheet_r1.py:13-19 y :201-239). Mide la
    tasa de error del juez; no reemplaza veredictos.
  - C5: las dos preguntas con criterios sin cita (T0F-008 y T0F-013) quedan
    fuera del marco de muestreo de B (decisión 2 del anexo).
  - Dos planillas: planilla_mezclada (fichas de C2, C3 y C4, un solo sorteo
    de orden sobre la unión) y planilla_c5. La ficha comparte texto solo
    dentro de un par de la misma celda. El id de ficha es FT0- + los primeros
    8 hex de sha256(sal de la planilla | celda | pregunta | sha de la
    respuesta). La pertenencia de cada ficha a su celda, el origen (A o B),
    los veredictos del juez y los censos por celda van solo a
    adjudicacion_SOLO_MESA/.
  - Cada ficha muestra: n, id de ficha, TO y nombre del TO, ancla del gold,
    pregunta, respuesta completa sin editar, criterios con su cita textual y
    un campo de observaciones. En los tres criterios sin cita de C5 la cita se
    reemplaza por TEXTO_SIN_CITA.
  - Las marcas van a <planilla>_marcas.csv (columnas id_ficha, indice,
    veredicto, observacion), que esta etapa genera con una fila por criterio
    en el orden de la planilla y las columnas veredicto y observacion vacías.

Salidas (sin fechas: dos corridas dan archivos byte-idénticos):
  adjudicacion/planilla_mezclada.{json,md}, planilla_c5.{json,md},
  planilla_mezclada_marcas.csv, planilla_c5_marcas.csv, censo_planillas_ciego.md
  adjudicacion_SOLO_MESA/pertenencia_fichas_tanda0_SOLO_MESA.json,
  tabla_fichas_tanda0_SOLO_MESA.json, poblaciones_tanda0_SOLO_MESA.json,
  censo_tanda0_SOLO_MESA.md
Si una salida existe y difiere de lo recomputado, levanta.

La salida estándar publica solo el número de fichas y de criterios por
planilla (anexo, FRENO E5.c.1). El selftest no-fuga
(selftest_nofuga_tanda0.py) es obligatorio antes de entregar.

Uso:  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/ev2_tanda0/code/planillas_tanda0.py
"""

from __future__ import annotations

import csv
import hashlib
import io
import json
import math
import random
import sys
from collections import Counter
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent                  # ev2_tanda0/code
TANDA0_DIR = CODE_DIR.parent                                # data/experiment/ev2_tanda0
EXP_DIR = TANDA0_DIR.parent                                 # data/experiment
REPO_DIR = EXP_DIR.parent.parent

for _p in (CODE_DIR, EXP_DIR / "ev2_encadenamiento" / "code", EXP_DIR / "ev2_juez"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import celdas_tanda0 as ce0                 # noqa: E402  (registro de celdas, rutas, gold de C5)
import enc_tanda0 as et                     # noqa: E402  (población del §7, solo lectura)
import agregacion_enc as ag                 # noqa: E402  (regla sellada 9044a04)
import mapping                              # noqa: E402  (mapping fijo §2)

ADJ = "requiere_adjudicacion"
FRACCION_MUESTRA = 0.10
PREFIJO_FICHA = "FT0-"
TEXTO_SIN_CITA = "el criterio no trae cita textual en el gold"
MARCAS_VALIDAS = ("cumplido", "no_cumplido")
COLUMNAS_CSV = ["id_ficha", "indice", "veredicto", "observacion"]

CELDAS_ADJ = ("C2", "C3", "C4", "C5")
# semilla de la muestra B, una propia por celda (anexo, decisión 1)
SEMILLA_MUESTRA = {"C2": "adjudicacion-ev2-tanda0-c2", "C3": "adjudicacion-ev2-tanda0-c3",
                   "C4": "adjudicacion-ev2-tanda0-c4", "C5": "adjudicacion-ev2-tanda0-c5"}
# C5: preguntas fuera del marco de muestreo de B (anexo, decisión 2): las de
# los criterios sin cita autorizados (celdas_tanda0.py:84-85)
EXCLUIDAS_MUESTRA = {"C5": frozenset(q for q, _ in ce0.CRITERIOS_CITA_VACIA_AUTORIZADOS)}

PLANILLAS = {
    "planilla_mezclada": {"celdas": ("C2", "C3", "C4"),
                          "semilla_orden": "orden-planilla-tanda0-mezclada",
                          "sal_id_ficha": "ficha-planilla-tanda0-mezclada"},
    "planilla_c5": {"celdas": ("C5",),
                    "semilla_orden": "orden-planilla-tanda0-c5",
                    "sal_id_ficha": "ficha-planilla-tanda0-c5"},
}

# Tabla pre-adjudicación sellada en E5 (7f3b207): los finales recomputados deben reproducirla
TABLA_E5 = REPO_DIR / "reports" / "tanda0" / "tabla_celdas_E5.json"
SHA_TABLA_E5 = "dd919e75f0ada72b45f4bdd94d9c041f14de50129e03dda2a08a2260293db610"

# Totales esperados, recomputados por la mesa el 29/09/2026 (anexo, E5.c.1 b): se verifican
ESPERADO_PARES_ADJ = 25
ESPERADO_OBJETIVOS_A = 29
ESPERADO_FICHAS_B = 14

ADJ_DIR = TANDA0_DIR / "adjudicacion"
SOLO_MESA_DIR = TANDA0_DIR / "adjudicacion_SOLO_MESA"
CENSO_CIEGO = ADJ_DIR / "censo_planillas_ciego.md"
PERTENENCIA_SM = SOLO_MESA_DIR / "pertenencia_fichas_tanda0_SOLO_MESA.json"
TABLA_FICHAS_SM = SOLO_MESA_DIR / "tabla_fichas_tanda0_SOLO_MESA.json"
POBLACIONES_SM = SOLO_MESA_DIR / "poblaciones_tanda0_SOLO_MESA.json"
CENSO_SM = SOLO_MESA_DIR / "censo_tanda0_SOLO_MESA.md"


def planilla_json_path(nombre: str) -> Path:
    return ADJ_DIR / f"{nombre}.json"


def planilla_md_path(nombre: str) -> Path:
    return ADJ_DIR / f"{nombre}.md"


def marcas_csv_path(nombre: str) -> Path:
    return ADJ_DIR / f"{nombre}_marcas.csv"


sha256_texto = ce0.sha256_texto
sha256_path = ce0.sha256_path
rel_repo = ce0.rel_repo


# --------------------------------------------------------------------------- #
# Gold (lo que la ficha muestra)                                              #
# --------------------------------------------------------------------------- #
def cargar_gold_fichas(celda: ce0.Celda) -> dict[str, dict]:
    """{id_pregunta: {pregunta, to, to_nombre, ancla, criterios[{criterio,
    cita_textual, sin_cita}]}}. EV2: archivo sellado con sha verificado
    (comun_r1.GOLD_SHA256_ESPERADO). C5: preguntas_tanda0.json con sha
    verificado y la guarda de criterios sin cita de celdas_tanda0."""
    if celda.conjunto == "ev2":
        sha = sha256_path(ce0.cf.GOLD_PATH)
        if sha != ce0.cr.GOLD_SHA256_ESPERADO:
            raise RuntimeError(f"gold de EV2 alterado: {sha}")
        ps = json.loads(ce0.cf.GOLD_PATH.read_text(encoding="utf-8"))["preguntas"]
        n_esp, c_esp = 40, 164
    else:
        ce0.cargar_gold_celda(celda)            # aplica la guarda de citas vacías
        ps = ce0.cargar_preguntas_c5()          # sha verificado
        n_esp, c_esp = ce0.N_PREGUNTAS_C5, ce0.N_CRITERIOS_C5
    out = {}
    for p in ps:
        crits = []
        for j, c in enumerate(p["gold"]["criterios"], start=1):
            vacia = not c["cita_textual"].strip()
            if vacia and (p["id"], j) not in ce0.CRITERIOS_CITA_VACIA_AUTORIZADOS:
                raise ValueError("criterio sin cita no autorizado")
            crits.append({"criterio": c["criterio"],
                          "cita_textual": TEXTO_SIN_CITA if vacia else c["cita_textual"],
                          "sin_cita": vacia})
        out[p["id"]] = {"pregunta": p["pregunta"], "to": p["to"], "to_nombre": p["to_nombre"],
                        "ancla": list(p["gold"]["ancla"]), "criterios": crits}
    if len(out) != n_esp or sum(len(v["criterios"]) for v in out.values()) != c_esp:
        raise ValueError(f"gold inesperado en {celda.id}")
    return out


# --------------------------------------------------------------------------- #
# Insumos por celda (solo lectura) y recómputo propio                         #
# --------------------------------------------------------------------------- #
def rutas_insumos(celda: ce0.Celda, rutas: ce0.Rutas = ce0.RUTAS) -> dict[str, Path]:
    d = rutas.celda(celda)
    sm = d / "desanonimizacion_SOLO_MESA"
    return {"base_agg": d / "base" / "veredictos_agregados_ciego.json",
            "base_tab": sm / "tabla_id_opaco_base_SOLO_MESA.json",
            "enc_fin": d / "reporte" / "veredictos_finales_s7.json",
            "enc_agg": d / "enc" / "veredictos_agregados_ciego.json",
            "enc_tab": sm / "tabla_id_opaco_s7_SOLO_MESA.json",
            **{f"base_r{r}": d / "base" / f"veredictos_r{r}.jsonl" for r in (1, 2, 3)},
            **{f"enc_r{r}": d / "enc" / f"veredictos_r{r}.jsonl" for r in (1, 2, 3)}}


def _leer_json(p: Path):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def _crudos(paths: list[Path]) -> dict[str, dict[int, list[str]]]:
    """{id_opaco: {rep: [veredicto por criterio, en orden de índice]}} desde
    los veredictos crudos del juez por repetición."""
    out: dict[str, dict[int, list[str]]] = {}
    for p in paths:
        for ln in Path(p).read_text(encoding="utf-8").splitlines():
            if not ln.strip():
                continue
            r = json.loads(ln)
            crit = sorted(r["criterios"], key=lambda c: c["indice"])
            if [c["indice"] for c in crit] != list(range(1, len(crit) + 1)):
                raise ValueError("índices de criterio no contiguos en un veredicto crudo")
            rep = int(r["rep"])
            if rep in out.setdefault(r["id_opaco"], {}):
                raise ValueError("veredicto crudo repetido")
            out[r["id_opaco"]][rep] = [c["veredicto"] for c in crit]
    return out


def recomputar_respuestas(agg: dict, crudos: dict) -> dict[str, dict]:
    """Por respuesta: modales (mapping.veredicto_modal sobre las 3 reps crudas)
    y veredicto (mapping.veredicto_pregunta); levanta si no reproduce el
    agregado persistido por el juez."""
    out = {}
    for a in agg["agregados"]:
        reps = crudos.get(a["id_opaco"])
        if reps is None or sorted(reps) != [1, 2, 3]:
            raise ValueError("respuesta sin sus tres repeticiones crudas")
        n = a["n_criterios"]
        if any(len(v) != n for v in reps.values()):
            raise ValueError("número de criterios inconsistente entre repeticiones")
        modales = [mapping.veredicto_modal([reps[r][j] for r in (1, 2, 3)]) for j in range(n)]
        v = mapping.veredicto_pregunta(modales)
        if modales != a["modales"] or v != a["veredicto_pregunta"]:
            raise ValueError("el recómputo desde los crudos no reproduce el agregado del juez")
        out[a["id_opaco"]] = {"modales": modales, "veredicto_pregunta": v}
    return out


def cargar_insumos(celda: ce0.Celda, rutas: ce0.Rutas = ce0.RUTAS) -> dict:
    p = rutas_insumos(celda, rutas)
    n = 40 if celda.conjunto == "ev2" else ce0.N_PREGUNTAS_C5
    base_agg, base_tab = _leer_json(p["base_agg"]), _leer_json(p["base_tab"])
    enc_fin, enc_agg, enc_tab = _leer_json(p["enc_fin"]), _leer_json(p["enc_agg"]), _leer_json(p["enc_tab"])
    if base_agg["n_agregados"] != n or base_tab["n"] != n or base_agg["incompletas"]:
        raise ValueError(f"base inesperada en {celda.id}")
    if enc_fin["n_pares_incompletos"] != 0 or enc_fin["faltantes_agente"]:
        raise ValueError(f"§7 incompleto en {celda.id}")
    n_enc = 3 * enc_fin["n_pares_agregados"]
    if enc_agg["n_agregados"] != n_enc or enc_tab["n"] != n_enc or enc_agg["incompletas"]:
        raise ValueError(f"juez del §7 inesperado en {celda.id}")
    rec_base = recomputar_respuestas(base_agg, _crudos([p[f"base_r{r}"] for r in (1, 2, 3)]))
    rec_enc = recomputar_respuestas(enc_agg, _crudos([p[f"enc_r{r}"] for r in (1, 2, 3)]))
    return {"celda": celda,
            "base_agg": {a["id_opaco"]: a for a in base_agg["agregados"]},
            "base_tab": {f["id_opaco"]: f for f in base_tab["filas"]},
            "enc_pares": {x["id_opaco_base"]: x for x in enc_fin["pares"]},
            "enc_agg": {a["id_opaco"]: a for a in enc_agg["agregados"]},
            "enc_tab": {f["id_opaco"]: f for f in enc_tab["filas"]},
            "rec_base": rec_base, "rec_enc": rec_enc,
            "gold": cargar_gold_fichas(celda),
            "sellos": {rel_repo(v): sha256_path(v) for v in p.values()}}


def leer_respuesta(celda: ce0.Celda, fila: dict, rutas: ce0.Rutas = ce0.RUTAS) -> str:
    """Texto de la respuesta desde su traza, con el sha256 de la tabla del juez."""
    path = rutas.trazas / fila["label"] / f"{ce0.rv._sanitizar(fila['id_pregunta'])}.json"
    t = _leer_json(path)
    r = (t["trace"].get("final_json") or {}).get("respuesta")
    if not isinstance(r, str) or not r.strip():
        raise ValueError("traza sin respuesta parseada")
    if sha256_texto(r) != fila["sha256_respuesta"]:
        raise ValueError("sha256 de la respuesta no coincide con la tabla del juez")
    return r


# --------------------------------------------------------------------------- #
# Finales por par, población A y muestra B (molde worksheet_r1, por celda)    #
# --------------------------------------------------------------------------- #
def finales_por_par(ins: dict) -> list[dict]:
    celda = ins["celda"]
    xs = []
    for idb, fb in ins["base_tab"].items():
        a = ins["base_agg"][idb]
        vb = ins["rec_base"][idb]["veredicto_pregunta"]
        if fb["id_opaco"] != idb or fb["label"] != celda.label:
            raise ValueError("fila de la tabla base inconsistente")
        rec = {"celda": celda.id, "id_pregunta": fb["id_pregunta"], "id_opaco_base": idb,
               "veredicto_base": vb, "modales_base": a["modales"],
               "sha256_respuesta_base": fb["sha256_respuesta"]}
        p = ins["enc_pares"].get(idb)
        if p is None:
            rec.update({"re_corrido": False, "tipo_enc": None, "final": vb, "fuente_final": "base",
                        "ids_reps": None, "veredictos_reps": None, "via_enc": None})
        else:
            if p["veredicto_base"] != vb:
                raise ValueError("veredicto base inconsistente entre la base y el §7")
            votos = []
            for rep, ide in enumerate(p["ids_reps"], start=1):
                fe = ins["enc_tab"][ide]
                if fe["rep"] != rep or fe["id_opaco_base"] != idb or fe["id_pregunta"] != fb["id_pregunta"]:
                    raise ValueError("rep o par inconsistente en la tabla del §7")
                votos.append(ins["rec_enc"][ide]["veredicto_pregunta"])
            if votos != list(p["veredictos_reps"]):
                raise ValueError("votos del §7 no reproducen el recómputo desde los crudos")
            final = ag.agregar_par(votos)
            if final != p["final"]:
                raise ValueError("agregado del §7 no reproduce con agregar_par")
            rec.update({"re_corrido": True, "tipo_enc": p["tipo"], "final": final,
                        "fuente_final": "s7", "ids_reps": list(p["ids_reps"]),
                        "veredictos_reps": votos, "via_enc": p["via"]})
        xs.append(rec)
    if len({x["id_pregunta"] for x in xs}) != len(xs):
        raise ValueError("pares repetidos")
    # los pares re-corridos son los que manda la regla del §7 (enc_tanda0.derivar_poblacion)
    pob = et.derivar_poblacion(celda, ce0.RUTAS)
    if {q["id_pregunta"] for q in pob["pares"]} != {x["id_pregunta"] for x in xs if x["re_corrido"]}:
        raise ValueError("pares re-corridos distintos de la población del §7 derivada de la base")
    return sorted(xs, key=lambda x: x["id_pregunta"])


def _objetivo_base(x: dict) -> dict:
    return {"id_opaco_respuesta": x["id_opaco_base"], "rep": None, "origen_respuesta": "base",
            "sha256_respuesta": x["sha256_respuesta_base"],
            "veredicto_juez_respuesta": x["veredicto_base"], "modales_juez": x["modales_base"]}


def _objetivo_enc(x: dict, rep: int, ins: dict) -> dict:
    ide = x["ids_reps"][rep - 1]
    fe, ae = ins["enc_tab"][ide], ins["enc_agg"][ide]
    return {"id_opaco_respuesta": ide, "rep": rep, "origen_respuesta": "enc",
            "sha256_respuesta": fe["sha256_respuesta"],
            "veredicto_juez_respuesta": ins["rec_enc"][ide]["veredicto_pregunta"],
            "modales_juez": ae["modales"]}


def poblacion_a(fin: list[dict], ins: dict) -> dict:
    heredados, pendientes = [], []
    for x in fin:
        if x["final"] != ADJ:
            continue
        if not x["re_corrido"]:
            heredados.append({**x, "objetivos": [_objetivo_base(x)]})
        else:
            objs = [_objetivo_enc(x, rep, ins)
                    for rep, v in enumerate(x["veredictos_reps"], start=1) if v == ADJ]
            if not objs:
                raise ValueError("pendiente del §7 sin votos requiere_adjudicacion")
            pendientes.append({**x, "objetivos": objs})
    return {"heredados": heredados, "pendientes_s7": pendientes}


def muestra_estrato(ids_pregunta: list[str], semilla: str) -> list[str]:
    ids = sorted(ids_pregunta)
    if not ids:
        return []
    k = math.ceil(FRACCION_MUESTRA * len(ids))
    return sorted(random.Random(semilla).sample(ids, k))    # generador nuevo por estrato


def objetivo_muestra(x: dict, ins: dict) -> dict:
    if not x["re_corrido"]:
        return _objetivo_base(x)
    for rep, v in enumerate(x["veredictos_reps"], start=1):
        if v == x["final"]:
            return _objetivo_enc(x, rep, ins)
    raise ValueError("ninguna re-corrida coincide con el final del par")


def muestra_b(fin: list[dict], ins: dict) -> dict:
    c = ins["celda"].id
    excl = EXCLUIDAS_MUESTRA.get(c, frozenset())
    por_q = {x["id_pregunta"]: x for x in fin}
    marco = [x for x in fin if x["id_pregunta"] not in excl]
    corr = [x["id_pregunta"] for x in marco if x["final"] == "correcto"]
    pi = [x["id_pregunta"] for x in marco if x["final"] in ("parcial", "incorrecto")]
    sc, sp = muestra_estrato(corr, SEMILLA_MUESTRA[c]), muestra_estrato(pi, SEMILLA_MUESTRA[c])
    out = {"semilla": SEMILLA_MUESTRA[c],
           "excluidas_del_marco": sorted(excl),
           "detalle_estratos": {"correcto": {"n": len(corr), "k": len(sc), "ids": sc},
                                "parcial_incorrecto": {"n": len(pi), "k": len(sp), "ids": sp}},
           "correcto": [], "parcial_incorrecto": []}
    for estrato, ids in (("correcto", sc), ("parcial_incorrecto", sp)):
        for q in ids:
            x = por_q[q]
            out[estrato].append({**x, "objetivos": [objetivo_muestra(x, ins)]})
    return out


# --------------------------------------------------------------------------- #
# Fichas por celda y planillas                                                #
# --------------------------------------------------------------------------- #
def fichas_celda(ins: dict, rutas: ce0.Rutas = ce0.RUTAS) -> dict:
    celda = ins["celda"]
    fin = finales_por_par(ins)
    pob_a = poblacion_a(fin, ins)
    mb = muestra_b(fin, ins)
    fichas: dict[tuple, dict] = {}

    def agregar(x: dict, obj: dict, origen: str):
        clave = (celda.id, x["id_pregunta"], obj["sha256_respuesta"])
        d = fichas.get(clave)
        if d is None:
            fila = (ins["base_tab"] if obj["origen_respuesta"] == "base"
                    else ins["enc_tab"])[obj["id_opaco_respuesta"]]
            d = fichas[clave] = {"celda": celda.id, "id_pregunta": x["id_pregunta"],
                                 "sha256_respuesta": obj["sha256_respuesta"],
                                 "respuesta": leer_respuesta(celda, fila, rutas), "objetivos": []}
        d["objetivos"].append({"origen": origen, "id_opaco_base": x["id_opaco_base"],
                               "final_juez_par": x["final"], "fuente_final": x["fuente_final"],
                               "veredictos_reps": x["veredictos_reps"], "ids_reps": x["ids_reps"],
                               **obj})

    for x in pob_a["heredados"]:
        for o in x["objetivos"]:
            agregar(x, o, "heredado_base")
    for x in pob_a["pendientes_s7"]:
        for o in x["objetivos"]:
            agregar(x, o, "s7_pendiente")
    for est, origen in (("correcto", "muestra_correcto"),
                        ("parcial_incorrecto", "muestra_parcial_incorrecto")):
        for x in mb[est]:
            for o in x["objetivos"]:
                agregar(x, o, origen)
    for d in fichas.values():
        if len({o["origen"] for o in d["objetivos"]}) != 1 \
                or len({o["id_opaco_base"] for o in d["objetivos"]}) != 1:
            raise ValueError("ficha con objetivos heterogéneos")
    return {"fin": fin, "pob_a": pob_a, "muestra": mb, "fichas": fichas}


def id_ficha(sal: str, celda: str, id_pregunta: str, sha_resp: str) -> str:
    return PREFIJO_FICHA + sha256_texto(f"{sal}|{celda}|{id_pregunta}|{sha_resp}")[:8]


def armar_planilla(nombre: str, por_celda: dict[str, dict], golds: dict[str, dict]) -> dict:
    cfg = PLANILLAS[nombre]
    fichas = {}
    for c in cfg["celdas"]:
        for d in por_celda[c]["fichas"].values():
            fid = id_ficha(cfg["sal_id_ficha"], d["celda"], d["id_pregunta"], d["sha256_respuesta"])
            if fid in fichas:
                raise ValueError("colisión de ids de ficha")
            fichas[fid] = d
    orden = sorted(fichas)                                   # un solo sorteo sobre la unión
    random.Random(cfg["semilla_orden"]).shuffle(orden)
    ws, mesa = [], []
    for n, fid in enumerate(orden, start=1):
        d = fichas[fid]
        g = golds[d["celda"]][d["id_pregunta"]]
        o0 = d["objetivos"][0]
        ws.append({"n": n, "id_ficha": fid, "to": g["to"], "to_nombre": g["to_nombre"],
                   "ancla": list(g["ancla"]), "pregunta": g["pregunta"], "respuesta": d["respuesta"],
                   "criterios": [{"indice": j, "criterio": c["criterio"], "cita_textual": c["cita_textual"]}
                                 for j, c in enumerate(g["criterios"], start=1)],
                   "observaciones": None})
        mesa.append({"planilla": nombre, "n": n, "id_ficha": fid, "celda": d["celda"],
                     "id_pregunta": d["id_pregunta"], "sha256_respuesta": d["sha256_respuesta"],
                     "n_criterios": len(g["criterios"]),
                     "criterios_sin_cita": [j for j, c in enumerate(g["criterios"], start=1) if c["sin_cita"]],
                     "origen": o0["origen"], "id_opaco_base": o0["id_opaco_base"],
                     "final_juez_par": o0["final_juez_par"], "fuente_final": o0["fuente_final"],
                     "veredictos_reps": o0["veredictos_reps"], "ids_reps": o0["ids_reps"],
                     "respuestas": [{"id_opaco_respuesta": o["id_opaco_respuesta"], "rep": o["rep"],
                                     "origen_respuesta": o["origen_respuesta"],
                                     "veredicto_juez_respuesta": o["veredicto_juez_respuesta"],
                                     "modales_juez": o["modales_juez"]} for o in d["objetivos"]]})
    return {"nombre": nombre, "fichas": ws, "mesa": mesa}


def construir(rutas: ce0.Rutas = ce0.RUTAS) -> dict:
    """Todo el cómputo, sin escribir. Verifica los esperados del anexo."""
    celdas = {c: ce0.CELDAS[c] for c in CELDAS_ADJ}
    ins = {c: cargar_insumos(celdas[c], rutas) for c in CELDAS_ADJ}
    por_celda = {c: fichas_celda(ins[c], rutas) for c in CELDAS_ADJ}
    golds = {c: ins[c]["gold"] for c in CELDAS_ADJ}
    planillas = {nom: armar_planilla(nom, por_celda, golds) for nom in PLANILLAS}
    ver = verificar_esperados(por_celda, planillas)
    sellos = {k: v for c in CELDAS_ADJ for k, v in ins[c]["sellos"].items()}
    sellos[rel_repo(TABLA_E5)] = sha256_path(TABLA_E5)
    return {"por_celda": por_celda, "planillas": planillas, "verificacion": ver, "sellos": sellos}


def verificar_esperados(por_celda: dict, planillas: dict) -> dict:
    if sha256_path(TABLA_E5) != SHA_TABLA_E5:
        raise RuntimeError("tabla_celdas_E5.json alterada")
    tabla_e5 = _leer_json(TABLA_E5)["celdas"]
    dist = {c: dict(Counter(x["final"] for x in por_celda[c]["fin"])) for c in CELDAS_ADJ}
    esperado = {c: {k: v for k, v in tabla_e5[c]["tabla_pre_adjudicacion"].items() if v}
                for c in CELDAS_ADJ}
    if dist != esperado:
        raise ValueError("los finales recomputados no reproducen tabla_celdas_E5.json")
    pares_adj = sum(dist[c].get(ADJ, 0) for c in CELDAS_ADJ)
    obj_a = sum(len(x["objetivos"]) for c in CELDAS_ADJ
                for k in ("heredados", "pendientes_s7") for x in por_celda[c]["pob_a"][k])
    pares_a = sum(len(por_celda[c]["pob_a"][k]) for c in CELDAS_ADJ
                  for k in ("heredados", "pendientes_s7"))
    fichas_b = sum(1 for p in planillas.values() for m in p["mesa"] if m["origen"].startswith("muestra_"))
    if (pares_adj, pares_a, obj_a, fichas_b) != (ESPERADO_PARES_ADJ, ESPERADO_PARES_ADJ,
                                                ESPERADO_OBJETIVOS_A, ESPERADO_FICHAS_B):
        raise ValueError("poblaciones fuera de los totales del anexo (25 pares, 29 respuestas "
                         "objetivo en A, 14 fichas en B): FRENO; detalle solo con la mesa")
    for c in CELDAS_ADJ:
        excl = EXCLUIDAS_MUESTRA.get(c, frozenset())
        if any(x["id_pregunta"] in excl for est in ("correcto", "parcial_incorrecto")
               for x in por_celda[c]["muestra"][est]):
            raise ValueError("pregunta excluida del marco de B presente en la muestra")
    return {"finales_por_celda": dist, "finales_reproducen_tabla_E5": True,
            "pares_adj_total": pares_adj, "objetivos_a_total": obj_a, "fichas_b_total": fichas_b,
            "esperados_anexo": {"pares_adj": ESPERADO_PARES_ADJ, "objetivos_a": ESPERADO_OBJETIVOS_A,
                                "fichas_b": ESPERADO_FICHAS_B}}


# --------------------------------------------------------------------------- #
# Render de los publicables                                                    #
# --------------------------------------------------------------------------- #
INSTRUCCIONES = (
    "Adjudicar cada ficha contra el PDF del Texto Ordenado indicado (el ancla del gold es el "
    "punto de partida) y contra la cita del gold, criterio por criterio. Para cada criterio "
    "marcar exactamente uno: cumplido (la respuesta satisface lo que el criterio exige, conforme "
    "a la norma) o no_cumplido (no lo satisface, lo contradice o no lo trata); no hay opción "
    "intermedia. El veredicto de la pregunta no se pone a mano: lo computa el mapping §2 en "
    "código a partir de las marcas. Las marcas se vuelcan en el CSV de marcas de esta planilla, "
    "una fila por criterio (id_ficha, indice); la observación es libre y opcional. Cada ficha se "
    "adjudica por sí sola: las fichas no indican de qué corrida proviene la respuesta ni qué "
    "veredicto recibió, y no debe intentarse inferirlo. Si una pregunta aparece más de una vez, "
    "cada ficha se marca por su propia respuesta.")


def planilla_json(p: dict) -> dict:
    return {"planilla": p["nombre"], "n_fichas": len(p["fichas"]),
            "n_criterios": sum(len(f["criterios"]) for f in p["fichas"]),
            "marcas_validas": list(MARCAS_VALIDAS),
            "csv_de_marcas": f"{p['nombre']}_marcas.csv",
            "instrucciones": INSTRUCCIONES,
            "fichas": p["fichas"]}


def render_md(pj: dict) -> str:
    out = [f"# Planilla de adjudicación ciega: {pj['planilla']}\n",
           f"Fichas: {pj['n_fichas']}. Criterios a marcar: {pj['n_criterios']}. "
           f"Marcas válidas: `cumplido` | `no_cumplido`. CSV de marcas: `{pj['csv_de_marcas']}`.\n",
           "## Instrucciones\n", pj["instrucciones"] + "\n", "---\n"]
    for f in pj["fichas"]:
        out.append(f"\n## Ficha {f['n']} · `{f['id_ficha']}`\n")
        out.append(f"**TO:** {f['to_nombre']} (`{f['to']}`) · **Ancla del gold:** {', '.join(f['ancla'])}\n")
        out.append(f"**Pregunta:**\n\n{f['pregunta']}\n")
        out.append("**Respuesta del sistema (completa):**\n")
        out.append("\n".join("> " + ln for ln in f["respuesta"].splitlines()) + "\n")
        out.append("**Criterios del gold:**\n")
        for c in f["criterios"]:
            out.append(f"- **Criterio {c['indice']}.** {c['criterio']}")
            if c["cita_textual"] == TEXTO_SIN_CITA:
                out.append(f"  - Cita textual del TO: {TEXTO_SIN_CITA}")
            else:
                out.append(f"  - Cita textual del TO: «{c['cita_textual']}»")
            out.append("  - Marca: `____________` (cumplido / no_cumplido)")
        out.append("\n**Observaciones (opcional):** ______________________________________\n")
        out.append("---\n")
    return "\n".join(out)


def render_csv(pj: dict) -> str:
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(COLUMNAS_CSV)
    for f in pj["fichas"]:
        for c in f["criterios"]:
            w.writerow([f["id_ficha"], c["indice"], "", ""])
    return buf.getvalue()


def render_censo_ciego(planillas: dict) -> str:
    L = ["# Censo ciego de las planillas de adjudicación\n",
         "| planilla | fichas | criterios |", "|---|---|---|"]
    for nom, p in planillas.items():
        L.append(f"| {nom} | {len(p['fichas'])} | {sum(len(f['criterios']) for f in p['fichas'])} |")
    return "\n".join(L) + "\n"


def publicables(res: dict) -> dict[Path, str]:
    out = {}
    for nom, p in res["planillas"].items():
        pj = planilla_json(p)
        out[planilla_json_path(nom)] = json.dumps(pj, ensure_ascii=False, indent=2) + "\n"
        out[planilla_md_path(nom)] = render_md(pj)
        out[marcas_csv_path(nom)] = render_csv(pj)
    out[CENSO_CIEGO] = render_censo_ciego(res["planillas"])
    return out


# --------------------------------------------------------------------------- #
# SOLO_MESA                                                                    #
# --------------------------------------------------------------------------- #
REGLA_ID = "id_ficha = 'FT0-' + sha256(sal_de_la_planilla|celda|id_pregunta|sha256(respuesta))[:8]"


def censo_mesa_md(res: dict) -> str:
    L = ["# Censo por celda y por origen de las planillas (SOLO_MESA)\n",
         "| celda | planilla | finales pre-adjudicación | pares ADJ heredados | pares ADJ pendientes §7 | "
         "votos ADJ con ficha | fichas A | fichas B correcto | fichas B parcial+incorrecto | "
         "marco B correcto / p+i | excluidas del marco |",
         "|---|---|---|---|---|---|---|---|---|---|---|"]
    mesa = [m for p in res["planillas"].values() for m in p["mesa"]]
    for c in CELDAS_ADJ:
        pc = res["por_celda"][c]
        mc = [m for m in mesa if m["celda"] == c]
        o = Counter(m["origen"] for m in mc)
        det = pc["muestra"]["detalle_estratos"]
        L.append(f"| {c} | {mc[0]['planilla'] if mc else '-'} | {res['verificacion']['finales_por_celda'][c]} | "
                 f"{len(pc['pob_a']['heredados'])} | {len(pc['pob_a']['pendientes_s7'])} | "
                 f"{sum(len(x['objetivos']) for x in pc['pob_a']['pendientes_s7'])} | "
                 f"{o['heredado_base'] + o['s7_pendiente']} | {o['muestra_correcto']} | "
                 f"{o['muestra_parcial_incorrecto']} | {det['correcto']['n']} / {det['parcial_incorrecto']['n']} | "
                 f"{', '.join(pc['muestra']['excluidas_del_marco']) or '-'} |")
    v = res["verificacion"]
    L += ["", f"- totales: pares ADJ {v['pares_adj_total']}, respuestas objetivo en A {v['objetivos_a_total']}, "
              f"fichas B {v['fichas_b_total']} (esperados del anexo {v['esperados_anexo']})",
          f"- fichas por planilla y origen: " + "; ".join(
              f"{nom} {dict(Counter(m['origen'] for m in p['mesa']))}" for nom, p in res["planillas"].items())]
    return "\n".join(L) + "\n"


def solo_mesa(res: dict) -> dict[Path, str]:
    mesa = [m for p in res["planillas"].values() for m in p["mesa"]]
    pert = {"SOLO_MESA": True, "regla_id_ficha": REGLA_ID,
            "sales": {n: c["sal_id_ficha"] for n, c in PLANILLAS.items()},
            "fichas": [{"planilla": m["planilla"], "n": m["n"], "id_ficha": m["id_ficha"],
                        "celda": m["celda"]} for m in mesa]}
    tabla = {"SOLO_MESA": True, "regla_id_ficha": REGLA_ID,
             "planillas": {n: {"celdas": list(c["celdas"]), "semilla_orden": c["semilla_orden"],
                               "sal_id_ficha": c["sal_id_ficha"]} for n, c in PLANILLAS.items()},
             "semillas_muestra": SEMILLA_MUESTRA, "texto_sin_cita": TEXTO_SIN_CITA,
             "sellos_insumos": res["sellos"], "n_fichas": len(mesa), "fichas": mesa}
    pobs = {"SOLO_MESA": True, "sellos_insumos": res["sellos"], "verificacion": res["verificacion"],
            "regla_final": "par re-corrido en el §7 → agregar_par(votos recomputados desde los crudos); resto → base",
            "regla_muestra": ("por celda y estrato, ids ordenados, random.Random(semilla de la celda)"
                              ".sample(ids, ceil(0.10·n)), generador nuevo por estrato; C5 sin las "
                              "preguntas de criterios sin cita"),
            "celdas": {c: {"finales_por_par": pc["fin"],
                           "poblacion_a": pc["pob_a"],
                           "muestra_b": pc["muestra"]} for c, pc in res["por_celda"].items()}}
    return {PERTENENCIA_SM: json.dumps(pert, ensure_ascii=False, indent=2) + "\n",
            TABLA_FICHAS_SM: json.dumps(tabla, ensure_ascii=False, indent=2) + "\n",
            POBLACIONES_SM: json.dumps(pobs, ensure_ascii=False, indent=2) + "\n",
            CENSO_SM: censo_mesa_md(res)}


def escribir(archivos: dict[Path, str]) -> None:
    for p, contenido in archivos.items():
        if p.exists() and p.read_text(encoding="utf-8") != contenido:
            raise RuntimeError(f"{rel_repo(p)} ya existe y difiere de lo recomputado")
    for p, contenido in archivos.items():
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(contenido, encoding="utf-8")


def main() -> int:
    print("== Planillas ciegas de adjudicación de C2 a C5 (anexo E5.c, E5.c.1, USD 0) ==")
    res = construir()
    res2 = construir()                                       # doble cómputo interno
    pub, sm = publicables(res), solo_mesa(res)
    if pub != publicables(res2) or sm != solo_mesa(res2):
        raise RuntimeError("doble cómputo NO byte-idéntico")
    escribir({**pub, **sm})
    for nom, p in res["planillas"].items():
        print(f"  {nom}: {len(p['fichas'])} fichas, "
              f"{sum(len(f['criterios']) for f in p['fichas'])} criterios")
    print("  totales del anexo verificados; finales recomputados = tabla_celdas_E5.json")
    for p in list(pub) + list(sm):
        print(f"  -> {rel_repo(p)}")
    print("  SIGUIENTE PASO OBLIGATORIO: selftest_nofuga_tanda0.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
