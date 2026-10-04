"""
borrador_prefijo_r2.py — U-PROMPT-R2 P1 (USD 0): BORRADOR del
prefijo r2 como reemplazos declarados, cada uno con ancla única, sobre el
texto sellado del perfil v3_b54 (prompt_v3_b54.PREFIJO_SISTEMA_V3,
sha 35e88c2d…), más el bloque de catálogo r2 generado desde el JSON único
(catalogo_unico/generados_r2/bloque_catalogo_r2.txt). Es el mismo mecanismo
de prompt_congelado.py y prompt_v3_b54.py: el texto sellado se importa y no
se edita.

No es el módulo del perfil (ese es de P2, en e1_extractor/): es la herramienta de P1 para (1) imprimir el lado a
lado del documento de diseño, (2) medir el largo del prefijo nuevo para el
censo de costo y (3) controlar la no-filtración (ninguna ventana de 5
palabras de un chunk de prueba en el texto agregado).

Uso: python -B borrador_prefijo_r2.py --repo <raíz del repo> --variante A|B --salida <dir>
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

# ------------------------------------------------------------------------- #
# Textos nuevos. Cada entrada: (id, decisión que lo manda, ancla vieja, texto nuevo)
# ------------------------------------------------------------------------- #

R_INTRO = (
    "R0", "L-ESQ-R2 §9 (esquema r2); decisión 10 (catálogo r2); decisión 5",
    "Trabajás con un schema CERRADO y RÍGIDO (esquema v2, catálogo de sujetos v2.0). NO inventes tipos. NO inventes predicados. NO inventes sujetos.",
    "Trabajás con un schema CERRADO y RÍGIDO (esquema r2, catálogo de sujetos r2). NO inventes tipos. NO inventes predicados. NO inventes sujetos. Lo que el texto expresa y el schema no puede representar NO se fuerza en una caja equivocada ni se calla: se registra en `omisiones` (ver OMISIONES).",
)

R_COMUNICACION = (
    "R1", "decisiones 8 y 16 (L-ESQ-R2 §2.3 y §2.4; protocolo D7)",
    '1. **Comunicacion**: Una Comunicación A/B/C del BCRA citada en el texto. Ej.: "Com. A 7825", "Comunicación A 7000".\n   Properties: codigo (string, ej. "A-7825"), tipo ("A"|"B"|"C"), numero (int).',
    '1. **Comunicacion**: Una Comunicación A/B/C del BCRA citada en el texto (ej.: "Com. A 7825", "Comunicación A 7000"), o una norma externa citada: una ley, un decreto o una resolución.\n   Properties: codigo (string: para una Comunicación, la forma "A-7825"; para una norma externa, su denominación tal como la cita el texto). NO emitas el tipo ni el número: el código los deriva de `codigo`.',
)

R_TO = (
    "R2", "decisión 16 (protocolo D7; r3_freno.md §3)",
    "   Properties: materia, archivo, version.",
    "   Sin properties: la materia, el archivo y la versión los completa el código desde el documento fuente; no los emitas.",
)

R_OPERACION = (
    "R3", "decisión 11 y X5 (BKL-0036)",
    "quién lo lleva a cabo, con qué medios, sobre qué soporte, con qué alcance — cuando no tienen otro campo donde alojarse).",
    "quién lo lleva a cabo, con qué medios, sobre qué soporte, con qué alcance — cuando no tienen otro campo donde alojarse). El calificador que convierte el acto en el que la norma regula, y no en su versión general, es parte del acto: va en la descripción y en el label y nunca se recorta. Un acto acotado por sus condiciones, su contraparte o su modalidad no es el mismo acto sin ese acote.",
)

R_RESTRICCION = (
    "R4", "decisión 3 (L-ESQ-R2 §1.3 y §1.4, par A)",
    '   Properties: descripcion (corta, grounded), tipo ("prohibicion"|"limite_cuantitativo"|"limite_cualitativo"), opcional umbral.',
    '   Properties: descripcion (corta, grounded), tipo ("prohibicion"|"limite_cuantitativo"|"limite_cualitativo"). Sus cuantías van en `umbrales` (ver UMBRALES), no en properties.',
)

R_EXCEPCION = (
    "R5", "decisión 3; X5 (BKL-0032)",
    '   Properties: descripcion (corta).\n\n6. **Obligacion**',
    '   Properties: descripcion (corta). Sus cuantías van en `umbrales`.\n   POLARIDAD: la Excepcion dice qué queda FUERA de una regla, con el mismo sentido que el texto. Si el texto NIEGA un deber o una prohibición en general y la salvedad lo vuelve a exigir en un supuesto, la salvedad no libera de nada: es el supuesto en que el deber SÍ rige. Extraé entonces la Obligacion (o la Restriccion) acotada a ese supuesto, con su Condicion si corresponde, y no una Excepcion que diga que el deber no aplica en él. Antes de emitir una Excepcion, releé su `tramo` y verificá que la descripción no invierta el sentido del texto.\n\n6. **Obligacion**',
)

_OBLIG_VIEJO = '   Properties: descripcion (corta), tipo ("presentacion_informativa"|"calculo"|"asignacion"|"comunicacion_a_cliente"|"reporte_al_supervisor"|"otra"), opcional plazo o frecuencia.'
R_OBLIGACION = {
    "A": (
        "R6", "decisiones 3 y 20, variante A (regla actual)", _OBLIG_VIEJO,
        '   Properties: descripcion (corta), tipo ("presentacion_informativa"|"calculo"|"asignacion"|"comunicacion_a_cliente"|"reporte_al_supervisor"|"otra"), opcional frecuencia: el tramo literal que fija cada cuánto se cumple el deber (diaria, semanal, mensual, trimestral, semestral, anual, con las palabras del texto) o, si el texto fija el momento del deber sin una cuantía temporal, ese tramo. Los plazos con cuantía temporal van en `umbrales`.',
    ),
    "B": (
        "R6", "decisiones 3 y 20, variante B (plazos sin cuantía temporal fuera de frecuencia)", _OBLIG_VIEJO,
        '   Properties: descripcion (corta), tipo ("presentacion_informativa"|"calculo"|"asignacion"|"comunicacion_a_cliente"|"reporte_al_supervisor"|"otra"), opcional frecuencia: SOLO el tramo literal que fija cada cuánto se cumple el deber (diaria, semanal, mensual, trimestral, semestral, anual, con las palabras del texto). Los plazos con cuantía temporal van en `umbrales`. Un momento sin cuantía temporal no es una frecuencia: queda en la descripción y en el `tramo` de la Obligacion, no en `frecuencia`.',
    ),
}

R_CONDICION_DEF = (
    "R7", "decisión 7 (L-ESQ-R2 §6.3 y §6.4)",
    "8. **Condicion**: El ANTECEDENTE de otra norma: el supuesto que debe verificarse para que una excepción, una obligación o una restricción se active, se relaje o deje de aplicar. Por sí sola NO manda nada.",
    "8. **Condicion**: El ANTECEDENTE de otra norma o de un acto: el supuesto que debe verificarse para que una excepción, una obligación o una restricción se active, se relaje o deje de aplicar, para que una operación pueda realizarse o para que una facultad se habilite. Por sí sola NO manda nada.",
)

R_CONDICION_DESTINO = (
    "R8", "decisión 7 (L-ESQ-R2 §6.4: la instrucción deja de mandarla solo a Excepcion, Obligacion o Restriccion); Condicion sin destino en la unidad (decisión de la autora en el FRENO P1, 03/10/2026)",
    "Conectala con `condicion_de` a la Excepcion, Obligacion o Restriccion del mismo chunk cuando el texto de la unidad enuncie ese vínculo.",
    "Conectala con `condicion_de` a lo que ese supuesto condiciona en el mismo chunk, cuando el texto de la unidad enuncie ese vínculo: una Excepcion, una Obligacion o una Restriccion; una Operacion, cuando el acto solo puede realizarse si el supuesto se verifica; o una Potestad, cuando la facultad solo se habilita si el supuesto se verifica. Si lo que el supuesto condiciona no está en tu unidad (por ejemplo, la norma de un encabezado con unidad propia, cuando tu unidad es uno de sus ítems), emití la Condicion sin condicion_de: no la conectes con otro elemento del chunk.",
)

R_CONDICION_PROPS = (
    "R9", "decisión 3",
    "aunque su verbo esté en subjuntivo con forma de deber.\n   Properties: descripcion (corta, grounded).",
    "aunque su verbo esté en subjuntivo con forma de deber.\n   Properties: descripcion (corta, grounded). Sus cuantías van en `umbrales`.",
)

R_DEFINICION = (
    "R10", "decisión 16 (protocolo D7: Definicion.termino literal)",
    "   Properties: termino (el término definido, tal como lo nombra el texto), descripcion (el definiens: cita o paráfrasis fiel).",
    "   Properties: termino (el término definido, copiado tal cual lo nombra el texto: mismas palabras y en el mismo orden, sin comillas), descripcion (el definiens: cita o paráfrasis fiel).",
)

BLOQUE_COPIA_UMBRALES = """
# COPIA LITERAL (`tramo`, `umbrales`, `sujeto_mencion`, `frecuencia`, `termino`, `omisiones`)

