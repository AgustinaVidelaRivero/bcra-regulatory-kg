"""B6.1, tanda 1, T4, primer tramo, punto 9: arma el FRENO T4 (primer tramo) desde los archivos del repo y del trabajo, por script: toda
cifra del texto sale de un JSON o de una tabla generada; el texto fijo no lleva cifras propias. Solo lee; escribe <salida.md> (fuera del
repo). Uso: python3 -I -B freno_t4t1_armar.py <repo> <paso0.md> <seccion_foto.md> <grep.json> <justificaciones_completadas.json> <salida.md>
"""
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
R, P0, FOTO, GREP, COMPL, OUT = (Path(x) for x in sys.argv[1:7])
T4 = R / "data/experiment/tanda1/t4"
L = lambda p: json.loads(Path(p).read_text(encoding="utf-8"))  # noqa: E731
mil = lambda n: f"{n:,}".replace(",", ".")  # noqa: E731
pob = L(T4 / "muestras/poblaciones_t4_tramo1.json")
sor = L(T4 / "muestras/sorteos_t4_tramo1.json")
mat = L(T4 / "muestras/material/material_t4_tramo1.json")
vis = L(R / "data/experiment/tanda1/t3/muestras/unidades_a_la_vista_T4.json")
la = L(T4 / "lectura_asistida/lectura_asistida_t4_tramo1.json")
t3pob = L(R / "data/experiment/tanda1/t3/muestras/poblaciones_t4.json")
grep = L(GREP)
compl = L(COMPL)
tablas = (T4 / "tablas_t4_tramo1.md").read_text(encoding="utf-8")
partes = {int(m.group(1)): m.group(0) for m in re.finditer(r"#### Tabla (\d+)\..*?(?=\n#### Tabla |\Z)", tablas, re.S)}
assert sorted(partes) == [1, 2, 3, 4, 5, 6]
prueba = (T4 / "lectura_asistida/consolas/prueba_convertidor_t4t1.txt").read_text(encoding="utf-8")
frenos = prueba.count("PROBLEMA(S)") + prueba.count("FRENO:")
oks = prueba.count("\nOK: ")
m12, m1, m3 = (pob["muestras"][k] for k in ("observacion:12", "vigilancia:1", "vigilancia:3"))
a41 = pob["observacion_12_A41_tal_cual_informacion"]
o10 = pob["controles"]["observacion_12_igual_a_la_extraccion_de_la_10"]
rest = pob["composicion_informacion"]["restadas_por_la_decision_1_2_sobre_A41"]
v2 = t3pob["muestras"]["vigilancia:2"]
tv = vis["todas_las_muestras"]
P = {m: x["propuestas"] for m, x in la["muestras"].items()}
nd1 = P["vigilancia_1"].get("no decidible", 0)
dud = [(m, e) for m in ("cola", "aceptadas_items", "aceptadas_no_items") for e in la["muestras"][m]["detalle"] if e["propuesta"] == "dudosa"]
otro_punto = [f"`{e['id']}`" for m, e in dud if "no está en el texto de la unidad" in e["justificacion"] or "no están en el texto de la unidad" in e["justificacion"]]
rem_obs = [f"`{e['id']}`" for m in la["muestras"] for e in la["muestras"][m]["detalle"] if "remite_a" in (e.get("observaciones") or "")]
nd12 = [f"`{e['id'] if isinstance(e['id'], str) else ' | '.join(e['id'])}`" for e in la["muestras"]["observacion_12"]["detalle"] if e["propuesta"] == "no decidible"]
vac_mmsef = sum(1 for e in la["muestras"]["vigilancia_2"]["detalle"] if e["propuesta"] == "vaciamiento" and str(e["id"]).startswith("ri_mmsef::"))
tipos3 = {json.dumps(f["id"]): {n["type"] for n in f["material"]["nodos"]} for f in
          (json.loads(x) for x in (T4 / "muestras/material/vigilancia_3/fichas_vigilancia_3.jsonl").read_text(encoding="utf-8").splitlines() if x.strip())}
