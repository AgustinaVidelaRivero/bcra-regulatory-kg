"""
t1_sellos_t4.py — U-REEXT-T0, T1, punto 7 (mandato firmado en e2027dd): lo que T4 lee, sellado antes de T2, con su
sha256 y su hora. Nada de esto mira una extracción: solo el texto de E0 (`e0_chunking/salida_tanda0_r2b/`, 9f6361e) y
las selecciones y lecturas ya versionadas. USD 0.

  a. Las 27 unidades de P4b: ya selladas (data/experiment/prompt_r2/p4b/salida/seleccion_p4b.json, sha256 e2551cf3…);
     se verifica el sha256 y se copia la lista.
  b. Las once listas que exceptúan de la tanda 0 que las lecturas anteriores ya identificaron, con su tipo (b1, lo que
     queda afuera de una clase; b2, las condiciones de una sola excepción) y la lectura de donde sale. Para las cuatro
     que P4b excluyó por leídas antes, ninguna lectura anterior les asigna b1 o b2 (U-DIAG-VINCULO las identificó como
     listas de excepción): el tipo es mi lectura en T1, con las definiciones del prefijo (P3C-b1), declarada y
     PENDIENTE de revisión de la autora. Los ítems de cada lista salen de E0 (los ítems directos y su ::intro, si lo
     tienen). No se buscan listas nuevas.
  c. El orden sorteado del grupo c: el pool c de P4b (seleccion_p4b.pools: una cuantía, reglas_comparacion
     .detectar_cuantias, y dos o más marcas de supuesto, RX_SUPUESTO, en el texto propio), importado y no copiado,
     sobre toda la tanda 0 y sin las exclusiones de P4b; orden: random.Random(f"{SEMILLA_C}:c").shuffle de los ids
     ordenados (el método de P4b, con semilla propia).
  d. Las semillas de los sorteos de T4 que dependen de la salida de T2 (las omisiones meta_normativo, con y sin marca
     del contador), con el procedimiento declarado; y la semilla del sorteo de la cola humana, la que fijó la autora al
     firmar (decisión 5).

Corre desde la raíz de una COPIA del repo y escribe solo --salida/sellos_t4.json (fuera de la copia).
  PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B data/experiment/reext_t0/t1_sellos_t4.py --salida DIR
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
E0 = REX / "e0_chunking" / "salida_tanda0_r2b"
P4B = REPO / "data" / "experiment" / "prompt_r2" / "p4b"
sys.path.insert(0, str(P4B))
import seleccion_p4b as SP4B  # noqa: E402 — pools y RX_SUPUESTO de P4b, importados, no copiados

TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
SHA_SELECCION_P4B = "e2551cf3c7dd110bf9e10bb4918f13c3d79a7320642843e61eb8ca88b8d9fd09"
SEMILLA_C = "U-REEXT-T0:grupo-c:2026-10-05"
SEMILLA_OMISIONES_SIN_MARCA = "U-REEXT-T0:omisiones-sin-marca:2026-10-05"
SEMILLA_OMISIONES_CON_MARCA = "U-REEXT-T0:omisiones-con-marca:2026-10-05"
SEMILLA_COLA_HUMANA = "U-REEXT-T0:cola-humana:2026-10-05"   # decisión 5 de la autora al firmar
LISTAS = [
    ("cla::5.1.1", "b1", "la del ejemplo (mandato de U-REEXT-T0, T1, 7.b; b1 se mide con el ejemplo, decisión de la "
                         "autora del 05/10/2026 tras el FRENO P4b)"),
    ("ext::3.5.4", "b2", "P4 la dejó aparte: los ítems son las condiciones de una sola excepción "
                         "(data/experiment/prompt_r2/p4/estrato_listas_excepciones.md:28-29)"),
    ("ext::2.6.1", "b2", "ídem (estrato_listas_excepciones.md:28-29)"),
    ("ext::7.8.4", "b2", "ídem (estrato_listas_excepciones.md:28-29)"),
    ("ext::2.7", "b2", "ídem (estrato_listas_excepciones.md:28-29)"),
    ("ctacte::3.2", "b1", "P4b, con su lectura dudosa declarada: también admite la de supuestos de una sola exclusión "
                          "(data/experiment/prompt_r2/p4b/seleccion_p4b.md:52-55); se reporta aparte (decisión de la "
                          "autora del 05/10/2026)"),
    ("ext::3.5.3", "b2", "P4b: la norma y una única salvedad, «excepto que el deudor encuadre en alguna de las "
                         "siguientes situaciones» (seleccion_p4b.py, DECISIONES; seleccion_p4b.md:48-49)"),
    ("ext::3.13.1", "b1", "excluida por P4b por leída antes (seleccion_p4b.md:50-51); U-DIAG-VINCULO la leyó como "
                          "lista de excepción (reports/u_diag_vinculo/salidas/lectura_precision.md:23). Tipo: mi "
                          "lectura en T1, PENDIENTE de revisión: «requerirá la conformidad previa del BCRA, excepto "
                          "para las operaciones de:» y cada ítem nombra una clase de operaciones o de sujetos que queda "
                          "afuera"),
    ("ext::3.6.1", "b1", "excluida por P4b por leída antes (seleccion_p4b.md:50-51; data/experiment/prompt_r2/p3b/"
                         "diseno_p3b.md:158). Tipo: mi lectura en T1, PENDIENTE de revisión: «Se prohíbe el acceso… "
                         "excepto para la cancelación… de:» y cada ítem nombra una clase de deudas que queda afuera"),
    ("ext::3.6.4", "b2", "excluida por P4b por leída antes (seleccion_p4b.md:50-51); U-DIAG-VINCULO "
                         "(lectura_precision.md:31). Tipo: mi lectura en T1, PENDIENTE de revisión: «requerirá la "
                         "conformidad previa del BCRA excepto que la operación encuadre en alguna de las siguientes "
                         "situaciones y se cumplan la totalidad de las condiciones», la forma de ext::3.5.3"),
    ("ext::10.11", "b2", "excluida por P4b por leída antes (seleccion_p4b.md:50-51); U-DIAG-VINCULO "
                         "(lectura_precision.md:18 y :26). Tipo: mi lectura en T1, PENDIENTE de revisión: «Se requerirá "
                         "la conformidad previa… excepto cuando… la entidad verifique que:» y cada ítem es un supuesto "
                         "de esa salvedad"),
]


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()
    if a.salida.resolve().is_relative_to(REPO.resolve()):
        raise SystemExit("--salida no puede estar dentro de la copia")
    ch = {}
    for to in TOS:
        ch.update({c["id"]: c for c in json.loads((E0 / f"chunks_{to}.json").read_text(encoding="utf-8"))})

    # a
    p = P4B / "salida" / "seleccion_p4b.json"
    s_a = sha(p.read_bytes())
    if s_a != SHA_SELECCION_P4B:
        raise SystemExit(f"seleccion_p4b.json con sha256 {s_a}, no el sellado")
    sel = json.loads(p.read_text(encoding="utf-8"))
    a_unidades = [{"id": u, "grupo": g} for g, us in sel["grupos"].items() for u in us]
    if len(a_unidades) != sel["unidades"] or len({x["id"] for x in a_unidades}) != sel["unidades"]:
        raise SystemExit(f"seleccion_p4b.json: {len(a_unidades)} unidades en los grupos, {sel['unidades']} declaradas")

    # b
    b_listas = []
    for cont, tipo, fuente in LISTAS:
        to, _, unidad = cont.partition("::")
        rx = re.compile(rf"^{re.escape(unidad)}\.\d+$")
        directos = sorted({c["unidad"] for c in ch.values() if c["to"] == to and rx.match(c["unidad"])},
                          key=lambda u: [int(x) for x in u.split(".")])
        items = []
        for u in directos:
            items += [i for i in (f"{to}::{u}", f"{to}::{u}::intro") if i in ch]
        b_listas.append({"contenedor": cont, "tipo": tipo, "intro": f"{cont}::intro" if f"{cont}::intro" in ch else None,
                         "items": items, "fuente": fuente})

    # c
    t_c = [cid for cid, c in ch.items()
           if SP4B.RCMP.detectar_cuantias(c.get("texto") or "") and len(SP4B.RX_SUPUESTO.findall(c.get("texto") or "")) >= 2]
    orden_c = sorted(t_c)
    random.Random(f"{SEMILLA_C}:c").shuffle(orden_c)

    out = {
        "unidad": "U-REEXT-T0, T1, punto 7 (sellado antes de T2)",
        "e0": {"ruta": "data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b", "commit": "9f6361e",
               "unidades": len(ch)},
        "a_unidades_p4b": {"fuente": "data/experiment/prompt_r2/p4b/salida/seleccion_p4b.json", "sha256": s_a,
                           "n": len(a_unidades), "unidades": a_unidades},
        "b_listas_que_exceptuan": {"n": len(b_listas), "por_tipo": {t: sum(1 for x in b_listas if x["tipo"] == t)
                                                                    for t in ("b1", "b2")},
                                   "listas": b_listas,
                                   "nota": "ctacte::3.2 se reporta aparte por su lectura dudosa; los tipos de "
                                           "ext::3.13.1, ext::3.6.1, ext::3.6.4 y ext::10.11 son lectura de T1"},
        "c_grupo_c": {"definicion": "pool c de P4b: texto propio con una cuantía (reglas_comparacion."
                                    "detectar_cuantias) y dos o más marcas de supuesto (seleccion_p4b.RX_SUPUESTO), "
                                    "sobre toda la tanda 0, sin las exclusiones de P4b",
                      "semilla": SEMILLA_C, "metodo": "random.Random(f'{semilla}:c').shuffle(sorted(ids))",
                      "pool": len(orden_c), "orden": orden_c,
                      "lectura": "en T4 se toman en este orden 30 unidades; antes de mirar la extracción se decide "
                                 "sobre el texto si tienen más de un supuesto (las que no, se saltean y se cuentan); "
                                 "si el pool no llega a 30, se leen todas"},
        "d_semillas_t4": {
            "cola_humana": {"semilla": SEMILLA_COLA_HUMANA, "fuente": "decisión 5 de la autora al firmar (e2027dd)",
                            "procedimiento": "si la cola de los diez TOs tiene más de 30 unidades, random.Random(semilla)"
                                             ".sample(sorted(chunk_ids de la cola), 30); si tiene 30 o menos, todas"},
            "omisiones_meta_normativo_sin_marca": {
                "semilla": SEMILLA_OMISIONES_SIN_MARCA,
                "procedimiento": "omisiones de categoría meta_normativo de omisiones.jsonl del ensamblado r2b de los diez "
                                 "TOs sin marca del contador (sin ninguna de las siete clases); clave de cada omisión "
                                 "(chunk_id, posición en la lista de omisiones de su unidad); si son más de 30, "
                                 "random.Random(semilla).sample(sorted(claves), 30); si son 30 o menos, todas"},
            "omisiones_meta_normativo_con_marca": {
                "semilla": SEMILLA_OMISIONES_CON_MARCA,
                "procedimiento": "ídem, con las omisiones meta_normativo que llevan alguna marca del contador"}},
        "insumos": {"seleccion_p4b.py_sha256": sha((P4B / "seleccion_p4b.py").read_bytes()),
                    "reglas_comparacion.py_sha256": sha(Path(SP4B.RCMP.__file__).read_bytes())},
    }
    a.salida.mkdir(parents=True, exist_ok=True)
    (a.salida / "sellos_t4.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"a": len(a_unidades), "b": out["b_listas_que_exceptuan"]["por_tipo"],
                      "b_items": {x["contenedor"]: len(x["items"]) for x in b_listas}, "c_pool": len(orden_c),
                      "c_primeros": orden_c[:5]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