Varios campos piden un tramo del texto «copiado tal cual»: las mismas palabras, en el mismo orden, con sus números, signos y artículos como aparecen; un solo tramo continuo (salvo en la norma compuesta con el encabezado de una lista); sin resumir, completar, reordenar ni cambiar número o género. Podés unir una palabra cortada con guion al final de línea. El código busca cada tramo en el texto del chunk y marca el que no encuentra: un tramo reformulado no se corrige, queda marcado como no verificado.

- `tramo` (toda entidad salvo el TextoOrdenado): el tramo del texto que FUNDA la entidad, el más corto que la sostenga por sí solo (la cláusula, no el párrafo entero). Sale del texto de la unidad; solo cuando la entidad se ancla en un ancestro (ver PROVENANCE) o se compone desde el encabezado de una lista (ver COMPOSICIÓN CON EL ENCABEZADO DE UNA LISTA) sale del bloque heredado. En la norma compuesta son dos segmentos. Es la evidencia de la entidad: si dudaste entre dos tipos, el tramo es lo que permite revisar la elección.
- `otras_propiedades` (entidades y relaciones): lo que el texto dice de ese elemento y la definición de su tipo no prevé, como nombre → valor. No se descarta: se registra aparte. No lo uses para lo que ya tiene campo.

# UMBRALES (Restriccion, Obligacion, Condicion, Excepcion)

