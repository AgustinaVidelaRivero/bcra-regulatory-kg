"""B6.1, tanda 1, T3 (desde el punto 4): la tabla del veredicto del gate con las decisiones 1 a 3 de la autora del 18/10/2026, por script,
desde los archivos de data/experiment/tanda1/t3/ (salidas/, selftests/, intrinsecas_gen3/ y gate_decisiones/). Solo lee; escribe
gate_decisiones/veredicto_gate_t3f.{json,md} bajo <raíz> y la imprime.
  - shapes (pre-registro, §5.1): con la E0 con las partes, la que rige (decisión 1), y con la E0 del repo, informada;
  - la suite: el gate se juzga sobre el acumulado (decisión 3); en la tanda 1 sola, «fuera del grafo» aparte y sin contar; E4-a1 y
    E4-a4 declaradas por la autora (decisión 2) y RT-C5-3, RT-C6-1 y RT-C6-2, las del laudo;
  - la reproducibilidad, los selftests, las intrínsecas con las partes y los contadores de E1, de las tablas del FRENO parcial.
El gate pasa si en los cuatro grafos las bloqueantes de shapes pasan con la E0 con las partes y su control dio OK, si la suite da 0
regresiones no declaradas que cuenten (en el acumulado, todas cuentan), si la reproducibilidad dio OK y si los selftests dieron rc=0
(el del catálogo, en el clon de git, error propio 1 del parcial, declarado por la decisión 7). Las intrínsecas y los contadores son
informativos.
Uso: python3 -I -B veredicto_gate_t3f.py <raíz>
"""
import json
import sys
from pathlib import Path

RAIZ = Path(sys.argv[1]).resolve()
T3 = RAIZ / "data/experiment/tanda1/t3"
GD = T3 / "gate_decisiones"
L = lambda p: json.loads(p.read_text(encoding="utf-8"))  # noqa: E731
NOMBRE = {"veinte": "KG-Tanda1-Veinte-r2b", "veinte_sincola": "KG-Tanda1-Veinte-r2b-sincola",
          "acumulado": "KG-Acumulado-Tandas0y1-r2b", "acumulado_sincola": "KG-Acumulado-Tandas0y1-r2b-sincola"}
ENS = {"veinte": "ens_veinte_r2b", "veinte_sincola": "ens_veinte_r2b_sincola", "acumulado": "ens_treinta_r2b",
       "acumulado_sincola": "ens_treinta_r2b_sincola"}

tg = L(T3 / "salidas/tablas_gate_t3.json")
ep = L(GD / "e0_con_partes_t3f.json")
fg = L(GD / "fuera_del_grafo_t3f.json")
dc = L(T3 / "salidas/doble_corrida_t3.json")
ce = L(T3 / "salidas/contadores_e1_t3.json")
w, v = [], {"grafos": {}}
w.append("#### Tabla V0. La E0 con las partes (`gate_decisiones/e0_con_partes_t3f.json`)\n")
w.append("| E0 | archivos | dos corridas iguales | sha256 del conjunto |")
w.append("|---|---:|---|---|")
for n, e in ep["e0_con_partes"].items():
    w.append(f"| {n} | {e['corridas'][0]['archivos']} | {e['iguales']} | `{e['sha256_conjunto']}` |")
w.append(f"\nEl acumulado rearmado en la copia, igual al del repo: {all(x['iguales'] for x in ep['acumulado']['rearmado_igual_al_repo'].values())}; "
         f"su entrada, {ep['acumulado']['entrada']['archivos']} archivos y {ep['acumulado']['entrada']['bytes']} bytes.")
w.append("\n#### Tabla V1. El control de shapes con esa E0, contra el FRENO parcial (`gate_decisiones/e0_con_partes_t3f.json`, `shapes`)\n")
w.append("| grafo | archivo | byte a byte | líneas del diff crudo | igual con rutas y fecha normalizadas | control |")
w.append("|---|---|---|---:|---|---|")
for g, s in ep["shapes"].items():
    for n, c in s["comparacion_con_el_parcial"].items():
        w.append(f"| {g} | {n} | {c['byte_a_byte']} | {c['lineas_distintas_en_el_diff_crudo']} | "
                 f"{c['igual_con_las_rutas_y_la_fecha_normalizadas']} | {s['control']} |")

w.append("\n#### Tabla V2. El veredicto del gate por grafo\n")
w.append("| grafo | shapes, E0 con las partes (rige) | shapes, E0 del repo (informada) | suite: resuelto / persiste / no aplica | "
         "regresiones | declaradas (laudo) | declaradas (autora) | fuera del grafo | no declaradas que cuentan |")
