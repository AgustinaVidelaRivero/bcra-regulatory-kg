"""U-REEXT-T0, T3, punto 2: la columna «Después de r2: r2b (prompt y re-extracción)» del tablero de correcciones
(docs/tablero_correcciones.md, filas :49 a :74), con las cifras de medicion_tablero_r2b.json (misma regla y comando
que la columna r2a, [cN] de la sección «Comandos») y de controles_t3.json. Escribe solo la columna 9 de esas 26 filas
y comprueba que el resto del archivo queda igual. Lee y escribe las rutas que se le pasan (una copia, o el destino).

Uso: python -B escribir_columna_r2b.py --tablero ENTRADA --salida SALIDA --medicion JSON --controles JSON
"""
import argparse
import json
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("--tablero", type=Path, required=True)
ap.add_argument("--salida", type=Path, required=True)
ap.add_argument("--medicion", type=Path, required=True)
ap.add_argument("--controles", type=Path, required=True)
a = ap.parse_args()
M = json.loads(a.medicion.read_text(encoding="utf-8"))
K = json.loads(a.controles.read_text(encoding="utf-8"))
D, S = M["diez"], M["desarrollo"]
KD, KS = K["por_grafo"]["diez"], K["por_grafo"]["desarrollo"]
MED = "`data/experiment/reext_t0/t3/salida/medicion_tablero_r2b.json`"
CON = "`data/experiment/reext_t0/t3/salida/controles_t3.json`"
P = "**[06/10/2026, U-REEXT-T0 T3]**"


def n(x) -> str:
    return f"{x:,}".replace(",", ".") if isinstance(x, int) else str(x).replace(".", ",")


def obs10(f):
    c = f["f49_obs10"]
    return f"{n(c['por_unidad'])} ({n(c['extraccion'])} / {n(f['unidades_e0_r2b'])})"


def ns(d: dict) -> str:
    return ", ".join(f"{k} {n(v)}" for k, v in d.items())


s55 = lambda f: f["f54_f55_suite"]
cel = {}
cel[49] = (f"{P} diez {obs10(D)}; desarrollo {obs10(S)} [c26], sobre las unidades de la E0 r2b. Se restan las `remite_a` "
           f"({n(D['f49_obs10']['conteos']['remisiones'])} y {n(S['f49_obs10']['conteos']['remisiones'])}) y las `establecida_en` "
           f"derivadas ({n(D['f49_obs10']['conteos']['establecida_en_derivadas'])} y {n(S['f49_obs10']['conteos']['establecida_en_derivadas'])}); "
           f"sin las `cuarentena_flaggeada` ({D['f49_obs10']['conteos']['de_ellas_cuarentena_flaggeada']} y "
           f"{S['f49_obs10']['conteos']['de_ellas_cuarentena_flaggeada']}), {n(D['f49_obs10']['estricta_por_unidad'])} y "
           f"{n(S['f49_obs10']['estricta_por_unidad'])}; 0 relaciones sin verificar por E3. Control: sobre los sellados, "
           f"{n(D['f49_control_sellado_c1']['extraccion'])} y {n(S['f49_control_sellado_c1']['extraccion'])} ({MED}, `<grafo>.f49_obs10` y `f49_control_sellado_c1`)")
cel[50] = (f"{P} diez {n(D['f50_obs11']['aristas_cross_to'])} aristas `remite_a` entre documentos ({ns(D['f50_obs11']['cross_to_por_alcance'])}); "
           f"desarrollo {n(S['f50_obs11']['aristas_cross_to'])} ({ns(S['f50_obs11']['cross_to_por_alcance'])}) [c27]. Citas resueltas: "
           f"{n(D['f50_obs11']['citas_resueltas'])} y {n(S['f50_obs11']['citas_resueltas'])} (menciones detectadas "
           f"{n(D['f50_obs11']['menciones_detectadas'])} y {n(S['f50_obs11']['menciones_detectadas'])}). Control: sobre los sellados, "
           f"{D['f50_control_sellado']['aristas_cross_to']} y {S['f50_control_sellado']['aristas_cross_to']} aristas ({MED}, `f50_obs11`)")
cel[51] = (f"{P} Salen de Condicion, Definicion o Potestad {n(D['f51_remisiones_por_origen']['condicion_definicion_potestad'])} aristas "
           f"`remite_a` en diez ({ns({t: D['f51_remisiones_por_origen']['por_tipo_de_origen'][t] for t in ('Condicion', 'Definicion', 'Potestad')})}) "
           f"y {n(S['f51_remisiones_por_origen']['condicion_definicion_potestad'])} en desarrollo [c28]; `referencia` con origen distinto de "
           f"TextoOrdenado: {D['f51_remisiones_por_origen']['referencia_con_origen_distinto_de_texto_ordenado']} en los dos. La remisión de "
           f"`cla::5.1.1.1` a `cla::3.7` existe ({KD['b_remision_del_ejemplo']['remite_a_5_1_1_1_a_3_7']} aristas en cada grafo; control b de T3, {CON}) "
           f"({MED}, `f51_remisiones_por_origen`)")
