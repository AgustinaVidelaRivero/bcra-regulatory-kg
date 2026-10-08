"""U-E3-LISTAS, O5, sin API: cifras contra O3 con el criterio sellado (criterio_o5.md) y la lectura sellada (a/lectura_o5.json),
las dos escritas antes de computar.
  - Mismo reclamo (regla de O3): misma categoría por la lectura (si el faltante de O3 no tiene categoría, porque no era
    candidato, solo la cita) y citas que comparten una ventana de 5 tokens normalizados o una contiene a la otra.
  - (i) en ext::3.6.4.1 y ext::3.6.4.2, el B de O3 no persiste (por la regla; y aparte, por la lectura: ningún B en O5).
  - (ii) en ext::3.16.2.1, el B de O3 persiste por la regla; su severidad y si bloquea, contra O3.
  - (iii) en las otras 17, ningún bloqueante de O5 sin un bloqueante de O3 en la unidad con cita compartida.
Uso: python o5_cifras.py <copia_o5> <dir_e3_listas>"""
import json, sys
from collections import Counter
from pathlib import Path
C, E = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
sys.path.insert(0, str(C / "data/experiment/reextraccion_v2/e3_verificador")); sys.path.insert(0, str(C / "data/experiment/pyd_r2/code"))
import comun_e3  # noqa: E402
import validador_r2 as V  # noqa: E402
O3, O5 = E / "o3", E / "o5"
jl = lambda p: [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]  # noqa: E731
ev3 = {r["chunk_id"]: r["evaluacion"] for r in jl(O3 / "a/evaluacion_e3_o3.jsonl")}
ev5 = {r["chunk_id"]: r["evaluacion"] for r in jl(O5 / "a/evaluacion_e3_o5.jsonl")}
h5 = json.loads((O5 / "a/hoja_de_lectura_o5.json").read_text(encoding="utf-8"))
l5 = json.loads((O5 / "a/lectura_o5.json").read_text(encoding="utf-8"))["unidades"]
f3 = json.loads((O3 / "a/cifras_a.json").read_text(encoding="utf-8"))["fichas"]
lista = json.loads((O5 / "lista_unidades_afectadas_tanda0.json").read_text(encoding="utf-8"))
chunks = {c["id"]: c for c in comun_e3.cargar_chunks(("ext", "docvig"), e0_dir=C / "data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b")}


def ventanas(t):
    k = V.norm_tokens(t or ""); return {tuple(k[i:i + 5]) for i in range(len(k) - 4)}


def se_tocan(a, b):
    na, nb = comun_e3.normalizar_para_cita(a or ""), comun_e3.normalizar_para_cita(b or "")
    return bool(ventanas(a) & ventanas(b)) or (bool(na) and bool(nb) and (na in nb or nb in na))


def camino(ev):
    if ev["es_completo_ok"] or ev["aceptable"]:
        return "aceptada"
    return "reintento" if ev["bloqueantes_utilizables"] else "cola_veredicto_inutilizable"


