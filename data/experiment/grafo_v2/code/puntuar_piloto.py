#!/usr/bin/env python3
"""Score mecánico del piloto contra la answer key sellada (B1b, paso 3c).

Este script CUENTA EVIDENCIA — no cierra veredictos. Los casos con matiz
(recomposición de fórmulas, cuarentenas-señal-positiva según las notas de la
key) los adjudica la autora sobre esta salida.

Reglas mecánicas (las del mandato B1b):
- Normalización: NFD sin diacríticos + minúsculas + espacios colapsados +
  remoción de guiones de corte de línea ("-\\n").
- Los "nodos del chunk" son los nodos cuya provenance (source_doc, location)
  coincide con la del chunk de la muestra; ídem aristas. (Un nodo mergeado
  entre chunks conserva la provenance del primero — limitación documentada.)
- debe_contener: cada frase entrecomillada ('...') de la entrada se busca en
  labels + descriptions de los nodos del chunk; entrada = hit si TODAS sus
  frases aparecen (en cualquier nodo del chunk). Entradas con '↔': todos los
  términos deben aparecer en el MISMO nodo.
- no_debe_contener: un hallazgo de cualquier frase = violación (se lista dónde).
- sujetos_esperados / sujetos_prohibidos: presencia del id como extremo sujeto
  de aristas aplica_a (target) / ejecuta (source) del chunk.
- emparejamientos_prohibidos: ambos lados del '↔' en el MISMO nodo = violación.
- Entradas sin comillas: se usa el texto completo (sin comentarios entre
  paréntesis) como frase única — si no matchea, queda listada para adjudicación.

Uso:
    python puntuar_piloto.py --kg KG.json --key answer_key.json \
        --muestra muestra_piloto.json --out score.json
"""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from pathlib import Path


def norm(s: str) -> str:
    s = s.replace("-\n", "").replace("-\r\n", "")
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = s.lower()
    return re.sub(r"\s+", " ", s).strip()


def frases_de(entrada: str) -> list[str]:
    """Frases entrecomilladas de una entrada; si no hay, el texto completo
    sin comentarios entre paréntesis."""
    q = re.findall(r"'([^']+)'", entrada)
    if q:
        return q
    limpio = re.sub(r"\([^)]*\)", " ", entrada)
    limpio = limpio.strip(" .")
    return [limpio] if limpio.strip() else []


def lados_de(entrada: str) -> list[list[str]]:
    """Para entradas con '↔': lista de lados, cada lado = lista de términos."""
    lados = []
    for lado in entrada.split("↔"):
        lados.append(frases_de(lado))
    return [l for l in lados if l]


def texto_nodo(n: dict) -> str:
    props = n.get("properties") or {}
    partes = [n.get("label", "")]
    for k in ("description", "descripcion"):
        v = props.get(k)
        if v:
            partes.append(str(v))
    return norm(" | ".join(partes))


