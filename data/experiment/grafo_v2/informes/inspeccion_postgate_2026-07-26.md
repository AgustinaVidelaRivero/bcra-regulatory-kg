# Inspección puntual post-gate (2026-07-26) — solo lectura

Tres nodos extraídos verbatim de los kg del piloto. Observaciones fácticas al pie de cada uno; la adjudicación es de la autora.

## (a) haiku r2 — el nodo que disparó "90 días ↔ no vinculada" (13.2)

```json
{
  "id": "Restriccion_para_servicio_no_comprendido_en_los_puntos_13_2_1_a_13_2_5_proporcionado_por_con",
  "type": "Restriccion",
  "label": "Plazo de 90 días para servicios desde contraparte no vinculada",
  "properties": {
    "descripcion": "Para servicio no comprendido en los puntos 13.2.1 a 13.2.5, proporcionado por contraparte no vinculada, el pago se concreta a partir de la fecha de prestación o devengamiento del servicio",
    "tipo": "limite_cuantitativo",
    "umbral": "0 días (inmediato desde prestación)"
  },
  "provenance": {
    "source_doc": "TO_exterior_cambios_actual.pdf",
    "location": "Punto 13.2. Pagos de servicios que fueron o serán prestados o devengados a partir del 13/12/"
  }
}
```

**Observación:** el **label** dice "90 días" y "no vinculada"; la **description** porta el contenido del 13.2.6 (no vinculada + "a partir de la fecha de prestación"), donde el corpus NO fija 90 días — los 90 son de las vinculadas (13.2.7.1). Es estructuralmente el mismo patrón label↔description que la quimera de CQN2-013 (label de un sub-punto con contenido de otro), ahora reproducido por haiku r2 sobre el chunk fresco. El `umbral: "0 días (inmediato desde prestación)"` no es literal del texto. Ambas violaciones mecánicas del score ("90 días ↔ no vinculada" y "a partir de la fecha de prestación ↔ vinculada") salen de este único nodo.

## (b) haiku r2 — el nodo de "Grupo 1 ↔ no comprendidas" (1.4)

```json
{
  "id": "Obligacion_las_entidades_financieras_se_clasificaran_en_grupo_1_entidades_d_sib_y_sucursale",
  "type": "Obligacion",
  "label": "Clasificación de entidades por importancia sistémica",
  "properties": {
    "descripcion": "Las entidades financieras se clasificarán en Grupo 1 (entidades D-SIB y sucursales/subsidiarias G-SIB) y Grupo 2 (entidades no comprendidas en Grupo 1).",
    "tipo": "calculo"
  },
  "provenance": {
    "source_doc": "TO_capitales_minimos_actual.pdf",
    "location": "Punto 1.4. Incumplimientos."
  }
}
```

**Observación:** la description une los DOS grupos en un solo nodo y su emparejamiento interno textual es "Grupo 2 (entidades **no comprendidas** en Grupo 1)" — es decir, el "no comprendidas" está adherido a Grupo 2, no a Grupo 1. La regla mecánica de mismo-nodo disparó por co-ocurrencia de "Grupo 1" y "no comprendidas" en el mismo nodo, sin leer a qué grupo se adhiere el término. El contenido coincide con lo que la key esperaba en `debe_contener` (fila "Sección 2 coalescida: Grupo 1 = D-SIB + ...; Grupo 2 = no comprendidas"). La provenance dice "Punto 1.4." para contenido del territorio de la Sección 2 coalescida — consistente con el artefacto de chunker pre-registrado como no puntuable en la key.

## (c) El nodo-tabla del 12.1 en LAS 6 corridas — emparejamiento interno

El nodo `Obligacion_desde_el_01_06_24_y_hasta_el_31_12_24_...` existe en las 6 corridas con provenance "Punto 12.1..." de CapMin. Descriptions:

- **haiku r1:** "…apliquen las exigencias que surgen de la tabla (**1.500 millones para Bancos, 700 millones para Restantes entidades salvo Cajas de Crédito Cooperativas**)." — label "Aplicar exigencias transitorias de capital", plazo "01/06/24 al 31/12/24".
- **haiku r2:** "…de la siguiente tabla: **Bancos 1.500 millones de pesos; Restantes entidades (salvo Cajas de Crédito Cooperativas) 700 millones de pesos**."
- **sonnet r1:** "…de la siguiente tabla: **Bancos 1.500 …; Restantes entidades (salvo Cajas de Crédito Cooperativas) 700 …**."
- **sonnet r2:** "…de la tabla: **Bancos 1.500 …, Restantes entidades (salvo Cajas de Crédito Cooperativas) 700 …**."
- **opus r1:** "…de la siguiente tabla: **Bancos 1.500 …, Restantes entidades (salvo Cajas de Crédito Cooperativas) 700 …**."
- **opus r2:** ídem opus r1 (sin punto final).

(JSON completo de los 6 en la salida de consola de esta inspección; el de haiku r1 verbatim:)

```json
{
  "id": "Obligacion_desde_el_01_06_24_y_hasta_el_31_12_24_correspondera_que_tales_entidades_en_funci",
  "type": "Obligacion",
  "label": "Aplicar exigencias transitorias de capital",
  "properties": {
    "descripcion": "Desde el 01/06/24 y hasta el 31/12/24 corresponderá que tales entidades en funcionamiento apliquen las exigencias que surgen de la tabla (1.500 millones para Bancos, 700 millones para Restantes entidades salvo Cajas de Crédito Cooperativas).",
    "tipo": "otra",
    "plazo": "01/06/24 al 31/12/24"
  },
  "provenance": {
    "source_doc": "TO_capitales_minimos_actual.pdf",
    "location": "Punto 12.1. Las entidades financieras en funcionamiento al 01/06/24 deberán observar la exig"
  }
}
```

**Observación:** en las 6 corridas el emparejamiento interno del texto corrido es el **correcto** (1.500 adherido a Bancos, 700 adherido a Restantes-salvo-Cajas). Las 2 "violaciones" de emparejamiento que el score reportó en `capitales::12.1` para TODAS las corridas ("700 ↔ Bancos" y "1.500 ↔ restantes") disparan por co-ocurrencia en el mismo nodo — la tabla entera vive en un solo nodo — sin leer la adherencia interna. Mismo patrón de artefacto que (b).

**Lectura transversal para tu adjudicación (fáctica):** de los tres nodos inspeccionados, (a) es una quimera real reproducida (label de un sub-punto con description de otro); (b) y (c) son co-ocurrencias legítimas dentro de un nodo que la regla mecánica de mismo-nodo no puede distinguir de un cruce — el criterio "ambos términos en el MISMO nodo" sobredispara cuando el modelo empaqueta una tabla o una definición doble en un solo nodo con la adherencia correcta.

Sin API, sin commits, solo lectura de `piloto/resultados/`.
