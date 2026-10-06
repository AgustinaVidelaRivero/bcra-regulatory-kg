"""U-REEXT-T0, T2-ter: pruebas sintéticas de la reparación acotada de la salida sin la clave relations (USD 0, sin
red), sobre una COPIA del repo, con clientes stub y el fase_e1 real del runner (como pruebas_t2bis.py).
Uso: python -B pruebas_t2ter.py <copia> [<salida_json>]"""
import contextlib
import importlib.util
import io
import json
import os
import sys
import tempfile
from pathlib import Path

COPIA = Path(sys.argv[1]).resolve()
os.chdir(COPIA)
RUNNER = COPIA / "data/experiment/reextraccion_v2/corpus_v2/runner_corpus.py"
sys.path[0] = str(RUNNER.parent)          # modo script, como `python runner_corpus.py`
spec = importlib.util.spec_from_file_location("runner_corpus", RUNNER)
RC = importlib.util.module_from_spec(spec); sys.modules["runner_corpus"] = RC; spec.loader.exec_module(RC)
import cliente_e1, perfil_e1   # noqa: E402  (del path que armó el runner)

R = []


def check(nombre, ok, det=""):
    R.append({"prueba": nombre, "ok": bool(ok), "detalle": det})
    print(("ok  " if ok else "FAIL"), nombre, det)


class B:
    def __init__(self, ti):
        self.type, self.name, self.input = "tool_use", "extraer_kg_e1", ti


class Resp:
    def __init__(self, ti, stop="tool_use"):
        self.content, self.stop_reason = [B(ti)], stop
        self.usage = type("U", (), {"input_tokens": 0, "output_tokens": 0, "cache_creation_input_tokens": 0,
                                    "cache_read_input_tokens": 0})()


class Stub:
    """create devuelve `primera`; cada reintento por forma, en orden, las salidas dadas; registra cada pedido."""

    def __init__(self, primera, reintentos, stop_ultima="tool_use"):
        self.messages, self.gasto_usd, self.primera, self.r = self, 0.0, primera, list(reintentos)
        self.stop_ultima, self.pedidos = stop_ultima, []

    def create(self, **kw):
        self.pedidos.append(("create", None))
        return Resp(self.primera)

    def crear_reintento_forma(self, doc=None, sufijo=cliente_e1.SUFIJO_REINTENTO_FORMA, **kw):
        self.pedidos.append(("reintento_forma", sufijo))
        ti = self.r.pop(0)
        return Resp(ti, self.stop_ultima if not self.r else "tool_use")

    def resumen(self):
        return {"llamadas": len(self.pedidos)}


def fase_e1_un_chunk(tmp, nombre, chunk, perfil, cli):
    e0, sal = tmp / f"e0_{nombre}", tmp / f"sal_{nombre}"
    e0.mkdir(); (sal / chunk["to"]).mkdir(parents=True)
    (e0 / f"chunks_{chunk['to']}.json").write_text(json.dumps([chunk], ensure_ascii=False), encoding="utf-8")
    orig = (RC.PERFIL, RC.PERFIL_R2, RC.E0_DIR, RC.ESTIMADO_USD)
    RC.PERFIL, RC.PERFIL_R2, RC.E0_DIR = perfil, True, e0
    RC.ESTIMADO_USD = {**RC.ESTIMADO_USD, chunk["to"]: {"e1": 0.0, "e3": 0.0}}
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            RC.fase_e1(chunk["to"], cli, RC.Estado(sal), sal, None, None, None)
    finally:
        RC.PERFIL, RC.PERFIL_R2, RC.E0_DIR, RC.ESTIMADO_USD = orig
    regs = [json.loads(x) for x in (sal / chunk["to"] / "extracciones_e1.jsonl").read_text(encoding="utf-8").splitlines()]
    return regs[-1], json.loads((sal / chunk["to"] / "resumen_e1.json").read_text(encoding="utf-8"))


X = COPIA / "data/experiment/reextraccion_v2/e0_chunking"
cid = "ctacte::3.2.4"
ch_r2b = next(c for c in json.loads((X / "salida_tanda0_r2b/chunks_ctacte.json").read_text(encoding="utf-8")) if c["id"] == cid)
ch_v3 = next(c for c in json.loads((X / "salida_tanda0/chunks_ctacte.json").read_text(encoding="utf-8")) if c["id"] == cid)
r2b, v3 = perfil_e1.perfil("r2b"), perfil_e1.perfil("v3_b54")
ENT = [{"local_id": "to", "type": "TextoOrdenado", "label": "TO", "punto": ch_r2b["unidad"]}]
SIN_REL = {"entities": ENT}                                # la forma de las 12 salidas mal formadas de T2 y T2-bis
SIN_ENT = {"relations": [], "omisiones": []}               # sin la clave entities
REL_MAL = {"entities": ENT, "relations": {"no": "lista"}}  # relations presente, pero no lista

