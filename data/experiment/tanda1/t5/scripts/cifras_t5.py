"""B6.1, tanda 1, T5, puntos 3 a 7: las cifras del reporte de cierre, por script, desde lo commiteado de T1 a T4 y de la corrida. USD 0,
sin API y sin red. Corre sobre una copia del repo (<raíz>) y no re-corre la extracción, el ensamblado ni el gate. Salida determinística,
sin horas: dos corridas a dos <salidas> distintas dan los mismos bytes.

  1. El costo (pre-registro firmado, §3, «Al cerrar»):
       - el real, por etapa y por TO: `gasto_usd` de cada fase de `estado_corpus.json` (40 fases, las dos de cada TO), contra
         `presupuesto_compartido.json`. Lo calcula el runner con la fórmula de caching (decisión 2 de docs/decisiones_caching_extraccion.md;
         cliente_e1.py:328-331, cliente_e3.py:194-197; precios en runner_corpus.py:91-96). De cada fase se leen solo `gasto_usd` y
         `resumen.n`: el resumen de E3 trae además el desglose por estado, que no se lee (cegamiento de U-MED-VERIF). E3 es una sola cifra
         por TO, con los reintentos adentro;
       - el estimado: por TO, el del manifiesto 818a62cf… (`limites.estimado_usd`, repartido por caracteres de E0; nota al pie del
         pre-registro, ca5b39fd); por etapa, U del TO por la tarifa de cada una (E1 0,010135 y E3 0,010980), con las líneas de alcance en
         E1 (§1.4) repartidas por TO como las repartió T1 (t1/t1_manifiesto.py:124-129, desde alcance_e1/a2/salidas/medicion_tanda1_a2.json,
         `usd_agregados`); el total, 69,6592;
       - la desviación por etapa, por TO y total; la tarifa observada por unidad (U = 3.290), como propuesta para el §5 de la tabla de
         reprocesamiento; y la cadena `para_el_preregistro_tanda_final`.
  2. Los ids de modelo que devolvió la API (§2 y §5.6): están solo en las bases de la caché del runner (ignoradas por git). Se copian, con
     sus -wal y -shm, a <trabajo>, como lo hace t2/freno_modelo_t2.py, y se consulta `cache.model` por `access_log.run_label`
     (corpus_<TO>_e1, corpus_<TO>_reintentos_e1 y corpus_<TO>_e3, de los 20 TOs). De E1 va la cuenta de respuestas distintas por id; las
     de E3 y de los reintentos de E1 de la fase de E3 cuentan los reintentos y van solo a <trabajo>/NO_ABRIR_parte_modelos_t5.json, que
     el script no imprime. Contra el código (runner_corpus.py:91 y :94), el §2 y lo que dio el freno por modelo de T2 (avance_t2.jsonl).
  3. Los volúmenes: unidades, aceptadas (los tres estados juntos) y cola, de t2/resumen_t2.json; nodos y aristas de los cuatro grafos, de
     t3/salidas/doble_corrida_t3.json.
  4. El alcance y el catálogo al cierre (§5.5), desde lo que contó T3 (t3/conteos_sin_leer/contado_sin_leer_t3f.json): las claves sobre el
     umbral de 2 unidades distintas (solo cuántas: las claves son menciones de unidades que no están todas a la vista), y lo que resolvió
     la única versión del catálogo. El derivado del alcance que leyó E1, contra el sello del manifiesto.
  5. Los hallazgos en los ejes A y B (§5.6; protocolo entre tandas, :71-100), las propuestas del backlog y la columna «Tanda 1» del
     tablero, con la regla de cada fila escrita abajo (REGLA_FILAS). La causa de un hallazgo de lectura sale de la nota de la autora; si
     no la hay, va «causa: no dicha por la lectura». Ningún desglose por estado de E3 ni por reintentos. Solo se muestran unidades de
     t3/muestras/unidades_a_la_vista_T4.json, y el script lo controla.
Uso: python3 -I -B cifras_t5.py <raíz> <trabajo> <salidas>
"""
import csv
import hashlib
import json
import re
import shutil
import sqlite3
import sys
from decimal import ROUND_HALF_UP, Decimal as D
from pathlib import Path

sys.dont_write_bytecode = True
RAIZ, TRABAJO, SAL = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve(), Path(sys.argv[3]).resolve()
assert not SAL.exists() and not TRABAJO.exists(), "las salidas y el trabajo tienen que ser nuevos"
SAL.mkdir(parents=True)
TRABAJO.mkdir(parents=True)
X = RAIZ / "data/experiment/reextraccion_v2"
T1 = RAIZ / "data/experiment/tanda1"
CORRIDA = X / "corpus_tanda1/salida_r2b"
MAN = X / "manifiestos/tanda1_20tos_r2b.json"
MAN_SHA = "818a62cfde403a453d0551916022f928f7cd9cb62d7947801eadb587f2385d9d"
DERIVADO_SHA = "e06933e77a1ae819229d5f2a4b5886f71f6129c809032e1e557932fb8cb69ff4"
TARIFA = {"e1": D("0.010135"), "e3": D("0.010980")}
ESTIMADO_TOTAL = D("69.6592")
ID_E1, ID_E3_CODIGO = "claude-haiku-4-5-20251001", "claude-sonnet-5"
BASES = {"e1": "e1_extractor/cache/e1_extraccion.db", "e1_reintentos": "e3_verificador/cache/e1_reintentos.db",
         "e3": "e3_verificador/cache/e3_verificacion.db"}
ETIQUETA = {"e1": "corpus_{}_e1", "e1_reintentos": "corpus_{}_reintentos_e1", "e3": "corpus_{}_e3"}
L = lambda p: json.loads(Path(p).read_text(encoding="utf-8"))  # noqa: E731
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()  # noqa: E731
rel = lambda p: Path(p).resolve().relative_to(RAIZ).as_posix()  # noqa: E731
q6 = lambda x: float(D(x).quantize(D("0.000001"), rounding=ROUND_HALF_UP))  # noqa: E731
q4 = lambda x: float(D(x).quantize(D("0.0001"), rounding=ROUND_HALF_UP))  # noqa: E731
coma = lambda x, k=4: f"{x:.{k}f}".replace(".", ",")  # noqa: E731
consola = []
fuentes = {}


