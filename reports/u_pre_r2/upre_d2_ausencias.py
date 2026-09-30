#!/usr/bin/env python3
"""upre_d2_ausencias.py — U-PRE-R2-DIAG, etapa D2: cruce de las ausencias con los candidatos.

Mandato: docs/mandatos/UPRE_R2_diagnostico.md (firmado el 2026-09-29), con las
decisiones de la autora del cierre de D1: (1) la regla de presencia del ancla es
la de regla_atribucion.md tal como está sellada (:83, coincidencia exacta, sin
descendientes; «y sus descendientes» de la decisión 8 fue un error del
mandato); (2) los pares de C1 salen de ev2_r1/cierre/cierre_r1.json (774acac),
con la clase A0.2 de esa misma fuente; (3) nota aparte sobre T2.

Solo lectura, USD 0, sin API y sin Neo4j (los módulos de E6 se importan; no se
abre ninguna conexión). La única db que se abre es la de reintentos de E1, con
file:…?immutable=1. Escribe únicamente en --out-dir.

Población: pares definitivos parcial o incorrecto de C1 a C4 con clase A0.2
ausencia_kg (C1: cierre_r1.json; C2 a C4: reports/tanda0/atribucion_tanda0.json).
Esperado 8 + 6 + 8 + 9 = 31; cualquier diferencia frena la corrida.

Reglas declaradas (se aplican igual en las dos generaciones):
  R-CITA  Claves de la cita textual de un criterio: números (incluye
          porcentajes, fechas y plazos: regex \\d+([./,]\\d+)*%?), siglas
          (dos o más mayúsculas) y palabras de contenido (5 letras o más, fuera
          de una lista fija de palabras vacías), todo normalizado (sin acentos,
          minúsculas). Un texto CONTIENE la cita si tiene todos los números y
          siglas y al menos el 80 % de las palabras; la contiene PARCIALMENTE si
          tiene al menos el 50 % de las palabras sin cumplir lo anterior; si no,
          no la contiene. Lo parcial no se resuelve: «requiere lectura».
  R-UBIC  Ubicación en E0: unidades del subárbol del ancla (unidad igual al
          punto, o que empieza con «punto.» o «punto::») cuyo texto propio
          contiene la cita; si ninguna, las que la contienen en el texto
          heredado desde el subárbol; si ninguna, las unidades del mismo TO
          fuera del subárbol (candidato D, requiere lectura).
  R-PRES  Contenido presente en el grafo: nodo cuyo texto (label y valores de
          properties) contiene la cita y que ancla (cualquier provenance) en el
          subárbol del ancla. Contenedor = nodo con más de 10 anclas distintas
          (resolucion.CONTENEDOR_MAX_ANCLAS, el mismo corte de A0.2).
  R-CAT   Categoría de un criterio no cubierto (decisión 7 del mandato):
          si el contenido está presente en un nodo no contenedor con aristas →
          P (fuera de la lista de la decisión 7: no hay pérdida en el pipeline;
          la ausencia la produce la coincidencia exacta de A0.2); presente solo
          en nodos no contenedores sin aristas → C; presente solo en
          contenedores → F. Si no está presente, en este orden: E (alguna unidad
          portadora con error o corte en E1, o con contenido_tabular de E0 y
          sin la cita en la salida de E1); G (la salida de E1 de las unidades
          portadoras —primera pasada cruda, reintento crudo y final validada—
          no contiene la cita); F (E1 la emitió y el nodo de su slug
          entity_slug_v3 está en el grafo sin la cita: se fundió y ganó otra
          escritura); H (E1 la emitió y el nodo de su slug no está: se perdió
          entre E1 y E2). Antes de G: si la cita está en la unión de los nodos
          (o de las entidades de E1) de una unidad portadora y en ninguno solo,
          «requiere lectura» (contenido repartido). Secundarias: B si E1 emitió
          la cita en una unidad portadora y alguna relación de esa entidad fue
          rechazada por firma_invalida; E-tabla si una unidad portadora es
          tabular y la primaria es otra; E-tabla-no-marcada si una unidad
          portadora no marcada como tabular por E0 tiene 3 o más líneas que
          empiezan con un código de 6 dígitos o más. Las reglas de unión y de
          tabla no marcada se agregaron después de una corrida de prueba en el
          scratchpad (declarado en el reporte de D2).
  Categoría de la fila: la primera, en el orden E, G, B, F, C, D, H, P, entre
  las de sus criterios no cubiertos; las demás, secundarias.

Uso (desde la raíz del repo):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B reports/u_pre_r2/upre_d2_ausencias.py --out-dir reports/u_pre_r2
"""
from __future__ import annotations

import sys

sys.dont_write_bytecode = True

import argparse
import hashlib
import json
import re
import sqlite3
import unicodedata
import urllib.parse
from collections import Counter, OrderedDict, defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "scripts"))
sys.path.insert(0, str(RAIZ / "data" / "experiment" / "ev2_tanda0" / "code"))
import regression_kg as RK        # noqa: E402  direccionamiento por provenances (sin editar)
import atribucion_tanda0 as AT    # noqa: E402  módulo de E6 (sin editar): veredictos, censo A0.2

REX = RAIZ / "data" / "experiment" / "reextraccion_v2"
for _p in (REX / "e2_reduce", REX / "corpus_v2", RAIZ / "data" / "experiment" / "grafo_v2" / "code"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))
import e2_lib                     # noqa: E402  entity_slug_v3 (e2_lib.py:110)

# --------------------------------------------------------------------------- #
# Entradas                                                                     #
# --------------------------------------------------------------------------- #
ENTRADAS = OrderedDict([
    ("kg_r1", ("data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json",
               "0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a")),
    ("kg_desarrollo", ("data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo/r1/kg.json",
                       "eab2fdd01dec4dad026d596a793919e666920fab127d7efb14b5b00857ae64ef")),
    ("cierre_r1_C1", ("data/experiment/ev2_r1/cierre/cierre_r1.json", None)),
    ("atribucion_tanda0", ("reports/tanda0/atribucion_tanda0.json",
                           "00b3c0a738b1d0de2e08dab606744407c3dd57b8aa57ed422ac0b6b381c896ce")),
    ("definitivos_tanda0", ("data/experiment/ev2_tanda0/adjudicacion_SOLO_MESA/definitivos_por_par_tanda0_SOLO_MESA.json", None)),
    ("gold_ev2", ("data/experiment/exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json", None)),
    ("regla_atribucion", ("data/experiment/ev2_reporte/regla_atribucion.md", None)),
    ("laudo_r2", ("docs/laudo_release_r2_pipeline.md", None)),
    ("p4_filas_rechazos_desarrollo", ("reports/u_audit_tipos_v3/p4_filas.json", None)),
    ("uestmat_poblacion_final", ("reports/u_estudio_matriz/uestmat_poblacion_final.json", None)),
    ("e1_reintentos_db", ("data/experiment/reextraccion_v2/e3_verificador/cache/e1_reintentos.db", None)),
])
GEN = OrderedDict([
    ("r1", {"kg": "kg_r1", "salida_e1": "data/experiment/reextraccion_v2/corpus_v2/salida",
            "nombre": "KG-Reextraído-r1 (0226e947…)", "celdas": ("C1", "C2")}),
    ("desarrollo", {"kg": "kg_desarrollo", "salida_e1": "data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida",
                    "nombre": "KG-Tanda0-Desarrollo-r1 (eab2fdd0…)", "celdas": ("C3", "C4")}),
])
OTRA = {"r1": "desarrollo", "desarrollo": "r1"}
CELDA_GEN = {"C1": "r1", "C2": "r1", "C3": "desarrollo", "C4": "desarrollo"}
ESPERADO = {"C1": 8, "C2": 6, "C3": 8, "C4": 9}
E0_TANDA0 = "data/experiment/reextraccion_v2/e0_chunking/salida_tanda0"
E0_ENM01 = "data/experiment/reextraccion_v2/e0_chunking/salida_enm01"
TOS = ("pro", "cla", "ric", "cap", "ext")
NS_V3 = "e1_extraccion|cv=e1-extractor-v1-p54a111e2175f|think=0"
CONTENEDOR = 10
CMD = "PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B reports/u_pre_r2/upre_d2_ausencias.py --out-dir reports/u_pre_r2"

