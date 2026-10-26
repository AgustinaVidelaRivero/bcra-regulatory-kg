"""armar_adjudicaciones_a2_2_mesa.py — el material de las adjudicaciones de A2.2 de la autora (A-D8; mesa, §277, 26/10/2026), con
el molde de la adjudicación ciega de la tanda 0 (`docs/mandatos/UTANDA0_2A_E5c_adjudicacion.md`, decisiones 1, 3 y 4). USD 0, sin API.

Uso: python3 -I -B armar_adjudicaciones_a2_2_mesa.py <repo> <clave.json> <carpeta de lectura>

Qué respuestas van (la población A del molde, con la regla del análisis de A2.2, `analizar_a2_2.py`, `finales`):
  - un par (pregunta, brazo) que no fue a N = 3 y cuya respuesta de N = 1 el juez deja en `requiere_adjudicacion`: una ficha con esa
    respuesta;
  - un par que fue a N = 3 y cuyo agregado de las tres re-corridas (`poblacion_a2_2.agregar_recorridas`, con `agregacion_enc`) queda
    en `requiere_adjudicacion`: una ficha por cada re-corrida en `requiere_adjudicacion`; dos con el mismo texto, dentro del par,
    comparten ficha;
  - un par decidido por invariancia no lleva ficha.
El brazo, la repetición y el id opaco de cada respuesta salen del código congelado del juez de A2.2 (`juez_a2_2.respuestas` e
`id_opaco`, como en el sorteo de Q8). No abre ninguna carpeta `desanonimizacion_SOLO_MESA/`. Cada entrada es la de HEAD; si no, frena.
Las fichas, en un orden con la semilla `A22:orden_adjudicacion:v1`. Cada una muestra el documento, el ancla, la pregunta, la respuesta tal
cual y los criterios con su cita y su página; nunca el brazo, la repetición, el id opaco, la sesión, el id de la pregunta, el veredicto
ni los modales del juez. La clave (qué respuestas lleva cada ficha) va al paquete de la mesa. Imprime solo cuentas.
"""
import csv
import hashlib
import html
import json
import random
import re
import shutil
import subprocess
import sys
import unicodedata
from pathlib import Path

SEMILLA = "A22:orden_adjudicacion:v1"
PENDIENTE = "requiere_adjudicacion"
PDF_DE_TO = {"ext": "TO_exterior_cambios_actual.pdf", "cap": "TO_capitales_minimos_actual.pdf",
             "cla": "TO_clasificacion_deudores_actual.pdf", "ric": "TO_regimen_informativo_contable_mensual_actual.pdf",
             "pro": "TO_proteccion_usuarios_servicios_financieros_actual.pdf"}
A = "data/experiment/banco_mcp/a2_2"
ENTRADAS = {"preguntas": "data/experiment/exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json",
            "orden_corridas": f"{A}/orden_corridas_a2_2.json", "poblacion": f"{A}/poblacion/poblacion_a2_2.json",
            "orden_juez_n1": f"{A}/juez/n1/orden_juez_n1.json", "agregados_n1": f"{A}/juez/n1/agregados_n1_ciego.json",
            "orden_juez_rc": f"{A}/juez/recorridas/orden_juez_recorridas.json",
            "agregados_rc": f"{A}/juez/recorridas/agregados_recorridas_ciego.json",
            "juez_a2_2": f"{A}/juez_a2_2.py", "comun_a2_2": f"{A}/comun_a2_2.py", "poblacion_a2_2": f"{A}/poblacion_a2_2.py"}
MARCAS = ("fragmentos_bm25", "fragmentos_denso", "A22J-", "N1-", "PRB-", "RC1-", "RC2-", "RC3-", "id_opaco")
COL_VEREDICTO = "veredicto (cumplido / no_cumplido)"


def frena(m):
    raise SystemExit(f"FRENO: {m}")


