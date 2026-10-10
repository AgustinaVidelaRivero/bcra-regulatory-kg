# Regla de calificación v1 (U-MED-UMBRALES, etapa P)

**PARA SELLAR.** Texto consolidado por la mesa el 10/10/2026, con las decisiones de la autora del mismo día sobre el borrador de 28
cambios, más dos cambios nuevos (C29 y C30). Sale de la v0 (`data/experiment/med_umbrales/p/regla_calificacion_v0.md`, sha256 `22eb6a78…`,
el §2 de la enmienda 1 firmada en `a0f9815`), que no se edita.

- Rige para el lote 2 del piloto. Se sella (sha256 y hora) antes del lote 2.
- La regla del §5.4 de la enmienda se sella al cerrar el piloto.
- Al pie va la lista de los cambios, cada uno con su número.

---
## 2. Unidad y campos

**2.1 Unidad.** El elemento de umbral, no el nodo: un nodo puede tener varios (1.306 elementos en 1.123 nodos en el grafo sin cola de la
tanda 0, `estratos_umbrales_salida_UMEDUMBRALES.txt`).

**2.2 Referencia.** El texto de la unidad de E0 del nodo, propio y heredado, en la versión de E0 con la que se construyó el grafo medido,
que es la que trae el material (C29). La página del PDF, si el texto de E0 es dudoso. Nunca la descripción del nodo ni otra salida de un
modelo.

**2.3 Resultado por campo.** *Correcto*; *contradicho* (el grafo dice otra cosa); *omitido* (la letra lo fija y el campo está vacío o
`no_determinada`); *espurio* (el campo está lleno y la letra no lo fija); *parcial* (solo la base); *no aplica*; *no decidible* (necesita
un experto, o el texto o la tabla no se leen), que se reporta aparte con sus dos cotas. Toda base *parcial* lleva una nota: el
calificador que falta y si con la base guardada se calcula otro monto (C16).

