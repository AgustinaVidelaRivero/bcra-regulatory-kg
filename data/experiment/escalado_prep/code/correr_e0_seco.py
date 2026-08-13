"""E0 + censo EN SECO sobre los TOs del inventario de escalado.

INVOCA el E0 calibrado (data/experiment/reextraccion_v2/e0_chunking/e0_lib.py)
sin editarlo ni copiarlo: lo importa por path. Cero llamadas a LLM, cero costo.

Diferencia con el driver del subset (correr_e0.py): allí el censo reconcilia el
inventario x.y del parser contra el mapa de territorio quemado, que solo existe
para los 5 TOs del subset. Acá el censo es el estructural que E0 produce por sí
mismo — secciones, puntos, terminales, mini-chunks, cobertura de cero pérdida y
divergencias índice↔cuerpo — que es lo que se necesita para dimensionar y para
juzgar si el parser generaliza.

Cada TO se corre aislado: si revienta, se registra el traceback textual y se
sigue con el siguiente.

Salidas por TO en ../e0_dry/<id>/:
  estructura_<id>.json, indice_<id>.json, chunks_<id>.json,
  divergencias_<id>.json, cobertura_<id>.json, censo_<id>.json,
  correcciones_<id>.json, diagnostico_<id>.json
Agregado en ../e0_dry/:
  conteos_e0_dry.json, fallos_e0_dry.json
"""

from __future__ import annotations

import json
import statistics
import sys
import traceback
from pathlib import Path

AQUI = Path(__file__).resolve().parent
PREP = AQUI.parent
REPO = PREP.parents[2]
E0_DIR = REPO / "data" / "experiment" / "reextraccion_v2" / "e0_chunking"
sys.path.insert(0, str(E0_DIR))

import e0_lib as E0  # noqa: E402  — import por path, el módulo no se modifica

PDFS = PREP / "pdfs"
SALIDA = PREP / "e0_dry"


def censo_estructural(res, chunks: list[dict]) -> dict:
    """Censo de la estructura derivada: nodos por profundidad y responsables
    de extracción. Un nodo terminal se cubre con su chunk terminal; un nodo no
    terminal, con sus mini-chunks de prosa (si tiene prosa propia)."""
    por_prof: dict[int, int] = {}
    terminales_arbol = 0
    no_terminales = 0

    def rec(n, prof: int):
        nonlocal terminales_arbol, no_terminales
        por_prof[prof] = por_prof.get(prof, 0) + 1
        if n.hijos:
            no_terminales += 1
            for h in n.hijos:
                rec(h, prof + 1)
        else:
            terminales_arbol += 1

    for s in res.secciones:
        rec(s, 1)

    minis = [c for c in chunks if c["tipo"] == "mini_chunk"]
    terminales = [c for c in chunks if c["tipo"] != "mini_chunk"]
    unidades_origen_mini = {c["id"].split("::")[1] for c in minis}
    return {
        "secciones": len(res.secciones),
        "nodos_por_profundidad": dict(sorted(por_prof.items())),
        "nodos_terminales_arbol": terminales_arbol,
        "nodos_no_terminales": no_terminales,
        "chunks_terminales": len(terminales),
        "mini_chunks": len(minis),
        "unidades_no_terminales_con_mini_chunk": len(unidades_origen_mini),
        "unidades_extraccion_total": len(chunks),
    }


def diagnostico(res, indice, chunks, div, cob) -> dict:
    """Señales que decide el reporte de generalización."""
    terminales = [c for c in chunks if c["tipo"] != "mini_chunk"]
    minis = [c for c in chunks if c["tipo"] == "mini_chunk"]
    propios = [c["chars_propio"] for c in terminales]

    motivos: dict[str, int] = {}
    for r in res.rechazos_header:
        motivos[r.get("motivo", "?")] = motivos.get(r.get("motivo", "?"), 0) + 1
    avisos: dict[str, int] = {}
    for a in res.avisos:
        avisos[a.get("tipo", "?")] = avisos.get(a.get("tipo", "?"), 0) + 1

    tabulares = [c for c in chunks if c["flags"]["contenido_tabular"]]
    formulas = [c for c in chunks if c["flags"]["formula"]]

    return {
        "indice": {
            "entradas_indice": len(indice),
            "secciones_en_indice": sum(1 for e in indice if e["tipo"] == "seccion"),
            "puntos_en_indice": sum(1 for e in indice if e["tipo"] == "punto"),
            "profundidad_declarada": div["profundidad_declarada_indice"],
            "anunciado_sin_cuerpo": len(div["anunciado_sin_cuerpo"]),
            "en_cuerpo_sin_anunciar": len(div["en_cuerpo_sin_anunciar"]),
            "titulos_distintos": len(div["titulos_distintos"]),
        },
        "rechazos_header": {"total": len(res.rechazos_header), "por_motivo": motivos},
        "saltos_numeracion": len(res.saltos_numeracion),
        "avisos": {"total": len(res.avisos), "por_tipo": avisos},
        "fronteras": {
            "reasignaciones_continuidad": len(res.reasignaciones_continuidad),
            "intra_palabra_antes": res.correccion_fronteras["antes"],
            "intra_palabra_despues": res.correccion_fronteras["despues"],
            "lineas_corridas": res.correccion_fronteras["n_corridas"],
        },
        "tabular": {
            "chunks_con_contenido_tabular": len(tabulares),
            "pct_chunks_tabulares": round(100 * len(tabulares) / len(chunks), 2) if chunks else 0.0,
            "chunks_con_formula": len(formulas),
        },
        "escala": {
            "mediana_chars_propio_terminal": statistics.median(propios) if propios else 0,
            "p90_chars_propio_terminal": (
                sorted(propios)[int(0.9 * (len(propios) - 1))] if propios else 0),
            "max_chars_propio_terminal": max(propios) if propios else 0,
            "mediana_chars_mini_chunk": (
                statistics.median([c["chars_propio"] for c in minis]) if minis else 0),
            "chars_propio_total": sum(c["chars_propio"] for c in chunks),
        },
        "cobertura": cob,
    }


