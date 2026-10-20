"""B6.1, tanda final, T3, punto 4: la tabla del veredicto del gate, por script, con data/experiment/tanda1/t3/scripts/veredicto_gate_t3f.py
como modelo y las decisiones del gate de la tanda 1 que siguen (registro de decisiones, §29; pre-registro de la tanda final, §7):
  - shapes: rige la corrida con la E0 con las partes por corte; la de la E0 de cada grafo se informa;
  - la suite se juzga sobre el acumulado; en el grafo de la tanda y en los del tramo 1, lo «fuera del grafo» se informa aparte y no
    cuenta; E4-a1 y E4-a4, declaradas (BKL-0048), y RT-C5-3, RT-C6-1 y RT-C6-2, las del laudo;
  - la doble corrida de los ocho y la reproducibilidad de los diez sellados (doble_corrida_tf.json), los selftests de la cadena y el de
    claves sin las cuentas (selftest_claves_sin_cuentas_tf.py);
  - informativos: las intrínsecas de generación 3 con la E0 con las partes, los contadores de E1, la causa de S31 con la E0 de cada grafo
    y los `nombres_remision` medidos.
El gate pasa si en los ocho grafos las bloqueantes de shapes pasan con la E0 con las partes, si la suite da 0 regresiones no declaradas
que cuenten, si la doble corrida y la reproducibilidad dieron OK, si la fixture solo suma las ocho entradas y si los selftests dieron
rc=0 y el de claves, OK. El de claves se juzga sin la R23 del perfil r2b y la V23 del sellado, declaradas no aplicables después de T2
(decisión de la autora sobre el FRENO T3 parcial: su TO ya se extrajo y su clave está en la caché, no por el código de la clave): pasa si
todo lo demás es igual a A3 sin cuentas, es decir, si todos los campos que difieren son de R23 o derivan de ella y la fila del contraste
que difiere es la de R23 (diagnostico_clave_cache_tf.json). Solo lee los archivos de <gate_decisiones> y <salidas>; escribe veredicto_gate_tf.{json,md} en <gate_decisiones>.
Uso: python3 -I -B veredicto_gate_tf.py <t3> (la carpeta data/experiment/tanda_final/t3 de la copia)
"""
import json
import sys
from pathlib import Path

T3 = Path(sys.argv[1]).resolve()
GD, SAL = T3 / "gate_decisiones", T3 / "salidas"
L = lambda p: json.loads(Path(p).read_text(encoding="utf-8"))  # noqa: E731
NOMBRE = {"tf98": "KG-TandaFinal-r2b", "tf98_sincola": "KG-TandaFinal-r2b-sincola", "tf_tramo1": "KG-TandaFinal-Tramo1-r2b",
          "tf_tramo1_sincola": "KG-TandaFinal-Tramo1-r2b-sincola", "acum128": "KG-Acumulado-Tandas0y1yFinal-r2b",
          "acum128_sincola": "KG-Acumulado-Tandas0y1yFinal-r2b-sincola", "acum60": "KG-Acumulado-Tandas0y1yTramo1-r2b",
          "acum60_sincola": "KG-Acumulado-Tandas0y1yTramo1-r2b-sincola"}
tg = L(GD / "tablas_gate_tf.json")
ep = L(GD / "e0_partes_tf.json")
fg = L(GD / "fuera_del_grafo_tf.json")
cs = L(GD / "causa_s31_tf.json")
cf = L(GD / "control_fixture_tf.json")
dc = L(SAL / "doble_corrida_tf.json")
ce = L(SAL / "contadores_e1_tf.json")
nr = L(T3 / "nombres_remision/tabla_nombres_t3_tf.json")
sc = L(T3 / "selftests/clave_cache/resumen_sin_cuentas_t3.json")
dg = L(GD / "diagnostico_clave_cache_tf.json") if (GD / "diagnostico_clave_cache_tf.json").exists() else None
w, v = [], {"grafos": {}}
w.append("#### Tabla V0. La E0 con las partes por corte (`gate_decisiones/e0_partes_tf.json`)\n")
w.append("| E0 | archivos | dos corridas iguales | unidades reemplazadas por sus partes | sha256 del conjunto |")
w.append("|---|---:|---|---:|---|")
for n, e in ep["e0_con_partes"].items():
    w.append(f"| {n} | {e['corridas'][0]['archivos']} | {e['iguales']} | {e['unidades_reemplazadas']} | `{e['sha256_conjunto']}` |")
