"""U-DIAG-PROCESO, tareas 2 y 3: indicadores mecánicos (no lectura) de los dos problemas.
Solo lectura de archivos commiteados; USD 0. Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B censo_estructural.py <repo> <salida_e0r2_esq> <out.json>

Definiciones (declaradas antes de contar):
- ITEM: chunk de punto (punto_terminal) cuyo último tramo heredado termina en ':' (lista abierta por un
  chapeau, sea un intro o una línea de título).
- CHAPEAU-TITULO SIN UNIDAD: unidad contenedora U cuya línea de título termina en ':' (tramo `encabezado`
  de U en la herencia de un hijo) y sin mini-chunk `U::intro` en la salida de E0 (subcausa de la ficha 11).
- MINI ORDENADOR: mini-chunk intro/chapeau_seccion cuyo texto termina en ':'.
- ENCABEZADO DE SALVEDAD: algún tramo heredado `encabezado` con Excepciones/Exclusiones/no alcanzad*/
  no comprendid*, o algún tramo heredado que termina en ':' con «en la medida en que», «siempre que»,
  «condicionad», «las siguientes condiciones/exigencias/requisitos/casos» (marcas del vínculo entre
  unidades sin cita, fichas 18, 39, 61, 72).
- Contenido de un chunk (tanda 0): entidades finales de tipo distinto de TextoOrdenado.
"""
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

repo, e0r2_esq, out = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
norm = lambda s: " ".join((s or "").split())
termina_dp = lambda s: norm(s).rstrip().endswith((":", "："))
RE_SALV_ENC = re.compile(r"excepci[oó]n|exclusi[oó]n|no alcanzad|no comprendid", re.I)
RE_COND = re.compile(r"en la medida en que|siempre que|condicionad|siguientes (condiciones|exigencias|requisitos|casos)", re.I)


def censo_chunks(chunks):
    ids = {c["id"] for c in chunks}
    n = Counter()
    chapeau_titulo_sin_unidad = set()
    items, salvedad = [], []
    for c in chunks:
        n[c["tipo"]] += 1
        her = c.get("herencia", [])
        if c["tipo"] == "mini_chunk" and c.get("rol_bloque") in ("intro", "chapeau_seccion") and termina_dp(c["texto"]):
            n["mini_ordenador"] += 1
        if c["tipo"] != "punto_terminal" or not her:
            continue
        if termina_dp(her[-1]["texto"]):
            items.append(c["id"])
        for h in her:
            if h["tipo"] == "encabezado" and termina_dp(h["texto"]) and h["unidad_origen"] != c["unidad"]:
                if f"{c['to']}::{h['unidad_origen']}::intro" not in ids:
                    chapeau_titulo_sin_unidad.add(f"{c['to']}::{h['unidad_origen']}")
        if any(h["tipo"] == "encabezado" and RE_SALV_ENC.search(h["texto"]) for h in her) or \
           any(termina_dp(h["texto"]) and RE_COND.search(h["texto"]) for h in her):
            salvedad.append(c["id"])
    hijos_de_chapeau_titulo = [c["id"] for c in chunks if c["tipo"] == "punto_terminal" and any(
        f"{c['to']}::{h['unidad_origen']}" in chapeau_titulo_sin_unidad and h["tipo"] == "encabezado"
        for h in c.get("herencia", []))]
    return {"chunks": len(chunks), "por_tipo": dict(n), "items": len(items),
            "chapeau_titulo_sin_unidad": sorted(chapeau_titulo_sin_unidad),
            "n_chapeau_titulo_sin_unidad": len(chapeau_titulo_sin_unidad),
            "hijos_de_chapeau_titulo_sin_unidad": len(hijos_de_chapeau_titulo),
            "con_encabezado_de_salvedad": len(salvedad),
            "_items": items, "_salvedad": salvedad, "_hijos_ct": hijos_de_chapeau_titulo}


res = {}

# (1) partición B5.8.4 (commiteada): 152 TOs
part = []
for d in sorted((repo / "data/experiment/segmentacion_84/b584_particion").iterdir()):
    f = d / f"chunks_{d.name}.json"
    if d.is_dir() and f.exists():
        part += json.loads(f.read_text())
cp = censo_chunks(part)
res["particion_b584"] = {k: v for k, v in cp.items() if not k.startswith("_") and k != "chapeau_titulo_sin_unidad"}

# (2) ESQ-2, e0-r2 de la corrida de control (10 TOs, 762 unidades)
esq = []
for f in sorted(e0r2_esq.glob("chunks_*.json")):
    esq += json.loads(f.read_text())
ce = censo_chunks(esq)
res["esq_e0r2"] = {k: v for k, v in ce.items() if not k.startswith("_")}

