"""B6.1, tanda final, T3, punto 7: las tablas de la preparación de T4 para el FRENO, por script, desde tanda_final/t3/muestras/ (las dos
poblaciones, los umbrales, los dos sorteos, el material y las unidades a la vista) y la proyección de la mesa
(controles_tanda1/umbrales_t4_por_celdas_mesa.json), con data/experiment/tanda1/t3/scripts/tablas_t4_t3f.py como modelo. Solo lee;
escribe muestras/tablas_t4_tf.md bajo <t3> y la imprime.
Uso: python3 -I -B tablas_t4_tf.py <raíz> <t3>
"""
import json
import sys
from pathlib import Path

RAIZ, T3 = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
M = T3 / "muestras"
L = lambda p: json.loads(Path(p).read_text(encoding="utf-8"))  # noqa: E731
p1, p2, um = L(M / "poblaciones_t4_t3f_tf.json"), L(M / "poblaciones_t4t1_tf.json"), L(M / "umbrales_t4_tf.json")
s1, s2 = L(M / "sorteos_t4_t3f_tf.json"), L(M / "sorteos_t4t1_tf.json")
m1, m2, vis = L(M / "material/material_t4_t3f_tf.json"), L(M / "material/material_t4t1_tf.json"), L(M / "unidades_a_la_vista_T4.json")
proy = L(RAIZ / "data/experiment/controles_tanda1/umbrales_t4_por_celdas_mesa.json")
# la línea de base informativa: las cifras del T4 de la tanda 1, de los huecos del pre-registro (decisión 4 de la autora sobre el FRENO
# T3 parcial)
vh = L(RAIZ / "data/experiment/tanda_final/preregistro/valores_huecos_tanda_final_mesa.json")
CEL = ["RI:sin_raiz", "RI:resto", "NG:sin_raiz", "NG:resto"]
mil = lambda n: f"{n:,}".replace(",", ".")  # noqa: E731
dec = lambda x, k=3: f"{x:.{k}f}".replace(".", ",")  # noqa: E731
pob = {**p1["muestras"], **p2["muestras"]}
w = [f"#### Tabla T1. La población de cada muestra, por celda (`muestras/poblaciones_t4_t3f_tf.json`, {p1['hora']}; "
     f"`muestras/poblaciones_t4t1_tf.json`, {p2['hora']})", "",
     f"Grafo de las poblaciones de elementos del grafo: `{p1['grafo']['ruta']}`, sha256 `{p1['grafo']['kg_sha256']}` (el mismo en los dos "
     f"archivos: {p1['grafo'] == p2['grafo']}). TOs por celda: " + ", ".join(f"{c} {p1['tos_por_celda'][c]}" for c in CEL) + ".", "",
     "| muestra | elemento | N | " + " | ".join(CEL) + " | se lee entera, sin celdas | sha256 de los ids por celda |",
     "|---|---|---:|" + "---:|" * 4 + "---|---|"]
for m, x in pob.items():
    w.append(f"| {m} | {x['elemento']} | {mil(x['N'])} | " + " | ".join(mil(x["N_por_celda"][c]) for c in CEL)
             + f" | {x['entera_sin_celdas']} | `{x['sha256_ids_por_celda'][:16]}…` |")
w.append(f"\nUnidades en `finales.jsonl`: {mil(p1['unidades_en_finales'])}; la cola, {p1['cola']}; las aceptadas (los tres estados juntos), "
         f"{mil(p1['aceptadas'])}. Partes por corte de E1: {len(p1['partes_por_corte_que_usan_el_chunk_de_su_unidad'])}. La (12), contra las "
         f"aristas de extracción de la (10) del mismo grafo: {p2['controles']['observacion_12_igual_a_la_extraccion_de_la_10']}. La (3): "
         f"{p2['muestras']['vigilancia:3']['nodos_en_grupos']} nodos en grupos, por tamaño {p2['muestras']['vigilancia:3']['nodos_por_grupo']}.")
