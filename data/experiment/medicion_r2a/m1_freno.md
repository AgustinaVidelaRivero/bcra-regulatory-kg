# U-MED-R2A — FRENO M1: el grafo r2a

Mandato: `docs/mandatos/UMED_R2A_medicion_r2a.md`, firmado el 03/10/2026 en `43dc44f`. Su cabecera lo dice desde
`b901f6d`. USD 0: ningún comando llama a la API y Neo4j no se usa.

Commits durante la unidad (`git log`):
- HEAD al abrir la sesión: `43dc44f`.
- Al iniciar la batería: `b901f6d`, de las 09:30:05 (`estado_repo_inicio_M1.txt` del paquete).
- Durante la producción entró `d69b11f`, a las 09:45:42: es la fe de erratas del plan y del tablero de correcciones.
- Ninguno de los tres toca código.

Código: el pipeline es el de `e1c9456`. `git diff --name-only e1c9456 HEAD` lista solo documentos de `docs/` y JSON y
`.md` de `data/experiment/r2_codigo/`, ningún archivo de código. No edité el pipeline, la suite, las shapes ni los
manifiestos.

## Cómo corrió

1. **Batería de control sobre dos copias** (regla l). Dos copias reales del repo, sin `.git` ni entornos: 17.125
   archivos y 0 enlaces cada una. Duró de 09:32:15 a 09:40:58. En cada copia corrí los comandos de M1.a a M1.c en las
   mismas rutas relativas que se versionan. En una de ellas, además, la E0 legada y los tres ensamblados sellados
   (M1.d) y los selftests.
2. **Producción en el repo**, de 09:42:38 a 09:45:59: los comandos de M1.a a M1.c, que escriben solo en los tres
   directorios enumerados.

Por qué la producción va en el repo y no se copia desde una copia: el reporte del ensamblado r2 registra, en
`redirecciones`, la ruta absoluta de cada módulo redirigido. Shapes y suite registran también rutas absolutas internas
(vocabulario, catálogo, esqueleto de referencia). Copiado desde una copia, lo versionado llevaría rutas del
scratchpad. Producido en el repo, lleva las del repo, como los ensamblados sellados.

Control del repo (sha256 de todos los archivos salvo `.git`, antes y después de cada paso):
- En la batería cambiaron 2 archivos ajenos a esta unidad: `docs/plan_tesis.md` y `docs/tablero_correcciones.md`.
  Los modificó otra sesión a las 09:40:42 (`ls -laT`), en las filas :51, :53 y :72 del tablero. Son los cambios que
  la autora commiteó en `d69b11f`. La batería no escribe en el repo.
- La producción agregó 103 archivos (47 + 35 + 21), todos en los tres directorios enumerados, y no modificó ni borró
  ningún otro.
- `.pyc`/`__pycache__`: 286 entradas antes y después, en la batería y en la producción.

## M1.a — E0 e0-r2 de los diez TOs

```
.venv/bin/python -B data/experiment/reextraccion_v2/e0_chunking/correr_e0.py \
  --manifiesto data/experiment/reextraccion_v2/manifiestos/tanda0_10tos.json --version-e0 e0-r2 \
  --salida data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2/
```

La corrí desde la raíz del repo. El mandato escribe el manifiesto relativo a `reextraccion_v2/` y la salida relativa
a la raíz; usé la ruta completa del manifiesto.

Resultados:
- 47 archivos.
- sha256 del manifiesto de la salida (líneas `sha256  nombre`, ordenadas por nombre, unidas con salto de línea final):
  `d93bcc01ab7e6fe517b308b6845b0d51e1d244b7e3c44dbfd7d0798e5b88e54a`.
- Doble corrida: las dos copias y el repo, byte a byte iguales en los 47.
- Control: los 47 son byte a byte iguales a la e0-r2 de la batería de cierre de U-R2-CODIGO (`final/e0_r2_a`,
  scratchpad de esa unidad).

## M1.b — KG-Tanda0-Diez-r2a y KG-Tanda0-Desarrollo-r2a

```
.venv/bin/python -B data/experiment/tanda0/code/ensamblar_tanda0.py \
  --manifiesto data/experiment/reextraccion_v2/manifiestos/tanda0_ens_diez.json \
  --entrada data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida --perfil-r2 \
  --e0-r2 data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2 \
  --salida data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2a
```

El de desarrollo es el mismo comando con `tanda0_ens_desarrollo.json` y `--salida …/ens_desarrollo_r2a`. El grafo
queda en `<salida>/r2/kg.json`.

