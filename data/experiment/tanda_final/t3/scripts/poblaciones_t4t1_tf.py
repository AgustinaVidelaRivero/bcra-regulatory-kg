"""B6.1, tanda final, T3, punto 7.1 y 7.2: la población por celda de las vigilancias (1) y (3) y de la observación (12), con
data/experiment/tanda1/t4/scripts/poblaciones_t4t1.py copiado y adaptado a la tanda final (pre-registro de la tanda final, §6; registro
de decisiones, §29 y §31). Solo lee; corre sobre una copia. No lee ninguna unidad ni marca nada: arma listas de ids.

  - Celda: como en poblaciones_t4_t3f_tf.py. La clase sale de `categoria` del manifiesto de extracción (RI → RI, no-RI → NG) y el modo,
    de `modo_lectura` (sin_raiz o el resto). Un nodo va a la celda de su unidad de procedencia primaria (`provenance`); una arista, a la
    de su nodo de origen; un grupo de la (3), a la de su nodo de id menor (§5.4 bis, punto 2, v8c, del pre-registro de la tanda 1).
  - El grafo es el de la tanda entera sin la cola (KG-TandaFinal-r2b-sincola, ens_98_r2b_sincola; su sha256, el de la doble corrida),
    como sin dividir (enmienda 9, §1, punto 2).
  - vigilancia:1: los nodos Condicion del grafo.
  - vigilancia:3: los grupos de 2 nodos o más de contenido con la misma unidad de procedencia primaria y el mismo tramo normalizado
    (espacios y mayúsculas). El id del grupo son sus ids de nodo ordenados y unidos con «|». El grupo por tramo igual no ve duplicaciones
    con tramos distintos (se declara). El par del deber y el acto regulado queda en la población; el criterio de la §31 es de la lectura.
  - observacion:12: todas las aristas del grafo menos `referencia`, menos `rol_fuente = esqueleto`, menos las `establecida_en` con
    `rol_fuente = derivada_de_procedencia` y menos las `remite_a` ([c1] del tablero, sin `remite_a`; registro, §29). Las
    `establecida_en` sin `rol_fuente` quedan. Control: da las aristas de extracción de la observación (10) del mismo grafo
    (t3/conteos_sin_leer/contado_sin_leer_tf.json). El id de una arista es la tripla (source, relation, target).
  - Como información, al lado: el universo de A4.1 tal cual (todas menos `referencia` y menos el esqueleto) y lo que la §29 le resta.
Uso: python3 -I -B poblaciones_t4t1_tf.py <raíz> <doble_corrida_tf.json> <contado_sin_leer_tf.json> <salida.json>
"""
import hashlib
import json
import re
import sys
from collections import Counter, OrderedDict
from datetime import datetime
from pathlib import Path

sys.dont_write_bytecode = True
RAIZ, DC, CONTADO, OUT = Path(sys.argv[1]).resolve(), Path(sys.argv[2]), Path(sys.argv[3]), Path(sys.argv[4])
X = RAIZ / "data/experiment/reextraccion_v2"
MAN = X / "manifiestos/tanda_final_98tos_r2b.json"
LISTA = RAIZ / "data/experiment/segmentacion_oficial_e0r2/s2/cifras/tanda_final_S2c.json"
KG = X / "corpus_tanda_final/ens_98_r2b_sincola/r2/kg.json"
dc = json.loads(DC.read_text(encoding="utf-8"))["doble_corrida"]["tf98_sincola"]
assert dc["kg_sha256"][0] == dc["kg_sha256"][1] and dc["carpeta"].endswith("ens_98_r2b_sincola")
KG_SHA = dc["kg_sha256"][0]
CELDAS = ["RI:sin_raiz", "RI:resto", "NG:sin_raiz", "NG:resto"]
TIPOS_CONTENIDO = ("Operacion", "Restriccion", "Excepcion", "Obligacion", "Potestad", "Condicion", "Definicion", "Comunicacion")


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def canon(x) -> bytes:
    return json.dumps(x, ensure_ascii=False, separators=(",", ":")).encode("utf-8")


man = json.loads(MAN.read_text(encoding="utf-8"))
celda_to = {}
for t in man["tos"]:
    clase = {"RI": "RI", "no-RI": "NG"}[t["categoria"]]
    celda_to[t["id"]] = f"{clase}:{'sin_raiz' if t['modo_lectura'] == 'sin_raiz' else 'resto'}"
sr = {to for to, c in celda_to.items() if c.endswith("sin_raiz")}
filas_s2 = json.loads(LISTA.read_text(encoding="utf-8"))["filas"]
sr_lista = {to for to, f in filas_s2.items() if f.get("modo_lectura") == "sin_raiz"}
assert sr == sr_lista and len(sr) == 26, (sorted(sr ^ sr_lista), len(sr))
kgb = KG.read_bytes()
assert sha(kgb) == KG_SHA, "el grafo de la tanda sin la cola no da su sha256"
kg = json.loads(kgb)
nodos = {n["id"]: n for n in kg["nodes"]}
assert len(nodos) == len(kg["nodes"]), "ids de nodo repetidos"


def celda_nodo(n: dict):
    p = n.get("provenance") or {}
    to = p.get("to") or (p["chunk_id"].split("::", 1)[0] if p.get("chunk_id") else None)
    return celda_to.get(to)


rf = lambda e: e.get("rol_fuente") or (e.get("properties") or {}).get("rol_fuente")  # noqa: E731
trip = lambda e: (e["source"], e["relation"], e["target"])  # noqa: E731
assert len({trip(e) for e in kg["edges"]}) == len(kg["edges"]), "triplas repetidas"


