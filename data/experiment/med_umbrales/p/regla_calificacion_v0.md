# Regla de calificación v0 (U-MED-UMBRALES, etapa P)

Es el §2 de la enmienda 1 al pre-registro de tripletas, FIRMADA en `a0f9815` (`docs/enmienda1_preregistro_evaluacion_tripletas_2026-10-08_umbrales.md`, líneas 47 a 105 del archivo de ese commit), sin cambios. sha256 del texto copiado (desde «## 2. Unidad y campos» hasta la línea anterior a «## 3.», con salto final): `3b386f99ee423a234de6af8a9c0e7da367ac729360073f4731f414e9fc3a35c7`.

El piloto la ajusta en el FRENO del lote 1 (v1) y la sella al cerrar el piloto (§5.4); esta versión no se edita: las versiones siguientes van en archivos aparte.

---
## 2. Unidad y campos

**2.1 Unidad.** El elemento de umbral, no el nodo: un nodo puede tener varios (1.306 elementos en 1.123 nodos en el grafo sin cola de la
tanda 0, `estratos_umbrales_salida_UMEDUMBRALES.txt`).

**2.2 Referencia.** El texto de la unidad de E0 del nodo, propio y heredado, y la página del PDF si el texto de E0 es dudoso. Nunca la
descripción del nodo ni otra salida de un modelo.

**2.3 Resultado por campo.** *Correcto*; *contradicho* (el grafo dice otra cosa); *omitido* (la letra lo fija y el campo está vacío o
`no_determinada`); *espurio* (el campo está lleno y la letra no lo fija); *parcial* (solo la base); *no aplica*; *no decidible* (necesita
un experto, o el texto o la tabla no se leen), que se reporta aparte con sus dos cotas.

| campo | aplica a | correcto si | casos límite |
|---|---|---|---|
| **pertinencia** (precondición) | todo elemento | la cuantía (en los del validador, el límite relativo) está en el texto de la unidad y fija un umbral, plazo, porcentaje o coeficiente de la regla que representa el nodo | *no pertinente*: el número de una norma citada, una fecha, el número de un punto, un ejemplo, o la cuantía de otra regla del mismo párrafo; *inexistente*: la cuantía no está en la norma (sale de la descripción); *duplicado*: un segundo elemento de la misma cuantía en el mismo nodo |
| **valor** | elementos con cuantía; en los del validador, que la cláusula no traiga cuantía | numéricamente igual a la cuantía, normalizada | «1,25 %» → 1.25; «$ 5.000 millones» → 5000000000; «dos veces» → 2; «180 (ciento ochenta) días» → 180; «el quinto día hábil» después de «hasta el» → 5; *contradicho*: otro número, otro multiplicador, un compuesto partido («treinta y cinco» leído como 5); *omitido*: un elemento del validador sin valor cuando la cláusula trae cuantía |
| **unidad** | ídem | la de la norma en la lista cerrada (porcentaje, moneda, días, meses, años, veces, UVA); horas y semanas, con la marca `fuera_de_lista` | «puntos básicos», «por mil» o una fracción guardados como porcentaje: *contradicho*; horas sin la marca: *contradicho*; la unidad que hereda una celda del rótulo de su tabla: correcta si el rótulo rige esa celda |
| **moneda** | unidad moneda | el código de la moneda que nombra la norma (ARS, USD, EUR) | «pesos o su equivalente en otras monedas» → ARS; «dólares estadounidenses» sin código: *omitido*; UVA es unidad, no moneda |
| **tipo de días** | unidad días | lo que dice la cláusula de la cuantía («hábiles», «corridos»); vacío si no lo dice | una regla general del TO («los plazos se computan en días hábiles») no se le exige al campo (decisión D8): se registra como dato informativo; hábiles por corridos: *contradicho* |
| **comparación** | todo elemento con contenido (los vacíos, §2.5) | el sentido que las definiciones del §0 dan a la letra de la cláusula | tabla del §2.4 |
| **base literal** | porcentaje y veces; los límites relativos del validador | identifica la magnitud sobre la que se aplica la cuantía, con los calificadores que cambian el monto, sin agregar texto que no es base | «10 % de la responsabilidad patrimonial computable del mes anterior»: sin «del mes anterior» es *parcial*; cortada en la coma o en la palabra 20 antes de terminar: *parcial*; un artículo inicial o una conjunción final de más no cuentan; otra magnitud: *contradicho*; vacía con base en la letra: *omitido*; llena sin base: *espurio*. El inicio de un plazo («dentro de los 10 días de recibida la solicitud») no es base: límite del esquema (L-ESQ-R2 §1.3 (c) habla de umbrales relacionales) |
| **destino de la base** | elementos con `base_destino` | el punto, la sección, el TO o la Definicion donde la norma establece la magnitud de la base | «importe de referencia establecido en el punto 3.7» → `cla::3.7` (caso de control de L-ESQ-R2, `4ef7650:…:303-306`); una Definicion homónima con otro sentido: *contradicho*. Informativo, sin cifra: en los marcados `base_no_resuelta`, si la base nombra un punto que existe |

Una base *parcial* cuenta como incorrecta si con la base guardada se calcula otro monto, y como correcta si no.

**2.4 Comparación: la tabla de sentidos** (L-ESQ-R2 §1.3, puntos 2 y 3; enmiendas 3 y 5; calibración P3).

| la letra de la cláusula | sentido |
|---|---|
| «superen», «exceda», «más de», «mayor(es) a», «superior a» | mínimo estricto |
| «igual o superior», «al menos», «por lo menos», «como mínimo», «un mínimo de», «no inferior a», «no menos de», «… o más» pospuesto | mínimo inclusivo |
| «inferior a», «menos de», «menor(es) a» | máximo estricto |
| «no podrá superar», «sin exceder», «no excedan, al momento de los acuerdos, del», «hasta», «como máximo», «dentro de», «igual o inferior», «máximo de» pegado a la cuantía | máximo inclusivo |
| «igual a», «equivalente a» pegados a la cuantía, sin otro comparativo en la cláusula | igual |
| «pondera», «ponderador», «coeficiente», «factor», sin un comparador pegado a la cuantía | coeficiente |
| sin marcador, también en un plazo (enmienda 3) | no_determinada |

- *Correcta*: el valor del grafo es el de la lectura. *Contradicha*: los dos fijan un sentido y no es el mismo, o el grafo fija uno y la
  letra no. «Mayor que» frente a «mayor o igual que» cuenta: estricto por inclusivo es *contradicha*, porque la distinción cambia la
  respuesta (L-ESQ-R2 §1.3, punto 2). *Omitida*: el grafo dice `no_determinada` y la letra fija un sentido.
- Cada *omitida* lleva una clase: **de implementación**, si la forma de la letra está en la tabla (el código no aplicó la definición), o
  **de la definición**, si no está («entre 30 días y 90 días», límite declarado en `plan:401`; «será de»; «límite de»).
- Más casos límite: «no superarán el 1,25 % de los activos ponderados» es máximo inclusivo y no coeficiente (comparador pegado,
  enmienda 5, punto 2); «sea o no superior» no es una negación (enmienda 5); «hasta el 31 de diciembre» no tiene cuantía.

**2.5 Veredictos del elemento.**
- **Núcleo correcto** (la cifra de la afirmación, §8): pertinente, y correctos el valor, la unidad, la moneda si aplica, la comparación y
  la base literal si la letra tiene base o el campo está lleno. Una comparación *omitida*, de cualquier clase, no es correcta: el grafo
  no dice el sentido.
- **Completo correcto**: el núcleo, más el tipo de días si aplica y el destino si está guardado.
- **Núcleo contra la definición** (diagnóstico, para el §10): igual al núcleo, pero la comparación *omitida de la definición* cuenta como
  correcta. La diferencia entre las dos cifras es lo que el esquema no expresa, no un error del código.
- **Elementos vacíos.** Un elemento sin valor, sin base y con la comparación `no_determinada` no afirma ningún monto: no tiene campos que
  puedan estar bien o mal. En el grafo sin cola de la tanda 0 son 305 de 1.306, todos del validador (`vacios_y_resueltas_salida_UMEDUMBRALES.txt`).
  Quedan fuera del núcleo y del completo, que se calculan sobre los elementos con contenido, y se leen aparte con una sola pregunta, en
  tres clases: *oculta un umbral* (la letra fija una cuantía, un sentido o una base que el elemento no guarda: campos omitidos), *límite
  sin cuantía en la letra* (la norma nombra un límite y no lo cuantifica, por ejemplo porque lo delega) o *no es un umbral*. Contarlos
  como correctos inflaría la cifra; contarlos como errores de monto mezclaría dos preguntas.
