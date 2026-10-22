"""B6.1, tanda final, T4, tercer tramo: arma el FRENO T4 (tercer tramo) desde los archivos del repo y del trabajo, por script: toda cifra
del texto sale de un JSON o de una tabla generada; las tablas van tal cual; el texto fijo no lleva cifras propias. Es
t4/scripts/freno_t4t2_armar_tf.py (segundo tramo) con las secciones del tercer tramo y los diffs enteros de los cinco scripts del tramo
contra los del segundo (difflib, sin contexto). Solo lee; escribe data/experiment/tanda_final/t4/FRENO_T4_tramo3.md (frena si ya existe).
Uso: python3 -I -B freno_t4t3_armar_tf.py <repo> <salida del paso 0> <foto_contra_commits.json> <seccion_foto.md> <grep.json>
       <foto_contra_despues.json>
"""
import csv
import difflib
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.dont_write_bytecode = True
R, P0, FCC, FOTO, GREP, FC = (Path(x) for x in sys.argv[1:7])
R = R.resolve()
TF = R / "data/experiment/tanda_final"
T4 = TF / "t4"
OUT = T4 / "FRENO_T4_tramo3.md"
if OUT.exists():
    raise SystemExit(f"FRENO: ya existe {OUT}")
L = lambda p: json.loads(Path(p).read_text(encoding="utf-8"))  # noqa: E731
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()  # noqa: E731
X = L(T4 / "tasas/tasas_t4_tramo3.json")
X2 = L(T4 / "tasas/tasas_t4_tramo2.json")
U = L(TF / "t3/muestras/umbrales_t4_tf.json")
VER = L(T4 / "tasas/verif_tasas_independiente_t4t3_tf.json")["_resumen"]
CTRL_AMP = L(T4 / "ampliacion/control_lectura_mesa/salida_control_lectura_T4_ampliacion.json")
grep, fc, fcc = L(GREP), L(FC), L(FCC)
tablas = (T4 / "tablas_t4_tramo3.md").read_text(encoding="utf-8")
partes = {int(m.group(1)): m.group(0).rstrip() for m in re.finditer(r"#### Tabla (\d+)\..*?(?=\n#### Tabla |\Z)", tablas, re.S)}
assert sorted(partes) == list(range(1, 13)), sorted(partes)
CEL = ["RI:sin_raiz", "RI:resto", "NG:sin_raiz", "NG:resto"]
d = lambda x, k=4: f"{x:.{k}f}".replace(".", ",")  # noqa: E731
iv = lambda w: f"[{d(w[0])}; {d(w[1])}]"  # noqa: E731
sn = lambda b: "sí" if b else "no"  # noqa: E731
mil = lambda n: f"{n:,}".replace(",", ".")  # noqa: E731
pl = lambda n, s, p: f"{n} {s if n == 1 else p}"  # noqa: E731
A, RI, B60, I6 = X["aceptadas"], X["atencion_RI"], X["aceptadas_no_items_sobre_60"], X["informacion_con_las_60"]
r6, z6 = B60["regla"], B60["sensibilidad_sin_dudosas"]
r3 = A["no_items"]["regla"]
u6 = B60["umbral_del_freno_por_atencion_sobre_60"]
dud = sum(B60["por_celda"][c]["dudosa"] for c in CEL)
otra = [k for k, v in B60["la_sensibilidad_da_otra_decision"].items() if v]
ctrl = X["controles"]
lo2 = X["lo_del_segundo_tramo"]
# lo que el texto afirma
assert all(B60["cada_celda_con_el_doble"].values()) and r6["cada_celda_con_el_doble"], "el texto dice que cada celda tiene el doble"
assert r6["umbral_recalculado_es_el_del_json"] and r6["el_umbral_y_el_p_valor_dicen_lo_mismo"]
assert r6["freno_por_atencion_sobre_60"] and not r6["freno_por_intervalos"] and r6["freno"], "el texto de las secciones 4 y 5"
assert not otra and dud == 0, "el texto dice que no hay dudosas y que la sensibilidad decide lo mismo"
assert all(lo2["bloques_iguales_a_tasas_t4_tramo2"].values()) and lo2["controles_del_segundo_tramo_iguales"]
assert lo2["lineas_de_base_que_cambian"] == ["aceptadas:total.tanda0", "atencion_RI.tanda0"]
assert fc["ok"] and not any(fc[k]["fuera_de_lo_admitido"] for k in ("nuevos", "borrados", "cambiados")) and fcc["ok"]
assert VER["iguales"] == VER["cifras"] and not VER["distintas"]
ri_igual = all(F_ == G_ for F_, G_ in ((B60["regla"]["k_por_celda"][c] * A["no_items"]["regla"]["n_por_celda"][c],
                                         A["no_items"]["regla"]["k_por_celda"][c] * B60["regla"]["n_por_celda"][c]) for c in ("RI:sin_raiz", "RI:resto")))