par = sum(1 for e in la["muestras"]["vigilancia_3"]["detalle"] if e["propuesta"] == "distintos" and tipos3[json.dumps(e["id"])] == {"Obligacion", "Operacion"})
n_mue = {x["n"] for x in sor["muestras"].values()}
assert len(n_mue) == 1
assert all(x["informacion_aristas_con_su_unidad_fuera_de_la_lista"] == 0 for x in vis["muestras"].values())
v_t3 = L(T4 / "muestras/unidades_a_la_vista_T4_regla_de_T3.json")["muestras"]
igual_t7 = all(vis["muestras"][m]["informacion_con_la_regla_de_T3"] == v_t3[m]["unidades_a_la_vista"] for m in v_t3 if m != "observacion:12")
assert igual_t7
fmt = lambda d: ", ".join(f"{k} {v}" for k, v in d.items())  # noqa: E731

w = [f"# FRENO T4 — tanda 1 de B6.1, primer tramo: los sorteos de (1) y (3), la (12) rehecha, el material, lo que queda a la vista y la "
     f"lectura asistida (USD 0, sin API, sin commit)", "",
     "Rigen el pre-registro firmado (`docs/preregistro_tanda1.md`, firma en `95b18217`, con su nota del 17/10/2026 en `ca5b39fd`), el «seguí» de",
     "T4 y lo que decidió la autora el 18/10/2026 sobre el FRENO T3 (va a la §29 del registro de decisiones). HEAD `764768a4`.", "",
     "**Resultado:**",
     f"- **Las poblaciones y los sorteos** (secciones 3 y 4): (1), {mil(m1['N'])} nodos Condicion; (3), {mil(m3['N'])} grupos; la (12), "
     f"{mil(m12['N'])} aristas con el universo de la decisión 1.2 (A4.1 tal cual daba {mil(a41['N'])}). Tres muestras de {n_mue.pop()}, en dos "
     "corridas iguales.",
     f"- **El material** (sección 5): {mat['control']['fichas']} fichas, con el control en {mat['control']['claves_vedadas']} claves vedadas.",
     f"- **Lo que queda a la vista** (sección 6), con la regla de la decisión 1.1: {mil(tv['unidades_a_la_vista'])} unidades en las ocho "
     f"muestras que se leen ({fmt(tv['por_version'])}). Con la regla de T3 serían {mil(tv['informacion_con_la_regla_de_T3'])}.",
     f"- **La lectura asistida** (sección 7) de las {len(la['muestras'])} muestras, con una propuesta y una justificación que cita el texto por elemento. Doy "
     "solo cuántas propuestas hay de cada respuesta (tabla 5). Sin tasas, sin atención y sin ampliación: son del segundo tramo.",
     f"- **Las planillas de la autora** (sección 8): {len(la['muestras'])}, con el `LEEME` y el convertidor, probado sobre una copia. El sello "
     "es de la autora.",
     "- Toda cifra sale por script de sus archivos. Las tablas que copio de una salida van tal cual; mis aclaraciones van fuera de las tablas.",
     "- Nada commiteado y ningún mensaje de commit preparado: los commits son de la autora y quedan PENDIENTES.", ""]
