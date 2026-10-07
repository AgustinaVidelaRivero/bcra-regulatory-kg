# Reglas de lectura de U-COMP-E1 (sellado en C0)

Fuente: `docs/mandatos/UCOMP_E1_comparacion_chica_modelo.md` en el commit de la firma, `cbcb823` (sha256 del archivo en ese commit: `89ce5508c574c4bc09f669df01468aeab1712af5651231eda16f63bc2d26d012`). Texto copiado verbatim, sin cambios; sellado en C0 (c) con su sha256 y su hora. Líneas 51 a 67 del mandato: las mediciones M1 a M4 (las cinco clases de M1 y las cuatro de M2, tal como las define el mandato) y la lectura cegada.

MEDICIONES, por brazo y por corrida, sobre las mismas fichas de T4:
M1. Los 137 supuestos del grupo c, clasificados con las cinco clases de T4 (Condicion con su relación hacia la norma; dentro de una
    norma; fusionado; omitido; sin relación), por el mismo lector y con el mismo criterio con que se clasificaron las salidas de Haiku.
M2. Las 46 omisiones normativas de T4 (y las 14 no normativas, aparte), en cuatro clases: extraída como contenido tipificado con tramo
    verificado por código (`pyd_r2/code/validador_r2.verificar_tramo_entidad`: contra el texto propio y el heredado, con la regla del
    tramo de dos segmentos en los ítems; nivel «exacta» o «tokens»); extraída con tramo no verificable (nivel «no»); registrada otra vez
    como omisión (con su categoría); ausente.
M3. Variación entre las dos corridas de cada brazo: unidades iguales byte a byte con la misma clave; cortes, respuestas sin
    herramienta y rechazos.
M4. Por brazo y corrida: elementos con tramo no verificable por código (nivel «no», sobre todo lo emitido), elementos fuera del esquema
    o del tool schema, y costo real por unidad y por brazo, con tokens de entrada y salida.

LECTURA. Fichas por unidad, brazo y corrida con un código y sin el nombre del brazo (decisión 2 al firmar: cegada con códigos; se
declara qué puede descubrir el brazo, por ejemplo el estilo o el largo). Las 8 relecturas del intento 0 de Haiku van con código entre
las demás. Primera lectura de la instancia; segunda lectura completa de la mesa; adjudicación de la autora
sobre las divergencias, como en T4. Ninguna lectura usa la API.