`umbrales` es una lista con un elemento por cuantía que acota la norma: monto, porcentaje, plazo con cuantía temporal, cantidad de «veces», UVA. Cada elemento es `{"tramo": …}`: el tramo literal con la cuantía y la palabra o frase que fija su sentido (un máximo, un mínimo, una negación del verbo que la compara, un «hasta», un «al menos», un ponderador), copiado tal cual. El valor, la unidad, la comparación y la base los calcula el código desde el tramo: no los escribas.
- Una cuantía, un elemento: si la cláusula fija dos cuantías (dos porcentajes, un monto y un plazo), son dos elementos.
- En la Condicion: si el supuesto se define por una cuantía (un plazo de cierta cantidad de días «o más», un monto «superior a»), esa cuantía es un elemento de la Condicion.
- Límite relativo: si el tope se compara con otra magnitud y no con un número (un nivel alcanzado en un período, el monto de otra operación, el saldo de una cuenta, un precio de referencia, lo que resultaría de otro cálculo), el elemento es el tramo de esa comparación, aunque no tenga cifra. También es límite relativo un múltiplo o una fracción de otra magnitud («el doble de», «la mitad de») y un límite fijado en otro punto o en otra norma que el texto nombra: el tramo es el de la referencia, y la remisión la registra el código.
- No es una cuantía de la norma un número que fija cómo se informa o se expresa un dato (la cantidad de decimales, la unidad en que se publica) ni un término de un cálculo (un factor, un divisor, los días de una base de cálculo): va en la descripción, no en `umbrales`.
- Una Restriccion de tipo `limite_cuantitativo` tiene al menos un elemento: la cuantía o el tramo de la comparación. Si no encontrás ninguno, revisá el tipo: definir qué es un exceso o fijar la consecuencia de un incumplimiento no es un límite.
- Cuantía de una tabla serializada (ver CONTENIDO NO-PROSA): el tramo es la fila del bloque, o la parte de la fila con la cuantía, tal como está en el bloque.
- No inventes cuantías: lo que no está en el texto no va. Un valor de relleno («N/A», «según corresponda») no es una cuantía. Si la cuantía está en los ítems de una lista que el texto anuncia, va en cada ítem (ver COMPOSICIÓN CON EL ENCABEZADO DE UNA LISTA), no en el encabezado.
- La Potestad no lleva `umbrales`.

# PREDICADOS VÁLIDOS (exactamente 13, ningún otro)"""

R_BLOQUE_NUEVO = (
    "R11", "decisiones 3, 15, 16, 17 y 21; F1-A en el `tramo` de la norma compuesta; umbrales con la columna r2a de U-MED-R2A (tablero :67, c50b094) (bloque nuevo, insertado antes de PREDICADOS)",
    "\n# PREDICADOS VÁLIDOS (exactamente 13, ningún otro)",
    BLOQUE_COPIA_UMBRALES,
)

R_TABLA_APLICA = (
    "R12", "decisión 4 (L-ESQ-R2 §3.3 y §3.4)",
    "| `aplica_a` | {Restriccion, Obligacion, Operacion, Excepcion, Potestad} → SUJETO del catálogo (source = local_id del elemento alcanzado; el sujeto va en sujeto_id o sujeto_propuesto, SIN target) |",
    "| `aplica_a` | {Restriccion, Obligacion, Operacion, Excepcion, Potestad} → SUJETO (source = local_id del elemento alcanzado; el sujeto va en `sujeto_mencion`, con `sujeto_id` como sugerencia; SIN target) |",
)

R_TABLA_EJECUTA = (
    "R13", "decisión 4",
    "| `ejecuta` | SUJETO del catálogo → Operacion (target = local_id de la operación; el sujeto va en sujeto_id o sujeto_propuesto, SIN source) |",
    "| `ejecuta` | SUJETO → Operacion (target = local_id de la operación; el sujeto va en `sujeto_mencion`, con `sujeto_id` como sugerencia; SIN source) |",
)

R_TABLA_CONDICION = (
    "R14", "decisiones 7 y 12; la Comunicacion sigue con su `referencia` (decisión de la autora en el FRENO P1, 03/10/2026)",
    "| `condicion_de` | Condicion → {Excepcion, Obligacion, Restriccion} |",
    "| `condicion_de` | Condicion → {Excepcion, Obligacion, Restriccion, Operacion, Potestad} |\n\nLa remisión del texto a otro punto o a otra norma la registra el código desde el texto: no es una relación que debas emitir ni una omisión. Esto no cambia la Comunicacion: una Comunicación o una norma externa citada sigue siendo una entidad Comunicacion, con su referencia desde el TextoOrdenado; lo que no emitís es la remisión desde el contenido. Si la remisión fija el contenido de una norma del chunk, ese contenido va en la descripción y en el `tramo` de la norma.",
)

SUJETOS_VIEJO = """El sujeto de una relación `aplica_a` o `ejecuta` se ELIGE del catálogo de abajo — NO se crea:

- Poné en `sujeto_id` el id EXACTO de la entrada del catálogo que el texto nombra (matcheá por label o por alias).
- Si el punto nombra uno o más sujetos ESPECÍFICOS, emití UNA relación por CADA sujeto nombrado, usando la clase del catálogo que corresponde a ese nombre.
  ✓ "Las entidades financieras, los PSPCP y las empresas emisoras deberán informar..." → 3 relaciones aplica_a, con sujeto_id "Sujeto_entidad_financiera", "Sujeto_pspcp" y "Sujeto_empresa_no_financiera_emisora_de_tarjetas".
  ✗ MAL: una única relación hacia el rol del TO cuando el texto enumera sujetos con nombre propio.
- Usá EXACTAMENTE la clase que el texto nombra: NUNCA una más específica ni una más general. La jerarquía del grafo se ocupa de la herencia; tu trabajo es fidelidad al texto.
  ✓ el texto dice "las entidades financieras" → sujeto_id "Sujeto_entidad_financiera".
  ✗ MAL: el texto dice "las entidades financieras" y emitís "Sujeto_banco" o "Sujeto_banco_comercial" (descenso de jerarquía sin licencia del texto).
  ✗ MAL: el texto dice "los bancos comerciales" y emitís "Sujeto_entidad_financiera" (ascenso: más general que lo que el texto nombra).
- Si la norma se dirige al colectivo del TO ("las entidades", "los sujetos obligados"), usá el rol de alcance indicado en el mensaje del chunk.
- Si el texto nombra un sujeto que NO matchea ninguna entrada del catálogo ni sus alias, usá `sujeto_propuesto` (texto libre con el nombre del sujeto tal como aparece) y, si podés, `sujeto_propuesto_padre_sugerido` con el id del catálogo más cercano como padre. NO fuerces el id más parecido: ante la duda, proponé.
- `sujeto_id` y `sujeto_propuesto` son MUTUAMENTE EXCLUYENTES: exactamente uno de los dos.
- Los sujetos "del exterior" NO son entradas propias: usá la clase local correspondiente (la jurisdicción es un atributo, ya contemplado en los alias)."""

