"""U-MED-UMBRALES: costo estimado de la opción B (juez por la API). Solo aritmética, sin llamadas.

Constantes tomadas del §8 del pre-registro de tripletas firmado (4afbe51:docs/preregistro_evaluacion_tripletas.md:224-247):
claude-sonnet-4-6 3 / 15 USD por millón (entrada / salida), lectura de caché 0,30 y escritura 3,75 (regla 0,1x y 1,25x,
NO VERIFICADA contra la tarifa publicada); 3,06 caracteres por token; fragmento con herencia mediana 979 y p90 2.078
caracteres. Supuestos propios de esta propuesta (NO VERIFICADOS): elemento de umbral y tramo de E1 en la ficha, 500
caracteres; prefijo fijo cacheado (instrucciones y casos resueltos) 3.500 tokens; salida 300 tokens; N = 3.
"""
PRECIO = {"in": 3.0, "out": 15.0, "cr": 0.30, "cw": 3.75}
CPT = 3.06
PREFIJO, SALIDA, N = 3500, 300, 3
FICHA = {"mediana": 979 + 500, "p90": 2078 + 500}
LLAMADAS = {
    "pool de calibración (20, hasta 2 corridas)": 20 * N * 2,
    "validación sobre la tanda 0 (100, hasta 2 corridas)": 100 * N * 2,
    "medición final (400)": 400 * N,
}


def costo(llamadas, chars):
    tin = chars / CPT
    por = (tin * PRECIO["in"] + PREFIJO * PRECIO["cr"] + SALIDA * PRECIO["out"]) / 1e6
    escrituras = 3 * 3 * PREFIJO * PRECIO["cw"] / 1e6
    return llamadas * por + escrituras, por


tot = {"mediana": 0.0, "p90": 0.0}
for nombre, k in LLAMADAS.items():
    fila = []
    for q, ch in FICHA.items():
        c, por = costo(k, ch)
        tot[q] += c
        fila.append(f"{q}: USD {c:.2f} (USD {por:.5f} por llamada)")
    print(f"{nombre}: {k} llamadas;", "; ".join(fila))
print(f"total: {sum(LLAMADAS.values())} llamadas; mediana USD {tot['mediana']:.2f}; p90 USD {tot['p90']:.2f}")
