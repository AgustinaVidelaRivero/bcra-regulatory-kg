"""U-E3-LISTAS, O3 (a), sin API: la hoja de lectura de los veredictos nuevos, antes de clasificar (criterio_o3.md).
Por unidad: los reclamos P, C, B y B2 del intento 0 de la tanda 0 (con su categoría del diagnóstico) y todos los faltantes
del veredicto nuevo, con el filtro de candidatos del diagnóstico, su tipo, severidad, si bloquea y si su cita verifica.
Uso: python o3_a_hoja_de_lectura.py <repo> <dir_o3>
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path

REPO, O3 = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
AN = REPO / "reports" / "u_diag_e3_listas" / "anexo"
RE_EXC = re.compile(r"excep|exceptu|salvo|excepto")


def norm(t: str) -> str:
    t = unicodedata.normalize("NFKD", t or "")
    return " ".join("".join(ch for ch in t if not unicodedata.combining(ch)).lower().split())


def candidato(f: dict) -> bool:
    texto = " ".join(str(f.get(x) or "") for x in ("nota", "cita_textual_del_fuente"))
    return f.get("tipo") == "excepcion_ausente" or bool(RE_EXC.search(norm(texto)))


lista = json.loads((O3 / "lista_unidades_afectadas_tanda0.json").read_text(encoding="utf-8"))
cand = {c["id"]: c for c in json.loads((AN / "UDIAG_E3_LISTAS_fase1_candidatos.json").read_text(encoding="utf-8"))
        + json.loads((AN / "UDIAG_E3_LISTAS_fase2_candidatos_extra.json").read_text(encoding="utf-8"))}
ev = {json.loads(x)["chunk_id"]: json.loads(x)["evaluacion"]
      for x in (O3 / "a" / "evaluacion_e3_o3.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()}
hoja, md = {}, ["# U-E3-LISTAS, O3 (a): hoja de lectura (veredictos nuevos contra los reclamos viejos del intento 0)", ""]
for u in lista["unidades"]:
    cid = u["chunk_id"]
    viejos = [dict(id=r["id"], categoria=r["categoria"], **{k: cand[r["id"]].get(k) for k in
                                                              ("tipo", "severidad", "bloqueante", "cita", "nota")})
              for r in u["reclamos_PCB"] if r["id"].split("|")[1] == "verificacion"]
    e = ev[cid]
    nuevos = [{"k": k, "tipo": f.get("tipo"), "severidad": f.get("severidad"), "bloqueante": f.get("bloqueante"),
               "cita_verificada": f.get("cita_verificada"), "candidato": candidato(f),
               "cita": f.get("cita_textual_del_fuente"), "nota": f.get("nota")} for k, f in enumerate(e["faltantes"])]
    hoja[cid] = {"viejos_intento_0": viejos, "veredicto_nuevo": {"es_completo_ok": e["es_completo_ok"],
                                                                 "aceptable": e["aceptable"],
                                                                 "incoherencias": e["incoherencias"]},
                 "faltantes_nuevos": nuevos}
    md.append(f"## {cid} — bloque {u['bloque_que_abre_la_lista']}; tanda 0: reintento={u['reintento_por_reclamo_PCB']}, "
              f"cola={u['cola']}")
    for v in viejos:
        md.append(f"- VIEJO {v['categoria']} ({v['tipo']}, {v['severidad']}, bloq {v['bloqueante']}): «{(v['cita'] or '')[:160]}» — "
                  f"{(v['nota'] or '')[:400]}")
    md.append(f"- NUEVO: completo_ok={e['es_completo_ok']} aceptable={e['aceptable']} faltantes={len(nuevos)}")
    for n in nuevos:
        md.append(f"  - [{n['k']}] {'CANDIDATO ' if n['candidato'] else ''}{n['tipo']}, {n['severidad']}, bloq "
                  f"{n['bloqueante']}, cita verificada {n['cita_verificada']}: «{(n['cita'] or '')[:200]}» — {(n['nota'] or '')[:600]}")
    md.append("")
(O3 / "a" / "hoja_de_lectura.json").write_text(json.dumps(hoja, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
(O3 / "a" / "hoja_de_lectura.md").write_text("\n".join(md), encoding="utf-8")
print(sum(len(h["viejos_intento_0"]) for h in hoja.values()), "reclamos viejos del intento 0;",
      sum(len(h["faltantes_nuevos"]) for h in hoja.values()), "faltantes nuevos;",
      sum(1 for h in hoja.values() for n in h["faltantes_nuevos"] if n["candidato"]), "candidatos")
