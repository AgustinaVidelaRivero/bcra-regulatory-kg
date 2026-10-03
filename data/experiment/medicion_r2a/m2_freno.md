# U-MED-R2A — FRENO M2: la columna r2a del tablero de correcciones

Contexto:
- M1 está commiteada por la autora en `f8dedd4` (`git log`).
- Antes de M2, la autora autorizó el 03/10/2026 sellar la entrada r2 de la fixture.
- USD 0: ningún comando llama a la API, Neo4j no se usa y no se re-extrae nada.
- Regla l: todo corrió primero sobre dos copias reales del repo, con el sha256 de todos sus archivos antes y después.

## Sellado de la entrada r2 (antes de M2)

Movimiento:
- En `scripts/regression_kg_esperado.json`, la entrada `KG-Tanda0-Diez-r2a` pasó de `propuesta_r2_sin_sellar` a
  `estado_esperado`, sin cambiar ningún estado: 56 ítems, 33 resuelto, 15 persiste y 8 no_aplicable.
- La clave `propuesta_r2_sin_sellar` ya no existe.
- T6 y E4-b llevan una nota fechada: «persiste» por construcción del test, que espera los 5 TextoOrdenado de
  desarrollo (`scripts/regression_kg.py:1306-1313`), y no por el grafo; la adaptación del test es de la unidad 11.
  E4-b dice además que depende de T6.

| | Antes | Después |
|---|---|---|
| sha256 canónico de `estado_esperado` | `73031656…` | `f8246902cee2fb371546d7cd24ca51c088ceaa815047b16b2b8e254028e53d1f` |
| sha256 del archivo | `3d3f7979…` | `b93c9fbefea52f2103d481bcb88a177be7a4aac9b13da734fa32a4392cd5eaf4` |

Ninguna otra entrada cambia. El sha canónico de cada una es el mismo antes y después:

| Entrada | sha canónico |
|---|---|
| KG-Refinado | `d27c767b…` |
| KG-Reextraido-r1 | `2156cf5f…` |
| KG-Base | `f7bb021c…` |
| KG-Reextraido | `01b7355c…` |
| `linea_de_base_observada` | `83fc4bb6…` |

Tampoco cambian `_rotulo` ni `_convencion`. El script de sellado lo comprueba antes de escribir
(`sellar_entrada_r2.py`, en el paquete).

Control sobre una copia nueva:
- Suite sobre KG-Tanda0-Diez-r2a: 0 regresiones y 56 ítems que coinciden.
- KG-Refinado, KG-Reextraido-r1, KG-Base y KG-Reextraido: 0 regresiones cada uno.

Registrar el sha nuevo de `estado_esperado` en el plan (decisión 4 del mandato) queda PENDIENTE: el plan no está entre
las escrituras de esta unidad.

## Cómo corrió M2

1. **Batería sobre dos copias** (`m2_bateria.sh`; 11:37 a 11:44). En cada copia, en `data/experiment/medicion_r2a/m2/`:
   - la suite del perfil r2 con la fixture sellada sobre los dos grafos r2a [c29];
   - M10 [c30];
   - [c20] sobre la e0-r2;
   - `m2_medicion.py` [c25].

   Resultado:
   - `m2_medicion.json`, M10 y [c20] salen byte a byte iguales en las dos copias;
   - la suite sale igual con la raíz de la copia normalizada (registra rutas absolutas internas);
   - una segunda corrida de `m2_medicion.py` es idéntica.
2. **Producción en el repo** (11:45 a 11:49), con los mismos comandos. Escribió solo los 9 archivos de M2 en
   `data/experiment/medicion_r2a/`. Coinciden con las dos copias: byte a byte, salvo la suite (igual con la raíz
   normalizada).
3. **Recómputo de las celdas.** Antes de escribirlas, recomputé contra `m2_medicion.json` cada cifra de las 26 celdas.
   Escribí el tablero con `escribir_columna_r2a.py` (paquete), que toca solo la columna r2a de :49 a :74 y agrega las
   entradas de comandos; comprueba que el resto del archivo queda idéntico.

Controles: cada medición reproduce, sobre el grafo sellado, el «Valor en la tanda 0» del tablero con la misma regla:

| Medición | Diez | Desarrollo |
|---|---|---|
| Observación (10), aristas de extracción | 13.979 | 10.634 |
| Observación (11), aristas cross-TO y menciones | 186 y 952 | 124 y 783 |
| Condicion aisladas | 42 de 1.383 | 35 de 1.178 |
| Remisiones de `cap::8.2.3.3` a `cap::6.5.1` | 9 | 9 |
| [c11] | 4 / 8 / 0, 13 claves | 4 / 6 / 0, 9 claves |
| [c14] | 323 de 683 | 287 de 606 |
| M10 | 4 de 2.434 | 3 de 1.763 |

