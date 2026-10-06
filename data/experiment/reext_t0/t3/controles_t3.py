"""U-REEXT-T0, T3, punto 3: los controles propios a–r (mandato firmado en e2027dd, :235-276), cada uno con su cifra,
sobre los dos grafos r2b, su salida de corrida y su gate. USD 0, sin red, solo lectura de lo que se le pasa; escribe
solo --out (JSON con las cifras y la evidencia de las lecturas). Corre desde la raíz de una COPIA del repo.

Las lecturas que el mandato pide «contra el chunk» (c, d, m, n, o, p) salen acá como evidencia (nodos, aristas, menciones
y texto del chunk); el juicio de cada una está en lectura_controles_t3.md, escrito sobre esta evidencia.

Uso: python -B controles_t3.py --out data/experiment/reext_t0/t3/salida/controles_t3.json
"""
import argparse
import glob
import json
import re
import sys
import unicodedata
from collections import Counter, OrderedDict, defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[4]
REX = RAIZ / "data/experiment/reextraccion_v2"
T0 = REX / "corpus_tanda0"
SAL = T0 / "salida_r2b"
E0 = REX / "e0_chunking" / "salida_tanda0_r2b"
for _p in (REX / "e1_extractor", RAIZ / "data/experiment/pyd_r2/code"):
    sys.path.insert(0, str(_p))
GRAFOS = OrderedDict([("diez", T0 / "ens_diez_r2b"), ("desarrollo", T0 / "ens_desarrollo_r2b")])

ap = argparse.ArgumentParser()
ap.add_argument("--out", required=True)
a = ap.parse_args()


def leer(p: Path):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def jsonl(p: Path) -> list:
    return [json.loads(x) for x in Path(p).read_text(encoding="utf-8").splitlines() if x.strip()] if Path(p).exists() else []


def last_wins(p: Path) -> dict:
    return {r["chunk_id"]: r for r in jsonl(p)}


def provs(x: dict) -> list:
    return [p for p in [x.get("provenance")] + (x.get("provenances") or []) if p]


def chunks_de(x: dict) -> set:
    return {p.get("chunk_id") for p in provs(x) if p.get("chunk_id")}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    return " ".join(re.sub(r"[^a-z0-9]+", " ", s).split())


def cola(x: dict) -> bool:
    return (x.get("properties") or {}).get("cola_humana") == "true"


CHUNKS = {}
for f in sorted(E0.glob("chunks_*.json")):
    for c in leer(f):
        CHUNKS[c["id"]] = c
for p in sorted(SAL.glob("*/particiones_por_corte.json")):
    for v in leer(p).values():
        for c in v["partes"]:
            CHUNKS[c["id"]] = c
TOS = sorted({p.parent.name for p in SAL.glob("*/finales.jsonl")})
FIN = {to: last_wins(SAL / to / "finales.jsonl") for to in TOS}
E1 = {to: last_wins(SAL / to / "extracciones_e1.jsonl") for to in TOS}
FR2 = {to: last_wins(SAL / to / f"extracciones_finales_r2_{to}.jsonl") for to in TOS}


def texto_chunk(cid: str) -> str:
    c = CHUNKS.get(cid) or {}
    her = " | ".join(f"[{h.get('tipo')}] {h.get('texto')}" for h in c.get("herencia") or [])
    return (f"HERENCIA: {her}\nTEXTO: " if her else "TEXTO: ") + (c.get("texto") or "")


def nodo_breve(n: dict) -> dict:
    pr = n.get("properties") or {}
    return OrderedDict([("id", n["id"]), ("type", n["type"]), ("label", n.get("label")),
                        ("descripcion", pr.get("descripcion")), ("tipo", pr.get("tipo")), ("cola", cola(n)),
                        ("chunks", sorted(chunks_de(n)))])


