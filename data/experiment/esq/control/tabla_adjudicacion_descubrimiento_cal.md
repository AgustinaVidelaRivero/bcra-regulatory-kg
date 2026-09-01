# Tabla de adjudicación — calibración del descubrimiento (U-ESQ-2-cal.d)

Generada 2026-08-31T21:31:36 desde `control/descubrimiento_cal.jsonl` (fuente primaria; recomputo independiente del resumen).

**La adjudicación es de la autora**, fila por fila, con la regla sellada del pre-registro §4: una detección VALE si el reporte identifica la materia de la cláusula plantada (no un nombre de tipo ni una cadena exacta); ante la duda NO cuenta; los cruces (dopada de tipo detectada como problema de relación o viceversa) se reportan aparte y no cuentan para su mitad; en C es espuria toda detección de contenido que el esquema sí captura. Este documento NO computa el veredicto contra P-cal.

## Resumen mecánico preliminar (solo lo inequívoco)

| medida | valor |
|---|---|
| A′ con CERO hallazgos (sin detección posible) | 1/10 |
| — mitad tipo con cero hallazgos | 1/5 |
| — mitad predicado con cero hallazgos | 0/5 |
| A′ con ≥1 hallazgo (a adjudicar) | 9/10 |
| C con CERO hallazgos | 2/10 |
| C con ≥1 hallazgo (a adjudicar como espurias o no) | 7/10 |
| contenedores no-lista | ['pro::2.4::cierre'] |
| unidades con error / sin registro | ['pro::2.4::cierre'] |

## Modelo resuelto (db, por llamada pagada)

El alias del contrato es `claude-haiku-4-5`; la db registra el modelo RESUELTO que la API devolvió en cada llamada:

| modelo resuelto | llamadas (misses en db) |
|---|--:|
| `claude-haiku-4-5-20251001` | 20 |

Compromiso sellado en la revisión del freno (a): si P-cal pasa, el censo modo (ii) corre con ese MISMO snapshot resuelto — calibración y censo con el mismo modelo, sin excepción.

## Índice

| # | unidad | brazo | mitad | n hallazgos | error |
|--:|---|---|---|--:|---|
| 1 | `dop::tipo::cap::8.3.2.4` | A' | tipo | 1 | — |
| 2 | `dop::predicado::cap::2.5.5` | A' | predicado | 2 | — |
| 3 | `dop::tipo::cla::6.5.2.1` | A' | tipo | 4 | — |
| 4 | `dop::predicado::cla::6.5.3.3` | A' | predicado | 2 | — |
| 5 | `dop::tipo::ext::3.17.3.5` | A' | tipo | 2 | — |
| 6 | `dop::predicado::ext::6.5.2` | A' | predicado | 3 | — |
| 7 | `dop::tipo::pro::1.1.1` | A' | tipo | 0 | — |
| 8 | `dop::predicado::pro::3.2.3.6` | A' | predicado | 1 | — |
| 9 | `dop::tipo::ric::8.1.2` | A' | tipo | 3 | — |
| 10 | `dop::predicado::ric::10.1.1` | A' | predicado | 3 | — |
| 11 | `cap::1.4.2.1` | C | — | 5 | — |
| 12 | `cap::5.2.1.3` | C | — | 2 | — |
| 13 | `cla::2.2.1.7` | C | — | 0 | — |
| 14 | `cla::4.4` | C | — | 1 | — |
| 15 | `ext::7.6.2::cierre` | C | — | 0 | — |
| 16 | `ext::7.5.7::intro` | C | — | 1 | — |
| 17 | `pro::2.3.11` | C | — | 2 | — |
| 18 | `pro::2.4::cierre` | C | — | — | salida_malformada: 'hallazgos' no es lista: str (contenedor no-lista) |
| 19 | `ric::11.1::intro` | C | — | 5 | — |
| 20 | `ric::8.1.4` | C | — | 1 | — |

## Filas (output verbatim + esperado al lado)

### 1. `dop::tipo::cap::8.3.2.4` — brazo A', mitad tipo

- **Concepto plantado esperado:** sanción pecuniaria (multa por incumplimiento)
- **Por qué está fuera del esquema (manifiesto):** una sanción es la consecuencia jurídica de un incumplimiento: no es prohibición ni límite (Restriccion), no es deber positivo (Obligacion), no suspende ninguna norma (Excepcion) y no es un acto regulado del sujeto (Operacion).
- **Cláusula plantada (manifiesto):** ver `manifiesto_dopadas_p1bis.md` § dop::tipo::cap::8.3.2.4

**Output verbatim del descubrimiento** (`tool_input_crudo`):

~~~json
{
  "hallazgos": [
    {
      "descripcion": "\"El incumplimiento de las condiciones establecidas en este punto dará lugar a la aplicación de una sanción de multa equivalente al 0,5 % del valor computable del instrumento, conforme al régimen sancionatorio previsto en la Ley de Entidades Financieras.\" Esta cláusula establece que la violación de las normas anteriores genera una consecuencia sancionatoria (multa). La sanción no es ni una Restriccion (prohibición/límite a una operación), ni una Obligacion (deber positivo), ni una Excepcion (suspensión de otra norma). Es una consecuencia secundaria de incumplimiento, vinculada a un régimen sancionatorio externo (Ley de Entidades Financieras).",
      "por_que_no_encaja": "El esquema no incluye un tipo de entidad para Sanciones ni un predicado que conecte el incumplimiento de una norma con sus consecuencias sancionatorias. Representarla como una Restriccion deformaría su naturaleza (no es una prohibición primaria sino una consecuencia), y no existe predicado que la conecte tanto con la norma incumplida como con el régimen sancionatorio externo. El contenido normativo es la existencia y magnitud de la sanción por incumplimiento, que escapa a los 12 predicados disponibles."
    }
  ]
}
~~~

### 2. `dop::predicado::cap::2.5.5` — brazo A', mitad predicado

- **Concepto plantado esperado:** equivalencia entre dos operaciones (Operacion→Operacion)
- **Por qué está fuera del esquema (manifiesto):** ningún predicado de la lista de 12 conecta Operacion con Operacion; «se considerarán equivalentes» tampoco es re-expresable invirtiendo dirección ni re-tipando sin perder el contenido.
- **Cláusula plantada (manifiesto):** ver `manifiesto_dopadas_p1bis.md` § dop::predicado::cap::2.5.5

**Output verbatim del descubrimiento** (`tool_input_crudo`):

