"""
selftest_ub53.py — U-B5.3: reintento por corte de max_tokens, tope compartido
entre clientes y sub-chunking por ítems para unidades sobre el umbral C8.

USD 0 / sin LLM: todo corre con stubs, clientes falsos y material vigente del
repo que se LEE, jamás se escribe (salidas E0 selladas, e0_dry del corpus de
escalado). Puntos:

  P1  reintento por corte (cliente_e1.crear_con_reintento_corte): dispara
      SOLO ante stop_reason == "max_tokens", una sola vez, con 32.768; el
      camino sin corte pasa kwargs byte-idénticos (misma clave de caché
      histórica); claves distintas entre intento 1 y 2; sin tercera llamada.
  P2  persistencia de AMBOS intentos en la db (CachingClient real sobre SDK
      falso, offline) y never-pay-twice del reintento (replay = 2 hits).
  P3  runner fase E1 (stub): el pase reintenta en el acto, registra ambos
      intentos en el jsonl, cierra sin reintentables pendientes y contabiliza
      los definitivos en resumen_e1.json; sin corte, el registro y el resumen
      no cambian de forma.
  P4  tope compartido (runner_corpus.PresupuestoCompartido): corta a través
      de más de un cliente (E1 y E3), acumula los misses de todos, persiste
      su estado para reanudar y el tope configurado manda.
  P5  sub-chunking (correr_e0.subdividir_unidades_grandes): 0 unidades del
      conjunto de desarrollo tocadas (identidad, con el peor terminal dev
      exactamente EN el umbral); parte un caso real del corpus de escalado
      (e0_dry, solo lectura) y casos sintéticos; cero pérdida; herencia del
      chapeau según el patrón E0; unidades sin ítems declaradas sin partir.
  P6  candados: prefijo E1 y tool schema byte-idénticos (hash sellado), techo
      del ratchet intacto (16.384) y techo del reintento por corte == 32.768.

Uso:  .venv/bin/python3 selftest_ub53.py
"""

from __future__ import annotations

import json
import os
import sqlite3
import sys
import tempfile
from pathlib import Path

AQUI = Path(__file__).resolve().parent                   # reextraccion_v2/
for sub in ("e1_extractor", "e3_verificador", "e2_reduce", "corpus_v2",
            "e0_chunking"):
    sys.path.insert(0, str(AQUI / sub))
sys.path.insert(0, str(AQUI))

from anthropic.types import Message   # noqa: E402 — solo tipos, sin red

import comun_e1                        # noqa: E402
import prompt_e1                       # noqa: E402
import cliente_e1                      # noqa: E402
import cliente_e3                      # noqa: E402
import correr_e0                       # noqa: E402
import healthcheck_e0                  # noqa: E402
import runner_corpus as RC             # noqa: E402
import llm_cache as lc                 # noqa: E402

REPO = AQUI.parents[2]
E0_DEV = AQUI / "e0_chunking" / "salida_enm01"
E0_DRY = REPO / "data" / "experiment" / "escalado_prep" / "e0_dry"

_n = 0
_fallos = 0


def check(desc: str, ok: bool, detalle: str = "") -> None:
    global _n, _fallos
    _n += 1
    if not ok:
        _fallos += 1
    print(f"[{_n:2d}] {'ok   ' if ok else 'FALLO'} {desc}"
          + (f" — {detalle}" if detalle else ""), flush=True)


# ------------------------------------------------------------------------- #
# Dobles de prueba                                                          #
# ------------------------------------------------------------------------- #

def _msg(stop: str, tool_input, out_tokens: int = 100) -> Message:
    """Message real del SDK (model_validate): lo que persiste la caché."""
    return Message.model_validate({
        "id": "msg_ub53", "type": "message", "role": "assistant",
        "model": "claude-haiku-4-5",
        "content": [{"type": "tool_use", "id": "tu_1",
                     "name": prompt_e1.NOMBRE_TOOL, "input": tool_input}],
        "stop_reason": stop, "stop_sequence": None,
        "usage": {"input_tokens": 11, "output_tokens": out_tokens,
                  "cache_creation_input_tokens": 0,
                  "cache_read_input_tokens": 0},
    })


