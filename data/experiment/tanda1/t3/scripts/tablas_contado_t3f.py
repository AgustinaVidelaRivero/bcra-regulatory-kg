"""B6.1, tanda 1, T3, punto 6: la columna «Tanda 1» del tablero de correcciones (docs/tablero_correcciones.md, filas :49 a :74) y las
tablas de lo contado sin leer, por script, desde tanda1/t3/conteos_sin_leer/contado_sin_leer_t3f.json y las líneas de base del
re-sellado. Cada fila del tablero lleva su cifra o la causa por la que no se midió. El tablero del repo no se toca. Solo lee; escribe
conteos_sin_leer/columna_tanda1_tablero_t3f.md y conteos_sin_leer/tablas_contado_t3f.md bajo <raíz> y los imprime.
Grafos: veinte (KG-Tanda1-Veinte-r2b), veinte sin cola (el evaluado), acumulado de las tandas 0 y 1 y acumulado sin cola.
Uso: python3 -I -B tablas_contado_t3f.py <raíz>
"""
import json
import sys
from pathlib import Path

RAIZ = Path(sys.argv[1]).resolve()
T3 = RAIZ / "data/experiment/tanda1/t3"
CS = T3 / "conteos_sin_leer"
L = lambda p: json.loads(Path(p).read_text(encoding="utf-8"))  # noqa: E731
d = L(CS / "contado_sin_leer_t3f.json")
rs = L(RAIZ / "data/experiment/resellado_t0/condicion_4/medicion_tablero_r2b_rs1.json")
vb = L(RAIZ / "data/experiment/resellado_t0/condicion_4/vigilancias_contables_rs1.json")["vigilancias"]
cb = L(RAIZ / "data/experiment/resellado_t0/salidas/cola_y_poblacion_rs1.json")
ub = L(RAIZ / "data/experiment/reresolucion_catalogo/salidas/r2_1_medicion.json")["umbral"]
ve = L(T3 / "gate_decisiones/veredicto_gate_t3f.json")
fg = L(T3 / "gate_decisiones/fuera_del_grafo_t3f.json")
G = d["grafos"]
NOM = {"veinte": "veinte", "veinte_sincola": "veinte sin cola", "acumulado": "acumulado", "acumulado_sincola": "acumulado sin cola"}
mil = lambda n: f"{n:,}".replace(",", ".")  # noqa: E731
dec = lambda x, k=2: f"{x:.{k}f}".replace(".", ",")  # noqa: E731


def por_grafo(fn) -> str:
    return "; ".join(f"{NOM[g]} {fn(G[g], g)}" for g in G)


filas = {}
filas[49] = por_grafo(lambda f, g: f"{dec(f['f49_obs10']['por_unidad'])} ({mil(f['f49_obs10']['extraccion'])} / {mil(f['f49_obs10']['unidades_e0'])})") + \
    f". Base re-sellada: diez {dec(rs['diez']['f49_obs10']['por_unidad'])} ({mil(rs['diez']['f49_obs10']['extraccion'])} / {mil(rs['diez']['f49_obs10']['unidades_e0'])})"
filas[50] = por_grafo(lambda f, g: f"{mil(f['f50_obs11']['aristas_cross_to'])} `remite_a` entre documentos ({mil(f['f50_obs11']['menciones_detectadas'])} menciones)") + \
    f". Base re-sellada: diez {rs['diez']['f50_obs11']['aristas_cross_to']}; desarrollo {rs['desarrollo']['f50_obs11']['aristas_cross_to']}"
filas[51] = por_grafo(lambda f, g: f"{mil(f['f51_remisiones_por_origen']['condicion_definicion_potestad'])} remisiones desde Condicion, Definicion o "
                      f"Potestad; {f['f51_remisiones_por_origen']['referencia_con_origen_distinto_de_texto_ordenado']} `referencia` con origen "
                      f"distinto de TextoOrdenado")
filas[52] = por_grafo(lambda f, g: f"{mil(f['f52_condiciones_sin_regla']['A_condicion_sin_arista_de_contenido'])} sin regla de "
                      f"{mil(f['f52_condiciones_sin_regla']['condicion'])} Condicion; aislados {mil(f['f52_aislados']['aislados_total'])}")
filas[53] = por_grafo(lambda f, g: f["f53_falsas_parafrasis"] if isinstance(f["f53_falsas_parafrasis"], str) else
                      f"{f['f53_falsas_parafrasis']['hacia_cap_6_5_1_o_debajo']} hacia cap 6.5.1 o debajo, de "
                      f"{f['f53_falsas_parafrasis']['remisiones_desde_cap_8_2_3_3']} remisiones desde cap::8.2.3.3")