~~~json
{
  "hallazgos": [
    {
      "descripcion": "\"las operaciones de pase pasivo en pesos mencionadas precedentemente se considerarán equivalentes a las tenencias de títulos públicos que les dieron origen\". La norma establece una equivalencia o equiparación entre dos actos financieros diferentes para ciertos efectos.",
      "por_que_no_encaja": "El esquema no contiene un tipo ni predicado que capture la relación de 'equivalencia normativa' o 'equiparación' entre dos Operaciones distintas. Los predicados disponibles (prohibe, limita, regula, condiciona, requiere, ejecuta) expresan control y obligaciones sobre operaciones, no equiparaciones clasificatorias entre ellas. Representar esto como si una operación 'regulara' o 'condicionara' la otra deformaría el contenido: la norma no ordena ni subordina una operación a otra, sino que afirma su identidad a efectos normativos."
    },
    {
      "descripcion": "\"A fin de determinar el importe de las financiaciones comprendidas en la exposición al sector público no financiero... se observará el criterio de posición neta de títulos previsto en el TO sobre Financiamiento al Sector Público no Financiero\". La norma remite a un criterio técnico externo para calcular un componente normativo.",
      "por_que_no_encaja": "El criterio de 'posición neta de títulos' no es una Operacion, Restriccion, Obligacion ni Excepcion en sí; es un método de cálculo que afecta la determinación de una obligación. El esquema carece de un tipo que capture 'método de cálculo' o 'criterio técnico aplicable'. El predicado 'condiciona' podría conectar una Obligacion a una Operacion, pero aquí la obligación se condiciona a la aplicación de un criterio externo, lo cual introducía una entidad de tipo diferente (criterio/metodología) que el esquema no tipifica."
    }
  ]
}
~~~

### 3. `dop::tipo::cla::6.5.2.1` — brazo A', mitad tipo

- **Concepto plantado esperado:** presunción legal (iuris et de iure)
- **Por qué está fuera del esquema (manifiesto):** una presunción fija un hecho tenido por cierto: no impone deber (Obligacion), no prohíbe ni limita (Restriccion), no exceptúa norma alguna (Excepcion) ni describe un acto regulado (Operacion).
- **Cláusula plantada (manifiesto):** ver `manifiesto_dopadas_p1bis.md` § dop::tipo::cla::6.5.2.1

**Output verbatim del descubrimiento** (`tool_input_crudo`):

~~~json
{
  "hallazgos": [
    {
      "descripcion": "\"Se presumirá, sin admitir prueba en contrario, que el cliente mantiene la capacidad de pago descripta en este punto cuando la totalidad de sus obligaciones registre atrasos inferiores a 30 días.\" — Establece una presunción legal o regla de prueba invertida: ante atrasos menores a 30 días, se asume automáticamente que el cliente puede pagar, sin permitir prueba en contrario.",
      "por_que_no_encaja": "El esquema captura restricciones (límites), obligaciones (deberes positivos) y operaciones reguladas, pero no captura reglas probatorias, presunciones legales, o inversiones de carga de la prueba. Aunque la presunción tiene efecto normativo, no es una prohibición, un límite cuantitativo/cualitativo, un deber positivo, ni una operación regulada. Representarla con los tipos y predicados disponibles deformaría su naturaleza como regla procesal/epistemológica, no como sustancia normativa de conducta."
    },
    {
      "descripcion": "\"Entre los indicadores que pueden reflejar esta situación se destacan que el cliente: i) Presente una buena situación financiera...\" — Define una categoría de clasificación de deudor (\"En observación\") mediante una enumeración de indicadores cualitativos y cuantitativos que pueden estar presentes en forma conjunta o parcial.",
      "por_que_no_encaja": "El esquema proporciona el tipo 'Operacion' para actos regulados, pero la clasificación de deudores es una categorización o estado del deudor dentro de un esquema de categorías; no es una operación (financiación, depósito, transferencia, etc.) ni una restricción ni una obligación específica, sino el criterio que determina qué restricciones y obligaciones aplican. Los indicadores (i a viii) no son prohibiciones, límites cuantitativos, o deberes, sino características o condiciones cuya presencia configura la categoría. Representar esto como una Operacion o fragmentarlo en múltiples Restricciones u Obligaciones mutilaría la estructura de 'categoría clasificatoria' como tipo de contenido normativo."
    },
    {
      "descripcion": "\"Cuando al menos se haya cumplido con el pago, sin haber incurrido en atrasos superiores a 31 días de la totalidad de los intereses devengados, podrá reclasificárselo en el nivel superior...\" — Establece un procedimiento o transición de estado entre categorías de clasificación: cambio de una categoría ('En observación') a otra ('en situación normal') según el cumplimiento de condiciones.",
      "por_que_no_encaja": "El esquema captura restricciones, obligaciones y excepciones, pero no captura transiciones de estado entre categorías clasificatorias ni procedimientos de reclasificación. El contenido normativo aquí es que bajo ciertos hechos, el deudor se mueve de una categoría a otra. Esto no es una prohibición (no hay restricción), ni un deber positivo a cargo de la entidad (no es una Obligacion según el esquema), ni un acto regulado de la entidad (no es una Operacion en el sentido de financiación, depósito, etc.). La reclasificación es una consecuencia o resultado normativo que no encaja en ninguno de los 6 tipos sin deformación."
    },
    {
      "descripcion": "\"En los casos de acuerdos superiores al equivalente a 2,5 veces el importe de referencia establecido en el punto 3.7., la reclasificación inicial del cliente a esta categoría podrá realizarse siempre que no medie objeción por parte de la Superintendencia de Entidades Financieras y Cambiarias...\" — Subordina una reclasificación a la falta de objeción de un órgano supervisor.",
      "por_que_no_encaja": "El esquema no captura dependencias normativas con respecto a actos o decisiones de órganos supervisores externos (la falta de objeción de un tercero como condición de validez). Esto no es una Restriccion (no es un límite ni una prohibición clara), ni una Obligacion (no es un deber de ejecutar), ni una Excepcion a una norma existente. Es una condición de eficacia que vincula la aplicabilidad de una reclasificación a la ausencia de pronunciamiento de un tercero, contenido normativo que el esquema no está equipado para representar sin deformación."
    }
  ]
}
~~~

### 4. `dop::predicado::cla::6.5.3.3` — brazo A', mitad predicado

- **Concepto plantado esperado:** complementariedad entre dos deberes/actos de clasificación
- **Por qué está fuera del esquema (manifiesto):** «complementa» entre dos revisiones/recalificaciones (ambas tipables como Obligacion u Operacion) no matchea ningún predicado ni ninguna firma dominio/rango de la matriz.
- **Cláusula plantada (manifiesto):** ver `manifiesto_dopadas_p1bis.md` § dop::predicado::cla::6.5.3.3

**Output verbatim del descubrimiento** (`tool_input_crudo`):

