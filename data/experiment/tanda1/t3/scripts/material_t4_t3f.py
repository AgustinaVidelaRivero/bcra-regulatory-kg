"""B6.1, tanda 1, T3, punto 7.5: el material de T4, por muestra: una ficha por elemento y la planilla en blanco. No lee ninguna unidad
para juzgarla ni marca nada: arma lo que T4 lee. Corre sobre una copia; USD 0, sin API (ANTHROPIC_API_KEY sin definir).

  - El texto de cada unidad es el que vio E3: comun_e3.fuente_integro(chunk, bloque_de_lista=ratchet_e3._forma_r2(validacion)), con
    el chunk de la E0 de la tanda 1 y, cuando la unidad es una parte por corte de E1, el de la E0 con las partes (rearmada en este T3,
    e0_partes_t3f.py). La validación es la de la versión que muestra la ficha: la final (extracciones_finales_<to>.jsonl) o, en la
    cola, la del primer intento (la primera fila de la unidad en extracciones_e1.jsonl).
  - El grafo es el sin cola (KG-Tanda1-Veinte-r2b-sincola, 384a6d5b…), salvo la cola, que va con su primer intento: las entidades y
    relaciones validadas de E1 de ese intento.
  - Ficha de una unidad (patrón de data/experiment/lectura_aceptadas/l1_fichas.py): id, TO, celda, páginas, el texto, y los nodos y
    aristas del grafo cuya procedencia (alguna de `provenances`) es la unidad, con su tramo y una referencia local (N1…, A1…, R1…, C1…,
    E1…). Ficha de una arista (enmienda de la observación 12, §2.1): origen y destino (id, tipo, label, propiedades), relación,
    propiedades de la arista, su procedencia y el texto de su unidad de procedencia.
  - Sin el estado de E3 ni las marcas de E3, que la lectura no necesita: se sacan las claves estado, estado_e3, n_reintentos,
    residuales, marcas_e3, copia_nota_e3, no_verificada_e3, cola_humana y cola_chunks donde aparezcan.
  - La planilla en blanco, por muestra, en CSV, con las columnas del veredicto de esa lectura y vacías.
Escribe en <salida>/<muestra>/ fichas_<muestra>.jsonl, fichas_<muestra>.md y planilla_<muestra>.csv, y <salida>/material_t4.json con
el sha256 y la hora de cada archivo; frena si la hora no es posterior a la de los sorteos.
Uso: python3 -I -B material_t4_t3f.py <raíz> <sorteos (con sorteos_t4.json)> <E0 de la tanda 1 con las partes> <salida>
"""
import csv
import hashlib
import io
import json
import os
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

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
PLANILLA = {
    "cola": ("veredicto (con error / sin error)", "lo no sostenido (nodo o relación y por qué)", "omisiones (aparte)", "nota"),
    "aceptadas:items": ("veredicto (con error / sin error)", "lo no sostenido (nodo o arista y por qué)", "omisiones (aparte)", "nota"),
    "aceptadas:no_items": ("veredicto (con error / sin error)", "lo no sostenido (nodo o arista y por qué)", "omisiones (aparte)", "nota"),
    "vigilancia:2": ("¿el texto porta contenido normativo que la extracción no tiene? (sí / no / no decidible)", "qué contenido", "nota"),
    "vigilancia:7": ("¿la arista ejecuta con el rol de alcance tiene apoyo textual? (sí / no / no decidible)", "nota"),
    "observacion:12": ("veredicto (correcta / incorrecta / no decidible)", "capa_pipeline (si es incorrecta)", "nota")}


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


indice_sor = json.loads((SOR / "sorteos_t4.json").read_text(encoding="utf-8"))
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
final, primero = {}, {}
for to in tos:
    for r in lineas(SAL / to / f"extracciones_finales_{to}.jsonl"):
        final[r["chunk_id"]] = r
    for r in lineas(SAL / to / "extracciones_e1.jsonl"):
        primero.setdefault(r["chunk_id"], r)


def chunk_de(cid: str) -> tuple:
    if cid in chunks:
        return chunks[cid], "e0"
    return chunks_p[cid], "e0_con_las_partes"


