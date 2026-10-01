"""
generar_desde_catalogo.py — U-CAT-UNICO: genera desde el catálogo único (JSON
de formato catalogo_sujetos_unico/1) cada artefacto que hoy consume el
catálogo de sujetos (decisión 1 del mandato). Ninguna llamada a la API.

Artefactos, con el sufijo de la versión del catálogo (`version`, p. ej. v3):
  bloque_catalogo_<v>.txt      bloque del prompt (de `## Sujetos regulados` al
                               fin de `## Roles de alcance por TO`)
  enums_tool_schema_<v>.json   enums `sujeto_id` y `sujeto_propuesto_padre_sugerido`
  rol_por_to_<v>.json          ROL_POR_TO (roles y mapeos a clase)
  labels_e2_<v>.json           id → {label, nivel} para el ensamblado E2
  indice_e4_<v>.json           r1_e4.indice_catalogo sobre la entrada del
                               esqueleto: [criterio, clave, id] ordenado
  entrada_esqueleto_<v>.json   forma de esquema_v3_clases.json (clases, roles,
                               excepciones_s15): entrada de assemble.build_skeleton,
                               de la resolución de E4 y de --excepciones (S15/S19)
  ids_s19_<v>.json             conjunto de ids vigentes de S19, ordenado
  catalogo_suite_<v>.json      catálogo de scripts/regression_kg.py --catalogo
                               (version, clases, roles)
  manifest_generados_<v>.json  sha256 del catálogo y de cada generado

Reglas de presentación (las mismas que reproducen los artefactos v3):
  - enum: ids vigentes en el orden de `sujetos`;
  - bloque: por encabezado de `presentacion.grupos_bloque`, sus ids en el orden
    de `sujetos`; línea `id — label[ (alias: …)][ [instancia]][ [rol del TO x]]`
    y `  def: …` si hay definición;
  - ROL_POR_TO: roles en el orden de `sujetos`, después mapeos a clase por
    archivo de TO;
  - esquema de clases: clases e instancias, después roles, en el orden de
    `sujetos`; excepciones_s15 por (causa, TO).

Uso (desde la raíz del repo):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/catalogo_unico/code/generar_desde_catalogo.py \
      --catalogo data/experiment/catalogo_unico/catalogo_sujetos_v3.json \
      --salida data/experiment/catalogo_unico/generados_v3
"""

from __future__ import annotations

import sys

sys.dont_write_bytecode = True

import argparse  # noqa: E402
import hashlib  # noqa: E402
import json  # noqa: E402
from pathlib import Path  # noqa: E402

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
_RUTAS_E4 = (REX, REX / "corpus_v2", REPO / "data" / "experiment" / "grafo_v2" / "code", REX / "e2_reduce")

FORMATO = "catalogo_sujetos_unico/1"
GENERADOR = "data/experiment/catalogo_unico/code/generar_desde_catalogo.py"


class ErrorCatalogo(RuntimeError):
    """El catálogo no cumple el formato o una regla de generación."""


