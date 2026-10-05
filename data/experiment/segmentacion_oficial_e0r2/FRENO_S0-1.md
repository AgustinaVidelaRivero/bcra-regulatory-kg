# U-SEG-OFICIAL — FRENO S0-1 (05/10/2026)
Diseño de las siete reglas de S0 con sus censos sobre los 152 TOs. USD 0, sin API; nada implementado en el repo ni commiteado. Diseño completo: `s0_1/DISENO_S0-1.md`; censos y scripts: `s0_1/censos/`, `s0_1/scripts/`.

**Precondiciones** (salidas, con cada commit recortado a su comienzo):
- `git log --oneline -1 -- docs/mandatos/USEG_OFICIAL_segmentacion_e0r2.md` → `e543cb2 U-SEG-OFICIAL FIRMADA por la autora (05/10/2026): …`; primera línea del archivo: «FIRMADO por la autora el 05/10/2026 (firma por mensaje de la autora; versión para firmar en `f1e4e1b`). …».
- `git show e543cb2:docs/mandatos/USEG_OFICIAL_segmentacion_e0r2.md | shasum -a 256` → `44cf30ca0d82a4541654932238ef81055073b407e5ed7b50b92a4a6d3f617c24`. `git cat-file -t 9f6361e` → `commit`.
- `git log --oneline -5` → `e543cb2`, `f1e4e1b`, `00fa231`, `23585e2`, `f948bf2`. `git status --short -- data/experiment/reextraccion_v2 data/experiment/reext_t0` → ` M …/selftest_manifiesto.py`, `?? …/reext_t0/t2_contadores.py`, `?? …/reext_t0/t2_criterio_objecion_omisiones.md`, `?? …/corpus_tanda0/salida_r2b/`.
- FRENO T2 de U-REEXT-T0 sin commit (`git log -- data/experiment/reext_t0` termina en `23585e2`): uso la cota de P4; la capacidad se recalcula con T2. Leí las notas posteriores: `b56984c` (punto 7) y `2faff14` (S1 y S2; no cambia S0-1); en los dos, las 239 líneas firmadas dan `44cf30ca…`.

**Resultado** (prototipo en una copia; `s0_1/censos/ids_que_cambian_S0-1.json`):
- Tanda 0: 57 de 57 archivos iguales byte a byte a `salida_tanda0_r2b/`; `cap::4.2.1.2` no cambia.
- Cambian 23 de los 152 TOs: 20 con ids (423 nuevos y 275 que desaparecen) y 3 solo de texto. Los otros 129, iguales byte a byte en todos sus archivos. Cobertura exacta en los 152.
- R1: «Seccón», «Sección N – …» y «Sección N Título» abren sección, con dos guardas; dmrd, garopt, inspag, opecam y snp_dd (122 ids nuevos).
- R2 (veto): `rdbcra::2.3.1`, `ri_tsa::1.1`, `ri_niif::21.526` y 22 códigos de actividad de ri_dsf. Límite: el catálogo 11.x de rdbcra (ids reales; el texto de cada fila sale corrido).
- R3: snp_mep, venliq y fimipyme recuperan la primera página de cuerpo (80 renglones, 15 ids). Límite: ri_cc pp. 2–47 y ri_tsa pp. 3–61, sub-documentos fuera de toda unidad.
- R4: ri_spi pasa de 1 a 95 unidades (APARTADO X, X.n., X.n.m.); solo actúa en ri_spi.
- R5: propongo ampliar la lista a 9 páginas de 6 TOs (15 renglones, 0 ids); la regla general con guarda además deja sin serializar la tabla002 de fabcra.
- R6: los 5 mini-chunks ya no se saltean (3 partidos; los 2 de manori los absorbe R7); partición por renglones en E0 y en E1: clase A 14 → 0 y B 15 → 0, con la cota de P4.
- R7 (punto 7): el censo da 36, con el mismo reparto (27 ri_mmsef S2, 6 rdbcra 2.3, 2 ri_dcpc 3.1, 1 snp_cheq S3); quedan 0. rdbcra lo resuelve R2, que va antes. Quedan 70 rótulos sin padre de otro mecanismo (manori 58: lista de puntos leída como cuerpo).
- Acompañamiento T de R1 y R7: una tabla partida en intersticiales de un mismo hueco se funde; tablas serializadas 460 → 467.

**Decisiones de la autora** (opciones y efecto, diseño §4): R5, lista o general; adoptar T; ri_cc y ri_tsa (modo de sub-documento, manifiesto o fuera); objetivo de las partes (13.091 o 10.937, con T2); partir en E0 las unidades con tabla (mueve `cap::4.2.1.2`) y umbral 15.052 (20 unidades de 15 TOs); filas del catálogo de rdbcra; lista de puntos de manori.
**Precisión al mandato:** de los 16 renglones «de texto corrido» de la regla general, uno («Código Descripción Explicación», snp_cheq pp. 89–93) es el encabezado de una tabla.

**Convivencia y controles.** Copia sin enlaces, sin `.db`, sin `salida_r2b/` ni `logs/`; no abrí carpetas, bases ni logs de U-REEXT-T0, así que no tengo nada que reportar de ella. sha256 del repo antes y después (exclusiones declaradas, `snapshot_repo.py`): solo cambian mi carpeta, los archivos de los commits de la autora `2bfda2a`, `b56984c`, `7b46800`, `4831ba2` y `2faff14` (`docs/`) y tres `.DS_Store`. `.pyc` y `__pycache__` fuera de `.venv`: 2.424 antes y después.
**Errores propios, con su causa:** (1) los `--exclude` de rsync estaban anclados a una raíz que no era la de la transferencia: la copia trajo `corpus_tanda0/` (473 archivos, con `salida_r2b/` y sin `.db`); la borré sin abrir su contenido. (2) La regla 2, evaluada antes que las validaciones de siempre, cambiaba el motivo registrado de rechazos de la tanda 0 (8 `estructura_<to>.json`): la pasé a veto. (3) Una corrida lanzada en segundo plano dentro de un subshell no corrió. (4) La fusión de T usaba un mapa de segmentos viejo. Los cuatro, detectados y corregidos antes de este freno.
**Paquete de revisión:** `<scratchpad>/revision_USEG_OFICIAL_FRENO_S0-1/` (parche completo y por regla sin aplicar, código del prototipo, comparaciones, `manifest.txt`).
**Grep de convenciones** (`grep -rniEf <patrones> data/experiment/segmentacion_oficial_e0r2` y el mismo sobre el paquete; los patrones, nombres propios de personas y referencias al origen conversacional de una decisión, quedan en un archivo del scratchpad para no escribirlos acá): sin coincidencias.

FRENO. Espero el «seguí» escrito de la autora; no empiezo S0-2.
