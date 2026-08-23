"""
selftest_r1.py — SELFTEST OFFLINE de U-B1.8 (fase A, $0, sin API).

Cubre los seis puntos del mandato con un cliente FALSO scripteado (patrón
selftest_ev2 de la corrida base), ejercitando el circuito REAL sobre r1:

  1. CARGA: r1 verificado por sha256 (4/4 grafos con el registro en memoria),
     vista runtime con el adaptador de provenance (conteos crudos, mapeo
     {archivo,punto} -> {source_doc,location}, aristas nuevas presentes).
  2. ORDEN: semilla orden-ev2-r1 determinística, 40 casos únicos, persistencia
     idempotente.
  3. PERSISTENCIA: runner_ev2.correr_grafo sobre r1 con cliente falso —
     metadata completa (kg_sha256 de r1), steps_full sin truncar, raw_turns
     1:1 con llamadas API, fidelidad sin evaluar, replay 100 % caché con
     cliente que explota.
  4. MAPPING: mapping §2/§4 (casos de respuesta conocida), pipeline_fidelidad.
     agregar sobre veredictos scripteados del juez, y agregar_par del §7
     (mayoría / empate triple -> parcial / invariancia con ADJ).
  5. 0 CROSS-HITS PROVOCADO: (a) compartir db+namespace produce hit detectado
     en access_log (por eso cada rep lleva db propia); (b) el detector
     verificar_cross_hits reporta >0 ante dbs con keys en común y 0 con dbs
     disjuntas.
  6. REPLAY CON LAS ARISTAS NUEVAS DE r1: ver_vecinos sirve aristas
     `referencia` (B1.3) y de esqueleto (`subclase_de`, B1.1); el replay
     estándar (metrica.evaluar_traza) y el FUERTE (metrica_ev2.
     verificar_steps_full) las reproducen; un nodo alcanzado SOLO a través de
     una arista `referencia` cuenta como consultado vía ver_vecinos.

Todo se escribe bajo selftest_out/ y cache/ (gitignorados).

Uso:  .venv/bin/python -B data/experiment/ev2_r1/code/selftest_r1.py
"""

from __future__ import annotations

import json
import shutil
import sqlite3
import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_r1 as cr                      # noqa: E402  (registra r1 al importarse)
import comun_ev2 as ce                     # noqa: E402
import runner_ev2 as rv                    # noqa: E402
import pipeline_fidelidad as pf            # noqa: E402
import agregacion_enc as ag                # noqa: E402
from comun_r1 import mapping               # noqa: E402
import llm_cache as lc                     # noqa: E402  (vía sys.path del cuarteto)
from harness import GraphIndex             # noqa: E402
from metrica import evaluar_traza          # noqa: E402
from metrica_ev2 import verificar_steps_full  # noqa: E402
from anthropic.types import Message        # noqa: E402

SELFTEST_DIR = cr.SELFTEST_DIR
DB_PATH = cr.CACHE_DIR / "ev2_r1_selftest.db"
LABEL = "ev2_r1_selftest"

_checks = []


