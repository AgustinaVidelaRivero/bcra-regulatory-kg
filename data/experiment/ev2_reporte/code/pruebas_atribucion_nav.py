"""
pruebas_atribucion_nav.py — Pruebas de ATRIB_NAV (USD 0, sin API, sin Neo4j y sin el codificador): los dos módulos
nuevos, `atribucion_fallas_nav.py` y `banco_mcp/adaptador/adaptador_banco_nav.py`, contra HEAD y contra casos armados.

  --regresion-selftest  el selftest de atribucion_fallas.py dos veces: con cada `atribuir_payload` de HEAD comparado
                        byte a byte con el nuevo, y con el nuevo en su lugar (tiene que dar todo PASS);
  --regresion-ev2       las trazas de EV2 que atribuye atribucion_fallas.py (las 120 base y las 198 re-corridas §7),
                        leídas por código: por traza, las anclas que portan los nodos que aparecen en sus salidas, tres
                        del censo del grafo por un sorteo fijo y una que no existe; cada una, y todas juntas, con HEAD y
                        con el nuevo, comparadas byte a byte. No lee el set sellado (es un conjunto de evaluación) ni los
                        veredictos (el veredicto es fijo, «parcial»). No imprime ningún texto;
  --sinteticos          un caso por cada una de las diez herramientas, con lo que cuenta y lo que no (la cabecera
                        incluida), y los del pedido a `mcp__kg`. Las salidas de las siete de navegación las arma el
                        código de HEAD (familias_nav_cand.NavegadorCand) sobre un índice por punto chico, en memoria,
                        con un doble del driver que responde sus consultas desde una lista de aristas;
  --humo                las sesiones del grafo del humo del banco (banco_mcp/paralelo/humo/): adaptador, lectores y
                        atribución, sin imprimir sus preguntas ni ningún texto de sus salidas;
  --nombres-b63         los nombres de herramienta del `mapa_R7` de las metas sin texto del grafo de B6.3 y si el
                        adaptador reconoce cada uno, sin cuentas por sesión;
  --lector-claves-b63   cuántas claves de punto del índice por punto del grafo de B6.3 lee de vuelta el lector de
                        claves de ucita2_indicadores_banco, por forma de la unidad (sin texto).
Vuelta b (los dos cierres del §7 del borrador):
  --sinteticos          suma los casos de la presencia con un grafo de juguete y los de las v1 del log R1;
  --presencia-b63       AnclaIndexBanco sobre el grafo de B6.3, contra su índice por punto, en todas sus claves;
  --equivalencia-ev2    las 318 trazas de EV2 con un log armado con la re-ejecución de HEAD: la atribución que lee las
                        v1 de ese log da, byte a byte, lo mismo que HEAD, con las mismas anclas que la regresión;
  --v1-b63              las salidas v1 de los logs R1 del brazo `kg` de B6.3 (banco_b63/resultados/real/pasada1/):
                        JSON, campos de la regla v1 y output_sha256; solo sí o no y cuentas totales;
  --limite-trazas N     solo para estimar el tiempo de las dos de EV2 con una muestra.

Uso (desde cualquier lugar; todo Python con -I -B):
  python3 -I -B data/experiment/ev2_reporte/code/pruebas_atribucion_nav.py --sinteticos --out DIR
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import random
import re
import sys
from collections import Counter
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO_DIR = AQUI.parents[3]
ADAPTADOR_DIR = REPO_DIR / "data" / "experiment" / "banco_mcp" / "adaptador"
for _p in (str(AQUI), str(ADAPTADOR_DIR)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import atribucion_fallas_nav as NAV  # noqa: E402
import adaptador_banco_nav as ABN  # noqa: E402
AF = NAV.AF
U = NAV.U
IP = NAV.IP
import adaptador_banco as AB  # noqa: E402  (HEAD: el contraste del caso de mcp__kg)
import familias_nav as FN  # noqa: E402  (HEAD, vía sys.path de ucita2_indicadores_banco)
import familias_nav_cand as FNC  # noqa: E402  (HEAD)
import bm25_fragmentos as BM  # noqa: E402  (HEAD)
from metrica import _reejecutar_step  # noqa: E402  (sintéticas, sin editar)
from adaptador_cc import _truncar  # noqa: E402  (HEAD)

BANCO_DIR = REPO_DIR / "data" / "experiment" / "banco_mcp"
HUMO_DIR = BANCO_DIR / "paralelo" / "humo"
METAS_B63 = BANCO_DIR / "b63" / "real" / "metas_sin_texto"
INDICES_DIR = BANCO_DIR / "mcp_kg" / "indice_puntos"
CONFIG_KG_N7 = BANCO_DIR / "n7" / "config_mcp_kg_n7_evaluado.json"


class Registro:
    def __init__(self):
        self.casos = []

    def caso(self, nombre: str, ok: bool, detalle=None):
        self.casos.append({"caso": nombre, "ok": bool(ok), "detalle": detalle})
        print(("PASS " if ok else "FAIL ") + nombre + ("" if ok or detalle is None else f"  [{detalle}]"))

    def resumen(self) -> dict:
        n_ok = sum(1 for c in self.casos if c["ok"])
        print(f"== {n_ok} de {len(self.casos)} PASS")
        return {"n_casos": len(self.casos), "n_ok": n_ok, "casos": self.casos}


def sha_json(obj) -> str:
    return hashlib.sha256(json.dumps(obj, ensure_ascii=False).encode("utf-8")).hexdigest()


def escribir(out_dir: Path, nombre: str, obj) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    p = out_dir / nombre
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return p


# --------------------------------------------------------------------------- #
# Regresión 1: el selftest de atribucion_fallas.py                             #
# --------------------------------------------------------------------------- #
def regresion_selftest(out_dir: Path) -> dict:
    original = AF.atribuir_payload
    comparaciones = []

    def comparado(payload, anclas, ancla_index, index, veredicto, replay_fuerte=True):
        a = original(payload, anclas, ancla_index, index, veredicto, replay_fuerte)
        b = NAV.atribuir_payload(payload, anclas, ancla_index, index, veredicto, replay_fuerte=replay_fuerte)
        comparaciones.append(json.dumps(a, ensure_ascii=False) == json.dumps(b, ensure_ascii=False))
        return a

    def nuevo(payload, anclas, ancla_index, index, veredicto, replay_fuerte=True):
        return NAV.atribuir_payload(payload, anclas, ancla_index, index, veredicto, replay_fuerte=replay_fuerte)

    AF.atribuir_payload = comparado
    try:
        r_head = AF.selftest(out_dir / "selftest_head")
    finally:
        AF.atribuir_payload = original
    AF.atribuir_payload = nuevo
    try:
        r_nav = AF.selftest(out_dir / "selftest_con_la_nueva")
    finally:
        AF.atribuir_payload = original
    a = json.loads((out_dir / "selftest_head" / "selftest_atribucion.json").read_text(encoding="utf-8"))
    b = json.loads((out_dir / "selftest_con_la_nueva" / "selftest_atribucion.json").read_text(encoding="utf-8"))
    a.pop("generado"), b.pop("generado")
    res = {"selftest_head_rc": r_head, "selftest_con_la_nueva_rc": r_nav,
           "checks_head": f"{a['n_ok']} de {a['n_checks']}", "checks_con_la_nueva": f"{b['n_ok']} de {b['n_checks']}",
           "llamadas_comparadas": len(comparaciones), "llamadas_iguales_byte_a_byte": sum(comparaciones),
           "selftest_json_igual_salvo_generado": a == b}
    print("regresión selftest:", json.dumps(res, ensure_ascii=False))
    escribir(out_dir, "regresion_selftest.json", res)
    return res


# --------------------------------------------------------------------------- #
# Regresión 2: las trazas de EV2 que atribuye atribucion_fallas.py             #
# --------------------------------------------------------------------------- #
def _nodos_de_salidas(payload: dict) -> list[str]:
    """Los ids de nodo que aparecen en las salidas persistidas (steps_full) de la traza, en orden."""
    out = []
    for sf in payload.get("steps_full", []):
        o = sf.get("output") or {}
        if sf["tool"] == "buscar_nodos":
            out += [r.get("id") for r in o.get("resultados", [])]
        elif sf["tool"] == "ver_nodo":
            out.append(o.get("id"))
        elif sf["tool"] == "ver_vecinos":
            out += [v.get("vecino_id") for k in ("salientes", "entrantes") for v in (o.get(k) or [])]
    return [x for x in dict.fromkeys(out) if x]


def anclas_derivadas(payload: dict, aidx, sorteo: random.Random, todas: list) -> list[str]:
    por_nodo = {}
    for (to, ancla), ids in aidx.por_ancla.items():
        for nid in ids:
            por_nodo.setdefault(nid, []).append(f"{to}:{ancla}")
    de_la_traza = [a for nid in _nodos_de_salidas(payload) for a in por_nodo.get(nid, [])]
    return list(dict.fromkeys(de_la_traza + sorteo.sample(todas, 3) + ["ext:999.999"]))


class IndiceConMemoria:
    """harness.GraphIndex con memoria por entrada. Las tres v1 son funciones puras del grafo y de la entrada (el
    supuesto de la re-ejecución de metrica.py), así que la salida es la misma; HEAD y la nueva reciben este mismo
    índice. Ningún consumidor modifica la salida (evaluar_traza la lee, _check_replay la serializa,
    verificar_steps_full la compara)."""

    def __init__(self, index):
        self.index, self.memo = index, {}

    def _de(self, clave, f):
        if clave not in self.memo:
            self.memo[clave] = f()
        return self.memo[clave]

    def buscar_nodos(self, consulta, limite=10):
        return self._de(("buscar_nodos", consulta, json.dumps(limite)), lambda: self.index.buscar_nodos(consulta, limite))

    def ver_nodo(self, id):
        return self._de(("ver_nodo", json.dumps(id)), lambda: self.index.ver_nodo(id))

    def ver_vecinos(self, id, direccion="ambas"):
        return self._de(("ver_vecinos", json.dumps(id), json.dumps(direccion)),
                        lambda: self.index.ver_vecinos(id, direccion))


def regresion_ev2(out_dir: Path, limite: int | None = None) -> dict:
    from comun_ev2 import cargar_runtime, indice_anclas, verificar_grafos
    from comun_reporte import CORRIDA_DIR, ENC_DIR, ORDEN_GRAFOS, rel_repo
    from harness import GraphIndex
    shas = verificar_grafos(verbose=False)
    res = {"grafos_sha256": shas, "por_grafo": {}, "n_trazas": 0, "n_comparaciones": 0, "n_iguales": 0,
           "trazas_con_alguna_diferencia": [], "clases_cubiertas_HEAD": Counter(), "replay_ok": 0, "replay_fuerte_ok": 0}
    h_head, h_nav = hashlib.sha256(), hashlib.sha256()
    for g in ORDEN_GRAFOS:
        aidx = indice_anclas(g)
        index = IndiceConMemoria(GraphIndex(cargar_runtime(g)))
        todas = sorted(f"{to}:{a}" for (to, a) in aidx.por_ancla)
        dirs = [CORRIDA_DIR / "trazas" / f"ev2_base_{'run3' if g == 'run_3' else g}"]
        dirs += [ENC_DIR / "trazas" / f"ev2_enc_{'run3' if g == 'run_3' else g}_r{r}" for r in (1, 2, 3)]
        n_g = 0
        for d in dirs:
            for p in sorted(d.glob("EV2F-*.json")):
                if limite and n_g >= limite:
                    break
                payload = json.loads(p.read_text(encoding="utf-8"))
                sorteo = random.Random(f"ATRIB_NAV:regresion:{rel_repo(p)}")
                anclas = anclas_derivadas(payload, aidx, sorteo, todas)
                llamadas = [([a], "parcial") for a in anclas] + [(anclas, "parcial"), (anclas[:1], "correcto")]
                distinta = False
                for lista, veredicto in llamadas:
                    a = json.dumps(AF.atribuir_payload(payload, lista, aidx, index, veredicto), ensure_ascii=False)
                    b = json.dumps(NAV.atribuir_payload(payload, lista, aidx, index, veredicto), ensure_ascii=False)
                    res["n_comparaciones"] += 1
                    res["n_iguales"] += a == b
                    distinta |= a != b
                    h_head.update(a.encode("utf-8"))
                    h_nav.update(b.encode("utf-8"))
                    x = json.loads(a)
                    if len(lista) == 1 and veredicto == "parcial":
                        res["clases_cubiertas_HEAD"][x["clase"]] += 1
                x = AF.atribuir_payload(payload, anclas[:1], aidx, index, "parcial")
                res["replay_ok"] += x["replay_ok"]
                res["replay_fuerte_ok"] += x["replay_fuerte_ok"]
                if distinta:
                    res["trazas_con_alguna_diferencia"].append(rel_repo(p))
                n_g += 1
        res["por_grafo"][g] = n_g
        res["n_trazas"] += n_g
        print(f"  {g}: {n_g} trazas")
    res["clases_cubiertas_HEAD"] = dict(sorted(res["clases_cubiertas_HEAD"].items()))
    res["sha256_salidas_HEAD"] = h_head.hexdigest()
    res["sha256_salidas_nueva"] = h_nav.hexdigest()
    res["nota"] = ("anclas derivadas por código de cada traza (no el gold sellado); veredicto fijo «parcial» "
                   "(y uno «correcto» por traza); las clases son de esas anclas, no resultados de EV2")
    print("regresión EV2:", json.dumps({k: v for k, v in res.items() if k != "grafos_sha256"}, ensure_ascii=False))
    escribir(out_dir, "regresion_ev2.json", res)
    return res


# --------------------------------------------------------------------------- #
# Casos sintéticos: el mundo chico                                             #
# --------------------------------------------------------------------------- #
DOC = "TO_exterior_cambios_actual.pdf"
TEXTO_611 = "Texto propio del punto alfa: el pago al exterior requiere la conformidad previa."


def _punto(clave, unidad, tipo, titulo, padre, hijos, textos, nodos):
    return {"clave": clave, "to": "ext", "unidad": unidad, "tipo": tipo, "titulo": titulo, "padre": padre,
            "hijos": hijos, "pagina": 1, "paginas": [1], "bloques": [], "textos": textos, "herencia": [],
            "intro": False, "nodos": nodos, "en_estructura": True}


def _nodo(tipo, label, puntos, tramo=None):
    return {"type": tipo, "label": label, "puntos": puntos, "tramo": tramo,
            "tramo_por_punto": {p: tramo for p in puntos} if tramo else {}, "rol_por_punto": {}, "rol": None,
            "termino": None, "descripcion": None, "umbrales": None, "cola": False}


def mundo_puntos(texto_611: str = TEXTO_611) -> tuple[dict, dict, list]:
    puntos = {
        "ext": _punto("ext", "ext", "to", "Exterior y cambios", None, ["ext::S6", "ext::S7"], [], []),
        "ext::S6": _punto("ext::S6", "S6", "seccion", "Pagos al exterior", "ext", ["ext::6.11", "ext::6.12"], [], []),
        "ext::6.11": _punto("ext::6.11", "6.11", "punto", "Ancla alfa", "ext::S6", ["ext::6.11.1"], [texto_611],
                            ["Obligacion_ancla_A"]),
        "ext::6.11.1": _punto("ext::6.11.1", "6.11.1", "punto", "Subpunto zeta", "ext::6.11", [],
                              ["Texto del subpunto zeta con un plazo especial."], []),
        "ext::6.12": _punto("ext::6.12", "6.12", "punto", "Vecino beta", "ext::S6", [], [], ["Operacion_vecino_B"]),
        "ext::S7": _punto("ext::S7", "S7", "seccion", "Restricciones", "ext", ["ext::7.1", "ext::7.2"], [], []),
        "ext::7.1": _punto("ext::7.1", "7.1", "punto", "Gamma tope", "ext::S7", [], ["Texto gamma del tope."],
                           ["Restriccion_gamma_C"]),
        "ext::7.2": _punto("ext::7.2", "7.2", "punto", "Delta excepcion", "ext::S7", [], ["Texto delta."],
                           ["Excepcion_delta_D"]),
    }
    nodos = {
        "Obligacion_ancla_A": _nodo("Obligacion", "Ancla alfa pago exterior", ["ext::6.11"], "contenido del ancla A"),
        "Operacion_vecino_B": _nodo("Operacion", "Vecino beta operacion cambio", ["ext::6.12"]),
        "Restriccion_gamma_C": _nodo("Restriccion", "Gamma restriccion tope", ["ext::7.1"]),
        "Excepcion_delta_D": _nodo("Excepcion", "Delta excepcion pago exterior", ["ext::7.2"]),
        "TextoOrdenado_contenedor": _nodo("TextoOrdenado", "Contenedor alfa exterior", []),
    }
    aristas = [
        {"a": "Operacion_vecino_B", "rel": "aplica_a", "b": "Obligacion_ancla_A", "o": 1, "p": {}},
        {"a": "Obligacion_ancla_A", "rel": "restringido_por", "b": "Restriccion_gamma_C", "o": 2, "p": {}},
        {"a": "Restriccion_gamma_C", "rel": "remite_a", "b": "Obligacion_ancla_A", "o": 3,
         "p": {"alcance": "punto", "destino": "ext::6.11",
               "provenances_json": json.dumps([{"source_doc": DOC, "location": "Punto 7.1"}])}},
    ]
    return puntos, nodos, aristas


class DriverDeAristas:
    """Doble del driver de Neo4j para las consultas de familias_nav que leen aristas: las relaciones entre los nodos
    listados de ver_punto, los vecinos de un nodo (_vecinos) y las remite_a (_remisiones). Otra consulta falla."""

    class _R:
        def __init__(self, filas):
            self.filas = filas

        def data(self):
            return self.filas

    def __init__(self, nodos: dict, aristas: list):
        self.nodos, self.aristas = nodos, sorted(aristas, key=lambda e: e["o"])

    def session(self):
        return self

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def run(self, cypher: str, **params):
        if "[r:remite_a]->" in cypher and "r.destino AS destino" in cypher:
            return self._R([{"a": e["a"], "b": e["b"], "destino": e["p"].get("destino"), "o": e["o"], "p": e["p"]}
                            for e in self.aristas if e["rel"] == "remite_a"])
        if "WHERE a.id IN $ids AND b.id IN $ids" in cypher:
            ids = set(params["ids"])
            return self._R([{"a": e["a"], "rel": e["rel"], "b": e["b"], "p": e["p"]}
                            for e in self.aristas if e["a"] in ids and e["b"] in ids])
        m = re.search(r"MATCH \(n:`[^`]+` \{id: \$id\}\) MATCH (\(n\)(<?-)\[r(?::`([^`]+)`)?\](->?)\(v:`[^`]+`\))", cypher)
        if m:
            saliente = m.group(4) == "->"
            rel = m.group(3)
            filas = []
            for e in self.aristas:
                if rel and e["rel"] != rel:
                    continue
                if saliente and e["a"] == params["id"]:
                    v = e["b"]
                elif not saliente and e["b"] == params["id"]:
                    v = e["a"]
                else:
                    continue
                filas.append({"rel": e["rel"], "v": v, "tipo": self.nodos[v]["type"], "label": self.nodos[v]["label"],
                              "p": e["p"]})
            return self._R(filas)
        raise RuntimeError("doble del driver: consulta no prevista")


def navegador_chico(texto_611: str = TEXTO_611) -> FNC.NavegadorCand:
    """El NavegadorCand de HEAD sin su constructor (que abre Neo4j y el índice en disco): los mismos atributos que
    arma __init__, desde el mundo chico; sin denso ni hubs."""
    puntos, nodos, aristas = mundo_puntos(texto_611)
    nav = object.__new__(FNC.NavegadorCand)
    nav.label, nav.dir = "MundoChico", Path("mundo_chico")
    nav.puntos, nav.nodos = puntos, nodos
    docs = [{"id": k, "texto": IP.documento(puntos, nodos, k)} for k in IP.orden_canonico(puntos)]
    nav.buscador = BM.Buscador(BM.construir(docs))
    nav.ids_docs = [d["id"] for d in docs]
    nav.textos_docs = [d["texto"] for d in docs]
    nav.archivo_a_to = {DOC: "ext"}
    nav.tos = ["ext"]
    nav.terminos = {k: [] for k in puntos}
    nav.driver = DriverDeAristas(nodos, aristas)
    grado = Counter()
    for e in aristas:
        grado[e["a"]] += 1
        grado[e["b"]] += 1
    nav.grado = {n: grado.get(n, 0) for n in nodos}
    nav.hubs, nav.umbral_hub = set(), 99
    nav.denso = None
    return nav


def lectura_chica(nav) -> dict:
    return {"man": U.armar_manifiesto([{"id": "ext", "archivo": DOC}], {"ext": frozenset({"6", "7"})}),
            "nodos_por_punto": {k: list(p["nodos"]) for k, p in nav.puntos.items() if p["tipo"] != "to"},
            "ids": frozenset(nav.nodos)}


def salida_de(nav, index, tool: str, inp: dict) -> str:
    if tool in NAV.TOOLS_V1:
        return json.dumps(_reejecutar_step(index, {"tool": tool, "input": inp}), ensure_ascii=False)
    return FNC.despachar_cand(nav, tool, inp)


def traza(nav, index, llamadas: list) -> dict:
    """Payload con la forma del adaptador del banco: steps con el truncado del harness y steps_full con la salida (JSON
    para las v1, texto para las de navegación)."""
    steps, full = [], []
    for n, (tool, inp) in enumerate(llamadas, 1):
        s = salida_de(nav, index, tool, inp)
        steps.append({"n": n, "tool": tool, "input": inp, "output_truncado": _truncar(s), "output_chars": len(s)})
        if tool in NAV.TOOLS_V1:
            full.append({"n": n, "tool": tool, "input": inp, "output": json.loads(s), "output_chars": len(s)})
        else:
            full.append({"n": n, "tool": tool, "input": inp, "output": s, "output_chars": len(s), "formato": "texto"})
    return {"meta": {"caso_id": "SINT"}, "trace": {"steps": steps, "final_json": {"respuesta": "x", "citas": [],
                                                                                    "respondible": True},
                                                   "tool_calls_used": len(steps), "hit_tool_limit": False},
            "steps_full": full}


def _resumen_ancla(at: dict) -> dict:
    pa = next(iter(at["por_ancla"].values()))
    return {"clase": at["clase"], "vista": at["ancla_vista"], "consultada": at["ancla_consultada"],
            "vista_en_step": pa.get("vista_en_step"), "consultada_en_step": pa.get("consultada_en_step"),
            "consultada_via": pa.get("consultada_via"),
            "vias_vista": sorted({e["via"] for e in (pa.get("navegacion") or {}).get("vista", [])})}


CASOS = [
    # (herramienta, nombre, llamadas, ancla, clase esperada, controles extra sobre el resumen)
    ("buscar_nodos", "v1: el ancla en los resultados -> vista, no consultada",
     [("buscar_nodos", {"consulta": "alfa exterior", "limite": 10})], "ext::6.11", "vista_no_consultada", {}),
    ("buscar_nodos", "v1: búsqueda que no devuelve el ancla -> alcanzabilidad",
     [("buscar_nodos", {"consulta": "gamma tope", "limite": 10})], "ext::6.11", "alcanzabilidad", {}),
    ("ver_nodo", "v1: ver_nodo del nodo del ancla -> consultada",
     [("ver_nodo", {"id": "Obligacion_ancla_A"})], "ext::6.11", "generacion", {"consultada_via": ["ver_nodo"]}),
    ("ver_nodo", "v1: ver_nodo de un id que no existe (error) -> no cuenta",
     [("ver_nodo", {"id": "Obligacion_ancla_A_typo"})], "ext::6.11", "alcanzabilidad", {}),
    ("ver_vecinos", "v1: el ancla como vecino_id -> consultada",
     [("ver_vecinos", {"id": "Operacion_vecino_B", "direccion": "salientes"})], "ext::6.11", "generacion",
     {"consultada_via": ["ver_vecinos"]}),
    ("ver_vecinos", "v1: ver_vecinos del propio nodo del ancla -> no cuenta (borde heredado)",
     [("ver_vecinos", {"id": "Obligacion_ancla_A", "direccion": "ambas"})], "ext::6.11", "alcanzabilidad", {}),
    ("buscar_puntos", "fila con la clave del ancla y su nodo (tipo · id) -> vista, no consultada",
     [("buscar_puntos", {"consulta": "alfa conformidad"})], "ext::6.11", "vista_no_consultada",
     {"vias_vista": ["clave_del_punto", "id_de_nodo", "nodo_de_una_clave"]}),
    ("buscar_puntos", "cabecera: el filtro punto=<ancla> sin el ancla en las filas -> no cuenta",
     [("buscar_puntos", {"consulta": "zeta", "punto": "ext::6.11"})], "ext::6.11", "alcanzabilidad", {}),
    ("ver_punto", "el punto del ancla con su texto -> consultada (y vista por su lista de nodos)",
     [("ver_punto", {"punto": "ext::6.11"})], "ext::6.11", "generacion",
     {"consultada_via": ["ver_punto"], "vias_vista": ["clave_del_punto", "id_de_nodo", "nodo_de_una_clave"]}),
    ("ver_punto", "punto del ancla sin texto propio: su lista de nodos -> vista, no consultada",
     [("ver_punto", {"punto": "ext::6.12"})], "ext::6.12", "vista_no_consultada", {"vias_vista": ["id_de_nodo"]}),
    ("ver_punto", "cabecera y ancestros: ver_punto de un hijo del ancla -> no cuenta",
     [("ver_punto", {"punto": "ext::6.11.1"})], "ext::6.11", "alcanzabilidad", {}),
    ("ver_punto", "salida de error (punto que no existe) -> no cuenta",
     [("ver_punto", {"punto": "ext::6.99"})], "ext::6.11", "alcanzabilidad", {}),
    ("ver_remisiones", "fila de remisión al punto del ancla -> vista, no consultada",
     [("ver_remisiones", {"punto": "ext::7.1", "direccion": "cita"})], "ext::6.11", "vista_no_consultada",
     {"vias_vista": ["clave_del_punto", "nodo_de_una_clave"]}),
    ("ver_remisiones", "cabecera: las remisiones del propio ancla -> no cuenta",
     [("ver_remisiones", {"punto": "ext::6.11"})], "ext::6.11", "alcanzabilidad", {}),
    ("indice_to", "el árbol del TO lista unidades sin el TO (no son claves to::unidad) -> no cuenta",
     [("indice_to", {"to": "ext", "niveles": 3})], "ext::6.11", "alcanzabilidad", {}),
    ("indice_to", "cabecera: indice_to desde el ancla -> no cuenta",
     [("indice_to", {"to": "ext", "desde": "ext::6.11"})], "ext::6.11", "alcanzabilidad", {}),
    ("tipos_de_relacion", "del nodo del ancla: su punto en la segunda línea -> vista, no consultada",
     [("tipos_de_relacion", {"id": "Obligacion_ancla_A"})], "ext::6.11", "vista_no_consultada",
     {"vias_vista": ["clave_del_punto", "nodo_de_una_clave"]}),
    ("tipos_de_relacion", "de otro nodo (el vecino): ni el id del ancla ni su punto -> no cuenta",
     [("tipos_de_relacion", {"id": "Operacion_vecino_B"})], "ext::6.11", "alcanzabilidad", {}),
    ("vecinos_por_relacion", "fila de vecino con el id y el punto del ancla -> vista, no consultada",
     [("vecinos_por_relacion", {"id": "Operacion_vecino_B", "relacion": "aplica_a", "direccion": "salientes"})],
     "ext::6.11", "vista_no_consultada", {"vias_vista": ["clave_del_punto", "id_de_nodo", "nodo_de_una_clave"]}),
    ("vecinos_por_relacion", "cabecera: los vecinos del propio nodo del ancla -> no cuenta",
     [("vecinos_por_relacion", {"id": "Obligacion_ancla_A", "relacion": "restringido_por", "direccion": "salientes"})],
     "ext::6.11", "alcanzabilidad", {}),
    ("ver_descendientes", "el bloque del ancla con su texto -> consultada",
     [("ver_descendientes", {"punto": "ext::S6"})], "ext::6.11", "generacion",
     {"consultada_via": ["ver_descendientes"]}),
    ("ver_descendientes", "bloque del ancla sin texto propio -> vista, no consultada",
     [("ver_descendientes", {"punto": "ext::S6"})], "ext::6.12", "vista_no_consultada",
     {"vias_vista": ["clave_del_punto", "nodo_de_una_clave"]}),
    ("ver_descendientes", "cabecera: los descendientes del propio ancla -> no cuenta",
     [("ver_descendientes", {"punto": "ext::6.11"})], "ext::6.11", "alcanzabilidad", {}),
    ("mezcla", "vista por navegación en el step 1 y consulta v1 en el 2 -> generacion, vista_en_step 1",
     [("buscar_puntos", {"consulta": "alfa conformidad"}), ("ver_nodo", {"id": "Obligacion_ancla_A"})],
     "ext::6.11", "generacion", {"vista_en_step": 1, "consultada_en_step": 2, "consultada_via": ["ver_nodo"]}),
    ("mezcla", "v1 vista en el step 2 y navegación en el 1 -> vista_en_step es el menor",
     [("vecinos_por_relacion", {"id": "Operacion_vecino_B", "relacion": "aplica_a", "direccion": "salientes"}),
      ("buscar_nodos", {"consulta": "alfa exterior", "limite": 10})], "ext::6.11", "vista_no_consultada",
     {"vista_en_step": 1}),
    ("mezcla", "ancla con el formato de EV2 (to:punto) y salida de navegación -> la misma clave",
     [("ver_punto", {"punto": "ext::6.11"})], "ext:6.11", "generacion", {"consultada_via": ["ver_punto"]}),
]


def sinteticos(out_dir: Path) -> dict:
    R = Registro()
    raw, index, aidx = AF._mini_grafo()
    nav = navegador_chico()
    lect = lectura_chica(nav)

    diez = set(NAV.TOOLS_V1) | set(NAV.TOOLS_NAV)
    R.caso("las diez: harness.TOOLS + TOOLS_NAV del lector = tools_esperadas del brazo kg de B6.3",
           diez == set(ABN.TOOLS_KG_B63) and len(diez) == 10, sorted(diez ^ set(ABN.TOOLS_KG_B63)))
    R.caso("las siete de navegación = TOOLS_NAV_CAND de familias_nav_cand",
           set(NAV.TOOLS_NAV) == {t["name"] for t in FNC.TOOLS_NAV_CAND} == set(ABN.TOOLS_NAV_B63))

    detalle, cubiertas = [], Counter()
    for tool, nombre, llamadas, ancla, esperada, extra in CASOS:
        t = traza(nav, index, llamadas)
        at = NAV.atribuir_payload(t, [ancla], aidx, index, "parcial", lect)
        r = _resumen_ancla(at)
        ok = r["clase"] == esperada and all(r.get(k) == v for k, v in extra.items()) and at["replay_ok"] \
            and at["replay_fuerte_ok"] and (at.get("navegacion_b63") or {}).get("consistencia_steps_full_ok", True)
        R.caso(f"{tool}: {nombre}", ok, r)
        cubiertas[tool] += 1
        detalle.append({"herramienta": tool, "caso": nombre, "llamadas": llamadas, "ancla": ancla,
                        "esperada": esperada, "obtenido": r,
                        "lecturas": [{k: v for k, v in lec.items()} for lec in
                                     (at.get("navegacion_b63") or {}).get("lecturas", [])]})
        if all(tl in NAV.TOOLS_V1 for tl, _ in llamadas) and ":" in ancla:
            a_ev2 = ancla.replace("::", ":")
            h = AF.atribuir_payload(t, [a_ev2], aidx, index, "parcial")
            n = NAV.atribuir_payload(t, [a_ev2], aidx, index, "parcial", lect)
            R.caso(f"{tool}: el mismo caso solo v1, igual byte a byte a HEAD", json.dumps(h) == json.dumps(n))

    # el texto cortado por el tope de ver_descendientes
    nav_largo = navegador_chico(texto_611=("Texto largo del ancla alfa. " * 400).strip())
    t = traza(nav_largo, index, [("ver_descendientes", {"punto": "ext::S6", "niveles": 1})])
    s = t["steps_full"][0]["output"]
    at = NAV.atribuir_payload(t, ["ext::6.11"], aidx, index, "parcial", lectura_chica(nav_largo))
    R.caso("ver_descendientes: el bloque del ancla con su texto cortado por el tope -> consultada",
           "cortado en" in s and at["clase"] == "generacion", _resumen_ancla(at))
    cubiertas["ver_descendientes"] += 1

    # la cabecera de cada una de las siete repite la entrada: la clave (o el id) del ancla que está solo ahí no cuenta
    for tool, inp, clave, nid in (("buscar_puntos", {"consulta": "zeta", "punto": "ext::6.11"}, "ext::6.11", None),
                                  ("ver_punto", {"punto": "ext::6.12"}, "ext::6.12", None),
                                  ("ver_remisiones", {"punto": "ext::6.11"}, "ext::6.11", None),
                                  ("indice_to", {"to": "ext", "desde": "ext::6.11"}, "ext::6.11", None),
                                  ("tipos_de_relacion", {"id": "Obligacion_ancla_A"}, None, "Obligacion_ancla_A"),
                                  ("vecinos_por_relacion", {"id": "Obligacion_ancla_A", "relacion": "restringido_por",
                                                            "direccion": "salientes"}, None, "Obligacion_ancla_A"),
                                  ("ver_descendientes", {"punto": "ext::6.11"}, "ext::6.11", None)):
        s = FNC.despachar_cand(nav, tool, inp)
        cab = s.split("\n", 1)[0]
        en_cab = bool(clave and (clave in cab or clave.partition("::")[2] in cab)) or bool(nid and nid in cab)
        lec = NAV.leer_paso(tool, s, lect)
        R.caso(f"cabecera de {tool}: {'la clave' if clave else 'el id'} del ancla en la primera línea no cuenta",
               en_cab and (clave is None or clave not in lec["claves"]) and (nid is None or nid not in lec["ids"]),
               {"en_cabecera": en_cab, "claves": lec["claves"], "ids": lec["ids"]})

    # el pedido a mcp__kg
    R_kg = casos_mcp_kg(out_dir / "sesiones_sinteticas", nav, index, aidx, lect)
    R.casos += R_kg
    cubiertas["mcp__kg"] += len(R_kg)

    # vuelta b: la presencia en el grafo del banco y las v1 del log R1
    R_pres = casos_presencia(nav, index, lect)
    R.casos += R_pres
    cubiertas["presencia_banco"] += len(R_pres)
    R_log = casos_v1_del_log(out_dir / "sesiones_sinteticas", nav, index, lect)
    R.casos += R_log
    cubiertas["v1_del_log"] += len(R_log)
    res = R.resumen() | {"casos_por_herramienta": dict(sorted(cubiertas.items())), "detalle": detalle}
    escribir(out_dir, "sinteticos.json", res)
    return res


def _sesion(dir_: Path, nombre: str, usos: list, llamadas_log: list, fin: bool = True) -> tuple[Path, Path]:
    """Escribe stream_<nombre>.jsonl y log_r1_<nombre>.jsonl con la forma de los del banco. `usos`: [(name, input,
    texto del tool_result, is_error)]; `llamadas_log`: [(tool, input, output_str)] o dicts ya armados."""
    dir_.mkdir(parents=True, exist_ok=True)
    L = [{"type": "system", "subtype": "init", "session_id": f"S-{nombre}"}]
    for i, (name, inp, texto, es_error) in enumerate(usos, 1):
        L.append({"type": "assistant", "uuid": f"u{i}", "message": {"content": [
            {"type": "tool_use", "id": f"tu{i}", "name": name, "input": inp}]}})
        if texto is not None:
            bloque = {"type": "tool_result", "tool_use_id": f"tu{i}", "content": [{"type": "text", "text": texto}]}
            if es_error:
                bloque["is_error"] = True
            L.append({"type": "user", "message": {"content": [bloque]}})
    L.append({"type": "result", "subtype": "success", "is_error": False, "num_turns": len(usos) + 1,
              "result": json.dumps({"respuesta": "x", "citas": [], "respondible": True})})
    st = dir_ / f"stream_{nombre}.jsonl"
    st.write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in L), encoding="utf-8")
    G = [{"evento": "inicio", "servidor": "mcp_kg", "config_sha256": "sintetica", "fuente": {"kg_path": "mundo_chico"}}]
    for n, ll in enumerate(llamadas_log, 1):
        if isinstance(ll, dict):
            G.append(ll)
            continue
        tool, inp, out = ll
        G.append({"evento": "llamada", "call_id": f"mcp_kg-1-{n}", "n": n, "tool": tool, "input": inp,
                  "output_str": out, "output_chars": len(out),
                  "output_sha256": hashlib.sha256(out.encode("utf-8")).hexdigest(), "error": None})
    if fin:
        G.append({"evento": "fin", "servidor": "mcp_kg", "n_llamadas": len(llamadas_log)})
    lg = dir_ / f"log_r1_{nombre}.jsonl"
    lg.write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in G), encoding="utf-8")
    return st, lg


ERROR_CLIENTE = "<tool_use_error>Error: No such tool available: mcp__kg</tool_use_error>"


def casos_mcp_kg(dir_: Path, nav, index, aidx, lect) -> list:
    R = Registro()
    bp = ("buscar_puntos", {"consulta": "alfa conformidad"})
    vp = ("ver_punto", {"punto": "ext::6.11"})
    s_bp, s_vp = salida_de(nav, index, *bp), salida_de(nav, index, *vp)

    # 1. el pedido a mcp__kg entre dos llamadas: no llega al servidor y no corre la reconciliación
    st, lg = _sesion(dir_, "kg_entre_dos", [("mcp__kg__buscar_puntos", bp[1], s_bp, False),
                                           ("mcp__kg", {"consulta": "alfa"}, ERROR_CLIENTE, True),
                                           ("mcp__kg__ver_punto", vp[1], s_vp, False)],
                     [(bp[0], bp[1], s_bp), (vp[0], vp[1], s_vp)])
    p = ABN.adaptar(st, lg, {"caso_id": "kg_entre_dos"})
    R.caso("mcp__kg (adaptador nuevo): 2 steps, el pedido contado aparte, R7 alineado, atribuible",
           p["gate"]["n_steps_adaptados"] == 2 and p["banco"]["pedidos_sin_herramienta"]["n"] == 1
           and not p["gate"]["rechazos"] and p["gate"]["atribuible"]
           and [m["n_log"] for m in p["gate"]["mapa_steps"]] == [1, 2],
           {"steps": p["gate"]["n_steps_adaptados"], "pedidos": p["banco"]["pedidos_sin_herramienta"]["n"],
            "rechazos": len(p["gate"]["rechazos"]), "atribuible": p["gate"]["atribuible"]})
    at = NAV.atribuir_payload(p, ["ext::6.11"], aidx, index, "parcial", lect)
    R.caso("mcp__kg (atribución): el pedido no hace vista ni consultada; se cuenta aparte; la clase sale de los otros",
           at["clase"] == "generacion"
           and at["navegacion_b63"]["pedidos_sin_herramienta"]["en_el_adaptador"] == 1
           and at["por_ancla"]["ext::6.11"]["consultada_en_step"] == 2,
           _resumen_ancla(at))
    h = AB.adaptar(st, lg, {"caso_id": "kg_entre_dos"})
    R.caso("mcp__kg (adaptador de HEAD, contraste): el pedido corre la reconciliación y la traza no es atribuible",
           not h["gate"]["atribuible"] and len(h["gate"]["rechazos"]) >= 2,
           [r["motivo_rechazo"][:60] for r in h["gate"]["rechazos"]])

    # 2. el pedido solo (sin otra llamada): payload sin steps, contado
    st, lg = _sesion(dir_, "kg_solo", [("mcp__kg", {}, ERROR_CLIENTE, True)], [])
    p = ABN.adaptar(st, lg, {"caso_id": "kg_solo"})
    at = NAV.atribuir_payload(p, ["ext::6.11"], aidx, index, "parcial", lect)
    R.caso("mcp__kg solo: 0 steps, 1 pedido, alcanzabilidad",
           p["gate"]["n_steps_adaptados"] == 0 and p["banco"]["pedidos_sin_herramienta"]["n"] == 1
           and p["gate"]["atribuible"] and at["clase"] == "alcanzabilidad", _resumen_ancla(at))

    # 3. un pedido sin herramienta con un tool_result que no es error: no atribuible
    st, lg = _sesion(dir_, "kg_sin_error", [("mcp__kg", {}, "algo", False), ("mcp__kg__ver_punto", vp[1], s_vp, False)],
                     [(vp[0], vp[1], s_vp)])
    p = ABN.adaptar(st, lg, {"caso_id": "kg_sin_error"})
    R.caso("pedido sin herramienta cuyo tool_result no es un error -> no atribuible (R3)",
           not p["gate"]["atribuible"] and any("no son herramientas" in m for m in p["banco"]["completitud_R3"]["motivos"]))

    # 4. un step con una herramienta que no es ninguna de las diez, dentro de la traza: se cuenta aparte
    t = traza(nav, index, [bp])
    t["trace"]["steps"].append({"n": 2, "tool": "kg", "input": {}, "output_truncado": None, "output_chars": None})
    at = NAV.atribuir_payload(t, ["ext::6.11"], aidx, index, "parcial", lect)
    R.caso("step con un nombre que no es herramienta (p. ej. «kg») en la traza: no cuenta y se cuenta aparte",
           at["clase"] == "vista_no_consultada" and at["navegacion_b63"]["pedidos_sin_herramienta"]["en_steps"]
           == [{"n": 2, "tool": "kg"}] and at["replay_ok"], _resumen_ancla(at))

    # 5. R7 del adaptador nuevo: sha256 del log, n del log, texto de la sesión distinto y truncado
    mal_sha = {"evento": "llamada", "call_id": "mcp_kg-1-1", "n": 1, "tool": vp[0], "input": vp[1], "output_str": s_vp,
               "output_chars": len(s_vp), "output_sha256": "0" * 64, "error": None}
    st, lg = _sesion(dir_, "r7_sha", [("mcp__kg__ver_punto", vp[1], s_vp, False)], [mal_sha])
    p = ABN.adaptar(st, lg)
    R.caso("R7: output_sha256 del log que no es el de su output_str -> rechazo",
           not p["gate"]["atribuible"] and "output_sha256" in p["gate"]["rechazos"][0]["motivo_rechazo"])
    mal_n = dict(mal_sha, n=2, output_sha256=hashlib.sha256(s_vp.encode("utf-8")).hexdigest())
    st, lg = _sesion(dir_, "r7_n", [("mcp__kg__ver_punto", vp[1], s_vp, False)], [mal_n])
    p = ABN.adaptar(st, lg)
    R.caso("R7: n del log distinto del orden de la llamada -> rechazo",
           not p["gate"]["atribuible"] and "el n del log" in p["gate"]["rechazos"][0]["motivo_rechazo"])
    st, lg = _sesion(dir_, "r7_distinta", [("mcp__kg__ver_punto", vp[1], s_vp.replace("alfa", "ALFA"), False)],
                     [(vp[0], vp[1], s_vp)])
    p = ABN.adaptar(st, lg)
    R.caso("R7: texto de la sesión del mismo largo y distinto del log -> rechazo",
           not p["gate"]["atribuible"] and "no es el del log" in p["gate"]["rechazos"][0]["motivo_rechazo"])
    st, lg = _sesion(dir_, "r7_truncada", [("mcp__kg__ver_punto", vp[1], s_vp[:50], False)], [(vp[0], vp[1], s_vp)])
    p = ABN.adaptar(st, lg)
    R.caso("R7: texto de la sesión truncado por el transporte -> la salida sale del log, atribuible",
           p["gate"]["atribuible"] and p["gate"]["mapa_steps"][0]["sesion_truncada_por_transporte"]
           and p["steps_full"][0]["output"] == s_vp)
    st, lg = _sesion(dir_, "r7_herramienta", [("mcp__kg__ver_punto", vp[1], s_vp, False)], [(bp[0], bp[1], s_bp)])
    p = ABN.adaptar(st, lg)
    R.caso("R7: herramienta o entrada distintas de las del log -> rechazo",
           not p["gate"]["atribuible"] and "no coincide" in p["gate"]["rechazos"][0]["motivo_rechazo"])
    st, lg = _sesion(dir_, "v1_y_nav", [("mcp__kg__buscar_nodos", {"consulta": "alfa exterior"},
                                        salida_de(nav, index, "buscar_nodos", {"consulta": "alfa exterior"}), False),
                                       ("mcp__kg__ver_punto", vp[1], s_vp, False)],
                     [("buscar_nodos", {"consulta": "alfa exterior"},
                       salida_de(nav, index, "buscar_nodos", {"consulta": "alfa exterior"})), (vp[0], vp[1], s_vp)])
    p = ABN.adaptar(st, lg)
    at = NAV.atribuir_payload(p, ["ext::6.11"], aidx, index, "parcial", lect)
    R.caso("v1 y navegación en una sesión: la v1 en steps_full como JSON, la otra como texto; atribuible y re-ejecutable",
           p["gate"]["atribuible"] and isinstance(p["steps_full"][0]["output"], dict)
           and p["steps_full"][1]["formato"] == "texto" and at["replay_ok"] and at["replay_fuerte_ok"]
           and at["clase"] == "generacion", _resumen_ancla(at))
    return R.casos


# --------------------------------------------------------------------------- #
# Vuelta b: la presencia en el grafo del banco, con un grafo de juguete        #
# --------------------------------------------------------------------------- #
def _pv(to, punto):
    return {"to": to, "punto": punto, "archivo": f"TO_{to}.pdf", "rol_documental": "cuerpo"}


def grafo_juguete_banco() -> dict:
    def nodo(i, tipo, provs, singular=False):
        return {"id": i, "type": tipo, "label": i} | ({"provenance": provs[0]} if singular else {"provenances": provs})
    return {"nodes": [
        nodo("N_exacto", "Obligacion", [_pv("ext", "6.11")]),
        nodo("N_hijo", "Obligacion", [_pv("ext", "6.11.1")]),
        nodo("N_intro", "Definicion", [_pv("ext", "6.11::intro")]),
        nodo("N_blancos", "Requisito", [_pv("ext", " 6.12 ")], singular=True),
        nodo("N_once", "Comunicacion", [_pv("ext", f"9.{i}") for i in range(1, 12)]),
        nodo("N_diez", "Comunicacion", [_pv("ext", f"8.{i}") for i in range(1, 11)]),
        nodo("TO_ext", "TextoOrdenado", [_pv("ext", "6.11"), _pv("ext", "8.1")]),
        nodo("N_seccion", "Obligacion", [_pv("ext", "S7")]),
        nodo("N_sin_punto", "Otro", [{"to": "ext", "archivo": "TO_ext.pdf"}]),
    ], "edges": []}


def casos_presencia(nav, index, lect) -> list:
    R = Registro()
    ai = NAV.AnclaIndexBanco(grafo_juguete_banco())
    R.caso("presencia: el punto exacto (6.11 no trae a su hijo 6.11.1)",
           ai.resolver("ext", "6.11") == ["N_exacto", "N_intro"] and ai.resolver("ext", "6.11.1") == ["N_hijo"],
           ai.resolver("ext", "6.11"))
    R.caso("presencia: base_punto lleva «ext::6.11::intro» a «ext::6.11», en la procedencia y en el ancla",
           ai.resolver("ext", "6.11::intro") == ["N_exacto", "N_intro"])
    R.caso("presencia: el strip del punto («provenance» sola, « 6.12 ») y del ancla",
           ai.resolver("ext", "6.12") == ["N_blancos"] == ai.resolver("ext", " 6.12 "))
    R.caso("presencia: un contenedor de más de 10 claves queda fuera (y vuelve con incluir_contenedores)",
           ai.resolver("ext", "9.3") == [] and ai.contenedores.get("N_once") == 11
           and ai.resolver("ext", "9.3", incluir_contenedores=True) == ["N_once"])
    R.caso("presencia: un nodo de 10 claves no es contenedor",
           ai.resolver("ext", "8.2") == ["N_diez"] and "N_diez" not in ai.contenedores)
    R.caso("presencia: un TextoOrdenado de 10 claves o menos (2) es contenedor y queda fuera",
           ai.contenedores.get("TO_ext") == 2 and "TO_ext" not in ai.resolver("ext", "6.11")
           and ai.resolver("ext", "8.1") == ["N_diez"])
    R.caso("presencia: las dos formas del ancla, «ext:6.11» y «ext::6.11», resuelven igual",
           NAV.resolver_anclas(["ext:6.11", "ext::6.11"], ai) == {"ext:6.11": ["N_exacto", "N_intro"],
                                                                 "ext::6.11": ["N_exacto", "N_intro"]})
    R.caso("presencia: un ancla ausente (punto que no está, TO que no está) resuelve a nada",
           ai.resolver("ext", "6.99") == [] and ai.resolver("cla", "6.11") == [])
    R.caso("presencia: la sección «S7» por su clave, y la procedencia sin punto no se lee",
           ai.resolver("ext", "S7") == ["N_seccion"] and ai.sin_parsear == [{"node_id": "N_sin_punto"}])
    c = ai.censo([{"to": "ext", "ancla": "6.11"}, {"to": "ext", "ancla": "6.99"}])
    R.caso("presencia: censo con la forma de resolucion.AnclaIndex.censo",
           c == {"resueltas": {("ext", "6.11"): ["N_exacto", "N_intro"]}, "ausentes": [("ext", "6.99")],
                 "nodos_gold": ["N_exacto", "N_intro"]})
    # el índice entra en atribuir_payload sin cambiarlo: el mundo chico, con sus procedencias en la forma del banco
    _, nodos, _ = mundo_puntos()
    raw = {"nodes": [{"id": i, "type": nd["type"], "label": nd["label"],
                      "provenances": [_pv(*k.split("::", 1)) for k in nd["puntos"]]} for i, nd in nodos.items()]}
    ai_chico = NAV.AnclaIndexBanco(raw)
    t = traza(nav, index, [("ver_punto", {"punto": "ext::6.11"})])
    at = NAV.atribuir_payload(t, ["ext::6.11"], ai_chico, index, "parcial", lect)
    at2 = NAV.atribuir_payload(t, ["ext::6.99"], ai_chico, index, "parcial", lect)
    R.caso("presencia: atribuir_payload recibe el índice del banco sin cambiar (generacion; un ancla ausente, ausencia_kg)",
           at["clase"] == "generacion" and at2["clase"] == "ausencia_kg", [at["clase"], at2["clase"]])
    return R.casos


# --------------------------------------------------------------------------- #
# Vuelta b: las v1 del log R1, con casos de juguete                            #
# --------------------------------------------------------------------------- #
def _alterar(log: dict, n: int, **cambios) -> dict:
    """Una copia del log leído con la llamada `n` cambiada."""
    return {"llamadas": [dict(ll, **cambios) if ll.get("n") == n else dict(ll) for ll in log["llamadas"]]}


def casos_v1_del_log(dir_: Path, nav, index, lect) -> list:
    R = Registro()
    _, nodos, _ = mundo_puntos()
    raw = {"nodes": [{"id": i, "type": nd["type"], "label": nd["label"],
                      "provenances": [_pv(*k.split("::", 1)) for k in nd["puntos"]]} for i, nd in nodos.items()]}
    ai = NAV.AnclaIndexBanco(raw)

    def sesion_v1(nombre, llamadas):
        usos, log = [], []
        for tool, inp in llamadas:
            s = salida_de(nav, index, tool, inp)        # la salida «del servidor»: la del mundo chico
            usos.append((ABN.PREFIJO_KG + tool, inp, s, False))
            log.append((tool, inp, s))
        st, lg = _sesion(dir_, nombre, usos, log)
        return ABN.adaptar(st, lg, {"caso_id": nombre}), lg

    casos = [("buscar_nodos: el ancla en los resultados del log -> vista", "v1log_buscar",
              [("buscar_nodos", {"consulta": "alfa exterior", "limite": 10})], "vista_no_consultada", None),
             ("ver_nodo sin error -> consultada", "v1log_ver_nodo",
              [("ver_nodo", {"id": "Obligacion_ancla_A"})], "generacion", ["ver_nodo"]),
             ("ver_nodo con error -> no cuenta", "v1log_ver_nodo_error",
              [("ver_nodo", {"id": "Obligacion_ancla_A_typo"})], "alcanzabilidad", None),
             ("ver_vecinos: el ancla como vecino_id -> consultada", "v1log_ver_vecinos",
              [("ver_vecinos", {"id": "Operacion_vecino_B", "direccion": "salientes"})], "generacion", ["ver_vecinos"]),
             ("una traza que mezcla v1 y navegación", "v1log_mezcla",
              [("buscar_puntos", {"consulta": "alfa conformidad"}), ("ver_nodo", {"id": "Obligacion_ancla_A"})],
              "generacion", ["ver_nodo"])]
    buenas = []
    for nombre, sid, llamadas, esperada, via in casos:
        p, lg = sesion_v1(sid, llamadas)
        at = NAV.atribuir_payload(p, ["ext::6.11"], ai, None, "parcial", lect, log_r1=lg)
        r = _resumen_ancla(at)
        buenas.append(at)
        R.caso(f"v1 del log: {nombre}", p["gate"]["atribuible"] and at["clase"] == esperada and at["replay_ok"]
               and at["replay_fuerte_ok"] and (via is None or r["consultada_via"] == via), r)
    R.caso("v1 del log: con los controles en verde, la corrida es válida", NAV.corrida_valida(buenas))

    # los tres controles que invalidan la corrida: el log leído, alterado en la llamada del step v1
    p, lg = sesion_v1("v1log_control", [("ver_nodo", {"id": "Obligacion_ancla_A"})])
    log = NAV.leer_log_r1(lg)
    s_obj = log["llamadas"][0]["output_str"]
    no_json = "esto no es JSON"
    for nombre, alterado, motivo in (
            ("el sha256 que no da", _alterar(log, 1, output_sha256="0" * 64), "sha256"),
            ("una salida que no es JSON", _alterar(log, 1, output_str=no_json,
                                                   output_sha256=hashlib.sha256(no_json.encode("utf-8")).hexdigest()),
             "JSON"),
            ("un R7 que no reconcilia (otra entrada en el log)", _alterar(log, 1, input={"id": "Excepcion_delta_D"}),
             "R7")):
        at = NAV.atribuir_payload(p, ["ext::6.11"], ai, None, "parcial", lect, log_r1=alterado)
        R.caso(f"v1 del log: {nombre} -> el control falla y la corrida entera es inválida",
               not at["replay_ok"] and motivo in at["replay_fallas"][0]["motivo"]
               and not NAV.corrida_valida(buenas + [at]), at["replay_fallas"])
    # el mismo R7 por el adaptador: el step rechazado no tiene llamada aceptada en el mapa
    st, lg = _sesion(dir_, "v1log_rechazo", [("mcp__kg__ver_nodo", {"id": "Obligacion_ancla_A"}, s_obj, False)],
                     [{"evento": "llamada", "call_id": "mcp_kg-1-1", "n": 1, "tool": "ver_nodo",
                       "input": {"id": "Obligacion_ancla_A"}, "output_str": s_obj, "output_chars": len(s_obj),
                       "output_sha256": "1" * 64, "error": None}])
    p = ABN.adaptar(st, lg)
    at = NAV.atribuir_payload(p, ["ext::6.11"], ai, None, "parcial", lect, log_r1=lg)
    R.caso("v1 del log: un step que el adaptador rechazó -> el control falla (R7) y la corrida es inválida",
           not p["gate"]["atribuible"] and not at["replay_ok"] and "R7" in at["replay_fallas"][0]["motivo"],
           at["replay_fallas"])
    try:
        NAV.atribuir_payload(p, ["ext::6.11"], ai, index, "parcial", lect, log_r1=lg)
        R.caso("v1 del log: con log_r1, pasar además un índice que re-ejecuta es un error", False)
    except ValueError:
        R.caso("v1 del log: con log_r1, pasar además un índice que re-ejecuta es un error", True)
    return R.casos


# --------------------------------------------------------------------------- #
# El humo del banco                                                            #
# --------------------------------------------------------------------------- #
def humo(out_dir: Path) -> dict:
    """Las sesiones del grafo del humo: adaptador, lectores y atribución, con la presencia por AnclaIndexBanco sobre el
    grafo del humo (el kg_path del manifiesto de su índice por punto) y las v1 desde el log R1."""
    R = Registro()
    sesiones = sorted(d for d in HUMO_DIR.glob("humo_*/HUMO-*-kg") if d.is_dir())
    res = {"n_sesiones_kg": len(sesiones), "sesiones": []}
    lecturas_cache, anclas_cache = {}, {}
    for d in sesiones:
        sid = d.name
        st, lg = d / f"stream_{sid}.jsonl", d / f"log_r1_{sid}.jsonl"
        p = ABN.adaptar(st, lg, {"caso_id": sid})
        ini = AB.leer_log(lg)["inicio"]
        cfg = ini["config"]
        clave_idx = cfg["indice_puntos"]
        if clave_idx not in lecturas_cache:
            lecturas_cache[clave_idx] = NAV.cargar_lectura(BANCO_DIR / "mcp_kg" / clave_idx, cfg["sha256_manifiesto_indice"])
            anclas_cache[clave_idx] = NAV.AnclaIndexBanco.desde_indice(BANCO_DIR / "mcp_kg" / clave_idx,
                                                                       cfg["sha256_manifiesto_indice"])
        lect, ai = lecturas_cache[clave_idx], anclas_cache[clave_idx]
        mapa = p["gate"]["mapa_steps"]
        fila = {"sesion": sid, "servidor": ini.get("version_servidor"), "familias": cfg.get("familias"),
                "n_steps": p["gate"]["n_steps_adaptados"],
                "por_herramienta": dict(Counter(s["tool"] for s in p["trace"]["steps"])),
                "rechazos": len(p["gate"]["rechazos"]), "atribuible": p["gate"]["atribuible"],
                "completa_R3": p["banco"]["completitud_R3"]["completa"],
                "pedidos_sin_herramienta": p["banco"]["pedidos_sin_herramienta"]["n"],
                "steps_igual_al_log": sum(1 for m in mapa if m.get("sesion_igual_al_log")),
                "steps_truncados_por_transporte": sum(1 for m in mapa if m.get("sesion_truncada_por_transporte"))}
        R.caso(f"humo {sid}: adaptador nuevo, todas las llamadas reconciliadas con el log R1",
               fila["atribuible"] and fila["rechazos"] == 0 and fila["completa_R3"],
               {k: fila[k] for k in ("n_steps", "rechazos", "atribuible", "completa_R3")})
        h = AB.adaptar(st, lg, {"caso_id": sid})
        fila["adaptador_HEAD"] = {"atribuible": h["gate"]["atribuible"], "rechazos": len(h["gate"]["rechazos"])}
        # lectores, por herramienta: cuántas claves, ids y textos leen (sin el texto)
        por_tool = {}
        for sf in p["steps_full"]:
            if sf["tool"] not in NAV.TOOLS_NAV:
                continue
            lec = NAV.leer_paso(sf["tool"], sf["output"], lect)
            c = por_tool.setdefault(sf["tool"], Counter())
            c["llamadas"] += 1
            c["claves"] += len(lec["claves"])
            c["ids"] += len(lec["ids"])
            c["nodos_de_claves"] += len(lec["nodos_de_claves"])
            c["textos"] += len(lec["textos"])
            c["errores"] += lec["error"]
        fila["lectores"] = {t: dict(c) for t, c in sorted(por_tool.items())}
        # atribución sobre anclas derivadas de la propia traza (las claves que leyó), con la presencia del grafo del
        # humo (AnclaIndexBanco) y las v1 del log R1
        claves = []
        for sf in p["steps_full"]:
            if sf["tool"] in NAV.TOOLS_NAV:
                lec = NAV.leer_paso(sf["tool"], sf["output"], lect)
                claves += lec["claves"] + lec["textos"]
        anclas = list(dict.fromkeys(claves))[:12] + ["ext::999.999"]
        clases = Counter()
        consistencia = True
        atribuciones = []
        for a in anclas:
            at = NAV.atribuir_payload(p, [a], ai, None, "parcial", lect, log_r1=lg)
            atribuciones.append(at)
            clases[at["clase"]] += 1
            consistencia &= at["navegacion_b63"]["consistencia_steps_full_ok"]
        fila["atribucion_anclas_derivadas"] = {"n_anclas": len(anclas), "clases": dict(sorted(clases.items())),
                                               "consistencia_steps_full_ok": consistencia,
                                               "steps_v1_del_log": sum(1 for s in p["trace"]["steps"]
                                                                       if s["tool"] in NAV.TOOLS_V1),
                                               "corrida_valida": NAV.corrida_valida(atribuciones)}
        R.caso(f"humo {sid}: la atribución corre sobre la traza entera, con las v1 del log y la presencia del grafo",
               consistencia and fila["atribucion_anclas_derivadas"]["corrida_valida"]
               and sum(clases.values()) == len(anclas), fila["atribucion_anclas_derivadas"])
        res["sesiones"].append(fila)
        print("  ", json.dumps({k: fila[k] for k in ("sesion", "n_steps", "por_herramienta", "lectores",
                                                     "adaptador_HEAD", "atribucion_anclas_derivadas")},
                               ensure_ascii=False))
    res["lecturas"] = {k: v["fuente"] for k, v in lecturas_cache.items()}
    res["presencia"] = {k: v.fuente | {"n_anclas": len(v.por_ancla), "n_contenedores": len(v.contenedores)}
                        for k, v in anclas_cache.items()}
    res |= R.resumen()
    escribir(out_dir, "humo.json", res)
    return res


# --------------------------------------------------------------------------- #
# Los nombres de herramienta de B6.3                                           #
# --------------------------------------------------------------------------- #
def nombres_b63(out_dir: Path) -> dict:
    metas = sorted(METAS_B63.glob("*-kg.json"))
    nombres, con_call_id = set(), {}
    for p in metas:
        m = json.loads(p.read_text(encoding="utf-8"))
        for e in m.get("mapa_R7") or []:
            t = e.get("tool")
            nombres.add(t)
            con_call_id[t] = con_call_id.get(t, False) or bool(e.get("call_id_log"))
    filas = []
    for t in sorted(nombres, key=str):
        # el mapa_R7 puede traer el nombre sin el prefijo del servidor; el adaptador lee el de la sesión, con él
        en_la_sesion = str(t) if str(t).startswith("mcp__") else ABN.PREFIJO_KG + str(t)
        clase = ABN.clasificar_nombre(en_la_sesion)[0]
        filas.append({"nombre": t, "nombre_en_la_sesion": en_la_sesion, "es_una_de_las_diez": clase == "herramienta",
                      "clase_en_el_adaptador": clase, "alguna_entrada_con_call_id_log": con_call_id[t]})
    res = {"n_metas_kg_leidas": len(metas), "nombres": filas,
           "todos_reconocidos_o_mcp__kg": all(f["es_una_de_las_diez"] or f["nombre"] == "mcp__kg" for f in filas)}
    for f in filas:
        print(f"  {f['nombre']!s:28} una de las diez: {'sí' if f['es_una_de_las_diez'] else 'no':2}  "
              f"adaptador: {f['clase_en_el_adaptador']:15}  con call_id del log: {'sí' if f['alguna_entrada_con_call_id_log'] else 'no'}")
    print(f"  metas leídas: {len(metas)} · cada nombre es una de las diez o mcp__kg: {res['todos_reconocidos_o_mcp__kg']}")
    escribir(out_dir, "nombres_b63.json", res)
    return res


# --------------------------------------------------------------------------- #
# El lector de claves sobre el índice por punto de B6.3                        #
# --------------------------------------------------------------------------- #
def lector_claves_b63(out_dir: Path) -> dict:
    cfg = json.loads(CONFIG_KG_N7.read_text(encoding="utf-8"))
    lect = NAV.cargar_lectura(BANCO_DIR / "mcp_kg" / cfg["indice_puntos"], cfg["sha256_manifiesto_indice"])
    formas = Counter()
    no_leidas = Counter()
    for k in sorted(lect["nodos_por_punto"]):
        unidad = k.partition("::")[2]
        forma = ("cifras" if re.fullmatch(r"\d+(\.\d+)*", unidad) else "S+cifras" if re.fullmatch(r"S\d+(\.\d+)*", unidad)
                 else "S+letras" if re.fullmatch(r"S[A-Za-z]\w*(\.\d+)*", unidad) else "subdocumento::unidad"
                 if "::" in unidad else "otra")
        formas[forma] += 1
        leidas = [NAV._clave(par) for par in U.claves_en(f"fila | {k} | x", lect["man"])]
        if leidas != [k]:
            no_leidas[forma] += 1
    res = {"indice": lect["fuente"], "n_claves": sum(formas.values()), "por_forma": dict(sorted(formas.items())),
           "no_leidas_por_forma": dict(sorted(no_leidas.items())), "n_no_leidas": sum(no_leidas.values())}
    print("lector de claves sobre el índice de B6.3:", json.dumps({k: v for k, v in res.items() if k != "indice"},
                                                                    ensure_ascii=False))
    escribir(out_dir, "lector_claves_b63.json", res)
    return res


# --------------------------------------------------------------------------- #
# Vuelta b: la presencia sobre el grafo de B6.3, contra su índice por punto    #
# --------------------------------------------------------------------------- #
def presencia_b63(out_dir: Path) -> dict:
    """AnclaIndexBanco sobre el grafo de B6.3 (el kg_path del manifiesto de su índice por punto, sha256 controlado)
    contra el índice por punto que sirvió el banco (puntos.json), en todas sus claves que no son de tipo `to`: los
    mismos nodos, en el mismo orden. Las claves que el lector encuentra y el índice no, solo por cuántas son. No lee
    ninguna ancla ni ninguna pregunta de B6.3."""
    cfg = json.loads(CONFIG_KG_N7.read_text(encoding="utf-8"))
    indice = BANCO_DIR / "mcp_kg" / cfg["indice_puntos"]
    man = json.loads((indice / "manifiesto.json").read_text(encoding="utf-8"))
    if IP.sha256_file(indice / "puntos.json") != man["archivos"]["puntos.json"]:
        raise SystemExit("ABORTO: puntos.json no es el del manifiesto")
    puntos = json.loads((indice / "puntos.json").read_text(encoding="utf-8"))
    ai = NAV.AnclaIndexBanco.desde_indice(indice, cfg["sha256_manifiesto_indice"])
    nodos_idx = json.loads((indice / "nodos.json").read_text(encoding="utf-8"))
    claves = sorted(k for k, p in puntos.items() if p["tipo"] != "to")
    iguales = mismo_conjunto = misma_presencia = igual_sin_contenedores = 0
    contenedores_en_el_indice = set()
    for k in claves:
        to, _, resto = k.partition("::")
        r, i = ai.resolver(to, resto), puntos[k]["nodos"]
        iguales += r == i
        mismo_conjunto += set(r) == set(i)
        misma_presencia += bool(r) == bool(i)
        igual_sin_contenedores += r == [n for n in i if n not in ai.contenedores]
        contenedores_en_el_indice |= {n for n in i if n in ai.contenedores}
    del_lector = {f"{to}::{a}" for (to, a) in ai.por_ancla}
    solo_lector = del_lector - set(claves)
    con_nodos = sum(1 for k in claves if puntos[k]["nodos"])
    res = {"grafo": ai.fuente, "n_claves_del_indice": len(claves), "con_nodos_en_el_indice": con_nodos,
           "mismos_nodos_que_el_indice": iguales == len(claves), "mismos_nodos_y_orden": iguales,
           "mismo_conjunto": mismo_conjunto, "misma_presencia": misma_presencia,
           "igual_al_indice_sin_los_contenedores_del_2": igual_sin_contenedores,
           "contenedores_que_el_indice_lista": {
               "n": len(contenedores_en_el_indice),
               "por_tipo": dict(sorted(Counter(nodos_idx[n]["type"] for n in contenedores_en_el_indice).items())),
               "todos_de_mas_de_10_claves": all(ai.contenedores[n] > 10 for n in contenedores_en_el_indice),
               "claves_del_indice_que_llevan_alguno": len(claves) - iguales},
           "claves_del_lector_que_el_indice_no_tiene": len(solo_lector),
           "contenedores": {"n": len(ai.contenedores),
                            "por_mas_de_10_claves": sum(1 for v in ai.contenedores.values() if v > 10),
                            "TextoOrdenado_de_10_o_menos": sum(1 for i, v in ai.contenedores.items() if v <= 10)},
           "procedencias_sin_to_o_punto": len(ai.sin_parsear)}
    res["la_diferencia_son_solo_los_contenedores"] = (igual_sin_contenedores == len(claves)
                                                     and res["contenedores_que_el_indice_lista"]["todos_de_mas_de_10_claves"])
    si = lambda b: "sí" if b else "no"  # noqa: E731
    print(f"  mismos nodos que el índice, en todas las claves: {si(res['mismos_nodos_que_el_indice'])} "
          f"({iguales} de {len(claves)}); misma presencia: {misma_presencia} de {len(claves)}")
    print(f"  igual al índice sin los contenedores del §2: {igual_sin_contenedores} de {len(claves)}; "
          f"contenedores que el índice lista: {json.dumps(res['contenedores_que_el_indice_lista'], ensure_ascii=False)}")
    print(f"  contenedores del lector: {json.dumps(res['contenedores'], ensure_ascii=False)}; claves del lector que "
          f"el índice no tiene: {len(solo_lector)}; procedencias sin to o punto: {len(ai.sin_parsear)}")
    escribir(out_dir, "presencia_b63.json", res)
    return res


# --------------------------------------------------------------------------- #
# Vuelta b: la equivalencia de las v1 del log con la re-ejecución, en EV2      #
# --------------------------------------------------------------------------- #
def log_de_la_reejecucion(payload: dict, index) -> tuple[dict, dict]:
    """(log, payload con mapa): para cada step, una `llamada` cuyo output_str es el json.dumps de la re-ejecución de
    HEAD (metrica._reejecutar_step), con su sha256, y el mapa R7 step -> llamada que arma el adaptador del banco."""
    llamadas, mapa = [], []
    for i, st in enumerate(payload["trace"].get("steps", []), 1):
        s = json.dumps(_reejecutar_step(index, st), ensure_ascii=False)
        llamadas.append({"evento": "llamada", "call_id": f"reejecucion-{i}", "n": i, "tool": st["tool"],
                         "input": st.get("input"), "output_str": s, "output_chars": len(s),
                         "output_sha256": hashlib.sha256(s.encode("utf-8")).hexdigest(), "error": None})
        mapa.append({"n": st["n"], "n_log": i, "call_id_log": f"reejecucion-{i}", "ok": True,
                     "sesion_igual_al_log": None, "sesion_truncada_por_transporte": False})
    return {"llamadas": llamadas}, {**payload, "gate": {"mapa_steps": mapa}}


def _trazas_ev2(limite: int | None):
    from comun_ev2 import cargar_runtime, indice_anclas
    from comun_reporte import CORRIDA_DIR, ENC_DIR, ORDEN_GRAFOS, rel_repo
    from harness import GraphIndex
    for g in ORDEN_GRAFOS:
        aidx = indice_anclas(g)
        index = IndiceConMemoria(GraphIndex(cargar_runtime(g)))
        todas = sorted(f"{to}:{a}" for (to, a) in aidx.por_ancla)
        dirs = [CORRIDA_DIR / "trazas" / f"ev2_base_{'run3' if g == 'run_3' else g}"]
        dirs += [ENC_DIR / "trazas" / f"ev2_enc_{'run3' if g == 'run_3' else g}_r{r}" for r in (1, 2, 3)]
        ps = [p for d in dirs for p in sorted(d.glob("EV2F-*.json"))]
        for p in ps[:limite] if limite else ps:
            yield g, aidx, index, todas, p, rel_repo(p)


def equivalencia_ev2(out_dir: Path, limite: int | None = None) -> dict:
    from comun_ev2 import verificar_grafos
    shas = verificar_grafos(verbose=False)
    res = {"grafos_sha256": shas, "por_grafo": Counter(), "n_trazas": 0, "n_comparaciones": 0, "n_iguales": 0,
           "trazas_con_alguna_diferencia": [], "controles_del_log_que_fallan": 0}
    h_head, h_log = hashlib.sha256(), hashlib.sha256()
    for g, aidx, index, todas, p, rel in _trazas_ev2(limite):
        payload = json.loads(p.read_text(encoding="utf-8"))
        log, payload_log = log_de_la_reejecucion(payload, index)
        sorteo = random.Random(f"ATRIB_NAV:regresion:{rel}")
        anclas = anclas_derivadas(payload, aidx, sorteo, todas)
        llamadas = [([a], "parcial") for a in anclas] + [(anclas, "parcial"), (anclas[:1], "correcto")]
        distinta = False
        for lista, veredicto in llamadas:
            a = json.dumps(AF.atribuir_payload(payload, lista, aidx, index, veredicto), ensure_ascii=False)
            x = NAV.atribuir_payload(payload_log, lista, aidx, None, veredicto, log_r1=log)
            b = json.dumps(x, ensure_ascii=False)
            res["controles_del_log_que_fallan"] += len(x["replay_fallas"])
            res["n_comparaciones"] += 1
            res["n_iguales"] += a == b
            distinta |= a != b
            h_head.update(a.encode("utf-8"))
            h_log.update(b.encode("utf-8"))
        if distinta:
            res["trazas_con_alguna_diferencia"].append(rel)
        res["por_grafo"][g] += 1
        res["n_trazas"] += 1
    res["por_grafo"] = dict(res["por_grafo"])
    res["sha256_salidas_HEAD"] = h_head.hexdigest()
    res["sha256_salidas_v1_del_log"] = h_log.hexdigest()
    res["nota"] = ("las mismas anclas y llamadas que la regresión de EV2; el log de cada traza, armado con la "
                   "re-ejecución de HEAD")
    print("equivalencia EV2:", json.dumps({k: v for k, v in res.items() if k != "grafos_sha256"}, ensure_ascii=False))
    escribir(out_dir, "equivalencia_ev2.json", res)
    return res


# --------------------------------------------------------------------------- #
# Vuelta b: las salidas v1 de los logs R1 de B6.3, sin atribuir                #
# --------------------------------------------------------------------------- #
BANCO_B63_PASADA1 = Path.home() / "INGENIERIA IA" / "TESIS" / "fuera_del_repo" / "banco_b63" / "resultados" / "real" / "pasada1"


def _campos_v1(tool: str, obj) -> bool:
    """Los campos que lee la regla v1 (metrica.evaluar_traza): `resultados[*].id`, `id` (o el error de ver_nodo) y
    `salientes`/`entrantes` con `vecino_id` (la regla lee `res.get(...) or []`: con una dirección, basta una)."""
    if not isinstance(obj, dict):
        return False
    if "error" in obj and tool in ("ver_nodo", "ver_vecinos"):
        return "id" not in obj
    if tool == "buscar_nodos":
        return isinstance(obj.get("resultados"), list) and all(isinstance(r, dict) and "id" in r for r in obj["resultados"])
    if tool == "ver_nodo":
        return "id" in obj
    presentes = [k for k in ("salientes", "entrantes") if k in obj]
    return bool(presentes) and all(isinstance(obj[k], list) and all(isinstance(v, dict) and "vecino_id" in v
                                                                    for v in obj[k]) for k in presentes)


def v1_b63(out_dir: Path) -> dict:
    """Cada salida v1 de los logs R1 del brazo `kg` de B6.3: se lee como JSON, trae los campos de la regla v1 y da su
    output_sha256. Imprime solo sí o no y cuentas totales; ningún nombre de sesión ni ninguna salida."""
    logs = []
    for raiz, dirs, files in os.walk(BANCO_B63_PASADA1):
        dirs[:] = sorted(d for d in dirs if not d.startswith("NO_ABRIR_") and "_SOLO_MESA" not in d)
        for f in sorted(files):
            if f.startswith("NO_ABRIR_") or "_SOLO_MESA" in f or f.endswith(".claude.json") or ".env" in f:
                continue
            if f.startswith("log_r1_") and f.endswith("-kg.jsonl"):
                logs.append(Path(raiz) / f)
    n_v1 = n_err = 0
    servidor_kg = json_ok = sha_ok = campos_ok = True
    por_tool = Counter()
    for p in logs:
        lineas = [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]
        ini = next((x for x in lineas if x.get("evento") == "inicio"), {})
        servidor_kg &= ini.get("servidor") == "mcp_kg"
        for ll in lineas:
            if ll.get("evento") != "llamada" or ll.get("tool") not in NAV.TOOLS_V1:
                continue
            if ll.get("output_str") is None:
                n_err += 1
                continue
            n_v1 += 1
            por_tool[ll["tool"]] += 1
            s = ll["output_str"]
            sha_ok &= hashlib.sha256(s.encode("utf-8")).hexdigest() == ll.get("output_sha256")
            try:
                obj = json.loads(s)
            except json.JSONDecodeError:
                json_ok = campos_ok = False
                continue
            campos_ok &= _campos_v1(ll["tool"], obj)
    si = lambda b: "sí" if b else "no"  # noqa: E731
    res = {"n_logs_kg": len(logs), "n_salidas_v1": n_v1, "por_herramienta": dict(sorted(por_tool.items())),
           "n_llamadas_v1_con_error_del_servidor": n_err, "todos_del_servidor_mcp_kg": servidor_kg,
           "todas_se_leen_como_JSON": json_ok, "todas_con_los_campos_de_la_regla_v1": campos_ok,
           "todas_dan_su_output_sha256": sha_ok}
    print(f"  logs del brazo kg: {len(logs)} · salidas v1: {n_v1} · del servidor mcp_kg: {si(servidor_kg)}")
    print(f"  todas se leen como JSON: {si(json_ok)} · con los campos de la regla v1: {si(campos_ok)} · "
          f"dan su output_sha256: {si(sha_ok)}")
    escribir(out_dir, "v1_b63.json", res)
    return res


def main() -> int:
    ap = argparse.ArgumentParser()
    for f in ("--regresion-selftest", "--regresion-ev2", "--sinteticos", "--humo", "--nombres-b63",
              "--lector-claves-b63", "--presencia-b63", "--equivalencia-ev2", "--v1-b63"):
        ap.add_argument(f, action="store_true")
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--limite-trazas", type=int, default=None,
                    help="solo para estimar el tiempo: las primeras N trazas de cada grafo")
    a = ap.parse_args()
    rc = 0
    if a.regresion_selftest:
        r = regresion_selftest(a.out)
        rc |= not (r["selftest_head_rc"] == 0 and r["selftest_con_la_nueva_rc"] == 0
                   and r["llamadas_iguales_byte_a_byte"] == r["llamadas_comparadas"] and r["selftest_json_igual_salvo_generado"])
    if a.regresion_ev2:
        r = regresion_ev2(a.out, a.limite_trazas)
        rc |= r["n_iguales"] != r["n_comparaciones"]
    if a.equivalencia_ev2:
        r = equivalencia_ev2(a.out, a.limite_trazas)
        rc |= r["n_iguales"] != r["n_comparaciones"] or r["controles_del_log_que_fallan"] != 0
    if a.presencia_b63:
        r = presencia_b63(a.out)
        rc |= not r["la_diferencia_son_solo_los_contenedores"]
    if a.v1_b63:
        r = v1_b63(a.out)
        rc |= not (r["todos_del_servidor_mcp_kg"] and r["todas_se_leen_como_JSON"]
                   and r["todas_con_los_campos_de_la_regla_v1"] and r["todas_dan_su_output_sha256"])
    if a.sinteticos:
        r = sinteticos(a.out)
        rc |= r["n_ok"] != r["n_casos"]
    if a.humo:
        r = humo(a.out)
        rc |= r["n_ok"] != r["n_casos"]
    if a.nombres_b63:
        r = nombres_b63(a.out)
        rc |= not r["todos_reconocidos_o_mcp__kg"]
    if a.lector_claves_b63:
        lector_claves_b63(a.out)
    return int(rc)


if __name__ == "__main__":
    raise SystemExit(main())
