#!/usr/bin/env python3
"""upre_d1_suite.py — U-PRE-R2-DIAG, etapa D1: los seis ítems de la suite.

Mandato: docs/mandatos/UPRE_R2_diagnostico.md (firmado el 2026-09-29).
Solo lectura, USD 0, sin API y sin Neo4j. Escribe únicamente en --out-dir.

Qué hace:
  1. Verifica por sha256 cada entrada (grafos, fixture, suite, catálogos,
     tablas de E4, muestra de T5, salidas de E1 citadas, línea de base de E6).
  2. Corre los 46 ítems de scripts/regression_kg.py POR IMPORT, sin editar
     ninguna función, sobre KG-Reextraído-r1 (0226e947…) con los parámetros
     de su entrada en la fixture (catálogo v2, política flaggeada) y sobre
     KG-Tanda0-Desarrollo-r1 (eab2fdd0…) con los parámetros de E6 (catálogo
     v3, política flaggeada; reports/tanda0/regression_ens_desarrollo.json).
  3. Controles: r1 medido contra su entrada de la fixture; desarrollo medido
     contra la línea de base de E6 (estado y detalle, ítem por ítem).
  4. Para E4-a7, E4-a8, T2, T4, T5 y T7: partes del test, estado de cada
     parte en las dos generaciones, clase de la decisión 3 del mandato y las
     re-verificaciones de la decisión 4, con reglas declaradas en la salida
     ANTES de sus resultados (clave `reglas_declaradas`).
  5. Registra sin diagnóstico los otros cuatro ítems que cambian y la lista
     de los 36 que no cambian.

Reglas declaradas (se aplican igual sobre r1 y sobre desarrollo):
  R-T5  Una fila x de la muestra sellada de T5 está «presente por contenido»
        en un grafo si existe una arista `referencia` con properties.evidencia
        tal que (1) origen: su nodo fuente ancla en x.source_ancla (conjunto
        completo de provenances, regla de direccionamiento de la suite);
        (2) destino: su nodo destino ancla en x.target_ancla y
        properties.destino == x.destino; (3) tipo de destino: el tipo del
        nodo destino == x.target_type; (4) texto: los números de punto de
        properties.evidencia y de x.evidencia_verbatim (regex \\d+(\\.\\d+)*,
        normalizados, sin punto final) tienen intersección no vacía.
        «R-T5 sin tipo» = (1), (2) y (4).
  R-E4a8 La regla de t_e4_a8 (alias_resueltos en el id de catálogo resuelto y
        ausencia del propuesto y de sus aristas), leída sobre la tabla
        e4_propuestos.json que produjo el ensamblado del grafo bajo prueba,
        en lugar de la tabla fija de salida_r1.
  R-T4  Esqueleto de un catálogo = las aristas de relaciones de esqueleto que
        construye assemble.build_skeleton (grafo_v2/code/assemble.py:118)
        sobre ese catálogo, invocado por import vía
        ensamblar_corpus.inyectar_esqueleto_v3 sobre un grafo vacío.
  R-CAT Catálogo ampliado en memoria = esquema_v3_clases.json más los ids del
        bloque v3 del perfil (perfil_e1.perfil("v3_b54").labels_catalogo) que
        no están en el JSON; T7 y E4-a7 se re-corren con él (contrafáctico,
        no es un resultado de r2).
  SIM-H1 Simulación en memoria del resolvedor de remisiones con TIPOS_ORIGEN
        ampliado a Condicion, Potestad y Definicion, con las redirecciones del
        manifiesto de desarrollo (precedente y control cruzado:
        reports/u_audit_tipos_v3/p2_referencias_sim.py y su JSON). No es un
        resultado de r2.

Uso (desde la raíz del repo):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B reports/u_pre_r2/upre_d1_suite.py --out-dir reports/u_pre_r2
"""
from __future__ import annotations

import sys

sys.dont_write_bytecode = True

import argparse
import contextlib
import copy
import hashlib
import inspect
import json
import re
from collections import Counter, OrderedDict
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "scripts"))
import regression_kg as RK   # noqa: E402  la suite, importada sin editar

REX = RAIZ / "data" / "experiment" / "reextraccion_v2"
E1_EXTRACTOR = REX / "e1_extractor"

# --------------------------------------------------------------------------- #
# Entradas con sha256 esperado (si alguno difiere, la corrida se frena)       #
# --------------------------------------------------------------------------- #
ENTRADAS = OrderedDict([
    ("kg_r1", ("data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json",
               "0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a")),
    ("kg_desarrollo", ("data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo/r1/kg.json",
                       "eab2fdd01dec4dad026d596a793919e666920fab127d7efb14b5b00857ae64ef")),
    ("kg_refinado_esqueleto_referencia", ("data/experiment/grafo_v2/reensamblado_v3/kg.json",
                                          "26fac8b49f6c08c1aa364b47273d36958d831f240d4e6b4ee7700b6a0bff3571")),
    ("fixture", ("scripts/regression_kg_esperado.json",
                 "696f3f941e0d64c3a2def37159d45f7814b546f9d461f6727f43db3eda160f5e")),
    ("suite", ("scripts/regression_kg.py",
               "87a57b6d80d443a325a53bdf0ed83b06029812a1e7a9608f52c203831d2b4edb")),
    ("catalogo_v2", ("data/experiment/grafo_v2/esquema_v2_clases.json",
                     "2672af5216e095bee2a4888e18d85930d7b0149263b87763daacc5fd21814d4d")),
    ("catalogo_v3", ("data/experiment/esq_v3_miembros/esquema_v3_clases.json",
                     "dad88cc92afc53e922989cad84eb68b2ef142b66c221f2a566e7fb5da1bcfd36")),
    ("muestra30_T5", ("data/experiment/reextraccion_v2/corpus_v2/salida_r1/referencias_muestra30_inspeccionada_A2.json",
                      "4dbc2d306df867dedc4464c54b56bf6f7224ee6d820577ffe83141b6cbba8da4")),
    ("e4_propuestos_r1", ("data/experiment/reextraccion_v2/corpus_v2/salida_r1/e4_propuestos.json",
                          "ad8e2ef78fb2db73deb1caf5949b707270a6c14ea791c493a8449dfe67dc3a21")),
    ("e4_propuestos_desarrollo", ("data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo/r1/e4_propuestos.json",
                                  "1c664faef4bb1f50098681f815dad95ab7fd2312a8bba176755f28084bf33409")),
    ("linea_base_E6_desarrollo", ("reports/tanda0/regression_ens_desarrollo.json",
                                  "0745a9dc2ec80bfa0aed6483d9669f6b587b1ff243e211129274a9ba1547fcf9")),
    ("e1_finales_ext_desarrollo", ("data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida/ext/extracciones_finales_ext.jsonl",
                                   "d92c36b2ea8fe344f4dc4e1b7983397faf6cda58171c8e045fecb74f20fe7220")),
    ("manifiesto_ens_desarrollo", ("data/experiment/reextraccion_v2/manifiestos/tanda0_ens_desarrollo.json",
                                   "bfe7c7b0912c990996b802c785e565741468d5cef49e67ba4a80beca06c0468f")),
    ("sim_h1_u_audit", ("reports/u_audit_tipos_v3/p2_referencias_sim.json",
                        "0e044879764afb584bcada881ec2a0455040e23b9ef4d39a60748e4d8f3c4e0d")),
])
# Registrados con su sha (sin esperado fijo): se leen para evidencia.
REGISTRADOS = (
    "data/experiment/reextraccion_v2/corpus_v2/salida/ext/extracciones_finales_ext.jsonl",
    "data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo/r1/reporte_ensamblado_r1.json",
    "data/experiment/reextraccion_v2/corpus_v2/r1_referencias.py",
    "data/experiment/reextraccion_v2/corpus_v2/r1_tests.py",
    "data/experiment/reextraccion_v2/corpus_v2/r1_e4.py",
    "data/experiment/reextraccion_v2/corpus_v2/ensamblar_corpus.py",
    "data/experiment/reextraccion_v2/e1_extractor/perfil_e1.py",
    "data/experiment/reextraccion_v2/e2_reduce/e2_lib.py",
    "data/experiment/grafo_v2/code/assemble.py",
)
TOS_DESARROLLO = ("pro", "cla", "ric", "cap", "ext")
E0_TANDA0 = "data/experiment/reextraccion_v2/e0_chunking/salida_tanda0"
E0_ENM01 = "data/experiment/reextraccion_v2/e0_chunking/salida_enm01"

SEIS = ("E4-a7", "E4-a8", "T2", "T4", "T5", "T7")
CUATRO = ("BKL-0006", "BKL-0028", "BKL-0029", "RT-C5-3")
CLASES = OrderedDict([
    ("a", "regresión real"),
    ("b", "efecto de direccionamiento"),
    ("c", "efecto de diseño del perfil v3"),
    ("d", "no decidible con el material"),
])
CUMPLE_AMBOS = "cumple en las dos generaciones (sin clase)"
TIPOS_NUEVOS = ("Condicion", "Potestad", "Definicion")
CMD = "PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B reports/u_pre_r2/upre_d1_suite.py --out-dir reports/u_pre_r2"


