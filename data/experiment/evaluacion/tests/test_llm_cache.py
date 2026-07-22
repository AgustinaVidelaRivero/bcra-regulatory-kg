"""
test_llm_cache.py — Test aislado de la capa de caché (NO depende del resto del pipeline
ni de la API real). Usa un cliente FALSO que devuelve un anthropic.types.Message real
construido por model_validate, para ejercitar el contrato exacto.

Foco (lo que pidió la autora): verificar EXPLÍCITAMENTE que un cache-hit (reconstruido)
y un cache-miss (del cliente) devuelven la MISMA forma, incluido el acceso por atributo
que usa el código aguas arriba (resp.usage.x, resp.content[i].y). Más: la llamada real
se paga UNA sola vez, determinismo de la key, errores no se cachean, separación por
namespace (thinking flag), preservación del desglose de tokens y del access_log.

Correr:  python test_llm_cache.py        (imprime PASS/FAIL y sale con código 0/1)
"""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path

from anthropic.types import Message

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import llm_cache as lc


# --------------------------------------------------------------------------- #
# Dobles de prueba                                                            #
# --------------------------------------------------------------------------- #
# Un Message realista: texto intermedio + thinking (con signature) + tool_use,
# y usage con los 4 campos de tokens. Es exactamente lo que el agente con thinking
# ON produciría en un turno que llama a una tool.
SAMPLE_MESSAGE = {
    "id": "msg_test_001",
    "type": "message",
    "role": "assistant",
    "model": "claude-haiku-4-5-20251001",
    "content": [
        {"type": "thinking", "thinking": "Necesito buscar el nodo.", "signature": "sig_abc123"},
        {"type": "text", "text": "Voy a buscar en el grafo."},
        {"type": "tool_use", "id": "toolu_001", "name": "buscar_nodos",
         "input": {"consulta": "encaje", "limite": 10}},
    ],
    "stop_reason": "tool_use",
    "stop_sequence": None,
    "usage": {"input_tokens": 1433, "output_tokens": 87,
              "cache_read_input_tokens": 0, "cache_creation_input_tokens": 1200},
}


class FakeMessages:
    def __init__(self, message_dict=None, raise_exc=None):
        self.calls = 0
        self._md = message_dict
        self._raise = raise_exc

    def create(self, **kwargs):
        self.calls += 1
        if self._raise is not None:
            raise self._raise
        return Message.model_validate(self._md)


class FakeClient:
    def __init__(self, msgs):
        self.messages = msgs


SAMPLE_KWARGS = dict(
    model="claude-haiku-4-5-20251001",
    max_tokens=8000,
    temperature=1,
    system="Sos un asistente del BCRA.",
    messages=[{"role": "user", "content": "¿Qué es el encaje?"}],
    tools=[{"name": "buscar_nodos", "description": "busca", "input_schema": {"type": "object"}}],
    thinking={"type": "enabled", "budget_tokens": 4000},
)


# --------------------------------------------------------------------------- #
# Runner mínimo de checks                                                     #
# --------------------------------------------------------------------------- #
_checks = []


def check(name, cond):
    _checks.append((name, bool(cond)))


def _new_cache(tmp, fake, *, thinking=True, namespace=None, run_label="test"):
    ns = namespace or lc.make_namespace("agent", code_ver="testcv",
                                        graph_fp="testgfp", thinking=thinking)
    return lc.CachingClient(FakeClient(fake), namespace=ns,
                            db_path=Path(tmp) / "calls.db", domain="agent",
                            thinking_enabled=thinking, run_label=run_label)


try:  # bajo pytest, `tmp` es un fixture (envuelve tmp_path); el modo script no requiere pytest
    import pytest

    @pytest.fixture
    def tmp(tmp_path):
        return str(tmp_path)
except ImportError:
    pass


