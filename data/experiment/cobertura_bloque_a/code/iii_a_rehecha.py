"""(iii-a) rehecha — tercera medicion de una cantidad donde dos de tres
estuvieron mal. Sin API.  Uso: python3 iii_a_rehecha.py

DEFINICION OPERATIVA (escrita ANTES de correr, guarda por discrepancia):
una unidad de dev cuenta si y solo si

  (1) su campo `titulo` contiene una mencion del catalogo de sujetos, Y
  (2) su CUERPO no la contiene — cuerpo = `texto` MENOS su primera linea,
      porque `texto` arranca con el titulo repetido, Y
  (3) NINGUNA entrada de su `herencia` la contiene — la herencia tambien
      viaja al modelo en el mensaje de usuario.

Las dos mediciones previas quedan SUPERSEDED y se recomputan aca para dejar
escrito por que fallaban:
  · «titulo si / `texto` completo no» -> `texto` CONTIENE el titulo, de modo
    que la condicion es casi autocontradictoria y lo que sobrevive son
    artefactos de guionado de la extraccion, no casos reales.
  · «titulo si / cuerpo sin linea 1 no» -> ignora la herencia, que el modelo
    tambien ve.

Marca de sujeto: la misma de toda la unidad (senal_sujeto.formas_de_superficie,
70 entradas del catalogo del esquema congelado), coincidencia lexica.
"""
from __future__ import annotations

import glob
import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import comun_coba as C  # noqa: E402
import senal_sujeto as SS  # noqa: E402

E0_DEV = C.EXPERIMENT / "reextraccion_v2/e0_chunking/salida_enm01"
PATS = SS.formas_de_superficie()

# la rama del prompt por la que pasa A.2: todo chunk NO mini_chunk
RAMA_A2 = ("punto_terminal", "seccion_sin_puntos")


def men(t: str | None) -> bool:
    return any(p.search(t or "") for p in PATS.values())


def cuerpo_sin_linea1(c: dict) -> str:
    """`texto` menos su primera linea (el titulo repetido)."""
    t = c.get("texto") or ""
    return t.split("\n", 1)[1] if "\n" in t else ""


def herencia_menciona(c: dict) -> bool:
    return any(men(h.get("texto")) for h in (c.get("herencia") or []))


def main() -> int:
    dev = []
    for f in sorted(glob.glob(str(E0_DEV / "chunks_*.json"))):
        dev += json.loads(Path(f).read_text(encoding="utf-8"))
    n = len(dev)

    correcta = [c for c in dev if men(c.get("titulo"))
                and not men(cuerpo_sin_linea1(c))
                and not herencia_menciona(c)]
    superseded_1 = [c for c in dev if men(c.get("titulo")) and not men(c.get("texto"))]
    superseded_2 = [c for c in dev if men(c.get("titulo"))
                    and not men(cuerpo_sin_linea1(c))]

    # dato que cierra la conclusion: en la rama del prompt de A.2, ¿el titulo
    # esta CONTENIDO en el texto?
    rama = [c for c in dev if c.get("tipo") in RAMA_A2]
    contenidos = [c for c in rama
                  if (c.get("titulo") or "").strip()
                  and (c.get("titulo") or "").strip() in (c.get("texto") or "")]

    out = {
        "_definicion_operativa": {
            "1": "el campo `titulo` contiene una mencion del catalogo",
            "2": "el CUERPO (= `texto` menos su primera linea) NO la contiene",
            "3": "NINGUNA entrada de `herencia` la contiene",
            "marca": "coincidencia lexica, 70 entradas "
                     "(senal_sujeto.formas_de_superficie)",
            "escrita_antes_de_correr": True,
        },
        "medicion_correcta": {
            "casos": len(correcta), "de": n,
            "fraccion": round(len(correcta) / n, 4),
            "texto": f"{len(correcta)}/{n} = {len(correcta)/n:.1%}",
        },
        "superseded": {
            "titulo_si_texto_completo_no": {
                "casos": len(superseded_1),
                "texto": f"{len(superseded_1)}/{n} = {len(superseded_1)/n:.1%}",
                "por_que_fallaba": "`texto` CONTIENE el titulo: la condicion es "
                                   "casi autocontradictoria y lo que sobrevive "
                                   "son artefactos de guionado",
            },
            "titulo_si_cuerpo_sin_linea1_no": {
                "casos": len(superseded_2),
                "texto": f"{len(superseded_2)}/{n} = {len(superseded_2)/n:.1%}",
                "por_que_fallaba": "ignora la HERENCIA, que tambien viaja al "
                                   "modelo en el mensaje de usuario",
            },
        },
        "titulo_contenido_en_texto_rama_de_A2": {
            "unidades_en_la_rama": len(rama),
            "con_titulo_contenido_en_su_texto": len(contenidos),
            "fraccion": round(len(contenidos) / len(rama), 4) if rama else None,
            "tipos_de_la_rama": RAMA_A2,
        },
    }
    salida = C.UNIDAD / "iii_a_rehecha.json"
    salida.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n",
                      encoding="utf-8")
    print(json.dumps(out, ensure_ascii=False, indent=1))
    print(f"\nescrito: {salida.relative_to(C.REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
