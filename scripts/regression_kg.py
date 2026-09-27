#!/usr/bin/env python3
"""regression_kg.py — U-B2.1 fase 2: regression suite del grafo de conocimiento.

Convierte cada uno de los 46 ítems del inventario de la fase 1
(reports/revision_UB21_diag/inventario_B21_fase1.md, §2; partición 19
convertibles / 23 con condición / 4 no convertibles según
tabla_resumen_B21_fase1.md §1) en un test de respuesta conocida ejecutable
sobre cualquier kg.json, y produce la tabla defecto → estado por grafo con
tres estados posibles: resuelto / persiste / no_aplicable.

Decisiones vinculantes (docs/mandatos/UB21_fase2_regression_suite.md):
  1. Direccionamiento sin ids de contenido: (archivo del TO, punto ∈ conjunto
     de provenances, tipo, cadena normalizada en label o properties) o id de
     catálogo de Sujetos. Nunca provenance[0] ni id de nodo de contenido.
  2. Adaptador de provenance propio: gen 2 lee {source_doc, location}
     («Punto 1.2.» → 1.2); gen 3 lee provenances[].archivo / .punto. La
     cuarentena se normaliza a booleano en las dos generaciones (gen 2 guarda
     un booleano; r1_tests.py:68 compara con la cadena "true"). No comparte
     código con scripts/shapes_validator.py.
  3. Política de cuarentena por generación: --politica-cuarentena laudada
     espera subclase_de desde los propuestos (KG-Refinado, laudo C4);
     flaggeada espera padre_sugerido (r1, T7).
  4. Rank (RK) solo con el retriever in-memory GraphIndex de
     data/experiment/evaluacion/harness.py (importado, no copiado), cargado
     con loader.load_graph_from_path(path, adapter_key=None). Cada consulta
     declara su limite (≥ rank esperado; tope 50 del harness). La forma
     «posición en ver_vecinos» (C4 paso e) se reduce a arista presente.
  5. RT-C5-1..4, RT-C6-1..3 y RT-C7-1..3 entran solo como tests de valor.
     RT-C5-5 es no_aplicable cuando el grafo no tiene nodos con punto 7.2 de
     Clasificación (gen 3).
  6/6bis. Salida .md + .json por grafo; la regresión se computa contra la
     fixture scripts/regression_kg_esperado.json (estado medido ≠ esperado),
     nunca contra la corrida anterior. Código de salida ≠ 0 solo con
     regresión; «persiste» esperado no es fallo.
  7. Catálogo leído del artefacto (--catalogo), nunca copiado.
  8. T4 lee el esqueleto del grafo de referencia (--esqueleto-referencia)
     excluyendo las aristas con rol_fuente cuarentena_laudada.

Estados: resuelto = la comprobación del ítem se cumple sobre el grafo;
persiste = no se cumple (el defecto está presente); no_aplicable = la
precondición del ítem no se da en este grafo (objeto o capa ausente cuya
ausencia no es el defecto) o el ítem no es observable sobre un kg.json.
Nunca hay PASS vacuo: una comprobación sin objeto sobre el que aplicar es
no_aplicable, con la razón.

Interfaz:
  python3 scripts/regression_kg.py --kg RUTA --generacion {2,3} --catalogo RUTA
      --politica-cuarentena {laudada,flaggeada} [--esperado RUTA]
      [--esqueleto-referencia RUTA] [--out RUTA.md]
  Sin --out no escribe nada. Sin --esperado reporta estados y no computa
  regresión. --solo ID[,ID] (opcional, para el selftest y depuración) corre un
  subconjunto de ítems.

Intérprete: los tests de E4 y T4/T6 importan r1_e4 / e2_lib / schema
(pydantic): correr con .venv/bin/python3 y PYTHONDONTWRITEBYTECODE=1. El
módulo en sí solo importa stdlib (los imports pesados son diferidos), para
que scripts/selftest_regression_kg.py corra con cualquier python3.
"""
from __future__ import annotations

import sys

sys.dont_write_bytecode = True

import argparse
import hashlib
import json
import re
import unicodedata
from collections import Counter, OrderedDict
from pathlib import Path

# --------------------------------------------------------------------------- #
# Rutas y constantes                                                           #
# --------------------------------------------------------------------------- #
RAIZ = Path(__file__).resolve().parent.parent
CORPUS_V2 = RAIZ / "data" / "experiment" / "reextraccion_v2" / "corpus_v2"
E2_REDUCE = RAIZ / "data" / "experiment" / "reextraccion_v2" / "e2_reduce"
EVALUACION = RAIZ / "data" / "experiment" / "evaluacion"
GRAFO_V2_CODE = RAIZ / "data" / "experiment" / "grafo_v2" / "code"
MUESTRA30 = CORPUS_V2 / "salida_r1" / "referencias_muestra30_inspeccionada_A2.json"
SHA_MUESTRA30 = "4dbc2d306df867dedc4464c54b56bf6f7224ee6d820577ffe83141b6cbba8da4"
E4_PROPUESTOS_R1 = CORPUS_V2 / "salida_r1" / "e4_propuestos.json"
DEFAULT_ESQUELETO_REF = RAIZ / "data" / "experiment" / "grafo_v2" / "reensamblado_v3" / "kg.json"

ESTADOS = ("resuelto", "persiste", "no_aplicable")
LIMITE_DEFAULT = 10          # corte de los retests («en top-10»)
TOPE_HARNESS = 50            # harness.py:159
POLITICAS = ("laudada", "flaggeada")

CLA, CAP, PRO, RIC, EXT = ("TO_clasificacion", "TO_capitales", "TO_proteccion",
                           "TO_regimen_informativo", "TO_exterior")
TO_PREFIJO = {"pro": PRO, "cla": CLA, "ric": RIC, "cap": CAP, "ext": EXT}

RE_PUNTO = re.compile(r"punto\s+(\d+(?:\.\d+)*)")
RE_MONTO = re.compile(r"(?<![\d.])(5\.000|2\.500)(?![\d.])")

NOTA_SIN_APLICACION = "defecto confirmado, no corrección aplicada"

# Partición de la tabla resumen §1 (tabla_resumen_B21_fase1.md:14-16).
CONVERTIBLES = ("BKL-0017", "BKL-0006", "BKL-0023", "BKL-0004", "BKL-0003", "BKL-0005",
                "BKL-0007", "RT-C5-4", "RT-C5-5", "RT-C6-4", "RT-C7-1", "RT-C7-2",
                "RT-C7-3", "T1", "T2", "T3", "I3", "I4", "I5")
CON_CONDICION = ("BKL-0019", "BKL-0028", "BKL-0029", "RT-C5-1", "RT-C5-2", "RT-C5-3",
                 "RT-C6-1", "RT-C6-2", "RT-C6-3", "T4", "T5", "T6", "T7",
                 "E4-a1", "E4-a2", "E4-a3", "E4-a4", "E4-a5", "E4-a6", "E4-a7", "E4-a8",
                 "E4-b", "E4-c")
NO_CONVERTIBLES = ("BKL-0026", "BKL-0027", "I1", "I2")
# Dependen del retriever (tabla_resumen_B21_fase1.md:20).
RETRIEVER = ("BKL-0017", "BKL-0019", "BKL-0004", "BKL-0003", "BKL-0005",
             "RT-C5-1", "RT-C5-2", "RT-C5-3", "RT-C5-4",
             "RT-C6-1", "RT-C6-2", "RT-C6-3", "RT-C7-1", "RT-C7-2", "RT-C7-3")


