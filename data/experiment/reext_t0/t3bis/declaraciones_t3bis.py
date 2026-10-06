"""U-REEXT-T0, T3-bis, decisión 5: las declaraciones con los textos de la norma (E0 r2b) y de los nodos (grafos r2b de
T3-bis) pegados, más las listas que pide el freno (propuestos, filas renombradas, umbrales con la unidad del rótulo,
marcas de S18 y aristas quitadas). Solo lee los grafos, sus reportes y registros, la E0 r2b y la suite de T3-bis;
escribe el Markdown de --out. Determinístico, USD 0.

Uso (desde la raíz del repo o de una copia): python -B data/experiment/reext_t0/t3bis/declaraciones_t3bis.py --out ARCHIVO.md
"""
import argparse
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[4]
T0 = RAIZ / "data" / "experiment" / "reextraccion_v2" / "corpus_tanda0"
E0 = RAIZ / "data" / "experiment" / "reextraccion_v2" / "e0_chunking" / "salida_tanda0_r2b"
SALIDA = RAIZ / "data" / "experiment" / "reext_t0" / "t3bis" / "salida"
GRAFOS = ("diez", "desarrollo")

ap = argparse.ArgumentParser()
ap.add_argument("--out", type=Path, required=True)
a = ap.parse_args()


def jl(p: Path) -> list:
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]


G = {}
for k in GRAFOS:
    d = T0 / f"ens_{k}_r2b" / "r2"
    kg = json.loads((d / "kg.json").read_text(encoding="utf-8"))
    G[k] = {"kg": kg, "by": {n["id"]: n for n in kg["nodes"]},
            "rep": json.loads((d / "reporte_ensamblado_r2.json").read_text(encoding="utf-8")),
            "reg": jl(d / "no_mapeados_sujetos.jsonl"), "quitadas": jl(d / "propuestos_descartados_aristas_quitadas.jsonl"),
            "nc": json.loads((d / "umbral_no_cuantificable.json").read_text(encoding="utf-8")),
            "suite": json.loads((SALIDA / f"suite_regresion_entrada_sellada_{k}_r2b.json").read_text(encoding="utf-8"))}
_chunks = {}


def texto_e0(cid: str) -> str:
    to = cid.split("::")[0]
    if to not in _chunks:
        d = json.loads((E0 / f"chunks_{to}.json").read_text(encoding="utf-8"))
        _chunks[to] = {c["id"]: c for c in (d["chunks"] if isinstance(d, dict) else d)}
    return " ".join(_chunks[to][cid]["texto"].split())


def nodos(k: str, cid: str, tipo: str) -> list:
    return [n for n in G[k]["kg"]["nodes"] if n["type"] == tipo and any(p.get("chunk_id") == cid for p in n["provenances"])]


def tramo(n: dict, cid: str):
    return next((p.get("tramo") for p in n["provenances"] if p.get("chunk_id") == cid and p.get("tramo")), None)


def desc_arista(e: dict, by: dict) -> str:
    return (f"{e['provenance'].get('chunk_id')} desde «{by[e['source']]['label']}», "
            f"mención «{e.get('sujeto_mencion')}»")


def desc_fila(f: dict) -> str:
    return f"{f['chunk_id']} {f['estado']} {f['motivo']}"


def item(k: str, i: str) -> dict:
    return next(x for x in G[k]["suite"]["items"] if x["id"] == i)


L = ["# U-REEXT-T0, T3-bis: declaraciones de la decisión 5 y listas del freno", "",
     f"Grafos: diez `{G['diez']['rep']['sha256_kg']}`, desarrollo `{G['desarrollo']['rep']['sha256_kg']}`. Textos de la norma: "
     "E0 r2b (`salida_tanda0_r2b`), con los saltos de línea colapsados. Lo generó "
     "`data/experiment/reext_t0/t3bis/declaraciones_t3bis.py`.", ""]

# RT-C6-1 y RT-C6-2
cid = "pro::1.1.2.5"
exc = nodos("diez", cid, "Excepcion")[0]
dfn = nodos("diez", cid, "Definicion")[0]
L += ["## RT-C6-1 y RT-C6-2: siguen en persiste, declarados", "",
      "Declaración: error de fidelidad del modelo en la descripción, conector «o» → «y»; tramo fiel.", "",
      f"- Norma (`{cid}`): «{texto_e0(cid)}»",
      f"- Excepcion `{exc['id']}`, descripción: «{exc['properties'].get('descripcion')}»",
      f"- Su tramo: «{tramo(exc, cid)}»",
      f"- Definicion del mismo chunk, descripción: «{dfn['properties'].get('descripcion')}»",
      f"- Suite (diez y desarrollo): RT-C6-1 «{item('diez', 'RT-C6-1')['estado']}» ({item('diez', 'RT-C6-1')['detalle']}); "
      f"RT-C6-2 «{item('diez', 'RT-C6-2')['estado']}».", ""]
