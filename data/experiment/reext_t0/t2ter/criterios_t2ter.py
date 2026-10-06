"""Criterios de aceptación de T2-ter de U-REEXT-T0, sobre COPIAS (USD 0, sin red): la salida, las bases y el log de
usage de antes y de después de la corrida (adaptado de t2bis/criterios_t2bis.py).

Uso: python -B criterios_t2ter.py --antes DIR --despues DIR --inicio ISO_LOCAL --tope 1.0 --out OUT
  (DIR con salida_r2b/, bases/{e1_extraccion,e3_verificacion,e1_reintentos}.db y cache_usage.jsonl)
"""
import argparse
import hashlib
import json
import sqlite3
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("--antes", type=Path, required=True)
ap.add_argument("--despues", type=Path, required=True)
ap.add_argument("--inicio", required=True)
ap.add_argument("--tope", type=float, required=True)
ap.add_argument("--out", type=Path, required=True)
a = ap.parse_args()
A, D = a.antes / "salida_r2b", a.despues / "salida_r2b"
TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
REPARAR = ("cap::4.2.1.2::parte1", "cap::3.1.1.2")
PRECIOS = {"claude-haiku-4-5": (1.00, 5.00, 1.25, 0.10), "claude-sonnet-5": (2.00, 10.00, 2.50, 0.20)}
res, fallas = {}, []


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def last_wins(p: Path) -> dict:
    out = {}
    if p.exists():
        for x in p.read_text(encoding="utf-8").splitlines():
            if x.strip():
                r = json.loads(x)
                out[r["chunk_id"]] = r
    return out


def criterio(nombre: str, ok: bool, evidencia) -> None:
    res[nombre] = {"ok": bool(ok), "evidencia": evidencia}
    if not ok:
        fallas.append(nombre)


# C1. cap: las unidades y partes con E1 válida conservan su último registro y su expediente; los otros nueve TOs, igual
e1a, e1d = (A / "cap/extracciones_e1.jsonl").read_bytes(), (D / "cap/extracciones_e1.jsonl").read_bytes()
fa, fd = (A / "cap/finales.jsonl").read_bytes(), (D / "cap/finales.jsonl").read_bytes()
ra, rd = last_wins(A / "cap/extracciones_e1.jsonl"), last_wins(D / "cap/extracciones_e1.jsonl")
la, ld = last_wins(A / "cap/finales.jsonl"), last_wins(D / "cap/finales.jsonl")
validas = sorted(c for c, r in ra.items() if r.get("error") is None)
cambian_e1 = [c for c in validas if json.dumps(ra[c], sort_keys=True) != json.dumps(rd.get(c), sort_keys=True)]
cambian_fin = [c for c in la if json.dumps(la[c], sort_keys=True) != json.dumps(ld.get(c), sort_keys=True)]
otros = {}
for to in TOS:
    xa = {p.relative_to(A / to).as_posix(): sha(p) for p in (A / to).rglob("*") if p.is_file()}
    xd = {p.relative_to(D / to).as_posix(): sha(p) for p in (D / to).rglob("*") if p.is_file()}
    otros[to] = {"cambian": sorted(k for k in xa if xd.get(k) not in (None, xa[k])), "nuevos": sorted(set(xd) - set(xa)),
                 "borrados": sorted(set(xa) - set(xd))}
criterio("C1 las unidades y partes de cap con E1 válida conservan su último registro y su expediente; en los otros "
         "nueve TOs no cambia ningún archivo",
         e1d.startswith(e1a) and fd.startswith(fa) and not cambian_e1 and not cambian_fin
         and all(not (v["cambian"] or v["nuevos"] or v["borrados"]) for t, v in otros.items() if t != "cap"),
         {"con_e1_valida_antes": len(validas), "expedientes_antes": len(la),
          "extracciones_e1_lineas": [e1a.count(b"\n"), e1d.count(b"\n")], "finales_lineas": [fa.count(b"\n"), fd.count(b"\n")],
          "registros_e1_que_cambian": cambian_e1, "expedientes_que_cambian": cambian_fin,
          "registros_e1_reescritos": sorted(c for c in rd if json.dumps(ra.get(c), sort_keys=True) != json.dumps(rd[c], sort_keys=True)),
          "expedientes_nuevos": sorted(set(ld) - set(la)), "archivos_por_to": otros})

