"""U-MED-UMBRALES: fichas comunes esperadas entre la muestra de umbrales y las lecturas de la autora en tripletas.

Solo aritmética sobre los recuentos de estratos_umbrales_salida_UMEDUMBRALES.txt. N_final (elementos de umbral de la población de T)
es un supuesto NO VERIFICADO, de 1.000 a 5.000.
"""
f_v = 956 / 3983
f_t0 = 1103 / 5252
epn = 1306 / 1123
print("fraccion de aristas de contenido con un extremo con umbrales: V (2922b72d) %.4f; diez sin cola (e22fae1a) %.4f;"
      " elementos por nodo con lista (e22fae1a) %.3f" % (f_v, f_t0, epn))
print("aristas de V (100) con extremo con umbrales, esperadas: %.1f" % (100 * f_v))
for N in (1000, 2000, 5000):
    for f in (f_t0, f_v):
        print("control de T (30 aristas), N_final=%d, f=%.3f: fichas compartidas esperadas %.2f" % (N, f, 30 * f * epn * 240 / N))
