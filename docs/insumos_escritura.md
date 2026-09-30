# Índice de insumos del repo para la escritura de la tesis

Índice de los artefactos del repo que alimentan la escritura. Lo mantengo desde el
30/09/2026 (plan, fila C1.11). La escritura sigue en la mesa de escritura; este índice
le dice qué insumo usar, de dónde sale y con qué salvedades.

**Convenciones.**
- La tesis se cita por sección y frase desde la versión de Overleaf.
  `docs/tesis/main.tex` del repo está desactualizado y no se usa como fuente (plan,
  fila C1.11).
- Las secciones se nombran por su contenido, según la estructura decidida el 30/09:
  - capítulo 3: del documento a su análisis y al esquema;
  - capítulo 4: el pipeline, componente por componente, y la construcción por etapas,
    con la tanda 0 como primera etapa.
  El número de sección en Overleaf queda NO VERIFICADO.
- Toda cifra que pase a la tesis se toma del artefacto, con su comando o su clave, no
  de este índice.
- Estado de cada insumo: **disponible** (commiteado) o **pendiente** (unidad en curso).

## 1. Estadísticas descriptivas del corpus — disponible

- **Ruta y commit:**
  - `reports/u_insumos_cap/estadisticas_corpus.md` y `estadisticas_corpus.json`,
    generados por `reports/u_insumos_cap/u_insumos_i1.py`;
  - commit `ded3494` (U-INSUMOS-CAP, etapa I1);
  - comando: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B reports/u_insumos_cap/u_insumos_i1.py`;
  - doble corrida byte a byte idéntica, y una re-corrida independiente de la mesa
    también idéntica.
- **Qué contiene:** para el corpus escalado (152 TOs), el conjunto de desarrollo (5) y
  los cinco TOs de la tanda 0:
  - TOs por clase y por categoría;
  - páginas por rol y por TO;
  - unidades por tipo y por profundidad;
  - estructura de la numeración: puntos terminales y contenedores;
  - tablas y fórmulas;
  - largos de unidad;
  - remisiones internas y externas;
  - marcadores deónticos;
  - tabla de origen de las disposiciones y procedencia, por TO;
  - nodos por tipo y aristas por predicado de KG-Tanda0-Desarrollo-r1 y de
    KG-Reextraído-r1.

  Las reglas R0 a R17 se declararon antes de aplicarse (§1 del `.md`). Las cuatro
  cifras publicadas de la partición (152 / 6.757 / 9.324 / 559) están reproducidas
  (§0).
- **Alimenta:**
  - capítulo 3: la descripción de los documentos del BCRA y su análisis (tamaño,
    estructura de la numeración, tablas, remisiones, lenguaje deóntico, tabla de
    origen);
  - capítulo 4: la construcción por etapas (qué se procesó en desarrollo y en la tanda
    0) y el grafo resultante (nodos y aristas por tipo).
- **Salvedades:**
  1. Las tablas lógicas son 559 parseadas (`particion_152.json`) o 563 detectadas
     (`conteos_b584.json`), según el archivo. Hay que citar cuál.
  2. Las remisiones «externas» son menciones a una norma nombrada detectadas por regex
     (regla R8). Pueden ser del mismo TO y no son remisiones entre TOs. Para las
     remisiones entre TOs se usan las aristas `referencia` entre TOs del grafo.
  3. Los cinco TOs de la tanda 0 no tienen chunks marcados como tabla.
  4. Límites que declara el propio reporte (§7):
     - los anexos son una cota inferior;
     - los TOs sin portada legible quedan sin dato de procedencia;
     - la clase de la partición no aplica al conjunto de desarrollo;
     - las tablas lógicas de cla, ext, pro y ric son NO ENCONTRADO (solo cap tiene el
       testigo del parser).
  5. Las 9.324 unidades incluyen 69 chunks con id repetido en 4 TOs. Son colisiones de
     numeración (`BKL-0037`) y no cambian las cifras publicadas.

## 2. Recorrido del ejemplo del préstamo por componente — pendiente

- **Ruta y commit:** `reports/u_insumos_cap/recorrido_prestamo.md` (U-INSUMOS-CAP,
  etapa I2; mandato `docs/mandatos/UINSUMOS_CAP_escritura.md`, firmado en `30f106c`).
  Commit pendiente.
- **Qué contendrá:** el paso del ejemplo `cla::5.1.1.1` → `cla::3.7` por cada
  componente, de E0 al agente, con su artefacto o NO ENCONTRADO, y las dependencias con
  las figuras.
- **Alimenta:** capítulo 4, el pipeline componente por componente, y las figuras del
  ejemplo (`docs/tesis/figuras/LEEME_figura_*.md`).
- **Salvedades conocidas:**
  - los datos son de KG-Reextraído-r1 (`0226e947…`); después de la re-extracción de la
    tanda 0 (U-REEXT-T0) siguen siendo datos de r1, salvo que se regeneren;
  - el juez, la atribución A0.2 y los indicadores de cita del préstamo son NO
    ENCONTRADO, por mandato.

## 3. Umbrales (U-UMBRAL) — pendiente

- **Ruta y commit:** `reports/u_umbral/` (mandato `docs/mandatos/UUMBRAL_investigacion.md`,
  firmado en `30f106c`). Commit pendiente.
- **Qué contendrá:** seis mediciones sobre umbrales, y la evidencia ordenada en dos
  ejes: dónde vive el umbral y cómo se llena. La propuesta es un par (representación,
  método de llenado), con su alternativa.
- **Alimenta:**
  - capítulo 3: la decisión de esquema sobre umbrales, una vez laudada en L-ESQ-R2;
  - capítulo 4: el método de llenado.
- **Salvedades conocidas:**
  - EV2 y sus trazas se usan como diagnóstico, no como resultado (principio 7 del
    plan);
  - la muestra de 30 aristas `limita` se prepara, pero no se lee en la unidad.

## 4. Listas cerradas y lo no mapeable (U-LISTAS-NOMAP) — pendiente

- **Ruta y commit:** `reports/u_listas_nomap/` (mandato
  `docs/mandatos/ULISTAS_NOMAP_diseno.md`, firmado en `30f106c`). Commit pendiente.
- **Qué contendrá:**
  - el inventario de las listas cerradas sobre el crudo de E1;
  - los sujetos posiblemente forzados;
  - la tasa de `sujeto_propuesto` literal en el chunk;
  - la re-resolución contrafáctica;
  - las omisiones;
  - el diseño del proceso para lo no mapeable.
- **Alimenta:**
  - capítulo 3: las listas cerradas y el catálogo de sujetos;
  - capítulo 4: la validación en código y la resolución de sujetos.
- **Salvedades conocidas:**
  - la re-resolución con los seis ids que faltan en el JSON es contrafáctica, no un
    resultado;
  - la muestra de posibles forzados no se lee en la unidad.
