# U-DIAG-VINCULO — lectura de precisión de la dirección (a) (04/10/2026, lectura asistida, revisión de la autora PENDIENTE)

Aplico la regla de lectura del §9 de `regla_deteccion.md` (sha `f912176c…`, escrita antes del sorteo) a las
fichas de `muestra_precision_fichas.md`, que sorteó `code/censo_anuncios.py` con semilla 20261004.
- Grafo: KG-Tanda0-Diez-r2a (`99fe2bfa…`), crudo `v3_b54`.
- Veredictos: C = correcta, I = incorrecta, ND = no decidible.
- **Lectura operativa de la condición 2 de `remite_a`** («la norma que contiene la cláusula»). La declaro acá
  porque la fijé al leer, no antes. Cuentan como origen: la cláusula que anuncia, el nodo deóntico de la
  oración que la contiene, el acto que esa norma regula y la condición que el anuncio completa. No cuenta un
  nodo de otra oración del párrafo, ni una condición de marco de la misma oración que no es la que completa
  el anuncio.

## (a-T), predicado tipado con regla de destino único: 15 pares, 23 aristas

| # | par | tipo | aristas | veredicto | motivo |
|---|---|---|--:|---|---|
| 1 | ext::13.3::intro → 13.3.4 | c1 | 1 | C | la situación del ítem condiciona el pago anticipado admitido (Operacion) |
| 2 | ext::10.11::intro → 10.11.3 | excepción | 1 | C | excepción alternativa a la conformidad previa |
| 3 | ext::3.16.3::intro → 3.16.3.7 | excepción | 1 | I | el contenedor anuncia el contenido de la declaración jurada (3.16.3.1 a .4); la Excepcion del 3.16.3.7 dispensa una declaración del propio 3.16.3.7, no la conformidad previa |
| 4 | ext::5.8.2::intro → 5.8.2.4 | c1 | 1 | C | condición del ingreso a nombre de la empresa local |
| 5 | ext::3.16.3::intro → 3.16.3.6 | excepción | 5 | I ×5 | 3.16.3.6 dice qué no se computa en la declaración jurada, no exceptúa la conformidad previa; el hijo no es uno de los ítems anunciados |
| 6 | ext::7.5.7::intro → 7.5.7.1 | c1 | 1 | C | condición conjunta de la potestad de extender el plazo |
| 7 | ext::3.13.1::intro → 3.13.1.1 | excepción | 1 | C | «excepto para las operaciones de:» → organismos internacionales |
| 8 | ext::10.4.3::intro → 10.4.3.4 | c1 | 1 | C | requisito de la potestad de dar acceso |
| 9 | ext::3.16.3::intro → 3.16.3.5 | excepción | 4 | I ×4 | 3.16.3.5 no es un ítem de la declaración jurada; dice que 3.16.3.1 a .4 no se aplican a ciertas operaciones. La arista afirma algo que el texto no dice en esos términos |
| 10 | ext::10.11::intro → 10.11.4 | excepción | 1 | C | excepción alternativa (BOPREAL) |
| 11 | ext::7.5.7::intro → 7.5.7.2 | c1 | 1 | C | segunda condición conjunta |
| 12 | ext::8.5.13::intro → 8.5.13.4 | c1 | 1 | C | condición de la imputación de multas |
| 13 | ext::9.3.10::intro → 9.3.10.4 | c1 | 2 | C ×2 | lo que la documentación debe permitir verificar, compuesto con el encabezado |
| 14 | ext::10.4.3::intro → 10.4.3.2 | c1 | 1 | C | requisito de la potestad de dar acceso |
| 15 | ext::3.6.4::intro → 3.6.4.5 | excepción | 1 | C | situación exceptuada de la conformidad previa |

- **Por arista: 13 de 23 correctas**, Wilson 95 % [0,368; 0,744].
- **Por par: 12 de 15**, Wilson [0,548; 0,930].
- 0 no decidibles.
- Las 10 incorrectas son de un solo contenedor (`ext::3.16.3::intro`): sus hijos 3.16.3.5 a .7 son hijos por
  número pero no son ítems de la lista anunciada.
