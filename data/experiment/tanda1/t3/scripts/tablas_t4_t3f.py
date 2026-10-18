"""B6.1, tanda 1, T3, punto 7: las tablas de la preparación de T4 para el FRENO, por script, desde tanda1/t3/muestras/ (poblaciones,
umbrales, sorteos, material y unidades a la vista) y la proyección de la mesa (controles_tanda1/umbrales_t4_por_celdas_mesa.json).
Solo lee; escribe muestras/tablas_t4_t3f.md bajo <raíz> y la imprime.
Uso: python3 -I -B tablas_t4_t3f.py <raíz>
"""
import json
import sys
from pathlib import Path

RAIZ = Path(sys.argv[1]).resolve()
M = RAIZ / "data/experiment/tanda1/t3/muestras"
L = lambda p: json.loads(Path(p).read_text(encoding="utf-8"))  # noqa: E731
pob, um = L(M / "poblaciones_t4.json"), L(M / "umbrales_t4_reales.json")
sor, mat, vis = L(M / "sorteos_t4.json"), L(M / "material/material_t4.json"), L(M / "unidades_a_la_vista_T4.json")
proy = L(RAIZ / "data/experiment/controles_tanda1/umbrales_t4_por_celdas_mesa.json")
CEL = ["RI:sin_raiz", "RI:resto", "NG:sin_raiz", "NG:resto"]
mil = lambda n: f"{n:,}".replace(",", ".")  # noqa: E731
dec = lambda x, k=3: f"{x:.{k}f}".replace(".", ",")  # noqa: E731
w = [f"#### Tabla T1. La población de cada muestra, por celda (`muestras/poblaciones_t4.json`, {pob['hora']})", "",
     "| muestra | elemento | N | " + " | ".join(CEL) + " | se lee entera, sin celdas |", "|---|---|---:|" + "---:|" * 4 + "---|"]
for m, x in pob["muestras"].items():
    w.append(f"| {m} | {x['elemento']} | {mil(x['N'])} | " + " | ".join(mil(x["N_por_celda"][c]) for c in CEL) + f" | {x['entera_sin_celdas']} |")
w.append(f"\nUnidades en `finales.jsonl`: {mil(pob['unidades_en_finales'])}; la cola, {pob['cola']}; las aceptadas (los tres estados "
         f"juntos), {mil(pob['aceptadas'])}. Las partes por corte de E1 que usan el chunk de su unidad: "
         f"{', '.join(pob['partes_por_corte_que_usan_el_chunk_de_su_unidad'])}.")
w += ["", "#### Tabla T2. Cuántos se sortean por celda, y lo que se declara (`celdas_t4_t3f.asignar`)", "",
      "| muestra | " + " | ".join(CEL) + " | total | notas |", "|---|" + "---:|" * 5 + "---|"]
for m, x in sor["muestras"].items():
    s = L(M / x["archivo"])
    w.append(f"| {m} | " + " | ".join(str(s["celdas"][c]["n"]) for c in CEL) + f" | {s['n']} | {'; '.join(s['notas']) or '—'} |")
w += ["", "#### Tabla T3. Los pesos reales por celda (w_c = N_c / N de la población de cada muestra)", "",
      "| muestra | " + " | ".join(CEL) + " |", "|---|" + "---:|" * 4]
filas_p = [("aceptadas:items", um["aceptadas"]["items"]["pesos"]), ("aceptadas:no_items", um["aceptadas"]["no_items"]["pesos"]),
           ("cola", um["cola"]["pesos"])] + [(m, x["pesos"]) for m, x in um["otras"].items()]
for m, p in filas_p:
    w.append(f"| {m} | " + " | ".join("—" if p[c] is None else dec(p[c], 4) for c in CEL) + " |")
w.append(f"| proyección de la E0 (pre-registro) | " + " | ".join(dec(proy["proyeccion_pesos_e0"]["pesos"][c], 4) for c in CEL) + " |")
w += ["", "#### Tabla T4. Los umbrales, con los pesos reales (`muestras/umbrales_t4_reales.json`) y la proyección del pre-registro", "",
      "| estrato | n efectivo | atención desde (p) | freno por intervalos desde | atención sobre las 60 desde | errores en una sola celda "
      "para la atención |", "|---|---:|---|---:|---:|---|"]
for s in ("items", "no_items"):
    for etiqueta, u in (("reales", um["aceptadas"][s]["umbrales"]), ("proyección", proy["proyeccion_pesos_e0"][s])):
        w.append(f"| {s} ({etiqueta}) | {dec(u['n_efectivo_kish'])} | {dec(u['atencion']['umbral_tasa_ponderada'])} "
                 f"({dec(u['atencion']['p_valor_en_el_umbral'], 4)}) | {dec(u['freno_por_intervalos']['umbral_tasa_ponderada'])} | "
                 f"{dec(u['freno_por_atencion_sobre_60']['umbral_tasa_ponderada'])} | "
                 + ", ".join(f"{c} {v}" for c, v in u["errores_minimos_en_una_sola_celda_para_la_atencion"].items()) + " |")
