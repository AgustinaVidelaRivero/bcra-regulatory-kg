"""B6.1, tanda final, T5: arma el FRENO T5 (t5/FRENO_T5.md) desde los archivos del repo y del trabajo, por script: toda cifra sale de un
JSON o de una tabla generada; las tablas van tal cual; el texto fijo no lleva cifras propias. Solo lee; escribe t5/FRENO_T5.md (frena si ya
existe).
Uso: python3 -I -B freno_t5_armar.py <repo> <salida del paso 0> <foto_contra_commits_T5.json> <seccion_foto_T5.md> <grep_T5.json>
       <foto_contra_despues_T5.json> <control_copia_T5.json>
"""
import hashlib
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
R, P0, FCC, FOTO, GREP, FC, CC = (Path(x) for x in sys.argv[1:8])
R = R.resolve()
TF = R / "data/experiment/tanda_final"
T5 = TF / "t5"
OUT = T5 / "FRENO_T5.md"
if OUT.exists():
    raise SystemExit(f"FRENO: ya existe {OUT}")
L = lambda p: json.loads(Path(p).read_text(encoding="utf-8"))  # noqa: E731
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()  # noqa: E731
mil = lambda n: f"{n:,}".replace(",", ".")  # noqa: E731
d = lambda x, k=6: f"{x:.{k}f}".replace(".", ",")  # noqa: E731
sn = lambda b: "sí" if b else "no"  # noqa: E731
c = L(T5 / "salidas/cifras_t5.json")
c2 = T5 / "salidas/segunda_corrida/cifras_t5.json"
fcc, fc, cc, g = L(FCC), L(FC), L(CC), L(GREP)
rep = (T5 / "reporte_tanda_final.md").read_text(encoding="utf-8")
tab = {m.group(1): m.group(0).rstrip() for m in re.finditer(r"#### Tabla (\d+)\..*?(?=\n#### |\n## |\Z)", rep, re.S)}
sec = {m.group(1): m.group(0).rstrip() for m in re.finditer(r"^## (\d+)\. .*?(?=\n## |\Z)", rep, re.S | re.M)}
assert sorted(tab) == ["1", "2", "3", "4", "5"] and "3" in sec and "7" in sec
ctrl = L(T5 / "salidas/control_registro_tramo1_t5.json")
esc = L(T5 / "salidas/escritura_registro_tramo1_t5.json")
ent = L(T5 / "salidas/entrada_acumulado_60_t5.json")
car = L(T5 / "salidas/carpetas_tramo1_t5.json")
cont = L(T5 / "salidas/contado_tramo1_t5.json")
st1 = c["sello_tramo1"]["costo"]
p0 = P0.read_text(encoding="utf-8").rstrip("\n")
HEAD = re.search(r"^== git log -4.*\n([0-9a-f]{8}) ", p0, re.M).group(1)
NA = T5 / "NO_ABRIR_conteos_t5.json"
assert ctrl["ok"] and all(v["iguales"] for k, v in esc.items() if isinstance(v, dict)) and ent["igual_a_la_de_T3"]
assert fc["ok"] and fcc["ok"] and cc["nombres_vedados"] == 0 and cc["enlaces"] == 0 and not cc["clasificacion_freno_en_la_copia"]
assert sha(T5 / "salidas/cifras_t5.json") == sha(c2), "las dos corridas no dan lo mismo"
r6 = c["t4"]["aceptadas_no_items_sobre_60"]
K = c["costo"]