# --------------------------------------------------------------------------- #
# Utilidades                                                                    #
# --------------------------------------------------------------------------- #
def sha256_path(p) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def sha256_canonico(obj) -> str:
    return hashlib.sha256(json.dumps(obj, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()


def norm(s) -> str:
    """NFD sin diacríticos, comillas tipográficas → rectas, minúsculas,
    espacios colapsados (misma normalización que las sondas del re-diagnóstico,
    reports/revision_UB21_diag/sonda_anclas_C1_C7_UB21.py:57-61)."""
    s = unicodedata.normalize("NFD", str(s or ""))
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.replace("\u201c", '"').replace("\u201d", '"').replace("\u2019", "'")
    return re.sub(r"\s+", " ", s.lower()).strip()


def _vals(o):
    if isinstance(o, dict):
        for v in o.values():
            yield from _vals(v)
    elif isinstance(o, list):
        for v in o:
            yield from _vals(v)
    else:
        yield str(o)


def texto(n: dict) -> str:
    """label + todos los valores de properties, normalizados (cadena
    normalizada «en label o properties», decisión 1)."""
    return norm(" | ".join([n.get("label") or ""] + list(_vals(n.get("properties") or {}))))


def prop(n: dict, k: str):
    return (n.get("properties") or {}).get(k)


# =========================================================================== #
# ADAPTADOR DE PROVENANCE (decisión 2) — módulo propio de la suite            #
# =========================================================================== #
def provenances(o: dict) -> list:
    """Conjunto completo de provenances de un nodo o arista, en las dos
    generaciones: `provenances` si existe; si no, `provenance` (dict) más
    `additional_provenance` (lista, gen 1). Nunca solo provenance[0]."""
    ps = list(o.get("provenances") or [])
    if not ps and isinstance(o.get("provenance"), dict):
        ps = [o["provenance"]]
    extra = o.get("additional_provenance")
    if isinstance(extra, list):
        ps += [p for p in extra if isinstance(p, dict)]
    return ps


def formato_provenance(p: dict) -> int:
    """3 si la provenance es gen 3 ({archivo, punto}); 2 si es gen 1/2
    ({source_doc, location}); 0 si no es reconocible."""
    if not isinstance(p, dict):
        return 0
    if "punto" in p or "archivo" in p:
        return 3
    if "source_doc" in p or "location" in p:
        return 2
    return 0


def anclas(o: dict) -> set:
    """Conjunto de (archivo, punto) sobre TODAS las provenances del objeto.
    gen 3: (archivo, punto) directos. gen 1/2: (source_doc, N.N) por cada
    «Punto N.N.» que aparezca en location."""
    out = set()
    for p in provenances(o):
        if formato_provenance(p) == 3:
            out.add((p.get("archivo") or "", str(p.get("punto") or "")))
        else:
            for pt in RE_PUNTO.findall(norm(p.get("location"))):
                out.add((p.get("source_doc") or "", pt))
    return out


def con_ancla(o: dict, archivo_pref: str, punto: str | None = None, prefijo_punto: bool = False) -> bool:
    """¿Alguna provenance del objeto ancla en (archivo que empieza por
    archivo_pref, punto)? punto None = cualquier punto de ese archivo;
    prefijo_punto = acepta también punto.x."""
    for a, p in anclas(o):
        if not a.startswith(archivo_pref):
            continue
        if punto is None or p == punto or (prefijo_punto and p.startswith(punto + ".")):
            return True
    return False


def cuarentena_bool(v) -> bool:
    """Normaliza `properties.cuarentena`: booleano (gen 2) o cadena "true"
    (gen 3) → booleano. Cualquier otro valor → False."""
    if isinstance(v, bool):
        return v
    if isinstance(v, str):
        return v.strip().lower() == "true"
    return False


def es_propuesto(n: dict) -> bool:
    return n.get("type") == "Sujeto" and prop(n, "nivel") == "propuesto"


def detectar_generacion(kg: dict) -> int:
    """Generación por el formato de la primera provenance reconocible
    (informativo: --generacion es lo declarado y se coteja contra esto)."""
    for n in kg.get("nodes", []):
        for p in provenances(n):
            f = formato_provenance(p)
            if f:
                return f
    return 0


# =========================================================================== #
# Grafo, catálogo y direccionamiento                                          #
# =========================================================================== #
class Grafo:
    def __init__(self, kg: dict, ruta: str = "", sha256: str = ""):
        self.kg = kg
        self.ruta = ruta
        self.sha256 = sha256
        self.N = kg["nodes"]
        self.E = kg["edges"]
        self.by_id = {n["id"]: n for n in self.N}
        self.out_e: dict = {}
        self.in_e: dict = {}
        for e in self.E:
            self.out_e.setdefault(e["source"], []).append(e)
            self.in_e.setdefault(e["target"], []).append(e)
        self.generacion_detectada = detectar_generacion(kg)

    @classmethod
    def desde_ruta(cls, ruta) -> "Grafo":
        ruta = Path(ruta)
        return cls(json.loads(ruta.read_text(encoding="utf-8")), str(ruta), sha256_path(ruta))

    def tipo(self, nid: str):
        n = self.by_id.get(nid)
        return n.get("type") if n else None

    def salientes(self, nid: str) -> list:
        return self.out_e.get(nid, [])

    def entrantes(self, nid: str) -> list:
        return self.in_e.get(nid, [])

    def buscar(self, tipo=None, archivo=None, punto=None, contiene=(), no_contiene=(), prefijo_punto=False) -> list:
        """Direccionamiento (decisión 1): (archivo del TO, punto ∈ conjunto de
        provenances, tipo, cadenas normalizadas contenidas / no contenidas)."""
        out = []
        for n in self.N:
            if tipo and n.get("type") != tipo:
                continue
            if archivo and not con_ancla(n, archivo, punto, prefijo_punto):
                continue
            t = texto(n)
            if any(norm(c) not in t for c in contiene):
                continue
            if any(norm(c) in t for c in no_contiene):
                continue
            out.append(n)
        return out

    def arista(self, src: str, relation: str, tgt: str | None = None, tgt_type: str | None = None) -> bool:
        """Forma F4: arista presente src --relation--> (tgt | cualquier nodo de tipo tgt_type)."""
        for e in self.salientes(src):
            if e.get("relation") != relation:
                continue
            if tgt is not None and e.get("target") != tgt:
                continue
            if tgt_type is not None and self.tipo(e.get("target")) != tgt_type:
                continue
            return True
        return False

    def sujeto_por_label(self, label: str):
        k = norm(label)
        for n in self.N:
            if n.get("type") == "Sujeto" and norm(n.get("label")) == k:
                return n
        return None


class Catalogo:
    """Catálogo de Sujetos leído del artefacto (decisión 7)."""

    def __init__(self, data: dict, ruta: str = "", sha256: str = ""):
        self.data = data
        self.ruta = ruta
        self.sha256 = sha256
        self.version = str(data.get("version", ""))
        self.clases = OrderedDict((e["id"], e) for e in data.get("clases", []))
        self.roles = OrderedDict((r["id"], r) for r in data.get("roles", []))
        self.ids = frozenset(list(self.clases) + list(self.roles))
        if len(self.ids) != len(self.clases) + len(self.roles):
            raise RuntimeError(f"catálogo con ids duplicados: {ruta}")

    @classmethod
    def desde_ruta(cls, ruta) -> "Catalogo":
        ruta = Path(ruta)
        return cls(json.loads(ruta.read_text(encoding="utf-8")), str(ruta), sha256_path(ruta))

    def miembros(self, rol_id: str) -> list:
        r = self.roles.get(rol_id)
        return list((r or {}).get("miembros") or [])


def rank_de(idx, consulta: str, ids_obj, limite: int):
    """Forma F5: menor posición (1-based) de cualquier id objetivo en
    buscar_nodos(consulta, limite) del retriever in-memory; None si no entra
    en la ventana pedida. `idx` expone buscar_nodos(consulta, limite) →
    {"resultados": [{"id": ...}, ...]} (harness.GraphIndex)."""
    limite = max(1, min(int(limite), TOPE_HARNESS))
    res = idx.buscar_nodos(consulta, limite)["resultados"]
    for k, r in enumerate(res, 1):
        if r["id"] in ids_obj:
            return k
    return None


def evaluar_consultas(idx, consultas: list) -> list:
    """consultas: [(consulta, {objetivo: {"ids": set, "esperado": int|None,
    "limite": int, "cuenta": bool}}, fuente)]. Devuelve una fila por consulta
    con rank medido, en_ventana (rank ≤ limite declarado) y coincide_sellado
    (rank == esperado; esperado None = fuera del top-10 sellado)."""
    filas = []
    for consulta, objetivos, fuente in consultas:
        lim_q = max([o["limite"] for o in objetivos.values()] + [LIMITE_DEFAULT])
        fila = {"consulta": consulta, "limite_pedido": lim_q, "fuente": fuente, "objetivos": []}
        for nombre, o in objetivos.items():
            ids = set(o["ids"])
            rank = rank_de(idx, consulta, ids, lim_q) if ids else None
            esperado = o["esperado"]
            en_ventana = rank is not None and rank <= o["limite"]
            if esperado is None:
                coincide = rank is None or rank > LIMITE_DEFAULT
            else:
                coincide = rank == esperado
            fila["objetivos"].append({
                "objetivo": nombre, "objetivo_presente": bool(ids), "n_ids": len(ids),
                "rank": rank, "rank_esperado_sellado": esperado, "limite": o["limite"],
                "en_ventana": en_ventana, "coincide_sellado": coincide, "cuenta_para_estado": o["cuenta"],
            })
        filas.append(fila)
    return filas


def alcanzabilidad_ok(filas: list) -> tuple:
    """(todos en ventana, n_fallan, n_cuentan) sobre los objetivos que cuentan
    para el estado y tienen rank sellado numérico."""
    cuentan = [o for f in filas for o in f["objetivos"] if o["cuenta_para_estado"] and o["rank_esperado_sellado"] is not None]
    fallan = [o for o in cuentan if not o["en_ventana"]]
    return (not fallan, len(fallan), len(cuentan))


def _obj(ids, esperado, limite=LIMITE_DEFAULT, cuenta=True) -> dict:
    return {"ids": set(ids), "esperado": esperado, "limite": limite, "cuenta": cuenta}


# =========================================================================== #
# Contexto de una corrida (imports pesados diferidos)                          #
# =========================================================================== #
class Contexto:
    def __init__(self, grafo: Grafo, catalogo: Catalogo, generacion: int, politica: str,
                 esqueleto_ref_ruta=None, relaciones_esqueleto=None, indice=None,
                 muestra30=None, archivos_e0=None, e4=None, esqueleto_ref: Grafo | None = None):
        self.grafo = grafo
        self.cat = catalogo
        self.generacion = generacion
        self.politica = politica
        self.esqueleto_ref_ruta = esqueleto_ref_ruta
        self._esqueleto_ref = esqueleto_ref
        self._relaciones_esqueleto = relaciones_esqueleto
        self._indice = indice
        self._muestra30 = muestra30
        self._archivos_e0 = archivos_e0
        self._e4 = e4

    # --- retriever in-memory (decisión 4): importado, no copiado ---
    @property
    def indice(self):
        if self._indice is None:
            if str(EVALUACION) not in sys.path:
                sys.path.insert(0, str(EVALUACION))
            import harness   # noqa: E402  data/experiment/evaluacion/harness.py:130 (GraphIndex)
            import loader    # noqa: E402  data/experiment/evaluacion/loader.py:325 (load_graph_from_path)
            kg = loader.load_graph_from_path(self.grafo.ruta, adapter_key=None)
            self._indice = harness.GraphIndex(kg)
        return self._indice

    # --- esqueleto de referencia (decisión 8) ---
    @property
    def esqueleto_ref(self) -> Grafo:
        if self._esqueleto_ref is None:
            ruta = self.esqueleto_ref_ruta or DEFAULT_ESQUELETO_REF
            if self.grafo.ruta and Path(ruta).resolve() == Path(self.grafo.ruta).resolve():
                self._esqueleto_ref = self.grafo
            else:
                self._esqueleto_ref = Grafo.desde_ruta(ruta)
        return self._esqueleto_ref

    @property
    def relaciones_esqueleto(self) -> tuple:
        if self._relaciones_esqueleto is None:
            if str(GRAFO_V2_CODE) not in sys.path:
                sys.path.insert(0, str(GRAFO_V2_CODE))
            from schema import RELACIONES_ESQUELETO   # noqa: E402  grafo_v2/code/schema.py:76
            self._relaciones_esqueleto = tuple(RELACIONES_ESQUELETO)
        return self._relaciones_esqueleto

    # --- muestra sellada de T5 ---
    @property
    def muestra30(self) -> list:
        if self._muestra30 is None:
            sha = sha256_path(MUESTRA30)
            if sha != SHA_MUESTRA30:
                raise RuntimeError(f"muestra30 con sha distinto del sellado: {sha}")
            self._muestra30 = json.loads(MUESTRA30.read_text(encoding="utf-8"))
        return self._muestra30

    # --- E4: r1_e4 / e2_lib / r1_comun importados, no copiados (pieza c) ---
    @property
    def e4(self):
        if self._e4 is None:
            for p in (str(CORPUS_V2), str(GRAFO_V2_CODE), str(E2_REDUCE)):
                if p not in sys.path:
                    sys.path.insert(0, p)
            import r1_comun   # noqa: E402
            import r1_e4      # noqa: E402  indice_catalogo :74, resolver_label :97
            import e2_lib     # noqa: E402  slugify_full :90
            self._e4 = {"r1_e4": r1_e4, "e2_lib": e2_lib, "r1_comun": r1_comun,
                        "indice": r1_e4.indice_catalogo(self.cat.data)}
        return self._e4

    @property
    def archivos_e0(self) -> dict:
        """Archivo PDF por TO según E0 (r1_comun.archivo_de_to, única fuente)."""
        if self._archivos_e0 is None:
            rc = self.e4["r1_comun"]
            self._archivos_e0 = {to: rc.archivo_de_to(to) for to in rc.TOS_ORDEN}
        return self._archivos_e0


def res(estado: str, detalle: str, **extra) -> dict:
    assert estado in ESTADOS, estado
    out = {"estado": estado, "detalle": detalle}
    out.update(extra)
    return out


def _ids(ns, k=3):
    return [n["id"][:72] for n in ns[:k]]


# =========================================================================== #
# Objetivos compartidos (direccionados sin id)                                 #
# =========================================================================== #
C5_NODOS = [("N1", "6.5", "cada cliente, y la totalidad de sus financiaciones comprendidas"),
            ("N2", "6.5.1", "situacion normal"), ("N3", "6.5.2", "seguimiento especial"),
            ("N4", "6.5.2.1", "en observacion"), ("N5", "6.5.2.2", "en negociacion o con acuerdos de refinanciacion"),
            ("N6", "6.5.2.3", "tratamiento especial"), ("N7", "6.5.3", "con problemas"),
            ("N8", "6.5.4", "alto riesgo de insolvencia"), ("N9", "6.5.5", "irrecuperable")]

# C4: (id de cuarentena registrado en C4_retest_2026-08-02.md:35-42, label de
# cuarentena.json, padre laudado). El sujeto se localiza por label
# normalizado (los ids Sujeto_propuesto_* derivan del label; no son de
# catálogo) o por ese id de cuarentena; nunca por id de contenido.
C4_OCHO = [("Sujeto_propuesto_inversor", "Inversor", "Sujeto_contraparte"),
           ("Sujeto_propuesto_entidades_financieras_del_grupo_1", "Entidades financieras del grupo 1", "Sujeto_entidad_financiera"),
           ("Sujeto_propuesto_beneficiarios_de_radpip_y_o_radpign", "Beneficiarios de RADPIP y/o RADPIGN", "Sujeto_contraparte"),
           ("Sujeto_propuesto_entidades_del_grupo_a", "Entidades del Grupo A", "Sujeto_entidad_financiera"),
           ("Sujeto_propuesto_entidades_financieras_del_grupo_2", "Entidades financieras del grupo 2", "Sujeto_entidad_financiera"),
           ("Sujeto_propuesto_inversores_y_tenedores_de_titulizacion", "Inversores y tenedores de titulización", "Sujeto_contraparte"),
           ("Sujeto_propuesto_originante_fiduciario", "Originante/fiduciario", "Sujeto_fiduciario_de_fideicomiso_financiero"),
           ("Sujeto_propuesto_personas_juridicas_beneficiarias_del_regimen_de_economia_del_conocimiento",
            "Personas jurídicas beneficiarias del régimen de economía del conocimiento", "Sujeto_beneficiario_economia_conocimiento")]
C4_EXCLUIDA = ("Sujeto_propuesto_originante_acreedor_inicial", "Originante/acreedor inicial")

ROL_PROTECCION = "Sujeto_rol_sujeto_obligado_proteccion"
PNFC = "Sujeto_proveedor_no_financiero_de_credito"
EMISORAS = "Sujeto_empresa_no_financiera_emisora_de_tarjetas"
C7_FRASE = "para el calculo del importe correspondiente al mes n"
C7_RPC = "responsabilidad patrimonial computable informada en el mes n"
C7_FRANQUICIA = "franquicia informada en el mes n calculada segun datos del mes n"
C1_FRASE = "los clientes de la entidad (tanto residentes en el pais"
C3_FRASE = "companias financieras que realicen, en forma directa, operaciones de comercio exterior"


def obj_c1(G: Grafo):
    return G.buscar("Obligacion", CLA, "1.1", contiene=[C1_FRASE])


def obj_c5(G: Grafo) -> dict:
    return {k: G.buscar(None, CLA, pt, contiene=[fr]) for k, pt, fr in C5_NODOS}


def obj_c6(G: Grafo):
    return G.buscar("Excepcion", PRO, "1.1.2.5", contiene=["mutuales o cooperativas"])


def obj_c7(G: Grafo):
    return G.buscar("Obligacion", RIC, "7.1", contiene=[C7_FRASE])


def localizar_c4(G: Grafo, id_cuarentena: str, label: str):
    n = G.sujeto_por_label(label)
    if n is None and id_cuarentena in G.by_id and G.by_id[id_cuarentena].get("type") == "Sujeto":
        n = G.by_id[id_cuarentena]
    return n


# =========================================================================== #
# Tests — grupo (i): BKL cerrados                                              #
# =========================================================================== #
def t_bkl_0017(ctx: Contexto) -> dict:
    """C1: criterio general 1.1 de Clasificación (F1 + F4 + F5)."""
    G = ctx.grafo
    c1 = obj_c1(G)
    sub = OrderedDict()
    sub["nodo_1_1"] = bool(c1)
    if not c1:
        return res("persiste", "sin Obligacion anclada en cla 1.1 con la frase del criterio general", subchecks=sub)
    n = c1[0]
    sub["arista_establecida_en_TextoOrdenado"] = G.arista(n["id"], "establecida_en", tgt_type="TextoOrdenado")
    sub["arista_aplica_a_Sujeto"] = G.arista(n["id"], "aplica_a", tgt_type="Sujeto") or G.arista(n["id"], "aplica_a", tgt_type="EntidadFinanciera")
    ids = {x["id"] for x in c1}
    f = "data/backlog/retests/C1_retest_2026-07-31.md:42-44"
    consultas = [("criterio general clasificación deudores", {"C1": _obj(ids, 1)}, f),
                 ("qué clientes deben ser clasificados", {"C1": _obj(ids, 1)}, f),
                 ("clasificación residentes en el exterior", {"C1": _obj(ids, 3)}, f)]
    filas = evaluar_consultas(ctx.indice, consultas)
    ok_rk, n_fallan, n_cuentan = alcanzabilidad_ok(filas)
    sub["alcanzable_en_ventana"] = ok_rk
    estado = "resuelto" if all(sub.values()) else "persiste"
    det = (f"nodo={len(c1)} {_ids(c1, 1)}; establecida_en={sub['arista_establecida_en_TextoOrdenado']}; "
           f"aplica_a={sub['arista_aplica_a_Sujeto']}; consultas en ventana={n_cuentan - n_fallan}/{n_cuentan}"
           + ("" if ok_rk else " (persiste solo por alcanzabilidad si lo demás cumple)"))
    return res(estado, det, subchecks=sub, ranks=filas)


def t_bkl_0006(ctx: Contexto) -> dict:
    """C2: montos del 1.2 de CapMin (F3 + F4; F5 informativo sin criterio)."""
    G = ctx.grafo
    tabla = G.buscar(None, CAP, "1.2", contiene=["exigencia basica"])
    filas, bancos_ok, restantes_ok, invertido = [], False, False, False
    for n in tabla:
        t = texto(n)
        clase = "restantes" if "restantes entidades" in t else ("bancos" if "bancos" in t else "otro")
        montos = sorted(set(RE_MONTO.findall(t)))
        umbral = prop(n, "umbral") or prop(n, "monto")
        filas.append(f"{n['type']}:{n['id'][:50]} clase={clase} montos={montos} umbral={umbral!r}")
        if n["type"] != "Excepcion":
            if clase == "bancos":
                bancos_ok |= ("5.000" in montos and "2.500" not in montos)
                invertido |= ("2.500" in montos)
            if clase == "restantes":
                restantes_ok |= ("2.500" in montos and "5.000" not in montos)
                invertido |= ("5.000" in montos)
    sub = OrderedDict()
    if not tabla:
        return res("no_aplicable", "sin nodos anclados en cap 1.2 con «exigencia básica»: tabla del 1.2 no extraída", subchecks=sub)
    sub["tabla_bancos_5000_restantes_2500"] = bancos_ok and restantes_ok and not invertido
    exc = G.buscar("Excepcion", CAP, "1.2", contiene=["cajas de credito cooperativas"])
    if exc:
        tg = [(e["relation"], texto(G.by_id[e["target"]])[:40]) for e in G.salientes(exc[0]["id"])
              if e["relation"].startswith("exceptua") and e["target"] in G.by_id]
        sub["excepcion_cajas_apunta_a_restantes"] = any("restantes" in t for _, t in tg)
    else:
        tg = None
    # F5 informativo (C2_retest:59: «informativo, sin criterio de corte»); el
    # «bancos 13» exige limite 13 (decisión 4, inventario §5.6).
    bancos = {n["id"] for n in G.buscar("Restriccion", CAP, "1.2", contiene=["bancos", "exigencia basica"], no_contiene=["restantes entidades"])}
    restantes = {n["id"] for n in G.buscar("Restriccion", CAP, "1.2", contiene=["restantes entidades", "exigencia basica"])}
    excep = {n["id"] for n in exc}
    f = "data/backlog/retests/C2_retest_2026-07-31.md:61-63"
    consultas = [("exigencia básica bancos", {"C2.bancos": _obj(bancos, 1, cuenta=False), "C2.excepcion": _obj(excep, 3, cuenta=False), "C2.restantes": _obj(restantes, 4, cuenta=False)}, f),
                 ("exigencia básica restantes entidades", {"C2.excepcion": _obj(excep, 1, cuenta=False), "C2.restantes": _obj(restantes, 2, cuenta=False), "C2.bancos": _obj(bancos, 13, limite=13, cuenta=False)}, f)]
    rk = evaluar_consultas(ctx.indice, consultas)
    estado = "resuelto" if all(sub.values()) else "persiste"
    det = (("invertido: " if invertido else "") + f"tabla={sub['tabla_bancos_5000_restantes_2500']}; "
           + (f"excepcion→restantes={sub['excepcion_cajas_apunta_a_restantes']} targets={tg}" if exc else "sin Excepcion de cajas en cap 1.2 (sub-check no aplicable)")
           + "; " + " || ".join(filas))
    return res(estado, det, subchecks=sub, ranks=rk)


def t_bkl_0023(ctx: Contexto) -> dict:
    """C3: umbral de compañías financieras con comercio exterior (F3). Sin
    nodo o sin umbral → no_aplicable (pieza e: nunca PASS vacuo)."""
    G = ctx.grafo
    c3 = G.buscar("Restriccion", CAP, "1.2", contiene=[C3_FRASE])
    if not c3:
        return res("no_aplicable", "ninguna Restriccion anclada en cap 1.2 con la oración de compañías financieras")
    u = [prop(n, "umbral") for n in c3]
    if all(x is None for x in u):
        return res("no_aplicable", f"nodo presente ({_ids(c3, 1)}) sin properties.umbral: no hay valor que comprobar", valores={"umbral": u})
    ok = any(norm(x) == "5.000 millones de pesos" for x in u if x)
    return res("resuelto" if ok else "persiste", f"n={len(c3)} umbral={u}", valores={"umbral": u})


def t_bkl_0019(ctx: Contexto) -> dict:
    """C4: jerarquía de los 8 sujetos de cuarentena, según política (F4 ×8 +
    F4 ausente para la excluida; la posición en ver_vecinos se reduce a
    arista presente, decisión 4)."""
    G = ctx.grafo
    rel = "subclase_de" if ctx.politica == "laudada" else "padre_sugerido"
    filas, presentes, con_arista = [], 0, 0
    for idc, lab, padre in C4_OCHO:
        n = localizar_c4(G, idc, lab)
        if n is None:
            filas.append(f"{lab[:30]}: src ausente")
            continue
        presentes += 1
        ok = G.arista(n["id"], rel, tgt=padre)
        con_arista += ok
        filas.append(f"{lab[:30]}: {rel}→{padre[7:]}={'si' if ok else 'NO'} tgt_presente={padre in G.by_id}")
    sub = OrderedDict()
    if presentes == 0:
        return res("no_aplicable", "ninguno de los 8 sujetos propuestos está en el grafo (por label ni por id de cuarentena)", valores={"presentes": 0})
    sub[f"{rel}_en_todos_los_presentes"] = con_arista == presentes
    if ctx.politica == "laudada":
        ex = localizar_c4(G, *C4_EXCLUIDA)
        if ex is not None:
            sub["excluida_sin_subclase_de"] = not any(e["relation"] == "subclase_de" for e in G.salientes(ex["id"]))
        else:
            filas.append("excluida: ausente (sub-check no aplicable)")
    estado = "resuelto" if all(sub.values()) else "persiste"
    return res(estado, f"politica={ctx.politica}: {rel} {con_arista}/{presentes} presentes (de 8); " + " || ".join(filas),
               subchecks=sub, valores={"presentes": presentes, "con_arista": con_arista})


def _consultas_c5(hall: dict) -> list:
    ids = {k: {n["id"] for n in v} for k, v in hall.items()}
    f = "data/backlog/propuestas/E4_enumeracion_65.md:283-289 (retest C5 (c) 7/7 en top-10, C5_retest_2026-08-02.md:65)"
    q = [("niveles clasificación deudores cartera comercial", {"N1": 1, "N7": 4, "N9": 5, "N2": 6, "N3": 8}),
         ("seguimiento especial deudores", {"N1": 1, "N4": 3, "N6": 4, "N5": 5, "N3": 6}),
         ("punto 6.5 niveles clasificación", {"N1": 1, "N7": 2, "N9": 3, "N2": 4, "N8": 5, "N3": 6}),
         ("situaciones que integran el seguimiento especial", {"N3": 7}),
         ("cinco categorías cartera comercial", {"N1": 1, "N7": 7, "N9": 8, "N2": 9, "N4": 10}),
         ("en negociación o con acuerdos de refinanciación", {"N5": 1, "N3": 2}),
         ("situación normal cartera comercial", {"N2": 1, "N1": 2, "N4": 3, "N6": 4, "N5": 5})]
    out = [(c, {("C5." + k): _obj(ids[k], r) for k, r in esp.items()}, f) for c, esp in q]
    out.append(("reclasificación en tratamiento especial refinanciación", {"C5.N6": _obj(ids["N6"], 4)},
                "data/backlog/retests/C5_retest_2026-08-02.md:70-72 (proxy RT-C5-4, consulta plausible mínima)"))
    return out


def t_bkl_0004(ctx: Contexto) -> dict:
    """C5: enumeración del 6.5 (F1 ×9 + F4 8 regula + 9 establecida_en + F5)."""
    G = ctx.grafo
    hall = obj_c5(G)
    n_ok = sum(1 for k in hall if hall[k])
    sub = OrderedDict()
    sub["9_nodos_por_ancla_y_frase"] = n_ok == 9
    det = [f"nodos {n_ok}/9 -> " + " ".join(f"{k}@{pt}:{len(hall[k])}" for k, pt, _ in C5_NODOS)]
    if hall["N1"]:
        n1 = hall["N1"][0]
        hijos = {n["id"] for k in hall if k != "N1" for n in hall[k]}
        regula = sum(1 for e in G.salientes(n1["id"]) if e["relation"] == "regula" and e["target"] in hijos)
        est_en = sum(1 for k in hall if any(G.arista(n["id"], "establecida_en", tgt_type="TextoOrdenado") for n in hall[k]))
        sub["8_regula_N1_a_hijos"] = regula == 8
        sub["9_establecida_en"] = est_en == 9
        det.append(f"regula={regula}/8 establecida_en={est_en}/9")
    else:
        det.append("sin N1: aristas no evaluables")
    rk = evaluar_consultas(ctx.indice, _consultas_c5(hall))
    ok_rk, n_fallan, n_cuentan = alcanzabilidad_ok(rk)
    sub["alcanzable_en_ventana"] = ok_rk
    det.append(f"objetivos en ventana={n_cuentan - n_fallan}/{n_cuentan}")
    estado = "resuelto" if all(sub.values()) else "persiste"
    return res(estado, "; ".join(det), subchecks=sub, ranks=rk, valores={"nodos": n_ok})


def _consultas_c6(G: Grafo, n1_ids: set) -> list:
    f = "data/backlog/propuestas/E3_salvedad_mutuales.md:288-298 (columna post; — = fuera del top-10; retest C6 (c) 14/14, C6_retest_2026-08-03.md:61)"
    rol = {ROL_PROTECCION} if ROL_PROTECCION in G.by_id else set()
    pnfc = {PNFC} if PNFC in G.by_id else set()
    tabla = [("asociación mutual financiaciones proveedor no financiero crédito", 1, None, 2),
             ("sujeto obligado protección usuarios servicios financieros", 1, 5, None),
             ("proveedor no financiero crédito", None, None, 1),
             ("asociación mutual", 1, None, None),
             ("definición proveedor no financiero crédito PNFC", None, None, 1),
             ("proveedor no financiero crédito comercios empresas personas jurídicas", None, None, 1),
             ("exclusión excluido no alcanzado no incluido sujeto obligado", 4, None, None),
             ("mutuales cooperativas sujeto obligado protección usuarios", 1, 2, None),
             ("excepción asociaciones mutuales cooperativas", 1, None, None),
             ("cooperativa que otorga financiaciones protección de usuarios", 1, 5, None),
             ("asociaciones mutuales proveedores no financieros de crédito", 1, None, 2)]
    return [(q, {"C6.N1": _obj(n1_ids, a), "C6.rol": _obj(rol, b), "C6.pnfc": _obj(pnfc, c)}, f) for q, a, b, c in tabla]


def t_bkl_0003(ctx: Contexto) -> dict:
    """C6: salvedad mutuales/cooperativas del 1.1.2.5 (F1 + F4 ×2 + F4 ausente a Sujeto + F5 ×11)."""
    G = ctx.grafo
    c6 = obj_c6(G)
    sub = OrderedDict()
    sub["excepcion_1_1_2_5_mutuales"] = bool(c6)
    det = [f"Excepcion={len(c6)} {_ids(c6, 1)}"]
    if c6:
        n = c6[0]
        sub["arista_establecida_en_TextoOrdenado"] = G.arista(n["id"], "establecida_en", tgt_type="TextoOrdenado")
        sub["arista_exceptua_obligacion_Obligacion"] = G.arista(n["id"], "exceptua_obligacion", tgt_type="Obligacion")
        a_suj = sum(1 for e in G.salientes(n["id"]) + G.entrantes(n["id"])
                    if G.tipo(e["target"]) == "Sujeto" or G.tipo(e["source"]) == "Sujeto")
        sub["sin_aristas_a_Sujeto"] = a_suj == 0
        det.append(f"establecida_en={sub['arista_establecida_en_TextoOrdenado']} exceptua_obligacion={sub['arista_exceptua_obligacion_Obligacion']} aristas_con_Sujeto={a_suj}")
    rk = evaluar_consultas(ctx.indice, _consultas_c6(G, {n["id"] for n in c6}))
    ok_rk, n_fallan, n_cuentan = alcanzabilidad_ok(rk)
    sub["alcanzable_en_ventana"] = ok_rk
    det.append(f"objetivos en ventana={n_cuentan - n_fallan}/{n_cuentan}")
    estado = "resuelto" if all(sub.values()) else "persiste"
    return res(estado, "; ".join(det), subchecks=sub, ranks=rk)


def _portador_c7(G: Grafo):
    port = obj_c7(G)
    con = [n for n in port if C7_RPC in texto(n) and C7_FRANQUICIA in texto(n)]
    return port, con


def t_bkl_0005(ctx: Contexto) -> dict:
    """C7: calificadores del 7.1 de RegInf (F3 + F5 ×3)."""
    G = ctx.grafo
    port, con = _portador_c7(G)
    if not port:
        return res("no_aplicable", "sin portador: ninguna Obligacion anclada en ric 7.1 con «para el cálculo del importe correspondiente al mes n»")
    sub = OrderedDict()
    sub["descripcion_con_RPC_y_franquicia"] = bool(con)
    ids = {n["id"] for n in port}
    f = "data/backlog/retests/C7_retest_2026-08-03.md:78"
    consultas = [("esquema cálculo importe mes n disminución exigencia franquicia", {"C7": _obj(ids, 1)}, f),
                 ("responsabilidad patrimonial computable cálculo importe correspondiente al mes", {"C7": _obj(ids, 1)}, f),
                 ("franquicia importe correspondiente al mes n cálculo esquema", {"C7": _obj(ids, 1)}, f)]
    rk = evaluar_consultas(ctx.indice, consultas)
    ok_rk, n_fallan, n_cuentan = alcanzabilidad_ok(rk)
    sub["alcanzable_en_ventana"] = ok_rk
    estado = "resuelto" if all(sub.values()) else "persiste"
    return res(estado, f"portadores={len(port)} con_ambos_calificadores={len(con)} {_ids(port, 1)}; consultas en ventana={n_cuentan - n_fallan}/{n_cuentan}",
               subchecks=sub, ranks=rk)


def t_bkl_0007(ctx: Contexto) -> dict:
    """Dedupe con BKL-0017 (pieza e): mismo objeto, sin test propio; el estado
    es el de BKL-0017."""
    r = t_bkl_0017(ctx)
    return res(r["estado"], "= BKL-0017 (cerrada por referencia; " + NOTA_SIN_APLICACION + "): " + r["detalle"], subchecks=r.get("subchecks"))


def t_bkl_0026(ctx: Contexto) -> dict:
    return res("no_aplicable", "no convertible: conducta del agente (paráfrasis invertida del verbatim con ver_nodo byte-idéntico, "
               "RT-C6-1 vs RT-C6-2, 3/3 en N=3); no es observable con una comprobación determinística sobre un kg.json "
               "(inventario_B21_fase1.md:107). El nodo objetivo se testea en BKL-0003. " + NOTA_SIN_APLICACION + ".")


def t_bkl_0027(ctx: Contexto) -> dict:
    return res("no_aplicable", "no convertible: conducta del agente (pidió ver_vecinos salientes de un rol que solo tiene miembro_de "
               "entrantes, RT-C6-3); la estructura del rol se testea en RT-C6-3 (inventario_B21_fase1.md:108). " + NOTA_SIN_APLICACION + ".")


def t_bkl_0028(ctx: Contexto) -> dict:
    """Tres ids con definición doméstica y alias «del exterior» en el
    catálogo v3 (b54): remedio = ids separados. Observable solo con un
    catálogo v3 y un grafo extraído con él (perfil v3_b54)."""
    cat = ctx.cat
    tres = ("Sujeto_entidad_financiera", "Sujeto_banco", "Sujeto_entidad_cambiaria")
    con_alias_ext = [i for i in tres if i in cat.clases and any("del exterior" in norm(a) for a in (cat.clases[i].get("alias") or []))]
    ids_ext = [i for i in cat.ids if "del_exterior" in i and any(i.startswith(t) for t in tres)]
    val = {"catalogo_version": cat.version, "ids_con_alias_del_exterior": con_alias_ext, "ids_separados_del_exterior": ids_ext}
    if not cat.version.startswith("3"):
        return res("no_aplicable", f"catálogo {cat.version}: el defecto se registró sobre el catálogo v3 de b54 y su remedio exige ids "
                   "nuevos en ese catálogo y un grafo extraído con perfil v3_b54 (inventario_B21_fase1.md:109); "
                   + NOTA_SIN_APLICACION + ".", valores=val)
    presentes = [i for i in ids_ext if i in ctx.grafo.by_id]
    val["ids_separados_presentes_en_grafo"] = presentes
    ok = not con_alias_ext and bool(ids_ext) and bool(presentes)
    return res("resuelto" if ok else "persiste", f"catálogo v3: alias «del exterior» en {con_alias_ext}; ids separados {ids_ext}; "
               f"presentes en el grafo {presentes}. " + NOTA_SIN_APLICACION + ".", valores=val)


def t_bkl_0029(ctx: Contexto) -> dict:
    """Colectivo «titulares de cuenta corriente en el BCRA» sin id (rol de
    convca). no_aplicable en todo grafo que no cubra convca (pieza e)."""
    G, cat = ctx.grafo, ctx.cat
    rol = "Sujeto_rol_alcance_convca"
    cubre = any("convca" in norm(a) for n in G.N for a, _ in anclas(n)) or \
        any("convca" in norm(prop(n, "archivo")) for n in G.N if n.get("type") == "TextoOrdenado") or \
        bool(G.entrantes(rol))
    if not cubre:
        return res("no_aplicable", "el grafo no cubre convca (ninguna provenance ni TextoOrdenado de convca; el rol "
                   f"{rol} no tiene miembro_de entrantes); " + NOTA_SIN_APLICACION + ".")
    cand = [i for i, c in cat.clases.items() if "titular" in norm(c.get("label")) and "cuenta corriente" in norm(c.get("label"))]
    miembros = [e["source"] for e in G.entrantes(rol) if e["relation"] == "miembro_de"]
    residuo = ((cat.roles.get(rol) or {}).get("residuo_declarado") or {})
    ok = bool(cand) and any(c in miembros for c in cand) and not residuo.get("colectivo_operativo_sin_id", False)
    return res("resuelto" if ok else "persiste", f"ids candidatos en catálogo={cand}; miembro_de del rol={miembros}; "
               f"residuo colectivo_operativo_sin_id={residuo.get('colectivo_operativo_sin_id')}. " + NOTA_SIN_APLICACION + ".",
               valores={"candidatos": cand, "miembros": miembros})


# =========================================================================== #
# Tests — grupo (i): preguntas RT (solo valor, decisión 5)                    #
# =========================================================================== #
def _valor_en(nodos: list, frases: list, etiqueta: str, ausente: str) -> dict:
    if not nodos:
        return res("persiste", ausente)
    faltan = [f for f in frases if not any(norm(f) in texto(n) for n in nodos)]
    return res("resuelto" if not faltan else "persiste",
               f"{etiqueta} {_ids(nodos, 1)}: gold {len(frases) - len(faltan)}/{len(frases)}" + (f"; faltan {faltan}" if faltan else ""),
               valores={"faltan": faltan})


def t_rt_c5_1(ctx: Contexto) -> dict:
    n1 = obj_c5(ctx.grafo)["N1"]
    return _valor_en(n1, ["en situacion normal", "con seguimiento especial", "con problemas", "con alto riesgo de insolvencia", "irrecuperable"],
                     "N1", "sin N1 (Obligacion del 6.5 con el encabezado): el gold no está en el grafo")


def t_rt_c5_2(ctx: Contexto) -> dict:
    n3 = obj_c5(ctx.grafo)["N3"]
    return _valor_en(n3, ["en observacion", "en negociacion o con acuerdos de refinanciacion", "en tratamiento especial"],
                     "N3", "sin N3 (nodo del 6.5.2 «seguimiento especial»): el gold no está en el grafo")


def t_rt_c5_3(ctx: Contexto) -> dict:
    n5 = obj_c5(ctx.grafo)["N5"]
    return _valor_en(n5, ["antes de los 60 dias", "mora"], "N5", "sin N5 (nodo del 6.5.2.2): el gold no está en el grafo")


def t_rt_c5_4(ctx: Contexto) -> dict:
    n6 = obj_c5(ctx.grafo)["N6"]
    return _valor_en(n6, ["por primera vez dentro del ano calendario", "primera cuota", "por unica vez"],
                     "N6", "sin N6 (nodo del 6.5.2.3): el gold no está en el grafo")


def t_rt_c5_5(ctx: Contexto) -> dict:
    """F2 (nodo con «riesgo medio» anclado exactamente en cla 7.2) + F3 (N1
    sin niveles del 7.2). Sin nodos con punto 7.2 → no_aplicable por ancla."""
    G = ctx.grafo
    n72 = G.buscar(None, CLA, "7.2")
    if not n72:
        return res("no_aplicable", "sin nodos con punto exactamente 7.2 de Clasificación: el proxy falla por ancla, no por contenido "
                   "(inventario_B21_fase1.md:267, §5.7; decisión 5)", valores={"nodos_en_7_2": 0})
    rm = G.buscar(None, CLA, "7.2", contiene=["riesgo medio"])
    sub = OrderedDict([("riesgo_medio_anclado_en_7_2", bool(rm))])
    n1 = obj_c5(G)["N1"]
    if n1:
        sub["N1_sin_niveles_del_7_2"] = not any(x in texto(n1[0]) for x in ("riesgo medio", "riesgo bajo", "riesgo alto"))
    estado = "resuelto" if all(sub.values()) else "persiste"
    return res(estado, f"nodos_en_7_2={len(n72)} con_riesgo_medio={len(rm)}; N1={'presente' if n1 else 'ausente (sub-check no aplicable)'}",
               subchecks=sub, valores={"nodos_en_7_2": len(n72), "con_riesgo_medio": len(rm)})


def _valor_c6(ctx: Contexto, etiqueta: str) -> dict:
    """Gold de RT-C6-1/2 en N1 de C6. Criterio de estado = el de la sonda de
    anclas (Excepcion anclada en pro 1.1.2.5 con «mutuales o cooperativas»,
    sonda_anclas_C1_C7_UB21.py:262); la cláusula de operaciones del gold
    («por las financiaciones que otorguen») se reporta como informativa."""
    c6 = obj_c6(ctx.grafo)
    if not c6:
        return res("persiste", f"{etiqueta}: sin Excepcion anclada en pro 1.1.2.5 con «mutuales o cooperativas»")
    clausula = any("por las financiaciones que otorguen" in texto(n) for n in c6)
    return res("resuelto", f"{etiqueta}: gold «mutuales o cooperativas» presente en {_ids(c6, 1)}; "
               f"cláusula «por las financiaciones que otorguen» (informativa)={'presente' if clausula else 'AUSENTE'}",
               valores={"clausula_financiaciones": clausula})


def t_rt_c6_1(ctx: Contexto) -> dict:
    return _valor_c6(ctx, "RT-C6-1")


def t_rt_c6_2(ctx: Contexto) -> dict:
    return _valor_c6(ctx, "RT-C6-2 (= RT-C6-1 en la parte de valor)")


def t_rt_c6_3(ctx: Contexto) -> dict:
    """Rol de sujetos obligados de Protección con sus miembro_de entrantes
    = miembros del rol en el catálogo parametrizado (F4 ×n, ids de catálogo)."""
    G, cat = ctx.grafo, ctx.cat
    if ROL_PROTECCION not in G.by_id:
        return res("no_aplicable", f"rol {ROL_PROTECCION} ausente: grafo sin esqueleto de roles")
    esperados = set(cat.miembros(ROL_PROTECCION))
    mde = {e["source"] for e in G.entrantes(ROL_PROTECCION) if e["relation"] == "miembro_de"}
    ok = bool(esperados) and mde == esperados
    return res("resuelto" if ok else "persiste",
               f"miembro_de entrantes={len(mde)} esperados(catálogo)={len(esperados)}; faltan={sorted(esperados - mde)} sobran={sorted(mde - esperados)}",
               valores={"n_miembro_de": len(mde), "n_esperados": len(esperados)})


def t_rt_c6_4(ctx: Contexto) -> dict:
    G = ctx.grafo
    if ROL_PROTECCION not in G.by_id:
        return res("no_aplicable", f"rol {ROL_PROTECCION} ausente: grafo sin esqueleto de roles")
    sub = OrderedDict()
    sub["emisoras_miembro_de_rol"] = G.arista(EMISORAS, "miembro_de", tgt=ROL_PROTECCION)
    c6 = obj_c6(G)
    if c6:
        n = c6[0]
        a_suj = sum(1 for e in G.salientes(n["id"]) + G.entrantes(n["id"]) if G.tipo(e["target"]) == "Sujeto" or G.tipo(e["source"]) == "Sujeto")
        sub["N1_sin_aristas_a_Sujeto"] = a_suj == 0
    estado = "resuelto" if all(sub.values()) else "persiste"
    return res(estado, f"emisoras→rol={sub['emisoras_miembro_de_rol']}; N1={'presente, aristas con Sujeto=' + str(not sub['N1_sin_aristas_a_Sujeto']) if c6 else 'ausente (sub-check no aplicable)'}",
               subchecks=sub)


def _valor_c7(ctx: Contexto, frases: list, etiqueta: str) -> dict:
    port, _ = _portador_c7(ctx.grafo)
    if not port:
        return res("no_aplicable", f"{etiqueta}: sin portador del 7.1 (Obligacion con «para el cálculo del importe correspondiente al mes n»)")
    return _valor_en(port, frases, etiqueta + " portador", "")


def t_rt_c7_1(ctx: Contexto) -> dict:
    return _valor_c7(ctx, [C7_RPC, C7_FRANQUICIA], "RT-C7-1")


def t_rt_c7_2(ctx: Contexto) -> dict:
    return _valor_c7(ctx, [C7_RPC], "RT-C7-2")


def t_rt_c7_3(ctx: Contexto) -> dict:
    return _valor_c7(ctx, [C7_FRANQUICIA], "RT-C7-3")


# =========================================================================== #
# Tests — grupo (ii): T1–T7 sobre el adaptador (pieza d) e I1–I5             #
# =========================================================================== #
def t_t1(ctx: Contexto) -> dict:
    """ensamblar_corpus.py:237-249 sobre el adaptador: ext 3.9 (y 3.9.x) con
    nodos de contenido y alguno con «200»."""
    G = ctx.grafo
    ext39 = G.buscar(None, EXT, "3.9", prefijo_punto=True)
    con_200 = [n for n in ext39 if "200" in texto(n)]
    puntos = sorted({p for n in ext39 for a, p in anclas(n) if a.startswith(EXT) and (p == "3.9" or p.startswith("3.9."))})
    val = {"pass": bool(ext39) and bool(con_200), "nodos_anclados_3_9": len(ext39), "puntos": puntos,
           "nodos_con_usd_200": [{"id": n["id"], "label": n.get("label")} for n in con_200][:8]}
    return res("resuelto" if val["pass"] else "persiste",
               f"anclados_3_9={len(ext39)} puntos={puntos} con_usd_200={len(con_200)}", valores=val)


def t_t2(ctx: Contexto) -> dict:
    """ensamblar_corpus.py:251-265: ≥ 5 nodos separados de ext con «125 %»/«125%» y ≥ 4 puntos distintos."""
    G = ctx.grafo
    n125 = [n for n in G.buscar(None, EXT) if "125 %" in texto(n) or "125%" in texto(n)]
    puntos = sorted({p for n in n125 for a, p in anclas(n) if a.startswith(EXT)})
    val = {"pass": len(n125) >= 5 and len(puntos) >= 4, "n_nodos_separados_ext": len(n125), "puntos_distintos": puntos,
           "nodos": [{"id": n["id"], "label": n.get("label"), "puntos": sorted(p for a, p in anclas(n) if a.startswith(EXT))} for n in n125][:12]}
    return res("resuelto" if val["pass"] else "persiste", f"nodos_separados_ext={len(n125)} puntos_distintos={puntos}", valores=val)


def t_t3(ctx: Contexto) -> dict:
    """ensamblar_corpus.py:267-280: pro 1.1.2.5 con un nodo con «mutual» o «cooperativ»."""
    G = ctx.grafo
    pro = G.buscar(None, PRO, "1.1.2.5")
    con = [n for n in pro if "mutual" in texto(n) or "cooperativ" in texto(n)]
    exc = [n for n in con if n.get("type") == "Excepcion"]
    val = {"pass": bool(con), "nodos_anclados": len(pro), "nodos_con_salvedad": [{"id": n["id"], "type": n["type"], "label": n.get("label")} for n in con][:6],
           "de_los_cuales_excepcion": len(exc)}
    return res("resuelto" if val["pass"] else "persiste", f"anclados_1_1_2_5={len(pro)} con_salvedad={len(con)} de_los_cuales_excepcion={len(exc)}", valores=val)


def t4_paridad(G: Grafo, ref: Grafo, relaciones_esqueleto: tuple) -> dict:
    """Decisión 8: la referencia es el conjunto de aristas de relaciones de
    esqueleto del grafo de referencia MENOS las de rol_fuente
    cuarentena_laudada; los nodos de referencia son los de rol_fuente
    esqueleto (r1_tests.py:32). En el grafo bajo prueba se cuenta con el
    mismo filtro."""
    ids_ref = {n["id"] for n in ref.N if n.get("rol_fuente") == "esqueleto"}
    trip_ref_total = {(e["source"], e["relation"], e["target"]) for e in ref.E if e["relation"] in relaciones_esqueleto}
    excl_ref = {(e["source"], e["relation"], e["target"]) for e in ref.E if e["relation"] in relaciones_esqueleto and e.get("rol_fuente") == "cuarentena_laudada"}
    trip_ref = trip_ref_total - excl_ref
    trip_g_total = [e for e in G.E if e["relation"] in relaciones_esqueleto]
    excl_g = [e for e in trip_g_total if e.get("rol_fuente") == "cuarentena_laudada"]
    trip_g = {(e["source"], e["relation"], e["target"]) for e in trip_g_total if e.get("rol_fuente") != "cuarentena_laudada"}
    falt_n = sorted(ids_ref - set(G.by_id))
    falt_t = sorted(trip_ref - trip_g)
    return {"pass": not falt_n and not falt_t and len(trip_g) == len(trip_ref),
            "nodos_esqueleto_esperados": len(ids_ref), "faltan_nodos": falt_n,
            "aristas_esqueleto_referencia": len(trip_ref), "aristas_excluidas_referencia_cuarentena_laudada": len(excl_ref),
            "aristas_esqueleto_en_grafo": len(trip_g), "aristas_excluidas_grafo_cuarentena_laudada": len(excl_g),
            "aristas_relaciones_esqueleto_total_grafo": len(trip_g_total), "faltan_triplas": falt_t}


def t_t4(ctx: Contexto) -> dict:
    G = ctx.grafo
    ref = ctx.esqueleto_ref
    val = t4_paridad(G, ref, ctx.relaciones_esqueleto)
    val["esqueleto_referencia"] = {"ruta": ref.ruta, "sha256": ref.sha256}
    if val["aristas_relaciones_esqueleto_total_grafo"] == 0:
        return res("no_aplicable", f"sin aristas de relaciones de esqueleto {ctx.relaciones_esqueleto}: el paso de esqueleto (E5/assemble) no corrió sobre este grafo; "
                   f"faltan {len(val['faltan_nodos'])}/{val['nodos_esqueleto_esperados']} nodos de esqueleto", valores=val)
    return res("resuelto" if val["pass"] else "persiste",
               f"esqueleto_esperados={val['nodos_esqueleto_esperados']} faltan_nodos={len(val['faltan_nodos'])} "
               f"aristas_esqueleto_en_grafo={val['aristas_esqueleto_en_grafo']} (excluidas cuarentena_laudada={val['aristas_excluidas_grafo_cuarentena_laudada']}) "
               f"referencia={val['aristas_esqueleto_referencia']} faltan_triplas={len(val['faltan_triplas'])}", valores=val)


def _ancla_desde_codigo(codigo: str) -> tuple:
    """'ext::7.5.2' → (prefijo de archivo del TO, punto)."""
    to, punto = codigo.split("::", 1)
    return TO_PREFIJO[to], punto


def t_t5(ctx: Contexto) -> dict:
    """r1_tests.py:44-54 direccionado por (ancla origen, ancla destino,
    evidencia verbatim) de la muestra sellada (pieza d), no por ids."""
    G = ctx.grafo
    refs = [e for e in G.E if e["relation"] == "referencia" and (e.get("properties") or {}).get("evidencia") is not None]
    if not refs:
        return res("no_aplicable", "sin aristas referencia con properties.evidencia (rol_fuente referencia_cruzada): el paso r1_referencias no corrió sobre este grafo",
                   valores={"n_muestra": len(ctx.muestra30), "aristas_referencia_con_evidencia": 0})
    fallas = []
    for x in ctx.muestra30:
        sa, sp = _ancla_desde_codigo(x["source_ancla"])
        ta, tp = _ancla_desde_codigo(x["target_ancla"])
        cands = [e for e in refs if con_ancla(G.by_id.get(e["source"], {}), sa, sp) and con_ancla(G.by_id.get(e["target"], {}), ta, tp)]
        ok = any(e["properties"]["evidencia"] == x["evidencia_verbatim"] for e in cands)
        if not ok:
            fallas.append({"n": x["n"], "source_ancla": x["source_ancla"], "target_ancla": x["target_ancla"], "presente": bool(cands)})
    val = {"pass": not fallas, "n_muestra": len(ctx.muestra30), "fallas": fallas, "aristas_referencia_con_evidencia": len(refs)}
    pres = Counter(f["presente"] for f in fallas)
    return res("resuelto" if not fallas else "persiste",
               f"n_muestra={len(ctx.muestra30)} fallas={len(fallas)} (presente_con_otra_evidencia={pres.get(True, 0)}, ausente={pres.get(False, 0)})", valores=val)


def t_t6(ctx: Contexto) -> dict:
    """r1_tests.py:56-61: 5 TextoOrdenado con id TextoOrdenado_<slugify_full(archivo de E0)>."""
    G = ctx.grafo
    slug = ctx.e4["e2_lib"].slugify_full
    ids_esp = {f"TextoOrdenado_{slug(a)}" for a in ctx.archivos_e0.values()}
    tos = [n for n in G.N if n.get("type") == "TextoOrdenado"]
    ids = sorted(n["id"] for n in tos)
    val = {"pass": len(tos) == 5 and set(ids) == ids_esp, "n": len(tos), "ids": ids, "ids_esperados": sorted(ids_esp)}
    return res("resuelto" if val["pass"] else "persiste", f"n={len(tos)} fuera_del_esperado={sorted(set(ids) - ids_esp)} faltan={sorted(ids_esp - set(ids))}", valores=val)


def t7_cuarentena(G: Grafo, catalogo_ids: frozenset, politica: str) -> dict:
    """r1_tests.py:63-82 con cuarentena normalizada (decisión 2) y política
    (decisión 3): flaggeada prohíbe subclase_de desde propuesto; laudada lo
    admite hacia un id de catálogo (laudo C4) y sigue prohibiéndolo fuera."""
    assert politica in POLITICAS, politica
    propuestos = [n for n in G.N if es_propuesto(n)]
    malos = []
    for n in propuestos:
        if not cuarentena_bool(prop(n, "cuarentena")):
            malos.append((n["id"], "sin cuarentena=true"))
        if n["id"] in catalogo_ids:
            malos.append((n["id"], "propuesto con id de catálogo"))
    n_ps = 0
    for e in G.E:
        if e["relation"] == "padre_sugerido":
            n_ps += 1
            if e["target"] not in catalogo_ids:
                malos.append((e["source"], f"padre_sugerido a {e['target']} fuera de catálogo"))
        if e["relation"] == "subclase_de" and es_propuesto(G.by_id.get(e["source"], {})):
            if politica == "flaggeada":
                malos.append((e["source"], "subclase_de desde propuesto"))
            elif e["target"] not in catalogo_ids:
                malos.append((e["source"], f"subclase_de laudada a {e['target']} fuera de catálogo"))
    fuera = [n["id"] for n in G.N if n.get("type") == "Sujeto" and n["id"] not in catalogo_ids and prop(n, "nivel") != "propuesto"]
    n_sujetos = sum(1 for n in G.N if n.get("type") == "Sujeto")
    return {"pass": not malos and not fuera, "politica": politica, "n_sujetos": n_sujetos, "n_propuestos": len(propuestos),
            "n_padre_sugerido": n_ps, "malos": malos, "sujetos_fuera_catalogo_no_propuestos": fuera}


def t_t7(ctx: Contexto) -> dict:
    val = t7_cuarentena(ctx.grafo, ctx.cat.ids, ctx.politica)
    if val["n_sujetos"] == 0:
        return res("no_aplicable", "sin nodos Sujeto: test vacuo", valores=val)
    motivos = Counter(m.split(" a ")[0] for _, m in val["malos"])
    return res("resuelto" if val["pass"] else "persiste",
               f"politica={ctx.politica} propuestos={val['n_propuestos']} aristas_padre_sugerido={val['n_padre_sugerido']} malos={len(val['malos'])} "
               f"{dict(motivos)} fuera_catalogo_no_propuestos={len(val['sujetos_fuera_catalogo_no_propuestos'])}", valores=val)


def t_i1(ctx: Contexto) -> dict:
    return res("no_aplicable", "no convertible: conservación de nodos Σ pre-merge − merges = finales exige los grafos pre-merge "
               "(salida/<to>/grafo_<to>.json) y los conteos de merge, que solo existen para la cadena r1 (inventario_B21_fase1.md:135)")


def t_i2(ctx: Contexto) -> dict:
    return res("no_aplicable", "no convertible: conservación de aristas, ídem I1 (inventario_B21_fase1.md:136)")


def t_i3(ctx: Contexto) -> dict:
    """r1_invariantes.py:72-77 sobre el JSON crudo (el loader del harness funde ids duplicados en silencio, loader.py:180)."""
    G = ctx.grafo
    ids = [n["id"] for n in G.N]
    trip = [(e["source"], e["relation"], e["target"]) for e in G.E]
    dup_n, dup_t = len(ids) - len(set(ids)), len(trip) - len(set(trip))
    return res("resuelto" if dup_n == 0 and dup_t == 0 else "persiste", f"nodes={len(ids)} edges={len(trip)} ids_duplicados={dup_n} triplas_duplicadas={dup_t}",
               valores={"nodes": len(ids), "edges": len(trip), "ids_duplicados": dup_n, "triplas_duplicadas": dup_t})


def t_i4(ctx: Contexto) -> dict:
    G = ctx.grafo
    colg = [(e["source"], e["relation"], e["target"]) for e in G.E if e["source"] not in G.by_id or e["target"] not in G.by_id]
    return res("resuelto" if not colg else "persiste", f"colgantes={len(colg)}" + (f" p.ej. {colg[:3]}" if colg else ""), valores={"aristas_colgantes": len(colg)})


def t_i5(ctx: Contexto) -> dict:
    """r1_invariantes.py:83-90 sobre el adaptador: al menos una provenance por nodo y por arista."""
    G = ctx.grafo
    sin_n = [n["id"] for n in G.N if not provenances(n)]
    sin_e = [(e["source"], e["relation"], e["target"]) for e in G.E if not provenances(e)]
    return res("resuelto" if not sin_n and not sin_e else "persiste", f"nodos_sin={len(sin_n)} aristas_sin={len(sin_e)}",
               valores={"nodos_sin_provenance": len(sin_n), "aristas_sin_provenance": len(sin_e)})


# =========================================================================== #
# Tests — grupo (iii): reglas de E4 (importadas, pieza c)                     #
# =========================================================================== #
def _resolucion_propuestos(ctx: Contexto) -> list:
    """Por cada Sujeto propuesto residual: (nodo, id_resuelto, motivo, candidatos) vía r1_e4.resolver_label."""
    E4 = ctx.e4
    out = []
    for n in ctx.grafo.N:
        if es_propuesto(n):
            rid, motivo, cands = E4["r1_e4"].resolver_label(n.get("label") or "", prop(n, "padre_sugerido"), E4["indice"])
            out.append((n, rid, motivo, cands))
    return out


def _e4_criterio(ctx: Contexto, criterio: str, extra_detalle: str = "") -> dict:
    """F1 ausente: ningún propuesto residual que E4 resolvería (motivo
    resuelto_por_*) con `criterio` entre sus candidatos. Sin propuestos →
    no_aplicable (vacuo)."""
    filas = _resolucion_propuestos(ctx)
    if not filas:
        return res("no_aplicable", "sin Sujetos propuestos: la regla no tiene sobre qué aplicarse (vacuo)", valores={"n_propuestos": 0})
    resolubles = [(n["id"], rid, motivo) for n, rid, motivo, cands in filas if rid is not None and any(c == criterio for c, _ in cands)]
    con_cand = sum(1 for n, rid, motivo, cands in filas if any(c == criterio for c, _ in cands))
    return res("resuelto" if not resolubles else "persiste",
               f"propuestos={len(filas)} con candidato {criterio}={con_cand} resolubles no resueltos={len(resolubles)} {resolubles[:3]}{extra_detalle}",
               valores={"n_propuestos": len(filas), "resolubles": resolubles})


def t_e4_a1(ctx): return _e4_criterio(ctx, "label_exacto")
def t_e4_a2(ctx): return _e4_criterio(ctx, "alias_exacto")
def t_e4_a3(ctx): return _e4_criterio(ctx, "id_slug")
def t_e4_a4(ctx): return _e4_criterio(ctx, "label_singularizado")


def t_e4_a5(ctx: Contexto) -> dict:
    """alias_en_parentesis, condicionado por properties.padre_sugerido (F3): la
    condición sobre el padre la aplica resolver_label (r1_e4.py:108-112)."""
    filas = _resolucion_propuestos(ctx)
    con_padre = sum(1 for n, _, _, _ in filas if prop(n, "padre_sugerido"))
    return _e4_criterio(ctx, "alias_en_parentesis", f"; propuestos con padre_sugerido={con_padre}")


def t_e4_a6(ctx: Contexto) -> dict:
    """Ambigüedad: (i) claves ambiguas del índice del catálogo; (ii) todo alias
    en alias_resueltos re-resuelve, sin ambigüedad, al id que lo porta; (iii)
    ningún propuesto residual con motivo distinto de sin_match_en_catalogo /
    ambiguo se contabiliza acá (es de a1–a5). El caso positivo (dos criterios
    a ids distintos) no ocurre en el catálogo v2: se ejercita en el selftest."""
    E4 = ctx.e4
    ambiguas = sum(1 for v in E4["indice"].values() if v == "__AMBIGUO__")
    filas = _resolucion_propuestos(ctx)
    portadores = [n for n in ctx.grafo.N if n.get("type") == "Sujeto" and prop(n, "alias_resueltos")]
    if not filas and not portadores:
        return res("no_aplicable", f"sin propuestos ni alias_resueltos: la regla no tiene sobre qué aplicarse (claves ambiguas del índice={ambiguas})",
                   valores={"claves_ambiguas": ambiguas})
    malos = []
    for n in portadores:
        for alias in prop(n, "alias_resueltos") or []:
            rid, motivo, _ = E4["r1_e4"].resolver_label(alias, None, E4["indice"])
            if motivo == "ambiguo" or rid != n["id"]:
                malos.append((n["id"], alias, rid, motivo))
    n_amb = sum(1 for _, _, motivo, _ in filas if motivo == "ambiguo")
    return res("resuelto" if not malos else "persiste",
               f"claves ambiguas del índice={ambiguas}; propuestos residuales con motivo ambiguo={n_amb}/{len(filas)}; "
               f"alias_resueltos re-resueltos={sum(len(prop(n, 'alias_resueltos') or []) for n in portadores) - len(malos)}/"
               f"{sum(len(prop(n, 'alias_resueltos') or []) for n in portadores)} malos={malos[:3]}",
               valores={"claves_ambiguas": ambiguas, "ambiguos_residuales": n_amb, "malos": malos})


def t_e4_a7(ctx: Contexto) -> dict:
    """Lo no resuelto queda tal cual: nivel=propuesto + cuarentena=true (bool o
    "true"), y ningún Sujeto fuera del catálogo que no sea propuesto (F3 +
    F1). Es la parte de T7 que no depende de la política."""
    G = ctx.grafo
    propuestos = [n for n in G.N if es_propuesto(n)]
    fuera = [n["id"] for n in G.N if n.get("type") == "Sujeto" and n["id"] not in ctx.cat.ids and not es_propuesto(n)]
    if not propuestos and not fuera and not any(n.get("type") == "Sujeto" for n in G.N):
        return res("no_aplicable", "sin nodos Sujeto (vacuo)")
    sin_cuar = [n["id"] for n in propuestos if not cuarentena_bool(prop(n, "cuarentena"))]
    en_cat = [n["id"] for n in propuestos if n["id"] in ctx.cat.ids]
    ok = not sin_cuar and not en_cat and not fuera
    return res("resuelto" if ok else "persiste", f"propuestos={len(propuestos)} sin_cuarentena_true={len(sin_cuar)} con_id_de_catalogo={len(en_cat)} "
               f"sujetos_fuera_catalogo_no_propuestos={len(fuera)}", valores={"n_propuestos": len(propuestos), "sin_cuarentena": sin_cuar, "fuera": fuera})


def t_e4_a8(ctx: Contexto) -> dict:
    """Merge aditivo registrado: alias_resueltos (F3) en los ids de catálogo a
    los que resolvieron los propuestos de e4_propuestos.json (cadena r1,
    estado resuelto) y ausencia de esos propuestos (F1 ausente) y de aristas
    que los toquen (F4 ausente). La acumulación de provenances y el dedup de
    triplas solo son observables con el grafo pre-E4: no_aplicable, con razón."""
    G = ctx.grafo
    tabla = json.loads(E4_PROPUESTOS_R1.read_text(encoding="utf-8"))
    remap = [(f["id_propuesto"], f["resuelto_a"], f["label"]) for f in tabla if f.get("estado") == "resuelto"]
    portadores = {n["id"]: prop(n, "alias_resueltos") for n in G.N if n.get("type") == "Sujeto" and prop(n, "alias_resueltos")}
    presentes_prop = [p for p, _, _ in remap if p in G.by_id]
    if not portadores and not presentes_prop:
        return res("no_aplicable", f"ninguno de los {len(remap)} propuestos resueltos en r1 existe en el grafo y no hay alias_resueltos: sin evento de E4-a8 que verificar; "
                   "la acumulación de provenances y el dedup de triplas exigen el grafo pre-E4 (solo cadena r1)", valores={"remap": remap})
    sub = OrderedDict()
    for p, rid, label in remap:
        sub[f"alias_en_{rid}"] = label in (portadores.get(rid) or [])
        sub[f"ausente_{p[:40]}"] = p not in G.by_id and not G.salientes(p) and not G.entrantes(p)
    ok = all(sub.values())
    return res("resuelto" if ok else "persiste", f"alias_resueltos en {sum(1 for p, rid, l in remap if l in (portadores.get(rid) or []))}/{len(remap)} ids de catálogo; "
               f"propuestos resueltos aún presentes={len(presentes_prop)}; provenances acumuladas y dedup: no observables sin el grafo pre-E4 (no_aplicable parcial)",
               subchecks=sub, valores={"remap": remap, "portadores": portadores})


def t_e4_b(ctx: Contexto) -> dict:
    """Un único TextoOrdenado por TO con id y archivo desde E0 (= T6 + F3 properties.archivo ∈ archivos de E0)."""
    r = t_t6(ctx)
    G = ctx.grafo
    arch = set(ctx.archivos_e0.values())
    tos = [(n["id"], prop(n, "archivo")) for n in G.N if n.get("type") == "TextoOrdenado"]
    fuera = [(i, a) for i, a in tos if a not in arch]
    ok = r["estado"] == "resuelto" and not fuera
    return res("resuelto" if ok else "persiste", f"TextoOrdenado={len(tos)}; con properties.archivo en el conjunto de E0: {len(tos) - len(fuera)}/{len(tos)}; fuera={fuera}; T6={r['estado']}",
               valores={"n": len(tos), "fuera": fuera})


def t_e4_c(ctx: Contexto) -> dict:
    G = ctx.grafo
    tos = [n for n in G.N if n.get("type") == "TextoOrdenado"]
    return res("no_aplicable", "solo observable con el registro de conflictos (salida_r1/e4_conflictos.json) o los grafos pre-E4: los conflictos de "
               "properties no se persisten en el kg.json; el proxy débil (un solo valor de materia/version por TextoOrdenado) no es la regla "
               f"(inventario_B21_fase1.md:176). Informativo: TextoOrdenado={len(tos)}, materia={sorted({str(prop(n, 'materia')) for n in tos})[:6]}")


# =========================================================================== #
# Registro de los 46 ítems (id del inventario, forma, direccionamiento, evidencia)
# =========================================================================== #
def T(id_, fn, forma, direcc, evidencia, nota=""):
    return {"id": id_, "fn": fn, "forma": forma, "direccionamiento": direcc, "evidencia": evidencia, "nota": nota}


INV = "reports/revision_UB21_diag/inventario_B21_fase1.md"
SA = "reports/revision_UB21_diag/sonda_anclas_C1_C7_UB21"
ST = "reports/revision_UB21_diag/sonda_T1_T7_cuatro_grafos_UB21"
SR = "reports/revision_UB21_diag/sonda_ranks_buscar_nodos_UB21"

TESTS = [
    T("BKL-0017", t_bkl_0017, "F1 + F4 ×2 + F5 ×3 (limite 10)",
      "(TO_clasificacion, 1.1, Obligacion, «los clientes de la entidad (tanto residentes en el pais»)",
      f"data/backlog/retests/C1_retest_2026-07-31.md:33-44 (4/4; ranks 1/1/3 :42-44); {SA}.py:100-111; {INV}:99"),
    T("BKL-0006", t_bkl_0006, "F3 (montos de la tabla) + F4 (exceptua → restantes) + F5 ×2 informativo (limite 10 / 13)",
      "(TO_capitales, 1.2, cualquier tipo, «exigencia basica» + «bancos» / «restantes entidades»); Excepcion por (cap, 1.2, Excepcion, «cajas de credito cooperativas»)",
      f"data/backlog/retests/C2_retest_2026-07-31.md:51-63 ((1)-(4) PASS; (5) informativo :59-63); {SA}.py:114-134; {INV}:100",
      "los ids viejos/nuevos del retest (3) son ids de contenido: excluidos del estado por la decisión 1"),
    T("BKL-0023", t_bkl_0023, "F3 (properties.umbral)",
      "(TO_capitales, 1.2, Restriccion, «companias financieras que realicen, en forma directa, operaciones de comercio exterior»)",
      f"data/backlog/retests/C3_retest_2026-08-02.md:30-37 ((a)-(d) 4/4); {SA}.py:146-155; {INV}:101",
      "sin nodo o sin umbral → no_aplicable, nunca PASS vacuo (pieza e)"),
    T("BKL-0019", t_bkl_0019, "F4 ×8 (subclase_de si laudada / padre_sugerido si flaggeada) + F4 ausente (excluida, laudada)",
      "8 sujetos por label normalizado de cuarentena.json (o id de cuarentena C4_retest:35-42) → padre laudado (id de catálogo); ver_vecinos (e) reducido a arista presente",
      f"data/backlog/retests/C4_retest_2026-08-02.md:35-42 (tabla), :52-58 ((a)-(e) 5/5); {SA}.py:158-190; {INV}:102"),
    T("BKL-0004", t_bkl_0004, "F1 ×9 + F4 (8 regula + 9 establecida_en) + F5 ×8 (7 consultas + proxy RT-C5-4; limite 10)",
      "(TO_clasificacion, 6.5 / 6.5.1 / 6.5.2 / 6.5.2.1 / 6.5.2.2 / 6.5.2.3 / 6.5.3 / 6.5.4 / 6.5.5, cualquier tipo, frase del título)",
      f"data/backlog/retests/C5_retest_2026-08-02.md:56-66 (32/32), :68-74 (proxy RT-4); data/backlog/propuestas/E4_enumeracion_65.md:283-289 (ranks); {SA}.py:193-226; {INV}:103"),
    T("BKL-0003", t_bkl_0003, "F1 + F4 ×2 + F4 ausente (a Sujeto) + F5 ×11 (N1 + controles rol/pnfc; limite 10)",
      "(TO_proteccion, 1.1.2.5, Excepcion, «mutuales o cooperativas»); controles por id de catálogo Sujeto_rol_sujeto_obligado_proteccion / Sujeto_proveedor_no_financiero_de_credito",
      f"data/backlog/retests/C6_retest_2026-08-03.md:52-62 (38/38); data/backlog/propuestas/E3_salvedad_mutuales.md:288-298 (ranks); {SA}.py:229-254; {INV}:104"),
    T("BKL-0005", t_bkl_0005, "F3 (dos calificadores en descripcion) + F5 ×3 (limite 10)",
      "(TO_regimen_informativo, 7.1, Obligacion, «para el calculo del importe correspondiente al mes n»)",
      f"data/backlog/retests/C7_retest_2026-08-03.md:67-78 (27/27; ranks :78); {SA}.py:257-264; {INV}:105"),
    T("BKL-0007", t_bkl_0007, "= BKL-0017 (sin test propio)", "= BKL-0017",
      f"data/backlog/backlog.jsonl líneas 42 y 46 (cerrada por referencia); {INV}:106, §5.9 :269", NOTA_SIN_APLICACION),
    T("BKL-0026", t_bkl_0026, "ninguna (no convertible)", "—", f"{INV}:107; data/backlog/retests/C6_retest_2026-08-03.md:99-103", NOTA_SIN_APLICACION),
    T("BKL-0027", t_bkl_0027, "ninguna (no convertible)", "—", f"{INV}:108; data/backlog/retests/C6_retest_2026-08-03.md:104-108", NOTA_SIN_APLICACION),
    T("BKL-0028", t_bkl_0028, "F1 sobre el catálogo parametrizado (ids «del exterior» separados; sin alias del exterior en los domésticos) + F1 en el grafo",
      "ids de catálogo Sujeto_entidad_financiera / Sujeto_banco / Sujeto_entidad_cambiaria", f"{INV}:109 (backlog línea 73)", NOTA_SIN_APLICACION),
    T("BKL-0029", t_bkl_0029, "F4 (miembro_de del rol de convca → id nuevo del catálogo)",
      "id de catálogo Sujeto_rol_alcance_convca; cobertura de convca por provenance", f"{INV}:110 (backlog línea 74)",
      NOTA_SIN_APLICACION + "; no_aplicable en todo grafo que no cubra convca (pieza e)"),
    T("RT-C5-1", t_rt_c5_1, "F3 (valor: cinco categorías en N1)", "N1 de C5", f"data/backlog/propuestas/E4_enumeracion_65.md:227-230; C5_retest:66 (d); {INV}:111", "solo valor (decisión 5)"),
    T("RT-C5-2", t_rt_c5_2, "F3 (valor: tres situaciones en N3)", "N3 de C5", f"data/backlog/propuestas/E4_enumeracion_65.md:231-234; C5_retest:66 (d); {INV}:112", "solo valor (decisión 5)"),
    T("RT-C5-3", t_rt_c5_3, "F3 (valor: «antes de los 60 días … mora» en N5)", "N5 de C5", f"data/backlog/propuestas/E4_enumeracion_65.md:235-238; C5_retest:66 (d); {INV}:113", "solo valor (decisión 5)"),
    T("RT-C5-4", t_rt_c5_4, "F3 (valor: primera vez / primera cuota / única vez en N6)", "N6 de C5",
      f"data/backlog/propuestas/E4_enumeracion_65.md:239-242; C5_retest:66-74 (d, observación RT-4); {INV}:114", "solo valor (decisión 5); su consulta proxy se evalúa en BKL-0004"),
    T("RT-C5-5", t_rt_c5_5, "F2 (nodo con «riesgo medio» anclado en 7.2 exacto) + F3 (N1 sin niveles del 7.2)",
      "(TO_clasificacion, 7.2 exacto, cualquier tipo, «riesgo medio»); N1 de C5", f"data/backlog/propuestas/E4_enumeracion_65.md:243-247; C5_retest:66 (d); {SA}.py:219-226; {INV}:115, §5.7 :267"),
    T("RT-C6-1", t_rt_c6_1, "F3 (valor en N1)", "N1 de C6", f"data/backlog/propuestas/E3_salvedad_mutuales.md:151-156; C6_retest:62 (d); {INV}:116", "solo valor (decisión 5)"),
    T("RT-C6-2", t_rt_c6_2, "F3 (valor en N1; = RT-C6-1)", "N1 de C6", f"data/backlog/propuestas/E3_salvedad_mutuales.md:157-164; C6_retest:62 (d); {INV}:117", "solo valor (decisión 5)"),
    T("RT-C6-3", t_rt_c6_3, "F4 ×n (miembro_de entrantes = miembros del rol en el catálogo)", "id de catálogo Sujeto_rol_sujeto_obligado_proteccion",
      f"data/backlog/propuestas/E3_salvedad_mutuales.md:165-174; C6_retest:62 (RT-3); {SA}.py:246-252; {INV}:118", "solo valor/estructura (decisión 5)"),
    T("RT-C6-4", t_rt_c6_4, "F4 (emisoras --miembro_de--> rol) + F4 ausente (N1 ↔ Sujeto)", "ids de catálogo; N1 de C6",
      f"data/backlog/propuestas/E3_salvedad_mutuales.md:175-179; C6_retest:62 (RT-4); {SA}.py:241-253; {INV}:119"),
    T("RT-C7-1", t_rt_c7_1, "F3 (valor: ambos calificadores en el portador)", "portador de C7", f"data/backlog/retests/C7_retest_2026-08-03.md:78 (d); {INV}:120, §5.8 :268", "solo valor (decisión 5); su consulta se evalúa en BKL-0005"),
    T("RT-C7-2", t_rt_c7_2, "F3 (valor: calificador de la RPC)", "portador de C7", f"data/backlog/retests/C7_retest_2026-08-03.md:78 (d); {INV}:121", "solo valor (decisión 5); su consulta se evalúa en BKL-0005"),
    T("RT-C7-3", t_rt_c7_3, "F3 (valor: calificador de la franquicia)", "portador de C7", f"data/backlog/retests/C7_retest_2026-08-03.md:78 (d); {INV}:122", "solo valor (decisión 5); su consulta se evalúa en BKL-0005"),
    T("T1", t_t1, "F2 + F3", "(TO_exterior, 3.9 y 3.9.x, cualquier tipo, «200»)",
      f"data/experiment/reextraccion_v2/corpus_v2/ensamblar_corpus.py:237-249 (reescrito sobre el adaptador); salida_r1/tests_respuesta_conocida_r1.json:2-4; {ST}_salida.txt:52; {INV}:128"),
    T("T2", t_t2, "F1 (conteo) + F2 (conteo de puntos)", "(TO_exterior, cualquier punto, cualquier tipo, «125 %» o «125%»)",
      f"ensamblar_corpus.py:251-265 (reescrito sobre el adaptador); tests_respuesta_conocida_r1.json:20-22; {ST}_salida.txt:53; {INV}:129"),
    T("T3", t_t3, "F2 + F3", "(TO_proteccion, 1.1.2.5, cualquier tipo, «mutual» o «cooperativ»)",
      f"ensamblar_corpus.py:267-280 (reescrito sobre el adaptador); tests_respuesta_conocida_r1.json:75-77; {ST}_salida.txt:54; {INV}:130"),
    T("T4", t_t4, "F1 + F4 (paridad de esqueleto contra --esqueleto-referencia, decisión 8)",
      "nodos rol_fuente=esqueleto y aristas de relaciones de esqueleto de la referencia, menos rol_fuente=cuarentena_laudada",
      f"data/experiment/reextraccion_v2/corpus_v2/r1_tests.py:30-42; tests_respuesta_conocida_r1.json:92-96; {ST}_salida.txt:27,55; {INV}:131, §5.1 :261"),
    T("T5", t_t5, "F4 + F3 (properties.evidencia)", "(ancla origen, ancla destino, evidencia verbatim) de salida_r1/referencias_muestra30_inspeccionada_A2.json (sha256 4dbc2d30…)",
      f"r1_tests.py:44-54; tests_respuesta_conocida_r1.json:99-101; {ST}_salida.txt:56; {INV}:132"),
    T("T6", t_t6, "F1", "TextoOrdenado_<e2_lib.slugify_full(archivo de E0 por TO)>",
      f"r1_tests.py:56-61; tests_respuesta_conocida_r1.json:104-105; {ST}_salida.txt:57; {INV}:133"),
    T("T7", t_t7, "F3 + F4 + F4 ausente (política de cuarentena, decisión 3)", "Sujetos con nivel=propuesto; catálogo parametrizado",
      f"r1_tests.py:63-82; tests_respuesta_conocida_r1.json:115-118; {ST}_salida.txt:30,58; {INV}:134, §5.2 :262"),
    T("I1", t_i1, "ninguna (no convertible)", "—", f"data/experiment/reextraccion_v2/corpus_v2/r1_invariantes.py:7,62-68; {INV}:135"),
    T("I2", t_i2, "ninguna (no convertible)", "—", f"r1_invariantes.py:8,69-70; {INV}:136"),
    T("I3", t_i3, "F1 (conteo: unicidad de ids y de triplas)", "JSON crudo", f"r1_invariantes.py:9,72-77; {ST}_salida.txt:60; {INV}:137"),
    T("I4", t_i4, "F4 (cero colgantes)", "JSON crudo", f"r1_invariantes.py:10,79-81; {ST}_salida.txt:61; {INV}:138"),
    T("I5", t_i5, "F2 (al menos una provenance por nodo y arista, adaptador)", "JSON crudo", f"r1_invariantes.py:11-12,83-90; {ST}_salida.txt:62; {INV}:139"),
    T("E4-a1", t_e4_a1, "F1 ausente (ningún propuesto residual resoluble por label_exacto)", "Sujetos propuestos; r1_e4.indice_catalogo / resolver_label sobre el catálogo parametrizado",
      f"data/experiment/reextraccion_v2/corpus_v2/r1_e4.py:10,89,101; {INV}:167, §4 :234-250"),
    T("E4-a2", t_e4_a2, "F1 ausente (alias_exacto)", "ídem", f"r1_e4.py:11,92-93,102; {INV}:168, §4"),
    T("E4-a3", t_e4_a3, "F1 ausente (id_slug; e2_lib.slugify_full importado)", "ídem", f"r1_e4.py:12,90,103; data/experiment/reextraccion_v2/e2_reduce/e2_lib.py:90; {INV}:169, §4"),
    T("E4-a4", t_e4_a4, "F1 ausente (label_singularizado)", "ídem", f"r1_e4.py:13-14,53-58,91,104; {INV}:170, §4"),
    T("E4-a5", t_e4_a5, "F1 ausente (alias_en_parentesis) + F3 (padre_sugerido)", "ídem", f"r1_e4.py:15-17,108-112; {INV}:171, §4"),
    T("E4-a6", t_e4_a6, "F1 ausente (claves ambiguas / alias_resueltos que re-resuelven sin ambigüedad)", "ídem + Sujetos con properties.alias_resueltos", f"r1_e4.py:7-9,79-84,113-117; {INV}:172, §4"),
    T("E4-a7", t_e4_a7, "F3 (cuarentena=true normalizada) + F1 (todo Sujeto no propuesto ∈ catálogo)", "Sujetos; catálogo parametrizado", f"r1_e4.py:18-19,141-147; {INV}:173"),
    T("E4-a8", t_e4_a8, "F3 (alias_resueltos en ids de catálogo) + F1 ausente + F4 ausente; parte pre-E4 no_aplicable",
      "ids de catálogo de salida_r1/e4_propuestos.json (estado resuelto)", f"r1_e4.py:20-24,152-171,178-202; salida_r1/e4_propuestos.json; {INV}:174, §4 :248"),
    T("E4-b", t_e4_b, "F1 (= T6) + F3 (properties.archivo ∈ archivos de E0)", "TextoOrdenado", f"r1_e4.py:26-30,208-250; salida_r1/e4_texto_ordenado.json; {INV}:175, §4"),
    T("E4-c", t_e4_c, "ninguna directa (no observable sobre un kg.json)", "—", f"r1_e4.py:32-36,256-291; salida_r1/e4_conflictos.json; {INV}:176"),
]


def convertibilidad(id_: str) -> str:
    if id_ in CONVERTIBLES:
        return "convertible"
    if id_ in CON_CONDICION:
        return "con condición"
    if id_ in NO_CONVERTIBLES:
        return "no convertible"
    raise KeyError(id_)


def grupo(id_: str) -> str:
    return "i-BKL" if id_.startswith("BKL") else "i-RT" if id_.startswith("RT") else "ii" if id_[0] in "TI" else "iii"


def verificar_particion() -> dict:
    """46 ítems, ids únicos, partición 19 / 23 / 4 y 15 dependientes del retriever, tal como la tabla resumen §1."""
    ids = [t["id"] for t in TESTS]
    assert len(ids) == 46 and len(set(ids)) == 46, len(ids)
    assert set(ids) == set(CONVERTIBLES) | set(CON_CONDICION) | set(NO_CONVERTIBLES)
    assert (len(CONVERTIBLES), len(CON_CONDICION), len(NO_CONVERTIBLES)) == (19, 23, 4)
    assert len(RETRIEVER) == 15 and set(RETRIEVER) <= set(ids)
    c = Counter(grupo(i) for i in ids)
    assert c == {"i-BKL": 12, "i-RT": 12, "ii": 12, "iii": 10}, c
    return {"items": 46, "convertibles": 19, "con_condicion": 23, "no_convertibles": 4, "retriever": 15, "por_grupo": dict(c)}


# =========================================================================== #
# Ejecución, salida y regresión                                                #
# =========================================================================== #
def ejecutar(ctx: Contexto, solo=None) -> list:
    out = []
    for t in TESTS:
        if solo and t["id"] not in solo:
            continue
        r = t["fn"](ctx)
        item = OrderedDict()
        item["id"] = t["id"]
        item["grupo"] = grupo(t["id"])
        item["convertibilidad"] = convertibilidad(t["id"])
        item["retriever"] = "sí" if t["id"] in RETRIEVER else "no"
        item["forma"] = t["forma"]
        item["direccionamiento"] = t["direccionamiento"]
        item["evidencia"] = t["evidencia"]
        if t["nota"]:
            item["nota"] = t["nota"]
        item["estado"] = r["estado"]
        item["detalle"] = r["detalle"]
        for k in ("subchecks", "valores", "ranks"):
            if r.get(k) is not None:
                item[k] = r[k]
        out.append(item)
    return out


def resumen_ranks(items: list) -> dict:
    filas = [f for it in items for f in it.get("ranks") or []]
    objs = [o for f in filas for o in f["objetivos"]]
    return {"consultas": len(filas), "consultas_coinciden_sellado": sum(1 for f in filas if all(o["coincide_sellado"] for o in f["objetivos"])),
            "objetivos": len(objs), "objetivos_coinciden_sellado": sum(1 for o in objs if o["coincide_sellado"]),
            "objetivos_en_ventana": sum(1 for o in objs if o["en_ventana"]),
            "objetivos_ausentes": sum(1 for o in objs if not o["objetivo_presente"])}


def seleccionar_esperado(fixture: dict, kg_sha: str):
    """Entrada de la fixture cuyo kg_sha256 coincide: ('estado_esperado' | 'linea_de_base_observada', nombre, entrada) o None."""
    for parte in ("estado_esperado", "linea_de_base_observada"):
        for nombre, ent in (fixture.get(parte) or {}).items():
            if isinstance(ent, dict) and ent.get("kg_sha256") == kg_sha:
                return parte, nombre, ent
    return None


def computar_regresion(items: list, esperado: dict, ranks: dict | None = None) -> dict:
    """Regresión = estado medido ≠ estado esperado (6bis). esperado null =
    NO VERIFICADA: no computa. Ítems medidos sin entrada esperada y
    viceversa se listan. `ranks_sellados` esperado (consultas/objetivos que
    coinciden) se compara como pseudo-ítem RANKS_SELLADOS."""
    esp_items = esperado.get("items") or {}
    medido = {it["id"]: it["estado"] for it in items}
    regresiones, no_verificadas, coinciden = [], [], []
    for id_, m in medido.items():
        e = esp_items.get(id_)
        if e is None:
            continue
        est = e.get("estado") if isinstance(e, dict) else e
        if est is None:
            no_verificadas.append(id_)
        elif est != m:
            regresiones.append({"item": id_, "esperado": est, "medido": m, "evidencia_del_esperado": (e.get("evidencia") if isinstance(e, dict) else None)})
        else:
            coinciden.append(id_)
    sin_esperado = sorted(set(medido) - set(esp_items))
    sin_medido = sorted(set(esp_items) - set(medido))
    rk_esp = esperado.get("ranks_sellados")
    if rk_esp and ranks is not None:
        m = {"consultas": ranks["consultas_coinciden_sellado"], "objetivos": ranks["objetivos_coinciden_sellado"]}
        e = {"consultas": rk_esp.get("consultas"), "objetivos": rk_esp.get("objetivos")}
        if m != e:
            regresiones.append({"item": "RANKS_SELLADOS", "esperado": e, "medido": m, "evidencia_del_esperado": rk_esp.get("evidencia")})
        else:
            coinciden.append("RANKS_SELLADOS")
    return {"n_regresiones": len(regresiones), "regresiones": regresiones, "coinciden": len(coinciden),
            "no_verificadas": no_verificadas, "sin_esperado": sin_esperado, "sin_medido": sin_medido}


def codigo_salida(regresion: dict | None) -> int:
    return 1 if regresion and regresion.get("n_regresiones") else 0


def _fila_md(it: dict) -> str:
    det = it["detalle"].replace("|", "\\|").replace("\n", " ")
    if len(det) > 220:
        det = det[:217] + "…"
    return f"| {it['id']} | {it['grupo']} | {it['convertibilidad']} | {it['retriever']} | {it['forma'].replace('|', '/')} | **{it['estado']}** | {det} |"


def render_md(salida: dict) -> str:
    p = salida["parametros"]
    L = ["# Regression suite — " + p["kg"], ""]
    L.append(f"- kg: `{p['kg']}` sha256 `{p['kg_sha256']}` — {p['n_nodes']} nodos / {p['n_edges']} aristas; generación declarada {p['generacion']} (formato detectado: {p['generacion_detectada']})")
    L.append(f"- catálogo: `{p['catalogo']}` (versión {p['catalogo_version']}, sha256 `{p['catalogo_sha256']}`); política de cuarentena: **{p['politica_cuarentena']}**")
    L.append(f"- esqueleto de referencia (T4): `{p['esqueleto_referencia']}`" + (f" sha256 `{p['esqueleto_referencia_sha256']}`" if p.get("esqueleto_referencia_sha256") else " (no cargado)"))
    L.append(f"- retriever: GraphIndex de data/experiment/evaluacion/harness.py (importado; sha256 `{p['harness_sha256']}`), loader.load_graph_from_path adapter_key=None")
    L.append(f"- partición declarada: {p['particion']}")
    L.append("")
    r = salida["resumen"]
    L.append(f"## Resumen: {r['items']} ítems — resuelto {r['resuelto']} / persiste {r['persiste']} / no_aplicable {r['no_aplicable']}")
    rk = salida["ranks_sellados"]
    L.append(f"Ranks sellados (retriever in-memory): consultas que coinciden con el sellado {rk['consultas_coinciden_sellado']}/{rk['consultas']}; "
             f"objetivos {rk['objetivos_coinciden_sellado']}/{rk['objetivos']}; objetivos en ventana declarada {rk['objetivos_en_ventana']}; objetivos ausentes {rk['objetivos_ausentes']}.")
    L.append("")
    L.append("| Id | Grupo | Convertibilidad | Retr. | Forma | Estado | Detalle |")
    L.append("|---|---|---|---|---|---|---|")
    for it in salida["items"]:
        L.append(_fila_md(it))
    L.append("")
    reg = salida.get("regresion")
    L.append("## Regresión contra la fixture")
    if reg is None:
        L.append(salida.get("regresion_nota") or "Sin `--esperado`: no se computa regresión.")
    else:
        L.append(f"Fixture `{reg['fixture']}` (sha256 `{reg['fixture_sha256']}`; subárbol estado_esperado sha256 `{reg['estado_esperado_sha256']}`), entrada **{reg['entrada']}** ({reg['parte']}).")
        if reg.get("nota"):
            L.append(reg["nota"])
        if "n_regresiones" in reg:
            L.append(f"- regresiones: **{reg['n_regresiones']}**; coinciden: {reg['coinciden']}; NO VERIFICADAS (esperado null): {reg['no_verificadas']}; sin esperado: {reg['sin_esperado']}; sin medido: {reg['sin_medido']}")
            for x in reg["regresiones"]:
                L.append(f"  - REGRESIÓN {x['item']}: esperado {x['esperado']} / medido {x['medido']} — evidencia del esperado: {x['evidencia_del_esperado']}")
    L.append("")
    L.append("## Consultas de rank (por ítem)")
    for it in salida["items"]:
        for f in it.get("ranks") or []:
            partes = [f"{o['objetivo']}: rank={o['rank']} sellado={o['rank_esperado_sellado']} limite={o['limite']} "
                      f"{'=' if o['coincide_sellado'] else '≠'}{'' if o['objetivo_presente'] else ' [objetivo AUSENTE]'}" for o in f["objetivos"]]
            L.append(f"- [{it['id']}] «{f['consulta']}» (limite pedido {f['limite_pedido']}): " + " | ".join(partes))
    L.append("")
    return "\n".join(L)


def correr(args) -> tuple:
    """Devuelve (salida dict, código de salida)."""
    kg_path = Path(args.kg)
    G = Grafo.desde_ruta(kg_path)
    cat = Catalogo.desde_ruta(args.catalogo)
    if G.generacion_detectada and G.generacion_detectada != args.generacion:
        raise SystemExit(f"--generacion {args.generacion} no coincide con el formato de provenance detectado (gen {G.generacion_detectada}) en {kg_path}")
    ctx = Contexto(G, cat, args.generacion, args.politica_cuarentena, esqueleto_ref_ruta=args.esqueleto_referencia)
    solo = set(args.solo.split(",")) if args.solo else None
    items = ejecutar(ctx, solo)
    resumen = Counter(it["estado"] for it in items)
    salida = OrderedDict()
    salida["suite"] = "scripts/regression_kg.py (U-B2.1 fase 2)"
    salida["parametros"] = OrderedDict([
        ("kg", str(kg_path)), ("kg_sha256", G.sha256), ("n_nodes", len(G.N)), ("n_edges", len(G.E)),
        ("generacion", args.generacion), ("generacion_detectada", G.generacion_detectada),
        ("catalogo", str(args.catalogo)), ("catalogo_version", cat.version), ("catalogo_sha256", cat.sha256),
        ("politica_cuarentena", args.politica_cuarentena),
        ("esqueleto_referencia", str(args.esqueleto_referencia or DEFAULT_ESQUELETO_REF)),
        ("esqueleto_referencia_sha256", ctx._esqueleto_ref.sha256 if ctx._esqueleto_ref is not None else None),
        ("harness_sha256", sha256_path(EVALUACION / "harness.py")), ("loader_sha256", sha256_path(EVALUACION / "loader.py")),
        ("particion", verificar_particion()), ("solo", sorted(solo) if solo else None),
    ])
    salida["resumen"] = {"items": len(items), "resuelto": resumen.get("resuelto", 0), "persiste": resumen.get("persiste", 0), "no_aplicable": resumen.get("no_aplicable", 0)}
    salida["ranks_sellados"] = resumen_ranks(items)
    salida["items"] = items
    codigo = 0
    if args.esperado:
        fx_path = Path(args.esperado)
        fixture = json.loads(fx_path.read_text(encoding="utf-8"))
        reg = OrderedDict([("fixture", str(fx_path)), ("fixture_sha256", sha256_path(fx_path)),
                           ("estado_esperado_sha256", sha256_canonico(fixture.get("estado_esperado") or {}))])
        sel = seleccionar_esperado(fixture, G.sha256)
        if sel is None:
            reg["parte"], reg["entrada"] = None, None
            reg["nota"] = f"la fixture no tiene entrada con kg_sha256 {G.sha256}: no se computa regresión"
        else:
            parte, nombre, ent = sel
            reg["parte"], reg["entrada"] = parte, nombre
            difieren = [k for k, v in (("generacion", args.generacion), ("politica_cuarentena", args.politica_cuarentena), ("catalogo_sha256", cat.sha256))
                        if ent.get(k) is not None and ent.get(k) != v]
            if parte != "estado_esperado":
                reg["nota"] = "entrada de LÍNEA DE BASE OBSERVADA: no participa del cómputo de regresión en esta fase (pieza f.2)"
            elif difieren:
                reg["nota"] = f"parámetros de la corrida distintos de los de la fixture ({difieren}): no se computa regresión"
                codigo = 2
            else:
                reg.update(computar_regresion(items, ent, salida["ranks_sellados"]))
                codigo = codigo_salida(reg)
        salida["regresion"] = reg
    else:
        salida["regresion"] = None
    if args.out:
        out_md = Path(args.out)
        out_json = out_md.with_suffix(".json")
        out_md.write_text(render_md(salida), encoding="utf-8")
        out_json.write_text(json.dumps(salida, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return salida, codigo


def parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(description="Regression suite del grafo (U-B2.1 fase 2).")
    ap.add_argument("--kg", required=True, help="ruta al kg.json (solo lectura)")
    ap.add_argument("--generacion", type=int, choices=(2, 3), required=True, help="2 = {source_doc, location}; 3 = {archivo, punto}")
    ap.add_argument("--catalogo", required=True, help="esquema_v2_clases.json o esquema_v3_clases.json (leído del artefacto)")
    ap.add_argument("--politica-cuarentena", choices=POLITICAS, required=True, dest="politica_cuarentena")
    ap.add_argument("--esperado", default=None, help="fixture scripts/regression_kg_esperado.json; sin ella no se computa regresión")
    ap.add_argument("--esqueleto-referencia", default=None, dest="esqueleto_referencia", help=f"grafo de referencia de T4 (default {DEFAULT_ESQUELETO_REF.relative_to(RAIZ)})")
    ap.add_argument("--out", default=None, help="RUTA.md (escribe también RUTA.json); sin --out no escribe nada")
    ap.add_argument("--solo", default=None, help="ids separados por coma (subconjunto; selftest/depuración)")
    return ap


def main(argv=None) -> int:
    args = parser().parse_args(argv)
    salida, codigo = correr(args)
    p, r, rk = salida["parametros"], salida["resumen"], salida["ranks_sellados"]
    print(f"regression_kg — {p['kg']} sha256 {p['kg_sha256']} gen {p['generacion']} catálogo v{p['catalogo_version']} política {p['politica_cuarentena']}")
    print(f"  ítems {r['items']}: resuelto {r['resuelto']} / persiste {r['persiste']} / no_aplicable {r['no_aplicable']}")
    print(f"  ranks sellados: consultas {rk['consultas_coinciden_sellado']}/{rk['consultas']}, objetivos {rk['objetivos_coinciden_sellado']}/{rk['objetivos']}")
    for it in salida["items"]:
        print(f"  {it['id']:9s} {it['estado']:13s} {it['detalle'][:150]}")
    reg = salida.get("regresion")
    if reg is not None:
        print(f"  fixture {reg['fixture']} sha256 {reg['fixture_sha256']} | estado_esperado sha256 {reg['estado_esperado_sha256']} | entrada {reg['entrada']} ({reg['parte']})")
        if reg.get("nota"):
            print("  " + reg["nota"])
        if "n_regresiones" in reg:
            print(f"  regresiones: {reg['n_regresiones']} (coinciden {reg['coinciden']}; NO VERIFICADAS {reg['no_verificadas']}; sin esperado {reg['sin_esperado']}; sin medido {reg['sin_medido']})")
            for x in reg["regresiones"]:
                print(f"    REGRESIÓN {x['item']}: esperado {x['esperado']} / medido {x['medido']}")
    if args.out:
        print(f"  escrito: {args.out} y {Path(args.out).with_suffix('.json')}")
    return codigo


if __name__ == "__main__":
    sys.exit(main())
