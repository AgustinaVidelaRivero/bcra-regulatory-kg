#!/usr/bin/env python3
"""comun_a2_2.py — Lo común de A2.2 (pre-registro FIRMADO `docs/preregistro_A2_2_sistema_por_fragmentos.md`, a78ead7b): rutas,
brazos, semillas, topes, la carga de EV2 por código y el control de las entradas.

- Los brazos (§2): el grafo de desarrollo re-sellado (`kg`) y las dos configuraciones de fragmentos (`fragmentos_bm25` y
  `fragmentos_denso`), con la configuración de los agentes de A2.2 (a2_2/config_agentes_a2_2.json).
- EV2 (§4) se lee solo por código: este módulo no imprime ninguna pregunta, ningún criterio ni ningún ancla. En la corrida real la
  ruta y el sha256 son los del pre-registro; la corrida en seco pasa un archivo sintético con el mismo esquema.
- Las semillas (§4, A-D7): A22:orden_corridas:v1, A22:auditoria:v1 y A22:orden_juez:v1.
- Los topes (§6, A-D2): el agente, 93 con freno en 69,75, con el presupuesto de 1,80 por sesión; el juez, 25 con freno en 18,75,
  con 0,0378 por respuesta mientras no haya ninguna juzgada.
- Las entradas que A2.2 usa sin editar, con su sha256 de HEAD, en a2_2/sellos_entrada_a2_2.json: `verificar_entradas` frena si
  alguna cambió.
"""
from __future__ import annotations

import hashlib
import json
import random
from pathlib import Path

AQUI = Path(__file__).resolve().parent                    # data/experiment/banco_mcp/a2_2
BANCO_DIR = AQUI.parent
EXP_DIR = BANCO_DIR.parent
REPO_DIR = BANCO_DIR.parents[2]

CONFIG_A22 = AQUI / "config_agentes_a2_2.json"
SELLOS_ENTRADA = AQUI / "sellos_entrada_a2_2.json"
ORDEN = AQUI / "orden_corridas_a2_2.json"
RESULTADOS = AQUI / "resultados"
OUT_PRUEBAS, OUT_N1, OUT_RECORRIDAS = RESULTADOS / "pruebas", RESULTADOS / "n1", RESULTADOS / "recorridas"
JUEZ_DIR = AQUI / "juez"
POBLACION = AQUI / "poblacion" / "poblacion_a2_2.json"

BRAZOS = ("fragmentos_bm25", "fragmentos_denso", "kg")   # los nombres ordenados (§4: «los nombres de los brazos ordenados»)
BRAZO_GRAFO = "kg"
FRAGMENTOS = ("fragmentos_bm25", "fragmentos_denso")

EV2_PATH = EXP_DIR / "exploracion" / "ev2_fidelidad" / "preguntas_ev2_fidelidad.json"
EV2_SHA256 = "1d58733699c325c90510e1ead5f18eac6c3cd970ee3b0ab7ff141da539162b40"
EV2_N_PREGUNTAS, EV2_N_CRITERIOS = 40, 164
COLA = EXP_DIR / "controles_a2_2" / "cola_grafo_desarrollo_r2b_rs1_mesa.json"
E0_DIR = EXP_DIR / "reextraccion_v2" / "e0_chunking" / "salida_tanda0_r2b"
E0_TOS = ("cap", "cla", "ext", "pro", "ric")
PREGUNTA_PRUEBA = ("SMK-01", BANCO_DIR / "smoke" / "preguntas_smoke.json")   # A-D5: una de prueba por brazo, sin pregunta de EV2

SEMILLA_ORDEN = "A22:orden_corridas:v1"
SEMILLA_AUDITORIA = "A22:auditoria:v1"
SEMILLA_ORDEN_JUEZ = "A22:orden_juez:v1"
REPETICIONES = (1, 2, 3, 4)          # 1, la de N = 1; 2, 3 y 4, las tres re-corridas (§4: tres sesiones nuevas; la base no vota)
REPS_RECORRIDA = (2, 3, 4)
REPS_JUEZ = (1, 2, 3)
FRACCION_AUDITORIA, MINIMO_AUDITORIA = 0.10, 1                  # max(ceil(10 % · n), 1) por brazo (§4, A-D10)

