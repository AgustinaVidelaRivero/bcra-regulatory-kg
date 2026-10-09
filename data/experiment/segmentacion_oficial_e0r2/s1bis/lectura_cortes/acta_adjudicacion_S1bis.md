# Adjudicación de la autora — lista de la lectura de cortes S1-bis (41 casos)
Fuente: lista_para_la_autora_S1bis_mesa.md. Criterio: mandato e543cb2 y nota de 2faff14. Adjudicación de la autora, 09/10/2026, caso por caso contra las páginas renderizadas; las correctas, también contra el texto de las fichas.

Fichas usadas para las correctas: fichas_lectura_S1-bis-b.md (paquete del FRENO S1-bis-b, copia permanente 0c0c6584…/revision_USEG_OFICIAL_FRENO_S1-bis-b/), 237841 bytes, 8/10 17:32, sha256 bf5da8aacc9ebc095f0dbb06f54cee2266921608b1df288bd6619d2f521f9d2e

## Errores (16): 8 del primer grupo y 8 del censo del 1.16

| # | parte | unidad | marca de la mesa | decisión de la autora | nota |
|---|---|---|---|---|---|
| 1 | 1 | adfsp::1.1.10 | error · corte · termina_fuera + trae_texto_de_otro_punto | confirma (09/10 08:46) | cierre de 1.1 en la sangría de los rótulos; patrón del 1.16 |
| 2 | 1 | snp_dd::S7::intersticial::17 | error · corte · falta_texto_propio | confirma (09/10 08:49) | título del campo 4 sin su descripción (mismo bloque, sin blanco) |
| 3 | 1 | snp_dd::S7::intersticial::13 | error · corte · falta_texto_propio | confirma (09/10 08:59) | primer renglón de la fila R95, corta en «En-» y «presente una». Observación para S0-5: 2 y 3, mismo mecanismo (bloque de varios renglones partido después del primero) |
| 4 | 1 | ri_iepsp::S0 | error · limpieza · restos_encabezado | confirma (09/10 09:01) | unidad hecha solo del 3er renglón del recuadro de encabezado; el límite con el punto 1 está bien |
| 5 | 1 | ri_ieccm::S0 | error · limpieza · restos_encabezado | confirma (09/10 09:01) | ídem 4. Observación para S0-5: 4 y 5, mismo mecanismo (encabezado de tres renglones limpiado en parte) |
| 6 | 1 | ri_ccna::D1F3::S0 | error · corte · termina_fuera + trae_texto_de_otro_punto | confirma (09/10 09:05) | «C» del rótulo vertical «CODIGO» del formulario siguiente (p. 39; 7 px por encima del primer renglón). Sin tolerancia en el criterio → error. Corte, no limpieza: «CODIGO» es contenido del formulario siguiente, no algo que se repite en la página |
| 7 | 1 | ri_icpipsp::A1C3::S2 | error · limpieza · restos_encabezado | confirma (09/10 09:08) | encabezado de página de la tabla (rótulos de columna + «PROCEDIMIENTOS ANUALES») entre (iv) y (v); se repite arriba de cada página; límites bien |
| 8 | 1 | ri2_ae::S2::chapeau_seccion | error · corte · empieza_fuera | confirma (09/10 09:10) | 2º renglón del título de la sección 2; la sección no tiene chapeau; la herencia queda cortada en «el "Registro» (para S0-5) |
| 9 | 4 (censo 1.16) | cajasc::11.4.4 | error · corte · termina_fuera + trae_texto_de_otro_punto | confirma (09/10 09:11) | cierre de 11.4; sus dos renglones en el margen de los rótulos (162 px), las continuaciones de ítem van a 217 |
| 10 | 4 (censo 1.16) | cajasc::4.2.2.3 | error · corte · termina_fuera + trae_texto_de_otro_punto | confirma (09/10 09:13) | «La vida promedio…» (260 px) es propio; «Los préstamos a que se refieren los puntos 4.2.2.1. y 4.2.2.3.…» (199 px, nombra dos hermanos) es el cierre de 4.2.2 |
| 11 | 4 (censo 1.16) | depaho::3.11.5.5 | error · corte · termina_fuera + trae_texto_de_otro_punto | confirma (09/10 09:14) | «Los movimientos…» arranca en 218 (cuerpo de un 3.11.x), el texto de 3.11.5.5 en 287; cierre de 3.11.5 |
| 12 | 4 (censo 1.16) | manori::1.4.1.3 | error · corte · termina_fuera + trae_texto_de_otro_punto | confirma (09/10 09:16) | párrafo «La entidad financiera deberá desarrollar documentación respaldatoria…» en 204-205 (rótulos / cuerpo de 1.4.2), texto de 1.4.1.3 en 269. Contenido ambiguo: decide la sangría, misma regla que en los correctos |
| 13 | 4 (censo 1.16) | manori::3.4.1.3 | error · corte · termina_fuera + trae_texto_de_otro_punto | confirma (09/10 09:16) | ídem 12, sección 3; medidas idénticas |
| 14 | 4 (censo 1.16) | ri_oc::B.1.28 | error · corte · termina_fuera + trae_texto_de_otro_punto | confirma (09/10 09:20) | tres bloques de la p. 17 en 118 px (margen de B.1) que explican B.1.24, B.1.25, B.1.16 y B.1.17. Pregunta para el plan: ¿«el cierre heredado de ri_oc» (límite declarado de S0-4) es este? Si lo es, la marca no cambia; la población del censo no se toca después de leer |
| 15 | 4 (censo 1.16) | ri_oc::C.11 | error · corte · termina_fuera + trae_texto_de_otro_punto | confirma (09/10 09:22) | se lleva los dos títulos del bloque de validaciones (p. 19) y no su cuerpo. Observación para S0-5: mismo mecanismo (el último ítem absorbe hasta el próximo rótulo), pero lo absorbido es el título del bloque siguiente, no el cierre del padre; una corrección solo de cierres no lo arregla |
| 16 | 4 (censo 1.16) | ri_rml::1.2.3 | error · corte · falta_texto_propio | confirma (09/10 09:23) | se corta en «…descripto en el punto»; el renglón siguiente empieza con «1.3.» (remisión leída como rótulo; arranca en 140 = cuerpo, los rótulos van en 118). No es el patrón del 1.16. Para el plan: verificar adónde fueron esos dos renglones (¿unidad fantasma «1.3»?) |