mesa_ok = [k for k, v in CTRL_AMP.items() if isinstance(v, dict) and "pasa" in v]
p0txt = P0.read_text(encoding="utf-8").rstrip("\n")
HEAD = re.search(r"^== git log -3.*\n([0-9a-f]{8}) ", p0txt, re.M).group(1)
# las horas de la autora, de los dos sellos
sellos = {}
for p in (T4 / "lectura_autora/sello_lectura_T4.txt", T4 / "ampliacion/lectura_autora/sello_lectura_T4_ampliacion.txt"):
    for ln in p.read_text(encoding="utf-8").splitlines():
        if ln.strip():
            h, f, fecha, hora, tz = ln.split()
            sellos[f] = (fecha, hora)
h30, h60 = sellos["aceptadas_no_items_marcada.csv"], sellos["aceptadas_no_items_ampliacion_marcada.csv"]
# mis propuestas de la ampliación contra la lectura de la autora (información)
with open(T4 / "ampliacion/lectura_autora/aceptadas_no_items_ampliacion_marcada.csv", encoding="utf-8", newline="") as fh:
    marc = list(csv.DictReader(fh, delimiter=";"))
cambios = [(i, x["propuesta"], x["veredicto_autora"]) for i, x in enumerate(marc, 1) if x["propuesta"] != x["veredicto_autora"]]
cprop, caut = Counter(x["propuesta"] for x in marc), Counter(x["veredicto_autora"] for x in marc)
# los .DS_Store del paso 0 y lo que trajeron los commits
n_cambios = fcc["nuevos"] + fcc["cambiados"] + fcc["borrados"]
de_commits = n_cambios - len(fcc["DS_Store"])
assert de_commits == fcc["rutas_en_los_commits"] - fcc["rutas_de_los_commits_ya_iguales_en_disco"]

# los diffs de los cinco scripts contra los del segundo tramo
PARES = [("tasas_t4t2_tf.py", "tasas_t4t3_tf.py"), ("verif_tasas_independiente_t4t2_tf.py", "verif_tasas_independiente_t4t3_tf.py"),
         ("tablas_t4t2_tf.py", "tablas_t4t3_tf.py"), ("freno_t4t2_foto_tf.py", "freno_t4t3_foto_tf.py"),
         ("freno_t4t2_armar_tf.py", "freno_t4t3_armar_tf.py")]
diffs = []
for a, b in PARES:
    ta = (T4 / "scripts" / a).read_text(encoding="utf-8").splitlines()
    tb = (T4 / "scripts" / b).read_text(encoding="utf-8").splitlines()
    diffs.append((a, b, list(difflib.unified_diff(ta, tb, f"tanda_final/t4/scripts/{a}", f"tanda_final/t4/scripts/{b}", n=0, lineterm=""))))

