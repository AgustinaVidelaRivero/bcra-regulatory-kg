"""U-ESTUDIO-MATRIZ, paso 2 — efecto de cada ampliación de la matriz congelada
(solo lectura, sin API, sin Neo4j).

Candidatos: pares (origen, predicado, destino) con n >= 10 en
reports/u_audit_tipos_v3/p4_resumen.json, más variantes agrupadas por
predicado. Cada variante amplía EN MEMORIA DOMAIN_RANGE_CONGELADO (dominio o
rango del predicado); se asserta que la ampliación valida exactamente los
pares buscados y ningún otro.

Por variante:
  A. E1 primera pasada (población de los 982): relaciones que pasan a válidas
     y unidades con alguna, en 10 TOs y en los 5 de desarrollo; se asserta
     que coinciden con los conteos de p4.
  B. Población final (lo que ensambla r1: validación final por unidad, crudo
     verificado en el paso 1): relaciones que pasan a válidas y unidades.
  C. KG-Tanda0-Desarrollo-r1 re-ensamblado en memoria (uestmat_cadena):
     aristas nuevas, nodos nuevos, nodos hoy aislados que dejan de estarlo.
  D. Fragmentos a re-verificar en E3 = unidades de A ∪ B; costo con la tarifa
     de E3 de la tanda 0.
Controles: la cadena en memoria sin envoltorio y con el envoltorio sobre la
matriz congelada SIN ampliar reproducen el sha sellado del grafo.
Salida: uestmat_paso2_variantes.json (la tabla del reporte sale de acá).
"""
from __future__ import annotations

import collections
import json
from pathlib import Path

import uestmat_comun as U
import uestmat_cadena as K

OUT = Path("/tmp/u_estudio_matriz")
TIPOS = tuple(U.pc.ENTITY_TYPES_CONGELADO) + ("Sujeto",)


def par_str(s, p, t):
    return f"{s} --{p}--> {t}"


def ampliacion_de_par(s, p, t):
    dom, ran = U.pc.DOMAIN_RANGE_CONGELADO[p]
    if s in dom:
        return {p: (set(), {t})}
    if t in ran:
        return {p: ({s}, set())}
    return {p: ({s}, {t})}


def pares_nuevos(dr) -> set:
    out = set()
    for p in U.pc.PREDICATES_CONGELADO:
        for s in TIPOS:
            for t in TIPOS:
                d, r = dr[p]
                if (s in d and t in r) and not U.pc.firma_valida(s, p, t):
                    out.add((s, p, t))
    return out


def fusionar(ampl: list[dict]) -> dict:
    out: dict = {}
    for a in ampl:
        for p, (d, r) in a.items():
            od, orr = out.setdefault(p, (set(), set()))
            od.update(d)
            orr.update(r)
    return out


def tarifas() -> dict:
    est = json.loads((U.SALIDA / "estado_corpus.json").read_text(encoding="utf-8"))["fases_cerradas"]
    g = sum(est[f"{to}:e3"]["gasto_usd"] for to in U.TOS_10)
    n = sum(est[f"{to}:e3"]["resumen"]["n"] for to in U.TOS_10)
    gv = nv = 0
    for to in U.TOS_10:
        r = json.loads((U.SALIDA / to / "resumen_e3.json").read_text(encoding="utf-8"))["cliente_e3"]
        gv += r["gasto_usd_real"]
        nv += r["llamadas"]
    return {"fase_e3_gasto_usd": round(g, 6), "fase_e3_unidades": n,
            "tarifa_fase_e3_usd_por_unidad": g / n,
            "verificacion_gasto_usd": round(gv, 4), "verificacion_llamadas": nv,
            "tarifa_verificacion_usd_por_llamada": gv / nv,
            "fuentes": ["corpus_tanda0/salida_dirigida/estado_corpus.json (fases_cerradas <to>:e3)",
                        "corpus_tanda0/salida_dirigida/<to>/resumen_e3.json (cliente_e3)"]}


