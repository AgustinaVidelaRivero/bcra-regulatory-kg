"""U-R2-CODIGO-2, C2 — casos sintéticos de los puntos b, k y o (USD 0, sin API ni Neo4j). Solo escribe --out.

  B  reintento ante una salida de E1 mal formada (punto b), con `runner_corpus.fase_e1` y un cliente simulado, sobre
     las 4 unidades de diez (`cap::5.3.2.3`, `ext::6.5.3`, `ric::6.3`, `ctacte::5.6.1`; las 3 de desarrollo son las
     tres primeras, con el mismo crudo): el chunk de la E0 legada, el perfil de E1 de los grafos r2a (`v3_b54`) y el
     crudo mal formado guardado (`corpus_tanda0/salida_dirigida`) como primera respuesta.
       B1  perfil r2 y reintento bien formado: dos requests idénticos, la unidad deja de quedar sin validación y el
           registro lleva `reintento_forma` (namespace propio, motivo, intento 1);
       B2  perfil r2 y reintento mal formado: la unidad queda con el error declarado y en la lista del resumen;
       B3  sin el perfil r2: una sola llamada, sin `reintento_forma` (como hoy);
       B4  claves de la caché local, con la db de E1 abierta en modo inmutable: la del request base está en la db
           con el mismo crudo; la del reintento (namespace `…-rforma1`) es otra y no está.
  O  la lista de umbrales se completa en r2b (punto o): un nodo con el elemento del límite relativo que deja
     validador_r2 y un tramo de E1 con cuantía conserva los dos; en r2a la lista se reemplaza (como en los grafos
     sellados).
  K  el tramo compuesto en el ensamblado r2b (punto k): el elemento de la cuantía del ítem toma el marcador del
     encabezado.

Uso, desde la raíz de una copia del repo:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/r2_codigo2/c2_sinteticos.py \
      --out data/experiment/r2_codigo2/salidas/c2_sinteticos.json
"""
from __future__ import annotations

import argparse
import contextlib
import io
import json
import sqlite3
import tempfile
import urllib.parse
from collections import OrderedDict
from pathlib import Path

import c1_comun as K

import comun_e1                         # noqa: E402  (en el path por ensamblar_tanda0)
import cliente_e1                       # noqa: E402
import runner_corpus as RC              # noqa: E402

ENS = K.ENS
REX = K.RAIZ / K.REX
DB_E1 = REX / "e1_extractor" / "cache" / "e1_extraccion.db"
UNIDADES = ("cap::5.3.2.3", "ext::6.5.3", "ric::6.3", "ctacte::5.6.1")
RES: list[tuple[str, str, bool, str]] = []


def check(grupo: str, nombre: str, ok: bool, detalle: str = "") -> None:
    RES.append((grupo, nombre, bool(ok), detalle))
    print(f"  [{'PASS' if ok else 'FAIL'}] {grupo} {nombre}" + (f" — {detalle}" if detalle and not ok else ""))


class _R:
    def __init__(self, ti):
        self.stop_reason = "tool_use"
        self.content = [type("B", (), {"type": "tool_use", "input": ti})()]
        self.usage = type("U", (), {"input_tokens": 0, "output_tokens": 0, "cache_creation_input_tokens": 0,
                                    "cache_read_input_tokens": 0})()


class ClienteForma:
    """Primera respuesta: el crudo mal formado; el reintento (segunda llamada): `segunda`."""

    def __init__(self, crudo, segunda):
        self.crudo, self.segunda = crudo, segunda
        self.requests: list[dict] = []
        self.messages = self
        self.gasto_usd = 0.0

    def create(self, **kw):
        self.requests.append(kw)
        return _R(self.crudo if len(self.requests) == 1 else self.segunda)

    def resumen(self) -> dict:
        return {"llamadas": len(self.requests)}


