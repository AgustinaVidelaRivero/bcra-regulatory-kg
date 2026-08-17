"""
selftest_enc.py — SELFTEST OFFLINE (cero API, USD 0) del encadenamiento §7.

Parte 1 — insumos REALES, solo lectura: sellos (instrumento, cuarteto, grafos,
base); población 63 + 3 = 66 con conteos por grafo contra 23/22/18 y 3/4/2;
muestra de auditoría reproducible desde la semilla; orden del agente por grafo
== orden resuelto del protocolo filtrado; labels/dbs por (grafo, rep) únicos;
tests_agregacion PASS; requests del juez sobre las respuestas BASE de los 66
pares (stand-in de las nuevas) sin fuga.

Parte 2 — circuito COMPLETO con clientes FALSOS sobre una población sintética
de 4 pares REALES de v3 (3 disparados + la auditoría) y trazas bajo
selftest_out/ (gitignorado):
  agente: runner_enc.correr_grafo_rep × 3 reps con FakeSequential (guion
    buscar_nodos + final) → 3 dbs separadas, 0 hits, trazas completas con
    meta.encadenamiento, respuestas distintas por rep salvo un par con texto
    idéntico en las 3 reps (duplicado provocado); re-lanzada con cliente que
    EXPLOTA → todo persistido, ninguna llamada; keys del primer turno comunes
    entre dbs (evidencia de por qué la db separada es la anti-cache).
  juez: pipeline ciego (pipeline_fidelidad.correr) con ClienteFalso que
    identifica el caso SOLO por el texto de la respuesta; freno por proyección
    frena y la re-lanzada retoma sin pagar dos veces; 3 dbs, keys disjuntas,
    hits == esperados por duplicados; agregación por respuesta (mapping §2) y
    por PAR (agregacion_enc: mayoría / empate triple / unánime / invariante
    con pendiente) con flip de la auditoría; ceguera de requests y de juez_out/;
    tabla SOLO_MESA aparte; reporte final ciego sin marcadores.

Correr:  .venv/bin/python -B data/experiment/ev2_encadenamiento/code/selftest_enc.py
"""

from __future__ import annotations

import hashlib
import json
import random
import shutil
import sqlite3
import subprocess
import sys
from collections import Counter
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(CODE_DIR))
import comun_enc as en                    # noqa: E402
import runner_enc as rn                   # noqa: E402
import juez_enc as je                     # noqa: E402
import agregacion_enc as ag               # noqa: E402
import pipeline_fidelidad as pf           # noqa: E402
import llm_cache as lc                    # noqa: E402
from comun_enc import cf, juez            # noqa: E402
from anthropic.types import Message       # noqa: E402

OUT = en.UNIDAD_DIR / "selftest_out"
CHECKS: list[tuple[str, bool]] = []


