"""Mesa, 10/10/2026, USD 0: arma la carpeta del lector de (e) de U-OMISIONES-COD (precisión del clasificador de la copia de la nota de
E3) con las 16 detecciones fuera de las 64 unidades de T4, desde la lista sellada de O1, sin imprimir ninguna detección.
- Controla el sha256 de la lista (4c385529…) y que las fuera de las 64 sean 16.
- Por caso: la unidad (texto propio y heredado, de la E0 de la tanda 0 r2b), las notas de E3 del veredicto anterior al último
  reintento (las mismas fuentes que medir_e.py: finales.jsonl y veredictos.jsonl de salida_r2b), el tipo de la entidad, el campo y su
  texto, las ventanas en común con la nota y, como ayuda, las palabras de contenido de la nota que no están en la unidad y las de
  metalenguaje (el procedimiento de la regla de lectura de T4). NO lleva la clase que asignó el clasificador.
- Renderiza las páginas de cada unidad desde una copia de los PDFs (pdftoppm, 80 ppp).
- Escribe en <salida>: casos.jsonl, casos.md, paginas/, planilla.jsonl (vacía), y en <control> un resumen sin contenido.
Uso: python3 -B armar_paquete_lector_e_mesa.py <repo> <dir_pdfs_copia> <salida> <control.json>"""
import json, sys, os, hashlib, subprocess
repo, pdfs, out, ctrl = sys.argv[1:5]
L = os.path.join(repo, "data/experiment/omisiones_cod/o1/salidas/e_lista_sellada/detecciones_e_copia_nota_diez.json")
assert hashlib.sha256(open(L, "rb").read()).hexdigest() == "4c3855292349a75d675216fd7ae772a948777dd76e226eaa1f32bcf67cda3efd"
det = [d for d in json.load(open(L))["detecciones"] if not d["dentro_de_las_64_de_T4"]]
assert len(det) == 16, len(det)
SAL = os.path.join(repo, "data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b")
E0 = os.path.join(repo, "data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b")
jl = lambda p: [json.loads(x) for x in open(p, encoding="utf-8") if x.strip()] if os.path.exists(p) else []
PDF = {"cap": "TO_capitales_minimos_actual.pdf", "cla": "TO_clasificacion_deudores_actual.pdf", "ext": "TO_exterior_cambios_actual.pdf",
       "pro": "TO_proteccion_usuarios_servicios_financieros_actual.pdf", "ric": "TO_regimen_informativo_contable_mensual_actual.pdf"}
os.makedirs(os.path.join(out, "paginas"), exist_ok=True)
det.sort(key=lambda d: (d["to"], d["chunk_id"], str(d["local_id"]), d["campo"]))
casos, cache = [], {}
for i, d in enumerate(det, 1):
    to, cid = d["to"], d["chunk_id"]
    if to not in cache:
        cache[to] = ({c["id"]: c for c in json.load(open(os.path.join(E0, f"chunks_{to}.json")))},
                     {r["chunk_id"]: r for r in jl(os.path.join(SAL, to, "finales.jsonl"))},
                     jl(os.path.join(SAL, to, "veredictos.jsonl")))
    ch, fin, ver = cache[to]
    c, f = ch[cid], fin[cid]
    n = f.get("n_reintentos") or 0
    previa = [v for v in ver if v["chunk_id"] == cid and v.get("intento") == n - 1][-1:]
    notas = [x.get("nota") or "" for v in previa for x in (v.get("faltantes") or [])]
    pdf = os.path.join(pdfs, PDF.get(to, f"{to}.pdf"))
    pags = []
    for p in c["paginas"]:
        nombre = f"{to}_p{p}"
        if not os.path.exists(os.path.join(out, "paginas", f"{nombre}.png")):
            subprocess.run(["pdftoppm", "-r", "80", "-png", "-singlefile", "-f", str(p), "-l", str(p), pdf,
                            os.path.join(out, "paginas", nombre)], check=True)
        pags.append(f"paginas/{nombre}.png")
    casos.append({"caso": f"C{i:02d}", "unidad": {"id": cid, "to": to, "titulo": c["titulo"], "paginas": c["paginas"],
                  "texto_propio": c["texto"], "herencia": c["herencia"]}, "tipo_de_la_entidad": d["type"], "campo": d["campo"],
                  "texto_del_campo": d["texto"], "notas_del_verificador": notas, "ventanas_en_comun": d["ventanas"],
                  "ayuda": {"palabras_de_contenido_de_la_nota_que_no_estan_en_la_unidad": d["palabras_de_la_nota"],
                            "metalenguaje_del_verificador": d["metalenguaje"]}, "paginas_render": pags})
with open(os.path.join(out, "casos.jsonl"), "w", encoding="utf-8") as w:
    for c in casos:
        w.write(json.dumps(c, ensure_ascii=False) + "\n")
md = ["# Casos para leer\n", "Dieciséis casos. En cada uno: el texto de la unidad de la norma (propio y heredado), las notas del verificador, el campo de la "
      "entidad extraída y las ventanas de tres palabras que el campo comparte con las notas. La ayuda lista palabras; no decide nada.\n"]
for c in casos:
    u = c["unidad"]
    md += [f"\n## {c['caso']}\n", f"- **Unidad:** `{u['id']}` ({u['to']}), páginas {u['paginas']}; render: " + ", ".join(f"`{p}`" for p in c["paginas_render"]),
           f"- **Entidad:** {c['tipo_de_la_entidad']}; **campo:** {c['campo']}", f"- **Texto del campo:** «{c['texto_del_campo']}»",
           "- **Ventanas en común con las notas:** " + "; ".join(f"«{w}»" for w in c["ventanas_en_comun"]),
           "- **Ayuda, palabras de contenido de las notas que no están en la unidad:** " + (", ".join(c["ayuda"]["palabras_de_contenido_de_la_nota_que_no_estan_en_la_unidad"]) or "(ninguna)"),
           "- **Ayuda, metalenguaje del verificador:** " + (", ".join(c["ayuda"]["metalenguaje_del_verificador"]) or "(ninguno)"),
           "- **Notas del verificador:**"] + [f"  - {x}" for x in c["notas_del_verificador"]] + \
          ["- **Texto heredado:**"] + [f"  - [{h['tipo']}, {h['unidad_origen']}] {h['texto']}" for h in u["herencia"]] + \
          [f"- **Texto propio** («{u['titulo']}»):\n", "```text", u["texto_propio"], "```"]
open(os.path.join(out, "casos.md"), "w", encoding="utf-8").write("\n".join(md) + "\n")
with open(os.path.join(out, "planilla.jsonl"), "w", encoding="utf-8") as w:
    for c in casos:
        w.write(json.dumps({"caso": c["caso"], "clase": None, "razon": "", "paginas_vistas": []}, ensure_ascii=False) + "\n")
mapa = [{"caso": c["caso"], "chunk_id": d["chunk_id"], "local_id": d["local_id"], "campo": d["campo"]} for c, d in zip(casos, det)]
json.dump({"casos": len(casos), "unidades": len({d["chunk_id"] for d in det}), "con_notas": sum(bool(c["notas_del_verificador"]) for c in casos),
           "paginas": len(os.listdir(os.path.join(out, "paginas"))), "mapa_caso_a_deteccion": mapa}, open(ctrl, "w"), ensure_ascii=False, indent=1)
print(json.dumps({"casos": len(casos), "unidades": len({d["chunk_id"] for d in det}), "con_notas": sum(bool(c["notas_del_verificador"]) for c in casos),
                  "paginas": len(os.listdir(os.path.join(out, "paginas")))}))