TOOL_OK = {"entities": [], "relations": []}
TOOL_CORTADO = {"entities": None, "relations": None}  # contenedor no-lista


class StubEspia:
    """Cola de responses + registro de cada kwargs recibido (sin doc)."""

    def __init__(self, cola):
        self._cola = list(cola)
        self.requests: list[dict] = []
        self.messages = self

    def create(self, **kwargs):
        self.requests.append(kwargs)
        return self._cola.pop(0)


class StubCortadorE1(RC.StubE1Corpus):
    """Stub del runner que corta por max_tokens en las llamadas indicadas
    (1-indexadas), devolviendo el contenedor no-lista de los cortes reales."""

    def __init__(self, cortar_en):
        super().__init__()
        self._cortar = set(cortar_en)
        self.n = 0
        self.requests: list[dict] = []

    def create(self, doc=None, **kwargs):
        self.n += 1
        self.requests.append(kwargs)
        resp = super().create(doc=doc, **kwargs)
        if self.n in self._cortar:
            resp.stop_reason = "max_tokens"
            resp.content[0].input = dict(TOOL_CORTADO)
        return resp


def _chunk_fx(texto: str, unidad: str = "1.1", herencia=None) -> dict:
    return {"id": f"fxa::{unidad}", "to": "fxa", "archivo": "fx.pdf",
            "unidad": unidad, "titulo": f"t {unidad}", "tipo": "punto_terminal",
            "paginas": [1], "texto": texto, "chars_propio": len(texto),
            "chars_completo": len(texto), "herencia": herencia or [],
            "flags": {"contenido_tabular": False, "formula": False},
            "sha256_propio": "x", "sha256_completo": "x"}


# ========================================================================= #
# P1 — reintento por corte: disparo, techo, claves                          #
# ========================================================================= #

def p1_reintento() -> None:
    chunk = _chunk_fx("1.1. Título.\nLas entidades deberán informar.")
    kwargs = prompt_e1.build_request_kwargs(chunk, model="claude-haiku-4-5")
    canon_base = lc.canonical_request(kwargs)

    # sin corte: una sola llamada, kwargs tal cual (byte-idénticos)
    stub = StubEspia([_msg("tool_use", TOOL_OK)])
    resp, cortado = cliente_e1.crear_con_reintento_corte(stub, kwargs)
    check("P1 sin corte: una sola llamada y sin intento cortado",
          len(stub.requests) == 1 and cortado is None)
    check("P1 sin corte: kwargs byte-idénticos (misma clave de caché histórica)",
          lc.canonical_request(stub.requests[0]) == canon_base
          and stub.requests[0]["max_tokens"] == prompt_e1.MAX_OUTPUT_TOKENS)

    # stop_reason end_turn tampoco dispara
    stub = StubEspia([_msg("end_turn", TOOL_OK)])
    _, cortado = cliente_e1.crear_con_reintento_corte(stub, kwargs)
    check("P1 stop_reason end_turn no dispara reintento",
          len(stub.requests) == 1 and cortado is None)

    # con corte: exactamente dos llamadas, la 2ª con 32k y solo eso cambiado
    stub = StubEspia([_msg("max_tokens", TOOL_CORTADO, 8192),
                      _msg("tool_use", TOOL_OK)])
    resp, cortado = cliente_e1.crear_con_reintento_corte(stub, kwargs)
    k2 = stub.requests[1]
    k2_sin_mt = {k: v for k, v in k2.items() if k != "max_tokens"}
    k1_sin_mt = {k: v for k, v in kwargs.items() if k != "max_tokens"}
    check("P1 con corte: exactamente dos llamadas, la 2ª con max_tokens 32.768",
          len(stub.requests) == 2 and k2["max_tokens"] == 32768)
    check("P1 con corte: el reintento solo cambia max_tokens (resto byte-idéntico)",
          lc.canonical_request(k2_sin_mt) == lc.canonical_request(k1_sin_mt))
    check("P1 con corte: el intento cortado se devuelve íntegro",
          cortado is not None
          and getattr(cortado, "stop_reason", None) == "max_tokens"
          and resp.stop_reason == "tool_use")
    ns = "selftest|ub53"
    check("P1 claves de caché DISTINTAS entre intento 1 y 2",
          lc.compute_key(ns, lc.canonical_request(stub.requests[0]))
          != lc.compute_key(ns, lc.canonical_request(stub.requests[1])))

    # doble corte: dos llamadas y NUNCA una tercera
    stub = StubEspia([_msg("max_tokens", TOOL_CORTADO, 8192),
                      _msg("max_tokens", TOOL_CORTADO, 32768)])
    resp, cortado = cliente_e1.crear_con_reintento_corte(stub, kwargs)
    check("P1 doble corte: dos llamadas, sin tercera, resp final cortada",
          len(stub.requests) == 2 and cortado is not None
          and resp.stop_reason == "max_tokens")