SUJETOS_NUEVO = """El sujeto de una relación `aplica_a` o `ejecuta` va en dos campos:

- `sujeto_mencion` (OBLIGATORIA en toda relación `aplica_a` o `ejecuta`): el tramo del texto que nombra al sujeto, copiado tal cual (ver COPIA LITERAL), con sus artículos y en el orden del texto; no la forma del catálogo. Si el texto de la unidad no lo nombra y el sujeto está en el contexto heredado, copiala de ahí.
- `sujeto_id` (sugerencia): el id EXACTO de la entrada del catálogo de abajo que la mención nombra (por label o por alias). La resolución final la hace el código desde la mención; tu sugerencia cuenta cuando la mención sola no alcanza.
- Si la mención no nombra ninguna entrada del catálogo ni sus alias, NO pongas `sujeto_id`: dejá la mención sola y, si podés, `sujeto_propuesto_padre_sugerido` con el id del catálogo más cercano como padre. NO fuerces el id más parecido: una mención sin id queda registrada para ampliar el catálogo; un id forzado es un error. Cuando una definición del catálogo dice que un sujeto «sigue en sujeto_propuesto», se lee así: mención sin `sujeto_id`.
- Si el punto nombra uno o más sujetos ESPECÍFICOS, emití UNA relación por CADA sujeto nombrado, cada una con su mención.
  ✓ "Las entidades financieras, los PSPCP y las empresas emisoras deberán informar..." → 3 relaciones aplica_a, con las menciones "Las entidades financieras", "los PSPCP" y "las empresas emisoras", y sujeto_id "Sujeto_entidad_financiera", "Sujeto_pspcp" y "Sujeto_empresa_no_financiera_emisora_de_tarjetas".
  ✗ MAL: una única relación hacia el rol del TO cuando el texto enumera sujetos con nombre propio.
- Usá EXACTAMENTE la clase que la mención nombra: NUNCA una más específica ni una más general. La jerarquía del grafo se ocupa de la herencia; tu trabajo es fidelidad al texto.
  ✓ el texto dice "las entidades financieras" → mención "las entidades financieras", sujeto_id "Sujeto_entidad_financiera".
  ✗ MAL: el texto dice "las entidades financieras" y emitís "Sujeto_banco" o "Sujeto_banco_comercial" (descenso de jerarquía sin licencia del texto).
  ✗ MAL: el texto dice "los bancos comerciales" y emitís "Sujeto_entidad_financiera" (ascenso: más general que lo que el texto nombra).
- Si la norma se dirige al colectivo del TO ("las entidades", "los sujetos obligados", sin otro calificativo), la mención es esa expresión y la sugerencia es el rol de alcance indicado en el mensaje del chunk: NUNCA una clase más estrecha, aunque el contexto hable de un tipo de entidad en particular.
- SUJETO ALCANZADO Y CALIFICADOR. La mención nombra al sujeto, no lo que acota el alcance de la norma. Si el texto agrega a un sujeto un calificativo que restringe a qué operaciones o actos de ese sujeto se aplica la norma, el sujeto es la clase nombrada (una mención por sujeto, sin el calificativo) y el calificativo es contenido de la norma: va en su descripción y en su `tramo`, y nunca se pierde. Una excepción para un sujeto en lo que respecta a una de sus actividades no exceptúa al sujeto entero.
- Una Obligacion o una Restriccion lleva `aplica_a` solo hacia el sujeto que el texto obliga o al que le prohíbe algo. Si el texto enuncia en voz pasiva un acto que realiza otro (la autoridad, un registro, un tercero), ese acto no es un deber del sujeto regulado: no se lo atribuyas con `aplica_a`; si es un efecto del deber del sujeto, va en la descripción de ese deber.
- `sujeto_id` y `sujeto_propuesto_padre_sugerido` son MUTUAMENTE EXCLUYENTES: a lo sumo uno de los dos.
- Los sujetos "del exterior" tienen entrada propia cuando el catálogo la tiene (entidades financieras, bancos y entidades cambiarias del exterior); si no, usá la clase local correspondiente."""

R_SUJETOS = ("R15", "decisiones 4, 10 y 11; X5 (BKL-0033); X9 (BKL-0009 a BKL-0016)", SUJETOS_VIEJO, SUJETOS_NUEVO)

R_REGLA1 = (
    "R16", "X5 (BKL-0035); F1-A y tratamiento por tipo del encabezado (decisiones de la autora, 03/10/2026)",
    "El número de punto va en el campo `punto`, no en una entidad.\n\n2.",
    "El número de punto va en el campo `punto`, no en una entidad. Tampoco es una entidad el anuncio de una lista: la unidad de un encabezado que abre una lista no emite una Obligacion, una Restriccion ni una Potestad cuyo único contenido es que siguen ítems, ni lo que se compone en cada ítem (el sujeto, la modalidad, el cuantificador y lo que el encabezado fija para cada ítem; ver COMPOSICIÓN CON EL ENCABEZADO DE UNA LISTA). Lo que el encabezado enuncia aparte de la lista (una norma propia, una excepción a la lista entera, la norma principal cuando los ítems son sus supuestos o condiciones) se extrae en su unidad como siempre.\n\n2.",
)

R_CHUNK_PUNTO = (
    "R28", "F1-A de U-DIAG-PROCESO (decisión de la autora, 03/10/2026)",
    "Extraés SOLO del texto del punto; el contexto heredado orienta y ancla, pero NO se extrae de él (cada bloque heredado tiene su propia unidad de extracción responsable — ver PROVENANCE).",
    "Extraés SOLO del texto del punto; el contexto heredado orienta y ancla, pero NO se extrae de él (cada bloque heredado tiene su propia unidad de extracción responsable — ver PROVENANCE), salvo un caso: si el punto es un ítem de una lista que abre el contexto heredado, su norma se compone con ese encabezado (ver COMPOSICIÓN CON EL ENCABEZADO DE UNA LISTA).",
)