def normalizar(s: str) -> str:
    s = unicodedata.normalize("NFKC", s).replace("­", "")
    s = re.sub(r"[‐-―−]", "-", s)
    s = re.sub(r"[“”«»\"]", '"', s)
    s = re.sub(r"[‘’']", "'", s)
    s = re.sub(r"-\s*\n\s*", "", s)
    return re.sub(r"\s+", " ", s).strip().lower()


def paginas_pdf(pdf: Path) -> list:
    return subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True, text=True, check=True).stdout.split("\f")


def ubicar(cita: str, pags_norm: list) -> str:
    c = normalizar(cita)
    for i, p in enumerate(pags_norm):
        if c in p:
            return f"pág. {i + 1}"
    for i in range(len(pags_norm) - 1):
        if c in pags_norm[i] + " " + pags_norm[i + 1]:
            return f"págs. {i + 1}-{i + 2}"
    hits = [i + 1 for i, p in enumerate(pags_norm) if c[:60] in p]
    return ("pág. " + ", ".join(map(str, hits)) + " (ubicada por su comienzo)") if hits else "no ubicada en el PDF"


def paginas_del_punto(punto: str, pags_raw: list, hasta) -> str:
    rx = re.compile(r"^\s*" + re.escape(punto) + r"\.?\s", re.M)
    hits = [i + 1 for i, p in enumerate(pags_raw) if rx.search(p)]
    if not hits:
        return "encabezado no ubicado"
    antes = [h for h in hits if hasta and h <= hasta]
    return f"pág. {antes[-1]}" if antes else "pág. " + ", ".join(map(str, hits))


def leer_del_repo(repo: Path) -> tuple:
    sha = {}
    for k, p in ENTRADAS.items():
        b = (repo / p).read_bytes()
        h = subprocess.run(["git", "--no-optional-locks", "-C", str(repo), "show", f"HEAD:{p}"], capture_output=True)
        if h.returncode != 0 or h.stdout != b:
            frena(f"{p} no es el de HEAD (¿falta el 193?)")
        sha[k] = hashlib.sha256(b).hexdigest()
    sys.path.insert(0, str(repo / A))
    import juez_a2_2 as JZ  # noqa: E402  (congelado: solo import)
    import poblacion_a2_2 as PB  # noqa: E402
    ld = lambda k: json.loads((repo / ENTRADAS[k]).read_text(encoding="utf-8"))  # noqa: E731
    orden, pob = ld("orden_corridas"), ld("poblacion")

    def recalcular(etapa, carpeta, poblacion, clave_orden):
        resps, _ = JZ.respuestas(etapa, repo / A / "resultados" / carpeta, orden, poblacion)
        rec = {}
        for r in resps:
            s = JZ.K.sha256_texto(r["respuesta"])
            rec[JZ.id_opaco(r["qid"], r["brazo"], r["rep"], s)] = r | {"sha256_respuesta": s, "etapa": etapa}
        ids = ld(clave_orden)["ids_opacos_en_orden"]
        if set(rec) != set(ids) or len(rec) != len(ids):
            frena(f"los ids recalculados de {etapa} no son los del orden del juez")
        return rec

    rec_n1 = recalcular("n1", "n1", None, "orden_juez_n1")
    rec_rc = recalcular("recorridas", "recorridas", pob, "orden_juez_rc")
    agr_n1 = {a["id_opaco"]: a for a in ld("agregados_n1")["agregados"]}
    agr_rc = {a["id_opaco"]: a for a in ld("agregados_rc")["agregados"]}
    if not set(agr_n1) <= set(rec_n1) or not set(agr_rc) <= set(rec_rc):
        frena("hay agregados con un id que no es de su etapa")
    v_rc = {(rec_rc[i]["qid"], rec_rc[i]["brazo"], rec_rc[i]["rep"]): a for i, a in agr_rc.items()}
    finales_rc = {(p["qid"], p["brazo"]): p["final"] for p in PB.agregar_recorridas(pob, v_rc)["pares"]}
    en_pob = {(p["qid"], p["brazo"]) for p in pob["pares"]}
    grupos = {}
    for i, a in agr_n1.items():
        r = rec_n1[i]
        if a["veredicto_pregunta"] == PENDIENTE and (r["qid"], r["brazo"]) not in en_pob:
            grupos.setdefault((r["qid"], r["brazo"], "n1", r["sha256_respuesta"]), []).append(i)
    for i, a in agr_rc.items():
        r = rec_rc[i]
        if finales_rc.get((r["qid"], r["brazo"])) == PENDIENTE and a["veredicto_pregunta"] == PENDIENTE:
            grupos.setdefault((r["qid"], r["brazo"], "recorridas", r["sha256_respuesta"]), []).append(i)
    pend_rc = {k for k, v in finales_rc.items() if v == PENDIENTE}
    if {(q, b) for q, b, e, _ in grupos if e == "recorridas"} != pend_rc:
        frena("un par pendiente de las re-corridas quedó sin ficha, o una ficha no es de un par pendiente")
    rec = rec_n1 | rec_rc
    return sha, grupos, rec


