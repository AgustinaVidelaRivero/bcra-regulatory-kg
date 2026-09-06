# Diseño de U-CABLE-V3 — cableado del prefijo v3 a producción

**ESTADO: APROBADO (06/09/2026)** — freno 1 aprobado con revisiones de la
instancia del plan y de mesa coincidentes, con estas TRES RESOLUCIONES de la
autora, vinculantes para la fase 2:

1. **Hallazgo 1 ratificado**: validador y E2 usan el VOCABULARIO CONGELADO
   COMPLETO en modo v3 (importado del módulo sellado `prompt_congelado`),
   según §2.2/§2.6. Criterio de verificación agregado: la aceptación se
   demuestra POR EXTENSIÓN — el selftest verifica los 102 ids del catálogo,
   los 9 tipos uno por uno y los 13 predicados uno por uno (instancia mínima
   de firma válida cada uno), con conteos recomputados; los rechazos
   planeados quedan igual.
2. **Alcance nuevo aprobado — endurecimiento de `properties.tipo`** (herencia
   del laudo de congelado): en modo v3 (esquema inyectado), un valor de
   `Obligacion.properties.tipo` fuera del enum de 6 del congelado se
   NORMALIZA a `"otra"` con contador visible en el resultado del validador y
   en el reporte de corrida, más contador SEPARADO para el valor retirado
   `requisito_de_estructura`. REGISTRO, NO RECHAZO. Instrumenta la
   vigilancia (5) del laudo 2593d4d para la tanda 1. La fuente de verdad del
   enum es `prompt_congelado.OBLIGACION_TIPO_CONGELADO` (verificado igual a
   los 6 valores de la resolución antes de implementar). El camino default
   queda byte-idéntico.
3. **Este documento viaja al repo** con el commit de fase 2, con este
   encabezado; el contenido aprobado de abajo no se reescribe.

---

# U-CABLE-V3 — FASE 1 (diseño): mapa de consumidores, candados y plan

Estado: FRENO 1 — pendiente de aprobación. USD 0. Ningún archivo del repo
editado (verificable: `git status --porcelain` idéntico al de apertura).

`git status --porcelain` al abrir la fase (2026-09-06):

```
 M docs/tesis/bibliografia.bib
 M docs/tesis/main.tex
?? adjudicar.py
```

Ninguna de las rutas de esta unidad está tocada (docs/tesis es de otra unidad
y me está prohibido; adjudicar.py es el residuo conocido de la entrada 14 de
la cola de higiene). Sin colisión: se procede.

---

## 0. Hechos verificados del contrato v3 (recomputados por import, USD 0)

Comando reproducible:
`.venv/bin/python3 -c "import sys; sys.path.insert(0,'data/experiment/b54_catalogo_v3/code'); import prompt_v3_b54 as v3; ..."`

| Hecho | Valor recomputado | Coincide con el sello |
|---|---|---|
| sha256 del texto v3 | `35e88c2dd0a2920302c29005b08ab9689405606d4bd5fcf8fb7ce807b1a3c512` | sí |
| hash canónico system+tools | `54a111e2175f` | sí |
| hash de producción dev (prompt_e1) | `4793d6152608` | sí (P6 de selftest_ub53) |
| hash del congelado | `1be8304e3d77` | sí |
| enum `type` del tool schema v3 | 9 tipos (los 6 viejos + Potestad, Condicion, Definicion) | sí (congelado) |
| enum `predicate` | 13 (los 12 viejos + `condicion_de`) | sí (congelado) |
| enum `sujeto_id` / padre sugerido | 102 ids | sí (102 = 70 − 5 + 7 + 30, recomputado) |
| `SUJETO_PREDICATES` congelado | `("aplica_a", "ejecuta")` — igual al viejo | sí |
| `ROL_POR_TO_V3` | 71 entradas = 5 dev + 30 roles + 36 mapeos a clase (5+30+36=71) | sí |
| Campos/required del tool schema v3 | idénticos al viejo (entities: local_id/type/label/punto/properties, req 4; relations: predicate/punto req; omisiones_no_prosa presente) | sí |

Consecuencia estructural que el mandato no explicita pero el contrato impone
(HALLAZGO 1, ver §4): el prefijo v3 es el CONGELADO (9 tipos / 13 predicados)
con catálogo v3 — el cableado coherente exige que el validador y el ensamblado
E2 validen contra el VOCABULARIO CONGELADO COMPLETO en modo v3, no solo contra
el catálogo de sujetos. Un validador que siga con los 6/12 viejos rechazaría
toda Potestad/Condicion/Definicion y todo `condicion_de` que el extractor v3
emite legítimamente bajo su tool schema.