RESIDUO, CONTROL = ("ext::3.6.4.1", "ext::3.6.4.2"), "ext::3.16.2.1"
fichas, tot = {}, Counter()
for u in lista["unidades"]:
    cid = u["chunk_id"]
    o3 = h5[cid]["o3"]; o5 = h5[cid]["o5"]; L = l5[cid]
    cat5 = {str(f["k"]): L["faltantes"][str(f["k"])]["categoria"] for f in o5}
    viejos = []
    usados = set()
    for f in o3:
        c3 = f["categoria_lectura_o3"]
        m = [str(g["k"]) for g in o5 if (c3 is None or cat5[str(g["k"])] == c3) and se_tocan(f["cita"], g["cita"])]
        usados |= set(m)
        viejos.append({"k": f["k"], "categoria_o3": c3, "bloqueante_o3": f["bloqueante"], "severidad_o3": f["severidad"],
                       "regla": "persiste" if m else "desaparece", "con": m,
                       "lectura": "persiste" if L["mismo_asunto_o3"][str(f["k"])] is not None else "desaparece",
                       "lectura_con": L["mismo_asunto_o3"][str(f["k"])]})
    nuevos = [{"k": g["k"], "categoria": cat5[str(g["k"])], "fundado": L["faltantes"][str(g["k"])]["fundado"],
               "severidad": g["severidad"], "bloqueante": g["bloqueante"]} for g in o5 if str(g["k"]) not in usados]
    # (iii): bloqueantes de O5 sin bloqueante de O3 con cita compartida
    b3 = [f for f in o3 if f["bloqueante"]]
    nb = [{"k": g["k"], "categoria": cat5[str(g["k"])], "sube_de_no_bloqueante": any(se_tocan(f["cita"], g["cita"]) for f in o3 if not f["bloqueante"])}
          for g in o5 if g["bloqueante"] and not any(se_tocan(f["cita"], g["cita"]) for f in b3)]
    fichas[cid] = {"o3": {"faltantes": len(o3), "bloqueantes": sum(1 for f in o3 if f["bloqueante"]), "camino": f3[cid]["camino_con_e3_corregido"]},
                   "o5": {"faltantes": len(o5), "bloqueantes": sum(1 for g in o5 if g["bloqueante"]), "camino": camino(ev5[cid]),
                          "completo_ok": ev5[cid]["es_completo_ok"]},
                   "viejos_o3": viejos, "nuevos_o5": nuevos, "bloqueantes_nuevos_iii": nb}
    for v in viejos:
        tot[f"o3_regla_{v['regla']}"] += 1; tot[f"o3_lectura_{v['lectura']}"] += 1
    tot["o5_nuevos_regla"] += len(nuevos)
    tot[f"camino_{fichas[cid]['o3']['camino']}->{fichas[cid]['o5']['camino']}"] += 1
res = {"criterio": "criterio_o5.md (sello en criterio_o5_sello.txt); lectura: a/lectura_o5.json (sello en a/lectura_o5_sello.txt)"}
# (i)
i_det = {}
for cid in RESIDUO:
    ch = chunks[cid]
    bloque = "\n".join(ch["herencia"][i]["texto"] for i in comun_e3.indices_bloque_lista(ch))
    bs = [v for v in fichas[cid]["viejos_o3"] if v["categoria_o3"] == "B"]
    i_det[cid] = {"B_de_O3": [{k: v[k] for k in ("k", "regla", "con", "lectura", "lectura_con", "severidad_o3", "bloqueante_o3")} for v in bs],
                  "B_en_O5_por_la_lectura": [g for g in fichas[cid]["nuevos_o5"] if g["categoria"] == "B"]
                  + [{"k": int(k), "categoria": "B", "via": "persistencia"} for v in bs for k in v["con"]],
                  "faltantes_o5_que_citan_el_bloque": [g["k"] for g in h5[cid]["o5"] if se_tocan(bloque, g["cita"])]}
res["i"] = {"regla_se_cumple": all(v["regla"] == "desaparece" for c in RESIDUO for v in i_det[c]["B_de_O3"]),
            "lectura_se_cumple": not any(i_det[c]["B_en_O5_por_la_lectura"] for c in RESIDUO), "detalle": i_det}
# (ii)
bc = [v for v in fichas[CONTROL]["viejos_o3"] if v["categoria_o3"] == "B"]
ks = [k for v in bc for k in v["con"]]
g5 = [g for g in h5[CONTROL]["o5"] if str(g["k"]) in ks]
res["ii"] = {"se_cumple": bool(ks), "B_de_O3": [{k: v[k] for k in ("k", "severidad_o3", "bloqueante_o3", "regla", "con", "lectura")} for v in bc],
             "en_O5": [{x: g[x] for x in ("k", "tipo", "severidad", "bloqueante", "cita_verificada")} for g in g5],
             "misma_severidad_y_bloquea": all(g["severidad"] == "alta" and g["bloqueante"] for g in g5) and bool(g5)}
