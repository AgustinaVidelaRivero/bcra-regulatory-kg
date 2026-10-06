"""Criterios de aceptación de T2-bis de U-REEXT-T0, sobre COPIAS (USD 0, sin red): la salida, las bases y el log de
usage de antes y de después de la corrida. Cada criterio da su evidencia en el JSON de salida.

Uso (desde la raíz de una COPIA del repo, para importar correr_e0 de la E0 de HEAD):
  python -B criterios_t2bis.py --antes DIR --despues DIR --inicio ISO_LOCAL --out OUT
  (DIR con salida_r2b/, bases/{e1_extraccion,e3_verificacion,e1_reintentos}.db y cache_usage.jsonl)
"""
import argparse
import hashlib
import json
import sqlite3
import sys
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("--antes", type=Path, required=True)
ap.add_argument("--despues", type=Path, required=True)
ap.add_argument("--inicio", required=True)
ap.add_argument("--out", type=Path, required=True)
a = ap.parse_args()
A, D = a.antes / "salida_r2b", a.despues / "salida_r2b"
TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
UNIDAD = "cap::4.2.1.2"
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


# C1. cap: append-only y las 460 unidades con E1 válida conservan su último registro y su expediente
e1a, e1d = (A / "cap/extracciones_e1.jsonl").read_bytes(), (D / "cap/extracciones_e1.jsonl").read_bytes()
fa, fd = (A / "cap/finales.jsonl").read_bytes(), (D / "cap/finales.jsonl").read_bytes()
ra, rd = last_wins(A / "cap/extracciones_e1.jsonl"), last_wins(D / "cap/extracciones_e1.jsonl")
la, ld = last_wins(A / "cap/finales.jsonl"), last_wins(D / "cap/finales.jsonl")
validas = sorted(c for c, r in ra.items() if r.get("error") is None)
cambian_e1 = [c for c in validas if json.dumps(ra[c], sort_keys=True) != json.dumps(rd.get(c), sort_keys=True)]
cambian_fin = [c for c in la if json.dumps(la[c], sort_keys=True) != json.dumps(ld.get(c), sort_keys=True)]
criterio("C1 cap: append-only; las unidades con E1 válida conservan su último registro y su expediente",
         e1d.startswith(e1a) and fd.startswith(fa) and not cambian_e1 and not cambian_fin,
         {"unidades_con_e1_valida_antes": len(validas), "expedientes_antes": len(la),
          "extracciones_e1_lineas": [e1a.count(b"\n"), e1d.count(b"\n")], "finales_lineas": [fa.count(b"\n"), fd.count(b"\n")],
          "extracciones_antes_es_prefijo": e1d.startswith(e1a), "finales_antes_es_prefijo": fd.startswith(fa),
          "registros_e1_que_cambian": cambian_e1, "expedientes_que_cambian": cambian_fin,
          "unidades_nuevas_en_e1": sorted(set(rd) - set(ra)), "unidades_reescritas_en_e1": sorted(
              c for c in ra if c not in validas and json.dumps(ra[c], sort_keys=True) != json.dumps(rd[c], sort_keys=True)),
          "expedientes_nuevos": sorted(set(ld) - set(la))})

# C2. los otros nueve TOs, byte a byte; y qué cambia en la raíz de la salida y en cap
otros = {}
for to in TOS:
    fa_ = {p.relative_to(A / to).as_posix(): sha(p) for p in (A / to).rglob("*") if p.is_file()}
    fd_ = {p.relative_to(D / to).as_posix(): sha(p) for p in (D / to).rglob("*") if p.is_file()}
    otros[to] = {"archivos": [len(fa_), len(fd_)], "cambian": sorted(k for k in fa_ if fd_.get(k) not in (None, fa_[k])),
                 "nuevos": sorted(set(fd_) - set(fa_)), "borrados": sorted(set(fa_) - set(fd_))}
raiz_a = {p.relative_to(A).as_posix(): sha(p) for p in A.rglob("*") if p.is_file() and p.relative_to(A).parts[0] not in TOS}
raiz_d = {p.relative_to(D).as_posix(): sha(p) for p in D.rglob("*") if p.is_file() and p.relative_to(D).parts[0] not in TOS}
criterio("C2 en los otros nueve TOs no cambia ningún archivo",
         all(not (v["cambian"] or v["nuevos"] or v["borrados"]) for t, v in otros.items() if t != "cap"),
         {"por_to": otros, "raiz_de_la_salida": {"cambian": sorted(k for k in raiz_a if raiz_d.get(k) not in (None, raiz_a[k])),
                                                  "nuevos": sorted(set(raiz_d) - set(raiz_a))}})

