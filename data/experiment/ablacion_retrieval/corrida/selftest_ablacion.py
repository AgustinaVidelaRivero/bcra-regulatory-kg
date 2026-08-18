"""
selftest_ablacion.py — SELFTEST OFFLINE de la corrida de la ablación (U-A1.4,
fase A, $0: cliente LLM FALSO scripteado; las tools corren contra el Neo4j
real con KG-Refinado, sin costo).

Ejercita el circuito REAL de punta a punta y verifica, con evidencia impresa:
  S0  piezas selladas OK; KG_Meta.kg_sha256 == KG-Refinado; celdas cargadas
      contra sus sha (archivo/prompt/specs) y ensamblado del agente por celda
      (control == harness verbatim; C11 == paquete A1.2 verbatim; despacho
      de tools según los factores);
  S1  corrida de 3 casos (los primeros del orden `orden-ablacion-v1`) en las
      4 celdas con guiones que producen: (A) ancla vista+consultada vía
      ver_nodo, (B) vista sin consultar (brecha), (C) consultada vía
      ver_vecinos + abstención (v2: además una llamada con pagina=2);
      persistencia completa (meta, trace, steps_full sin truncar 1:1,
      raw_turns == llamadas API, latencia por tool), db por celda con
      `cache_stats.hits == 0` y solo domain='agent', namespace del §4;
  S2  RETOMA sin repago: re-correr la celda con un cliente que explota →
      todos los casos salteados (0 accesos); borrar una traza y re-correr →
      se regenera desde la caché (hits == llamadas de ese caso, 0 misses),
      misma respuesta final; los hits quedan DECLARADOS en el resumen;
  S3  0 CROSS-HITS provocado: C10 corre el MISMO guion y las mismas preguntas
      que C00 → su db fresca tiene hits == 0; las keys de C00 no existen en la
      db de C10 (namespace distinto ⇒ key distinta) y sí en la de C00;
  S4  freno por proyección: con cuota ínfima la celda se detiene tras 3 casos
      hechos y lo declara (`freno.tipo == 'proyeccion'`);
  S5  replay determinístico por celda (v1 con Neo4jIndex; v2 con el adaptador
      inyectado): replay estándar + fuerte OK en todas, cruce in-memory del
      control OK, métricas coinciden con lo scripteado, doble corrida
      byte-idéntica; tests del adaptador (tests_replay_v2) PASS;
  S6  pipeline de ANÁLISIS COMPLETO sobre resultados SINTÉTICOS (50 pares × 2
      variantes × 4 celdas, construidos con propiedades conocidas): tabla
      central (micro/macro contra valores calculados a mano), diferencias
      apareadas con bootstrap (determinismo entre dos corridas; IC contiene el
      punto), evaluación mecánica P1–P6 con los umbrales del §5 (escenario
      "todo cumplido" → 6 cumplidas; "P1 falla" → P2–P6 no evaluables y
      reportadas; clase chica → no evaluable a priori), render markdown;
  S7  estimación de costo (Haiku) bajo el tope laudado.

Todo se escribe bajo selftest_out/ (gitignorado). Uso:
  .venv/bin/python -B selftest_ablacion.py
"""

from __future__ import annotations

import json
import shutil
import sqlite3
import sys
from pathlib import Path

CORRIDA_DIR = Path(__file__).resolve().parent
if str(CORRIDA_DIR) not in sys.path:
    sys.path.insert(0, str(CORRIDA_DIR))

from comun_corrida import (ESTRATOS, GRAFO, KG_REFINADO_SHA256, ORDEN_CELDAS, SELFTEST_DIR,  # noqa: E402
                           UMBRALES, VARIANTES, cargar_celdas, cargar_pares, huerfanos_p6,
                           indice_anclas_refinado, namespace_celda, orden_resuelto, sanitizar,
                           sha_texto, verificar_kg_meta)
from comun_ablacion import verificar_piezas  # noqa: E402
from agente_celda import AgenteCelda, BackendCelda  # noqa: E402
import runner_ablacion as run  # noqa: E402
import replay_ablacion as rep  # noqa: E402
import analisis_ablacion as ana  # noqa: E402
import estimacion_ablacion as est  # noqa: E402
import tests_replay_v2  # noqa: E402

import harness  # noqa: E402
import llm_cache as lc  # noqa: E402
from harness import GraphIndex, SYSTEM_PROMPT, TOOLS  # noqa: E402
from agente_v2 import SYSTEM_PROMPT_V2_PROPUESTO  # noqa: E402
from tools_v2 import TOOLS_V2  # noqa: E402
from comun_ev2 import cargar_runtime  # noqa: E402
from anthropic.types import Message  # noqa: E402

PRECIO_IN, PRECIO_OUT = harness.PRICE_IN_PER_M, harness.PRICE_OUT_PER_M
_checks: list[tuple[str, bool]] = []


