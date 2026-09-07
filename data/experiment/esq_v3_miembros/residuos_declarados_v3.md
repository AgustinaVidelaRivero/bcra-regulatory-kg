# U-ESQ-V3 — RESIDUOS DECLARADOS

Lo que el recurso **no** afirma, y por qué. El principio §1 del laudo del esquema congelado acepta la omisión con residuo declarado y manda retirar la falsedad; esto es el registro de las omisiones que esa regla produjo.

**26** colectivos sin id en el catálogo · **7** filas rechazadas por aplanamiento · **2** candidatos de nivel instancia rechazados · **1** enumeración parcial aceptada con su faltante.

## 1. Los 26 colectivos que el pasaje nombra y el catálogo v3 no tiene

El matcheo no sube al padre: hacerlo sería colapsar a la madre. **Remedio: abrir id, que es re-sello del prefijo v3 y unidad propia.**

| # | TO | colectivo |
|---:|---|---|
| 1 | autenf | Personas que ejercen cargos de administración, fiscalización o gerencia en entidades financieras |
| 2 | cryl | Mercados de Valores del país |
| 3 | cryl | Centrales depositarias de valores |
| 4 | depaho | Sociedades de ahorro y préstamo para la vivienda u otros inmuebles |
| 5 | fabcra | Cajas de valores |
| 6 | fabcra | Mercados |
| 7 | fabcra | Agentes de liquidación y compensación |
| 8 | fabcra | ANSES |
| 9 | icmecma | Administradores de carteras crediticias de ex-entidades financieras |
| 10 | icmecma | Otros proveedores no financieros de crédito |
| 11 | ordcom | Destinatarios de Comunicaciones (entidades financieras, cajas de crédito cooperativas, etc.) |
| 12 | osapsa | Empresas no financieras emisoras de tarjetas (Secciones 3 y 5) |
| 13 | osapsa | Operadores de cambio y empresas de cobranzas extrabancarias (Sección 5) |
| 14 | pfmipyme | Plataformas para el financiamiento MiPyME (PFM) |
| 15 | pimf | Infraestructuras del mercado financiero (IMF) nominadas en la Sección 5 |
| 16 | ratiofn | Sucursales o subsidiarias de bancos del exterior G-SIB |
| 17 | repefe | Representantes de entidades financieras del exterior no autorizadas |
| 18 | retype | Banco de la Nación Argentina |
| 19 | retype | Otros bancos públicos participantes (IAF) |
| 20 | rrci | PSP incluidos en el Registro del BCRA |
| 21 | rrci | Infraestructuras del mercado financiero de importancia sistémica |
| 22 | snp_atm | Empresas no financieras operadoras de cajeros automáticos |
| 23 | supcon | Empresas del perímetro de supervisión consolidada |
| 24 | traval | Transportadoras de valores (TV) |
| 25 | traval | Prestadoras de Servicios de Transporte de Valores (PSTV) |
| 26 | traval | Transportadoras de Valores Propias (TVP) |

## 2. Las 7 filas rechazadas por aplanamiento (laudo (a))

Su candidato era la clase madre del colectivo. Adoptarlo habría hecho que el grafo afirme la norma sobre toda la clase y, por la regla 1, sobre cada subclase. **Remedio: una clase más específica en el catálogo.**

| TO | colectivo | clase madre descartada |
|---|---|---|
| adrei | Entidades financieras de importancia sistémica local (D-SIB) | `Sujeto_entidad_financiera` |
| ctacor | Entidades financieras del país | `Sujeto_entidad_financiera` |
| depaho | Bancos comerciales de primer grado | `Sujeto_banco_comercial` |
| pagjub | Entidades financieras participantes del pago de beneficios ANSES | `Sujeto_entidad_financiera` |
| ratiofn | Entidades financieras D-SIB | `Sujeto_entidad_financiera` |
| rdbcra | Personas jurídicas y humanas sometidas al ámbito de la Ley de Entidades Financieras | `Sujeto_persona_juridica` |
| snp_atm | Entidades financieras que ofrezcan cuentas a la vista | `Sujeto_entidad_financiera` |