## 1. Arquitectura elegida: PERFIL DE EXTRACCIÓN seleccionado por manifiesto

Tres restricciones duras cierran el espacio de diseño:

r1. `prompt_e1.py` NO puede cambiar su prefijo ni su API: lo anclan
    selftest_congelado (candado `prompt_e1.prefijo_hash(False) == hash de
    ESQ-2` + tres comparaciones de identidad), selftest_ub53 P6
    (`PREFIJO_HASH == "4793d6152608"` y el literal del namespace) y
    selftest_manifiesto P3 (1.763 requests byte a byte contra la caché
    sellada). El prefijo viejo es lo sellado; sigue siendo importable tal cual.

r2. `prompt_v3_b54.py` es SOLO LECTURA e importa `prompt_e1` a nivel módulo
    (usa `ROL_POR_TO` y `build_user_message` de producción) → `prompt_e1` no
    puede importar el módulo v3 sin ciclo. El punto de construcción del
    prefijo v3 debe ser un módulo NUEVO (shim), no una edición de prompt_e1.

r3. selftest_manifiesto P7 exige que el runner con el manifiesto dev produzca
    una huella byte-idéntica a la golden → todo cambio del runner debe ser
    aditivo con default = comportamiento actual exacto.

Diseño: un registro de PERFILES DE EXTRACCIÓN E1. El manifiesto declara cuál
usa su corpus (campo top-level nuevo, opcional); la ausencia del campo es el
perfil vigente hoy (dev), byte-idéntico. El corpus escalado (manifiesto que
creará B5.7/tanda 1) declarará `"v3_b54"`.

- Perfil `"produccion_dev"` (default): prompt_e1 + schema.py viejos, tal cual.
- Perfil `"v3_b54"`: prompt_v3_b54 (prefijo/tool schema/mensaje/tabla TO→rol)
  + vocabulario congelado (prompt_congelado) + catálogo 102. CANDADO en la
  construcción del perfil: recomputa sha y hash y FRENA (RuntimeError) si no
  son `35e88c2dd0a2…` / `54a111e2175f` (decisión 1 del mandato); corre al
  cargar el manifiesto, antes de toda llamada.

Caching (docs/decisiones_caching_extraccion.md leído; las cinco decisiones se
respetan): D1 ya la cumple `bloques_sistema_v3()` (system en bloque único con
cache_control ephemeral); D2/D3 sin cambio (el cliente no cambia su fórmula ni
su log); D4 sin cambio (runner secuencial); D5 no aplica (evaluación no se
toca). NEVER-PAY-TWICE (decisión 4 del mandato): misma db
`e1_extractor/cache/e1_extraccion.db`, namespace NUEVO — la key incluye el
namespace, así que las keys viejas no se tocan ni colisionan; el namespace v3
sale del mismo patrón vigente (`make_namespace(DOMAIN,
code_ver="e1-extractor-v1-p" + hash_del_perfil, thinking=False)`) con
`54a111e2175f` como hash. El namespace del canal abierto y el de producción
dev quedan intactos byte a byte.

## 2. Entregable (a) — lista EXACTA de archivos a tocar (7: 6 ediciones + 1 nuevo)

Todos bajo `data/experiment/reextraccion_v2/` salvo indicación. Frontera
respetada: `e0_chunking/` NO se toca (B5.8.1 en vuelo); `b54_catalogo_v3/`,
`esq/code/` y `grafo_v2/code/` solo se IMPORTAN.

### 2.1 `e1_extractor/perfil_e1.py` — NUEVO (el "punto de construcción del prefijo" del mandato)

Registro de perfiles. Un `PerfilE1` (dataclass congelada) por modo, con:

- `nombre`, `prefijo_hash` (para namespace y banner),
- `build_request_kwargs(chunk, model, max_tokens=...)`,
- `build_user_message(chunk)`,
- `rol_por_to` (tabla TO→rol del perfil),
- `esquema`: objeto de vocabulario para validador/E2 con `entity_types`,
  `predicates`, `sujeto_predicates`, `sujetos_catalogo_set`,
  `firma_valida(src, pred, tgt)`,
