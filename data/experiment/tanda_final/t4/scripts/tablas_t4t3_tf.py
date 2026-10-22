"""B6.1, tanda final, T4, tercer tramo: las cifras para la hoja de la revisión entre tandas y las tablas del FRENO, por script, desde la
salida de tasas_t4t3_tf.py (<raíz>/data/experiment/tanda_final/t4/tasas/tasas_t4_tramo3.json). Es t4/scripts/tablas_t4t2_tf.py (segundo
tramo) con la fila de las aceptadas no ítems sobre las 60 en la tabla 1, la ponderada total y la atención de RI con las 60 (información)
al lado de las del segundo tramo, y las tablas 10 a 12 del tercer tramo. Solo lee; escribe tanda_final/t4/tablas_t4_tramo3.md bajo <raíz>
y la imprime. Los números van con coma decimal; los intervalos, como [inferior; superior].
Uso: python3 -I -B tablas_t4t3_tf.py <raíz>
"""
import hashlib
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
RAIZ = Path(sys.argv[1]).resolve()
T4 = RAIZ / "data/experiment/tanda_final/t4"
TASAS = T4 / "tasas/tasas_t4_tramo3.json"
X = json.loads(TASAS.read_text(encoding="utf-8"))
sha = hashlib.sha256(TASAS.read_bytes()).hexdigest()
CEL = ["RI:sin_raiz", "RI:resto", "NG:sin_raiz", "NG:resto"]
ESTR = ["items", "no_items"]
d = lambda x, k=4: "—" if x is None else f"{x:.{k}f}".replace(".", ",")  # noqa: E731
iv = lambda w: f"[{d(w[0])}; {d(w[1])}]"  # noqa: E731
sn = lambda b: "sí" if b else "no"  # noqa: E731
mil = lambda n: f"{n:,}".replace(",", ".")  # noqa: E731
pl = lambda n, s, p: f"{n} {s if n == 1 else p}"  # noqa: E731
SAL = "`tasas/tasas_t4_tramo3.json`"
A, RI, C, V, O = X["aceptadas"], X["atencion_RI"], X["cola"], X["vigilancias"], X["observacion:12"]
LB = X["lineas_de_base"]
B60, I6 = X["aceptadas_no_items_sobre_60"], X["informacion_con_las_60"]
# la tanda 1 de las vigilancias y de la (12) es un solo valor de la versión derivada: «(1) …; (2) …; (3) …; (7) …; (12) …»
V1 = dict(re.findall(r"\((\d+)\) (.*?)(?=; \(\d+\) |$)", LB["vigilancias_y_12"]["tanda1"]))
assert sorted(V1) == sorted(["1", "2", "3", "7", "12"]), V1
V1 = {(f"vigilancia:{k}" if k != "12" else "12"): v for k, v in V1.items()}
w = [f"Salida: `tasas/tasas_t4_tramo3.json` ({X['hora']}, sha256 `{sha}`), de `scripts/tasas_t4t3_tf.py`. Rutas relativas a "
     "`data/experiment/tanda_final/t4/`.", ""]

# 1. Las cifras para la hoja
w += ["#### Tabla 1. Las cifras para la hoja de la revisión entre tandas (filas que esperan a T4)", "",
      "| fila | tanda final | línea de base: tanda 1 (versión derivada) | tanda 0 | decisión | script y clave de la salida |",
      "|---|---|---|---|---|---|"]