`ctacor` y `depaho` figuran acá y **no** en la lista de excepciones de S15: conservan otro miembro. Estar en la lista de filas rechazadas y estar en la de excepciones son cosas distintas.

## 3. Los 2 candidatos de nivel instancia rechazados (laudo (b))

`miembro_de` es Clase → Rol. Admitir una instancia cambia la firma del esquema congelado, que es laudo de la autora y jamás efecto de esta unidad. **Costo asumido y declarado: `ordcom` queda sin miembro; `fabcra` sobrevive con los suyos.**

| TO | colectivo | id descartado | nivel |
|---|---|---|---|
| fabcra | Ministerio de Economía | `Sujeto_ministerio_de_economia` | instancia |
| ordcom | BCRA (emisor) | `Sujeto_bcra` | instancia |

## 4. `convca` — la enumeración parcial y lo que le falta

El pasaje (`convca::1.1`) dice «a solicitud de las **entidades financieras y otras habilitadas**». `Sujeto_entidad_financiera` entra como miembro por la lectura llana, laudada. **Lo que falta: las «otras habilitadas», que no tienen id en el catálogo v3.**

### Ambigüedad REGISTRADA, no resuelta en silencio

Bajo el parseo alternativo «(EF y otras) habilitadas» el calificador alcanzaría también a las entidades financieras y volvería a ser aplanamiento. El argumento más fuerte a su favor no es sintáctico sino léxico: el «otras» de «otras habilitadas» presupone que las EF mencionadas antes también están habilitadas, lo que sugiere un conjunto «habilitadas» del que las EF serían una parte. **Se adopta la lectura llana por laudo de la autora, no por resolución de esta unidad**, y se deja escrito porque es el punto que haría cambiar la adjudicación si algún día se relee. Verificado además que el TO no la resuelve: ninguna de sus 13 unidades enumera las «otras habilitadas» ni declara que todas las EF lo estén.

### Chequeo de anidación ordenado antes de escribir este residuo

**Pregunta:** ¿alguna norma del corpus establece que las entidades financieras DEBEN mantener cuenta corriente en el BCRA? De eso depende si el colectivo operativo del TO —«titulares de cuenta corriente en este Banco Central»— contiene al colectivo EF, y por lo tanto si la arista es segura.

El criterio operativo que el propio TO usa no es «entidad financiera» sino ser titular de cuenta corriente en el BCRA:

- `convca::1.1`: «sus cuentas corrientes abiertas en el Banco Central»
- `convca::2.1.3`: «Los titulares de cuentas corrientes en este Banco Central»

**Rama verificada: SÍ EXISTE.** El corpus sí trae esa norma, en `ccbcra::1.1`:

```
Las entidades financieras deberán mantener abierta en el Banco Central de la República Argentina una cuenta corriente en pesos. Dicha cuenta tendrá carácter optativo para las cajas de crédito (Ley 25.782) y las entidades cambiarias.
```

Los conjuntos se anidan y **la arista es segura**: la obligación de mantener cuenta corriente en el BCRA recae sobre las entidades financieras por norma expresa, de modo que el colectivo operativo del TO contiene al colectivo EF. El residuo se escribe entonces como **aproximación con anclaje**: el recurso afirma la norma sobre las entidades financieras, que es un subconjunto veraz del colectivo operativo; lo que no afirma es el resto de ese colectivo.

**Matiz que la propia norma introduce y que no se absorbe:** la misma cláusula dice que la cuenta «tendrá carácter optativo para las cajas de crédito (Ley 25.782) y las entidades cambiarias». Las cajas de crédito de la Ley 25.782 **son** entidades financieras según el catálogo (`Sujeto_caja_de_credito`: «ES la entidad financiera “caja de crédito” de la Ley 25.782»), de modo que la anidación EF ⊆ titulares **no es estricta**: hay un subconjunto de entidades financieras para el que la titularidad es optativa. La arista se mantiene —la regla general es la obligación— pero la excepción queda escrita, y no se afirma «toda EF es titular por construcción», que es la forma de argumento que ya falló en `ctacor`.