def fuente(p) -> Path:
    p = Path(p)
    fuentes[rel(p)] = sha(p)
    return p


# ------------------------------------------------------------------ 1. el costo
assert sha(MAN) == MAN_SHA, "el manifiesto no es el 818a62cf…"
man = L(fuente(MAN))
orden = man["orden_corrida"]
assert len(orden) == 20
est = L(fuente(CORRIDA / "estado_corpus.json"))
pres = L(fuente(CORRIDA / "presupuesto_compartido.json"))
assert est["fase_actual"] is None and len(est["fases_cerradas"]) == 40
real = {}
n_fase = {}
for to in orden:
    real[to], n_fase[to] = {}, {}
    for e in ("e1", "e3"):
        f = est["fases_cerradas"][f"{to}:{e}"]
        real[to][e] = D(str(f["gasto_usd"]))  # solo gasto_usd y resumen.n: el resumen de E3 trae el desglose por estado
        n_fase[to][e] = f["resumen"]["n"]
lista = {f["to"]: f for f in L(fuente(RAIZ / "data/experiment/segmentacion_oficial_e0r2/s2/lista_tanda1_S2.json"))["filas"]}
U = {to: lista[to]["unidades_extraccion"] for to in orden}
assert sum(U.values()) == 3290
alc = L(fuente(RAIZ / "data/experiment/alcance_e1/a2/salidas/medicion_tanda1_a2.json"))["medicion_tanda1"]
alc_to = {to: D(str(alc["por_documento"][to]["usd_agregados"])) if to in alc["por_documento"] else D(0) for to in orden}
r6 = lambda x: x.quantize(D("0.000001"), rounding=ROUND_HALF_UP)  # noqa: E731
plano = {to: {"e1": r6(U[to] * TARIFA["e1"] + alc_to[to]), "e3": r6(U[to] * TARIFA["e3"])} for to in orden}
mani = {to: {e: D(str(man["limites"]["estimado_usd"][to][e])) for e in ("e1", "e3")} for to in orden}
res_t2 = L(fuente(T1 / "t2/resumen_t2.json"))


def dif(r: D, e: D) -> dict:
    return {"real": q6(r), "estimado": q6(e), "diferencia": q6(r - e), "razon": q4(r / e) if e else None}


por_to = {}
for to in orden:
    rt, mt = real[to]["e1"] + real[to]["e3"], mani[to]["e1"] + mani[to]["e3"]
    por_to[to] = {"unidades": U[to], "lineas_de_alcance_usd": q6(alc_to[to]),
                  "contra_el_manifiesto": {"e1": dif(real[to]["e1"], mani[to]["e1"]), "e3": dif(real[to]["e3"], mani[to]["e3"]),
                                           "total": dif(rt, mt)},
                  "contra_la_tarifa": {"e1": dif(real[to]["e1"], plano[to]["e1"]), "e3": dif(real[to]["e3"], plano[to]["e3"]),
                                       "total": dif(rt, plano[to]["e1"] + plano[to]["e3"])},
                  "unidades_de_las_fases": n_fase[to]}
tot_real = {e: sum(real[to][e] for to in orden) for e in ("e1", "e3")}
tot_mani = {e: sum(mani[to][e] for to in orden) for e in ("e1", "e3")}
tot_plano = {e: sum(plano[to][e] for to in orden) for e in ("e1", "e3")}
total_real = tot_real["e1"] + tot_real["e3"]
assert q4(tot_plano["e1"] + tot_plano["e3"]) == float(ESTIMADO_TOTAL) == q4(tot_mani["e1"] + tot_mani["e3"])
assert q6(total_real) == res_t2["total"]["gasto_por_to_sumado_usd"]
tarifa_obs = {e: tot_real[e] / 3290 for e in ("e1", "e3")}
para = "; ".join(f"{n}: real USD {coma(q4(r))}, estimado USD {coma(q4(e))}, razón {coma(q4(r / e))}" for n, r, e in (
    ("E1", tot_real["e1"], tot_plano["e1"]), ("E3", tot_real["e3"], tot_plano["e3"]),
    ("total", total_real, tot_plano["e1"] + tot_plano["e3"])))
