#!/usr/bin/env python3
"""PASO 3 — chequeo anti-fuga sobre las 216 respuestas (protocolo §3).

Busca en lo que el juez ve de cada respuesta (respuesta final + citas) los
identificadores de esquema: prefijo `Sujeto_` (subsume los 70 ids del catálogo,
que igual se listan por id), "esqueleto", vocabulario estructural
(subclase_de / miembro_de / instancia_de) y "nivel" con valores rol/clase/
instancia. NO edita ninguna respuesta: lista los casos (id, grafo, réplica,
término) — protocolo: se registra el riesgo y se reporta junto al resultado.

El chequeo corre simétrico sobre AMBOS brazos.
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
TRACES = HERE.parent / "evaluacion" / "posthoc_run" / "traces"
CATALOGO = HERE.parent / "grafo_v2" / "esquema_v2_clases.json"
OUT = HERE / "corridas" / "antifuga_2026-07-26.json"

cat = json.load(open(CATALOGO, encoding="utf-8"))
ids_catalogo = [e["id"] for e in cat.get("clases", []) + cat.get("roles", [])]

PATTERNS = [("prefijo Sujeto_", re.compile(r"Sujeto_\w+"))] + [
    (f"id catálogo {i}", re.compile(re.escape(i))) for i in ids_catalogo
] + [
    ("esqueleto", re.compile(r"esqueleto", re.I)),
    ("subclase_de", re.compile(r"subclase_de")),
    ("miembro_de", re.compile(r"miembro_de")),
    ("instancia_de", re.compile(r"instancia_de")),
    ("nivel rol/clase/instancia",
     re.compile(r"nivel[\"']?\s*[:=]\s*[\"']?(rol|clase|instancia)", re.I)),
]

casos, n_scan = [], 0
for g in ("run_3", "grafo_v2"):
    for rep in (1, 2, 3):
        for f in sorted((TRACES / f"escalon1_r{rep}" / g).glob("EV1-*.json")):
            r = json.load(open(f, encoding="utf-8"))[0]
            fj = r["trace"].get("final_json") or {}
            texto = json.dumps({"respuesta": fj.get("respuesta"),
                                "citas": fj.get("citas")}, ensure_ascii=False)
            n_scan += 1
            hits = []
            for nombre, pat in PATTERNS:
                m = pat.search(texto)
                if m:
                    hits.append({"termino": nombre, "match": m.group(0)[:80]})
            if hits:
                # dedup: si ya matcheó el prefijo, los ids individuales son eco
                vistos, uniq = set(), []
                for h in hits:
                    key = h["match"]
                    if key not in vistos:
                        vistos.add(key)
                        uniq.append(h)
                casos.append({"id": r["qid"], "grafo": g, "replica": rep,
                              "terminos": uniq})

res = {"fecha": "2026-07-26", "n_respuestas_escaneadas": n_scan,
       "n_casos_con_hits": len(casos), "casos": casos,
       "nota": "Ninguna respuesta fue editada (protocolo §3): se registra el "
               "riesgo de fuga y se reporta junto al resultado."}
OUT.parent.mkdir(parents=True, exist_ok=True)
json.dump(res, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"escaneadas: {n_scan} | casos con identificadores: {len(casos)}")
for c in casos:
    print(f"  {c['id']} {c['grafo']} r{c['replica']}: "
          + "; ".join(h["termino"] + "→" + h["match"] for h in c["terminos"]))
print(f"registro en {OUT}")