w = ["# FRENO T4 — tanda final de B6.1, tercer tramo: las aceptadas no ítems sobre las 60 y el freno por la atención sobre las 60 "
     "(USD 0, sin API, sin commit)", "",
     "Rigen el pre-registro firmado de la tanda final (`docs/preregistro_tanda_final.md`, firma en `4de7f2a7`), §6, con su versión derivada",
     f"para la lectura de T4 (sha256 `{X['entradas']['preregistro_tanda_final_derivada_T4.md']}`), la regla del freno del script de la mesa y "
     "del pre-registro de la tanda 1 (§5.4, `95b18217:592-593`), el umbral de `t3/muestras/umbrales_t4_tf.json`, la regla de las dudosas "
     "(registro de decisiones, §35), lo que decidió la autora sobre el FRENO del segundo tramo (registro, §85) y el «seguí» del tercer tramo.",
     f"Las lecturas son las de la autora: las 30 del primer tramo, selladas el {h30[0]} a las {h30[1]}, y las 30 de la ampliación, selladas "
     f"el {h60[0]} a las {h60[1]} y controladas por la mesa ({sum(CTRL_AMP[k]['pasa'] for k in mesa_ok)} de {len(mesa_ok)}). HEAD `{HEAD}`.",
     "", "**Resultado:**",
     f"- **Las aceptadas no ítems sobre las 60** (sección 4): {r6['errores']} de {r6['leidas']} con error, contando las dudosas; tasa "
     f"ponderada {d(r6['tasa_ponderada'])}, Wilson {iv(r6['wilson'])} (n efectivo {d(r6['n_efectivo_kish'], 3)}). Sobre las 30 del primer "
     f"tramo era {d(r3['tasa_ponderada'])}.",
     f"- **El freno por la atención sobre las 60: sí.** La tasa ({d(r6['tasa_ponderada'])}) pasa el umbral ({d(r6['umbral_recalculado'])}); "
     f"el p-valor sobre las 60 es {d(r6['p_valor_sobre_60'])}. La ampliación dejó cada celda con el doble de unidades, así que la regla "
     "se aplica tal cual.",
     f"- **El freno por intervalos: no.** El límite inferior del Wilson ({d(r6['wilson'][0])}) no pasa el superior del Wilson de la tanda 0 "
     f"({d(B60['wilson_tanda0'][1])}).",
     "- **Hay freno de T4 por las aceptadas no ítems** (sección 5): la regla da freno si se cumple cualquiera de los dos, y se cumple el "
     "de la atención sobre las 60. Qué sigue no es de esta unidad.",
     f"- **Las dudosas:** {dud}, así que la sensibilidad da la misma decisión.",
     f"- **La ponderada total y la atención de RI con las 60** (sección 6, información): {d(I6['total']['regla']['tasa_ponderada'])} y "
     f"{d(I6['atencion_RI']['regla']['tasa_ponderada_RI'])} (p {d(I6['atencion_RI']['regla']['p_valor'])}); en el segundo tramo, "
     f"{d(A['total']['regla']['tasa_ponderada'])} y {d(RI['regla']['tasa_ponderada_RI'])}.",
     f"- **Lo del segundo tramo** (sección 7), rehecho: {sum(lo2['bloques_iguales_a_tasas_t4_tramo2'].values())} de "
     f"{len(lo2['bloques_iguales_a_tasas_t4_tramo2'])} bloques iguales. En las líneas de base cambian solo los dos textos con el nombre "
     "del archivo, ya sin la coma.",
     f"- **La verificación independiente:** {VER['iguales']} de {VER['cifras']} cifras iguales.",
     "- Toda cifra sale por script de sus archivos. Las tablas que copio de una salida van tal cual; mis aclaraciones van fuera de las tablas.",
     "- Nada commiteado y ningún mensaje de commit preparado: los commits son de la autora y quedan PENDIENTES.", ""]

