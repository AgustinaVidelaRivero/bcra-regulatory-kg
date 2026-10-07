# `ext::8.5.22` — Exportación alcanzada por los beneficios cambiarios del Régimen de Promoción de

Grupos: omisiones. Estado final en la tanda 0: `aceptado_con_residuales`.

## Texto

> *heredado:* Sección 8. Seguimiento de las negociaciones de divisas por exportaciones de bienes
> *heredado:* 8.5. Otras imputaciones admitidas en el cumplimiento del seguimiento.
> *heredado:* La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso de embarque cuando cuente con los elementos que le permitan considerar que la operación se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las condiciones previstas en cada caso. La documentación utilizada para certificar el concepto y monto de las divisas imputado en cada caso deberá quedar archivada en la entidad a disposición del BCRA.
> *propio:* 8.5.22. Exportación alcanzada por los beneficios cambiarios del Régimen de Promoción de Inversión para la Explotación de Hidrocarburos (Decreto 929/13). A pedido de un cliente que posea un proyecto incluido en el Régimen de Promoción de Inversión para la Explotación de Hidrocarburos establecido por el Decreto 929/13, la entidad podrá considerar cumplimentado el seguimiento de un permiso de embarque por la parte del permiso que se encuentre amparado por un "Certificado DECRETO 929/13" emitido a partir de lo dispuesto por la Resolución 26/23 de la Secretaría de Energía.

## Omisiones leídas en T4 (M2)

con_marca:27 [normativa; heredado] «La documentación utilizada para certificar el concepto y monto de las divisas imputado en cada caso deberá quedar archivada en la entidad a disposición del BCRA»

## Código A

- **p1 Potestad** «Considerar cumplimentado seguimiento — certificado Decreto 929/13» — La entidad podrá considerar cumplimentado el seguimiento de un permiso de embarque por la parte del permiso amparada por un "Certificado DECRETO 929/13" emitido a partir de la Resolución 26/23 de la Secretaría de Energía, a pedido de un cliente con proyecto incluido en el Régimen de Promoción de Inversión para la Explotación de Hidrocarburos (Decreto 929/13). · tramo [exacta]: «la entidad podrá considerar cumplimentado el seguimiento de un permiso de embarque por la parte del permiso que se encuentre amparado por un "Certificado DECRETO 929/13" emitido a partir de lo dispuesto por la Resolución 26/23 de la Secretaría de Energía»
- **c1 Condicion** «Pedido de cliente con proyecto en régimen Decreto 929/13» — Que el cliente pida la imputación y posea un proyecto incluido en el Régimen de Promoción de Inversión para la Explotación de Hidrocarburos (Decreto 929/13). · tramo [exacta]: «A pedido de un cliente que posea un proyecto incluido en el Régimen de Promoción de Inversión para la Explotación de Hidrocarburos establecido por el Decreto 929/13»
- **d929 Comunicacion** «Decreto 929/13» —  · props: `{"codigo": "Decreto 929/13", "tipo": "externa"}` · tramo [exacta]: «Decreto 929/13»
- **r26 Comunicacion** «Resolución 26/23 Secretaría de Energía» —  · props: `{"codigo": "Resolución 26/23 de la Secretaría de Energía", "tipo": "externa"}` · tramo [exacta]: «Resolución 26/23 de la Secretaría de Energía»
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: p1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: to TextoOrdenado —referencia→ d929 Comunicacion
- R: to TextoOrdenado —referencia→ r26 Comunicacion

### A — omisiones de T4 a clasificar

- con_marca:27 → entidades: — | omisiones: —

## Código H

- **c1 Comunicacion** «Decreto 929/13» —  · props: `{"codigo": "Decreto 929/13", "tipo": "externa"}` · tramo [exacta]: «Decreto 929/13»
- **c2 Comunicacion** «Resolución 26/23 SE» —  · props: `{"codigo": "Resolución 26/23 de la Secretaría de Energía", "tipo": "externa"}` · tramo [exacta]: «Resolución 26/23 de la Secretaría de Energía»
- **p1 Potestad** «Considerar cumplimentado seguimiento — Certificado Decreto 929/13» — A pedido de un cliente con proyecto incluido en el Régimen de Promoción de Inversión para la Explotación de Hidrocarburos (Decreto 929/13), la entidad puede considerar cumplimentado el seguimiento de un permiso de embarque por la parte amparada por un "Certificado DECRETO 929/13" emitido a partir de la Resolución 26/23 de la Secretaría de Energía. · tramo [exacta]: «la entidad podrá considerar cumplimentado el seguimiento de un permiso de embarque por la parte del permiso que se encuentre amparado por un "Certificado DECRETO 929/13" emitido a partir de lo dispuesto por la Resolución 26/23 de la Secretaría de Energía»
- **cond1 Condicion** «Pedido de cliente con proyecto Decreto 929/13» — Que el cliente lo pida y posea un proyecto incluido en el Régimen de Promoción de Inversión para la Explotación de Hidrocarburos (Decreto 929/13). · tramo [exacta]: «A pedido de un cliente que posea un proyecto incluido en el Régimen de Promoción de Inversión para la Explotación de Hidrocarburos establecido por el Decreto 929/13»
- R: cond1 Condicion —condicion_de→ p1 Potestad
- R: to TextoOrdenado —referencia→ c1 Comunicacion
- R: to TextoOrdenado —referencia→ c2 Comunicacion
- R: p1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)

### H — omisiones de T4 a clasificar

