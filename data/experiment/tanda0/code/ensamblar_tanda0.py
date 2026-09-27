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
                    help="no inyectar la cola flaggeada (r1 corrió CON cola: default con cola)")
    ap.add_argument("--motor", choices=("replica", "ensamblar_r1"), default="replica",
                    help="replica (default) = cadena r1 paso a paso; ensamblar_r1 = ensamblar_r1.correr "
                         "directo (solo perfil produccion_dev)")
    ap.add_argument("--selftest-dev", action="store_true",
                    help="tras ensamblar, verificar la verdad conocida del corpus de desarrollo")
    ap.add_argument("--resumen-json", type=Path, default=None, help="escribir el resumen de la corrida acá")
    args = ap.parse_args()

    man = MC.cargar(args.manifiesto)
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