def main() -> None:
    repo, clave_p, out = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
    if clave_p.exists() or (out / "fichas").exists():
        frena("la clave o las fichas ya existen: no se pisan")
    sha_e, grupos, rec = leer_del_repo(repo)
    preguntas = {p["id"]: p for p in json.loads((repo / ENTRADAS["preguntas"]).read_text(encoding="utf-8"))["preguntas"]}
    orden = sorted(grupos)
    random.Random(SEMILLA).shuffle(orden)
    (out / "fichas").mkdir(parents=True, exist_ok=True)
    (out / "fuentes").mkdir(parents=True, exist_ok=True)
    cache, sha_pdf = {}, {}
    for to, nombre in PDF_DE_TO.items():
        src = repo / "data/experiment/subset" / nombre
        shutil.copyfile(src, out / "fuentes" / nombre)
        sha_pdf[nombre] = hashlib.sha256(src.read_bytes()).hexdigest()
        if hashlib.sha256((out / "fuentes" / nombre).read_bytes()).hexdigest() != sha_pdf[nombre]:
            frena(f"la copia de {nombre} no da su sha256")
        raw = paginas_pdf(src)
        cache[to] = (raw, [normalizar(p) for p in raw])
    fichas, filas, mds, htmls, control = [], [], [], [], []
    for n, k in enumerate(orden, 1):
        qid, brazo, etapa, s = k
        ids = sorted(grupos[k])
        resp = rec[ids[0]]["respuesta"]
        if any(rec[i]["respuesta"] != resp for i in ids):
            frena("dos respuestas de una ficha no tienen el mismo texto")
        q = preguntas[qid]
        crits = q["gold"]["criterios"]
        raw, norm = cache[q["to"]]
        ubic = [ubicar(c["cita_textual"], norm) for c in crits]
        primera = next((int(re.search(r"\d+", u).group()) for u in ubic if u.startswith("pág")), None)
        anclas = [(a, paginas_del_punto(a.split(":", 1)[1], raw, primera)) for a in q["gold"]["ancla"]]
        f = f"AD{n:02d}"
        fichas.append({"ficha": f, "ids_opacos": ids, "id_pregunta": qid, "brazo": brazo, "etapa": etapa,
                       "reps": sorted(rec[i]["rep"] for i in ids), "sha256_respuesta": s, "n_criterios": len(crits)})
        control.append(ubic)
        pdf = PDF_DE_TO[q["to"]]
        md = [f"# Ficha {f}", "", f"- **Documento:** {q['to_nombre']} (`fuentes/{pdf}`)",
              "- **Ancla normativa de la pregunta:** " + "; ".join(f"punto {a.split(':', 1)[1]} ({p})" for a, p in anclas),
              "", "## Pregunta", "", q["pregunta"], "", "## Respuesta (tal cual, sin tocar)", "", "```text", resp, "```", "", "## Criterios", ""]
        for i, (c, u) in enumerate(zip(crits, ubic), 1):
            md += [f"**{i}.** {c['criterio']}", "", f"> Cita de la norma: «{c['cita_textual']}» ({u})", ""]
            filas.append({"ficha": f, "criterio": str(i), COL_VEREDICTO: "", "observación": ""})
        md += ["## Lo que anotás", "", "En la planilla, un renglón por criterio: cumplido o no_cumplido (ver la regla).", ""]
        (out / "fichas" / f"{f}.md").write_text("\n".join(md), encoding="utf-8")
        mds.append("\n".join(md))
        h = [f"<section><h2>Ficha {f}</h2>", f"<p><b>Documento:</b> {html.escape(q['to_nombre'])} (<code>fuentes/{pdf}</code>)<br>",
             "<b>Ancla normativa:</b> " + html.escape("; ".join(f"punto {a.split(':', 1)[1]} ({p})" for a, p in anclas)) + "</p>",
             f"<h3>Pregunta</h3><p>{html.escape(q['pregunta'])}</p>", f"<h3>Respuesta (tal cual)</h3><pre>{html.escape(resp)}</pre><h3>Criterios</h3><ol>"]
        h += [f"<li>{html.escape(c['criterio'])}<blockquote>«{html.escape(c['cita_textual'])}» ({html.escape(u)})</blockquote></li>"
              for c, u in zip(crits, ubic)]
        htmls.append("\n".join(h + ["</ol></section>"]))
    nombre_todo = "fichas_de_adjudicacion_a2_2"
    (out / f"{nombre_todo}.md").write_text("\n\n---\n\n".join(mds) + "\n", encoding="utf-8")
    estilo = ("body{font-family:Georgia,serif;max-width:46rem;margin:2rem auto;padding:0 1rem;line-height:1.5}"
              "pre{white-space:pre-wrap;background:#f6f6f2;padding:.8rem;border-left:3px solid #999}"
              "blockquote{margin:.4rem 0 .8rem 1rem;color:#333;font-style:italic}section{page-break-after:always}")
    (out / f"{nombre_todo}.html").write_text("<!doctype html><html lang='es'><head><meta charset='utf-8'><title>Adjudicaciones de A2.2"
                                             "</title><style>" + estilo + "</style></head><body><h1>Fichas de adjudicación de A2.2</h1>\n"
                                             + "\n".join(htmls) + "</body></html>\n", encoding="utf-8")
    cols = ["ficha", "criterio", COL_VEREDICTO, "observación"]
    with open(out / "planilla_adjudicacion_a2_2.csv", "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows(filas)
    (out / "estructura_planilla.json").write_text(json.dumps({"columnas": cols, "renglones": [[x["ficha"], x["criterio"]] for x in filas]},
                                                             ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    textos = {rec[f["ids_opacos"][0]]["respuesta"] for f in fichas}
    for p in sorted(out.rglob("*")):
        if p.is_file() and p.suffix in (".md", ".html", ".csv", ".json"):
            t = p.read_text(encoding="utf-8")
            for r in textos:
                t = t.replace(r, "").replace(html.escape(r), "")
            for f in fichas:
                for x in f["ids_opacos"] + [f["id_pregunta"], f["sha256_respuesta"][:12]]:
                    if x in t:
                        frena(f"{p.name} trae un id de la clave")
            if any(m in t for m in MARCAS):
                frena(f"{p.name} trae una marca de brazo fuera de una respuesta")
    clave_p.parent.mkdir(parents=True, exist_ok=True)
    clave_p.write_text(json.dumps({"semilla": SEMILLA, "sha256_entradas": sha_e, "sha256_pdf": sha_pdf, "fichas": fichas},
                                  ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"fichas": len(fichas), "criterios": len(filas), "respuestas": sum(len(f["ids_opacos"]) for f in fichas),
                      "citas_no_ubicadas": sum(u == "no ubicada en el PDF" for c in control for u in c)}, ensure_ascii=False))


if __name__ == "__main__":
    sys.dont_write_bytecode = True
    main()