- `labels_catalogo()`: id → {label, nivel} (consumo de E2, ver 2.6).

`perfil("produccion_dev")` → referencias directas a prompt_e1/schema vigentes
(cero transformación). `perfil("v3_b54")` → sys.path a
`data/experiment/b54_catalogo_v3/code` (solo import), y ANTES de exponer nada:

```python
if v3.PREFIJO_SHA256_V3 != "35e88c2dd0a2920302c29005b08ab9689405606d4bd5fcf8fb7ce807b1a3c512" \
        or v3.PREFIJO_HASH_V3 != "54a111e2175f":
    raise RuntimeError("candado v3: el prefijo integrado no reproduce el sello — se frena")
```

(los literales completos en el código; el módulo v3 ya frena por su lado si el
congelado subyacente no es `e69feaaa…`). Vocabulario del perfil v3: importado
de `prompt_congelado` (`ENTITY_TYPES_CONGELADO` 9, `PREDICATES_CONGELADO` 13,
`SUJETO_PREDICATES`, `firma_valida`) + `SUJETOS_CATALOGO_V3` (102) +
`ROL_POR_TO_V3` (71) + `build_user_message_v3` / `build_request_kwargs_v3`.
`labels_catalogo()` v3: derivado mecánicamente de `BLOQUE_CATALOGO_V3`
(línea `Sujeto_x — Label (alias: …)`; nivel por sufijo `[instancia]` /
`[rol del TO …]` / clase en otro caso; label sin el tramo de alias — el mismo
parsing que el módulo sellado usa internamente), con assert de 102 entradas.

NOTA DE INTEGRACIÓN VINCULANTE (decisión 2 del mandato), asentada en el
docstring del shim y respetada por todo consumidor: en `ROL_POR_TO_V3` los 36
mapeos a clase portan un id de CLASE en el campo `rol_id` — el campo se lee
como «sujeto por defecto del TO», nunca se asume rol. Los consumidores del
campo son: el mensaje (ya resuelto dentro del módulo sellado
`build_user_message_v3`), el manifiesto (2.4) y el selftest nuevo (§5); el
validador no consume `rol_id` (valida `sujeto_id` contra el set de 102, donde
clases y roles conviven).

### 2.2 `e1_extractor/validador_e1.py` — parametrización del vocabulario

`validar_salida(tool_input, chunk, canal_abierto=False, esquema=None)`:

- `esquema=None` (default): EXACTAMENTE el comportamiento actual — los
  imports de module-level de schema viejo quedan como el default; ni un byte
  de salida cambia en ningún call site existente.
- `esquema=<PerfilE1.esquema>`: `type` contra `esquema.entity_types`,
  `predicate` contra `esquema.predicates`, `sujeto_id` contra
  `esquema.sujetos_catalogo_set` (102: acepta los 102, rechaza los 5
  retirados y `Sujeto_rol_alcance_snp_cec` por ausencia del set — decisión 3),
  padre sugerido ídem, firmas con `esquema.firma_valida`. La lógica de ramas
  no cambia (`SUJETO_PREDICATES` v3 == viejo, verificado §0; los campos y
  required del tool schema v3 son idénticos, verificado §0).

### 2.3 `e1_extractor/cliente_e1.py` — namespace parametrizable

- `namespace_e1(canal_abierto=False, prefijo_hash=None)`: `None` → literal
  actual (P6 de ub53 asserta `namespace_e1()` sin argumentos: intacto);
  con hash → mismo patrón con ese hash.
- `ClienteE1Real(..., prefijo_hash=None)`: pasa el hash a `namespace_e1`.
  Default None → namespace histórico byte-idéntico. Misma db (la partición es
  por namespace dentro de la key).

Nada más cambia: fórmula D2, log D3, tope, guardián, reintento por corte —
intactos (el reintento copia kwargs y solo toca max_tokens: agnóstico del
prefijo).

### 2.4 `manifiesto_corpus.py` — campo `perfil_e1` + validación de roles por perfil

- Campo top-level OPCIONAL `perfil_e1`: ausente → `"produccion_dev"` (el
  manifiesto dev NO se edita); valor fuera del registro → `ErrorManifiesto`.
  Accessor `man.perfil_e1`. `VERSIONES_CONOCIDAS` sin cambio (campo opcional,
  no rompe la versión 1).
