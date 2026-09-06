"""Driver de E0: corre parser + chunker sobre un corpus y escribe la salida.

Uso: python3 correr_e0.py [--salida DIR] [--manifiesto RUTA]

Sin --manifiesto: comportamiento legacy intacto (los 5 TOs del subset vía
E0.TO_KEYS y el mapa de territorio quemado). Con --manifiesto (U-B5.1): los
TOs, las rutas de PDF y el mapa-oráculo salen del manifiesto de corpus; con
`oraculo.mapa_territorio: null` NO se construye censo_oraculo.json (modo sin
oráculo — las etapas aguas abajo lo declaran, ver e2_lib.SIN_ORACULO).

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
  sub_chunking.json      SOLO si alguna unidad superó el umbral C8 (U-B5.3):
                         particiones por ítems y unidades no particionables
                         declaradas; en el subset de desarrollo no se emite
                         (0 unidades sobre el umbral) y la salida es
                         byte-idéntica a la histórica
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import statistics
from pathlib import Path

import e0_lib as E0

REPO = Path(__file__).resolve().parents[3]
SUBSET = REPO / "experiment" / "subset"
MAPA = REPO / "experiment" / "exploracion" / "mapa_territorio_quemado_5TOs_5sets.json"


# ------------------------------------------------------------ sub-chunking
# U-B5.3 decisión 6 — partición por ítems de unidades que exceden el umbral
# de tamaño, SOLO relevante para TOs nuevos: el peor terminal del subset de
# desarrollo mide exactamente 26.182 chars (criterio C8 de la banda de
# referencia, escalado_prep/reporte_generalizacion.md §2, mismo valor que
# healthcheck_e0.UMBRAL_CHARS_TERMINAL) y el corte es ESTRICTO (>), así que
# ninguna unidad de desarrollo se toca y la salida dev queda byte-idéntica.
# Medición sobre el corpus de escalado (152 TOs de e0_dry): 6/6.670
# terminales superan el umbral (27.161–126.723 chars), todos de TOs
# "necesita reglas" — 0 en los 68 digeribles. Mecánica: se detectan ítems de
# lista por marcadores al inicio de línea, se agrupan bloques consecutivos
# hasta un objetivo de tamaño y el chapeau (texto previo al primer ítem)
# queda en el texto de la parte 1 y viaja como HERENCIA (tramos encabezado +
# intro, patrón E0) en las partes siguientes. Una unidad sobre el umbral SIN
# ítems detectables NO se particiona y queda declarada en sub_chunking.json
# (nunca en silencio).
UMBRAL_CHARS_SUBCHUNK = 26182            # == C8; > estricto preserva dev
OBJETIVO_CHARS_PARTE = UMBRAL_CHARS_SUBCHUNK // 2   # 13.091
MIN_ITEMS_SUBCHUNK = 3

# familias de marcador de ítem, por precedencia de matcheo por línea
FAMILIAS_ITEM = [
    ("num", re.compile(r"^\d+(?:\.\d+)*\.(?:\s|$)")),      # "2.", "1.5.1. …"
    ("inciso", re.compile(r"^[a-zñ]\)(?:\s|$)")),          # "a) …"
    ("romano", re.compile(r"^[ivxlcdm]{2,}\)(?:\s|$)")),   # "ii) …"
    ("guion", re.compile(r"^[-–—•]\s")),                   # "— …"
]


def _particionar_texto(texto: str) -> dict | None:
    """Partición por ítems del texto propio de una unidad. La línea 0 (label/
    título) nunca es marcador. Devuelve chapeau + grupos (cada uno ≤ objetivo
    salvo bloque único mayor) o None si no hay familia con MIN_ITEMS líneas.
    Invariante: chapeau + grupos reconstruyen el texto línea a línea (cero
    pérdida, mismo principio que verificar_cobertura)."""
    lineas = texto.split("\n")
    conteo: dict[str, list[int]] = {f: [] for f, _ in FAMILIAS_ITEM}
    for i, l in enumerate(lineas[1:], start=1):
        s = l.strip()
        for fam, pat in FAMILIAS_ITEM:
            if pat.match(s):
                conteo[fam].append(i)
                break
    familia = max(conteo, key=lambda f: len(conteo[f]))
    indices = conteo[familia]
    if len(indices) < MIN_ITEMS_SUBCHUNK:
        return None
    chapeau = "\n".join(lineas[:indices[0]])
    bloques = ["\n".join(lineas[i0:(indices[j + 1] if j + 1 < len(indices)
                                    else len(lineas))])
               for j, i0 in enumerate(indices)]
    grupos: list[str] = []
    actual: list[str] = []
    tam = 0
    for b in bloques:
        if actual and tam + len(b) + 1 > OBJETIVO_CHARS_PARTE:
            grupos.append("\n".join(actual))
            actual, tam = [], 0
        actual.append(b)
        tam += len(b) + 1
    if actual:
        grupos.append("\n".join(actual))
    if len(grupos) < 2:
        return None  # partir en 1 no remedia nada: se declara, no se parte
    return {"chapeau": chapeau, "grupos": grupos, "familia": familia,
            "n_items": len(indices)}


def _sub_chunks_de(c: dict, part: dict) -> list[dict]:
    """Materializa las partes de una unidad particionada. La parte 1 lleva el
    chapeau en su TEXTO (es la unidad responsable de su contenido normativo);
    las partes 2..n lo reciben como herencia (tramos `encabezado` + `intro`
    con unidad_origen = la unidad, patrón E0: el contexto ancla, la unidad
    extrae). `unidad` no cambia: la provenance de los elementos extraídos
    sigue anclando en la unidad documental real. Flags y páginas se heredan
    de la unidad completa (conservador, declarado)."""
    chapeau, grupos = part["chapeau"], part["grupos"]
    lineas_chapeau = chapeau.split("\n")
    tramos_chapeau = [{"tipo": "encabezado", "unidad_origen": c["unidad"],
                       "texto": lineas_chapeau[0], "paginas": list(c["paginas"])}]
    resto = "\n".join(lineas_chapeau[1:])
    if resto.strip():
        tramos_chapeau.append({"tipo": "intro", "unidad_origen": c["unidad"],
                               "texto": resto, "paginas": list(c["paginas"])})
    n = len(grupos)
    out = []
    for k, g in enumerate(grupos, start=1):
        texto = (chapeau + "\n" + g) if k == 1 else g
        herencia = copy.deepcopy(c["herencia"])
        if k > 1:
            herencia += copy.deepcopy(tramos_chapeau)
        texto_herencia = "\n".join(t["texto"] for t in herencia)
        completo = (texto_herencia + "\n" + texto) if texto_herencia else texto
        out.append({
            "id": f"{c['id']}::parte{k}",
            "to": c["to"],
            "archivo": c["archivo"],
            "unidad": c["unidad"],
            "titulo": f"{c['titulo']} (parte {k}/{n})",
            "tipo": c["tipo"],
            "paginas": list(c["paginas"]),
            "texto": texto,
            "chars_propio": len(texto),
            "chars_completo": len(completo),
            "herencia": herencia,
            "flags": copy.deepcopy(c["flags"]),
            "sub_chunk": {"parte": k, "de": n,
                          "id_unidad_completa": c["id"],
                          "chars_unidad_completa": c["chars_propio"],
                          "familia_items": part["familia"]},
            "sha256_propio": hashlib.sha256(texto.encode("utf-8")).hexdigest(),
            "sha256_completo": hashlib.sha256(completo.encode("utf-8")).hexdigest(),
        })
    return out


def subdividir_unidades_grandes(chunks: list[dict],
                                umbral: int = UMBRAL_CHARS_SUBCHUNK) -> tuple[list[dict], dict]:
    """Aplica la partición a los chunks terminales cuyo texto propio EXCEDE el
    umbral (estricto). Los demás pasan tal cual (mismos objetos: con 0
    unidades sobre el umbral la salida serializada es byte-idéntica).
    Devuelve (chunks, reporte) con particiones y no-particionables."""
    out: list[dict] = []
    particiones: list[dict] = []
    no_particionables: list[dict] = []
    for c in chunks:
        if c.get("tipo") == "mini_chunk" or c["chars_propio"] <= umbral:
            out.append(c)
            continue
        part = _particionar_texto(c["texto"])
        if part is None:
            out.append(c)
            no_particionables.append({
                "id": c["id"], "chars_propio": c["chars_propio"],
                "motivo": "sin_items_detectables"})
            continue
        subs = _sub_chunks_de(c, part)
        out.extend(subs)
        particiones.append({
            "id": c["id"], "chars_propio": c["chars_propio"],
            "familia_items": part["familia"], "n_items": part["n_items"],
            "n_partes": len(subs),
            "partes": [{"id": s["id"], "chars_propio": s["chars_propio"]}
                       for s in subs],
            "partes_sobre_umbral": [s["id"] for s in subs
                                    if s["chars_propio"] > umbral]})
    reporte = {"umbral_chars": umbral,
               "objetivo_chars_parte": OBJETIVO_CHARS_PARTE,
               "particiones": particiones,
               "no_particionables": no_particionables}
    return out, reporte


def inventario_mapa(mapa_path: Path = MAPA) -> dict[str, list[str]]:
    m = json.loads(mapa_path.read_text(encoding="utf-8"))
    out: dict[str, list[str]] = {}
    for to, d in m["por_to"].items():
        unidades = []
        for cat in ("quemadas_enteras", "quemadas_parcialmente", "disponibles"):
            for it in d.get(cat, []):
                unidades.append(it["unidad"] if isinstance(it, dict) else it)
        out[to] = unidades
    return out


def correr(salida: Path, manifiesto=None) -> dict:
    salida.mkdir(parents=True, exist_ok=True)
    if manifiesto is None:
        items = sorted(E0.TO_KEYS.items(), key=lambda kv: kv[1])
        pdfs = {to: SUBSET / archivo for archivo, to in items}
        mapa = inventario_mapa()
    else:
        items = sorted(((manifiesto.archivo_de(t), t) for t in manifiesto.ids),
                       key=lambda kv: kv[1])
        pdfs = {to: manifiesto.pdf_de(to) for _, to in items}
        mapa = (inventario_mapa(manifiesto.mapa_territorio)
                if manifiesto.tiene_oraculo else None)
    conteos: dict = {}
    divergencias: dict = {}
    censo: dict = {}
    cobertura: dict = {}

    correcciones: dict = {}
    sub_chunking: dict = {}

    for archivo, to in items:
        pdf = pdfs[to]
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
        # U-B5.3 decisión 6: partición por ítems de unidades sobre el umbral
        # C8 (identidad en el subset de desarrollo: 0 unidades lo superan).
        chunks, rep_sub = subdividir_unidades_grandes(chunks)
        if rep_sub["particiones"] or rep_sub["no_particionables"]:
            sub_chunking[to] = rep_sub
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

        if mapa is not None:
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
    if mapa is not None:
        (salida / "censo_oraculo.json").write_text(
            json.dumps(censo, ensure_ascii=False, indent=1), encoding="utf-8")
    (salida / "conteos.json").write_text(
        json.dumps(conteos, ensure_ascii=False, indent=1), encoding="utf-8")
    (salida / "cobertura.json").write_text(
        json.dumps(cobertura, ensure_ascii=False, indent=1), encoding="utf-8")
    (salida / "correcciones.json").write_text(
        json.dumps(correcciones, ensure_ascii=False, indent=1), encoding="utf-8")
    if sub_chunking:  # solo si hubo unidades sobre el umbral (jamás en dev)
        (salida / "sub_chunking.json").write_text(
            json.dumps(sub_chunking, ensure_ascii=False, indent=1),
            encoding="utf-8")
    return conteos


def shas_salida(salida: Path) -> dict[str, str]:
    return {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(salida.glob("*.json"))}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", default=str(Path(__file__).parent / "salida"))
    ap.add_argument("--manifiesto", default=None,
                    help="ruta a un manifiesto de corpus (U-B5.1); sin él, "
                         "comportamiento legacy sobre los 5 TOs del subset")
    args = ap.parse_args()
    man = None
    if args.manifiesto:
        import sys
        sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
        import manifiesto_corpus
        man = manifiesto_corpus.cargar(Path(args.manifiesto))
    conteos = correr(Path(args.salida), manifiesto=man)
    print(json.dumps(conteos, ensure_ascii=False, indent=1))
