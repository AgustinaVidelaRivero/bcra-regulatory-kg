# Lectura de los 14 límites de sub-documento de la tanda 1: cómo leer (mesa, §118)

Decisión 1 de la autora del 16/10/2026: lee los 14 con la regla de lectura de S1-bis, el sábado 17 o el domingo 18, mientras corre T2.
Un error de corte confirmado confirma el rasgo, y entonces los 33 límites de la tanda final van por la regla de la decisión 1.

**Qué hay en esta carpeta:**
- `fichas_subdocumento_tanda1.md`: una ficha por unidad de E0 (8 unidades), con los límites que caen en ella;
- `planilla_subdocumento_tanda1.tsv`: una fila por límite (14), con las columnas de marca vacías;
- `paginas/`: las 17 páginas de esas unidades, a 110 ppp.

**Cómo leer:**
1. Para cada fila de la planilla, abrí la página del límite y ubicá el renglón: `top` en puntos desde arriba; en la imagen, a unos
   `top × 110 / 72` píxeles. La ficha da los dos números.
2. Leé la unidad que lo contiene contra la página, con el criterio (1) a (5) de la ficha.
3. Escribí en la fila:
   - `unidad_leida`: el id de esa unidad;
   - `marca`: `correcta`, `error` o `dudosa`;
   - si es error: `clase` (`corte` o `limpieza`), `subclase` y, si hace falta, `subclase_adicional`;
   - `nota`: lo que viste.
4. Cuenta solo el error de corte. La herencia se muestra en la ficha, pero no es parte del criterio.

**Lo que la ficha no tiene:** ninguna marca ni opinión de un modelo. Las ocho unidades salen tal cual de la E0 corregida (`80adbd58…`).

**Al terminar:** sellá la planilla (sha256 y hora) y pasala. La mesa la controla contra este manifiesto y arma el registro y su commit.
