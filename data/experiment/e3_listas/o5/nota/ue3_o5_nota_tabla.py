"""U-E3-LISTAS, O5: la tabla cláusula → regla de los casos resueltos de la NOTA del ítem, como la de O2. Cada cláusula es
un tramo del texto propuesto (se comprueba que está en él) y cada apoyo es un fragmento verbatim del prefijo de E1 r2b
armado (PREFIJO_SISTEMA_R2B, con su línea) o de una NOTA de E3 del código de la copia (se comprueba). Sin API.
Uso: python ue3_o5_nota_tabla.py <copia_o5> <texto.txt> <salida.md> <salida.json>"""
import json, sys
from pathlib import Path
C, TXT, MD, JS = (Path(x).resolve() for x in sys.argv[1:5])
REX = C / "data/experiment/reextraccion_v2"
sys.path.insert(0, str(REX / "e3_verificador"))
import prompt_e3 as P  # noqa: E402
import prompt_r2b as R  # noqa: E402
assert Path(P.__file__).resolve().is_relative_to(C)
texto = TXT.read_text(encoding="utf-8")
assert P.NOTA_E3_ITEM_CASOS == texto
pref = R.PREFIJO_SISTEMA_R2B.split("\n")


def e1(regla, archivo, frag):
    linea = [i for i, l in enumerate(pref, 1) if frag in l]
    assert len(linea) == 1, (regla, frag, linea)
    return {"fuente": f"{regla} (`{archivo}`; prefijo :{linea[0]})", "fragmento": frag}


def e3(nombre, frag):
    v = getattr(P, nombre)
    v = " ".join(v.values()) if isinstance(v, dict) else v
    assert frag in v, (nombre, frag)
    return {"fuente": f"NOTA de E3 `{nombre}` (`prompt_e3.py`)", "fragmento": frag}


