"""U-ALCANCE-E1, A2: copia un archivo de texto con las rutas de la máquina reemplazadas, para que lo que entra al repo y al
paquete no escriba la cuenta del sistema: la carpeta de trabajo de la etapa (scratchpad) pasa a `$W` y la carpeta personal,
a `$HOME`. Uso: python3 -I -B sin_rutas_a2.py <carpeta de trabajo> <origen> <destino>"""
import os
import sys
from pathlib import Path

trabajo, origen, destino = Path(sys.argv[1]).resolve(), Path(sys.argv[2]), Path(sys.argv[3])
texto = origen.read_text(encoding="utf-8")
for viejo, nuevo in ((str(trabajo), "$W"), (str(Path(os.path.realpath(trabajo))), "$W"),
                     (os.path.expanduser("~"), "$HOME")):
    texto = texto.replace(viejo, nuevo)
destino.write_text(texto, encoding="utf-8")
