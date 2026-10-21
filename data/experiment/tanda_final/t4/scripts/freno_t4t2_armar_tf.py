"""B6.1, tanda final, T4, segundo tramo: arma el FRENO T4 (segundo tramo) desde los archivos del repo y del trabajo, por script: toda
cifra del texto sale de un JSON o de una tabla generada; las tablas van tal cual; el texto fijo no lleva cifras propias. Es
tanda1/t4/scripts/freno_t4t2_armar.py con las secciones de la tanda final, la ampliación y los diffs enteros de los cuatro scripts contra
los de la tanda 1 (difflib, sin contexto). Solo lee; escribe data/experiment/tanda_final/t4/FRENO_T4_tramo2.md (frena si ya existe).
Uso: python3 -I -B freno_t4t2_armar_tf.py <repo> <paquete del paso 0> <salida del paso 0 repetido> <seccion_foto.md> <grep.json>
       <foto_contra_despues.json> <control_copia.json>
"""
import difflib
import hashlib
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
R, PQ0, P0B, FOTO, GREP, FC, CC = (Path(x) for x in sys.argv[1:8])
R = R.resolve()
TF = R / "data/experiment/tanda_final"
T4 = TF / "t4"
OUT = T4 / "FRENO_T4_tramo2.md"
if OUT.exists():
    raise SystemExit(f"FRENO: ya existe {OUT}")
L = lambda p: json.loads(Path(p).read_text(encoding="utf-8"))  # noqa: E731
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()  # noqa: E731
X = L(T4 / "tasas/tasas_t4_tramo2.json")
U = L(TF / "t3/muestras/umbrales_t4_tf.json")
POB4 = L(TF / "t3/muestras/poblaciones_t4t1_tf.json")["muestras"]
VER = L(T4 / "tasas/verif_tasas_independiente_t4t2_tf.json")["_resumen"]
grep, fc, cc = L(GREP), L(FC), L(CC)
tablas = (T4 / "tablas_t4_tramo2.md").read_text(encoding="utf-8")
partes = {int(m.group(1)): m.group(0).rstrip() for m in re.finditer(r"#### Tabla (\d+)\..*?(?=\n#### Tabla |\Z)", tablas, re.S)}
assert sorted(partes) == list(range(1, 10)), sorted(partes)
tamp = (T4 / "ampliacion/tablas_ampliacion_t4t2.md").read_text(encoding="utf-8")
pamp = {m.group(1): m.group(0).rstrip() for m in re.finditer(r"#### Tabla (A\d)\..*?(?=\n#### Tabla |\Z)", tamp, re.S)}
assert sorted(pamp) == [f"A{i}" for i in range(1, 6)], sorted(pamp)
M = "aceptadas_no_items_ampliacion"
LA = L(T4 / "ampliacion/lectura_asistida/lectura_asistida_t4_ampliacion.json")
mu = L(T4 / "ampliacion/muestras" / f"{M}.json")
idx = L(T4 / "ampliacion/muestras/sorteo_ampliacion_t4t2_tf.json")
vista = L(TF / "t3/muestras/unidades_a_la_vista_T4.json")["ampliacion"]
CONV = (T4 / "lectura_autora/convertir_lectura_T4.py").read_text(encoding="utf-8")
LEEME = (T4 / "lectura_autora/LEEME_lectura_T4.md").read_text(encoding="utf-8")
CEL = ["RI:sin_raiz", "RI:resto", "NG:sin_raiz", "NG:resto"]
ESTR = ["items", "no_items"]
NOM = {"items": "ítems", "no_items": "no ítems"}
d = lambda x, k=4: f"{x:.{k}f}".replace(".", ",")  # noqa: E731
iv = lambda w: f"[{d(w[0])}; {d(w[1])}]"  # noqa: E731
sn = lambda b: "sí" if b else "no"  # noqa: E731
mil = lambda n: f"{n:,}".replace(",", ".")  # noqa: E731
pl = lambda n, s, p: f"{n} {s if n == 1 else p}"  # noqa: E731
A, RI, C, V, O, AMP = X["aceptadas"], X["atencion_RI"], X["cola"], X["vigilancias"], X["observacion:12"], X["ampliacion"]
dud = {m: sum(b["por_celda"][c]["dudosa"] for c in CEL) for m, b in (("cola", C), ("items", A["items"]), ("no_items", A["no_items"]))}
otra = [k for k, v in {**{f"aceptadas:{s}:{x}": A[s]["la_sensibilidad_da_otra_decision"][x] for s in ESTR for x in ("atencion", "freno_por_intervalos")},
                       "atencion_RI": RI["la_sensibilidad_da_otra_decision"]["atencion"],
                       "cola:regla_del_25": C["la_sensibilidad_da_otra_decision"]["regla_del_25"]}.items() if v]
ctrl = X["controles"]
caps = "; ".join(f"{k}, {v['n']}" for k, v in O["incorrectas_por_capa_pipeline"].items())
vg = lambda m, q: f"{V[m]['cruda']['k']} {q} de {V[m]['cruda']['n']}"  # noqa: E731
salta = [k for k, v in AMP["salta"].items() if v]
# lo que el texto afirma: la decisión por el p y por el umbral de T3 coinciden; salta solo la de no ítems; la ampliación es de ese estrato
for s in ESTR:
    r = A[s]["regla"]
    assert (r["tasa_ponderada"] >= A[s]["umbrales_T3"]["atencion_desde"]) == r["atencion"] == (r["p_valor_atencion"] <= 0.05), s
    assert (r["tasa_ponderada"] >= A[s]["umbrales_T3"]["freno_por_intervalos_desde"]) == r["freno_por_intervalos"], s
