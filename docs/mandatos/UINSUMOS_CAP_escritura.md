BORRADOR — PENDIENTE DE FIRMA DE LA AUTORA

MANDATO — U-INSUMOS-CAP: INSUMOS DEL REPO PARA LOS CAPÍTULOS 3 Y 4.
Repo bcra-regulatory-kg. Leé CLAUDE.md antes de empezar.
- Unidad en DOS ETAPAS, con FRENO obligatorio al final de cada una: reporte corto
  (no más de 40 líneas) y espera de la revisión y del «seguí» escrito de la autora.
  Ninguna etapa arranca sin él.
- Costo de API: USD 0. Ninguna llamada a la API; Neo4j no se usa.
- Corre en paralelo con U-UMBRAL y U-LISTAS-NOMAP, con directorios de escritura
  disjuntos: no leas ni escribas en reports/u_umbral/ ni en reports/u_listas_nomap/.

CONTEXTO. Plan, fila B2.11, unidad 14 (docs/plan_tesis.md:402), y fila C1.11
(:854); checklist W9, W10 y W12.
- Estructura decidida por la autora el 30/09:
  - capítulo 3: del documento a su análisis y al esquema;
  - capítulo 4: el pipeline, componente por componente, y la construcción por
    etapas, con la tanda 0 como primera etapa.
- La escritura sigue en la mesa de escritura. Esta unidad le da insumos citables;
  no escribe la tesis.

Leé completos, antes de escribir una línea:
- la partición del segmentador, en data/experiment/segmentacion_84/b584_particion/:
  - reporte_b584.md;
  - particion_152.json (claves `agregados` y `por_to`);
  - conteos_b584.json;
  - los archivos chunks_<to>.json y estructura_<to>.json de cada <to>/;
- data/experiment/escalado_prep/inventario_resumen.json;
- data/experiment/job_actualizacion/sonda_procedencia.json;
- el ejemplo del préstamo:
  - docs/tesis/figuras/ejemplo_prestamo_datos.json;
  - docs/tesis/figuras/extraer_datos_ejemplo_prestamo.py;
  - los LEEME_figura_*.md de docs/tesis/figuras/;
- las trazas del agente sobre el ejemplo: reports/u_med_ejemplo/umed2_analista_paso4_*.

DECISIONES YA TOMADAS. No se re-deciden.
1. La unidad produce insumos citables, no prosa de la tesis. No edita docs/tesis/
   ni Overleaf.
2. La tesis se cita por sección y frase desde Overleaf. docs/tesis/main.tex del
   repo está desactualizado y no se usa como fuente (fila C1.11). Si hace falta una
   frase de la tesis, se marca NO VERIFICADA contra Overleaf.
3. Antes de usar cualquier otra cifra, se reproducen desde los JSON las cifras de
   la partición ya publicadas (152 / 6.757 / 9.324 / 559, reporte_b584.md:20). Una
   diferencia es FRENO.
4. El ejemplo del préstamo es `cla::5.1.1.1` → `cla::3.7` sobre KG-Reextraído-r1
   (`0226e947…`). El recorrido usa solo artefactos existentes: lo que no exista se
   marca NO ENCONTRADO y no se genera. El juez, la atribución A0.2 y los
   indicadores de cita del préstamo costarían API o no están en alcance.
5. Después de la re-extracción de la tanda 0 (U-REEXT-T0), los datos del ejemplo
   quedan como datos de r1. La unidad lo declara en su salida.

I1 — Estadísticas descriptivas del corpus. USD 0.
a. Script nuevo reports/u_insumos_cap/u_insumos_i1.py, de solo lectura.
b. Para el corpus de 152 TOs y, aparte, para el conjunto de desarrollo (5 TOs) y
   para los cinco TOs de la tanda 0:
   - TOs por clase de la partición y por categoría (normativa general, régimen
     informativo);
   - páginas por rol;
   - unidades por tipo (punto terminal, mini-chunk, sección sin puntos) y por
     profundidad. La regla de profundidad se declara antes; los `::intro` toman la
     profundidad del padre;
   - tablas lógicas, y chunks marcados como tabla o fórmula;
   - largos de unidad: mediana, percentiles y máximo;
   - remisiones «punto X.Y» por TO, con una regex declarada antes;
   - última Comunicación incorporada y fecha del texto ordenado, por TO
     (sonda_procedencia.json), con su cobertura.
