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

BLOQUES
-------
Cada registro del jsonl guarda DOS versiones de lo que el extractor emitió:

  crudo       -> `tool_input_crudo`, el tool_input tal como lo devolvió el
                 modelo, antes de que el validador lo mire.
  validacion  -> `validacion`, lo que sobrevivió a la validación.

ESQ-1 mide sobre el CRUDO. La fe de erratas
`docs/fe_erratas_prerregistro_esq1_alcance.md` (b) lo decidió así: leer del
validado descarta propuestas por motivos ajenos a la propuesta misma —la
relación que la transportaba falló firma o predicado—, y esa pérdida
correlaciona con la señal que ESQ-1 mide, o sea que sesga hacia el resultado
cómodo. El bloque `validacion` sigue disponible porque la BRECHA entre ambos
números es un dato propio que ESQ-1 reporta.

El bloque es un parámetro explícito, sin valor por defecto: el instrumento se
niega a correr si quien lo invoca no declara cuál de los dos está midiendo.
Sobre los cinco jsonl de producción de hoy los dos números difieren, así que un
default silencioso decidiría por el usuario cuál es el número de ESQ-1.

CANALES
-------
Los nombres de contenedor NO son los mismos en los dos bloques: el crudo usa
las claves en inglés del tool schema y el validado las castellaniza. Por eso la
tabla es por par (bloque, canal) y no por canal solo:

  bloque      canal                  ruta dentro del registro
  ----------  ---------------------  -------------------------------------------
  crudo       tipo_propuesto         tool_input_crudo.entities[i].tipo_propuesto
  crudo       predicado_propuesto    tool_input_crudo.relations[i].predicado_propuesto
  crudo       sujeto_propuesto       tool_input_crudo.relations[i].sujeto_propuesto
  validacion  tipo_propuesto         validacion.entidades[i].tipo_propuesto
  validacion  predicado_propuesto    validacion.relaciones[i].predicado_propuesto
  validacion  sujeto_propuesto       validacion.relaciones[i].sujeto_propuesto

`tipo_propuesto` y `predicado_propuesto` —el canal abierto— NO existen todavía
en el pipeline: su implementación es otra unidad. Verificado sobre los cinco
jsonl de producción, los cuatro caminos dan cero ocurrencias:

  jq -r '.tool_input_crudo.entities[]? | select(type=="object") | .tipo_propuesto | select(.!=null)' \
     data/experiment/reextraccion_v2/corpus_v2/salida/*/extracciones_e1.jsonl | wc -l   # 0
  jq -r '.tool_input_crudo.relations[]? | select(type=="object") | .predicado_propuesto | select(.!=null)' \
     data/experiment/reextraccion_v2/corpus_v2/salida/*/extracciones_e1.jsonl | wc -l   # 0
  jq -r '.validacion.entidades[]?  | .tipo_propuesto      | select(.!=null)' \
     data/experiment/reextraccion_v2/corpus_v2/salida/*/extracciones_e1.jsonl | wc -l   # 0
  jq -r '.validacion.relaciones[]? | .predicado_propuesto | select(.!=null)' \
     data/experiment/reextraccion_v2/corpus_v2/salida/*/extracciones_e1.jsonl | wc -l   # 0

El instrumento corre igual y devuelve lista vacía para esos canales EN LOS DOS
BLOQUES, sin romperse y sin inventar (§ "AUSENCIA TOLERADA").

`sujeto_propuesto` es el ÚNICO canal abierto que hoy tiene datos, y está acá
como canal de validación del instrumento — ancla del selftest sobre datos
reales. NO es insumo de ESQ-1: el laudo (D5, §7.3) excluye los sujetos de
T_fam y P_fam.

AUSENCIA TOLERADA
-----------------
Un registro sin el bloque, o cuyo contenedor no es una lista, o cuyo campo no
está, no aporta cadenas y no es un error. Vale la pena declarar una
consecuencia medida de esa regla en el bloque crudo: 7 de los 1769 registros de
producción tienen el contenedor con un tipo distinto de lista, y el instrumento
los saltea como ausentes.

  .venv/bin/python -B -c "
  import json,glob,collections
  t=collections.Counter()
  for r in sorted(glob.glob('data/experiment/reextraccion_v2/corpus_v2/salida/*/extracciones_e1.jsonl')):
      for l in open(r,encoding='utf-8'):
          c=json.loads(l)['tool_input_crudo']
          t[(type(c.get('entities')).__name__, type(c.get('relations')).__name__)]+=1
  print(dict(t))"
  # {('list','list'): 1762, ('list','NoneType'): 3, ('NoneType','NoneType'): 1,
  #  ('str','NoneType'): 3}

Los cuatro con `NoneType` son cortes por `max_tokens`; los tres con `str` son
tool_input parcial, con el json de `entities` a medio emitir. En `validacion`
los 1769 registros tienen ambos contenedores como lista, y por eso la asimetría
sólo aparece en el crudo. Hoy no cambia ningún número —esos 7 registros no
aportan `sujeto_propuesto` y el canal abierto todavía no existe—, pero cuando
el canal abierto se implemente serán 7 registros que el instrumento no lee.
Elevarlos a error sería una decisión de diseño nueva, y esta unidad no la toma:
quedan declarados y asertados en el selftest para que no pasen inadvertidos.

