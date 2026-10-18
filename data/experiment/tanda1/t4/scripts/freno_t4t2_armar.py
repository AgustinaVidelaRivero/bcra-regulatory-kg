"""B6.1, tanda 1, T4, segundo tramo, punto 8: arma el FRENO T4 (segundo tramo) desde los archivos del repo y del trabajo, por script: toda
cifra del texto sale de un JSON o de una tabla generada; las tablas van tal cual; el texto fijo no lleva cifras propias. Solo lee; escribe
<salida.md> (fuera del repo). Copia de freno_t4t1_armar.py con las secciones de este tramo.
Uso: python3 -I -B freno_t4t2_armar.py <repo> <paso0.md> <seccion_foto.md> <grep.json> <salida.md>
"""
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
R, P0, FOTO, GREP, OUT = (Path(x) for x in sys.argv[1:6])
T4 = R / "data/experiment/tanda1/t4"
L = lambda p: json.loads(Path(p).read_text(encoding="utf-8"))  # noqa: E731
X = L(T4 / "tasas/tasas_t4_tramo2.json")
U = L(R / "data/experiment/tanda1/t3/muestras/umbrales_t4_reales.json")
POB4 = L(T4 / "muestras/poblaciones_t4_tramo1.json")["muestras"]
grep = L(GREP)
tablas = (T4 / "tablas_t4_tramo2.md").read_text(encoding="utf-8")
partes = {int(m.group(1)): m.group(0).rstrip() for m in re.finditer(r"#### Tabla (\d+)\..*?(?=\n#### Tabla |\Z)", tablas, re.S)}
assert sorted(partes) == list(range(1, 10)), sorted(partes)
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
assert not AMP["hay_ampliacion"], "con ampliación, este FRENO no sirve: faltan el sorteo, el material, las planillas y la lista nueva"
ctrl = X["controles"]
caps = "; ".join(f"{k}, {v['n']}" for k, v in O["incorrectas_por_capa_pipeline"].items())
vg = lambda m, q: f"{V[m]['cruda']['k']} {q} de {V[m]['cruda']['n']}"  # noqa: E731
# lo que el texto afirma sobre los umbrales de T3: la decisión por el p y por el umbral coinciden
for s in ESTR:
    r = A[s]["regla"]
    assert (r["tasa_ponderada"] >= A[s]["umbrales_T3"]["atencion_desde"]) == r["atencion"] == (r["p_valor_atencion"] <= 0.05), s
    assert (r["tasa_ponderada"] >= A[s]["umbrales_T3"]["freno_por_intervalos_desde"]) == r["freno_por_intervalos"], s
assert (RI["regla"]["tasa_ponderada_RI"] >= RI["umbral_T3"]) == RI["regla"]["atencion"]
assert all(not A[s]["regla"]["atencion"] for s in ESTR), "el texto de la sección 3 dice que la tasa está debajo del umbral"
assert sum(X["NG_sin_raiz"][s]["N"] for s in ESTR) == 94  # pre-registro, 95b18217:619
assert C["regla"]["regla_del_25_se_dispara"] and C["sensibilidad_sin_dudosas"]["regla_del_25_se_dispara"], "el texto de la sección 4"

w = ["# FRENO T4 — tanda 1 de B6.1, segundo tramo: las tasas, la atención y la ampliación (USD 0, sin API, sin commit)", "",
     "Rigen el pre-registro firmado (`docs/preregistro_tanda1.md`, firma en `95b18217`, con su nota del 17/10/2026 en `ca5b39fd`), §5.4 y",
     "§5.4 bis, el «seguí» del segundo tramo y lo que decidió la autora sobre las dudosas. La lectura es la de la autora, sellada el",
     "18/10/2026 y controlada por la mesa (`t4/control_lectura_mesa/`). HEAD `b4c42ebd`.", "",
     "**Resultado:**"]