def es_o12_nuevo(e: dict) -> bool:
    rel = e.get("relation")
    return (rel != "referencia" and rf(e) != "esqueleto" and not (rel == "establecida_en" and rf(e) == "derivada_de_procedencia")
            and rel != "remite_a")


o12 = sorted(trip(e) for e in kg["edges"] if es_o12_nuevo(e))
o12_a41 = sorted(trip(e) for e in kg["edges"] if e.get("relation") != "referencia" and rf(e) != "esqueleto")
cond = sorted(n["id"] for n in kg["nodes"] if n["type"] == "Condicion")
grupos = {}
for n in kg["nodes"]:
    if n["type"] not in TIPOS_CONTENIDO:
        continue
    p = n.get("provenance") or {}
    tr = re.sub(r"\s+", " ", (p.get("tramo") or "")).strip().lower()
    if p.get("chunk_id") and tr:
        grupos.setdefault((p["chunk_id"], tr), []).append(n["id"])
g3 = {"|".join(sorted(v)): sorted(v) for v in grupos.values() if len(v) >= 2}
assert len(g3) == sum(1 for v in grupos.values() if len(v) >= 2), "dos grupos con el mismo id"


def por_celda(ids, celda) -> OrderedDict:
    out = OrderedDict((c, []) for c in CELDAS)
    sin = []
    for i in ids:
        c = celda(i)
        (out[c] if c in out else sin).append(i)
    if sin:
        raise SystemExit(f"FRENO: {len(sin)} elementos sin celda (primeros: {sin[:5]})")
    return out


cel_n = lambda i: celda_nodo(nodos[i])  # noqa: E731
cel_a = lambda t: celda_nodo(nodos[t[0]])  # noqa: E731
cel_g = lambda g: celda_nodo(nodos[g3[g][0]])  # noqa: E731
MUESTRAS = OrderedDict([
    ("vigilancia:1", ("nodo Condicion", cond, cel_n)),
    ("vigilancia:3", ("grupo de nodos", sorted(g3), cel_g)),
    ("observacion:12", ("arista", o12, cel_a))])


def bloque(tipo, ids, cel) -> OrderedDict:
    pc = por_celda(ids, cel)
    lista_c = OrderedDict((c, [list(x) if isinstance(x, tuple) else x for x in v]) for c, v in pc.items())
    return OrderedDict([("elemento", tipo), ("N", len(ids)), ("N_por_celda", {c: len(v) for c, v in pc.items()}),
                        ("entera_sin_celdas", len(ids) <= 30), ("pesos", {c: (len(v) / len(ids) if ids else None) for c, v in pc.items()}),
                        ("sha256_ids_por_celda", sha(canon(lista_c))), ("ids_por_celda", lista_c)])


res = OrderedDict([("hora", datetime.now().astimezone().isoformat(timespec="seconds")),
                   ("grafo", {"ruta": str(KG.relative_to(RAIZ)), "kg_sha256": KG_SHA}),
                   ("manifiesto", {"ruta": str(MAN.relative_to(RAIZ)), "sha256": sha(MAN.read_bytes())}),
                   ("celda_por_to", dict(sorted(celda_to.items()))), ("muestras", OrderedDict())])
for m, (tipo, ids, cel) in MUESTRAS.items():
    res["muestras"][m] = bloque(tipo, ids, cel)
res["muestras"]["vigilancia:3"]["grupos"] = {g: v for g, v in sorted(g3.items())}
res["muestras"]["vigilancia:3"]["nodos_en_grupos"] = sum(len(v) for v in g3.values())
res["muestras"]["vigilancia:3"]["nodos_por_grupo"] = dict(sorted(Counter(len(v) for v in g3.values()).items()))
info = bloque("arista", o12_a41, cel_a)
res["observacion_12_A41_tal_cual_informacion"] = OrderedDict((k, v) for k, v in info.items() if k != "ids_por_celda")
comp = lambda ids: dict(Counter(t[1] for t in ids).most_common())  # noqa: E731
rfs = {trip(e): str(rf(e)) for e in kg["edges"]}
res["composicion_informacion"] = {
    "observacion:12": {"relacion": comp(o12), "rol_fuente": dict(Counter(rfs[t] for t in o12).most_common())},
    "A41_tal_cual": {"relacion": comp(o12_a41), "rol_fuente": dict(Counter(rfs[t] for t in o12_a41).most_common())},
    "restadas_por_la_29_sobre_A41": dict(Counter(f"{t[1]} / rol_fuente {rfs[t]}" for t in set(o12_a41) - set(o12)).most_common())}
o10 = json.loads(CONTADO.read_text(encoding="utf-8"))["grafos"]["tf98_sincola"]["f49_obs10"]
ctl = OrderedDict([("observacion_12_igual_a_la_extraccion_de_la_10", {"universo": len(o12), "obs10_extraccion": o10["extraccion"],
                                                                      "igual": len(o12) == o10["extraccion"]})])
res["controles"] = ctl
assert ctl["observacion_12_igual_a_la_extraccion_de_la_10"]["igual"], ctl
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("hora", res["hora"])
for m, v in res["muestras"].items():
    print(f"{m}: N {v['N']} {v['N_por_celda']} sha256 {v['sha256_ids_por_celda']}")
print(f"A4.1 tal cual (información): N {info['N']} {info['N_por_celda']} sha256 {info['sha256_ids_por_celda']}")
print("restadas sobre A4.1:", res["composicion_informacion"]["restadas_por_la_29_sobre_A41"])
print("controles:", json.dumps(ctl, ensure_ascii=False))
print("sha256", sha(OUT.read_bytes()))