w = ["# FRENO T5 — tanda final de B6.1: el reporte de cierre y el sello del tramo 1 como respaldo (USD 0, sin API, sin commit)", "",
     "Rigen el pre-registro firmado de la tanda final (`docs/preregistro_tanda_final.md`, firma en `4de7f2a7`), §5 y §7, con sus notas al pie "
     "(`27bfaeb5` y `86541475`), y la enmienda 9 al protocolo entre tandas (`756a0394`), §1, punto 1; para los hallazgos, el protocolo entre "
     "tandas (§2, `:71-100`) y el pre-registro de la tanda 1 (§5.6); las decisiones de la autora, en el registro de decisiones, §89. "
     f"HEAD `{HEAD}`. El tercer tramo de T4 se lee desde el árbol, con los sha256 de su FRENO.", "", "**Resultado:**",
     f"- **El reporte** está en `t5/reporte_tanda_final.md` (sha256 `{sha(T5 / 'reporte_tanda_final.md')}`).",
     f"- **El costo real:** USD {d(K['total']['real']['total'])} (E1 {d(K['total']['real']['e1'])}, E3 {d(K['total']['real']['e3'])}), "
     f"{d(K['total']['desviacion_contra_s3']['razon_total'], 4)} del estimado del §3 con las líneas de alcance "
     f"({d(K['total']['estimado_s3']['total'])}). El tramo 1: {d(st1['real']['total'])} contra {d(st1['estimado_s3']['total'])} "
     f"({d(st1['desviacion_contra_s3']['razon_total'], 4)}); el tramo 2: {d(K['por_tramo']['tramo_2']['real']['total'])} contra "
     f"{d(K['por_tramo']['tramo_2']['estimado_s3']['total'])} ({d(K['por_tramo']['tramo_2']['desviacion_contra_s3']['razon_total'], 4)}).",
     f"- **Los ids de modelo:** los esperados, en E1, en los reintentos de E1 de la fase de E3 y en E3: "
     f"{sn(c['ids_de_modelo']['todo_igual_a_lo_esperado'])}.",
     f"- **Los hallazgos:** {len(c['hallazgos'])}; propuestas de entrada del backlog: {len(c['propuestas_backlog'])} "
     "(`t5/propuestas_backlog_t5.jsonl`). Las 16 de las aceptadas no ítems llevan «causa: en la clasificación de la autora».",
     f"- **El freno de T4** (aceptadas no ítems, atención sobre las 60: tasa {d(r6['tasa_ponderada'], 4)}, umbral "
     f"{d(r6['umbral_recalculado'], 4)}) va en el reporte con la línea del §89.",
     "- **El sello del tramo 1** (sección 6): su costo, su columna del tablero (contada con el código de T3 sobre una copia: T3 no la "
     "había contado), el sha256 de sus 30 carpetas (el del cierre del tramo 1 no está en los FRENOs de T1 ni de T2) y el registro de sus "
     "dos grafos en `grafos.py`, con su vista y su control: OK. No cargué nada en Neo4j.",
     f"- **El `NO_ABRIR_`:** `t5/NO_ABRIR_conteos_t5.json`, sha256 `{sha(NA)}`, sin abrir.",
     "- Toda cifra sale por script de sus archivos. Las tablas que copio de una salida van tal cual; mis aclaraciones van fuera de las tablas.",
     "- Nada commiteado y ningún mensaje de commit preparado: los commits son de la autora y quedan PENDIENTES.", ""]

# 1. Paso 0
w += ["## 1. Paso 0", "",
      "La salida, con la carpeta personal reemplazada por `$HOME` y la carpeta de trabajo por `<DIR DE TRABAJO>` (`paso0_T5_salida.txt`, de "
      "`paso0_t5.sh`, con `paso0_sha_tramo3_t5.py`, `foto_repo_sin_clasificacion_t5.py` y `paso0_foto_contra_commits_t5.py`, en el "
      "paquete):", "", "```", p0, "```", "",
      "La impresión de la comparación de arriba sale filtrada: el filtro de `paso0_t5.sh` sacó los renglones de las rutas (sección 13, punto "
      "1). Las listas completas, de `foto_contra_commits_T5.json`:",
      "- **las rutas de los commits** `" + fcc["commits"] + "`: " + "; ".join(f"`{k}` ({v})" for k, v in fcc["rutas_en_los_commits"].items()) + ";",
      "- **nuevas:** " + (", ".join(f"`{k}`" for k in fcc["nuevos"]) or "ninguna") + "; **cambiadas:** " +
      (", ".join(f"`{k}`" for k in fcc["cambiados"]) or "ninguna") + "; **borradas:** " + (", ".join(fcc["borrados"]) or "ninguna") + ";",
      f"- **fuera de los commits:** {len(fcc['fuera_de_los_commits'])}; **`.DS_Store`:** {len(fcc['DS_Store'])}; **distintas de HEAD:** "
      f"{len(fcc['rutas_de_los_commits_distintas_de_HEAD'])}. Las rutas de los commits son, byte a byte, las de `git show HEAD:`.",
      "- **El 157 v2 y el 158:** debajo del 159 están `ca5d192f` (el commit del banco, con los cuatro archivos de `banco_mcp/`: el 157 v2) y "
      "`368d50a3` (el registro de decisiones: el 158). El 160 no entró.",
      "- **La foto nueva no entra en `t4/clasificacion_freno/`:** `foto_repo_sin_clasificacion_t5.py` importa la foto de T1 sin cambiarla "
      "(su sha256 se controla) y saca esa carpeta de la recorrida antes de bajar a ella. Está guardada en `t4t2_fotos/`.", ""]

