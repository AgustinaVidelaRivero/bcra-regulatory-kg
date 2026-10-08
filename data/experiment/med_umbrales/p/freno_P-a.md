# FRENO P-a — U-MED-UMBRALES, etapa P (piloto), tramo P-a (USD 0, sin API)

Enmienda 1 al pre-registro de tripletas, FIRMADA en `a0f9815`.

**HEAD.** `2a70b20` al inicio. Durante la sesión entró `2abb346` (17:27:50, asientos de la mesa), que solo toca el plan y
dos mandatos y ningún insumo de este tramo (`git diff --name-only 2a70b20 2abb346`). La copia definitiva se armó con
`2abb346` (`insumos_espejo_P.json`, campo `head`).

Escribí solo en
`data/experiment/med_umbrales/p/` y en el scratchpad; nada commiteado. Todo el Python corrió con `PYTHONDONTWRITEBYTECODE=1`, `.venv/bin/python -B`
(3.10.13), sobre una copia del repo armada con `code/preparar_espejo_P.py` (`git show HEAD:<ruta>` de cada insumo rastreado,
la enmienda de `a0f9815`, los PDFs copiados con su sha256; 67 archivos, ningún enlace; `insumos_espejo_P.json`).

## 1. Entrada

- `a0f9815` está en el log.
- El texto firmado (líneas anteriores a «## Firma») da `c77e92ad…7e01`.
- La semilla de P recalculada da `51fbea50388e7481`. La de T no se calculó ni se usó.
- Foto del repo al inicio: 15.905 archivos rastreados y no ignorados, sha256 de la foto `a790b838…`. Había 2.213 `.pyc` fuera de
  `.venv`.

## 2. Grafo

KG-Tanda0-Diez-r2b-sincola, `e22fae1a…`, verificado contra `data/experiment/neo4j/grafos.py:172`. El re-sellado único sigue
pendiente (`docs/tablero.md:19` en HEAD), así que el sorteo usa este sello.

## 3. Marco y estratos

Los recuentos dan exactamente los del mandato:

| estrato | elementos |
|---|---:|
| `E-e1-sin` | 652 |
| `E-e1-con` | 76 |
| `E-desc-sin` | 88 |
| `E-desc-con` | 18 |
| `V-sin-cont` | 7 |
| `V-con` | 150 |
| `base resuelta` | 10 |
| `V-vacío` | 305 |
| **total** | **1.306** |

- Con contenido son 1.001.
- Los cinco TOs nuevos tienen 143.
- Los conjuntos con `base_via` y con `base_destino` coinciden (10).

Fuente: los cinco `controles` en `true` del acta.

## 4. Sorteo

`acta_sorteo_P.json`, sellada a las 17:29:41 del 08/10/2026, sha256 `435fc76f…`
(`acta_sorteo_P.sha256`), antes del diagnóstico y antes de armar cualquier ficha.
- Hashes: lista `1f59d3f6…`, muestra `5de4b00d…`, orden `187bc5f7…`.
- Lotes: 20 y 20.
- La regla del lote 3 está escrita en el acta y no se ejecutó.
- Una segunda corrida reproduce la misma lista, muestra y orden.

El acta trae el estrato de cada elemento, que sale de campos guardados: la autora no la abre antes de cerrar el paso 1
del lote.

## 5. Diagnóstico de la comparación `no_determinada`

Archivos: `diagnostico_no_determinada/diagnostico_no_determinada_P.{json,md}`.

**Población.** 331 elementos, todos del ensamblado. Coincide con el mandato en los tres cortes:

| corte | cifras |
|---|---|
| por regla | `sin_marcador_plazo` 201, `sin_marcador` 130 |
| por estrato | `E-e1-sin` 247, `E-desc-sin` 55, `E-e1-con` 18, `E-desc-con` 8, `base resuelta` 3 |
| por unidad | porcentaje 113, días 105, meses 49, años 47, moneda 13, veces 4 |

**Regla de corte de la cláusula (declarada).** Corta en:
- un punto y coma;
- un punto seguido de espacio y de una mayúscula, de un número de punto o del fin del texto;
- un salto de línea, solo si abre un ítem, si sigue a dos puntos o si une el texto propio con un bloque heredado.

**Desvío respecto del mandato, que sugería cortar en todo salto de línea.** El texto de E0 conserva los renglones del
PDF («refinancia-» + salto). Cortar ahí deja cláusulas de un renglón y pierde marcadores del renglón anterior. Con esa
regla, un ejemplo arrancaba en «do, como máximo,».

Largo de la cláusula: mediana 237 caracteres, p90 559, máximo 2.189.

**Familias.**

| familia | elementos |
|---|---:|
| (i) | 132 |
| (ii) | 120 |
| (iii) | 73 |
| sin cláusula (la cuantía no se ubica en E0) | 6 |
| **total** | **331** |

**(i), por qué la regla no tomó el marcador.**

| causa | elementos |
|---|---:|
| marcador fuera del texto que leyó la regla | 108 |
| forma que la regla no toma dentro de la ventana | 10 |
| otra cuantía en medio | 6 |
| fuera de la ventana después | 5 |
| fuera de la ventana antes | 3 |
| **total** | **132** |

- Según el texto leído: 99 son del tramo de E1 y 33 de la descripción.
- Contraste (`reglas_comparacion.analizar` sobre la cláusula completa de E0): la regla fija un sentido en 33 de los 132 y no
  lo fija en 92; en 7 no reconoce la cuantía. De los 108 con el marcador fuera del texto leído, la cláusula completa da
  sentido en 31.

**(ii), por forma.**

| forma | elementos |
|---|---:|
| «a partir de», «luego de», «después de», «transcurrido» | 48 |
| período de referencia («últimos», «anteriores», «siguientes») | 47 |
| «máximo» o «mínimo» no pegados a la cuantía | 19 |
| «límite» | 10 |
| «será de» | 7 |
| «entre … y …» | 5 |
| «antes de» | 3 |
| «mayor de» o «menor de» | 2 |
| «tope» | 1 |

**Anclas.** En `reglas_comparacion.py`:

| qué | líneas |
|---|---|
| valores por defecto de `Cuantia` | `:224-225` |
| ventana de 10 y 3 palabras | `:110-111` y `:512-519` |
| límites de cláusula | `:343-355` |
| rama sin marcador | `:612-618` |

El texto que lee la regla está en `ensamblar_tanda0.py:723-727` y `:748`. Las anclas del mandato `:505-516` y `:613-616`
corresponden hoy a `:512-519` y `:612-618`.

**A ciegas.** 10 elementos de la población están en la muestra, y 5 los daría la regla del lote 3. Cuentan solo en los
agregados: el listado (316) y los ejemplos los dejan fuera. Los ids del lote 3 se calcularon en memoria, solo para
excluirlos, y no se escribieron.

**Candidato principal (sin veredicto).** En 108 elementos, el texto que leyó la regla (el tramo de E1 o la descripción) no
trae el marcador que trae la oración. Si la lectura lo confirma:
- por el §10.2, va al backlog como error de E1;
- salvo que la autora decida que la regla lea la oración de E0, lo que cambia la definición.

## 6 a 8. Fichas, formulario y comparador

**Fichas del lote 1.** `lote1/fichas/ficha_L1-NN.md` (20), `lote1/paginas/` (22 páginas, `pdftoppm -r 110`, sin errores),
`lote1/fichas_lote1.json`.
- Ubicación: 9 por la cuantía dentro de su tramo de E1, 5 por la cuantía sola (elemento de la descripción) y 6 por el
  tramo del validador. Dos son vacíos, con la pregunta única del §2.5.
- Una ficha trae el aviso de que la cuantía aparece 9 veces en el texto (van todas resaltadas).
- El armador aborta si la ficha muestra un campo del umbral, y no abortó.
- Las palabras «máximo» o «mínimo» que aparecen en dos fichas son parte del id del nodo, que sale de su descripción.

**Lo que la ficha deja ver a la fuerza.**
- La ausencia de tramo de E1 indica que el elemento salió de la descripción.
- El tramo resaltado indica que el elemento es del validador.
- La pregunta del §2.5 indica que el elemento es un vacío.

**Formulario.** `lote1/formulario_paso1_lote1.md`. El formato se probó con una ficha inventada
(`ejemplo_ficha_inventada_formulario_P.md`).

**Comparador.** `code/comparador_paso2_P.py`.
- `selftest/salida_selftest_comparador_P.txt`: 23 de 23, sobre una copia del código.
- Corrida en seco con el formulario sin llenar: 20 fichas, 0 diferencias, 8 campos sin llenar por ficha con contenido.

## 9. Regla de calificación v0

`regla_calificacion_v0.md`: el §2 firmado sin cambios, sacado de `a0f9815` (líneas 47 a 105; sha256 del texto `3b386f99…`,
el mismo que da `sed` sobre `git show a0f9815:…`).

## Reproducción

- Las 47 salidas del diagnóstico, del lote 1 y de la regla se reproducen byte a byte en una segunda corrida desde la copia.
- El código de `code/` es igual al que corrió.
- `comun_P.py` y `marco_sorteo_P.py` son los del sello (sus sha256 están en el acta).
- La regla de corte nueva vive en `texto_P.py`, para no cambiar `comun_P.py` después del sello; `comun_P.clausula` quedó
  sin uso.

## Para el lote 1 (P-b)

La autora llena `lote1/formulario_paso1_lote1.md` leyendo las fichas del mismo número, sin abrir el acta ni el diagnóstico
por elemento. Después, en P-b, el comparador devuelve las diferencias con el valor del grafo a la vista y ella las
clasifica.