# C2. las dos reparadas: E1 sin error, marcadas, con expediente; sin validación quedan 0
r1 = json.loads((D / "cap/resumen_e1.json").read_text(encoding="utf-8"))
r3 = json.loads((D / "cap/resumen_e3.json").read_text(encoding="utf-8"))
reparadas = {c: {"error_e1": rd[c].get("error"), "reparacion_forma": rd[c].get("reparacion_forma"),
                 "claves_del_crudo": sorted(rd[c].get("tool_input_crudo") or {}),
                 "relaciones_en_el_crudo": len((rd[c].get("tool_input_crudo") or {}).get("relations") or []),
                 "estado_e3": (ld.get(c) or {}).get("estado"), "reintentos_ratchet": (ld.get(c) or {}).get("n_reintentos")}
             for c in REPARAR}
fr2 = last_wins(D / "cap/extracciones_finales_r2_cap.jsonl")
sin_val = []
for to in TOS:
    for c, r in last_wins(D / to / f"extracciones_finales_r2_{to}.jsonl").items():
        if r.get("validacion") is None and not r.get("cola_humana"):
            sin_val.append({"chunk_id": c, "error": r.get("error"), "estado_e3": r.get("estado_e3")})
criterio("C2 las dos unidades reparadas: E1 sin error, marcadas, con expediente de E3 o cola humana; sin validación 0",
         all(v["error_e1"] is None and v["reparacion_forma"] and v["estado_e3"] for v in reparadas.values()) and not sin_val,
         {"reparadas": reparadas, "sin_validacion_fuera_de_la_cola": sin_val,
          "resumen_e1": {k: r1.get(k) for k in ("n_unidades", "reintentos_forma", "reparadas_forma", "errores_definitivos",
                                                "particionadas_por_corte")},
          "resumen_e3_estados": r3.get("estados")})

# C3. E2 r2 de cap con los nodos de las reparadas; el E2 del perfil de E1 sigue declarando la unidad partida
ga = json.loads((A / "cap/grafo_r2_cap.json").read_text(encoding="utf-8"))
gd = json.loads((D / "cap/grafo_r2_cap.json").read_text(encoding="utf-8"))
ids_a = {n["id"] for n in ga["nodes"]}
por_unidad = {}
for n in gd["nodes"]:
    for p in [n.get("provenance")] + (n.get("provenances") or []):
        if p and p.get("chunk_id") in REPARAR:
            por_unidad.setdefault(p["chunk_id"], set()).add(n["id"])
nuevos = [n for n in gd["nodes"] if n["id"] not in ids_a]
rep = json.loads((D / "cap/reporte_e2_cap.json").read_text(encoding="utf-8"))
criterio("C3 el E2 r2 de cap incorpora los nodos de las reparadas; el E2 del perfil de E1 sigue declarando "
         "cap::4.2.1.2 reemplazada por sus partes",
         all(por_unidad.get(c) for c in REPARAR if (reparadas[c]["estado_e3"] or "").startswith(("completo", "aceptado")))
         and "cap::4.2.1.2" in (rep.get("particionadas_por_corte") or {}),
         {"nodos_antes_despues": [len(ga["nodes"]), len(gd["nodes"])], "aristas_antes_despues": [len(ga["edges"]), len(gd["edges"])],
          "nodos_nuevos": len(nuevos), "nodos_con_procedencia_en_las_reparadas": {c: len(v) for c, v in por_unidad.items()},
          "e2_perfil_e1": {"nodos": rep["nodes_total"], "aristas": rep["edges_total"],
                           "fan_in": {k: rep["fanin"][k] for k in ("esperados", "aceptados", "rechazados", "ausentes")},
                           "particionadas_por_corte": rep.get("particionadas_por_corte")}})

