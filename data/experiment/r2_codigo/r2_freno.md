# U-R2-CODIGO — FRENO R2: complemento de R1 (G a K) y R2

Fecha: 02/10/2026. USD 0: ninguna llamada a la API. Commits previos de la unidad:
- R1, en `b18e808`: «U-R2-CODIGO R1 (tablas, USD 0)…», según `git log`;
- el mandato, en `c60e89c`.

**Interpretación declarada.** K mide y propone. Como hay contenido perdido, la regla propuesta **no se
implementó** (FRENO de K) y queda a decisión en el §1.5. El resto del complemento y R2 se ejecutaron.

Toda cifra sale de un JSON de este directorio, regenerable con el comando del encabezado de su script.

## 1. Complemento de R1

### 1.1 G — combinaciones horizontales (`r1c_censo_serializacion.json`, `r1c_ejemplos.txt`)

Implementación en `correr_e0.py`:
- **Geometría.** `_geometria_segmento` da, por cada celda None, su tipo: vertical, horizontal,
  bidimensional o indeterminada. Por cada celda con contenido da la última columna que cubre, tomada de su
  borde derecho.
- **Marca.** El valor se escribe una vez, en su columna, con «⟨abarca hasta <clave>⟩».
- **Celdas bidimensionales.** Una celda que empieza en una fila y una columna anteriores es parte del
  alcance; no se reescribe.
- **Sin alcance determinado** (las celdas cubiertas no son, todas, de esa misma celda): la tabla no se
  serializa.
- **V1** descuenta la marca y comprueba su clave.

**Caso de control.** `cap::tabla032` (`cap::5.3.2.3`), fila 5 del bloque:
«col2 = 100% | col3 = 15% ⟨abarca hasta col7⟩».

**Conteos.**
- Marcas de alcance escritas: 85, de las cuales 59 están en filas de datos (11 tablas) y 26 en filas de
  encabezado del modo posicional (16 tablas).
- Celdas cubiertas:

  | tipo | filas de datos | zona de encabezado |
  |---|---|---|
  | horizontales | **96, en 11 tablas** | **104, en 17 tablas** |
  | bidimensionales | 10, en 2 tablas | 4, en 3 tablas |

- Contra la referencia de la revisión:
  - filas de datos: coincide (96 en 11 tablas);
  - zona de encabezado: no coincide (104 contra 97). Con mi definición (filas escritas anteriores a la
    primera fila con dato), 2 de las 104 caen después de la cuarta fila (`cap::tabla017`). Las filas de
    rótulo del modo columnas no se cuentan, porque no se escriben como filas. **NO VERIFICADO** de dónde
    sale la diferencia de 7: no conozco la definición de la referencia.
- Tablas que G deja sin serializar: 0. Siguen 51 de 54.
- Tamaño de las líneas de E0 reemplazadas → bloques: columnas 18.002 → 29.129 caracteres; posicional
  17.808 → 34.724.
- E sin cambios:
  - 37 celdas propagadas, en 6 tablas;
  - 42 combinadas sin propagar: 22 con el origen en el encabezado y 20 con la celda de origen vacía, todas
    en `cap::tabla037`.

### 1.2 H — metadatos por tabla

Cada entrada de `flags.tablas_e0` lleva:
- `modo`;
- `celdas_propagadas`;
- `celdas_con_alcance`;
- `combinadas_sin_propagar`;
- `filas_subtitulo`.

Si la tabla no se serializó, los cinco van en None. El censo comprueba las 54 entradas contra la
serialización: 54 correctas, 0 con falla. El texto no cambia.

Caso que los motiva, `cap::6.2.2.6`: `cap::tabla037`, posicional, con 18 celdas propagadas, 3 con
alcance, **20 combinadas sin propagar** y 1 fila de subtítulo.

### 1.3 I — `selftest_e0r2.py`: 22/22

Está en este directorio y comprueba A3 de `selftest_b583`.
- El bloque literal de `cap::1.2`, sobre el PDF real.
- Una propagación E (`cap::tabla035`) y una marca G (`cap::tabla032`), con su V1.
- G-RECUADRO y R-TC2, cada una con un caso positivo y uno negativo.
- V1 rechaza la inversión de dos valores, la marca de combinada borrada y un carácter perdido.
- `verificacion_tablas`: las dos marcas de `cap::1.2`, cinco falsos positivos de las versiones 1 a 3 como
  casos negativos, y la inversión sintética en `cap::tabla2f004` (30 % de «A+ hasta A-» atribuido a «AAA
  hasta AA-») como caso positivo.

### 1.4 J — menores

