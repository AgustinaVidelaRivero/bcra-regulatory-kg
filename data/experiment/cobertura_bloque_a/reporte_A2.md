# U-COB-A fase A.2 — corrida de extracción sobre los NUEVE

**FRENO.** Gasto **USD 0,7399** de tope USD 4,00. **191/191 unidades**, cero
errores, cero reintentos por corte, `stop_reason = tool_use` en las 191.

Verificadores: `python3 code/verificar_a2.py` (12 comprobaciones de integridad
y cruce, cero fallas, mas los 10 veredictos de prediccion, desde `/tmp`) y `python3 code/verificar_a1.py` (68, cero
fallas). Batería de regresión **corrida ANTES de gastar**: 307 checks verdes
(§7).

---

## 1. Los diez veredictos, contra los umbrales SELLADOS en la v4

Pre-registro `prerregistro_A2_v4.md`, sha
`87fae986a8dc5370bef67c65e257409b26653a021f262e007d3348f21657b0ff`,
**recomputado por el propio runner antes de la primera llamada**.

| # | predicción | umbral sellado | medido | veredicto |
|---|---|---|---|---|
| PR-1 | cero tipo/predicado fuera de lista | 0 | **0** | **CUMPLE** |
| PR-2 | rinde ≥ 80 % | ≥ 80 % | **65/77 = 84,4 %** | **CUMPLE** |
| PR-3 | Obligacion domina y ≥ 45 % | ≥ 45 % | **37,7 %**; dominancia **NO EVALUABLE** (52 vs 51) | **FALLA el umbral** |
| PR-4 | `aplica_a` en (42,9 % ; 53,1 %) | intervalo | **13/77 = 16,9 %** | **FALLA por el PISO** |
| PR-5 | ≥ 1 label con palabra partida | ≥ 1 | **0** | **FALLA** |
| PL-1 | cero tipo/predicado fuera de lista | 0 | **0** | **CUMPLE** |
| PL-2 | rinde < 50 % | < 50 % | **17/114 = 14,9 %** | **CUMPLE** |
| PL-3 | ≥ 1 testigo RX-10 | ≥ 1 | **sí, con caso citado** | **CUMPLE** |
| PL-4 | Obligacion < 25 % | < 25 % | **0,0 %** (cero Obligacion) | **CUMPLE** |
| PL-5 | prosa < filas tabulares | < | **13 < 27** | **CUMPLE** |

**7 cumplen, 3 fallan.** De las tres falladas, **dos son de caracterización**
(PR-3 y PR-5) y por la línea de cierre de §6 **no gatean ingreso**.

## 2. Qué ENTRA al recurso, aplicando §6 de la v4

**Disparan dos filas, y cada una decide su brazo** — que es exactamente para lo
que se emitió la v4:

- **Fila 1** («PR-2 se cumple y PR-4 no falla por el techo · PL-2 y PL-4 se
  cumplen») → **el brazo planilla NO entra**: se declara, con su medición, y su
  tratamiento pasa al bloque B.
- **Fila 5** (falla PR-4 por el piso) → **ENTRA el brazo prosa, con residuo
  declarado por documento** (§3). **Sin exclusión de ningún documento.**
- La fila de PR-1/PL-1 **no dispara**: no hubo freno de ingreso.

**Resultado: entran las 77 unidades de prosa con
`granularidad_procedencia = pagina`; las 114 de planilla quedan declaradas y
fuera.** Con la v3 esta corrida habría dejado la planilla sin fila que la
decidiera.

## 3. Residuo declarado por documento (obligación de la fila 5)

Tasa emitida contra **tasa literal propia** de cada TO, que es la base de
comparación que fija §4 — no el 42,9 % del brazo.

