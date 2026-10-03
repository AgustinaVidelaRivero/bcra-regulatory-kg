# U-MED-R2A — FRENO M3: lecturas asistidas pendientes

Contexto:
- M2 está aprobada y commiteada en `c50b094` (`git log`).
- USD 0: ningún script llama a la API, Neo4j no se usa y no se re-extrae nada.
- Las cinco lecturas son **lecturas asistidas**: las hizo la instancia de modelo que ejecuta la unidad, el 03/10/2026, y
  las revisa la autora. La revisión está PENDIENTE: si cambia un veredicto, lo anota en `revision_autora` y la mesa
  registra el resultado final.
- Modelo: Claude Opus 5.5, identificador `claude-opus-5-5`. Lo declara la propia instancia a partir de su contexto de
  sistema; ningún artefacto del repo lo respalda: NO VERIFICADO.

**Reglas fijadas antes de leer.** Están en `data/experiment/medicion_r2a/m3/m3_reglas_lectura.md`, sha256
`84d6a1bebca77f0ace68caad59b311a77cbe45d8c3247f202f955dcf5d7ae3b6`, escrito a las 19:15:29 del 03/10/2026 (`date`),
antes de generar ninguna planilla. El sha es el mismo al cierre. No ajusté ninguna regla durante la lectura.

**Cómo se arma cada lectura:**
- `data/experiment/medicion_r2a/m3_planillas.py` genera la planilla de cada lectura (`m3/planillas/`).
  - Doble corrida idéntica sobre una copia del repo; la salida es igual a la del repo.
  - Las muestras aleatorias se sortean con `random.Random(20261003)` (decisión 10 del mandato).
- La copia de trabajo (`m3/lecturas/`) es la planilla más `veredicto`, las columnas propias de la lectura,
  `justificacion` y `revision_autora` (vacía).
- `data/experiment/medicion_r2a/m3_conteo.py` comprueba cada copia contra su planilla (mismas filas, orden y celdas) y
  cuenta; salida en `m3/m3_conteo.json`, con doble corrida byte a byte idéntica.

## M3.d — Plazos mandados a `frecuencia` (todos, diez TOs)

Población: 250 plazos heredados sin cuantía temporal que el código manda a `frecuencia` (comando [c37]; 213 fuera de la
lista), 161 valores distintos. Aparte, las 8 Obligaciones con `frecuencia` emitida por E1 sin plazo heredado (pedido de
la autora). Población completa: sin intervalo.

| | Frecuencia | Plazo | Otra | Total |
|---|---|---|---|---|
| Plazos heredados | 45 | 38 | 167 | 250 |
| … en la lista | 37 | 0 | 0 | 37 |
| … fuera de la lista | 8 | 38 | 167 | 213 |
| Valores distintos | 19 | 32 | 110 | 161 |
| Frecuencia de E1 sin plazo heredado | 5 | 0 | 3 | 8 |

Fuente: `m3/m3_conteo.json`, claves `m3d.por_grupo`, `plazo_heredado_por_lista` y
`plazo_heredado_valores_distintos_por_veredicto`.

Lectura:
- 205 de los 250 no son una frecuencia.
- Los 37 que caen en la lista son todos frecuencias.
- Fuera de la lista hay 8 frecuencias compuestas (8 filas, 7 valores): «mensual y trimestral», «Trimestral y anual», «al cierre de cada mes»,
  «a fin de cada mes», «Mes siguiente al cierre de cada trimestre», «Por cada período de pago» y «hasta el quinto día
  hábil posterior al vencimiento de cada período de pago».
- Cinco combinan una periodicidad con un límite dentro del período (`mixto` = sí).
- Por TO (frecuencia / plazo / otra):

  | TO | Frecuencia | Plazo | Otra |
  |---|---|---|---|
  | ext | 0 | 8 | 61 |
  | ctacte | 5 | 11 | 30 |
  | cap | 15 | 8 | 26 |
  | ric | 13 | 1 | 3 |
  | pro | 4 | 1 | 15 |
  | cla | 1 | 2 | 14 |
  | lingob | 3 | 0 | 14 |
  | pagjub | 2 | 7 | 2 |
  | polcre | 2 | 0 | 1 |
  | docvig | 0 | 0 | 1 |

  Clave `m3d.plazo_heredado_por_to`.
