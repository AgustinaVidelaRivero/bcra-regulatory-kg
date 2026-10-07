# Procedimiento: qué se corre cuando crece el catálogo de resolución (U-RERESOL-CAT, R2, punto 4)

Rige con la enmienda 4 al protocolo entre tandas firmada (hoy BORRADOR). Costo de API: cero. Todo corre sobre una copia
del repo sin enlaces, con el sha256 de los archivos del repo antes y después (CLAUDE.md §4.k y §4.l).

**Qué crece y qué no.** Crece solo el catálogo de resolución: el del request (`catalogo_sujetos_r2.json`) más una lista
de ampliaciones que solo agrega (alta de un id con su padre, alta de un alias) y las entradas del registro de alcance por
tanda (`catalogo_unico/registro_alcance_por_tanda.md`: clase o rol reutilizado de un documento nuevo). El request de E1 no
cambia por el catálogo: el bloque, el enum y el tool schema salen del request. Lo agregado actúa por las reglas sobre la
mención guardada; el modelo no lo sugiere (L-ESQ-R2 §7). En la release siguiente, todo pasa al request y la lista vuelve a cero.

**La parte A de la enmienda 6** (firmada el 06/10/2026; la cadena la aplica en r2b). En un documento sin alcance, la
expresión colectiva de la lista de R3 y la relación sin mención o con una mención que no verifica van a cuarentena con la
sugerencia del modelo guardada. Cuando el documento recibe alcance (registro de alcance o release), el script las resuelve
con la regla de la cadena: R1; si no, la sugerencia guardada (R4), aunque la mención no verifique (esas filas conservan su
marca y se cuentan aparte); sin sugerencia, R3. Una fila sin mención en cuarentena es condición con disparador: si aparece,
se frena (`parte_a.filas_sin_mencion_en_cuarentena` del reporte).

**1. Candidatas (al cierre de la tanda).** Del registro acumulado, las claves con la mención verificada en cuarentena en
al menos 2 unidades distintas (enmienda 4, §1.2; `r2_1_medicion.py`, sección `umbral`), ninguna colectiva. Cada una se
lee contra el texto (lectura asistida, declarada) y entra solo con la aprobación de la autora, como alias o id nuevo.

**2. Las entradas.** La lista de ampliaciones (JSON `ampliaciones_resolucion_r2/1`, con el sha del request, y por alta la
operación, el id, el padre o el alias, la evidencia y la aprobación) y, para el alcance, las filas de la tanda en el
registro de alcance, que se lee tal como está (`reresolver_catalogo.py registro`: forma legible por código).

**3. Componer** (en la copia): `reresolver_catalogo.py componer --ampliaciones <lista> [--registro-alcance <md>
--tandas <n>] --salida <G>`: generados de resolución y manifiesto (candado de `r1_e4.catalogo_resolucion_r2`). Se revisa
`reporte_composicion.json`: claves que pasan a ambiguas o cambian de id (se leen antes de seguir) y alcances nuevos.

**4. Re-resolver y rehacer el grafo** (en la copia, dos veces, en dos directorios): `reresolver_catalogo.py correr
--manifiesto <M> --entrada <crudo> --e0-r2 <E0> --anterior <ensamblado anterior>/r2 --generados-resolucion <G>
[--generados-anterior <G0>] [--sin-cola] --salida <S>`: (a), (a+) y (b), contraste, registro acumulado y gate.

**5. Qué se verifica.**
- `no_explicado` vacío (código 0); las dos corridas, byte a byte (rutas de salida normalizadas).
- (a+) reproduce la decisión guardada; (a) es idempotente y coincide con (a+) en la cuarentena; la resolución de (b) es la
  de (a+), relación por relación, con el sha del compuesto.
- Registro acumulado: lo sin resolver es lo de (b) salvo la versión; el destino de cada resuelta, el de (b); las filas de
  (b) fuera del anterior se listan y se leen. Cero rechazos de E2 por `sujeto_id_fuera_de_catalogo`.
- Archivos: solo cambian el grafo, los registros, el reporte y los registros por TO; con alcance nuevo, los propuestos del
  documento toman el rol como padre por defecto.
- Gate: shapes r2 con los ids de S19 de G sin bloqueantes en FAIL; LN-6 resuelto con `--generados-resolucion G`; los ítems
  de la suite que cambian de estado, explicados. Se leen las relaciones del modelo que cambian de destino.
- El código sin `--catalogo-resolucion` reproduce los ensamblados sellados (`controles_r2_1.sh`); con un registro de
  alcance nuevo, el mensaje de E1 de toda unidad ya extraída sale byte a byte igual (`r2_2_medicion.py`).

**6. Qué se reporta con la tanda (P-d4).** Los tres sha (request, ampliaciones, compuesto) y el del registro de alcance;
las ampliaciones con su evidencia y su aprobación; las relaciones por `catalogo_sha256` y las filas del registro por versión
de entrada y de resolución (`resueltos_por_version`); la sección `parte_a` (cuarentena con sugerencia por motivo, resueltas
por R4 con mención que no verifica, filas sin mención); las relaciones del modelo que cambiaron de destino, con su lectura.

**7. Después.** El grafo nuevo pasa por el circuito de sello de la tanda (fixture de la suite, `grafos.py`). La lista de
ampliaciones y los generados de resolución se commitean con él. Antes de extraer la tanda 1, con la enmienda 4 firmada,
`prompt_r2b.py` tiene que leer el registro de alcance al armar el mensaje (hoy no lo lee).