# ========================================================================= #
# P2 — ambos intentos persistidos en la db + never-pay-twice del reintento  #
# ========================================================================= #

def p2_persistencia(tmp: Path) -> None:
    chunk = _chunk_fx("1.1. Título.\nLas entidades deberán informar.")
    kwargs = prompt_e1.build_request_kwargs(chunk, model="claude-haiku-4-5")
    sdk = StubEspia([_msg("max_tokens", TOOL_CORTADO, 8192),
                     _msg("tool_use", TOOL_OK)])
    ns = lc.make_namespace("selftest_ub53", code_ver="ub53", thinking=False)
    db = tmp / "ub53.db"
    cache = lc.CachingClient(sdk, domain="selftest_ub53", db_path=db,
                             namespace=ns, thinking_enabled=False,
                             run_label="selftest_ub53")
    resp, cortado = cliente_e1.crear_con_reintento_corte(cache, kwargs)
    con = sqlite3.connect(db)
    filas = {r[0]: r[1] for r in con.execute("SELECT key, raw_json FROM cache")}
    con.close()
    k1 = lc.compute_key(ns, lc.canonical_request(kwargs))
    kwargs2 = dict(kwargs)
    kwargs2["max_tokens"] = 32768
    k2 = lc.compute_key(ns, lc.canonical_request(kwargs2))
    check("P2 la db tiene EXACTAMENTE los dos intentos (claves propias)",
          set(filas) == {k1, k2}, f"filas={len(filas)}")
    crudo1 = json.loads(filas[k1]) if k1 in filas else {}
    check("P2 el crudo del intento cortado quedó íntegro (stop + tool_input)",
          crudo1.get("stop_reason") == "max_tokens"
          and crudo1.get("content", [{}])[0].get("input") == TOOL_CORTADO)
    # replay: never-pay-twice — el SDK falso no recibe ninguna llamada nueva
    resp2, cortado2 = cliente_e1.crear_con_reintento_corte(cache, kwargs)
    check("P2 replay del par completo: 2 hits, 0 llamadas nuevas al SDK",
          len(sdk.requests) == 2 and cortado2 is not None
          and resp2.stop_reason == "tool_use")
    cache.close()


# ========================================================================= #
# P3 — runner fase E1 con stub: reintento, cierre y contabilidad            #
# ========================================================================= #

