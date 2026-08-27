"""test_u_app.py — Tests determinísticos de U-APP (sin red, costo API $0).

Cubre:
  (a) campo `usage` bien formado en el registro del turno (cliente LLM fake,
      ninguna llamada sale a la red) y lectura retrocompatible del formato
      viejo: _ultimo_turno sobre registros sin usage + reanudación de la
      numeración de turnos.
  (b) backend de retrieval por grafo en /runs; un turno servido contra el
      índice full-text real de Neo4j (tools despachadas por _ChatAgentNeo4j,
      LLM fake); y el estado graphindex/fallback forzado por
      APP_FORZAR_FALLBACK_GRAPHINDEX=1 en subproceso — el contenedor Neo4j
      NO se tumba para probar el fallback.

Correr desde la raíz del repo:
    .venv/bin/python -m pytest app/test_u_app.py -v

El import de app.main carga todos los grafos (tarda ~1 minuto), y el test
del fallback re-importa la app en un subproceso (otro tanto).
"""

import json
import os
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent

# post_chat exige la key en modo anthropic; acá ninguna llamada sale a la red
# (el cliente LLM es fake), solo hace falta que la variable exista.
os.environ.setdefault("ANTHROPIC_API_KEY", "sk-ant-test-sin-red")

import app.main as m  # noqa: E402  (carga los grafos al importar)

from fastapi.testclient import TestClient  # noqa: E402
from loader import KnowledgeGraph  # noqa: E402  (sys.path ya configurado por app.main)

client = TestClient(m.app)

RESPUESTA_JSON = '{"respondible": true, "respuesta": "respuesta de prueba", "citas": []}'


def _kg_vacio_test() -> KnowledgeGraph:
    return KnowledgeGraph(run_key="test", path=Path("test"), nodes=[], edges=[],
                          raw_node_count=0, raw_edge_count=0, merges=[])


def _resp_final(tin: int, tout: int, cr: int, cw: int):
    return SimpleNamespace(
        stop_reason="end_turn",
        content=[SimpleNamespace(type="text", text=RESPUESTA_JSON)],
        usage=SimpleNamespace(input_tokens=tin, output_tokens=tout,
                              cache_read_input_tokens=cr,
                              cache_creation_input_tokens=cw),
    )


class _FakeLLM:
    """Cliente LLM fake: responde el JSON final en la primera llamada."""

    def __init__(self):
        self.messages = self

    def create(self, **kwargs):
        return _resp_final(tin=123, tout=45, cr=7, cw=9)


class _FakeLLMConTool:
    """1a llamada: tool_use buscar_nodos (se despacha contra el índice real);
    2a llamada: JSON final. Dos entradas de usage en el turno."""

    def __init__(self, consulta: str):
        self.messages = self
        self.consulta = consulta
        self.n = 0

    def create(self, **kwargs):
        self.n += 1
        if self.n == 1:
            return SimpleNamespace(
                stop_reason="tool_use",
                content=[SimpleNamespace(type="tool_use", id="tu_1",
                                         name="buscar_nodos",
                                         input={"consulta": self.consulta,
                                                "limite": 3})],
                usage=SimpleNamespace(input_tokens=200, output_tokens=30,
                                      cache_read_input_tokens=0,
                                      cache_creation_input_tokens=0),
            )
        return _resp_final(tin=400, tout=60, cr=0, cw=0)


@pytest.fixture()
def sessions_tmp(tmp_path, monkeypatch):
    """Redirige el registro de sesiones a un directorio temporal: los jsonl
    reales de app/sessions/ no se tocan."""
    monkeypatch.setattr(m, "SESSIONS_DIR", tmp_path)
    return tmp_path


# --------------------------------------------------------------------------- #
# (a) usage en el registro del turno                                           #
# --------------------------------------------------------------------------- #
def test_usage_bien_formado(sessions_tmp, monkeypatch):
    assert "error" not in m.RUNS_BY_ID["run_3_ppf_core"]
    monkeypatch.setitem(m.AGENTS, "run_3_ppf_core",
                        m._ChatAgent(_kg_vacio_test(), client=_FakeLLM()))

    r = client.post("/chat", json={"run_id": "run_3_ppf_core",
                                   "pregunta": "pregunta de prueba",
                                   "session_id": "t-usage-1"})
    assert r.status_code == 200, r.text
    body = r.json()
    assert body["turno"] == 1
    assert body["backend_grafo"] == "graphindex"

    lineas = (sessions_tmp / "local" / "t-usage-1.jsonl").read_text(
        encoding="utf-8").splitlines()
    assert len(lineas) == 1
    reg = json.loads(lineas[0])
    assert reg["tipo"] == "turno"
    assert reg["backend_grafo"] == "graphindex"

    usage = reg["usage"]
    assert usage["total"] == {"llamadas": 1, "input_tokens": 123,
                              "output_tokens": 45, "cache_read": 7,
                              "cache_write": 9, "modelo": m.MODEL_EFECTIVO}
    (llamada,) = usage["por_llamada"]
    assert llamada["input_tokens"] == 123
    assert llamada["output_tokens"] == 45
    assert llamada["cache_read"] == 7
    assert llamada["cache_write"] == 9
    assert llamada["stop_reason"] == "end_turn"
    assert llamada["modelo"] == m.MODEL_EFECTIVO
    assert isinstance(llamada["latency_s"], float)


