# FRENO T3-bis de U-REEXT-T0: correcciones del ensamblado, re-ensamblado y gate (06/10/2026; USD 0, sin API; sin commit)

**Precondiciones** (salida completa: `UREEXT_T0_T3bis_precondiciones.txt`, en el paquete):
- a. `git log --oneline -1 -- data/experiment/reext_t0` → `c499eb3 U-REEXT-T0 T3 (USD 0, sin API; …`; `git status --short -- data/experiment scripts docs/tablero_correcciones.md` vacío.
- b. `git diff --stat 9f6361e HEAD -- data/experiment/reextraccion_v2/e0_chunking/` vacío; `pgrep -fl runner_corpus` rc 1.
- c. `shasum -a 256` de los kg de T3: `12c5cfc3…` y `6de41495…`; la fixture tiene `kg_sha256 = null` en las dos entradas r2b.

**Código** (primero sobre una copia, después en el repo; diffs en el paquete):
- `tanda0/code/ensamblar_tanda0.py`, solo con r2b (r1 y r2a no cambian): `normalizar_propuestos_r2b` después del merge (1.a–c); `unidad_desde_rotulo` dentro de `llenar_umbrales_r2` (2); `marcar_umbral_no_cuantificable_r2b` después de los umbrales (3); dos archivos nuevos en `r2/`. `scripts/shapes_validator.py`: `shape_s18_r2` cuenta la marca; `selftest_shapes_congelado.py`, un caso más.
- **Ampliación de la decisión 3, tomada en la sesión**: también se marcan las cuantías que están solo en celdas de una tabla de `tablas_residuales_forzadas_r2b.json`, con el motivo «cuantías solo en tabla residual forzada» y el sha256 de la lista (`98cc96b2…`). La tabla de `cap::6.2.2.6` es `cap::tabla037`, que está en la lista: 1 nodo en cada grafo. **Decidido en la sesión**: se descartan «se» y «cada una».
- **Contradicción** (manda el archivo): la marca va en `properties_no_definidas.umbral_no_cuantificable`, no en `properties`. `NodoR2` es `extra="forbid"` y S26, bloqueante, cierra `properties` por tipo; `modelos_r2.py` tiene el sha256 fijado en `selftest_pyd_r2` y en `manifest_generados_r2.json`.
- **Pruebas**: `t3bis/pruebas_t3bis.py` 17/17. La batería sale igual que en T3: siguen `canal_abierto_e1` 45/46 y `manifiesto` 44/49, que fallan desde HEAD, y `selftest_r3` solo cambia el orden de impresión de un conjunto. Shapes 84/84 (83 y el caso nuevo); suite 184/184.
- **Errores propios**, corregidos antes de dar cifras: esperé mal el orden de las aristas quitadas en una prueba (16/17), y dos scripts derivados tenían f-strings con comillas anidadas, que Python 3.10 no admite.

**Ensamblados** (`ensamblar_tanda0.py --manifiesto …/tanda0_ens_<e>_r2b.json --entrada corpus_tanda0/salida_r2b --salida corpus_tanda0/ens_<e>_r2b`): en la copia, dos corridas con los directorios byte a byte iguales (34 y 24 archivos) y `doble_corrida_byte_identica` true; en el repo, kg igual al de la copia, y reporte igual salvo la ruta. Para el sello: **diez `a9631a64b422bdae634fb05135373c6f04c6272cdf7acd43a1be9f5b6c1f5f57`** (8.816 / 27.632) y **desarrollo `6e7560433148cfe0c476cdd61199c32278187c4196d6f90dc0a38976a6d8e9a2`** (6.990 / 23.445).

**Gate**:
- **Shapes** (`--perfil r2 --fase r2b`): **PASA en los dos grafos**. S3, S18, S19 y S28 dan PASS. S18 cuenta 14 y 13 marcados: 13 y 12 sin cuantía, más 1 de tabla forzada en cada grafo. Las informativas son las de T3.
- **Suite** (`--perfil r2 --generacion 3 --politica-cuarentena flaggeada`, fixture de una copia con los dos sha, `f72518b3…`): diez 48/11/9, desarrollo 45/11/12. LN-5, BKL-0006 y BKL-0023 pasan a **resuelto**. Quedan 3 regresiones, que siguen en persiste y van declaradas: RT-C5-3, RT-C6-1 y RT-C6-2. Coinciden 56 y siguen null las 9 NO VERIFICADAS: 3 + 56 + 9 = 68. Regresiones nuevas: 0.
- Intrínsecas gen 3: M10 0/2.440 y 0/1.769. Reproducibilidad (`t3/control_repro_t3.py`), igual que en T3: E0 34/34; los tres r1, 10 iguales, 3 iguales con la ruta normalizada y 0 distintos; r2a `70d51e42…` y `fa4c1043…`; el repo, igual antes y después.

