"""
ensamblar_tanda0.py — U-TANDA0-2A (E1c, gate 1 del pre-registro): cableado
de r1 para un MANIFIESTO DE ENSAMBLADO. Código puro, cero LLM. Ningún módulo
sellado se edita: todos se IMPORTAN y sus rutas y tablas se REDIRIGEN EN
MEMORIA (monkeypatch de atributos de módulo, precedente del gate 6:
scripts/metricas_intrinsecas.py --reensamblar-r1, que redirige
r1_comun.SALIDA_R1 y llama ensamblar_r1.correr sin editar).

Produce, para un manifiesto de ensamblado (tanda0_ens_*.json o
desarrollo_5tos.json) y un directorio de ENTRADA con las salidas E1→E3 por TO
(runner_corpus.py --salida: <to>/grafo_<to>.json, reporte_e2_<to>.json,
extracciones_finales_<to>.jsonl, finales.jsonl, extracciones_e1_compact.jsonl):

  <salida>/kg.json                    E5 de ensamblar_corpus.ensamblar (merge
                                      determinístico + esqueleto v3 POR PERFIL
                                      + suite de tests si el manifiesto la declara)
  <salida>/reporte_ensamblado.json    reporte de ensamblar_corpus
  <salida>/r1/kg.json                 cadena r1 (E2 con cola flaggeada → merge
                                      guardado → E4 determinístico → esqueleto →
                                      referencias → provenance rica → orden final)
  <salida>/r1/*.json                  los mismos intermedios que salida_r1/
  <salida>/r1/reporte_ensamblado_r1.json

POR QUÉ UNA RÉPLICA DE LA CADENA Y NO ensamblar_r1.correr TAL CUAL. La cadena
de ensamblar_r1.correr (ensamblar_r1.py:72-194) está cableada al corpus de
desarrollo en cuatro puntos que un corpus con perfil v3_b54 no puede
compartir:
  (a) etapa_e2 llama e2_lib.ensamblar(chunks, registros) sin `esquema` ni
      `labels_catalogo` del perfil (ensamblar_r1.py:61), mientras la corrida
      E2 del runner sí los pasa (runner_corpus.py:696-698): sobre un corpus v3
      el E2 de la cadena no reproduciría grafo_<to>.json;
  (b) r1_e5_esqueleto.inyectar_esqueleto aborta si build_skeleton no tiene
      paridad con KG-Refinado (r1_e5_esqueleto.py:56-58), una guarda del
      esqueleto v2 que por construcción no vale para el catálogo v3
      (ensamblar_corpus.py:41-44 lo declara así);
  (c) r1_comun.CATALOGO_PATH, assemble.CATALOGO_PATH y
      r1_invariantes.SUJETOS_CATALOGO_SET son del catálogo v2;
  (d) r1_referencias.INVENTARIO_TOS cablea los cinco TOs de desarrollo
      (r1_referencias.py:54-61) y ensamblar_corpus.merge_grafos usa el orden
      default TOS_ORDEN cuando r1_invariantes lo llama sin orden.
Por eso este módulo replica la cadena PASO A PASO importando los mismos
módulos r1_* (r1_cola_flaggeada, r1_invariantes, r1_e4, r1_e5_esqueleto,
r1_referencias, r1_provenance) y redirige lo que corresponde. Con perfil
produccion_dev todas las redirecciones son identidad y la réplica debe
reproducir salida/kg.json (8e2eadee…) y salida_r1/kg.json (0226e947…) byte a
byte; `--selftest-dev` además compara la réplica con ensamblar_r1.correr
llamado directamente (motor `ensamblar_r1`, solo válido en perfil dev).

Pasos de ensamblar_r1.cerrar que leen artefactos propios de r1 y se SALTEAN
con nota (ensamblar_r1.py:213-222): tests T1-T7 (r1_tests lee la muestra
inspeccionada de r1 y KG-Refinado), recomputo de política de la cola y diff
contra el kg sellado 8e2eadee. La tabla propuestos antes/después de la cola
(corrida sin cola hasta e4) sí se replica: es genérica.

Uso:
  .venv/bin/python ensamblar_tanda0.py --manifiesto <ens.json> --entrada <dir E1-E3> --salida <dir>
      [--hasta final] [--sin-cola] [--motor replica|ensamblar_r1] [--selftest-dev]
"""

from __future__ import annotations

import argparse
import contextlib
import hashlib
import json
import re
import sys
from copy import deepcopy
from pathlib import Path

AQUI = Path(__file__).resolve().parent                    # tanda0/code
REPO = AQUI.parents[3]                                    # raíz del repo
REX = REPO / "data" / "experiment" / "reextraccion_v2"
CORPUS_V2 = REX / "corpus_v2"
GRAFO_V2_CODE = REPO / "data" / "experiment" / "grafo_v2" / "code"
ESQUEMA_V3 = REPO / "data" / "experiment" / "esq_v3_miembros" / "esquema_v3_clases.json"
PERFIL_V3 = "v3_b54"

