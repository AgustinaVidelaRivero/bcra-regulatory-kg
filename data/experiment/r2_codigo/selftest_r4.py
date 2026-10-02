"""U-R2-CODIGO, R4 — selftest sin API ni red. USD 0.

Grupos:
  B1  BKL-0030 (a): el request del reintento por corte del perfil r2 pasa la
      guarda del SDK (anthropic 0.100.0) y el de los perfiles existentes
      (32.768) no, con los tres casos del laudo de r2 (`cap::3.1.14.1`,
      `cap::4.2.1.2`, `cap::4.3.3.1`), armados con el perfil de E1 del
      manifiesto (`v3_b54`) sobre la E0 de la tanda 0. El SDK corre contra un
      transporte local (httpx.MockTransport): ningún byte sale de la máquina.
  B2  BKL-0030 (a), costo: la clave de caché del reintento a 16.384 de los tres
      casos está en la caché de E1 (re-extracción dirigida de la tanda 0), que
      se abre en solo lectura (immutable=1). Sin la db en disco, NO_VERIFICABLE.
  B3  BKL-0030 (b) y agregado 7: la unidad que corta también en el reintento
      se parte (runner_corpus.fase_e1 con --perfil-r2 y un cliente simulado que
      corta en la unidad y responde en las partes), sin cortar ningún bloque
      [TABLA … FIN TABLA] (`cap::4.2.1.2` de e0-r2, tres tablas); las partes
      se extraen en el mismo pase, quedan en particiones_por_corte.json y
      reemplazan a la unidad en la compactación. Sin el perfil r2, el mismo
      corte es error definitivo y el reintento es a 32.768.
  B4  R4.a: la clave de fusión del perfil r2 (`e2_lib.entity_slug_r2`).
  B5  agregado 8: el pie desde la línea «Versión» de e0-r2 (e0_lib).

Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/r2_codigo/selftest_r4.py [--e0-r2 <dir>]
"""

from __future__ import annotations

import argparse
import contextlib
import io
import json
import sqlite3
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
for p in (REX / "corpus_v2", REX, REX / "e0_chunking", REX / "e1_extractor", REX / "e3_verificador",
          REX / "e2_reduce", REPO / "data" / "experiment" / "grafo_v2" / "code"):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))
import cliente_e1  # noqa: E402
import perfil_e1  # noqa: E402
import correr_e0  # noqa: E402
import e0_lib as E0  # noqa: E402
import e2_lib  # noqa: E402
import runner_corpus as RC  # noqa: E402

E0_TANDA0 = REX / "e0_chunking" / "salida_tanda0"
DB_E1 = REX / "e1_extractor" / "cache" / "e1_extraccion.db"
CASOS = ("cap::3.1.14.1", "cap::4.2.1.2", "cap::4.3.3.1")
RES: list[tuple[str, str]] = []


def check(nombre: str, ok, detalle: str = "") -> None:
    estado = "NO_VERIFICABLE" if ok is None else "PASS" if ok else "FAIL"
    RES.append((nombre, estado))
    print(f"  [{estado}] {nombre}" + (f" — {detalle}" if detalle else ""))


def chunks_cap(d: Path) -> dict[str, dict]:
    x = json.loads((d / "chunks_cap.json").read_text(encoding="utf-8"))
    return {c["id"]: c for c in (x["chunks"] if isinstance(x, dict) else x)}


