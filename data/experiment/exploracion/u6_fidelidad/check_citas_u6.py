#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verifica que cada cita_textual de criterios_u6.json aparezca como subcadena exacta
del texto extraído del PDF del TO correspondiente.

Normalización aplicada al texto extraído (y a NADA más):
  1. Guiones de corte de línea propios de la extracción: una letra minúscula, seguida
     de '-' y salto de línea, seguida de letra minúscula -> se elimina el guion y el salto.
  2. Saltos de línea (con el espacio en blanco que los rodea) -> un único espacio.
No se aplica ninguna otra normalización (ni de mayúsculas, ni de tildes, ni de comillas,
ni de espacios internos). La cita se busca tal cual está escrita en el JSON.
"""
import json, re, subprocess, sys, os

BASE = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(BASE, "criterios_u6.json")

PDFS = {
    "ext": "TO_exterior_cambios_actual.pdf",
    "cap": "TO_capitales_minimos_actual.pdf",
    "cla": "TO_clasificacion_deudores_actual.pdf",
    "ric": "TO_regimen_informativo_contable_mensual_actual.pdf",
    "pro": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
}


def extract(pdf_path):
    res = subprocess.run(["pdftotext", "-enc", "UTF-8", pdf_path, "-"],
                         capture_output=True, check=True)
    return res.stdout.decode("utf-8")


def normalize(text):
    text = re.sub(r"(?<=[a-záéíóúñü])-\n(?=[a-záéíóúñü])", "", text)  # guiones de corte de línea
    text = re.sub(r"\s*\n\s*", " ", text)                             # saltos de línea -> espacio
    return text


def main():
    with open(JSON_PATH, encoding="utf-8") as f:
        data = json.load(f)

    textos = {}
    for to, fn in PDFS.items():
        path = os.path.join(BASE, fn)
        raw = extract(path)
        textos[to] = normalize(raw)
        print(f"[extract] {to}: {fn} -> {len(raw)} chars crudos, {len(textos[to])} chars normalizados")

    total = ok = 0
    fallas = []
    for p in data["preguntas"]:
        to = p["to"]
        for i, c in enumerate(p["gold"]["criterios"], 1):
            total += 1
            cita = c["cita_textual"]
            if cita in textos[to]:
                ok += 1
            else:
                fallas.append((p["id"], to, p["gold"]["ancla"], i, cita))

    print()
    print(f"Preguntas en el JSON: {len(data['preguntas'])}")
    print(f"Total de citas: {total}")
    print(f"Citas que verifican: {ok}")
    print(f"Citas que NO verifican: {len(fallas)}")
    for pid, to, ancla, i, cita in fallas:
        print(f"\n--- NO VERIFICA: {pid} (to={to}, ancla={ancla}) criterio #{i}")
        print(cita)
    return 0 if not fallas else 1


if __name__ == "__main__":
    sys.exit(main())