def p3_runner(tmp: Path) -> None:
    # corrida A: corta la 1ª llamada, el reintento completa
    salida = tmp / "runA"
    salida.mkdir()
    stub = StubCortadorE1(cortar_en={1})
    estado = RC.Estado(salida)
    RC.fase_e1("pro", stub, estado, salida, 2, None, None)
    regs = [json.loads(l) for l in
            (salida / "pro" / "extracciones_e1.jsonl").read_text(
                encoding="utf-8").splitlines()]
    r1, r2 = regs[0], regs[1]
    check("P3 corrida A: 3 llamadas (2 unidades + 1 reintento), 2ª con 32k",
          stub.n == 3 and stub.requests[1]["max_tokens"] == 32768
          and stub.requests[0]["max_tokens"] == prompt_e1.MAX_OUTPUT_TOKENS
          and stub.requests[2]["max_tokens"] == prompt_e1.MAX_OUTPUT_TOKENS)
    check("P3 corrida A: unidad cortada termina sin error y con AMBOS intentos "
          "en el jsonl",
          r1["error"] is None and "reintento_corte" in r1
          and r1["reintento_corte"]["intento_1"]["stop_reason"] == "max_tokens"
          and r1["reintento_corte"]["intento_1"]["tool_input_crudo"] == TOOL_CORTADO
          and r1["reintento_corte"]["max_tokens_reintento"] == 32768)
    check("P3 corrida A: unidad sin corte con registro de forma histórica "
          "(sin claves nuevas)",
          "reintento_corte" not in r2 and r2["error"] is None)
    resumen = json.loads((salida / "pro" / "resumen_e1.json").read_text(
        encoding="utf-8"))
    check("P3 corrida A: fase cerrada, 1 reintento contabilizado y 0 errores "
          "definitivos",
          estado.fase_cerrada("pro:e1")
          and resumen.get("reintentos_corte") == 1
          and "errores_definitivos" not in resumen)

    # corrida B: corta también el reintento → error definitivo contabilizado
    salida = tmp / "runB"
    salida.mkdir()
    stub = StubCortadorE1(cortar_en={1, 2})
    estado = RC.Estado(salida)
    RC.fase_e1("pro", stub, estado, salida, 2, None, None)
    regs = [json.loads(l) for l in
            (salida / "pro" / "extracciones_e1.jsonl").read_text(
                encoding="utf-8").splitlines()]
    resumen = json.loads((salida / "pro" / "resumen_e1.json").read_text(
        encoding="utf-8"))
    check("P3 corrida B: doble corte queda como error DEFINITIVO (no "
          "reintentable) con ambos intentos persistidos",
          regs[0]["error"] == "max_tokens_hit_tras_reintento"
          and "reintento_corte" in regs[0] and stub.n == 3)
    check("P3 corrida B: la fase cierra con el definitivo contabilizado en "
          "resumen_e1.json",
          estado.fase_cerrada("pro:e1")
          and resumen.get("errores_definitivos") == [
              {"chunk_id": regs[0]["chunk_id"],
               "error": "max_tokens_hit_tras_reintento"}])

    # guardia de cierre: un reintentable pendiente (marcador pre-B5.3) frena
    check("P3 guardia decisión 5: reintentable pendiente detectado",
          RC.reintentables_pendientes(
              {"x::1": {"error": "max_tokens_hit"},
               "x::2": {"error": None},
               "x::3": {"error": "max_tokens_hit_tras_reintento"}}) == ["x::1"])

    # corrida C: sin cortes → resumen byte-equivalente al histórico (sin
    # claves nuevas) — el candado fuerte de huella lo da P7 del selftest del
    # manifiesto (GOLDEN_STUB_PRO); acá se aserta la forma.
    salida = tmp / "runC"
    salida.mkdir()
    stub = RC.StubE1Corpus()
    estado = RC.Estado(salida)
    RC.fase_e1("pro", stub, estado, salida, 2, None, None)
    resumen = json.loads((salida / "pro" / "resumen_e1.json").read_text(
        encoding="utf-8"))
    check("P3 corrida C (sin cortes): resumen con las claves históricas "
          "exactas",
          set(resumen) == {"n_unidades", "cliente", "gasto_fase_usd"})


# ========================================================================= #
# P4 — tope compartido entre clientes                                       #
# ========================================================================= #