# --------------------------------------------------------------------------- #
# Utilidades                                                                    #
# --------------------------------------------------------------------------- #
def sha256_path(p: Path) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def rel(obj):
    """Rutas absolutas del repo → relativas, recursivo (salida sin rutas de la máquina)."""
    raiz = str(RAIZ) + "/"
    if isinstance(obj, str):
        return obj.replace(raiz, "")
    if isinstance(obj, dict):
        return {k: rel(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [rel(v) for v in obj]
    return obj


def lineas(fn) -> str:
    """archivo:inicio-fin de una función, medido con inspect (no a mano)."""
    src, ini = inspect.getsourcelines(fn)
    return f"{Path(inspect.getsourcefile(fn)).resolve().relative_to(RAIZ)}:{ini}-{ini + len(src) - 1}"


RE_TOK = re.compile(r"\d+(?:\.\d+)*")


def tokens_punto(s) -> set:
    return {t.rstrip(".") for t in RE_TOK.findall(RK.norm(s))}


def puntos_ext(n: dict) -> list:
    return sorted(p for a, p in RK.anclas(n) if a.startswith(RK.EXT))


def leer_jsonl_por_chunk(ruta: Path) -> dict:
    out = {}
    with ruta.open(encoding="utf-8") as f:
        for linea in f:
            r = json.loads(linea)
            out[r["chunk_id"]] = r
    return out


@contextlib.contextmanager
def redirigido(plan):
    """(módulo, atributo, valor) aplicados en memoria y restaurados al salir
    (mismo patrón que ensamblar_tanda0.redirigido)."""
    originales = [(m, a, getattr(m, a)) for m, a, _ in plan]
    try:
        for m, a, v in plan:
            setattr(m, a, v)
        yield
    finally:
        for m, a, v in originales:
            setattr(m, a, v)


def verificar_entradas() -> OrderedDict:
    out = OrderedDict()
    malos = []
    for clave, (ruta, esperado) in ENTRADAS.items():
        medido = sha256_path(RAIZ / ruta)
        out[clave] = {"ruta": ruta, "sha256": medido, "sha256_esperado": esperado, "coincide": medido == esperado}
        if medido != esperado:
            malos.append(clave)
    for ruta in REGISTRADOS:
        out[ruta] = {"ruta": ruta, "sha256": sha256_path(RAIZ / ruta)}
    if malos:
        raise SystemExit(f"FRENO: sha256 distinto del esperado en {malos}")
    return out


# --------------------------------------------------------------------------- #
# Corridas de la suite                                                         #
# --------------------------------------------------------------------------- #
def contexto(kg_clave: str, cat_clave: str) -> RK.Contexto:
    G = RK.Grafo.desde_ruta(RAIZ / ENTRADAS[kg_clave][0])
    cat = RK.Catalogo.desde_ruta(RAIZ / ENTRADAS[cat_clave][0])
    return RK.Contexto(G, cat, 3, "flaggeada")


def correr_suite(ctx: RK.Contexto) -> list:
    return RK.ejecutar(ctx)


def estados(items: list) -> OrderedDict:
    return OrderedDict((it["id"], it["estado"]) for it in items)


# --------------------------------------------------------------------------- #
# T2                                                                           #
# --------------------------------------------------------------------------- #
def nodos_125(G: RK.Grafo) -> list:
    return [n for n in G.buscar(None, RK.EXT) if "125 %" in RK.texto(n) or "125%" in RK.texto(n)]


def analizar_t2(G_r1, G_dev, e2_lib, chunks_ext: dict) -> OrderedDict:
    fil = OrderedDict()
    for nombre, G in (("r1", G_r1), ("desarrollo", G_dev)):
        ns = nodos_125(G)
        fil[nombre] = {
            "n_nodos": len(ns),
            "puntos_distintos": sorted({p for n in ns for p in puntos_ext(n)}),
            "nodos": sorted(({"id": n["id"], "type": n["type"], "puntos_ext": puntos_ext(n)} for n in ns), key=lambda d: d["id"]),
            "nodos_con_mas_de_un_punto": sorted(n["id"] for n in ns if len(puntos_ext(n)) > 1),
        }
    # Fusión: por cada nodo de desarrollo con más de un punto, las entidades de
    # E1 (salida final que ensambla E2) con «125» en esos chunks y su slug.
    fin_dev = leer_jsonl_por_chunk(RAIZ / ENTRADAS["e1_finales_ext_desarrollo"][0])
    fin_r1 = leer_jsonl_por_chunk(RAIZ / REGISTRADOS[0])
    fusion = []
    for nid in fil["desarrollo"]["nodos_con_mas_de_un_punto"]:
        n = G_dev.by_id[nid]
        ents = []
        for p in puntos_ext(n):
            cid = f"ext::{p}"
            for e in ((fin_dev.get(cid) or {}).get("validacion") or {}).get("entidades", []):
                if "125" in json.dumps(e.get("properties") or {}, ensure_ascii=False):
                    slug = e2_lib.entity_slug_v3(e)
                    ents.append({"chunk_id": cid, "type": e["type"], "descripcion": (e.get("properties") or {}).get("descripcion"),
                                 "entity_slug_v3": slug, "id_del_nodo_termina_en_slug": nid.endswith(slug)})
        fusion.append({"nodo": nid, "puntos_ext": puntos_ext(n), "entidades_e1_con_125": ents,
                       "slugs_distintos": len({x["entity_slug_v3"] for x in ents}),
                       "descripciones_distintas": len({x["descripcion"] for x in ents})})
    # r1: las mismas unidades en la salida de E1 que ensambló la cadena r1.
    r1_mismas = []
    for f in fusion:
        for p in f["puntos_ext"]:
            cid = f"ext::{p}"
            for e in ((fin_r1.get(cid) or {}).get("validacion") or {}).get("entidades", []):
                if "125" in json.dumps(e.get("properties") or {}, ensure_ascii=False):
                    r1_mismas.append({"chunk_id": cid, "type": e["type"], "descripcion": (e.get("properties") or {}).get("descripcion"),
                                      "entity_slug_v3": e2_lib.entity_slug_v3(e)})
    # Ocurrencias de «125%» en el texto propio de E0 por punto (E0 idéntico en las dos generaciones).
    occ = OrderedDict()
    for p in fil["r1"]["puntos_distintos"]:
        t = (chunks_ext.get(f"ext::{p}") or {}).get("texto") or ""
        occ[p] = t.count("125%") + t.count("125 %")
    por_punto = OrderedDict()
    for nombre in ("r1", "desarrollo"):
        c = Counter(p for d in fil[nombre]["nodos"] for p in d["puntos_ext"])
        por_punto[nombre] = OrderedDict((p, c.get(p, 0)) for p in fil["r1"]["puntos_distintos"])
    return OrderedDict([
        ("medido", fil),
        ("fusion_en_desarrollo", fusion),
        ("r1_mismas_unidades_en_e1", r1_mismas),
        ("ocurrencias_125_en_E0_texto_propio", occ),
        ("nodos_125_por_punto", por_punto),
    ])


# --------------------------------------------------------------------------- #
# T4                                                                           #
# --------------------------------------------------------------------------- #
def esqueleto_de_catalogo(EC, ruta_catalogo: Path, relaciones: tuple) -> set:
    kg = {"nodes": [], "edges": []}
    EC.inyectar_esqueleto_v3(kg, ruta_catalogo)
    return {(e["source"], e["relation"], e["target"]) for e in kg["edges"] if e["relation"] in relaciones}


def triplas_esqueleto(G: RK.Grafo, relaciones: tuple) -> set:
    return {(e["source"], e["relation"], e["target"]) for e in G.E
            if e["relation"] in relaciones and e.get("rol_fuente") != "cuarentena_laudada"}


def analizar_t4(G_r1, G_dev, ref: RK.Grafo, relaciones: tuple, EC, cat2: RK.Catalogo, cat3: RK.Catalogo) -> OrderedDict:
    sk2 = esqueleto_de_catalogo(EC, RAIZ / ENTRADAS["catalogo_v2"][0], relaciones)
    sk3 = esqueleto_de_catalogo(EC, RAIZ / ENTRADAS["catalogo_v3"][0], relaciones)
    t_ref = triplas_esqueleto(ref, relaciones)
    t_r1 = triplas_esqueleto(G_r1, relaciones)
    t_dev = triplas_esqueleto(G_dev, relaciones)
    extra = sorted(t_dev - t_ref)
    return OrderedDict([
        ("relaciones_esqueleto", list(relaciones)),
        ("aristas", {"referencia_kg_refinado": len(t_ref), "r1": len(t_r1), "desarrollo": len(t_dev),
                     "build_skeleton_catalogo_v2": len(sk2), "build_skeleton_catalogo_v3": len(sk3)}),
        ("r1_igual_a_build_skeleton_v2", t_r1 == sk2),
        ("desarrollo_igual_a_build_skeleton_v3", t_dev == sk3),
        ("referencia_igual_a_build_skeleton_v2", t_ref == sk2),
        ("referencia_contenida_en_desarrollo", t_ref <= t_dev),
        ("extra_desarrollo_menos_referencia", {
            "n": len(extra),
            "por_relacion": dict(sorted(Counter(r for _, r, _ in extra).items())),
            "con_algun_extremo_fuera_del_catalogo_v2": sum(1 for s, _, t in extra if s not in cat2.ids or t not in cat2.ids),
            "con_ambos_extremos_en_el_catalogo_v3": sum(1 for s, _, t in extra if s in cat3.ids and t in cat3.ids),
            "triplas": [list(x) for x in extra],
        }),
    ])


# --------------------------------------------------------------------------- #
# T5                                                                           #
# --------------------------------------------------------------------------- #
def regla_rt5(G: RK.Grafo, x: dict, con_tipo: bool) -> list:
    sa, sp = RK._ancla_desde_codigo(x["source_ancla"])
    ta, tp = RK._ancla_desde_codigo(x["target_ancla"])
    tok_x = tokens_punto(x["evidencia_verbatim"])
    out = []
    for e in G.E:
        P = e.get("properties") or {}
        if e["relation"] != "referencia" or P.get("evidencia") is None:
            continue
        if not RK.con_ancla(G.by_id.get(e["source"], {}), sa, sp):
            continue
        if not RK.con_ancla(G.by_id.get(e["target"], {}), ta, tp) or P.get("destino") != x["destino"]:
            continue
        if con_tipo and G.tipo(e["target"]) != x["target_type"]:
            continue
        if not (tokens_punto(P["evidencia"]) & tok_x):
            continue
        out.append(e)
    return out


def verbatim_ok(G: RK.Grafo, x: dict) -> tuple:
    """La comprobación de t_t5 para una fila (regression_kg.py, t_t5), recomputada por fila."""
    refs = [e for e in G.E if e["relation"] == "referencia" and (e.get("properties") or {}).get("evidencia") is not None]
    sa, sp = RK._ancla_desde_codigo(x["source_ancla"])
    ta, tp = RK._ancla_desde_codigo(x["target_ancla"])
    cands = [e for e in refs if RK.con_ancla(G.by_id.get(e["source"], {}), sa, sp) and RK.con_ancla(G.by_id.get(e["target"], {}), ta, tp)]
    return any(e["properties"]["evidencia"] == x["evidencia_verbatim"] for e in cands), bool(cands)


def menciones_en_origen(G: RK.Grafo, x: dict, REF) -> list:
    """Nodos de contenido anclados en el origen cuyo texto (el que lee el
    resolvedor: r1_referencias._texto) tiene una mención que
    r1_referencias.detectar_menciones resuelve al destino de la fila."""
    sa, sp = RK._ancla_desde_codigo(x["source_ancla"])
    dto, dp = x["destino"].split("::", 1)
    out = []
    for n in G.buscar(None, sa, sp):
        if n["type"] in ("Sujeto", "TextoOrdenado", "Comunicacion"):
            continue
        to_o = (n.get("provenance") or {}).get("to") or x["source_ancla"].split("::")[0]
        men = REF.detectar_menciones(REF._texto(n), to_o)
        ok = [m for m in men if m["to_destino"] == dto and (dp in m["puntos"] or dp.lstrip("S") in m["secciones"])]
        if ok:
            out.append({"id": n["id"], "type": n["type"], "tipo_en_TIPOS_ORIGEN": n["type"] in REF.TIPOS_ORIGEN,
                        "punto_provenance_primaria": (n.get("provenance") or {}).get("punto")})
    return sorted(out, key=lambda d: d["id"])


def _resuelve_al_destino(texto: str, to_o: str, x: dict, REF) -> bool:
    dto, dp = x["destino"].split("::", 1)
    return any(m["to_destino"] == dto and (dp in m["puntos"] or dp.lstrip("S") in m["secciones"])
               for m in REF.detectar_menciones(texto or "", to_o))


def destino_en_e0(chunks: dict, x: dict, REF) -> dict:
    """¿El texto de E0 del chunk de origen tiene una mención que
    r1_referencias.detectar_menciones (con su expansión de rangos) resuelve
    al destino de la fila? Texto propio y texto heredado por separado (E0
    idéntico en las dos generaciones para los cinco TOs de desarrollo)."""
    c = chunks.get(x["source_ancla"]) or {}
    to_o = x["source_ancla"].split("::")[0]
    propio = _resuelve_al_destino(c.get("texto"), to_o, x, REF)
    heredado = any(_resuelve_al_destino(h.get("texto"), to_o, x, REF) for h in c.get("herencia") or [])
    return {"chunk_en_E0": bool(c), "en_texto_propio": propio, "en_texto_heredado": heredado}


def arista_origen_con_destino(G: RK.Grafo, x: dict) -> bool:
    """Evidencia (no es regla de clase): alguna arista referencia con fuente
    anclada en el origen y properties.destino == x.destino, sin condición
    sobre el ancla del nodo destino."""
    sa, sp = RK._ancla_desde_codigo(x["source_ancla"])
    return any(e["relation"] == "referencia" and (e.get("properties") or {}).get("destino") == x["destino"]
               and RK.con_ancla(G.by_id.get(e["source"], {}), sa, sp) for e in G.E)


def simular_h1(kg_dev: dict, C, REF) -> tuple:
    """Re-detección en memoria con TIPOS_ORIGEN original (control) y ampliado a
    los tres tipos nuevos (p2_referencias_sim.py, mismas redirecciones)."""
    man = json.loads((RAIZ / ENTRADAS["manifiesto_ens_desarrollo"][0]).read_text(encoding="utf-8"))
    rep = json.loads((RAIZ / REGISTRADOS[1]).read_text(encoding="utf-8"))
    e0 = Path(rep["manifiesto"]["e0_salida"])
    e0 = e0 if e0.is_absolute() else RAIZ / e0
    plan = [(C, "TOS_ORDEN", tuple(man["orden_corrida"])), (C, "E0_ENM01", e0),
            (REF, "INVENTARIO_TOS", {t["id"]: tuple(t["nombres_remision"]) for t in sorted(man["tos"], key=lambda t: t["id"])})]
    existentes = {(e["source"], e["relation"], e["target"]) for e in kg_dev["edges"] if e.get("rol_fuente") == "referencia_cruzada"}
    base = {"nodes": kg_dev["nodes"], "edges": [e for e in kg_dev["edges"] if e.get("rol_fuente") != "referencia_cruzada"]}
    orig = tuple(REF.TIPOS_ORIGEN)

    def correr(tipos):
        with redirigido(plan + [(REF, "TIPOS_ORIGEN", tipos)]):
            kg = copy.deepcopy(base)
            REF.detectar_y_resolver(kg)
        return kg

    kg_ctrl = correr(orig)
    n_ctrl = {(e["source"], e["relation"], e["target"]) for e in kg_ctrl["edges"] if e.get("rol_fuente") == "referencia_cruzada"}
    kg_ext = correr(orig + TIPOS_NUEVOS)
    n_ext = {(e["source"], e["relation"], e["target"]) for e in kg_ext["edges"] if e.get("rol_fuente") == "referencia_cruzada"}
    previo = json.loads((RAIZ / ENTRADAS["sim_h1_u_audit"][0]).read_text(encoding="utf-8"))
    control = OrderedDict([
        ("tipos_origen_original", list(orig)),
        ("aristas_existentes", len(existentes)),
        ("re_detectadas_con_tipos_originales", len(n_ctrl)),
        ("identicas", n_ctrl == existentes),
        ("adicionales_con_tres_tipos_nuevos", len(n_ext - n_ctrl)),
        ("perdidas_con_tres_tipos_nuevos", len(n_ctrl - n_ext)),
        ("adicionales_segun_p2_referencias_sim", previo["con_9_tipos"]["aristas_referencia_adicionales"]),
        ("coincide_con_p2_referencias_sim", len(n_ext - n_ctrl) == previo["con_9_tipos"]["aristas_referencia_adicionales"]),
    ])
    return RK.Grafo(kg_ext, "simulacion_h1_en_memoria", ""), control


def analizar_t5(G_r1, G_dev, REF, C, chunks_por_to: dict, kg_dev_dict: dict) -> OrderedDict:
    muestra = json.loads((RAIZ / ENTRADAS["muestra30_T5"][0]).read_text(encoding="utf-8"))
    G_sim, control_sim = simular_h1(kg_dev_dict, C, REF)
    filas = []
    for x in muestra:
        fila = OrderedDict([("n", x["n"]), ("source_ancla", x["source_ancla"]), ("target_ancla", x["target_ancla"]),
                            ("destino", x["destino"]), ("target_type_r1", x["target_type"])])
        for nombre, G in (("r1", G_r1), ("desarrollo", G_dev)):
            vb, cand = verbatim_ok(G, x)
            completa = regla_rt5(G, x, True)
            sin_tipo = regla_rt5(G, x, False)
            fila[nombre] = {"verbatim": vb, "arista_origen_destino_presente": cand,
                            "rt5_completa": bool(completa), "rt5_sin_tipo": bool(sin_tipo),
                            "tipos_destino_rt5_sin_tipo": sorted({G.tipo(e["target"]) for e in sin_tipo})}
        d = fila["desarrollo"]
        if d["verbatim"]:
            fila["clase"], fila["motivo"] = None, "verbatim presente en las dos generaciones"
        elif d["rt5_completa"]:
            fila["clase"], fila["motivo"] = "b", "presente por contenido (R-T5) con otra evidencia verbatim"
        elif d["rt5_sin_tipo"]:
            fila["clase"], fila["motivo"] = "b", "presente por contenido (R-T5 sin tipo): el nodo destino tiene otro tipo"
        else:
            men = menciones_en_origen(G_dev, x, REF)
            e0 = destino_en_e0(chunks_por_to[x["source_ancla"].split("::")[0]], x, REF)
            sim_completa = bool(regla_rt5(G_sim, x, True))
            sim_sin_tipo = bool(regla_rt5(G_sim, x, False))
            fila["diagnostico_ausencia"] = {"nodos_origen_con_mencion_al_destino": men, "destino_en_E0": e0,
                                            "sim_h1_rt5_completa": sim_completa, "sim_h1_rt5_sin_tipo": sim_sin_tipo,
                                            "sim_h1_arista_origen_con_destino": arista_origen_con_destino(G_sim, x),
                                            "desarrollo_arista_origen_con_destino": arista_origen_con_destino(G_dev, x)}
            if men and all(not m["tipo_en_TIPOS_ORIGEN"] for m in men):
                fila["clase"] = "a"
                fila["motivo"] = ("arista ausente; la mención al destino está en un nodo de tipo "
                                  + "/".join(sorted({m["type"] for m in men}))
                                  + ", excluido como origen por TIPOS_ORIGEN (H1)")
                fila["causa"] = "H1"
            elif not men:
                fila["clase"] = "a"
                fila["motivo"] = ("arista ausente; ningún nodo de contenido anclado en el origen tiene la mención en el texto que lee el "
                                  "resolvedor; E0 la tiene en el texto " + ("propio" if e0["en_texto_propio"] else "heredado" if e0["en_texto_heredado"] else "— NO ENCONTRADA"))
                fila["causa"] = "mencion_fuera_del_texto_del_resolvedor"
            else:
                fila["clase"] = "d"
                fila["motivo"] = "arista ausente con un nodo de TIPOS_ORIGEN que tiene la mención: no decidible con esta regla"
                fila["causa"] = "no_decidible"
        filas.append(fila)
    c_clase = Counter((f["clase"] or "verbatim") for f in filas)
    c_causa = Counter(f.get("causa") for f in filas if f.get("causa"))
    resumen = OrderedDict([
        ("n_muestra", len(filas)),
        ("r1", {"verbatim": sum(f["r1"]["verbatim"] for f in filas), "rt5_completa": sum(f["r1"]["rt5_completa"] for f in filas),
                "rt5_sin_tipo": sum(f["r1"]["rt5_sin_tipo"] for f in filas)}),
        ("desarrollo", {"verbatim": sum(f["desarrollo"]["verbatim"] for f in filas),
                        "arista_origen_destino_presente": sum(f["desarrollo"]["arista_origen_destino_presente"] for f in filas),
                        "rt5_completa": sum(f["desarrollo"]["rt5_completa"] for f in filas),
                        "rt5_sin_tipo": sum(f["desarrollo"]["rt5_sin_tipo"] for f in filas)}),
        ("por_clase", dict(sorted(c_clase.items()))),
        ("ausentes_por_causa", dict(sorted(c_causa.items()))),
        ("ausentes_recuperadas_en_sim_h1", {
            "rt5_completa": sum(1 for f in filas if (f.get("diagnostico_ausencia") or {}).get("sim_h1_rt5_completa")),
            "rt5_sin_tipo": sum(1 for f in filas if (f.get("diagnostico_ausencia") or {}).get("sim_h1_rt5_sin_tipo")),
            "arista_origen_con_destino": sum(1 for f in filas if (f.get("diagnostico_ausencia") or {}).get("sim_h1_arista_origen_con_destino"))}),
    ])
    return OrderedDict([("control_sim_h1", control_sim), ("resumen", resumen), ("filas", filas)])


# --------------------------------------------------------------------------- #
# T7 y E4-a7                                                                   #
# --------------------------------------------------------------------------- #
def bloque_perfil_v3() -> OrderedDict:
    if str(E1_EXTRACTOR) not in sys.path:
        sys.path.insert(0, str(E1_EXTRACTOR))
    import perfil_e1   # noqa: E402  e1_extractor/perfil_e1.py (import, sin editar)
    p = perfil_e1.perfil("v3_b54")
    labels = p.labels_catalogo
    ids = set(labels)
    if ids != set(p.esquema.sujetos_catalogo_set):
        raise SystemExit("FRENO: labels_catalogo y sujetos_catalogo_set del perfil v3_b54 no coinciden")
    return OrderedDict(sorted(labels.items()))


def catalogo_ampliado(cat3: RK.Catalogo, bloque: dict) -> tuple:
    faltan = sorted(set(bloque) - cat3.ids)
    data = copy.deepcopy(cat3.data)
    for i in faltan:
        ent = {"id": i, "label": bloque[i]["label"], "nivel": bloque[i]["nivel"]}
        (data.setdefault("roles", []) if bloque[i]["nivel"] == "rol" else data.setdefault("clases", [])).append(
            dict(ent, miembros=[]) if bloque[i]["nivel"] == "rol" else ent)
    return RK.Catalogo(data, "catálogo JSON v3 ∪ ids del bloque v3 del perfil (en memoria)", ""), faltan


def analizar_t7_e4a7(ctx_dev: RK.Contexto, item_t7: dict, item_a7: dict) -> OrderedDict:
    bloque = bloque_perfil_v3()
    cat3 = ctx_dev.cat
    cat_amp, seis = catalogo_ampliado(cat3, bloque)
    fuera = item_t7["valores"]["sujetos_fuera_catalogo_no_propuestos"]
    t7_amp = RK.t7_cuarentena(ctx_dev.grafo, cat_amp.ids, "flaggeada")
    ctx_amp = RK.Contexto(ctx_dev.grafo, cat_amp, 3, "flaggeada")
    a7_amp = RK.t_e4_a7(ctx_amp)
    G = ctx_dev.grafo
    detalle_fuera = []
    for i in fuera:
        n = G.by_id[i]
        detalle_fuera.append({"id": i, "en_bloque_v3_del_perfil": i in bloque, "en_catalogo_json_v3": i in cat3.ids,
                              "n_provenances": len(RK.provenances(n)),
                              "tos": sorted({(p.get("to") or "") for p in RK.provenances(n)})})
    return OrderedDict([
        ("ids_bloque_perfil_v3", len(bloque)),
        ("ids_catalogo_json_v3", len(cat3.ids)),
        ("en_bloque_y_no_en_json", seis),
        ("en_json_y_no_en_bloque", sorted(cat3.ids - set(bloque))),
        ("fuera_de_catalogo_no_propuestos_desarrollo", detalle_fuera),
        ("fuera_contenidos_en_bloque_menos_json", set(fuera) <= set(seis)),
        ("contrafactico_catalogo_ampliado", {
            "T7_pass": t7_amp["pass"], "T7_malos": len(t7_amp["malos"]),
            "T7_fuera": len(t7_amp["sujetos_fuera_catalogo_no_propuestos"]),
            "E4-a7_estado": a7_amp["estado"], "E4-a7_detalle": a7_amp["detalle"]}),
    ])


def partes_t7(item: dict) -> OrderedDict:
    v = item["valores"]
    motivos = Counter()
    for _, m in v["malos"]:
        if m.startswith("padre_sugerido a"):
            motivos["padre_sugerido_fuera_de_catalogo"] += 1
        elif m.startswith("subclase_de"):
            motivos["subclase_de_desde_propuesto"] += 1
        else:
            motivos[m] += 1
    return OrderedDict([
        ("P1 propuestos con cuarentena=true (normalizada)", motivos.get("sin cuarentena=true", 0) == 0),
        ("P2 ningún propuesto con id de catálogo", motivos.get("propuesto con id de catálogo", 0) == 0),
        ("P3 toda padre_sugerido apunta a un id del catálogo", motivos.get("padre_sugerido_fuera_de_catalogo", 0) == 0),
        ("P4 ninguna subclase_de desde un propuesto (flaggeada)", motivos.get("subclase_de_desde_propuesto", 0) == 0),
        ("P5 ningún Sujeto fuera del catálogo que no sea propuesto", len(v["sujetos_fuera_catalogo_no_propuestos"]) == 0),
    ])


def partes_e4a7(item: dict) -> OrderedDict:
    det = item["detalle"]
    num = {k: int(v) for k, v in re.findall(r"(\w+)=(\d+)", det)}
    return OrderedDict([
        ("P1 propuestos con cuarentena=true (normalizada)", num.get("sin_cuarentena_true", 0) == 0),
        ("P2 ningún propuesto con id de catálogo", num.get("con_id_de_catalogo", 0) == 0),
        ("P3 ningún Sujeto fuera del catálogo que no sea propuesto", num.get("sujetos_fuera_catalogo_no_propuestos", 0) == 0),
    ])


# --------------------------------------------------------------------------- #
# E4-a8                                                                        #
# --------------------------------------------------------------------------- #
def regla_e4a8(G: RK.Grafo, tabla: list) -> OrderedDict:
    remap = [(f["id_propuesto"], f["resuelto_a"], f["label"]) for f in tabla if f.get("estado") == "resuelto"]
    port = {n["id"]: RK.prop(n, "alias_resueltos") for n in G.N if n.get("type") == "Sujeto" and RK.prop(n, "alias_resueltos")}
    filas = []
    for p, rid, label in remap:
        filas.append({"id_propuesto": p, "resuelto_a": rid, "label": label,
                      "alias_en_id_de_catalogo": label in (port.get(rid) or []),
                      "propuesto_ausente_sin_aristas": p not in G.by_id and not G.salientes(p) and not G.entrantes(p)})
    return OrderedDict([("n_resueltos_en_la_tabla", len(remap)),
                        ("alias_en_id_de_catalogo", sum(f["alias_en_id_de_catalogo"] for f in filas)),
                        ("propuesto_ausente_sin_aristas", sum(f["propuesto_ausente_sin_aristas"] for f in filas)),
                        ("filas", filas)])


def analizar_e4a8(G_r1, G_dev) -> OrderedDict:
    t_r1 = json.loads((RAIZ / ENTRADAS["e4_propuestos_r1"][0]).read_text(encoding="utf-8"))
    t_dev = json.loads((RAIZ / ENTRADAS["e4_propuestos_desarrollo"][0]).read_text(encoding="utf-8"))
    ids_r1 = sorted({f["resuelto_a"] for f in t_r1 if f.get("estado") == "resuelto"})
    presencia = []
    for i in ids_r1:
        n = G_dev.by_id.get(i)
        provs = RK.provenances(n) if n else []
        presencia.append({"id": i, "presente_en_desarrollo": n is not None,
                          "provenances_de_extraccion": sum(1 for p in provs if p.get("rol_documental") != "esqueleto"),
                          "alias_resueltos": RK.prop(n, "alias_resueltos") if n else None,
                          "label_resuelto_en_r1_aparece_en_tabla_de_desarrollo": any(
                              f.get("resuelto_a") == i or RK.norm(f.get("label")) in {RK.norm(g["label"]) for g in t_r1 if g.get("resuelto_a") == i}
                              for f in t_dev)})
    return OrderedDict([
        ("tablas", {"r1": {"filas": len(t_r1), "por_estado": dict(sorted(Counter(f.get("estado") for f in t_r1).items()))},
                    "desarrollo": {"filas": len(t_dev), "por_estado": dict(sorted(Counter(f.get("estado") for f in t_dev).items()))}}),
        ("control_tabla_r1_sobre_r1", regla_e4a8(G_r1, t_r1)),
        ("control_tabla_r1_sobre_desarrollo", regla_e4a8(G_dev, t_r1)),
        ("R-E4a8_r1_con_su_tabla", regla_e4a8(G_r1, t_r1)),
        ("R-E4a8_desarrollo_con_su_tabla", regla_e4a8(G_dev, t_dev)),
        ("ids_resueltos_en_r1_en_el_grafo_de_desarrollo", presencia),
    ])


# --------------------------------------------------------------------------- #
# Propuestas (rotuladas PROPUESTA: la entrada de r2 la sella la autora)        #
# --------------------------------------------------------------------------- #
def propuestas(an: dict) -> OrderedDict:
    t5 = an["T5"]["resumen"]
    t4 = an["T4"]
    return OrderedDict([
        ("T2", OrderedDict([
            ("recomendada", "A"),
            ("A", "esperado r2 = persiste, como regresión conocida con causa documentada (fusión por descripción idéntica en E2). "
                  "r2 no toca el prefijo de E1 ni entity_slug_v3: las dos unidades salen de la caché con la misma descripción y se funden igual."),
            ("B", "esperado r2 = resuelto solo si la autora decide, fuera de los candidatos del §1, que la clave de fusión de "
                  "Restriccion/Obligacion/Excepcion no una descripciones idénticas de puntos distintos (se relaciona con la "
                  "decisión abierta de H2 del §4); cambia ids y exige actualizar la fixture."),
        ])),
        ("T4", OrderedDict([
            ("recomendada", "A"),
            ("A", "re-direccionar T4 en una unidad de la suite: comparar el esqueleto del grafo con el que build_skeleton construye "
                  f"desde el catálogo pasado por --catalogo (R-T4); con eso desarrollo da {t4['aristas']['desarrollo']} = "
                  f"{t4['aristas']['build_skeleton_catalogo_v3']} y r1 {t4['aristas']['r1']} = {t4['aristas']['build_skeleton_catalogo_v2']}; "
                  "esperado r2 = resuelto. Absorbe además el cambio de esqueleto si entra el ítem de la §1.6 que completa el catálogo JSON."),
            ("B", "sin cambio de la suite: declarar T4 no comparable entre generaciones (el 82 es el esqueleto del catálogo v2) y "
                  "sellar esperado r2 = persiste, con el detalle faltan 0 / 0 como condición de lectura."),
            ("C", "sin cambio de código: sellar en la entrada de r2 un --esqueleto-referencia de generación 3 construido con el "
                  "catálogo que use r2; exige re-sellar esa referencia si el catálogo JSON cambia (§1.6)."),
        ])),
        ("T5", OrderedDict([
            ("recomendada", "A"),
            ("A", "re-direccionar T5 en una unidad de la suite por contenido (R-T5) sobre la misma muestra sellada; esperado r2 = "
                  f"persiste: en desarrollo faltan {t5['por_clase'].get('a', 0)} de {t5['n_muestra']} "
                  f"({t5['ausentes_por_causa'].get('H1', 0)} por H1 y {t5['ausentes_por_causa'].get('mencion_fuera_del_texto_del_resolvedor', 0)} "
                  "cuya mención no llegó al texto que lee el resolvedor, que r2 no cambia porque no toca E1). Si H1 entra a r2, la "
                  f"simulación en memoria recupera {t5['ausentes_recuperadas_en_sim_h1']['rt5_completa']} de las ausentes con R-T5 "
                  f"({t5['ausentes_recuperadas_en_sim_h1']['rt5_sin_tipo']} sin tipo) y T5 sigue en persiste; pasaría a resuelto solo si "
                  "las ausencias de E1 se resuelven en una release que toque el prefijo."),
            ("B", "declarar T5 no comparable entre generaciones (la muestra y su evidencia verbatim son de r1) y sellar esperado "
                  "r2 = persiste; reemplazarla por una muestra sobre r2 con direccionamiento (chunk_id, relación, tipo de destino), "
                  "como anticipa reports/tanda0/obs12_lectura/decision_tests.txt."),
            ("nota", "la fixture guarda solo el estado del ítem: con cualquier opción, un «persiste» esperado no detecta que las ausencias "
                     "crezcan; registrar el conteo como criterio exige un cambio de la suite."),
        ])),
        ("T7", OrderedDict([
            ("recomendada", "A"),
            ("A", "si entra a r2 el ítem de la §1.6 que completa esquema_v3_clases.json con los ids del bloque v3: esperado r2 = "
                  "resuelto (verificado en memoria con R-CAT sobre desarrollo)."),
            ("B", "si no entra: esperado r2 = persiste, con los ids fuera de catálogo documentados (misma causa que el FAIL "
                  "conocido de S19)."),
        ])),
        ("E4-a7", OrderedDict([
            ("recomendada", "A"),
            ("A", "igual que T7: resuelto si se completa el catálogo JSON (verificado con R-CAT); P3 de E4-a7 es la P5 de T7."),
            ("B", "persiste si no se completa."),
        ])),
        ("E4-a8", OrderedDict([
            ("recomendada", "A"),
            ("A", "re-direccionar E4-a8 en una unidad de la suite para que lea la tabla e4_propuestos.json del ensamblado bajo "
                  "prueba (R-E4a8); esperado r2 = resuelto si la tabla de r2 tiene filas resueltas, no_aplicable si no tiene."),
            ("B", "sin cambio de la suite: declarar E4-a8 no comparable (lee un artefacto de r1) y sellar esperado r2 = persiste."),
        ])),
    ])


# --------------------------------------------------------------------------- #
# Armado de la salida                                                          #
# --------------------------------------------------------------------------- #
def item_por_id(items: list) -> dict:
    return {it["id"]: it for it in items}


def resumen_item(it: dict) -> OrderedDict:
    out = OrderedDict([("estado", it["estado"]), ("detalle", it["detalle"])])
    for k in ("subchecks", "valores"):
        if it.get(k) is not None:
            out[k] = it[k]
    return out


def construir() -> OrderedDict:
    entradas = verificar_entradas()
    fixture = json.loads((RAIZ / ENTRADAS["fixture"][0]).read_text(encoding="utf-8"))
    ent_r1 = fixture["estado_esperado"]["KG-Reextraido-r1"]
    esp_r1 = OrderedDict((k, (v.get("estado") if isinstance(v, dict) else v)) for k, v in ent_r1["items"].items())

    ctx_r1 = contexto("kg_r1", "catalogo_v2")
    ctx_dev = contexto("kg_desarrollo", "catalogo_v3")
    params_ok = (ent_r1["generacion"] == 3 and ent_r1["politica_cuarentena"] == "flaggeada"
                 and ent_r1["catalogo_sha256"] == ctx_r1.cat.sha256)
    if not params_ok:
        raise SystemExit("FRENO: parámetros de la corrida de r1 distintos de su entrada en la fixture")
    items_r1 = correr_suite(ctx_r1)
    items_dev = correr_suite(ctx_dev)
    I1, ID = item_por_id(items_r1), item_por_id(items_dev)
    reg_r1 = RK.computar_regresion(items_r1, ent_r1)

    e6 = json.loads((RAIZ / ENTRADAS["linea_base_E6_desarrollo"][0]).read_text(encoding="utf-8"))
    e6_items = item_por_id(e6["items"])
    control_e6 = OrderedDict([
        ("estado_igual", sum(1 for i in ID if e6_items[i]["estado"] == ID[i]["estado"])),
        ("detalle_igual", sum(1 for i in ID if e6_items[i]["detalle"] == ID[i]["detalle"])),
        ("items", len(ID)),
        ("parametros_E6", rel({k: e6["parametros"][k] for k in ("kg_sha256", "catalogo_sha256", "politica_cuarentena", "generacion")})),
    ])

    trans = Counter(f"{esp_r1[i]} → {ID[i]['estado']}" for i in esp_r1)
    cambian = sorted(i for i in esp_r1 if esp_r1[i] != ID[i]["estado"])
    no_cambian = sorted(i for i in esp_r1 if esp_r1[i] == ID[i]["estado"])

    # Módulos de la cadena r1 (ya en sys.path por ctx.e4)
    e4 = ctx_dev.e4
    import r1_referencias as REF   # noqa: E402
    import r1_comun as C           # noqa: E402
    import ensamblar_corpus as EC  # noqa: E402

    chunks_por_to = {}
    e0_identico = OrderedDict()
    for to in TOS_DESARROLLO:
        a, b = RAIZ / E0_TANDA0 / f"chunks_{to}.json", RAIZ / E0_ENM01 / f"chunks_{to}.json"
        e0_identico[to] = a.read_bytes() == b.read_bytes()
        chunks_por_to[to] = {c["id"]: c for c in json.loads(a.read_text(encoding="utf-8"))}

    kg_dev_dict = json.loads((RAIZ / ENTRADAS["kg_desarrollo"][0]).read_text(encoding="utf-8"))
    an = OrderedDict()
    an["T2"] = analizar_t2(ctx_r1.grafo, ctx_dev.grafo, e4["e2_lib"], chunks_por_to["ext"])
    an["T4"] = analizar_t4(ctx_r1.grafo, ctx_dev.grafo, ctx_dev.esqueleto_ref, ctx_dev.relaciones_esqueleto, EC, ctx_r1.cat, ctx_dev.cat)
    an["T5"] = analizar_t5(ctx_r1.grafo, ctx_dev.grafo, REF, C, chunks_por_to, kg_dev_dict)
    an["T7_E4-a7"] = analizar_t7_e4a7(ctx_dev, ID["T7"], ID["E4-a7"])
    an["E4-a8"] = analizar_e4a8(ctx_r1.grafo, ctx_dev.grafo)

    seis = OrderedDict()
    # --- T2
    t2 = an["T2"]["medido"]
    seis["T2"] = OrderedDict([
        ("verifica", [lineas(RK.t_t2), "data/experiment/reextraccion_v2/corpus_v2/ensamblar_corpus.py:251-265 (origen)"]),
        ("estado", {"r1_fixture": esp_r1["T2"], "r1": I1["T2"]["estado"], "desarrollo": ID["T2"]["estado"]}),
        ("partes", [
            {"parte": "P1 al menos 5 nodos de ext con «125 %»", "r1": t2["r1"]["n_nodos"], "desarrollo": t2["desarrollo"]["n_nodos"],
             "clase": "a", "motivo": "dos puntos (ext::7.5.3 y ext::7.8.5.1) quedan en un solo nodo: la estructura separada que el test protege falta en desarrollo"},
            {"parte": "P2 al menos 4 puntos distintos", "r1": len(t2["r1"]["puntos_distintos"]), "desarrollo": len(t2["desarrollo"]["puntos_distintos"]),
             "clase": None, "motivo": CUMPLE_AMBOS},
        ]),
    ])
    # --- T4
    t4v1, t4vd = I1["T4"]["valores"], ID["T4"]["valores"]
    seis["T4"] = OrderedDict([
        ("verifica", [lineas(RK.t4_paridad), lineas(RK.t_t4), "data/experiment/reextraccion_v2/corpus_v2/r1_tests.py:30-42 (origen)"]),
        ("estado", {"r1_fixture": esp_r1["T4"], "r1": I1["T4"]["estado"], "desarrollo": ID["T4"]["estado"]}),
        ("partes", [
            {"parte": "P1 los nodos de esqueleto de la referencia están", "r1": len(t4v1["faltan_nodos"]) == 0, "desarrollo": len(t4vd["faltan_nodos"]) == 0,
             "clase": None, "motivo": CUMPLE_AMBOS},
            {"parte": "P2 las triplas de esqueleto de la referencia están", "r1": len(t4v1["faltan_triplas"]) == 0, "desarrollo": len(t4vd["faltan_triplas"]) == 0,
             "clase": None, "motivo": CUMPLE_AMBOS},
            {"parte": "P3 cantidad de aristas de esqueleto igual a la de la referencia",
             "r1": f"{t4v1['aristas_esqueleto_en_grafo']} = {t4v1['aristas_esqueleto_referencia']}",
             "desarrollo": f"{t4vd['aristas_esqueleto_en_grafo']} ≠ {t4vd['aristas_esqueleto_referencia']}",
             "clase": "c", "motivo": "el esqueleto de desarrollo es exactamente el que build_skeleton construye desde el catálogo v3 (R-T4); las aristas de más tienen algún extremo fuera del catálogo v2"},
        ]),
    ])
    # --- T5
    t5r = an["T5"]["resumen"]
    seis["T5"] = OrderedDict([
        ("verifica", [lineas(RK.t_t5), "data/experiment/reextraccion_v2/corpus_v2/r1_tests.py:44-54 (origen)"]),
        ("estado", {"r1_fixture": esp_r1["T5"], "r1": I1["T5"]["estado"], "desarrollo": ID["T5"]["estado"]}),
        ("partes", [
            {"parte": "P1…P30 una parte por fila de la muestra sellada", "r1": f"verbatim {t5r['r1']['verbatim']}/30",
             "desarrollo": f"verbatim {t5r['desarrollo']['verbatim']}/30", "clase": "por fila",
             "motivo": "por_clase " + json.dumps(t5r["por_clase"], ensure_ascii=False, sort_keys=True)
                       + "; ausentes_por_causa " + json.dumps(t5r["ausentes_por_causa"], ensure_ascii=False, sort_keys=True)},
        ]),
    ])
    # --- T7
    p7_r1, p7_dev = partes_t7(I1["T7"]), partes_t7(ID["T7"])
    seis["T7"] = OrderedDict([
        ("verifica", [lineas(RK.t7_cuarentena), lineas(RK.t_t7), "data/experiment/reextraccion_v2/corpus_v2/r1_tests.py:63-82 (origen)"]),
        ("estado", {"r1_fixture": esp_r1["T7"], "r1": I1["T7"]["estado"], "desarrollo": ID["T7"]["estado"]}),
        ("partes", [{"parte": k, "r1": p7_r1[k], "desarrollo": p7_dev[k],
                     "clase": (None if (p7_r1[k] and p7_dev[k]) else ("c" if k.startswith("P5") else "d")),
                     "motivo": (CUMPLE_AMBOS if (p7_r1[k] and p7_dev[k]) else
                                "los Sujetos fuera del catálogo JSON están en el bloque v3 del perfil (hallazgo E1, decisión pre-registrada del 27/09)" if k.startswith("P5") else "sin diagnóstico")}
                    for k in p7_r1]),
    ])
    # --- E4-a7
    pa7_r1, pa7_dev = partes_e4a7(I1["E4-a7"]), partes_e4a7(ID["E4-a7"])
    seis["E4-a7"] = OrderedDict([
        ("verifica", [lineas(RK.t_e4_a7), "data/experiment/reextraccion_v2/corpus_v2/r1_e4.py:18-19, :141-147 (origen)"]),
        ("estado", {"r1_fixture": esp_r1["E4-a7"], "r1": I1["E4-a7"]["estado"], "desarrollo": ID["E4-a7"]["estado"]}),
        ("partes", [{"parte": k, "r1": pa7_r1[k], "desarrollo": pa7_dev[k],
                     "clase": (None if (pa7_r1[k] and pa7_dev[k]) else ("c" if k.startswith("P3") else "d")),
                     "motivo": (CUMPLE_AMBOS if (pa7_r1[k] and pa7_dev[k]) else
                                "mismos cuatro ids que T7 P5" if k.startswith("P3") else "sin diagnóstico")}
                    for k in pa7_r1]),
    ])
    # --- E4-a8
    e8 = an["E4-a8"]
    seis["E4-a8"] = OrderedDict([
        ("verifica", [lineas(RK.t_e4_a8), "data/experiment/reextraccion_v2/corpus_v2/r1_e4.py:18-24, :141-202 (origen)"]),
        ("estado", {"r1_fixture": esp_r1["E4-a8"], "r1": I1["E4-a8"]["estado"], "desarrollo": ID["E4-a8"]["estado"]}),
        ("partes", [
            {"parte": "P1 alias_resueltos en los ids de catálogo de la tabla de r1",
             "r1": f"{e8['control_tabla_r1_sobre_r1']['alias_en_id_de_catalogo']}/{e8['control_tabla_r1_sobre_r1']['n_resueltos_en_la_tabla']}",
             "desarrollo": f"{e8['control_tabla_r1_sobre_desarrollo']['alias_en_id_de_catalogo']}/{e8['control_tabla_r1_sobre_desarrollo']['n_resueltos_en_la_tabla']}",
             "clase": "b", "motivo": "lee un artefacto propio de r1 (salida_r1/e4_propuestos.json); con la tabla del propio ensamblado (R-E4a8) desarrollo cumple"},
            {"parte": "P2 los propuestos resueltos no quedan en el grafo ni con aristas",
             "r1": f"{e8['control_tabla_r1_sobre_r1']['propuesto_ausente_sin_aristas']}/{e8['control_tabla_r1_sobre_r1']['n_resueltos_en_la_tabla']}",
             "desarrollo": f"{e8['control_tabla_r1_sobre_desarrollo']['propuesto_ausente_sin_aristas']}/{e8['control_tabla_r1_sobre_desarrollo']['n_resueltos_en_la_tabla']}",
             "clase": None, "motivo": CUMPLE_AMBOS},
        ]),
    ])
    props = propuestas(an)
    for k in seis:
        seis[k]["propuesta"] = props[k]
        seis[k]["rotulo_propuesta"] = "PROPUESTA — la entrada de r2 la sella la autora (laudo §3.1, punto 2)"

    cuatro = OrderedDict((i, OrderedDict([("r1_fixture", esp_r1[i]), ("r1", resumen_item(I1[i])), ("desarrollo", resumen_item(ID[i]))]))
                         for i in CUATRO)
    lista36 = [OrderedDict([("id", i), ("estado_r1_fixture", esp_r1[i]), ("estado_r1", I1[i]["estado"]), ("estado_desarrollo", ID[i]["estado"])])
               for i in no_cambian]

    conteos = OrderedDict([
        ("items", len(esp_r1)),
        ("cambian", len(cambian)),
        ("no_cambian", len(no_cambian)),
        ("seis_mas_cuatro_igual_a_cambian", sorted(SEIS + CUATRO) == cambian),
        ("transiciones_suman_46", sum(trans.values()) == len(esp_r1)),
        ("t5_filas_suman_30", sum(an["T5"]["resumen"]["por_clase"].values()) == 30),
        ("resuelto_a_persiste", sorted(i for i in cambian if esp_r1[i] == "resuelto" and ID[i]["estado"] == "persiste")),
    ])

    salida = OrderedDict()
    salida["unidad"] = "U-PRE-R2-DIAG"
    salida["etapa"] = "D1"
    salida["mandato"] = "docs/mandatos/UPRE_R2_diagnostico.md"
    salida["comando"] = CMD
    salida["clases_decision_3"] = CLASES
    salida["reglas_declaradas"] = OrderedDict([
        ("R-T5", "fila x presente por contenido si existe una arista referencia con evidencia tal que: (1) su fuente ancla en x.source_ancla "
                 "(todas las provenances); (2) su destino ancla en x.target_ancla y properties.destino == x.destino; (3) tipo del destino == "
                 "x.target_type; (4) los números de punto de su evidencia y de x.evidencia_verbatim se intersecan. R-T5 sin tipo = (1), (2), (4)."),
        ("R-E4a8", "la regla de t_e4_a8 leída sobre la tabla e4_propuestos.json del ensamblado del grafo bajo prueba"),
        ("R-T4", "esqueleto de un catálogo = aristas de RELACIONES_ESQUELETO que build_skeleton construye sobre ese catálogo "
                 "(ensamblar_corpus.inyectar_esqueleto_v3 sobre un grafo vacío, por import)"),
        ("R-CAT", "catálogo JSON v3 más los ids del bloque v3 del perfil que no están en el JSON, en memoria; contrafáctico, no resultado de r2"),
        ("SIM-H1", "resolvedor de remisiones re-corrido en memoria con TIPOS_ORIGEN + Condicion, Potestad y Definicion y las redirecciones "
                   "del manifiesto de desarrollo; control con los tipos originales; no es resultado de r2"),
        ("clase_T5_por_fila", "verbatim presente → sin clase; R-T5 → b; R-T5 sin tipo → b; ausente con la mención solo en nodos fuera de "
                              "TIPOS_ORIGEN → a (H1); ausente sin mención en el texto que lee el resolvedor → a; otro caso → d"),
    ])
    salida["entradas"] = entradas
    salida["corridas"] = OrderedDict([
        ("r1", OrderedDict([("kg", ENTRADAS["kg_r1"][0]), ("catalogo", ENTRADAS["catalogo_v2"][0]), ("politica_cuarentena", "flaggeada"),
                            ("resumen", dict(sorted(Counter(it["estado"] for it in items_r1).items()))),
                            ("control_contra_fixture", {"entrada": "KG-Reextraido-r1", "n_regresiones": reg_r1["n_regresiones"],
                                                        "regresiones": reg_r1["regresiones"], "coinciden": reg_r1["coinciden"]})])),
        ("desarrollo", OrderedDict([("kg", ENTRADAS["kg_desarrollo"][0]), ("catalogo", ENTRADAS["catalogo_v3"][0]), ("politica_cuarentena", "flaggeada"),
                                    ("resumen", dict(sorted(Counter(it["estado"] for it in items_dev).items()))),
                                    ("control_contra_linea_base_E6", control_e6)])),
    ])
    salida["e0_identico_tanda0_vs_enm01"] = e0_identico
    salida["transiciones_r1_fixture_a_desarrollo"] = dict(sorted(trans.items()))
    salida["seis_items"] = seis
    salida["analisis"] = an
    salida["cuatro_items_sin_diagnostico"] = cuatro
    salida["treinta_y_seis_sin_cambio"] = lista36
    salida["conteos"] = conteos
    return rel(salida)


# --------------------------------------------------------------------------- #
# Render .md                                                                   #
# --------------------------------------------------------------------------- #
def _c(v) -> str:
    if v is None:
        return "—"
    if isinstance(v, bool):
        return "sí" if v else "no"
    return str(v).replace("|", "/")


def render_md(s: dict) -> str:
    L = ["# U-PRE-R2-DIAG — D1: los seis ítems de la suite", ""]
    L.append(f"Mandato `{s['mandato']}`. Solo lectura, USD 0, sin API ni Neo4j. Comando: `{s['comando']}`. "
             "Todo número de este archivo sale de `d1_suite.json` (misma corrida).")
    L.append("")
    L.append("## 1. Reglas declaradas antes de aplicarse")
    L.append("")
    for k, v in s["reglas_declaradas"].items():
        L.append(f"- **{k}**: {v}")
    L.append("")
    L.append("Clases de la decisión 3: " + "; ".join(f"({k}) {v}" for k, v in s["clases_decision_3"].items()) + ".")
    L.append("")
    L.append("## 2. Entradas y controles")
    L.append("")
    L.append("| clave | ruta | sha256 |")
    L.append("|---|---|---|")
    for k, v in s["entradas"].items():
        L.append(f"| {k if k != v['ruta'] else '(registrado)'} | `{v['ruta']}` | `{v['sha256'][:16]}…` |")
    L.append("")
    cr = s["corridas"]
    L.append(f"- r1 (`{cr['r1']['kg']}`, catálogo v2, flaggeada): {cr['r1']['resumen']}; contra su entrada de la fixture: "
             f"{cr['r1']['control_contra_fixture']['n_regresiones']} diferencias, {cr['r1']['control_contra_fixture']['coinciden']} coinciden.")
    ce = cr["desarrollo"]["control_contra_linea_base_E6"]
    L.append(f"- desarrollo (`{cr['desarrollo']['kg']}`, catálogo v3, flaggeada): {cr['desarrollo']['resumen']}; contra la línea de base "
             f"de E6: estado igual {ce['estado_igual']}/{ce['items']}, detalle igual {ce['detalle_igual']}/{ce['items']}.")
    L.append(f"- E0 de los cinco TOs de desarrollo idéntico entre `salida_tanda0` y `salida_enm01` (byte a byte): {s['e0_identico_tanda0_vs_enm01']}.")
    L.append(f"- Transiciones r1 (fixture) → desarrollo: {s['transiciones_r1_fixture_a_desarrollo']}.")
    L.append("")
    L.append("## 3. Tabla de los seis ítems")
    L.append("")
    L.append("| ítem | verifica | r1 (fixture / medido) | desarrollo | clases por parte | propuesta recomendada |")
    L.append("|---|---|---|---|---|---|")
    for i, it in s["seis_items"].items():
        clases = ", ".join(f"{p['parte'].split(' ')[0]}={p['clase'] or '—'}" for p in it["partes"])
        rec = it["propuesta"]["recomendada"]
        L.append(f"| {i} | `{it['verifica'][0]}` | {it['estado']['r1_fixture']} / {it['estado']['r1']} | {it['estado']['desarrollo']} | {clases} | "
                 f"{rec}: {_c(it['propuesta'][rec])[:160]}… |")
    L.append("")
    L.append("## 4. Ítem por ítem")
    an = s["analisis"]
    for i, it in s["seis_items"].items():
        L.append("")
        L.append(f"### {i}")
        L.append("")
        L.append("Verifica: " + "; ".join(f"`{x}`" for x in it["verifica"]) + ".")
        L.append(f"Estado: r1 en la fixture **{it['estado']['r1_fixture']}**, r1 medido **{it['estado']['r1']}**, desarrollo **{it['estado']['desarrollo']}**.")
        L.append("")
        L.append("| parte | r1 | desarrollo | clase | motivo |")
        L.append("|---|---|---|---|---|")
        for p in it["partes"]:
            L.append(f"| {_c(p['parte'])} | {_c(p['r1'])} | {_c(p['desarrollo'])} | {_c(p['clase'])} | {_c(p['motivo'])} |")
        L.append("")
        if i == "T2":
            t = an["T2"]
            L.append(f"Evidencia (`d1_suite.json`, `analisis.T2`): nodos con «125 %» por punto — r1 {dict(t['nodos_125_por_punto']['r1'])}, "
                     f"desarrollo {dict(t['nodos_125_por_punto']['desarrollo'])}; ocurrencias de «125%» en el texto propio de E0 por punto "
                     f"{dict(t['ocurrencias_125_en_E0_texto_propio'])}.")
            for f in t["fusion_en_desarrollo"]:
                L.append(f"- Nodo fundido `{f['nodo'][:60]}…` en {f['puntos_ext']}: {len(f['entidades_e1_con_125'])} entidades de E1 con «125», "
                         f"{f['descripciones_distintas']} descripción distinta y {f['slugs_distintos']} slug de `entity_slug_v3` "
                         f"(`e2_lib.py`: Restriccion/Obligacion/Excepcion se deduplican por descripción); el id del nodo termina en ese slug: "
                         f"{all(x['id_del_nodo_termina_en_slug'] for x in f['entidades_e1_con_125'])}.")
            r1d = Counter((x["chunk_id"], x["entity_slug_v3"]) for x in t["r1_mismas_unidades_en_e1"])
            L.append(f"- En la salida de E1 que ensambló r1, las mismas unidades tienen {len(t['r1_mismas_unidades_en_e1'])} entidades con «125» y "
                     f"{len({x['entity_slug_v3'] for x in t['r1_mismas_unidades_en_e1']})} slugs distintos: no se funden.")
            L.append("- Clasificación asistida (lectura de texto de esta instancia, para revisión de la autora): en r1, los dos nodos con «125 %» "
                     "de `ext::7.5.3` parafrasean la única ocurrencia de E0 en ese punto; sin la fusión, desarrollo tendría 5 nodos en 5 puntos y P1 cumpliría.")
        if i == "T4":
            t = an["T4"]
            L.append(f"Evidencia (`analisis.T4`, R-T4): aristas {t['aristas']}; r1 = build_skeleton(v2): {_c(t['r1_igual_a_build_skeleton_v2'])}; "
                     f"desarrollo = build_skeleton(v3): {_c(t['desarrollo_igual_a_build_skeleton_v3'])}; referencia contenida en desarrollo: "
                     f"{_c(t['referencia_contenida_en_desarrollo'])}. Las {t['extra_desarrollo_menos_referencia']['n']} de más: "
                     f"{t['extra_desarrollo_menos_referencia']['por_relacion']}, con algún extremo fuera del catálogo v2 "
                     f"{t['extra_desarrollo_menos_referencia']['con_algun_extremo_fuera_del_catalogo_v2']}, con ambos extremos en el catálogo v3 "
                     f"{t['extra_desarrollo_menos_referencia']['con_ambos_extremos_en_el_catalogo_v3']}.")
        if i == "T5":
            t = an["T5"]
            L.append(f"Control de SIM-H1 (`analisis.T5.control_sim_h1`): {dict(t['control_sim_h1'])}.")
            L.append(f"Resumen: {json.dumps(t['resumen'], ensure_ascii=False, sort_keys=True)}.")
            L.append("")
            L.append("| n | origen → destino | tipo destino r1 | r1 verbatim / R-T5 | desarrollo verbatim / R-T5 / sin tipo | clase | motivo | SIM-H1 R-T5 / sin tipo / arista al destino |")
            L.append("|---|---|---|---|---|---|---|---|")
            for f in t["filas"]:
                da = f.get("diagnostico_ausencia") or {}
                sim = (f"{_c(da.get('sim_h1_rt5_completa'))} / {_c(da.get('sim_h1_rt5_sin_tipo'))} / "
                       f"{_c(da.get('sim_h1_arista_origen_con_destino'))}") if da else "—"
                L.append(f"| {f['n']} | {f['source_ancla']} → {f['destino']} | {f['target_type_r1']} | {_c(f['r1']['verbatim'])} / {_c(f['r1']['rt5_completa'])} | "
                         f"{_c(f['desarrollo']['verbatim'])} / {_c(f['desarrollo']['rt5_completa'])} / {_c(f['desarrollo']['rt5_sin_tipo'])} | "
                         f"{_c(f['clase'])} | {_c(f['motivo'])} | {sim} |")
            L.append("")
            L.append("SIM-H1 es evidencia sobre la causa, no un resultado de r2. «Arista al destino» = alguna arista referencia de la simulación "
                     "con fuente en el origen y properties.destino igual al de la fila, sin condición sobre el ancla del nodo destino: donde da sí y "
                     "R-T5 da no, la diferencia está en la condición (2) de R-T5 (ancla primaria del nodo destino de r1), no en la mención.")
            L.append("")
            L.append("Clasificación asistida (lectura de texto de esta instancia, para revisión de la autora) de las ausencias sin mención en el texto "
                     "del resolvedor: n=2, la descripción de la Excepcion termina en «comprendidos en este punto 3.5» y deja afuera «en el marco de lo "
                     "previsto en el punto 14.2.1»; n=5, las Excepciones de `ext::3.16.3.5` parafrasean «Lo previsto en los puntos 3.16.3.1. al "
                     "3.16.3.4.» como «la declaración jurada»; n=10, la mención está solo en el texto heredado del chunk y E1 no la llevó a ningún nodo.")
        if i in ("T7", "E4-a7"):
            t = an["T7_E4-a7"]
            L.append(f"Evidencia (`analisis.T7_E4-a7`): bloque v3 del perfil {t['ids_bloque_perfil_v3']} ids, catálogo JSON {t['ids_catalogo_json_v3']}; "
                     f"en el bloque y no en el JSON: {t['en_bloque_y_no_en_json']}; los Sujetos fuera de catálogo de desarrollo están todos ahí: "
                     f"{_c(t['fuera_contenidos_en_bloque_menos_json'])} ({[d['id'] for d in t['fuera_de_catalogo_no_propuestos_desarrollo']]}). "
                     f"Contrafáctico R-CAT: {t['contrafactico_catalogo_ampliado']}.")
        if i == "E4-a8":
            t = an["E4-a8"]
            L.append(f"Evidencia (`analisis.E4-a8`): tablas {t['tablas']}; R-E4a8 r1 con su tabla: alias {t['R-E4a8_r1_con_su_tabla']['alias_en_id_de_catalogo']}/"
                     f"{t['R-E4a8_r1_con_su_tabla']['n_resueltos_en_la_tabla']}, ausentes {t['R-E4a8_r1_con_su_tabla']['propuesto_ausente_sin_aristas']}; "
                     f"desarrollo con su tabla: alias {t['R-E4a8_desarrollo_con_su_tabla']['alias_en_id_de_catalogo']}/"
                     f"{t['R-E4a8_desarrollo_con_su_tabla']['n_resueltos_en_la_tabla']}, ausentes {t['R-E4a8_desarrollo_con_su_tabla']['propuesto_ausente_sin_aristas']}. "
                     "Los tres ids de catálogo de la tabla de r1 en desarrollo: "
                     + "; ".join(f"{d['id']} presente={_c(d['presente_en_desarrollo'])}, provenances de extracción {d['provenances_de_extraccion']}, "
                                 f"alias_resueltos {d['alias_resueltos']}" for d in t["ids_resueltos_en_r1_en_el_grafo_de_desarrollo"]) + ". "
                     "Un id con provenances de extracción y sin alias_resueltos fue emitido por E1 con el id de catálogo (en desarrollo E4 "
                     "solo resolvió las filas de su propia tabla); un id con 0 provenances de extracción está solo como nodo de esqueleto. "
                     "Lo que E4-a8 verifica es la mecánica del merge de E4, que R-E4a8 cumple en las dos generaciones.")
        L.append("")
        L.append(f"**{it['rotulo_propuesta']}.** Recomendada: {it['propuesta']['recomendada']}.")
        for k, v in it["propuesta"].items():
            if k != "recomendada":
                L.append(f"- ({k}) {v}")
    L.append("")
    L.append("## 5. Los otros cuatro ítems que cambian (sin diagnóstico)")
    L.append("")
    L.append("| ítem | r1 fixture | r1 medido | desarrollo | detalle r1 | detalle desarrollo |")
    L.append("|---|---|---|---|---|---|")
    for i, v in s["cuatro_items_sin_diagnostico"].items():
        L.append(f"| {i} | {v['r1_fixture']} | {v['r1']['estado']} | {v['desarrollo']['estado']} | {_c(v['r1']['detalle'])[:200]} | {_c(v['desarrollo']['detalle'])[:200]} |")
    L.append("")
    L.append("## 6. Los 36 ítems que no cambian")
    L.append("")
    L.append("| ítem | r1 fixture | r1 medido | desarrollo |")
    L.append("|---|---|---|---|")
    for v in s["treinta_y_seis_sin_cambio"]:
        L.append(f"| {v['id']} | {v['estado_r1_fixture']} | {v['estado_r1']} | {v['estado_desarrollo']} |")
    L.append("")
    L.append("## 7. Conteos")
    L.append("")
    for k, v in s["conteos"].items():
        L.append(f"- {k}: {v}")
    L.append("")
    return "\n".join(L)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="U-PRE-R2-DIAG D1 (solo lectura)")
    ap.add_argument("--out-dir", required=True, help="directorio de salida (d1_suite.json y d1_suite.md)")
    a = ap.parse_args(argv)
    out = Path(a.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    s = construir()
    (out / "d1_suite.json").write_text(json.dumps(s, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    (out / "d1_suite.md").write_text(render_md(s), encoding="utf-8")
    print(f"escrito: {out / 'd1_suite.json'} y {out / 'd1_suite.md'}")
    print(f"transiciones: {s['transiciones_r1_fixture_a_desarrollo']}")
    print(f"conteos: {s['conteos']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
