# U-SEG-OFICIAL — Diseño de S0-6a-bis: la corrección de E0 con los ajustes de la autora (12/10/2026)

**Este archivo nombra unidades con error de corte y de herencia: ninguna lectura a ciegas lo abre, tampoco la de
S1-quater.** Texto de unidades: solo de las 40 filas y de las 286 leídas en S1-ter; de las demás, solo cuentas por regla y
por documento, sin ids (los ids, en los archivos `NO_ABRIR_` del paquete).

Fuentes: el mandato `docs/mandatos/USEG_OFICIAL_S0-6a_correccion_E0.md` (leído en HEAD `d32f6db8`, sha256 `5edfd993…`),
con el «seguí» de S0-6a-bis (decisiones de la autora del 12/10/2026, que rigen donde difieren); los cuatro extractos de
`para_la_ejecutora_S0-6a/` (los mismos sha256 del despacho de S0-6a) y la clasificación de la mesa de los 70 cambios en
leídas (`cambios_en_leidas_S0-6a_clasificados_mesa.md`, `b2cb4709…`), que la autora aceptó. Código de partida: el de S0-5b
(el del repo); el parche de esta etapa es completo sobre él, y reemplaza al de S0-6a. Diseño de S0-6a: `../DISENO_S0-6a.md`.

## 1. Lo que se queda (decisión 1)

B, D, F, G y la parte de A que mejora quedan como estaban en S0-6a. Las reglas H, I, J, K y E tampoco cambian.

## 2. C y A, ajustadas (decisión 2)

Las definiciones las fijé y las anoté antes de correr el censo, y no las ajusté después; la tolerancia de C sigue en
3,0 pt (`TOL_COL_C`).

- **«Comparten columna»** (`_comparte_columna_c`; D21, regla 3; grupo G10): los renglones de un párrafo comparten
  columna si todos, salvo el primero (sangría de primera línea o rótulo colgante), están a 3,0 pt o menos del x0 del
  segundo; un párrafo de un renglón la comparte. Los párrafos son los de C. C no mueve un párrafo que no comparte
  columna; y como el primer párrafo que sale arrastra a los que le siguen en el texto de la hoja, si alguno de ese grupo
  no comparte columna, no sale ninguno: el grupo queda donde está y decide el contenido. Si al grupo le sigue, en el
  texto de la hoja, una tabla que se serializa, la tabla es parte del bloque (C no mueve sus renglones y sus filas no
  comparten columna): no sale nada. En el paso de las intersticiales y los cierres, un segmento sale solo si cada uno de
  sus párrafos comparte columna.
  - Por qué el grupo y no el párrafo solo: el modelo de boleta de depaho (p. 25) son párrafos de un renglón
    («BANCO:…») seguidos de uno que no comparte columna; con el párrafo solo, el primer renglón del modelo saldría. En
    E2-006 (ri_ccna p. 41), el cierre de la declaración y los rótulos de firma son párrafos que, cada uno, comparten
    columna, y salen como pide la fila.
  - Por qué la tabla: en snp_tr (p. 39), el renglón que describe el campo de la tabla de códigos subía a la Sección 1 y
    lo heredaban dos unidades leídas (E1-039 y E1-068).
- **La medida nueva del párrafo** (`_col_parrafo_c`; grupo G11): la columna que comparten sus renglones, el x0 del
  segundo, o el de su único renglón; ya no su renglón más a la izquierda. En el paso de los segmentos, la del primer
  párrafo. En expaef (p. 8), el texto del 1.7 (99,2) y un número con un espacio adentro (76,6) quedaban en un párrafo y
  subían a la Sección 1.
- **La columna propia de un punto cuyo renglón de rótulo es un título** (G11, ri_dcpc p. 15): vuelve a valer la columna
  de su texto aunque corra en la del rótulo (el 3.3 corre todo en 76,6). En S0-6a la restringí a un texto más adentro
  que el rótulo por ri_spi C.1.3, que ahora queda en R5-a por lista (§4).
- **A no abre divisiones en una carátula** (G5): la página 1 leída como cuerpo con a lo sumo 8 renglones, el tope de J
  (`MAX_RENGLONES_CARATULA_J`). No pido las marcas de J («Última comunicación», «Texto ordenado») ni la ausencia de
  rótulos: la carátula de ri_ii_31_12_19 dice «Vigente a partir del…» y su título lleva el número del régimen.

## 3. L: un índice no corta la sucesión de números (decisión 5)