- «Otra» es sobre todo:
  - momentos atados a un hecho: «previa» (8 filas), «al momento de…», «previo al acceso al mercado de cambios»;
  - rellenos: «N/A», «sin especificar», «permanente»;
  - remisiones: «según régimen…», «conforme a punto…».
- **Dos plazos con cuantía temporal pasaron a `frecuencia`**: «24 hs. hábiles» y «hasta el quinto día hábil posterior
  al vencimiento…». La detección de cuantías (`reglas_comparacion.detectar_cuantias`) no reconoce «hs.» ni el ordinal.
- Las 8 de E1:
  - frecuencia: mensual ×2, diaria, trimestral, «en cada ciclo de clasificación»;
  - otra: «a cada requerimiento del usuario», «cuando corresponda», «según cálculo de capital».

**Desvío declarado (M3.d).**
- El veredicto es por valor: las filas con texto idéntico reciben el mismo.
- Cómo apliqué la regla en los casos de borde, sin cambiarla:
  - «plazo» incluye un límite expresado en unidades de calendario aunque sea relativo a un hecho («el mismo día de la
    aceptación», «tercer mes siguiente a la notificación», «en la fecha de…»);
  - «otra» incluye los momentos sin unidad de calendario («al momento de…», «previo a…»);
  - «regular», «periódicamente» y «regularidad» van a «otra», porque no dicen cada cuánto;
  - «al cierre de operaciones del día» va a «plazo», porque no dice «cada»;
  - «horario: 10 a 15» va a «plazo» (franja horaria para cumplir).
- La regla de `frecuencia` no se toca (decisión 7): la decide la autora con esta medición.

## M3.a — Cambios de destino de las remisiones, de la paráfrasis al texto de E0

Población, recomputada sobre KG-Tanda0-Diez-r2a con las dos variantes de `r3d_remisiones.py` (`C_diez_cambio_de_destino`):
- **750 nodos de origen cambian de destino**; en el sellado eran 732 (clave `m3a_cambios_destino` de
  `m3/planillas/m3_planillas_resumen.json`);
- pares: 863 en ambas variantes, 28 solo por la paráfrasis y 1.323 solo por el texto de E0.

Muestra: 30 nodos.

| sí | no | no decidible | Wilson 95 % para «sí» (sobre 30 y sobre decididos) |
|---|---|---|---|
| 17 | 13 | 0 | 0,392–0,726 |

Clave `m3a` de `m3/m3_conteo.json`.

Los 13 «no» (columna `destino_correcto` de la copia de trabajo):
- **A01** (pro::2.3.1.2): `pro::2.4` se cita para informar un aumento de costos, no para la excepción de las cajas de
  ahorros.
- **A05** (cap::3.1.11.2): `cap::3.1.14` se cita para el parámetro p, no para W de las retitulizaciones.
- **A07** (ctacte::6.5): `ctacte::6.4.3` es de la obligación de informar al BCRA; el nodo es la de las multas.
- **A09** (cap::3.1.14.3): `cap::3.1.14.2` cierra la oración anterior.
- **A11** (ric::3.1.6): da 4.2.1.1 y 4.2.1.2 (CR y EPF) y pierde `cap::2.12`, citado para el ponderador.
- **A13** (ext::13.6): el inciso i) no cita unidades; `ext::10.10.2.1` es de los fletes S30.
- **A14** (cla::6.5.2.2): `cla::6.5.2.1` es de la intención de refinanciar.
- **A15** (ext::10.4.2.6): 10.4.1.2 a 10.4.1.4 y 10.5 son de otro párrafo.
- **A16** (cap::4.3.3.2): `cap::4.2` se cita para la EPF y las EAD, no para la regla de las 5.000 operaciones.
- **A18** (pro::2.3.1.2): `pro::2.4` es de informar costos, no de la adhesión.
- **A19** (ext::9.2): agrega `ext::9.1.8`, que es de la oración siguiente.
- **A20** (ext::7.10.5): `ext::7.10.3` es de la permanencia de los fondos, no del límite del 60 %.
- **A21** (cap::3.1.14): agrega 3.1.14.1 y 3.1.14.4, citados en otros incisos.

Patrón: en los 13, el texto de E0 atribuye al nodo una cita que el punto hace para otra cláusula u otra oración. En A11
y A19, además, falta un destino citado (2.12 y 7.9).