cel[52] = (f"{P} {D['f52_aislados']['condicion_aisladas']} Condicion aisladas, de {n(D['f52_aislados']['condicion_total'])} en diez y de "
           f"{n(S['f52_aislados']['condicion_total'])} en desarrollo; los aislados son {D['f52_aislados']['aislados_total']} en diez "
           f"({ns(D['f52_aislados']['aislados_por_tipo'])}) y {S['f52_aislados']['aislados_total']} en desarrollo "
           f"({ns(S['f52_aislados']['aislados_por_tipo'])}): ningún nodo de contenido aislado [c3] ({MED}, `f52_aislados`)")
cel[53] = (f"{P} {D['f53_falsas_parafrasis']['hacia_cap_6_5_1_o_debajo']} remisiones de `cap::8.2.3.3` hacia `cap::6.5.1` o debajo, en diez y en "
           f"desarrollo: las {D['f53_falsas_parafrasis']['remisiones_desde_cap_8_2_3_3']} remisiones de sus {D['f53_falsas_parafrasis']['nodos_de_origen']} "
           f"nodos van a {ns(D['f53_falsas_parafrasis']['por_destino'])} [c3] ({MED}, `f53_falsas_parafrasis`)")
cel[54] = (f"{P} {s55(D)['items'].get('EJ-cla-5.1.1.1', {}).get('estado', '?').capitalize()} en diez y en desarrollo [c29]: dos `condicion_de` "
           f"Condicion → Operacion, verificadas por E3, y dos `remite_a` a `cla::3.7`. La Excepcion de `cla::5.1.1.1` existe; su `exceptua` "
           f"hacia la Operacion la rechazó el validador por firma (control c de T3, {CON}) "
           f"(`ens_<grafo>_r2b/suite_perfil_r2.json`, ítem `EJ-cla-5.1.1.1`)")
r1d = s55(D)["contra_entrada_r1"]
cel[55] = (f"{P} Los 46 ítems: diez {s55(D)['particion_46']['estados'].get('resuelto', 0)} / {s55(D)['particion_46']['estados'].get('persiste', 0)} / "
           f"{s55(D)['particion_46']['estados'].get('no_aplicable', 0)}, desarrollo {s55(S)['particion_46']['estados'].get('resuelto', 0)} / "
           f"{s55(S)['particion_46']['estados'].get('persiste', 0)} / {s55(S)['particion_46']['estados'].get('no_aplicable', 0)} [c29]. Contra la entrada de r1, "
           f"pasan de resuelto a persiste {', '.join(r1d['de_resuelto_a_persiste'])} y a no_aplicable {', '.join(r1d['de_resuelto_a_no_aplicable'])}. "
           f"Contra la entrada r2b sellada (`00fa231`), con su `kg_sha256` completado solo en una copia (en el repo es null hasta que lo "
           f"complete la autora): {s55(D)['regresion']['n_regresiones']} regresiones en cada grafo (BKL-0006 y BKL-0023 a no_aplicable; RT-C5-3, "
           f"RT-C6-1, RT-C6-2 y LN-5 a persiste), {s55(D)['regresion']['coinciden']} coinciden. Los 68: diez {s55(D)['resumen']['resuelto']} / "
           f"{s55(D)['resumen']['persiste']} / {s55(D)['resumen']['no_aplicable']}, desarrollo {s55(S)['resumen']['resuelto']} / "
           f"{s55(S)['resumen']['persiste']} / {s55(S)['resumen']['no_aplicable']} ({MED}, `f54_f55_suite`)")
NOAG = "No medible en r2b: exige correr el agente (USD > 0, EV2), y el gate de r2 nunca usa EV2 (laudo §3.1, punto 7)"
cel[56] = NOAG
cel[57] = NOAG
cel[58] = NOAG
cel[59] = ("No medible en T3: la muestra de 30 aristas pide una lectura con quién lee decidido antes (checklist P15, Q12), fuera "
           "de U-REEXT-T0")
cel[60] = "No medible en r2b: exige correr el agente con juez (USD > 0, EV2), y el gate de r2 nunca usa EV2 (laudo §3.1, punto 7)"
cel[61] = (f"{P} diez {D['f61_m10']['numerador']} de {n(D['f61_m10']['denominador'])}; desarrollo {S['f61_m10']['numerador']} de "
           f"{n(S['f61_m10']['denominador'])} [c30], sobre la E0 r2b con las dos partes de `cap::4.2.1.2` (`data/experiment/reext_t0/t3/e0_con_partes.py`). "
           f"Ninguna de las 4 unidades mudas de la tanda 0 lo es en r2b; `cap::4.2.1.2` cortó también en 16.384 y se partió por corte "
           f"(`ens_<grafo>_r2b/r2/declaracion_partes_y_reparadas.json`) ({MED}, `f61_m10`)")