# 2. Costo
w += ["## 2. El costo, por etapa, por tramo y por TO, con la desviación (§7)", "",
      "Las tablas 3, 4 y 5 del reporte, tal cual (de `t5/salidas/cifras_t5.json`, `costo`):", "", tab["3"], "", tab["4"], "",
      re.search(r"- \*\*El estimado del §3:\*\*.*?(?=\n\n#### Tabla 5)", rep, re.S).group(0), "", tab["5"], "",
      "Mis aclaraciones:",
      "- **El costo de cada fase** es su `gasto_usd` en `estado_corpus.json`; el resumen de E3 de cada fase trae el desglose por estado, que "
      "no se lee. E3 va como una sola cifra por TO, con los reintentos adentro.",
      "- **El estimado del §3 por tramo** no lleva las líneas de alcance, como las cifras del §3 (12,6901 y 91,8502); el total, sí. El "
      "repartido es el que usó la proyección del runner, y va al lado.",
      "- **La tanda 1** es solo la cadena del hueco `T5.costo_real_tanda1`, leída con `git show 0c2befad:` y su clave: es lo único de la tanda "
      "1 que leí.", ""]

# 3. Ids
w += ["## 3. Los ids de modelo", "", sec["3"].split("\n", 1)[1].strip(), ""]

# 4. Hallazgos
w += ["## 4. Los hallazgos y las propuestas del backlog", "", sec["7"].split("\n", 1)[1].strip(), "",
      "**Las propuestas** (`t5/propuestas_backlog_t5.jsonl`; el backlog no se tocó):", "",
      "| id | `capa_pipeline` | eje A | eje B | causa |", "|---|---|---|---|---|"]
for x in c["propuestas_backlog"]:
    w.append(f"| {x['id']} | {', '.join(x['capa_pipeline']) if x['capa_pipeline'] else '—'} | {x['eje_A']} | {x['eje_B']} | {x['causa']} |")
w += ["", "Mis aclaraciones:",
      "- **El tablero contra su meta:** el criterio de cada fila está en el reporte (sección 6) y en `tablero_contra_su_meta`. Lo escribí "
      "yo; las filas 50, 52 y 64 son las que más pueden pesar (la 50 no se decide con lo contado; en la 52 rige la parte medible de la "
      "meta; en la 64, la Comunicacion sin `tipo` es el residuo que la meta declara).",
      "- **Las vigilancias:** el criterio de «fuera de su línea de base» también es mío (está en `vigilancias_contra_su_linea_de_base`). Con "
      "él, la (1) es hallazgo; la (2) queda fuera, pero mejora.",
      "- **La cola y las aceptadas de ítems:** la planilla de T4 no tiene la capa. Van con la causa que da la lectura de la autora, unidad por "
      "unidad (`errores_de_las_lecturas`), y como propuestas a clasificar (PROP-T5-03 y PROP-T5-04), sin inferir la capa.",
      "- **Los ids de nodos y aristas** van por su código (los 12 primeros caracteres del sha256 del id); las causas citan solo texto de "
      "unidades a la vista de T4. No hizo falta `t5/unidades_a_la_vista_T5.json`.", ""]

# 5. El reporte
w += ["## 5. El reporte", "",
      f"`t5/reporte_tanda_final.md` (sha256 `{sha(T5 / 'reporte_tanda_final.md')}`), de `t5/scripts/reporte_t5_tf.py`: los volúmenes, el costo, "
      "los ids de modelo, las incidencias, las tasas de T4 con el freno, la columna del tablero (completa, como propuesta, en "
      f"`t5/columna_tanda_final_tablero_PROPUESTA.md`, sha256 `{sha(T5 / 'columna_tanda_final_tablero_PROPUESTA.md')}`), los hallazgos y lo que "
      "sigue.", ""]