R_PROVENANCE = (
    "R29", "F1-A de U-DIAG-PROCESO (decisión de la autora, 03/10/2026)",
    "y extraerlo acá duplicaría y anclaría mal.",
    "y extraerlo acá duplicaría y anclaría mal. La única excepción es la composición con el encabezado de una lista (ver COMPOSICIÓN CON EL ENCABEZADO DE UNA LISTA): ese encabezado puede no tener unidad propia (cuando está en la línea de título del punto que lo contiene) y, cuando la tiene, esa unidad no extrae la norma de los ítems.",
)

BLOQUE_COMPOSICION = """
# COMPOSICIÓN CON EL ENCABEZADO DE UNA LISTA

Un encabezado que abre una lista termina en «:»: es la línea de título de un punto (bloque heredado `encabezado`, sin unidad propia) o un párrafo introductorio con unidad propia. Enuncia parte de una norma cuyo contenido está repartido en los ítems. Si el contexto heredado termina en un encabezado así y tu unidad es uno de sus ítems, mirá qué son los ítems:
- CONTENIDOS (lo que hay que hacer, informar, incluir o cumplir; los miembros de una clase que el encabezado nombra): la norma del ítem es la COMPUESTA. Extraela entera en el ítem, con `punto` = el ítem: el sujeto del encabezado, su modalidad (deber, prohibición o facultad), su cuantificador (si los ítems se exigen todos o si basta con cualquiera de ellos) y el contenido del ítem. La descripción dice la norma completa y conserva el cuantificador. Si el encabezado no trae el sujeto o la modalidad, tomalos del bloque heredado más cercano que los trae.
- SUPUESTOS O CONDICIONES de una norma que el encabezado enuncia: el ítem es una Condicion (ver Condicion) y la norma queda en la unidad del encabezado; como esa norma no está en tu unidad, la Condicion va sin `condicion_de` (ver Condicion). Si el encabezado es la línea de título de un punto, no tiene unidad propia; entonces:
  - si los supuestos son alternativos (basta cualquiera: «o», «alguno de», «cualquiera de»), la norma del ítem es la COMPUESTA: la del encabezado con el supuesto del ítem, y conserva el cuantificador;
  - si se exigen juntos («y», «la totalidad», «concurrentemente») o no queda claro, el ítem es solo una Condicion, y la norma del encabezado no se extrae en ningún ítem: repetirla con una sola condición la daría por suficiente.

En la norma compuesta:
- El sujeto del encabezado va también en la relación `aplica_a` o `ejecuta` del ítem, con la mención copiada del encabezado.
- Lo que el encabezado fija para cada ítem (un plazo, un ámbito, una condición que vale para todos los ítems) también se compone en el ítem: el plazo, como elemento de `umbrales` de la norma compuesta; la condición, como Condicion del ítem con `condicion_de` hacia esa norma. Su `tramo` es el segmento del encabezado, tomado del contexto heredado.
- El `tramo` de la entidad compuesta lleva dos segmentos, cada uno copiado tal cual y unidos por « […] »: primero el del encabezado, tomado del contexto heredado (puede abarcar bloques heredados seguidos, como una línea de título y el párrafo que la continúa); después el del ítem, tomado del texto de tu unidad.

En la unidad del encabezado:
- No se emite un nodo por el solo anuncio de la lista (regla 1), ni lo que se compone en los ítems: así no hay duplicados.
- Sí se extrae lo que el encabezado enuncia aparte de la lista: una norma propia, una excepción a la lista entera, y la norma principal cuando los ítems son sus supuestos o condiciones.

# REGLAS NO NEGOCIABLES"""

R_COMPOSICION = (
    "R30", "F1-A de U-DIAG-PROCESO y tratamiento por tipo del encabezado (decisiones de la autora, 03/10/2026; sección nueva, insertada antes de REGLAS)",
    "\n# REGLAS NO NEGOCIABLES",
    BLOQUE_COMPOSICION,
)

R_REGLA4 = (
    "R17", "decisiones 5 y 17 (L-ESQ-R2 §5.3 y §8.3; protocolo D8)",
    "4. **NO inventes tipos ni predicados fuera de las listas.** Si una idea no encaja en los 9 tipos de entidad o 13 predicados, NO la incluyas. Es preferible no extraer algo a forzarlo en una caja equivocada.",
    "4. **NO inventes tipos ni predicados fuera de las listas.** Si un contenido normativo no encaja en los 9 tipos de entidad, NO lo fuerces en el más parecido: registralo en `omisiones` con categoría `fuera_de_tipos`, su tramo y, en `nota`, el tipo que habrías usado. Si una relación que el texto expresa no encaja en los 13 predicados (por vocabulario o por dominio y rango), registrala con categoría `relacion_sin_predicado`, su tramo, `source` y `destino` (los local_id de sus extremos, si los extrajiste) y, en `nota`, el predicado que habrías usado. Es preferible registrar a forzar una caja equivocada.",
)

R_REGLA7 = (
    "R18", "decisión 4 (L-ESQ-R2 §3.4: extiende la regla 7)",
    "generá una relación `aplica_a` (o `ejecuta`) POR CADA sujeto, cada una con su propio sujeto_id del catálogo. NO metas la enumeración entera en un solo sujeto_propuesto.",
    "generá una relación `aplica_a` (o `ejecuta`) POR CADA sujeto, cada una con SU mención (solo ese sujeto, con su artículo si lo tiene) y su sugerencia. NO metas la enumeración entera en una sola mención.",
)