def b1_b2(perfil) -> None:
    print("B1. guarda del SDK, sin red")
    import anthropic
    import httpx
    recibidos = []

    def handler(req: httpx.Request) -> httpx.Response:
        recibidos.append(json.loads(req.content))
        return httpx.Response(200, json={"id": "msg_local", "type": "message", "role": "assistant",
                                          "model": RC.MODEL_E1, "content": [{"type": "text", "text": "ok"}],
                                          "stop_reason": "end_turn", "stop_sequence": None,
                                          "usage": {"input_tokens": 1, "output_tokens": 1}})
    cli = anthropic.Anthropic(api_key="sin-red", max_retries=0, http_client=httpx.Client(transport=httpx.MockTransport(handler)))
    cs = chunks_cap(E0_TANDA0)
    ns = cliente_e1.namespace_e1(prefijo_hash=perfil.prefijo_hash_para_namespace)
    claves = {}
    for cid in CASOS:
        kw = perfil.build_request_kwargs(cs[cid], model=RC.MODEL_E1)
        kw_r2 = {**kw, "max_tokens": cliente_e1.MAX_TOKENS_REINTENTO_CORTE_R2}
        kw_v = {**kw, "max_tokens": cliente_e1.MAX_TOKENS_REINTENTO_CORTE}
        n0 = len(recibidos)
        cli.messages.create(**kw_r2)
        llega = len(recibidos) == n0 + 1 and recibidos[-1]["max_tokens"] == 16384
        try:
            cli.messages.create(**kw_v)
            rechaza = False
        except ValueError as e:
            rechaza = "Streaming is required" in str(e) and len(recibidos) == n0 + 1
        check(f"B1 {cid}: el reintento a 16.384 llega al transporte y el de 32.768 lo rechaza la guarda",
              llega and rechaza)
        claves[cid] = cliente_e1.lc.compute_key(ns, cliente_e1.lc.canonical_request(kw_r2))
    check("B1 constantes: r2 16.384; perfiles existentes 32.768 (sin cambio)",
          (cliente_e1.MAX_TOKENS_REINTENTO_CORTE_R2, cliente_e1.MAX_TOKENS_REINTENTO_CORTE) == (16384, 32768))
    print("B2. clave del reintento a 16.384 en la caché de E1 (dirigida de la tanda 0)")
    if not DB_E1.exists():
        check("B2 claves en la caché", None, f"{DB_E1.relative_to(REPO)} no está en disco")
        return
    con = sqlite3.connect("file:" + str(DB_E1.resolve()) + "?mode=ro&immutable=1", uri=True)
    try:
        for cid, k in claves.items():
            fila = con.execute("SELECT namespace, stop_reason FROM cache WHERE key = ?", (k,)).fetchone()
            run = [r for (r,) in con.execute("SELECT DISTINCT run_label FROM access_log WHERE key = ?", (k,))]
            check(f"B2 {cid}: la clave está en la caché, con el namespace del perfil", fila is not None and fila[0] == ns,
                  f"stop_reason={fila[1] if fila else None} run_label={sorted(run)}")
    finally:
        con.close()


class ClienteCorte:
    """Cliente simulado: corta por max_tokens en la unidad (primer intento y
    reintento) y responde con un crudo en cada parte."""

    class _R:
        def __init__(self, stop, ti):
            self.stop_reason = stop
            self.content = [type("B", (), {"type": "tool_use", "input": ti})()] if ti is not None else []
            self.usage = type("U", (), {"input_tokens": 0, "output_tokens": 0, "cache_creation_input_tokens": 0,
                                        "cache_read_input_tokens": 0})()

    def __init__(self, crudo: dict):
        self.crudo = crudo
        self.requests: list[dict] = []
        self.messages = self
        self.gasto_usd = 0.0

    def create(self, **kw):
        self.requests.append(kw)
        texto = json.dumps(kw.get("messages"), ensure_ascii=False)
        if "(parte " not in texto:
            return self._R("max_tokens", None)
        return self._R("tool_use", self.crudo)

    def resumen(self) -> dict:
        return {"llamadas": len(self.requests)}


@contextlib.contextmanager
def runner_en(tmp: Path, chunk: dict, r2: bool, perfil):
    e0 = tmp / "e0"
    e0.mkdir(parents=True, exist_ok=True)
    (e0 / "chunks_cap.json").write_text(json.dumps([chunk], ensure_ascii=False), encoding="utf-8")
    orig = (RC.PERFIL, RC.PERFIL_R2, RC.E0_DIR)
    RC.PERFIL, RC.PERFIL_R2, RC.E0_DIR = perfil, r2, e0
    try:
        yield
    finally:
        RC.PERFIL, RC.PERFIL_R2, RC.E0_DIR = orig


