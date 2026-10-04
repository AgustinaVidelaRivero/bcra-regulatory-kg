# L4 — Declaración de la muestra y de la regla de clases

Escrita el 04/10/2026, ANTES de leer ninguna página de la muestra (U-NOSEG-LIMITE, L4). Su sha256 se
toma al escribirla; `code/l4_muestra.py` la aplica sin cambios. Lo que se corrija después de leer va
como nota fechada al pie, nunca como edición de este texto.

## 1. Semilla, orden y método

- Semilla: 20261004. Para cada estrato, en el orden de la tabla, se instancia `random.Random(20261004)`
  de nuevo y se toma `sample(sorted(poblacion), k)`; la muestra se ordena por página para leerla.
- Poblaciones: números de página (base 1) del PDF congelado de `data/experiment/escalado_prep/pdfs/`
  (sha256 contra `manifest_pdfs.sha256`), con los roles por página del camino de B5.8.4 recomputados con
  `e0_lib` de HEAD en el espejo del scratchpad y controlados contra `conteos_b584.json`.

## 2. Estratos y tamaños (decisión 1 de la autora)

| # | estrato | población | k |
|--:|---|---|--:|
| 1 | ficha de manual | páginas de `manual` con rol `ficha_registro` | 20 |
| 2 | ficha de ri2_pm | páginas de `ri2_pm` con rol `ficha_registro` | 10 |
| 3 | cuerpo entre fichas | páginas de rol `cuerpo` de `manual` y `ri2_pm` listadas por las 4 unidades que cruzan fichas según la regla de L2, menos las listadas también por una unidad por punto | 10 |
| 4 | planilla de los nueve | páginas con `clase_forma` = `planilla_ficha` de los nueve documentos del bloque A (`cobertura_bloque_a/censo_forma.json`, `bloque_a_extraccion`, sin `ri_spi`) | 10 |
| 5 | optico | todas sus páginas | 3 |
| 6 | plandecuentas | todas sus páginas | 3 |
| 7 | ri_spi | todas sus páginas | 3 |

Si una población tiene menos páginas que k, se toman todas y se declara.

## 3. Texto que se lee

El texto de la página tal como lo extrae `e0_lib.extraer_lineas` (las líneas de la página, sin quitar
encabezado ni pie), con el número de página. Si una página no tiene texto extraíble, va a «otro» con
la nota «sin texto».

## 4. Clases (una por página)

1. **tabla de códigos**: lista o tabla de códigos con su denominación (partidas, conceptos, códigos de
   operación), sin criterio de qué se registra en cada uno.
2. **formulario o planilla**: modelo a completar (campos, casilleros, columnas con encabezados de
   dato, fórmulas de cálculo de una planilla, modelos de nota), con poca o ninguna prosa.
3. **ficha de cuenta con criterio de imputación**: código y nombre de cuenta seguidos de texto que dice
   qué se registra, qué incluye o cómo se debita o acredita.
4. **prosa normativa**: oraciones corridas que establecen obligaciones, instrucciones, plazos,
   procedimientos o definiciones para los sujetos alcanzados.
5. **historial o índice**: tabla de normas de origen, historial de modificaciones o índice.
6. **otro**: lo que no entra en las anteriores (portada, página en blanco, texto sin texto extraíble).

Regla de decisión: la clase del contenido que ocupa más líneas de la página. Empate: la primera en
este orden: prosa normativa, ficha de cuenta con criterio de imputación, formulario o planilla, tabla
de códigos, historial o índice, otro.

## 5. Columna aparte: prescribe

«sí» si la página tiene al menos una oración que impone una obligación, prohibición, plazo o
instrucción a un sujeto alcanzado (verbo deóntico o futuro impersonal: «deberán», «se informará»,
«no podrán», «se imputarán»); «no» si no la tiene; «no decidible» si la extracción no permite leerla.
Es lectura asistida; no reemplaza la lectura a ciegas de la adenda 2 (§1 y §6), que fue de la autora.

## 6. Planilla

Una fila por página: estrato, TO, página, rol de la página, clase, prescribe, nota de una línea
(qué contiene), `revision_autora` vacía. Conteos crudos por estrato y clase; sin porcentajes.

## 7. Preguntas

Hasta 10 preguntas plausibles de un oficial de cumplimiento que se respondan con una página leída de
la muestra. Para cada una: la página, los términos de búsqueda (dos o tres, literales de la página) y
el resultado de buscarlos en el texto de los otros TOs (los chunks de la partición de los 138
reconocidos plenos y los chunks de E0 de los cinco de desarrollo, `salida_enm01`). Si algún término
aparece en otro TO con el mismo contenido, la pregunta no se responde «solo» con esas páginas y se
descarta o se declara. No son material de evaluación: no se usan para medir nada.