for s, nom in (("items", "aceptadas, ítems"), ("no_items", "aceptadas, no ítems")):
    r, z = A[s]["regla"], A[s]["sensibilidad_sin_dudosas"]
    pc = A[s]["por_celda"]
    lb1 = LB[f"aceptadas:{s}"]["tanda1"]
    if s == "no_items":  # la fila de la hoja es la de las 60; la de las 30 va dentro de la misma celda
        r6, z6, pc6 = B60["regla"], B60["sensibilidad_sin_dudosas"], B60["por_celda"]
        ce6, du6 = sum(pc6[c]["con error"] for c in CEL), sum(pc6[c]["dudosa"] for c in CEL)
        w.append(f"| {nom}, sobre las 60 | {r6['errores']} de {r6['leidas']} ({ce6} con error y {pl(du6, 'dudosa', 'dudosas')}); ponderada "
                 f"{d(r6['tasa_ponderada'])}, Wilson {iv(r6['wilson'])} (n ef. {d(r6['n_efectivo_kish'], 3)}); sin las dudosas, {z6['errores']} de "
                 f"{z6['leidas']}, {d(z6['tasa_ponderada'])} {iv(z6['wilson'])}; sobre las 30 del primer tramo, {r['errores']} de {r['leidas']}, "
                 f"{d(r['tasa_ponderada'])} | {lb1} | {round(A[s]['p0_tanda0'] * 30)} de 30, Wilson {iv(A[s]['wilson_tanda0'])} | atención sobre "
                 f"las 30: {sn(r['atencion'])} (p {d(r['p_valor_atencion'])}); freno por la atención sobre las 60: "
                 f"{sn(r6['freno_por_atencion_sobre_60'])} (umbral {d(r6['umbral_recalculado'])}, p {d(r6['p_valor_sobre_60'])}); freno por "
                 f"intervalos: {sn(r6['freno_por_intervalos'])} | `scripts/tasas_t4t3_tf.py`, {SAL}, `aceptadas_no_items_sobre_60` y "
                 f"`aceptadas.no_items` |")
        continue
    ce, du = sum(pc[c]["con error"] for c in CEL), sum(pc[c]["dudosa"] for c in CEL)
    w.append(f"| {nom} | {r['errores']} de {r['leidas']} ({ce} con error y {pl(du, 'dudosa', 'dudosas')}); ponderada {d(r['tasa_ponderada'])}, Wilson "
             f"{iv(r['wilson'])} (n ef. {d(r['n_efectivo_kish'], 3)}); sin las dudosas, {z['errores']} de {z['leidas']}, {d(z['tasa_ponderada'])} "
             f"{iv(z['wilson'])} | {lb1} | {round(A[s]['p0_tanda0'] * 30)} de 30, Wilson {iv(A[s]['wilson_tanda0'])} | atención: {sn(r['atencion'])} "
             f"(p {d(r['p_valor_atencion'])}); freno: {sn(r['freno_por_intervalos'])} | `scripts/tasas_t4t3_tf.py`, {SAL}, `aceptadas.{s}` |")
t = A["total"]
w.append(f"| aceptadas, ponderada total | con las 30 de no ítems, {d(t['regla']['tasa_ponderada'])}, Wilson {iv(t['regla']['wilson'])} (n ef. "
         f"{d(t['regla']['n_efectivo_kish'], 3)}); sin las dudosas, {d(t['sensibilidad_sin_dudosas']['tasa_ponderada'])} "
         f"{iv(t['sensibilidad_sin_dudosas']['wilson'])}; con las 60 de no ítems (información), {d(I6['total']['regla']['tasa_ponderada'])}, "
         f"Wilson {iv(I6['total']['regla']['wilson'])} (n ef. {d(I6['total']['regla']['n_efectivo_kish'], 3)}) | {LB['aceptadas:total']['tanda1']} | {d(t['tanda0_con_el_mismo_metodo']['p'])}, Wilson "
         f"{iv(t['tanda0_con_el_mismo_metodo']['wilson'])} (mismo método) | sin umbral | `scripts/tasas_t4t3_tf.py`, {SAL}, `aceptadas.total` |")
r, z = RI["regla"], RI["sensibilidad_sin_dudosas"]
w.append(f"| atención de RI | con las 30 de no ítems, {r['errores']} de {r['leidas']}; ponderada de RI {d(r['tasa_ponderada_RI'])}, Wilson {iv(r['wilson'])} (n ef. "
         f"{d(r['n_efectivo_kish'], 3)}); sin las dudosas, {z['errores']} de {z['leidas']}, {d(z['tasa_ponderada_RI'])}; con las 60 de no ítems (información), {I6['atencion_RI']['regla']['errores']} de "
         f"{I6['atencion_RI']['regla']['leidas']}, {d(I6['atencion_RI']['regla']['tasa_ponderada_RI'])}, p {d(I6['atencion_RI']['regla']['p_valor'])} | "
         f"{LB['atencion_RI']['tanda1']} | bajo H0, "
         f"{d(RI['tasa_de_RI_bajo_H0'])} (umbral de T3: {d(RI['umbral_T3'])}) | atención: {sn(r['atencion'])} (p {d(r['p_valor_atencion'])}) | "
         f"`scripts/tasas_t4t3_tf.py`, {SAL}, `atencion_RI` |")