assert (RI["regla"]["tasa_ponderada_RI"] >= RI["umbral_T3"]) == RI["regla"]["atencion"]
assert salta == ["aceptadas:no_items"] and AMP["hay_ampliacion"], "el texto de las secciones 7 y 8 es el de la ampliación de no ítems"
assert not any(A[s]["regla"]["freno_por_intervalos"] for s in ESTR), "el texto de la sección 7 dice que no hay freno"
assert mu["estrato"] == "aceptadas:no_items" and mu["n"] == 30 and idx["sha256"] == sha(T4 / "ampliacion/muestras" / f"{M}.json")
assert vista["unidades_a_la_vista_antes"] + vista["unidades_que_suma_la_ampliacion"] == vista["unidades_a_la_vista_despues"]
assert C["regla"]["regla_del_25_se_dispara"] and C["sensibilidad_sin_dudosas"]["regla_del_25_se_dispara"], "el texto de la sección 4"
assert fc["ok"] and not any(fc[k]["fuera_de_lo_admitido"] for k in ("nuevos", "borrados", "cambiados"))
assert cc["nombres_vedados"] == 0 and cc["enlaces"] == 0
m_conv = re.search(r"SHA_PLANILLAS = \{(.*?)\}", CONV, re.S)
conv_muestras = re.findall(r'"([a-z_0-9]+)":', m_conv.group(1))
assert M not in conv_muestras and len(conv_muestras) == 8, conv_muestras
assert "ampliaci" not in LEEME.lower()

# las horas de la autora, del sello
sello = [x.split() for x in (T4 / "lectura_autora/sello_lectura_T4.txt").read_text(encoding="utf-8").splitlines() if x.strip()]
NOMM = {"cola": "cola", "aceptadas_items": "aceptadas ítems", "aceptadas_no_items": "aceptadas no ítems", "vigilancia_2": "(2)",
        "vigilancia_7": "(7)", "vigilancia_1": "(1)", "vigilancia_3": "(3)", "observacion_12": "(12)"}
horas = {}
for h, f, fecha, hora, tz in sorted(sello, key=lambda x: (x[2], x[3])):
    horas.setdefault(fecha, []).append(f"{NOMM[f.removesuffix('_marcada.csv')]} {hora}")
ultima = max((x[2], x[3]) for x in sello)

# el paquete del paso 0: sus archivos, con el sha256 de su manifiesto
man = {ln.split()[1]: ln.split()[0] for ln in (PQ0 / "manifest.txt").read_text(encoding="utf-8").splitlines() if ln.strip()}
P0N = ["FRENO_T4_tramo2_paso0.md", "paso0_T4_tramo2_salida.txt", "paso0_t4_tramo2.sh", "control_sustituto_foto_t4_tramo2.py",
       "control_sustituto_foto_T4_tramo2.json"]
assert all(man[n] == sha(PQ0 / n) for n in P0N), "el paquete del paso 0 no da los sha256 de su manifiesto"
cs = L(PQ0 / "control_sustituto_foto_T4_tramo2.json")
ds0 = cs["C_cuenta"]["nacidos_despues_fuera_de_los_commits"] + cs["D_modificados_despues_fuera_de_los_commits"]
assert all(Path(r).name == ".DS_Store" for r in ds0)
p0b = P0B.read_text(encoding="utf-8").rstrip("\n")
HEAD = re.search(r"^== git log -1.*\n([0-9a-f]{8}) ", p0b, re.M).group(1)

# los diffs de los cuatro scripts contra los de la tanda 1
PARES = [("tasas_t4t2.py", "tasas_t4t2_tf.py"), ("tablas_t4t2.py", "tablas_t4t2_tf.py"), ("freno_t4t2_foto.py", "freno_t4t2_foto_tf.py"),
         ("freno_t4t2_armar.py", "freno_t4t2_armar_tf.py")]
diffs = []
for a, b in PARES:
    ta = (R / "data/experiment/tanda1/t4/scripts" / a).read_text(encoding="utf-8").splitlines()
    tb = (T4 / "scripts" / b).read_text(encoding="utf-8").splitlines()
    dl = list(difflib.unified_diff(ta, tb, f"tanda1/t4/scripts/{a}", f"tanda_final/t4/scripts/{b}", n=0, lineterm=""))
    diffs.append((a, b, dl))

w = ["# FRENO T4 — tanda final de B6.1, segundo tramo: las tasas, la atención y la ampliación (USD 0, sin API, sin commit)", "",
     "Rigen el pre-registro firmado de la tanda final (`docs/preregistro_tanda_final.md`, firma en `4de7f2a7`), §6, con su versión derivada",
     f"para la lectura de T4 (`tanda_final/preregistro/preregistro_tanda_final_derivada_T4.md`, sha256 "
     f"`{X['entradas']['preregistro_tanda_final_derivada_T4.md']}`), el «seguí» del segundo tramo, la regla de las dudosas (registro de",
     "decisiones, §35) y lo que decidió la autora sobre el FRENO del paso 0. La lectura es la de la autora, sellada en",
     f"`t4/lectura_autora/sello_lectura_T4.txt` y controlada por la mesa (`t4/control_lectura_mesa/`). HEAD `{HEAD}`.", "",
     "**Resultado:**"]