def ej(f, g):
    e = f["f54_f55_suite"]["items"]["EJ-cla-5.1.1.1"]["estado"]
    fuera = fg["grafos"][g]["tanda_sola"] and fg["grafos"][g]["por_item"]["EJ-cla-5.1.1.1"]["alcance"] == "fuera del grafo"
    return e + (" (fuera del grafo: no cuenta, decisión 3)" if fuera else "")


filas[54] = por_grafo(ej)
filas[55] = por_grafo(lambda f, g: f"{f['f54_f55_suite']['resumen']['resuelto']} / {f['f54_f55_suite']['resumen']['persiste']} / "
                      f"{f['f54_f55_suite']['resumen']['no_aplicable']}, contra r1 de resuelto a persiste "
                      f"{len(f['f54_f55_suite']['contra_entrada_r1']['de_resuelto_a_persiste'])}; no declaradas que cuentan en el gate: "
                      f"{len(ve['grafos'][g]['suite']['no_declaradas_que_cuentan'])}")
EV2 = "no medido: residuo declarado, no medible en r2 sin correr el agente (EV2, que nunca se corre; laudo, §3, punto 6)"
filas[56] = filas[57] = filas[58] = filas[60] = EV2
filas[59] = "no medido en T3: es una lectura asistida de T4. Su población y su sorteo por celda están en tanda1/t3/muestras/"
filas[61] = por_grafo(lambda f, g: f"{f['f61_m10']['numerador']} de {mil(f['f61_m10']['denominador'])} (E0 con las partes)")


def cap12(f, g):
    x = f["f62_cap_1_2"]
    if isinstance(x, str):
        return x
    return "; ".join(f"{len(r['umbrales'])} umbral(es) " + ", ".join(f"{u['valor']} {u['unidad'] or ''} {u['moneda'] or ''}".strip()
                                                               for u in r["umbrales"]) for r in x["restricciones_cap_1_2"]) or "sin Restriccion"


filas[62] = por_grafo(lambda f, g: cap12(f, g) + (f"; BKL-0006 {f['f54_f55_suite']['items']['BKL-0006']['estado']}, "
                                                  f"BKL-0023 {f['f54_f55_suite']['items']['BKL-0023']['estado']}"))
filas[63] = por_grafo(lambda f, g: f["f63_tablas"] if isinstance(f["f63_tablas"], str) else
                      f"{sum(c['presente_r_pres'] for c in f['f63_tablas']['citas_d2'])} de {len(f['f63_tablas']['citas_d2'])} citas presentes (R-PRES)")
filas[64] = por_grafo(lambda f, g: ", ".join(f"{k} {v['fuera_de_lista']}" for k, v in f["f64_valores_fuera_de_lista"].items()
                                             if k != "claves_fuera_de_la_definicion") +
                      f"; claves fuera {f['f64_valores_fuera_de_lista']['claves_fuera_de_la_definicion']['total']}") + \
    ". `properties_no_definidas`: en NO_ABRIR_conteos_t3.json (cuenta `copia_nota_e3`, bajo el cegamiento, y la marca de L-04)"
filas[65] = por_grafo(lambda f, g: f"{mil(f['f65_sujetos']['con_sujeto_mencion'])} de {mil(f['f65_sujetos']['aristas_de_sujeto'])} "
                      f"con mención; propuestos en el grafo {f['f65_sujetos']['propuestos_en_el_grafo']}")
c = d["f66_catalogo"]
filas[66] = f"{len(c['solo_en_bloque'])} / {len(c['solo_en_catalogo'])} (ids solo en el bloque / solo en el catálogo; {c['ids_bloque']} en el bloque)"
filas[67] = por_grafo(lambda f, g: f"{mil(f['f67_cuantias']['sin_campo'])} sin campo de {mil(f['f67_cuantias']['con_cuantia'])} con cuantía")
filas[68] = por_grafo(lambda f, g: f"{mil(f['f68_omisiones']['unidades_con_omisiones'])} unidades con omisiones; sin categoría "
                      f"{f['f68_omisiones']['sin_categoria']}, sin tramo {f['f68_omisiones']['sin_tramo']}; registro del ensamblado "
                      f"{mil(f['f68_omisiones']['registro_del_ensamblado_filas'])} filas")
