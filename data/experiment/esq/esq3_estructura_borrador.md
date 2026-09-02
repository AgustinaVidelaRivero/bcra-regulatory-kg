# ESQ-3 — Estructura en dos tiempos (BORRADOR DE MESA, revisión de autora pendiente)

Gate sellado en `docs/plan_tesis.md` (bloque ESQ): lectura conjunta + retoques
+ **laudo de esquema congelado** [LAUDO ESCRITO REQUERIDO — toca compromisos
del PPF/alcance]. Ningún ítem de B5/B6 arranca sin este laudo. Insumos:
tabla de resultados `bbac990`, desvíos `685fc8a` + adenda, escalera
P1/P1′/P1″, calibración `eadf4a5`, scoping D8, cola de mejoras.

## ESQ-3a — Laudo de retoques

1. **Decisión madre (insumo: opinión de mesa; la decide la autora)**:
   ¿ampliación DENTRO del paradigma (escalones 1–2) o cambio de paradigma
   (4–5)? El laudo la registra con su justificación y con la posición
   resultante para la exigencia 10 del mapa de related work (schema-based
   vs schema-light). Los escalones 4–5, si se consideraran, son CONSULTA DE
   ALCANCE a mentores antes de laudar.
2. **Retoques, cada uno anclado a fichas/familias**: por cada cambio
   (agregar/renombrar/fusionar tipo, predicado, valor de subtipo, campo),
   el laudo lista: qué se cambia · fichas/familias que lo motivan (números
   de ficha) · qué firma/candidata ataca · predicción verificable que deja
   para ESQ-3b.
3. **Pronunciamiento explícito sobre (e) hechos con valor**: no promovió
   por criterio (0 azarosas); llega por material propio (`fe1fe36`,
   entrada 5 de la cola). El laudo dice si se trata ahora, se difiere a
   ESQ-RI-3 (secuencia laudada `94bb7a7` §D10), o se resuelve como
   conclusión de diseño en C1.7 — con el porqué.
4. **Triage de las 13 familias q3** según la columna E3/ESQUEMA/EXTRACTOR
   de `tabla_resultados_esq2.md`: las ESQUEMA se resuelven o difieren acá
   con destino explícito; las E3 se verifican como promesa del ensamblado
   (B5 las hereda como criterio de aceptación); las EXTRACTOR/PIPELINE se
   derivan a B5 (endurecimiento) con entrada trazable — no son retoques de
   esquema y este laudo no las decide.
5. **Checklist de la cola** (obligatorio, regla del gate): entradas 2
   (304 `firma_invalida` / dominio de `aplica_a`, D8), 3
   (`RECHAZO_PREDECLARADO` como categoría con nombre), 4 (anotados de
   U-ESQ-1b i–iii), 7 (permanencia del canal abierto — la evidencia de la
   escalera pesa acá), + pronunciamiento sobre la 5 (modelo de datos);
   revisión de las entradas 9–11 en lo que toque al esquema.
6. **Salida**: lista cerrada de retoques con sus predicciones, y el
   pre-registro de ESQ-3b listo para sellar.

## ESQ-3b — Verificación pre-congelado (dos brazos, predicciones selladas)

Re-extracción **pareada**: mismas unidades, esquema viejo vs retocado — la
comparación es limpia porque las 762 extracciones viejas ya están
persistidas (`esq_cobertura.db`, sellos `a7788c1`) y son el brazo base a
costo cero. Predicciones selladas por separado ANTES de correr:

- **BRAZO OBJETIVO** — las unidades que motivaron cada retoque. Una
  predicción por retoque, falsable y concreta (formato: «la unidad de la
  ficha 15 deja de caer en la caja errónea Obligacion y cae en X»).
- **BRAZO REGRESIÓN** — ~30–40 unidades HOY bien tipadas, reusables de las
  fichas marcadas sí_completo/ninguna (20 fichas disponibles) más azarosas
  limpias adicionales si hace falta completar el n. Predicción única: «no
  cambian de tipo ni pierden relaciones». Mide el riesgo real de ampliar:
  la ATRACCIÓN — que contenido bien tipado migre a las cajas nuevas.
- **REGLA SELLADA**: si el brazo de regresión falla, el retoque se revisa
  aunque el objetivo pase. Un retoque que cumple su promesa pero desordena
  lo que estaba bien NO entra al esquema congelado.
- **Adjudicación**: de la autora, con fichas pareadas viejo-vs-nuevo por
  unidad (patrón de ESQ-2); regla de cegado de la entrada 10 de la cola
  (ninguna lectura ajena visible); instrumento con el arreglo de textos
  largos (entrada 11) aplicado antes de esta lectura.
- **Costo y tope**: ~60–75 unidades re-extraídas con prefijo nuevo
  (namespace de caché nuevo, decisiones de
  `docs/decisiones_caching_extraccion.md` vinculantes). Estimación
  ≈ USD 0,45 (por unidad promedio de ESQ-2: 4,1079/762 ≈ 0,0054, más una
  escritura de prefijo). **Tope propio propuesto: USD 1,00**, dentro del
  remanente de la saga (van 5,03 de 9,00).
- Si un retoque se ajusta por resultado de ESQ-3b: se corrige, se re-sella
  la predicción del retoque ajustado y se re-corre SOLO ese par — con el
  mismo tope.

## Laudo de esquema congelado (cierre del gate)

Se emite recién con los dos brazos pasando. Declara: versión final del
esquema con sha; posición registrada de la exigencia 10; y la **política de
corrección post-congelado**, que debe quedar escrita de antemano:

> **Decisión a tomar en este laudo** — ¿qué pasa si el escalado revela algo
> que ESQ-2 no vio? Opciones: (i) congelado DEFINITIVO — toda corrección es
> release posterior a la evaluación final (principio 9, sin excepciones);
> (ii) UNA ventana declarada — la tanda 1 de B6 (20 TOs) actúa como
> health-check de esquema: si revela una clase nueva de falla DE ESQUEMA
> (no de pipeline), se admite UN ciclo de corrección con laudo propio,
> re-extracción de la tanda 1 incluida, SIEMPRE ANTES de sellar el
> pre-registro de B6.3; sellado ese pre-registro, la ventana muere y rige
> (i). La opción elegida cambia el peso de cada decisión de ESQ-3a y por
> eso se fija acá, no cuando el problema aparezca.

## Qué NO hace ESQ-3

No corrige al extractor (deudas EXTRACTOR/PIPELINE → B5), no decide el
régimen informativo (ciclo ESQ-RI propio, `94bb7a7` §D10), no toca los
grafos medidos (principio 9), no arranca ningún ítem de B5/B6.