# 1. Paso 0
w += ["## 1. Paso 0", "",
      "La salida, con la carpeta personal reemplazada por `$HOME` y la carpeta de trabajo por `<DIR DE TRABAJO>` (`paso0_T4_tramo3_salida.txt`, "
      "de `paso0_t4_tramo3.sh`, con la comparación de `paso0_foto_contra_commits_t4_tramo3.py`, en el paquete):", "", "```", p0txt, "```", "",
      f"- **La foto nueva** (`t4t2_fotos/foto_repo_antes_T4t3.json`, sha256 `{fcc['foto_nueva']['sha256']}`) contra la final del segundo "
      f"tramo (`foto_repo_final_T4t2.json`): {fcc['nuevos']} nuevos, {fcc['cambiados']} cambiados y {fcc['borrados']} borrados. "
      f"{len(fcc['DS_Store'])} son `.DS_Store`, ruido de Finder que queda fuera de lo que cuenta (decisión de la autora sobre el FRENO del "
      f"paso 0 del segundo tramo); los otros {de_commits} son rutas de los commits `{fcc['commits']}`. De las {fcc['rutas_en_los_commits']} rutas "
      f"de esos commits, {fcc['rutas_de_los_commits_ya_iguales_en_disco']} ya estaban iguales en disco: son las del segundo tramo, que el "
      "TF4b commiteó sin cambios. Todas dan el sha256 de su blob en HEAD.",
      "- **Los `.DS_Store`** (sin abrirlos): " + ", ".join(f"`{r}`" for r in fcc["DS_Store"]) + ".",
      f"- **Las horas de la autora, de los sellos:** las 30 del primer tramo, {h30[0]} {h30[1]} (`t4/lectura_autora/sello_lectura_T4.txt`); "
      f"las 30 de la ampliación, {h60[0]} {h60[1]} (`t4/ampliacion/lectura_autora/sello_lectura_T4_ampliacion.txt`).", ""]

# 2. Lo decidido
w += ["## 2. Lo que decidió la autora sobre el FRENO del segundo tramo (registro de decisiones, §85)", "",
      "1. La exclusión de `data/experiment/neo4j/volumen` en la copia del repo: aceptada y declarada.",
      "2. El texto «umbrales_t4_tf,json» de `tasas_t4_tramo2.json` se corrige cuando se rehacen las tasas: lo corrige este tramo (sección 7).",
      "3. Que la unidad haya abierto `tanda1/t3/scripts/celdas_t4_t3f.py` y calculado el sha256 de dos `kg.json` de `tanda1/t3/acumulado/` "
      "contra su sello: aceptado y declarado.",
      "4. Para sellar la lectura de la ampliación, la mesa armó `t4/ampliacion/lectura_autora/convertir_lectura_T4_ampliacion.py` y "
      "`LEEME_lectura_T4_ampliacion.md`, que entraron con el commit del segundo tramo. No los toqué.", ""]

# 3. La regla
w += ["## 3. La regla", "",
      "- **El freno** (script de la mesa, `data/experiment/controles_tanda1/umbrales_t4_por_celdas_mesa.py`, docstring, «Freno»; pre-registro "
      "de la tanda 1, `95b18217:592-593`): hay freno si el intervalo de la tasa no se solapa con el Wilson de la tanda 0, «o si la atención "
      "se confirma sobre las 60 (cada celda con el doble de unidades)».",
      f"- **El umbral:** `freno_por_atencion_sobre_60` de `aceptadas.no_items` en `t3/muestras/umbrales_t4_tf.json` (sha256 "
      f"`{X['entradas']['umbrales_t4_tf.json']}`), con los pesos reales: {d(u6['umbral_tasa_ponderada'])}, p {d(u6['p_valor'])}.",
      "- **Las dudosas** (pre-registro, §6; registro, §35): cuentan como error para la tasa, la atención y el freno; la cuenta sin ellas va al "
      "lado como sensibilidad y no decide nada.", ""]