En r1, [c14] da 639 / 218 (`prueba_c14.py` del paquete).

## La columna r2a, fila por fila

El texto completo de cada celda está en el tablero. Fuente de todas las cifras: `m2/m2_medicion.json`, salvo donde se
indica otra.

| Fila | Síntoma | r2a |
|---|---|---|
| :49 | Obs. (10) | diez 6,09 (14.820 / 2.434), desarrollo 6,46 (11.383 / 1.763); 5,80 y 6,10 sin las no verificadas por E3 [c26] |
| :50 | Obs. (11) | 969 y 781 aristas `remite_a` entre documentos; 1.547 y 1.382 citas resueltas (otra unidad que la paráfrasis) [c27] |
| :51 | `referencia` por tipo de origen | 5.652 y 5.395 `remite_a` desde Condicion, Definicion o Potestad; 0 `referencia` con origen distinto de TextoOrdenado [c28] |
| :52 | Condiciones aisladas | 0 de 1.409 y 0 de 1.203; 16 y 15 aislados, solo Sujeto y Comunicacion [c3] |
| :53 | Remisiones falsas por paráfrasis | 0 hacia `cap::6.5.1`; las 9 van a `cla::6.5.1` (1) y `cla::7.2.1` (8). Cambio de destino: M3.a |
| :54 | Test del ejemplo | resuelto en los dos; las dos `condicion_de`, marcadas no verificadas por E3 [c29] |
| :55 | Regresiones contra r1 | 46 ítems: 26 / 13 / 7 y 28 / 11 / 7; contra la entrada r2 sellada, 0 regresiones [c29] |
| :56 | Patrón (a) | no medible: exige correr el agente (USD > 0, EV2) |
| :57 | Patrón (b) | no medible: exige correr el agente |
| :58 | Tope de herramientas | no medible: exige correr el agente |
| :59 | Obs. (12) | no medible: la lectura pide decidir antes quién lee (P15, Q12) |
| :60 | Clases A0.2 | no medible: exige correr el agente con juez |
| :61 | Unidades mudas | 4 de 2.434 y 3 de 1.763, igual a la tanda 0 [c30] |
| :62 | `cap::1.2` | sigue invertido; los dos elementos sin verificar; `BKL-0006` y `BKL-0023` persiste; e0-r2 marca y serializa la tabla [c10] |
| :63 | Pérdidas por tablas | las 5 citas siguen ausentes; detección en e0-r2: 4 de 4 ponderadores, 9 de 12 [c31] |
| :64 | Fuera de lista | 0 sin tratar; 4 / 7 / 0 / 217 en diez, todos con marca u original; 0 claves fuera [c32] |
| :65 | Mención y no mapeables | mención: r2b; 60 de 4.086 con mención; registro 48 filas (8 a clase, 40 en cuarentena) [c33] |
| :66 | Catálogo | 0 / 0: el bloque r2 y el catálogo r2, 110 ids [c34] |
| :67 | Cuantías sin campo | 7 de 689 y 2 de 611; límites relativos de S18 aparte (26 y 25) [c35] |
| :68 | Omisiones | r2b; LN-7 no_aplicable |
| :69 | Crudo del reintento | no medible: se cuenta sobre U-REEXT-T0; r2a leyó de la caché los 220 y 168 reintentos |
| :70 | Colisiones de ids | 0 en la e0-r2 de la tanda 0 [c18] |
| :71 | Matriz sin E3 | 697 (434 / 263) y 627 (388 / 239), todas marcadas [c19] |
| :72 | Mayúsculas descartadas | 0 de contenido en e0-r2: conserva las 5 [c36] |
| :73 | Pies en E0 | 0 en e0-r2; la E0 legada sigue con 3 [c22] |
| :74 | Plazos a `frecuencia` | 250, 213 fuera de la lista, por TO; desarrollo 172 y 144 [c37] |

Las seis filas sin valor medido (:56 a :60 y :69) llevan su causa en la celda. Las dos que exigen el prompt nuevo
(:65, la mención, y :68) llevan «r2b».

## Comandos nuevos

Se agregaron 13 comandos y una nota en la sección «Comandos» del tablero:

| Comando | Qué mide |
|---|---|
| [c25] | El script de medición de la columna r2a |
| [c26] | Observación (10) en r2 |
| [c27] | Observación (11) en r2 |
| [c28] | Remisiones por tipo de origen |
| [c29] | Suite con la fixture sellada |
| [c30] | M10 en r2a |
| [c31] | Tablas con R-CITA y R-PRES |
| [c32] | Valores fuera de lista en r2 |
| [c33] | Sujetos en r2a |
| [c34] | Catálogo: bloque contra JSON |
| [c35] | Cuantías en r2 |
| [c36] | Líneas en mayúsculas en e0-r2 |
| [c37] | Plazos a `frecuencia` por TO |

