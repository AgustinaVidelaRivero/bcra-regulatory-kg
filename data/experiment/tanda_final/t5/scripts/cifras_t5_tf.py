"""B6.1, tanda final, T5 (pre-registro firmado en 4de7f2a7, §5 y §7, con sus notas en 27bfaeb5 y 86541475; enmienda 9 al protocolo
entre tandas, 756a0394, §1, punto 1): las cifras del reporte de cierre y del sello del tramo 1, por script. Solo lee; escribe
<salida>/cifras_t5.json, sin hora ni rutas absolutas, para que dos corridas a dos salidas den los mismos bytes.

  1. El costo (§3 y §7), desde reextraccion_v2/corpus_tanda_final/salida_r2b/estado_corpus.json (de cada fase cerrada, solo `gasto_usd`:
     el resumen de E3 trae el desglose por estado, que no se lee) y presupuesto_compartido.json:
       - el real, por etapa (E1 y E3), por TO y por tramo (los tramos de tanda_final/preregistro/tramos_tanda_final.json), y el total
         contra el presupuesto compartido. E3 va como una sola cifra por TO, con los reintentos adentro (cegamiento). Los pasos sin API
         (E0, E2 y el validador, el ensamblado, T3, las lecturas de T4 y T5), en 0, declarados;
       - el estimado: por TO, el del manifiesto (`limites.estimado_usd`, el repartido por caracteres de la nota 27bfaeb5); por tramo y en
         total, el del §3 (U × 0,021115; el total, más las líneas de alcance, A3.costo_lineas_usd) y el repartido al lado; por etapa, con
         las tarifas por etapa del manifiesto (e1 0,010135 más las líneas de alcance; e3 0,010980);
       - la desviación (real − estimado y real / estimado) por etapa, por tramo, por TO y total;
       - la tanda 1 al lado: el hueco T5.costo_real_tanda1, tal como lo define tanda_final/preregistro/huecos_preregistro_tanda_final.json
         (la clave `para_el_preregistro_tanda_final` de data/experiment/tanda1/t5/salidas/costo_t5.json, leída en 0c2befad con git show).
         Es lo único de la tanda 1 que se lee.
  2. Los ids de modelo, desde t5/salidas/ids_modelo_t5.json (ids_modelo_t5.py).
  3. Los volúmenes: por tramo, las unidades, las aceptadas (los tres estados juntos), la cola y los errores, desde
     t2/resumen_t2_final.json (resumen_t2.py, que no desglosa por estado); los nodos y aristas de los ocho ensamblados, desde
     t3/salidas/doble_corrida_tf.json.
  4. T4: las cifras de t4/tasas/tasas_t4_tramo3.json que van al reporte, tal cual.
  5. El tablero: cada fila de la columna «Tanda final» contra su meta (docs/tablero_correcciones.md, columna «Meta»), con un criterio
     escrito por fila; y los hallazgos (protocolo entre tandas, §2, :71-100; pre-registro de la tanda 1, §5.6), con su eje A, su eje B, su
     `capa_pipeline` y su propuesta de entrada del backlog. La causa de las incorrectas sale de la lectura de la autora; la de las 16 de
     las aceptadas no ítems, de su clasificación (t4/clasificacion_freno/), que no se abre ni se usa.
  6. El sello del tramo 1: su costo (del punto 1), y los sha256 de sus carpetas (t5/salidas/carpetas_tramo1_t5.json) y de la entrada del
     acumulado de 60 rearmada (t5/salidas/entrada_acumulado_60_t5.json).
Los ids de nodos y aristas que no son de unidades a la vista (t3/muestras/unidades_a_la_vista_T4.json) van por su código: los primeros 12
caracteres del sha256 del id.
Uso: python3 -I -B cifras_t5_tf.py <raíz> <salida>
"""
import csv
import hashlib
import json
import math
import re
import subprocess
import sys
from collections import Counter, OrderedDict
from pathlib import Path

sys.dont_write_bytecode = True
R, OUT = Path(sys.argv[1]).resolve(), Path(sys.argv[2])
TF = R / "data/experiment/tanda_final"
REX = R / "data/experiment/reextraccion_v2"
SAL = REX / "corpus_tanda_final/salida_r2b"
MAN = REX / "manifiestos/tanda_final_98tos_r2b.json"
L = lambda p: json.loads(Path(p).read_text(encoding="utf-8"))  # noqa: E731
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()  # noqa: E731
codigo = lambda s: hashlib.sha256(s.encode()).hexdigest()[:12]  # noqa: E731
r6 = lambda x: round(float(x), 6)  # noqa: E731
r4 = lambda x: round(float(x), 4)  # noqa: E731
Z = 1.959964
cm = lambda x, k=4: f"{x:.{k}f}".replace(".", ",")  # noqa: E731  (la coma decimal, en el texto)
sn = lambda b: "sí" if b else "no"  # noqa: E731
mil = lambda n: f"{n:,}".replace(",", ".")  # noqa: E731


def wilson(k: int, n: int) -> list:
    p = k / n
    c = p + Z * Z / (2 * n)
    m = Z * math.sqrt(p * (1 - p) / n + Z * Z / (4 * n * n))
    return [r4((c - m) / (1 + Z * Z / n)), r4((c + m) / (1 + Z * Z / n))]


