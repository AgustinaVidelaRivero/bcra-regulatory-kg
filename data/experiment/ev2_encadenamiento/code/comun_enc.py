"""
comun_enc.py — Infraestructura común del ENCADENAMIENTO del protocolo EV2
(docs/protocolo_corrida_ev2.md §3-§5; docs/preregistro_evaluacion_fidelidad_ev2.md §7).

Qué encadena: los veredictos de la corrida base de fidelidad
(data/experiment/ev2_fidelidad_eval/, juez v1 congelado) disparan
  (a) re-corrida N=3 del AGENTE sobre cada par (pregunta, grafo) con veredicto
      base "parcial" — trigger mecánico único, protocolo §3;
  (b) auditoría simétrica: re-corrida N=3 sobre una muestra del 10 % de los
      "correcto" de cada grafo, semilla `auditoria-ev2-v1` sobre ids ordenados
      (protocolo §3; con 3/4/2 correctos el 10 % redondea a cero → laudo:
      mínimo 1 por grafo, ceil).
Las respuestas nuevas se evalúan con el MISMO juez congelado y el MISMO
pipeline ciego de la corrida base (pre-registro §7: "sin cambios").

Este módulo NO edita nada fuera de data/experiment/ev2_encadenamiento/. Importa:
  - el runner de la corrida base del agente (data/experiment/ev2_corrida/code/
    runner_ev2.py + comun_ev2.py: harness congelado, mismo modelo hardcodeado,
    grafos verificados por sha 3/3, captura completa de trazas);
  - el pipeline ciego del juez (data/experiment/ev2_fidelidad_eval/code/
    comun_fidelidad.py + pipeline_fidelidad.py), que a su vez importa el juez
    congelado (data/experiment/ev2_juez/{juez,mapping}.py, prompt v1 sha256
    fd446f8e61f4…). Nada de eso se edita: sha verificados al inicio y al fin.

Ceguera: esta unidad CONOCE el grafo de cada par (inevitable para re-correr el
agente), pero el JUEZ sigue ciego: cada respuesta nueva recibe un id opaco
nuevo por el mismo esquema de la base (prefijo + sha256(salt|…)[:10]) con salt
propio y con la repetición en la clave (dos re-corridas de un mismo par pueden
producir texto idéntico; sin la rep en la clave colisionarían), y el input del
juez sigue siendo exactamente prompt + (pregunta, respuesta, criterios). La
tabla id_opaco_nuevo → (id_pregunta, grafo, rep, sha256 respuesta) va en
`desanonimizacion_SOLO_MESA/`, fuera de las salidas ciegas del juez.
"""

from __future__ import annotations

import hashlib
import json
import math
import random
import sys
from collections import Counter
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
UNIDAD_DIR = CODE_DIR.parent                       # data/experiment/ev2_encadenamiento
EXP_DIR = UNIDAD_DIR.parent                        # data/experiment
REPO_DIR = EXP_DIR.parent.parent

CORRIDA_DIR = EXP_DIR / "ev2_corrida"
FIDELIDAD_EVAL_DIR = EXP_DIR / "ev2_fidelidad_eval"
JUEZ_DIR = EXP_DIR / "ev2_juez"

