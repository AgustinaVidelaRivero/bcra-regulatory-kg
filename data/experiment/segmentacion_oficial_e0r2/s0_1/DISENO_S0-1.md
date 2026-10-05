# U-SEG-OFICIAL — S0-1: diseño de las correcciones de E0 que cambian ids, con sus censos

Etapa S0-1 del mandato FIRMADO por la autora (`e543cb2`; sha256 del texto firmado `44cf30ca0d82…`, con
`git show e543cb2:docs/mandatos/USEG_OFICIAL_segmentacion_e0r2.md | shasum -a 256`), más el punto 7 de la nota
fechada del 05/10/2026 (`b56984c`; las primeras 239 líneas del archivo en ese commit dan el mismo sha256). USD 0:
ninguna llamada a la API; Neo4j no se usa. No implementé nada en el repo: el prototipo vive en una copia del
scratchpad y va, como parche sin aplicar, en el paquete de revisión. Los censos están en `censos/` y los scripts
que los producen, en `scripts/` (§6).

## 0. Método

- Código de partida: `e0_lib.py`, `correr_e0.py` y `e0_tablas.py` del árbol de trabajo, iguales a HEAD
  (`git show HEAD:<ruta> | cmp - <copia>`); su último cambio es `9f6361e`.
- Copia armada copiando (0 enlaces simbólicos), sin bases `.db`, sin `corpus_tanda0/` y sin `logs/`.
- Base: e0-r2 de los 152 TOs de la partición (los de `segmentacion_84/b584_particion/conteos_b584.json`) con el
  código sin tocar, por TO y en paralelo (`scripts/correr_152.py`, la corrida de `r2_codigo2/c2_e0_152.py`
  repartida en procesos), y la tanda 0 con el manifiesto `tanda0_10tos.json` (`scripts/correr_tanda0.py`): 57 de 57
  archivos iguales byte a byte a `salida_tanda0_r2b/`. La base da 9.385 unidades, la cifra del mandato.
- Prototipo: cada regla es un parámetro que solo pasan los sitios de llamada de e0-r2 (con los valores por defecto
  ninguna rama nueva corre), con un interruptor por regla (`S0_REGLAS`) para correrla sola.
- Comparación por TO con el criterio de `r2_codigo2/c2_e0.py` (`comparar_to`): ids nuevos y que desaparecen, orden
  de los comunes, chunks que cambian, renglones (`scripts/comparar_e0.py`). Atribución: cada evento de la corrida
  con todas las reglas va a la regla cuya corrida sola produce el mismo evento; el acompañamiento T, por resta
  contra la corrida sin él; lo que ninguna explica sola es «interacción» y está leído (`scripts/atribuir.py`,
  `censos/atribucion_S0-1.json`).
- En los JSON de `censos/`, la clave `e0` nombra la corrida: `base_152` es la base y `final_c` la corrida final
  con el prototipo (las siete reglas y el acompañamiento T).

## 1. Resultado de conjunto (prototipo final: las siete reglas y el acompañamiento T)

Fuente: `censos/ids_que_cambian_S0-1.json` (`totales`, `tos_por_regla`, `por_to`).

- Cambian 23 de los 152 TOs: 20 con ids (423 ids nuevos y 275 que desaparecen) y 3 solo de texto (cirmo3, cryl y
  ri2_ci); 379 chunks comunes cambian. Las unidades pasan de 9.385 a 9.533 (`conteos.json`, suma de `chunks`).
- Los otros 129 TOs salen iguales byte a byte en sus cinco archivos por TO (`chunks_`, `estructura_`, `indice_`,
  `tablas_`, `pies_`); los siete archivos agregados difieren solo en las entradas de los 23.
- Cobertura de E0 exacta en los 152 (`cobertura.json`, `cobertura_exacta`).
- Tanda 0: 57 de 57 archivos iguales byte a byte a `salida_tanda0_r2b/`; `cap::4.2.1.2` igual (26.726 caracteres,
  sha256 propio `1baa2682bd64…`).