ENTRADAS = OrderedDict()
for rel in ("data/experiment/reextraccion_v2/corpus_tanda_final/salida_r2b/estado_corpus.json",
            "data/experiment/reextraccion_v2/corpus_tanda_final/salida_r2b/presupuesto_compartido.json",
            "data/experiment/reextraccion_v2/manifiestos/tanda_final_98tos_r2b.json",
            "data/experiment/tanda_final/preregistro/tramos_tanda_final.json",
            "data/experiment/tanda_final/preregistro/huecos_preregistro_tanda_final.json",
            "data/experiment/tanda_final/preregistro/preregistro_tanda_final_derivada_T1.huecos.json",
            "data/experiment/tanda_final/t2/resumen_t2_final.json", "data/experiment/tanda_final/t3/salidas/doble_corrida_tf.json",
            "data/experiment/tanda_final/t3/conteos_sin_leer/contado_sin_leer_tf.json",
            "data/experiment/tanda_final/t3/gate_decisiones/veredicto_gate_tf.json",
            "data/experiment/tanda_final/t4/tasas/tasas_t4_tramo3.json", "data/experiment/tanda_final/t5/salidas/ids_modelo_t5.json",
            "data/experiment/tanda_final/t5/salidas/carpetas_tramo1_t5.json",
            "data/experiment/tanda_final/t5/salidas/entrada_acumulado_60_t5.json",
            "data/experiment/tanda_final/t5/salidas/contado_tramo1_t5.json", "docs/tablero_correcciones.md",
            "data/experiment/tanda_final/t3/muestras/unidades_a_la_vista_T4.json"):
    ENTRADAS[rel] = sha(R / rel)
out = OrderedDict([("entradas", ENTRADAS)])

# 1. El costo
tramos = L(TF / "preregistro/tramos_tanda_final.json")
T1, T2 = list(tramos["tramo_1_tos"]), list(tramos["tramo_2_tos"])
TRAMO = {t: "tramo_1" for t in T1} | {t: "tramo_2" for t in T2}
U = {"tramo_1": tramos["tramo_1"]["unidades"], "tramo_2": tramos["tramo_2"]["unidades"]}
assert len(TRAMO) == 98 and sum(U.values()) == tramos["tanda_final"]["unidades"] == 4951
est = L(SAL / "estado_corpus.json")
fc = est["fases_cerradas"]
assert est["fase_actual"] is None and set(fc) == {f"{t}:{e}" for t in TRAMO for e in ("e1", "e3")}
real = OrderedDict((t, OrderedDict((e, r6(fc[f"{t}:{e}"]["gasto_usd"])) for e in ("e1", "e3"))) for t in T1 + T2)
pres = L(SAL / "presupuesto_compartido.json")
man = L(MAN)
estm = man["limites"]["estimado_usd"]
assert set(estm) == set(TRAMO)
TARIFA, E1U, E3U = 0.021115, 0.010135, 0.010980
assert abs(E1U + E3U - TARIFA) < 1e-12
hu = L(TF / "preregistro/preregistro_tanda_final_derivada_T1.huecos.json")["valores"]["A3.costo_lineas_usd"]["valor"]
LINEAS = float(".".join(re.match(r"USD (\d+),(\d+),", hu).groups()))
por_to = OrderedDict()
for t in T1 + T2:
    re_, es_ = real[t], estm[t]
    rt, et = re_["e1"] + re_["e3"], es_["e1"] + es_["e3"]
    por_to[t] = OrderedDict([("tramo", TRAMO[t]), ("real", OrderedDict([("e1", re_["e1"]), ("e3", re_["e3"]), ("total", r6(rt))])),
                             ("estimado_manifiesto", OrderedDict([("e1", es_["e1"]), ("e3", es_["e3"]), ("total", r6(et))])),
                             ("desviacion", OrderedDict([("e1", r6(re_["e1"] - es_["e1"])), ("e3", r6(re_["e3"] - es_["e3"])),
                                                         ("total", r6(rt - et)), ("razon_total", r4(rt / et))]))])


def suma(tos, f) -> float:
    return sum(f(t) for t in tos)


por_tramo = OrderedDict()
for tr, tos in (("tramo_1", T1), ("tramo_2", T2)):
    re1, re3 = suma(tos, lambda t: real[t]["e1"]), suma(tos, lambda t: real[t]["e3"])
    m1, m3 = suma(tos, lambda t: estm[t]["e1"]), suma(tos, lambda t: estm[t]["e3"])
    s3 = U[tr] * TARIFA
    por_tramo[tr] = OrderedDict([
        ("tos", len(tos)), ("unidades", U[tr]),
        ("real", OrderedDict([("e1", r6(re1)), ("e3", r6(re3)), ("total", r6(re1 + re3))])),
        ("estimado_s3", OrderedDict([("e1", r6(U[tr] * E1U)), ("e3", r6(U[tr] * E3U)), ("total", r6(s3)),
                                     ("como", "U del tramo × 0,021115 (§3), sin las líneas de alcance, como las cifras del §3")])),
        ("estimado_repartido", OrderedDict([("e1", r6(m1)), ("e3", r6(m3)), ("total", r6(m1 + m3)),
                                            ("como", "la suma del estimado por TO del manifiesto (nota 27bfaeb5)")])),
        ("desviacion_contra_s3", OrderedDict([("e1", r6(re1 - U[tr] * E1U)), ("e3", r6(re3 - U[tr] * E3U)), ("total", r6(re1 + re3 - s3)),
                                              ("razon_total", r4((re1 + re3) / s3))])),
        ("desviacion_contra_repartido", OrderedDict([("e1", r6(re1 - m1)), ("e3", r6(re3 - m3)), ("total", r6(re1 + re3 - m1 - m3)),
                                                     ("razon_total", r4((re1 + re3) / (m1 + m3)))]))])
