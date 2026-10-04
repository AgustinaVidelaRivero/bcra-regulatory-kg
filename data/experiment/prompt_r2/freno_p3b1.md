# U-PROMPT-R2 — FRENO P3b-1 (diseño)

04/10/2026. HEAD `8d01b04` al empezar y `0b98045` al cerrar; ese commit, de otras unidades, no toca este mandato ni la
cadena. USD 0, sin API y sin commit. Nada congelado ni implementado. El detalle, con sus anclas,
está en `p3b/diseno_p3b.md`.

**Fuentes.** Leí completas las notas de P3b al pie del mandato (`4f3bcff` y `8d01b04`).
- **Diferencia con el «seguí».** P3 está commiteada en `4aa92c7`, no en `8d01b04`. Ese hash es el de las enmiendas
  firmadas (protocolo y cola humana), que traen la última nota del mandato. Mandan los archivos.

## 1. El texto nuevo

**Prefijo:** 12 reemplazos con ancla única sobre el congelado (`14d6b63b508e`), reversibles byte a byte.
- **Tamaño:** de 51.780 a 55.105 caracteres.
- **Hash canónico del borrador:** `3817de475c93`; el tool schema no cambia (`0c391f2b…`).
- **Lado a lado:** en `p3b/salida/lado_a_lado_p3b.md`.

| Punto (hallazgo) | Qué agrega |
|---|---|
| a, recomendación (1.3) | Obligacion, con el tramo que la califica en `otras_propiedades.modalidad` y la descripción que dice que es recomendación |
| b, consecuencia de un incumplimiento (1.4) | Obligacion o Potestad de quien la aplica; si el texto no lo nombra, omisión `fuera_de_tipos`; nunca Restriccion; `otras_propiedades.consecuencia` |
| c, Excepcion (2.8) | Se conecta si la norma que exceptúa está en la unidad; si no, va sin relación |
| d, predicados (3.2) | `regula`, `condiciona` y `requiere` definidos (definiciones operativas del esquema v2, `docs/esquema_v2_diseño.md` §2.1); `regula` desde Restriccion: la tabla lo admite y la regla lo descarta, sin tocar la matriz |
| e, lista dentro de la unidad (1.18) | La composición vale también ahí |
| f, listas de excepciones (U-DIAG-VINCULO) | Cada ítem es una Excepcion compuesta, sin `exceptua` cuando la norma está en otra unidad |

**Mensaje de E1.**
- **g:** un ítem es el que tiene el bloque con «:» seguido solo de cierres. Pasa de 706 a 1.053 ítems: los 347 de
  la revisión, con `cap::8.5.1` a `8.5.3`, y sin perder ninguno. Da lo mismo con el recorte de herencia de C2.
- **h:** 121 de 376 mini-chunks empiezan a mitad de oración. El mensaje avisa que la última línea de títulos es
  parte de la oración. Su par en el código verifica el tramo en orden de lectura: un tramo de prueba que cruza del
  título al cuerpo verifica hoy en 5 de los 121 y así en los 121.
- **Total:** cambian 1.174 mensajes.

**NOTA de E3 (i).** Una omisión declarada `meta_normativo`, `fuera_de_tipos` o `relacion_sin_predicado` no es un
faltante, salvo que lo declarado no sea lo que dice su categoría.

**No-filtración.**
- **Población:** 5.376 chunks, de la E0 legada y la e0-r2 de los diez TOs y de los cuatro fuera de muestra.
- **Resultado:** 0 choques de las 610 ventanas de 5 palabras que agrega el prefijo y de las 230 de los literales
  nuevos.
- **Casos de control:** 0 bigramas o trigramas de los 37 casos.

## 2. Quién decide

| Forma | Puntos |
|---|---|
| El modelo copia el marcador y el código clasifica | a; b también copia el marcador, pero quién aplica la consecuencia lo decide el modelo |
| Decide el modelo | c, d, e y f, porque es lectura de la oración. En e y f el código verifica el tramo de dos segmentos |
| Decide el código | g, h, i y l, y k en la comparación y la marca |

j depende de la opción (§3). La razón de cada uno está en el diseño, §3.

## 3. j: veredictos de E3 como texto (25 unidades de la cola)

En las 25, el texto trae el veredicto entero: 24 se leen con `json.loads` y `cap::5.3.2.5`, solo con reparo.