| Regla | TOs | ids nuevos | ids que desaparecen | chunks que cambian |
|---|---|--:|--:|--:|
| 1 sección escrita de otra forma | dmrd, garopt, inspag, opecam, snp_dd | 122 | 1 | 58 |
| 2 rótulos que no lo son | rdbcra, ri_dsf, ri_niif, ri_tsa | 8 | 41 | 6 |
| 3 páginas de norma fuera de unidad | fimipyme, snp_mep, venliq | 15 | 1 | 15 |
| 4 E0 de ri_spi | ri_spi | 94 | 0 | 1 |
| 5 cola de título (lista) | cirmo3, cryl, ri2_ci, snp_cheq | 0 | 0 | 19 |
| 6 unidades grandes | manori, manual, nmaeef, ri_ccna, snp_mep | 51 | 5 | 4 |
| 7 reapertura del padre | manori, rdbcra, ri_dcpc, ri_mmsef, snp_cheq | 128 | 96 | 169 |
| T acompañamiento de 1 y 7 | ri_dcpc, snp_cheq | 0 | 143 | 111 |
| interacción (leída, §2.6) | manori, ri_dsf | 10 | 0 | 0 |

Los eventos de rdbcra (5 nuevos, 12 que desaparecen y 4 que cambian) cuentan en las reglas 2 y 7, porque las dos
corridas solas los producen; por eso las filas suman más que el total. En la combinada actúa la regla 2 (§2.7).

## 2. Las siete reglas

### 2.1 Regla 1 — Sección escrita de otra forma (1.14)

**Hallazgo y censo** (`censos/censo_r1_r3_r4_base.json`, clave `r1`): 182 líneas de la zona de encabezado en 6 TOs
tienen forma de sección y `RE_SECCION` (`e0_lib.py:252`) no las lee. Las 49 de ri_dcpc («SECCION N – …») ya las lee
la variante de B5.8.2 en su modo de marcadores. Quedan 5 TOs: opecam («Seccón 3.» p. 14 y «Seccón 9.» p. 25),
garopt («Sección 2 Operaciones con títulos.», pp. 6–7), inspag («Sección 2 Modelos.», 16 líneas), snp_dd («Sección
7 – Diseño de registros», 35) y dmrd («Sección N – …», 78, en el modo sin raíz). La revisión independiente
confirmó 3 de 5 (`reports/u_revision_libre/reporte.md:104`); el censo encuentra los 5.

**Diseño.** En e0-r2, además de `RE_SECCION`, la zona de encabezado acepta `RE_SECCION_VARIANTE_R2`:
`Secci?[oó]n N` seguido de punto o dos puntos, de un guion, o de un título en mayúscula sin separador. Dos guardas,
que solo actúan donde actúa la variante: (a) la sección por variante abre o continúa solo si no retrocede respecto
de la abierta, y si no hay ninguna, solo si es la 1 (la p. 5 de dmrd es una tabla resumen cuya primera fila dice
«Sección 9 – CCRA…»); (b) en una página cuya sección se leyó por la variante, el modo sin raíz no abre raíces
sintéticas (los ítems «1.», «2.» de la sección 1 de dmrd, p. 6). La continuación de índice y el parseo del índice
no cambian.

**Resultado.** opecam: secciones 3 y 9 (`opecam::3.1`, `3.2::intro`, `3.2.1`, `3.2.2`, `3.2::cierre`, `9.1`);
`opecam::2.6` y `8.2` dejan el texto que no era suyo. garopt: 14 puntos de la sección 2 (`garopt::2.1.1` a
`2.2.6`). inspag: 16 puntos `inspag::2.x` y desaparece `inspag::S1::cierre`. snp_dd: la sección 7 (diseños de
registro, pp. 31–65) sale de `snp_dd::6.2.6`, que pasa de 50.309 caracteres declarados por tabla a 256, y da 77 ids
nuevos. dmrd: de un preámbulo (`dmrd::S0`, pp. 1–6), cinco raíces chicas que eran los ítems «1.» a «5.» de la p. 6
(`dmrd::S1` a `S5`) y `dmrd::S6` con el resto del TO (118.714 caracteres, pp. 6–72), a un preámbulo de las pp. 1–5
y las secciones 1 a 15. En dmrd salen del texto 79 renglones descartados como encabezado: 77 son las
líneas «Sección N – …» y 2 son fragmentos del título («Activos Ponderados por Riesgo», cola del encabezado corrido
de las pp. 7–9, y «tivos Ponderados por Riesgo (APR)», continuación del título partido con guion de la sección 2):
los leí, no son texto de la norma.

### 2.2 Regla 2 — Rótulos de punto que no lo son (1.15)

