"""
t1_corrida_en_seco.py — U-REEXT-T0, T1, punto 3 (mandato firmado en e2027dd): corrida en seco de T2, sin llamar a la
API, sin construir ningún cliente y sin leer la clave. USD 0.

Con el manifiesto `tanda0_10tos_r2b.json` (después del punto 1) y el camino del runner (runner_corpus.configurar,
chunks_sin_ids_repetidos, PERFIL.build_request_kwargs, kwargs_reintento_forma y corresponde_escalon_3):
  a. el pedido de cada unidad (sha256 del pedido canónico y del mensaje; modelo, max_tokens y temperatura), su
     namespace y su clave de caché; las claves del reintento por corte (16.384), del tercer escalón (40.960) y del
     reintento por salida mal formada (namespace `-rforma1`, temperatura 1);
  b. las unidades por TO y el prefijo (system + tools + tool_choice) idéntico en todas;
  c. cuántas de esas claves ya están en las bases de la copia (la de E1 de la tanda 0 y la de los reintentos de E1),
     abiertas en solo lectura;
  d. los namespaces de los reintentos y de E3, con su base;
  e. el control contra P5: la clave de cada una de las 27 unidades de P4b contra la de
     data/experiment/prompt_r2/p5/salida/claves_despues.json, y contra la del brazo de P3c de P4b
     (p4b/salida/claves_despues_p3c.json);
  f. las unidades grandes, con el mecanismo que cubre a cada una;
  g. la estimación por TO contra el tope del manifiesto.

La estimación (g) es la de P5 (data/experiment/prompt_r2/p5/costo_p5.py y su salida costo_p5.json): los cuatro
escenarios de costo_p5.json (corrida a y b de P5; salida de P4 sin ponderar y ponderada por estrato), repartidos por
TO con lo que cada TO gastó y consumió en la corrida sellada de la tanda 0 (corpus_tanda0/salida, perfil v3_b54):
  - E1: lecturas del prefijo por unidad del TO en la e0 r2b; las 5 escrituras del prefijo, repartidas por igual
    entre los diez TOs (0,5 por TO); entrada y salida no cacheadas del crudo de E1 del TO (extracciones_e1.jsonl,
    último registro por unidad), por los cocientes del escenario;
  - E3: el gasto del verificador del TO, el agregado por el render de la salida (repartido por el gasto del
    verificador) y el de los reintentos de E1 del TO por el crecimiento de la salida;
  - los deltas de P3b-2 (1,33 en el total), repartidos por unidades;
  - el tercer escalón (las cotas de P3c-1), asignado a los TOs de sus unidades candidatas (cap y ric), por mitades;
  - ric sumó 5 unidades con C2 (89 contra 84 de la e0 sellada): su base se escala por 89/84;
  - la entrada y la salida del crudo de cada TO se escalan a los totales del censo de P1 (usage_crudo_total), que suma
    todos los registros (el último registro por unidad da un poco menos).
Con las unidades de la e0 sellada (2.434), la suma por TO reproduce el central de costo_p5.json
(`central_con_la_e0_sellada_usd`); con las 2.439 de la e0 r2b, el total cambia en las lecturas del prefijo de las 5
unidades nuevas y en la escala de ric.

Corre desde la raíz de una COPIA del repo; escribe solo en --salida (fuera del repo).
  PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B data/experiment/reext_t0/t1_corrida_en_seco.py --salida DIR
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
import statistics
import sys
from collections import Counter
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[2]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
for sub in ("e1_extractor", "e3_verificador", "e2_reduce", "corpus_v2", "e0_chunking"):
    sys.path.insert(0, str(REX / sub))
sys.path.insert(0, str(REX))
sys.path.insert(0, str(REPO / "data" / "experiment" / "evaluacion"))

import llm_cache as lc            # noqa: E402 — capa sellada, solo import
import comun_e1                   # noqa: E402
import cliente_e1                 # noqa: E402
import cliente_e3                 # noqa: E402
import prompt_e3                  # noqa: E402
import manifiesto_corpus as MC    # noqa: E402
import runner_corpus as RC        # noqa: E402 — solo funciones y constantes; no se llama main()

MANIFIESTO = REX / "manifiestos" / "tanda0_10tos_r2b.json"
PR2 = REPO / "data" / "experiment" / "prompt_r2"
CLAVES_P5 = PR2 / "p5" / "salida" / "claves_despues.json"
CLAVES_P4B_P3C = PR2 / "p4b" / "salida" / "claves_despues_p3c.json"
COSTO_P5 = PR2 / "p5" / "salida" / "costo_p5.json"
CENSO_P1 = PR2 / "p1" / "salida" / "censo_p1.json"
COSTO_P3B2 = PR2 / "p3b2" / "salida" / "costo_p3b2.json"
COSTO_P4 = PR2 / "p4" / "salida" / "costo_real_p4.json"
COSTO_P3C2 = PR2 / "p3c2" / "salida" / "costo_p3c2.json"
SALIDA_T0 = REX / "corpus_tanda0" / "salida"
E0_SELLADA = REX / "e0_chunking" / "salida_tanda0"
DB_E1 = cliente_e1.DB_PATH
DB_E3 = cliente_e3.DB_PATH
PREC = {"in": 1.00, "out": 5.00, "cw": 1.25, "cr": 0.10}
PREFIJO_TOKENS = 27840          # medido en P3c-2 (freno_p3c2.md); el mismo de costo_p5.py
GRANDES = ("cap::4.2.1.2", "ric::11.2::intro", "cap::3.1.14.1", "cap::4.3.3.1")
# Salida por carácter de texto propio que usa el mandato (P4, prefijo de P3b-2): mediana 1,175 y máximo 1,498 en 6
# unidades de 3.109 a 9.825 caracteres; con ellas, el reintento de 16.384 cubre 13.944 y 10.937 caracteres.
RAZON_MEDIANA, RAZON_MAX = 1.175, 1.498


def sha(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def claves_en_db(db: Path, claves: set[str]) -> tuple[int, dict]:
    if not db.exists():
        return 0, {"existe": False}
    con = sqlite3.connect(f"file:{db}?mode=ro&immutable=1", uri=True)
    try:
        hits = sum(1 for k in claves if con.execute("SELECT 1 FROM cache WHERE key = ?", (k,)).fetchone())
        por_ns = dict(con.execute("SELECT namespace, count(*) FROM cache GROUP BY namespace").fetchall())
    finally:
        con.close()
    return hits, por_ns


def jl_last(p: Path) -> dict:
    out = {}
    for x in p.read_text(encoding="utf-8").splitlines():
        if x.strip():
            r = json.loads(x)
            out[r["chunk_id"]] = r
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()
    sal = a.salida.resolve()
    if sal.is_relative_to(REPO.resolve()):
        raise SystemExit("--salida no puede estar dentro de la copia")
    sal.mkdir(parents=True, exist_ok=True)

    man = MC.cargar(MANIFIESTO)
    RC.configurar(man)
    RC.PERFIL_R2 = RC.perfil_forma_r2(RC.PERFIL)          # lo que hace main() con este manifiesto
    pf = RC.PERFIL
    ns = cliente_e1.namespace_e1(prefijo_hash=pf.prefijo_hash_para_namespace)
    nsf = cliente_e1.namespace_e1(prefijo_hash=pf.prefijo_hash_para_namespace, sufijo=cliente_e1.SUFIJO_REINTENTO_FORMA)
    techo = cliente_e1.MAX_TOKENS_REINTENTO_CORTE_R2 if RC.PERFIL_R2 else cliente_e1.MAX_TOKENS_REINTENTO_CORTE

    filas, prefijos, por_to = [], set(), {}
    for to in man.orden_corrida:
        chunks = RC.chunks_sin_ids_repetidos(comun_e1.cargar_chunks((to,), e0_dir=RC.E0_DIR), to)
        por_to[to] = {"unidades": len(chunks), "chars_propio": sum(c["chars_propio"] for c in chunks)}
        for c in chunks:
            kw = pf.build_request_kwargs(c, model=RC.MODEL_E1)
            kw2 = pf.build_request_kwargs(json.loads(json.dumps(c)), model=RC.MODEL_E1)
            can = lc.canonical_request(kw)
            prefijos.add(json.dumps({k: kw[k] for k in ("system", "tools", "tool_choice")}, sort_keys=True,
                                    ensure_ascii=False))
            kf = RC.kwargs_reintento_forma(kw, pf)
            filas.append({
                "chunk_id": c["id"], "to": to, "tipo": c["tipo"], "chars_propio": c["chars_propio"],
                "sha256_request": sha(can), "sha256_mensaje": sha(kw["messages"][0]["content"]),
                "request_determinista": can == lc.canonical_request(kw2),
                "model": kw["model"], "max_tokens": kw["max_tokens"], "temperature": kw.get("temperature"),
                "namespace": ns, "clave": lc.compute_key(ns, can),
                "clave_reintento_corte": lc.compute_key(ns, lc.canonical_request(dict(kw, max_tokens=techo))),
                "clave_escalon_3": lc.compute_key(ns, lc.canonical_request(
                    dict(kw, max_tokens=cliente_e1.MAX_TOKENS_ESCALON_3_R2))),
                "namespace_reintento_forma": nsf, "temperatura_reintento_forma": kf.get("temperature"),
                "clave_reintento_forma": lc.compute_key(nsf, lc.canonical_request(kf))})
    with open(sal / "requests_t1.jsonl", "w", encoding="utf-8") as f:
        for r in filas:
            f.write(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n")

    claves = {r["clave"] for r in filas}
    todas = claves | {r[k] for r in filas for k in ("clave_reintento_corte", "clave_escalon_3", "clave_reintento_forma")}
    hits_e1, ns_e1 = claves_en_db(DB_E1, todas)
    hits_r, ns_r = claves_en_db(RC.DB_REINTENTOS_E1, todas)
    _, ns_e3 = claves_en_db(DB_E3, set())
    ns3 = cliente_e3.namespace_e3()

    # e. control contra P5
    p5 = json.loads(CLAVES_P5.read_text(encoding="utf-8"))
    p4b = {x["chunk_id"]: x["clave"] for x in json.loads(CLAVES_P4B_P3C.read_text(encoding="utf-8"))}
    por_id = {r["chunk_id"]: r for r in filas}
    ctrl = []
    for u in p5["unidades"]:
        r = por_id.get(u["chunk_id"])
        ctrl.append({"chunk_id": u["chunk_id"], "grupo": u["grupo"], "clave_t1": r and r["clave"],
                     "clave_p5": u["clave"], "igual_a_p5": bool(r) and r["clave"] == u["clave"],
                     "igual_a_p4b_p3c": bool(r) and r["clave"] == p4b.get(u["chunk_id"])})
    rf = p5["reintento_forma"]
    ctrl_forma = {"chunk_id": rf["chunk_id"], "clave_p5": rf["clave"],
                  "clave_t1": por_id[rf["chunk_id"]]["clave_reintento_forma"],
                  "igual": por_id[rf["chunk_id"]]["clave_reintento_forma"] == rf["clave"]
                  and nsf == rf["namespace"]}

    # f. unidades grandes
    import correr_e0  # noqa: PLC0415
    chunks_por_id = {c["id"]: c for to in man.orden_corrida for c in comun_e1.cargar_chunks((to,), e0_dir=RC.E0_DIR)}
    cap_med, cap_max = 16384 / RAZON_MEDIANA, 16384 / RAZON_MAX
    grandes = []
    for cid in GRANDES:
        c = chunks_por_id[cid]
        partes, info = correr_e0.particionar_por_corte(c)
        d = {"chunk_id": cid, "chars_propio": c["chars_propio"],
             "salida_proyectada_mediana": round(c["chars_propio"] * RAZON_MEDIANA),
             "salida_proyectada_max": round(c["chars_propio"] * RAZON_MAX),
             "primer_intento": 8192, "reintento_por_corte": techo,
             "se_parte": partes is not None, "particion": info,
             "tercer_escalon_si_el_reintento_corta": RC.corresponde_escalon_3(c)}
        if partes:
            d["partes"] = [{"id": p["id"], "chars_propio": p["chars_propio"],
                            "pasa_13944": p["chars_propio"] > cap_med, "pasa_10937": p["chars_propio"] > cap_max,
                            "tercer_escalon_si_corta": RC.corresponde_escalon_3(p)} for p in partes]
        d["mecanismo"] = (
            "primer intento 8.192 → reintento por corte 16.384 → si corta, se parte por ítems y cada parte va con "
            "8.192 → 16.384 → tercer escalón 40.960 (una parte no se vuelve a partir)" if partes else
            "primer intento 8.192 → reintento por corte 16.384 → si corta, tercer escalón 40.960 (no se puede partir: "
            + info.get("motivo", "") + ")")
        grandes.append(d)
    sobre = [{"chunk_id": r["chunk_id"], "chars_propio": r["chars_propio"]} for r in filas
             if r["chars_propio"] > cap_max]
    sobre.sort(key=lambda x: -x["chars_propio"])

    # g. estimación por TO
    cp5 = json.loads(COSTO_P5.read_text(encoding="utf-8"))
    censo = json.loads(CENSO_P1.read_text(encoding="utf-8"))
    p3b2 = json.loads(COSTO_P3B2.read_text(encoding="utf-8"))
    p4 = json.loads(COSTO_P4.read_text(encoding="utf-8"))
    c3c2 = json.loads(COSTO_P3C2.read_text(encoding="utf-8"))
    deltas = p3b2["u_reext_t0"]["componentes_usd"]
    p3b_resto = sum(v for k, v in deltas.items() if k not in ("e1_prefijo_lecturas", "e1_prefijo_escrituras"))
    render_p1 = censo["costos"]["B_central"]["e3_extra_por_render_usd"]
    crec_p1 = censo["escenarios_salida"]["B_central"]["crecimiento_salida"]
    esc3 = {k: v for k, v in c3c2["u_reext_t0"]["tercer_escalon_usd"].items() if k.startswith("nuevo")}
    esc3_min = min(v["sin_ratchet"] for v in esc3.values())
    esc3_max = max(v["sin_ratchet"] for v in esc3.values())
    base = {}
    n_sellada = {}
    for to in man.orden_corrida:
        e1 = jl_last(SALIDA_T0 / to / "extracciones_e1.jsonl")
        r3 = json.loads((SALIDA_T0 / to / "resumen_e3.json").read_text(encoding="utf-8"))
        n_sellada[to] = len(json.loads((E0_SELLADA / f"chunks_{to}.json").read_text(encoding="utf-8")))
        base[to] = {"in": sum((r.get("usage") or {}).get("input_tokens", 0) for r in e1.values()),
                    "out": sum((r.get("usage") or {}).get("output_tokens", 0) for r in e1.values()),
                    "e3v": r3["cliente_e3"]["gasto_usd_real"], "e1r": r3["cliente_e1_reintentos"]["gasto_usd_real"]}
    tot_in = sum(b["in"] for b in base.values())
    tot_out = sum(b["out"] for b in base.values())
    u = censo["usage_crudo_total"]
    tot_e3v = sum(b["e3v"] for b in base.values())
    # el censo de P1 suma el crudo de todos los registros; el último registro por unidad da un poco menos: cada TO se
    # escala a los totales del censo, para que con las unidades de la e0 sellada se reproduzca costo_p5.json
    f_in, f_out = u["input_tokens"] / tot_in, u["output_tokens"] / tot_out
    escenarios = {}
    g_in = p4["medido"]["entrada_nuevo_sobre_sellado"]

    def estimar(gin: float, gout: float, unidades: dict) -> tuple[dict, float]:
        filas_to, tot = {}, 0.0
        n_tot = sum(unidades.values())
        for to in man.orden_corrida:
            n = unidades[to]
            esc = n / n_sellada[to]                           # 89/84 en ric con la e0 r2b; 1 en los demás
            b = base[to]
            e1 = (n * PREFIJO_TOKENS * PREC["cr"] + 0.5 * PREFIJO_TOKENS * (PREC["cw"] - PREC["cr"])) / 1e6 \
                + esc * (b["in"] * f_in * PREC["in"] * gin + b["out"] * f_out * PREC["out"] * gout) / 1e6
            e3 = esc * (b["e3v"] + render_p1 * max(0.0, gout - 1) / crec_p1 * b["e3v"] / tot_e3v + b["e1r"] * gout)
            resto = p3b_resto * n / n_tot
            e3esc = esc3_max / 2 if to in ("cap", "ric") else 0.0
            filas_to[to] = {"unidades": n, "e1_usd": round(e1, 4), "e3_usd": round(e3, 4),
                            "deltas_p3b2_usd": round(resto, 4), "central_usd": round(e1 + e3 + resto, 4),
                            "con_tercer_escalon_max_usd": round(e1 + e3 + resto + e3esc, 4),
                            "estimado_manifiesto_usd": round(man.limites["estimado_usd"][to]["e1"]
                                                             + man.limites["estimado_usd"][to]["e3"], 4)}
            tot += e1 + e3 + resto
        return filas_to, tot

    for nombre_c, q in cp5["medido"].items():
        for nombre, v in p4["u_reext_t0"].items():
            gout = v["crecimiento_salida"] * q["salida_sobre_anterior"]
            gin = g_in * q["entrada_sobre_anterior"]
            _, tot_sellada = estimar(gin, gout, n_sellada)
            filas_to, tot = estimar(gin, gout, {to: por_to[to]["unidades"] for to in man.orden_corrida})
            escenarios[f"corrida_{nombre_c}_p4_{nombre}"] = {
                "por_to": filas_to, "central_usd": round(tot, 2),
                "central_con_la_e0_sellada_usd": round(tot_sellada, 2),
                "con_tercer_escalon_usd": [round(tot + esc3_min, 2), round(tot + esc3_max, 2)],
                "por_1_4_usd": round((tot + esc3_max) * 1.4, 2),
                "central_costo_p5_usd": cp5["u_reext_t0"][f"corrida_{nombre_c}_p4_{nombre}"]["central_usd"],
                "bajo_el_tope": round((tot + esc3_max) * 1.4, 2) <= man.limites["tope_global_usd"]}
    peor = max(e["por_1_4_usd"] for e in escenarios.values())

    res = {
        "comando": "data/experiment/reext_t0/t1_corrida_en_seco.py --salida DIR (desde la raíz de una copia)",
        "manifiesto": {"nombre": man.nombre, "e0": str(RC.E0_DIR.relative_to(REPO)), "perfil": pf.nombre,
                       "tope_global_usd": RC.TOPE_GLOBAL_USD, "estimado_total_manifiesto_usd": RC.ESTIMADO_TOTAL_USD,
                       "orden": list(man.orden_corrida)},
        "llamadas_a_la_api": 0,
        "unidades": {"total": len(filas), "por_to": por_to, "unidades_e0_sellada": n_sellada,
                     "ids_repetidos": sum(v - 1 for v in Counter(r["chunk_id"] for r in filas).values())},
        "pedido": {"prefijos_distintos": len(prefijos), "modelos": dict(Counter(r["model"] for r in filas)),
                   "max_tokens": dict(Counter(r["max_tokens"] for r in filas)),
                   "temperaturas": dict(Counter(str(r["temperature"]) for r in filas)),
                   "deterministas": sum(r["request_determinista"] for r in filas),
                   "claves_distintas": len(claves)},
        "namespaces": {
            "e1": {"namespace": ns, "db": str(DB_E1.relative_to(REPO)), "max_tokens": 8192, "temperatura": 0},
            "e1_reintento_por_corte": {"namespace": ns, "db": str(DB_E1.relative_to(REPO)), "max_tokens": techo,
                                       "nota": "el mismo pedido con otro max_tokens: otra clave, el mismo namespace"},
            "e1_tercer_escalon": {"namespace": ns, "db": str(DB_E1.relative_to(REPO)),
                                  "max_tokens": cliente_e1.MAX_TOKENS_ESCALON_3_R2, "transmision": True},
            "e1_reintento_forma": {"namespace": nsf, "db": str(DB_E1.relative_to(REPO)), "temperatura": 1},
            "e3": {"namespace": ns3, "db": str(DB_E3.relative_to(REPO)), "temperatura": "sin fijar",
                   "nota": "su clave depende de la salida de E1: no se calcula en seco"},
            "e3_reintentos_e1_ratchet": {"namespace": ns, "db": str(RC.DB_REINTENTOS_E1.relative_to(REPO)),
                                         "nota": "build_reextraccion_kwargs con el perfil: el pedido de E1 con el "
                                                 "feedback de E3; su clave depende de E3"}},
        "claves_ya_en_las_bases": {"e1_extraccion_db": hits_e1, "e1_reintentos_db": hits_r,
                                   "claves_controladas": len(todas),
                                   "entradas_por_namespace": {"e1_extraccion_db": {k: v for k, v in ns_e1.items()
                                                                                    if "322c5a23e9b7" in k},
                                                              "e1_reintentos_db": {k: v for k, v in ns_r.items()
                                                                                   if "322c5a23e9b7" in k},
                                                              "e3_verificacion_db_namespace_e3": ns_e3.get(ns3, 0)}},
        "control_p5": {"unidades": len(ctrl), "iguales_a_p5": sum(x["igual_a_p5"] for x in ctrl),
                       "iguales_a_p4b_p3c": sum(x["igual_a_p4b_p3c"] for x in ctrl),
                       "namespace_igual": ns == p5["namespace"], "reintento_forma": ctrl_forma,
                       "difieren": [x for x in ctrl if not x["igual_a_p5"]], "detalle": ctrl},
        "unidades_grandes": grandes,
        "unidades_sobre_10937_caracteres": sobre,
        "estimacion": {"metodo": "costo_p5.py repartido por TO (ver docstring)",
                       "base_e1_tokens": {"entrada": tot_in, "salida": tot_out,
                                          "escala_al_censo": [round(f_in, 6), round(f_out, 6)],
                                          "censo_p1_entrada": u["input_tokens"], "censo_p1_salida": u["output_tokens"]},
                       "escenarios": escenarios, "peor_por_1_4_usd": peor,
                       "tope_usd": man.limites["tope_global_usd"],
                       "margen_sobre_el_peor_usd": round(man.limites["tope_global_usd"] - peor, 2)}}
    (sal / "corrida_en_seco_t1.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n",
                                                 encoding="utf-8")
    print(json.dumps({k: res[k] for k in ("unidades", "pedido", "claves_ya_en_las_bases")}, ensure_ascii=False)[:1500])
    print("control P5:", res["control_p5"]["iguales_a_p5"], "de", res["control_p5"]["unidades"],
          "| iguales a P4b P3c:", res["control_p5"]["iguales_a_p4b_p3c"], "| forma:", ctrl_forma["igual"])
    for k, e in escenarios.items():
        print(k, e["central_usd"], e["central_con_la_e0_sellada_usd"], e["central_costo_p5_usd"],
              e["con_tercer_escalon_usd"], e["por_1_4_usd"])
    print("peor ×1,4:", peor, "tope:", man.limites["tope_global_usd"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
