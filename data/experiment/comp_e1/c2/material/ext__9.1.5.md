# `ext::9.1.5` — Préstamos financieros con contratos vigentes al 31/08/19 cuyas condiciones prevean

Grupos: omisiones. Estado final en la tanda 0: `completo_ok_directo`.

## Texto

> *heredado:* Sección 9. Seguimiento de anticipos y otras financiaciones de exportación de bienes.
> *heredado:* 9.1. Operaciones comprendidas.
> *propio:* 9.1.5. Préstamos financieros con contratos vigentes al 31/08/19 cuyas condiciones prevean la atención de los servicios mediante la aplicación en el exterior del flujo de fondos de exportaciones y para los cuales el exportador solicite su aplicación a permisos de embarque oficializados a partir del 02/09/19.

## Omisiones leídas en T4 (M2)

con_marca:3 [no normativa; heredado] «9.1. Operaciones comprendidas.»

## Código A

- **op1 Operacion** «Préstamos financieros con contratos vigentes al 31/08/19, servicios atendidos con flujo de exportaciones en el exterior» — Préstamos financieros con contratos vigentes al 31/08/19 cuyas condiciones prevean la atención de los servicios mediante la aplicación en el exterior del flujo de fondos de exportaciones, y para los cuales el exportador solicite su aplicación a permisos de embarque oficializados a partir del 02/09/19. Operación comprendida en el seguimiento de anticipos y otras financiaciones de exportación de bie… · props: `{"tipo": "prestamo_financiero_de_exportacion_comprendido"}` · tramo [exacta]: «Préstamos financieros con contratos vigentes al 31/08/19 cuyas condiciones prevean la atención de los servicios mediante la aplicación en el exterior del flujo de fondos de exportaciones y para los cuales el exportador solicite su aplicación a permisos de embarque oficializados a partir del 02/09/19.»

### A — omisiones de T4 a clasificar

- con_marca:3 → entidades: — | omisiones: —

## Código H

- **op1 Operacion** «Préstamo financiero con contrato vigente al 31/08/19, servicios aplicados en el exterior» — Préstamos financieros con contratos vigentes al 31/08/19 cuyas condiciones prevean la atención de los servicios mediante la aplicación en el exterior del flujo de fondos de exportaciones y para los cuales el exportador solicite su aplicación a permisos de embarque oficializados a partir del 02/09/19. Operación comprendida en el seguimiento de anticipos y otras financiaciones de exportación de bien… · props: `{"tipo": "financiacion"}` · tramo [exacta]: «Préstamos financieros con contratos vigentes al 31/08/19 cuyas condiciones prevean la atención de los servicios mediante la aplicación en el exterior del flujo de fondos de exportaciones y para los cuales el exportador solicite su aplicación a permisos de embarque oficializados a partir del 02/09/19.»

### H — omisiones de T4 a clasificar

- con_marca:3 → entidades: — | omisiones: —

## Código K

- **e1 Operacion** «Préstamos financieros vigentes al 31/08/19 aplicados a exportaciones» — Operación comprendida en el seguimiento de financiaciones de exportación de bienes (Sección 9): préstamos financieros con contratos vigentes al 31/08/19 cuyas condiciones prevean la atención de los servicios mediante la aplicación en el exterior del flujo de fondos de exportaciones, y que el exportador pida aplicar a permisos de embarque oficializados a partir del 02/09/19. · props: `{"tipo": "financiación de exportación de bienes"}` · tramo [exacta]: «Préstamos financieros con contratos vigentes al 31/08/19 cuyas condiciones prevean la atención de los servicios mediante la aplicación en el exterior del flujo de fondos de exportaciones»
- **e2 Condicion** «Contrato vigente al 31/08/19 con aplicación de exportaciones en el exterior» — El contrato del préstamo financiero estaba vigente al 31/08/19 y sus condiciones prevén atender los servicios aplicando en el exterior el flujo de fondos de exportaciones. · tramo [exacta]: «con contratos vigentes al 31/08/19 cuyas condiciones prevean la atención de los servicios mediante la aplicación en el exterior del flujo de fondos de exportaciones»
- **e3 Condicion** «Solicitud del exportador: permisos oficializados desde 02/09/19» — El exportador pide que el préstamo se aplique a permisos de embarque oficializados a partir del 02/09/19. · tramo [exacta]: «para los cuales el exportador solicite su aplicación a permisos de embarque oficializados a partir del 02/09/19»
- R: e2 Condicion —condicion_de→ e1 Operacion
- R: e3 Condicion —condicion_de→ e1 Operacion
- R: Sujeto_exportador (mención «el exportador») —ejecuta→ e1 Operacion

### K — omisiones de T4 a clasificar

- con_marca:3 → entidades: — | omisiones: —

## Código W

- **e1 Operacion** «Préstamos financieros atendidos con exportaciones — seguimiento» — Operación comprendida en el seguimiento de anticipos y otras financiaciones de exportación de bienes: préstamos financieros con contratos vigentes al 31/08/19 cuyas condiciones prevean la atención de los servicios mediante la aplicación en el exterior del flujo de fondos de exportaciones, y para los cuales el exportador solicite su aplicación a permisos de embarque oficializados a partir del 02/09… · props: `{"tipo": "préstamo financiero de exportación"}` · tramo [exacta]: «Préstamos financieros con contratos vigentes al 31/08/19 cuyas condiciones prevean la atención de los servicios mediante la aplicación en el exterior del flujo de fondos de exportaciones»
- **c1 Condicion** «Contrato vigente al 31/08/19 con atención por exportaciones» — El préstamo tiene contrato vigente al 31/08/19 y sus condiciones prevén atender los servicios aplicando en el exterior el flujo de fondos de exportaciones. · tramo [exacta]: «con contratos vigentes al 31/08/19 cuyas condiciones prevean la atención de los servicios mediante la aplicación en el exterior del flujo de fondos de exportaciones»
- **c2 Condicion** «Solicitud de aplicación a permisos desde 02/09/19» — El exportador solicita aplicar el préstamo a permisos de embarque oficializados a partir del 02/09/19. · tramo [exacta]: «el exportador solicite su aplicación a permisos de embarque oficializados a partir del 02/09/19»
- R: c1 Condicion —condicion_de→ e1 Operacion
- R: c2 Condicion —condicion_de→ e1 Operacion
- R: Sujeto_exportador (mención «el exportador») —ejecuta→ e1 Operacion

### W — omisiones de T4 a clasificar

- con_marca:3 → entidades: — | omisiones: —