**Hallazgo y censo** (`censos/censo_rotulos_base.json`, `censos/censo_sin_punto_base.json`). Son falsos:
`rdbcra::2.3.1` («2.3.1. y 2.3.2. siguientes.», remisión envuelta), `ri_tsa::1.1` («1.1. de las normas sobre
“Ratio de fondeo neto estable”.»), `ri_niif::21.526` (la Ley 21.526 al inicio de renglón, que en el modo sin raíz
abre la raíz 21) y, en ri_dsf, los códigos de actividad «10.1 Producción…» a «30.9 …» (22 rótulos sin punto final
con hueco de columna después del número, que abren puntos y raíces 11 a 30). Los demás rótulos en minúscula del
censo (160) son ítems reales de listas (lingeef, gerc, snp_spd y otros); los rótulos sin punto final con hueco
aislado (`ri_oc::3.51`, `rmrtsd::1.1.2`) son reales.

**Diseño.** Un veto al final de la validación de un rótulo: actúa solo sobre un rótulo que la validación de
siempre aceptaría, y no deja abrir una raíz implícita del modo sin raíz. Motivos: `remision_envuelta_r2` (el resto
empieza en minúscula con «y/a/al/hasta N.» o «de las normas / de la Sección / del presente…»),
`numero_con_componente_de_tres_cifras_r2` y `fila_de_lista_de_codigos_r2` (sin punto final, con hueco de columna y
al menos 3 renglones así en la página). Un renglón que ya se rechazaba conserva su motivo.

**Resultado.** rdbcra: sale el falso 2.3.1 y entran los cinco subpuntos del real (`rdbcra::2.3.1.1` a `2.3.1.5`);
desaparecen las 11 intersticiales de `rdbcra::2.3`. ri_tsa: salen `ri_tsa::1.1` y `ri_tsa::S1::chapeau_seccion` y
la segunda sección 1 (la de la parte posterior al índice, sin puntos ahora) queda como `ri_tsa::S1::rep2` por la
desambiguación de siempre (la primera conserva `ri_tsa::S1`). ri_niif: sale `ri_niif::21.526`; su texto vuelve a
la unidad anterior, `ri_niif::3.2::rep2`. ri_dsf: salen los 22 códigos y las raíces 11 a 30; su texto vuelve a la sección 10, que pasa
de 26.182 y la parte E0 (§2.6).

**Límite medido: el catálogo de infracciones de rdbcra (sección 11).** Los 91 rótulos 11.x con dos o más huecos de
columna son los números del catálogo, no rótulos falsos: la regla no los toca. Lo que falla es el texto de cada
fila: la descripción de una infracción empieza renglones antes que su número y queda en la unidad anterior
(`rdbcra::11.1.2` lleva «Muy alta 800 N/A» y la descripción de otra fila). Son 13 tablas (pp. 36–48), las 13 en «más
de un chunk», y 115 unidades 11.x, 97 de ellas puntos terminales (`tablas_rdbcra.json` y `chunks_rdbcra.json` de la
base). Va a decisión de la autora (§4).

### 2.3 Regla 3 — Páginas de norma fuera de toda unidad (2.4)

**3a. Primera página de cuerpo leída como índice.** En snp_mep (p. 3), venliq (p. 3) y fimipyme (p. 4) la primera
página de cuerpo cae como «continuación de índice» (`clasificar_paginas`, `e0_lib.py:433`: dos o más líneas
«Sección N.» después de una página de índice) porque una remisión en prosa empieza renglón con «Sección 8.»,
«Sección 2.» o «Sección 4. de las normas…». **Diseño:** en e0-r2, para la continuación cuentan solo las líneas de
sección con título que empieza en mayúscula. Censo de las páginas de índice sin marcador
(`censos/censo_r1_r3_r4_base.json`, `r3a`): 7 páginas en 5 TOs; cambian las 3 de cuerpo; cajasc p. 4 y optico
pp. 3–5 son índice y siguen así. **Resultado:** snp_mep recupera 32 renglones y 7 ids (`snp_mep::1.1`, `1.2.1` a
`1.2.5`, `1.3`); venliq, 36 renglones y 7 ids (`venliq::1.1.1` a `1.1.4`, `1.2::intro`, `1.2.1`, `1.2.2`; sale
`venliq::S1::chapeau_seccion`); fimipyme, 12 renglones en `fimipyme::S1`.