def texto_e3(cid: str, validacion) -> dict:
    c, de = chunk_de(cid)
    forma = ratchet_e3._forma_r2(validacion)
    return {"chunk_de": de, "bloque_de_lista": forma, "texto": comun_e3.fuente_integro(c, bloque_de_lista=forma),
            "unidad": c.get("unidad"), "tipo": c.get("tipo"), "titulo": c.get("titulo"), "paginas": c.get("paginas")}


def nodo_resumen(nid: str, refs: dict) -> dict:
    m = nodos[nid]
    return {"ref": refs.get(nid), "id": nid, "type": m["type"], "label": m["label"]}


def ficha_unidad(cid: str) -> dict:
    nod, refs = [], {}
    for n in kg["nodes"]:
        provs = [p for p in (n.get("provenances") or []) if p.get("chunk_id") == cid]
        if not provs:
            continue
        ref = f"N{len(nod) + 1}"
        refs[n["id"]] = ref
        nod.append(limpio({"ref": ref, "id": n["id"], "type": n["type"], "label": n["label"], "properties": n.get("properties") or {},
                           "procedencia": [{k: p[k] for k in CAMPOS_PROC if k in p} for p in provs],
                           "procedencias_en_el_grafo": len(n.get("provenances") or []),
                           **{k: n[k] for k in CAMPOS_NODO if k in n}}))
    ari, cont = [], Counter()
    for x in kg["edges"]:
        provs = [p for p in (x.get("provenances") or []) if p.get("chunk_id") == cid]
        if not provs:
            continue
        cl = clase_arista(x["relation"])
        cont[cl] += 1
        pref = {"extraccion": "A", "remision_derivada": "R", "catalogo_sujetos": "C", "estructural": "E"}[cl]
        ari.append(limpio({"ref": f"{pref}{cont[cl]}", "clase": cl, "relation": x["relation"], "source": nodo_resumen(x["source"], refs),
                           "target": nodo_resumen(x["target"], refs), "properties": x.get("properties") or {},
                           "procedencia": [{k: p[k] for k in CAMPOS_PROC if k in p} for p in provs],
                           **{k: x[k] for k in CAMPOS_ARISTA if k in x}}))
    return {"version": "final (grafo sin cola)", "texto_e3": texto_e3(cid, (final.get(cid) or {}).get("validacion")),
            "nodos": nod, "aristas": ari, "conteos": {"nodos": len(nod), "aristas": len(ari), "aristas_por_clase": dict(cont)}}


def ficha_primer_intento(cid: str) -> dict:
    r = primero[cid]
    v = r.get("validacion") or {}
    return {"version": "primer intento (cola)", "texto_e3": texto_e3(cid, v), "error": r.get("error"),
            "entidades": limpio(v.get("entidades") or []), "relaciones": limpio(v.get("relaciones") or []),
            "omisiones_no_prosa": limpio(v.get("omisiones_no_prosa") or []),
            "conteos": {"entidades": len(v.get("entidades") or []), "relaciones": len(v.get("relaciones") or [])}}


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
            "texto_e3": texto_e3(pv["chunk_id"], (final.get(pv["chunk_id"]) or {}).get("validacion")) if pv.get("chunk_id") else None}


