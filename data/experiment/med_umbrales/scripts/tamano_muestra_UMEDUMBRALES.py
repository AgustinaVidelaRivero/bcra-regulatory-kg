"""U-MED-UMBRALES: cálculo del tamaño de la muestra (solo aritmética, sin datos de corrección).

Valores de planificación: tamaños de estrato del grafo sin cola de la tanda 0 (e22fae1a), de
estratos_umbrales_salida_UMEDUMBRALES.txt. La población final se recuenta al sellar el grafo evaluado.
"""
import math

Z = 1.959964


def wilson(k, n, z=Z):
    if n == 0:
        return (float("nan"), float("nan"))
    p = k / n
    den = 1 + z * z / n
    c = (p + z * z / (2 * n)) / den
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return c - h, c + h


def n0(p, d, z=Z):
    return z * z * p * (1 - p) / (d * d)


print("1. n de muestreo simple para la mitad del ancho d con p de planificación")
for p in (0.95, 0.90, 0.85, 0.80, 0.70, 0.50):
    print(f"   p={p:.2f}", "  ".join(f"d={d:.2f}: {math.ceil(n0(p, d))}" for d in (0.03, 0.04, 0.05, 0.06, 0.07)))

# Estratos del grafo sin cola de la tanda 0 (e22fae1a), sin los 305 elementos vacíos del validador (sin valor, sin
# base y con comparación no_determinada; vacios_y_resueltas_salida_UMEDUMBRALES.txt), que se leen aparte (§2.5 del borrador). Las
# bases resueltas (10, todas del ensamblado) salen de E-e1-con (8, origen e1) y de E-desc-con (2, origen descripción)
# a un estrato censal, según vacios_y_resueltas_salida_UMEDUMBRALES.txt. V-sin-cont: los 312 − 305 = 7 del validador sin base y con
# comparación determinada.
N = {"E-e1-sin": 652, "E-e1-con": 84 - 8, "E-desc-sin": 88, "E-desc-con": 20 - 2,
     "V-sin-cont": 312 - 305, "V-con": 150}
CENSO = {"base_resuelta": 10}
NT = sum(N.values()) + sum(CENSO.values())


def asignar(n_total, minimo):
    tot = sum(N.values())
    alloc = {h: (Nh if Nh <= minimo else minimo) for h, Nh in N.items()}
    resto = n_total - sum(alloc.values())
    # proporcional al tamaño por encima del mínimo, iterativo, con tope en N_h
    for _ in range(50):
        libres = {h: N[h] for h in N if alloc[h] < N[h]}
        if resto <= 0 or not libres:
            break
        tl = sum(libres.values())
        add = {h: resto * N[h] / tl for h in libres}
        for h in libres:
            alloc[h] = min(N[h], alloc[h] + add[h])
        resto = n_total - sum(alloc.values())
    # redondeo a enteros conservando el total
    ent = {h: int(math.floor(a)) for h, a in alloc.items()}
    falta = n_total - sum(ent.values())
    for h in sorted(alloc, key=lambda h: alloc[h] - ent[h], reverse=True)[:falta]:
        ent[h] += 1
    return ent


def var_ponderada(alloc, p, censo=True):
    """Varianza del estimador ponderado Σ W_h p_h con p_h = p en todos los estratos, con corrección por
    población finita; el estrato censal aporta varianza 0."""
    v = 0.0
    for h, nh in alloc.items():
        W = N[h] / NT
        fpc = 1 - nh / N[h]
        v += W * W * p * (1 - p) / nh * fpc
    return v


print("\n2. asignación proporcional con mínimo por estrato, más el censo de las bases resueltas")
print("   N_h (planificación, e22fae1a):", N, "censo:", CENSO, "total", NT)
for n_total, minimo in ((200, 25), (220, 25), (240, 25), (220, 30), (260, 30)):
    a = asignar(n_total, minimo)
    for p in (0.85, 0.80):
        v = var_ponderada(a, p)
        hw = Z * math.sqrt(v)
        # n efectivo: el n de muestreo simple (sin fpc) con la misma varianza
        neff = p * (1 - p) / v
        print(f"   n={n_total} min={minimo} p={p:.2f} asign={a} mitad_ancho={hw:.4f} n_efectivo={neff:.0f}")

print("\n3. Wilson de referencia")
for k, n in ((27, 30), (28, 30), (26, 30), (36, 40), (38, 40), (95, 100), (90, 100), (209, 220), (198, 220)):
    lo, hi = wilson(k, n)
    print(f"   {k}/{n}: {lo:.4f} a {hi:.4f}")

print("\n4. potencia de la afirmación: P(límite inferior de Wilson >= umbral) con n efectivo y p verdadera")


def binom_pmf(k, n, p):
    return math.comb(n, k) * p ** k * (1 - p) ** (n - k)


for umbral in (0.85, 0.90, 0.95):
    for n in (150, 200, 220, 250):
        kmin = next(k for k in range(n + 1) if wilson(k, n)[0] >= umbral) if wilson(n, n)[0] >= umbral else None
        fila = []
        for p in (0.90, 0.93, 0.95, 0.97, 0.98):
            pot = sum(binom_pmf(k, n, p) for k in range(kmin, n + 1)) if kmin is not None else 0.0
            fila.append(f"p={p:.2f}: {pot:.2f}")
        print(f"   umbral={umbral:.2f} n={n} k_min={kmin} ({(kmin or 0) / n:.3f})", "  ".join(fila))

print("\n5. sin corrección por población finita (población final grande), misma asignación y mismos pesos W_h")
for n_total, minimo in ((160, 25), (180, 25), (220, 25), (240, 25), (260, 25), (280, 25), (400, 25)):
    a = asignar(n_total, minimo)
    a_sin_censo = {h: nh for h, nh in a.items()}
    for p in (0.85, 0.80):
        v = sum((N[h] / NT) ** 2 * p * (1 - p) / nh for h, nh in a_sin_censo.items())
        print(f"   n={n_total} min={minimo} p={p:.2f} mitad_ancho={Z * math.sqrt(v):.4f} "
              f"efecto_de_diseno={v / (p * (1 - p) / n_total):.3f}")