| TO | unid. | rinde | tasa literal propia | `aplica_a` emitido |
|---|--:|--:|--:|--:|
| `ri_tii` | 25 | 92,0 % | 76,0 % | **20,0 %** |
| `ri_con` | 14 | 92,9 % | 28,6 % | 14,3 % |
| `ri_rem` | 11 | 81,8 % | **0 %** | **0 %** |
| `ri_itme` | 11 | 72,7 % | 27,3 % | 9,1 % |
| `ri_pspii` | 5 | 60,0 % | 40,0 % | 20,0 % |
| `ri_chr` | 4 | 100 % | 25,0 % | 0 % |
| `ri_fcem` | 4 | 75,0 % | 50,0 % | 50,0 % |
| `ri_pfmipyme` | 2 | 50,0 % | 50,0 % | 50,0 % |
| `ri_pscpp` | 1 | 100 % | 100 % | 100 % |
| **brazo** | **77** | **84,4 %** | **42,9 %** | **16,9 %** |

**`ri_rem` CONFORMA**: 0 de 11 bloques nombran sujeto y emitió **cero** aristas
`aplica_a` — el caso límite que §4 declaró antes de medir, cumplido al pie.

**`ri_tii` concentra la brecha aparente** (76,0 % de tasa literal contra 20,0 %
emitido), y la adjudicación de causa dice por qué: de sus 14 casos de Prioridad
2, **12 son menciones que no son destinatarios** —definiciones de códigos de
partida y remisiones— y **2 son chapeaux huérfanos** («Para entidades
financieras:», «Para PSPCP:») que el corte por página separó de las partidas
que encabezan. Ver `adjudicacion_pr4.md`. **El residuo de `ri_tii` no es
omisión de sujeto: es sobrecuenta de la marca más un defecto localizado del
corte.** Sin la partición, este párrafo habría atribuido la brecha al modelo.

## 4. Cruce 2×2 de PR-4 — **ES TAMIZ, NO MEDICIÓN**

**Qué testea la marca literal: COINCIDENCIA LÉXICA** sobre el texto de la
unidad contra las 70 entradas del catálogo del esquema congelado — **no
posición de destinatario**. Es cota inferior: no resuelve anáfora ni sujeto
heredado del encabezado, y una mención no siempre es el destinatario. **El piso
de PR-4 (42,9 %) está fijado sobre esa cota, con falsos positivos posibles.**

| estrato | n |
|---|--:|
| **EMISIÓN SIN MENCIÓN LITERAL — PRIORIDAD 1 DE REVISIÓN MANUAL** | **2** |
| **MENCIÓN LITERAL SIN EMISIÓN — PRIORIDAD 2** | **22** |
| CONCORDANTE | 11 |
| SILENCIO CONCORDANTE | 42 |
| suma | **77** |

Controles: mención literal = 11 + 22 = **33** (idéntico a la marca de A.1);
`aplica_a` = 11 + 2 = **13**.

**Lo que el cruce distingue y el agregado no**: la caída de PR-4 **no** es
invención compensando omisión. **Prioridad 1 = 2 casos** (`ri_con` 1,
`ri_fcem` 1): el extractor prácticamente no emitió sujetos donde el texto no
los nombra. **La caída es casi enteramente Prioridad 2 — 22 casos, de los
cuales 14 son de `ri_tii`** (64 %): menciones literales sin arista emitida.

**Ninguna cifra de este cruce dispara retiro por sí sola**: el principio §1 se
aplica sobre casos revisados, no sobre el tamaño de un estrato. Los 24 casos de
Prioridad 1 y 2 van citados uno por uno en `medicion_a2.json`.

## 5. PL-3 y PL-5 — el material de planilla, con su evidencia

**PL-3 (testigo RX-10), con caso citado.** `ri_tii::p3.b1`, verbatim del texto
que recibió el extractor:

```
Tipos de Código de Cantidad Código Monto Concepto transferencias moneda
total de Partida total Tabla 1 Tabla 2 operac. 1010000 De CBU PSPCP patrocinad…
```

Los encabezados de siete columnas quedan intercalados antes de los datos: es
RX-10 exacto. Otro caso, `ri_con::p3.b3`: «Efectivo y Depósitos en Bancos
Efectivo Entidades financieras y corresponsales B.C.R.A. Otras del país Del
exterior Otras» — rótulo de fila y valores de columna fundidos.