# --------------------------------------------------------------------------- #
# Tests                                                                       #
# --------------------------------------------------------------------------- #
def test_hit_equals_miss_shape(tmp):
    """EL test central: hit y miss devuelven la misma forma y el mismo acceso por atributo."""
    fake = FakeMessages(SAMPLE_MESSAGE)
    cache = _new_cache(tmp, fake)

    resp_miss = cache.messages.create(**SAMPLE_KWARGS)   # 1ra vez → miss (va al fake)
    resp_hit = cache.messages.create(**SAMPLE_KWARGS)    # 2da vez → hit (reconstruido de DB)

    # La llamada real se pagó UNA sola vez.
    check("la API real se llama 1 sola vez (2 create, 1 hit)", fake.calls == 1)

    # Mismo tipo SDK.
    check("hit y miss son anthropic.types.Message",
          type(resp_hit) is Message and type(resp_miss) is Message)

    # Igualdad profunda: NADA se dropeó en el round-trip.
    check("model_dump idéntico hit vs miss",
          resp_hit.model_dump(mode="json") == resp_miss.model_dump(mode="json"))

    # Acceso por atributo a usage (lo que hace harness.py / judge.py).
    for r in (resp_miss, resp_hit):
        pass
    check("usage.input_tokens igual por atributo",
          resp_hit.usage.input_tokens == resp_miss.usage.input_tokens == 1433)
    check("usage.output_tokens igual por atributo",
          resp_hit.usage.output_tokens == resp_miss.usage.output_tokens == 87)
    check("usage.cache_creation_input_tokens preservado",
          resp_hit.usage.cache_creation_input_tokens
          == resp_miss.usage.cache_creation_input_tokens == 1200)
    check("usage.cache_read_input_tokens preservado",
          resp_hit.usage.cache_read_input_tokens
          == resp_miss.usage.cache_read_input_tokens == 0)
    check("stop_reason igual por atributo",
          resp_hit.stop_reason == resp_miss.stop_reason == "tool_use")
    check("model igual por atributo", resp_hit.model == resp_miss.model)
    check("id igual por atributo", resp_hit.id == resp_miss.id == "msg_test_001")

    # content[] recorre igual, incluido el thinking block con su signature.
    check("content tiene mismo nº de bloques",
          len(resp_hit.content) == len(resp_miss.content) == 3)
    check("tipos de bloque iguales",
          [b.type for b in resp_hit.content] == [b.type for b in resp_miss.content]
          == ["thinking", "text", "tool_use"])
    th_hit = resp_hit.content[0]
    th_miss = resp_miss.content[0]
    check("thinking.thinking preservado",
          th_hit.thinking == th_miss.thinking == "Necesito buscar el nodo.")
    check("thinking.signature preservado (clave para replay multi-turno)",
          th_hit.signature == th_miss.signature == "sig_abc123")
    tu_hit = resp_hit.content[2]
    check("tool_use.id / name / input preservados",
          tu_hit.id == "toolu_001" and tu_hit.name == "buscar_nodos"
          and tu_hit.input == {"consulta": "encaje", "limite": 10})

    # Smoke de INTEGRACIÓN: ejercitar el contrato real que usan harness y juez.
    # harness.py:543 — extracción del texto final:
    final_text_hit = "".join(b.text for b in resp_hit.content if getattr(b, "type", "") == "text")
    final_text_miss = "".join(b.text for b in resp_miss.content if getattr(b, "type", "") == "text")
    check("extracción de texto final (patrón harness) no rompe y coincide",
          final_text_hit == final_text_miss == "Voy a buscar en el grafo.")
    # harness.py:506 — iteración de tool_use blocks:
    tools_hit = [b for b in resp_hit.content if b.type == "tool_use"]
    check("iteración de tool_use blocks (patrón harness) funciona en el hit",
          len(tools_hit) == 1 and tools_hit[0].name == "buscar_nodos")
    # judge.py:196 / harness.py:489 — usage por atributo:
    check("uso de usage por atributo (patrón juez/harness) no rompe en el hit",
          isinstance(resp_hit.usage.input_tokens, int))

    cache.close()


def test_token_breakdown_persisted(tmp):
    """El desglose de tokens por llamada —irrecuperable en el frozen— queda en columnas."""
    fake = FakeMessages(SAMPLE_MESSAGE)
    cache = _new_cache(tmp, fake)
    cache.messages.create(**SAMPLE_KWARGS)
    cur = cache._conn.execute(
        "SELECT input_tokens, output_tokens, cache_read_tokens, cache_write_tokens FROM cache")
    row = cur.fetchone()
    check("columnas de tokens persistidas con el desglose exacto",
          row["input_tokens"] == 1433 and row["output_tokens"] == 87
          and row["cache_read_tokens"] == 0 and row["cache_write_tokens"] == 1200)
    # request_json y raw_json presentes (auditable + crudo íntegro)
    cur = cache._conn.execute("SELECT request_json, raw_json FROM cache")
    r = cur.fetchone()
    check("request_json (auditable) y raw_json (crudo íntegro) persistidos",
          bool(r["request_json"]) and bool(r["raw_json"]))
    cache.close()


def test_key_determinism(tmp):
    """Misma llamada con distinto orden de claves → misma key. Cambios reales → key distinta."""
    import collections
    ns = lc.make_namespace("agent", code_ver="cv", graph_fp="gfp", thinking=True)

    k1 = lc.compute_key(ns, lc.canonical_request(dict(SAMPLE_KWARGS)))
    # mismo contenido, distinto orden de inserción de las claves top-level:
    reordered = collections.OrderedDict()
    for key in reversed(list(SAMPLE_KWARGS.keys())):
        reordered[key] = SAMPLE_KWARGS[key]
    k2 = lc.compute_key(ns, lc.canonical_request(reordered))
    check("orden de claves no cambia la key (canónica)", k1 == k2)

    # cambiar temperature → key distinta
    kw_temp = dict(SAMPLE_KWARGS, temperature=0)
    k3 = lc.compute_key(ns, lc.canonical_request(kw_temp))
    check("temperature distinta → key distinta", k1 != k3)

    # cambiar thinking → key distinta (mismo namespace)
    kw_think = dict(SAMPLE_KWARGS, thinking={"type": "disabled"})
    k4 = lc.compute_key(ns, lc.canonical_request(kw_think))
    check("thinking distinto → key distinta", k1 != k4)


