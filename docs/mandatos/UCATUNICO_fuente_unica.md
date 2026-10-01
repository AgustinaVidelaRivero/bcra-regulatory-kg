BORRADOR — PENDIENTE DE FIRMA de la autora

MANDATO — U-CAT-UNICO: CATÁLOGO DE SUJETOS EN UNA SOLA FUENTE.
Repo bcra-regulatory-kg. Leé CLAUDE.md antes de empezar.
- Unidad en DOS ETAPAS, con FRENO obligatorio al final de cada una: reporte corto (no más de
  40 líneas) y espera de la revisión y del «seguí» escrito de la autora. C2 no arranca sin él.
- Costo de API: USD 0. Ninguna llamada a la API; Neo4j no se usa.

CONTEXTO. Plan, fila B2.11, unidad 6 (docs/plan_tesis.md:395), habilitada por la firma de
L-ESQ-R2 (`4ef7650`). Checklist X15 (absorbe R8), X6 y X7.
- Hoy el catálogo de sujetos vive en dos fuentes que no coinciden:
  - el bloque del prompt v3, con 102 ids (B5.4; prefijo sha256 `35e88c2dd0a2…`, hash
    `54a111e2175f`);
  - data/experiment/esq_v3_miembros/esquema_v3_clases.json (sha256 `dad88cc9…`), con 101 ids,
    que leen E4, el esqueleto y S19.

  Seis ids están solo en el bloque y cinco solo en el JSON (tablero, fila «Catálogo de sujetos
  en dos fuentes», [c13]).
- L-ESQ-R2 §7.3 decide el contenido (abajo, decisiones 2 y 3).
- Esta unidad construye la fuente única y genera desde ella todo lo que hoy consume el
  catálogo. No sella ningún prefijo: el bloque nuevo entra al prefijo de U-PROMPT-R2 (unidad
  10). No edita consumidores: el perfil nuevo que los conecta es de U-PYD (unidad 7).

Leé completos, antes de escribir una línea:
- data/experiment/esq/enmienda_L-ESQ-R2_2026-09-30.md (FIRMADA en `4ef7650`): §7 entero, y
  §3 y §4 (resolución en código y registro de no mapeados);
- data/experiment/b54_catalogo_v3/code/prompt_v3_b54.py:
  - `bloque_catalogo_v3` (:326) y `BLOQUE_CATALOGO_V3` (:396);
  - `sujetos_catalogo_v3` (:402);
  - `_rol_por_to_v3` (:428) y `ROL_POR_TO_V3` (:453);
  - `prefijo_sistema_v3` (:382), con las anclas del bloque (:90-91);
- el laudo de B5.4 fase 1, docs/laudo_B5.4_fase1_catalogo.md: adiciones de F1.4 (:46-49) y
  retiros de F1.5 (:70-75). Las lápidas están en
  data/experiment/b54_catalogo_v3/catalogo_sujetos_v3.md:51-55;
- data/experiment/esq_v3_miembros/esquema_v3_clases.json (claves `clases`, `roles` y
  `excepciones_s15`);
- los consumidores actuales del catálogo:
  - data/experiment/reextraccion_v2/e1_extractor/perfil_e1.py (`_labels_catalogo_v3` :101,
    `sujetos_catalogo_set` :166, `labels_catalogo` :179) y validador_e1.py;
  - data/experiment/reextraccion_v2/e2_reduce/e2_lib.py (:756);
  - data/experiment/reextraccion_v2/corpus_v2/r1_e4.py (`indice_catalogo` :74,
    `resolver_label` :97) y r1_e5_esqueleto.py;
  - data/experiment/tanda0/code/ensamblar_tanda0.py (:75 y :218);
  - scripts/shapes_validator.py (`cargar_catalogo_sujetos` :227, `shape_s19_catalogo` :760);
  - scripts/regression_kg.py (`--catalogo`, :35 y :451-454);
- data/backlog/backlog.jsonl: `BKL-0028` (:73), `BKL-0029` (:74) y `BKL-0034` (:79, con el
  evento de :84);
- reports/u_listas_nomap/diseno_listas_nomap.md: P-a4, P-d3, LN-6, LN-8 y S29.

DECISIONES YA TOMADAS. No se re-deciden.
1. Una sola fuente. Desde un JSON se generan:
   - el bloque del prompt;
   - los enums del tool schema (`sujeto_id` y padre sugerido);
   - `ROL_POR_TO`;
   - los labels de E2;
   - el índice de E4;
   - la entrada del esqueleto;
   - el conjunto de ids de S19;
   - el catálogo de la suite.
