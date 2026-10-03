import json, sys
from pathlib import Path
S = Path(sys.argv[1]); M = S / "espejo"
sys.path.insert(0, str(M / "data/experiment/reextraccion_v2/corpus_v2"))
import r1_referencias as RR
W = json.loads((M / "data/experiment/esq/cobertura/fichas/worksheet_fichas_esq2.json").read_text(encoding="utf-8"))
byn = {x["n"]: x for x in W["fichas"]}
FICHAS = [11, 13, 48, 52, 64, 18, 39, 61, 72, 44]
salida = {}
cache = {}
def chunks(to):
    if to not in cache:
        d = json.loads((S / "e0r2_seis" / f"chunks_{to}.json").read_text(encoding="utf-8"))
        cache[to] = d["chunks"] if isinstance(d, dict) else d
    return cache[to]
for n in FICHAS:
    f = byn[n]; to = f["to"]; cid = f["chunk_id"]
    cs = {c["id"]: c for c in chunks(to)}
    c = cs.get(cid)
    r = {"chunk_id": cid, "existe_en_e0r2": c is not None}
    if c:
        her_ws = [(h["tipo"], h["unidad_origen"], h["texto"]) for h in f["texto_fuente"]["contexto_heredado"]]
        her_r2 = [(h["tipo"], h["unidad_origen"], h["texto"]) for h in c["herencia"]]
        r["texto_igual"] = c["texto"] == f["texto_fuente"]["texto_propio"]
        r["herencia_igual"] = her_ws == her_r2
        r["flags_e0r2"] = {k: v for k, v in (c.get("flags") or {}).items() if v}
        # unidades de los bloques heredados: cuales tienen chunk propio (mini_chunk)
        r["herencia_con_unidad"] = []
        for (tipo, uo, tx) in her_r2:
            minis = [k for k in cs if k.startswith(f"{to}::{uo}::")]
            r["herencia_con_unidad"].append({"tipo": tipo, "unidad_origen": uo,
                                             "mini_chunks_de_esa_unidad": minis,
                                             "texto": tx[:160]})
        # regla (i): citas en el texto heredado y en el propio
        men_her = []
        for (tipo, uo, tx) in her_r2:
            for m in RR.detectar_menciones_r2(tx, to):
                men_her.append({"tramo": f"{tipo}|{uo}", "mencion": {k: m.get(k) for k in ("unidades", "clase", "to_destino", "evidencia", "causa") if k in m}})
        r["citas_en_herencia_r2"] = men_her
        r["citas_en_texto_propio_r2"] = [{k: m.get(k) for k in ("unidades", "clase", "to_destino", "evidencia", "causa") if k in m}
                                         for m in RR.detectar_menciones_r2(c["texto"], to)]
    salida[n] = r
json.dump(salida, sys.stdout, ensure_ascii=False, indent=1)