for s in ESTR:
    r = A[s]["regla"]
    w.append(f"- **Las aceptadas, {NOM[s]}** (sección 3): {r['errores']} de {r['leidas']} con error, contando las dudosas; tasa ponderada "
             f"{d(r['tasa_ponderada'])}, Wilson {iv(r['wilson'])}. Atención: {sn(r['atencion'])} (p {d(r['p_valor_atencion'])}). Freno: "
             f"{sn(r['freno_por_intervalos'])}.")
w += [f"- **La atención de RI** (sección 3): {RI['regla']['errores']} de {RI['regla']['leidas']}; tasa ponderada de RI "
      f"{d(RI['regla']['tasa_ponderada_RI'])}, p {d(RI['regla']['p_valor_atencion'])}: no salta.",
      f"- **La ampliación** (secciones 7 y 8): sí, por la atención de las aceptadas no ítems. Sorteé {mu['n']} unidades más de las que "
      "no se leyeron, armé su material, la lectura asistida y la planilla en blanco de la autora, y sumé sus unidades a "
      f"`t3/muestras/unidades_a_la_vista_T4.json`, que pasa a sha256 `{sha(TF / 't3/muestras/unidades_a_la_vista_T4.json')}`. Las tasas "
      "sobre las 60 van en el tercer tramo, después de la lectura de la autora.",
      f"- **La cola** (sección 4): {C['regla']['errores']} de {C['regla']['leidas']} con error; tasa ponderada {d(C['regla']['tasa_ponderada'])}, "
      f"Wilson {iv(C['regla']['wilson'])}. La regla del 25 % se dispara: es cifra y vigilancia, no freno.",
      f"- **La observación (12)** (sección 6): {O['cruda']['correctas']} correctas de {O['cruda']['de']}, Wilson {iv(O['cruda']['wilson'])}; "
      f"incorrectas por `capa_pipeline`: {caps}.",
      f"- **Las vigilancias** (sección 5): (1), {vg('vigilancia:1', 'sí')}; (2), {vg('vigilancia:2', 'vaciamientos')}; (3), "
      f"{vg('vigilancia:3', 'duplicaciones')}; (7), {vg('vigilancia:7', 'sin apoyo')}, leída entera.",
      f"- **La regla de las dudosas** (sección 2): hay {dud['cola'] + dud['items'] + dud['no_items']} dudosas en la cola y las aceptadas, así "
      f"que la sensibilidad da otra decisión en {len(otra)} de las seis (atención y freno de cada estrato, atención de RI y regla del 25 % "
      "de la cola).",
      "- Toda cifra sale por script de sus archivos. Las tablas que copio de una salida van tal cual; mis aclaraciones van fuera de las tablas.",
      "- Nada commiteado y ningún mensaje de commit preparado: los commits son de la autora y quedan PENDIENTES.", ""]

# 1. Paso 0
w += ["## 1. Paso 0", "",
      "- **El primer paso 0 frenó** (12:16). La foto de después del primer tramo, que era su punto de comparación, había quedado solo en "
      "`/private/tmp` y se perdió, y había cambios fuera de los commits: "
      f"{len(ds0)} archivos `.DS_Store`. Ese FRENO, su salida y su control sustituto están en el paquete "
      f"`revision_tanda_final_FRENO_T4_tramo2_paso0/` (manifiesto con sha256 `{sha(PQ0 / 'manifest.txt')}`), en la carpeta permanente "
      "de esta sesión, con estos nombres:",
      "  - `FRENO_T4_tramo2_paso0.md`: el FRENO, con el error propio en su sección 5;",
      "  - `paso0_T4_tramo2_salida.txt`, de `paso0_t4_tramo2.sh`: la salida del paso 0;",
      "  - `control_sustituto_foto_t4_tramo2.py` y su salida, `control_sustituto_foto_T4_tramo2.json`: el control sustituto (A a H).",
      "- **Lo que decidió la autora sobre ese FRENO:**",
      "  1. el control sustituto vale como la foto de ese paso 0. Lo que no cubre: el contenido de los no rastreados o ignorados que no "
      "cambiaron de fecha (los cubre por la fecha y la cuenta, no por su sha256, salvo los seis `kg.json`);",
      "  2. los archivos que se llaman exactamente `.DS_Store` son ruido de Finder y quedan fuera de lo que cuenta; se listan con su ruta. "
      "Cualquier otro cambio fuera de lo admitido cuenta, y freno;",
      "  3. el paso 0 se repite antes de las tasas, contra la foto de las 12:16:33 guardada en `t4t2_fotos/`;",
      "  4. la foto de después se compara archivo por archivo con la de las 12:16:33 y se guarda también en `t4t2_fotos/`;",
      "  5. este FRENO cita el paquete del paso 0 y el error propio con los nombres del paquete (sección 14, punto 1).",
      f"- **Los `.DS_Store` del primer paso 0** (sin abrirlos): " + ", ".join(f"`{r}`" for r in sorted(ds0)) + ".",
      "- **El paso 0 repetido**, antes de las tasas. La salida, con la carpeta personal reemplazada por `$HOME` y la carpeta de trabajo por "
      "`<DIR DE TRABAJO>` (`paso0_bis_T4_tramo2_salida.txt`, de `paso0_bis_t4_tramo2.sh`, y la comparación de `foto_contra_t4_tramo2.py`, "
      "en el paquete):", "", "```", p0b, "```", "",
      "- **Las horas de la autora, del sello** (`t4/lectura_autora/sello_lectura_T4.txt`): " + "; ".join(
          f"{f[8:10]}/{f[5:7]}: " + ", ".join(v) for f, v in horas.items()) + f". La última marcada es de las {ultima[1]} del {ultima[0]}, "
      "antes del primer paso 0.", ""]

