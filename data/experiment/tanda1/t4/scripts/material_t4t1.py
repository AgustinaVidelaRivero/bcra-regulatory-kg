"""B6.1, tanda 1, T4, primer tramo, punto 4: el material de las tres muestras nuevas (vigilancias (1) y (3) y observación (12) rehecha),
una ficha por elemento, con las mismas reglas que el de T3 (material_t4_t3f.py). No lee ninguna unidad para juzgarla ni marca nada:
arma lo que se lee. Corre sobre una copia; USD 0, sin API (ANTHROPIC_API_KEY sin definir).

  - El texto de cada unidad es el que vio E3: comun_e3.fuente_integro(chunk, bloque_de_lista=ratchet_e3._forma_r2(validacion)), con
    la validación de la extracción final (extracciones_finales_<to>.jsonl) y el chunk de la E0 de la tanda 1 o, si la unidad es una
    parte por corte de E1, el de la E0 con las partes (reext_t0/t3/e0_con_partes.py sobre la copia; se controla que el conjunto sea el
    de T3, f079c1ff…).
  - El grafo es el evaluado, el sin cola (KG-Tanda1-Veinte-r2b-sincola, 384a6d5b…).
  - Ficha de (1): el nodo Condicion con sus propiedades y su procedencia, el texto de su unidad (la de su procedencia primaria) y sus
    aristas, entrantes y salientes, con la relación, sus propiedades y el id, el tipo y el label del otro nodo.
  - Ficha de (3): los nodos del grupo con sus propiedades y su procedencia, y el texto de su unidad.
  - Ficha de la (12): como la de T3 (ficha_arista de material_t4_t3f.py): la arista, sus dos nodos y el texto de su unidad de procedencia.
  - Sin el estado de E3 ni las marcas de E3: se sacan las claves estado, estado_e3, n_reintentos, residuales, marcas_e3, copia_nota_e3,
    no_verificada_e3, cola_humana y cola_chunks donde aparezcan. El control, al final, relee lo escrito.
Escribe en <salida>/<muestra>/ fichas_<muestra>.jsonl y fichas_<muestra>.md, y <salida>/material_t4_tramo1.json con el sha256 y la hora
de cada archivo y el control; frena si la hora no es posterior a la de los sorteos.
Uso: python3 -I -B material_t4t1.py <raíz> <sorteos (con sorteos_t4_tramo1.json)> <E0 de la tanda 1 con las partes> <salida>
"""
import hashlib
import json
import os
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

sys.dont_write_bytecode = True
RAIZ, SOR, E0P, OUT = (Path(x).resolve() for x in sys.argv[1:5])
assert not os.environ.get("ANTHROPIC_API_KEY"), "ANTHROPIC_API_KEY definida"
X = RAIZ / "data/experiment/reextraccion_v2"
sys.path.insert(0, str(X / "e3_verificador"))
import comun_e3  # noqa: E402
import ratchet_e3  # noqa: E402

for mod in (comun_e3, ratchet_e3):
    assert Path(mod.__file__).resolve().is_relative_to(RAIZ)
KG = X / "corpus_tanda1/ens_veinte_r2b_sincola/r2/kg.json"
KG_SHA = "384a6d5bc139cd7b74d86840c68e7034b7a9bcb4bc26da7c61567f3f053e624e"
E0P_CONJUNTO = "f079c1ff1b680eb7c766e8bebf05da489f474dd39e68ad228266296e8bd52028"
SAL = X / "corpus_tanda1/salida_r2b"
E0 = X / "e0_chunking/salida_tanda1_r2b"
FUERA = {"estado", "estado_e3", "n_reintentos", "residuales", "marcas_e3", "copia_nota_e3", "no_verificada_e3", "cola_humana",
         "cola_chunks"}
EXTRACCION = {"aplica_a", "condicion_de", "condiciona", "ejecuta", "exceptua", "exceptua_obligacion", "limita", "prohibe", "regula",
              "requiere"}
ESTRUCTURAL = {"establecida_en", "miembro_de", "subclase_de", "instancia_de", "parte_de", "referencia", "modificada_por"}
CAMPOS_ARISTA = ("sujeto_mencion", "mencion_verificada", "metodo_resolucion", "sujeto_id_modelo", "sujeto_mencion_modelo", "rol_fuente",
                 "calificador", "coherencia_tipo_predicado", "properties_no_definidas")
