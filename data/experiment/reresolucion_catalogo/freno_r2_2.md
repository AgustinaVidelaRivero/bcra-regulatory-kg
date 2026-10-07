# U-RERESOL-CAT — FRENO R2-2, final de la unidad (07/10/2026)

Mandato firmado en `f87ec4a` (notas hasta `0737497`); enmienda 6 a L-ESQ-R2 FIRMADA en su parte A (`0737497`). HEAD `6e611d6` (los commits
desde `0737497` no tocan rutas de esta unidad). USD 0; sin API ni Neo4j; todo sobre una copia sin enlaces; cifras en `salidas/r2_2_*`.
**Decisiones de la autora en la sesión (regla d).** (1) Parte A solo en r2b: `parte_a=False` por defecto y la cadena pasa `parte_a=(fase ==
"r2b")`, una línea en `ensamblar_tanda0.py`. (2) Precisión a la decisión 2: con alcance nuevo, la fila con sugerencia guardada va por R4 como
en la cadena, aunque la mención no verifique (darle el rol es la parte B no adoptada); conserva su marca y se cuenta aparte (sección
`parte_a` del reporte). Lo asienta la mesa. (3) `prompt_r2b.py` no se toca. (4) S19: declarar y frenar.
**Código** (6 archivos). `r1_e4.py` +48/−14 (parte A antes de R4; `reresolver_registro` con la regla de la cadena y el calificador en
`resuelto_a_clase`); `ensamblar_tanda0.py` +1/−1; `reresolver_catalogo.py` +196/−23 (lector del registro de alcance, `registro`, `componer
--registro-alcance`; parte A en `decidir` y (a+); alcance nuevo en el contraste; sección `parte_a`); selftests `selftest_r3` +63 (124/124) y
`selftest_reresolver_catalogo` +118 (66/66); procedimiento +48/−44. Nuevo: `r2_2_medicion.py`.
**Controles** (`r2_2_controles_parte_a_y_mensaje.json`, `r2_2_resumen_controles.json`; otros selftests: regression_kg 184/184,
catalogo_unico 60/60, prompt_r2b 55/55).
- docvig, crudo r2b: regla 1 = 4, regla 2 = 0. Las 4, iguales en r2b diez y sin cola diez: `docvig::3.4`, relaciones 5, 6, 7 y 9 (`aplica_a`,
  «Las/las entidades», exacta, sugerencia `Sujeto_sujeto_regulado`): antes `Sujeto_sujeto_regulado` por R4, después cuarentena
  (`colectivo_sin_sujeto_por_defecto`) con el nodo `Sujeto_propuesto_las_entidades`. Grafo: +1 nodo; las 4 aristas (3 Obligacion, 1
  Restriccion) pasan al propuesto; nada más. Diez `a9631a64…` → `892f3803…` (8.817/27.632); sin cola `e22fae1a…` → `75f8e599…`
  (8.504/26.129). Registro: 4 filas nuevas, 0 cambiadas. No re-sellé ni toqué la fixture ni `grafos.py`.
- Nueve con alcance: `resolucion_sujetos` (2.605 filas; sin cola 2.534) y registro (291; 286) byte a byte. Cadenas sin parámetro: r2a
  `70d51e42…`/`fa4c1043…`, r2b desarrollo `6e756043…`, sin cola desarrollo `2922b72d…`; con el catálogo vacío por la línea de comando, =
  cadena. Suite de las seis entradas selladas, HEAD contra nuevo, byte a byte.
- Script con el catálogo sin ampliaciones: contra el sellado, lo no explicado son esas 4 y S19; contra la cadena nueva, solo S19; doble
  corrida, 38 iguales y 4 con la ruta normalizada. Gate: suite 48/11/9 sin cambios de estado, LN-6 resuelto con `--generados-resolucion`,
  S4/S5/S28/S23 cambian de cifra y **S19 pasa de PASS a FAIL**.
- (a) = (b) con alcance de prueba (docvig → `Sujeto_entidad_financiera`): las 4 por R4 en los dos caminos, (b) = (a+) en 2.622, 0 sin
  explicar, shapes PASA, el grafo vuelve a `a9631a64…`. Mensaje de E1 con el registro: 2.439 unidades y 13 del candado, byte a byte.
**Hallazgo: S19 bloqueante.** El nodo de cuarentena de la parte A en un documento sin alcance queda sin `padre_sugerido`
(`normalizar_propuestos_r2b`, `sin_rol_de_alcance` = 1; 0 en los sellados): bloquea el gate de los dos grafos de diez y va a pasar en todo
documento sin alcance. Opciones de la autora, antes de re-sellar o de la tanda 1: padre = la sugerencia guardada con marca (ensamblador),
o exención en S19 (shapes). `runner_corpus.py:1261` (E2 por TO del runner) no aplica la parte A.
**Pre-medición B′** (`r2_2_premedicion_b_prima.json`): de 1.362 normas sin `aplica_a`, 986 nombran otro Sujeto (968 sin la raíz; 946 fuera
de los miembros del rol); por TO y los diez más frecuentes en la salida (entidad financiera 589, cliente 329, BCRA 289, …).
**Registro de alcance** (`r2_2_registro_alcance_por_tanda.json`): tanda 1, 12 filas, 9 con alcance y 3 sin (ri_oc, ceninf, cirmo3).
Cablearlo en `prompt_r2b.py` (antes de extraer la tanda 1, tras la firma de la enmienda 4) mueve el candado del mensaje de E1, las claves
de E1 de los documentos con alcance nuevo y una fila de la tabla de reprocesamiento.
**Cierre.** sha256 del repo (salvo `.git` y `.venv`): antes 23.777, después 23.812. De esta unidad cambian los 6 archivos de arriba y
aparecen 9 (este freno, `r2_2_medicion.py` y 7 salidas); lo demás es de otras sesiones (U-E3-LISTAS 10, U-COMP-E1 21, U-LECTURA-ACEPTADAS
4, volumen de Neo4j 1, `.DS_Store` 1). `.pyc`: 2.213. Grep de convenciones: limpio («correo», solo en un label del corpus en la pre-medición).
**Paquete `revision_URERESOL_CAT_FRENO_R2-2/`. Commit, firma de la enmienda 4 y decisión sobre S19: PENDIENTES de la autora. FRENO.**