# 2. Las dudosas
w += ["## 2. La regla de las dudosas y cómo la apliqué", "",
      "- **La regla** (pre-registro de la tanda final, §6; registro de decisiones, §35):",
      "  - en la cola y en las dos de las aceptadas, una unidad «dudosa» cuenta como error para la tasa, la atención y el freno;",
      "  - la misma cuenta con las dudosas fuera, sobre las decididas, va al lado como sensibilidad y no decide nada;",
      "  - si la sensibilidad diera otra decisión de atención o de freno, se declara, y rige la primera.",
      "- **Cómo la apliqué** (`scripts/tasas_t4t2_tf.py`): en cada celda, la regla cuenta k = «con error» + «dudosa» sobre las n leídas; la "
      "sensibilidad cuenta k = «con error» sobre n − «dudosa». Los pesos de las celdas son los mismos en las dos.",
      f"- **Las dudosas:** {dud['cola']} en la cola, {dud['items']} en ítems y {dud['no_items']} en no ítems (tablas 2 y 6).",
      (f"- **Lo que da la sensibilidad:** otra decisión en {len(otra)}. No hay nada que declarar por el tercer punto de la regla." if not otra
       else f"- **Lo que da la sensibilidad:** otra decisión en {', '.join(otra)}; rige la primera."), ""]

# 3. Las aceptadas
r_no = A["no_items"]["regla"]
w += ["## 3. Las aceptadas", "",
      partes[2], "", partes[3], "", partes[4], "", partes[5], "",
      "Mis aclaraciones:",
      "- **Los pesos** son los de `t3/muestras/umbrales_t4_tf.json`, que T3 calculó con las unidades de cada celda antes de leer. "
      "`tasas_t4t2_tf.py` controla que sean los de `t3/muestras/poblaciones_t4_t3f_tf.json` y que las n de cada celda sean las de la muestra.",
      "- **La atención** es el test exacto unilateral al 5 % contra la tanda 0, con la distribución de la tasa enumerada entera por la "
      "función `distribucion` del script de la mesa, importado sin cambiarlo. Su salida al importarse es byte a byte su JSON "
      f"({sn(ctrl['el script de la mesa, importado, da su JSON byte a byte'])}). Las distribuciones van en "
      "`tasas/distribuciones_bajo_H0_t4_tramo2.json`.",
      "- **Los umbrales de T3** van en la tabla 3 como información. La decisión sale del p-valor, y las dos dicen lo mismo en cada estrato: "
      f"en ítems, la tasa ({d(A['items']['regla']['tasa_ponderada'])}) está debajo del umbral de la atención "
      f"({d(A['items']['umbrales_T3']['atencion_desde'])}) y el p pasa de 0,05; en no ítems, la tasa ({d(r_no['tasa_ponderada'])}) pasa el "
      f"umbral ({d(A['no_items']['umbrales_T3']['atencion_desde'])}) y el p ({d(r_no['p_valor_atencion'])}) no pasa de 0,05.",
      "- **El freno** es el de los intervalos: el límite inferior del Wilson de la tasa contra el superior del Wilson de la tanda 0, la misma "
      "comparación que hace `umbrales` en el script de la mesa. No salta en ningún estrato. La tasa de no ítems sobre las 60 y su freno van "
      "en el tercer tramo.",
      f"- **NG `sin_raiz`** (tabla 5): son {mil(sum(X['NG_sin_raiz'][s]['N'] for s in ESTR))} unidades aceptadas. Van con su cifra por celda "
      "y sin umbral, como en la tanda 1 (pre-registro de la tanda 1, `95b18217:619`).", ""]

# 4. La cola
w += ["## 4. La cola", "", partes[6], "",
      "Mis aclaraciones:",
      "- **La ponderada** usa los pesos de la cola de `umbrales_t4_tf.json`, con el n efectivo de Kish.",
      "- **La regla del 25 %** se dispara con la regla de las dudosas y también sin ellas. Es cifra y vigilancia, no freno, como en la tanda 1 "
      "(pre-registro de la tanda 1, `95b18217:641`). Qué se hace con ella en la tanda final queda para la mesa y la autora (sección 11).", ""]