def test_formato_viejo_sigue_leyendose(sessions_tmp, monkeypatch):
    """Un jsonl con turnos SIN usage (formato pre-U-APP) no rompe la lectura:
    _ultimo_turno lo cuenta y la numeración se reanuda desde ahí."""
    path = sessions_tmp / "local" / "t-viejo.jsonl"
    path.parent.mkdir(parents=True)
    registro_viejo = {
        "tipo": "turno", "ts": "2026-08-01T00:00:00-03:00",
        "session_id": "t-viejo", "turno": 5, "usuario": "local",
        "run_id": "run_3_ppf_core", "backend": "anthropic",
        "modelo": "claude-haiku-4-5-20251001", "pregunta": "p",
        "respuesta": {"respondible": True}, "tools_llamadas": [],
        "feedback": None,
    }
    path.write_text(json.dumps(registro_viejo, ensure_ascii=False) + "\n",
                    encoding="utf-8")
    assert m._ultimo_turno(path) == 5

    monkeypatch.setitem(m.AGENTS, "run_3_ppf_core",
                        m._ChatAgent(_kg_vacio_test(), client=_FakeLLM()))
    r = client.post("/chat", json={"run_id": "run_3_ppf_core",
                                   "pregunta": "pregunta nueva",
                                   "session_id": "t-viejo"})
    assert r.status_code == 200, r.text
    assert r.json()["turno"] == 6

    lineas = path.read_text(encoding="utf-8").splitlines()
    assert len(lineas) == 2
    assert json.loads(lineas[0]) == registro_viejo  # la línea vieja, intacta
    nuevo = json.loads(lineas[1])
    assert nuevo["turno"] == 6 and "usage" in nuevo


# --------------------------------------------------------------------------- #
# (b) backend por grafo                                                        #
# --------------------------------------------------------------------------- #
def test_runs_declara_backend_por_grafo():
    runs = client.get("/runs").json()
    assert all("backend" in r for r in runs)
    por_id = {r["id"]: r for r in runs}
    assert por_id["run_1_cookbook"]["backend"] == "graphindex"
    esperado = ("neo4j/fulltext" if m.NEO4J_DRIVER is not None
                else "graphindex/fallback")
    for run_id in m.NEO4J_GRAFOS:
        assert por_id[run_id]["backend"] == esperado
        if esperado == "graphindex/fallback":
            assert por_id[run_id]["backend_motivo"]


@pytest.mark.skipif(m.NEO4J_DRIVER is None,
                    reason="Neo4j no disponible en este entorno")
def test_chat_neo4j_fulltext(sessions_tmp, monkeypatch):
    """Turno completo por /chat con las tools resueltas contra el índice
    full-text REAL de r1 en Neo4j (LLM fake, $0)."""
    from neo4j_index import Neo4jIndex

    indice = Neo4jIndex(m.NEO4J_DRIVER, grafo="KG_Reextraido_r1",
                        modo="fulltext")
    assert indice.indice == "nodos_fulltext_kg_reextraido_r1"
    agente = m._clase_agente_neo4j()(indice,
                                     client=_FakeLLMConTool("efectivo mínimo"))
    monkeypatch.setitem(m.AGENTS, "r1_vigente", agente)

    r = client.post("/chat", json={"run_id": "r1_vigente",
                                   "pregunta": "¿Qué es el efectivo mínimo?",
                                   "session_id": "t-neo4j-1"})
    assert r.status_code == 200, r.text
    body = r.json()
    assert body["backend_grafo"] == "neo4j/fulltext"
    assert len(body["tools_llamadas"]) == 1
    assert body["tools_llamadas"][0]["tool"] == "buscar_nodos"

    reg = json.loads((sessions_tmp / "local" / "t-neo4j-1.jsonl").read_text(
        encoding="utf-8").splitlines()[0])
    assert reg["backend_grafo"] == "neo4j/fulltext"
    assert reg["usage"]["total"] == {"llamadas": 2, "input_tokens": 600,
                                     "output_tokens": 90, "cache_read": 0,
                                     "cache_write": 0,
                                     "modelo": m.MODEL_EFECTIVO}
    # El resultado completo de la tool viene del índice Lucene real.
    resultado = reg["tools_llamadas"][0]["resultado"]
    assert resultado["total_con_match"] > 0
    assert resultado["resultados"]


def test_fallback_forzado_por_flag():
    """Con APP_FORZAR_FALLBACK_GRAPHINDEX=1 los grafos registrados declaran
    graphindex/fallback con motivo, sin tumbar el contenedor. Subproceso:
    la conexión Neo4j se resuelve al import de app.main."""
    codigo = ("import json; from app.main import RUNS_BY_ID; "
              "print(json.dumps({k: [v.get('backend'), v.get('backend_motivo')] "
              "for k, v in RUNS_BY_ID.items()}))")
    env = dict(os.environ, APP_FORZAR_FALLBACK_GRAPHINDEX="1")
    out = subprocess.run([sys.executable, "-c", codigo], cwd=str(REPO_ROOT),
                         env=env, capture_output=True, text=True, timeout=600)
    assert out.returncode == 0, out.stderr
    backends = json.loads(out.stdout.strip().splitlines()[-1])
    for run_id in m.NEO4J_GRAFOS:
        assert backends[run_id][0] == "graphindex/fallback"
        assert "APP_FORZAR_FALLBACK_GRAPHINDEX" in backends[run_id][1]
    assert backends["run_1_cookbook"] == ["graphindex", None]
