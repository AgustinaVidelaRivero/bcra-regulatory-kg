"""
lectura_plazos_sin_marcador_enmienda3.py — respaldo de la enmienda 3 a L-ESQ-R2 (USD 0, solo lectura).

Lee los elementos de umbral con `comparacion_asumida` de KG-Tanda0-Diez-r2a (plazos sin marcador de
comparación, regla `sin_marcador_plazo`) y los clasifica por las palabras que anteceden a la cuantía en
el texto propio de la unidad (E0 de `salida_tanda0_r2`). Es una lectura aproximada, por patrón: no
reemplaza una lectura caso por caso.

Clases:
  - antecedente que no es un máximo («últimos», «transcurrido», «períodos de», «durante»…);
  - antecedente compatible con un máximo («en los», «plazo de», «a los»…); incluye máximos falsos, como
    «luego del plazo de» o las ventanas hacia atrás;
  - sin clasificar;
  - tramo no hallado en el texto propio de la unidad.

No escribe archivos. Uso (desde la raíz del repo):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/esq/code/lectura_plazos_sin_marcador_enmienda3.py
"""

from __future__ import annotations

import sys

sys.dont_write_bytecode = True

import collections  # noqa: E402
import json  # noqa: E402
import re  # noqa: E402
from pathlib import Path  # noqa: E402

REPO = Path(__file__).resolve().parents[4]
KG = REPO / "data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2a/r2/kg.json"
E0 = REPO / "data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2"
VENTANA = 70  # caracteres antes de la cuantía

NO_MAX = re.compile(
    r"(luego de[l]?|despu[ée]s de[l]?|a partir de|transcurrid[oa]s?|vencid[oa]s?|una vez|durante"
    r"|por (un|el) (plazo|t[ée]rmino|per[ií]odo|lapso)|per[ií]odo(s)? de|cada|antelaci[oó]n|anticipaci[oó]n"
    r"|antig[üu]edad|no (sea )?(inferior|menor)|al menos|como m[ií]nimo|m[ií]nim[oa]s?( de)?|superior(es)? a"
    r"|mayor(es)? a|m[áa]s de|exceda|supere|últimos|anteriores|previos|vigencia|validez|por|de más de"
    r"|plazo(s)? (residual|promedio)|vida promedio|con vencimiento|mora|atraso|cuyo plazo|de hasta|hasta)\W*$",
    re.I)
MAX = re.compile(
    r"(dentro de (los|las)?|dentro del plazo de|en (el|un) plazo de|plazo de|en el t[ée]rmino de|t[ée]rmino de"
    r"|a los|en los|dentro de los primeros|plazo m[áa]ximo de|no (mayor|superior) a( los)?)\W*$", re.I)


def plegar(s: str) -> str:
    return re.sub(r"\s+", " ", s)


def main() -> None:
    kg = json.loads(KG.read_bytes())
    filas = [{"chunk": (n.get("provenance") or {}).get("chunk_id"), "tramo": u.get("tramo")}
             for n in kg["nodes"] for u in (n["properties"].get("umbrales") or []) if u.get("comparacion_asumida")]
    textos = {}
    for f in sorted(E0.glob("chunks_*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        for ch in (d if isinstance(d, list) else d.get("chunks") or d.get("unidades") or []):
            textos[ch.get("chunk_id") or ch.get("id")] = ch.get("texto") or ""
    conteo: collections.Counter = collections.Counter()
    ejemplos: dict[str, list] = collections.defaultdict(list)
    for f in filas:
        texto, tramo = plegar(textos.get(f["chunk"], "")), plegar(f["tramo"] or "")
        i = texto.find(tramo)
        if i < 0:
            clase = "tramo no hallado en el texto propio"
        else:
            antes = texto[max(0, i - VENTANA):i]
            clase = ("antecedente compatible con un máximo" if MAX.search(antes) else
                     "antecedente que no es un máximo" if NO_MAX.search(antes) else "sin clasificar")
            if len(ejemplos[clase]) < 6:
                ejemplos[clase].append(f"{f['chunk']}: …{antes[-45:]}[{tramo}]")
        conteo[clase] += 1
    print(f"elementos con comparacion_asumida: {len(filas)}")
    for clase, n in conteo.most_common():
        print(f"  {n:4d}  {clase}")
        for e in ejemplos.get(clase, []):
            print(f"          {e}")
    print(f"suma: {sum(conteo.values())}")


if __name__ == "__main__":
    main()
