# FRENO T3 de U-REEXT-T0: ensamblados r2b, registro de los grafos y gate (06/10/2026; USD 0 y ninguna llamada a la API; sin commit)

**Precondiciones**: `git log --oneline -1 -- data/experiment/reext_t0` → `ad99ac7`; `git diff --stat 9f6361e HEAD -- …/e0_chunking/` vacío; `pgrep -fl runner_corpus` rc 1; presupuesto 50,401698 de 80; en la fixture (`00fa231`), las dos entradas r2b tienen `kg_sha256` null.

**1. Ensamblados** (`tanda0/code/ensamblar_tanda0.py --manifiesto …/manifiestos/tanda0_ens_<e>_r2b.json --entrada corpus_tanda0/salida_r2b --salida corpus_tanda0/ens_<e>_r2b`). Primero corrí sobre una copia: dos corridas, con los directorios byte a byte iguales (32 y 22 archivos) y `doble_corrida_byte_identica` true. Después corrí en el repo: el `kg.json` sale igual al de la copia.
- **diez `12c5cfc3ea4c46536c72b6eafdb6c890c626b550f76dd96c50a579156975e055`** (8.818 nodos / 27.629 aristas); **desarrollo `6de41495105736330a11e8f19d3625f57987938570e4bcf84aa623bea5a952f0`** (6.992 / 23.442).
- Partes y reparadas: `reporte_ensamblado_r2.json` no las declara, así que las declara `ens_<e>_r2b/r2/declaracion_partes_y_reparadas.json` (`t3/declaracion_partes_reparadas.py`). En los dos grafos: `cap::4.2.1.2` entra por sus partes. La parte 1 está reparada, en la cola humana, con 54 nodos, todos marcados. La parte 2 está `aceptado_con_residuales`, con 25 nodos, 2 marcados por fusión. `cap::3.1.1.2` está reparada y `aceptado_con_residuales`, con 2 nodos, 1 marcado.

**2. Gate**:
- **Shapes** (`scripts/shapes_validator.py --perfil r2 --fase r2b --e0 …/salida_tanda0_r2b --registro-dir … --excepciones …/entrada_esqueleto_r2.json`): **NO PASA en los dos**. Fallan S3 (1 arista fuera de firma: `padre_sugerido` hacia una instancia), S18 (14 y 13 `limite_cuantitativo` sin lista), S19 (7 propuestos incompletos en cada grafo) y S28 (2 y 1 propuestos sin fila). En r2a solo fallaba S18 entre los bloqueantes.
- **Suite** (`scripts/regression_kg.py --perfil r2 --generacion 3 --catalogo …/catalogo_suite_r2.json --politica-cuarentena flaggeada --esperado …`): con la fixture del repo, la entrada r2b no se elige (sha null). Sobre una copia de la fixture con los dos sha (`t3/fixture_con_sha.py`, solo cambian esos dos campos) da **6 regresiones en cada grafo**: BKL-0006 y BKL-0023 (de resuelto a no_aplicable), y RT-C5-3, RT-C6-1, RT-C6-2 y LN-5 (de resuelto a persiste). Además coinciden 53 y quedan 9 NO VERIFICADAS (null): 6 + 53 + 9 = 68. **No se cumple «0 regresiones».**
- Contadores de E1: `tipo_obligacion_requisito_de_estructura` y `tipo_obligacion_normalizados` dan 0 en los 10 TOs. Intrínsecas gen 3 (sobre la E0 r2b con las partes, `t3/e0_con_partes.py`): M10 0/2.440 y 0/1.769; nodos aislados, 18 y 19. Indicadores de cita: **no medidos**, porque necesitan trazas del agente y EV2 no se corre.
- Reproducibilidad (`t3/control_repro_t3.py`, sobre una copia): la E0 legada da 34/34. En `ens_cinco`, `ens_diez` y `ens_desarrollo` r1, 10 archivos salen iguales, 3 iguales con la ruta normalizada y 0 distintos. r2a da `70d51e42…` y `fa4c1043…`.
- Selftests (la batería de T2-ter más `selftest_tools_v2` de los r2b, sobre una copia): igual que en T2-ter. Siguen los dos fallos que vienen de HEAD: `canal_abierto_e1` (45/46) y `manifiesto` (44/49, sobre una copia). Las tools v2 de los r2b dan 232/232.
- Tablero: 26 celdas en la columna r2b (`t3/medicion_tablero_r2b.py`, `t3/escribir_columna_r2b.py`); el diff toca solo la columna 9.

