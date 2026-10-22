"""B6.1, tanda final, T5, puntos 7 y 8: las dos columnas del tablero de correcciones (docs/tablero_correcciones.md, filas :49 a :74) como
propuestas aparte; el tablero del repo no se toca. Solo lee; escribe <t5>/columna_tanda_final_tablero_PROPUESTA.md y
<t5>/columna_tramo1_tablero_PROPUESTA.md, y las imprime.
  - «Tanda final»: las celdas de T3, tal cual (t3/conteos_sin_leer/columna_tanda_final_tablero_tf.md, de t3/scripts/tablas_contado_tf.py,
    sobre contado_sin_leer_tf.json), y la que esperaba a T4, la de la observación (12), desde t4/tasas/tasas_t4_tramo3.json
    (`observacion:12`). Cada celda con su ancla.
  - «Tramo 1»: el tramo 1 (KG-TandaFinal-Tramo1-r2b) y su acumulado (KG-Acumulado-Tandas0y1yTramo1-r2b), completos y sin cola, desde
    t5/salidas/contado_tramo1_t5.json (contado_tramo1_t5.py, el código de T3 sobre una copia), con las fórmulas de celda de
    t3/scripts/tablas_contado_tf.py (filas 49 a 74), sin la línea de base de la tanda 1 (el «seguí» de T5 veda sus cifras). La suite y la
    regresión, del gate de T3 (t3/gate_decisiones/veredicto_gate_tf.json y fuera_del_grafo_tf.json), que corrió sobre los cuatro.
Uso: python3 -I -B columnas_tablero_t5.py <raíz>
"""
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
RAIZ = Path(sys.argv[1]).resolve()
TF = RAIZ / "data/experiment/tanda_final"
T3, T5 = TF / "t3", TF / "t5"
L = lambda p: json.loads(Path(p).read_text(encoding="utf-8"))  # noqa: E731
d = L(T5 / "salidas/contado_tramo1_t5.json")
rs = L(RAIZ / "data/experiment/resellado_t0/condicion_4/medicion_tablero_r2b_rs1.json")
ve = L(T3 / "gate_decisiones/veredicto_gate_tf.json")
fg = L(T3 / "gate_decisiones/fuera_del_grafo_tf.json")
X4 = L(TF / "t4/tasas/tasas_t4_tramo3.json")
G = d["grafos"]
NOM = {"tf_tramo1": "tramo 1", "tf_tramo1_sincola": "tramo 1 sin cola", "acum60": "acumulado de las tandas 0 y 1 con el tramo 1",
       "acum60_sincola": "acumulado de las tandas 0 y 1 con el tramo 1 sin cola"}
assert list(G) == list(NOM), list(G)
mil = lambda n: f"{n:,}".replace(",", ".")  # noqa: E731
dec = lambda x, k=2: f"{x:.{k}f}".replace(".", ",")  # noqa: E731
CJ = "t5/salidas/contado_tramo1_t5.json"


def por_grafo(fn) -> str:
    return "; ".join(f"{NOM[g]} {fn(G[g], g)}" for g in G)


filas, ancla = {}, {}
filas[49] = por_grafo(lambda f, g: f"{dec(f['f49_obs10']['por_unidad'])} ({mil(f['f49_obs10']['extraccion'])} / {mil(f['f49_obs10']['unidades_e0'])})") + \
    f". Base re-sellada: diez {dec(rs['diez']['f49_obs10']['por_unidad'])} ({mil(rs['diez']['f49_obs10']['extraccion'])} / {mil(rs['diez']['f49_obs10']['unidades_e0'])})"
ancla[49] = f"{CJ}, grafos.<g>.f49_obs10; base: resellado_t0/condicion_4/medicion_tablero_r2b_rs1.json"
filas[50] = por_grafo(lambda f, g: f"{mil(f['f50_obs11']['aristas_cross_to'])} `remite_a` entre documentos ({mil(f['f50_obs11']['menciones_detectadas'])} menciones)") + \
    f". Base re-sellada: diez {rs['diez']['f50_obs11']['aristas_cross_to']}; desarrollo {rs['desarrollo']['f50_obs11']['aristas_cross_to']}"
