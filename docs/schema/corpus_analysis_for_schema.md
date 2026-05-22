# Análisis del corpus para fundamentar el RFC v0.2 del schema

Material empírico extraído del corpus regulatorio del BCRA al 2026-05-14.

Insumo para el diseño del schema v0.2 (7 entidades core PPF). Cero LLM, todo análisis local con regex/frequency.


**Sample base**:
- 100 Comunicaciones A (random sample sobre 1666 disponibles, max 12 págs/doc)
- 50 Comunicaciones B (random sample sobre 1301 disponibles, max 12 págs/doc)
- 3 Textos Ordenados completos (Clasificación de Deudores, Garantías, Exterior y Cambios)
- Seed determinístico (42), reproducible.

**Caveat aplicado**: NO se usa `titulo_extraido` (caveat #1). Texto extraído directo de PDFs con `pypdf`.

---

## 1. Vocabulario de relaciones entre normas

Frecuencia de verbos y expresiones modificatorias / referenciales en 100 Comunicaciones A muestreadas.
Texto agregado total escaneado: ~897,625 caracteres.

Las categorías están agrupadas por **tipo semántico de relación** que sugieren — útil como punto de partida para definir el conjunto de tipos de relación del schema (ej: `bcra:sustituyeA`, `bcra:incorporaA`, `bcra:complementaA`, `bcra:refiere`, etc.).

### ACCION DISPOSITIVA — Sustituir / reemplazar (modificación in-place)  — total 35 ocurrencias

| Expresión | Ocurrencias |
|---|---:|
| `Reemplazar (infinitivo)` | 26 |
| `Sustituir (infinitivo dispositivo)` | 9 |
| `sustitúyese (forma enclítica)` | 0 |
| `se sustituye (forma reflexiva)` | 0 |

### ACCION DISPOSITIVA — Incorporar / agregar (extensión del corpus)  — total 74 ocurrencias

| Expresión | Ocurrencias |
|---|---:|
| `Incorporar (infinitivo dispositivo)` | 71 |
| `se incorpora` | 3 |
| `Agregar (infinitivo)` | 0 |
| `incorpórase (enclítica)` | 0 |
| `agrégase (enclítica)` | 0 |

### ACCION DISPOSITIVA — Derogar / dejar sin efecto (eliminación)  — total 10 ocurrencias

| Expresión | Ocurrencias |
|---|---:|
| `deja(r/n) sin efecto` | 7 |
| `Eliminar (infinitivo)` | 2 |
| `Derogar (infinitivo)` | 1 |
| `derógase (enclítica)` | 0 |
| `se deroga` | 0 |
| `déjase sin efecto` | 0 |
| `elimínase` | 0 |

### ACCION DISPOSITIVA — Establecer / disponer (creación normativa)  — total 70 ocurrencias

| Expresión | Ocurrencias |
|---|---:|
| `Establecer (infinitivo)` | 37 |
| `Disponer (infinitivo)` | 33 |
| `establécese (enclítica)` | 0 |
| `dispónese (enclítica)` | 0 |

### ACCION DISPOSITIVA — Prorrogar / suspender (efectos temporales)  — total 4 ocurrencias

| Expresión | Ocurrencias |
|---|---:|
| `Prorrogar (infinitivo)` | 2 |
| `se suspende` | 2 |
| `prorrógase (enclítica)` | 0 |
| `se prorroga` | 0 |
| `Suspender (infinitivo)` | 0 |
| `suspéndese (enclítica)` | 0 |

### DERIVADAS REFERENCIALES — modificación, derogación, etc. (mención de cambios pasados)  — total 112 ocurrencias

| Expresión | Ocurrencias |
|---|---:|
| `modificación(es) — sustantivo` | 66 |
| `modificatorio/a(s)` | 27 |
| `incorporación(es)` | 18 |
| `modificado(a/s) por` | 1 |
| `derogación(es)` | 0 |
| `sustitución(es)` | 0 |
| `enmienda(s)` | 0 |

### ACLARAR (interpretación / fe de erratas)  — total 69 ocurrencias

| Expresión | Ocurrencias |
|---|---:|
| `aclaración(es)` | 61 |
| `Aclarar (infinitivo)` | 6 |
| `se aclara` | 2 |
| `aclárase` | 0 |
| `fe de erratas` | 0 |

### COMPLEMENTAR (relación de complementariedad entre normas)  — total 33 ocurrencias

| Expresión | Ocurrencias |
|---|---:|
| `complementario(a/s)` | 31 |
| `complementar(do/n/ndo)` | 2 |
| `complemento(s) de/al/a` | 0 |
| `se complementa` | 0 |

### REFERENCIAS NORMATIVAS (apuntar a otra norma sin modificarla)  — total 469 ocurrencias

| Expresión | Ocurrencias |
|---|---:|
| `previsto(s) en` | 134 |
| `de acuerdo a/con/al` | 90 |
| `conforme a/al/con` | 89 |
| `establecido(s) en` | 64 |
| `lo establecido por/en` | 36 |
| `lo dispuesto por/en` | 35 |
| `en los términos de/del` | 12 |
| `según lo dispuesto` | 5 |
| `contemplado(s) en` | 3 |
| `según lo establecido` | 1 |

### VIGENCIA / APLICACIÓN (efectos temporales)  — total 444 ocurrencias

| Expresión | Ocurrencias |
|---|---:|
| `vigencia (a partir)` | 296 |
| `a partir de(l)` | 123 |
| `será(n) de aplicación` | 15 |
| `entrará(n) en vigencia` | 5 |
| `tendrá(n) vigencia` | 3 |
| `con vigencia desde` | 2 |
| `comenzará(n) a regir` | 0 |
| `será(n) aplicables` | 0 |

---

## 2. Patrones de referencia cruzada (ejemplos textuales)

Cómo las normas citan a otras normas o a fragmentos. Ejemplos concretos extraídos del corpus, con el archivo fuente.
Esto fundamenta el modelado de la **provenance** y de las **referencias entre nodos**.

**[Comunicacion (letra) (numero)]** desde `A8333_ano_de_la_reconstruccion_de_la.pdf`:
> …la Nación Argentina” “Año de la Reconstrucción de la Nación Argentina” . COMUNICACIÓN “A” 8333 22/09/2025 A LAS ENTIDADES FINANCIERAS, A LOS OPERADORES DE CAMBIO: Ref.: Circular CONAU 1-1697: R.I. Contabl…

**[Comunicacion (letra) (numero)]** desde `A7322_2021_ano_de_homenaje_al_premio.pdf`:
> …2021 - AÑO DE HOMENAJE AL PREMIO NOBEL DE MEDICINA DR. CÉSAR MILSTEIN” COMUNICACIÓN “A” 7322 06/07/2021 A LAS ENTIDADES FINANCIERAS: Ref.: Circular RUNOR 1-1682: Presentación de Informaciones al Banco Ce…

**[Comunicacion (letra) (numero)]** desde `A6933_2020_ano_del_general_manuel_be.pdf`:
> …“2020 - AÑO DEL GENERAL MANUEL BELGRANO” COMUNICACIÓN “A” 6933 18/03/2020 A LAS ENTIDADES FINANCIERAS: Ref.: Circular RUNOR 1 - 1534 Horario de atención exclusivo para…

**[Artículo N]** desde `A8333_ano_de_la_reconstruccion_de_la.pdf`:
> …ros anticipados de exportaciones de bienes por operaciones comprendi- das en el artículo 2° del Dto. 38/2025 o Dto. 682/2025” • B30 “Financiaciones del exterior por exportaciones de bienes por operaciones c…

**[Artículo N]** desde `A7322_2021_ano_de_homenaje_al_premio.pdf`:
> …en el Sistema de Circulación Abierta (campo 10 =2). 73.1.2.14. El campo 15 “Artículo 26 inciso 4. Ley Nº 25.326 de Protección de los Datos Personales” – se integrará teniendo en cuenta las siguientes pauta…

**[Decreto/Ley N]** desde `A8333_ano_de_la_reconstruccion_de_la.pdf`:
> …men Informativo de la referencia, como consecuencia de lo dispuesto mediante el Decreto 682/2025. En ese sentido, se restablecen los códigos de concepto que se detallan a continuación: • B28 “Cobros de export…

**[Decreto/Ley N]** desde `A7322_2021_ano_de_homenaje_al_premio.pdf`:
> …lación Abierta (campo 10 =2). 73.1.2.14. El campo 15 “Artículo 26 inciso 4. Ley Nº 25.326 de Protección de los Datos Personales” – se integrará teniendo en cuenta las siguientes pautas:  Se deberán ident…

**[Decreto/Ley N]** desde `A8124_ano_de_la_defensa_de_la_vida_l.pdf`:
> …ancelación anticipada en Unidades de Valor Adquisitivo actualizables por CER - Ley 25.827 (UVA), o el plazo originalmente pactado, en caso de que la entidad sea titular de ese derecho. B.C.R.A. EFECTIVO MÍN…

**[punto X.Y(.Z)...]** desde `A7322_2021_ano_de_homenaje_al_premio.pdf`:
> …aciones 1 CUIT del comprador de la factura (empresa deu- dora) Numérico 11 Punto 73.1.2.1. de estas instrucciones 2 ID FCEM Numérico 13 Punto 73.1.2.2. de estas instrucciones 3 CUIT del emisor del…

**[punto X.Y(.Z)...]** desde `A7227_2021_ano_de_homenaje_al_premio.pdf`:
> …financiaciones desembolsadas a partir del 16.10.2020 inclusive con destino al punto 4.2. “Capital de trabajo y descuento de cheques de pago diferido y de otros documentos” que las entidades financieras pued…

**[punto X.Y(.Z)...]** desde `A8422_2026_ano_de_la_grandeza_argent.pdf`:
> …“- No formular observaciones, en el marco de la restricción contenida en el punto 2.1. del texto ordenado sobre Financiamiento al Sector Público no Financiero, a que las entidades financieras puedan adqu…

**[Sección N]** desde `A7322_2021_ano_de_homenaje_al_premio.pdf`:
> …“A” 7321. Al respecto, les hacemos llegar el Texto Ordenado relativo a la Sección 73. de Presen- tación de informaciones al Banco Central. Por último, se señala que las presentes instrucciones tendrá…

**[Sección N]** desde `A7227_2021_ano_de_homenaje_al_premio.pdf`:
> …a 2 LÍNEA DE FINANCIAMIENTO PARA LA INVERSIÓN PRODUCTIVA DE MiPyME B.C.R.A. Sección 3. Aplicaciones. B.C.R.A. ORIGEN DE LAS DISPOSICIONES CONTENIDAS EN LAS NORMAS SOBRE “LÍNEA DE FINANCIAMI…

**[Sección N]** desde `A6979_2020_ano_del_general_manuel_be.pdf`:
> …PASES, CAUCIONES, OTROS DERIVADOS Y CON FONDOS COMUNES DE INVERSIÓN B.C.R.A. Sección 8. Posición neta diaria en LELIQ. Versión: 4a COMUNICACIÓN “A” 6979 Vigencia: 17/04/2020 Página 1 “OPERACI…

**[Inciso X]** desde `A7322_2021_ano_de_homenaje_al_premio.pdf`:
> …a de Circulación Abierta (campo 10 =2). 73.1.2.14. El campo 15 “Artículo 26 inciso 4. Ley Nº 25.326 de Protección de los Datos Personales” – se integrará teniendo en cuenta las siguientes pautas:  S…

**[normas sobre XXX]** desde `A7227_2021_ano_de_homenaje_al_premio.pdf`:
> …a resolución que, en su parte pertinente, establece: “- Incrementar, en las normas sobre “Línea de financiamiento para la inversión productiva de Mi- PyME”, del 65 % al 100 % de su valor, el cómputo de las financiaciones desembolsadas a partir del 16…

**[normas sobre XXX]** desde `A6979_2020_ano_del_general_manuel_be.pdf`:
> …Establecer, con vigencia 17.4.2020, que las disposiciones del punto 8.2. de las normas sobre “Operaciones al contado a liquidar y a término, pases, cauciones, otros derivados y con fondos comunes de inversión” se computen en términos de posición.”…

**[normas sobre XXX]** desde `A8124_ano_de_la_defensa_de_la_vida_l.pdf`:
> …ones transitorias. Tabla de correlaciones. B.C.R.A. TEXTO ORDENADO DE LAS NORMAS SOBRE EFECTIVO MÍNIMO Versión:36a. COMUNICACIÓN “A” 8124 Vigencia: 02/11/2024 Página 1 1.1. Obligaciones comprendidas. 1.1.1. Concepto…

**[Texto Ordenado de XXX]** desde `A8422_2026_ano_de_la_grandeza_argent.pdf`:
> …lar observaciones, en el marco de la restricción contenida en el punto 2.1. del texto ordenado sobre Financiamiento al Sector Público no Financiero, a que las entidades financieras puedan adquirir Letras del Tesoro a ser emitidas por el municipio de Córdoba –provinc…

**[Texto Ordenado de XXX]** desde `A8124_ano_de_la_defensa_de_la_vida_l.pdf`:
> …Sección 7. Disposiciones transitorias. Tabla de correlaciones. B.C.R.A. TEXTO ORDENADO DE LAS NORMAS SOBRE EFECTIVO MÍNIMO Versión:36a. COMUNICACIÓN “A” 8124 Vigencia: 02/11/2024 Página 1 1.1. Obligaciones comprendidas. 1.1.1. Concepto…

---

## 3. Estructura interna de un Texto Ordenado

Cómo se organiza internamente un TO. Útil para entender la relación **Texto Ordenado ↔ Artículo/Punto** y cómo modelar la jerarquía documental como **provenance** (no como nodos del grafo, según restricción de Lucho).

### Clasificación de Deudores (`TO_clasificacion_deudores_actual.pdf`, 60 páginas)

**Secciones detectadas** (primeras 15 de 15):
- Sección 1. Deudores comprendidos.
- Sección 2. Financiaciones comprendidas.
- Sección 3. Tarea de clasificación.
- Sección 4. Criterios de clasificación.
- Sección 5. Categorías de carteras.
- Sección 6. Clasificación de los deudores de la cartera comercial.
- Sección 7. Clasificación de los deudores de la cartera para consumo o vivienda.
- Sección 8. Informaciones a clientes.
- Sección 9. Bases de observancia de las normas.
- Sección 10. Otros obligados a la observancia de las normas sobre clasificación de deudores.
- Sección 2. F inanciaciones comprendidas.
- Sección 2. Financiaciones comprendidas.
- Sección 3. Tarea de clasificación.
- Sección 6. Clasificación de los deudores de la cartera comercial.
- Sección 7. Clasificación de los deudores de la cartera para consumo o vivienda.

**Numeración de puntos** (sample primeros 30 únicos): `1.1, 1.1.3.2, 1.1.3.3, 1.1.3.4, 1.1.4, 1.1.5, 1.12, 1.2, 1.2.1, 1.2.2, 1.5.5, 10.1, 10.2, 10.2.1, 10.2.2, 10.3, 10.4, 13.7.99, 2.1, 2.1.1, 2.1.2, 2.1.3, 2.1.4, 2.1.5, 2.1.5.1, 2.1.5.2, 2.1.5.3, 2.1.5.4, 2.1.5.5, 2.1.6`

**Excerpt de tabla de contenidos / primeras páginas:**
```
CLASIFICACIÓN DE DEUDORES -Última comunicación incorporada: “A” 8378- Texto ordenado al 19/12/2025 -Índice- Sección 1. Deudores comprendidos. 1.1. Criterio general. 1.2. Criterios especiales de imputación. Sección 2. Financiaciones comprendidas. 2.1. Conceptos incluidos. 2.2. Exclusiones. Sección 3. Tarea de clasificación. 3.1. Procedimientos de análisis de cartera. 3.2. Periodicidad de clasificación. 3.3. Manual de procedimientos de clasificación y previsión. 3.4. Legajo del cliente. 3.5. Responsabilidad de la tarea de clasificación. 3.6. Aprobación de la clasificación. 3.7. Importe de referencia. Sección 4. Criterios de clasificación. 4.1. Niveles de clasificación. 4.2. Criterio básico de clasificación. 4.3. Evaluación de la capacidad de pago. 4.4. Financiaciones cubiertas con garantías preferidas “A”. 4.5. Deudores que no deben ser objeto de clasificación. 4.6. Financiaciones –sin responsabilidad para el cedente– amparadas con seguros de crédito por riesgo comercial y con seguros de riesgo de crédito “con alcance de comprador público”. Sección 5. Categorías de carteras. 5.1. Categorías. Sección 6. Clasificación de los deudores de la cartera comercial. 6.1. Información básica. 6.2. Criterio de clasificación. 6.3. Periodicidad mínima de clasificación. 6.4. Reconsideración obligatoria de la clasificación. 6.5. Niveles de clasificación. 6.6. Recategorización obligatoria. B.C.R.A. TEXTO ORDENADO DE LAS NORMAS SOBRE “CLASIFICACION DE DEUDORES” Versión: 6a. COMUNICACIÓN “A” 6558 Vig encia: 5/9/2018 Página 1 -Índice- Sección 7. Clasificación de los deudores de la cartera para consumo o vivienda. 7.1. Criterio de clasificación. 7.2. Niveles de clasificación. 7.3. Recategorización obligatoria. 7.4. Información a la Superintendencia de Entidades Financieras y Cambiarias sobre incrementos de la cartera irregular. Sección 8. Informaciones a clientes. 8.1. Informaciones a suministrar. Sección 9. Bases de observancia de las normas. 9.1. Base individual. 9.2. Base consolidada. S…
```

**Excerpt de un punto típico (cuerpo normativo):**
```
1.1. Criterio general. 1.2. Criterios especiales de imputación. Sección 2. Financiaciones comprendidas. 2.1. Conceptos incluidos. 2.2. Exclusiones. Sección 3. Tarea de clasificación. 3.1. Procedimientos de análisis de cartera. 3.2. Periodicidad de clasificación. 3.3. Manual de procedimientos de clasificación y previsión. 3.4. Legajo del cliente. 3.5. Responsabilidad de la tarea de clasificación. 3.6. Aprobación de la clasificación. 3.7. Importe de referencia. Sección 4. Criterios de clasificación. 4.1. Niveles de clasificación. 4.2. Criterio básico de clasificación. 4.3. Evaluación de la capacidad de pago. 4.4. Financiaciones cubiertas con garantías preferidas “A”. 4.5. Deudores que no deben ser objeto de clasificación. 4.6. Financiaciones –sin responsabilidad para el cedente– amparadas con seguros de crédito por riesgo comercial y con seguros de riesgo de crédito “con alcance de comprador público”. Sección 5. Categorías de carteras. 5.1. Categorías. Sección 6. Clasificación de los deudores de la cartera comercial. 6.1. Información básica. 6.2. Criterio de clasificación. 6.3. Periodicidad mínima de clasificación. 6.4. Reconsideración obligatoria de la clasificación. 6.5. Niveles de clasificación. 6.6. Recategorización obligatoria. B.C.R.A. TEXTO ORDENADO DE LAS NORMAS SOBRE “CLASIFICACION DE DEUDORES” Versión: 6a. COMUNICACIÓN “A” 6558 Vig encia: 5/9/2018 Página 1 -Índice- Sección 7. Clasificación de los deudores de la cartera para consumo o vivienda. 7.1. Criterio de clasificación. 7.2. Niveles de clasificación. 7.3. Recategorización obligatoria. 7.4. Información a la Superintendencia de Entidades Financieras y Cambiarias sobre incrementos de la cartera irregular. Sección 8. Informaciones a clientes. 8.1. Informaciones a suministra
```

### Garantías (`TO_garantias_actual.pdf`, 25 páginas)

**Secciones detectadas** (primeras 6 de 6):
- Sección 2. Condiciones.
- Sección 3. Cómputo.
- Sección 4. Disposiciones transitorias.
- Sección 1. Clases.
- Sección 1. Clases.
- Sección 3. Cómputo.

**Numeración de puntos** (sample primeros 30 únicos): `1.000, 1.017, 1.1, 1.1.1, 1.1.10, 1.1.10.1, 1.1.10.2, 1.1.11, 1.1.12, 1.1.13, 1.1.14, 1.1.14.1, 1.1.14.2, 1.1.15, 1.1.16, 1.1.2, 1.1.3, 1.1.4, 1.1.5, 1.1.6, 1.1.7, 1.1.8, 1.1.9, 1.2, 1.2.1, 1.2.10, 1.2.11, 1.2.2, 1.2.3, 1.2.3.1`

**Excerpt de tabla de contenidos / primeras páginas:**
```
GARANTÍAS -Última comunicación incorporada: “A” 8135- Texto ordenado al 21/112024 B.C.R.A. TEXTO ORDENADO DE LAS NORMAS SOBRE “GARANTIAS” -Índice- Sección 1. Cl ases. 1.1. Preferidas “A”. 1.2. Preferidas “B”. 1.3. Restantes garantías. 1.4. Importe de referencia. Sección 2. Condiciones. 2.1. Consideración de las garantías preferidas. 2.2. Documentación respaldatoria. Sección 3. Cómputo. 3.1. Márgenes de cobertura. 3.2. Cobertura parcial con garantías preferidas. Sección 4. Disposiciones transitorias. Tabla de correlaciones. Versión: 6a. COMUNICACIÓN “A” 5998 Vigencia: 25/06/2016 Página 1 1.1. Preferidas “A”. Están constituidas por la cesión o caución de derechos respecto de títulos o documentos de cualquier naturaleza que, fehacientemente instrumentadas, aseguren que la entidad podrá dis- poner de los fondos en concepto de cancelación de la obligación contraída por el cliente, sin necesidad de requerir previamente el pago al deudor dado que la efectivización depende de terceros solventes o de la existencia de mercados en los cuales puedan liquidarse directamente los mencionados títulos o documentos, o los efectos que ellos representan, ya sea que el ven- cimiento de ellos coincida o sea posterior al vencimiento del préstamo o de los pagos periódicos comprometidos o que el producido sea aplicado a la cancelación de la deuda o transferido di- rectamente a la entidad a ese fin. Se incluyen en esta categoría, con el carácter de enumeración taxativa, las siguientes: 1.1.1. Garantías constituidas en efectivo, en pesos, o en las siguientes monedas extranjeras: dólares estadounidenses, francos suizos, libras esterlinas, yenes y euros, teniendo en cuenta en forma permanente su valor de cotización. 1.1.2. Garantías constituidas en oro, teniendo en cuenta en forma permanente su valor de coti- zación. 1.1.3. Cauciones de certificados de depósito a plazo fijo emitidos por la propia entidad financie- ra, constituidos en las monedas a que se refiere el punto 1.1.1. 1.1.4. Reembols…
```

**Excerpt de un punto típico (cuerpo normativo):**
```
1.1. Preferidas “A”. 1.2. Preferidas “B”. 1.3. Restantes garantías. 1.4. Importe de referencia. Sección 2. Condiciones. 2.1. Consideración de las garantías preferidas. 2.2. Documentación respaldatoria. Sección 3. Cómputo. 3.1. Márgenes de cobertura. 3.2. Cobertura parcial con garantías preferidas. Sección 4. Disposiciones transitorias. Tabla de correlaciones. Versión: 6a. COMUNICACIÓN “A” 5998 Vigencia: 25/06/2016 Página 1 1.1. Preferidas “A”. Están constituidas por la cesión o caución de derechos respecto de títulos o documentos de cualquier naturaleza que, fehacientemente instrumentadas, aseguren que la entidad podrá dis- poner de los fondos en concepto de cancelación de la obligación contraída por el cliente, sin necesidad de requerir previamente el pago al deudor dado que la efectivización depende de terceros solventes o de la existencia de mercados en los cuales puedan liquidarse directamente los mencionados títulos o documentos, o los efectos que ellos representan, ya sea que el ven- cimiento de ellos coincida o sea posterior al vencimiento del préstamo o de los pagos periódicos comprometidos o que el producido sea aplicado a la cancelación de la deuda o transferido di- rectamente a la entidad a ese fin. Se incluyen en esta categoría, con el carácter de enumeración taxativa, las siguientes: 1.1.1. Garantías constituidas en efectivo, en pesos, o en las siguientes monedas extranjeras: dólares estadounidenses, francos suizos, libras esterlinas, yenes y euros, teniendo en cuenta en forma permanente su valor de cotización. 1.1.2. Garantías constituidas en oro, teniendo en cuenta en forma permanente su valor de coti- zación. 1.1.3. Cauciones de certificados de depósito a plazo fijo emitidos por la propia entidad financie- ra, constituidos
```

### Exterior y Cambios (`TO_exterior_cambios_actual.pdf`, 201 páginas)

**Secciones detectadas** (primeras 15 de 15):
- Sección 1. Disposiciones generales.
- Sección 2. Disposiciones específicas para los ingresos por el mercado de cambios.
- Sección 3. Disposiciones específicas para los egresos por el mercado de cambios.
- Sección 4. Otras disposiciones específicas.
- Sección 5. Pautas operativas.
- Sección 6. Definiciones.
- Sección 7. Cobros de exportaciones de bienes.
- Sección 8. Seguimiento de las negociaciones de divisas por exportaciones de bienes
- Sección 9. Seguimiento de anticipos y otras financiaciones de exportación de bienes.
- Sección 10. Pagos de importaciones y otras compras de bienes en el exterior.
- Sección 11. Sistema de seguimiento de pagos de importaciones (SEPAIMPO).
- Sección 12. Posiciones arancelarias de la NCM con tratamiento específico en las normas de
- Sección 13. Pagos de servicios prestados por no residentes.
- Sección 14. Disposiciones complementarias asociadas al Régimen de Incentivos a las Grandes
- Sección 15. Disposiciones legales que determinan la estructura general del mercado de cambios

**Numeración de puntos** (sample primeros 30 únicos): `00.00, 0202.30.00, 0203.21.00, 0206.29.90, 0207.14.00, 1.001, 1.003, 1.1, 1.2, 1.2.1.1, 1.2.2, 1.2.2.1, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 10.000, 10.1, 10.10, 10.10.1, 10.10.2, 10.10.2.1, 10.10.2.10, 10.10.2.11, 10.10.2.12, 10.10.2.13, 10.10.2.14`

**Excerpt de tabla de contenidos / primeras páginas:**
```
EXTERIOR Y CAMBIOS -Última comunicación incorporada: A 8307- Texto ordenado al 25/08/2025 - Índice - Sección 1. Disposiciones generales. Sección 2. Disposiciones específicas para los ingresos por el mercado de cambios. 2.1. 2.2. 2.3. 2.4. 2.5. 2.6. 2.7. 2.8. 2.9. Cobros de exportaciones de bienes. Cobros de exportaciones de servicios. Enajenación de activos no financieros no producidos. Títulos de deuda suscriptos en el exterior y endeudamientos financieros con el exterior. Títulos de deuda u otros valores representativos de deuda denominados y pagaderos en moneda extranjera en el país. Excepción de liquidación de cobros de exportaciones de bienes y servicios para los beneficiarios del "Régimen de fomento para las exportaciones de la economía del conocimiento”. Otras excepciones a la obligación de liquidación. Canjes y arbitrajes con clientes asociados a ingresos de divisas del exterior. Operaciones comprendidas en el artículo 3° del Decreto 616/05. Sección 3. Disposiciones específicas para los egresos por el mercado de cambios. 3.1. 3.2. 3.3. 3.4. 3.5. 3.6. 3.7. 3.8. 3.9. Pagos de importaciones y otras compras de bienes al exterior. Pagos de servicios prestados por no residentes. Pagos de intereses de deudas por importaciones de bienes y servicios. Pagos de utilidades y dividendos. Pagos de títulos de deuda suscriptos en el exterior y endeudamientos financieros con el exterior. Pagos de títulos de deuda u otros valores representativos de deuda denominados y pagaderos en moneda extranjera en el país y obligaciones en moneda extranjera entre residentes. Pagos de endeudamientos en moneda extranjera de residentes por parte de fideicomisos constituidos en el país para garantizar la atención de los servicios. Compra de moneda extranjera por parte de personas humanas residentes para la formación de activos externos en forma de billetes y/o depósitos. Compra de moneda extranjera por parte de personas humanas residentes para la formación de activos externos bajo otras modal…
```

**Excerpt de un punto típico (cuerpo normativo):**
```
2.9. Cobros de exportaciones de bienes. Cobros de exportaciones de servicios. Enajenación de activos no financieros no producidos. Títulos de deuda suscriptos en el exterior y endeudamientos financieros con el exterior. Títulos de deuda u otros valores representativos de deuda denominados y pagaderos en moneda extranjera en el país. Excepción de liquidación de cobros de exportaciones de bienes y servicios para los beneficiarios del "Régimen de fomento para las exportaciones de la economía del conocimiento”. Otras excepciones a la obligación de liquidación. Canjes y arbitrajes con clientes asociados a ingresos de divisas del exterior. Operaciones comprendidas en el artículo 3° del Decreto 616/05. Sección 3. Disposiciones específicas para los egresos por el mercado de cambios. 3.1. 3.2. 3.3. 3.4. 3.5. 3.6. 3.7. 3.8. 3.9. Pagos de importaciones y otras compras de bienes al exterior. Pagos de servicios prestados por no residentes. Pagos de intereses de deudas por importaciones de bienes y servicios. Pagos de utilidades y dividendos. Pagos de títulos de deuda suscriptos en el exterior y endeudamientos financieros con el exterior. Pagos de títulos de deuda u otros valores representativos de deuda denominados y pagaderos en moneda extranjera en el país y obligaciones en moneda extranjera entre residentes. Pagos de endeudamientos en moneda extranjera de residentes por parte de fideicomisos constituidos en el país para garantizar la atención de los servicios. Compra de moneda extranjera por parte de personas humanas residentes para la formación de activos externos en forma de billetes y/o depósitos. Compra de moneda extranjera por parte de personas humanas residentes para la formación de activos externos bajo otras modalidades, la remisión
```

---

## 4. Restricciones y excepciones reales

Ejemplos textuales de cómo el corpus expresa **Restricciones** (prohibiciones, obligaciones, límites cuantitativos) y **Excepciones** (situaciones donde una restricción no aplica).
Esto fundamenta el modelado de las entidades `Restricción` y `Excepción` del schema.

### 4.1 Restricciones (14 ejemplos)

**[deberá(n) cumplir/observar/etc]** desde `A7322_2021_ano_de_homenaje_al_premio.pdf`:
> …facturas pagas luego del vencimiento, deberán informarse siempre con campo 4 = 1 (impagas). 73.1.2.10. El campo 10 “Causal de rechazo ” se integrará con código 0 (no aplicable) en el caso de facturas pagas al vencimiento (campo 4 = 0). 73.1.2.11. En el campo 11 “Cal emitido” se identif…

**[no podrá(n) / prohibición indirecta]** desde `A7227_2021_ano_de_homenaje_al_premio.pdf`:
> …l exterior. − El importe a imputar no podrá superar el aumento que resulte de considerar el pro- medio de los incrementos en los saldos diarios que se registren entre el 13.11.2020 y el 31.3.21, respecto del saldo registrado al 12.11.2020. En todos los casos se considerarán los…

**[no podrá(n) / prohibición indirecta]** desde `A6979_2020_ano_del_general_manuel_be.pdf`:
> …en Letras de Liquidez del BCRA (LELIQ) no podrá superar lo mayor entre: 8.1.1. Su responsabilidad patrimonial computable (RPC) del mes anterior. 8.1.2. El 100 % del promedio mensual de saldos diarios del total de depósitos en pesos –excluyendo los del sector financiero– y del va…

**[no podrá(n) / prohibición indirecta]** desde `A7919_1983_2023_40_anos_de_democraci.pdf`:
> …a tarjeta. Las entidades financieras no podrán cargar a los comercios adheridos interés ni comisión vincu- lado a los plazos de liquidación señalados, debiendo observar lo previst o en las normas sobre “Determinación de la condición de micro, pequeña o mediana empresa”. Tampoco deberá…

**[deberá(n) cumplir/observar/etc]** desde `A7919_1983_2023_40_anos_de_democraci.pdf`:
> …2023 Página 1 La carga del alias deberá observar procedimientos de autenticación acordes con las normas sobre “Requisitos mínimos para la gestión de los riesgos de tecnología y seguridad de la información asociados a los servicios financieros digitales”. 3.7.2.2. El mantenimiento…

**[como mínimo (umbral)]** desde `A7919_1983_2023_40_anos_de_democraci.pdf`:
> …ente una pantalla de confirmación que, como mínimo, tenga los siguientes datos: tipo de cuenta de destino, CBU/CVU, alias, nombre real del destinatario, número de c uenta, en- tidad financiera o PSPCP de destino, monto de la transacción y CUIT/CUIL/CDI/DNI del receptor. La persona usuari…

**[no podrá(n) / prohibición indirecta]** desde `A6858_2020_ano_del_general_manuel_be.pdf`:
> …iciones señala- das. Esta deducción no podrá superar el 2 % de los conceptos en pesos sujetos a exigencia, en promedio, del mes anterior al de cómputo.” 2. Incorporar, con vigencia a partir del 1.2.2020, como último párrafo del punto 1.5. de las normas sobre “Efectivo mínimo” l…

**[como mínimo (umbral)]** desde `A6858_2020_ano_del_general_manuel_be.pdf`:
> …putan aquellos cajeros automáticos que –como mínimo– permi- tan realizar extracciones de efectivo a los usuarios con independencia de la entidad de la cual sean clientes y de la red administradora de esos equipos y que –en promedio men- sual, computando días hábiles e inhábiles– hayan perm…

**[no se admitirá(n)]** desde `A8288_ano_de_la_reconstruccion_de_la.pdf`:
> …Durante el periodo de indisponibilidad no se admitirán débitos diferentes de los especí- ficamente autorizados. 3.16.4. Régimen informativo. Conforme al procedimiento y pautas que determine la ARCA, l as entidades financieras deberán informar al citado organismo la totalidad de movimien…

**[deberá(n) cumplir/observar/etc]** desde `A8288_ano_de_la_reconstruccion_de_la.pdf`:
> …o del pago de impuest os, el declarante deberá presentar a la entidad el “Vo- lante electrónico de pago” (VEP) que emita el sistema de la ARCA. Una copia del VEP y de las transacciones realizadas se conservarán en el legajo de la cuenta para acredi- tar el cumplimiento de la aplicación de los f…

**[no podrá(n) / prohibición indirecta]** desde `A6916_2020_ano_del_general_manuel_be.pdf`:
> …del citado Programa. Esta deducción no podrá superar el 4 % de los conceptos en pesos sujetos a exigencia, en promedio, del mes anterior al de cómputo. EFECTIVO MÍNIMO B.C.R.A. Sección 1. Exigencia. Versión: 21a. COMUNICACIÓN “A” 6916 Vigencia: 01/03/2020 Página 11…

**[deberá(n) cumplir/observar/etc]** desde `A7635_las_malvinas_son_argentinas.pdf`:
> …apital de nivel uno. Consecuentemente, deberá cumplirse con los requisitos de información sobre las exposicio- nes al riego de crédito a que hace referencia el punto 1.4.1. de las normas sobre “Grandes exposiciones al riesgo de crédito”. Si la exposición al “cliente desconocido” se encuen…

**[no podrá(n) / prohibición indirecta]** desde `A7316_2021_ano_de_homenaje_al_premio.pdf`:
> …de país beneficiario final/ordenante” no podrá integrarse con el código d e Ar- gentina cuando se informe alguno de los siguientes conceptos: Leyenda de error Tipo de operación (campo 5) Conceptos (campo 19) 41 (campo 16 del diseño 2713) A11 o A21 A01 – A05 – A06…

**[deberá(n) cumplir/observar/etc]** desde `A7316_2021_ano_de_homenaje_al_premio.pdf`:
> …mportaciones – Boletos múltiples. Se deberá informar un registro por cada permiso de embarque o despacho a plaza i n- cluido en la concertación de cambio. A esos fines, para los códigos de concepto B01, B06, B14, B15, B17 y P13 en los casos en que existan más de uno involucrados en el mism…

### 4.2 Excepciones (12 ejemplos)

**[con excepción de]** desde `A7322_2021_ano_de_homenaje_al_premio.pdf`:
> …/s incorporado/s en el movimiento alta, con excepción de los campos 1 a 3 o para introducir el dato correspondiente al campo 9. Se inte- grarán obligatoriamente los mismos campos exigibles para un Alta. Se utilizará el código de movimiento 2 “Baja” en campo 5 , para eliminar un re- gistro da…

**[excepto (que / cuando / para)]** desde `A8124_ano_de_la_defensa_de_la_vida_l.pdf`:
> …medida en que sea titular del derecho, excepto para los depósitos con opción de cancelación anticipada en Unidades de Valor Adquisitivo actualizables por CER - Ley 25.827 (UVA), o el plazo originalmente pactado, en caso de que la entidad sea titular de ese derecho. B.C.R.A. EFECTIVO MÍN…

**[con excepción de]** desde `A8124_ano_de_la_defensa_de_la_vida_l.pdf`:
> …/de la seguridad social y especia les –con excepción de los depósitos comprendidos en los puntos 1.3.7., 1.3.10. y 1.3.15.–, otros depósitos y obligaciones a la vista, haberes previsionales a creditados por la ANSES pendientes de efectivización y saldos inmovilizados correspondientes a obl…

**[excepto (que / cuando / para)]** desde `A7919_1983_2023_40_anos_de_democraci.pdf`:
> …e ahorro, cuenta sueldo y especiales” (excepto lo requerido en su ú ltimo párrafo, en relación con la declaración jurada del cliente) y concordantes –puntos 4.1., 4.2. y 4.16.1.–. 5.5.2.2. Habilitar los medios técnicos para que el cliente al momento del enrolamiento de su cuenta a la…

**[salvo (que / cuando / el)]** desde `A8288_ano_de_la_reconstruccion_de_la.pdf`:
> …y depósitos en la entidad financiera, salvo que se trate de una entidad financiera controlante sujeta a su- pervisión consolidada, en cuyo caso la acumulación será sobre base consolidada. Se incluirá en esta categoría a los c itados depósitos hasta el límite establecido en el TO sob…

**[excepto (que / cuando / para)]** desde `A7316_2021_ano_de_homenaje_al_premio.pdf`:
> …operación no se lo completó con ceros, excepto lo e s- tablecido para los códigos B01, B06, B14, B15, B17 y P13 (punto 23.2.1.10. de estas instrucciones). 15 TIPO DE IDENTIFICACIÓN MAL I N- FORMADO Se utilizó en el campo 8 un tipo de identific a- ción no previsto en el punto 23.2.1.…

**[excepto (que / cuando / para)]** desde `A8236_ano_de_la_reconstruccion_de_la.pdf`:
> …entidad financiera por parte del BCRA, excepto que medie un requerimiento judicial, quedarán a disposición de las CEC para completar el ciclo de compensación de las operaciones ingresadas con anterioridad. Cumplido lo descripto, la CEC procederá a transferir el s aldo remanente de la c…

**[salvo (que / cuando / el)]** desde `A6976_2020_ano_del_general_manuel_be.pdf`:
> …país por ellas, sin límites de importe –salvo los que expresamente se convengan por razones de seguridad y/o resulten de restricciones operativas del equipo– ni de cantidad de extracciones, ni distinción alguna entre clientes y no clientes, independientemente del tipo de cuenta a la vis…

**[con excepción de]** desde `A8206_ano_de_la_reconstruccion_de_la.pdf`:
> …re “Proveedores de servicios de pago”, con excepción de lo solicitado en el punto 2.2.2.10. -2- 4. Establecer que toda billetera digital interoperable que desee ofrecer a sus clientes la posibili- dad de generar VQR que sean procesados por determina do administrador QR deberá previa…

**[excepto (que / cuando / para)]** desde `A6783_2019_ano_de_la_exportacion.pdf`:
> …la Sección 1. Instrucciones generales, excepto en aquellos aspectos para los que expresamente se indique otro tratamiento. El cómputo de las partidas componentes de la posición diaria se efectuará sobre los saldos a fin de cada día, que deberán ser consistentes con los registros cont…

**[salvo (que / cuando / el)]** desde `A8057_ano_de_la_defensa_de_la_vida_l.pdf`:
> …o retenido por cua l- quier autoridad, salvo que la retención o deducción de tales impuestos, tasas o gravámenes esté requerida por la ley o disposición aplicable. En tal caso , el DEUDOR pagará los importes adicionales necesarios para que los montos netos que perciba el ACREEDOR (lueg…

**[no obstante (lo anterior)]** desde `A8057_ano_de_la_defensa_de_la_vida_l.pdf`:
> …es previstas en el mencionado artículo. No obstante, en el supuesto de que la cesión implique modificación del domicilio de pago, el nuevo domicilio de pago deberá notificarse en forma fehaciente al DEUDOR en el domicilio constituido. Se cons i- derará medio fehaciente la comunicación del…

---

## 5. Keywords temáticas y validación de las 7 entidades core

Sobre el sample combinado de 100 Com A + 50 Com B (texto normalizado, sin acentos, stopwords removidas, palabras de 5+ chars).

### 5.1 Top 40 unigramas (sustantivos / términos recurrentes)

| # | Término | Ocurrencias |
|---:|---|---:|
| 1 | `financieras` | 522 |
| 2 | `entidades` | 514 |
| 3 | `normas` | 391 |
| 4 | `cuenta` | 359 |
| 5 | `operaciones` | 356 |
| 6 | `plazo` | 317 |
| 7 | `entidad` | 302 |
| 8 | `cuentas` | 302 |
| 9 | `vigencia` | 298 |
| 10 | `depositos` | 297 |
| 11 | `pesos` | 275 |
| 12 | `credito` | 270 |
| 13 | `informacion` | 268 |
| 14 | `servicios` | 268 |
| 15 | `regimen` | 265 |
| 16 | `efectivo` | 260 |
| 17 | `unico` | 256 |
| 18 | `moneda` | 247 |
| 19 | `financieros` | 235 |
| 20 | `minimo` | 226 |
| 21 | `interes` | 216 |
| 22 | `informativo` | 211 |
| 23 | `partir` | 209 |
| 24 | `valor` | 205 |
| 25 | `hasta` | 204 |
| 26 | `tasas` | 203 |
| 27 | `financiaciones` | 199 |
| 28 | `exterior` | 199 |
| 29 | `financiero` | 185 |
| 30 | `fondos` | 180 |
| 31 | `debera` | 177 |
| 32 | `financiera` | 176 |
| 33 | `exigencia` | 176 |
| 34 | `siguiente` | 167 |
| 35 | `titulos` | 167 |
| 36 | `general` | 166 |
| 37 | `total` | 162 |
| 38 | `intereses` | 161 |
| 39 | `estadisticas` | 159 |
| 40 | `sistema` | 158 |

### 5.2 Top 30 bigramas (frases candidatas a tipos de entidad)

| # | Bigrama | Ocurrencias |
|---:|---|---:|
| 1 | `entidades financieras` | 398 |
| 2 | `regimen informativo` | 208 |
| 3 | `efectivo minimo` | 181 |
| 4 | `saludamos atentamente` | 150 |
| 5 | `moneda extranjera` | 131 |
| 6 | `dirigimos comunicarles` | 114 |
| 7 | `texto ordenado` | 104 |
| 8 | `entidad financiera` | 99 |
| 9 | `tasas interes` | 98 |
| 10 | `servicios financieros` | 86 |
| 11 | `gerente principal` | 85 |
| 12 | `series estadisticas` | 79 |
| 13 | `titulos publicos` | 74 |
| 14 | `sector publico` | 73 |
| 15 | `estadisticas monetarias` | 73 |
| 16 | `intereses devengados` | 71 |
| 17 | `informativo contable` | 70 |
| 18 | `financieras circular` | 69 |
| 19 | `presentacion informaciones` | 69 |
| 20 | `exterior cambios` | 67 |
| 21 | `contable mensual` | 65 |
| 22 | `devengados pagar` | 65 |
| 23 | `publico financiero` | 55 |
| 24 | `inversiones plazo` | 55 |
| 25 | `valor adquisitivo` | 55 |
| 26 | `proveedores servicios` | 53 |
| 27 | `normas exterior` | 51 |
| 28 | `comunicarles institucion` | 49 |
| 29 | `llegar hojas` | 49 |
| 30 | `cuenta corriente` | 49 |

### 5.3 Validación de las 7 entidades core de la PPF

Frecuencia de menciones explícitas en el corpus muestreado. **Una entidad mencionada con frecuencia validamos empíricamente**; una entidad casi-ausente puede requerir reconceptualización o renombre.

| Entidad core (PPF) | Ocurrencias | Lectura |
|---|---:|---|
| Comunicación | 534 | ✅ Frecuente — entidad justificada |
| Texto Ordenado | 238 | ✅ Frecuente — entidad justificada |
| Artículo (o Punto X.Y) | 679 | ✅ Frecuente — entidad justificada |
| Entidad Financiera | 495 | ✅ Frecuente — entidad justificada |
| Operación | 433 | ✅ Frecuente — entidad justificada |
| Restricción | 16 | ⚠️ Pocas menciones — puede ser baja densidad o reconceptualizar |
| Excepción | 18 | ⚠️ Pocas menciones — puede ser baja densidad o reconceptualizar |