**Informativo, no cambia los veredictos.** Destinos de las aristas `remite_a` de r2a (regla firmada completa) en las
mismas 30 filas, contra los de la variante de texto de E0 (columna `destinos_remite_a_r2a_informativo`):
- de los 17 «sí», 10 tienen los mismos destinos en r2a, 1 pierde uno (A24, `ext::3.5`) y 6 no tienen ninguna `remite_a`
  (A04, A06, A08, A17, A25, A27);
- de los 13 «no», 7 conservan el destino equivocado (A01, A07, A09, A11, A16, A18, A20), 3 no tienen ninguna `remite_a`
  (A05, A14, A15) y 3 quedan reducidos al destino que corresponde o a parte de él (A13, A19, A21).

La regla firmada corrige parte de los errores de atribución y pierde remisiones que el texto cita para el nodo. Es un
hallazgo para A1.8 y para la regla D1, no medido con una muestra propia.

**Desvío declarado (M3.a).**
- La población es la de la variante sin reglas de `r3d` (la clave del mandato), no la de la regla firmada completa de
  r2a.
- Sobre r2a son 750 nodos, no 732 (cifra del sellado).
- La columna de r2a es informativa y no la usé para decidir.

## M3.a′ — Los 35 pares perdidos contra la paráfrasis «sin lectura»

Población: las 35 filas «SIN LECTURA» de `r3_perdidas_remisiones.json`. Comparten una sola cita:
- origen: la Operacion «Transferencia real de activos — titulización»;
- chunk: `cap::3.1.14.4`;
- tramo: «…involucra una transferencia real de activos –en los términos del acápite v) del punto 3.1.14.1.–»;
- destino: los 35 nodos anclados en `cap::3.1.14.1`.

Resultado: **35 pérdidas reales**, 0 «no es pérdida» y 0 «no decidible» (población completa, sin intervalo). La cita es
del contenido del nodo de origen, cuyo texto guardado nombra el acápite v) del 3.1.14.1, y la regla firmada no emite el
par.

Informativo: en KG-Tanda0-Desarrollo-r2a y KG-Tanda0-Diez-r2a el mismo origen (`Operacion_transferencia_real_de_activos_titulizacion_c2537f`)
tiene `remite_a` a 3.1.11, 3.1.14.4, 3.1.2.2 y 3.1.8.2, pero no a 3.1.14.1: la pérdida sigue en r2a.

**Desvío declarado (M3.a′).** Los 35 veredictos son uno solo aplicado a cada par: los pares difieren solo en el nodo de
destino dentro de la misma unidad citada.

## M3.b — Remisiones a puntos inexistentes en la E0 del TO de destino (las 30 de diez)

Población: las 30 citas con causa «punto inexistente en E0» del registro de KG-Tanda0-Diez-r2a. Coinciden, por chunk,
evidencia y destino, con las 30 de `r3d_remisiones.json`, `G_reglas_diez.h_irresolubles.inexistentes`. Población
completa.

| Normativa | Detector | E0 | No decidible |
|---|---|---|---|
| 5 | 18 | 2 | 5 |

- **Detector, 18.** La cita es de otra norma y el detector la resolvió como interna del TO de origen:
  - la cita nombra la norma externa (9): NIIF 9 (B01, B03, B04), «Grandes exposiciones al riesgo de crédito» (B10, B11,
    B12, B16) y la «Reglamentación de la cuenta corriente bancaria», que es otro TO del inventario (B07, B08);
  - el Anexo de la Comunicación A 7914 (4: B13, B14, B15, B17);
  - la norma surge del contexto, sin nombrarla en la cita (5): «Lineamientos para la gestión de riesgos» (B19) y
    «Capitales mínimos» (B21, B22, B29, B30).
- **Normativa, 5.** El punto citado no existe en el texto congelado:
  - B02: cap no tiene punto 3.6; la Sección 3 tiene 3.1 y 3.2;
  - B05 y B06: ctacte 1.3.1 llega a 1.3.1.8;
  - B09: ext 14.5 salta de 14.5.3 a 14.5.7;
  - B20: ric 5.1.2 no tiene subpuntos.
- **E0, 2.** «4.4.3. Riesgo de cambio» y «4.4.4. Riesgo de posiciones en opciones» son encabezados del PDF de ric (p. 18)
  que quedaron dentro del texto de `ric::4.3.3` (B26, B27).
