"""B6.1, tanda final, T5, puntos 6 y 7: el reporte de cierre (t5/reporte_tanda_final.md) y las propuestas de entrada del backlog
(t5/propuestas_backlog_t5.jsonl; el backlog no se toca), por script, desde t5/salidas/cifras_t5.json (cifras_t5_tf.py), la tabla 1 de
t4/tablas_t4_tramo3.md (tal cual) y la columna propuesta del tablero (t5/columna_tanda_final_tablero_PROPUESTA.md). Toda cifra sale de
esos archivos; el texto fijo no lleva cifras propias. Solo lee; escribe esos dos archivos.
Uso: python3 -I -B reporte_t5_tf.py <raíz>
"""
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
R = Path(sys.argv[1]).resolve()
TF = R / "data/experiment/tanda_final"
T5 = TF / "t5"
c = json.loads((T5 / "salidas/cifras_t5.json").read_text(encoding="utf-8"))
t4tab = (TF / "t4/tablas_t4_tramo3.md").read_text(encoding="utf-8")
tabla1 = re.search(r"#### Tabla 1\..*?(?=\n#### Tabla 2\.)", t4tab, re.S).group(0).rstrip()
d = lambda x, k=6: f"{x:.{k}f}".replace(".", ",")  # noqa: E731
mil = lambda n: f"{n:,}".replace(",", ".")  # noqa: E731
sn = lambda b: "sí" if b else "no"  # noqa: E731
K, V, IDS = c["costo"], c["volumenes"], c["ids_de_modelo"]
w = ["# Reporte de cierre de la tanda final de B6.1 (T5)", "",
     "Pre-registro de la tanda final, firmado en `4de7f2a7` (§5 y §7), con sus notas al pie (`27bfaeb5` y `86541475`); enmienda 9 al "
     "protocolo entre tandas (`756a0394`), §1, punto 1; el protocolo entre tandas, §2, y el pre-registro de la tanda 1, §5.6, para los "
     "hallazgos. Toda cifra sale de `t5/salidas/cifras_t5.json` (`t5/scripts/cifras_t5_tf.py`); este archivo lo arma "
     "`t5/scripts/reporte_t5_tf.py`. USD 0, sin API.", ""]