# 5. Las vigilancias
w += ["## 5. Las vigilancias (1), (2), (3) y (7)", "", partes[7], "", partes[8], "",
      "Mis aclaraciones:",
      "- **La ponderación:** las cuatro muestras salieron por celdas, y van la cruda (k sobre las leídas, con el Wilson de esa n) y la "
      "ponderada por celda (con el Wilson del n efectivo de Kish), las dos, como en la tanda 1.",
      f"- **Las no decidibles:** en la (1) quedan fuera de la tasa, con su cuenta (registro de decisiones, §29), y son "
      f"{V['vigilancia:1']['fuera_de_la_tasa']['no decidible']}. En la (2) y en la (7) no hay ninguna: "
      f"{V['vigilancia:2']['por_respuesta']['no decidible']} y {V['vigilancia:7']['por_respuesta']['no decidible']}.",
      f"- **Los pesos:** los de la (1) y la (3) son los de `t3/muestras/poblaciones_t4t1_tf.json` ({mil(POB4['vigilancia:1']['N'])} nodos "
      f"Condicion y {mil(POB4['vigilancia:3']['N'])} grupos). Los de la (2), los de la extracción final de `umbrales_t4_tf.json` "
      f"({mil(U['otras']['vigilancia:2']['N'])} unidades).",
      "- **La (3)** lleva su declaración debajo de la tabla 8. El criterio de su lectura para el par deber y acto regulado es el de la §31 "
      "del registro de decisiones, fijado antes de leer.",
      f"- **La (7)** se leyó entera ({V['vigilancia:7']['leidas']} aristas, sin celdas). Su Wilson es el de la cruda con esa n.", ""]

# 6. La (12)
w += ["## 6. La observación (12)", "", partes[9], "",
      "Mis aclaraciones:",
      "- **La cuenta** es la de la enmienda de la observación 12 (`docs/enmienda_preregistro_tanda0_2026-09-27_observacion12.md:107-111`): "
      "correctas sobre 30, con las no decidibles aparte y en el denominador, y el Wilson sobre correctas / 30. La ponderada por celda va al "
      "lado porque la muestra salió por celdas.",
      f"- **Los pesos** son los del universo de la decisión 1.2 ({mil(POB4['observacion:12']['N'])} aristas, "
      "`t3/muestras/poblaciones_t4t1_tf.json`), los mismos que trae `otras.observacion:12` de `umbrales_t4_tf.json` "
      f"({mil(U['otras']['observacion:12']['N'])} aristas).", ""]

# 7. Atención, freno y ampliación
w += ["## 7. La atención, el freno y la ampliación", "",
      f"- **La atención:** ítems, {sn(AMP['salta']['aceptadas:items'])} (p {d(A['items']['regla']['p_valor_atencion'])}); no ítems, "
      f"{sn(AMP['salta']['aceptadas:no_items'])} (p {d(r_no['p_valor_atencion'])}); RI, {sn(AMP['salta']['RI'])} "
      f"(p {d(RI['regla']['p_valor_atencion'])}). Con las dudosas fuera, lo mismo: "
      + ", ".join(f"{k} {sn(v)}" for k, v in AMP["con_la_sensibilidad"].items()) + ".",
      f"- **El freno:** ítems, {sn(A['items']['regla']['freno_por_intervalos'])}; no ítems, {sn(r_no['freno_por_intervalos'])}.",
      "- **La ampliación: sí,** de las aceptadas no ítems (sección 8). La atención de ítems y la de RI no saltan, así que no se sortea nada "
      "de ítems.", ""]

# 8. La ampliación
la_h = LA["hora_de_la_lectura"][M]
w += ["## 8. La ampliación de las aceptadas no ítems", "",
      "Las tablas A1 a A5 son las de `t4/ampliacion/tablas_ampliacion_t4t2.md`, de `scripts/tablas_ampliacion_t4t2_tf.py` (rutas relativas a "
      "`t4/`). Las copio tal cual.", "",
      "- **El sorteo** (`scripts/sorteo_ampliacion_t4t2_tf.py`): sobre las unidades del estrato que no se leyeron, con las cuotas y las reglas "
      "de celda de la tanda 1 (`celdas_t4_t3f.asignar`, sin cambios) y la cadena `tandafinal:{muestra}:{celda}:ampliacion:{base}` "
      "(«seguí», punto 5; pre-registro, §6: «las ampliaciones con `:ampliacion:`»). La base es el sha256 de la versión para firmar del "
      "pre-registro (`5289b02f`), como en T3; el script controla que el texto firmado (`4de7f2a7`) traiga la base, la plantilla y "
      "«`:ampliacion:`», y que la salida de las tasas diga que salta solo la atención de no ítems.", "",
      pamp["A1"], "", pamp["A2"], "",
      "- **El material** (`scripts/material_ampliacion_t4t2_tf.py`, que es `t3/scripts/material_t4_t3f_tf.py` con la muestra de la "
      "ampliación): corrió sobre la copia del repo (sección 12), sin `ANTHROPIC_API_KEY`, y lo copié a `t4/ampliacion/material/` con su "
      "consola; los sha256 del repo son los de la copia. El control (`scripts/control_material_ampliacion_t4t2_tf.py`, el de T3 con el "
      "índice de la ampliación) da 0 claves vedadas.",
      "- **La lectura asistida** (`scripts/anotar_ampliacion_t4t2.py` y `scripts/armar_lectura_ampliacion_t4t2.py`): como en el primer "
      f"tramo, con los mismos criterios (`criterios_de_la_propuesta`; solo cambia la nota de las dudosas, que remite al tercer tramo). La "
      f"leí yo ({LA['modelo']['nombre']}, `{LA['modelo']['id']}`), sin API; las propuestas se escribieron de "
      f"{la_h['primera_propuesta'][11:19]} a {la_h['ultima_escritura'][11:19]} del {la_h['primera_propuesta'][:10]}. El borrador "
      "se escribió en el repo (`t4/ampliacion/lectura_asistida/borradores/`) y de ahí salen la lectura asistida, las omisiones y "
      "observaciones y la planilla de la autora.",
      f"- **La planilla de la autora:** `t4/ampliacion/lectura_autora/{M}.csv`, con las columnas de las del primer tramo (`id`, `celda`, "
      "`ficha`, `propuesta`, `justificacion`, `veredicto_autora` y `nota_autora`, las dos últimas vacías) y la ruta de cada ficha en "
      f"`t4/ampliacion/material/{M}/fichas_{M}.md`.",
      "- **La lista de unidades a la vista** (`scripts/unidades_a_la_vista_ampliacion_t4t2_tf.py`, con la regla de T3, copiada): corrió sobre "
      "la copia, controló que las ocho muestras de T3 den lo mismo que en la lista vigente y la reemplacé en el repo después de controlar que "
      "la vigente era la de HEAD. Es antes de cualquier sorteo de las FICHAS: no hubo ninguno.", "",
      pamp["A3"], "", pamp["A4"], "", pamp["A5"], "",
      "- **Lo que sigue (tercer tramo):** la autora lee la planilla; con su lectura sellada, las tasas sobre las 60 (las 30 leídas y las 30 "
      "de la ampliación), la atención y el freno. Lo que hace falta antes está en la sección 11, puntos 1 y 2.", ""]