# 4. Las 60
w += ["## 4. Las aceptadas no ítems sobre las 60", "", partes[10], "", partes[11], "",
      "Mis aclaraciones:",
      "- **Los pesos** son los del segundo tramo (`umbrales_t4_tf.json`). Las 60 son las 30 de `t4/lectura_autora/aceptadas_no_items_marcada.csv` "
      "y las 30 de `t4/ampliacion/lectura_autora/aceptadas_no_items_ampliacion_marcada.csv`, cada una contra su sello; `tasas_t4t3_tf.py` "
      "controla además que las de la ampliación sean las de su muestra y que ninguna esté entre las 30 del primer tramo.",
      "- **El doble por celda:** la ampliación salió con las mismas cuotas por celda que la primera muestra, así que cada celda tiene el doble (tabla 10). "
      "No hizo falta aplicar la regla con otras n.",
      "- **El umbral:** con el doble, la distribución bajo H0 de la tasa sobre las 60 es la misma con la que la mesa calculó el umbral (los "
      "mismos pesos, las mismas n y la tasa de la tanda 0). `tasas_t4t3_tf.py` la enumera entera con `distribucion` de la mesa, recalcula el "
      "umbral (la menor tasa con P(T' ≥ t) ≤ 0,05) y controla que, redondeado, sea el del JSON. Decide con el umbral exacto, y el p-valor "
      "va al lado: los dos dicen lo mismo.",
      "- **El freno por intervalos** usa el Wilson con el n efectivo de Kish de las 60 y el superior del Wilson de la tanda 0 de no ítems, "
      "como en el segundo tramo.", ""]

# 5. La decisión
w += ["## 5. Los dos frenos y la decisión", "",
      f"- **Freno por la atención sobre las 60:** {sn(r6['freno_por_atencion_sobre_60'])} (tasa {d(r6['tasa_ponderada'])}, umbral "
      f"{d(r6['umbral_recalculado'])}, p {d(r6['p_valor_sobre_60'])}).",
      f"- **Freno por intervalos:** {sn(r6['freno_por_intervalos'])} (inferior {d(r6['wilson'][0])}, superior de la tanda 0 "
      f"{d(B60['wilson_tanda0'][1])}).",
      f"- **Freno de T4 por las aceptadas no ítems:** {sn(r6['freno'])}. Con las dudosas fuera, lo mismo.",
      "- **Lo que no decido:** qué sigue después del freno. Las líneas de la regla (`95b18217:592-593`) fijan cuándo hay freno; lo que "
      "sigue es de la mesa y la autora (sección 10).", ""]

# 6. Total y RI
w += ["## 6. La ponderada total y la atención de RI con las 60 (información)", "", partes[12], "",
      "Mis aclaraciones:",
      "- **No deciden nada:** la atención de RI se decidió en el segundo tramo, con su umbral de T3 para las n de entonces. Con las 60 van "
      "como información, con el mismo método.",
      ("- **La tasa de RI no cambia** con las 60 porque, en las dos celdas RI de no ítems, la proporción de errores de las 60 es la de las 30. "
       "Cambian el n efectivo, el Wilson y el p-valor." if ri_igual else "- **La tasa de RI cambia** con las 60."), ""]

# 7. Lo del segundo tramo
lb2, lb3 = X2["lineas_de_base"], X["lineas_de_base"]
w += ["## 7. Lo del segundo tramo, rehecho, y las líneas de base", "",
      f"- **`tasas_t4t3_tf.py` rehace todo lo del segundo tramo** y controla, al final, que cada bloque dé lo mismo que "
      f"`tasas/tasas_t4_tramo2.json`: {sum(lo2['bloques_iguales_a_tasas_t4_tramo2'].values())} de {len(lo2['bloques_iguales_a_tasas_t4_tramo2'])} "
      f"(" + ", ".join(f"`{k}`" for k in lo2["bloques_iguales_a_tasas_t4_tramo2"]) + f"). Los controles de entrada del segundo tramo, iguales: "
      f"{sn(lo2['controles_del_segundo_tramo_iguales'])}; los del tercero, {sum(ctrl.values())} de {len(ctrl)}.",
      "- **Las líneas de base:** la coma decimal va ahora solo en los números. Cambian estos dos textos, y nada más:"]
for k in lo2["lineas_de_base_que_cambian"]:
    a, b = k.split(".")
    w += [f"  - `{k}`: antes «{lb2[a][b]}»; ahora «{lb3[a][b]}»."]
