"""U-OMISIONES-COD, O2 — escribe `limites_O2.md` desde las salidas de O2 (solo las lee):
  salidas/limites_O2.json            `o1/scripts/limites_O1.py` corrido sobre el grafo de diez de O2 (igual al de O1, campo
                                     por campo);
  salidas/limites_C_O2_diez.json     `limites_C_O2.py`, el grupo C elemento por elemento;
  salidas/h_i_sellado_head_O2.json   `medir_h_i.py`, el ítem (i).
Uso: python3 -I limites_md_O2.py <dir salidas> <out.md>"""
import json
import sys
from pathlib import Path

s = Path(sys.argv[1])
d = json.loads((s / "limites_O2.json").read_text(encoding="utf-8"))
c = json.loads((s / "limites_C_O2_diez.json").read_text(encoding="utf-8"))
hi = json.loads((s / "h_i_sellado_head_O2.json").read_text(encoding="utf-8"))
# mecanismo de los 6 de L: la lectura de la nota del 10/10/2026 al pie de la v7 (decisión 4), por unidad
L_NOTA = {"ext::3.5.3::intro": "E0 corta el texto en «…a los 3»",
          "ext::7.8.5.2": "«promedia» donde el texto dice «promedio»",
          "pro::2.3.5.1": "E1 une el «dentro de:» del encabezado con el segundo guion",
          "cap::3.2.4": "la fórmula intercala «fondo» y el literal pierde el «%»",
          "ext::4.2::cierre": "«podrá» donde el texto dice «podrán»",
          "cap::5.3.2.1": "E1 omite palabras"}
L = ["# U-OMISIONES-COD, O2 — límites y residuos, caso por caso", "",
     "Generado por `scripts/limites_md_O2.py` desde `salidas/`. Páginas: las de la unidad en la E0 r2b. Todo sale del grafo de "
     "diez de O2 (`710664e9`) salvo donde se dice. «sin leer»: no leí el caso. Ninguno sale de los grupos de la v7: los que "
     "quedan fuera de lo que corrige esta unidad van, como límite medido, al grupo 2.", ""]
L += ["## Grupo L: elementos que conservan la cuantía (6)", "",
      "Decidido en la nota del 10/10/2026 al pie de la v7 (decisión 4): se conserva la cuantía y quedan como límite. El "
      "mecanismo es la lectura de esa nota.", "",
      "| unidad | páginas | cuantía | tramo de E1 | mecanismo |", "|---|---|---|---|---|"]
L += [f"| `{x['unidad']}` | {x['paginas']} | «{x['cuantia']}» | «{x['tramo_e1']}» | {L_NOTA.get(x['unidad'], x['mecanismo'])} |"
      for x in d["L_conservan_la_cuantia"]]
f = d["f_conjunto_de_51"]
L += ["", f"## Grupo B, f: menciones que verifican sin el artículo inicial y siguen sin verificar ({len(f['quedan'])} de {f['n']})", "",
      f"El conjunto de R2-1, reconstruido, da {f['n']} relaciones; pasan {f['pasan']} (257 → 210 menciones sin verificar en "
      "`resolucion_sujetos.jsonl`). La expansión de contracciones solo alcanza al artículo «el» («del», «al»). «las entidades» "
      "es la expresión colectiva de R3.", "", "| unidad | páginas | relación | mención | mecanismo |", "|---|---|---|---|---|"]


def mec(m):
    return ("artículo «la»/«las»/«los»: sin contracción que expandir" if m.split()[0].lower() in ("la", "las", "los")
            else "sin leer")


L += [f"| `{x['unidad']}` | {x['paginas']} | {x['indice_relacion']} | «{x['mencion']}» | {mec(x['mencion'])} |" for x in f["quedan"]]
L += ["", f"## Grupo A, a: omisiones con el tramo en el orden de lectura, sin la marca ({len(d['a_orden_de_lectura_sin_marca'])})", "",
      "| unidad | páginas | categoría | tramo | mecanismo |", "|---|---|---|---|---|"]
L += [f"| `{x['unidad']}` | {x['paginas']} | {x['categoria']} | «{x['tramo']}» | {x['mecanismo']} |" for x in d["a_orden_de_lectura_sin_marca"]]
L += ["", f"## Grupo A, d: entidades de T4 con un supuesto dentro que la marca no detecta ({len(d['d_positivas_T4_no_detectadas'])})", "",
      "| unidad | entidad | páginas | supuestos de T4 | mecanismo |", "|---|---|---|---|---|"]
L += [f"| `{x['unidad']}` | {x['entidad']} | {x['paginas']} | {'; '.join(x['supuestos_de_T4'])} | {x['mecanismo']} |"
      for x in d["d_positivas_T4_no_detectadas"]]