- con_marca:27 → entidades: — | omisiones: —

## Código K

- **c1 Comunicacion** «Decreto 929/13» —  · props: `{"codigo": "Decreto 929/13", "tipo": "externa"}` · tramo [exacta]: «Decreto 929/13»
- **c2 Comunicacion** «Resolución 26/23 Secretaría de Energía» —  · props: `{"codigo": "Resolución 26/23 de la Secretaría de Energía", "tipo": "externa"}` · tramo [exacta]: «Resolución 26/23 de la Secretaría de Energía»
- **op1 Operacion** «Cumplimiento seguimiento permiso de embarque — Decreto 929/13» — Considerar cumplimentado el seguimiento de un permiso de embarque por la parte amparada por un Certificado DECRETO 929/13 · props: `{"tipo": "seguimiento de negociación de divisas por exportaciones"}` · tramo [exacta]: «considerar cumplimentado el seguimiento de un permiso de embarque»
- **p1 Potestad** «Imputación por Certificado Decreto 929/13 — seguimiento» — A pedido de un cliente con proyecto incluido en el Régimen de Promoción de Inversión para la Explotación de Hidrocarburos (Decreto 929/13), la entidad podrá considerar cumplimentado el seguimiento de un permiso de embarque por la parte del permiso amparada por un "Certificado DECRETO 929/13" emitido según la Resolución 26/23 de la Secretaría de Energía. · tramo [exacta]: «la entidad podrá considerar cumplimentado el seguimiento de un permiso de embarque por la parte del permiso que se encuentre amparado por un "Certificado DECRETO 929/13"»
- **k1 Condicion** «Pedido de cliente con proyecto Decreto 929/13» — Que lo pida un cliente que posea un proyecto incluido en el Régimen de Promoción de Inversión para la Explotación de Hidrocarburos (Decreto 929/13). · tramo [exacta]: «A pedido de un cliente que posea un proyecto incluido en el Régimen de Promoción de Inversión para la Explotación de Hidrocarburos establecido por el Decreto 929/13»
- **k2 Condicion** «Certificado DECRETO 929/13 según Resolución 26/23» — Parte del permiso amparada por un Certificado DECRETO 929/13 emitido a partir de la Resolución 26/23 de la Secretaría de Energía. · tramo [exacta]: «amparado por un "Certificado DECRETO 929/13" emitido a partir de lo dispuesto por la Resolución 26/23 de la Secretaría de Energía»
- R: to TextoOrdenado —referencia→ c1 Comunicacion
- R: to TextoOrdenado —referencia→ c2 Comunicacion
- R: k1 Condicion —condicion_de→ p1 Potestad
- R: k2 Condicion —condicion_de→ p1 Potestad
- R: p1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)
- R: Sujeto_rol_entidad_autorizada_exterior (mención «la entidad») —ejecuta→ op1 Operacion
- Omisión `relacion_sin_predicado` [exacta]: «la entidad podrá considerar cumplimentado el seguimiento» — Vínculo Potestad → Operacion habilitada; no hay predicado

### K — omisiones de T4 a clasificar

- con_marca:27 → entidades: — | omisiones: —

## Código W

- **c1 Comunicacion** «Decreto 929/13» —  · props: `{"codigo": "Decreto 929/13", "tipo": "externa"}` · tramo [exacta]: «Decreto 929/13»
- **c2 Comunicacion** «Resolución 26/23 Secretaría de Energía» —  · props: `{"codigo": "Resolución 26/23 de la Secretaría de Energía", "tipo": "externa"}` · tramo [exacta]: «Resolución 26/23 de la Secretaría de Energía»
- **p1 Potestad** «Cumplido seguimiento por Certificado Decreto 929/13» — A pedido del cliente, la entidad podrá considerar cumplimentado el seguimiento de un permiso de embarque por la parte amparada por un "Certificado DECRETO 929/13" emitido a partir de la Resolución 26/23 de la Secretaría de Energía. · tramo [exacta]: «la entidad podrá considerar cumplimentado el seguimiento de un permiso de embarque por la parte del permiso que se encuentre amparado por un "Certificado DECRETO 929/13"»
- **k1 Condicion** «Pedido de cliente con proyecto Decreto 929/13» — Que lo pida un cliente con proyecto incluido en el Régimen de Promoción de Inversión para la Explotación de Hidrocarburos (Decreto 929/13). · tramo [exacta]: «A pedido de un cliente que posea un proyecto incluido en el Régimen de Promoción de Inversión para la Explotación de Hidrocarburos establecido por el Decreto 929/13»
- **k2 Condicion** «Certificado emitido según Resolución 26/23» — Solo por la parte del permiso amparada por un Certificado DECRETO 929/13 emitido conforme la Resolución 26/23 de la Secretaría de Energía. · tramo [exacta]: «amparado por un "Certificado DECRETO 929/13" emitido a partir de lo dispuesto por la Resolución 26/23 de la Secretaría de Energía»
- R: to TextoOrdenado —referencia→ c1 Comunicacion
- R: to TextoOrdenado —referencia→ c2 Comunicacion
- R: k1 Condicion —condicion_de→ p1 Potestad
- R: k2 Condicion —condicion_de→ p1 Potestad
- R: p1 Potestad —aplica_a→ Sujeto_rol_entidad_autorizada_exterior (mención «la entidad»)

### W — omisiones de T4 a clasificar

- con_marca:27 → entidades: — | omisiones: —

