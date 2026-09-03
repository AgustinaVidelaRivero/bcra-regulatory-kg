"""
entrada_larga_v2.py — FASE (c) de U-ESQ-3b-v2: entrada de textos largos CON
el arreglo del BUG DE PEGADO (prerrequisito de la lectura, pre-registro v2
§5).

EL DEFECTO QUE ARREGLA. En la lectura de la vuelta 1, el campo `que_cambio` de
una ficha quedó contaminado con un volcado de ~4 KB del render de la PROPIA
ficha (nota de instrumento (i) de la tabla `0c19dc8`): un pegado de terminal
que incluía el render completo entró línea por línea al campo multilínea, y el
instrumento lo aceptó como si fuera la respuesta. El campo quedó sellado así
en el worksheet adjudicado.

EL ARREGLO. El lector multilínea DETECTA las firmas estructurales del render
de ficha (reglas de ancho completo, encabezados de sección del instrumento) en
las líneas que entran. Si al cerrar el campo hubo AL MENOS UNA línea con firma
de render, el campo se DESCARTA ENTERO, se avisa en el acto y se vuelve a
pedir — un render pegado no puede contaminar un campo de respuesta: o el campo
queda limpio o no queda. Las firmas son estructurales (reglas de 100
caracteres, encabezados exactos del render), no palabras sueltas: una
respuesta legítima no las contiene.

Se conservan los tres mecanismos y la alarma de la entrada 11 (vuelta 1,
`entrada_larga.py`, que no se toca): multilínea con terminador '.', ':f
<ruta>' para archivo, ':e' para $EDITOR, y alarma ante líneas de ≥1000 bytes.
La detección de render se aplica al texto final SIN importar el mecanismo.

El módulo es independiente de la terminal (recibe el lector por parámetro):
el selftest pega un render REAL de ficha y verifica que el campo queda limpio.
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

# ----------------------- firmas del render de ficha -------------------------- #
# El ancho del render del instrumento (leer_fichas_esq3b_v2.W usa este valor:
# una sola fuente para render y detección).
W_RENDER = 100

# Una línea es firma de render si ES una regla de ancho completo o si CONTIENE
# uno de los encabezados exactos que el instrumento imprime en cada ficha.
_REGLAS_COMPLETAS = ("=" * W_RENDER, "-" * W_RENDER, "·" * W_RENDER)
_ENCABEZADOS_RENDER = (
    "EXTRACCIONES PAREADAS (crudas",
    "TEXTO FUENTE DE LA UNIDAD:",
    ") EXTRACCIÓN BASE",
    ") EXTRACCIÓN NUEVA",
    "CONTEXTO HEREDADO (solo contexto",
)


def linea_es_render(linea: str) -> bool:
    s = linea.rstrip("\n")
    if s.strip() in _REGLAS_COMPLETAS:
        return True
    if any(f in s for f in _ENCABEZADOS_RENDER):
        return True
    stripped = s.strip()
    if stripped.startswith("FICHA ") and "/" in stripped and " — " in stripped:
        return True
    return False


def lineas_render(texto: str) -> list[int]:
    """Índices 1-based de las líneas de `texto` con firma de render."""
    return [i for i, ln in enumerate(texto.splitlines(), start=1)
            if linea_es_render(ln)]


class ResultadoEntrada:
    """Texto leído + trazabilidad de cómo entró (para el reporte y el
    selftest)."""

    def __init__(self, texto: str, *, mecanismo: str, lineas: int,
                 lineas_sospechosas: list[int], bytes_totales: int,
                 descartes_por_render: int = 0):
        self.texto = texto
        self.mecanismo = mecanismo
        self.lineas = lineas
        self.lineas_sospechosas = lineas_sospechosas
        self.bytes_totales = bytes_totales
        self.descartes_por_render = descartes_por_render

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
    """Lee un campo de texto sin depender del límite de línea de la terminal y
    SIN aceptar un render de ficha pegado (bug de pegado de la vuelta 1).

    `lector` y `salida` se inyectan para poder ejercitar la función sin tty
    (el selftest le pasa una lista de líneas). Devuelve ResultadoEntrada; el
    llamador usa `.texto`."""
    descartes = 0
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

        # --- detección del bug de pegado: firma de render en el campo -------
        con_render = lineas_render(texto)
        if con_render:
            descartes += 1
            salida(f"  ⚠ RENDER DE FICHA DETECTADO en el campo (líneas "
                   f"{con_render[:5]}{'…' if len(con_render) > 5 else ''}): "
                   f"parece un pegado del render del instrumento, no una "
                   f"respuesta. El campo se DESCARTA ENTERO y se vuelve a "
                   f"pedir — escribí (o pegá) solo la respuesta.")
            continue

        if texto.strip() or not obligatorio:
            return ResultadoEntrada(
                texto, mecanismo=mecanismo, lineas=len(lineas),
                lineas_sospechosas=sospechosas,
                bytes_totales=len(texto.encode("utf-8")),
                descartes_por_render=descartes)
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
