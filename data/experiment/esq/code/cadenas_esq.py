"""
cadenas_esq.py — Instrumento de ESQ-1: inventario de cadenas DISTINTAS de un
canal abierto de los jsonl de extracción E1.

Declarado antes de existir en `data/experiment/esq/prerregistro_esq1.md` §7.
Produce el número central de ESQ-1: la lista de cadenas distintas que el
extractor emitió por un canal de texto libre.

REQUISITO DE DISEÑO (no negociable, pre-registro §7 y blindaje de D9)
--------------------------------------------------------------------
La salida es la lista de cadenas distintas, ordenada y deduplicada, SIN
frecuencias, SIN documento de origen, SIN spread, SIN volumen y SIN
porcentajes. La normalización de cadenas a familias la hace la autora A CIEGAS
sobre esta lista pelada (paso 7 de la secuencia), y recién después se computa
cualquier conteo (paso 9). Si la salida trajera frecuencias u origen, la
normalización dejaría de ser ciega y el blindaje caería. Por eso el archivo de
salida NO lleva encabezado, ni comentarios, ni totales: sólo las cadenas.

Este módulo LEE los jsonl de extracción. No los escribe, no los modifica y no
toca el pipeline.

CANALES
-------
Por analogía estricta con `sujeto_propuesto` —que no existe en el crudo del
modelo y lo agrega el validador al normalizar—, los tres canales viven en el
bloque `validacion` de cada registro:

  tipo_propuesto       -> validacion.entidades[i].tipo_propuesto
  predicado_propuesto  -> validacion.relaciones[i].predicado_propuesto
  sujeto_propuesto     -> validacion.relaciones[i].sujeto_propuesto

Los dos primeros NO existen todavía en el pipeline: su implementación es otra
unidad. El instrumento corre igual sobre los jsonl actuales y devuelve lista
vacía para esos canales, sin romperse y sin inventar (§ "AUSENCIA TOLERADA").

`sujeto_propuesto` es el ÚNICO canal abierto que hoy tiene datos, y está acá
como canal de validación del instrumento — ancla del selftest sobre datos
reales. NO es insumo de ESQ-1: el laudo (D5, §7.3) excluye los sujetos de
T_fam y P_fam.

FORMATO DE SALIDA
-----------------
Texto plano UTF-8, una cadena por línea, terminada en LF, ordenada por punto de
código Unicode (`sorted()` de Python, sin locale) y deduplicada por igualdad
exacta de cadena. Un canal por archivo de salida. Determinístico y
re-derivable por un tercero desde la misma corrida: mismas entradas -> mismos
bytes, cualquiera sea el orden en que se pasen los archivos.

Las cadenas se emiten VERBATIM, sin recortar espacios: recortarlas sería una
normalización, y toda normalización es del paso 7, no del instrumento. Un valor
cuyo `strip()` sea vacío se trata como ausente. Si alguna cadena distinta
contuviera un salto de línea o un retorno de carro, el formato de una-por-línea
dejaría de ser reversible: en ese caso el instrumento ABORTA con error en vez
de emitir una lista ambigua.

El resumen de corrida (canal, cantidad de archivos, cantidad de cadenas) va a
STDERR, nunca al archivo de salida.

USO
---
  .venv/bin/python -B data/experiment/esq/code/cadenas_esq.py \
      --canal sujeto_propuesto \
      --salida /ruta/cadenas_sujeto.txt \
      data/experiment/reextraccion_v2/corpus_v2/salida/*/extracciones_e1.jsonl

Sin `--salida`, la lista va a stdout. Nada está cableado: canal y rutas son
parámetros explícitos.

CÓDIGOS DE SALIDA
-----------------
  0  corrida completa (incluye el caso de lista vacía)
  2  error de datos o de uso (json inválido, campo con tipo inesperado,
     archivo inexistente, cadena con salto de línea)
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# --------------------------------------------------------------------------- #
# Canales: nombre -> (contenedor dentro de `validacion`, campo)               #
# --------------------------------------------------------------------------- #
CANALES = {
    "tipo_propuesto": ("entidades", "tipo_propuesto"),
    "predicado_propuesto": ("relaciones", "predicado_propuesto"),
    "sujeto_propuesto": ("relaciones", "sujeto_propuesto"),
}


class ErrorDeDatos(Exception):
    """Anomalía en la entrada que el instrumento no puede resolver sin decidir."""


def cadenas_distintas(rutas, canal):
    """Devuelve la lista ordenada y deduplicada de cadenas del `canal`.

    `rutas`: iterable de Path a jsonl de extracción E1.
    `canal`: clave de CANALES.

    Un registro sin bloque `validacion`, o sin el contenedor, o sin el campo,
    no aporta cadenas y no es un error: es el caso de AUSENCIA TOLERADA.
    """
    if canal not in CANALES:
        raise ErrorDeDatos(
            f"canal desconocido: {canal!r} (conocidos: {sorted(CANALES)})")
    contenedor, campo = CANALES[canal]

    distintas = set()
    for ruta in rutas:
        ruta = Path(ruta)
        if not ruta.is_file():
            raise ErrorDeDatos(f"no es un archivo legible: {ruta}")
        with ruta.open(encoding="utf-8") as fh:
            for nlinea, linea in enumerate(fh, start=1):
                if not linea.strip():
                    continue
                try:
                    registro = json.loads(linea)
                except json.JSONDecodeError as exc:
                    raise ErrorDeDatos(
                        f"json inválido en {ruta}:{nlinea}: {exc}") from exc
                if not isinstance(registro, dict):
                    raise ErrorDeDatos(
                        f"la línea {ruta}:{nlinea} no es un objeto json")
                validacion = registro.get("validacion")
                if not isinstance(validacion, dict):
                    continue                       # ausencia tolerada
                items = validacion.get(contenedor)
                if not isinstance(items, list):
                    continue                       # ausencia tolerada
                for i, item in enumerate(items):
                    if not isinstance(item, dict):
                        continue
                    valor = item.get(campo)
                    if valor is None:
                        continue                   # ausencia tolerada
                    if not isinstance(valor, str):
                        raise ErrorDeDatos(
                            f"{ruta}:{nlinea} validacion.{contenedor}[{i}]."
                            f"{campo} no es cadena: {type(valor).__name__}")
                    if not valor.strip():
                        continue                   # vacío == ausente
                    distintas.add(valor)

    for cadena in distintas:
        if "\n" in cadena or "\r" in cadena:
            raise ErrorDeDatos(
                "una cadena distinta contiene un salto de línea: el formato de "
                "una-por-línea dejaría de ser reversible. Resolverlo antes de "
                f"seguir. Repr: {cadena!r}")
    return sorted(distintas)


def render(cadenas):
    """Bytes exactos de la salida: una cadena por línea, LF, sin encabezado."""
    return "".join(c + "\n" for c in cadenas)


def main(argv=None):
    ap = argparse.ArgumentParser(
        prog="cadenas_esq.py",
        description="Lista de cadenas distintas de un canal abierto de los "
                    "jsonl de extracción E1, sin frecuencias ni origen.")
    ap.add_argument("--canal", required=True, choices=sorted(CANALES),
                    help="canal a inventariar")
    ap.add_argument("--salida", default=None,
                    help="archivo de salida (por defecto, stdout)")
    ap.add_argument("entradas", nargs="+",
                    help="jsonl de extracción a leer")
    args = ap.parse_args(argv)

    try:
        cadenas = cadenas_distintas(args.entradas, args.canal)
    except ErrorDeDatos as exc:
        print(f"cadenas_esq: ERROR: {exc}", file=sys.stderr)
        return 2

    texto = render(cadenas)
    if args.salida:
        destino = Path(args.salida)
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text(texto, encoding="utf-8")
        donde = str(destino)
    else:
        sys.stdout.write(texto)
        donde = "stdout"

    # Resumen a stderr: nunca al archivo de salida.
    print(f"cadenas_esq: canal={args.canal} entradas={len(args.entradas)} "
          f"distintas={len(cadenas)} salida={donde}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