- `_validar_roles_contra_catalogo(tos, perfil)`: valida contra
  `perfil.rol_por_to` (para el dev: las 5 entradas pass-through son
  byte-idénticas a las de producción, así que el manifiesto dev valida igual).
  Reglas v3 por forma de entrada (decisión 2 aplicada):
  * entrada con `rol_id` string (30 roles + 35 mapeos a una clase):
    `rol_alcance` declarado == `rol_id` (el manifiesto declara el «sujeto por
    defecto del TO», sea rol o clase);
  * entrada `ri2_ci` (`rol_id` None, `clase_ids` de 2): `rol_alcance` declara
    la LISTA exacta `["Sujeto_casa_de_cambio", "Sujeto_agencia_de_cambio"]`
    (se admite lista en el campo solo para este caso; string ≠ lista →
    `ErrorManifiesto`);
  * TO sin entrada (docvig, fimipyme y cualquier otro): `rol_alcance` null
    obligatorio (un rol declarado sin respaldo del catálogo frena, como hoy).
- Mensaje del error "rol declarado sin rol en catálogo": el texto vigente
  dice «la tabla TO→rol del catálogo la puebla B5.4; hasta entonces…» — ya
  pobló. Se actualiza a un texto correcto post-B5.4 («el catálogo del perfil
  no declara rol para este TO: o el manifiesto declara null o el TO entra al
  catálogo por su circuito»). Esto VERSIONA el candado P1 de
  selftest_manifiesto (ver §4, candado C6) en la misma edición, declarado.

### 2.5 `corpus_v2/runner_corpus.py` — despacho por perfil

- `configurar(man)` resuelve `PERFIL = perfil_e1_mod.perfil(man.perfil_e1)`
  (los candados v3 corren acá, antes de cualquier llamada).
- `fase_e1`: `PERFIL.build_request_kwargs(c, model=MODEL_E1)` y
  `validador_e1.validar_salida(tool_input, c, esquema=PERFIL.esquema)`.
- clientes reales (fase E1 y reintentos de fase E3):
  `cliente_e1.ClienteE1Real(..., prefijo_hash=PERFIL.prefijo_hash_para_namespace)`
  (None en dev → namespace histórico).
- `fase_e3`: pasa `perfil=PERFIL` a `ratchet_e3.ciclo_ratchet`.
- `cerrar_e2`: pasa `esquema=PERFIL.esquema` y `labels=PERFIL.labels_catalogo()`
  a `e2_lib.reducir`.
- banner: imprime el hash del perfil activo (dev: el mismo string de hoy —
  el banner no integra la huella P7, que es de archivos).

Con manifiesto dev: PERFIL es el default y cada uno de esos puntos degrada a
la llamada actual — P7 (golden stub) y el chequeo de hits de pro quedan
intactos por construcción.

### 2.6 `e2_reduce/e2_lib.py` — vocabulario y labels parametrizados

`reducir(..., esquema=None, labels_catalogo=None)`:

- defaults None → schema viejo + `_labels_catalogo()` del JSON vigente:
  byte-idéntico (P5 de selftest_manifiesto lo demuestra).
- en modo v3: `PREDICATES`/`SUJETOS_CATALOGO_SET`/`is_valid_triple` del
  esquema inyectado; `nodo_sujeto` toma label/nivel del dict inyectado.
  HALLAZGO 2 (defecto latente que el cableado evita): hoy `nodo_sujeto` hace
  `labels_cat.get(sujeto_id, {})` con fallback silencioso label=id, nivel=""
  — con sujetos v3 y el JSON viejo, el grafo escalado saldría degradado sin
  aviso. Con el dict del perfil, cada id v3 tiene label y nivel reales; se
  agrega además una ADVERTENCIA contada en el reporte E2 si algún sujeto cae
  al fallback (registro, no rechazo — no cambia grafos dev porque en dev no
  hay ids fuera del JSON).

### 2.7 `e3_verificador/ratchet_e3.py` — reintentos con el perfil de la corrida

`build_reextraccion_kwargs(..., perfil=None)` y
`ciclo_ratchet(..., perfil=None)` / `reextraer_chunk(..., perfil=None)`:

- `None` → `prompt_e1.build_request_kwargs` + `validar_salida` sin esquema:
  byte-idéntico (selftest_e3 y las corridas selladas intactos).
