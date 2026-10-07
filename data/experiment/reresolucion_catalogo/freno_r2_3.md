# U-RERESOL-CAT — FRENO R2-3 (07/10/2026)

Mandato firmado en `f87ec4a` (notas hasta `604640c`; R2-2 en `a079275`). HEAD `334bdd1` al empezar y `93bebd2` al cerrar (los commits del
medio no tocan rutas de esta unidad). USD 0; sin API ni Neo4j; copia sin enlaces (sin `.venv`, `.venv-app` ni el volumen de Neo4j, con
`.git`); cifras en `salidas/r2_3_*.json`, de `r2_3_medicion.py` (`seco`, `controles`, `anclas`; doble corrida byte a byte). No re-sellé.
**Decisiones de la autora en la sesión (regla d).** (1) El despacho llama «raíz del catálogo» a `Sujeto_sujeto_regulado`; la raíz de
`entrada_esqueleto_r2.json` es `Sujeto_sujeto` (única clase sin padre), y la autora eligió `Sujeto_sujeto` para (b). (2) Con más de una
sugerencia del catálogo en las filas de la parte A de un propuesto, (b). La rama corre antes del paso de las instancias (no justo antes
del paso c) para que una instancia sugerida pase a su clase. La condición de fase del runner está en `:1264`, no en `:1266`.
**Código.** `ensamblar_tanda0.py` +42/−1: `raiz_del_catalogo` (`:830-836`) y la rama b′ de `normalizar_propuestos_r2b` (`:906-931`), con
`padre_desde_sugerencia_modelo` y `padre_por_defecto_generico` en el resumen y por nodo en el detalle. `runner_corpus.py:1261` +1/−1
(`parte_a=perfil_forma_r2(PERFIL)`). `selftest_r3.py` +147 (T11, 9 casos). Procedimiento +3. S19 sin tocar.
**Grafos** (`r2_3_controles.json`). r2b diez `40c54830…` (8.817/27.633), sin cola diez `8d747e57…` (8.504/26.130). Contra `a9631a64…`/
`e22fae1a…`: +1 nodo (`Sujeto_propuesto_las_entidades`), las 4 `aplica_a` de `docvig::3.4` (3 Obligacion, 1 Restriccion) movidas al
propuesto y +1 `padre_sugerido` flaggeada hacia `Sujeto_sujeto_regulado`; `Sujeto_sujeto_regulado` cambia sus procedencias, como en R2-2.
Contra R2-2 (`892f3803…`/`75f8e599…`, reproducidos con el código de HEAD): 1 nodo con 2 claves nuevas en `properties` y 1 arista;
resolución y registro byte a byte. Resumen: (a) 1, (b) 0, `padre_por_defecto` 6, `sin_rol_de_alcance` 1→0; esqueleto 98→99 aristas
flaggeadas (sin cola 96→97). Las otras cuatro cadenas, byte a byte: `70d51e42…`, `fa4c1043…`, `6e756043…`, `2922b72d…`; sus `r2/` iguales a
HEAD salvo el reporte (r2a: la ruta; r2b desarrollo: las 2 claves, en 0). Doble corrida de las de diez: 33 iguales y el reporte con la ruta.
**Shapes r2.** Sellado PASA, R2-2 NO PASA (S19), R2-3 PASA; 0 bloqueantes en FAIL. Contra R2-2 cambian S19 (1→0 incompletos), S1, S2, S4,
S5 (+1 arista), S3, S29, S22 (`padre_sugerido` 98→99; sin cola 96→97) y S28 solo en la ruta del registro.
**Suite.** Seis entradas selladas, HEAD contra nuevo: `.json` y `.md` byte a byte (r2b con RT-C5-3, RT-C6-1 y RT-C6-2, preexistentes).
Los dos grafos nuevos, sin entrada en la fixture; contra los de R2-2: 48/11/9, 0 cambios de estado, detalle de T7, I3 y E4-a5 (+1).
**Runner** (`r2_3_corrida_en_seco_runner_{nuevo,head}.json`). `cerrar_e2_r2` sobre docvig con el directorio del runner como `sys.path[0]`,
el manifiesto `tanda0_10tos_r2b.json` y una copia de lo guardado. Nuevo: las 4 filas de `docvig::3.4` byte a byte iguales a las del
ensamblado r2b (también los 17 renglones de la resolución y los 7 del registro); contra lo guardado cambian 5 de 18 archivos (3 JSONL solo
en `docvig::3.4`, el grafo del TO con +1 nodo y 4 `aplica_a`, y su reporte). HEAD: los 18 iguales a lo guardado y las 4 filas por R4.
**Selftests** (copia). `selftest_r3` 133/133 (HEAD 124/124; T11 con el código de HEAD se corta en T11b), `selftest_reresolver_catalogo`
66/66, `selftest_regression_kg` 184/184, `selftest_catalogo_unico` 60/60 (con `.git`), `selftest_prompt_r2b` 55/55, `pruebas_t3bis` 17/17
(JSON igual al guardado); `selftest_e0`, sin tocar.
**Tabla.** F15d, sin filas nuevas: `selftest_clave_cache --salida-r2b` OK (A1r 2.449/2.449; A3r 1.386 presentes y 1.054 ausentes;
contraste 44 filas), JSON byte a byte igual al del repo. Con 41 líneas más, 12 de las 14 anclas de la tabla al ensamblador corren
(`r2_3_anclas_tabla.json`; `:955` y `:839` ya no caían en lo que nombran en HEAD). No toqué la tabla.
**Hallazgo.** La rama cubre solo los motivos de la parte A: un propuesto sin padre del modelo, en un documento sin alcance y con otro
motivo (`sin_match`, `ambiguo`, `id_fuera_de_catalogo`), sigue en `sin_rol_de_alcance` y S19 falla (T11i). En la tanda 0 no pasa; en los
diez el paso c da el rol a 6 propuestos (9 filas `sin_match`: cap 5, ext 4). Tanda 1 (ri_oc, ceninf, cirmo3 sin alcance): decide la autora.
**Cierre.** sha256 del repo (salvo `.git` y `.venv`): antes 23.950, después 23.957. Míos: cambian los 4 de arriba y aparecen 6 (este freno,
el script y 4 salidas). De otras sesiones: cambian `registro_alcance_por_tanda.md` (la copia tiene el de `93bebd2`), el borrador de la
enmienda 4 y `plan_tesis.md`, y aparece `comp_e1/freno_c2.md`. `.pyc`: 2.213. Grep de convenciones: vacío.
**Paquete `revision_URERESOL_CAT_FRENO_R2-3/`. Commit y firma de la enmienda 4: PENDIENTES de la autora. FRENO.**