r62 = D["f62_cap_1_2"]["restricciones_cap_1_2"]
cel[62] = (f"{P} Sin afirmación falsa en diez y en desarrollo: las dos Restricciones de `cap::1.2` dicen en su descripción los montos "
           f"del PDF (bancos 5.000 millones; restantes entidades 2.500), pero sus elementos de umbral no llevan valor (comparación "
           f"`no_determinada`, tramo verificado exacto) [c10]; `BKL-0006` y `BKL-0023` «no_aplicable» en la suite, porque no hay monto de la "
           f"tabla en la lista de umbrales [c29] ({MED}, `f62_cap_1_2`). Regresión contra la entrada sellada, que esperaba «resuelto»")
cel[63] = (f"{P} Las 5 citas de los criterios de EV2F-031 (`ric:7.2`, 4) y EV2F-032 (`ric:9.2`, 1) están presentes por R-PRES en diez y "
           f"en desarrollo [c31] ({MED}, `f63_tablas`). La lectura de «Incumplimientos reiterados» no se repite acá")
v64 = lambda f: f["f64_valores_fuera_de_lista"]
cel[64] = (f"{P} Diez: Restriccion.tipo {v64(D)['Restriccion.tipo']['fuera_de_lista']}; Comunicacion.tipo {v64(D)['Comunicacion.tipo']['fuera_de_lista']} "
           f"(nodos sin `tipo`, sin marca ni original); Obligacion.tipo 0 ({v64(D)['Obligacion.tipo']['normalizados_con_original_guardado']} normalizados, "
           f"con el original); Obligacion.frecuencia {v64(D)['Obligacion.frecuencia']['fuera_de_lista']} (marcados) [c32]. Desarrollo: "
           f"{v64(S)['Restriccion.tipo']['fuera_de_lista']}, {v64(S)['Comunicacion.tipo']['fuera_de_lista']} (sin tipo), 0 y "
           f"{v64(S)['Obligacion.frecuencia']['fuera_de_lista']}. Claves fuera de la definición r2: 0. Residuo: los Comunicacion sin `tipo` "
           f"cuentan como fuera de lista sin tratar ({MED}, `f64_*`)")
f65 = lambda f: f["f65_sujetos"]
cel[65] = (f"{P} Mención: {n(f65(D)['con_sujeto_mencion'])} de {n(f65(D)['aristas_de_sujeto'])} aristas de sujeto la llevan en diez "
           f"({ns(f65(D)['mencion_verificada'])}) y {n(f65(S)['con_sujeto_mencion'])} de {n(f65(S)['aristas_de_sujeto'])} en desarrollo "
           f"({ns(f65(S)['mencion_verificada'])}). No mapeables: el registro tiene {f65(D)['registro_no_mapeados']['filas']} filas en diez "
           f"({ns(f65(D)['registro_no_mapeados']['por_estado'])}) y {f65(S)['registro_no_mapeados']['filas']} en desarrollo "
           f"({ns(f65(S)['registro_no_mapeados']['por_estado'])}); 2 propuestos sin fila en diez y 1 en desarrollo (S28) [c33] ({MED}, `f65_sujetos`)")
c66 = M["f66_catalogo"]
cel[66] = (f"{P} 0 / 0: el bloque de catálogo del prompt r2b (`bloque_catalogo_r2.txt`, `{c66['bloque_sha256'][:8]}…`) tiene los mismos "
           f"{c66['ids_bloque']} ids que el catálogo r2 sin sus {c66['lapidas']} lápidas (`{c66['catalogo_sha256'][:8]}…`) [c34] "
           f"({MED}, `f66_catalogo`)")
f67 = lambda f: f["f67_cuantias"]
cel[67] = (f"{P} Sin elemento de umbral: diez {f67(D)['sin_campo']} de {f67(D)['con_cuantia']} con cuantía (Obligacion "
           f"{f67(D)['sin_campo_por_tipo']['Obligacion']}); desarrollo {f67(S)['sin_campo']} de {f67(S)['con_cuantia']} [c35]. Límites relativos "
           f"de S18, aparte: {D['f67_limites_relativos_s18']['sin_lista_ni_marca']} de {D['f67_limites_relativos_s18']['restricciones_limite_cuantitativo']} y "
           f"{S['f67_limites_relativos_s18']['sin_lista_ni_marca']} de {S['f67_limites_relativos_s18']['restricciones_limite_cuantitativo']} Restricciones "
           f"`limite_cuantitativo` sin lista ni marca, ninguna con cuantía de [c14] ({MED}, `f67_*`)")
