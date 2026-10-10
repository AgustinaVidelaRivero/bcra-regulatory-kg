"""
c3_cifras.py — U-CONF-MATRIZ, C3 (mandato FIRMADO en 90addb35, §2, §5 y §7): las cifras por par y la lista para la autora, a
partir del acta sellada (c1/acta_c1.json) y la planilla sellada (c2/planilla_c2.jsonl). USD 0.

  Por par: correctas, incorrectas y no decidibles; Wilson al 95 % (z = 1,959964, como reext_t0/t4/tasas_t4.py:244-249) de
  correctas / (correctas + incorrectas); si el límite inferior es ≥ 0,75 el par se confirma; con más de 6 no decidibles el par no
  se decide con esta muestra (§2). Además, el mínimo de correctas que el piso pide con ese número de decididas.
  Lista para la autora (§5): las incorrectas, las no decidibles y 5 correctas por par, sorteadas entre las correctas del par
  ordenadas por (origen, destino) con random.Random(semilla de revisión del par).sample(lista, 5); si son menos de 5, van todas.
  Las semillas de revisión se recalculan desde el texto firmado (como en c1_acta.py) y se comparan con las asentadas.

Corre desde la raíz de una COPIA del repo (CLAUDE.md §4.l) y escribe solo en --salida: cifras_c3.json, lista_autora_c3.md.
  PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B data/experiment/conf_matriz/c3_cifras.py --salida DIR
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
import sys
from math import sqrt
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ACTA = AQUI / "c1" / "acta_c1.json"
FICHAS = AQUI / "c1" / "fichas_c1.jsonl"
PLANILLA = AQUI / "c2" / "planilla_c2.jsonl"
ACTA_SHA256 = "f5990dff532e6ca2c9eb91e4f8db7e98be105da517e1071c7b8ddc14c8926602"       # c1/sello_acta_c1.txt
FICHAS_SHA256 = "ebe7dd72bcd04b8c1781c1756f4048540d432c458adb35af7cf328bb17d3e8a3"     # c1/sello_fichas_c1.txt
PLANILLA_SHA256 = "bd2824135e2170342f8e812436fc6df08ed2b8b2cdce372ea77d784aa6bcf9ab"   # c2/sello_planilla_c2.txt
PARES = ("Operacion", "Potestad")
Z = 1.959964
PISO = 0.75
MAX_NO_DECIDIBLES = 6
N_REVISION = 5


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def wilson(k: int, n: int) -> list[float]:
    p = k / n
    den = 1 + Z * Z / n
    centro = (p + Z * Z / (2 * n)) / den
    medio = Z * sqrt(p * (1 - p) / n + Z * Z / (4 * n * n)) / den
    return [round(max(0.0, centro - medio), 4), round(min(1.0, centro + medio), 4)]


def wilson_inf(k: int, n: int) -> float:
    p = k / n
    den = 1 + Z * Z / n
    return (p + Z * Z / (2 * n) - Z * sqrt(p * (1 - p) / n + Z * Z / (4 * n * n))) / den


def minimo_correctas(n: int) -> int | None:
    return next((k for k in range(n + 1) if wilson_inf(k, n) >= PISO), None)


def semilla(uso: str, texto_sha: str) -> int:
    return int(sha(("U-CONF-MATRIZ|" + uso + "|" + texto_sha).encode())[:16], 16)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()

    for p, s in ((ACTA, ACTA_SHA256), (FICHAS, FICHAS_SHA256), (PLANILLA, PLANILLA_SHA256)):
        if sha(p.read_bytes()) != s:
            raise SystemExit(f"{p.name} distinto del sellado")
    acta = json.loads(ACTA.read_text(encoding="utf-8"))
    texto_sha = acta["mandato"]["sha256_texto_firmado"]
    semillas = {par: semilla("revision|" + par, texto_sha) for par in PARES}
    if any(str(semillas[par]) != acta["sorteo"]["semillas"]["revision|" + par] for par in PARES):
        raise SystemExit("semillas de revisión distintas de las asentadas")
    fichas_acta = {f["ficha"]: f for f in acta["orden_de_lectura"]["fichas"]}
    fichas = {json.loads(x)["ficha"]: json.loads(x) for x in FICHAS.read_text(encoding="utf-8").splitlines() if x.strip()}
    planilla = {json.loads(x)["ficha"]: json.loads(x) for x in PLANILLA.read_text(encoding="utf-8").splitlines() if x.strip()}
    if set(planilla) != set(fichas_acta):
        raise SystemExit("planilla y acta no coinciden")

    cifras, revision = {}, {}
    for par in PARES:
        del_par = sorted((f for f in fichas_acta.values() if f["par"] == par), key=lambda f: (f["origen"], f["destino"]))
        marcas = {m: [f["ficha"] for f in del_par if planilla[f["ficha"]]["marca"] == m]
                  for m in ("correcta", "incorrecta", "no_decidible")}
        c, i, nd = (len(marcas[m]) for m in ("correcta", "incorrecta", "no_decidible"))
        n = c + i
        se_decide = nd <= MAX_NO_DECIDIBLES
        inf = wilson_inf(c, n) if n else None
        cifras[par] = {
            "muestra": len(del_par), "correctas": c, "incorrectas": i, "no_decidibles": nd, "decididas": n,
            "proporcion": f"{c}/{n}" if n else None,
            "wilson95": wilson(c, n) if n else None,
            "wilson95_inferior_sin_redondeo": inf,
            "minimo_de_correctas_para_el_piso_con_estas_decididas": minimo_correctas(n) if n else None,
            "se_decide_con_esta_muestra": se_decide,
            "cumple": (se_decide and inf is not None and inf >= PISO),
            "fichas_por_marca": marcas}
        correctas_ordenadas = [f["ficha"] for f in del_par if planilla[f["ficha"]]["marca"] == "correcta"]
        sorteadas = (random.Random(semillas[par]).sample(correctas_ordenadas, N_REVISION)
                     if len(correctas_ordenadas) > N_REVISION else list(correctas_ordenadas))
        revision[par] = {"semilla": str(semillas[par]),
                         "metodo": "random.Random(semilla).sample(correctas del par ordenadas por (origen, destino), 5)",
                         "correctas_ordenadas": correctas_ordenadas, "correctas_sorteadas": sorteadas,
                         "incorrectas": marcas["incorrecta"], "no_decidibles": marcas["no_decidible"]}

    anotadas = {par: [f for f in sorted(fichas_acta) if fichas_acta[f]["par"] == par and planilla[f]["marca"] == "correcta"
                      and planilla[f]["anotaciones"]] for par in PARES}
    out = {"unidad": "U-CONF-MATRIZ, C3 (cifras de la lectura; antes de la revisión de la autora)",
           "insumos": {"acta_sha256": ACTA_SHA256, "fichas_sha256": FICHAS_SHA256, "planilla_sha256": PLANILLA_SHA256,
                       "c3_cifras.py_sha256": sha(Path(__file__).read_bytes()), "python": sys.version.split()[0]},
           "criterio": {"piso_wilson_inferior": PISO, "z": Z, "max_no_decidibles": MAX_NO_DECIDIBLES},
           "cifras": cifras, "revision_de_la_autora": revision,
           "correctas_con_anotacion": anotadas}
    a.salida.mkdir(parents=True, exist_ok=True)
    (a.salida / "cifras_c3.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    # la lista para la autora, con cada ficha
    md = ["# U-CONF-MATRIZ, C3: lista para la revisión de la autora\n",
          "Mandato §5: las incorrectas, las no decidibles y 5 correctas por par, sorteadas con la semilla de revisión del par. "
          "Cada entrada lleva la marca y la nota de C2 y la ficha de C1. La autora adjudica las que no comparta (C4).\n"]
    for par in PARES:
        r = revision[par]
        md.append(f"## → {par}\n")
        md.append(f"Cifras de C2: {cifras[par]['correctas']} correctas, {cifras[par]['incorrectas']} incorrectas, "
                  f"{cifras[par]['no_decidibles']} no decidibles; Wilson 95 % {cifras[par]['wilson95']}.\n")
        grupos = (("Incorrectas", r["incorrectas"]), ("No decidibles", r["no_decidibles"]),
                  (f"Correctas sorteadas (semilla {r['semilla']})", r["correctas_sorteadas"]))
        for titulo, lista in grupos:
            md.append(f"### {titulo}: {len(lista)}\n")
            for fid in lista:
                fi, pl = fichas[fid], planilla[fid]
                u = fi["unidad"]
                md.append(f"#### {fid} — {pl['marca']}\n")
                md.append(f"- Nota de C2: {pl['nota']}")
                if pl["anotaciones"]:
                    md.append(f"- Anotaciones: {'; '.join(pl['anotaciones'])}")
                for rol in ("origen", "destino"):
                    b = fi[rol]
                    md.append(f"- {rol.capitalize()}: {b['tipo']} — «{b['etiqueta']}» (`{b['id']}`)")
                    md.append(f"  - descripción (salida del extractor): {b['descripcion_extractor']}")
                    md.append(f"  - tramo de E1 (salida del extractor): {b['tramo_e1']!r}")
                md.append(f"- Unidad `{u['chunk_id']}` ({u['to']}, punto {u['punto']}), páginas {u['paginas_unidad']}; PDF "
                          f"`{fi['pdf']}`; render " + ", ".join(f"`c1/{p}`" for p in fi["paginas_render"]))
                md.append("- Texto heredado: " + " / ".join(f"[{h['tipo']} {h['unidad_origen']}] {h['texto']}"
                                                            for h in u["herencia"]).replace("\n", " "))
                md.append("- Texto propio:\n\n```text\n" + u["texto_propio"] + "\n```\n")
    (a.salida / "lista_autora_c3.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(json.dumps({par: {k: cifras[par][k] for k in ("correctas", "incorrectas", "no_decidibles", "wilson95",
                                                        "se_decide_con_esta_muestra", "cumple")} for par in PARES}
                     | {"revision": {par: revision[par]["correctas_sorteadas"] for par in PARES}}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
