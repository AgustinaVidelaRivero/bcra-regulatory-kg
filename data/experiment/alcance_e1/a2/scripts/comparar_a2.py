"""
comparar_a2.py — U-ALCANCE-E1, A2 (USD 0, sin API): compara, unidad por unidad, los mensajes de E1 de la corrida en seco
con el código de HEAD y con el de A2 (mensajes_runner_a2.py), y mide lo que agrega la línea de alcance en la lista final
de la tanda 1, como O2 de U-E3-LISTAS (data/experiment/e3_listas/freno_o2.md): por documento con línea nueva, unidades,
caracteres agregados, tokens estimados con la razón marginal de E1 (caracteres por token,
data/experiment/e3_listas/o3/razon_tokens_e1.json) y su costo a la tarifa de entrada de E1 (precio_in_por_mtok de P_E1,
corpus_v2/runner_corpus.py). La tarifa por unidad de E1 de la tabla de reprocesamiento (§5) da la referencia.

Una unidad se identifica por (origen, archivo, posición dentro del documento, id), como en comparar_a1.py. Un mensaje
distinto cuenta como «solo la línea» si el de A2, sin «línea + salto + salto», es el de HEAD.
Uso: comparar_a2.py DIR_SECO RAIZ_COPIA LISTA_JSON DERIVADO_JSON SALIDA.json
"""
import json
import re
import sys
from collections import OrderedDict
from pathlib import Path

d, raiz, lista_p, derivado_p, salida = (Path(x) for x in sys.argv[1:6])
TARIFA_E1_POR_UNIDAD = 0.010135   # tabla de reprocesamiento, §5 (comando 1), USD por unidad de la tanda 0
razon = json.loads((raiz / "data/experiment/e3_listas/o3/razon_tokens_e1.json").read_text(encoding="utf-8"))
runner = (raiz / "data/experiment/reextraccion_v2/corpus_v2/runner_corpus.py").read_text(encoding="utf-8")
m = re.search(r'^MODEL_E1 = "([^"]+)"\nP_E1 = dict\(precio_in_por_mtok=([0-9.]+),', runner, flags=re.M)
MODELO_E1, PRECIO_IN = m.group(1), float(m.group(2))
MARG = razon["chars_por_token_marginal"]
lista = json.loads(lista_p.read_text(encoding="utf-8"))
tanda1 = [to for k in sorted(lista["lista_final"], key=int) for to in lista["lista_final"][k]]
derivado = json.loads(derivado_p.read_text(encoding="utf-8"))


def leer(et):
    out, pos = OrderedDict(), {}
    for linea in (d / f"mensajes_{et}.jsonl").open(encoding="utf-8"):
        f = json.loads(linea)
        i = pos[(f["origen"], f["archivo"])] = pos.get((f["origen"], f["archivo"]), -1) + 1
        out[(f["origen"], f["archivo"], i, f["id"])] = f
    return out


h, n = leer("head"), leer("a2")
res = OrderedDict([("solo_en_a2", [list(k) for k in n if k not in h]),
                   ("solo_en_head", [list(k) for k in h if k not in n])])
por = OrderedDict()
for k, fn in n.items():
    if k not in h:
        continue
    fh = h[k]
    r = por.setdefault(k[0], OrderedDict()).setdefault(k[1], OrderedDict(
        [("unidades", 0), ("distintos", 0), ("solo_la_linea", 0), ("caracteres_agregados", 0),
         ("linea_head", set()), ("linea_a2", set())]))
    r["unidades"] += 1
    r["linea_head"].add(fh["linea_alcance"])
    r["linea_a2"].add(fn["linea_alcance"])
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
        lh, la = sorted(r["linea_head"], key=str), sorted(r["linea_a2"], key=str)
        filas[a] = OrderedDict([("unidades", r["unidades"]), ("distintos", r["distintos"]),
                                ("solo_la_linea_de_alcance", r["solo_la_linea"]),
                                ("con_linea_head", lh != [None]), ("con_linea_a2", la != [None]),
                                ("linea_nueva", la[0] if r["distintos"] and len(la) == 1 else None),
                                ("caracteres_agregados", r["caracteres_agregados"])])
    origenes[o] = OrderedDict([("unidades", sum(x["unidades"] for x in filas.values())),
                               ("distintos", sum(x["distintos"] for x in filas.values())),
                               ("solo_la_linea", sum(x["solo_la_linea_de_alcance"] for x in filas.values())),
                               ("documentos_que_cambian", [a for a, x in filas.items() if x["distintos"]]),
                               ("por_documento", filas)])
res["por_origen"] = origenes

t1 = origenes.get("tanda1_e0_corregida", {}).get("por_documento", {})
archivos_t1 = [f"{to}.pdf" for to in tanda1]
con_linea_nueva = [a for a in archivos_t1 if t1.get(a, {}).get("distintos")]
medicion = OrderedDict()
for a in con_linea_nueva:
    x = t1[a]
    tok = x["caracteres_agregados"] / MARG
    medicion[a[:-4]] = OrderedDict([
        ("unidades", x["unidades"]), ("unidades_que_cambian", x["distintos"]),
        ("solo_la_linea", x["solo_la_linea_de_alcance"]), ("linea", x["linea_nueva"]),
        ("caracteres_por_unidad", len(x["linea_nueva"]) + 2 if x["linea_nueva"] else None),
        ("caracteres_agregados", x["caracteres_agregados"]), ("tokens_agregados", round(tok)),
        ("usd_agregados", round(tok * PRECIO_IN / 1e6, 6)),
        ("usd_e1_de_referencia", round(x["unidades"] * TARIFA_E1_POR_UNIDAD, 4))])
tot_chars = sum(v["caracteres_agregados"] for v in medicion.values())
tot_tok = tot_chars / MARG
res["medicion_tanda1"] = OrderedDict([
    ("lista_final", tanda1), ("unidades_de_la_lista", sum(t1.get(a, {}).get("unidades", 0) for a in archivos_t1)),
    ("documentos_del_derivado_en_la_lista", [a[:-4] for a in archivos_t1 if a in derivado]),
    ("documentos_con_linea_nueva", [a[:-4] for a in con_linea_nueva]),
    ("cambian_solo_los_del_derivado", sorted(con_linea_nueva) == sorted(a for a in archivos_t1 if a in derivado)),
    ("todo_cambio_es_solo_la_linea", all(v["unidades_que_cambian"] == v["solo_la_linea"] == v["unidades"]
                                         for v in medicion.values())),
    ("por_documento", medicion),
    ("total", OrderedDict([("unidades_que_cambian", sum(v["unidades_que_cambian"] for v in medicion.values())),
                           ("caracteres_agregados", tot_chars), ("tokens_agregados", round(tot_tok)),
                           ("usd_agregados", round(tot_tok * PRECIO_IN / 1e6, 6))])),
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
mt = res["medicion_tanda1"]
print("tanda 1:", mt["unidades_de_la_lista"], "unidades;", len(mt["documentos_con_linea_nueva"]), "documentos con línea nueva;",
      "solo los del derivado:", mt["cambian_solo_los_del_derivado"], "| solo la línea:", mt["todo_cambio_es_solo_la_linea"])
for to, v in mt["por_documento"].items():
    print(f"   {to:10s} u={v['unidades']:4d} cambian={v['unidades_que_cambian']:4d} +{v['caracteres_por_unidad']} car/u "
          f"car={v['caracteres_agregados']:6d} tok={v['tokens_agregados']:6d} usd={v['usd_agregados']:.6f}")
print("   total", mt["total"])
print("solo en a2:", res["solo_en_a2"], "| solo en head:", res["solo_en_head"])