**PL-5.** Sobre las mismas `ri_tii` p.3-4: la lectura tabular sellada de B5.8.3
da **5 tablas lógicas / 27 filas**; la lectura de prosa da **13 entidades bien
formadas**. La lectura de prosa recupera **menos de la mitad** de lo que la
tabular estructura sobre el mismo material.

**Composición del brazo planilla**: 32 entidades en 114 unidades — 21
`Definicion`, 10 `Operacion`, 1 `Restriccion`, **cero `Obligacion`**. El
extractor **no alucinó modalidad deóntica sobre un formulario**, que era el
riesgo que PL-4 vigilaba.

## 6. Cinco hallazgos

**(a) PR-1 no falló, pero hubo 2 firmas inválidas — y no son lo mismo.** PR-1
dice textual «cero emisiones de **tipo o de predicado** fuera de los 9 y los
13», y eso se cumplió: **cero**. Los 2 rechazos son `firma_invalida`, donde
tipos y predicado **sí** son del vocabulario y lo que falla es la matriz
dominio/rango:

```
[ri_tii::p6.b1] relations[1]: Condicion --condicion_de--> Operacion
[ri_rem::p1.b7] relations[2]: TextoOrdenado --referencia--> TextoOrdenado
```

`condicion_de` tiene rango {Obligacion, Restriccion, Excepcion} y `referencia`
va a Comunicacion. **El validador los rechazó correctamente y nada entró mal.**
Lo registro porque mi primera versión del medidor los agrupó con PR-1, lo que
habría reportado un freno de ingreso inexistente; corregido antes de publicar.

**(b) PR-5 falló, y la falla es buena noticia.** 30 de las 77 unidades de prosa
contienen palabras partidas por guión en su texto de entrada, y el extractor
emitió **cero** labels con palabra partida: **normaliza la partición silábica
al generar el label**. El arrastre medido en A.1 no llega al grafo por esta vía.
No cierra el asunto —el texto del chunk sigue partido— pero acota el daño.

**(c) El detector de flags de producción no ve la planilla.** Solo **16 de las
114** unidades de planilla activan `contenido_tabular` de
`e0_lib._flags_tabla_formula`. No lo elegí: apliqué el detector de producción
para no sesgar PL-2/PL-4. Tercera vez que el mismo material resulta invisible a
un instrumento del pipeline (parser de prosa, parser de tablas, detector de
flags).

**(d-corregido) PR-3: el umbral falla; la dominancia NO ES EVALUABLE.** La
mitad de umbral de PR-3 **falla**: 37,7 % contra el ≥45 % predicho. La mitad de
dominancia **no es evaluable con este n**: `Obligacion` 52 contra `Operacion`
51 sobre 138 entidades es **una entidad de diferencia — 37,7 % contra 37,0 %**,
un empate dentro del ruido. Escribir «Obligacion domina» sobre ese margen sería
leer una señal donde hay ruido. Se reporta como empate, no como dominancia.

**(e) El mensaje de producción llama «punto» a lo que no lo es.** Toda unidad
viajó con «Tipo de unidad: chunk de punto» y «Punto del chunk: p1.b0 — » (con
el título vacío, porque estos documentos no titulan sus bloques). **No edité el
módulo de producción**: el pre-registro exige el prefijo cableado sin tocar. Es
candidato a corrección en el mandato que cablee el bloque A al escalado.

## 7. Guarda 1 — batería corrida ANTES de gastar

Con el desdoblamiento de intérpretes que fija la autorización, de modo que no
apareció el freno falso de los 9 deltas de bbox.