La nota, pedida por la autora, dice que reproducir los sellados exige `--entrada` con ruta absoluta.

## Hallazgos

1. **La regex de [c14] de `reports/u_umbral/u_umbral_u1.py` es la versión anterior** que declara el tablero: no
   admite la cifra entre paréntesis («diez (10) años»).
   - Da 682 en diez, 605 en desarrollo y 638 en r1.
   - La regex escrita tal como dice [c14] reproduce 683, 606 y 639, con los mismos «sin campo»: lo comprobé nodo por
     nodo (`prueba_c14.py` del paquete); la única diferencia es ese nodo.
   - [c35] usa la del tablero.
2. **[c20] no mide la e0-r2.** `r1k_encabezados_descartados.py` mide el descarte de la función de la E0 legada y
   simula una regla.
   - Sobre la e0-r2, las únicas 3 diferencias de la simulación (`ctacte::6.1.2.3`, `ric::11.1.1`, `ric::11.1.4`) son
     los chunks con pie, que la e0-r2 recorta y la simulación no. En la rama de mayúsculas no hay ninguna.
   - Para la fila :72 uso [c36], que compara con las líneas que la e0-r2 conserva (`encabezados_conservados.json`).
3. **Los ids de nodo cambian entre los sellados y r2a.** Los únicos ids de contenido comunes son los de Operacion:
   2.047 en diez (de 8.087 en el sellado y 8.192 en r2a) y 1.555 en desarrollo (`ids_comunes_sellado_r2a.py` del
   paquete). Por eso el cambio de destino de las remisiones no se cuenta por id contra el sellado: lo recomputa M3.a
   sobre r2a.
4. **`cap::1.2` en r2a: la verificación no distingue el monto correcto del invertido.** Los dos elementos quedan con
   `tramo_verificado` = no y `verificado_en_tabla` = false. La marca está, pero no señala cuál está invertido.
5. **«Incumplimientos reiterados» (EV2F-032) está parcial en 5 nodos** (R-CITA). D2 manda leerlos («requiere
   lectura»). No los leí: no está entre las lecturas de esta unidad.
6. **Fila :69: 4 unidades de diez y 3 de desarrollo no tienen validación** (`rechazados` del reporte del ensamblado).
   La causa no está desglosada en el reporte, y no la afirmo.

## Cambios ajenos durante la unidad

Otra sesión (U-PROMPT-R2) modificó o creó archivos mientras corrían mis controles:
- `data/experiment/prompt_r2/p1/*`;
- `docs/mandatos/UPROMPT_R2_prefijo_nuevo.md`;
- `docs/.DS_Store` y `docs/mandatos/.DS_Store`.

Ninguno es de esta unidad. Las corridas de producción escribieron solo en `data/experiment/medicion_r2a/`, en
`scripts/regression_kg_esperado.json` (el sellado) y en `docs/tablero_correcciones.md` (comparación de los sha del repo
antes y después de cada escritura).

## Escrito en el repo (sha256)

| Ruta | sha256 |
|---|---|
| `scripts/regression_kg_esperado.json` (sellado) | `b93c9fbefea52f2103d481bcb88a177be7a4aac9b13da734fa32a4392cd5eaf4` |
| `docs/tablero_correcciones.md` (columna r2a y comandos) | `70875c145601c1cd59ff041aa627a0694ebba18705e68c5efba3537e8b9194d3` |
| `data/experiment/medicion_r2a/m2_medicion.py` | `bac496b57b32d5f46de23a4831f6ad877798be36a473fcbfea90997bf6f2f09b` |
| `data/experiment/medicion_r2a/m2/m2_medicion.json` | `4e35c201f86deba7dfd958fa72e19d9e362f601c82e3561d8787cfd26f0adc0a` |
| `…/m2/suite_diez.json` y `.md` | `97d60696…` y `18331a55…` |
| `…/m2/suite_desarrollo.json` y `.md` | `4b97effb…` y `c1d03e33…` |
| `…/m2/intrinsecas/KG-Tanda0-Diez-r2a.json` | `fdd959a7…` |
| `…/m2/intrinsecas/KG-Tanda0-Desarrollo-r2a.json` | `8f0cdf1f…` |
| `…/m2/r1k_encabezados_descartados_e0r2.json` | `f4e2ff6d…` |
| `data/experiment/medicion_r2a/m2_freno.md` | este documento |

No hay `.pyc` nuevos: 286 entradas antes y después.

## Pendiente de la autora

- Commit del sellado y de M2: PENDIENTE.
- Registrar en el plan el sha nuevo de `estado_esperado` (`f8246902…`), según la decisión 4: PENDIENTE.
- «Seguí» de M3.