L += ["", "## Grupo A, e: la pieza aparte", "",
      "No está aplicada (`pieza_e/`). Entra solo si la lectura a ciegas de sus 16 detecciones fuera de las 64 unidades de T4 "
      "llega al piso: límite inferior de Wilson al 95 % de 0,75 o más sobre las decididas, con las dudosas excluidas (al menos "
      "12 decididas, todas correctas). Si no llega, (e) queda como límite declarado. Mientras tanto, en el conjunto de diseño "
      "de T4:", "",
      "| caso T4 | unidad | páginas | clase de T4 | razón de T4 | mecanismo |", "|---|---|---|---|---|---|"]
L += [f"| {x['caso_T4']} | `{x['unidad']}` | {x['paginas']} | copia real | {x['razon_T4']} | {x['mecanismo']} |"
      for x in d["e_copias_reales_de_T4_no_detectadas"]]
L += [f"| {x['caso_T4']} | `{x['unidad']}` | — | {x['clase_T4']} | {x['razon_T4']} | sin leer |" for x in d["e_falsos_positivos_de_T4"]]
L += ["", f"## Grupo H: Comunicacion con `tipo_no_derivable` ({len(d['H_tipo_no_derivable'])} en diez)", "",
      "Quedan como error de extracción declarado (v7). El código y la etiqueta no nombran una Comunicación ni una norma externa "
      "(una remisión a un punto o una sección, o el nombre de un TO u otro documento). En el sin cola de diez son 25 (todas "
      "menos `Comunicacion_grandes_exposiciones_al_riesgo_de_credito`); en desarrollo, con y sin cola, 18, todas de esta lista.",
      "", "| nodo | código | unidades |", "|---|---|---|"]
L += [f"| `{x['nodo']}` | «{x['codigo']}» | {', '.join(x['unidades'])} |" for x in d["H_tipo_no_derivable"]]
e = c["por_estado_o2"]
L += ["", f"## Grupo C: los {c['elementos_con_base_en_head']} elementos con base ({e['resuelta']} resueltas, {e['marcada']} marcadas y "
      f"{e['sin_base']} sin base)", "",
      f"Por estado y origen: {c['por_estado_o2_y_origen']}. Las marcadas quedan como límite declarado de la v7 (base no "
      "resuelta); las sin base son los límites relativos del validador cuya «base» no es una base (g1), sin marca.", "",
      "### Las resueltas", "", "| unidad | origen | destino | vía | lectura |", "|---|---|---|---|---|"]
LECT = {"ext::13.4.6": "leído en O2: la base es «total pendiente por sus deudas elegibles para los puntos 4.4. y 4.5.» "
                       "(p. 172). Resuelve al primero de los dos puntos y la base es un monto, no la unidad citada: correcta "
                       "solo en parte. Ya estaba así en `a9631a64`; queda como límite medido, para el grupo 2",
        "ext::3.14.4": "nueva (g), caso positivo de la v7", "ext::14.2.3": "nueva (g), caso positivo de la v7",
        "ext::3.18.2.4": "nueva (g), caso positivo de la v7"}
for x in c["resueltas"]:
    L.append(f"| `{x['unidad']}` | {x['origen']} | `{x['destino_o2']}` | {x['via_o2']} | "
             f"{LECT.get(x['unidad'], 'una de las 7 correctas de la v7')} |")
for est, tit in (("marcadas", "Las marcadas"), ("sin_base", "Las sin base (g1)")):
    L += ["", f"### {tit} ({len(c[est])})", "", "| unidad | origen | base en HEAD | cuantía |", "|---|---|---|---|"]
    L += [f"| `{x['unidad']}` | {x['origen']} | «{(x['base_head'] or '').replace('|', '/')}» | {x['cuantia_o2']} |" for x in c[est]]
nav = hi["o2_diez"]["i_navegacion"]
L += ["", "## Ítem (i): los nodos que pasan la ventana del agente (insumo de U-NAV-DISENO)", "",
      "La ventana real: `ver_vecinos(limite=40)` corta 40 por dirección (`evaluacion/harness.py:230-235`). Con el código nuevo, "
      f"{nav['ventana_del_agente_con_remite_a']['n']} nodos con `remite_a` y {nav['ventana_del_agente_sin_remite_a']['n']} sin "
      "ella, los mismos nodos que en `a9631a64`. La definición de la v6 (más de 40 entre entrantes y salientes) queda como "
      f"referencia: {nav['grado_total_solo_remite_a']['n']} y {nav['grado_total_sin_remite_a']['n']} (43 y 22 en `a9631a64`).", ""]
for k, tit in (("ventana_del_agente_con_remite_a", "Con `remite_a`"), ("ventana_del_agente_sin_remite_a", "Sin `remite_a`")):
    L += [f"### {tit} ({nav[k]['n']})", "", "| nodo | tipo | salientes | entrantes | salientes `remite_a` | entrantes `remite_a` |",
          "|---|---|---|---|---|---|"]
    L += [f"| `{x['id']}` | {x['type']} | {x['salientes']} | {x['entrantes']} | {x['salientes_remite_a']} | {x['entrantes_remite_a']} |"
          for x in nav[k]["lista"]]
    L.append("")
Path(sys.argv[2]).write_text("\n".join(L).rstrip("\n") + "\n", encoding="utf-8")
print(len(L))