w += [""]

# 8. Para la hoja
w += ["## 8. Las cifras para la hoja de la revisión entre tandas", "",
      "Van en `t4/tablas_t4_tramo3.md` (tabla 1), que genera `scripts/tablas_t4t3_tf.py` desde la salida de las tasas, con la fila de no "
      "ítems sobre las 60. La copio tal cual:", "", partes[1], ""]

# 9. Cegamiento
w += ["## 9. El cegamiento", "",
      "- **Ninguna cifra usa el estado de E3, `n_reintentos`, `reintentos_e3.jsonl`, `copias_nota_e3.jsonl`, las `marcas_e3` ni el gasto de "
      "los reintentos.** `tasas_t4t3_tf.py` lee las marcadas y sus sellos, las muestras, las poblaciones, los umbrales, la versión derivada, "
      "el script de la mesa y la salida del segundo tramo.",
      "- **De la tanda 1** no abrí nada: ni muestras, ni material, ni planillas, ni cifras, ni scripts. El script de la mesa "
      "(`controles_tanda1/umbrales_t4_por_celdas_mesa.py`) lo importo sin cambiarlo, como en el segundo tramo, y leí su docstring, que es la "
      "regla del punto 2.",
      "- No abrí ningún `.env` ni ningún `NO_ABRIR_` (la foto da 0 en `t4/`), ni entré en las carpetas vedadas.", ""]

# 10. Para la autora y la mesa
w += ["## 10. Para la autora y la mesa", "",
      "1. **El freno salta** por la atención sobre las 60 de las aceptadas no ítems. Qué sigue lo deciden la mesa y la autora.",
      "2. **La fila de no ítems para la hoja** es ahora la de las 60 (tabla 1); la de las 30 queda dentro de la misma celda.",
      f"3. **Mis propuestas y la lectura de la autora en la ampliación** (información): coinciden en {len(marc) - len(cambios)} de {len(marc)}. "
      f"Las propuestas daban " + ", ".join(f"{v} {k}" for k, v in sorted(cprop.items())) + "; la lectura da "
      + ", ".join(f"{v} {k}" for k, v in sorted(caut.items())) + ". "
      + ("Las que cambian: " + "; ".join(f"ficha {i}, de «{p}» a «{v}»" for i, p, v in cambios) + "." if cambios else ""),
      "4. **La ponderada total y la atención de RI con las 60** van como información (sección 6).", ""]

# 11. Foto y grep
g = grep
w += [FOTO.read_text(encoding="utf-8").strip(), "",
      f"- **El grep de convenciones** (`t3/scripts/grep_convenciones_tf.py`, sin cambios, con `LC_ALL=en_US.UTF-8`) sobre los "
      f"{g['archivos']} archivos nuevos de la foto: {g['coincidencias']} coincidencias de los tokens del nombre y de los términos, "
      f"{len(g['con_rutas_absolutas'])} archivos con rutas absolutas, {g['tokens_dentro_de_rutas_absolutas']} tokens dentro de rutas "
      f"absolutas; control positivo, {g['control_positivo']}. Su salida va en el paquete. Este FRENO y su script se escriben después de la "
      "foto: el control final del paquete confirma que son lo único nuevo desde ella y les pasa el grep.",
      "- **Un `__pycache__` que creé y borré antes de la foto** (sección 13, punto 1): la lista de `.pyc` de después es la del paso 0.",
      "- **No hice copias del repo** en este tramo. Ningún `git clone`.", ""]