- con perfil → `perfil.build_request_kwargs` (prefijo v3 idéntico al de la
  fase E1 de la corrida: el feedback sigue DESPUÉS del breakpoint, el caching
  no se invalida) + re-validación con `esquema=perfil.esquema`.

Sin esto, el ciclo de ratchet de una corrida v3 RE-EXTRAERÍA CON EL PREFIJO
VIEJO y validaría contra el catálogo viejo (HALLAZGO 3): mezcla de prefijos
dentro de la misma unidad y rechazo espurio de los sujetos/tipos v3. Es la
razón por la que ratchet_e3.py entra a la lista aunque el mandato no lo
enumere entre los esperados (su lista era abierta: «esperados: …»). E3 en sí
(prompt_e3, cliente_e3, comun_e3) NO se toca: su prompt declara
explícitamente que no valida esquema («La elección de granularidad de
sujetos, tipos de entidad o predicados: eso lo controla otra capa»),
su namespace y sus cachés selladas quedan intactos.

### Consumidores relevados y DECLARADOS FUERA (no se tocan, con causa)

| Archivo | Por qué queda fuera |
|---|---|
| `e1_extractor/prompt_e1.py` | prefijo dev sellado por 3 candados (r1) — el modo v3 vive en el shim |
| `grafo_v2/code/schema.py` y `extract.py` | fuente del esquema v2 dev / extractor legado Fase 2.2 — historia sellada |
| `esq/code/*` (congelado, esq3b, cobertura, control, suj_freq…) | mediciones selladas de la saga ESQ; importan prompt_e1/schema con defaults intactos |
| `e3_verificador/prompt_e3.py`, `cliente_e3.py`, `comun_e3.py` | E3 agnóstico del esquema (verifica contenido); caché/namespace sellados |
| `corpus_v2/ensamblar_corpus.py` | sin contacto con el catálogo (grep limpio); tests dev5 solo corren con esa suite |
| `corpus_v2/r1_*.py`, `reextraccion_dirigida.py` | circuito r1 / laudo post-corrida del corpus DEV — herramientas históricas legacy |
| `e1_extractor/estimacion_e1.py`, `runner_faseB_e1*.py`, `e3_verificador/estimacion_*` | estimadores/runners históricos de fase A/B dev; la estimación v3 es materia del re-presupuesto B5.7 (nota para su mandato) |
| `e1_extractor/selftest_canal_abierto_e1.py` | FAIL preexistente conocido (check stale post-P1″), derivado a la entrada 14 de la cola — no se toca acá |
| `escalado_prep/*` (catalogo_sujetos.py, etc.) | censo/inventario históricos, solo informan |
| `manifiestos/desarrollo_5tos.json` | NO se edita: el campo nuevo es opcional con default |

## 3. Entregable (b) — inventario de candados y selftests, con plan por candado

Ninguno se borra ni se afloja; dos se VERSIONAN con justificación y edición
declarada (C6, C7). «Intacto» = cero ediciones y re-corrida en verde exigida
por la fase 2.