for s in ESTR:
    r = A[s]["regla"]
    w.append(f"- **Las aceptadas, {NOM[s]}** (sección 3): {r['errores']} de {r['leidas']} con error, contando las dudosas; tasa ponderada "
             f"{d(r['tasa_ponderada'])}, Wilson {iv(r['wilson'])}. Atención: {sn(r['atencion'])} (p {d(r['p_valor_atencion'])}). Freno: "
             f"{sn(r['freno_por_intervalos'])}.")
w += [f"- **La atención de RI** (sección 3): {RI['regla']['errores']} de {RI['regla']['leidas']}; tasa ponderada de RI "
      f"{d(RI['regla']['tasa_ponderada_RI'])}, p {d(RI['regla']['p_valor_atencion'])}: no salta." if not RI["regla"]["atencion"] else
      f"- **La atención de RI** (sección 3): salta.",
      f"- **La ampliación** (sección 7): {sn(AMP['hay_ampliacion'])}. No salta ninguna atención, así que no sorteé nada y "
      "`t3/muestras/unidades_a_la_vista_T4.json` no se tocó.",
      f"- **La cola** (sección 4): {C['regla']['errores']} de {C['regla']['leidas']} con error; tasa ponderada {d(C['regla']['tasa_ponderada'])}, "
      f"Wilson {iv(C['regla']['wilson'])}. La regla del 25 % " + ("se dispara" if C["regla"]["regla_del_25_se_dispara"] else "no se dispara")
      + ": es cifra y vigilancia, no freno.",
      f"- **La observación (12)** (sección 6): {O['cruda']['correctas']} correctas de {O['cruda']['de']}, Wilson {iv(O['cruda']['wilson'])}; "
      f"incorrectas por `capa_pipeline`: {caps}.",
      f"- **Las vigilancias** (sección 5): (1), {vg('vigilancia:1', 'sí')}; (2), {vg('vigilancia:2', 'vaciamientos')}; (3), "
      f"{vg('vigilancia:3', 'duplicaciones')}; (7), {vg('vigilancia:7', 'sin apoyo')}, leída entera.",
      f"- **La regla de las dudosas** (sección 2): la sensibilidad, con las dudosas fuera, da otra decisión en {len(otra)} de las seis "
      "(atención y freno de cada estrato, atención de RI y regla del 25 % de la cola).",
      "- Toda cifra sale por script de sus archivos. Las tablas que copio de una salida van tal cual; mis aclaraciones van fuera de las tablas.",
      "- Nada commiteado y ningún mensaje de commit preparado: los commits son de la autora y quedan PENDIENTES.", ""]
w += [P0.read_text(encoding="utf-8").strip(), ""]

# 2. Las dudosas
w += ["## 2. La regla de las dudosas y cómo la apliqué", "",
      "- **Lo que decidió la autora** (va al registro de decisiones; su asiento es de la autora y queda PENDIENTE):",
      "  - en la cola y en las dos de las aceptadas, una unidad «dudosa» cuenta como error para la tasa, la atención y el freno;",
      "  - la misma cuenta con las dudosas fuera, sobre las decididas, va al lado como sensibilidad y no decide nada;",
      "  - si la sensibilidad diera otra decisión de atención o de freno, se declara, y rige la primera.",
      "- **Cómo la apliqué** (`scripts/tasas_t4t2.py`): en cada celda, la regla cuenta k = «con error» + «dudosa» sobre las n leídas; la "
      "sensibilidad cuenta k = «con error» sobre n − «dudosa». Los pesos de las celdas son los mismos en las dos.",
      f"- **Las dudosas:** {dud['cola']} en la cola, {dud['items']} en ítems y {dud['no_items']} en no ítems (tablas 2 y 6).",
      f"- **Lo que da la sensibilidad:** otra decisión en {len(otra)}" + (": " + ", ".join(otra) if otra else "") + ". No hay nada que "
      "declarar por el tercer punto de la regla." if not otra else f"- **Lo que da la sensibilidad:** otra decisión en {', '.join(otra)}; rige "
      "la primera.", ""]