# C3. particiones_por_corte.json, contra la precondición e (particionar_por_corte de la E0 de HEAD, en esta copia)
sys.path.insert(0, str(Path("data/experiment/reextraccion_v2/e1_extractor").resolve()))
sys.path.insert(0, str(Path("data/experiment/reextraccion_v2/e0_chunking").resolve()))
import comun_e1, correr_e0   # noqa: E402
E0 = Path("data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b")
ch = next(c for c in comun_e1.cargar_chunks(("cap",), e0_dir=E0) if c["id"] == UNIDAD)
pe, ie = correr_e0.particionar_por_corte(ch)
pp = json.loads((D / "cap/particiones_por_corte.json").read_text(encoding="utf-8"))
reg = pp.get(UNIDAD, {})
criterio("C3 particiones_por_corte.json: cap::4.2.1.2 con sus dos partes e informe, igual a la precondición e",
         list(pp) == [UNIDAD] and [p["id"] for p in reg.get("partes", [])] == [p["id"] for p in pe]
         and [hashlib.sha256(json.dumps(p, sort_keys=True, ensure_ascii=False).encode()).hexdigest() for p in reg["partes"]]
         == [hashlib.sha256(json.dumps(p, sort_keys=True, ensure_ascii=False).encode()).hexdigest() for p in pe]
         and reg.get("informe") == ie,
         {"unidades_partidas": list(pp), "partes": [(p["id"], p["chars_propio"]) for p in reg.get("partes", [])],
          "informe": reg.get("informe"), "precondicion_e": [(p["id"], p["chars_propio"]) for p in pe]})

# C6 (antes que C4: el gasto se recalcula de las filas nuevas). Filas nuevas en las bases = líneas nuevas de usage
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
ua = (a.antes / "cache_usage.jsonl").read_bytes()
ud = (a.despues / "cache_usage.jsonl").read_bytes()
nuevas = [json.loads(x) for x in ud[len(ua):].decode("utf-8").splitlines() if x.strip()]
gasto_filas = round(sum(f["usd"] for f in filas), 6)
criterio("C6 filas nuevas en las bases = líneas nuevas de usage, con el modelo y la temperatura de cada pedido",
         ud.startswith(ua) and len(filas) == len(nuevas) and all(f["posterior_al_inicio"] for f in filas),
         {"filas_nuevas_por_base": por_base, "filas_nuevas": len(filas), "lineas_de_usage_nuevas": len(nuevas),
          "usage_antes_es_prefijo": ud.startswith(ua),
          "usage_por_componente": {c: sum(1 for x in nuevas if x["component"] == c) for c in sorted({x["component"] for x in nuevas})},
          "gasto_recalculado_de_las_filas_usd": gasto_filas, "filas": filas})

# C4. estado_corpus y presupuesto compartido
ea = json.loads((A / "estado_corpus.json").read_text(encoding="utf-8"))
ed = json.loads((D / "estado_corpus.json").read_text(encoding="utf-8"))
pa_ = json.loads((A / "presupuesto_compartido.json").read_text(encoding="utf-8"))
pd_ = json.loads((D / "presupuesto_compartido.json").read_text(encoding="utf-8"))
g = {k: (ea["fases_cerradas"][k]["gasto_usd"], ed["fases_cerradas"].get(k, {}).get("gasto_usd")) for k in ("cap:e1", "cap:e3")}
r1 = json.loads((D / "cap/resumen_e1.json").read_text(encoding="utf-8"))
r3 = json.loads((D / "cap/resumen_e3.json").read_text(encoding="utf-8"))
nuevo_e1 = r1["cliente"]["gasto_usd_real"]
nuevo_e3 = r3["cliente_e3"]["gasto_usd_real"] + r3["cliente_e1_reintentos"]["gasto_usd_real"]
suma_fases = round(sum(f["gasto_usd"] for f in ed["fases_cerradas"].values()), 6)
nuevo_total = round(pd_["gasto_usd"] - pa_["gasto_usd"], 6)
otras_iguales = all(ea["fases_cerradas"][k] == ed["fases_cerradas"][k] for k in ea["fases_cerradas"] if not k.startswith("cap:"))
criterio("C4 estado_corpus: cap:e1 y cap:e3 cerradas con el gasto previo más el nuevo; el presupuesto suma lo mismo; "
         "el gasto nuevo no pasa el tope de USD 3",
         ed["fase_actual"] is None and abs(g["cap:e1"][1] - (g["cap:e1"][0] + nuevo_e1)) < 1e-4
         and abs(g["cap:e3"][1] - (g["cap:e3"][0] + nuevo_e3)) < 1e-4 and abs(suma_fases - pd_["gasto_usd"]) < 1e-5
         and abs(nuevo_total - gasto_filas) < 1e-5 and nuevo_total <= 3.0 and otras_iguales,
         {"cap_e1_antes_despues": g["cap:e1"], "cap_e3_antes_despues": g["cap:e3"],
          "nuevo_e1_resumen": nuevo_e1, "nuevo_e3_resumen": round(nuevo_e3, 6), "presupuesto_antes_despues": [pa_["gasto_usd"], pd_["gasto_usd"]],
          "gasto_nuevo_presupuesto": nuevo_total, "gasto_nuevo_filas": gasto_filas, "suma_fases_cerradas": suma_fases,
          "reaperturas": [{"key": x["key"], "ts": x["ts"], "gasto_previo_usd": x["fase_cerrada"]["gasto_usd"]} for x in ed.get("reaperturas", [])],
          "otras_fases_iguales": otras_iguales})