| # | Candado / selftest | Qué asegura hoy | Plan |
|---|---|---|---|
| C1 | `esq/code/selftest_congelado.py` (46 checks) — `prompt_e1.prefijo_hash(False) == ESQ-2`; `t != prompt_e1.PREFIJO_SISTEMA`; hash congelado ∉ {v2, v1, producción, abierto} | la cadena ESQ-2 → v1 → v2 → congelado y que producción dev sigue siendo la sellada | INTACTO (prompt_e1 no cambia). Se re-corre: 46/46. Nota semántica al acta: «producción» ahí nombra el prefijo dev pre-v3, que sigue siendo el que esas corridas selladas usaron |
| C2 | `selftest_ub53.py` P6 — `PREFIJO_HASH == "4793d6152608"`, literal del namespace E1, techos 8.192/16.384/32.768 | prefijo/namespace/techos de la producción dev | INTACTO (defaults de `namespace_e1` y `ClienteE1Real` preservan el literal). Se re-corre: 40/40. P1–P5 usan runner/cliente con defaults → sin cambio |
| C3 | `selftest_manifiesto.py` P3/P4 — 1.763 requests E1 y 1.762 keys E3 byte a byte contra cachés selladas, 0 misses proyectados | reproducibilidad de la corrida dev | INTACTO (P3 construye con `prompt_e1.build_request_kwargs` directo; P4 con prompt_e3 intacto) |
| C4 | `selftest_manifiesto.py` P7 — golden de 14 archivos del runner stub (pro) | comportamiento del runner con el manifiesto dev | INTACTO por defaults del despacho (2.5). Cualquier dif en la huella = FRENO de la fase 2 |
| C5 | `selftest_manifiesto.py` P5/P6 — paridad E2 byte a byte + sellos del ensamblado (8e2eadee…/98ee43e5…/5bf4ffd7…) | E2/ensamblado dev | INTACTO (defaults de `reducir`; ensamblar sin cambio) |
| C6 | `selftest_manifiesto.py` P1, caso `fx_rol_gap` — exige el fragmento «puebla B5.4» en el error del loader | mensaje del gap de rol pre-B5.4 | SE VERSIONA: B5.4 ya pobló la tabla; mensaje y fragmento esperado se actualizan JUNTOS en la misma edición (candado de mensaje, no de sellado; los otros 9 adversariales P1 intactos). Se AGREGAN casos: `perfil_e1` desconocido rechazado; ausencia del campo = default dev; reglas de rol v3 (rol nuevo ok / clase como sujeto por defecto ok / ri2_ci lista / hueco exige null). El conteo del selftest sube de 35; nunca baja |
| C7 | mensajes de `_validar_roles_contra_catalogo` (manifiesto_corpus) | texto del freno de roles | SE VERSIONA junto con C6 (misma edición, ver 2.4) |
| C8 | `selftest_e1.py` — catálogo viejo en el enum del prefijo dev; archivos de chunks ⊆ `schema.ROL_POR_TO` | contrato E1 dev | INTACTO (prompt_e1/schema sin cambio; `validar_salida` gana un kwarg con default). Se re-corre |
| C9 | `selftest_e3.py` — ratchet con defaults | ciclo E3 dev | INTACTO (`ciclo_ratchet` gana kwarg con default). Se re-corre |
| C10 | `selftest_corpus.py` — muertes simuladas + reanudación del runner (stub, dev) | mecánica de reanudación | INTACTO (defaults). Se re-corre; su efecto colateral conocido sobre `salida_selftest/` sigue derivado a la entrada 14 de la cola |
| C11 | `b54_catalogo_v3/code/selftest_prompt_v3_b54.py` (57) | el sello v3 mismo | SOLO LECTURA, se re-corre tal cual: 57/57 |
| C12 | selftests de `e0_chunking` (E0 57, B5.2 39) | segmentación sellada | PROHIBIDO tocar y sin contacto con el catálogo; se re-corren para la batería de la fase 2 |
| C13 | `selftest_canal_abierto_e1.py` | canal abierto retirado | FAIL preexistente declarado (cola entrada 14); no se corre en la batería ni se toca |
| C14 | candado del propio módulo v3 (`bloque_catalogo_congelado` frena si el congelado ≠ `e69feaaa…`) | cadena congelado→v3 | heredado por import; el candado NUEVO del perfil (2.1) agrega la punta producción→v3 |
| C15 | selftests de esq no listados en el mandato (cobertura_esq2, control_esq, esq3b, descubrimiento) | mediciones ESQ selladas | INTACTOS por análisis (importan prompt_e1/validador con defaults); no integran la batería exigida, se declaran |

## 4. Hallazgos de fase 1 (reportados, no resueltos por mi cuenta)

1. **El cableado es del ESQUEMA CONGELADO COMPLETO, no solo del catálogo**:
   el tool schema v3 emite 9 tipos / 13 predicados; validador y E2 deben
   validar contra ese vocabulario en modo v3 (§0). El plan §2.2/§2.6 lo
   resuelve importando el vocabulario del módulo sellado `prompt_congelado`.
   Si la mesa prefiere restringir esta unidad al catálogo estricto, el
   validador v3 rechazaría sistemáticamente tipos que su propio tool schema
   ofrece — lo dejo decidido en el freno, con mi recomendación: vocabulario
   congelado completo.
2. **Fallback silencioso de labels en E2** (`nodo_sujeto`): con ids v3 y el
   JSON viejo, label=id y nivel="" sin aviso. Resuelto por inyección de
   labels del perfil + advertencia contada (§2.6).
3. **El ratchet E3 re-extraería con el prefijo viejo** en una corrida v3 si
   no se parametriza (§2.7). Entra a la lista de archivos por esto.
