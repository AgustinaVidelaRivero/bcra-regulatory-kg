# Laudo B2.4 — asignación de sujeto: los ocho patrones y las entradas BKL-0001, 0002, 0018, 0020, 0021 y 0028

**VERSIÓN PARA FIRMAR (mesa, 09/10/2026; corregida el mismo día con la revisión de la autora)**, con las decisiones de la autora del 09/10/2026 sobre las dos lecturas (§3.1). Redactado por la
mesa el 07/10/2026 (noche), con las decisiones de la autora del mismo día sobre la ficha de decisión de la mesa. Fila B2.4 del plan (`docs/plan_tesis.md:383`); condición 13 de la tanda 1
(`docs/checklist_pre_escalado.md`, línea de las condiciones) y fila X9 del checklist: se firma antes de la tanda 1.

## 1. Qué decide

- Resuelve las entradas del backlog que la autora asignó a este laudo el 04/10/2026 (`plan:383`, decisión 1):
  - BKL-0001 y 0002 se cierran como `verificado`;
  - BKL-0018 y 0021 quedan en `triaged`, como límite y cuarentena declarados.
- Resuelve los ocho patrones de asignación de sujeto, BKL-0009 a BKL-0016, con su lectura sobre el grafo de U-REEXT-T0 (`plan:383`,
  decisión 3): cinco se cierran como `verificado` y tres quedan como límites declarados de la extracción, en `triaged` (§3.1).
- Suma BKL-0020, del mismo origen que BKL-0021: los sujetos de cuarentena de v3 sin padre (`data/backlog/expediente_retriage_v3.md:182-196`).
- Fija la meta de los sujetos resueltos del tablero (fila de la mención del sujeto y los sujetos no mapeables).
- No corrige el grafo: lo que no se corrige se declara.

## 2. Sobre qué grafo se lee

El diez r2b completo, KG-Tanda0-Diez-r2b, `a9631a64…` (sellado en `bbc38dc`; `data/experiment/neo4j/grafos.py`), por decisión de la autora.
El re-sellado único posterior no toca los puntos de los ocho patrones. R2-3 (`803623a`) y R2-3 bis (`dac7d57`) cambian solo `docvig::3.4`
(`data/experiment/reresolucion_catalogo/freno_r2_3.md:13-18`), y ninguno de los ocho puntos está en docvig. U-OMISIONES-COD cambia la
procedencia (grupos G y J), las menciones (grupo B) y las bases de los relativos (grupo C), no el destino de las aristas de sujeto. Si
alguno de esos cambios moviera una arista de estos puntos, la re-medición posterior al re-sellado lo dice, y el laudo recibe una nota.

## 3. Decisiones de la autora (07/10/2026), por entrada