for _p in (str(REX), str(CORPUS_V2), str(GRAFO_V2_CODE), str(REX / "e2_reduce"),
           str(REX / "e1_extractor"), str(REX / "e3_verificador")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import manifiesto_corpus as MC          # noqa: E402  (sellados: solo import)
import perfil_e1                        # noqa: E402
import ensamblar_corpus as EC           # noqa: E402
import r1_comun as C                    # noqa: E402
import r1_invariantes as INV            # noqa: E402
import r1_e4 as E4                      # noqa: E402
import r1_e5_esqueleto as E5            # noqa: E402
import r1_referencias as REF            # noqa: E402
import r1_provenance as PROV            # noqa: E402
import r1_cola_flaggeada as COLA        # noqa: E402
import e2_lib                           # noqa: E402
import assemble                         # noqa: E402
from schema import RELACIONES_ESQUELETO  # noqa: E402

ETAPAS = ("e2", "merge", "e4", "esqueleto", "referencias", "provenance", "final")

SELLOS_DEV = {  # verdad conocida del corpus de desarrollo (desarrollo_5tos.json → sellos.kg; r1: nomenclatura)
    "kg_e5": "8e2eadee57b48e00ccb51ade9a953ba1469001fe089c45d97c4307ccf2725581",
    "kg_r1": "0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a",
}


def sha256_texto(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def _rel(p: Path) -> str:
    """Ruta relativa al repo cuando está adentro; absoluta si no (scratchpad)."""
    p = Path(p).resolve()
    try:
        return str(p.relative_to(REPO))
    except ValueError:
        return str(p)


# ------------------------------------------------------------------------- #
# Redirecciones en memoria                                                   #
# ------------------------------------------------------------------------- #
def inventario_desde_manifiesto(man: MC.Manifiesto) -> dict[str, tuple[str, ...]]:
    """r1_referencias.INVENTARIO_TOS a partir de `nombres_remision` del
    manifiesto, en orden alfabético de id (el mismo orden del dict cableado de
    r1_referencias, que resolver_norma recorre devolviendo el primer match)."""
    return {t["id"]: tuple(t["nombres_remision"]) for t in sorted(man.tos, key=lambda t: t["id"])}


def plan_redirecciones(man: MC.Manifiesto, perfil, entrada: Path, salida_r1: Path) -> list[tuple]:
    """(módulo, atributo, valor nuevo). En perfil dev los valores de catálogo
    e inventario coinciden con los cableados (se verifica en --selftest-dev)."""
    v3 = perfil.nombre == PERFIL_V3
    orden = tuple(man.orden_corrida)
    return [
        (C, "SALIDA", Path(entrada)),
        (C, "SALIDA_R1", Path(salida_r1)),
        (C, "E0_ENM01", Path(man.e0_salida)),
        (C, "TOS_ORDEN", orden),
        (C, "CATALOGO_PATH", ESQUEMA_V3 if v3 else C.CATALOGO_PATH),
        (EC, "TOS_ORDEN", orden),
        (assemble, "CATALOGO_PATH", ESQUEMA_V3 if v3 else assemble.CATALOGO_PATH),
        (INV, "SUJETOS_CATALOGO_SET",
         perfil.esquema.sujetos_catalogo_set if v3 else INV.SUJETOS_CATALOGO_SET),
        (REF, "INVENTARIO_TOS", inventario_desde_manifiesto(man)),
    ]


@contextlib.contextmanager
def redirigido(plan: list[tuple]):
    originales = [(m, a, getattr(m, a)) for m, a, _ in plan]
    try:
        for m, a, v in plan:
            setattr(m, a, v)
        yield
    finally:
        for m, a, v in originales:
            setattr(m, a, v)


def describir_plan(plan: list[tuple]) -> list[dict]:
    out = []
    for m, a, v in plan:
        if isinstance(v, (frozenset, set)):
            desc = f"<{len(v)} ids>"
        elif isinstance(v, dict):
            desc = {k: list(x) for k, x in v.items()}
        else:
            desc = str(v)
        out.append({"modulo": m.__name__, "atributo": a, "valor": desc})
    return out


# ------------------------------------------------------------------------- #
# E5: ensamblar_corpus.ensamblar con esqueleto v3 por perfil                 #
# ------------------------------------------------------------------------- #
def cargar_grafos(entrada: Path, orden: tuple) -> dict[str, dict]:
    grafos = {}
    for to in orden:
        p = Path(entrada) / to / f"grafo_{to}.json"
        if not p.exists():
            raise FileNotFoundError(f"falta {p} — la corrida de {to} no cerró su E2")
        grafos[to] = json.loads(p.read_text(encoding="utf-8"))
    return grafos


def ensamblar_e5(man: MC.Manifiesto, perfil, entrada: Path, salida: Path, escribir: bool) -> dict:
    orden = tuple(man.orden_corrida)
    esqueleto_v3 = EC.ESQUEMA_V3_DEFAULT if perfil.nombre == EC.PERFIL_CON_ESQUELETO_V3 else None
    if esqueleto_v3 is not None and not Path(esqueleto_v3).exists():
        raise FileNotFoundError(f"perfil {perfil.nombre} sin artefacto de esqueleto v3: {esqueleto_v3}")
    grafos = cargar_grafos(entrada, orden)
    res = EC.ensamblar(grafos, orden, man.tests_respuesta_conocida, esqueleto_v3)
    if escribir:
        salida.mkdir(parents=True, exist_ok=True)
        (salida / "kg.json").write_text(res["kg_json"], encoding="utf-8")
        if res["tests"] is not None:
            (salida / "tests_respuesta_conocida.json").write_text(
                json.dumps(res["tests"], ensure_ascii=False, indent=1), encoding="utf-8")
        (salida / "reporte_ensamblado.json").write_text(
            json.dumps(res["reporte"], ensure_ascii=False, indent=1), encoding="utf-8")
    return {"sha256_kg": res["sha256_kg"], "kg_json": res["kg_json"], "reporte": res["reporte"],
            "esqueleto_v3": str(esqueleto_v3) if esqueleto_v3 else None}


# ------------------------------------------------------------------------- #
# Cadena r1 (réplica paso a paso de ensamblar_r1.correr)                     #
# ------------------------------------------------------------------------- #
def etapa_e2(perfil, con_cola: bool) -> dict:
    """ensamblar_r1.etapa_e2 (ensamblar_r1.py:49-69) con el esquema y los
    labels del PERFIL (None en dev = byte-idéntico al original)."""
    out = {}
    for to in C.TOS_ORDEN:
        chunks = C.cargar_chunks_enm01(to)
        registros = C.cargar_extracciones_finales(to)
        info_cola = None
        if con_cola:
            registros, info_cola = COLA.inyectar_cola(to, registros)
        ens = e2_lib.ensamblar(chunks, registros, esquema=perfil.esquema,
                               labels_catalogo=perfil.labels_catalogo)
        grafo = {"nodes": ens["nodes"], "edges": ens["edges"]}
        if con_cola:
            COLA.flaggear_grafo(grafo, info_cola)
        sha = C.sha256_bytes(C.dumps_kg(grafo).encode("utf-8"))
        out[to] = {"grafo": grafo, "ensamblado": ens, "sha": sha,
                   "paridad_sellado": sha == C.cargar_reporte_e2(to)["sha256_grafo"],
                   "cola": info_cola, "registros": registros}
    return out


def inyectar_esqueleto_v3(kg: dict, catalogo: dict) -> dict:
    """r1_e5_esqueleto.inyectar_esqueleto (r1_e5_esqueleto.py:54-131) SIN la
    guarda de paridad contra KG-Refinado, que es del esqueleto v2. Mismos
    pasos, mismos helpers importados (E5._prov_esqueleto, E5.REL_PADRE_SUGERIDO,
    assemble.build_skeleton con CATALOGO_PATH redirigido al catálogo v3). El
    campo `paridad_kg_refinado` declara la no aplicabilidad en vez de simular
    una comparación."""
    nodes_sk, edges_sk, counts_sk = assemble.build_skeleton()
    antes_rel = C.conteo(kg["edges"], "relation")
    nodes_by_id = {n["id"]: n for n in kg["nodes"]}
    creados, enriquecidos = [], []
    for sid, sk in nodes_sk.items():
        prov = E5._prov_esqueleto(sk["provenance"])
        n = nodes_by_id.get(sid)
        if n is None:
            n = {"id": sid, "type": "Sujeto", "label": sk["label"],
                 "properties": dict(sk["properties"]),
                 "provenance": prov, "provenances": [prov], "rol_fuente": "esqueleto"}
            kg["nodes"].append(n)
            nodes_by_id[sid] = n
            creados.append(sid)
        else:
            for k, v in sk["properties"].items():
                n["properties"].setdefault(k, v)
            if C.prov_key(prov) not in {C.prov_key(p) for p in n["provenances"]}:
                n["provenances"].append(prov)
            n["rol_fuente"] = "extraido+esqueleto"
            enriquecidos.append(sid)

    triplas = {(e["source"], e["relation"], e["target"]) for e in kg["edges"]}
    n_esq = 0
    for (s, r, t), e in edges_sk.items():
        if (s, r, t) in triplas:
            continue
        prov = E5._prov_esqueleto(e["provenance"])
        kg["edges"].append({"source": s, "target": t, "relation": r,
                            "provenance": prov, "provenances": [prov],
                            "rol_fuente": "esqueleto"})
        triplas.add((s, r, t))
        n_esq += 1

    flag, sin_padre, padre_fuera = [], [], []
    for n in kg["nodes"]:
        if n["type"] != "Sujeto" or n["properties"].get("nivel") != "propuesto":
            continue
        padre = n["properties"].get("padre_sugerido")
        if not padre:
            sin_padre.append(n["id"])
            continue
        if padre not in nodes_sk:
            padre_fuera.append((n["id"], padre))
            continue
        k = (n["id"], E5.REL_PADRE_SUGERIDO, padre)
        if k in triplas:
            continue
        prov = dict(n["provenance"])
        kg["edges"].append({"source": n["id"], "target": padre, "relation": E5.REL_PADRE_SUGERIDO,
                            "provenance": prov, "provenances": [dict(p) for p in n["provenances"]],
                            "rol_fuente": "cuarentena_flaggeada",
                            "properties": {"flag": "padre_sugerido_no_laudado"}})
        triplas.add(k)
        flag.append(k)

    despues_rel = C.conteo(kg["edges"], "relation")
    rels = RELACIONES_ESQUELETO + (E5.REL_PADRE_SUGERIDO,)
    return {
        "paridad_kg_refinado": {
            "aplicable": False,
            "motivo": "guarda del esqueleto v2 (paridad de build_skeleton con KG-Refinado, "
                      "r1_e5_esqueleto.py:56-58); no vale para el catálogo v3 "
                      "(ensamblar_corpus.py:41-44). Salteada con nota; nada se simula.",
            "catalogo": str(assemble.CATALOGO_PATH),
        },
        "conteos_build_skeleton": counts_sk,
        "nodos_esqueleto_creados": len(creados),
        "nodos_esqueleto_enriquecidos": len(enriquecidos),
        "aristas_esqueleto_agregadas": n_esq,
        "aristas_padre_sugerido_flaggeadas": len(flag),
        "propuestos_sin_padre": sin_padre,
        "propuestos_padre_fuera_de_catalogo": padre_fuera,
        "relaciones_antes": {r: antes_rel.get(r, 0) for r in rels},
        "relaciones_despues": {r: despues_rel.get(r, 0) for r in rels},
        "declaracion_esquema": "padre_sugerido no está en schema.DOMAIN_RANGE; arista flaggeada "
                               "de cuarentena, no subclase_de. No se edita schema.py.",
        "ids_creados": creados,
    }


def correr_cadena(perfil, con_cola: bool, hasta: str = "final", w=None) -> dict:
    """Réplica de ensamblar_r1.correr (ensamblar_r1.py:72-194). `w(nombre, obj)`
    escribe intermedios (None = no escribe). Devuelve el mismo `estado`."""
    h = ETAPAS.index(hasta)
    w = w or (lambda *a, **k: None)
    resumen: dict = {"etapas": [], "con_cola": con_cola, "perfil_e1": perfil.nombre}

    por_to = etapa_e2(perfil, con_cola)
    resumen["e2_por_to"] = {to: {"nodes": len(d["grafo"]["nodes"]), "edges": len(d["grafo"]["edges"]),
                                 "sha256": d["sha"], "paridad_con_grafo_sellado": d["paridad_sellado"],
                                 "conflictos_properties": len(d["ensamblado"]["conflictos_properties"]),
                                 "cuarentena_propuestos": len(d["ensamblado"]["cuarentena"]),
                                 "rechazos_e2": len(d["ensamblado"]["rechazos_e2"]),
                                 "cola": (d["cola"] or {}).get("resumen")}
                            for to, d in por_to.items()}
    if not con_cola:
        assert all(d["paridad_sellado"] for d in por_to.values()), \
            "sin cola, E2 por TO debe reproducir grafo_<to>.json byte a byte"
    resumen["etapas"].append("e2")
    print("[e2]", json.dumps({to: (v["nodes"], v["edges"], v["paridad_con_grafo_sellado"])
                             for to, v in resumen["e2_por_to"].items()}), flush=True)
    estado = {"resumen": resumen, "por_to": por_to}
    if h == 0:
        return estado

    grafos = {to: d["grafo"] for to, d in por_to.items()}
    m = INV.merge_grafos_guardado(grafos)
    kg = {"nodes": m["nodes"], "edges": m["edges"]}
    inv_merge = INV.verificar_invariantes(
        kg, m["grafos_pre_merge"], merges_nodo=len(m["merges_cross_to"]),
        merges_arista=INV.merges_arista_de(m["grafos_pre_merge"], kg["edges"]))
    assert inv_merge["ok"], inv_merge["fallos"]
    resumen["merge"] = {"invariantes": inv_merge, "merges_cross_to": len(m["merges_cross_to"]),
                        "merges_por_tipo": C.conteo(m["merges_cross_to"], "type"),
                        "adjudicacion_cross_to": len(m["adjudicacion_cross_to"]),
                        "conflictos_cross_to": len(m["conflictos"])}
    w("adjudicacion_cross_to.json", m["adjudicacion_cross_to"])
    resumen["etapas"].append("merge")
    print("[merge]", json.dumps({k: v for k, v in resumen["merge"].items() if k != "invariantes"}), flush=True)
    estado.update({"kg": kg, "m": m})
    if h == 1:
        return estado

    catalogo = C.cargar_catalogo()
    r_prop = E4.resolver_propuestos(kg, catalogo)
    r_to = E4.canonizar_texto_ordenado(kg)
    intra = [{**c, "to": to} for to, d in por_to.items() for c in d["ensamblado"]["conflictos_properties"]]
    r_conf = E4.filtrar_conflictos(intra, m["conflictos"])
    nodes_by_id = {n["id"]: n for n in kg["nodes"]}
    for tid, props in r_conf["variantes_texto_ordenado"].items():
        n = nodes_by_id.get(tid)
        if n is not None:
            for p, vals in props.items():
                n["properties"][f"{p}_variantes"] = list(vals)
    inv_e4 = INV.verificar_invariantes(kg)
    assert inv_e4["ok"], inv_e4["fallos"]
    resumen["e4"] = {
        "propuestos": {"resueltos": r_prop["n_resueltos"], "cuarentena": r_prop["n_cuarentena"],
                       "motivos": r_prop["motivos"], "aristas_reapuntadas": r_prop["aristas_reapuntadas"]},
        "texto_ordenado": {"canonicos": r_to["canonicos"],
                           "eliminados": [{"id": e["id_eliminado"], "reasignado_a": e["reasignado_a"],
                                           "n_provenances": len(e["provenances"])} for e in r_to["eliminados"]],
                           "aristas_reapuntadas": r_to["aristas_reapuntadas"],
                           "n_final": sum(1 for n in kg["nodes"] if n["type"] == "TextoOrdenado")},
        "conflictos": {k: v for k, v in r_conf.items()
                       if k in ("n_total", "n_variantes_to", "n_reales", "reales_por_tipo_property")},
        "invariantes": inv_e4,
    }
    w("e4_propuestos.json", r_prop["tabla"])
    w("e4_texto_ordenado.json", r_to)
    w("e4_conflictos.json", r_conf)
    resumen["etapas"].append("e4")
    print("[e4]", json.dumps({k: v for k, v in resumen["e4"].items() if k != "invariantes"},
                             ensure_ascii=False), flush=True)
    estado["e4_propuestos"] = r_prop["tabla"]
    if h == 2:
        return estado

    if perfil.nombre == PERFIL_V3:
        r_esq = inyectar_esqueleto_v3(kg, catalogo)
    else:
        r_esq = E5.inyectar_esqueleto(kg, catalogo)
    inv_e5 = INV.verificar_invariantes(kg)
    assert inv_e5["ok"], inv_e5["fallos"]
    resumen["esqueleto"] = {k: v for k, v in r_esq.items() if k != "ids_creados"}
    w("e5_esqueleto.json", r_esq)
    resumen["etapas"].append("esqueleto")
    print("[esqueleto]", json.dumps(resumen["esqueleto"], ensure_ascii=False), flush=True)
    if h == 3:
        return estado

    r_ref = REF.detectar_y_resolver(kg)
    inv_ref = INV.verificar_invariantes(kg)
    assert inv_ref["ok"], inv_ref["fallos"]
    resumen["referencias"] = r_ref["resumen"]
    w("referencias_remisiones.json", r_ref["remisiones"])
    w("referencias_muestra30.json", r_ref["muestra"])
    w("referencias_irresolubles.json", r_ref["irresolubles"])
    resumen["etapas"].append("referencias")
    print("[referencias]", json.dumps(r_ref["resumen"], ensure_ascii=False), flush=True)
    if h == 4:
        return estado

    r_prov = PROV.enriquecer(kg, por_to)
    resumen["provenance"] = r_prov["resumen"]
    w("provenance_verificacion.json", r_prov)
    resumen["etapas"].append("provenance")
    print("[provenance]", json.dumps(r_prov["resumen"], ensure_ascii=False), flush=True)
    if h == 5:
        return estado

    kg["nodes"].sort(key=lambda n: n["id"])
    kg["edges"].sort(key=lambda e: (e["source"], e["relation"], e["target"]))
    estado["kg_json"] = C.dumps_kg(kg)
    estado["sha256"] = C.sha256_bytes(estado["kg_json"].encode("utf-8"))
    resumen["etapas"].append("final")
    return estado


def correr_motor_ensamblar_r1(perfil, con_cola: bool, hasta: str) -> dict:
    """Motor literal: ensamblar_r1.correr con las rutas ya redirigidas. Solo
    válido en perfil dev (ver docstring del módulo, puntos a-d)."""
    if perfil.nombre != "produccion_dev":
        raise RuntimeError(
            f"el motor ensamblar_r1 solo vale con perfil produccion_dev: con {perfil.nombre} su E2 "
            "corre sin esquema/labels del perfil (ensamblar_r1.py:61) y su esqueleto exige paridad "
            "con KG-Refinado (r1_e5_esqueleto.py:56-58) — usar --motor replica")
    import ensamblar_r1 as ER  # noqa: PLC0415 — import diferido, módulo real sin modificar
    return ER.correr(con_cola=con_cola, hasta=hasta, escribir_salida=False)


# ------------------------------------------------------------------------- #
# Orquestación                                                               #
# ------------------------------------------------------------------------- #
def ensamblar_manifiesto(man: MC.Manifiesto, entrada: Path, salida: Path, hasta: str = "final",
                         con_cola: bool = True, motor: str = "replica") -> dict:
    perfil = perfil_e1.perfil(man.perfil_e1)
    entrada, salida = Path(entrada), Path(salida)
    salida_r1 = salida / "r1"
    plan = plan_redirecciones(man, perfil, entrada, salida_r1)

    # --- E5 (ensamblar_corpus) ---
    e5 = ensamblar_e5(man, perfil, entrada, salida, escribir=True)
    print(f"[e5] nodes={e5['reporte']['nodes_total']} edges={e5['reporte']['edges_total']} "
          f"sha256={e5['sha256_kg'][:12]}… esqueleto_v3={e5['esqueleto_v3']}", flush=True)

    # --- cadena r1 ---
    def w(nombre: str, obj) -> None:
        salida_r1.mkdir(parents=True, exist_ok=True)
        (salida_r1 / nombre).write_text(json.dumps(obj, ensure_ascii=False, indent=1), encoding="utf-8")

    with redirigido(plan):
        if motor == "replica":
            print("=== cadena r1 (réplica), corrida 1 ===", flush=True)
            e1 = correr_cadena(perfil, con_cola, hasta, w)
            e2 = None
            e0 = None
            if hasta == "final":
                print("=== cadena r1 (réplica), corrida 2 (sin escribir) ===", flush=True)
                e2 = correr_cadena(perfil, con_cola, hasta, None)
                if con_cola:
                    print("=== cadena r1 sin cola hasta e4 (tabla antes/después) ===", flush=True)
                    e0 = correr_cadena(perfil, False, "e4", None)
        else:
            print("=== cadena r1 (motor ensamblar_r1.correr) ===", flush=True)
            e1 = correr_motor_ensamblar_r1(perfil, con_cola, hasta)
            e2 = correr_motor_ensamblar_r1(perfil, con_cola, hasta) if hasta == "final" else None
            e0 = None

    out = {"manifiesto": {"nombre": man.nombre, "path": _rel(man.path),
                          "sha256": hashlib.sha256(Path(man.path).read_bytes()).hexdigest(),
                          "perfil_e1": man.perfil_e1, "orden_corrida": list(man.orden_corrida),
                          "tests_respuesta_conocida": man.tests_respuesta_conocida,
                          "e0_salida": _rel(man.e0_salida)},
           "entrada": _rel(entrada), "salida": _rel(salida), "motor": motor, "hasta": hasta,
           "con_cola": con_cola, "redirecciones": describir_plan(plan),
           "e5": {"sha256_kg": e5["sha256_kg"], "nodes_total": e5["reporte"]["nodes_total"],
                  "edges_total": e5["reporte"]["edges_total"], "esqueleto_v3": e5["esqueleto_v3"],
                  "tests_respuesta_conocida": e5["reporte"]["tests_respuesta_conocida"]}}
    if hasta != "final":
        out["r1"] = {"hasta": hasta, "resumen": e1["resumen"]}
        return out

    kg = e1["kg"]
    doble = e2 is not None and e1["sha256"] == e2["sha256"] and e1["kg_json"] == e2["kg_json"]
    salida_r1.mkdir(parents=True, exist_ok=True)
    (salida_r1 / "kg.json").write_text(e1["kg_json"], encoding="utf-8")
    sha_disco = C.sha256_path(salida_r1 / "kg.json")
    inv = INV.verificar_invariantes(kg)

    def tabla_prop(t):
        return {"resueltos": sum(1 for f in t if f["estado"] == "resuelto"),
                "cuarentena": sum(1 for f in t if f["estado"] == "cuarentena"), "total": len(t)}
    prop_antes_despues = None
    if e0 is not None:
        antes, despues = tabla_prop(e0["e4_propuestos"]), tabla_prop(e1["e4_propuestos"])
        ids_antes = {f["id_propuesto"] for f in e0["e4_propuestos"]}
        nuevos = [f for f in e1["e4_propuestos"] if f["id_propuesto"] not in ids_antes]
        prop_antes_despues = {"sin_cola": antes, "con_cola": despues,
                              "nuevos_con_cola": [{"id": f["id_propuesto"], "label": f["label"],
                                                   "estado": f["estado"], "resuelto_a": f["resuelto_a"]}
                                                  for f in nuevos]}

    r = e1["resumen"]
    reporte = {
        "grafo": f"{man.nombre}/r1", "manifiesto": out["manifiesto"], "motor": motor,
        "sha256_kg": e1["sha256"], "sha256_kg_en_disco": sha_disco,
        "doble_corrida_byte_identica": doble,
        "entrada": _rel(entrada), "kg_e5_sha256": e5["sha256_kg"],
        "nodes_total": len(kg["nodes"]), "edges_total": len(kg["edges"]),
        "nodes_by_type": C.conteo(kg["nodes"], "type"),
        "edges_by_relation": C.conteo(kg["edges"], "relation"),
        "invariantes_final": inv,
        "e2_por_to": r["e2_por_to"],
        "merge": {k: v for k, v in r["merge"].items() if k != "invariantes"},
        "e4": {k: v for k, v in r["e4"].items() if k != "invariantes"},
        "propuestos_antes_despues_cola": prop_antes_despues,
        "esqueleto": r["esqueleto"],
        "referencias": r["referencias"],
        "provenance": r["provenance"],
        "cola_flaggeada": {to: v["cola"] for to, v in r["e2_por_to"].items()},
        "redirecciones": out["redirecciones"],
        "pasos_de_r1_salteados_con_nota": [
            "tests T1-T7 de r1_tests (ensamblar_r1.py:215-217): leen referencias_muestra30_inspeccionada_A2.json "
            "de salida_r1 y KG-Refinado — artefactos propios de r1; el manifiesto declara "
            f"tests_respuesta_conocida={man.tests_respuesta_conocida!r}.",
            "cola_recomputo_politica (ensamblar_r1.py:219-220): recomputo informativo de la política de "
            "la cola de r1; no forma parte del grafo.",
            "diff_vs_sellado (ensamblar_r1.py:222-235): compara contra salida/kg.json (8e2eadee…), sellado de "
            "desarrollo; no aplica a otro corpus.",
        ],
        "declaraciones_esquema": [
            "referencia nodo→nodo (B1.3) no está en schema.DOMAIN_RANGE (solo TextoOrdenado→Comunicacion).",
            "padre_sugerido (E5, cuarentena flaggeada) no está en schema.DOMAIN_RANGE.",
            "schema.py no se edita; las aristas nuevas llevan rol_fuente.",
        ],
    }
    w("reporte_ensamblado_r1.json", reporte)
    out["r1"] = {k: reporte[k] for k in ("sha256_kg", "sha256_kg_en_disco", "doble_corrida_byte_identica",
                                          "nodes_total", "edges_total", "invariantes_final")}
    out["r1"]["invariantes_ok"] = inv["ok"]
    return out


# ------------------------------------------------------------------------- #
# Perfil r2 (U-R2-CODIGO, R3): cadena r2 sobre la salida guardada E1→E3       #
# ------------------------------------------------------------------------- #
# Con --perfil-r2, el ensamblado aplica el perfil r2 (validador, política y
# catálogo r2) a la salida guardada del perfil de E1 del manifiesto: el
# manifiesto no cambia de perfil (perfil_e1.py y manifiesto_corpus.py no se
# editan), y la cadena r2 corre aparte de la r1, con salida en <salida>/r2/.
# Pasos: entrada r2 (crudo del intento aceptado, validador r2) → sujetos por
# relación y registro de no mapeados → E2 r2 por TO → fusión con la guarda
# cross-TO → E4 sin la pasada residual de propuestos (medida, no aplicada) →
# esqueleto del catálogo r2 → remite_a → establecida_en derivada → umbrales
# (par B) → procedencia rica → orden final. Las marcas de la cadena van al
# grafo, en el modelo de pyd_r2/code/modelos_r2: cola humana y colisión
# cross-TO en las properties del nodo (como en los grafos sellados), la base
# resuelta y la verificación en tabla en el elemento de umbral, el calificador
# en la arista de sujeto; las variantes del TextoOrdenado quedan en el reporte
# de E4 (e4_conflictos.json).
TIPOS_CONTENIDO_R2 = REF.TIPOS_CONTENIDO_R2


def sujetos_de_resolucion(cat: dict, M) -> frozenset:
    """R2 de U-RERESOL-CAT, W1: el conjunto de ids contra el que E2 y el merge
    entre TOs aceptan un sujeto. Con el catálogo de resolución
    (`r1_e4.catalogo_resolucion_r2`), el suyo; sin él, el del request
    (`modelos_r2.SUJETOS_R2_SET`), como siempre."""
    return cat["sujetos_set"] if "sujetos_set" in cat else M.SUJETOS_R2_SET


def plan_redirecciones_r2(man: MC.Manifiesto, perfil, entrada: Path, salida_r2: Path, cat: dict, M) -> list[tuple]:
    plan = [(m, a, v) for m, a, v in plan_redirecciones(man, perfil, entrada, salida_r2)
            if (m, a) not in ((C, "CATALOGO_PATH"), (assemble, "CATALOGO_PATH"), (INV, "SUJETOS_CATALOGO_SET"))]
    return plan + [(C, "CATALOGO_PATH", cat["entrada_esqueleto_path"]),
                   (assemble, "CATALOGO_PATH", cat["entrada_esqueleto_path"]),
                   (INV, "SUJETOS_CATALOGO_SET", sujetos_de_resolucion(cat, M)),
                   (REF, "TITULOS_TOS", REF.titulos_de_inventario(
                       sorted(t["id"] for t in man.tos), {t["id"]: t["nombres_remision"] for t in man.tos}))]


def derivar_establecida_en(kg: dict, canon: dict[str, str]) -> dict:
    """Decisión 11 del mandato: todo nodo de contenido sin `establecida_en`
    la recibe hacia el TextoOrdenado de cada TO de su procedencia, con
    `rol_fuente = derivada_de_procedencia`."""
    con = {e["source"] for e in kg["edges"] if e["relation"] == "establecida_en"}
    triplas = {(e["source"], e["relation"], e["target"]) for e in kg["edges"]}
    nuevas = []
    for n in sorted(kg["nodes"], key=lambda x: x["id"]):
        if n["type"] not in TIPOS_CONTENIDO_R2 or n["id"] in con:
            continue
        for to in sorted({p["to"] for p in n["provenances"] if p.get("to") in canon}):
            k = (n["id"], "establecida_en", canon[to])
            if k in triplas:
                continue
            provs = [dict(p) for p in n["provenances"] if p.get("to") == to]
            e = {"source": n["id"], "target": canon[to], "relation": "establecida_en",
                 "provenance": dict(provs[0]), "provenances": provs, "rol_fuente": "derivada_de_procedencia"}
            kg["edges"].append(e)
            triplas.add(k)
            nuevas.append(e)
    tipo = {n["id"]: n["type"] for n in kg["nodes"]}
    sin = [n["id"] for n in kg["nodes"] if n["type"] in TIPOS_CONTENIDO_R2
           and n["id"] not in {e["source"] for e in kg["edges"] if e["relation"] == "establecida_en"}]
    return {"aristas_derivadas": len(nuevas),
            "por_tipo": C.conteo([{"t": tipo[e["source"]]} for e in nuevas], "t"),
            "nodos_de_contenido_sin_establecida_en": len(sin), "ids_sin": sin[:20]}


def _texto_e0_nodo(n: dict, chunks: dict[str, dict], V) -> list[tuple[str, str]]:
    out = []
    for p in n.get("provenances", []):
        cid = p.get("chunk_id")
        if cid and cid in chunks and cid not in [c for c, _ in out]:
            out.append((cid, V.texto_completo(chunks[cid])))
    return out


def _rangos_unidad_repetida(texto: str, cs: list) -> list[str]:
    """Rangos «entre X <unidad> y Y <unidad>» con la unidad repetida (límite
    declarado en la fila 7 del plan: la cota inferior recibe máximo asumido)."""
    out = []
    for a, b in zip(cs, cs[1:]):
        if a.unidad and a.unidad == b.unidad and re.fullmatch(r"\s+y\s+", texto[a.fin:b.inicio]) \
                and re.search(r"\bentre\s+$", texto[:a.inicio], re.I):
            out.append(texto[max(0, a.inicio - 7):b.fin])
    return out


def resolver_base(base: str | None, to: str, kg_def: dict[tuple[str, str], str], detector_r2: bool = False) -> dict:
    """L-ESQ-R2 §1.3 (c): la base literal se resuelve a su punto por el
    mecanismo de remisiones (detectar_menciones sobre la base) o a una
    Definicion del mismo TO cuyo `termino` normalizado es la base; si no
    resuelve, se marca. Con `detector_r2` (fase r2b; U-R2-CODIGO-2, C2,
    punto r), las menciones salen del mismo detector que `remite_a`
    (`REF.menciones_por_tramo`, que normaliza el texto y aplica
    `detectar_menciones_r2` con las reglas de REF.REGLAS_R2)."""
    if not base:
        return {"base_destino": None, "via": None, "marca": None}
    menciones = (REF.menciones_por_tramo([base], to, REF.REGLAS_R2) if detector_r2
                 else REF.detectar_menciones(base, to))
    for men in menciones:
        td = men["to_destino"]
        if td is None or td not in C.TOS_ORDEN:
            continue
        unidades = REF.unidades_e0(td)
        for d in men["puntos"] + [f"S{s}" for s in men["secciones"]]:
            if d in unidades:
                return {"base_destino": f"{td}::{d}", "via": "remision", "marca": None}
        if not men["puntos"] and not men["secciones"] and men["clase"] != "interna":
            return {"base_destino": f"{td}::TO", "via": "remision", "marca": None}
    nid = kg_def.get((to, C.norm(base)))
    if nid:
        return {"base_destino": nid, "via": "definicion", "marca": None}
    return {"base_destino": None, "via": None, "marca": "base_no_resuelta"}


def llenar_umbrales_r2(kg: dict, tramos_e1: dict[str, list[str]], tablas: dict[str, list[str]], M, V, RCMP,
                       pol, fase: str = "r2a") -> dict:
    """Par B en r2a (L-ESQ-R2 §1.3 y §1.4; mandato R3.f): la lista de umbrales
    de Restriccion, Obligacion, Condicion y Excepcion, armada en código con las
    reglas de U-PYD (reglas_comparacion.analizar), desde los tramos de E1 si
    los hay (r2b) o, en r2a, desde la descripción guardada y los
    campos_heredados_v3 (umbral, plazo). El tramo del elemento es la cuantía
    tal como está en esa fuente; se verifica contra el texto de E0 de los
    chunks del nodo y, si el chunk tiene tablas de e0-r2, contra sus celdas.
    Lo que no verifica queda marcado (`tramo_verificado = no`), sin
    corregirse. El plazo heredado que no es un plazo va a `frecuencia`.
    Con la fase r2b (U-R2-CODIGO-2, C2): el plazo sin marcador queda
    `no_determinada`, sin `comparacion_asumida` (punto m, enmienda 3 a
    L-ESQ-R2); la lista se completa, no se reemplaza, y el elemento del
    límite relativo que dejó validador_r2 se conserva junto a los de cuantía
    (punto o); y la base se resuelve con el detector de `remite_a` (punto
    r). En r2a, la regla anterior, para reproducir los grafos sellados."""
    r2b = fase == "r2b"
    plazo_sin_marcador = "no_determinada" if r2b else "maximo_asumido"
    chunks = {c["id"]: c for to in C.TOS_ORDEN for c in _chunks_r2(to)}
    kg_def = {}
    for n in kg["nodes"]:
        if n["type"] == "Definicion" and isinstance(n["properties"].get("termino"), str):
            for p in n["provenances"]:
                kg_def.setdefault((p.get("to"), C.norm(n["properties"]["termino"])), n["id"])
    rangos = []
    cont = {"nodos": 0, "nodos_con_lista": 0, "elementos": 0, "por_origen": {}, "por_comparacion": {},
            "comparacion_asumida": 0, "no_determinada": 0, "tramo_verificado": {}, "verificado_en_tabla": {},
            "base_resuelta": 0, "base_no_resuelta": 0, "frecuencia_desde_plazo": 0,
            "frecuencia_fuera_de_lista": 0}
    if r2b:
        cont["elementos_previos_conservados"] = 0
        cont["unidad_desde_rotulo"] = {"elementos": 0, "por_to": {}, "nodos": []}

    def suma(d, k):
        cont[d][k] = cont[d].get(k, 0) + 1

    for n in sorted(kg["nodes"], key=lambda x: x["id"]):
        if n["type"] not in M.TIPOS_CON_UMBRALES:
            continue
        cont["nodos"] += 1
        props = n["properties"]
        desc = props.get("descripcion")
        prim = n["provenance"].get("chunk_id")
        titulo = chunks[prim].get("titulo") if prim in chunks else None
        to = n["provenance"].get("to")
        fuentes = []
        if tramos_e1.get(n["id"]):
            fuentes = [(t, "e1") for t in tramos_e1[n["id"]]]
        else:
            if isinstance(desc, str) and desc:
                fuentes.append((desc, "descripcion"))
            for k, v in sorted((n.get("campos_heredados_v3") or {}).items()):
                if not isinstance(v, str) or not v.strip():
                    continue
                if n["type"] == "Obligacion" and k == "plazo" and not any(
                        c.unidad in M.UNIDADES_TEMPORALES + M.UNIDADES_TEMPORALES_FUERA
                        for c in RCMP.detectar_cuantias(v)):
                    if props.get("frecuencia") is None:
                        f = V.frecuencia_desde_tramo(v)
                        props["frecuencia"] = f or v
                        n.setdefault("originales", {}).setdefault("frecuencia", v)
                        if f is None:
                            n.setdefault("fuera_de_lista", []).append("frecuencia")
                            cont["frecuencia_fuera_de_lista"] += 1
                        cont["frecuencia_desde_plazo"] += 1
                    continue
                fuentes.append((v, "campo_v3"))
        textos = _texto_e0_nodo(n, chunks, V)
        celdas = "\n".join(t for cid, _ in textos for t in tablas.get(cid, []))
        elementos, vistos = [], set()
        for texto, origen in fuentes:
            cs = RCMP.analizar(texto, desc, titulo, plazo_sin_marcador)
            rangos += [{"id": n["id"], "tramo": r} for r in _rangos_unidad_repetida(texto, cs)]
            for c in cs:
                clave = (c.valor, c.unidad, c.moneda)
                if origen == "campo_v3" and clave in vistos:
                    continue
                vistos.add(clave)
                el = RCMP.elemento_umbral(c, c.texto, origen)
                niveles = [V.verificar_tramo(c.texto, t, pol.holgura)[0] for _, t in textos] or ["no"]
                el["tramo_verificado"] = ("exacta" if "exacta" in niveles else
                                          "tokens" if "tokens" in niveles else "no")
                en_tabla = (None if not celdas else
                            V.verificar_tramo(c.texto, celdas, pol.holgura)[0] in ("exacta", "tokens"))
                b = resolver_base(c.base, to, kg_def, detector_r2=r2b)
                el.update(base_destino=b["base_destino"], base_via=b["via"],
                          base_no_resuelta=b["marca"] == "base_no_resuelta", verificado_en_tabla=en_tabla)
                elementos.append(M.ElementoUmbral.model_validate(el).model_dump(mode="json", exclude_defaults=True))
                cont["elementos"] += 1
                suma("por_origen", origen)
                suma("por_comparacion", c.comparacion)
                suma("tramo_verificado", el["tramo_verificado"])
                suma("verificado_en_tabla", str(en_tabla))
                cont["comparacion_asumida"] += c.comparacion_asumida
                cont["no_determinada"] += c.comparacion == "no_determinada"
                cont["base_resuelta"] += b["base_destino"] is not None
                cont["base_no_resuelta"] += b["marca"] == "base_no_resuelta"
        if elementos and r2b and props.get("umbrales"):
            cont["elementos_previos_conservados"] += len(props["umbrales"])
            props["umbrales"] = list(props["umbrales"]) + elementos
            cont["nodos_con_lista"] += 1
        elif elementos:
            props["umbrales"] = elementos
            cont["nodos_con_lista"] += 1
        if r2b and props.get("umbrales"):
            # T3-bis de U-REEXT-T0, decisión 2: la cuantía que es una celda de una tabla serializada con rótulo
            # hereda la unidad del rótulo; el tramo no cambia.
            bloques = bloques_con_rotulo(textos)
            if bloques:
                nuevos = []
                for el in props["umbrales"]:
                    h = unidad_desde_rotulo(el, bloques, RCMP, M, desc, titulo, plazo_sin_marcador)
                    nuevos.append(h or el)
                    if h:
                        u = cont["unidad_desde_rotulo"]
                        u["elementos"] += 1
                        u["por_to"][to] = u["por_to"].get(to, 0) + 1
                        u["nodos"].append({"id": n["id"], "to": to, "tramo": h["tramo"], "valor": h.get("valor"),
                                           "unidad": h.get("unidad"), "moneda": h.get("moneda"),
                                           "tabla": h["originales"]["tabla"],
                                           "rotulo": h["originales"]["unidad_desde_rotulo"]})
                props["umbrales"] = nuevos
    cont["rangos_con_unidad_repetida"] = len(rangos)
    return {"resumen": cont, "rangos": rangos}


# ------------------------------------------------------------------------- #
# T3-bis de U-REEXT-T0 (fase r2b): propuestos después del merge cross-TO,    #
# unidad del rótulo de tabla y marca de umbral no cuantificable              #
# ------------------------------------------------------------------------- #
# Decisión 1.b: una mención hecha solo de pronombres, determinantes o palabras funcionales (lista cerrada, sobre el
# texto normalizado por C.norm) no nombra un sujeto.
PALABRAS_VACIAS_SUJETO = frozenset((
    "se", "el", "ella", "ellos", "ellas", "ello", "este", "esta", "estos", "estas", "esto", "ese", "esa", "esos",
    "esas", "eso", "aquel", "aquella", "aquellos", "aquellas", "aquello", "cada", "uno", "una", "unos", "unas",
    "otro", "otra", "otros", "otras", "quien", "quienes", "quienquiera", "cual", "cuales", "la", "los", "las", "lo",
    "le", "les", "su", "sus", "mismo", "misma", "mismos", "mismas", "dicho", "dicha", "dichos", "dichas", "tal",
    "tales", "ambos", "ambas", "todo", "toda", "todos", "todas", "alguno", "alguna", "algunos", "algunas",
    "ninguno", "ninguna", "cualquiera", "que", "de", "del", "al", "a", "y", "o", "u", "e"))
MARCA_MENCION_VACIA = "mencion_pronombre_o_palabra_vacia"
TABLAS_FORZADAS_R2B = REX / "e1_extractor" / "tablas_residuales_forzadas_r2b.json"
MOTIVO_SIN_CUANTIA = "sin cuantía detectable"
MOTIVO_TABLA_FORZADA = "cuantías solo en tabla residual forzada"
RE_BLOQUE_TABLA = re.compile(r"\[TABLA (\S+) \|[^\]\n]*\]\n(.*?)\n\[FIN TABLA \1\]", re.S)
RE_ROTULO_TABLA = re.compile(r"^Rótulo: (.+)$", re.M)
RE_FILA_TABLA = re.compile(r"^Fila \d+: (.*)$", re.M)


def mencion_vacia(label: str) -> bool:
    toks = re.findall(r"\w+", C.norm(label))
    return bool(toks) and all(t in PALABRAS_VACIAS_SUJETO for t in toks)


def normalizar_propuestos_r2b(kg: dict, registro: list[dict], renombres: dict[str, dict[str, str]], cat: dict) -> dict:
    """Decisión 1 de T3-bis de U-REEXT-T0 (fase r2b), después del merge cross-TO y antes del esqueleto, que arma
    las aristas padre_sugerido desde la propiedad del propuesto:
    a. el propuesto renombrado por la colisión cross-TO (sufijo __<to>) lleva su id nuevo en las filas de su TO del
       registro de no mapeados (LN-5, S28);
    b. el propuesto cuya mención es un pronombre o una palabra vacía se descarta: el nodo y sus aristas salen del
       grafo, sus filas del registro quedan con estado «descartado» y la marca, y las aristas quitadas se listan con
       la norma, la unidad, la mención y el tramo, sin asignarles rol. El padre_sugerido hacia un Sujeto de nivel
       instancia se reemplaza por la clase de la instancia (instancia_de; marca padre_sugerido_instancia) o, sin
       clase, se quita con la marca padre_sugerido_descartado (S3);
    c. el propuesto sin padre_sugerido recibe el rol de alcance de su TO (rol_por_to del catálogo r2) con la marca
       padre_por_defecto (S19); si sus TOs no dan un único rol, queda sin padre y listado.
    Muta kg y las filas del registro. Devuelve el resumen y las filas de las aristas quitadas."""
    entrada = cat["entrada_esqueleto"]
    clases = {c["id"]: c for c in entrada["clases"]}
    roles = {r["id"] for r in entrada["roles"]}
    res = {"filas_renombradas": [], "descartados": [], "padre_desde_instancia": [], "padre_descartado": [],
           "padre_por_defecto": [], "sin_rol_de_alcance": []}
    for to, ren in sorted(renombres.items()):
        for f in registro:
            if f.get("to") == to and f.get("id_nodo") in ren:
                res["filas_renombradas"].append({"to": to, "chunk_id": f.get("chunk_id"),
                                                 "indice_relacion": f.get("indice_relacion"),
                                                 "id_anterior": f["id_nodo"], "id_nodo": ren[f["id_nodo"]]})
                f["id_nodo"] = ren[f["id_nodo"]]
    by_id = {n["id"]: n for n in kg["nodes"]}
    propuestos = sorted((n for n in kg["nodes"] if n["type"] == "Sujeto" and n["properties"].get("nivel") == "propuesto"),
                        key=lambda n: n["id"])
    descartar = {n["id"] for n in propuestos if mencion_vacia(n["label"])}
    quitadas = sorted((e for e in kg["edges"] if e["source"] in descartar or e["target"] in descartar),
                      key=lambda e: (e["source"], e["relation"], e["target"]))
    filas_quitadas = []
    for e in quitadas:
        prop = e["target"] if e["target"] in descartar else e["source"]
        otro = by_id.get(e["source"] if prop == e["target"] else e["target"], {})
        pv = e.get("provenance") or {}
        fila_reg = next((f for f in registro if f.get("id_nodo") == prop and f.get("chunk_id") == pv.get("chunk_id")),
                        {})
        filas_quitadas.append({
            "propuesto": prop, "mencion": by_id[prop]["label"], "marca": MARCA_MENCION_VACIA,
            "relacion": e["relation"], "source": e["source"], "target": e["target"],
            "to": pv.get("to"), "archivo": pv.get("archivo"), "chunk_id": pv.get("chunk_id"), "punto": pv.get("punto"),
            "sujeto_mencion": e.get("sujeto_mencion"), "mencion_verificada": e.get("mencion_verificada"),
            "indice_relacion": fila_reg.get("indice_relacion"),
            "extremo": otro.get("id"), "extremo_tipo": otro.get("type"), "extremo_label": otro.get("label"),
            "tramo_del_extremo": next((p.get("tramo") for p in otro.get("provenances", [])
                                       if p.get("chunk_id") == pv.get("chunk_id") and p.get("tramo")), None)})
    if descartar:
        kg["edges"][:] = [e for e in kg["edges"] if e["source"] not in descartar and e["target"] not in descartar]
        kg["nodes"][:] = [n for n in kg["nodes"] if n["id"] not in descartar]
        for f in registro:
            if f.get("id_nodo") in descartar:
                f["estado"] = "descartado"
                f["motivo_descarte"] = MARCA_MENCION_VACIA
    for i in sorted(descartar):
        res["descartados"].append({
            "id": i, "mencion": by_id[i]["label"], "padre_sugerido": by_id[i]["properties"].get("padre_sugerido"),
            "tos": sorted({p.get("to") for p in by_id[i].get("provenances", []) if p.get("to")}),
            "aristas_quitadas": sum(1 for x in filas_quitadas if x["propuesto"] == i),
            "filas_del_registro": sum(1 for f in registro if f.get("id_nodo") == i)})
    propuestos = [n for n in propuestos if n["id"] not in descartar]
    for n in propuestos:
        p = n["properties"].get("padre_sugerido")
        if not p or (clases.get(p) or {}).get("nivel") != "instancia":
            continue
        clase = clases[p].get("instancia_de")
        if clase and ((clases.get(clase) or {}).get("nivel") == "clase" or clase in roles):
            n["properties"]["padre_sugerido"] = clase
            n["properties"]["padre_sugerido_instancia"] = p
            res["padre_desde_instancia"].append({"id": n["id"], "instancia": p, "padre_sugerido": clase})
        else:
            del n["properties"]["padre_sugerido"]
            n["properties"]["padre_sugerido_descartado"] = p
            res["padre_descartado"].append({"id": n["id"], "instancia": p})
    for n in propuestos:
        if n["properties"].get("padre_sugerido"):
            continue
        tos = sorted({p.get("to") for p in n.get("provenances", []) if p.get("to")})
        rol = {to: (cat["rol_por_to"].get(C.archivo_de_to(to)) or {}).get("rol_id") for to in tos}
        candidatos = set(rol.values())
        if len(candidatos) == 1 and None not in candidatos:
            r = candidatos.pop()
            n["properties"]["padre_sugerido"] = r
            n["properties"]["padre_por_defecto"] = "true"
            res["padre_por_defecto"].append({"id": n["id"], "mencion": n["label"], "tos": tos, "padre_sugerido": r})
        else:
            res["sin_rol_de_alcance"].append({"id": n["id"], "mencion": n["label"], "rol_por_to": rol})
    resumen = {k: len(v) for k, v in res.items()}
    resumen.update(aristas_quitadas=len(filas_quitadas), detalle=res)
    return {"resumen": resumen, "aristas_quitadas": filas_quitadas}


def bloques_con_rotulo(textos: list[tuple[str, str]]) -> list[dict]:
    """Bloques de tabla serializada ([TABLA …] … [FIN TABLA …]) con una línea «Rótulo:», de los textos de E0 del
    nodo, con el conjunto de valores de sus celdas («columna = valor» de las líneas «Fila n:»)."""
    out, vistos = [], set()
    for cid, t in textos:
        for m in RE_BLOQUE_TABLA.finditer(t or ""):
            r = RE_ROTULO_TABLA.search(m.group(2))
            if not r or (cid, m.group(1)) in vistos:
                continue
            vistos.add((cid, m.group(1)))
            celdas = {c.split(" = ", 1)[1].strip() for f in RE_FILA_TABLA.findall(m.group(2))
                      for c in f.split(" | ") if " = " in c}
            out.append({"chunk_id": cid, "tabla": m.group(1), "rotulo": r.group(1).strip(), "celdas": celdas})
    return out


def unidad_desde_rotulo(el: dict, bloques: list[dict], RCMP, M, desc, titulo, plazo_sin_marcador) -> dict | None:
    """Decisión 2 de T3-bis: un elemento sin valor ni unidad cuyo tramo es el valor de una celda de un bloque con
    rótulo hereda la unidad del rótulo («-En millones de pesos-»): la cuantía se detecta sobre «<tramo> <unidad>»
    con las reglas de U-PYD y el elemento gana valor, unidad y moneda; tramo, comparación y verificación no
    cambian (si la comparación del texto compuesto fuera otra, no se aplica). La regla anterior, el rótulo y la
    tabla quedan en `originales`."""
    if el.get("valor") is not None or el.get("unidad") is not None:
        return None
    tramo = str(el.get("tramo") or "").strip()
    for b in bloques:
        if tramo not in b["celdas"]:
            continue
        frase = re.sub(r"^en\s+", "", b["rotulo"].strip(" -–—()[]"), flags=re.I).strip()
        compuesto = f"{tramo} {frase}"
        cs = RCMP.analizar(compuesto, desc, titulo, plazo_sin_marcador) if frase else []
        if len(cs) != 1 or cs[0].texto != compuesto or cs[0].valor is None or cs[0].comparacion != el.get("comparacion"):
            continue
        c = cs[0]
        nuevo = dict(el)
        nuevo.update(valor=c.valor, unidad=c.unidad, regla_comparacion=c.regla)
        for k in ("moneda", "dias_tipo"):
            if getattr(c, k) is not None:
                nuevo[k] = getattr(c, k)
        if c.fuera_de_lista:
            nuevo["fuera_de_lista"] = sorted(set(nuevo.get("fuera_de_lista") or []) | set(c.fuera_de_lista))
        nuevo["originales"] = {**(el.get("originales") or {}), "regla_comparacion": el.get("regla_comparacion"),
                               "unidad_desde_rotulo": b["rotulo"], "tabla": b["tabla"], "chunk_id": b["chunk_id"]}
        return M.ElementoUmbral.model_validate(nuevo).model_dump(mode="json", exclude_defaults=True)
    return None


def _celdas_por_tabla(tablas_dir: Path | None) -> dict[str, list[tuple[str, list[str]]]]:
    """chunk_id → [(id de tabla, textos de sus celdas)] de las tablas de e0-r2 (como `_celdas_por_chunk`, por tabla)."""
    out: dict[str, list[tuple[str, list[str]]]] = {}
    if tablas_dir is None:
        return out
    for to in C.TOS_ORDEN:
        p = Path(tablas_dir) / f"tablas_{to}.json"
        if not p.exists():
            continue
        for t in json.loads(p.read_text(encoding="utf-8"))["tablas"]:
            celdas = [str(c) for s in t.get("segmentos", []) for f in s.get("filas", []) for c in f if c]
            for cid in t.get("chunks", []):
                out.setdefault(cid, []).append((t["id"], celdas))
    return out


def marcar_umbral_no_cuantificable_r2b(kg: dict, tramos_e1: dict[str, list[str]], celdas_tabla: dict, RCMP) -> dict:
    """Decisión 3 de T3-bis (S18, primera pieza): la Restriccion limite_cuantitativo que queda sin lista de
    umbrales y sin cuantía detectable (RCMP.detectar_cuantias) en su descripción, sus tramos (los de umbral de E1 y
    el de la entidad, en la procedencia) y las celdas de las tablas de sus chunks lleva la marca r2b
    `umbral_no_cuantificable` con el sha256 del detector. Ampliación tomada en la sesión de T3-bis: también la lleva,
    con su propio motivo y el sha256 de la lista, la que solo tiene cuantías en celdas de tablas forzadas a residual
    (tablas_residuales_forzadas_r2b.json). La marca va en `properties_no_definidas`: NodoR2 y la shape S26 cierran
    las claves de `properties` por tipo."""
    det_sha = C.sha256_path(Path(RCMP.__file__))
    crudo = TABLAS_FORZADAS_R2B.read_bytes()
    forz_sha = C.sha256_bytes(crudo)
    forzadas = {t["tabla"] for t in json.loads(crudo.decode("utf-8"))["tablas"]}
    filas, sin_marca = [], []
    for n in sorted(kg["nodes"], key=lambda x: x["id"]):
        props = n["properties"]
        if n["type"] != "Restriccion" or props.get("tipo") != "limite_cuantitativo" or props.get("umbrales"):
            continue
        cids = sorted({p.get("chunk_id") for p in n.get("provenances", []) if p.get("chunk_id")})
        textos = ([("descripcion", props.get("descripcion"))] + [("tramo_de_umbral_e1", t) for t in tramos_e1.get(n["id"], [])]
                  + [("tramo", p.get("tramo")) for p in n.get("provenances", []) if p.get("tramo")])
        en_texto = sorted({o for o, t in textos if isinstance(t, str) and RCMP.detectar_cuantias(t)})
        tablas_con = sorted({tid for cid in cids for tid, cs in celdas_tabla.get(cid, [])
                             if any(RCMP.detectar_cuantias(x) for x in cs)})
        fila = {"id": n["id"], "to": n["provenance"].get("to"), "chunks": cids, "descripcion": props.get("descripcion"),
                "cuantias_en": en_texto, "tablas_con_cuantias": tablas_con}
        if not en_texto and not tablas_con:
            motivo = MOTIVO_SIN_CUANTIA
        elif not en_texto and all(t in forzadas for t in tablas_con):
            motivo = MOTIVO_TABLA_FORZADA
        else:
            sin_marca.append(fila)
            continue
        nd = n.setdefault("properties_no_definidas", {})
        nd["umbral_no_cuantificable"] = True
        nd["umbral_no_cuantificable_motivo"] = motivo
        nd["umbral_no_cuantificable_detector_sha256"] = det_sha
        if motivo == MOTIVO_TABLA_FORZADA:
            nd["umbral_no_cuantificable_tablas_forzadas_sha256"] = forz_sha
        filas.append({**fila, "motivo": motivo})
    return {"resumen": {"marcados": len(filas), "por_motivo": C.conteo([{"m": f["motivo"]} for f in filas], "m"),
                        "por_to": C.conteo(filas, "to"), "sin_marca_con_cuantia": [f["id"] for f in sin_marca],
                        "detector_sha256": det_sha, "tablas_forzadas_sha256": forz_sha},
            "filas": filas, "sin_marca": sin_marca}


def enriquecer_procedencias_r2(kg: dict) -> dict:
    """Procedencia rica (los campos de r1_provenance: chunk_id, paginas,
    ancestros) conservando el `chunk_id` que trae la procedencia del perfil r2
    (r1_provenance, que no se edita, lo reasignaría por regla)."""
    chunks = {to: {c["id"]: c for c in _chunks_r2(to)} for to in C.TOS_ORDEN}
    stats = {"provenances": 0, "extraccion": 0, "esqueleto": 0, "sin_chunk": 0}

    def una(p: dict) -> None:
        stats["provenances"] += 1
        rol, to = p.get("rol_documental") or "", p.get("to")
        if rol == "esqueleto" or to not in C.TOS_ORDEN:
            p.setdefault("chunk_id", None)
            p.setdefault("paginas", [])
            p.setdefault("ancestros", [])
            stats["esqueleto"] += 1
            return
        cid = p.get("chunk_id")
        ch = chunks[to].get(cid) if cid else None
        if ch is None:
            stats["sin_chunk"] += 1
            p.setdefault("paginas", [])
            p.setdefault("ancestros", [])
            return
        ancestros = []
        for h in ch.get("herencia", []):
            if h["unidad_origen"] not in ancestros:
                ancestros.append(h["unidad_origen"])
        punto = p["punto"]
        if rol.startswith("herencia_"):
            paginas = sorted({pg for h in ch.get("herencia", []) if h["unidad_origen"] == punto
                              for pg in h.get("paginas", [])})
            ancestros = ancestros[:ancestros.index(punto)] if punto in ancestros else ancestros
        else:
            paginas = list(ch.get("paginas", []))
            ancestros = [a for a in ancestros if a != punto]
        p["paginas"] = paginas
        p["ancestros"] = ancestros
        stats["extraccion"] += 1

    for obj in kg["nodes"] + kg["edges"]:
        una(obj["provenance"])
        for p in obj.get("provenances", []):
            if p is not obj["provenance"]:
                una(p)
    return stats


def titulos_oficiales_inventario(tos: list[str]) -> dict[str, str]:
    """U-R2-CODIGO-2, C2, punto n: el título oficial de cada TO, tal cual, sin
    el punto final, de las dos fuentes de `REF.titulos_de_inventario`
    (`inventario_tos.csv`, `titulo_oficial`; para los cinco de desarrollo,
    `inventario_resumen.json`, `subset_excluido`), sin normalizar: es la
    materia del TextoOrdenado. Frena si falta alguno."""
    import csv  # noqa: PLC0415
    tit = {r["id"]: r["titulo_oficial"] for r in csv.DictReader(REF.INVENTARIO_TITULOS.open(encoding="utf-8"))}
    for x in json.loads(REF.INVENTARIO_RESUMEN.read_text(encoding="utf-8"))["subset_excluido"]:
        tit[x["id_interno"]] = x["titulo"]
    faltan = [t for t in tos if t not in tit]
    if faltan:
        raise RuntimeError(f"TOs sin título en el inventario: {faltan}")
    return {t: re.sub(r"\.\s*$", "", tit[t].strip()) for t in tos}


def version_y_materia_r2b(kg: dict, canon: dict[str, str], e0_r2_dir: Path | None) -> dict:
    """U-R2-CODIGO-2, C2, punto n (fase r2b): `version` del TextoOrdenado = la
    versión vigente de `pies_<to>.json` de la E0 e0-r2 (el pie legible con la
    vigencia más reciente; en un empate, el de mayor número), con la forma
    «Comunicación A 8378 (vigencia 20/12/2025)»; `materia` = el título
    oficial del inventario (`titulos_oficiales_inventario`). Un TO sin
    `pies_<to>.json` o sin páginas legibles queda sin `version`, declarado.
    Lo que traía E1 queda en `originales`."""
    tit = titulos_oficiales_inventario(sorted(canon))
    nodos = {n["id"]: n for n in kg["nodes"]}
    filas, sin_version = {}, []
    for to in sorted(canon):
        n = nodos.get(canon[to])
        if n is None:
            continue
        pies = None
        if e0_r2_dir is not None and (Path(e0_r2_dir) / f"pies_{to}.json").exists():
            pies = json.loads((Path(e0_r2_dir) / f"pies_{to}.json").read_text(encoding="utf-8"))
        vig = (pies or {}).get("version_vigente")
        nuevos = {"materia": tit[to]}
        if vig:
            nuevos["version"] = vig["valor"]
        else:
            sin_version.append(to)
        props = n.setdefault("properties", {})
        for k, v in nuevos.items():
            previo = props.get(k)
            if previo is not None and previo != v:
                n.setdefault("originales", {}).setdefault(k, previo)
            props[k] = v
        if not vig and "version" in props:
            n.setdefault("originales", {}).setdefault("version", props.pop("version"))
        car = (pies or {}).get("caratula")
        filas[to] = {"id": n["id"], "materia": tit[to], "version": nuevos.get("version"),
                     "pagina_del_pie_vigente": (vig or {}).get("pagina"),
                     "caratula": (car or {}).get("ultima_comunicacion_incorporada"),
                     "coincide_con_la_caratula": (pies or {}).get("coincide_con_la_caratula")}
    return {"por_to": filas, "sin_version": sin_version,
            "coinciden_con_la_caratula": sum(1 for f in filas.values() if f["coincide_con_la_caratula"] is True),
            "no_coinciden_con_la_caratula": sorted(t for t, f in filas.items()
                                                   if f["coincide_con_la_caratula"] is False)}


def aristas_derivadas_de_cola(kg: dict, chunks_cola: set[str]) -> dict:
    """U-R2-CODIGO-2, C2, punto q (fase r2b): aristas sin la marca de la cola
    que tocan un nodo que solo viene de la cola humana (nodo con la marca y
    todas sus procedencias en chunks de la cola). Se cuentan aparte, después
    de derivar `remite_a` y `establecida_en`, por predicado; la arista no
    lleva marca (AristaR2 no la admite en esas aristas)."""
    def chunks_de(o):
        return {p.get("chunk_id") for p in o.get("provenances", [])}
    solo = {n["id"] for n in kg["nodes"] if (n.get("properties") or {}).get("cola_humana") == "true"
            and chunks_de(n) and chunks_de(n) <= chunks_cola}
    filas = [{"source": e["source"], "relation": e["relation"], "target": e["target"],
              "rol_fuente": e.get("rol_fuente"),
              "nodo_de_la_cola": [x for x in (e["source"], e["target"]) if x in solo]}
             for e in kg["edges"] if (e["source"] in solo or e["target"] in solo)
             and (e.get("properties") or {}).get("cola_humana") != "true"]
    filas.sort(key=lambda f: (f["source"], f["relation"], f["target"]))
    return {"nodos_solo_de_la_cola": len(solo), "aristas": len(filas),
            "por_predicado": C.conteo([{"r": f["relation"]} for f in filas], "r"), "filas": filas}


def sumar_paso_por_e3(conteos: list[dict]) -> dict:
    """U-R2-CODIGO-2, C2, punto s: suma de los conteos de
    `runner_corpus.conteo_paso_por_e3` de cada TO (claves numéricas y
    diccionarios de conteos, recursivamente)."""
    total: dict = {}
    for c in conteos:
        for k, v in c.items():
            if isinstance(v, dict):
                total[k] = sumar_paso_por_e3([total.get(k, {}), v])
            else:
                total[k] = total.get(k, 0) + v
    return {k: (dict(sorted(v.items())) if isinstance(v, dict) and k == "por_estado" else v)
            for k, v in total.items()}


def descartar_cola_r2(regs: list[dict], con_cola: bool) -> tuple[list[dict], list[str]]:
    """U-SINCOLA-T0, enmienda 1 al mandato (06/10/2026), punto 3.c: con
    `con_cola` False, los registros de la cola humana que devuelve
    `runner_corpus.entrada_r2` (`cola_humana` True) se descartan antes de
    `resolver_relaciones_r2` y de `ensamblar_r2`, en ese único punto; el
    registro de omisiones, el paso por E3, `cola_estados`, `flaggear_cola_r2`
    y `aristas_derivadas_de_cola` se computan sobre lo que queda. Con True, los
    registros vuelven tal cual. Devuelve (registros, chunk_ids descartados en
    el orden de E0)."""
    if con_cola:
        return regs, []
    return ([r for r in regs if not r.get("cola_humana")],
            [r["chunk_id"] for r in regs if r.get("cola_humana")])


def correr_cadena_r2(man: MC.Manifiesto, perfil, w=None, wl=None, tablas_dir: Path | None = None,
                     fase: str | None = None, con_cola: bool = True, cat_resolucion: dict | None = None) -> dict:
    """Cadena r2. `w(nombre, obj)` y `wl(nombre, filas)` escriben JSON y JSONL
    en <salida>/r2/ (None = no escriben). `fase`: «r2a» o «r2b»; por defecto,
    la del perfil del crudo (r2b con la forma r2). Pasarla explícita sirve a
    los controles (U-R2-CODIGO-2, C2): el crudo de r2a ensamblado con las
    reglas de r2b. Con r2b rigen además, solo en esta cadena, los puntos (m)
    a (s) de C2 de U-R2-CODIGO-2: versión y materia del TextoOrdenado (n),
    lista de umbrales completada (o), registro de omisiones (p), aristas
    derivadas que tocan un nodo de la cola contadas aparte (q), base con el
    detector de `remite_a` (r) y el conteo de elementos sin verificar por E3
    en el reporte (s); el plazo sin marcador (m) va por `llenar_umbrales_r2`.
    `con_cola` (U-SINCOLA-T0, enmienda 1, 06/10/2026): con False, los registros
    de la cola humana se descartan después de `entrada_r2`, en ese único punto
    (`descartar_cola_r2`), y lo que sigue se computa sobre lo que queda.
    `cat_resolucion` (R2 de U-RERESOL-CAT, W1): el catálogo de resolución de
    `r1_e4.catalogo_resolucion_r2`; reemplaza al del request en E4, en E2
    (labels y conjunto de ids) y en la normalización de los propuestos, y el
    resumen lleva sus tres versiones. Con None (default), la salida de siempre."""
    import runner_corpus as RC          # noqa: PLC0415 — solo con --perfil-r2
    w = w or (lambda *a, **k: None)
    wl = wl or (lambda *a, **k: None)
    M = E4.modulo_modelos_r2()
    V = E4.modulo_validador_r2()
    import reglas_comparacion as RCMP   # noqa: PLC0415 — pyd_r2/code, en el path por modulo_modelos_r2
    cat = cat_resolucion if cat_resolucion is not None else E4.catalogo_r2()
    validar, pol = RC.validador_perfil_r2(perfil)
    fase = fase or ("r2b" if RC.perfil_forma_r2(perfil) else "r2a")
    if fase not in e2_lib.FASES_R2:
        raise ValueError(f"fase desconocida: {fase!r}")
    r2b = fase == "r2b"
    versiones = {"catalogo_sha256": cat["catalogo_sha256"], "politica_sha256": pol.sha256,
                 "perfil": "r2", "prefijo_hash": perfil.prefijo_hash}
    resumen: dict = {"perfil_e1_del_crudo": perfil.nombre, **versiones, "etapas": []}
    if r2b:
        resumen["fase"] = fase
    resumen["con_cola"] = con_cola
    resumen["cola_descartada_por_to"] = {}
    if cat_resolucion is not None:
        resumen["catalogo_resolucion"] = cat_resolucion["versiones_catalogo"]
    omisiones: list[dict] = []
    paso_por_e3: dict[str, dict] = {}
    chunks_cola: set[str] = set()
    grafos, registro_total, resolucion_total, tramos_e1 = {}, [], [], {}
    conflictos_intra: list[dict] = []
    resumen["e2_por_to"] = {}
    for to in C.TOS_ORDEN:
        chunks = _chunks_r2(to)
        regs = RC.entrada_r2(to, C.SALIDA / to, chunks, perfil, validar)
        regs, descartadas = descartar_cola_r2(regs, con_cola)
        resumen["cola_descartada_por_to"][to] = {"n": len(descartadas), "chunks": descartadas}
        res = E4.resolver_relaciones_r2(regs, cat["indice"], cat["rol_por_to"], versiones)
        ens = e2_lib.ensamblar_r2(chunks, regs, cat["labels"], sujetos_de_resolucion(cat, M), M.firma_r2,
                                  M.TIPOS_ENTIDAD, M.PREDICADOS, res["registro"], fase=fase)
        grafos[to] = {"nodes": ens["nodes"], "edges": ens["edges"]}
        cola_estados = {r["chunk_id"]: r["estado_e3"] for r in regs if r.get("cola_humana")}
        if r2b:
            # puntos p y s: el registro de omisiones (lo lee LN-7) y el conteo de elementos sin verificar por E3
            omisiones += [{"chunk_id": r["chunk_id"], "to": to, **o} for r in regs
                          for o in (r.get("validacion") or {}).get("omisiones", [])]
            paso_por_e3[to] = RC.conteo_paso_por_e3(regs)
            chunks_cola |= set(cola_estados)
        r_cola = e2_lib.flaggear_cola_r2(grafos[to], cola_estados)
        tramos_e1.update(ens["tramos_umbral"])
        conflictos_intra += [{**c, "to": to} for c in ens["conflictos_properties"]]
        wl(f"por_to/{to}/no_mapeados_sujetos.jsonl", res["registro"])
        wl(f"por_to/{to}/resolucion_sujetos.jsonl", res["resolucion"])
        registro_total += res["registro"]
        resolucion_total += res["resolucion"]
        resumen["e2_por_to"][to] = {
            "nodes": len(ens["nodes"]), "edges": len(ens["edges"]),
            "origen_crudo": C.conteo([{"o": r["origen_crudo"]} for r in regs], "o"),
            "rechazados": sum(1 for r in regs if r.get("validacion") is None),
            "rechazos_validador": sum(len((r.get("validacion") or {}).get("rechazos", [])) for r in regs),
            "relaciones_no_verificadas_e3": sum(1 for r in regs for x in (r.get("validacion") or {}).get(
                "relaciones", []) if x.get("no_verificada_e3")),
            "cola_flaggeada": r_cola, "stats": ens["stats"], "rechazos_e2": len(ens["rechazos_e2"]),
            "conflictos_properties": len(ens["conflictos_properties"]), "resolucion_sujetos": res["resumen"]}
    resumen["etapas"].append("entrada_r2+sujetos+e2")
    print("[e2-r2]", json.dumps({to: (v["nodes"], v["edges"]) for to, v in resumen["e2_por_to"].items()}),
          flush=True)

    m = INV.merge_grafos_guardado(grafos)
    kg = {"nodes": m["nodes"], "edges": m["edges"]}
    inv = INV.verificar_invariantes(kg, m["grafos_pre_merge"], merges_nodo=len(m["merges_cross_to"]),
                                    merges_arista=INV.merges_arista_de(m["grafos_pre_merge"], kg["edges"]))
    assert inv["ok"], inv["fallos"]
    if r2b:
        r_prop = normalizar_propuestos_r2b(kg, registro_total, m["renombres"], cat)
        resumen["propuestos_r2b"] = r_prop["resumen"]
        wl("propuestos_descartados_aristas_quitadas.jsonl", r_prop["aristas_quitadas"])
    resumen["merge"] = {"merges_cross_to": len(m["merges_cross_to"]),
                        "nodos_con_colision_cross_to": sum(1 for n in kg["nodes"] if n.get("properties", {}).get(
                            "colision_cross_to") == "true"),
                        "adjudicacion_cross_to": len(m["adjudicacion_cross_to"]),
                        "conflictos_cross_to": len(m["conflictos"])}
    w("adjudicacion_cross_to.json", m["adjudicacion_cross_to"])

    r_to = E4.canonizar_texto_ordenado(kg)
    r_conf = E4.filtrar_conflictos(conflictos_intra, m["conflictos"])
    catalogo = C.cargar_catalogo()
    # U-R2-CODIGO-2, C2, punto e: la pasada residual de E4 se retira del perfil r2 (decisión 1 del mandato; en
    # la medición de r2a propuso 0 resoluciones sobre 24 propuestos). La clave queda, marcada como retirada,
    # porque la lee medicion_r2a/m2_medicion.py.
    resumen["e4"] = {"texto_ordenado": {"canonicos": r_to["canonicos"], "eliminados": len(r_to["eliminados"])},
                     "conflictos_cross_to": {k: v for k, v in r_conf.items()
                                             if k in ("n_total", "n_variantes_to", "n_reales")},
                     "pasada_residual_de_propuestos_medida_no_aplicada": {
                         "retirada": True, "motivo": "retirada del perfil r2 (U-R2-CODIGO-2, decisión 1 del "
                                                     "mandato): en r2a propuso 0 resoluciones sobre 24 propuestos"}}
    w("e4_texto_ordenado.json", r_to)
    w("e4_conflictos.json", r_conf)
    canon = {to: E4.id_texto_ordenado_canonico(C.archivo_de_to(to)) for to in C.TOS_ORDEN}
    if r2b:
        resumen["texto_ordenado_version_materia"] = version_y_materia_r2b(kg, canon, tablas_dir)

    r_esq = inyectar_esqueleto_v3(kg, catalogo)
    resumen["esqueleto"] = {k: v for k, v in r_esq.items() if k not in ("ids_creados", "paridad_kg_refinado")}
    inv = INV.verificar_invariantes(kg)
    assert inv["ok"], inv["fallos"]

    partes = {c["id"]: c for to in C.TOS_ORDEN for c in _chunks_r2(to) if "sub_chunk" in c}
    r_ref = REF.detectar_y_resolver(kg, perfil="r2", chunks_e0_r2=_chunks_e0_r2(tablas_dir),
                                    chunks_partes=partes or None)
    resumen["remite_a"] = r_ref["resumen"]
    tipo_de = {n["id"]: n["type"] for n in kg["nodes"]}
    resumen["referencia_con_origen_distinto_de_texto_ordenado"] = sum(
        1 for e in kg["edges"] if e["relation"] == "referencia" and tipo_de[e["source"]] != "TextoOrdenado")
    resumen["comunicaciones"] = {k: v for k, v in r_ref["comunicaciones"].items() if k != "filas"}
    w("remisiones_registro.json", r_ref["registro"])
    w("comunicaciones_registro.json", r_ref["comunicaciones"])

    resumen["establecida_en_derivada"] = derivar_establecida_en(kg, canon)
    if r2b:
        r_der = aristas_derivadas_de_cola(kg, chunks_cola)
        resumen["aristas_derivadas_que_tocan_un_nodo_solo_de_la_cola"] = {k: v for k, v in r_der.items()
                                                                         if k != "filas"}
        w("aristas_derivadas_cola_humana.json", r_der["filas"])
        wl("omisiones.jsonl", omisiones)
        resumen["omisiones"] = {"filas": len(omisiones), "por_categoria": C.conteo(omisiones, "categoria")}
        resumen["paso_por_e3"] = {"por_to": paso_por_e3, "total": sumar_paso_por_e3(list(paso_por_e3.values()))}

    r_umb = llenar_umbrales_r2(kg, tramos_e1, _celdas_por_chunk(tablas_dir), M, V, RCMP, pol, fase)
    resumen["umbrales"] = r_umb["resumen"]
    w("umbrales_rangos_unidad_repetida.json", r_umb["rangos"])
    if r2b:
        r_nc = marcar_umbral_no_cuantificable_r2b(kg, tramos_e1, _celdas_por_tabla(tablas_dir), RCMP)
        resumen["umbral_no_cuantificable"] = r_nc["resumen"]
        w("umbral_no_cuantificable.json", {"marcados": r_nc["filas"], "sin_marca_con_cuantia": r_nc["sin_marca"]})

    resumen["procedencia"] = enriquecer_procedencias_r2(kg)
    inv = INV.verificar_invariantes(kg)
    assert inv["ok"], inv["fallos"]

    resumen["registro_no_mapeados"] = {
        "filas": len(registro_total), "por_estado": C.conteo([{"e": f["estado"]} for f in registro_total], "e"),
        "por_motivo": C.conteo([{"m": f["motivo"]} for f in registro_total], "m"),
        "cuarentena_sin_nodo": sum(1 for f in registro_total if f["estado"] == "cuarentena" and not f.get("id_nodo")),
        "propuestos_en_grafo_sin_fila": sorted(
            n["id"] for n in kg["nodes"] if n["type"] == "Sujeto" and n["properties"].get("nivel") == "propuesto"
            and n["id"] not in {f.get("id_nodo") for f in registro_total})}
    wl("no_mapeados_sujetos.jsonl", registro_total)
    wl("resolucion_sujetos.jsonl", resolucion_total)
    resumen["resolucion_sujetos"] = {
        "relaciones_de_sujeto": len(resolucion_total),
        "por_metodo": C.conteo([{"m": f["metodo_resolucion"]} for f in resolucion_total], "m"),
        "desacuerdos_regla_modelo": sum(f["desacuerdo_regla_modelo"] for f in resolucion_total)}


    kg["nodes"].sort(key=lambda n: n["id"])
    kg["edges"].sort(key=lambda e: (e["source"], e["relation"], e["target"]))
    tipo = {n["id"]: n["type"] for n in kg["nodes"]}
    con_arista = {e["source"] for e in kg["edges"]} | {e["target"] for e in kg["edges"]}
    resumen["aislados_por_tipo"] = C.conteo([{"t": n["type"]} for n in kg["nodes"] if n["id"] not in con_arista], "t")
    resumen["aristas_no_verificadas_e3"] = {
        "total": sum(1 for e in kg["edges"] if e.get("no_verificada_e3")),
        "por_firma": C.conteo([{"f": f"{tipo[e['source']]}-{e['relation']}-{tipo[e['target']]}"}
                               for e in kg["edges"] if e.get("no_verificada_e3")], "f")}
    resumen["validacion_modelos_r2"] = validar_grafo_r2(kg, M)
    kg_json = C.dumps_kg(kg)
    return {"kg": kg, "kg_json": kg_json, "sha256": C.sha256_bytes(kg_json.encode("utf-8")), "resumen": resumen}


def _chunks_r2(to: str) -> list[dict]:
    """Chunks de E0 del TO para la cadena r2: con las unidades partidas por
    corte en E1 (runner_corpus.py --perfil-r2, R4.b; particiones_por_corte.json
    de la salida del TO) reemplazadas por sus partes. Sin particiones, los de
    E0."""
    import runner_corpus as RC          # noqa: PLC0415 — solo con --perfil-r2
    return RC.chunks_con_partes(C.cargar_chunks_enm01(to), C.SALIDA / to)


def _chunks_e0_r2(e0_r2_dir: Path | None) -> dict[str, dict] | None:
    """chunk_id → chunk de e0-r2 (chunks_<to>.json de `correr_e0.py
    --version-e0 e0-r2`), para detectar las remisiones sobre su texto (regla b
    del perfil r2); None sin el directorio."""
    if e0_r2_dir is None:
        return None
    out: dict[str, dict] = {}
    for to in C.TOS_ORDEN:
        p = Path(e0_r2_dir) / f"chunks_{to}.json"
        if not p.exists():
            continue
        d = json.loads(p.read_text(encoding="utf-8"))
        for c in d["chunks"] if isinstance(d, dict) else d:
            out[c["id"]] = c
    return out


def _celdas_por_chunk(tablas_dir: Path | None) -> dict[str, list[str]]:
    """chunk_id → textos de celdas de las tablas de e0-r2 (tablas_<to>.json de
    `correr_e0.py --version-e0 e0-r2`); vacío sin el directorio."""
    out: dict[str, list[str]] = {}
    if tablas_dir is None:
        return out
    for to in C.TOS_ORDEN:
        p = Path(tablas_dir) / f"tablas_{to}.json"
        if not p.exists():
            continue
        for t in json.loads(p.read_text(encoding="utf-8"))["tablas"]:
            celdas = [str(c) for s in t.get("segmentos", []) for f in s.get("filas", []) for c in f if c]
            for cid in t.get("chunks", []):
                out.setdefault(cid, []).extend(celdas)
    return out


def validar_grafo_r2(kg: dict, M) -> dict:
    """Cada nodo con NodoR2 y cada arista con AristaR2 (pyd_r2), y la firma de
    cada arista con los tipos de sus extremos (modelos_r2.firma_arista: matriz
    r2, remite_a y esqueleto). Devuelve los conteos fuera del modelo, que deben
    ser 0, y los primeros errores."""
    from pydantic import ValidationError  # noqa: PLC0415
    tipo = {n["id"]: n["type"] for n in kg["nodes"]}
    nodos_fuera, aristas_fuera = [], []
    for n in kg["nodes"]:
        try:
            M.NodoR2.model_validate(n)
        except ValidationError as e:
            nodos_fuera.append({"objeto": n["id"], "error": str(e).splitlines()[0:3]})
    for e in kg["edges"]:
        clave = f"{e['source']}|{e['relation']}|{e['target']}"
        try:
            M.AristaR2.model_validate(e)
        except ValidationError as x:
            aristas_fuera.append({"objeto": clave, "error": str(x).splitlines()[0:3]})
            continue
        if not M.firma_arista(tipo[e["source"]], e["relation"], tipo[e["target"]]):
            aristas_fuera.append({"objeto": clave, "error": [f"firma {tipo[e['source']]} --{e['relation']}--> "
                                                             f"{tipo[e['target']]}"]})
    return {"nodos": len(kg["nodes"]), "aristas": len(kg["edges"]), "nodos_fuera_del_modelo": len(nodos_fuera),
            "aristas_fuera_del_modelo": len(aristas_fuera), "primeros": (nodos_fuera + aristas_fuera)[:20]}


def ensamblar_manifiesto_r2(man: MC.Manifiesto, entrada: Path, salida: Path,
                            tablas_dir: Path | None = None, con_cola: bool = True,
                            cat_resolucion: dict | None = None) -> dict:
    """`con_cola` (U-SINCOLA-T0, enmienda 1 al mandato, 06/10/2026): con False,
    las dos corridas de `correr_cadena_r2` descartan los registros de la cola
    humana (`descartar_cola_r2`); el reporte declara `con_cola` y las unidades
    descartadas por TO. Con True (default), la salida de siempre.
    `cat_resolucion` (R2 de U-RERESOL-CAT, W1): el catálogo de resolución, en
    las redirecciones (esqueleto y conjunto de ids del merge entre TOs) y en las
    dos corridas; el reporte lleva sus tres versiones. Con None (default), el
    catálogo del request, como siempre."""
    perfil = perfil_e1.perfil(man.perfil_e1)
    entrada, salida = Path(entrada), Path(salida)
    salida_r2 = salida / "r2"
    M = E4.modulo_modelos_r2()
    cat = cat_resolucion if cat_resolucion is not None else E4.catalogo_r2()
    plan = plan_redirecciones_r2(man, perfil, entrada, salida_r2, cat, M)

    def w(nombre: str, obj) -> None:
        p = salida_r2 / nombre
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(obj, ensure_ascii=False, indent=1), encoding="utf-8")

    def wl(nombre: str, filas: list[dict]) -> None:
        p = salida_r2 / nombre
        p.parent.mkdir(parents=True, exist_ok=True)
        with p.open("w", encoding="utf-8") as f:
            for r in filas:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")

    with redirigido(plan):
        print("=== cadena r2, corrida 1 ===", flush=True)
        a = correr_cadena_r2(man, perfil, w, wl, tablas_dir, con_cola=con_cola, cat_resolucion=cat_resolucion)
        print("=== cadena r2, corrida 2 (sin escribir) ===", flush=True)
        b = correr_cadena_r2(man, perfil, None, None, tablas_dir, con_cola=con_cola, cat_resolucion=cat_resolucion)
    salida_r2.mkdir(parents=True, exist_ok=True)
    (salida_r2 / "kg.json").write_text(a["kg_json"], encoding="utf-8")
    reporte = {"grafo": f"{man.nombre}/r2", "perfil": "r2",
               "manifiesto": {"nombre": man.nombre, "path": _rel(man.path), "perfil_e1": man.perfil_e1,
                              "orden_corrida": list(man.orden_corrida), "e0_salida": _rel(man.e0_salida)},
               "entrada": _rel(entrada), "tablas_e0_r2": _rel(tablas_dir) if tablas_dir else None,
               "sha256_kg": a["sha256"], "sha256_kg_en_disco": C.sha256_path(salida_r2 / "kg.json"),
               "doble_corrida_byte_identica": a["kg_json"] == b["kg_json"],
               "nodes_total": len(a["kg"]["nodes"]), "edges_total": len(a["kg"]["edges"]),
               "nodes_by_type": C.conteo(a["kg"]["nodes"], "type"),
               "edges_by_relation": C.conteo(a["kg"]["edges"], "relation"),
               "redirecciones": describir_plan(plan), **a["resumen"]}
    w("reporte_ensamblado_r2.json", reporte)
    return {"r2": {k: reporte[k] for k in ("sha256_kg", "sha256_kg_en_disco", "doble_corrida_byte_identica",
                                            "nodes_total", "edges_total")},
            "validacion_modelos_r2": reporte["validacion_modelos_r2"]}


# ------------------------------------------------------------------------- #
# Selftest sobre el corpus de desarrollo (verdad conocida)                   #
# ------------------------------------------------------------------------- #
def selftest_dev(man: MC.Manifiesto, entrada: Path, salida: Path, resultado: dict) -> dict:
    """Comprueba, con perfil dev: (1) kg.json == 8e2eadee…; (2) r1/kg.json ==
    0226e947…; (3) réplica ≡ ensamblar_r1.correr directo (mismo kg_json);
    (4) inyector v3 local ≡ r1_e5_esqueleto.inyectar_esqueleto cuando ambos
    apuntan al catálogo v2 (mismo kg tras el esqueleto); (5) las redirecciones
    dev son identidad (inventario de remisión y orden iguales a los cableados)."""
    perfil = perfil_e1.perfil(man.perfil_e1)
    assert perfil.nombre == "produccion_dev", "el selftest de verdad conocida es del corpus de desarrollo"
    checks = {}
    checks["kg_e5_byte_identico_8e2eadee"] = (resultado["e5"]["sha256_kg"] == SELLOS_DEV["kg_e5"]
                                              and C.sha256_path(Path(salida) / "kg.json") == SELLOS_DEV["kg_e5"])
    checks["kg_r1_byte_identico_0226e947"] = (resultado["r1"]["sha256_kg"] == SELLOS_DEV["kg_r1"]
                                              and C.sha256_path(Path(salida) / "r1" / "kg.json") == SELLOS_DEV["kg_r1"])
    checks["cmp_con_salida_kg"] = ((Path(salida) / "kg.json").read_bytes()
                                   == (CORPUS_V2 / "salida" / "kg.json").read_bytes())
    checks["cmp_con_salida_r1_kg"] = ((Path(salida) / "r1" / "kg.json").read_bytes()
                                      == (CORPUS_V2 / "salida_r1" / "kg.json").read_bytes())

    plan = plan_redirecciones(man, perfil, entrada, Path(salida) / "r1")
    inv_man = inventario_desde_manifiesto(man)
    checks["inventario_remision_igual_al_cableado"] = inv_man == REF.INVENTARIO_TOS
    checks["orden_igual_al_cableado"] = tuple(man.orden_corrida) == C.TOS_ORDEN == EC.TOS_ORDEN
    # en dev, catálogo y conjunto de sujetos del plan son los cableados (identidad)
    valores = {(m.__name__, a): v for m, a, v in plan}
    checks["catalogo_dev_sin_cambio"] = (
        valores[("r1_comun", "CATALOGO_PATH")] == C.CATALOGO_PATH
        and valores[("assemble", "CATALOGO_PATH")] == assemble.CATALOGO_PATH
        and valores[("r1_invariantes", "SUJETOS_CATALOGO_SET")] == INV.SUJETOS_CATALOGO_SET
        and Path(entrada).resolve() == C.SALIDA.resolve()
        and Path(man.e0_salida).resolve() == C.E0_ENM01.resolve())
    with redirigido(plan):
        directo = correr_motor_ensamblar_r1(perfil, True, "final")
        replica = correr_cadena(perfil, True, "final", None)
        checks["replica_igual_a_ensamblar_r1_correr"] = (directo["kg_json"] == replica["kg_json"]
                                                          and directo["sha256"] == SELLOS_DEV["kg_r1"])
        # (4) inyector local vs r1_e5_esqueleto sobre el catálogo v2
        base = correr_cadena(perfil, True, "e4", None)
        kg_a, kg_b = deepcopy(base["kg"]), deepcopy(base["kg"])
        catalogo = C.cargar_catalogo()
        ra = E5.inyectar_esqueleto(kg_a, catalogo)
        rb = inyectar_esqueleto_v3(kg_b, catalogo)   # con assemble.CATALOGO_PATH = v2 (dev)
        checks["inyector_local_igual_a_r1_e5_esqueleto"] = C.dumps_kg(kg_a) == C.dumps_kg(kg_b)
        checks["inyector_local_mismo_reporte_salvo_paridad"] = (
            {k: v for k, v in ra.items() if k != "paridad_kg_refinado"}
            == {k: v for k, v in rb.items() if k != "paridad_kg_refinado"})
    checks["ok"] = all(v for k, v in checks.items())
    return checks


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--manifiesto", type=Path, required=True, help="manifiesto de ensamblado (JSON)")
    ap.add_argument("--entrada", type=Path, required=True,
                    help="directorio con las salidas E1→E3 por TO (runner_corpus.py --salida)")
    ap.add_argument("--salida", type=Path, required=True, help="directorio de salida del ensamblado")
    ap.add_argument("--hasta", choices=ETAPAS, default="final")
    ap.add_argument("--sin-cola", action="store_true",
                    help="no inyectar la cola flaggeada (r1 corrió CON cola: default con cola); en la cadena r2 "
                         "(U-SINCOLA-T0, enmienda 1) descarta los registros de la cola humana después de entrada_r2")
    ap.add_argument("--motor", choices=("replica", "ensamblar_r1"), default="replica",
                    help="replica (default) = cadena r1 paso a paso; ensamblar_r1 = ensamblar_r1.correr "
                         "directo (solo perfil produccion_dev)")
    ap.add_argument("--selftest-dev", action="store_true",
                    help="tras ensamblar, verificar la verdad conocida del corpus de desarrollo")
    ap.add_argument("--resumen-json", type=Path, default=None, help="escribir el resumen de la corrida acá")
    ap.add_argument("--perfil-r2", action="store_true",
                    help="U-R2-CODIGO R3: cadena r2 (validador, política y catálogo r2) sobre la salida "
                         "guardada, en <salida>/r2/; no corre la cadena r1 ni el E5")
    ap.add_argument("--e0-r2", "--tablas-e0-r2", dest="tablas_e0_r2", type=Path, default=None,
                    help="con --perfil-r2: salida de correr_e0.py --version-e0 e0-r2 (chunks_<to>.json y "
                         "tablas_<to>.json): texto de las remisiones y verificación de umbrales contra las tablas")
    ap.add_argument("--catalogo-resolucion", dest="catalogo_resolucion", type=Path, default=None,
                    help="solo en la cadena r2 (R2 de U-RERESOL-CAT, W1): directorio con los generados del catálogo "
                         "de resolución (r1_e4.catalogo_resolucion_r2, con su candado); sin la opción, el catálogo "
                         "del request, como siempre")
    args = ap.parse_args()

    man = MC.cargar(args.manifiesto)
    # U-PROMPT-R2 (decisión 1 del mandato): un manifiesto con un perfil de forma «r2» (r2b) corre la cadena r2,
    # como --perfil-r2, con las tablas de su propia E0 (e0-r2) salvo que se indique otra. Los perfiles existentes
    # siguen con el camino por defecto.
    esq = perfil_e1.perfil(man.perfil_e1).esquema
    forma_r2 = esq is not None and getattr(esq, "forma_salida", "v3") == "r2"
    if args.perfil_r2 or forma_r2:
        tablas = args.tablas_e0_r2 if args.tablas_e0_r2 is not None else (man.e0_salida if forma_r2 else None)
        cat_res = (E4.catalogo_resolucion_r2(args.catalogo_resolucion) if args.catalogo_resolucion is not None
                   else None)
        res = ensamblar_manifiesto_r2(man, args.entrada, args.salida, tablas, con_cola=not args.sin_cola,
                                      cat_resolucion=cat_res)
        print(json.dumps(res, ensure_ascii=False, indent=1))
        if args.resumen_json:
            args.resumen_json.parent.mkdir(parents=True, exist_ok=True)
            args.resumen_json.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
        return 0 if res["r2"]["doble_corrida_byte_identica"] else 1
    if args.catalogo_resolucion is not None:
        ap.error("--catalogo-resolucion es solo de la cadena r2")
    res = ensamblar_manifiesto(man, args.entrada, args.salida, hasta=args.hasta,
                               con_cola=not args.sin_cola, motor=args.motor)
    if args.selftest_dev:
        res["selftest_dev"] = selftest_dev(man, args.entrada, args.salida, res)
    print(json.dumps({k: v for k, v in res.items() if k != "redirecciones"}, ensure_ascii=False, indent=1))
    if args.resumen_json:
        args.resumen_json.parent.mkdir(parents=True, exist_ok=True)
        args.resumen_json.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    ok = res.get("r1", {}).get("invariantes_ok", True)
    if "selftest_dev" in res:
        ok = ok and res["selftest_dev"]["ok"]
    if args.hasta == "final":
        ok = ok and res["r1"]["doble_corrida_byte_identica"]
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