def p4_tope_compartido(tmp: Path) -> None:
    os.environ.setdefault("ANTHROPIC_API_KEY", "selftest-ub53-sin-red")
    chunk = _chunk_fx("1.1. Título.\nLas entidades deberán informar.")
    kwargs = prompt_e1.build_request_kwargs(chunk, model="claude-haiku-4-5")

    class FakeCacheMiss:
        """Doble del CachingClient: cada create es un miss con usage fijo."""

        def __init__(self, tokens_out):
            self._stats = {"misses": 0, "hits": 0, "tokens_in": 0,
                           "tokens_out": 0, "cache_write": 0, "cache_read": 0}
            self._tokens_out = tokens_out
            self.messages = self

        def create(self, **kw):
            self._stats["misses"] += 1
            self._stats["tokens_in"] += 1000
            self._stats["tokens_out"] += self._tokens_out
            return _msg("tool_use", TOOL_OK, self._tokens_out)

        def stats(self):
            return dict(self._stats)

        def close(self):
            pass

    guardian = RC.PresupuestoCompartido(1.0, tmp / "pc.json")
    c1 = cliente_e1.ClienteE1Real(
        precio_in_por_mtok=1.0, precio_out_por_mtok=5.0,
        precio_cache_write_por_mtok=1.25, precio_cache_read_por_mtok=0.10,
        tope_usd=100.0, run_label="selftest_ub53_e1",
        db_path=tmp / "e1x.db", guardian=guardian)
    c3 = cliente_e3.ClienteE3Real(
        precio_in_por_mtok=2.0, precio_out_por_mtok=10.0,
        precio_cache_write_por_mtok=2.50, precio_cache_read_por_mtok=0.20,
        tope_usd=100.0, run_label="selftest_ub53_e3",
        db_path=tmp / "e3x.db", guardian=guardian)
    # sin red: se inyecta el doble de caché y se silencia el log de usage
    c1.cache.close()
    c3.cache.close()
    c1.cache = FakeCacheMiss(2000)
    c3.cache = FakeCacheMiss(2000)
    c1._log_usage = lambda *a, **k: None
    c3._log_usage = lambda *a, **k: None

    c1.create(doc=None, **kwargs)          # miss E1: +0.011
    c3.create(doc=None, **kwargs)          # miss E3: +0.022
    esperado = (1000 * 1.0 + 2000 * 5.0) / 1e6 + (1000 * 2.0 + 2000 * 10.0) / 1e6
    check("P4 el guardián acumula los misses de MÁS DE UN cliente",
          abs(guardian.gasto_usd - esperado) < 1e-9,
          f"gasto={guardian.gasto_usd:.6f}")
    check("P4 estado persistido tras cada registro (archivo con el gasto)",
          json.loads((tmp / "pc.json").read_text(encoding="utf-8"))
          ["gasto_usd"] == round(guardian.gasto_usd, 6))

    # tope chico: el PRÓXIMO cliente frena ANTES de llamar (freno duro)
    guardian2 = RC.PresupuestoCompartido(0.02, tmp / "pc2.json")
    guardian2.registrar(0.019)
    c1b = cliente_e1.ClienteE1Real(
        precio_in_por_mtok=1.0, precio_out_por_mtok=5.0,
        precio_cache_write_por_mtok=1.25, precio_cache_read_por_mtok=0.10,
        tope_usd=100.0, run_label="selftest_ub53_e1b",
        db_path=tmp / "e1y.db", guardian=guardian2)
    espia = FakeCacheMiss(2000)
    c1b.cache.close()
    c1b.cache = espia
    try:
        c1b.create(doc=None, **kwargs)
        check("P4 freno duro por tope compartido (E1)", False, "no frenó")
    except cliente_e1.TopeExcedido as e:
        check("P4 freno duro por tope compartido (E1), sin tocar la red",
              "COMPARTIDO" in str(e) and espia._stats["misses"] == 0)
    c3b = cliente_e3.ClienteE3Real(
        precio_in_por_mtok=2.0, precio_out_por_mtok=10.0,
        precio_cache_write_por_mtok=2.50, precio_cache_read_por_mtok=0.20,
        tope_usd=100.0, run_label="selftest_ub53_e3b",
        db_path=tmp / "e3y.db", guardian=guardian2)
    espia3 = FakeCacheMiss(2000)
    c3b.cache.close()
    c3b.cache = espia3
    try:
        c3b.create(doc=None, **kwargs)
        check("P4 freno duro por tope compartido (E3)", False, "no frenó")
    except cliente_e3.TopeExcedido as e:
        check("P4 freno duro por tope compartido (E3): el MISMO guardián corta "
              "al otro cliente",
              "COMPARTIDO" in str(e) and espia3._stats["misses"] == 0)

    # reanudación: un guardián nuevo sobre el mismo path carga el gasto; el
    # tope configurado por la corrida manda sobre el persistido
    g3 = RC.PresupuestoCompartido(5.0, tmp / "pc.json")
    check("P4 reanudación: gasto previo cargado del archivo y tope "
          "configurado vigente",
          abs(g3.gasto_usd - esperado) < 1e-9 and g3.tope_usd == 5.0)