for _p in (CORRIDA_DIR / "code", FIDELIDAD_EVAL_DIR / "code"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import comun_ev2 as ce                 # noqa: E402  (corrida base del agente)
import comun_fidelidad as cf           # noqa: E402  (pipeline ciego del juez)
from comun_fidelidad import juez, mapping  # noqa: E402  (juez congelado)

# --------------------------------------------------------------------------- #
# Rutas de esta unidad                                                        #
# --------------------------------------------------------------------------- #
POBLACION_DIR = UNIDAD_DIR / "poblacion"
ORDEN_DIR = UNIDAD_DIR / "orden"
TRAZAS_DIR = UNIDAD_DIR / "trazas"
CACHE_DIR = UNIDAD_DIR / "cache"
JUEZ_OUT_DIR = UNIDAD_DIR / "juez_out"                       # salidas CIEGAS del juez
JUEZ_ORDEN_DIR = UNIDAD_DIR / "juez_orden"
DESANON_DIR = UNIDAD_DIR / "desanonimizacion_SOLO_MESA"      # tabla id opaco → par
ESTIMACION_DIR = UNIDAD_DIR / "estimacion"
REPORTE_DIR = UNIDAD_DIR / "reporte"
SELLOS_DIR = UNIDAD_DIR / "sellos"

# Insumos de la corrida base (solo lectura)
BASE_AGREGADOS = FIDELIDAD_EVAL_DIR / "out" / "veredictos_agregados_ciego.json"
BASE_TABLA = FIDELIDAD_EVAL_DIR / "desanonimizacion" / "tabla_id_opaco.json"
BASE_TRAZAS_DIR = CORRIDA_DIR / "trazas"

# Parámetros pre-declarados
GRAFOS = ce.GRAFO_KEYS                     # ["v2", "v3", "run_3"]
REPS_AGENTE = 3
REPS_JUEZ = 3
SEMILLA_AUDITORIA = "auditoria-ev2-v1"     # protocolo §3
FRACCION_AUDITORIA = 0.10
MINIMO_AUDITORIA_POR_GRAFO = 1             # laudo: ceil, mínimo 1 por grafo
LABEL_AGENTE = "ev2_enc_{grafo}_r{rep}"    # db propia por (grafo, rep)
LABEL_JUEZ = "ev2_enc_juez_r{rep}"         # db propia por rep del juez
DB_PREFIX_JUEZ = "ev2_enc_juez"            # cache/ev2_enc_juez_r{rep}.db
SAL_ID_OPACO = "juez-ev2-enc-v1"
PREFIJO_ID = "EV2E-"
SEMILLA_ORDEN_JUEZ = "juez-ev2-enc-v1"

ESPERADO_PARCIALES = {"v2": 23, "v3": 22, "run_3": 18}
ESPERADO_CORRECTOS = {"v2": 3, "v3": 4, "run_3": 2}
VEREDICTO_DISPARADOR = "parcial"


def label_agente(grafo: str, rep: int) -> str:
    return LABEL_AGENTE.format(grafo=grafo.replace("_", ""), rep=rep)


def label_juez(rep: int) -> str:
    return LABEL_JUEZ.format(rep=rep)


def rel_repo(p: Path) -> str:
    return str(Path(p).resolve().relative_to(REPO_DIR))


def sha256_path(p: Path) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def sha256_texto(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


# --------------------------------------------------------------------------- #
# Sellos: cuarteto + juez + grafos + insumos de la base                        #
# --------------------------------------------------------------------------- #
def verificar_sellos(verbose: bool = False) -> dict:
    """Instrumento congelado (prompt/juez/mapping + cuarteto, vía
    comun_fidelidad.verificar_sellos), tres grafos (vía comun_ev2.verificar_grafos)
    y sha de los insumos de la corrida base. Levanta si algo difiere."""
    s = cf.verificar_sellos()                     # prompt v1, juez.py, mapping.py, cuarteto, gold
    g = ce.verificar_grafos(verbose=verbose)      # 3/3 o levanta
    for k, v in g.items():
        s[f"grafo_{k}"] = v
    s["base_veredictos_agregados_ciego.json"] = sha256_path(BASE_AGREGADOS)
    s["base_tabla_id_opaco.json"] = sha256_path(BASE_TABLA)
    s["runner_ev2.py"] = sha256_path(CORRIDA_DIR / "code" / "runner_ev2.py")
    s["comun_ev2.py"] = sha256_path(CORRIDA_DIR / "code" / "comun_ev2.py")
    s["comun_fidelidad.py"] = sha256_path(FIDELIDAD_EVAL_DIR / "code" / "comun_fidelidad.py")
    s["pipeline_fidelidad.py"] = sha256_path(FIDELIDAD_EVAL_DIR / "code" / "pipeline_fidelidad.py")
    return s


def escribir_sellos(nombre: str) -> Path:
    SELLOS_DIR.mkdir(parents=True, exist_ok=True)
    s = verificar_sellos()
    p = SELLOS_DIR / nombre
    p.write_text("".join(f"{v}  {k}\n" for k, v in s.items()), encoding="utf-8")
    return p


# --------------------------------------------------------------------------- #
# Población disparada: 63 "parcial" + auditoría del 10 % de los "correcto"     #
# --------------------------------------------------------------------------- #
def cargar_base() -> tuple[dict, dict]:
    agg = json.loads(BASE_AGREGADOS.read_text(encoding="utf-8"))
    tab = json.loads(BASE_TABLA.read_text(encoding="utf-8"))
    if agg["n_casos"] != 120 or agg["n_agregados"] != 120 or agg["incompletas"]:
        raise ValueError("corrida base inesperada (esperaba 120 agregados, 0 incompletas)")
    if tab["n"] != 120:
        raise ValueError("tabla base inesperada")
    return agg, tab


def cruce_base(agg: dict, tab: dict) -> list[dict]:
    """Veredicto base por par (id_pregunta, grafo) — el cruce que la mesa hace
    con la tabla; esta unidad lo necesita porque debe re-correr el agente."""
    fila = {f["id_opaco"]: f for f in tab["filas"]}
    xs = []
    for a in agg["agregados"]:
        f = fila[a["id_opaco"]]
        xs.append({"id_pregunta": f["id_pregunta"], "grafo": f["grafo"],
                   "label_base": f["label"], "id_opaco_base": a["id_opaco"],
                   "sha256_respuesta_base": f["sha256_respuesta"],
                   "veredicto_base": a["veredicto_pregunta"],
                   "n_criterios": a["n_criterios"]})
    if len({(x["id_pregunta"], x["grafo"]) for x in xs}) != len(xs):
        raise ValueError("par (id_pregunta, grafo) repetido en la base")
    return sorted(xs, key=lambda x: (x["grafo"], x["id_pregunta"]))


def muestra_auditoria(correctos_por_grafo: dict[str, list[str]]) -> dict[str, list[str]]:
    """10 % de los ids 'correcto' de cada grafo, random.Random('auditoria-ev2-v1')
    sobre ids ORDENADOS (protocolo §3); tamaño = max(ceil(10 %·n), 1) (laudo).
    Un generador nuevo por grafo con la misma semilla: la muestra de un grafo no
    depende de la de otro (misma regla, independiente)."""
    out = {}
    for g in sorted(correctos_por_grafo):
        ids = sorted(correctos_por_grafo[g])
        if not ids:
            out[g] = []
            continue
        k = max(math.ceil(FRACCION_AUDITORIA * len(ids)), MINIMO_AUDITORIA_POR_GRAFO)
        out[g] = sorted(random.Random(SEMILLA_AUDITORIA).sample(ids, k))
    return out


def derivar_poblacion() -> dict:
    agg, tab = cargar_base()
    cruce = cruce_base(agg, tab)
    dist_base = {g: dict(Counter(x["veredicto_base"] for x in cruce if x["grafo"] == g))
                 for g in GRAFOS}
    parciales = [x for x in cruce if x["veredicto_base"] == VEREDICTO_DISPARADOR]
    correctos = {g: [x["id_pregunta"] for x in cruce if x["grafo"] == g and x["veredicto_base"] == "correcto"]
                 for g in GRAFOS}
    aud_ids = muestra_auditoria(correctos)
    por_par = {(x["id_pregunta"], x["grafo"]): x for x in cruce}
    auditoria = [por_par[(q, g)] for g in GRAFOS for q in aud_ids[g]]

    pares = []
    for x in parciales:
        pares.append({**x, "tipo": "parcial_disparado"})
    for x in auditoria:
        pares.append({**x, "tipo": "auditoria_correcto"})
    pares.sort(key=lambda p: (p["grafo"], p["id_pregunta"]))

    conteo_parciales = {g: sum(1 for p in parciales if p["grafo"] == g) for g in GRAFOS}
    conteo_correctos = {g: len(correctos[g]) for g in GRAFOS}
    conteo_aud = {g: len(aud_ids[g]) for g in GRAFOS}
    ok = conteo_parciales == ESPERADO_PARCIALES and conteo_correctos == ESPERADO_CORRECTOS
    if not ok:
        raise ValueError(f"conteos base fuera de lo esperado: parciales {conteo_parciales}, "
                         f"correctos {conteo_correctos}")
    return {
        "fuente_base": {"agregados": rel_repo(BASE_AGREGADOS), "tabla": rel_repo(BASE_TABLA),
                        "sha256_agregados": sha256_path(BASE_AGREGADOS),
                        "sha256_tabla": sha256_path(BASE_TABLA)},
        "regla": {"disparador": f"veredicto_base == '{VEREDICTO_DISPARADOR}' (protocolo §3, trigger único)",
                  "auditoria": (f"{int(FRACCION_AUDITORIA*100)} % de los 'correcto' por grafo, "
                                f"random.Random('{SEMILLA_AUDITORIA}').sample sobre ids ordenados, "
                                f"tamaño max(ceil, {MINIMO_AUDITORIA_POR_GRAFO}) (laudo)"),
                  "reps_agente": REPS_AGENTE, "reps_juez": REPS_JUEZ},
        "distribucion_base_por_grafo": dist_base,
        "conteo_parciales_por_grafo": conteo_parciales,
        "esperado_parciales_por_grafo": ESPERADO_PARCIALES,
        "conteo_correctos_por_grafo": conteo_correctos,
        "esperado_correctos_por_grafo": ESPERADO_CORRECTOS,
        "auditoria_por_grafo": {g: {"n_correctos": conteo_correctos[g], "n_muestra": conteo_aud[g],
                                    "ids_muestra": aud_ids[g], "ids_correctos_ordenados": sorted(correctos[g])}
                                for g in GRAFOS},
        "n_pares_parciales": len(parciales),
        "n_pares_auditoria": len(auditoria),
        "n_pares": len(pares),
        "n_corridas_agente": len(pares) * REPS_AGENTE,
        "n_llamadas_juez": len(pares) * REPS_AGENTE * REPS_JUEZ,
        "conteos_ok": ok,
        "pares": pares,
    }


def cargar_poblacion() -> dict:
    p = POBLACION_DIR / "poblacion_disparada.json"
    pob = json.loads(p.read_text(encoding="utf-8"))
    rec = derivar_poblacion()
    if rec["pares"] != pob["pares"]:
        raise RuntimeError("poblacion_disparada.json difiere de la derivación desde la base")
    return pob


# --------------------------------------------------------------------------- #
# Casos del agente por grafo, en el orden del protocolo §5                     #
# --------------------------------------------------------------------------- #
def casos_agente(pob: dict, grafo: str) -> list[dict]:
    """Casos de fidelidad del orden resuelto global (`orden-ev2-v1`, comun_ev2)
    filtrados a los pares disparados de este grafo: el orden relativo del
    protocolo se conserva (mismo patrón que las ausencias salteadas de la base)."""
    disparados = {p["id_pregunta"]: p for p in pob["pares"] if p["grafo"] == grafo}
    out = []
    for pos_global, c in enumerate(ce.orden_resuelto(), 1):
        if c["eje"] == "fidelidad" and c["caso_id"] in disparados:
            out.append({**c, "pos_orden_global": pos_global})
    if len(out) != len(disparados):
        raise ValueError(f"{grafo}: {len(out)} casos en orden vs {len(disparados)} pares")
    return out


# --------------------------------------------------------------------------- #
# Respuestas nuevas: carga desde trazas + ids opacos nuevos + vista ciega       #
# --------------------------------------------------------------------------- #
def id_opaco(id_pregunta: str, grafo: str, rep: int, sha_resp: str) -> str:
    return PREFIJO_ID + sha256_texto(f"{SAL_ID_OPACO}|{id_pregunta}|{grafo}|{rep}|{sha_resp}")[:10]


def cargar_respuestas_nuevas(pob: dict, trazas_dir: Path = TRAZAS_DIR,
                             reps: int = REPS_AGENTE) -> tuple[list[dict], list[dict]]:
    """Una entrada por (par, rep) leída de trazas/<label>/<id_pregunta>.json.
    Devuelve (respuestas, faltantes). Exige respuesta parseada no vacía; una
    traza sin respuesta parseada se lista en `faltantes` (incompleta, laudo)."""
    xs, faltantes = [], []
    for p in pob["pares"]:
        for rep in range(1, reps + 1):
            lab = label_agente(p["grafo"], rep)
            f = trazas_dir / lab / f"{p['id_pregunta']}.json"
            if not f.exists():
                faltantes.append({"id_pregunta": p["id_pregunta"], "grafo": p["grafo"], "rep": rep,
                                  "motivo": "traza inexistente"})
                continue
            t = json.loads(f.read_text(encoding="utf-8"))
            m, tr = t["meta"], t["trace"]
            fj = tr.get("final_json") or {}
            if m["label"] != lab or m["grafo"] != p["grafo"] or m["caso_id"] != p["id_pregunta"] \
                    or tr["qid"] != p["id_pregunta"]:
                raise ValueError(f"{f}: meta inconsistente")
            if not tr.get("parse_ok") or not isinstance(fj.get("respuesta"), str) \
                    or not fj["respuesta"].strip():
                faltantes.append({"id_pregunta": p["id_pregunta"], "grafo": p["grafo"], "rep": rep,
                                  "motivo": f"sin respuesta parseada (parse_ok={tr.get('parse_ok')}, "
                                            f"error={tr.get('error')})"})
                continue
            xs.append({"id_pregunta": p["id_pregunta"], "grafo": p["grafo"], "rep": rep,
                       "label": lab, "tipo": p["tipo"], "id_opaco_base": p["id_opaco_base"],
                       "veredicto_base": p["veredicto_base"],
                       "respuesta": fj["respuesta"], "respondible_flag": fj.get("respondible"),
                       "pregunta_traza": t["pregunta"]})
    return xs, faltantes


def armar_casos(respuestas: list[dict], gold: dict) -> list[dict]:
    """Casos COMPLETOS (con grafo/rep) en orden ciego pre-declarado:
    sorted por (id_pregunta, sha256 respuesta, grafo, rep) → shuffle con
    `juez-ev2-enc-v1`. Solo este módulo y la tabla SOLO_MESA ven grafo/rep."""
    xs = []
    for r in respuestas:
        if r["pregunta_traza"].strip() != gold[r["id_pregunta"]]["pregunta"].strip():
            raise ValueError(f"{r['id_pregunta']} r{r['rep']}: pregunta de traza ≠ gold")
        sha = sha256_texto(r["respuesta"])
        xs.append({**r, "sha256_respuesta": sha,
                   "id_opaco": id_opaco(r["id_pregunta"], r["grafo"], r["rep"], sha),
                   "pregunta": gold[r["id_pregunta"]]["pregunta"],
                   "criterios": gold[r["id_pregunta"]]["criterios"]})
    xs.sort(key=lambda c: (c["id_pregunta"], c["sha256_respuesta"], c["grafo"], c["rep"]))
    ids = [c["id_opaco"] for c in xs]
    if len(set(ids)) != len(ids):
        raise ValueError("colisión de ids opacos")
    # textos idénticos dentro de una misma pregunta (entre reps/grafos o con la base):
    # se reportan; con la rep en la clave no colisionan los ids
    dup = Counter((c["id_pregunta"], c["sha256_respuesta"]) for c in xs)
    duplicados = sorted([q, s, n] for (q, s), n in dup.items() if n > 1)
    random.Random(SEMILLA_ORDEN_JUEZ).shuffle(xs)
    for c in xs:
        c["duplicados_texto"] = duplicados
    return xs


def vista_ciega(casos: list[dict]) -> list[dict]:
    return cf.vista_ciega(casos)     # {id_opaco, pregunta, respuesta, criterios} y nada más


def tabla_desanonimizacion(casos: list[dict]) -> dict:
    return {"SOLO_MESA": True, "salt_id_opaco": SAL_ID_OPACO, "prefijo": PREFIJO_ID,
            "regla": "id_opaco = prefijo + sha256(salt|id_pregunta|grafo|rep|sha256(respuesta))[:10]",
            "n": len(casos),
            "filas": sorted(({"id_opaco": c["id_opaco"], "id_pregunta": c["id_pregunta"],
                              "grafo": c["grafo"], "rep": c["rep"], "label": c["label"],
                              "tipo": c["tipo"], "id_opaco_base": c["id_opaco_base"],
                              "veredicto_base": c["veredicto_base"],
                              "sha256_respuesta": c["sha256_respuesta"],
                              "respondible_flag": c["respondible_flag"],
                              "n_criterios": len(c["criterios"])} for c in casos),
                            key=lambda f: f["id_opaco"])}


def vinculo_pares_ciego(casos: list[dict]) -> dict:
    """Vínculo CIEGO id_opaco_base (par) → ids opacos nuevos por rep. No lleva
    grafo ni id de pregunta: solo relaciona ids opacos entre sí (necesario para
    agregar por par en el reporte ciego; el tipo revela el veredicto base, que
    ya es público en el reporte ciego de la base)."""
    por_par: dict[str, dict] = {}
    for c in casos:
        d = por_par.setdefault(c["id_opaco_base"], {"id_opaco_base": c["id_opaco_base"],
                                                    "tipo": c["tipo"], "reps": {}})
        d["reps"][str(c["rep"])] = c["id_opaco"]
    return {"n_pares": len(por_par),
            "pares": [por_par[k] for k in sorted(por_par)]}


def orden_ciego(casos: list[dict]) -> dict:
    return {"semilla": SEMILLA_ORDEN_JUEZ,
            "regla": "sorted por (id_pregunta, sha256 respuesta, grafo, rep) → random.Random(semilla).shuffle",
            "n": len(casos),
            "n_textos_duplicados_por_pregunta": len(casos[0]["duplicados_texto"]) if casos else 0,
            "ids_opacos_en_orden": [c["id_opaco"] for c in casos]}


def persistir_orden_y_tabla(casos: list[dict], orden_dir: Path = JUEZ_ORDEN_DIR,
                            desanon_dir: Path = DESANON_DIR) -> tuple[Path, Path, Path]:
    orden_dir.mkdir(parents=True, exist_ok=True)
    desanon_dir.mkdir(parents=True, exist_ok=True)
    p_ord = orden_dir / "orden_juez_encadenamiento_ciego.json"
    p_tab = desanon_dir / "tabla_id_opaco_encadenamiento_SOLO_MESA.json"
    p_vin = orden_dir / "vinculo_pares_ciego.json"
    for p, obj in ((p_ord, orden_ciego(casos)), (p_tab, tabla_desanonimizacion(casos)),
                   (p_vin, vinculo_pares_ciego(casos))):
        nuevo = json.dumps(obj, ensure_ascii=False, indent=2)
        if p.exists():
            if p.read_text(encoding="utf-8") != nuevo:
                raise RuntimeError(f"{p} ya existe y difiere de lo recomputado")
        else:
            p.write_text(nuevo, encoding="utf-8")
    return p_ord, p_tab, p_vin


# Marcadores que jamás pueden aparecer en un input del juez ni en una salida ciega.
MARCADORES = list(cf.MARCADORES_GRAFO) + ["ev2_enc_", "EV2F-", "\"id_pregunta\"",
                                          "veredicto_base", "parcial_disparado",
                                          "auditoria_correcto"]


def buscar_marcadores(texto: str, extra: list[str] = ()) -> list[str]:
    return [m for m in MARCADORES + list(extra) if m in texto]