- El docstring de `correr` dice que la sección de tablas está en `correr_e0.py`.
- `r1_freno.md` §5 suma el total de valores por grafo: 375, 375 y 156.
- El comentario de F aclara que una clave `contenido_tabular_residual` ausente se lee como igual a
  `contenido_tabular`. Los 6 chunks marcados solo por la heurística legada, recontados en
  `r1c_censo_serializacion.json`, son `cap::2.13`, `cap::3.2.4`, `cap::4.2.2`, `cap::4.3.3.2`,
  `cap::7.1.1::intro` y `ext::7.1.1.3`.

### 1.5 K — líneas descartadas como encabezado (`r1k_encabezados_descartados.json`). **FRENO**

`separar_encabezado_pie` (`e0_lib.py:502`), corrida tal como la llama `parsear_cuerpo` (`:683`), sobre
las páginas de cuerpo de los diez TOs.

**Qué descarta.** En la zona de encabezado:
- 597 líneas de sección;
- 531 con «B.C.R.A.»;
- 635 en mayúsculas;
- 73 colas de título.

Además, 1.782 líneas de pie.

**Las 635 en mayúsculas.**
- 629 se repiten en las primeras 5 líneas de otra página del mismo TO: son encabezado de página real.
- **6 no se repiten: son contenido**, en 4 chunks de la E0 legada:
  - «AAA A+ BBB+ BB+», `cap::2.12.2.6`, p. 24;
  - «0202.30.00.111D, 0202.30.00.115M, 0202.30.00.117R;» y «0202.30.00.118U, 0202.30.00.121G,
    0202.30.00.124N,», `ext::7.1.1.3`, p. 81. Son posiciones NCM; los códigos llevan letras mayúsculas;
  - «CONSOLIDACIÓN» y «COD CASOS», `ric::S2`, p. 4;
  - «PROTECCIÓN DE LOS USUARIOS DE SERVI CIOS FINANCIEROS», `pro::3.1.3`, p. 26. Es el encabezado corrido
    del TO con un espacio de más: comparado sin espacios, se repite.

**Regla propuesta.** En la rama de mayúsculas, descartar solo si el texto, sin espacios, está en las
primeras 5 líneas de al menos 2 páginas de cuerpo del TO. Sección, «B.C.R.A.», cola de título y pie
quedan sin cambios. Con ella se conservan 5 líneas.

**Efecto, simulado en el proceso de medición** (sin editar el pipeline):
- en la E0 legada cambian 3 chunks (`cap::2.12.2.6`, `ext::7.1.1.3`, `ric::S2`), sin ids nuevos ni
  perdidos;
- en e0-r2 cambian 2 (`ext::7.1.1.3`, `ric::S2`). `cap::2.12.2.6` ya lleva esas celdas en su bloque.

La regla iría solo en e0-r2. **No la implementé: espera tu decisión.**

### 1.6 Controles del complemento

- E0 legada: 34 de 34 idénticos.
- e0-r2: doble corrida idéntica, 46 archivos.
- V1 a V3: 0 fallas.
- V4: 2.395 chunks sin tabla idénticos; 39 con tabla iguales a la versión legada al reemplazar los
  bloques; 0 fallos.
- Selftests de E0: §2.4.
- Censo R1.d recomputado (`r1d_censo_requests.json`): 38 requests cambian (ric 21, cap 16, ext 1), USD
  0,6308. Es igual que en R1: G solo cambia el texto de chunks que ya tenían bloque. Anclaje: 2.434
  claves legadas en la caché y 38 faltan.

## 2. R2

### 2.1 a. Ids de chunk únicos (`BKL-0037`)

**Regla, declarada en `e0_lib.desambiguar_ids` antes de aplicarla.** Dentro de un TO y en orden
documental:
- el primer chunk con un id lo conserva;
- cada aparición posterior recibe el sufijo `::rep<k>`, donde k es su número de aparición;
- conserva `unidad`;
- guarda el id original en `id_e0_original`.

**Dónde corre.** Solo en e0-r2 (`correr_e0.procesar_tablas_r2`). Los renombres van a
`ids_desambiguados.json`, que se escribe solo si hubo alguno.

**Resultados.**
- En la partición del corpus escalado, que se lee sin escribir: 69 renombres (adfsp 9, ceninf 4, cirmo3
  52, ri_niif 4) y ningún id repetido después.
- La E0 de la tanda 0: 0 ids repetidos y 0 renombres; no se escribe el archivo y no cambia.

Las colisiones de la partición son numeraciones del índice del TO leídas como cuerpo. Por ejemplo,
`adfsp::6.1` aparece en la p. 3, que es el índice, y en la p. 25, que es el cuerpo.

**Límite.** La E0 de la partición la produjo el código de B5.8.4, no `correr_e0`. Para la tanda 1, el
productor de su E0 tiene que llamar a `desambiguar_ids`; si no, el runner frena (abajo).

**Runner.**
- `chunks_sin_ids_repetidos` frena con `IdsRepetidos` ante un id repetido, en las cuatro cargas de chunks:
  fase E1 (`runner_corpus.py:478`), compactación (`:605`), fase E3 (`:621`) y cierre de E2 (`:708`).
