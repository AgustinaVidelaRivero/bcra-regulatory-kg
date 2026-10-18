"""Mesa, §139 y §140 (17/10/2026), U-MED-DESAMB, parte 4: los estimadores y las reglas de decisión, sin modelo y sin datos.

- wilson(k, n): intervalo de Wilson al 95 % (z = 1,959963984540054).
- ponderado(estratos): la proporción ponderada por N de cada estrato, con Wilson sobre el n efectivo de Kish
  (n_ef = (Σ w)² / Σ w², con w = N_h / n_h para cada ítem leído del estrato h), como T4 de la tanda 1.
- mcnemar_exacto(b, c): la prueba exacta de McNemar, de dos colas: p = min(1, 2 · P[X ≤ min(b, c)]), X ~ Bin(b + c, 1/2).
- las reglas de decisión de S1, S2 y S3, firmadas por la autora el 17/10/2026 (§140), con la sensibilidad de S1 («correcta o genérica»
  como acierto, que se informa y no decide) y la descripción de E4 por regla. O1 no se decide con la lectura: va al grafo corregido.
Uso: python3 -I -B estimadores_desamb_mesa.py   (corre su selftest)"""
import math
from collections import Counter

Z95 = 1.959963984540054


def wilson(k, n, z=Z95):
    if n <= 0:
        return (None, None, None)
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (p, max(0.0, c - h), min(1.0, c + h))


def wilson_p(p, n, z=Z95):
    """Wilson para una proporción ya calculada (la ponderada) sobre un n efectivo no entero."""
    if n <= 0:
        return (None, None)
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))


def ponderado(estratos):
    """estratos: {nombre: (N_h, aciertos_h, n_h)}. Los estratos con n_h = 0 no entran (se declaran aparte)."""
    usados = {h: v for h, v in estratos.items() if v[2] > 0}
    N = sum(v[0] for v in usados.values())
    if N == 0:
        return None
    p = sum(v[0] / N * (v[1] / v[2]) for v in usados.values())
    sw = sum(v[0] / v[2] * v[2] for v in usados.values())          # Σ w = Σ_h n_h · (N_h / n_h) = N
    sw2 = sum((v[0] / v[2]) ** 2 * v[2] for v in usados.values())  # Σ w² = Σ_h n_h · (N_h / n_h)²
    n_ef = sw * sw / sw2
    lo, hi = wilson_p(p, n_ef)
    return {"p": p, "n_efectivo_kish": n_ef, "wilson_95": (lo, hi), "N": N, "estratos_sin_lectura": sorted(set(estratos) - set(usados))}


def mcnemar_exacto(b, c):
    n = b + c
    if n == 0:
        return 1.0
    k = min(b, c)
    cola = sum(math.comb(n, i) for i in range(k + 1)) / 2 ** n
    return min(1.0, 2 * cola)


# ----- Las reglas de decisión, firmadas el 17/10/2026 (§140) -----
CLASES = ("correcta", "generica", "incorrecta", "no_decidible")
ACIERTO = ("correcta",)                      # el criterio firmado: «acierta» es solo «correcta»
ACIERTO_SENSIBILIDAD = ("correcta", "generica")
S2_N, S2_MAX_ACIERTOS = 16, 7                # S2 aplica si aciertan 7 o menos de 16


def pares_E4(lecturas, acierto=ACIERTO):
    """lecturas: lista de (clase_regla, clase_modelo). Las que tienen una no decidible salen del McNemar (declaradas)."""
    usados = [(r in acierto, m in acierto) for r, m in lecturas if "no_decidible" not in (r, m)]
    return usados, len(lecturas) - len(usados)



def decide_S1(pares):
    """pares: lista de (regla_correcta: bool, modelo_correcta: bool) de E4, sin los no decidibles. S1 se aplica si la regla del
    texto acierta más que el modelo (b > c) y McNemar exacto da p < 0,05."""
    b = sum(1 for r, m in pares if r and not m)
    c = sum(1 for r, m in pares if m and not r)
    p = mcnemar_exacto(b, c)
    return {"b_regla_si_modelo_no": b, "c_modelo_si_regla_no": c, "p_mcnemar_exacto": p, "aplica": b > c and p < 0.05}


def decide_S2(aciertos, n=S2_N):
    """E6: S2 aplica si aciertan 7 o menos de 16 (forma firmada el 17/10/2026). Se informa el Wilson; con n = 16 la condición del
    superior < 0,75 es redundante (con este umbral, solo pesaría con n de 1, 3 o 5)."""
    if n != S2_N:
        raise ValueError("S2 se decide sobre las 16 de E6")
    p, lo, hi = wilson(aciertos, n)
    return {"aciertos": aciertos, "n": n, "p": p, "wilson_95": (lo, hi), "aplica": aciertos <= S2_MAX_ACIERTOS}


def describir_E4_por_regla(filas):
    """filas: lista de (regla_del_texto, clase_regla, clase_modelo). Descripción, no decide: cuántos casos de cada regla cayeron en
    la muestra y sus aciertos (criterio firmado y sensibilidad)."""
    out = {}
    for regla in sorted({f[0] for f in filas}):
        fs = [(r, m) for g, r, m in filas if g == regla]
        out[regla] = {"casos": len(fs), "regla_acierta": sum(r in ACIERTO for r, _ in fs), "modelo_acierta": sum(m in ACIERTO for _, m in fs),
                      "regla_acierta_sensibilidad": sum(r in ACIERTO_SENSIBILIDAD for r, _ in fs),
                      "modelo_acierta_sensibilidad": sum(m in ACIERTO_SENSIBILIDAD for _, m in fs)}
    return out