| campo | aplica a | correcto si | casos límite |
|---|---|---|---|
| **pertinencia** (precondición; se juzga en el paso 2, primero, §5 de abajo) | todo elemento | la cuantía (en los del validador, el límite relativo) está en el texto de la unidad, propio o heredado, y fija un umbral, plazo, porcentaje o coeficiente de la regla que representa el nodo. La regla se identifica por la etiqueta y el tramo del nodo, nunca por la descripción (C7, C9). Un monto fijo («la multa será de $…») es pertinente (C9) | *no pertinente*: el número de una norma citada, una fecha, el número de un punto, un ejemplo, o la cuantía de otra regla del mismo párrafo; *inexistente*: la cuantía no está en la norma (sale de la descripción); *duplicado*: el segundo elemento, en el orden del grafo, que representa la misma aparición de la cuantía en el texto; dos apariciones distintas del mismo número no son duplicado (C8) |
| **valor** | elementos con cuantía; en los del validador, que la cláusula no traiga cuantía | numéricamente igual a la cuantía, normalizada | «1,25 %» → 1.25; «$ 5.000 millones» → 5000000000; «tres veces» → 3; «90 (noventa) días» → 90; «el décimo día hábil» después de «hasta el» → 10; una cuantía en letras vale como en cifras (C15); *contradicho*: otro número, otro multiplicador, un compuesto partido («treinta y cinco» leído como 5); *omitido*: un elemento del validador sin valor cuando la cláusula trae cuantía, en cifras o en letras (C15) |
| **unidad** | ídem | la de la norma en la lista cerrada (porcentaje, moneda, días, meses, años, veces, UVA); una unidad fuera de la lista (horas, semanas u otra), con la marca `fuera_de_lista`, que vale para cualquier campo de lista cerrada (C11) | una unidad fuera de la lista guardada como otra unidad de la lista y sin la marca («puntos básicos», «por mil» o una fracción guardados como porcentaje; horas sin la marca): *contradicho* (C12); fuera de la lista, sin valor y sin la marca: *omitido* (C11); `sin unidad`: correcta si la norma no da unidad y el grafo la deja vacía (C13); la unidad que hereda una celda del rótulo de su tabla: correcta si el rótulo rige esa celda |
| **moneda** | unidad moneda | el código de la moneda que nombra la norma (ARS, USD, EUR); «$» se lee ARS (C14) | «pesos o su equivalente en otras monedas» → ARS; «euros» sin código: *omitido*; UVA es unidad, no moneda; la cláusula que no nombra moneda, o «moneda extranjera» sin decir cuál: opción «no nombra» (C14); una moneda llena donde no aplica (en un porcentaje) se anota y no mueve el núcleo (C14) |
| **tipo de días** | unidad días | lo que dice la cláusula de la cuantía («hábiles», «corridos»); vacío si no lo dice | una regla general del TO («los plazos se computan en días hábiles») no se le exige al campo (decisión D8): si la cláusula no lo dice y el grafo lo llena, es *espurio*, con la nota «regla general», y no mueve el núcleo (C20); hábiles por corridos: *contradicho* |
| **comparación** | todo elemento con contenido (los vacíos, §2.5) | el sentido que las definiciones del §0 dan a la letra de la cláusula (C1) | §2.4 |
| **base literal** | porcentaje y veces; los límites relativos del validador | identifica la magnitud sobre la que se aplica la cuantía, con los calificadores que cambian el monto, sin agregar texto que no es base | «10 % de la responsabilidad patrimonial computable del mes anterior»: sin «del mes anterior» es *parcial*; cortada en la coma o en la palabra 20 antes de terminar: *parcial*; un artículo inicial o una conjunción final de más no cuentan; otra magnitud: *contradicho*; vacía con base en la letra: *omitido*; llena sin base: *espurio*. El ancla temporal de un plazo no es base, corra hacia adelante («dentro de los 10 días de recibida la solicitud») o hacia atrás («con una antelación de 30 días a su vencimiento») (C17): límite del esquema (L-ESQ-R2 §1.3 (c) habla de umbrales relacionales) |
| **destino de la base** | elementos con `base_destino` | el punto, la sección, el TO o la Definicion donde la norma establece la magnitud de la base | «la suma establecida en el punto 4.2» → el punto 4.2 del mismo TO; una Definicion homónima con otro sentido: *contradicho*; opciones para lo que el formato de un solo punto no expresa: remisión genérica, sin punto ni término; destino múltiple; destino en otro TO (C18). Informativo, sin cifra: en los marcados `base_no_resuelta`, si la base nombra un punto que existe |

Una base *parcial* cuenta como incorrecta si con la base guardada se calcula otro monto, y como correcta si no.

**2.4 Comparación: la tabla de sentidos** (L-ESQ-R2 §1.3, puntos 2 y 3; enmiendas 3 y 5; calibración P3).

La comparación se lee por el sentido que le dan las definiciones del §0; si el §0 dice otra cosa que la tabla, manda el §0. La tabla
solo decide la clase de una omisión (C1). Antes de buscar una forma en la tabla, «del» se lee «de el» y «al», «a el» (C4).

| la letra de la cláusula | sentido |
|---|---|
| «superen», «exceda», «más de», «mayor(es) a», «superior a» | mínimo estricto |
| «igual o superior», «al menos», «por lo menos», «como mínimo», «un mínimo de», «no inferior a», «no menos de», «… o más» pospuesto | mínimo inclusivo |
| «inferior a», «menos de», «menor(es) a» | máximo estricto |
| «no podrá superar», «sin exceder», «no excedan, al momento de los acuerdos, del», «hasta», «como máximo», «dentro de», «igual o inferior», «máximo de» pegado a la cuantía | máximo inclusivo |
| «igual a», «equivalente a» pegados a la cuantía, sin otro comparativo en la cláusula | igual |
| «pondera», «ponderador», «coeficiente», «factor», sin un comparador pegado a la cuantía | coeficiente |
| sin marcador, también en un plazo (enmienda 3) | no_determinada |

**Formas fuera de la tabla, con su sentido** (C2, C3, C5). No entran a la tabla mientras el código medido no las implemente. Su omisión es
de la definición. Si el grupo 2 las lleva al código, entran a la tabla para el grafo medido con esa versión, y se declara.