def main() -> None:
    p4 = json.loads((U.AUDIT / "p4_resumen.json").read_text(encoding="utf-8"))
    p4_filas = json.loads((U.AUDIT / "p4_filas.json").read_text(encoding="utf-8"))
    cand = [(x["origen"], x["predicado"], x["destino"], x["n"]) for x in p4["por_par"] if x["n"] >= 10]
    cand.sort(key=lambda x: (-x[3], x[0], x[1], x[2]))
    variantes = []
    for i, (s, p, t, n) in enumerate(cand, 1):
        variantes.append({"id": f"P{i:02d}", "tipo": "par", "pares": [(s, p, t)],
                          "ampliacion": ampliacion_de_par(s, p, t)})
    por_pred = collections.OrderedDict()
    for s, p, t, n in cand:
        por_pred.setdefault(p, []).append((s, p, t))
    for p, pares in por_pred.items():
        variantes.append({"id": f"G-{p}", "tipo": "agrupada_por_predicado", "pares": pares,
                          "ampliacion": fusionar([ampliacion_de_par(*x) for x in pares])})
    ej = [("Condicion", "condicion_de", "Operacion"), ("Condicion", "condicion_de", "Potestad")]
    variantes.append({"id": "G-condicion_de-ejemplo", "tipo": "agrupada_ejemplo_del_mandato", "pares": ej,
                      "ampliacion": fusionar([ampliacion_de_par(*x) for x in ej])})

    perfil = U.perfil_v3()
    chunks = {to: {c["id"]: c for c in U.cargar_chunks(to)} for to in U.TOS_10}
    e1 = {to: U.leer_jsonl(U.SALIDA / to / "extracciones_e1.jsonl") for to in U.TOS_10}
    crudos_fin = K.cargar_crudos()
    fin_val = {}
    for to in U.TOS_10:
        for d in U.leer_jsonl(U.SALIDA / to / f"extracciones_finales_{to}.jsonl"):
            fin_val[d["chunk_id"]] = d.get("validacion")
    comp_lw = {}
    for to in U.TOS_10:
        for d in U.leer_jsonl(U.SALIDA / to / "extracciones_e1_compact.jsonl"):
            comp_lw[d["chunk_id"]] = d
    pob = json.loads((OUT / "uestmat_poblacion_final.json").read_text(encoding="utf-8"))
    val_final = {}
    for v in pob.values():
        cid = v["chunk_id"]
        val_final[cid] = (comp_lw[cid]["validacion"] if v["fuente_crudo"] == "e1_compact_last_wins"
                          else fin_val[cid])

    kg0 = json.loads(U.KG_DEV.read_text(encoding="utf-8"))
    assert U.sha256_path(U.KG_DEV) == U.KG_DEV_SHA
    grado0 = collections.Counter()
    for e in kg0["edges"]:
        grado0[e["source"]] += 1
        grado0[e["target"]] += 1
    tipo0 = {n["id"]: n["type"] for n in kg0["nodes"]}
    aislados0 = {nid for nid in tipo0 if grado0[nid] == 0}
    aristas0 = {(e["source"], e["relation"], e["target"]) for e in kg0["edges"]}

    tar = tarifas()
    ctrl_orig = K.correr()
    assert ctrl_orig["sha256"] == U.KG_DEV_SHA
    ctrl_cong = K.correr(U.esquema_ampliado({})[0], crudos_fin)
    assert ctrl_cong["sha256"] == U.KG_DEV_SHA and not ctrl_cong["envoltorio"].relaciones_nuevas
    assert ctrl_cong["envoltorio"].unidades_revalidadas > 0

    resultados = []
    for v in variantes:
        esq, dr = U.esquema_ampliado(v["ampliacion"])
        nuevos = pares_nuevos(dr)
        assert nuevos == set(v["pares"]), (v["id"], nuevos)
        claves = {par_str(*x) for x in v["pares"]}
        esperado_p4 = {"10": sum(1 for f in p4_filas if par_str(f["origen"], f["predicado"], f["destino"]) in claves)}
        esperado_p4["dev"] = sum(1 for f in p4_filas if f["to"] in U.TOS_DEV and
                                 par_str(f["origen"], f["predicado"], f["destino"]) in claves)

        # A. E1 primera pasada
        a_rel = collections.Counter()
        a_uni = {"10": set(), "dev": set()}
        for to in U.TOS_10:
            for d in e1[to]:
                crudo = d.get("tool_input_crudo")
                if crudo is None:
                    continue
                amp = U.validador_e1.validar_salida(crudo, chunks[to][d["chunk_id"]], esquema=esq).as_dict()
                k = len(amp["relaciones"]) - len(d["validacion"]["relaciones"])
                assert k >= 0
                if k:
                    a_rel["10"] += k
                    a_uni["10"].add(d["chunk_id"])
                    if to in U.TOS_DEV:
                        a_rel["dev"] += k
                        a_uni["dev"].add(d["chunk_id"])
        assert a_rel["10"] == esperado_p4["10"] and a_rel["dev"] == esperado_p4["dev"], (v["id"], a_rel, esperado_p4)

        # B. población final
        b_rel = collections.Counter()
        b_uni = {"10": set(), "dev": set()}
        for cid, crudo in crudos_fin.items():
            to = cid.split("::")[0]
            base = val_final[cid]
            if base is None:
                continue
            amp = U.validador_e1.validar_salida(crudo, chunks[to][cid], esquema=esq).as_dict()
            k = len(amp["relaciones"]) - len(base["relaciones"])
            assert k >= 0
            if k:
                b_rel["10"] += k
                b_uni["10"].add(cid)
                if to in U.TOS_DEV:
                    b_rel["dev"] += k
                    b_uni["dev"].add(cid)

        # C. grafo de desarrollo re-ensamblado en memoria
        r = K.correr(esq, crudos_fin)
        kg1 = r["kg"]
        env = r["envoltorio"]
        assert len(env.relaciones_nuevas) == b_rel["dev"], (v["id"], len(env.relaciones_nuevas), b_rel["dev"])
        aristas1 = {(e["source"], e["relation"], e["target"]) for e in kg1["edges"]}
        nodos1 = {n["id"]: n["type"] for n in kg1["nodes"]}
        grado1 = collections.Counter()
        for e in kg1["edges"]:
            grado1[e["source"]] += 1
            grado1[e["target"]] += 1
        nuevas = aristas1 - aristas0
        perdidas = aristas0 - aristas1
        des_aislados = sorted(n for n in aislados0 if grado1[n] > 0)
        nodos_nuevos = sorted(set(nodos1) - set(tipo0))
        nodos_perdidos = sorted(set(tipo0) - set(nodos1))

        # D. fragmentos a re-verificar en E3
        u10 = a_uni["10"] | b_uni["10"]
        udev = a_uni["dev"] | b_uni["dev"]
        resultados.append({
            "id": v["id"], "tipo": v["tipo"], "pares": [par_str(*x) for x in v["pares"]],
            "ampliacion_en_memoria": {p: {"dominio_mas": sorted(d), "rango_mas": sorted(rr)}
                                      for p, (d, rr) in v["ampliacion"].items()},
            "pares_que_valida_la_ampliacion": sorted(par_str(*x) for x in nuevos),
            "A_e1_primera_pasada": {"relaciones_validas_nuevas_10tos": a_rel["10"],
                                    "relaciones_validas_nuevas_dev": a_rel["dev"],
                                    "unidades_10tos": len(a_uni["10"]), "unidades_dev": len(a_uni["dev"]),
                                    "coincide_con_p4": True},
            "B_poblacion_final": {"relaciones_validas_nuevas_10tos": b_rel["10"],
                                  "relaciones_validas_nuevas_dev": b_rel["dev"],
                                  "unidades_10tos": len(b_uni["10"]), "unidades_dev": len(b_uni["dev"])},
            "C_grafo_dev_r1": {"sha256_variante": r["sha256"],
                               "aristas_nuevas": len(nuevas),
                               "aristas_nuevas_por_relacion": dict(collections.Counter(x[1] for x in nuevas)),
                               "aristas_perdidas": len(perdidas),
                               "nodos_nuevos": nodos_nuevos, "nodos_perdidos": nodos_perdidos,
                               "aislados_hoy": len(aislados0),
                               "aislados_que_dejan_de_estarlo": len(des_aislados),
                               "aislados_que_dejan_de_estarlo_por_tipo": dict(collections.Counter(tipo0[n] for n in des_aislados)),
                               "ids_aislados_que_dejan_de_estarlo": des_aislados},
            "D_reverificacion_e3": {
                "fragmentos_10tos": len(u10), "fragmentos_dev": len(udev),
                "costo_usd_10tos_tarifa_fase": round(len(u10) * tar["tarifa_fase_e3_usd_por_unidad"], 4),
                "costo_usd_dev_tarifa_fase": round(len(udev) * tar["tarifa_fase_e3_usd_por_unidad"], 4),
                "costo_usd_10tos_tarifa_verificacion": round(len(u10) * tar["tarifa_verificacion_usd_por_llamada"], 4),
                "costo_usd_dev_tarifa_verificacion": round(len(udev) * tar["tarifa_verificacion_usd_por_llamada"], 4),
                "chunk_ids_10tos": sorted(u10)},
        })
        print(v["id"], a_rel["10"], a_rel["dev"], b_rel["10"], b_rel["dev"], len(nuevas), len(des_aislados), len(u10), len(udev), flush=True)

    salida = {
        "unidad": "U-ESTUDIO-MATRIZ",
        "grafo": {"path": str(U.KG_DEV.relative_to(U.REPO)), "sha256": U.KG_DEV_SHA,
                  "nodos": len(tipo0), "aristas": len(aristas0),
                  "aislados_hoy": len(aislados0),
                  "aislados_hoy_por_tipo": dict(collections.Counter(tipo0[n] for n in aislados0))},
        "control_reensamblado_sin_envoltorio_sha256": ctrl_orig["sha256"],
        "control_reensamblado_envoltorio_congelado_sha256": ctrl_cong["sha256"],
        "control_unidades_revalidadas_dev": ctrl_cong["envoltorio"].unidades_revalidadas,
        "tarifas_e3_tanda0": tar,
        "candidatos_umbral": ">= 10 rechazos en p4_resumen.json",
        "candidatos": [{"par": par_str(s, p, t), "n_p4": n} for s, p, t, n in cand],
        "supuesto": ("las relaciones que pasan a válidas entran al grafo sin nueva verificación E3: "
                     "cota superior del efecto antes de re-verificar"),
        "variantes": resultados,
    }
    (OUT / "uestmat_paso2_variantes.json").write_text(json.dumps(salida, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