costo = {
    "como": ("el real es el `gasto_usd` de las 40 fases de estado_corpus.json, que el runner calcula con la fórmula de caching (decisión 2 "
             "de docs/decisiones_caching_extraccion.md; data/experiment/reextraccion_v2/e1_extractor/cliente_e1.py:328-331, "
             "e3_verificador/cliente_e3.py:194-197; precios en corpus_v2/runner_corpus.py:91-96); de cada fase se leen solo gasto_usd y "
             "resumen.n. E3 va como una sola cifra por TO, con los reintentos adentro. El estimado por TO es el del manifiesto 818a62cf… "
             "(repartido por caracteres de E0); el estimado por etapa es U × tarifa (E1 0,010135 y E3 0,010980) más las líneas de alcance "
             "en E1, repartidas por TO como en T1 (t1/t1_manifiesto.py:124-129)"),
    "real": {"por_etapa": {e: q6(tot_real[e]) for e in tot_real}, "total": q6(total_real),
             "presupuesto_compartido_gasto_usd": pres["gasto_usd"], "tope_usd": pres["tope_usd"],
             "suma_de_las_fases_menos_presupuesto_compartido": q6(total_real - D(str(pres["gasto_usd"]))),
             "fraccion_del_tope": q4(total_real / D(str(pres["tope_usd"]))),
             "fases_cerradas": len(est["fases_cerradas"]), "fase_actual": est["fase_actual"]},
    "pasos_sin_api_en_0": ["E0 (T1 la generó con el código del gate, dentro del repo)", "la corrida en seco de T1 (clientes stub)",
                           "E2 y el ensamblado de los cuatro grafos (T2 y T3)", "el gate, la suite, shapes, las intrínsecas y Neo4j (T3)",
                           "lo contado sin leer (T3)", "los sorteos, el material y la lectura asistida (T4, primer tramo; lectura de la "
                           "ejecutora, sin API)", "las tasas (T4, segundo tramo)", "este reporte (T5)"],
    "estimado": {"por_etapa_con_la_tarifa": {e: q6(tot_plano[e]) for e in tot_plano}, "por_etapa_del_manifiesto": {e: q6(tot_mani[e]) for e in tot_mani},
                 "total": float(ESTIMADO_TOTAL), "lineas_de_alcance_total_usd": q6(sum(alc_to.values())),
                 "lineas_de_alcance_por_to": {to: q6(v) for to, v in alc_to.items() if v},
                 "lineas_de_alcance_como": "en E1, por TO, `usd_agregados` de alcance_e1/a2/salidas/medicion_tanda1_a2.json (como T1)"},
    "desviacion": {"por_etapa_contra_la_tarifa": {e: dif(tot_real[e], tot_plano[e]) for e in ("e1", "e3")},
                   "por_etapa_contra_el_manifiesto": {e: dif(tot_real[e], tot_mani[e]) for e in ("e1", "e3")},
                   "total": dif(total_real, tot_plano["e1"] + tot_plano["e3"]),
                   "va_a": "el re-presupuesto de la tanda final (docs/protocolo_entre_tandas.md:65-69)"},
    "por_to": por_to,
    "tarifa_observada": {"U": 3290, "e1_por_unidad": q6(tarifa_obs["e1"]), "e3_por_unidad": q6(tarifa_obs["e3"]),
                         "total_por_unidad": q6(tarifa_obs["e1"] + tarifa_obs["e3"]),
                         "tarifa_de_referencia": {"e1": float(TARIFA["e1"]), "e3": float(TARIFA["e3"]), "total": 0.021115},
                         "es": "propuesta para el §5 de la tabla de reprocesamiento; T5 no la escribe en la tabla"},
    "para_el_preregistro_tanda_final": para,
}
(SAL / "costo_t5.json").write_text(json.dumps(costo, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
consola.append(f"costo: real {coma(q6(total_real), 6)} (E1 {coma(q6(tot_real['e1']), 6)}, E3 {coma(q6(tot_real['e3']), 6)}); estimado "
               f"{coma(float(ESTIMADO_TOTAL))}; presupuesto_compartido {pres['gasto_usd']}; tarifa observada E1 "
               f"{coma(q6(tarifa_obs['e1']), 6)}, E3 {coma(q6(tarifa_obs['e3']), 6)}")

# ------------------------------------------------------------------ 2. los ids de modelo
copias = {}
for nombre, r in BASES.items():
    origen = X / r
    for suf in ("", "-wal", "-shm"):
        o = Path(str(origen) + suf)
        if o.exists():
            shutil.copy2(o, TRABAJO / f"{nombre}.db{suf}")
    copias[nombre] = TRABAJO / f"{nombre}.db" if origen.exists() else None
por_etapa, cuentas = {}, {}
for nombre, db in copias.items():
    assert db is not None, nombre
    etiquetas = [ETIQUETA[nombre].format(t) for t in orden]
    con = sqlite3.connect(str(db))
    try:
        filas = con.execute(f"SELECT c.model, COUNT(DISTINCT a.key) FROM access_log a JOIN cache c ON c.key = a.key "
                            f"WHERE a.run_label IN ({','.join('?' * len(etiquetas))}) GROUP BY c.model ORDER BY c.model", etiquetas).fetchall()
    finally:
        con.close()
    por_etapa[nombre] = sorted(m for m, _ in filas)
    cuentas[nombre] = {m: n for m, n in filas}
avance = [json.loads(x) for x in fuente(T1 / "t2/avance_t2.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
ev = [a for a in avance if "freno_modelo" in a or a.get("evento", "").startswith("freno_modelo")]
fm_res = sorted({a.get("resultado") or a.get("freno_modelo") for a in ev})
fm_e1 = sorted({i for a in ev for i in a.get("ids_e1", [])})
fm_e3 = sorted({i for a in ev for i in a.get("ids_e3", [])})
modelos = {
    "fuente": ("las bases de la caché del runner (data/experiment/reextraccion_v2/" + ", ".join(BASES.values()) + "), ignoradas por git; "
               "copiadas con sus -wal y -shm fuera del repo, como en t2/freno_modelo_t2.py; cache.model por access_log.run_label"),
    "e1": {"ids": por_etapa["e1"], "respuestas_distintas_por_id": cuentas["e1"],
           "que_cuenta": "las claves distintas de la caché de E1 con las etiquetas corpus_<TO>_e1 de los 20 TOs (incluye los reintentos "
                         "por corte y por forma de la fase E1)"},
    "e1_reintentos_de_la_fase_e3": {"ids": por_etapa["e1_reintentos"], "cuentas": "en NO_ABRIR_conteos_t5.json: cuentan los reintentos"},
    "e3": {"ids": por_etapa["e3"], "cuentas": "en NO_ABRIR_conteos_t5.json: cuentan los reintentos"},
    "contra_el_codigo_y_el_preregistro": {
        "e1": {"esperado": ID_E1, "fuente": "pre-registro, §2 (el freno por id); el código pide el alias claude-haiku-4-5 (runner_corpus.py:91)",
               "igual": por_etapa["e1"] == [ID_E1] and por_etapa["e1_reintentos"] in ([ID_E1], [])},
        "e3": {"esperado": ID_E3_CODIGO, "fuente": "runner_corpus.py:94 y pre-registro, §2", "igual": por_etapa["e3"] == [ID_E3_CODIGO]}},
    "contra_el_manifiesto": "el manifiesto 818a62cf… no fija el id de modelo: sus sellos no tienen esa clave (solo temperaturas y namespaces)",
    "contra_el_freno_por_modelo_de_T2": {"eventos": len(ev), "resultados": fm_res, "ids_e1": fm_e1, "ids_e3": fm_e3,
                                         "igual": fm_e1 == por_etapa["e1"] and fm_e3 == por_etapa["e3"]},
}
(SAL / "modelos_t5.json").write_text(json.dumps(modelos, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
no_abrir = {"que_es": "las cuentas de respuestas por id de modelo de E3 y de los reintentos de E1 de la fase de E3 (cuentan los reintentos)",
            "cuentas": {k: cuentas[k] for k in ("e1_reintentos", "e3")}}
(TRABAJO / "NO_ABRIR_parte_modelos_t5.json").write_text(json.dumps(no_abrir, ensure_ascii=False, indent=1, sort_keys=True) + "\n",
                                                         encoding="utf-8")
for p in TRABAJO.glob("*.db*"):
    p.unlink()
consola.append(f"modelos: E1 {por_etapa['e1']} {cuentas['e1']}; reintentos de E1 {por_etapa['e1_reintentos']}; E3 {por_etapa['e3']}; "
               f"freno de T2: {len(ev)} eventos, {fm_res}; iguales: {modelos['contra_el_freno_por_modelo_de_T2']['igual']}")

# ------------------------------------------------------------------ 3. los volúmenes
doble = L(fuente(T1 / "t3/salidas/doble_corrida_t3.json"))["doble_corrida"]
cont = L(fuente(T1 / "t3/conteos_sin_leer/contado_sin_leer_t3f.json"))
NOMBRES = {"t1_veinte": ("KG-Tanda1-Veinte-r2b", "veinte"), "t1_veinte_sincola": ("KG-Tanda1-Veinte-r2b-sincola", "veinte_sincola"),
           "acum_treinta": ("KG-Acumulado-Tandas0y1-r2b", "acumulado"), "acum_treinta_sincola": ("KG-Acumulado-Tandas0y1-r2b-sincola", "acumulado_sincola")}
volumenes = {
    "unidades": {k: res_t2["total"][k] for k in ("unidades", "unidades_con_partes", "aceptadas", "cola", "errores", "ids_repetidos")},
    "por_to": {to: {k: res_t2["por_to"][to][k] for k in ("unidades", "unidades_con_partes", "aceptadas", "cola", "errores")
                    if k in res_t2["por_to"][to]} for to in orden},
    "aceptadas_como": "los tres estados de aceptación juntos (t2/resumen_t2.json)",
    "grafos": {NOMBRES[k][0]: {"nodos": v["nodos"], "aristas": v["aristas"], "kg_sha256": v["kg_sha256"][0],
                               "unidades_e0": cont["grafos"][NOMBRES[k][1]]["unidades_e0_r2b"]} for k, v in doble.items()},
}
assert all(len(set(v["kg_sha256"])) == 1 for v in doble.values())
(SAL / "volumenes_t5.json").write_text(json.dumps(volumenes, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
consola.append("volúmenes: " + json.dumps(volumenes["unidades"], ensure_ascii=False) + " | " +
               "; ".join(f"{n} {v['nodos']}/{v['aristas']}" for n, v in volumenes["grafos"].items()))

# ------------------------------------------------------------------ 4. el alcance y el catálogo
cat = cont["catalogo_al_cierre"]
g_sc = cont["grafos"]["veinte_sincola"]
scripts_t3 = sorted((T1 / "t3/scripts").glob("*"))
con_cat_res = [p.name for p in scripts_t3 if p.is_file() and re.search(r"catalogo[-_]resolucion", p.read_text(encoding="utf-8", errors="replace"))]
alcance = {
    "catalogo_al_cierre": {g: {k: cat[g][k] for k in ("filas_registro", "cuarentena", "verificadas_en_cuarentena", "claves",
                                                      "n_claves_con_2_unidades_o_mas")}
                           | {"claves_con_3_unidades_o_mas": len(cat[g]["claves_con_3_unidades_o_mas"]),
                              "claves_en_2_tos_o_mas": len(cat[g]["claves_en_2_tos_o_mas"])} for g in cat},
    "umbral": "2 unidades distintas (enmienda 4, §1, punto 2, y decisión 1 al firmar)",
    "las_claves": "solo cuántas: son menciones de unidades que no están todas en unidades_a_la_vista_T4.json; la lista está en "
                  "t3/conteos_sin_leer/contado_sin_leer_t3f.json (catalogo_al_cierre), commiteada",
    "el_catalogo_no_crece_en_la_tanda_1": ("la lectura de sus claves se hace una sola vez, sobre el acumulado de las tres tandas "
                                           "(pre-registro de la tanda final, versión para firmar v3, §9, decisión 4); se declara como "
                                           "desvío del §5.5 del pre-registro de la tanda 1"),
    "versiones_del_catalogo": {
        "cuantas": 1,
        "cual": "la de la release (catálogo del request c3ad1581…, sin ampliaciones del catálogo de resolución)",
        "el_ensamblado_de_la_tanda_1_sin_catalogo_de_resolucion": not con_cat_res,
        "scripts_de_t3_que_lo_nombran": con_cat_res,
        "lo_que_resolvio_en_el_evaluado": {
            "relaciones_con_sujeto_id_de_E1": g_sc["vigilancias"]["8"]["sujeto_id"],
            "relaciones_con_sujeto_propuesto": g_sc["vigilancias"]["8"]["sujeto_propuesto"],
            "registro_de_no_mapeados": g_sc["f65_sujetos"]["registro_no_mapeados"]["filas"],
            "registro_por_estado": g_sc["f65_sujetos"]["registro_no_mapeados"]["por_estado"]},
        "fuente": "t3/conteos_sin_leer/contado_sin_leer_t3f.json, grafos.veinte_sincola (vigilancias.8 y f65_sujetos.registro_no_mapeados)",
        "sin_re_resolucion": "la cuenta por versión de la enmienda 4 (§1, punto 5) sigue a una re-resolución, que en la tanda 1 no corre"},
    "alcance_que_leyo_E1": {"derivado": "data/experiment/catalogo_unico/registro_alcance_r2b.json",
                            "sha256": sha(RAIZ / "data/experiment/catalogo_unico/registro_alcance_r2b.json"),
                            "igual_al_sello_del_manifiesto": sha(RAIZ / "data/experiment/catalogo_unico/registro_alcance_r2b.json") == DERIVADO_SHA
                            and man["sellos"]["candados"]["registro_alcance_r2b_json_sha256"] == DERIVADO_SHA,
                            "lineas_de_alcance": {"unidades": alc["total"]["unidades_que_cambian"], "tokens": alc["total"]["tokens_agregados"],
                                                  "usd": alc["total"]["usd_agregados"], "usd_sumado_por_to": q6(sum(alc_to.values()))}},
}
(SAL / "alcance_catalogo_t5.json").write_text(json.dumps(alcance, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
consola.append(f"catálogo: claves con 2 unidades o más, veinte sin cola {cat['veinte_sincola']['n_claves_con_2_unidades_o_mas']}; una versión; "
               f"sin catálogo de resolución en el ensamblado: {not con_cat_res}; derivado igual al sello: "
               f"{alcance['alcance_que_leyo_E1']['igual_al_sello_del_manifiesto']}")

# ------------------------------------------------------------------ 5. hallazgos, backlog y la columna del tablero
vista = L(fuente(T1 / "t3/muestras/unidades_a_la_vista_T4.json"))
a_la_vista = {u["chunk_id"] for m in vista["muestras"].values() for u in m["unidades"]}
LA = T1 / "t4/lectura_autora"


def marcada(m: str) -> list:
    with open(fuente(LA / f"{m}_marcada.csv"), encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter=";"))


fichas12 = {f"#{json.loads(x)['n']}": json.loads(x) for x in fuente(T1 / "t4/muestras/material/observacion_12/fichas_observacion_12.jsonl")
            .read_text(encoding="utf-8").splitlines() if x.strip()}
tasas = L(fuente(T1 / "t4/tasas/tasas_t4_tramo2.json"))
SIN_CAUSA = "causa: no dicha por la lectura"
DIFIERE_LECTURA = "se difiere: las incorrectas van al backlog con capa_pipeline (protocolo entre tandas, :97-100)"
hallazgos, dudosas, propuestas = [], [], []


def nuevo(**k) -> dict:
    k["id"] = f"H{len(hallazgos) + 1:02d}"
    hallazgos.append(k)
    return k


# 5a. las incorrectas de las lecturas de T4: aceptadas con error y la (12)
for m, nom in (("aceptadas_items", "aceptadas, ítems"), ("aceptadas_no_items", "aceptadas, no ítems")):
    for f in marcada(m):
        v = f["veredicto_autora"]
        if v not in ("con error", "dudosa"):
            continue
        assert f["id"] in a_la_vista, f["id"]
        x = {"muestra": nom, "unidad": f["id"], "celda": f["celda"], "ficha": f["ficha"], "veredicto_autora": v,
             "propuesta": f["propuesta"], "causa": f["nota_autora"].strip() or SIN_CAUSA}
        if v == "dudosa":
            dudosas.append(x)
            continue
        nuevo(tipo="incorrecta de una lectura de T4", **x, capa_pipeline="no dicha por la lectura",
              eje_A={"fila": None, "clase": None, "por_que": "la lectura no da la capa ni la fila" + ("" if f["nota_autora"].strip() else
                                                                                                      ", ni la causa")},
              eje_B=DIFIERE_LECTURA, backlog="propuesta", ancla=f"t4/lectura_autora/{m}_marcada.csv")
for f in marcada("observacion_12"):
    v = f["veredicto_autora"]
    if not v.startswith("incorrecta"):
        continue
    capa = re.match(r"^incorrecta \((.+)\)$", v).group(1)
    fi = fichas12[f["ficha"].split(".md")[-1]]
    u = fi["material"]["arista"]["procedencia"]["chunk_id"]
    assert u in a_la_vista, u
    nuevo(tipo="incorrecta de una lectura de T4", muestra="observación (12)", arista=f["id"],
          arista_codigo=hashlib.sha256(f["id"].encode()).hexdigest()[:12], unidad=u, celda=f["celda"], ficha=f["ficha"],
          veredicto_autora=v, propuesta=f["propuesta"], causa=f["nota_autora"].strip() or SIN_CAUSA, capa_pipeline=capa,
          eje_A={"fila": "F06" if capa == "E1-prompt" else None, "clase": "todo" if capa == "E1-prompt" else None,
                 "por_que": "la capa la da la lectura (E1-prompt): la corrige el prefijo de E1 (tabla de reprocesamiento, F06)"},
          eje_B=("se difiere: un cambio de prompt queda fuera del grafo que evalúa B6.3 (pre-registro, §6.1; protocolo entre tandas, "
                 ":93-95), y las incorrectas van al backlog con capa_pipeline (:97-100)"),
          backlog="propuesta", ancla="t4/lectura_autora/observacion_12_marcada.csv")
# 5b. la cola
cola_unid = []
for f in marcada("cola"):
    if f["veredicto_autora"] in ("con error", "dudosa"):
        assert f["id"] in a_la_vista, f["id"]
        cola_unid.append({"unidad": f["id"], "celda": f["celda"], "veredicto_autora": f["veredicto_autora"],
                          "causa": f["nota_autora"].strip() or SIN_CAUSA})
c = tasas["cola"]
nuevo(tipo="la cola, con la regla del 25 % disparada", muestra="cola",
      cifra=f"{c['regla']['errores']} de {c['regla']['leidas']}; ponderada {coma(c['regla']['tasa_ponderada'])}, Wilson "
            f"[{coma(c['regla']['wilson'][0])}; {coma(c['regla']['wilson'][1])}]; sin las dudosas, {c['sensibilidad_sin_dudosas']['errores']} de "
            f"{c['sensibilidad_sin_dudosas']['leidas']}", unidades=cola_unid, capa_pipeline="no dicha por la lectura",
      causa=("por unidad, en `unidades`: la nota de la autora, o «causa: no dicha por la lectura»; la causa de que se dispare la regla es "
             "la que investiga la mesa"),
      eje_A={"fila": None, "clase": None, "por_que": ("la regla, si se dispara, re-procesa las unidades de la cola o las saca del grafo "
                                                      "evaluado (enmienda de la cola humana, §1, punto 6); el evaluado ya es el sin cola")},
      eje_B=("la investigación de su causa, antes de la tanda final y sin cambiar el grafo sin cola (pre-registro, 95b18217:634-635); "
             "la diseña la mesa, no es de T5"), backlog="no: queda para la investigación de la causa", ancla="t4/tasas/tasas_t4_tramo2.json, cola")
# 5c. las regresiones declaradas de T3
clas = L(fuente(T1 / "t3/salidas/clasificacion_regresiones_t3.json"))


def buscar(v, item: str):
    """El registro de la suite con ese item, en cualquier nivel de la clasificación del evaluado."""
    if isinstance(v, dict):
        if v.get("item") == item:
            return v
        v = list(v.values())
    if isinstance(v, list):
        for x in v:
            r = buscar(x, item)
            if r is not None:
                return r
    return None


for item in ("E4-a1", "E4-a4"):
    r = buscar(clas["veinte_sincola"], item)
    assert r is not None and r["medido"] == "persiste", item
    nuevo(tipo="regresión declarada de T3", item=item, medido=r["medido"], esperado=r["esperado"],
          causa=("la de BKL-0048: la relación aplica_a de su unidad trae una mención que no está en el texto de la unidad, no verifica y va "
                 "a cuarentena; la suite lo cuenta porque mira la etiqueta con la regla de E4 de r1 (data/backlog/backlog.jsonl, BKL-0048)"),
          capa_pipeline="E1-prompt (la de BKL-0048)",
          eje_A={"fila": "F06", "clase": "todo", "por_que": "por la capa de BKL-0048, E1-prompt"},
          eje_B="se difiere: decisión de la autora del 18/10/2026, opción (ii) (registro de decisiones, §29)",
          backlog="ya está: BKL-0048", ancla="t3/salidas/clasificacion_regresiones_t3.json")
# 5d. las vigilancias fuera de su línea de base (pre-registro, §5.3; contado por T3)
vg = g_sc["vigilancias"]
nuevo(tipo="vigilancia fuera de su línea de base", vigilancia="(5)",
      cifra=f"requisito_de_estructura {vg['5']['total']['tipo_obligacion_requisito_de_estructura']}, tipo_obligacion_normalizados "
            f"{vg['5']['total']['tipo_obligacion_normalizados']}", linea_de_base="0 y 0 (pre-registro, §5.3)",
      causa="no dicha: es un conteo, sin lectura", capa_pipeline="no dicha: es un conteo, sin lectura",
      eje_A={"fila": None, "clase": "nada", "por_que": "requisito_de_estructura da 0, como su línea de base; el contador de normalizados da 1 "
                                                         "contra 0: el validador ya normalizó el valor, y se declara como residuo"},
      eje_B="no se corrige: residuo declarado", backlog="no", ancla="t3/conteos_sin_leer/contado_sin_leer_t3f.json, grafos.veinte_sincola.vigilancias.5")
nuevo(tipo="vigilancia fuera de su línea de base", vigilancia="(8)",
      cifra=f"sujeto_propuesto {vg['8']['sujeto_propuesto']} de sujeto_id {vg['8']['sujeto_id']} ({coma(vg['8']['tasa_pct'], 2)} %)",
      linea_de_base="diez 7,55 %; desarrollo 7,76 % (pre-registro, §5.3)", causa="no dicha: es un conteo, sin lectura",
      capa_pipeline="catálogo (la del remedio previsto: el crecimiento del catálogo de resolución, enmienda 4)",
      eje_A={"fila": "F13", "clase": "solo código sobre lo guardado", "por_que": "el catálogo de resolución crece al cierre y actúa sobre la mención guardada"},
      eje_B=("se corrige antes del sello del grafo evaluado, con la lectura única de las claves sobre las tres tandas (pre-registro de la "
             "tanda final, v3, §9, decisión 4), si la autora la aprueba a tiempo"), backlog="no: va por la lectura de las claves",
      ancla="t3/conteos_sin_leer/contado_sin_leer_t3f.json, grafos.veinte_sincola.vigilancias.8")
tos9 = sorted(t for t, n in vg["9"]["emisiones_E1_por_to"].items() if n)
por_to9 = ", ".join(f"{t} {vg['9']['emisiones_E1_por_to'][t]}" for t in tos9)
nuevo(tipo="vigilancia fuera de su línea de base", vigilancia="(9)",
      cifra=f"{vg['9']['emisiones_E1_total']} emisiones en E1 ({por_to9}); "
            f"{vg['9']['aristas_en_kg']} aristas en el grafo", linea_de_base="0 emisiones y 8 aristas (pre-registro, §5.3)",
      causa=("no dicha: es un conteo, sin lectura. La vigilancia pregunta por las emisiones fuera del dominio de pagos; si las de "
             + ", ".join(tos9) + " lo están no lo leí: NO VERIFICADO"),
      capa_pipeline="no dicha: es un conteo, sin lectura",
      eje_A={"fila": None, "clase": None, "por_que": "hace falta leer las emisiones (el instrumento de la vigilancia es un muestreo)"},
      eje_B="se difiere: la lectura de las emisiones no está despachada", backlog="propuesta",
      ancla="t3/conteos_sin_leer/contado_sin_leer_t3f.json, grafos.veinte_sincola.vigilancias.9")
# 5e. las filas del tablero, con la regla de cada una sobre el evaluado (veinte sin cola)
tabl = (RAIZ / "docs/tablero_correcciones.md").read_text(encoding="utf-8").splitlines()
fuente(RAIZ / "docs/tablero_correcciones.md")
sintoma = {}
for i in range(49, 75):
    celdas = [x.strip() for x in tabl[i - 1].split("|")]
    assert len(celdas) == 12, i
    sintoma[i] = celdas[1]
f64 = g_sc["f64_valores_fuera_de_lista"]
f67, f68 = g_sc["f67_cuantias"], g_sc["f68_omisiones"]
REGLA_FILAS = {
    49: ("sin meta numérica", "la meta es descriptiva, sin umbral (tablero:49)"),
    50: ("no medida", "la meta es de precisión (toda remite_a sostenida por cita y destino) y la tanda 1 no la leyó: la lectura de T4 contó "
                      "las remite_a aparte (lectura_asistida_t4_tramo1.json, criterios)"),
    51: ("no aplica", "la meta es la del laudo, §4, sobre el desarrollo; en la tanda 1, 0 `referencia` con origen distinto de TextoOrdenado"),
    52: ("no medida", "la cuenta de la meta (nodos de contenido sin establecida_en) no está en lo que contó T3, que es la de la "
                      "definición del 07/10/2026"),
    53: ("cumple", "el veinte no tiene cap; el acumulado, 0 hacia cap 6.5.1 o debajo"),
    54: ("cumple", "el veinte, fuera del grafo (decisión 3); el acumulado, resuelto"),
    55: ("cumple", "0 regresiones no declaradas que cuentan; las declaradas (E4-a1 y E4-a4) van como hallazgo aparte"),
    56: ("residuo declarado", "no medible sin el agente (EV2)"), 57: ("residuo declarado", "no medible sin el agente (EV2)"),
    58: ("residuo declarado", "no medible sin el agente (EV2)"),
    59: ("hallazgos por la lectura", "las incorrectas de la (12) van como hallazgos de lectura"),
    60: ("residuo declarado", "no medible sin el agente y el juez (EV2)"),
    61: ("cumple", "0 errores definitivos en T2 (resumen_t2.json); las 42 del sin cola son las de la cola"),
    62: ("cumple", "el veinte no tiene cap; el acumulado, resuelto"), 63: ("cumple", "el veinte no tiene esos TOs; el acumulado, 5 de 5"),
    64: ("no cumple", f"Comunicacion.tipo sin marca ni original {f64['Comunicacion.tipo']['sin_marca_ni_original']}: el residuo que la meta "
                      "declara (Comunicacion sin `tipo`; L-04)"),
    65: ("cumple", f"{g_sc['f65_sujetos']['con_sujeto_mencion']} de {g_sc['f65_sujetos']['aristas_de_sujeto']} con mención"),
    66: ("cumple", "0 / 0"),
    67: ("no cumple", f"{f67['sin_campo']} sin campo de {f67['con_cuantia']} con cuantía: el residuo que la meta declara (4 en diez)"),
    68: ("no cumple", f"sin categoría {f68['sin_categoria']}, sin tramo {f68['sin_tramo']}: el residuo que la meta declara (1 sin tramo por grafo)"),
    69: ("no medida", "bajo el cegamiento de U-MED-VERIF (NO_ABRIR_conteos_t3.json)"),
    70: ("cumple", "0 ids repetidos"), 71: ("cumple", "0"), 72: ("no aplica", "la tanda 1 no tiene E0 legada"), 73: ("cumple", "0"),
    74: ("cumple", "0 a `frecuencia`"),
}
assert sorted(REGLA_FILAS) == list(range(49, 75))
EJE_FILA = {
    64: ({"fila": "F14b", "clase": "solo código sobre lo guardado", "por_que": "si la lectura de L-04 llega al piso, la corrige su código "
                                                                               "previsto (la marca tipo_no_derivable de validador_r2; §6.7)"},
         "se corrige entre tandas solo por la regla de L-04 (§6.7), que no está despachada (registro de decisiones, §29); si no llega al "
         "piso, queda el residuo declarado"),
    67: ({"fila": None, "clase": "nada", "por_que": "se declara como residuo, como en la tanda 0 (tablero:67)"}, "no se corrige: residuo declarado"),
    68: ({"fila": None, "clase": "nada", "por_que": "se declara como residuo, como en la tanda 0 (tablero:68)"}, "no se corrige: residuo declarado"),
}
for i, (estado, porque) in REGLA_FILAS.items():
    if estado == "no cumple":
        eA, eB = EJE_FILA[i]
        nuevo(tipo="fila del tablero que no cumple su meta", fila_tablero=i, sintoma=sintoma[i], cifra=porque,
              causa="no dicha: es un conteo de T3, sin lectura", capa_pipeline="no dicha: es un conteo, sin lectura", eje_A=eA, eje_B=eB,
              backlog="no", ancla=f"t3/conteos_sin_leer/contado_sin_leer_t3f.json, grafos.veinte_sincola (fila {i})")
# 5f. las propuestas del backlog: lo diferido que pide una entrada
GRAFO = "KG-Tanda1-Veinte-r2b-sincola (data/experiment/reextraccion_v2/corpus_tanda1/ens_veinte_r2b_sincola/r2/kg.json, 384a6d5b…)"
for h in hallazgos:
    if h["backlog"] != "propuesta":
        continue
    p = {"propuesta_de": "T5 de la tanda 1 (B6.1)", "hallazgo": h["id"], "estado": "PROPUESTA: no está en el backlog", "grafo": GRAFO,
         "tipo": h["tipo"], "capa_pipeline": [h["capa_pipeline"]], "causa": h["causa"], "eje_A": h["eje_A"], "eje_B": h["eje_B"]}
    if "unidad" in h:
        p |= {"unidad": h["unidad"], "muestra": h["muestra"], "veredicto_autora": h["veredicto_autora"],
              "evidencia": [h["ancla"], h["ficha"]]}
    if "arista" in h:
        p |= {"arista_codigo": h["arista_codigo"]}
    if "vigilancia" in h:
        p |= {"vigilancia": h["vigilancia"], "cifra": h["cifra"], "evidencia": [h["ancla"]],
              "remedio": "leer las emisiones contra el dominio de pagos (instrumento de la vigilancia (9): muestreo de las emisiones)"}
    else:
        p["remedio"] = "a decidir: T5 no lo decide"
    propuestas.append(p)
# la columna «Tanda 1»: las celdas de T3, tal cual, y las que esperaban a T4
col_t3 = {}
for ln in fuente(T1 / "t3/conteos_sin_leer/columna_tanda1_tablero_t3f.md").read_text(encoding="utf-8").splitlines():
    mm = re.match(r"^\| (\d+) \| (.*) \| (.*) \|$", ln)
    if mm and 49 <= int(mm.group(1)) <= 74:
        col_t3[int(mm.group(1))] = mm.group(3)
assert sorted(col_t3) == list(range(49, 75))
o12 = tasas["observacion:12"]
celda59 = (f"veinte sin cola (el evaluado; lectura de T4): {o12['cruda']['correctas']} correctas de {o12['cruda']['de']}, Wilson "
           f"[{coma(o12['cruda']['wilson'][0])}; {coma(o12['cruda']['wilson'][1])}]; {o12['por_respuesta']['no decidible']} no decidibles; "
           f"incorrectas por capa: " + "; ".join(f"{k} {v['n']}" for k, v in o12["incorrectas_por_capa_pipeline"].items()) +
           f". Ponderada por celda {coma(o12['ponderada_por_celda']['tasa'])}. Base: {o12['linea_de_base_tanda0']}")
columna = []
for i in range(49, 75):
    t4 = i == 59
    columna.append({"fila": i, "sintoma": sintoma[i], "tanda_1": celda59 if t4 else col_t3[i],
                    "ancla": ("t4/tasas/tasas_t4_tramo2.json, observacion:12 (scripts/tasas_t4t2.py)" if t4 else
                              "t3/conteos_sin_leer/columna_tanda1_tablero_t3f.md, de contado_sin_leer_t3f.json (t3/scripts/tablas_contado_t3f.py)"),
                    "de": "T4" if t4 else "T3", "lectura_de_la_meta": {"estado": REGLA_FILAS[i][0], "por_que": REGLA_FILAS[i][1]}})
hall = {"hallazgos": hallazgos, "dudosas_de_las_aceptadas_aparte": dudosas,
        "dudosas_como": ("la lectura no las decidió: cuentan como error para la tasa, la atención y el freno (regla de las dudosas), y no "
                         "van como hallazgo ni al backlog; quedan para la mesa"),
        "no_son_hallazgo_por_las_reglas": {
            "vigilancias_sin_linea_de_base_comparable": {"(1)": tasas["vigilancias"]["vigilancia:1"]["por_respuesta"],
                                                         "(2)": tasas["vigilancias"]["vigilancia:2"]["por_respuesta"],
                                                         "(3)": tasas["vigilancias"]["vigilancia:3"]["por_respuesta"],
                                                         "(7)": tasas["vigilancias"]["vigilancia:7"]["por_respuesta"],
                                                         "por_que": "la tanda 0 no las leyó (pre-registro, §5.3): no hay una línea de base que pasar"},
            "vigilancia_4": vg["4"]["uno_por_to"], "aceptadas": "sin atención ni freno (tasas_t4_tramo2.json)",
            "filas_del_tablero": {str(i): REGLA_FILAS[i][0] for i in REGLA_FILAS if REGLA_FILAS[i][0] != "no cumple"}},
        "cuantos": {t: sum(1 for h in hallazgos if h["tipo"] == t) for t in dict.fromkeys(h["tipo"] for h in hallazgos)},
        "propuestas_del_backlog": len(propuestas)}
(SAL / "hallazgos_t5.json").write_text(json.dumps(hall, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
(SAL.parent / "propuestas_backlog_t5.jsonl").write_text("".join(json.dumps(p, ensure_ascii=False) + "\n" for p in propuestas), encoding="utf-8")
(SAL / "columna_tanda1_t5.json").write_text(json.dumps(columna, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
# ------------------------------------------------------------------ 6. las incidencias de T2
lanz, actual = [], None
for a in avance:
    if a.get("evento") == "inicio_lanzador":
        actual = {"inicio": a["ts"], "pid": a.get("pid"), "paradas": []}
        lanz.append(actual)
    elif a.get("evento") == "parada":
        actual["paradas"].append({"ts": a["ts"], "motivo": a["motivo"]})
    elif a.get("evento") == "fin_lanzador":
        actual["fin"] = a["ts"]
frenos = [x for x in res_t2["lineas_del_runner"] if x["linea"].startswith("FRENO")]
incid = {"lanzamientos_de_T2": lanz, "frenos_del_runner": frenos,
         "fuente": "t2/avance_t2.jsonl (inicio_lanzador, parada, fin_lanzador) y t2/resumen_t2.json (lineas_del_runner)",
         "decisiones_entre_lanzamientos": "las del FRENO T2, §0 (t2/FRENO_T2.md): relanzar igual; repartir el estimado por caracteres de E0 (ca5b39fd)"}
assert len(lanz) == 3 and len(frenos) == 2
(SAL / "incidencias_t5.json").write_text(json.dumps(incid, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
consola.append(f"incidencias: {len(lanz)} lanzamientos, {sum(len(x['paradas']) for x in lanz)} paradas, {len(frenos)} frenos por proyección")
(SAL / "fuentes_t5.json").write_text(json.dumps(dict(sorted(fuentes.items())), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
consola.append("hallazgos: " + json.dumps(hall["cuantos"], ensure_ascii=False) + f"; dudosas aparte {len(dudosas)}; propuestas del backlog "
               f"{len(propuestas)}; filas del tablero que no cumplen: {[i for i in REGLA_FILAS if REGLA_FILAS[i][0] == 'no cumple']}")
consola.append(f"fuentes leídas: {len(fuentes)}; salidas: " + ", ".join(sorted(p.name for p in SAL.iterdir()))
               + "; y ../propuestas_backlog_t5.jsonl")
(SAL / "consola_cifras_t5.txt").write_text("\n".join(consola) + "\n", encoding="utf-8")
print("\n".join(consola))
