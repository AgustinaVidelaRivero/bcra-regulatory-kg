"""
derivar_registro_alcance_r2b.py — U-ALCANCE-E1, A1: el derivado del registro de alcance por tanda que lee el mensaje de
E1 del perfil r2b (mandato docs/mandatos/UALCANCE_E1_cableado_registro_alcance.md, firmado el 07/10/2026; enmienda 4 al
protocolo entre tandas, §7, punto 1).

Lee catalogo_unico/registro_alcance_por_tanda.md con el lector de R2-2 de U-RERESOL-CAT
(reresolucion_catalogo/reresolver_catalogo.py: leer_registro_alcance y entradas_de_alcance, las mismas funciones con que el
ensamblado compone el rol_por_to de resolución), así que el formato registro_alcance_por_tanda/1 tiene un solo intérprete.
Escribe archivo → entrada con la forma de una entrada de generados_r2/rol_por_to_r2.json, solo para las filas con alcance
(una clase, dos clases o un rol reutilizado) de las tandas pedidas: una fila «sin alcance declarado» no tiene entrada, y su
documento va sin línea de alcance, como hoy. Las tandas se piden siempre (--tandas): el derivado crece por tanda, con un
cambio declarado entre tandas (fila F13c de la tabla de reprocesamiento), y una fila anticipada para una tanda posterior
no entra antes de su tanda.

prompt_r2b.py lo lee al importarse, con su candado (sha256 literal del módulo; decisión 1 de la autora al firmar).
Regenerarlo con otro contenido cambia su sha256: el candado frena hasta re-sellar.

Control: la salida es igual a la unión, en el orden del registro, de las entradas por tanda de
reresolver_catalogo.registro_legible (el subcomando `registro` de R2-2); si no, frena.

Se corre desde la raíz de una COPIA del repo (CLAUDE.md §4.k y §4.l):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/catalogo_unico/code/derivar_registro_alcance_r2b.py \\
      --tandas 1 [--salida RUTA | --salida -] [--reporte RUTA.json]
Con `--salida -`, el derivado va a la salida estándar y nada más se imprime. USD 0, sin API. Determinístico: dos corridas
dan el mismo archivo byte a byte.
"""
from __future__ import annotations

import argparse
import hashlib
import sys
from collections import OrderedDict
from pathlib import Path

sys.dont_write_bytecode = True
RAIZ = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(RAIZ / "data" / "experiment" / "reresolucion_catalogo"))
import reresolver_catalogo as RR        # noqa: E402  (el lector de R2-2 del registro de alcance por tanda)

SALIDA = RAIZ / "data" / "experiment" / "catalogo_unico" / "registro_alcance_r2b.json"
GENERADOR = "data/experiment/catalogo_unico/code/derivar_registro_alcance_r2b.py"


def derivar(md: Path, tandas: list[str]) -> tuple[OrderedDict, OrderedDict]:
    """(derivado, registro leído). El derivado: las entradas de alcance de `tandas` contra el rol_por_to y los labels del
    catálogo del request (r1_e4.catalogo_r2, con sus candados). Frena si una tanda pedida no tiene tabla en el registro o si
    el derivado no es la unión de las entradas por tanda de registro_legible."""
    reg = RR.leer_registro_alcance(md)
    faltan = [t for t in tandas if t not in reg["tandas"]]
    if faltan:
        raise RR.ErrorRegistroAlcance(f"tandas sin tabla en el registro: {faltan}")
    cat = RR.E4.catalogo_r2()
    derivado = RR.entradas_de_alcance(reg, cat["rol_por_to"], cat["labels"], tandas)
    union: OrderedDict = OrderedDict()
    for t, entradas in RR.registro_legible(md)["rol_por_to_por_tanda"].items():
        if t in tandas:
            union.update(entradas)
    if RR.json_texto(union) != RR.json_texto(derivado):
        raise RR.ErrorRegistroAlcance("el derivado no es la unión de las entradas por tanda de registro_legible")
    return derivado, reg


def reporte(reg: dict, tandas: list[str], derivado: dict, texto: str) -> OrderedDict:
    filas = [(t, f) for t, fs in reg["tandas"].items() for f in fs]
    return OrderedDict([
        ("generador", GENERADOR), ("formato_registro", reg["formato"]), ("registro", reg["fuente"]),
        ("registro_sha256", reg["fuente_sha256"]), ("tandas_pedidas", list(tandas)),
        ("filas_por_tanda_del_registro", OrderedDict((t, len(fs)) for t, fs in reg["tandas"].items())),
        ("derivado_sha256", hashlib.sha256(texto.encode("utf-8")).hexdigest()), ("entradas", len(derivado)),
        ("filas_con_alcance", [OrderedDict([("tanda", t), ("to", f["to"]), ("archivo", f["archivo"]),
                                            ("decision", f["decision"]), ("ids", f["ids"]), ("linea_registro", f["linea"])])
                               for t, f in filas if t in tandas and f["decision"] != "sin_alcance"]),
        ("sin_alcance_declarado", [OrderedDict([("tanda", t), ("to", f["to"]), ("linea_registro", f["linea"])])
                                   for t, f in filas if t in tandas and f["decision"] == "sin_alcance"]),
        ("filas_de_otras_tandas", [OrderedDict([("tanda", t), ("to", f["to"]), ("decision", f["decision"])])
                                   for t, f in filas if t not in tandas]),
        ("control_union_registro_legible", True)])


def main() -> int:
    ap = argparse.ArgumentParser(description="derivado del registro de alcance por tanda para el mensaje de E1 r2b")
    ap.add_argument("--tandas", required=True, help="tandas del registro que entran, separadas por coma (p. ej. 1)")
    ap.add_argument("--registro", type=Path, default=RR.REGISTRO_ALCANCE_MD)
    ap.add_argument("--salida", default=str(SALIDA), help="ruta del derivado, o «-» para la salida estándar")
    ap.add_argument("--reporte", type=Path, default=None)
    a = ap.parse_args()
    tandas = [t.strip() for t in a.tandas.split(",") if t.strip()]
    derivado, reg = derivar(a.registro, tandas)
    texto = RR.json_texto(derivado)
    if a.salida == "-":
        sys.stdout.write(texto)
        return 0
    Path(a.salida).write_text(texto, encoding="utf-8")
    rep = reporte(reg, tandas, derivado, texto)
    if a.reporte is not None:
        a.reporte.write_text(RR.json_texto(rep), encoding="utf-8")
    print(f"derivado: {RR.ruta(a.salida)} ({rep['entradas']} entradas, tandas {','.join(tandas)}), sha256 "
          f"{rep['derivado_sha256']}; registro {reg['fuente']} sha256 {reg['fuente_sha256']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
