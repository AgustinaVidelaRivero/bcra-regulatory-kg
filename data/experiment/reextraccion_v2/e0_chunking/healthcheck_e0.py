"""Health-check de troceo por TO (unidad B5.2, plan fila B5.2) — módulo aparte.

Corre el pipeline determinístico de E0 (e0_lib, sin editar) sobre un PDF y
reporta las señales de TROCEO ENFERMO, cada una con su evidencia. Es un
instrumento de lectura previo al escalado: no corrige nada, no escribe en el
repo y no llama a ningún LLM (costo USD 0).

Señales (las tres de la fila B5.2 del plan, más el invariante de cobertura):

  1. cid — líneas con '(cid:NN)' en el texto extraído: la fuente del PDF no
     trae mapa Unicode y pdfplumber emite el código de glifo en vez del
     carácter; todo lo que E1 lea de esas líneas está corrupto a nivel
     extracción. Medido en el corpus de escalado: 5 TOs, hasta 208 líneas
     en un solo TO (grep '(cid:' sobre
     data/experiment/escalado_prep/e0_dry/*/chunks_*.json).

  2. paginas_sin_seccion — grados de opacidad estructural, de mayor a menor:
     (a) el TO no tiene NINGUNA página de rol cuerpo (la compuerta de
     clasificar_paginas nunca abre: 47/53 TOs del bloque de régimen
     informativo, fe de erratas D10 §a); (b) tiene cuerpo pero 0 secciones
     parseadas (ninguna línea con formato de sección); (c) páginas de cuerpo
     cuyo encabezado no trae 'Sección N.' (aviso pagina_cuerpo_sin_seccion
     del parser: la página se lee como continuación del punto abierto, y a
     escala es señal de deriva de formato).

  3. unidades_anomalas_por_tamano — chunks terminales cuyo texto propio
     supera UMBRAL_CHARS_TERMINAL (26.182 chars: el peor terminal del subset
     de desarrollo, criterio C8 de la banda de referencia en
     data/experiment/escalado_prep/reporte_generalizacion.md §2). Un terminal
     muy por encima de la banda es un tramo que el parser no supo segmentar
     (casos medidos en el corpus de escalado: 126.723 chars en un TO de dos
     secciones sin puntos).

  4. cobertura_no_exacta — el invariante de cero pérdida de E0 no cierra
     (líneas duplicadas o huérfanas). En el subset es siempre exacto; si acá
     falla, el troceo de ese TO no es confiable.

Veredicto por TO: 'sano' si ninguna señal dispara; si no, la lista de
señales disparadas. El veredicto es de LECTURA (dónde mirar antes de gastar
en E1), no un gate: los umbrales vienen declarados de la banda de referencia
y pueden ajustarse por parámetro.

Uso:
  python3 healthcheck_e0.py                        # demo: los 5 TOs del subset
  python3 healthcheck_e0.py --pdf RUTA [--pdf …]   # TOs arbitrarios
  python3 healthcheck_e0.py --salida ARCHIVO.json  # además de stdout

Sin llamadas a LLM: código determinístico puro.
"""

from __future__ import annotations

import argparse
import json
import statistics
from pathlib import Path

import e0_lib as E0

REPO = Path(__file__).resolve().parents[3]
SUBSET = REPO / "experiment" / "subset"

# peor chunk terminal del subset de desarrollo (cap): criterio C8 de la banda
# de referencia del reporte de generalización del escalado
UMBRAL_CHARS_TERMINAL = 26182

MARCA_CID = "(cid:"


