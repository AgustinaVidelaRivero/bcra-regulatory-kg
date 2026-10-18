"""B6.1, tanda 1, T3, punto 7.1 y 7.2: la población de cada muestra de T4, por celda (pre-registro firmado, §5.4 y §5.4 bis, punto 2).
Solo lee; corre sobre una copia. No lee ninguna unidad ni marca nada: arma listas de ids.

  - Celda: la clase sale del TO (`categoria` del manifiesto de extracción, tanda1_20tos_r2b.json: RI → RI, no-RI → NG) y el modo,
    de su `modo_lectura` (sin_raiz o el resto). Control: los TOs sin_raiz son ceninf, nmcief, ri_ccna y ri_mmsef, y en
    lista_tanda1_S2.json su modo_lectura_e0_corregida es sin_raiz. Una unidad va a la celda de su TO; un nodo, a la de su unidad de
    procedencia primaria (`provenance`); una arista, a la de su nodo de origen (§5.4 bis, punto 2, v8c).
  - El grafo es el evaluado, el sin cola (KG-Tanda1-Veinte-r2b-sincola, 384a6d5b…), salvo la cola. La última versión de cada unidad es
    la de corpus_tanda1/salida_r2b/<to>/finales.jsonl; de los estados solo se usa si es de la cola (cola_humana*) o una aceptada (los
    tres estados de aceptación juntos, ACEPTADOS de r0_f2_cifras_enmienda7.py); no se cuenta ni se reporta el desglose de las aceptadas.
  - Las muestras con definición firmada:
      cola: las unidades de la cola (§5.4 b);
      aceptadas:items y aceptadas:no_items: las unidades aceptadas, por `es_item` de prompt_r2b.py sobre el chunk de la E0 (una parte por
        corte de E1 usa el chunk de su unidad; un chunk de la E0 con ::parteN en el id es el suyo), como en la tanda 0 (docs/mandatos/ULECTURA_ACEPTADAS_tasa_error_tanda0.md, §2);
      vigilancia:2: las unidades aceptadas cuya extracción final (extracciones_finales_<to>.jsonl, última por unidad) no tiene error y
        tiene 0 relaciones aceptadas: la cifra que el código de la tanda 0 da como total (lectura_e6_tanda0.py:231-252,
        cero_relaciones_final), sobre el grafo evaluado;
      vigilancia:7: las aristas `ejecuta` cuyo origen es un Sujeto_rol_alcance_<to> (lectura_e6_tanda0.py:286-294, PREFIJO_V7);
      observacion:12: las aristas de extracción tal como A4.1 las define: todas menos `relation == referencia` y menos
        `rol_fuente == esqueleto` (enmienda de la observación 12, §2.1; el predicado de c1_literal del re-sellado).
    El id de una arista es la tripla (source, relation, target), única en el grafo (se controla).
  - Las vigilancias (1) y (3) dicen «a definir» (docs/preregistro_tanda0.md:594-602): no se sortean. Se cuentan, como información, las
    poblaciones de la definición que propone el FRENO: (1) los nodos Condicion; (3) los grupos de 2 nodos o más de contenido de una
    misma unidad de procedencia primaria con el mismo tramo normalizado.
Uso: python3 -I -B poblaciones_t4_t3f.py <raíz> <salida.json>
"""
import hashlib
import json
import re
import sys
from collections import Counter, OrderedDict
from datetime import datetime
from pathlib import Path

RAIZ, OUT = Path(sys.argv[1]).resolve(), Path(sys.argv[2])
X = RAIZ / "data/experiment/reextraccion_v2"
sys.path.insert(0, str(X / "e1_extractor"))
import prompt_r2b  # noqa: E402

