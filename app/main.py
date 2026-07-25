"""main.py — App local mínima sobre los grafos del repo (U1-U5 + H2).

U1: descubrimiento de grafos al iniciar (glob de data/experiment/*/kg.json)
y endpoint GET /runs. U2: POST /chat envolviendo al GraphAgent del harness.
U3: registro append-only de turnos y feedback (POST /feedback). H2: backend
de inferencia configurable (API Anthropic o Bedrock, ver llm_backend.py) y
registro por app/sessions/<usuario>/<session_id>.jsonl con turno derivado
del archivo. Toda carga de grafos pasa por load_graph_from_path() del
loader de la Fase 2.3; acá no se parsea ningún kg.json a mano.

Arranque, desde la raíz del repo (modo local: requiere ANTHROPIC_API_KEY en
el entorno para /chat; la app no lee ningún .env. Modo Bedrock: ver README):
    uvicorn app.main:app --port 8000
"""

import json
import os
import re
import secrets
import sys
import threading
import time
import uuid
from datetime import datetime
from pathlib import Path
from typing import Literal, Optional

from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel

REPO_ROOT = Path(__file__).resolve().parent.parent
EXPERIMENT_DIR = REPO_ROOT / "data" / "experiment"
EVALUACION_DIR = EXPERIMENT_DIR / "evaluacion"

# El loader y el harness viven fuera de un package; se importan por sys.path.
sys.path.insert(0, str(EVALUACION_DIR))
from loader import load_graph_from_path  # noqa: E402
from harness import GraphAgent  # noqa: E402

from app.llm_backend import backend_name, build_client, effective_model_id  # noqa: E402

# Config del backend, resuelta UNA vez al arranque (falla acá si está incompleta).
BACKEND = backend_name()
LLM_CLIENT = build_client()
MODEL_EFECTIVO = effective_model_id()

# --- Auth por token (H3): mapa token -> usuario, validado al arranque --------
_USUARIO_RE = re.compile(r"^[A-Za-z0-9._-]+$")


def _parse_tokens() -> dict:
    """Mapa token -> usuario. Fuentes (precedencia: archivo > env):
    APP_TOKENS_FILE (una línea 'token:usuario' por usuario; '#' comenta) o
    APP_TOKENS ('token:usuario' separado por comas). Sin ninguna de las dos,
    devuelve {} = modo local sin auth. Formato inválido impide el arranque."""
    src_file = (os.environ.get("APP_TOKENS_FILE") or "").strip()
    src_env = (os.environ.get("APP_TOKENS") or "").strip()
    if src_file:
        origen = f"APP_TOKENS_FILE ({src_file})"
        try:
            entradas = Path(src_file).read_text(encoding="utf-8").splitlines()
        except OSError as e:
            raise RuntimeError(f"{origen}: no se pudo leer: {e}")
    elif src_env:
        origen = "APP_TOKENS"
        entradas = src_env.split(",")
    else:
        return {}

    tokens = {}
    for cruda in entradas:
        entrada = cruda.strip()
        if not entrada or entrada.startswith("#"):
            continue
        token, sep, usuario = entrada.partition(":")
        token, usuario = token.strip(), usuario.strip()
        if not sep or not token or not usuario:
            raise RuntimeError(
                f"{origen}: entrada inválida {entrada!r} "
                "(formato esperado 'token:usuario')."
            )
        if not _USUARIO_RE.fullmatch(usuario):
            raise RuntimeError(
                f"{origen}: usuario inválido {usuario!r} "
                "(permitidos: letras, dígitos, '.', '_', '-')."
            )
        if token in tokens:
            raise RuntimeError(
                f"{origen}: token duplicado (asignado a {tokens[token]!r} "
                f"y a {usuario!r})."
            )
        tokens[token] = usuario
    if not tokens:
        raise RuntimeError(f"{origen}: no contiene ningún token válido.")
    return tokens


TOKENS = _parse_tokens()
AUTH_ACTIVA = bool(TOKENS)