def puntuar(kg_path: Path, key_path: Path, muestra_path: Path) -> dict:
    kg = json.loads(kg_path.read_text(encoding="utf-8"))
    key = json.loads(key_path.read_text(encoding="utf-8"))
    muestra = json.loads(muestra_path.read_text(encoding="utf-8"))
    m_by_id = {m["chunk_id"]: m for m in muestra}

    nodes, edges = kg["nodes"], kg["edges"]

    por_chunk = []
    tot = {"debe_hits": 0, "debe_misses": 0, "no_debe_violaciones": 0,
           "suj_esperados_cubiertos": 0, "suj_esperados_faltantes": 0,
           "suj_prohibidos_aparecidos": 0, "emparejamientos_violados": 0,
           "emparejamientos_evaluados": 0}

    for entrada in key:
        cid = entrada["chunk_id"]
        m = m_by_id[cid]
        doc, loc = m["doc"], m["location"]

        nodos_chunk = [n for n in nodes
                       if (n.get("provenance") or {}).get("source_doc") == doc
                       and (n.get("provenance") or {}).get("location") == loc]
        aristas_chunk = [e for e in edges
                         if (e.get("provenance") or {}).get("source_doc") == doc
                         and (e.get("provenance") or {}).get("location") == loc]
        textos = {n["id"]: texto_nodo(n) for n in nodos_chunk}

        def en_algun_nodo(frase):
            f = norm(frase)
            return [nid for nid, t in textos.items() if f in t]

        def mismo_nodo(listas_de_terminos):
            """ids de nodos que contienen TODOS los términos de TODAS las listas."""
            hits = []
            for nid, t in textos.items():
                if all(all(norm(term) in t for term in lado) for lado in listas_de_terminos):
                    hits.append(nid)
            return hits

        # --- debe_contener ---
        debe = {"hits": [], "misses": []}
        for ent in entrada["debe_contener"]:
            if "↔" in ent:
                lados = lados_de(ent)
                donde = mismo_nodo(lados)
                if donde:
                    debe["hits"].append({"entrada": ent, "nodos": donde[:3]})
                else:
                    debe["misses"].append({"entrada": ent,
                                           "detalle": "requiere co-ocurrencia en el MISMO nodo; no hallada"})
            else:
                frases = frases_de(ent)
                faltan = [f for f in frases if not en_algun_nodo(f)]
                if not faltan:
                    debe["hits"].append({"entrada": ent})
                else:
                    debe["misses"].append({"entrada": ent, "frases_no_halladas": faltan})
        tot["debe_hits"] += len(debe["hits"])
        tot["debe_misses"] += len(debe["misses"])

        # --- no_debe_contener ---
        no_debe = {"violaciones": []}
        for ent in entrada["no_debe_contener"]:
            for f in frases_de(ent):
                donde = en_algun_nodo(f)
                if donde:
                    no_debe["violaciones"].append({"entrada": ent, "frase": f, "nodos": donde[:5]})
        tot["no_debe_violaciones"] += len(no_debe["violaciones"])

        # --- sujetos ---
        sujetos_obs = set()
        for e in aristas_chunk:
            if e["relation"] == "aplica_a":
                sujetos_obs.add(e["target"])
            elif e["relation"] == "ejecuta":
                sujetos_obs.add(e["source"])
        esperados = entrada["sujetos_esperados"]
        prohibidos = entrada["sujetos_prohibidos"]
        cubiertos = [s for s in esperados if s in sujetos_obs]
        faltantes = [s for s in esperados if s not in sujetos_obs]
        aparecidos = [s for s in prohibidos if s in sujetos_obs]
        tot["suj_esperados_cubiertos"] += len(cubiertos)
        tot["suj_esperados_faltantes"] += len(faltantes)
        tot["suj_prohibidos_aparecidos"] += len(aparecidos)

        # --- emparejamientos_prohibidos ---
        emp = {"violaciones": [], "no_evaluables": []}
        for ent in entrada["emparejamientos_prohibidos"]:
            if "↔" not in ent:
                emp["no_evaluables"].append({"entrada": ent, "motivo": "sin '↔' — adjudicación manual"})
                continue
            lados = lados_de(ent)
            if len(lados) < 2:
                emp["no_evaluables"].append({"entrada": ent, "motivo": "lado vacío tras limpieza"})
                continue
            donde = mismo_nodo(lados)
            tot["emparejamientos_evaluados"] += 1
            if donde:
                emp["violaciones"].append({"entrada": ent, "nodos": donde[:5]})
        tot["emparejamientos_violados"] += len(emp["violaciones"])

        por_chunk.append({
            "chunk_id": cid,
            "caso_bestiario": entrada["caso_bestiario"],
            "n_nodos_chunk": len(nodos_chunk),
            "n_aristas_chunk": len(aristas_chunk),
            "debe_contener": debe,
            "no_debe_contener": no_debe,
            "sujetos": {"observados": sorted(sujetos_obs), "cubiertos": cubiertos,
                        "faltantes": faltantes, "prohibidos_aparecidos": aparecidos},
            "emparejamientos_prohibidos": emp,
            "notas_key": entrada.get("notas", ""),
        })

    return {"kg": str(kg_path), "totales": tot, "por_chunk": por_chunk}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kg", required=True, type=Path)
    ap.add_argument("--key", required=True, type=Path)
    ap.add_argument("--muestra", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()

    score = puntuar(args.kg, args.key, args.muestra)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(score, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    t = score["totales"]
    print(f"SCORE {args.kg.name}")
    print(f"  debe_contener: {t['debe_hits']} hits / {t['debe_misses']} misses")
    print(f"  no_debe_contener: {t['no_debe_violaciones']} violaciones")
    print(f"  sujetos esperados: {t['suj_esperados_cubiertos']} cubiertos / {t['suj_esperados_faltantes']} faltantes")
    print(f"  sujetos prohibidos aparecidos: {t['suj_prohibidos_aparecidos']}")
    print(f"  emparejamientos: {t['emparejamientos_violados']} violados / {t['emparejamientos_evaluados']} evaluados")
    for ch in score["por_chunk"]:
        d, nd, s, e = ch["debe_contener"], ch["no_debe_contener"], ch["sujetos"], ch["emparejamientos_prohibidos"]
        print(f"  - {ch['chunk_id'].replace('TO_','').replace('_actual.pdf','')} [{ch['caso_bestiario']}]: "
              f"debe {len(d['hits'])}/{len(d['hits'])+len(d['misses'])} | no_debe viol {len(nd['violaciones'])} | "
              f"suj {len(s['cubiertos'])}/{len(s['cubiertos'])+len(s['faltantes'])} cub, {len(s['prohibidos_aparecidos'])} prohib | "
              f"emp viol {len(e['violaciones'])}")
    print(f"Salida: {args.out}")


if __name__ == "__main__":
    main()
