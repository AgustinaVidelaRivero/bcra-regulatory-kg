"""
calibracion_roles_dev.py — U-ESQ-V3 fase 1: EJEMPLO TRABAJADO de la convención
vigente. Emite los 5 roles dev del grafo con sus 17 miembros, el nivel de cada
miembro y el pasaje del que salieron, para que las 30 filas nuevas se
adjudiquen contra la misma vara y no contra una inventada acá.

Los pasajes se leen de los chunks del subset de desarrollo
(escalado_prep/e0_dry_subset_ref/<to>/chunks_<to>.json) buscando la unidad que
declara el `provenance.location` del rol en esquema_v2_clases.json. Cuando la
location apunta a varias unidades («Secciones 1 y 10») se emiten las unidades
de apertura de cada una. Solo lectura; USD 0.

Uso:  python3 calibracion_roles_dev.py [--out DIR]
Escribe: calibracion_roles_dev.md
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import comun_v3m as C

SUBSET = C.EXPERIMENT / "escalado_prep" / "e0_dry_subset_ref"

# archivo del TO → id corto del subset
TO_DE_ARCHIVO = {
    "TO_proteccion_usuarios_servicios_financieros_actual.pdf": "pro",
    "TO_exterior_cambios_actual.pdf": "ext",
    "TO_clasificacion_deudores_actual.pdf": "cla",
    "TO_regimen_informativo_contable_mensual_actual.pdf": "ric",
    "TO_capitales_minimos_actual.pdf": "cap",
}

# location del rol → unidades E0 que la materializan (una location como
# «Secciones 1 y 10» cubre más de una unidad; se citan las de apertura).
UNIDADES_DE_LOCATION = {
    # El punto 1.1.2 de pro no es una unidad E0: son sus siete subpuntos, y
    # cada uno enumera uno de los siete miembros. Se citan los siete.
    ("pro", "Punto 1.1.2"): ["1.1.2.1", "1.1.2.2", "1.1.2.3", "1.1.2.4",
                             "1.1.2.5", "1.1.2.6", "1.1.2.7"],
    ("ext", "Punto 1.1"): ["1.1"],
    ("cla", "Secciones 1 y 10"): ["1.1", "10.1"],
    ("ric", "Sección 2"): ["S2"],
    ("cap", "Sección 1"): ["1.1"],
}


def _chunks(to: str) -> list[dict]:
    return json.loads((SUBSET / to / f"chunks_{to}.json").read_text(encoding="utf-8"))


def _busca(chs: list[dict], unidad: str) -> dict | None:
    """Chunk de la unidad pedida; si esa unidad se subdividió en mini_chunks,
    el de apertura. Si no existe, el primer chunk cuyo `unidad` la prefija."""
    for c in chs:
        if c.get("unidad") == unidad and c.get("rol_bloque") in (None, "intro"):
            return c
    for c in chs:
        if c.get("unidad") == unidad:
            return c
    for c in chs:
        u = c.get("unidad") or ""
        if u == unidad or u.startswith(unidad + "."):
            return c
    return None


def construir() -> dict:
    esq = C.esquema_v2()
    nivel = {c["id"]: c["nivel"] for c in esq["clases"]}
    filas = []
    for rol in esq["roles"]:
        to = TO_DE_ARCHIVO[rol["to"]]
        loc = rol["provenance"]["location"]
        chs = _chunks(to)
        pasajes = []
        for u in UNIDADES_DE_LOCATION[(to, loc)]:
            ch = _busca(chs, u)
            if ch:
                pasajes.append({"chunk_id": ch["id"], "titulo": ch["titulo"],
                                "paginas": ch["paginas"], "texto": ch["texto"]})
        filas.append({
            "rol_id": rol["id"], "label": rol["label"], "to": rol["to"], "to_corto": to,
            "location": loc,
            "miembros": [{"id": m, "nivel": nivel.get(m, "AUSENTE")} for m in rol["miembros"]],
            "pasajes": pasajes,
        })
    return {"roles": filas,
            "total_miembros": sum(len(f["miembros"]) for f in filas),
            "por_nivel": {n: sum(1 for f in filas for m in f["miembros"]
                                 if m["nivel"] == n)
                          for n in sorted({m["nivel"] for f in filas
                                           for m in f["miembros"]})}}


def render_md(d: dict) -> str:
    desglose = " + ".join(str(len(f["miembros"])) for f in d["roles"])
    L = [
        "# U-ESQ-V3 fase 1 — Calibración: los 5 roles dev y sus 17 miembros",
        "",
        "Ejemplo trabajado de **la convención que el grafo vigente ya aplica**. Las 30 filas nuevas "
        "se adjudican contra esta vara.",
        "",
        f"Miembros: **{desglose} = {d['total_miembros']}**, que son exactamente las "
        f"{d['total_miembros']} aristas `miembro_de` del grafo vigente. "
        f"Por nivel: {d['por_nivel']} — **los {d['total_miembros']} son de nivel `clase`; "
        "ninguno es instancia**. Ese hecho es el que fija la segunda cláusula de S15.",
        "",
        "Fuente de los miembros: `data/experiment/grafo_v2/esquema_v2_clases.json` (SELLADO, solo "
        "lectura). Fuente de los pasajes: "
        "`data/experiment/escalado_prep/e0_dry_subset_ref/<to>/chunks_<to>.json`.",
        "",
        "| rol_id | label | miembros | niveles | location |",
        "|---|---|---:|---|---|",
    ]
    for f in d["roles"]:
        niveles = ", ".join(sorted({m["nivel"] for m in f["miembros"]}))
        L.append(f"| `{f['rol_id']}` | {f['label']} | {len(f['miembros'])} | {niveles} | "
                 f"{f['location']} |")
    L += ["", "## Rol por rol, con el pasaje del que salieron los miembros", ""]
    for f in d["roles"]:
        L += [f"### `{f['rol_id']}` — {f['label']}",
              f"**TO:** {f['to']} · **location declarada:** {f['location']}", "",
              "**Miembros adjudicados:**", ""]
        for m in f["miembros"]:
            L.append(f"- `{m['id']}` — nivel `{m['nivel']}`")
        L += ["", "**Pasaje(s):**", ""]
        for p in f["pasajes"]:
            L += [f"`{p['chunk_id']}` · página(s) {p['paginas']} · «{p['titulo']}»", "",
                  "```", p["texto"].strip(), "```", ""]
    L += [
        "## Lectura de la calibración (lo que la vara dice y lo que no)",
        "",
        "1. **La granularidad es la del pasaje.** `Sujeto_rol_sujeto_obligado_proteccion` tiene 7 "
        "miembros porque el punto 1.1.2 enumera siete colectivos; no se expandió a las subclases "
        "de entidad financiera ni se colapsó a `Sujeto_sujeto_regulado`.",
        "2. **Un pasaje de un solo colectivo da un solo miembro.** Es el caso de reginf y capmin: "
        "un miembro cada uno, no una lista de conveniencia.",
        "3. **Todos los miembros vigentes son clases.** No hay precedente de instancia como "
        "miembro de un rol — lo que no significa que esté prohibido, sino que **adjudicar la "
        "primera instancia sería estrenar la convención**, y por eso las filas con candidato "
        "`instancia` van marcadas en la tabla de adjudicación.",
        "4. **El rol se queda con lo que el pasaje nombra.** Ningún rol dev tiene miembros que su "
        "pasaje no mencione.",
        "5. **HAY precedente vigente de recorte absorbido, y conviene tenerlo a la vista al "
        "adjudicar las filas `mas_amplio`.** Dos de los siete subpuntos de pro traen un recorte "
        "que el miembro adjudicado no porta: `pro::1.1.2.3` dice «Fiduciarios de fideicomisos "
        "**acreedores de créditos cedidos por entidades financieras**» y el miembro es "
        "`Sujeto_fiduciario_de_fideicomiso_financiero` a secas; `pro::1.1.2.5` dice «Otros "
        "proveedores no financieros de crédito […] **excepto que se trate de asociaciones mutuales "
        "o cooperativas**» y el miembro es `Sujeto_proveedor_no_financiero_de_credito` entero. "
        "Es decir: cuando el catálogo no tiene id para el recorte, la convención vigente adjudicó "
        "**la clase más cercana que el catálogo sí tiene, sin fabricar id nuevo** — y el recorte "
        "quedó donde estaba, en el texto de la norma, alcanzable por procedencia. Esto no "
        "convierte el aplanamiento en la respuesta correcta por defecto, pero sí muestra que el "
        "grafo vigente ya lo hace en 2 de 17 miembros, y la decisión sobre las 8 filas "
        "`mas_amplio` de la tabla nueva se toma sabiéndolo.",
        "",
    ]
    return "\n".join(L) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, default=C.UNIDAD)
    args = ap.parse_args()
    d = construir()
    (args.out / "calibracion_roles_dev.md").write_text(render_md(d), encoding="utf-8")
    print(f"roles dev: {len(d['roles'])} | miembros: {d['total_miembros']} | "
          f"por nivel: {d['por_nivel']}")
    print(f"-> {args.out / 'calibracion_roles_dev.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
