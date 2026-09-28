"""
selftest_dirigida_tanda0.py — U-TANDA0-2A-DIR (D1.b): selftest OFFLINE de
reextraccion_dirigida_tanda0.py. Clientes stub, cero red, cero gasto.

Toda escritura va a un directorio temporal (tempfile; correr con TMPDIR
apuntando a un scratch) que recibe copias de corpus_tanda0/salida/ (la E2
commiteada). El repo se fotografía (ruta, tamaño, mtime) antes y después:
ningún archivo del repo puede cambiar, dbs de caché incluidas.

Escenarios:
  0. Paridad: compactar_e1 + cerrar_e2 de cap con la configuración del
     módulo sobre una copia intacta reproducen byte a byte las salidas de
     cap de E2 (salvo la ruta absoluta del campo `extracciones`).
  A. Corrida normal con los tres desenlaces: aceptada directo, corte de nuevo
     a 16.384 (cola humana, sin re-llamada) y aceptada tras reintento del
     ratchet. Solo las tres unidades; request = el de E2 salvo max_tokens;
     escritura solo en cap/, estado, presupuesto y resumen; los nueve TOs
     restantes intactos; append-only; fan-in de cap +2; fase no re-corre.
  B. Tope compartido: (1) la guarda pre-unidad frena antes de empezar una
     unidad; (2) reanudación sobre el presupuesto persistido; (3) la guarda
     por llamada frena sobre el gasto COMBINADO de los tres clientes sin que
     ninguno alcance su tope propio.
  C. Clientes reales construidos sin red (dbs temporales): namespace v3,
     run_label, precios, guardián compartido; la guarda compartida de
     ClienteE1Real y ClienteE3Real frena antes de tocar la red.
  D. Prueba del request (D1.c) contra e1_extraccion.db, lectura immutable.

Uso: PYTHONDONTWRITEBYTECODE=1 TMPDIR=<scratch> .venv/bin/python selftest_dirigida_tanda0.py [--conservar]
"""

from __future__ import annotations

import sys

if not sys.dont_write_bytecode:
    print("correr con PYTHONDONTWRITEBYTECODE=1")
    sys.exit(2)

import hashlib        # noqa: E402
import json           # noqa: E402
import os             # noqa: E402
import shutil         # noqa: E402
import tempfile       # noqa: E402
from pathlib import Path  # noqa: E402

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))

import reextraccion_dirigida_tanda0 as rdt   # noqa: E402

rc = rdt.rc
import cliente_e1     # noqa: E402
import cliente_e3     # noqa: E402
import comun_e3       # noqa: E402
import prompt_e3      # noqa: E402
import ratchet_e3     # noqa: E402

REPO = rdt.REPO
NOMBRE_TOOL_E1 = rdt._v3.NOMBRE_TOOL
ZONAS_REPO = [REPO / "data" / "experiment" / "reextraccion_v2",
              REPO / "data" / "experiment" / "tanda0",
              REPO / "reports", REPO / "logs"]
PERMITIDOS = {"cap/extracciones_e1.jsonl", "cap/finales.jsonl", "cap/veredictos.jsonl",
              "cap/cola_humana.jsonl", "cap/extracciones_e1_compact.jsonl",
              "cap/extracciones_finales_cap.jsonl", "cap/grafo_cap.json",
              "cap/reporte_e2_cap.json", "cap/censo_cap.json", "estado_corpus.json",
              rdt.PRESUPUESTO, rdt.RESUMEN}

RESULTADOS: list[tuple[str, bool, str]] = []


def check(nombre: str, cond: bool, detalle: str = "") -> None:
    RESULTADOS.append((nombre, bool(cond), detalle))
    print(f"  [{'OK' if cond else 'FALLA'}] {nombre}" + (f" — {detalle}" if detalle else ""))


# ----------------------------- utilidades -------------------------------- #
def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def arbol(raiz: Path) -> dict[str, str]:
    return {str(p.relative_to(raiz)): sha(p) for p in sorted(raiz.rglob("*")) if p.is_file()}


def foto_repo() -> dict[str, tuple[int, int]]:
    out = {}
    for z in ZONAS_REPO:
        for raiz, _, fs in os.walk(z):
            for f in fs:
                p = Path(raiz) / f
                st = p.stat()
                out[str(p)] = (st.st_size, st.st_mtime_ns)
    return out


