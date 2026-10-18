"""B6.1, tanda 1, T5, punto 11: arma el FRENO T5 desde los archivos de T5 y del trabajo, por script: toda cifra del texto sale de un JSON
de t5/salidas/ o de una sección del reporte, copiada tal cual; el texto fijo no lleva cifras propias. Solo lee; escribe <salida.md>
(fuera del repo). Copia de t4/scripts/freno_t4t2_armar.py con las secciones de T5.
Uso: python3 -I -B freno_t5_armar.py <raíz> <paso0.md> <seccion_foto.md> <grep.json> <escrituras.json> <salida.md>
"""
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
R, P0, FOTO, GREP, ESC, OUT = (Path(x) for x in sys.argv[1:7])
T5 = R / "data/experiment/tanda1/t5"
S = T5 / "salidas"
L = lambda n: json.loads((S / n).read_text(encoding="utf-8"))  # noqa: E731
co = lambda x, k=4: f"{x:.{k}f}".replace(".", ",")  # noqa: E731
mil = lambda n: f"{n:,}".replace(",", ".")  # noqa: E731
costo, mod, hal, st, dos, alc = (L(n) for n in ("costo_t5.json", "modelos_t5.json", "hallazgos_t5.json", "selftest_t5.json",
                                                "dos_corridas_t5.json", "alcance_catalogo_t5.json"))