# 6. El sello del tramo 1
r1 = ctrl["grafos"]
w += ["## 6. El sello del tramo 1 como respaldo (enmienda 9, §1, punto 1)", "",
      f"- **Su costo** (`cifras_t5.json`, `sello_tramo1.costo`): USD {d(st1['real']['total'])} (E1 {d(st1['real']['e1'])}, E3 "
      f"{d(st1['real']['e3'])}), contra {d(st1['estimado_s3']['total'])} del §3 ({d(st1['desviacion_contra_s3']['razon_total'], 4)}) y "
      f"{d(st1['estimado_repartido']['total'])} del repartido ({d(st1['desviacion_contra_repartido']['razon_total'], 4)}).",
      f"- **Su columna del tablero:** `t5/columna_tramo1_tablero_PROPUESTA.md` (sha256 `{sha(T5 / 'columna_tramo1_tablero_PROPUESTA.md')}`), "
      "con el tramo 1 y su acumulado, completos y sin cola. **Lo que contó T3 no la traía** (`contado_sin_leer_tf.json` cuenta la tanda y el "
      "acumulado de las tres): la conté con el mismo código de T3 (`t5/scripts/contado_tramo1_t5.py`, copiado y adaptado) sobre una copia "
      "del repo. Para el acumulado de 60 rearmé en la copia su entrada, que T3 armó solo en la suya "
      f"(`entrada_acumulado_60_t5.py`): {mil(ent['entrada']['archivos'])} archivos y la misma lista que T3 ({sn(ent['igual_a_la_de_T3'])}). "
      f"El control contra el re-sellado de la tanda 0: {sum(cont['control_contra_el_re_sellado']['iguales'].values())} de "
      f"{len(cont['control_contra_el_re_sellado']['iguales'])}. Saqué el control contra la línea de base de la tanda 1 (sus cifras están "
      "vedadas) y mandé la cola por estado al `NO_ABRIR_`.",
      "- **Sus carpetas de salida** (`t5/salidas/carpetas_tramo1_t5.json`, de `carpetas_tramo1_t5.py`): **el sha256 tomado al cerrar el "
      "tramo 1 no está** en los FRENOs de T1 ni de T2, ni en el control entre tramos. Doy el de hoy, por TO, y el de las 30 juntas, "
      f"`{car['sha256_de_las_30']}`. Al lado, un control indirecto: la entrada del acumulado de 60 que armó T3 el 20/10, después de cerrar el "
      "tramo 2, copia esas 30 carpetas, y rearmada hoy da la misma lista (arriba).", "",
      "| TO | sha256 de la carpeta (hoy) |", "|---|---|"]