~~~json
{
  "hallazgos": [
    {
      "descripcion": "\"Cuente con una dirección de poca capacidad y/o experiencia y/o de honestidad poco clara y/o débil y/o con sistemas de control interno objetables.\" — Este pasaje establece un indicador que debe considerarse en la clasificación de deudores. Se trata de un criterio cualitativo basado en atributos del deudor (capacidad gerencial, honestidad, sistemas de control interno) que, de forma implícita, impide o desaconseja la clasificación en una categoría mejor o la mantiene en una categoría deteriorada.",
      "por_que_no_encaja": "El contenido describe una CONDICIÓN sobre atributos del Sujeto (la dirección del deudor) que actúa como un factor de juicio en la clasificación. No encaja en ninguno de los 6 tipos porque no es: una Restriccion (no prohíbe ni limita un acto regulado); no es una Obligacion (no impone un deber positivo al regulado); no es una Excepcion (no suspende ni relaja otra norma); no es una Operacion (no es un acto regulado, sino una característica cualitativa del sujeto). El predicado más próximo sería algo como «condiciona_clasificacion» o «criterio_de», pero ni existe en el esquema ni cabe en los 12 predicados disponibles. Intentar forzarlo a Restriccion (\"limita la clasificación a mejor\") o Obligacion (\"debe verificarse\") deformaría su naturaleza: es un factor de evaluación cualitativa, no una prohibición ni un deber positivo."
    },
    {
      "descripcion": "\"La revisión de la clasificación motivada por este indicador complementará a la recalificación periódica prevista en esta sección, sin sustituirla.\" — Este pasaje establece que la revisión por este indicador es complementaria (no sustitutiva) de la recalificación periódica.",
      "por_que_no_encaja": "El contenido expresa una RELACIÓN PROCEDURAL: que una revisión debe complementar (sin sustituir) otro proceso (la recalificación periódica). No encaja en los 6 tipos ni en los 12 predicados porque no describe un acto regulado (Operacion), no es una restricción ni obligación sobre los sujetos regulados, ni un vínculo entre éstos y actos concretos. Es una disposición sobre cómo se relacionan dos procesos normativos entre sí. Ningún predicado disponible (establecida_en, referencia, modificada_por, aplica_a, regula, exceptua, exceptua_obligacion, prohibe, limita, ejecuta, requiere, condiciona) captura una relación de complementariedad procesal entre normas o procesos administrativos internos."
    }
  ]
}
~~~

### 5. `dop::tipo::ext::3.17.3.5` — brazo A', mitad tipo

- **Concepto plantado esperado:** término definido (definición normativa de un valor)
- **Por qué está fuera del esquema (manifiesto):** una definición fija el sentido de un término: no manda, no prohíbe, no exceptúa ni es un acto; define un valor, no un sujeto ni una operación, así que tampoco tiene canal vecino posible (sujeto_propuesto no aplica).
- **Cláusula plantada (manifiesto):** ver `manifiesto_dopadas_p1bis.md` § dop::tipo::ext::3.17.3.5

**Output verbatim del descubrimiento** (`tool_input_crudo`):

~~~json
{
  "hallazgos": [
    {
      "descripcion": "\"el monto equivalente de los pagos realizados desde el 01/07/22 por el beneficiario en el marco de lo dispuesto en los puntos 3.4.4.4. y/o 3.4.4.5., por utilidades y dividendos generados por aportes de inversión directa liquidados a partir del 17/01/20 y/o por proyectos enmarcados en el 'PLAN GAS'\": establece un concepto deducible que debe restarse del monto acumulado de beneficios para calcular el certificado máximo emitible, pero no es una restricción simple de \"no podrá\" ni un límite directo a una operación; es más bien un criterio de cálculo o ajuste cuantitativo que modula el derecho de acceso.",
      "por_que_no_encaja": "El contenido describe una deducción o ajuste en la base de cálculo de un derecho (monto certificable), no una Restriccion (prohibición o límite directo a una Operacion) ni una Obligacion (deber positivo). El tipo Restriccion captura límites cuantitativos que frenan o prohíben actos, pero aquí no se prohíbe ni se limita una operación: se especifica qué debe sustraerse de un acumulado para determinar un monto disponible. Representar esto como Restriccion deformaría la naturaleza del contenido, que es un ajuste en la fórmula de cálculo del derecho, no una norma que frena o reduce capacidad de actuar. No hay predicado que exprese \"ajusta_base_de_cálculo\" o \"se_sustrae_de\"."
    },
    {
      "descripcion": "\"se entiende por 'valor de referencia ajustado' el promedio simple de los tipos de cambio de cierre de los últimos cinco días hábiles, incrementado en el porcentaje que establezca la reglamentación\": establece una definición operativa de un concepto (valor de referencia ajustado) y un método de cálculo indexado a futuro (\"en el porcentaje que establezca la reglamentación\").",
      "por_que_no_encaja": "El contenido es una definición técnica o fórmula de cálculo, no una Operacion, Restriccion, Obligacion o Excepcion. Tampoco encaja en ninguno de los 12 predicados: no se prohíbe nada, no se obliga a nada directamente, ni se excluye una norma. Una definición de concepto técnico —cómo se calcula un valor de referencia— no es contenido normativo capturado por el esquema, que se enfoca en actos regulados, deberes, prohibiciones y excepciones. Representarla como Obligacion (\"calcularán el valor de referencia ajustado...\") no conservaría el hecho de que es ante todo una precisión de significado, y la parte \"en el porcentaje que establezca la reglamentación\" es una remisión a norma futura que introduce indeterminación abierta."
    }
  ]
}
~~~

### 6. `dop::predicado::ext::6.5.2` — brazo A', mitad predicado

- **Concepto plantado esperado:** asimilación entre dos operaciones (Operacion→Operacion)
- **Por qué está fuera del esquema (manifiesto):** misma familia que la equivalencia: no existe predicado Operacion→Operacion y «quedan asimiladas a» no es prohibición, límite, excepción ni condición.
- **Cláusula plantada (manifiesto):** ver `manifiesto_dopadas_p1bis.md` § dop::predicado::ext::6.5.2

**Output verbatim del descubrimiento** (`tool_input_crudo`):