| | KG-Tanda0-Diez-r2a | KG-Tanda0-Desarrollo-r2a |
|---|---|---|
| sha256 | `99fe2bfa0de05704e4c636bdf9b0455a30e29b378e3b0e61eadc49dad3f7c649` | `93a7af7279a415ee72cfec547bcd080d4c85a96746e219ed94dea4239007e8dd` |
| nodos / aristas | 8.358 / 29.499 | 6.470 / 24.728 |
| fuera del modelo r2 (nodos / aristas) | 0 / 0 | 0 / 0 |
| `remite_a`: aristas (interna / externa / to_entero) | 14.000 (13.021 / 949 / 30) | 12.833 (12.049 / 775 / 9) |
| `remite_a`: citas resueltas / irresolubles | 1.547 / 510 | 1.382 / 425 |
| relaciones no verificadas por E3 (→ Operacion / → Potestad) | 697 (434 / 263) | 627 (388 / 239) |
| no mapeados (filas del registro) | 48 | 33 |
| umbrales: elementos en nodos con lista | 842 en 727 | 758 en 653 |

Fuente: `<salida>/r2/reporte_ensamblado_r2.json`, claves `validacion_modelos_r2`, `remite_a`,
`aristas_no_verificadas_e3`, `registro_no_mapeados` y `umbrales`.

Desglose de diez, de las mismas claves:
- Citas resueltas por alcance: interna 1.474, externa 52, to_entero 21.
- Irresolubles por causa (510): punto sin nodos 205, norma fuera del inventario 189, anáfora sin número 55, punto
  inexistente en E0 30, autorreferencia al punto propio 30, anáfora sin antecedente 1.
- Atribución D1 (`atribucion_d1`): 1.142 a los nodos que contienen la unidad y 243 a todos los nodos del punto.
  La unidad de este conteo es la mención detectada en el texto de cada procedencia, sin las anáforas sin número ni
  las citas del texto heredado (`data/experiment/reextraccion_v2/corpus_v2/r1_referencias.py:1167-1171`). No son
  citas resueltas.
- Umbrales:
  - 842 elementos sobre 5.040 nodos de los cuatro tipos;
  - comparación: máximo inclusivo 379, no determinada 129, coeficiente 140, mínimo inclusivo 111, mínimo estricto
    71, máximo estricto 8, igual 4; con `comparacion_asumida` 176;
  - tramo verificado: exacto 803, por tokens 22, no 17;
  - en tabla: verificado 60, no verificado 31, sin tabla 751;
  - base resuelta 19, no resuelta 141;
  - plazos a `frecuencia` 250, fuera de la lista 213;
  - rangos con la unidad repetida 0.
- Registro de no mapeados: por estado, cuarentena 40 y resuelto a clase 8; por motivo, sin match 27, mención no
  verificada 13 y calificador 8. Resolución de sujetos: 4.147 relaciones, 0 desacuerdos entre regla y modelo.
- `establecida_en` derivadas 536; nodos de contenido sin `establecida_en`: 0.
- Pasada residual de E4, medida y no aplicada: 24 propuestos, 0 resoluciones (motivo de los 24: sin match en el
  catálogo). Su lectura es de M3.c.
- `referencia` con origen distinto de TextoOrdenado: 0.

Doble corrida:
- Interna del ensamblado (`doble_corrida_byte_identica`): true en los dos grafos, en las dos copias y en el repo.
- Externa, entre las dos copias y contra el repo:
  - diez: 30 de 35 archivos byte a byte; los otros 5 son iguales con la raíz de la copia reemplazada por la del
    repo: `r2/reporte_ensamblado_r2.json` y las salidas de shapes y suite (`.md` y `.json`);
  - desarrollo: 20 de 21 byte a byte, más el reporte, igual con la ruta normalizada.
- Entre los iguales byte a byte están `kg.json`, `remisiones_registro.json`, `no_mapeados_sujetos.jsonl`,
  `resolucion_sujetos.jsonl` y los registros por TO.

Controles:
- KG-Tanda0-Desarrollo-r2a reproduce byte a byte el grafo `93a7af72…` de la batería de cierre de U-R2-CODIGO.
- KG-Tanda0-Diez-r2a es byte a byte la prueba de diez de esa batería (`99fe2bfa…`).
- Los demás archivos de `r2/` son byte a byte los de esa batería: 29 de 29 en diez y 19 de 19 en desarrollo. Los
  reportes difieren solo en las claves de ruta `redirecciones` y `tablas_e0_r2`.