def decide_S3(errores):
    """errores: lista de (mención normalizada, entrada) de las lecturas incorrectas o genéricas. S3 propone un alias por cada par
    que se repite en 3 errores o más."""
    c = Counter(errores)
    return {"pares_con_3_o_mas": sorted([list(k) + [v] for k, v in c.items() if v >= 3]), "aplica": any(v >= 3 for v in c.values())}


def _selftest():
    fallas = []

    def ok(cond, que):
        print(("OK   " if cond else "FALLA") + " " + que)
        if not cond:
            fallas.append(que)
    p, lo, hi = wilson(26, 30)
    ok(abs(lo - 0.7032) < 5e-4 and abs(hi - 0.9469) < 5e-4, f"Wilson 26/30 = ({lo:.4f}, {hi:.4f}), referencia (0,7032, 0,9469)")
    p, lo, hi = wilson(85, 90)
    ok(abs(lo - 0.8765) < 5e-4, f"Wilson 85/90, límite inferior {lo:.4f}: el 0,8765 de S1-bis (tablero, §0)")
    ok(wilson(0, 0) == (None, None, None), "Wilson con n = 0 no inventa")
    ok(abs(mcnemar_exacto(8, 1) - 0.0390625) < 1e-12, f"McNemar exacto (8, 1) = {mcnemar_exacto(8, 1)}: 2 · 10/512 = 0,0390625")
    ok(abs(mcnemar_exacto(7, 2) - 0.1796875) < 1e-12, f"McNemar exacto (7, 2) = {mcnemar_exacto(7, 2)}: 2 · 46/512")
    ok(mcnemar_exacto(0, 0) == 1.0 and mcnemar_exacto(3, 3) == 1.0, "McNemar sin discordantes o empatado da 1")
    r = ponderado({"A": (100, 9, 10), "B": (100, 9, 10)})
    ok(abs(r["p"] - 0.9) < 1e-12 and abs(r["n_efectivo_kish"] - 20) < 1e-9, f"ponderado con pesos iguales: p 0,9 y n_ef 20 (da {r['p']}, {r['n_efectivo_kish']})")
    r = ponderado({"A": (900, 9, 10), "B": (100, 5, 10)})
    nef = (1000 ** 2) / (10 * 90 ** 2 + 10 * 10 ** 2)
    ok(abs(r["p"] - 0.86) < 1e-12 and abs(r["n_efectivo_kish"] - nef) < 1e-9, f"ponderado 900/100: p 0,86 y n_ef {nef:.4f} (da {r['p']}, {r['n_efectivo_kish']:.4f})")
    ok(ponderado({"A": (10, 0, 0)}) is None and ponderado({"A": (10, 1, 2), "B": (5, 0, 0)})["estratos_sin_lectura"] == ["B"], "estratos sin lectura: se declaran")
    ok(decide_S1([(True, False)] * 8 + [(False, True)] + [(True, True)] * 17)["aplica"], "S1 aplica con 8 contra 1")
    ok(not decide_S1([(True, False)] * 7 + [(False, True)] * 2 + [(True, True)] * 17)["aplica"], "S1 no aplica con 7 contra 2 (p 0,18)")
    ok(not decide_S1([(False, True)] * 8 + [(True, False)])["aplica"], "S1 no aplica si el modelo acierta más, aunque p < 0,05")
    ok(decide_S2(7)["aplica"] and not decide_S2(8)["aplica"] and abs(decide_S2(7)["wilson_95"][1] - 0.6682) < 5e-4,
       "S2: aplica con 7 de 16 (superior 0,668) y no con 8")
    try:
        decide_S2(7, 15)
        ok(False, "S2 rechaza un n distinto de 16")
    except ValueError:
        ok(True, "S2 rechaza un n distinto de 16")
    us, fuera = pares_E4([("correcta", "incorrecta"), ("generica", "correcta"), ("no_decidible", "correcta"), ("correcta", "correcta")])
    ok(us == [(True, False), (False, True), (True, True)] and fuera == 1, "E4: la genérica no acierta y la no decidible sale del McNemar")
    us2, _ = pares_E4([("generica", "incorrecta")], acierto=ACIERTO_SENSIBILIDAD)
    ok(us2 == [(True, False)], "sensibilidad: con «correcta o genérica», la genérica acierta")
    d = describir_E4_por_regla([("R2_calificador", "generica", "correcta"), ("R3", "correcta", "incorrecta"), ("R2_calificador", "correcta", "correcta")])
    ok(d["R2_calificador"]["casos"] == 2 and d["R2_calificador"]["regla_acierta"] == 1 and d["R2_calificador"]["regla_acierta_sensibilidad"] == 2
       and d["R3"]["casos"] == 1, "E4 por regla: casos y aciertos, con y sin sensibilidad")
    ok(decide_S3([("la entidad", "Sujeto_x")] * 3 + [("el banco", "Sujeto_y")] * 2)["pares_con_3_o_mas"] == [["la entidad", "Sujeto_x", 3]], "S3: el par con 3 errores")
    print("FALLAS:", len(fallas))
    return 1 if fallas else 0


if __name__ == "__main__":
    raise SystemExit(_selftest())
