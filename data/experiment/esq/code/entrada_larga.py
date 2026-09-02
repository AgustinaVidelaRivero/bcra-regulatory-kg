"""
entrada_larga.py — FASE (e) de U-ESQ-3b: arreglo de la entrada de textos largos
en los instrumentos de lectura humana (entrada 11 de
`docs/cola_mejoras_diferidas.md`).

EL DEFECTO QUE ARREGLA. En la lectura de U-ESQ-2, 35 campos de análisis
quedaron cortados a mitad de palabra en 1001–1011 caracteres
(`cobertura/desvios_lectura_esq2.md` §2). El instrumento no truncaba: el modo
CANÓNICO de la terminal descarta en silencio lo que excede ~1024 bytes de UNA
línea, y `input()` devuelve el resto sin señal alguna de pérdida. Por eso el
arreglo no puede ser «no truncar» (nadie truncaba): tiene que ser dejar de
depender de una única línea de terminal.

TRES MECANISMOS, y una alarma:

  1. MULTILÍNEA con terminador. El campo se cierra con una línea que contiene
     solo un punto (`.`). Cada línea entra por separado, así que el límite de
     línea de la terminal deja de ser el límite del campo: un texto de 8 kB
     entra en ocho líneas de 1 kB sin perder un byte.
  2. ARCHIVO: `:f <ruta>` lee el contenido íntegro de un archivo de texto. Es
     la salida robusta para pegar de una vez algo muy largo — no pasa por la
     línea de la terminal en absoluto.
  3. EDITOR: `:e` abre $EDITOR (default `vi`) sobre un temporal y toma lo que
     quede guardado.

  ALARMA DE TRUNCAMIENTO: toda línea que llegue con ≥ `UMBRAL_SOSPECHA` bytes
  se marca como sospechosa y se avisa EN EL ACTO, con el consejo de seguir
  pegando la cola en la línea siguiente. Es la señal que faltó en ESQ-2: la
  pérdida era silenciosa.

El módulo es independiente de la terminal (recibe el lector por parámetro), de
modo que el selftest lo ejercita con >1024 bytes sin necesidad de un tty.
"""

from __future__ import annotations

import os
import subprocess
import tempfile
from pathlib import Path

TERMINADOR = "."
UMBRAL_SOSPECHA = 1000     # bytes: por debajo del límite canónico (~1024)
AYUDA = ("texto multilínea — cerrá con una línea que contenga solo '.'  ·  "
         "':f <ruta>' lee un archivo  ·  ':e' abre $EDITOR  ·  "
         "línea vacía + '.' = campo vacío")


class ResultadoEntrada:
    """Texto leído + trazabilidad de cómo entró (para el reporte y el selftest)."""

    def __init__(self, texto: str, *, mecanismo: str, lineas: int,
                 lineas_sospechosas: list[int], bytes_totales: int):
        self.texto = texto
        self.mecanismo = mecanismo
        self.lineas = lineas
        self.lineas_sospechosas = lineas_sospechosas
        self.bytes_totales = bytes_totales

    def __str__(self) -> str:  # el instrumento guarda el texto, no el objeto
        return self.texto


def _leer_archivo(ruta: str) -> str:
    p = Path(os.path.expanduser(ruta.strip()))
    return p.read_text(encoding="utf-8")


def _leer_editor(salida) -> str:
    editor = os.environ.get("EDITOR", "vi")
    with tempfile.NamedTemporaryFile("w+", suffix=".txt", delete=False,
                                     encoding="utf-8") as tmp:
        path = tmp.name
    try:
        subprocess.call([editor, path])
        return Path(path).read_text(encoding="utf-8")
    finally:
        try:
            os.unlink(path)
        except OSError:
            salida(f"  (no se pudo borrar el temporal {path})")


def leer_texto_largo(prompt: str, *, obligatorio: bool = False,
                     lector=input, salida=print) -> ResultadoEntrada:
    """Lee un campo de texto sin depender del límite de línea de la terminal.

    `lector` y `salida` se inyectan para poder ejercitar la función sin tty
    (el selftest le pasa una lista de líneas). Devuelve ResultadoEntrada; el
    llamador usa `.texto`."""
    while True:
        salida(f"{prompt}")
        salida(f"  [{AYUDA}]")
        lineas: list[str] = []
        sospechosas: list[int] = []
        mecanismo = "multilinea"
        while True:
            try:
                linea = lector("  | ")
            except EOFError:
                linea = TERMINADOR
            if linea is None:
                linea = TERMINADOR
            linea = linea.rstrip("\n")
            if linea.strip() == TERMINADOR:
                break
            if linea.strip().startswith(":f "):
                try:
                    contenido = _leer_archivo(linea.strip()[3:])
                except OSError as e:
                    salida(f"  → no se pudo leer el archivo: {e}")
                    continue
                lineas = contenido.splitlines()
                mecanismo = "archivo"
                break
            if linea.strip() == ":e":
                contenido = _leer_editor(salida)
                lineas = contenido.splitlines()
                mecanismo = "editor"
                break
            n_bytes = len(linea.encode("utf-8"))
            if n_bytes >= UMBRAL_SOSPECHA:
                sospechosas.append(len(lineas) + 1)
                salida(f"  ⚠ línea {len(lineas)+1} con {n_bytes} bytes: la "
                       f"terminal corta cerca de 1024 y la pérdida es "
                       f"SILENCIOSA. Si el texto se cortó, seguí pegando la "
                       f"cola en la línea siguiente (el campo se arma con "
                       f"todas las líneas).")
            lineas.append(linea)
        texto = "\n".join(lineas).strip("\n")
        if texto.strip() or not obligatorio:
            return ResultadoEntrada(
                texto, mecanismo=mecanismo, lineas=len(lineas),
                lineas_sospechosas=sospechosas,
                bytes_totales=len(texto.encode("utf-8")))
        salida("  → este campo es OBLIGATORIO")


def pedir_opcion(prompt: str, validas: set[str], *, lector=input,
                 salida=print) -> str:
    """Marca codificada de una sola letra/dígito: acá el límite de línea no
    puede morder, así que se lee en una línea."""
    while True:
        try:
            v = lector(prompt).strip().lower()
        except EOFError:
            return "q"
        if v in validas:
            return v
        salida(f"  → opción inválida (usá: {' / '.join(sorted(validas))})")