| entrada | decisión | evidencia |
|---|---|---|
| BKL-0009 a BKL-0016 (los ocho patrones) | Se resuelven con la lectura de T3 (control o de U-REEXT-T0, lectura asistida de la instancia), más una **segunda lectura a ciegas de los 8 puntos**, que hizo una sesión nueva de la mesa, la misma de la segunda lectura de las 41 de la enmienda 8, el 08/10/2026 desde las 18 h. Las divergencias las adjudicó la autora. **Resultado (§3.1): cinco se cierran como `verificado`; tres quedan como límites declarados, en `triaged`.** Se declara el cambio de verificación: lectura asistida y a ciegas, en lugar de chunk contra PDF. | `data/experiment/reext_t0/t3/salida/lectura_controles_t3.md:60-68`; despacho de la mesa |
| BKL-0001 y BKL-0002 | Se cierran con el test por punto de la suite r2b, declarando el cambio de verificación: test de la suite en lugar de chunk contra PDF. | `data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2b/suite_perfil_r2.md:70-71`: BKL-0001 resuelto (7 nodos anclados en 2.8.3.3, uno con «75 veces SMVM»); BKL-0002 resuelto (35 anclados en 3.5.3, 2 con la ventana de 3 días hábiles) |
| BKL-0018 | Límite declarado, junto con BKL-0004, que persiste como falla conocida sellada. | `suite_perfil_r2.md:18` |
| BKL-0021 | Queda como **cuarentena declarada**, en `triaged`. Los dos propuestos («la entidad nominada», `ext::11.1.1.10` y `ext::3.18.2::intro`; «la entidad nominada por el exportador», `ext::7.3::intro` y `ext::7.3.7`) quedan en cuarentena con sus 4 `aplica_a`. El rol nuevo, si corresponde, entra por el procedimiento de crecimiento de la enmienda 4 al protocolo (FIRMADA el 07/10/2026, §1) al cierre de la tanda 1: la clave llega al umbral de 2 unidades. La misma sesión leyó si las 4 filas «entidad(es) encargada(s) del seguimiento de la(s) oficialización(es)» (`ext::4.4::intro`, `ext::4.4.2`, `ext::10.8`, `ext::11.1.5::intro`) designan el mismo sujeto: lo designan y entran a la clave (§3.1). **Esta decisión reemplaza la decisión (c) del 06/10/2026** (un rol nuevo por U-RERESOL-CAT; mandato de U-REEXT-T0, `:585-588`), que ninguna unidad ejecutó. | control q de T3: la mención reaparece como «la entidad nominada» (`lectura_controles_t3.md:73-76`); la condición de cierre del 04/10 («no reaparece») no se cumplió |
| BKL-0020 | Cuarentena declarada: 1 fila en r2b, «una entidad originante» (`cap::3.1.3::cierre`), por debajo del umbral. | registro de no mapeados del diez r2b |
| Meta de resueltos (tablero) | Sin meta numérica: dependen del crecimiento del catálogo (enmienda 4). La cuarentena se declara con su cifra: 294 filas en el registro del diez r2b (164 en cuarentena, 128 resueltas a clase, 2 descartadas) y 98 nodos `Sujeto_propuesto_*`. | `docs/tablero_correcciones.md`, fila de la mención del sujeto |

### 3.1 Resultado de las dos lecturas y decisiones de la autora (09/10/2026)

**Las lecturas.**
- La segunda lectura a ciegas, de una sesión nueva de la mesa sobre el diez r2b (`a9631a64…`), quedó sellada antes de compararse con T3
  (18:30:35 del 08/10/2026):
  - ocho patrones: 18:28:59 (`4b39868c…`), con sus dos anexos;
  - cuatro filas: 18:30:23 (`bf1176fc…`).
- Paquete: `fuera_del_repo/scratchpads/3a3e232d-f9a6-4197-ba2e-7a3f30b6d678/scratchpad/revision_segunda_lectura_ciega_41_patrones_filas/`.
- La revisión de la mesa del 09/10/2026, sobre una copia, controló los sellos y la tabla de divergencias.

**Los ocho patrones** (adjudicación de las divergencias D2-1 a D2-3 con T3):

| entrada | resultado |
|---|---|
| BKL-0009, 0010, 0011, 0012 y 0016 | No reaparecen: se cierran como `verificado`. |
| BKL-0013 | Reaparece en 3 de las 646 aristas del universo de ext: `ext::8.5.18.2` (2, «La entidad emisora de la mencionada certificación» → entidad financiera) y `ext::14.2.1.6` (1, de frontera). D2-1: la autora acepta el veredicto con las anclas de la segunda lectura. |
| BKL-0014 | Reaparece: 2 aristas de `ext::14.1.4` a `Sujeto_exportador` («el exportador», en un punto que se aplica al VPU adherido al RIGI). D2-2: cuenta como reaparición. |
| BKL-0015 | Vale `ext::7.9.6`, donde está hoy la norma del patrón, porque el patrón sigue a la norma y no al número de punto (el «3.17» del triage es hoy `ext::7.9`; contradicción reportada por la lectura, CLAUDE.md §4.d). Reaparece: 1 arista a `Sujeto_persona_humana` («Los residentes»). D2-3. |

