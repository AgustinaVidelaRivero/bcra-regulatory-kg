"""U-UNION-ESTRECHA, U2: fichas sin veredicto de las 29 uniones del marco (censo), USD 0, sin API.

Una ficha por unión, numerada U01 a U29 en el orden de `marco_u2_diez.json`, con:
  - la Condicion del ítem: id, descripción y tramo (con todas sus provenances);
  - el texto entero de la unidad del ítem (texto propio y lo que hereda de E0);
  - el nodo destino: id, tipo, descripción y tramo (con todas sus provenances);
  - el texto entero del bloque que abre la lista (la unidad del encabezado), con su herencia.
Sin los campos de la regla (forma, expresión del anuncio, candidatos, compatibilidad) y sin ningún veredicto.

Uso: python -I -B fichas_u2.py FUENTES SALIDA
FUENTES es una copia sin enlaces, armada con git show:
  FUENTES/u1/marco_u2_diez.json      (data/experiment/union_estrecha/salida/)
  FUENTES/u1/registro_u1_diez.json   (data/experiment/union_estrecha/salida/)
  FUENTES/ens_diez/kg.json           (el grafo a9631a64, registrado en data/experiment/neo4j/grafos.py)
  FUENTES/grafos.py                  (data/experiment/neo4j/grafos.py, solo se lee como texto)
  FUENTES/e0_r2b/chunks_<to>.json    (data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b/)
Escribe SALIDA/fichas_u2.json y SALIDA/fichas_u2.md. La salida no lleva hora: dos corridas dan los mismos bytes.
"""

import hashlib
import json
import re
import sys
from pathlib import Path

SHA_GRAFO = "a9631a64b422bdae634fb05135373c6f04c6272cdf7acd43a1be9f5b6c1f5f57"
SHA_MARCO = "69177a21e8e40cae12bf3fe97ac82a7349750e888ff61e4ea72adc7e6a6a097c"
CLAVE_GRAFOS = "KG_Tanda0_Diez_r2b"


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def sha_en_grafos_py(texto: str, clave: str) -> str:
    m = re.search(r'"%s":\s*\{(.*?)\n    \}' % re.escape(clave), texto, re.S)
    if m is None:
        raise SystemExit(f"{clave} no está en grafos.py")
    s = re.search(r'"sha256":\s*"([0-9a-f]{64})"', m.group(1))
    if s is None:
        raise SystemExit(f"{clave} sin sha256 en grafos.py")
    return s.group(1)


def provenances(nodo: dict) -> list:
    provs = nodo.get("provenances") or ([nodo["provenance"]] if nodo.get("provenance") else [])
    return [
        {
            "chunk_id": p.get("chunk_id"),
            "punto": p.get("punto"),
            "tramo": p.get("tramo"),
            "tramo_verificado": p.get("tramo_verificado"),
        }
        for p in provs
    ]


def nodo_ficha(nodo: dict) -> dict:
    return {
        "id": nodo["id"],
        "tipo": nodo["type"],
        "descripcion": (nodo.get("properties") or {}).get("descripcion"),
        "provenances": provenances(nodo),
    }


def unidad_ficha(chunk: dict) -> dict:
    return {
        "id": chunk["id"],
        "titulo": chunk.get("titulo"),
        "paginas": chunk.get("paginas"),
        "texto": chunk["texto"],
        "herencia": [
            {"tipo": h.get("tipo"), "unidad_origen": h.get("unidad_origen"), "texto": h.get("texto")}
            for h in (chunk.get("herencia") or [])
        ],
    }


def bloque(texto: str) -> list:
    if "```" in texto:
        raise SystemExit("texto con triple acento grave: el formato .md no lo admite")
    return ["```text", texto, "```"]


def md_nodo(titulo: str, n: dict) -> list:
    out = [f"### {titulo}", "", f"- id: `{n['id']}`", f"- tipo: {n['tipo']}", f"- descripción: {n['descripcion']}"]
    for i, p in enumerate(n["provenances"], 1):
        out.append(f"- tramo {i} (unidad `{p['chunk_id']}`, punto {p['punto']}, verificación {p['tramo_verificado']}):")
        out.append("")
        out += bloque(p["tramo"] or "")
    out.append("")
    return out


def md_unidad(titulo: str, u: dict) -> list:
    out = [f"### {titulo}: `{u['id']}`", "", f"- título: {u['titulo']}", f"- páginas: {u['paginas']}", "",
           "Texto propio de la unidad:", ""]
    out += bloque(u["texto"])
    out.append("")
    if u["herencia"]:
        out.append("Herencia de E0, en orden:")
        out.append("")
        for h in u["herencia"]:
            out.append(f"- {h['tipo']} de `{h['unidad_origen']}`:")
            out.append("")
            out += bloque(h["texto"] or "")
        out.append("")
    return out