def copia_e2(tmp: Path, nombre: str) -> Path:
    dst = tmp / nombre
    shutil.copytree(rdt.SALIDA_E2, dst)
    return dst


def unidad_de(kwargs: dict, casos: dict[str, dict]) -> str:
    msg = kwargs["messages"][0]["content"]
    hits = [cid for cid, c in casos.items() if c["texto"] in msg]
    if len(hits) != 1:
        raise AssertionError(f"request sin unidad única: {hits}")
    return hits[0]


# ----------------------------- stubs ------------------------------------- #
class _Bloque:
    type = "tool_use"

    def __init__(self, nombre, tool_input):
        self.name = nombre
        self.input = tool_input


class _Usage:
    input_tokens = output_tokens = 0
    cache_creation_input_tokens = cache_read_input_tokens = 0


class _Resp:
    def __init__(self, nombre, tool_input, stop_reason="tool_use"):
        self.content = [_Bloque(nombre, tool_input)]
        self.stop_reason = stop_reason
        self.usage = _Usage()


class StubGuardado:
    """Contrato de guarda de ClienteE1Real/ClienteE3Real (cliente_e1.py:191-219,
    cliente_e3.py:172-200): chequeo pre-llamada contra el tope propio y contra
    el guardián compartido; delta registrado en ambos tras la llamada."""

    def __init__(self, excepcion, responder, costo, proyeccion, guardian, tope):
        self.messages = self
        self.exc = excepcion
        self.responder = responder
        self.costo = costo
        self._proyeccion_usd = proyeccion
        self.guardian = guardian
        self.tope_usd = tope
        self.gasto_usd = 0.0
        self.requests: list[dict] = []

    def create(self, **kwargs):
        if self.gasto_usd + self._proyeccion_usd > self.tope_usd:
            raise self.exc("tope propio")
        if self.guardian.excedido(self._proyeccion_usd):
            raise self.exc("presupuesto COMPARTIDO agotado")
        self.requests.append(kwargs)
        resp = self.responder(kwargs)
        self.gasto_usd += self.costo
        self.guardian.registrar(self.costo)
        return resp

    def resumen(self):
        return {"stub": True, "llamadas": len(self.requests),
                "gasto_usd_real": round(self.gasto_usd, 6)}

    def close(self):
        pass


def extraccion_minima(punto: str) -> dict:
    return {"entities": [{"local_id": "e1", "type": "Obligacion",
                          "label": f"obligacion stub {punto}", "punto": punto,
                          "properties": {}}],
            "relations": [], "omisiones_no_prosa": []}


def cita_verificable(chunk: dict) -> str:
    linea = max((l.strip() for l in chunk["texto"].split("\n")), key=len)
    cita = linea[:80]
    assert comun_e3.cita_en_fuente(cita, chunk), "cita del stub no verifica"
    return cita


def armar_stubs(casos, guardian, *, cortar=(), ratchet=(), costos=None, tope=1.0):
    """E1: corta (stop max_tokens) en las unidades de `cortar`. E3: en las de
    `ratchet` el primer veredicto trae un faltante 'alta' con cita verificada
    y el segundo es completo_ok; en el resto, completo_ok directo."""
    costos = costos or {"e1": (0.0, 0.05), "e3": (0.0, 0.104), "reint": (0.0, 0.05)}
    vistos_e3: dict[str, int] = {}

    def resp_e1(kw):
        cid = unidad_de(kw, casos)
        punto = casos[cid]["unidad"]
        stop = "max_tokens" if cid in cortar else "tool_use"
        return _Resp(NOMBRE_TOOL_E1, extraccion_minima(punto), stop)

    def resp_e3(kw):
        cid = unidad_de(kw, casos)
        vistos_e3[cid] = vistos_e3.get(cid, 0) + 1
        if cid in ratchet and vistos_e3[cid] == 1:
            return _Resp(prompt_e3.NOMBRE_TOOL, {
                "veredicto": "faltantes_detectados",
                "faltantes": [{"tipo": "otro", "ubicacion": casos[cid]["unidad"],
                               "severidad": "alta",
                               "cita_textual_del_fuente": cita_verificable(casos[cid]),
                               "nota": "stub"}]})
        return _Resp(prompt_e3.NOMBRE_TOOL, {"veredicto": "completo_ok", "faltantes": []})

    return {
        "e1": StubGuardado(cliente_e1.TopeExcedido, resp_e1, *costos["e1"], guardian, tope),
        "e3": StubGuardado(cliente_e3.TopeExcedido, resp_e3, *costos["e3"], guardian, tope),
        "reint": StubGuardado(cliente_e1.TopeExcedido, resp_e1, *costos["reint"], guardian, tope),
    }