# --- Registro autoservicio por código de invitación (H6) ---------------------
TOKENS_FILE = (os.environ.get("APP_TOKENS_FILE") or "").strip()
INVITE_CODE = (os.environ.get("APP_INVITE_CODE") or "").strip()
if AUTH_ACTIVA and TOKENS_FILE and not INVITE_CODE:
    raise RuntimeError(
        "APP_INVITE_CODE es obligatoria cuando la auth usa APP_TOKENS_FILE "
        "(el registro autoservicio necesita el código de invitación)."
    )


def _usuario_de(authorization: Optional[str]) -> str:
    """Resuelve el usuario del request. Sin auth configurada: 'local'."""
    if not AUTH_ACTIVA:
        return "local"
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Falta el header 'Authorization: Bearer <token>'.",
        )
    usuario = TOKENS.get(authorization[len("Bearer "):].strip())
    if usuario is None:
        raise HTTPException(
            status_code=401,
            detail="Token inválido: revisá el token configurado para tu usuario.",
        )
    return usuario

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

# --- Registro de sesiones (U3 + H2 + H3): jsonl append-only estricto, un -----
# --- archivo por sesión en app/sessions/<usuario>/<session_id>.jsonl ---------
# El usuario sale del token (auth activa) o es "local" (modo sin auth).
SESSIONS_DIR = Path(__file__).resolve().parent / "sessions"
_TURNOS = {}  # (usuario, session_id) -> último turno emitido (1-based)
# Serializa contador de turnos + append al jsonl (una línea por write, con flush).
_LOG_LOCK = threading.Lock()

# El session_id es también nombre de archivo: formato restringido (sin "/",
# sin "..") para que un id arbitrario no pueda salirse de app/sessions/.
_SESSION_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,99}$")


def _validar_session_id(session_id: str) -> str:
    if not _SESSION_ID_RE.fullmatch(session_id):
        raise HTTPException(
            status_code=422,
            detail="session_id inválido: se admiten letras, dígitos, '.', '_' y "
                   "'-' (máx. 100 chars, sin empezar con símbolo).",
        )
    return session_id


def _now_iso() -> str:
    """Timestamp ISO 8601 con zona horaria local del server."""
    return datetime.now().astimezone().isoformat()


def _session_path(usuario: str, session_id: str) -> Path:
    return SESSIONS_DIR / usuario / f"{session_id}.jsonl"


def _ultimo_turno(path: Path) -> int:
    """Último turno registrado en el jsonl de la sesión (0 si no existe).
    Permite que la numeración continúe tras un reinicio del server."""
    if not path.exists():
        return 0
    ultimo = 0
    with path.open(encoding="utf-8") as f:
        for line in f:
            try:
                d = json.loads(line)
            except json.JSONDecodeError:
                continue
            if d.get("tipo") == "turno" and isinstance(d.get("turno"), int):
                ultimo = max(ultimo, d["turno"])
    return ultimo


