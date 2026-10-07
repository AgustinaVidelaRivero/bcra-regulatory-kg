# U-LECTURA-ACEPTADAS — reporte de L2: tasa de error por unidad de las aceptadas de la tanda 0

Generado por `l2_estimadores.py` a las 2026-10-07T00:41:45-03:00 (USD 0, sin API). Mandato `docs/mandatos/ULECTURA_ACEPTADAS_tasa_error_tanda0.md`, FIRMADO en `9502ca4`, con su nota al pie del 06/10/2026 (`6e611d6`). Todas las cifras salen de `estimadores_l2.json`, que el mismo script escribe; el comando está en la sección 9.

## 1. Método

- **Población.** Las unidades aceptadas del grafo evaluado de los diez TOs sin la cola (KG-Tanda0-Diez-r2b-sincola, `e22fae1a…`): las de estado final `completo_ok_directo`, `aceptado_con_residuales` o `aceptado_tras_reintento` en `corpus_tanda0/salida_r2b/<to>/finales.jsonl`. N = 2.366; ítems de lista (`prompt_r2b.es_item` sobre el chunk de E0 r2b) N₁ = 1.003 y no ítems N₂ = 1.363; W₁ = 1.003/2.366 = 0,423922 y W₂ = 0,576078, recomputados contando las filas de `sellos_l0.json`.
- **Sello previo (L0).** Semilla `U-LECTURA-ACEPTADAS:sorteo:2026-10-06`, fijada por la firma; sorteo a las 2026-10-06T19:18:34-03:00, antes de abrir una ficha (la hora de las fichas, posterior, está en `fichas_l1_cabecera.json`); sha256 de la muestra `a3c5a595…`; 30 unidades por estrato, por muestreo simple dentro de cada uno.
- **Dos lecturas y adjudicación.** Primera lectura, de la instancia, sobre las 60 fichas (`veredictos_l1.jsonl`); segunda, de la mesa, a ciegas sobre las fichas sin veredicto: el mismo veredicto en las 60, sin divergencias (nota al pie del mandato, `6e611d6`). Las reglas de lectura R1–R4 están en la cabecera de `l1_veredictos.py`. Adjudicación de la autora (`adjudicacion_autora_l2.json`, sha256 `ad99a2f6…`): «Las 10 confirmadas; las dudas quedan como observaciones.»
- **Criterio** (§1, el del punto 1 de T4): una unidad tiene error si al menos un nodo o una relación de la extracción no se sostiene en el texto de la unidad (propio o heredado); las omisiones no cuentan. **Alcance fijado** (decisión 1 de la nota al pie): tres cifras, (i) la tasa de la unidad con ese criterio, (ii) aparte, las `remite_a` por cita y destino, (iii) los tipos documentales mal asignados, como observación.
- **Estimadores** (§5, escritos antes de leer). Wilson al 95 % con z = 1,959964 (la fórmula de T4, `reext_t0/t4/tasas_t4.py:244-249`); ponderado p̂ = W₁·p̂₁ + W₂·p̂₂ con p̂ ± z·√(W₁²·p̂₁(1−p̂₁)/n₁ + W₂²·p̂₂(1−p̂₂)/n₂), sin corrección por población finita (las fracciones muestrales son 0,030 y 0,022); y el conservador por combinación de los límites de Wilson.

## 2. Las tres cifras

### (i) Tasa de error por unidad (criterio de T4)

| Estrato | N_h | W_h | con error | p̂ | Wilson 95 % |
|---|--:|--:|--:|--:|---|
| ítems | 1.003 | 0,423922 | 6 de 30 | 0,2000 | [0,0951; 0,3731] |
| no ítems | 1.363 | 0,576078 | 4 de 30 | 0,1333 | [0,0531; 0,2968] |

