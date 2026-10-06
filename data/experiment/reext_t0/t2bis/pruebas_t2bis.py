"""Pruebas sintéticas de las ramas nuevas de T2-bis (USD 0, sin red), sobre una COPIA del repo, con clientes stub y el
fase_e1 real del runner (como selftest_ub53, P8). Uso: python -B pruebas_t2bis.py <copia>"""
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
sys.path[0] = str(RUNNER.parent)
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
    def __init__(self, ti):
        self.content, self.stop_reason = [B(ti)], "tool_use"
        self.usage = type("U", (), {"input_tokens": 0, "output_tokens": 0, "cache_creation_input_tokens": 0,
                                    "cache_read_input_tokens": 0})()


MAL = {"entities": {"no": "lista"}, "relations": {}}          # contenedores no-lista: rechazo de chunk por forma


class StubForma:
    """create devuelve MAL; el reintento por forma devuelve, en orden, las salidas dadas; registra el sufijo."""

    def __init__(self, reintentos):
        self.messages, self.gasto_usd, self.r = self, 0.0, list(reintentos)
        self.pedidos = []

    def create(self, **kw):
        self.pedidos.append(("create", None, kw.get("temperature")))
        return Resp(MAL)

    def crear_reintento_forma(self, doc=None, sufijo=cliente_e1.SUFIJO_REINTENTO_FORMA, **kw):
        self.pedidos.append(("reintento_forma", sufijo, kw.get("temperature")))
        return Resp(self.r.pop(0))

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
    return regs, json.loads((sal / chunk["to"] / "resumen_e1.json").read_text(encoding="utf-8"))


X = COPIA / "data/experiment/reextraccion_v2/e0_chunking"
cid = "ctacte::3.2.4"
ch_r2b = next(c for c in json.loads((X / "salida_tanda0_r2b/chunks_ctacte.json").read_text(encoding="utf-8")) if c["id"] == cid)
ch_v3 = next(c for c in json.loads((X / "salida_tanda0/chunks_ctacte.json").read_text(encoding="utf-8")) if c["id"] == cid)
r2b, v3 = perfil_e1.perfil("r2b"), perfil_e1.perfil("v3_b54")
OK = {"entities": [{"local_id": "to", "type": "TextoOrdenado", "label": "TO", "punto": ch_r2b["unidad"]}],
      "relations": [], "omisiones": []}
ns2 = cliente_e1.namespace_e1(prefijo_hash=r2b.prefijo_hash_para_namespace, sufijo=cliente_e1.SUFIJO_REINTENTO_FORMA_2)