re1, re3 = suma(T1 + T2, lambda t: real[t]["e1"]), suma(T1 + T2, lambda t: real[t]["e3"])
m1, m3 = suma(T1 + T2, lambda t: estm[t]["e1"]), suma(T1 + T2, lambda t: estm[t]["e3"])
UT = sum(U.values())
s3e1, s3e3 = UT * E1U + LINEAS, UT * E3U
total = OrderedDict([
    ("real", OrderedDict([("e1", r6(re1)), ("e3", r6(re3)), ("total", r6(re1 + re3))])),
    ("presupuesto_compartido", OrderedDict([("gasto_usd", pres["gasto_usd"]), ("tope_usd", pres["tope_usd"]),
                                            ("suma_de_las_fases_menos_el_presupuesto", r6(re1 + re3 - pres["gasto_usd"])),
                                            ("proporcion_del_tope", r4(pres["gasto_usd"] / pres["tope_usd"]))])),
    ("estimado_s3", OrderedDict([("e1", r6(s3e1)), ("e3", r6(s3e3)), ("total", r6(s3e1 + s3e3)),
                                 ("como", "U × 0,021115 más las líneas de alcance (A3.costo_lineas_usd, USD 0,209440; §3); por etapa, con "
                                          "e1 0,010135 más las líneas y e3 0,010980 (las tarifas del manifiesto)")])),
    ("estimado_repartido", OrderedDict([("e1", r6(m1)), ("e3", r6(m3)), ("total", r6(m1 + m3)),
                                        ("estimado_total_usd_del_estado", est["estimado_total_usd"])])),
    ("desviacion_contra_s3", OrderedDict([("e1", r6(re1 - s3e1)), ("e3", r6(re3 - s3e3)), ("total", r6(re1 + re3 - s3e1 - s3e3)),
                                          ("razon_total", r4((re1 + re3) / (s3e1 + s3e3)))])),
    ("desviacion_contra_repartido", OrderedDict([("e1", r6(re1 - m1)), ("e3", r6(re3 - m3)), ("total", r6(re1 + re3 - m1 - m3)),
                                                 ("razon_total", r4((re1 + re3) / (m1 + m3)))]))])
SIN_API = OrderedDict((k, 0.0) for k in ("E0", "E2 y el validador", "ensamblado", "T3 (ensamblados, gate, registro y lo contado)",
                                         "T4 (sorteos, material y lecturas)", "T5"))
hue = L(TF / "preregistro/huecos_preregistro_tanda_final.json")["T5.costo_real_tanda1"]
assert hue["tipo"] == "json" and hue["clave"] == "para_el_preregistro_tanda_final"
t1c = json.loads(subprocess.run(["git", "--no-optional-locks", "-C", str(R), "show", f"{hue['commit']}:{hue['fuente']}"],
                                capture_output=True, check=True).stdout)
tanda1 = OrderedDict([("hueco", "T5.costo_real_tanda1"), ("fuente", hue["fuente"]), ("commit", hue["commit"]), ("clave", hue["clave"]),
                      ("valor", t1c[hue["clave"]])])
del t1c
out["costo"] = OrderedDict([("por_to", por_to), ("por_tramo", por_tramo), ("total", total),
                            ("pasos_sin_api_usd", SIN_API), ("tanda1", tanda1)])
res2 = L(TF / "t2/resumen_t2_final.json")
out["costo"]["control_con_resumen_t2"] = OrderedDict([
    ("gasto_por_to_sumado_usd", res2["total"]["gasto_por_to_sumado_usd"]),
    ("igual_a_la_suma_de_las_fases", abs(res2["total"]["gasto_por_to_sumado_usd"] - (re1 + re3)) < 5e-6),
    ("por_to_igual", all(abs(res2["por_to"][t]["gasto_usd"] - (real[t]["e1"] + real[t]["e3"])) < 5e-6 for t in TRAMO))])

# 2. Los ids de modelo
out["ids_de_modelo"] = L(TF / "t5/salidas/ids_modelo_t5.json")

# 3. Los volúmenes
vol = OrderedDict()
for tr, tos in (("tramo_1", T1), ("tramo_2", T2), ("tanda", T1 + T2)):
    vol[tr] = OrderedDict((k, sum(res2["por_to"][t][k] for t in tos))
                          for k in ("unidades", "unidades_con_partes", "aceptadas", "cola", "errores", "sin_destino", "ids_repetidos"))
    vol[tr]["tos"] = len(tos)
assert vol["tanda"]["unidades"] == res2["total"]["unidades"] and vol["tanda"]["cola"] == res2["total"]["cola"]
assert vol["tramo_1"]["unidades"] == U["tramo_1"] and vol["tramo_2"]["unidades"] == U["tramo_2"]
errores_ids = sorted(OrderedDict.fromkeys(t for t in TRAMO if res2["por_to"][t]["errores"]))
vol["tos_con_error_definitivo"] = errores_ids
dc = L(TF / "t3/salidas/doble_corrida_tf.json")["doble_corrida"]
NOMBRES = {"tf98": "KG-TandaFinal-r2b", "tf98_sincola": "KG-TandaFinal-r2b-sincola", "tf_tramo1": "KG-TandaFinal-Tramo1-r2b",
           "tf_tramo1_sincola": "KG-TandaFinal-Tramo1-r2b-sincola", "acum128": "KG-Acumulado-Tandas0y1yFinal-r2b",
           "acum128_sincola": "KG-Acumulado-Tandas0y1yFinal-r2b-sincola", "acum60": "KG-Acumulado-Tandas0y1yTramo1-r2b",
           "acum60_sincola": "KG-Acumulado-Tandas0y1yTramo1-r2b-sincola"}