- **Ponderado, la tasa del grafo:** p̂ = 0,1616 ± 0,0927, es decir [0,0689; 0,2543] (con 1,96, el redondeo que escribe el mandato: [0,0689; 0,2543]).
- **Conservador** (W₁·LI₁ + W₂·LI₂; W₁·LS₁ + W₂·LS₂): [0,0709; 0,3291]. Ningún estrato dio 0 ni 30 de 30, así que el intervalo ponderado no colapsa; las dos cifras van, con la ponderada como la tasa del grafo.
- **Comparación con la cola** (T4 de U-REEXT-T0, `data/experiment/reext_t0/t4/salida/tasas_t4.json, punto_1`): 12 de 30 con error, Wilson [0,2459; 0,5768]. Mismo criterio y misma fórmula; poblaciones distintas (las 74 de la cola frente a las 2.366 aceptadas), así que es una comparación descriptiva, no una prueba. Ítems: [0,0951; 0,3731], se superpone con el de la cola; no ítems: [0,0531; 0,2968], se superpone con el de la cola; ponderado: [0,0689; 0,2543], se superpone con el de la cola; conservador: [0,0709; 0,3291], se superpone con el de la cola. El p̂ ponderado (0,1616) queda por debajo del límite inferior de la cola (0,2459).

### (ii) Las `remite_a`, por cita y destino

- 0 de 167 aristas no sostenidas, en 11 unidades (ítems: 46 aristas en 6 unidades; no ítems: 121 en 5). Wilson al 95 %: por aristas [0,0000; 0,0225]; por unidades (0 de 11) [0,0000; 0,2588].
- Las aristas no son independientes (van agrupadas en las unidades, y en cada unidad repiten la cita por cada nodo de origen y de destino): el intervalo por aristas es descriptivo; el de unidades es el más honesto. Ninguno se pondera por estrato. Se juzga si la cita está en el texto de la unidad y si el destino es el punto citado; la atribución del origen (D1) y el reparto a los nodos del destino son de diseño (`docs/plan_remite_a.md`).

### (iii) Tipos documentales mal asignados (observación, no error)

- 4 nodos `Comunicacion` en 2 unidades: `cap::6.1.4.2` N1 «Punto 6.6.2» (punto del mismo TO, código 6.6.2); `cap::6.1.4.2` N2 «Punto 6.6.3» (punto del mismo TO, código 6.6.3); `pro::S5` N1 «Tramitación de sumarios cambiarios» (ley, código Ley 19.359); `pro::S5` N2 «Régimen disciplinario BCRA» (ley, código Leyes 21.526 y 25.065).

## 3. Las 10 unidades con error

| n | Unidad | Estrato | Estado | Elemento no sostenido | Clase |
|--:|---|---|---|---|---|
| 1 | `cap::5.4.5` | ítems | `completo_ok_directo` | A1 (arista) | relación no sostenida |
| 2 | `ext::3.17.3.4` | ítems | `aceptado_con_residuales` | A1 (arista), A2 (arista) | relación no sostenida |
| 10 | `ctacte::6.1.2.5` | ítems | `aceptado_con_residuales` | N2 (nodo), A1 (arista) | causal de rechazo leída como prohibición |
| 15 | `ext::7.9.1.1` | ítems | `completo_ok_directo` | N2 (nodo) | permiso leído como deber |
| 17 | `ctacte::6.1.2.7` | ítems | `aceptado_con_residuales` | N3 (nodo), A2 (arista), A1 (arista) | causal de rechazo leída como prohibición |
| 21 | `lingob::2.3.2.1` | ítems | `aceptado_con_residuales` | A1 (arista) | relación no sostenida |
| 37 | `ext::7.3.11` | no ítems | `aceptado_tras_reintento` | N4 (nodo), A3 (arista) | permiso leído como deber; sujeto equivocado |
| 40 | `ext::10.2.4::cierre` | no ítems | `aceptado_tras_reintento` | N1 (nodo) | rótulo y tipo invertidos |
| 42 | `ctacte::1.5.2.9` | no ítems | `aceptado_tras_reintento` | N9 (nodo) | deber acotado leído como prohibición |
| 43 | `ctacte::9.1.3` | no ítems | `completo_ok_directo` | A3 (arista) | relación no sostenida |