r, z = C["regla"], C["sensibilidad_sin_dudosas"]
pc = C["por_celda"]
w.append(f"| tasa de error de la cola | {r['errores']} de {r['leidas']} ({sum(pc[c]['con error'] for c in CEL)} con error y "
         f"{pl(sum(pc[c]['dudosa'] for c in CEL), 'dudosa', 'dudosas')}); ponderada {d(r['tasa_ponderada'])}, Wilson {iv(r['wilson'])} (n ef. "
         f"{d(r['n_efectivo_kish'], 3)}); sin las dudosas, {z['errores']} de {z['leidas']}, {d(z['tasa_ponderada'])} {iv(z['wilson'])} | "
         f"{LB['cola']['tanda1']} | {C['base_tanda0']} | regla del 25 %: {'se dispara' if r['regla_del_25_se_dispara'] else 'no se dispara'} (cifra y vigilancia, no freno) | "
         f"`scripts/tasas_t4t3_tf.py`, {SAL}, `cola` |")
pr = O["por_respuesta"]
caps = "; ".join(f"{k} {v['n']}" for k, v in O["incorrectas_por_capa_pipeline"].items()) or "—"
w.append(f"| observación (12) | {O['cruda']['correctas']} correctas de {O['cruda']['de']} ({pl(pr['no decidible'], 'no decidible', 'no decidibles')}, en el "
         f"denominador; {pl(pr['incorrecta'], 'incorrecta', 'incorrectas')}: {caps}); Wilson {iv(O['cruda']['wilson'])}; ponderada por celda "
         f"{d(O['ponderada_por_celda']['tasa'])} {iv(O['ponderada_por_celda']['wilson'])} | {V1['12']} | {O['linea_de_base_tanda0']} | sin umbral | "
         f"`scripts/tasas_t4t3_tf.py`, {SAL}, `observacion:12` |")
NOMV = {"vigilancia:1": ("vigilancia (1)", "sí"), "vigilancia:2": ("vigilancia (2)", "vaciamientos"),
        "vigilancia:3": ("vigilancia (3)", "duplicaciones"), "vigilancia:7": ("vigilancia (7)", "sin apoyo")}
BASEV = {m: LB["vigilancias_y_12"]["tanda0"][m] for m in NOMV}
for m, (nom, que) in NOMV.items():
    x = V[m]
    fuera = "; ".join(f"{pl(v, k, k + 's')}, fuera de la tasa" for k, v in x["fuera_de_la_tasa"].items())
    pond = (f"ponderada por celda {d(x['ponderada_por_celda']['tasa'])} {iv(x['ponderada_por_celda']['wilson'])}"
            if isinstance(x["ponderada_por_celda"], dict) else "leída entera, sin celdas")
    w.append(f"| {nom} | {x['cruda']['k']} {que} de {x['cruda']['n']}" + (f" ({fuera})" if fuera else "") +
             f"; cruda {d(x['cruda']['tasa'])}, Wilson {iv(x['cruda']['wilson'])}; {pond} | {V1[m]} | {BASEV[m]} | sin umbral | "
             f"`scripts/tasas_t4t3_tf.py`, {SAL}, `vigilancias.{m}` |")
w.append("")
w.append(f"- **La ampliación:** salta la atención de ítems, {sn(X['ampliacion']['salta']['aceptadas:items'])}; la de no ítems, "
         f"{sn(X['ampliacion']['salta']['aceptadas:no_items'])}; la de RI, {sn(X['ampliacion']['salta']['RI'])}. Hay ampliación: "
         f"{sn(X['ampliacion']['hay_ampliacion'])}. Con las dudosas fuera: " + ", ".join(
             f"{k} {sn(v)}" for k, v in X["ampliacion"]["con_la_sensibilidad"].items()) + ".")
