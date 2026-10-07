# U-RERESOL-CAT — FRENO R2-3 bis (07/10/2026)

Mandato firmado en `f87ec4a` (notas hasta `803623a`, R2-3). Parche aplicado al repo sobre `803623a`; HEAD `f96ab49` (los tres commits
posteriores no tocan código). USD 0; sin API ni Neo4j; controles sobre una copia nueva del repo con el parche (sin enlaces; sin `.venv`,
`.venv-app` ni el volumen de Neo4j, con `.git`). Cifras en `salidas/r2_3bis_*.json`, de `r2_3bis_medicion.py` (`simulacion`, `controles`;
doble corrida byte a byte, e iguales a las de una primera copia del árbol con R2-3 sin commitear). No re-sellé.
**Hashes (regla d).** El despacho daba a R2-3 por commiteada en `a079275` (es R2-2) y un mensaje posterior, en `d007be8` (O4 de U-E3-LISTAS).
Por decisión de la autora preparé R2-3 bis en una copia y lo apliqué con R2-3 en `803623a` (verificado con `git show --stat`: 14 archivos; el
ensamblador, `selftest_r3`, el procedimiento y el runner son la base sobre la que probé el parche).
**Código** (contra `803623a`). `ensamblar_tanda0.py` +9/−9: la rama b′ (`:906-931`) deja de filtrar por `E4.MOTIVOS_PARTE_A` y toma toda
fila en cuarentena con `id_nodo` de un documento sin alcance, con cualquier motivo; el detalle lista los motivos. Mismas 1.649 líneas: las
anclas de la tabla siguen valiendo. `selftest_r3.py` +77/−10: T11h y T11i al caso nuevo (`sin_match` sin alcance → raíz) y T12 (7 casos).
Procedimiento +4/−3. Una sugerencia que es una instancia cuenta como del catálogo y pasa a su clase, como en R2-3 (T11g).
**Cadenas** (`r2_3bis_controles.json`). Las seis con R2-3 bis: r2b diez `40c54830…` y sin cola diez `8d747e57…`, iguales a R2-3 (también
corridas con el código de HEAD: 33 archivos de `r2/` iguales y el reporte igual con la ruta normalizada); r2a `70d51e42…`/`fa4c1043…`, r2b
desarrollo `6e756043…`, sin cola desarrollo `2922b72d…`, byte a byte. En la tanda 0 ningún propuesto fuera de la parte A está en un documento
sin alcance: resumen igual a R2-3 ((a) 1, `colectivo_sin_sujeto_por_defecto`; (b) 0; `padre_por_defecto` 6; `sin_rol_de_alcance` 0).
Shapes de las dos de diez: PASA, S19 PASS, 0 bloqueantes en FAIL. Suite: seis entradas, HEAD contra R2-3 bis, `.json` y `.md` byte a byte
(r2b con las 3 regresiones preexistentes). Los dos sha no tienen entrada en la fixture.
**Simulación** (`r2_3bis_simulacion.json`). La cadena r2b diez en memoria (sha `40c54830…`, como el ensamblado) hasta la normalización, y
solo la normalización con cap, ext y los dos fuera de `rol_por_to`; con el alcance de la release reproduce la cadena. Los 6 propuestos del
paso c (9 filas `sin_match` sin sugerencia: cap 2 propuestos con 5 filas, ext 4 con 4) van a la raíz con `padre_por_defecto_generico`:
cap sin alcance 2, ext 4, los dos 6; marca (a) 0; `sin_rol_de_alcance` 0 y S19 PASS en las cuatro variantes.
**Observación.** Antes de normalizar, el registro de diez tiene en cuarentena 4 filas colectivas con sugerencia, 19 `mencion_no_verificada`
y 147 `sin_match`, todas sin sugerencia: con sugerencia, R4 las resuelve. Fuera de la parte A, la regla da en la práctica la raíz (o deja el
padre del modelo, que b′ no toca); los casos con sugerencia de T12 (a, c, d) prueban la regla, no un camino que hoy produzca la cadena.
**Selftests** (copia). `selftest_r3` 140/140; con el ensamblador de HEAD, 135/140: fallan T11i y T12a–d (T12e–g pasan, ya cubiertos).
`selftest_reresolver_catalogo` 66/66, `selftest_regression_kg` 184/184, `selftest_prompt_r2b` 55/55, `pruebas_t3bis` 17/17 (JSON igual al
guardado); además `selftest_catalogo_unico` 60/60. `selftest_clave_cache --salida-r2b` OK (A1r 2.449/2.449; A3r 1.386 y 1.054; contraste 44
filas, 0 discrepancias), JSON igual al del repo: F15d, sin filas nuevas.
**Fuera de la lista del despacho.** `r2_3bis_medicion.py`, que produce las dos salidas (CLAUDE.md §5: todo número con su comando).
**Error propio de R2-3 (lo detectó la revisión).** Mi freno de R2-3 afirmó que «12 de las 14 anclas» de la tabla corrían por mi cambio; 10 ya
no caían en lo que nombran desde `2a857db` (nota de revisión en el mandato): trasladé números de línea sin mirar a qué apuntaban.
**Cierre.** sha256 del repo (salvo `.git` y `.venv`): antes 24.009, después 24.022. Míos: cambian los 3 archivos de arriba y aparecen 4 (este
freno, el script y 2 salidas). De otras sesiones: cambian 8 (la enmienda 8, `insumos_escritura.md`, el mandato de U-E3-LISTAS y 5 de
`reports/u_diag_cap3_grafo/`), aparecen 10 y se va 1, todos en esa carpeta. `.pyc`: 2.213. Grep de convenciones: vacío.
**Paquete `revision_URERESOL_CAT_FRENO_R2-3bis/`. Commit de R2-3 bis y firma de la enmienda 4: PENDIENTES de la autora. FRENO.**
