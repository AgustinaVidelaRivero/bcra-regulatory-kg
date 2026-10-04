# Notas a la política por campo del perfil r2

La política (`politica_campos_r2.json`, versión 3) está sellada por su sha256 (`82e8752a…`,
`data/experiment/reextraccion_v2/corpus_v2/r1_e4.py:499`) y no se edita. Estas notas se leen junto con ella.

- **04/10/2026 — `Comunicacion.tipo`, paso `derivar_de_codigo_o_label` (decisión de la autora; etapa P3b de
  U-PROMPT-R2).** El texto del paso dice: «el `codigo` o el `label` tiene la forma de una Comunicación: letra
  A, B o C y número» (`politica_campos_r2.json:78`). Con la forma de salida «r2», el validador aplica ese paso
  sobre el tramo de evidencia de la entidad, verificado contra el texto de la unidad, y no sobre el `codigo`
  ni el `label` (`code/validador_r2.py`, `derivar_comunicacion_tramo`):
  - si el tramo nombra una Comunicación, el tipo es su letra, y el número se controla contra el `codigo`;
  - si nombra una norma externa, por el léxico de la política, el tipo es «externa»;
  - si no, el tipo no se deriva y se cuenta.

  Motivo: el `codigo` y el `label` los escribe el modelo. En KG-Tanda0-Diez-r2a, el nodo de código `A-39` es
  el artículo 39 de la Ley 21.526 (`ctacte::12.10.2`) y quedó con tipo «A» (hallazgo 1.12 de la revisión
  independiente, `reports/u_revision_libre/`; medida en `data/experiment/prompt_r2/p3b/diseno_p3b.md`, §6).

  Con la forma «v3» el paso sigue como dice su texto, y los grafos sellados no cambian. El nombre del paso
  tampoco cambia, para no mover el sha256 de la política.

  L-ESQ-R2 dice lo mismo que el texto del paso: el tipo «se deriva en código del `codigo`» (§2.3 y §2.4;
  `git show 4ef7650:data/experiment/esq/enmienda_L-ESQ-R2_2026-09-30.md`, `:488-489` y `:505`).

- **04/10/2026 — la nota anterior es la referencia de implementación de la enmienda 4 a L-ESQ-R2 (decisión de
  la autora).** La regla quedó en `data/experiment/esq/enmienda4_L-ESQ-R2_comunicacion_tramo_2026-10-04.md`,
  FIRMADA por la autora el 04/10/2026: con la forma r2, el tipo de la Comunicación se deriva del tramo
  verificado; el número se toma del `codigo` y se controla contra los números que nombra el tramo
  (`code/validador_r2.py`, contadores `tramo_coincide`, `tramo_no_coincide` y `sin_numero_para_controlar`); con
  los perfiles existentes, la regla de L-ESQ-R2 §2.3 y §2.4 sigue igual.
