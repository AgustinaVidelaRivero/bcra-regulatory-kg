"""U-DIAG-E3-LISTAS: para las unidades de flag «cola_humana» que son ítems de lista, ubica la cita de cada reclamo
bloqueante de la re-verificación (el que persistió) en el texto de E0: texto propio, bloque que abre la lista, otro
bloque heredado (tipo y unidad) o ninguno. Normalización: comun_e3.normalizar_para_cita.

Uso: python ubicar_citas_29.py <copia> <salida_dir>
"""
import json
import sys
from pathlib import Path

COPIA = Path(sys.argv[1]).resolve()
SAL = Path(sys.argv[2]).resolve()
REX = COPIA / "data" / "experiment" / "reextraccion_v2"
sys.path.insert(0, str(REX / "e3_verificador"))
import comun_e3  # noqa: E402
import prompt_r2b as R  # noqa: E402

SALIDA = REX / "corpus_tanda0" / "salida_r2b"
E0 = REX / "e0_chunking" / "salida_tanda0_r2b"
TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
N = comun_e3.normalizar_para_cita


def jl(p):
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()] if p.exists() else []


unidades = {u["chunk_id"]: u for u in json.loads((SAL / "fase1_unidades.json").read_text(encoding="utf-8"))}
out = []
for to in TOS:
    cola = {r["chunk_id"]: r["flag"] for r in jl(SALIDA / to / "cola_humana.jsonl")}
    sel = {u for u, f in cola.items() if f == "cola_humana" and unidades[u]["linea_item"]}
    if not sel:
        continue
    d = json.loads((E0 / f"chunks_{to}.json").read_text(encoding="utf-8"))
    ch = {c["id"]: c for c in (d["chunks"] if isinstance(d, dict) else d)}
    for v in jl(SALIDA / to / "veredictos.jsonl"):
        if v["chunk_id"] not in sel or v["intento"] != 1:
            continue
        c = ch[v["chunk_id"]]
        i = R.bloque_lista(c)
        for k, f in enumerate(v["faltantes"]):
            if not f.get("bloqueante"):
                continue
            cita = N(f.get("cita_textual_del_fuente") or "")
            donde = []
            if cita and cita in N(c["texto"]):
                donde.append("texto_propio")
            for j, h in enumerate(c.get("herencia") or []):
                if cita and cita in N(h["texto"]):
                    donde.append(("abre_lista:" if j == i else "heredado:") + f"{h['tipo']}|{h['unidad_origen']}")
            out.append({"id": f"{v['chunk_id']}|{v['fase']}|{v['intento']}|{k}", "tipo": f.get("tipo"),
                        "cita_verificada": f.get("cita_verificada"), "ubicacion_cita": donde or ["ninguna"]})
(SAL / "ubicacion_citas_29_items.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for x in out:
    print(x["id"], x["tipo"], x["cita_verificada"], x["ubicacion_cita"])
print(len(out), "reclamos en", len({x["id"].split("|")[0] for x in out}), "unidades")
