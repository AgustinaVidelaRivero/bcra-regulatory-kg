"""
generalizacion_catalogo.py — U-ESQ-V3: entregable nombrado de la unidad.

QUÉ MIDE. Cuántos de los 69 colectivos de alcance que nombran los 30 TOs
frescos tienen id de clase VERAZ en un catálogo derivado de 5 TOs de
desarrollo. «Veraz» = el id existe, es de nivel clase, y no aplana al
colectivo a su clase madre: lo que sobrevive a los laudos (a) y (b).

POR QUÉ SE GENERA CON CÓDIGO. La cifra viaja al plan y al capítulo. Un
entregable regenerado a mano deriva en cuanto una adjudicación cambia — ya
pasó una vez en esta unidad: el desglose quedó en la base de 33 después de
que el rescate de convca moviera el titular a 34, y la suma dejó de cerrar.
El comando de regeneración va DENTRO del propio artefacto para que cualquiera
recompute sin preguntar.

LAS TRES CIFRAS SE CONSERVAN, ROTULADAS. La diferencia entre ellas ES el
registro de la adjudicación: 33 es la base sin rescates, 34 la ADOPTADA
(convca aceptado como enumeración parcial), 35 la que habría dado si `ctacor`
hubiera sobrevivido a la verificación — y no sobrevivió.

EL DESCARTE SE PUBLICA PARTIDO EN DOS, porque son problemas opuestos con
remedios opuestos: falta el concepto en el catálogo (remedio mecánico: abrir
ids, re-sello del prefijo) contra granularidad equivocada (remedio: modelado).
Sin ese corte, «49,3 % generaliza» esconde lo único que la cifra tiene para
decir, que es dónde está el hueco.

Uso:  python3 generalizacion_catalogo.py [--out DIR]
Escribe: generalizacion_catalogo_v3.md (+ .json)
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import comun_v3m as C

COMANDO = ("cd data/experiment/esq_v3_miembros/code && "
           "python3 generalizacion_catalogo.py")

# Escenarios: qué rescates de filas `mas_amplio` se aceptan en cada uno.
ESCENARIOS = [
    ("base_sin_rescates", frozenset(), "base, sin ningún rescate", False),
    ("adoptada", frozenset({"convca"}), "ADOPTADA — convca aceptado como enumeración "
     "parcial (laudo a.2); ctacor rechazado (su re-examinación no reprodujo)", True),
    ("si_ctacor_hubiera_sobrevivido", frozenset({"convca", "ctacor"}),
     "contrafáctico: si ctacor hubiera sobrevivido a la verificación", False),
]


def _colectivos() -> list[tuple[str, dict]]:
    d = json.loads((C.UNIDAD / "candidatos_miembros_v3.json").read_text(encoding="utf-8"))
    return [(r["to"], c) for r in d["roles"] for c in r["candidatos"]]


def _clasificar(to: str, c: dict, rescates: frozenset) -> str:
    """Destino de un colectivo bajo los laudos (a) y (b) con estos rescates."""
    if not c["candidato_id"]:
        return "sin_id_en_catalogo"
    if c["nivel_candidato"] == "instancia":
        return "instancia_rechazada"
    if c["relacion"] == "mas_amplio":
        return "veraz" if to in rescates else "aplanamiento_rechazado"
    return "veraz"


def medir() -> dict:
    cs = _colectivos()
    total = len(cs)
    out = {}
    for clave, rescates, rotulo, adoptada in ESCENARIOS:
        d = {}
        for to, c in cs:
            d.setdefault(_clasificar(to, c, rescates), []).append((to, c["colectivo"]))
        veraz = len(d.get("veraz", []))
        sin_id = len(d.get("sin_id_en_catalogo", []))
        apl = len(d.get("aplanamiento_rechazado", []))
        inst = len(d.get("instancia_rechazada", []))
        descarte = sin_id + apl + inst
        out[clave] = {
            "rotulo": rotulo, "adoptada": adoptada,
            "veraz": veraz, "total": total,
            "porcentaje": round(100 * veraz / total, 1),
            "descarte_total": descarte,
            "ausencia_de_concepto": sin_id,
            "granularidad_equivocada": apl + inst,
            "granularidad_detalle": {"aplanamiento_rechazado": apl,
                                     "instancia_rechazada": inst},
            "pct_ausencia": round(100 * sin_id / descarte, 1) if descarte else 0.0,
            "pct_granularidad": round(100 * (apl + inst) / descarte, 1) if descarte else 0.0,
            "control_descarte": f"{sin_id} + {apl} + {inst} = {descarte}",
            "control_total": f"{veraz} + {descarte} = {veraz + descarte}",
            "cierra": veraz + descarte == total,
        }
    return {"unidad": "U-ESQ-V3", "comando": COMANDO,
            "denominador": total, "escenarios": out}


def render_md(m: dict) -> str:
    ad = next(v for v in m["escenarios"].values() if v["adoptada"])
    L = [
        "# U-ESQ-V3 — Generalización del catálogo de sujetos a TOs frescos",
        "",
        "**Entregable nombrado de la unidad.** Se REGENERA, no se edita a mano:",
        "",
        "```bash",
        m["comando"],
        "```",
        "",
        "## Qué mide",
        "",
        f"Cuántos de los **{m['denominador']}** colectivos de alcance que nombran los 30 TOs "
        "frescos del escalado tienen **id de clase veraz** en un catálogo derivado de 5 TOs de "
        "desarrollo. «Veraz» = el id existe, es de nivel `clase`, y **no aplana** al colectivo a "
        "su clase madre: lo que sobrevive a los laudos (a) y (b).",
        "",
        "## La cifra",
        "",
        f"# {ad['veraz']}/{ad['total']} = {ad['porcentaje']} %",
        "",
        "## Las tres cifras, rotuladas",
        "",
        "La diferencia entre ellas **es** el registro de la adjudicación.",
        "",
        "| escenario | cifra | % | descarte | ausencia de concepto | granularidad equivocada |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for v in m["escenarios"].values():
        marca = " **← ADOPTADA**" if v["adoptada"] else ""
        L.append(f"| {v['rotulo']}{marca} | {v['veraz']}/{v['total']} | {v['porcentaje']} % | "
                 f"{v['descarte_total']} | {v['ausencia_de_concepto']} "
                 f"({v['pct_ausencia']} %) | {v['granularidad_equivocada']} "
                 f"({v['pct_granularidad']} %) |")
    L += ["", "### Desglose de cada escenario, con su control", ""]
    for v in m["escenarios"].values():
        L += [f"**{v['rotulo']}** — {v['veraz']}/{v['total']} = {v['porcentaje']} %", "",
              f"- descarte por ausencia de concepto (sin id en el catálogo): "
              f"**{v['ausencia_de_concepto']}**",
              f"- descarte por granularidad equivocada: **{v['granularidad_equivocada']}** "
              f"({v['granularidad_detalle']['aplanamiento_rechazado']} aplanamiento rechazado + "
              f"{v['granularidad_detalle']['instancia_rechazada']} candidato de nivel instancia)",
              f"- control del descarte: `{v['control_descarte']}`",
              f"- control del total: `{v['control_total']}` sobre {v['total']} — "
              f"cierra: **{v['cierra']}**", ""]
    L += [
        "## El descarte, partido en dos (lo que la cifra tiene para decir)",
        "",
        "Sobre la cifra adoptada, el hueco **no es homogéneo**: son dos problemas opuestos con "
        "remedios opuestos, y publicar un cubo único los esconde.",
        "",
        "| naturaleza del hueco | n | % del descarte | remedio |",
        "|---|---:|---:|---|",
        f"| **ausencia de concepto en el catálogo** | {ad['ausencia_de_concepto']} | "
        f"{ad['pct_ausencia']} % | abrir ids — mecánico, re-sello del prefijo v3 |",
        f"| **granularidad equivocada** | {ad['granularidad_equivocada']} | "
        f"{ad['pct_granularidad']} % | modelado (una clase más específica, o la firma de "
        "`miembro_de`) |",
        f"| control | {ad['descarte_total']} | 100 % | `{ad['control_descarte']}` |",
        "",
        f"**Casi tres cuartos del hueco ({ad['pct_ausencia']} %) son cobertura, no modelado.** "
        "Un catálogo derivado de 5 TOs no conoce las transportadoras de valores, las "
        "infraestructuras del mercado financiero ni las plataformas de financiamiento MiPyME "
        "sencillamente porque esos 5 TOs no las mencionan; abrirles id es trabajo mecánico. El "
        "cuarto restante es distinto: ahí el concepto existe y lo que falla es a qué "
        "granularidad se lo modeló.",
        "",
        "## Advertencia que viaja con la cifra",
        "",
        "**NO es comparable con el 96,9 % de cobertura del catálogo que ya está en el tramo 2 "
        "del capítulo (`main.tex:679`).** Difieren en cuatro cosas:",
        "",
        "1. **Denominador:** 4.029 relaciones con sujeto EMITIDAS, contra "
        f"{m['denominador']} colectivos NOMBRADOS en cláusulas de alcance.",
        "2. **Unidad:** una mención individual, contra un colectivo — que muchas veces es una "
        "unión de varios sujetos.",
        "3. **Material:** desarrollo más los diez de cobertura, contra 30 TOs frescos del "
        "escalado.",
        "4. **Y el que muerde:** el 96,9 % cuenta lo que el extractor **eligió emitir**. Un "
        "colectivo sin id puede no llegar nunca a producir una relación con sujeto y caer fuera "
        "de ese denominador — **la cifra baja puede explicar en parte por qué la alta es alta**.",
        "",
        "**Las dos cifras no van juntas en el capítulo sin este párrafo.**",
        "",
    ]
    return "\n".join(L) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, default=C.UNIDAD)
    args = ap.parse_args()
    m = medir()
    for v in m["escenarios"].values():
        if not v["cierra"]:
            print(f"FRENO: el escenario {v['rotulo']!r} no cierra: {v['control_total']}")
            return 1
    (args.out / "generalizacion_catalogo_v3.json").write_text(
        json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")
    (args.out / "generalizacion_catalogo_v3.md").write_text(render_md(m), encoding="utf-8")
    for k, v in m["escenarios"].items():
        marca = "  <- ADOPTADA" if v["adoptada"] else ""
        print(f"  {k:32s} {v['veraz']}/{v['total']} = {v['porcentaje']:.1f} %  | "
              f"descarte {v['control_descarte']} | ausencia {v['ausencia_de_concepto']} "
              f"({v['pct_ausencia']} %) / granularidad {v['granularidad_equivocada']} "
              f"({v['pct_granularidad']} %){marca}")
    print(f"-> {args.out / 'generalizacion_catalogo_v3.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
