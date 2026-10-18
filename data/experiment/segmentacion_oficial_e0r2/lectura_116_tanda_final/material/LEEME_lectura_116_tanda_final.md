# Lectura corta de 1.16 en la tanda final: cómo leer (mesa, §119)

Decisión 1 de la autora del 16/10/2026: lectura corta escalonada, con la regla de la §118. Se lee el sábado 17 o el domingo 18,
mientras corre T2. Se lee sobre la E0 corregida y el PDF, sin nada de la tanda 1.

**Qué hay en esta carpeta:**
- `fichas_116_tanda_final.md`: los 30 cortes, en el orden sellado (sello: `orden_y_cortes_116_tanda_final.json`, `3db5328f…`, 08:19:19);
- `planilla_116_tanda_final.tsv`: una fila por corte, con el orden y el tramo, y las columnas de marca vacías;
- `paginas/`: las 45 páginas de las unidades y de la primera página de la unidad que sigue, a 110 ppp.

**Cómo leer:**
1. En el orden de la planilla, del corte 1 al 10 (tramo 1).
2. Cada unidad se lee contra su página, con el criterio de la ficha.
3. Escribí en la fila:
   - `marca`: `correcta`, `error` o `dudosa`;
   - si es error: `clase` (`corte` o `limpieza`), `subclase` y, si hace falta, `subclase_adicional`;
   - `nota`: lo que viste.
4. **Al terminar el corte 10:**
   - **si ninguno de los 10 tiene un error de corte confirmado,** la lectura para ahí: los 18 documentos restantes se declaran con «0 de 10»;
   - **si alguno se confirma,** seguí con los cortes 11 a 30. Sale solo el documento con un error de corte confirmado.
5. Cuenta solo el error de corte.

**Lo que la ficha no tiene:** ninguna marca ni opinión de un modelo. El «cierre candidato» es lo que marca el detector de 1.16. No se
muestran las marcas de S1-ter de los 11 candidatos que ya se leyeron, porque no están en la población.

**Al terminar:** sellá la planilla (sha256 y hora) y pasala. La mesa la controla contra el manifiesto de esta carpeta.