with tempfile.TemporaryDirectory(prefix="t2bis_") as td:
    tmp = Path(td)
    # 1. r2b: el primer reintento vuelve mal formado, el segundo bien
    cli = StubForma([MAL, OK])
    regs, res = fase_e1_un_chunk(tmp, "a", ch_r2b, r2b, cli)
    rf = regs[-1].get("reintento_forma", {})
    check("r2b: mal formada, reintento 1 mal formado → segundo reintento -rforma2 con temperatura 1; queda válida",
          [p[:2] for p in cli.pedidos] == [("create", None), ("reintento_forma", "-rforma1"), ("reintento_forma", "-rforma2")]
          and [p[2] for p in cli.pedidos] == [0, 1, 1] and regs[-1]["error"] is None
          and rf.get("reintento_2", {}).get("namespace") == ns2 and "intento_2" in rf["reintento_2"] and "intento_1" in rf,
          json.dumps({"pedidos": cli.pedidos, "error": regs[-1]["error"]}, ensure_ascii=False))
    check("r2b: el resumen de E1 lista la unidad con segundo reintento y no la da por agotada",
          res["reintentos_forma"].get("con_segundo_reintento") == [cid] and res["reintentos_forma"]["agotados"] == [])
    # 2. r2b: los dos reintentos mal formados
    cli = StubForma([MAL, MAL])
    regs, res = fase_e1_un_chunk(tmp, "b", ch_r2b, r2b, cli)
    check("r2b: los dos reintentos mal formados → salida_mal_formada_tras_reintento, una sola vez cada uno, "
          "con las tres salidas en el registro",
          len(cli.pedidos) == 3 and regs[-1]["error"] == RC.ERROR_FORMA_TRAS_REINTENTO
          and "intento_1" in regs[-1]["reintento_forma"] and "intento_2" in regs[-1]["reintento_forma"]["reintento_2"]
          and regs[-1]["tool_input_crudo"] == MAL and res["reintentos_forma"]["agotados"] == [cid],
          json.dumps({"pedidos": len(cli.pedidos), "error": regs[-1]["error"]}, ensure_ascii=False))
    # 3. r2b: el primer reintento bien → sin segundo (como siempre)
    cli = StubForma([OK])
    regs, res = fase_e1_un_chunk(tmp, "c", ch_r2b, r2b, cli)
    check("r2b: reintento 1 bien formado → sin segundo reintento, registro sin reintento_2 ni clave nueva en el resumen",
          len(cli.pedidos) == 2 and "reintento_2" not in regs[-1]["reintento_forma"]
          and "con_segundo_reintento" not in res["reintentos_forma"])
    # 4. perfil sellado con el camino r2: sin segundo reintento
    cli = StubForma([MAL, OK])
    regs, res = fase_e1_un_chunk(tmp, "d", ch_v3, v3, cli)
    check("v3_b54 con el camino r2: reintento 1 mal formado → sin segundo reintento (salida_mal_formada_tras_reintento)",
          len(cli.pedidos) == 2 and regs[-1]["error"] == RC.ERROR_FORMA_TRAS_REINTENTO
          and "reintento_2" not in regs[-1]["reintento_forma"])
    # 5. reabrir_fase
    sal = tmp / "estado"; sal.mkdir()
    est = RC.Estado(sal)
    est.d["fases_cerradas"] = {"cap:e1": {"gasto_usd": 5.660739, "resumen": {"n": 462}},
                               "cap:e3": {"gasto_usd": 4.724213, "resumen": {"n": 460}}}
    est.persistir()
    a = est.reabrir_fase("cap:e1")
    check("reabrir_fase: saca la fase cerrada y la deja como fase_actual con su gasto como previo; queda en reaperturas",
          a and "cap:e1" not in est.d["fases_cerradas"] and est.d["fase_actual"]["gasto_previo_usd"] == 5.660739
          and est.d["reaperturas"][0]["fase_cerrada"]["gasto_usd"] == 5.660739)
    b = est.reabrir_fase("cap:e3")
    check("reabrir_fase: con otra fase en curso no hace nada (no pisa su gasto)",
          b is False and "cap:e3" in est.d["fases_cerradas"] and est.d["fase_actual"]["key"] == "cap:e1")
    previo = est.abrir_fase("cap:e1"); est.tick(0.25, 2); est.cerrar_fase("cap:e1", {"n": 463})
    check("abrir_fase conserva el gasto previo y cerrar_fase cierra con previo + nuevo",
          previo == 5.660739 and est.d["fases_cerradas"]["cap:e1"]["gasto_usd"] == round(5.660739 + 0.25, 6))
    c = est.reabrir_fase("cap:e9")
    check("reabrir_fase: una fase que no está cerrada no se toca", c is False)
    est2 = RC.Estado(sal)
    check("Estado persistido: la reapertura y el cierre nuevo quedan en estado_corpus.json",
          est2.d["fases_cerradas"]["cap:e1"]["gasto_usd"] == round(5.910739, 6) and len(est2.d["reaperturas"]) == 1)

n_ok = sum(r["ok"] for r in R)
print(f"PRUEBAS T2-bis: {n_ok}/{len(R)}")
Path(sys.argv[2]).write_text(json.dumps(R, ensure_ascii=False, indent=1), encoding="utf-8") if len(sys.argv) > 2 else None