vol["ensamblados"] = OrderedDict((NOMBRES[k], OrderedDict([("carpeta", v["carpeta"]), ("nodos", v["nodos"]), ("aristas", v["aristas"]),
                                                          ("kg_sha256", v["kg_sha256"][0]),
                                                          ("dos_corridas_iguales", v["kg_sha256"][0] == v["kg_sha256"][1])]))
                                 for k, v in dc.items())
out["volumenes"] = vol

# 4. T4
X4 = L(TF / "t4/tasas/tasas_t4_tramo3.json")
out["t4"] = OrderedDict([("fuente", "data/experiment/tanda_final/t4/tasas/tasas_t4_tramo3.json"),
                         ("aceptadas_no_items_sobre_60", X4["aceptadas_no_items_sobre_60"]["regla"]),
                         ("aceptadas", {s: X4["aceptadas"][s]["regla"] for s in ("items", "no_items")}),
                         ("atencion_RI", X4["atencion_RI"]["regla"]), ("cola", X4["cola"]["regla"]),
                         ("vigilancias", {m: X4["vigilancias"][m]["cruda"] for m in X4["vigilancias"]}),
                         ("observacion_12", X4["observacion:12"]["cruda"]), ("lineas_de_base", X4["lineas_de_base"])])

# 5. El tablero contra su meta, y los hallazgos
cs = L(TF / "t3/conteos_sin_leer/contado_sin_leer_tf.json")["grafos"]
tf, ac = cs["tf98"], cs["acum128"]
tab = (R / "docs/tablero_correcciones.md").read_text(encoding="utf-8").splitlines()
meta = {n: [c.strip() for c in tab[n - 1].strip().strip("|").split("|")][4] for n in range(49, 75)}
sint = {n: [c.strip() for c in tab[n - 1].strip().strip("|").split("|")][0] for n in range(49, 75)}
fila = OrderedDict()


def f_(n, estado, cifra, criterio):
    fila[n] = OrderedDict([("sintoma", sint[n]), ("meta", meta[n]), ("cifra", cifra), ("criterio", criterio), ("estado", estado)])


f_(49, "sin meta numérica", f"{cm(tf['f49_obs10']['por_unidad'], 2)} aristas de extracción por unidad",
   "la meta dice «Sin meta numérica»: la cifra se vigila como descriptivo")
f_(50, "no se decide con lo contado", f"{tf['f50_obs11']['aristas_cross_to']} `remite_a` entre documentos",
   "la meta es de precisión (toda `remite_a` sostenida por cita y destino) y la lectura de T4 no la mide aparte")
f_(51, "cumple", f"{tf['f51_remisiones_por_origen']['referencia_con_origen_distinto_de_texto_ordenado']} `referencia` con origen "
                 "distinto de TextoOrdenado", "ninguna `referencia` sale de Condicion, Potestad ni Definicion")
c52 = tf["f52_condiciones_sin_regla"]
f_(52, "cumple", f"{c52['vigente_condicion_sin_ninguna_arista']} Condicion sin ninguna arista; {c52['A_condicion_sin_arista_de_contenido']} "
                 f"sin regla de {c52['condicion']}, declaradas por causa; aislados {tf['f52_aislados']['aislados_total']} "
                 f"({', '.join(f'{k} {v}' for k, v in tf['f52_aislados']['aislados_por_tipo'].items())})",
   "la parte medible de la meta, cero Condicion sin `establecida_en` ni ninguna arista, da 0; las sin regla se declaran por causa. "
   "Los aislados no son Condicion")
f_(53, "cumple" if ac["f53_falsas_parafrasis"]["hacia_cap_6_5_1_o_debajo"] == 0 else "no cumple",
   f"acumulado de las tres: {ac['f53_falsas_parafrasis']['hacia_cap_6_5_1_o_debajo']} hacia cap 6.5.1 o debajo",
   "la tanda no tiene cap; se mide en el acumulado")
f_(54, "cumple" if ac["f54_f55_suite"]["items"]["EJ-cla-5.1.1.1"]["estado"] == "resuelto" else "no cumple",
   f"acumulado de las tres: {ac['f54_f55_suite']['items']['EJ-cla-5.1.1.1']['estado']}", "la tanda no tiene cla; se mide en el acumulado")
ve = L(TF / "t3/gate_decisiones/veredicto_gate_tf.json")["grafos"]
f_(55, "cumple" if not ve["tf98"]["suite"]["no_declaradas_que_cuentan"] and not ve["acum128"]["suite"]["no_declaradas_que_cuentan"] else "no cumple",
   f"no declaradas que cuentan: tanda {len(ve['tf98']['suite']['no_declaradas_que_cuentan'])}, acumulado "
   f"{len(ve['acum128']['suite']['no_declaradas_que_cuentan'])}; declaradas: laudo {len(ve['acum128']['suite']['declaradas_laudo'])}, "
   f"autora {len(ve['acum128']['suite']['declaradas_autora'])}", "0 regresiones que cuentan en el gate; las declaradas, aparte (hallazgos)")
for n in (56, 57, 58, 60):
    f_(n, "residuo declarado", "no medido", "la meta declara el residuo: no medible en r2 sin correr el agente")
O12 = X4["observacion:12"]
f_(59, "no cumple", f"{O12['cruda']['correctas']} correctas de {O12['cruda']['de']}; {O12['por_respuesta']['incorrecta']} incorrecta "
                    f"({', '.join(O12['incorrectas_por_capa_pipeline'])})",
   "la meta cerró la fila con la precisión de L2; una incorrecta de la lectura es un hallazgo (protocolo, §2)")
