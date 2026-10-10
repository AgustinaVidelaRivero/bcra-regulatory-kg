"""
c3_clases.py — U-CONF-MATRIZ, C3 (mandato FIRMADO en 90addb35, §7): insumos para la adjudicación de la autora en C4. USD 0.

  1. Sensibilidad de las cifras a la lectura de las correctas con anotación (planilla sellada, c2/planilla_c2.jsonl): cuánto
     cambia cada par si la autora adjudicara incorrectas las de una clase de anotación. Es informativa: no cambia el criterio ni
     las cifras de C2 (c3/cifras_c3.json).
  2. Señales de código de las clases propuestas, medidas sobre la población entera (las 907 aristas del acta), sin leer: cada
     arista que la señal marca se lista con su unidad, sus páginas y si fue leída en C2 (ficha) o no («sin leer»).
     - circular: el tramo de E1 del destino, normalizado, está contenido en el de la Condicion;
     - indiferencia: la etiqueta, la descripción o el tramo de la Condicion dicen «o no», «con o sin» o «indiferente»;
     - regla de plazo: la descripción o la etiqueta de la Condicion dicen «se regirá», «se rige», «se aplica(rá) el plazo» o
       «el plazo será» (señal construida sobre el caso leído).
     Normalización: NFKD a ASCII, minúsculas, todo lo que no es letra, dígito o espacio pasa a espacio, espacios colapsados.

  3. El anexo de la sensibilidad: las fichas del escenario más amplio, completas, para que la autora pueda leerlas en C4 aunque
     no estén en la lista del §5 (no la amplía: es informativo).

Corre desde la raíz de una COPIA del repo (CLAUDE.md §4.l) y escribe solo en --salida: clases_c3.json, clases_c3.md y
anexo_sensibilidad_c3.md.
  PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B data/experiment/conf_matriz/c3_clases.py --salida DIR
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import unicodedata
from pathlib import Path

from c3_cifras import PISO, wilson, wilson_inf  # mismo Wilson y piso que las cifras (misma carpeta)

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[2]
KG = REPO / "data" / "experiment" / "reextraccion_v2" / "corpus_tanda0" / "ens_diez_r2b_sincola" / "r2" / "kg.json"
ACTA = AQUI / "c1" / "acta_c1.json"
PLANILLA = AQUI / "c2" / "planilla_c2.jsonl"
FICHAS = AQUI / "c1" / "fichas_c1.jsonl"
FICHAS_SHA256 = "ebe7dd72bcd04b8c1781c1756f4048540d432c458adb35af7cf328bb17d3e8a3"
CIFRAS = AQUI / "c3" / "cifras_c3.json"
ACTA_SHA256 = "f5990dff532e6ca2c9eb91e4f8db7e98be105da517e1071c7b8ddc14c8926602"
PLANILLA_SHA256 = "bd2824135e2170342f8e812436fc6df08ed2b8b2cdce372ea77d784aa6bcf9ab"
PARES = ("Operacion", "Potestad")
# escenarios acumulativos: prefijos de anotación que se pasarían a «incorrecta»
ESCENARIOS = (("circular", ("circular",)),
              ("circular + alcance", ("circular", "alcance")),
              ("circular + alcance + consecuencia fuera de la arista",
               ("circular", "alcance", "consecuencia fuera de la arista")))
SENALES = {
    "circular": "el tramo del destino, normalizado, está contenido en el de la Condicion",
    "indiferencia": "la Condicion dice «o no», «con o sin» o «indiferente»",
    "regla de plazo": "la Condicion dice «se regirá», «se rige», «se aplica(rá) el plazo» o «el plazo será»",
}


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def norm(s: str | None) -> str:
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return " ".join(re.sub(r"[^a-z0-9 ]+", " ", s).split())


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()

    for p, s in ((ACTA, ACTA_SHA256), (PLANILLA, PLANILLA_SHA256), (FICHAS, FICHAS_SHA256)):
        if sha(p.read_bytes()) != s:
            raise SystemExit(f"{p.name} distinto del sellado")
    acta = json.loads(ACTA.read_text(encoding="utf-8"))
    raw = KG.read_bytes()
    if sha(raw) != acta["grafo"]["kg_sha256"]:
        raise SystemExit("kg.json distinto del sellado")
    kg = json.loads(raw)
    nodos = {n["id"]: n for n in kg["nodes"]}
    aristas = {(e["source"], e["target"]): e for e in kg["edges"] if e["relation"] == "condicion_de"}
    fichas = acta["orden_de_lectura"]["fichas"]
    par_de = {f["ficha"]: f["par"] for f in fichas}
    ficha_de = {(f["origen"], f["destino"]): f["ficha"] for f in fichas}
    planilla = {json.loads(x)["ficha"]: json.loads(x) for x in PLANILLA.read_text(encoding="utf-8").splitlines() if x.strip()}
    cifras = json.loads(CIFRAS.read_text(encoding="utf-8"))["cifras"]

    # 1. sensibilidad
    sens = []
    for nombre, prefijos in ESCENARIOS:
        pasan = sorted(f for f, r in planilla.items() if r["marca"] == "correcta"
                       and any(an.startswith(pr) for an in r["anotaciones"] for pr in prefijos))
        fila = {"escenario": nombre, "fichas_que_pasarian_a_incorrecta": pasan, "por_par": {}}
        for par in PARES:
            c = cifras[par]["correctas"] - sum(1 for f in pasan if par_de[f] == par)
            n = cifras[par]["decididas"]
            fila["por_par"][par] = {"correctas": c, "decididas": n, "wilson95": wilson(c, n),
                                    "cumpliria": wilson_inf(c, n) >= PISO}
        sens.append(fila)

    # 2. señales sobre la población
    def tramo(nodo: dict, cid: str) -> str | None:
        return next(p.get("tramo") for p in nodo["provenances"] if p["chunk_id"] == cid)

    casos = {k: [] for k in SENALES}
    for par in PARES:
        for o, d, cid in acta["poblacion"][par]["filas"]:
            no, nd = nodos[o], nodos[d]
            to, td = norm(tramo(no, cid)), norm(tramo(nd, cid))
            texto_c = " ".join((norm(no["label"]), norm(no["properties"].get("descripcion")), to))
            marca = {"circular": bool(td) and td in to,
                     "indiferencia": bool(re.search(r"\b(o no|con o sin|indiferente)\b", texto_c)),
                     "regla de plazo": bool(re.search(r"\b(se regira|se rige|se aplica el plazo|se aplicara el plazo|"
                                                      r"el plazo sera)\b",
                                                      norm(no["properties"].get("descripcion")) + " " + norm(no["label"])))}
            for k, v in marca.items():
                if v:
                    f = ficha_de.get((o, d))
                    casos[k].append({"par": par, "origen": o, "destino": d, "unidad": cid,
                                     "paginas": aristas[(o, d)]["provenance"]["paginas"],
                                     "etiqueta_origen": no["label"], "etiqueta_destino": nd["label"],
                                     "lectura": (f"leída en C2 ({f}, {planilla[f]['marca']})" if f else "sin leer")})
    out = {"insumos": {"acta_sha256": ACTA_SHA256, "planilla_sha256": PLANILLA_SHA256, "kg_sha256": sha(raw),
                       "c3_clases.py_sha256": sha(Path(__file__).read_bytes())},
           "sensibilidad": sens,
           "senales": {k: {"definicion": SENALES[k], "aristas": len(v),
                           "por_par": {p: sum(1 for x in v if x["par"] == p) for p in PARES}, "casos": v}
                       for k, v in casos.items()}}
    a.salida.mkdir(parents=True, exist_ok=True)
    (a.salida / "clases_c3.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    md = ["# U-CONF-MATRIZ, C3: sensibilidad y señales de las clases (insumo de C4)\n",
          "## Sensibilidad a la lectura de las correctas con anotación\n",
          "Informativa: no cambia el criterio ni las cifras de C2. Cada escenario pasa a «incorrecta» las correctas cuya "
          "anotación empieza como se indica.\n",
          "| escenario | fichas | → Operacion | → Potestad |", "|---|---|---|---|",
          f"| C2, sellado | — | {cifras['Operacion']['proporcion']}, Wilson {cifras['Operacion']['wilson95']} | "
          f"{cifras['Potestad']['proporcion']}, Wilson {cifras['Potestad']['wilson95']} |"]
    for s in sens:
        celdas = [f"{s['por_par'][p]['correctas']}/{s['por_par'][p]['decididas']}, Wilson {s['por_par'][p]['wilson95']}, "
                  f"{'cumpliría' if s['por_par'][p]['cumpliria'] else 'no cumpliría'}" for p in PARES]
        md.append(f"| {s['escenario']} | {', '.join(s['fichas_que_pasarian_a_incorrecta'])} | {celdas[0]} | {celdas[1]} |")
    md.append("\n## Señales de código sobre la población (907 aristas), caso por caso\n")
    for k, v in casos.items():
        por_par = ", ".join(f"{p} {out['senales'][k]['por_par'][p]}" for p in PARES)
        md.append(f"### {k}: {len(v)} aristas ({por_par})\n")
        md.append(f"Señal: {SENALES[k]}.\n")
        md.append("| par | unidad | páginas | origen | destino | lectura |")
        md.append("|---|---|---|---|---|---|")
        for x in v:
            md.append(f"| {x['par']} | `{x['unidad']}` | {x['paginas']} | {x['etiqueta_origen']} | {x['etiqueta_destino']} | "
                      f"{x['lectura']} |")
        md.append("")
    (a.salida / "clases_c3.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    # 3. anexo: las fichas del escenario más amplio
    fichas_c1 = {json.loads(x)["ficha"]: json.loads(x) for x in FICHAS.read_text(encoding="utf-8").splitlines() if x.strip()}
    anexo = ["# U-CONF-MATRIZ, C3: anexo de la sensibilidad (fuera de la lista del §5; informativo)\n",
             "Las correctas con anotación cuyo pase a «incorrecta» cambiaría el resultado de algún par (tabla de "
             "`clases_c3.md`). Cada entrada lleva la marca, la nota y las anotaciones de C2 y la ficha de C1.\n"]
    for fid in sens[-1]["fichas_que_pasarian_a_incorrecta"]:
        fi, pl = fichas_c1[fid], planilla[fid]
        u = fi["unidad"]
        anexo.append(f"## {fid} — {pl['marca']} (→ {par_de[fid]})\n")
        anexo.append(f"- Nota de C2: {pl['nota']}")
        anexo.append(f"- Anotaciones: {'; '.join(pl['anotaciones'])}")
        for rol in ("origen", "destino"):
            b = fi[rol]
            anexo.append(f"- {rol.capitalize()}: {b['tipo']} — «{b['etiqueta']}» (`{b['id']}`)")
            anexo.append(f"  - descripción (salida del extractor): {b['descripcion_extractor']}")
            anexo.append(f"  - tramo de E1 (salida del extractor): {b['tramo_e1']!r}")
        anexo.append(f"- Unidad `{u['chunk_id']}` ({u['to']}, punto {u['punto']}), páginas {u['paginas_unidad']}; PDF "
                     f"`{fi['pdf']}`; render " + ", ".join(f"`c1/{p}`" for p in fi["paginas_render"]))
        anexo.append("- Texto heredado: " + " / ".join(f"[{h['tipo']} {h['unidad_origen']}] {h['texto']}"
                                                     for h in u["herencia"]).replace("\n", " "))
        anexo.append("- Texto propio:\n\n```text\n" + u["texto_propio"] + "\n```\n")
    (a.salida / "anexo_sensibilidad_c3.md").write_text("\n".join(anexo) + "\n", encoding="utf-8")
    print(json.dumps({"sensibilidad": [{s["escenario"]: {p: s["por_par"][p] for p in PARES}} for s in sens],
                      "senales": {k: out["senales"][k]["por_par"] for k in SENALES}}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
