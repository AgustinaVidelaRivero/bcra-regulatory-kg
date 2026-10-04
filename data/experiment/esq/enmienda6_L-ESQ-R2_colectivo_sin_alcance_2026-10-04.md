# Enmienda 6 a L-ESQ-R2 — en un documento sin alcance, la sugerencia del modelo no gana ni para una expresión colectiva ni para una relación sin mención

**BORRADOR — PENDIENTE DE FIRMA** · Redactada: 2026-10-04.

Enmienda con fecha a L-ESQ-R2 (`data/experiment/esq/enmienda_L-ESQ-R2_2026-09-30.md`, FIRMADA en `4ef7650`;
sha256 del texto firmado `66c4a1b9…`). L-ESQ-R2 no se edita: esta enmienda vive al lado y se lee junto con
ella, con sus notas posteriores a la firma y con las enmiendas 2 (`5f9a731`), 3 (`8d01b04`), 4 (`5c58f38`) y
5 (`3a4b980`). Por la regla k de CLAUDE.md §4, toda cita de L-ESQ-R2 es del texto firmado
(`git show 4ef7650:data/experiment/esq/enmienda_L-ESQ-R2_2026-09-30.md`), con su línea.

No rige hasta la firma. La medición del §2 está PENDIENTE: la hace R2 de U-RERESOL-CAT sobre el crudo de
U-REEXT-T0, y la autora firma con esa medición a la vista, antes de que R2 implemente las dos reglas.

Versiones del borrador: la primera, con la regla del colectivo, quedó en `28ec100`. Esta suma la regla de la
relación sin mención (decisión de la autora del 04/10/2026).

---

## 0. Qué enmienda y por qué

**Lo que dice L-ESQ-R2.**

- §3.2, resolución por relación (`:565-570`): R1, label o alias exacto; R2, slug, singular y alias entre
  paréntesis; «R3: expresión colectiva → sujeto por defecto del TO»; «R4: sugerencia del modelo»; y lo
  ambiguo o sin resolver, al registro.
- §3.3, punto 5 (`:580-582`): «la regla textual gana solo con coincidencia exacta de label o alias (R1). Con
  las reglas aproximadas (R2 y R3) gana la sugerencia del modelo».
- Decisión del 30/09 (`:593-594`): la lista de expresiones colectivas de R3 es «una lista inicial cerrada,
  tomada de la redacción del propio prompt», «que se amplía en código con las menciones de r2b».

**Lo que hace el código** (`data/experiment/reextraccion_v2/corpus_v2/r1_e4.py`, en `9f6361e`).

- La lista es `("entidades", "sujetos obligados")`, comparada sin el artículo inicial (`:306`).
- Si la mención verificada es una expresión de la lista y el documento tiene alcance, R3 devuelve su rol. Si
  no lo tiene, devuelve el motivo `colectivo_sin_sujeto_por_defecto` (`:377`).
- Si la relación no trae mención, no se aplica ninguna regla textual y el motivo es `sin_mencion`.
- En la decisión, después de R1 gana la sugerencia del modelo si la hay (`:418`). En un documento sin alcance,
  entonces, «las entidades» y las relaciones sin mención quedan resueltas al id que sugirió el modelo, que no
  vio ninguna línea de alcance.

**Lo que se encontró.**

- De los 157 documentos, 86 no tienen alcance (`docs/plan_tesis.md:404`). En la tanda 0 es uno solo, docvig.
- En KG-Tanda0-Diez-r2a, docvig tiene 20 relaciones con sujeto: 17 resueltas por la sugerencia del modelo y 3
  en cuarentena. Las 17 no traen mención. Sus sugerencias van a seis ids distintos:
  `Sujeto_entidad_financiera` (7), `Sujeto_cliente` (3), `Sujeto_rol_alcance_lavdin` (3), que es el rol de
  alcance de otro documento, `Sujeto_sujeto_regulado` (2), `Sujeto_empresa_no_financiera_emisora_de_tarjetas`
  (1) y `Sujeto_entidad_cambiaria` (1) (`data/experiment/reresolucion_catalogo/salidas/r1_medicion.json`,
  clave `docvig`, `c98093a`).
