"""
conversor_criterios.py — Convierte la tabla de criterios redactada por la
autora (id | criterio | cita_textual) a calibracion/criterios_u6.json con el
esquema fijo del driver, y verifica CADA cita textual verbatim contra el PDF
del TO correspondiente.

Entrada aceptada: archivo con tabla markdown (| id | criterio | cita_textual |)
o TSV (id<TAB>criterio<TAB>cita_textual), una fila por criterio, varias filas
por pregunta.

Verificación de citas: el texto del PDF se extrae con pdfplumber y ambos lados
se normalizan SOLO por espacios en blanco (NFC + colapso de whitespace); no se
altera mayúsculas, tildes ni puntuación. Una cita que no aparece verbatim se
REPORTA — jamás se corrige acá: la corrección es de la autora.

Uso:
  .venv/bin/python data/experiment/ev2_juez/conversor_criterios.py \
      --tabla <archivo .md o .tsv> \
      [--out data/experiment/ev2_juez/calibracion/criterios_u6.json]
"""

from __future__ import annotations

import argparse
import json
import unicodedata
from pathlib import Path

JUEZ_DIR = Path(__file__).resolve().parent
EXP_DIR = JUEZ_DIR.parent
PREGUNTAS_PATH = EXP_DIR / "exploracion" / "generacion" / "preguntas_u6.json"
SUBSET_DIR = EXP_DIR / "subset"

PDF_POR_TO = {
    "ext": "TO_exterior_cambios_actual.pdf",
    "cap": "TO_capitales_minimos_actual.pdf",
    "cla": "TO_clasificacion_deudores_actual.pdf",
    "ric": "TO_regimen_informativo_contable_mensual_actual.pdf",
    "pro": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
}


def normalizar(s: str) -> str:
    """NFC + colapso de todo whitespace a un espacio. Nada más se toca."""
    return " ".join(unicodedata.normalize("NFC", s).split())


def parsear_tabla(path: Path) -> list[dict]:
    """Filas {id, criterio, cita_textual} desde markdown o TSV."""
    filas = []
    for ln in path.read_text(encoding="utf-8").splitlines():
        ln = ln.strip()
        if not ln or ln.lower().startswith(("id\t", "| id", "|--", "|:-", "| :-")):
            continue
        if ln.startswith("|"):
            celdas = [c.strip() for c in ln.strip("|").split("|")]
        elif "\t" in ln:
            celdas = [c.strip() for c in ln.split("\t")]
        else:
            continue
        if len(celdas) != 3:
            raise ValueError(f"fila con {len(celdas)} columnas (esperadas 3): {ln[:80]!r}")
        if celdas[0].lower() == "id":
            continue
        filas.append({"id": celdas[0], "criterio": celdas[1], "cita_textual": celdas[2]})
    if not filas:
        raise ValueError("tabla vacía o formato no reconocido")
    return filas


def extraer_texto_pdf(pdf_path: Path) -> str:
    import pdfplumber
    partes = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            partes.append(page.extract_text() or "")
    return normalizar("\n".join(partes))


def main() -> int:
    ap = argparse.ArgumentParser(description="Tabla de criterios → criterios_u6.json + verificación de citas")
    ap.add_argument("--tabla", required=True, type=Path)
    ap.add_argument("--out", type=Path, default=JUEZ_DIR / "calibracion" / "criterios_u6.json")
    args = ap.parse_args()

    preguntas = {x["id"]: x for x in json.loads(PREGUNTAS_PATH.read_text(encoding="utf-8"))}
    filas = parsear_tabla(args.tabla)

    desconocidos = sorted({f["id"] for f in filas} - set(preguntas))
    if desconocidos:
        raise ValueError(f"ids fuera de preguntas_u6.json: {desconocidos}")

    # agrupar preservando el orden de la tabla dentro de cada pregunta
    por_id: dict[str, list[dict]] = {}
    for f in filas:
        por_id.setdefault(f["id"], []).append(
            {"criterio": f["criterio"], "cita_textual": f["cita_textual"]})

    faltantes = sorted(set(preguntas) - set(por_id))
    salida = [{"id_pregunta": q, "criterios": por_id[q]} for q in sorted(por_id)]

    # --- verificación verbatim de citas contra el PDF del TO de cada pregunta ---
    textos_pdf = {}
    resultados, ok = [], 0
    for q in sorted(por_id):
        to = preguntas[q]["to"]
        if to not in textos_pdf:
            textos_pdf[to] = extraer_texto_pdf(SUBSET_DIR / PDF_POR_TO[to])
        for j, c in enumerate(por_id[q], start=1):
            hallada = normalizar(c["cita_textual"]) in textos_pdf[to]
            ok += hallada
            resultados.append({"id_pregunta": q, "indice": j, "to": to,
                               "verifica": hallada,
                               "cita": c["cita_textual"][:120]})
    total = len(resultados)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(salida, ensure_ascii=False, indent=2), encoding="utf-8")
    reporte = args.out.parent / "reporte_verificacion_citas.json"
    reporte.write_text(json.dumps({
        "total_criterios": total, "citas_verificadas": ok,
        "preguntas_con_criterios": len(por_id),
        "preguntas_sin_criterios": faltantes,
        "no_verifican": [r for r in resultados if not r["verifica"]],
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"criterios: {total} sobre {len(por_id)} preguntas → {args.out}")
    print(f"citas verificadas verbatim: {ok}/{total}")
    if faltantes:
        print(f"ATENCIÓN — preguntas sin criterios: {faltantes}")
    if ok < total:
        print("CITAS QUE NO VERIFICAN (se reportan, NO se corrigen acá):")
        for r in resultados:
            if not r["verifica"]:
                print(f"  {r['id_pregunta']} criterio {r['indice']}: {r['cita']!r}…")
    print(f"reporte → {reporte}")
    return 0 if (ok == total and not faltantes) else 1


if __name__ == "__main__":
    raise SystemExit(main())