def main() -> None:
    fuentes, salida = Path(sys.argv[1]), Path(sys.argv[2])
    p_marco = fuentes / "u1" / "marco_u2_diez.json"
    p_registro = fuentes / "u1" / "registro_u1_diez.json"
    p_kg = fuentes / "ens_diez" / "kg.json"
    if sha256(p_marco) != SHA_MARCO:
        raise SystemExit("marco_u2_diez.json no es el sellado en U1")
    if sha256(p_kg) != SHA_GRAFO or sha_en_grafos_py((fuentes / "grafos.py").read_text("utf-8"), CLAVE_GRAFOS) != SHA_GRAFO:
        raise SystemExit("el grafo no es a9631a64 o no coincide con su registro en grafos.py")

    marco = json.loads(p_marco.read_text("utf-8"))
    registro = json.loads(p_registro.read_text("utf-8"))
    if marco["grafo"] != SHA_GRAFO or registro["grafo"] != SHA_GRAFO:
        raise SystemExit("el marco o el registro no son del grafo a9631a64")
    ids = marco["marco"]
    if len(ids) != 29 or len(set(ids)) != 29:
        raise SystemExit("el marco no tiene 29 ids distintos")

    filas = {f["id"]: f for f in registro["registro"]}
    aristas = {(a["source"], a["target"], a["relation"]) for a in registro["aristas"]}
    kg = json.loads(p_kg.read_text("utf-8"))
    nodos = {n["id"]: n for n in kg["nodes"]}
    chunks, shas_e0 = {}, {}
    for p in sorted((fuentes / "e0_r2b").glob("chunks_*.json")):
        shas_e0[p.name] = sha256(p)
        for c in json.loads(p.read_text("utf-8")):
            chunks[c["id"]] = c

    fichas = []
    for i, cid in enumerate(ids, 1):
        f = filas[cid]
        if f["resultado"] != "union" or f["en_control_diagnostico"]:
            raise SystemExit(f"{cid}: no es una unión del marco")
        if (cid, f["destino"], "condicion_de") not in aristas:
            raise SystemExit(f"{cid}: sin arista en el registro")
        cond, dest = nodos[cid], nodos[f["destino"]]
        if cond["type"] != "Condicion":
            raise SystemExit(f"{cid}: el nodo no es Condicion")
        fichas.append({
            "ficha": f"U{i:02d}",
            "to": f["to"],
            "condicion": nodo_ficha(cond),
            "unidad_item": unidad_ficha(chunks[f["chunk_id"]]),
            "destino": nodo_ficha(dest),
            "unidad_encabezado": unidad_ficha(chunks[f["encabezado"]]),
        })

    doc = {
        "unidad": "U-UNION-ESTRECHA, U2",
        "contenido": "fichas sin veredicto de las 29 uniones del marco (censo), en el orden del marco",
        "fuentes": {
            "grafo": SHA_GRAFO,
            "marco_u2_diez.json": SHA_MARCO,
            "registro_u1_diez.json": sha256(p_registro),
            "e0_r2b": shas_e0,
        },
        "fichas": fichas,
    }
    salida.mkdir(parents=True, exist_ok=True)
    (salida / "fichas_u2.json").write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    md = ["# U-UNION-ESTRECHA, U2: fichas sin veredicto (29 uniones, censo del marco)", "",
          f"Grafo `{SHA_GRAFO[:8]}`; marco `{SHA_MARCO[:8]}`; registro `{sha256(p_registro)[:8]}`. "
          "Criterio de lectura: `criterio_u2.md`.", ""]
    for fi in fichas:
        md += [f"## {fi['ficha']}", ""]
        md += md_nodo("Condicion del ítem", fi["condicion"])
        md += md_unidad("Unidad del ítem", fi["unidad_item"])
        md += md_nodo("Nodo destino", fi["destino"])
        md += md_unidad("Unidad del encabezado (bloque que abre la lista)", fi["unidad_encabezado"])
    (salida / "fichas_u2.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    print(f"fichas: {len(fichas)}")
    print(f"unidades de ítem distintas: {len({fi['unidad_item']['id'] for fi in fichas})}")
    print(f"unidades de encabezado distintas: {len({fi['unidad_encabezado']['id'] for fi in fichas})}")


if __name__ == "__main__":
    main()
