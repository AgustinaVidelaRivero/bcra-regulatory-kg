"""U-E3-LISTAS, O5, sin API: la hoja de lectura de los veredictos con los casos resueltos, antes de clasificar (criterio_o5.md).
Por unidad: los faltantes de O3 (o3/a/hoja_de_lectura.json, con la categoría de la lectura sellada de O3 para sus
candidatos) y todos los faltantes de O5, con el filtro de candidatos del diagnóstico, su tipo, severidad, si bloquea y si su
cita verifica. Uso: python o5_hoja_de_lectura.py <dir_e3_listas>"""
import json, re, sys, unicodedata
from pathlib import Path
E = Path(sys.argv[1]).resolve()
O3, O5 = E / "o3", E / "o5"
RE_EXC = re.compile(r"excep|exceptu|salvo|excepto")


def norm(t):
    t = unicodedata.normalize("NFKD", t or "")
    return " ".join("".join(ch for ch in t if not unicodedata.combining(ch)).lower().split())


def candidato(f):
    texto = " ".join(str(f.get(x) or "") for x in ("nota", "cita_textual_del_fuente"))
    return f.get("tipo") == "excepcion_ausente" or bool(RE_EXC.search(norm(texto)))


lista = json.loads((O5 / "lista_unidades_afectadas_tanda0.json").read_text(encoding="utf-8"))
h3 = json.loads((O3 / "a" / "hoja_de_lectura.json").read_text(encoding="utf-8"))
l3 = json.loads((O3 / "a" / "lectura_o3.json").read_text(encoding="utf-8"))["unidades"]
ev5 = {json.loads(x)["chunk_id"]: json.loads(x)["evaluacion"]
       for x in (O5 / "a" / "evaluacion_e3_o5.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()}
hoja, md = {}, ["# U-E3-LISTAS, O5: hoja de lectura (veredictos con los casos resueltos contra los de O3)", ""]
for u in lista["unidades"]:
    cid = u["chunk_id"]
    o3 = []
    for n in h3[cid]["faltantes_nuevos"]:
        k = str(n["k"])
        cat = (l3[cid]["candidatos"].get(k) or {}).get("categoria") if n["candidato"] else None
        o3.append({**{x: n[x] for x in ("k", "tipo", "severidad", "bloqueante", "cita_verificada", "candidato", "cita", "nota")},
                   "categoria_lectura_o3": cat, "lectura_o3": (l3[cid]["candidatos"].get(k) or {}).get("lectura")
                   if n["candidato"] else l3[cid]["no_candidatos"].get(k)})
    e = ev5[cid]
    o5 = [{"k": k, "tipo": f.get("tipo"), "severidad": f.get("severidad"), "bloqueante": f.get("bloqueante"),
           "cita_verificada": f.get("cita_verificada"), "candidato": candidato(f), "cita": f.get("cita_textual_del_fuente"),
           "nota": f.get("nota")} for k, f in enumerate(e["faltantes"])]
    hoja[cid] = {"o3": o3, "o5": o5, "o5_veredicto": {"es_completo_ok": e["es_completo_ok"], "aceptable": e["aceptable"]}}
    md.append(f"## {cid} — O3: {len(o3)} faltantes ({sum(1 for x in o3 if x['bloqueante'])} bloq) | O5: {len(o5)} "
              f"({sum(1 for x in o5 if x['bloqueante'])} bloq), completo_ok={e['es_completo_ok']}")
    for x in o3:
        md.append(f"- O3 [{x['k']}] {x['categoria_lectura_o3'] or '-'} {x['tipo']}, {x['severidad']}, bloq {x['bloqueante']}: "
                  f"«{(x['cita'] or '')[:160]}» — {(x['nota'] or '')[:300]}")
    for x in o5:
        md.append(f"- O5 [{x['k']}] {'CANDIDATO ' if x['candidato'] else ''}{x['tipo']}, {x['severidad']}, bloq {x['bloqueante']}, "
                  f"cita verificada {x['cita_verificada']}: «{(x['cita'] or '')[:220]}» — {(x['nota'] or '')[:700]}")
    md.append("")
(O5 / "a" / "hoja_de_lectura_o5.json").write_text(json.dumps(hoja, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
(O5 / "a" / "hoja_de_lectura_o5.md").write_text("\n".join(md), encoding="utf-8")
print(sum(len(h["o5"]) for h in hoja.values()), "faltantes en O5;", sum(len(h["o3"]) for h in hoja.values()), "en O3")