**3b. ri_cc y ri_tsa: límite medido.** Son regímenes compuestos por sub-documentos «N – TÍTULO» con numeración
propia que reinicia; su primer «Índice» está en la p. 48 (ri_cc) y en la p. 62 (ri_tsa), y todo lo anterior queda
como portada, fuera de toda unidad. Censo (`censos/censo_r3b.json`): ri_cc, pp. 2–47 (46 páginas y 31.002
caracteres sin la carátula): normas generales (p. 2), balance de saldos (pp. 3–37, listado de cuentas: 380
renglones con huecos de columna y 21 de prosa) y deudores del sistema financiero (pp. 38–47, 77 renglones de
prosa); ri_tsa, pp. 3–61 (59 páginas y 70.719 caracteres sin la carátula de las pp. 1–2): sub-documentos 1 a 8, con
planillas de consolidación en las pp. 6–33. Ninguna regla de marcador lo resuelve sin un modo nuevo de E0
(sub-documento con prefijo en el id, porque la numeración reinicia y choca con la de la parte posterior al índice,
que en ri_tsa ya hoy junta dos sub-documentos). Va a decisión de la autora (§4). Los dos son regímenes informativos,
que entran con la tanda 3 según las enmiendas firmadas (`e82e22f`).

### 2.4 Regla 4 — E0 de ri_spi

**Hallazgo.** ri_spi no tiene índice ni sección: todo el TO (11 páginas) es una unidad, `ri_spi::S0` (18.565
caracteres, clase A). Su espina es «APARTADO A: …», «A.1.», «A.1.1.» (pp. 4–9); la p. 2 trae la misma lista con
guion delante («-APARTADO A:») y las pp. 10–11, los anexos I y II.

**Diseño.** Etapa 4 de la escalera de e0-r2: si el modo sin raíz deja el TO en una sola unidad y el cuerpo tiene
al menos 2 líneas «APARTADO X: …» sin guion delante, el TO se lee con el marcador de letra: la línea abre la raíz X
(sección sintética con número «A»), y «X.n.», «X.n.m.» son puntos de esa raíz, con la secuencia y el padre de
siempre («A.3.6.0.» no sucede a nada y queda como texto de `A.3.6`). Censo de la activación
(`censos/censo_r1_r3_r4_base.json`, `r4`): de los 12 TOs de una sola unidad, solo ri_spi tiene líneas
«APARTADO»; los otros con «APARTADO» (ri_oc, ri_pnp, ri_secoexpo, ri_ccpnp) tienen espina numérica y no se tocan.
`conteos.json` declara `modo_lectura` «sin_raiz_letra».

**Resultado.** 95 unidades (87 puntos `A.x`, `B.x` y `C.x`, 7 mini-chunks y el preámbulo `ri_spi::S0` de las pp.
1–3, de 3.639 caracteres). La mayor, `ri_spi::C.1.3` (5.873), lleva los anexos I y II: un anexo final queda en la
última unidad, como en el resto de E0 (límite declarado; entra en una llamada).

### 2.5 Regla 5 — Cola de título en toda página

**Medición.** La regla general (cola estricta en toda página) recupera 34 renglones en 7 TOs y mueve ids en
snp_cheq (`r2_codigo2/salidas/c2_e0.json`, `particion_152_cola_en_toda_pagina`). Leí cada página. Precisión al
texto del mandato: de los 16 renglones de los seis primeros TOs, 15 son texto de la norma y uno no: «Código
Descripción Explicación» de snp_cheq es el encabezado de una tabla de diseño de registros (pp. 89–93); es el que
abre un intersticial nuevo en 7.1 y corre la numeración. Los 18 de fabcra son celdas de su tabla002.

**Opciones medidas** (corridas con todas las demás reglas iguales; solo difiere fabcra,
`cmp_r5_lista_vs_general.json` en el paquete):
- (A) Regla general con guarda: rige en toda página si el primer renglón candidato a cola es prosa (sin huecos de
  columna). Protege a snp_cheq (ningún id se mueve) pero no a fabcra: en su p. 11 el primer renglón es
  «Funcionarios delegados:», texto real que queda entre los dos segmentos de una tabla que e0_tablas une entre
  páginas, y la tabla002 deja de serializarse («líneas no contiguas»; un chunk, ningún id).