**Criterio para escalar (enmienda 2 de L-ESQ-R2, §9): se cumple.** En KG-Tanda0-Diez-r2a hay 2 aristas `remite_a` con
`destino = cla::3.7`, desde nodos anclados en `cla::5.1.1.1` hacia la Definicion anclada en `cla::3.7`
(`Definicion_importe_de_referencia__…_bd1e8e`). Los orígenes son `Condicion_monto_supera_dos_veces_importe_referencia_3_7__…_b79da9`
y `Definicion_cartera_comercial_creditos_consumo_vivienda__…_aa2e70`. Lo controla `m1_post.py` (paquete), que filtra
las aristas `remite_a` por `properties.destino` y por la procedencia de los dos extremos.

## M1.c — Validación

- **Modelo r2:** 0 nodos y 0 aristas fuera del modelo (arriba).
- **Shapes**, salida versionada en `ens_diez_r2a/shapes_perfil_r2_fase_r2a.{md,json}`:
  ```
  .venv/bin/python -B scripts/shapes_validator.py --kg <diez>/r2/kg.json --perfil r2 --fase r2a \
    --e0 data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2 --registro-dir <diez>/r2 \
    --out <diez>/shapes_perfil_r2_fase_r2a.md
  ```
  `--registro-dir` no está en el comando del mandato. Le paso el mismo directorio que toma por defecto (el del
  `--kg`), para que el registro quede con ruta relativa y no absoluta. El resultado no cambia.
  - **Veredicto: NO PASA, solo por S18**: 301 Restricciones `limite_cuantitativo`, de las cuales 253 tienen lista,
    22 tienen el umbral guardado sin lista (la marca) y 26 no tienen ninguna de las dos. Los 26 son los límites
    relativos de la decisión 8: resultado declarado, no freno.
  - Las otras 16 bloqueantes dan PASS, entre ellas S31: 14.000 de 14.000 evidencias en un tramo del chunk de la
    arista.
  - Informativas: S7 FAIL (52 grupos), S12 FAIL (221 Excepciones sin salida), S8, S11, S21, S23 y S27 WARN.
    S21 cuenta como incoherentes las 30 `to_entero`, por construcción de su enunciado: apuntan al TextoOrdenado, no
    a un punto. S27 da 4.026 aristas de sujeto sin mención, porque la mención es de r2b.
  - Desarrollo, informativa, fuera del repo: NO PASA solo por S18, con 25 de 273 sin ninguna de las dos.
- **Suite**, salida versionada en `ens_diez_r2a/suite_perfil_r2.{md,json}`:
  ```
  .venv/bin/python -B scripts/regression_kg.py --kg <diez>/r2/kg.json --perfil r2 --generacion 3 \
    --catalogo data/experiment/catalogo_unico/generados_r2/catalogo_suite_r2.json \
    --politica-cuarentena flaggeada --esperado scripts/regression_kg_esperado.json --out <diez>/suite_perfil_r2.md
  ```
  - **56 ítems: 33 resuelto, 15 persiste, 8 no_aplicable.**
  - Persisten BKL-0017, BKL-0006, BKL-0023, BKL-0019, BKL-0004, BKL-0003, BKL-0007, RT-C5-1, RT-C5-2, RT-C5-4,
    RT-C6-5, T5, T6, E4-b y LN-3.
  - No aplican BKL-0026, BKL-0027, RT-C5-5, I1, I2, E4-a8, E4-c y LN-7.
  - `EJ-cla-5.1.1.1` resuelto: (i) dos `condicion_de`, marcadas no verificadas por E3; (ii) dos `remite_a` a
    `cla::3.7`; (iii) informativo, cumplido.
  - BKL-0006 y BKL-0023 «persiste» (tabla del 1.2 invertida), como anticipó el cierre de U-R2-CODIGO.
  - No se computa regresión: la fixture no tiene entrada con ese sha.
  - Desarrollo, informativa: 35 / 13 / 8.

## M1.d — Sellados y selftests

- E0 legada, `correr_e0.py --manifiesto …/tanda0_10tos.json`: 34 de 34 archivos byte a byte iguales a
  `e0_chunking/salida_tanda0/`.
- Ensamblados sellados `ens_desarrollo`, `ens_diez` y `ens_cinco`: en los tres, 10 de 13 archivos byte a byte y 3 iguales
  con la ruta normalizada (`reporte_ensamblado.json`, `r1/e5_esqueleto.json`, `r1/reporte_ensamblado_r1.json`).
  - El `r1/kg.json` da `eab2fdd0…`, `dd42d6d9…` y `4097d4fd…`.
  - Para eso corrí `--entrada` con ruta absoluta, como se produjeron los sellados. Con la ruta relativa, el reporte
    r1 difiere además en una línea: `redirecciones`, `r1_comun.SALIDA` registra el valor tal como llega.
