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

## 2. Recorrido del ejemplo del préstamo por componente — disponible

- **Ruta y commit:**
  - `reports/u_insumos_cap/recorrido_prestamo.md`, generado por
    `reports/u_insumos_cap/u_insumos_i2.py`;
  - commit `f32f20c` (U-INSUMOS-CAP, etapa I2; mandato
    `docs/mandatos/UINSUMOS_CAP_escritura.md`, firmado en `30f106c`);
  - comando: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B reports/u_insumos_cap/u_insumos_i2.py`;
  - doble corrida byte a byte idéntica, y una re-corrida independiente de la mesa
    también idéntica. El script se detiene si falla cualquier afirmación que el `.md`
    escribe como texto fijo.
- **Qué contiene:** el paso del ejemplo `cla::5.1.1.1` → `cla::3.7` por trece
  componentes: E0, E1, E3, extracción final, E2, E4, esqueleto, referencias y
  procedencia de r1, grafo final, agente, juez, atribución A0.2 e indicadores de cita.
  Para cada uno, el artefacto con ruta y línea o id, o NO ENCONTRADO, y una línea con
  lo que el ejemplo muestra. Incluye las dependencias con las cuatro figuras del
  ejemplo.
- **Alimenta:**
  - capítulo 4: el pipeline, componente por componente, y las figuras del ejemplo
    (`docs/tesis/figuras/LEEME_figura_*.md`);
  - **uso posible en el capítulo 4:** el mismo punto extraído por dos generaciones
    del pipeline, como ilustración de la construcción por etapas (ver la salvedad 2).
- **Salvedades:**
  1. Los datos son de KG-Reextraído-r1 (`0226e947…`), construido con el esquema v2.
  2. En KG-Tanda0-Desarrollo-r1 el ejemplo tiene otra estructura: 2 Condicion, 1
     Definicion y 1 Operacion, sin `limita` ni remisión al 3.7 (recomputado por la mesa
     el 30/09). En r1 son 2 Restriccion y 1 Operacion, con 2 `limita` y la remisión.
  3. La remisión de r1 al 3.7 sale de la paráfrasis del nodo (descripción y
     `umbral`), no del texto de E0.
  4. E4, juez, atribución A0.2 e indicadores de cita son NO ENCONTRADO:
     - E4 no toca el ejemplo;
     - la corrida del agente sobre el ejemplo fue sin juez;
     - A0.2 exige el veredicto de cada traza;
     - los indicadores de cita se calculan solo sobre las trazas de EV2.
  5. Los sha de los LEEME de figuras que cita el recorrido son los del árbol de
     trabajo al correr I2, y coinciden con los commiteados en `e6e6021`.
  6. Después de la re-extracción de la tanda 0 (U-REEXT-T0), estos datos siguen
     siendo de r1, salvo que se regeneren (tablero, fila del test del ejemplo).

## 3. Umbrales (U-UMBRAL) — disponible

- **Ruta y commit:**
  - `reports/u_umbral/`: `u1_mediciones.json` y `.md` (U1, commit `e81ed69`);
    `u2_muestra_trazas.json` y `.md`, `muestra_limita_30.csv` y `reporte_u_umbral.md`
    (U2, commit `e4d053b`);
  - mandato `docs/mandatos/UUMBRAL_investigacion.md`, firmado en `30f106c`;
  - comandos: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B reports/u_umbral/u_umbral_u1.py`
    y `… reports/u_umbral/u_umbral_u2.py`. Dobles corridas byte a byte idénticas, y
    re-corridas independientes de la mesa también idénticas.
- **Qué contiene:**
  - seis mediciones sobre umbrales en los tres grafos (desarrollo, r1 y diez):
    literalidad de `umbral` y `plazo`, tablas que E0 no marca, cuantías sin campo, un
    prototipo de llenado en código, aristas `limita` y trazas;
  - la evidencia ordenada en dos ejes, dónde vive el umbral y cómo se llena, con la
    propuesta como par (representación, método de llenado) y su alternativa
    (`reporte_u_umbral.md`);
  - la orientación de la autora para L-ESQ-R2 está registrada en el plan (fila B2.11,
    unidad 5).
- **Alimenta:**
  - capítulo 3: dónde vive el umbral, justificado por los documentos (umbrales
    frecuentes, a menudo relativos a otro valor y a veces varios en un mismo punto);
  - capítulo 4: cómo se llena (E1 copia el tramo literal; la normalización y la
    verificación contra E0 y el parser de tablas son código).
- **Salvedades:**
  1. Los denominadores de U-UMBRAL salen del [c14] del mandato (605 en desarrollo, 638
     en r1, 682 en diez). En la tesis se citan los del tablero corregido: 606, 639 y
     683. La diferencia es un nodo, «diez (10) años».
  2. EV2 se usa como diagnóstico, sobre 8 criterios con cuantía, no como resultado
     (principio 7 del plan).
  3. La muestra de 30 aristas `limita` está sellada y sin leer; se lee en la unidad 4b
     del plan, antes de L-ESQ-R2.
  4. El costo del llenado por un modelo es una estimación no verificada.

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
