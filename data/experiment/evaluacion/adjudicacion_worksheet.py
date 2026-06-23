"""
adjudicacion_worksheet.py — Worksheet de adjudicación humana (Fase 2.3).

Reorganiza la cola `adjudicacion_pendiente.json` (90 entradas por repetición) en un
worksheet para adjudicar contra los PDFs, SIN tocar el dataset congelado.

Reglas (firmadas por la autora):
  · PROPAGACIÓN SOLO POR IDENTIDAD ESTRICTA: dos afirmaciones se agrupan (un
    veredicto → muchas celdas) únicamente si su texto es IDÉNTICO tras
    normalización COSMÉTICA — exactamente la regla congelada de citas
    (harness._norm_loc: unifica comillas, colapsa whitespace, quita punto/espacio
    final). NO se hace lowercasing ni equivalencia laxa: "31" y "30" jamás se
    agrupan; "hasta 31 días" y "31 días" son textos distintos → filas separadas.
  · Las casi-idénticas quedan ADYACENTES (las afirmaciones de cada pregunta se
    ordenan por texto normalizado) pero se adjudican por SEPARADO.
  · DOBLE AGRUPACIÓN: por TO fuente primero (un PDF abierto por vez), por
    pregunta→afirmación adentro.
  · LOG DE PROPAGACIÓN: cada afirmación lista las celdas (grafo×pregunta×rep) a las
    que su veredicto se propaga → trazabilidad veredicto→celdas auditable.
  · Agrupación por (qid, afirmación normalizada): la propagación es dentro de la
    misma pregunta, a través de grafos y reps (que es donde recurren).

Salidas: adjudicacion_worksheet.json (para llenar veredicto/evidencia) +
adjudicacion_worksheet.md (legible). Reporta cuántas afirmaciones únicas quedan.
"""

from __future__ import annotations

import json
from collections import defaultdict, OrderedDict

from loader import EVAL_DIR
from harness import _norm_loc   # MISMA regla congelada de citas (cosmética)

ADJ_QUEUE = EVAL_DIR / "adjudicacion_pendiente.json"
EVAL_SET = EVAL_DIR / "queries" / "eval_set_v1.json"
OUT_JSON = EVAL_DIR / "adjudicacion_worksheet.json"
OUT_MD = EVAL_DIR / "adjudicacion_worksheet.md"


def _cita_key(c):
    return (c.get("source_doc"), _norm_loc(c.get("location") or ""))


