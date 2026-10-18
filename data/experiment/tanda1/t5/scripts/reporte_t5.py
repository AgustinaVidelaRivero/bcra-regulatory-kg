"""B6.1, tanda 1, T5, punto 8: el reporte de cierre (t5/reporte_tanda1.md) y la columna «Tanda 1» como propuesta aparte
(t5/columna_tanda1_tablero_PROPUESTA.md), por script, desde las salidas de cifras_t5.py y selftest_t5.py (t5/salidas/), las propuestas
del backlog (t5/propuestas_backlog_t5.jsonl) y la tabla 1 de t4/tablas_t4_tramo2.md, tal cual. Las cifras se copian de su salida; el
texto fijo no lleva cifras propias. Solo lee; escribe los dos .md bajo <raíz> y no imprime su contenido.
Uso: python3 -I -B reporte_t5.py <raíz>
"""
import hashlib
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
RAIZ = Path(sys.argv[1]).resolve()
T1 = RAIZ / "data/experiment/tanda1"
T5 = T1 / "t5"
S = T5 / "salidas"
L = lambda n: json.loads((S / n).read_text(encoding="utf-8"))  # noqa: E731
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()  # noqa: E731
co = lambda x, k=4: "—" if x is None else f"{x:.{k}f}".replace(".", ",")  # noqa: E731
mil = lambda n: f"{n:,}".replace(",", ".")  # noqa: E731
iv = lambda w: f"[{co(w[0])}; {co(w[1])}]"  # noqa: E731
costo, mod, vol, alc, hal = L("costo_t5.json"), L("modelos_t5.json"), L("volumenes_t5.json"), L("alcance_catalogo_t5.json"), L("hallazgos_t5.json")
inc, col, st, fu = L("incidencias_t5.json"), L("columna_tanda1_t5.json"), L("selftest_t5.json"), L("fuentes_t5.json")
props = [json.loads(x) for x in (T5 / "propuestas_backlog_t5.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
tas = json.loads((T1 / "t4/tasas/tasas_t4_tramo2.json").read_text(encoding="utf-8"))
tab4 = (T1 / "t4/tablas_t4_tramo2.md").read_text(encoding="utf-8")
tabla1 = re.search(r"#### Tabla 1\..*?(?=\n#### Tabla 2\.)", tab4, re.S).group(0).rstrip()
SALIDA = lambda n: f"`t5/salidas/{n}`"  # noqa: E731
R, E = costo["real"], costo["estimado"]
w = ["# Reporte de cierre de la tanda 1 de B6.1", "",
     "Pre-registro firmado (`docs/preregistro_tanda1.md`, firma en `95b18217`, con su nota al pie en `ca5b39fd`): §3 («Al cerrar»), §5.5,",
     "§5.6 y el §6 donde se cita. USD 0, sin API. Lo genera `t5/scripts/reporte_t5.py` desde las salidas de `t5/scripts/cifras_t5.py` y",
     "`t5/scripts/selftest_t5.py`; cada cifra va con la salida de la que se copia. Las aclaraciones que no son cifras de una salida son de",
     "la ejecutora de T5 y lo dicen.", ""]

# 1. volúmenes
u = vol["unidades"]
w += ["## 1. Los volúmenes", "", f"De {SALIDA('volumenes_t5.json')} (de `t2/resumen_t2.json` y `t3/salidas/doble_corrida_t3.json`).", "",
      "| unidades | con las partes por corte | aceptadas (los tres estados juntos) | cola | errores | ids repetidos |",
      "|---:|---:|---:|---:|---:|---:|",
      f"| {mil(u['unidades'])} | {mil(u['unidades_con_partes'])} | {mil(u['aceptadas'])} | {u['cola']} | {u['errores']} | {u['ids_repetidos']} |", "",
      "| grafo | unidades de E0 | nodos | aristas | sha256 del `kg.json` |", "|---|---:|---:|---:|---|"]
for n, g in vol["grafos"].items():
    w.append(f"| {n} | {mil(g['unidades_e0'])} | {mil(g['nodos'])} | {mil(g['aristas'])} | `{g['kg_sha256'][:16]}…` |")
w += ["", "| TO | unidades | con partes | aceptadas | cola | errores |", "|---|---:|---:|---:|---:|---:|"]
for to, x in vol["por_to"].items():
    w.append(f"| {to} | {x['unidades']} | {x['unidades_con_partes']} | {x['aceptadas']} | {x['cola']} | {x['errores']} |")

# 2. costo
dv = costo["desviacion"]
w += ["", "## 2. El costo real contra el estimado (§3, «Al cerrar»)", "", f"De {SALIDA('costo_t5.json')}. {costo['como'][0].upper()}{costo['como'][1:]}.", "",
      "| etapa | real USD | estimado con la tarifa | razón | estimado del manifiesto | razón |", "|---|---:|---:|---:|---:|---:|"]
for e, n in (("e1", "E1"), ("e3", "E3 (con los reintentos adentro)")):
    a, b = dv["por_etapa_contra_la_tarifa"][e], dv["por_etapa_contra_el_manifiesto"][e]
    w.append(f"| {n} | {co(a['real'], 6)} | {co(a['estimado'], 6)} | {co(a['razon'])} | {co(b['estimado'], 6)} | {co(b['razon'])} |")
t = dv["total"]
w.append(f"| total | {co(t['real'], 6)} | {co(t['estimado'], 6)} | {co(t['razon'])} | {co(t['estimado'], 6)} | {co(t['razon'])} |")
w += ["", f"- **Contra el tope:** {co(R['total'], 6)} de {co(R['tope_usd'])} ({co(R['fraccion_del_tope'])}). `presupuesto_compartido.json` da "
      f"{co(R['presupuesto_compartido_gasto_usd'], 6)}; la suma de las {R['fases_cerradas']} fases menos ese valor, {co(R['suma_de_las_fases_menos_presupuesto_compartido'], 6)}.",
      f"- **Las líneas de alcance** en E1: USD {co(E['lineas_de_alcance_total_usd'], 6)}, repartidas por TO así: " +
      ", ".join(f"{k} {co(v, 6)}" for k, v in E["lineas_de_alcance_por_to"].items()) + f" ({E['lineas_de_alcance_como']}).",
      f"- **La desviación**, por etapa, por TO y total, va a: {dv['va_a']}.",
      f"- **La tarifa observada** (U = {mil(costo['tarifa_observada']['U'])}): E1 {co(costo['tarifa_observada']['e1_por_unidad'], 6)}, E3 "
      f"{co(costo['tarifa_observada']['e3_por_unidad'], 6)}, juntas {co(costo['tarifa_observada']['total_por_unidad'], 6)}, contra la de "
      f"referencia {co(costo['tarifa_observada']['tarifa_de_referencia']['e1'], 6)}, {co(costo['tarifa_observada']['tarifa_de_referencia']['e3'], 6)} y "
      f"{co(costo['tarifa_observada']['tarifa_de_referencia']['total'], 6)}. Es {costo['tarifa_observada']['es']}.",
      f"- **Para el pre-registro de la tanda final** (`para_el_preregistro_tanda_final`): «{costo['para_el_preregistro_tanda_final']}».",
      "- **Los pasos sin API, en 0:** " + "; ".join(costo["pasos_sin_api_en_0"]) + ".", "",
      "| TO | U | E1 real | E3 real | total real | estimado del manifiesto | razón | estimado con la tarifa | razón |",
      "|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
for to, x in costo["por_to"].items():
    m, p = x["contra_el_manifiesto"], x["contra_la_tarifa"]
    w.append(f"| {to} | {x['unidades']} | {co(m['e1']['real'], 6)} | {co(m['e3']['real'], 6)} | {co(m['total']['real'], 6)} | "
             f"{co(m['total']['estimado'], 6)} | {co(m['total']['razon'])} | {co(p['total']['estimado'], 6)} | {co(p['total']['razon'])} |")

# 3. modelos
c = mod["contra_el_codigo_y_el_preregistro"]
f2 = mod["contra_el_freno_por_modelo_de_T2"]
w += ["", "## 3. Los ids de modelo que devolvió la API (§2 y §5.6)", "", f"De {SALIDA('modelos_t5.json')}. Fuente: {mod['fuente']}.", "",
      "| etapa | ids | respuestas distintas | esperado | igual |", "|---|---|---|---|---|",
      f"| E1 | {', '.join(mod['e1']['ids'])} | " + ", ".join(f"{k} {mil(v)}" for k, v in mod["e1"]["respuestas_distintas_por_id"].items()) +
      f" | {c['e1']['esperado']} | {c['e1']['igual']} |",
      f"| reintentos de E1 de la fase de E3 | {', '.join(mod['e1_reintentos_de_la_fase_e3']['ids'])} | {mod['e1_reintentos_de_la_fase_e3']['cuentas']} | "
      f"{c['e1']['esperado']} | {c['e1']['igual']} |",
      f"| E3 | {', '.join(mod['e3']['ids'])} | {mod['e3']['cuentas']} | {c['e3']['esperado']} | {c['e3']['igual']} |", "",
      f"- Lo que cuenta la columna de E1: {mod['e1']['que_cuenta']}.",
      f"- {mod['contra_el_manifiesto'][0].upper()}{mod['contra_el_manifiesto'][1:]}.",
      f"- El freno por modelo de T2: {f2['eventos']} eventos en `avance_t2.jsonl`, con {', '.join(f2['resultados'])}; ids de E1 "
      f"{', '.join(f2['ids_e1'])} y de E3 {', '.join(f2['ids_e3'])}; iguales a los de las bases: {f2['igual']}.",
      f"- Fuentes del esperado: E1, {c['e1']['fuente']}; E3, {c['e3']['fuente']}."]

# 4. incidencias
w += ["", "## 4. Las incidencias", "", f"De {SALIDA('incidencias_t5.json')} ({inc['fuente']}).", "",
      "| lanzamiento de T2 | inicio | fin | pid | paradas |", "|---:|---|---|---:|---|"]
for i, x in enumerate(inc["lanzamientos_de_T2"], start=1):
    w.append(f"| {i} | {x['inicio']} | {x.get('fin', '—')} | {x['pid']} | " + ("; ".join(f"{p['ts']}: {p['motivo']}" for p in x["paradas"]) or "ninguna") + " |")
w += ["", "Los frenos por proyección del runner, tal cual: " + "; ".join(f"[{x['to']}] {x['linea']}" for x in inc["frenos_del_runner"]) + ".",
      f"Entre los lanzamientos: {inc['decisiones_entre_lanzamientos']}.", "",
      "Mis aclaraciones, con su ancla y sin cifras:",
      "- **T3:** el gate pasa con las decisiones de la autora sobre su FRENO parcial (registro de decisiones, §29, puntos 1 a 7: la E0 con las partes "
      "por corte para S31; la suite sobre el acumulado, con lo «fuera del grafo» aparte; E4-a1 y E4-a4 declaradas; los `nombres_remision` de "
      "la regla v2; la fixture; las salidas de shapes y de la suite donde están; el clon declarado).",
      "- **Las regresiones declaradas de T3:** E4-a1 y E4-a4, que se declaran y se difieren (opción (ii), registro, §29; BKL-0048). Van como "
      "hallazgos en la sección 8.",
      "- **La regla de las dudosas** (registro de decisiones, §35): en la cola y en las dos de las aceptadas, una «dudosa» cuenta como error "
      "para la tasa, la atención y el freno; la cuenta sin ellas va al lado como sensibilidad y no decide.",
      f"- **La regla del 25 % de la cola** " + ("se disparó" if tas["cola"]["regla"]["regla_del_25_se_dispara"] else "no se disparó") +
      ": la tabla 1 de la sección 5 trae su cifra. La investigación de su causa la diseña la mesa (sección 9)."]

# 5. tasas de T4
w += ["", "## 5. Las tasas de T4", "", "La tabla 1 de `t4/tablas_t4_tramo2.md`, que genera `t4/scripts/tablas_t4t2.py` desde "
      f"`t4/tasas/tasas_t4_tramo2.json` (sha256 `{sha(T1 / 't4/tasas/tasas_t4_tramo2.json')}`), tal cual. Sus rutas son relativas a "
      "`data/experiment/tanda1/t4/`.", "", tabla1]

# 6. la columna del tablero
w += ["", "## 6. La columna «Tanda 1» del tablero de correcciones (§5.2)", "",
      f"De {SALIDA('columna_tanda1_t5.json')}: las celdas de T3, tal cual, y la que esperaba a T4 (la fila 59). La misma tabla va como "
      "propuesta aparte en `t5/columna_tanda1_tablero_PROPUESTA.md`; el tablero del repo no se toca.", "",
      "| fila | síntoma | Tanda 1 | ancla |", "|---:|---|---|---|"]
for x in col:
    w.append(f"| {x['fila']} | {x['sintoma']} | {x['tanda_1']} | {x['ancla']} |")

# 7. alcance y catálogo
v = alc["versiones_del_catalogo"]
lo = v["lo_que_resolvio_en_el_evaluado"]
w += ["", "## 7. El alcance y el catálogo al cierre (§5.5)", "", f"De {SALIDA('alcance_catalogo_t5.json')}, desde `t3/conteos_sin_leer/contado_sin_leer_t3f.json`.", "",
      "| registro | filas | en cuarentena | verificadas en cuarentena | claves | con 2 unidades o más | con 3 o más | en 2 TOs o más |",
      "|---|---:|---:|---:|---:|---:|---:|---:|"]
for g, x in alc["catalogo_al_cierre"].items():
    w.append(f"| {g} | {mil(x['filas_registro'])} | {x['cuarentena']} | {x['verificadas_en_cuarentena']} | {x['claves']} | "
             f"{x['n_claves_con_2_unidades_o_mas']} | {x['claves_con_3_unidades_o_mas']} | {x['claves_en_2_tos_o_mas']} |")
w += ["", f"- **El umbral:** {alc['umbral']}. Las claves: {alc['las_claves']}.",
      f"- **Desvío del §5.5, declarado:** el catálogo no crece en la tanda 1; {alc['el_catalogo_no_crece_en_la_tanda_1']}.",
      f"- **Cuántas relaciones resolvió cada versión del catálogo:** hubo {v['cuantas']}, {v['cual']}. En el evaluado, E1 dio "
      f"{mil(lo['relaciones_con_sujeto_id_de_E1'])} relaciones con `sujeto_id` y {lo['relaciones_con_sujeto_propuesto']} con `sujeto_propuesto`; el "
      f"registro de no mapeados tiene {lo['registro_de_no_mapeados']} filas (" + ", ".join(f"{k} {vv}" for k, vv in lo["registro_por_estado"].items()) +
      f"). Fuente: {v['fuente']}. {v['sin_re_resolucion'][0].upper()}{v['sin_re_resolucion'][1:]}.",
      f"- **El ensamblado de la tanda 1 corrió sin catálogo de resolución:** {v['el_ensamblado_de_la_tanda_1_sin_catalogo_de_resolucion']} (ningún "
      "script de `t3/scripts/` lo nombra).",
      f"- **El alcance que leyó E1:** `{alc['alcance_que_leyo_E1']['derivado']}`, `{alc['alcance_que_leyo_E1']['sha256'][:16]}…`, igual al sello "
      f"del manifiesto: {alc['alcance_que_leyo_E1']['igual_al_sello_del_manifiesto']}. Las líneas de alcance: "
      f"{mil(alc['alcance_que_leyo_E1']['lineas_de_alcance']['unidades'])} unidades, {mil(alc['alcance_que_leyo_E1']['lineas_de_alcance']['tokens'])} "
      f"tokens, USD {co(alc['alcance_que_leyo_E1']['lineas_de_alcance']['usd'], 6)}."]

# 8. hallazgos
H = hal["hallazgos"]
qual = lambda h: h.get("unidad") or h.get("item") or h.get("vigilancia") or (f"fila {h['fila_tablero']}" if "fila_tablero" in h else h.get("muestra"))  # noqa: E731
w += ["", "## 8. Los hallazgos, en los ejes A y B (§5.6; protocolo entre tandas, `:71-100`)", "",
      f"De {SALIDA('hallazgos_t5.json')}. Cuántos: " + "; ".join(f"{k}, {n}" for k, n in hal["cuantos"].items()) + ". Propuestas del backlog: "
      f"{hal['propuestas_del_backlog']}, en `t5/propuestas_backlog_t5.jsonl` (no se escriben en el backlog).", "",
      "| id | tipo | qué | cifra o veredicto | capa_pipeline | eje A | eje B | backlog |", "|---|---|---|---|---|---|---|---|"]
for h in H:
    a = h["eje_A"]
    ea = " ".join(x for x in (a.get("fila"), a.get("clase")) if x) or "sin fila"
    w.append(f"| {h['id']} | {h['tipo']} | {h.get('muestra', '') + ': ' if 'unidad' in h else ''}`{qual(h)}` | "
             f"{h.get('veredicto_autora') or h.get('cifra') or h.get('medido', '')} | {h['capa_pipeline']} | {ea}: {a['por_que']} | {h['eje_B']} | {h['backlog']} |")
w += ["", "**La causa de cada hallazgo**, tal cual (la de las lecturas es la nota de la autora; sin nota, «causa: no dicha por la lectura»):", ""]
for h in H:
    w.append(f"- **{h['id']}** (`{qual(h)}`): {h['causa']}")
    for x in h.get("unidades", []):
        w.append(f"  - `{x['unidad']}` ({x['celda']}, {x['veredicto_autora']}): {x['causa']}")
w += ["", f"**Las dudosas de las aceptadas, aparte** ({len(hal['dudosas_de_las_aceptadas_aparte'])}): {hal['dudosas_como']}.", ""]
for x in hal["dudosas_de_las_aceptadas_aparte"]:
    w.append(f"- `{x['unidad']}` ({x['muestra']}, {x['celda']}; propuesta {x['propuesta']}): {x['causa']}")
ns = hal["no_son_hallazgo_por_las_reglas"]
vs = ns["vigilancias_sin_linea_de_base_comparable"]
w += ["", "**Lo que no es hallazgo por estas reglas:**",
      f"- las vigilancias (1), (2), (3) y (7): " + "; ".join(f"{k} " + ", ".join(f"{r} {n}" for r, n in vs[k].items()) for k in ("(1)", "(2)", "(3)", "(7)")) +
      f" ({vs['por_que']});",
      f"- la vigilancia (4): un TextoOrdenado por TO, {ns['vigilancia_4']}; las aceptadas: {ns['aceptadas']};",
      "- las filas del tablero, por la lectura de su meta (mía, en `REGLA_FILAS` de `cifras_t5.py`): " +
      "; ".join(f"{k} {vv}" for k, vv in ns["filas_del_tablero"].items()) + "."]

# 9. lo que sigue
v3, v2, v7 = (tas["vigilancias"][k] for k in ("vigilancia:3", "vigilancia:2", "vigilancia:7"))
w += ["", "## 9. Lo que sigue, sin hacerlo en T5", "",
      "1. **La investigación de la causa de la cola,** antes de la tanda final y sin cambiar el grafo sin cola (pre-registro, `95b18217:634-635`). "
      "La diseña la mesa.",
      f"2. **La vigilancia (3),** con {v3['cruda']['k']} duplicaciones de {v3['cruda']['n']}, y la unión de nodos que esperaba a su resultado "
      "(registro de decisiones, §32: «Unir nodos con los de la unidad de origen espera a lo que encuentre la (3). Sacarlos, no.»).",
      f"3. **La vigilancia (2),** con {v2['cruda']['k']} vaciamientos de {v2['cruda']['n']}, y la (7), con {v7['cruda']['k']} sin apoyo de "
      f"{v7['cruda']['n']}.",
      "4. **El conteo de `cid`** (pre-registro, §6.9) y **las FICHAS** de U-MED-VERIF, que van después del commit de T5.", "",
      "## 10. Las fuentes que leyó `cifras_t5.py`", "", f"De {SALIDA('fuentes_t5.json')}, con el sha256 de cada una en la copia.", "",
      "| archivo | sha256 |", "|---|---|"] + [f"| `{k}` | `{vv}` |" for k, vv in fu.items()]
w += ["", "## 11. El selftest de claves", "", f"De {SALIDA('selftest_t5.json')}: veredicto general {st['veredicto_general']}; "
      + "; ".join(f"{k}: {vv}" for k, vv in st["bloques"].items()) + f". Las dos corridas, iguales: {st['las_dos_corridas_dan_el_mismo_json_byte_a_byte']}. "
      f"{st['declarado'][0].upper()}{st['declarado'][1:]}. Los conteos, en `t5/NO_ABRIR_conteos_t5.json`."]
(T5 / "reporte_tanda1.md").write_text("\n".join(w) + "\n", encoding="utf-8")

# la columna, como propuesta aparte
p = ["# La columna «Tanda 1» del tablero de correcciones — PROPUESTA", "",
     "B6.1, tanda 1, T5 (pre-registro firmado, §5.2). Generada por `t5/scripts/reporte_t5.py` desde `t5/salidas/columna_tanda1_t5.json`:",
     "las celdas de T3 (`t3/conteos_sin_leer/columna_tanda1_tablero_t3f.md`), tal cual, y la de la fila 59, que esperaba a T4. Es una",
     "propuesta: `docs/tablero_correcciones.md` no se toca. La última columna es mi lectura de la meta de cada fila, que decide si es un",
     "hallazgo (reporte, sección 8).", "",
     "| fila | síntoma | Tanda 1 | ancla | lectura de la meta (mía) |", "|---:|---|---|---|---|"]
for x in col:
    p.append(f"| {x['fila']} | {x['sintoma']} | {x['tanda_1']} | {x['ancla']} | {x['lectura_de_la_meta']['estado']}: {x['lectura_de_la_meta']['por_que']} |")
(T5 / "columna_tanda1_tablero_PROPUESTA.md").write_text("\n".join(p) + "\n", encoding="utf-8")
print("reporte_tanda1.md:", sha(T5 / "reporte_tanda1.md"), len(w), "líneas")
print("columna_tanda1_tablero_PROPUESTA.md:", sha(T5 / "columna_tanda1_tablero_PROPUESTA.md"), len(p), "líneas")