f68 = lambda f: f["f68_omisiones"]
cel[68] = (f"{P} Las omisiones las emite E1 con categoría y tramo: {n(f68(D)['omisiones'])} en {n(f68(D)['unidades_con_omisiones'])} unidades en "
           f"diez ({ns(f68(D)['por_categoria'])}) y {n(f68(S)['omisiones'])} en desarrollo; {f68(D)['sin_categoria']} sin categoría y "
           f"{f68(D)['sin_tramo']} sin tramo en cada grafo; el registro del ensamblado (`omisiones.jsonl`) tiene {n(f68(D)['registro_del_ensamblado_filas'])} "
           f"y {n(f68(S)['registro_del_ensamblado_filas'])} filas; LN-7 «{f68(D)['ln7']['estado']}» en los dos [c29] ({MED}, `f68_omisiones`)")
cel[69] = (f"{P} 0 unidades sin el crudo del reintento persistido: {D['f69_crudo_reintento_en_la_salida']['unidades_con_reintento']} unidades con "
           f"reintento del ratchet en la salida de U-REEXT-T0 (los diez TOs), todas con su crudo en `reintentos_e3.jsonl`; la cadena r2 leyó "
           f"{D['f69_crudo_reintento']['origen_crudo'].get('reintento_1:companero', 0)} crudos de reintento del archivo compañero en diez y "
           f"{S['f69_crudo_reintento']['origen_crudo'].get('reintento_1:companero', 0)} en desarrollo, ninguno de la caché ({MED}, `f69_*`)")
cel[70] = (f"{P} {D['f70_colisiones_e0_r2']['total']} ids repetidos en la E0 r2b de la tanda 0 ({n(D['f73_pies_e0_r2']['de'])} unidades); "
           f"`ids_desambiguados.json` no existe [c18] ({MED}, `f70_colisiones_e0_r2`)")
cel[71] = (f"{P} {D['f71_no_verificadas_e3']['total']} en diez y {S['f71_no_verificadas_e3']['total']} en desarrollo: las relaciones de la "
           f"matriz ampliada pasaron por E3 (`aristas_no_verificadas_e3.total` del reporte del ensamblado; control a de T3, {CON}) [c19] "
           f"({MED}, `f71_no_verificadas_e3`)")
l72 = M["f72_lineas_mayusculas"]
cel[72] = (f"{P} {l72['contenido_descartado_en_e0_r2']} líneas de contenido descartadas en la E0 r2b: conserva las "
           f"{l72['contenido_conservado_en_e0_r2']} que la E0 legada descarta (`encabezados_conservados.json` de `salida_tanda0_r2b`) [c36]; "
           f"la E0 r2b es la de la extracción (manifiesto `tanda0_10tos_r2b.json`, `rutas.e0_salida`) ({MED}, `f72_lineas_mayusculas`)")
cel[73] = (f"{P} {D['f73_pies_e0_r2']['chunks']} chunks con pie en la E0 r2b (de {n(D['f73_pies_e0_r2']['de'])} en diez y "
           f"{n(S['f73_pies_e0_r2']['de'])} en desarrollo), la E0 de la extracción r2b; la E0 legada sigue con "
           f"{D['f73_control_e0_legada']['chunks']} [c22] ({MED}, `f73_pies_e0_r2` y `f73_control_e0_legada`)")
cel[74] = (f"{P} {D['f74_frecuencia']['a_frecuencia']} plazos a `frecuencia` en diez y {S['f74_frecuencia']['a_frecuencia']} en desarrollo: "
           f"ninguna Obligacion con plazo heredado sin cuantía temporal mandado a `frecuencia`; coincide con los contadores del "
           f"ensamblado (`umbrales.frecuencia_desde_plazo` = 0) [c37] ({MED}, `f74_frecuencia`)")

lineas = a.tablero.read_text(encoding="utf-8").split("\n")
nuevas = list(lineas)
for i in range(49, 75):
    celdas = lineas[i - 1].split("|")
    assert len(celdas) == 12, (i, len(celdas))      # «| a | … | j |»: 10 columnas, 12 trozos
    assert celdas[9].strip() == "", f"la celda r2b de la línea {i} no está vacía"
    texto = cel[i]
    assert "|" not in texto, i
    celdas[9] = f" {texto} "
    nuevas[i - 1] = "|".join(celdas)
for i, (x, y) in enumerate(zip(lineas, nuevas), 1):
    if x != y:
        assert 49 <= i <= 74
        cx, cy = x.split("|"), y.split("|")
        assert cx[:9] == cy[:9] and cx[10:] == cy[10:], i
a.salida.write_text("\n".join(nuevas), encoding="utf-8")
print("celdas escritas:", sum(1 for x, y in zip(lineas, nuevas) if x != y))