Por qué no se sostiene cada elemento (A1 de `ext::3.17.3.4`, de la segunda lectura, por la decisión 2; los demás, de la primera, confirmados):

- `cap::5.4.5` A1: N5 —exceptua→ N8 hace del reconocimiento parcial una excepción a la regla de no reconocer la CRC con plazo original inferior a un año o residual no mayor a tres meses; el texto no exceptúa esa regla: el reconocimiento parcial rige cuando el cómputo es factible, es decir, para la CRC con descalce que la regla anterior no excluye.
- `ext::3.17.3.4` A1: N1 —condicion_de→ N3: la condición «beneficiario directo del Decreto 277/22» condiciona la emisión de las certificaciones del Decreto 277/22 (encabezado 3.17.3: «En el caso de que el cliente sea un beneficiario directo…, la entidad podrá emitir…»), no el concepto que se deduce del tope.
- `ext::3.17.3.4` A2: N3 —limita→ N2 limita la emisión de las «Certificaciones de aumento de exportaciones de bienes» (punto 3.18), que en el texto son el concepto que se deduce; lo que el tope limita es la emisión de las certificaciones del Decreto 277/22 («podrá emitir… por hasta el monto… neto de…», encabezado 3.17.3).
- `ctacte::6.1.2.5` N2: Restriccion «Prohibición — firmante inhabilitado en Central»: el texto define un defecto formal, causal de rechazo del cheque (encabezados 6.1 y 6.1.2), no prohíbe emitir.
- `ctacte::6.1.2.5` A1: N2 —prohibe→ N1 (emisión de cheque): misma razón.
- `ext::7.9.1.1` N2: Obligacion «Habilitación aplicación cobros exportaciones»: el texto habilita («estará habilitada»), es un permiso; leído como deber (como ext::8.5.13.2 en T4).
- `ctacte::6.1.2.7` N3: Restriccion «Prohibición giro sobre librador»: el texto define un defecto formal, causal de rechazo (encabezados 6.1 y 6.1.2), no prohíbe girar.
- `ctacte::6.1.2.7` A2: N3 —prohibe→ N2: misma razón.
- `ctacte::6.1.2.7` A1: N1 —exceptua→ N3 exceptúa una prohibición que el texto no establece; la salvedad es del defecto formal.
- `lingob::2.3.2.1` A1: N1 —condicion_de→ N2 hace de los conflictos de intereses el supuesto de la obligación; en el texto son la situación que los procedimientos deben prevenir o limitar («tales como»): la obligación no se aplica cuando hay conflicto.
- `ext::7.3.11` N4: Obligacion «Certificación proporcional — múltiples entidades liquidadoras»: el texto dice «cada una podrá certificar», una facultad leída como deber.
- `ext::7.3.11` A3: N3 —aplica_a→ N9 atribuye el deber de «contar con la certificación de la entidad que cursó la operación de canje y/o arbitraje» a esa misma entidad, que es la que emite la certificación, no la que debe contar con ella.
- `ext::10.2.4::cierre` N1: Definicion rotulada «Deuda comercial por importación de bienes» con el contenido de las deudas que NO encuadran como comerciales; y el texto no define: fija el régimen aplicable a esos pagos (el de los préstamos financieros).
- `ctacte::1.5.2.9` N9: Restriccion de tipo prohibicion «No verificar autenticidad de firma de endosantes»: el texto acota el deber («la regularidad de la serie de endosos pero no la autenticidad de la firma»), no prohíbe verificarla.
- `ctacte::9.1.3` A3: N2 —condiciona→ N3 hace del cierre de cuentas un requisito del rechazo de cheques; en el texto es al revés: el rechazo sin percibir las multas es el supuesto del deber de cerrar.

Por clase: relación no sostenida, 5 elementos en 4 unidades; causal de rechazo leída como prohibición, 5 elementos en 2 unidades; permiso leído como deber, 2 elementos en 2 unidades; sujeto equivocado, 1 elemento en 1 unidad; rótulo y tipo invertidos, 1 elemento en 1 unidad; deber acotado leído como prohibición, 1 elemento en 1 unidad. Una unidad puede tener elementos de más de una clase (`ext::7.3.11`).

