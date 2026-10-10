"""Mesa, 10/10/2026: arma la lista de C4 de C2-bis para la autora, desde la salida de C3 (c3_C2bis.json), las fichas de C1 (con el par,
que la autora puede ver), la planilla nueva sellada y la primera (solo para las discrepancias).
Uso: python3 -B lista_C4_C2bis_mesa.py <repo> <c3_C2bis.json> <planilla_nueva> <salida.md>"""
import json, sys
repo, c3p, pn, out = sys.argv[1:5]
c3 = json.load(open(c3p))
F = {json.loads(x)["ficha"]: json.loads(x) for x in open(f"{repo}/data/experiment/conf_matriz/c1/fichas_c1.jsonl", encoding="utf-8") if x.strip()}
acta = {f["ficha"]: f for f in json.load(open(f"{repo}/data/experiment/conf_matriz/c1/acta_c1.json"))["orden_de_lectura"]["fichas"]}
nueva = {json.loads(x)["ficha"]: json.loads(x) for x in open(pn, encoding="utf-8") if x.strip()}
primera = {json.loads(x)["ficha"]: json.loads(x) for x in open(f"{repo}/data/experiment/conf_matriz/c2/planilla_c2.jsonl", encoding="utf-8") if x.strip()}
def ficha(fid, con_primera=False):
    f, n = F[fid], nueva[fid]
    u = f["unidad"]
    L = [f"#### {fid} — → {acta[fid]['par']}", f"- **Origen:** {f['origen']['tipo']} «{f['origen']['etiqueta']}» — {f['origen']['descripcion_extractor']}",
         f"- **Destino:** {f['destino']['tipo']} «{f['destino']['etiqueta']}» — {f['destino']['descripcion_extractor']}",
         f"- **Tramos de E1:** origen {f['origen']['tramo_e1']!r}; destino {f['destino']['tramo_e1']!r}",
         f"- **Unidad:** `{u['chunk_id']}`, páginas {u['paginas_unidad']}; render en la carpeta del lector: {', '.join(f['paginas_render'])}",
         f"- **Lectura nueva:** `{n['marca']}` — {n.get('nota') or '(sin nota)'}" + (f" · anotaciones: {n['anotaciones']}" if n.get('anotaciones') else "")]
    if con_primera:
        p = primera[fid]
        L.append(f"- **Primera lectura (contaminada, no decide):** `{p['marca']}` — {p.get('nota') or '(sin nota)'}")
    L.append("- **Adjudicación de la autora:** ")
    return "\n".join(L) + "\n"
md = ["# U-CONF-MATRIZ, C2-bis: lista para la revisión de la autora (C4)\n",
      f"Planilla nueva sellada (`{c3['planilla_nueva_sha256']}`). Entran: las incorrectas y las no decidibles de la lectura nueva, 5 correctas por par "
      "con la semilla sellada en la nota del mandato, y toda ficha en la que las dos lecturas no coinciden. La primera lectura se muestra solo en las "
      "discrepancias. El texto de cada unidad está en `fichas_c1.md` y las páginas, en la carpeta del lector.\n"]
for par, r in c3["por_par"].items():
    md.append(f"\n## → {par}\n")
    md.append(f"C3: {r['correctas']} correctas, {r['incorrectas']} incorrectas, {r['no_decidibles']} no decidibles, de {r['n']}; límite inferior de "
              f"Wilson al 95 % {r['wilson95_inferior']}; {'confirma' if r['confirma'] else 'no confirma'} con el criterio del §2 (antes de C4).\n")
    la = c3["lista_autora"][par]
    for titulo, ids in (("Incorrectas", la["incorrectas"]), ("No decidibles", la["no_decidibles"]),
                        (f"Correctas sorteadas (semilla {la['semilla']})", la["correctas_sorteadas"])):
        md.append(f"\n### {titulo} ({len(ids)})\n")
        md += [ficha(i, i in c3["discrepancias_con_la_primera"]) for i in ids] or ["(ninguna)\n"]
otras = [d for d in c3["discrepancias_con_la_primera"] if not any(d in c3["lista_autora"][p][k] for p in c3["lista_autora"] for k in ("incorrectas", "no_decidibles", "correctas_sorteadas"))]
md.append(f"\n## Discrepancias con la primera lectura que no están arriba ({len(otras)} de {len(c3['discrepancias_con_la_primera'])})\n")
md += [ficha(i, True) for i in otras] or ["(ninguna)\n"]
open(out, "w", encoding="utf-8").write("\n".join(md))
print("discrepancias:", c3["discrepancias_con_la_primera"], "| fuera de las otras listas:", otras)
print({p: {k: len(v) if isinstance(v, list) else v for k, v in la.items()} for p, la in c3["lista_autora"].items()})
