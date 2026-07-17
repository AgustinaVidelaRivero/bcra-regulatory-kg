"""main.py — App local mínima sobre los grafos del repo (U1 + U2).

U1: descubrimiento de grafos al iniciar (glob de data/experiment/*/kg.json)
y endpoint GET /runs. U2: POST /chat envolviendo al GraphAgent del harness.
U3: registro append-only de turnos y feedback en app/sessions/<fecha>.jsonl
(POST /feedback). Toda carga de grafos pasa por load_graph_from_path() del
loader de la Fase 2.3; acá no se parsea ningún kg.json a mano.

Arranque, desde la raíz del repo (requiere ANTHROPIC_API_KEY en el entorno
para /chat; la app no lee ningún .env):
    uvicorn app.main:app --port 8000
"""

import json
import os
import sys
import threading
import uuid
from datetime import datetime
from pathlib import Path
from typing import Literal, Optional

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel

REPO_ROOT = Path(__file__).resolve().parent.parent
EXPERIMENT_DIR = REPO_ROOT / "data" / "experiment"
EVALUACION_DIR = EXPERIMENT_DIR / "evaluacion"

# El loader y el harness viven fuera de un package; se importan por sys.path.
sys.path.insert(0, str(EVALUACION_DIR))
from loader import load_graph_from_path  # noqa: E402
from harness import GraphAgent  # noqa: E402

# Al agregar un grafo nuevo con provenance múltiple, registrar acá su adapter_key.
ADAPTER_KEYS = {
    "run_1_cookbook": "run_1",
    "run_2_papers": "run_2",
    "run_3_ppf_core": "run_3",
    "run_4_schema_light": "run_4",
    "run_5_hybrid": "run_5",
}


def _discover_runs() -> list:
    """Un objeto {id, ruta, nodos, aristas} por directorio con kg.json; si un
    grafo no carga, el run entra como {id, ruta, error} sin romper el arranque."""
    runs = []
    for kg_path in sorted(EXPERIMENT_DIR.glob("*/kg.json")):
        run_id = kg_path.parent.name
        ruta = str(kg_path.relative_to(REPO_ROOT))
        try:
            kg = load_graph_from_path(kg_path, adapter_key=ADAPTER_KEYS.get(run_id))
            runs.append({"id": run_id, "ruta": ruta,
                         "nodos": len(kg.nodes), "aristas": len(kg.edges)})
        except Exception as e:
            runs.append({"id": run_id, "ruta": ruta,
                         "error": f"{type(e).__name__}: {e}"})
    return runs