# C5. las partes y cap::3.1.1.2; el error de cap::4.2.1.2 en ninguna última versión
partes = [p["id"] for p in reg.get("partes", [])]
estado_partes = {p: {"error_e1": (rd.get(p) or {}).get("error", "sin registro"), "con_validacion": bool((rd.get(p) or {}).get("validacion")),
                     "escalon_3": bool((rd.get(p) or {}).get("escalon_3")), "estado_e3": (ld.get(p) or {}).get("estado")} for p in partes}
partes_ok = all(v["error_e1"] is None and v["con_validacion"] and v["estado_e3"] for v in estado_partes.values())
buscar = "ModuleNotFoundError"
apariciones = [f"extracciones_e1:{c}" for c, r in rd.items() if buscar in json.dumps(r.get("error"))] \
    + [f"finales:{c}" for c, r in ld.items() if buscar in json.dumps(r, ensure_ascii=False)] \
    + (["resumen_e1"] if buscar in json.dumps(r1, ensure_ascii=False) else []) \
    + (["resumen_e3"] if buscar in json.dumps(r3, ensure_ascii=False) else [])
u3 = rd.get("cap::3.1.1.2", {})
rf = u3.get("reintento_forma", {})


def forma(ti):
    return None if ti is None else {k: type(v).__name__ for k, v in ti.items()}


salidas_3112 = {"intento_1": forma((rf.get("intento_1") or {}).get("tool_input_crudo")),
                "reintento_1 (-rforma1)": forma(((rf.get("reintento_2") or {}).get("intento_2") or {}).get("tool_input_crudo")),
                "reintento_2 (-rforma2)": forma(u3.get("tool_input_crudo"))}
c3112_ok = (u3.get("error") is None and "cap::3.1.1.2" in ld) or (
    u3.get("error") == "salida_mal_formada_tras_reintento" and "reintento_2" in rf and all(salidas_3112.values()))
criterio("C5 las partes con E1 válida y E3 (o en la cola); el error de cap::4.2.1.2 en ninguna última versión; "
         "cap::3.1.1.2 válida o declarada con sus tres salidas mal formadas",
         partes_ok and not apariciones and rd.get(UNIDAD, {}).get("error") == "particionada_por_corte" and c3112_ok,
         {"partes": estado_partes, "ultimo_registro_de_la_unidad": rd.get(UNIDAD, {}).get("error"),
          "apariciones_de_ModuleNotFoundError_en_ultimas_versiones": apariciones,
          "cap_3_1_1_2": {"error": u3.get("error"), "en_finales": "cap::3.1.1.2" in ld,
                          "motivo_reintento_1": rf.get("motivo"), "motivo_reintento_2": (rf.get("reintento_2") or {}).get("motivo"),
                          "namespace_reintento_2": (rf.get("reintento_2") or {}).get("namespace"),
                          "salidas (claves y tipo)": salidas_3112},
          "resumen_e1": {k: r1.get(k) for k in ("n_unidades", "reintentos_forma", "particionadas_por_corte", "errores_definitivos", "escalon_3", "reintentos_corte")},
          "resumen_e3_estados": r3.get("estados")})

out = {"inicio_corrida": a.inicio, "criterios": res, "fallas": fallas, "veredicto": "OK" if not fallas else "FALLA"}
a.out.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
for k, v in res.items():
    print(("OK   " if v["ok"] else "FALLA"), k)
print("VEREDICTO:", out["veredicto"])