# 3. Las aceptadas
w += ["## 3. Las aceptadas (§5.4 a, con [v8b] y [v8c])", "",
      partes[2], "", partes[3], "", partes[4], "", partes[5], "",
      "Mis aclaraciones:",
      "- **Los pesos** son los de `t3/muestras/umbrales_t4_reales.json`, que T3 calculó con las unidades de cada celda antes de leer. "
      "`tasas_t4t2.py` controla que sean los de `t3/muestras/poblaciones_t4.json` y que las n de cada celda sean las de la muestra.",
      "- **La atención** es el test exacto unilateral al 5 % contra la tanda 0, con la distribución de la tasa enumerada entera por la "
      "función `distribucion` del script de la mesa, importado sin cambiarlo. Su salida al importarse es byte a byte su JSON "
      f"({sn(ctrl['el script de la mesa, importado, da su JSON byte a byte'])}). Las distribuciones van en "
      "`tasas/distribuciones_bajo_H0_t4_tramo2.json`.",
      "- **Los umbrales de T3** van en la tabla 3 como información. La decisión sale del p-valor, y las dos dicen lo mismo: en cada estrato, "
      "la tasa está debajo del umbral de la atención y el p pasa de 0,05.",
      "- **El freno** es el de los intervalos: el límite inferior del Wilson de la tasa contra el superior del Wilson de la tanda 0, la misma "
      "comparación que hace `umbrales` en el script de la mesa. El freno por la atención sobre las 60 no se mira: no hay ampliación.",
      f"- **NG `sin_raiz`** (tabla 5): son {mil(sum(X['NG_sin_raiz'][s]['N'] for s in ESTR))} unidades aceptadas, ceninf y nmcief. Van con "
      "su cifra por celda y sin umbral, como dice el pre-registro (`95b18217:619`).", ""]

# 4. La cola
w += ["## 4. La cola (§5.4 b, con [v8b])", "", partes[6], "",
      "Mis aclaraciones:",
      "- **La ponderada** usa los pesos de la cola de `umbrales_t4_reales.json`. NG `sin_raiz` no tiene unidades en la cola, así que su "
      "celda no pesa ni se lee.",
      f"- **La regla del 25 %** se dispara con la regla de las dudosas y también sin ellas. El pre-registro la fija como cifra y vigilancia, "
      "no como freno (`95b18217:641`). Si se dispara, «se investiga la causa antes de la tanda 2, sin cambiar el grafo sin cola» "
      "(`95b18217:634-635`). Esa investigación no es de este mandato: queda para la mesa y la autora (sección 10).", ""]

# 5. Las vigilancias
w += ["## 5. Las vigilancias (1), (2), (3) y (7)", "", partes[7], "", partes[8], "",
      "Mis aclaraciones:",
      "- **La ponderación:** las cuatro muestras salieron por celdas y el pre-registro no fija cómo se ponderan sus tasas. Van la cruda (k "
      "sobre las leídas, con el Wilson de esa n) y la ponderada por celda (con el Wilson del n efectivo de Kish), las dos.",
      f"- **Las no decidibles:** en la (1) quedan fuera de la tasa, con su cuenta (registro de decisiones, §29), y son "
      f"{V['vigilancia:1']['fuera_de_la_tasa']['no decidible']}. En la (2) y en la (7) no hay ninguna: "
      f"{V['vigilancia:2']['por_respuesta']['no decidible']} y {V['vigilancia:7']['por_respuesta']['no decidible']}.",
      f"- **Los pesos:** los de la (1) y la (3) son los de `t4/muestras/poblaciones_t4_tramo1.json` ({mil(POB4['vigilancia:1']['N'])} nodos "
      f"Condicion y {mil(POB4['vigilancia:3']['N'])} grupos). Los de la (2), los de la extracción final de `umbrales_t4_reales.json` "
      f"({mil(U['otras']['vigilancia:2']['N'])} unidades, decisión 1.3).",
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
      "`t4/muestras/poblaciones_t4_tramo1.json`). El bloque `otras.observacion:12` de `umbrales_t4_reales.json` trae los de A4.1 "
      f"({mil(U['otras']['observacion:12']['N'])} aristas), que no rigen desde esa decisión. La muestra vieja de `t3/` no se leyó.",
      "- **La comparación con la tanda 0:** con las `remite_a` fuera, la (12) de la tanda 1 queda comparable con la de la tanda 0 "
      "(registro de decisiones, §29). La línea de base es la de la tabla 1.", ""]