f_(61, "no cumple" if tf["f61_m10"]["numerador"] else "cumple", f"{tf['f61_m10']['numerador']} de {tf['f61_m10']['denominador']}",
   "la meta pide cero unidades con error definitivo por corte y M10 en 0")
f_(62, "cumple" if all(ac["f54_f55_suite"]["items"][b]["estado"] == "resuelto" for b in ("BKL-0006", "BKL-0023")) else "no se decide con lo contado",
   f"acumulado: BKL-0006 {ac['f54_f55_suite']['items']['BKL-0006']['estado']}, BKL-0023 {ac['f54_f55_suite']['items']['BKL-0023']['estado']}",
   "la tanda no tiene cap; la meta pide BKL-0006 y BKL-0023 aplicables y en «resuelto»")
f_(63, "cumple" if all(c["presente_r_pres"] for c in ac["f63_tablas"]["citas_d2"]) else "no cumple",
   f"acumulado: {sum(c['presente_r_pres'] for c in ac['f63_tablas']['citas_d2'])} de {len(ac['f63_tablas']['citas_d2'])} citas presentes",
   "la tanda no tiene los TOs de las citas; se mide en el acumulado")
v64 = tf["f64_valores_fuera_de_lista"]
sin_tratar = {k: v["sin_marca_ni_original"] for k, v in v64.items() if k != "claves_fuera_de_la_definicion"}
f_(64, "cumple, con el residuo que la meta declara" if {k: v for k, v in sin_tratar.items() if v and k != "Comunicacion.tipo"} == {} else "no cumple",
   f"sin marca ni original: {', '.join(f'{k} {v}' for k, v in sin_tratar.items())}; claves fuera {v64['claves_fuera_de_la_definicion']['total']}",
   "fuera de lista sin tratar = sin marca y sin el original guardado; la meta declara como residuo de r2b la Comunicacion sin `tipo`")
f_(65, "cumple" if tf["f65_sujetos"]["con_sujeto_mencion"] == tf["f65_sujetos"]["aristas_de_sujeto"] else "no cumple",
   f"{tf['f65_sujetos']['con_sujeto_mencion']} de {tf['f65_sujetos']['aristas_de_sujeto']} con mención", "toda relación con sujeto lleva su mención")
c66 = L(TF / "t3/conteos_sin_leer/contado_sin_leer_tf.json")["f66_catalogo"]
f_(66, "cumple" if not c66["solo_en_bloque"] and not c66["solo_en_catalogo"] else "no cumple",
   f"{len(c66['solo_en_bloque'])} / {len(c66['solo_en_catalogo'])}", "una sola fuente: 0 / 0")
f_(67, "no cumple" if tf["f67_cuantias"]["sin_campo"] else "cumple",
   f"{tf['f67_cuantias']['sin_campo']} sin campo de {tf['f67_cuantias']['con_cuantia']} con cuantía "
   f"({', '.join(f'{k} {v}' for k, v in tf['f67_cuantias']['sin_campo_por_tipo'].items() if v)})",
   "toda cuantía con elemento de umbral o con marca; el residuo que la meta declara es el de diez")
f_(68, "cumple" if tf["f68_omisiones"]["sin_categoria"] == 0 and tf["f68_omisiones"]["sin_tramo"] <= 1 else "no cumple",
   f"sin categoría {tf['f68_omisiones']['sin_categoria']}, sin tramo {tf['f68_omisiones']['sin_tramo']}",
   "toda omisión con categoría y tramo; la meta declara un residuo de 1 sin tramo por grafo")
f_(69, "no se decide: bajo el cegamiento", "en t3/NO_ABRIR_conteos_t3.json", "usa los reintentos de E3")
f_(70, "cumple" if tf["f70_colisiones_e0_r2"]["total"] == 0 else "no cumple", f"{tf['f70_colisiones_e0_r2']['total']}", "0 ids repetidos")
f_(71, "cumple" if tf["f71_no_verificadas_e3"]["total"] == 0 else "no cumple", f"{tf['f71_no_verificadas_e3']['total']}", "0 sin verificar por E3")
f_(72, "no aplica", "no medido", "la fila lee la E0 legada, que la tanda final no tiene")
f_(73, "cumple" if tf["f73_pies_e0_r2"]["chunks"] == 0 else "no cumple", f"{tf['f73_pies_e0_r2']['chunks']} de {tf['f73_pies_e0_r2']['de']}",
   "0 chunks con pie")
f_(74, "cumple" if tf["f74_frecuencia"]["a_frecuencia"] == 0 else "no cumple", f"{tf['f74_frecuencia']['a_frecuencia']} a `frecuencia`",
   "0 plazos sin cuantía mandados a `frecuencia`")
assert sorted(fila) == list(range(49, 75))
out["tablero_contra_su_meta"] = OrderedDict((str(n), v) for n, v in fila.items())

# las lecturas de la autora: los errores, con la causa de la lectura
LA1 = L(TF / "t4/lectura_asistida/lectura_asistida_t4_tramo1.json")["propuestas"]
regla = {(m, p["id"]): p["regla"] for m, ps in LA1.items() for p in ps}


def marcada(p: Path) -> list:
    with open(p, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter=";"))