R_REGLA9_TITULO = (
    "R19", "decisión 5 (L-ESQ-R2 §5.3: la regla 9 registra en lugar de callar)",
    "9. **CONTENIDO META-NORMATIVO: NO SE EXTRAE.**",
    "9. **CONTENIDO META-NORMATIVO: NO SE EXTRAE, SE REGISTRA.**",
)

R_REGLA9_CIERRE = (
    "R20", "decisión 5",
    "No lo fuerces en Restriccion, Obligacion, Potestad ni Definicion: simplemente no lo extraigas.",
    "No lo fuerces en Restriccion, Obligacion, Potestad ni Definicion: no lo extraigas y registralo en `omisiones` con categoría `meta_normativo` y su tramo.",
)

NOPROSA_VIEJO = """# CONTENIDO NO-PROSA (chunks flaggeados por E0)

Si el mensaje del chunk trae un bloque "FLAGS E0" (contenido tabular y/o fórmulas detectados determinísticamente), ese contenido está DECLARADO NO-CONFIABLE en su forma extraída del PDF:

- NO reconstruyas tablas ni fórmulas: la estructura visual (columnas, alineación, sub/superíndices) pudo haberse destruido en la extracción del PDF, y una lectura "prolija" de texto destrozado fabrica contenido falso.
- Extraé SOLO lo que la prosa circundante sostiene por sí sola (el enunciado de que existe una exigencia, quién la cumple, a qué operación refiere).
- NO copies valores numéricos de celdas de tabla ni coeficientes de fórmulas a properties (umbral, plazo) salvo que la prosa los enuncie en una oración completa.
- Registrá en `omisiones_no_prosa` (lista de strings, uno por omisión) qué contenido quedó afuera y por qué (ej.: "tabla de ponderadores por grupo: estructura tabular no confiable, valores no extraídos").
- Si el chunk entero es tabla/fórmula y nada es extraíble con confianza, devolvé entities/relations con lo mínimo sostenible (puede ser solo el nodo TextoOrdenado) y registrá la omisión. Un chunk flaggeado SIN omisiones registradas y CON valores numéricos extraídos es una extracción sospechosa."""

NOPROSA_NUEVO = """# CONTENIDO NO-PROSA (tablas y fórmulas marcadas por E0)

El texto del chunk puede traer tablas SERIALIZADAS por E0, entre `[TABLA <id> | …]` y `[FIN TABLA <id>]`, y el mensaje puede traer un bloque "FLAGS E0". Son dos cosas distintas:

- **Tabla serializada: CONFIABLE.** E0 la reconstruyó desde la estructura del PDF y la verificó contra sus celdas. Cada fila es `Fila k: clave = valor | clave = valor`. En modo «columnas», la clave es el encabezado de su columna (las líneas `Rótulo:` y `Columnas:` lo anuncian); en modo «posicional», E0 no reconoció un encabezado y la clave es `colN`: el nombre de cada columna está en las primeras filas del bloque. Leela como texto: extraé lo que dice y COPIÁ sus valores (en `umbrales`, en el `tramo` y en la descripción) tal como figuran en el bloque, asociando cada valor a su columna y a su fila. `⟨combinada con fila n⟩` marca un valor que el PDF escribe una sola vez, en la fila n, y que vale también en esa fila; `⟨abarca hasta c⟩` marca un valor que ocupa varias columnas, hasta la columna c. No reordenes filas ni columnas y no completes celdas que el bloque no trae. El mensaje lista cada tabla con lo que E0 no pudo resolver: una fila de subtítulo no es un dato y califica a las filas que la siguen; el valor de una celda combinada que E0 no asignó a sus filas puede valer para varias filas sin que el bloque indique cuáles, y si el texto no lo aclara no se asocia a ninguna: se registra la omisión `tabla`.
- **Contenido tabular residual y fórmulas: NO CONFIABLES.** Lo que el bloque "FLAGS E0" declara como contenido tabular residual (una tabla que E0 no pudo serializar, una tabla serializada que el mensaje declare no confiable, o texto con forma de tabla fuera de los bloques) y las fórmulas siguen DECLARADOS NO-CONFIABLES en su forma extraída del PDF:
  - NO reconstruyas tablas ni fórmulas: la estructura visual (columnas, alineación, sub/superíndices) pudo haberse destruido en la extracción del PDF, y una lectura "prolija" de texto destrozado fabrica contenido falso.
  - Extraé SOLO lo que la prosa circundante sostiene por sí sola (el enunciado de que existe una exigencia, quién la cumple, a qué operación refiere).
  - NO copies valores numéricos de ese contenido ni coeficientes de fórmulas a `umbrales` salvo que la prosa los enuncie en una oración completa.
  - Registrá en `omisiones` lo que quedó afuera, con categoría `tabla` o `formula`, su tramo y, en `nota`, por qué.
  - Si el chunk entero es contenido no confiable y nada es extraíble con confianza, devolvé lo mínimo sostenible (puede ser solo el nodo TextoOrdenado) y registrá la omisión. Un chunk con contenido no confiable SIN omisiones registradas y CON valores numéricos extraídos de ese contenido es una extracción sospechosa."""

R_NOPROSA = ("R21", "decisión 6 (plan :399, notas del 02/10; L-ESQ-R2 §1.4 r2b y §5.4)", NOPROSA_VIEJO, NOPROSA_NUEVO)

R_NEG_PRED = (
    "R22", "coherencia (13 predicados desde el congelado) y decisión 5",
    '- ❌ Predicado "regulado_por" o "contiene" o "se_aplica_si" → no están en la lista de 12.',
    '- ❌ Predicado "regulado_por" o "contiene" o "se_aplica_si" → no están en la lista de 13. Si la relación está en el texto y ningún predicado la representa, va a `omisiones` como `relacion_sin_predicado`.',
)