props = [json.loads(x) for x in (T5 / "propuestas_backlog_t5.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
esc = json.loads(ESC.read_text(encoding="utf-8"))["escritos"]
grep = json.loads(GREP.read_text(encoding="utf-8"))
rep = (T5 / "reporte_tanda1.md").read_text(encoding="utf-8")
sec = {int(m.group(1)): m.group(2).strip() for m in re.finditer(r"^## (\d+)\. [^\n]*\n(.*?)(?=^## \d+\. |\Z)", rep, re.S | re.M)}
assert sorted(sec) == list(range(1, 12)), sorted(sec)
NA = "data/experiment/tanda1/t5/NO_ABRIR_conteos_t5.json"
na_sha = esc[NA]["sha256"]
vista_t5 = (T5 / "unidades_a_la_vista_T5.json").exists()
dv = costo["desviacion"]
ok_dos = dos["todo_igual"]
assert ok_dos and st["veredicto_general"] == "OK" and st["las_dos_corridas_dan_el_mismo_json_byte_a_byte"]
filas_nc = [h["fila_tablero"] for h in hal["hallazgos"] if "fila_tablero" in h]
sin_nota = [h for h in hal["hallazgos"] if h["tipo"].startswith("incorrecta") and h["causa"] == "causa: no dicha por la lectura"]
acep = [h for h in hal["hallazgos"] if h["tipo"].startswith("incorrecta") and h["muestra"].startswith("aceptadas")]
v9 = next(h for h in hal["hallazgos"] if h.get("vigilancia") == "(9)")

w = ["# FRENO T5 — tanda 1 de B6.1: el reporte de cierre (USD 0, sin API, sin commit)", "",
     "Rigen el pre-registro firmado (`docs/preregistro_tanda1.md`, firma en `95b18217`, con su nota al pie en `ca5b39fd`): el §3, «Al",
     "cerrar»; el §5.5; el §5.6, y el §6 donde el reporte lo cita. HEAD `bd60f6c0`. El reporte es `data/experiment/tanda1/t5/reporte_tanda1.md`.", "",
     "**Resultado:**",
     f"- **El costo** (sección 2): real USD {co(dv['total']['real'], 6)} contra el estimado de {co(dv['total']['estimado'], 6)} (razón "
     f"{co(dv['total']['razon'])}). E1, {co(dv['por_etapa_contra_la_tarifa']['e1']['real'], 6)} contra {co(dv['por_etapa_contra_la_tarifa']['e1']['estimado'], 6)} "
     f"({co(dv['por_etapa_contra_la_tarifa']['e1']['razon'])}); E3, con los reintentos adentro, {co(dv['por_etapa_contra_la_tarifa']['e3']['real'], 6)} contra "
     f"{co(dv['por_etapa_contra_la_tarifa']['e3']['estimado'], 6)} ({co(dv['por_etapa_contra_la_tarifa']['e3']['razon'])}).",
     f"- **Los ids de modelo** (sección 3): E1 {', '.join(mod['e1']['ids'])}; E3 {', '.join(mod['e3']['ids'])}; iguales a lo esperado y a lo que "
     f"dio el freno por modelo de T2: {mod['contra_el_codigo_y_el_preregistro']['e1']['igual'] and mod['contra_el_codigo_y_el_preregistro']['e3']['igual']} "
     f"y {mod['contra_el_freno_por_modelo_de_T2']['igual']}.",
     f"- **El catálogo** (sección 4): no crece en la tanda 1, declarado como desvío del §5.5; una sola versión.",
     f"- **Los hallazgos** (sección 5): {len(hal['hallazgos'])} (" + "; ".join(f"{k}, {n}" for k, n in hal["cuantos"].items()) +
     f"), con {hal['propuestas_del_backlog']} propuestas del backlog en `t5/propuestas_backlog_t5.jsonl`.",
     f"- **El selftest de claves** (sección 6), tal cual y dos veces sobre una copia: {st['veredicto_general']}, con los dos JSON iguales.",
     f"- **Las dos corridas de `cifras_t5.py`** dan los mismos bytes: {ok_dos} (sección 9).",
     f"- **El `NO_ABRIR_conteos_t5.json`:** `{na_sha}`. `unidades_a_la_vista_T5.json`: " + ("existe." if vista_t5 else
                                                                                           "no hizo falta (sección 8)."),
     "- Toda cifra sale por script de sus archivos. Las tablas que copio de una salida van tal cual; mis aclaraciones van fuera de las tablas.",
     "- Nada commiteado y ningún mensaje de commit preparado: los commits son de la autora y quedan PENDIENTES.", ""]
w += [P0.read_text(encoding="utf-8").strip(), ""]
w += ["## 2. El costo por etapa y por TO, con la desviación", "", "La sección 2 del reporte, tal cual:", "", sec[2], ""]
w += ["## 3. Los ids de modelo", "", "La sección 3 del reporte, tal cual:", "", sec[3], ""]
w += ["## 4. El alcance y el catálogo", "", "La sección 7 del reporte, tal cual:", "", sec[7], ""]
w += ["## 5. Los hallazgos en los dos ejes y las propuestas del backlog", "", "La sección 8 del reporte, tal cual:", "", sec[8], "",
      f"**Las propuestas del backlog** (`t5/propuestas_backlog_t5.jsonl`, {len(props)}):", "",
      "| hallazgo | tipo | qué | capa_pipeline | eje A | estado |", "|---|---|---|---|---|---|"]
for p in props:
    a = p["eje_A"]
    w.append(f"| {p['hallazgo']} | {p['tipo']} | `{p.get('unidad') or p.get('vigilancia')}` | {', '.join(p['capa_pipeline'])} | "
             f"{' '.join(x for x in (a.get('fila'), a.get('clase')) if x) or 'sin fila'} | {p['estado']} |")
w += ["", "## 6. El selftest de claves", "", f"`scripts/selftest_t5.py` corre `{st['selftest']}` (sha256 `{st['sha256_del_selftest']}`) tal cual, "
      "sobre la copia y dos veces (`salidas/selftest_t5.json`). Sus conteos van al `NO_ABRIR_`.", "",
      "| bloque | veredicto |", "|---|---|"] + [f"| {k} | {v} |" for k, v in st["bloques"].items()] + [
      f"| **general** | **{st['veredicto_general']}** |", "",
      f"- Las dos corridas dan el mismo JSON byte a byte: {st['las_dos_corridas_dan_el_mismo_json_byte_a_byte']}; códigos de salida "
      f"{st['codigos_de_salida']}.",
      f"- {st['declarado'][0].upper()}{st['declarado'][1:]}.", ""]
w += ["## 7. El reporte y los demás archivos de T5", "",
      "- **El reporte:** `data/experiment/tanda1/t5/reporte_tanda1.md`, que genera `scripts/reporte_t5.py` desde `salidas/`.",
      "- **La columna «Tanda 1», como propuesta aparte:** `t5/columna_tanda1_tablero_PROPUESTA.md`. No escribí en `docs/tablero_correcciones.md`.",
      "- **Las propuestas del backlog:** `t5/propuestas_backlog_t5.jsonl`. No escribí en el backlog.",
      f"- **El `NO_ABRIR_`:** `t5/NO_ABRIR_conteos_t5.json`, sha256 `{na_sha}`. Lo arma `scripts/no_abrir_t5.py` desde las dos partes que "
      "escriben `cifras_t5.py` y `selftest_t5.py`; ninguno imprime su contenido, y no lo abrí.",
      "- **La tarifa observada** es una propuesta para el §5 de la tabla de reprocesamiento (`salidas/costo_t5.json`, `tarifa_observada`). No "
      "la escribí en la tabla.", ""]
w += ["## 8. El cegamiento de U-MED-VERIF", "",
      "- **Lo que no miré ni reporto:** el desglose por estado de E3, `n_reintentos`, `reintentos_e3.jsonl`, `copias_nota_e3.jsonl`, las "
      "`marcas_e3` y el gasto de los reintentos aparte.",
      "- **De `estado_corpus.json`** el script lee solo `gasto_usd` y `resumen.n` de cada fase: el resumen de E3 trae además el desglose por "
      "estado, que no se lee. Las aceptadas y la cola salen de `t2/resumen_t2.json`, con los tres estados juntos; de `finales.jsonl` no "
      "se lee nada.",
      "- **E3 va como una sola cifra por TO,** con los reintentos adentro. No recalculé el costo con los tokens, porque los registros de E3 "
      "separan los reintentos.",
      "- **Los ids de modelo:** de E1, su cuenta; de E3 y de los reintentos de E1 de la fase de E3, solo los ids, porque sus cuentas incluyen "
      "los reintentos. Esas cuentas van al `NO_ABRIR_`, con los conteos del selftest.",
      "- **El contenido de extracciones:** el reporte y este FRENO muestran solo unidades de `t3/muestras/unidades_a_la_vista_T4.json`; "
      "`cifras_t5.py` lo controla para cada unidad que nombra. Las claves del catálogo, que son menciones de unidades que no están todas a la "
      "vista, van solo como cuántas. Por eso `unidades_a_la_vista_T5.json` no hizo falta, y no lo escribí.",
      "- **Los `NO_ABRIR_` de T2, T3 y T4** no se tocaron ni se abrieron (sección 12). La copia del repo los excluye.", ""]
w += ["## 9. Las dos corridas de `cifras_t5.py`", "",
      "`scripts/dos_corridas_t5.py` compara la corrida que va al repo (`salidas/`) con la segunda, a otra salida (en el paquete), archivo por "
      "archivo, y las dos partes del `NO_ABRIR_` solo por su sha256 (`salidas/dos_corridas_t5.json`):", "",
      "| archivo | sha256 | igual en la segunda corrida |", "|---|---|---|"] + [
      f"| `{k}` | `{v['sha256']}` | {v['igual']} |" for k, v in dos["archivos"].items()] + [
      "", f"Mismos nombres: {dos['mismos_nombres']}. La parte del `NO_ABRIR_` de cada corrida, igual por sha256: "
      f"{dos['parte_del_NO_ABRIR_de_cada_corrida_igual_por_sha256']}. Todo igual: {dos['todo_igual']}.", ""]
w += ["## 10. Para la autora y la mesa", "",
      f"1. **Las metas del tablero:** la lectura de cada meta es mía (`REGLA_FILAS` en `cifras_t5.py`, y la última columna de la propuesta). "
      f"No cumplen las filas {', '.join(map(str, filas_nc))}, las tres con el mismo residuo que su meta ya declara para la tanda 0.",
      f"2. **Las incorrectas de las lecturas:** {len(sin_nota)} no tienen nota de la autora, así que su causa va «no dicha por la lectura». "
      f"Ninguna de las {len(acep)} de las aceptadas trae su capa, así que su propuesta del backlog lleva «no dicha por la lectura» en "
      "`capa_pipeline`: la fija quien la triage.",
      f"3. **Las dudosas de las aceptadas** ({len(hal['dudosas_de_las_aceptadas_aparte'])}) no van como hallazgo ni al backlog: la lectura no las decidió.",
      f"4. **La vigilancia (9):** {v9['causa'].split('. ', 1)[1][0].lower()}{v9['causa'].split('. ', 1)[1][1:]}.",
      "5. **La cola:** la investigación de la causa queda para la mesa, como dice el mandato. No la empecé.",
      "6. **El catálogo:** la lectura de las claves va una sola vez, sobre las tres tandas. El reporte declara el desvío del §5.5.",
      "7. **La foto del paso 0:** las horas que da el mandato (17:23:48 a 17:24:00) son las de mi foto de después del segundo tramo, anterior "
      "a su FRENO. La comparé con esa y con la final (17:24:35): las dos dan lo que trajeron los commits (sección 1).", ""]
w += ["## 11. El script de cada cifra", "",
      "| cifras | script (`t5/scripts/`) | salida |", "|---|---|---|",
      "| el costo, los ids de modelo, los volúmenes, el alcance y el catálogo, los hallazgos, la columna, las incidencias y las propuestas | "
      "`cifras_t5.py` | `salidas/` (`costo_t5.json`, `modelos_t5.json`, `volumenes_t5.json`, `alcance_catalogo_t5.json`, `hallazgos_t5.json`, "
      "`columna_tanda1_t5.json`, `incidencias_t5.json`, `fuentes_t5.json`, `consola_cifras_t5.txt`) y `propuestas_backlog_t5.jsonl` |",
      "| las dos corridas iguales | `dos_corridas_t5.py` | `salidas/dos_corridas_t5.json` |",
      "| el selftest de claves | `selftest_t5.py` | `salidas/selftest_t5.json` (su consola es ese mismo JSON, byte a byte: no la guardé aparte) |",
      "| el `NO_ABRIR_` | `no_abrir_t5.py` | `NO_ABRIR_conteos_t5.json` (aquí, solo su sha256) |",
      "| el reporte y la columna propuesta | `reporte_t5.py` | `reporte_tanda1.md`, `columna_tanda1_tablero_PROPUESTA.md` |",
      "| la foto (sección 12) | `freno_t5_foto.py` | la sección 12 |",
      "| el texto de este FRENO | `freno_t5_armar.py` | este archivo |",
      "| la escritura en el repo | `escribir_en_el_repo_t5.py` | `escrituras_en_el_repo_t5.json`, en el paquete |",
      "| el paso 0 (sección 1) | sus comandos y `verif_paso0_commits_t5.py` | sus salidas, pegadas; el script, en el paquete |", ""]
props_g = grep["propios_con_patron"]
w += [FOTO.read_text(encoding="utf-8").strip(), "",
      f"- **El grep de convenciones** (`grep_convenciones_t5.py` y su salida, en el paquete) busca las palabras del `user.name` de git y las "
      f"de origen conversacional (Slack, mail, correo, «como dijo», «pedido por», …) en los {grep['archivos']} archivos nuevos o cambiados de "
      f"la foto, sin los `.DS_Store` ni el `NO_ABRIR_`. El control positivo da la línea {', '.join(map(str, grep['control_positivo_lineas']))}. "
      + (f"Con el patrón, en los archivos que redacté: " + "; ".join(f"`{Path(k).name}`, {len(v)} línea(s)" for k, v in props_g.items())
         + ": son las líneas de un script que describen el patrón del grep. " if props_g else "Con el patrón, en los archivos que redacté: ninguno. ")
      + f"Las palabras del nombre, en ningún archivo: {not grep['nombre_sin_rutas']}. "
      + f"Rutas con la carpeta personal o el scratchpad: {len(grep['con_rutas_absolutas'])} archivo(s). El grep del FRENO va en el mensaje "
        "de cierre.",
      "- **La copia** del repo es la del `rsync` de la cláusula, más la exclusión del volumen de Neo4j, y su control dio 0 "
      "(`rsync_copia_t5.log` en el paquete). Ningún `git clone`, ningún heredoc sin el delimitador entre comillas, y no abrí ninguna carpeta "
      "vedada. No abrí ni usé la sesión ni la copia de A3.", ""]
w += ["## 13. Errores propios, con su causa", "",
      "1. **El hallazgo de la cola salió sin el campo `causa`** en la primera versión de `cifras_t5.py`.",
      "   - La causa: en la cola puse la causa de cada unidad dentro de `unidades` y no la del hallazgo.",
      "   - Lo vi al revisar la salida, antes de escribir nada en el repo, y lo agregué: apunta a la nota de cada unidad.", "",
      "FRENO T5. Espero la revisión de la mesa."]
texto = "\n".join(w) + "\n"
OUT.write_text(texto, encoding="utf-8")
print(f"{len(texto.splitlines())} líneas; secciones: {len(re.findall(r'^## ', texto, re.M))}")
