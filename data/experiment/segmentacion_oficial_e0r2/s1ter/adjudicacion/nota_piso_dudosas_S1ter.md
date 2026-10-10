# U-SEG-OFICIAL, S1-ter: qué versión del piso decide (nota de la mesa, 10/10/2026)

Decisión de la autora del 10/10/2026, tomada antes de marcar la pasada 1 y sin haber visto nada de la pasada 1 ni de la lectura.
Registrada en la hoja de ruta de la mesa a las 19:10:57 (§59).

- **Decide la versión con las dudosas como error:** `etapa_1.cifra_del_piso.dudosas_como_error.llega_al_piso` en la salida de
  `scripts/cifras_lectura_S1ter.py`. Se informan las dos versiones.
- **Motivo:** una unidad es correcta solo si cumple las cinco condiciones del criterio, y una dudosa no se pudo confirmar. Así una dudosa
  nunca ayuda a llegar al piso.
- **Antes no estaba fijado:**
  - `scripts/cifras_lectura_S1ter.py:13` calcula el piso «con las dudosas como correctas y como error» y no dice cuál decide;
  - el despacho de S1-ter fija el piso sin hablar de las dudosas.
- **El script no cambia.** Esta nota fija cuál de sus dos salidas decide.