# 9. Para la hoja
w += ["## 9. Las cifras para la hoja de la revisión entre tandas", "",
      "Van en `t4/tablas_t4_tramo2.md` (tabla 1), que genera `scripts/tablas_t4t2_tf.py` desde la salida de las tasas. La copio tal cual:", "",
      partes[1], ""]

# 10. Cegamiento
w += ["## 10. El cegamiento", "",
      "- **Ninguna cifra de este tramo usa el estado de E3, `n_reintentos`, `reintentos_e3.jsonl`, `copias_nota_e3.jsonl`, las `marcas_e3` "
      "ni el gasto de los reintentos.** `tasas_t4t2_tf.py` lee solo las marcadas y su sello, las muestras, las poblaciones, los umbrales, la "
      "versión derivada y el script de la mesa. El material de la ampliación no trae el estado ni las marcas de E3 (tabla A3: 0 claves "
      "vedadas). No miré ningún desglose por estado de E3.",
      "- **Por eso no escribí `t4/NO_ABRIR_conteos_t4_tramo2.json`:** no hay nada que lo use. La foto da 0 `NO_ABRIR_` en `t4/` (sección 12).",
      "- **De la tanda 1** abrí sus cuatro scripts del segundo tramo (`tasas_t4t2.py`, `tablas_t4t2.py`, `freno_t4t2_foto.py` y "
      "`freno_t4t2_armar.py`) y listé los nombres de `tanda1/t4/scripts/`. Además, y lo declaro porque la cláusula dice «solo sus scripts del "
      "segundo tramo»:",
      f"  - leí e importo sin cambios `tanda1/t3/scripts/celdas_t4_t3f.py` (sha256 `{idx['celdas_t4_t3f_sha256']}`), que tiene las cuotas "
      "y las reglas de celda que pide el punto 5. Es código, sin cifras de la tanda 1, y es el que importa el T3 de la tanda final;",
      "  - el control sustituto del primer paso 0 calculó el sha256 de los seis `kg.json` no rastreados contra su sello, dos de ellos de "
      "`tanda1/t3/acumulado/`. No los leyó como datos.",
      "  - No abrí sus muestras, su material, sus planillas, su lectura ni sus cifras: las de base salen de la versión derivada.",
      "- No abrí ningún `.env` ni ningún `NO_ABRIR_`, ni entré en las carpetas vedadas.", ""]

# 11. Para la autora y la mesa
w += ["## 11. Para la autora y la mesa", "",
      f"1. **El convertidor no conoce la planilla de la ampliación.** `t4/lectura_autora/convertir_lectura_T4.py` tiene en `SHA_PLANILLAS` "
      f"las {len(conv_muestras)} muestras del primer tramo y frena con cualquier otra. No lo toqué (el «seguí» lo veda). Para sellar la "
      "lectura de la ampliación hace falta decidir cómo: extenderlo o uno nuevo. Queda PENDIENTE de la mesa.",
      "2. **El LEEME** (`t4/lectura_autora/LEEME_lectura_T4.md`) no nombra la ampliación. Las respuestas válidas son las de las aceptadas, "
      "y las columnas de la planilla, las mismas. Si hace falta una nota para la ampliación, es de la mesa.",
      "3. **Las interpretaciones mías que más pueden pesar en la lectura de la ampliación** (los criterios son los del primer tramo):",
      "   - **U-tipo con el futuro normativo:** la ficha 20 («el Banco Central… determinará si corresponde el pago…», tipada Potestad) y la "
      "28 («El lapso a consultar será el que medie…», tipada Condicion). Es el mismo criterio de la ficha 30 de las aceptadas no ítems del "
      "primer tramo;",
      "   - **la ficha 26** es la única en que miré texto que la ficha no muestra: el punto 1.4 del TO, para el desarrollo de la sigla FCEM. Sin "
      "esa lectura, el desarrollo agregado sería una observación, como en la ficha 6, y la propuesta, «sin error»;",
      "   - **la ficha 22** depende de quién devuelve las operaciones, que el texto no nombra. Su observación da la otra lectura;",
      "   - **la ficha 18:** la entidad financiera es donde se pide el cambio, no quien tiene la facultad. La propongo como «con error».",
      "4. **La cola:** la regla del 25 % se dispara. Qué se hace con ella en la tanda final no es de este mandato.",
      "5. **La fila de no ítems para la hoja** queda con las 30 leídas (tabla 1). Su cifra sobre las 60 es del tercer tramo.",
      "6. **Dos textos de `lineas_de_base` en `tasas/tasas_t4_tramo2.json`** dicen «umbrales_t4_tf,json» (sección 14, punto 4). Las cifras "
      "están bien. Propongo corregir el script cuando se rehagan las tasas en el tercer tramo.",
      "7. **`NO_ABRIR_conteos_t4_tramo2.json`** no existe (sección 10).", ""]