def _append_line(usuario: str, session_id: str, record: dict) -> Path:
    """Apenda `record` como UNA línea al jsonl de la sesión y devuelve su ruta.
    Nunca reescribe: solo open en modo append + write de línea completa + flush."""
    path = _session_path(usuario, session_id)
    path.parent.mkdir(parents=True, exist_ok=True)
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
def post_chat(req: ChatRequest,
              authorization: Optional[str] = Header(default=None)) -> dict:
    usuario = _usuario_de(authorization)
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
    # La key solo se exige en modo anthropic; en modo bedrock no debe usarse.
    if BACKEND == "anthropic" and not os.environ.get("ANTHROPIC_API_KEY", "").strip():
        raise HTTPException(
            status_code=503,
            detail="ANTHROPIC_API_KEY no está seteada en el entorno. Exportala "
                   "antes de arrancar la app: export ANTHROPIC_API_KEY=sk-ant-...",
        )

    session_id = _validar_session_id(req.session_id or str(uuid.uuid4()))

    with _CHAT_LOCK:
        agent = AGENTS.get(req.run_id)
        if agent is None:
            kg = load_graph_from_path(REPO_ROOT / info["ruta"],
                                      adapter_key=ADAPTER_KEYS.get(req.run_id))
            agent = _ChatAgent(kg, client=LLM_CLIENT)
            AGENTS[req.run_id] = agent

        agent.tool_log.clear()
        tr = agent.ask(session_id, req.pregunta)
        tool_log = list(agent.tool_log)

    if tr.error:
        raise HTTPException(status_code=502,
                            detail=f"Error del backend LLM ({BACKEND}): {tr.error}")

    if tr.parse_ok:
        respuesta = tr.final_json
    else:
        respuesta = {"respuesta_cruda": tr.final_raw, "parse_error": tr.parse_error}

    with _LOG_LOCK:
        clave = (usuario, session_id)
        if clave not in _TURNOS:
            # Reanudación: el contador arranca del último turno ya persistido.
            _TURNOS[clave] = _ultimo_turno(_session_path(usuario, session_id))
        _TURNOS[clave] += 1
        turno = _TURNOS[clave]
        _append_line(usuario, session_id, {
            "tipo": "turno",
            "ts": _now_iso(),
            "session_id": session_id,
            "turno": turno,
            "usuario": usuario,
            "run_id": req.run_id,
            "backend": BACKEND,
            "modelo": MODEL_EFECTIVO,
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


class RegisterRequest(BaseModel):
    usuario: str
    codigo: str


_REGISTROS = []  # time.time() de cada registro exitoso (rate limit global)
_MAX_REGISTROS_HORA = 10


@app.post("/register")
def post_register(req: RegisterRequest) -> dict:
    """Registro autoservicio: valida el código de invitación, genera un token
    y lo apenda al archivo de tokens. El usuario nunca elige ni ve tokens
    ajenos; el suyo se devuelve una única vez."""
    if not (AUTH_ACTIVA and TOKENS_FILE):
        raise HTTPException(
            status_code=503,
            detail="El registro está deshabilitado: el server no usa archivo "
                   "de tokens (APP_TOKENS_FILE).",
        )
    if req.codigo != INVITE_CODE:
        raise HTTPException(status_code=403, detail="código de invitación incorrecto")
    usuario = req.usuario.strip()
    if not _USUARIO_RE.fullmatch(usuario) or len(usuario) > 32:
        raise HTTPException(
            status_code=422,
            detail="usuario inválido: letras, dígitos, '.', '_' y '-' (máx. 32).",
        )
    with _LOG_LOCK:
        if usuario in TOKENS.values():
            raise HTTPException(status_code=409, detail="nombre en uso, elegí otro")
        ahora = time.time()
        _REGISTROS[:] = [t for t in _REGISTROS if ahora - t < 3600]
        if len(_REGISTROS) >= _MAX_REGISTROS_HORA:
            raise HTTPException(
                status_code=429,
                detail="límite de registros por hora alcanzado; probá más tarde",
            )
        token = secrets.token_hex(16)
        # append-only al archivo de tokens, una línea completa con flush
        with open(TOKENS_FILE, "a", encoding="utf-8") as f:
            f.write(f"{token}:{usuario}\n")
            f.flush()
        TOKENS[token] = usuario
        _REGISTROS.append(ahora)
    return {"token": token, "usuario": usuario}


class FeedbackRequest(BaseModel):
    session_id: str
    turno: int
    voto: Literal["up", "down"]
    comentario: Optional[str] = None


@app.post("/feedback")
def post_feedback(req: FeedbackRequest,
                  authorization: Optional[str] = Header(default=None)) -> dict:
    usuario = _usuario_de(authorization)
    session_id = _validar_session_id(req.session_id)
    with _LOG_LOCK:
        path = _append_line(usuario, session_id, {
            "tipo": "feedback",
            "ts": _now_iso(),
            "session_id": session_id,
            "turno": req.turno,
            "usuario": usuario,
            "voto": req.voto,
            "comentario": req.comentario,
        })
    return {"ok": True, "archivo": str(path.relative_to(REPO_ROOT))}