def b3(perfil, e0_r2: Path | None) -> None:
    print("B3. partición por corte, sin cortar bloques de tabla")
    if e0_r2 is None or not (e0_r2 / "chunks_cap.json").exists():
        check("B3 partición por corte", None, "sin --e0-r2: no hay texto de e0-r2 de cap::4.2.1.2")
        return
    c = chunks_cap(e0_r2)["cap::4.2.1.2"]
    crudo = next(json.loads(l)["tool_input_crudo"] for l in
                 (REX / "corpus_tanda0" / "salida_dirigida" / "cap" / "extracciones_e1_compact.jsonl").open(encoding="utf-8")
                 if json.loads(l)["chunk_id"] == "cap::4.2.1.2")
    partes, informe = correr_e0.particionar_por_corte(c)
    check("B3 cap::4.2.1.2 de e0-r2 tiene tres bloques de tabla y se parte", informe["bloques_tabla"] == 3 and bool(partes),
          json.dumps({k: v for k, v in informe.items() if k != "partes"}, ensure_ascii=False))
    abiertos = []
    for s in partes or []:
        ls = s["texto"].split("\n")
        ini = [l.split()[1] for l in ls if correr_e0.RE_INICIO_BLOQUE_TABLA.match(l)]
        fin = [l.split()[2].rstrip("]") for l in ls if correr_e0.RE_FIN_BLOQUE_TABLA.match(l)]
        abiertos.append(sorted(ini) == sorted(fin))
    check("B3 cada bloque [TABLA …] abre y cierra en la misma parte", bool(partes) and all(abiertos), str(abiertos))
    check("B3 las partes reconstruyen el texto de la unidad (chapeau + grupos)",
          bool(partes) and "\n".join([partes[0]["texto"]] + [s["texto"] for s in partes[1:]]) == c["texto"])
    largo = "x" * 7000
    lineas = ("1. Título\n" + f"a) {largo}\n" * 2 + "[TABLA cap::t1 | página 1 | e0_tablas | posicional]\n"
              + "a) celda que parece ítem\n" * 5 + "[FIN TABLA cap::t1]\n" + f"b) {largo}\n" * 2)
    con = correr_e0._particionar_texto(lineas, respetar_tablas=True)
    sin = correr_e0._particionar_texto(lineas)
    check("B3 una línea de celda con forma de ítem no es marcador con respetar_tablas (sí sin él)",
          con is not None and con["n_items"] == 4 and sin is not None and sin["n_items"] == 9,
          f"con={con and con['n_items']} sin={sin and sin['n_items']}")
    for r2 in (True, False):
        with tempfile.TemporaryDirectory() as d, runner_en(Path(d), c, r2, perfil):
            sal = Path(d) / "salida"
            (sal / "cap").mkdir(parents=True)
            estado = RC.Estado(sal)
            cli = ClienteCorte(crudo)
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                RC.fase_e1("cap", cli, estado, sal, None, None, None)
            regs = [json.loads(l) for l in (sal / "cap" / "extracciones_e1.jsonl").read_text(encoding="utf-8").splitlines()]
            unidad = next(r for r in regs if r["chunk_id"] == "cap::4.2.1.2")
            if r2:
                ids_partes = [s["id"] for s in partes]
                check("B3 r2: la unidad queda registrada como partida, con reintento a 16.384",
                      unidad["error"] == RC.ERROR_PARTICIONADA
                      and unidad["reintento_corte"]["max_tokens_reintento"] == 16384
                      and [p["id"] for p in unidad["particion_por_corte"]["partes"]] == ids_partes)
                check("B3 r2: el reintento llega con max_tokens 16.384",
                      [k["max_tokens"] for k in cli.requests[:2]] == [cli.requests[0]["max_tokens"], 16384])
                check("B3 r2: las partes se extraen en el mismo pase y sin error",
                      [r["chunk_id"] for r in regs[1:]] == ids_partes and all(r["error"] is None for r in regs[1:]))
                part = json.loads((sal / "cap" / RC.ARCHIVO_PARTICIONES_CORTE).read_text(encoding="utf-8"))
                check("B3 r2: particiones_por_corte.json con las partes de la unidad",
                      list(part) == ["cap::4.2.1.2"] and [p["id"] for p in part["cap::4.2.1.2"]["partes"]] == ids_partes)
                check("B3 r2: en las fases siguientes las partes reemplazan a la unidad",
                      [x["id"] for x in RC.chunks_con_partes([c], sal / "cap")] == ids_partes)
                comp = RC.compactar_e1("cap", sal)
                check("B3 r2: la compactación lleva las partes y no la unidad",
                      [json.loads(l)["chunk_id"] for l in comp.read_text(encoding="utf-8").splitlines()] == ids_partes)
                resumen = json.loads((sal / "cap" / "resumen_e1.json").read_text(encoding="utf-8"))
                check("B3 r2: el resumen de E1 informa la partición y no la cuenta como error definitivo",
                      resumen.get("particionadas_por_corte") == {"cap::4.2.1.2": ids_partes}
                      and "errores_definitivos" not in resumen)
            else:
                check("B3 sin r2: el corte tras el reintento es error definitivo, reintento a 32.768, sin partición",
                      unidad["error"] == "max_tokens_hit_tras_reintento"
                      and unidad["reintento_corte"]["max_tokens_reintento"] == 32768
                      and len(regs) == 1 and not (sal / "cap" / RC.ARCHIVO_PARTICIONES_CORTE).exists()
                      and "particion_por_corte" not in unidad)