## Correctas sorteadas (25): 20 del primer grupo y ri_spi, 5 del censo — confirmadas el 09/10 a las 09:31

| # | parte | unidad | marca de la mesa | decisión | nota |
|---|---|---|---|---|---|
| 17 | 3 | snp_psp::4.5.6 | correcta | confirma | completa; sigue el título 4.6 |
| 18 | 3 | pagjub::2.7.5 | correcta | confirma | solo el ítem; el cierre de 2.7 está en la herencia (no en la unidad) |
| 19 | 3 | snp_cheq::8.4.2.5 | correcta | confirma | |
| 20 | 3 | garant::3.1.11 | correcta | confirma | |
| 21 | 3 | snp_cheq::8.4.1.11 | correcta | confirma | |
| 22 | 3 | snp_spd::8.1.1.4 | correcta | confirma | |
| 23 | 3 | gerc::4.3.2 | correcta | confirma | serialización de la tabla rara (fuera del criterio de corte; ya anotado por la mesa) |
| 24 | 3 | ri_dcpc::3.6.5 | correcta | confirma | |
| 25 | 3 | seguef::6.5.15 | correcta | confirma | cierre de 6.5 en la herencia |
| 26 | 3 | ri_dcpc::3.2.2.1 | correcta | confirma | pp. 13-14, termina antes de 3.2.2.2 |
| 27 | 3 | seguef::2.3.2 | correcta | confirma | |
| 28 | 3 | seguef::1.4 | correcta | confirma | |
| 29 | 3 | seggar::S2 | correcta | confirma | |
| 30 | 3 | nmaeef::S9 | correcta | confirma | |
| 31 | 3 | ri_oc::B.3.1 | correcta | confirma | (ver pregunta b2: la herencia no muestra cierre de B.3) |
| 32 | 3 | ri_mmsef::2.2.8.3.5 | correcta | confirma | (herencia: intro de 2.2 partida a mitad de oración) |
| 33 | 3 | ri_secoexpo::S16 | correcta | confirma | |
| 34 | 3 | ri_mmsef::2.3.5.2 | correcta | confirma | |
| 35 | 3 | seggar::S3::cierre | correcta | confirma | exactamente el cierre de 3 |
| 36 | 3 | ri_spi::C.1.2 | correcta | confirma | (herencia: título de C partido en encabezado + chapeau «APARTADO B») |
| 37 | 5 | depaho::3.6.2.4 | correcta | confirma | párrafo en la sangría del texto de 3.6.2.4 |
| 38 | 5 | lingeef::10.3.2 | correcta | confirma | ídem |
| 39 | 5 | lingeef::5.1.1.3 | correcta | confirma | cierre de 5.1.1 en la herencia |
| 40 | 5 | lingeef::6.2.1.9 | correcta | confirma | termina antes de 6.2.1.10 (6.2.1.10 quedó como cierre de 6.2.1: error de otra unidad, ya anotado por la mesa) |
| 41 | 5 | snp_tr::4.2 | correcta | confirma | |

## Resultado
Las 41 marcas de la mesa confirmadas tal cual, con su clase y subclase: 16 errores y 25 correctas. Ninguna cambia.

## Observaciones para el diseño de S0-5 (hipótesis a verificar en código; no tocan marcas)
- Elementos de varios renglones reconocidos solo por el primero o los primeros: casos 2, 3 (bloque de campo, fila de tabla), 4, 5 (recuadro de encabezado de tres renglones) y 8 (título de dos renglones). Fuera de la muestra, en la herencia: título de C en ri_spi (encabezado «…RELACIONADOS CON EL» + chapeau «APARTADO B») e intro de 2.2 en ri_mmsef partida en «…de acuerdo con lo» / «establecido por las…».
- Caso 15 (ri_oc::C.11): el último ítem absorbe el título del bloque siguiente, no el cierre del padre.
- Caso 16 (ri_rml::1.2.3): remisión al principio de un renglón leída como rótulo.
- Caso 7 (ri_icpipsp::A1C3::S2): encabezado de página de una tabla de varias páginas dentro de la unidad.
- lingeef 6.2.1.10 en el cierre de 6.2.1 (ya anotado por la mesa).

## Preguntas para el plan
- ¿«El cierre heredado de ri_oc» (límite declarado de S0-4) es el cierre de B.1 que está dentro de ri_oc::B.1.28?
- ¿Cómo se eligieron los 35 candidatos del censo del 1.16? ri_oc B.2.4 y B.3.4 (cierres de B.2 y B.3 en el margen del padre, sin cierre en la herencia de B.3.1) y el párrafo que sigue al ítem 17 de ri_secoexpo no están entre ellos.
- ¿En qué unidad quedaron los dos renglones que le faltan a ri_rml::1.2.3?