# (iii)
otras = [u["chunk_id"] for u in lista["unidades"] if u["chunk_id"] not in RESIDUO + (CONTROL,)]
res["iii"] = {"unidades": len(otras), "bloqueantes_nuevos": {c: fichas[c]["bloqueantes_nuevos_iii"] for c in otras if fichas[c]["bloqueantes_nuevos_iii"]}}
res["iii"]["se_cumple"] = not res["iii"]["bloqueantes_nuevos"]
res["iii_tambien_en_las_3"] = {c: fichas[c]["bloqueantes_nuevos_iii"] for c in RESIDUO + (CONTROL,) if fichas[c]["bloqueantes_nuevos_iii"]}
res["totales"] = dict(sorted(tot.items()))
res["o5"] = {"faltantes": sum(f["o5"]["faltantes"] for f in fichas.values()), "bloqueantes": sum(f["o5"]["bloqueantes"] for f in fichas.values()),
             "completas": sum(1 for f in fichas.values() if f["o5"]["completo_ok"]),
             "aceptadas": sum(1 for f in fichas.values() if f["o5"]["camino"] == "aceptada"),
             "por_categoria": dict(Counter(g["categoria"] for c in fichas for g in [{"categoria": l5[c]["faltantes"][str(x["k"])]["categoria"]} for x in h5[c]["o5"]])),
             "bloqueantes_por_lectura": {"fundados": sum(1 for c in fichas for x in h5[c]["o5"] if x["bloqueante"] and l5[c]["faltantes"][str(x["k"])]["fundado"]),
                                         "falsas_alarmas": sum(1 for c in fichas for x in h5[c]["o5"] if x["bloqueante"] and not l5[c]["faltantes"][str(x["k"])]["fundado"])}}
res["o3"] = {"faltantes": sum(f["o3"]["faltantes"] for f in fichas.values()), "bloqueantes": sum(f["o3"]["bloqueantes"] for f in fichas.values()),
             "aceptadas": sum(1 for f in fichas.values() if f["o3"]["camino"] == "aceptada")}
res["fichas"] = fichas
(O5 / "a/cifras_o5.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
md = ["# U-E3-LISTAS, O5: fichas por unidad contra O3 (casos resueltos en la NOTA del ítem, primera verificación, sin ratchet)", ""]
for cid, f in fichas.items():
    md.append(f"## {cid} — O3: {f['o3']['faltantes']} faltantes, {f['o3']['bloqueantes']} bloq, {f['o3']['camino']} | O5: "
              f"{f['o5']['faltantes']} faltantes, {f['o5']['bloqueantes']} bloq, {f['o5']['camino']}")
    for v in f["viejos_o3"]:
        md.append(f"- O3 [{v['k']}] {v['categoria_o3'] or '-'} ({v['severidad_o3']}, bloq {v['bloqueante_o3']}): por la regla {v['regla']}"
                  f"{' con [' + ', '.join(v['con']) + ']' if v['con'] else ''}; leído, {v['lectura']}"
                  f"{' con [' + v['lectura_con'] + ']' if v['lectura_con'] is not None else ''}")
    for g in f["nuevos_o5"]:
        md.append(f"- O5 nuevo [{g['k']}] {g['categoria']} ({g['severidad']}, bloq {g['bloqueante']}, {'fundado' if g['fundado'] else 'falsa alarma'}): "
                  f"{l5[cid]['faltantes'][str(g['k'])]['lectura']}")
    md.append("")
(O5 / "a/fichas_o5.md").write_text("\n".join(md), encoding="utf-8")
print(json.dumps({k: res[k] for k in ("i", "ii", "iii", "iii_tambien_en_las_3", "totales", "o5", "o3")}, ensure_ascii=False, indent=1))