c. Cada cifra lleva el comando o la clave del JSON que la reproduce, y su
   denominador explícito.
d. Salidas: reports/u_insumos_cap/estadisticas_corpus.json y
   estadisticas_corpus.md; doble corrida byte a byte idéntica.
FRENO I1: las cuatro cifras publicadas, reproducidas; tabla de estadísticas con su
comando; sha256 de lo escrito.

I2 — Recorrido del préstamo por componente. USD 0.
a. Documento reports/u_insumos_cap/recorrido_prestamo.md. Si hace falta, un script
   de solo lectura, reports/u_insumos_cap/u_insumos_i2.py, que extraiga los
   fragmentos.
b. Componentes: E0 (chunks); E1 (salida cruda y validación); E3 (veredicto y
   reintento); extracción final; E2; E4; esqueleto; referencias y procedencia de
   r1; grafo final; agente (trazas umed2); juez; atribución A0.2; indicadores de
   cita. Para cada uno:
   - el artefacto que contiene el paso del ejemplo, con ruta y línea o id, y un
     extracto corto;
   - NO ENCONTRADO si no hay artefacto;
   - una línea con lo que el ejemplo muestra sobre ese componente: un hecho
     verificable, no una interpretación.
c. Dependencias con las figuras: qué figura usa qué dato (LEEME_figura_*.md) y qué
   cambiaría después de U-REEXT-T0.
FRENO I2, final: la tabla de componentes con artefacto o NO ENCONTRADO; sha256 de
lo escrito. Commit de la autora.

REQUISITOS TRANSVERSALES (CLAUDE.md §4 a–j), en todas las etapas.
- Escrituras: solo reports/u_insumos_cap/ (se crea) y tu scratchpad.
  - No se editan el plan, el checklist, el tablero, el laudo, docs/tesis/, el
    backlog ni nada bajo data/experiment/.
  - Nada sellado se toca (CLAUDE.md §3).
  - No commitees.
- Python:
  - PYTHONDONTWRITEBYTECODE=1 y .venv/bin/python -B en todo Python.
  - Ningún __pycache__ ni .pyc nuevo: línea de base al inicio (conteo de .pyc) y
    control al cierre.
  - Las dbs de caché, si hicieran falta, solo con file:…?immutable=1.
- Afirmaciones y citas:
  - Toda afirmación lleva path:línea o comando.
  - Los conteos se recomputan antes de escribirse (§4 i).
  - Lo que no esté en un artefacto es NO ENCONTRADO.
  - Los mentores solo por rol; cero nombres propios.
- Si algo de este mandato contradice un archivo del repo, mandan los archivos y se
  reporta la contradicción.
- Revisión y checkpoint:
  - Paquete de revisión revision_UINSUMOS_CAP_I<n>/ por etapa, con manifest.txt
    (sha256 y una línea por archivo) y nombres únicos.
  - Checkpoint checkpoint_UINSUMOS_CAP.md en el scratchpad, actualizado al cierre
    de cada etapa y antes de cualquier compactación.
- Shell zsh: variables entre comillas o como arrays; ningún comentario con # dentro
  de los bloques de comandos para copiar.

CRITERIO DE ACEPTACIÓN por etapa:
- el reporte corto con las salidas pedidas;
- git status --short con solo reports/u_insumos_cap/ como nuevo;
- doble corrida byte a byte idéntica;
- las cifras 152 / 6.757 / 9.324 / 559 reproducidas desde los JSON;
- el grep de convenciones, pegado aunque dé vacío.
Criterio final: cada estadística con comando y denominador; cada componente del
recorrido con su artefacto o NO ENCONTRADO.

FRENO al final de cada etapa.
