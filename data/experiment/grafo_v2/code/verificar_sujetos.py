"""Verificador léxico de sujetos — post-hoc, determinístico, sin API (U4d).

Para cada arista aplica_a/ejecuta de un kg.json v2 cuyo extremo sujeto sea una
clase o instancia del esqueleto: recupera el texto del chunk de provenance
(match por (doc, location) → chunk_id contra los chunks guardados en el caché)
y verifica, con normalización NFD + minúsculas + de-guionado de saltos de
línea, si el texto contiene el label o algún alias de la clase asignada.
Para destinos nivel rol: verifica lenguaje colectivo (label/alias del rol o
frases genéricas "sujetos obligados" / "las entidades" / "los sujetos").

SIN auto-corrección: solo detección. Salida: sujetos_sospechosos.json (junto
al kg de entrada) + listado en consola con norma, sujeto asignado, chunk y
los primeros 200 chars del texto.

Uso:
    python verificar_sujetos.py <kg.json> <cache_dir>
    # cache_dir: directorio que contiene los chunks_*.json de la corrida
    # (con el campo `text` por chunk); se escanea recursivamente.
"""

from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path
from typing import Any

from schema import CATALOGO_PATH

FRASES_COLECTIVAS = [
    "sujetos obligados", "las entidades", "los sujetos",
    # U4e: variantes en singular del genérico regulatorio (calibradas en U4d:
    # el 100% de los falsos positivos del smoke usaba el singular).
    "el sujeto obligado", "la entidad", "el sujeto",
]


def normalizar(s: str) -> str:
    """NFD sin combinantes + minúsculas + de-guionado de cortes de línea del
    PDF ("fi-\\nnancieras" → "financieras") + espacios colapsados."""
    s = s.replace("-\n", "").replace("-\r\n", "")
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower()
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def terminos_de(entry: dict[str, Any]) -> list[str]:
    """Términos de matcheo de una entrada del catálogo: label + alias.
    Los labels "X (Y)" aportan además X e Y por separado (ej. "Entidades de
    contraparte central (CCP)" → también "Entidades de contraparte central"
    y "CCP")."""
    terms: list[str] = []
    label = entry.get("label", "")
    terms.append(label)
    m = re.match(r"^(.*?)\s*\((.+)\)\s*$", label)
    if m:
        terms.append(m.group(1))
        terms.append(m.group(2))
    terms.extend(entry.get("alias") or [])
    return [normalizar(t) for t in terms if t and t.strip()]


def cargar_chunks(cache_dir: Path) -> list[dict[str, Any]]:
    """Carga TODOS los chunks con texto del caché (recursivo, chunks_*.json).

    NO dedupea por chunk_id: el chunker emite chunk_ids repetidos (numeración
    que aparece como header real Y como referencia/índice) y la provenance de
    una arista no distingue cuál de los duplicados alimentó la extracción —
    se verifican todos los textos candidatos (lectura conservadora: si ALGUNO
    menciona al sujeto, la arista no es sospechosa). Se dedupea solo por
    contenido exacto (mismo chunk en varios archivos del caché)."""
    vistos: set[tuple[str, str]] = set()
    out: list[dict[str, Any]] = []
    for fp in sorted(cache_dir.rglob("*.json")):
        try:
            data = json.loads(fp.read_text(encoding="utf-8"))
        except Exception:
            continue
        if isinstance(data, list):
            for item in data:
                if isinstance(item, dict) and "chunk_id" in item and "text" in item:
                    key = (item["chunk_id"], item["text"])
                    if key not in vistos:
                        vistos.add(key)
                        out.append(item)
    return out


