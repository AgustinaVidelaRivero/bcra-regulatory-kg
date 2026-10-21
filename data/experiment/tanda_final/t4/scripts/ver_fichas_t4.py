"""B6.1, tanda final, T4, primer tramo: ayuda de lectura. Imprime, compactas, las fichas de una muestra desde su fichas_<muestra>.jsonl
(el material de T3, punto 7.5, sin el estado ni las marcas de E3: control_material_tf.json da 0 claves vedadas). No decide ni escribe
nada; solo saca el ruido para leer:
  - el texto de la unidad va entero;
  - un nodo, en una línea: su ref, su tipo, su etiqueta, sus propiedades y su procedencia (punto, rol si no es el propio, chunk si no es
    la unidad, si el tramo está verificado y el tramo, cortado a 90 caracteres);
  - una relación o arista, en una línea: origen -predicado-> destino, con lo que no es nulo;
  - salen los ids largos donde hay ref o etiqueta, `indice_crudo`, `archivo`, las páginas y los campos nulos.
Uso: python3 -I -B ver_fichas_t4.py <material> <muestra> [<desde> <hasta>]   (números de ficha, «## n.» del .md)
"""
import json
import sys
from pathlib import Path

MAT, M = Path(sys.argv[1]), sys.argv[2]
DESDE, HASTA = (int(sys.argv[3]), int(sys.argv[4])) if len(sys.argv) > 4 else (1, 10 ** 6)
J = lambda x: json.dumps(x, ensure_ascii=False)  # noqa: E731


def proc(p, unidad, to) -> str:
    if isinstance(p, list):
        return " ; ".join(proc(x, unidad, to) for x in p)
    if not isinstance(p, dict):
        return J(p)
    s = []
    if p.get("punto") != unidad:
        s.append(f"@{p.get('punto')}")
    if p.get("rol_documental") not in (None, "punto_propio"):
        s.append(f"rol={p['rol_documental']}")
    if p.get("chunk_id") and not str(p["chunk_id"]).endswith(f"::{unidad}"):
        s.append(f"chunk={p['chunk_id']}")
    if p.get("to") and p["to"] != to:
        s.append(f"to={p['to']}")
    if "tramo" in p:
        t = p["tramo"] or ""
        s.append(f"tramo[{p.get('tramo_verificado')}]=«{t[:90]}{'…' if len(t) > 90 else ''}»")
    if "termino_verificado" in p:
        s.append(f"termino_verificado={p['termino_verificado']}")
    return " ".join(s)


def nodo(x, unidad, to) -> str:
    ref = x.get("ref") or x.get("local_id") or ""
    props = {k: v for k, v in (x.get("properties") or {}).items() if v not in (None, "", [], {})}
    extra = {k: v for k, v in x.items() if k not in ("ref", "local_id", "id", "type", "label", "properties", "provenance", "procedencia",
                                                    "indice_crudo") and v not in (None, "", [], {})}
    p = proc(x.get("provenance", x.get("procedencia", {})), unidad, to)
    return (f"{ref} {x.get('type')} «{x.get('label')}»" + (f" {J(props)}" if props else "") + (f" {J(extra)}" if extra else "")
            + (f"  [{p}]" if p else ""))


def lado(v) -> str:
    if isinstance(v, dict):
        return f"{v.get('ref', '')}:{v.get('type')}«{v.get('label')}»"
    return str(v)


def rel(x, unidad, to) -> str:
    pred = x.get("predicate") or x.get("relation")
    tgt = x.get("target")
    if tgt is None and x.get("sujeto_id"):
        tgt = x["sujeto_id"]
    elif tgt is None and x.get("sujeto_propuesto"):
        tgt = f"?«{x['sujeto_propuesto']}» (padre {x.get('sujeto_propuesto_padre_sugerido')})"
    if "otro_nodo" in x:
        a, b = ("ESTE", lado(x["otro_nodo"])) if x.get("sentido") == "sale" else (lado(x["otro_nodo"]), "ESTE")
        cab = f"{a} -{pred}-> {b}"
    else:
        cab = f"{x.get('ref', '')} {lado(x.get('source'))} -{pred}-> {lado(tgt)}"
    extra = {k: v for k, v in x.items() if k not in ("ref", "source", "target", "predicate", "relation", "sujeto_id", "sujeto_propuesto",
                                                    "sujeto_propuesto_padre_sugerido", "provenance", "procedencia", "indice_crudo",
                                                    "otro_nodo", "sentido") and v not in (None, "", [], {})}
    p = proc(x.get("provenance", x.get("procedencia", {})), unidad, to)
    return cab + (f" {J(extra)}" if extra else "") + (f"  [{p}]" if p else "")


for linea in (MAT / M / f"fichas_{M}.jsonl").read_text(encoding="utf-8").splitlines():
    if not linea.strip():
        continue
    f = json.loads(linea)
    if not DESDE <= f["n"] <= HASTA:
        continue
    mat = f["material"]
    t = mat.get("texto_e3") or {}
    u = t.get("unidad")
    print(f"\n######## {f['n']}. {f['id'] if isinstance(f['id'], str) else ' | '.join(f['id'])} — {f['celda']} · TO {f['to']} · {mat.get('version')}")
    print(f"[texto: unidad {u}, {t.get('tipo')}, «{t.get('titulo')}», chunk_de {t.get('chunk_de')}, lista {t.get('bloque_de_lista')}]")
    print(t.get("texto"))
    for k, v in mat.items():
        if k in ("version", "texto_e3"):
            continue
        if k in ("entidades", "nodos"):
            print(f"-- {k} ({len(v)}):")
            for x in v:
                print("   ", nodo(x, u, f["to"]))
        elif k in ("relaciones", "aristas"):
            print(f"-- {k} ({len(v)}):")
            for x in v:
                print("   ", rel(x, u, f["to"]))
        elif k in ("nodo", "origen", "destino"):
            print(f"-- {k}: {nodo(v, u, f['to'])}")
        elif k == "arista":
            extra = {a: b for a, b in v.items() if a not in ("procedencia",) and b not in (None, "", [], {})}
            p = proc(v.get("procedencia", {}), u, f["to"])
            print(f"-- arista: {J(extra)}" + (f"  [{p}]" if p else ""))
        elif v not in (None, [], {}, ""):
            print(f"-- {k}: {J(v)}")
