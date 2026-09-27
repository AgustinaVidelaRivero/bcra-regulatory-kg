"""
selftest_runner_ev2_neo4j.py — SELFTEST del runner del gate 4 (sin API, $0).

Solo stdlib + módulos del repo (+ el SDK de Anthropic para construir los
mensajes falsos, como selftest_r1.py). Ningún cliente real se construye;
ANTHROPIC_API_KEY no se lee.

Bloque (i) OFFLINE — sin Neo4j y sin API:
  cliente falso con respuestas scripteadas (tool_use + final_json válido,
  patrón ev2_r1/code/selftest_r1.py) y un stub de Neo4jIndex con las tres
  herramientas sobre tres nodos inventados. Verifica: el runner aborta sin
  --autorizado-fase-b y --tope (exit 2, nada escrito); la traza tiene
  exactamente las claves de la decisión 4 (comparadas contra
  ev2_r1/trazas/ev2_r1_base/EV2F-001.json, salvo u_b18 y las dos nuevas);
  steps_full 1:1 con trace.steps; meta.model_segun_api sale del raw.model del
  cliente falso; meta.backend trae modo fulltext y el índice; el tope de 15
  llamadas del harness corta con hit_tool_limit cuando el cliente falso pide
  16; el namespace de la caché contiene el sha del grafo, el modo y el índice;
  --casos con un JSON alternativo.

Bloque (ii) INTEGRACIÓN — Neo4j arriba, sin API:
  mismo cliente falso, Neo4jIndex REAL sobre KG_Reextraido_r1 en modo
  fulltext. Primero una consulta DIRECTA al índice full-text (Cypher, se
  imprime); luego el cliente falso pide buscar_nodos con esa consulta,
  ver_nodo del primer id y ver_vecinos. Verifica que los outputs capturados
  en steps_full vienen de Neo4j (mismo id que la consulta directa),
  trace.seen_provenances no vacío y sha256 del grafo en meta.backend =
  0226e947…. Precondición: `docker ps --filter name=neo4j` con el contenedor
  Up (healthy); si no, el bloque se marca NO CORRIDO y no se toca Docker.

Uso (ambos argumentos obligatorios, FUERA del repo):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B \
      data/experiment/ev2_tanda0/code/selftest_runner_ev2_neo4j.py \
      --outdir <scratchpad>/selftest_gate4 --db <scratchpad>/selftest_gate4/selftest.db
  --db es la ruta BASE: cada bloque usa una db propia derivada
  (<base>_offline.db, <base>_casos.db, <base>_integracion.db) para que ningún
  hit de caché cruce de un bloque a otro.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sqlite3
import subprocess
import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import runner_ev2_neo4j as rn              # noqa: E402  (arma sys.path del repo)
import harness                             # noqa: E402  (solo import)
import llm_cache as lc                     # noqa: E402
from neo4j_index import Neo4jIndex         # noqa: E402
from anthropic.types import Message        # noqa: E402

RUNNER = CODE_DIR / "runner_ev2_neo4j.py"
GRAFO = "KG_Reextraido_r1"
MODO = "fulltext"
SHA_R1 = "0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a"
INDICE_R1 = "nodos_fulltext_kg_reextraido_r1"
TRAZA_C1 = rn.EXP_DIR / "ev2_r1" / "trazas" / "ev2_r1_base" / "EV2F-001.json"
MODELO_FALSO = "fake-model-selftest-gate4"   # distinto de harness.MODEL a propósito
CONSULTA_INTEGRACION = "asociación mutual"   # ejemplo documentado en neo4j_index.py

_checks: list[tuple[str, bool]] = []


def check(nombre: str, cond) -> bool:
    _checks.append((nombre, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {nombre}", flush=True)
    return bool(cond)


# --------------------------------------------------------------------------- #
# Cliente falso (patrón selftest_r1) — honra tool_choice none como la API      #
# --------------------------------------------------------------------------- #
def _msg(content, stop_reason, uid):
    return Message.model_validate({
        "id": f"msg_selftest_gate4_{uid}", "type": "message", "role": "assistant",
        "model": MODELO_FALSO, "content": content,
        "stop_reason": stop_reason, "stop_sequence": None,
        "usage": {"input_tokens": 1500, "output_tokens": 60,
                  "cache_read_input_tokens": 0,
                  "cache_creation_input_tokens": 1200},
    })


def turno_tool(nombre, args, uid):
    return _msg([{"type": "text", "text": "Exploro el grafo."},
                 {"type": "tool_use", "id": f"tu_{uid}", "name": nombre, "input": args}],
                "tool_use", uid)


def turno_final(respuesta, citas=(), uid="final"):
    txt = json.dumps({"respuesta": respuesta, "citas": list(citas), "respondible": True},
                     ensure_ascii=False)
    return _msg([{"type": "text", "text": txt}], "end_turn", uid)


class FakeClient:
    """Devuelve el guion en orden. Si el harness fuerza la respuesta final
    (tool_choice {"type": "none"}, harness.py:480-484), responde con un final
    canónico SIN consumir el guion — como haría la API real, que no puede
    emitir tool_use bajo tool_choice none."""

    def __init__(self, script):
        self.script = list(script)
        self.calls = 0
        self.forzados = 0
        self.messages = self

    def create(self, **kwargs):
        self.calls += 1
        if kwargs.get("tool_choice") == {"type": "none"}:
            self.forzados += 1
            return turno_final("final forzado por el tope de tool calls",
                               uid=f"forzado{self.forzados}")
        if not self.script:
            raise AssertionError("llamada API no prevista en el selftest")
        return self.script.pop(0)


# --------------------------------------------------------------------------- #
# Stub de Neo4jIndex (bloque i): tres nodos inventados, sin driver             #
# --------------------------------------------------------------------------- #
class StubNeo4jIndex(Neo4jIndex):
    """Neo4jIndex sin driver: las tres tools responden desde tres nodos
    inventados, con los MISMOS shapes que neo4j_index.py (modo fulltext)."""

    NODOS = {
        "Sujeto_entidad_financiera_stub": {
            "type": "Sujeto", "label": "Entidad financiera (stub)",
            "properties": {"descripcion": "Entidad financiera inventada para el selftest."},
            "provenances": [{"source_doc": "t-stub.pdf", "location": "Punto 1.1"}]},
        "Obligacion_informar_stub": {
            "type": "Obligacion", "label": "Obligación de informar (stub)",
            "properties": {"descripcion": "Obligación inventada para el selftest."},
            "provenances": [{"source_doc": "t-stub.pdf", "location": "Punto 2.3"}]},
        "Excepcion_mutual_stub": {
            "type": "Excepcion", "label": "Excepción mutuales (stub)",
            "properties": {"descripcion": "Excepción inventada para el selftest."},
            "provenances": [{"source_doc": "t-stub.pdf", "location": "Sección 3"}]},
    }
    ARISTAS = [
        ("Sujeto_entidad_financiera_stub", "sujeto_de", "Obligacion_informar_stub",
         [{"source_doc": "t-stub.pdf", "location": "Punto 2.3"}]),
        ("Excepcion_mutual_stub", "excepcion_de", "Obligacion_informar_stub",
         [{"source_doc": "t-stub.pdf", "location": "Sección 3"}]),
    ]

    def __init__(self, grafo: str = GRAFO, modo: str = MODO):
        super().__init__(driver=None, grafo=grafo, modo=modo)
        self.llamadas: list = []

    def buscar_nodos(self, consulta: str, limite: int = 10) -> dict:
        self.llamadas.append(("buscar_nodos", consulta))
        lim = self._limite(limite)
        res = [{"id": i, "type": n["type"], "label": n["label"], "tokens_matcheados": 1,
                "resumen_propiedades": dict(n["properties"])}
               for i, n in self.NODOS.items()]
        return {"consulta": consulta, "total_con_match": len(res), "resultados": res[:lim]}

    def ver_nodo(self, id: str) -> dict:
        self.llamadas.append(("ver_nodo", id))
        n = self.NODOS.get(id)
        if n is None:
            return {"error": f"No existe un nodo con id '{id}'.",
                    "sugerencia": "Usá buscar_nodos para encontrar el id correcto."}
        return {"id": id, "type": n["type"], "label": n["label"],
                "properties": dict(n["properties"]), "provenances": list(n["provenances"])}

    def ver_vecinos(self, id: str, direccion: str = "ambas", limite: int = 40) -> dict:
        self.llamadas.append(("ver_vecinos", id))
        n = self.NODOS.get(id)
        if n is None:
            return {"error": f"No existe un nodo con id '{id}'.",
                    "sugerencia": "Usá buscar_nodos para encontrar el id correcto."}
        out = [{"relation": r, "vecino_id": t, "vecino_label": self.NODOS[t]["label"],
                "provenances": p} for s, r, t, p in self.ARISTAS if s == id]
        inn = [{"relation": r, "vecino_id": s, "vecino_label": self.NODOS[s]["label"],
                "provenances": p} for s, r, t, p in self.ARISTAS if t == id]
        direccion = (direccion or "ambas").lower()
        if direccion not in ("ambas", "salientes", "entrantes"):
            direccion = "ambas"
        res = {"id": id, "label": n["label"], "n_salientes_total": len(out),
               "n_entrantes_total": len(inn)}
        if direccion in ("ambas", "salientes"):
            res["salientes"] = out[:limite]
            res["salientes_truncado"] = len(out) > limite
        if direccion in ("ambas", "entrantes"):
            res["entrantes"] = inn[:limite]
            res["entrantes_truncado"] = len(inn) > limite
        return res


# --------------------------------------------------------------------------- #
# Utilidades                                                                    #
# --------------------------------------------------------------------------- #
def cargar_traza(outdir: Path, caso_id: str) -> dict:
    return json.loads((outdir / f"{rn.rv._sanitizar(caso_id)}.json").read_text(encoding="utf-8"))


def steps_1a1(pl: dict) -> bool:
    """steps_full 1:1 con trace.steps: mismo largo, mismo n/tool/input,
    output_chars idéntico y output_truncado = prefijo del output completo."""
    st, sf = pl["trace"]["steps"], pl["steps_full"]
    if len(st) != len(sf):
        return False
    for a, b in zip(st, sf):
        s = json.dumps(b["output"], ensure_ascii=False)
        if (a["n"], a["tool"], a["input"], a["output_chars"]) != (b["n"], b["tool"], b["input"], b["output_chars"]):
            return False
        if len(s) != b["output_chars"]:
            return False
        trunc = a["output_truncado"]
        if len(s) <= harness.TRUNC_TOOL_OUTPUT:
            if trunc != s:
                return False
        elif not trunc.startswith(s[:harness.TRUNC_TOOL_OUTPUT]):
            return False
    return True


def namespace_en_db(db: Path) -> list[str]:
    conn = sqlite3.connect(db)
    try:
        return [r[0] for r in conn.execute("SELECT DISTINCT namespace FROM cache")]
    finally:
        conn.close()


def dentro_del_repo(p: Path) -> bool:
    try:
        Path(p).resolve().relative_to(rn.REPO_DIR)
        return True
    except ValueError:
        return False


def claves_esperadas_meta(c1: dict) -> set:
    return (set(c1["meta"]) - {"u_b18"}) | {"backend", "model_segun_api"}


# --------------------------------------------------------------------------- #
# Bloque (i): OFFLINE                                                            #
# --------------------------------------------------------------------------- #
def bloque_offline(outdir: Path, db_base: Path, c1: dict) -> None:
    print("\n== BLOQUE (i) OFFLINE — sin Neo4j, sin API ==", flush=True)

    # (a) gating: el runner aborta sin --autorizado-fase-b y --tope, sin escribir nada
    env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
    env.pop("ANTHROPIC_API_KEY", None)
    base = [sys.executable, "-B", str(RUNNER), "--grafo", GRAFO, "--modo", MODO,
            "--label", "selftest_abort"]
    for nombre, extra in (("sin ninguno de los dos", []),
                          ("solo --autorizado-fase-b", ["--autorizado-fase-b"]),
                          ("solo --tope", ["--tope", "1"])):
        od, dbp = outdir / f"abort_{len(_checks)}", db_base.with_name(f"{db_base.stem}_abort{len(_checks)}.db")
        r = subprocess.run(base + ["--outdir", str(od), "--db", str(dbp)] + extra,
                           capture_output=True, text=True, env=env, cwd=str(rn.REPO_DIR))
        check(f"gating: aborta {nombre} (exit 2, 'ABORTADO', nada escrito)",
              r.returncode == 2 and "ABORTADO" in r.stdout and not od.exists() and not dbp.exists())
    r = subprocess.run(base + ["--autorizado-fase-b"], capture_output=True, text=True,
                       env=env, cwd=str(rn.REPO_DIR))
    check("gating: con --autorizado-fase-b sin --tope no aparece salida de Neo4j ni de sellos",
          r.returncode == 2 and "sello OK" not in r.stdout)

    # (b) corrida offline: cliente falso + stub, dos casos del orden sellado
    casos, fuente = rn.cargar_casos(None)
    check("casos: 40 de fidelidad en el orden sellado de C1 (semilla orden-ev2-r1)",
          len(casos) == 40 and fuente["semilla_orden"] == "orden-ev2-r1"
          and [c["caso_id"] for c in casos] == [c["caso_id"] for c in rn.cr.casos_fidelidad_r1()])
    casos2 = [dict(casos[0]), dict(casos[1])]
    n1, n2, n3 = list(StubNeo4jIndex.NODOS)
    cita = StubNeo4jIndex.NODOS[n2]["provenances"][0]
    script = [
        # caso 1: las tres tools + final con una cita vista
        turno_tool("buscar_nodos", {"consulta": "entidad financiera stub", "limite": 10}, "c1a"),
        turno_tool("ver_nodo", {"id": n2}, "c1b"),
        turno_tool("ver_vecinos", {"id": n2, "direccion": "ambas"}, "c1c"),
        turno_final("respuesta offline caso 1", citas=[cita], uid="c1fin"),
    ]
    # caso 2: el cliente falso PIDE 16 tool calls; el harness corta en 15
    script += [turno_tool("buscar_nodos", {"consulta": f"tope {k}"}, f"c2_{k}") for k in range(1, 17)]
    script += [turno_final("respuesta offline caso 2 (nunca servida)", uid="c2fin")]
    fake = FakeClient(script)
    stub = StubNeo4jIndex()
    od, dbp = outdir / "offline", db_base.with_name(f"{db_base.stem}_offline.db")
    resumen = rn.correr_grafo(GRAFO, modo=MODO, label="selftest_offline", client_real=fake,
                              indice=stub, db_path=dbp, outdir=od, casos=casos2,
                              fuente_casos=fuente)
    check("runner: 2 casos corridos, resumen persistido",
          resumen["n_casos_corridos"] == 2 and (od / "resumen_selftest_offline.json").exists())
    pl1, pl2 = cargar_traza(od, casos2[0]["caso_id"]), cargar_traza(od, casos2[1]["caso_id"])

    # (c) estructura de la traza = C1 (decisión 4)
    check("traza: claves de primer nivel == EV2F-001 de C1",
          set(pl1) == set(c1) == {"meta", "pregunta", "trace", "steps_full", "raw_turns_agent"})
    check("traza: meta == claves de C1 (sin u_b18) + backend + model_segun_api, exactas",
          set(pl1["meta"]) == claves_esperadas_meta(c1) and set(pl2["meta"]) == claves_esperadas_meta(c1))
    check("traza: trace == vars(QuestionTrace), mismas claves que C1",
          set(pl1["trace"]) == set(c1["trace"]))
    check("traza: steps_full[i] y raw_turns_agent[i] con las claves de C1",
          set(pl1["steps_full"][0]) == set(c1["steps_full"][0])
          and set(pl1["raw_turns_agent"][0]) == set(c1["raw_turns_agent"][0]))
    check("traza: lo que leen juez v1 y ucita2 está y tiene la forma de C1",
          pl1["meta"]["caso_id"] == pl1["trace"]["qid"] == casos2[0]["caso_id"]
          and pl1["trace"]["parse_ok"] is True
          and pl1["trace"]["final_json"]["respuesta"] == "respuesta offline caso 1"
          and isinstance(pl1["trace"]["seen_provenances"], list) and pl1["trace"]["seen_provenances"])
    check("traza: meta valores base (unidad, grafo, kg_path, kg_sha256, model/temperature/max del harness)",
          pl1["meta"]["unidad"] == "ev2_tanda0" and pl1["meta"]["grafo"] == GRAFO
          and pl1["meta"]["kg_path"] == "data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json"
          and pl1["meta"]["kg_sha256"] == SHA_R1
          and pl1["meta"]["model"] == harness.MODEL and pl1["meta"]["temperature"] == harness.TEMPERATURE
          and pl1["meta"]["max_tool_calls"] == harness.MAX_TOOL_CALLS
          and pl1["meta"]["thinking_enabled"] is False and pl1["meta"]["fidelidad_sin_evaluar"] is True
          and pl1["meta"]["semilla_orden"] == "orden-ev2-r1"
          and pl1["meta"]["pos_orden_global"] == casos2[0]["pos_orden_global"]
          and pl1["meta"]["pos_orden_efectivo"] == 1 and pl2["meta"]["pos_orden_efectivo"] == 2)

    # (d) steps_full 1:1 con trace.steps
    check("steps_full: 1:1 con trace.steps en ambos casos (n/tool/input/chars/prefijo)",
          steps_1a1(pl1) and steps_1a1(pl2) and len(pl1["steps_full"]) == 3)
    check("steps_full: outputs vienen del stub (ver_nodo del id pedido, con provenances)",
          pl1["steps_full"][1]["output"]["id"] == n2
          and pl1["steps_full"][1]["output"]["provenances"] == StubNeo4jIndex.NODOS[n2]["provenances"]
          and stub.llamadas[:3] == [("buscar_nodos", "entidad financiera stub"), ("ver_nodo", n2), ("ver_vecinos", n2)])
    check("citas: la cita vista es fiel (citations_unseen_raw/normalized vacías)",
          pl1["trace"]["citations_unseen_raw"] == [] and pl1["trace"]["citations_unseen_normalized"] == [])

    # (e) model_segun_api sale del raw.model del cliente falso
    check("meta.model_segun_api == [raw.model del cliente falso] (≠ harness.MODEL)",
          pl1["meta"]["model_segun_api"] == [MODELO_FALSO] and pl2["meta"]["model_segun_api"] == [MODELO_FALSO]
          and MODELO_FALSO != harness.MODEL
          and all(t["raw"]["model"] == MODELO_FALSO for t in pl1["raw_turns_agent"]))
    check("raw_turns_agent: 1:1 con trace.api_calls (crudos íntegros de cada llamada)",
          len(pl1["raw_turns_agent"]) == len(pl1["trace"]["api_calls"]) == 4
          and len(pl2["raw_turns_agent"]) == len(pl2["trace"]["api_calls"]))

    # (f) meta.backend
    b = pl1["meta"]["backend"]
    check("meta.backend: backend neo4j, grafo, nombre canónico, sha r1, modo fulltext, índice",
          set(b) == {"backend", "grafo", "nombre_canonico", "kg_sha256", "modo", "indice_fulltext"}
          and b["backend"] == "neo4j" and b["grafo"] == GRAFO and b["nombre_canonico"] == "KG-Reextraído-r1"
          and b["kg_sha256"] == SHA_R1 and b["modo"] == MODO and b["indice_fulltext"] == INDICE_R1)

    # (g) tope de 15 tool calls del harness
    check("tope: el cliente falso pidió 16 tool calls; el harness cortó en 15 con hit_tool_limit",
          pl2["trace"]["tool_calls_used"] == 15 and pl2["trace"]["hit_tool_limit"] is True
          and len(pl2["steps_full"]) == 15 and pl2["trace"]["parse_ok"] is True
          and fake.forzados == 1 and len(fake.script) == 2)   # quedan el 16.º tool_use y su final
    check("tope: caso 1 no tocó el límite (hit_tool_limit falso, 3 tool calls)",
          pl2["meta"]["caso_id"] != pl1["meta"]["caso_id"] and pl1["trace"]["hit_tool_limit"] is False
          and pl1["trace"]["tool_calls_used"] == 3)

    # (h) namespace de la caché
    ns_db = namespace_en_db(dbp)
    ns_esp = lc.make_namespace("agent", code_ver=lc.code_version(),
                               graph_fp=f"{SHA_R1}|neo4j:{MODO}:{INDICE_R1}", thinking=False)
    check("namespace: contiene sha del grafo, modo e índice; único en la db; == make_namespace esperado",
          ns_db == [ns_esp] and SHA_R1 in ns_esp and f"neo4j:{MODO}:{INDICE_R1}" in ns_esp
          and resumen["cache_stats"]["namespace"] == ns_esp
          and pl1["meta"]["graph_fingerprint"] == f"{SHA_R1}|neo4j:{MODO}:{INDICE_R1}")
    check("namespace: distinto del de C1 (graph_fingerprint de 16 hex del loader)",
          pl1["meta"]["graph_fingerprint"] != c1["meta"]["graph_fingerprint"])
    conn = sqlite3.connect(dbp)
    dom = [r[0] for r in conn.execute("SELECT DISTINCT domain FROM cache UNION SELECT DISTINCT domain FROM access_log")]
    conn.close()
    check("caché: db solo con dominio 'agent'", dom == ["agent"])

    # (i) --casos alternativo
    alt = outdir / "casos_alternativos.json"
    alt.write_text(json.dumps([{"caso_id": "NUEVA-001", "eje": "fidelidad",
                                "pregunta": "¿Pregunta inventada sobre un documento nuevo?"}],
                              ensure_ascii=False), encoding="utf-8")
    casos_alt, fuente_alt = rn.cargar_casos(alt)
    fake2 = FakeClient([turno_tool("ver_nodo", {"id": n1}, "alt1"),
                        turno_final("respuesta alternativa", uid="altfin")])
    od2, dbp2 = outdir / "casos_alt", db_base.with_name(f"{db_base.stem}_casos.db")
    res2 = rn.correr_grafo(GRAFO, modo=MODO, label="selftest_casos", client_real=fake2,
                           indice=StubNeo4jIndex(), db_path=dbp2, outdir=od2, casos=casos_alt,
                           fuente_casos=fuente_alt)
    pla = cargar_traza(od2, "NUEVA-001")
    check("--casos: JSON alternativo {caso_id, eje, pregunta} corre; semilla_orden None; fuente con sha",
          res2["n_casos_corridos"] == 1 and pla["meta"]["caso_id"] == "NUEVA-001"
          and pla["meta"]["semilla_orden"] is None and pla["meta"]["pos_orden_global"] == 1
          and res2["casos_fuente"]["sha256"] == rn.sha256_path(alt)
          and set(pla["meta"]) == claves_esperadas_meta(c1))
    malo = outdir / "casos_malos.json"
    malo.write_text(json.dumps([{"caso_id": "X", "pregunta": "sin eje"}]), encoding="utf-8")
    try:
        rn.cargar_casos(malo)
        ok_malo = False
    except ValueError:
        ok_malo = True
    check("--casos: JSON sin las tres claves es rechazado", ok_malo)

    # (j) inconsistencias guardadas
    try:
        rn.correr_grafo(GRAFO, modo="paridad", label="x", client_real=fake2, indice=StubNeo4jIndex(),
                        db_path=dbp2, outdir=od2, casos=casos_alt, fuente_casos=fuente_alt)
        ok_inc = False
    except ValueError:
        ok_inc = True
    check("guarda: índice con modo distinto de --modo es rechazado", ok_inc)


# --------------------------------------------------------------------------- #
# Bloque (ii): INTEGRACIÓN con Neo4j real (sin API)                             #
# --------------------------------------------------------------------------- #
def docker_neo4j_up() -> tuple[bool, str]:
    cmd = ["docker", "ps", "--filter", "name=neo4j", "--format", "{{.Names}}\t{{.Status}}"]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        salida = (r.stdout + r.stderr).strip()
        ok = r.returncode == 0 and "Up" in salida and "healthy" in salida
    except (OSError, subprocess.TimeoutExpired) as e:
        salida, ok = f"{type(e).__name__}: {e}", False
    return ok, f"$ {' '.join(cmd)}\n{salida}"


def bloque_integracion(outdir: Path, db_base: Path, c1: dict) -> bool:
    """Devuelve True si corrió; False si quedó NO CORRIDO (precondición)."""
    print("\n== BLOQUE (ii) INTEGRACIÓN — Neo4j real, sin API ==", flush=True)
    ok, salida = docker_neo4j_up()
    print(salida, flush=True)
    if not ok:
        print("  BLOQUE (ii): NO CORRIDO — el contenedor de Neo4j no está Up (healthy). "
              "No se levanta ni se toca Docker.", flush=True)
        return False
    from conexion import abrir_driver
    try:
        driver = abrir_driver()
    except Exception as e:  # noqa: BLE001
        print(f"  BLOQUE (ii): NO CORRIDO — abrir_driver falló: {type(e).__name__}: {e}", flush=True)
        return False

    try:
        # Consulta DIRECTA al índice full-text (misma query Lucene que Neo4jIndex._buscar_fulltext)
        q_lucene = " ".join(harness._tokens(CONSULTA_INTEGRACION))
        with driver.session() as s:
            filas = s.run(
                "CALL db.index.fulltext.queryNodes($idx, $q) YIELD node, score "
                "RETURN node.id AS id, node.label AS label, score "
                "ORDER BY score DESC, size(node.label) ASC, node.id ASC LIMIT 5",
                idx=INDICE_R1, q=q_lucene).data()
            total = s.run("CALL db.index.fulltext.queryNodes($idx, $q) YIELD node "
                          "RETURN count(node) AS n", idx=INDICE_R1, q=q_lucene).single()["n"]
            meta_db = s.run("MATCH (m:KG_Meta {grafo: $g}) RETURN properties(m) AS p",
                            g=GRAFO).single()
        directa = {"consulta": CONSULTA_INTEGRACION, "q_lucene": q_lucene, "indice": INDICE_R1,
                   "total_con_match": total, "top5": filas,
                   "kg_meta_neo4j": dict(meta_db["p"]) if meta_db else None}
        (outdir / "consulta_directa_indice.json").write_text(
            json.dumps(directa, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"  consulta directa: {CONSULTA_INTEGRACION!r} -> q_lucene={q_lucene!r} "
              f"total={total}", flush=True)
        for f in filas:
            print(f"     {f['score']:8.4f}  {f['id']}  | {f['label']}", flush=True)
        if not filas:
            check("integración: la consulta directa devuelve al menos un hit", False)
            return True
        id_directo = filas[0]["id"]

        indice = Neo4jIndex(driver, grafo=GRAFO, modo=MODO)
        nodo_directo = indice.ver_nodo(id_directo)
        busq_directa = indice.buscar_nodos(CONSULTA_INTEGRACION, 10)
        prov0 = (nodo_directo.get("provenances") or [None])[0]
        casos, fuente = rn.cargar_casos(None)
        caso = dict(casos[2])
        script = [
            turno_tool("buscar_nodos", {"consulta": CONSULTA_INTEGRACION, "limite": 10}, "i1"),
            turno_tool("ver_nodo", {"id": id_directo}, "i2"),
            turno_tool("ver_vecinos", {"id": id_directo, "direccion": "ambas"}, "i3"),
            turno_final("respuesta integración", citas=[prov0] if prov0 else [], uid="ifin"),
        ]
        fake = FakeClient(script)
        od, dbp = outdir / "integracion", db_base.with_name(f"{db_base.stem}_integracion.db")
        resumen = rn.correr_grafo(GRAFO, modo=MODO, label="selftest_integracion", client_real=fake,
                                  indice=indice, db_path=dbp, outdir=od, casos=[caso],
                                  fuente_casos=fuente)
        pl = cargar_traza(od, caso["caso_id"])
        sf = pl["steps_full"]
        check("integración: guion consumido (4 llamadas) y 1 caso corrido",
              fake.calls == 4 and resumen["n_casos_corridos"] == 1 and len(sf) == 3)
        check("integración: buscar_nodos capturado viene de Neo4j — primer id == consulta directa, mismo total",
              sf[0]["output"]["resultados"][0]["id"] == id_directo
              and sf[0]["output"]["total_con_match"] == total)
        check("integración: buscar_nodos capturado == Neo4jIndex.buscar_nodos directo (byte-idéntico)",
              json.dumps(sf[0]["output"], ensure_ascii=False, sort_keys=True)
              == json.dumps(busq_directa, ensure_ascii=False, sort_keys=True))
        check("integración: ver_nodo capturado == nodo de Neo4j (mismo id, provenances no vacías)",
              sf[1]["output"]["id"] == id_directo and sf[1]["output"].get("provenances")
              and sf[1]["output"] == nodo_directo)
        check("integración: ver_vecinos capturado responde por el mismo id con conteos de Neo4j",
              sf[2]["output"]["id"] == id_directo
              and isinstance(sf[2]["output"].get("n_salientes_total"), int)
              and isinstance(sf[2]["output"].get("n_entrantes_total"), int))
        check("integración: trace.seen_provenances no vacío",
              isinstance(pl["trace"]["seen_provenances"], list) and len(pl["trace"]["seen_provenances"]) > 0)
        check("integración: sha256 del grafo en meta.backend == 0226e947… (registro) == KG_Meta en Neo4j",
              pl["meta"]["backend"]["kg_sha256"] == SHA_R1
              and (directa["kg_meta_neo4j"] or {}).get("kg_sha256") == SHA_R1)
        check("integración: meta.backend modo fulltext + índice de r1; model_segun_api del cliente falso",
              pl["meta"]["backend"]["modo"] == MODO and pl["meta"]["backend"]["indice_fulltext"] == INDICE_R1
              and pl["meta"]["model_segun_api"] == [MODELO_FALSO])
        check("integración: steps_full 1:1 con trace.steps; claves de meta exactas",
              steps_1a1(pl) and set(pl["meta"]) == claves_esperadas_meta(c1))
        check("integración: namespace con sha + modo + índice",
              namespace_en_db(dbp) == [lc.make_namespace(
                  "agent", code_ver=lc.code_version(),
                  graph_fp=f"{SHA_R1}|neo4j:{MODO}:{INDICE_R1}", thinking=False)])
        check("integración: cita tomada de la provenance vista es fiel (citations_unseen_normalized vacía)",
              pl["trace"]["citations_unseen_normalized"] == [])
    finally:
        driver.close()
    return True


# --------------------------------------------------------------------------- #
def main() -> int:
    ap = argparse.ArgumentParser(description="Selftest del runner del gate 4 ($0, sin API).")
    ap.add_argument("--outdir", type=Path, required=True, help="directorio de salida (FUERA del repo)")
    ap.add_argument("--db", type=Path, required=True, help="ruta base de las dbs (FUERA del repo)")
    ap.add_argument("--solo-offline", action="store_true", help="no intenta el bloque (ii)")
    args = ap.parse_args()
    outdir, db_base = args.outdir.resolve(), args.db.resolve()
    if dentro_del_repo(outdir) or dentro_del_repo(db_base):
        print(f"ABORTADO: --outdir y --db deben apuntar FUERA del repo ({rn.REPO_DIR}).")
        return 2
    if outdir.exists():
        shutil.rmtree(outdir)
    outdir.mkdir(parents=True)
    db_base.parent.mkdir(parents=True, exist_ok=True)
    for p in db_base.parent.glob(f"{db_base.stem}_*.db"):
        p.unlink()

    print("== SELFTEST runner_ev2_neo4j (gate 4) — $0, sin API ==")
    print(f"  python {sys.version.split()[0]} | outdir {outdir} | db base {db_base}")
    sellos = rn.verificar_sellos(verbose=True)
    check("sellos: harness / runner_ev2 / agente_neo4j / neo4j_index con el sha del mandato",
          len(sellos) == 4)
    c1 = json.loads(TRAZA_C1.read_text(encoding="utf-8"))
    check("referencia: EV2F-001.json de C1 cargada (claves meta/trace de comparación)",
          {"meta", "trace", "steps_full", "raw_turns_agent", "pregunta"} == set(c1) and "u_b18" in c1["meta"])

    bloque_offline(outdir, db_base, c1)
    corrio_ii = False if args.solo_offline else bloque_integracion(outdir, db_base, c1)

    # Cierre: nada bajo el repo, sellos intactos
    repo_t0 = rn.TANDA0_DIR
    basura = [str(p) for p in repo_t0.rglob("*") if p.suffix in (".json", ".db", ".pyc")
              or p.name == "__pycache__"]
    check("repo: ningún .json/.db/.pyc/__pycache__ bajo data/experiment/ev2_tanda0", basura == [])
    check("sellos idénticos al cierre", rn.verificar_sellos() == sellos)

    passed = sum(ok for _, ok in _checks)
    print(f"\n  {passed}/{len(_checks)} checks OK")
    print(f"  bloque (ii): {'CORRIDO' if corrio_ii else 'NO CORRIDO'}")
    print("  RESULTADO:", "PASS" if passed == len(_checks) else "FAIL")
    return 0 if passed == len(_checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
