# U-UNION-ESTRECHA: qué pasa con U3 si el control de las uniones de la tanda 1 no llega al piso (sellado el 15/10/2026, antes de leer)

USD 0. Decisión de la autora del 15/10/2026, recibida a las 13:55:26 (hoja de ruta de la mesa, §103), tal cual:
«si no llega al piso, U3 no entra en el grafo evaluado y va al grafo corregido del cap. 6, declarado con su cifra. Lo mismo si salen
menos de 12 uniones y el piso no se puede alcanzar. Fijalo antes de leer, en un archivo aparte y sellado que cite el control
(c5aec07a…), sin tocar el archivo ya sellado.»

**El control que esta regla completa:** `parametros_control_uniones_tanda1_2026-10-15.md`, en esta misma carpeta, sellado el 15/10/2026 a
las 13:08:23 (sha256 `c5aec07ad603eef60d8ac3ca1920c4151fac9c863e49616f109bffe24373079f`). Ese archivo no se toca.

## La regla

1. **Si el control llega al piso** (el límite inferior de Wilson al 95 % ≥ 0,75, con las no decidibles como no correctas, como fija el
   control), U3 entra en el grafo evaluado.
2. **Si no llega al piso,** U3 no entra en el grafo evaluado:
   - va al grafo corregido del cap. 6;
   - se declara con la cifra del control: las correctas sobre las leídas, con su intervalo.
3. **Si la regla da menos de 12 uniones en los TOs de la tanda 1,** el piso no se puede alcanzar ni con todas correctas, y pasa lo mismo
   que en el punto 2:
   - el control se lee igual, como fija el control sellado;
   - U3 no entra en el grafo evaluado, va al grafo corregido del cap. 6 y se declara con su cifra.

## Lo que no cambia

- El tamaño, la semilla, el piso y la manera de leer del control sellado.
- Lo que el control mide: la precisión de la regla de U3 en los TOs de la tanda 1, con el criterio de U2.
