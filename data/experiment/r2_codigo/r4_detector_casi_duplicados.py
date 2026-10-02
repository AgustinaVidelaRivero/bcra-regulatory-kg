"""U-R2-CODIGO, R4.a — `BKL-0031`, paso 1: detector de candidatos a duplicado,
de solo lectura (laudo de r2, §1.2). Reporta pares con su diff y no funde.
USD 0.

Criterio de candidato (laudo de r2, §1.2, paso 1):
  - mismo tipo de nodo;
  - mismo sujeto: el mismo conjunto de nodos Sujeto unidos al nodo por alguna
    arista (en cualquier sentido); dos nodos sin sujeto cuentan como «mismo
    sujeto» y el par lo marca (`sin_sujeto`);
  - texto similar por RapidFuzz con el protocolo de M2
    (`scripts/metricas_intrinsecas.py`: `fuzz.ratio` sobre
    `normalizar_superficie` del label, umbral 75, `:96` y `:144-160`); se
    informa también la similitud de M1 (`fuzz.partial_ratio` sobre el label
    crudo), que no decide;
  - mismo documento (algún TO de procedencia en común) o documentos unidos
    por una arista `referencia` entre nodos de uno y otro.
Cada par lleva el diff por palabras de los labels y, si los dos nodos tienen
`descripcion`, el de las descripciones, con dos marcas para la adjudicación del
paso 2: `diff_toca_valores` (números, porcentajes, fechas o plazos en las
palabras que cambian) y `mismo_texto_normalizado`.

Grafos: KG-Reextraído-r1 y los tres ensamblados de la tanda 0 (desarrollo,
diez y cinco). Salida determinística (sin fechas): dos corridas dan el mismo
JSON.

Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/r2_codigo/r4_detector_casi_duplicados.py --out <json>
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

from rapidfuzz import fuzz, process

REPO = Path(__file__).resolve().parents[3]
if str(REPO / "scripts") not in sys.path:
    sys.path.insert(0, str(REPO / "scripts"))

REX = REPO / "data" / "experiment" / "reextraccion_v2"
GRAFOS = {
    "KG-Reextraido-r1": REX / "corpus_v2" / "salida_r1" / "kg.json",
    "KG-Tanda0-Desarrollo-r1": REX / "corpus_tanda0" / "ens_desarrollo" / "r1" / "kg.json",
    "KG-Tanda0-Diez-r1": REX / "corpus_tanda0" / "ens_diez" / "r1" / "kg.json",
    "KG-Tanda0-Cinco-r1": REX / "corpus_tanda0" / "ens_cinco" / "r1" / "kg.json",
}
UMBRAL = 75.0
MUESTRA_POR_TIPO = 5
RE_VALOR = re.compile(r"\d|%|\b(?:d[ií]as?|mes(?:es)?|a[nñ]os?|h[aá]biles|corridos|veces)\b", re.I)


def normalizar_superficie(s: str) -> str:
    """Copia textual de scripts/metricas_intrinsecas.normalizar_superficie
    (importar ese módulo carga los ensambladores sellados)."""
    import unicodedata
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", " ", s).strip()
    return s


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def tos_de(n: dict) -> set[str]:
    out = set()
    for p in n.get("provenances") or [n.get("provenance") or {}]:
        to = p.get("to") or p.get("archivo")
        if to:
            out.add(to)
    return out


def diff_palabras(a: str, b: str) -> list[str]:
    return [t for t in difflib.ndiff((a or "").split(), (b or "").split()) if t[:1] in "+-"]


def detectar(kg: dict) -> dict:
    nodos = {n["id"]: n for n in kg["nodes"]}
    sujetos: dict[str, set] = defaultdict(set)
    enlazados: set[frozenset] = set()
    for e in kg["edges"]:
        s, t = e["source"], e["target"]
        if nodos.get(t, {}).get("type") == "Sujeto" and nodos.get(s, {}).get("type") != "Sujeto":
            sujetos[s].add(t)
        if nodos.get(s, {}).get("type") == "Sujeto" and nodos.get(t, {}).get("type") != "Sujeto":
            sujetos[t].add(s)
        if e["relation"] == "referencia":
            for a in tos_de(nodos[s]):
                for b in tos_de(nodos[t]):
                    if a != b:
                        enlazados.add(frozenset((a, b)))
    grupos: dict[tuple, list[str]] = defaultdict(list)
    for n in kg["nodes"]:
        if n["type"] in ("Sujeto", "TextoOrdenado", "Comunicacion"):
            continue
        grupos[(n["type"], frozenset(sujetos.get(n["id"], set())))].append(n["id"])
    pares = []
    for (tipo, suj), ids in sorted(grupos.items(), key=lambda kv: (kv[0][0], sorted(kv[0][1]))):
        ids = sorted(ids)
        if len(ids) < 2:
            continue
        labels = [normalizar_superficie(nodos[i].get("label", "")) for i in ids]
        m = process.cdist(labels, labels, scorer=fuzz.ratio, dtype=None)
        for i in range(len(ids)):
            for j in range(i + 1, len(ids)):
                if m[i][j] < UMBRAL:
                    continue
                a, b = nodos[ids[i]], nodos[ids[j]]
                ta, tb = tos_de(a), tos_de(b)
                if ta & tb:
                    doc = "mismo_documento"
                elif any(frozenset((x, y)) in enlazados for x in ta for y in tb):
                    doc = "documentos_unidos_por_referencia"
                else:
                    continue
                dl = diff_palabras(a.get("label", ""), b.get("label", ""))
                da, db = (a.get("properties") or {}).get("descripcion"), (b.get("properties") or {}).get("descripcion")
                dd = diff_palabras(da, db) if isinstance(da, str) and isinstance(db, str) else None
                cambios = dl + (dd or [])
                pares.append({
                    "tipo": tipo, "a": ids[i], "b": ids[j], "documento": doc, "sin_sujeto": not suj,
                    "sujetos": sorted(suj), "similitud_m2": round(float(m[i][j]), 2),
                    "similitud_m1": round(float(fuzz.partial_ratio(a.get("label", ""), b.get("label", ""))), 2),
                    "mismo_texto_normalizado": labels[i] == labels[j],
                    "diff_toca_valores": any(RE_VALOR.search(t[2:]) for t in cambios),
                    "label_a": a.get("label"), "label_b": b.get("label"),
                    "puntos_a": sorted({f"{p.get('to')}::{p.get('punto')}" for p in a.get("provenances") or []}),
                    "puntos_b": sorted({f"{p.get('to')}::{p.get('punto')}" for p in b.get("provenances") or []}),
                    "diff_label": dl, "diff_descripcion": dd})
    por_tipo = Counter(p["tipo"] for p in pares)
    muestras = {t: [p for p in pares if p["tipo"] == t][:MUESTRA_POR_TIPO] for t in sorted(por_tipo)}
    nodos_en_pares = {x for p in pares for x in (p["a"], p["b"])}
    return {"nodos": len(kg["nodes"]), "pares_candidatos": len(pares),
            "nodos_en_algun_par": len(nodos_en_pares),
            "por_tipo": dict(sorted(por_tipo.items())),
            "por_documento": dict(sorted(Counter(p["documento"] for p in pares).items())),
            "sin_sujeto": sum(p["sin_sujeto"] for p in pares),
            "diff_toca_valores": sum(p["diff_toca_valores"] for p in pares),
            "mismo_texto_normalizado": sum(p["mismo_texto_normalizado"] for p in pares),
            "muestras": muestras, "pares": pares}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    out = {"unidad": "U-R2-CODIGO", "etapa": "R4.a, BKL-0031 paso 1 (solo lectura)",
           "criterio": {"umbral_m2": UMBRAL, "scorer": "rapidfuzz.fuzz.ratio sobre normalizar_superficie(label)",
                        "informativo": "rapidfuzz.fuzz.partial_ratio sobre el label crudo (M1)",
                        "documento": "TO de procedencia en común o TOs unidos por una arista referencia",
                        "sujeto": "mismo conjunto de nodos Sujeto adyacentes"},
           "grafos": {}}
    for nombre, p in GRAFOS.items():
        r = detectar(json.loads(p.read_text(encoding="utf-8")))
        out["grafos"][nombre] = {"ruta": str(p.relative_to(REPO)), "sha256": sha256(p), **r}
        print(nombre, {k: v for k, v in r.items() if k not in ("muestras", "pares")}, flush=True)
    Path(a.out).write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