**BKL-0013, 0014 y 0015 quedan como límites declarados de la extracción.**
- **La cifra en `a9631a64`:** 3, 2 y 1 aristas.
- **Vigilancia por tanda.**
  - En el grafo de cada tanda se corren las mismas consultas de la segunda lectura: el universo del colectivo de sujetos y las aristas de
    los puntos del patrón.
  - **Quién lee:** la sesión de la mesa que revisa el FRENO de la tanda lee cada acierto contra el texto de su unidad, con el criterio de
    la segunda lectura (`criterio_mesa_L2_patrones_sujeto.md`, sellado el 08/10/2026 a las 18:18:19, en el paquete `fuera_del_repo/scratchpads/3a3e232d-f9a6-4197-ba2e-7a3f30b6d678/scratchpad/revision_segunda_lectura_ciega_41_patrones_filas/`).
  - **La regla** (decisión 4 de la autora, 09/10/2026): sin umbral. Se informa la cifra en el FRENO de la tanda. Lo que reabre la
    corrección es una forma de falla nueva, no que la cifra suba.
- **Por qué la verificación de la mención no las atrapó.** Esa verificación controla solo que la mención esté, literal, en el texto de la
  unidad (`verificar_tramo` sobre `texto_completo`, `pyd_r2/code/validador_r2.py:830`).
  - Las 6 menciones dan `exacta` y están en el texto propio de su unidad, no en la herencia.
  - El sujeto lo pone la sugerencia del modelo (`R4_sugerencia_modelo`): fuera de R1, la sugerencia gana a las reglas del texto
    (`reextraccion_v2/corpus_v2/r1_e4.py:426-427`), y nada controla que la mención designe ese sujeto.
  - En 3 de las 6 (`ext::8.5.18.2`, dos, y `ext::7.9.6`) ninguna regla del texto resuelve la mención.
  - En las otras 3 (`ext::14.1.4`, dos, y `ext::14.2.1.6`) la regla del texto da el mismo sujeto: el error es de contexto, no de mención.
- **Corrección de código, medida sobre lo guardado** (USD 0; medición de la mesa del 09/10/2026, script y salida en el paquete de la mesa).
  Las dos reglas candidatas, contra las 646 aristas del universo de BKL-0013 clasificadas por la segunda lectura (574 correctas):

  | regla | casos que manda a cuarentena | correctas que pierde (universo) | aristas de sujeto que manda a cuarentena (de 2.616 del diez r2b) |
  |---|---|---:|---:|
  | (A) exigir la mención en el tramo de la norma | 5 de los 6 (todos menos `…eca5ca`, de BKL-0014); entre ellos están las 3 aristas que repiten el patrón en el universo, que son las 3 de BKL-0013 | 194 de 574 | 1.400 |
  | (B) mandar a cuarentena la sugerencia del modelo sin respaldo del texto | 3 de los 6: las 2 de `ext::8.5.18.2` (BKL-0013) y la de `ext::7.9.6` (BKL-0015) | 396 de 574 | 993 |

  Ninguna entra al grupo 2: las dos pierden muchas aristas correctas. La (A) falla porque el tramo guardado de una norma casi nunca incluye a
  su sujeto («podrán acceder…», sin «Los residentes»).

**El universo de BKL-0013: 646 aristas, 574 correctas y 72 más.** Lo arma el anexo sellado de la segunda lectura
(`lectura_mesa_L2_anexo_universo_BKL0013.json`, `5d70cc79…`, campo `conteo`). Son las aristas `aplica_a` y `ejecuta` de las normas de ext
con una mención del colectivo, o hacia entidad financiera o un sujeto más estrecho.
- **Las 574 correctas:** 493 van al rol, 79 a EF porque el texto nombra a EF, y 2 vienen de normas con aristas a EF y a la clase cambiaria.
- **Las 72 que no son correctas:**

  | clase de la lectura | aristas | qué son |
  |---|---:|---|
  | `repite_patron` | 3 | las 3 de BKL-0013 (`ext::8.5.18.2`, dos, y `ext::14.2.1.6`), que están entre los 6 casos de la tabla de arriba |
  | `otro_defecto_cuarentena` | 58 | aristas a un `Sujeto_propuesto_*` (método `cuarentena`): el colectivo quedó en cuarentena, con el rol disponible en el catálogo. No es un sujeto equivocado sino una resolución pendiente, y ya cuenta en la cuarentena declarada (§3, meta de resueltos) |
  | `otro_defecto` | 7 | errores de sujeto fuera de los ocho patrones (detalle abajo) |
  | `falso_positivo_filtro` | 4 | entraron al universo por el filtro (`ext::3.10`, «personas jurídicas que no sean entidades autorizadas…»), pero no nombran al colectivo como sujeto: no se juzgan |

