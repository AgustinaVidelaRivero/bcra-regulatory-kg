"""
comparar_a3.py — U-ALCANCE-E1, A3 (USD 0, sin API): compara, unidad por unidad, los mensajes de E1 de la corrida en seco con
el código de HEAD y con el de A3 (mensajes_runner_a3.py) en las tres tandas, y mide lo que agrega la línea de alcance en la
tanda final, como comparar_a2.py de A2 en la tanda 1: por documento con línea nueva, unidades, caracteres agregados, tokens
estimados con la razón marginal de E1 (caracteres por token, data/experiment/e3_listas/o3/razon_tokens_e1.json) y su costo
a la tarifa de entrada de E1 (precio_in_por_mtok de P_E1, corpus_v2/runner_corpus.py). La tarifa por unidad de E1 de la
tabla de reprocesamiento (§5) da la referencia.

Una unidad se identifica por (origen, archivo, posición dentro del documento, id), como en comparar_a2.py. Un mensaje
distinto cuenta como «solo la línea» si el de A3, sin «línea + salto + salto», es el de HEAD.

Los documentos que tienen que cambiar: los de la tanda final con entrada nueva en el derivado (las del derivado de A3 que no
están en el de HEAD), que son las filas de la tabla «## Tanda final» con clase, dos clases o rol reutilizado (reporte del
derivado). Los documentos de la tanda final sin fila en el registro ni entrada en la tabla de la release
(generados_r2/rol_por_to_r2.json) se listan con su id: la lista tiene que ser vacía o la de los que la mesa sacó.
Uso: comparar_a3.py DIR_SECO RAIZ_COPIA LISTA_TANDA1 TANDA_FINAL_S2C DERIVADO_HEAD DERIVADO_A3 REPORTE_DERIVADO_A3 SALIDA.json
"""
import json
import re
import sys
from collections import OrderedDict
from pathlib import Path

d, raiz, lista_p, tf_p, der_h_p, der_n_p, rep_p, salida = (Path(x) for x in sys.argv[1:9])
TARIFA_E1_POR_UNIDAD = 0.010135   # tabla de reprocesamiento, §5 (comando 1), USD por unidad de la tanda 0
SHA_TANDA0_A2 = "48fdec197658"     # el de R2-2 y A2 (freno_a2.md, criterios)
razon = json.loads((raiz / "data/experiment/e3_listas/o3/razon_tokens_e1.json").read_text(encoding="utf-8"))
runner = (raiz / "data/experiment/reextraccion_v2/corpus_v2/runner_corpus.py").read_text(encoding="utf-8")
m = re.search(r'^MODEL_E1 = "([^"]+)"\nP_E1 = dict\(precio_in_por_mtok=([0-9.]+),', runner, flags=re.M)
MODELO_E1, PRECIO_IN = m.group(1), float(m.group(2))
MARG = razon["chars_por_token_marginal"]
rol_por_to = json.loads((raiz / "data/experiment/catalogo_unico/generados_r2/rol_por_to_r2.json").read_text(encoding="utf-8"))
lista = json.loads(lista_p.read_text(encoding="utf-8"))
tanda1 = [to for k in sorted(lista["lista_final"], key=int) for to in lista["lista_final"][k]]
tanda_final = list(json.loads(tf_p.read_text(encoding="utf-8"))["tanda_final"]["lista"])
der_h = json.loads(der_h_p.read_text(encoding="utf-8"))
der_n = json.loads(der_n_p.read_text(encoding="utf-8"))
rep = json.loads(rep_p.read_text(encoding="utf-8"))
filas_final = {f["archivo"]: {"rol_reutilizado": "rol reutilizado"}.get(f["decision"], "clase (dos)" if len(f["ids"]) == 2
                                                                       else "clase")
               for f in rep["filas_con_alcance"] if f["tanda"] == "final"}
filas_final.update({f"{f['to']}.pdf": "sin_alcance" for f in rep["sin_alcance_declarado"] if f["tanda"] == "final"})


def leer(et):
    out, pos = OrderedDict(), {}
    for linea in (d / f"mensajes_{et}.jsonl").open(encoding="utf-8"):
        f = json.loads(linea)
        i = pos[(f["origen"], f["archivo"])] = pos.get((f["origen"], f["archivo"]), -1) + 1
        out[(f["origen"], f["archivo"], i, f["id"])] = f
    return out


h, n = leer("head"), leer("a3")
res = OrderedDict([("solo_en_a3", [list(k) for k in n if k not in h]),
                   ("solo_en_head", [list(k) for k in h if k not in n])])
