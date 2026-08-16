"""
comun_fidelidad.py — Insumos, ids opacos, orden y vista CIEGA para la evaluación
de fidelidad de las 120 respuestas de EV2 con el juez calibrado.

Vinculantes: docs/preregistro_evaluacion_fidelidad_ev2.md (commit be8a84f) y el
juez congelado de data/experiment/ev2_juez/ (prompt_juez_v1.md sha256
fd446f8e61f4…, juez.py, mapping.py) — se IMPORTAN, jamás se editan.

Insumos (solo lectura):
  - gold sellado: data/experiment/exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json
    (commit 9c44516; 40 preguntas / 164 criterios con cita textual);
  - respuestas: trazas EV2F-* de data/experiment/ev2_corrida/trazas/
    ev2_base_{v2,v3,run3}/ (commit bb89a8e); viaja al juez ÚNICAMENTE el
    campo trace.final_json.respuesta.

Ceguera de grafo (§3): el caso que ve el juez es (pregunta, respuesta,
criterios). Cada respuesta recibe un id opaco = "EV2R-" + sha256("juez-ev2-v1|
id_pregunta|grafo|sha256(respuesta)")[:10]; la tabla id_opaco → (id_pregunta,
pregunta, grafo, label, sha256 respuesta) se persiste en desanonimizacion/, un
directorio distinto de out/ (donde viven las salidas ciegas del juez) y ajeno
a todo input del juez.

Orden (§3): lista de 120 ordenada por (id_pregunta, sha256 respuesta) y
`random.Random("juez-ev2-v1").shuffle`. Se persiste en orden/ como lista de
ids opacos (sin grafo).
"""

from __future__ import annotations

import hashlib
import json
import os
import random
import sys
from collections import Counter
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
UNIDAD_DIR = CODE_DIR.parent                      # data/experiment/ev2_fidelidad_eval
EXP_DIR = UNIDAD_DIR.parent                       # data/experiment
REPO_DIR = EXP_DIR.parent.parent
JUEZ_DIR = EXP_DIR / "ev2_juez"

# El juez congelado se importa desde su directorio; juez.py agrega evaluacion/
# (llm_cache sellado) al sys.path por su cuenta.
if str(JUEZ_DIR) not in sys.path:
    sys.path.insert(0, str(JUEZ_DIR))
import juez      # noqa: E402
import mapping   # noqa: E402

GOLD_PATH = EXP_DIR / "exploracion" / "ev2_fidelidad" / "preguntas_ev2_fidelidad.json"
TRAZAS_DIR = EXP_DIR / "ev2_corrida" / "trazas"
LABELS = ("ev2_base_v2", "ev2_base_v3", "ev2_base_run3")

ORDEN_DIR = UNIDAD_DIR / "orden"
DESANON_DIR = UNIDAD_DIR / "desanonimizacion"
OUT_DIR = UNIDAD_DIR / "out"
CACHE_DIR = UNIDAD_DIR / "cache"
CARGA_DIR = UNIDAD_DIR / "carga"

SEMILLA_ORDEN = "juez-ev2-v1"
SAL_ID_OPACO = "juez-ev2-v1"
PREFIJO_ID = "EV2R-"
REPS = 3
DB_PREFIX = "ev2_eval"           # cache/ev2_eval_r{rep}.db
RUN_LABEL_BASE = "ev2_eval"      # ev2_eval_r{rep}

# Sellos esperados del instrumento (pre-registro §5 y registro_calibracion §8).
PROMPT_SHA256_ESPERADO = "fd446f8e61f46033d7de9b862121c698b2c52dcc2696b7f10993f44e509f5455"
GOLD_N_PREGUNTAS = 40
GOLD_N_CRITERIOS = 164
N_RESPUESTAS = 120

