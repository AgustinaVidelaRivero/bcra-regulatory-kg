"""
verificar_citas.py — Verificación INDEPENDIENTE de cada cita_textual del
archivo sellado de criterios (data/experiment/exploracion/u6_fidelidad/
criterios_u6.json, commit 2ac2fab) contra el PDF del TO correspondiente, con
extractor propio (pdfplumber). No reutiliza el verificador del commit.

Normalización, idéntica en ambos lados y declarada: NFC + colapso de todo
whitespace (incluidos saltos de línea) a un espacio. NO se altera mayúsculas,
tildes, puntuación ni guiones. Se prueba en dos niveles, del más estricto al
más laxo, y se reporta en cuál verificó cada cita:
  N1: whitespace colapsado (texto de página con extract_text)
  N2: N1 + eliminación de guiones de corte de línea ("- " → "") — solo para
      diagnosticar citas que crucen un salto de línea con palabra partida.
Una cita que no verifica en ningún nivel se REPORTA con detalle (mejor prefijo
coincidente) y el script devuelve exit 1. Jamás corrige nada.

Uso:  .venv/bin/python data/experiment/ev2_juez/verificar_citas.py
"""

from __future__ import annotations

import json
import unicodedata
from pathlib import Path

JUEZ_DIR = Path(__file__).resolve().parent
EXP_DIR = JUEZ_DIR.parent
CRITERIOS_PATH = EXP_DIR / "exploracion" / "u6_fidelidad" / "criterios_u6.json"
SUBSET_DIR = EXP_DIR / "subset"
PDF_POR_TO = {
    "ext": "TO_exterior_cambios_actual.pdf",
    "cap": "TO_capitales_minimos_actual.pdf",
    "cla": "TO_clasificacion_deudores_actual.pdf",
    "ric": "TO_regimen_informativo_contable_mensual_actual.pdf",
    "pro": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
}


def n1(s: str) -> str:
    return " ".join(unicodedata.normalize("NFC", s).split())


def n2(s: str) -> str:
    return n1(s).replace("- ", "")


def texto_pdf(to: str) -> str:
    import pdfplumber
    partes = []
    with pdfplumber.open(SUBSET_DIR / PDF_POR_TO[to]) as pdf:
        for page in pdf.pages:
            partes.append(page.extract_text() or "")
    return "\n".join(partes)


def mejor_prefijo(cita: str, texto: str) -> int:
    """Largo del prefijo más largo de la cita (normalizada N1) presente en el texto."""
    lo, hi = 0, len(cita)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if cita[:mid] in texto:
            lo = mid
        else:
            hi = mid - 1
    return lo


def main() -> int:
    data = json.loads(CRITERIOS_PATH.read_text(encoding="utf-8"))
    textos = {}
    filas = []
    for p in data["preguntas"]:
        to = p["to"]
        if to not in textos:
            crudo = texto_pdf(to)
            textos[to] = (n1(crudo), n2(crudo))
        t1, t2 = textos[to]
        for j, c in enumerate(p["gold"]["criterios"], start=1):
            cita = c["cita_textual"]
            nivel = None
            if n1(cita) in t1:
                nivel = "N1"
            elif n2(cita) in t2:
                nivel = "N2"
            filas.append({"id": p["id"], "indice": j, "to": to, "nivel": nivel,
                          "chars": len(cita),
                          "prefijo_ok": None if nivel else mejor_prefijo(n1(cita), t1),
                          "cita": cita})

    total = len(filas)
    ok1 = sum(1 for f in filas if f["nivel"] == "N1")
    ok2 = sum(1 for f in filas if f["nivel"] == "N2")
    fallan = [f for f in filas if f["nivel"] is None]
    print(f"citas: {total} | verifican N1 (whitespace): {ok1} | solo N2 (guiones de corte): {ok2} "
          f"| NO verifican: {len(fallan)}")
    print("por pregunta (N1/total):")
    por_q = {}
    for f in filas:
        a, b = por_q.get(f["id"], (0, 0))
        por_q[f["id"]] = (a + (f["nivel"] == "N1"), b + 1)
    print("  " + "  ".join(f"{q}:{a}/{b}" for q, (a, b) in sorted(por_q.items())))
    if ok2:
        print("citas que solo verifican en N2:")
        for f in filas:
            if f["nivel"] == "N2":
                print(f"  {f['id']} c{f['indice']} ({f['chars']} chars)")
    if fallan:
        print("CITAS QUE NO VERIFICAN (detalle; no se corrigen):")
        for f in fallan:
            c = n1(f["cita"])
            k = f["prefijo_ok"]
            print(f"  {f['id']} c{f['indice']} [{f['to']}] {f['chars']} chars — "
                  f"prefijo coincidente {k}/{len(c)} chars")
            print(f"     cita : {c[:200]!r}")
            print(f"     corte: …{c[max(0, k-40):k]!r} ▶ {c[k:k+60]!r}")

    salida = JUEZ_DIR / "selftest_out" / "verificacion_citas_u6.json"
    salida.parent.mkdir(exist_ok=True)
    salida.write_text(json.dumps({"total": total, "n1": ok1, "n2": ok2,
                                  "no_verifican": fallan, "detalle": filas},
                                 ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"→ {salida}")
    return 0 if not fallan else 1


if __name__ == "__main__":
    raise SystemExit(main())