def check(nombre: str, cond) -> None:
    _checks.append((nombre, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {nombre}", flush=True)


# --------------------------------------------------------------------------- #
# Cliente falso                                                                #
# --------------------------------------------------------------------------- #
def _msg(content, stop_reason):
    return Message.model_validate({
        "id": "msg_selftest", "type": "message", "role": "assistant", "model": harness.MODEL,
        "content": content, "stop_reason": stop_reason, "stop_sequence": None,
        "usage": {"input_tokens": 1500, "output_tokens": 60, "cache_read_input_tokens": 0,
                  "cache_creation_input_tokens": 1200}})


def turno_tool(nombre, args, uid):
    return _msg([{"type": "text", "text": "Exploro el grafo."},
                 {"type": "tool_use", "id": uid, "name": nombre, "input": args}], "tool_use")


def turno_final(respuesta, respondible=True):
    txt = json.dumps({"respuesta": respuesta, "citas": [], "respondible": respondible}, ensure_ascii=False)
    return _msg([{"type": "text", "text": txt}], "end_turn")


class FakeSequential:
    def __init__(self, script):
        self.script, self.calls, self.messages = list(script), 0, self

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
# Guiones por celda                                                            #
# --------------------------------------------------------------------------- #
def _gold_y_vecino(driver, ancla_index, par, backends: dict) -> tuple[str, str]:
    """(gold_id, vecino_id) tal que gold aparece en ver_vecinos(vecino) en TODAS las
    celdas (v1 ventana 40 'ambas'; v2 página 1 por_pagina 40)."""
    a = par["gold"]["anclas"][0]
    ids = ancla_index.resolver(a["to"], a["ancla"])
    b0 = backends["C00_booleano_v1"]
    for gid in ids:
        vv = b0.ver_vecinos(gid, "ambas")
        vecinos = [x["vecino_id"] for x in (vv.get("salientes") or []) + (vv.get("entrantes") or [])]
        for vid in vecinos:
            ok = True
            for cid, b in backends.items():
                out = (b.ver_vecinos(vid, "ambas") if b.tools_version == "v1"
                       else b.ver_vecinos_v2(vid, relacion=None, pagina=1, por_pagina=40))
                lst = [x["vecino_id"] for x in (out.get("salientes") or []) + (out.get("entrantes") or [])]
                ok = ok and (gid in lst)
            if ok:
                return gid, vid
    raise RuntimeError(f"sin (gold, vecino) apto para {par['sample_id']}")


def _consulta_que_trae(backends: dict, gid: str, label: str) -> str:
    """Consulta que trae el gold al top-50 en TODOS los retrievers (id, si no label)."""
    for q in (gid, label):
        if all(any(r["id"] == gid for r in b.buscar_nodos(q, 50)["resultados"]) for b in backends.values()):
            return q
    raise RuntimeError(f"ningún retriever trae {gid}")


def guion_celda(celda: dict, casos: list[dict], plan: dict) -> list:
    """Guion global (en el orden de `casos`) para una celda; `plan[caso_id]` =
    {'tipo': 'A'|'B'|'C', 'gold', 'vecino', 'consulta'}."""
    v2 = celda["tools"] == "v2"
    script = []
    for c in casos:
        p = plan[c["caso_id"]]
        if p["tipo"] == "A":
            script += [turno_tool("buscar_nodos", {"consulta": p["consulta"], "limite": 50}, "t_b"),
                       turno_tool("ver_nodo", {"id": p["gold"]}, "t_v"),
                       turno_final(f"selftest A {c['caso_id']}")]
        elif p["tipo"] == "B":
            script += [turno_tool("buscar_nodos", {"consulta": p["consulta"], "limite": 50}, "t_b"),
                       turno_final(f"selftest B {c['caso_id']}")]
        else:
            vv = ({"id": p["vecino"], "relacion": None, "pagina": 1} if v2
                  else {"id": p["vecino"], "direccion": "ambas"})
            script += [turno_tool("buscar_nodos", {"consulta": "selftest sin gold xyz"}, "t_b"),
                       turno_tool("ver_vecinos", vv, "t_vv")]
            if v2:
                script += [turno_tool("ver_vecinos", {"id": p["vecino"], "pagina": 2, "por_pagina": 5}, "t_vv2")]
            script += [turno_final(f"selftest C {c['caso_id']}", respondible=False)]
    return script


# --------------------------------------------------------------------------- #
# S6: resultados sintéticos del replay                                         #
# --------------------------------------------------------------------------- #
def _res_sintetico(par: dict, variante: str, consultada: bool, vista: bool, htl: bool,
                   n_anclas: int = 1, huer: list | None = None, huer_visto=False, huer_cons=False,
                   pag_gt1: int = 0, latency=1.0) -> dict:
    nc = n_anclas if consultada else 0
    nv = n_anclas if (vista or consultada) else 0
    return {"caso_id": f"{par['sample_id']}::{variante}", "sample_id": par["sample_id"], "variante": variante,
            "estrato": par["estrato"], "sub_estrato": par.get("sub_estrato"),
            "n_anclas": n_anclas, "n_vistas": nv, "n_consultadas": nc, "n_brecha": nv - nc,
            "recall_vista": nv / n_anclas, "recall_consultada": nc / n_anclas, "por_ancla": [],
            "anclas_ausentes_en_este_grafo": [], "replay_ok": True, "replay_fuerte_ok": True,
            "replay_fallas": [], "replay_fuerte_fallas": [],
            "clases": {"tool_calls_used": 15 if htl else 5, "hit_tool_limit": htl, "parse_ok": True, "error": None,
                       "abstencion": False, "final_stop_reason": "end_turn", "truncated_max_tokens": False,
                       "latency_s": latency, "tokens_in": 1000, "tokens_out": 100, "cache_read": 0, "cache_write": 0,
                       "cost_usd_harness": 0.0015, "costo_usd_cli": 0.0015, "api_calls": 3,
                       "llamadas_por_tool": {"buscar_nodos": 2, "ver_nodo": 1, "ver_vecinos": 2},
                       "latencias_por_tool_s": {"buscar_nodos": [0.01, 0.02], "ver_vecinos": [0.03, 0.05]},
                       "n_ver_vecinos_pagina_gt1": pag_gt1, "n_ver_vecinos_con_relacion": 0},
            "huerfanos_p6": [{"nodo": h, "visto": huer_visto, "consultado": huer_cons, "consultado_via": None}
                             for h in (huer or [])],
            "detalle_nodos": {}}


def replays_sinteticos(pares: list[dict], huer: dict, escenario: str) -> dict:
    """Escenarios con propiedades conocidas. Unidad = par (ordenado por sample_id).
    'todo': P1–P6 cumplidas por construcción; 'p1_falla': Δ_c(C00) = 0,05."""
    ps = sorted(pares, key=lambda p: p["sample_id"])
    n = len(ps)
    rank = {p["sample_id"]: i for i, p in enumerate(ps)}          # 0..49
    ebe = [p["sample_id"] for p in ps if p["estrato"] == "E-B" and p.get("sub_estrato") == "entrante"]
    # fracciones de consultada anti-léxica por celda (grupo todos), fuera de E-B/entrante se
    # asignan por rango: los primeros k pares consultan.
    if escenario == "todo":
        frac = {"C00_booleano_v1": 0.60, "C10_bm25_v1": 0.84, "C01_booleano_v2": 0.66, "C11_bm25_v2": 0.90}
    else:   # p1_falla
        frac = {"C00_booleano_v1": 0.96, "C10_bm25_v1": 0.98, "C01_booleano_v2": 0.96, "C11_bm25_v2": 1.00}
    htl_frac = {"C00_booleano_v1": 0.30, "C10_bm25_v1": 0.20, "C01_booleano_v2": 0.10, "C11_bm25_v2": 0.04}
    out = {}
    for cid in ORDEN_CELDAS:
        res = []
        k = round(frac[cid] * n)
        k_htl = round(htl_frac[cid] * n)
        for p in ps:
            sid = p["sample_id"]
            r = rank[sid]
            # literal: siempre consultada (P3 trivial), sin htl
            res.append(_res_sintetico(p, "literal", True, True, False,
                                      huer=huer.get(sid), huer_visto=True, huer_cons=True))
            # anti-léxica
            cons = r < k
            if sid in ebe:      # P4(i): E-B/entrante — orden C00 < C01 y C10 < C11 en anti
                cons = {"C00_booleano_v1": ebe.index(sid) < 4, "C01_booleano_v2": ebe.index(sid) < 6,
                        "C10_bm25_v1": ebe.index(sid) < 7, "C11_bm25_v2": ebe.index(sid) < 9}[cid]
                if escenario != "todo":
                    cons = True
            htl = (r % 10) < round(htl_frac[cid] * 10)     # ~fracción por décimas
            vista = cons or (r % 3 == 0)                    # algunas vistas sin consultar (brecha)
            # P6: huérfanos — vista C00 = C10 (bm25 no mejora), consultada v2 > v1
            hv = (r % 2 == 0)
            hc = {"C00_booleano_v1": False, "C10_bm25_v1": False, "C01_booleano_v2": (r % 2 == 0), "C11_bm25_v2": True}[cid]
            # P4(ii-b): en C01 mejoran los que en C00 tuvieron htl o brecha (clase K); en el resto no
            if cid == "C01_booleano_v2":
                c00_htl = (r % 10) < round(htl_frac["C00_booleano_v1"] * 10)
                c00_cons = r < round(frac["C00_booleano_v1"] * n)
                if sid in ebe:
                    c00_cons = ebe.index(sid) < 4
                c00_vista = c00_cons or (r % 3 == 0)
                enK = c00_htl or (c00_vista and not c00_cons)
                cons = (cons or (enK and r % 2 == 0)) if sid not in ebe else cons
                if not enK and sid not in ebe:
                    cons = c00_cons      # el resto no mejora
            pag = 1 if (cid.endswith("v2") and r % 4 == 0) else 0
            res.append(_res_sintetico(p, "antilexica", cons, vista, htl, huer=huer.get(sid),
                                      huer_visto=hv, huer_cons=hc, pag_gt1=pag, latency=1.0 + r / 10))
        out[cid] = {"celda_id": cid, "n_trazas": len(res), "replay_ok_todos": True, "replay_fuerte_ok_todos": True,
                    "cruce_inmemory_ok_todos": True if cid == "C00_booleano_v1" else None,
                    "n_divergencias": 0, "resultados": res}
    return out


# --------------------------------------------------------------------------- #
# Selftest                                                                     #
# --------------------------------------------------------------------------- #
def main() -> int:
    print("== SELFTEST OFFLINE U-A1.4 (sin API, $0; tools contra Neo4j real) ==")
    if SELFTEST_DIR.exists():
        shutil.rmtree(SELFTEST_DIR)
    SELFTEST_DIR.mkdir(parents=True)
    trazas_base = SELFTEST_DIR / "trazas"
    cache_base = SELFTEST_DIR / "cache"

    # ---------------- S0 ----------------
    print("\n[S0] piezas, KG_Meta, celdas, ensamblado")
    verificar_piezas(verbose=False)
    check("piezas selladas OK (comun_ablacion.verificar_piezas)", True)
    from conexion import abrir_driver
    driver = abrir_driver()
    meta = verificar_kg_meta(driver, GRAFO)
    check(f"KG_Meta.kg_sha256 == KG-Refinado ({meta['kg_sha256'][:16]}…)", meta["kg_sha256"] == KG_REFINADO_SHA256)
    celdas = cargar_celdas()
    check("4 celdas cargadas con sha de archivo/prompt/specs verificado contra el manifest", len(celdas) == 4)
    backends = {cid: BackendCelda(driver, c, grafo=GRAFO) for cid, c in celdas.items()}
    agentes = {cid: AgenteCelda(driver, c, client=ExplodingClient()) for cid, c in celdas.items()}
    check("C00 == harness verbatim (prompt y TOOLS byte a byte)",
          agentes["C00_booleano_v1"].system_prompt == SYSTEM_PROMPT and agentes["C00_booleano_v1"].tools == TOOLS)
    check("C11 == paquete A1.2 verbatim (SYSTEM_PROMPT_V2_PROPUESTO y TOOLS_V2)",
          agentes["C11_bm25_v2"].system_prompt == SYSTEM_PROMPT_V2_PROPUESTO and agentes["C11_bm25_v2"].tools == TOOLS_V2)
    check("4 prompts y 4 juegos de specs distintos entre sí",
          len({sha_texto(a.system_prompt) for a in agentes.values()}) == 4
          and len({json.dumps(a.tools, sort_keys=True) for a in agentes.values()}) == 4)
    check("despacho: modo de búsqueda paridad en C00/C01 y fulltext en C10/C11",
          [backends[c].index_busqueda.modo for c in ORDEN_CELDAS] == ["paridad", "fulltext", "paridad", "fulltext"])
    check("despacho: ver_vecinos v1 (claves *_truncado) en C00/C10 y v2 (pagina) en C01/C11",
          all("salientes_truncado" in backends[c].despachar("ver_vecinos", {"id": tests_replay_v2.HUB}) for c in ("C00_booleano_v1", "C10_bm25_v1"))
          and all(backends[c].despachar("ver_vecinos", {"id": tests_replay_v2.HUB}).get("pagina") == 1 for c in ("C01_booleano_v2", "C11_bm25_v2")))
    for cid, c in celdas.items():
        ns = namespace_celda(c)
        check(f"namespace {cid} = agent|gfp=<sha KG>|cv=<sha harness>+<sha celda>|think=0",
              ns.startswith(f"agent|gfp={KG_REFINADO_SHA256}|cv=") and ns.endswith(f"+{c['archivo_sha256']}|think=0"))

    # ---------------- S1 ----------------
    print("\n[S1] corrida con cliente falso en las 4 celdas")
    pares = cargar_pares()
    orden = orden_resuelto(pares)
    casos = orden[:3]
    print("  casos:", [c["caso_id"] for c in casos])
    ancla_index = indice_anclas_refinado()
    por_id = {p["sample_id"]: p for p in pares}
    plan = {}
    for c, tipo in zip(casos, ("A", "B", "C")):
        par = por_id[c["sample_id"]]
        gid, vid = _gold_y_vecino(driver, ancla_index, par, backends)
        label = backends["C00_booleano_v1"].ver_nodo(gid)["label"]
        plan[c["caso_id"]] = {"tipo": tipo, "gold": gid, "vecino": vid,
                              "consulta": _consulta_que_trae(backends, gid, label)}
    check("precondiciones: gold+vecino y consulta que trae el gold en todos los retrievers", len(plan) == 3)

    resumenes, fakes = {}, {}
    for cid, c in celdas.items():
        script = guion_celda(c, casos, plan)
        fake = FakeSequential(script)
        fakes[cid] = fake
        r = run.correr_celda(cid, client_real=fake, precio_in=PRECIO_IN, precio_out=PRECIO_OUT, cuota_usd=5.0,
                             driver=driver, casos=casos, outdir=trazas_base / cid,
                             db_path=cache_base / f"selftest_{cid}.db", label=f"selftest_{cid}")
        resumenes[cid] = r
        check(f"{cid}: guion consumido completo ({fake.calls}/{len(script)}) y 3 trazas corridas",
              fake.calls == len(script) and r["n_corridos_esta_sesion"] == 3)
        check(f"{cid}: cache_stats.hits == 0 y misses == llamadas ({r['cache_stats']['misses']})",
              r["cache_stats"]["hits"] == 0 and r["cache_stats"]["misses"] == len(script))
        check(f"{cid}: sin freno", r["freno"] is None)

    META_KEYS = {"unidad", "label", "celda_id", "retriever", "tools", "es_control", "system_prompt_sha256",
                 "tools_specs_sha256", "celda_archivo_sha256", "backend", "grafo", "kg_path", "kg_sha256",
                 "caso_id", "sample_id", "variante", "estrato", "sub_estrato", "pos_orden", "semilla_orden",
                 "n_rep", "model", "temperature", "max_tokens", "max_tool_calls", "thinking_enabled",
                 "cache_conversation", "timestamp_inicio", "timestamp_fin", "code_version", "graph_fingerprint",
                 "namespace", "cache_turnos", "precios_cli_usd_por_mtok", "costo_usd_cli", "precios_harness_usd_por_mtok"}
    payloads = {}
    for cid in ORDEN_CELDAS:
        for c in casos:
            with (trazas_base / cid / f"{sanitizar(c['caso_id'])}.json").open(encoding="utf-8") as f:
                payloads[(cid, c["caso_id"])] = json.load(f)
    check("metadata completa en las 12 trazas", all(META_KEYS <= set(p["meta"]) for p in payloads.values()))
    check("steps_full sin truncar (output_chars == len(json)) y con latencia por tool",
          all(sf["output_chars"] == len(json.dumps(sf["output"], ensure_ascii=False)) and "latency_tool_s" in sf
              for p in payloads.values() for sf in p["steps_full"]))
    check("steps_full 1:1 con trace.tool_calls_used", all(len(p["steps_full"]) == p["trace"]["tool_calls_used"] for p in payloads.values()))
    check("raw_turns_agent == nº de llamadas API por caso", all(len(p["raw_turns_agent"]) == len(p["trace"]["api_calls"]) for p in payloads.values()))
    check("celdas v2: la traza C tiene una llamada ver_vecinos con pagina=2 persistida",
          all(any(sf["tool"] == "ver_vecinos" and sf["input"].get("pagina") == 2 for sf in payloads[(cid, casos[2]["caso_id"])]["steps_full"])
              for cid in ("C01_booleano_v2", "C11_bm25_v2")))
    check("graph_fingerprint de llm_cache == el publicado en EV2 base v3 (91573e01c7135581) y code_version aa15d9c9b5b7 (cuarteto intacto)",
          all(p["meta"]["graph_fingerprint"] == "91573e01c7135581" and p["meta"]["code_version"] == "aa15d9c9b5b7" for p in payloads.values()))
    doms = set()
    for cid in ORDEN_CELDAS:
        con = sqlite3.connect(cache_base / f"selftest_{cid}.db")
        doms |= {r[0] for r in con.execute("SELECT DISTINCT domain FROM cache UNION SELECT DISTINCT domain FROM access_log")}
        con.close()
    check("dbs con un solo dominio 'agent' (ningún juez)", doms == {"agent"})
    check("payload del control byte-idéntico al harness: system y tools del request == SYSTEM_PROMPT/TOOLS",
          all(json.loads(r[0])["system"] == SYSTEM_PROMPT and json.loads(r[0])["tools"] == TOOLS
              for r in sqlite3.connect(cache_base / "selftest_C00_booleano_v1.db").execute("SELECT request_json FROM cache")))

    # ---------------- S2 ----------------
    print("\n[S2] retoma sin repago")
    cid = "C00_booleano_v1"
    r2 = run.correr_celda(cid, client_real=ExplodingClient(), precio_in=PRECIO_IN, precio_out=PRECIO_OUT, cuota_usd=5.0,
                          driver=driver, casos=casos, outdir=trazas_base / cid,
                          db_path=cache_base / f"selftest_{cid}.db", label=f"selftest_{cid}")
    check("retoma total: 3 ya persistidos, 0 corridos, 0 accesos a la caché",
          r2["n_ya_persistidos_al_iniciar"] == 3 and r2["n_corridos_esta_sesion"] == 0 and r2["cache_stats"]["accesses"] == 0)
    p_b = trazas_base / cid / f"{sanitizar(casos[1]['caso_id'])}.json"
    orig = json.loads(p_b.read_text(encoding="utf-8"))
    p_b.unlink()
    r3 = run.correr_celda(cid, client_real=ExplodingClient(), precio_in=PRECIO_IN, precio_out=PRECIO_OUT, cuota_usd=5.0,
                          driver=driver, casos=casos, outdir=trazas_base / cid,
                          db_path=cache_base / f"selftest_{cid}.db", label=f"selftest_{cid}_reanudacion")
    nuevo = json.loads(p_b.read_text(encoding="utf-8"))
    check("retoma parcial: el caso borrado se regenera desde la caché (misses 0, hits == sus llamadas) y queda DECLARADO",
          r3["n_corridos_esta_sesion"] == 1 and r3["cache_stats"]["misses"] == 0
          and r3["cache_stats"]["hits"] == len(orig["trace"]["api_calls"]) and r3["casos_con_hits_esta_sesion"]
          and r3["casos_con_hits_esta_sesion"][0]["hits"] == len(orig["trace"]["api_calls"]))
    check("retoma parcial: misma respuesta final y mismos steps que la traza original",
          nuevo["trace"]["final_json"] == orig["trace"]["final_json"] and nuevo["trace"]["steps"] == orig["trace"]["steps"])

    # ---------------- S3 ----------------
    print("\n[S3] 0 cross-hits provocado")
    con0 = sqlite3.connect(cache_base / "selftest_C00_booleano_v1.db")
    con1 = sqlite3.connect(cache_base / "selftest_C10_bm25_v1.db")
    keys0 = {r[0] for r in con0.execute("SELECT key FROM cache")}
    keys1 = {r[0] for r in con1.execute("SELECT key FROM cache")}
    reqs0 = [r[0] for r in con0.execute("SELECT request_json FROM cache")]
    con0.close(); con1.close()
    check("C10 corrió el mismo guion/preguntas que C00 y su db fresca cerró con hits == 0",
          resumenes["C10_bm25_v1"]["cache_stats"]["hits"] == 0 and fakes["C10_bm25_v1"].calls == fakes["C00_booleano_v1"].calls)
    check("keys de C00 ∩ keys de C10 = ∅ (namespaces distintos ⇒ keys distintas)", not (keys0 & keys1))
    ns0, ns1 = namespace_celda(celdas["C00_booleano_v1"]), namespace_celda(celdas["C10_bm25_v1"])
    check("re-hash de los requests de C00 con el namespace de C00 → todos presentes; con el de C10 → ninguno",
          all(lc.compute_key(ns0, rq) in keys0 for rq in reqs0) and not any(lc.compute_key(ns1, rq) in keys1 for rq in reqs0))

    # ---------------- S4 ----------------
    print("\n[S4] freno por proyección")
    casos4 = orden[:4]
    plan4 = dict(plan)
    c4 = casos4[3]
    par4 = por_id[c4["sample_id"]]
    gid4, vid4 = _gold_y_vecino(driver, ancla_index, par4, backends)
    plan4[c4["caso_id"]] = {"tipo": "B", "gold": gid4, "vecino": vid4,
                            "consulta": _consulta_que_trae(backends, gid4, backends["C00_booleano_v1"].ver_nodo(gid4)["label"])}
    cidf = "C01_booleano_v2"
    fake4 = FakeSequential(guion_celda(celdas[cidf], casos4, plan4))
    r4 = run.correr_celda(cidf, client_real=fake4, precio_in=PRECIO_IN, precio_out=PRECIO_OUT, cuota_usd=0.0001,
                          driver=driver, casos=casos4, outdir=trazas_base / f"{cidf}_freno",
                          db_path=cache_base / f"selftest_{cidf}_freno.db", label=f"selftest_{cidf}_freno")
    check("freno por proyección tras 3 casos hechos: 4º no corrido, freno.tipo == 'proyeccion' declarado",
          r4["freno"] is not None and r4["freno"]["tipo"] == "proyeccion" and r4["n_corridos_esta_sesion"] == 3
          and fake4.calls < len(fake4.script))

    # ---------------- S5 ----------------
    print("\n[S5] replay determinístico por celda")
    tchecks = tests_replay_v2.correr_tests(driver=driver, verbose=False)
    check(f"tests del adaptador v2-aware: {sum(1 for _, ok in tchecks if ok)}/{len(tchecks)} PASS", all(ok for _, ok in tchecks))
    huer = huerfanos_p6()
    idx_mem = GraphIndex(cargar_runtime("v3"))
    salidas = {}
    for cid in ORDEN_CELDAS:
        kw = dict(driver=driver, ancla_index=ancla_index, pares_por_id=por_id, huerfanos=huer,
                  trazas_dir=trazas_base / cid, index_inmemory=idx_mem, casos_esperados=casos)
        s1 = rep.replay_celda(cid, **kw)
        s2 = rep.replay_celda(cid, **kw)
        salidas[cid] = s1
        check(f"{cid}: replay estándar y fuerte OK en las 3 trazas; doble corrida byte-idéntica",
              s1["replay_ok_todos"] and s1["replay_fuerte_ok_todos"] and s1["n_trazas"] == 3 and rep._canon(s1) == rep._canon(s2))
        by = {r["caso_id"]: r for r in s1["resultados"]}
        A, B, C = (by[c["caso_id"]] for c in casos)
        check(f"{cid}: caso A vista+consultada (n_consultadas ≥ 1, brecha 0)", A["n_consultadas"] >= 1 and A["n_vistas"] >= 1 and A["n_brecha"] == 0)
        check(f"{cid}: caso B vista sin consultar (n_brecha ≥ 1, n_consultadas 0)", B["n_brecha"] >= 1 and B["n_consultadas"] == 0)
        check(f"{cid}: caso C consultada vía ver_vecinos + abstención declarada",
              C["n_consultadas"] >= 1 and C["clases"]["abstencion"] is True
              and any(pn["consultado_via"] == "ver_vecinos" for lst in C["detalle_nodos"].values() for pn in lst if pn["consultado"]))
        if cid.endswith("v2"):
            check(f"{cid}: caso C registra 1 llamada ver_vecinos con pagina > 1", C["clases"]["n_ver_vecinos_pagina_gt1"] == 1)
        if cid == "C00_booleano_v1":
            check("C00: cruce con GraphIndex in-memory OK (mismos conteos y por_ancla, replay OK)", s1["cruce_inmemory_ok_todos"] is True)
    # replay_todo (escritura + verificación) sobre el árbol del selftest
    out_rep = SELFTEST_DIR / "resultados_replay"
    rt = rep.replay_todo(ORDEN_CELDAS, driver=driver, trazas_base=trazas_base, out_dir=out_rep, doble=True, verbose=False)
    check("replay_todo: 4 archivos escritos, doble corrida byte-idéntica en las 4 celdas",
          all(v["doble_corrida_byte_identica"] for v in rt["verificacion"]["celdas"].values())
          and all((out_rep / f"replay_{c}.json").exists() for c in ORDEN_CELDAS))

    # ---------------- S6 ----------------
    print("\n[S6] pipeline de análisis completo sobre resultados sintéticos")
    # (a) análisis sobre las 3 trazas reales del selftest (n chico ⇒ todo no evaluable, sin excepciones)
    an_real = ana.analizar({c: salidas[c] for c in ORDEN_CELDAS}, huer, n_boot=200)
    check("análisis sobre 3 trazas reales (ningún par con sus 2 variantes ⇒ 0 apareados) corre sin excepciones; P1 no evaluable",
          an_real["predicciones"]["P1"]["veredicto"] == "no evaluable" and an_real["n_pares_apareados"] == 0)
    # (b) escenario 'todo cumplido'
    reps = replays_sinteticos(pares, huer, "todo")
    an1 = ana.analizar(reps, huer, n_boot=2000)
    an1b = ana.analizar(reps, huer, n_boot=2000)
    check("determinismo: dos corridas del análisis (bootstrap incluido) son idénticas",
          json.dumps(an1, sort_keys=True) == json.dumps(an1b, sort_keys=True))
    T = an1["tabla_central"]
    todos_anti = {c: T[c]["todos"]["antilexica"]["recall_consultada_micro"] for c in ORDEN_CELDAS}
    # valores esperados a mano: fracción de pares (n_anclas=1) consultados en anti, contando E-B/entrante aparte
    ps = sorted(pares, key=lambda p: p["sample_id"])
    ebe = [p["sample_id"] for p in ps if p["estrato"] == "E-B" and p.get("sub_estrato") == "entrante"]
    def esperado(cid, frac, ebe_k):
        k = round(frac * len(ps))
        idx = {p["sample_id"]: i for i, p in enumerate(ps)}
        cons = 0
        for sid in idx:
            if sid in ebe:
                cons += 1 if ebe.index(sid) < ebe_k else 0
            elif cid == "C01_booleano_v2":
                cons += 1 if reps[cid]["resultados"] and next(r for r in reps[cid]["resultados"] if r["caso_id"] == f"{sid}::antilexica")["n_consultadas"] else 0
            else:
                cons += 1 if idx[sid] < k else 0
        return round(cons / len(ps), 4)
    check("tabla central: recall consultada micro anti-léxica de C00/C10/C11 == valores construidos",
          todos_anti["C00_booleano_v1"] == esperado("C00_booleano_v1", 0.60, 4)
          and todos_anti["C10_bm25_v1"] == esperado("C10_bm25_v1", 0.84, 7)
          and todos_anti["C11_bm25_v2"] == esperado("C11_bm25_v2", 0.90, 9))
    check("tabla central: literal recall 1.0 en las 4 celdas; n_pares 50; n_anclas == n_casos (1 ancla por caso)",
          all(T[c]["todos"]["literal"]["recall_consultada_micro"] == 1.0 and T[c]["todos"]["literal"]["n_pares"] == 50
              and T[c]["todos"]["literal"]["n_anclas"] == T[c]["todos"]["literal"]["n_casos"] for c in ORDEN_CELDAS))
    check("cohortes E-E y E-A..E-D separadas: n_pares suman 50 y coinciden con los estratos",
          T["C00_booleano_v1"]["cohorte_nucleo_limpio_EE"]["literal"]["n_pares"] + T["C00_booleano_v1"]["cohorte_dirigida_EA_ED"]["literal"]["n_pares"] == 50
          and T["C00_booleano_v1"]["cohorte_nucleo_limpio_EE"]["literal"]["n_pares"] == sum(1 for p in pares if p["estrato"] == "E-E"))
    d = an1["diferencias_apareadas"]
    k = "dif_consultada_micro::antilexica::C10_bm25_v1-C00_booleano_v1"
    check("bootstrap: punto de C10−C00 (anti, micro) == diferencia de la tabla y el IC lo contiene",
          abs(d["estadisticos"][k]["punto"] - round(todos_anti["C10_bm25_v1"] - todos_anti["C00_booleano_v1"], 4)) < 1e-9
          and d["estadisticos"][k]["ic95_inf"] <= d["estadisticos"][k]["punto"] <= d["estadisticos"][k]["ic95_sup"]
          and d["n_remuestreos"] == 2000 and d["semilla"] == "bootstrap-ablacion-v1")
    P = an1["predicciones"]
    print("   veredictos escenario 'todo':", P["resumen"])
    check("escenario 'todo cumplido': P1–P6 cumplidas", all(v == "cumplida" for v in P["resumen"].values()))
    check("P1: Δ_c(C00) == 0.60−… ≥ 0.15 y refleja la tabla",
          P["P1"]["delta_c_C00"] == round(1.0 - todos_anti["C00_booleano_v1"], 4))
    check("P4(i) sobre E-B/entrante con n_pares == 9 y P6 sobre 11 pares con huérfano",
          P["P4"]["sub"]["i_EB_entrante"]["n_pares"] == len(ebe) == 9 and P["P6"]["n_pares_con_huerfano"] == 11)
    tl = an1["tasas_y_latencias"]["C00_booleano_v1"]["todas"]
    check("tasas: hit_tool_limit y latencia p50/p95 computadas; abstención 0 en sintéticos",
          tl["tasa_hit_tool_limit"] > 0 and tl["latencia_s_p50"] is not None and tl["latencia_s_p95"] >= tl["latencia_s_p50"]
          and tl["tasa_abstencion"] == 0.0)
    md = ana.render_md(an1)
    check("render markdown del análisis (> 40 líneas, con tabla central y predicciones)",
          md.count("\n") > 40 and "Tabla central" in md and "P6" in md)
    # (c) escenario 'P1 falla'
    an2 = ana.analizar(replays_sinteticos(pares, huer, "p1_falla"), huer, n_boot=200)
    P2 = an2["predicciones"]
    print("   veredictos escenario 'p1_falla':", P2["resumen"])
    check("escenario 'P1 falla': P1 no cumplida; P2–P6 'no evaluable' con veredicto_propio reportado",
          P2["P1"]["veredicto"] == "no cumplida" and all(P2[k]["veredicto"] == "no evaluable" and "veredicto_propio" in P2[k]
                                                         for k in ("P2", "P3", "P4", "P5", "P6")))
    # (d) clase chica ⇒ no evaluable a priori (P6 con 3 pares)
    huer3 = {k: v for k, v in list(huer.items())[:3]}
    an3 = ana.analizar(replays_sinteticos(pares, huer3, "todo"), huer3, n_boot=100)
    check("clase con < 8 pares (P6 con 3) ⇒ 'no evaluable' a priori",
          an3["predicciones"]["P6"]["veredicto"] == "no evaluable" and an3["predicciones"]["P6"]["n_pares_con_huerfano"] == 3)
    (SELFTEST_DIR / "analisis_sintetico_todo.json").write_text(json.dumps(an1, ensure_ascii=False, indent=1), encoding="utf-8")
    (SELFTEST_DIR / "reporte_sintetico_todo.md").write_text(md, encoding="utf-8")

    # ---------------- S7 ----------------
    print("\n[S7] estimación")
    e = est.estimar(PRECIO_IN, PRECIO_OUT)
    check(f"estimación: {e['n_trazas']} trazas; escenarios {e['escenarios']}; todos bajo tope {e['tope_laudado_usd']}",
          e["n_trazas"] == 400 and e["todos_bajo_tope"])

    driver.close()
    fails = [n for n, ok in _checks if not ok]
    print(f"\n== {len(_checks) - len(fails)}/{len(_checks)} PASS ==")
    if fails:
        print("FALLARON:", *fails, sep="\n  - ")
    (SELFTEST_DIR / "selftest_resultado.json").write_text(
        json.dumps({"checks": [{"nombre": n, "ok": ok} for n, ok in _checks], "n_pass": len(_checks) - len(fails),
                    "n_total": len(_checks)}, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0 if not fails else 1


if __name__ == "__main__":
    raise SystemExit(main())
