"""Arma las 20 fichas, las planillas vacías y la copia de las fuentes del gold de Q12, mitad de verificación: las 20 de A2.2 (mesa,
§276, 25/10/2026). Es `ev2_juez/gold_q12_ajuste/codigo/armar_fichas_gold_q12_mesa.py` (§128) con la respuesta de A2.2. USD 0, sin API.

Uso: python3 -I -B armar_fichas_gold_q12_verificacion_mesa.py <repo> <clave_sorteo.json> <carpeta para_leer>

Lee, solo lectura:
  - la clave del sorteo (qué respuesta va en cada ficha);
  - del repo: las preguntas de EV2 con su gold (ancla y criterios con cita); de cada sesión de N = 1 de A2.2, solo
    `final_json_R4.respuesta` de su meta, que es lo único que vio el juez (`a2_2/juez_a2_2.py`, `respuestas`); los cinco PDF de
    data/experiment/subset/.
No lee ningún veredicto. No escribe en el repo. Imprime solo cuentas.

La ficha no dice el brazo, el id opaco, la sesión ni el id de la pregunta. Tampoco lleva las citas que dio el agente: su formato
cambia de un brazo a otro y lo delataría, y el juez no las vio.
"""
import csv
import hashlib
import html
import json
import re
import shutil
import subprocess
import sys
import unicodedata
from pathlib import Path

PDF_DE_TO = {"ext": "TO_exterior_cambios_actual.pdf", "cap": "TO_capitales_minimos_actual.pdf",
             "cla": "TO_clasificacion_deudores_actual.pdf", "ric": "TO_regimen_informativo_contable_mensual_actual.pdf",
             "pro": "TO_proteccion_usuarios_servicios_financieros_actual.pdf"}
A = "data/experiment/banco_mcp/a2_2"
MARCAS = ("fragmentos_bm25", "fragmentos_denso", "A22J-", "N1-", "PRB-", "RC1-", "RC2-", "RC3-", "id_opaco")


def normalizar(s: str) -> str:
    s = unicodedata.normalize("NFKC", s).replace("­", "")
    s = re.sub(r"[‐-―−]", "-", s)
    s = re.sub(r"[“”«»\"]", '"', s)
    s = re.sub(r"[‘’']", "'", s)
    s = re.sub(r"-\s*\n\s*", "", s)          # des-hifenado al final de renglón (absorbe la sangría de -layout)
    return re.sub(r"\s+", " ", s).strip().lower()


def paginas_pdf(pdf: Path) -> list:
    txt = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True, text=True, check=True).stdout
    return txt.split("\f")


def ubicar(cita: str, pags_norm: list) -> str:
    """Página o páginas (desde 1) donde está la cita; si no está entera, por su comienzo; si no, 'no ubicada'."""
    c = normalizar(cita)
    for i, p in enumerate(pags_norm):
        if c in p:
            return f"pág. {i + 1}"
    for i in range(len(pags_norm) - 1):
        if c in pags_norm[i] + " " + pags_norm[i + 1]:
            return f"págs. {i + 1}-{i + 2}"
    pref = c[:60]
    hits = [i + 1 for i, p in enumerate(pags_norm) if pref in p]
    if hits:
        return "pág. " + ", ".join(map(str, hits)) + " (ubicada por su comienzo)"
    return "no ubicada en el PDF"


def paginas_del_punto(punto: str, pags_raw: list, hasta: int | None) -> str:
    """Páginas donde un renglón empieza con el número del punto (p. ej. «6.11.»); se queda con la última antes de la cita."""
    rx = re.compile(r"^\s*" + re.escape(punto) + r"\.?\s", re.M)
    hits = [i + 1 for i, p in enumerate(pags_raw) if rx.search(p)]
    if not hits:
        return "encabezado no ubicado"
    if hasta:
        antes = [h for h in hits if h <= hasta]
        if antes:
            return f"pág. {antes[-1]}"
    return "pág. " + ", ".join(map(str, hits))