w += [P0.read_text(encoding="utf-8").strip(), ""]
w += ["## 2. Lo decidido el 18/10/2026 y cómo lo apliqué", "",
      "1. **La lista de exclusión de U-MED-VERIF, con los nodos compartidos** (punto 1.1). `unidades_a_la_vista_t4t1.py` suma la unidad de "
      "cada ficha de unidad (versión final) o de cola (versión primera), y las unidades de procedencia de todo otro nodo que muestra una "
      "ficha. No suma un TextoOrdenado ni un Sujeto con más de una unidad de procedencia. Un Sujeto con una sola unidad suma.",
      "   - Los nodos que muestra una ficha: en una de unidad, los suyos y los dos extremos de cada arista; en una de arista, sus dos nodos; "
      "en una de (1), el nodo y el otro nodo de cada arista; en una de (3), los nodos del grupo.",
      "   - Las aristas que muestran las fichas de (1) y de la (12) tienen su unidad de procedencia en la lista en todas las muestras (tabla 4, "
      "información): ninguna arista queda a la vista sin su unidad.",
      f"2. **El universo de la observación (12)** (punto 1.2). `poblaciones_t4t1.py` resta de todas las aristas del grafo evaluado las "
      f"`referencia`, las de `rol_fuente = esqueleto`, las `establecida_en` con `rol_fuente = derivada_de_procedencia` y las `remite_a`. "
      f"Da {mil(m12['N'])}, igual a las aristas de extracción de la (10) del grafo evaluado ({mil(o10['obs10_extraccion'])}, "
      f"`t3/conteos_sin_leer/contado_sin_leer_t3f.json`): {o10['igual']}. Las `establecida_en` sin `rol_fuente` quedan. La muestra de T3, "
      "con A4.1 tal cual, queda en `t3/muestras/` sin cambios y no se lee.",
      f"3. **La vigilancia (2)** (punto 1.3). Su población es la de T3, la extracción final ({mil(v2['N'])} aceptadas sin relaciones), y su "
      "muestra es la de T3. La del primer intento no se sortea ni se reporta: `no_abrir_t4t1.py` escribe su cuenta por TO solo en "
      "`t4/NO_ABRIR_conteos_t4.json`, sin imprimir ninguna cifra, y de él doy solo el sha256 (tabla 6).",
      "4. **Las definiciones de (1) y (3)** (punto 1.4): las del FRENO T3, sección 6, con los dos agregados. En (1), `no decidible` queda "
      f"fuera de la tasa y se declara con su cuenta (hoy, {nd1} propuesta de 30). En (3), el grupo por tramo igual no ve duplicaciones con "
      "tramos distintos. Lo declaro en la sección 9.", ""]
w += ["## 3. Las poblaciones (punto 3)", "", "Script: `poblaciones_t4t1.py`, sobre una copia del repo. La tabla, tal cual:", "", partes[1].strip(), "",
      "- La celda de un nodo es la de su unidad de procedencia primaria; la de un grupo de (3), la de su nodo de id menor; la de una arista, la "
      "de su nodo de origen (§5.4 bis, punto 2, v8c).",
      "- El id de un grupo de (3) son sus ids de nodo ordenados y unidos con «|»; el de una arista, la tripla (source, relation, target).", ""]
w += ["## 4. Los sorteos", "", "Script: `sorteos_t4t1.py`, con `celdas_t4_t3f.asignar` de T3 sin cambios. Cada cadena se controla contra las "
      "del texto firmado (`95b18217:1019-1062`). La tabla, tal cual:", "", partes[2].strip(), "",
      "- Las cadenas: `tanda1:vigilancia:1:<celda>:<base>`, `tanda1:vigilancia:3:<celda>:<base>` y `tanda1:observacion:12:<celda>:<base>`. "
      "Las cadenas de la ampliación no se usan. Las otras cinco muestras no se tocaron.", ""]
w += ["## 5. El material", "", "Script: `material_t4t1.py`, sobre la copia, con la E0 con las partes rearmada en la copia "
      "(`reext_t0/t3/e0_con_partes.py`). La tabla, tal cual:", "", partes[3].strip(), "",
      "- **(1):** el nodo Condicion con sus propiedades y su procedencia, el texto de su unidad y sus aristas, con la relación y el id, el "
      "tipo y el label del otro nodo.",
      "- **(3):** los nodos del grupo con sus propiedades y su procedencia, y el texto de su unidad.",
      "- **La (12):** como en T3, la arista, sus dos nodos y el texto de su unidad de procedencia.",
      "- El texto de cada unidad es el que vio E3 (`comun_e3.fuente_integro`). Sin el estado de E3 ni sus marcas. La hora del material es "
      "posterior a la de los sorteos.",
      "- No armé planillas en el material: las que valen son las de `lectura_autora/` (sección 8). Las planillas en blanco del material de "
      "T3 (`t3/muestras/material/*/planilla_*.csv`) quedan como están y no se usan.", ""]