def main() -> int:
    if len(sys.argv) != 3:
        print("Uso: python verificar_sujetos.py <kg.json> <cache_dir>")
        return 1
    kg_path = Path(sys.argv[1]).resolve()
    cache_dir = Path(sys.argv[2]).resolve()

    kg = json.loads(kg_path.read_text(encoding="utf-8"))
    catalogo = json.loads(CATALOGO_PATH.read_text(encoding="utf-8"))

    nodes_by_id = {n["id"]: n for n in kg["nodes"]}
    cat_by_id: dict[str, dict[str, Any]] = {e["id"]: e for e in catalogo["clases"]}
    for r in catalogo["roles"]:
        cat_by_id[r["id"]] = r

    chunks = cargar_chunks(cache_dir)
    if not chunks:
        print(f"ERROR: no encontré chunks con texto (chunks_*.json) bajo {cache_dir}")
        return 1
    # Índice (doc, location) → chunks (una location puede tener >1 chunk por
    # la numeración repetida del chunker; se verifican todos los textos).
    chunks_by_loc: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for ch in chunks:
        chunks_by_loc.setdefault((ch["doc"], ch["location"]), []).append(ch)

    sospechosas: list[dict[str, Any]] = []
    verificadas = 0
    ok = 0
    sin_chunk = 0
    salteadas_propuesto = 0

    for e in kg["edges"]:
        rel = e["relation"]
        if rel not in ("aplica_a", "ejecuta"):
            continue
        sujeto_id = e["target"] if rel == "aplica_a" else e["source"]
        norma_id = e["source"] if rel == "aplica_a" else e["target"]
        sujeto_node = nodes_by_id.get(sujeto_id)
        if sujeto_node is None or sujeto_node.get("type") != "Sujeto":
            continue
        nivel = sujeto_node.get("properties", {}).get("nivel")
        if nivel == "propuesto":
            salteadas_propuesto += 1
            continue  # los propuestos llevan el nombre textual del chunk por construcción
        entry = cat_by_id.get(sujeto_id)
        if entry is None:
            continue

        verificadas += 1
        prov = e.get("provenance", {})
        key = (prov.get("source_doc", ""), prov.get("location", ""))
        candidatos = chunks_by_loc.get(key, [])
        if not candidatos:
            sin_chunk += 1
            sospechosas.append({
                "motivo": "sin_chunk_en_cache",
                "relation": rel,
                "norma": norma_id,
                "sujeto": sujeto_id,
                "nivel": nivel,
                "provenance": prov,
                "chunk_id": None,
                "texto_inicio": None,
                "terminos_buscados": [],
            })
            continue

        if nivel == "rol":
            terms = terminos_de(entry) + [normalizar(f) for f in FRASES_COLECTIVAS]
        else:  # clase o instancia
            terms = terminos_de(entry)

        hallado = False
        for ch in candidatos:
            texto_norm = normalizar(ch["text"])
            if any(t in texto_norm for t in terms):
                hallado = True
                break

        if hallado:
            ok += 1
        else:
            ch0 = candidatos[0]
            sospechosas.append({
                "motivo": "sujeto_no_mencionado_en_chunk",
                "relation": rel,
                "norma": norma_id,
                "sujeto": sujeto_id,
                "nivel": nivel,
                "provenance": prov,
                "chunk_id": ch0["chunk_id"],
                "texto_inicio": re.sub(r"\s+", " ", ch0["text"])[:200],
                "terminos_buscados": terms,
            })

    out_path = kg_path.parent / "sujetos_sospechosos.json"
    out_path.write_text(json.dumps(sospechosas, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Verificador léxico de sujetos — kg: {kg_path}")
    print(f"chunks con texto indexados: {len(chunks)}")
    print(f"aristas sujeto verificadas: {verificadas} (saltadas por nivel=propuesto: {salteadas_propuesto})")
    print(f"OK (mención hallada): {ok} | SOSPECHOSAS: {len(sospechosas)} (de las cuales sin_chunk: {sin_chunk})")
    print()
    for s in sospechosas:
        print(f"[SOSPECHOSA] {s['relation']}: {s['norma']}")
        print(f"    sujeto asignado: {s['sujeto']} (nivel {s['nivel']})")
        print(f"    chunk: {s['chunk_id']}  |  provenance: {s['provenance'].get('location', '')[:80]}")
        if s["texto_inicio"]:
            print(f"    texto[:200]: {s['texto_inicio']}")
        print()
    print(f"Salida: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