~~~json
{
  "hallazgos": [
    {
      "descripcion": "\"Una persona jurídica (incluidas las sociedades de hecho u otras que no reúnan los requisitos exigidos por la Ley General de Sociedades) se considerará residente del país donde está constituida.\" El texto establece un criterio de residencia (atribución de domicilio regulatorio) basado en el lugar de constitución de una entidad.",
      "por_que_no_encaja": "El esquema no cuenta con un tipo para representar criterios de clasificación, atribución de estatus o características identitarias de sujetos. Las entidades de SUJETO no son parte del esquema (viven en un catálogo aparte), y los 6 tipos disponibles (Comunicacion, TextoOrdenado, Operacion, Restriccion, Excepcion, Obligacion) no capturan normas que definen o atribuyen propiedades permanentes a categorías de personas. Representarlo como Restriccion u Obligacion lo deformaría, pues no es una prohibición, límite ni deber positivo, sino una definición clasificatoria."
    },
    {
      "descripcion": "\"Las sucursales en una economía de personas jurídicas de otra economía se considerarán residentes del primer país cuando están inscriptas a los fines de poder realizar actividades en el país de manera habitual.\" Nuevamente, se establece un criterio de residencia condicionado a un requisito de inscripción y habitualidad de actividades.",
      "por_que_no_encaja": "Igual motivo: es una regla de atribución de estatus (residencia) a un tipo de sujeto, condicionada a circunstancias (inscripción y habitualidad), pero no encaja en ninguno de los 6 tipos del esquema. Los predicados no capturan relaciones de clasificación o asignación de propiedades. Representarlo como Obligacion (\"deberán ser consideradas\") mutilaría su naturaleza: no es un deber de acción, sino una norma que declara/establece cuándo un sujeto cae bajo una categoría regulatoria."
    },
    {
      "descripcion": "\"A los efectos de esta reglamentación, las operaciones de cambio concertadas por dichas sucursales quedan asimiladas a las operaciones concertadas por su casa matriz.\" El texto ordena que las operaciones de cambio de las sucursales sean equiparadas o asimiladas a las de la matriz.",
      "por_que_no_encaja": "No existe un predicado que exprese asimilación, equiparación o igualación normativa entre operaciones o entre sujetos. Los predicados existentes (regula, prohibe, limita, requiere, condiciona, ejecuta) expresan relaciones de regulación, ejecución o condicionamiento, pero no equivalencia regulatoria. Representar esta asimilación como una Obligacion (\"deberán tratarse como\") o como una relación regula/prohibe deformaría su sentido: no es un deber de comportamiento ni una prohibición, sino un mandato de trato paritario para efectos normativos."
    }
  ]
}
~~~

### 7. `dop::tipo::pro::1.1.1` — brazo A', mitad tipo

- **Concepto plantado esperado:** cláusula de vigencia diferida (disposición transitoria)
- **Por qué está fuera del esquema (manifiesto):** una regla de vigencia predica sobre la norma misma (cuándo rige), no sobre la conducta de un sujeto: no encaja en deber, prohibición, excepción ni acto regulado.
- **Cláusula plantada (manifiesto):** ver `manifiesto_dopadas_p1bis.md` § dop::tipo::pro::1.1.1

**Output verbatim del descubrimiento** (`tool_input_crudo`):

~~~json
{
  "hallazgos": []
}
~~~

### 8. `dop::predicado::pro::3.2.3.6` — brazo A', mitad predicado

- **Concepto plantado esperado:** acreditación de cumplimiento (deber→deber)
- **Por qué está fuera del esquema (manifiesto):** «acredita el cumplimiento de» conecta dos deberes; no es requiere (Operacion→Obligacion), no es condiciona (Obligacion→Operacion), no exceptúa nada.
- **Cláusula plantada (manifiesto):** ver `manifiesto_dopadas_p1bis.md` § dop::predicado::pro::3.2.3.6

**Output verbatim del descubrimiento** (`tool_input_crudo`):

~~~json
{
  "hallazgos": [
    {
      "descripcion": "«La conservación de la documentación indicada en este punto acreditará el cumplimiento de la obligación de designación prevista en el punto 3.1.1.» El texto establece que la conservación (posesión de documentos) es prueba o acreditación de cumplimiento de una obligación. Se trata de una relación normativa entre una conducta (conservar documentación) y su efecto probatorio o exoneratorio (acreditar cumplimiento), que no se canaliza mediante los predicados disponibles.",
      "por_que_no_encaja": "El esquema ofrece predicados como `regula`, `limita`, `prohibe`, `condiciona` y `requiere`, pero ninguno captura la relación 'conservar documentación acredita cumplimiento de obligación', que es una conexión causal-evidentiva entre una conducta probatoria y una obligación preexistente. La causalidad y el efecto probatorio no están modelados en el esquema de referencia: ni siquiera el tipo `Obligacion` se vincula a través de 'ser acreditada por' o similar. Representar esto con los predicados existentes mutilaría el significado normativo de la acreditación."
    }
  ]
}
~~~

### 9. `dop::tipo::ric::8.1.2` — brazo A', mitad tipo

- **Concepto plantado esperado:** facultad discrecional de la autoridad (permiso, no deber)
- **Por qué está fuera del esquema (manifiesto):** una facultad («queda facultada», «podrá») es deónticamente distinta del deber y de la prohibición; el esquema no tiene categoría para permisos/potestades.
- **Cláusula plantada (manifiesto):** ver `manifiesto_dopadas_p1bis.md` § dop::tipo::ric::8.1.2

**Output verbatim del descubrimiento** (`tool_input_crudo`):

~~~json
{
  "hallazgos": [
    {
      "descripcion": "\"Se consignará el importe máximo de los registrados en las partidas 3650000X, es decir, se toma la máxima pérdida registrada para los 6 escenarios posibles.\". La norma prescribe un método de cálculo específico (tomar el máximo entre 6 escenarios) para construir una medida de riesgo (EVE estandarizado). No es simplemente un deber de presentación (Obligacion), sino una regla de transformación de datos que define cómo se produce el valor a informar.",
      "por_que_no_encaja": "El esquema captura deberes positivos (Obligacion → ej. 'informarán', 'calcularán') pero no distingue entre un deber de presentación de un dato y una prescripción metodológica (algoritmo, fórmula, transformación de inputs en outputs). Representar esto como una simple Obligacion ('calcularán') pierde la naturaleza técnica y determinística de la regla de cálculo. No existe predicado que exprese 'define el método de cálculo para' o 'prescribe la fórmula para'; solo 'condiciona' (que enlaza Obligacion → Operacion), que no captura la relación entre una norma y un procedimiento de transformación numérica."
    },
    {
      "descripcion": "\"La Superintendencia de Entidades Financieras y Cambiarias queda facultada para adecuar el porcentaje indicado precedentemente cuando la evolución de las condiciones de mercado lo justifique.\". La norma atribuye a un actor (la Superintendencia) una facultad de modificación discrecional de un parámetro regulatorio (el 15%) según una condición (evolución del mercado), sin fijar límites sustantivos a esa discreción.",
      "por_que_no_encaja": "El esquema no incluye un tipo para representar facultades o poderes discrecionales de actores reguladores, ni un predicado que exprese 'está facultado para modificar' o 'tiene discreción sobre'. Los 12 predicados describen relaciones entre tipos normados (qué prohíbe, qué obliga, qué requiere), no atribuciones de poder a sujetos. Representar esto como una Obligacion (que contraería un deber positivo) o como una Excepcion (que suspendería otra norma) deformaría su naturaleza: es una delegación de autoridad discrecional sobre un parámetro, no un deber ni una condición de excepción."
    },
    {
      "descripcion": "\"Cuando esta medida supere el 15 % del nivel de capital 1, se identificará a la entidad como una 'entidad atípica' y la SEFyC podrá exigirle la adopción de medidas específicas\". La norma establece una consecuencia condicional (alcanzado el umbral, la entidad adquiere una categoría y queda sujeta a nuevas demandas regulatorias), pero no prescribe cuáles son esas 'medidas específicas'; remite a otro punto normativo (5.6.) sin reproducir su contenido.",
      "por_que_no_encaja": "El esquema permite representar una Restriccion o Obligacion condicionada por una Excepcion, pero aquí el contenido normativo es una clasificación dinámica (convertirse en 'entidad atípica') que acarrea consecuencias futuras indeterminadas en el punto de enunciación. No existe tipo para 'categoría' o 'estatus', ni predicado para 'causa la clasificación de' o 'activa el régimen de'. La remisión a medidas externas sin especificar qué son mantiene la operación abierta: no se puede modelar como una Operacion regulada ni como una Restriccion específica porque su alcance es indeterminado dentro del marco del esquema."
    }
  ]
}
~~~