w += ["## 6. Lo que queda a la vista (punto 5)", "",
      "Script: `unidades_a_la_vista_t4t1.py`. Reescribí `t3/muestras/unidades_a_la_vista_T4.json`, el único archivo de `t3/` que cambia. "
      "Antes copié la versión de T3, tomada del T3a (`git show eb0711a1`), a `t4/muestras/unidades_a_la_vista_T4_regla_de_T3.json`. "
      "Por muestra, el archivo da el `chunk_id` de cada unidad, la versión que muestra y por qué suma: la ficha o el tipo del nodo. "
      "La tabla, tal cual:", "", partes[4].strip(), "",
      f"- Las muestras de T3, con la regla de T3, dan las mismas cifras que su versión del T3a (tabla T7 del FRENO T3): {igual_t7}. El cálculo "
      "de información reproduce el de entonces.",
      "- No calculé si quedan 30 en la población de U-MED-VERIF: lo controla la mesa.", ""]
w += ["## 7. La lectura asistida (punto 6)", "",
      f"La leí yo: {la['lectura']['modelo']} (`{la['lectura']['id']}`), sobre las fichas del material, sin API. Las propuestas de "
      "entrada están en `t4/lectura_asistida/propuestas/`; `planillas_t4t1.py` las controla contra el material (los mismos ids, en el mismo "
      "orden, una respuesta válida y una cita del texto por elemento) y arma el JSON y las planillas. La tabla, tal cual:", "", partes[5].strip(), "",
      "**Los criterios que apliqué** (`criterios_de_la_propuesta` del JSON):",
      "- **Cola y aceptadas:** un tipo cercano con la descripción fiel es lectura laxa, sin error, como en la lectura de las aceptadas de la "
      "tanda 0. Es error una facultad o un fin leído como deber, un supuesto o una regla invertidos, un sujeto que no es el del texto, una "
      "relación que el texto no sostiene o un contenido que no está. Es dudosa si el contenido viene de otro punto del documento y no está en "
      "el texto de la unidad, o si el texto admite las dos lecturas. Los tipos documentales y las `remite_a` no entran en el veredicto.",
      "- **(2):** vaciamiento si el ítem fija un dato, una medida, un concepto o un sujeto del régimen, o el texto fija una regla o una tabla "
      "del modelo de información, y la unidad no tiene relaciones. No lo es si el texto propio solo abre una lista, es un título o es un "
      "formulario.",
      "- **(1):** sí, solo si el texto formula el deber y la Condicion lo lleva; el «debe» que pone la descripción del extractor no cuenta.",
      "- **(3):** duplicación si el mismo contenido normativo está en dos nodos del grupo. Son distintos si cada nodo dice algo que el otro "
      "no, incluido el par deber y acto regulado (`Obligacion —regula→ Operacion`, `e1_extractor/prompt_e1.py:67` y `:184-189`), cuando la "
      "descripción del acto no repite el deber.",
      "- **La (12):** una `establecida_en` es correcta si el nodo de origen está en el texto de su unidad y es de ese TO; en las demás, decide "
      "la relación contra el texto.",
      "- Las omisiones y las observaciones van aparte, en `t4/lectura_asistida/omisiones_y_observaciones_t4_tramo1.md`.", ""]