**Listas** (`t3bis/salida/declaraciones_t3bis.md`, de `t3bis/declaraciones_t3bis.py`):
- Los 7 sin padre de T3: 6 reciben `padre_por_defecto`, 4 de ext hacia `Sujeto_rol_entidad_autorizada_exterior` y 2 de cap hacia `Sujeto_rol_alcance_capmin`; «cada una» se descarta. El padre hacia una instancia («se» → `Sujeto_sefyc`) sale con su propuesto.
- Renombrados con fila: `…la_entidad__ctacte`, 1 fila (solo en diez), y `…la_entidad__ext`, 14. Aristas quitadas: 2 en cada grafo, en `ens_<grafo>_r2b/r2/propuestos_descartados_aristas_quitadas.jsonl`.
- Unidad del rótulo: en cada grafo ganan valor 2 elementos, de cap, en 2 nodos del 1.2: «5.000» → 5000000000 moneda ARS y «2.500» → 2500000000.

**Declaraciones de la decisión 5** (textos completos en `declaraciones_t3bis.md`):
- RT-C6-1 y RT-C6-2: la norma dice «asociaciones mutuales o cooperativas» y la descripción, «mutuales y cooperativas». Es un error de fidelidad del modelo en la descripción («o» → «y»); el tramo, «excepto que se trate de asociaciones mutuales o cooperativas», es fiel.
- RT-C5-3: la norma dice «antes de los 60 días contados desde la fecha en que se verificó la mora» y el nodo, «antes de 60 días desde la mora». Persiste por una paráfrasis sin cambio de sentido.
- BKL-0039 no cierra (prefijo congelado; va a la lista de T5). BKL-0036 queda cerrada: la Restriccion conserva «en condiciones más favorables que las acordadas de ordinario». BKL-0028 pasa a U-RERESOL-CAT.
- BKL-0021: opción (c), y mientras tanto (d); los dos propuestos siguen en cuarentena, con 4 `aplica_a` y 4 filas. T5 no tiene casos: la norma dice «nominar una única entidad financiera local». `remite_a` no se toca: 5 de 1.385 citas siguen sin registrar (nota `07ef3c9`).

**Controles a–r** (`t3bis/salida/controles_t3bis.json`): solo cambian f (2 elementos pasan de `limite_relativo:sin_marcador` a `sin_marcador`, con la regla anterior en `originales`) y k (nodos con `properties_no_definidas`: de 153 a 167 en diez y de 77 a 90 en desarrollo). Las lecturas de T3 siguen valiendo.

**Neo4j y tablero**: en `grafos.py` reemplacé las dos entradas (sha y conteos nuevos, registro en `t3bis/registro_vista_r2b.py`, `commit_sellado` «PENDIENTE»). Gate 5 OK, paridad 147/147; la marca de la cola llega en 334/334 y 281/281 nodos. Las marcas de las aristas no se cargan, como en T3. En el tablero reescribí 22 celdas; las 4 «No medible» quedan igual y el diff toca solo la columna 9.

**Para la autora**: completar los `kg_sha256` de la fixture con estos sha y sellar los grafos (PENDIENTE); confirmar `properties_no_definidas` para la marca. La regla de la mención vacía no alcanza a «podrán» ni a «Deberá rechazarse», que son verbos.

**Controles de cierre**: desde el inicio de T3-bis, el sha256 del repo cambia solo en los 3 archivos de código, `grafos.py`, el tablero, `ens_diez_r2b/` y `ens_desarrollo_r2b/` (8 cambian y 2 son nuevos en cada uno), `reext_t0/t3bis/` (17 nuevos), este freno y el volumen de Neo4j, que git ignora. Hay 2.213 `.pyc`. El grep de convenciones está en el paquete. **Paquete:** `revision_UREEXT_T0_FRENO_T3bis/`, en el scratchpad. **Commit PENDIENTE de la autora. Espero el «seguí»; T4 no empezó.**