- `main` lo informa como «ERROR» y sale con código 4 (`:878`), antes de llamar a la API.
- Con una E0 sin ids repetidos, el comportamiento es el de siempre en todo perfil.

**Selftest** (`selftest_r2.py`, bloque B):
- un par de igual id frena;
- una lista sin repetidos pasa intacta;
- la compactación de E1 con un par repetido frena sin escribir el compactado.

### 2.2 b. Crudo del reintento de E3

**Formato.** `reintentos_e3.jsonl`, archivo compañero de `finales.jsonl` en el directorio de cada TO.
- Una línea por reintento: `{chunk_id, intento, tool_input, error}`.
- Lo escribe `runner_corpus.fase_e3`, en `runner_corpus.py:661`, antes de la línea de `finales.jsonl`.
- Sin reintentos no se crea, así que las corridas sin reintentos dejan los mismos archivos que antes.
- Se lee con `leer_companero` (last-wins por chunk e intento).

**Lector de lo ya corrido** (`lector_reintentos_e3.py`). Reconstruye el request de cada reintento con el
código del pipeline:
1. el veredicto de la verificación, de `veredictos.jsonl`;
2. `evaluar_veredicto` y los bloqueantes con cita;
3. `build_reextraccion_kwargs`, con el perfil, el modelo y el techo de 16.384 de la corrida.

Con eso calcula la clave y lee el crudo de `e3_verificador/cache/e1_reintentos.db`, abierta con
`immutable=1`.

**Resultados** (`lector_reintentos_e3.json`).

| generación | reintentos en `finales.jsonl` | claves en la caché | entradas sobrantes |
|---|--:|--:|--:|
| tanda 0, `salida_dirigida/` (la que leen los ensamblados) | 255 | 255 | 0 |
| tanda 0, `salida/` | 254 | 254 | 1 |
| r1 | 406 | 406 | 25 |

- La sobrante de `salida/` es `cap::4.3.3.1`, de la re-extracción dirigida del 28/09
  (`tanda0_dirigida_reint`).
- **Diferencia de r1, 431 contra 406.** Las 25 entradas sobrantes son todas de la corrida
  `e3_faseB_reintentos_e1_enm01`, creadas el 2026-08-11, todas de `pro`. Son la fase B de E3 sobre la E0
  enmendada: la calibración, anterior a la corrida del corpus de r1, que comparte namespace. Es coherente
  con el desglose de N1: 25 = 22 entradas de unidades sin reintento en `finales` + 3 de más en unidades
  con reintento.

### 2.3 Agregados de E3 (autorizados, plan, fila 8)

**Candado del prefijo**, al final de `prompt_e3.py`.
- `PREFIJO_HASH` (`:217`) se compara contra `21a836c7de6d` y la importación frena con `RuntimeError` si
  difiere. Solo compara: el prefijo no cambia.
- Va al final del módulo para no correr las líneas que cita el selftest de U-MANT (`prompt_e3.py:266`,
  `:213-217`).
- Prueba (`selftest_r2.py`, bloque E):
  - con los datos actuales, sobre una copia temporal, no frena y el hash es `21a836c7de6d`;
  - con `chunks_ric.json` alterado en la copia, la importación frena;
  - el archivo real no cambió.

**Docstring** de `ratchet_e3.py:238-239`: «Cambiar max_tokens no invalida la caché de prompts de la API
(no integra el prefijo), pero sí la caché local: su clave incluye max_tokens». Misma cantidad de líneas.

### 2.4 Reproducción de lo sellado y selftests

Todo sobre una copia del código fuera del repo.
- E0 legada de la tanda 0: 34 de 34 idénticos.
- Ensamblados re-corridos con `ensamblar_tanda0.py` desde `salida_dirigida/`:

  | ensamblado | `r1/kg.json` |
  |---|---|
  | desarrollo | `eab2fdd0…` |
  | diez | `dd42d6d9…` |
  | cinco | `4097d4fd…` |

  En los tres, 10 de 13 archivos son idénticos byte a byte, incluidos `kg.json` y `r1/kg.json`. Los otros
  3 (`r1/e5_esqueleto.json`, `r1/reporte_ensamblado_r1.json` y `reporte_ensamblado.json`) difieren solo
  en la raíz de las rutas: la corrida sellada recibió rutas relativas a la raíz del repo; con la raíz
  normalizada son idénticos.
- Selftests:
  - en verde: `selftest_e0` 57/57, `b52` 39/39, `b581` 34/34, `b582` 59/59, `b583` 33/33, `ub53`
    40/40, `cablev3` 45/45, `selftest_e0r2` 22/22 y `selftest_r2` 16/16;
  - `selftest_manifiesto` 32/37: los 5 fallos P5 (ruta absoluta en `reporte_e2_<to>.json`) son los mismos
    con el código original.