- docvig no declara su alcance en ningún pasaje. Su índice tiene cuatro secciones y ninguna es de alcance.
  Nombra tres clases en lugares distintos: «las casas operativas de las entidades financieras» (puntos 1.2.3,
  2.1.3 y 2.2.3), «Recaudos especiales de las entidades financieras y cambiarias» (título del punto 3.6) y
  «las empresas no financieras emisoras de tarjetas de crédito y/o compra» (sección 4). En los puntos 3.4 y
  3.5 dice «las entidades», cuatro veces, sin decir cuáles. Queda sin alcance en U-REEXT-T0 (decisión de la
  autora del 04/10/2026).

**Por qué una enmienda.** Cambia una regla de un texto firmado: el orden del §3.2 y el punto 5 del §3.3.

## 1. Qué decide

El principio: en un documento sin alcance, la sugerencia del modelo no reemplaza a un sujeto que el texto no
identifica.

1. **Expresión colectiva.** Cuando el documento no tiene alcance y la mención verificada de la relación es
   una expresión colectiva de la lista de R3, la sugerencia del modelo no se aplica. La relación va a
   cuarentena, con el motivo `colectivo_sin_sujeto_por_defecto`.
2. **Relación sin mención.** Cuando el documento no tiene alcance y la relación no trae mención, la
   sugerencia del modelo tampoco se aplica. La relación va a cuarentena, con el motivo `sin_mencion`.
3. **El registro.** En los dos casos, la fila guarda la sugerencia (`sujeto_id_modelo`).
4. **El orden.** R1 sigue primero: un label o un alias exacto gana también en un documento sin alcance. Las
   dos reglas van después de R1 y antes de R4.
5. **Cuando el documento recibe alcance,** en el catálogo de resolución o en una release, las filas de la
   regla 1 se resuelven por R3 con `reresolver_registro`, sin volver a extraer.
6. **Restricción para el crecimiento del catálogo.** Ningún label ni alias puede ser igual a una expresión
   colectiva de la lista, porque R1 se evalúa antes y le ganaría a la regla. Hoy no hay ninguno.
7. **En los documentos con alcance no cambia nada.** R3 y R4 siguen como dice el punto 5 del §3.3.

## 2. La medición (PENDIENTE)

**La lista de expresiones colectivas** de la regla 1 deja afuera el singular.

- **Por texto** (aproximación sobre el texto propio de la E0 de los diez TOs; no son menciones de E1): la
  lista cubre 231 de 1.088 apariciones de una forma colectiva. Fuera quedan «la entidad» (806), «el sujeto
  obligado» (33), «cada entidad» (10) y otras cinco formas (8). No cuenta las formas seguidas de
  «financiera(s)» o «cambiaria(s)», que nombran una clase (`r1_medicion.json`, clave `colectivos`).
- **Una primera mirada con menciones reales** (brazo nuevo de la pareada de P4 de U-PROMPT-R2, 76 fichas, con
  el prefijo de P3b-2; no es la medición): de 123 menciones de sujeto, 45 son «las entidades», 31 de ellas
  verificadas, y 14 son «la entidad», las 14 verificadas
  (`data/experiment/prompt_r2/p4/salida/analisis_p4.json`, `2ed47a0`).

**Las relaciones sin mención** dependen del prefijo. El ajuste de P3c de U-PROMPT-R2 le pide al modelo que no
emita la relación cuando ni la unidad ni el texto heredado nombran al sujeto. Con ese prefijo, la regla 2
actúa solo sobre las relaciones sin mención que el modelo emita igual.

**Medición que falta, sobre el crudo de U-REEXT-T0** (la hace R2 de U-RERESOL-CAT), en los documentos sin
alcance:

| Qué se mide | Relaciones que pasan de la sugerencia del modelo a cuarentena | Ids que sugería el modelo |
|---|---|---|
| Regla 1, con la lista de hoy | PENDIENTE | PENDIENTE |
| Regla 1, con el singular y con «cada», «esta(s)», «dicha(s)» y «tal(es)» | PENDIENTE | PENDIENTE |
| Regla 2, relaciones sin mención | PENDIENTE | PENDIENTE |
| Aparte: relaciones con una mención que no verifica | PENDIENTE | PENDIENTE |

Y, en los documentos con alcance: en cuántas relaciones cambia el resultado de R3 o la marca de desacuerdo si
la lista se amplía. Ampliar la lista de R3 cambia R3 también ahí.

Con esas cifras la autora decide, al firmar, si la lista de la regla 1 incluye el singular y si es la misma
que la de R3.

## 3. Efectos declarados

- **En la tanda 0,** las dos reglas actúan solo sobre docvig.
  - Sobre el crudo de r2a, la regla 1 cambiaría 0 relaciones y la regla 2, las 17 que resolvió el modelo:
    ninguna trae mención (`r1_medicion.json`, clave `docvig`).
  - La cifra real sale del crudo de U-REEXT-T0, que trae la mención y corre con el prefijo de P3c.
- **En el escalado,** actúan sobre los documentos sin alcance: sus menciones colectivas van a cuarentena, con
  un nodo por documento, porque el merge entre TOs renombra los propuestos repetidos
  (`corpus_v2/r1_invariantes.py:124`).
- **Reprocesamiento.** Es un cambio de las reglas de sujetos por relación: fila F15d de la tabla, «solo código
  sobre lo guardado» (`data/experiment/mantenimiento/tabla_reprocesamiento.md:157`). No cambia ningún request.

## 4. Límites declarados y lo que queda abierto

- **Menciones que no verifican.** Las reglas no las alcanzan: sin verificación no hay regla textual, y gana el
  modelo. R2 las cuenta aparte, en la tabla del §2.
- **Una relación sin mención en cuarentena no tiene con qué nombrar su nodo.** R2 dice, antes de la firma, cómo
  queda: una fila en el registro sin nodo, o un nodo por documento.
- **Cuando un documento recibe alcance, sus filas de la regla 2 no tienen mención que re-resolver.** Queda a
  decisión de la autora, con la medición: se aplica la sugerencia guardada, se re-extrae el documento o siguen
  en cuarentena.
- **El alcance de docvig** solo de resolución, inferido del título de su punto 3.6, no se decide acá: se
  decide con la medición de R2.

## 5. Implementación, después de la firma

- `corpus_v2/r1_e4.py`, `resolver_relaciones_r2` (`:383`): una rama nueva antes de `elif modelo:` (`:418`).
  Si el documento no tiene alcance y el motivo es `colectivo_sin_sujeto_por_defecto` o `sin_mencion`, la
  sugerencia no se aplica. El registro ya guarda `sujeto_id_modelo` (`:451`).
- **Sin alcance** quiere decir sin entrada en `rol_por_to`. `ri2_ci.pdf` tiene entrada, con dos clases y sin
  rol: tiene alcance, y las reglas no lo tocan.
- Casos nuevos en el selftest de la resolución, con un documento sin alcance.
- Control: en los documentos con alcance, `resolucion_sujetos.jsonl` sale byte a byte igual.
- La implementa R2 de U-RERESOL-CAT, con esta enmienda firmada.

## 6. Qué no cambia

- El texto de L-ESQ-R2, sus notas y sus enmiendas 2 a 5.
- R1, R2 y el calificador, en todos los documentos. R3 y R4, en los documentos con alcance.
- El prefijo de E1, su tool schema, el catálogo de sujetos y sus candados.
- El paso de lectura del alcance entre tandas, que asigna solo clases que ya existen
  (`docs/mandatos/URERESOL_CAT_reresolucion_catalogo.md`, segunda nota del 04/10/2026).

## Firma

BORRADOR — PENDIENTE DE FIRMA de la autora.
