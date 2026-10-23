"""La lista de los códigos que no se unen de la regla C1 (--union-comunicaciones de tanda0/code/ensamblar_tanda0.py), desde la hoja
sellada del censo de sus colisiones: una colisión mal unida no se une, se declara, y el resto de C1 sigue.

La hoja es un CSV (separado por tabuladores si su extensión es .tsv) con exactamente las columnas colision, codigo_normalizado, nodos,
decision y nota, una fila por colisión. La decisión de cada fila es une_bien o une_mal: a la lista van los códigos normalizados de las
filas une_mal. Frena, nombrando la fila por su número de línea en la hoja y sin mostrar su texto, si:
  - el sha256 de la hoja no es el que se pasa;
  - faltan columnas o sobran;
  - una fila tiene la decisión vacía o distinta de une_bien y une_mal;
  - una fila une_mal no tiene código normalizado;
  - dos filas tienen el mismo código normalizado.
Escribe {"no_unir": [<codigo_normalizado>, ...]} (ordenada, sin repetidos; vacía si no hay filas une_mal) y da su sha256, que va con la
lista a --union-comunicaciones-sha256. Imprime solo cuentas y sha256, nunca un código. No escribe nada si frena. USD 0, sin API.

Uso: python3 -I -B armar_no_unir_c1.py --hoja <hoja.csv> --hoja-sha256 <sha256> --salida <no_unir_c1.json>
"""
import argparse
import csv
import hashlib
import io
import json
import sys
from pathlib import Path

COLUMNAS = ("colision", "codigo_normalizado", "nodos", "decision", "nota")
DECISIONES = ("une_bien", "une_mal")


class Freno(Exception):
    pass


def armar(datos: bytes, separador: str) -> tuple[list[str], dict]:
    """Las filas de la hoja → (la lista ordenada de los códigos une_mal, las cuentas). Frena con Freno."""
    lector = csv.DictReader(io.StringIO(datos.decode("utf-8-sig"), newline=""), delimiter=separador)
    cols = tuple(lector.fieldnames or ())
    if sorted(cols) != sorted(COLUMNAS):
        raise Freno(f"la hoja no tiene exactamente las columnas {', '.join(COLUMNAS)} "
                    f"(faltan {len(set(COLUMNAS) - set(cols))}, sobran {len(set(cols) - set(COLUMNAS))})")
    por_codigo: dict[str, int] = {}
    une_mal, cuentas = set(), {"filas": 0, "une_bien": 0, "une_mal": 0}
    for fila in lector:
        linea = lector.line_num
        if None in fila or any(v is None for v in fila.values()):
            raise Freno(f"fila de la línea {linea}: no tiene las {len(COLUMNAS)} columnas")
        decision = fila["decision"].strip()
        if not decision:
            raise Freno(f"fila de la línea {linea}: la decisión está vacía")
        if decision not in DECISIONES:
            raise Freno(f"fila de la línea {linea}: la decisión no es une_bien ni une_mal")
        codigo = fila["codigo_normalizado"].strip()
        if decision == "une_mal" and not codigo:
            raise Freno(f"fila de la línea {linea}: une_mal sin código normalizado")
        if codigo and codigo in por_codigo:
            raise Freno(f"filas de las líneas {por_codigo[codigo]} y {linea}: el mismo código normalizado")
        if codigo:
            por_codigo[codigo] = linea
        cuentas["filas"] += 1
        cuentas[decision] += 1
        if decision == "une_mal":
            une_mal.add(codigo)
    return sorted(une_mal), cuentas


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--hoja", type=Path, required=True, help="la hoja sellada del censo de las colisiones (CSV)")
    ap.add_argument("--hoja-sha256", required=True, help="el sha256 de la hoja sellada: si no coincide, frena")
    ap.add_argument("--salida", type=Path, required=True, help="el JSON de la lista; no se pisa si ya existe")
    a = ap.parse_args()
    datos = a.hoja.read_bytes()
    try:
        sha_hoja = hashlib.sha256(datos).hexdigest()
        if sha_hoja != a.hoja_sha256:
            raise Freno(f"la hoja tiene sha256 {sha_hoja}, no {a.hoja_sha256}")
        if a.salida.exists():
            raise Freno(f"{a.salida} ya existe")
        lista, cuentas = armar(datos, "\t" if a.hoja.suffix.lower() == ".tsv" else ",")
    except Freno as e:
        print(f"FRENO: {e}", file=sys.stderr)
        return 1
    texto = json.dumps({"no_unir": lista}, ensure_ascii=False, indent=1) + "\n"
    a.salida.parent.mkdir(parents=True, exist_ok=True)
    a.salida.write_text(texto, encoding="utf-8")
    sha = hashlib.sha256(texto.encode("utf-8")).hexdigest()
    print(json.dumps({"hoja_sha256": sha_hoja, **cuentas, "codigos_en_la_lista": len(lista), "lista": str(a.salida),
                      "lista_sha256": sha}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
