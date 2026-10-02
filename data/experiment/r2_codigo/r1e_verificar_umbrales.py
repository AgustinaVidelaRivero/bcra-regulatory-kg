"""U-R2-CODIGO, R1.e — verificación de los valores de los nodos contra las
tablas de la E0 e0-r2, como marca y sin corregir (regla en
verificacion_tablas.py). Corre sobre KG-Tanda0-Desarrollo-r1, KG-Tanda0-Diez-r1
y KG-Reextraído-r1 (solo lectura, con candado de sha256) y escribe: conteo de
nodos y valores por veredicto, nodos marcados, el caso de control `cap::1.2`
y los casos adicionales `ric::7.2` y `ric::9.2` (pérdidas reales de D2 de
U-PRE-R2-DIAG). La corrección del valor exige re-extraer: este paso solo
marca. USD 0, sin LLM.

Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B \\
    data/experiment/r2_codigo/r1e_verificar_umbrales.py --e0-r2 <salida e0-r2> --out <json>
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[2]
sys.path.insert(0, str(AQUI))
import verificacion_tablas as VT  # noqa: E402

REX = REPO / "data" / "experiment" / "reextraccion_v2"
GRAFOS = {
    "KG-Tanda0-Desarrollo-r1": (REX / "corpus_tanda0" / "ens_desarrollo" / "r1" / "kg.json",
                                "eab2fdd0"),
    "KG-Tanda0-Diez-r1": (REX / "corpus_tanda0" / "ens_diez" / "r1" / "kg.json", "dd42d6d9"),
    "KG-Reextraido-r1": (REX / "corpus_v2" / "salida_r1" / "kg.json", "0226e947"),
}
NO_CONTENIDO = {"TextoOrdenado", "Sujeto", "Sujeto_propuesto", "Comunicacion"}
CASOS = ("cap::1.2", "ric::7.2", "ric::9.2")


def _chunks_de(n: dict) -> list[str]:
    out = []
    for p in [n.get("provenance") or {}] + list(n.get("provenances") or []):
        c = p.get("chunk_id")
        if c and c not in out:
            out.append(c)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--e0-r2", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    tablas_por_chunk: dict[str, list[dict]] = collections.defaultdict(list)
    estado_tablas: dict[str, list[dict]] = collections.defaultdict(list)
    for p in sorted(Path(a.e0_r2).glob("tablas_*.json")):
        for t in json.loads(p.read_text(encoding="utf-8"))["tablas"]:
            if t["marca"]:
                tablas_por_chunk[t["chunks"][0]].append(t)
                estado_tablas[t["chunks"][0]].append(
                    {"tabla": t["id"], "serializada": t["serializacion"]["serializada"],
                     "motivo": t["serializacion"].get("motivo"),
                     "modo": t["serializacion"].get("modo")})
    out = {"unidad": "U-R2-CODIGO", "etapa": "R1.e", "grafos": {}}
    for nombre, (ruta, prefijo) in GRAFOS.items():
        sha = hashlib.sha256(ruta.read_bytes()).hexdigest()
        if not sha.startswith(prefijo):
            raise SystemExit(f"{nombre}: sha {sha[:8]} no es el sellado {prefijo}")
        kg = json.loads(ruta.read_text(encoding="utf-8"))
        por_nodo = collections.Counter()
        por_valor = collections.Counter()
        marcados, casos = [], {c: [] for c in CASOS}
        for n in kg["nodes"]:
            if n.get("type") in NO_CONTENIDO:
                continue
            chunks = _chunks_de(n)
            for caso in CASOS:
                if any(c == caso or c.startswith(caso + ".") for c in chunks):
                    casos[caso].append(n)
            tablas = [t for c in chunks for t in tablas_por_chunk.get(c, [])]
            if not tablas:
                continue
            r = VT.verificar_nodo(n, tablas)
            por_nodo["evaluados"] += 1
            for v in r["valores"]:
                por_valor[v["veredicto"]] += 1
            if r["marca"]:
                por_nodo["marcados"] += 1
                marcados.append({"nodo": n["id"], "chunks": chunks,
                                 "valores": [v for v in r["valores"]
                                             if v["veredicto"] != "fuera_de_tabla"]})
        casos_out = {}
        for caso, nodos in casos.items():
            casos_out[caso] = []
            for n in nodos:
                tablas = [t for c in _chunks_de(n) for t in tablas_por_chunk.get(c, [])]
                r = VT.verificar_nodo(n, tablas) if tablas else None
                casos_out[caso].append({
                    "nodo": n["id"], "tipo": n["type"], "chunks": _chunks_de(n),
                    "umbral": n.get("properties", {}).get("umbral"),
                    "marca": r["marca"] if r else None,
                    "valores": [v for v in r["valores"] if v["veredicto"] != "fuera_de_tabla"]
                    if r else []})
        out["grafos"][nombre] = {"sha256": sha, "nodos": dict(sorted(por_nodo.items())),
                                 "valores_por_veredicto": dict(sorted(por_valor.items())),
                                 "marcados": marcados, "casos": casos_out}
    out["tablas_de_los_casos"] = {c: v for c, v in sorted(estado_tablas.items())
                                  if any(c == k or c.startswith(k + ".") for k in CASOS)}
    out["declaracion"] = ("La corrección del valor exige re-extraer: en r2a el test C2 y el "
                          "de BKL-0006 siguen en «persiste»; la marca no corrige el grafo.")
    Path(a.out).write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n",
                           encoding="utf-8")


if __name__ == "__main__":
    main()