- **Los 7 errores de sujeto fuera de los ocho patrones** quedan como límite declarado, con su cifra: 7 en el universo de ext, que no es
  una muestra del grafo. Tienen dos formas:
  - **La EF del texto cumple otro papel en la norma (5):** cliente apoderado (`ext::5.7.3.3`, dos), prestamista (`ext::3.6.4.1`), referencia
    del horario de atención (`ext::5.2.2`) y entidad donde están las cuentas, cuando la obligación exceptuada es del exportador
    (`ext::2.2.2.1`). Dos vienen de `R1_label_exacto` y tres de la
    sugerencia del modelo.
  - **Faltan sujetos que la norma nombra junto a EF (2):** `ext::4.1.1` y `ext::4.1.4.6` («las entidades financieras y otras emisoras de
    tarjetas»), con la arista solo a EF.
  - **Propuesta de la mesa:** una entrada nueva del backlog (sería BKL-0041; la última es BKL-0040), en `triaged`, con las 7 aristas como
    evidencia y la vigilancia por tanda de arriba, sin umbral. PENDIENTE de la autora: el lote del §5 no la incluye hasta que la apruebe.

**Las 4 filas de BKL-0021.**
- **Decisión de la autora:** designan el **mismo sujeto**, porque la herencia es parte del texto que lee E1: la intro de `ext::11.1` dice que
  la entidad la nomina el importador.
- **La clave del rol de la entidad nominada por el importador** queda con 5 unidades: `ext::11.1.1.10`, `ext::4.4::intro`, `ext::4.4.2`,
  `ext::10.8` y `ext::11.1.5::intro`.
- **La entidad nominada por el exportador es otro sujeto:** `ext::3.18.2::intro`, `ext::7.3::intro` y `ext::7.3.7`.
- **`Sujeto_propuesto_la_entidad_nominada` junta las dos** (`ext::11.1.1.10` y `ext::3.18.2::intro`). Cuando el rol se cree al cierre de la
  tanda 1 (enmienda 4, §1), las dos entidades tienen que quedar separadas, cada una con su clave.

**Cómo queda el estado de las entradas** (DECIDIDO por la autora el 07/10/2026, noche).
- La máquina de estados del backlog (`docs/spec_backlog_refinamiento.md`, §2 y §5) no tiene un estado de «límite declarado» ni de
  «cuarentena declarada».
- BKL-0018, 0020 y 0021 quedan en `triaged`, con un evento `nota`: son límites o cuarentenas declaradas, no descartes, y no se corrigen en
  esta versión.
- BKL-0001, 0002 y 0009 a 0016 pasan a `verificado` (los ocho, si la segunda lectura y la adjudicación no cambian el veredicto).
  **[09/10/2026]** Con las lecturas adjudicadas (§3.1): BKL-0009, 0010, 0011, 0012 y 0016 pasan a `verificado`; BKL-0013, 0014 y 0015
  quedan en `triaged`, con un evento `nota`, como límites declarados de la extracción.

**BKL-0028** (miembro del rol de alcance de ctacor; sumada por la autora el 07/10/2026, noche).
- **El defecto.** La entrada nació porque el catálogo v3 enrutaba por alias las variantes «del exterior» a ids domésticos, y por eso
  U-ESQ-V3 no adjudicó el miembro del rol de ctacor.
- **Su condición de cierre** («ningún id del bloque de catálogo tiene definición o label doméstico junto a un alias del exterior») ya se
  cumple en el catálogo r2. Fuente: U-CAT-UNICO C2, `bd2122d`, con 0 ids domésticos con alias del exterior y tres ids del exterior
  separados; nota del 01/10/2026 en `backlog.jsonl`.
