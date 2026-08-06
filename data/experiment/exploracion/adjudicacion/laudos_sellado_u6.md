# Laudos de sellado — Adjudicación U6

Registro de los laudos con los que sello la adjudicación humana de las 25
preguntas de U6 (territorio virgen, grafo v3_vigente). Los veredictos y la
planilla `u6_adjudicacion_humana.jsonl` quedan congelados con este commit;
las notas `notas_adjudicacion_u6.md` contienen mis pre-diagnósticos
pre-registrados y no forman parte del material que verá ningún verificador.

## Laudo №0 — aceptación de las dos desviaciones de protocolo de la pasada

Acepto las dos desviaciones de protocolo ocurridas durante la corrida:

**(i) Adjudicación informada contra el ancla en las 25 preguntas.** La
decisión de adjudicar cada respuesta contra el texto normativo del TO en el
ancla (a falta de respuesta esperada en el archivo de preguntas) fue una
decisión operativa tomada en U6-001, sin freno previo para laudo formal.
La convalido: el método fue uniforme en las 25 y no hay mezcla de estatus.
En consecuencia, la corrida queda re-etiquetada **"adjudicación informada"**,
no "percepción de usuaria". Los 18 síntomas enviados al intake son de
cohorte informada — síntoma de usuaria experta con la norma a la vista — y
constituyen una **cota superior del intake orgánico**, no un proxy del
feedback de producción.

**(ii) Sesión única de app en lugar de sesión-por-pregunta.** Las 25
preguntas corrieron en una única sesión de la app local. Verifiqué en código
que el procesamiento es independiente por turno: en `harness.py` línea 470,
`messages` nace local en cada `ask` con solo la pregunta del turno; un grep
exhaustivo de asignaciones a `self` no muestra ningún contenedor de
historial; y en `app/main.py` líneas 372-382 el agente se comparte por
`run_id` con `tool_log` limpiado por request bajo lock. Por lo tanto el
apareamiento con la corrida B2 queda preservado.

Queda abierta, para consulta con mentores, la mini-cohorte de contraste con
síntoma naive (4-5 casos re-ingresados con síntoma mínimo) para medir la
sensibilidad del diagnóstico a la informatividad del síntoma.

## Laudo №1 — completitud sobre lo no preguntado

No se penaliza la omisión de instrumentación o excepciones no preguntadas.
Formalizo el criterio que apliqué de facto durante la corrida.

## Laudo №2 — U6-014

U6-014 = **parcial**. La enumeración 4/4 no compensa los calificadores y la
modalidad despojados; la respuesta habilita lecturas más permisivas que la
norma.

## Laudo №3 — U6-023

U6-023 = **correcta**, con matiz registrado (omisión de la cláusula de
cierre discrecional). La omisión no altera el contenido normativo de lo
respondido.

## Laudo №4 — severidad vs. pulgar

La severidad triple (correcta / parcial / incorrecta) vive en la planilla
`u6_adjudicacion_humana.jsonl`, junto con qué mitad falló por pregunta. El
pulgar binario (correcta → 👍, parcial e incorrecta → 👎) es la **compuerta
de intake**, no la métrica.

## Laudo №5 — mecanismos hipotetizados y backlog

Los mecanismos causales hipotetizados en mis notas no generan entradas de
backlog hasta el dictamen independiente de Motor 3. El verificador debe
llegar solo a sus conclusiones.

## Cohorte de síntomas

U6-001, U6-003, U6-010, U6-011 y U6-019 quedan etiquetadas **"síntoma con
atribución de fuente"**: su comentario de feedback atribuye el contenido
erróneo a otro mecanismo, régimen o TO en términos normativos. Al evaluar la
capacidad diagnóstica del verificador sobre la familia de contaminación
cruzada, estas cinco se excluyen o se analizan aparte, porque no es separable
si el verificador halló la familia solo o si el síntoma la insinuó. Los
otros 13 casos con 👎 son síntoma puro.

## Cierre

Este commit sella los veredictos y las hipótesis pre-registradas ANTES de
exponer cualquier caso a Motor 3.