# 12. Foto y grep
g = grep
fotos = FOTO.read_text(encoding="utf-8").strip()
w += [fotos, "",
      f"- **El grep de convenciones** (`t3/scripts/grep_convenciones_tf.py`, sin cambios, con `LC_ALL=en_US.UTF-8`) sobre los "
      f"{g['archivos']} archivos nuevos o cambiados de la foto: {g['coincidencias']} coincidencias de los tokens del nombre y de los "
      f"términos, {len(g['con_rutas_absolutas'])} archivos con rutas absolutas, {g['tokens_dentro_de_rutas_absolutas']} tokens dentro de "
      f"rutas absolutas; control positivo, {g['control_positivo']}. Su salida va en el paquete. Este FRENO y su script se escriben después de "
      "la foto: el control final del paquete confirma que son lo único nuevo desde ella y les pasa el grep.",
      f"- **La copia del repo** (para el material y la lista de la ampliación) es la del `rsync` de la cláusula más una exclusión que la "
      "cláusula no trae, `--exclude=/data/experiment/neo4j/volumen` (sección 14, punto 2). El control da "
      f"{cc['nombres_vedados']} nombres vedados y {cc['enlaces']} enlaces; el log del `rsync` tiene {cc['log_lineas']} líneas, todas «skipping "
      "non-regular file» (los enlaces que `--no-links` no copia). El control y el log van en el paquete. Ningún `git clone`.", ""]

# 13. Scripts
w += ["## 13. El script de cada cifra", "",
      "| cifras | script (`t4/scripts/`) | salida |", "|---|---|---|",
      "| las tasas, la atención, el freno, la sensibilidad, la ampliación (secciones 2 a 7) | `tasas_t4t2_tf.py` | "
      "`tasas/tasas_t4_tramo2.json`, `tasas/distribuciones_bajo_H0_t4_tramo2.json`, `tasas/consola_tasas_t4t2_tf.txt` |",
      "| la verificación independiente de las tasas | `verif_tasas_independiente_t4t2_tf.py` | `tasas/verif_tasas_independiente_t4t2_tf.json`, "
      "su consola |",
      "| las tablas 1 a 9 y las cifras para la hoja (secciones 3 a 6 y 9) | `tablas_t4t2_tf.py` | `tablas_t4_tramo2.md`, "
      "`consola_tablas_t4t2_tf.txt` |",
      "| el sorteo de la ampliación y sus dos corridas | `sorteo_ampliacion_t4t2_tf.py` | `ampliacion/muestras/`, "
      "`ampliacion/segunda_corrida_del_sorteo/`, `ampliacion/consola_sorteo_ampliacion_corrida1.txt` |",
      "| el material de la ampliación y su control | `material_ampliacion_t4t2_tf.py`, `control_material_ampliacion_t4t2_tf.py` | "
      "`ampliacion/material/` |",
      "| la lista de unidades a la vista | `unidades_a_la_vista_ampliacion_t4t2_tf.py` | `../t3/muestras/unidades_a_la_vista_T4.json`, "
      "`ampliacion/consola_unidades_a_la_vista_ampliacion_t4t2_tf.txt` |",
      "| la lectura asistida y la planilla de la autora | `anotar_ampliacion_t4t2.py`, `armar_lectura_ampliacion_t4t2.py` | "
      "`ampliacion/lectura_asistida/`, `ampliacion/lectura_autora/` |",
      "| las tablas A1 a A5 (sección 8) | `tablas_ampliacion_t4t2_tf.py` | `ampliacion/tablas_ampliacion_t4t2.md` y su consola |",
      "| la foto (sección 12) | `freno_t4t2_foto_tf.py` | la sección 12; su salida, en el paquete |",
      "| el texto de este FRENO | `freno_t4t2_armar_tf.py` | este archivo |",
      "| el paso 0 repetido (sección 1) | `paso0_bis_t4_tramo2.sh` y `foto_contra_t4_tramo2.py`, en el paquete | su salida, pegada |", "",
      f"- **Los controles de la entrada** de `tasas_t4t2_tf.py`: {sum(ctrl.values())} de {len(ctrl)} pasan (están en la salida, `controles`).",
      f"- **La verificación independiente** recuenta las marcadas sin el código de la mesa y recalcula las tasas, los Wilson y los p-valores "
      f"por convolución exacta con fracciones: {VER['iguales']} de {VER['cifras']} cifras iguales, {len(VER['distintas'])} distintas.",
      "- **Cómo salieron los scripts:** `tasas_t4t2_tf.py`, `tablas_t4t2_tf.py`, `freno_t4t2_foto_tf.py`, `material_ampliacion_t4t2_tf.py` y "
      "`armar_lectura_ampliacion_t4t2.py` los escribieron adaptadores con reemplazos exactos (`adaptar_*_t4_tramo2.py`, en el paquete) desde "
      "los de la tanda 1 o los del primer tramo y T3; `freno_t4t2_armar_tf.py` lo escribí desde el de la tanda 1. Los diffs enteros de los "
      "cuatro del «seguí» contra los de la tanda 1 van en el anexo.", ""]

