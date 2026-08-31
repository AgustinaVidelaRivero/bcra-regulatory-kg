# Manifiesto de unidades dopadas — control rediseñado P1′ (U-ESQ-1d.b)

**Estado: APROBADO por la autora (freno (b) de U-ESQ-1d, 31/08/2026),
con UN reemplazo respecto de la versión presentada: la cláusula de
ext::3.17.3.5 dejó de definir una categoría de persona (tenía canal
vecino preexistente, sujeto_propuesto: un disparo por ese canal habría
contado como fallo sin canal de tipos muerto) y pasó a definir un
VALOR, sin canal vecino posible. Las otras nueve, tal cual. Este
manifiesto refleja el contenido vigente post-reemplazo.**

10 unidades dopadas = unidad real limpia del conjunto de desarrollo
+ exactamente UNA cláusula plantada en prosa (5 de tipo nuevo, 5 de
predicado nuevo). Selección de bases determinística (semilla sellada
20260827; regla completa en `code/construir_dopadas_p1bis.py`).
Umbral P1′: A′ ≥7/10 en total Y ≥3/5 en cada mitad — cuenta el
disparo del canal esperado de cada mitad, no ningún valor de cadena
particular. Las cadenas plantadas y los conceptos NO aparecen en
ningún prompt ni ejemplo (no sembrar): solo en el texto de la propia
unidad dopada.

Alcance declarado (adenda §3): este control prueba capacidad de
disparo sobre contenido claro y plantado; no mide sensibilidad sobre
contenido real sutil. Las dopadas son material de instrumento: no
entran a ningún conteo de ESQ-1.

## Mitad TIPO (5) y mitad PREDICADO (5)

### dop::tipo::cap::8.3.2.4

- **Unidad base:** `cap::8.3.2.4` (No prever pago de ningún tipo en concepto de capital, excepto en caso )
- **Mitad / canal esperado:** tipo → `tipo_propuesto`
- **Concepto plantado:** sanción pecuniaria (multa por incumplimiento)
- **Por qué está fuera del esquema:** una sanción es la consecuencia jurídica de un incumplimiento: no es prohibición ni límite (Restriccion), no es deber positivo (Obligacion), no suspende ninguna norma (Excepcion) y no es un acto regulado del sujeto (Operacion).
- **Cláusula plantada (verbatim, se appendea como párrafo final del texto de la unidad):**

  > El incumplimiento de las condiciones establecidas en este punto dará lugar a la aplicación de una sanción de multa equivalente al 0,5 % del valor computable del instrumento, conforme al régimen sancionatorio previsto en la Ley de Entidades Financieras.

### dop::predicado::cap::2.5.5

- **Unidad base:** `cap::2.5.5` (El término “exposición” abarca a todas las financiaciones otorgadas po)
- **Mitad / canal esperado:** predicado → `predicado_propuesto`
- **Concepto plantado:** equivalencia entre dos operaciones (Operacion→Operacion)
- **Por qué está fuera del esquema:** ningún predicado de la lista de 12 conecta Operacion con Operacion; «se considerarán equivalentes» tampoco es re-expresable invirtiendo dirección ni re-tipando sin perder el contenido.
- **Cláusula plantada (verbatim, se appendea como párrafo final del texto de la unidad):**

  > A los fines de esta sección, las operaciones de pase pasivo en pesos mencionadas precedentemente se considerarán equivalentes a las tenencias de títulos públicos que les dieron origen.

### dop::tipo::cla::6.5.2.1

- **Unidad base:** `cla::6.5.2.1` (En observación.)
- **Mitad / canal esperado:** tipo → `tipo_propuesto`
- **Concepto plantado:** presunción legal (iuris et de iure)
- **Por qué está fuera del esquema:** una presunción fija un hecho tenido por cierto: no impone deber (Obligacion), no prohíbe ni limita (Restriccion), no exceptúa norma alguna (Excepcion) ni describe un acto regulado (Operacion).
- **Cláusula plantada (verbatim, se appendea como párrafo final del texto de la unidad):**

  > Se presumirá, sin admitir prueba en contrario, que el cliente mantiene la capacidad de pago descripta en este punto cuando la totalidad de sus obligaciones registre atrasos inferiores a 30 días.

### dop::predicado::cla::6.5.3.3

- **Unidad base:** `cla::6.5.3.3` (Cuente con una dirección de poca capacidad y/o experiencia y/o de hone)
- **Mitad / canal esperado:** predicado → `predicado_propuesto`
- **Concepto plantado:** complementariedad entre dos deberes/actos de clasificación
- **Por qué está fuera del esquema:** «complementa» entre dos revisiones/recalificaciones (ambas tipables como Obligacion u Operacion) no matchea ningún predicado ni ninguna firma dominio/rango de la matriz.
- **Cláusula plantada (verbatim, se appendea como párrafo final del texto de la unidad):**

  > La revisión de la clasificación motivada por este indicador complementará a la recalificación periódica prevista en esta sección, sin sustituirla.