por = OrderedDict()
for k, fn in n.items():
    if k not in h:
        continue
    fh = h[k]
    r = por.setdefault(k[0], OrderedDict()).setdefault(k[1], OrderedDict(
        [("unidades", 0), ("distintos", 0), ("solo_la_linea", 0), ("caracteres_agregados", 0),
         ("linea_head", set()), ("linea_a3", set())]))
    r["unidades"] += 1
    r["linea_head"].add(fh["linea_alcance"])
    r["linea_a3"].add(fn["linea_alcance"])
    if fn["mensaje"] != fh["mensaje"]:
        r["distintos"] += 1
        ln = fn["linea_alcance"]
        if (fh["linea_alcance"] is None and ln is not None and fn["mensaje"].count(ln + "\n\n") == 1
                and fn["mensaje"].replace(ln + "\n\n", "") == fh["mensaje"]):
            r["solo_la_linea"] += 1
        r["caracteres_agregados"] += fn["caracteres"] - fh["caracteres"]
origenes = OrderedDict()
for o, docs in por.items():
    filas = OrderedDict()
    for a, r in docs.items():
        lh, la = sorted(r["linea_head"], key=str), sorted(r["linea_a3"], key=str)
        filas[a] = OrderedDict([("unidades", r["unidades"]), ("distintos", r["distintos"]),
                                ("solo_la_linea_de_alcance", r["solo_la_linea"]),
                                ("con_linea_head", lh != [None]), ("con_linea_a3", la != [None]),
                                ("linea_nueva", la[0] if r["distintos"] and len(la) == 1 else None),
                                ("caracteres_agregados", r["caracteres_agregados"])])
    origenes[o] = OrderedDict([("unidades", sum(x["unidades"] for x in filas.values())),
                               ("distintos", sum(x["distintos"] for x in filas.values())),
                               ("solo_la_linea", sum(x["solo_la_linea_de_alcance"] for x in filas.values())),
                               ("documentos_que_cambian", [a for a, x in filas.items() if x["distintos"]]),
                               ("por_documento", filas)])
res["por_origen"] = origenes


def sha_mensajes(et: str, origen: str) -> str:
    import hashlib
    ms = [f["mensaje"] for k, f in (h if et == "head" else n).items() if k[0] == origen]
    return hashlib.sha256("\n\x1e\n".join(ms).encode("utf-8")).hexdigest()


t0, t1 = origenes["tanda0_salida_tanda0_r2b"], origenes["tanda1_e0_corregida"]
res["tanda0"] = OrderedDict([("unidades", t0["unidades"]), ("distintas", t0["distintos"]),
                             ("sha256_mensajes_head", sha_mensajes("head", "tanda0_salida_tanda0_r2b")),
                             ("sha256_mensajes_a3", sha_mensajes("a3", "tanda0_salida_tanda0_r2b"))])
res["tanda0"]["igual"] = (t0["distintos"] == 0 and res["tanda0"]["sha256_mensajes_head"] == res["tanda0"]["sha256_mensajes_a3"]
                          and res["tanda0"]["sha256_mensajes_a3"].startswith(SHA_TANDA0_A2))
res["tanda1"] = OrderedDict([("lista_final", tanda1), ("unidades", t1["unidades"]), ("distintas", t1["distintos"]),
                             ("documentos", len(t1["por_documento"])), ("igual", t1["distintos"] == 0)])
fx = origenes["fixture_candado"]
res["fixture"] = OrderedDict([("unidades", fx["unidades"]), ("distintas", fx["distintos"])])

tf = origenes["tandafinal_e0_corregida"]["por_documento"]
archivos_tf = [f"{to}.pdf" for to in tanda_final]
nuevos_en_el_derivado = [a for a in der_n if a not in der_h]
deben_cambiar = [a for a in archivos_tf if a in nuevos_en_el_derivado]
con_linea_nueva = [a for a in archivos_tf if tf.get(a, {}).get("distintos")]
sin_fila_ni_rol = [a[:-4] for a in archivos_tf if a not in rol_por_to and a not in filas_final]
medicion = OrderedDict()
for a in con_linea_nueva:
    x = tf[a]
    tok = x["caracteres_agregados"] / MARG
    medicion[a[:-4]] = OrderedDict([
        ("decision_del_registro", filas_final.get(a)),
        ("unidades", x["unidades"]), ("unidades_que_cambian", x["distintos"]),
        ("solo_la_linea", x["solo_la_linea_de_alcance"]), ("linea", x["linea_nueva"]),
        ("caracteres_por_unidad", len(x["linea_nueva"]) + 2 if x["linea_nueva"] else None),
        ("caracteres_agregados", x["caracteres_agregados"]), ("tokens_agregados", round(tok)),
        ("usd_agregados", round(tok * PRECIO_IN / 1e6, 6)),
        ("usd_e1_de_referencia", round(x["unidades"] * TARIFA_E1_POR_UNIDAD, 4))])