w.append("|---|---|---|---|---:|---:|---:|---:|---|")
for g in NOMBRE:
    rige = tg["extra"][f"{g}_con_partes"]
    repo = tg["grafos"][g]["nuevo"]["shapes"]
    f = fg["grafos"][g]
    r = f["resumen_suite"]
    pr = f["por_regresion"]
    laudo = sorted(i for i, x in pr.items() if x["clase"] == "declarada (laudo)")
    autora = sorted(i for i, x in pr.items() if x["clase"] == "declarada (autora, 18/10/2026)")
    fuera = sorted(i for i, x in pr.items() if x["fuera_del_grafo"])
    cuentan = f["no_declaradas_que_cuentan"]
    shapes_ok = rige["veredicto"] == "PASA" and not rige["bloqueantes_en_fail"] and ep["shapes"][ENS[g]]["control"]
    v["grafos"][g] = {"nombre": NOMBRE[g], "shapes_rige": {"veredicto": rige["veredicto"], "por_resultado": rige["por_resultado"],
                                                          "bloqueantes_en_fail": rige["bloqueantes_en_fail"],
                                                          "control_contra_el_parcial": ep["shapes"][ENS[g]]["control"]},
                      "shapes_repo": {"veredicto": repo["veredicto"], "bloqueantes_en_fail": repo["bloqueantes_en_fail"]},
                      "suite": {"resumen": r, "regresiones": f["regresiones"], "declaradas_laudo": laudo, "declaradas_autora": autora,
                                "fuera_del_grafo": fuera, "no_declaradas_que_cuentan": cuentan},
                      "pasa": shapes_ok and not cuentan}
    fr = lambda s: f"{s['veredicto']} ({s['por_resultado']['PASS']} / {s['por_resultado']['FAIL']} / {s['por_resultado']['WARN']}" + (  # noqa: E731
        f"; bloqueantes en FAIL: {', '.join(s['bloqueantes_en_fail'])})" if s["bloqueantes_en_fail"] else ")")
    w.append(f"| {g} | {fr(rige)} | {fr(repo)} | {r['resuelto']} / {r['persiste']} / {r['no_aplicable']} | {f['regresiones']} | "
             f"{len(laudo)} | {len(autora)} | {len(fuera) if f['tanda_sola'] else '— (no se aplica)'} | {', '.join(cuentan) or '0'} |")
w.append("\nLas columnas de shapes dan PASS / FAIL / WARN. «Fuera del grafo» cuenta las regresiones con todas sus anclas en TOs que el grafo "
         "no tiene; en el acumulado no se aplica (decisión 3). Las declaradas del laudo, en la tanda 1 sola, también caen fuera del grafo.")
for g in ("veinte", "veinte_sincola"):
    f = fg["grafos"][g]
    w.append(f"\n- **{g}, «fuera del grafo»:** {len(f['regresiones_fuera_del_grafo'])} regresiones "
             f"({', '.join(f['regresiones_fuera_del_grafo'])}); de los {sum(f['items_por_alcance'].values())} ítems, "
             f"{f['items_por_alcance']['fuera del grafo']} fuera del grafo, {f['items_por_alcance']['general']} generales y "
             f"{f['items_por_alcance']['en el grafo']} en el grafo. Cruce con `clasificar_regresiones_t3.py`: "
             f"{fg['cruce'][g]['cuantos'][0]} y {fg['cruce'][g]['cuantos'][1]} ítems, iguales: {fg['cruce'][g]['iguales']}.")

rep_ok = dc["ok"]
st = {}
for p in sorted((T3 / "selftests").glob("*.txt")):
    if p.stem == "fin":
        continue
    t = p.read_text(encoding="utf-8", errors="replace").splitlines()
    st[p.stem] = next((x for x in t if x.startswith("rc=")), "sin rc")
st_ok = all(r == "rc=0" for k, r in st.items() if k != "catalogo_unico") and st.get("catalogo_unico_en_clon_git") == "rc=0"
cc = L(T3 / "selftests/selftest_clave_cache_t3.json")["veredicto"]
w.append("\n#### Tabla V3. Reproducibilidad, selftests, intrínsecas y contadores (de las tablas 2, 6, 7 y 8 del FRENO parcial)\n")
w.append(f"- **Reproducibilidad:** {len(dc['cadenas'])} cadenas, todas iguales: {all(c['igual'] for c in dc['cadenas'])}; veredicto "
         f"{'OK' if rep_ok else 'CON FALLAS'}.")
w.append(f"- **Selftests:** {', '.join(f'{k} {r}' for k, r in st.items())}; el de claves, {cc}. El del catálogo pide git: rc=1 en la "
         f"copia y rc=0 en el clon de git del parcial (error propio 1, declarado por la decisión 7).")
w.append("- **Intrínsecas de generación 3, con la E0 con las partes (informativas):**")
intr = {}
for g, n in NOMBRE.items():
    m = L(T3 / f"intrinsecas_gen3/con_partes/{n}.json")["metricas"]
    m10 = m["M10_chunks_mudos"]
    intr[g] = {"M4": m["M4_average_degree"]["valor"], "M9_aislados": m["M9_nodos_aislados_y_componentes"]["valor"]["nodos_aislados"],
               "M10": [m10["numerador"], m10["denominador"]]}
    w.append(f"  - {n}: M4 {intr[g]['M4']}, M9 {intr[g]['M9_aislados']} nodos aislados, M10 {m10['numerador']} / {m10['denominador']}.")
w.append(f"- **Contadores de E1 (informativos):** {ce['total']}.")
v.update({"reproducibilidad_ok": rep_ok, "selftests": st, "selftests_ok": st_ok, "clave_cache": cc, "intrinsecas_con_partes": intr,
          "contadores_e1": ce["total"]})
v["gate_pasa"] = all(x["pasa"] for x in v["grafos"].values()) and rep_ok and st_ok and cc == "OK"
w.append(f"\n**Veredicto del gate, con las decisiones 1 a 3: {'PASA' if v['gate_pasa'] else 'NO PASA'}.**")
texto = "\n".join(w) + "\n"
(GD / "veredicto_gate_t3f.md").write_text(texto, encoding="utf-8")
(GD / "veredicto_gate_t3f.json").write_text(json.dumps(v, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(texto)
sys.exit(0 if v["gate_pasa"] else 1)
