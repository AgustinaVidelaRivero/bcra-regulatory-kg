#!/usr/bin/env python3
"""U-MED-EJEMPLO-2, Paso 4 (análisis, sin API) — Lectura de las tres trazas del agente.

Por corrida: secuencia de llamadas (herramienta y argumentos textuales, en el orden del loop del
harness: steps_full 1:1 con trace.steps); en cada buscar_nodos, rango (1-based) de los nodos de
5.1.1.1 y de 3.7 en `resultados`; en cada ver_vecinos, posición (1-based) en `salientes` y
`entrantes`; qué nodos abrió con ver_nodo y cómo llegó a cada uno (primera aparición del id en un
output previo: resultado de búsqueda, o vecino de qué nodo y por qué arista); respuesta final,
citas, tokens y costo.
Conjuntos de nodos: los del Paso 2 (umed2_analista_paso2_resultado.json); los nodos concentradores
(TextoOrdenado y Sujeto, con procedencia primaria cla::1.1) se marcan aparte.
Escribe únicamente en /tmp/u_med_ejemplo/.
"""
import json
from pathlib import Path

OUT = Path("/tmp/u_med_ejemplo")
PFX = "umed2_analista_"
p2 = json.loads((OUT / f"{PFX}paso2_resultado.json").read_text(encoding="utf-8"))
S511 = set(p2["nodos_por_punto"]["cla::5.1.1.1"])
S37 = set(p2["nodos_por_punto"]["cla::3.7"])
PRIM = {n["id"] for n in p2["nodos"] if n["primaria_chunk_id"] in ("cla::5.1.1.1", "cla::3.7")}
ETQ = {n["id"]: n["label"] for n in p2["nodos"]}


def punto(i):
    ps = [k for k, s in (("5.1.1.1", S511), ("3.7", S37)) if i in s]
    return "/".join(ps) + ("" if i in PRIM else " [concentrador]")


def analizar(c):
    d = json.loads((OUT / f"{PFX}paso4_traza_c{c}.json").read_text(encoding="utf-8"))
    tr = d["trace"]
    steps = d["steps_full"]
    assert [s["n"] for s in steps] == [s["n"] for s in tr["steps"]]
    assert [s["tool"] for s in steps] == [s["tool"] for s in tr["steps"]]
    primera_aparicion = {}
    llamadas = []
    for s in steps:
        o = s["output"]
        fila = {"n": s["n"], "tool": s["tool"], "input": s["input"], "objetivo_en_output": []}
        if s["tool"] == "buscar_nodos":
            fila["total_con_match"] = o.get("total_con_match", o.get("total"))
            for r, x in enumerate(o.get("resultados", []), 1):
                if x["id"] in S511 | S37:
                    fila["objetivo_en_output"].append({"id": x["id"], "punto": punto(x["id"]), "rango": r})
                primera_aparicion.setdefault(x["id"], {"via": "busqueda", "paso": s["n"], "rango": r,
                                                       "consulta": s["input"].get("consulta")})
        elif s["tool"] == "ver_vecinos":
            fila["n_salientes_total"] = o.get("n_salientes_total")
            fila["n_entrantes_total"] = o.get("n_entrantes_total")
            fila["nodo_consultado_punto"] = punto(o["id"]) if o.get("id") in S511 | S37 else None
            for lado in ("salientes", "entrantes"):
                for r, x in enumerate(o.get(lado, []) or [], 1):
                    if x["vecino_id"] in S511 | S37:
                        fila["objetivo_en_output"].append({"id": x["vecino_id"], "punto": punto(x["vecino_id"]),
                                                           "lista": lado, "posicion": r, "relation": x["relation"]})
                    primera_aparicion.setdefault(x["vecino_id"], {"via": "vecino", "paso": s["n"], "de": o.get("id"),
                                                                  "relation": x["relation"], "lista": lado,
                                                                  "posicion": r})
        elif s["tool"] == "ver_nodo":
            i = s["input"].get("id")
            fila["nodo_punto"] = punto(i) if i in S511 | S37 else None
            fila["error"] = o.get("error")
        llamadas.append(fila)
    abiertos = []
    for s in steps:
        if s["tool"] == "ver_nodo":
            i = s["input"].get("id")
            if i in S511 | S37:
                previo = primera_aparicion.get(i)
                # solo cuenta si la aparición es ANTERIOR a este ver_nodo
                if previo and previo["paso"] >= s["n"]:
                    previo = None
                abiertos.append({"paso": s["n"], "id": i, "punto": punto(i), "llego_por": previo})
    fj = tr.get("final_json") or {}
    return {
        "corrida": c, "tool_calls": tr["tool_calls_used"], "hit_tool_limit": tr["hit_tool_limit"],
        "parse_ok": tr["parse_ok"], "error": tr["error"], "api_calls": len(tr["api_calls"]),
        "llamadas": llamadas,
        "abrio_nodo_5_1_1_1": any("5.1.1.1" in a["punto"] and "concentrador" not in a["punto"] for a in abiertos),
        "abrio_nodo_3_7": any("3.7" in a["punto"] and "concentrador" not in a["punto"] for a in abiertos),
        "nodos_objetivo_abiertos": abiertos,
        "respuesta": fj.get("respuesta"), "citas": fj.get("citas"), "respondible": fj.get("respondible"),
        "final_raw": tr.get("final_raw"),
        "citas_no_vistas_normalizadas": tr.get("citations_unseen_normalized"),
        "seen_provenances": tr.get("seen_provenances"),
        "tokens": {"in": tr["tokens_in"], "out": tr["tokens_out"], "cache_read": tr["cache_read"],
                   "cache_write": tr["cache_write"]},
        "costo_usd": tr["cost_usd"], "latencia_s": tr["latency_s"],
        "model_segun_api": d["meta"]["model_segun_api"], "cache_stats": d["meta"]["cache_stats"],
    }


