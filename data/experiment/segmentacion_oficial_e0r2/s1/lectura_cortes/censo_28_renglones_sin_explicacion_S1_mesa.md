# Punto 3 — Los 28 renglones sin explicación del censo de S1 (leídos contra la página)

Fuente: `s1/explicacion_censo_S1.json` (`explicacion_posterior = sin_explicacion`, 28 en 19 TOs). Cada renglón leído en
la página renderizada (`pdftoppm -r 110`). La regla que lo descarta la confirmé corriendo `e0_lib.separar_encabezado_pie`
(código de `26c6502`, copia) sobre la página, con los argumentos de e0-r2 (`scripts_mesa/diag_encabezado.py`). Ningún
renglón está en una página con el rol mal asignado: las 25 páginas tienen rol de cuerpo y lo son.

## Con pérdida (13 renglones en 7 TOs: 11 de texto en 6 TOs, de ellos 7 de texto de norma en 3 TOs, y 2 signos de fórmula)

| # | TO | p. | r. | qué dice en la página | qué se pierde | causa (regla de E0) |
|---|---|---|---|---|---|---|
| 7-8 | fimipyme | 4 | 4-5 | «Las entidades financieras que estén comprendidas en el Grupo “A” –conforme a lo previsto en la / Sección 4. de las normas sobre “Autoridades de entidades financieras”, para lo cual el indicador del» | **texto de norma**: los dos primeros renglones del único párrafo de la sección 1 (quién está alcanzado); `fimipyme::S1` empieza en «punto 4.1. de esas normas…» | e0-r2, K (`e0_lib.py:851-867` y `:894-896`, zona de 5 renglones `:858` y `:868`): en la zona de 5 renglones, todo lo que precede a la última línea de sección es encabezado; el renglón 5 empieza con «Sección 4.» (remisión a otra norma) y cierra el encabezado. La excepción K-a′ cubre solo «B.C.R.A.», no la línea de sección. Caso que ninguna regla de S0 cubre |
| 15-16 | ri2_ci | 5 | 4-5 | «abordando las expectativas, las responsabilidades de los indivi- / duos y grupos, teniendo en cuenta la clasificación y confidenciali-» (negrita) | **texto de norma**: dos renglones de `ri2_ci::1.1.1.4`, que queda «…en un sentido más amplio, / dad de la información…» | cola envuelta del título de sección (`e0_lib.py:912-925`): renglón inmediato a ≤ 16 pt sin numeración se pega al título «Sección 1. Aspectos generales». La p. 5 no está en la lista de la regla 5 (`correr_e0.py:108-110`) y la cola estricta tampoco lo salva (`continua_titulo`, `:929-941`, acepta el renglón que empieza en minúscula). No mira el x0 (139,4 del título contra 184,3 del texto). Caso que ninguna regla cubre |
| 17-18 | ri_cc | 60 | 4-5 | «- Financiaciones cubiertas con garantías o avales otorgados por sociedades de garantía recípro- / ca inscriptas en el registro habilitado en el B.C.R.A. o por fondos provinciales constituidos con» | **texto de norma**: el ítem de la categoría de ponderación (sección 3, capitales mínimos); en `ri_cc::S3::chapeau_seccion` queda solo «igual objeto al de esas sociedades…» | K (`e0_lib.py:857-867`): el renglón 5 contiene «B.C.R.A.» y cierra el encabezado; K-a′ no aplica porque el renglón previo es un ítem con guion, no un punto numerado |
| 19 | ri_cc | 62 | 4 | «4. Facilidades Otorgadas por el B.C.R.A.» | **título de punto**: se pierde el rótulo del punto 4 y su texto (4.1, 4.2) queda dentro de `ri_cc::3.3` | descarte genérico de un renglón con «B.C.R.A.» en la zona (`e0_lib.py:897-905`), que no tiene la excepción K-a′ (esa solo cuenta para las forzadas) |
| 11 | nmaeef | 63 | 5 | «EXTERNO/A DE ENTIDADES SUJETAS AL CONTROL DEL B.C.R.A. (aplicable también a» | título del modelo de nota del Anexo V (renglones 4-5 de 6) | K (`e0_lib.py:857-867`), como ri_cc p. 60 |
| 26 | snp_cheq | 71 | 4 | «ii) Cabecera de lote» | título del ítem ii (su párrafo sí está) | cola de título: «una línea que arranca con numeración nunca es cola» mira solo `RE_NUM_TOKEN`; un inciso romano «ii)» pasa como cola |
| 5 | fabcra | 11 | 4 | «Funcionarios delegados:» | rótulo de la segunda tabla del modelo 1.7.3 | cola de título histórica; la p. 11 quedó fuera de la regla 5 a propósito (`correr_e0.py:106`, la tabla002 dejaría de serializarse). Declarado |
| 27 | snp_cheq | 92 | 5 | «Código Descripción Explicación» | encabezado de columnas de una tabla | cola de título histórica; pp. 89-93 fuera de la regla 5 a propósito (`correr_e0.py:107`). Declarado |
| 22-23 | ri_rml | 48 / 54 | 28 / 9 | «]» y «______» | signos de fórmula (corchete y raya de fracción), sin texto | ningún renglón de unidad los contiene; elemento gráfico de fórmula |

