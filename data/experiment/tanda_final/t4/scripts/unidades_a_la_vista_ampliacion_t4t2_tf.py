"""B6.1, tanda final, T4, segundo tramo, punto 5 del «seguí»: suma las unidades de la ampliación a
data/experiment/tanda_final/t3/muestras/unidades_a_la_vista_T4.json, con la regla de T3 (t3/scripts/unidades_a_la_vista_tf.py, copiado:
las funciones y la regla, línea por línea iguales), antes de cualquier sorteo de las FICHAS.
  - Recalcula la lista con las nueve muestras: las ocho de T3 (en <material de T3>) y la ampliación de las aceptadas no ítems
    (aceptadas:no_items:ampliacion, en <material de la ampliación>). Antes de escribir, controla que las ocho entradas de T3 den lo mismo
    que en la lista vigente (todo salvo la hora), y que la lista vigente tenga el sha256 del «seguí» (06a126ed…).
  - La regla, la del punto 7.6 del «seguí» de T3: por muestra, el chunk_id de cada unidad cuya extracción aparece en el material y qué
    versión muestra; la unidad de cada ficha de unidad (final) o de cola (primera); de un nodo que muestra una ficha, todas las unidades
    de su procedencia; de una arista, las de sus dos nodos. Como información, la regla del T4 de la tanda 1 (punto 1.1).
Uso: python3 -I -B unidades_a_la_vista_ampliacion_t4t2_tf.py <raíz> <material de T3> <material de la ampliación> <doble_corrida_tf.json>
       <lista vigente> <salida.json>
"""
import hashlib
import json
import sys
from collections import Counter, OrderedDict
from datetime import datetime
from pathlib import Path

sys.dont_write_bytecode = True
RAIZ, MAT, MATA, DC, VIG, OUT = (Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve(), Path(sys.argv[3]).resolve(), Path(sys.argv[4]),
                                 Path(sys.argv[5]), Path(sys.argv[6]))
VIG_SHA = "06a126ed487f4ab9fc41b14d4a8c2d757dcb0706d578edcfdc9382fc70d8af5e"
KG = RAIZ / "data/experiment/reextraccion_v2/corpus_tanda_final/ens_98_r2b_sincola/r2/kg.json"
dc = json.loads(DC.read_text(encoding="utf-8"))["doble_corrida"]["tf98_sincola"]
assert dc["kg_sha256"][0] == dc["kg_sha256"][1] and dc["carpeta"].endswith("ens_98_r2b_sincola")
KG_SHA = dc["kg_sha256"][0]
MUESTRAS = ["cola", "aceptadas:items", "aceptadas:no_items", "vigilancia:2", "vigilancia:7", "vigilancia:1", "vigilancia:3",
            "observacion:12", "aceptadas:no_items:ampliacion"]
DIR = {m: (MATA if m.endswith(":ampliacion") else MAT) for m in MUESTRAS}


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


kgb = KG.read_bytes()
assert sha(kgb) == KG_SHA
kg = json.loads(kgb)
nodos = {n["id"]: n for n in kg["nodes"]}
i3, i4 = (json.loads((MAT / n).read_text(encoding="utf-8")) for n in ("material_t4_t3f_tf.json", "material_t4t1_tf.json"))
i5 = json.loads((MATA / "material_ampliacion_t4t2_tf.json").read_text(encoding="utf-8"))
assert set(i3["muestras"]) | set(i4["muestras"]) | set(i5["muestras"]) == set(MUESTRAS)
assert i3["grafo_sha256"] == i4["grafo_sha256"] == i5["grafo_sha256"] == KG_SHA
vigb = VIG.read_bytes()
assert sha(vigb) == VIG_SHA, "la lista vigente no tiene el sha256 del «seguí»"
vig = json.loads(vigb)
hora = datetime.now().astimezone().isoformat(timespec="seconds")
assert datetime.fromisoformat(hora) > max(datetime.fromisoformat(i3["hora"]), datetime.fromisoformat(i4["hora"]),
                                          datetime.fromisoformat(i5["hora"]))


def unidades_de(nid: str) -> set:
    return {p["chunk_id"] for p in (nodos[nid].get("provenances") or []) if p.get("chunk_id")}


def suma_1_1(nid: str) -> bool:
    t = nodos[nid]["type"]
    return not (t == "TextoOrdenado" or (t == "Sujeto" and len(unidades_de(nid)) > 1))


def nodos_de_la_ficha(x: dict) -> set:
    if "nodos" in x and "aristas" in x:                      # ficha de unidad (T3)
        return {n["id"] for n in x["nodos"]} | {a[k]["id"] for a in x["aristas"] for k in ("source", "target")}
    if "nodo" in x:                                          # ficha de (1)
        return {x["nodo"]["id"]} | {a["otro_nodo"]["id"] for a in x["aristas"]}
    if "grupo" in x:                                         # ficha de (3)
        return {n["id"] for n in x["nodos"]}
    return {x["origen"]["id"], x["destino"]["id"]}           # ficha de arista


def aristas_de_la_ficha(x: dict) -> list:
    if "nodo" in x:
        return [a.get("procedencia", {}).get("chunk_id") for a in x["aristas"]]
    if "origen" in x:
        return [x["arista"].get("procedencia", {}).get("chunk_id")]
    return []


