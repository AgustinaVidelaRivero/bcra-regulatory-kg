# U-R2-CODIGO — decisiones sobre el FRENO R3: aplicadas 1 a 4, FRENO en la 5

Fecha: 02/10/2026. Sin commit (commit PENDIENTE de la autora). USD 0. R3 está commiteada en `91fe4b9`.
Apliqué las decisiones 1 a 4 en su orden y me detuve en la 5: el desglose encontró pérdidas reales. La 6 no pide
acción (la pasada residual de E4 se sigue midiendo). No arranqué los agregados 7 a 9 ni R4.

## Error propio, con su causa

En R3 (`91fe4b9`), `r1_referencias._texto_e0_de` tomaba como texto de una procedencia de herencia solo el tramo
cuyo tipo nombra el rol (`herencia_encabezado`), y para un mini-chunk solo su texto propio. Pero
`comun_e1.rol_documental_de_punto` rotula la procedencia con el primer tramo de la unidad, así que el resto del
texto del punto quedaba afuera; y E0 deja el encabezado del propio punto en la herencia de sus mini-chunks
(«7.9.2. Las operaciones de los puntos 7.9.1.1. a 7.9.1.3. …»). Ahora el texto del punto es todo tramo de esa
unidad que el chunk hereda más, si la procedencia es el punto propio o un bloque, el texto del chunk
(`selftest_r3.py`, T2i y T2j). Con el error, las remisiones selladas que la regla firmada no reproducía eran 279,
296 y 235 (desarrollo, diez, r1) y los pares perdidos contra la paráfrasis, 656; corregido, son 119, 132, 128 y
245 (§ decisión 5). Los números de R3.d de `r3_freno.md` quedan reemplazados por los de abajo.

## Decisión 1 — arrastre de K

En e0-r2, todo lo que precede en la zona a la última línea con «B.C.R.A.» o de sección (incluida) es encabezado;
la regla de repetición rige solo después (`e0_lib.separar_encabezado_pie`, `forzadas`).
- Tanda 0: se conservan las mismas 5 líneas (cap 1, ext 2, ric 2; los otros siete TOs, 0).
- E0 legada 34/34; la salida e0-r2 de la tanda 0 es idéntica a la de R3 (47 archivos), así que el censo R1.d no
  cambia (39 requests, USD 0,6474).
- Censo fuera de muestra recomputado (`rk_fuera_de_muestra.json`, 145 TOs, doble corrida idéntica): 187 líneas
  en 23 TOs, 184 de contenido y 3 de encabezado, las tres después de la línea «B.C.R.A.»: `micemp` p3 «PEQUEÑA O
  MEDIANA EMPRESA», `ri_ai` p3 «CONCEPTOS. (R.I. – A.I.)», `ri_tsa` p92 «INFORMACIÓN PARA LA COOPERACIÓN TRIBUTARIA
  INTERNACIONAL». Ninguna línea de sección queda en el cuerpo. Páginas de cuerpo cuya zona no tiene «B.C.R.A.» ni
  sección: 12 en 2 TOs (`ri_ccna`, 11 páginas de fórmulas modelo con 19 líneas conservadas, todas de contenido;
  `ri_rml`, 1 página sin líneas conservadas).

## Decisión 3 — brechas del modelo, al grafo

`modelos_r2.py` (y nada más de pyd_r2/ salvo su selftest):
- nodo del grafo (`NodoR2`, con `PROPS_NODO_POR_TIPO`): `cola_humana`, `cola_chunks`, `estado_e3` y
  `colision_cross_to` en `properties`, con la forma de los grafos sellados (`r1_cola_flaggeada.flaggear_grafo`,
  `r1_invariantes.merge_grafos_guardado`). Agregué `cola_chunks` porque es parte de la misma marca sellada. La
  entidad de E1 (`EntidadR2`) no las admite. En el perfil r2 la marca de cola sigue el `chunk_id` de la procedencia
  (`e2_lib.flaggear_cola_r2`), no la clave (to, punto, rol) de la cadena r1;
- elemento de umbral: `base_destino`, `base_via` (remision o definicion), `base_no_resuelta` y
  `verificado_en_tabla`;
- arista de sujeto: `calificador`;
- `AristaR2`: `subclase_de`, `miembro_de`, `instancia_de`, `parte_de` y `padre_sugerido`, con firma
  Sujeto → Sujeto (`firma_esqueleto`, `firma_arista`).

