# U-R2-CODIGO — FRENO de cierre, complemento final después de R5

Contexto: R5 commiteada en `92b45d6`. El complemento final cubre los puntos 1 a 4 y la regeneración de las salidas
de remisiones. USD 0, sin API ni Neo4j y sin commit.

La batería es `control_final.sh` y su post-proceso `post_final.py` (los dos en el paquete de revisión). Corrió de
22:11 a 22:44 del 02/10/2026 sobre dos copias armadas con `rsync --copy-links`, con 0 enlaces en cada una:
- la copia final;
- la copia de HEAD `92b45d6`, con los archivos modificados restaurados por `git show HEAD:`.

Regla l. La batería toma el sha256 de todos los archivos del repo, salvo `.git`, antes y después:
- Entre el inicio y el fin cambiaron 6 archivos ajenos a la unidad: `docs/tesis/.DS_Store` y
  `docs/tesis/figuras/{figura_ficha.pdf,figura_ficha.png,figura_ficha.svg,LEEME_figura_ficha.md,generar_figura_ficha.py}`.
  Los modificó otra sesión entre las 22:36:42 y las 22:39:09 (`ls -laT`).
- Ningún archivo de esta unidad cambió. La batería escribe solo en el scratchpad.
- No hay `.pyc` nuevos: 286 entradas antes y después.
- En un control anterior cambió además `data/experiment/neo4j/volumen/logs/debug.log`. Es el log del contenedor
  `neo4j-bcra-kg-compose` (`docker ps`) y git lo ignora (`data/experiment/neo4j/.gitignore:4`).

Rutas absolutas. Los reportes que registran la ruta absoluta de la copia se comparan con esa ruta reemplazada por la
del repo.

## 1 — K-a′ y K-b en e0-r2

Dónde está: `e0_lib.separar_encabezado_pie`, con la constante `RE_TITULO_SECCION_NUMERADO_K`. Las dos ramas actúan
solo con `mayusculas_repetidas`, es decir, solo en e0-r2. K-b no actúa en el modo sin raíz, que decide por
`labels_preservables`.

Selftests (`selftest_e0r2.py`):
- S13: páginas reales de `ri_rml`, `nmaeef`, `snp_cheq`, `snp_dd` y `ri_rcl`, más tres casos sintéticos. Comprueba
  qué quita la zona de encabezado y que el descarte histórico no cambia.
- S14: chunks de la escalera en los cuatro TOs.
- Resultado: 48/48 con el código final. Con el `e0_lib.py` de HEAD, 38/48: los 10 casos nuevos fallan.

Control sobre los 152 TOs de la partición (escalera final contra escalera de HEAD, en la misma batería):

| TO | Chunks (HEAD → final) | Qué recupera |
|---|---|---|
| `nmaeef` | 39 → 39 | `S11::chapeau_seccion` recupera los dos renglones de la norma |
| `ri_rml` | 26 → 27 | aparece `ri_rml::1.11`; «CUENTAS EN PESOS» deja `1.10.4` |
| `snp_cheq` | 618 → 528 | desaparecen 97 intersticiales; vuelven los 7 puntos 3.1.2.3 a 3.1.4.2 |
| `snp_dd` | 55 → 53 | desaparecen `S6::chapeau_seccion` y `S6::cierre`; `6.2.6` recupera «Este código se asigna…» |

Resultados del control:
- Ningún TO queda en 0 chunks.
- Los otros 148 TOs no cambian.
- La salida final es byte a byte la de la propuesta K-a′ + K-b medida en R5 (`esck_*`), y la de HEAD es la de R5.
- La tanda 0 en e0-r2 sale igual con el código final y con el de HEAD.

Comparación con la partición (`r5_escalera_particion.py --comparar --atribuir`, doble corrida idéntica):
- 129 TOs con los mismos ids (R5: 128).
- Diferencias de ids por clase:

  | Clase | Final | R5 |
  |---|---|---|
  | L | 69 | 69 |
  | Tabla | 8 | 7 |
  | K | 93, en 16 TOs | 205, en 19 TOs |

  Salen de K `ri_rml`, `snp_cheq` y `snp_dd`. La tabla nueva es `snp_dd::6.2.6`: ahora contiene una tabla, y e0-r2
  no la parte (R4.b).
