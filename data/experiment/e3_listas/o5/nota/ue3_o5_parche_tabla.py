"""U-E3-LISTAS, O5: la fila F23b de la tabla de reprocesamiento y su nota, sobre UNA COPIA (nunca el repo): las anclas
de la NOTA del ítem suman sus casos resueltos (`prompt_e3.py:495-510`) y las del candado se corren por la constante
nueva (`:459-492` y la llamada en `:513`); la nota de F23b dice qué agrega O5. Sin fila nueva.
Uso: python ue3_o5_parche_tabla.py <copia>"""
import sys
from pathlib import Path
p = Path(sys.argv[1]).resolve() / "data/experiment/mantenimiento/tabla_reprocesamiento.md"
t = p.read_text(encoding="utf-8")
cambios = [
    ("`prompt_e3.py:265-323`, `:375-378`, `:398`, `:407`; `ratchet_e3.py:283`; candado `prompt_e3.py:459-495` | R33, R33b, A3r |",
     "`prompt_e3.py:265-323`, `:375-378`, `:398`, `:407`, `:495-510`; `ratchet_e3.py:283`; candado `prompt_e3.py:459-492`, "
     "`:513` | R33, R33b, A3r |"),
    ("  verificación de citas recibe la marca de la forma r2 (`ratchet_e3.py:283`, la única línea del ratchet que cambia,\n"
     "  D1): una cita al bloque que abre la lista queda verificada (F24).\n",
     "  verificación de citas recibe la marca de la forma r2 (`ratchet_e3.py:283`, la única línea del ratchet que cambia,\n"
     "  D1): una cita al bloque que abre la lista queda verificada (F24). Desde O5 (nota al pie del 07/10/2026, noche), la\n"
     "  NOTA del ítem termina con dos casos resueltos sobre las omisiones `[meta_normativo]` (`prompt_e3.py:495-510`, una\n"
     "  constante aparte que `nota_item_lista` agrega): son parte de la NOTA del ítem, y un cambio en ellos frena igual\n"
     "  (candado del mensaje; check M de `selftest_e3`).\n"),
]
for a, b in cambios:
    assert t.count(a) == 1, a[:60]
    t = t.replace(a, b)
p.write_text(t, encoding="utf-8")
print("tabla: F23b, anclas y nota")
