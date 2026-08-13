# Registro de generación — EV2, eje de fidelidad (40 preguntas)

Fecha de generación: 2026-08-10. Unidad aislada de generación ciega, heredera
entera del protocolo U6 (`docs/protocolo_u6.md` §4) según `docs/diseno_ev2.md`
§2, §4 y §5. Este registro sigue el precedente declarado en
`docs/diseno_ev2.md` §6 (registro con semillas, rondas y descartes con motivo).

## 1. Aislamiento y fuentes leídas

La instancia generadora leyó EXCLUSIVAMENTE:

- los 5 PDFs de `data/experiment/subset/` (texto extraído con
  `pdftotext -layout`, poppler);
- `data/experiment/exploracion/mapa_territorio_quemado_5TOs_5sets.json`
  (solo anclas de territorio; no contiene contenido del grafo ni preguntas);
- `docs/protocolo_u6.md`, `docs/diseno_ev2.md`,
  `data/experiment/exploracion/validar_anclas.py`.

No se abrió kg.json, nada bajo `sinteticas/`, `posthoc_run/`, el backlog, ni
ningún eval set previo. La generación no vio ningún output del pipeline v2
(gate de `docs/diseno_ev2.md` §6).

## 2. Verificación del corpus (sha256 de los 5 PDFs)

Calculados antes de generar, con
`shasum -a 256 data/experiment/subset/*.pdf`:

```
f6ab71be7783c4192e67c13ee84f1fc585c6ae5e05aa074961c9c59429280bb8  TO_capitales_minimos_actual.pdf
6e7f528d3fea7b756f15e1278eecd828f203f0651fc6f778212033de6a0883e2  TO_clasificacion_deudores_actual.pdf
baea7264918877da132acca5f7ec6df1a3a33fd5be77109b90360a3d586bc130  TO_exterior_cambios_actual.pdf
48564cc714daa9a8c8bbd7115dfe006307ca7cb1c3d78b106c52555fe75a12ec  TO_proteccion_usuarios_servicios_financieros_actual.pdf
754c888ae6034f63eb04991c5cad441435b6bf6f8e8fb3669fd2bb279c3b35d5  TO_regimen_informativo_contable_mensual_actual.pdf
```

Nota de contradicción reportada (regla d del circuito): el mandato pedía
verificar estos hashes "contra el sello del protocolo", pero
`docs/protocolo_u6.md` sella los hashes de los archivos del MAPA (§2), no de
los PDFs; §4 solo exige la verificación byte-idéntica del corpus. Los PDFs
están además gitignoreados (`.gitignore:35`), por lo que no existe sello por
commit contra el cual comparar. Resolución: se registran acá los sha256
calculados como estado del corpus al momento de generar (mismo régimen que
U6 §4: "verificación byte-idéntica del corpus antes de generar").

## 3. Dosificación

Laudada por el mandato, con la proporcionalidad de `docs/diseno_ev2.md` §4:
**ext 16 / cap 8 / cla 6 / ric 5 / pro 5 = 40**.

## 4. Procedimiento y semilla

1. Del mapa de 5 sets se tomó, por TO, la lista de unidades `disponibles`
   (solo numeración + título). Las parcialmente quemadas no se usaron: la
   cuota de cada TO se cubrió íntegramente con unidades enteramente
   disponibles, eliminando el riesgo de caer en subpuntos quemados.
2. Orden de selección de unidades determinístico por semilla:
   `random.Random(f"20260810-{to}").sample(disponibles, len(disponibles))`
   (Python 3; `disponibles` en el orden del mapa). Se tomaron las primeras
   N unidades usables del orden por TO; una unidad descartada por contenido
   se reemplaza por la siguiente del mismo orden.
3. Por unidad seleccionada se leyó su texto en el PDF y se redactó UNA
   pregunta natural de usuario profesional, auto-contenida, sin números de
   punto en el texto de la pregunta; el ancla exacta (TO + punto) vive en el
   gold, junto con 2–5 criterios verificables, cada uno con su cita textual
   del PDF.