- **Lo que queda.** En la tabla de la release, `Sujeto_rol_alcance_ctacor` tiene `miembros_ids` vacío, con los rótulos «Entidades
  financieras del país» y «Casas de cambio (Sección 3)» (`catalogo_unico/generados_r2/rol_por_to_r2.json`).
- **Propuesta de la autora:** el mismo camino que BKL-0021 (el procedimiento de crecimiento de la enmienda 4 al cierre de la tanda 1).
- **Recomendación de la mesa, distinta:** cerrar BKL-0028 como `verificado` por su propia condición de cierre, y llevar la adjudicación
  del miembro del rol de ctacor a la release siguiente, como cambio de la tabla de la release (fila F12). Tres razones:
  - El §1 de la enmienda 4 hace crecer el catálogo de resolución desde menciones en cuarentena, y la pertenencia a un rol no es una
    mención en cuarentena.
  - La enmienda fija el catálogo del request, y con él la tabla de roles, por release (§1, punto 4).
  - ctacor no está en la tanda 0 ni en la tanda 1, así que no la afecta.
- **Decisión de la autora (07/10/2026, noche): se adopta la recomendación de la mesa.** BKL-0028 se cierra como `verificado` por su
  condición de cierre, y la adjudicación del miembro de `Sujeto_rol_alcance_ctacor` va a la release siguiente (F12).

## 4. Qué falta para firmarlo

1. ~~La segunda lectura a ciegas de los 8 puntos, y la adjudicación de la autora sobre sus divergencias con T3.~~ Hechas: §3.1
   (09/10/2026).
2. ~~La lectura de las 4 filas de «entidad(es) encargada(s) del seguimiento».~~ Hecha y decidida: §3.1 (09/10/2026).
3. ~~La decisión sobre BKL-0028.~~ Decidida el 07/10/2026 (noche): la recomendación de la mesa (§3).

Las dos lecturas las hizo una sesión nueva de la mesa el 08/10/2026, desde las 18 h, junto con la segunda lectura de las 41 de la
enmienda 8 (§3.1).

## 5. Lote de eventos del backlog (se agrega a `data/backlog/backlog.jsonl` con el commit de la firma)

El backlog es append-only (`docs/spec_backlog_refinamiento.md`, §5). Los cambios de estado dependen de la firma; las dos
lecturas ya están hechas y adjudicadas (§3.1). El lote se escribe acá y se agrega al archivo con la firma, con la fecha de la firma en
`ts`. Los tres patrones que reaparecen llevan una `nota` en lugar de `cambio_estado` y quedan en `triaged`.

