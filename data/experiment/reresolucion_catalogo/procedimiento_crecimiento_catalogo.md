# Procedimiento: qué se corre cuando crece el catálogo de resolución (U-RERESOL-CAT, R2, punto 4)

Rige con la enmienda 4 al protocolo entre tandas firmada (hoy BORRADOR). Costo de API: cero. Todo corre sobre una copia
del repo sin enlaces, con el sha256 de los archivos del repo antes y después (CLAUDE.md §4.k y §4.l).

**Qué crece y qué no.** Crece solo el catálogo de resolución: el catálogo del request (`catalogo_sujetos_r2.json`) más
una lista de ampliaciones que solo agrega (alta de un id con su padre, alta de un alias de un id que existe). El request
de E1 no cambia: el bloque del prefijo, el enum y el tool schema salen del catálogo del request. Lo agregado actúa por las
reglas sobre la mención guardada y el modelo no lo sugiere (L-ESQ-R2 §7). Una mención que no verifica nunca resuelve por
crecimiento. En la release siguiente, las ampliaciones pasan al catálogo del request y la lista vuelve a cero.

**1. Candidatas (al cierre de la tanda).** Del registro acumulado de la tanda, las claves con la mención verificada en
cuarentena en al menos 2 unidades distintas (enmienda 4, §1.2; tabla en `r2_1_medicion.py`, sección `umbral`). Ninguna
puede ser una expresión colectiva (R1 se evalúa antes y le ganaría a R3). Cada candidata se lee contra el texto (lectura
asistida, declarada) y entra solo con la aprobación de la autora, como alias o como id nuevo con su padre.

**2. La lista de ampliaciones.** Un JSON de formato `ampliaciones_resolucion_r2/1` con el sha256 del catálogo del
request y, por alta, la operación, el id (y el padre o el alias), la evidencia (claves del registro) y la aprobación.
Propuesta de ubicación: `catalogo_unico/ampliaciones_resolucion_r2.json` y `catalogo_unico/generados_resolucion_r2/`,
creados con el primer crecimiento aprobado.

**3. Componer** (en la copia): `reresolver_catalogo.py componer --ampliaciones <lista> --salida <G>`. Escribe los
generados de resolución y su manifiesto, que es el candado de `r1_e4.catalogo_resolucion_r2`. Se revisa
`reporte_composicion.json`: claves que pasan a ambiguas o que cambian de id. Si hay alguna, se lee antes de seguir.

**4. Re-resolver y rehacer el grafo** (en la copia, dos veces, en dos directorios):
`reresolver_catalogo.py correr --manifiesto <M> --entrada <crudo> --e0-r2 <E0> --anterior <ensamblado anterior>/r2
--generados-resolucion <G> [--generados-anterior <G0>] [--sin-cola] --salida <S>`. Corre (a), (a+) y (b), contrasta y
escribe el registro acumulado y el gate.

**5. Qué se verifica.**
- `no_explicado` vacío (código de salida 0); las dos corridas, byte a byte (rutas de salida normalizadas).
- (a+) reproduce la decisión guardada en todas las relaciones; (a) es idempotente y coincide con (a+) en la cuarentena.
- La resolución de (b) es la que predice (a+), relación por relación; todas las relaciones llevan el sha del compuesto.
- Registro acumulado: lo que sigue sin resolver es lo de (b) salvo la versión; el destino de cada fila resuelta es el de
  (b); las filas de (b) fuera del registro anterior se listan y se leen.
- Cero relaciones rechazadas en E2 por `sujeto_id_fuera_de_catalogo`.
- Archivos de la salida: solo cambian el grafo, los registros, el reporte y los registros por TO (en los TOs sin cambios,
  solo la versión del catálogo).
- Gate: shapes r2 con los ids de S19 de G, sin bloqueantes en FAIL; LN-6 resuelto con `--generados-resolucion G`; los
  ítems de la suite que cambian de estado, explicados.
- Se leen las relaciones que resolvió el modelo y cambian de destino (en (a+), tipo «destino» fuera de la cuarentena).
- El código sin `--catalogo-resolucion` reproduce los ensamblados sellados (`controles_r2_1.sh`).

**6. Qué se reporta con la tanda (P-d4).** Los tres sha (request, ampliaciones, compuesto); las ampliaciones con su
evidencia y su aprobación; las relaciones por `catalogo_sha256` y las filas del registro por versión de entrada
(`catalogo_sha256`) y de resolución (`catalogo_sha256_resolucion`), en `resueltos_por_version` del reporte; las filas
resueltas, las relaciones del modelo que cambiaron de destino, con su lectura, y las que siguen en cuarentena y por qué.

**7. Después.** El grafo nuevo pasa por el circuito de sello de la tanda (fixture de la suite, registro en
`grafos.py`), como cualquier ensamblado. La lista de ampliaciones y los generados de resolución se commitean con él.
