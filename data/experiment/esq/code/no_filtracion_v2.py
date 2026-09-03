"""
no_filtracion_v2.py — verificación de NO-FILTRACIÓN de la vuelta 2, en los
DOS niveles del §5 del pre-registro v2 (`40493c9`). Módulo compartido por
selftest_esq3b_v2.py (que asserta) y manifiesto_esq3b_v2.py (que imprime la
salida verbatim para el freno 1). No escribe nada y no llama a la API.

NIVEL 1 — ventanas de 5 palabras: ninguna ventana de 5 palabras del texto de
NINGUNA unidad seleccionada (objetivo Y regresión fresca; texto propio y
también el contexto heredado que la ficha muestra — criterio más estricto que
el de la vuelta 1, que solo miraba el texto propio) aparece en el texto
AGREGADO o MODIFICADO por los retoques v2.

NIVEL 2 — sub-5-gramas de las delimitaciones nuevas: ninguna delimitación
nueva contiene bigramas ni trigramas DISTINTIVOS de las unidades de P1–P14
(las 15 del brazo objetivo). Operacionalización declarada: los n-gramas se
forman sobre la secuencia de palabras de CONTENIDO del texto propio de cada
unidad (palabras funcionales excluidas por la lista cerrada de abajo,
consecutivas tras el filtrado), y se buscan en el texto normalizado de las
delimitaciones nuevas. Para cada colisión se anota además en cuántas de las
762 unidades del corpus aparece el n-grama (medida de distintividad, para el
laudo de la autora).

En AMBOS niveles, una coincidencia que ya estaba en el prefijo v1 o en el de
producción se clasifica PREEXISTENTE: se declara y no bloquea (es simétrica en
el pareo). La normalización es la de la vuelta 1 (minúsculas, sin tildes,
no-alfanumérico → espacio).
"""

from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_esq3b_v2 as cc      # noqa: E402
import prompt_esq3b_v2 as pr2    # noqa: E402
import prompt_esq3b as pr1       # noqa: E402
import prompt_e1                 # noqa: E402

# Lista CERRADA de palabras funcionales del castellano (artículos,
# preposiciones, conjunciones, pronombres, demostrativos, auxiliares y modales
# frecuentes). Solo gramática: ningún sustantivo ni verbo de contenido.
PALABRAS_FUNCIONALES = frozenset("""
de la el los las un una unos unas y o u e en a al del que se su sus con por
para no ni es son ser sera seran fue fueron este esta esto estos estas ese esa
eso esos esas aquel aquella aquellos aquellas como mas si lo le les ya entre
sobre cuando donde cual cuales quien quienes ante bajo cabe contra desde
durante hacia hasta mediante salvo segun sin so tras cada todo toda todos
todas otro otra otros otras ha han haya hay habra debera deberan debe deben
debera deberan podra podran pueda puedan puede pueden sea sean estar estara
estaran esté estén tambien ademas asi solo tanto cuyo cuya cuyos cuyas
""".split())