## 4. Descriptivo por estado y por TO (sin inferencia)

| Estado | ítems | no ítems | los dos |
|---|--:|--:|--:|
| `aceptado_con_residuales` | 4 de 14 | 0 de 5 | 4 de 19 |
| `aceptado_tras_reintento` | 0 de 2 | 3 de 6 | 3 de 8 |
| `completo_ok_directo` | 2 de 14 | 1 de 19 | 3 de 33 |

| TO | ítems | no ítems | los dos |
|---|--:|--:|--:|
| `ext` | 2 de 16 | 2 de 9 | 4 de 25 |
| `cap` | 1 de 4 | 0 de 6 | 1 de 10 |
| `ctacte` | 2 de 6 | 2 de 4 | 4 de 10 |
| `cla` | 0 de 2 | 0 de 3 | 0 de 5 |
| `ric` | — | 0 de 4 | 0 de 4 |
| `lingob` | 1 de 1 | 0 de 1 | 1 de 2 |
| `pro` | 0 de 1 | 0 de 1 | 0 de 2 |
| `docvig` | — | 0 de 1 | 0 de 1 |
| `pagjub` | — | 0 de 1 | 0 de 1 |

Las cuentas por estado y por TO no se ponderan ni llevan intervalo: las celdas son chicas y el sorteo no se estratificó por ellas.

## 5. Omisiones, dudas y observaciones

- **Omisiones, aparte** (no cuentan como error; las registró la primera lectura, sin adjudicar): en 19 de 30 ítems y 9 de 30 no ítems. 7 unidades no aportan ningún nodo de contenido: `ext::11.1.3.9`, `ext::11.1.3.1`, `ctacte::4.5.2::intro`, `docvig::1.2.1`, `lingob::1.3::intro`, `ctacte::10.2.2::intro`, `ext::11.1.1::intro` (bloques de apertura de lista y renglones de datos).
- **Dudas, como observaciones** (adjudicación): 9 unidades; no cambian ningún veredicto.
  - `cap::5.4.5`: «Cuando en estos casos sea factible el cómputo» admite una lectura literal en la que «estos casos» son los excluidos; con esa lectura el texto se contradice («no será reconocida» y «será parcial»).
  - `ext::8.5.17.14`: la descripción de N3 aplica la condición del área franca también a las exportaciones «al resto del territorio de la Nación», que el texto no condiciona; N2, la Excepcion, la limita bien al área franca.
  - `ext::14.2.1.6`: A3 resuelve el titular de la Potestad con la mención «entidades financieras locales», que en el texto son las que otorgaron la financiación; el titular es «las entidades» del encabezado 14.2.1. La clase resuelta (Entidades financieras) incluye al titular: la doy por sostenida (R2), pero puede leerse como sujeto equivocado (R1).
  - `lingob::2.3.2.1`: la modalidad: 2.3 enmarca el punto como buena práctica («se considera como buena práctica que el Directorio…»); N2 va como Obligacion sin esa marca. No lo cuento porque «se asegurará» es categórico.
  - `cap::6.1.4.2`: la descripción de N4 («facultad de elegir») no recoge «según corresponda», que acota la elección; el tramo sí lo trae.
  - `ext::10.2.4::cierre`: la propiedad `termino` sí nombra bien el concepto («deudas… que no encuadren como deudas comerciales»); el error está en el rótulo y en el tipo.
  - `ctacte::9.1.3`: puede leerse como lectura laxa de un predicado (R2); la cuento porque invierte el sentido.
  - `cap::8.2.2.2`: la descripción agrega «en los casos de consolidación, se incluyen también en este concepto»: el texto («Además, en los casos de consolidación, incluye:») abre la lista siguiente; el agregado no contradice el texto, pero no lo dice.
  - `pro::S5`: N3 tipa como Obligacion la sujeción a sanciones («serán pasibles»); el esquema no tiene un tipo para la sanción y la descripción es fiel.
