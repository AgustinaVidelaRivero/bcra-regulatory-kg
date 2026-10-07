# FRENO O1 de U-E3-LISTAS (06/10/2026; USD 0, sin API; sin commit)

Mandato firmado en `d9d8888`. El despacho traía `<HASH_FIRMA_UE3>` sin llenar, así que saqué el hash de `git log`. Todo corrió sobre copias de `d9d8888` armadas con `git archive`, sin enlaces. Paquete: `revision_UE3_LISTAS_FRENO_O1/`, con `manifest.txt`; los archivos citados abajo están ahí.

**Precondiciones: las tres en verde** (evidencia en `UE3_LISTAS_O1_precondiciones.txt`).
- **a.** `git log --oneline -1 -- docs/mandatos/UE3_LISTAS_bloque_de_lista_en_e3.md` da `d9d8888`. El sha256 es `6270ff05…` en la firma y hoy. La línea 1 es el título; «**FIRMADO por la autora el 06/10/2026**» está en la 3.
- **b.** `prompt_e3`, importado desde la copia, pasa sus candados: prefijo `21a836c7de6d`, fixture `e8fa5dc4…`, mensaje `da17c22e…`. Son 13 casos de 6 unidades (no «6 casos»), ninguno ítem.
- **c.** `comun_e3.py:123-125` es `for h in chunk.get("herencia", []): / if h["tipo"] != "encabezado": / continue`, y `prompt_e3.py:315-316` es `if R.es_encabezado_de_lista(chunk): / notas.append(NOTA_E3_ENCABEZADO_LISTA)`. Recomputado con `prompt_r2b`: 1.054 ítems con LINEA_ITEM de 2.440 unidades verificadas.

**Contradicciones con el mandato (mandan los archivos).**
1. `reports/u_diag_e3_listas/` (mandato `:4-5`) no está en el repo ni en su historia. Leí el paquete del diagnóstico en el scratchpad de su sesión, con el manifiesto en verde, y lo reproduje sobre `d9d8888`: las 8 salidas dan igual byte a byte, `fase3_efecto.json` incluido.
2. Las «24 unidades afectadas» son 20 distintas: 17 con reintento y 7 en la cola, pero 4 están en los dos grupos (`ext::3.18.1.1`, `ext::3.5.6.1`, `ext::3.6.1.1`, `ext::3.6.4.2`).
3. Pieza 1 en las citas: que el bloque entre solo con la forma r2 exige que `ratchet_e3.py:283` pase la marca, y `ratchet_e3.py` está en PROHIBIDO (D1).
4. Pieza 1, «solo ese bloque»: en 23 ítems el bloque que la abre es el último fragmento de un párrafo que E0 partió (D2).

**Resultados.**
1. **NOTA.** Una sola NOTA con las ramas, porque el tipo de lista no lo decide el código. Una oración cambia según el bloque tenga unidad propia o sea la línea de título (R30, R29). Tiene 1.991 o 2.098 caracteres (`UE3_LISTAS_O1_nota_texto_propuesto.txt`). La tabla tiene 16 cláusulas y usa las 11 reglas, verificada en código (`UE3_LISTAS_O1_nota_tabla_clausula_regla.md`). Ninguno de los 1.054 mensajes trae un centinela de E1.
2. **Fixture.** Propongo `ext::3.5.6.1` (bloque intro; deja afuera el chapeau, la intro de 3.5 y el cierre) y `cap::6.8.3.1` (bloque encabezado), cada uno con y sin la marca: 17 casos de 8 unidades. Con la fixture de hoy, el prototipo pasa el candado viejo: ese es el riesgo. Con la nueva, un espacio de más en la NOTA, quitar la pieza 1 o volver al código de HEAD cambian el sha.
   - Valores propuestos: `CANDADO_MENSAJE_E3_JSON_SHA256_ESPERADO` = `f9590519d03f9957542eb3ee10f2c0f5ecc31abe6c770e828b8af790580977d1`; `MENSAJE_E3_SHA256_ESPERADO` = `a7407ee568c651f1bf4f0b737cfe55e326e448b4c46ad6b1053a4d509d162270`.
3. **Mensaje antes y después** (`UE3_LISTAS_O1_punto3_comparacion_mensajes.json`; comandos en `UE3_LISTAS_O1_comandos.sh`). Cambian los 1.054 ítems. El bloque entra al fuente en 1.015 (intro 982, intersticial 22, chapeau_seccion 11). En los 39 de tipo encabezado el bloque ya estaba, y cambia solo la NOTA.
   - Se agregan 2.396.141 caracteres (bloque 287.020, NOTA 2.109.121), unos 783.104 tokens (3,06 caracteres por token, ajuste sobre 2.438 pedidos de E1): unos USD 1,76 por corrida del tamaño de la tanda 0.
   - Quedan iguales byte a byte los 1.386 no ítems; sin la marca r2, las 2.440 unidades r2b, las 2.427 de v3_b54 y las 1.762 de r1; y los 13 casos del candado.
4. **Lista sellada**: `UE3_LISTAS_O1_lista_unidades_afectadas_tanda0.json`, sha256 `cc6b0cd6c56831c486d60bf7da64712cea391a1eb2948eef822448567df9bab6`, hora 2026-10-06T17:42:48-03:00.
5. **Prueba en seco** (lectura mía, sin el modelo; `UE3_LISTAS_O1_prueba_en_seco_lectura.md`), sobre `cla::5.1.1.1` (b1), `ext::3.6.1.1` (b2) y `polcre::7.1.2` (condiciones, del grupo c de T4). De 5 reclamos, 4 quedan sin base (P, C y B) y 1 sigue, porque no tiene que ver con la lista. Aparece un reclamo nuevo y fundado posible: c3 de polcre, por C15.

**A decisión de la autora** (detalle en `UE3_LISTAS_O1_nota_propuesta_y_decisiones.md`).
- **D1, citas.** Variante A: una línea en `ratchet_e3.py:283`. Variante B: las citas como hoy. Con A, sobre los veredictos de hoy, 37 citas pasan a verificadas y 19 unidades pasan de cola por veredicto inutilizable a reintento. Recomiendo A.
- **D2, fragmentos.** Sumar los bloques contiguos con el mismo rótulo agrega 8.819 caracteres en 23 ítems. Recomiendo sumarlos.
- **D3 y D4.** Reclamar la norma del encabezado vuelta a emitir en el ítem (no la incluí), y el largo de la NOTA.
- **D5, para O2.** A3r de `selftest_clave_cache` daría DISCREPANCIA en los 1.054 ítems (`:498-499`, `:1841`); hay anclas corridas; y el bloque M de `selftest_e3` pasa de 13 casos a 17.

**Controles.** Tomé el sha256 de todo el repo a las 17:19 y a las 17:55.
- `e3_verificador/` (58 archivos), `mantenimiento/` (51) y `e1_extractor/` (41) quedaron iguales.
- Los 148 cambios son de las unidades en paralelo: `neo4j/` 70, `sincola_t0/` 39, `segmentacion_oficial_e0r2/` 25, `ens_*_sincola/` 8, `e0_chunking/` 3 y otros 3. Ninguno es mío. HEAD avanzó a `01046b6` (SC1-bis), que no toca nada de lo que leí.
- 2.213 `.pyc` antes y después. Todo se reproduce desde cero con `UE3_LISTAS_O1_comandos.sh`, salvo la hora de la lista. El grep de convenciones está en `UE3_LISTAS_O1_grep_convenciones.txt`.

Commit PENDIENTE de la autora. Espero el «seguí» escrito; no empiezo O2.
