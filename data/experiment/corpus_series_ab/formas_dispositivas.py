#!/usr/bin/env python3
"""Tasa de formas dispositivas en las comunicaciones «A» y «B» del corpus.

Artefacto de respaldo de la afirmación de docs/tesis/main.tex §3.1 (fila 146
de docs/tesis/mapa_fuentes_cap_esquema.md): «se cuentan tres formas
dispositivas, "se establece", "deberán" y "no podrán"; alguna de las tres
aparece en el 63 % de las 1.666 comunicaciones "A" y en el 9 % de las 1.301 de
la serie "B"».

Criterio (fijado por el mandato de la unidad, no por este script):
  - Universo: filas de data/raw/manifiesto.csv cuyo `archivo_local` cae bajo
    02_comunicaciones_A/ (serie A) o 03_comunicaciones_B/ (serie B).
  - Texto: no existe en el repo un caché de texto extraído de esas
    comunicaciones, así que se extrae con `pdftotext` (poppler) en memoria;
    no se persiste ningún texto.
  - Formas: exactamente «se establece», «deberán» y «no podrán», buscadas
    como cadenas literales (subcadena) sobre texto normalizado: NFKD sin
    marcas diacríticas, minúsculas, corridas de espacio en blanco (incluidos
    saltos de línea) colapsadas a un espacio. Sin variantes morfológicas; los
    cortes de palabra con guion al final de línea no se recomponen.
  - Una comunicación cuenta si contiene al menos una de las tres.

Uso (desde la raíz del repo, sin API, sin dependencias fuera de la stdlib):
    python3 data/experiment/corpus_series_ab/formas_dispositivas.py

Escribe únicamente data/experiment/corpus_series_ab/reporte_formas_dispositivas.md
e imprime un resumen por stdout.
"""

from __future__ import annotations

import csv
import datetime as dt
import os
import re
import subprocess
import sys
import unicodedata
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

AQUI = Path(__file__).resolve()
RAIZ = AQUI.parents[3]  # corpus_series_ab -> experiment -> data -> raíz
MANIFIESTO = RAIZ / "data" / "raw" / "manifiesto.csv"
REPORTE = AQUI.parent / "reporte_formas_dispositivas.md"

SERIES = (
    ("A", "02_comunicaciones_A/"),
    ("B", "03_comunicaciones_B/"),
)
FORMAS = ("se establece", "deberán", "no podrán")
# Valor que afirma la prosa (docs/tesis/main.tex §3.1), por serie, en %.
PROSA = {"A": 63.0, "B": 9.0}


def normalizar(texto: str) -> str:
    """NFKD sin diacríticos, minúsculas, espacio en blanco colapsado."""
    sin_marcas = "".join(
        c for c in unicodedata.normalize("NFKD", texto)
        if not unicodedata.combining(c)
    )
    return re.sub(r"\s+", " ", sin_marcas.lower())


FORMAS_NORM = tuple(normalizar(f) for f in FORMAS)


def extraer_texto(pdf: Path) -> tuple[str, str | None]:
    """Devuelve (texto, error). error es None si pdftotext terminó bien."""
    try:
        proc = subprocess.run(
            ["pdftotext", "-enc", "UTF-8", str(pdf), "-"],
            capture_output=True, check=False,
        )
    except FileNotFoundError:
        return "", "pdftotext no está instalado"
    texto = proc.stdout.decode("utf-8", errors="replace")
    if proc.returncode != 0:
        err = proc.stderr.decode("utf-8", errors="replace").strip()
        return texto, f"rc={proc.returncode}: {err[:200]}"
    return texto, None


def analizar(pdf: Path) -> dict:
    texto, error = extraer_texto(pdf)
    norm = normalizar(texto)
    presentes = [f for f, fn in zip(FORMAS, FORMAS_NORM) if fn in norm]
    # Sensibilidad (solo informativa): mismas cadenas con límite de palabra.
    palabra = [
        f for f, fn in zip(FORMAS, FORMAS_NORM)
        if re.search(r"(?<![a-z0-9])" + re.escape(fn) + r"(?![a-z0-9])", norm)
    ]
    return {
        "archivo": str(pdf.relative_to(RAIZ)),
        "error": error,
        "chars": len(norm.strip()),
        "formas": presentes,
        "formas_palabra": palabra,
    }


def leer_universo() -> dict[str, list[Path]]:
    universo: dict[str, list[Path]] = {s: [] for s, _ in SERIES}
    with MANIFIESTO.open(newline="", encoding="utf-8") as fh:
        for fila in csv.DictReader(fh):
            ruta = fila["archivo_local"]
            for serie, prefijo in SERIES:
                if prefijo in ruta:
                    universo[serie].append(RAIZ / ruta)
                    break
    return universo