w.append(f"- **Las aceptadas no ítems sobre las 60** (las 30 del primer tramo y las 30 de la ampliación; cada celda con el doble: "
         f"{sn(all(B60['cada_celda_con_el_doble'].values()))}): freno por la atención sobre las 60, "
         f"{sn(B60['regla']['freno_por_atencion_sobre_60'])}; freno por intervalos, {sn(B60['regla']['freno_por_intervalos'])}. Con las "
         f"dudosas fuera, la sensibilidad da otra decisión: {sn(any(B60['la_sensibilidad_da_otra_decision'].values()))}. Su fila de la hoja es "
         "la de las 60 (tablas 10 y 11).")
w.append("- **La ponderada total y la atención de RI con las 60** van como información, sin decisión, al lado de las del segundo tramo "
         "(tabla 12).")
w.append(f"- **Las líneas de base:** la tanda 1, {LB['fuente_tanda1']}; la tanda 0, al lado, la de cada fila de `lineas_de_base`.")
w.append(f"- **Los controles de la entrada** (`scripts/tasas_t4t3_tf.py`): {sum(X['controles'].values())} de {len(X['controles'])} pasan.")
w.append(f"- **Lo del segundo tramo da lo mismo** (`lo_del_segundo_tramo`): "
         f"{sum(X['lo_del_segundo_tramo']['bloques_iguales_a_tasas_t4_tramo2'].values())} de "
         f"{len(X['lo_del_segundo_tramo']['bloques_iguales_a_tasas_t4_tramo2'])} bloques iguales a `tasas/tasas_t4_tramo2.json`; en las líneas "
         f"de base cambian solo " + " y ".join(f"`{x}`" for x in X["lo_del_segundo_tramo"]["lineas_de_base_que_cambian"]) + ".")

# 2. Las aceptadas por celda
w += ["", "#### Tabla 2. Las aceptadas por celda (`aceptadas.<estrato>.por_celda`; pesos de `t3/muestras/umbrales_t4_tf.json`)", "",
      "| estrato | celda | N | peso | leídas | con error | sin error | dudosa |", "|---|---|---:|---:|---:|---:|---:|---:|"]
for s in ESTR:
    for c in CEL:
        p = A[s]["por_celda"][c]
        w.append(f"| {s} | {c} | {mil(A[s]['N_por_celda'][c])} | {d(A[s]['pesos'][c])} | {p['n']} | {p['con error']} | {p['sin error']} | {p['dudosa']} |")
w += ["", "#### Tabla 3. Las tasas de las aceptadas, la regla y la sensibilidad (`aceptadas.<estrato>.regla` y `.sensibilidad_sin_dudosas`)", "",
      "| estrato | cuenta | errores | leídas | tasa ponderada | n ef. | Wilson | p de la atención | atención | freno por intervalos | atención de T3 desde | freno de T3 desde |",
      "|---|---|---:|---:|---:|---:|---|---:|---|---|---:|---:|"]
for s in ESTR:
    for nombre, et in (("regla", "regla (dudosa = error)"), ("sensibilidad_sin_dudosas", "sensibilidad (dudosas fuera)")):
        r = A[s][nombre]
        w.append(f"| {s} | {et} | {r['errores']} | {r['leidas']} | {d(r['tasa_ponderada'])} | {d(r['n_efectivo_kish'], 3)} | {iv(r['wilson'])} | "
                 f"{d(r['p_valor_atencion'])} | {sn(r['atencion'])} | {sn(r['freno_por_intervalos'])} | {d(A[s]['umbrales_T3']['atencion_desde'])} | "
                 f"{d(A[s]['umbrales_T3']['freno_por_intervalos_desde'])} |")
for s in ESTR:
    w.append(f"\n{s}: la sensibilidad da otra decisión de atención, {sn(A[s]['la_sensibilidad_da_otra_decision']['atencion'])}; de freno, "
             f"{sn(A[s]['la_sensibilidad_da_otra_decision']['freno_por_intervalos'])}. La distribución bajo H0: "
             f"{mil(A[s]['regla']['puntos_de_la_distribucion'])} valores, suma {d(A[s]['regla']['suma_de_la_distribucion'], 6)} "
             f"(`tasas/distribuciones_bajo_H0_t4_tramo3.json`, `aceptadas:{s}:regla`).")