def correr_uno(ident: str, pdf: Path) -> dict:
    paginas = E0.extraer_lineas(pdf)
    roles = E0.clasificar_paginas(paginas)
    res = E0.parsear_cuerpo(ident, pdf.name, paginas, roles)

    fronteras_antes = E0.detectar_fronteras_intra_palabra(res)
    res.reasignaciones_continuidad = E0.aplicar_continuidad_enumeracion(res)
    regla2 = E0.corregir_fronteras_intra_palabra(res)
    fronteras_despues = E0.detectar_fronteras_intra_palabra(res)
    res.correccion_fronteras = {
        "antes": fronteras_antes["n_intra_palabra"],
        "despues": fronteras_despues["n_intra_palabra"],
        **regla2,
    }

    indice = E0.parsear_indice(paginas, roles)
    chunks = E0.construir_chunks(res)
    div = E0.divergencias_indice_cuerpo(res, indice)
    cob = E0.verificar_cobertura(res)
    censo = censo_estructural(res, chunks)
    diag = diagnostico(res, indice, chunks, div, cob)

    d = SALIDA / ident
    d.mkdir(parents=True, exist_ok=True)
    esc = lambda n, o: (d / f"{n}_{ident}.json").write_text(  # noqa: E731
        json.dumps(o, ensure_ascii=False, indent=1), encoding="utf-8")
    esc("estructura", E0.serializar_estructura(res))
    esc("indice", indice)
    esc("chunks", chunks)
    esc("divergencias", div)
    esc("cobertura", cob)
    esc("censo", censo)
    esc("correcciones", {
        "reasignaciones_continuidad": res.reasignaciones_continuidad,
        "fronteras_intra_palabra": {
            "antes": fronteras_antes["n_intra_palabra"],
            "despues": fronteras_despues["n_intra_palabra"],
            "detalle_antes": fronteras_antes["fronteras"],
            "sospechosas_excluidas": fronteras_antes["sospechosas_excluidas"],
            "lineas_corridas": regla2["lineas_corridas"],
        },
    })
    esc("diagnostico", diag)

    terminales = [c for c in chunks if c["tipo"] != "mini_chunk"]
    minis = [c for c in chunks if c["tipo"] == "mini_chunk"]
    roles_pag = {r: roles.count(r) for r in sorted(set(roles))}
    return {
        "archivo": pdf.name,
        "bytes": pdf.stat().st_size,
        "paginas": len(paginas),
        "roles_pagina": roles_pag,
        "paginas_cuerpo": res.paginas_cuerpo,
        "secciones": len(res.secciones),
        "chunks_terminales": len(terminales),
        "mini_chunks": len(minis),
        "unidades_extraccion": len(chunks),
        "censo": censo,
        "diagnostico": diag,
    }


def main() -> None:
    SALIDA.mkdir(parents=True, exist_ok=True)
    pdfs = sorted(PDFS.glob("*.pdf"))
    conteos: dict[str, dict] = {}
    fallos: dict[str, dict] = {}

    conteos_path = SALIDA / "conteos_e0_dry.json"
    fallos_path = SALIDA / "fallos_e0_dry.json"
    if conteos_path.exists():
        conteos = json.loads(conteos_path.read_text(encoding="utf-8"))
    if fallos_path.exists():
        fallos = json.loads(fallos_path.read_text(encoding="utf-8"))

    for i, pdf in enumerate(pdfs, 1):
        ident = pdf.stem
        if ident in conteos or ident in fallos:
            continue
        try:
            conteos[ident] = correr_uno(ident, pdf)
            c = conteos[ident]
            print(f"[{i:3d}/{len(pdfs)}] {ident:28s} OK  pag={c['paginas']:4d} "
                  f"sec={c['secciones']:3d} term={c['chunks_terminales']:5d} "
                  f"mini={c['mini_chunks']:5d}", flush=True)
        except Exception:                          # noqa: BLE001 — se registra textual
            fallos[ident] = {"archivo": pdf.name, "bytes": pdf.stat().st_size,
                             "traceback": traceback.format_exc()}
            print(f"[{i:3d}/{len(pdfs)}] {ident:28s} FALLO", flush=True)
        conteos_path.write_text(json.dumps(conteos, ensure_ascii=False, indent=1),
                                encoding="utf-8")
        fallos_path.write_text(json.dumps(fallos, ensure_ascii=False, indent=1),
                               encoding="utf-8")

    print(f"\nOK={len(conteos)}  FALLOS={len(fallos)}  PDFs={len(pdfs)}")


if __name__ == "__main__":
    main()