def main() -> None:
    repo, clave_p, out = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
    clave = json.loads(clave_p.read_text(encoding="utf-8"))
    preguntas = {p["id"]: p for p in json.loads(
        (repo / "data/experiment/exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json").read_text(encoding="utf-8"))["preguntas"]}
    (out / "fichas").mkdir(parents=True, exist_ok=True)
    (out / "fuentes").mkdir(parents=True, exist_ok=True)

    pdf_cache, sha_pdf = {}, {}
    for to, nombre in PDF_DE_TO.items():
        src = repo / "data/experiment/subset" / nombre
        dst = out / "fuentes" / nombre
        shutil.copyfile(src, dst)
        sha_pdf[nombre] = hashlib.sha256(src.read_bytes()).hexdigest()
        assert hashlib.sha256(dst.read_bytes()).hexdigest() == sha_pdf[nombre]
        raw = paginas_pdf(src)
        pdf_cache[to] = (raw, [normalizar(p) for p in raw])

    fichas_md, fichas_html, filas_crit, filas_resp, control = [], [], [], [], []
    for f in clave["fichas"]:
        q = preguntas[f["id_pregunta"]]
        meta = json.loads((repo / A / "resultados/n1" / f"meta_{f['id_sesion']}.json").read_text(encoding="utf-8"))
        resp = meta["final_json_R4"]["respuesta"]
        assert hashlib.sha256(resp.encode("utf-8")).hexdigest() == f["sha256_respuesta"], f["ficha"]
        crits = q["gold"]["criterios"]
        assert len(crits) == f["n_criterios"], f["ficha"]
        raw, norm = pdf_cache[q["to"]]
        ubic = [ubicar(c["cita_textual"], norm) for c in crits]
        primera = next((int(re.search(r"\d+", u).group()) for u in ubic if u.startswith("pág")), None)
        anclas = [(a, paginas_del_punto(a.split(":", 1)[1], raw, primera)) for a in q["gold"]["ancla"]]
        pdf = PDF_DE_TO[q["to"]]
        control.append({"ficha": f["ficha"], "ubicaciones": ubic, "anclas": anclas})

        md = [f"# Ficha {f['ficha']}", "",
              f"- **Documento:** {q['to_nombre']} (`fuentes/{pdf}`)",
              "- **Ancla normativa de la pregunta:** " + "; ".join(f"punto {a.split(':', 1)[1]} ({p})" for a, p in anclas),
              "", "## Pregunta", "", q["pregunta"], "", "## Respuesta (tal cual, sin tocar)", "", "```text", resp, "```", "",
              "## Criterios", ""]
        for i, (c, u) in enumerate(zip(crits, ubic), 1):
            md += [f"**{i}.** {c['criterio']}", "", f"> Cita de la norma: «{c['cita_textual']}» ({u})", ""]
            filas_crit.append({"ficha": f["ficha"], "criterio": i, "veredicto (cumplido / no_cumplido)": "",
                               "fragmento de la respuesta (opcional)": "", "dudosa para mí (sí/no)": "",
                               "necesita experto del dominio (sí/no)": "", "criterio mal planteado (sí/no)": "", "nota": ""})
        md += ["## Lo que anotás", "", "En la planilla: un renglón por criterio y uno por respuesta (ver la regla de lectura).", ""]
        (out / "fichas" / f"{f['ficha']}.md").write_text("\n".join(md), encoding="utf-8")
        fichas_md.append("\n".join(md))
        filas_resp.append({"ficha": f["ficha"], "clasificación (abstencion / contenido)": "",
                           "error fuera de los criterios (sí/no)": "", "cuál": "", "minutos": "", "nota": ""})

        h = [f"<section><h2>Ficha {f['ficha']}</h2>",
             f"<p><b>Documento:</b> {html.escape(q['to_nombre'])} (<code>fuentes/{pdf}</code>)<br>",
             "<b>Ancla normativa:</b> " + html.escape("; ".join(f"punto {a.split(':', 1)[1]} ({p})" for a, p in anclas)) + "</p>",
             f"<h3>Pregunta</h3><p>{html.escape(q['pregunta'])}</p>",
             f"<h3>Respuesta (tal cual)</h3><pre>{html.escape(resp)}</pre><h3>Criterios</h3><ol>"]
        for c, u in zip(crits, ubic):
            h.append(f"<li>{html.escape(c['criterio'])}<blockquote>«{html.escape(c['cita_textual'])}» ({html.escape(u)})</blockquote></li>")
        h.append("</ol></section>")
        fichas_html.append("\n".join(h))

    (out / "fichas_VG01_a_VG20.md").write_text("\n\n---\n\n".join(fichas_md) + "\n", encoding="utf-8")
    estilo = ("body{font-family:Georgia,serif;max-width:46rem;margin:2rem auto;padding:0 1rem;line-height:1.5}"
              "pre{white-space:pre-wrap;background:#f6f6f2;padding:.8rem;border-left:3px solid #999}"
              "blockquote{margin:.4rem 0 .8rem 1rem;color:#333;font-style:italic}section{page-break-after:always}")
    (out / "fichas_VG01_a_VG20.html").write_text(
        "<!doctype html><html lang='es'><head><meta charset='utf-8'><title>Fichas del gold, verificación</title><style>" + estilo +
        "</style></head><body><h1>Fichas del gold, mitad de verificación (VG01 a VG20)</h1>\n" + "\n".join(fichas_html) +
        "</body></html>\n", encoding="utf-8")
    for nombre, filas in (("planilla_criterios_gold_q12_verificacion.csv", filas_crit), ("planilla_respuestas_gold_q12_verificacion.csv", filas_resp)):
        with open(out / nombre, "w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(filas[0].keys()))
            w.writeheader()
            w.writerows(filas)
    (out / "estructura_planillas.json").write_text(json.dumps(
        {"criterios": {"columnas": list(filas_crit[0]), "renglones": [[f["ficha"], str(f["criterio"])] for f in filas_crit]},
         "respuestas": {"columnas": list(filas_resp[0]), "renglones": [[f["ficha"]] for f in filas_resp]}},
        ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    respuestas_de = {f["ficha"]: json.loads((repo / A / "resultados/n1" / f"meta_{f['id_sesion']}.json").read_text(encoding="utf-8"))
                     ["final_json_R4"]["respuesta"] for f in clave["fichas"]}
    for p in sorted(out.rglob("*")):
        if p.is_file() and p.suffix in (".md", ".html", ".csv"):
            txt = p.read_text(encoding="utf-8")
            for r in respuestas_de.values():
                txt = txt.replace(r, "").replace(html.escape(r), "")
            for f in clave["fichas"]:
                for x in (f["id_opaco"], f["id_sesion"], f["id_pregunta"]):
                    assert x not in txt, f"{p.name} trae un id de la clave"
            assert not any(m in txt for m in MARCAS), f"{p.name} trae una marca de brazo fuera de una respuesta"
    con_marca = sum(any(m in r.lower() for m in ("fragmento", "grafo", "bm25", "denso", "knowledge graph")) for r in respuestas_de.values())
    print(json.dumps({"fichas": len(clave["fichas"]), "criterios": len(filas_crit),
                      "respuestas_que_nombran_grafo_o_fragmentos": con_marca,
                      "citas_no_ubicadas": sum(u == "no ubicada en el PDF" for c in control for u in c["ubicaciones"]),
                      "citas_por_su_comienzo": sum("comienzo" in u for c in control for u in c["ubicaciones"]),
                      "citas_en_dos_paginas": sum(u.startswith("págs.") for c in control for u in c["ubicaciones"]),
                      "anclas_sin_encabezado": sum(p == "encabezado no ubicado" for c in control for _, p in c["anclas"]),
                      "sha256_pdf": sha_pdf}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