w += ["", "#### Tabla 4. La ponderada total y la atención de RI (`aceptadas.total` y `atencion_RI`)", "",
      "| cifra | cuenta | errores de leídas | tasa | n ef. | Wilson | p de la atención | atención |", "|---|---|---|---:|---:|---|---:|---|"]
for nombre, et in (("regla", "regla"), ("sensibilidad_sin_dudosas", "sensibilidad")):
    t = A["total"][nombre]
    w.append(f"| ponderada total | {et} | — | {d(t['tasa_ponderada'])} | {d(t['n_efectivo_kish'], 3)} | {iv(t['wilson'])} | — | sin umbral |")
for nombre, et in (("regla", "regla"), ("sensibilidad_sin_dudosas", "sensibilidad")):
    r = RI[nombre]
    w.append(f"| atención de RI | {et} | {r['errores']} de {r['leidas']} | {d(r['tasa_ponderada_RI'])} | {d(r['n_efectivo_kish'], 3)} | "
             f"{iv(r['wilson'])} | {d(r['p_valor_atencion'])} | {sn(r['atencion'])} |")
w.append(f"\nAtención de RI: {mil(RI['N_RI'])} unidades RI aceptadas; pesos " + ", ".join(f"{k} {d(v)}" for k, v in RI["pesos"].items()) +
         f"; por celda, con la regla, " + ", ".join(f"{k} {RI['regla']['k_por_celda'][k]} de {RI['regla']['n_por_celda'][k]}" for k in RI["pesos"]) + ".")
w += ["", "#### Tabla 5. NG `sin_raiz`, por celda y sin umbral (`NG_sin_raiz`)", "",
      "| estrato | N | leídas | con error | sin error | dudosa | tasa con la regla | tasa sin las dudosas |", "|---|---:|---:|---:|---:|---:|---:|---:|"]
for s in ESTR:
    g = X["NG_sin_raiz"][s]
    w.append(f"| {s} | {g['N']} | {g['n']} | {g['con error']} | {g['sin error']} | {g['dudosa']} | {d(g['tasa_con_la_regla'])} | {d(g['tasa_sin_dudosas'])} |")

# 3. La cola
w += ["", "#### Tabla 6. La cola por celda y su tasa (`cola`)", "",
      "| celda | N | peso | leídas | con error | sin error | dudosa |", "|---|---:|---:|---:|---:|---:|---:|"]
for c in CEL:
    p = C["por_celda"][c]
    w.append(f"| {c} | {C['N_por_celda'][c]} | {d(C['pesos'][c])} | {p['n']} | {p['con error']} | {p['sin error']} | {p['dudosa']} |")
w += ["", "| cuenta | errores | leídas | tasa ponderada | n ef. | Wilson | la regla del 25 % se dispara |", "|---|---:|---:|---:|---:|---|---|"]
for nombre, et in (("regla", "regla (dudosa = error)"), ("sensibilidad_sin_dudosas", "sensibilidad (dudosas fuera)")):
    r = C[nombre]
    w.append(f"| {et} | {r['errores']} | {r['leidas']} | {d(r['tasa_ponderada'])} | {d(r['n_efectivo_kish'], 3)} | {iv(r['wilson'])} | "
             f"{sn(r['regla_del_25_se_dispara'])} |")
w.append(f"\nLa sensibilidad da otra decisión de la regla del 25 %: {sn(C['la_sensibilidad_da_otra_decision']['regla_del_25'])}.")

# 4. Las vigilancias y la (12)
w += ["", "#### Tabla 7. Las vigilancias (1), (2), (3) y (7), por celda (`vigilancias.<muestra>.por_celda`)", "",
      "| muestra | celda | N | leídas | " + " | ".join(["respuestas"]) + " |", "|---|---|---:|---:|---|"]
for m in NOMV:
    x = V[m]
    for c in CEL:
        p = x["por_celda"][c]
        w.append(f"| {m} | {c} | {mil(x['N_por_celda'][c])} | {p['n']} | " + ", ".join(f"{k} {v}" for k, v in p.items() if k != "n") + " |")
