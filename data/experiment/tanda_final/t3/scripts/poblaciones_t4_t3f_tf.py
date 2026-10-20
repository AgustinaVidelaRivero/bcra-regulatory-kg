"""B6.1, tanda final, T3, punto 7.1 y 7.2: la población por celda de la cola, de las aceptadas (ítems y no ítems) y de las vigilancias
(2) y (7), con data/experiment/tanda1/t3/scripts/poblaciones_t4_t3f.py copiado y adaptado a la tanda final (pre-registro de la tanda
final, §6; pre-registro de la tanda 1, §5.4 y §5.4 bis, punto 2). Solo lee; corre sobre una copia. No lee ninguna unidad ni marca nada:
arma listas de ids. Las vigilancias (1) y (3) y la observación (12) las arma poblaciones_t4t1_tf.py, con el mecanismo del T4 de la
tanda 1.

  - Celda: la clase sale del TO (`categoria` del manifiesto de extracción, tanda_final_98tos_r2b.json: RI → RI, no-RI → NG) y el modo,
    de su `modo_lectura` (sin_raiz o el resto). Control: los TOs sin_raiz del manifiesto son los 26 que tienen `modo_lectura` sin_raiz en
    segmentacion_oficial_e0r2/s2/cifras/tanda_final_S2c.json, y su categoría es la de esa lista. Una unidad va a la celda de su TO; un
    nodo, a la de su unidad de procedencia primaria (`provenance`); una arista, a la de su nodo de origen (§5.4 bis, punto 2, v8c).
  - El grafo es el de la tanda entera sin la cola (KG-TandaFinal-r2b-sincola, ens_98_r2b_sincola; su sha256, el de la doble corrida),
    salvo la cola. La última versión de cada unidad es la de corpus_tanda_final/salida_r2b/<to>/finales.jsonl; de los estados solo se
    usa si es de la cola (cola_humana*) o una aceptada (los tres estados de aceptación juntos, ACEPTADOS de r0_f2_cifras_enmienda7.py);
    no se cuenta ni se reporta el desglose de las aceptadas.
  - Las muestras:
      cola: las unidades de la cola;
      aceptadas:items y aceptadas:no_items: las unidades aceptadas, por `es_item` de prompt_r2b.py sobre el chunk de la E0 (una parte por
        corte de E1 usa el chunk de su unidad);
      vigilancia:2: las unidades aceptadas cuya extracción final (extracciones_finales_<to>.jsonl, última por unidad) no tiene error y
        tiene 0 relaciones aceptadas (la (2), en la extracción final; registro, §29);
      vigilancia:7: las aristas `ejecuta` cuyo origen es un Sujeto_rol_alcance_<to>.
    El id de una arista es la tripla (source, relation, target), única en el grafo (se controla).
Uso: python3 -I -B poblaciones_t4_t3f_tf.py <raíz> <doble_corrida_tf.json> <salida.json>
"""
import hashlib
import json
import sys
from collections import OrderedDict
from datetime import datetime
from pathlib import Path

RAIZ, DC, OUT = Path(sys.argv[1]).resolve(), Path(sys.argv[2]), Path(sys.argv[3])
X = RAIZ / "data/experiment/reextraccion_v2"
sys.path.insert(0, str(X / "e1_extractor"))
import prompt_r2b  # noqa: E402

assert Path(prompt_r2b.__file__).resolve().is_relative_to(RAIZ)
MAN = X / "manifiestos/tanda_final_98tos_r2b.json"
LISTA = RAIZ / "data/experiment/segmentacion_oficial_e0r2/s2/cifras/tanda_final_S2c.json"
KG = X / "corpus_tanda_final/ens_98_r2b_sincola/r2/kg.json"
dc = json.loads(DC.read_text(encoding="utf-8"))["doble_corrida"]["tf98_sincola"]
assert dc["kg_sha256"][0] == dc["kg_sha256"][1] and dc["carpeta"].endswith("ens_98_r2b_sincola")
KG_SHA = dc["kg_sha256"][0]
SAL = X / "corpus_tanda_final/salida_r2b"
E0 = X / "e0_chunking/salida_tanda_final_r2b"
ACEPTADOS = ("completo_ok_directo", "aceptado_con_residuales", "aceptado_tras_reintento")
CELDAS = ["RI:sin_raiz", "RI:resto", "NG:sin_raiz", "NG:resto"]


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def canon(x) -> bytes:
    return json.dumps(x, ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def lineas(p: Path) -> list:
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()] if p.exists() else []


man = json.loads(MAN.read_text(encoding="utf-8"))
celda_to = {}
for t in man["tos"]:
    clase = {"RI": "RI", "no-RI": "NG"}[t["categoria"]]
    celda_to[t["id"]] = f"{clase}:{'sin_raiz' if t['modo_lectura'] == 'sin_raiz' else 'resto'}"
sr = {to for to, c in celda_to.items() if c.endswith("sin_raiz")}
filas_s2 = json.loads(LISTA.read_text(encoding="utf-8"))["filas"]
sr_lista = {to for to, f in filas_s2.items() if f.get("modo_lectura") == "sin_raiz"}
assert sr == sr_lista and len(sr) == 26, (sorted(sr ^ sr_lista), len(sr))
assert set(filas_s2) == set(celda_to) and all(
    {"regimen_informativo": "RI", "normativa_general": "NG"}[filas_s2[to]["categoria"]] == celda_to[to].split(":")[0] for to in celda_to)