# RT-C5-3
cid = "cla::6.5.2.2"
n5 = [n for n in nodos("diez", cid, "Definicion") if n["id"].startswith("Definicion_categoria_en_negociacion")][0]
t = texto_e0(cid)
i = t.find("Incluye")
L += ["## RT-C5-3: sigue en persiste, declarado", "",
      "Declaración: persiste por paráfrasis sin cambio de sentido (el ítem compara literalmente un gold escrito para la "
      "extracción textual).", "",
      f"- Norma (`{cid}`): «{t[i:t.find('.', t.find('6.5.2.1', i) + 7) + 1]}»",
      "- Gold del ítem (`scripts/regression_kg.py`, `t_rt_c5_3`): «antes de los 60 dias» y «mora», en el texto normalizado del nodo N5.",
      f"- Definicion `{n5['id']}`, descripción: «{n5['properties'].get('descripcion')}»",
      f"- Su tramo: «{tramo(n5, cid)}»",
      f"- Suite: «{item('diez', 'RT-C5-3')['estado']}» ({item('diez', 'RT-C5-3')['detalle']}).", ""]
# S18
L += ["## S18: Restricciones limite_cuantitativo con la marca r2b `umbral_no_cuantificable`", "",
      "La marca va en `properties_no_definidas` (NodoR2 y S26 cierran las claves de `properties`). Lista: "
      "`ens_<grafo>_r2b/r2/umbral_no_cuantificable.json`.", ""]
for k in GRAFOS:
    r = G[k]["rep"]["umbral_no_cuantificable"]
    motivos = ", ".join(f"{m}: {v}" for m, v in r["por_motivo"].items())
    L.append(f"- {k}: {len(G[k]['nc']['marcados'])} marcados ({motivos}); "
             f"sin marca con cuantía: {len(G[k]['nc']['sin_marca_con_cuantia'])}; detector `{r['detector_sha256'][:12]}…`; "
             f"lista de tablas forzadas `{r['tablas_forzadas_sha256'][:12]}…`.")
L.append("")
for x in G["diez"]["nc"]["marcados"]:
    extra = f"; tablas: {', '.join(x['tablas_con_cuantias'])}" if x["tablas_con_cuantias"] else ""
    L.append(f"  - `{x['id']}` ({', '.join(x['chunks'])}; {x['motivo']}{extra}): «{x['descripcion']}»")
solo_diez = sorted({x["id"] for x in G["diez"]["nc"]["marcados"]} - {x["id"] for x in G["desarrollo"]["nc"]["marcados"]})
L += [f"  - En desarrollo, los mismos salvo {', '.join('`' + i + '`' for i in solo_diez)} (TO fuera de desarrollo).", ""]
# BKL-0039, BKL-0036, BKL-0028, BKL-0021, T5
cid = "ctacte::6.4.7::intro"
ob = nodos("diez", cid, "Obligacion")[0]
L += ["## BKL-0039: no cierra (prefijo congelado; a la lista de T5)", "",
      f"- Norma (`{cid}`, texto propio de la unidad): «{texto_e0(cid)}»",
      f"- Obligacion `{ob['id']}`, descripción: «{ob['properties'].get('descripcion')}»; tramo: «{tramo(ob, cid)}»", ""]
cid = "lingob::2.3.2.2"
rs = nodos("diez", cid, "Restriccion")[0]
L += ["## BKL-0036: cerrada, con la condición releída sin atarla al tipo (la Restriccion conserva el calificador)", "",
      f"- Norma (`{cid}`): «{texto_e0(cid)}»",
      f"- Restriccion `{rs['id']}`, descripción: «{rs['properties'].get('descripcion')}»",
      f"- Su tramo: «{tramo(rs, cid)}»", "",
      "## BKL-0028: a U-RERESOL-CAT", "",
      "- Sin cambio en estos grafos: el miembro del rol de ctacor se re-adjudica en U-RERESOL-CAT.", ""]
L += ["## BKL-0021: opción (c) por U-RERESOL-CAT; mientras tanto, (d): los dos propuestos siguen en cuarentena", ""]
for k in GRAFOS:
    by = G[k]["by"]
    for pid in sorted(i for i in by if i.startswith("Sujeto_propuesto_la_entidad_nominada")):
        ar = [e for e in G[k]["kg"]["edges"] if e["target"] == pid]
        fi = [f for f in G[k]["reg"] if f.get("id_nodo") == pid]
        L.append(f"- {k}: `{pid}` («{by[pid]['label']}», padre_sugerido `{by[pid]['properties'].get('padre_sugerido')}`): "
                 f"{len(ar)} aplica_a ({'; '.join(desc_arista(e, by) for e in ar)}); "
                 f"{len(fi)} filas ({'; '.join(desc_fila(f) for f in fi)})")