| selftest | intérprete | resultado |
|---|---|---|
| `selftest_e0` | `python3` 3.12 | 57/57 |
| `selftest_b52` | `python3` 3.12 | 39/39 |
| `selftest_b581` | `python3` 3.12 | 34/34 |
| `selftest_b582` | `python3` 3.12 | 59/59 |
| `selftest_b583` | `python3` 3.12 | 33/33 |
| `selftest_ub53` | `.venv/bin/python3` 3.10 | 40/40 |
| `selftest_cablev3` | `.venv/bin/python3` 3.10 | 45/45 |
| **total** | | **307, cero fallas** |

Ningún módulo de segmentación tocado; `e0_lib.py`, `e0_tablas.py` y
`prompt_congelado.py` idénticos a HEAD.

## 8. Cableado y candados

- **Perfil `v3_b54`** — el prefijo v3 cableado, que integra el esquema
  CONGELADO. Su constructor **recomputa sha256 y hash y frena si no
  reproducen**: pasó (`54a111e2175f`).
- **Candado propio del runner**: recomputa el sha del pre-registro v4 y aborta
  si difiere. Pasó antes de la primera llamada.
- **`CachingClient`** (never-pay-twice + captura del crudo íntegro), DB propia
  de la unidad, contabilidad D2 con la fórmula de caching, tope duro, y
  **secuencial** por la decisión 4 de `docs/decisiones_caching_extraccion.md`.

## 9. Defecto propio, declarado con causa (regla e)

Mi primer lanzamiento abortó en la unidad 1 con `AttributeError: 'tuple' object
has no attribute 'content'`. **Causa**: usé el retorno de
`cliente_e1.crear_con_reintento_corte` con el contrato de
`cliente_e1.extraer_chunk` — la primera devuelve `(response_final,
response_del_corte_o_None)` y la segunda un dict. Corregido desempaquetando la
tupla y registrando `reintento_por_corte` por unidad.

**Costo del error: cero llamadas re-pagadas.** La única llamada que alcanzó a
hacerse quedó en la caché y la corrida definitiva la tomó como hit — es el
`hits 1/191` del log. El never-pay-twice hizo exactamente lo que existe para
hacer.

## 10. Cambios en el árbol que NO son míos, registrados

`git status` muestra `data/experiment/reextraccion_v2/corpus_v2/ensamblar_corpus.py`
modificado (+124 lineas) y `data/experiment/esq_v3_miembros/` sin seguimiento.
**No son mios**: el propio diff los atribuye a **U-ESQ-V3** (inyeccion del paso
de esqueleto al ensamblado bajo perfil `v3_b54`), y `esq_v3_miembros/` ya
figuraba en el freno anterior. Mis escrituras son exclusivamente
`data/experiment/cobertura_bloque_a/`, y esta unidad **nunca importo**
`ensamblar_corpus.py`. Tampoco toque `docs/`, `esq_v3_miembros/` ni
`adjudicar.py`. Lo registro por la regla j: la accion es de la autora y no la
afirmo mas alla de lo que muestran el diff y `git status`.

**Nota de coordinacion**: U-ESQ-V3 cambia el ensamblado **para el mismo perfil
`v3_b54`** con el que corrio A.2. Esta corrida produjo extracciones E1, no
ensamblado, de modo que no hay interferencia con lo medido aca; pero el ingreso
al recurso de las 77 unidades de prosa pasara por ese ensamblado, y conviene
que las dos unidades se coordinen en ese punto.

## 11. Lo que queda para el laudo de la autora

1. **Los 24 casos de Prioridad 1 y 2**, citados uno por uno en
   `medicion_a2.json`. La adjudicación sobre casos revisados es suya; ninguna
   cifra del tamiz dispara retiro por sí sola.
2. **`ri_tii`**: 14 de los 22 casos de Prioridad 2. Es el documento que
   sostenía el piso de PR-4 y el que más se aparta de su tasa propia.
3. **El brazo planilla**, declarado y fuera del recurso por la fila 1: su
   material está extraído y medido, y su tratamiento pasa al bloque B.
4. **PR-3 fallada** (Obligacion 37,7 % contra el ≥45 % predicho, aunque domina):
   caracterización, no gatea ingreso, pero es insumo del capítulo.