ORDEN = ("E", "G", "B", "F", "C", "D", "H", "P")
CATEGORIAS = OrderedDict([
    ("E", "el chunk del ancla no se extrajo o se cortó, o su contenido es una tabla linealizada"),
    ("G", "E1 no lo emitió: sin rastro en su salida"),
    ("B", "E1 lo emitió y la matriz rechazó su relación por firma_invalida"),
    ("F", "quedó fundido o duplicado en otro nodo"),
    ("C", "está en el grafo sin la arista que lo conecta"),
    ("D", "depende de una remisión no resuelta o falsa"),
    ("H", "no decidible con el material"),
    ("P", "fuera de la lista de la decisión 7: el contenido está en el grafo bajo una ancla descendiente; no hay pérdida en el pipeline"),
])
CANDIDATO = {
    "E-corte": "§1.1 BKL-0030 (reintento por corte y partición)",
    "E-tabla": "§1.3 BKL-0006 / RX-10 (cablear el parser de tablas a E0)",
    "E-tabla-no-marcada": "§1.3 BKL-0006 / RX-10, si la unidad que E0 no marca como tabular se trata como tabla",
    "G": "fuera de r2 (toca el prompt de E1; «Qué no es» del laudo)",
    "B": "decisión sobre la matriz congelada (checklist X1 y X11); fuera del §1",
    "F": "§4 H2 (clave de fusión) y §1.2 BKL-0031 (detector de duplicados)",
    "C": "§4 nodos sin ninguna arista (establecida_en derivada)",
    "D": "§4 H1/H4, remisiones por paráfrasis y procedencia de las remisiones",
    "H": "—",
    "P": "fuera de r2 (no es pérdida del pipeline: granularidad del ancla bajo la regla exacta de A0.2)",
}
STOP = frozenset((
    "para como sobre entre desde hasta cuando donde deberan debera podra podran seran sera esta estas estos "
    "este dicha dicho dichos dichas otras otros otra otro cada toda todas todo todos tales segun mediante "
    "durante tambien siempre cuales cual respecto caso casos forma misma mismo mismas mismos").split())