```jsonl
{"evento": "cambio_estado", "id": "BKL-0001", "estado": "verificado", "aplicado_en": null, "ts": "<FECHA_FIRMA>", "nota": "laudo B2.4: resuelta en r2b por el test por punto de la suite (7 nodos anclados en 2.8.3.3, uno con «75 veces SMVM»; suite_perfil_r2.md:70); cambio de verificación declarado: test de la suite en lugar de chunk contra PDF", "evidencia": "docs/laudo_B2.4_sujetos.md"}
{"evento": "cambio_estado", "id": "BKL-0002", "estado": "verificado", "aplicado_en": null, "ts": "<FECHA_FIRMA>", "nota": "laudo B2.4: resuelta en r2b por el test por punto de la suite (35 nodos anclados en 3.5.3, 2 con la ventana de 3 días hábiles; suite_perfil_r2.md:71); cambio de verificación declarado", "evidencia": "docs/laudo_B2.4_sujetos.md"}
{"evento": "cambio_estado", "id": "BKL-0009", "estado": "verificado", "aplicado_en": null, "ts": "<FECHA_FIRMA>", "nota": "laudo B2.4: el patrón no reaparece en a9631a64 (cap::2.5), por la lectura de T3 y la segunda lectura a ciegas adjudicada; cambio de verificación declarado", "evidencia": "docs/laudo_B2.4_sujetos.md"}
{"evento": "cambio_estado", "id": "BKL-0010", "estado": "verificado", "aplicado_en": null, "ts": "<FECHA_FIRMA>", "nota": "laudo B2.4: el patrón no reaparece en a9631a64 (ext::14.5), por la lectura de T3 y la segunda lectura a ciegas adjudicada; cambio de verificación declarado", "evidencia": "docs/laudo_B2.4_sujetos.md"}
{"evento": "cambio_estado", "id": "BKL-0011", "estado": "verificado", "aplicado_en": null, "ts": "<FECHA_FIRMA>", "nota": "laudo B2.4: el patrón no reaparece en a9631a64 (ric::3.1), por la lectura de T3 y la segunda lectura a ciegas adjudicada; cambio de verificación declarado", "evidencia": "docs/laudo_B2.4_sujetos.md"}
{"evento": "cambio_estado", "id": "BKL-0012", "estado": "verificado", "aplicado_en": null, "ts": "<FECHA_FIRMA>", "nota": "laudo B2.4: el patrón no reaparece en a9631a64 (ext::13.4), por la lectura de T3 y la segunda lectura a ciegas adjudicada; cambio de verificación declarado", "evidencia": "docs/laudo_B2.4_sujetos.md"}
{"evento": "nota", "id": "BKL-0013", "ts": "<FECHA_FIRMA>", "nota": "laudo B2.4: el patrón reaparece en a9631a64 (3 de las 646 aristas del universo de ext: ext::8.5.18.2, dos, y ext::14.2.1.6, de frontera), por la segunda lectura a ciegas adjudicada (D2-1); límite declarado de la extracción, con su cifra y vigilancia por tanda; ninguna corrección de código entra (medición de la mesa del 09/10/2026); queda en triaged", "evidencia": "docs/laudo_B2.4_sujetos.md"}
{"evento": "nota", "id": "BKL-0014", "ts": "<FECHA_FIRMA>", "nota": "laudo B2.4: el patrón reaparece en a9631a64 (2 aristas de ext::14.1.4 a Sujeto_exportador), por la segunda lectura adjudicada (D2-2); límite declarado de la extracción, con su cifra y vigilancia por tanda; queda en triaged", "evidencia": "docs/laudo_B2.4_sujetos.md"}
{"evento": "nota", "id": "BKL-0015", "ts": "<FECHA_FIRMA>", "nota": "laudo B2.4: vale ext::7.9.6, donde está hoy la norma del patrón (D2-3); el patrón reaparece en a9631a64 (1 arista a Sujeto_persona_humana, «Los residentes»); límite declarado de la extracción, con su cifra y vigilancia por tanda; queda en triaged", "evidencia": "docs/laudo_B2.4_sujetos.md"}
{"evento": "cambio_estado", "id": "BKL-0016", "estado": "verificado", "aplicado_en": null, "ts": "<FECHA_FIRMA>", "nota": "laudo B2.4: el patrón no reaparece en a9631a64 (ext::3.18), por la lectura de T3 y la segunda lectura a ciegas adjudicada; cambio de verificación declarado", "evidencia": "docs/laudo_B2.4_sujetos.md"}
{"evento": "nota", "id": "BKL-0018", "ts": "<FECHA_FIRMA>", "nota": "laudo B2.4: límite declarado junto con BKL-0004, que persiste como falla conocida sellada en la suite r2b (suite_perfil_r2.md:18); no se corrige en esta versión; queda en triaged", "evidencia": "docs/laudo_B2.4_sujetos.md"}
{"evento": "nota", "id": "BKL-0020", "ts": "<FECHA_FIRMA>", "nota": "laudo B2.4: cuarentena declarada (1 fila en r2b, «una entidad originante», cap::3.1.3::cierre, por debajo del umbral de la enmienda 4); queda en triaged", "evidencia": "docs/laudo_B2.4_sujetos.md"}
{"evento": "cambio_estado", "id": "BKL-0028", "estado": "verificado", "aplicado_en": "data/experiment/catalogo_unico/catalogo_sujetos_r2.json (bd2122d)", "ts": "<FECHA_FIRMA>", "nota": "laudo B2.4 (decisión de la autora del 07/10/2026): la condición de cierre se cumple en el catálogo r2 (0 ids domésticos con alias del exterior; tres ids del exterior separados); la adjudicación del miembro de Sujeto_rol_alcance_ctacor (miembros_ids vacío) va a la release siguiente, fila F12", "evidencia": "docs/laudo_B2.4_sujetos.md"}
{"evento": "nota", "id": "BKL-0021", "ts": "<FECHA_FIRMA>", "nota": "laudo B2.4: la mención reaparece en r2b como «la entidad nominada» (control q de T3); cuarentena declarada, con el rol nuevo por el procedimiento de crecimiento de la enmienda 4 al cierre de la tanda 1; reemplaza la decisión (c) del 06/10/2026, que ninguna unidad ejecutó; las 4 filas «entidad(es) encargada(s) del seguimiento» (ext::4.4::intro, ext::4.4.2, ext::10.8, ext::11.1.5::intro) designan el mismo sujeto que ext::11.1.1.10 y entran en su clave (5 unidades); la entidad nominada por el exportador (ext::3.18.2::intro, ext::7.3::intro, ext::7.3.7) es otro sujeto, y Sujeto_propuesto_la_entidad_nominada, que junta las dos, se separa al crear el rol; queda en triaged", "evidencia": "docs/laudo_B2.4_sujetos.md"}
```