- Las demás observaciones de la primera lectura (tipos cercanos, lecturas laxas, menciones no literales) están por unidad en el campo `observaciones` de `veredictos_l1.jsonl`.

## 6. Solapamiento con T4

6 de las 60 unidades ya se habían leído en T4 de U-REEXT-T0 (no se excluyen, §3): `ctacte::6.1.2.7` (punto 8, omisiones; con error); `ext::10.3.2.1` (punto 8, omisiones; sin error); `ext::2.6.1.2` (punto 3, copia de la nota de E3 y punto 6, listas; sin error); `ext::7.3.11` (punto 3, copia de la nota de E3; con error); `lingob::2.3.2.1` (punto 8, omisiones; con error); `pagjub::1.6` (punto 3, copia de la nota de E3; sin error). En el punto 3 de T4 se leyó la copia de la nota de E3, en el 6 las listas y en el 8 las omisiones, no la unidad entera con el criterio de este reporte.

## 7. Declaración sobre `cla::1.2.1`

Antes del sello, para conocer el formato, la instancia abrió el chunk de E0 de `cla::1.2.1` (encabezados y 200 caracteres del texto), y esa unidad salió en la muestra (no ítems, 4 del sorteo). La semilla la fija la firma y el sorteo no depende de lo que se mire, así que la unidad no se reemplaza (decisión 3). Las dos lecturas la dan **sin error**: la primera, la de la instancia, y la segunda, la de la mesa a ciegas, coinciden.

## 8. Vigilancia por tanda (para el pre-registro de la tanda 1; no se edita aquí)

- **Muestra:** 60 unidades aceptadas por tanda, en dos estratos (ítems y no ítems, por `prompt_r2b.es_item`), 30 por estrato (decisión 2 al firmar), con el mismo método de sorteo (`random.Random(f"{semilla}:{estrato}").sample(sorted(ids), 30)`, con la semilla sellada antes de leer; la fija el pre-registro) y el mismo criterio (§1, con el alcance de la decisión 1 de la nota al pie).
- **Las tres cifras por tanda:** (i) la tasa por unidad, por estrato con Wilson y ponderada con los pesos de la tanda (y el conservador); (ii) las `remite_a` no sostenidas por cita y destino, por aristas y por unidades; (iii) los tipos documentales mal asignados, contados como observación.
- **Umbral de atención:** el límite inferior de Wilson de la tanda por encima del límite superior de la tanda 0, por estrato y ponderado. Con la tanda 0: ítems, LI de la tanda > 0,3731 (con 30 unidades, desde 17 con error); no ítems, LI > 0,2968 (desde 14 de 30); ponderado, con el intervalo conservador, LI conservador de la tanda > 0,3291 (el conservador es el intervalo ponderado hecho con límites de Wilson; si el pre-registro prefiere el intervalo ponderado del §5, el límite superior de la tanda 0 es 0,2543).

## 9. Reproducción

Desde la raíz de una copia del repo sin enlaces (CLAUDE.md §4.l), con las salidas en `lectura_aceptadas/`:

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/lectura_aceptadas/l2_estimadores.py --sellos data/experiment/lectura_aceptadas/sellos_l0.json --veredictos data/experiment/lectura_aceptadas/veredictos_l1.jsonl --fichas data/experiment/lectura_aceptadas/fichas_l1.jsonl --adjudicacion data/experiment/lectura_aceptadas/adjudicacion_autora_l2.json --adjudicacion-sha256 ad99a2f61b7a52f9a4a809e637981fba27ba99f6ffc05981653ce70ba2a4b070 --tasas-t4 data/experiment/reext_t0/t4/salida/tasas_t4.json --salida <directorio>
```

Insumos (sha256): `sellos_l0.json` `640cb1f43ffdf642…`; `veredictos_l1.jsonl` `ea932459d11fff16…`; `fichas_l1.jsonl` `5fac796e4bb1c073…`; `adjudicacion_autora_l2.json` `ad99a2f61b7a52f9…`; `tasas_t4.json` `f9a459a7d1926682…`. Script: `a3b8908781a4587b…`.