def main():
    queue = json.load(open(ADJ_QUEUE, encoding="utf-8"))
    pooljson = json.load(open(EVAL_SET, encoding="utf-8"))
    pool = {q["id"]: q for q in pooljson["preguntas"]}
    corpus = pooljson.get("metadata", {}).get("corpus", {})  # key -> nombre PDF

    # 1. Explotar entradas en registros de afirmación (una por claim por celda).
    # Agrupar por (qid, norm_claim). Cada grupo = una afirmación única a adjudicar.
    grupos = defaultdict(lambda: {"surface": OrderedDict(), "celdas": [],
                                  "citas": OrderedDict(), "qid": None})
    total_instancias = 0
    for e in queue:
        run, qid, rep = e["run"], e["qid"], e["rep"]
        for claim in e.get("afirmaciones_centrales_no_soportadas", []):
            total_instancias += 1
            nk = _norm_loc(claim)          # normalización cosmética estricta
            g = grupos[(qid, nk)]
            g["qid"] = qid
            g["surface"][claim] = True     # formas superficiales (cosmética distinta)
            g["celdas"].append([run, qid, rep])
            for c in (e.get("citas_agente") or []):
                g["citas"][_cita_key(c)] = c

    # 2. Organizar por TO fuente -> pregunta -> afirmaciones (ordenadas por texto).
    #    Sección = tupla ordenada de tos_fuente de la pregunta (single-TO primero).
    secciones = defaultdict(lambda: defaultdict(list))  # tos_tuple -> qid -> [afirm]
    for (qid, nk), g in grupos.items():
        tos = tuple(sorted(pool[qid].get("tos_fuente") or ["(sin_to)"]))
        surfaces = list(g["surface"].keys())
        afirm = {
            "afirmacion": surfaces[0],
            "variantes_cosmeticas": surfaces[1:],   # mismo norm, distinta cosmética
            "citas_agente": list(g["citas"].values()),
            "celdas": g["celdas"],                  # LOG DE PROPAGACIÓN
            "n_celdas": len(g["celdas"]),
            "veredicto": None,                      # "verdadera" | "falsa"
            "evidencia_seccion_pdf": None,
        }
        secciones[tos][qid].append((nk, afirm))

    # ordenar: secciones single-TO primero; dentro, qid en orden del eval_set;
    # dentro de cada qid, afirmaciones por texto normalizado (adyacencia).
    qorder = {q["id"]: i for i, q in enumerate(pooljson["preguntas"])}
    sec_keys = sorted(secciones, key=lambda t: (len(t), t))

    worksheet = {"meta": {}, "secciones": []}
    n_unicas = 0
    for tos in sec_keys:
        pdfs = [corpus.get(k, k) for k in tos]
        sec = {"tos_fuente": list(tos), "pdf": pdfs, "preguntas": []}
        for qid in sorted(secciones[tos], key=lambda q: qorder.get(q, 999)):
            afs = [a for _, a in sorted(secciones[tos][qid], key=lambda x: x[0])]
            n_unicas += len(afs)
            q = pool[qid]
            sec["preguntas"].append({
                "qid": qid,
                "pregunta": q["pregunta"],
                "categoria": q.get("categoria"),
                "ground_truth_secciones": q.get("ground_truth_secciones"),
                "cita_textual": q.get("cita_textual"),
                "afirmaciones": afs,
            })
        worksheet["secciones"].append(sec)

    worksheet["meta"] = {
        "entradas_cola": len(queue),
        "instancias_de_afirmacion": total_instancias,
        "afirmaciones_unicas_tras_agrupado": n_unicas,
        "regla_agrupacion": "identidad estricta post-normalizacion cosmetica "
                            "(harness._norm_loc); sin lowercase; por (qid, afirmacion)",
        "celdas_propagacion_total": sum(a["n_celdas"]
                                        for s in worksheet["secciones"]
                                        for qq in s["preguntas"]
                                        for a in qq["afirmaciones"]),
    }
    json.dump(worksheet, open(OUT_JSON, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    _write_md(worksheet)
    m = worksheet["meta"]
    print(f"entradas de cola: {m['entradas_cola']}")
    print(f"instancias de afirmación (explotadas): {m['instancias_de_afirmacion']}")
    print(f"AFIRMACIONES ÚNICAS tras agrupado estricto: {m['afirmaciones_unicas_tras_agrupado']}")
    print(f"celdas de propagación cubiertas: {m['celdas_propagacion_total']}")
    print(f"Worksheet: {OUT_JSON}  +  {OUT_MD}")


def _write_md(ws):
    m = ws["meta"]
    L = ["# Worksheet de adjudicación humana — corrida congelada Fase 2.3", ""]
    L.append(f"- Entradas de cola (por repetición): **{m['entradas_cola']}**")
    L.append(f"- Instancias de afirmación: {m['instancias_de_afirmacion']}")
    L.append(f"- **Afirmaciones únicas tras agrupado estricto: {m['afirmaciones_unicas_tras_agrupado']}**")
    L.append(f"- Celdas de propagación cubiertas: {m['celdas_propagacion_total']}")
    L.append("")
    L.append("Regla: agrupación por **identidad estricta** (misma regla cosmética de "
             "citas, sin lowercase). Variantes casi-idénticas quedan ADYACENTES pero "
             "se adjudican por separado. Llená `veredicto` (verdadera/falsa) y "
             "`evidencia` (sección del PDF) por afirmación; el veredicto se propaga a "
             "todas las celdas listadas.")
    L.append("")
    for sec in ws["secciones"]:
        L.append(f"## TO fuente: {', '.join(sec['pdf'])}")
        L.append("")
        for qq in sec["preguntas"]:
            L.append(f"### {qq['qid']} ({qq['categoria']}) — {qq['pregunta']}")
            if qq.get("ground_truth_secciones"):
                L.append(f"*GT secciones:* {qq['ground_truth_secciones']}")
            if qq.get("cita_textual"):
                L.append(f"*Cita textual del gold:* {qq['cita_textual'][:300]}")
            L.append("")
            for i, a in enumerate(qq["afirmaciones"], 1):
                L.append(f"**[{qq['qid']}·{i}]** «{a['afirmacion']}»")
                if a["variantes_cosmeticas"]:
                    L.append(f"  · variantes cosméticas (mismo veredicto): {a['variantes_cosmeticas']}")
                L.append(f"  · citas del agente: {json.dumps(a['citas_agente'], ensure_ascii=False)}")
                L.append(f"  · propaga a {a['n_celdas']} celdas: "
                         f"{[f'{r}/{q}/r{rep}' for r,q,rep in a['celdas']]}")
                L.append(f"  · **veredicto:** ___ (verdadera/falsa)   **evidencia:** ___ (sección PDF)")
                L.append("")
    OUT_MD.write_text("\n".join(L), encoding="utf-8")


if __name__ == "__main__":
    main()