4. Observación menor, sin acción (módulo sellado): dos comentarios internos
   de `prompt_v3_b54.py` conservan los conteos pre-mini-laudo («31 roles A2 +
   35 mapeos», línea de sección) mientras el código y el selftest sellado
   materializan 30 + 36. El contrato real está verificado (§0).
5. El mensaje de error del loader de manifiesto quedó anacrónico post-B5.4
   (C6/C7): se versiona con el candado, no en silencio.

## 5. Entregable (c) — plan del selftest nuevo del cableado

`data/experiment/reextraccion_v2/selftest_cablev3.py` — USD 0, sin red,
corrible desde cwd ajeno, patrón N/N. Bloques:

- **B1 candados**: perfil v3 → sha/hash recomputados == sellados (los dos
  literales completos en el selftest, independientes de los del shim);
  monkeypatch del sha reportado por el módulo v3 → la construcción del perfil
  FRENA con RuntimeError; restaurado, vuelve a construir.
- **B2 mensajes** (mandato fase 2): (i) chunk real dev (salida_enm01) →
  kwargs v3 con system/tools v3 y mensaje BYTE-IDÉNTICO al de producción;
  (ii) chunk de TO con rol nuevo (p. ej. `traval.pdf`) → línea de alcance con
  el rol y la guarda de ejecuta («NO es el ejecutor por defecto en ejecuta»);
  (iii) chunk de TO con mapeo a clase (p. ej. `ayccef.pdf` →
  `Sujeto_entidad_financiera` como sujeto por defecto) y el caso `ri2_ci.pdf`
  (dos clases, variante declarada de la línea); (iv) hueco (`docvig.pdf`) →
  sin línea de alcance.
- **B3 validador**: con `esquema` v3 ACEPTA una muestra de los 102 (clase
  vigente, adición, rol nuevo, id de clase usado como sujeto) y los tipos/
  predicados congelados (Potestad, Condicion, Definicion, `condicion_de` con
  firma válida); RECHAZA los 5 retirados uno a uno, `Sujeto_rol_alcance_snp_cec`,
  y un type/predicate fuera del vocabulario congelado. Además: los 102
  aceptados se verifican POR EXTENSIÓN (loop sobre `SUJETOS_CATALOGO_V3`
  con una relación aplica_a mínima cada uno, conteo 102/102 recomputado).
  Camino default: `validar_salida` sin `esquema` sobre un registro real de la
  corrida dev == salida actual (igualdad de dicts).
- **B4 namespace**: cliente/`namespace_e1` con hash v3 → namespace contiene
  `54a111e2175f`; sin argumentos → literal histórico; ambos distintos.
- **B5 manifiesto**: sintético v3 (TOs de `escalado_prep/e0_dry`, solo
  lectura) carga con `perfil_e1: "v3_b54"`; adversariales: perfil
  desconocido, rol de clase mal declarado, ri2_ci con string, hueco con rol.
- **B6 runner stub v3**: corrida `--stub` con el manifiesto sintético v3 →
  termina, y los requests que recibió el stub llevan el system v3 (sha
  recomputado del texto) y el tool schema v3 (enum de 102); reanudación
  idempotente básica en v3 (relanzar no duplica).
- **B7 ratchet**: `build_reextraccion_kwargs` con perfil v3 → system/tools
  byte-idénticos a los de la fase E1 v3, feedback después del breakpoint;
  default → byte-idéntico al histórico.
- **B8 E2**: `reducir` con esquema v3 + labels v3 sobre un jsonl sintético
  con Potestad/`condicion_de`/rol v3/clase-como-sujeto → ensambla con labels
  y niveles reales (ningún fallback); default sobre un TO dev sellado →
  byte-idéntico (redundante con P5, barato).

La batería de cierre de la fase 2 (outputs pegados, como exige el mandato):
selftest_manifiesto completo, E0 57/57, B5.2 39/39, ub53 40/40, congelado
46/46, prompt_v3 57/57, selftest_e1, selftest_e3, selftest_corpus, y el
selftest nuevo N/N.

## 6. Qué NO hace esta unidad (fronteras re-declaradas)

- No crea el manifiesto del corpus escalado (B5.7/tanda 1); el campo
  `perfil_e1: "v3_b54"` queda listo para que ese manifiesto lo declare.
- No re-presupuesta (B5.7) ni corre nada pago (el humo real es la tanda 1).
- No toca E3 (prompt/cachés), ni e0_chunking, ni docs/tesis, ni nada sellado.
- No edita el plan ni la cola.
