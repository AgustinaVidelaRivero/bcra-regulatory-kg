"""U-E3-LISTAS, O3 (a), sin API: cifras y fichas, con la regla sellada en criterio_o3.md y la lectura sellada en
a/lectura_o3.json (las dos escritas antes de computar).

- Regla mecánica: un reclamo viejo del intento 0 persiste si el veredicto nuevo trae un candidato de la misma categoría
  (lectura) cuya cita comparte con la vieja al menos una ventana de 5 tokens normalizados (validador_r2.norm_tokens), o una
  contiene a la otra (comun_e3.normalizar_para_cita). Si no, desaparece. Nuevo: candidato P, C, B o B2 que no es la
  persistencia de ningún reclamo viejo.
- Lectura (aparte): el «mismo asunto» de la lectura sellada, sea o no candidato.
- Por unidad, por código: faltantes, bloqueantes y el camino del ratchet con este veredicto, contra el de la tanda 0.
Uso: python o3_a_cifras.py <repo> <copia> <dir_o3>
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

REPO, COPIA, O3 = (Path(x).resolve() for x in sys.argv[1:4])
sys.path.insert(0, str(COPIA / "data" / "experiment" / "reextraccion_v2" / "e3_verificador"))
sys.path.insert(0, str(COPIA / "data" / "experiment" / "pyd_r2" / "code"))
import comun_e3  # noqa: E402
import validador_r2 as V  # noqa: E402

PCB = ("P", "C", "B", "B2")
hoja = json.loads((O3 / "a" / "hoja_de_lectura.json").read_text(encoding="utf-8"))
lect = json.loads((O3 / "a" / "lectura_o3.json").read_text(encoding="utf-8"))["unidades"]
evs = {json.loads(x)["chunk_id"]: json.loads(x)["evaluacion"]
       for x in (O3 / "a" / "evaluacion_e3_o3.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()}
lista = json.loads((O3 / "lista_unidades_afectadas_tanda0.json").read_text(encoding="utf-8"))
sr = COPIA / "data" / "experiment" / "reextraccion_v2" / "corpus_tanda0" / "salida_r2b"


def jl(p: Path) -> list[dict]:
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()] if p.exists() else []


def ventanas(t: str) -> set:
    toks = V.norm_tokens(t or "")
    return {tuple(toks[i:i + 5]) for i in range(len(toks) - 4)}


def se_tocan(a: str, b: str) -> bool:
    na, nb = comun_e3.normalizar_para_cita(a or ""), comun_e3.normalizar_para_cita(b or "")
    return bool(ventanas(a) & ventanas(b)) or (bool(na) and bool(nb) and (na in nb or nb in na))


def camino(ev: dict) -> str:
    if ev["es_completo_ok"] or ev["aceptable"]:
        return "aceptada"
    return "reintento" if ev["bloqueantes_utilizables"] else "cola_veredicto_inutilizable"


reint, cola = set(), {}
for to in {u["chunk_id"].split("::")[0] for u in lista["unidades"]}:
    reint |= {r["chunk_id"] for r in jl(sr / to / "reintentos_e3.jsonl")}
    cola.update({r["chunk_id"]: r["flag"] for r in jl(sr / to / "cola_humana.jsonl")})
fichas, tot = {}, Counter()
for u in lista["unidades"]:
    cid = u["chunk_id"]
    h, L, ev = hoja[cid], lect[cid], evs[cid]
    cands = {str(n["k"]): n for n in h["faltantes_nuevos"] if n["candidato"]}
    cat = {k: L["candidatos"][k]["categoria"] for k in cands}
    assert set(cat) == set(L["candidatos"]), (cid, set(cat), set(L["candidatos"]))
    usados, viejos = set(), []
    for v in h["viejos_intento_0"]:
        match = [k for k in cands if cat[k] == v["categoria"] and se_tocan(v["cita"], cands[k]["cita"])]
        estado = "persiste" if match else "desaparece"
        usados |= set(match)
        lectura_k = L["mismo_asunto"][v["id"]]
        viejos.append({"id": v["id"], "categoria": v["categoria"], "regla": estado, "con": match,
                       "lectura": "persiste" if lectura_k is not None else "desaparece", "lectura_con": lectura_k})
        tot[f"regla_{estado}"] += 1
        tot[f"lectura_{'persiste' if lectura_k is not None else 'desaparece'}"] += 1
    nuevos = [{"k": k, "categoria": cat[k], **{x: cands[k][x] for x in ("tipo", "severidad", "bloqueante")}}
              for k in cands if cat[k] in PCB and k not in usados]
    tot["regla_nuevos"] += len(nuevos)
    t0 = "reintento" if cid in reint else ("cola_veredicto_inutilizable" if cola.get(cid) == "cola_humana_veredicto_inutilizable"
                                           else "aceptada")
    c_nuevo = camino(ev)
    tot[f"camino_{t0}->{c_nuevo}"] += 1
    fichas[cid] = {"bloque": u["bloque_que_abre_la_lista"], "viejos_intento_0": viejos, "nuevos_PCB": nuevos,
                   "faltantes_nuevos": len(ev["faltantes"]), "bloqueantes_nuevos": len(ev["faltantes_bloqueantes"]),
                   "candidatos_nuevos": {k: cat[k] for k in cands}, "no_candidatos": L["no_candidatos"],
                   "camino_tanda0_intento0": t0, "camino_con_e3_corregido": c_nuevo}
res = {"criterio": "criterio_o3.md (sha256 en criterio_o3_sello.txt); lectura: a/lectura_o3.json (sello en a/lectura_o3_sello.txt)",
       "reclamos_viejos_intento_0": sum(len(f["viejos_intento_0"]) for f in fichas.values()),
       "por_categoria_vieja": dict(Counter(v["categoria"] for f in fichas.values() for v in f["viejos_intento_0"])),
       "totales": dict(sorted(tot.items())),
       "persisten_por_la_regla": sorted(v["id"] for f in fichas.values() for v in f["viejos_intento_0"] if v["regla"] == "persiste"),
       "persisten_por_la_lectura": sorted(v["id"] for f in fichas.values() for v in f["viejos_intento_0"] if v["lectura"] == "persiste"),
       "nuevos_PCB": {cid: f["nuevos_PCB"] for cid, f in fichas.items() if f["nuevos_PCB"]},
       "faltantes_nuevos": sum(f["faltantes_nuevos"] for f in fichas.values()),
       "bloqueantes_nuevos": sum(f["bloqueantes_nuevos"] for f in fichas.values()),
       "unidades_completo_ok": sum(1 for cid in fichas if evs[cid]["es_completo_ok"]),
       "fichas": fichas}
(O3 / "a" / "cifras_a.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
md = ["# U-E3-LISTAS, O3 (a): fichas por unidad (E3 corregido, primera verificación, sin ratchet)", ""]
for cid, f in fichas.items():
    md.append(f"## {cid} — bloque {f['bloque']}; camino: tanda 0 {f['camino_tanda0_intento0']} → ahora "
              f"{f['camino_con_e3_corregido']}; faltantes {f['faltantes_nuevos']}, bloqueantes {f['bloqueantes_nuevos']}")
    for v in f["viejos_intento_0"]:
        md.append(f"- reclamo viejo {v['categoria']} `{v['id']}`: por la regla, {v['regla']}"
                  f"{' (con [' + ', '.join(v['con']) + '])' if v['con'] else ''}; leído, {v['lectura']}"
                  f"{' (con [' + v['lectura_con'] + '])' if v['lectura_con'] is not None else ''}")
    for n in f["nuevos_PCB"]:
        md.append(f"- nuevo {n['categoria']} [{n['k']}] ({n['tipo']}, {n['severidad']}, bloqueante {n['bloqueante']}): "
                  f"{lect[cid]['candidatos'][n['k']]['lectura']}")
    for k, t in f["no_candidatos"].items():
        md.append(f"- faltante nuevo [{k}], no candidato: {t}")
    md.append("")
(O3 / "a" / "fichas_a.md").write_text("\n".join(md), encoding="utf-8")
print(json.dumps({k: res[k] for k in ("reclamos_viejos_intento_0", "por_categoria_vieja", "totales", "persisten_por_la_regla",
                                      "persisten_por_la_lectura", "faltantes_nuevos", "bloqueantes_nuevos",
                                      "unidades_completo_ok")}, ensure_ascii=False, indent=1))
print(json.dumps(res["nuevos_PCB"], ensure_ascii=False))