Controles: `selftest_pyd_r2` 296/296 (249 + 24 de G11 + 23 de G12); tool schema y enums de E1 byte a byte los de
57a8dd2. Prueba de cla con el perfil r2: 595 nodos, 1.129 aristas, **0 nodos y 0 aristas fuera del modelo** (cada
arista validada también por su firma con los tipos de sus extremos); 22 nodos y 32 aristas marcados por los dos
chunks de cola; el elemento de `cla::5.1.1.1` lleva `base_destino = cla::3.7`, `base_via = remision`. Sin
`marcas_r2.json` ni `umbrales_r2.jsonl`; las variantes del TextoOrdenado siguen en `e4_conflictos.json`.

## Decisión 4 — evidencia en límite de palabra

`evidencia_literal` extiende el tramo hacia afuera hasta el límite de palabra en los dos extremos; un número con
puntos («3.7.1») y un corte de palabra al final de línea («nor-\nmas») cuentan como una palabra. En cla, 177 de
177 evidencias de `remite_a` son literales del texto de E0 de su procedencia y ninguna empieza ni termina en la
mitad de una palabra. Ejemplo: «equivalente a dos veces el importe de\nreferencia establecido en el punto 3.7. y
cuyo repago no se».

## Decisión 5 — remisiones que se pierden: FRENO

Dos cifras que no se mezclan (`r3_perdidas_remisiones.json`, doble corrida idéntica; la causa de cada par y la
lectura de cada cita, en el JSON):
- **A. Remisiones de los grafos sellados que la regla firmada no reproduce.** En R3 eran 279 (desarrollo), 296
  (diez) y 235 (r1); con el texto del punto corregido son **119, 132 y 128**.
- **B. Pares del conjunto por paráfrasis con los siete tipos de origen** (variante de la simulación de
  U-AUDIT-TIPOS-V3, 7.929 pares en desarrollo) que la regla firmada no reproduce: **245**. El 656 de R3 se midió
  contra el conjunto con cada procedencia y `termino` (7.940); contra ese conjunto también son 245 hoy.

Veredictos (pares / citas distintas; cita = procedencia y unidad de destino):

| veredicto | A desarrollo | A diez | A r1 | B desarrollo |
|---|--:|--:|--:|--:|
| queda desde otro punto (punto superior o chunk emisor) | 80 / 14 | 80 / 14 | 75 / 15 | 169 / 27 |
| corrección | 9 / 1 | 18 / 2 | 6 / 1 | 18 / 3 |
| corrección, con destino nuevo falso | — | — | 16 / 1 | 8 / 1 |
| no es una cita del texto (la paráfrasis nombra el punto padre o enumera) | 4 / 1 | 4 / 1 | 22 / 7 | 13 / 2 |
| **pérdida real** | **21 / 6** | **25 / 7** | **9 / 4** | **32 / 8** |
| **pérdida real, anáfora sin número** | **5 / 1** | **5 / 1** | — | **5 / 1** |
| total | 119 | 132 | 128 | 245 |

Corrección de lo que reporté antes: no toda «cita a otra norma» es una corrección. Las pérdidas reales, por cita:
1. `cap::6.2.1.1` → `cap::2.12.3.1` (A desarrollo, diez, r1; B): celdas de la tabla linealizada entre «punto» y el
   número («del punto Plazo residual 1,6% 2.12.3.1.»); con e0-r2 la tabla se serializa y la cita se lee entera.
2. `cap::8.2.2.3` → `cap::8.3.5` (A los tres; B) y `cap::7.1` → `cap::7.1.2` (A r1; B): una línea suelta entre
   «punto» y el número («punto\nn1\n8.3.5.», «punto\ni\n7.1.2.»). La «n1» es un subíndice: en la página 156 del PDF
   de cap las seis líneas «n1» empiezan entre x0 293,9 y 521,4, dentro del renglón, y E0 las ordena por altura. Que
   la «i» sea el subíndice de «α» es NO VERIFICADO.
3. `ext::7.9.1.3` → `ext::3.6.1.4` y `3.6.1.5` (A desarrollo, diez; B): «en los puntos 3.6.1.3.\n(únicamente
   cuando … a partir del 16/10/20) a 3.6.1.5.»: el paréntesis corta el rango.
4. `cla::5.1.2.3` → `cla::3.7` (A los tres; B): «establecido en el punto 3.7.– y a microemprendedores (según lo
   previsto en el punto 1.1.3.4. de las normas sobre “Gestión crediticia”)»: la ventana de 120 caracteres atribuye
   también el 3.7 a la norma nombrada después de otro punto, y la cita queda irresoluble.
5. `ric::3.1.6` → `cap::4.2.1.3` (A desarrollo, diez; B) y `ric::3.1.2` → `cap::4.1.1` (B): «del punto 4.2.1.3. de
   las citadas disposiciones», «del punto 4.1.1. de las citadas normas»: la anáfora de la norma no se reconoce y
   la cita se resuelve como interna (`ric::4.2.1.3`, `ric::4.1.1`), una remisión falsa nueva.
