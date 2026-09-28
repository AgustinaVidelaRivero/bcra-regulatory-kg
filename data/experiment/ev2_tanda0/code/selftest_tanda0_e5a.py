"""
selftest_tanda0_e5a.py — SELFTEST EN SECO de los instrumentos 9 y 10 de la
tanda 0 (U-TANDA0-2A E5.a): comun_tanda0 (registro en memoria de la vista
runtime), juez_tanda0 (juez v1 N=3 por celda) y enc_tanda0 (§7 por celda),
más el registro de celdas celdas_tanda0 que los dos últimos usan. USD 0:
ningún cliente real se construye (candados que levantan si alguien lo intenta)
y ninguna llamada sale a la API; el agente y el juez usan clientes falsos, el
backend Neo4j un stub sin driver.

Bloques:
  A. comun_tanda0: entradas en comun_ev2.GRAFOS, despachador en comun_ev2 y
     runner_ev2, vistas de los dos grafos (conteos del registro, provenance en
     todos los nodos), delegación a r1 y v2, idempotencia, resolución por
     grafos.cargar_vista_runtime (opción B).
  B. celdas_tanda0: cuatro celdas con los labels del mandato, sha de cada
     kg.json, sales / prefijos / semillas únicos y distintos de r1, casos
     (C2-C4 = los 40 de EV2 en el orden de C1; C5 = 20 en el orden del archivo
     sellado), gold (EV2 40/164; C5 20/60) y marcadores.
  C. corrida del agente en memoria (C3, 2 casos, cliente falso): trazas con
     meta de la celda, anotación meta.tanda0, 0 hits en db nueva, replay por
     caché sin llamadas.
  D. corrida del agente en Neo4j (C4, 2 casos, stub + cliente falso):
     meta.backend y meta.model_segun_api.
  E. juez de la base (C3 sobre los 2 casos de C, juez falso): orden ciego
     determinístico, ids con prefijo propio, ceguera limpia y fugas provocadas
     detectadas, agregados por mapping §2, reporte escrito, retoma sin
     re-llamar; ids de C5 con su prefijo.
  F. §7 (C3): población derivada (1 parcial + auditoría de 1 correcto),
     persistencia verificada, agente N=3 con db por rep y 0 hits, anotación
     meta.tanda0_enc, juez §7, agregación por par (enc_r1.agregar_pares),
     retoma sin re-llamar; guarda del backend Neo4j sin índice.
  G. gating de las tres CLI: sin autorización salen con código 2 y no escriben.
  H. ninguna escritura fuera de selftest_out/ y ningún .pyc.

Uso:  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/ev2_tanda0/code/selftest_tanda0_e5a.py
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import celdas_tanda0 as ce0                 # noqa: E402
import juez_tanda0 as jt                    # noqa: E402
import enc_tanda0 as et                     # noqa: E402
import comun_tanda0 as ct                   # noqa: E402
import pipeline_fidelidad as pf             # noqa: E402
import runner_ev2 as rv                     # noqa: E402
import comun_ev2 as cev2                    # noqa: E402
import grafos as G                          # noqa: E402
from comun_r1 import juez                   # noqa: E402
from selftest_runner_ev2_neo4j import (     # noqa: E402  (fakes del gate 4, import sin efectos)
    FakeClient, StubNeo4jIndex, turno_tool, turno_final)
from anthropic.types import Message         # noqa: E402

OUT = ce0.TANDA0_DIR / "selftest_out" / "tanda0_e5a"
RUTAS_T = ce0.Rutas(OUT)
_checks: list[tuple[str, bool]] = []


def check(nombre: str, cond) -> bool:
    _checks.append((nombre, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {nombre}")
    return bool(cond)


# --------------------------------------------------------------------------- #
# Candados: ningún cliente real                                               #
# --------------------------------------------------------------------------- #
def _prohibido(*a, **k):
    raise AssertionError("el selftest intentó construir un cliente REAL (API)")


rv._real_client = _prohibido
juez.construir_cliente_real = _prohibido


class FakeJuez:
    """Juez falso: por pregunta (primera línea del contenido del usuario),
    devuelve veredictos por criterio según el guion {pregunta: [lista por llamada]}."""

    def __init__(self, guion: dict):
        self.guion = {k: list(v) for k, v in guion.items()}
        self.llamadas = 0
        self.messages = self

    def create(self, **kwargs):
        preg = kwargs["messages"][0]["content"].split("\n")[1]
        cola = self.guion[preg]
        if not cola:
            raise AssertionError(f"llamada de juez no prevista para {preg!r}")
        self.llamadas += 1
        vs = cola.pop(0)
        txt = json.dumps({"clasificacion_respuesta": "contenido",
                          "criterios": [{"indice": i + 1, "veredicto": v, "fragmento": None,
                                         "justificacion": ""} for i, v in enumerate(vs)]},
                         ensure_ascii=False)
        return Message.model_validate({
            "id": "msg_selftest_juez_t0", "type": "message", "role": "assistant",
            "model": "fake-juez-selftest", "content": [{"type": "text", "text": txt}],
            "stop_reason": "end_turn", "stop_sequence": None,
            "usage": {"input_tokens": 100, "output_tokens": 50}})


class Explota:
    def __init__(self):
        self.messages = self

    def create(self, **kwargs):
        raise AssertionError("re-lanzamiento llamó a un cliente (debió servirse de caché o saltearse)")


def _clave_pregunta(p: str) -> str:
    return p.strip().splitlines()[0]


# --------------------------------------------------------------------------- #
def bloque_a() -> None:
    print("\n== A. comun_tanda0 (instrumento 9) ==")
    for k, g in ct.TANDA0.items():
        check(f"comun_ev2.GRAFOS tiene {k} con sha del archivo",
              cev2.GRAFOS.get(k) is g and ce0.sha256_path(g["path"]) == g["sha256"])
    check("despachador instalado en comun_ev2 y runner_ev2",
          cev2.cargar_runtime is ct._cargar_runtime_ext and rv.cargar_runtime is ct._cargar_runtime_ext)
    for k, (n, e) in {"tanda0_ens_desarrollo": (6378, 15007), "tanda0_ens_diez": (8256, 18932)}.items():
        kg = rv.cargar_runtime(k)
        check(f"vista {k}: {n}/{e} y provenance en todos los nodos",
              len(kg.nodes) == n and len(kg.edges) == e and all(x.provenances for x in kg.nodes))
    kg = rv.cargar_runtime("r1")
    check("delega r1 (6529/17772)", (len(kg.nodes), len(kg.edges)) == (6529, 17772))
    kg = rv.cargar_runtime("v2")
    check("delega v2 (6178/11415)", (len(kg.nodes), len(kg.edges)) == (6178, 11415))
    ct.registrar_tanda0()
    kg = rv.cargar_runtime("r1")
    check("re-registro idempotente (sin doble envoltura, r1 sigue resolviendo)",
          cev2.cargar_runtime is ct._cargar_runtime_ext and len(kg.nodes) == 6529)
    kg = G.cargar_vista_runtime("KG_Tanda0_Desarrollo_r1")
    check("grafos.cargar_vista_runtime resuelve KG_Tanda0_Desarrollo_r1 (opción B)",
          (len(kg.nodes), len(kg.edges)) == (6378, 15007))


def bloque_b() -> None:
    print("\n== B. celdas_tanda0 ==")
    esperado = {"C2": ("neo4j", "KG_Reextraido_r1", "ev2_c2_r1_neo4j"),
                "C3": ("memoria", "tanda0_ens_desarrollo", "ev2_c3_dev_mem"),
                "C4": ("neo4j", "KG_Tanda0_Desarrollo_r1", "ev2_c4_dev_neo4j"),
                "C5": ("memoria", "tanda0_ens_diez", "ev2_c5_diez_mem")}
    check("cuatro celdas con backend, grafo y label del mandato",
          {k: (c.backend, c.grafo, c.label) for k, c in ce0.CELDAS.items()} == esperado)
    check("sha256 de cada kg.json igual al de la celda",
          all(ce0.sha256_path(ce0.kg_path(c)) == c.kg_sha256 for c in ce0.CELDAS.values()))
    todos = [x for c in ce0.CELDAS.values() for x in (c.sal_base, c.sal_enc, c.prefijo_base,
                                                     c.prefijo_enc, c.semilla_auditoria)]
    check("sales, prefijos y semillas únicos por celda", len(todos) == len(set(todos)))
    check("ninguno coincide con los de r1",
          not set(todos) & {ce0.cr.SAL_ID_BASE, ce0.cr.SAL_ID_ENC, ce0.cr.PREFIJO_BASE,
                            ce0.cr.PREFIJO_ENC, ce0.cr.SEMILLA_AUDITORIA})
    ids_c1 = [c["caso_id"] for c in ce0.cr.casos_fidelidad_r1()]
    for k in ("C2", "C3", "C4"):
        casos, fuente = ce0.casos_celda(ce0.CELDAS[k])
        check(f"{k}: 40 casos en el orden de C1 (semilla {fuente['semilla_orden']})",
              [c["caso_id"] for c in casos] == ids_c1 and len(casos) == 40)
    casos5, f5 = ce0.casos_celda(ce0.CELDAS["C5"])
    check("C5: 20 casos en el orden del archivo sellado (T0F-001 a T0F-020)",
          [c["caso_id"] for c in casos5] == [f"T0F-{i:03d}" for i in range(1, 21)]
          and f5["sha256"] == ce0.SHA_PREGUNTAS_C5)
    g_ev2 = ce0.cargar_gold_celda(ce0.CELDAS["C3"])
    vacios = [("T0F-008", 1), ("T0F-008", 3), ("T0F-013", 1)]
    check("C5: criterios sin cita textual = los 3 de las preguntas de abstención",
          ce0.criterios_cita_vacia() == vacios)
    check("C5: autorizados = exactamente los 3 criterios de abstención (decisión de la autora, 28/09)",
          ce0.CRITERIOS_CITA_VACIA_AUTORIZADOS == frozenset(vacios))
    try:
        ce0.cargar_gold_celda(ce0.CELDAS["C5"], autorizados=frozenset())
        guarda = False
    except ValueError as e:
        guarda = all(str(v) in str(e) for v in vacios)
    check("C5: con la lista vacía, el cargador rechaza y nombra los 3 criterios", guarda)
    try:
        ce0.cargar_gold_celda(ce0.CELDAS["C5"], autorizados=frozenset(vacios[:2]))
        guarda_parcial = False
    except ValueError as e:
        guarda_parcial = str(vacios[2]) in str(e) and str(vacios[0]) not in str(e)
    check("C5: autorizar solo 2 de 3 rechaza y nombra el que falta", guarda_parcial)
    g_c5 = ce0.cargar_gold_celda(ce0.CELDAS["C5"])
    kw = ce0.cr.juez.construir_kwargs(g_c5["T0F-008"]["pregunta"], "respuesta sintética",
                                      g_c5["T0F-008"]["criterios"])
    check("C5: el juez congelado recibe «Cita textual de la norma: «»» tal como está sellado (2 veces en T0F-008)",
          kw["messages"][0]["content"].count("Cita textual de la norma: «»") == 2)
    kw13 = ce0.cr.juez.construir_kwargs(g_c5["T0F-013"]["pregunta"], "respuesta sintética",
                                        g_c5["T0F-013"]["criterios"])
    check("C5: T0F-013 llega con 1 cita vacía y el resto del gold intacto",
          kw13["messages"][0]["content"].count("Cita textual de la norma: «»") == 1
          and g_c5["T0F-013"]["criterios"] == [{"criterio": c["criterio"], "cita_textual": c["cita_textual"]}
                                               for c in next(p for p in ce0.cargar_preguntas_c5()
                                                             if p["id"] == "T0F-013")["gold"]["criterios"]])
    check("gold EV2 40/164 y gold C5 20/60",
          (len(g_ev2), sum(len(v["criterios"]) for v in g_ev2.values())) == (40, 164)
          and (len(g_c5), sum(len(v["criterios"]) for v in g_c5.values())) == (20, 60))
    check("pregunta de cada caso de C5 == pregunta del gold",
          all(c["pregunta"] == g_c5[c["caso_id"]]["pregunta"] for c in casos5))
    m = ce0.marcadores_celda(ce0.CELDAS["C4"])
    check("marcadores de la celda incluyen label, grafo, sha y prefijos",
          {"ev2_c4_dev_neo4j", "KG_Tanda0_Desarrollo_r1", ce0.CELDAS["C4"].kg_sha256[:12],
           "T0C4B-", "T0C4E-", "T0F-"} <= set(m))


def _script_agente(casos, final_prefijo: str, con_tool: bool = True) -> list:
    s = []
    for i, c in enumerate(casos, 1):
        if con_tool and i == 1:
            s.append(turno_tool("buscar_nodos", {"consulta": "entidad financiera"}, uid=f"t{i}"))
        s.append(turno_final(f"{final_prefijo} {i}", uid=f"f{i}"))
    return s


def bloque_c() -> list[dict]:
    print("\n== C. agente en memoria (C3, cliente falso) ==")
    celda = ce0.CELDAS["C3"]
    casos, fuente = ce0.casos_celda(celda)
    sub = casos[:2]
    fake = FakeClient(_script_agente(sub, "respuesta sintética de la celda tres"))
    estado = {"gastado": 0.0, "corridos": 0, "total": 2, "tope_usd": 1.0}
    res = ce0.correr_agente(celda, label=celda.label, casos=sub, fuente=fuente, rutas=RUTAS_T,
                            client_real=fake, estado_gasto=estado)
    outdir = RUTAS_T.trazas / celda.label
    n_anot = ce0.anotar_trazas(celda, outdir, fuente, "tanda0", {"etapa": "base"})
    ts = [json.loads((outdir / f"{c['caso_id']}.json").read_text(encoding="utf-8")) for c in sub]
    check("2 trazas con meta de la celda (label, grafo, sha)",
          res["n_casos_corridos"] == 2 and all(
              t["meta"]["label"] == celda.label and t["meta"]["grafo"] == celda.grafo
              and t["meta"]["kg_sha256"] == celda.kg_sha256 for t in ts))
    check("anotación meta.tanda0 con el orden real (orden-ev2-r1)",
          n_anot == 2 and all(t["meta"]["tanda0"]["semilla_orden_real"] == "orden-ev2-r1"
                              for t in [json.loads((outdir / f"{c['caso_id']}.json").read_text(encoding="utf-8"))
                                        for c in sub]))
    check("anotación idempotente", ce0.anotar_trazas(celda, outdir, fuente, "tanda0", {}) == 0)
    check("0 hits en la db nueva", ce0.hits_db(RUTAS_T.cache / f"{celda.label}.db") == 0)
    replay = OUT / "replay_c3"
    res2 = rv.correr_grafo(celda.grafo, client_real=Explota(), db_path=RUTAS_T.cache / f"{celda.label}.db",
                           label=celda.label, casos=sub, outdir=replay,
                           estado_gasto={"gastado": 0.0, "corridos": 0, "total": 2, "tope_usd": 1.0})
    check("replay desde la caché sin llamar al cliente (misma respuesta)",
          res2["n_casos_corridos"] == 2 and json.loads((replay / f"{sub[0]['caso_id']}.json")
                                                       .read_text(encoding="utf-8"))["trace"]["final_json"]
          == ts[0]["trace"]["final_json"])
    return sub


def bloque_d() -> None:
    print("\n== D. agente en Neo4j (C4, stub + cliente falso) ==")
    celda = ce0.CELDAS["C4"]
    casos, fuente = ce0.casos_celda(celda)
    sub = casos[:2]
    fake = FakeClient(_script_agente(sub, "respuesta sintética de la celda cuatro"))
    estado = {"gastado": 0.0, "corridos": 0, "total": 2, "tope_usd": 1.0}
    stub = StubNeo4jIndex(grafo=celda.grafo, modo=ce0.MODO_NEO4J)
    res = ce0.correr_agente(celda, label=celda.label, casos=sub, fuente=fuente, rutas=RUTAS_T,
                            client_real=fake, estado_gasto=estado, indice=stub)
    t = json.loads((RUTAS_T.trazas / celda.label / f"{sub[0]['caso_id']}.json").read_text(encoding="utf-8"))
    check("2 trazas Neo4j con meta.backend de la celda y model_segun_api",
          res["n_casos_corridos"] == 2 and t["meta"]["backend"]["grafo"] == celda.grafo
          and t["meta"]["backend"]["modo"] == "fulltext" and t["meta"]["model_segun_api"]
          and t["meta"]["label"] == celda.label and t["meta"]["kg_sha256"] == celda.kg_sha256)
    check("el stub recibió la tool del guion", ("buscar_nodos", "entidad financiera") in stub.llamadas)


def bloque_e(sub: list[dict]) -> None:
    print("\n== E. juez de la base (C3, juez falso) ==")
    celda = ce0.CELDAS["C3"]
    gold = ce0.cargar_gold_celda(celda)
    ids = [c["caso_id"] for c in sub]
    resp, falt = ce0.cargar_respuestas(celda, RUTAS_T.trazas / celda.label, celda.label, ids)
    c1 = jt.armar_casos(celda, resp, gold)
    c2 = jt.armar_casos(celda, resp, gold)
    check("carga estricta de las 2 trazas", len(resp) == 2 and not falt)
    check("orden ciego determinístico e ids T0C3B- únicos",
          [c["id_opaco"] for c in c1] == [c["id_opaco"] for c in c2]
          and all(c["id_opaco"].startswith("T0C3B-") for c in c1) and len({c["id_opaco"] for c in c1}) == 2)
    ciegos = jt.vista_ciega(c1)
    check("ceguera limpia (0 fugas)", jt.verificar_ceguera(celda, ciegos) == [])
    for marca in ("ev2_c3_dev_mem", "tanda0_ens_desarrollo", "T0F-", celda.kg_sha256[:12]):
        sucio = [dict(ciegos[0], respuesta=ciegos[0]["respuesta"] + " " + marca)]
        check(f"fuga provocada detectada: {marca}", jt.verificar_ceguera(celda, sucio) != [])
    c5 = ce0.CELDAS["C5"]
    g5 = ce0.cargar_gold_celda(c5)
    x5 = jt.armar_casos(c5, [{"id_pregunta": "T0F-001", "respuesta": "respuesta sintética",
                              "respondible_flag": True, "pregunta_traza": g5["T0F-001"]["pregunta"]}], g5)
    check("C5: id opaco con prefijo T0C5B- y criterios del gold de C5",
          x5[0]["id_opaco"].startswith("T0C5B-") and x5[0]["criterios"] == g5["T0F-001"]["criterios"])
    # juzgar_base end-to-end sobre los 2 casos (casos_celda acotado en memoria)
    guion = {}
    for c in c1:
        k = len(c["criterios"])
        if c["id_pregunta"] == ids[0]:     # parcial: primer criterio no cumplido en las 3 reps
            guion[_clave_pregunta(c["pregunta"])] = [["no_cumplido"] + ["cumplido"] * (k - 1)] * 3
        else:                               # correcto
            guion[_clave_pregunta(c["pregunta"])] = [["cumplido"] * k] * 3
    fake = FakeJuez(guion)
    orig = ce0.casos_celda
    ce0.casos_celda = lambda cel: (orig(cel)[0][:2], orig(cel)[1])
    try:
        res = jt.juzgar_base(celda, RUTAS_T, client_factory=lambda rep, lab: fake, verbose=False)
        dist = res["distribucion"]["veredicto_pregunta"]
        check("juzgar_base: 6 llamadas, 0 incompletas, veredictos parcial 1 / correcto 1",
              fake.llamadas == 6 and not res["incompletas"]
              and dist.get("parcial") == 1 and dist.get("correcto") == 1)
        check("reporte ciego y agregados escritos",
              (RUTAS_T.sub(celda, "base") / f"reporte_ciego_{celda.label}.md").exists()
              and (RUTAS_T.sub(celda, "base") / "veredictos_agregados_ciego.json").exists())
        res2 = jt.juzgar_base(celda, RUTAS_T, client_factory=lambda rep, lab: Explota(), verbose=False)
        check("retoma del juez sin re-llamar (write-through por id opaco)", res2["frenado"] is None)
        try:
            jt._persistir_o_verificar(RUTAS_T.sub(celda, "orden") / jt.ARCHIVO_ORDEN, {"otro": 1})
            difiere = False
        except RuntimeError:
            difiere = True
        check("orden persistido: una derivación distinta levanta RuntimeError", difiere)
    finally:
        ce0.casos_celda = orig


def bloque_f(sub: list[dict]) -> None:
    print("\n== F. §7 (C3) ==")
    celda = ce0.CELDAS["C3"]
    orig = ce0.casos_celda
    ce0.casos_celda = lambda cel: (orig(cel)[0][:2], orig(cel)[1])
    try:
        pob = et.persistir_poblacion(celda, RUTAS_T)
        check("población: 1 parcial disparado + 1 auditoría (ceil(10 %) de 1 correcto)",
              pob["n_pares"] == 2 and sorted(p["tipo"] for p in pob["pares"])
              == ["auditoria_correcto", "parcial_disparado"])
        check("población re-derivada idéntica", et.persistir_poblacion(celda, RUTAS_T)["pares"] == pob["pares"])
        casos, fuente = et.casos_agente(celda, pob)
        check("casos del §7 en el orden de la base filtrado", [c["caso_id"] for c in casos]
              == [c["caso_id"] for c in sub])
        script = []
        for rep in range(1, 4):
            for i, c in enumerate(casos, 1):
                script.append(turno_final(f"re-corrida {rep} del caso {i}", uid=f"e{rep}{i}"))
        fake = FakeClient(script)
        res = et.etapa_agente(celda, RUTAS_T, client_real=fake, tope=5.0)
        check("agente §7: 2 casos × 3 reps, db por rep con 0 hits",
              res["indice"]["reps"] == {1: 2, 2: 2, 3: 2} and res["indice"]["hits"] == {1: 0, 2: 0, 3: 0}
              and not res["frenado"])
        t = json.loads((RUTAS_T.trazas / celda.label_enc(2) / f"{casos[0]['caso_id']}.json").read_text(encoding="utf-8"))
        check("traza §7 anotada con meta.tanda0_enc (rep y tipo)",
              t["meta"]["tanda0_enc"]["rep"] == 2 and t["meta"]["tanda0_enc"]["tipo"] in
              ("parcial_disparado", "auditoria_correcto") and t["meta"]["label"] == celda.label_enc(2))
        gold = ce0.cargar_gold_celda(celda)
        guion = {}
        for q in [c["caso_id"] for c in casos]:
            k = len(gold[q]["criterios"])
            guion[_clave_pregunta(gold[q]["pregunta"])] = [["cumplido"] * k] * 9   # 3 reps agente × 3 juez
        fj = FakeJuez(guion)
        rj = et.etapa_juez(celda, RUTAS_T, client_factory=lambda rep, lab: fj, verbose=False)
        pares = rj["pares"]
        check("juez §7: 18 llamadas, 2 pares agregados, sin incompletos",
              fj.llamadas == 18 and pares["n_pares_agregados"] == 2 and pares["n_pares_incompletos"] == 0)
        check("agregación por par: disparado → correcto; auditoría sin flip",
              pares["distribucion_final_disparados"] == {"correcto": 1}
              and pares["auditoria"]["sin_flip"] == 1)
        check("ids §7 con prefijo T0C3E- en la tabla SOLO_MESA",
              all(f["id_opaco"].startswith("T0C3E-") for f in json.loads(
                  (RUTAS_T.sub(celda, "desanonimizacion_SOLO_MESA") / "tabla_id_opaco_s7_SOLO_MESA.json")
                  .read_text(encoding="utf-8"))["filas"]))
        rj2 = et.etapa_juez(celda, RUTAS_T, client_factory=lambda rep, lab: Explota(), verbose=False)
        check("retoma del juez §7 sin re-llamar", rj2["frenado"] is None)
        try:
            ce0.correr_agente(ce0.CELDAS["C4"], label="x", casos=[], fuente={}, rutas=RUTAS_T,
                              client_real=None, estado_gasto={}, indice=None)
            guarda = False
        except ValueError:
            guarda = True
        check("guarda: backend Neo4j sin índice levanta ValueError", guarda)
    finally:
        ce0.casos_celda = orig


def bloque_g() -> None:
    print("\n== G. gating de las CLI (sin autorización → exit 2, sin escribir) ==")
    env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
    py = sys.executable
    for args in (["celdas_tanda0.py", "--celda", "C3"],
                 ["juez_tanda0.py", "--celda", "C2"],
                 ["enc_tanda0.py", "--celda", "C2", "--etapa", "agente"],
                 ["enc_tanda0.py", "--celda", "C2", "--etapa", "juez"]):
        r = subprocess.run([py, "-B", str(CODE_DIR / args[0]), *args[1:]], env=env,
                           capture_output=True, text=True)
        check(f"{' '.join(args)} → exit 2 y 'ABORTADO'", r.returncode == 2 and "ABORTADO" in r.stdout)


def main() -> int:
    print("== SELFTEST EN SECO — instrumentos 9 y 10 de la tanda 0 (sin API, USD 0) ==")
    check("PYTHONDONTWRITEBYTECODE activo", sys.dont_write_bytecode)
    antes = {d: (ce0.TANDA0_DIR / d).exists() for d in ("trazas", "juez_out", "cache")}
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    bloque_a()
    bloque_b()
    sub = bloque_c()
    bloque_d()
    bloque_e(sub)
    bloque_f(sub)
    bloque_g()
    print("\n== H. escrituras ==")
    despues = {d: (ce0.TANDA0_DIR / d).exists() for d in ("trazas", "juez_out", "cache")}
    check("ningún directorio real de trazas/juez_out/cache creado por el selftest", antes == despues)
    passed = sum(ok for _, ok in _checks)
    print(f"\n  {passed}/{len(_checks)} checks OK")
    print("  RESULTADO:", "PASS" if passed == len(_checks) else "FAIL")
    return 0 if passed == len(_checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
