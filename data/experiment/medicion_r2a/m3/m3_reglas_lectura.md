# U-MED-R2A, M3 — reglas de las lecturas asistidas, fijadas antes de leer

Escrito el 03/10/2026, antes de abrir ninguna planilla de lectura. Las reglas no se ajustan después de empezar
(decisión 5 del mandato, `docs/mandatos/UMED_R2A_medicion_r2a.md`). El sha256 de este archivo queda registrado en el
reporte de M3 antes de la primera lectura.

**Lectura asistida.** Las lecturas las hace la instancia de modelo que ejecuta la unidad y las revisa la autora. No son
lectura humana; se rotulan «lectura asistida» en todo artefacto. Modelo declarado por la propia instancia a partir de
su contexto de sistema: Claude Opus 5.5, identificador `claude-opus-5-5` (NO VERIFICADO por un artefacto del repo).

**Reglas comunes.**
- Cada lectura tiene una planilla generada por `data/experiment/medicion_r2a/m3_planillas.py`, que no se edita, y una
  copia de trabajo con las columnas de la planilla más `veredicto`, `justificacion` y `revision_autora` (vacía). La
  copia de trabajo es la única que se escribe a mano.
- Se lee solo lo que trae la planilla: el texto de E0 (propio y heredado) y lo que la planilla copie del grafo. No se
  consultan EV2, otras lecturas ni otros grafos.
- La justificación lleva, en una o dos oraciones, el tramo del texto que sostiene el veredicto.
- Los conteos los hace `data/experiment/medicion_r2a/m3_conteo.py`, de solo lectura, con doble corrida idéntica.
  Intervalo de Wilson al 95 % solo donde la muestra es aleatoria (M3.a y M3.e).

## M3.d — Plazos mandados a `frecuencia` (todos, diez TOs)

Población: las Obligaciones de KG-Tanda0-Diez-r2a con plazo heredado (`campos_heredados_v3.plazo`) sin cuantía temporal
que el llenado en código mandó a `frecuencia` (comando [c37] del tablero; 250 filas). Aparte, con la misma regla: las
Obligaciones con `frecuencia` emitida por E1 y sin plazo heredado (8 filas).

Se lee el valor (el plazo heredado; para las 8, la frecuencia de E1), con la descripción del nodo como contexto solo si
el valor no se entiende solo. Veredicto:
- **frecuencia**: el valor dice cada cuánto se repite la obligación: una periodicidad de calendario (diaria, semanal,
  quincenal, mensual, bimestral, trimestral, semestral, anual, «cada <período>», «por <período>» en sentido
  distributivo, «en forma <periódica>»);
- **plazo**: el valor fija un límite o un momento de calendario para cumplir (una fecha, un día o una parte de un mes,
  el cierre o el vencimiento de un período, «el mes siguiente», «antes del» más una fecha), sin decir cada cuánto se
  repite;
- **otra**: ninguna de las dos: un momento atado a un hecho o a un trámite («inmediata», «al momento de…», «previo
  a…», «en oportunidad de…», «cuando…», «a requerimiento»), una condición («de corresponder»), un relleno («N/A», «no
  aplica», «permanente») o un texto que no es temporal.
- Si el valor combina una periodicidad y un límite dentro del período («mensualmente, hasta el día 10»), el veredicto es
  **frecuencia** y la columna `mixto` lleva «sí».
- Filas con el mismo valor (texto idéntico) reciben el mismo veredicto.

Población completa: sin intervalo.

## M3.a — Cambios de destino de las remisiones, de la paráfrasis al texto de E0

Población: nodos de origen de los cuatro tipos de la cadena r1 (Obligacion, Restriccion, Excepcion, Operacion) cuyo
conjunto de unidades de destino difiere entre la paráfrasis y el texto de E0, con las dos variantes de
`r3d_remisiones.py`, clave `C_diez_cambio_de_destino` (paráfrasis: `fuente = parafrasis`, procedencia primaria,
puntos propios del nodo, sin `termino`; texto de E0: `fuente = e0`, ídem, sin reglas), recomputado sobre
KG-Tanda0-Diez-r2a sin sus aristas `remite_a`. Muestra: 30 nodos, `random.Random(20261003).sample(sorted(población),
30)` (decisión 10 del mandato).

Se lee el texto de E0 del chunk de la procedencia primaria del nodo (propio y heredado), la descripción del nodo y los
dos conjuntos de destinos. Veredicto:
- **sí**: los destinos por el texto de E0 son los que el texto cita para el contenido del nodo: todo destino que solo
  da el texto de E0 está citado en el texto, y ningún destino que solo daba la paráfrasis es una cita del texto que se
  pierde;
- **no**: el texto de E0 falla en algún destino: da uno que el texto no cita para el contenido del nodo, o pierde uno
  que el texto cita y la paráfrasis daba. Se anota en una línea cuál era el correcto;