def test_namespace_separation(tmp):
    """thinking-ON y thinking-OFF nunca se cruzan: distinto namespace → no hay hit cruzado."""
    fake = FakeMessages(SAMPLE_MESSAGE)
    db = Path(tmp) / "calls.db"
    ns_off = lc.make_namespace("agent", code_ver="cv", graph_fp="gfp", thinking=False)
    ns_on = lc.make_namespace("agent", code_ver="cv", graph_fp="gfp", thinking=True)
    c_off = lc.CachingClient(FakeClient(fake), namespace=ns_off, db_path=db,
                             domain="agent", thinking_enabled=False, run_label="off")
    c_on = lc.CachingClient(FakeClient(fake), namespace=ns_on, db_path=db,
                            domain="agent", thinking_enabled=True, run_label="on")
    c_off.messages.create(**SAMPLE_KWARGS)   # miss en namespace off
    c_on.messages.create(**SAMPLE_KWARGS)    # miss en namespace on (NO hit cruzado)
    check("misma llamada en namespaces distintos → 2 llamadas reales (sin cruce)",
          fake.calls == 2)
    n = c_off._conn.execute("SELECT COUNT(*) AS n FROM cache").fetchone()["n"]
    check("dos entradas separadas en la caché (off + on)", n == 2)
    c_off.close()
    c_on.close()


def test_error_not_cached(tmp):
    """Si la API falla, la excepción se propaga y NO se cachea el error."""
    class Boom(Exception):
        pass

    fake_err = FakeMessages(raise_exc=Boom("falla de API simulada"))
    cache = _new_cache(tmp, fake_err)
    raised = False
    try:
        cache.messages.create(**SAMPLE_KWARGS)
    except Boom:
        raised = True
    check("la excepción de la API se propaga", raised)
    ns = cache.namespace
    key = lc.compute_key(ns, lc.canonical_request(SAMPLE_KWARGS))
    check("el error NO quedó cacheado (sin fila)", lc._lookup(cache._conn, key) is None)

    # ahora el mismo request con un cliente que responde bien → miss que sí se cachea
    fake_ok = FakeMessages(SAMPLE_MESSAGE)
    cache._real = FakeClient(fake_ok)
    resp = cache.messages.create(**SAMPLE_KWARGS)
    check("tras el fallo, un reintento exitoso sí se cachea",
          lc._lookup(cache._conn, key) is not None and resp.id == "msg_test_001")
    cache.close()


def test_access_log_and_stats(tmp):
    """access_log registra hit/miss y stats() reporta hit rate de la corrida."""
    fake = FakeMessages(SAMPLE_MESSAGE)
    cache = _new_cache(tmp, fake, run_label="corrida_x")
    cache.messages.create(**SAMPLE_KWARGS)   # miss
    cache.messages.create(**SAMPLE_KWARGS)   # hit
    rows = cache._conn.execute(
        "SELECT hit FROM access_log ORDER BY rowid").fetchall()
    check("access_log registró 2 accesos (1 miss, 1 hit)",
          [r["hit"] for r in rows] == [0, 1])
    s = cache.stats()
    check("stats(): 1 hit, 1 miss, hit_rate 0.5",
          s["hits"] == 1 and s["misses"] == 1 and s["hit_rate"] == 0.5)
    check("stats(): tokens_in acumulado de las 2 lecturas (miss+hit)",
          s["tokens_in"] == 1433 * 2)
    cache.close()


def test_multiturn_all_captured(tmp):
    """Cada turno es un create() distinto → key distinta → TODOS los turnos se capturan."""
    fake = FakeMessages(SAMPLE_MESSAGE)
    cache = _new_cache(tmp, fake)
    kw_t1 = dict(SAMPLE_KWARGS)
    kw_t2 = dict(SAMPLE_KWARGS, messages=SAMPLE_KWARGS["messages"] + [
        {"role": "assistant", "content": "..."},
        {"role": "user", "content": [{"type": "tool_result", "tool_use_id": "toolu_001",
                                       "content": "{}"}]},
    ])
    cache.messages.create(**kw_t1)
    cache.messages.create(**kw_t2)
    n = cache._conn.execute("SELECT COUNT(*) AS n FROM cache").fetchone()["n"]
    check("dos turnos distintos → dos entradas (toda la trayectoria queda)",
          n == 2 and fake.calls == 2)
    cache.close()


# --------------------------------------------------------------------------- #
# Main                                                                        #
# --------------------------------------------------------------------------- #
def main():
    tests = [
        test_hit_equals_miss_shape,
        test_token_breakdown_persisted,
        test_key_determinism,
        test_namespace_separation,
        test_error_not_cached,
        test_access_log_and_stats,
        test_multiturn_all_captured,
    ]
    for t in tests:
        with tempfile.TemporaryDirectory() as tmp:
            t(tmp)

    print("\n=== Resultados del test de la capa de caché (llm_cache.py) ===\n")
    passed = 0
    for name, ok in _checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
        passed += ok
    total = len(_checks)
    print(f"\n  {passed}/{total} checks OK")
    print("  RESULTADO:", "PASS ✅" if passed == total else "FAIL ❌")
    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main())