def md_ficha(f: dict) -> list:
    out = [f"## {f['n']}. `{f['id'] if isinstance(f['id'], str) else ' | '.join(f['id'])}` — {f['celda']} · {f['muestra']}", ""]
    t = f["material"].get("texto_e3")
    if t:
        out += [f"Texto que vio E3 ({t['chunk_de']}, bloque de lista {t['bloque_de_lista']}; págs. "
                f"{', '.join(map(str, t.get('paginas') or []))}):", "", "```", t["texto"], "```", ""]
    m = f["material"]
    if "nodos" in m:
        out.append(f"Versión: {m['version']}. Nodos {m['conteos']['nodos']}, aristas {m['conteos']['aristas']}.")
        for n in m["nodos"]:
            tr = "; ".join(re.sub(r"\s+", " ", p.get("tramo") or "")[:300] for p in n["procedencia"])
            out.append(f"- **{n['ref']}** {n['type']} `{n['id']}` — {n['label']} · {json.dumps(n['properties'], ensure_ascii=False)[:400]} · tramo: {tr}")
        for a in m["aristas"]:
            out.append(f"- **{a['ref']}** ({a['clase']}) {a['source']['ref'] or a['source']['id']} —{a['relation']}→ "
                       f"{a['target']['ref'] or a['target']['id']} · {json.dumps(a['properties'], ensure_ascii=False)[:300]}")
    elif "entidades" in m:
        out.append(f"Versión: {m['version']}. Entidades {m['conteos']['entidades']}, relaciones {m['conteos']['relaciones']}"
                   + (f"; error: {m['error']}" if m.get("error") else "") + ".")
        for e in m["entidades"]:
            out.append(f"- {json.dumps(e, ensure_ascii=False)[:500]}")
        for r in m["relaciones"]:
            out.append(f"- relación: {json.dumps(r, ensure_ascii=False)[:400]}")
    else:
        out += [f"Versión: {m['version']}.", f"- origen: {json.dumps(m['origen'], ensure_ascii=False)[:600]}",
                f"- relación: `{m['relacion']}`", f"- destino: {json.dumps(m['destino'], ensure_ascii=False)[:600]}",
                f"- arista: {json.dumps(m['arista'], ensure_ascii=False)[:600]}"]
    return out + [""]


OUT.mkdir(parents=True, exist_ok=True)
indice = {"hora": hora, "sorteos_t4_sha256": sha((SOR / "sorteos_t4.json").read_bytes()), "grafo_sha256": KG_SHA,
          "e0_con_las_partes": str(E0P.name), "muestras": {}}
for m, info in indice_sor["muestras"].items():
    s = json.loads((SOR / info["archivo"]).read_text(encoding="utf-8"))
    assert sha((SOR / info["archivo"]).read_bytes()) == info["sha256"]
    fichas, n = [], 0
    for celda, x in s["celdas"].items():
        for orden, e in enumerate(x["elementos"], 1):
            n += 1
            if s["elemento"] == "unidad":
                mat = ficha_primer_intento(e) if m == "cola" else ficha_unidad(e)
            else:
                mat = ficha_arista(e)
            fichas.append({"n": n, "muestra": m, "celda": celda, "orden_en_la_celda": orden, "id": e,
                           "to": (e if isinstance(e, str) else (nodos[e[0]].get("provenance") or {}).get("to") or "").split("::")[0],
                           "material": mat})
    d = OUT / m.replace(":", "_")
    d.mkdir(parents=True, exist_ok=True)
    nom = m.replace(":", "_")
    fj = d / f"fichas_{nom}.jsonl"
    fj.write_text("".join(json.dumps(f, ensure_ascii=False) + "\n" for f in fichas), encoding="utf-8")
    md = [f"# Material de T4 — {m} ({len(fichas)} fichas; B6.1, tanda 1, T3, punto 7.5)", "",
          f"Sorteo: `{info['archivo']}` ({info['sha256'][:8]}…, {info['hora']}); material armado a las {hora}. Sin el estado de E3 "
          "ni las marcas de E3.", ""]
    for f in fichas:
        md += md_ficha(f)
    fm = d / f"fichas_{nom}.md"
    fm.write_text("\n".join(md) + "\n", encoding="utf-8")
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(("n", "celda", "id") + PLANILLA[m])
    for f in fichas:
        w.writerow((f["n"], f["celda"], f["id"] if isinstance(f["id"], str) else " | ".join(f["id"])) + ("",) * len(PLANILLA[m]))
    fc = d / f"planilla_{nom}.csv"
    fc.write_text(buf.getvalue(), encoding="utf-8")
    indice["muestras"][m] = {"fichas": len(fichas), "archivos": {p.name: sha(p.read_bytes()) for p in (fj, fm, fc)}}
(OUT / "material_t4.json").write_text(json.dumps(indice, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for m, x in indice["muestras"].items():
    print(m, x["fichas"], "fichas", {k: v[:12] for k, v in x["archivos"].items()})
print("hora", hora)
