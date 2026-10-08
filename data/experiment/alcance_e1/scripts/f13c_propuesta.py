"""U-ALCANCE-E1, A1: texto propuesto para la fila F13c de tabla_reprocesamiento.md (no se aplica al repo en A1).
Escribe en DIR las dos variantes (fila completa, una línea) y la fila vigente. Uso: f13c_propuesta.py TABLA DIR"""
import sys
from pathlib import Path

tabla, d = Path(sys.argv[1]), Path(sys.argv[2])
fila = next(l for l in tabla.read_text(encoding="utf-8").splitlines() if l.startswith("| F13c |"))
celdas = [c.strip() for c in fila.strip().strip("|").split("|")]
assert len(celdas) == 10 and celdas[-1] == "R20"
CAMBIO = ("Registro de alcance por tanda (`catalogo_unico/registro_alcance_por_tanda.md`, legible por código desde R2-2 de "
          "U-RERESOL-CAT) y su derivado para E1 (`catalogo_unico/registro_alcance_r2b.json`, que escribe "
          "`catalogo_unico/code/derivar_registro_alcance_r2b.py` con el mismo lector): una entrada de clase o de rol "
          "reutilizado para un documento nuevo, o un documento declarado sin alcance")
ENTRA = ("en el ensamblado, el `rol_por_to` del catálogo de resolución: la resolución por relación (R4 o R3 si el documento "
         "recibe alcance; cuarentena por la parte A de la enmienda 6 a L-ESQ-R2 si no lo tiene, solo en r2b); en E1, desde "
         "A2 de U-ALCANCE-E1 (`<commit de A2>`), la línea «Alcance de este TO» del mensaje: `prompt_r2b.py` lee el derivado "
         "al importar, con su candado, y lo usa cuando el documento no tiene entrada en la tabla de la release (F12); un "
         "documento declarado sin alcance no tiene entrada en el derivado y va sin línea. Hasta A2 el mensaje no leía el "
         "registro (R2-2 lo midió idéntico en las 2.439 unidades y en los 13 casos del candado)")
RECOMPUTA = ("regenerar el derivado y re-sellar su sha (el candado del derivado frena hasta entonces, y el del mensaje si el "
             "documento está en su fixture); resolución, E2 y ensamblado en código; E1 y E3 de las unidades del documento "
             "que recibe alcance, como F12, si ya estaban extraídas")
ANCLA = ("`prompt_r2b.py:409`, `:476-478` (derivado y su candado), `:481-487` (`alcance_del_documento`); "
         "`catalogo_unico/code/derivar_registro_alcance_r2b.py`; `r1_e4.py:417-423` (parte A), `:593-642`; "
         "`reresolucion_catalogo/reresolver_catalogo.py:159`, `:199` (lector), `--registro-alcance`; enmienda 4 al protocolo, "
         "§2 y §7 (FIRMADA, `53bbd6f`)")
a = list(celdas)
a[1], a[2], a[3] = CAMBIO, ENTRA, RECOMPUTA
a[4] = ("cambia (las unidades del documento que recibe alcance, como F12; con el derivado regenerado y sin re-sellar, el "
        "candado frena)")
a[5] = "no cambia (con la salida de E1 fija)"
a[6] = "E1 y E3 de las afectadas (F12); sin unidades ya extraídas del documento, solo código sobre lo guardado"
a[7], a[8], a[9] = "9", ANCLA, "R34"
b = list(celdas)
b[1], b[2], b[3], b[8] = CAMBIO, ENTRA, RECOMPUTA, ANCLA
b[4] = ("no cambia (el mensaje no lee el registro sino su derivado: con el derivado regenerado, el candado frena hasta "
        "re-sellar su sha, como F11b, y, re-sellado, cambian las unidades del documento que recibe alcance, como F12)")
b[6] = ("solo código sobre lo guardado mientras el derivado no se regenere; regenerado y re-sellado, E1 y E3 de las "
        "afectadas (F12)")
for nombre, c in (("f13c_vigente.md", celdas), ("f13c_propuesta_A.md", a), ("f13c_propuesta_B.md", b)):
    (d / nombre).write_text("| " + " | ".join(c) + " |\n", encoding="utf-8")
print("ok", len(a), len(b))