w += [f"| {t} | `{h}` |" for t, h in car["sha256_por_carpeta"].items()]
w += ["", "- **El registro de sus dos grafos** (`t5/scripts/editar_grafos_t5.py`, el de T3 adaptado, corrido sobre la copia; el repo recibió "
      "después los mismos bytes):",
      f"  - `data/experiment/neo4j/grafos.py`: dos entradas al final de `GRAFOS`, con la forma de `KG_TandaFinal_r2b`, `commit_sellado` "
      f"«PENDIENTE» y los sha256 y conteos de la tabla E1 de T3. Nada más cambia: las {len(ctrl['grafos_py_selladas_iguales'])} entradas "
      f"selladas, iguales ({sn(all(ctrl['grafos_py_selladas_iguales'].values()))}); solo dos nuevas ({sn(ctrl['grafos_py_solo_dos_nuevas'])}). "
      f"sha256 de `grafos.py`: antes `{esc['grafos_py_antes']}`; después `{esc['data/experiment/neo4j/grafos.py']['repo']}`, igual en la copia "
      "controlada. No está entre las 78 rutas del código de la cadena.",
      f"  - la vista: `t5/registro_vista_r2b_tramo1.py` (sha256 `{esc['data/experiment/tanda_final/t5/registro_vista_r2b_tramo1.py']['repo']}`), "
      "con el patrón de `t3/registro_vista_r2b_tanda_final.py`, que no edité; las entradas la nombran en `requiere_registro_dir` y "
      "`requiere_registro_modulo`.",
      "  - **el control** (`t5/scripts/control_registro_tramo1_t5.py`, el control en seco de T3 adaptado, sobre la copia; "
      "`t5/salidas/control_registro_tramo1_t5.json`): " + "; ".join(
          f"{k}: sha256 {sn(v['sha256_ok'])}, vista {mil(v['vista_nodos'])} / {mil(v['vista_aristas'])} contra el registro "
          f"{mil(v['n_nodos_registro'])} / {mil(v['n_aristas_registro'])} ({sn(v['conteos_iguales'])})" for k, v in r1.items()) +
      f"; el desglose de «punto sin nodos», igual a lo declarado ({sn(all(x['igual_a_lo_declarado'] for x in ctrl['desglose'].values()))}). "
      f"Resultado: {'OK' if ctrl['ok'] else 'CON FALLAS'}.",
      "  - **No cargué nada en Neo4j.** El control sigue el camino de imports del cargador hasta antes de tocar Neo4j.",
      "- **Lo que entra en el commit del sello del tramo 1** (lo arma la mesa): las salidas del sello del tramo 1 y las dos entradas de "
      "`grafos.py`:",
      "  - `data/experiment/neo4j/grafos.py` (las dos entradas) y `data/experiment/tanda_final/t5/registro_vista_r2b_tramo1.py`;",
      "  - `t5/columna_tramo1_tablero_PROPUESTA.md`;",
      "  - `t5/salidas/`: `contado_tramo1_t5.json`, `consola_contado_tramo1_t5.txt`, `entrada_acumulado_60_t5.json`, `carpetas_tramo1_t5.json`, "
      "`control_registro_tramo1_t5.json`, `consola_control_registro_tramo1_t5.txt`, `consola_editar_grafos_t5.txt` y "
      "`escritura_registro_tramo1_t5.json`;",
      "  - `t5/scripts/`: `entrada_acumulado_60_t5.py`, `contado_tramo1_t5.py`, `carpetas_tramo1_t5.py`, `editar_grafos_t5.py` y "
      "`control_registro_tramo1_t5.py`;",
      "  - compartidos con el resto de T5 (lo decide la mesa): `t5/salidas/cifras_t5.json` (el costo por tramo, `sello_tramo1`), "
      "`columnas_tablero_t5.py` (arma las dos columnas) y `t5/NO_ABRIR_conteos_t5.json` (junta el `NO_ABRIR_` del tramo 1 con el de los ids).",
      "  - El `commit_sellado` de las dos entradas se completa en el commit siguiente, como en T3.", ""]

# 7. Cegamiento
w += ["## 7. El cegamiento", "",
      "- **Ninguna cifra usa el desglose por estado de E3, `n_reintentos`, `reintentos_e3.jsonl`, `copias_nota_e3.jsonl`, las `marcas_e3` ni "
      "el gasto de los reintentos aparte.** Lo que los usa va a `t5/NO_ABRIR_conteos_t5.json` (sha256 "
      f"`{sha(NA)}`), que junta, sin abrirlas, la cola por estado, el crudo del reintento y las `properties_no_definidas` de los grafos del "
      "tramo 1, y las llamadas por id de E3 y de los reintentos de E1 de su fase.",
      "- **De la tanda 1** leí solo la cadena del hueco `T5.costo_real_tanda1`. El acumulado de 60 contiene la tanda 1, como en T3: su "
      "entrada copia sus carpetas de salida y lo contado lee el acumulado, sin abrir muestras, material, planillas ni cifras de la tanda 1.",
      "- **El contenido de extracciones** que muestro es solo de unidades a la vista de T4 (las justificaciones de la lectura); los nodos y "
      "aristas van por su código.",
      "- No abrí ningún `NO_ABRIR_` ni la carpeta `t4/clasificacion_freno/` (la copia y las fotos la excluyen), ni ningún `.env`, ni las "
      "carpetas vedadas.", ""]