TOPE_AGENTE, FRENO_AGENTE, PRESUPUESTO_SESION = 93.0, 69.75, 1.80
TOPE_JUEZ, FRENO_JUEZ, COSTO_RESPUESTA_INICIAL = 25.0, 18.75, 0.0378
# Precios del juez (claude-sonnet-4-6), USD por millón de tokens: 3,00 de entrada y 15,00 de salida
# (`data/experiment/run_1_cookbook/code/common.py:207`; el costo por llamada de U-NAV, `:243`, es 0,0126).
PRECIO_JUEZ_IN, PRECIO_JUEZ_OUT = 3.00, 15.00


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def sha256_texto(s: str) -> str:
    return sha256_bytes(s.encode("utf-8"))


def rel_repo(p) -> str:
    try:
        return str(Path(p).resolve().relative_to(REPO_DIR))
    except ValueError:
        return str(p).replace(str(Path.home()), "$HOME")


class FrenoA22(Exception):
    """Un control de A2.2 no se cumple: se frena sin seguir."""


# --------------------------------------------------------------------------- #
# Entradas usadas sin editar                                                   #
# --------------------------------------------------------------------------- #
def verificar_entradas(repo: Path = REPO_DIR) -> dict:
    """Cada entrada de sellos_entrada_a2_2.json con el sha256 de HEAD. Frena con la lista de las que no dan."""
    d = json.loads(SELLOS_ENTRADA.read_text(encoding="utf-8"))
    mal = []
    for ruta, esperado in d["entradas"].items():
        p = repo / ruta
        if not p.is_file():
            mal.append(f"{ruta}: no existe")
        elif sha256_file(p) != esperado:
            mal.append(f"{ruta}: sha256 distinto")
    if mal:
        raise FrenoA22("entradas cambiadas: " + "; ".join(mal))
    return {"n_entradas": len(d["entradas"]), "todas_dan": True}


# --------------------------------------------------------------------------- #
# EV2 por código                                                               #
# --------------------------------------------------------------------------- #
def cargar_preguntas(ruta: Path = EV2_PATH, sha_esperado: str = EV2_SHA256, real: bool = True) -> dict:
    """{id: {"pregunta", "criterios": [{"criterio", "cita_textual"}], "anclas": [...], "to"}}, en el orden del archivo para
    los criterios (el que viaja al juez, como `ev2_fidelidad_eval/code/comun_fidelidad.py`, `cargar_gold`). En la corrida
    real frena si la ruta, el sha256, las 40 preguntas o los 164 criterios no son los del pre-registro. No imprime nada."""
    ruta = Path(ruta)
    sha = sha256_file(ruta)
    if sha != sha_esperado:
        raise FrenoA22("el archivo de preguntas no tiene el sha256 esperado")
    if real and (ruta.resolve() != EV2_PATH.resolve() or sha != EV2_SHA256):
        raise FrenoA22("la corrida real usa solo el archivo de EV2 del pre-registro")
    data = json.loads(ruta.read_text(encoding="utf-8"))
    out = {}
    for p in data["preguntas"]:
        crits = [{"criterio": c["criterio"], "cita_textual": c["cita_textual"]} for c in p["gold"]["criterios"]]
        if not crits or any(not c["criterio"].strip() or not c["cita_textual"].strip() for c in crits):
            raise FrenoA22("una pregunta sin criterios, o un criterio o una cita vacíos")
        if p["id"] in out:
            raise FrenoA22("id repetido en el archivo de preguntas")
        out[p["id"]] = {"pregunta": p["pregunta"], "criterios": crits, "anclas": list(p["gold"]["ancla"] or []),
                        "to": p["to"]}
    n_crit = sum(len(v["criterios"]) for v in out.values())
    if real and (len(out) != EV2_N_PREGUNTAS or n_crit != EV2_N_CRITERIOS):
        raise FrenoA22("EV2 no trae las 40 preguntas y los 164 criterios del pre-registro")
    return out


def pregunta_de_prueba() -> tuple[str, str]:
    """(id, texto) de la pregunta del smoke del tramo 2 de A2.1 con que corren las tres sesiones de prueba (A-D5)."""
    qid, ruta = PREGUNTA_PRUEBA
    d = json.loads(ruta.read_text(encoding="utf-8"))
    q = next(x for x in d["preguntas"] if x["id"] == qid)
    return qid, q["pregunta"]