### 10. `dop::predicado::ric::10.1.1` — brazo A', mitad predicado

- **Concepto plantado esperado:** cómputo conjunto entre dos requerimientos informativos
- **Por qué está fuera del esquema (manifiesto):** «se computa conjuntamente con» entre dos requerimientos (Obligacion→Obligacion) no tiene predicado en la lista ni firma válida en la matriz dominio/rango.
- **Cláusula plantada (manifiesto):** ver `manifiesto_dopadas_p1bis.md` § dop::predicado::ric::10.1.1

**Output verbatim del descubrimiento** (`tool_input_crudo`):

~~~json
{
  "hallazgos": [
    {
      "descripcion": "\"Los datos se informarán con frecuencia trimestral, sobre base individual y consolidada trimestral\" — la norma establece una FRECUENCIA de presentación (trimestral) como parte del contenido normativo de la Obligacion.",
      "por_que_no_encaja": "El esquema captura Obligaciones y sus conexiones (quién, qué acto regulado, bajo qué condición), pero la frecuencia o periodicidad de cumplimiento de una Obligacion no tiene predicado de representación. Un predicado como 'frecuencia_de', 'período_de' o 'cada_cuándo' sería necesario para capturar que esta Obligacion se ejecuta trimestral y no anualmente o mensualmente. Sin él, la dimensión temporal de la obligación queda fuera del modelo."
    },
    {
      "descripcion": "\"Se regirá por los plazos de presentación previstos para el régimen informativo contable mensual\" (para base individual) y \"Se regirá por los plazos de presentación del régimen informativo para Supervisión\" (para base consolidada) — la norma vincula el cumplimiento de una Obligacion (informar el ratio) a PLAZOS o calendarios externos definidos en otros documentos.",
      "por_que_no_encaja": "El esquema no tiene predicado que exprese la delegación de plazos o la dependencia temporal de una Obligacion respecto de un régimen informativo externo. Predicados como 'regida_por', 'subordinada_a_plazos_de', 'aplica_cronograma_de' no existen. Sin ellos, no se puede capturar que la presentación de esta información debe acatarse a calendarios definidos en otro marco normativo, lo cual es contenido normativo esencial."
    },
    {
      "descripcion": "\"El requerimiento previsto en el presente punto se computará conjuntamente con el previsto para el régimen informativo de Supervisión a los fines del control de cumplimiento\" — la norma establece un vínculo de AGREGACIÓN o CÓMPUTO CONJUNTO entre dos obligaciones informativas (la de este punto y la del régimen de Supervisión) para efectos de fiscalización.",
      "por_que_no_encaja": "El esquema no dispone de un predicado que exprese la relación de 'se computa junto a', 'se consolida con' o 'se verifica conjuntamente con'. La sola enumeración de dos Obligaciones separadas no captura que deben considerarse como un conjunto único a los efectos del cumplimiento normativo. Sin un predicado de agregación o co-reporte, se pierde la instrucción de que el control y la validación operan sobre ambas simultáneamente."
    }
  ]
}
~~~

### 11. `cap::1.4.2.1` — brazo C

- **Esperado (brazo C, unidad limpia):** cero detecciones; toda detección de contenido que el esquema sí captura es espuria

**Output verbatim del descubrimiento** (`tool_input_crudo`):

