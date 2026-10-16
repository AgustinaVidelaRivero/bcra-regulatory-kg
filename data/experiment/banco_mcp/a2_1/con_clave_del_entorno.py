"""Corre un comando con ANTHROPIC_API_KEY tomada de un archivo de entorno, sin imprimirla (mesa, §106; para los pasos pagos de A2.1).

- Lee el archivo con `dotenv_values` (python-dotenv, como `runner_corpus.py:1370-1371`) y pasa al comando SOLO esa variable, por su
  entorno: no va en la línea de comandos, no se imprime y no queda en el historial de la terminal (la terminal registra solo la línea
  que se escribe, que no la lleva).
- Si falta el archivo o la variable, frena con un mensaje que no muestra ningún valor.
- El código de salida es el del comando.

Uso: python -I -B con_clave_del_entorno.py --entorno <archivo> -- <comando> [args...]
"""
import os
import subprocess
import sys


def main() -> int:
    a = sys.argv[1:]
    if len(a) < 4 or a[0] != "--entorno" or a[2] != "--":
        sys.stderr.write("uso: con_clave_del_entorno.py --entorno <archivo> -- <comando> [args...]\n")
        return 2
    entorno, comando = a[1], a[3:]
    if not os.path.isfile(entorno):
        sys.stderr.write("FRENO: no existe el archivo de entorno indicado\n")
        return 3
    from dotenv import dotenv_values  # noqa: PLC0415
    valor = (dotenv_values(entorno).get("ANTHROPIC_API_KEY") or "").strip()
    if not valor:
        sys.stderr.write("FRENO: el archivo de entorno no trae ANTHROPIC_API_KEY\n")
        return 4
    env = dict(os.environ)
    env["ANTHROPIC_API_KEY"] = valor
    del valor
    return subprocess.run(comando, env=env).returncode


if __name__ == "__main__":
    sys.exit(main())
