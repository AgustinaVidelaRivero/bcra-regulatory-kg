"""B6.1, tanda final, T3, punto 4: la causa de un FAIL de S31 con la E0 de cada grafo, en los ocho grafos, por id y sin texto (es
data/experiment/tanda1/t3/scripts/causa_s31_t3.py con los ocho grafos; la cuenta, igual). Para cada grafo, las aristas
`remite_a` cuyo chunk de procedencia no está en la E0 del grafo (la misma cuenta que `chunk_no_encontrado` de S31,
scripts/shapes_validator.py:1361-1410, antes de mirar otras procedencias), agrupadas por chunk_id; y, aparte, las `remite_a` de toda
procedencia que sea una parte por corte (`::parteN`). Solo lee.
Uso: python3 -I -B causa_s31_tf.py <raíz> <salida.json>"""
import json
import sys
from collections import Counter
from pathlib import Path

RAIZ, OUT = Path(sys.argv[1]), Path(sys.argv[2])
X = "data/experiment/reextraccion_v2"
T = f"{X}/corpus_tanda_final"
A = "data/experiment/tanda_final/t3/acumulado"
EF = f"{X}/e0_chunking/salida_tanda_final_r2b"
GRAFOS = {"tf98": (f"{T}/ens_98_r2b", EF), "tf98_sincola": (f"{T}/ens_98_r2b_sincola", EF),
          "tf_tramo1": (f"{T}/ens_tramo1_r2b", EF), "tf_tramo1_sincola": (f"{T}/ens_tramo1_r2b_sincola", EF),
          "acum128": (f"{A}/ens_128_r2b", f"{A}/e0_acumulado_128_r2b"), "acum128_sincola": (f"{A}/ens_128_r2b_sincola", f"{A}/e0_acumulado_128_r2b"),
          "acum60": (f"{A}/ens_60_tramo1_r2b", f"{A}/e0_acumulado_60_r2b"),
          "acum60_sincola": (f"{A}/ens_60_tramo1_r2b_sincola", f"{A}/e0_acumulado_60_r2b")}


def ids_e0(e0: Path) -> dict[str, set]:
    out = {}
    for p in e0.glob("chunks_*.json"):
        d = json.loads(p.read_text(encoding="utf-8"))
        out[p.stem[len("chunks_"):]] = {c["id"] for c in (d["chunks"] if isinstance(d, dict) else d)}
    return out


res = {}
for g, (ens, e0) in GRAFOS.items():
    ids = ids_e0(RAIZ / e0)
    kg = json.loads((RAIZ / ens / "r2/kg.json").read_text(encoding="utf-8"))
    rem = [e for e in kg["edges"] if e["relation"] == "remite_a"]
    falta, de_partes = Counter(), Counter()
    for e in rem:
        pv = e.get("provenance") or {}
        cid = pv.get("chunk_id") or ""
        to = pv.get("to") or (cid.split("::", 1)[0] if "::" in cid else None)
        if cid not in ids.get(to, set()):
            falta[cid] += 1
        partes = {((p or {}).get("chunk_id") or "") for p in [pv] + list(e.get("provenances") or [])}
        for c in partes:                      # cada arista una vez por parte, aunque `provenances` repita la `provenance`
            if "::parte" in c:
                de_partes[c] += 1
    res[g] = {"ensamblado": ens, "e0": e0, "remite_a": len(rem), "con_chunk_de_procedencia_fuera_de_la_e0": sum(falta.values()),
              "por_chunk": dict(sorted(falta.items())),
              "todos_son_partes_por_corte": all("::parte" in c for c in falta),
              "remite_a_con_alguna_procedencia_en_una_parte": dict(sorted(de_partes.items()))}
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for g, v in res.items():
    print(g, v["remite_a"], "| fuera de la E0:", v["con_chunk_de_procedencia_fuera_de_la_e0"], v["por_chunk"],
          "| todas partes:", v["todos_son_partes_por_corte"])