w += ["", "#### Tabla T2. Cuántos se sortean por celda, y lo que se declara (`celdas_t4_t3f.asignar`, sin cambios)", "",
      "| muestra | " + " | ".join(CEL) + " | total | notas |", "|---|" + "---:|" * 5 + "---|"]
sor = {**{m: (s1, x) for m, x in s1["muestras"].items()}, **{m: (s2, x) for m, x in s2["muestras"].items()}}
for m, (_, x) in sor.items():
    s = L(M / x["archivo"])
    w.append(f"| {m} | " + " | ".join(str(s["celdas"][c]["n"]) for c in CEL) + f" | {s['n']} | {'; '.join(s['notas']) or '—'} |")
w += ["", "#### Tabla T3. Los pesos reales por celda (w_c = N_c / N de la población de cada muestra)", "",
      "| muestra | " + " | ".join(CEL) + " |", "|---|" + "---:|" * 4]
filas_p = [("aceptadas:items", um["aceptadas"]["items"]["pesos"]), ("aceptadas:no_items", um["aceptadas"]["no_items"]["pesos"]),
           ("cola", um["cola"]["pesos"])] + [(m, x["pesos"]) for m, x in um["otras"].items()]
for m, p in filas_p:
    w.append(f"| {m} | " + " | ".join("—" if p[c] is None else dec(p[c], 4) for c in CEL) + " |")
w.append("| proyección de la E0 de la tanda 1 (script de la mesa) | " + " | ".join(dec(proy["proyeccion_pesos_e0"]["pesos"][c], 4) for c in CEL) + " |")
w += ["", "#### Tabla T4. Los umbrales, con los pesos reales (`muestras/umbrales_t4_tf.json`) y la proyección", "",
      "| estrato | n efectivo | atención desde (p) | freno por intervalos desde | atención sobre las 60 desde | errores en una sola celda "
      "para la atención |", "|---|---:|---|---:|---:|---|"]
for s in ("items", "no_items"):
    for etiqueta, u in (("reales", um["aceptadas"][s]["umbrales"]), ("proyección", proy["proyeccion_pesos_e0"][s])):
        w.append(f"| {s} ({etiqueta}) | {dec(u['n_efectivo_kish'])} | {dec(u['atencion']['umbral_tasa_ponderada'])} "
                 f"({dec(u['atencion']['p_valor_en_el_umbral'], 4)}) | {dec(u['freno_por_intervalos']['umbral_tasa_ponderada'])} | "
                 f"{dec(u['freno_por_atencion_sobre_60']['umbral_tasa_ponderada'])} | "
                 + ", ".join(f"{c} {v}" for c, v in u["errores_minimos_en_una_sola_celda_para_la_atencion"].items()) + " |")
t = um["tasa_ponderada_total"]
w.append(f"\n- **La tasa bajo H0** de cada estrato es la del script de la mesa (la de la tanda 0): " + "; ".join(
    f"{s} {x['k']} de {x['n']}" for s, x in um["tasa_bajo_H0"].items()) + ". " + um["momentos_de_lectura"][0].upper()
         + um["momentos_de_lectura"][1:] + ".")
w.append(f"- **Tasa ponderada total:** n efectivo {dec(t['n_efectivo'])} (proyección {dec(proy['tasa_ponderada_total']['n_efectivo_proyectado'])}); "
         f"pesos de los estratos ítems {dec(t['pesos_de_los_estratos']['items'], 4)} y no ítems {dec(t['pesos_de_los_estratos']['no_items'], 4)}.")
r, rp = um["atencion_RI"], proy["atencion_RI"]
w.append(f"- **Atención de RI** ({mil(r['N_RI'])} unidades RI aceptadas): salta desde una tasa ponderada de RI de {dec(r['umbral_tasa_ponderada'])} "
         f"(p {dec(r['p_valor_en_el_umbral'], 4)}); bajo H0, {dec(r['tasa_de_RI_bajo_H0'], 4)}; n efectivo {dec(r['n_efectivo_kish'])}; potencia "
         f"con la tasa de RI duplicada {dec(r['potencia_con_la_tasa_de_RI_duplicada'], 4)}. Proyección: {dec(rp['umbral_tasa_ponderada'])}, "
         f"{dec(rp['tasa_de_RI_bajo_H0'], 4)}, {dec(rp['n_efectivo_kish'])} y {dec(rp['potencia_con_la_tasa_de_RI_duplicada'], 4)}.")