@contextlib.contextmanager
def runner_en(tmp: Path, to: str, chunk: dict, r2: bool, perfil):
    e0 = tmp / "e0"
    e0.mkdir(parents=True, exist_ok=True)
    (e0 / f"chunks_{to}.json").write_text(json.dumps([chunk], ensure_ascii=False), encoding="utf-8")
    orig = (RC.PERFIL, RC.PERFIL_R2, RC.E0_DIR, RC.ESTIMADO_USD)
    RC.PERFIL, RC.PERFIL_R2, RC.E0_DIR = perfil, r2, e0
    # el checkpoint del runner proyecta el gasto con la estimación del manifiesto; acá, cero
    RC.ESTIMADO_USD = {**RC.ESTIMADO_USD, to: {"e1": 0.0, "e3": 0.0}}
    try:
        yield
    finally:
        RC.PERFIL, RC.PERFIL_R2, RC.E0_DIR, RC.ESTIMADO_USD = orig


def correr_e1(to: str, chunk: dict, r2: bool, perfil, cli) -> tuple[list[dict], dict]:
    with tempfile.TemporaryDirectory() as d, runner_en(Path(d), to, chunk, r2, perfil):
        sal = Path(d) / "salida"
        (sal / to).mkdir(parents=True)
        with contextlib.redirect_stdout(io.StringIO()):
            RC.fase_e1(to, cli, RC.Estado(sal), sal, None, None, None)
        regs = [json.loads(x) for x in (sal / to / "extracciones_e1.jsonl").read_text(encoding="utf-8").splitlines()]
        resumen = json.loads((sal / to / "resumen_e1.json").read_text(encoding="utf-8"))
    return regs, resumen


def canon(kw: dict) -> str:
    return cliente_e1.lc.canonical_request(kw)


