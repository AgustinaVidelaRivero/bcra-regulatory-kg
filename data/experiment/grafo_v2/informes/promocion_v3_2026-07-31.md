# Acta — Promoción de reensamblado_v3 a grafo vigente de trabajo (2026-07-31)

**Resultado: registro `reensamblado_v3` como grafo vigente de trabajo en la app
(entrada explícita en `app/main.py`, listada primera; sin glob recursivo) y
dejo esta acta como registro de la decisión. Ningún kg.json se toca; los grafos
previos siguen disponibles (verificado: 7 grafos cargan, v3 = 4.458 nodos /
8.044 aristas).** Decisión ya laudada tras la medición del escalón 1b; esta
unidad la implementa y la documenta.

## 1. La decisión

`data/experiment/grafo_v2/reensamblado_v3/kg.json` pasa a ser el **grafo
vigente de trabajo** — el objeto sobre el que operan el refinamiento, la app y
el triage de feedback de acá en adelante. Es una **decisión explícita y
registrada, no una edición silenciosa**: el registro en la app es una entrada
directa (`GRAFOS_EXPLICITOS` en `app/main.py`), deliberadamente sin
generalizar el descubrimiento a glob recursivo, para que ningún kg.json
futuro se promueva por accidente de estar en el árbol. La UI lo lista primero
por el mecanismo de orden existente; el marcador "(recomendado)" del frontend
vive en `app/static/index.html` (fuera de las escrituras de esta unidad) y
sigue apuntando a run_3 hasta que se decida tocarlo.

## 2. La evidencia

- **Escalón 1b** (`docs/lectura_escalon1b.md`, resultados en
  `evaluacion_escalon1/corridas/resultados_1b_FINALES_2026-07-31.json`):
  **v2 27/36 → v3 29/36** sobre EV1 sellado, mismo caché de extracción y mismo
  instrumento congelado; dos conversiones atribuibles al re-ensamblado
  (EV1-031, EV1-042, predichas y selladas antes de correr), la tercera por
  varianza de trayectoria, y la única regresión (EV1-035) exonerada del grafo
  por sus trazas.
- **Pasada 1 de métricas intrínsecas**
  (`data/experiment/metricas_intrinsecas/pasada1_resumen.md`): menor
  conflación, menor ruido por rol documental, cero chunks mudos. Salvedad de
  una línea: M1/M2 muestran a v3 peor y eso está previsto en la spec §3 (la
  inversión intrínseco/extrínseco es un resultado esperado del régimen de dos
  pasadas, no una anomalía).

## 3. Lo que la promoción NO cambia

- `grafo_v2/kg.json` queda **sellado como medición** (baseline del escalón 1
  y del 1b; commit `11f0d4a` intacto).
- `run_3` sigue siendo el **baseline congelado de la Fase 2.3** (la selección
  del ganador no se reabre; su rol en el 1b fue referencia descriptiva).
- **EV1 queda quemado**: cualquier medición futura del vigente requiere EV2
  por generación ciega.

## 4. Defectos conocidos que v3 CARGA (la lista de trabajo del refinamiento)

Con puntero al backlog (`docs/backlog_reextraccion.md`):

- **Residuo RX-02 / RX-05 / RX-06**: locations desplazadas por coalescing,
  chunks con roles documentales mezclados, contexto cortado por el hard cap —
  congelados en el texto de los chunks; ningún re-ensamblado los arregla.
- **RX-10 vigente en v3**: los montos de la tabla del punto 1.2 de capitales
  mínimos siguen invertidos (bancos 2.500 / restantes 5.000) — la
  linealización de la tabla está en el texto del chunk.
- **Pérdida del criterio general 1.1** (precisión de RX-07): el chunk mixto
  `clasificacion_deudores::10.4` quedó excluido por rol índice y ese texto
  desapareció de v3 respecto de v2.
- **11 sujetos de cuarentena sin aristas de jerarquía**
  (`reensamblado_v3/cuarentena.json`): nodos `Sujeto_propuesto_*` léxicamente
  alcanzables en su mayoría pero sueltos del esqueleto.

El refinamiento (U3/U4) opera sobre esta lista, con el circuito de backlog y
verificación del proyecto.

— FRENO. Nada commiteado; el commit de la promoción es de la autora. —