| la letra de la cláusula | sentido |
|---|---|
| «no superior a», «no mayor a», «no más de», «no supere» y las negaciones parecidas | máximo inclusivo |
| «será de» | igual |
| «límite de» | máximo inclusivo |
| «un máximo … equivalente al» | máximo inclusivo |
| «antelación mínima de» | mínimo inclusivo |

- *Correcta*: el valor del grafo es el de la lectura. *Contradicha*: los dos fijan un sentido y no es el mismo, o el grafo fija uno y la
  letra no. «Mayor que» frente a «mayor o igual que» cuenta: estricto por inclusivo es *contradicha*, porque la distinción cambia la
  respuesta (L-ESQ-R2 §1.3, punto 2). *Omitida*: el grafo dice `no_determinada` y la letra fija un sentido.
- Cada *omitida* lleva una clase: **de implementación**, si la forma de la letra está en la tabla (el código no aplicó la definición), o
  **de la definición**, si no está (las formas fuera de la tabla, y los rangos).
- **Qué mención se califica** (C6): la que cubre el tramo del elemento, no cada mención de la cuantía en la unidad. Si el nodo representa
  una regla con varias menciones, el sentido es el de la mención del tramo, y la diferencia con las otras se anota.
- **Rangos** (C22): «entre X y Y» es un límite declarado de la definición (`plan:401`). Con `no_determinada`, la omisión es de la
  definición. Si el grafo lo parte en dos elementos, cada extremo se califica: el inferior como mínimo inclusivo y el superior como
  máximo inclusivo.
- Más casos límite: «no superarán el 1,25 % de los activos ponderados» es máximo inclusivo y no coeficiente (comparador pegado,
  enmienda 5, punto 2); «sea o no superior» no es una negación (enmienda 5); «hasta el 31 de diciembre» no tiene cuantía.

**2.5 Veredictos del elemento.** En los veredictos, «correctos» se lee «correctos o no aplica» (C21).
- **Núcleo correcto** (la cifra de la afirmación, §8): pertinente, y correctos el valor, la unidad, la moneda si aplica, la comparación y
  la base literal si la letra tiene base o el campo está lleno. Una comparación *omitida*, de cualquier clase, no es correcta: el grafo
  no dice el sentido.
- **Completo correcto**: el núcleo, más el tipo de días si aplica y el destino si está guardado. La exactitud del destino se informa además
  aparte (C19).
- **Núcleo contra la definición** (diagnóstico, para el §10): igual al núcleo, pero la comparación *omitida de la definición* cuenta como
  correcta. La diferencia entre las dos cifras es lo que el esquema no expresa, no un error del código.
- **Un campo no decidible** deja al elemento no decidible solo si los demás campos del veredicto están bien. Si otro campo está mal, el
  elemento es incorrecto (C30).
- **Elementos vacíos.** Un elemento sin valor, sin base y con la comparación `no_determinada` no afirma ningún monto: no tiene campos que
  puedan estar bien o mal. En el grafo sin cola de la tanda 0 son 305 de 1.306, todos del validador (`vacios_y_resueltas_salida_UMEDUMBRALES.txt`).
  Quedan fuera del núcleo y del completo, que se calculan sobre los elementos con contenido, y se leen aparte con una sola pregunta, en
  tres clases: *oculta un umbral* (la letra fija una cuantía, un sentido o una base que el elemento no guarda: campos omitidos), *límite
  sin cuantía en la letra* (la norma nombra un límite y no lo cuantifica, por ejemplo porque lo delega) o *no es un umbral*. Contarlos
  como correctos inflaría la cifra; contarlos como errores de monto mezclaría dos preguntas.
- **Un elemento no pertinente** (C10): con cuantía en la norma, sus campos describen la cuantía tal como la norma la enuncia, y el motivo va
  en la nota; *inexistente*: las opciones nulas.

---
## 5. Lectura (cambios al §5 de la enmienda que la v1 necesita)