- **no decidible**: el texto de la planilla no alcanza.

La planilla trae además, como columna informativa, los destinos de las aristas `remite_a` del nodo en r2a (regla
firmada completa); no cambian el veredicto. Wilson al 95 % para «sí», sobre los 30 y sobre los decididos.

## M3.a′ — Los 35 pares perdidos contra la paráfrasis «sin lectura»

Población: las 35 filas con veredicto «SIN LECTURA» de `data/experiment/r2_codigo/r3_perdidas_remisiones.json`,
`B_parafrasis_siete_tipos_desarrollo.filas`. Se lee el texto de E0 del punto (`texto_e0_del_punto`), la evidencia y el
nodo de origen. Veredicto:
- **pérdida real**: el texto cita la unidad de destino para el contenido del nodo de origen, y la regla firmada no
  emite el par;
- **no es pérdida**: el texto no cita esa unidad para el contenido del nodo de origen (la cita es de otro contenido
  del punto, o la paráfrasis la trasladó);
- **no decidible**.

Población completa (no aleatoria): sin intervalo.

## M3.b — Remisiones a puntos inexistentes en la E0 del TO de destino (las 30 de diez)

Población: las citas irresolubles con causa «punto inexistente en E0» del registro de remisiones de
KG-Tanda0-Diez-r2a (`ens_diez_r2a/r2/remisiones_registro.json`), con su chunk de origen y su tramo; se controla
contra `r3d_remisiones.json`, `G_reglas_diez.h_irresolubles.inexistentes`. Se lee el tramo, el texto del chunk de
origen y la lista de unidades de E0 del TO de destino (las vecinas del punto citado), y se busca el número citado en el
texto de E0 de todos los chunks del TO de destino. Veredicto:
- **normativa**: inconsistencia de la propia normativa: el punto citado no existe en el texto congelado o fue
  renumerado (caso `cla::3.3.8`);
- **detector**: error del detector: el punto existe y la cita se leyó mal (otro número, otro TO, una enumeración
  partida);
- **E0**: el punto existe en el texto del TO (aparece como encabezado dentro del texto de otro chunk) pero E0 no lo
  segmentó como unidad. Esta categoría no está en la lista del mandato: la agrego antes de leer, como desvío declarado,
  porque no es inconsistencia de la normativa ni error del detector;
- **no decidible**.

Población completa: sin intervalo.

## M3.c — Pasada residual de E4 (medida y no aplicada)

Población: las resoluciones que propondría la pasada residual sobre KG-Tanda0-Diez-r2a
(`ens_diez_r2a/r2/e4_pasada_residual_medida.json`). Por cada resolución propuesta: **correcta** (el id de catálogo que
asignaría corresponde a la mención del propuesto), **incorrecta** o **duda**. Si no propone ninguna, no hay nada que
leer y se reporta el conteo de propuestos y sus motivos.

## M3.e — Relaciones de la matriz ampliada marcadas como no verificadas por E3

Población: las aristas `condicion_de` con `no_verificada_e3` de KG-Tanda0-Diez-r2a, por par (Condicion → Operacion y
Condicion → Potestad). Muestra: 20 por par, `random.Random(20261003).sample(sorted(aristas del par, por (origen,
destino)), 20)`, cada par con su propio generador (decisión 10 del mandato).

Regla de U-ESTUDIO-MATRIZ (`reports/u_estudio_matriz/lectura/resultado_lectura_matriz.md`, «Protocolo»), sobre el
texto de E0 del chunk de la procedencia de la arista:
- **correcta**: el texto sostiene que la Condicion es condición del destino; si el nodo parece mal tipado pero la
  relación es cierta, cuenta como correcta y se anota;
- **incorrecta**: el texto no sostiene la relación;
- **duda**: el texto no alcanza.

Wilson al 95 % sobre correctas / (correctas + incorrectas), por par. Es una señal temprana, no reemplaza la lectura de
confirmación sobre el grafo de r2b (plan, unidad 11).

## Mediciones adicionales (no son lecturas)

- **Regla (i) y la línea «Sección N.».** Sobre KG-Tanda0-Diez-r2a, de las menciones que la regla (i) detecta en texto
  heredado (contador `texto_heredado.menciones` del reporte del ensamblado), cuántas son la línea «Sección N.» del
  contexto heredado leída como cita de la misma sección: mención con `secciones = [N]`, sin puntos, en un bloque
  heredado cuya unidad de origen es `S<N>` y con la evidencia que empieza con «Sección N». Y cuántas terminan en arista
  `remite_a`. Instrumentación en memoria de la cadena r2, sin editar el pipeline.
- **Unidades sin validación** (4 en diez y 3 en desarrollo, hallazgo 6 del FRENO M2): la causa de cada una, del campo
  `error` de `runner_corpus.entrada_r2`, en la misma corrida instrumentada.
