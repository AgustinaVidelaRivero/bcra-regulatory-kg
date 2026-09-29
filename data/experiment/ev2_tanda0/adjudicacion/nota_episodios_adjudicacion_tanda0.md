# Nota de episodios de la adjudicación de la tanda 0 (anexo E5.c de U-TANDA0-2A)

Declaración de desvío: la adjudicación de C2 a C5 la ejecutó una instancia de
modelo, contra lo que fijan el pre-registro (`docs/preregistro_tanda0.md:308-309`,
protocolo de C1) y el anexo (decisión 5: la sesión de marcado es de la autora).
Modelo y versión de la instancia adjudicadora: a confirmar por la autora.

Registro de los episodios y límites que rodean la adjudicación ciega de las
celdas C2 a C5, para que la lectura de la muestra de control sea honesta.
Planillas selladas en blanco en `f425657`; marcas de la instancia adjudicadora
selladas en `2e4280c` y corregidas en `8e0597c`; cierre con
`data/experiment/ev2_tanda0/code/cierre_adj_tanda0.py --commit-marcas 8e0597c`.
Molde: la nota de episodios de C1,
`data/experiment/ev2_r1/adjudicacion/nota_episodios_adjudicacion.md` (`774acac`).

Ningún episodio altera los veredictos definitivos: en la población A la marca
es definitiva por diseño, y en la muestra B las marcas no reemplazan
veredictos, miden el acuerdo entre el juez y la instancia adjudicadora (anexo,
decisiones 1 y 6).

## Episodio 1: exposición de veredictos del juez en E5, antes de la adjudicación

Anexo, decisión 2; precedente: episodio 1 de C1. Las tres exposiciones son
anteriores a la construcción de las planillas.

- (a) Por la decisión (a) de la autora sobre los criterios sin cita, el FRENO
  de E5 listó los veredictos del juez sobre los tres criterios sin cita de C5
  (T0F-008 criterios 1 y 3, T0F-013 criterio 1), con sus tres repeticiones.
  Están en `reports/tanda0/tabla_celdas_E5.json` (`7f3b207`).
- (b) La salida de herramientas de la sesión ejecutora de E5 imprimió el
  veredicto por pregunta de cinco preguntas de C5: T0F-001, T0F-002, T0F-003,
  T0F-008 y T0F-013. Declarado en el FRENO de E5; el detalle pregunta por
  pregunta estaba en la nota de mesa de su paquete de revisión, fuera del repo.
- (c) La primera versión del script de cierre de E5 dejó el veredicto por
  pregunta de las cuatro celdas en `reports/tanda0/tabla_celdas_E5.json`
  entre las 18:48:34 y las 18:55:50 del 28/09/2026 (campo `generado` de las dos
  versiones), sin commit. La versión commiteada en `7f3b207` solo contiene las
  nueve entradas de criterio de (a):
  `git show 7f3b207:reports/tanda0/tabla_celdas_E5.json | grep -c '"id_pregunta"'` da 9.
  Que alguien haya abierto la primera versión: NO VERIFICADO.

Mitigación: T0F-008 y T0F-013 quedan fuera del marco de muestreo de la
población B de C5 (anexo, decisión 2). Declaración de la autora del 29/09/2026
(anexo, decisión 2): no abrió los archivos SOLO_MESA.

Alcance medido al cierre, desde
`adjudicacion_SOLO_MESA/tabla_fichas_tanda0_SOLO_MESA.json`: de las dos fichas
de la muestra B de C5, ninguna corresponde a una pregunta expuesta en (a) o
(b). De las cinco preguntas de (b), dos tienen ficha en la planilla de C5, y
las dos están en la población A, donde la marca es definitiva por diseño.

Lectura: (a) y (b) no afectan los veredictos definitivos ni la medición de la
muestra B. Si (c) fue vista, la medición de la muestra B de las cuatro celdas
lleva la salvedad del episodio 1 de C1: quien adjudica podría recordar el final
del juez de una pregunta muestreada. Declaración de la instancia que marcó,
del 29/09/2026: no vio la primera versión de reports/tanda0/tabla_celdas_E5.json.
Un grep recursivo sobre reports/ del 28/09 pudo haber leído sus bytes; con -l
no la listó y no mostró contenido. Declaración de la autora del 29/09/2026: no
la vio.

## Episodio 2: el id de ficha permite recalcular la celda

Límite declarado por instrucción de la autora (29/09/2026, aprobación de
E5.c.1). El id de ficha es `FT0-` más los primeros 8 hex de
sha256(sal de la planilla | celda | pregunta | sha de la respuesta). Con la sal,
que está en `data/experiment/ev2_tanda0/code/planillas_tanda0.py` y en
`adjudicacion_SOLO_MESA/`, se puede recalcular la celda de cada ficha probando
las tres celdas de la planilla mezclada. Declaración de la instancia que marcó,
del 29/09/2026, posterior al cierre: no abrió el código del anexo ni
adjudicacion_SOLO_MESA/ antes de sellar las marcas. Declaración de la autora
del 29/09/2026: tampoco los abrió.