w += ["## 8. Las planillas, el LEEME y el convertidor (punto 7)", "", partes[6].strip(), "",
      "- **Las planillas** (`t4/lectura_autora/<muestra>.csv`): UTF-8, «;» y «\\n», con `id`, `celda`, `ficha` (la ruta del `.md` y, tras «#», el "
      "número de la ficha), `propuesta`, `justificacion`, y `veredicto_autora` y `nota_autora` vacías.",
      "- **El `LEEME_lectura_T4.md`:** el orden de lectura (cola, aceptadas ítems, aceptadas no ítems, (2), (7), (1), (3) y la (12)), las "
      "respuestas válidas de cada muestra, que el veredicto puede repetir la propuesta o cambiarla con la razón en la nota, que la (12) que "
      "vale es la de `t4/` y nunca la de `t3/`, cómo se convierte y cómo se sella.",
      "- **El convertidor** (`convertir_lectura_T4.py`, generado por `planillas_t4t1.py` desde `convertir_lectura_T4_plantilla.py` con el sha256 "
      "de cada planilla adentro): toma `id`, `celda`, `ficha`, `propuesta` y `justificacion` de la planilla y de la exportación solo las dos "
      "columnas de la autora. Controla los códigos, que los ids y su orden sean los de la muestra y que un cambio de la propuesta traiga su "
      "razón; frena si algo no cierra, no cambia ninguna marca y no pisa una marcada.",
      f"- **La prueba**, sobre una copia de `lectura_autora/` con exportaciones simuladas (`lectura_asistida/consolas/prueba_convertidor_t4t1.txt`): "
      f"{oks} conversiones pasan (separadores «,», «;» y tabulador, con y sin BOM, una con un cambio con su nota) y {frenos} frenan como "
      "deben (un cambio sin razón, un código mal escrito, dos filas reordenadas y una marcada que ya existe).",
      "- **El sello lo hace la autora:** el sha256 y la hora de cada marcada, en `t4/lectura_autora/sello_lectura_T4.txt` (el `LEEME` trae "
      "el comando). Queda PENDIENTE.", ""]
w += ["## 9. Lo declarado por los puntos 1.2 a 1.4", "",
      f"1. **La (12) se rehízo con el universo de la decisión 1.2** ({mil(m12['N'])} aristas); la muestra de T3, con A4.1 tal cual "
      f"({mil(a41['N'])}), queda en `t3/muestras/observacion_12.json` sin cambios y no se lee. Lo que la decisión resta de A4.1: "
      + "; ".join(f"{k}, {mil(v)}" for k, v in rest.items()) + ".",
      f"2. **La vigilancia (2)** se lee sobre la población de la extracción final ({mil(v2['N'])} unidades). La del primer intento no se sortea "
      "ni se reporta: su cuenta por TO está solo en `t4/NO_ABRIR_conteos_t4.json`.",
      f"3. **En la vigilancia (1), `no decidible` queda fuera de la tasa** y se declara con su cuenta: hoy {nd1} propuesta; la cuenta que vale "
      "es la de la lectura de la autora.",
      "4. **En la vigilancia (3), el grupo por tramo igual no ve duplicaciones con tramos distintos.** Una duplicación entre nodos cuyos tramos "
      "difieren no entra en la población.", ""]
w += ["## 10. Para la autora y la mesa", "",
      f"1. **Dudosas por contenido de otro punto:** {', '.join(otro_punto)}. Sus nodos traen texto que no está en el texto de la unidad que vio "
      "E3: en ri_mmsef, «Se informará el cumplimiento…» y los parámetros «Si / No / Eximida / No Aplicable». Que E1 lo haya visto en su "
      "mensaje: NO VERIFICADO. Si se confirma, es un rasgo del contexto de E1 frente al de E3, no un error de una unidad.",
      f"2. **Una observación de `remite_a`** ({', '.join(rem_obs)}): las aristas hacia `ceninf::2.1` se apoyan en la cita «punto 2.1 del "
      "apartado A del T.O.», que es de otro texto ordenado. Va como observación porque las `remite_a` se cuentan aparte.",
      f"3. **En la (3), {par} de los grupos son el par deber y acto regulado** (`Obligacion —regula→ Operacion`) con la descripción del acto "
      "sin el deber: los propuse distintos, por el diseño del esquema. Si la autora lee ese par como duplicación, la cifra cambia mucho.",
      f"4. **La (12) tiene un no decidible por un texto incompleto** ({', '.join(nd12)}): la oración «Para que las autoridades de la entidad "
      "tomen conocimiento…» termina en la lista, sin el verbo principal.",
      f"5. **En la (2), {vac_mmsef} de los vaciamientos son ítems de ri_mmsef**, datos o medidas del régimen informativo sin relaciones.",
      "6. **Lo que queda a la vista** (sección 6): la mesa controla si quedan 30 en la población de U-MED-VERIF, sin abrir nada.", ""]
