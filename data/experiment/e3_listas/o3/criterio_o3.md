# U-E3-LISTAS, O3: criterio, escrito antes de la primera llamada (07/10/2026)

Mandato firmado en `d9d8888`, etapa O3; enmienda 1 (nota al pie del 06/10/2026: población de 20, D3); código de E3 de O2
(`7fe848c`). Este archivo se escribe antes de llamar a la API; su sha256 va al freno.

**Población.** Las 20 unidades distintas de `lista_unidades_afectadas_tanda0.json` (sha256 `cc6b0cd6…`, la lista sellada
de O1): 17 con reintento por los reclamos P, C, B y B2 y 7 en la cola, 4 en los dos grupos.

**(a) Entrada y llamada.**
- La entrada es la extracción que E3 vio en la verificación del intento 0 de la tanda 0 (`extracciones_e1.jsonl`, la
  validación). El mensaje de cada unidad se controla contra la medición de O2 (`UE3_LISTAS_O2_medicion_mensajes_e3_O2.jsonl`):
  20 de 20 iguales en la corrida en seco (`a/control_mensajes_o2.json`).
- Una verificación por unidad, sin ratchet, con el código de `7fe848c` (desde una copia), el modelo y los precios de E3 de
  la tanda 0 (`claude-sonnet-5`; USD 2 / 10 / 2,5 / 0,2 por millón), en secuencia, con una base propia
  (`data/experiment/e3_listas/cache/e3_listas_o3.db`) y tope duro USD 1. Estimación: USD 0,2155
  (`a/estimacion_o3.json`).
- El veredicto se evalúa con `ratchet_e3.evaluar_veredicto` (citas con la marca r2, D1). Sin reintento.

**(a) Universo de comparación.** Los 21 reclamos P, C, B o B2 de la verificación del intento 0 de las 20 unidades, con la
categoría de la adjudicación de U-DIAG-E3-LISTAS (`reports/u_diag_e3_listas/anexo/`): C 3, B 16, B2 2. Los 3 de la
re-verificación (`ext::3.5.6.1` y `ext::3.6.1.1`: 2 P y 1 B) quedan afuera: se hicieron sobre la extracción del reintento,
no sobre la que recibe esta llamada.

**(a) Reglas de lectura.**
- *Candidatos nuevos.* Los faltantes del veredicto nuevo que pasan el filtro del diagnóstico (tipo `excepcion_ausente`,
  o «excep», «exceptu», «salvo» o «excepto» en la nota o la cita, sin tildes y en minúscula). Cada candidato lo clasifico,
  leyéndolo, con las categorías del diagnóstico: P (polaridad o sentido de una Excepcion), C (contenido que E3 no encuentra
  en su fuente), B (la norma del encabezado reclamada como entidad del ítem), B2 (sujeto o condición del encabezado que el
  ítem no compone), M (modalidad de una Excepcion), E (salvedad no representada), O (otro). La lectura se vuelca a
  `lectura_o3.json` antes de computar las cifras, y es mía: la autora la puede adjudicar.
- *Persiste.* Un reclamo viejo persiste si el veredicto nuevo trae un candidato de la misma categoría cuya cita comparte con
  la del reclamo viejo al menos una ventana de 5 tokens normalizados (`validador_r2.norm_tokens`), o una de las dos citas
  contiene a la otra después de `comun_e3.normalizar_para_cita`. Si no, desaparece.
- *Nuevo.* Un candidato P, C, B o B2 del veredicto nuevo que no es la persistencia de ningún reclamo viejo.
- *Por unidad, además, por código:* el número de faltantes y de bloqueantes, y el camino que tomaría el ratchet con este
  veredicto (aceptada, reintento o cola por veredicto inutilizable), contra el de la tanda 0.

**(b) Intento 0 contra final, sin API.** En las 17 unidades con reintento: la validación del intento 0
(`extracciones_e1.jsonl`) contra la validación de `extracciones_finales_r2_<to>.jsonl`. Entidades por (tipo, etiqueta
normalizada) y su descripción; relaciones por (predicado, etiqueta del origen, etiqueta del destino o `sujeto_id`). Sin el
`TextoOrdenado` ni las `establecida_en`. Entra, sale o cambia (misma clave, otra descripción). Se declara de qué intento es
la final (`origen_crudo`).

**(c) D3, sin API.** `ue3_o3_d3_repite_norma.py` (en `7fe848c`, sha256 `6646f7e6…`), sin cambios, sobre las 20 unidades,
intento 0 y final, con el criterio de su docstring.