FILAS = [
    ("K1", "Casos resueltos de omisiones [meta_normativo] en un ítem", "todas", "encuadre",
     [e3("NOTA_E3_OMISIONES", "Un tramo declarado así no es un faltante: no lo reclames."),
      e1("R19, regla 9", "prompt_r2b_reemplazos.json:138", "registralo en `omisiones` con categoría `meta_normativo` y su tramo")]),
    ("K2", "(una omisión es del texto propio de la unidad; el contexto heredado se extrae en su unidad):", "todas", "frontera",
     [e1("R26, OMISIONES", "prompt_r2b_reemplazos.json:180", "el tramo del texto PROPIO de la unidad que no extrajiste, copiado tal cual (no del contexto heredado: ese tiene su propia unidad)"),
      e1("R26, OMISIONES", "prompt_r2b_reemplazos.json:180", "con un elemento por cada contenido del texto de la unidad que NO extrajiste"),
      e1("R28", "prompt_r2b_reemplazos.json:12", "cada bloque heredado tiene su propia unidad de extracción responsable")]),
    ("K3", "- el bloque que abre la lista dice «Se requerirá la conformidad previa del BCRA para … excepto cuando … la entidad verifique que:», el ítem lleva su supuesto como Condicion",
     "condiciones de una sola excepción (b2)", "ejemplo, lado «no es faltante» (ext::10.11.5, tanda 0 r2b)",
     [e1("P3C-b1", "prompt_r2b_parche_p3c.json:48", "LAS CONDICIONES DE UNA SOLA EXCEPCIÓN: el encabezado enuncia la norma y una única salvedad"),
      e3("NOTA_E3_ITEM_LISTA", "el ítem es una Condicion de esa excepción")]),
    ("K4", "y el extractor declaró [meta_normativo] texto de ese bloque, con la glosa de que se compone en los ítems:", "todas",
     "la forma observada (ext::10.11.5; la misma en ext::3.6.4.1 y ext::3.6.4.2, el residuo)", []),
    ("K5", "no es faltante, porque el tramo no es del texto propio del ítem;", "todas", "exime (lado «no es faltante»)",
     [e1("R26, OMISIONES", "prompt_r2b_reemplazos.json:180", "no del contexto heredado: ese tiene su propia unidad"),
      e1("R28", "prompt_r2b_reemplazos.json:12", "el contexto heredado orienta y ancla, pero NO se extrae de él"),
      e3("NOTA_E3_ITEM_UNIDAD", "Ese bloque tiene unidad propia: allí se extrae lo que el encabezado enuncia aparte de la lista"),
      e1("P3C-b2", "prompt_r2b_parche_p3c.json:55", "Si los ítems son las condiciones de una sola excepción, esta unidad extrae la norma y esa excepción")]),
    ("K6", "la declaración solo deja constancia de la composición, aunque el bloque enuncie la norma y su salvedad;", "todas",
     "exime (lado «no es faltante»)",
     [e3("NOTA_E3_ITEM_LISTA", "Lo que el ítem toma del encabezado no es contenido agregado."),
      e3("NOTA_E3_ITEM_LISTA", "Que esa norma falte aquí como entidad aparte, o que el ítem no tenga relación hacia ella, no es faltante."),
      e1("P3C-d2", "prompt_r2b_parche_p3c.json:90", "La norma del encabezado no se emite como una entidad aparte dentro del ítem, en ninguno de los casos")]),
    ("K7", "- el texto propio del ítem dice «Los deudores excluidos precedentemente deberán ser clasificados y sus deudas previsionadas conforme a las disposiciones de carácter general», el extractor lo declaró [meta_normativo] y ninguna entidad lo lleva:",
     "todas", "ejemplo, lado «sí es faltante» (cla::6.5.5.8, texto real; en la tanda 0 el deber también se extrajo, e12: el ejemplo enuncia el caso sin extraer)",
     [e1("R26, OMISIONES", "prompt_r2b_reemplazos.json:180", "No registres como omisión lo que sí extrajiste")]),
    ("K8", "es faltante, porque está en el texto del ítem y dice un deber.", "todas", "controla (lado «sí es faltante»)",
     [e1("P3C-a3, PRUEBA de la regla 9", "prompt_r2b_parche_p3c.json:21", "Si dice un deber, una prohibición, una facultad, una condición, una excepción"),
      e1("P3C-a3, PRUEBA de la regla 9", "prompt_r2b_parche_p3c.json:21", "NO es meta-normativo: extraelo con el tipo que le toca"),
      e3("NOTA_E3_OMISIONES", "Sí es un faltante si lo declarado no es lo que dice su categoría")]),
]
cubierto = ""
for k, cl, *_ in FILAS:
    assert cl in texto, (k, cl)
filas_md = ["| Cláusula | Texto de los casos resueltos | Tipos de lista | Papel | Apoyo (archivo:línea; línea del prefijo de E1 armado) |", "|---|---|---|---|---|"]
for k, cl, tipos, papel, apoyos in FILAS:
    ap = "; ".join(f"{a['fuente']}: «{a['fragmento']}»" for a in apoyos) or "— (descripción de la forma observada; sin regla)"
    filas_md.append(f"| {k} | {cl} | {tipos} | {papel} | {ap} |")
# reconstrucción: las cláusulas, en orden y unidas como en el texto, dan el texto entero
rec = texto
for _, cl, *_ in FILAS:
    rec = rec.replace(cl, "", 1)
resto = rec.replace(" ", "").replace("\n", "")
MD.write_text("\n".join(filas_md) + "\n\nResto del texto fuera de las cláusulas (solo espacios y saltos): "
              + ("ninguno" if not resto else repr(resto)) + "\n", encoding="utf-8")
JS.write_text(json.dumps([{"clausula": k, "texto": cl, "tipos": t, "papel": p, "apoyos": a} for k, cl, t, p, a in FILAS],
                         ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(len(FILAS), "cláusulas; resto fuera de las cláusulas:", repr(resto))