- (B, la que propongo) Ampliar la lista `COLA_TITULO_ESTRICTA_E0_R2` (`correr_e0.py:94`) a las páginas de texto
  corrido: cirmo3 19, cryl 27, manori 6, ri2_ci 8, 9, 16 y 24, snp_cheq 80 y snp_mep 19. El universo es cerrado (152
  TOs congelados): la lista sale completa del censo. Fuera de fabcra, (A) y (B) recuperan los mismos renglones.

**Resultado de (B).** 15 renglones en 6 TOs (cirmo3 2, cryl 1, manori 1, ri2_ci 8, snp_cheq 1 y snp_mep 2), ningún
id cambia; con la regla sola cambian 23 chunks (corrida aislada). En la combinada, los de manori y snp_mep quedan
dentro de unidades que reorganizan las reglas 6 y 7.

### 2.6 Regla 6 — Unidades que no entran en una llamada de E1

**Censo recomputado y versionado** (`censos/censo_unidades_grandes_base.json`; `scripts/censo_unidades_grandes.py`)
con el código vigente. Reproduce todas las cifras del mandato: 9.385 unidades; 57 en 32 TOs sobre 13.091
caracteres con su herencia (46 por texto propio y 11 por herencia; 22 secciones sin puntos, 12 puntos terminales,
11 partes, 7 cierres, 4 chapeaux y 1 intro); la partición por tamaño partió 5 en 23 partes; 27 entre 13.091 y
26.182; 13 declaradas (11 por tabla y 2 sin ítems); los 5 mini-chunks salteados sin declarar; simulación sobre las
46 que no son partes: 30 partibles y 16 no, 19 con la parte mayor sobre 13.091 y 6 sobre 26.182; 66 unidades en 37
TOs sobre 10.937 caracteres propios y 43 en 30 TOs sobre 13.944; clases A 14, B 15, C 32 (10 partidas, 12 partes
de E0, 10 sin partir) y D 5; la clase A son las 14 del mandato.
La capacidad sale de la cota de P4 (mediana 1,175 y máximo 1,498 tokens por carácter sobre 6 unidades,
`prompt_r2/p4/salida/analisis_p4.json`, `medicion_e`): el FRENO T2 de U-REEXT-T0 no está commiteado al hacer este
diseño (`git log -- data/experiment/reext_t0` termina en `23585e2`, T1). Se recalcula con T2; la clase de una
unidad puede cambiar.

**a. Ninguna unidad salteada.** En e0-r2 un mini-chunk sobre el umbral entra a la partición por tamaño como
cualquier unidad, respetando los bloques de tabla; las partes llevan `rol_bloque`; si no se puede partir, se
declara. Resultado: `manual::S2::cierre` en 25 partes, `nmaeef::S11::chapeau_seccion` en 9 y
`ri_ccna::S8::cierre` en 8. `manori::S1::cierre` y `manori::S3::cierre` dejan de existir con la regla 7 (su texto
pasa a `manori::1.5::intro` y `manori::3.5::intro`, partidas en 4 y 4); sin la regla 7, llevan bloques de tabla y
quedan declaradas por tabla serializada. Con todas las reglas: 12 unidades partidas en 83 partes, 9 declaradas por
tabla y ninguna salteada (`sub_chunking.json` de la corrida final).

**b. La tanda 0 no cambia.** En la tanda 0 solo dos unidades pasan de 13.091: `cap::4.2.1.2` (26.726, declarada por
tabla serializada) y `ric::11.2::intro` (15.051, mini-chunk). Ningún umbral de la partición por tamaño puede bajar
de 15.052 sin tocar la tanda 0, y la opción de partir las unidades con tabla mueve `cap::4.2.1.2` (d).

**c. Clase A, una por una** (`censos/clase_A_una_por_una.json`). Propongo, además de la partición por tamaño de E0,
una partición por renglones cuando no hay ítems, cuando un ítem solo pasa el objetivo o cuando el chapeau no entra
con el primer grupo: corta después de un renglón que termina en punto, dos puntos o punto y coma (si no hay, en el
último que entra) y nunca dentro de un bloque de tabla. Rige en la partición por tamaño de E0 (más de 26.182) y en
la partición por corte de E1 (`particionar_por_corte`), con el mismo objetivo de 13.091.
- `ri_spi::S0`: la resuelve la regla 4 (queda un preámbulo de 3.639).
- `snp_mep::S7` (49.553) y `manori::S2` (45.412): las parte E0 por renglones, en 4 partes cada una (máximo 13.050).
- `dmrd::S0` (14.558 con la regla 1): por corte, 2 partes (máximo 8.594).
- `cateloc::S2` (130.099, declarada por tabla en E0): por corte, 14 partes (máximo 13.085).
- `ri_laft::3.7`, `manori::S4`, `ri_niif::3.2`, `seggar::8.2`, `ri_oc::3.51`, `ri_psp::SIII`, `ri_iepsp::S4`,
  `nmcief::S3::chapeau_seccion` y `ri_tsa::3.2`: por corte, en 2 o 3 partes, con la mayor entre 10.175 y 13.076.
