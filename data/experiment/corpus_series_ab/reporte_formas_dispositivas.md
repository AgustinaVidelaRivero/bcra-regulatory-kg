# Formas dispositivas en las series «A» y «B»

Artefacto de respaldo de `docs/tesis/main.tex` §3.1 (fila 146 de `docs/tesis/mapa_fuentes_cap_esquema.md`). Generado por `data/experiment/corpus_series_ab/formas_dispositivas.py`.

- Comando (desde la raíz del repo): `python3 data/experiment/corpus_series_ab/formas_dispositivas.py`

## Formas buscadas

Exactamente tres, como cadenas literales, sin variantes morfológicas:

- «se establece» (normalizada: `se establece`)
- «deberán» (normalizada: `deberan`)
- «no podrán» (normalizada: `no podran`)

Una comunicación cuenta si su texto contiene al menos una de las tres.

## Método

- Universo: filas de `data/raw/manifiesto.csv` cuyo `archivo_local` cae bajo `02_comunicaciones_A/` (serie A) o `03_comunicaciones_B/` (serie B).
- Texto: el repo no tiene caché de texto extraído de estas comunicaciones (los PDF están gitignoreados y ningún archivo del árbol los transcribe), así que se extrae en memoria con `pdftotext -enc UTF-8 <pdf> -` (pdftotext version 26.06.0); no se persiste texto.
- Normalización previa a la búsqueda: NFKD sin marcas diacríticas, minúsculas, toda corrida de espacio en blanco (incluidos saltos de línea) colapsada a un espacio. Los cortes de palabra con guion al final de línea NO se recomponen.
- Coincidencia: búsqueda de subcadena literal de cada forma normalizada sobre el texto normalizado. Un PDF cuyo `pdftotext` falla o devuelve texto vacío no puede contar como positivo y queda en el denominador (se informa aparte).

## (A) Universo por serie: listadas, presentes, faltantes

| Serie | Listadas en manifiesto | Presentes en disco | Faltantes | Error de pdftotext | Texto vacío |
|---|---:|---:|---:|---:|---:|
| A | 1666 | 1666 | 0 | 0 | 0 |
| B | 1301 | 1301 | 0 | 0 | 0 |

La tasa se calcula sobre los PRESENTES en disco (denominador); si hubiera faltantes, la tasa no cubre al universo completo.

## (B) Tasa con al menos una forma, por serie

| Serie | Con al menos una forma (numerador) | Presentes (denominador) | Tasa |
|---|---:|---:|---:|
| A | 1049 | 1666 | 63,0 % |
| B | 122 | 1301 | 9,4 % |

Desglose por forma (una comunicación puede contar en más de una fila; por eso las filas no suman el numerador):

| Serie | «se establece» | «deberán» | «no podrán» |
|---|---:|---:|---:|
| A | 105 | 952 | 276 |
| B | 8 | 115 | 5 |

Sensibilidad (solo informativa; no es el criterio del mandato): mismas cadenas exigiendo límite de palabra a ambos lados, lo que excluye p. ej. «se establecen»:

| Serie | Con al menos una forma (límite de palabra) | Presentes | Tasa |
|---|---:|---:|---:|
| A | 1044 | 1666 | 62,7 % |
| B | 121 | 1301 | 9,3 % |

## (C) Contraste con la prosa vigente de §3.1

La prosa de `docs/tesis/main.tex` §3.1 afirma 63 % (serie A) y 9 % (serie B). Diferencia = tasa computada − prosa, en puntos porcentuales.

| Serie | Prosa | Computada | Diferencia (p.p.) | Redondeo entero coincide |
|---|---:|---:|---:|---|
| A | 63 % | 63,0 % | -0,0 | sí |
| B | 9 % | 9,4 % | +0,4 | sí |

Este artefacto no corrige la prosa: informa el número que produce el criterio declarado arriba.
