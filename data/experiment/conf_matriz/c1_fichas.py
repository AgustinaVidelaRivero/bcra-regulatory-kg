"""
c1_fichas.py — U-CONF-MATRIZ, C1 (mandato FIRMADO en 90addb35, §4): las 60 fichas, en el orden de lectura del acta sellada
(c1/acta_c1.json), con su página renderizada. USD 0.

  Cada ficha lleva:
  - el nodo Condicion (tipo, etiqueta y descripción) y el predicado y el nodo de destino (tipo, etiqueta y descripción), con la
    descripción marcada como salida del extractor;
  - la unidad de procedencia de la arista, que es también la de los dos extremos (en las 907 aristas de la población los dos
    extremos tienen una procedencia en la unidad de la arista; el script lo controla): su texto heredado (`herencia`) y propio
    (`texto`) de e0_chunking/salida_tanda0_r2b/chunks_<to>.json, y el tramo de E1 de cada extremo en esa unidad;
  - las páginas y la ruta del PDF (del manifiesto tanda0_10tos_r2b.json, con su sha256 controlado), y el render de cada página
    de la unidad, de la arista y del texto heredado que no es encabezado (pdftoppm -r 110, como
    med_umbrales/p/code/armador_fichas_P.py).
  No lleva el par ni el orden del sorteo, ni campos de verificación (tramo_verificado, mención verificada, coherencia), ni otras
  aristas de los nodos, ni el resultado del estudio original. El tipo del nodo de destino va porque el §4 lo pide.

Corre desde la raíz de una COPIA del repo (CLAUDE.md §4.l) y escribe solo en --salida: fichas_c1.md, fichas_c1.jsonl y paginas/.
  PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B data/experiment/conf_matriz/c1_fichas.py --salida DIR
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
ACTA = Path(__file__).resolve().parent / "c1" / "acta_c1.json"
ACTA_SHA256 = "f5990dff532e6ca2c9eb91e4f8db7e98be105da517e1071c7b8ddc14c8926602"   # c1/sello_acta_c1.txt
REX = REPO / "data" / "experiment" / "reextraccion_v2"
KG = REX / "corpus_tanda0" / "ens_diez_r2b_sincola" / "r2" / "kg.json"
E0 = REX / "e0_chunking" / "salida_tanda0_r2b"
MANIFIESTO = REX / "manifiestos" / "tanda0_10tos_r2b.json"
PDFTOPPM = "/opt/homebrew/bin/pdftoppm"
DPI = 110


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def prov_en(nodo: dict, cid: str) -> dict:
    ps = [p for p in nodo["provenances"] if p["chunk_id"] == cid]
    if not ps:
        raise SystemExit(f"{nodo['id']} sin procedencia en {cid}")
    return ps[0]


def bloque_nodo(nodo: dict, prov: dict) -> dict:
    return {"id": nodo["id"], "tipo": nodo["type"], "etiqueta": nodo["label"],
            "descripcion_extractor": nodo["properties"].get("descripcion"),
            "tramo_e1": prov.get("tramo"),
            "otras_unidades_de_procedencia": len({p["chunk_id"] for p in nodo["provenances"]}) - 1}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", type=Path, required=True)
    ap.add_argument("--sin-render", action="store_true")
    a = ap.parse_args()

    raw_acta = ACTA.read_bytes()
    if sha(raw_acta) != ACTA_SHA256:
        raise SystemExit("acta distinta de la sellada")
    acta = json.loads(raw_acta)
    raw = KG.read_bytes()
    if sha(raw) != acta["grafo"]["kg_sha256"]:
        raise SystemExit("kg.json distinto del sellado")
    kg = json.loads(raw)
    nodos = {n["id"]: n for n in kg["nodes"]}
    aristas = {(e["source"], e["target"]): e for e in kg["edges"] if e["relation"] == "condicion_de"}
    man = json.loads(MANIFIESTO.read_bytes())
    pdfs = {t["id"]: t for t in man["tos"]}
    chunks, sha_chunks = {}, {}
    for to in pdfs:
        p = E0 / f"chunks_{to}.json"
        sha_chunks[p.name] = sha(p.read_bytes())
        for c in json.loads(p.read_text(encoding="utf-8")):
            chunks[c["id"]] = c

    # control de la población entera: los dos extremos tienen procedencia en la unidad de la arista
    for par in ("Operacion", "Potestad"):
        for o, d, cid in acta["poblacion"][par]["filas"]:
            prov_en(nodos[o], cid), prov_en(nodos[d], cid)

    a.salida.mkdir(parents=True, exist_ok=True)
    (a.salida / "paginas").mkdir(exist_ok=True)
    fichas, md, renders, sha_pdfs = [], [], {}, {}
    for f in acta["orden_de_lectura"]["fichas"]:
        e = aristas[(f["origen"], f["destino"])]
        cid = e["provenance"]["chunk_id"]
        if cid != f["chunk_id_arista"]:
            raise SystemExit(f"{f['ficha']}: chunk_id distinto del acta")
        base = cid.split("::parte")[0]
        ch = chunks[base]
        to = e["provenance"]["to"]
        t = pdfs[to]
        if t["pdf"] not in sha_pdfs:
            s = sha((REPO / t["pdf"]).read_bytes())
            if s != t["sha256_pdf"]:
                raise SystemExit(f"{t['pdf']} con sha256 {s}, no el del manifiesto")
            sha_pdfs[t["pdf"]] = s
        o, d = nodos[f["origen"]], nodos[f["destino"]]
        paginas = sorted(set(ch["paginas"]) | set(e["provenance"]["paginas"])
                         | {pg for h in ch["herencia"] if h["tipo"] != "encabezado" for pg in h["paginas"]})
        imgs = []
        for pg in paginas:
            nombre = f"{to}_p{pg}.png"
            renders[nombre] = (REPO / t["pdf"], pg)
            imgs.append(f"paginas/{nombre}")
        ficha = {"ficha": f["ficha"], "predicado": "condicion_de",
                 "origen": bloque_nodo(o, prov_en(o, cid)), "destino": bloque_nodo(d, prov_en(d, cid)),
                 "unidad": {"chunk_id": cid, "chunk_e0": base, "parte_por_corte": base != cid, "to": to,
                            "punto": e["provenance"]["punto"], "rol_documental": e["provenance"]["rol_documental"],
                            "titulo": ch["titulo"], "herencia": ch["herencia"], "texto_propio": ch["texto"],
                            "paginas_unidad": ch["paginas"], "paginas_arista": e["provenance"]["paginas"]},
                 "pdf": t["pdf"], "paginas_render": imgs}
        fichas.append(ficha)

        md.append(f"## {f['ficha']}\n")
        md.append(f"- **Predicado:** `condicion_de`")
        for rol, b in (("Origen", ficha["origen"]), ("Destino", ficha["destino"])):
            md.append(f"- **{rol}:** {b['tipo']} — «{b['etiqueta']}» (`{b['id']}`)")
            md.append(f"  - descripción (salida del extractor): {b['descripcion_extractor']}")
            md.append(f"  - tramo de E1 en la unidad (salida del extractor): {b['tramo_e1']!r}")
        u = ficha["unidad"]
        aviso = " — **la arista viene de una parte de la unidad partida por corte; se muestra la unidad entera**" \
            if u["parte_por_corte"] else ""
        md.append(f"- **Unidad:** `{cid}` ({to}, punto {u['punto']}, {u['rol_documental']}){aviso}")
        md.append(f"- **Páginas:** unidad {u['paginas_unidad']}, arista {u['paginas_arista']}; PDF `{t['pdf']}`")
        md.append(f"- **Render:** " + ", ".join(f"`{x}`" for x in imgs))
        md.append(f"- **Texto heredado:**")
        for h in u["herencia"]:
            md.append(f"  - [{h['tipo']}, {h['unidad_origen']}, p. {h['paginas']}] {h['texto']}".replace("\n", " "))
        md.append(f"- **Texto propio** («{u['titulo']}»):\n")
        md.append("```text\n" + u["texto_propio"] + "\n```\n")

    if not a.sin_render:
        for nombre, (pdf, pg) in sorted(renders.items()):
            destino = a.salida / "paginas" / nombre
            if not destino.exists():
                subprocess.run([PDFTOPPM, "-r", str(DPI), "-f", str(pg), "-l", str(pg), "-png", "-singlefile", str(pdf),
                                str(destino.with_suffix(""))], check=True)

    cab = ("# U-CONF-MATRIZ, C1: fichas en el orden de lectura\n\n"
           f"Acta sellada `c1/acta_c1.json` (sha256 `{ACTA_SHA256}`). Las fichas no llevan el par ni el orden del sorteo; "
           "las descripciones y los tramos son salida del extractor, no del texto. Sin el veredicto de E3, sin otras aristas "
           "de los nodos y sin el resultado del estudio original.\n\n")
    (a.salida / "fichas_c1.md").write_text(cab + "\n".join(md) + "\n", encoding="utf-8")
    with open(a.salida / "fichas_c1.jsonl", "w", encoding="utf-8") as fh:
        for x in fichas:
            fh.write(json.dumps(x, ensure_ascii=False) + "\n")
    (a.salida / "insumos_fichas_c1.json").write_text(json.dumps(
        {"acta_sha256": ACTA_SHA256, "kg_sha256": sha(raw), "manifiesto_sha256": sha(MANIFIESTO.read_bytes()),
         "chunks_sha256": sha_chunks, "pdfs_sha256": sha_pdfs, "render": {"herramienta": PDFTOPPM, "dpi": DPI},
         "paginas_render": {n: sha((a.salida / "paginas" / n).read_bytes()) for n in sorted(renders)
                            if (a.salida / "paginas" / n).exists()},
         "c1_fichas.py_sha256": sha(Path(__file__).read_bytes())}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"fichas": len(fichas), "paginas": len(renders),
                      "partes": [x["ficha"] for x in fichas if x["unidad"]["parte_por_corte"]]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