c = um["cola"]["regla_del_25"]
w.append(f"- **La cola, regla del 25 %:** n efectivo {dec(c['n_efectivo_kish'])}; límite superior de Wilson con 0 errores "
         f"{dec(c['superior_con_0_errores'], 4)}; con 1 error en cada celda sola: "
         + ", ".join(f"{k} {dec(v, 4)}" for k, v in c["superior_con_1_error_en_cada_celda_sola"].items())
         + f". Bases: tanda 0, {um['cola']['base_tanda0']}; tanda 1, {um['cola']['base_tanda1']}.")
w.append(f"- **Los controles:** la importación del script de la mesa reproduce su JSON byte a byte: {um['control']['igual']}; las tres cuentas "
         f"con los pesos proyectados dan sus cifras: {um['control_ok']}.")
w.append("- **La línea de base informativa, el T4 de la tanda 1** (`preregistro/valores_huecos_tanda_final_mesa.json`; no decide nada): "
         + "; ".join(f"{k.split('.', 1)[1]}: {vh[k]}" for k in ("T4.aceptadas_items", "T4.aceptadas_no_items", "T4.ponderada_total",
                                                                "T4.atencion_RI", "T4.cola", "T4.vigilancias_y_12")) + ".")
w += ["", f"#### Tabla T5. Los sorteos (base `{s1['base'][:8]}…`; igual al sha256 de la versión para firmar, de `5289b02f`: "
      f"{s1['base'] == s1['version_para_firmar_sha256'] == s2['version_para_firmar_sha256']})", "",
      "| muestra | archivo | elementos | sha256 | hora |", "|---|---|---:|---|---|"]
for m, (_, x) in sor.items():
    w.append(f"| {m} | `muestras/{x['archivo']}` | {x['n']} | `{x['sha256']}` | {x['hora']} |")
w += ["", f"#### Tabla T6. El material (`muestras/material/`; {m1['hora']} y {m2['hora']})", "",
      "| muestra | fichas | fichas (.jsonl) | fichas (.md) | planilla (.csv) |", "|---|---:|---|---|---|"]
for mat in (m1, m2):
    for m, x in mat["muestras"].items():
        a = x["archivos"]
        nom = m.replace(":", "_")
        w.append(f"| {m} | {x['fichas']} | `{a[f'fichas_{nom}.jsonl'][:16]}…` | `{a[f'fichas_{nom}.md'][:16]}…` | `{a[f'planilla_{nom}.csv'][:16]}…` |")
w.append(f"\nEl control del material de (1), (3) y (12): {json.dumps(m2['control'], ensure_ascii=False)}.")
w += ["", f"#### Tabla T7. Las unidades a la vista (`muestras/unidades_a_la_vista_T4.json`, {vis['hora']})", "",
      "| muestra | fichas | unidades a la vista | por versión | con la regla 1.1 de la tanda 1 (información) |", "|---|---:|---:|---|---:|"]
for m, x in vis["muestras"].items():
    w.append(f"| {m} | {x['fichas']} | {mil(x['unidades_a_la_vista'])} | {x['por_version']} | {mil(x['informacion_con_la_regla_1_1_de_la_tanda_1'])} |")
tv = vis["todas_las_muestras"]
w.append(f"| todas | — | {mil(tv['unidades_a_la_vista'])} | {tv['por_version']} | {mil(tv['informacion_con_la_regla_1_1_de_la_tanda_1'])} |")
texto = "\n".join(w) + "\n"
(M / "tablas_t4_tf.md").write_text(texto, encoding="utf-8")
print(texto)