## Límites de la decisión 3 f (no se corrigen; se declaran)

1. La planilla de C5 se reconoce por ir aparte y por sus preguntas, que son
   de los cinco documentos nuevos.
2. En la planilla mezclada, una misma pregunta de EV2 puede aparecer más de una
   vez, con respuestas de celdas distintas. Al sellar: 22 preguntas distintas en
   36 fichas; 12 aparecen más de una vez, hasta tres veces (recomputable desde la
   tabla SOLO_MESA).
3. Una respuesta que cite un punto presente en un solo grafo puede insinuar su
   celda. Ejemplo conocido: `cap::4.2.1.2` tiene nodos en el desarrollo de la
   tanda 0 y ninguno en r1 (`docs/plan_tesis.md`, diferencia conocida entre C1
   y C3 y entre C2 y C4).

## Sesión de marcado (E5.c.2)

Marcas selladas en `2e4280c` y corregidas en `8e0597c` (criterio 3 de dos
fichas): 156 criterios en la planilla mezclada y 18 en la de C5; cada
(id_ficha, indice) una sola vez; todas en el dominio cumplido o no_cumplido;
130 filas con observación. La ejecutora del anexo no participó de la sesión.

Declaración de la instancia que marcó, del 29/09/2026. El marcado lo ejecutó
una instancia de modelo, no la autora; ninguna otra instancia le propuso
veredictos. Se declaran cuatro episodios: (a) exposición previa, en una tarea
anterior de la misma sesión, al texto de TO que está detrás de seis criterios
que luego marcó —cap::8.3.2.5, cap::2.11.3.2, ext::13.3.5 y ext::5.8.2.1—, con
dirección hacia no_cumplido, y las seis quedaron no_cumplido; (b) búsqueda de
texto completo sobre el mismo TO además del entorno del ancla, en la que se
apoyan diez marcas; (c) marcado contra texto extraído con pdftotext -layout y
no contra la página renderizada, relevante en los cuadros de ric:4.2 y ric:7.2;
(d) identificación de los PDF contra manifiestos/tanda0_10tos.json, único
archivo abierto fuera de adjudicacion/. Un ls -d sobre
data/experiment/ev2_tanda0/*/ imprimió nombres de subcarpeta sin entrar en
ninguna, posterior a tener las 174 marcas escritas.

## Calibración

La autora marcó 20 de los 174 criterios a ciegas (universo ordenado por
(planilla, id_ficha, indice), random.Random(20260929).sample(range(174), 20),
índices ascendentes), con 18 coincidencias de 20. Dado que declaró no tener
dominio del vocabulario regulatorio, el 18/20 no se reporta como aval: lo que la
calibración produjo fue el hallazgo de una inconsistencia en el marcado,
encontrada por la autora, y su corrección en 8e0597c (FT0-48158917 y
FT0-7b959591, criterio 3, de cumplido a no_cumplido). La corrección se hizo
antes de que la autora viera las tablas agregadas del cierre de las 14:58
(declaración de la autora del 29/09/2026). El cierre está computado sobre
8e0597c.

Anclas: el cambio de las dos marcas se verifica con
`git diff 2e4280c 8e0597c -- data/experiment/ev2_tanda0/adjudicacion/`; el
mensaje de `8e0597c` menciona la calibración de 20 criterios. Las cifras 20 de
174 y 18 de 20 y el procedimiento de sorteo no tienen artefacto en el repo: NO
VERIFICADAS (declaración de la autora del 29/09/2026).

## Incidencia del instrumento de cierre (ejecutora; no afecta la ceguera)

La versión de `cierre_adj_tanda0.py` sellada en `f425657` comparaba los CSV de
marcas con su render en blanco y levantaba antes de escribir, porque su selftest
no ejercitaba la función principal. En E5.c.3 los CSV quedaron fuera de esa
comparación: se verifican contra el commit de marcas (`8e0597c`) y por
completitud. El selftest del
cierre suma la prueba que faltaba. En la misma etapa, la salvedad del reporte
toma el rango de fichas por celda de los datos en lugar de un texto fijo.
Ningún veredicto cambia por estas correcciones.

## Revisión de mesa

La revisión de mesa de E5, E5.c.1 y E5.c.3 leyó
juez_out/*/desanonimizacion_SOLO_MESA/ y adjudicacion_SOLO_MESA/ por programa;
sus salidas visibles mostraron solo totales, booleanos y conteos por celda ya
publicados, y ninguna asoció una ficha con su celda, su origen o su veredicto.

Ancla: declaración de la autora del 29/09/2026 (corrección del cierre de
E5.c.3); sin artefacto en el repo: NO VERIFICADA.