**3. Controles a–r** (`t3/controles_t3.py`; las lecturas, en `t3/salida/lectura_controles_t3.md`):
- **Cumplen**: a (0 sin verificar; cola de 74 entradas en diez y 59 en desarrollo), b, c, f, g, h, j, y BKL-0032, BKL-0033 y BKL-0035.
- **Se informan**: e (42 de 75), i (1.092 y 1.023), k (153 y 77 nodos), l (122 de 377; 0 con dos segmentos) y r (4.109 y 3.841 pares; en r1, 2.429 y 2.096).
- **Vuelven a la autora**: d, porque BKL-0039 no cierra (`ctacte::6.4.7::intro` sigue con una Obligacion que es solo el encabezado); m, porque en BKL-0036 el calificador quedó en una Restriccion y el chunk no tiene Operacion; p, porque en BKL-0028 el miembro del catálogo es la casa de cambio y el texto dice «entidades financieras del país»; q, porque en BKL-0021 la mención reaparece; y o, porque T5 deja 1 arista residual (`ext::3.17.2::intro`).
- **n**: hay 1 `limita` incoherente, marcada; con la marca, la condición de cierre se cumple. De las 4 aristas de r2a, en 2 está mal el tipo y en 2 el predicado.

**4. Neo4j**. En `grafos.py` agregué dos entradas, `KG_Tanda0_{Diez,Desarrollo}_r2b`, y su vista se registra en `t3/registro_vista_r2b.py`. La carga (`tanda0/code/cargar_neo4j_tanda0.py --grafo <clave> --out-dir t3/salida/neo4j_<e>`) da gate 5 OK: carga idempotente, sha de KG_Meta igual al del archivo, huella de Neo4j igual a la del loader y paridad 147/147. La marca de la cola (`t3/control_cola_neo4j.py`) **llega en 334/334 y 281/281 nodos**, con los mismos ids, `props_json` y `cola_chunks`. Las marcas de las 412 y 339 aristas **no llegan**: el cargador sube solo `orden` y `provenances_json`.

**Error propio**: en las dos entradas puse `commit_sellado: None`. Neo4j no guarda las propiedades nulas, así que `verificar_carga` falló con un KeyError después de cargar. Lo cambié a `"PENDIENTE"` y volví a cargar; la recarga borra solo la etiqueta de cada grafo. En el control o, primero filtré por la procedencia del nodo de origen; lo corregí a la procedencia de la arista antes de dar cifras.

**Contradicciones**:
1. El laudo de r2 (`docs/laudo_release_r2_pipeline.md`, BORRADOR) pide en su §3.1 `--perfil congelado` y la fixture `696f3f94…`. Seguí el mandato firmado: `--perfil r2 --fase r2b` y la fixture del repo.
2. `cargar_neo4j_tanda0.py --grafo todos` y `selftest_tools_v2` sin `--grafos` ahora incluyen los r2b, porque toman las claves por prefijo o todas.
3. El reporte del ensamblado y las shapes guardan rutas absolutas, como en r2a.
4. Las salidas JSON quedaron en `reext_t0/t3/salida/`; así leí «scripts en t3/».

**Para la autora**: completar `kg_sha256` en la fixture; sellar los grafos y reemplazar `"PENDIENTE"`; decidir sobre el gate (shapes y 6 regresiones), los controles que vuelven y las marcas de las aristas en Neo4j.

**Controles**: desde el inicio de T3, el sha256 del repo cambia solo en `grafos.py`, el tablero, `ens_diez_r2b/` (37 archivos), `ens_desarrollo_r2b/` (27), `reext_t0/t3/` y el volumen de Neo4j (ignorado por git). Hay 2.213 `.pyc`. El grep de convenciones está en el paquete. **Paquete:** `revision_UREEXT_T0_FRENO_T3/`, en el scratchpad. **Commit PENDIENTE de la autora; los grafos los sella la autora. Espero el «seguí»; T4 no empezó.**