res = OrderedDict([("hora", hora), ("grafo_sha256", KG_SHA),
                   ("material_t4_t3f_tf_sha256", sha((MAT / "material_t4_t3f_tf.json").read_bytes())),
                   ("material_t4t1_tf_sha256", sha((MAT / "material_t4t1_tf.json").read_bytes())),
                   ("material_ampliacion_t4t2_tf_sha256", sha((MATA / "material_ampliacion_t4t2_tf.json").read_bytes())),
                   ("regla", "la del punto 7.6 del «seguí» de T3: la unidad de cada ficha de unidad (final) o de cola (primera); de un "
                             "nodo que muestra una ficha, todas las unidades de su procedencia (final); de una arista, las de sus dos nodos"),
                   ("muestras", OrderedDict())])
union, union_11 = {}, set()
for m in MUESTRAS:
    nom = m.replace(":", "_")
    fichas = [json.loads(x) for x in (DIR[m] / nom / f"fichas_{nom}.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
    vis, por = {}, {}
    r11 = set()
    no_suman_11 = Counter()
    aristas_fuera = []

    def poner(cid: str, version: str, razon: str) -> None:
        vis.setdefault(cid, set()).add(version)
        por.setdefault(cid, set()).add(razon)
    for f in fichas:
        x = f["material"]
        if "entidades" in x:                                 # cola: primer intento
            poner(f["id"], "primera", "ficha de cola")
            r11.add(f["id"])
            continue
        if "nodos" in x and "aristas" in x:
            poner(f["id"], "final", "ficha de unidad")
            r11.add(f["id"])
        for nid in nodos_de_la_ficha(x):
            for cid in unidades_de(nid):
                poner(cid, "final", nodos[nid]["type"])
            if suma_1_1(nid):
                r11 |= unidades_de(nid)
            else:
                no_suman_11[nodos[nid]["type"] + (" (más de una unidad)" if nodos[nid]["type"] == "Sujeto" else "")] += 1
        aristas_fuera += [c for c in aristas_de_la_ficha(x) if c and c not in vis]
    filas = [{"chunk_id": c, "version": ("las dos" if len(vis[c]) == 2 else next(iter(vis[c]))), "por": sorted(por[c])}
             for c in sorted(vis)]
    res["muestras"][m] = OrderedDict([
        ("fichas", len(fichas)), ("unidades_a_la_vista", len(filas)), ("por_version", dict(Counter(r["version"] for r in filas))),
        ("por_razon", dict(Counter(z for r in filas for z in r["por"]).most_common())),
        ("informacion_con_la_regla_1_1_de_la_tanda_1", len(r11)),
        ("informacion_nodos_que_no_suman_con_la_regla_1_1", dict(no_suman_11.most_common())),
        ("informacion_aristas_con_su_unidad_fuera_de_la_lista", len(aristas_fuera)),
        ("unidades", filas)])
    for c, v in vis.items():
        union.setdefault(c, set()).update(v)
    union_11 |= r11
res["todas_las_muestras"] = OrderedDict([
    ("unidades_a_la_vista", len(union)),
    ("por_version", dict(Counter("las dos" if len(v) == 2 else next(iter(v)) for v in union.values()))),
    ("informacion_con_la_regla_1_1_de_la_tanda_1", len(union_11))])
iguales = {m: res["muestras"][m] == vig["muestras"][m] for m in MUESTRAS[:8]}
assert all(iguales.values()), iguales
nuevas = sorted({r["chunk_id"] for r in res["muestras"]["aceptadas:no_items:ampliacion"]["unidades"]}
                - {r["chunk_id"] for m in MUESTRAS[:8] for r in vig["muestras"][m]["unidades"]})
res["ampliacion"] = OrderedDict([
    ("lista_anterior_sha256", VIG_SHA), ("lista_anterior_hora", vig["hora"]),
    ("las_ocho_muestras_de_T3_dan_lo_mismo_que_en_la_lista_anterior", all(iguales.values())),
    ("unidades_a_la_vista_antes", vig["todas_las_muestras"]["unidades_a_la_vista"]),
    ("unidades_que_suma_la_ampliacion", len(nuevas)),
    ("unidades_a_la_vista_despues", res["todas_las_muestras"]["unidades_a_la_vista"])])
assert res["ampliacion"]["unidades_a_la_vista_antes"] + len(nuevas) == res["ampliacion"]["unidades_a_la_vista_despues"]
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for m, x in res["muestras"].items():
    print(f"{m}: {x['fichas']} fichas → {x['unidades_a_la_vista']} unidades {x['por_version']} {x['por_razon']}; con la regla 1.1 "
          f"{x['informacion_con_la_regla_1_1_de_la_tanda_1']} (no suman {x['informacion_nodos_que_no_suman_con_la_regla_1_1']}); aristas "
          f"con su unidad fuera {x['informacion_aristas_con_su_unidad_fuera_de_la_lista']}")
print("todas:", dict(res["todas_las_muestras"]), "| ampliación:", dict(res["ampliacion"]), "| hora", hora, "| sha256", sha(OUT.read_bytes()))