# ========================================================================= #
# P5 — sub-chunking                                                         #
# ========================================================================= #

def p5_subchunking() -> None:
    U = correr_e0.UMBRAL_CHARS_SUBCHUNK
    check("P5 umbral == C8 del health-check de B5.2 (26.182)",
          U == healthcheck_e0.UMBRAL_CHARS_TERMINAL == 26182)

    # conjunto de desarrollo: 0 unidades afectadas, identidad estricta
    tocadas = 0
    peor = 0
    identidad = True
    for to in comun_e1.TOS:
        chunks = json.loads((E0_DEV / f"chunks_{to}.json").read_text(
            encoding="utf-8"))
        out, rep = correr_e0.subdividir_unidades_grandes(chunks)
        tocadas += len(rep["particiones"]) + len(rep["no_particionables"])
        peor = max(peor, max(c["chars_propio"] for c in chunks
                             if c["tipo"] != "mini_chunk"))
        identidad = identidad and len(out) == len(chunks) and all(
            a is b for a, b in zip(out, chunks))
    check("P5 conjunto de desarrollo: recuento de unidades tocadas == 0, "
          "identidad estricta (mismos objetos)",
          tocadas == 0 and identidad)
    check("P5 el peor terminal dev mide EXACTAMENTE el umbral y no se parte "
          "(corte estricto >)", peor == U)

    # caso real del corpus de escalado (solo lectura): manori::1.5
    chunks_man = json.loads((E0_DRY / "manori" / "chunks_manori.json"
                             ).read_text(encoding="utf-8"))
    c = next(x for x in chunks_man if x["id"] == "manori::1.5")
    out, rep = correr_e0.subdividir_unidades_grandes([c])
    subs = out
    check("P5 caso real manori::1.5 (27.161 chars) parte en ≥2 partes, todas "
          "≤ umbral",
          len(subs) >= 2 and all(s["chars_propio"] <= U for s in subs)
          and rep["particiones"][0]["id"] == "manori::1.5"
          and not rep["particiones"][0]["partes_sobre_umbral"],
          f"partes={[s['chars_propio'] for s in subs]}")
    reconstruido = "\n".join(s["texto"] for s in subs)
    check("P5 caso real: CERO PÉRDIDA — las partes reconstruyen el texto "
          "byte a byte", reconstruido == c["texto"])
    check("P5 caso real: ids únicos con sufijo ::parteK, unidad y tipo "
          "preservados",
          len({s["id"] for s in subs}) == len(subs)
          and all(s["id"] == f"{c['id']}::parte{k}"
                  for k, s in enumerate(subs, 1))
          and all(s["unidad"] == c["unidad"] and s["tipo"] == c["tipo"]
                  for s in subs))
    n_h = len(c["herencia"])
    extra = [s["herencia"][n_h:] for s in subs]
    check("P5 caso real: la parte 1 lleva el chapeau en su TEXTO; las partes "
          "2..n lo heredan como tramos del patrón E0 (encabezado[+intro], "
          "unidad_origen = la unidad)",
          extra[0] == [] and subs[0]["texto"].startswith(c["texto"][:20])
          and all(t and t[0]["tipo"] == "encabezado"
                  and all(x["unidad_origen"] == c["unidad"] for x in t)
                  and all(x["tipo"] in ("encabezado", "intro") for x in t)
                  for t in extra[1:]))
    import hashlib as _h
    check("P5 caso real: chars y sha256 recomputados por parte",
          all(s["chars_propio"] == len(s["texto"])
              and s["sha256_propio"] == _h.sha256(
                  s["texto"].encode("utf-8")).hexdigest()
              and s["sub_chunk"] == {"parte": k, "de": len(subs),
                                     "id_unidad_completa": c["id"],
                                     "chars_unidad_completa": c["chars_propio"],
                                     "familia_items": "num"}
              for k, s in enumerate(subs, 1)))
    # las partes son consumibles por el pipeline E1 tal cual
    pa_orig = set(comun_e1.puntos_admitidos(c))
    ok_pipeline = True
    for s in subs:
        ok_pipeline = ok_pipeline and set(comun_e1.puntos_admitidos(s)) == pa_orig
        kw = prompt_e1.build_request_kwargs(s, model="claude-haiku-4-5")
        ok_pipeline = ok_pipeline and kw["max_tokens"] == prompt_e1.MAX_OUTPUT_TOKENS
    msj2 = prompt_e1.build_user_message(subs[1])
    check("P5 caso real: puntos admitidos idénticos a la unidad completa y "
          "requests E1 construibles; el chapeau viaja en el contexto heredado "
          "del mensaje",
          ok_pipeline and "[encabezado | punto 1.5]" in msj2
          and "1.5. Modelos de formularios." in msj2)

    # sintético: unidad sobre el umbral SIN ítems → intacta y DECLARADA
    gigante = "S9. Tabla.\n" + ("FILA SIN MARCADOR DE ITEM\n" * 2000)
    cx = _chunk_fx(gigante, unidad="S9")
    cx["tipo"] = "seccion_sin_puntos"
    out, rep = correr_e0.subdividir_unidades_grandes([cx])
    check("P5 sintético sin ítems: no se parte y queda declarado "
          "(sin_items_detectables)",
          out == [cx] and rep["particiones"] == []
          and rep["no_particionables"] == [
              {"id": cx["id"], "chars_propio": cx["chars_propio"],
               "motivo": "sin_items_detectables"}])

    # sintético: ítems por inciso a)…, con un ítem gigante como parte propia
    item_gigante = "b) " + "x" * (correr_e0.OBJETIVO_CHARS_PARTE + 100)
    texto = "\n".join(["2.4. Requisitos.", "Chapeau de la lista:"]
                      + [f"a) ítem chico {i}" for i in range(3)]
                      + [item_gigante]
                      + [f"c) cierre {i}" for i in range(3)])
    cy = _chunk_fx(texto, unidad="2.4")
    out, rep = correr_e0.subdividir_unidades_grandes(
        [cy], umbral=len("2.4. Requisitos.\nChapeau de la lista:"))
    check("P5 sintético con ítems: parte por incisos, el ítem que excede el "
          "objetivo queda como parte propia y nada se pierde",
          len(out) >= 3
          and any(s["texto"] == item_gigante for s in out)
          and "\n".join(s["texto"] for s in out) == texto)

    # los mini-chunks jamás se particionan (aunque midieran de más)
    mini = dict(_chunk_fx("bloque\n" + "z" * 30000, unidad="3.1"))
    mini["tipo"] = "mini_chunk"
    out, rep = correr_e0.subdividir_unidades_grandes([mini])
    check("P5 mini-chunks fuera del alcance de la partición",
          out == [mini] and not rep["particiones"]
          and not rep["no_particionables"])


