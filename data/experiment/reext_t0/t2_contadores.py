"""
t2_contadores.py — U-REEXT-T0, T2 (mandato firmado en e2027dd): los contadores y las mediciones de T2, sobre COPIAS de
la salida de la corrida (corpus_tanda0/salida_r2b), de sus bases de caché y del log de usage. USD 0, sin red.

Cada cifra sale de un archivo de la corrida, que se nombra en la salida:
  a. unidades por estado final (una por unidad de E0; las partidas por corte, aparte, con el estado de sus partes) y
     las que quedan sin validación, una por una;
  b. el gasto real por etapa y por TO (estado_corpus.json, fases_cerradas), contra el estimado del manifiesto y la
     estimación de T1 (salida/corrida_en_seco_t1.json); llamadas y aciertos de caché de cada cliente (resumen_e1/e3);
  c. el registro del modelo de cada llamada pagada, con la temperatura de su pedido guardado (request_json de las
     filas de las bases con created_at desde el inicio de la corrida), y su línea de usage (logs/cache_usage.jsonl);
  d. el vocabulario retirado (tipo de Obligacion «requisito_de_estructura»: resumen_e1 y validación r2);
  e. las unidades con cada marca de E3 (reporte_e2_r2_<to>.json, stats.p3b.unidades_con_marca_e3);
  f. las salidas mal formadas y sus reintentos; los cortes en el primer intento y en el reintento, las partidas por
     corte y el tercer escalón, con sus tokens de salida (extracciones_e1.jsonl);
  g. los tokens de salida por carácter de texto propio (intento efectivo de E1 de cada unidad) por tramo de tamaño:
     < 500, 500 a 999, 1.000 a 2.999, 3.000 a 9.999 y 10.000 o más caracteres; aparte las de 3.000 o más y, una por una,
     las de 10.000 o más;
  h. las omisiones meta_normativo de la extracción final (validación r2): cuántas, con marca (validador_r2
     .marcas_meta_normativo y subclases_modalidad, importados) por clase y subclase, el contador del validador
     (contadores.omisiones de cada unidad) y aparte las del tramo solo en el texto heredado; las objetadas por E3 y
     las recuperadas por el reintento, con el criterio sellado antes de contar
     (data/experiment/reext_t0/t2_criterio_objecion_omisiones.md, sha256 5ceafba5…);
  i. las normas (Obligacion, Restriccion, Potestad) con aplica_a, en el crudo final y después de la validación;
  j. las relaciones aplica_a y ejecuta con una mención que no verifica (mencion_verificada «no»), con la mención y la
     unidad;
  k. el control de la caché de E3: aciertos (access_log, hit = 1, desde el inicio) sobre entradas con created_at
     anterior al inicio.

Uso (desde la raíz de una COPIA del repo, para importar validador_r2):
  PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B data/experiment/reext_t0/t2_contadores.py \
      --salida DIR_COPIA_SALIDA_R2B --bases DIR_COPIA_BASES --usage-antes A --usage-despues B --inicio ISO_LOCAL --out OUT
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sqlite3
import statistics
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
sys.path.insert(0, str(REPO / "data" / "experiment" / "pyd_r2" / "code"))
import validador_r2 as V  # noqa: E402 — marcas_meta_normativo y subclases_modalidad, importados

TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
E0 = REX / "e0_chunking" / "salida_tanda0_r2b"
MANIFIESTO = REX / "manifiestos" / "tanda0_10tos_r2b.json"
SECO = REPO / "data" / "experiment" / "reext_t0" / "salida" / "corrida_en_seco_t1.json"
CRITERIO = REPO / "data" / "experiment" / "reext_t0" / "t2_criterio_objecion_omisiones.md"
SHA_CRITERIO = "5ceafba51c106b0fc3be26fe5ebc14d5c7d9743e97405f6a6352ec568cbed982"
NORMAS = ("Obligacion", "Restriccion", "Potestad")
TRAMOS = ((0, 500), (500, 1000), (1000, 3000), (3000, 10000), (10000, 10 ** 9))
NS_E1 = "e1_extraccion|cv=e1-extractor-v1-p322c5a23e9b7|think=0"
NS_FORMA = "e1_extraccion|cv=e1-extractor-v1-p322c5a23e9b7-rforma1|think=0"
NS_E3 = "e3_verificacion|cv=e3-verificador-v1-p21a836c7de6d|think=0"
MIN_PALABRAS = 8


def jl(p: Path) -> list[dict]:
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()] if p.exists() else []


def last_wins(p: Path) -> dict:
    return {r["chunk_id"]: r for r in jl(p)}


def norm_pal(s) -> list[str]:
    s = unicodedata.normalize("NFD", str(s or "").replace("-\n", ""))
    s = "".join(c for c in s if not unicodedata.combining(c)).lower().replace("“", '"').replace("”", '"')
    return re.sub(r"[^a-z0-9]+", " ", s).split()


def solapa(a, b) -> bool:
    """Criterio sellado: uno contiene al otro, normalizados, o comparten 8 palabras seguidas."""
    pa, pb = norm_pal(a), norm_pal(b)
    if not pa or not pb:
        return False
    sa, sb = " ".join(pa), " ".join(pb)
    if sa in sb or sb in sa:
        return True
    if len(pa) < MIN_PALABRAS or len(pb) < MIN_PALABRAS:
        return False
    gramas = {tuple(pa[i:i + MIN_PALABRAS]) for i in range(len(pa) - MIN_PALABRAS + 1)}
    return any(tuple(pb[i:i + MIN_PALABRAS]) in gramas for i in range(len(pb) - MIN_PALABRAS + 1))


def pct(xs: list[float], q: float) -> float | None:
    if not xs:
        return None
    xs = sorted(xs)
    k = (len(xs) - 1) * q
    f, c = int(k), min(int(k) + 1, len(xs) - 1)
    return round(xs[f] + (xs[c] - xs[f]) * (k - f), 4)


def pred(r: dict) -> str | None:
    return r.get("predicate") or r.get("predicado")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", type=Path, required=True)
    ap.add_argument("--bases", type=Path, required=True)
    ap.add_argument("--usage-antes", type=Path, required=True)
    ap.add_argument("--usage-despues", type=Path, required=True)
    ap.add_argument("--inicio", required=True, help="hora local ISO del inicio de la corrida (created_at es local)")
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    if hashlib.sha256(CRITERIO.read_bytes()).hexdigest() != SHA_CRITERIO:
        raise SystemExit("el criterio de objeción no es el sellado")
    S = a.salida
    res: dict = {"fuentes": {"salida": "corpus_tanda0/salida_r2b (copia)", "criterio_objecion": f"{CRITERIO.name} ({SHA_CRITERIO[:8]}…)"}}

    chunks = {to: {c["id"]: c for c in json.loads((E0 / f"chunks_{to}.json").read_text(encoding="utf-8"))} for to in TOS}
    e1 = {to: last_wins(S / to / "extracciones_e1.jsonl") for to in TOS}
    fin = {to: last_wins(S / to / "finales.jsonl") for to in TOS}
    fr2 = {to: last_wins(S / to / f"extracciones_finales_r2_{to}.jsonl") for to in TOS}
    ver = {to: jl(S / to / "veredictos.jsonl") for to in TOS}
    rei = {to: jl(S / to / "reintentos_e3.jsonl") for to in TOS}
    part = {to: (json.loads((S / to / "particiones_por_corte.json").read_text(encoding="utf-8"))
                 if (S / to / "particiones_por_corte.json").exists() else {}) for to in TOS}

    # a. estados finales
    estados, sin_val, partidas = {}, [], []
    for to in TOS:
        c_est = Counter()
        for cid in chunks[to]:
            if cid in part[to]:
                c_est["particionada_por_corte"] += 1
                partidas.append({"chunk_id": cid, "partes": {p["id"]: (fin[to].get(p["id"]) or {}).get("estado")
                                                             or (e1[to].get(p["id"]) or {}).get("error")
                                                             for p in part[to][cid]["partes"]}})
                continue
            f = fin[to].get(cid)
            c_est[f["estado"] if f else f"sin_E3:{(e1[to].get(cid) or {}).get('error')}"] += 1
        estados[to] = dict(sorted(c_est.items()))
        for cid, r in fr2[to].items():
            if r.get("validacion") is None:
                sin_val.append({"chunk_id": cid, "error": r.get("error"), "estado_e3": r.get("estado_e3")})
    tot = Counter()
    for v in estados.values():
        tot.update(v)
    res["a_estados"] = {"por_to": estados, "total": dict(sorted(tot.items())), "suma": sum(tot.values()),
                        "unidades_e0": sum(len(c) for c in chunks.values()), "partidas": partidas,
                        "sin_validacion": sin_val, "n_sin_validacion": len(sin_val)}

    # b. gasto
    est = json.loads((S / "estado_corpus.json").read_text(encoding="utf-8"))
    man = json.loads(MANIFIESTO.read_text(encoding="utf-8"))
    seco = json.loads(SECO.read_text(encoding="utf-8"))["estimacion"]["escenarios"]
    gasto, clientes = {}, {}
    for to in TOS:
        g1 = est["fases_cerradas"].get(f"{to}:e1", {}).get("gasto_usd")
        g3 = est["fases_cerradas"].get(f"{to}:e3", {}).get("gasto_usd")
        r1 = json.loads((S / to / "resumen_e1.json").read_text(encoding="utf-8")) if (S / to / "resumen_e1.json").exists() else {}
        r3 = json.loads((S / to / "resumen_e3.json").read_text(encoding="utf-8")) if (S / to / "resumen_e3.json").exists() else {}
        gasto[to] = {"e1_usd": g1, "e3_usd": g3, "total_usd": round((g1 or 0) + (g3 or 0), 4),
                     "estimado_manifiesto_usd": round(man["limites"]["estimado_usd"][to]["e1"] + man["limites"]["estimado_usd"][to]["e3"], 4),
                     "estimacion_t1_central_usd": {k: v["por_to"][to]["central_usd"] for k, v in seco.items()}}
        clientes[to] = {"e1": {k: (r1.get("cliente") or {}).get(k) for k in ("llamadas", "hits_cache_local", "gasto_usd_real")},
                        "e3": {k: (r3.get("cliente_e3") or {}).get(k) for k in ("llamadas", "hits_cache_local", "gasto_usd_real")},
                        "e1_reintentos": {k: (r3.get("cliente_e1_reintentos") or {}).get(k) for k in ("llamadas", "hits_cache_local", "gasto_usd_real")}}
    pres = json.loads((S / "presupuesto_compartido.json").read_text(encoding="utf-8"))
    res["b_gasto"] = {"por_to": gasto, "clientes": clientes,
                      "total_e1_usd": round(sum(g["e1_usd"] or 0 for g in gasto.values()), 4),
                      "total_e3_usd": round(sum(g["e3_usd"] or 0 for g in gasto.values()), 4),
                      # suma sin redondear: la suma de los totales por TO ya redondeados no cierra
                      "total_usd": round(sum((g["e1_usd"] or 0) + (g["e3_usd"] or 0) for g in gasto.values()), 4),
                      "presupuesto_compartido": {k: pres.get(k) for k in ("gasto_usd", "tope_usd")},
                      "tope_usd": man["limites"]["tope_global_usd"],
                      "estimacion_t1_total_usd": {k: v["central_usd"] for k, v in seco.items()}}

    # c. registro de modelos y usage
    regs = {}
    filas_nuevas = 0
    for nombre in ("e1_extraccion.db", "e3_verificacion.db", "e1_reintentos.db"):
        con = sqlite3.connect(str(a.bases / nombre))
        try:
            filas = con.execute("SELECT namespace, model, request_json FROM cache WHERE created_at >= ?", (a.inicio,)).fetchall()
            acc = con.execute("SELECT hit, count(*) FROM access_log WHERE ts >= ? GROUP BY hit", (a.inicio,)).fetchall()
        finally:
            con.close()
        c = Counter()
        for ns, model, rq in filas:
            q = json.loads(rq)
            t = q.get("temperature", "default del proveedor")
            c[f"{ns} | pedido {q.get('model')} | respuesta {model} | temperatura {t}"] += 1
        filas_nuevas += len(filas)
        regs[nombre] = {"llamadas_pagadas_registradas": len(filas), "por_namespace_modelo_temperatura": dict(sorted(c.items())),
                        "access_log_desde_el_inicio": {("aciertos" if h else "fallos"): n for h, n in acc}}
    ua = a.usage_antes.read_text(encoding="utf-8").splitlines()
    ud = a.usage_despues.read_text(encoding="utf-8").splitlines()
    nuevas = [json.loads(x) for x in ud[len(ua):] if x.strip()]
    res["c_modelos_y_usage"] = {"bases": regs, "filas_nuevas_en_las_bases": filas_nuevas,
                                "lineas_de_usage_nuevas": len(nuevas),
                                "usage_por_componente": dict(sorted(Counter(x.get("component") for x in nuevas).items())),
                                "usage_antes_es_prefijo": ud[:len(ua)] == ua}

    # d. vocabulario retirado
    ret = {}
    for to in TOS:
        r1 = json.loads((S / to / "resumen_e1.json").read_text(encoding="utf-8")) if (S / to / "resumen_e1.json").exists() else {}
        en_val = sum(1 for r in fr2[to].values() for e in ((r.get("validacion") or {}).get("entidades") or [])
                     if e.get("type") == "Obligacion" and (e.get("properties") or {}).get("tipo") == "requisito_de_estructura")
        ret[to] = {"resumen_e1": r1.get("tipo_obligacion_requisito_de_estructura"), "validacion_r2": en_val}
    res["d_vocabulario_retirado"] = {"por_to": ret, "total": sum((v["resumen_e1"] or 0) + v["validacion_r2"] for v in ret.values())}

    # e. marcas de E3
    marcas = {}
    for to in TOS:
        p = S / to / f"reporte_e2_r2_{to}.json"
        marcas[to] = (json.loads(p.read_text(encoding="utf-8"))["stats"].get("p3b") or {}).get("unidades_con_marca_e3") if p.exists() else None
    mt = Counter()
    for v in marcas.values():
        mt.update(v or {})
    res["e_marcas_e3"] = {"por_to": marcas, "total": dict(sorted(mt.items()))}

    # f. forma, cortes, partidas y tercer escalón
    forma, cortes, esc3 = [], [], []
    for to in TOS:
        for cid, r in e1[to].items():
            if "reintento_forma" in r:
                forma.append({"chunk_id": cid, "motivo": r["reintento_forma"].get("motivo"), "error_final": r.get("error")})
            if "reintento_corte" in r:
                cortes.append({"chunk_id": cid, "salida_intento_1": ((r["reintento_corte"].get("intento_1") or {}).get("usage") or {}).get("output_tokens"),
                               "salida_efectiva": (r.get("usage") or {}).get("output_tokens"), "escalon_3": "escalon_3" in r,
                               "particionada": r.get("error") == "particionada_por_corte", "error": r.get("error")})
            if "escalon_3" in r:
                esc3.append({"chunk_id": cid, "salida_intento_2": ((r["escalon_3"].get("intento_2") or {}).get("usage") or {}).get("output_tokens"),
                             "salida_efectiva": (r.get("usage") or {}).get("output_tokens"), "error": r.get("error")})
    res["f_forma_cortes_escalon3"] = {"reintentos_por_forma": forma, "mal_formadas_tras_reintento": sum(1 for x in forma if x["error_final"]),
                                     "cortan_primer_intento": len(cortes), "cortan_en_el_reintento": sum(1 for x in cortes if x["escalon_3"] or x["particionada"]),
                                     "cortes": cortes, "particionadas": [x["chunk_id"] for x in cortes if x["particionada"]],
                                     "tercer_escalon": esc3}

    # g. salida por carácter
    filas_g = []
    for to in TOS:
        todos = dict(chunks[to])
        for cid in part[to]:
            for p in part[to][cid]["partes"]:
                todos[p["id"]] = p
        for cid, r in e1[to].items():
            c = todos.get(cid)
            out = (r.get("usage") or {}).get("output_tokens")
            if c is None or not out or r.get("error") == "particionada_por_corte" or not c.get("chars_propio"):
                continue
            filas_g.append((cid, c["chars_propio"], out, out / c["chars_propio"]))
    tramos = {}
    for lo, hi in TRAMOS:
        xs = [x[3] for x in filas_g if lo <= x[1] < hi]
        tramos[f"{lo}-{hi - 1 if hi < 10 ** 9 else 'mas'}"] = {"unidades": len(xs), "mediana": pct(xs, .5), "p90": pct(xs, .9),
                                                               "max": round(max(xs), 4) if xs else None}
    g3000 = [x[3] for x in filas_g if x[1] >= 3000]
    res["g_salida_por_caracter"] = {"unidades": len(filas_g), "por_tramo": tramos,
                                    "de_3000_o_mas": {"unidades": len(g3000), "mediana": pct(g3000, .5), "p90": pct(g3000, .9)},
                                    "de_10000_o_mas": [{"chunk_id": x[0], "chars_propio": x[1], "salida": x[2], "por_caracter": round(x[3], 4)}
                                                       for x in sorted(filas_g, key=lambda y: -y[1]) if x[1] >= 10000]}

    # h. omisiones meta_normativo
    om = {}
    obj_total = Counter()
    objetadas_lista = []
    for to in TOS:
        n = con_marca = heredado = 0
        clases, subs, contador = Counter(), Counter(), Counter()
        for cid, r in fr2[to].items():
            v = r.get("validacion") or {}
            for k, x in ((v.get("contadores") or {}).get("omisiones") or {}).items():
                if k.startswith("meta_normativo") or k.startswith("tramo_solo") or k == "categoria:meta_normativo":
                    contador[k] += x
            for o in v.get("omisiones") or []:
                if o.get("categoria") != "meta_normativo":
                    continue
                n += 1
                cl = V.marcas_meta_normativo(o.get("tramo") or "")
                con_marca += bool(cl)
                clases.update(cl)
                if "modalidad" in cl:
                    subs.update(V.subclases_modalidad(o.get("tramo") or ""))
        heredado = contador.get("tramo_solo_heredado", 0)
        # objeción, con el criterio sellado: omisiones del crudo que vio la primera verificación y sus faltantes
        primeras = {}
        for x in ver[to]:
            if x.get("fase") == "verificacion" and x.get("intento") == 0 and x["chunk_id"] not in primeras:
                primeras[x["chunk_id"]] = x
        n_obj = n_rec = n_dejo = n_vistas = 0
        for cid, r in e1[to].items():
            oms = [o for o in ((r.get("tool_input_crudo") or {}).get("omisiones") or []) if o.get("categoria") == "meta_normativo"]
            if not oms or cid not in primeras:
                continue
            n_vistas += len(oms)
            falt = [f.get("cita_textual_del_fuente") for f in (primeras[cid].get("faltantes") or [])]
            final = fr2[to].get(cid) or {}
            reintento = (fin[to].get(cid) or {}).get("n_reintentos", 0) > 0
            vf = final.get("validacion") or {}
            om_final = [o.get("tramo") for o in (vf.get("omisiones") or []) if o.get("categoria") == "meta_normativo"]
            textos = [" ".join([e.get("label") or "", str((e.get("properties") or {}).get("descripcion") or "")]) for e in vf.get("entidades") or []]
            for o in oms:
                t = o.get("tramo") or ""
                if not any(solapa(f, t) for f in falt):
                    continue
                n_obj += 1
                fila = {"chunk_id": cid, "tramo": t[:160], "reintento": reintento, "recuperada": False}
                if reintento and not any(solapa(x, t) for x in om_final):
                    if any(solapa(x, t) for x in textos):
                        n_rec += 1
                        fila["recuperada"] = True
                    else:
                        n_dejo += 1
                        fila["dejo_de_declararse_sin_el_contenido"] = True
                objetadas_lista.append(fila)
        om[to] = {"meta_normativo": n, "con_marca": con_marca, "por_clase": dict(sorted(clases.items())),
                  "modalidad_por_subclase": dict(sorted(subs.items())), "tramo_solo_heredado": heredado,
                  "contador_validador": dict(sorted(contador.items())),
                  "vistas_por_la_primera_verificacion": n_vistas, "objetadas_por_e3": n_obj, "recuperadas_por_el_reintento": n_rec,
                  "dejaron_de_declararse_sin_el_contenido": n_dejo}
        obj_total.update({k: v for k, v in om[to].items() if isinstance(v, int)})
    res["h_omisiones_meta_normativo"] = {"por_to": om, "total": dict(sorted(obj_total.items())), "objetadas": objetadas_lista}

    # i. normas con sujeto, crudo final y validación
    normas = {}
    for to in TOS:
        crudo_n = crudo_ap = val_n = val_ap = 0
        sin_crudo = []
        rei_por = defaultdict(dict)
        for x in rei[to]:
            rei_por[x["chunk_id"]][x.get("intento")] = x
        for cid, r in fr2[to].items():
            org = r.get("origen_crudo") or "e1"
            if org == "e1":
                ti = (e1[to].get(cid) or {}).get("tool_input_crudo")
            else:
                m = re.match(r"reintento_(\d+)", org)      # p. ej. «reintento_1:companero»
                ti = (rei_por[cid].get(int(m.group(1))) or {}).get("tool_input") if m else None
                if ti is None:
                    sin_crudo.append({"chunk_id": cid, "origen_crudo": org})
            if ti:
                ids = {e.get("local_id") for e in ti.get("entities") or [] if e.get("type") in NORMAS}
                con = {x.get("source") for x in ti.get("relations") or [] if pred(x) == "aplica_a" and x.get("source") in ids}
                crudo_n += len(ids)
                crudo_ap += len(con)
            v = r.get("validacion") or {}
            ids = {e.get("local_id") for e in v.get("entidades") or [] if e.get("type") in NORMAS}
            con = {x.get("source") for x in v.get("relaciones") or [] if pred(x) == "aplica_a" and x.get("source") in ids}
            val_n += len(ids)
            val_ap += len(con)
        normas[to] = {"crudo": {"normas": crudo_n, "con_aplica_a": crudo_ap}, "validacion": {"normas": val_n, "con_aplica_a": val_ap},
                      "unidades_sin_crudo_localizado": sin_crudo}
    res["i_normas_con_sujeto"] = {"por_to": normas,
                                  "total": {f: {k: sum(normas[t][f][k] for t in TOS) for k in ("normas", "con_aplica_a")}
                                            for f in ("crudo", "validacion")}}

    # j. menciones que no verifican
    men = []
    for to in TOS:
        for cid, r in fr2[to].items():
            for x in ((r.get("validacion") or {}).get("relaciones") or []):
                if pred(x) in ("aplica_a", "ejecuta") and x.get("mencion_verificada") == "no":
                    men.append({"to": to, "chunk_id": cid, "predicado": pred(x), "mencion": x.get("sujeto_mencion"),
                                "sujeto_id_modelo": x.get("sujeto_id_modelo")})
    res["j_menciones_que_no_verifican"] = {"por_to": dict(Counter(m["to"] for m in men)), "total": len(men), "filas": men}

    # k. caché de E3: aciertos sobre entradas anteriores al inicio
    con = sqlite3.connect(str(a.bases / "e3_verificacion.db"))
    try:
        hits = con.execute("SELECT a.key, a.run_label, c.created_at FROM access_log a JOIN cache c ON c.key = a.key "
                           "WHERE a.ts >= ? AND a.hit = 1", (a.inicio,)).fetchall()
    finally:
        con.close()
    viejos = [{"clave": k, "run_label": rl, "created_at": ca} for k, rl, ca in hits if ca < a.inicio]
    res["k_cache_e3"] = {"aciertos_desde_el_inicio": len(hits), "sobre_entradas_anteriores_al_inicio": len(viejos), "filas": viejos}

    a.out.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"a_suma": res["a_estados"]["suma"], "a_total": res["a_estados"]["total"],
                      "sin_validacion": res["a_estados"]["n_sin_validacion"], "gasto": res["b_gasto"]["total_usd"],
                      "retirado": res["d_vocabulario_retirado"]["total"], "marcas": res["e_marcas_e3"]["total"],
                      "usage_nuevas": len(nuevas), "filas_nuevas": filas_nuevas, "k": res["k_cache_e3"]["sobre_entradas_anteriores_al_inicio"]},
                     ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
