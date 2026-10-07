"""U-DIAG-E3-LISTAS, fase 2 (solo lectura, USD 0), sobre la copia de HEAD.

1. Amplía los candidatos de la fase 1: suma los faltantes de las unidades con LINEA_ITEM cuya nota nombra el
   local_id de una entidad Excepcion de la extracción que E3 vio (intento 0: validación de extracciones_e1.jsonl;
   intento 1: tool_input del reintento en reintentos_e3.jsonl). Escribe la lista completa a adjudicar.
2. Indicador mecánico de generalidad: faltantes cuya nota dice que lo extraído trae contenido que no está en el
   fuente o que invierte el sentido (RE_AGREGADO), por grupo: ítems cuyo bloque que abre la lista no llega a E3,
   ítems cuyo bloque llega (tipo encabezado) y unidades que no son ítem.
3. Sorteo (semilla fija) de 15 faltantes del indicador en los ítems cuyo bloque no llega a E3, para leer después.

Uso: python fase2_candidatos_y_generalidad.py <copia> <salida_dir>
"""
from __future__ import annotations

import json
import random
import re
import sys
import unicodedata
from collections import Counter
from datetime import datetime
from pathlib import Path

COPIA = Path(sys.argv[1]).resolve()
SAL = Path(sys.argv[2]).resolve()
REX = COPIA / "data" / "experiment" / "reextraccion_v2"
SALIDA = REX / "corpus_tanda0" / "salida_r2b"
TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
SEMILLA = 20261006


def jl(p: Path) -> list[dict]:
    if not p.exists():
        return []
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]


def norm(t: str) -> str:
    t = unicodedata.normalize("NFKD", t or "")
    t = "".join(ch for ch in t if not unicodedata.combining(ch))
    return " ".join(t.lower().split())


RE_EXC = re.compile(r"excep|exceptu|salvo|excepto")
RE_AGREGADO = re.compile(r"agreg|no figura en|no aparece en el (texto )?fuente|no esta en el (texto )?fuente|"
                         r"sin respaldo|no presente en|invier|invert|contradic")

unidades = {u["chunk_id"]: u for u in json.loads((SAL / "fase1_unidades.json").read_text(encoding="utf-8"))}
fase1 = {c["id"]: c for c in json.loads((SAL / "fase1_candidatos.json").read_text(encoding="utf-8"))}


def grupo(cid: str) -> str:
    u = unidades[cid]
    if not u["linea_item"]:
        return "no_item"
    return "item_bloque_llega" if u["abre_lista_en_fuente_e3"] else "item_bloque_no_llega"


extra = []
indicador = []
faltantes_por_grupo = Counter()
for to in TOS:
    e1 = {r["chunk_id"]: r for r in jl(SALIDA / to / "extracciones_e1.jsonl")}
    reint = {(r["chunk_id"], r["intento"]): r for r in jl(SALIDA / to / "reintentos_e3.jsonl")}
    for v in jl(SALIDA / to / "veredictos.jsonl"):
        cid = v["chunk_id"]
        if cid not in unidades:
            continue
        g = grupo(cid)
        if v["intento"] == 0:
            ents = ((e1.get(cid) or {}).get("validacion") or {}).get("entidades") or []
        else:
            ents = ((reint.get((cid, v["intento"])) or {}).get("tool_input") or {}).get("entities") or []
        exc_ids = {e.get("local_id") for e in ents if isinstance(e, dict) and e.get("type") == "Excepcion"}
        for k, f in enumerate(v.get("faltantes") or []):
            fid = f"{cid}|{v['fase']}|{v['intento']}|{k}"
            faltantes_por_grupo[g] += 1
            nota = f.get("nota") or ""
            if RE_AGREGADO.search(norm(nota)):
                indicador.append({"id": fid, "grupo": g, "tipo": f.get("tipo"), "severidad": f.get("severidad"),
                                  "bloqueante": f.get("bloqueante"), "nota": nota,
                                  "cita": f.get("cita_textual_del_fuente")})
            if g != "no_item" and fid not in fase1:
                nombra = [x for x in exc_ids if x and re.search(rf"\b{re.escape(x)}\b", nota)]
                if nombra:
                    extra.append({"id": fid, "chunk_id": cid, "fase": v["fase"], "intento": v["intento"],
                                  "tipo": f.get("tipo"), "severidad": f.get("severidad"),
                                  "bloqueante": f.get("bloqueante"), "cita_verificada": f.get("cita_verificada"),
                                  "estructural_no_bloqueante": f.get("estructural_no_bloqueante"),
                                  "cita": f.get("cita_textual_del_fuente"), "nota": nota,
                                  "ubicacion": f.get("ubicacion"), "nombra_excepcion": nombra})

unid_por_grupo = Counter(grupo(c) for c in unidades)
ind_por_grupo = Counter(x["grupo"] for x in indicador)
ind_unid_por_grupo = Counter(g for g, _ in sorted({(x["grupo"], x["id"].split("|")[0]) for x in indicador}))
pool = sorted(x["id"] for x in indicador if x["grupo"] == "item_bloque_no_llega")
rng = random.Random(SEMILLA)
muestra = sorted(rng.sample(pool, 15))
res = {
    "candidatos_fase1": len(fase1), "candidatos_extra_nombran_excepcion": len(extra),
    "candidatos_total": len(fase1) + len(extra),
    "unidades_por_grupo": dict(unid_por_grupo),
    "faltantes_por_grupo": dict(faltantes_por_grupo),
    "indicador_faltantes_por_grupo": dict(ind_por_grupo),
    "indicador_unidades_por_grupo": dict(ind_unid_por_grupo),
    "sorteo": {"semilla": SEMILLA, "pool": len(pool), "n": 15, "ids": muestra,
               "hora": datetime.now().astimezone().isoformat(timespec="seconds")},
}
(SAL / "fase2_resumen.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
(SAL / "fase2_candidatos_extra.json").write_text(json.dumps(extra, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
(SAL / "fase2_indicador.json").write_text(json.dumps(indicador, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps(res, ensure_ascii=False, indent=1))