`lineas_de_indice_l` y `parsear_cuerpo(indice_l=…)`, interruptor `l`. Sale de D15 («un índice no es texto de ninguna
unidad»). Un índice leído como cuerpo es una corrida de rótulos en una página que empieza en «1.», sin números repetidos,
en la que entre un rótulo y el siguiente solo hay renglones que continúan su título (a la altura de su rótulo o más
adentro, a lo sumo `MAX_RENGLONES_TITULO_L` = 4) y que termina en el primer renglón más a la izquierda que no es un
rótulo, en un número repetido (el cuerpo que vuelve a empezar) o al final de la página. Es índice si tiene al menos 3
rótulos, cada número reaparece después como rótulo, con el mismo título en al menos el 80 %, y no en forma de lista (los
umbrales de la regla 8). Sus rótulos no abren raíz ni punto (motivo `indice_l`): el índice no corta la sucesión, y el
cuerpo que vuelve a empezar en «1.» no se rechaza por ella. Es la regla 8 de S0 con títulos partidos en varios renglones,
que la regla 8 no admite: en el Anexo IV de nmaeef, la regla 8 tomaba solo 3, 4 y 4.1 a 4.6, y 1, 2, 4.7 a 4.9, 5 y 6
abrían raíces dentro del sub-documento.

## 4. Las listas de R5-a (decisión 3)

Con C ajustada comparé las 13 listas con la página, con el criterio de S1-ter (D19, D21, D13 bis). Donde C coincide,
queda C; donde no, R5-a por lista (`LISTAS_R5A_S0_6`, tomada de `LISTAS_R5A_S0_5`), y C no toca esas listas (ni la madre
ni sus ítems: `asignar_por_columna_c(listas_fijas=…)`).

- **Queda C (7):** apnf 1.3.1.2, depaho 3.11.5.5 y las tres de manori (C da lo mismo que R5-a); cryl 4.2.2 (el cierre
  pasa a la Sección 4: la corrección de E2-033); ri2_ae 14.3 (el cierre del 14 queda igual, en el sub-documento del
  Anexo III).
- **Queda R5-a por lista (6):** ri_oc B.1.28 (además, decisión 6); ri_rml 1.4.2 (el bloque «Para el punto 1.4.1. …»
  corre en 90,3, entre las columnas del 1.4 y la del texto del 1.4.2, y la columna no discrimina); ri_spi C.1.3 (el
  párrafo «Además de los datos…» es el cierre de C.1; con el título de C.1.3 medido por su texto, C lo deja en el ítem);
  y tres listas que no son de diseño, en adfsp (1) y ri_oc (2): el contenido del cierre es de la madre y C lo deja en el
  último ítem.
- **Dos listas más (no de las 13):** con C ajustada, en snp_mep 4.6.2 y tasint 3.3.2, leídas en S1-ter y con su cierre
  juzgado correcto con R5-a, el cierre deja de salir. En tasint, «En las expresiones anteriores se entiende» y las
  definiciones forman un párrafo que no comparte columna. En snp_mep, «Además, se proporciona información adicional
  sobre:» se mide por su segundo renglón, una viñeta. En S0-6a C coincidía ahí con R5-a. Les aplico el mismo criterio
  (C no coincide con la página: R5-a por lista) y lo declaro. Ninguna otra de las 43 listas cambia el texto de sus
  unidades.
- Las tres listas que no son de diseño salen de S1-quater por la adenda 3 al diseño (`adenda_3_diseno_S1quater.md`,
  `16b36464…`; entra al repo con un commit de la autora después de este FRENO). Van con sus ids en un archivo
  `NO_ABRIR_`; acá y en el FRENO, solo por documento y por cuenta.

## 5. M: la raíz 0 de un sub-documento aporta a la herencia solo su título (decisión 6)

`construir_chunks(raiz0_solo_titulo_m=True)`, interruptor `m`, en los sub-documentos que abre A (no corre donde los
sub-documentos son de la regla de S0-4: ri_sef, nmcief, ri_ccna, ri_icpipsp, ri_cc y ri_oc). El título es lo que empieza
el primer segmento de la raíz 0 con forma de título de bloque (`_es_titulo_bloque`); su índice y sus bloques de cuerpo
dejan de heredarse. Positivo: E2-002 (ri2_ae, Anexo III, 14.3). E2-057 (ri_ccna, Anexo II) no cambia: es un
sub-documento de S0-4, y su herencia sigue con el título y la introducción del anexo.

## 6. La herencia (decisión 4)

La política de herencia no cambia: se corrige C. El tamaño de la herencia (la suma, sobre todas las unidades, de los
caracteres de los textos de su `herencia`), en los 152 y por documento, en las tres corridas, va en el informe
(`scripts/tamano_herencia_S0-6a-bis.py`). El efecto en el costo de E1 y en el tope de la tanda 1 lo calcula la mesa.

## 7. Lo que no cambia

La tanda 0 queda fuera, igual byte a byte, sin mover claves. Ningún caso de diseño nuevo: solo las 40 filas y las 286
leídas, con la excepción de las tres listas de la decisión 3 que no son de diseño. Las unidades que no son de diseño y me
parecen un error de una regla van con su id y la regla en un `NO_ABRIR_`; en el FRENO, solo la cuenta por regla y por
documento.
