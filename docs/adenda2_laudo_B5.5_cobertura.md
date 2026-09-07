# Adenda 2 al laudo B5.5 — Ampliación de cobertura a los bloques excluidos

**Estado: FIRMADA — Agustina Videla Rivero, 07/09/2026** (versión enmendada con las tres enmiendas de su laudo del 07/09). Segunda adenda al laudo
`docs/laudo_B5.5_alcance_corpus_y_catalogo.md` (firmado 04/09, `c0daef1`);
el laudo original y la adenda 1 (segmentación universal, firmada 06/09)
se conservan íntegros. Implementación:
`docs/diseno_B5.9_ampliacion_cobertura.md` (en freno de diseño).

## §1. La evidencia que motiva el laudo

Unidades U-COB-EXCL y U-COB-EXCL-2 (adjudicación registrándose en
U-COB-EXCL-3):

1. El instrumento deóntico original **no contaba el futuro impersonal**,
   que es la forma con que este corpus manda. Corregido, la relación
   entre el material excluido y el articulado cayó de **5,58× a 1,56×**.
2. **Lectura a ciegas de 32 páginas** por la autora, con pre-registro
   sellado y enmendado antes de leer: **23 prescriptivo / 9 referencia /
   0 duda**.
3. **Diez de los doce** documentos declarados no segmentables contienen
   contenido prescriptivo. Solo `plandecuentas` y `optico` son referencia
   pura, y son exactamente los dos con densidad deóntica **0,000** en las
   tres variantes del instrumento.

**Conclusión de la autora:** el criterio de forma (¿tiene espina
numerada?) no coincide con el criterio de contenido (¿manda algo?). El
recurso, tal como estaba planificado, excluiría normativa vigente.

## §2. El laudo

**Se amplía la cobertura a los dos bloques hoy excluidos, ANTES del
escalado. Ambos, no uno.**

- **Bloque A — EXTRACCIÓN sobre DIEZ documentos y 41 páginas**
  (enmienda 1 de la autora, recomputada contra `particion_152.json`:
  ri_con 16, ri_spi 11, ri_tii 6, ri_rem 2, y seis de 1 página —
  ri_chr, ri_fcem, ri_itme, ri_pfmipyme, ri_pscpp, ri_pspii; control
  161 − 43 − 77 = 41). **`optico` (43 pág) y `plandecuentas` (77 pág) NO
  se extraen**: ya están adjudicados como referencia pura por la lectura
  a ciegas y son los dos con densidad deóntica 0,000 en las tres
  variantes; se censan para el registro y se DECLARAN. `plandecuentas`
  es además material ficha (76/77 páginas), de modo que esta enmienda
  resuelve su caso y no la herencia del bloque B. Proyección de costo
  recalculada: 41 × 1,38 = **57 unidades ≈ USD 1,10**.
- **Bloque B**: el bloque ficha de los 2 parciales — **2.175 páginas**
  (manual 1.830, ri2_pm 345; ídem verificado).

## §3. Guardas vinculantes (las cinco del laudo, más una del diseño)

1. **Regresión de no-cambio**, como en B5.8: ninguna regla ni unidad
   nueva altera la segmentación ya obtenida — verificación documento por
   documento contra **1.763 / 762 / 6.340 / 9.266**. Diferencia = FRENO.
2. **Esquema congelado**: se verifica sobre muestra pequeña que el
   material nuevo cabe en el vocabulario del laudo `2593d4d` (9 tipos /
   13 relaciones / enum de 6) ANTES de extraer a escala. Si no cabe,
   FRENO y reporte: reabrir el esquema es laudo de la autora, nunca
   efecto colateral.
3. **Modelo de unidad y procedencia — LAUDADO (enmienda 3).** Se aprueba
   el modelo del diseño §2: unidad = bloque de prosa contiguo dentro de
   una página, **sin fabricar espina**; procedencia = documento + página
   + offset; campo `granularidad_procedencia` distinguiendo `punto` de
   `pagina` por elemento. La afirmación de la tesis pasa a «cada
   elemento cita su ubicación en el texto oficial, con la granularidad
   que el documento permite». **EXIGENCIA AGREGADA**: el reporte entrega
   el **conteo exacto** de elementos con procedencia a nivel de página
   sobre el total del recurso, para escribir «N elementos de M, todos
   provenientes de los diez documentos sin numeración» y no una salvedad
   general.
4. **Guarda de volumen** para el bloque B: se mide antes de extraer; si
   el bloque ficha pasara a ser fracción dominante de las unidades del
   recurso, es laudo de la autora y no automático.
5. **Piloto antes de masa** en el bloque B: ri2_pm (345) antes de manual
   (1.830), con techo de gasto declarado por unidad.
6. *(agregada por el diseño, §5)* **Umbral de balance declarado**: si la
   proyección del bloque B supera el **25 %** de las unidades del recurso
   final, su fase de extracción no arranca sin laudo explícito sobre el
   balance del recurso. Convención anterior y auditable, no calibrada.

## §4. Efecto en la secuencia (registrado con todas las letras)

- **El capítulo del esquema y la lectura de mentores NO se detienen**: lo
  que se valida es la metodología y el esquema, no la partición final.
  El tramo 5 narra la partición de B5.8.4 como hecho **y declara el
  hallazgo de cobertura** y la ampliación en curso.
- **La fecha del escalado SÍ se mueve**: del orden de dos a tres semanas
  de trabajo efectivo si ambos bloques van antes, más las adjudicaciones.
- **DECISIÓN DE SECUENCIA (enmienda 2): DESACOPLE.** Bloque A **antes**
  del escalado; bloque B como **release posterior declarada** (principio
  9). El «ambos, no uno» sigue en pie en el qué: B no se abandona, se
  declara con su evidencia medida y su fase B.1 corre cuando el escalado
  esté encaminado. Razones: la superficie real de A es de días y de un
  dólar; A es el único de los dos bloques con evidencia de la autora
  detrás; B exige otra lectura a ciegas antes de extraer una página, que
  es tiempo en la ruta crítica; y su costo no tiene ancla (cota de
  referencia: el escalado completo, ~USD 123). **Efecto sobre la fecha
  del escalado: días, no semanas.** El tramo 5 del capítulo declara el
  hallazgo de cobertura **con la ampliación en dos tiempos**.

## §5. Qué NO cambia

El corpus congelado sigue congelado (principio 9 y regla del inventario
solo-lectura); el esquema sigue congelado salvo laudo propio; los
documentos ya segmentados no se re-segmentan; y el resultado de B5.8.4
(138 / 2 / 12) sigue siendo el hecho verificado sobre el que se escribe
el capítulo, con la ampliación declarada en dos tiempos.

**Nota de coordinación (autora, 07/09): `docs/tesis/main.tex` NO se toca
por nada de esto.** La afirmación sobre la procedencia y el párrafo de la
partición dependen de laudos que recién ahora quedan cerrados, y el tramo
2 está en la mesa de tuneo: **los dos se ajustan en el tramo 5**.

## Firma

**Firma: Agustina Videla Rivero · Fecha: 07/09/2026.** Firmada sobre la versión enmendada: alcance del bloque A en diez documentos y 41 páginas (cuenta verificada por la autora), desacople de secuencia, y laudo del modelo de procedencia con su conteo exigido.
