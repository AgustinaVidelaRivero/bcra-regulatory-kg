# Regla de caída del grafo evaluado, por calendario (decisión de la autora del 15/10/2026, sellada por la mesa)

USD 0. La propuso la mesa en su plan hacia atrás desde el 28/10/2026 (hoja de ruta de la mesa, §100,
`decisiones_100_mesa/plan/plan_hacia_atras_desde_el_28_10_mesa.md`, §7). La aprobó la autora el 15/10/2026, en el pedido recibido a las
12:16:27 (hoja §101): «La regla de caída, tal cual la propusiste. Sellala hoy.»

Se fija antes de que corra la tanda 1 y antes de leer cualquier salida de las tandas que faltan, así que no depende de lo que se lea. El
archivo de sello que la acompaña tiene su sha256 y la hora.

## La regla

1. **El punto de corte.** El grafo evaluado se sella el sábado 24/10/2026 con lo cerrado, que son las tandas 0 y 1, «por calendario»
   (`docs/protocolo_dos_grafos.md:64`), si pasa cualquiera de estas dos cosas:
   - el miércoles 21/10/2026 a las 18:00 (−03) la tanda final, que es la fusión de las tandas 2 y 3, no está despachada;
   - el viernes 23/10/2026 a las 18:00 (−03) la tanda final no está sellada.
2. **Las preguntas.** Las de los documentos de la tanda final salen del conjunto (a) de B6.3, declaradas. El sorteo de documentos va
   estratificado de modo que la opción de U-EVAL-CLASES que se fije se cumpla con los documentos de la tanda 1. Si la regla de
   contaminación deja menos documentos por grupo de los que esa opción pide, no se cumple y se declara.
3. **La tanda final.** Corre igual después, para el grafo completo y el grafo corregido del cap. 6, sin entrar en B6.3.

## Lo que esta regla no cambia

- No saca ninguna revisión entre tandas, lectura a ciegas, verificación, control ni prueba en seco, ni las acorta para llegar a las
  fechas (regla de la autora del 15/10/2026, hoja §101: «las fechas son el límite, no el objetivo»). Si un paso se demora por eso, la
  regla de arriba decide qué entra en el grafo evaluado.
- Las fechas son el límite. Si la tanda final queda lista antes, se despacha antes.
