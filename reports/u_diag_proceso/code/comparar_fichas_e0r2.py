"""U-DIAG-PROCESO, tarea 2: las diez fichas de los dos problemas, E0 de ESQ-2 (worksheet) contra
E0 e0-r2 (corrida de control del espejo). Solo lectura del repo. Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B comparar_fichas_e0r2.py <repo> <salida_e0r2> <out.json>
"""
import json
import re
import sys
from pathlib import Path

repo, e0r2, out = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
W = json.loads((repo / "data/experiment/esq/cobertura/fichas/worksheet_fichas_esq2.json").read_text())
FICHAS = {11: "F1", 13: "F1", 48: "F1", 52: "F1", 64: "F1",
          18: "VU", 39: "VU", 61: "VU", 72: "VU", 44: "VU-nota"}
norm = lambda s: " ".join((s or "").split())

chunks = {}
for f in sorted(e0r2.glob("chunks_*.json")):
    for c in json.loads(f.read_text()):
        chunks[c["id"]] = c

res = []
for fi in W["fichas"]:
    if fi["n"] not in FICHAS:
        continue
    cid = fi["chunk_id"]
    to, unidad = fi["to"], fi["unidad"]
    c = chunks.get(cid)
    tf = fi["texto_fuente"]
    her_ws = [(h["tipo"], h["unidad_origen"], norm(h["texto"])) for h in tf["contexto_heredado"]]
    her_r2 = [(h["tipo"], h["unidad_origen"], norm(h["texto"])) for h in (c or {}).get("herencia", [])]
    # unidades contenedoras de la ficha: ¿tienen mini-chunk propio en e0-r2?
    base = unidad.split("::")[0]
    comps = base.split(".")
    ancestros = [".".join(comps[:i]) for i in range(1, len(comps))]
    minis = {a: sorted(k for k in chunks if k.startswith(f"{to}::{a}::")) for a in ancestros}
    # encabezados heredados que terminan en ':' (el chapeau vive en la línea de título)
    enc_dos_puntos = [u for (t, u, x) in her_r2 if t == "encabezado" and x.rstrip().endswith(":")]
    # menciones explícitas de unidad en texto propio + heredado (regex amplia, informativa)
    texto_total = " ".join(x for (_, _, x) in her_r2) + " " + norm((c or {}).get("texto"))
    menciones = re.findall(r"(?:punto|puntos|apartado|Secci[oó]n|secci[oó]n)\s+\d+(?:\.\d+)*", texto_total)
    res.append({
        "ficha": fi["n"], "problema": FICHAS[fi["n"]], "chunk_id": cid,
        "existe_en_e0r2": c is not None,
        "tipo_e0r2": (c or {}).get("tipo"),
        "texto_propio_igual": c is not None and norm(c["texto"]) == norm(tf["texto_propio"]),
        "herencia_igual": her_ws == her_r2,
        "herencia_e0r2": her_r2,
        "minichunks_de_ancestros_e0r2": minis,
        "encabezados_heredados_que_terminan_en_dos_puntos": enc_dos_puntos,
        "menciones_explicitas_de_unidad": menciones,
    })

out.write_text(json.dumps(res, ensure_ascii=False, indent=1))
for r in res:
    print(r["ficha"], r["problema"], r["chunk_id"], "existe", r["existe_en_e0r2"],
          "propio=", r["texto_propio_igual"], "herencia=", r["herencia_igual"],
          "minis", {a: v for a, v in r["minichunks_de_ancestros_e0r2"].items() if v},
          "enc:", r["encabezados_heredados_que_terminan_en_dos_puntos"],
          "menc:", r["menciones_explicitas_de_unidad"])
