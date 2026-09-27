"""
runner_ev2_neo4j.py — Runner de EV2 (eje de fidelidad, firma v1 del harness)
sobre GraphAgentNeo4j en modo fulltext. Gate 4 de la fase 2 de B6.0: celdas
C2 y C4 del pre-registro de la tanda 0 (docs/preregistro_tanda0.md A3.1-A3.3
y A6; laudo docs/laudo_promocion_backend.md §3).

Módulo NUEVO que extiende en memoria el circuito sellado de EV2 al backend
Neo4j sin editar ningún módulo sellado (patrón ev2_r1/code/comun_r1.py).

QUÉ REUTILIZA POR IMPORT (solo import; sha verificados en SELLOS)
  - harness (cuarteto hasheado): GraphAgent.ask con su prompt del sistema,
    TOOLS v1 (buscar_nodos / ver_nodo / ver_vecinos), MODEL / TEMPERATURE /
    MAX_TOOL_CALLS (harness.py:47-50), truncado de outputs y colección de
    provenances vistas. Nada de eso se redefine acá.
  - llm_cache: CachingClient, make_namespace, code_version.
  - agente_neo4j.GraphAgentNeo4j + neo4j_index.Neo4jIndex (A1.1): el agente
    del harness con las tres tools resueltas contra Neo4j; constructor
    (indice, client, cache_conversation) (agente_neo4j.py:59-65).
  - grafos.GRAFOS / verificar_sha / rel_repo: registro de grafos con path,
    sha256 sellado, label Neo4j y nombre del índice full-text.
  - conexion.abrir_driver: driver de Neo4j (conexion.py:27-31).
  - comun_r1.casos_fidelidad_r1 / SEMILLA_ORDEN_R1: los 40 casos de fidelidad
    de EV2 en el orden sellado de C1 (semilla orden-ev2-r1), para que C2 sea
    comparable con C1 (pre-registro A3.3, par C1 vs C2).
  - runner_ev2._sanitizar y _real_client: nombre de archivo por caso y
    cliente real (este último solo en modo real, gateado).
  - run_posthoc._max_access_rowid / _turns_since: recuperación del crudo
    íntegro de cada llamada API desde el access_log de la caché.

QUÉ REPLICA, Y POR QUÉ NO PUEDE IMPORTARLO
  - FullCaptureAgentNeo4j replica _run_tool y ask_capturando de
    runner_ev2.FullCaptureAgent (runner_ev2.py:64-84) sin heredar de él:
    FullCaptureAgent hereda de GraphAgent y su __init__ arma un GraphIndex
    en memoria desde un KnowledgeGraph; GraphAgentNeo4j reemplaza ese índice
    por un Neo4jIndex. Heredar de las dos clases dejaría el MRO colgando de
    dos módulos sellados. Precedente: ablacion_retrieval/corrida/
    agente_celda.py:156-169.
  - La cadena de caché replica build_cache_client (runner_ev2.py:90-102) sin
    importarla: esa función exige un KnowledgeGraph con .path existente y
    calcula la huella leyendo el kg.json; GraphAgentNeo4j corre sobre un kg
    VACÍO (agente_neo4j.py:49-53). Acá la huella es el sha256 sellado del
    registro + "|neo4j:<modo>:<índice>" (decisión 5 del mandato), lo que
    garantiza que el namespace nunca colisiona con las dbs de C1.
  - correr_grafo replica la persistencia por caso de runner_ev2.correr_grafo
    (runner_ev2.py:126-228): esa función arma su propio FullCaptureAgent
    sobre cargar_runtime(grafo) y no admite inyectar el agente. La traza por
    caso tiene la MISMA estructura que las de C1 (meta, pregunta, trace,
    steps_full, raw_turns_agent; runner_ev2.py:157-183) más dos claves en
    meta: backend (GraphAgentNeo4j.backend) y model_segun_api (ids de modelo
    devueltos por la API, regla C1.9 del plan / A6 del pre-registro). Lo que
    leen el juez v1 (ev2_r1/code/juez_r1.py:61-83) y los indicadores de cita
    (scripts/ucita2_indicadores.py) — meta.caso_id, trace.final_json.
    respuesta, trace.parse_ok, trace.seen_provenances — no cambia de nombre
    ni de forma.

GATING DE GASTO (decisión 7; patrón runner_r1.py:17-23,99-100): el modo real
exige --autorizado-fase-b Y --tope <USD>; sin los dos, aborta (exit 2) sin
abrir Neo4j ni construir ningún cliente. Freno por proyección de correr_grafo
(protocolo §5, runner_ev2.py:197-211). Retoma: los casos con traza persistida
en outdir se saltean (precedente runner_r1.py:105-106).

Uso (modo real, solo con autorización explícita; primera corrida = celda C2):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B \
      data/experiment/ev2_tanda0/code/runner_ev2_neo4j.py \
      --grafo KG_Reextraido_r1 --modo fulltext --label <label> \
      [--casos RUTA] [--outdir RUTA] [--db RUTA] \
      --autorizado-fase-b --tope <USD>
  Salida por default: data/experiment/ev2_tanda0/trazas/<label>/<caso_id>.json
  y resumen_<label>.json; caché data/experiment/ev2_tanda0/cache/<label>.db.
  El selftest ($0, sin API) vive en selftest_runner_ev2_neo4j.py.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
TANDA0_DIR = CODE_DIR.parent                       # data/experiment/ev2_tanda0
EXP_DIR = TANDA0_DIR.parent                        # data/experiment
REPO_DIR = EXP_DIR.parent.parent
NEO4J_DIR = EXP_DIR / "neo4j"
EV2_R1_CODE_DIR = EXP_DIR / "ev2_r1" / "code"
EV2_CORRIDA_CODE_DIR = EXP_DIR / "ev2_corrida" / "code"
EVAL_DIR = EXP_DIR / "evaluacion"
RUNNERS_DIR = EVAL_DIR / "runners"

for _p in (NEO4J_DIR, EV2_R1_CODE_DIR, EV2_CORRIDA_CODE_DIR, EVAL_DIR, RUNNERS_DIR):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import comun_r1 as cr                      # noqa: E402  (registra r1 en memoria al importarse)
import runner_ev2 as rv                    # noqa: E402  (runner base, sin editar)
import harness                             # noqa: E402  (cuarteto: solo import)
import llm_cache as lc                     # noqa: E402
from agente_neo4j import GraphAgentNeo4j   # noqa: E402  (A1.1, sin editar)
from conexion import abrir_driver          # noqa: E402
from grafos import CLAVES, GRAFOS, rel_repo, verificar_sha  # noqa: E402
from neo4j_index import Neo4jIndex         # noqa: E402  (A1.1, sin editar)
from run_posthoc import _max_access_rowid, _turns_since  # noqa: E402

UNIDAD = "ev2_tanda0"
MODO_DEFAULT = "fulltext"                  # celdas C2 y C4 (pre-registro A3.1)
# Único modo admitido por la CLI: las celdas pre-registradas corren fulltext.
# El modo "paridad" de Neo4jIndex sería una celda NO pre-registrada y exige
# mandato propio; correr_grafo lo acepta solo por inyección programática.
MODOS_CLI = (MODO_DEFAULT,)
CACHE_DIR = TANDA0_DIR / "cache"
TRAZAS_DIR = TANDA0_DIR / "trazas"

# Sellados que este módulo importa (decisión 1). Se verifican antes de correr.
SELLOS = {
    EVAL_DIR / "harness.py":
        "fd267e833866f86850e43130e627b08d78e05523b97484696de0ab0c8c9fba9e",
    EV2_CORRIDA_CODE_DIR / "runner_ev2.py":
        "c4b067f914cb080574fe16ba087f806e95351b4338ed8463092ad3ffae5ca931",
    NEO4J_DIR / "agente_neo4j.py":
        "403a9b4295961f461c73a35b46ccc4d973a20cefdddf2ae97b50231dd7a3576a",
    NEO4J_DIR / "neo4j_index.py":
        "5f38db1b915caf8a4cd71e0f7f0d281ba5a9ca6867d327a9e0f4aac67cd2d0c1",
}


def sha256_path(p: Path) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def verificar_sellos(verbose: bool = False) -> dict:
    """sha256 de los cuatro módulos sellados que se importan. Levanta si alguno
    difiere del valor sellado en el mandato del gate 4."""
    out = {}
    for p, esperado in SELLOS.items():
        got = sha256_path(p)
        if got != esperado:
            raise RuntimeError(f"SELLO ROTO: {rel_repo(p)} sha256={got} != {esperado}")
        out[rel_repo(p)] = got
        if verbose:
            print(f"  sello OK  {got[:12]}…  {rel_repo(p)}")
    return out


# --------------------------------------------------------------------------- #
# Agente con captura COMPLETA sobre Neo4j (réplica de FullCaptureAgent)        #
# --------------------------------------------------------------------------- #
class FullCaptureAgentNeo4j(GraphAgentNeo4j):
    """GraphAgentNeo4j cuyo _run_tool registra el output ÍNTEGRO de cada tool
    call (réplica de runner_ev2.FullCaptureAgent:64-84, sin heredar de él).
    El loop del harness llama _run_tool una vez por tool call, en orden: la
    lista full_outputs queda 1:1 con trace.steps (mismo índice)."""

    def __init__(self, indice: Neo4jIndex, client=None, cache_conversation=True):
        super().__init__(indice, client=client, cache_conversation=cache_conversation)
        self.full_outputs: list = []

    def _run_tool(self, name: str, args: dict):
        result = super()._run_tool(name, args)
        s = json.dumps(result, ensure_ascii=False)
        self.full_outputs.append({"n": len(self.full_outputs) + 1,
                                  "tool": name, "input": args,
                                  "output": result, "output_chars": len(s)})
        return result

    def ask_capturando(self, qid: str, question: str):
        self.full_outputs = []
        tr = self.ask(qid, question)
        return tr, list(self.full_outputs)


# --------------------------------------------------------------------------- #
# Cadena de clientes (caché por corrida; namespace con grafo + modo + índice)  #
# --------------------------------------------------------------------------- #
def graph_fingerprint_neo4j(grafo: str, modo: str, indice_nombre: str) -> str:
    """Huella del grafo que consume el agente (decisión 5): sha256 sellado del
    kg.json (grafos.py) + backend, modo e índice full-text."""
    return f"{GRAFOS[grafo]['sha256']}|neo4j:{modo}:{indice_nombre}"


def build_cache_client_neo4j(real_client, *, grafo: str, modo: str,
                             indice_nombre: str, label: str, db_path: Path):
    cv = lc.code_version()
    gfp = graph_fingerprint_neo4j(grafo, modo, indice_nombre)
    cache = lc.CachingClient(
        real_client, domain="agent", db_path=db_path,
        namespace=lc.make_namespace("agent", code_ver=cv, graph_fp=gfp,
                                    thinking=False),
        thinking_enabled=False, run_label=label)
    return cache, cv, gfp


# --------------------------------------------------------------------------- #
# Casos (decisión 6)                                                          #
# --------------------------------------------------------------------------- #
def cargar_casos(ruta: Path | None) -> tuple[list[dict], dict]:
    """Default: los 40 casos de fidelidad en el orden sellado de C1
    (comun_r1.casos_fidelidad_r1, semilla orden-ev2-r1). Con --casos: JSON
    con una lista de {caso_id, eje, pregunta} (o {"casos": [...]}); el orden
    es el del archivo. Devuelve (casos, fuente) para meta/resumen."""
    if ruta is None:
        casos = cr.casos_fidelidad_r1()
        fuente = {"origen": "comun_r1.casos_fidelidad_r1 (orden sellado de C1)",
                  "semilla_orden": cr.SEMILLA_ORDEN_R1, "n": len(casos)}
        return casos, fuente
    ruta = Path(ruta)
    data = json.loads(ruta.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        data = data.get("casos")
    if not isinstance(data, list) or not data:
        raise ValueError(f"{ruta}: se esperaba una lista no vacía de casos")
    casos, vistos = [], set()
    for i, c in enumerate(data, 1):
        if not isinstance(c, dict) or not {"caso_id", "eje", "pregunta"} <= set(c):
            raise ValueError(f"{ruta}: caso {i} sin claves caso_id/eje/pregunta")
        if not all(isinstance(c[k], str) and c[k].strip() for k in ("caso_id", "eje", "pregunta")):
            raise ValueError(f"{ruta}: caso {i} con caso_id/eje/pregunta vacíos o no string")
        if c["caso_id"] in vistos:
            raise ValueError(f"{ruta}: caso_id repetido {c['caso_id']!r}")
        vistos.add(c["caso_id"])
        casos.append({"caso_id": c["caso_id"], "eje": c["eje"],
                      "pregunta": c["pregunta"], "pos_orden_global": i})
    fuente = {"origen": str(ruta), "sha256": sha256_path(ruta),
              "semilla_orden": None, "n": len(casos)}
    return casos, fuente


# --------------------------------------------------------------------------- #
# Corrida (N=1) con persistencia por caso — réplica de runner_ev2.correr_grafo #
# --------------------------------------------------------------------------- #
def correr_grafo(grafo: str, *, modo: str, label: str, client_real, indice: Neo4jIndex,
                 db_path: Path, outdir: Path, casos: list[dict], fuente_casos: dict,
                 estado_gasto: dict | None = None) -> dict:
    """Corre `casos` (N=1) con FullCaptureAgentNeo4j sobre `indice` y persiste
    una traza por caso (estructura de C1 + meta.backend + meta.model_segun_api).
    `client_real` e `indice` son inyectables (el selftest usa un cliente falso
    y un Neo4jIndex stub). `estado_gasto`: freno por proyección (runner_ev2)."""
    if grafo not in GRAFOS:
        raise KeyError(f"grafo desconocido: {grafo!r}; válidos: {CLAVES}")
    if indice.grafo != grafo or indice.modo != modo:
        raise ValueError(f"índice inconsistente: indice.grafo={indice.grafo!r} "
                         f"indice.modo={indice.modo!r} vs --grafo {grafo!r} --modo {modo!r}")
    kg_sha = verificar_sha(grafo)              # única lectura del kg.json (grafos.py)
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)

    cache, cv, gfp = build_cache_client_neo4j(
        client_real, grafo=grafo, modo=modo, indice_nombre=indice.indice,
        label=label, db_path=Path(db_path))
    agent = FullCaptureAgentNeo4j(indice, client=cache, cache_conversation=True)
    backend = agent.backend
    print(f"== EV2 tanda 0 · {grafo} ({label}) · backend {backend['backend']} "
          f"modo={backend['modo']} índice={backend['indice_fulltext']} — "
          f"{len(casos)} casos, N=1 ==", flush=True)

    resumenes, costo_acum, modelos_api = [], 0.0, set()
    for pos_ef, c in enumerate(casos, 1):
        a0 = _max_access_rowid(cache)
        t_ini = datetime.now().isoformat(timespec="seconds")
        tr, steps_full = agent.ask_capturando(c["caso_id"], c["pregunta"])
        t_fin = datetime.now().isoformat(timespec="seconds")
        hits, n_turnos, raw_turns = _turns_since(cache, a0, "agent")
        model_segun_api = sorted({(t.get("raw") or {}).get("model") for t in raw_turns}
                                 - {None})
        modelos_api.update(model_segun_api)

        payload = {
            "meta": {
                "unidad": UNIDAD, "label": label, "grafo": grafo,
                "kg_path": rel_repo(GRAFOS[grafo]["path"]),
                "kg_sha256": kg_sha,
                "eje": c["eje"], "caso_id": c["caso_id"],
                "sample_id": c.get("sample_id"),
                "variante": c.get("variante"),
                "estrato": c.get("estrato"),
                "pos_orden_global": c.get("pos_orden_global"),
                "pos_orden_efectivo": pos_ef,
                "semilla_orden": fuente_casos.get("semilla_orden"),
                "n_rep": 1,
                "model": harness.MODEL,
                "temperature": harness.TEMPERATURE,
                "max_tool_calls": harness.MAX_TOOL_CALLS,
                "thinking_enabled": False,
                "timestamp_inicio": t_ini, "timestamp_fin": t_fin,
                "code_version": cv, "graph_fingerprint": gfp,
                "cache_turnos": {"hits": hits, "total": n_turnos},
                "fidelidad_sin_evaluar": c["eje"] == "fidelidad",
                "backend": backend,
                "model_segun_api": model_segun_api,
            },
            "pregunta": c["pregunta"],
            "trace": vars(tr),
            "steps_full": steps_full,
            "raw_turns_agent": raw_turns,
        }
        out_path = outdir / f"{rv._sanitizar(c['caso_id'])}.json"
        with out_path.open("w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)

        costo_acum += tr.cost_usd
        resumenes.append({"caso_id": c["caso_id"], "eje": c["eje"],
                          "tools": tr.tool_calls_used, "parse_ok": tr.parse_ok,
                          "hit_tool_limit": tr.hit_tool_limit,
                          "error": tr.error, "costo_usd": tr.cost_usd,
                          "model_segun_api": model_segun_api})
        print(f"  [{pos_ef}/{len(casos)}] {c['caso_id']} tools={tr.tool_calls_used} "
              f"parse_ok={tr.parse_ok} hits={hits}/{n_turnos} "
              f"costo=${tr.cost_usd:.5f}"
              + (f" ERROR={tr.error}" if tr.error else ""), flush=True)

        # Freno por proyección (protocolo §5) — tope GLOBAL de la corrida.
        if estado_gasto is not None:
            estado_gasto["gastado"] += tr.cost_usd
            estado_gasto["corridos"] += 1
            if estado_gasto["corridos"] >= 3:
                proyeccion = (estado_gasto["gastado"] / estado_gasto["corridos"]
                              * estado_gasto["total"])
                if proyeccion > estado_gasto["tope_usd"]:
                    print(f"  FRENO POR PROYECCIÓN: gasto global "
                          f"${estado_gasto['gastado']:.4f} en "
                          f"{estado_gasto['corridos']} casos proyecta "
                          f"${proyeccion:.4f} > tope "
                          f"${estado_gasto['tope_usd']:.4f}. Corrida detenida.",
                          flush=True)
                    break

    resumen = {
        "unidad": UNIDAD, "grafo": grafo, "label": label, "modo": modo,
        "backend": backend, "db": str(db_path),
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "n_casos_corridos": len(resumenes),
        "n_casos_previstos": len(casos),
        "costo_usd": round(costo_acum, 6),
        "cache_stats": cache.stats(),
        "code_version": cv, "graph_fingerprint": gfp,
        "model_segun_api": sorted(modelos_api),
        "casos_fuente": fuente_casos,
        "casos": resumenes,
    }
    with (outdir / f"resumen_{label}.json").open("w", encoding="utf-8") as f:
        json.dump(resumen, f, ensure_ascii=False, indent=2)
    cache.close()
    print(f"  -> {len(resumenes)} trazas en {outdir} | costo ${costo_acum:.4f}",
          flush=True)
    return resumen


# --------------------------------------------------------------------------- #
# CLI (modo real, gateado)                                                     #
# --------------------------------------------------------------------------- #
def main() -> int:
    ap = argparse.ArgumentParser(
        description="EV2 (fidelidad, firma v1) sobre GraphAgentNeo4j — celdas C2/C4 de "
                    "la tanda 0. Modo real gateado: exige --autorizado-fase-b y --tope.")
    ap.add_argument("--grafo", required=True, choices=CLAVES,
                    help="clave del registro data/experiment/neo4j/grafos.py")
    ap.add_argument("--modo", default=MODO_DEFAULT, choices=MODOS_CLI,
                    help=f"modo de Neo4jIndex (único admitido: {MODO_DEFAULT}, pre-registro A3.1)")
    ap.add_argument("--label", required=True,
                    help="etiqueta de la corrida (trazas/<label>/, cache/<label>.db)")
    ap.add_argument("--casos", type=Path, default=None,
                    help="JSON alternativo [{caso_id, eje, pregunta}, ...]; default: los 40 "
                         "casos de fidelidad de EV2 en el orden sellado de C1")
    ap.add_argument("--outdir", type=Path, default=None,
                    help="directorio de trazas (default data/experiment/ev2_tanda0/trazas/<label>)")
    ap.add_argument("--db", type=Path, default=None,
                    help="db de caché (default data/experiment/ev2_tanda0/cache/<label>.db)")
    ap.add_argument("--autorizado-fase-b", action="store_true",
                    help="declara que la corrida real fue autorizada con tope")
    ap.add_argument("--tope", type=float, default=None, help="tope USD de ESTA corrida")
    args = ap.parse_args()

    if not args.autorizado_fase_b or args.tope is None:
        print("ABORTADO: el modo real exige --autorizado-fase-b y --tope <USD>. "
              "Nada se llamó (ni Neo4j ni API).")
        return 2

    sellos = verificar_sellos(verbose=True)
    print(f"  sha256 OK  {args.grafo}: {verificar_sha(args.grafo)}")
    casos, fuente = cargar_casos(args.casos)
    outdir = args.outdir or (TRAZAS_DIR / args.label)
    db_path = args.db or (CACHE_DIR / f"{args.label}.db")
    outdir.mkdir(parents=True, exist_ok=True)
    pend = [c for c in casos
            if not (outdir / f"{rv._sanitizar(c['caso_id'])}.json").exists()]
    print(f"== {UNIDAD} · {args.grafo} · modo {args.modo} · {len(casos)} casos, "
          f"{len(casos) - len(pend)} ya persistidos, {len(pend)} pendientes | "
          f"tope USD {args.tope} ==", flush=True)
    if not pend:
        print("Nada pendiente: no se abre Neo4j ni se construye cliente.")
        return 0

    driver = abrir_driver()
    try:
        indice = Neo4jIndex(driver, grafo=args.grafo, modo=args.modo)
        real = rv._real_client()
        estado = {"gastado": 0.0, "corridos": 0, "total": len(pend), "tope_usd": args.tope}
        correr_grafo(args.grafo, modo=args.modo, label=args.label, client_real=real,
                     indice=indice, db_path=db_path, outdir=outdir, casos=pend,
                     fuente_casos=fuente, estado_gasto=estado)
    finally:
        driver.close()
    if verificar_sellos() != sellos:
        raise RuntimeError("sellos cambiaron durante la corrida")
    frenado = estado["corridos"] < len(pend)
    print(f"corridos {estado['corridos']}/{len(pend)} pendientes | gasto "
          f"${estado['gastado']:.4f}" + (" | FRENADO POR PROYECCIÓN" if frenado else ""),
          flush=True)
    return 1 if frenado else 0


if __name__ == "__main__":
    raise SystemExit(main())
