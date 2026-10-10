"""Escribe limites_O1.md desde limites_O1.json y las salidas de O1 (solo lee las salidas). Uso: python limites_md.py <salidas> <out.md>"""
import json, sys
from pathlib import Path
s = Path(sys.argv[1]); d = json.loads((s / "limites_O1.json").read_text(encoding="utf-8"))
cl = json.loads((s / "grupos_C_L_diez.json").read_text(encoding="utf-8"))
L = ["# U-OMISIONES-COD, O1 — límites y residuos, caso por caso", "",
     "Generado por `scripts/limites_md.py` desde `salidas/limites_O1.json` (de `scripts/limites_O1.py`). Páginas: las de la "
     "unidad en la E0 r2b. «sin leer»: no leí el caso; el mecanismo es una hipótesis o falta.", ""]
L += ["## Grupo L: elementos que conservan la cuantía (6)", "", "| unidad | páginas | cuantía | tramo de E1 | mecanismo |", "|---|---|---|---|---|"]
L += [f"| `{x['unidad']}` | {x['paginas']} | «{x['cuantia']}» | «{x['tramo_e1']}» | {x['mecanismo']} |" for x in d["L_conservan_la_cuantia"]]
f = d["f_conjunto_de_51"]
L += ["", f"## Grupo B, f: menciones que verifican sin el artículo inicial y siguen sin verificar ({len(f['quedan'])} de {f['n']})", "",
      "El conjunto lo reconstruí con la definición de R2-1 (mención que no verifica y verifica sin su artículo inicial): da "
      f"{f['n']} relaciones, no 51. Pasan {f['pasan']}. La expansión de contracciones solo alcanza al artículo «el» (en «del» y "
      "«al»): con «la» y «los» no hay contracción, y por construcción esas menciones no pasan. «las entidades» es la expresión "
      "colectiva de R3, que R2-1 dejó fuera de sus 51.", "", "| unidad | páginas | relación | mención | mecanismo |", "|---|---|---|---|---|"]
def mec(m):
    w = m.split()[0].lower()
    return ("artículo «la»/«las»/«los»: sin contracción que expandir" if w in ("la", "las", "los") else "sin leer")
L += [f"| `{x['unidad']}` | {x['paginas']} | {x['indice_relacion']} | «{x['mencion']}» | {mec(x['mencion'])} |" for x in f["quedan"]]
L += ["", f"## Grupo A, a: omisiones con el tramo en el orden de lectura, sin la marca ({len(d['a_orden_de_lectura_sin_marca'])})", "",
      "| unidad | páginas | categoría | tramo | mecanismo |", "|---|---|---|---|---|"]
L += [f"| `{x['unidad']}` | {x['paginas']} | {x['categoria']} | «{x['tramo']}» | {x['mecanismo']} |" for x in d["a_orden_de_lectura_sin_marca"]]
L += ["", f"## Grupo A, d: entidades de T4 con un supuesto dentro que la marca no detecta ({len(d['d_positivas_T4_no_detectadas'])})", "",
      "| unidad | entidad | páginas | supuestos de T4 | mecanismo |", "|---|---|---|---|---|"]
L += [f"| `{x['unidad']}` | {x['entidad']} | {x['paginas']} | {'; '.join(x['supuestos_de_T4'])} | {x['mecanismo']} |" for x in d["d_positivas_T4_no_detectadas"]]
L += ["", f"## Grupo A, e: en el conjunto de diseño de T4, copias reales no detectadas ({len(d['e_copias_reales_de_T4_no_detectadas'])}) y detecciones que T4 no leyó como copia ({len(d['e_falsos_positivos_de_T4'])})", "",
      "| caso T4 | unidad | páginas | clase de T4 | razón de T4 | mecanismo |", "|---|---|---|---|---|---|"]
L += [f"| {x['caso_T4']} | `{x['unidad']}` | {x['paginas']} | copia real | {x['razon_T4']} | {x['mecanismo']} |" for x in d["e_copias_reales_de_T4_no_detectadas"]]
L += [f"| {x['caso_T4']} | `{x['unidad']}` | — | {x['clase_T4']} | {x['razon_T4']} | sin leer |" for x in d["e_falsos_positivos_de_T4"]]
L += ["", f"## Grupo H: Comunicacion con `tipo_no_derivable` ({len(d['H_tipo_no_derivable'])})", "",
      "Quedan como error de extracción declarado (v7). Mecanismo de las 26: el código y la etiqueta no nombran una Comunicación "
      "ni una norma externa (remisión a un punto o una sección, o el nombre de un TO u otro documento).", "",
      "| nodo | código | unidades |", "|---|---|---|"]
L += [f"| `{x['nodo']}` | «{x['codigo']}» | {', '.join(x['unidades'])} |" for x in d["H_tipo_no_derivable"]]
c = cl["C"]
L += ["", "## Grupo C: lo que queda marcado o sin base (la cifra de la v7; lista entera en `salidas/grupos_C_L_diez.json`, `C.lista`)", "",
      f"De los 264 elementos con base: {c['despues_de_esos_elementos']}. Las 160 que cambian, por motivo: {c['por_motivo']}. "
      "Las 177 marcadas quedan como límite declarado de la v7 (base no resuelta), y las 76 sin base, sin marca. Entre las 11 "
      "resueltas está `ext::13.4.6` → `ext::4.4`, que no es de las 7 correctas que nombra la v7: sin leer.", ""]
Path(sys.argv[2]).write_text("\n".join(L) + "\n", encoding="utf-8")
print(len(L))
