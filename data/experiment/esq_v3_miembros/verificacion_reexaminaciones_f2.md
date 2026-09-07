# U-ESQ-V3 fase 2 — Verificación independiente de las dos re-examinaciones

El laudo (a) ordena verificar contra los artefactos las dos re-examinaciones **antes de aplicarlas**, y no aplicarlas si no reproducen. Esto es esa verificación.

| caso | tesis del laudo | veredicto |
|---|---|---|
| `ctacor` | «del país» es calificador redundante porque la definición del catálogo es domést… | **NO_REPRODUCE** |
| `convca` | no es aplanamiento sino enumeración parcial: las EF pertenecen al colectivo sin … | **REPRODUCE** |

## ctacor — «Entidades financieras del país» — **NO_REPRODUCE**

**Tesis del laudo:** «del país» es calificador redundante porque la definición del catálogo es doméstica por construcción — reclasificar a `identico`.

**Entrada del catálogo v3 sellado para `Sujeto_entidad_financiera`** (línea completa, con sus alias):

```
Sujeto_entidad_financiera — Entidades financieras (alias: Entidades financieras del exterior, Entidad financiera del exterior, Entidades financieras emisoras de tarjetas de crédito y/o compra, Entidad financiera emisora de tarjetas de crédito y/o compra)
  def: ES el intermediario autorizado por el BCRA a operar bajo la Ley de Entidades Financieras (bancos, compañías financieras, cajas de crédito cooperativas). Quien no tiene esa autorización (aseguradoras, PSP, PNFC, transportadoras de valores) no es entidad financiera.
```

**Pasaje(s) del TO (verbatim de e0_dry, sin editar):**

`ctacor::1.1` · página(s) [3] · «Entidades intervinientes.»

```
1.1. Entidades intervinientes.
Las entidades financieras del país se encuentran facultadas para ofrecer la apertura de
cuentas y la provisión de sus servicios relacionados a otras entidades financieras del país para
la realización de transacciones locales admitidas, a fin de dar curso a las operaciones que
estas últimas efectúen por cuenta de terceros, relativas a: liquidación de cobros y pagos,
gestión de liquidez, de préstamos, recaudación, transferencias y compensación, con
observancia de lo dispuesto por las normas sobre “Política de crédito”.
Estas normas no serán de aplicación respecto de la apertura de cuentas de custodia a
entidades financieras del país y del exterior y para aquellas cuentas a la vista abiertas en
entidades financieras del país por casas de cambio locales y/o por entidades financieras
locales y del exterior, siempre que sean utilizadas exclusivamente para la realización por
cuenta propia de transacciones locales de cobros y pagos.
```

`ctacor::1.4` · página(s) [4] · «Entidades financieras del exterior.»

```
1.4. Entidades financieras del exterior.
Las entidades financieras del país podrán prestar los servicios señalados precedentemente a
entidades financieras del exterior únicamente por intermedio de sus sucursales y subsidiarias
radicadas en el extranjero.
A los efectos de esta reglamentación se considerarán entidades financieras del exterior a
aquellas que, constituidas de acuerdo con el derecho extranjero aplicable, tengan por actividad
permitida desarrollar en las plazas del exterior en que operen, la intermediación habitual entre
la oferta y la demanda de recursos financieros -depósitos del público- en los términos de la Ley
de Entidades Financieras argentina y su reglamentación independientemente del tipo social que
adopten y/o de su carácter público, privado o mixto.
Serán de aplicación los requisitos de apertura, funcionamiento y cierre de cuentas establecidos
en la presente sección para las entidades financieras del país y, adicionalmente, en el punto
2.2. de estas normas.
```

**Verificación:**

- **El ancla del laudo es exacta**: `prompt_v3_b54.py:117` dice literalmente «ES el intermediario AUTORIZADO POR EL BCRA a operar bajo la Ley de Entidades Financieras». La cita se verificó carácter por carácter.
- **Pero la definición no es la única parte de la entrada.** La MISMA línea del catálogo declara, entre sus alias, «Entidades financieras del exterior» y «Entidad financiera del exterior». El catálogo v3 **no tiene id separado para la entidad financiera del exterior**: la manda por alias a este mismo id. Ese es el patrón general del catálogo para lo extranjero — `Sujeto_banco` lleva el alias «Bancos del exterior» y `Sujeto_entidad_cambiaria` el alias «Compañía cambista del exterior». El `Sujeto_banco_central_del_exterior` que el laudo cita como prueba de que lo extranjero tiene id propio es el banco CENTRAL de otro estado, no una entidad financiera del exterior.
- Es decir: en el catálogo v3, `Sujeto_entidad_financiera` es la UNIÓN de las domésticas y las del exterior, y hay contradicción interna entre su `def` (doméstica) y sus `alias` (incluyen lo extranjero). Bajo el uso efectivo —el alias es lo que gobierna a qué id cae una mención—, «del país» es subconjunto PROPIO.
- **Y el propio TO lo confirma, que es la evidencia decisiva.** `ctacor::1.1` no usa «del país» como muletilla: lo contrasta en el mismo párrafo con «entidades financieras del país **y del exterior**», y el documento dedica una unidad entera, `ctacor::1.4`, titulada «Entidades financieras del exterior.». La Sección 1 regula la corresponsalía LOCAL («para la realización de transacciones locales admitidas») y las entidades del exterior se tratan aparte. «Del país» es el recorte que estructura el documento.
- **Consecuencia bajo el criterio del propio laudo (a):** con `Sujeto_entidad_financiera` como miembro, la regla de herencia 2 haría que el grafo afirme que las normas de corresponsalía local alcanzan también a las entidades financieras del exterior — exactamente lo que la Sección 1 excluye. Es el mismo vicio que el laudo manda retirar en las otras seis filas.
- **ctacor NO queda huérfano por esto**: conserva `Sujeto_casa_de_cambio`, que ya tenía por recorte declarado («Casas de cambio (Sección 3)»). Su situación es la de `depaho`: fila rechazada, rol con miembro.