def lineas(p: Path) -> list[str]:
    return p.read_text(encoding="utf-8").splitlines()


# ----------------------------- escenarios -------------------------------- #
def escenario_0(tmp: Path) -> None:
    print("\n[0] paridad de compactar_e1 + cerrar_e2 de cap con E2")
    s = copia_e2(tmp, "s0")
    rc.compactar_e1("cap", s)
    rc.cerrar_e2("cap", s)
    for f in ("extracciones_e1_compact.jsonl", "extracciones_finales_cap.jsonl",
              "grafo_cap.json", "censo_cap.json"):
        check(f"0 {f} byte-idéntico a E2", sha(s / "cap" / f) == sha(rdt.SALIDA_E2 / "cap" / f))
    r_tmp = json.loads((s / "cap" / "reporte_e2_cap.json").read_text(encoding="utf-8"))
    r_e2 = json.loads((rdt.SALIDA_E2 / "cap" / "reporte_e2_cap.json").read_text(encoding="utf-8"))
    r_tmp.pop("extracciones")
    r_e2.pop("extracciones")
    check("0 reporte_e2_cap igual a E2 salvo la ruta de `extracciones`", r_tmp == r_e2,
          f"sha256_grafo {r_e2['sha256_grafo'][:12]}")


def escenario_a(tmp: Path) -> None:
    print("\n[A] corrida normal con stubs")
    _, casos = rdt.cargar_cap()
    s = copia_e2(tmp, "sA")
    orig = arbol(rdt.SALIDA_E2)
    guardian = rc.PresupuestoCompartido(rdt.TOPE_USD, s / rdt.PRESUPUESTO)
    cl = armar_stubs(casos, guardian, cortar=("cap::4.2.1.2",), ratchet=("cap::4.3.3.1",))
    res = rdt.correr(s, cl, guardian)
    d = res["casos"]
    check("A1 desenlaces: directo / cola por corte / tras reintento",
          d["cap::3.1.14.1"]["resultado"] == "completo_ok_directo"
          and d["cap::4.2.1.2"]["resultado"] == "cola_humana"
          and d["cap::4.2.1.2"]["motivo"] == rdt.ERROR_CORTE
          and d["cap::4.3.3.1"]["resultado"] == "aceptado_tras_reintento",
          json.dumps({k: v["resultado"] for k, v in d.items()}))

    u_e1 = [unidad_de(k, casos) for k in cl["e1"].requests]
    u_e3 = [unidad_de(k, casos) for k in cl["e3"].requests]
    u_re = [unidad_de(k, casos) for k in cl["reint"].requests]
    check("A2 solo las tres unidades (E1 una llamada por unidad)",
          sorted(u_e1) == sorted(rdt.CASOS) and set(u_e3) <= set(rdt.CASOS)
          and u_e3 == ["cap::3.1.14.1", "cap::4.3.3.1", "cap::4.3.3.1"]
          and u_re == ["cap::4.3.3.1"], f"E1 {u_e1} | E3 {u_e3} | reint {u_re}")
    check("A3 sin reintento por corte: todo E1 a 16.384, ninguno a 32.768",
          all(k["max_tokens"] == 16384 for k in cl["e1"].requests)
          and u_e1.count("cap::4.2.1.2") == 1)

    iguales = True
    for k in cl["e1"].requests:
        chunk = casos[unidad_de(k, casos)]
        k8 = dict(k, max_tokens=8192)
        e2 = rdt.PERFIL.build_request_kwargs(chunk, model=rc.MODEL_E1)
        iguales &= (json.dumps(k8, sort_keys=True, ensure_ascii=False)
                    == json.dumps(e2, sort_keys=True, ensure_ascii=False))
        iguales &= k["model"] == "claude-haiku-4-5"
    check("A4 request E1 = request de E2 (perfil v3, default 8.192) salvo max_tokens", iguales)
    k_re, k_e1 = cl["reint"].requests[0], cl["e1"].requests[u_e1.index("cap::4.3.3.1")]
    check("A5 reintento del ratchet: 16.384, prefijo idéntico, feedback tras el mensaje",
          k_re["max_tokens"] == rc.MAX_TOKENS_REINTENTO
          and all(k_re[x] == k_e1[x] for x in ("system", "tools", "tool_choice", "model"))
          and k_re["messages"][0]["content"].startswith(k_e1["messages"][0]["content"])
          and ratchet_e3.MARCA_REINTENTO in k_re["messages"][0]["content"])
    check("A6 E3 con el modelo del runner", all(k["model"] == rc.MODEL_E3
                                               for k in cl["e3"].requests))

    nuevo = arbol(s)
    cambiados = {p for p in nuevo if orig.get(p) != nuevo[p]}
    check("A7 escritura solo en cap/ (lista cerrada), estado, presupuesto y resumen",
          cambiados <= PERMITIDOS and not (set(orig) - set(nuevo))
          and {rdt.PRESUPUESTO, rdt.RESUMEN, "estado_corpus.json",
               "cap/grafo_cap.json"} <= cambiados, f"{len(cambiados)} archivos: {sorted(cambiados)}")
    otros = {p for p in orig if not p.startswith("cap/") and p != "estado_corpus.json"}
    dirs_to = sorted({p.split("/")[0] for p in otros if "/" in p} - {"checkpoints"})
    check("A8 los nueve TOs distintos de cap, checkpoints y presupuesto de E2 intactos",
          all(nuevo[p] == orig[p] for p in otros) and len(dirs_to) == 9,
          f"{len(otros)} archivos; TOs {dirs_to}")

    ok_append = True
    for f, n in (("extracciones_e1.jsonl", 3), ("finales.jsonl", 3),
                 ("veredictos.jsonl", 3), ("cola_humana.jsonl", 1)):
        a, b = lineas(rdt.SALIDA_E2 / "cap" / f), lineas(s / "cap" / f)
        ok_append &= b[:len(a)] == a and len(b) == len(a) + n
    check("A9 append-only (E1 +3, finales +3, veredictos +3, cola +1)", ok_append)

    e_o = json.loads((rdt.SALIDA_E2 / "estado_corpus.json").read_text(encoding="utf-8"))
    e_n = json.loads((s / "estado_corpus.json").read_text(encoding="utf-8"))
    fase = e_n["fases_cerradas"].pop(rdt.FASE, None)
    check("A10 estado: solo se agrega la fase reextraccion_dirigida",
          fase is not None and fase["resumen"]["n"] == 3 and e_n == e_o)

    fin_o = {json.loads(l)["chunk_id"]: json.loads(l)
             for l in lineas(rdt.SALIDA_E2 / "cap" / "extracciones_finales_cap.jsonl")}
    fin_n = {json.loads(l)["chunk_id"]: json.loads(l)
             for l in lineas(s / "cap" / "extracciones_finales_cap.jsonl")}
    resto_igual = all(fin_n[c] == fin_o[c] for c in fin_o if c not in rdt.CASOS)
    check("A11 fan-in final: resto de cap igual; dos ingresan, una a cola",
          resto_igual and set(fin_n) == set(fin_o)
          and fin_n["cap::3.1.14.1"]["validacion"] is not None
          and fin_n["cap::4.3.3.1"]["validacion"] is not None
          and fin_n["cap::4.2.1.2"]["error"] == f"cola_humana:{rdt.ESTADO_COLA}")
    rep_o = json.loads((rdt.SALIDA_E2 / "cap" / "reporte_e2_cap.json").read_text(encoding="utf-8"))
    fo, fn = rep_o["fanin"], res["e2_cap"]["fanin"]
    check("A12 fan-in de cap: aceptados +2, rechazados −2, esperados igual",
          fn["esperados"] == fo["esperados"] and fn["aceptados"] == fo["aceptados"] + 2
          and fn["rechazados"] == fo["rechazados"] - 2 and fn["ausentes"] == 0,
          f"{fo['aceptados']}/{fo['rechazados']} → {fn['aceptados']}/{fn['rechazados']}")

    antes = arbol(s)
    try:
        rdt.correr(s, cl, guardian)
        repite = True
    except RuntimeError:
        repite = False
    check("A13 la fase cerrada no re-corre ni escribe", not repite and arbol(s) == antes)

    vedadas = []
    for p in (rdt.SALIDA_E2, rdt.CORPUS_V2 / "salida", rdt.CORPUS_V2):
        try:
            rdt.validar_salida_dir(p)
        except RuntimeError:
            vedadas.append(p.name)
    check("A14 guarda de ruta: salida/ y corpus_v2/ vedadas; salida_dirigida admitida",
          len(vedadas) == 3 and rdt.validar_salida_dir(rdt.SALIDA) == rdt.SALIDA.resolve(),
          f"vedadas {vedadas}")


