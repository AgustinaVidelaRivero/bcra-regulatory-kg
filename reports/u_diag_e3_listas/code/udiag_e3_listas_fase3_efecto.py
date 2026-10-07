"""U-DIAG-E3-LISTAS, fase 3 (solo lectura, USD 0): cifras de los puntos 2 y 3 desde la adjudicación volcada antes.

Punto 2: reclamos por categoría (P, C, B, B2...) en ítems de lista, con severidad, bloqueante, intento y si el
bloque que abre la lista llega a E3; juicio del censo de P y C; muestra de generalidad (15) con Wilson al 95 %.
Punto 3, por conjunto de unidades (las de P, y las de P, C, B o B2):
  - reintento por ese reclamo: un reclamo de la categoría en el intento 0, bloqueante y con cita verificada
    (entra al feedback, ratchet_e3.py:563-564), y la unidad en reintentos_e3.jsonl;
  - cola humana: la unidad en cola_humana.jsonl, por flag; de las de flag «cola_humana» (tope agotado), si el
    reclamo de la categoría está entre los bloqueantes de la re-verificación (el que persistió);
  - copia real de la nota: la unidad con al menos un caso «copia real» en
    reext_t0/t4/salida/clasificacion_copia_nota_t4.json (T4, punto 3).
También: las 74 de la cola y las 29 de flag «cola_humana», por grupo (ítem con o sin el bloque, no ítem).

Uso: python fase3_efecto.py <copia> <salida_dir>
"""
from __future__ import annotations

import json
import math
import sys
from collections import Counter
from pathlib import Path

COPIA = Path(sys.argv[1]).resolve()
SAL = Path(sys.argv[2]).resolve()
EXP = COPIA / "data" / "experiment"
SALIDA = EXP / "reextraccion_v2" / "corpus_tanda0" / "salida_r2b"
TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")


def jl(p: Path) -> list[dict]:
    if not p.exists():
        return []
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]


def wilson(k: int, n: int, z: float = 1.959964) -> list[float]:
    if n == 0:
        return [0.0, 0.0]
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    m = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return [round(c - m, 3), round(c + m, 3)]


unidades = {u["chunk_id"]: u for u in json.loads((SAL / "fase1_unidades.json").read_text(encoding="utf-8"))}
adj = json.loads((SAL / "adjudicacion_candidatos.json").read_text(encoding="utf-8"))
muestra = json.loads((SAL / "adjudicacion_muestra.json").read_text(encoding="utf-8"))
cand = {c["id"]: c for c in json.loads((SAL / "fase1_candidatos.json").read_text(encoding="utf-8"))
        + json.loads((SAL / "fase2_candidatos_extra.json").read_text(encoding="utf-8"))}

reint, cola = set(), {}
for to in TOS:
    reint |= {r["chunk_id"] for r in jl(SALIDA / to / "reintentos_e3.jsonl")}
    for r in jl(SALIDA / to / "cola_humana.jsonl"):
        cola[r["chunk_id"]] = r["flag"]
copia = json.loads((EXP / "reext_t0" / "t4" / "salida" / "clasificacion_copia_nota_t4.json").read_text(encoding="utf-8"))
copia_real = {c["chunk_id"] for c in copia["casos"] if c["clase"] == "copia real"}


def grupo(cid: str) -> str:
    u = unidades[cid]
    if not u["linea_item"]:
        return "no_item"
    return "item_bloque_llega" if u["abre_lista_en_fuente_e3"] else "item_bloque_no_llega"


def reclamos(cats: set[str]) -> list[dict]:
    out = []
    for fid, a in adj.items():
        if a["categoria"] in cats:
            x = dict(cand[fid])
            x.update(a)
            x["grupo"] = grupo(x["chunk_id"])
            out.append(x)
    return sorted(out, key=lambda r: r["id"])


def efecto(rs: list[dict]) -> dict:
    us = sorted({r["chunk_id"] for r in rs})
    por_reclamo = sorted({r["chunk_id"] for r in rs if r["intento"] == 0 and r["bloqueante"] and r["cita_verificada"]
                          and r["chunk_id"] in reint})
    en_cola = {u: cola[u] for u in us if u in cola}
    persistio = sorted({r["chunk_id"] for r in rs if r["intento"] == 1 and r["bloqueante"]
                        and cola.get(r["chunk_id"]) == "cola_humana"})
    return {
        "unidades": len(us), "lista_unidades": us,
        "con_reintento_cualquiera": sorted(u for u in us if u in reint),
        "reintento_por_ese_reclamo": por_reclamo,
        "en_cola": en_cola, "en_cola_por_flag": dict(Counter(en_cola.values())),
        "cola_humana_con_ese_reclamo_persistente": persistio,
        "con_copia_real_t4": sorted(u for u in us if u in copia_real),
    }


def resumen_reclamos(rs: list[dict]) -> dict:
    return {
        "reclamos": len(rs), "unidades": len({r["chunk_id"] for r in rs}),
        "por_severidad": dict(Counter(r["severidad"] for r in rs)),
        "bloqueantes": sum(1 for r in rs if r["bloqueante"]),
        "residuales": sum(1 for r in rs if not r["bloqueante"]),
        "por_intento": dict(Counter(str(r["intento"]) for r in rs)),
        "por_grupo": dict(Counter(r["grupo"] for r in rs)),
        "por_juicio": dict(Counter(r.get("juicio", "sin_juicio") for r in rs)),
    }


P = reclamos({"P"})
PCB = reclamos({"P", "C", "B", "B2"})
todos = reclamos({"P", "C", "B", "B2", "M", "E", "O"})
fa = sum(1 for v in muestra.values() if v["juicio"] == "falsa_alarma_lista")
items_cola = Counter(grupo(u) for u in cola)
items_29 = Counter(grupo(u) for u, f in cola.items() if f == "cola_humana")
res = {
    "candidatos_por_categoria": dict(Counter(a["categoria"] for a in adj.values())),
    "punto2_P": resumen_reclamos(P),
    "punto2_P_detalle": [{k: r.get(k) for k in ("id", "severidad", "bloqueante", "cita_verificada", "grupo", "juicio")}
                         for r in P],
    "punto2_C": resumen_reclamos(reclamos({"C"})),
    "punto2_B": resumen_reclamos(reclamos({"B"})),
    "punto2_B2": resumen_reclamos(reclamos({"B2"})),
    "punto2_PCB": resumen_reclamos(PCB),
    "punto2_muestra_generalidad": {"n": len(muestra), "por_juicio": dict(Counter(v["juicio"] for v in muestra.values())),
                                   "falsa_alarma_lista": fa, "wilson95": wilson(fa, len(muestra))},
    "punto3_P": efecto(P),
    "punto3_PCB": efecto(PCB),
    "cola_total": len(cola), "cola_por_flag": dict(Counter(cola.values())),
    "cola_por_grupo": dict(items_cola), "cola_humana_29_por_grupo": dict(items_29),
    "copia_real_unidades_t4": len(copia_real),
    "copia_real_por_grupo": dict(Counter(grupo(u) for u in sorted(copia_real))),
    "reintentos_unidades": len(reint),
    "reintentos_por_grupo": dict(Counter(grupo(u) for u in sorted(reint))),
}
(SAL / "fase3_efecto.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps(res, ensure_ascii=False, indent=1))