~~~json
{
  "hallazgos": [
    {
      "descripcion": "\"La entidad deberá encuadrarse en la exigencia a más tardar en el segundo mes siguiente a aquel en que se registre el incumplimiento, o presentar un plan de regularización y saneamiento dentro de los 30 días corridos siguientes al último día del mes al que corresponda el incumplimiento.\" — La norma impone un plazo de acción (enmienda o presentación de plan) después de detectado un incumplimiento. Este contenido es una obligación temporal: las entidades tienen un tiempo determinado para corregir o remitir documentación ante el regulador.",
      "por_que_no_encaja": "El esquema carece de tipo y predicados para capturar plazos, vencimientos o límites temporales como dimensión normativa independiente. Obligacion (tipo 6) captura «deberán presentar», pero no la dimensión temporal «a más tardar en X período» que es normativa por sí misma. No existe predicado que vincule una Obligacion con un plazo de cumplimiento, ni tipo que represente plazos como entidades. Representar solo la obligación sin el plazo la deformaría: la norma no solo ordena actuar, sino actuar en una ventana temporal específica, y esa ventana es parte esencial de lo que prohíbe o permite."
    },
    {
      "descripcion": "\"La obligación de presentar planes determinará que el importe de los depósitos –en moneda nacional y extranjera– no podrá exceder del nivel que haya alcanzado durante el mes en que se originó el incumplimiento. Dicho límite –que se mantendrá mientras persista la deficiencia–...\" — La norma establece un límite cuantitativo sobre depósitos (moneda nacional y extranjera), pero ese límite está condicionado a una circunstancia variable: la persistencia de la deficiencia. Es una restricción que cambia de vigencia según un estado dinámico.",
      "por_que_no_encaja": "El esquema admite Restriccion con predicado limita, pero no captura el carácter condicionado y temporal de un límite cuantitativo: «se mantendrá mientras persista la deficiencia». La norma no impone un límite estático, sino un límite que se activa y desactiva según una condición dinámica (persistencia del incumplimiento). No existe predicado que vincule una Restriccion con una condición de vigencia temporal o cambio de estado. Representar solo el límite sin su dependencia de la persistencia de la deficiencia mutilaría la naturaleza normativa: el límite es navegable, no permanente."
    },
    {
      "descripcion": "\"Además, esa obligación de presentar planes determinará los siguientes efectos: i) La Superintendencia de Entidades Financieras y Cambiarias (SEFyC) podrá designar veedor con las facultades establecidas en la Ley de Entidades Financieras.\" — La norma autoriza a la SEFyC a tomar una acción administrativa (designación de veedor) como consecuencia de la presentación de planes en incumplimiento de capital mínimo.",
      "por_que_no_encaja": "El esquema no posee tipo para representar facultades de acción del regulador como SEFyC ni predicados que vinculen obligaciones de entidades con poderes discrecionales del regulador. «Podrá designar veedor» es contenido normativo (confiere potestad), pero la entidad SEFyC es un Sujeto y el esquema no modeliza potestades de Sujetos, solo deberes y prohibiciones sobre operaciones de entidades. No existe predicado que capture «como consecuencia de X obligación, Y sujeto regulador puede Z acción», ni tipo para Facultad o Potestad. Representar solo la obligación de presentar planes, sin la potestadad SEFyC que se dispara, sería incompleto."
    },
    {
      "descripcion": "\"ii) Impedimento para: a) Transformación de entidades financieras. b) Instalación de sucursales en el exterior. c) Instalación de oficinas de representación en el exterior, excepto que dicha instalación reemplace una sucursal en funcionamiento –cerrada en forma contemporánea– localizada en el mismo país. d) Participación en entidades financieras del exterior.\" — La norma prohíbe cuatro operaciones con una excepción: la instalación de oficinas de representación está permitida si reemplaza (en el mismo país) una sucursal cerrada contemporáneamente.",
      "por_que_no_encaja": "La excepción (c) no es una excepción a una Restriccion preexistente en el esquema: es una excepción dentro la enumeración de Restricciones nuevas impuestas como consecuencia de la presentación de planes. El esquema modeliza Excepcion como tipo que exceptua o exceptua_obligacion a una Restriccion o Obligacion preexistente. Aquí la excepción («excepto que dicha instalación reemplace...») es interna a una regla de consecuencias: es una salvedad condicional que relativiza la prohibición dentro del mismo párrafo, no suspende una norma citada o implícita. Además, la condición («reemplace una sucursal en funcionamiento –cerrada en forma contemporánea– localizada en el mismo país») vincula dos operaciones futuras (cierre y apertura) con coordinación temporal y geográfica, cosa que ningún predicado captura. Representar la prohibición sin la salvedad deformaría; representar la salvedad como Excepcion descontextualizada tampoco sería fiel."
    },
    {
      "descripcion": "\"iii) No podrán distribuirse dividendos en efectivo, ni efectuarse pagos de honorarios, participaciones o gratificaciones provenientes de la distribución de resultados de la entidad. Esta limitación regirá en tanto los planes de regularización y saneamiento estén pendientes de presentación o, habiéndose presentado, la SEFyC los haya observado o verifique su incumplimiento.\" — La norma prohíbe distribución de dividendos, honorarios y gratificaciones mientras persistan ciertas condiciones (planes pendientes, observados o incumplidos según verificación SEFyC).",
      "por_que_no_encaja": "La prohibición está condicionada a estados dinámicos de terceros (la SEFyC): la prohibición se activa/desactiva según (a) si planes están pendientes, (b) si SEFyC los observó, (c) si SEFyC verifica su incumplimiento. No existe predicado que vincule una Restriccion con condiciones de vigencia basadas en acciones o verificaciones de un Sujeto regulador. El esquema no captura «la prohibición rige mientras suceda X», y menos aún «mientras el regulador verifique Y». Representar solo la prohibición de distribuir sin el carácter condicional según observación/verificación SEFyC sería una distorsión: la norma no prohíbe incondicionalmente, sino prohíbe bajo circunstancias que dependen de actos administrativos del regulador."
    }
  ]
}
~~~

### 12. `cap::5.2.1.3` — brazo C

- **Esperado (brazo C, unidad limpia):** cero detecciones; toda detección de contenido que el esquema sí captura es espuria

**Output verbatim del descubrimiento** (`tool_input_crudo`):

~~~json
{
  "hallazgos": [
    {
      "descripcion": "«No deberá existir una correlación positiva sustancial entre la calidad crediticia de la contraparte y el valor de la garantía». Esta disposición prohíbe que exista una cierta relación cuantitativa/cualitativa (correlación positiva sustancial) entre dos atributos de entidades distintas (calidad crediticia de la contraparte vs. valor de la garantía).",
      "por_que_no_encaja": "El esquema de tipos de restricción (prohibe, limita) captura prohibiciones o límites sobre OPERACIONES. Aquí no se prohíbe una operación sino una CONDICIÓN ESTRUCTURAL entre dos atributos de sujetos diferentes (correlación entre propiedades). No existe un tipo ni un predicado que capture una restricción sobre la relación cuantitativa/cualitativa entre atributos de entidades financieras. La prohibición refiere a una geometría de garantía, no a un acto regulado."
    },
    {
      "descripcion": "«los títulos valores emitidos por la contraparte o un vinculado a ella, no son admisibles». Esta cláusula especifica que cierta clase de garantía (títulos emitidos por la contraparte o sus vinculadas) está vedada.",
      "por_que_no_encaja": "Se trata de una prohibición sobre una CLASE DE GARANTÍA ESPECÍFICA, no sobre una operación ni sobre una relación entre atributos. El esquema captura restricciones sobre Operaciones (prohibe_operacion, limita_operacion vía el predicado prohibe/limita), pero no dispone de un mecanismo para capturar prohibiciones sobre TIPOS DE COLATERALES o CARACTERÍSTICAS DE GARANTÍA por su naturaleza o composición. Representarlo como una Restriccion sobre Operacion deformaría el contenido: lo que se veda no es ejecutar una operación, sino la admisibilidad de una clase de instrumento como garantía."
    }
  ]
}
~~~

### 13. `cla::2.2.1.7` — brazo C

- **Esperado (brazo C, unidad limpia):** cero detecciones; toda detección de contenido que el esquema sí captura es espuria

**Output verbatim del descubrimiento** (`tool_input_crudo`):

~~~json
{
  "hallazgos": []
}
~~~

### 14. `cla::4.4` — brazo C

- **Esperado (brazo C, unidad limpia):** cero detecciones; toda detección de contenido que el esquema sí captura es espuria

**Output verbatim del descubrimiento** (`tool_input_crudo`):

~~~json
{
  "hallazgos": [
    {
      "descripcion": "\"No corresponderá la evaluación de la capacidad de repago respecto de las financiaciones que se encuentren respaldadas con tales garantías.\" La norma establece que se exime una evaluación específica (la evaluación de capacidad de repago) para un cierto tipo de operación (financiaciones con garantías preferidas \"A\"), pero no simplemente prohíbe una operación ni establece un límite cuantitativo: suspende la aplicación de un procedimiento o criterio de análisis a una operación bajo ciertas circunstancias.",
      "por_que_no_encaja": "El predicado 'prohibe' captura la prohibición de ejecutar una operación; 'limita' captura el establecimiento de límites cuantitativos o cualitativos sobre una operación. Ambos presuponen que la operación misma se restringe. Aquí lo que se suspende no es la operación de financiación, sino la obligación o criterio procedural de evaluar capacidad de repago. Es una excepción a un procedimiento, no una prohibición de operación. Si se fuerza a 'prohibe' deformaría el sentido: la financiación sigue permitida, solo que sin cierto análisis. El esquema carece de un predicado que capture la suspensión de un requisito procedural o criterio de análisis para una operación bajo circunstancias específicas."
    }
  ]
}
~~~