def health_check_to(pdf_path: Path, to: str | None = None,
                    umbral_chars: int = UMBRAL_CHARS_TERMINAL) -> dict:
    """Corre E0 completo (parser + reglas 1 y 2 + chunker, mismo orden que el
    driver de producción) sobre un PDF y devuelve el reporte de señales."""
    to = to or E0.TO_KEYS.get(pdf_path.name, pdf_path.stem)
    paginas = E0.extraer_lineas(pdf_path)
    roles = E0.clasificar_paginas(paginas)

    # --- señal 1: (cid:NN) sobre TODAS las líneas extraídas (todos los roles)
    lineas_cid: list[dict] = []
    for pi, lineas in enumerate(paginas, start=1):
        for l in lineas:
            if MARCA_CID in l.texto:
                lineas_cid.append({"pagina": pi, "rol": roles[pi - 1],
                                   "texto": l.texto[:90]})
    paginas_cid = sorted({d["pagina"] for d in lineas_cid})

    # --- parseo (idéntica secuencia a correr_e0.correr: reglas 1 y 2 aplicadas)
    res = E0.parsear_cuerpo(to, pdf_path.name, paginas, roles)
    res.reasignaciones_continuidad = E0.aplicar_continuidad_enumeracion(res)
    res.correccion_fronteras = E0.corregir_fronteras_intra_palabra(res)
    chunks = E0.construir_chunks(res)
    cob = E0.verificar_cobertura(res)

    # --- señal 2: páginas sin sección (tres grados)
    avisos_sin_seccion = [a for a in res.avisos
                          if a["tipo"] == "pagina_cuerpo_sin_seccion"]
    n_cuerpo = roles.count(E0.ROL_CUERPO)
    sin_seccion = {
        "paginas_cuerpo": n_cuerpo,
        "sin_pagina_de_cuerpo": n_cuerpo == 0,
        "secciones_parseadas": len(res.secciones),
        "avisos_pagina_cuerpo_sin_seccion": len(avisos_sin_seccion),
        "paginas": [a["pagina"] for a in avisos_sin_seccion],
    }

    # --- señal 3: unidades anómalas por tamaño
    terminales = [c for c in chunks if c["tipo"] != "mini_chunk"]
    propios = [c["chars_propio"] for c in terminales]
    anomalas = [{"unidad": c["unidad"], "chars_propio": c["chars_propio"],
                 "paginas": c["paginas"]}
                for c in terminales if c["chars_propio"] > umbral_chars]
    anomalas.sort(key=lambda d: -d["chars_propio"])
    tamanos = {
        "umbral_chars": umbral_chars,
        "chunks_terminales": len(terminales),
        "mediana_chars_propio": statistics.median(propios) if propios else 0,
        "max_chars_propio": max(propios) if propios else 0,
        "anomalas": anomalas,
    }

    senales = {
        "cid": {
            "lineas": len(lineas_cid),
            "paginas": paginas_cid,
            "muestras": lineas_cid[:3],
        },
        "paginas_sin_seccion": sin_seccion,
        "unidades_anomalas_por_tamano": tamanos,
        "cobertura_no_exacta": None if cob["cobertura_exacta"] else cob,
    }
    disparadas = []
    if lineas_cid:
        disparadas.append("cid")
    if sin_seccion["sin_pagina_de_cuerpo"] or not res.secciones \
            or avisos_sin_seccion:
        disparadas.append("paginas_sin_seccion")
    if anomalas:
        disparadas.append("unidades_anomalas_por_tamano")
    if not cob["cobertura_exacta"]:
        disparadas.append("cobertura_no_exacta")

    return {
        "to": to,
        "archivo": pdf_path.name,
        "paginas": len(paginas),
        "roles_pagina": {r: roles.count(r) for r in sorted(set(roles))},
        "unidades_extraccion": len(chunks),
        "senales": senales,
        "veredicto": "sano" if not disparadas else disparadas,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", action="append", default=None,
                    help="PDF a chequear (repetible); sin --pdf corre la demo "
                         "sobre los 5 TOs del subset de desarrollo")
    ap.add_argument("--umbral-chars", type=int, default=UMBRAL_CHARS_TERMINAL)
    ap.add_argument("--salida", default=None,
                    help="ruta de un JSON de salida (además de stdout)")
    args = ap.parse_args()

    if args.pdf:
        pdfs = [Path(p) for p in args.pdf]
    else:
        pdfs = [SUBSET / archivo
                for archivo, _to in sorted(E0.TO_KEYS.items(), key=lambda kv: kv[1])]

    reporte: dict[str, dict] = {}
    for pdf in pdfs:
        r = health_check_to(pdf, umbral_chars=args.umbral_chars)
        reporte[r["to"]] = r
        v = r["veredicto"]
        print(f"{r['to']:12s} {r['archivo']:55s} "
              f"{'SANO' if v == 'sano' else 'SEÑALES: ' + ', '.join(v)}")

    texto = json.dumps(reporte, ensure_ascii=False, indent=1)
    if args.salida:
        Path(args.salida).write_text(texto, encoding="utf-8")
    else:
        print(texto)


if __name__ == "__main__":
    main()