def grupo_b() -> OrderedDict:
    man = json.loads((K.RAIZ / K.GRAFOS["diez"]["manifiesto"]).read_text(encoding="utf-8"))
    perfil = ENS.perfil_e1.perfil(man["perfil_e1"])
    ns = cliente_e1.namespace_e1(prefijo_hash=perfil.prefijo_hash_para_namespace)
    ns_r = cliente_e1.namespace_e1(prefijo_hash=perfil.prefijo_hash_para_namespace,
                                   sufijo=cliente_e1.SUFIJO_REINTENTO_FORMA)
    check("B", "el namespace del reintento es el base con el sufijo «-rforma1» en el code_ver",
          ns_r == ns.replace(f"-p{perfil.prefijo_hash_para_namespace}|",
                             f"-p{perfil.prefijo_hash_para_namespace}-rforma1|"), f"{ns} {ns_r}")
    check("B", "sin sufijo, el namespace de siempre", cliente_e1.namespace_e1(
        prefijo_hash=perfil.prefijo_hash_para_namespace, sufijo="") == ns)
    con = sqlite3.connect(f"file:{urllib.parse.quote(str(DB_E1.resolve()))}?mode=ro&immutable=1", uri=True)
    filas = []
    try:
        for cid in UNIDADES:
            to = cid.split("::")[0]
            chunk = next(c for c in comun_e1.cargar_chunks((to,), e0_dir=K.RAIZ / K.E0_LEGADA) if c["id"] == cid)
            crudo = next(json.loads(x)["tool_input_crudo"] for x in
                         (K.RAIZ / K.ENTRADA / to / "extracciones_e1.jsonl").read_text(encoding="utf-8").splitlines()
                         if x.strip() and json.loads(x)["chunk_id"] == cid)
            buena = {"entities": [{"local_id": "to", "type": "TextoOrdenado", "label": "TO", "punto": chunk["unidad"]
                                   if chunk["tipo"] != "mini_chunk" else chunk["unidad"]}],
                     "relations": [], "omisiones_no_prosa": []}
            kw = perfil.build_request_kwargs(chunk, model=RC.MODEL_E1)
            # B1
            cli = ClienteForma(crudo, buena)
            regs, resumen = correr_e1(to, chunk, True, perfil, cli)
            r = regs[0]
            rech = [x for x in (r.get("validacion") or {}).get("rechazos", []) if x["nivel"] == "chunk"]
            b1 = (len(cli.requests) == 2 and canon(cli.requests[0]) == canon(cli.requests[1]) == canon(kw)
                  and r["error"] is None and not rech and r["tool_input_crudo"] == buena
                  and r["reintento_forma"]["namespace"] == ns_r
                  and r["reintento_forma"]["motivo"] in RC.MOTIVOS_FORMA_E1
                  and r["reintento_forma"]["intento_1"]["tool_input_crudo"] == crudo
                  and resumen.get("reintentos_forma") == {"unidades": [cid], "agotados": []}
                  and "errores_definitivos" not in resumen)
            check("B1", f"{cid}: dispara el reintento con el mismo request; bien formado, deja de quedar sin validación",
                  b1, json.dumps({"requests": len(cli.requests), "error": r["error"], "rechazos": rech,
                                  "resumen": resumen.get("reintentos_forma")}, ensure_ascii=False))
            # B2
            cli2 = ClienteForma(crudo, crudo)
            regs2, resumen2 = correr_e1(to, chunk, True, perfil, cli2)
            r2 = regs2[0]
            check("B2", f"{cid}: agotado el reintento, error declarado y lista del resumen",
                  len(cli2.requests) == 2 and r2["error"] == RC.ERROR_FORMA_TRAS_REINTENTO
                  and {"chunk_id": cid, "error": RC.ERROR_FORMA_TRAS_REINTENTO} in resumen2.get("errores_definitivos", [])
                  and resumen2.get("reintentos_forma") == {"unidades": [cid], "agotados": [cid]},
                  json.dumps({"error": r2["error"], "resumen": {k: resumen2.get(k) for k in
                                                                ("errores_definitivos", "reintentos_forma")}},
                             ensure_ascii=False))
            # B3
            cli3 = ClienteForma(crudo, buena)
            regs3, resumen3 = correr_e1(to, chunk, False, perfil, cli3)
            r3 = regs3[0]
            check("B3", f"{cid}: sin el perfil r2, una llamada con el request de siempre y sin reintento (como hoy)",
                  len(cli3.requests) == 1 and canon(cli3.requests[0]) == canon(kw) and r3["error"] is None
                  and "reintento_forma" not in r3 and "reintentos_forma" not in resumen3
                  and set(r3) == {"chunk_id", "unidad", "tipo_unidad", "titulo", "stop_reason", "error", "usage",
                                  "tool_input_crudo", "validacion"})
            # B4
            clave = cliente_e1.lc.compute_key(ns, canon(kw))
            clave_r = cliente_e1.lc.compute_key(ns_r, canon(kw))
            fila = con.execute("select raw_json from cache where key = ?", (clave,)).fetchone()
            crudo_db = None
            if fila is not None:
                crudo_db = next((b.get("input") for b in json.loads(fila[0]).get("content") or []
                                 if isinstance(b, dict) and b.get("type") == "tool_use"), None)
            en_db_r = con.execute("select 1 from cache where key = ?", (clave_r,)).fetchone() is not None
            check("B4", f"{cid}: la clave base está en la db con el mismo crudo; la del reintento es otra y no está",
                  fila is not None and crudo_db == crudo and clave_r != clave and not en_db_r)
            filas.append(OrderedDict([("chunk_id", cid), ("motivo", r["reintento_forma"]["motivo"] if b1 else None),
                                      ("clave_base", clave), ("clave_reintento", clave_r),
                                      ("clave_base_en_la_db", fila is not None), ("clave_reintento_en_la_db", en_db_r)]))
    finally:
        con.close()
    return OrderedDict([("perfil", perfil.nombre), ("namespace", ns), ("namespace_reintento", ns_r), ("unidades", filas)])