w += ["", "#### Tabla 8. Las tasas de las vigilancias, la cruda y la ponderada por celda (`vigilancias.<muestra>`)", "",
      "| muestra | se vigila | por respuesta | fuera de la tasa | cruda | Wilson (cruda) | ponderada por celda | n ef. | Wilson (ponderada) |",
      "|---|---|---|---|---|---|---:|---:|---|"]
for m in NOMV:
    x = V[m]
    pp = x["ponderada_por_celda"]
    fuera = ", ".join(f"{k} {v}" for k, v in x["fuera_de_la_tasa"].items()) or "—"
    w.append(f"| {m} | {x['vigilada']} | " + ", ".join(f"{k} {v}" for k, v in x["por_respuesta"].items()) + f" | {fuera} | "
             f"{x['cruda']['k']} de {x['cruda']['n']}, {d(x['cruda']['tasa'])} | {iv(x['cruda']['wilson'])} | " +
             (f"{d(pp['tasa'])} | {d(pp['n_efectivo_kish'], 3)} | {iv(pp['wilson'])} |" if isinstance(pp, dict) else "— | — | leída entera, sin celdas |"))
w.append(f"\nVigilancia (3): {V['vigilancia:3']['declaracion']}.")
w += ["", "#### Tabla 9. La observación (12), por celda (`observacion:12`; pesos de `t3/muestras/poblaciones_t4t1_tf.json`)", "",
      "| celda | N | peso | leídas | correcta | no decidible | incorrecta |", "|---|---:|---:|---:|---:|---:|---:|"]
for c in CEL:
    p = O["por_celda"][c]
    w.append(f"| {c} | {mil(O['N_por_celda'][c])} | {d(O['pesos'][c])} | {p['n']} | {p['correcta']} | {p['no decidible']} | {p['incorrecta']} |")
w.append(f"\nCruda: {O['cruda']['correctas']} correctas de {O['cruda']['de']}, {d(O['cruda']['tasa'])}, Wilson {iv(O['cruda']['wilson'])}. "
         f"Ponderada por celda: {d(O['ponderada_por_celda']['tasa'])}, n ef. {d(O['ponderada_por_celda']['n_efectivo_kish'], 3)}, Wilson "
         f"{iv(O['ponderada_por_celda']['wilson'])}. Las incorrectas, por `capa_pipeline`: " + "; ".join(
             f"{k}, {v['n']} (fichas " + ", ".join(f"`{Path(e['ficha']).name}`" for e in v["elementos"]) + ")"
             for k, v in O["incorrectas_por_capa_pipeline"].items()) + ".")
# 5. El tercer tramo: las aceptadas no ítems sobre las 60
w += ["", "#### Tabla 10. Las aceptadas no ítems sobre las 60, por celda (`aceptadas_no_items_sobre_60`; pesos de `t3/muestras/umbrales_t4_tf.json`)",
      "", "Cada celda: primer tramo + ampliación = las 60.", "",
      "| celda | N | peso | leídas | con error | sin error | dudosa | el doble |", "|---|---:|---:|---|---|---|---|---|"]
pt, pa, p6 = B60["por_celda_primer_tramo"], B60["por_celda_ampliacion"], B60["por_celda"]
for c in CEL + [None]:
    g = (lambda q, r: q[c][r]) if c else (lambda q, r: sum(q[x][r] for x in CEL))
    cols = " | ".join(f"{g(pt, r)} + {g(pa, r)} = {g(p6, r)}" for r in ("n", "con error", "sin error", "dudosa"))
    w.append(f"| {c or 'total'} | {mil(B60['N_por_celda'][c] if c else sum(B60['N_por_celda'].values()))} | "
             f"{d(B60['pesos'][c]) if c else '1,0000'} | {cols} | {sn(B60['cada_celda_con_el_doble'][c]) if c else sn(all(B60['cada_celda_con_el_doble'].values()))} |")