6. `ctacte::12.2.3.1` → `ctacte::12.2.3.2` (A diez): «salvo lo previsto en el apartado 12.2.3.2.»: la cita usa
   «apartado».
7. `ext::10.11.7.3` → `ext::10.11.7` (A desarrollo, diez; B), anáfora sin número: «en el marco de los mecanismos
   previstos en este punto»; remite al punto que lo contiene sin nombrarlo, y la regla firmada solo toma citas con
   número. La marco como pérdida para que decidas si entra.

Hallazgo aparte (corrección con destino nuevo falso): `ric::9.1.1` cita la Sección 2 de las normas sobre
«Incumplimientos de capitales mínimos y relaciones técnicas», fuera del inventario. La remisión sellada a
`ric::S2` era falsa, pero el inventario resuelve esa norma a `cap` porque su nombre contiene «capitales mínimos»
(`r1_referencias.resolver_norma`, coincidencia por subcadena), y la regla firmada crea `cap::S2`.

Propuestas, no implementadas (solo en el perfil r2; `RE_PUNTOS`, `RE_DICHO`, la ventana y el inventario son de la
cadena r1 y cambiarlos rompería la reproducción de lo sellado):
- (a) subíndices: en e0-r2, unir al renglón la línea de uno o dos caracteres alfanuméricos cuyo x0 cae dentro del
  renglón vecino; o tolerar en el detector r2 una línea suelta de hasta dos caracteres entre «punto» y el número;
- (b) tablas: detectar sobre el texto de e0-r2, con la tabla serializada;
- (c) rangos: admitir un paréntesis entre los elementos de una lista o de un rango;
- (d) ventana: no atribuir a una norma los puntos que están antes de otro punto más cercano a ella;
- (e) anáfora de la norma: «de las citadas normas», «de las citadas disposiciones» y variantes resuelven a la
  última norma nombrada en el punto (como hoy «de dicho ordenamiento»), y si no hay ninguna, la cita queda
  irresoluble en vez de interna;
- (f) «apartado» como forma de cita, igual que «punto»;
- (g) inventario: comparar el nombre de la norma completo y no por subcadena;
- (h) «este punto»: decidir si entra como remisión al punto que lo contiene.

## Lo demás

- R3.d recontado con el texto del punto corregido (`r3d_remisiones.json`): simulación 4.242 sellados con 4 tipos
  y +3.687/0 con 7 (igual); pasos: `termino` +0, cada procedencia +11, texto de E0 con D1 +4.952 y −245 pares.
  Desarrollo con la regla firmada: 1.203 citas resueltas (1.149 interna, 46 externa, 8 to_entero), 354
  irresolubles (punto sin nodos 175, norma fuera del inventario 136, punto inexistente en E0 28, autorreferencia
  15), 12.647 aristas. D1: 949 menciones a los nodos que contienen la unidad, 186 a todos los del punto.
  `cla::5.1.1.1` → `cla::3.7` y `cap::8.2.3.3` → `cla::6.5.1`/`cla::7.2.1` siguen. Diez, 4 tipos y procedencia
  primaria: 28 pares solo de la paráfrasis, 1.265 solo de E0, 857 en ambos; 732 orígenes cambian de destino.
  Condicion aisladas con remisión: 9 con la paráfrasis, 10 con la regla firmada. Comunicaciones: sin cambio.
- Pasada residual de E4: medida y no aplicada (cla: 1 propuesto, 0 resoluciones).
- Ensamblados sellados reproducidos con el código nuevo (`r1/kg.json` eab2fdd0, dd42d6d9, 4097d4fd).
- Selftests: repo — `selftest_pyd_r2` 296/296, `selftest_r3` 52/52, `selftest_r2` 18/18, `selftest_e0r2` 31/31,
  `selftest_dirigida_tanda0` 28/28, `selftest_clave_cache` OK, `selftest_regression_kg` 85/85; espejo — E0
  (57, 39, 34, 59, 33), U-B5.3 40/40, cable v3 45/45, corpus 21/21, E2 35/35, `selftest_manifiesto` 32/37 (P5,
  conocido).

## Comandos

`control_post_r3.sh` (paquete): espejo, E0 legada y e0-r2 doble, ensamblados, prueba de cla doble,
`r3d_remisiones.py` y `r3h_lectura_umbrales.py` dobles y selftests. `r3_perdidas_remisiones.py --out` (doble), que
reemplaza al clasificador de la primera versión de este freno.
`rk_fuera_de_muestra.py --max-paginas 300 --out` (doble).
