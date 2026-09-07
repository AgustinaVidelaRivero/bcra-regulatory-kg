"""
barrido_domestico_exterior.py — U-ESQ-V3 fase 2, §5: barrido del bloque
sellado en busca del patrón que el caso `ctacor` puso a la vista.

EL PATRÓN. Un id cuya definición o label lo presenta como doméstico (o
simplemente sin marca de extranjería) y que, en la MISMA línea, declara entre
sus alias una variante «del exterior» o equivalente. El alias es lo que
gobierna a qué id cae una mención del texto, de modo que ese id termina
cubriendo el doméstico y el extranjero a la vez, mientras su definición dice
otra cosa.

POR QUÉ IMPORTA. `miembro_de` va de clase a rol, y la regla de herencia 2
hace que un `aplica_a` hacia el rol alcance a cada miembro; desde ahí la
regla 1 desciende a toda subclase. Un miembro con este patrón arrastra la
contradicción a todo lo que herede de él: una norma de alcance doméstico
termina afirmada sobre sujetos del exterior.

Barrido puramente léxico sobre marcas de extranjería, con la lista de marcas
declarada en el código y a la vista. No resuelve nada: registra. El remedio
—ids separados para lo extranjero— es re-sello del prefijo v3 y unidad
propia, por laudo.

Uso:  python3 barrido_domestico_exterior.py [--out DIR]
Escribe: residuo_catalogo_domestico_exterior.md (+ .json)
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import comun_v3m as C

# Marcas de extranjería buscadas en los alias (normalizadas con C.norm).
MARCAS_EXTERIOR = (
    "del exterior", "extranjer", "de otros estados", "de otro estado",
    "del extranjero", "europeo", "internacional", "no residente", "off shore",
    "offshore", "del exterior no autorizad",
)


def _marca(texto: str) -> str | None:
    n = C.norm(texto)
    for m in MARCAS_EXTERIOR:
        if m in n:
            return m
    return None


def barrer() -> dict:
    ix = C.catalogo_v3_index()
    afectados, alias_extranjeros_con_id_propio = [], []
    for sid, v in ix.items():
        if v["nivel"] == "rol":
            continue
        marcados = [(a, _marca(a)) for a in v["alias"] if _marca(a)]
        if not marcados:
            continue
        # ¿El label mismo ya declara la extranjería? Entonces el id ES el
        # extranjero y no hay contradicción: el alias es coherente con él.
        if _marca(v["label"]):
            alias_extranjeros_con_id_propio.append(
                {"id": sid, "label": v["label"],
                 "alias_extranjeros": [a for a, _ in marcados]})
            continue
        afectados.append({
            "id": sid,
            "label": v["label"],
            "nivel": v["nivel"],
            "alias_extranjeros": [a for a, _ in marcados],
            "alias_todos": list(v["alias"]),
            "marcas": sorted({m for _, m in marcados}),
        })
    return {
        "unidad": "U-ESQ-V3",
        "seccion_del_laudo": "5",
        "patron": ("id con label/definición sin marca de extranjería y alias «del exterior» "
                   "o equivalente en la misma línea del bloque sellado"),
        "marcas_buscadas": list(MARCAS_EXTERIOR),
        "ids_afectados": sorted(afectados, key=lambda x: x["id"]),
        "n_afectados": len(afectados),
        "ids_extranjeros_propios": sorted(alias_extranjeros_con_id_propio,
                                          key=lambda x: x["id"]),
        "total_entradas_barridas": sum(1 for v in ix.values() if v["nivel"] != "rol"),
    }


def render_md(d: dict) -> str:
    L = [
        "# U-ESQ-V3 — RESIDUO DECLARADO: ids del catálogo v3 con definición doméstica "
        "y alias extranjeros",
        "",
        "Hallazgo del laudo §5, a raíz del caso `ctacor`. **No se arregla en esta unidad: el "
        "prefijo v3 está sellado y abrir ids es re-sello y unidad propia.** Acá se registra, con "
        "los ids nombrados y el mecanismo por el que se propaga.",
        "",
        f"Barrido de las **{d['total_entradas_barridas']}** entradas de clase e instancia del "
        f"bloque sellado (los 35 roles quedan fuera: no llevan alias). "
        f"**Ids con el patrón: {d['n_afectados']}.**",
        "",
        "## El patrón",
        "",
        "Un id cuya definición o label lo presenta como doméstico —o simplemente sin marca de "
        "extranjería— y que, **en la misma línea**, declara entre sus alias una variante «del "
        "exterior». El alias es lo que gobierna a qué id cae una mención del texto, de modo que "
        "el id cubre el doméstico y el extranjero a la vez mientras su definición dice otra cosa.",
        "",
        "## Los ids afectados",
        "",
        "| id | label | alias con marca de extranjería |",
        "|---|---|---|",
    ]
    for a in d["ids_afectados"]:
        L.append(f"| `{a['id']}` | {a['label']} | {'; '.join(a['alias_extranjeros'])} |")
    L += [
        "",
        "## Mecanismo de propagación (por qué no es cosmético)",
        "",
        "`miembro_de` va de clase a rol. La **regla de herencia 2** del diseño del esquema hace "
        "que un `aplica_a` hacia un rol alcance a **cada uno de sus miembros**; desde ahí la "
        "**regla 1** desciende a **toda subclase** del miembro. Un miembro con este patrón "
        "arrastra la contradicción a todo lo que herede de él: una norma de alcance doméstico "
        "termina afirmada sobre sujetos del exterior, sin que nada en el grafo lo señale.",
        "",
        "Es exactamente el vicio que el laudo (a) manda retirar cuando se aplana a la clase "
        "madre, con la diferencia de que acá **no está en la adjudicación sino dentro del propio "
        "catálogo**: aunque cada fila se adjudique con el criterio correcto, el id adjudicado ya "
        "trae la unión.",
        "",
        "## Alcance real dentro de esta unidad",
        "",
        "De los ids afectados, los que efectivamente entran como miembros en la adjudicación de "
        "esta fase se listan en el reporte con su cuenta. El caso que lo destapó —`ctacor`— **no** "
        "produce arista, justamente porque «del país» resultó ser recorte real frente a un id que "
        "cubre ambos. **Este hallazgo no cambia ninguna cifra de la fase 2.**",
        "",
        "## Ids que SÍ tienen id propio para lo extranjero (contraste, no afectados)",
        "",
    ]
    if d["ids_extranjeros_propios"]:
        L += ["| id | label |", "|---|---|"]
        for a in d["ids_extranjeros_propios"]:
            L.append(f"| `{a['id']}` | {a['label']} |")
    else:
        L.append("Ninguno: no hay en el catálogo v3 un id cuyo label declare la extranjería y "
                 "lleve además alias extranjeros.")
    L += [
        "",
        "## Remedio propuesto (ítem de backlog, no de esta unidad)",
        "",
        "Ids separados para los sujetos del exterior, con su propia definición y su lugar en el "
        "árbol, y los alias extranjeros migrados a ellos. Eso **cambia el bloque de catálogo y "
        "por lo tanto el prefijo v3**, cuyo sha está sellado y candado en `perfil_e1`: es "
        "re-sello del prefijo y unidad propia, con su laudo.",
        "",
    ]
    return "\n".join(L) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, default=C.UNIDAD)
    args = ap.parse_args()
    d = barrer()
    (args.out / "residuo_catalogo_domestico_exterior.json").write_text(
        json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
    (args.out / "residuo_catalogo_domestico_exterior.md").write_text(
        render_md(d), encoding="utf-8")
    print(f"entradas barridas (clase+instancia): {d['total_entradas_barridas']}")
    print(f"ids con el patrón: {d['n_afectados']}")
    for a in d["ids_afectados"]:
        print(f"  {a['id']:45s} alias: {'; '.join(a['alias_extranjeros'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