# 14. Errores
w += ["## 14. Errores propios, con su causa", "",
      "1. **La foto de después del primer tramo quedó solo en `/private/tmp` y se perdió.** Está declarado en la sección 5 de "
      "`FRENO_T4_tramo2_paso0.md`, del paquete `revision_tanda_final_FRENO_T4_tramo2_paso0/`; lo reemplazó el control sustituto "
      "(`control_sustituto_foto_t4_tramo2.py`, `control_sustituto_foto_T4_tramo2.json`), y la salida del paso 0 es "
      "`paso0_T4_tramo2_salida.txt`, de `paso0_t4_tramo2.sh`. La causa: dejé la foto fuera del paquete porque nombra todas las rutas del "
      "repo, y no la guardé en otro lugar permanente. Desde este tramo, las fotos van a `t4t2_fotos/`, en la carpeta permanente: la de las "
      "12:16:33, la del paso 0 repetido, la de después y la final del paquete.",
      "2. **La copia del repo lleva una exclusión que la cláusula no trae:** `--exclude=/data/experiment/neo4j/volumen`, la base de Neo4j, "
      "fuera de git. La agregué sin que el mandato la autorizara. Ninguno de los tres scripts que corrieron sobre la copia la lee (no nombran "
      "Neo4j), así que no cambia ninguna salida; el control de la copia dio 0 de todos modos. Lo declaro para que la mesa decida.",
      "3. **La primera corrida del sorteo no arrancó.** La consola iba a `t4/ampliacion/`, que todavía no existía, y el shell frenó antes de "
      "correr el script; la segunda corrida, a la carpeta de trabajo, sí corrió (dio el mismo sha256 de la muestra). Borré esa salida, creé "
      "la carpeta y corrí las dos en orden: la del repo y la segunda, que copié a `t4/ampliacion/segunda_corrida_del_sorteo/`. Las tres "
      "dan los mismos bytes (tabla A2).",
      "4. **Dos textos de `lineas_de_base` dicen «umbrales_t4_tf,json».** En `tasas_t4t2_tf.py`, el `.replace(\".\", \",\")` de la coma "
      "decimal se aplica a toda la cadena, con el nombre del archivo (las líneas de `aceptadas:total` y `atencion_RI`). Las cifras están "
      "bien. No volví a correr las tasas: el índice del sorteo guarda el sha256 de su salida, y las tablas arman esas celdas desde los "
      "campos numéricos. Lo vi al armar las tablas.",
      "5. **Tres controles de mis adaptadores frenaron antes de escribir.** El de `adaptar_tasas_t4_tramo2.py` y el de "
      "`adaptar_tablas_t4_tramo2.py` marcaban menciones legítimas de la tanda 1 (la ruta del script de la mesa y la del script de origen en "
      "la cabecera); el de `adaptar_foto_t4_tramo2.py` encontró un `endswith(\".DS_Store\")` que ningún reemplazo cubría. Corregí la lista "
      "o agregué el reemplazo y volví a correr; ningún destino estaba escrito.", ""]

# 15. Lo que no hice
w += ["## 15. Lo que no hice", "",
      "- **T5 ni las FICHAS**, ni las tasas sobre las 60.",
      "- **Lo que no toqué:** las marcadas, las exportaciones, el sello, las planillas del primer tramo, el LEEME, el convertidor y el control "
      "de la mesa; los grafos, los manifiestos, la E0, el código del pipeline, la fixture, `grafos.py`, Neo4j, el backlog y el registro de "
      "alcance. De `t3/` solo cambié `t3/muestras/unidades_a_la_vista_T4.json` (punto 5).",
      "- **Commits y escrituras ajenas:** no commiteé ni preparé mensajes de commit; no escribí en la memoria, en `.claude/` ni en "
      "`.gitignore`.",
      "- **El scratchpad:** nada que se necesite después queda solo en él. El paquete y su copia permanente llevan los scripts del paso 0 "
      "repetido, los adaptadores, la sección de la foto, el grep, el control y el log de la copia; las fotos van a `t4t2_fotos/`.",
      "- Los heredocs, siempre con el delimitador entre comillas.", "",
      "FRENO T4, segundo tramo. Espero la revisión de la mesa.", ""]

# Anexo: los diffs
w += ["## Anexo. Los diffs enteros de los cuatro scripts contra los de la tanda 1", "",
      "Con `difflib.unified_diff`, sin líneas de contexto (`n=0`): cada bloque trae todo lo que cambia.", ""]
for a, b, dl in diffs:
    w += [f"### `{a}` → `{b}` ({len([x for x in dl if x.startswith(('+', '-')) and not x.startswith(('+++', '---'))])} líneas cambiadas)", "",
          "```diff", *dl, "```", ""]
texto = "\n".join(w).rstrip("\n") + "\n"
OUT.write_text(texto, encoding="utf-8")
print(f"{len(texto.splitlines())} líneas; secciones: {len(re.findall(r'^## ', texto, re.M))}; {OUT.name} {sha(OUT)}")