class _ChatAgent(GraphAgent):
    """GraphAgent que además registra cada tool call con su resultado COMPLETO
    (tr.steps del harness trunca el output a 1200 chars; para los resúmenes de
    /chat hace falta el dict entero)."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tool_log = []  # [(tool, argumentos, resultado_completo), ...]

    def _run_tool(self, name: str, args: dict):
        result = super()._run_tool(name, args)
        self.tool_log.append((name, args, result))
        return result


def _resumen_tool(name: str, result) -> str:
    """Versión corta del resultado de una tool para tools_llamadas."""
    if not isinstance(result, dict):
        return "resultado no resumible"
    if result.get("error"):
        return f"error: {result['error']}"
    if name == "buscar_nodos":
        rs = result.get("resultados", [])
        ids = ", ".join(r.get("id", "?") for r in rs[:3])
        base = f"{result.get('total_con_match', 0)} nodos con match; devueltos {len(rs)}"
        return f"{base} (primeros: {ids})" if ids else base
    if name == "ver_nodo":
        return (f"{result.get('id')} — {result.get('label')} "
                f"({len(result.get('properties') or {})} properties, "
                f"{len(result.get('provenances') or [])} provenances)")
    if name == "ver_vecinos":
        return (f"{result.get('id')} — {result.get('n_salientes_total', 0)} salientes, "
                f"{result.get('n_entrantes_total', 0)} entrantes")
    return "resultado no resumible"


app = FastAPI(title="bcra-regulatory-kg — app local")
RUNS = _discover_runs()
RUNS_BY_ID = {r["id"]: r for r in RUNS}
AGENTS = {}  # run_id -> _ChatAgent, creado perezosamente en el primer /chat
# tool_log es estado compartido por agente: serializamos /chat para no mezclarlo.
_CHAT_LOCK = threading.Lock()

# --- Registro de sesiones (U3): jsonl append-only estricto en app/sessions/ ---
SESSIONS_DIR = Path(__file__).resolve().parent / "sessions"
_TURNOS = {}  # session_id -> último turno emitido (1-based), contado en memoria
# Serializa contador de turnos + append al jsonl (una línea por write, con flush).
_LOG_LOCK = threading.Lock()


def _now_iso() -> str:
    """Timestamp ISO 8601 con zona horaria local del server."""
    return datetime.now().astimezone().isoformat()


def _append_line(record: dict) -> Path:
    """Apenda `record` como UNA línea al jsonl del día y devuelve su ruta.
    Nunca reescribe: solo open en modo append + write de línea completa + flush."""
    SESSIONS_DIR.mkdir(parents=True, exist_ok=True)
    path = SESSIONS_DIR / f"{datetime.now().strftime('%Y-%m-%d')}.jsonl"
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
        f.flush()
    return path


class ChatRequest(BaseModel):
    run_id: str
    pregunta: str
    session_id: Optional[str] = None


STATIC_DIR = Path(__file__).resolve().parent / "static"


@app.get("/")
def index() -> FileResponse:
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/runs")
def get_runs() -> list:
    return RUNS


@app.post("/chat")
def post_chat(req: ChatRequest) -> dict:
    info = RUNS_BY_ID.get(req.run_id)
    if info is None:
        raise HTTPException(
            status_code=404,
            detail=f"run_id desconocido: {req.run_id!r}. "
                   f"Disponibles: {sorted(RUNS_BY_ID)}",
        )
    if "error" in info:
        raise HTTPException(
            status_code=404,
            detail=f"El run {req.run_id!r} existe pero su kg.json no cargó "
                   f"al iniciar: {info['error']}",
        )
    if not os.environ.get("ANTHROPIC_API_KEY", "").strip():
        raise HTTPException(
            status_code=503,
            detail="ANTHROPIC_API_KEY no está seteada en el entorno. Exportala "
                   "antes de arrancar la app: export ANTHROPIC_API_KEY=sk-ant-...",
        )

    session_id = req.session_id or str(uuid.uuid4())

    with _CHAT_LOCK:
        agent = AGENTS.get(req.run_id)
        if agent is None:
            kg = load_graph_from_path(REPO_ROOT / info["ruta"],
                                      adapter_key=ADAPTER_KEYS.get(req.run_id))
            agent = _ChatAgent(kg)
            AGENTS[req.run_id] = agent

        agent.tool_log.clear()
        tr = agent.ask(session_id, req.pregunta)
        tool_log = list(agent.tool_log)

    if tr.error:
        raise HTTPException(status_code=502,
                            detail=f"Error de la API de Anthropic: {tr.error}")

    if tr.parse_ok:
        respuesta = tr.final_json
    else:
        respuesta = {"respuesta_cruda": tr.final_raw, "parse_error": tr.parse_error}

    with _LOG_LOCK:
        _TURNOS[session_id] = _TURNOS.get(session_id, 0) + 1
        turno = _TURNOS[session_id]
        _append_line({
            "tipo": "turno",
            "ts": _now_iso(),
            "session_id": session_id,
            "turno": turno,
            "run_id": req.run_id,
            "pregunta": req.pregunta,
            "respuesta": respuesta,
            # En el registro va el resultado COMPLETO de cada tool, sin truncar.
            "tools_llamadas": [
                {"tool": name, "argumentos": args, "resultado": result}
                for name, args, result in tool_log
            ],
            "feedback": None,
        })

    return {
        "respuesta": respuesta,
        "tools_llamadas": [
            {"tool": name, "argumentos": args, "resumen": _resumen_tool(name, result)}
            for name, args, result in tool_log
        ],
        "session_id": session_id,
        "turno": turno,
    }


class FeedbackRequest(BaseModel):
    session_id: str
    turno: int
    voto: Literal["up", "down"]
    comentario: Optional[str] = None


@app.post("/feedback")
def post_feedback(req: FeedbackRequest) -> dict:
    with _LOG_LOCK:
        path = _append_line({
            "tipo": "feedback",
            "ts": _now_iso(),
            "session_id": req.session_id,
            "turno": req.turno,
            "voto": req.voto,
            "comentario": req.comentario,
        })
    return {"ok": True, "archivo": str(path.relative_to(REPO_ROOT))}