# ========================================================================= #
# P6 — candados                                                             #
# ========================================================================= #

def p6_candados() -> None:
    check("P6 prefijo E1 byte-idéntico: PREFIJO_HASH sellado 4793d6152608",
          prompt_e1.PREFIJO_HASH == "4793d6152608")
    check("P6 namespace E1 intacto (mismas claves de caché de producción)",
          cliente_e1.namespace_e1()
          == "e1_extraccion|cv=e1-extractor-v1-p4793d6152608|think=0")
    check("P6 techo del request base E1 intacto (8.192)",
          prompt_e1.MAX_OUTPUT_TOKENS == 8192)
    check("P6 techo del ratchet E3 intacto (16.384) y reintento por corte == "
          "su doble (32.768)",
          RC.MAX_TOKENS_REINTENTO == 16384
          and cliente_e1.MAX_TOKENS_REINTENTO_CORTE == 32768
          == 2 * RC.MAX_TOKENS_REINTENTO)


# ========================================================================= #

def main() -> int:
    with tempfile.TemporaryDirectory(prefix="selftest_ub53_") as td:
        tmp = Path(td)
        p1_reintento()
        p2_persistencia(tmp)
        p3_runner(tmp)
        p4_tope_compartido(tmp)
        p5_subchunking()
        p6_candados()

    print(f"\nSELFTEST U-B5.3: {_n - _fallos}/{_n}"
          + ("" if not _fallos else f"  ({_fallos} FALLOS)"), flush=True)
    return 0 if not _fallos else 1


if __name__ == "__main__":
    sys.exit(main())