## 6. Contradicciones de la ficha de la mesa, corregidas en este asiento

1. **«R2-1 está en `c98093a`»: no está en ningún documento del repo.** El repo cita `c98093a` como R1, que es correcto (la tabla de
   reprocesamiento, `:139`; la enmienda 4, `:28`; el mandato de U-RERESOL-CAT, `:187`), y R2-1 y R2-1 bis en `0737497`. La atribución
   errónea estaba en el pedido de la mesa al agente que juntó los hechos: es un error propio de la mesa, sin nada que corregir en el repo.
2. **Anclas corridas a la fila B2.4.** `plan:380` pasa a `:383` en el checklist (línea de las condiciones y fila X9), en
   `docs/tablero.md:324`, en `data/backlog/clasificacion_backlog_2026-10-04.md` (con una nota fechada al pie) y en `plan:403`. `:376` pasa
   a `:379`.
3. **Los conteos de la fila B2.4** (15, 16 y 17). Los 15 del título eran las entradas `triaged` de entonces, y suman 2 + 2 + 8 + 1 + 2 = 15:
   - BKL-0001 y 0002 (ausencias);
   - BKL-0008 y 0022 (alcanzabilidad, a A1.8 y U-NAV-DISENO);
   - BKL-0009 a 0016 (ocho de asignación de sujeto);
   - BKL-0018;
   - BKL-0020 y 0021 (sujetos de cuarentena sin padre).

   El «17» de `:379` suma BKL-0024 y 0025, ausencias resueltas por el pipeline que no entran a este laudo. Nota fechada en la fila del plan.
4. **BKL-0021:** la condición de cierre falló (la mención reaparece), y ni el plan ni el backlog lo registraban. Queda en la nota de la
   fila del plan y en el lote de eventos.
5. **BKL-0021 y BKL-0028 se pasaron a U-RERESOL-CAT, que no los tomó.** BKL-0021 queda resuelta por la decisión de este laudo, que
   reemplaza la (c) del 06/10. **BKL-0028** entra a este laudo (decisión de la autora del 07/10/2026, noche), con la recomendación de la
   mesa del §3, que la autora adoptó el 07/10/2026 (noche).
6. **«Re-sellado del grafo evaluado de la tanda 0»** (mandato de U-RERESOL-CAT, nota del 07/10, `:325`) contra los nombres D13, que
   reservan «el grafo evaluado» para el escalado (`docs/protocolo_dos_grafos.md`, §1, FIRMADO el 07/10/2026). Se agrega al pie de ese
   mandato la nota de equivalencia que el protocolo prescribe: donde dice «grafo evaluado de la tanda 0», léase «grafo sin cola de la
   tanda 0».

## Firma

PENDIENTE de la firma de la autora (versión para firmar del 09/10/2026, con las lecturas del §4 hechas y decididas).