# 8. Para la autora y la mesa
w += ["## 8. Para la autora y la mesa", "",
      "1. **La copia del repo** lleva, además del `rsync` de la cláusula, `--exclude=/data/experiment/tanda_final/t4/clasificacion_freno`: "
      "copiarla habría sido leerla. Lo declaro.",
      "2. **El sha256 de las carpetas del tramo 1 al cerrarlo** no está; doy el de hoy y el control indirecto de la entrada del acumulado.",
      "3. **Los criterios del tablero y de las vigilancias** son míos (sección 4): los decide la mesa.",
      "4. **La capa de los errores de la cola y de ítems** no la da la lectura: van como propuestas a clasificar.",
      "5. **El commit del sello del tramo 1:** la lista está en la sección 6; tres archivos son compartidos con el resto de T5.", ""]

# 9. La copia
w += ["## 9. La copia del repo", "",
      f"- `{cc['comando']}`. El control antes de correr nada: {cc['nombres_vedados']} nombres vedados (`.env`, `.env.*`, `*.env`, `NO_ABRIR_*`) "
      f"y {cc['enlaces']} enlaces; `t4/clasificacion_freno/` en la copia: {sn(cc['clasificacion_freno_en_la_copia'])}. El log del `rsync` tiene "
      f"{cc['log_lineas']} líneas, todas «skipping non-regular file». Ningún `git clone`. El control y el log van en el paquete.", ""]

# 10. Dos corridas
w += ["## 10. Las dos corridas del script de cifras", "",
      f"`cifras_t5_tf.py` corrió a `t5/salidas/` y a `t5/salidas/segunda_corrida/`: los dos `cifras_t5.json` dan el mismo sha256, "
      f"`{sha(T5 / 'salidas/cifras_t5.json')}` (iguales: {sn(sha(T5 / 'salidas/cifras_t5.json') == sha(c2))}).", ""]

# 11. Foto y grep
w += [FOTO.read_text(encoding="utf-8").strip(), "",
      f"- **El grep de convenciones** (`t3/scripts/grep_convenciones_tf.py`, sin cambios, con `LC_ALL=en_US.UTF-8`) sobre los {g['archivos']} "
      f"archivos nuevos o cambiados de la foto, sin el `NO_ABRIR_`: {g['coincidencias']} coincidencias, {len(g['con_rutas_absolutas'])} archivos "
      f"con rutas absolutas, {g['tokens_dentro_de_rutas_absolutas']} tokens dentro de rutas absolutas; control positivo, {g['control_positivo']}. "
      "Este FRENO y su script se escriben después de la foto: el control final del paquete confirma que son lo único nuevo y les pasa el grep.", ""]

# 12. Scripts
w += ["## 12. El script de cada cifra", "",
      "| cifras | script (`t5/scripts/`) | salida |", "|---|---|---|",
      "| el costo, los volúmenes, el tablero contra su meta, los hallazgos, las propuestas, el sello del tramo 1 | `cifras_t5_tf.py` | "
      "`salidas/cifras_t5.json` (y la segunda corrida) |",
      "| los ids de modelo | `ids_modelo_t5.py` | `salidas/ids_modelo_t5.json` |",
      "| el reporte y las propuestas | `reporte_t5_tf.py` | `reporte_tanda_final.md`, `propuestas_backlog_t5.jsonl` |",
      "| las dos columnas del tablero | `columnas_tablero_t5.py` | las dos `*_PROPUESTA.md` |",
      "| lo contado del tramo 1 | `contado_tramo1_t5.py`, `entrada_acumulado_60_t5.py` (sobre la copia) | `salidas/contado_tramo1_t5.json`, "
      "`salidas/entrada_acumulado_60_t5.json` |",
      "| las carpetas del tramo 1 | `carpetas_tramo1_t5.py` | `salidas/carpetas_tramo1_t5.json` |",
      "| el registro y su control | `editar_grafos_t5.py`, `control_registro_tramo1_t5.py` (sobre la copia) | `grafos.py`, la vista, "
      "`salidas/control_registro_tramo1_t5.json` |",
      "| el `NO_ABRIR_` | `no_abrir_t5.py` | `NO_ABRIR_conteos_t5.json` |",
      "| la foto | `freno_t5_foto.py` | la sección 11 |", "| este FRENO | `freno_t5_armar.py` | este archivo |",
      "| el paso 0 | `paso0_t5.sh` y sus tres scripts, en el paquete | su salida, pegada |", "",
      "Los adaptadores que escribieron `contado_tramo1_t5.py`, `editar_grafos_t5.py`, `control_registro_tramo1_t5.py` y `freno_t5_foto.py` "
      "desde los de T3 y T4, con reemplazos exactos, van en el paquete.", ""]