def errores(m: str, causa_de_la_autora: bool) -> list:
    out_ = []
    for f in marcada(TF / f"t4/lectura_autora/{m}_marcada.csv"):
        if f["veredicto_autora"] not in ("con error", "dudosa"):
            continue
        x = OrderedDict([("id", f["id"]), ("celda", f["celda"]), ("veredicto", f["veredicto_autora"]), ("ficha", f["ficha"])])
        if causa_de_la_autora:
            x["causa"] = "en la clasificación de la autora (t4/clasificacion_freno/)"
        elif f["veredicto_autora"] == f["propuesta"]:
            x["regla"] = regla[(m, f["id"])]
            x["causa"] = f"la de la propuesta, que la lectura confirma: {f['justificacion']}"
        else:
            x["regla"] = None
            x["causa"] = f"la nota de la autora: {f['nota_autora']}"
        out_.append(x)
    return out_


err = OrderedDict()
err["cola"] = errores("cola", False)
err["aceptadas_items"] = errores("aceptadas_items", False)
amp = marcada(TF / "t4/ampliacion/lectura_autora/aceptadas_no_items_ampliacion_marcada.csv")
err["aceptadas_no_items_60"] = errores("aceptadas_no_items", True) + [
    OrderedDict([("id", f["id"]), ("celda", f["celda"]), ("veredicto", f["veredicto_autora"]), ("ficha", f["ficha"]),
                 ("causa", "en la clasificación de la autora (t4/clasificacion_freno/)")])
    for f in amp if f["veredicto_autora"] in ("con error", "dudosa")]
assert len(err["aceptadas_no_items_60"]) == X4["aceptadas_no_items_sobre_60"]["regla"]["errores"]
assert len(err["cola"]) == X4["cola"]["regla"]["errores"] and len(err["aceptadas_items"]) == X4["aceptadas"]["items"]["regla"]["errores"]
out["errores_de_las_lecturas"] = err

# las vigilancias leídas contra su línea de base (la de la tanda 1, de la versión derivada): «fuera» si la línea de base cae fuera del
# Wilson de la tanda final; es un hallazgo si además la cifra empeora
lb_txt = X4["lineas_de_base"]["vigilancias_y_12"]["tanda1"]
base_v = {f"vigilancia:{a}": (int(k), int(n)) for a, k, n in re.findall(r"\((\d+)\) (\d+) [^;]*? de (\d+)", lb_txt) if a != "12"}
assert sorted(base_v) == ["vigilancia:1", "vigilancia:2", "vigilancia:3", "vigilancia:7"], base_v
vig = OrderedDict()
for m, (k0, n0) in base_v.items():
    c = X4["vigilancias"][m]["cruda"]
    p0 = k0 / n0
    fuera = not (c["wilson"][0] <= p0 <= c["wilson"][1])
    vig[m] = OrderedDict([("tanda_final", f"{c['k']} de {c['n']}"), ("wilson", c["wilson"]), ("tanda1", f"{k0} de {n0}"),
                          ("fuera_de_la_linea_de_base", fuera), ("empeora", c["tasa"] > p0), ("hallazgo", fuera and c["tasa"] > p0)])
out["vigilancias_contra_su_linea_de_base"] = OrderedDict([
    ("criterio", "propuesta de la ejecutora: una vigilancia leída está fuera de su línea de base si la de la tanda 1 cae fuera del Wilson "
                 "de la tanda final; es un hallazgo si además la cifra empeora. Las contadas sin leer, (4), (5), (8) y (9), no tienen "
                 "intervalo: van con su cifra y la de la tanda 1 al lado, sin juicio"),
    ("fuente_de_la_tanda1", "t4/tasas/tasas_t4_tramo3.json, lineas_de_base.vigilancias_y_12.tanda1 (la versión derivada)"),
    ("leidas", vig)])

# los hallazgos
H = []


def h(id_, tipo, que, cifra, ancla, eje_a, eje_b, capa, causa, backlog, propuesta=None):
    H.append(OrderedDict([("id", id_), ("tipo", tipo), ("que", que), ("cifra", cifra), ("ancla", ancla), ("eje_A", eje_a),
                          ("eje_B", eje_b), ("capa_pipeline", capa), ("causa", causa), ("backlog", backlog),
                          ("propuesta", propuesta)]))


mud = tf["f61_m10"]["mudos"]
h("H-T5-01", "fila del tablero que no cumple su meta (61)", "Unidades cortadas o mudas",
  f"{tf['f61_m10']['numerador']} de {mil(tf['f61_m10']['denominador'])}: " + ", ".join(mud) + "; la misma es el error definitivo de T2",
  "t3/conteos_sin_leer/contado_sin_leer_tf.json, grafos.tf98.f61_m10; t2/resumen_t2_final.json (errores)",
  "F08c (reintento por salida de E1 mal formada): «E1 y E3 de las afectadas»", "se difiere: el runner es código sellado (pre-registro, §8)",
  ["corrida"], "la de BKL-0050: el reintento por forma de E1 corta en 8.192 sin escalar", "ya está: BKL-0050")
h("H-T5-02", "fila del tablero que no cumple su meta (67)", "Cuantías sin campo estructurado",
  fila[67]["cifra"], "t3/conteos_sin_leer/contado_sin_leer_tf.json, grafos.tf98.f67_cuantias",
  "F15b (umbrales del ensamblado): «solo código sobre lo guardado»",
  "puede corregirse con código antes del sello del grafo evaluado (re-aplicación única); sin una corrección lista, se difiere",
  ["ensamblado"], "lo contado no la da: son nodos con cuantía en la descripción y sin `umbral` ni `plazo` (la regex de la fila, c14)",
  "propuesta", "PROP-T5-01")
