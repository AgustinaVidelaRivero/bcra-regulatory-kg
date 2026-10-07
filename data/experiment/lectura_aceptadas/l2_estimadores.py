"""
l2_estimadores.py — U-LECTURA-ACEPTADAS, L2 (mandato FIRMADO en 9502ca4, §5 y §6; nota al pie del 06/10/2026 en 6e611d6):
las cifras con la adjudicación de la autora y el reporte. USD 0, sin API; solo lee archivos de lectura_aceptadas/ y la
tasa de la cola de T4.

Insumos (todos por argumento, con su sha256 en la salida):
  - sellos_l0.json: la población (N, N₁, N₂ se recomputan contando las filas por estrato) y la muestra;
  - veredictos_l1.jsonl: la primera lectura; fichas_l1.jsonl: los nodos y aristas de cada unidad;
  - adjudicacion_autora_l2.json (su sha256 se pasa y se controla): las 10 confirmadas, las dudas como observaciones,
    las tres decisiones y la arista A1 de ext::3.17.3.4;
  - reext_t0/t4/salida/tasas_t4.json: la tasa adjudicada de la cola (12 de 30), para la comparación.

Estimadores (mandato §5, escritos antes de leer): Wilson al 95 % por estrato con z = 1,959964 (la misma fórmula que
reext_t0/t4/tasas_t4.py:244-249, para que la comparación con la cola sea directa); ponderado p̂ = W₁·p̂₁ + W₂·p̂₂ con
p̂ ± z·√(W₁²·p̂₁(1−p̂₁)/n₁ + W₂²·p̂₂(1−p̂₂)/n₂), sin corrección por población finita (como escribe el mandato); y el
conservador por combinación de los límites de Wilson (W₁·LI₁ + W₂·LI₂; W₁·LS₁ + W₂·LS₂).

Corre desde la raíz de una COPIA del repo (CLAUDE.md §4.l) y escribe solo --salida/estimadores_l2.json y
--salida/reporte_l2.md.
  PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B data/experiment/lectura_aceptadas/l2_estimadores.py \
      --sellos S --veredictos V --fichas F --adjudicacion A --adjudicacion-sha256 H --tasas-t4 T --salida DIR
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from datetime import datetime
from math import sqrt
from pathlib import Path

Z = 1.959964
ESTRATOS = ("item", "no_item")
NOMBRE_ESTRATO = {"item": "ítems", "no_item": "no ítems"}
PUNTO_T4 = {"punto_1_cola_humana": "punto 1, cola humana", "punto_3_copia_nota": "punto 3, copia de la nota de E3",
            "punto_5_p4b": "punto 5, P4b", "punto_6_listas": "punto 6, listas",
            "punto_7_grupo_c_fase_a": "punto 7, grupo c", "punto_8_omisiones": "punto 8, omisiones"}
# Clase de cada elemento no sostenido (las seis del «seguí» de L2), por unidad y referencia.
CLASE = {
    ("cap::5.4.5", "A1"): "relación no sostenida",
    ("ext::3.17.3.4", "A1"): "relación no sostenida",
    ("ext::3.17.3.4", "A2"): "relación no sostenida",
    ("ctacte::6.1.2.5", "N2"): "causal de rechazo leída como prohibición",
    ("ctacte::6.1.2.5", "A1"): "causal de rechazo leída como prohibición",
    ("ext::7.9.1.1", "N2"): "permiso leído como deber",
    ("ctacte::6.1.2.7", "N3"): "causal de rechazo leída como prohibición",
    ("ctacte::6.1.2.7", "A2"): "causal de rechazo leída como prohibición",
    ("ctacte::6.1.2.7", "A1"): "causal de rechazo leída como prohibición",
    ("lingob::2.3.2.1", "A1"): "relación no sostenida",
    ("ext::7.3.11", "N4"): "permiso leído como deber",
    ("ext::7.3.11", "A3"): "sujeto equivocado",
    ("ext::10.2.4::cierre", "N1"): "rótulo y tipo invertidos",
    ("ctacte::1.5.2.9", "N9"): "deber acotado leído como prohibición",
    ("ctacte::9.1.3", "A3"): "relación no sostenida",
}


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def wilson(k: int, n: int, z: float = Z) -> tuple[float, float]:
    p = k / n
    den = 1 + z * z / n
    centro = (p + z * z / (2 * n)) / den
    medio = z * sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return max(0.0, centro - medio), min(1.0, centro + medio)


def f(x: float, d: int = 4) -> str:
    """Número con coma decimal, para el reporte."""
    return f"{x:.{d}f}".replace(".", ",")


def pl(n: int, s: str, p: str | None = None) -> str:
    return f"{n} {s if n == 1 else (p or s + 's')}"


def miles(n: int) -> str:
    return f"{n:,}".replace(",", ".")


def k_minimo(n: int, umbral: float) -> int | None:
    """El menor k de n cuyo límite inferior de Wilson supera el umbral (para la vigilancia por tanda)."""
    for k in range(n + 1):
        if wilson(k, n)[0] > umbral:
            return k
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    for a_ in ("--sellos", "--veredictos", "--fichas", "--adjudicacion", "--tasas-t4", "--salida"):
        ap.add_argument(a_, type=Path, required=True)
    ap.add_argument("--adjudicacion-sha256", required=True)
    a = ap.parse_args()

    shas = {n: sha(p.read_bytes()) for n, p in (("sellos_l0.json", a.sellos), ("veredictos_l1.jsonl", a.veredictos),
                                                ("fichas_l1.jsonl", a.fichas),
                                                ("adjudicacion_autora_l2.json", a.adjudicacion),
                                                ("tasas_t4.json", a.tasas_t4))}
    if shas["adjudicacion_autora_l2.json"] != a.adjudicacion_sha256:
        raise SystemExit(f"adjudicacion_autora_l2.json con sha256 {shas['adjudicacion_autora_l2.json']}, no el pasado")
    s = json.loads(a.sellos.read_text(encoding="utf-8"))
    ver = [json.loads(x) for x in a.veredictos.read_text(encoding="utf-8").splitlines() if x.strip()]
    fichas = {x["id"]: x for x in (json.loads(y) for y in a.fichas.read_text(encoding="utf-8").splitlines() if y.strip())}
    adj = json.loads(a.adjudicacion.read_text(encoding="utf-8"))
    t4 = json.loads(a.tasas_t4.read_text(encoding="utf-8"))
    hora = datetime.now().astimezone().isoformat(timespec="seconds")

    # ---- población y pesos, recomputados desde las filas del sello
    filas = s["poblacion"]["filas"]
    N_h = Counter(x[3] for x in filas)
    N = len(filas)
    if (N, N_h["item"], N_h["no_item"]) != (s["poblacion"]["N"], s["poblacion"]["N1_item"], s["poblacion"]["N2_no_item"]):
        raise SystemExit("los conteos de las filas del sello no dan N, N1 y N2 del sello")
    W = {e: N_h[e] / N for e in ESTRATOS}
    muestra = {e: [m["id"] for m in s["sorteo"]["muestra"][e]] for e in ESTRATOS}
    if [v["id"] for v in ver] != muestra["item"] + muestra["no_item"] or set(fichas) != set(muestra["item"] + muestra["no_item"]):
        raise SystemExit("veredictos o fichas no son las 60 de la muestra sellada, en su orden")

    # ---- la adjudicación sobre la primera lectura
    confirmadas = {e: adj["con_error_confirmadas"][e] for e in ESTRATOS}
    primera = {e: [v["id"] for v in ver if v["estrato"] == e and v["veredicto"] == "con_error"] for e in ESTRATOS}
    if any(sorted(confirmadas[e]) != sorted(primera[e]) for e in ESTRATOS):
        raise SystemExit("la lista adjudicada no coincide con las con error de la primera lectura")
    agregado = adj["elemento_agregado_por_la_decision_2"]
    filas_ver = []
    for v in ver:
        marca = "con_error" if v["id"] in confirmadas[v["estrato"]] else "sin_error"
        elementos = [{"elemento": x["elemento"], "ref": r, "por_que": x["por_que"], "lectura": "primera"}
                     for x in v["no_sostenido"] for r in x["refs"]]
        if v["id"] == agregado["id"]:
            elementos.insert(0, {"elemento": agregado["elemento"], "ref": agregado["ref"], "por_que": agregado["por_que"],
                                 "lectura": "segunda (decisión 2)"})
        refs_ficha = {n["ref"] for n in fichas[v["id"]]["nodos"]} | {x["ref"] for x in fichas[v["id"]]["aristas"]}
        for x in elementos:
            if x["ref"] not in refs_ficha:
                raise SystemExit(f"{v['id']}: {x['ref']} no está en la ficha")
            x["clase"] = CLASE[(v["id"], x["ref"])]
        if (marca == "con_error") != bool(elementos):
            raise SystemExit(f"{v['id']}: marca {marca} con {len(elementos)} elementos")
        filas_ver.append({**{k: v[k] for k in ("n", "id", "estrato", "to", "estado")}, "marca": marca,
                          "elementos": elementos, "observaciones_por_dudas": v["dudas"],
                          "observaciones": v["observaciones"], "omisiones": v["omisiones"]})
    if len(CLASE) != sum(len(x["elementos"]) for x in filas_ver):
        raise SystemExit("hay clases sin elemento o elementos sin clase")

    # ---- (i) la tasa de la unidad
    est = {}
    for e in ESTRATOS:
        xs = [x for x in filas_ver if x["estrato"] == e]
        k, n = sum(x["marca"] == "con_error" for x in xs), len(xs)
        li, ls = wilson(k, n)
        est[e] = {"k": k, "n": n, "p": k / n, "wilson95": [li, ls], "N_h": N_h[e], "W_h": W[e]}
    p_pond = sum(W[e] * est[e]["p"] for e in ESTRATOS)
    var = sum(W[e] ** 2 * est[e]["p"] * (1 - est[e]["p"]) / est[e]["n"] for e in ESTRATOS)
    ponderado = {
        "p": p_pond, "ee": sqrt(var), "medio": Z * sqrt(var), "intervalo95": [p_pond - Z * sqrt(var), p_pond + Z * sqrt(var)],
        "intervalo95_con_1_96": [p_pond - 1.96 * sqrt(var), p_pond + 1.96 * sqrt(var)],
        "conservador95": [sum(W[e] * est[e]["wilson95"][0] for e in ESTRATOS),
                          sum(W[e] * est[e]["wilson95"][1] for e in ESTRATOS)],
        "fraccion_muestral": {e: est[e]["n"] / N_h[e] for e in ESTRATOS},
        "nota": "sin corrección por población finita, como escribe el mandato §5"}
    cola = t4["punto_1"]["con_error"]

    def tabla(clave: str) -> dict:
        out = {}
        for e in ESTRATOS + ("ambos",):
            xs = [x for x in filas_ver if e == "ambos" or x["estrato"] == e]
            c = Counter((x[clave], x["marca"]) for x in xs)
            out[e] = {g: {"con_error": c[(g, "con_error")], "de": c[(g, "con_error")] + c[(g, "sin_error")]}
                      for g in sorted({x[clave] for x in xs})}
        return out

    # ---- (ii) las remite_a
    rem = {}
    for e in ESTRATOS:
        ids = [x["id"] for x in filas_ver if x["estrato"] == e]
        ar = [y for i in ids for y in fichas[i]["aristas"] if y["clase"] == "remision_derivada"]
        uds = [i for i in ids if any(y["clase"] == "remision_derivada" for y in fichas[i]["aristas"])]
        ns = sum(v["remisiones_derivadas"]["no_sostenidas"] for v in ver if v["id"] in ids)
        rem[e] = {"aristas": len(ar), "unidades": len(uds), "no_sostenidas": ns, "ids": uds}
    rem_tot = {"aristas": sum(rem[e]["aristas"] for e in ESTRATOS), "unidades": sum(rem[e]["unidades"] for e in ESTRATOS),
               "no_sostenidas": sum(rem[e]["no_sostenidas"] for e in ESTRATOS)}
    rem_tot["wilson95_aristas"] = list(wilson(rem_tot["no_sostenidas"], rem_tot["aristas"]))
    rem_tot["unidades_con_alguna_no_sostenida"] = sum(1 for e in ESTRATOS for v in ver if v["id"] in rem[e]["ids"]
                                                      and v["remisiones_derivadas"]["no_sostenidas"])
    rem_tot["wilson95_unidades"] = list(wilson(rem_tot["unidades_con_alguna_no_sostenida"], rem_tot["unidades"]))
    rem_tot["nota"] = ("las aristas no son independientes (van agrupadas en las unidades, y en cada unidad repiten la cita "
                       "por cada nodo de origen y de destino): el intervalo por aristas es descriptivo; el de unidades es "
                       "el más honesto. Ninguno se pondera por estrato.")

    # ---- (iii) tipos documentales mal asignados (observación)
    doc = []
    for x in filas_ver:
        for n_ in fichas[x["id"]]["nodos"]:
            if n_["type"] == "Comunicacion":
                cod = str((n_["properties"] or {}).get("codigo", ""))
                clase = ("punto del mismo TO" if n_["label"].startswith("Punto") else
                         "ley" if "Ley" in cod else "otra")
                doc.append({"id": x["id"], "estrato": x["estrato"], "ref": n_["ref"], "label": n_["label"],
                            "codigo": cod, "clase": clase})

    # ---- observaciones, omisiones, solapamiento, cla::1.2.1
    con_dudas = [{"id": x["id"], "observacion": x["observaciones_por_dudas"]} for x in filas_ver
                 if x["observaciones_por_dudas"]]
    omis = {e: sum(1 for x in filas_ver if x["estrato"] == e and x["omisiones"]) for e in ESTRATOS}
    sin_contenido = {e: [x["id"] for x in filas_ver if x["estrato"] == e and not any(
        n_["type"] not in ("TextoOrdenado", "Sujeto") for n_ in fichas[x["id"]]["nodos"])] for e in ESTRATOS}
    marca_de = {x["id"]: x["marca"] for x in filas_ver}
    solap = s["solapamiento_t4"]
    puntos_de = {}
    for punto, v in solap["por_punto"].items():
        for i in v["en_la_muestra"]:
            puntos_de.setdefault(i, []).append(punto)
    solapamiento = [{"id": i, "puntos_t4": puntos_de[i], "marca": marca_de[i]}
                    for i in solap["unidades_de_la_muestra_leidas_en_t4"]]
    cla = next(x for x in filas_ver if x["id"] == "cla::1.2.1")

    # ---- vigilancia por tanda (para el pre-registro)
    vig = {e: {"LS_tanda0": est[e]["wilson95"][1], "k_minimo_de_30_que_dispara": k_minimo(30, est[e]["wilson95"][1])}
           for e in ESTRATOS}
    vig["ponderado"] = {"LS_conservador_tanda0": ponderado["conservador95"][1]}

    out = {
        "unidad": "U-LECTURA-ACEPTADAS, L2 (cifras con la adjudicación)", "hora": hora, "insumos_sha256": shas,
        "z": Z, "poblacion": {"N": N, "N_h": dict(N_h), "W": W},
        "i_tasa_por_unidad": {"por_estrato": est, "ponderado": ponderado,
                              "cola_t4": {"k": cola["k"], "n": cola["n"], "wilson95": cola["wilson95"],
                                          "fuente": "data/experiment/reext_t0/t4/salida/tasas_t4.json, punto_1"}},
        "ii_remite_a": {"por_estrato": rem, "total": rem_tot},
        "iii_tipos_documentales": {"nodos": len(doc), "unidades": sorted({d["id"] for d in doc}),
                                   "por_clase": dict(Counter(d["clase"] for d in doc)), "detalle": doc},
        "descriptivo": {"por_estado": tabla("estado"), "por_to": tabla("to")},
        "con_error": [x for x in filas_ver if x["marca"] == "con_error"],
        "elementos_por_clase": dict(Counter(y["clase"] for x in filas_ver for y in x["elementos"])),
        "unidades_por_clase": dict(Counter(c for x in filas_ver for c in {y["clase"] for y in x["elementos"]})),
        "observaciones_por_dudas": con_dudas, "omisiones_aparte": omis, "sin_nodos_de_contenido": sin_contenido,
        "solapamiento_t4": solapamiento, "cla_1_2_1": {"marca": cla["marca"], "primera_lectura": "sin_error",
                                                        "segunda_lectura": "sin_error (60 de 60 iguales)"},
        "vigilancia": vig, "l2_estimadores.py_sha256": sha(Path(__file__).read_bytes()),
    }
    a.salida.mkdir(parents=True, exist_ok=True)
    (a.salida / "estimadores_l2.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    reporte(a.salida, out, s, adj, shas)
    print(json.dumps({"hora": hora,
                      "estratos": {e: [est[e]["k"], est[e]["n"], round(est[e]["p"], 4),
                                       [round(x, 4) for x in est[e]["wilson95"]]] for e in ESTRATOS},
                      "W": {e: round(W[e], 6) for e in ESTRATOS},
                      "ponderado": [round(p_pond, 4), round(ponderado["medio"], 4),
                                    [round(x, 4) for x in ponderado["intervalo95"]]],
                      "conservador": [round(x, 4) for x in ponderado["conservador95"]],
                      "remite_a": [rem_tot["no_sostenidas"], rem_tot["aristas"], rem_tot["unidades"],
                                   [round(x, 4) for x in rem_tot["wilson95_aristas"]],
                                   [round(x, 4) for x in rem_tot["wilson95_unidades"]]],
                      "documentales": [len(doc), out["iii_tipos_documentales"]["por_clase"]],
                      "elementos_por_clase": out["elementos_por_clase"],
                      "vigilancia_k_min": {e: vig[e]["k_minimo_de_30_que_dispara"] for e in ESTRATOS}},
                     ensure_ascii=False))
    return 0


def reporte(salida: Path, o: dict, s: dict, adj: dict, shas: dict) -> None:
    est, pond = o["i_tasa_por_unidad"]["por_estrato"], o["i_tasa_por_unidad"]["ponderado"]
    cola, rem, doc = o["i_tasa_por_unidad"]["cola_t4"], o["ii_remite_a"], o["iii_tipos_documentales"]
    N, Nh, W = o["poblacion"]["N"], o["poblacion"]["N_h"], o["poblacion"]["W"]
    ls = lambda x: f"[{f(x[0])}; {f(x[1])}]"  # noqa: E731
    L = [
        "# U-LECTURA-ACEPTADAS — reporte de L2: tasa de error por unidad de las aceptadas de la tanda 0", "",
        f"Generado por `l2_estimadores.py` a las {o['hora']} (USD 0, sin API). Mandato `docs/mandatos/"
        "ULECTURA_ACEPTADAS_tasa_error_tanda0.md`, FIRMADO en `9502ca4`, con su nota al pie del 06/10/2026 (`6e611d6`). "
        "Todas las cifras salen de `estimadores_l2.json`, que el mismo script escribe; el comando está en la sección 9.", "",
        "## 1. Método", "",
        f"- **Población.** Las unidades aceptadas del grafo evaluado de los diez TOs sin la cola (KG-Tanda0-Diez-r2b-sincola, "
        f"`e22fae1a…`): las de estado final `completo_ok_directo`, `aceptado_con_residuales` o `aceptado_tras_reintento` en "
        f"`corpus_tanda0/salida_r2b/<to>/finales.jsonl`. N = {miles(N)}; ítems de lista (`prompt_r2b.es_item` sobre el chunk de "
        f"E0 r2b) N₁ = {miles(Nh['item'])} y no ítems N₂ = {miles(Nh['no_item'])}; W₁ = {miles(Nh['item'])}/{miles(N)} = "
        f"{f(W['item'], 6)} y W₂ = {f(W['no_item'], 6)}, recomputados contando las filas de `sellos_l0.json`.",
        f"- **Sello previo (L0).** Semilla `{s['sorteo']['semilla']}`, fijada por la firma; sorteo a las "
        f"{s['sorteo']['hora']}, antes de abrir una ficha (la hora de las fichas, posterior, está en "
        "`fichas_l1_cabecera.json`); sha256 de la muestra "
        f"`{s['sorteo']['sha256_muestra'][:8]}…`; 30 unidades por estrato, por muestreo simple dentro de cada uno.",
        "- **Dos lecturas y adjudicación.** Primera lectura, de la instancia, sobre las 60 fichas (`veredictos_l1.jsonl`); "
        "segunda, de la mesa, a ciegas sobre las fichas sin veredicto: el mismo veredicto en las 60, sin divergencias "
        "(nota al pie del mandato, `6e611d6`). Las reglas de lectura R1–R4 están en la cabecera de `l1_veredictos.py`. "
        f"Adjudicación de la autora (`adjudicacion_autora_l2.json`, sha256 `{shas['adjudicacion_autora_l2.json'][:8]}…`): "
        f"«{adj['texto_de_la_adjudicacion']}»",
        "- **Criterio** (§1, el del punto 1 de T4): una unidad tiene error si al menos un nodo o una relación de la "
        "extracción no se sostiene en el texto de la unidad (propio o heredado); las omisiones no cuentan. **Alcance "
        "fijado** (decisión 1 de la nota al pie): tres cifras, (i) la tasa de la unidad con ese criterio, (ii) aparte, las "
        "`remite_a` por cita y destino, (iii) los tipos documentales mal asignados, como observación.",
        f"- **Estimadores** (§5, escritos antes de leer). Wilson al 95 % con z = {f(Z, 6)} (la fórmula de T4, "
        "`reext_t0/t4/tasas_t4.py:244-249`); ponderado p̂ = W₁·p̂₁ + W₂·p̂₂ con p̂ ± z·√(W₁²·p̂₁(1−p̂₁)/n₁ + W₂²·p̂₂(1−p̂₂)/n₂), "
        "sin corrección por población finita (las fracciones muestrales son "
        f"{f(pond['fraccion_muestral']['item'], 3)} y {f(pond['fraccion_muestral']['no_item'], 3)}); y el conservador por "
        "combinación de los límites de Wilson.", "",
        "## 2. Las tres cifras", "",
        "### (i) Tasa de error por unidad (criterio de T4)", "",
        "| Estrato | N_h | W_h | con error | p̂ | Wilson 95 % |", "|---|--:|--:|--:|--:|---|"]
    for e in ESTRATOS:
        x = est[e]
        L.append(f"| {NOMBRE_ESTRATO[e]} | {miles(x['N_h'])} | {f(x['W_h'], 6)} | {x['k']} de {x['n']} | {f(x['p'])} | "
                 f"{ls(x['wilson95'])} |")
    L += ["",
          f"- **Ponderado, la tasa del grafo:** p̂ = {f(pond['p'])} ± {f(pond['medio'])}, es decir {ls(pond['intervalo95'])} "
          f"(con 1,96, el redondeo que escribe el mandato: {ls(pond['intervalo95_con_1_96'])}).",
          f"- **Conservador** (W₁·LI₁ + W₂·LI₂; W₁·LS₁ + W₂·LS₂): {ls(pond['conservador95'])}. Ningún estrato dio 0 ni 30 de "
          "30, así que el intervalo ponderado no colapsa; las dos cifras van, con la ponderada como la tasa del grafo.",
          f"- **Comparación con la cola** (T4 de U-REEXT-T0, `{cola['fuente']}`): {cola['k']} de {cola['n']} con error, Wilson "
          f"{ls(cola['wilson95'])}. Mismo criterio y misma fórmula; poblaciones distintas (las 74 de la cola frente a las "
          f"{miles(N)} aceptadas), así que es una comparación descriptiva, no una prueba. "
          + "; ".join(f"{nombre}: {ls(iv)}, {'se superpone con' if iv[1] >= cola['wilson95'][0] else 'queda por debajo de'} "
                      "el de la cola"
                      for nombre, iv in (("Ítems", est["item"]["wilson95"]), ("no ítems", est["no_item"]["wilson95"]),
                                         ("ponderado", pond["intervalo95"]), ("conservador", pond["conservador95"])))
          + f". El p̂ ponderado ({f(pond['p'])}) queda "
          + ("por debajo" if pond["p"] < cola["wilson95"][0] else "dentro o por encima")
          + f" del límite inferior de la cola ({f(cola['wilson95'][0])}).", "",
          "### (ii) Las `remite_a`, por cita y destino", ""]
    t = rem["total"]
    L += [f"- {t['no_sostenidas']} de {t['aristas']} aristas no sostenidas, en {t['unidades']} unidades (ítems: "
          f"{rem['por_estrato']['item']['aristas']} aristas en {rem['por_estrato']['item']['unidades']} unidades; no ítems: "
          f"{rem['por_estrato']['no_item']['aristas']} en {rem['por_estrato']['no_item']['unidades']}). Wilson al 95 %: por "
          f"aristas {ls(t['wilson95_aristas'])}; por unidades ({t['unidades_con_alguna_no_sostenida']} de {t['unidades']}) "
          f"{ls(t['wilson95_unidades'])}.",
          f"- {t['nota'][0].upper()}{t['nota'][1:]} Se juzga si la cita está en el texto de la unidad y si el destino es el "
          "punto citado; la atribución del origen (D1) y el reparto a los nodos del destino son de diseño (`docs/plan_remite_a.md`).",
          "", "### (iii) Tipos documentales mal asignados (observación, no error)", ""]
    L.append(f"- {doc['nodos']} nodos `Comunicacion` en {len(doc['unidades'])} unidades: "
             + "; ".join(f"`{d['id']}` {d['ref']} «{d['label']}» ({d['clase']}{', código ' + d['codigo'] if d['codigo'] else ''})"
                         for d in doc["detalle"]) + ".")
    L += ["", "## 3. Las 10 unidades con error", "",
          "| n | Unidad | Estrato | Estado | Elemento no sostenido | Clase |", "|--:|---|---|---|---|---|"]
    for x in o["con_error"]:
        L.append(f"| {x['n']} | `{x['id']}` | {NOMBRE_ESTRATO[x['estrato']]} | `{x['estado']}` | "
                 + ", ".join(f"{y['ref']} ({y['elemento']})" for y in x["elementos"]) + " | "
                 + "; ".join(sorted({y['clase'] for y in x["elementos"]})) + " |")
    L += ["", "Por qué no se sostiene cada elemento (A1 de `ext::3.17.3.4`, de la segunda lectura, por la decisión 2; los demás, "
          "de la primera, confirmados):", ""]
    for x in o["con_error"]:
        for y in x["elementos"]:
            L.append(f"- `{x['id']}` {y['ref']}: {y['por_que']}.")
    L += ["", "Por clase: " + "; ".join(f"{c}, {pl(k, 'elemento')} en {pl(o['unidades_por_clase'][c], 'unidad', 'unidades')}"
                                       for c, k in sorted(o["elementos_por_clase"].items(), key=lambda z: -z[1]))
          + ". Una unidad puede tener elementos de más de una clase (`ext::7.3.11`).", "",
          "## 4. Descriptivo por estado y por TO (sin inferencia)", "",
          "| Estado | ítems | no ítems | los dos |", "|---|--:|--:|--:|"]
    pe = o["descriptivo"]["por_estado"]
    for g in sorted(pe["ambos"]):
        L.append(f"| `{g}` | " + " | ".join(f"{pe[e][g]['con_error']} de {pe[e][g]['de']}" if g in pe[e] else "—"
                                             for e in ESTRATOS + ("ambos",)) + " |")
    pt = o["descriptivo"]["por_to"]
    L += ["", "| TO | ítems | no ítems | los dos |", "|---|--:|--:|--:|"]
    for g in sorted(pt["ambos"], key=lambda z: (-pt["ambos"][z]["de"], z)):
        L.append(f"| `{g}` | " + " | ".join(f"{pt[e][g]['con_error']} de {pt[e][g]['de']}" if g in pt[e] else "—"
                                             for e in ESTRATOS + ("ambos",)) + " |")
    L += ["", "Las cuentas por estado y por TO no se ponderan ni llevan intervalo: las celdas son chicas y el sorteo no se "
          "estratificó por ellas.", "",
          "## 5. Omisiones, dudas y observaciones", "",
          f"- **Omisiones, aparte** (no cuentan como error; las registró la primera lectura, sin adjudicar): en "
          f"{o['omisiones_aparte']['item']} de 30 ítems y {o['omisiones_aparte']['no_item']} de 30 no ítems. "
          f"{sum(len(v) for v in o['sin_nodos_de_contenido'].values())} unidades no aportan ningún nodo de contenido: "
          + ", ".join(f"`{i}`" for e in ESTRATOS for i in o["sin_nodos_de_contenido"][e])
          + " (bloques de apertura de lista y renglones de datos).",
          f"- **Dudas, como observaciones** (adjudicación): {len(o['observaciones_por_dudas'])} unidades; no cambian ningún "
          "veredicto."]
    for d in o["observaciones_por_dudas"]:
        L.append(f"  - `{d['id']}`: {d['observacion']}.")
    L += ["- Las demás observaciones de la primera lectura (tipos cercanos, lecturas laxas, menciones no literales) están "
          "por unidad en el campo `observaciones` de `veredictos_l1.jsonl`.", "",
          "## 6. Solapamiento con T4", "",
          f"{len(o['solapamiento_t4'])} de las 60 unidades ya se habían leído en T4 de U-REEXT-T0 (no se excluyen, §3): "
          + "; ".join(f"`{x['id']}` ({' y '.join(PUNTO_T4[p] for p in x['puntos_t4'])}; {x['marca'].replace('_', ' ')})"
                      for x in o["solapamiento_t4"])
          + ". En el punto 3 de T4 se leyó la copia de la nota de E3, en el 6 las listas y en el 8 las omisiones, no la "
          "unidad entera con el criterio de este reporte.", "",
          "## 7. Declaración sobre `cla::1.2.1`", "",
          "Antes del sello, para conocer el formato, la instancia abrió el chunk de E0 de `cla::1.2.1` (encabezados y 200 "
          "caracteres del texto), y esa unidad salió en la muestra (no ítems, 4 del sorteo). La semilla la fija la firma y el "
          "sorteo no depende de lo que se mire, así que la unidad no se reemplaza (decisión 3). Las dos lecturas la dan "
          f"**{o['cla_1_2_1']['marca'].replace('_', ' ')}**: la primera, la de la instancia, y la segunda, la de la mesa a "
          "ciegas, coinciden.", "",
          "## 8. Vigilancia por tanda (para el pre-registro de la tanda 1; no se edita aquí)", "",
          "- **Muestra:** 60 unidades aceptadas por tanda, en dos estratos (ítems y no ítems, por `prompt_r2b.es_item`), 30 "
          "por estrato (decisión 2 al firmar), con el mismo método de sorteo (`random.Random(f\"{semilla}:{estrato}\")"
          ".sample(sorted(ids), 30)`, con la semilla sellada antes de leer; la fija el pre-registro) y el mismo criterio "
          "(§1, con el alcance de la decisión 1 de la nota al pie).",
          "- **Las tres cifras por tanda:** (i) la tasa por unidad, por estrato con Wilson y ponderada con los pesos de la "
          "tanda (y el conservador); (ii) las `remite_a` no sostenidas por cita y destino, por aristas y por unidades; (iii) "
          "los tipos documentales mal asignados, contados como observación.",
          "- **Umbral de atención:** el límite inferior de Wilson de la tanda por encima del límite superior de la tanda 0, "
          f"por estrato y ponderado. Con la tanda 0: ítems, LI de la tanda > {f(o['vigilancia']['item']['LS_tanda0'])} (con "
          f"30 unidades, desde {o['vigilancia']['item']['k_minimo_de_30_que_dispara']} con error); no ítems, LI > "
          f"{f(o['vigilancia']['no_item']['LS_tanda0'])} (desde {o['vigilancia']['no_item']['k_minimo_de_30_que_dispara']} "
          f"de 30); ponderado, con el intervalo conservador, LI conservador de la tanda > "
          f"{f(o['vigilancia']['ponderado']['LS_conservador_tanda0'])} (el conservador es el intervalo ponderado hecho con "
          "límites de Wilson; si el pre-registro prefiere el intervalo ponderado del §5, el límite superior de la tanda 0 "
          f"es {f(pond['intervalo95'][1])}).", "",
          "## 9. Reproducción", "",
          "Desde la raíz de una copia del repo sin enlaces (CLAUDE.md §4.l), con las salidas en `lectura_aceptadas/`:", "",
          "```bash",
          "PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/lectura_aceptadas/l2_estimadores.py "
          "--sellos data/experiment/lectura_aceptadas/sellos_l0.json "
          "--veredictos data/experiment/lectura_aceptadas/veredictos_l1.jsonl "
          "--fichas data/experiment/lectura_aceptadas/fichas_l1.jsonl "
          "--adjudicacion data/experiment/lectura_aceptadas/adjudicacion_autora_l2.json "
          f"--adjudicacion-sha256 {shas['adjudicacion_autora_l2.json']} "
          "--tasas-t4 data/experiment/reext_t0/t4/salida/tasas_t4.json --salida <directorio>",
          "```", "",
          "Insumos (sha256): " + "; ".join(f"`{n}` `{h[:16]}…`" for n, h in shas.items())
          + f". Script: `{o['l2_estimadores.py_sha256'][:16]}…`."]
    (salida / "reporte_l2.md").write_text("\n".join(L) + "\n", encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
