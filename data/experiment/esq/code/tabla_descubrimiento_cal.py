"""
tabla_descubrimiento_cal.py — Entrega para ADJUDICACIÓN (U-ESQ-2-cal.d), sin
adjudicar: genera control/tabla_adjudicacion_descubrimiento_cal.md con una
fila/sección por unidad (las 20), el output VERBATIM del descubrimiento de
esa unidad y, para las dopadas, el concepto plantado esperado al lado
(parseado mecánicamente de manifiesto_dopadas_p1bis.md).

RECOMPUTO INDEPENDIENTE: este script NO lee resumen_descubrimiento_cal.json —
recomputa todo desde el jsonl persistido (fuente primaria) y reporta:
  - conteo mecánico preliminar SOLO de lo inequívoco (unidades con cero
    hallazgos reportados), por brazo y por mitad;
  - contenedores no-lista y unidades con error.
NO computa el veredicto contra P-cal: la adjudicación fila por fila es de la
autora con la regla sellada del pre-registro §4 (vale si identifica la
materia de la cláusula; duda NO cuenta; cruces aparte; en C es espuria la
detección de contenido que el esquema sí captura).

Uso:  .venv/bin/python3 -B data/experiment/esq/code/tabla_descubrimiento_cal.py
"""

from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_control_esq as cc             # noqa: E402
import runner_control_esq as rc            # noqa: E402
import runner_control_esq_p1bis as rp      # noqa: E402
import runner_descubrimiento_cal as rd     # noqa: E402

SALIDA = cc.CONTROL_DIR / "tabla_adjudicacion_descubrimiento_cal.md"


def modelos_resueltos_db() -> dict[str, int]:
    """Modelo RESUELTO por llamada, leído de raw_json en la .db propia (la
    db registra el snapshot que la API resolvió, no el alias). Mandato de la
    revisión del freno (a): el reporte de (d) lo declara explícito; si P-cal
    pasa, el censo modo (ii) queda comprometido a correr con ese mismo
    snapshot resuelto."""
    import sqlite3
    if not rd.DB_DESC.exists():
        return {}
    conn = sqlite3.connect(str(rd.DB_DESC))
    filas = conn.execute("SELECT raw_json FROM cache").fetchall()
    conn.close()
    out: dict[str, int] = {}
    for (raw,) in filas:
        m = json.loads(raw).get("model") or "¿sin model en raw_json?"
        out[m] = out.get(m, 0) + 1
    return out


def porque_de_manifiesto() -> dict[str, str]:
    """chunk_id_dopado → 'Por qué está fuera del esquema' del manifiesto de
    dopadas (contexto para la adjudicación, mismo parseo mecánico)."""
    import re
    txt = (cc.CONTROL_DIR / "manifiesto_dopadas_p1bis.md").read_text(
        encoding="utf-8")
    out, actual = {}, None
    for linea in txt.split("\n"):
        m = re.match(r"^### (dop::\S+)\s*$", linea)
        if m:
            actual = m.group(1)
            continue
        m = re.match(r"^- \*\*Por qué está fuera del esquema:\*\* (.+)$", linea)
        if m and actual:
            out[actual] = m.group(1).strip()
    return out


