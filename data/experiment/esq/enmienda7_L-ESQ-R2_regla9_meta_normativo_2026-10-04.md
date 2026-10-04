# Enmienda 7 a L-ESQ-R2 — la regla 9: el alcance y los regímenes de transición no son meta-normativos

**BORRADOR — PENDIENTE DE FIRMA** · Redactada: 2026-10-04.

Enmienda con fecha a L-ESQ-R2 (`data/experiment/esq/enmienda_L-ESQ-R2_2026-09-30.md`, FIRMADA en `4ef7650`;
sha256 del texto firmado `66c4a1b9…`). L-ESQ-R2 no se edita: esta enmienda vive al lado y se lee junto con
ella, con sus notas posteriores a la firma y con las enmiendas 2 (`5f9a731`), 3 (`8d01b04`), 4 (`5c58f38`) y
5 (`3a4b980`). La enmienda 6 está en BORRADOR. Por la regla k de CLAUDE.md §4, toda cita de L-ESQ-R2 es del
texto firmado (`git show 4ef7650:data/experiment/esq/enmienda_L-ESQ-R2_2026-09-30.md`), con su línea.

No rige hasta la firma. La autora la firma antes del commit de P3c-2 de U-PROMPT-R2, la etapa que re-congela
el prefijo con este cambio.

---

## 0. Qué enmienda y por qué

**Lo que dicen los textos firmados.**

- **El laudo de esquema congelado,** R4 (`data/experiment/esq/laudo_esquema_congelado.md:50-57`, `2593d4d`):
  la regla 9 de omisión de contenido meta-normativo «SE ACEPTA con los residuos declarados, sin tocar más la
  regla». Declara dos residuos: una cláusula interpretativa que el extractor tipa igual, en 2 de 2 corridas, y
  la «sobre-omisión de transitorias» de `traval::S5`, que llama «la limitación de diseño declarada».
- **L-ESQ-R2,** §5.1 (`:687-688`): el contenido meta-normativo es «finalidad, vigencia, interpretación y
  alcance de una norma». §5.2, P-e1 (`:705-706`): la regla 9 pasa de «no se extrae» a «no se extrae y se
  registra con su tramo». §5.3 (`:725-726`): una muestra de control de `meta_normativo`, para vigilar el
  contenido habilitante que la regla no debe excluir.

**Lo que se encontró.** En el brazo nuevo de la pareada de P4 de U-PROMPT-R2 hay 24 omisiones
`meta_normativo`, una por ficha. Nueve son contenido normativo: deberes, condiciones, excepciones, alcances y
modalidades (`data/experiment/prompt_r2/p4/lectura_p4.md`, sección «Revisión de la autora», `2ed47a0`). Una
es la frase que define el alcance de la cartera comercial en `cla::5.1.1::intro`, el ejemplo de la tesis: con
ella declarada como omisión, la exclusión de los créditos para consumo o vivienda no queda en ningún nodo.

**Por qué una enmienda.** Cambia qué cuenta como meta-normativo: una regla que el laudo dejó cerrada y que
L-ESQ-R2 describe.

## 1. Qué decide

1. **Qué queda como meta-normativo.**
   - Lo que predica sobre el significado de un acto o de una norma: las cláusulas interpretativas.
   - Las declaraciones de objetivo o de finalidad de una norma.
   - La fecha desde la que una norma entra en vigencia.
2. **Qué deja de serlo.**
   - El alcance: a quién o a qué se aplica una norma, qué abarca una clase o qué deja afuera.
   - Las reglas de aplicabilidad temporal y los regímenes de transición con condiciones. De una frase de
     vigencia, solo la fecha es meta-normativa.
   - En general, un tramo que dice un deber, una prohibición, una facultad, una condición, una excepción, un
     alcance o una modalidad nunca es meta-normativo.
3. **Adónde va lo que deja de serlo.**
   - Lo que abarca o excluye una clase que el texto nombra es una Definicion de esa clase.
   - El alcance de una norma va en esa norma: en su descripción, su `aplica_a`, su Condicion o su Excepcion.
   - Si ningún tipo lo representa, se registra como `fuera_de_tipos`, nunca como `meta_normativo`.
4. **Finalidad o alcance.** Si quitar la frase hace que la norma valga para más casos, es alcance. Si no
   cambia a qué se aplica, es finalidad.
5. **El encabezado puro de una lista.** El deber, la modalidad, el cuantificador o la condición que un
   encabezado fija para cada ítem se extraen en cada ítem. En la unidad del encabezado no se extraen ni se
   registran como omisión.
6. **La Definicion.** La delimitación de R3 del laudo (`laudo_esquema_congelado.md:42-46`) se precisa: no
   vuelve definitoria a una unidad delimitar el alcance de una norma; lo que una clase abarca o deja afuera
   sí la define. Es lo que R3 ya había adjudicado: «el cuerpo que da la extensión define».

## 2. Qué dice sobre el laudo de esquema congelado

- El laudo no se edita. Esta enmienda cambia, para la release r2, el contenido de la regla 9 que R4 aceptó
  «sin tocar más la regla».
- La sobre-omisión de transitorias deja de ser una limitación de diseño declarada: un régimen de transición
  con condiciones pasa a extraerse, y lo que se omita se mide.
- El otro residuo de R4 no cambia: la cláusula interpretativa sigue siendo meta-normativa, y que el extractor
  la tipe sigue siendo un modo de falla suyo.
- La justificación de la regla tampoco cambia: tipar lo que solo interpreta fabrica deberes que la norma no
  enuncia. Lo que cambia es el borde: el alcance y las condiciones de una transición no interpretan; dicen a
  qué y cuándo se aplica la norma.

## 3. Efectos declarados

- **El texto** es el de los reemplazos P3C-a1 a P3C-a6 del prefijo de P3c
  (`data/experiment/prompt_r2/p3c/salida/lado_a_lado_p3c.md`, `438bbd5`) y la NOTA de E3 de las omisiones de
  esquema. Los implementa P3c-2 de U-PROMPT-R2.
- **Reprocesamiento.** Cambia el prefijo de E1: todas las unidades pagan E1 y E3. Lo absorbe U-REEXT-T0, que
  corre con el prefijo nuevo.
- **Cómo se mide.**
  - En P4b de U-PROMPT-R2: casos no leídos al escribir el ajuste, con un régimen de transición entre ellos.
  - En U-REEXT-T0: el contador de omisiones `meta_normativo` cuyo tramo trae una marca de deber, de facultad,
    de condición o de excepción.
  - La muestra de control de `meta_normativo` del §5.3 sigue en pie.

## 4. Qué no cambia

- El texto de L-ESQ-R2, sus notas y sus enmiendas 2 a 5.
- El registro de la omisión con su categoría y su tramo, y las cinco categorías.
- El contenido habilitante sigue extrayéndose como Potestad.
- El tool schema y los tipos del esquema: esta enmienda no agrega ni quita ninguno.

## Firma

BORRADOR — PENDIENTE DE FIRMA de la autora.