filas[69] = "en NO_ABRIR_conteos_t3.json: usa los reintentos de E3 (cegamiento de U-MED-VERIF, punto 8)"
filas[70] = por_grafo(lambda f, g: f"{f['f70_colisiones_e0_r2']['total']} ids repetidos")
filas[71] = por_grafo(lambda f, g: f"{f['f71_no_verificadas_e3']['total']}")
filas[72] = d["f72_lineas_mayusculas"]
filas[73] = por_grafo(lambda f, g: f"{f['f73_pies_e0_r2']['chunks']} de {mil(f['f73_pies_e0_r2']['de'])} chunks ({f['f73_pies_e0_r2']['lineas']} líneas)")
filas[74] = por_grafo(lambda f, g: f"{f['f74_frecuencia']['a_frecuencia']} a `frecuencia`, {f['f74_frecuencia']['fuera_de_lista']} fuera "
                      f"de la lista (control con el reporte: {f['f74_frecuencia']['control_reporte']['coincide']})")

tab = (RAIZ / "docs/tablero_correcciones.md").read_text(encoding="utf-8").splitlines()
col = ["# La columna «Tanda 1» del tablero de correcciones (B6.1, tanda 1, T3, punto 6)", "",
       "Generada por `tanda1/t3/scripts/tablas_contado_t3f.py` desde `conteos_sin_leer/contado_sin_leer_t3f.json`. El tablero del repo "
       "(`docs/tablero_correcciones.md`) no se toca. Cada celda dice el grafo: veinte (KG-Tanda1-Veinte-r2b), veinte sin cola (el "
       "evaluado), acumulado de las tandas 0 y 1, y acumulado sin cola.", "",
       "| fila | síntoma | Tanda 1 |", "|---:|---|---|"]
for n in range(49, 75):
    sint = tab[n - 1].strip("|").split("|")[0].strip()
    col.append(f"| {n} | {sint} | {filas[n].replace('|', '/')} |")
texto_col = "\n".join(col) + "\n"
(CS / "columna_tanda1_tablero_t3f.md").write_text(texto_col, encoding="utf-8")

w = ["#### Tabla C1. Observaciones (10) y (11) contra sus líneas de base re-selladas (pre-registro, §5.2)", "",
     "| grafo | unidades de E0 | (10) aristas de extracción | (10) por unidad | (11) `remite_a` entre documentos | menciones |",
     "|---|---:|---:|---:|---:|---:|"]
for g, f in G.items():
    w.append(f"| {NOM[g]} | {mil(f['unidades_e0_r2b'])} | {mil(f['f49_obs10']['extraccion'])} | {dec(f['f49_obs10']['por_unidad'])} | "
             f"{mil(f['f50_obs11']['aristas_cross_to'])} | {mil(f['f50_obs11']['menciones_detectadas'])} |")
for b in ("diez", "desarrollo"):
    w.append(f"| base re-sellada: {b} | {mil(rs[b]['f49_obs10']['unidades_e0'])} | {mil(rs[b]['f49_obs10']['extraccion'])} | "
             f"{dec(rs[b]['f49_obs10']['por_unidad'])} | {rs[b]['f50_obs11']['aristas_cross_to']} | {mil(rs[b]['f50_obs11']['menciones_detectadas'])} |")
w += ["", "#### Tabla C2. Vigilancias (4), (5), (8) y (9) contra sus líneas de base re-selladas (§5.3)", "",
      "| grafo | (4) un TextoOrdenado por TO | (5) requisito_de_estructura / normalizados | (8) sujeto_propuesto / sujeto_id (tasa %) | "
      "(9) emisiones en E1 / aristas en el kg |", "|---|---|---|---|---|"]
for g, f in G.items():
    v = f["vigilancias"]
    w.append(f"| {NOM[g]} | {v['4']['uno_por_to']} | {v['5']['total']['tipo_obligacion_requisito_de_estructura']} / "
             f"{v['5']['total']['tipo_obligacion_normalizados']} | {v['8']['sujeto_propuesto']} / {mil(v['8']['sujeto_id'])} "
             f"({dec(v['8']['tasa_pct'])}) | {v['9']['emisiones_E1_total']} / {v['9']['aristas_en_kg']} |")
for b in ("diez", "desarrollo"):
    v8 = vb["8"][b]
    w.append(f"| base re-sellada: {b} | {all(x['uno_por_to'] for k, x in vb['4']['por_grafo'].items() if k.startswith(b))} | "
             f"{sum((x or 0) for x in vb['5']['tipo_obligacion_requisito_de_estructura'].values())} / "
             f"{sum((x or 0) for x in vb['5']['tipo_obligacion_normalizados'].values())} (los diez TOs) | {v8['sujeto_propuesto']} / "
             f"{mil(v8['sujeto_id'])} ({dec(v8['tasa_pct'])}) | {sum(vb['9']['emisiones_E1_por_to'].values())} (los diez TOs) / "
             f"{vb['9']['aristas_en_kg'][b]} |")