- Chunks con texto distinto por clase:

  | Clase | Final | R5 |
  |---|---|---|
  | Tablas | 146 | 145 |
  | K | 64 | 72 |
  | Arrastre de K | 1 | 32 |
  | Pies | 45 | 45 |
  | Pies y K | 5 | 5 |

  Ninguna diferencia queda sin causa.

## 2 — BKL-0006 y BKL-0023 por punto y monto

Dónde está, en `scripts/regression_kg.py`:
- `tabla_1_2_r2`: Restricciones ancladas en cap 1.2 con un monto de la tabla del 1.2 (`MONTO_DE_VALOR`) en el valor
  normalizado de su lista de umbrales, sin la frase «exigencia básica»;
- `clase_1_2` y `montos_de_lista`.

En BKL-0023, el nodo objetivo es la Restriccion de las compañías financieras, si existe. Si no existe, es la de
bancos. Razón: en la extracción r2 la oración es una Obligacion sin monto que remite a «las exigencias establecidas
para los bancos».

El perfil existente no cambia. `selftest_regression_kg.py` tiene 7 casos nuevos: 147/147.

En las pruebas r2 de desarrollo y de diez, los dos ítems pasan de no_aplicable a «persiste»:
- BKL-0006: tabla invertida (bancos 2.500, restantes 5.000);
- BKL-0023: la Restriccion de bancos lleva 2500000000 ARS.

En cla, los dos quedan no_aplicable (no hay cap).

## 3 — «de este/del presente ordenamiento» y «de este/del presente texto ordenado»

Dónde está, en `r1_referencias.py`:
- las cuatro formas pasan a `RE_PROPIO_TO`;
- `RE_ANAFORA_NORMA` ya no incluye «este»; «de dicho/ese ordenamiento» siguen siendo anáfora;
- `RE_NORMA_R2` no toma «del presente texto ordenado de» ni «de este texto ordenado de» como norma nombrada.

`selftest_r3.py`: T7e (C) ajustado y tres casos nuevos, uno de ellos `ri_niif::2.1`. Resultado 96/96.

Medición (`r5_comparar_g.py --tabla` con HEAD y con el código final, comparada con `medir_propio_to.py`):
- Tanda 0: 0 menciones cambian (desarrollo 1.246, diez 1.454).
- Partición: 4.139 → 4.137 menciones, en tres chunks.
  - `dmrd::S6::parte5` («dentro del marco de este Texto Ordenado») y `repefe::S9::chapeau_seccion` («a las
    disposiciones de este ordenamiento») eran anáforas irresolubles sin antecedente y dejan de contarse. No hay un
    punto antes, así que tampoco queda una mención interna.
  - `ri_niif::2.1`: la mención externa irresoluble («del presente texto ordenado de: - Estado de Situación
    Financiera») pasa a ser la Sección 4 interna.

## 4 — fixture

E4-a8 de KG-Reextraido queda re-sellado a no_aplicable, con una nota fechada:
- El «persiste» anterior leía `corpus_v2/salida_r1/e4_propuestos.json` (`E4_PROPUESTOS_R1`, en `26d274d`
  `scripts/regression_kg.py:83` y `:1241`) sobre otro grafo.
- `corpus_v2/salida/` no tiene `e4_propuestos.json`.
- El `detalle_observado` es el que la suite mide en la batería (comparado: igual).

| sha256 | Antes | Después |
|---|---|---|
| subárbol `estado_esperado` (canónico) | `69b46385…` | `73031656cc24a389b75931e2621c1fc8127ad91deb2282cea97d7eb2e84adedf` |
| archivo de la fixture | — | `2c9e9b5e8f26…` |

Fuera de E4-a8, `estado_esperado` es idéntico, comparado objeto a objeto (`resellar_e4a8.py`).
`linea_de_base_observada` no cambia. `resumen_observado` conserva los conteos de la corrida del 2026-09-27.

La entrada propuesta r2 (sin sellar, fuera de `estado_esperado`) se actualizó con la corrida final:
- el kg no cambia (`93a7af72…`);
- cambian solo BKL-0006 y BKL-0023, de no_aplicable a persiste.

## Salidas de remisiones regeneradas

`data/experiment/r2_codigo/r3d_remisiones.json` y `r3_perdidas_remisiones.json` (eran las de R4, `26d274d`) son
ahora las de la batería final, con doble corrida idéntica. Son byte a byte iguales con el código final y con el de
HEAD: el punto 3 no toca la tanda 0. Las cifras de los asientos coinciden con lo que escriben:

| Cifra | Valor | Dónde |
|---|---|---|
| Aristas en desarrollo | 12.547 | `B_pasos_desarrollo.resumen_regla_firmada.aristas` |
| Citas en desarrollo | 1.297 | `B_pasos_desarrollo.resumen_regla_firmada.citas_resueltas` |
| Remisiones selladas perdidas | 109 | `A_remisiones_selladas_que_se_pierden.desarrollo.pares_perdidos` |
| Pares perdidos contra la paráfrasis | 141 | `B_parafrasis_siete_tipos_desarrollo.pares_perdidos` |

Otros JSON de `r2_codigo/` que difieren de la salida de la batería final y no regeneré (no estaba pedido):
- `reglas_remisiones_censos.json`, `r4_pies_e0.json` y `r3h_lectura_umbrales.json` (de `26d274d`);
- `r1d_censo_requests.json` (de `91fe4b9`).

`r4_detector_casi_duplicados.json` y `r4_claves_cache.json` coinciden con la salida final.

## Sin regresiones

Suite sobre los siete grafos sellados (los cuatro de la fixture y los tres ensamblados de la tanda 0):
- Los estados son iguales con el código final y con el de HEAD.
- Con la fixture final hay 0 regresiones en los cuatro grafos con entrada; con la de HEAD, 1 (E4-a8 de
  KG-Reextraido).
- Un control posterior a la escritura, sobre una copia nueva, da otra vez 0 en los cuatro. La entrada r2 no se lee:
  «no se computa regresión».

Shapes:
- v0 sobre run_3 y el perfil congelado sobre r1 y los tres ensamblados dan lo mismo que HEAD, con la ruta
  normalizada.
- Perfil r2: sin cambios respecto de R5. Desarrollo y diez dan NO PASA solo por S18; cla da PASA.

Reproducciones:
- Los tres ensamblados sellados se reproducen: 10 de 13 archivos byte a byte y los 3 reportes iguales con la ruta
  normalizada.
- E0 legada: 34/34.
- La muestra de la observación 12 sobre r1 es byte a byte la de HEAD.
- Pies (G), R1.d (F) y T7 de `r1_tests` (E) son iguales a los de R5.
- Las claves de caché son iguales con el código final y con el de HEAD.

Dobles corridas idénticas: prueba r2 de desarrollo (21 archivos), suite y shapes r2, r3d, pérdidas, censos, R1.d,
pies, casi duplicados, claves y comparación con la partición.

Remisiones `remite_a` de las pruebas r2, sin cambio respecto de R5. Las citas tienen dos definiciones:
- citas resueltas (`reporte_ensamblado_r2.json`, `remite_a.citas_resueltas`);
- citas del censo de la suite: chunk, evidencia y destino de las aristas, `censos.remisiones.citas`.

| Prueba | Aristas (interna / externa / to_entero) | Citas resueltas | Citas del censo |
|---|---|---|---|
| Desarrollo | 12.833 (12.049 / 775 / 9) | 1.382 | 1.164 |
| Diez | 14.000 (13.021 / 949 / 30) | 1.547 | 1.323 |
| cla | 179 (177 / 0 / 2) | 31 | 30 |

Selftests:
- obs12 26/26, e0 57/57, b52 39/39, b581 34/34, b582 59/59, b583 33/33, ub53 40/40, cablev3 45/45, corpus 21/21,
  e2 35/35, dirigida 28/28, pyd_r2 296/296, r3 96/96, r2 18/18, e0r2 48/48, clave_cache OK, regression_kg 147/147,
  shapes 79/79, r4 26/26;
- `selftest_manifiesto` 32/37, con los mismos 5 fallos P5 que en R4 y en R5 (comparado con el log de R5).

## Errores propios, con su causa

En el FRENO R5 di las citas `remite_a` del reporte del ensamblado (1.382 en desarrollo) sin decir que el censo de la
suite cuenta otra unidad (1.164). Las dos cifras son correctas para su definición, pero la ambigüedad era mía. Acá
quedan las dos con su fuente.

## Pendiente de la autora

- Commit: PENDIENTE.
- Decisiones que siguen abiertas de R5: la marca de S18 y los tres pedidos de L-ESQ-R2 fuera de la lista del
  mandato (§1.5, §6.5 y §7.5).
- Si se regeneran los cuatro JSON de `r2_codigo/` que difieren de la salida final.