with tempfile.TemporaryDirectory(prefix="t2ter_") as td:
    tmp = Path(td)
    # 1. las tres salidas sin relations → reparada la del segundo reintento
    cli = Stub(SIN_REL, [SIN_REL, SIN_REL])
    reg, res = fase_e1_un_chunk(tmp, "a", ch_r2b, r2b, cli)
    check("r2b: tres salidas sin relations → reparada la última (-rforma2), sin error, con relations = [] y marcada",
          reg["error"] is None and reg["reparacion_forma"] == {"motivo": "relations_ausente", "intento": "-rforma2"}
          and reg["tool_input_crudo"] == {**SIN_REL, "relations": []}
          and not any(x.get("nivel") == "chunk" for x in reg["validacion"]["rechazos"]),
          json.dumps({"error": reg["error"], "reparacion": reg.get("reparacion_forma")}, ensure_ascii=False))
    check("r2b: la reparación no hace pedidos (tres pedidos: primer intento, -rforma1 y -rforma2)",
          cli.pedidos == [("create", None), ("reintento_forma", "-rforma1"), ("reintento_forma", "-rforma2")])
    check("r2b: el resumen de E1 la cuenta en reparadas_forma y no en agotados",
          res.get("reparadas_forma") == {"motivo": "relations_ausente", "unidades": [cid]}
          and res["reintentos_forma"]["agotados"] == [] and res["reintentos_forma"]["con_segundo_reintento"] == [cid])
    # 2. sin entities → error como hoy
    cli = Stub(SIN_ENT, [SIN_ENT, SIN_ENT])
    reg, res = fase_e1_un_chunk(tmp, "b", ch_r2b, r2b, cli)
    check("r2b: salidas sin entities → salida_mal_formada_tras_reintento, sin reparar",
          reg["error"] == RC.ERROR_FORMA_TRAS_REINTENTO and "reparacion_forma" not in reg
          and "reparadas_forma" not in res and res["reintentos_forma"]["agotados"] == [cid])
    # 3. relations presente pero no lista → error como hoy
    cli = Stub(REL_MAL, [REL_MAL, REL_MAL])
    reg, _ = fase_e1_un_chunk(tmp, "c", ch_r2b, r2b, cli)
    check("r2b: relations presente pero no lista → error, sin reparar",
          reg["error"] == RC.ERROR_FORMA_TRAS_REINTENTO and "reparacion_forma" not in reg)
    # 4. el último reintento corta → error como hoy
    cli = Stub(SIN_REL, [SIN_REL, SIN_REL], stop_ultima="max_tokens")
    reg, _ = fase_e1_un_chunk(tmp, "d", ch_r2b, r2b, cli)
    check("r2b: el último reintento corta por max_tokens → error, sin reparar",
          reg["error"] == RC.ERROR_FORMA_TRAS_REINTENTO and "reparacion_forma" not in reg)
    # 5. el primer reintento sale bien → sin segundo ni reparación (como siempre)
    ok = {"entities": ENT, "relations": [], "omisiones": []}
    cli = Stub(SIN_REL, [ok])
    reg, res = fase_e1_un_chunk(tmp, "e", ch_r2b, r2b, cli)
    check("r2b: el reintento sale bien → sin segundo reintento ni reparación; el resumen sin reparadas_forma",
          reg["error"] is None and "reparacion_forma" not in reg and "reparadas_forma" not in res and len(cli.pedidos) == 2)
    # 6. perfil sellado con el camino r2: sin reparación
    ENT3 = [{"local_id": "to", "type": "TextoOrdenado", "label": "TO", "punto": ch_v3["unidad"]}]
    cli = Stub({"entities": ENT3}, [{"entities": ENT3}])
    reg, res = fase_e1_un_chunk(tmp, "f", ch_v3, v3, cli)
    check("v3_b54 con el camino r2: salida sin relations → error, sin reparar (la reparación es del perfil r2b)",
          reg["error"] == RC.ERROR_FORMA_TRAS_REINTENTO and "reparacion_forma" not in reg and "reparadas_forma" not in res)

n_ok = sum(r["ok"] for r in R)
print(f"PRUEBAS T2-ter: {n_ok}/{len(R)}")
if len(sys.argv) > 2:
    Path(sys.argv[2]).write_text(json.dumps(R, ensure_ascii=False, indent=1), encoding="utf-8")