### 15. `ext::7.6.2::cierre` — brazo C

- **Esperado (brazo C, unidad limpia):** cero detecciones; toda detección de contenido que el esquema sí captura es espuria

**Output verbatim del descubrimiento** (`tool_input_crudo`):

~~~json
{
  "hallazgos": []
}
~~~

### 16. `ext::7.5.7::intro` — brazo C

- **Esperado (brazo C, unidad limpia):** cero detecciones; toda detección de contenido que el esquema sí captura es espuria

**Output verbatim del descubrimiento** (`tool_input_crudo`):

~~~json
{
  "hallazgos": [
    {
      "descripcion": "\"La entidad encargada del seguimiento podrá extender el plazo para la liquidación de un permiso de embarque\". Se establece un acto o potestad (extensión de plazo) que puede ejercer un sujeto específico (entidad encargada del seguimiento) sobre un acto regulado concreto (liquidación de un permiso de embarque), pero este acto tiene naturaleza de POTESTAD DISCRECIONAL O FACULTAD CONDICIONADA, no un deber imperativo ni una prohibición.",
      "por_que_no_encaja": "El esquema solo captura Obligaciones (deberes positivos) y Restricciones (prohibiciones o límites). Una potestad o facultad que un sujeto puede ejercer bajo ciertas condiciones no encaja en ninguno de estos dos tipos. El predicado \"condiciona\" (Obligacion → Operacion) expresa que una obligación condiciona una operación, pero aquí la relación es inversa: una condición habilita una potestad. Tampoco hay un predicado que represente \"autoriza\", \"puede ejecutar\", \"tiene la facultad de\" o similar. Representar esto como una Obligacion deformaría el contenido, porque no es un deber sino una habilitación potestativa."
    }
  ]
}
~~~

### 17. `pro::2.3.11` — brazo C

- **Esperado (brazo C, unidad limpia):** cero detecciones; toda detección de contenido que el esquema sí captura es espuria

**Output verbatim del descubrimiento** (`tool_input_crudo`):

~~~json
{
  "hallazgos": [
    {
      "descripcion": "\"La denominación de los productos o servicios en las solicitudes, contratos, sistema de banca por Internet (home banking) y resúmenes de cuenta deberá ajustarse a la prevista en las normas del BCRA\": se requiere que las denominaciones de productos o servicios en varios canales (solicitudes, contratos, home banking, resúmenes) sean conformes a lo establecido en otras normas del BCRA.",
      "por_que_no_encaja": "El contenido trata sobre la denominación o nomenclatura que debe usarse para designar productos/servicios financieros, no sobre una operación financiera, una restricción, una obligación de hacer algo, ni una excepción. El esquema captura operaciones (actos regulados: financiación, depósito, etc.), restricciones (prohibiciones, límites), obligaciones (deberes positivos de acción) y excepciones. La especificación de cómo deben denominarse las cosas no es ninguno de estos: es un requerimiento formal/nominal que no se ajusta a los 6 tipos disponibles sin mutilar su naturaleza. Aunque podría forzarse como 'Obligacion' ('deberá ajustarse'), esto desdibujaría que lo normado no es un acto sino una nomenclatura, un estándar de denominación."
    },
    {
      "descripcion": "\"sin perjuicio de que se pueda aludir adicionalmente al paquete comercial que eventualmente conformen\": se permite o reconoce que, además de la denominación normada, las entidades pueden hacer referencia adicional al paquete comercial.",
      "por_que_no_encaja": "Este contenido introduce una flexibilización o permiso adicional que no es capturado por ningún predicado del esquema. No es una excepción (Excepcion) en sentido de suspensión de una restricción u obligación clara previa, sino una cláusula permisiva que coexiste con el deber de conformarse a denominaciones estándar. El esquema no tiene un predicado para 'permite', 'faculta' o 'autoriza adicionalmente', y los 12 predicados disponibles no expresarían esta clase de acuerdo normativo sin deformarlo."
    }
  ]
}
~~~

### 18. `pro::2.4::cierre` — brazo C

- **Esperado (brazo C, unidad limpia):** cero detecciones; toda detección de contenido que el esquema sí captura es espuria
- **ERROR:** `salida_malformada: 'hallazgos' no es lista: str (contenedor no-lista)`

**Output verbatim del descubrimiento** (`tool_input_crudo`):

~~~json
{
  "hallazgos": "[\n  {\n    \"descripcion\": \"\\\"los sujetos obligados deberán evitar prácticas o acciones que reflejen o promuevan visiones estereotipadas y jerarquizantes de los géneros, androcentrismo, lenguaje sexista, violencia mediática y/o simbólica contra mujeres y personas LGBTTIQ+\\\". La norma establece un deber positivo de EVITAR (omisión obligatoria) conductas específicas de índole ética, de género y no-discriminatoria. No regula ninguna Operacion financiera, sino la calidad y características que debe revestir el contenido de publicidad.\",\n    \"por_que_no_encaja\": \"El esquema define Obligacion como un 'deber positivo' que se conecta a una Operacion mediante predicados como regula (→ Operacion), condiciona (→ Operacion) o requiere (← Operacion). Sin embargo, esta norma impone deberes sobre el carácter y contenido de las acciones de publicidad, no sobre operaciones financieras. La Operacion del esquema captura actos regulados: 'financiación, depósito, transferencia, compra/venta de moneda extranjera, clasificación de deudor, presentación informativa, etc.' — actos que están regulados porque generan riesgos financieros. Aquí se trata de regulación de FORMA y CONTENIDO ideológico de mensajes, no de un acto o evento financiero susceptible de ser operación. Representar esto como una Obligacion que regula una Operacion sería deformador: pretendería que la norma está limitando una operación financiera cuando en realidad está prescribiendo estándares éticos sobre comunicación.\"\n  },\n  {\n    \"descripcion\": \"\\\"deberán evitar la condescendencia masculina –conocida como mansplaining–, utilizar la imagen de la mujer como mero objeto desvinculado del producto que se pretende promocionar o asociada a comportamientos estereotipados, o reproducir mensajes homofóbicos, lesbofóbicos y transfóbicos\\\". La norma detalla categorías específicas de conductas o mensajes que deben evitarse en el contenido de la publicidad.\",\n    \"por_que_no_encaja\": \"Estas prohibiciones tienen carácter ESTILÍSTICO, IDENTITARIO y DE CONTENIDO EXPRESIVO. No son limitaciones cuantitativas o cualitativas sobre operaciones financieras (el rango normativo de Restriccion y Obligacion en el esquema). El esquema captura 'prohibición o un límite cuantitativo/cualitativo (\"no podrá\", \"se prohíbe\", \"el monto no excederá\")' — restricciones sobre QUÉ se puede hacer financieramente o CUÁNTO se puede hacer. Aquí se trata de restricciones sobre CÓMO se debe decir algo, qué formas de expresión evitar, qué símbolos o mensajes no usar. Esto es una regulación de la FORMA DEL DISCURSO, no una operación financiera ni un límite operacional. Representarlo como una Restriccion dentro del esquema mutilaría su naturaleza: sería forzar contenido de política de género y comunicación responsable a entrar en una estructura pensada para límites de actos financieros.\"\n  }\n]"
}
~~~