CAMPOS_NODO = ("rol_fuente", "originales", "fuera_de_lista", "properties_no_definidas")
CAMPOS_PROC = ("chunk_id", "punto", "rol_documental", "tramo", "tramo_verificado", "termino_verificado", "tramo_modelo", "paginas")


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def lineas(p: Path) -> list:
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()] if p.exists() else []


def limpio(x):
    if isinstance(x, dict):
        return {k: limpio(v) for k, v in x.items() if k not in FUERA}
    if isinstance(x, list):
        return [limpio(v) for v in x]
    return x


def clase_arista(rel: str) -> str:
    if rel == "remite_a":
        return "remision_derivada"
    if rel == "padre_sugerido":
        return "catalogo_sujetos"
    if rel in ESTRUCTURAL:
        return "estructural"
    if rel in EXTRACCION:
        return "extraccion"
    raise SystemExit(f"predicado sin clase: {rel}")


def conjunto(d: Path) -> str:
    fs = {p.relative_to(d).as_posix(): sha(p.read_bytes()) for p in d.rglob("*") if p.is_file()}
    return sha("".join(f"{h}  {n}\n" for n, h in sorted(fs.items())).encode())


assert conjunto(E0P) == E0P_CONJUNTO, "la E0 con las partes no es la de T3"
indice_sor = json.loads((SOR / "sorteos_t4_tramo1.json").read_text(encoding="utf-8"))
hora = datetime.now().astimezone().isoformat(timespec="seconds")
assert all(datetime.fromisoformat(hora) > datetime.fromisoformat(v["hora"]) for v in indice_sor["muestras"].values()), \
    "la hora del material no es posterior a la de los sorteos"
kgb = KG.read_bytes()
assert sha(kgb) == KG_SHA
kg = json.loads(kgb)
nodos = {n["id"]: n for n in kg["nodes"]}
tos = sorted(t["id"] for t in json.loads((X / "manifiestos/tanda1_20tos_r2b.json").read_text(encoding="utf-8"))["tos"])
chunks, chunks_p = {}, {}
for to in tos:
    for d, dest in ((E0, chunks), (E0P, chunks_p)):
        x = json.loads((d / f"chunks_{to}.json").read_text(encoding="utf-8"))
        dest.update({c["id"]: c for c in (x["chunks"] if isinstance(x, dict) else x)})
final = {}
for to in tos:
    for r in lineas(SAL / to / f"extracciones_finales_{to}.jsonl"):
        final[r["chunk_id"]] = r


def chunk_de(cid: str) -> tuple:
    if cid in chunks:
        return chunks[cid], "e0"
    return chunks_p[cid], "e0_con_las_partes"


def texto_e3(cid: str) -> dict:
    c, de = chunk_de(cid)
    forma = ratchet_e3._forma_r2((final.get(cid) or {}).get("validacion"))
    return {"chunk_id": cid, "chunk_de": de, "bloque_de_lista": forma, "texto": comun_e3.fuente_integro(c, bloque_de_lista=forma),
            "unidad": c.get("unidad"), "tipo": c.get("tipo"), "titulo": c.get("titulo"), "paginas": c.get("paginas")}


def nodo_completo(nid: str, ref: str = None) -> dict:
    n = nodos[nid]
    provs = n.get("provenances") or ([n["provenance"]] if n.get("provenance") else [])
    return limpio({**({"ref": ref} if ref else {}), "id": nid, "type": n["type"], "label": n["label"],
                   "properties": n.get("properties") or {}, "procedencia": [{k: p[k] for k in CAMPOS_PROC if k in p} for p in provs],
                   "unidades_de_procedencia": len({p.get("chunk_id") for p in provs if p.get("chunk_id")}),
                   **{k: n[k] for k in CAMPOS_NODO if k in n}})