# (2b) muestra azarosa de ESQ-2: cuántas de las 38 son ITEM / con encabezado de salvedad
sel = json.loads((repo / "data/experiment/esq/cobertura/orden/seleccion_muestra_esq2.json").read_text())
res["seleccion_claves"] = list(sel.keys())[:20]

# (3) tanda 0 (E0 legada commiteada + extracción final E1+E3 commiteada)
T0 = repo / "data/experiment/reextraccion_v2/corpus_tanda0/salida"
E0T0 = repo / "data/experiment/reextraccion_v2/e0_chunking/salida_tanda0"
t0_chunks, finales = [], {}
for f in sorted(E0T0.glob("chunks_*.json")):
    t0_chunks += json.loads(f.read_text())
for d in sorted(T0.iterdir()):
    f = d / f"extracciones_finales_{d.name}.jsonl"
    if f.exists():
        for line in f.read_text().splitlines():
            r = json.loads(line)
            finales[r["chunk_id"]] = r
ct = censo_chunks(t0_chunks)
porid = {c["id"]: c for c in t0_chunks}


def contenido(cid):
    r = finales.get(cid)
    if not r or not r.get("validacion"):
        return None
    ents = r["validacion"].get("entidades", [])
    prop = [e for e in ents if e["type"] != "TextoOrdenado" and ((e.get("provenance") or {}).get("rol_documental") == "punto_propio" or (e.get("provenance") or {}).get("rol_documental", "").startswith("bloque_"))]
    her = [e for e in ents if e["type"] != "TextoOrdenado" and (e.get("provenance") or {}).get("rol_documental", "").startswith("herencia")]
    return len(prop), len(her)


def tasa(ids):
    c = Counter()
    for i in ids:
        x = contenido(i)
        if x is None:
            c["sin_final"] += 1
        elif x[0] == 0 and x[1] == 0:
            c["vacio"] += 1
        elif x[0] == 0:
            c["solo_herencia"] += 1
        else:
            c["con_contenido_propio"] += 1
    return dict(c)


minis_ord = [c["id"] for c in t0_chunks if c["tipo"] == "mini_chunk" and c.get("rol_bloque") in ("intro", "chapeau_seccion") and termina_dp(c["texto"])]
res["tanda0"] = {k: v for k, v in ct.items() if not k.startswith("_")}
res["tanda0"]["finales"] = len(finales)
res["tanda0"]["items_estado_final"] = tasa(ct["_items"])
res["tanda0"]["hijos_chapeau_titulo_estado_final"] = tasa(ct["_hijos_ct"])
res["tanda0"]["minis_ordenadores_estado_final"] = tasa(minis_ord)
res["tanda0"]["terminales_todos_estado_final"] = tasa([c["id"] for c in t0_chunks if c["tipo"] == "punto_terminal"])

# (3b) E3 en tanda 0: faltantes con ubicación en un bloque heredado, y la guarda estructural (LAUDO B)
e3 = Counter()
guard_minis_vacios = []
for d in sorted(T0.iterdir()):
    f = d / "veredictos.jsonl"
    if not f.exists():
        continue
    for line in f.read_text().splitlines():
        v = json.loads(line)
        c = porid.get(v["chunk_id"])
        if c is None:
            continue
        her_units = {h["unidad_origen"] for h in c.get("herencia", [])} - {c["unidad"]}
        for fa in v.get("faltantes") or []:
            ub = str(fa.get("ubicacion") or "")
            ub0 = ub.split()[0].rstrip(".,;") if ub else ""
            en_her = ub0 in her_units and ub0 != c["unidad"].split("::")[0]
            key = (v["fase"], v["intento"], "heredado" if en_her else "propio")
            e3[key + ("total",)] += 1
            if fa.get("bloqueante"):
                e3[key + ("bloqueante",)] += 1
            if fa.get("estructural_no_bloqueante"):
                e3[key + ("estructural_no_bloqueante",)] += 1
                if c["tipo"] == "mini_chunk" and contenido(c["id"]) in ((0, 0),):
                    guard_minis_vacios.append(c["id"])
res["tanda0"]["e3_faltantes"] = {"|".join(map(str, k)): n for k, n in sorted(e3.items())}
res["tanda0"]["guarda_laudoB_en_minis_sin_contenido"] = sorted(set(guard_minis_vacios))

out.write_text(json.dumps(res, ensure_ascii=False, indent=1))
print(json.dumps({k: (v if k != "esq_e0r2" else {kk: vv for kk, vv in v.items() if kk != "chapeau_titulo_sin_unidad"}) for k, v in res.items()}, ensure_ascii=False, indent=1))