def arista_breve(e: dict, idx: dict) -> dict:
    return OrderedDict([("source", e["source"]), ("relation", e["relation"]), ("target", e["target"]),
                        ("tipo_source", idx.get(e["source"], {}).get("type")),
                        ("tipo_target", idx.get(e["target"], {}).get("type")),
                        ("sujeto_mencion", e.get("sujeto_mencion")), ("mencion_verificada", e.get("mencion_verificada")),
                        ("metodo_resolucion", e.get("metodo_resolucion")), ("sujeto_id_modelo", e.get("sujeto_id_modelo")),
                        ("coherencia_tipo_predicado", e.get("coherencia_tipo_predicado")),
                        ("chunks", sorted(chunks_de(e)))])


res = OrderedDict([("insumos", OrderedDict()), ("por_grafo", OrderedDict())])
for k, d in GRAFOS.items():
    res["insumos"][k] = {"kg": str((d / "r2" / "kg.json").relative_to(RAIZ))}

# ---- controles que dependen solo de la salida de la corrida (iguales en los dos grafos) ----
# e. forma A (método de reports/u_diag_proceso/code/vu_tanda0.py y vu_b_alcance.py, sobre la E0 r2b y la validación
#    final r2 de la entrada de E2 r2; mismo criterio: Condicion de un ítem = último tramo heredado que termina en «:»)
nrm = lambda s: " ".join((s or "").split())
dp = lambda s: nrm(s).endswith((":", "："))
DEST = {"Excepcion", "Obligacion", "Restriccion", "Operacion", "Potestad"}
fin_val = {cid: r["validacion"] for to in TOS for cid, r in FR2[to].items() if r.get("validacion")}
cnt_e = Counter()
casos_a = []
for cid, v in fin_val.items():
    c = CHUNKS.get(cid)
    if not c or c["tipo"] != "punto_terminal" or not c.get("herencia"):
        continue
    rels = v.get("relaciones", [])
    rech = [x.get("elemento") or {} for x in v.get("rechazos", []) if x.get("nivel") == "relacion"]
    ult = c["herencia"][-1]
    if not dp(ult["texto"]):
        continue
    for e in v.get("entidades", []):
        if e["type"] != "Condicion":
            continue
        cnt_e["condicion_de_item"] += 1
        sal = any(x["source"] == e["local_id"] and x["predicate"] == "condicion_de" for x in rels)
        if sal:
            continue
        cnt_e["sin_condicion_de"] += 1
        if any(x.get("source") == e["local_id"] and x.get("predicate") == "condicion_de" for x in rech):
            cnt_e["sin_condicion_de_pero_rechazada"] += 1
            continue
        cnt_e["sin_condicion_de_ni_rechazada"] += 1
        mini = f"{c['to']}::{ult.get('unidad_origen')}::intro"
        vm = fin_val.get(mini)
        dest = [x["type"] for x in (vm or {}).get("entidades", []) if x["type"] in DEST]
        if ult.get("tipo") == "intro" and dest:
            cnt_e["forma_A_encabezado_con_nodos_destino"] += 1
            casos_a.append({"chunk": cid, "mini": mini, "destinos": dest})
        elif ult.get("tipo") == "encabezado":
            cnt_e["encabezado_es_titulo"] += 1
        else:
            cnt_e["otro"] += 1
res["e_forma_A"] = OrderedDict([("conteos", dict(cnt_e)), ("referencia_matriz_congelada", "36 de las 56 sin condicion_de, sobre 458"),
                               ("casos_forma_A", casos_a)])

# l. mini-chunks a mitad de oración (prompt_r2b.mini_a_mitad) con un tramo de dos segmentos (validador_r2,
#    _RE_SEPARADOR_TRAMO)
import prompt_r2b    # noqa: E402
import validador_r2  # noqa: E402
RE_SEP = validador_r2._RE_SEPARADOR_TRAMO
mitad = [cid for cid, c in CHUNKS.items() if c.get("tipo") == "mini_chunk" and prompt_r2b.mini_a_mitad(c)]
minis = [cid for cid, c in CHUNKS.items() if c.get("tipo") == "mini_chunk"]
dos_seg = defaultdict(list)
for cid in mitad:
    v = fin_val.get(cid) or {}
    for e in v.get("entidades", []):
        t = (e.get("provenance") or {}).get("tramo") or e.get("tramo") or ""
        if len(RE_SEP.findall(t)) == 1:
            dos_seg[cid].append(e.get("local_id"))