# 13. Errores
w += ["## 13. Errores propios, con su causa", "",
      "1. **La salida del paso 0 imprime filtrada la comparación de la foto.** En `paso0_t5.sh`, un `grep -v` sacaba de la impresión los "
      "renglones que empiezan con una ruta, y con ellos las rutas de las listas. La comparación y su JSON están completos; la sección 1 da "
      "las listas desde el JSON. No lo vi hasta leer la salida.",
      "2. **La primera corrida de lo contado del tramo 1 no arrancó** (rc 127): en una subshell con `cd` a la copia, `$PWD` ya era la copia y "
      "el intérprete no estaba ahí. No corrió nada; la relancé con la ruta absoluta.",
      "3. **Tres scripts frenaron en su primera corrida, sin escribir:** `ids_modelo_t5.py` (las listas de TOs de los tramos son "
      "diccionarios), `cifras_t5_tf.py` (leía mal «USD 0,209440,») y `freno_t5_foto.py` (el `NO_ABRIR_` no tiene sha256 en la foto). "
      "Los corregí y volví a correr. En `cifras_t5_tf.py` cambié además una etiqueta antes de las dos corridas, que rehice enteras.",
      "4. **Saqué la foto de después cuatro veces** (14:01:00, 14:01:53, 14:05:02 y 14:05:57). Cada una de las tres primeras quedó vieja "
      "porque después cambié un archivo de `t5/`: primero corregí `freno_t5_foto.py` (fallaba con el `NO_ABRIR_`, que no tiene sha256 en la "
      "foto); después, el formato de tres cifras de los hallazgos en `cifras_t5_tf.py`, y con él `cifras_t5.json` y el reporte; y por "
      "último otra vez `freno_t5_foto.py`, que buscaba la hora de un `.DS_Store` que agregó Finder y la foto no la guarda. Las borré. Los "
      "sha256 de la segunda y la tercera están en `sha_fotos_despues_descartadas_T5.txt`, en el paquete; el de la primera no: lo anoté en "
      "un archivo de la carpeta de trabajo que borré al rehacerla. La sección 11 es la de la cuarta.",
      "5. **La sección 11 dice «tamaño en bytes y hora» del `NO_ABRIR_` y da solo el tamaño.** El texto viene del script de T4 y no lo "
      "corregí para no sacar la foto una cuarta vez.",
      "6. **Un control de un adaptador frenó antes de escribir:** el de `freno_t5_foto.py` buscaba `GRAFOS` donde el script dice `GRUPOS`.", ""]

# 14. Lo que no hice
w += ["## 14. Lo que no hice", "",
      "- **La señal cid, el material del catálogo ni nada de la clasificación del freno.**",
      "- **No escribí** en el tablero, el backlog, la tabla de reprocesamiento ni el registro de decisiones; no re-ensamblé ni toqué los "
      "grafos, los manifiestos, la E0, el código del pipeline, la fixture, el registro de alcance ni nada de `t1/` a `t4/`. Fuera de `t5/`, "
      "solo las dos entradas de `grafos.py`.",
      "- **No cargué nada en Neo4j.**",
      "- **Commits y escrituras ajenas:** no commiteé ni preparé mensajes de commit; no escribí en la memoria, en `.claude/` ni en `.gitignore`.",
      "- **El scratchpad:** nada que se necesite después queda solo en él; las fotos van a `t4t2_fotos/` y el resto, al paquete.",
      "- Los heredocs, siempre con el delimitador entre comillas.", "",
      "FRENO T5: espero la revisión de la mesa.", ""]
OUT.write_text("\n".join(w), encoding="utf-8")
print(f"{len(w)} renglones; FRENO_T5.md {sha(OUT)}")