ancla[50] = f"{CJ}, grafos.<g>.f50_obs11"
filas[51] = por_grafo(lambda f, g: f"{mil(f['f51_remisiones_por_origen']['condicion_definicion_potestad'])} remisiones desde Condicion, Definicion o "
                      f"Potestad; {f['f51_remisiones_por_origen']['referencia_con_origen_distinto_de_texto_ordenado']} `referencia` con origen "
                      f"distinto de TextoOrdenado")
ancla[51] = f"{CJ}, grafos.<g>.f51_remisiones_por_origen"
filas[52] = por_grafo(lambda f, g: f"{mil(f['f52_condiciones_sin_regla']['A_condicion_sin_arista_de_contenido'])} sin regla de "
                      f"{mil(f['f52_condiciones_sin_regla']['condicion'])} Condicion; aislados {mil(f['f52_aislados']['aislados_total'])}")
ancla[52] = f"{CJ}, grafos.<g>.f52_condiciones_sin_regla y f52_aislados"
filas[53] = por_grafo(lambda f, g: f["f53_falsas_parafrasis"] if isinstance(f["f53_falsas_parafrasis"], str) else
                      f"{f['f53_falsas_parafrasis']['hacia_cap_6_5_1_o_debajo']} hacia cap 6.5.1 o debajo, de "
                      f"{f['f53_falsas_parafrasis']['remisiones_desde_cap_8_2_3_3']} remisiones desde cap::8.2.3.3")
ancla[53] = f"{CJ}, grafos.<g>.f53_falsas_parafrasis"


def ej(f, g):
    e = f["f54_f55_suite"]["items"]["EJ-cla-5.1.1.1"]["estado"]
    fuera = fg["grafos"][g]["tanda_sola"] and fg["grafos"][g]["por_item"]["EJ-cla-5.1.1.1"]["alcance"] == "fuera del grafo"
    return e + (" (fuera del grafo: no cuenta, decisión 3)" if fuera else "")


filas[54] = por_grafo(ej)
ancla[54] = f"{CJ}, grafos.<g>.f54_f55_suite.items; t3/gate_decisiones/fuera_del_grafo_tf.json"
filas[55] = por_grafo(lambda f, g: f"{f['f54_f55_suite']['resumen']['resuelto']} / {f['f54_f55_suite']['resumen']['persiste']} / "
                      f"{f['f54_f55_suite']['resumen']['no_aplicable']}, contra r1 de resuelto a persiste "
                      f"{len(f['f54_f55_suite']['contra_entrada_r1']['de_resuelto_a_persiste'])}; no declaradas que cuentan en el gate: "
                      f"{len(ve['grafos'][g]['suite']['no_declaradas_que_cuentan'])}")
ancla[55] = f"{CJ}, grafos.<g>.f54_f55_suite; t3/gate_decisiones/veredicto_gate_tf.json"
EV2 = "no medido: residuo declarado, no medible en r2 sin correr el agente (EV2, que nunca se corre; laudo, §3, punto 6)"
for n in (56, 57, 58, 60):
    filas[n], ancla[n] = EV2, "causa: la meta de la fila (residuo declarado)"
filas[59] = ("no medido en el tramo 1 solo: la (12) se sorteó sobre el ensamblado de la tanda entera, como sin dividir (enmienda 9, "
             "punto 2); su cifra va en la columna de la tanda final")
ancla[59] = "causa: enmienda 9, §1, punto 2 (756a0394)"
filas[61] = por_grafo(lambda f, g: f"{f['f61_m10']['numerador']} de {mil(f['f61_m10']['denominador'])} (E0 con las partes)")
ancla[61] = f"{CJ}, grafos.<g>.f61_m10"


def cap12(f, g):
    x = f["f62_cap_1_2"]
    if isinstance(x, str):
        return x
    return "; ".join(f"{len(r['umbrales'])} umbral(es) " + ", ".join(f"{u['valor']} {u['unidad'] or ''} {u['moneda'] or ''}".strip()
                                                               for u in r["umbrales"]) for r in x["restricciones_cap_1_2"]) or "sin Restriccion"


filas[62] = por_grafo(lambda f, g: cap12(f, g) + (f"; BKL-0006 {f['f54_f55_suite']['items']['BKL-0006']['estado']}, "
                                                  f"BKL-0023 {f['f54_f55_suite']['items']['BKL-0023']['estado']}"))