Con esto, sobre la salida final (`censos/censo_unidades_grandes_final_e1_r6.json`): ninguna unidad en las clases A
ni B; 87 en la C (50 partes de E0, 28 partidas y 9 sin partir) y 7 en la D. Con la partición por corte de hoy
(`censos/censo_unidades_grandes_final_e1_hoy.json`) quedarían 14 en la A (entre ellas `dmrd::S4`, `S7` y `S8`, que
la regla 1 separa). Límite declarado: con la razón máxima de P4 (1,498) la capacidad del reintento es 10.937, y
las partes de hasta 13.091 quedan en el borde (clase C): el objetivo se fija con la medición de T2.

**d. Tablas, partes grandes y umbral.**
- Partir respetando bloques las unidades que hoy se declaran por tabla serializada: las 9 de los 152 darían 63
  partes en 8 TOs (todas de 13.085 o menos; 7 de esos TOs no los toca ninguna otra regla), y en la tanda 0
  `cap::4.2.1.2` pasa a 3 partes (cambian `chunks_cap.json`, `conteos.json` y `sub_chunking.json`). Choca con b:
  propongo no hacerlo en E0 y que las tome la partición por corte de E1 (c), que ya respeta los bloques.
- Parte que sigue grande: con la partición por renglones de c, ninguna parte de E0 pasa de 13.091.
- Umbral: bajarlo a 15.052, el mínimo que no toca la tanda 0, partiría 20 unidades de 15 TOs en 48 partes
  (`censos/simulacion_umbral_15052.json`), varias en TOs que hoy ninguna regla toca. Propongo mantener 26.182.

### 2.7 Regla 7 (punto 7) — Párrafos sin numerar que empiezan con un número de punto

**Censo recomputado** con el código vigente (`censos/censo_p7_base.json`): 36 intersticiales, con el mismo reparto
de la verificación del 03/10/2026: 27 en ri_mmsef (todos de `ri_mmsef::S2`), 6 en rdbcra (`rdbcra::2.3`), 2 en
ri_dcpc (`ri_dcpc::3.1`) y 1 en snp_cheq (`snp_cheq::S3`); 28 atribuidos a una sección y 8 a un punto. La lista,
con id y primera línea, está en el archivo.

**Mecanismo.** Dos causas. En rdbcra, el 2.3.1 real («Factores de ponderación…», p. 14) se rechaza porque antes
se aceptó la remisión «2.3.1. y 2.3.2. siguientes.», y sus cinco subpuntos no encuentran padre. En ri_mmsef,
ri_dcpc y snp_cheq el rótulo del padre (2.2, 3.1.3 y 3.2.2, 3.1.4) está en la columna del texto de un ancestro: la
prosa que sigue se re-ancla al ancestro y cierra el punto, y sus hijos se rechazan por «padre no abierto». En
snp_cheq la prosa re-anclada (pp. 25–27) es la continuación de 3.1.4.2 «Feriados locales» con otro margen.

**Diseño.** Reapertura del padre: un rótulo con título en mayúscula, rechazado solo porque su padre no está abierto,
reabre ese padre si es el último hijo de la cadena que baja desde el nodo abierto más profundo (nada se abrió
después); la prosa que el re-anclaje le dio a un ancestro después de la última línea del padre vuelve a él, o a su
último hijo si es terminal (la continuación). Queda un aviso `padre_reabierto_r2`. La guarda de mayúscula deja fuera
las remisiones envueltas: en la tanda 0 los 14 rechazos de ese tipo con padre existente (cap 4, ext 9 y ric 1) son
remisiones en minúscula o cifras.

**Resultado.** Los 36 pasan a 0 (`censos/censo_p7_final.json`). Con la regla sola, 11 reaperturas en 5 TOs
(`estructura_<to>.json`, avisos `padre_reabierto_r2`): ri_mmsef 1 (de ella cuelgan los 27), ri_dcpc 5, snp_cheq 1,
rdbcra 1 y manori 3.