# Sellos del cuarteto y de las piezas del juez, verificados al inicio y al fin.
CUARTETO = {
    "loader.py":    "5aba8b7a0aa46e8d5c4c83b33884b8cae7d0a099884a7d3bc935de4d3097af8b",
    "harness.py":   "fd267e833866f86850e43130e627b08d78e05523b97484696de0ab0c8c9fba9e",
    "judge.py":     "7169145aaeb3f2d90a7e3873964378aa6520c5688fed136cf5a79ea63b589eaa",
    "llm_cache.py": "fc86b0e48df464d01d87aa1d8067168d2d522f66ead53f594092a16484c22752",
}


def sha256_path(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def sha256_texto(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def verificar_sellos() -> dict:
    """Instrumento congelado + cuarteto intocable. Levanta si algo difiere."""
    if os.environ.get("JUEZ_PROMPT_VERSION", "v1") != "v1" or juez.PROMPT_VERSION != "v1":
        raise RuntimeError("JUEZ_PROMPT_VERSION distinto de v1: prohibido en esta unidad")
    if juez.PROMPT_SHA256 != PROMPT_SHA256_ESPERADO:
        raise RuntimeError(f"prompt del juez alterado: {juez.PROMPT_SHA256}")
    sellos = {"prompt_juez_v1.md": juez.PROMPT_SHA256,
              "juez.py": sha256_path(JUEZ_DIR / "juez.py"),
              "mapping.py": sha256_path(JUEZ_DIR / "mapping.py")}
    for f, esperado in CUARTETO.items():
        real = sha256_path(EXP_DIR / "evaluacion" / f)
        if real != esperado:
            raise RuntimeError(f"cuarteto alterado: {f} {real}")
        sellos[f] = real
    sellos["gold"] = sha256_path(GOLD_PATH)
    return sellos


# --------------------------------------------------------------------------- #
# Gold                                                                        #
# --------------------------------------------------------------------------- #
def cargar_gold() -> dict[str, dict]:
    """{id_pregunta: {"pregunta", "criterios": [{"criterio","cita_textual"}], "to"}}
    Al juez viajan solo criterio + cita_textual, en el orden del archivo."""
    data = json.loads(GOLD_PATH.read_text(encoding="utf-8"))
    out = {}
    for p in data["preguntas"]:
        crits = [{"criterio": c["criterio"], "cita_textual": c["cita_textual"]}
                 for c in p["gold"]["criterios"]]
        for j, c in enumerate(crits, start=1):
            if not c["criterio"].strip() or not c["cita_textual"].strip():
                raise ValueError(f"{p['id']} criterio {j}: criterio o cita vacíos")
        if p["id"] in out:
            raise ValueError(f"id duplicado en gold: {p['id']}")
        out[p["id"]] = {"pregunta": p["pregunta"], "criterios": crits, "to": p["to"]}
    n_crit = sum(len(v["criterios"]) for v in out.values())
    if len(out) != GOLD_N_PREGUNTAS or n_crit != GOLD_N_CRITERIOS:
        raise ValueError(f"gold inesperado: {len(out)} preguntas / {n_crit} criterios")
    return out


# --------------------------------------------------------------------------- #
# Respuestas (120 trazas)                                                     #
# --------------------------------------------------------------------------- #
def cargar_respuestas(trazas_dir: Path = TRAZAS_DIR, labels=LABELS) -> list[dict]:
    """Una entrada por traza EV2F-*: {id_pregunta, grafo, label, respuesta,
    respondible_flag, pregunta_traza}. Exige respuesta parseada no vacía."""
    xs = []
    for label in labels:
        for f in sorted((trazas_dir / label).glob("EV2F-*.json")):
            t = json.loads(f.read_text(encoding="utf-8"))
            m, tr = t["meta"], t["trace"]
            fj = tr.get("final_json") or {}
            if m["eje"] != "fidelidad" or m["label"] != label:
                raise ValueError(f"{f}: meta inesperada {m['eje']}/{m['label']}")
            if m["caso_id"] != tr["qid"] or m["caso_id"] != f.stem:
                raise ValueError(f"{f}: caso_id/qid/nombre inconsistentes")
            if not tr.get("parse_ok") or not isinstance(fj.get("respuesta"), str) \
                    or not fj["respuesta"].strip():
                raise ValueError(f"{f}: traza sin respuesta parseada")
            xs.append({"id_pregunta": m["caso_id"], "grafo": m["grafo"], "label": label,
                       "respuesta": fj["respuesta"],
                       "respondible_flag": fj.get("respondible"),
                       "pregunta_traza": t["pregunta"]})
    return xs


def censo_carga(respuestas: list[dict], gold: dict) -> dict:
    """Conteos de la carga (fase A.a). Levanta si no son 120 / 40×3 / 3 por pregunta."""
    por_grafo = Counter(r["grafo"] for r in respuestas)
    por_label = Counter(r["label"] for r in respuestas)
    por_preg = Counter(r["id_pregunta"] for r in respuestas)
    faltan = sorted(set(gold) - set(por_preg))
    sobran = sorted(set(por_preg) - set(gold))
    preg_distinta = [r["id_pregunta"] for r in respuestas
                     if r["pregunta_traza"].strip() != gold[r["id_pregunta"]]["pregunta"].strip()]
    ok = (len(respuestas) == N_RESPUESTAS and all(v == 40 for v in por_grafo.values())
          and len(por_grafo) == 3 and all(v == 3 for v in por_preg.values())
          and not faltan and not sobran and not preg_distinta)
    c = {"n_respuestas": len(respuestas), "por_grafo": dict(sorted(por_grafo.items())),
         "por_label": dict(sorted(por_label.items())),
         "preguntas_distintas": len(por_preg),
         "respuestas_por_pregunta": dict(Counter(por_preg.values())),
         "preguntas_gold_sin_respuesta": faltan, "respuestas_sin_pregunta_gold": sobran,
         "pregunta_traza_distinta_del_gold": preg_distinta,
         "n_criterios_gold": sum(len(g["criterios"]) for g in gold.values()),
         "respondible_flag": dict(Counter(str(r["respondible_flag"]) for r in respuestas)),
         "chars_respuesta": {"min": min(len(r["respuesta"]) for r in respuestas),
                             "max": max(len(r["respuesta"]) for r in respuestas),
                             "total": sum(len(r["respuesta"]) for r in respuestas)},
         "ok": ok}
    if not ok:
        raise ValueError(f"censo de carga fuera de lo esperado: {c}")
    return c


# --------------------------------------------------------------------------- #
# Ids opacos, orden y tabla de des-anonimización                              #
# --------------------------------------------------------------------------- #
def id_opaco(id_pregunta: str, grafo: str, sha_resp: str) -> str:
    return PREFIJO_ID + sha256_texto(f"{SAL_ID_OPACO}|{id_pregunta}|{grafo}|{sha_resp}")[:10]


def armar_casos(respuestas: list[dict], gold: dict) -> list[dict]:
    """Casos COMPLETOS (con grafo) en el orden §3. Solo comun_fidelidad y la
    tabla de des-anonimización ven el grafo; el pipeline trabaja con la vista
    ciega de `vista_ciega`."""
    xs = []
    for r in respuestas:
        sha = sha256_texto(r["respuesta"])
        xs.append({"id_pregunta": r["id_pregunta"], "grafo": r["grafo"], "label": r["label"],
                   "sha256_respuesta": sha,
                   "id_opaco": id_opaco(r["id_pregunta"], r["grafo"], sha),
                   "pregunta": gold[r["id_pregunta"]]["pregunta"],
                   "respuesta": r["respuesta"],
                   "respondible_flag": r["respondible_flag"],
                   "criterios": gold[r["id_pregunta"]]["criterios"]})
    # clave pre-registrada (id_pregunta, sha256 respuesta); grafo solo desempata
    # respuestas idénticas de la misma pregunta (se reporta si ocurre)
    xs.sort(key=lambda c: (c["id_pregunta"], c["sha256_respuesta"], c["grafo"]))
    empates = [(a["id_pregunta"], a["sha256_respuesta"]) for a, b in zip(xs, xs[1:])
               if (a["id_pregunta"], a["sha256_respuesta"]) == (b["id_pregunta"], b["sha256_respuesta"])]
    ids = [c["id_opaco"] for c in xs]
    if len(set(ids)) != len(ids):
        raise ValueError("colisión de ids opacos")
    random.Random(SEMILLA_ORDEN).shuffle(xs)
    for c in xs:
        c["empates_clave_orden"] = empates
    return xs


def vista_ciega(casos: list[dict]) -> list[dict]:
    """Lo único que el pipeline del juez recibe: id opaco + input del juez.
    Sin id_pregunta, grafo, label, sha ni flag."""
    return [{"id_opaco": c["id_opaco"], "pregunta": c["pregunta"],
             "respuesta": c["respuesta"], "criterios": c["criterios"]} for c in casos]


def tabla_desanonimizacion(casos: list[dict]) -> dict:
    return {"salt_id_opaco": SAL_ID_OPACO, "prefijo": PREFIJO_ID,
            "regla": "id_opaco = prefijo + sha256(salt|id_pregunta|grafo|sha256(respuesta))[:10]",
            "n": len(casos),
            "filas": sorted(({"id_opaco": c["id_opaco"], "id_pregunta": c["id_pregunta"],
                              "grafo": c["grafo"], "label": c["label"],
                              "sha256_respuesta": c["sha256_respuesta"],
                              "respondible_flag": c["respondible_flag"],
                              "n_criterios": len(c["criterios"])} for c in casos),
                            key=lambda f: f["id_opaco"])}


def orden_ciego(casos: list[dict]) -> dict:
    return {"semilla": SEMILLA_ORDEN,
            "regla": "sorted por (id_pregunta, sha256 respuesta) → random.Random(semilla).shuffle",
            "n": len(casos),
            "empates_clave_orden": casos[0]["empates_clave_orden"] if casos else [],
            "ids_opacos_en_orden": [c["id_opaco"] for c in casos]}


def persistir_orden_y_tabla(casos: list[dict], orden_dir: Path = ORDEN_DIR,
                            desanon_dir: Path = DESANON_DIR) -> tuple[Path, Path]:
    """Escribe (o verifica, si ya existen) el orden ciego y la tabla. Si existen
    y difieren, levanta: el orden y los ids son únicos y sellados por sesión."""
    orden_dir.mkdir(parents=True, exist_ok=True)
    desanon_dir.mkdir(parents=True, exist_ok=True)
    p_ord = orden_dir / "orden_ev2_fidelidad_ciego.json"
    p_tab = desanon_dir / "tabla_id_opaco.json"
    nuevo_ord = json.dumps(orden_ciego(casos), ensure_ascii=False, indent=2)
    nuevo_tab = json.dumps(tabla_desanonimizacion(casos), ensure_ascii=False, indent=2)
    for p, nuevo in ((p_ord, nuevo_ord), (p_tab, nuevo_tab)):
        if p.exists():
            if p.read_text(encoding="utf-8") != nuevo:
                raise RuntimeError(f"{p} ya existe y difiere de lo recomputado")
        else:
            p.write_text(nuevo, encoding="utf-8")
    return p_ord, p_tab


def cargar_todo() -> tuple[dict, list[dict], dict, list[dict]]:
    """gold, respuestas, censo, casos (orden §3, con grafo)."""
    gold = cargar_gold()
    respuestas = cargar_respuestas()
    censo = censo_carga(respuestas, gold)
    casos = armar_casos(respuestas, gold)
    return gold, respuestas, censo, casos


# Marcadores de identidad de grafo que JAMÁS pueden aparecer en un input del
# juez ni en una salida ciega (valores reales de meta de las trazas + labels).
MARCADORES_GRAFO = ["ev2_base_v2", "ev2_base_v3", "ev2_base_run3", "reensamblado_v3",
                    "grafo_v2", "run_3_ppf_core", "kg_path", "kg_sha256",
                    "graph_fingerprint", "\"grafo\"", "'grafo'", "26fac8b49f6c08c1",
                    "run3", "\"label\""]


def buscar_marcadores(texto: str, extra: list[str] = ()) -> list[str]:
    return [m for m in list(MARCADORES_GRAFO) + list(extra) if m in texto]
