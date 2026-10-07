# Punto 4 — Renglones anotados como «parte de un título heredado»

La clase tiene **14** renglones, no 20 o más (`s1/explicacion_censo_S1.json`, `por_clase_y_explicacion`:
`encabezado_o_pie_no_repetido|parte_de_un_titulo_heredado` = 14). `random.Random("U-SEG-OFICIAL:censo:2026-10-06:titulo_heredado").sample(lista_ordenada, 20)`
falla («Sample larger than population»), así que los leí todos, como manda la nota de `2faff14` para un estrato chico.

| # | TO | p. | r. | renglón | qué es en la página |
|---|---|---|---|---|---|
| 1 | ceninf | 7 | 3 | adulterados. | 2.ª línea del título de la sección 2 en el recuadro |
| 2-3 | cryl | 16 | 4-5 | Sección 6. Instructivos… con concer- / tación y liquidación en CRyL. | título de la sección 6 en dos líneas, recuadro |
| 4-5 | ctacor | 7 | 3-4 | Sección 3. Solicitud del servicio… - / “nuestra cuenta”. | título de la sección 3, recuadro |
| 6 | ctacte | 54 | 3 | exigibles. | 2.ª línea del título de la sección 11, recuadro |
| 7 | ctavis | 32 | 4 | cambio inhabilitados y Central de letras… extra- | 2.ª de 3 líneas del título de la sección 7, recuadro |
| 8 | expaef | 14 | 3 | Sección 4. Instalación de cajeros automáticos… características | 1.ª línea del título de la sección 4, recuadro |
| 9 | finsec | 18 | 3 | ficos. Requisitos. | 2.ª línea del título de la sección 5, recuadro |
| 10 | finsec | 20 | 3 | Sección 5. Asistencias a fideicomisos… espe- | 1.ª línea del mismo título, recuadro |
| 11 | icmecma | 23 | 5 | Internet (“home banking”). | 2.ª línea del título de la sección 5, recuadro |
| 12-13 | rdbcra | 22 | 4-5 | Sección 4. Sumarios Financieros… / cumplimiento normativo voluntario… (AC). | título de la sección 4, recuadro |
| 14 | rmrtsd | 5 | 5 | digitales. | 2.ª línea del título de la sección 2, recuadro |

Resultado: **14 de 14 son títulos** (de sección, en el recuadro del encabezado); **0 son texto de norma**.
Recortes de las 14 zonas en `paginas_titulo_heredado_S1_mesa_a.png` y `_b.png`.