4. Cada candidata pasó por `validar_anclas.py` contra
   `mapa_territorio_quemado_5TOs_5sets.json` y por el chequeo verbatim de
   citas (§6).
5. Seis anclas precisan al subpunto pertinente de su unidad semillada:
   ext 4.6→4.6.1, ext 10.6→10.6.2, ext 3.13→3.13.1, cap 5.2→5.2.1,
   cap 8.3→8.3.2, ric S12→12.4. En los seis casos la unidad está
   íntegramente disponible en el mapa, por lo que todo subpunto es
   territorio no quemado.

Observación pre-declarada (EV2F-018): el criterio 1 (definición de producto
básico) excede lo estrictamente elicitado por la pregunta, que apunta a la
medición de la exposición y a las compensaciones admitidas. Si el caso
resulta parcial por ese único criterio, esta observación es la explicación
registrada ex ante.

Órdenes semillados completos por TO (primeras posiciones):

- ext: 6.11, 5.10, 5.3, 2.6, 4.6, 7.7, 13.3, 10.6, **8.6**, 5.7, 6.10, 5.8,
  10.8, 3.17, **3.1**, 13.5, 3.13, 9.5, …
- cap: 5.2, 6.5, 4.2, 2.4, 8.6, 6.11, 8.3, 2.11, …
- cla: 2.1, 3.5, 6.1, 3.1, 4.1, 10.3, …
- ric: 7.2, 9.2, S12, **3.2**, 4.2, 5.2, …
- pro: 1.3, 2.4, 4.4, 2.5, 2.1, …

(en negrita las unidades descartadas en ronda 1, §5).

## 5. Rondas y descartes

**Ronda 1** — 40 unidades candidatas (las primeras del orden semillado por
TO). Descartes: 3, todos por contenido, previos a la validación de anclas:

| Candidata | Motivo del descarte |
|---|---|
| ext 3.1 | Contenido de mera remisión ("se detallan en las Secciones 10. y 11."): sin sustancia normativa propia para 2 criterios verificables. |
| ext 8.6 | Un único enunciado de remisión al régimen informativo: insuficiente para 2 criterios independientes. |
| ric 3.2 | Discrepancia índice/cuerpo del PDF: el índice lista "3.2. Modelo de información" pero en el cuerpo el modelo de la Sección 3 figura como punto 3.1.4 (y 3.1 es unidad parcialmente quemada). Ancla no localizable en el cuerpo sin ambigüedad. |

Verificación a posteriori: las 3 unidades descartadas eran territorialmente
APTAS según `validar_anclas.py` (3/3 apto, `unidad_disponible`) — el descarte
fue exclusivamente de contenido, no de territorio.

**Ronda 2** — 3 reemplazos por la siguiente unidad del orden semillado:
ext 3.1 → 3.13; ext 8.6 → 9.5; ric 3.2 → 5.2. Sin nuevos descartes.

Total: 43 unidades candidatas, 40 aptas usadas, 3 descartadas con motivo.

## 6. Chequeos mecánicos agregados

**Validación de anclas** (`validar_anclas.py` sobre
`mapa_territorio_quemado_5TOs_5sets.json`):

```
-- 40 candidatas: 40 aptas, 0 descartadas
```

Las 40 anclas resuelven a `unidad_disponible` (ninguna cae en unidad parcial).

**Chequeo verbatim de citas** — cada cita de criterio debe aparecer como
substring del texto extraído del PDF de su TO, bajo una de dos
normalizaciones declaradas: (A) colapso de espacios en blanco a un espacio;
(B) des-hifenado de cortes de línea (`-\n` se une) y colapso de espacios.
Resultado:

```
citas verbatim: 164/164
```

Reproducción de ambos chequeos: `build_ev2_fidelidad.py` +
`chequeo_citas_detalle.json` + `validacion_anclas_ev2_fidelidad.json` en el
paquete de revisión de esta unidad.

## 7. Quema

Conforme `docs/protocolo_u6.md` §9 (régimen heredado), las 40 anclas de este
set quedarán QUEMADAS al sellarse EV2 y deberán incorporarse a la próxima
regeneración del mapa de territorio como set adicional (punto exacto +
subpuntos).