# --------------------------------------------------------------------------- #
# Utilidades                                                                    #
# --------------------------------------------------------------------------- #
def sha256_path(p: Path) -> str:
    h = hashlib.sha256()
    with Path(p).open("rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def leer(p):
    return json.loads((RAIZ / p).read_text(encoding="utf-8")) if not Path(p).is_absolute() else json.loads(Path(p).read_text(encoding="utf-8"))


def verificar_entradas() -> OrderedDict:
    out, malos = OrderedDict(), []
    for k, (ruta, esp) in ENTRADAS.items():
        s = sha256_path(RAIZ / ruta)
        out[k] = {"ruta": ruta, "sha256": s}
        if esp is not None:
            out[k]["sha256_esperado"] = esp
            if s != esp:
                malos.append(k)
    if malos:
        raise SystemExit(f"FRENO: sha256 distinto del esperado en {malos}")
    return out


def normalizar(s) -> str:
    s = unicodedata.normalize("NFD", str(s or ""))
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.replace("\u2013", " ").replace("\u2014", " ").replace("\u201c", '"').replace("\u201d", '"')
    return re.sub(r"\s+", " ", s.lower()).strip()


RE_NUM = re.compile(r"\d+(?:[./,]\d+)*%?")
RE_SIGLA = re.compile(r"\b[A-ZÁÉÍÓÚÑ]{2,}\b")
RE_PAL = re.compile(r"[a-zñ]+")


def claves(cita: str) -> tuple:
    nums = sorted({t.rstrip(".") for t in RE_NUM.findall(normalizar(cita))})
    siglas = sorted({normalizar(t) for t in RE_SIGLA.findall(cita)})
    pals = sorted({w for w in RE_PAL.findall(normalizar(cita)) if len(w) >= 5 and w not in STOP})
    return nums, siglas, pals


def tokens(texto: str) -> set:
    n = normalizar(texto)
    return set(RE_PAL.findall(n)) | {t.rstrip(".") for t in RE_NUM.findall(n)}


def evaluar_cita(cita: str, texto: str) -> str:
    """R-CITA → 'presente' | 'parcial' | 'ausente'."""
    nums, siglas, pals = claves(cita)
    T = tokens(texto)
    req_ok = all(x in T for x in nums + siglas)
    cov = (sum(1 for w in pals if w in T) / len(pals)) if pals else 1.0
    if req_ok and cov >= 0.8:
        return "presente"
    if cov >= 0.5:
        return "parcial"
    return "ausente"


def texto_nodo(n: dict) -> str:
    return " | ".join([n.get("label") or ""] + list(RK._vals(n.get("properties") or {})))


def texto_entidad(e: dict) -> str:
    return " | ".join([e.get("label") or ""] + list(RK._vals(e.get("properties") or {})))


def en_subarbol(punto: str, ancla: str) -> bool:
    return punto == ancla or punto.startswith(ancla + ".") or punto.startswith(ancla + "::")


# --------------------------------------------------------------------------- #
# Población                                                                    #
# --------------------------------------------------------------------------- #
def poblacion(gold: dict) -> list:
    filas = []
    c1 = leer(ENTRADAS["cierre_r1_C1"][0])["atribucion"]
    reprs = {r["id_pregunta"]: r for r in c1["reprs"]}
    for p in c1["pares_definitivos"]["por_par"]:
        if p["definitivo"] in ("parcial", "incorrecto") and p["clase"] == "ausencia_kg":
            r = reprs[p["id_pregunta"]]
            repr_ = r["repr_origen"] if r["repr_rep"] is None else f"{r['repr_origen']}_r{r['repr_rep']}"
            filas.append({"celda": "C1", "id_pregunta": p["id_pregunta"], "definitivo": p["definitivo"], "via": p["via"],
                          "repr": repr_, "marcas": list(r["repr_marcas"]),
                          "fuente_clase": "data/experiment/ev2_r1/cierre/cierre_r1.json → atribucion.pares_definitivos.por_par",
                          "fuente_marcas": "data/experiment/ev2_r1/cierre/cierre_r1.json → atribucion.reprs[].repr_marcas"})
    at = leer(ENTRADAS["atribucion_tanda0"][0])
    defs_all = leer(ENTRADAS["definitivos_tanda0"][0])
    for c in ("C2", "C3", "C4"):
        celda = AT.ce0.CELDAS[c]
        ins = AT.pt.cargar_insumos(celda)
        vb, ve, _ = AT.veredictos_por_traza(celda, ins, defs_all["celdas"][c]["definitivos"])
        for p in at["celdas"][c]["pares_definitivos"]["por_par"]:
            if p["definitivo"] in ("parcial", "incorrecto") and p["clase"] == "ausencia_kg":
                if p["repr"] == "base":
                    v = vb[p["id_pregunta"]]
                else:
                    v = ve[(p["id_pregunta"], int(p["repr"].split("_r")[1]))]
                if v["veredicto"] != p["definitivo"]:
                    raise SystemExit(f"FRENO: veredicto de la traza representativa ≠ definitivo en {c} {p['id_pregunta']}")
                filas.append({"celda": c, "id_pregunta": p["id_pregunta"], "definitivo": p["definitivo"], "via": p["via"],
                              "repr": p["repr"], "marcas": list(v["marcas"]),
                              "fuente_clase": f"reports/tanda0/atribucion_tanda0.json → celdas.{c}.pares_definitivos.por_par",
                              "fuente_marcas": f"atribucion_tanda0.veredictos_por_traza (import) sobre juez_out de {c} y {ENTRADAS['definitivos_tanda0'][0]}"})
    for f in filas:
        q = gold[f["id_pregunta"]]
        f["ancla"] = q["gold"]["ancla"][0]
        if len(q["gold"]["ancla"]) != 1:
            raise SystemExit(f"FRENO: {f['id_pregunta']} con más de un ancla")
        if len(f["marcas"]) != len(q["gold"]["criterios"]):
            raise SystemExit(f"FRENO: marcas y criterios no alinean en {f['celda']} {f['id_pregunta']}")
        f["criterios_no_cubiertos"] = [i + 1 for i, m in enumerate(f["marcas"]) if m != "cumplido"]
    return filas


# --------------------------------------------------------------------------- #
# Contexto por generación                                                      #
# --------------------------------------------------------------------------- #
class Generacion:
    def __init__(self, clave: str, chunks: dict, db):
        g = GEN[clave]
        self.clave = clave
        self.kg_path = RAIZ / ENTRADAS[g["kg"]][0]
        self.G = RK.Grafo.desde_ruta(self.kg_path)
        self.aidx = AT.indice_anclas(self.kg_path, None)
        self.chunks = chunks
        self.db = db
        self.consultas_reintento = {}
        self.salida = g["salida_e1"]
        self.grado = Counter()
        for e in self.G.E:
            self.grado[e["source"]] += 1
            self.grado[e["target"]] += 1
        self.anclas_nodo = {}
        for n in self.G.N:
            s = set()
            for p in RK.provenances(n):
                if RK.formato_provenance(p) == 3 and p.get("to"):
                    s.add((p["to"], str(p.get("punto") or "")))
            self.anclas_nodo[n["id"]] = s
        self.e1 = {}
        self.finales = {}
        for to in TOS:
            d = RAIZ / self.salida / to
            for nombre, destino in (("extracciones_e1.jsonl", self.e1), (f"extracciones_finales_{to}.jsonl", self.finales)):
                ruta = d / nombre
                for i, ln in enumerate(ruta.read_text(encoding="utf-8").splitlines(), 1):
                    if ln.strip():
                        r = json.loads(ln)
                        destino.setdefault(r["chunk_id"], []).append((f"{self.salida}/{to}/{nombre}:{i}", r))

    def presente_ancla(self, ancla: str) -> OrderedDict:
        """Resolución del ancla con resolucion.AnclaIndex (regla sellada de A0.2) y,
        como evidencia, con descendientes y con contenedores; diagnóstico descriptivo
        (no es categoría): granularidad si el contenido ancla en descendientes."""
        to, pt = AT.parse_ancla(ancla)
        exacta = self.aidx.resolver(to, pt)
        desc = self.aidx.resolver(to, pt, incluir_descendientes=True)
        cont = [i for i in self.aidx.resolver(to, pt, incluir_contenedores=True) if i not in exacta]
        tipos_cont = sorted({self.G.tipo(i) for i in cont})
        if exacta:
            diag = "resuelve"
        elif desc:
            diag = "granularidad: el ancla no tiene nodos propios y el contenido ancla en descendientes"
        elif cont and tipos_cont == ["TextoOrdenado"]:
            diag = "sin nodos de contenido: solo el nodo TextoOrdenado (contenedor) porta el ancla"
        elif cont:
            diag = "solo contenedores de contenido"
        else:
            diag = "sin nodos"
        return OrderedDict([("exacta_A0_2", len(exacta)), ("con_descendientes", len(desc)),
                            ("contenedores", [{"id": i, "type": self.G.tipo(i), "n_anclas": self.aidx.contenedores.get(i)} for i in sorted(cont)]),
                            ("diagnostico", diag)])

    def nodos_con_cita(self, to: str, ancla_pt: str, cita: str) -> list:
        out = []
        for n in self.G.N:
            if n.get("type") in ("TextoOrdenado", "Sujeto"):
                continue
            anc = [p for t, p in self.anclas_nodo[n["id"]] if t == to and en_subarbol(p, ancla_pt)]
            if not anc:
                continue
            est = evaluar_cita(cita, texto_nodo(n))
            if est == "ausente":
                continue
            n_anc = len(self.anclas_nodo[n["id"]])
            out.append({"id": n["id"], "type": n["type"], "estado_cita": est, "anclas_en_subarbol": sorted(anc),
                        "n_anclas": n_anc, "contenedor": n_anc > CONTENEDOR, "grado": self.grado.get(n["id"], 0)})
        return sorted(out, key=lambda d: d["id"])

    def salida_e1_unidad(self, cid: str) -> list:
        """Textos de entidades emitidas por E1 para la unidad: primera pasada cruda
        (tool_input_crudo), validada, final (tras E3/reintento) y reintento crudo (db)."""
        out = []
        for ref, r in self.e1.get(cid, []):
            for e in ((r.get("tool_input_crudo") or {}).get("entities") or []):
                out.append(("e1_crudo", ref, e))
            for e in ((r.get("validacion") or {}).get("entidades") or []):
                out.append(("e1_validada", ref, e))
        for ref, r in self.finales.get(cid, []):
            for e in ((r.get("validacion") or {}).get("entidades") or []):
                out.append(("final", ref, e))
            if r.get("estado_e3") == "aceptado_tras_reintento":
                for ref_db, e in self.reintento_crudo(cid):
                    out.append(("reintento_crudo", ref_db, e))
        return out

    def reintento_crudo(self, cid: str) -> list:
        """Reintentos de E1 de la unidad en e1_reintentos.db (immutable=1). El pedido
        no lleva el chunk_id: se identifica por «TO: <to>» y «Punto del chunk: <unidad> »
        del mensaje de usuario, verificados tras decodificar el pedido."""
        to, unidad = cid.split("::", 1)
        cur = self.db.cursor()
        ns_cond = "namespace = ?" if self.clave == "desarrollo" else "namespace != ?"
        filas = cur.execute(f"select key, request_json, raw_json from cache where {ns_cond} and request_json like ? order by key",
                            (NS_V3, f"%Punto del chunk: {unidad} %")).fetchall()
        out, n = [], 0
        for key, req, raw in filas:
            try:
                msgs = json.loads(req).get("messages") or []
                msg = json.loads(raw)
            except json.JSONDecodeError:
                continue
            u = msgs[0]["content"] if msgs and isinstance(msgs[0]["content"], str) else " ".join(
                b.get("text", "") for b in (msgs[0]["content"] if msgs else []) if isinstance(b, dict))
            if f"| TO: {to} |" not in u.replace("\n", " | ") and f"TO: {to}\n" not in u:
                continue
            m = re.search(r"Punto del chunk: (\S+)", u)
            if not m or m.group(1) != unidad:
                continue
            n += 1
            for blk in msg.get("content") or []:
                if blk.get("type") == "tool_use":
                    for e in (blk.get("input") or {}).get("entities") or []:
                        out.append((f"{ENTRADAS['e1_reintentos_db'][0]} key {key[:12]}…", e))
        self.consultas_reintento[cid] = n
        return out

    def nodos_de_unidad(self, cid: str) -> list:
        """Nodos de contenido con alguna provenance en el punto de la unidad (sin
        el sufijo ::intro/::cierre)."""
        to, unidad = cid.split("::", 1)
        pt = unidad.split("::")[0]
        return [n for n in self.G.N if n.get("type") not in ("TextoOrdenado", "Sujeto")
                and (to, pt) in self.anclas_nodo[n["id"]]]

    def estado_unidad(self, cid: str) -> OrderedDict:
        e1 = [r for _, r in self.e1.get(cid, [])]
        fin = [r for _, r in self.finales.get(cid, [])]
        chunk = self.chunks.get(cid) or {}
        lineas_codigo = sum(1 for ln in (chunk.get("texto") or "").splitlines() if re.match(r"^\s*\d{6,}[X\d]*\s", ln))
        return OrderedDict([
            ("lineas_con_codigo_E0", lineas_codigo),
            ("registros_e1", len(e1)),
            ("errores_e1", sorted({str(r.get("error")) for r in e1 if r.get("error")})),
            ("stop_reason_e1", sorted({str(r.get("stop_reason")) for r in e1})),
            ("final", bool(fin)),
            ("error_final", sorted({str(r.get("error")) for r in fin if r.get("error")})),
            ("estado_e3", sorted({str(r.get("estado_e3")) for r in fin})),
            ("contenido_tabular_E0", bool((chunk.get("flags") or {}).get("contenido_tabular"))),
        ])

    def rechazos_firma(self, cid: str, cita: str) -> list:
        """Relaciones rechazadas por firma_invalida en la primera pasada de la unidad
        cuya entidad de origen o destino (en el crudo) contiene la cita."""
        out = []
        for ref, r in self.e1.get(cid, []):
            crudo = r.get("tool_input_crudo") or {}
            ents = {e.get("id") or e.get("local_id"): e for e in crudo.get("entities") or []}
            for rz in (r.get("validacion") or {}).get("rechazos") or []:
                if rz.get("motivo") != "firma_invalida":
                    continue
                el = rz.get("elemento") or {}
                for extremo in (el.get("source"), el.get("target")):
                    e = ents.get(extremo)
                    if e is not None and evaluar_cita(cita, texto_entidad(e)) == "presente":
                        out.append({"ref": ref, "detalle": rz.get("detalle")})
                        break
        return out


# --------------------------------------------------------------------------- #
# Diagnóstico por (generación, ancla, criterio)                                #
# --------------------------------------------------------------------------- #
def ubicar_e0(chunks_to: list, ancla_pt: str, cita: str) -> OrderedDict:
    """R-UBIC: texto propio; si no, texto completo que recibe E1 (herencia desde
    el subárbol del ancla + texto propio, en ese orden); si no, fuera del subárbol."""
    propias, herencia, parciales, fuera = [], [], [], []
    for u in chunks_to:
        if en_subarbol(u["unidad"], ancla_pt):
            est = evaluar_cita(cita, u["texto"])
            if est == "presente":
                propias.append(u["id"])
                continue
            hs = [h.get("texto") or "" for h in u.get("herencia") or [] if en_subarbol(str(h.get("unidad_origen")), ancla_pt)]
            est_h = evaluar_cita(cita, "\n".join(hs + [u["texto"]])) if hs else "ausente"
            if est_h == "presente":
                herencia.append(u["id"])
            elif "parcial" in (est, est_h):
                parciales.append(u["id"])
    if not propias and not herencia:
        fuera = [u["id"] for u in chunks_to if not en_subarbol(u["unidad"], ancla_pt) and evaluar_cita(cita, u["texto"]) == "presente"]
    return OrderedDict([("propias", propias), ("solo_herencia", herencia), ("parciales", parciales), ("fuera_del_subarbol", fuera)])


def diagnosticar(gen: Generacion, ancla: str, cita: str) -> OrderedDict:
    to, pt = AT.parse_ancla(ancla)
    ub = ubicar_e0([c for c in gen.chunks.values() if c["to"] == to], pt, cita)
    nodos = gen.nodos_con_cita(to, pt, cita)
    pres = [n for n in nodos if n["estado_cita"] == "presente"]
    d = OrderedDict([("e0", ub), ("nodos_con_cita", nodos)])
    portadoras = ub["propias"] + ub["solo_herencia"]
    secundarias = []
    no_cont = [n for n in pres if not n["contenedor"]]
    if no_cont and any(n["grado"] > 0 for n in no_cont):
        cat, motivo = "P", "contenido presente en un nodo con aristas bajo el subárbol del ancla"
    elif no_cont:
        cat, motivo = "C", "contenido presente solo en nodos sin aristas"
    elif pres:
        cat, motivo = "F", "contenido presente solo en nodos contenedores (más de 10 anclas)"
    elif not portadoras:
        if ub["parciales"] or any(n["estado_cita"] == "parcial" for n in nodos):
            cat, motivo = "requiere_lectura", "la cita se ubica solo parcialmente (R-CITA)"
        elif ub["fuera_del_subarbol"]:
            cat, motivo = "requiere_lectura", "la cita está en E0 fuera del subárbol del ancla (candidato D)"
            secundarias.append("D")
        else:
            cat, motivo = "requiere_lectura", "la cita no se ubica en E0 con R-CITA"
    else:
        estados = {cid: gen.estado_unidad(cid) for cid in portadoras}
        d["unidades_portadoras"] = estados
        salidas = [(src, ref, e, cid) for cid in portadoras for src, ref, e in gen.salida_e1_unidad(cid)]
        emitidas = [(src, ref, e, cid) for src, ref, e, cid in salidas if evaluar_cita(cita, texto_entidad(e)) == "presente"]
        parciales_e1 = [x for x in salidas if evaluar_cita(cita, texto_entidad(x[2])) == "parcial"]
        union_e1 = {cid: evaluar_cita(cita, "\n".join(texto_entidad(e) for _, _, e, c in salidas if c == cid)) for cid in portadoras}
        union_nodos = {cid: evaluar_cita(cita, "\n".join(texto_nodo(n) for n in gen.nodos_de_unidad(cid))) for cid in portadoras}
        d["union_entidades_e1_por_unidad"] = union_e1
        d["union_nodos_por_unidad"] = union_nodos
        d["e1_emitida_en"] = sorted({f"{src} {ref}" for src, ref, _, _ in emitidas})
        cortada = [cid for cid, s in estados.items() if s["errores_e1"] or s["error_final"] or "max_tokens" in s["stop_reason_e1"] or not s["final"]]
        tabular = [cid for cid, s in estados.items() if s["contenido_tabular_E0"]]
        tabla_no_marcada = [cid for cid, s in estados.items() if not s["contenido_tabular_E0"] and s["lineas_con_codigo_E0"] >= 3]
        if cortada:
            cat, motivo = "E-corte", f"unidad portadora con error, corte o sin salida final: {cortada}"
        elif not emitidas and tabular:
            cat, motivo = "E-tabla", f"unidad portadora tabular en E0 y sin la cita en la salida de E1: {tabular}"
        elif not emitidas and "presente" in union_nodos.values():
            cat, motivo = "requiere_lectura", "la cita está repartida entre varios nodos de la unidad portadora (ningún nodo la contiene solo)"
        elif not emitidas and "presente" in union_e1.values():
            cat, motivo = "requiere_lectura", "la cita está repartida entre varias entidades de la salida de E1 (ninguna la contiene sola)"
        elif not emitidas and parciales_e1:
            cat, motivo = "requiere_lectura", "la salida de E1 contiene la cita solo parcialmente"
        elif not emitidas:
            cat, motivo = "G", "la salida de E1 de las unidades portadoras no contiene la cita"
        else:
            e = emitidas[0][2]
            nid = f"{e.get('type')}_{e2_lib.entity_slug_v3(e)}"
            n = gen.G.by_id.get(nid)
            d["nodo_del_slug"] = {"id": nid, "presente": n is not None,
                                  "contiene_cita": (evaluar_cita(cita, texto_nodo(n)) if n else None)}
            if n is not None and evaluar_cita(cita, texto_nodo(n)) != "presente":
                cat, motivo = "F", "E1 la emitió; el nodo de su slug está en el grafo sin la cita (se fundió y ganó otra escritura)"
            elif n is None:
                cat, motivo = "H", "E1 la emitió y el nodo de su slug no está en el grafo"
            else:
                cat, motivo = "H", "E1 la emitió y el nodo de su slug tiene la cita pero no ancla en el subárbol"
        if tabular and cat not in ("E-tabla",):
            secundarias.append("E-tabla")
        if tabla_no_marcada:
            secundarias.append("E-tabla-no-marcada")
            d["tabla_no_marcada_por_E0"] = tabla_no_marcada
    if portadoras:
        rech = [x for cid in portadoras for x in gen.rechazos_firma(cid, cita)]
        d["rechazos_firma_invalida_con_la_cita"] = rech
        if rech:
            secundarias.append("B")
    d["categoria"] = cat
    d["motivo"] = motivo
    d["secundarias"] = sorted(set(secundarias))
    return d


def base_cat(c: str) -> str:
    return c.split("-")[0] if c not in ("requiere_lectura",) else c


def candidato(c: str) -> str:
    return CANDIDATO.get(c, "requiere lectura (sin candidato)")


# --------------------------------------------------------------------------- #
# Construcción                                                                 #
# --------------------------------------------------------------------------- #
def construir() -> OrderedDict:
    entradas = verificar_entradas()
    gold = {p["id"]: p for p in leer(ENTRADAS["gold_ev2"][0])["preguntas"]}
    filas = poblacion(gold)
    conteo = Counter(f["celda"] for f in filas)
    if dict(conteo) != ESPERADO:
        raise SystemExit(f"FRENO: población {dict(conteo)} ≠ {ESPERADO}")

    chunks, e0_identico = {}, OrderedDict()
    for to in TOS:
        a, b = RAIZ / E0_TANDA0 / f"chunks_{to}.json", RAIZ / E0_ENM01 / f"chunks_{to}.json"
        e0_identico[to] = a.read_bytes() == b.read_bytes()
        for c in json.loads(a.read_text(encoding="utf-8")):
            chunks[c["id"]] = c
    dbp = (RAIZ / ENTRADAS["e1_reintentos_db"][0]).resolve()
    db = sqlite3.connect(f"file:{urllib.parse.quote(str(dbp))}?immutable=1", uri=True)
    try:
        gens = {k: Generacion(k, chunks, db) for k in GEN}
        cache = {}
        for f in filas:
            gen_k = CELDA_GEN[f["celda"]]
            q = gold[f["id_pregunta"]]
            crit = []
            for i in f["criterios_no_cubiertos"]:
                cita = q["gold"]["criterios"][i - 1]["cita_textual"]
                for gk in (gen_k, OTRA[gen_k]):
                    key = (gk, f["ancla"], i, f["id_pregunta"])
                    if key not in cache:
                        cache[key] = diagnosticar(gens[gk], f["ancla"], cita)
                d = cache[(gen_k, f["ancla"], i, f["id_pregunta"])]
                o = cache[(OTRA[gen_k], f["ancla"], i, f["id_pregunta"])]
                crit.append(OrderedDict([("indice", i), ("criterio", q["gold"]["criterios"][i - 1]["criterio"]),
                                         ("cita_textual", cita), ("claves_R_CITA", dict(zip(("numeros", "siglas", "palabras"), claves(cita)))),
                                         ("categoria", d["categoria"]), ("motivo", d["motivo"]), ("secundarias", d["secundarias"]),
                                         ("diagnostico", d),
                                         ("otra_generacion", {"categoria": o["categoria"],
                                                              "contenido_presente_bajo_el_subarbol": any(n["estado_cita"] == "presente" for n in o["nodos_con_cita"])})]))
            f["criterios"] = crit
            f["presencia_ancla"] = {"esta_generacion": gens[gen_k].presente_ancla(f["ancla"]),
                                    "otra_generacion": gens[OTRA[gen_k]].presente_ancla(f["ancla"])}
            if f["presencia_ancla"]["esta_generacion"]["exacta_A0_2"] != 0:
                raise SystemExit(f"FRENO: el ancla de {f['celda']} {f['id_pregunta']} resuelve en su grafo (no es ausencia_kg)")
            cats = [c["categoria"] for c in crit]
            resueltas = [c for c in cats if c != "requiere_lectura"]
            if resueltas:
                prim = min(resueltas, key=lambda c: ORDEN.index(base_cat(c)))
            else:
                prim = "requiere_lectura"
            sec = sorted(({c for c in resueltas if c != prim} | {s for c in crit for s in c["secundarias"]}) - {prim})
            f["categoria_primaria"] = prim
            f["categorias_secundarias"] = sec
            f["candidato"] = candidato(prim)
            f["requiere_lectura"] = [c["indice"] for c in crit if c["categoria"] == "requiere_lectura"]
            f["otra_generacion"] = OrderedDict([
                ("generacion", OTRA[gen_k]),
                ("ancla_exacta_A0_2", f["presencia_ancla"]["otra_generacion"]["exacta_A0_2"] > 0),
                ("criterios_con_contenido_presente", sum(1 for c in crit if c["otra_generacion"]["contenido_presente_bajo_el_subarbol"])),
                ("criterios_no_cubiertos", len(crit))])
            f["evidencia"] = (f"{CMD} → d2_ausencias.json filas[celda={f['celda']}, id_pregunta={f['id_pregunta']}]; "
                              f"clase: {f['fuente_clase']}; marcas: {f['fuente_marcas']}")
            del f["marcas"]
        consultas_db = {k: dict(sorted(g.consultas_reintento.items())) for k, g in gens.items()}
    finally:
        db.close()

    filas.sort(key=lambda f: (f["celda"], f["id_pregunta"]))
    # --- prioridad
    def tabla(clave):
        t = defaultdict(lambda: {"primaria": 0, "primaria_o_secundaria": 0, "celdas_primaria": set(), "celdas": set()})
        for f in filas:
            prim = clave(f["categoria_primaria"])
            t[prim]["primaria"] += 1
            t[prim]["celdas_primaria"].add(f["celda"])
            for c in {prim} | {clave(s) for s in f["categorias_secundarias"]}:
                t[c]["primaria_o_secundaria"] += 1
                t[c]["celdas"].add(f["celda"])
        return OrderedDict((k, {"ausencias_como_primaria": v["primaria"], "celdas_como_primaria": sorted(v["celdas_primaria"]),
                                "ausencias_como_primaria_o_secundaria": v["primaria_o_secundaria"], "celdas": sorted(v["celdas"])})
                           for k, v in sorted(t.items()))
    por_categoria = tabla(lambda c: c)
    por_candidato = tabla(candidato)
    suma = sum(v["ausencias_como_primaria"] for v in por_categoria.values())
    requiere = [OrderedDict([("celda", f["celda"]), ("id_pregunta", f["id_pregunta"]), ("ancla", f["ancla"]),
                             ("criterios", [OrderedDict([("indice", c["indice"]), ("motivo", c["motivo"])]) for c in f["criterios"] if c["categoria"] == "requiere_lectura"])])
                for f in filas if f["requiere_lectura"]]
    no_dec = [OrderedDict([("celda", f["celda"]), ("id_pregunta", f["id_pregunta"]), ("ancla", f["ancla"]),
                           ("criterios", [OrderedDict([("indice", c["indice"]), ("motivo", c["motivo"])]) for c in f["criterios"] if base_cat(c["categoria"]) == "H"])])
              for f in filas if any(base_cat(c["categoria"]) == "H" for c in f["criterios"])]

    salida = OrderedDict()
    salida["unidad"] = "U-PRE-R2-DIAG"
    salida["etapa"] = "D2"
    salida["mandato"] = "docs/mandatos/UPRE_R2_diagnostico.md"
    salida["comando"] = CMD
    salida["decisiones_de_la_autora_D1"] = [
        "Regla de presencia del ancla: la de regla_atribucion.md tal como está sellada (:83, coincidencia exacta, sin descendientes). "
        "La frase «y sus descendientes» de la decisión 8 del mandato fue un error del mandato.",
        "C1: pares y clase A0.2 desde data/experiment/ev2_r1/cierre/cierre_r1.json (774acac), la misma fuente que usó E6 para "
        "c1.lectura_plan_punto_3; la clase por par está en el archivo (atribucion.pares_definitivos.por_par): no se recomputó.",
        "Nota aparte sobre T2 (fusión de ext::7.5.3 y ext::7.8.5.1), clasificación asistida con el texto de E0 como evidencia.",
    ]
    salida["reglas_declaradas"] = OrderedDict([
        ("R-CITA", "números (porcentajes, fechas, plazos), siglas y palabras de 5 letras o más fuera de palabras vacías, normalizados; "
                   "contiene si están todos los números y siglas y al menos 80 % de las palabras; parcial si al menos 50 % sin lo anterior; "
                   "lo parcial es «requiere lectura»"),
        ("R-UBIC", "unidades de E0 del subárbol del ancla con la cita en el texto propio; si ninguna, en el texto heredado desde el "
                   "subárbol; si ninguna, fuera del subárbol (candidato D, requiere lectura)"),
        ("R-PRES", "nodo que contiene la cita y ancla en el subárbol del ancla; contenedor = más de 10 anclas distintas"),
        ("R-CAT", "P si está en un nodo no contenedor con aristas; C si solo en nodos sin aristas; F si solo en contenedores; si no está: "
                  "E (unidad con error, corte o sin salida final; o tabular sin la cita en E1), G (la salida de E1 no la tiene), F (el nodo "
                  "de su slug no la tiene), H (el nodo de su slug no está); antes de G, cita repartida entre varios nodos o entidades "
                  "de la unidad y en ninguno solo → requiere lectura; secundarias B (relación de esa entidad rechazada por "
                  "firma_invalida), E-tabla y E-tabla-no-marcada (unidad no marcada tabular por E0 con 3 o más líneas que empiezan "
                  "con un código de 6 dígitos o más); fila = primera en el orden E, G, B, F, C, D, H, P"),
        ("desvio_declarado", "la regla de contenido repartido y la secundaria E-tabla-no-marcada se agregaron después de una corrida "
                             "de prueba en el scratchpad, que había marcado G en EV2F-025 criterio 4 de r1 (contenido emitido en dos "
                             "entidades) y en EV2F-032 criterio 5 (cuadro de códigos que E0 no marca como tabular); R-CITA y sus umbrales "
                             "no cambiaron"),
    ])
    salida["categorias"] = CATEGORIAS
    salida["registros_de_rechazo"] = OrderedDict([
        ("desarrollo", "validacion.rechazos en corpus_tanda0/salida_dirigida/<to>/extracciones_e1.jsonl (la misma población que "
                       "reports/u_audit_tipos_v3/p4_filas.json, 982 filas); población final por unidad en "
                       "reports/u_estudio_matriz/uestmat_poblacion_final.json"),
        ("r1", "validacion.rechazos en corpus_v2/salida/<to>/extracciones_e1.jsonl y extracciones_finales_<to>.jsonl (existen); "
               "equivalente de p4_filas.json o de uestmat_poblacion_final.json para r1: NO ENCONTRADO"),
        ("reintentos_crudos", f"{ENTRADAS['e1_reintentos_db'][0]} abierta con file:…?immutable=1; se consulta solo para unidades "
                              "portadoras con estado_e3 aceptado_tras_reintento (namespace v3 en desarrollo; los otros en r1)"),
    ])
    salida["entradas"] = entradas
    salida["unidades_consultadas_en_e1_reintentos_db"] = consultas_db
    salida["e0_identico_tanda0_vs_enm01"] = e0_identico
    salida["poblacion"] = OrderedDict([("por_celda", dict(sorted(conteo.items()))), ("total", len(filas)),
                                       ("anclas_distintas", sorted({f["ancla"] for f in filas})),
                                       ("preguntas_distintas", sorted({f["id_pregunta"] for f in filas}))])
    salida["filas"] = filas
    salida["prioridad"] = OrderedDict([("por_categoria", por_categoria), ("por_candidato", por_candidato),
                                       ("suma_primarias", suma), ("suma_cierra_31", suma == 31)])
    salida["requiere_lectura"] = requiere
    salida["no_decidibles"] = no_dec
    salida["nota_T2"] = nota_t2(chunks)
    return salida


# --------------------------------------------------------------------------- #
# Nota T2 (decisión 3 de la autora al cierre de D1)                            #
# --------------------------------------------------------------------------- #
def nota_t2(chunks: dict) -> OrderedDict:
    oracion = "Esta opción estará disponible hasta alcanzar el 125% (ciento veinticinco por ciento) de los servicios por capital e intereses"
    filas = []
    for cid in ("ext::7.5.3", "ext::7.8.5.1"):
        c = chunks[cid]
        t = re.sub(r"\s+", " ", c["texto"]).strip()
        i = t.find("Esta opción")
        filas.append(OrderedDict([
            ("chunk_id", cid), ("titulo_E0", c["titulo"]), ("sha256_completo_E0", c["sha256_completo"]),
            ("contiene_la_oracion_espacios_normalizados", oracion in t),
            ("texto_propio_E0_espacios_normalizados", t),
            ("herencia_E0", [str(h["unidad_origen"]) + ": " + re.sub(r"\s+", " ", h["texto"]).strip() for h in c.get("herencia") or []]),
            ("texto_previo_a_esta_opcion", t[:i].strip() if i >= 0 else None),
        ]))
    return OrderedDict([
        ("pregunta", "¿las dos restricciones fundidas en KG-Tanda0-Desarrollo-r1 son la misma regla repetida en dos puntos o reglas "
                     "distintas con la misma redacción?"),
        ("evidencia_E0", filas),
        ("clasificacion_asistida", "reglas distintas con la misma redacción"),
        ("fundamento_asistido", (
            "Lectura de esta instancia, para revisión de la autora. La oración del 125 % es idéntica en los dos puntos, pero "
            "«Esta opción» remite a opciones distintas. En ext::7.5.3 la opción es la ampliación del plazo de liquidación de "
            "divisas del permiso hasta el quinto día hábil posterior a la fecha en que los cobros deben permanecer depositados; "
            "el tope del 125 % limita esa ampliación. En ext::7.8.5.1 la opción es acumular los fondos del cobro de exportaciones "
            "en cuentas en moneda extranjera en garantía de la prefinanciación; el tope limita esa acumulación, y el punto agrega "
            "que los fondos excedentes se liquidan en los plazos generales. Los dos puntos están relacionados (7.5.3 menciona las "
            "prefinanciaciones del 7.8.5), pero el objeto del tope es distinto: el nodo fundido pierde de qué opción se trata.")),
    ])


# --------------------------------------------------------------------------- #
# Render .md                                                                   #
# --------------------------------------------------------------------------- #
def _c(v) -> str:
    if v is None:
        return "—"
    if isinstance(v, bool):
        return "sí" if v else "no"
    if isinstance(v, (list, tuple)):
        return ", ".join(_c(x) for x in v) if v else "—"
    return str(v).replace("|", "/").replace("\n", " ")


def render_md(s: dict) -> str:
    L = ["# U-PRE-R2-DIAG — D2: cruce de las ausencias con los candidatos del laudo", ""]
    L.append(f"Mandato `{s['mandato']}`. Solo lectura, USD 0, sin API ni Neo4j. Comando: `{s['comando']}`. Todo número de este "
             "archivo sale de `d2_ausencias.json` (misma corrida). EV2 y sus trazas se usan como material de desarrollo para "
             "diagnosticar y priorizar; nada de esto es un resultado de r2 sobre EV2.")
    L.append("")
    L.append("## 1. Decisiones de la autora al cierre de D1 y declaración")
    L.append("")
    for x in s["decisiones_de_la_autora_D1"]:
        L.append(f"- {x}")
    L.append("")
    L.append("## 2. Reglas declaradas antes de aplicarse")
    L.append("")
    for k, v in s["reglas_declaradas"].items():
        L.append(f"- **{k}**: {v}")
    L.append("")
    L.append("Categorías: " + "; ".join(f"**{k}** {v}" for k, v in s["categorias"].items()) + ".")
    L.append("")
    L.append("Registros de rechazo:")
    for k, v in s["registros_de_rechazo"].items():
        L.append(f"- {k}: {v}")
    L.append("")
    L.append("## 3. Entradas y población")
    L.append("")
    L.append("| clave | ruta | sha256 |")
    L.append("|---|---|---|")
    for k, v in s["entradas"].items():
        L.append(f"| {k} | `{v['ruta']}` | `{v['sha256'][:16]}…` |")
    L.append("")
    p = s["poblacion"]
    L.append(f"- Población recomputada por par: {p['por_celda']} = {p['total']}; {len(p['anclas_distintas'])} anclas distintas "
             f"({', '.join(p['anclas_distintas'])}).")
    L.append(f"- E0 de los cinco TOs idéntico entre `salida_tanda0` y `salida_enm01`: {dict(s['e0_identico_tanda0_vs_enm01'])}.")
    L.append(f"- Unidades consultadas en `e1_reintentos.db` (reintentos encontrados): {dict(s['unidades_consultadas_en_e1_reintentos_db'])}.")
    L.append("")
    L.append("## 4. Tabla de prioridad")
    L.append("")
    pr = s["prioridad"]
    L.append("Por categoría (una fila por ausencia; primaria y primaria o secundaria):")
    L.append("")
    L.append("| categoría | ausencias como primaria | celdas | ausencias como primaria o secundaria | celdas |")
    L.append("|---|---|---|---|---|")
    for k, v in pr["por_categoria"].items():
        L.append(f"| {k} | {v['ausencias_como_primaria']} | {_c(v['celdas_como_primaria'])} | {v['ausencias_como_primaria_o_secundaria']} | {_c(v['celdas'])} |")
    L.append("")
    L.append(f"Suma de primarias: {pr['suma_primarias']} (cierra en 31: {_c(pr['suma_cierra_31'])}).")
    L.append("")
    L.append("Por candidato del laudo:")
    L.append("")
    L.append("| candidato | ausencias como primaria | celdas | ausencias como primaria o secundaria | celdas |")
    L.append("|---|---|---|---|---|")
    for k, v in pr["por_candidato"].items():
        L.append(f"| {k} | {v['ausencias_como_primaria']} | {_c(v['celdas_como_primaria'])} | {v['ausencias_como_primaria_o_secundaria']} | {_c(v['celdas'])} |")
    L.append("")
    L.append("## 5. Una fila por ausencia")
    L.append("")
    L.append("| celda | pregunta | ancla | definitivo | criterios no cubiertos | primaria | secundarias | candidato | ancla (descendientes) | ancla en la otra generación | contenido en la otra generación | requiere lectura |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for f in s["filas"]:
        og = f["otra_generacion"]
        pa = f["presencia_ancla"]["esta_generacion"]
        L.append(f"| {f['celda']} | {f['id_pregunta']} | {f['ancla']} | {f['definitivo']} | {_c(f['criterios_no_cubiertos'])} | "
                 f"{f['categoria_primaria']} | {_c(f['categorias_secundarias'])} | {_c(f['candidato'])} | "
                 f"{pa['exacta_A0_2']} ({pa['con_descendientes']}) | "
                 f"{og['generacion']}: {_c(og['ancla_exacta_A0_2'])} | {og['criterios_con_contenido_presente']}/{og['criterios_no_cubiertos']} | "
                 f"{_c(f['requiere_lectura'])} |")
    L.append("")
    L.append("Diagnóstico descriptivo del ancla (no es categoría; resolucion.AnclaIndex con y sin descendientes y contenedores): "
             + "; ".join(sorted({f"{f['ancla']} en {CELDA_GEN[f['celda']]}: {f['presencia_ancla']['esta_generacion']['diagnostico']}" for f in s["filas"]})) + ".")
    L.append("")
    L.append("Evidencia de cada fila: `d2_ausencias.json`, `filas[]` (clave `evidencia`), con el diagnóstico por criterio "
             "(`criterios[].diagnostico`: unidades de E0, nodos con la cita, estado de las unidades portadoras con archivo:línea de "
             "sus registros de E1, nodo del slug y rechazos).")
    L.append("")
    L.append("### Detalle por criterio")
    L.append("")
    L.append("| celda | pregunta | criterio | categoría | motivo | unidades E0 (propias / herencia) | nodos con la cita (grado, contenedor) |")
    L.append("|---|---|---|---|---|---|---|")
    for f in s["filas"]:
        for c in f["criterios"]:
            d = c["diagnostico"]
            nod = "; ".join(f"{n['id'][:40]}… (g{n['grado']}{', cont' if n['contenedor'] else ''}{', parcial' if n['estado_cita'] == 'parcial' else ''})" for n in d["nodos_con_cita"][:3])
            L.append(f"| {f['celda']} | {f['id_pregunta']} | {c['indice']} | {c['categoria']} | {_c(c['motivo'])} | "
                     f"{_c(d['e0']['propias'])} / {_c(d['e0']['solo_herencia'])} | {nod or '—'} |")
    L.append("")
    L.append("## 6. Requiere lectura y no decidibles")
    L.append("")
    L.append(f"Requiere lectura ({len(s['requiere_lectura'])} filas; quién lee lo decide la autora, checklist P15 y Q12):")
    for r in s["requiere_lectura"]:
        L.append(f"- {r['celda']} {r['id_pregunta']} ({r['ancla']}): " + "; ".join(f"criterio {c['indice']}: {c['motivo']}" for c in r["criterios"]))
    L.append("")
    L.append(f"No decidibles, H ({len(s['no_decidibles'])} filas):" + ("" if s["no_decidibles"] else " ninguna."))
    for r in s["no_decidibles"]:
        L.append(f"- {r['celda']} {r['id_pregunta']} ({r['ancla']}): " + "; ".join(f"criterio {c['indice']}: {c['motivo']}" for c in r["criterios"]))
    L.append("")
    L.append("## 7. Nota aparte: T2 (clasificación asistida)")
    L.append("")
    t = s["nota_T2"]
    L.append(f"Pregunta: {t['pregunta']}")
    L.append("")
    for e in t["evidencia_E0"]:
        L.append(f"- `{e['chunk_id']}` (E0, sha256 completo `{e['sha256_completo_E0'][:12]}…`), contiene la oración del 125 % "
                 f"(espacios normalizados): {_c(e['contiene_la_oracion_espacios_normalizados'])}. Texto propio previo a «Esta opción»: "
                 f"«{e['texto_previo_a_esta_opcion']}»")
    L.append("")
    L.append(f"**Clasificación asistida: {t['clasificacion_asistida']}.** {t['fundamento_asistido']}")
    L.append("")
    return "\n".join(L)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="U-PRE-R2-DIAG D2 (solo lectura)")
    ap.add_argument("--out-dir", required=True)
    a = ap.parse_args(argv)
    out = Path(a.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    s = construir()
    (out / "d2_ausencias.json").write_text(json.dumps(s, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    (out / "d2_ausencias.md").write_text(render_md(s), encoding="utf-8")
    print(f"escrito: {out / 'd2_ausencias.json'} y {out / 'd2_ausencias.md'}")
    print(f"población: {s['poblacion']['por_celda']} = {s['poblacion']['total']}")
    print(f"suma de primarias: {s['prioridad']['suma_primarias']} (cierra 31: {s['prioridad']['suma_cierra_31']})")
    for k, v in s["prioridad"]["por_categoria"].items():
        print(f"  {k}: primaria {v['ausencias_como_primaria']} {v['celdas_como_primaria']} / prim+sec {v['ausencias_como_primaria_o_secundaria']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