FORMATO DE SALIDA
-----------------
Texto plano UTF-8, una cadena por línea, terminada en LF, ordenada por punto de
código Unicode (`sorted()` de Python, sin locale) y deduplicada por igualdad
exacta de cadena. Un par (bloque, canal) por archivo de salida. Determinístico
y re-derivable por un tercero desde la misma corrida: mismas entradas -> mismos
bytes, cualquiera sea el orden en que se pasen los archivos.

Las cadenas se emiten VERBATIM, sin recortar espacios: recortarlas sería una
normalización, y toda normalización es del paso 7, no del instrumento. Un valor
cuyo `strip()` sea vacío se trata como ausente. Si alguna cadena distinta
contuviera un salto de línea o un retorno de carro, el formato de una-por-línea
dejaría de ser reversible: en ese caso el instrumento ABORTA con error en vez
de emitir una lista ambigua.

El resumen de corrida (bloque, canal, cantidad de archivos, cantidad de
cadenas) va a STDERR, nunca al archivo de salida.

USO
---
  .venv/bin/python -B data/experiment/esq/code/cadenas_esq.py \
      --bloque crudo \
      --canal sujeto_propuesto \
      --salida /ruta/cadenas_sujeto_crudo.txt \
      data/experiment/reextraccion_v2/corpus_v2/salida/*/extracciones_e1.jsonl

Sin `--salida`, la lista va a stdout. Nada está cableado: bloque, canal y rutas
son parámetros explícitos, y `--bloque` y `--canal` son obligatorios.

CÓDIGOS DE SALIDA
-----------------
  0  corrida completa (incluye el caso de lista vacía)
  2  error de datos o de uso (json inválido, campo con tipo inesperado,
     archivo inexistente, cadena con salto de línea, bloque o canal omitido)
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# --------------------------------------------------------------------------- #
# Bloques: nombre de CLI -> clave del bloque dentro del registro jsonl         #
# --------------------------------------------------------------------------- #
BLOQUES = {
    "crudo": "tool_input_crudo",
    "validacion": "validacion",
}

# --------------------------------------------------------------------------- #
# Canales: (bloque, canal) -> (contenedor dentro del bloque, campo)            #
#                                                                             #
# La clave es el PAR porque los contenedores no se llaman igual en los dos     #
# bloques: el crudo conserva las claves del tool schema (entities/relations),  #
# el validado las castellaniza (entidades/relaciones).                         #
# --------------------------------------------------------------------------- #
CANALES = {
    ("crudo", "tipo_propuesto"): ("entities", "tipo_propuesto"),
    ("crudo", "predicado_propuesto"): ("relations", "predicado_propuesto"),
    ("crudo", "sujeto_propuesto"): ("relations", "sujeto_propuesto"),
    ("validacion", "tipo_propuesto"): ("entidades", "tipo_propuesto"),
    ("validacion", "predicado_propuesto"): ("relaciones", "predicado_propuesto"),
    ("validacion", "sujeto_propuesto"): ("relaciones", "sujeto_propuesto"),
}

NOMBRES_CANAL = sorted({canal for _, canal in CANALES})


class ErrorDeDatos(Exception):
    """Anomalía en la entrada que el instrumento no puede resolver sin decidir."""


def cadenas_distintas(rutas, canal, bloque):
    """Devuelve la lista ordenada y deduplicada de cadenas del `canal` leído
    dentro del `bloque`.

    `rutas`:  iterable de Path a jsonl de extracción E1.
    `canal`:  uno de NOMBRES_CANAL.
    `bloque`: clave de BLOQUES. No tiene valor por defecto a propósito: los dos
              bloques dan números distintos y el instrumento no elige por el
              usuario cuál se está midiendo.

    Un registro sin el bloque, o sin el contenedor, o con el contenedor de un
    tipo que no es lista, o sin el campo, no aporta cadenas y no es un error:
    es el caso de AUSENCIA TOLERADA.
    """
    if bloque not in BLOQUES:
        raise ErrorDeDatos(
            f"bloque desconocido: {bloque!r} (conocidos: {sorted(BLOQUES)})")
    if (bloque, canal) not in CANALES:
        raise ErrorDeDatos(
            f"canal desconocido para el bloque {bloque!r}: {canal!r} "
            f"(conocidos: {NOMBRES_CANAL})")
    clave_bloque = BLOQUES[bloque]
    contenedor, campo = CANALES[(bloque, canal)]

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
                contenido = registro.get(clave_bloque)
                if not isinstance(contenido, dict):
                    continue                       # ausencia tolerada
                items = contenido.get(contenedor)
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
                            f"{ruta}:{nlinea} {clave_bloque}.{contenedor}[{i}]."
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
    ap.add_argument("--bloque", required=True, choices=sorted(BLOQUES),
                    help="bloque del registro a leer: 'crudo' es "
                         "tool_input_crudo (el que mide ESQ-1) y 'validacion' "
                         "es lo que sobrevivió a la validación. Obligatorio: "
                         "los dos dan números distintos.")
    ap.add_argument("--canal", required=True, choices=NOMBRES_CANAL,
                    help="canal a inventariar")
    ap.add_argument("--salida", default=None,
                    help="archivo de salida (por defecto, stdout)")
    ap.add_argument("entradas", nargs="+",
                    help="jsonl de extracción a leer")
    args = ap.parse_args(argv)

    try:
        cadenas = cadenas_distintas(args.entradas, args.canal, args.bloque)
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
    print(f"cadenas_esq: canal={args.canal} bloque={args.bloque} "
          f"entradas={len(args.entradas)} distintas={len(cadenas)} "
          f"salida={donde}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