- **Paso 1** (C23): la ficha no muestra ningún campo del grafo, ni etiqueta, ni descripción, ni tramos, ni el id del elemento.
  - Se resalta solo la cuantía, ubicada con el tramo del elemento; no se muestra la extensión del tramo (C24).
  - El paso 1 califica los campos de la cuantía resaltada, sin la pertinencia.
- **Paso 2:**
  - **la pertinencia se decide primero** (C7), viendo solo la etiqueta, el tramo y los otros elementos del nodo, y antes de ver los
    valores del grafo para los demás campos;
  - después, el comparador devuelve las diferencias de los demás campos, con el valor del grafo a la vista (§5.3).
- **Los formularios** de los dos pasos tienen columna de nota (C26). Las fichas llevan un id opaco derivado de una semilla, con el mapa
  sellado aparte y reproducible (C25).
- **Dos elementos de la misma unidad de E0** (C27). Si el sorteo da dos elementos de la misma unidad, no se vuelve a sortear. La segunda
  ficha se declara y se lee sabiendo que la primera la informa.
- **Los ejemplos de esta regla** no salen de la muestra del piloto ni de T (C28). Los ejemplos resueltos con cuantía, base o moneda se
  cruzaron contra el texto de E0 de los elementos de la muestra, y se cambiaron los que hacía falta. También se cambiaron otros que no
  aparecen en ella, para que los cambios no digan nada de la muestra.

---
## Cambios sobre la v0

Aprobados tal como estaban en el borrador: C1, C4, C6, C8, C9, C10, C11, C13 a C18, C20, C21, C23, C25, C26 y C28. Modificados por la
autora: C2, C3 y C5 (formas fuera de la tabla), C7 (la pertinencia primero, en el paso 2), C12, C19, C22, C24 y C27. Nuevos: C29 (la
versión de E0 de la referencia) y C30 (un campo no decidible y otro incorrecto).

- **C1.** La comparación por el sentido del §0; la tabla decide la clase de una omisión.
- **C2, C3 y C5.** Negaciones, «será de», «límite de», «un máximo … equivalente al» y «antelación mínima de»: fuera de la tabla, con su
  sentido; su omisión es de la definición.
- **C4.** Contracciones «del» y «al».
- **C6.** Qué mención se califica.
- **C7.** La pertinencia, primero, en el paso 2.
- **C8.** Duplicado.
- **C9.** Monto fijo pertinente; la regla del nodo por la etiqueta y el tramo.
- **C10.** Campos de un elemento no pertinente (D-L1-1 bis).
- **C11.** La marca `fuera_de_lista` es general.
- **C12.** Una unidad fuera de la lista guardada como otra de la lista y sin la marca: contradicha, sin clase de límite del esquema.
  Corrige la lectura provisional L4.
- **C13.** `sin unidad` y `otra: <cuál>`.
- **C14.** Moneda: «$», moneda donde no aplica, «no nombra».
- **C15.** Valor en letras.
- **C16.** Nota obligatoria en la base parcial.
- **C17.** El ancla temporal no es base, hacia adelante o hacia atrás.
- **C18.** Opciones de destino.
- **C19.** El destino sigue en el completo, como en la v0, y su exactitud se informa además aparte.
- **C20.** Tipo de días por regla general: espurio con nota, sin mover el núcleo.
- **C21.** «Correctos o no aplica».
- **C22.** Rangos.
- **C23.** Ficha sin campos del grafo.
- **C24.** Se resalta solo la cuantía, ubicada con el tramo.
- **C25.** Ids opacos de una semilla.
- **C26.** Columna de nota.
- **C27.** Dos elementos de la misma unidad: no se vuelve a sortear.
- **C28.** Ejemplos fuera de la muestra del piloto y de T. Cambian cinco ejemplos resueltos de la v0, entre ellos la base del caso de
  control de L-ESQ-R2 (se ven comparando con la v0).
- **C29.** La referencia, en la versión de E0 del grafo medido.
- **C30.** Un campo no decidible deja al elemento no decidible solo si los demás campos del veredicto están bien.
