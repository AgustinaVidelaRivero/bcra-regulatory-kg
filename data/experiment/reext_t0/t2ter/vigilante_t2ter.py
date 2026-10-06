"""Vigilante externo del tope de T2-ter de U-REEXT-T0 (copia de t2bis/vigilante_t2bis.py): el runner corre con
--autorizado-tope 80.0, el tope del manifiesto, y el de USD 1 de T2-ter se hace cumplir por fuera del runner.

Solo LEE presupuesto_compartido.json (stat cada 10 ms y lectura cuando cambia); no toca las bases, la caché ni la
salida. El gasto solo cambia cuando una llamada pagada ya quedó registrada (fila en la base, línea de usage y
presupuesto): si la lectura pasa el umbral, manda SIGINT al runner enseguida; si a los 30 s el proceso sigue vivo,
SIGKILL. Riesgo aceptado y declarado: si el cruce cae justo antes de un reintento por corte, ese reintento puede quedar
en vuelo y perderse. Si actúa, la unidad frena sin relanzar.

Uso: python -B vigilante_t2ter.py --pid PID --presupuesto RUTA --umbral 51.152696 --log RUTA
Salida: 0 si el runner terminó sin que el vigilante actuara; 2 si mandó SIGINT; 3 si tuvo que mandar SIGKILL.
"""
import argparse
import json
import os
import signal
import time

ap = argparse.ArgumentParser()
ap.add_argument("--pid", type=int, required=True)
ap.add_argument("--presupuesto", required=True)
ap.add_argument("--umbral", type=float, required=True)
ap.add_argument("--log", required=True)
ap.add_argument("--intervalo", type=float, default=0.01)
ap.add_argument("--gracia", type=float, default=30.0)
a = ap.parse_args()


def log(msg: str) -> None:
    with open(a.log, "a", encoding="utf-8") as f:
        f.write(f"{time.strftime('%Y-%m-%dT%H:%M:%S%z')} {msg}\n")


def vivo(pid: int) -> bool:
    try:
        os.kill(pid, 0)
        return True
    except ProcessLookupError:
        return False


def leer_gasto() -> float | None:
    for _ in range(5):
        try:
            with open(a.presupuesto, encoding="utf-8") as f:
                return float(json.load(f)["gasto_usd"])
        except (OSError, ValueError, KeyError):
            time.sleep(0.005)
    return None


log(f"inicio | pid {a.pid} | umbral USD {a.umbral:.6f} | gasto USD {leer_gasto()}")
ultimo = None
while vivo(a.pid):
    try:
        mt = os.stat(a.presupuesto).st_mtime_ns
    except OSError:
        mt = None
    if mt != ultimo:
        ultimo = mt
        g = leer_gasto()
        log(f"cambio | gasto USD {g}")
        if g is not None and g > a.umbral:
            log(f"UMBRAL superado ({g:.6f} > {a.umbral:.6f}): SIGINT al pid {a.pid}")
            os.kill(a.pid, signal.SIGINT)
            t0 = time.time()
            while vivo(a.pid) and time.time() - t0 < a.gracia:
                time.sleep(0.1)
            if vivo(a.pid):
                log(f"sigue vivo a los {a.gracia:.0f} s: SIGKILL")
                os.kill(a.pid, signal.SIGKILL)
                raise SystemExit(3)
            log("el runner terminó tras SIGINT")
            raise SystemExit(2)
    time.sleep(a.intervalo)
log(f"fin del runner sin actuar | gasto USD {leer_gasto()}")
raise SystemExit(0)