def main() -> int:
    fx = rp.cargar_fixtures()
    seleccion = rp.seleccion_p1bis(fx)
    regs = rc.cargar_jsonl_last_wins(cc.CONTROL_DIR / rd.JSONL_DESC)
    conceptos = rd.conceptos_del_manifiesto()
    porques = porque_de_manifiesto()
    conteo = rd.conteo_mecanico(seleccion, regs)

    n_cero = conteo["n_cero_hallazgos"]
    n_con = conteo["n_con_hallazgos"]
    ap = "A'"
    modelos = modelos_resueltos_db()
    filas_modelo = ([f"| `{m}` | {n} |" for m, n in sorted(modelos.items())]
                    or ["| (db sin filas) | 0 |"])
    cero_tipo = [c for c in conteo["cero_hallazgos"]["A'"]
                 if conteo["detalle_por_unidad"][c]["mitad"] == "tipo"]
    cero_pred = [c for c in conteo["cero_hallazgos"]["A'"]
                 if conteo["detalle_por_unidad"][c]["mitad"] == "predicado"]

    L: list[str] = []
    L += [
        "# Tabla de adjudicación — calibración del descubrimiento (U-ESQ-2-cal.d)",
        "",
        f"Generada {datetime.now().isoformat(timespec='seconds')} desde "
        f"`control/{rd.JSONL_DESC}` (fuente primaria; recomputo independiente "
        "del resumen).",
        "",
        "**La adjudicación es de la autora**, fila por fila, con la regla "
        "sellada del pre-registro §4: una detección VALE si el reporte "
        "identifica la materia de la cláusula plantada (no un nombre de tipo "
        "ni una cadena exacta); ante la duda NO cuenta; los cruces "
        "(dopada de tipo detectada como problema de relación o viceversa) se "
        "reportan aparte y no cuentan para su mitad; en C es espuria toda "
        "detección de contenido que el esquema sí captura. Este documento NO "
        "computa el veredicto contra P-cal.",
        "",
        "## Resumen mecánico preliminar (solo lo inequívoco)",
        "",
        "| medida | valor |",
        "|---|---|",
        f"| A′ con CERO hallazgos (sin detección posible) | {n_cero[ap]}/10 |",
        f"| — mitad tipo con cero hallazgos | {len(cero_tipo)}/5 |",
        f"| — mitad predicado con cero hallazgos | {len(cero_pred)}/5 |",
        f"| A′ con ≥1 hallazgo (a adjudicar) | {n_con[ap]}/10 |",
        f"| C con CERO hallazgos | {conteo['n_cero_hallazgos']['C']}/10 |",
        f"| C con ≥1 hallazgo (a adjudicar como espurias o no) | "
        f"{conteo['n_con_hallazgos']['C']}/10 |",
        f"| contenedores no-lista | {conteo['contenedores_no_lista'] or '—'} |",
        f"| unidades con error / sin registro | {conteo['con_error'] or '—'} |",
        "",
        "## Modelo resuelto (db, por llamada pagada)",
        "",
        "El alias del contrato es `claude-haiku-4-5`; la db registra el "
        "modelo RESUELTO que la API devolvió en cada llamada:",
        "",
        "| modelo resuelto | llamadas (misses en db) |",
        "|---|--:|",
        *filas_modelo,
        "",
        "Compromiso sellado en la revisión del freno (a): si P-cal pasa, el "
        "censo modo (ii) corre con ese MISMO snapshot resuelto — calibración "
        "y censo con el mismo modelo, sin excepción.",
        "",
        "## Índice",
        "",
        "| # | unidad | brazo | mitad | n hallazgos | error |",
        "|--:|---|---|---|--:|---|",
    ]
    for i, s in enumerate(seleccion, 1):
        d = conteo["detalle_por_unidad"][s["chunk_id"]]
        L.append(f"| {i} | `{s['chunk_id']}` | {s['brazo']} | "
                 f"{d['mitad'] or '—'} | "
                 f"{'—' if d['n_hallazgos'] is None else d['n_hallazgos']} | "
                 f"{d['error'] or '—'} |")
    L.append("")
    L.append("## Filas (output verbatim + esperado al lado)")
    L.append("")

    for i, s in enumerate(seleccion, 1):
        cid = s["chunk_id"]
        reg = regs.get(cid) or {}
        L.append(f"### {i}. `{cid}` — brazo {s['brazo']}"
                 + (f", mitad {s['mitad']}" if s.get("mitad") else ""))
        L.append("")
        if s["brazo"] == "A'":
            L.append(f"- **Concepto plantado esperado:** {conceptos.get(cid, '¿?')}")
            if cid in porques:
                L.append(f"- **Por qué está fuera del esquema (manifiesto):** "
                         f"{porques[cid]}")
            L.append(f"- **Cláusula plantada (manifiesto):** ver "
                     f"`manifiesto_dopadas_p1bis.md` § {cid}")
        else:
            L.append("- **Esperado (brazo C, unidad limpia):** cero "
                     "detecciones; toda detección de contenido que el "
                     "esquema sí captura es espuria")
        if reg.get("error"):
            L.append(f"- **ERROR:** `{reg['error']}`")
        L.append("")
        L.append("**Output verbatim del descubrimiento** "
                 "(`tool_input_crudo`):")
        L.append("")
        L.append("~~~json")
        L.append(json.dumps(reg.get("tool_input_crudo"), ensure_ascii=False,
                            indent=2))
        L.append("~~~")
        L.append("")

    SALIDA.write_text("\n".join(L), encoding="utf-8")
    print(f"tabla -> {SALIDA}")
    print(f"cero hallazgos: A' {n_cero[ap]}/10 "
          f"(tipo {len(cero_tipo)}/5, predicado {len(cero_pred)}/5) | "
          f"C {n_cero['C']}/10 — mecánico, sin veredicto")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