- **No decidible, 5.** B18, B23, B24, B25 y B28 citan ric 4.4, 4.4.1 o 4.4.2. Sus encabezados no aparecen en el texto
  extraído del PDF; como existen 4.4.3 y 4.4.4, probablemente están en páginas sin texto extraíble, pero no lo puedo
  afirmar.

**Desvío declarado (M3.b).**
- La categoría «E0» no está en la lista del mandato. La agregué en las reglas, antes de leer, porque un punto que existe
  y E0 no segmentó no es inconsistencia de la normativa ni error del detector.
- Además del texto de E0, para separar «normativa» de «E0», busqué el número citado en las líneas del PDF del TO
  (`e0_lib.extraer_lineas`, solo lectura), en 11 filas: B05, B06, B09, B18, B20 y B23 a B28.
- Para B21, B22, B29 y B30 consulté si cap tiene las unidades 5.3.2.1, 5.3.2.5, 8.3.2 y 8.3.3 (las tres primeras sí; 8.3.3
  no es unidad, pero tiene subpuntos 8.3.3.x).

## M3.c — Pasada residual de E4 (medida y no aplicada)

Sobre KG-Tanda0-Diez-r2a, la pasada residual tiene **24 propuestos y propone 0 resoluciones**:
- los 24 quedan en cuarentena, con motivo «sin match en catálogo» y sin candidatos (`ens_diez_r2a/r2/e4_pasada_residual_medida.json`);
- no hay ninguna resolución que leer: 0 correctas, 0 incorrectas, 0 dudas.

La copia de trabajo lleva «sin resolución propuesta» en las 24 filas. El veredicto lo asignó el script, después de
comprobar fila por fila que no hay `resuelto_a` ni candidatos. Es el insumo de la decisión 6: en los diez TOs, la pasada
residual no resuelve ningún propuesto que la resolución por relación no haya resuelto.

**Desvío declarado (M3.c).** No hubo lectura. La copia existe para conservar la forma de las cinco lecturas.

## M3.e — Relaciones de la matriz ampliada marcadas como no verificadas por E3

Muestra: 20 por par, sobre 434 (→ Operacion) y 263 (→ Potestad). Regla de U-ESTUDIO-MATRIZ. Es una **señal temprana**:
no reemplaza la lectura de confirmación sobre el grafo de r2b, que E3 ya habrá verificado (plan, unidad 11).

| Par | Correcta | Incorrecta | Duda | Wilson 95 % (sobre decididas) | Wilson 95 % (sobre 20) |
|---|---|---|---|---|---|
| `condicion_de` → Operacion | 16 | 3 | 1 | 0,624–0,945 (16 de 19) | 0,584–0,919 |
| `condicion_de` → Potestad | 17 | 2 | 1 | 0,686–0,971 (17 de 19) | 0,640–0,948 |

Clave `m3e.por_grupo` de `m3/m3_conteo.json`.

Las 5 incorrectas:
- **EO03:** la condición de productores y acopiadores (2.1.3.2) se une a la operación de proveedores de servicios, que
  tiene su propia condición.
- **EO11:** origen y destino dicen lo mismo, como C22 de U-ESTUDIO-MATRIZ.
- **EO16:** una regla de agrupamiento para el cálculo («cada mercado nacional») no es condición del cálculo del riesgo
  vega.
- **EP01:** lo que depende del medio electrónico es la aplicación del 12.10, no la facultad de presentar.
- **EP13:** el requisito de conformidad previa es del acceso de los clientes, no condición de que la entidad precancele
  las líneas.

Las 2 dudas:
- **EO18:** el texto sostiene la condición para la suscripción de 4.6.2, pero el destino es un nodo fusionado
  (procedencias en ext 3.4, 4.4 y 4.6.2) cuya descripción es la de otra modalidad.
- **EP09:** «En el marco de lo dispuesto en los puntos 3.3., 3.5., 3.6. y 10.3.2.» puede ser condición o remisión.

Correctas con un nodo mal tipado, anotadas (3): EO07 (el destino es una regla de cómputo), EO08 (el origen es un tipo de
deuda) y EO09 (el destino es un documento válido).

**Desvío declarado (M3.e).** Para EO18 consulté las procedencias del nodo de destino en el grafo, que no están en la
planilla. Lo hice para entender la duda; el veredicto es «duda» con o sin ese dato.

## Mediciones adicionales