**Cruces, caso por caso.**
- Con la regla 2 (rdbcra): actúa primero la 2 (veto del rótulo falso); después el 2.3.1 real se acepta por la
  validación de siempre y la 7 no tiene nada que reabrir. Con la 7 sola, reabre el 2.3.1 falso y le cuelga los
  cinco subpuntos: por eso el orden importa y la 2 va antes.
- Con la regla 1: la 7 no actúa sobre rechazos «fuera de sección» (los que deja una sección sin leer); en los cinco
  TOs de la regla 1 no hay reaperturas. La regla 1 en snp_dd y la 7 en manori dejan tablas partidas en
  intersticiales: lo resuelve el acompañamiento T (§2.8).
- Con la guarda de snp_cheq de la regla 5: actúan en partes distintas del TO. La 7 reorganiza la sección 3 (las 30
  intersticiales de `snp_cheq::S3`, de las pp. 25–27, vuelven a 3.1.4.2, 3.1.4.3 y 3.1.4.4); la lista de la
  regla 5 recupera un renglón en la p. 80 (sección 7) sin abrir intersticiales; el encabezado de tabla de las pp.
  89–93, que es el que movía los ids de 7.1, queda fuera de la lista. El acompañamiento T sí renumera
  intersticiales de snp_cheq (fusiona las 6 tablas partidas de la base).
- Interacciones leídas (`atribucion_S0-1.json`, `interaccion`): en manori la 6 parte `manori::1.5::intro`, que crea
  la 7 (8 ids); en ri_dsf la 6 parte en 4 la sección 10 que agranda la 2 (2 ids).

**Lo que no alcanza (límite medido;** `censos/censo_p7_resto_base.json` y `_final.json`**).** Fuera de los
intersticiales, hay 101 rótulos con título en mayúscula rechazados por «padre no abierto» con el padre existente;
la regla resuelve 31 y quedan 70: manori 58, snp_tr 3, snp_tr_nc 3, cirmo3 2, depaho 1, ri_cc 1, ri_mmsef 1 y
ri_rml 1. En manori es otro mecanismo: la p. 3 trae una lista interna de 1.1 a 1.5 que E0 lee como puntos vacíos;
el 1.1 real de la p. 4 se rechaza y sus subpuntos no encuentran padre (el mismo patrón de lista leída como cuerpo
aparece en ri_niif p. 1 y en dmrd p. 6). Va a decisión de la autora (§4).

### 2.8 Acompañamiento T de las reglas 1 y 7 — una tabla partida en intersticiales

Si las líneas de una tabla marcada caen en dos o más intersticiales de un mismo nodo y de un mismo hueco entre
hijos, esos segmentos se funden en uno antes de armar los chunks: la tabla queda en un solo chunk y se serializa.
En la base ya hay 8 tablas así (ri_dcpc 2 y snp_cheq 6); sin el acompañamiento, las reglas 1 y 7 suman 8 más
(snp_dd 5 y manori 3) y 9 tablas dejan de serializarse. Con él, en los 152: 467 tablas serializadas (460 en la
base), 18 en «más de un chunk» (26) y ninguna partida en intersticiales (8). En los cuatro TOs, las intersticiales
pasan de 375 (base) a 559 (reglas sin T) y a 293 (con T). No toca TOs que las reglas no toquen. Cambia la
numeración de intersticiales de ri_dcpc y snp_cheq (el orden de los ids comunes cambia en esos dos TOs).

## 3. Condiciones de aceptación de S0-1

- Tanda 0 con el prototipo: 57 de 57 iguales byte a byte; `cap::4.2.1.2` no cambia.
- TOs que ninguna regla toca: 129, iguales byte a byte en sus cinco archivos por TO y en sus entradas de los
  agregados (los mismos ids).
- Las 14 de la clase A: §2.6 c, una por una.
- Los cinco mini-chunks salteados: §2.6 a.
- Cada regla con su lista de TOs e ids: `censos/ids_que_cambian_S0-1.json` (por TO: ids nuevos, ids que
  desaparecen, chunks que cambian y la regla de cada evento).
- Prototipo como parche, sin aplicar, en el paquete: completo y partido por regla, con un índice de trozos; aplicar
  los trozos en orden sobre el código del repo reproduce el prototipo byte a byte.

## 4. Decisiones de la autora

