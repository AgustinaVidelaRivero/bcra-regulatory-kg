"""U-ALCANCE-E1, A3: registro de lecturas de un proceso de Python (USD 0; no cambia lo que el proceso hace).

Si la variable A3_LOG_LECTURAS nombra una carpeta, instala un audit hook (PEP 578) que anota cada evento «open» (open,
os.open e io.open_code, que usan también los imports) en <carpeta>/lecturas_<pid>.tsv: ruta absoluta, modo y flags. Entra
por PYTHONPATH (esta carpeta solo tiene este archivo), así que los procesos hijos que heredan el entorno también anotan.
El hook no abre archivos: escribe en el que abrió al cargarse. Sirve para la lista de los archivos leídos (despacho de A3,
punto 5) y para controlar que ningún proceso abra una ruta del repo.
"""
import os
import sys

_DIR = os.environ.get("A3_LOG_LECTURAS")
if _DIR:
    _f = open(os.path.join(_DIR, f"lecturas_{os.getpid()}.tsv"), "a", encoding="utf-8", buffering=1)
    _cwd = os.getcwd

    def _hook(evento, args):
        if evento != "open":
            return
        ruta = args[0]
        if isinstance(ruta, bytes):
            ruta = ruta.decode("utf-8", "replace")
        if not isinstance(ruta, str):
            return
        if not ruta.startswith("/"):
            ruta = _cwd() + "/" + ruta
        modo = args[1] if len(args) > 1 else None
        flags = args[2] if len(args) > 2 else None
        _f.write(f"{ruta}\t{modo}\t{flags}\n")

    sys.addaudithook(_hook)