2. La diferencia 6/5 se resuelve aplicando el laudo de B5.4: los seis ids del bloque son
   vigentes y los cinco del JSON quedan como lápidas no vigentes (L-ESQ-R2 §7.3).
3. Contenido nuevo (L-ESQ-R2 §7.3):
   - `BKL-0028`: tres ids del exterior, y los alias «del exterior» salen de las entradas
     domésticas;
   - `BKL-0029`: un id para «titulares de cuenta corriente en el BCRA», con re-adjudicación
     del miembro del rol de convca;
   - `BKL-0034`: Directorio, Alta Gerencia y Comité de auditoría como clases bajo una clase
     nueva «órgano de gobierno», dentro del árbol actual y sin nivel nuevo. Los nombres de los
     ids los fija esta unidad.
4. Las marcas de revisión de B5.4 (`ministerio_de_economia`, `sociedad_de_proposito_especial`)
   no se tocan: se revisan con datos de la tanda 1 (L-ESQ-R2 §7.3).
5. El catálogo v3 y el r2 son dos versiones del mismo esquema de JSON, cada una con su sha256.
   La re-resolución por programa se dispara por cambio de sha (L-ESQ-R2 §4; diseño, P-d3).

C1 — Fuente única con el contenido v3. USD 0.
a. Esquema del JSON, declarado en el reporte antes de construirlo. Por id:
   - nivel: clase, instancia o rol;
   - label, alias y definición;
   - padre (subclase de);
   - miembros, si es rol;
   - rol por TO;
   - estado: vigente o lápida, con evidencia, fecha y laudo;
   - procedencia de cada campo: de qué artefacto sale.
b. Construcción por programa, nunca a mano, desde los artefactos de la lista de lectura:
   data/experiment/catalogo_unico/catalogo_sujetos_v3.json. Lleva los 102 ids del bloque v3
   como vigentes y los 5 retirados como lápidas. Script:
   data/experiment/catalogo_unico/code/construir_catalogo_v3.py.
c. Generador data/experiment/catalogo_unico/code/generar_desde_catalogo.py. Produce desde el
   JSON cada artefacto de la decisión 1, en archivos nuevos bajo
   data/experiment/catalogo_unico/generados_v3/.
d. Selftest data/experiment/catalogo_unico/code/selftest_catalogo_unico.py. Compara cada
   artefacto generado con su consumidor actual:
   - el bloque, byte a byte contra `BLOQUE_CATALOGO_V3`; y el prefijo v3 recompuesto con ese
     bloque, contra `PREFIJO_SHA256_V3` (`35e88c2dd0a2…`);
   - la lista de ids, contra `sujetos_catalogo_v3()` y el `sujetos_catalogo_set` del perfil
     `v3_b54`;
   - `ROL_POR_TO`, contra `ROL_POR_TO_V3`;
   - los labels, contra `labels_catalogo` del perfil `v3_b54`;
   - el índice de E4 (`r1_e4.indice_catalogo`) y la entrada del esqueleto, contra los que se
     obtienen hoy con esquema_v3_clases.json. La única diferencia admitida es la 6/5;
   - el conjunto de ids de S19: los 102 vigentes (hoy S19 lee 101).

   Toda diferencia no declarada es FRENO. Es también el control LN-8 del diseño (bloque y JSON
   sin diferencias); su entrada en scripts/regression_kg.py la hace U-R2-CODIGO.
e. Tabla de consumidores: para cada uno, el archivo y la línea donde hoy lee el catálogo, y el
   artefacto generado que lo reemplaza en el perfil nuevo.
FRENO C1:
- el resultado del selftest por artefacto;
- el sha256 del JSON v3 y de cada generado;
- la tabla de consumidores.

C2 — Contenido de L-ESQ-R2 §7.3: el catálogo r2. USD 0.
a. data/experiment/catalogo_unico/catalogo_sujetos_r2.json, derivado del v3 por un script
   (data/experiment/catalogo_unico/code/derivar_catalogo_r2.py). Cada cambio es una operación
   declarada y registrada: alta, cambio de alias o cambio de miembro de rol.