**Regla (i) y la línea «Sección N.»** (pedido de la autora; observación lateral del anexo de U-DIAG-PROCESO, §5,
`93ce4b7`):
- **En KG-Tanda0-Diez-r2a, 2.540 de las 3.801 menciones** que la regla (i) detecta en texto heredado son la línea
  «Sección N.» del encabezado heredado, leída como cita de su propia sección.
- Esas 2.540 están en 2.368 chunks y 86 secciones, todas en `herencia_encabezado`.
- Solo 7 llegan al registro de remisiones (cuando algún nodo del chunk nombra la sección), y las 7 son irresolubles por
  «autorreferencia al punto propio».
- **Ninguna termina en arista `remite_a`.**
- Las otras 1.261 menciones: 1.178 internas y 83 externas.
- En desarrollo: 1.859 de 2.993, también sin aristas.
- Por eso el contador `texto_heredado.menciones` del reporte del ensamblado está inflado por autocitas de encabezado. Las
  2.870 «menciones en texto heredado» de `r2_codigo/reglas_remisiones_postR3.md:102` (otro grafo y otra versión de la
  regla) probablemente lo están también: NO VERIFICADO.

**Unidades sin validación** (hallazgo 6 del FRENO M2): 4 en diez y 3 en desarrollo, las mismas unidades mudas de M10:
- `cap::5.3.2.3`, `ext::6.5.3` y `ric::6.3` en los dos grafos, y `ctacte::5.6.1` solo en diez;
- causa en las cuatro: E1 devolvió un `tool_input` mal formado, y la validación lo rechazó a nivel de chunk con
  `entities_o_relations_invalidos` («entities/relations ausentes o no-lista (ni siquiera como string JSON)»):
  - en `cap::5.3.2.3` falta `relations`;
  - en las otras tres, `entities` viene como texto;
- `stop_reason` es `tool_use` en las cuatro, y ninguna llegó a E3: no están en `finales.jsonl`.

Fuente: `m3/m3_cadena_instrumentada.json`, que sale de `m3_cadena_instrumentada.py`. El script corre la cadena r2 en
memoria y envuelve, solo durante la corrida, tres funciones de módulos importados, sin editarlos. Controles:
- el sha del grafo de la corrida es el versionado (`99fe2bfa…` y `93a7af72…`);
- el total de menciones es el contador del reporte;
- doble corrida idéntica en una copia, y en el repo la misma salida.

## Control del repo y escrito

Regla l:
- `m3_planillas.py` y `m3_cadena_instrumentada.py` corrieron primero sobre una copia del repo (rsync, 0 enlaces), con
  doble corrida, y después en el repo, con la misma salida.
- `m3_conteo.py` (solo lectura) y el armado de las copias de trabajo (`llenar_copia.py`, en el paquete) escribieron
  directo en el repo.
- Comparé el sha256 de todos los archivos del repo al empezar M3 (`sha_repo_antes_planillas_M3.txt`) con el del cierre:
  todo lo que cambió está en `data/experiment/medicion_r2a/`, salvo lo ajeno de la línea siguiente.
- Durante la unidad, otras sesiones cambiaron archivos ajenos a esta unidad, que no toqué:
  - `data/experiment/prompt_r2/`;
  - `docs/mandatos/UPROMPT_R2_prefijo_nuevo.md`;
  - `docs/plan_tesis.md`;
  - `data/backlog/backlog.jsonl`;
  - `docs/enmienda_laudo_B_guarda_ratchet_2026-10-03.md` (nuevo).
- `.pyc`: sin cambios.

Escrito en el repo, todo nuevo dentro de `data/experiment/medicion_r2a/`: `m3_planillas.py`, `m3_conteo.py`,
`m3_cadena_instrumentada.py`, `m3/m3_reglas_lectura.md`, `m3/planillas/` (6 planillas y el resumen), `m3/lecturas/` (6
copias de trabajo), `m3/m3_conteo.json`, `m3/m3_cadena_instrumentada.json` y este documento. El sha256 de cada archivo
está en el paquete de revisión (`archivos_escritos_M3.txt`).

## Pendiente de la autora

- Revisar las cinco lecturas en `revision_autora`.
- Decidir la regla de `frecuencia` (decisión 7), con M3.d.
- Decidir si la pasada residual de E4 se retira del perfil r2 (decisión 6), con M3.c.
- Commit de M3: PENDIENTE.
