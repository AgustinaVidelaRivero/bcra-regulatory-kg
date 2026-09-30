"""
conteo_lectura.py — U-LECTURA-LIMITA, etapa L1: control y conteo de la lectura
asistida de la muestra sellada de 30 aristas `limita` (USD 0).

Mandato: docs/mandatos/ULECTURA_LIMITA_lectura_asistida.md (firmado el
30/09/2026). Solo lectura: no llama a ninguna API, no usa Neo4j y no escribe
ningún archivo; imprime el resultado por la salida estándar.

Uso (desde la raíz del repo):
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B reports/u_umbral/lectura_limita/conteo_lectura.py

Controles sobre la copia de trabajo lectura_limita_30.csv contra la planilla
sellada reports/u_umbral/muestra_limita_30.csv (sellada en e4d053b):
  - encabezado = columnas de la planilla + veredicto, justificación,
    destino_esperado y revision_autora;
  - 30 filas, en el orden de la planilla, con los mismos n_sorteo,
    restriccion_id y operacion_id, y con las columnas de la planilla sin cambios;
  - veredicto en {sí, no, no decidible}, justificación no vacía y
    destino_esperado presente solo cuando el veredicto es «no».

Conteo: veredictos de la columna `veredicto` (la lectura asistida). La columna
`revision_autora` no se aplica: solo se informa cuántas celdas tienen texto.

Intervalo de Wilson al 95 % para «sí», sobre los 30 y sobre los decididos
(«sí» + «no»), con z = 1.959963984540054, la misma constante que
reports/tanda0/obs12_lectura/fila_obs12.md («Reproducción»).

Salida determinística (sin fechas ni rutas absolutas): la doble corrida tiene
que dar el mismo texto byte a byte. Código de salida 1 si falla un control.
"""

import csv
import hashlib
import math
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
SELLADA = Path("reports/u_umbral/muestra_limita_30.csv")
COPIA = Path("reports/u_umbral/lectura_limita/lectura_limita_30.csv")
SHA_SELLADA = "8e9818173100ac880c7bdc34121a4f4e66916e42b16636421f5e4e993512b2a9"
COLUMNAS_NUEVAS = ["veredicto", "justificación", "destino_esperado", "revision_autora"]
VEREDICTOS = ["sí", "no", "no decidible"]
Z = 1.959963984540054


def sha256(ruta):
    return hashlib.sha256((RAIZ / ruta).read_bytes()).hexdigest()


def leer(ruta):
    with (RAIZ / ruta).open(encoding="utf-8", newline="") as f:
        filas = list(csv.reader(f))
    return filas[0], filas[1:]


def wilson(k, n):
    p = k / n
    den = 1 + Z * Z / n
    centro = (p + Z * Z / (2 * n)) / den
    medio = Z * math.sqrt(p * (1 - p) / n + Z * Z / (4 * n * n)) / den
    return centro - medio, centro + medio


def main():
    errores = []
    print("U-LECTURA-LIMITA · L1 · conteo de la lectura asistida")
    sha_s = sha256(SELLADA)
    print(f"planilla sellada: {SELLADA} sha256 {sha_s}")
    if sha_s != SHA_SELLADA:
        errores.append("sha256 de la planilla sellada distinto del sellado en e4d053b")
    print(f"copia de trabajo: {COPIA} sha256 {sha256(COPIA)}")

    enc_s, filas_s = leer(SELLADA)
    enc_c, filas_c = leer(COPIA)
    if enc_c != enc_s + COLUMNAS_NUEVAS:
        errores.append("encabezado de la copia distinto de planilla + columnas nuevas")
    if len(filas_s) != 30 or len(filas_c) != 30:
        errores.append(f"filas: planilla {len(filas_s)}, copia {len(filas_c)} (se esperan 30)")

    i_n = enc_s.index("n_sorteo")
    i_r = enc_s.index("restriccion_id")
    i_o = enc_s.index("operacion_id")
    ancho = len(enc_s)
    conteo = {v: 0 for v in VEREDICTOS}
    revisadas = 0
    for pos, (fs, fc) in enumerate(zip(filas_s, filas_c), start=1):
        if len(fc) != len(enc_s) + len(COLUMNAS_NUEVAS):
            errores.append(f"fila {pos}: {len(fc)} columnas")
            continue
        if (fs[i_n], fs[i_r], fs[i_o]) != (fc[i_n], fc[i_r], fc[i_o]):
            errores.append(f"fila {pos}: n_sorteo o ids distintos de la planilla")
        if fs != fc[:ancho]:
            errores.append(f"fila {pos}: columnas de la planilla modificadas")
        veredicto, justificacion, destino, revision = fc[ancho:]
        if veredicto not in conteo:
            errores.append(f"fila {pos}: veredicto fuera de la lista: {veredicto!r}")
            continue
        conteo[veredicto] += 1
        if not justificacion.strip():
            errores.append(f"fila {pos}: justificación vacía")
        if (veredicto == "no") != bool(destino.strip()):
            errores.append(f"fila {pos}: destino_esperado inconsistente con el veredicto")
        if revision.strip():
            revisadas += 1

    total = sum(conteo.values())
    decididos = conteo["sí"] + conteo["no"]
    print("")
    print("veredictos (lectura asistida):")
    for v in VEREDICTOS:
        print(f"  {v}: {conteo[v]}")
    print(f"  total: {total}")
    print(f"revision_autora con texto: {revisadas}")
    if total != 30:
        errores.append(f"los veredictos suman {total}, no 30")
    print("")
    print("intervalo de Wilson al 95 % para «sí»:")
    for nombre, n in (("sobre los 30", total), ("sobre los decididos", decididos)):
        if n:
            lo, hi = wilson(conteo["sí"], n)
            print(f"  {nombre}: {conteo['sí']}/{n} = {conteo['sí'] / n:.3f}; IC95 {lo:.3f}–{hi:.3f}")
    print("")
    for e in errores:
        print(f"ERROR: {e}")
    print("controles: " + ("FALLAN" if errores else "OK"))
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
