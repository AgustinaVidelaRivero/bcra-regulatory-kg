"""U-E3-LISTAS, O3 (b), sin API: en las 17 unidades con reintento por los reclamos P, C, B y B2, la extracción del intento 0
contra la extracción final de la tanda 0 (criterio en criterio_o3.md, escrito antes de correr).

- Intento 0: la validación de `extracciones_e1.jsonl` (validador_e1). Final: la validación de
  `extracciones_finales_r2_<to>.jsonl` (validador_r2), con su `origen_crudo` (`e1` = el intento 0; `reintento_1:companero`
  = el reintento).
- Entidades por (tipo, etiqueta normalizada), con su descripción; relaciones por (predicado, etiqueta del origen, etiqueta del
  destino o el sujeto: `sujeto_id`, y si falta `sujeto_id_modelo`, `sujeto_propuesto` o `sujeto_mencion`). Sin el
  TextoOrdenado ni las `establecida_en`. Entra, sale o cambia (misma clave, otra descripción).
- Las unidades cuya final es el intento 0 sirven de control: un cambio ahí sería un artefacto de los dos esquemas.

Uso: python o3_b_intento0_vs_final.py <copia> <lista_sellada.json> <salida_dir>
"""
from __future__ import annotations

import json
import sys
import unicodedata
from pathlib import Path


def norm(t) -> str:
    t = unicodedata.normalize("NFKD", str(t or ""))
    return " ".join("".join(ch for ch in t if not unicodedata.combining(ch)).lower().split())


def jl(p: Path) -> list[dict]:
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()] if p.exists() else []


def claves(val: dict) -> tuple[dict, dict]:
    ents = [e for e in (val or {}).get("entidades") or [] if e.get("type") != "TextoOrdenado"]
    lab = {e.get("local_id"): norm(e.get("label")) for e in (val or {}).get("entidades") or []}
    E = {}
    for e in ents:
        E.setdefault((e.get("type"), norm(e.get("label"))), []).append(norm((e.get("properties") or {}).get("descripcion")))
    R = {}
    for r in (val or {}).get("relaciones") or []:
        if r.get("predicate") == "establecida_en":
            continue
        suj = r.get("sujeto_id") or r.get("sujeto_id_modelo") or r.get("sujeto_propuesto") or r.get("sujeto_mencion")
        destino = lab.get(r.get("target")) if r.get("target") else None
        R.setdefault((r.get("predicate"), lab.get(r.get("source")), destino or norm(suj)), 0)
        R[(r.get("predicate"), lab.get(r.get("source")), destino or norm(suj))] += 1
    return E, R


def main() -> int:
    copia, lista, sal = (Path(x).resolve() for x in sys.argv[1:4])
    sr = copia / "data" / "experiment" / "reextraccion_v2" / "corpus_tanda0" / "salida_r2b"
    doc = json.loads(lista.read_text(encoding="utf-8"))
    unidades = doc["con_reintento_por_reclamo"]
    assert len(unidades) == 17
    res = {"criterio": "criterio_o3.md, (b)", "unidades": {}}
    for cid in unidades:
        to = cid.split("::")[0]
        v0 = {r["chunk_id"]: r for r in jl(sr / to / "extracciones_e1.jsonl")}[cid]["validacion"]
        fin = {r["chunk_id"]: r for r in jl(sr / to / f"extracciones_finales_r2_{to}.jsonl")}[cid]
        E0, R0 = claves(v0)
        E1, R1 = claves(fin["validacion"])
        entran = sorted(f"{t} «{l}»" for t, l in set(E1) - set(E0))
        salen = sorted(f"{t} «{l}»" for t, l in set(E0) - set(E1))
        cambian = sorted(f"{t} «{l}»" for t, l in set(E0) & set(E1) if sorted(E0[(t, l)]) != sorted(E1[(t, l)]))
        r_entran = sorted(" ".join(str(x) for x in k) for k in set(R1) - set(R0))
        r_salen = sorted(" ".join(str(x) for x in k) for k in set(R0) - set(R1))
        res["unidades"][cid] = {
            "origen_de_la_final": fin.get("origen_crudo"), "estado_e3": fin.get("estado_e3"),
            "entidades": {"intento_0": sum(len(v) for v in E0.values()), "final": sum(len(v) for v in E1.values())},
            "relaciones": {"intento_0": sum(R0.values()), "final": sum(R1.values())},
            "entidades_que_entran": entran, "entidades_que_salen": salen, "entidades_que_cambian": cambian,
            "relaciones_que_entran": r_entran, "relaciones_que_salen": r_salen,
            "cambio": bool(entran or salen or cambian or r_entran or r_salen)}
    u = res["unidades"]
    res["resumen"] = {
        "unidades": len(u), "final_es_el_reintento": sum(1 for x in u.values() if x["origen_de_la_final"] != "e1"),
        "final_es_el_intento_0": sum(1 for x in u.values() if x["origen_de_la_final"] == "e1"),
        "cambiaron": sum(1 for x in u.values() if x["cambio"]),
        "cambiaron_entre_las_del_reintento": sum(1 for x in u.values() if x["cambio"] and x["origen_de_la_final"] != "e1"),
        "control_cambios_en_las_del_intento_0": sum(1 for x in u.values() if x["cambio"] and x["origen_de_la_final"] == "e1"),
        "entidades_que_entran": sum(len(x["entidades_que_entran"]) for x in u.values()),
        "entidades_que_salen": sum(len(x["entidades_que_salen"]) for x in u.values()),
        "entidades_que_cambian": sum(len(x["entidades_que_cambian"]) for x in u.values()),
        "relaciones_que_entran": sum(len(x["relaciones_que_entran"]) for x in u.values()),
        "relaciones_que_salen": sum(len(x["relaciones_que_salen"]) for x in u.values())}
    sal.mkdir(parents=True, exist_ok=True)
    (sal / "b_intento0_vs_final.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    md = ["# U-E3-LISTAS, O3 (b): intento 0 contra final, por unidad (sin API)", ""]
    for cid, x in u.items():
        md.append(f"## {cid} — final: {x['origen_de_la_final']} ({x['estado_e3']}); {'cambió' if x['cambio'] else 'no cambió'}")
        md.append(f"Entidades {x['entidades']['intento_0']} → {x['entidades']['final']}; relaciones "
                  f"{x['relaciones']['intento_0']} → {x['relaciones']['final']}.")
        for k, rot in (("entidades_que_entran", "Entran"), ("entidades_que_salen", "Salen"),
                       ("entidades_que_cambian", "Cambian de descripción"), ("relaciones_que_entran", "Relaciones que entran"),
                       ("relaciones_que_salen", "Relaciones que salen")):
            if x[k]:
                md.append(f"- {rot}: " + "; ".join(x[k]))
        md.append("")
    (sal / "b_fichas.md").write_text("\n".join(md), encoding="utf-8")
    print(json.dumps(res["resumen"], ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