ancla[62] = f"{CJ}, grafos.<g>.f62_cap_1_2 y f54_f55_suite.items"
filas[63] = por_grafo(lambda f, g: f["f63_tablas"] if isinstance(f["f63_tablas"], str) else
                      f"{sum(c['presente_r_pres'] for c in f['f63_tablas']['citas_d2'])} de {len(f['f63_tablas']['citas_d2'])} citas presentes (R-PRES)")
ancla[63] = f"{CJ}, grafos.<g>.f63_tablas"
filas[64] = por_grafo(lambda f, g: ", ".join(f"{k} {v['fuera_de_lista']}" for k, v in f["f64_valores_fuera_de_lista"].items()
                                             if k != "claves_fuera_de_la_definicion") +
                      f"; claves fuera {f['f64_valores_fuera_de_lista']['claves_fuera_de_la_definicion']['total']}") + \
    ". `properties_no_definidas`: en NO_ABRIR_conteos_t5.json (cuenta `copia_nota_e3`, bajo el cegamiento, y la marca de L-04)"
ancla[64] = f"{CJ}, grafos.<g>.f64_valores_fuera_de_lista"
filas[65] = por_grafo(lambda f, g: f"{mil(f['f65_sujetos']['con_sujeto_mencion'])} de {mil(f['f65_sujetos']['aristas_de_sujeto'])} "
                      f"con mención; propuestos en el grafo {f['f65_sujetos']['propuestos_en_el_grafo']}")
ancla[65] = f"{CJ}, grafos.<g>.f65_sujetos"
c = d["f66_catalogo"]
filas[66] = f"{len(c['solo_en_bloque'])} / {len(c['solo_en_catalogo'])} (ids solo en el bloque / solo en el catálogo; {c['ids_bloque']} en el bloque)"
ancla[66] = f"{CJ}, f66_catalogo"
filas[67] = por_grafo(lambda f, g: f"{mil(f['f67_cuantias']['sin_campo'])} sin campo de {mil(f['f67_cuantias']['con_cuantia'])} con cuantía")
ancla[67] = f"{CJ}, grafos.<g>.f67_cuantias"
filas[68] = por_grafo(lambda f, g: f"{mil(f['f68_omisiones']['unidades_con_omisiones'])} unidades con omisiones; sin categoría "
                      f"{f['f68_omisiones']['sin_categoria']}, sin tramo {f['f68_omisiones']['sin_tramo']}; registro del ensamblado "
                      f"{mil(f['f68_omisiones']['registro_del_ensamblado_filas'])} filas")
ancla[68] = f"{CJ}, grafos.<g>.f68_omisiones"
filas[69] = "en NO_ABRIR_conteos_t5.json: usa los reintentos de E3 (cegamiento de U-MED-VERIF, punto 9)"
ancla[69] = "causa: el cegamiento (punto 9 del «seguí» de T5)"
filas[70] = por_grafo(lambda f, g: f"{f['f70_colisiones_e0_r2']['total']} ids repetidos")
ancla[70] = f"{CJ}, grafos.<g>.f70_colisiones_e0_r2"
filas[71] = por_grafo(lambda f, g: f"{f['f71_no_verificadas_e3']['total']}")
ancla[71] = f"{CJ}, grafos.<g>.f71_no_verificadas_e3"
filas[72] = d["f72_lineas_mayusculas"]
ancla[72] = "causa: la fila lee la E0 legada, que la tanda final no tiene"
filas[73] = por_grafo(lambda f, g: f"{f['f73_pies_e0_r2']['chunks']} de {mil(f['f73_pies_e0_r2']['de'])} chunks ({f['f73_pies_e0_r2']['lineas']} líneas)")
ancla[73] = f"{CJ}, grafos.<g>.f73_pies_e0_r2"
filas[74] = por_grafo(lambda f, g: f"{f['f74_frecuencia']['a_frecuencia']} a `frecuencia`, {f['f74_frecuencia']['fuera_de_lista']} fuera "
                      f"de la lista (control con el reporte: {f['f74_frecuencia']['control_reporte']['coincide']})")
ancla[74] = f"{CJ}, grafos.<g>.f74_frecuencia"
assert sorted(filas) == list(range(49, 75)) and sorted(ancla) == list(range(49, 75))

