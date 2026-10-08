"""U-E3-LISTAS, O5: aplica a UNA COPIA (nunca el repo) los casos resueltos al final de la NOTA del ítem.
  - prompt_e3.py: la constante NOTA_E3_ITEM_CASOS (el texto del archivo que se pasa, byte a byte), antes de la llamada
    final al candado del mensaje (para no mover las líneas que citan otros documentos), y nota_item_lista la agrega al
    armar la NOTA (misma línea, sin correr ninguna otra).
  - selftest_e3.py: el check M que perturba las NOTAS suma la constante nueva.
Los valores del candado no se tocan aquí (los recomputa ue3_o5_candado.py). Uso: python ue3_o5_parche_e3.py <copia> <texto.txt>"""
import sys
from pathlib import Path
C, TXT = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
E3 = C / "data/experiment/reextraccion_v2/e3_verificador"
texto = TXT.read_text(encoding="utf-8")
assert '"' not in texto and "\\" not in texto and "{" not in texto


def literal(t: str, ancho: int = 112) -> list[str]:
    filas = []
    parrafos = t.split("\n")
    for k, parrafo in enumerate(parrafos):
        resto, fin = parrafo, "\\n" if k < len(parrafos) - 1 else ""
        partes = []
        while len(resto) > ancho:
            corte = resto.rfind(" ", 0, ancho) + 1
            partes.append(resto[:corte]); resto = resto[corte:]
        partes.append(resto)
        partes[-1] += fin
        filas += partes
    return filas


filas = literal(texto)
bloque = ("# U-E3-LISTAS, O5 (nota al pie del 07/10/2026, noche): casos resueltos al final de la NOTA del ítem, uno de cada\n"
          "# lado de la frontera entre el bloque que abre la lista (otra unidad) y el texto propio del ítem, para las omisiones\n"
          "# declaradas [meta_normativo]. Cada cláusula con su regla de E1 r2b en la tabla del FRENO O5 (prefijo :3, :324, :387\n"
          "# y :390); los ejemplos son de ext::10.11.5 y cla::6.5.5.8, fuera de las 20 unidades de O3. Va aquí, antes de correr\n"
          "# el candado del mensaje, para no mover las líneas que citan otros documentos; nota_item_lista la agrega a la NOTA.\n"
          "NOTA_E3_ITEM_CASOS = (\n" + "\n".join(f'    "{f}"' for f in filas) + ")\n\n\n")
ns = {}
exec("NOTA_E3_ITEM_CASOS = (\n" + "\n".join(f'    "{f}"' for f in filas) + ")", ns)
assert ns["NOTA_E3_ITEM_CASOS"] == texto
p = E3 / "prompt_e3.py"; src = p.read_text(encoding="utf-8")
viejo_ret = ('                                     unidad_del_bloque=NOTA_E3_ITEM_UNIDAD[clave])\n')
nuevo_ret = ('                                     unidad_del_bloque=NOTA_E3_ITEM_UNIDAD[clave]) + "\\n" + NOTA_E3_ITEM_CASOS\n')
assert src.count(viejo_ret) == 1 and src.endswith("\n\n\n_candado_mensaje_e3()\n")
src = src.replace(viejo_ret, nuevo_ret)
src = src[: -len("_candado_mensaje_e3()\n")] + bloque + "_candado_mensaje_e3()\n"
assert max(len(l) for l in bloque.splitlines()) <= 120 and len(nuevo_ret.rstrip("\n")) <= 120
p.write_text(src, encoding="utf-8")
q = E3 / "selftest_e3.py"; st = q.read_text(encoding="utf-8")
a = '    for nombre in ("NOTA_E3_OMISIONES", "NOTA_E3_ENCABEZADO_LISTA", "NOTA_E3_ITEM_LISTA"):\n'
b = '    for nombre in ("NOTA_E3_OMISIONES", "NOTA_E3_ENCABEZADO_LISTA", "NOTA_E3_ITEM_LISTA", "NOTA_E3_ITEM_CASOS"):\n'
a2 = '    check("M: un espacio más en cualquiera de las tres NOTAS (la del ítem, U-E3-LISTAS) hace frenar el candado; "\n'
b2 = '    check("M: un espacio más en cualquiera de las NOTAS (la del ítem y sus casos resueltos, U-E3-LISTAS) hace frenar "\n'
a3 = '          "restaurado, pasa",\n'
b3 = '          "el candado; restaurado, pasa",\n'
for x, y in ((a, b), (a2, b2)):
    assert st.count(x) == 1, x
    st = st.replace(x, y)
i = st.index(b2) + len(b2)
assert st[i:i + len(a3)] == a3
st = st[:i] + b3 + st[i + len(a3):]
q.write_text(st, encoding="utf-8")
print("parche aplicado en", C.name, "| filas del literal:", len(filas), "| líneas agregadas a prompt_e3:", bloque.count("\n"))