def norm_palabras(s: str) -> list[str]:
    s = unicodedata.normalize("NFKD", s.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.replace("- ", "").replace("-\n", "")
    return re.sub(r"[^a-z0-9 ]", " ", s.replace("\n", " ")).split()


def _cargar():
    sel = json.loads((cc.ORDEN_DIR / "seleccion_brazos_esq3b_v2.json"
                      ).read_text(encoding="utf-8"))
    chunks = {c["id"]: c for c in cc.cargar_chunks_esq2()}
    agregado = " ".join(norm_palabras(
        " \n ".join(pr2.TEXTOS_AGREGADOS_V2.values())))
    delims = " ".join(norm_palabras(
        " \n ".join(pr2.DELIMITACIONES_NUEVAS_V2.values())))
    v1_norm = " ".join(norm_palabras(pr1.PREFIJO_SISTEMA_RETOCADO))
    prod_norm = " ".join(norm_palabras(prompt_e1.PREFIJO_SISTEMA))
    return sel, chunks, agregado, delims, v1_norm, prod_norm


def verificar() -> dict:
    sel, chunks, agregado, delims, v1_norm, prod_norm = _cargar()
    obj = [u["chunk_id"] for u in sel["objetivo"]["unidades"]]
    reg = [u["chunk_id"] for u in sel["regresion_fresca"]["unidades"]]

    # ---- nivel 1: ventanas de 5 palabras vs texto agregado/modificado ------
    n1_col: dict[str, list] = {"objetivo": [], "regresion_fresca": []}
    n1_pre: dict[str, list] = {"objetivo": [], "regresion_fresca": []}
    for brazo, cids in (("objetivo", obj), ("regresion_fresca", reg)):
        for cid in cids:
            c = chunks[cid]
            textos = [("propio", c["texto"])] + [
                ("heredado", h["texto"]) for h in (c.get("herencia") or [])]
            for origen, texto in textos:
                w = norm_palabras(texto)
                for i in range(len(w) - 4):
                    g = " ".join(w[i:i + 5])
                    if g not in agregado:
                        continue
                    destino = (n1_pre if (g in v1_norm or g in prod_norm)
                               else n1_col)
                    destino[brazo].append((cid, origen, g))

    # ---- nivel 2: bigramas/trigramas distintivos de P1–P14 vs delimitaciones
    freq_corpus: dict[str, int] = {}

    def _grams_de(texto: str) -> set[str]:
        w = [t for t in norm_palabras(texto)
             if t not in PALABRAS_FUNCIONALES]
        out: set[str] = set()
        for n in (2, 3):
            for i in range(len(w) - n + 1):
                out.add(" ".join(w[i:i + n]))
        return out

    n2_col: list = []
    n2_pre: list = []
    for cid in obj:
        for g in sorted(_grams_de(chunks[cid]["texto"])):
            if g not in delims:
                continue
            if g not in freq_corpus:
                freq_corpus[g] = sum(
                    1 for c in chunks.values() if g in " ".join(
                        t for t in norm_palabras(c["texto"])))
            fila = (cid, g, f"en_{freq_corpus[g]}_de_{len(chunks)}_unidades")
            (n2_pre if (g in v1_norm or g in prod_norm) else n2_col).append(fila)

    return {
        "n_unidades": {"objetivo": len(obj), "regresion_fresca": len(reg)},
        "nivel1_colisiones_nuevas": n1_col,
        "nivel1_preexistentes_v1_o_produccion": n1_pre,
        "nivel2_colisiones_nuevas": n2_col,
        "nivel2_preexistentes_v1_o_produccion": n2_pre,
        "verde": (not n1_col["objetivo"] and not n1_col["regresion_fresca"]
                  and not n2_col),
    }


def imprimir(res: dict) -> None:
    print("NO-FILTRACIÓN v2 — DOS NIVELES (pre-registro v2 §5)")
    print(f"  unidades: objetivo {res['n_unidades']['objetivo']} · "
          f"regresión fresca {res['n_unidades']['regresion_fresca']}")
    print(f"  NIVEL 1 (ventanas de 5 palabras, texto propio + contexto "
          f"heredado, vs texto agregado/modificado):")
    for brazo in ("objetivo", "regresion_fresca"):
        col = res["nivel1_colisiones_nuevas"][brazo]
        print(f"    {brazo}: colisiones NUEVAS = {len(col)} {col}")
    pre1 = (res["nivel1_preexistentes_v1_o_produccion"]["objetivo"]
            + res["nivel1_preexistentes_v1_o_produccion"]["regresion_fresca"])
    print(f"    preexistentes v1/producción (declaradas, no bloquean): "
          f"{len(pre1)} {pre1}")
    print(f"  NIVEL 2 (bigramas/trigramas de contenido de las unidades de "
          f"P1–P14, palabras funcionales excluidas, vs delimitaciones nuevas):")
    print(f"    colisiones NUEVAS = {len(res['nivel2_colisiones_nuevas'])} "
          f"{res['nivel2_colisiones_nuevas']}")
    print(f"    preexistentes v1/producción (declaradas, no bloquean): "
          f"{len(res['nivel2_preexistentes_v1_o_produccion'])} "
          f"{res['nivel2_preexistentes_v1_o_produccion']}")
    print(f"  VEREDICTO: {'VERDE' if res['verde'] else 'ROJO — se frena'}")


if __name__ == "__main__":
    r = verificar()
    imprimir(r)
    raise SystemExit(0 if r["verde"] else 1)