### 19. `ric::11.1::intro` — brazo C

- **Esperado (brazo C, unidad limpia):** cero detecciones; toda detección de contenido que el esquema sí captura es espuria

**Output verbatim del descubrimiento** (`tool_input_crudo`):

~~~json
{
  "hallazgos": [
    {
      "descripcion": "\"Se incluirán los flujos de fondos nocionales futuros sujetos a reapreciación de activos, pasivos y partidas fuera de balance sensibles a variaciones en la tasa de interés.\" — La norma especifica QUÉ conceptos deben incluirse en la presentación informativa mediante una lógica de clasificación: los fondos que cumplan ciertas características (ser nocionales, ser futuros, ser sensibles a tasa de interés) forman el conjunto a incluir.",
      "por_que_no_encaja": "Ninguno de los 6 tipos de entidad captura una regla de inclusión de elementos de un conjunto. Tampoco encaja en Operacion (que son actos regulados), ni en Obligacion (que es un deber positivo general, no una clasificación de qué incluir en un informe). El predicado 'regula' conecta restricción u obligación con operación, pero no hay un tipo que represente 'criterio de clasificación de contenido informativo'. La definición de qué entra y qué no entra en un concepto informativo es un esquema clasificatorio que el esquema de referencia no prevé."
    },
    {
      "descripcion": "\"Activos que se deducen del capital ordinario del nivel 1 (COn1); Activos fijos; Posiciones en acciones en la cartera de inversión.\" — La norma enumera explícitamente qué conceptos quedan EXCLUIDOS de la presentación.",
      "por_que_no_encaja": "Aunque el esquema define Excepcion como una condición que suspende o relaja una Restriccion u Obligacion, la exclusión de conceptos de un universo informativo no es la suspensión de una prohibición o un deber particular: es un criterio de demarcación sobre qué entra en el perímetro del reporte. Representarla como Excepcion deformaría su naturaleza: no es una condición especial que 'relaja' una regla, sino una definición negativa del alcance. Además, Excepcion solo puede exceptuar restricciones u obligaciones existentes (según el predicado), pero aquí no hay una restricción u obligación previa que sea 'exceptuada'."
    },
    {
      "descripcion": "\"Los datos se informarán con frecuencia trimestral y se integrarán con los datos correspondientes al último mes de cada trimestre (marzo, junio, septiembre y diciembre), sobre base individual y consolidada mensual.\" — La norma establece tanto la periodicidad de la presentación (trimestral) como la base temporal de consolidación de los datos (último mes de cada trimestre, con periodización mensual).",
      "por_que_no_encaja": "La especificación de periodicidad y base de consolidación de un informe no es un deber (Obligacion) ni una prohibición (Restriccion), sino una característica metadata del acto informativo. Obligacion captura deberes como 'presentarán', 'calcularán', 'informarán', pero no la propiedad técnica de CÓMO se consolida o CON QUÉ FRECUENCIA se reporta. Representarlo como Obligacion ('deberán informar con frecuencia trimestral') simplificaría el contenido: la norma no ordena un comportamiento, sino que define parámetros operacionales de un proceso ya establecido."
    },
    {
      "descripcion": "\"Serán aplicables los siguientes códigos de consolidación definidos en la Sección 2.: Base individual (código de consolidación 0 o 1); Base consolidada (código de consolidación 2).\" — La norma remite a definiciones de códigos técnicos de consolidación y enumera qué códigos aplican.",
      "por_que_no_encaja": "La asignación de códigos técnicos y la remisión a un catálogo de clasificación no es un predicado que el esquema captura. No es una Restriccion (no prohibe ni limita), no es una Obligacion (no ordena un deber), y no es una Operacion (es metadata normativa sobre cómo clasificar la información). El esquema no prevé un tipo para 'tabla de clasificación' ni un predicado que exprese 'aplican estos códigos definidos en otra sección'."
    },
    {
      "descripcion": "\"Se regirá por los plazos de presentación previstos para el régimen informativo contable mensual correspondiente al mes siguiente al del cierre de cada trimestre.\" — La norma condiciona los plazos de presentación de este régimen particular a los plazos ya establecidos para el régimen informativo contable mensual.",
      "por_que_no_encaja": "Esta es una conexión entre dos Operaciones (el régimen de información sobre riesgo de tasa de interés y el régimen informativo contable mensual) mediante una relación de 'herencia de plazos': el primero hereda los plazos del segundo. El esquema no prevé un predicado que exprese esta relación. El predicado 'condiciona' conecta Obligacion → Operacion, pero aquí la condición no es una obligación, es una referencia a plazos de otro régimen. El predicado 'modificada_por' conecta TextoOrdenado → Comunicacion (para cambios formales de la norma), no para heredar parámetros de otro acto regulado."
    }
  ]
}
~~~

### 20. `ric::8.1.4` — brazo C

- **Esperado (brazo C, unidad limpia):** cero detecciones; toda detección de contenido que el esquema sí captura es espuria

**Output verbatim del descubrimiento** (`tool_input_crudo`):

~~~json
{
  "hallazgos": [
    {
      "descripcion": "\"Los bancos comerciales que ejerzan la función de custodia de los títulos representativos de las inversiones del Fondo de Garantía de Sustentabilidad del Sistema Integrado Previsional Argentino (FGS), informarán el importe total de esos valores en custodia, sobre la base de los saldos al cierre de cada mes.\" La norma establece una obligación de información sobre saldos de custodia, pero condiciona esa presentación informativa a un requisito temporal recurrente: que se base en los saldos al cierre de cada mes. Este requisito temporal no es una mera operación regulada sino una condición que parametriza CÓMO debe ejecutarse la obligación (periodicidad y punto de referencia del cálculo).",
      "por_que_no_encaja": "El esquema dispone del predicado `condiciona` (Obligacion → Operacion), pero aquí la condición no es una Operacion distinta que dispara o modula la obligación, sino un parámetro técnico de ejecución (temporalidad: \"cierre de cada mes\"). La estructura temporal de una obligación recurrente (periodicidad y base de cálculo) es contenido normativo que el esquema no captura: no es una Operacion separada ni un predicado binario Obligacion-a-Obligacion. Representarlo como `condiciona` deformaría la naturaleza de la relación: no es que una Operacion haga que otra Obligacion suceda, sino que la Obligacion misma inhiere un parámetro de periodicidad y cálculo."
    }
  ]
}
~~~