c = ep["controles"]
w.append(f"\nControles: la de la tanda final es la E0 del repo: {c['tanda_final_igual_a_la_e0_del_repo']}; en los acumulados, los archivos "
         "de las tandas 0 y 1 son los de la E0 con las partes del acumulado de la tanda 1 y los de la tanda final, los de la suya: "
         + "; ".join(f"{n} {c[n]['archivos_de_las_tandas_0_y_1']} y {c[n]['archivos_de_la_tanda_final']} archivos, "
                     f"{c[n]['iguales_a_la_tanda_1'] and c[n]['iguales_a_la_tanda_final']}" for n in ("acum128", "acum60")) + ".")
w.append("\n#### Tabla V1. El veredicto del gate por grafo\n")
w.append("| grafo | shapes, E0 con las partes (rige) | shapes, E0 del grafo (informada) | suite: resuelto / persiste / no aplica | "
         "regresiones | declaradas (laudo) | declaradas (§29) | fuera del grafo | no declaradas que cuentan |")
w.append("|---|---|---|---|---:|---:|---:|---:|---|")
fr = lambda s: f"{s['veredicto']} ({s['por_resultado']['PASS']} / {s['por_resultado']['FAIL']} / {s['por_resultado']['WARN']}" + (  # noqa: E731
    f"; bloqueantes en FAIL: {', '.join(s['bloqueantes_en_fail'])})" if s["bloqueantes_en_fail"] else ")")
for g in NOMBRE:
    rige = tg["extra"][f"{g}_con_partes"]
    repo = tg["grafos"][g]["nuevo"]["shapes"]
    f = fg["grafos"][g]
    r = f["resumen_suite"]
    pr = f["por_regresion"]
    laudo = sorted(i for i, x in pr.items() if x["clase"] == "declarada (laudo)")
    autora = sorted(i for i, x in pr.items() if x["clase"] == "declarada (autora, §29)")
    fuera = sorted(i for i, x in pr.items() if x["fuera_del_grafo"])
    cuentan = f["no_declaradas_que_cuentan"]
    v["grafos"][g] = {"nombre": NOMBRE[g],
                      "shapes_rige": {k: rige[k] for k in ("veredicto", "por_resultado", "bloqueantes_en_fail", "no_pass")},
                      "shapes_e0_del_grafo": {k: repo[k] for k in ("veredicto", "por_resultado", "bloqueantes_en_fail", "no_pass")},
                      "suite": {"resumen": r, "entrada": f["entrada"], "regresiones": f["regresiones"], "declaradas_laudo": laudo,
                                "declaradas_autora": autora, "fuera_del_grafo": fuera, "no_declaradas_que_cuentan": cuentan},
                      "pasa": rige["veredicto"] == "PASA" and not rige["bloqueantes_en_fail"] and not cuentan}
    w.append(f"| {NOMBRE[g]} | {fr(rige)} | {fr(repo)} | {r['resuelto']} / {r['persiste']} / {r['no_aplicable']} | {f['regresiones']} | "
             f"{len(laudo)} | {len(autora)} | {len(fuera) if f['tanda_sola'] else '— (no se aplica)'} | {', '.join(cuentan) or '0'} |")
w.append("\nLas columnas de shapes dan PASS / FAIL / WARN; los FAIL que no bloquean, por grafo, están en `tablas_gate_tf.json` (`no_pass`). "
         "«Fuera del grafo» cuenta las regresiones con todas sus anclas en TOs que el grafo no tiene; en los acumulados no se aplica (§29). "
         "La entrada de la fixture contra la que se mide cada grafo es la suya (las ocho nuevas heredan las expectativas de la tanda 1).")