def escenario_b(tmp: Path) -> None:
    print("\n[B] tope compartido")
    _, casos = rdt.cargar_cap()
    orig_grafo = sha(rdt.SALIDA_E2 / "cap" / "grafo_cap.json")

    # (1) guarda pre-unidad con el margen del manifiesto
    s = copia_e2(tmp, "sB1")
    g = rc.PresupuestoCompartido(0.50, s / rdt.PRESUPUESTO)
    cl = armar_stubs(casos, g, ratchet=("cap::3.1.14.1",), tope=0.50,
                     costos={"e1": (0.05, 0.05), "e3": (0.10, 0.104),
                             "reint": (0.05, 0.05)})
    try:
        rdt.correr(s, cl, g, tope_usd=0.50)
        freno = None
    except rc.Freno as e:
        freno = str(e)
    pres = json.loads((s / rdt.PRESUPUESTO).read_text(encoding="utf-8"))
    check("B1 guarda pre-unidad (margen 0,35 del manifiesto): frena antes de la 2.ª unidad",
          rc.MARGEN_UNIDAD_USD == 0.35 and freno is not None and "cap::4.2.1.2" in freno
          and len(cl["e1"].requests) == 1 and abs(g.gasto_usd - 0.30) < 1e-9
          and g.gasto_usd <= 0.50 and pres == {"tope_usd": 0.5, "gasto_usd": 0.3}
          and sha(s / "cap" / "grafo_cap.json") == orig_grafo
          and rdt.FASE not in json.loads((s / "estado_corpus.json").read_text(
              encoding="utf-8"))["fases_cerradas"],
          f"gasto combinado {g.gasto_usd:.4f} ≤ 0,50; {freno}")

    # (2) reanudación sobre el presupuesto persistido (tope mayor)
    g2 = rc.PresupuestoCompartido(1.00, s / rdt.PRESUPUESTO)
    cl2 = armar_stubs(casos, g2, cortar=("cap::4.2.1.2",),
                      costos={"e1": (0.05, 0.05), "e3": (0.10, 0.104),
                              "reint": (0.05, 0.05)})
    res = rdt.correr(s, cl2, g2)
    u_e1 = [unidad_de(k, casos) for k in cl2["e1"].requests]
    check("B2 reanudación: gasto previo cargado, unidad hecha salteada, fase cerrada",
          abs(g2.gasto_usd - (0.30 + 0.05 + 0.05 + 0.10)) < 1e-9
          and u_e1 == ["cap::4.2.1.2", "cap::4.3.3.1"]
          and res["casos"]["cap::3.1.14.1"]["resultado"] == "aceptado_tras_reintento"
          and res["casos"]["cap::4.2.1.2"]["resultado"] == "cola_humana"
          and res["casos"]["cap::4.3.3.1"]["resultado"] == "completo_ok_directo",
          f"gasto combinado {g2.gasto_usd:.4f}; E1 {u_e1}")

    # (3) guarda por llamada sobre el gasto COMBINADO (fracciones binarias
    # exactas: 1/16 y 1/8 — sin ruido de coma flotante en el borde)
    s = copia_e2(tmp, "sB2")
    g = rc.PresupuestoCompartido(0.25, s / rdt.PRESUPUESTO)
    cl = armar_stubs(casos, g, ratchet=("cap::3.1.14.1",), tope=0.25,
                     costos={"e1": (0.0625, 0.0625), "e3": (0.125, 0.125),
                             "reint": (0.0625, 0.0625)})
    exc = None
    try:
        rdt.correr(s, cl, g, tope_usd=0.25, margen_unidad_usd=0.0)
    except cliente_e3.TopeExcedido as e:
        exc = str(e)
    propios_ok = all(c.gasto_usd + c._proyeccion_usd <= c.tope_usd for c in cl.values())
    check("B3 guarda por llamada: frena la re-verificación por el gasto COMBINADO",
          exc is not None and "COMPARTIDO" in exc and g.gasto_usd == 0.25
          and g.gasto_usd == sum(c.gasto_usd for c in cl.values())
          and [len(c.requests) for c in cl.values()] == [1, 1, 1] and propios_ok
          and rdt.FASE not in json.loads((s / "estado_corpus.json").read_text(
              encoding="utf-8"))["fases_cerradas"],
          f"gasto combinado {g.gasto_usd} = tope; ningún tope propio alcanzado")


