"""Driver de E0: corre parser + chunker sobre los 5 TOs y escribe la salida.

Uso: python3 correr_e0.py [--salida DIR]

Salida (por defecto ./salida/):
  estructura_<to>.json   árbol estructural del cuerpo (mapa de E0)
  indice_<to>.json       entradas parseadas del índice
  chunks_<to>.json       chunks terminales con herencia, flags y sha256
  divergencias_indice_cuerpo.json
  censo_oraculo.json     reconciliación vs mapa de territorio (inventario x.y)
  conteos.json           conteos agregados por TO
  cobertura.json         verificación de cero pérdida por TO
  correcciones.json      reglas post-parseo: reasignaciones por continuidad de
                         enumeración (regla 1) y fronteras intra-palabra
                         corridas (regla 2), con conteos antes/después
"""

from __future__ import annotations

import argparse
import hashlib
import json
import statistics
from pathlib import Path

import e0_lib as E0

REPO = Path(__file__).resolve().parents[3]
SUBSET = REPO / "experiment" / "subset"
MAPA = REPO / "experiment" / "exploracion" / "mapa_territorio_quemado_5TOs_5sets.json"


def inventario_mapa() -> dict[str, list[str]]:
    m = json.loads(MAPA.read_text(encoding="utf-8"))
    out: dict[str, list[str]] = {}
    for to, d in m["por_to"].items():
        unidades = []
        for cat in ("quemadas_enteras", "quemadas_parcialmente", "disponibles"):
            for it in d.get(cat, []):
                unidades.append(it["unidad"] if isinstance(it, dict) else it)
        out[to] = unidades
    return out