1. **Regla 5:** (B) ampliar la lista de páginas (propuesta; 6 TOs, 15 renglones, ningún id) o (A) regla general con
   guarda (además, fabcra: un chunk, la tabla002 deja de serializarse; ningún id).
2. **Acompañamiento T:** adoptarlo (467 tablas serializadas; renumera intersticiales de ri_dcpc y snp_cheq) o no
   (las reglas 1 y 7 dejan 9 tablas sin serializar y 559 intersticiales en los cuatro TOs). Propongo adoptarlo.
3. **Regla 3b (ri_cc, ri_tsa):** (i) unidad propia con un modo de sub-documento en E0 (ids nuevos con prefijo; puede
   tocar ids de la parte posterior al índice de ri_tsa); (ii) declararlas en el manifiesto de S1 como páginas de
   norma sin unidad, con su censo, para la vía de páginas de la tanda 3 (propuesta para esta release: E0 no cambia);
   (iii) dejarlas fuera, declaradas.
4. **Regla 6:** el objetivo de las partes (13.091 hoy; 10.937 con la razón máxima de P4), que fijo con la medición de
   T2; partir en E0 las unidades con tabla (mueve `cap::4.2.1.2` de la tanda 0; propongo no); bajar el umbral a
   15.052 (20 unidades, 15 TOs; propongo no).
5. **Catálogo de rdbcra:** una regla que ancle cada renglón a su fila por la geometría de la tabla (cambia el texto
   de las 97 unidades terminales 11.x, ningún id) o límite declarado.
6. **Lista de puntos leída como cuerpo** (manori, con 58 subpuntos sin padre; ri_niif p. 1; dmrd p. 6): regla nueva,
   fuera de las siete, o límite declarado.

## 5. Para S0-2

- Orden de las reglas en el código: la 2 (veto) antes que la 7; la 1 antes que la cola de título; T después de
  asignar las tablas y antes de serializar; la 6 al final, sobre los chunks.
- Los interruptores del prototipo (`S0_REGLAS`, `S0_PARTIR_TABLAS`) son de medición: en S0-2 las reglas quedan como
  constantes de e0-r2.
- Tabla de reprocesamiento (`data/experiment/mantenimiento/tabla_reprocesamiento.md`): el texto propio que cambia
  es F01 (la cola estricta ya está nombrada ahí); la herencia que cambia, F02 o F03; un id renombrado sin cambio de
  texto (`ri_tsa::S1::rep2`), F05. Unidades que aparecen o desaparecen por un cambio de segmentación: S0-2 tiene que
  ver si F01 las cubre o hace falta una fila nueva (se propone en el freno, no se escribe). En la tanda 0 ninguna
  fila se dispara: su E0 no cambia un byte.
- La capacidad de E1 y el objetivo de las partes se recalculan con T2.

## 6. Comandos

Desde el scratchpad, con `PYTHONDONTWRITEBYTECODE=1` y el python de `.venv` con `-B`; `<copia>` es una copia del repo
sin enlaces (con el prototipo, para las corridas de las reglas) y `S0_REGLAS` elige las reglas del prototipo.
```
scripts/lineas_152.py <copia> <cache>
scripts/correr_152.py --codigo <copia> --salida <dir> [--workers 7] [--tos a,b]
scripts/correr_tanda0.py --codigo <copia> --salida <dir>
scripts/comparar_e0.py <dir base> <dir nuevo> <salida.json> [--tos a,b]
scripts/atribuir.py --base <base> --todas <final> --regla r1=<dir>[,<dir>] … --resta T=<dir>[,<dir>] --out <json>
scripts/ids_que_cambian.py <comparación> <atribución> <salida>
scripts/censo_unidades_grandes.py --e0 <dir> --codigo <copia> --out <json>
scripts/censo_rotulos.py <copia> <cache> <salida>      scripts/censo_sin_punto.py <copia> <cache> <salida>
scripts/censo_r1_r3_r4.py <copia> <cache> <salida>     scripts/censo_r3b.py <copia> <cache> <salida>
scripts/censo_p7.py <dir> <salida>                     scripts/censo_p7_resto.py <dir> <salida>
scripts/clase_a_una_por_una.py <base> <final> <copia con el prototipo> <salida>
scripts/simular_umbral.py <dir> <copia con el prototipo> 15052 <salida>
scripts/partir_parche.py <e0_chunking del repo> <e0_chunking del prototipo> <salida>
```