def ficha_condicion(nid: str) -> dict:
    n = nodos[nid]
    ari, cont = [], Counter()
    for x in kg["edges"]:
        if nid not in (x["source"], x["target"]):
            continue
        sale = x["source"] == nid
        otro = nodos[x["target"] if sale else x["source"]]
        cl = clase_arista(x["relation"])
        cont[cl] += 1
        pv = x.get("provenance") or {}
        ari.append(limpio({"sentido": "sale" if sale else "entra", "relation": x["relation"], "clase": cl,
                           "otro_nodo": {"id": otro["id"], "type": otro["type"], "label": otro["label"]},
                           "properties": x.get("properties") or {}, **{k: x[k] for k in CAMPOS_ARISTA if k in x},
                           "procedencia": {k: pv[k] for k in CAMPOS_PROC if k in pv}}))
    cid = (n.get("provenance") or {}).get("chunk_id")
    return {"version": "final (grafo sin cola)", "nodo": nodo_completo(nid), "texto_e3": texto_e3(cid),
            "aristas": ari, "conteos": {"aristas": len(ari), "aristas_por_clase": dict(cont)}}


def ficha_grupo(gid: str, ids: list) -> dict:
    cids = {(nodos[i].get("provenance") or {}).get("chunk_id") for i in ids}
    assert len(cids) == 1, gid
    return {"version": "final (grafo sin cola)", "grupo": gid, "nodos": [nodo_completo(i, f"N{k}") for k, i in enumerate(ids, 1)],
            "texto_e3": texto_e3(cids.pop()), "conteos": {"nodos": len(ids)}}


def ficha_arista(t: list) -> dict:
    s, rel, d = t
    x = next(e for e in kg["edges"] if (e["source"], e["relation"], e["target"]) == (s, rel, d))
    pv = x.get("provenance") or {}

    def nodo(nid):
        n = nodos[nid]
        return limpio({"id": nid, "type": n["type"], "label": n["label"], "properties": n.get("properties") or {},
                       "procedencia": {k: (n.get("provenance") or {}).get(k) for k in CAMPOS_PROC if k in (n.get("provenance") or {})}})
    return {"version": "final (grafo sin cola)", "origen": nodo(s), "relacion": rel, "destino": nodo(d),
            "arista": limpio({"properties": x.get("properties") or {}, **{k: x[k] for k in CAMPOS_ARISTA if k in x},
                              "procedencia": {k: pv[k] for k in CAMPOS_PROC if k in pv}}),
            "texto_e3": texto_e3(pv["chunk_id"]) if pv.get("chunk_id") else None}


def j(x, n: int) -> str:
    s = json.dumps(x, ensure_ascii=False)
    return s if len(s) <= n else s[:n] + "…"


def md_ficha(f: dict) -> list:
    out = [f"## {f['n']}. `{f['id'] if isinstance(f['id'], str) else ' | '.join(f['id'])}` — {f['celda']} · {f['muestra']}", ""]
    m = f["material"]
    t = m.get("texto_e3")
    if t:
        out += [f"Texto que vio E3 de `{t['chunk_id']}` ({t['chunk_de']}, bloque de lista {t['bloque_de_lista']}; págs. "
                f"{', '.join(map(str, t.get('paginas') or []))}):", "", "```", t["texto"], "```", ""]
    out.append(f"Versión: {m['version']}.")
    if "nodo" in m:
        n = m["nodo"]
        tr = "; ".join(re.sub(r"\s+", " ", p.get("tramo") or "") for p in n["procedencia"])
        out += [f"- **Nodo** {n['type']} `{n['id']}` — {n['label']}", f"  - propiedades: {j(n['properties'], 1500)}",
                f"  - tramo: {tr}"]
        out.append(f"- **Aristas** ({m['conteos']['aristas']}):")
        for a in m["aristas"]:
            o = a["otro_nodo"]
            flecha = f"—{a['relation']}→ {o['type']} `{o['id']}`" if a["sentido"] == "sale" else f"←{a['relation']}— {o['type']} `{o['id']}`"
            extra = {k: a[k] for k in ("rol_fuente", "sujeto_mencion", "mencion_verificada", "calificador") if k in a}
            out.append(f"  - ({a['clase']}) {flecha} — {o['label']}" + (f" · {j(a['properties'], 300)}" if a["properties"] else "")
                       + (f" · {j(extra, 300)}" if extra else ""))
    elif "grupo" in m:
        out.append(f"Grupo de {m['conteos']['nodos']} nodos con la misma unidad y el mismo tramo normalizado.")
        for n in m["nodos"]:
            tr = "; ".join(re.sub(r"\s+", " ", p.get("tramo") or "") for p in n["procedencia"])
            out += [f"- **{n['ref']}** {n['type']} `{n['id']}` — {n['label']}", f"  - propiedades: {j(n['properties'], 1500)}",
                    f"  - tramo: {tr}"]
    else:
        out += [f"- origen: {j(m['origen'], 1200)}", f"- relación: `{m['relacion']}`", f"- destino: {j(m['destino'], 1200)}",
                f"- arista: {j(m['arista'], 800)}"]
    return out + [""]