u6 = B60["umbral_del_freno_por_atencion_sobre_60"]
w += ["", "#### Tabla 11. La tasa sobre las 60 y los dos frenos (`aceptadas_no_items_sobre_60.regla` y `.sensibilidad_sin_dudosas`)", "",
      f"El umbral de `t3/muestras/umbrales_t4_tf.json` (`aceptadas.no_items.umbrales.freno_por_atencion_sobre_60`): {d(u6['umbral_tasa_ponderada'])}, "
      f"p {d(u6['p_valor'])}. El superior del Wilson de la tanda 0: {d(B60['wilson_tanda0'][1])}.", "",
      "| cuenta | errores | leídas | tasa ponderada | n ef. | Wilson | umbral recalculado (igual al del JSON) | p sobre las 60 | "
      "freno por la atención sobre las 60 | freno por intervalos | freno |", "|---|---:|---:|---:|---:|---|---|---:|---|---|---|"]
for nombre, et in (("regla", "regla (dudosa = error)"), ("sensibilidad_sin_dudosas", "sensibilidad (dudosas fuera)")):
    r = B60[nombre]
    w.append(f"| {et} | {r['errores']} | {r['leidas']} | {d(r['tasa_ponderada'])} | {d(r['n_efectivo_kish'], 3)} | {iv(r['wilson'])} | "
             f"{d(r['umbral_recalculado'])} ({sn(r['umbral_recalculado_es_el_del_json'])}) | {d(r['p_valor_sobre_60'])} | "
             f"{sn(r['freno_por_atencion_sobre_60'])} | {sn(r['freno_por_intervalos'])} | {sn(r['freno'])} |")
w.append(f"\nEl umbral y el p-valor dicen lo mismo: {sn(B60['regla']['el_umbral_y_el_p_valor_dicen_lo_mismo'])}. La sensibilidad da otra "
         f"decisión: {sn(any(B60['la_sensibilidad_da_otra_decision'].values()))}. La distribución bajo H0, con las n de la regla: "
         f"{mil(B60['regla']['puntos_de_la_distribucion'])} valores, suma {d(B60['regla']['suma_de_la_distribucion'], 6)} "
         f"(`tasas/distribuciones_bajo_H0_t4_tramo3.json`, `aceptadas:no_items:sobre_60:regla`).")
w += ["", "#### Tabla 12. La ponderada total y la atención de RI: el segundo tramo y con las 60 de no ítems (`aceptadas.total`, `atencion_RI` "
      "e `informacion_con_las_60`)", "",
      "| cifra | no ítems con | cuenta | errores de leídas | tasa | n ef. | Wilson | p de la atención | decide |",
      "|---|---|---|---|---:|---:|---|---:|---|"]
for nombre, et in (("regla", "regla"), ("sensibilidad_sin_dudosas", "sensibilidad")):
    t2, t6 = A["total"][nombre], I6["total"][nombre]
    w.append(f"| ponderada total | 30 | {et} | — | {d(t2['tasa_ponderada'])} | {d(t2['n_efectivo_kish'], 3)} | {iv(t2['wilson'])} | — | sin umbral |")
    w.append(f"| ponderada total | 60 | {et} | — | {d(t6['tasa_ponderada'])} | {d(t6['n_efectivo_kish'], 3)} | {iv(t6['wilson'])} | — | información |")
for nombre, et in (("regla", "regla"), ("sensibilidad_sin_dudosas", "sensibilidad")):
    r2, r6 = RI[nombre], I6["atencion_RI"][nombre]
    w.append(f"| atención de RI | 30 | {et} | {r2['errores']} de {r2['leidas']} | {d(r2['tasa_ponderada_RI'])} | {d(r2['n_efectivo_kish'], 3)} | "
             f"{iv(r2['wilson'])} | {d(r2['p_valor_atencion'])} | atención: {sn(r2['atencion'])} |")
    w.append(f"| atención de RI | 60 | {et} | {r6['errores']} de {r6['leidas']} | {d(r6['tasa_ponderada_RI'])} | {d(r6['n_efectivo_kish'], 3)} | "
             f"{iv(r6['wilson'])} | {d(r6['p_valor'])} | información |")
texto = "\n".join(w) + "\n"
(T4 / "tablas_t4_tramo3.md").write_text(texto, encoding="utf-8")
print(texto)