R_NEG_APLICA = (
    "R23", "decisión 4; alineación con BKL-0038 (una Restriccion no usa regula)",
    "- ❌ Restriccion --aplica_a--> Operacion → MAL, `aplica_a` requiere un SUJETO del catálogo como rango (sujeto_id). Usá `regula` o `prohibe`/`limita`.",
    "- ❌ Restriccion --aplica_a--> Operacion → MAL, `aplica_a` requiere un SUJETO como rango (en `sujeto_mencion`). Usá `prohibe` o `limita`, según el tipo de la Restriccion.",
)

R_NEG_SUJETO = (
    "R24", "decisión 4",
    "- ❌ Entidad de tipo \"EntidadFinanciera\" o \"Sujeto\" → los sujetos NO son entidades del chunk: van en sujeto_id/sujeto_propuesto de aplica_a/ejecuta.\n- ❌ sujeto_id \"Sujeto_entidad_financiera\" para \"empresas de seguros\" → si el sujeto no matchea entrada ni alias del catálogo, usá sujeto_propuesto; NO fuerces el más parecido.",
    "- ❌ Entidad de tipo \"EntidadFinanciera\" o \"Sujeto\" → los sujetos NO son entidades del chunk: van en la mención (con su sugerencia) de aplica_a/ejecuta.\n- ❌ sujeto_id \"Sujeto_entidad_financiera\" para \"empresas de seguros\" → si la mención no nombra entrada ni alias del catálogo, va sin sujeto_id; NO fuerces el más parecido.\n- ❌ sujeto_mencion \"Sujeto_entidad_financiera\" o \"Entidades financieras\" cuando el texto dice otra cosa → la mención es el texto del chunk, no el catálogo.\n- ❌ Excepcion que dice que un deber no aplica en el supuesto en que el texto lo exige → invierte la polaridad (ver Excepcion).",
)

REGLA_LIMITA_VIEJO = """Tres predicados Restriccion→Operacion. NO son intercambiables. Elegí según `Restriccion.tipo`:

- Si `Restriccion.tipo = "prohibicion"` → usá `prohibe`. Patrón: "no podrá", "se prohíbe", "queda prohibido".
- Si `Restriccion.tipo = "limite_cuantitativo"` (hay umbral numérico: %, $, monto) → usá `limita`.
- Si `Restriccion.tipo = "limite_cualitativo"` (restricción cualitativa sin monto) → usá `limita`.
- `regula` queda RESERVADO para Obligacion→Operacion. Cuando una Obligacion regula cómo se hace una Operacion, usá `regula`.

✅ Restriccion(tipo=prohibicion) --prohibe--> Operacion
✅ Restriccion(tipo=limite_cuantitativo, umbral="10%") --limita--> Operacion
✅ Restriccion(tipo=limite_cualitativo) --limita--> Operacion
✅ Obligacion --regula--> Operacion
❌ Restriccion(tipo=limite_cuantitativo) --regula--> Operacion  ← MAL, usá `limita`
❌ Restriccion(tipo=prohibicion) --regula--> Operacion  ← MAL, usá `prohibe`"""

REGLA_LIMITA_NUEVO = """Tres predicados Restriccion→Operacion. NO son intercambiables. El predicado sale de `Restriccion.tipo`, y el código controla que coincidan:

- Si `Restriccion.tipo = "prohibicion"` → usá `prohibe`. Patrón: "no podrá", "se prohíbe", "queda prohibido", sin una cuantía que fije hasta dónde.
- Si `Restriccion.tipo = "limite_cuantitativo"` (hay una cuantía: %, $, monto, plazo, o un límite relativo) → usá `limita`.
- Si `Restriccion.tipo = "limite_cualitativo"` (restricción cualitativa sin monto) → usá `limita`.
- Una Restriccion NUNCA usa `regula`: `regula` queda RESERVADO para Obligacion→Operacion. Cuando una Obligacion regula cómo se hace una Operacion, usá `regula`.
- Si dudás entre prohibición y límite, decidí primero el tipo (¿el texto veda el acto o lo acota?) y usá el predicado de ese tipo. Una Restriccion "prohibicion" con `limita`, o una "limite_cuantitativo" o "limite_cualitativo" con `prohibe`, queda marcada como incoherente.
- **Destino de `limita`:** el destino de `limita` es el acto o la magnitud que el tope acota o, si es un ponderador, la exposición que pondera; no su base, su finalidad, su consecuencia ni el supuesto que lo habilita.

✅ Restriccion(tipo=prohibicion) --prohibe--> Operacion
✅ Restriccion(tipo=limite_cuantitativo, umbrales=[{tramo: "no podrá superar el 10 %"}]) --limita--> Operacion
✅ Restriccion(tipo=limite_cualitativo) --limita--> Operacion
✅ Obligacion --regula--> Operacion
❌ Restriccion(tipo=limite_cuantitativo) --regula--> Operacion  ← MAL, usá `limita`
❌ Restriccion(tipo=prohibicion) --regula--> Operacion  ← MAL, usá `prohibe`
❌ Restriccion(tipo=prohibicion) --limita--> Operacion  ← MAL: o el tipo es un límite, o el predicado es `prohibe`
❌ Restriccion --limita--> la base del tope, su finalidad o lo que pasa si se supera  ← MAL: el destino es lo que el tope acota"""

R_REGLA_LIMITA = ("R25", "P1.a (alineación con BKL-0038, plan :396) y decisión 9 (L-ESQ-R2 §1.4)", REGLA_LIMITA_VIEJO, REGLA_LIMITA_NUEVO)

FORMATO_VIEJO = """# FORMATO DE SALIDA

Llamá la herramienta `extraer_kg_e1` con el schema dado. Si el chunk no tiene contenido normativo extraíble (preámbulo vacío, lista de abreviaturas, etc.), devolvé entities y relations vacíos (el nodo TextoOrdenado igual va). Todo elemento lleva `punto`."""

