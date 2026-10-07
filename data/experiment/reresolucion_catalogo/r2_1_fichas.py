"""U-RERESOL-CAT, R2-1 — fichas de la lectura de la parte B de la enmienda 6 (§B.2), para la adjudicación de la autora.

Junta las 30 fichas que sortea r2_1_medicion.py (semilla declarada) con la lectura asistida (un JSON con el veredicto,
el sujeto según el texto y el fundamento de cada ficha) y escribe un Markdown con el texto completo de la unidad, su
texto heredado, el rol de alcance y la lectura; al final, el recuento y el límite inferior de Wilson al 95 % de las
correctas, también en los dos extremos de las dudosas (todas incorrectas, todas correctas). USD 0.

Uso: r2_1_fichas.py --fichas F.json --lectura L.json --out FICHAS.md
"""
from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from pathlib import Path

PISO = 0.75
Z = 1.959963984540054


def wilson_inferior(k: int, n: int) -> float:
    if n == 0:
        return 0.0
    p = k / n
    centro = p + Z * Z / (2 * n)
    margen = Z * math.sqrt(p * (1 - p) / n + Z * Z / (4 * n * n))
    return (centro - margen) / (1 + Z * Z / n)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--fichas", type=Path, required=True)
    ap.add_argument("--lectura", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    fx = json.loads(a.fichas.read_text(encoding="utf-8"))
    lec = json.loads(a.lectura.read_text(encoding="utf-8"))
    fichas, lecturas = fx["fichas"], lec["lecturas"]
    faltan = [f["ficha"] for f in fichas if f["ficha"] not in lecturas]
    if faltan:
        raise SystemExit(f"fichas sin lectura: {faltan}")
    n = len(fichas)
    c = Counter(lecturas[f["ficha"]]["veredicto"] for f in fichas)
    correctas, dudosas = c.get("correcta", 0), c.get("dudosa", 0)
    nv = [f for f in fichas if f["categoria"] != "sin_aplica_a"]
    L = ["# Lectura de la parte B de la enmienda 6 a L-ESQ-R2 — fichas para la adjudicación de la autora", "",
         f"Muestra de {n} normas de la población de la parte B (KG-Tanda0-Diez-r2b), sorteada con la semilla "
         f"{fx['semilla']} antes de leer (r2_1_medicion.py). Lectura asistida y declarada; la adjudicación es de la autora.",
         "", f"**Criterio.** {lec['criterio']}", "",
         "## Recuento de la lectura (antes de la adjudicación)", "",
         "| veredicto | fichas |", "|---|---|"]
    L += [f"| {v} | {c.get(v, 0)} |" for v in ("correcta", "incorrecta", "dudosa")]
    L += ["", f"- Límite inferior de Wilson al 95 % con las correctas de la lectura: {correctas} de {n}, "
              f"{wilson_inferior(correctas, n):.3f} (piso {PISO}).",
          f"- Si todas las dudosas se adjudicaran correctas: {correctas + dudosas} de {n}, "
          f"{wilson_inferior(correctas + dudosas, n):.3f}.",
          f"- El piso de 28 de 30 da {wilson_inferior(28, 30):.3f}; 27 de 30 da {wilson_inferior(27, 30):.3f}.",
          f"- De las leídas, {len(nv)} vienen de una relación con una mención que no verifica: "
          + ", ".join(f"{f['ficha']} {lecturas[f['ficha']]['veredicto']}" for f in nv) + ".", "",
          "| ficha | TO | unidad | tipo | categoría | cola | veredicto | sujeto según el texto |", "|---|---|---|---|---|---|---|---|"]
    L += [f"| {f['ficha']} | {f['to']} | `{f['chunk_id']}` | {f['tipo']} | {f['categoria']} | {'sí' if f['cola_humana'] else 'no'} "
          f"| {lecturas[f['ficha']]['veredicto']} | {lecturas[f['ficha']]['sujeto_segun_el_texto']} |" for f in fichas]
    L += ["", "## Fichas", ""]
    for f in fichas:
        x = lecturas[f["ficha"]]
        L += [f"### {f['ficha']} — {f['to']}, `{f['chunk_id']}` (punto {f['punto']}), {f['tipo']}", "",
              f"- **Norma:** {f['label']}", f"- **Descripción:** {f['descripcion']}", f"- **Tramo:** {f['tramo']}",
              f"- **Rol de alcance del documento:** `{f['rol_de_alcance']}` — {f['rol_de_alcance_label']} "
              f"(miembros: {', '.join(f['rol_de_alcance_miembros'] or [])})",
              f"- **Categoría:** {f['categoria']}; cola humana: {'sí' if f['cola_humana'] else 'no'}; "
              f"índice en la población: {f['indice_en_la_poblacion']}",
              "- **Relaciones aplica_a que emitió el modelo:** " + ("ninguna" if not f["aplica_a"] else "; ".join(
                  f"mención «{r['mencion']}» ({r['mencion_verificada']}), sugerencia {r['sujeto_id_modelo']}, "
                  f"resuelta a {r['resuelto_a']} ({r['metodo']})" for r in f["aplica_a"])), "",
              "**Texto heredado.**", ""]
        L += [f"> [{h['unidad_origen']}, {h['tipo']}] " + (h["texto"] or "").replace("\n", " ") for h in f["texto_heredado"]] \
            or ["> (sin texto heredado)"]
        L += ["", "**Texto de la unidad.**", "", "```", (f["texto_de_la_unidad"] or "").rstrip(), "```", "",
              f"**Lectura: {x['veredicto'].upper()}.** Sujeto según el texto: {x['sujeto_segun_el_texto']}. {x['fundamento']}",
              "", "**Adjudicación de la autora:** PENDIENTE", ""]
    a.out.write_text("\n".join(L), encoding="utf-8")
    print(json.dumps({"n": n, "por_veredicto": dict(c), "wilson_correctas": round(wilson_inferior(correctas, n), 3),
                      "wilson_si_dudosas_correctas": round(wilson_inferior(correctas + dudosas, n), 3),
                      "con_mencion_que_no_verifica": {f["ficha"]: lecturas[f["ficha"]]["veredicto"] for f in nv}},
                     ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