res["l_mini_a_mitad"] = OrderedDict([("mini_chunks", len(minis)), ("a_mitad_de_oracion", len(mitad)),
                                    ("con_tramo_de_dos_segmentos", len(dos_seg)),
                                    ("tramos_de_dos_segmentos", sum(len(v) for v in dos_seg.values())),
                                    ("chunks", OrderedDict(sorted(dos_seg.items())))])

# a (parte de la salida): la cola humana, unidades y partes
cola_unidades = sorted(cid for to in TOS for cid, r in FIN[to].items() if str(r.get("estado")).startswith("cola_humana"))
res["a_cola_humana_salida"] = OrderedDict([("entradas", len(cola_unidades)),
                                           ("partes", [c for c in cola_unidades if "::parte" in c]),
                                           ("por_estado", dict(Counter(FIN[c.split("::")[0]][c]["estado"] for c in cola_unidades)))])

for k, d in GRAFOS.items():
    kg = leer(d / "r2" / "kg.json")
    rep = leer(d / "r2" / "reporte_ensamblado_r2.json")
    suite = leer(d / "suite_perfil_r2.json")
    items = {it["id"]: it for it in suite["items"]}
    decl = leer(d / "r2" / "declaracion_partes_y_reparadas.json")
    idx = {n["id"]: n for n in kg["nodes"]}
    tos_g = rep["manifiesto"]["orden_corrida"]
    g = OrderedDict()
    # a
    reparadas = list(decl["reparadas_forma"])
    parte1 = [p for v in decl["particionadas_por_corte"].values() for p in v["partes"] if p.endswith("parte1")]
    nodos_cola = [n for n in kg["nodes"] if cola(n)]
    g["a_cero_sin_verificar"] = OrderedDict([
        ("paso_por_e3_total", rep.get("paso_por_e3", {}).get("total")),
        ("aristas_no_verificadas_e3", rep.get("aristas_no_verificadas_e3")),
        ("item_SIN_VERIF_E3", {x: items.get("SIN-VERIF-E3", {}).get(x) for x in ("estado", "detalle")}),
        ("cola_humana", OrderedDict([("unidades_de_cola_del_grafo", sum(len((v.get("cola_flaggeada") or {}).get("chunks_de_cola") or [])
                                                                       for v in rep["e2_por_to"].values())),
                                     ("nodos_con_marca", len(nodos_cola)),
                                     ("nodos_de_la_parte1", sum(1 for n in kg["nodes"] if set(parte1) & chunks_de(n))),
                                     ("nodos_de_las_reparadas", OrderedDict((r, sum(1 for n in kg["nodes"] if r in chunks_de(n)))
                                                                            for r in reparadas))]))])
    # b
    def anclado(n, to, punto, exacto=True):
        return any(p.get("to") == to and (str(p.get("punto")) == punto if exacto else
                                          (str(p.get("punto")) == punto or str(p.get("punto")).startswith(punto + ".")))
                   for p in provs(n))
    rb = [e for e in kg["edges"] if e["relation"] == "remite_a" and anclado(idx[e["source"]], "cla", "5.1.1.1")
          and anclado(idx[e["target"]], "cla", "3.7")]
    rb_sub = [e for e in kg["edges"] if e["relation"] == "remite_a" and anclado(idx[e["source"]], "cla", "5.1.1.1")
              and anclado(idx[e["target"]], "cla", "3.7", exacto=False)]
    g["b_remision_del_ejemplo"] = OrderedDict([("remite_a_5_1_1_1_a_3_7", len(rb)), ("a_3_7_o_debajo", len(rb_sub)),
                                              ("aristas", [arista_breve(e, idx) for e in rb_sub]),
                                              ("item_EJ_cla_5_1_1_1", {x: items.get("EJ-cla-5.1.1.1", {}).get(x) for x in ("estado", "detalle")})])
    # c
    n5111 = [n for n in kg["nodes"] if "cla::5.1.1.1" in chunks_de(n)]
    intro = [n for n in kg["nodes"] if "cla::5.1.1::intro" in chunks_de(n)]
    hijos = defaultdict(list)
    for n in kg["nodes"]:
        for p in provs(n):
            cid = p.get("chunk_id") or ""
            if cid.startswith("cla::5.1.1.") and n["type"] not in ("TextoOrdenado", "Sujeto"):
                hijos[cid].append((n["id"], "5.1.1" in (p.get("ancestros") or [])))
    hijos_ok = {cid: all(x[1] for x in v) for cid, v in hijos.items()}
    exc_rech = [r for r in (fin_val.get("cla::5.1.1.1") or {}).get("rechazos", []) if r.get("nivel") == "relacion"]
    g["c_condicion_10"] = OrderedDict([
        ("excepcion_de_5_1_1_1", [nodo_breve(n) for n in n5111 if n["type"] == "Excepcion"]),
        ("tipos_en_5_1_1_1", dict(Counter(n["type"] for n in n5111))),
        ("condicion_en_5_1_1_1", sum(1 for n in n5111 if n["type"] == "Condicion")),
        ("nodos_del_intro", [nodo_breve(n) for n in intro if n["type"] not in ("TextoOrdenado", "Sujeto")]),
        ("intro_conserva_definicion_de_alcance", any(n["type"] == "Definicion" and "alcance" in norm(n.get("label")) for n in intro)),
        ("hijos_con_nodos", len(hijos)), ("hijos_con_ancestro_5_1_1_en_todos_sus_nodos", sum(hijos_ok.values())),
        ("hijos", OrderedDict(sorted((cid, {"nodos": len(v), "todos_con_ancestro_5_1_1": hijos_ok[cid]}) for cid, v in hijos.items()))),
        ("relaciones_rechazadas_en_5_1_1_1", exc_rech),
        ("aristas_de_5_1_1_1", [arista_breve(e, idx) for e in kg["edges"] if "cla::5.1.1.1" in chunks_de(e)
                                 and e["relation"] not in ("establecida_en",)][:40]),
        ("texto", texto_chunk("cla::5.1.1.1"))])
    # d
    enc = {"ctacte::8.3::intro": "Se demostrará con cualquiera de las siguientes alternativas:",
           "ctacte::8.4::intro": "Se demostrará con cualquiera de las siguientes alternativas:",
           "ctacte::6.4.7::intro": "se observará el siguiente proceso:"}
    dd = OrderedDict()
    for cid, h in enc.items():
        ns = [n for n in kg["nodes"] if cid in chunks_de(n) and n["type"] not in ("TextoOrdenado", "Sujeto")]
        oblig = [n for n in ns if n["type"] == "Obligacion"]
        solo_enc = [n["id"] for n in oblig if norm(h) in norm((n.get("properties") or {}).get("descripcion") or n.get("label"))
                    and len(norm((n.get("properties") or {}).get("descripcion") or "")) <= len(norm(h)) + 40]
        dd[cid] = OrderedDict([("en_el_grafo", cid.split("::")[0] in tos_g), ("nodos", [nodo_breve(n) for n in ns]),
                               ("obligaciones", len(oblig)), ("obligaciones_cuyo_contenido_es_el_encabezado (regla)", solo_enc),
                               ("texto", texto_chunk(cid))])
    g["d_bkl_0035_0039"] = dd
    # f
    um = [u for n in kg["nodes"] for u in ((n.get("properties") or {}).get("umbrales") or []) if isinstance(u, dict)]
    g["f_umbrales"] = OrderedDict([("elementos_de_umbral", len(um)),
                                   ("comparacion_asumida", sum(1 for u in um if u.get("regla_comparacion") == "comparacion_asumida"
                                                               or u.get("comparacion_asumida"))),
                                   ("por_regla", dict(sorted(Counter(u.get("regla_comparacion") for u in um).items(), key=lambda x: str(x[0])))),
                                   ("plazos_sin_marcador", sum(1 for u in um if u.get("regla_comparacion") == "sin_marcador_plazo"))])
    # g
    tos_nodos = [n for n in kg["nodes"] if n["type"] == "TextoOrdenado"]
    g["g_texto_ordenado"] = OrderedDict([("n", len(tos_nodos)),
                                         ("nodos", [{"id": n["id"], "version": (n.get("properties") or {}).get("version"),
                                                     "materia": (n.get("properties") or {}).get("materia")} for n in tos_nodos]),
                                         ("sin_version", sum(1 for n in tos_nodos if not (n.get("properties") or {}).get("version"))),
                                         ("sin_materia", sum(1 for n in tos_nodos if not (n.get("properties") or {}).get("materia"))),
                                         ("reporte", rep.get("texto_ordenado_version_materia"))])
    # h
    om = jsonl(d / "r2" / "omisiones.jsonl")
    g["h_omisiones"] = OrderedDict([("filas", len(om)), ("por_categoria", dict(sorted(Counter(o.get("categoria") for o in om).items(), key=lambda x: str(x[0])))),
                                    ("por_tramo_verificado", dict(sorted(Counter(o.get("tramo_verificado") for o in om).items(), key=lambda x: str(x[0])))),
                                    ("reporte", rep.get("omisiones")),
                                    ("item_LN_7", {x: items.get("LN-7", {}).get(x) for x in ("estado", "detalle")})])
    # i
    der = leer(d / "r2" / "aristas_derivadas_cola_humana.json")
    nodos_p1 = {n["id"] for n in kg["nodes"] if set(parte1) & chunks_de(n)}
    g["i_derivadas_cola"] = OrderedDict([("aristas", len(der)), ("por_predicado", dict(sorted(Counter(x["relation"] for x in der).items()))),
                                         ("que_tocan_la_parte1", sum(1 for x in der if set(x.get("nodo_de_la_cola") or []) & nodos_p1)),
                                         ("reporte", rep.get("aristas_derivadas_que_tocan_un_nodo_solo_de_la_cola"))])
    # j
    ops = [n for n in kg["nodes"] if n["type"] == "Operacion"]
    multi = [n["id"] for n in ops if len({(p.get("to"), p.get("punto")) for p in provs(n) if p.get("rol_documental") != "esqueleto"}) > 1]
    g["j_operacion_un_punto"] = OrderedDict([("operaciones", len(ops)), ("con_mas_de_un_punto", len(multi)), ("ids", multi)])
    # k
    cl = Counter(kk for n in kg["nodes"] for kk in (n.get("properties_no_definidas") or {}))
    cuatro = ("modalidad", "consecuencia", "modalidad_clasificada", "copia_nota_e3")
    g["k_properties_no_definidas"] = OrderedDict([("nodos_con_la_clave", len([n for n in kg["nodes"] if n.get("properties_no_definidas")])),
                                                  ("las_cuatro", {c: cl.get(c, 0) for c in cuatro}),
                                                  ("las_demas", {c: v for c, v in sorted(cl.items()) if c not in cuatro})])
    # m
    mm = OrderedDict()
    for cid in ("docvig::3.3::cierre", "ctacte::7.3.1.5", "lingob::2.3.2.2"):
        ns = [n for n in kg["nodes"] if cid in chunks_de(n) and n["type"] not in ("TextoOrdenado",)]
        es = [e for e in kg["edges"] if cid in chunks_de(e) and e["relation"] != "establecida_en"]
        mm[cid] = OrderedDict([("en_el_grafo", cid.split("::")[0] in tos_g), ("nodos", [nodo_breve(n) for n in ns]),
                               ("aristas", [arista_breve(e, idx) for e in es]), ("texto", texto_chunk(cid))])
    g["m_bkl_0032_0033_0036"] = mm
    # n
    lp = [e for e in kg["edges"] if e["relation"] in ("limita", "prohibe")]
    g["n_bkl_0038"] = OrderedDict([("por_predicado_y_coherencia", {f"{r}|{c}": v for (r, c), v in sorted(
        Counter((e["relation"], e.get("coherencia_tipo_predicado")) for e in lp).items(), key=lambda x: (x[0][0], str(x[0][1])))}),
        ("incoherentes", [arista_breve(e, idx) | {"tipo_restriccion": (idx[e["source"]].get("properties") or {}).get("tipo"),
                                                  "label_source": idx[e["source"]].get("label"), "label_target": idx[e["target"]].get("label")}
                          for e in lp if e.get("coherencia_tipo_predicado") == "incoherente"]),
        ("en_los_tres_chunks_de_r2a", OrderedDict((cid, [arista_breve(e, idx) | {"tipo_restriccion": (idx[e["source"]].get("properties") or {}).get("tipo"),
                                                                                  "label_source": idx[e["source"]].get("label")}
                                                         for e in lp if cid in chunks_de(e)])
                                                  for cid in ("cap::6.2.1.4", "ext::3.5.6.6", "cap::4.3.3.1")))])
    # o (evidencia por caso: aristas de sujeto extraídas en el subárbol del punto del triage)
    casos = OrderedDict([("BKL-0009 T1", ("cap", "2.5")), ("BKL-0010 T2", ("ext", "14.5")), ("BKL-0011 T3", ("ric", "3.1")),
                         ("BKL-0012 T4", ("ext", "13.4")), ("BKL-0013 T5", ("ext", ("14.5", "3.17", "3.18", "9.7"))),
                         ("BKL-0014 T6", ("ext", "14.1")), ("BKL-0015 T7", ("ext", "3.17")), ("BKL-0016 T8", ("ext", "3.18"))])
    oo = OrderedDict()
    for caso, (to, pts) in casos.items():
        pts = pts if isinstance(pts, tuple) else (pts,)
        # la arista se ubica por su propia procedencia (el chunk donde se extrajo la relación)
        es = [e for e in kg["edges"] if e["relation"] in ("aplica_a", "ejecuta") and e.get("rol_fuente") != "esqueleto"
              and any(p.get("to") == to and any(str(p.get("punto")) == q or str(p.get("punto")).startswith(q + ".") for q in pts)
                      for p in provs(e))]
        oo[caso] = OrderedDict([("en_el_grafo", to in tos_g), ("aristas_de_sujeto", len(es)),
                                ("por_sujeto", dict(sorted(Counter(e["target"] for e in es).items()))),
                                ("por_mencion_y_sujeto", dict(sorted(Counter(f"{norm(e.get('sujeto_mencion'))} -> {e['target']}" for e in es).items()))),
                                ("aristas", [arista_breve(e, idx) for e in es])])
    g["o_patrones_de_sujeto"] = oo
    # p (rol de ctacor: miembro_de hacia el rol y excepciones del catálogo)
    roles = [n for n in kg["nodes"] if n["type"] == "Sujeto" and "ctacor" in n["id"]]
    g["p_bkl_0028_ctacor"] = OrderedDict([("ctacor_en_el_grafo", "ctacor" in tos_g),
                                          ("nodos_sujeto_ctacor", [nodo_breve(n) for n in roles]),
                                          ("miembro_de_hacia_esos_nodos", [arista_breve(e, idx) for e in kg["edges"]
                                                                           if e["relation"] == "miembro_de" and e["target"] in {n["id"] for n in roles}])])
    # q
    reg = jsonl(d / "r2" / "no_mapeados_sujetos.jsonl")
    hit = [r for r in reg if "importador" in norm(json.dumps(r, ensure_ascii=False))]
    g["q_bkl_0021"] = OrderedDict([("filas_del_registro", len(reg)), ("filas_que_mencionan_importador", hit),
                                   ("nodo_en_el_grafo", "Sujeto_propuesto_entidad_nominada_por_el_importador_para_realizar_seguimiento_de_oficializaciones" in idx),
                                   ("propuestos_con_importador", [n["id"] for n in kg["nodes"] if n["type"] == "Sujeto" and "importador" in n["id"]])])
    res["por_grafo"][k] = g

Path(a.out).parent.mkdir(parents=True, exist_ok=True)
Path(a.out).write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("escrito:", a.out)
