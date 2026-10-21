"""B6.1, tanda final, T4, segundo tramo: las cifras para la hoja de la revisión entre tandas y las tablas del FRENO, por script, desde la
salida de tasas_t4t2_tf.py (<raíz>/data/experiment/tanda_final/t4/tasas/tasas_t4_tramo2.json). Es tanda1/t4/scripts/tablas_t4t2.py con
las rutas de la tanda final y, en la tabla 1, la línea de base de la tanda 1 (los valores T4.* de la versión derivada, que tasas_t4t2_tf.py
guarda en `lineas_de_base`) al lado de la de la tanda 0. Solo lee; escribe tanda_final/t4/tablas_t4_tramo2.md bajo <raíz> y la imprime.
Los números van con coma decimal; los intervalos, como [inferior; superior].
Uso: python3 -I -B tablas_t4t2_tf.py <raíz>
"""
import hashlib
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
RAIZ = Path(sys.argv[1]).resolve()
T4 = RAIZ / "data/experiment/tanda_final/t4"
TASAS = T4 / "tasas/tasas_t4_tramo2.json"
X = json.loads(TASAS.read_text(encoding="utf-8"))
sha = hashlib.sha256(TASAS.read_bytes()).hexdigest()
CEL = ["RI:sin_raiz", "RI:resto", "NG:sin_raiz", "NG:resto"]
ESTR = ["items", "no_items"]
d = lambda x, k=4: "—" if x is None else f"{x:.{k}f}".replace(".", ",")  # noqa: E731
iv = lambda w: f"[{d(w[0])}; {d(w[1])}]"  # noqa: E731
sn = lambda b: "sí" if b else "no"  # noqa: E731
mil = lambda n: f"{n:,}".replace(",", ".")  # noqa: E731
pl = lambda n, s, p: f"{n} {s if n == 1 else p}"  # noqa: E731
SAL = "`tasas/tasas_t4_tramo2.json`"
A, RI, C, V, O = X["aceptadas"], X["atencion_RI"], X["cola"], X["vigilancias"], X["observacion:12"]
LB = X["lineas_de_base"]
# la tanda 1 de las vigilancias y de la (12) es un solo valor de la versión derivada: «(1) …; (2) …; (3) …; (7) …; (12) …»
V1 = dict(re.findall(r"\((\d+)\) (.*?)(?=; \(\d+\) |$)", LB["vigilancias_y_12"]["tanda1"]))
assert sorted(V1) == sorted(["1", "2", "3", "7", "12"]), V1
V1 = {(f"vigilancia:{k}" if k != "12" else "12"): v for k, v in V1.items()}
w = [f"Salida: `tasas/tasas_t4_tramo2.json` ({X['hora']}, sha256 `{sha}`), de `scripts/tasas_t4t2_tf.py`. Rutas relativas a "
     "`data/experiment/tanda_final/t4/`.", ""]

# 1. Las cifras para la hoja
w += ["#### Tabla 1. Las cifras para la hoja de la revisión entre tandas (filas que esperan a T4)", "",
      "| fila | tanda final | línea de base: tanda 1 (versión derivada) | tanda 0 | decisión | script y clave de la salida |",
      "|---|---|---|---|---|---|"]
for s, nom in (("items", "aceptadas, ítems"), ("no_items", "aceptadas, no ítems")):
    r, z = A[s]["regla"], A[s]["sensibilidad_sin_dudosas"]
    pc = A[s]["por_celda"]
    lb1 = LB[f"aceptadas:{s}"]["tanda1"]
    ce, du = sum(pc[c]["con error"] for c in CEL), sum(pc[c]["dudosa"] for c in CEL)
    w.append(f"| {nom} | {r['errores']} de {r['leidas']} ({ce} con error y {pl(du, 'dudosa', 'dudosas')}); ponderada {d(r['tasa_ponderada'])}, Wilson "
             f"{iv(r['wilson'])} (n ef. {d(r['n_efectivo_kish'], 3)}); sin las dudosas, {z['errores']} de {z['leidas']}, {d(z['tasa_ponderada'])} "
             f"{iv(z['wilson'])} | {lb1} | {round(A[s]['p0_tanda0'] * 30)} de 30, Wilson {iv(A[s]['wilson_tanda0'])} | atención: {sn(r['atencion'])} "
             f"(p {d(r['p_valor_atencion'])}); freno: {sn(r['freno_por_intervalos'])} | `scripts/tasas_t4t2_tf.py`, {SAL}, `aceptadas.{s}` |")