# 12. Scripts
w += ["## 12. El script de cada cifra", "",
      "| cifras | script (`t4/scripts/`) | salida |", "|---|---|---|",
      "| las tasas sobre las 60, los dos frenos, lo del segundo tramo rehecho, la ponderada total y la atención de RI con las 60 | "
      "`tasas_t4t3_tf.py` | `tasas/tasas_t4_tramo3.json`, `tasas/distribuciones_bajo_H0_t4_tramo3.json`, `tasas/consola_tasas_t4t3_tf.txt` |",
      "| la verificación independiente | `verif_tasas_independiente_t4t3_tf.py` | `tasas/verif_tasas_independiente_t4t3_tf.json` y su consola |",
      "| las tablas 1 a 12 y las cifras para la hoja | `tablas_t4t3_tf.py` | `tablas_t4_tramo3.md`, `consola_tablas_t4t3_tf.txt` |",
      "| la foto (sección 11) | `freno_t4t3_foto_tf.py` | la sección 11; su salida, en el paquete |",
      "| el texto de este FRENO | `freno_t4t3_armar_tf.py` | este archivo |",
      "| el paso 0 (sección 1) | `paso0_t4_tramo3.sh` y `paso0_foto_contra_commits_t4_tramo3.py`, en el paquete | su salida, pegada |", "",
      f"- **Los controles de la entrada** de `tasas_t4t3_tf.py`: {sum(ctrl.values())} de {len(ctrl)} pasan.",
      f"- **La verificación independiente** recuenta las dos marcadas sin el código de la mesa ni `tasas_t4t3_tf.py` y recalcula con "
      f"fracciones exactas, también el p-valor y el umbral sobre las 60 por convolución: {VER['iguales']} de {VER['cifras']} cifras "
      f"iguales, {len(VER['distintas'])} distintas.",
      "- **Cómo salieron los scripts:** los cuatro primeros los escribieron adaptadores con reemplazos exactos desde los del segundo tramo "
      "(`adaptar_*_t4_tramo3.py`, en el paquete); `freno_t4t3_armar_tf.py` lo escribí desde el del segundo tramo. Los diffs enteros de los "
      "cinco contra los del segundo tramo van en el anexo.", ""]

# 13. Errores
w += ["## 13. Errores propios, con su causa", "",
      "1. **Escribí un `__pycache__` en `t4/scripts/`.** Para controlar la sintaxis de `freno_t4t3_foto_tf.py` corrí `python -m py_compile`, "
      "que escribe el `.pyc` aunque se pase `-B`. Lo vi enseguida con un `find`, y borré el archivo y la carpeta (los dos, solo míos y sin "
      "rastrear) antes de la foto de después. La lista de `.pyc` volvió a ser la del paso 0, y la de después lo confirma.", ""]

# 14. Lo que no hice
w += ["## 14. Lo que no hice", "",
      "- **T5 ni las FICHAS.**",
      "- **Lo que no toqué:** las marcadas, los sellos, las planillas, los convertidores, los LEEME y los controles de la mesa; nada de `t3/` "
      "ni de fuera de `t4/`.",
      "- **Commits y escrituras ajenas:** no commiteé ni preparé mensajes de commit; no escribí en la memoria, en `.claude/` ni en "
      "`.gitignore`.",
      "- **El scratchpad:** nada que se necesite después queda solo en él. El paquete y su copia permanente llevan el paso 0, los "
      "adaptadores, la sección de la foto y el grep; las fotos van a `t4t2_fotos/`.",
      "- Los heredocs, siempre con el delimitador entre comillas.", "",
      "FRENO T4, tercer tramo. Espero la revisión de la mesa.", ""]

# Anexo
w += ["## Anexo. Los diffs enteros de los cinco scripts contra los del segundo tramo", "",
      "Con `difflib.unified_diff`, sin líneas de contexto (`n=0`): cada bloque trae todo lo que cambia.", ""]
for a, b, dl in diffs:
    w += [f"### `{a}` → `{b}` ({len([x for x in dl if x.startswith(('+', '-')) and not x.startswith(('+++', '---'))])} líneas cambiadas)", "",
          "```diff", *dl, "```", ""]
texto = "\n".join(w).rstrip("\n") + "\n"
OUT.write_text(texto, encoding="utf-8")
print(f"{len(texto.splitlines())} líneas; secciones: {len(re.findall(r'^## ', texto, re.M))}; {OUT.name} {sha(OUT)}")