b. Cada id nuevo lleva id, label, alias, definición positiva y padre, cada uno con su ancla en
   el texto del corpus (TO::punto). Lo que no tenga ancla se marca NO ENCONTRADO y no se
   inventa.
   - `BKL-0028`: tres ids del exterior. Los alias «del exterior» salen de
     `Sujeto_entidad_financiera`, `Sujeto_banco` y `Sujeto_entidad_cambiaria` y pasan a los
     nuevos. Anclas: `ctacor::1.1` y `ctacor::1.4`, más las que cite la entrada del backlog.
   - `BKL-0029`: un id para «titulares de cuenta corriente en el BCRA». El miembro de
     `Sujeto_rol_alcance_convca` pasa a ese id, y su residuo declarado queda sin el campo
     `colectivo_operativo_sin_id`. Anclas: `convca::1.1`, `convca::2.1.3` y `ccbcra::1.1`.
   - `BKL-0034`: la clase «órgano de gobierno» y, bajo ella, Directorio, Alta Gerencia y Comité
     de auditoría. Ancla: `lingob::2.3.2` y su sección.
c. Regenerar todos los artefactos en data/experiment/catalogo_unico/generados_r2/ y comprobar:
   - que el bloque r2 difiere del v3 solo en las entradas que toca (b), con el diff declarado;
   - las condiciones de cierre que se verifican sobre el catálogo:
     - `BKL-0028`: el barrido de data/experiment/esq_v3_miembros/code/, que hoy devuelve los tres
       ids domésticos con alias del exterior, devuelve cero sobre el catálogo r2;
     - `BKL-0029`: el miembro del rol de convca es el id nuevo.

     La parte de `BKL-0034` que exige una arista del grafo (`lingob::2.3.2::intro` →
     Directorio) queda para r2b, y se declara pendiente.
d. Re-resolución contrafáctica sobre lo guardado, USD 0. Se resuelven en código, con el catálogo
   r2 y los criterios de `r1_e4.resolver_label`, los sujetos propuestos de la tanda 0: en diez,
   34 propuestos, 30 en cuarentena (U-LISTAS-NOMAP N1, `propuestos_e4`). Cuenta cuántos resuelven
   con r2 y no con v3. Es un dato, no una meta (L-ESQ-R2 §4.3).
FRENO C2, final:
- el diff del bloque v3 → r2;
- el sha256 del JSON r2 y de cada generado;
- las condiciones de cierre, verificadas o pendientes con su motivo;
- la cifra de la re-resolución, con su comando.

Commit de la autora.

REQUISITOS TRANSVERSALES (CLAUDE.md §4 a–j), en todas las etapas.
- Escrituras: solo data/experiment/catalogo_unico/ (se crea) y tu scratchpad.
  - No se editan el plan, el checklist, el tablero, los laudos, el backlog, scripts/, los
    prompts ni los perfiles. En particular, no se tocan prompt_v3_b54.py, perfil_e1.py,
    validador_e1.py ni esquema_v3_clases.json.
  - Nada sellado se toca (CLAUDE.md §3).
  - No commitees.
- Python:
  - PYTHONDONTWRITEBYTECODE=1 y .venv/bin/python -B en todo Python.
  - Ningún __pycache__ ni .pyc nuevo: línea de base al inicio (conteo de .pyc) y control al
    cierre.
  - Construcción, generador y selftest con doble corrida byte a byte idéntica.
- Afirmaciones y citas:
  - Toda afirmación lleva path:línea o comando.
  - Los conteos se recomputan antes de escribirse (§4 i).
  - Lo que no esté en un artefacto es NO ENCONTRADO.
  - La tesis no se cita por línea de docs/tesis/main.tex; la fuente es Overleaf.
  - Los mentores solo por rol; cero nombres propios.
- Si algo de este mandato contradice un archivo del repo, mandan los archivos y se reporta la
  contradicción.
- Revisión y checkpoint:
  - Paquete de revisión revision_UCATUNICO_C<n>/ por etapa, con manifest.txt (sha256 y una
    línea por archivo) y nombres únicos.
  - Checkpoint checkpoint_UCATUNICO.md en el scratchpad, actualizado al cierre de cada etapa y
    antes de cualquier compactación.
- Shell zsh: variables entre comillas o como arrays; ningún comentario con # dentro de los
  bloques de comandos para copiar.

CRITERIO DE ACEPTACIÓN por etapa:
- el reporte corto con las salidas pedidas;
- git status --short con solo data/experiment/catalogo_unico/ como nuevo;
- doble corrida byte a byte idéntica de lo que la etapa escribe;
- C1: el bloque generado igual byte a byte a `BLOQUE_CATALOGO_V3`, y la 6/5 como única
  diferencia contra esquema_v3_clases.json;
- C2: cada id nuevo con su ancla o NO ENCONTRADO, y el diff del bloque limitado a lo que toca
  L-ESQ-R2 §7.3;
- el grep de convenciones, pegado aunque dé vacío.

FRENO al final de cada etapa.
