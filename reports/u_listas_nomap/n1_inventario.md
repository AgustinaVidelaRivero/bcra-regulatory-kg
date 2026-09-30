# U-LISTAS-NOMAP — N1: inventario de las listas cerradas y mediciones

Mandato `docs/mandatos/ULISTAS_NOMAP_diseno.md`. Solo lectura, USD 0, sin API ni Neo4j. Comando: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B reports/u_listas_nomap/u_listas_n1.py --out-dir reports/u_listas_nomap`. Todo número de este archivo sale de `n1_inventario.json` (misma corrida); cada tabla dice de qué clave.

## 1. Reglas declaradas antes de aplicarse

El texto completo de cada regla está en el docstring de `reports/u_listas_nomap/u_listas_n1.py`.

- **R-LISTAS**: listas del prefijo v3 (perfil v3_b54) y claves de [c11]; vacío o ausente = fuera.
- **R-CAPAS**: L0 crudo primer intento; L0r crudo de reintentos E3; L1 validado primer intento; L2 entrada efectiva de E2 con cola flaggeada; L3 grafo.
- **R-NORM**: une cortes por guion de fin de línea; NFKD sin diacríticos; minúsculas; no alfanumérico→espacio; presencia con límites de palabra en texto propio + heredado de E0.
- **R-FORZ**: sujeto_id del bloque v3 sin label/alias presente; amplia (principal) con label sin paréntesis, contenido de paréntesis (no roles) y singularización r1_e4._singular; estricta: label y alias.
- **R-LIT**: sujeto_propuesto normalizado (R-NORM) presente en texto propio o heredado.
- **R-MUESTRA**: pares de la tanda 0, otra_clase_o_instancia, posible forzado amplia; orden (chunk_id, sujeto_id); random.Random(20260930).sample(población, 30).
- **R-CAT**: JSON v3 + ids del bloque ausentes del JSON (label y nivel del perfil, sin alias).
- **R-OMIS**: omisiones_no_prosa con al menos un string no vacío; capa finales = [c15].

Grupos: r1 = crudo de `corpus_v2/salida` (cinco TOs, perfil produccion_dev) y grafo KG-Reextraído-r1; desarrollo, cinco y diez = crudo de `corpus_tanda0/salida_dirigida` (perfil v3_b54; la entrada de los ensamblados, `ens_desarrollo/r1/reporte_ensamblado_r1.json:22`) y el `r1/kg.json` de cada ensamblado. diez = desarrollo + cinco.

## 2. Entradas y controles

| clave | ruta | sha256 |
|---|---|---|
| e0_cap | `data/experiment/reextraccion_v2/e0_chunking/salida_tanda0/chunks_cap.json` | `1931138dac0a107a…` |
| e0_cla | `data/experiment/reextraccion_v2/e0_chunking/salida_tanda0/chunks_cla.json` | `98808886a406d832…` |
| e0_ctacte | `data/experiment/reextraccion_v2/e0_chunking/salida_tanda0/chunks_ctacte.json` | `e65fd5e7defc68c0…` |
| e0_docvig | `data/experiment/reextraccion_v2/e0_chunking/salida_tanda0/chunks_docvig.json` | `97b62c050d8880b3…` |
| e0_ext | `data/experiment/reextraccion_v2/e0_chunking/salida_tanda0/chunks_ext.json` | `cbcd1a86f55ea491…` |
| e0_lingob | `data/experiment/reextraccion_v2/e0_chunking/salida_tanda0/chunks_lingob.json` | `8c502976b7e34989…` |
| e0_pagjub | `data/experiment/reextraccion_v2/e0_chunking/salida_tanda0/chunks_pagjub.json` | `1bba0713dae796c4…` |
| e0_polcre | `data/experiment/reextraccion_v2/e0_chunking/salida_tanda0/chunks_polcre.json` | `9f6518549f4fbade…` |
| e0_pro | `data/experiment/reextraccion_v2/e0_chunking/salida_tanda0/chunks_pro.json` | `d8717d1c7423bb5f…` |
| e0_ric | `data/experiment/reextraccion_v2/e0_chunking/salida_tanda0/chunks_ric.json` | `fafebb82e07b3419…` |
| r1_cap_compact | `data/experiment/reextraccion_v2/corpus_v2/salida/cap/extracciones_e1_compact.jsonl` | `4ab8e8279c9e77ef…` |
| r1_cap_finales_ext | `data/experiment/reextraccion_v2/corpus_v2/salida/cap/extracciones_finales_cap.jsonl` | `7ff2f33ef15cb4a6…` |
| r1_cap_finales | `data/experiment/reextraccion_v2/corpus_v2/salida/cap/finales.jsonl` | `c323781ec7b1352f…` |
| r1_cla_compact | `data/experiment/reextraccion_v2/corpus_v2/salida/cla/extracciones_e1_compact.jsonl` | `544378cb6107e771…` |
| r1_cla_finales_ext | `data/experiment/reextraccion_v2/corpus_v2/salida/cla/extracciones_finales_cla.jsonl` | `dfcb4643ecd24d63…` |
| r1_cla_finales | `data/experiment/reextraccion_v2/corpus_v2/salida/cla/finales.jsonl` | `961d99689bd007f7…` |
| r1_ext_compact | `data/experiment/reextraccion_v2/corpus_v2/salida/ext/extracciones_e1_compact.jsonl` | `8f685491305fe726…` |
| r1_ext_finales_ext | `data/experiment/reextraccion_v2/corpus_v2/salida/ext/extracciones_finales_ext.jsonl` | `c477948f6eabbb16…` |
| r1_ext_finales | `data/experiment/reextraccion_v2/corpus_v2/salida/ext/finales.jsonl` | `196d0eb454dfa624…` |
| r1_pro_compact | `data/experiment/reextraccion_v2/corpus_v2/salida/pro/extracciones_e1_compact.jsonl` | `799034d71205d1c6…` |
| r1_pro_finales_ext | `data/experiment/reextraccion_v2/corpus_v2/salida/pro/extracciones_finales_pro.jsonl` | `537b1996720c912c…` |
| r1_pro_finales | `data/experiment/reextraccion_v2/corpus_v2/salida/pro/finales.jsonl` | `99f3fe392accd595…` |
| r1_ric_compact | `data/experiment/reextraccion_v2/corpus_v2/salida/ric/extracciones_e1_compact.jsonl` | `0963a629a7d3c770…` |
| r1_ric_finales_ext | `data/experiment/reextraccion_v2/corpus_v2/salida/ric/extracciones_finales_ric.jsonl` | `9b7f26641e2f9f2b…` |
| r1_ric_finales | `data/experiment/reextraccion_v2/corpus_v2/salida/ric/finales.jsonl` | `cd2b0bfe06ca0482…` |
| t0_cap_compact | `data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida/cap/extracciones_e1_compact.jsonl` | `d4c23128a85ceb89…` |
| t0_cap_finales_ext | `data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida/cap/extracciones_finales_cap.jsonl` | `3f1b893e73890d57…` |
| t0_cap_finales | `data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida/cap/finales.jsonl` | `2d5b4ee5bcd78564…` |
| t0_cla_compact | `data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida/cla/extracciones_e1_compact.jsonl` | `1d3baa2349a1298e…` |
| t0_cla_finales_ext | `data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida/cla/extracciones_finales_cla.jsonl` | `e552ce9645666f1f…` |
| t0_cla_finales | `data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida/cla/finales.jsonl` | `bfa62961c3abd1e7…` |
| t0_ctacte_compact | `data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida/ctacte/extracciones_e1_compact.jsonl` | `74e45a2551f9da7e…` |
| t0_ctacte_finales_ext | `data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida/ctacte/extracciones_finales_ctacte.jsonl` | `5e51671103b70eb5…` |
| t0_ctacte_finales | `data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida/ctacte/finales.jsonl` | `d1d64e4902b52d6a…` |
| t0_docvig_compact | `data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida/docvig/extracciones_e1_compact.jsonl` | `ef8945e5a2d4b3e4…` |
| t0_docvig_finales_ext | `data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida/docvig/extracciones_finales_docvig.jsonl` | `f1bd683f9b244611…` |
| t0_docvig_finales | `data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida/docvig/finales.jsonl` | `b75e5b8556848454…` |
| t0_ext_compact | `data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida/ext/extracciones_e1_compact.jsonl` | `72836a819c4c3ed5…` |
| t0_ext_finales_ext | `data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida/ext/extracciones_finales_ext.jsonl` | `d92c36b2ea8fe344…` |
| t0_ext_finales | `data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida/ext/finales.jsonl` | `a289fcb706a50047…` |
| t0_lingob_compact | `data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida/lingob/extracciones_e1_compact.jsonl` | `c116092a98aaee9d…` |
| t0_lingob_finales_ext | `data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida/lingob/extracciones_finales_lingob.jsonl` | `99597c13081b68b8…` |
| t0_lingob_finales | `data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida/lingob/finales.jsonl` | `3d04f2cf24285d27…` |
| t0_pagjub_compact | `data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida/pagjub/extracciones_e1_compact.jsonl` | `29a67c758750506b…` |
| t0_pagjub_finales_ext | `data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida/pagjub/extracciones_finales_pagjub.jsonl` | `0dfcc6c8dcadb55a…` |
| t0_pagjub_finales | `data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida/pagjub/finales.jsonl` | `eb1833e6e07ef98a…` |
| t0_polcre_compact | `data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida/polcre/extracciones_e1_compact.jsonl` | `d45adb792d4f8ced…` |
| t0_polcre_finales_ext | `data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida/polcre/extracciones_finales_polcre.jsonl` | `d43c6ea43b0b144b…` |
| t0_polcre_finales | `data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida/polcre/finales.jsonl` | `2ed29a7f22211be3…` |
| t0_pro_compact | `data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida/pro/extracciones_e1_compact.jsonl` | `1142c658a87c4b75…` |
| t0_pro_finales_ext | `data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida/pro/extracciones_finales_pro.jsonl` | `eba94c87656c0bc1…` |
| t0_pro_finales | `data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida/pro/finales.jsonl` | `54df0f607446ea5a…` |
| t0_ric_compact | `data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida/ric/extracciones_e1_compact.jsonl` | `32162401e3d06125…` |
| t0_ric_finales_ext | `data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida/ric/extracciones_finales_ric.jsonl` | `ecaaf68d06c0dc6a…` |
| t0_ric_finales | `data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida/ric/finales.jsonl` | `cbf53282c1e66f47…` |
| r1_kg.json | `data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json` | `0226e9477baee02d…` |
| r1_e4_propuestos.json | `data/experiment/reextraccion_v2/corpus_v2/salida_r1/e4_propuestos.json` | `ad8e2ef78fb2db73…` |
| r1_e5_esqueleto.json | `data/experiment/reextraccion_v2/corpus_v2/salida_r1/e5_esqueleto.json` | `831b1314b382135d…` |
| desarrollo_kg.json | `data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo/r1/kg.json` | `eab2fdd01dec4dad…` |
| desarrollo_e4_propuestos.json | `data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo/r1/e4_propuestos.json` | `1c664faef4bb1f50…` |
| desarrollo_e5_esqueleto.json | `data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo/r1/e5_esqueleto.json` | `eb7f818144823746…` |
| cinco_kg.json | `data/experiment/reextraccion_v2/corpus_tanda0/ens_cinco/r1/kg.json` | `4097d4fd3f300cb1…` |
| cinco_e4_propuestos.json | `data/experiment/reextraccion_v2/corpus_tanda0/ens_cinco/r1/e4_propuestos.json` | `385aafd62b7e8278…` |
| cinco_e5_esqueleto.json | `data/experiment/reextraccion_v2/corpus_tanda0/ens_cinco/r1/e5_esqueleto.json` | `a53b744feced711a…` |
| diez_kg.json | `data/experiment/reextraccion_v2/corpus_tanda0/ens_diez/r1/kg.json` | `dd42d6d9c0c8379d…` |
| diez_e4_propuestos.json | `data/experiment/reextraccion_v2/corpus_tanda0/ens_diez/r1/e4_propuestos.json` | `73a20ed1c24b06c5…` |
| diez_e5_esqueleto.json | `data/experiment/reextraccion_v2/corpus_tanda0/ens_diez/r1/e5_esqueleto.json` | `1037cf023e3e0a3e…` |
| catalogo_json_v3 | `data/experiment/esq_v3_miembros/esquema_v3_clases.json` | `dad88cc92afc53e9…` |
| prompt_v3_b54 | `data/experiment/b54_catalogo_v3/code/prompt_v3_b54.py` | `fb0a2bd81faabe01…` |
| r1_e4 | `data/experiment/reextraccion_v2/corpus_v2/r1_e4.py` | `179db09c2e87dd73…` |
| e1_reintentos_db | `data/experiment/reextraccion_v2/e3_verificador/cache/e1_reintentos.db` | `e71380308cbe3dde…` |
| t0_cap_finales_ext_salida_no_dirigida | `data/experiment/reextraccion_v2/corpus_tanda0/salida/cap/extracciones_finales_cap.jsonl` | `c56743b43ae14ea6…` |

Controles contra `docs/tablero_correcciones.md` ([c11], [c12], [c13]) sobre KG-Tanda0-Desarrollo-r1 (clave `controles_tablero_desarrollo`; el script frena si no coinciden):

| cifra | tablero | obtenido |
|---|---|---|
| Restriccion.tipo | 4 | 4 |
| Comunicacion.tipo | 6 | 6 |
| claves | 9 | 9 |
| propuestos | 22 | 22 |
| resueltos | 3 | 3 |
| cuarentena | 19 | 19 |
| solo_bloque | 6 | 6 |
| solo_json | 5 | 5 |

E0 de la tanda 0 idéntico byte a byte al de r1 (`salida_enm01`) en los cinco TOs de desarrollo: True (clave `e0_tanda0_identico_a_enm01`).

Reintentos de E3 en `e1_reintentos.db` (clave `reintentos_db`):

| generación | namespace | entradas | asignadas a un chunk | unidades distintas | no asignadas | de otros TOs | reintentos en finales (unidades) | entradas de unidades sin reintento en finales | unidades con más entradas que reintentos | unidades con reintento sin entrada |
|---|---|---|---|---|---|---|---|---|---|---|
| r1 | `4793d6152608` | 431 | 431 | 428 | 0 | 0 | 406 (406) | 22 | 3 | 0 |
| t0 | `54a111e2175f` | 255 | 255 | 255 | 0 | 0 | 255 (255) | 0 | 0 | 0 |

L0r inventaría todas las entradas asignadas; el crudo del reintento no está en `finales.jsonl` (tablero, fila «Crudo del reintento de E3 sin persistir», [c16]).

## 3. Inventario por lista cerrada

Clave `resumen_por_lista.<lista>.<grupo>`. Columnas: emitidos y fuera de lista en el crudo L0; efecto del validador sobre los fuera de lista del crudo (mismo registro, L0→L1): rechazados (por cualquier motivo), normalizados a «otra», anulados (padre) y que pasaron; fuera de lista en L1; emitidos y fuera en el crudo de los reintentos L0r; fuera en la entrada de E2 (L2); fuera en el grafo L3 ([c11]).

### Tipos de entidad (9)

| grupo | emitidos L0 | fuera L0 | rechazados | normalizados | pasaron | fuera L1 | emitidos L0r | fuera L0r | fuera L2 | fuera L3 |
|---|---|---|---|---|---|---|---|---|---|---|
| r1 | 8092 | 0 | 0 | 0 | 0 | 0 | 2720 | 0 | 0 | 0 |
| desarrollo | 8008 | 2 | 2 | 0 | 0 | 0 | 1149 | 0 | 0 | 0 |
| cinco | 2523 | 2 | 2 | 0 | 0 | 0 | 266 | 0 | 0 | 0 |
| diez | 10531 | 4 | 4 | 0 | 0 | 0 | 1415 | 0 | 0 | 0 |

Valores fuera de lista (L0 crudo; L3 grafo), clave `grupos.<g>.capas.crudo.fuera` y `grafos.<g>`:

- r1: L0 —. L3 —.
- desarrollo: L0 `Restriction` 2. L3 —.
- cinco: L0 `Recomendacion` 2. L3 —.
- diez: L0 `Recomendacion` 2, `Restriction` 2. L3 —.

Estado tras el validador de cada valor fuera de lista del crudo (clave `grupos.<g>.efecto_validador`): r1: —; desarrollo: rechazado:type_invalido 2; cinco: rechazado:type_invalido 2; diez: rechazado:type_invalido 4.

### Predicados (13)

| grupo | emitidos L0 | fuera L0 | rechazados | normalizados | pasaron | fuera L1 | emitidos L0r | fuera L0r | fuera L2 | fuera L3 |
|---|---|---|---|---|---|---|---|---|---|---|
| r1 | 11827 | 2 | 2 | 0 | 0 | 0 | 4360 | 2 | 0 | 0 (+123 del pipeline) |
| desarrollo | 11322 | 1 | 1 | 0 | 0 | 0 | 1865 | 0 | 0 | 0 (+135 del pipeline) |
| cinco | 3419 | 1 | 1 | 0 | 0 | 0 | 358 | 0 | 0 | 0 (+128 del pipeline) |
| diez | 14741 | 2 | 2 | 0 | 0 | 0 | 2223 | 0 | 0 | 0 (+146 del pipeline) |

Valores fuera de lista (L0 crudo; L3 grafo), clave `grupos.<g>.capas.crudo.fuera` y `grafos.<g>`:

- r1: L0 `aplicaA` 1, `exceptua_restriccion` 1. L3 `subclase_de|esqueleto` 57, `padre_sugerido|cuarentena_flaggeada` 41, `miembro_de|esqueleto` 17, `instancia_de|esqueleto` 7, `parte_de|esqueleto` 1.
- desarrollo: L0 `establec\nida_en` 1. L3 `subclase_de|esqueleto` 58, `miembro_de|esqueleto` 51, `padre_sugerido|cuarentena_flaggeada` 18, `instancia_de|esqueleto` 7, `parte_de|esqueleto` 1.
- cinco: L0 `establec ida_en` 1. L3 `subclase_de|esqueleto` 58, `miembro_de|esqueleto` 51, `padre_sugerido|cuarentena_flaggeada` 11, `instancia_de|esqueleto` 7, `parte_de|esqueleto` 1.
- diez: L0 `establec\nida_en` 1, `establec ida_en` 1. L3 `subclase_de|esqueleto` 58, `miembro_de|esqueleto` 51, `padre_sugerido|cuarentena_flaggeada` 29, `instancia_de|esqueleto` 7, `parte_de|esqueleto` 1.

Estado tras el validador de cada valor fuera de lista del crudo (clave `grupos.<g>.efecto_validador`): r1: rechazado:predicado_invalido 2; desarrollo: rechazado:predicado_invalido 1; cinco: rechazado:predicado_invalido 1; diez: rechazado:predicado_invalido 2.

### Catálogo de sujetos, sujeto_id (102)

| grupo | emitidos L0 | fuera L0 | rechazados | normalizados | pasaron | fuera L1 | emitidos L0r | fuera L0r | fuera L2 | fuera L3 |
|---|---|---|---|---|---|---|---|---|---|---|
| r1 | 3449 | 0 | 0 | 0 | 0 | 0 | 1172 | 0 | 0 | 0 (+5 nodos del esqueleto) |
| desarrollo | 3014 | 0 | 0 | 0 | 0 | 0 | 477 | 0 | 0 | 0 (+5 nodos del esqueleto) |
| cinco | 1027 | 0 | 0 | 0 | 0 | 0 | 84 | 0 | 0 | 0 (+5 nodos del esqueleto) |
| diez | 4041 | 0 | 0 | 0 | 0 | 0 | 561 | 0 | 0 | 0 (+5 nodos del esqueleto) |

Valores fuera de lista (L0 crudo; L3 grafo), clave `grupos.<g>.capas.crudo.fuera` y `grafos.<g>`:

- r1: L0 —. L3 `Sujeto_acreedor_del_exterior` solo JSON, `Sujeto_autoridad_nacional_de_aplicacion` solo JSON, `Sujeto_secretaria_de_comercio` solo JSON, `Sujeto_secretaria_de_energia` solo JSON, `Sujeto_secretaria_de_transporte` solo JSON.
- desarrollo: L0 —. L3 `Sujeto_acreedor_del_exterior` solo JSON, `Sujeto_autoridad_nacional_de_aplicacion` solo JSON, `Sujeto_secretaria_de_comercio` solo JSON, `Sujeto_secretaria_de_energia` solo JSON, `Sujeto_secretaria_de_transporte` solo JSON.
- cinco: L0 —. L3 `Sujeto_acreedor_del_exterior` solo JSON, `Sujeto_autoridad_nacional_de_aplicacion` solo JSON, `Sujeto_secretaria_de_comercio` solo JSON, `Sujeto_secretaria_de_energia` solo JSON, `Sujeto_secretaria_de_transporte` solo JSON.
- diez: L0 —. L3 `Sujeto_acreedor_del_exterior` solo JSON, `Sujeto_autoridad_nacional_de_aplicacion` solo JSON, `Sujeto_secretaria_de_comercio` solo JSON, `Sujeto_secretaria_de_energia` solo JSON, `Sujeto_secretaria_de_transporte` solo JSON.

Estado tras el validador de cada valor fuera de lista del crudo (clave `grupos.<g>.efecto_validador`): r1: —; desarrollo: —; cinco: —; diez: —.

### Obligacion.tipo (enum de 6)

| grupo | emitidos L0 | fuera L0 | rechazados | normalizados | pasaron | fuera L1 | emitidos L0r | fuera L0r | fuera L2 | fuera L3 |
|---|---|---|---|---|---|---|---|---|---|---|
| r1 | 2495 | 2 | 0 | 0 | 2 | 2 | 843 | 1 | 1 | 1 |
| desarrollo | 1627 | 0 | 0 | 0 | 0 | 0 | 269 | 0 | 0 | 0 |
| cinco | 738 | 3 | 0 | 3 | 0 | 0 | 68 | 0 | 0 | 0 |
| diez | 2365 | 3 | 0 | 3 | 0 | 0 | 337 | 0 | 0 | 0 |

Valores fuera de lista (L0 crudo; L3 grafo), clave `grupos.<g>.capas.crudo.fuera` y `grafos.<g>`:

- r1: L0 `verificacion` 1, `verificacion_informativa` 1. L3 `verificacion_informativa` 1.
- desarrollo: L0 —. L3 —.
- cinco: L0 `evaluacion` 1, `obtención_de_datos` 1, `pago` 1. L3 —.
- diez: L0 `evaluacion` 1, `obtención_de_datos` 1, `pago` 1. L3 —.

Estado tras el validador de cada valor fuera de lista del crudo (clave `grupos.<g>.efecto_validador`): r1: paso 2; desarrollo: —; cinco: normalizado_a_otra 3; diez: normalizado_a_otra 3.

### Restriccion.tipo (3)

| grupo | emitidos L0 | fuera L0 | rechazados | normalizados | pasaron | fuera L1 | emitidos L0r | fuera L0r | fuera L2 | fuera L3 |
|---|---|---|---|---|---|---|---|---|---|---|
| r1 | 1313 | 0 | 0 | 0 | 0 | 0 | 501 | 0 | 0 | 0 |
| desarrollo | 658 | 4 | 0 | 0 | 4 | 4 | 96 | 0 | 4 | 4 |
| cinco | 160 | 0 | 0 | 0 | 0 | 0 | 18 | 0 | 0 | 0 |
| diez | 818 | 4 | 0 | 0 | 4 | 4 | 114 | 0 | 4 | 4 |

Valores fuera de lista (L0 crudo; L3 grafo), clave `grupos.<g>.capas.crudo.fuera` y `grafos.<g>`:

- r1: L0 —. L3 —.
- desarrollo: L0 `limite_temporal` 3, `obligacion_cualitativa` 1. L3 `limite_temporal` 3, `obligacion_cualitativa` 1.
- cinco: L0 —. L3 —.
- diez: L0 `limite_temporal` 3, `obligacion_cualitativa` 1. L3 `limite_temporal` 3, `obligacion_cualitativa` 1.

Estado tras el validador de cada valor fuera de lista del crudo (clave `grupos.<g>.efecto_validador`): r1: —; desarrollo: paso 4; cinco: —; diez: paso 4.

### Comunicacion.tipo (3)

| grupo | emitidos L0 | fuera L0 | rechazados | normalizados | pasaron | fuera L1 | emitidos L0r | fuera L0r | fuera L2 | fuera L3 |
|---|---|---|---|---|---|---|---|---|---|---|
| r1 | 41 | 14 | 0 | 0 | 14 | 14 | 21 | 4 | 14 | 14 |
| desarrollo | 27 | 4 | 0 | 0 | 4 | 4 | 4 | 2 | 6 | 6 |
| cinco | 4 | 1 | 0 | 0 | 1 | 1 | 1 | 1 | 2 | 2 |
| diez | 31 | 5 | 0 | 0 | 5 | 5 | 5 | 3 | 8 | 8 |

Valores fuera de lista (L0 crudo; L3 grafo), clave `grupos.<g>.capas.crudo.fuera` y `grafos.<g>`:

- r1: L0 `(vacío)` 2, `interna` 2, `referencia_normativa` 2, `Decreto` 1, `LEY` 1, `MINISTERIAL` 1, `Resolución` 1, `decreto` 1, `normas` 1, `referencia` 1, `referencia a normas` 1. L3 `(vacío)` 2, `interna` 2, `referencia_normativa` 2, `Decreto` 1, `LEY` 1, `MINISTERIAL` 1, `norma` 1, `normas` 1, `referencia` 1, `referencia a normas` 1, `referencia_interna` 1.
- desarrollo: L0 `referencia` 3, `TO` 1. L3 `referencia` 3, `otro` 2, `TO` 1.
- cinco: L0 `Resolución` 1. L3 `(vacío)` 1, `Resolución` 1.
- diez: L0 `referencia` 3, `Resolución` 1, `TO` 1. L3 `referencia` 3, `otro` 2, `(vacío)` 1, `Resolución` 1, `TO` 1.

Estado tras el validador de cada valor fuera de lista del crudo (clave `grupos.<g>.efecto_validador`): r1: paso 14; desarrollo: paso 4; cinco: paso 1; diez: paso 5.

### Claves de properties por tipo ([c11])

| grupo | emitidos L0 | fuera L0 | rechazados | normalizados | pasaron | fuera L1 | emitidos L0r | fuera L0r | fuera L2 | fuera L3 |
|---|---|---|---|---|---|---|---|---|---|---|
| r1 | 16210 | 10 | 0 | 0 | 10 | 10 | 5235 | 9 | 17 | 12 |
| desarrollo | 16600 | 6 | 0 | 0 | 6 | 6 | 2211 | 5 | 9 | 9 |
| cinco | 5545 | 4 | 0 | 0 | 4 | 4 | 560 | 0 | 4 | 4 |
| diez | 22145 | 10 | 0 | 0 | 10 | 10 | 2771 | 5 | 13 | 13 |

Valores fuera de lista (L0 crudo; L3 grafo), clave `grupos.<g>.capas.crudo.fuera` y `grafos.<g>`:

- r1: L0 `Obligacion.plazo_o_frecuencia` 4, `TextoOrdenado.descripcion` 4, `Obligacion.umbral` 1, `TextoOrdenado.tipo` 1. L3 `Obligacion.plazo_o_frecuencia` 5, `TextoOrdenado.descripcion` 3, `Obligacion.modalidad_deonica` 1, `Obligacion.plazo_o_condicion` 1, `Obligacion.umbral` 1, `TextoOrdenado.tipo` 1.
- desarrollo: L0 `Obligacion.plazo_frecuencia` 1, `Obligacion.plazo_o_frecuencia` 1, `Obligacion.umbral` 1, `Operacion.etapa` 1, `Potestad.tipo` 1, `Potestad.umbral` 1. L3 `Obligacion.plazo_o_frecuencia` 4, `Obligacion.plazo_frecuencia` 1, `Obligacion.umbral` 1, `Operacion.etapa` 1, `Potestad.tipo` 1, `Potestad.umbral` 1.
- cinco: L0 `Obligacion.destinatario` 2, `Obligacion.plazo_frecuencia` 1, `Obligacion.referencia_normativa` 1. L3 `Obligacion.destinatario` 2, `Obligacion.plazo_frecuencia` 1, `Obligacion.referencia_normativa` 1.
- diez: L0 `Obligacion.destinatario` 2, `Obligacion.plazo_frecuencia` 2, `Obligacion.plazo_o_frecuencia` 1, `Obligacion.referencia_normativa` 1, `Obligacion.umbral` 1, `Operacion.etapa` 1, `Potestad.tipo` 1, `Potestad.umbral` 1. L3 `Obligacion.plazo_o_frecuencia` 4, `Obligacion.destinatario` 2, `Obligacion.plazo_frecuencia` 2, `Obligacion.referencia_normativa` 1, `Obligacion.umbral` 1, `Operacion.etapa` 1, `Potestad.tipo` 1, `Potestad.umbral` 1.

Estado tras el validador de cada valor fuera de lista del crudo (clave `grupos.<g>.efecto_validador`): r1: paso 10; desarrollo: paso 6; cinco: paso 4; diez: paso 10.

### Operacion.tipo (texto libre, se describe)

| grupo | Operacion en L0 | valores distintos L0 | vacíos L0 | nodos Operacion L3 | valores distintos L3 |
|---|---|---|---|---|---|
| r1 | 2021 | 1652 | 0 | 1957 | 1651 |
| desarrollo | 1587 | 1035 | 0 | 1555 | 1027 |
| cinco | 523 | 373 | 0 | 492 | 369 |
| diez | 2110 | 1381 | 0 | 2047 | 1370 |

- r1, diez más frecuentes en L0: `clasificación de deudor` 24, `compra de moneda extranjera` 22, `presentacion_informativa` 21, `calculo` 15, `pago de importación` 9, `financiacion` 8, `acceso al mercado de cambios` 7, `asignacion_ponderador_riesgo` 7, `clasificacion_de_deudor` 7, `emisión de certificaciones` 7.
- desarrollo, diez más frecuentes en L0: `Presentación informativa` 25, `compra de moneda extranjera` 25, `acceso al mercado de cambios` 15, `calculo` 14, `emisión de certificaciones` 14, `financiación` 13, `emisión de certificación` 11, `pago` 11, `pago de importación` 11, `pago de capital e intereses` 10.
- cinco, diez más frecuentes en L0: `depósito` 10, `financiación` 10, `endoso` 9, `Financiación` 7, `emisión de cheques` 7, `presentación informativa` 7, `débito` 6, `emisión de cheque` 6, `transferencia` 6, `débito de cuenta corriente` 5.
- diez, diez más frecuentes en L0: `Presentación informativa` 26, `compra de moneda extranjera` 26, `financiación` 23, `acceso al mercado de cambios` 15, `presentacion_informativa` 15, `calculo` 14, `emisión de certificaciones` 14, `depósito` 13, `pago` 12, `Financiación` 11.

### Padre sugerido de sujeto_propuesto

Clave `padre_sugerido_validador` (crudo L0: padre fuera del bloque v3 en relaciones aplica_a/ejecuta) y `grupos.<g>.capas.crudo.forma_sujeto`:

- r1: con padre en catálogo 54, con padre fuera 1, sin padre 0, padre sin propuesto 0; estado de los padres fuera: paso 1.
- desarrollo: con padre en catálogo 44, con padre fuera 0, sin padre 0, padre sin propuesto 1; estado de los padres fuera: —.
- cinco: con padre en catálogo 19, con padre fuera 0, sin padre 0, padre sin propuesto 0; estado de los padres fuera: —.
- diez: con padre en catálogo 63, con padre fuera 0, sin padre 0, padre sin propuesto 1; estado de los padres fuera: —.

## 4. Motivos de rechazo del validador, por lista

Clave `grupos.<g>.motivos_rechazo` (validacion.rechazos del primer intento, L1). La lista a la que se asigna cada motivo es la del mapeo `MOTIVO_A_LISTA` del script; «sin lista» = motivo ajeno a las listas cerradas.

| nivel | motivo | lista | r1 | desarrollo | cinco | diez |
|---|---|---|---|---|---|---|
| chunk | entities_o_relations_invalidos | sin lista | 1 | 3 | 1 | 4 |
| entidad | punto_fuera_de_admitidos | sin lista | 1 | 0 | 0 | 0 |
| entidad | type_invalido | tipo_entidad | 0 | 2 | 2 | 4 |
| relacion | extremo_chunk_ausente | sin lista | 2 | 0 | 3 | 3 |
| relacion | firma_invalida | tipo_entidad×predicado (matriz) | 304 | 870 | 112 | 982 |
| relacion | padre_sugerido_sin_propuesto | padre_sugerido | 0 | 1 | 0 | 1 |
| relacion | predicado_invalido | predicado | 2 | 1 | 1 | 2 |
| relacion | ref_colgante | sin lista | 10 | 20 | 1 | 21 |
| relacion | sujeto_en_predicado_no_sujeto | sujeto_id | 0 | 4 | 2 | 6 |
| relacion | sujeto_extremo_invalido | sujeto_id | 0 | 3 | 0 | 3 |

Elementos del crudo sin correspondencia con el validado (clave `grupos.<g>.efecto_validador.sin_correspondencia`): r1 0; desarrollo 0; cinco 0; diez 0.

r1 contra las listas de su perfil (v2: 6 tipos, 12 predicados, 70 ids, Obligacion.tipo de 5, Operacion {tipo}), clave `grupos.r1.efecto_validador_perfil_v2`: tipo_entidad: —; predicado: rechazado:predicado_invalido 2; sujeto_id: —; padre_sugerido: —; Obligacion.tipo: paso 2; Restriccion.tipo: —; Comunicacion.tipo: paso 14; claves: paso 14; sin_correspondencia: —.

## 5. Sujetos

### 5.1 Forma de las relaciones aplica_a y ejecuta

Clave `grupos.<g>.capas.<capa>.forma_sujeto` (L0, L1, L2) y `grafos.<g>.aristas_sujeto_no_esqueleto` (L3).

| grupo | capa | solo sujeto_id | solo sujeto_propuesto | ambos | ninguno |
|---|---|---|---|---|---|
| r1 | crudo | 3449 | 55 | 0 | 0 |
| r1 | validado_e1 | 3248 | 54 | 0 | 0 |
| r1 | reintentos_crudo | 1168 | 24 | 4 | 0 |
| r1 | entrada_e2 | 3364 | 67 | 0 | 0 |
| r1 | grafo L3 | 3279 (a id de catálogo) | 62 (a propuesto en cuarentena) | — | — |
| desarrollo | crudo | 3009 | 43 | 1 | 2 |
| desarrollo | validado_e1 | 2940 | 43 | 0 | 0 |
| desarrollo | reintentos_crudo | 477 | 3 | 0 | 0 |
| desarrollo | entrada_e2 | 3064 | 42 | 0 | 0 |
| desarrollo | grafo L3 | 2987 (a id de catálogo) | 32 (a propuesto en cuarentena) | — | — |
| cinco | crudo | 1025 | 19 | 0 | 0 |
| cinco | validado_e1 | 1003 | 16 | 0 | 0 |
| cinco | reintentos_crudo | 84 | 3 | 0 | 0 |
| cinco | entrada_e2 | 1020 | 19 | 0 | 0 |
| cinco | grafo L3 | 1007 (a id de catálogo) | 18 (a propuesto en cuarentena) | — | — |
| diez | crudo | 4034 | 62 | 1 | 2 |
| diez | validado_e1 | 3943 | 59 | 0 | 0 |
| diez | reintentos_crudo | 561 | 6 | 0 | 0 |
| diez | entrada_e2 | 4084 | 61 | 0 | 0 |
| diez | grafo L3 | 3994 (a id de catálogo) | 50 (a propuesto en cuarentena) | — | — |

Mención textual guardada en aristas aplica_a/ejecuta del grafo (sin esqueleto): r1 0 de 3341, desarrollo 0 de 3019, cinco 0 de 1025, diez 0 de 4044 ([c12]; el campo no existe).

### 5.2 Propuestos en el ensamblado (E4 y esqueleto)

Clave `propuestos_e4` (`e4_propuestos.json` y `e5_esqueleto.json` de cada ensamblado).

| grupo | propuestos | resueltos | cuarentena | con padre | sin padre | padre fuera del bloque v3 | padre fuera del JSON (esqueleto) | aristas padre_sugerido |
|---|---|---|---|---|---|---|---|---|
| r1 | 44 | 3 | 41 | 44 | 0 | 1 | 0 | 41 |
| desarrollo | 22 | 3 | 19 | 22 | 0 | 0 | `Sujeto_propuesto_originante`→`Sujeto_entidad_originante_de_transferencia` | 18 |
| cinco | 12 | 1 | 11 | 12 | 0 | 0 | 0 | 11 |
| diez | 34 | 4 | 30 | 34 | 0 | 0 | `Sujeto_propuesto_originante`→`Sujeto_entidad_originante_de_transferencia` | 29 |

### 5.3 Posibles forzados (R-FORZ)

Clave `sujetos_forzados.<g>`. Unidad: par (chunk, sujeto_id) del crudo L0. Indicador, no veredicto.

| grupo | relaciones con sujeto_id | pares | categoría | pares de la categoría | posibles forzados (amplia) | posibles forzados (estricta) |
|---|---|---|---|---|---|---|
| r1 | 3449 | 1666 | otra_clase_o_instancia | 345 | 49 | 132 |
| r1 | 3449 | 1666 | defecto_del_to | 1321 | 1247 | 1321 |
| r1 | 3449 | 1666 | rol_no_defecto | 0 | 0 | 0 |
| r1 | 3449 | 1666 | sin_entrada_en_bloque_v3 | 0 | 0 | 0 |
| desarrollo | 3010 | 1541 | otra_clase_o_instancia | 314 | 43 | 129 |
| desarrollo | 3010 | 1541 | defecto_del_to | 1227 | 1155 | 1227 |
| desarrollo | 3010 | 1541 | rol_no_defecto | 0 | 0 | 0 |
| desarrollo | 3010 | 1541 | sin_entrada_en_bloque_v3 | 0 | 0 | 0 |
| cinco | 1025 | 595 | otra_clase_o_instancia | 84 | 18 | 39 |
| cinco | 1025 | 595 | defecto_del_to | 510 | 315 | 447 |
| cinco | 1025 | 595 | rol_no_defecto | 1 | 1 | 1 |
| cinco | 1025 | 595 | sin_entrada_en_bloque_v3 | 0 | 0 | 0 |
| diez | 4035 | 2136 | otra_clase_o_instancia | 398 | 61 | 168 |
| diez | 4035 | 2136 | defecto_del_to | 1737 | 1470 | 1674 |
| diez | 4035 | 2136 | rol_no_defecto | 1 | 1 | 1 |
| diez | 4035 | 2136 | sin_entrada_en_bloque_v3 | 0 | 0 | 0 |

Ids de clase o instancia (no defecto del TO) con más posibles forzados (amplia), «id posibles/pares»:

- r1: `Sujeto_entidad_cambiaria` 9/12, `Sujeto_empresa_no_financiera_emisora_de_tarjetas` 8/14, `Sujeto_beneficiario_economia_conocimiento` 4/5, `Sujeto_entidad_financiera` 4/96, `Sujeto_aseguradora` 3/3, `Sujeto_casa_de_cambio` 3/5, `Sujeto_persona_humana` 3/14, `Sujeto_banco_comercial` 2/4, `Sujeto_emisor_de_titulos_de_deuda` 2/2, `Sujeto_fiduciario_de_fideicomiso_financiero` 2/4, `Sujeto_persona_juridica` 2/6, `Sujeto_bcra` 1/12, `Sujeto_deudor` 1/3, `Sujeto_estructura` 1/1, `Sujeto_exportador` 1/29.
- desarrollo: `Sujeto_entidad_cambiaria` 10/13, `Sujeto_empresa_no_financiera_emisora_de_tarjetas` 8/14, `Sujeto_aseguradora` 3/3, `Sujeto_banco` 2/4, `Sujeto_beneficiario_economia_conocimiento` 2/3, `Sujeto_casa_de_cambio` 2/4, `Sujeto_entidad_originante_de_transferencia` 2/4, `Sujeto_persona_humana` 2/14, `Sujeto_persona_juridica` 2/3, `Sujeto_banco_comercial` 1/3, `Sujeto_banco_multilateral_de_desarrollo` 1/3, `Sujeto_entidad_financiera` 1/69, `Sujeto_entidad_receptora` 1/3, `Sujeto_fiduciario_de_fideicomiso_financiero` 1/3, `Sujeto_fmi` 1/2.
- cinco: `Sujeto_cliente` 3/8, `Sujeto_entidad_depositaria` 3/9, `Sujeto_usuario_de_servicios_financieros` 3/4, `Sujeto_entidad_girada` 2/17, `Sujeto_banco` 1/1, `Sujeto_entidad_cambiaria` 1/1, `Sujeto_entidad_financiera` 1/11, `Sujeto_fiduciario_de_fideicomiso_financiero` 1/2, `Sujeto_persona_humana` 1/4, `Sujeto_persona_juridica` 1/1, `Sujeto_sujeto_regulado` 1/1.
- diez: `Sujeto_entidad_cambiaria` 11/14, `Sujeto_empresa_no_financiera_emisora_de_tarjetas` 8/16, `Sujeto_aseguradora` 3/3, `Sujeto_banco` 3/5, `Sujeto_cliente` 3/34, `Sujeto_entidad_depositaria` 3/9, `Sujeto_persona_humana` 3/18, `Sujeto_persona_juridica` 3/4, `Sujeto_usuario_de_servicios_financieros` 3/7, `Sujeto_beneficiario_economia_conocimiento` 2/3, `Sujeto_casa_de_cambio` 2/4, `Sujeto_entidad_financiera` 2/80, `Sujeto_entidad_girada` 2/17, `Sujeto_entidad_originante_de_transferencia` 2/4, `Sujeto_fiduciario_de_fideicomiso_financiero` 2/5.

Muestra sellada: `muestra_forzados_30.csv`, 30 pares sorteados con semilla 20260930 sobre una población de 61 (R-MUESTRA; clave `muestra_forzados`). Columnas de lectura vacías; quién lee lo decide la autora (checklist P15 y Q12).

### 5.4 sujeto_propuesto literal en el texto del chunk (R-LIT)

Clave `sujeto_propuesto_literal`. Unidad: relación aplica_a/ejecuta con sujeto_propuesto.

La última columna es una descripción posterior, no una regla de presencia: de los ausentes, cuántos tienen cada token normalizado en el texto del chunk, en cualquier orden y no contiguos.

| capa | grupo | total | presente | ausente | ausente con todos los tokens |
|---|---|---|---|---|---|
| crudo | r1 | 55 | 45 | 10 | 7 |
| crudo | desarrollo | 44 | 33 | 11 | 4 |
| crudo | cinco | 19 | 12 | 7 | 4 |
| crudo | diez | 63 | 45 | 18 | 8 |
| entrada_e2 | r1 | 67 | 50 | 17 | 12 |
| entrada_e2 | desarrollo | 42 | 32 | 10 | 3 |
| entrada_e2 | cinco | 19 | 14 | 5 | 2 |
| entrada_e2 | diez | 61 | 46 | 15 | 5 |

Por TO (crudo L0 / entrada E2, «presente/total»):

- r1: cap 26/30 · 28/35; cla 0/0 · 0/0; ext 17/22 · 18/27; pro 0/0 · 1/1; ric 2/3 · 3/4.
- t0: cap 7/7 · 9/9; cla 1/2 · 0/1; ctacte 3/8 · 6/9; docvig 1/3 · 1/3; ext 22/32 · 20/29; lingob 7/7 · 7/7; pagjub 0/0 · 0/0; polcre 1/1 · 0/0; pro 0/0 · 0/0; ric 3/3 · 3/3.

## 6. Re-resolución por programa, contrafáctica (R-CAT)

Clave `reresolucion_contrafactica`. `r1_e4.resolver_label` por import sobre cada fila de `e4_propuestos.json`. Catálogo (i): `esquema_v3_clases.json`; (ii): (i) más 6 ids del bloque (`Sujeto_banco_central_del_exterior`, `Sujeto_entidad_depositaria`, `Sujeto_entidad_girada`, `Sujeto_entidad_originante_de_transferencia`, `Sujeto_entidad_receptora`, `Sujeto_fmi`), sin alias. Control: (i) reproduce la tabla guardada fila a fila. Es un contrafáctico, no un resultado.

| ensamblado | propuestos | guardado: resueltos / cuarentena | resuelven con (i) | resuelven con (ii) |
|---|---|---|---|---|
| desarrollo | 22 | 3 / 19 | 3 | 3 |
| cinco | 12 | 1 / 11 | 1 | 1 |
| diez | 34 | 4 / 30 | 4 | 4 |

- desarrollo: «cliente» (padre `Sujeto_contraparte`): (i) `Sujeto_cliente` resuelto_por_id_slug+label_singularizado; (ii) `Sujeto_cliente` resuelto_por_id_slug+label_singularizado; «exportador» (padre `Sujeto_exportador`): (i) `Sujeto_exportador` resuelto_por_id_slug+label_singularizado; (ii) `Sujeto_exportador` resuelto_por_id_slug+label_singularizado; «exportadores» (padre `Sujeto_exportador`): (i) `Sujeto_exportador` resuelto_por_label_exacto+label_singularizado; (ii) `Sujeto_exportador` resuelto_por_label_exacto+label_singularizado.
- cinco: «Persona jurídica» (padre `Sujeto_persona_juridica`): (i) `Sujeto_persona_juridica` resuelto_por_id_slug+label_singularizado; (ii) `Sujeto_persona_juridica` resuelto_por_id_slug+label_singularizado.
- diez: «cliente» (padre `Sujeto_contraparte`): (i) `Sujeto_cliente` resuelto_por_id_slug+label_singularizado; (ii) `Sujeto_cliente` resuelto_por_id_slug+label_singularizado; «exportador» (padre `Sujeto_exportador`): (i) `Sujeto_exportador` resuelto_por_id_slug+label_singularizado; (ii) `Sujeto_exportador` resuelto_por_id_slug+label_singularizado; «exportadores» (padre `Sujeto_exportador`): (i) `Sujeto_exportador` resuelto_por_label_exacto+label_singularizado; (ii) `Sujeto_exportador` resuelto_por_label_exacto+label_singularizado; «Persona jurídica» (padre `Sujeto_persona_juridica`): (i) `Sujeto_persona_juridica` resuelto_por_id_slug+label_singularizado; (ii) `Sujeto_persona_juridica` resuelto_por_id_slug+label_singularizado.

## 7. Omisiones (R-OMIS)

Clave `omisiones.<g>`. Marca de E0: tabla = `flags.contenido_tabular`, fórmula = `flags.formula`. «Marcadas sin omisión» se abre en: con extracción (alguna entidad distinta de TextoOrdenado en esa capa) y sin extracción (rechazo de chunk, unidad en cola humana o salida vacía).

| grupo | unidades | por marca (E0) | capa | con omisiones: total | por marca | marcadas sin omisión: con extracción / sin extracción |
|---|---|---|---|---|---|---|
| r1 | 1763 | formula 34, sin_marca 1698, tabla 17, tabla_y_formula 14 | crudo | 74 | formula 34, sin_marca 10, tabla 17, tabla_y_formula 13 | 1 / 0 |
| r1 | 1763 | formula 34, sin_marca 1698, tabla 17, tabla_y_formula 14 | validado_e1 | 74 | formula 34, sin_marca 10, tabla 17, tabla_y_formula 13 | 0 / 1 |
| r1 | 1763 | formula 34, sin_marca 1698, tabla 17, tabla_y_formula 14 | finales_c15 | 81 | formula 33, sin_marca 20, tabla 16, tabla_y_formula 12 | 0 / 4 |
| desarrollo | 1763 | formula 34, sin_marca 1698, tabla 17, tabla_y_formula 14 | crudo | 75 | formula 33, sin_marca 12, tabla 17, tabla_y_formula 13 | 1 / 1 |
| desarrollo | 1763 | formula 34, sin_marca 1698, tabla 17, tabla_y_formula 14 | validado_e1 | 75 | formula 33, sin_marca 12, tabla 17, tabla_y_formula 13 | 0 / 2 |
| desarrollo | 1763 | formula 34, sin_marca 1698, tabla 17, tabla_y_formula 14 | finales_c15 | 78 | formula 30, sin_marca 21, tabla 17, tabla_y_formula 10 | 0 / 8 |
| cinco | 671 | formula 5, sin_marca 666 | crudo | 5 | formula 5 | 0 / 0 |
| cinco | 671 | formula 5, sin_marca 666 | validado_e1 | 5 | formula 5 | 0 / 0 |
| cinco | 671 | formula 5, sin_marca 666 | finales_c15 | 7 | formula 5, sin_marca 2 | 0 / 0 |
| diez | 2434 | formula 39, sin_marca 2364, tabla 17, tabla_y_formula 14 | crudo | 80 | formula 38, sin_marca 12, tabla 17, tabla_y_formula 13 | 1 / 1 |
| diez | 2434 | formula 39, sin_marca 2364, tabla 17, tabla_y_formula 14 | validado_e1 | 80 | formula 38, sin_marca 12, tabla 17, tabla_y_formula 13 | 0 / 2 |
| diez | 2434 | formula 39, sin_marca 2364, tabla 17, tabla_y_formula 14 | finales_c15 | 85 | formula 35, sin_marca 23, tabla 17, tabla_y_formula 10 | 0 / 8 |

omisiones_no_prosa emitido como string en el crudo (el validador solo toma listas, `validador_e1.py:154-156`): r1 como_string_vacio 3; desarrollo como_string_vacio 2; cinco como_string_vacio 2; diez como_string_vacio 4. Advertencias `flag_*` del validador en finales: r1 0; desarrollo 0; cinco 0; diez 0.

Conciliación con [c15] (clave `conciliacion_c15`): el comando [c15] lee `corpus_tanda0/salida/`; los ensamblados leen `salida_dirigida/`, que solo difiere en cap. Unidades de cap con omisiones: salida/ 36, salida_dirigida/ 37; difieren: `cap::4.2.1.2`.

## 8. Catálogo: bloque v3 contra esquema_v3_clases.json

Clave `catalogo_diff`. Bloque parseado de `prompt_v3_b54.BLOQUE_CATALOGO_V3` (102 ids; label y nivel verificados contra `perfil_e1.perfil('v3_b54').labels_catalogo`); JSON: 101 ids.

- Solo en el bloque (6): `Sujeto_banco_central_del_exterior`, `Sujeto_entidad_depositaria`, `Sujeto_entidad_girada`, `Sujeto_entidad_originante_de_transferencia`, `Sujeto_entidad_receptora`, `Sujeto_fmi`.
- Solo en el JSON (5): `Sujeto_acreedor_del_exterior`, `Sujeto_autoridad_nacional_de_aplicacion`, `Sujeto_secretaria_de_comercio`, `Sujeto_secretaria_de_energia`, `Sujeto_secretaria_de_transporte`.
- Comunes: 96. Label distinto: 0. Alias distinto: 0. Nivel distinto: 0. TO de rol distinto: 0.
- Padre: el bloque no serializa padres (0); `ADICIONES_V3` (`prompt_v3_b54.py:150`) declara padre para 7 ids. De ellos, en el JSON: `Sujeto_camara_electronica_de_compensacion` módulo `Sujeto_sujeto_regulado` / JSON `Sujeto_sujeto_regulado`; fuera del JSON: `Sujeto_banco_central_del_exterior` (padre `Sujeto_organismo_publico`), `Sujeto_entidad_depositaria` (padre `Sujeto_sujeto_regulado`), `Sujeto_entidad_girada` (padre `Sujeto_sujeto_regulado`), `Sujeto_entidad_originante_de_transferencia` (padre `Sujeto_sujeto_regulado`), `Sujeto_entidad_receptora` (padre `Sujeto_sujeto_regulado`), `Sujeto_fmi` (padre `Sujeto_organismo_internacional`). Padre en el JSON de los ids solo-JSON: `Sujeto_acreedor_del_exterior`→`Sujeto_contraparte`, `Sujeto_autoridad_nacional_de_aplicacion`→`Sujeto_organismo_publico`, `Sujeto_secretaria_de_comercio`→`None`, `Sujeto_secretaria_de_energia`→`None`, `Sujeto_secretaria_de_transporte`→`None`.