tab = (RAIZ / "docs/tablero_correcciones.md").read_text(encoding="utf-8").splitlines()
sint = {n: tab[n - 1].strip("|").split("|")[0].strip() for n in range(49, 75)}
col = ["# La columna del tramo 1 en el tablero de correcciones: PROPUESTA (B6.1, tanda final, T5, punto 8)", "",
       "Generada por `tanda_final/t5/scripts/columnas_tablero_t5.py` desde `t5/salidas/contado_tramo1_t5.json` (el código de lo contado "
       "sin leer de T3, sobre una copia del repo: `t5/scripts/contado_tramo1_t5.py`). T3 no la contó: su `contado_sin_leer_tf.json` trae "
       "la tanda, el acumulado de las tres y sus sin cola, no el tramo 1. Cada celda dice el grafo: el tramo 1 (KG-TandaFinal-Tramo1-r2b), "
       "su sin cola, y el acumulado de las tandas 0 y 1 con el tramo 1 (KG-Acumulado-Tandas0y1yTramo1-r2b) y su sin cola. Sin la línea de "
       "base de la tanda 1. El tablero del repo no se toca.", "",
       "| fila | síntoma | Tramo 1 | ancla o causa |", "|---:|---|---|---|"]
for n in range(49, 75):
    col.append(f"| {n} | {sint[n]} | {filas[n].replace('|', '/')} | {ancla[n]} |")
(T5 / "columna_tramo1_tablero_PROPUESTA.md").write_text("\n".join(col) + "\n", encoding="utf-8")

# la columna de la tanda final: la de T3 tal cual, y la fila 59 desde T4
t3c = (T3 / "conteos_sin_leer/columna_tanda_final_tablero_tf.md").read_text(encoding="utf-8").splitlines()
celdas = {}
for ln in t3c:
    m = re.match(r"^\| (\d+) \| (.*) \| (.*) \|$", ln)
    if m:
        celdas[int(m.group(1))] = m.group(3)
assert sorted(celdas) == list(range(49, 75)), sorted(celdas)
O = X4["observacion:12"]
caps = "; ".join(f"{k} {v['n']}" for k, v in O["incorrectas_por_capa_pipeline"].items()) or "ninguna"
celdas[59] = (f"tanda final (grafo sin cola de la tanda, (10) sin `remite_a`): {O['cruda']['correctas']} correctas de {O['cruda']['de']} "
              f"({O['por_respuesta']['no decidible']} no decidibles, en el denominador); Wilson [{dec(O['cruda']['wilson'][0], 4)}; "
              f"{dec(O['cruda']['wilson'][1], 4)}]; incorrectas por `capa_pipeline`: {caps}; ponderada por celda "
              f"{dec(O['ponderada_por_celda']['tasa'], 4)}")
ancla_tf = {n: f"t3/conteos_sin_leer/columna_tanda_final_tablero_tf.md, fila {n} (de contado_sin_leer_tf.json)" for n in range(49, 75)}
ancla_tf[59] = "t4/tasas/tasas_t4_tramo3.json, `observacion:12` (la lectura de la autora, T4)"
for n in (56, 57, 58, 60, 72):
    ancla_tf[n] = "causa: la de la celda (T3)"
ancla_tf[69] = "causa: el cegamiento (en t3/NO_ABRIR_conteos_t3.json)"
col = ["# La columna «Tanda final» del tablero de correcciones: PROPUESTA (B6.1, tanda final, T5, punto 7)", "",
       "Generada por `tanda_final/t5/scripts/columnas_tablero_t5.py`. Las celdas de T3, tal cual (`t3/conteos_sin_leer/"
       "columna_tanda_final_tablero_tf.md`), y la que esperaba a T4, la fila 59, desde `t4/tasas/tasas_t4_tramo3.json`. Cada celda dice "
       "el grafo como en T3: tanda final (KG-TandaFinal-r2b), tanda final sin cola, acumulado de las tres tandas "
       "(KG-Acumulado-Tandas0y1yFinal-r2b) y acumulado sin cola. El tablero del repo no se toca.", "",
       "| fila | síntoma | Tanda final | ancla o causa |", "|---:|---|---|---|"]
for n in range(49, 75):
    col.append(f"| {n} | {sint[n]} | {celdas[n].replace('|', '/')} | {ancla_tf[n]} |")
(T5 / "columna_tanda_final_tablero_PROPUESTA.md").write_text("\n".join(col) + "\n", encoding="utf-8")
print((T5 / "columna_tramo1_tablero_PROPUESTA.md").read_text(encoding="utf-8"))
print((T5 / "columna_tanda_final_tablero_PROPUESTA.md").read_text(encoding="utf-8"))
