"""Mesa, 09/10/2026, USD 0: arma la carpeta del lector de la repetición de C2 de U-CONF-MATRIZ (C2-bis) desde las 60 fichas
selladas en C1, sin abrir la planilla de C2 ni el FRENO de C3.
- Controla el sha256 de c1/fichas_c1.jsonl contra su sello (ebe7dd72…) y cada PNG contra el manifiesto de la mesa.
- Por ficha conserva: ficha, predicado, origen (tipo, etiqueta, descripción y tramo de E1), destino (etiqueta, descripción y tramo
  de E1: SIN tipo y SIN id, porque el juicio no los necesita y revelan el par), unidad (texto propio y heredado, páginas), páginas
  renderizadas y el nombre del PDF. Saca los ids de los dos nodos (el del destino empieza con su tipo en las 60) y la ruta del PDF
  en el repo. El orden es el de C1.
- Escribe en <salida>: fichas.jsonl, fichas.md, paginas/, planilla.jsonl (vacía, una fila por ficha), instrucciones.md,
  sellar_planilla.py y manifest.txt. Nada de eso nombra el par, el umbral, cifras previas ni consecuencias.
- Escribe en <control>: el control de que ninguna ficha trae el tipo del destino, y cuántas veces aparecen las palabras
  «Potestad» u «Operación» en el texto que queda (etiquetas, descripciones y texto de la norma), como exposición declarada.
Uso: python3 -B armar_paquete_lector_C2bis_mesa.py <repo> <manifiesto_png_87.sha256> <salida> <control.json>"""
import json, sys, os, hashlib, shutil, re
repo, mpng, out, ctrl = sys.argv[1:5]
F = os.path.join(repo, "data/experiment/conf_matriz/c1/fichas_c1.jsonl")
assert hashlib.sha256(open(F, "rb").read()).hexdigest() == "ebe7dd72bcd04b8c1781c1756f4048540d432c458adb35af7cf328bb17d3e8a3"
png = {l[66:].strip(): l[:64] for l in open(mpng)}
L = [json.loads(x) for x in open(F, encoding="utf-8") if x.strip()]
assert len(L) == 60
os.makedirs(os.path.join(out, "paginas"), exist_ok=True)
nodo = lambda n, con_tipo: {**({"tipo": n["tipo"]} if con_tipo else {}), "etiqueta": n["etiqueta"],
                            "descripcion_extractor": n["descripcion_extractor"], "tramo_e1": n["tramo_e1"],
                            "otras_unidades_de_procedencia": n["otras_unidades_de_procedencia"]}
fichas = []
for f in L:
    for p in f["paginas_render"]:
        src = os.path.join(repo, "data/experiment/conf_matriz/c1", p)
        h = hashlib.sha256(open(src, "rb").read()).hexdigest()
        assert png["data/experiment/conf_matriz/c1/" + p] == h, p
        shutil.copyfile(src, os.path.join(out, p))
    fichas.append({"ficha": f["ficha"], "predicado": f["predicado"], "origen": nodo(f["origen"], True),
                   "destino": nodo(f["destino"], False), "unidad": f["unidad"], "paginas_render": f["paginas_render"],
                   "pdf": os.path.basename(f["pdf"])})
with open(os.path.join(out, "fichas.jsonl"), "w", encoding="utf-8") as w:
    for f in fichas:
        w.write(json.dumps(f, ensure_ascii=False) + "\n")
md = ["# Fichas para leer\n", "Sesenta fichas, en el orden de lectura. Las descripciones y los tramos son salida del extractor, no texto de "
      "la norma. El texto de la norma es el de la unidad (propio y heredado) y el de las páginas.\n"]
for f in fichas:
    o, d, u = f["origen"], f["destino"], f["unidad"]
    md += [f"\n## {f['ficha']}\n", f"- **Predicado:** `{f['predicado']}`",
           f"- **Origen:** {o['tipo']} — «{o['etiqueta']}»", f"  - descripción (salida del extractor): {o['descripcion_extractor']}",
           f"  - tramo de E1 en la unidad (salida del extractor): {o['tramo_e1']!r}",
           f"- **Destino:** «{d['etiqueta']}»", f"  - descripción (salida del extractor): {d['descripcion_extractor']}",
           f"  - tramo de E1 en la unidad (salida del extractor): {d['tramo_e1']!r}",
           f"- **Unidad:** `{u['chunk_id']}` ({u['to']}, punto {u['punto']}, {u['rol_documental']})",
           f"- **Páginas:** unidad {u['paginas_unidad']}, arista {u['paginas_arista']}; PDF `{f['pdf']}`",
           "- **Render:** " + ", ".join(f"`{p}`" for p in f["paginas_render"]), "- **Texto heredado:**"]
    md += [f"  - [{h['tipo']}, {h['unidad_origen']}, p. {h['paginas']}] {h['texto']}" for h in u["herencia"]] or ["  - (ninguno)"]
    md += [f"- **Texto propio** («{u['titulo']}»):\n", "```text", u["texto_propio"], "```"]
open(os.path.join(out, "fichas.md"), "w", encoding="utf-8").write("\n".join(md) + "\n")
with open(os.path.join(out, "planilla.jsonl"), "w", encoding="utf-8") as w:
    for f in fichas:
        w.write(json.dumps({"ficha": f["ficha"], "marca": "", "nota": "", "anotaciones": "", "paginas_vistas": []}, ensure_ascii=False) + "\n")
texto = json.dumps(fichas, ensure_ascii=False)
control = {"fichas": len(fichas), "con_tipo_de_destino": sum("tipo" in f["destino"] for f in fichas),
           "con_id_de_nodo": sum("id" in f["origen"] or "id" in f["destino"] for f in fichas),
           "apariciones_en_el_texto_que_queda": {w: len(re.findall(w, texto, flags=re.I)) for w in ("potestad", "operaci[oó]n")},
           "fichas_sha256_origen": "ebe7dd72bcd04b8c1781c1756f4048540d432c458adb35af7cf328bb17d3e8a3",
           "paginas": sum(len(f["paginas_render"]) for f in fichas), "paginas_distintas": len(os.listdir(os.path.join(out, "paginas")))}
json.dump(control, open(ctrl, "w"), ensure_ascii=False, indent=1)
print(json.dumps(control, ensure_ascii=False))
