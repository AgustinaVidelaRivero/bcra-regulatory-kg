"""
c2_sello.py — U-CONF-MATRIZ, C2 (mandato FIRMADO en 90addb35, §2 y §5): valida la planilla de la lectura y la deja lista para
el sello, sin calcular ninguna cifra. USD 0.

  Entrada: la planilla de la lectura (una fila por ficha: ficha, marca, nota, anotaciones, páginas vistas), escrita a mano por la
  sesión lectora contra c1/fichas_c1.md y las páginas renderizadas.
  Controles: las 60 fichas del acta sellada (c1/acta_c1.json), sin repetir ni faltar; marca en {correcta, incorrecta,
  no_decidible}; nota no vacía en toda marca que no sea «correcta» (§2 del mandato); páginas vistas entre las renderizadas.
  Salida: c2/planilla_c2.jsonl (las filas, ordenadas por ficha) y c2/planilla_c2.md (la misma planilla legible, con las reglas de
  lectura). No escribe el par de ninguna ficha ni cuenta marcas: eso es C3.

Corre desde la raíz de una COPIA del repo (CLAUDE.md §4.l).
  PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B data/experiment/conf_matriz/c2_sello.py --planilla FILAS.jsonl --salida DIR
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ACTA = AQUI / "c1" / "acta_c1.json"
ACTA_SHA256 = "f5990dff532e6ca2c9eb91e4f8db7e98be105da517e1071c7b8ddc14c8926602"   # c1/sello_acta_c1.txt
INSUMOS_FICHAS = AQUI / "c1" / "insumos_fichas_c1.json"
MARCAS = ("correcta", "incorrecta", "no_decidible")
CAMPOS = ("ficha", "marca", "nota", "anotaciones", "paginas_vistas")

REGLAS = """\
## Reglas de lectura con que apliqué el protocolo

El criterio es el del protocolo del 28/09/2026 (sha256 en el acta) y el §2 del mandato. Estas reglas dicen cómo lo apliqué
a los casos que el protocolo no nombra; no lo cambian.

1. El nodo de destino se lee por su etiqueta, su descripción y su tramo juntos: la ficha da los tres como salida del extractor.
2. Una Condicion que restringe el alcance del destino (sujeto, objeto, finalidad, fecha, elegibilidad, calificación) es
   antecedente: el destino rige solo cuando ella se cumple. Cuenta como correcta. Si además reformula parte de la definición del
   destino, se anota («alcance» o «circular»).
3. Una de varias condiciones alternativas o acumuladas es antecedente del destino. Cuenta como correcta.
4. Una Condicion vacía (el tramo remite a una enumeración que está en otras unidades: «siempre que la contraparte sea:»,
   «las siguientes condiciones») es antecedente. Cuenta como correcta y se anota.
5. Es incorrecta la Condicion cuyo consecuente en el texto es otro y que no restringe el alcance del destino (por ejemplo, una
   regla que fija un plazo), y la que el texto declara indiferente («cuenten o no»).
6. Un destino permisivo o una regla de cómputo tipados Operacion, con la relación cierta, cuentan como correcta y se anotan
   (protocolo: nodo mal tipado con relación cierta).
"""


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--planilla", type=Path, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()

    raw_acta = ACTA.read_bytes()
    if sha(raw_acta) != ACTA_SHA256:
        raise SystemExit("acta distinta de la sellada")
    fichas_acta = [f["ficha"] for f in json.loads(raw_acta)["orden_de_lectura"]["fichas"]]
    renders = {Path(n).stem for n in json.loads(INSUMOS_FICHAS.read_text(encoding="utf-8"))["paginas_render"]}

    filas = [json.loads(x) for x in a.planilla.read_text(encoding="utf-8").splitlines() if x.strip()]
    ids = [f["ficha"] for f in filas]
    if sorted(ids) != sorted(fichas_acta) or len(ids) != len(set(ids)):
        raise SystemExit("las fichas de la planilla no son las del acta")
    for f in filas:
        if not set(CAMPOS) <= set(f):
            raise SystemExit(f"{f.get('ficha')}: faltan campos")
        if f["marca"] not in MARCAS:
            raise SystemExit(f"{f['ficha']}: marca {f['marca']!r}")
        if f["marca"] != "correcta" and not f["nota"].strip():
            raise SystemExit(f"{f['ficha']}: marca sin nota")
        if not f["paginas_vistas"] or not set(f["paginas_vistas"]) <= renders:
            raise SystemExit(f"{f['ficha']}: páginas vistas fuera de las renderizadas")
    filas.sort(key=lambda f: f["ficha"])

    a.salida.mkdir(parents=True, exist_ok=True)
    with open(a.salida / "planilla_c2.jsonl", "w", encoding="utf-8") as fh:
        for f in filas:
            fh.write(json.dumps(f, ensure_ascii=False) + "\n")
    md = ["# U-CONF-MATRIZ, C2: planilla de la lectura\n",
          f"Lectura de las 60 fichas de `c1/fichas_c1.md` (acta `{ACTA_SHA256}`), en el orden de lectura, contra el texto de E0 "
          "y la página renderizada. La planilla no lleva el par de cada ficha ni cuenta marcas: eso es C3.\n", REGLAS,
          "## Planilla\n"]
    for f in filas:
        md.append(f"### {f['ficha']} — {f['marca']}\n")
        md.append(f"{f['nota']}\n")
        if f["anotaciones"]:
            md.append("Anotaciones: " + "; ".join(f["anotaciones"]) + ".\n")
        md.append("Páginas vistas: " + ", ".join(f"`{p}.png`" for p in f["paginas_vistas"]) + ".\n")
        if f.get("cambio_antes_del_sello"):
            md.append(f"Cambio antes del sello: {f['cambio_antes_del_sello']}\n")
    (a.salida / "planilla_c2.md").write_text("\n".join(md), encoding="utf-8")
    print(json.dumps({"filas": len(filas), "planilla_c2.jsonl": sha((a.salida / "planilla_c2.jsonl").read_bytes()),
                      "planilla_c2.md": sha((a.salida / "planilla_c2.md").read_bytes())}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