# C4. filas nuevas = líneas de usage nuevas, con modelo y temperatura; gasto nuevo dentro del tope
filas, por_base = [], {}
for base in ("e1_extraccion", "e3_verificacion", "e1_reintentos"):
    pa = sqlite3.connect(f"file:{a.antes / 'bases' / (base + '.db')}?mode=ro", uri=True)
    claves_a = {k for (k,) in pa.execute("select key from cache")}
    pd = sqlite3.connect(f"file:{a.despues / 'bases' / (base + '.db')}?mode=ro", uri=True)
    n = 0
    for k, ns, ca, rq, rw in pd.execute("select key, namespace, created_at, request_json, raw_json from cache"):
        if k in claves_a:
            continue
        n += 1
        rq, rw = json.loads(rq), json.loads(rw)
        u = rw.get("usage") or {}
        p_in, p_out, p_cw, p_cr = PRECIOS[rq["model"]]
        usd = (u.get("input_tokens", 0) * p_in + u.get("output_tokens", 0) * p_out
               + (u.get("cache_creation_input_tokens") or 0) * p_cw + (u.get("cache_read_input_tokens") or 0) * p_cr) / 1e6
        filas.append({"base": base, "namespace": ns, "created_at": ca, "modelo_pedido": rq["model"],
                      "modelo_respuesta": rw.get("model"), "temperatura": rq.get("temperature", "sin fijar (la del proveedor)"),
                      "max_tokens": rq.get("max_tokens"), "stop_reason": rw.get("stop_reason"),
                      "output_tokens": u.get("output_tokens"), "usd": round(usd, 6), "posterior_al_inicio": ca >= a.inicio})
    por_base[base] = n
ua, ud = (a.antes / "cache_usage.jsonl").read_bytes(), (a.despues / "cache_usage.jsonl").read_bytes()
nuevas = [json.loads(x) for x in ud[len(ua):].decode("utf-8").splitlines() if x.strip()]
gasto_filas = round(sum(f["usd"] for f in filas), 6)
ea = json.loads((A / "estado_corpus.json").read_text(encoding="utf-8"))
ed = json.loads((D / "estado_corpus.json").read_text(encoding="utf-8"))
pa_ = json.loads((A / "presupuesto_compartido.json").read_text(encoding="utf-8"))
pd_ = json.loads((D / "presupuesto_compartido.json").read_text(encoding="utf-8"))
nuevo = round(pd_["gasto_usd"] - pa_["gasto_usd"], 6)
suma_fases = round(sum(f["gasto_usd"] for f in ed["fases_cerradas"].values()), 6)
g = {k: (ea["fases_cerradas"][k]["gasto_usd"], ed["fases_cerradas"][k]["gasto_usd"]) for k in ("cap:e1", "cap:e3")}
criterio("C4 filas nuevas en las bases = líneas nuevas de usage; el gasto nuevo no pasa el tope; estado y presupuesto "
         "suman lo mismo",
         ud.startswith(ua) and len(filas) == len(nuevas) and all(f["posterior_al_inicio"] for f in filas)
         and abs(nuevo - gasto_filas) < 1e-5 and nuevo <= a.tope and ed["fase_actual"] is None
         and abs(suma_fases - pd_["gasto_usd"]) < 1e-5,
         {"filas_nuevas_por_base": por_base, "filas_nuevas": len(filas), "lineas_de_usage_nuevas": len(nuevas),
          "usage_por_componente": {c: sum(1 for x in nuevas if x["component"] == c) for c in sorted({x["component"] for x in nuevas})},
          "gasto_nuevo_presupuesto": nuevo, "gasto_nuevo_filas": gasto_filas, "tope": a.tope,
          "cap_e1_antes_despues": g["cap:e1"], "cap_e3_antes_despues": g["cap:e3"],
          "presupuesto_antes_despues": [pa_["gasto_usd"], pd_["gasto_usd"]], "suma_fases_cerradas": suma_fases,
          "reaperturas": [{"key": x["key"], "ts": x["ts"], "gasto_previo_usd": x["fase_cerrada"]["gasto_usd"]}
                          for x in ed.get("reaperturas", [])], "filas": filas})

out = {"inicio_corrida": a.inicio, "criterios": res, "fallas": fallas, "veredicto": "OK" if not fallas else "FALLA"}
a.out.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
for k, v in res.items():
    print(("OK   " if v["ok"] else "FALLA"), k)
print("VEREDICTO:", out["veredicto"])
