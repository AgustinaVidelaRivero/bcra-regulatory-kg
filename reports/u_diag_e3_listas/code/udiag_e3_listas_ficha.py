"""U-DIAG-E3-LISTAS: ficha de lectura de un faltante (solo lectura), sobre la copia de HEAD.

Para cada id «chunk|fase|intento|k»: el texto propio del ítem, la herencia (con el bloque que abre la lista
marcado), las entidades y relaciones de la extracción que E3 vio en ese intento (intento 0: validación de
extracciones_e1.jsonl; intento 1: tool_input de reintentos_e3.jsonl) y el faltante entero.

Uso: python ficha.py <copia> <id> [<id> ...]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

COPIA = Path(sys.argv[1]).resolve()
REX = COPIA / "data" / "experiment" / "reextraccion_v2"
sys.path.insert(0, str(REX / "e3_verificador"))
import comun_e3  # noqa: E402,F401
import prompt_r2b as R  # noqa: E402

SALIDA = REX / "corpus_tanda0" / "salida_r2b"
E0 = REX / "e0_chunking" / "salida_tanda0_r2b"


def jl(p: Path) -> list[dict]:
    if not p.exists():
        return []
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]


def chunk(cid: str) -> dict:
    to = cid.split("::")[0]
    d = json.loads((E0 / f"chunks_{to}.json").read_text(encoding="utf-8"))
    out = {c["id"]: c for c in (d["chunks"] if isinstance(d, dict) else d)}
    p = SALIDA / to / "particiones_por_corte.json"
    if p.exists():
        for base_id, v in json.loads(p.read_text(encoding="utf-8")).items():
            for parte in v["partes"]:
                b = dict(out[base_id])
                b.update({k: parte[k] for k in parte if k != "id"}, id=parte["id"])
                out[parte["id"]] = b
    return out[cid]


for fid in sys.argv[2:]:
    cid, fase, intento, k = fid.split("|")
    to = cid.split("::")[0]
    c = chunk(cid)
    i = R.bloque_lista(c)
    print("=" * 100)
    print(fid)
    for j, h in enumerate(c.get("herencia") or []):
        marca = "  <== ABRE LA LISTA" if j == i else ""
        print(f"[{h['tipo']} | punto {h['unidad_origen']}]{marca}")
        print("   ", " ".join(h["texto"].split())[:900])
    print(f"[texto propio | punto {c['unidad']}]")
    print("   ", " ".join(c["texto"].split())[:1500])
    if int(intento) == 0:
        r = next((x for x in jl(SALIDA / to / "extracciones_e1.jsonl") if x["chunk_id"] == cid), None)
        val = (r or {}).get("validacion") or {}
        ents, rels = val.get("entidades") or [], val.get("relaciones") or []
        oms = val.get("omisiones_no_prosa") or []
    else:
        r = next((x for x in jl(SALIDA / to / "reintentos_e3.jsonl")
                  if x["chunk_id"] == cid and x["intento"] == int(intento)), None)
        ti = (r or {}).get("tool_input") or {}
        ents, rels = ti.get("entities") or [], ti.get("relations") or []
        oms = [f"[{o.get('categoria')}] {o.get('tramo')}" for o in ti.get("omisiones") or [] if isinstance(o, dict)]
    print("-- EXTRACCIÓN QUE VIO E3:")
    for e in ents:
        if e.get("type") == "TextoOrdenado":
            continue
        d = (e.get("properties") or {}).get("descripcion")
        print(f"   {e.get('local_id')} {e.get('type')} «{e.get('label')}» — {(d or '')[:400]}")
    for rl in rels:
        if rl.get("predicate") == "establecida_en":
            continue
        print(f"   {rl.get('source')} -{rl.get('predicate')}-> {rl.get('target') or rl.get('sujeto_mencion')}")
    for o in oms:
        print("   OMISIÓN:", str(o)[:300])
    v = next(x for x in jl(SALIDA / to / "veredictos.jsonl")
             if x["chunk_id"] == cid and x["fase"] == fase and x["intento"] == int(intento))
    f = v["faltantes"][int(k)]
    print("-- FALTANTE:", json.dumps({x: f.get(x) for x in ("tipo", "severidad", "bloqueante", "cita_verificada")},
                                    ensure_ascii=False))
    print("   CITA:", " ".join((f.get("cita_textual_del_fuente") or "").split()))
    print("   NOTA:", f.get("nota"))