tot_chars = sum(v["caracteres_agregados"] for v in medicion.values())
tot_tok = tot_chars / MARG
unidades_tf = sum(tf.get(a, {}).get("unidades", 0) for a in archivos_tf)
res["tanda_final"] = OrderedDict([
    ("documentos", len(archivos_tf)), ("unidades", unidades_tf),
    ("con_entrada_en_la_release", sum(a in rol_por_to for a in archivos_tf)),
    ("con_fila_en_la_tabla_final_del_registro", sum(a in filas_final for a in archivos_tf)),
    ("con_fila_y_entrada_en_la_release", [a[:-4] for a in archivos_tf if a in rol_por_to and a in filas_final]),
    ("filas_de_la_tabla_final_fuera_de_la_tanda", sorted(a[:-4] for a in filas_final if a not in archivos_tf)),
    ("sin_fila_ni_rol", sin_fila_ni_rol),
    ("entradas_nuevas_del_derivado", len(nuevos_en_el_derivado)),
    ("entradas_nuevas_fuera_de_la_tanda_final", [a[:-4] for a in nuevos_en_el_derivado if a not in archivos_tf]),
    ("documentos_que_deben_cambiar", [a[:-4] for a in deben_cambiar]),
    ("documentos_con_linea_nueva", [a[:-4] for a in con_linea_nueva]),
    ("cambian_solo_los_de_fila_nueva", con_linea_nueva == deben_cambiar),
    ("todo_cambio_es_solo_la_linea_y_en_todas_sus_unidades",
     all(v["unidades_que_cambian"] == v["solo_la_linea"] == v["unidades"] for v in medicion.values())),
    ("los_demas_sin_cambios", sum(tf.get(a, {}).get("distintos", 0) for a in archivos_tf if a not in deben_cambiar) == 0),
    ("por_documento", medicion),
    ("total", OrderedDict([("documentos", len(medicion)),
                           ("unidades_que_cambian", sum(v["unidades_que_cambian"] for v in medicion.values())),
                           ("caracteres_agregados", tot_chars), ("tokens_agregados", round(tot_tok)),
                           ("usd_agregados", round(tot_tok * PRECIO_IN / 1e6, 6)),
                           ("usd_e1_de_referencia_de_esas_unidades",
                            round(sum(v["unidades"] for v in medicion.values()) * TARIFA_E1_POR_UNIDAD, 4)),
                           ("usd_e1_de_referencia_de_la_tanda_final", round(unidades_tf * TARIFA_E1_POR_UNIDAD, 4))])),
    ("metodo", OrderedDict([("razon_marginal_chars_por_token", MARG),
                            ("fuente_razon", "data/experiment/e3_listas/o3/razon_tokens_e1.json"),
                            ("modelo_e1", MODELO_E1), ("precio_entrada_usd_por_millon", PRECIO_IN),
                            ("fuente_precio", "data/experiment/reextraccion_v2/corpus_v2/runner_corpus.py, P_E1"),
                            ("tarifa_e1_por_unidad_tabla", TARIFA_E1_POR_UNIDAD),
                            ("alcance", "una llamada de E1 por unidad; los reintentos de E1 (por corte, por forma y del "
                                        "ratchet) reenvían el mensaje y suman lo suyo")]))])
salida.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for o, r in origenes.items():
    print(o, "unidades", r["unidades"], "distintos", r["distintos"], "solo la línea", r["solo_la_linea"],
          "documentos que cambian", len(r["documentos_que_cambian"]))
print("tanda 0:", {k: v for k, v in res["tanda0"].items()})
print("tanda 1:", {k: v for k, v in res["tanda1"].items() if k != "lista_final"})
print("fixture:", dict(res["fixture"]))
mt = res["tanda_final"]
print("tanda final:", mt["documentos"], "documentos,", mt["unidades"], "unidades;", "con entrada en la release",
      mt["con_entrada_en_la_release"], "| con fila en la tabla final", mt["con_fila_en_la_tabla_final_del_registro"],
      "| sin fila ni rol", mt["sin_fila_ni_rol"], "| fila y release a la vez", mt["con_fila_y_entrada_en_la_release"],
      "| filas fuera de la tanda", mt["filas_de_la_tabla_final_fuera_de_la_tanda"])
print("   entradas nuevas del derivado", mt["entradas_nuevas_del_derivado"], "| fuera de la tanda final",
      mt["entradas_nuevas_fuera_de_la_tanda_final"], "| documentos con línea nueva", len(mt["documentos_con_linea_nueva"]),
      "| solo los de fila nueva:", mt["cambian_solo_los_de_fila_nueva"], "| solo la línea, en todas sus unidades:",
      mt["todo_cambio_es_solo_la_linea_y_en_todas_sus_unidades"], "| los demás sin cambios:", mt["los_demas_sin_cambios"])
for to, v in mt["por_documento"].items():
    print(f"   {to:16s} {v['decision_del_registro']:16s} u={v['unidades']:4d} cambian={v['unidades_que_cambian']:4d} "
          f"+{v['caracteres_por_unidad']} car/u car={v['caracteres_agregados']:6d} tok={v['tokens_agregados']:6d} "
          f"usd={v['usd_agregados']:.6f}")
print("   total", dict(mt["total"]))
print("solo en a3:", res["solo_en_a3"], "| solo en head:", res["solo_en_head"])