## convca — «Entidades financieras y otras habilitadas a conversión cambiaria» — **REPRODUCE**

**Tesis del laudo:** no es aplanamiento sino enumeración parcial: las EF pertenecen al colectivo sin condición y lo que falta son las «otras», que no tienen id — omisión con residuo declarado.

**Entrada del catálogo v3 sellado para `Sujeto_entidad_financiera`** (línea completa, con sus alias):

```
Sujeto_entidad_financiera — Entidades financieras (alias: Entidades financieras del exterior, Entidad financiera del exterior, Entidades financieras emisoras de tarjetas de crédito y/o compra, Entidad financiera emisora de tarjetas de crédito y/o compra)
  def: ES el intermediario autorizado por el BCRA a operar bajo la Ley de Entidades Financieras (bancos, compañías financieras, cajas de crédito cooperativas). Quien no tiene esa autorización (aseguradoras, PSP, PNFC, transportadoras de valores) no es entidad financiera.
```

**Pasaje(s) del TO (verbatim de e0_dry, sin editar):**

`convca::1.1` · página(s) [3] · «Concepto de conversión cambiaria.»

```
1.1. Concepto de conversión cambiaria.
Son operaciones de conversión cambiaria las que realiza el Banco Central a solicitud de las en-
tidades financieras y otras habilitadas, mediante la emisión y recepción de transferencias de dó-
lares estadounidenses entre sus cuentas corrientes abiertas en el Banco Central y otras cuen-
tas propias o de terceros radicadas en bancos de plaza Nueva York.
```

**Verificación:**

- El pasaje dice literalmente «a solicitud de las **entidades financieras y otras habilitadas**». Bajo la lectura llana son dos colectivos coordinados: las entidades financieras, sin condición alguna, y unas «otras» que el catálogo no tiene. Eso es omisión —falta un miembro— y no falsedad: nada de lo que el grafo afirmaría sería incorrecto. El principio §1 acepta el residuo declarado.
- **AMBIGÜEDAD REGISTRADA, no resuelta en silencio** (por instrucción del laudo). El parseo alternativo «(EF y otras) habilitadas» haría que el calificador alcance también a las EF, y entonces sería aplanamiento. El argumento más fuerte a su favor no es sintáctico sino léxico: el «otras» de «otras habilitadas» presupone que las entidades financieras mencionadas antes también están habilitadas, lo que sugiere un conjunto «habilitadas» del que las EF son una parte. Se deja escrito porque es el punto que haría cambiar la adjudicación si algún día se relee.
- Se adopta la lectura llana **por laudo de la autora**, no por resolución de esta unidad. El residuo («otras habilitadas», sin id) va a la lista de residuos declarados con su texto.

## Recomputo bajo las cuatro combinaciones

Ambos laudos (a) —sin aplanamiento— y (b) —sin instancias— aplicados; los dos rescates como parámetro. Recomputado por este script sobre `candidatos_miembros_v3.json`.

| ctacor rescatado | convca rescatado | aristas `miembro_de` | roles huérfanos |
|---|---|---:|---:|
| SÍ | SÍ | 35 | 12  ← lo que el laudo predice |
| SÍ | NO | 34 | 13 |
| NO | SÍ | 34 | 12  ← **lo que la verificación sostiene** |
| NO | NO | 33 | 13 |

## Resultado verificado y su distancia con el laudo

**34 aristas `miembro_de` · 12 roles huérfanos.**

Los **12 huérfanos y su descomposición por causa (6 / 5 / 1) coinciden exactamente** con lo laudado. La única diferencia es de **una arista**: la de `ctacor`, cuyo rescate no reproduce. El laudo predice 35; la verificación sostiene 34.

| causa | n | roles |
|---|---:|---|
| `sin_id_en_catalogo` | 6 | autenf, pfmipyme, pimf, repefe, retype, traval |
| `aplanamiento_rechazado` | 5 | adrei, pagjub, ratiofn, rdbcra, snp_atm |
| `instancia_rechazada` | 1 | ordcom |
| **total** | **12** | |

Control: la lista de causas reproduce la lista de huérfanos medida — True.

`ctacor` NO figura entre los huérfanos: conserva `Sujeto_casa_de_cambio`. Estar en la lista de filas rechazadas y estar en la de excepciones son cosas distintas, como el propio laudo advierte para `depaho`.