w += ["", "#### Tabla C3. La cola (§5.4 b), contra los 69 de 2.439 del re-sellado", "",
      "| grafo | cola | de unidades de E0 | % | por estado | aceptadas (los tres estados juntos) | en el grafo |", "|---|---:|---:|---:|---|---:|---|"]
for g, f in G.items():
    c = f["cola"]
    gr = c["grafo"]
    eng = (f"{gr['descartadas_por_el_ensamblado_sin_cola']} descartadas por el ensamblado" if gr["con_cola"] is False
           else f"{gr['nodos_con_la_marca']} nodos y {gr['aristas_con_la_marca']} aristas con la marca")
    w.append(f"| {NOM[g]} | {c['cola']} | {mil(f['unidades_e0_r2b'])} | {dec(100 * c['cola'] / f['unidades_e0_r2b'], 1)} | "
             + ", ".join(f"{k} {v}" for k, v in c["cola_por_estado"].items()) + f" | {mil(c['aceptadas_los_tres_estados_juntos'])} | {eng} |")
w.append(f"| base re-sellada (diez) | {cb['linea_de_base_pre_registro_tanda1']['grafo_re_sellado'].split()[0]} | "
         f"{mil(int(cb['linea_de_base_pre_registro_tanda1']['grafo_re_sellado'].split()[-1]))} | "
         f"{dec(100 * int(cb['linea_de_base_pre_registro_tanda1']['grafo_re_sellado'].split()[0]) / int(cb['linea_de_base_pre_registro_tanda1']['grafo_re_sellado'].split()[-1]), 1)} | "
         + ", ".join(f"{k} {v}" for k, v in cb["cola_despues_por_estado"].items()) + " | — | — |")
w.append("\nEl umbral de atención es 6 % (§5.4 b). Las unidades en `finales.jsonl` son " + ", ".join(
    f"{NOM[g]} {mil(f['cola']['unidades_en_finales'])}" for g, f in G.items()) + " (las partes por corte cuentan aparte); otros estados: "
         + ", ".join(f"{NOM[g]} {f['cola']['otros_estados'] or 'ninguno'}" for g, f in G.items()) + ".")
w.append("\nLa cola por TO (veinte): " + ", ".join(f"{k} {v}" for k, v in G["veinte"]["cola"]["cola_por_to"].items()) + ".")
w += ["", "#### Tabla C4. El catálogo al cierre (§5.5): claves con la mención verificada en cuarentena en 2 unidades o más", "",
      "| registro | filas en cuarentena | verificadas | claves | claves con 2 unidades o más | en 2 TOs o más |", "|---|---:|---:|---:|---:|---:|"]
for g, u in d["catalogo_al_cierre"].items():
    w.append(f"| {NOM[g]} | {u['cuarentena']} | {u['verificadas_en_cuarentena']} | {u['claves']} | {u['n_claves_con_2_unidades_o_mas']} | "
             f"{len(u['claves_en_2_tos_o_mas'])} |")
for b in ("diez", "diez_sincola"):
    w.append(f"| base de la tanda 0: {b} (r2_1_medicion.json) | {ub[b]['cuarentena']} | {ub[b]['verificadas_en_cuarentena']} | {ub[b]['claves']} | "
             f"{len(ub[b]['claves_con_2_unidades_o_mas'])} | {len(ub[b]['claves_en_2_tos_o_mas'])} |")
w.append("\nLas claves y sus formas están en `contado_sin_leer_t3f.json` (`catalogo_al_cierre`). Su lectura y aprobación es de la autora "
         "(enmienda 4, §1, punto 3); cuántas relaciones resuelve cada versión del catálogo se mide después de la re-resolución (punto 5).")
p = d["pozos_L02_L04"]
w += ["", "#### Tabla C5. Los pozos de L-02 y L-04 (§5.4 d; cegamiento, punto 8: solo si llegan a 30)", "",
      f"- L-02 ({p['L-02']['de']}): llega a 30: {p['L-02']['llega_a_30']}.",
      "- L-04 (nodos Comunicacion con `tipo_no_derivable`): " + "; ".join(f"{NOM[g]} llega a 30: {x['llega_a_30']}" for g, x in p["L-04"].items()) + ".",
      "- Las cuentas, en `NO_ABRIR_conteos_t3.json`.", "",
      f"Control de las funciones importadas (las del re-sellado sobre KG-Tanda0-Diez-r2b-rs1 contra su medición): "
      f"{d['control_contra_el_re_sellado']['todos']} en las {len(d['control_contra_el_re_sellado']['iguales'])} filas controladas."]
texto = "\n".join(w) + "\n"
(CS / "tablas_contado_t3f.md").write_text(texto, encoding="utf-8")
print(texto_col)
print(texto)