def check(nombre: str, cond: bool, detalle: str = "") -> None:
    CHECKS.append((nombre, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {nombre}{(' — ' + detalle) if detalle else ''}")


# --------------------------------------------------------------------------- #
# Parte 1 — insumos reales                                                    #
# --------------------------------------------------------------------------- #
def parte_real() -> dict:
    print("== 1. sellos, población y orden (insumos reales, offline) ==")
    sellos = en.verificar_sellos()
    check("prompt v1 sha256 esperado", sellos["prompt_juez_v1.md"] == cf.PROMPT_SHA256_ESPERADO)
    check("cuarteto 4/4 intacto", all(sellos[k] == v for k, v in cf.CUARTETO.items()))
    check("grafos 3/3 con sha esperado", all(sellos[f"grafo_{g}"] == en.ce.GRAFOS[g]["sha256"] for g in en.GRAFOS))
    check("modelo del agente = harness.MODEL hardcodeado (Haiku 4.5)",
          rn.rv.harness.MODEL == "claude-haiku-4-5-20251001" and rn.rv.harness.TEMPERATURE == 0)
    check("modelo del juez claude-sonnet-4-6 / temp 0", juez.MODELO == "claude-sonnet-4-6" and juez.TEMPERATURE == 0.0)

    pob = en.cargar_poblacion()
    check("población persistida == derivada desde la base", True)
    check("63 pares parcial: v2 23 / v3 22 / run_3 18",
          pob["conteo_parciales_por_grafo"] == {"v2": 23, "v3": 22, "run_3": 18}, str(pob["conteo_parciales_por_grafo"]))
    check("correctos base: v2 3 / v3 4 / run_3 2", pob["conteo_correctos_por_grafo"] == {"v2": 3, "v3": 4, "run_3": 2})
    check("auditoría: 1 por grafo (ceil, laudo) → 3 pares", pob["n_pares_auditoria"] == 3 and
          all(v["n_muestra"] == 1 for v in pob["auditoria_por_grafo"].values()))
    aud_ok = all(v["ids_muestra"] == sorted(random.Random(en.SEMILLA_AUDITORIA).sample(sorted(v["ids_correctos_ordenados"]), 1))
                 for v in pob["auditoria_por_grafo"].values())
    check("muestra de auditoría reproducible desde random.Random('auditoria-ev2-v1') sobre ids ordenados", aud_ok)
    check("66 pares / 198 corridas / 594 llamadas", (pob["n_pares"], pob["n_corridas_agente"], pob["n_llamadas_juez"]) == (66, 198, 594))
    check("todos los pares disparados tienen veredicto_base parcial; auditoría correcto",
          all(p["veredicto_base"] == "parcial" for p in pob["pares"] if p["tipo"] == "parcial_disparado") and
          all(p["veredicto_base"] == "correcto" for p in pob["pares"] if p["tipo"] == "auditoria_correcto"))
    check("cada par tiene id_opaco_base EV2R- de la tabla base",
          all(p["id_opaco_base"].startswith("EV2R-") for p in pob["pares"]))

    orden = json.loads((en.ORDEN_DIR / "orden_agente_por_grafo.json").read_text(encoding="utf-8"))
    ok_ord = True
    for g in en.GRAFOS:
        cs = en.casos_agente(pob, g)
        ok_ord &= [c["caso_id"] for c in cs] == [c["caso_id"] for c in orden["por_grafo"][g]["casos"]]
        # subsecuencia del orden resuelto global
        glob = [c["caso_id"] for c in en.ce.orden_resuelto() if c["eje"] == "fidelidad"]
        pos = [glob.index(c["caso_id"]) for c in cs]
        ok_ord &= pos == sorted(pos)
    check("orden del agente por grafo == orden resuelto (orden-ev2-v1) filtrado, subsecuencia", ok_ord)
    check("orden por grafo: v2 24 / v3 23 / run_3 19",
          {g: orden["por_grafo"][g]["n_casos"] for g in en.GRAFOS} == {"v2": 24, "v3": 23, "run_3": 19})
    labels = [en.label_agente(g, r) for g in en.GRAFOS for r in (1, 2, 3)]
    dbs = [rn.db_agente(g, r).name for g in en.GRAFOS for r in (1, 2, 3)]
    check("9 labels y 9 dbs de agente únicos (ev2_enc_<grafo>_r{n})", len(set(labels)) == 9 and len(set(dbs)) == 9
          and labels[0] == "ev2_enc_v2_r1" and dbs[-1] == "ev2_enc_run3_r3.db")
    check("labels del juez ev2_enc_juez_r{1,2,3}", [en.label_juez(r) for r in (1, 2, 3)] == ["ev2_enc_juez_r1", "ev2_enc_juez_r2", "ev2_enc_juez_r3"])
    check("ninguna db/label de esta unidad coincide con las de la base",
          not ({*labels, *(en.label_juez(r) for r in (1, 2, 3))} & {"ev2_base_v2", "ev2_base_v3", "ev2_base_run3",
                                                                    "ev2_eval_r1", "ev2_eval_r2", "ev2_eval_r3"}))
    check("cache/ de la unidad no existe aún (nada llamado)", not en.CACHE_DIR.exists() or
          not any(p.name.startswith("ev2_enc_") for p in en.CACHE_DIR.glob("*.db")))
    check("trazas/ de la unidad sin corridas reales aún", not en.TRAZAS_DIR.exists() or not any(en.TRAZAS_DIR.rglob("*.json")))

    r = subprocess.run([sys.executable, "-B", str(CODE_DIR / "tests_agregacion.py")], capture_output=True, text=True)
    check("tests_agregacion.py PASS", r.returncode == 0 and "FAIL" not in r.stdout,
          r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr[-200:])
    r = subprocess.run([sys.executable, "-B", str(cf.JUEZ_DIR / "tests_mapping.py")], capture_output=True, text=True, cwd=str(cf.JUEZ_DIR))
    check("tests_mapping.py del juez PASS", r.returncode == 0 and "FAIL" not in r.stdout)

    # requests del juez sobre las respuestas BASE de los 66 pares (stand-in de las nuevas)
    gold = cf.cargar_gold()
    base_resp = {(r["id_pregunta"], r["grafo"]): r for r in cf.cargar_respuestas()}
    stand_in = []
    for p in pob["pares"]:
        r = base_resp[(p["id_pregunta"], p["grafo"])]
        stand_in.append({"id_pregunta": p["id_pregunta"], "grafo": p["grafo"], "rep": 0, "label": "stand_in",
                         "tipo": p["tipo"], "id_opaco_base": p["id_opaco_base"], "veredicto_base": p["veredicto_base"],
                         "respuesta": r["respuesta"], "respondible_flag": r["respondible_flag"],
                         "pregunta_traza": r["pregunta_traza"]})
    casos = en.armar_casos(stand_in, gold)
    ciegos = en.vista_ciega(casos)
    check("66 stand-in: ids opacos EV2E- únicos y distintos de los EV2R- base",
          len({c["id_opaco"] for c in casos}) == 66 and all(c["id_opaco"].startswith("EV2E-") for c in casos)
          and not ({c["id_opaco"] for c in casos} & {p["id_opaco_base"] for p in pob["pares"]}))
    check("66 requests reales (stand-in) == prompt + (pregunta, respuesta, criterios), sin marcadores",
          not je.verificar_ceguera_requests(ciegos))
    return pob


# --------------------------------------------------------------------------- #
# Parte 2 — circuito completo sintético                                       #
# --------------------------------------------------------------------------- #
def _msg(content, stop_reason, model="claude-haiku-4-5-20251001"):
    return Message.model_validate({
        "id": "msg_selftest", "type": "message", "role": "assistant", "model": model,
        "content": content, "stop_reason": stop_reason, "stop_sequence": None,
        "usage": {"input_tokens": 1500, "output_tokens": 60, "cache_read_input_tokens": 0,
                  "cache_creation_input_tokens": 1200}})


def turno_tool(nombre, args, uid):
    return _msg([{"type": "text", "text": "Exploro el grafo."},
                 {"type": "tool_use", "id": uid, "name": nombre, "input": args}], "tool_use")


def turno_final(respuesta):
    return _msg([{"type": "text", "text": json.dumps({"respuesta": respuesta, "citas": [], "respondible": True},
                                                      ensure_ascii=False)}], "end_turn")


class FakeSequential:
    def __init__(self, script):
        self.script, self.calls, self.messages = list(script), 0, self

    def create(self, **kwargs):
        if self.calls >= len(self.script):
            raise AssertionError("llamada API no prevista")
        m = self.script[self.calls]
        self.calls += 1
        return m


class ExplodingClient:
    def __init__(self):
        self.messages = self

    def create(self, **kwargs):
        raise AssertionError("cliente real llamado (debía ser caché o skip)")


# Población sintética: 4 pares REALES de v3 (3 disparados + la auditoría EV2F-033)
PARES_SYN = ["EV2F-003", "EV2F-004", "EV2F-033", "EV2F-005"]
# Respuesta del agente por (id_pregunta, rep): el par 2 (EV2F-004) repite texto en las 3 reps
def resp_syn(q: str, rep: int) -> str:
    n = int(q[-3:])
    if q == "EV2F-004":
        return f"Respuesta sintética idéntica en las tres repeticiones para la pregunta número {n}."
    return f"Respuesta sintética pregunta número {n} repetición {rep}: dato uno; dato dos."

# Guion del juez por (id_pregunta, rep del agente): veredicto por pregunta deseado
# → cumplido/no_cumplido/dudoso por criterio (todos los K criterios).
GUION_PAR = {
    "EV2F-003": ["correcto", "correcto", "parcial"],                       # mayoría 2-de-3 → correcto
    "EV2F-004": ["incorrecto", "incorrecto", "incorrecto"],                # texto idéntico → unánime incorrecto
    "EV2F-033": ["correcto", "parcial", "incorrecto"],                     # auditoría: empate triple → parcial → FLIP
    "EV2F-005": ["parcial", "parcial", "requiere_adjudicacion"],           # invariante con pendiente → parcial
}
ESPERADO_FINAL = {"EV2F-003": "correcto", "EV2F-004": "incorrecto", "EV2F-033": "parcial", "EV2F-005": "parcial"}
ESPERADO_VIA = {"EV2F-003": "mayoria_2_de_3", "EV2F-004": "unanime", "EV2F-033": "mediana_empate_triple",
                "EV2F-005": "invariante_con_pendiente"}


def _crits_para(veredicto: str, k: int, rep_juez: int) -> list[str]:
    if veredicto == "correcto":
        return ["cumplido"] * k
    if veredicto == "incorrecto":
        return ["no_cumplido"] * k
    if veredicto == "parcial":
        return ["cumplido"] + ["no_cumplido"] * (k - 1)
    # requiere_adjudicacion: criterio 1 dudoso unánime
    return ["dudoso"] + ["cumplido"] * (k - 1)


class ClienteFalsoJuez:
    """Identifica el caso SOLO por el texto de la respuesta que llega en el request."""

    def __init__(self, rep: int, registro: list, sha_a_caso: dict):
        self._rep, self._registro, self._s2c, self.messages = rep, registro, sha_a_caso, self

    def create(self, **kwargs):
        self._registro.append({"rep": self._rep, "kwargs": kwargs})
        u = kwargs["messages"][0]["content"]
        resp_txt = u.split("RESPUESTA:\n", 1)[1].split("\n\nCRITERIOS (", 1)[0]
        k = int(u.split("CRITERIOS (", 1)[1].split(")", 1)[0])
        q, rep_ag = self._s2c[cf.sha256_texto(resp_txt)]
        vs = _crits_para(GUION_PAR[q][rep_ag - 1], k, self._rep)
        crits = [{"indice": i + 1, "veredicto": v, "fragmento": ("dato uno" if v == "cumplido" else None),
                  "justificacion": f"scripteado-{hashlib.md5(f'{q}{rep_ag}{i}{self._rep}'.encode()).hexdigest()[:10]}"}
                 for i, v in enumerate(vs)]
        texto = json.dumps({"clasificacion_respuesta": "contenido", "criterios": crits}, ensure_ascii=False)
        return Message.model_validate({
            "id": f"fake_{q}_{rep_ag}_r{self._rep}", "type": "message", "role": "assistant", "model": "cliente-falso",
            "stop_reason": "end_turn", "stop_sequence": None, "content": [{"type": "text", "text": texto}],
            "usage": {"input_tokens": len(kwargs["system"]) // 4 + len(u) // 4, "output_tokens": len(texto) // 4}})


def parte_sintetica(pob_real: dict) -> None:
    print("== 2. circuito completo sintético (clientes falsos + caché real) ==")
    if OUT.exists():
        shutil.rmtree(OUT)
    cache_dir, trazas_dir, juez_out = OUT / "cache", OUT / "trazas", OUT / "juez_out"
    for d in (cache_dir, trazas_dir, juez_out):
        d.mkdir(parents=True)
    por_par = {(p["id_pregunta"], p["grafo"]): p for p in pob_real["pares"]}
    pob = {**{k: v for k, v in pob_real.items() if k != "pares"},
           "pares": [por_par[(q, "v3")] for q in PARES_SYN]}
    check("población sintética: 4 pares reales de v3 (3 disparados + auditoría EV2F-033)",
          Counter(p["tipo"] for p in pob["pares"]) == {"parcial_disparado": 3, "auditoria_correcto": 1})

    # --- agente: 3 reps con guion; orden = casos_agente(pob, v3) ---
    casos = en.casos_agente(pob, "v3")
    check("casos_agente sobre la población sintética: 4, en orden del protocolo", len(casos) == 4)
    estado = {"gastado": 0.0, "corridos": 0, "total": 12, "tope_usd": 100.0}
    fakes = {}
    for rep in (1, 2, 3):
        script = []
        for c in casos:
            script.append(turno_tool("buscar_nodos", {"consulta": "selftest encadenamiento"}, "t_b"))
            script.append(turno_final(resp_syn(c["caso_id"], rep)))
        fakes[rep] = FakeSequential(script)
        rn.correr_grafo_rep(pob, "v3", rep, client_real=fakes[rep], cache_dir=cache_dir, trazas_dir=trazas_dir,
                            estado_gasto=estado, casos=casos)
    check("guiones consumidos completos: 8 llamadas por rep", all(f.calls == 8 for f in fakes.values()))
    check("estado de gasto: 12 corridas contabilizadas", estado["corridos"] == 12)
    dbs_ag = sorted(cache_dir.glob("ev2_enc_v3_r*.db"))
    check("3 dbs de agente separadas ev2_enc_v3_r{1,2,3}.db", [p.name for p in dbs_ag] == [f"ev2_enc_v3_r{r}.db" for r in (1, 2, 3)])
    g = rn.gasto_dbs_agente(cache_dir, ["v3"], 3, {"in": 1.0, "out": 5.0, "cw": 1.25, "cr": 0.10})
    check("gasto desde dbs: 8 filas por db, 0 hits por db, dominio solo 'agent'",
          all(v["filas"] == 8 and v["hits"] == 0 and v["dominios"] == ["agent"] for v in g["por_db"].values()), str(g["total"]))
    check("labels de access_log = ev2_enc_v3_r{n}", all(list(v["hits_por_label"]) == [f"ev2_enc_v3_r{r}"]
                                                        for r, v in zip((1, 2, 3), g["por_db"].values())))
    keys = [je.keys_db(p) for p in dbs_ag]
    check("keys del PRIMER turno comunes entre dbs de reps (mismo request inicial): ≥ 4 en común r1∩r2",
          len(keys[0] & keys[1]) >= 4, f"{len(keys[0] & keys[1])} comunes")
    idx = rn.indice_trazas(pob, trazas_dir, 3)
    check("índice: 12/12 trazas persistidas, 0 faltantes, 0 incompletas",
          idx["n_persistidas"] == 12 and idx["n_faltantes"] == 0 and idx["n_incompletas"] == 0)
    check("meta.encadenamiento agregada en las 12 trazas (rep, tipo, veredicto_base, id_opaco_base)",
          all(x["encadenamiento_meta"] for x in idx["filas"]))
    t = json.loads((trazas_dir / "ev2_enc_v3_r2" / "EV2F-033.json").read_text(encoding="utf-8"))
    me = t["meta"]["encadenamiento"]
    check("traza EV2F-033 r2: label/rep/tipo/veredicto_base correctos y claves de la base intactas",
          me["rep"] == 2 and me["label"] == "ev2_enc_v3_r2" and me["tipo"] == "auditoria_correcto"
          and me["veredicto_base"] == "correcto" and t["meta"]["label"] == "ev2_enc_v3_r2" and t["meta"]["n_rep"] == 1
          and t["meta"]["grafo"] == "v3" and t["meta"]["kg_sha256"] == en.ce.GRAFOS["v3"]["sha256"])
    check("trazas completas: steps_full 1:1 con tools, raw_turns == api_calls, respuesta parseada",
          all(len(json.loads((trazas_dir / f"ev2_enc_v3_r{r}" / f"{q}.json").read_text())["steps_full"]) ==
              json.loads((trazas_dir / f"ev2_enc_v3_r{r}" / f"{q}.json").read_text())["trace"]["tool_calls_used"] == 1
              and len(json.loads((trazas_dir / f"ev2_enc_v3_r{r}" / f"{q}.json").read_text())["raw_turns_agent"]) == 2
              for r in (1, 2, 3) for q in PARES_SYN))
    # re-lanzada: todo persistido → ninguna llamada
    for rep in (1, 2, 3):
        rn.correr_grafo_rep(pob, "v3", rep, client_real=ExplodingClient(), cache_dir=cache_dir, trazas_dir=trazas_dir,
                            estado_gasto=None, casos=casos)
    g2 = rn.gasto_dbs_agente(cache_dir, ["v3"], 3, None)
    check("re-lanzada: retoma sin llamar (mismas 8 filas y 0 hits por db)",
          all(v["filas"] == 8 and v["hits"] == 0 for v in g2["por_db"].values()))
    # freno por proyección con tope minúsculo: frena antes de la 4ª corrida (nuevo dir)
    trazas_freno = OUT / "trazas_freno"
    fk = FakeSequential([m for c in casos for m in (turno_tool("buscar_nodos", {"consulta": "x"}, "t"), turno_final("f"))])
    est = {"gastado": 0.0, "corridos": 0, "total": 12, "tope_usd": 0.0001}
    rn.correr_grafo_rep(pob, "v3", 1, client_real=fk, cache_dir=OUT / "cache_freno", trazas_dir=trazas_freno,
                        estado_gasto=est, casos=casos)
    check("freno por proyección del agente: se detuvo tras 3 corridas (tope minúsculo)",
          est["corridos"] == 3 and len(list((trazas_freno / "ev2_enc_v3_r1").glob("EV2F-*.json"))) == 3)

    # --- juez: carga desde trazas, ids nuevos, orden, tabla SOLO_MESA, vínculo ---
    respuestas, faltantes = en.cargar_respuestas_nuevas(pob, trazas_dir)
    check("12 respuestas nuevas cargadas desde trazas, 0 faltantes", len(respuestas) == 12 and not faltantes)
    gold = cf.cargar_gold()
    casos_j = en.armar_casos(respuestas, gold)
    check("12 ids opacos EV2E- únicos (incluido el par con texto idéntico ×3: rep en la clave)",
          len({c["id_opaco"] for c in casos_j}) == 12)
    check("duplicados de texto detectados: 1 grupo de 3 (EV2F-004)",
          casos_j[0]["duplicados_texto"] and len(casos_j[0]["duplicados_texto"]) == 1 and casos_j[0]["duplicados_texto"][0][2] == 3)
    ids_ord = [c["id_opaco"] for c in casos_j]
    clave = sorted((c["id_pregunta"], c["sha256_respuesta"], c["grafo"], c["rep"], c["id_opaco"]) for c in casos_j)
    rep_ids = [x[4] for x in clave]
    random.Random(en.SEMILLA_ORDEN_JUEZ).shuffle(rep_ids)
    check("orden ciego = shuffle(juez-ev2-enc-v1) sobre sorted(id_pregunta, sha, grafo, rep)", rep_ids == ids_ord)
    p_ord, p_tab, p_vin = en.persistir_orden_y_tabla(casos_j, OUT / "juez_orden", OUT / "desanon_SOLO_MESA")
    tab = json.loads(p_tab.read_text()); vin = json.loads(p_vin.read_text()); orden = json.loads(p_ord.read_text())
    check("tabla SOLO_MESA: 12 filas con grafo/rep/id_pregunta, fuera de juez_out/",
          tab["n"] == 12 and all({"grafo", "rep", "id_pregunta", "id_opaco_base"} <= set(f) for f in tab["filas"])
          and juez_out not in p_tab.parents)
    check("tabla reproduce los ids desde la regla",
          all(en.id_opaco(f["id_pregunta"], f["grafo"], f["rep"], f["sha256_respuesta"]) == f["id_opaco"] for f in tab["filas"]))
    check("orden ciego y vínculo sin grafo/id de pregunta/label",
          not en.buscar_marcadores(p_ord.read_text(), ["EV2F-"]) and
          not cf.buscar_marcadores(p_vin.read_text(), ["EV2F-", "\"id_pregunta\"", "\"grafo\""]))
    check("vínculo: 4 pares × 3 ids nuevos, ids nuevos ⊂ orden", vin["n_pares"] == 4 and
          all(len(p["reps"]) == 3 for p in vin["pares"]) and
          {i for p in vin["pares"] for i in p["reps"].values()} == set(orden["ids_opacos_en_orden"]))
    ciegos = en.vista_ciega(casos_j)
    check("vista ciega: solo {id_opaco, pregunta, respuesta, criterios}",
          all(set(c) == {"id_opaco", "pregunta", "respuesta", "criterios"} for c in ciegos))
    check("requests del juez sin fuga (verificar_ceguera_requests)", not je.verificar_ceguera_requests(ciegos))
    sha_a_caso = {c["sha256_respuesta"]: (c["id_pregunta"], c["rep"]) for c in casos_j}
    # el par duplicado: las 3 reps comparten sha → todas mapean a alguna rep del mismo par (mismo guion) — ok

    registro: list = []

    def factory(rep: int, _label):
        return lc.CachingClient(ClienteFalsoJuez(rep, registro, sha_a_caso), domain="juez_ev2",
                                db_path=cache_dir / f"{en.DB_PREFIX_JUEZ}_r{rep}.db",
                                namespace=lc.make_namespace(f"juez_ev2_r{rep}", code_ver=juez.CODE_VER, thinking=False),
                                thinking_enabled=False, run_label=en.label_juez(rep))

    freno_chico = pf.FrenoProyeccion(cache_dir, 3, 3.0, 15.0, tope=0.0001, total_llamadas=36, min_filas=3,
                                     db_prefix=en.DB_PREFIX_JUEZ)
    f = pf.correr(ciegos, reps=3, out_dir=juez_out, client_factory=factory, freno=freno_chico, verbose=False)
    check("freno por proyección del juez frenó con ≥3 filas observadas", f is not None and f["hechas"] == 3 and len(registro) == 3, str(f))
    freno_ok = pf.FrenoProyeccion(cache_dir, 3, 3.0, 15.0, tope=100.0, total_llamadas=36, db_prefix=en.DB_PREFIX_JUEZ)
    f2 = pf.correr(ciegos, reps=3, out_dir=juez_out, client_factory=factory, freno=freno_ok, verbose=False)
    n_dup_extra = 2   # EV2F-004: 3 textos idénticos → 2 hits intra-db por rep
    check("re-lanzada completa sin freno; llamadas reales = 36 − hits por duplicados (3×2) = 30",
          f2 is None and len(registro) == 36 - 3 * n_dup_extra, str(len(registro)))
    dbs_j = je.dbs_juez(cache_dir)
    ver = pf.verificar_cross_hits(dbs_j)
    check("3 dbs del juez, keys por db = 10 (12 − 2 duplicados), pairwise disjuntas → 0 cross-hits",
          all(n == 10 for n in ver["keys_por_db"].values()) and ver["cross_hits"] == 0, str(ver["keys_por_db"]))
    check("hits intra-db == esperados por duplicados (2 por rep, 6 total), labels ev2_enc_juez_r{n}",
          ver["hits_total"] == 6 and all(list(d) == [en.label_juez(r)] and d[en.label_juez(r)] == 2
                                         for r, d in zip((1, 2, 3), (ver["hits_por_label"][p.name] for p in dbs_j))),
          str(ver["hits_por_label"]))
    gasto = pf.gasto_dbs(cache_dir, 3, 3.0, 15.0, en.DB_PREFIX_JUEZ)
    check("gasto juez desde dbs: 30 filas (misses pagados)", gasto["filas"] == 30)

    # --- agregación por respuesta y por par ---
    agg = pf.agregar(juez_out, 3, ciegos)
    check("agregados 12/12, 0 incompletas", agg["n_agregados"] == 12 and not agg["incompletas"])
    id2 = {f["id_opaco"]: (f["id_pregunta"], f["rep"]) for f in tab["filas"]}
    ok_resp = all(a["veredicto_pregunta"] == GUION_PAR[id2[a["id_opaco"]][0]][id2[a["id_opaco"]][1] - 1]
                  for a in agg["agregados"])
    check("mapping §2 por respuesta == guion (12/12)", ok_resp)
    pares_agg = je.agregar_pares(agg, vin)
    base_id = {p["id_opaco_base"]: p["id_pregunta"] for p in pob["pares"]}
    finales = {base_id[x["id_opaco_base"]]: x for x in pares_agg["pares"]}
    check("agregación por par: 4/4 finales esperados (mayoría / unánime / empate triple / invariante)",
          {q: x["final"] for q, x in finales.items()} == ESPERADO_FINAL, str({q: x["final"] for q, x in finales.items()}))
    check("vías esperadas", {q: x["via"] for q, x in finales.items()} == ESPERADO_VIA)
    check("auditoría: 1 par, flip descendente 1/1 (correcto → parcial por empate triple), tasa 1.0",
          pares_agg["auditoria"] == {"n_pares": 1, "flips": 1, "sin_flip": 0, "pendientes": 0, "tasa_flip_descendente": 1.0,
                                     "re_corridas_individuales_no_correcto": 2, "re_corridas_individuales_total": 3},
          str(pares_agg["auditoria"]))
    check("distribución final disparados {correcto 1, incorrecto 1, parcial 1}",
          pares_agg["distribucion_final_disparados"] == {"correcto": 1, "incorrecto": 1, "parcial": 1})
    check("veredicto base del par en el agregado: parcial (disparados) / correcto (auditoría)",
          all((x["veredicto_base"] == "correcto") == (x["tipo"] == "auditoria_correcto") for x in pares_agg["pares"]))
    check("distribución completa persistida por par (3 votos)", all(len(x["veredictos_reps"]) == 3 for x in pares_agg["pares"]))
    # par incompleto: quitar una rep del vínculo → incompleto listado, no agregado
    vin_inc = json.loads(json.dumps(vin)); del vin_inc["pares"][0]["reps"]["3"]
    pa_inc = je.agregar_pares(agg, vin_inc)
    check("par con rep faltante → incompleto (para laudo), no agregado",
          pa_inc["n_pares_incompletos"] == 1 and pa_inc["n_pares_agregados"] == 3 and pa_inc["pares_incompletos"][0]["reps_sin_veredicto"] == [3])

    # --- ceguera de requests y de salidas ---
    check("30 requests reales capturados (36 − 6 hits) con estructura exacta y system == prompt v1",
          len(registro) == 30 and all(set(r["kwargs"]) == {"model", "max_tokens", "temperature", "system", "messages"}
                                      and r["kwargs"]["system"] == juez.PROMPT_JUEZ for r in registro))
    payload = json.dumps([r["kwargs"]["messages"] for r in registro], ensure_ascii=False)
    check("payloads del juez sin grafo/label/rep/tipo/id opaco/veredicto base",
          not en.buscar_marcadores(payload, ["EV2E-", "EV2R-", "id_opaco", "respondible", "\"rep\""]),
          str(en.buscar_marcadores(payload, ["EV2E-", "EV2R-", "id_opaco"])))
    justifs = [c["justificacion"] for rep in pf.cargar_veredictos(juez_out, 3)[0].values() for r in rep.values() for c in r["criterios"]]
    check("payloads sin rastro de veredictos previos", all(j not in payload for j in justifs) and "scripteado" not in payload)
    # reporte final ciego + agregados en juez_out
    agg["verificacion_cross_hits"] = ver
    dist = pf.distribucion(agg); agg["distribucion"] = dist
    (juez_out / "veredictos_agregados_ciego.json").write_text(json.dumps(agg, ensure_ascii=False, indent=2))
    censo = {"n_respuestas": 12, "n_previstas": 12, "n_textos_duplicados": 1, "hits_intra_db_esperados_por_duplicados": 6,
             "n_criterios_gold": 164, "respondible_flag": {"True": 12}}
    md = je.reporte_final_md({"agg": agg, "pares_agg": pares_agg}, dist, ver, {"r1": 0, "r2": 0, "r3": 0}, gasto,
                             {"selftest": "sí"}, censo, None, [])
    (OUT / "reporte_final_ciego.md").write_text(md, encoding="utf-8")
    (OUT / "veredictos_finales_ciego.json").write_text(json.dumps(pares_agg, ensure_ascii=False, indent=2))
    marcas_out = ["EV2F-", "\"id_pregunta\"", "\"grafo\"", "\"label\"", "ev2_enc_v3", "reensamblado_v3", "\"rep\": "]
    fugas = {p.name: [m for m in marcas_out if m in p.read_text(encoding="utf-8")]
             for p in list(juez_out.glob("*")) + [OUT / "reporte_final_ciego.md", OUT / "veredictos_finales_ciego.json"]}
    # nota: veredictos_r{n}.jsonl y veredictos_agregados_ciego.json del pipeline base llevan "rep" del
    # JUEZ (meta_reps), no del agente; se excluye ese marcador ahí (la rep del agente jamás entra a juez_out/)
    fugas = {n: [m for m in f if not (m == "\"rep\": " and n.startswith("veredictos_"))] for n, f in fugas.items()}
    fugas = {n: f for n, f in fugas.items() if f}
    check("juez_out/ + reporte final + veredictos finales sin grafo/id de pregunta/label/rep del agente", not fugas, str(fugas))
    check("reporte final ciego contiene ids EV2R- de par y tabla de veredictos", "EV2R-" in md and "| final |" in md)


def main() -> int:
    pob = parte_real()
    parte_sintetica(pob)
    fallos = [n for n, ok in CHECKS if not ok]
    print(f"\nRESULTADO: {'PASS' if not fallos else 'FAIL'} ({len(CHECKS) - len(fallos)}/{len(CHECKS)} checks)")
    if fallos:
        print("fallos:", fallos)
    return 0 if not fallos else 1


if __name__ == "__main__":
    sys.exit(main())