- E0 les pone a todos los hijos el mismo intro en la herencia (`salida_tanda0/chunks_ext.json`, 3.16.3.1, .4 y
  .5), así que la herencia no los distingue.
- La población es chica: 23 pares, 22 de ext y 1 de ctacte (`censo_anuncios.json`, `pares_aT`).

## (a-R), `remite_a` estructural: 15 pares, 76 aristas

| # | par | aristas | C | I | motivo de las I |
|---|---|--:|--:|--:|---|
| 1 | ext::11.1.1::intro → 11.1.1.7 | 3 | 3 | 0 | |
| 2 | cla::6.5.1::intro → 6.5.1.6 | 1 | 1 | 0 | |
| 3 | ext::4.1.4::intro → 4.1.4.4 | 2 | 2 | 0 | |
| 4 | ext::8.5.17::intro → 8.5.17.2 | 4 | 4 | 0 | |
| 5 | ext::3.5.1::intro → 3.5.1.2 | 6 | 6 | 0 | |
| 6 | ext::13.1::intro → 13.1.1 | 6 | 3 | 3 | el destino Operacion «Pago de servicio prestado por no residente» repite el encabezado; no es contenido del texto del hijo (condición 3) |
| 7 | ctacte::8.3::intro → 8.3.2 | 6 | 6 | 0 | (el origen es el nodo de solo anuncio de `BKL-0035`) |
| 8 | pagjub::2.8.1::intro → 2.8.1.1 | 4 | 2 | 2 | origen «Aceptación de presentación…», de la oración anterior (condición 2) |
| 9 | ext::10.2.4::intro → 10.2.4.5 | 2 | 2 | 0 | |
| 10 | ext::8.5.17::intro → 8.5.17.20 | 6 | 6 | 0 | |
| 11 | ext::7.6.1::intro → 7.6.1.1 | 2 | 2 | 0 | |
| 12 | ext::14.2.1::intro → 14.2.1.1 | 4 | 2 | 2 | origen: condición de marco «en el marco de lo dispuesto en los puntos 3.3…» (condición 2) |
| 13 | ext::14.2::intro → 14.2.2 | 8 | 4 | 4 | origen: condición de marco «se cumplan los restantes requisitos» (condición 2) |
| 14 | ctacte::3.2.1::intro → 3.2.1.9 | 2 | 2 | 0 | |
| 15 | ext::3.16.3::intro → 3.16.3.5 | 20 | 0 | 20 | el hijo no es uno de los ítems anunciados (condición 1) |

- **Por arista: 45 de 76 correctas**, Wilson [0,480; 0,696]. Sin el par 15, 45 de 56, Wilson [0,682; 0,887].
- **Pares con todas sus aristas correctas: 10 de 15**, Wilson [0,417; 0,848].
- **Pares con el anuncio bien atribuido (condición 1): 14 de 15**, Wilson [0,702; 0,988].
- **Causas de las 31 incorrectas:**
  - 20 por hijo no anunciado;
  - 8 por origen: la regla D1 atribuye la cita a todos los nodos del contenedor;
  - 3 por destino que repite el encabezado.
- Las aristas de un mismo par no son independientes, así que los intervalos por arista subestiman la
  incertidumbre.

## Resumen frente al criterio de L-ESQ-R2

El piso de Wilson del criterio de §6.3 es 0,75 (`git show 4ef7650:data/experiment/esq/enmienda_L-ESQ-R2_2026-09-30.md`,
`:788-789`), y el principio del §1 dice que se retira lo que produce falsedad en campo estructurado (`:100-101`).
Con la regla simulada sobre el crudo `v3_b54`, ninguna de las dos variantes llega a ese piso: 0,368 para (a-T) y
0,480 para (a-R). Las tres causas tienen un arreglo candidato en código:
- el origen, con el `tramo` que r2b pide en toda entidad;
- el hijo no anunciado, con un filtro de hijos;
- el destino compuesto, con el segundo segmento del `tramo`.

Ninguno de los tres está medido.