- Selftests, todos en verde, iguales a los del cierre de U-R2-CODIGO:
  - e0 57/57, b52 39/39, b581 34/34, b582 59/59, b583 33/33, ub53 40/40, cablev3 45/45, corpus 21/21, e2 35/35;
  - obs12 26/26, dirigida 28/28, pyd_r2 296/296, r3 96/96, r2 18/18, e0r2 48/48, clave_cache OK;
  - regression_kg 147/147, shapes congelado 79/79, r4 26/26.

  `selftest_manifiesto` da 32/37, con los 5 fallos P5 conocidos (ruta absoluta en `reporte_e2`; cierre de
  U-R2-CODIGO).

## M1.e — Entrada r2 de la fixture, PROPUESTA

```
.venv/bin/python -B data/experiment/medicion_r2a/m1e_propuesta_r2a.py scripts/regression_kg_esperado.json \
  data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2a/suite_perfil_r2.json --escribir
```

- `propuesta_r2_sin_sellar` pasa a tener una sola entrada, `KG-Tanda0-Diez-r2a`, con:
  - la ruta del grafo en el repo, su comando y su sha256;
  - la generación, la política, el catálogo y su sha, y el perfil;
  - la evidencia, que es la corrida de M1.c;
  - los 56 estados.
- Reemplaza la propuesta `KG-Prueba-r2-desarrollo`, cuyo grafo `93a7af72…` es hoy KG-Tanda0-Desarrollo-r2a.
- Contra esa propuesta cambian 2 ítems: T6 y E4-b, de resuelto a persiste.
- **Hallazgo:** los dos persisten por construcción del test, no por el grafo.
  - T6 exige exactamente 5 TextoOrdenado con los ids de `r1_comun.TOS_ORDEN`, los cinco TOs de desarrollo
    (`scripts/regression_kg.py:1306-1313`, `:547-552`; `data/experiment/reextraccion_v2/corpus_v2/r1_comun.py:38`).
    El grafo de diez tiene 10, uno por TO: no falta ninguno, y los 5 «fuera del esperado» son ctacte, docvig, lingob,
    pagjub y polcre.
  - E4-b depende de T6 (`:1506`).
  - Los dos ítems llevan una `nota` con esto en la propuesta. El estado no lo cambié.
- `estado_esperado` no cambia (sha canónico `73031656…`), ni `linea_de_base_observada` (`83fc4bb6…`), ni el resto de
  las claves (el script lo comprueba antes de escribir).
- sha256 de la fixture: `2c9e9b5e…` antes, `3d3f7979c8bd0c213b6f92de7ba288a5fd7cd5414ef550b4a4387014e3212fb2`
  después.
- Control posterior, sobre una copia nueva (17.229 archivos, 0 enlaces; el repo no cambió durante el control):
  - la suite sobre los cuatro grafos sellados con entrada da 0 regresiones;
  - sobre KG-Tanda0-Diez-r2a, los 56 estados y detalles son iguales a los versionados; solo cambia el sha de la
    fixture que registra.

## Escrito en el repo (sha256)

| Ruta | Contenido |
|---|---|
| `data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2/` | 47 archivos; manifiesto `d93bcc01…` |
| `data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2a/` | 35 archivos; `r2/kg.json` `99fe2bfa…` |
| `data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo_r2a/` | 21 archivos; `r2/kg.json` `93a7af72…` |
| `scripts/regression_kg_esperado.json` | `3d3f7979…` (solo `propuesta_r2_sin_sellar`) |
| `data/experiment/medicion_r2a/m1e_propuesta_r2a.py` | `6d961973560c8d122b4d0aba70333e9ae55a8b8caf99209a3e4d153b775d9981` |
| `data/experiment/medicion_r2a/m1_freno.md` | este documento |

El sha de cada archivo de los tres directorios está en el paquete de revisión (`archivos_versionados_M1.txt`).

## Pendiente de la autora

- Sellar la entrada r2: moverla de `propuesta_r2_sin_sellar` a `estado_esperado` y registrar el sha nuevo en el plan
  (decisión 4). PENDIENTE. Antes, decidir T6 y E4-b (hallazgo de M1.e).
- Commit de M1: PENDIENTE.
- M2 escribe en el tablero de correcciones sobre la versión de `d69b11f`, que ya trae la fe de erratas de las filas
  :51, :53 y :72.
