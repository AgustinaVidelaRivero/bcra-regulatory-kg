"""Construye el inventario de Textos Ordenados del BCRA a escalar.

Fuente: el endpoint que alimenta la lista renderizada en
https://www.bcra.gob.ar/ordenamiento-y-resumenes/ (la página monta la lista por
JS; el JS de la vista — Divi-BCRA/js/ordenamiento-y-resumenes-app.js, const
CONFIG.apiUrl — la pide a /api/endpoints/ordenamiento-y-resumenes.php?lang=es).
La respuesta cruda queda congelada en ../indice_oficial_raw.json y ESE archivo
es la fuente de este inventario: el script no vuelve a tocar la red.

Reglas:
  - dedup por URL (el índice publica t-optico.pdf dos veces, en dos entradas de
    título distinto);
  - se excluyen los 5 TOs del subset congelado (data/experiment/subset/),
    identificados por nombre de archivo publicado;
  - identificador corto propuesto = stem del archivo oficial, sin prefijo 't-',
    minúsculas, no alfanuméricos a '_'. Es función del nombre publicado por el
    BCRA, así que es estable y auditable contra la fuente.

Salida: ../inventario_tos.csv
"""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path

AQUI = Path(__file__).resolve().parent
PREP = AQUI.parent

# archivos publicados que corresponden a los 5 TOs del subset congelado,
# con el id interno que ya usa el pipeline (data/experiment/subset/)
SUBSET = {
    "t-excbio.pdf": "ext",
    "t-capmin.pdf": "cap",
    "t-cladeu.pdf": "cla",
    "t-pusf.pdf": "pro",
    "t-RI-CM.pdf": "ric",
}

CATEGORIAS = [
    ("normativa_general", "textos_ordenados"),
    ("regimen_informativo", "regimenes_informativos"),
]


def id_corto(archivo: str) -> str:
    stem = archivo.rsplit(".", 1)[0].lower()
    stem = re.sub(r"^t-", "", stem)
    return re.sub(r"[^a-z0-9]+", "_", stem).strip("_")


def main() -> None:
    crudo = json.loads((PREP / "indice_oficial_raw.json").read_text(encoding="utf-8"))

    filas: list[dict] = []
    vistos: dict[str, str] = {}          # url -> id ya emitido
    duplicados: list[tuple[str, str]] = []
    excluidos: list[tuple[str, str]] = []

    for categoria, clave in CATEGORIAS:
        for it in crudo[clave]:
            archivo, url, titulo = it["archivo"], it["url"], it["titulo"]
            if archivo in SUBSET:
                excluidos.append((SUBSET[archivo], titulo))
                continue
            if url in vistos:
                duplicados.append((url, titulo))
                continue
            ident = id_corto(archivo)
            vistos[url] = ident
            filas.append({
                "id": ident,
                "categoria": categoria,
                "titulo_oficial": titulo,
                "archivo_oficial": archivo,
                "url_pdf": url,
            })

    ids = [f["id"] for f in filas]
    assert len(set(ids)) == len(ids), "ids cortos no únicos"

    destino = PREP / "inventario_tos.csv"
    with destino.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["id", "categoria", "titulo_oficial",
                                           "archivo_oficial", "url_pdf"])
        w.writeheader()
        w.writerows(filas)

    resumen = {
        "entradas_indice": sum(len(crudo[c]) for _, c in CATEGORIAS),
        "urls_unicas": len({it["url"] for _, c in CATEGORIAS for it in crudo[c]}),
        "duplicados_descartados": [{"url": u, "titulo": t} for u, t in duplicados],
        "subset_excluido": [{"id_interno": i, "titulo": t} for i, t in excluidos],
        "filas_inventario": len(filas),
        "por_categoria": {cat: sum(1 for f in filas if f["categoria"] == cat)
                          for cat, _ in CATEGORIAS},
    }
    (PREP / "inventario_resumen.json").write_text(
        json.dumps(resumen, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(resumen, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