def sha256_texto(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def _rel(p: Path) -> str:
    p = Path(p).resolve()
    try:
        return str(p.relative_to(REPO))
    except ValueError:
        return p.name


def _json(obj) -> str:
    return json.dumps(obj, ensure_ascii=False, indent=1) + "\n"


def cargar(ruta: Path) -> tuple[dict, str, str]:
    texto = Path(ruta).read_text(encoding="utf-8")
    cat = json.loads(texto)
    if cat.get("formato") != FORMATO:
        raise ErrorCatalogo(f"{ruta}: formato {cat.get('formato')!r} ≠ {FORMATO}")
    ids = [s["id"] for s in cat["sujetos"]]
    if len(ids) != len(set(ids)):
        raise ErrorCatalogo(f"{ruta}: ids duplicados")
    return cat, sha256_texto(texto), _rel(Path(ruta))


def vigentes(cat: dict) -> list[dict]:
    return [s for s in cat["sujetos"] if s["estado"]["valor"] == "vigente"]


# ------------------------------------------------------------------------- #
# Prompt y tool schema                                                        #
# ------------------------------------------------------------------------- #
def _linea_bloque(s: dict) -> str:
    linea = f"{s['id']} — {s['label']}"
    if s["alias"]:
        linea += f" (alias: {', '.join(s['alias'])})"
    if s["nivel"] == "instancia":
        linea += " [instancia]"
    if s["nivel"] == "rol":
        if len(s["rol_por_to"]) != 1:
            raise ErrorCatalogo(f"{s['id']}: un rol tiene exactamente un TO")
        linea += f" [rol del TO {s['rol_por_to'][0]}]"
    return linea


def orden_bloque(cat: dict) -> list[dict]:
    vig = vigentes(cat)
    grupos = cat["presentacion"]["grupos_bloque"]
    fuera = {s["grupo_bloque"] for s in vig} - set(grupos)
    if fuera:
        raise ErrorCatalogo(f"grupos sin encabezado declarado: {sorted(fuera)}")
    return [s for g in grupos for s in vig if s["grupo_bloque"] == g]


def generar_bloque(cat: dict) -> str:
    vig = vigentes(cat)
    lineas: list[str] = []
    for g in cat["presentacion"]["grupos_bloque"]:
        lineas.append(g)
        for s in vig:
            if s["grupo_bloque"] != g:
                continue
            lineas.append(_linea_bloque(s))
            if s["definicion"]:
                lineas.append(f"  def: {s['definicion']}")
    orden_bloque(cat)  # valida que todo id vigente tenga encabezado
    return "\n".join(lineas) + "\n"


def generar_enums(cat: dict) -> dict:
    ids = [s["id"] for s in vigentes(cat)]
    return {"sujeto_id": list(ids), "sujeto_propuesto_padre_sugerido": list(ids)}


def generar_rol_por_to(cat: dict) -> dict:
    vig = vigentes(cat)
    out: dict[str, dict] = {}
    for s in vig:
        if s["nivel"] != "rol":
            continue
        to = s["rol_por_to"][0]
        out[to] = {"rol_id": s["id"], "label": s["label"],
                   "miembros_ids": list(s["rol"]["miembros_ids_mensaje"]),
                   "miembros_labels": list(s["rol"]["miembros_labels_mensaje"])}
    tos = sorted({to for s in vig if s["nivel"] != "rol" for to in s["rol_por_to"]})
    for to in tos:
        if to in out:
            raise ErrorCatalogo(f"{to}: TO con rol y con mapeo a clase")
        clases = [s for s in vig if s["nivel"] != "rol" and to in s["rol_por_to"]]
        ids = [s["id"] for s in clases]
        labels = [s["label"] for s in clases]
        out[to] = {"rol_id": ids[0] if len(ids) == 1 else None, "clase_ids": ids,
                   "label": " / ".join(labels), "miembros_ids": list(ids), "miembros_labels": labels}
    return out


def generar_labels_e2(cat: dict) -> dict:
    return {s["id"]: {"label": s["label"], "nivel": s["nivel"]} for s in orden_bloque(cat)}


# ------------------------------------------------------------------------- #
# Esquema de clases (esqueleto, E4, S15/S19, suite)                           #
# ------------------------------------------------------------------------- #
def _clase_esquema(s: dict) -> dict:
    if s["nivel"] == "clase":
        d = {"id": s["id"], "label": s["label"], "nivel": "clase", "padre": s["padre"]}
        if s["padre_inferido"]:
            d["padre_inferido"] = True
        d["disjunta_con"] = list(s["disjunta_con"])
        d["alias"] = list(s["alias"])
        d["provenance"] = dict(s["provenance_esqueleto"])
        return d
    d = {"id": s["id"], "label": s["label"], "nivel": "instancia", "instancia_de": s["instancia_de"],
         "alias": list(s["alias"]), "provenance": dict(s["provenance_esqueleto"])}
    if s["parte_de"]:
        d["parte_de"] = s["parte_de"]
    return d


def _rol_esquema(s: dict) -> dict:
    r = s["rol"]
    d = {"id": s["id"], "label": s["label"], "nivel": "rol", "to": s["rol_por_to"][0],
         "miembros": list(r["miembros"]), "provenance": dict(s["provenance_esqueleto"])}
    if r["sin_miembro_adjudicable"]:
        d["sin_miembro_adjudicable"] = r["sin_miembro_adjudicable"]
    if r["residuo_declarado"]:
        d["residuo_declarado"] = r["residuo_declarado"]
    return d


def generar_excepciones_s15(cat: dict) -> dict:
    pol = cat["politicas"]["excepciones_s15"]
    remedios = pol["remedios"]
    filas = []
    for s in vigentes(cat):
        if s["nivel"] == "rol" and s["rol"]["sin_miembro_adjudicable"]:
            causa = s["rol"]["sin_miembro_adjudicable"]
            if causa not in remedios:
                raise ErrorCatalogo(f"{s['id']}: causa {causa!r} sin remedio declarado")
            filas.append({"rol_id": s["id"], "to": s["rol_por_to"][0].removesuffix(".pdf"),
                          "causa": causa, "remedio": remedios[causa],
                          "colectivos": list(s["rol"]["miembros_labels_mensaje"])})
    filas.sort(key=lambda f: (f["causa"], f["to"]))
    return {"enunciado": pol["enunciado"], "total": len(filas),
            "por_causa": {k: sum(1 for f in filas if f["causa"] == k) for k in remedios},
            "remedios": dict(remedios), "roles": filas}


def _deriva_de(ruta_cat: str, sha_cat: str) -> dict:
    return {"catalogo_unico": ruta_cat, "sha256": sha_cat, "generador": GENERADOR}


def generar_entrada_esqueleto(cat: dict, ruta_cat: str, sha_cat: str) -> dict:
    vig = vigentes(cat)
    return {"version": cat["version_esquema_clases"], "deriva_de": _deriva_de(ruta_cat, sha_cat),
            "clases": [_clase_esquema(s) for s in vig if s["nivel"] != "rol"],
            "roles": [_rol_esquema(s) for s in vig if s["nivel"] == "rol"],
            "excepciones_s15": generar_excepciones_s15(cat)}


def generar_catalogo_suite(cat: dict, ruta_cat: str, sha_cat: str) -> dict:
    e = generar_entrada_esqueleto(cat, ruta_cat, sha_cat)
    return {"version": e["version"], "deriva_de": e["deriva_de"], "clases": e["clases"], "roles": e["roles"]}


def _r1_e4():
    for p in _RUTAS_E4:
        if str(p) not in sys.path:
            sys.path.insert(0, str(p))
    import r1_e4  # noqa: PLC0415 — importado, no copiado (indice_catalogo :74)
    return r1_e4


def indice_e4_serializable(idx: dict) -> list[list[str]]:
    return [[crit, clave, i] for (crit, clave), i in sorted(idx.items())]


def generar_indice_e4(entrada: dict) -> list[list[str]]:
    return indice_e4_serializable(_r1_e4().indice_catalogo(entrada))


def generar_ids_s19(cat: dict) -> list[str]:
    return sorted(s["id"] for s in vigentes(cat))


# ------------------------------------------------------------------------- #
# Conjunto completo                                                           #
# ------------------------------------------------------------------------- #
def generar_todo(ruta_catalogo: Path) -> dict[str, str]:
    """nombre de archivo → texto, en orden fijo; el manifiesto va al final."""
    cat, sha_cat, ruta_cat = cargar(ruta_catalogo)
    v = cat["version"]
    entrada = generar_entrada_esqueleto(cat, ruta_cat, sha_cat)
    archivos = {
        f"bloque_catalogo_{v}.txt": generar_bloque(cat),
        f"enums_tool_schema_{v}.json": _json(generar_enums(cat)),
        f"rol_por_to_{v}.json": _json(generar_rol_por_to(cat)),
        f"labels_e2_{v}.json": _json(generar_labels_e2(cat)),
        f"indice_e4_{v}.json": _json(generar_indice_e4(entrada)),
        f"entrada_esqueleto_{v}.json": _json(entrada),
        f"ids_s19_{v}.json": _json(generar_ids_s19(cat)),
        f"catalogo_suite_{v}.json": _json(generar_catalogo_suite(cat, ruta_cat, sha_cat)),
    }
    manifest = {"catalogo": ruta_cat, "catalogo_sha256": sha_cat, "version": v,
                "generador": GENERADOR,
                "archivos": {n: sha256_texto(t) for n, t in archivos.items()}}
    archivos[f"manifest_generados_{v}.json"] = _json(manifest)
    return archivos


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--catalogo", type=Path, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    args = ap.parse_args()
    archivos = generar_todo(args.catalogo)
    args.salida.mkdir(parents=True, exist_ok=True)
    for nombre, texto in archivos.items():
        (args.salida / nombre).write_text(texto, encoding="utf-8")
        print(f"{sha256_texto(texto)}  {_rel(args.salida / nombre)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
