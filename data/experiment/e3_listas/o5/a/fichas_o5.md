# U-E3-LISTAS, O5: fichas por unidad contra O3 (casos resueltos en la NOTA del ítem, primera verificación, sin ratchet)

## docvig::3.3.2 — O3: 1 faltantes, 1 bloq, cola_veredicto_inutilizable | O5: 1 faltantes, 1 bloq, cola_veredicto_inutilizable
- O3 [0] C (alta, bloq True): por la regla persiste con [0]; leído, persiste con [0]

## ext::2.6.1.1 — O3: 1 faltantes, 0 bloq, aceptada | O5: 0 faltantes, 0 bloq, aceptada
- O3 [0] - (media, bloq False): por la regla desaparece; leído, desaparece

## ext::2.6.1.2 — O3: 0 faltantes, 0 bloq, aceptada | O5: 0 faltantes, 0 bloq, aceptada

## ext::3.3.3.1 — O3: 0 faltantes, 0 bloq, aceptada | O5: 0 faltantes, 0 bloq, aceptada

## ext::3.3.3.2 — O3: 0 faltantes, 0 bloq, aceptada | O5: 0 faltantes, 0 bloq, aceptada

## ext::3.5.3.5 — O3: 0 faltantes, 0 bloq, aceptada | O5: 0 faltantes, 0 bloq, aceptada

## ext::3.5.4.3 — O3: 0 faltantes, 0 bloq, aceptada | O5: 0 faltantes, 0 bloq, aceptada

## ext::3.5.6.1 — O3: 0 faltantes, 0 bloq, aceptada | O5: 0 faltantes, 0 bloq, aceptada

## ext::3.5.6.2 — O3: 0 faltantes, 0 bloq, aceptada | O5: 0 faltantes, 0 bloq, aceptada

## ext::3.5.6.7 — O3: 0 faltantes, 0 bloq, aceptada | O5: 0 faltantes, 0 bloq, aceptada

## ext::3.6.1.1 — O3: 2 faltantes, 0 bloq, aceptada | O5: 1 faltantes, 0 bloq, aceptada
- O3 [0] B2 (media, bloq False): por la regla desaparece; leído, desaparece
- O3 [1] - (baja, bloq False): por la regla desaparece; leído, desaparece
- O5 nuevo [0] P (media, bloq False, falsa alarma): objeta que e3 sea Restriccion porque el texto dice «sólo podrá efectuarse con fondos en esa moneda»: limitar el medio de pago es una restricción; la modalidad no está invertida. Media, residual; asunto distinto de los de O3.

## ext::3.6.1.2 — O3: 1 faltantes, 0 bloq, aceptada | O5: 0 faltantes, 0 bloq, aceptada
- O3 [0] B (baja, bloq False): por la regla desaparece; leído, desaparece

## ext::3.6.1.6 — O3: 0 faltantes, 0 bloq, aceptada | O5: 0 faltantes, 0 bloq, aceptada

## ext::3.6.4.1 — O3: 1 faltantes, 1 bloq, reintento | O5: 1 faltantes, 1 bloq, reintento
- O3 [0] B (alta, bloq True): por la regla desaparece; leído, persiste con [0]
- O5 nuevo [0] B (alta, bloq True, falsa alarma): pide en el ítem la excepción compuesta con la norma del encabezado (que la operación no requiere conformidad previa) y objeta que no haya una Excepcion conectada a la norma del 3.6.4; cita el texto propio, ya no el bloque, y ya no invoca la declaración [meta_normativo] (el caso resuelto). Los ítems son los supuestos de una sola salvedad («excepto que la operación encuadre en alguna de las siguientes situaciones») y E1 los modeló como Condicion: la NOTA dice que esa forma vale (C5b), que si no queda claro cualquiera vale (C7) y que la falta de la norma del encabezado no es faltante (C9, C11). Falsa alarma, alta y bloqueante: el mismo asunto que el B de O3 por otro camino.

## ext::3.6.4.2 — O3: 2 faltantes, 0 bloq, aceptada | O5: 2 faltantes, 1 bloq, reintento
- O3 [0] B (media, bloq False): por la regla desaparece; leído, desaparece
- O3 [1] O (baja, bloq False): por la regla desaparece; leído, desaparece
- O5 nuevo [0] O (media, bloq False, fundado): la descripción de e4 no lleva el calificador temporal «en ningún momento, hasta la fecha de vencimiento de la deuda que se cancela»: fundado en eso; lo que dice de que la descripción quedó con «podrá superar» es falso (dice «no podrá superar»). Media, residual; texto propio, no la lista.
- O5 nuevo [1] P (alta, bloq True, falsa alarma): polaridad: los umbrales de e4 copian «podrá superar el monto…», fragmento literal del texto, que dice «en ningún momento … podrá superar» y no «no podrá superar»; el tipo Restriccion y la descripción («no podrá superar») llevan la prohibición. Falsa alarma, alta y bloqueante, ajena a la lista y a los casos resueltos (O3 no la tenía: variación entre muestras).

## ext::3.13.1.1 — O3: 0 faltantes, 0 bloq, aceptada | O5: 0 faltantes, 0 bloq, aceptada

## ext::3.13.1.6 — O3: 0 faltantes, 0 bloq, aceptada | O5: 1 faltantes, 0 bloq, aceptada
- O5 nuevo [0] B (baja, bloq False, falsa alarma): pide que el ítem sea una Excepcion compuesta con el encabezado («requerirá la conformidad previa del BCRA, excepto para las operaciones de:») y no Operacion con Condicion; con miembros que quedan afuera la forma es Excepcion (C5a), pero si no queda claro cualquiera vale (C7). Baja, residual; O3 no lo tenía.

## ext::3.13.1.10 — O3: 2 faltantes, 0 bloq, aceptada | O5: 0 faltantes, 0 bloq, aceptada
- O3 [0] - (media, bloq False): por la regla desaparece; leído, desaparece
- O3 [1] - (media, bloq False): por la regla desaparece; leído, desaparece

## ext::3.16.2.1 — O3: 2 faltantes, 1 bloq, reintento | O5: 1 faltantes, 1 bloq, reintento
- O3 [0] B (alta, bloq True): por la regla persiste con [0]; leído, persiste con [0]
- O3 [1] - (media, bloq False): por la regla desaparece; leído, desaparece

## ext::3.18.1.1 — O3: 2 faltantes, 2 bloq, reintento | O5: 2 faltantes, 1 bloq, reintento
- O3 [0] - (alta, bloq True): por la regla persiste con [0]; leído, persiste con [0]
- O3 [1] - (alta, bloq True): por la regla persiste con [1]; leído, persiste con [1]