| | Salen de la cola | Van a un reintento | Quedan |
|---|---|---|---|
| Opción 1, leer en código con reparo (USD 0) | 20: 5 `completo_ok_directo`, 11 `aceptado_con_residuales`, 4 `aceptado_tras_reintento` | 4 | 1 (`ric::5.1.3.2`, alto sin cita verificada) |
| Opción 1, estricta | 19 | 4 | 2 (más `cap::5.3.2.5`, sin leer) |
| Opción 2, volver a pedir a E3 | lo mismo si E3 repite el contenido, sin certeza | | |

- **Costo de la opción 2:** unos USD 0,19 por las 25 llamadas, y unos 0,25 con los 4 reintentos. Puede volver a
  fallar: la falla fue de 25 en 2.681 llamadas.
- **Recomiendo la opción 1 con reparo,** con la marca de cómo se leyó.

## 4. k: reintento que reemplaza sin comparar y copia de la nota de E3

**Pérdidas.** De 220 unidades aceptadas tras el reintento, 18 tienen menos entidades, 27 menos relaciones y 12
menos de las dos: 33 con pérdida.

| Opción | Efecto |
|---|---|
| k1, hoy | 33 pérdidas aceptadas sin marca |
| k2, a la cola | entran 33 a la cola |
| k3, unión | sin regla de identidad: con etiqueta o descripción quedan 472 entidades sin par |
| k4, marca y muestra de la tanda | 33 marcadas; la cola no cambia |

Ninguna saca unidades de la cola. **Recomiendo k4.**

**Copia de la nota de E3.** La regla, fijada antes de contar: R-NORM y ventana de 5 tokens que estén en la nota y no
en la unidad ni en sus citas. Da 45 casos en 40 de las 220 unidades, `cla::6.3.3` incluida, listados en
`salida/copia_nota_casos.md`. No los clasifiqué por lectura.

**Dos defensas, solo con la forma «r2».**
1. Una frase en el mensaje del reintento: la nota no es texto de la norma y no se copia. Pasó la no-filtración.
2. Un control en el ratchet que marca, sin rechazar, las entidades con texto de la nota ausente de la unidad. En la
   tanda 0 habría marcado los 45 casos. La marca queda en los registros de la corrida, porque `runner_corpus.py` no
   está en las escrituras.

## 5. l, la modalidad, y lo que P3b-2 implementa sin opciones

**l.** `derivar_comunicacion`, con la forma r2, lee el tramo verificado: una Comunicación nombrada da su letra (con
enumeraciones); una norma externa, «externa»; si no hay sustento, no se deriva.
- **En los 22 nodos de r2a, con el texto de la unidad:** `A-39` (artículo de la Ley 21.526) pasa a «externa», las
  11 Comunicaciones reales siguen en «A» y los 7 que no son normas quedan sin derivar.
- **Con la etiqueta, en cambio, nada cambia:** la etiqueta la escribió el modelo.

**La modalidad.**
- **El agente:** la ve en la descripción, que está en `properties`.
- **El código:** la clasifica en `properties_no_definidas.modalidad_clasificada`.
- **La exportación** de esa clave al agente toca U-NAV-DISENO: su requisito de las vistas ya pide las claves fuera
  de `properties` (`UNAV_DISENO_navegacion_agente.md:117-121`). Propongo nombrar ahí la modalidad, con una nota que
  escribe la autora.

**P3b-2 implementa además:**
- `e2_lib.py`, solo en el camino r2: las `properties_no_definidas` de la relación pasan a la arista; los cinco
  ensamblados sellados se reproducen;
- el `todo` de `cola_humana.jsonl` (`ratchet_e3.py:351-355`), solo con la forma r2;
- el prefijo re-congelado, con sus candados;
- el costo de la pareada y de U-REEXT-T0.
No corre a la vez que la implementación de C2, y antes de implementar miro `git status` y `git log`.

## 6. Controles

- **Corridas:** los cinco scripts de `p3b/` corrieron dos veces sobre una copia sin enlaces. Los 11 archivos de
  salida dan lo mismo en las dos corridas y son iguales a los de `p3b/salida/`.
- **El repo** no cambió durante el control: los 12.698 archivos con el mismo sha256 antes y después.
- **`.pyc`:** sin nuevos.

## 7. Pendiente de la autora

- Aprobar el texto (prefijo, mensaje, NOTA y aviso del reintento).
- Decidir j y k.
- La nota a U-NAV-DISENO sobre la modalidad.
- El commit de P3b-1.