def main():
    res = [analizar(c) for c in (1, 2, 3)]
    (OUT / f"{PFX}paso4_analisis.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    for r in res:
        print(f"\n######## CORRIDA {r['corrida']} — tools {r['tool_calls']} · api_calls {r['api_calls']} · "
              f"tope {r['hit_tool_limit']} · parse_ok {r['parse_ok']} · error {r['error']} · modelo {r['model_segun_api']}")
        for f in r["llamadas"]:
            extra = ""
            if f["tool"] == "buscar_nodos":
                extra = f" total={f['total_con_match']}"
            elif f["tool"] == "ver_vecinos":
                extra = f" sal={f['n_salientes_total']} ent={f['n_entrantes_total']} consultado={f['nodo_consultado_punto']}"
            elif f["tool"] == "ver_nodo":
                extra = f" punto={f['nodo_punto']}" + (f" ERROR={f['error']}" if f.get("error") else "")
            print(f"  {f['n']:>2}. {f['tool']} {json.dumps(f['input'], ensure_ascii=False)}{extra}")
            for x in f["objetivo_en_output"]:
                print(f"        -> {x['punto']} {x['id'][:70]} " +
                      (f"rango {x['rango']}" if "rango" in x else f"{x['lista']} pos {x['posicion']} ({x['relation']})"))
        print("  abrio 5.1.1.1:", r["abrio_nodo_5_1_1_1"], "| abrio 3.7:", r["abrio_nodo_3_7"])
        for a in r["nodos_objetivo_abiertos"]:
            print("   abierto paso", a["paso"], a["punto"], a["id"][:70], "| llegó por", json.dumps(a["llego_por"], ensure_ascii=False))
        print("  respondible:", r["respondible"])
        print("  RESPUESTA:", r["respuesta"])
        print("  CITAS:", json.dumps(r["citas"], ensure_ascii=False))
        print("  citas no vistas (normalizado):", json.dumps(r["citas_no_vistas_normalizadas"], ensure_ascii=False))
        print("  tokens:", r["tokens"], "| costo USD", r["costo_usd"], "| latencia s", r["latencia_s"])


if __name__ == "__main__":
    main()