### dop::tipo::ext::3.17.3.5

- **Unidad base:** `ext::3.17.3.5` (el monto equivalente de los pagos realizados desde el 01/07/22 por el)
- **Mitad / canal esperado:** tipo → `tipo_propuesto`
- **Concepto plantado:** término definido (definición normativa de un valor)
- **Por qué está fuera del esquema:** una definición fija el sentido de un término: no manda, no prohíbe, no exceptúa ni es un acto; define un valor, no un sujeto ni una operación, así que tampoco tiene canal vecino posible (sujeto_propuesto no aplica).
- **Cláusula plantada (verbatim, se appendea como párrafo final del texto de la unidad):**

  > A los efectos de este punto, se entiende por "valor de referencia ajustado" el promedio simple de los tipos de cambio de cierre de los últimos cinco días hábiles, incrementado en el porcentaje que establezca la reglamentación.

### dop::predicado::ext::6.5.2

- **Unidad base:** `ext::6.5.2` (Persona jurídica.)
- **Mitad / canal esperado:** predicado → `predicado_propuesto`
- **Concepto plantado:** asimilación entre dos operaciones (Operacion→Operacion)
- **Por qué está fuera del esquema:** misma familia que la equivalencia: no existe predicado Operacion→Operacion y «quedan asimiladas a» no es prohibición, límite, excepción ni condición.
- **Cláusula plantada (verbatim, se appendea como párrafo final del texto de la unidad):**

  > A los efectos de esta reglamentación, las operaciones de cambio concertadas por dichas sucursales quedan asimiladas a las operaciones concertadas por su casa matriz.

### dop::tipo::pro::1.1.1

- **Unidad base:** `pro::1.1.1` (Usuario de servicios financieros.)
- **Mitad / canal esperado:** tipo → `tipo_propuesto`
- **Concepto plantado:** cláusula de vigencia diferida (disposición transitoria)
- **Por qué está fuera del esquema:** una regla de vigencia predica sobre la norma misma (cuándo rige), no sobre la conducta de un sujeto: no encaja en deber, prohibición, excepción ni acto regulado.
- **Cláusula plantada (verbatim, se appendea como párrafo final del texto de la unidad):**

  > Las previsiones del presente punto entrarán en vigencia a los ciento ochenta días corridos de su difusión, rigiendo hasta esa fecha el alcance establecido en la reglamentación que se reemplaza.

### dop::predicado::pro::3.2.3.6

- **Unidad base:** `pro::3.2.3.6` (La documentación relativa a la designación de los responsables de aten)
- **Mitad / canal esperado:** predicado → `predicado_propuesto`
- **Concepto plantado:** acreditación de cumplimiento (deber→deber)
- **Por qué está fuera del esquema:** «acredita el cumplimiento de» conecta dos deberes; no es requiere (Operacion→Obligacion), no es condiciona (Obligacion→Operacion), no exceptúa nada.
- **Cláusula plantada (verbatim, se appendea como párrafo final del texto de la unidad):**

  > La conservación de la documentación indicada en este punto acreditará el cumplimiento de la obligación de designación prevista en el punto 3.1.1.

### dop::tipo::ric::8.1.2

- **Unidad base:** `ric::8.1.2` (Código 70500000.)
- **Mitad / canal esperado:** tipo → `tipo_propuesto`
- **Concepto plantado:** facultad discrecional de la autoridad (permiso, no deber)
- **Por qué está fuera del esquema:** una facultad («queda facultada», «podrá») es deónticamente distinta del deber y de la prohibición; el esquema no tiene categoría para permisos/potestades.
- **Cláusula plantada (verbatim, se appendea como párrafo final del texto de la unidad):**

  > La Superintendencia de Entidades Financieras y Cambiarias queda facultada para adecuar el porcentaje indicado precedentemente cuando la evolución de las condiciones de mercado lo justifique.

### dop::predicado::ric::10.1.1

- **Unidad base:** `ric::10.1.1` (Disposiciones generales.)
- **Mitad / canal esperado:** predicado → `predicado_propuesto`
- **Concepto plantado:** cómputo conjunto entre dos requerimientos informativos
- **Por qué está fuera del esquema:** «se computa conjuntamente con» entre dos requerimientos (Obligacion→Obligacion) no tiene predicado en la lista ni firma válida en la matriz dominio/rango.
- **Cláusula plantada (verbatim, se appendea como párrafo final del texto de la unidad):**

  > El requerimiento previsto en el presente punto se computará conjuntamente con el previsto para el régimen informativo de Supervisión a los fines del control de cumplimiento.