OUT.mkdir(parents=True, exist_ok=True)
indice = {"hora": hora, "sorteos_t4_tramo1_sha256": sha((SOR / "sorteos_t4_tramo1.json").read_bytes()), "grafo_sha256": KG_SHA,
          "e0_con_las_partes_conjunto": E0P_CONJUNTO, "muestras": {}}
for m, info in indice_sor["muestras"].items():
    s = json.loads((SOR / info["archivo"]).read_text(encoding="utf-8"))
    assert sha((SOR / info["archivo"]).read_bytes()) == info["sha256"]
    fichas, n = [], 0
    for celda, x in s["celdas"].items():
        for orden, e in enumerate(x["elementos"], 1):
            n += 1
            if m == "vigilancia:1":
                mat, to = ficha_condicion(e), (nodos[e].get("provenance") or {}).get("to")
            elif m == "vigilancia:3":
                mat, to = ficha_grupo(e, s["grupos"][e]), (nodos[s["grupos"][e][0]].get("provenance") or {}).get("to")
            else:
                mat, to = ficha_arista(e), (nodos[e[0]].get("provenance") or {}).get("to")
            fichas.append({"n": n, "muestra": m, "celda": celda, "orden_en_la_celda": orden, "id": e, "to": to, "material": mat})
    nom = m.replace(":", "_")
    d = OUT / nom
    d.mkdir(parents=True, exist_ok=True)
    fj = d / f"fichas_{nom}.jsonl"
    fj.write_text("".join(json.dumps(f, ensure_ascii=False) + "\n" for f in fichas), encoding="utf-8")
    md = [f"# Material de T4 — {m} ({len(fichas)} fichas; B6.1, tanda 1, T4, primer tramo, punto 4)", "",
          f"Sorteo: `{info['archivo']}` ({info['sha256'][:8]}…, {info['hora']}); material armado a las {hora}. Sin el estado de E3 "
          "ni las marcas de E3.", ""]
    for f in fichas:
        md += md_ficha(f)
    fm = d / f"fichas_{nom}.md"
    fm.write_text("\n".join(md) + "\n", encoding="utf-8")
    indice["muestras"][m] = {"fichas": len(fichas), "archivos": {p.name: sha(p.read_bytes()) for p in (fj, fm)}}


# el control: relee lo escrito
def claves(x, acc: Counter) -> None:
    if isinstance(x, dict):
        for k, v in x.items():
            acc[k] += 1
            claves(v, acc)
    elif isinstance(x, list):
        for v in x:
            claves(v, acc)


ctl = {"fichas": 0, "claves_vedadas": 0, "texto_de": Counter(), "sin_texto": 0, "estado_en_los_md": 0}
for m in indice["muestras"]:
    nom = m.replace(":", "_")
    for f in lineas(OUT / nom / f"fichas_{nom}.jsonl"):
        ctl["fichas"] += 1
        acc = Counter()
        claves(f, acc)
        ctl["claves_vedadas"] += sum(acc[k] for k in FUERA)
        t = f["material"].get("texto_e3")
        if t and t.get("texto"):
            ctl["texto_de"][t["chunk_de"]] += 1
        else:
            ctl["sin_texto"] += 1
    ctl["estado_en_los_md"] += (OUT / nom / f"fichas_{nom}.md").read_text(encoding="utf-8").count('"estado')
ctl["texto_de"] = dict(ctl["texto_de"])
indice["control"] = ctl
(OUT / "material_t4_tramo1.json").write_text(json.dumps(indice, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for m, x in indice["muestras"].items():
    print(m, x["fichas"], "fichas", {k: v[:12] for k, v in x["archivos"].items()})
print("control:", json.dumps(ctl, ensure_ascii=False))
print("hora", hora, "| material_t4_tramo1.json", sha((OUT / "material_t4_tramo1.json").read_bytes()))
assert ctl["claves_vedadas"] == 0 and ctl["estado_en_los_md"] == 0 and ctl["sin_texto"] == 0
