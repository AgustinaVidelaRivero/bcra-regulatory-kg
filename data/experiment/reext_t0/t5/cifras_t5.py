"""U-REEXT-T0, T5 (USD 0, sin red): las cifras del reporte, cada una recomputada contra su archivo (CLAUDE.md §4.i).
Lee archivos commiteados de la corrida y de las etapas, y las salidas de los comandos de t5/comandos_t5.sh (--gate),
que corren sobre una copia del repo. Escribe solo --out (JSON) y --md. Corre desde la raíz de una COPIA del repo.

Bloques (los del mandato, sección T5):
  1. costos (contadores de T2, estado y presupuesto de la corrida), gate de T3-bis (shapes y suite re-corridas sobre la
     copia), columna «r2b» del tablero (celdas y derivación), controles de T3 y reparación acotada;
  2. lo que P4b dejó sin mejorar (tasas de T4, con la adjudicación por supuesto de la nota del 06/10/2026, c9d4c40;
     omisiones de T2);
  3. variación del modelo (P5, punto 5.b de T4, y los pedidos de E3 de la corrida en su base de caché);
  5. claves de la caché (salida del selftest con --salida-r2b);
  6. la cola humana: lo que sale del grafo evaluado (nodos con toda la procedencia en la cola, aristas que los tocan,
     derivadas, compartidos), anclas de las 15 preguntas, ejemplo de la tesis y la simulación sin la cola.

Uso: python -B data/experiment/reext_t0/t5/cifras_t5.py --gate DIR --out J --md M
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sqlite3
from collections import Counter, OrderedDict
from math import sqrt
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[4]
X = RAIZ / "data" / "experiment"
SAL = X / "reextraccion_v2" / "corpus_tanda0" / "salida_r2b"
ENS = X / "reextraccion_v2" / "corpus_tanda0"
T0 = X / "reext_t0"
TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
Z = 1.959964
N_UNIDADES = 2439
# gasto de las corridas de reparación, de sus frenos (commiteados): T2-bis en 4ab7a0a, T2-ter en ad99ac7
GASTO_T2BIS, GASTO_T2TER = 0.49291, 0.249002
INICIO_CORRIDA = "2026-10-05T14:38"  # hora local de inicio de T2 (freno_t2.md, 3d793aa); created_at de la base es local
SHA = {"diez": "a9631a64b422bdae634fb05135373c6f04c6272cdf7acd43a1be9f5b6c1f5f57",
       "desarrollo": "6e7560433148cfe0c476cdd61199c32278187c4196d6f90dc0a38976a6d8e9a2"}
NOMBRE = {"diez": "KG-Tanda0-Diez-r2b", "desarrollo": "KG-Tanda0-Desarrollo-r2b"}


def leer(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def wilson(k: int, n: int) -> list[float]:
    p = k / n
    d = 1 + Z * Z / n
    c = (p + Z * Z / (2 * n)) / d
    h = Z * sqrt(p * (1 - p) / n + Z * Z / (4 * n * n)) / d
    return [round(max(0.0, c - h), 4), round(min(1.0, c + h), 4)]


def tasa(k: int, n: int) -> OrderedDict:
    return OrderedDict([("fraccion", f"{k}/{n}"), ("wilson95", wilson(k, n))])


# ------------------------------------------------------------------------------------------------------- bloque 1
def costos() -> OrderedDict:
    c = leer(T0 / "salida" / "contadores_t2.json")["b_gasto"]
    cl = c["clientes"]
    verif = sum(x["e3"]["gasto_usd_real"] for x in cl.values())
    reint = sum(x["e1_reintentos"]["gasto_usd_real"] for x in cl.values())
    fases = leer(SAL / "estado_corpus.json")["fases_cerradas"]
    e1f = sum(v["gasto_usd"] for k, v in fases.items() if k.endswith(":e1"))
    e3f = sum(v["gasto_usd"] for k, v in fases.items() if k.endswith(":e3"))
    pres = leer(SAL / "presupuesto_compartido.json")
    t2 = c["presupuesto_compartido"]["gasto_usd"]
    assert abs(pres["gasto_usd"] - (t2 + GASTO_T2BIS + GASTO_T2TER)) < 1e-6, "el presupuesto no cierra con T2 + T2-bis + T2-ter"
    return OrderedDict([
        ("t2", OrderedDict([("e1_usd", c["total_e1_usd"]), ("e3_usd", c["total_e3_usd"]),
                            ("e3_verificacion_usd", round(verif, 4)), ("e3_reintentos_e1_ratchet_usd", round(reint, 4)),
                            ("total_usd", c["total_usd"]), ("presupuesto_al_cierre_de_t2_usd", t2)])),
        ("t2bis_usd", GASTO_T2BIS), ("t2ter_usd", GASTO_T2TER),
        ("t1_t3_t3bis_t4_t5_usd", 0),
        ("total_unidad_usd", pres["gasto_usd"]), ("tope_usd", pres["tope_usd"]),
        ("fases_cerradas_al_cierre", OrderedDict([("e1_usd", round(e1f, 6)), ("e3_usd", round(e3f, 6)),
                                                  ("suma_usd", round(e1f + e3f, 6))])),
        ("tarifa_por_unidad_t2", OrderedDict([
            ("unidades", N_UNIDADES), ("e1", round(c["total_e1_usd"] / N_UNIDADES, 6)),
            ("e3", round(c["total_e3_usd"] / N_UNIDADES, 6)), ("e3_verificacion", round(verif / N_UNIDADES, 6)),
            ("e3_reintentos_e1_ratchet", round(reint / N_UNIDADES, 6)),
            ("e1_y_e3", round(c["total_usd"] / N_UNIDADES, 6))]))])


def gate(g: Path) -> OrderedDict:
    fx = leer(RAIZ / "scripts" / "regression_kg_esperado.json")["estado_esperado"]
    out = OrderedDict()
    for k in ("diez", "desarrollo"):
        con = (g / f"consola_shapes_{k}.txt").read_text(encoding="utf-8")
        bloq = [x for x in con.splitlines() if x.startswith("bloqueante")]
        s = leer(g / f"suite_{k}_r2b.json")
        entrada = fx[NOMBRE[k]]
        mapa = entrada.get("items") or entrada.get("estados")
        esp = {i: (v.get("estado") if isinstance(v, dict) else v) for i, v in mapa.items()}
        obs = {i["id"]: i["estado"] for i in s["items"]}
        no_ver = sorted(i for i, e in esp.items() if e is None)
        coinc = sorted(i for i, e in esp.items() if e is not None and obs.get(i) == e)
        regr = sorted(i for i, e in esp.items() if e is not None and obs.get(i) != e)
        assert s["parametros"]["kg_sha256"] == SHA[k]
        out[k] = OrderedDict([
            ("shapes_veredicto", re.search(r"VEREDICTO GLOBAL: (\S+( \S+)?)", con).group(1)),
            ("shapes_bloqueantes", f"{sum(' PASS ' in x for x in bloq)}/{len(bloq)} en PASS"),
            ("suite_items", len(obs)), ("suite_resumen", s["resumen"]),
            ("suite_regresion", {kk: s["regresion"][kk] for kk in ("fixture_sha256", "entrada", "n_regresiones",
                                                                   "coinciden", "no_verificadas")}),
            ("recomputado_contra_la_fixture", OrderedDict([("items_con_estado", len(esp)),
                                                           ("no_verificadas", len(no_ver)), ("coinciden", len(coinc)),
                                                           ("regresiones", regr)]))])
        assert len(regr) == s["regresion"]["n_regresiones"] and len(coinc) == s["regresion"]["coinciden"]
    return out


def tablero(g: Path) -> OrderedDict:
    filas = (RAIZ / "docs" / "tablero_correcciones.md").read_text(encoding="utf-8").splitlines()
    cab = next(i for i, x in enumerate(filas) if "Después de r2: r2b" in x)
    cols = [c.strip() for c in filas[cab].split("|")]
    j = next(i for i, c in enumerate(cols) if c.startswith("Después de r2: r2b"))
    celdas = []
    for x in filas[cab + 2:]:
        if not x.startswith("|"):
            break
        c = [y.strip() for y in x.split("|")]
        celdas.append((c[1][:60], c[j]))
    llenas = [c for c in celdas if c[1] and c[1] not in ("—", "-")]
    escritas = int(re.search(r"celdas escritas: (\d+)", (g / "consola_tablero.txt").read_text(encoding="utf-8")).group(1))
    return OrderedDict([("filas", len(celdas)), ("celdas_con_valor", len(llenas)),
                        ("celdas_que_escribe_la_derivacion", escritas),
                        ("no_medible_en_r2b_sin_tocar", sum(c[1].startswith("No medible en r2b") for c in celdas)),
                        ("no_medible_escritas_por_t3bis", sum(c[1].startswith("No medible en T3") for c in celdas)),
                        ("derivacion", (g / "cmp_tablero.txt").read_text(encoding="utf-8").strip()),
                        ("controles_t3", (g / "cmp_controles.txt").read_text(encoding="utf-8").strip())])


# ------------------------------------------------------------------------------------------------------- bloque 2
def p4b_sin_mejorar() -> OrderedDict:
    t = leer(T0 / "t4" / "salida" / "tasas_t4.json")
    sup = t["punto_7"]["por_supuesto"]["supuestos"]
    # adjudicación de la nota del 06/10/2026 (c9d4c40): «emisoras no financieras» de ext::4.1.3.2 va dentro de una norma
    cambios = 0
    for s in sup:
        if s["chunk_id"] == "ext::4.1.3.2" and s["fragmento_fase_a"] == "emisoras no financieras":
            assert s["clase"] == "omitido"
            s["clase"] = "dentro_de_norma"
            cambios += 1
    assert cambios == 1
    n = len(sup)
    cuenta = Counter(s["clase"] for s in sup)
    p8 = t["punto_8"]
    h = leer(T0 / "salida" / "contadores_t2.json")["h_omisiones_meta_normativo"]
    return OrderedDict([
        ("listas", {k: v["fraccion"] for k, v in t["punto_6"]["por_tipo_y_rol"].items()}),
        ("listas_encabezados_b1_con_forma_b2", t["punto_6"]["encabezados_b1_con_forma_de_b2"]["si_las_dos_listas_fueran_b2"]),
        ("condicion_por_supuesto_criterio_sellado", t["punto_7"]["criterio_sellado"]["cumple"]),
        ("por_supuesto_adjudicado", OrderedDict((c, tasa(cuenta[c], n)) for c in
                                                ("condicion_con_relacion", "dentro_de_norma", "fusionado", "omitido",
                                                 "sin_relacion"))),
        ("unidades_con_un_supuesto_dentro_de_una_norma",
         len({s["chunk_id"] for s in sup if s["clase"] == "dentro_de_norma"})),
        ("omisiones_t2", h["total"]),
        ("omisiones_t4", OrderedDict((g, OrderedDict([
            ("normativas_con_remisiones", p8[g]["normativas_con_remisiones"]["fraccion"]),
            ("normativas_sin_remisiones", p8[g]["normativas_sin_remisiones"]["fraccion"]),
            ("habilitantes", p8[g]["habilitantes"]["fraccion"]), ("tramo_heredado", p8[g]["tramo_heredado"]),
            ("estimacion_tramo_propio", p8[g]["estimacion_universo_tramo_propio"]),
            ("estimacion_tramo_heredado", p8[g]["estimacion_universo_tramo_heredado"])])) for g in ("sin_marca", "con_marca")))])


# ------------------------------------------------------------------------------------------------------- bloque 3
def variacion() -> OrderedDict:
    a = leer(X / "prompt_r2" / "p5" / "salida" / "analisis_p5.json")
    f5 = leer(T0 / "t4" / "salida" / "fichas_punto5_p4b.json")["resumen"]
    con = sqlite3.connect(f"file:{X / 'reextraccion_v2' / 'e3_verificador' / 'cache' / 'e3_verificacion.db'}?mode=ro&immutable=1",
                          uri=True)
    filas = con.execute("select request_json from cache where created_at >= ?", (INICIO_CORRIDA,)).fetchall()
    req = Counter(hashlib.sha256(r[0].encode("utf-8")).hexdigest() for r in filas)
    temp = Counter("temperature" in json.loads(r[0]) for r in filas)
    acc = con.execute("select count(*), coalesce(sum(hit), 0) from access_log where ts >= ?", (INICIO_CORRIDA,)).fetchone()
    ver = Counter()
    for to in TOS:
        for x in (SAL / to / "veredictos.jsonl").read_text(encoding="utf-8").splitlines():
            if x.strip():
                ver[json.loads(x)["chunk_id"]] += 1
    b = a["medicion_b"]["a_contra_b"]
    return OrderedDict([
        ("p5_e1_a_contra_b", f"{b['iguales_byte_a_byte']}/{b['de']} iguales byte a byte"),
        ("p5_e3", a["medicion_f_e3"]["resumen"]),
        ("t4_punto_5b", OrderedDict([("identicas_a_alguna_de_p5", f5["identicas_a_alguna_de_p5"]),
                                     ("difieren", 27 - f5["identicas_a_alguna_de_p5"]),
                                     ("cambia_contra_a", len(f5["cambia_la_marca_contra_a"])),
                                     ("cambia_contra_b", len(f5["cambia_la_marca_contra_b"]))])),
        ("e3_corrida", OrderedDict([("pedidos", len(filas)), ("pedidos_distintos", len(req)),
                                    ("pedidos_repetidos", sum(1 for v in req.values() if v > 1)),
                                    ("con_temperatura_en_el_pedido", temp.get(True, 0)),
                                    ("accesos_y_aciertos_de_cache", list(acc)),
                                    ("veredictos", sum(ver.values())), ("unidades", len(ver)),
                                    ("unidades_con_dos_veredictos", sum(1 for v in ver.values() if v == 2)),
                                    ("unidades_con_veredictos_distintos_para_el_mismo_pedido", 0 if all(v == 1 for v in req.values()) else None)]))])


# ------------------------------------------------------------------------------------------------------- bloque 5
def claves(g: Path) -> OrderedDict:
    s = leer(g / "selftest_clave_cache_t5.json")   # la corrida de comandos_t5.sh con --salida-r2b, no la del repo
    assert s == leer(X / "mantenimiento" / "selftest_clave_cache.json"), "la salida del repo no es la de esta corrida"
    a = s["perfil_r2b"]["anclaje"]
    return OrderedDict([("veredicto", s["veredicto"]), ("e1", a["e1"]), ("e3", a["e3"]),
                        ("claves_db_e1_namespace_r2b", a["claves_db_e1_en_namespace_r2b"]),
                        ("claves_db_e1_rforma1", a["claves_db_e1_en_namespace_reintento_forma"]),
                        ("claves_db_e1_rforma2", a.get("claves_db_e1_en_namespace_segundo_reintento_forma"))])


# ------------------------------------------------------------------------------------------------------- bloque 6
def cola(g: Path) -> OrderedDict:
    kgp = ENS / "ens_diez_r2b" / "r2" / "kg.json"
    assert sha(kgp) == SHA["diez"]
    kg = leer(kgp)
    s = leer(T0 / "t4" / "salida" / "sorteos_t4.json")["punto_1_cola_humana"]
    cola_ids = {m["chunk_id"] for m in s["muestra_en_orden_del_sorteo"]} | set(s["fuera_de_la_muestra"])
    assert len(cola_ids) == 74

    def ch(x):
        return [p.get("chunk_id") for p in (x.get("provenances") or [x.get("provenance") or {}])]
    fuera = {x["id"] for x in kg["nodes"] if ch(x) and all(c in cola_ids for c in ch(x))}
    comp = sorted(x["id"] for x in kg["nodes"] if x["id"] not in fuera and any(c in cola_ids for c in ch(x)))
    toc = [x for x in kg["edges"] if x["source"] in fuera or x["target"] in fuera]
    marca = [x for x in toc if (x.get("properties") or {}).get("cola_humana")]
    deriv = [x for x in toc if not (x.get("properties") or {}).get("cola_humana")]
    p1 = [x for x in kg["nodes"] if ch(x) and all(c == "cap::4.2.1.2::parte1" for c in ch(x))]
    t = leer(T0 / "t4" / "salida" / "tasas_t4.json")["punto_1"]
    q = leer(T0 / "t4" / "salida" / "preguntas_r2b.json")["preguntas"]

    def ancla(a):
        return None if not a else re.sub(r" y sub-puntos$", "", a).replace("::S", "::")

    def bajo(c, a):
        to, p = a.split("::")
        cto, cp = c.split("::", 1)
        return cto == to and (cp == p or cp.startswith(p + ".") or cp.startswith(p + "::"))
    bajo_ancla = {p["n"]: sorted(c for c in cola_ids if ancla(p["ancla"]) and bajo(c, ancla(p["ancla"]))) for p in q}
    sim = leer(g / "preguntas_sin_cola_simulado.json")["preguntas"]
    antes = {p["n"]: p["resultado"] for p in q}
    return OrderedDict([
        ("muestra", OrderedDict([("con_error", t["con_error"]), ("regla_se_dispara", t["regla_se_dispara"])])),
        ("unidades_de_la_cola", len(cola_ids)),
        ("nodos_que_salen", len(fuera)), ("nodos", len(kg["nodes"])),
        ("nodos_compartidos_que_se_quedan", len(comp)), ("compartidos", comp),
        ("aristas_que_salen", len(toc)), ("aristas", len(kg["edges"])),
        ("aristas_que_salen_por_relacion", dict(Counter(x["relation"] for x in toc).most_common())),
        ("aristas_con_marca_de_cola", len(marca)),
        ("aristas_derivadas_sin_marca", dict(Counter(x["relation"] for x in deriv).most_common())),
        ("parte1_entidades", len(p1)), ("parte1_toda_sale", all(x["id"] in fuera for x in p1)),
        ("unidades_de_la_cola_bajo_un_ancla", {k: v for k, v in bajo_ancla.items() if v}),
        ("ejemplo_de_la_tesis_en_la_cola", sorted(c for c in cola_ids if c.startswith("cla::5.1.1") or c.startswith("cla::3.7"))),
        ("simulacion_sin_cola", OrderedDict([("nodos", len(kg["nodes"]) - len(fuera)),
                                             ("aristas", len(kg["edges"]) - len(toc)),
                                             ("preguntas_que_cambian", {p["n"]: (antes[p["n"]], p["resultado"])
                                                                        for p in sim if p["resultado"] != antes[p["n"]]})]))])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--gate", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--md", type=Path, required=True)
    a = ap.parse_args()
    leidos = ["consola_shapes_diez.txt", "consola_shapes_desarrollo.txt", "suite_diez_r2b.json", "suite_desarrollo_r2b.json",
              "cifra_reparacion_t5.json", "preguntas_sin_cola_simulado.json", "selftest_clave_cache_t5.json",
              "consola_tablero.txt", "cmp_tablero.txt", "cmp_controles.txt"]
    insumos = {n: sha(a.gate / n) for n in leidos}
    res = OrderedDict([("unidad", "U-REEXT-T0, T5: cifras del reporte, recomputadas"),
                       ("insumos_gate_sha256", insumos),
                       ("bloque_1", OrderedDict([("costos", costos()), ("gate", gate(a.gate)), ("tablero_r2b", tablero(a.gate)),
                                                 ("reparacion", leer(a.gate / "cifra_reparacion_t5.json")["final"])])),
                       ("bloque_2", p4b_sin_mejorar()), ("bloque_3", variacion()), ("bloque_5", claves(a.gate)),
                       ("bloque_6", cola(a.gate))])
    a.out.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    c, gt = res["bloque_1"]["costos"], res["bloque_1"]["gate"]
    md = ["# Anexo de cifras de T5 de U-REEXT-T0", "",
          "Cada cifra sale de `t5/cifras_t5.py` sobre una copia del repo y de las salidas de `t5/comandos_t5.sh`; el JSON "
          "completo es `anexo_cifras_t5.json`.", "",
          f"- Gasto: T2 {c['t2']['total_usd']} (E1 {c['t2']['e1_usd']}, E3 {c['t2']['e3_usd']}), T2-bis {c['t2bis_usd']}, "
          f"T2-ter {c['t2ter_usd']}; total {c['total_unidad_usd']} de {c['tope_usd']}. Tarifa por unidad (T2): "
          f"{dict(c['tarifa_por_unidad_t2'])}.",
          f"- Gate: {json.dumps({k: [v['shapes_veredicto'], v['shapes_bloqueantes'], v['recomputado_contra_la_fixture']] for k, v in gt.items()}, ensure_ascii=False)}.",
          f"- Tablero: {dict(res['bloque_1']['tablero_r2b'])}. Reparación: {json.dumps(res['bloque_1']['reparacion'], ensure_ascii=False)}.",
          f"- P4b sin mejorar: {json.dumps(res['bloque_2'], ensure_ascii=False)}.",
          f"- Variación: {json.dumps(res['bloque_3'], ensure_ascii=False)}.",
          f"- Claves: {json.dumps(res['bloque_5'], ensure_ascii=False)}.",
          f"- Cola: {json.dumps({k: v for k, v in res['bloque_6'].items() if k != 'compartidos'}, ensure_ascii=False)}."]
    a.md.write_text("\n".join(md) + "\n", encoding="utf-8")
    print(json.dumps({"total": c["total_unidad_usd"], "cola": [res["bloque_6"]["nodos_que_salen"], res["bloque_6"]["aristas_que_salen"]]},
                     ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
