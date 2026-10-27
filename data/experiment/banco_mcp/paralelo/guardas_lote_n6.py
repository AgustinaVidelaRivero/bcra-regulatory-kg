#!/usr/bin/env python3
"""guardas_lote_n6.py — Las guardas del lanzador del lote para N6 de U-NAV-DISENO: la de guardas_lote_r5.py (HEAD, importada
sin editarla) con `lanzar_lote_paralelo_r5.py` y `correr_n6.py` en el patrón de otro paso pago.

El hueco que cierra (registro de decisiones, §130): ninguna guarda veía `lanzar_lote_paralelo_r5.py`. El patrón de los
comandos de la mesa trae `lanzar_lote_paralelo\\.py`, que no lo encuentra, y el de guardas_lote.py y guardas_lote_r5.py, ninguno
de los dos (su `lanzar_t`, sin escapes, no lo toca). N6 corre con un script nuevo, `correr_n6.py`, que también tiene que estar
en el patrón de toda guarda.

  pago        PATRON_PAGO = guardas_lote_r5.PATRON_PAGO_REAL + `|lanzar_lote_paralelo_r5\\.py|correr_n6\\.py`, con el mismo
              filtro y las mismas exclusiones que guardas_lote_r5.otro_paso_pago (de lo que da pgrep quedan solo los procesos de
              Python que corren un script con un nombre del patrón; sin el árbol propio: los ancestros, el proceso que corre la
              guarda y sus descendientes, y los del lote que se pase), a la que delega;
  pgrep       la espera de un comando que aguarda a que termine un paso pago, con el mismo patrón;
  extraccion  la de guardas_lote_r5, con el PATRON_EXTRACCION de este módulo (el de HEAD, el de la §198).
El patrón se puede pasar por parámetro o cambiar en el módulo (PATRON_PAGO), así las pruebas usan un token propio y ningún
`pgrep` de una prueba lleva el patrón real. PATRON_PAGO_REAL guarda el real aunque una prueba cambie PATRON_PAGO.

Imprime solo el pid y el nombre del script de lo que encuentra, nunca la línea entera ni el entorno. Ninguna espera.
Uso: guardas_lote_n6.py pago [--patron P] | extraccion      (código 7 o 9 si encuentra algo; 0 si no)
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
if str(AQUI) not in sys.path:
    sys.path.insert(0, str(AQUI))
import guardas_lote_r5 as R5                     # noqa: E402  (HEAD: solo import; trae guardas_lote como R5.BASE)

SUFIJO_N6 = r"|lanzar_lote_paralelo_r5\.py|correr_n6\.py"
PATRON_PAGO = R5.PATRON_PAGO_REAL + SUFIJO_N6
PATRON_PAGO_REAL = PATRON_PAGO                   # el de arriba, aunque una prueba cambie PATRON_PAGO
PATRON_EXTRACCION = R5.PATRON_EXTRACCION
CODIGO_PAGO = R5.CODIGO_PAGO
CODIGO_EXTRACCION = R5.CODIGO_EXTRACCION
tabla_procesos = R5.tabla_procesos
ancestros = R5.ancestros
descendientes = R5.descendientes
script_python = R5.script_python


def pgrep(patron: str | None = None) -> set[int]:
    """Los pids de `pgrep -f` con el patrón (por defecto, PATRON_PAGO), sin filtrar."""
    return R5.pgrep(patron or PATRON_PAGO)


def otro_paso_pago(raiz_lote: int | None = None, patron: str | None = None) -> list[dict]:
    """Los pasos pagos que corren, salvo el árbol propio: [{pid, script}] (guardas_lote_r5.otro_paso_pago con este patrón)."""
    return R5.otro_paso_pago(raiz_lote=raiz_lote, patron=patron or PATRON_PAGO)


def extraccion_corriendo() -> list[dict]:
    """La de guardas_lote_r5, con el PATRON_EXTRACCION de este módulo."""
    tabla = tabla_procesos()
    yo = os.getpid()
    propios = ancestros(yo, tabla) | {yo}
    pat = re.compile(PATRON_EXTRACCION)
    hallados = []
    for pid, (_, args) in sorted(tabla.items()):
        if pid in propios:
            continue
        m = pat.search(args)
        if m:
            hallados.append({"pid": pid, "script": m.group(3) + ".py"})
    return hallados


def main(argv: list[str]) -> int:
    args = argv[1:]
    if args[:1] == ["pago"] and (len(args) == 1 or (len(args) == 3 and args[1] == "--patron")):
        h = otro_paso_pago(patron=args[2] if len(args) == 3 else None)
        for x in h:
            print(f"FRENO: otro paso pago corriendo: pid {x['pid']} ({x['script']})")
        if not h:
            print("guarda de otro paso pago: ninguno")
        return CODIGO_PAGO if h else 0
    if args == ["extraccion"]:
        h = extraccion_corriendo()
        for x in h:
            print(f"FRENO: extracción corriendo: pid {x['pid']} ({x['script']})")
        if not h:
            print("control de la extracción: ninguna")
        return CODIGO_EXTRACCION if h else 0
    sys.stderr.write("uso: guardas_lote_n6.py pago [--patron P] | extraccion\n")
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