L.append("")
cid = "ext::3.17.2::intro"
L += ["## T5: sin casos (la arista de `ext::3.17.2::intro` sigue al texto)", "",
      f"- Norma (`{cid}`): «{texto_e0(cid)}»"]
for e in G["diez"]["kg"]["edges"]:
    if e["target"] == "Sujeto_entidad_financiera" and e["provenance"].get("chunk_id") == cid:
        s = G["diez"]["by"][e["source"]]
        L.append(f"- `{e['source']}` («{s['label']}») --{e['relation']}--> `Sujeto_entidad_financiera`, mención «{e.get('sujeto_mencion')}», "
                 f"tramo del origen «{tramo(s, cid)}»")
L += ["", "## remite_a: no se toca", "",
      "- Según la nota del 06/10/2026 al pie del mandato (`07ef3c9`): sobre el texto propio de las 2.439 unidades el detector del "
      "perfil r2 encuentra 1.385 citas; r2b registra 1.380 y deja 5 sin registrar. Se declaran, no se corrigen. "
      f"Aristas `remite_a` en T3-bis: diez {sum(1 for e in G['diez']['kg']['edges'] if e['relation'] == 'remite_a')}, "
      f"desarrollo {sum(1 for e in G['desarrollo']['kg']['edges'] if e['relation'] == 'remite_a')}.", ""]
# Propuestos
L += ["## Propuestos (decisión 1): los 7 sin padre de T3, el padre hacia una instancia, los renombrados y los descartados", ""]
for k in GRAFOS:
    d = G[k]["rep"]["propuestos_r2b"]["detalle"]
    L.append(f"- {k}:")
    for x in d["descartados"]:
        L.append(f"  - «{x['mencion']}» (`{x['id']}`, {', '.join(x['tos'])}; padre_sugerido de E1: `{x['padre_sugerido']}`): descartado "
                 f"por mención vacía; {x['aristas_quitadas']} arista quitada, {x['filas_del_registro']} fila con estado «descartado».")
    for x in d["padre_por_defecto"]:
        L.append(f"  - «{x['mencion']}» (`{x['id']}`): padre_por_defecto → `{x['padre_sugerido']}`.")
    for x in d["padre_desde_instancia"] + d["padre_descartado"]:
        L.append(f"  - `{x['id']}`: padre hacia la instancia `{x['instancia']}` → {x.get('padre_sugerido', 'quitado')}.")
    if not d["padre_desde_instancia"] and not d["padre_descartado"]:
        L.append("  - Padre hacia una instancia: 0 después del descarte (el único caso de T3, «se» → `Sujeto_sefyc`, salió con el propuesto).")
    ren = {}
    for f in d["filas_renombradas"]:
        ren.setdefault(f["id_nodo"], []).append(f)
    for i, fs in sorted(ren.items()):
        pl = "filas pasan" if len(fs) != 1 else "fila pasa"
        L.append(f"  - `{i}`: {len(fs)} {pl} de `{fs[0]['id_anterior']}` a este id ({fs[0]['to']}; "
                 f"{', '.join(sorted({f['chunk_id'] for f in fs}))}).")
    L.append(f"  - Aristas quitadas: {len(G[k]['quitadas'])} (`ens_{k}_r2b/r2/propuestos_descartados_aristas_quitadas.jsonl`, insumo de R2 de "
             "U-RERESOL-CAT; sin rol asignado):")
    for q in G[k]["quitadas"]:
        L.append(f"    - {q['archivo']} `{q['chunk_id']}` (punto {q['punto']}): «{q['sujeto_mencion']}» ({q['mencion_verificada']}), "
                 f"{q['relacion']} desde `{q['extremo']}`; tramo del origen «{q['tramo_del_extremo']}».")
L.append("")
# Umbrales con la unidad del rótulo
L += ["## Umbrales que ganan valor por la unidad del rótulo (decisión 2)", ""]
for k in GRAFOS:
    u = G[k]["rep"]["umbrales"]["unidad_desde_rotulo"]
    L.append(f"- {k}: {u['elementos']} elementos, por TO {u['por_to']}:")
    for x in u["nodos"]:
        L.append(f"  - `{x['id']}`: tramo «{x['tramo']}» → {x['valor']} {x['unidad']} {x['moneda']} (rótulo «{x['rotulo']}», `{x['tabla']}`)")
L.append("")
a.out.write_text("\n".join(L), encoding="utf-8")
print("escrito:", a.out, len(L), "líneas")