foto = FOTO.read_text(encoding="utf-8").strip()
assert foto.startswith("## La foto del repo")
w += ["## 11. " + foto[3:], ""]
pos = grep["control_positivo_lineas"]
propios = grep["propios_con_patron"]
w += [f"- **El grep de convenciones** (`grep_convenciones_t4t1.py` y su salida, en el paquete) busca las palabras del `user.name` de git y "
      f"las de origen conversacional (Slack, mail, correo, «como dijo», «pedido por», …) en los {grep['archivos']} archivos nuevos o cambiados "
      f"de la foto, sin el `NO_ABRIR_`. El control positivo da la línea {', '.join(map(str, pos))}. Con el patrón, en los archivos que redacté: "
      + ("ninguno" if not propios else "; ".join(f"`{Path(k).name}`, {len(v)} línea(s)" for k, v in propios.items())
         + ": son las líneas de este script que describen el patrón del grep")
      + f". Las palabras del nombre, en ningún archivo: {not grep['nombre_sin_rutas']}. En las salidas de los generadores, las coincidencias "
      f"son texto de la norma (como «correo electrónico» en ids de nodo): "
      + (", ".join(f"`{Path(k).name}`" for k in grep["con_patron_sin_rutas"] if k not in propios) or "ninguna")
      + f". Rutas con la carpeta personal o el scratchpad: {len(grep['con_rutas_absolutas'])} archivo(s)"
      + (f" ({', '.join('`' + Path(x).name + '`' for x in grep['con_rutas_absolutas'])}: son los controles que buscan esas cadenas)"
         if grep["con_rutas_absolutas"] else "") + ". El grep del FRENO va en el mensaje de cierre.",
      "- **Las copias** del repo son con el `rsync` de la cláusula, más la exclusión del volumen de Neo4j, y su control dio 0 "
      "(`rsync_copia_t4t1.log` en el paquete). Ningún `git clone`. No abrí ninguna carpeta vedada.", ""]
w += ["## 12. Errores propios, con su causa", "",
      "1. **Dos constantes de sha256 escritas de memoria.** En `poblaciones_t4t1.py` y `sorteos_t4t1.py` puse primero un sha256 inventado para "
      "`t3/muestras/poblaciones_t4.json` y un prefijo inventado para `celdas_t4_t3f.py`.",
      "   - La causa: escribí la constante antes de calcularla.",
      "   - Lo vi antes de correr: las reemplacé por el sha256 que da `shasum -a 256` sobre el archivo y sobre `git show HEAD:`, y los "
      "controles las comparan enteras.",
      f"2. **{len(compl['justificaciones'])} justificaciones sin cita** (`justificaciones_completadas_t4t1.json`, en el paquete). En las unidades sin contenido y "
      "en otras escribí la justificación sin citar el texto.",
      "   - La causa: di por obvia la cita cuando la unidad no tiene nodos.",
      "   - El control de `planillas_t4t1.py` frenó antes de escribir nada, y las completé con la cita del texto.",
      "3. **La primera prueba del convertidor no probó nada.** El bucle de zsh pasó la muestra y la exportación como un solo argumento, y "
      "todas las corridas dieron el error de uso.",
      "   - La causa: zsh no parte las variables en palabras.",
      "   - La repetí con los dos argumentos separados; la consola que va al repo es la de esa segunda corrida.", "",
      "FRENO T4, primer tramo. Espero la revisión de la mesa y la lectura de la autora."]
texto = "\n".join(w) + "\n"
OUT.write_text(texto, encoding="utf-8")
print(texto)