t = A["total"]
w.append(f"| aceptadas, ponderada total | {d(t['regla']['tasa_ponderada'])}, Wilson {iv(t['regla']['wilson'])} (n ef. "
         f"{d(t['regla']['n_efectivo_kish'], 3)}); sin las dudosas, {d(t['sensibilidad_sin_dudosas']['tasa_ponderada'])} "
         f"{iv(t['sensibilidad_sin_dudosas']['wilson'])} | {LB['aceptadas:total']['tanda1']} | {d(t['tanda0_con_el_mismo_metodo']['p'])}, Wilson "
         f"{iv(t['tanda0_con_el_mismo_metodo']['wilson'])} (mismo método) | sin umbral | `scripts/tasas_t4t2_tf.py`, {SAL}, `aceptadas.total` |")
r, z = RI["regla"], RI["sensibilidad_sin_dudosas"]
w.append(f"| atención de RI | {r['errores']} de {r['leidas']}; ponderada de RI {d(r['tasa_ponderada_RI'])}, Wilson {iv(r['wilson'])} (n ef. "
         f"{d(r['n_efectivo_kish'], 3)}); sin las dudosas, {z['errores']} de {z['leidas']}, {d(z['tasa_ponderada_RI'])} | {LB['atencion_RI']['tanda1']} | bajo H0, "
         f"{d(RI['tasa_de_RI_bajo_H0'])} (umbral de T3: {d(RI['umbral_T3'])}) | atención: {sn(r['atencion'])} (p {d(r['p_valor_atencion'])}) | "
         f"`scripts/tasas_t4t2_tf.py`, {SAL}, `atencion_RI` |")
r, z = C["regla"], C["sensibilidad_sin_dudosas"]
pc = C["por_celda"]
w.append(f"| tasa de error de la cola | {r['errores']} de {r['leidas']} ({sum(pc[c]['con error'] for c in CEL)} con error y "
         f"{pl(sum(pc[c]['dudosa'] for c in CEL), 'dudosa', 'dudosas')}); ponderada {d(r['tasa_ponderada'])}, Wilson {iv(r['wilson'])} (n ef. "
         f"{d(r['n_efectivo_kish'], 3)}); sin las dudosas, {z['errores']} de {z['leidas']}, {d(z['tasa_ponderada'])} {iv(z['wilson'])} | "
         f"{LB['cola']['tanda1']} | {C['base_tanda0']} | regla del 25 %: {'se dispara' if r['regla_del_25_se_dispara'] else 'no se dispara'} (cifra y vigilancia, no freno) | "
         f"`scripts/tasas_t4t2_tf.py`, {SAL}, `cola` |")
pr = O["por_respuesta"]
caps = "; ".join(f"{k} {v['n']}" for k, v in O["incorrectas_por_capa_pipeline"].items()) or "—"
w.append(f"| observación (12) | {O['cruda']['correctas']} correctas de {O['cruda']['de']} ({pl(pr['no decidible'], 'no decidible', 'no decidibles')}, en el "
         f"denominador; {pl(pr['incorrecta'], 'incorrecta', 'incorrectas')}: {caps}); Wilson {iv(O['cruda']['wilson'])}; ponderada por celda "
         f"{d(O['ponderada_por_celda']['tasa'])} {iv(O['ponderada_por_celda']['wilson'])} | {V1['12']} | {O['linea_de_base_tanda0']} | sin umbral | "
         f"`scripts/tasas_t4t2_tf.py`, {SAL}, `observacion:12` |")
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
             f"`scripts/tasas_t4t2_tf.py`, {SAL}, `vigilancias.{m}` |")
w.append("")
w.append(f"- **La ampliación:** salta la atención de ítems, {sn(X['ampliacion']['salta']['aceptadas:items'])}; la de no ítems, "
         f"{sn(X['ampliacion']['salta']['aceptadas:no_items'])}; la de RI, {sn(X['ampliacion']['salta']['RI'])}. Hay ampliación: "
         f"{sn(X['ampliacion']['hay_ampliacion'])}. Con las dudosas fuera: " + ", ".join(
             f"{k} {sn(v)}" for k, v in X["ampliacion"]["con_la_sensibilidad"].items()) + ".")
if X["ampliacion"]["hay_ampliacion"]:
    w.append("- **Lo que salta va a la ampliación:** " + ", ".join(k for k, v in X["ampliacion"]["salta"].items() if v) + ". Su fila de la "
             "hoja queda con las 30 leídas: las tasas sobre las 60 (las 30 y las 30 de la ampliación) van en el tercer tramo, después de la "
             "lectura de la autora.")
w.append(f"- **Las líneas de base:** la tanda 1, {LB['fuente_tanda1']}; la tanda 0, al lado, la de cada fila de `lineas_de_base`.")
w.append(f"- **Los controles de la entrada** (`scripts/tasas_t4t2_tf.py`): {sum(X['controles'].values())} de {len(X['controles'])} pasan.")

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
             f"(`tasas/distribuciones_bajo_H0_t4_tramo2.json`, `aceptadas:{s}:regla`).")
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
texto = "\n".join(w) + "\n"
(T4 / "tablas_t4_tramo2.md").write_text(texto, encoding="utf-8")
print(texto)