for g, x in fg["cruce"].items():
    f = fg["grafos"][g]
    w.append(f"- **{NOMBRE[g]}, «fuera del grafo»:** {len(f['regresiones_fuera_del_grafo'])} regresiones; de los "
             f"{sum(f['items_por_alcance'].values())} ítems, {f['items_por_alcance']['fuera del grafo']} fuera del grafo, "
             f"{f['items_por_alcance']['general']} generales y {f['items_por_alcance']['en el grafo']} en el grafo. Cruce con {x['acumulado']}: "
             f"{x['cuantos'][0]} y {x['cuantos'][1]} ítems, iguales: {x['iguales']}.")
w.append("\n#### Tabla V2. S31 con la E0 de cada grafo: la causa, por id (`gate_decisiones/causa_s31_tf.json`)\n")
w.append("| grafo | `remite_a` | con su chunk fuera de la E0 del grafo | todos son partes por corte |")
w.append("|---|---:|---:|---|")
for g, x in cs.items():
    w.append(f"| {NOMBRE[g]} | {x['remite_a']} | {x['con_chunk_de_procedencia_fuera_de_la_e0']} | {x['todos_son_partes_por_corte']} |")
rep_ok = dc["ok"]
st = {}
for p in sorted((T3 / "selftests").glob("*.txt")):
    if p.stem == "fin":
        continue
    t = p.read_text(encoding="utf-8", errors="replace").splitlines()
    st[p.stem] = next((x for x in t if x.startswith("rc=")), "sin rc")
st_ok = bool(st) and all(r == "rc=0" for r in st.values())
cc = sc.get("veredicto_del_selftest")
cc_igual_a_a3 = cc == "OK" and sc["json_igual_al_de_a3_sin_cuentas"] and sc["consola_igual_a_la_de_a3_sin_cuentas"]
cc_sin_r23 = bool(dg) and dg["todas_en_la_variacion_del_TO_nuevo_o_derivadas"] and dg["la_fila_que_difiere_es_la_de_R23"] \
    and dg["el_TO_esta_en_la_tanda_final"] and dg["chunk_igual_en_las_dos"]
cc_ok = cc_igual_a_a3 or cc_sin_r23
w.append("\n#### Tabla V3. La doble corrida, la reproducibilidad, la fixture, los selftests y lo informativo\n")
w.append(f"- **La doble corrida** de los ocho: {all(x['kg_sha256'][0] == x['kg_sha256'][1] for x in dc['doble_corrida'].values())}; "
         f"**la reproducibilidad**: {len(dc['cadenas'])} cadenas, todas iguales a su sello: {all(c['igual'] for c in dc['cadenas'])}; "
         f"veredicto {'OK' if rep_ok else 'CON FALLAS'} (`salidas/doble_corrida_tf.json`).")
w.append(f"- **La fixture** (`gate_decisiones/control_fixture_tf.json`): {cf['claves_de_HEAD']} claves de HEAD, {cf['quitadas']} quitadas y "
         f"{cf['cambiadas']} cambiadas; {cf['claves_nuevas']} claves nuevas, todas de las ocho entradas nuevas: {cf['son_las_ocho']}; "
         f"veredicto {'OK' if cf['ok'] else 'CON FALLAS'}.")
w.append(f"- **Los selftests:** {', '.join(f'{k} {r}' for k, r in st.items())}. **El de claves**, sin las cuentas: {cc}; sus dos salidas sin "
         f"cuentas, byte a byte las de A3: {sc['json_igual_al_de_a3_sin_cuentas']} y {sc['consola_igual_a_la_de_a3_sin_cuentas']}.")