def escenario_c(tmp: Path) -> None:
    print("\n[C] clientes reales sin red (dbs temporales)")
    dbs = {k: tmp / "dbs" / f"{k}.db" for k in ("e1", "e3", "reint")}
    g = rc.PresupuestoCompartido(rdt.TOPE_USD, tmp / "presupuesto_c.json")
    cl = rdt.construir_clientes(g, dbs=dbs)
    ns = rdt.namespace_e1()
    try:
        check("C1 namespace v3 en E1 y reintentos; E3 con el suyo",
              cl["e1"].cache.namespace == ns == cl["reint"].cache.namespace
              and ns.endswith("-p54a111e2175f|think=0")
              and cl["e3"].cache.namespace == cliente_e3.namespace_e3(), ns)
        check("C2 run_label, precios, tope y guardián compartido",
              {k: c.cache.run_label for k, c in cl.items()} == rdt.RUN_LABELS
              and all(c.guardian is g and c.tope_usd == 1.0 for c in cl.values())
              and (cl["e1"].p_in, cl["e1"].p_out, cl["e1"].p_cw, cl["e1"].p_cr) == tuple(rc.P_E1.values())
              and (cl["e3"].p_in, cl["e3"].p_out, cl["e3"].p_cw, cl["e3"].p_cr) == tuple(rc.P_E3.values()))
        check("C3 dbs por defecto de la corrida = las de E2 (never-pay-twice)",
              rdt.DBS == {"e1": cliente_e1.DB_PATH, "e3": cliente_e3.DB_PATH,
                          "reint": rc.DB_REINTENTOS_E1})
    finally:
        for c in cl.values():
            c.close()
    g_chico = rc.PresupuestoCompartido(0.01, tmp / "presupuesto_c2.json")
    cl = rdt.construir_clientes(g_chico, dbs=dbs)
    frenos = []
    try:
        for k, exc in (("e1", cliente_e1.TopeExcedido), ("e3", cliente_e3.TopeExcedido),
                       ("reint", cliente_e1.TopeExcedido)):
            try:
                cl[k].create(doc="selftest", model="x", max_tokens=1, messages=[])
            except exc as e:
                frenos.append("COMPARTIDO" in str(e))
    finally:
        for c in cl.values():
            c.close()
    check("C4 ClienteE1Real/E3Real reales frenan por el guardián compartido antes de la red",
          frenos == [True, True, True] and g_chico.gasto_usd == 0.0)