def check(nombre, cond):
    _checks.append((nombre, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {nombre}")


# --------------------------------------------------------------------------- #
# Cliente falso (patrón selftest_ev2)                                          #
# --------------------------------------------------------------------------- #
def _msg(content, stop_reason):
    return Message.model_validate({
        "id": "msg_selftest_r1", "type": "message", "role": "assistant",
        "model": "claude-haiku-4-5-20251001", "content": content,
        "stop_reason": stop_reason, "stop_sequence": None,
        "usage": {"input_tokens": 1500, "output_tokens": 60,
                  "cache_read_input_tokens": 0,
                  "cache_creation_input_tokens": 1200},
    })


def turno_tool(nombre, args, uid):
    return _msg([{"type": "text", "text": "Exploro el grafo."},
                 {"type": "tool_use", "id": uid, "name": nombre, "input": args}],
                "tool_use")


def turno_final(respuesta):
    txt = json.dumps({"respuesta": respuesta, "citas": [], "respondible": True},
                     ensure_ascii=False)
    return _msg([{"type": "text", "text": txt}], "end_turn")


class FakeSequential:
    def __init__(self, script):
        self.script = list(script)
        self.calls = 0
        self.messages = self

    def create(self, **kwargs):
        if self.calls >= len(self.script):
            raise AssertionError("llamada API no prevista en el selftest")
        m = self.script[self.calls]
        self.calls += 1
        return m


class ExplodingClient:
    def __init__(self):
        self.messages = self

    def create(self, **kwargs):
        raise AssertionError("el replay llamó al cliente real (cache miss)")


# --------------------------------------------------------------------------- #
# Elección determinística de nodos con las aristas nuevas                       #
# --------------------------------------------------------------------------- #
def elegir_nodos(index: GraphIndex, aidx) -> dict:
    """(a) una arista `referencia` cuyo TARGET porta un ancla que resuelve a él
    (no contenedor) y cuyo source la sirve entre sus primeros 40 salientes;
    (b) una arista `subclase_de` (esqueleto). Primeras en orden de aparición."""
    kg = json.loads(cr.R1["path"].read_text(encoding="utf-8"))
    por_id = {n["id"]: n for n in kg["nodes"]}
    ref = None
    for e in kg["edges"]:
        if e["relation"] != "referencia":
            continue
        src, tgt = e["source"], e["target"]
        p = (por_id.get(tgt) or {}).get("provenance") or {}
        punto, to = (p.get("punto") or ""), (p.get("to") or "")
        if not punto or not to:
            continue
        if tgt not in aidx.resolver(to, punto):
            continue                      # contenedor o ancla que no resuelve a él
        sal = index.ver_vecinos(src, "salientes")
        if "error" in sal:
            continue
        if any(v["vecino_id"] == tgt and v["relation"] == "referencia"
               for v in sal.get("salientes", [])):
            ref = {"source": src, "target": tgt, "to": to, "punto": punto}
            break
    esq = None
    for e in kg["edges"]:
        if e["relation"] == "subclase_de":
            ent = index.ver_vecinos(e["target"], "entrantes")
            if "error" not in ent and any(
                    v["vecino_id"] == e["source"] and v["relation"] == "subclase_de"
                    for v in ent.get("entrantes", [])):
                esq = {"source": e["source"], "target": e["target"]}
                break
    if not ref or not esq:
        raise RuntimeError(f"no se encontraron aristas de prueba: ref={ref} esq={esq}")
    return {"ref": ref, "esq": esq}


# --------------------------------------------------------------------------- #
# Selftest                                                                     #
# --------------------------------------------------------------------------- #
def main() -> int:
    print("== SELFTEST OFFLINE U-B1.8 (sin API, $0) ==")
    if SELFTEST_DIR.exists():
        shutil.rmtree(SELFTEST_DIR)
    SELFTEST_DIR.mkdir(parents=True)
    cr.CACHE_DIR.mkdir(parents=True, exist_ok=True)
    for p in list(cr.CACHE_DIR.glob("ev2_r1_selftest*.db")) \
            + list(cr.CACHE_DIR.glob("selftest_cross_*.db")):
        p.unlink()

    # --- 1) CARGA ---
    sellos = cr.verificar_sellos()
    check("sellos: cuarteto + juez v1 + gold + 4/4 grafos (incluye r1)",
          sellos["prompt_juez_v1.md"] == cr.cf.PROMPT_SHA256_ESPERADO
          and sellos["grafo_r1"] == cr.R1["sha256"])
    kg_rt = ce.cargar_runtime("r1")
    check("runtime r1: conteos crudos 6529/17772",
          kg_rt.raw_node_count == 6529 and kg_rt.raw_edge_count == 17772)
    n0 = kg_rt.nodes[0]
    check("runtime r1: provenance primaria mapeada a {source_doc, location}",
          n0.provenances and set(n0.provenances[0]) == {"source_doc", "location"}
          and (n0.provenances[0]["location"].startswith("Punto ")
               or n0.provenances[0]["location"].startswith("Sección ")))
    rels = {e.relation for e in kg_rt.edges}
    check("runtime r1: aristas nuevas presentes (referencia + subclase_de)",
          "referencia" in rels and "subclase_de" in rels)
    check("registro en memoria: runner_ev2 ve r1 en GRAFOS y su runtime",
          rv.GRAFOS is ce.GRAFOS and "r1" in rv.GRAFOS
          and rv.cargar_runtime("r1").raw_node_count == 6529)

    # --- 2) ORDEN ---
    c1, c2 = cr.casos_fidelidad_r1(), cr.casos_fidelidad_r1()
    ids1 = [c["caso_id"] for c in c1]
    check("orden: determinístico (dos derivaciones idénticas)",
          ids1 == [c["caso_id"] for c in c2])
    check("orden: 40 casos únicos, todos EV2F-*",
          len(set(ids1)) == 40 and all(i.startswith("EV2F-") for i in ids1))
    check("orden: la semilla baraja (orden distinto del ordenado)",
          ids1 != sorted(ids1))
    p_ord = cr.persistir_orden(c1)
    check("orden: persistido e idempotente", p_ord.exists()
          and cr.persistir_orden(c1) == p_ord)

    # --- guion sobre r1 con las aristas nuevas ---
    index = GraphIndex(kg_rt)
    aidx = cr.indice_anclas_r1()
    nodos = elegir_nodos(index, aidx)
    ref, esq = nodos["ref"], nodos["esq"]
    print(f"  aristas de prueba: referencia {ref['source']} -> {ref['target']} "
          f"(ancla {ref['to']}:{ref['punto']}); subclase_de {esq['source']} -> {esq['target']}")
    casos = [dict(c1[0]), dict(c1[1])]
    script = [
        # caso 1: buscar + ver_vecinos salientes del source (sirve la arista
        # `referencia`; el TARGET queda consultado SOLO por esa arista)
        turno_tool("buscar_nodos", {"consulta": "selftest r1", "limite": 10}, "t1"),
        turno_tool("ver_vecinos", {"id": ref["source"], "direccion": "salientes"}, "t2"),
        turno_final("dry run r1 caso 1"),
        # caso 2: ver_vecinos entrantes del padre de esqueleto (sirve `subclase_de`)
        turno_tool("ver_vecinos", {"id": esq["target"], "direccion": "entrantes"}, "t3"),
        turno_final("dry run r1 caso 2"),
    ]

    # --- 3) PERSISTENCIA (runner real sobre r1, cliente falso) ---
    fake = FakeSequential(script)
    outdir = SELFTEST_DIR / "trazas"
    resumen = rv.correr_grafo("r1", client_real=fake, db_path=DB_PATH,
                              label=LABEL, casos=casos, outdir=outdir)
    check("runner: guion consumido completo y 2 casos corridos",
          fake.calls == len(script) and resumen["n_casos_corridos"] == 2)
    payloads = {}
    for c in casos:
        with (outdir / f"{rv._sanitizar(c['caso_id'])}.json").open(encoding="utf-8") as f:
            payloads[c["caso_id"]] = json.load(f)
    META_KEYS = {"unidad", "label", "grafo", "kg_path", "kg_sha256", "eje", "caso_id",
                 "pos_orden_global", "pos_orden_efectivo", "semilla_orden", "n_rep",
                 "model", "temperature", "max_tool_calls", "thinking_enabled",
                 "timestamp_inicio", "timestamp_fin", "code_version",
                 "graph_fingerprint", "cache_turnos", "fidelidad_sin_evaluar"}
    check("persistencia: metadata completa, grafo r1 y sha de r1",
          all(META_KEYS <= set(pl["meta"]) and pl["meta"]["grafo"] == "r1"
              and pl["meta"]["kg_sha256"] == cr.R1["sha256"]
              for pl in payloads.values()))
    check("persistencia: steps_full sin truncar (output_chars == len(json))",
          all(sf["output_chars"] == len(json.dumps(sf["output"], ensure_ascii=False))
              for pl in payloads.values() for sf in pl["steps_full"]))
    check("persistencia: raw_turns_agent 1:1 con llamadas API",
          all(len(pl["raw_turns_agent"]) == len(pl["trace"]["api_calls"])
              for pl in payloads.values()))
    check("persistencia: fidelidad sin evaluar y respuesta parseada",
          all(pl["meta"]["fidelidad_sin_evaluar"] and pl["trace"]["parse_ok"]
              for pl in payloads.values()))
    conn = sqlite3.connect(DB_PATH)
    domains = [r[0] for r in conn.execute(
        "SELECT DISTINCT domain FROM cache UNION SELECT DISTINCT domain FROM access_log")]
    conn.close()
    check("persistencia: db solo con dominio 'agent' (cero juez)", domains == ["agent"])
    res2 = rv.correr_grafo("r1", client_real=ExplodingClient(), db_path=DB_PATH,
                           label=LABEL + "_replay", casos=casos,
                           outdir=SELFTEST_DIR / "trazas_replay")
    check("persistencia: replay 100 % caché (0 misses, misma respuesta final)",
          res2["cache_stats"]["misses"] == 0
          and res2["cache_stats"]["hits"] == len(script)
          and json.loads((SELFTEST_DIR / "trazas_replay" /
                          f"{rv._sanitizar(casos[0]['caso_id'])}.json").read_text(
                              encoding="utf-8"))["trace"]["final_json"]
          == payloads[casos[0]["caso_id"]]["trace"]["final_json"])

    # --- 6) REPLAY con las aristas nuevas ---
    pl1, pl2 = payloads[casos[0]["caso_id"]], payloads[casos[1]["caso_id"]]
    sal = pl1["steps_full"][1]["output"]
    check("harness sirve la arista `referencia` en ver_vecinos (steps_full)",
          any(v["vecino_id"] == ref["target"] and v["relation"] == "referencia"
              for v in sal.get("salientes", [])))
    ent = pl2["steps_full"][0]["output"]
    check("harness sirve la arista de esqueleto `subclase_de` (steps_full)",
          any(v["vecino_id"] == esq["source"] and v["relation"] == "subclase_de"
              for v in ent.get("entrantes", [])))
    ev_nav = evaluar_traza(pl1["trace"], [ref["target"]], index, verificar_replay=False)
    pn = ev_nav["por_nodo"][0]
    check("métrica: target consultado SOLO vía la arista `referencia` (ver_vecinos)",
          pn["consultado"] and pn["consultado_via"] == "ver_vecinos" and not pn["visto"])
    check("réplica de la regla del censo: el ancla del target resuelve a él",
          ref["target"] in aidx.resolver(ref["to"], ref["punto"]))
    rep_ok = all(evaluar_traza(pl["trace"], [], index, verificar_replay=True)["replay_ok"]
                 for pl in (pl1, pl2))
    check("replay estándar OK en ambos casos (aristas nuevas reproducidas)", rep_ok)
    check("replay FUERTE OK en ambos casos (steps_full == re-ejecución)",
          all(not verificar_steps_full(pl, index) for pl in (pl1, pl2)))
    tr_manipulada = json.loads(json.dumps(pl1))
    tr_manipulada["steps_full"][1]["output"] = {"id": "x", "salientes": []}
    check("replay FUERTE detecta manipulación de steps_full",
          bool(verificar_steps_full(tr_manipulada, index)))

    # --- 4) MAPPING (§2/§4 + agregar del pipeline + agregar_par §7) ---
    check("mapping §4: modal 2-de-3 y sin_consenso",
          mapping.veredicto_modal(["cumplido", "cumplido", "dudoso"]) == "cumplido"
          and mapping.veredicto_modal(["cumplido", "no_cumplido", "dudoso"]) == "sin_consenso")
    check("mapping §2: correcto / incorrecto / parcial / requiere_adjudicacion",
          mapping.veredicto_pregunta(["cumplido", "cumplido"]) == "correcto"
          and mapping.veredicto_pregunta(["no_cumplido", "no_cumplido"]) == "incorrecto"
          and mapping.veredicto_pregunta(["cumplido", "no_cumplido"]) == "parcial"
          and mapping.veredicto_pregunta(["cumplido", "sin_consenso"]) == "requiere_adjudicacion")
    # pipeline_fidelidad.agregar sobre veredictos scripteados (ids opacos r1)
    ciegos = [{"id_opaco": cr.id_opaco_base("EV2F-901", "sha_a"),
               "pregunta": "p1", "respuesta": "r1_texto",
               "criterios": [{"criterio": "c1", "cita_textual": "x"},
                             {"criterio": "c2", "cita_textual": "y"}]},
              {"id_opaco": cr.id_opaco_base("EV2F-902", "sha_b"),
               "pregunta": "p2", "respuesta": "r2_texto",
               "criterios": [{"criterio": "c1", "cita_textual": "z"}]}]
    jdir = SELFTEST_DIR / "juez_out"
    jdir.mkdir()
    veredictos = {1: [["cumplido", "cumplido"], ["no_cumplido"]],
                  2: [["cumplido", "no_cumplido"], ["no_cumplido"]],
                  3: [["cumplido", "cumplido"], ["dudoso"]]}
    for rep, (v1, v2) in veredictos.items():
        with (jdir / f"veredictos_r{rep}.jsonl").open("w", encoding="utf-8") as f:
            for c, vs in zip(ciegos, (v1, v2)):
                f.write(json.dumps({
                    "id_opaco": c["id_opaco"], "rep": rep,
                    "clasificacion_respuesta": "contenido",
                    "criterios": [{"indice": i + 1, "veredicto": v, "fragmento": None,
                                   "justificacion": ""} for i, v in enumerate(vs)],
                    "meta": {"modelo": "m", "stop_reason": "end_turn",
                             "input_tokens": 1, "output_tokens": 1,
                             "prompt_sha256": "s", "code_ver": "cv"}},
                    ensure_ascii=False) + "\n")
    agg = pf.agregar(jdir, 3, ciegos)
    por_id = {a["id_opaco"]: a for a in agg["agregados"]}
    check("pipeline.agregar: modal por criterio y veredicto por pregunta",
          por_id[ciegos[0]["id_opaco"]]["veredicto_pregunta"] == "correcto"
          and por_id[ciegos[0]["id_opaco"]]["modales"] == ["cumplido", "cumplido"])
    check("pipeline.agregar: dudoso 1/3 no fuerza adjudicación (modal 2-de-3)",
          por_id[ciegos[1]["id_opaco"]]["veredicto_pregunta"] == "incorrecto")
    check("agregar_par §7: mayoría / empate triple -> parcial / invariancia ADJ",
          ag.agregar_par(["correcto", "correcto", "parcial"]) == "correcto"
          and ag.agregar_par(["correcto", "parcial", "incorrecto"]) == "parcial"
          and ag.agregar_par(["correcto", "correcto", "requiere_adjudicacion"]) == "correcto"
          and ag.agregar_par(["correcto", "parcial", "requiere_adjudicacion"])
          == "requiere_adjudicacion")

    # --- 5) CROSS-HITS: provocación y detección ---
    ns = lc.make_namespace("selftest_r1", code_ver="selftest-v1", thinking=False)
    db_c1 = cr.CACHE_DIR / "selftest_cross_a.db"
    kwargs = {"model": "m", "max_tokens": 10,
              "messages": [{"role": "user", "content": "hola"}]}
    fk = FakeSequential([turno_final("una sola llamada pagada")])
    cli1 = lc.CachingClient(fk, domain="agent", db_path=db_c1, namespace=ns,
                            thinking_enabled=False, run_label="rep_a")
    cli1.messages.create(**kwargs)
    cli1.close()
    cli2 = lc.CachingClient(ExplodingClient(), domain="agent", db_path=db_c1,
                            namespace=ns, thinking_enabled=False, run_label="rep_b")
    cli2.messages.create(**kwargs)      # hit: misma db + namespace -> no re-muestrea
    st = cli2.stats()
    cli2.close()
    check("cross-hit PROVOCADO: misma db+namespace sirve la llamada de otra rep "
          "(por eso cada rep lleva db propia)", st["hits"] == 1 and st["misses"] == 0
          and fk.calls == 1)
    db_c2 = cr.CACHE_DIR / "selftest_cross_b.db"
    fk2 = FakeSequential([turno_final("otra db, misma key")])
    cli3 = lc.CachingClient(fk2, domain="agent", db_path=db_c2, namespace=ns,
                            thinking_enabled=False, run_label="rep_c")
    cli3.messages.create(**kwargs)
    cli3.close()
    det = pf.verificar_cross_hits([db_c1, db_c2])
    check("detector: keys en común entre dbs -> cross_hits > 0", det["cross_hits"] > 0)
    det2 = pf.verificar_cross_hits([db_c1, DB_PATH])
    check("detector: dbs disjuntas (agente selftest vs provocada) -> cross_hits 0",
          det2["cross_hits"] == 0)

    # --- sellos al cierre ---
    check("sellos idénticos al cierre (nada sellado cambió durante el selftest)",
          cr.verificar_sellos() == sellos)

    passed = sum(ok for _, ok in _checks)
    print(f"\n  {passed}/{len(_checks)} checks OK")
    print("  RESULTADO:", "PASS" if passed == len(_checks) else "FAIL")
    return 0 if passed == len(_checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