inc = O12["incorrectas_por_capa_pipeline"]
h("H-T5-03", "incorrecta de la lectura de T4: observación (12)", "una arista `aplica_a` al rol de alcance de otro TO",
  f"{O12['por_respuesta']['incorrecta']} de {O12['cruda']['de']}; arista " +
  ", ".join(codigo(e["id"]) for v in inc.values() for e in v["elementos"]) + " (código: los 12 primeros caracteres del sha256 del id)",
  "t4/tasas/tasas_t4_tramo3.json, observacion:12.incorrectas_por_capa_pipeline; " + ", ".join(e["ficha"] for v in inc.values() for e in v["elementos"]),
  "F15d (sujetos por relación, reglas R1 a R4): «solo código sobre lo guardado»",
  "puede corregirse con código antes del sello del grafo evaluado; sin una corrección lista, se difiere",
  list(inc), "la de la lectura de la autora: «incorrecta (catálogo)», el destino es el rol de alcance de otro TO, que la resolución tomó "
             "de la sugerencia del modelo (criterio O12-sujeto-de-otro-TO)", "propuesta", "PROP-T5-02")
h("H-T5-04", "incorrectas de la lectura de T4: aceptadas no ítems (sobre las 60), con el freno", "las unidades con error de no ítems",
  f"{len(err['aceptadas_no_items_60'])} de 60; tasa ponderada {cm(X4['aceptadas_no_items_sobre_60']['regla']['tasa_ponderada'])}; freno por "
  f"la atención sobre las 60: {sn(X4['aceptadas_no_items_sobre_60']['regla']['freno_por_atencion_sobre_60'])}",
  "t4/tasas/tasas_t4_tramo3.json, aceptadas_no_items_sobre_60; las marcadas de las 30 y de la ampliación",
  "según la clasificación de la autora", "según la clasificación de la autora (registro de decisiones, §89)", None,
  "en la clasificación de la autora (t4/clasificacion_freno/)", "la decide la clasificación")
NOMR = lambda r: r if r else "veredicto cambiado por la autora (causa en su nota)"  # noqa: E731
porr = Counter(NOMR(x.get("regla")) for x in err["aceptadas_items"])
h("H-T5-05", "incorrectas de la lectura de T4: aceptadas ítems", "las unidades con error de ítems",
  f"{len(err['aceptadas_items'])} de 30; por la regla de la propuesta que la lectura confirma: " + ", ".join(f"{k} {v}" for k, v in sorted(porr.items())),
  "t4/lectura_autora/aceptadas_items_marcada.csv; errores_de_las_lecturas.aceptadas_items",
  "según la capa de cada una", "según la capa de cada una", None,
  "la de cada unidad, de la lectura de la autora (errores_de_las_lecturas.aceptadas_items); la planilla de T4 no tiene la capa",
  "propuesta", "PROP-T5-03")
porc = Counter(NOMR(x.get("regla")) for x in err["cola"])
h("H-T5-06", "incorrectas de la lectura de T4: la cola, con la regla del 25 % disparada", "las unidades con error de la cola",
  f"{len(err['cola'])} de 30; tasa ponderada {cm(X4['cola']['regla']['tasa_ponderada'])}, Wilson [{cm(X4['cola']['regla']['wilson'][0])}; "
  f"{cm(X4['cola']['regla']['wilson'][1])}]; la regla del 25 % se dispara: {sn(X4['cola']['regla']['regla_del_25_se_dispara'])}; por la regla de la propuesta que la lectura confirma: " +
  ", ".join(f"{k} {v}" for k, v in sorted(porc.items())),
  "t4/tasas/tasas_t4_tramo3.json, cola; t4/lectura_autora/cola_marcada.csv",
  "según la capa de cada una", "la cola no entra al grafo sin cola; la regla del 25 % es cifra y vigilancia, no freno", None,
  "la de cada unidad, de la lectura de la autora (errores_de_las_lecturas.cola); la planilla de T4 no tiene la capa", "propuesta", "PROP-T5-04")
for m, v in vig.items():
    if v["hallazgo"]:
        h("H-T5-07", f"vigilancia fuera de su línea de base ({m})", "Condicion que lleva un deber explícito",
          f"{v['tanda_final']}, Wilson [{cm(v['wilson'][0])}; {cm(v['wilson'][1])}]; tanda 1 {v['tanda1']}", "t4/tasas/tasas_t4_tramo3.json, vigilancias",
          "F06 (prefijo de E1): «todo»", "se difiere: un cambio de prompt queda fuera del grafo que evalúa B6.3 (protocolo, §2, eje B)",
          ["E1-prompt"], "la de la lectura: la Condicion recoge un deber que el texto formula como tal (V1-deber); la tipa E1",
          "propuesta", "PROP-T5-05")
for i, rid in enumerate(ve["acum128"]["suite"]["declaradas_laudo"] + ve["acum128"]["suite"]["declaradas_autora"], 1):
    dl = rid in ve["acum128"]["suite"]["declaradas_laudo"]
    h(f"H-T5-08.{i}", "regresión declarada de T3", rid, "declarada en el gate de T3 (acumulado de las tres)",
      "t3/gate_decisiones/veredicto_gate_tf.json, grafos.acum128.suite." + ("declaradas_laudo" if dl else "declaradas_autora"),
      "nada: residuo declarado" if dl else "la de BKL-0048", "residuo declarado (laudo)" if dl else "se difiere (BKL-0048)",
      None if dl else ["E1-prompt"], "la del laudo" if dl else "la de BKL-0048", "no" if dl else "ya está: BKL-0048")
out["hallazgos"] = H