# 7. Atención, freno y ampliación
w += ["## 7. La atención, el freno y la ampliación", "",
      f"- **La atención:** ítems, {sn(AMP['salta']['aceptadas:items'])} (p {d(A['items']['regla']['p_valor_atencion'])}); no ítems, "
      f"{sn(AMP['salta']['aceptadas:no_items'])} (p {d(A['no_items']['regla']['p_valor_atencion'])}); RI, {sn(AMP['salta']['RI'])} "
      f"(p {d(RI['regla']['p_valor_atencion'])}). Con las dudosas fuera, tampoco salta ninguna: "
      + ", ".join(f"{k} {sn(v)}" for k, v in AMP["con_la_sensibilidad"].items()) + ".",
      f"- **El freno:** ítems, {sn(A['items']['regla']['freno_por_intervalos'])}; no ítems, {sn(A['no_items']['regla']['freno_por_intervalos'])}.",
      "- **La ampliación: no.** No sorteé nada ni armé material, lectura asistida ni planillas. `t3/muestras/unidades_a_la_vista_T4.json` "
      "queda como lo dejó el primer tramo (sección 11). No hay tercer tramo de tasas.", ""]

# 8. Para la hoja
w += ["## 8. Las cifras para la hoja de la revisión entre tandas", "",
      "Van en `t4/tablas_t4_tramo2.md` (tabla 1), que genera `scripts/tablas_t4t2.py` desde la salida de las tasas. La copio tal cual:", "",
      partes[1], ""]

# 9. Cegamiento
w += ["## 9. El cegamiento", "",
      "- **Ninguna cifra de este tramo usa el estado de E3, `n_reintentos`, `reintentos_e3.jsonl`, `copias_nota_e3.jsonl`, las `marcas_e3` "
      "ni el gasto de los reintentos.** `tasas_t4t2.py` lee solo las marcadas y su sello, las muestras, las poblaciones, los umbrales y el "
      "script de la mesa. No miré ningún desglose por estado de E3.",
      "- **Por eso no escribí `t4/NO_ABRIR_conteos_t4_tramo2.json`:** no hay nada que lo use, y no tiene contenido que yo pueda decidir sin "
      "mirar lo que el cegamiento veda. Es mi lectura del punto 7 del mandato («lo que los use va a un archivo nuevo»); si la mesa lo leía de "
      "otro modo, queda para su revisión.",
      "- **El `NO_ABRIR_` del primer tramo** no se tocó ni se abrió: la foto da el mismo tamaño y la misma hora (sección 11).",
      "- No abrí ningún `.env` ni ningún `NO_ABRIR_`, ni entré en las carpetas vedadas.", ""]

# 10. Para la autora y la mesa
w += ["## 10. Para la autora y la mesa", "",
      "1. **La cola:** la regla del 25 % " + ("se dispara" if C["regla"]["regla_del_25_se_dispara"] else "no se dispara") + ". El "
      "pre-registro dice que, si se dispara, «se investiga la causa antes de la tanda 2, sin cambiar el grafo sin cola» "
      "(`95b18217:634-635`). No lo investigué: no es de este mandato.",
      "2. **La regla de las dudosas** va al registro de decisiones. Su asiento queda PENDIENTE.",
      "3. **Las vigilancias y la (12)** van con la cruda y con la ponderada por celda (tabla 1). Cuál va a la hoja lo decide la mesa.",
      "4. **`NO_ABRIR_conteos_t4_tramo2.json`** no existe (sección 9).",
      "5. **Las horas:** la última marcada es anterior a la hora que da la autora para la última conversión (sección 1).", ""]