## Sin pérdida (15 renglones en 13 TOs)

| # | TO | p. | r. | qué es |
|---|---|---|---|---|
| 1 | adrei | 17 | 5 | «Cambiarias.», cola del título de la sección 5 dentro del recuadro del encabezado |
| 2 | cryl | 27 | 3 | línea de sección del recuadro («Sección 12. Modelo de notas…») |
| 3 | dmrd | 9 | 1 | título del recuadro con errata («divultgación»): por eso no se repite |
| 4 | dmrd | 15 | 4 | título de la sección 4 repetido en el cuerpo, bajo el recuadro; la sección lo trae como título |
| 6 | fabcra | 13 | 6 | «(...) .……………..»: está en `fabcra::1.7.4`; la comparación del censo no lo encontró |
| 9 | icmecma | 18 | 3 | línea de sección del recuadro con errata («recientos») |
| 10 | manual | 4 | 16 | «Circular CONAU 1 – 1», segunda línea del pie |
| 12-13 | opecam | 14 / 25 | 3 | línea de sección del recuadro con errata («Seccón») |
| 14 | retype | 7 | 3 | línea de sección del recuadro |
| 20 | ri_dsf | 25 | 2 | «Anexo I a la», celda derecha del recuadro |
| 21 | ri_rcl | 1 | 3 | «21. Ratio de Cobertura de Liquidez», fila del recuadro |
| 24 | ri_spi | 9 | 4 | primer renglón del título del apartado C: va en la herencia reescrito como «C. DENUNCIAS…» (regla 4) |
| 25 | seguef | 12 | 3 | línea de sección del recuadro sin tilde («Seccion») |
| 28 | snp_psp | 19 | 3 | «actividades ilícitas», cola del título de la sección 7 en el recuadro |

## Lo que pediría S0-3

1. Zona de encabezado (K): que una línea de sección o con «B.C.R.A.» cierre el encabezado solo si está en el recuadro
   (antes de la primera línea de prosa, o por x0/top), no si es prosa de la norma: fimipyme p. 4, ri_cc p. 60 y p. 62,
   nmaeef p. 63. Extender K-a′ a la línea de sección y al descarte genérico de `:897`.
2. Cola del título: exigir el x0 del título (o el interlineado del recuadro) y tratar los incisos («ii)», «a)») como
   numeración: ri2_ci p. 5 y snp_cheq p. 71.
Las dos son casos que ninguna regla de S0 cubre. Los 7 renglones de texto de norma perdidos son de fimipyme (2), ri2_ci (2)
y ri_cc (3, uno de ellos el título del punto 4). Conteo: 13 con pérdida + 15 sin pérdida = 28; 7 + 13 TOs menos fabcra, que
está en las dos listas = 19.