if dg and not cc_igual_a_a3:
    filas_dif = ", ".join(f"{k}: {v['fila']} ({v['variacion']})" for k, v in dg["filas_de_la_tabla_que_difieren"].items())
    w.append(f"  - **La causa del de claves** (`gate_decisiones/diagnostico_clave_cache_tf.json`, sin abrir sus salidas): los "
             f"{len(dg['rutas_que_difieren_de_A3_sin_cuentas'])} campos que difieren de A3 sin cuentas son de la variación del TO nuevo "
             f"(`{', '.join(dg['funciones_con_clave_en_cache_e1'])}`, R23 en el perfil r2b) o derivan de ella: "
             f"{dg['todas_en_la_variacion_del_TO_nuevo_o_derivadas']}. Supone que `{dg['UNIDAD_TO_NUEVO']}` no está en la caché de E1; "
             f"`{dg['TO_NUEVO']}` es de la tanda final ({dg['lugar_en_orden_corrida']}.º de `orden_corrida`, tramo {dg['tramo']}) y su chunk "
             f"es el mismo en la E0 de la tanda final y en b584: {dg['chunk_igual_en_las_dos']}. La fila del contraste que difiere, "
             f"{filas_dif}, es la de R23: "
             f"{dg['la_fila_que_difiere_es_la_de_R23']}. {dg['lectura']}")
    w.append(f"  - **Declaradas no aplicables después de T2** (decisión de la autora sobre el FRENO T3 parcial): la R23 del perfil r2b y la "
             f"V23 del sellado. Sin ellas, todo lo demás del selftest es igual a A3 sin cuentas: {cc_sin_r23}. El selftest no se tocó; el "
             f"cambio de su TO lo hace la mesa aparte.")
w.append("- **Las intrínsecas de generación 3, con la E0 con las partes (informativas):**")
intr = {}
for g, n in NOMBRE.items():
    m = L(T3 / f"intrinsecas_gen3/con_partes/{n}.json")["metricas"]
    m10 = m["M10_chunks_mudos"]
    intr[g] = {"M4": m["M4_average_degree"]["valor"], "M9_aislados": m["M9_nodos_aislados_y_componentes"]["valor"]["nodos_aislados"],
               "M10": [m10["numerador"], m10["denominador"]]}
    w.append(f"  - {n}: M4 {intr[g]['M4']}, M9 {intr[g]['M9_aislados']} nodos aislados, M10 {m10['numerador']} / {m10['denominador']}.")
w.append(f"- **Los contadores de E1 (informativos):** {ce['total']}.")
w.append("- **Los `nombres_remision` medidos** (`nombres_remision/tabla_nombres_t3_tf.json`): iguales a la medición de la mesa en los cuatro "
         f"ensamblados: {nr['todas_iguales_a_la_mesa']}; la variante en cada manifiesto sigue la §19: "
         + "; ".join(f"{x['grafo'].split(' ')[0]} {x['manifiesto_sigue_la_19']}" for x in nr["filas"].values()) + ".")
v.update({"reproducibilidad_ok": rep_ok, "fixture_ok": cf["ok"], "selftests": st, "selftests_ok": st_ok, "clave_cache": cc,
          "clave_cache_ok": cc_ok, "clave_cache_igual_a_A3": cc_igual_a_a3, "clave_cache_sin_R23_y_V23": cc_sin_r23, "intrinsecas_con_partes": intr, "contadores_e1": ce["total"],
          "e0_con_partes_ok": ep["ok"], "nombres_remision_iguales_a_la_mesa": nr["todas_iguales_a_la_mesa"],
          "clave_cache_diagnostico": dg})
v["gate_pasa"] = (all(x["pasa"] for x in v["grafos"].values()) and rep_ok and cf["ok"] and st_ok and cc_ok and ep["ok"])
w.append(f"\n**Veredicto del gate, con las decisiones de la §29 y la R23 y la V23 declaradas: {'PASA' if v['gate_pasa'] else 'NO PASA'}.**")
texto = "\n".join(w) + "\n"
(GD / "veredicto_gate_tf.md").write_text(texto, encoding="utf-8")
(GD / "veredicto_gate_tf.json").write_text(json.dumps(v, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(texto)
sys.exit(0 if v["gate_pasa"] else 1)