def grupos_o_k() -> OrderedDict:
    """Puntos o y k, con llenar_umbrales_r2 sobre nodos sintéticos anclados en chunks reales de cla (la E0 del
    manifiesto r2a de desarrollo)."""
    cfg = K.GRAFOS["desarrollo"]
    man = ENS.MC.cargar(K.RAIZ / cfg["manifiesto"])
    perfil = ENS.perfil_e1.perfil(man.perfil_e1)
    M = ENS.E4.modulo_modelos_r2()
    V = ENS.E4.modulo_validador_r2()
    import reglas_comparacion as RCMP   # noqa: PLC0415
    cat = ENS.E4.catalogo_r2()
    _, pol = RC.validador_perfil_r2(perfil)
    out = OrderedDict()
    with tempfile.TemporaryDirectory() as tmp:
        plan = ENS.plan_redirecciones_r2(man, perfil, K.RAIZ / K.ENTRADA, Path(tmp) / "r2", cat, M)
        with ENS.redirigido(plan):
            prov = {"to": "cla", "punto": "5.1.1.1", "chunk_id": "cla::5.1.1.1", "rol_documental": "contenido"}
            relativo = V.elemento_umbral_relativo("no podrán superar el patrimonio neto de la entidad", "no")
            tramo = "superen el equivalente a dos veces el importe de referencia establecido en el punto 3.7."

            def kg_con(umbrales):
                n = {"id": "Restriccion_sintetica", "type": "Restriccion", "label": "x",
                     "properties": {"descripcion": "Restricción sintética", **({"umbrales": umbrales} if umbrales else {})},
                     "provenance": dict(prov), "provenances": [dict(prov)]}
                return {"nodes": [n], "edges": []}
            res = {}
            for fase in ("r2b", "r2a"):
                kg = kg_con([relativo])
                r = ENS.llenar_umbrales_r2(kg, {"Restriccion_sintetica": [tramo]}, {}, M, V, RCMP, pol, fase)
                res[fase] = (kg["nodes"][0]["properties"].get("umbrales") or [], r["resumen"])
            u_b, u_a = res["r2b"][0], res["r2a"][0]
            check("O", "r2b: la lista conserva el elemento del límite relativo y suma el de cuantía",
                  len(u_b) == 2 and u_b[0] == relativo and u_b[1].get("valor") == "2"
                  and res["r2b"][1].get("elementos_previos_conservados") == 1, json.dumps(u_b, ensure_ascii=False))
            check("O", "r2a: la lista se reemplaza, como en los grafos sellados",
                  len(u_a) == 1 and u_a[0].get("valor") == "2" and "elementos_previos_conservados" not in res["r2a"][1])
            check("O", "los elementos validan con ElementoUmbral",
                  all(M.ElementoUmbral.model_validate(x) for x in u_b))
            out["o"] = {"r2b": u_b, "r2a": u_a}
            # k
            compuesto = "deberán observar los siguientes límites mínimos: […] multiplicar 6% por los activos ponderados"
            for fase in ("r2b", "r2a"):
                kg = kg_con(None)
                ENS.llenar_umbrales_r2(kg, {"Restriccion_sintetica": [compuesto]}, {}, M, V, RCMP, pol, fase)
                res[fase] = kg["nodes"][0]["properties"].get("umbrales") or []
            check("K", "r2b: el elemento de la cuantía del ítem toma «mínimos» del encabezado del tramo compuesto",
                  len(res["r2b"]) == 1 and res["r2b"][0]["comparacion"] == "minimo_inclusivo"
                  and res["r2b"][0]["regla_comparacion"] == "encabezado:compuesta:adyacencia_minimo",
                  json.dumps(res["r2b"], ensure_ascii=False))
            check("K", "la regla del encabezado rige también en r2a (no depende de la fase)",
                  [x["regla_comparacion"] for x in res["r2a"]] == ["encabezado:compuesta:adyacencia_minimo"])
            out["k"] = {"tramo": compuesto, "r2b": res["r2b"]}
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    out = OrderedDict([("b", grupo_b()), ("o_k", grupos_o_k())])
    out["controles"] = [{"grupo": g, "nombre": n, "ok": b} for g, n, b, _ in RES]
    out["resultado"] = f"{sum(1 for x in RES if x[2])}/{len(RES)}"
    K.escribir_json(K.RAIZ / a.out, out)
    print("RESULTADO", out["resultado"])


if __name__ == "__main__":
    main()