def correr(salida: Path) -> dict:
    salida.mkdir(parents=True, exist_ok=True)
    mapa = inventario_mapa()
    conteos: dict = {}
    divergencias: dict = {}
    censo: dict = {}
    cobertura: dict = {}

    correcciones: dict = {}

    for archivo, to in sorted(E0.TO_KEYS.items(), key=lambda kv: kv[1]):
        pdf = SUBSET / archivo
        paginas = E0.extraer_lineas(pdf)
        roles = E0.clasificar_paginas(paginas)
        res = E0.parsear_cuerpo(to, archivo, paginas, roles)
        # correcciones post-parseo (reglas 1 y 2; ver docstring de e0_lib):
        # el conteo "antes" se toma sobre el árbol recién parseado, idéntico
        # al de la corrida sin reglas
        fronteras_antes = E0.detectar_fronteras_intra_palabra(res)
        res.reasignaciones_continuidad = E0.aplicar_continuidad_enumeracion(res)
        regla2 = E0.corregir_fronteras_intra_palabra(res)
        fronteras_despues = E0.detectar_fronteras_intra_palabra(res)
        res.correccion_fronteras = {
            "antes": fronteras_antes["n_intra_palabra"],
            "despues": fronteras_despues["n_intra_palabra"],
            **regla2,
        }
        correcciones[to] = {
            "reasignaciones_continuidad": res.reasignaciones_continuidad,
            "fronteras_intra_palabra": {
                "antes": fronteras_antes["n_intra_palabra"],
                "despues": fronteras_despues["n_intra_palabra"],
                "detalle_antes": fronteras_antes["fronteras"],
                "sospechosas_excluidas": fronteras_antes["sospechosas_excluidas"],
                "lineas_corridas": regla2["lineas_corridas"],
            },
        }
        indice = E0.parsear_indice(paginas, roles)
        chunks = E0.construir_chunks(res)
        div = E0.divergencias_indice_cuerpo(res, indice)
        cob = E0.verificar_cobertura(res)

        (salida / f"estructura_{to}.json").write_text(
            json.dumps(E0.serializar_estructura(res), ensure_ascii=False, indent=1),
            encoding="utf-8")
        (salida / f"indice_{to}.json").write_text(
            json.dumps(indice, ensure_ascii=False, indent=1), encoding="utf-8")
        (salida / f"chunks_{to}.json").write_text(
            json.dumps(chunks, ensure_ascii=False, indent=1), encoding="utf-8")

        divergencias[to] = div
        cobertura[to] = cob

        inv_parser = E0.inventario_nivel_mapa(res)
        inv_mapa = set(mapa[to])
        censo[to] = {
            "n_parser": len(inv_parser),
            "n_mapa": len(inv_mapa),
            "coincidencias": sorted(inv_parser & inv_mapa),
            "solo_mapa": sorted(inv_mapa - inv_parser),
            "solo_parser": sorted(inv_parser - inv_mapa),
        }

        terminales = [c for c in chunks if c["tipo"] != "mini_chunk"]
        minis = [c for c in chunks if c["tipo"] == "mini_chunk"]
        minis_por_rol: dict[str, int] = {}
        for c in minis:
            minis_por_rol[c["rol_bloque"]] = minis_por_rol.get(c["rol_bloque"], 0) + 1
        propios = [c["chars_propio"] for c in terminales]
        completos = [c["chars_completo"] for c in terminales]
        roles_pag = {r: roles.count(r) for r in sorted(set(roles))}
        conteos[to] = {
            "archivo": archivo,
            "paginas": len(paginas),
            "roles_pagina": roles_pag,
            "secciones": len(res.secciones),
            "puntos_terminales": sum(1 for c in terminales if c["tipo"] == "punto_terminal"),
            "secciones_sin_puntos": sum(1 for c in terminales if c["tipo"] == "seccion_sin_puntos"),
            "chunks_terminales": len(terminales),
            "mini_chunks": len(minis),
            "mini_chunks_por_rol": dict(sorted(minis_por_rol.items())),
            "chunks": len(chunks),
            "flag_contenido_tabular": sum(1 for c in chunks if c["flags"]["contenido_tabular"]),
            "flag_formula": sum(1 for c in chunks if c["flags"]["formula"]),
            "mediana_chars_propio": statistics.median(propios) if propios else 0,
            "mediana_chars_completo": statistics.median(completos) if completos else 0,
            "mediana_chars_mini_chunk": statistics.median(
                [c["chars_propio"] for c in minis]) if minis else 0,
            "rechazos_header": len(res.rechazos_header),
            "saltos_numeracion": len(res.saltos_numeracion),
            "avisos": len(res.avisos),
            "lineas_descartadas_encabezado_pie":
                res.accounting["lineas_descartadas_encabezado_pie"],
            "lineas_contenido": res.lineas_contenido,
            "lineas_huerfanas": res.lineas_huerfanas,
            "reasignaciones_continuidad": len(res.reasignaciones_continuidad),
            "fronteras_intra_palabra_antes": res.correccion_fronteras["antes"],
            "fronteras_intra_palabra_despues": res.correccion_fronteras["despues"],
            "lineas_corridas_por_frontera": res.correccion_fronteras["n_corridas"],
        }

    (salida / "divergencias_indice_cuerpo.json").write_text(
        json.dumps(divergencias, ensure_ascii=False, indent=1), encoding="utf-8")
    (salida / "censo_oraculo.json").write_text(
        json.dumps(censo, ensure_ascii=False, indent=1), encoding="utf-8")
    (salida / "conteos.json").write_text(
        json.dumps(conteos, ensure_ascii=False, indent=1), encoding="utf-8")
    (salida / "cobertura.json").write_text(
        json.dumps(cobertura, ensure_ascii=False, indent=1), encoding="utf-8")
    (salida / "correcciones.json").write_text(
        json.dumps(correcciones, ensure_ascii=False, indent=1), encoding="utf-8")
    return conteos


def shas_salida(salida: Path) -> dict[str, str]:
    return {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(salida.glob("*.json"))}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", default=str(Path(__file__).parent / "salida"))
    args = ap.parse_args()
    conteos = correr(Path(args.salida))
    print(json.dumps(conteos, ensure_ascii=False, indent=1))