t = um["tasa_ponderada_total"]
w.append(f"\n- **Tasa ponderada total:** n efectivo {dec(t['n_efectivo'])} (proyección {dec(proy['tasa_ponderada_total']['n_efectivo_proyectado'])}); "
         f"pesos de los estratos ítems {dec(t['pesos_de_los_estratos']['items'], 4)} y no ítems {dec(t['pesos_de_los_estratos']['no_items'], 4)}. "
         f"La tanda 0 con el mismo método: {dec(t['tanda0_con_el_mismo_metodo']['p'], 4)}, Wilson {t['tanda0_con_el_mismo_metodo']['wilson']}.")
r, rp = um["atencion_RI"], proy["atencion_RI"]
w.append(f"- **Atención de RI** ({r['N_RI']} unidades RI aceptadas): salta desde una tasa ponderada de RI de {dec(r['umbral_tasa_ponderada'])} "
         f"(p {dec(r['p_valor_en_el_umbral'], 4)}); bajo H0, {dec(r['tasa_de_RI_bajo_H0'], 4)}; n efectivo {dec(r['n_efectivo_kish'])}; potencia "
         f"con la tasa de RI duplicada {dec(r['potencia_con_la_tasa_de_RI_duplicada'], 4)}. Proyección: {dec(rp['umbral_tasa_ponderada'])}, "
         f"{dec(rp['tasa_de_RI_bajo_H0'], 4)}, {dec(rp['n_efectivo_kish'])} y {dec(rp['potencia_con_la_tasa_de_RI_duplicada'], 4)}.")
c = um["cola"]["regla_del_25"]
w.append(f"- **La cola, regla del 25 %:** n efectivo {dec(c['n_efectivo_kish'])}; límite superior de Wilson con 0 errores "
         f"{dec(c['superior_con_0_errores'], 4)}; con 1 error en cada celda sola: "
         + ", ".join(f"{k} {dec(v, 4)}" for k, v in c["superior_con_1_error_en_cada_celda_sola"].items()) + ". Es cifra y vigilancia, no freno.")
w.append(f"- **Los controles:** la importación del script de la mesa reproduce su JSON byte a byte: {um['control']['igual']}; las tres cuentas "
         f"con los pesos proyectados dan sus cifras: {um['control_ok']}.")
w += ["", f"#### Tabla T5. Los sorteos (`muestras/sorteos_t4.json`; base `{sor['base'][:8]}…`; poblaciones `{sor['poblaciones_t4_sha256'][:8]}…`)", "",
      "| muestra | archivo | elementos | sha256 | hora |", "|---|---|---:|---|---|"]
for m, x in sor["muestras"].items():
    w.append(f"| {m} | `muestras/{x['archivo']}` | {x['n']} | `{x['sha256']}` | {x['hora']} |")
w.append("\nLa segunda corrida (`muestras/segunda_corrida_de_los_sorteos/`) da las seis muestras byte a byte iguales, y el índice igual salvo las horas "
         "(`consola_sorteos_corrida2.txt`). Las vigilancias (1) y (3) no se sortean; las cadenas de la ampliación no se usan.")
w += ["", f"#### Tabla T6. El material (`muestras/material/material_t4.json`, {mat['hora']})", "",
      "| muestra | fichas | fichas (.jsonl) | fichas (.md) | planilla (.csv) |", "|---|---:|---|---|---|"]
for m, x in mat["muestras"].items():
    a = x["archivos"]
    nom = m.replace(":", "_")
    w.append(f"| {m} | {x['fichas']} | `{a[f'fichas_{nom}.jsonl'][:16]}…` | `{a[f'fichas_{nom}.md'][:16]}…` | `{a[f'planilla_{nom}.csv'][:16]}…` |")
w += ["", f"#### Tabla T7. Las unidades a la vista (`muestras/unidades_a_la_vista_T4.json`, {vis['hora']})", "",
      "| muestra | fichas | unidades a la vista | por versión | de ellas, solo por un TextoOrdenado o un Sujeto (información) |", "|---|---:|---:|---|---:|"]
for m, x in vis["muestras"].items():
    w.append(f"| {m} | {x['fichas']} | {mil(x['unidades_a_la_vista'])} | {x['por_version']} | {mil(x['informacion_solo_por_TextoOrdenado_o_Sujeto'])} |")
w.append(f"| todas | — | {mil(vis['todas_las_muestras']['unidades_a_la_vista'])} | {vis['todas_las_muestras']['por_version']} | — |")
pp = pob["propuestas_sin_sorteo"]
w += ["", "#### Tabla T8. Las vigilancias (1) y (3): la población de la definición propuesta (información; no se sortean)", "",
      f"- (1): {pp['vigilancia:1']['definicion']}: {mil(pp['vigilancia:1']['N'])}, por celda {pp['vigilancia:1']['N_por_celda']}.",
      f"- (3): {pp['vigilancia:3']['definicion']}: {pp['vigilancia:3']['N_grupos']} grupos con {pp['vigilancia:3']['nodos_en_grupos']} nodos, "
      f"por celda del nodo de id menor {pp['vigilancia:3']['N_por_celda_del_nodo_de_id_menor']}."]
texto = "\n".join(w) + "\n"
(M / "tablas_t4_t3f.md").write_text(texto, encoding="utf-8")
print(texto)