# --------------------------------------------------------------------------- #
# Orden de las corridas (§4, A-D1 y A-D7)                                      #
# --------------------------------------------------------------------------- #
def orden_preguntas(ids: list[str], semilla: str = SEMILLA_ORDEN) -> list[str]:
    """`random.Random("A22:orden_corridas:v1").shuffle` sobre los ids ordenados."""
    xs = sorted(ids)
    random.Random(semilla).shuffle(xs)
    return xs


def orden_brazos(qid: str, rep: int, semilla: str = SEMILLA_ORDEN) -> list[str]:
    """`random.Random(f"A22:orden_corridas:v1:{id}:r{r}").shuffle` sobre los nombres de los brazos ordenados."""
    xs = sorted(BRAZOS)
    random.Random(f"{semilla}:{qid}:r{rep}").shuffle(xs)
    return xs


def armar_orden(ids: list[str]) -> dict:
    """El orden de A2.2, sin ningún texto: las preguntas en su orden y, por pregunta y por repetición, los brazos en su orden.
    Las re-corridas (r2 a r4) toman de cada pregunta solo los brazos que van a N = 3, en ese orden relativo."""
    preg = orden_preguntas(ids)
    return {"que": "el orden de las corridas de A2.2 (pre-registro, §4), escrito antes de correr; solo ids y nombres de brazos",
            "semilla": SEMILLA_ORDEN,
            "regla_preguntas": f"random.Random('{SEMILLA_ORDEN}').shuffle sobre los ids ordenados",
            "regla_brazos": f"random.Random(f'{SEMILLA_ORDEN}:{{id}}:r{{r}}').shuffle sobre los nombres de los brazos ordenados",
            "repeticiones": {"r1": "N = 1", "r2": "re-corrida 1", "r3": "re-corrida 2", "r4": "re-corrida 3"},
            "regla_recorridas": ("después de juzgar N = 1, por repetición (r2, r3, r4) y, dentro de cada una, en el orden de las "
                                 "preguntas de N = 1, con los brazos de esa pregunta que van a N = 3 seguidos, en el orden de su "
                                 "repetición"),
            "pruebas": {"pregunta": PREGUNTA_PRUEBA[0], "brazos": sorted(BRAZOS),
                        "regla": "una por brazo, en el orden de los nombres, antes de la primera de EV2 (A-D5)"},
            "n_preguntas": len(preg), "brazos": sorted(BRAZOS), "preguntas_en_orden": preg,
            "brazos_por_pregunta": {q: {f"r{r}": orden_brazos(q, r) for r in REPETICIONES} for q in preg},
            "sha256_ids_ordenados": sha256_texto("".join(x + "\n" for x in sorted(ids)))}


def id_sesion(etapa: str, qid: str, brazo: str, rep: int = 1) -> str:
    if etapa == "pruebas":
        return f"PRB-{brazo}"
    if etapa == "n1":
        return f"N1-{qid}-{brazo}"
    return f"RC{rep - 1}-{qid}-{brazo}"


def secuencia(orden: dict, etapa: str, poblacion: dict | None = None) -> list[dict]:
    """Las sesiones de una etapa, en su orden: [{id, qid, brazo, rep}]. Para las re-corridas, la población de N = 3."""
    if etapa == "pruebas":
        return [{"id": id_sesion("pruebas", None, b), "qid": orden["pruebas"]["pregunta"], "brazo": b, "rep": 0}
                for b in orden["pruebas"]["brazos"]]
    if etapa == "n1":
        return [{"id": id_sesion("n1", q, b), "qid": q, "brazo": b, "rep": 1}
                for q in orden["preguntas_en_orden"] for b in orden["brazos_por_pregunta"][q]["r1"]]
    van = {(p["qid"], p["brazo"]) for p in (poblacion or {}).get("pares", [])}
    out = []
    for r in REPS_RECORRIDA:
        for q in orden["preguntas_en_orden"]:
            for b in orden["brazos_por_pregunta"][q][f"r{r}"]:
                if (q, b) in van:
                    out.append({"id": id_sesion("recorridas", q, b, r), "qid": q, "brazo": b, "rep": r})
    return out