def escenario_d() -> None:
    print("\n[D] prueba del request contra e1_extraccion.db (lectura immutable)")
    r = rdt.prueba_request()
    ok = r["n_filas_db"] == 3 and all(
        u["coinciden"] and u["clave_db_recomputada"] == u["clave_db"]
        and u["namespace_db"] == r["namespace_modulo"] for u in r["unidades"].values())
    check("D1 claves a 8.192 = claves de corpus_cap_e1 (max_tokens, 27/09) de a pares",
          ok, "; ".join(f"{c.split('::')[1]} {u['clave_modulo_8192'][:12]}"
                        for c, u in r["unidades"].items()))


def main() -> int:
    conservar = "--conservar" in sys.argv[1:]
    foto0 = foto_repo()
    tmp = Path(tempfile.mkdtemp(prefix="selftest_dirigida_tanda0_"))
    print(f"temporal: {tmp}")
    try:
        escenario_0(tmp)
        escenario_a(tmp)
        escenario_b(tmp)
        escenario_c(tmp)
        escenario_d()
    finally:
        if not conservar:
            shutil.rmtree(tmp, ignore_errors=True)
    foto1 = foto_repo()
    check("R repo intacto (reextraccion_v2 con dbs, tanda0, reports, logs)",
          foto0 == foto1, f"{len(foto0)} archivos fotografiados")
    n_ok = sum(1 for _, ok, _ in RESULTADOS if ok)
    print(f"\nselftest: {n_ok}/{len(RESULTADOS)} OK")
    return 0 if n_ok == len(RESULTADOS) else 1


if __name__ == "__main__":
    sys.exit(main())