# las propuestas de entrada del backlog (no se escribe en el backlog)
ids_sin = tf["f67_cuantias"]["ids_sin_campo"]
P = [
    OrderedDict([("id", "PROP-T5-01"), ("fuente", "T5_tanda_final"), ("diagnostico", "deteccion_determinista"),
                 ("grafo", "KG-TandaFinal-r2b (y su sin cola)"), ("nodos_objetivo", [codigo(x) for x in ids_sin]),
                 ("capa_pipeline", ["ensamblado"]), ("causa", f"{len(ids_sin)} nodos con cuantía en la descripción y sin `umbral` ni `plazo` "
                  "(fila 67 del tablero); la meta los admite solo como el residuo de diez"),
                 ("remedio", "a diagnosticar: la regla de umbrales del ensamblado (F15b) sobre esas descripciones"),
                 ("eje_A", "F15b, solo código sobre lo guardado"), ("eje_B", "se difiere sin una corrección lista"),
                 ("evidencia", "t3/conteos_sin_leer/contado_sin_leer_tf.json, grafos.tf98.f67_cuantias.ids_sin_campo (por código)"),
                 ("estado", "propuesta")]),
    OrderedDict([("id", "PROP-T5-02"), ("fuente", "T5_tanda_final"), ("diagnostico", "lectura_autora"),
                 ("grafo", "KG-TandaFinal-r2b-sincola"), ("nodos_objetivo", [codigo(e["id"]) for v in inc.values() for e in v["elementos"]]),
                 ("capa_pipeline", list(inc)), ("causa", "la (12): el `aplica_a` va al rol de alcance de otro TO, que la resolución del sujeto "
                  "tomó de la sugerencia del modelo"), ("remedio", "a diagnosticar: R4 (sugerencia del modelo) cuando el rol es de otro TO"),
                 ("eje_A", "F15d, solo código sobre lo guardado"), ("eje_B", "se difiere sin una corrección lista"),
                 ("evidencia", "t4/tasas/tasas_t4_tramo3.json, observacion:12; " + ", ".join(e["ficha"] for v in inc.values() for e in v["elementos"])),
                 ("estado", "propuesta")]),
    OrderedDict([("id", "PROP-T5-03"), ("fuente", "T5_tanda_final"), ("diagnostico", "lectura_autora"),
                 ("grafo", "KG-TandaFinal-r2b-sincola"), ("nodos_objetivo", None), ("capa_pipeline", None),
                 ("causa", f"{len(err['aceptadas_items'])} unidades aceptadas de ítems con error en la lectura de la autora; la causa de cada "
                  "una, en errores_de_las_lecturas.aceptadas_items de t5/salidas/cifras_t5.json"),
                 ("remedio", "clasificar cada una por capa, como las 16 de no ítems, antes de proponer un remedio"),
                 ("eje_A", "según la capa"), ("eje_B", "según la capa"),
                 ("evidencia", "t4/lectura_autora/aceptadas_items_marcada.csv"), ("estado", "propuesta")]),
    OrderedDict([("id", "PROP-T5-04"), ("fuente", "T5_tanda_final"), ("diagnostico", "lectura_autora"),
                 ("grafo", "KG-TandaFinal-r2b (la cola, marcada)"), ("nodos_objetivo", None), ("capa_pipeline", None),
                 ("causa", f"{len(err['cola'])} unidades de la cola con error en la lectura de la autora y la regla del 25 % disparada; la "
                  "causa de cada una, en errores_de_las_lecturas.cola de t5/salidas/cifras_t5.json"),
                 ("remedio", "clasificar cada una por capa; la regla del 25 % pide investigar la causa (pre-registro de la tanda 1, "
                  "95b18217:634-635)"), ("eje_A", "según la capa"), ("eje_B", "según la capa"),
                 ("evidencia", "t4/lectura_autora/cola_marcada.csv"), ("estado", "propuesta")]),
]
if any(v["hallazgo"] for v in vig.values()):
    P.append(OrderedDict([("id", "PROP-T5-05"), ("fuente", "T5_tanda_final"), ("diagnostico", "lectura_autora"),
                          ("grafo", "KG-TandaFinal-r2b-sincola"), ("nodos_objetivo", None), ("capa_pipeline", ["E1-prompt"]),
                          ("causa", "la vigilancia (1) sube contra la línea de base de la tanda 1: Condicion que llevan un deber explícito"),
                          ("remedio", "para la versión posterior a la evaluación: la regla del prefijo que separa Condicion de Obligacion"),
                          ("eje_A", "F06, todo"), ("eje_B", "se difiere: fuera del grafo que evalúa B6.3"),
                          ("evidencia", "t4/tasas/tasas_t4_tramo3.json, vigilancias.vigilancia:1"), ("estado", "propuesta")]))
out["propuestas_backlog"] = P

# 6. El sello del tramo 1
out["sello_tramo1"] = OrderedDict([
    ("costo", out["costo"]["por_tramo"]["tramo_1"]),
    ("carpetas_hoy", L(TF / "t5/salidas/carpetas_tramo1_t5.json")),
    ("carpetas_al_cerrar_el_tramo_1", "no lo encontré en los FRENOs de T1 ni de T2 (ni en t2/control_entre_tramos_tanda_final.json)"),
    ("entrada_del_acumulado_de_60", L(TF / "t5/salidas/entrada_acumulado_60_t5.json"))])
OUT.mkdir(parents=True, exist_ok=True)
(OUT / "cifras_t5.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("cifras_t5.json", sha(OUT / "cifras_t5.json"))