assert Path(prompt_r2b.__file__).resolve().is_relative_to(RAIZ)
MAN = X / "manifiestos/tanda1_20tos_r2b.json"
LISTA = RAIZ / "data/experiment/segmentacion_oficial_e0r2/s2/lista_tanda1_S2.json"
KG = X / "corpus_tanda1/ens_veinte_r2b_sincola/r2/kg.json"
KG_SHA = "384a6d5bc139cd7b74d86840c68e7034b7a9bcb4bc26da7c61567f3f053e624e"
SAL = X / "corpus_tanda1/salida_r2b"
E0 = X / "e0_chunking/salida_tanda1_r2b"
ACEPTADOS = ("completo_ok_directo", "aceptado_con_residuales", "aceptado_tras_reintento")
CELDAS = ["RI:sin_raiz", "RI:resto", "NG:sin_raiz", "NG:resto"]
SIN_RAIZ_ESPERADOS = {"ceninf", "nmcief", "ri_ccna", "ri_mmsef"}
TIPOS_CONTENIDO = ("Operacion", "Restriccion", "Excepcion", "Obligacion", "Potestad", "Condicion", "Definicion", "Comunicacion")


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
lista = json.loads(LISTA.read_text(encoding="utf-8"))
sr_lista = {f["to"] for f in lista["filas"] if f.get("modo_lectura_e0_corregida") == "sin_raiz"}
assert sr == SIN_RAIZ_ESPERADOS == sr_lista, (sr, sr_lista)
kgb = KG.read_bytes()
assert sha(kgb) == KG_SHA, "el grafo evaluado no da su sha256"
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
    """El chunk de la E0 de una unidad: el propio si está en la E0 (manori::Sbloque4::parte3 es un chunk de la E0); si no, una parte
    por corte de E1 usa el chunk de su unidad (se quita solo el último ::parteN)."""
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
rf = lambda e: e.get("rol_fuente") or (e.get("properties") or {}).get("rol_fuente")  # noqa: E731
trip = lambda e: (e["source"], e["relation"], e["target"])  # noqa: E731
assert len({trip(e) for e in kg["edges"]}) == len(kg["edges"]), "triplas repetidas"
v7 = sorted(trip(e) for e in kg["edges"] if e["relation"] == "ejecuta" and str(e["source"]).startswith("Sujeto_rol_alcance_"))
o12 = sorted(trip(e) for e in kg["edges"] if e.get("relation") != "referencia" and rf(e) != "esqueleto")


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
    ("vigilancia:7", ("arista", v7, cel_a)),
    ("observacion:12", ("arista", o12, cel_a))])
res = OrderedDict([("hora", datetime.now().astimezone().isoformat(timespec="seconds")),
                   ("grafo", {"ruta": str(KG.relative_to(RAIZ)), "kg_sha256": KG_SHA}),
                   ("manifiesto", {"ruta": str(MAN.relative_to(RAIZ)), "sha256": sha(MAN.read_bytes())}),
                   ("lista_S2", {"ruta": str(LISTA.relative_to(RAIZ)), "sha256": sha(LISTA.read_bytes())}),
                   ("celda_por_to", dict(sorted(celda_to.items()))),
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
# (1) y (3), solo información: las poblaciones de la definición propuesta
cond = [n["id"] for n in kg["nodes"] if n["type"] == "Condicion"]
grupos = {}
for n in kg["nodes"]:
    if n["type"] not in TIPOS_CONTENIDO:
        continue
    p = n.get("provenance") or {}
    tr = re.sub(r"\s+", " ", (p.get("tramo") or "")).strip().lower()
    if p.get("chunk_id") and tr:
        grupos.setdefault((p["chunk_id"], tr), []).append(n["id"])
g3 = [sorted(v) for v in grupos.values() if len(v) >= 2]
res["propuestas_sin_sorteo"] = OrderedDict([
    ("vigilancia:1", {"definicion": "nodos Condicion del grafo evaluado", "N": len(cond),
                      "N_por_celda": dict(Counter(celda_nodo(nodos[i]) for i in cond))}),
    ("vigilancia:3", {"definicion": "grupos de 2 nodos o más de contenido con la misma unidad de procedencia primaria y el mismo tramo "
                                    "normalizado (espacios y mayúsculas)", "N_grupos": len(g3), "nodos_en_grupos": sum(len(x) for x in g3),
                      "N_por_celda_del_nodo_de_id_menor": dict(Counter(celda_nodo(nodos[x[0]]) for x in g3))})])
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("hora", res["hora"], "| unidades en finales", len(ult), "| cola", len(cola_ids), "| aceptadas", len(acept_ids))
for m, v in res["muestras"].items():
    print(f"{m}: N {v['N']} {v['N_por_celda']} entera {v['entera_sin_celdas']}")
print("propuestas:", json.dumps({k: {kk: vv for kk, vv in v.items() if kk != 'definicion'} for k, v in res["propuestas_sin_sorteo"].items()},
                                ensure_ascii=False))
print("sha256", sha(OUT.read_bytes()))