def git(*args: str) -> str:
    try:
        return subprocess.run(
            ["git", "-C", str(RAIZ), *args], capture_output=True, text=True,
            check=True,
        ).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "NO DISPONIBLE"


def version_pdftotext() -> str:
    try:
        proc = subprocess.run(["pdftotext", "-v"], capture_output=True, text=True)
    except FileNotFoundError:
        return "NO DISPONIBLE"
    salida = (proc.stderr or proc.stdout).strip().splitlines()
    return salida[0] if salida else "NO DISPONIBLE"


def pct(num: int, den: int) -> str:
    if den == 0:
        return "n/d"
    return f"{100.0 * num / den:.1f}".replace(".", ",") + " %"


def principal() -> int:
    if not MANIFIESTO.exists():
        print(f"No se encuentra {MANIFIESTO}", file=sys.stderr)
        return 1

    universo = leer_universo()
    resultados: dict[str, dict] = {}
    for serie, rutas in universo.items():
        listadas = len(rutas)
        presentes = [p for p in rutas if p.exists()]
        faltantes = [p for p in rutas if not p.exists()]
        with ThreadPoolExecutor(max_workers=os.cpu_count() or 4) as pool:
            filas = list(pool.map(analizar, presentes))
        con_error = [f for f in filas if f["error"]]
        sin_texto = [f for f in filas if not f["error"] and f["chars"] == 0]
        con_alguna = [f for f in filas if f["formas"]]
        con_alguna_palabra = [f for f in filas if f["formas_palabra"]]
        por_forma = {f: sum(1 for r in filas if f in r["formas"]) for f in FORMAS}
        resultados[serie] = {
            "listadas": listadas,
            "presentes": len(presentes),
            "faltantes": [str(p.relative_to(RAIZ)) for p in faltantes],
            "con_error": [(f["archivo"], f["error"]) for f in con_error],
            "sin_texto": [f["archivo"] for f in sin_texto],
            "con_alguna": len(con_alguna),
            "con_alguna_palabra": len(con_alguna_palabra),
            "por_forma": por_forma,
        }

    head = git("rev-parse", "HEAD")
    ahora = dt.datetime.now(dt.timezone.utc).astimezone().isoformat(timespec="seconds")
    pdft = version_pdftotext()
    comando = "python3 data/experiment/corpus_series_ab/formas_dispositivas.py"

    L: list[str] = []
    L.append("# Formas dispositivas en las series «A» y «B»\n")
    L.append("Artefacto de respaldo de `docs/tesis/main.tex` §3.1 (fila 146 de "
             "`docs/tesis/mapa_fuentes_cap_esquema.md`). Generado por "
             "`data/experiment/corpus_series_ab/formas_dispositivas.py`.\n")
    L.append(f"- Comando (desde la raíz del repo): `{comando}`\n")

    L.append("## Formas buscadas\n")
    L.append("Exactamente tres, como cadenas literales, sin variantes morfológicas:\n")
    for f, fn in zip(FORMAS, FORMAS_NORM):
        L.append(f"- «{f}» (normalizada: `{fn}`)")
    L.append("\nUna comunicación cuenta si su texto contiene al menos una de las tres.\n")

    L.append("## Método\n")
    L.append("- Universo: filas de `data/raw/manifiesto.csv` cuyo `archivo_local` "
             "cae bajo `02_comunicaciones_A/` (serie A) o `03_comunicaciones_B/` "
             "(serie B).")
    L.append("- Texto: el repo no tiene caché de texto extraído de estas "
             "comunicaciones (los PDF están gitignoreados y ningún archivo del "
             "árbol los transcribe), así que se extrae en memoria con "
             f"`pdftotext -enc UTF-8 <pdf> -` ({pdft}); no se persiste texto.")
    L.append("- Normalización previa a la búsqueda: NFKD sin marcas diacríticas, "
             "minúsculas, toda corrida de espacio en blanco (incluidos saltos de "
             "línea) colapsada a un espacio. Los cortes de palabra con guion al "
             "final de línea NO se recomponen.")
    L.append("- Coincidencia: búsqueda de subcadena literal de cada forma "
             "normalizada sobre el texto normalizado. Un PDF cuyo `pdftotext` "
             "falla o devuelve texto vacío no puede contar como positivo y queda "
             "en el denominador (se informa aparte).\n")

    L.append("## (A) Universo por serie: listadas, presentes, faltantes\n")
    L.append("| Serie | Listadas en manifiesto | Presentes en disco | Faltantes | Error de pdftotext | Texto vacío |")
    L.append("|---|---:|---:|---:|---:|---:|")
    for serie, r in resultados.items():
        L.append(f"| {serie} | {r['listadas']} | {r['presentes']} | {len(r['faltantes'])} | "
                 f"{len(r['con_error'])} | {len(r['sin_texto'])} |")
    L.append("")
    for serie, r in resultados.items():
        if r["faltantes"]:
            L.append(f"Faltantes en serie {serie} ({len(r['faltantes'])}):")
            for p in r["faltantes"][:50]:
                L.append(f"- `{p}`")
            if len(r["faltantes"]) > 50:
                L.append(f"- … y {len(r['faltantes']) - 50} más")
            L.append("")
        if r["con_error"]:
            L.append(f"Errores de pdftotext en serie {serie} ({len(r['con_error'])}):")
            for p, e in r["con_error"][:50]:
                L.append(f"- `{p}`: {e}")
            if len(r["con_error"]) > 50:
                L.append(f"- … y {len(r['con_error']) - 50} más")
            L.append("")
        if r["sin_texto"]:
            L.append(f"Texto vacío tras pdftotext en serie {serie} ({len(r['sin_texto'])}):")
            for p in r["sin_texto"][:50]:
                L.append(f"- `{p}`")
            if len(r["sin_texto"]) > 50:
                L.append(f"- … y {len(r['sin_texto']) - 50} más")
            L.append("")
    L.append("La tasa se calcula sobre los PRESENTES en disco (denominador); si "
             "hubiera faltantes, la tasa no cubre al universo completo.\n")

    L.append("## (B) Tasa con al menos una forma, por serie\n")
    L.append("| Serie | Con al menos una forma (numerador) | Presentes (denominador) | Tasa |")
    L.append("|---|---:|---:|---:|")
    for serie, r in resultados.items():
        L.append(f"| {serie} | {r['con_alguna']} | {r['presentes']} | "
                 f"{pct(r['con_alguna'], r['presentes'])} |")
    L.append("")
    L.append("Desglose por forma (una comunicación puede contar en más de una "
             "fila; por eso las filas no suman el numerador):\n")
    L.append("| Serie | " + " | ".join(f"«{f}»" for f in FORMAS) + " |")
    L.append("|---|" + "---:|" * len(FORMAS))
    for serie, r in resultados.items():
        L.append(f"| {serie} | " + " | ".join(str(r["por_forma"][f]) for f in FORMAS) + " |")
    L.append("")
    L.append("Sensibilidad (solo informativa; no es el criterio del mandato): "
             "mismas cadenas exigiendo límite de palabra a ambos lados, lo que "
             "excluye p. ej. «se establecen»:\n")
    L.append("| Serie | Con al menos una forma (límite de palabra) | Presentes | Tasa |")
    L.append("|---|---:|---:|---:|")
    for serie, r in resultados.items():
        L.append(f"| {serie} | {r['con_alguna_palabra']} | {r['presentes']} | "
                 f"{pct(r['con_alguna_palabra'], r['presentes'])} |")
    L.append("")

    L.append("## (C) Contraste con la prosa vigente de §3.1\n")
    L.append(f"La prosa de `docs/tesis/main.tex` §3.1 afirma {PROSA['A']:.0f} % "
             f"(serie A) y {PROSA['B']:.0f} % (serie B). Diferencia = tasa "
             "computada − prosa, en puntos porcentuales.\n")
    L.append("| Serie | Prosa | Computada | Diferencia (p.p.) | Redondeo entero coincide |")
    L.append("|---|---:|---:|---:|---|")
    for serie, r in resultados.items():
        if r["presentes"] == 0:
            L.append(f"| {serie} | {PROSA[serie]:.0f} % | n/d | n/d | n/d |")
            continue
        tasa = 100.0 * r["con_alguna"] / r["presentes"]
        dif = tasa - PROSA[serie]
        coincide = "sí" if round(tasa) == int(PROSA[serie]) else "NO"
        L.append(f"| {serie} | {PROSA[serie]:.0f} % | {pct(r['con_alguna'], r['presentes'])} | "
                 f"{dif:+.1f}".replace(".", ",") + f" | {coincide} |")
    L.append("")
    L.append("Este artefacto no corrige la prosa: informa el número que produce "
             "el criterio declarado arriba.\n")

    REPORTE.write_text("\n".join(L), encoding="utf-8")

    for serie, r in resultados.items():
        print(f"Serie {serie}: listadas {r['listadas']}, presentes {r['presentes']}, "
              f"faltantes {len(r['faltantes'])}, error {len(r['con_error'])}, "
              f"vacío {len(r['sin_texto'])}; con alguna forma {r['con_alguna']} "
              f"/ {r['presentes']} = {pct(r['con_alguna'], r['presentes'])} "
              f"(prosa {PROSA[serie]:.0f} %)")
    print(f"Generado: {ahora}")
    print(f"HEAD del repo al generar: {head}")
    print(f"Reporte escrito en {REPORTE.relative_to(RAIZ)}")
    return 0


if __name__ == "__main__":
    sys.exit(principal())