def b4() -> None:
    print("B4. clave de fusión del perfil r2 (T2 y H2)")
    s = e2_lib.entity_slug_r2
    pa = {"to": "ext", "punto": "7.5.3"}
    pb = {"to": "ext", "punto": "7.8.5.1"}
    r = {"type": "Restriccion", "label": "x", "properties": {"descripcion": "Esta opción no podrá superar el 125 %"}}
    check("B4 T2: misma descripción en puntos distintos → nodos distintos; en el mismo punto → el mismo",
          s(r, pa) != s(r, pb) and s(r, pa) == s(dict(r), dict(pa)))
    c1 = {"type": "Condicion", "label": "Monto", "properties": {"descripcion": "supera dos veces"}}
    c2 = {"type": "Condicion", "label": "Monto", "properties": {"descripcion": "no supera"}}
    check("B4 H2: Condicion con igual label y distinta descripción en el mismo punto → nodos distintos",
          s(c1, pa) != s(c2, pa) and s(c1, pa) == s(dict(c1), pa))
    op = {"type": "Operacion", "label": "Préstamo", "properties": {}}
    check("B4 Operacion y Sujeto siguen como v3 (sin el punto)",
          s(op, pa) == s(op, pb) == e2_lib.entity_slug_v3(op))
    check("B4 entity_slug_v3 sin cambios para Restriccion (descripción, sin punto)",
          e2_lib.entity_slug_v3(r) == e2_lib._id_estable(e2_lib.slugify_full(r["properties"]["descripcion"])))


def b5() -> None:
    print("B5. pie desde la línea «Versión» (e0-r2)")
    L = lambda t, i: E0.Linea(pagina=1, top=float(i), x0=0.0, texto=t, ngaps=0, ultimo_numerico=False,  # noqa: E731
                              primer_codigo=False)
    pag = [L("Texto del punto.", 1), L("Versión: 1a. COMUNICACIÓN “A” 6561 Página 2", 2), L("01/07/2018", 3),
           L("Comunicación “C” 81129", 4)]
    c_h, _, _ = E0.separar_encabezado_pie(pag)
    c_r, d_r, _ = E0.separar_encabezado_pie(pag, pie_desde_version=True)
    check("B5 el recorte histórico se detiene en «Comunicación “C”» y deja el pie; e0-r2 lo quita entero",
          len(c_h) == 4 and [l.texto for l in c_r] == ["Texto del punto."] and len(d_r) == 3)
    pag2 = [L("Versión : 1ª. Comunicación “A” 3671 Vigencia Página 1 de 1", 1)] + [L(f"línea {i}", i + 2) for i in range(5)]
    c2, _, _ = E0.separar_encabezado_pie(pag2, pie_desde_version=True)
    check("B5 una línea de versión fuera de las últimas 3 líneas no corta la página", len(c2) == 6)
    pag3 = [L("Texto.", 1), L("Versión : 2ª Comunicación “A” 4150 Vigencia Página 3 de 9", 2),
            L("Circular CONAU 1 – 270 04.09.98", 3)]
    c3, _, _ = E0.separar_encabezado_pie(pag3, pie_desde_version=True)
    check("B5 forma «Versión :» sin «Página N» al final y línea CONAU debajo", [l.texto for l in c3] == ["Texto."])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--e0-r2", type=Path, default=None)
    a = ap.parse_args()
    perfil = perfil_e1.perfil("v3_b54")
    b1_b2(perfil)
    b3(perfil, a.e0_r2)
    b4()
    b5()
    n_ok = sum(1 for _, e in RES if e == "PASS")
    n_nv = sum(1 for _, e in RES if e == "NO_VERIFICABLE")
    print(f"SELFTEST R4: {n_ok}/{len(RES)} PASS" + (f", {n_nv} NO_VERIFICABLE" if n_nv else ""))
    return 0 if all(e != "FAIL" for _, e in RES) else 1


if __name__ == "__main__":
    raise SystemExit(main())