# 11. Foto y grep
g = grep
fotos = FOTO.read_text(encoding="utf-8").strip()
props = g["propios_con_patron"]
w += [fotos, "",
      f"- **El grep de convenciones** (`grep_convenciones_t4t2.py` y su salida, en el paquete) busca las palabras del `user.name` de git y "
      f"las de origen conversacional (Slack, mail, correo, «como dijo», «pedido por», …) en los {g['archivos']} archivos nuevos o cambiados "
      f"de la foto, sin los `.DS_Store`. El control positivo da la línea {', '.join(map(str, g['control_positivo_lineas']))}. "
      + (f"Con el patrón, en los archivos que redacté: " + "; ".join(f"`{Path(k).name}`, {len(v)} línea(s)" for k, v in props.items())
         + ": son las líneas de un script que describen el patrón del grep. " if props else "Con el patrón, en los archivos que redacté: ninguno. ")
      + f"Las palabras del nombre, en ningún archivo: {not g['nombre_sin_rutas']}. "
      + (f"Con el patrón en otros archivos: {', '.join(f'`{Path(k).name}`' for k in g['con_patron_sin_rutas'] if k not in props)}. "
         if [k for k in g["con_patron_sin_rutas"] if k not in props] else "")
      + f"Rutas con la carpeta personal o el scratchpad: {len(g['con_rutas_absolutas'])} archivo(s)"
      + (f" ({', '.join(f'`{Path(k).name}`' for k in g['con_rutas_absolutas'])})" if g["con_rutas_absolutas"] else "")
      + ". El grep del FRENO va en el mensaje de cierre.",
      "- **La copia** del repo es la del `rsync` de la cláusula, más la exclusión del volumen de Neo4j, y su control dio 0 "
      "(`rsync_copia_t4t2.log` en el paquete). Ningún `git clone`. Ningún heredoc sin el delimitador entre comillas.", ""]

# 12. Scripts
w += ["## 12. El script de cada cifra", "",
      "| cifras | script (`t4/scripts/`) | salida |", "|---|---|---|",
      "| las tasas, la atención, el freno, la sensibilidad, la ampliación (secciones 2 a 7) | `tasas_t4t2.py` | "
      "`tasas/tasas_t4_tramo2.json`, `tasas/distribuciones_bajo_H0_t4_tramo2.json`, `tasas/consola_tasas_t4t2.txt` |",
      "| las tablas 1 a 9 y las cifras para la hoja (sección 8) | `tablas_t4t2.py` | `tablas_t4_tramo2.md` |",
      "| la foto (sección 11) | `freno_t4t2_foto.py` | la sección 11 |",
      "| el texto de este FRENO | `freno_t4t2_armar.py` | este archivo |",
      "| la escritura en el repo | `escribir_en_el_repo_t4t2.py` | `escrituras_en_el_repo_t4t2.json`, en el paquete |",
      "| el paso 0 (sección 1) | los comandos de la sección 1 y `verif_paso0_commits.py` | sus salidas, pegadas; el script, en el paquete |", "",
      f"- **Los controles de la entrada** de `tasas_t4t2.py`: {sum(ctrl.values())} de {len(ctrl)} pasan (están en la salida, `controles`).",
      "- **Una verificación independiente** (`verif_tasas_independiente_t4t2.py`, en el paquete, fuera del repo) recuenta las marcadas sin el "
      "código de la mesa y recalcula las tasas, los Wilson y los p-valores por convolución exacta con fracciones. Da las mismas cifras: su "
      "consola va en el paquete.", ""]

# 13. Errores
w += ["## 13. Errores propios, con su causa", "",
      "1. **El control de entrada de `tasas_t4t2.py` frenó la primera corrida antes de contar.** Comparaba los ids de la (7) y de la (12) "
      "con los de su muestra, y no daban.",
      "   - La causa: en la muestra, una arista es la lista [origen, relación, destino]; en la planilla va con « | » "
      "(`planillas_t4t1.py:93-94`). Comparé sin unir la lista.",
      "   - Lo corregí uniéndola igual que la planilla, y la segunda corrida pasa todos los controles. No había escrito nada.", "",
      "FRENO T4, segundo tramo. Espero la revisión de la mesa."]
texto = "\n".join(w) + "\n"
OUT.write_text(texto, encoding="utf-8")
print(f"{len(texto.splitlines())} líneas; secciones: {len(re.findall(r'^## ', texto, re.M))}")