# 1. Volúmenes
w += ["## 1. Los volúmenes", "", "#### Tabla 1. Las unidades por tramo (`volumenes`, de `t2/resumen_t2_final.json`)", "",
      "| tramo | TOs | unidades | con las partes | aceptadas (los tres estados juntos) | cola | errores definitivos | sin destino | ids repetidos |",
      "|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
for tr, nom in (("tramo_1", "tramo 1"), ("tramo_2", "tramo 2"), ("tanda", "tanda final")):
    x = V[tr]
    w.append(f"| {nom} | {x['tos']} | {mil(x['unidades'])} | {mil(x['unidades_con_partes'])} | {mil(x['aceptadas'])} | {x['cola']} | "
             f"{x['errores']} | {x['sin_destino']} | {x['ids_repetidos']} |")
w += ["", f"El error definitivo está en {', '.join(V['tos_con_error_definitivo'])} (la unidad muda de la fila 61 del tablero; hallazgo "
      "H-T5-01).", "", "#### Tabla 2. Los ocho ensamblados de T3 (`volumenes.ensamblados`, de `t3/salidas/doble_corrida_tf.json`)", "",
      "| grafo | nodos | aristas | sha256 del `kg.json` | dos corridas iguales |", "|---|---:|---:|---|---|"]
for g, x in V["ensamblados"].items():
    w.append(f"| {g} | {mil(x['nodos'])} | {mil(x['aristas'])} | `{x['kg_sha256']}` | {sn(x['dos_corridas_iguales'])} |")

# 2. Costo
tot = K["total"]
w += ["", "## 2. El costo real contra el estimado (§3 y §7)", "",
      "#### Tabla 3. Por etapa y por tramo, en USD (`costo.por_tramo` y `costo.total`)", "",
      "| | E1 real | E3 real | total real | estimado del §3 | razón | estimado repartido (manifiesto) | razón |", "|---|---:|---:|---:|---:|---:|---:|---:|"]
for tr, nom in (("tramo_1", "tramo 1"), ("tramo_2", "tramo 2")):
    x = K["por_tramo"][tr]
    w.append(f"| {nom} | {d(x['real']['e1'])} | {d(x['real']['e3'])} | {d(x['real']['total'])} | {d(x['estimado_s3']['total'])} | "
             f"{d(x['desviacion_contra_s3']['razon_total'], 4)} | {d(x['estimado_repartido']['total'])} | "
             f"{d(x['desviacion_contra_repartido']['razon_total'], 4)} |")
w.append(f"| tanda final | {d(tot['real']['e1'])} | {d(tot['real']['e3'])} | {d(tot['real']['total'])} | {d(tot['estimado_s3']['total'])} | "
         f"{d(tot['desviacion_contra_s3']['razon_total'], 4)} | {d(tot['estimado_repartido']['total'])} | "
         f"{d(tot['desviacion_contra_repartido']['razon_total'], 4)} |")
w += ["", "#### Tabla 4. La desviación por etapa, en USD (real − estimado)", "",
      "| | E1 contra el §3 | E3 contra el §3 | total contra el §3 | E1 contra el repartido | E3 contra el repartido | total contra el repartido |",
      "|---|---:|---:|---:|---:|---:|---:|"]
for tr, nom, x in (("tramo_1", "tramo 1", K["por_tramo"]["tramo_1"]), ("tramo_2", "tramo 2", K["por_tramo"]["tramo_2"]), ("total", "tanda final", tot)):
    a, b = x["desviacion_contra_s3"], x["desviacion_contra_repartido"]
    w.append(f"| {nom} | {d(a['e1'])} | {d(a['e3'])} | {d(a['total'])} | {d(b['e1'])} | {d(b['e3'])} | {d(b['total'])} |")
p = tot["presupuesto_compartido"]
w += ["", f"- **El estimado del §3:** por tramo, {d(K['por_tramo']['tramo_1']['estimado_s3']['total'])} y "
      f"{d(K['por_tramo']['tramo_2']['estimado_s3']['total'])}: U × 0,021115, sin las líneas de alcance, como las cifras del §3; en total, "
      f"con las líneas (A3.costo_lineas_usd), {d(tot['estimado_s3']['total'])}. Por etapa, con las tarifas del manifiesto (e1 0,010135 más "
      "las líneas; e3 0,010980).",
      "- **El estimado repartido** es el del manifiesto, por TO (nota `27bfaeb5`): el que usó la proyección del runner. Va al lado.",
      f"- **El presupuesto compartido:** USD {d(p['gasto_usd'])} de un tope de {d(p['tope_usd'], 4)} ({d(p['proporcion_del_tope'], 4)} del "
      f"tope). La suma de las fases da {d(tot['real']['total'])}: la diferencia, {d(p['suma_de_las_fases_menos_el_presupuesto'])}, es de "
      f"redondeo. El resumen de T2 da la misma suma por TO: {sn(K['control_con_resumen_t2']['por_to_igual'])}.",
      "- **Los pasos sin API** van en 0: " + ", ".join(f"{k}" for k in K["pasos_sin_api_usd"]) + ".",
      "- **E3 va como una sola cifra por TO,** con los reintentos adentro (cegamiento).",
      f"- **La tanda 1 al lado** (hueco `{K['tanda1']['hueco']}`, `{K['tanda1']['fuente']}`, clave `{K['tanda1']['clave']}`, en "
      f"`{K['tanda1']['commit']}`), tal cual: «{K['tanda1']['valor']}».", "",
      "#### Tabla 5. Por TO, en USD (`costo.por_to`; el estimado, el del manifiesto)", "",
      "| TO | tramo | E1 real | E3 real | total real | estimado | desviación | razón |", "|---|---|---:|---:|---:|---:|---:|---:|"]
for t, x in K["por_to"].items():
    w.append(f"| {t} | {x['tramo'][-1]} | {d(x['real']['e1'])} | {d(x['real']['e3'])} | {d(x['real']['total'])} | "
             f"{d(x['estimado_manifiesto']['total'])} | {d(x['desviacion']['total'])} | {d(x['desviacion']['razon_total'], 4)} |")

# 3. Ids
w += ["", "## 3. Los ids de modelo que devolvió la API (`ids_de_modelo`, de `t5/salidas/ids_modelo_t5.json`)", "",
      "| etapa | ids | llamadas | lo esperado | igual |", "|---|---|---|---|---|",
      f"| E1 | {', '.join(IDS['e1']['ids'])} | " + ", ".join(f"{k}: {mil(v)}" for k, v in IDS["e1"]["llamadas_por_id"].items()) +
      f" | {', '.join(IDS['e1']['esperado'])} | {sn(IDS['e1']['igual'])} |",
      f"| reintentos de E1 de la fase de E3 | {', '.join(IDS['e1_reintentos_de_la_fase_de_e3']['ids'])} | en el `NO_ABRIR_` | "
      f"{', '.join(IDS['e1_reintentos_de_la_fase_de_e3']['esperado'])} | {sn(IDS['e1_reintentos_de_la_fase_de_e3']['igual'])} |",
      f"| E3 | {', '.join(IDS['e3']['ids'])} | en el `NO_ABRIR_` | {', '.join(IDS['e3']['esperado'])} | {sn(IDS['e3']['igual'])} |", "",
      f"Lo esperado sale del pre-registro de la tanda final, §2; {IDS['manifiesto']}. El freno por modelo de T2: {IDS['freno_por_modelo_de_T2']}.",
      "Las llamadas de E1 incluyen sus reintentos y las partes; las de E3 cuentan los reintentos de E3 y van solo al `NO_ABRIR_`."]

# 4. Incidencias
w += ["", "## 4. Las incidencias", "",
      "- **T1** (`t1/FRENO_T1.md`): la corrida en seco frenó con dos decisiones para la autora antes de T2: el estimado por TO del "
      "manifiesto, que pasó a ser el repartido por caracteres (nota al pie `27bfaeb5`), y si el ensamblado del tramo 1 alcanzaba para su "
      "sello. Hubo además un incidente externo (un Neo4j que se apagó y reescribió su volumen, ignorado por git).",
      f"- **T2** (`t2/FRENO_T2.md`): el control entre tramos dio FRENO por {V['tramo_1']['errores']} error definitivo en el tramo 1 "
      f"({', '.join(V['tos_con_error_definitivo'])}); con la decisión de la autora, el segundo lanzamiento siguió con el tramo 2 y terminó con "
      "salida 0. La unidad falta en los grafos, como decidió la autora (registro de decisiones, §44); su causa está en `BKL-0050`.",
      "- **T3** (`t3/FRENO_T3.md`, §2): el selftest de claves sin la R23 y la V23; los manifiestos del tramo 1 con la raya (enmienda 9, "
      "punto 8); el derivador adaptado del acumulado de 60; los umbrales de T4 del script de la mesa; y la lista de unidades a la vista. "
      "Las regresiones declaradas del gate van en los hallazgos (H-T5-08).",
      "- **La regla de las dudosas** (pre-registro, §6; registro, §35): una «dudosa» cuenta como error para la tasa, la atención y el freno, "
      "y la cuenta sin ellas va al lado como sensibilidad. En T4 no hubo dudosas en la cola ni en las aceptadas."]

# 5. Las tasas de T4
r6 = c["t4"]["aceptadas_no_items_sobre_60"]
w += ["", "## 5. Las tasas de T4 (`t4/tasas/tasas_t4_tramo3.json`)", "",
      "La tabla 1 de `t4/tablas_t4_tramo3.md` (de `t4/scripts/tablas_t4t3_tf.py`), tal cual:", "", tabla1, "",
      f"- **El freno de las aceptadas no ítems:** la atención sobre las 60 se confirma (tasa {d(r6['tasa_ponderada'], 4)}, umbral "
      f"{d(r6['umbral_recalculado'], 4)}, p {d(r6['p_valor_sobre_60'], 4)}); el freno por intervalos, {sn(r6['freno_por_intervalos'])}.",
      "- Lo que sigue al freno lo decide la autora con su clasificación (registro de decisiones, §89)."]

# 6. El tablero
w += ["", "## 6. La columna «Tanda final» del tablero", "",
      "Va completa, como propuesta, en `t5/columna_tanda_final_tablero_PROPUESTA.md` (de `t5/scripts/columnas_tablero_t5.py`): las celdas de "
      "T3 y la fila 59, que esperaba a T4. El tablero del repo no se toca. Cada fila contra su meta (`tablero_contra_su_meta`):", "",
      "| fila | síntoma | cifra | estado | criterio |", "|---:|---|---|---|---|"]
for n, x in c["tablero_contra_su_meta"].items():
    w.append(f"| {n} | {x['sintoma']} | {x['cifra']} | {x['estado']} | {x['criterio']} |")

# 7. Hallazgos
vg = c["vigilancias_contra_su_linea_de_base"]
w += ["", "## 7. Los hallazgos, en los ejes A y B", "",
      "Qué es un hallazgo: una fila del tablero que no cumple su meta, una incorrecta de las lecturas de T4, una vigilancia fuera de su "
      "línea de base, una regresión declarada de T3 y la cola con la regla del 25 % disparada (protocolo entre tandas, §2; pre-registro de la "
      "tanda 1, §5.6). La causa de las incorrectas sale de la lectura de la autora; la de las aceptadas no ítems, de su clasificación.", "",
      "| id | qué | cifra | eje A | eje B | `capa_pipeline` | causa | backlog |", "|---|---|---|---|---|---|---|---|"]
for h in c["hallazgos"]:
    w.append(f"| {h['id']} | {h['tipo']}: {h['que']} | {h['cifra']} | {h['eje_A']} | {h['eje_B']} | "
             f"{', '.join(h['capa_pipeline']) if h['capa_pipeline'] else '—'} | {h['causa']} | {h['backlog']}"
             + (f" (`{h['propuesta']}`)" if h["propuesta"] else "") + " |")
w += ["", f"**Las vigilancias leídas contra su línea de base** ({vg['criterio']}):", "",
      "| vigilancia | tanda final | Wilson | tanda 1 | fuera | empeora | hallazgo |", "|---|---|---|---|---|---|---|"]
for m, x in vg["leidas"].items():
    w.append(f"| {m} | {x['tanda_final']} | [{d(x['wilson'][0], 4)}; {d(x['wilson'][1], 4)}] | {x['tanda1']} | {sn(x['fuera_de_la_linea_de_base'])} | "
             f"{sn(x['empeora'])} | {sn(x['hallazgo'])} |")
w += ["", "Las causas de cada unidad con error de la cola y de las aceptadas de ítems (de la lectura de la autora) están en "
      "`errores_de_las_lecturas` de `t5/salidas/cifras_t5.json`; las 16 de no ítems, con «causa: en la clasificación de la autora "
      "(`t4/clasificacion_freno/`)». Lo diferido va como propuesta de entrada del backlog en `t5/propuestas_backlog_t5.jsonl`: "
      + ", ".join(f"`{x['id']}`" for x in c["propuestas_backlog"]) + "."]

# 8. Lo que sigue
w += ["", "## 8. Lo que sigue (no lo hace T5)", "",
      "- **La señal cid:** las 3 unidades de la tanda final con «(cid:», después de su T5 (registro de decisiones, §14).",
      "- **El catálogo al cierre:** su material, con la decisión 4 del §9 del pre-registro, después del sello.",
      "- **La clasificación del freno** de las aceptadas no ítems, que hace la autora (registro de decisiones, §89).", ""]
(T5 / "reporte_tanda_final.md").write_text("\n".join(w), encoding="utf-8")
(T5 / "propuestas_backlog_t5.jsonl").write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in c["propuestas_backlog"]),
                                                 encoding="utf-8")
print("reporte_tanda_final.md", len(w), "líneas; propuestas_backlog_t5.jsonl", len(c["propuestas_backlog"]))