kgb = KG.read_bytes()
assert sha(kgb) == KG_SHA, "el grafo de la tanda sin la cola no da su sha256"
kg = json.loads(kgb)
nodos = {n["id"]: n for n in kg["nodes"]}


def to_de_chunk(cid: str) -> str:
    return cid.split("::", 1)[0]


def celda_nodo(n: dict):
    p = n.get("provenance") or {}
    to = p.get("to") or (to_de_chunk(p["chunk_id"]) if p.get("chunk_id") else None)
    return celda_to.get(to)


ult = {}
for to in celda_to:
    for r in lineas(SAL / to / "finales.jsonl"):
        ult[r["chunk_id"]] = r
cola_ids = sorted(c for c, r in ult.items() if str(r["estado"]).startswith("cola_humana"))
acept_ids = sorted(c for c, r in ult.items() if r["estado"] in ACEPTADOS)
chunks = {}
for to in celda_to:
    d = json.loads((E0 / f"chunks_{to}.json").read_text(encoding="utf-8"))
    chunks.update({c["id"]: c for c in (d["chunks"] if isinstance(d, dict) else d)})


def base_de(c: str) -> str:
    """El chunk de la E0 de una unidad: el propio si está en la E0; si no, una parte por corte de E1 usa el chunk de su unidad (se
    quita solo el último ::parteN)."""
    b = c if c in chunks else c.rsplit("::parte", 1)[0]
    assert b in chunks, c
    return b


es_item = {c: bool(prompt_r2b.es_item(chunks[base_de(c)])) for c in acept_ids}
partes_por_corte = sorted(c for c in acept_ids + cola_ids if c not in chunks)
final_e1 = {}
for to in celda_to:
    for r in lineas(SAL / to / f"extracciones_finales_{to}.jsonl"):
        final_e1[r["chunk_id"]] = r
vac = sorted(c for c in acept_ids if c in final_e1 and not final_e1[c].get("error")
             and not ((final_e1[c].get("validacion") or {}).get("relaciones")))
trip = lambda e: (e["source"], e["relation"], e["target"])  # noqa: E731
assert len({trip(e) for e in kg["edges"]}) == len(kg["edges"]), "triplas repetidas"
v7 = sorted(trip(e) for e in kg["edges"] if e["relation"] == "ejecuta" and str(e["source"]).startswith("Sujeto_rol_alcance_"))


def por_celda(ids, celda) -> OrderedDict:
    out = OrderedDict((c, []) for c in CELDAS)
    sin = []
    for i in ids:
        c = celda(i)
        (out[c] if c in out else sin).append(i)
    if sin:
        raise SystemExit(f"FRENO: {len(sin)} elementos sin celda (primeros: {sin[:5]})")
    return out


cel_u = lambda c: celda_to[to_de_chunk(c)]  # noqa: E731
cel_a = lambda t: celda_nodo(nodos[t[0]])  # noqa: E731
MUESTRAS = OrderedDict([
    ("cola", ("unidad", cola_ids, cel_u)),
    ("aceptadas:items", ("unidad", [c for c in acept_ids if es_item[c]], cel_u)),
    ("aceptadas:no_items", ("unidad", [c for c in acept_ids if not es_item[c]], cel_u)),
    ("vigilancia:2", ("unidad", vac, cel_u)),
    ("vigilancia:7", ("arista", v7, cel_a))])
res = OrderedDict([("hora", datetime.now().astimezone().isoformat(timespec="seconds")),
                   ("grafo", {"ruta": str(KG.relative_to(RAIZ)), "kg_sha256": KG_SHA}),
                   ("manifiesto", {"ruta": str(MAN.relative_to(RAIZ)), "sha256": sha(MAN.read_bytes())}),
                   ("lista_S2c", {"ruta": str(LISTA.relative_to(RAIZ)), "sha256": sha(LISTA.read_bytes())}),
                   ("celda_por_to", dict(sorted(celda_to.items()))),
                   ("tos_por_celda", {c: sum(1 for v in celda_to.values() if v == c) for c in CELDAS}),
                   ("unidades_en_finales", len(ult)), ("cola", len(cola_ids)), ("aceptadas", len(acept_ids)),
                   ("partes_por_corte_que_usan_el_chunk_de_su_unidad", partes_por_corte),
                   ("muestras", OrderedDict())])
for m, (tipo, ids, cel) in MUESTRAS.items():
    pc = por_celda(ids, cel)
    lista_c = OrderedDict((c, [list(x) if isinstance(x, tuple) else x for x in v]) for c, v in pc.items())
    res["muestras"][m] = OrderedDict([
        ("elemento", tipo), ("N", len(ids)), ("N_por_celda", {c: len(v) for c, v in pc.items()}),
        ("entera_sin_celdas", len(ids) <= 30),
        ("pesos", {c: (len(v) / len(ids) if ids else None) for c, v in pc.items()}),
        ("sha256_ids_por_celda", sha(canon(lista_c))), ("ids_por_celda", lista_c)])
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("hora", res["hora"], "| unidades en finales", len(ult), "| cola", len(cola_ids), "| aceptadas", len(acept_ids))
for m, v in res["muestras"].items():
    print(f"{m}: N {v['N']} {v['N_por_celda']} entera {v['entera_sin_celdas']} sha256 {v['sha256_ids_por_celda']}")
print("sha256", sha(OUT.read_bytes()))