FORMATO_NUEVO = """# OMISIONES (campo `omisiones`, en TODO chunk)

`omisiones` es una lista, obligatoria en todo chunk (vacía si no omitiste nada), con un elemento por cada contenido del texto de la unidad que NO extrajiste:
- `categoria`: `meta_normativo` (regla 9); `tabla` o `formula` (contenido no confiable, ver CONTENIDO NO-PROSA); `fuera_de_tipos` (contenido normativo que no encaja en ningún tipo, regla 4); `relacion_sin_predicado` (relación que el texto expresa y ningún predicado representa, regla 4).
- `tramo`: el tramo del texto PROPIO de la unidad que no extrajiste, copiado tal cual (no del contexto heredado: ese tiene su propia unidad).
- `nota`: por qué quedó afuera; en `fuera_de_tipos`, el tipo que habrías usado; en `relacion_sin_predicado`, el predicado que habrías usado.
- `source` y `destino` (solo en `relacion_sin_predicado`, opcionales): los local_id de los extremos de esa relación, si los extrajiste como entidades.
No registres como omisión lo que sí extrajiste, los títulos ni las remisiones a otros puntos o normas.

# FORMATO DE SALIDA

Llamá la herramienta `extraer_kg_e1` con el schema dado. Si el chunk no tiene contenido normativo extraíble (preámbulo vacío, lista de abreviaturas, etc.), devolvé entities y relations vacíos (el nodo TextoOrdenado igual va). Todo elemento lleva `punto`; toda entidad salvo el TextoOrdenado lleva `tramo`; toda relación `aplica_a` o `ejecuta` lleva `sujeto_mencion`; `omisiones` va siempre (vacía si no omitiste nada)."""

R_FORMATO = ("R26", "decisiones 5, 15 y 17 (L-ESQ-R2 §5.3 y §8.3; protocolo D6 y D8)", FORMATO_VIEJO, FORMATO_NUEVO)


def reemplazos(variante: str) -> list[tuple[str, str, str, str]]:
    return [R_INTRO, R_CHUNK_PUNTO, R_COMUNICACION, R_TO, R_OPERACION, R_RESTRICCION, R_EXCEPCION,
            R_OBLIGACION[variante], R_CONDICION_DEF, R_CONDICION_DESTINO, R_CONDICION_PROPS,
            R_DEFINICION, R_BLOQUE_NUEVO, R_TABLA_APLICA, R_TABLA_EJECUTA, R_TABLA_CONDICION,
            R_SUJETOS, R_PROVENANCE, R_COMPOSICION, R_REGLA1, R_REGLA4, R_REGLA7, R_REGLA9_TITULO, R_REGLA9_CIERRE,
            R_NOPROSA, R_NEG_PRED, R_NEG_APLICA, R_NEG_SUJETO, R_REGLA_LIMITA, R_FORMATO]


ANCLA_INICIO_BLOQUE = "## Sujetos regulados"
ANCLA_FIN_BLOQUE = "\n# PROVENANCE OBLIGATORIA POR ELEMENTO"


def armar(texto_v3: str, bloque_r2: str, variante: str) -> tuple[str, list[dict]]:
    t = texto_v3
    registro = []
    for rid, decision, viejo, nuevo in reemplazos(variante):
        n = t.count(viejo)
        if n != 1:
            raise RuntimeError(f"{rid}: el ancla aparece {n} veces (esperado 1)")
        t = t.replace(viejo, nuevo)
        registro.append({"id": rid, "decision": decision, "viejo": viejo, "nuevo": nuevo})
    for a in (ANCLA_INICIO_BLOQUE, ANCLA_FIN_BLOQUE):
        if t.count(a) != 1:
            raise RuntimeError(f"ancla del bloque {a!r} no única")
    i, k = t.index(ANCLA_INICIO_BLOQUE), t.index(ANCLA_FIN_BLOQUE)
    viejo_bloque = t[i:k]
    t = t[:i] + bloque_r2 + t[k:]
    registro.append({"id": "R27", "decision": "decisión 10 (L-ESQ-R2 §7.4; LN-8)",
                     "viejo": f"<bloque de catálogo v3: {len(viejo_bloque)} caracteres, "
                              f"sha256 {hashlib.sha256(viejo_bloque.encode()).hexdigest()[:12]}…>",
                     "nuevo": f"<bloque_catalogo_r2.txt: {len(bloque_r2)} caracteres, "
                              f"sha256 {hashlib.sha256(bloque_r2.encode()).hexdigest()[:12]}…>"})
    return t, registro


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--variante", choices=("A", "B"), required=True)
    ap.add_argument("--salida", required=True)
    a = ap.parse_args()
    repo = Path(a.repo)
    for p in (repo / "data/experiment/b54_catalogo_v3/code", repo / "data/experiment/esq/code",
              repo / "data/experiment/reextraccion_v2/e1_extractor"):
        sys.path.insert(0, str(p))
    import prompt_v3_b54 as v3  # noqa: PLC0415 — módulo sellado, solo lectura
    assert v3.PREFIJO_SHA256_V3 == "35e88c2dd0a2920302c29005b08ab9689405606d4bd5fcf8fb7ce807b1a3c512"
    bloque = (repo / "data/experiment/catalogo_unico/generados_r2/bloque_catalogo_r2.txt").read_text(encoding="utf-8")
    texto, registro = armar(v3.PREFIJO_SISTEMA_V3, bloque, a.variante)
    out = Path(a.salida)
    out.mkdir(parents=True, exist_ok=True)
    (out / f"prefijo_r2_borrador_{a.variante}.txt").write_text(texto, encoding="utf-8")
    (out / f"reemplazos_r2_borrador_{a.variante}.json").write_text(
        json.dumps(registro, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"variante {a.variante}: {len(texto)} caracteres, sha256 "
          f"{hashlib.sha256(texto.encode()).hexdigest()}; {len(registro)} reemplazos")


if __name__ == "__main__":
    main()
