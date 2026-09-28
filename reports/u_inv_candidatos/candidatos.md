# U-INV-CANDIDATOS — candidatos (O, D) de remisión entre puntos, grafo r1

- Grafo: `data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json` sha256 `0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a`
- EV2: `data/experiment/exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json` sha256 `1d58733699c325c90510e1ead5f18eac6c3cd970ee3b0ab7ff141da539162b40`
- E0: `data/experiment/reextraccion_v2/e0_chunking/salida_enm01/chunks_cap.json` sha256 `1931138dac0a107a69a7ff6312400f00465b991d52135457735beeb3e442c825`
- E0: `data/experiment/reextraccion_v2/e0_chunking/salida_enm01/chunks_cla.json` sha256 `98808886a406d8321c678836a55f92eea983d594d95358dd21ceb537487ac0b1`
- E0: `data/experiment/reextraccion_v2/e0_chunking/salida_enm01/chunks_ext.json` sha256 `cbcd1a86f55ea49110610587873881c68c13a9d7975d3fd5e465f26302be2d12`
- E0: `data/experiment/reextraccion_v2/e0_chunking/salida_enm01/chunks_pro.json` sha256 `d8717d1c7423bb5f4d80cc830ff97635ce4d9839f8490b73860ea272568620e2`
- E0: `data/experiment/reextraccion_v2/e0_chunking/salida_enm01/chunks_ric.json` sha256 `fafebb82e07b34191b60022c1c179ea7d2213fd1f5d5f3a408b518c836c94c0d`
- Arista de remisión resuelta: `referencia` con `rol_fuente = referencia_cruzada` (5645 aristas)
- Embudo: 1_arista_resuelta: 439 → 2_tam_D_1a3: 317 → 3_sin_ancestro_descendiente: 295 → 4_palabras_O80_D120: 63 → 5_D_sin_remision_saliente: 42

## Candidatos que pasan los cinco criterios (42)

### C01 — `cap::2.5.3` → {cap::S5}

- Texto Ordenado de O: `cap`
- O = `cap::2.5.3` — 78 palabras
  - fragmento E0 `cap::2.5.3` (punto_terminal; campo `texto`):

````text
2.5.3. Las entidades financieras del grupo 1 deberán asignar a las exposiciones denominadas
en una moneda distinta a la de los ingresos de sus contrapartes –en los casos de expo-
siciones minoristas sin cobertura del riesgo de crédito de la Sección 5. y de exposiciones
con garantía hipotecaria sobre inmuebles residenciales– un ponderador de riesgo del
150% o el que resulte de multiplicar por 1,5 el ponderador que le correspondería según
las presentes disposiciones, el mayor de ambos.
````

- d = `cap::S5` — 97 palabras — mismo Texto Ordenado que O
  - fragmento E0 `cap::S5::chapeau_seccion` (mini_chunk, rol_bloque chapeau_seccion; campo `texto`):

````text
A los efectos del cómputo de la exigencia de capital por riesgo de crédito, se reconocerá –total o
parcialmente– la cobertura del riesgo de crédito (CRC) de las operaciones registradas en la cartera
de inversión –tales como préstamos y responsabilidades eventuales– mediante la utilización de las
técnicas previstas en el punto 5.1.
La presente sección contempla, además, el cálculo de la exposición a las operaciones de financia-
ción con títulos valores (securities financing transactions, SFT) –conforme a lo previsto en la Sec-
ción 4.–, registradas tanto en la cartera de inversión como en la cartera de negociación.
````

  - aristas de remisión resuelta O → d: 5
    - [Restriccion] «Alcance: exposiciones minoristas sin cobertura Sección 5» → [Obligacion] «Calcular exposición SFT conforme Sección 4» (destino `cap::S5`; evidencia «Alcance: exposiciones minoristas sin cobertura Sección 5 | Aplicar a exposic»)
    - [Restriccion] «Alcance: exposiciones minoristas sin cobertura Sección 5» → [Obligacion] «Utilizar técnicas cobertura riesgo crédito punto 5.1» (destino `cap::S5`; evidencia «Alcance: exposiciones minoristas sin cobertura Sección 5 | Aplicar a exposic»)
    - [Restriccion] «Alcance: exposiciones minoristas sin cobertura Sección 5» → [Operacion] «Cálculo exposición operaciones financiación títulos» (destino `cap::S5`; evidencia «Alcance: exposiciones minoristas sin cobertura Sección 5 | Aplicar a exposic»)
    - [Restriccion] «Alcance: exposiciones minoristas sin cobertura Sección 5» → [Operacion] «Cobertura riesgo crédito cartera inversión» (destino `cap::S5`; evidencia «Alcance: exposiciones minoristas sin cobertura Sección 5 | Aplicar a exposic»)
    - [Restriccion] «Alcance: exposiciones minoristas sin cobertura Sección 5» → [Operacion] «Cómputo exigencia capital riesgo crédito» (destino `cap::S5`; evidencia «Alcance: exposiciones minoristas sin cobertura Sección 5 | Aplicar a exposic»)
- Preguntas EV2 que citan O o algún d: ninguna

### C02 — `cap::2.5.11` → {cap::S5}

- Texto Ordenado de O: `cap`
- O = `cap::2.5.11` — 23 palabras
  - fragmento E0 `cap::2.5.11` (punto_terminal; campo `texto`):

````text
2.5.11. A los efectos del reconocimiento de la cobertura del riesgo de crédito, se tendrá en
cuenta lo dispuesto en la Sección 5.
````

- d = `cap::S5` — 97 palabras — mismo Texto Ordenado que O
  - fragmento E0 `cap::S5::chapeau_seccion` (mini_chunk, rol_bloque chapeau_seccion; campo `texto`):

````text
A los efectos del cómputo de la exigencia de capital por riesgo de crédito, se reconocerá –total o
parcialmente– la cobertura del riesgo de crédito (CRC) de las operaciones registradas en la cartera
de inversión –tales como préstamos y responsabilidades eventuales– mediante la utilización de las
técnicas previstas en el punto 5.1.
La presente sección contempla, además, el cálculo de la exposición a las operaciones de financia-
ción con títulos valores (securities financing transactions, SFT) –conforme a lo previsto en la Sec-
ción 4.–, registradas tanto en la cartera de inversión como en la cartera de negociación.
````

  - aristas de remisión resuelta O → d: 5
    - [Obligacion] «Reconocimiento cobertura riesgo crédito según Sección 5» → [Obligacion] «Calcular exposición SFT conforme Sección 4» (destino `cap::S5`; evidencia «Reconocimiento cobertura riesgo crédito según Sección 5 | A los efectos del»)
    - [Obligacion] «Reconocimiento cobertura riesgo crédito según Sección 5» → [Obligacion] «Utilizar técnicas cobertura riesgo crédito punto 5.1» (destino `cap::S5`; evidencia «Reconocimiento cobertura riesgo crédito según Sección 5 | A los efectos del»)
    - [Obligacion] «Reconocimiento cobertura riesgo crédito según Sección 5» → [Operacion] «Cálculo exposición operaciones financiación títulos» (destino `cap::S5`; evidencia «Reconocimiento cobertura riesgo crédito según Sección 5 | A los efectos del»)
    - [Obligacion] «Reconocimiento cobertura riesgo crédito según Sección 5» → [Operacion] «Cobertura riesgo crédito cartera inversión» (destino `cap::S5`; evidencia «Reconocimiento cobertura riesgo crédito según Sección 5 | A los efectos del»)
    - [Obligacion] «Reconocimiento cobertura riesgo crédito según Sección 5» → [Operacion] «Cómputo exigencia capital riesgo crédito» (destino `cap::S5`; evidencia «Reconocimiento cobertura riesgo crédito según Sección 5 | A los efectos del»)
- Preguntas EV2 que citan O o algún d: ninguna

### C03 — `cap::2.11.1` → {cap::2.11.3}

- Texto Ordenado de O: `cap`
- O = `cap::2.11.1` — 47 palabras
  - fragmento E0 `cap::2.11.1` (punto_terminal; campo `texto`):

````text
2.11.1. Las entidades financieras del grupo 1 deberán clasificar las exposiciones a instrumen-
tos en:
i) Deuda subordinada emitida por empresas y/o entidades financieras.
ii) Acciones –definidas conforme a los criterios establecidos en el punto 2.11.3.–.
iii) Demás instrumentos de capital emitidos por empresas y/o entidades financieras.
````

- d = `cap::2.11.3` — 33 palabras — mismo Texto Ordenado que O
  - fragmento E0 `cap::2.11.3::intro` (mini_chunk, rol_bloque intro; campo `texto`):

````text
A los fines de determinar si una exposición debe ser tratada como una acción, las en-
tidades financieras del grupo 1 deberán tener en cuenta la realidad económica del ins-
trumento.
Quedan comprendidas:
````

  - aristas de remisión resuelta O → d: 1
    - [Obligacion] «Clasificación de exposiciones a acciones» → [Obligacion] «Tener en cuenta realidad económica» (destino `cap::2.11.3`; evidencia «ones, definidas conforme a los criterios establecidos en el punto 2.11.3.»)
- Preguntas EV2 que citan O o algún d: ninguna

### C04 — `cap::2.12.9.3` → {cap::S5}

- Texto Ordenado de O: `cap`
- O = `cap::2.12.9.3` — 25 palabras
  - fragmento E0 `cap::2.12.9.3` (punto_terminal; campo `texto`):

````text
2.12.9.3. Parte de las exposiciones que cuenten con coberturas del ries-
go de crédito. Deberá tenerse en cuenta lo dispuesto en la Sec-
ción 5.
````

- d = `cap::S5` — 97 palabras — mismo Texto Ordenado que O
  - fragmento E0 `cap::S5::chapeau_seccion` (mini_chunk, rol_bloque chapeau_seccion; campo `texto`):

````text
A los efectos del cómputo de la exigencia de capital por riesgo de crédito, se reconocerá –total o
parcialmente– la cobertura del riesgo de crédito (CRC) de las operaciones registradas en la cartera
de inversión –tales como préstamos y responsabilidades eventuales– mediante la utilización de las
técnicas previstas en el punto 5.1.
La presente sección contempla, además, el cálculo de la exposición a las operaciones de financia-
ción con títulos valores (securities financing transactions, SFT) –conforme a lo previsto en la Sec-
ción 4.–, registradas tanto en la cartera de inversión como en la cartera de negociación.
````

  - aristas de remisión resuelta O → d: 5
    - [Obligacion] «Aplicar disposiciones Sección 5» → [Obligacion] «Calcular exposición SFT conforme Sección 4» (destino `cap::S5`; evidencia «Aplicar disposiciones Sección 5 | Deberá tenerse en»)
    - [Obligacion] «Aplicar disposiciones Sección 5» → [Obligacion] «Utilizar técnicas cobertura riesgo crédito punto 5.1» (destino `cap::S5`; evidencia «Aplicar disposiciones Sección 5 | Deberá tenerse en»)
    - [Obligacion] «Aplicar disposiciones Sección 5» → [Operacion] «Cálculo exposición operaciones financiación títulos» (destino `cap::S5`; evidencia «Aplicar disposiciones Sección 5 | Deberá tenerse en»)
    - [Obligacion] «Aplicar disposiciones Sección 5» → [Operacion] «Cobertura riesgo crédito cartera inversión» (destino `cap::S5`; evidencia «Aplicar disposiciones Sección 5 | Deberá tenerse en»)
    - [Obligacion] «Aplicar disposiciones Sección 5» → [Operacion] «Cómputo exigencia capital riesgo crédito» (destino `cap::S5`; evidencia «Aplicar disposiciones Sección 5 | Deberá tenerse en»)
- Preguntas EV2 que citan O o algún d: ninguna

### C05 — `cap::2.12.10.1` → {cap::2.11.3}

- Texto Ordenado de O: `cap`
- O = `cap::2.12.10.1` — 38 palabras
  - fragmento E0 `cap::2.12.10.1` (punto_terminal; campo `texto`):

````text
2.12.10.1. Exposiciones a instrumentos por parte de entidades financieras
del grupo 1.
i) Deuda subordinada e instrumentos de capital que no reúnen
las características para ser considerados como acciones. 150
ii) Acciones (definidas conforme al punto 2.11.3.). 250
````

- d = `cap::2.11.3` — 33 palabras — mismo Texto Ordenado que O
  - fragmento E0 `cap::2.11.3::intro` (mini_chunk, rol_bloque intro; campo `texto`):

````text
A los fines de determinar si una exposición debe ser tratada como una acción, las en-
tidades financieras del grupo 1 deberán tener en cuenta la realidad económica del ins-
trumento.
Quedan comprendidas:
````

  - aristas de remisión resuelta O → d: 1
    - [Restriccion] «Ponderador 250% — acciones» → [Obligacion] «Tener en cuenta realidad económica» (destino `cap::2.11.3`; evidencia «— acciones | Exposiciones a acciones (definidas conforme al punto 2.11.3.): ponderador 250% |»)
- Preguntas EV2 que citan O o algún d: ninguna

### C06 — `cap::6.1.3.4` → {cap::S5}

- Texto Ordenado de O: `cap`
- O = `cap::6.1.3.4` — 38 palabras
  - fragmento E0 `cap::6.1.3.4` (punto_terminal; campo `texto`):

````text
6.1.3.4. Con independencia de la cartera en la que se registren, las operaciones de pase
(acuerdos REPO) estarán sujetas a la exigencia de capital por riesgo de crédito
de contraparte conforme a lo previsto en la Sección 5.
````

- d = `cap::S5` — 97 palabras — mismo Texto Ordenado que O
  - fragmento E0 `cap::S5::chapeau_seccion` (mini_chunk, rol_bloque chapeau_seccion; campo `texto`):

````text
A los efectos del cómputo de la exigencia de capital por riesgo de crédito, se reconocerá –total o
parcialmente– la cobertura del riesgo de crédito (CRC) de las operaciones registradas en la cartera
de inversión –tales como préstamos y responsabilidades eventuales– mediante la utilización de las
técnicas previstas en el punto 5.1.
La presente sección contempla, además, el cálculo de la exposición a las operaciones de financia-
ción con títulos valores (securities financing transactions, SFT) –conforme a lo previsto en la Sec-
ción 4.–, registradas tanto en la cartera de inversión como en la cartera de negociación.
````

  - aristas de remisión resuelta O → d: 5
    - [Restriccion] «Operaciones de pase sujetas a exigencia de capital» → [Obligacion] «Calcular exposición SFT conforme Sección 4» (destino `cap::S5`; evidencia «esgo de crédito de contraparte conforme a lo previsto en la Sección 5.»)
    - [Restriccion] «Operaciones de pase sujetas a exigencia de capital» → [Obligacion] «Utilizar técnicas cobertura riesgo crédito punto 5.1» (destino `cap::S5`; evidencia «esgo de crédito de contraparte conforme a lo previsto en la Sección 5.»)
    - [Restriccion] «Operaciones de pase sujetas a exigencia de capital» → [Operacion] «Cálculo exposición operaciones financiación títulos» (destino `cap::S5`; evidencia «esgo de crédito de contraparte conforme a lo previsto en la Sección 5.»)
    - [Restriccion] «Operaciones de pase sujetas a exigencia de capital» → [Operacion] «Cobertura riesgo crédito cartera inversión» (destino `cap::S5`; evidencia «esgo de crédito de contraparte conforme a lo previsto en la Sección 5.»)
    - [Restriccion] «Operaciones de pase sujetas a exigencia de capital» → [Operacion] «Cómputo exigencia capital riesgo crédito» (destino `cap::S5`; evidencia «esgo de crédito de contraparte conforme a lo previsto en la Sección 5.»)
- Preguntas EV2 que citan O o algún d: ninguna

### C07 — `cap::6.5` → {cap::6.4}

- Texto Ordenado de O: `cap`
- O = `cap::6.5` — 47 palabras
  - fragmento E0 `cap::6.5::intro` (mini_chunk, rol_bloque intro; campo `texto`):

````text
Cubre el riesgo de mantener posiciones en productos básicos, incluidos metales preciosos ex-
cepto el oro (tratado en el punto 6.4.). A los fines de estas normas, se define como producto
básico (o materia prima) –“commodities”– a todo producto físico negociado o negociable en un
mercado secundario.
````

- d = `cap::6.4` — 22 palabras — mismo Texto Ordenado que O
  - fragmento E0 `cap::6.4::intro` (mini_chunk, rol_bloque intro; campo `texto`):

````text
El presente punto establece el capital mínimo necesario para cubrir el riesgo de mantener po-
siciones en moneda extranjera, incluido el oro.
````

  - aristas de remisión resuelta O → d: 1
    - [Restriccion] «Exclusión del oro de cobertura» → [Obligacion] «Capital mínimo — riesgo de tipo de cambio» (destino `cap::6.4`; evidencia «exigencia de capital excluyen el oro, que es tratado en el punto 6.4»)
- Preguntas EV2 que citan O o algún d: `EV2F-018` (ancla cap:6.5)

### C08 — `cap::6.6.3.4` → {cap::6.4}

- Texto Ordenado de O: `cap`
- O = `cap::6.6.3.4` — 42 palabras
  - fragmento E0 `cap::6.6.3.4` (punto_terminal; campo `texto`):

````text
6.6.3.4. En el caso de las opciones sobre oro y monedas extranjeras, el neto del equi-
valente delta de estas opciones se incorporará a la exposición en oro o en la
moneda extranjera correspondiente conforme a lo previsto en el punto 6.4.
````

- d = `cap::6.4` — 22 palabras — mismo Texto Ordenado que O
  - fragmento E0 `cap::6.4::intro` (mini_chunk, rol_bloque intro; campo `texto`):

````text
El presente punto establece el capital mínimo necesario para cubrir el riesgo de mantener po-
siciones en moneda extranjera, incluido el oro.
````

  - aristas de remisión resuelta O → d: 1
    - [Obligacion] «Neto equivalente delta opciones oro/monedas se incorpora» → [Obligacion] «Capital mínimo — riesgo de tipo de cambio» (destino `cap::6.4`; evidencia «eda extranjera correspondiente conforme a lo previsto en el punto 6.4»)
- Preguntas EV2 que citan O o algún d: ninguna

### C09 — `cap::6.7.1` → {cap::1.1}

- Texto Ordenado de O: `cap`
- O = `cap::6.7.1` — 21 palabras
  - fragmento E0 `cap::6.7.1::intro` (mini_chunk, rol_bloque intro; campo `texto`):

````text
A los fines del cumplimiento de lo establecido en el punto 1.1., la integración se deter-
minará en forma diaria considerando:
````

- d = `cap::1.1` — 51 palabras — mismo Texto Ordenado que O
  - fragmento E0 `cap::1.1` (punto_terminal; campo `texto`):

````text
1.1. Exigencia.
La exigencia de capital mínimo que las entidades financieras deberán tener integrada será
equivalente al mayor valor que resulte de la comparación entre la exigencia básica y la suma de
las determinadas por riesgos de crédito, de mercado –exigencia por las posiciones diarias de
los activos comprendidos– y operacional.
````

  - aristas de remisión resuelta O → d: 2
    - [Obligacion] «Integración diaria considerando lo establecido» → [Obligacion] «Integración de capital mínimo requerido» (destino `cap::1.1`; evidencia «cido | A los fines del cumplimiento de lo establecido en el punto 1.1., la integración se»)
    - [Obligacion] «Integración diaria considerando lo establecido» → [Operacion] «Determinación de exigencia de capital mínimo» (destino `cap::1.1`; evidencia «cido | A los fines del cumplimiento de lo establecido en el punto 1.1., la integración se»)
- Preguntas EV2 que citan O o algún d: ninguna

### C10 — `cap::6.7.1.1` → {cap::1.1}

- Texto Ordenado de O: `cap`
- O = `cap::6.7.1.1` — 10 palabras
  - fragmento E0 `cap::6.7.1.1` (punto_terminal; campo `texto`):

````text
6.7.1.1. la RPC del último día del mes anterior; y
````

- d = `cap::1.1` — 51 palabras — mismo Texto Ordenado que O
  - fragmento E0 `cap::1.1` (punto_terminal; campo `texto`):

````text
1.1. Exigencia.
La exigencia de capital mínimo que las entidades financieras deberán tener integrada será
equivalente al mayor valor que resulte de la comparación entre la exigencia básica y la suma de
las determinadas por riesgos de crédito, de mercado –exigencia por las posiciones diarias de
los activos comprendidos– y operacional.
````

  - aristas de remisión resuelta O → d: 2
    - [Obligacion] «Integración de capital — RPC último día mes anterior» → [Obligacion] «Integración de capital mínimo requerido» (destino `cap::1.1`; evidencia «rior | A los fines del cumplimiento de lo establecido en el punto 1.1., la integración se»)
    - [Obligacion] «Integración de capital — RPC último día mes anterior» → [Operacion] «Determinación de exigencia de capital mínimo» (destino `cap::1.1`; evidencia «rior | A los fines del cumplimiento de lo establecido en el punto 1.1., la integración se»)
- Preguntas EV2 que citan O o algún d: ninguna

### C11 — `cap::8.2.1.9` → {cap::8.3.5}

- Texto Ordenado de O: `cap`
- O = `cap::8.2.1.9` — 54 palabras
  - fragmento E0 `cap::8.2.1.9` (punto_terminal; campo `texto`):

````text
8.2.1.9. Participaciones minoritarias. Acciones ordinarias emitidas por subsidiarias suje-
tas a supervisión consolidada y en poder de terceros, que cumplan los criterios
establecidos en el punto 8.3.5.
A los conceptos citados en los puntos precedentes se les restarán los conceptos dedu-
cibles previstos en el punto 8.4.1. y, de corresponder, en el punto 8.4.2.
````

- d = `cap::8.3.5` — 13 palabras — mismo Texto Ordenado que O
  - fragmento E0 `cap::8.3.5::intro` (mini_chunk, rol_bloque intro; campo `texto`):

````text
como capital emitidos por subsidiarias sujetas a supervisión consolidada en poder de
terceros.
````

  - aristas de remisión resuelta O → d: 2
    - [Obligacion] «Inclusión de acciones ordinarias minoritarias CO1» → [Obligacion] «Capital emitido por subsidiarias consolidadas computable» (destino `cap::8.3.5`; evidencia «r de terceros, que cumplan los criterios establecidos en el punto 8.3.5, se incluyen como r»)
    - [Obligacion] «Inclusión de acciones ordinarias minoritarias CO1» → [Operacion] «Emisión de capital por subsidiarias consolidadas» (destino `cap::8.3.5`; evidencia «r de terceros, que cumplan los criterios establecidos en el punto 8.3.5, se incluyen como r»)
- Preguntas EV2 que citan O o algún d: ninguna

### C12 — `cap::8.2.2.1` → {cap::8.3.2}

- Texto Ordenado de O: `cap`
- O = `cap::8.2.2.1` — 28 palabras
  - fragmento E0 `cap::8.2.2.1` (punto_terminal; campo `texto`):

````text
8.2.2.1. Instrumentos emitidos por la entidad financiera que cumplan los requisitos pre-
vistos en el punto 8.3.2. y no se hallen ya incluidos en el CO .
n1
````

- d = `cap::8.3.2` — 1 palabras — mismo Texto Ordenado que O
  - fragmento E0 `cap::8.3.2::intro` (mini_chunk, rol_bloque intro; campo `texto`):

````text
n1
````

  - aristas de remisión resuelta O → d: 1
    - [Restriccion] «Cumplimiento requisitos punto 8.3.2» → [Obligacion] «Requisitos observancia instrumentos CA» (destino `cap::8.3.2`; evidencia «Cumplimiento requisitos punto 8.3.2 | Los instrumentos»)
- Preguntas EV2 que citan O o algún d: `EV2F-023` (ancla cap:8.3.2)

### C13 — `cap::8.2.2.3` → {cap::8.3.5}

- Texto Ordenado de O: `cap`
- O = `cap::8.2.2.3` — 63 palabras
  - fragmento E0 `cap::8.2.2.3` (punto_terminal; campo `texto`):

````text
8.2.2.3. Instrumentos emitidos por subsidiarias sujetas a supervisión consolidada en
poder de terceros, que cumplan los criterios para su inclusión en el CA y que
n1
no estén incluidos en el CO , observando los criterios establecidos en el punto
n1
8.3.5.
A los conceptos citados en los puntos precedentes se les restarán, de corresponder, los
conceptos deducibles previstos en el punto 8.4.2.
````

- d = `cap::8.3.5` — 13 palabras — mismo Texto Ordenado que O
  - fragmento E0 `cap::8.3.5::intro` (mini_chunk, rol_bloque intro; campo `texto`):

````text
como capital emitidos por subsidiarias sujetas a supervisión consolidada en poder de
terceros.
````

  - aristas de remisión resuelta O → d: 2
    - [Restriccion] «Criterios de cumplimiento para inclusión en CA n1» → [Obligacion] «Capital emitido por subsidiarias consolidadas computable» (destino `cap::8.3.5`; evidencia «ón en el CA n1, observando los criterios establecidos en el punto 8.3.5»)
    - [Restriccion] «Criterios de cumplimiento para inclusión en CA n1» → [Operacion] «Emisión de capital por subsidiarias consolidadas» (destino `cap::8.3.5`; evidencia «ón en el CA n1, observando los criterios establecidos en el punto 8.3.5»)
- Preguntas EV2 que citan O o algún d: ninguna

### C14 — `cap::8.2.3.4` → {cap::8.3.5}

- Texto Ordenado de O: `cap`
- O = `cap::8.2.3.4` — 39 palabras
  - fragmento E0 `cap::8.2.3.4` (punto_terminal; campo `texto`):

````text
8.2.3.4. Instrumentos emitidos por subsidiarias sujetas a supervisión consolidada en
poder de terceros, que cumplan los criterios para su inclusión en el PNc y que
no estén incluidos en el PNb, observando los criterios establecidos en el punto
8.3.5.
````

- d = `cap::8.3.5` — 13 palabras — mismo Texto Ordenado que O
  - fragmento E0 `cap::8.3.5::intro` (mini_chunk, rol_bloque intro; campo `texto`):

````text
como capital emitidos por subsidiarias sujetas a supervisión consolidada en poder de
terceros.
````

  - aristas de remisión resuelta O → d: 2
    - [Obligacion] «Observancia de criterios punto 8.3.5» → [Obligacion] «Capital emitido por subsidiarias consolidadas computable» (destino `cap::8.3.5`; evidencia «Observancia de criterios punto 8.3.5 | Observar los crit»)
    - [Obligacion] «Observancia de criterios punto 8.3.5» → [Operacion] «Emisión de capital por subsidiarias consolidadas» (destino `cap::8.3.5`; evidencia «Observancia de criterios punto 8.3.5 | Observar los crit»)
- Preguntas EV2 que citan O o algún d: ninguna

### C15 — `cla::3.3.3` → {cla::3.7}

- Texto Ordenado de O: `cla`
- O = `cla::3.3.3` — 43 palabras
  - fragmento E0 `cla::3.3.3` (punto_terminal; campo `texto`):

````text
3.3.3. El ejercicio de la opción de agrupar las financiaciones de naturaleza comercial de hasta el
equivalente a dos veces el importe de referencia establecido en el punto 3.7., cuenten o
no con garantías preferidas, junto con los créditos para consumo o vivienda.
````

- d = `cla::3.7` — 39 palabras — mismo Texto Ordenado que O
  - fragmento E0 `cla::3.7` (punto_terminal; campo `texto`):

````text
3.7. Importe de referencia.
El importe a considerar será el nivel máximo del valor de ventas totales anuales para la
categoría “Micro” correspondiente al sector “Comercio” que determine la autoridad de
aplicación de la Ley 24.467 (y sus modificatorias).
````

  - aristas de remisión resuelta O → d: 1
    - [Restriccion] «Tope de hasta dos veces importe referencia — agrupación comercial» → [Obligacion] «Considerar importe de referencia — ventas anuales Micro Comercio» (destino `cla::3.7`; evidencia «ente a dos veces el importe de referencia establecido en el punto 3.7. | dos veces el impo»)
- Preguntas EV2 que citan O o algún d: ninguna

### C16 — `cla::5.1.1.1` → {cla::3.7}

- Texto Ordenado de O: `cla`
- O = `cla::5.1.1.1` — 60 palabras
  - fragmento E0 `cla::5.1.1.1` (punto_terminal; campo `texto`):

````text
5.1.1.1. Los créditos para consumo o vivienda.
Los créditos de esta clase que superen el equivalente a dos veces el importe de
referencia establecido en el punto 3.7. y cuyo repago no se encuentre vinculado
a ingresos fijos o periódicos del cliente sino a la evolución de su actividad pro-
ductiva o comercial se incluirán dentro de la cartera comercial.
````

- d = `cla::3.7` — 39 palabras — mismo Texto Ordenado que O
  - fragmento E0 `cla::3.7` (punto_terminal; campo `texto`):

````text
3.7. Importe de referencia.
El importe a considerar será el nivel máximo del valor de ventas totales anuales para la
categoría “Micro” correspondiente al sector “Comercio” que determine la autoridad de
aplicación de la Ley 24.467 (y sus modificatorias).
````

  - aristas de remisión resuelta O → d: 1
    - [Restriccion] «Créditos consumo/vivienda — monto supera dos veces importe referencia» → [Obligacion] «Considerar importe de referencia — ventas anuales Micro Comercio» (destino `cla::3.7`; evidencia «ente a dos veces el importe de referencia establecido en el punto 3.7. | 2x importe refere»)
- Preguntas EV2 que citan O o algún d: ninguna

### C17 — `cla::5.1.2.3` → {cla::3.7}

- Texto Ordenado de O: `cla`
- O = `cla::5.1.2.3` — 39 palabras
  - fragmento E0 `cla::5.1.2.3` (punto_terminal; campo `texto`):

````text
5.1.2.3. Préstamos a Instituciones de Microcrédito –hasta el equivalente al 40 % del im-
porte de referencia establecido en el punto 3.7.– y a microemprendedores (se-
gún lo previsto en el punto 1.1.3.4. de las normas sobre “Gestión crediticia”).
````

- d = `cla::3.7` — 39 palabras — mismo Texto Ordenado que O
  - fragmento E0 `cla::3.7` (punto_terminal; campo `texto`):

````text
3.7. Importe de referencia.
El importe a considerar será el nivel máximo del valor de ventas totales anuales para la
categoría “Micro” correspondiente al sector “Comercio” que determine la autoridad de
aplicación de la Ley 24.467 (y sus modificatorias).
````

  - aristas de remisión resuelta O → d: 1
    - [Restriccion] «Tope 40 % importe de referencia (punto 3.7)» → [Obligacion] «Considerar importe de referencia — ventas anuales Micro Comercio» (destino `cla::3.7`; evidencia «Tope 40 % importe de referencia (punto 3.7) | hasta el equival»)
- Preguntas EV2 que citan O o algún d: ninguna

### C18 — `cla::5.1.2.4` → {cla::3.7}

- Texto Ordenado de O: `cla`
- O = `cla::5.1.2.4` — 35 palabras
  - fragmento E0 `cla::5.1.2.4` (punto_terminal; campo `texto`):

````text
5.1.2.4. Las financiaciones de naturaleza comercial de hasta el equivalente a dos veces
el importe de referencia establecido en el punto 3.7., cuenten o no con garantías
preferidas, cuando la entidad haya optado por ello.
````

- d = `cla::3.7` — 39 palabras — mismo Texto Ordenado que O
  - fragmento E0 `cla::3.7` (punto_terminal; campo `texto`):

````text
3.7. Importe de referencia.
El importe a considerar será el nivel máximo del valor de ventas totales anuales para la
categoría “Micro” correspondiente al sector “Comercio” que determine la autoridad de
aplicación de la Ley 24.467 (y sus modificatorias).
````

  - aristas de remisión resuelta O → d: 1
    - [Restriccion] «Límite cuantitativo — dos veces importe referencia» → [Obligacion] «Considerar importe de referencia — ventas anuales Micro Comercio» (destino `cla::3.7`; evidencia «ente a dos veces el importe de referencia establecido en el punto 3.7. | 2x importe refere»)
- Preguntas EV2 que citan O o algún d: ninguna

### C19 — `cla::6.5.1.4` → {cla::6.3}

- Texto Ordenado de O: `cla`
- O = `cla::6.5.1.4` — 71 palabras
  - fragmento E0 `cla::6.5.1.4` (punto_terminal; campo `texto`):

````text
6.5.1.4. tenga un adecuado sistema de información que permita conocer en forma per-
manente la situación financiera y económica de la empresa. La información es
consistente y está actualizada. Cuando las financiaciones cuenten con garantías
preferidas “B”, según las normas aplicables en esa materia, la entidad podrá re-
querir esa información con la frecuencia que le permita efectuar la evaluación
del deudor observando la periodicidad mínima establecida en el punto 6.3.
````

- d = `cla::6.3` — 23 palabras — mismo Texto Ordenado que O
  - fragmento E0 `cla::6.3::intro` (mini_chunk, rol_bloque intro; campo `texto`):

````text
La revisión deberá efectuarse como mínimo con la periodicidad que se indica seguidamente,
dejando constancia de ello en el legajo del cliente analizado:
````

  - aristas de remisión resuelta O → d: 1
    - [Obligacion] «Requerimiento información garantías preferidas B» → [Obligacion] «Revisión con periodicidad mínima de clasificación» (destino `cla::6.3`; evidencia «deudor observando la periodicidad mínima establecida en el punto 6.3 | periodicidad míni»)
- Preguntas EV2 que citan O o algún d: ninguna

### C20 — `ext::2.6.1.2` → {ext::2.6.2}

- Texto Ordenado de O: `ext`
- O = `ext::2.6.1.2` — 25 palabras
  - fragmento E0 `ext::2.6.1.2` (punto_terminal; campo `texto`):

````text
2.6.1.2. cuenten con una “Certificación de incremento de exportaciones asociadas a
la economía del conocimiento (Decreto 679/22)” en los términos previstos en
el punto 2.6.2.;
````

- d = `ext::2.6.2` — 71 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ext::2.6.2::intro` (mini_chunk, rol_bloque intro; campo `texto`):

````text
responsable de emitir las “Certificaciones de incremento de exportaciones asociadas a
la economía del conocimiento (Decreto 679/22)” y remitirlas a las entidades por las
cuales el cliente desee concretar los ingresos de sus cobros de exportaciones de
bienes o servicios.
La entidad nominada podrá emitir estas certificaciones para cada periodo trimestral de
referencia posterior a la inscripción del cliente en el registro, cuando se verifiquen la
totalidad de los siguientes requisitos:
````

  - aristas de remisión resuelta O → d: 2
    - [Obligacion] «Certificación incremento exportaciones economía conocimiento» → [Obligacion] «Nominación entidad financiera local — emisión certificaciones exportación» (destino `ext::2.6.2`; evidencia «ocimiento (Decreto 679/22)" en los términos previstos en el punto 2.6.2.»)
    - [Obligacion] «Certificación incremento exportaciones economía conocimiento» → [Obligacion] «Emisión certificaciones por periodo trimestral — requisitos» (destino `ext::2.6.2`; evidencia «ocimiento (Decreto 679/22)" en los términos previstos en el punto 2.6.2.»)
- Preguntas EV2 que citan O o algún d: ninguna

### C21 — `ext::3.4.4.3` → {ext::14.2.2}

- Texto Ordenado de O: `ext`
- O = `ext::3.4.4.3` — 51 palabras
  - fragmento E0 `ext::3.4.4.3` (punto_terminal; campo `texto`):

````text
3.4.4.3. El cliente es un Vehículo de Proyecto Único (VPU) adherido al Régimen de
Incentivo para Grandes Inversiones (RIGI) y las utilidades corresponden a
aportes de inversión extranjera directa que encuadran en lo previsto en el
punto 14.2.2.
El cliente deberá presentar la documentación que avale la capitalización
definitiva del aporte.
````

- d = `ext::14.2.2` — 112 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ext::14.2.2` (punto_terminal; campo `texto`):

````text
14.2.2. En el marco de lo dispuesto en el punto 3.4. las entidades también podrán darle
acceso al mercado de cambios al VPU para pagar utilidades y dividendos a sus
accionistas no residentes, sin necesidad de contar con la conformidad previa del
BCRA si este requisito estuviese vigente, cuando el pago corresponda a montos
pendientes con el accionista no residente por:
i) la proporción de sus aportes de inversión directa en el VPU que fue ingresada y
liquidada por el mercado de cambios, o
ii) por sus aportes de inversión directa en especie instrumentados mediante la
entrega al VPU de bienes de capital que cumplen las condiciones previstas en
el punto 14.5.4.
````

  - aristas de remisión resuelta O → d: 5
    - [Restriccion] «Cliente debe encuadrar en situación — pagos de utilidades» → [Excepcion] «Exención conformidad previa BCRA — utilidades/dividendos» (destino `ext::14.2.2`; evidencia «rsión extranjera directa que encuadran en lo previsto en el punto 14.2.2»)
    - [Restriccion] «Cliente debe encuadrar en situación — pagos de utilidades» → [Obligacion] «Cumplimiento requisitos — acceso cambios utilidades/dividendos» (destino `ext::14.2.2`; evidencia «rsión extranjera directa que encuadran en lo previsto en el punto 14.2.2»)
    - [Restriccion] «Cliente debe encuadrar en situación — pagos de utilidades» → [Operacion] «Acceso mercado cambios — pago utilidades/dividendos VPU» (destino `ext::14.2.2`; evidencia «rsión extranjera directa que encuadran en lo previsto en el punto 14.2.2»)
    - [Restriccion] «Cliente debe encuadrar en situación — pagos de utilidades» → [Restriccion] «Límite cualitativo — aportes inversión directa en especie» (destino `ext::14.2.2`; evidencia «rsión extranjera directa que encuadran en lo previsto en el punto 14.2.2»)
    - [Restriccion] «Cliente debe encuadrar en situación — pagos de utilidades» → [Restriccion] «Límite cualitativo — proporción aportes inversión directa» (destino `ext::14.2.2`; evidencia «rsión extranjera directa que encuadran en lo previsto en el punto 14.2.2»)
- Preguntas EV2 que citan O o algún d: ninguna

### C22 — `ext::3.6.1.2` → {ext::3.6.2}

- Texto Ordenado de O: `ext`
- O = `ext::3.6.1.2` — 34 palabras
  - fragmento E0 `ext::3.6.1.2` (punto_terminal; campo `texto`):

````text
3.6.1.2. las emisiones de títulos de deuda realizadas a partir del 01/09/19 con el
objeto de refinanciar deudas comprendidas en el punto 3.6.2. y conlleven un
incremento de la vida promedio de las obligaciones.
````

- d = `ext::3.6.2` — 33 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ext::3.6.2` (punto_terminal; campo `texto`):

````text
3.6.2. Las entidades podrán dar acceso al mercado de cambios para la cancelación a partir
de su vencimiento de obligaciones en moneda extranjera entre residentes
instrumentadas mediante registros o escrituras públicos al 30/08/19.
````

  - aristas de remisión resuelta O → d: 2
    - [Restriccion] «Prohibición pagos deudas refinanciadas con incremento vida promedio» → [Obligacion] «Acceso mercado cambios para cancelación desde vencimiento» (destino `ext::3.6.2`; evidencia «9/19 con el objeto de refinanciar deudas comprendidas en el punto 3.6.2., siempre que conlle»)
    - [Restriccion] «Prohibición pagos deudas refinanciadas con incremento vida promedio» → [Operacion] «Cancelación de obligaciones moneda extranjera» (destino `ext::3.6.2`; evidencia «9/19 con el objeto de refinanciar deudas comprendidas en el punto 3.6.2., siempre que conlle»)
- Preguntas EV2 que citan O o algún d: ninguna

### C23 — `ext::3.11.1.1` → {ext::3.5}

- Texto Ordenado de O: `ext`
- O = `ext::3.11.1.1` — 71 palabras
  - fragmento E0 `ext::3.11.1.1` (punto_terminal; campo `texto`):

````text
3.11.1.1. se trate de deudas comerciales por importaciones de bienes y/o servicios
con una entidad financiera del exterior o agencia oficial de crédito a la
exportación o endeudamientos financieros comprendidos en el punto 3.5.
con acreedores no vinculados, que normativamente tengan acceso al
mercado de cambios para su repago, en cuyos contratos se prevea la
acreditación de fondos en cuentas de garantía de futuros servicios de las
deudas con el exterior;
````

- d = `ext::3.5` — 61 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ext::3.5::intro` (mini_chunk, rol_bloque intro; campo `texto`):

````text
exterior.
Las entidades podrán dar acceso al mercado de cambios para realizar pagos de capital o
intereses de títulos de deuda con registro público en el exterior, otros endeudamientos
financieros con el exterior y títulos de deuda con registro público en el país denominados en
moneda extranjera íntegramente suscriptos en el exterior, en la medida que se verifiquen las
siguientes condiciones:
````

  - aristas de remisión resuelta O → d: 8
    - [Restriccion] «Deudas comerciales por importaciones bienes/servicios» → [Obligacion] «Acceso mercado cambios pagos deuda» (destino `ext::3.5`; evidencia «exportación o endeudamientos financieros comprendidos en el punto 3.5. con acreedores no v»)
    - [Restriccion] «Deudas comerciales por importaciones bienes/servicios» → [Operacion] «Endeudamientos financieros exterior» (destino `ext::3.5`; evidencia «exportación o endeudamientos financieros comprendidos en el punto 3.5. con acreedores no v»)
    - [Restriccion] «Deudas comerciales por importaciones bienes/servicios» → [Operacion] «Pago títulos deuda y endeudamientos» (destino `ext::3.5`; evidencia «exportación o endeudamientos financieros comprendidos en el punto 3.5. con acreedores no v»)
    - [Restriccion] «Deudas comerciales por importaciones bienes/servicios» → [Operacion] «Pago títulos deuda y endeudamientos exterior» (destino `ext::3.5`; evidencia «exportación o endeudamientos financieros comprendidos en el punto 3.5. con acreedores no v»)
    - [Restriccion] «Deudas comerciales por importaciones bienes/servicios» → [Operacion] «Pagos de endeudamientos financieros» (destino `ext::3.5`; evidencia «exportación o endeudamientos financieros comprendidos en el punto 3.5. con acreedores no v»)
    - [Restriccion] «Deudas comerciales por importaciones bienes/servicios» → [Operacion] «Pagos de títulos deuda exterior» (destino `ext::3.5`; evidencia «exportación o endeudamientos financieros comprendidos en el punto 3.5. con acreedores no v»)
    - [Restriccion] «Deudas comerciales por importaciones bienes/servicios» → [Operacion] «Pagos intereses títulos deuda exterior» (destino `ext::3.5`; evidencia «exportación o endeudamientos financieros comprendidos en el punto 3.5. con acreedores no v»)
    - [Restriccion] «Deudas comerciales por importaciones bienes/servicios» → [Operacion] «Pagos títulos deuda país moneda extranjera» (destino `ext::3.5`; evidencia «exportación o endeudamientos financieros comprendidos en el punto 3.5. con acreedores no v»)
- Preguntas EV2 que citan O o algún d: ninguna

### C24 — `ext::3.18.3.1` → {ext::7.1.1.2, ext::7.8.1.1}

- Texto Ordenado de O: `ext`
- O = `ext::3.18.3.1` — 28 palabras
  - fragmento E0 `ext::3.18.3.1` (punto_terminal; campo `texto`):

````text
3.18.3.1. 5% (cinco por ciento) cuando corresponda a bienes que tienen asignado
un plazo de 30 (treinta) días corridos en virtud de lo dispuesto en el punto
7.1.1.2.
````

- d = `ext::7.1.1.2` — 30 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ext::7.1.1.2` (punto_terminal; campo `texto`):

````text
7.1.1.2. 30 (treinta) días corridos para las exportaciones de bienes que correspondan
a las posiciones arancelarias 1003.90.10, 1003.90.80, 1007.90.00 y a las
correspondientes al capítulo 27 (excepto la posición 2716.00.00).
````

  - aristas de remisión resuelta O → d: 2
    - [Restriccion] «Coeficiente 5% — bienes plazo 30 días» → [Obligacion] «Ingreso y liquidación 30 días — exportaciones posiciones arancelarias» (destino `ext::7.1.1.2`; evidencia «30 (treinta) días corridos en virtud de lo dispuesto en el punto 7.1.1.2 | 5%»)
    - [Restriccion] «Coeficiente 5% — bienes plazo 30 días» → [Operacion] «Ingreso y liquidación de divisas — exportación» (destino `ext::7.1.1.2`; evidencia «30 (treinta) días corridos en virtud de lo dispuesto en el punto 7.1.1.2 | 5%»; procedencias del nodo destino: `ext::7.1.1.2`, `ext::7.8.1.1`)
- d = `ext::7.8.1.1` — 36 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ext::7.8.1.1` (punto_terminal; campo `texto`):

````text
7.8.1.1. En la medida que estén nominados en el permiso de embarque, ambas
partes (documentante y propietario de la mercadería) son responsables del
cumplimiento de la obligación de ingreso y liquidación de divisas por la
operación.
````

  - d entra a D solo por procedencia múltiple del nodo destino (ninguna arista O → d tiene `destino` = d)
  - aristas de remisión resuelta O → d: 1
    - [Restriccion] «Coeficiente 5% — bienes plazo 30 días» → [Operacion] «Ingreso y liquidación de divisas — exportación» (destino `ext::7.1.1.2`; evidencia «30 (treinta) días corridos en virtud de lo dispuesto en el punto 7.1.1.2 | 5%»; procedencias del nodo destino: `ext::7.1.1.2`, `ext::7.8.1.1`)
- Preguntas EV2 que citan O o algún d: ninguna

### C25 — `ext::5.5.2` → {ext::5.5.1, ext::5.5.1.1}

- Texto Ordenado de O: `ext`
- O = `ext::5.5.2` — 33 palabras
  - fragmento E0 `ext::5.5.2` (punto_terminal; campo `texto`):

````text
5.5.2. Contar con procedimientos efectivos que permitan detectar aquellas transferencias
recibidas del exterior y sus respectivos mensajes, con información incompleta del
ordenante y/o del beneficiario, conforme a lo previsto en el punto 5.5.1.
````

- d = `ext::5.5.1` — 12 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ext::5.5.1::intro` (mini_chunk, rol_bloque intro; campo `texto`):

````text
información completa respecto del ordenante y del beneficiario. Como mínimo la
siguiente:
````

  - aristas de remisión resuelta O → d: 2
    - [Obligacion] «Procedimientos detección transferencias incompletas» → [Obligacion] «Incluir información ordenante y beneficiario» (destino `ext::5.5.1`; evidencia «rdenante y/o del beneficiario, conforme a lo previsto en el punto 5.5.1»)
    - [Obligacion] «Procedimientos detección transferencias incompletas» → [Operacion] «Transferencia de fondos con exterior» (destino `ext::5.5.1`; evidencia «rdenante y/o del beneficiario, conforme a lo previsto en el punto 5.5.1»; procedencias del nodo destino: `ext::5.5.1`, `ext::5.5.1.1`)
- d = `ext::5.5.1.1` — 46 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ext::5.5.1.1` (punto_terminal; campo `texto`):

````text
5.5.1.1. Ordenante:
i) apellidos y nombres completos o denominación social, según corresponda;
ii) domicilio o número de DNI o número de CUIT, CUIL, CDI o CIE;
iii)número de identificación del cliente en la entidad ordenante; y
iv)número de cuenta o Código Internacional de Cuenta Bancaria (IBAN)
````

  - d entra a D solo por procedencia múltiple del nodo destino (ninguna arista O → d tiene `destino` = d)
  - aristas de remisión resuelta O → d: 1
    - [Obligacion] «Procedimientos detección transferencias incompletas» → [Operacion] «Transferencia de fondos con exterior» (destino `ext::5.5.1`; evidencia «rdenante y/o del beneficiario, conforme a lo previsto en el punto 5.5.1»; procedencias del nodo destino: `ext::5.5.1`, `ext::5.5.1.1`)
- Preguntas EV2 que citan O o algún d: ninguna

### C26 — `ext::7.3.9` → {ext::7.10}

- Texto Ordenado de O: `ext`
- O = `ext::7.3.9` — 56 palabras
  - fragmento E0 `ext::7.3.9` (punto_terminal; campo `texto`):

````text
7.3.9. Operaciones habilitadas para la aplicación de cobros de exportaciones de bienes en el
marco del régimen de fomento de inversión para las exportaciones (Decreto 234/21).
Las operaciones enunciadas en el punto 7.10. en la medida que se cumplan los
requisitos y procedimientos estipulados para quedar habilitadas para la aplicación de
cobros de exportaciones de bienes.
````

- d = `ext::7.10` — 11 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ext::7.10::intro` (mini_chunk, rol_bloque intro; campo `texto`):

````text
del régimen de fomento de inversión para las exportaciones (Decreto 234/21).
````

  - aristas de remisión resuelta O → d: 3
    - [Obligacion] «Cumplimiento de requisitos y procedimientos» → [Obligacion] «Aplicación cobros — régimen Decreto 234/21» (destino `ext::7.10`; evidencia «uisitos y procedimientos | Las operaciones enunciadas en el punto 7.10. en la medida que se»)
    - [Obligacion] «Cumplimiento de requisitos y procedimientos» → [Operacion] «Aplicación divisas a cobros exportaciones» (destino `ext::7.10`; evidencia «uisitos y procedimientos | Las operaciones enunciadas en el punto 7.10. en la medida que se»)
    - [Obligacion] «Cumplimiento de requisitos y procedimientos» → [Operacion] «Cobro exportaciones bienes — fomento inversión» (destino `ext::7.10`; evidencia «uisitos y procedimientos | Las operaciones enunciadas en el punto 7.10. en la medida que se»)
- Preguntas EV2 que citan O o algún d: ninguna

### C27 — `ext::7.3.10` → {ext::7.11}

- Texto Ordenado de O: `ext`
- O = `ext::7.3.10` — 47 palabras
  - fragmento E0 `ext::7.3.10` (punto_terminal; campo `texto`):

````text
7.3.10. Financiaciones asociadas a importaciones de bienes habilitadas para la aplicación de
cobros de exportaciones de bienes
Financiaciones comerciales o financieras asociadas a la realización de pagos diferidos
o a la vista de importaciones de bienes que cumplan las condiciones y requisitos
previstos en el punto 7.11.
````

- d = `ext::7.11` — 4 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ext::7.11::intro` (mini_chunk, rol_bloque intro; campo `texto`):

````text
de exportaciones de bienes.
````

  - aristas de remisión resuelta O → d: 2
    - [Restriccion] «Condiciones y requisitos punto 7.11 — aplicación cobros exportaciones» → [Obligacion] «Habilitación de financiaciones de importaciones para cobros» (destino `ext::7.11`; evidencia «Condiciones y requisitos punto 7.11 — aplicación cobros»)
    - [Restriccion] «Condiciones y requisitos punto 7.11 — aplicación cobros exportaciones» → [Operacion] «Financiaciones asociadas a importaciones — cobros de exportaciones» (destino `ext::7.11`; evidencia «Condiciones y requisitos punto 7.11 — aplicación cobros»)
- Preguntas EV2 que citan O o algún d: ninguna

### C28 — `ext::7.8.4.3` → {ext::2.6.2}

- Texto Ordenado de O: `ext`
- O = `ext::7.8.4.3` — 38 palabras
  - fragmento E0 `ext::7.8.4.3` (punto_terminal; campo `texto`):

````text
7.8.4.3. el cliente cuente por el equivalente del monto que se pretende no liquidar
con una “Certificación de incremento de exportaciones asociadas a la
economía del conocimiento (Decreto 679/22)” emitida en los términos
previstos en el punto 2.6.2.
````

- d = `ext::2.6.2` — 71 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ext::2.6.2::intro` (mini_chunk, rol_bloque intro; campo `texto`):

````text
responsable de emitir las “Certificaciones de incremento de exportaciones asociadas a
la economía del conocimiento (Decreto 679/22)” y remitirlas a las entidades por las
cuales el cliente desee concretar los ingresos de sus cobros de exportaciones de
bienes o servicios.
La entidad nominada podrá emitir estas certificaciones para cada periodo trimestral de
referencia posterior a la inscripción del cliente en el registro, cuando se verifiquen la
totalidad de los siguientes requisitos:
````

  - aristas de remisión resuelta O → d: 2
    - [Obligacion] «Certificación de incremento de exportaciones — economía del conocimiento» → [Obligacion] «Nominación entidad financiera local — emisión certificaciones exportación» (destino `ext::2.6.2`; evidencia «o (Decreto 679/22)" emitida en los términos previstos en el punto 2.6.2»)
    - [Obligacion] «Certificación de incremento de exportaciones — economía del conocimiento» → [Obligacion] «Emisión certificaciones por periodo trimestral — requisitos» (destino `ext::2.6.2`; evidencia «o (Decreto 679/22)" emitida en los términos previstos en el punto 2.6.2»)
- Preguntas EV2 que citan O o algún d: ninguna

### C29 — `ext::7.10.1.2` → {ext::3.5}

- Texto Ordenado de O: `ext`
- O = `ext::7.10.1.2` — 18 palabras
  - fragmento E0 `ext::7.10.1.2` (punto_terminal; campo `texto`):

````text
7.10.1.2. Pago a partir del vencimiento de capital e intereses de endeudamientos
financieros comprendidos en el punto 3.5.
````

- d = `ext::3.5` — 61 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ext::3.5::intro` (mini_chunk, rol_bloque intro; campo `texto`):

````text
exterior.
Las entidades podrán dar acceso al mercado de cambios para realizar pagos de capital o
intereses de títulos de deuda con registro público en el exterior, otros endeudamientos
financieros con el exterior y títulos de deuda con registro público en el país denominados en
moneda extranjera íntegramente suscriptos en el exterior, en la medida que se verifiquen las
siguientes condiciones:
````

  - aristas de remisión resuelta O → d: 8
    - [Obligacion] «Aplicación cobros exportaciones — endeudamientos» → [Obligacion] «Acceso mercado cambios pagos deuda» (destino `ext::3.5`; evidencia «intereses de endeudamientos financieros comprendidos en el punto 3.5»)
    - [Obligacion] «Aplicación cobros exportaciones — endeudamientos» → [Operacion] «Endeudamientos financieros exterior» (destino `ext::3.5`; evidencia «intereses de endeudamientos financieros comprendidos en el punto 3.5»)
    - [Obligacion] «Aplicación cobros exportaciones — endeudamientos» → [Operacion] «Pago títulos deuda y endeudamientos» (destino `ext::3.5`; evidencia «intereses de endeudamientos financieros comprendidos en el punto 3.5»)
    - [Obligacion] «Aplicación cobros exportaciones — endeudamientos» → [Operacion] «Pago títulos deuda y endeudamientos exterior» (destino `ext::3.5`; evidencia «intereses de endeudamientos financieros comprendidos en el punto 3.5»)
    - [Obligacion] «Aplicación cobros exportaciones — endeudamientos» → [Operacion] «Pagos de endeudamientos financieros» (destino `ext::3.5`; evidencia «intereses de endeudamientos financieros comprendidos en el punto 3.5»)
    - [Obligacion] «Aplicación cobros exportaciones — endeudamientos» → [Operacion] «Pagos de títulos deuda exterior» (destino `ext::3.5`; evidencia «intereses de endeudamientos financieros comprendidos en el punto 3.5»)
    - [Obligacion] «Aplicación cobros exportaciones — endeudamientos» → [Operacion] «Pagos intereses títulos deuda exterior» (destino `ext::3.5`; evidencia «intereses de endeudamientos financieros comprendidos en el punto 3.5»)
    - [Obligacion] «Aplicación cobros exportaciones — endeudamientos» → [Operacion] «Pagos títulos deuda país moneda extranjera» (destino `ext::3.5`; evidencia «intereses de endeudamientos financieros comprendidos en el punto 3.5»)
- Preguntas EV2 que citan O o algún d: ninguna

### C30 — `ext::7.11.1.4` → {ext::7.11.1.2, ext::7.11.1.3}

- Texto Ordenado de O: `ext`
- O = `ext::7.11.1.4` — 63 palabras
  - fragmento E0 `ext::7.11.1.4` (punto_terminal; campo `texto`):

````text
7.11.1.4. Préstamos financieros otorgados por los acreedores referidos en los puntos
7.11.1.2. y 7.11.1.3. que son liquidados en el mercado de cambios y que
simultáneamente fueron utilizados para concretar pagos anticipados, a la
vista y/o diferidos de importaciones de bienes al proveedor del exterior y/o
al proveedor de servicios de fletes de importaciones de bienes no incluidos
en su condición de compra pactada.
````

- d = `ext::7.11.1.2` — 96 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ext::7.11.1.2` (punto_terminal; campo `texto`):

````text
7.11.1.2. Financiaciones comerciales por la importación de bienes donde los
desembolsos en divisas se aplicaron, neto de gastos, directa e
íntegramente a pagos anticipados, a la vista y/o diferidos al proveedor del
exterior y/o a pagos en forma directa al proveedor de servicios de fletes de
importaciones de bienes no incluidos en su condición de compra pactada,
que hayan sido otorgados por:
i) una entidad financiera del exterior o agencia oficial de crédito a la
exportación del exterior.
ii) una entidad financiera local a partir de una línea de crédito de una
entidad financiera del exterior.
````

  - aristas de remisión resuelta O → d: 4
    - [Obligacion] «Aplicación de divisas de cobros de exportación — préstamos financieros» → [Operacion] «Financiaciones comerciales — importación de bienes» (destino `ext::7.11.1.2`; evidencia «préstamos financieros otorgados por acreedores referidos en puntos 7.11.1.2 y 7.11.1.3, liquidados en merc»)
    - [Obligacion] «Aplicación de divisas de cobros de exportación — préstamos financieros» → [Restriccion] «Otorgamiento por entidad financiera del exterior o agencia oficial» (destino `ext::7.11.1.2`; evidencia «préstamos financieros otorgados por acreedores referidos en puntos 7.11.1.2 y 7.11.1.3, liquidados en merc»)
    - [Obligacion] «Aplicación de divisas de cobros de exportación — préstamos financieros» → [Restriccion] «Otorgamiento por entidad financiera local con línea del exterior» (destino `ext::7.11.1.2`; evidencia «préstamos financieros otorgados por acreedores referidos en puntos 7.11.1.2 y 7.11.1.3, liquidados en merc»)
    - [Obligacion] «Aplicación de divisas de cobros de exportación — préstamos financieros» → [Restriccion] «Desembolsos netos aplicados a pagos anticipados/a la vista/diferidos» (destino `ext::7.11.1.2`; evidencia «préstamos financieros otorgados por acreedores referidos en puntos 7.11.1.2 y 7.11.1.3, liquidados en merc»)
- d = `ext::7.11.1.3` — 61 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ext::7.11.1.3` (punto_terminal; campo `texto`):

````text
7.11.1.3. Préstamos financieros otorgados por contrapartes vinculadas al cliente en
los cuales los desembolsos en divisas se aplicaron directa e íntegramente
a pagos anticipados, a la vista y/o diferidos de importaciones de bienes al
proveedor del exterior y/o a pagos en forma directa al proveedor de
servicios de fletes de importaciones de bienes no incluidos en su condición
de compra pactada.
````

  - aristas de remisión resuelta O → d: 2
    - [Obligacion] «Aplicación de divisas de cobros de exportación — préstamos financieros» → [Operacion] «Préstamos financieros de contrapartes vinculadas» (destino `ext::7.11.1.3`; evidencia «préstamos financieros otorgados por acreedores referidos en puntos 7.11.1.2 y 7.11.1.3, liquidados en merc»)
    - [Obligacion] «Aplicación de divisas de cobros de exportación — préstamos financieros» → [Restriccion] «Desembolsos — aplicación directa e íntegra a pagos» (destino `ext::7.11.1.3`; evidencia «préstamos financieros otorgados por acreedores referidos en puntos 7.11.1.2 y 7.11.1.3, liquidados en merc»)
- Preguntas EV2 que citan O o algún d: ninguna

### C31 — `ext::8.1` → {ext::8.5.17, ext::8.5.17.26}

- Texto Ordenado de O: `ext`
- O = `ext::8.1` — 75 palabras
  - fragmento E0 `ext::8.1` (punto_terminal; campo `texto`):

````text
8.1. Operaciones comprendidas.
Este seguimiento comprende a todas las exportaciones de bienes cuya oficialización se haya
concretado a partir del 02/09/19 y que hayan obtenido el pertinente cumplido de embarque
aduanero, excepto las operaciones aduaneras que se detallan en el punto 8.5.17.
Independientemente de que una exportación sea considerada como exceptuada del
seguimiento, si el exportador recibiera cobros por tal exportación, éstos también se
encontrarán alcanzados por la obligación de ingreso y liquidación de divisas.
````

- d = `ext::8.5.17` — 18 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ext::8.5.17::intro` (mini_chunk, rol_bloque intro; campo `texto`):

````text
Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
siguiente listado de operaciones:
````

  - aristas de remisión resuelta O → d: 4
    - [Excepcion] «Operaciones aduaneras exceptuadas — punto 8.5.17» → [Excepcion] «Excepción del seguimiento — operaciones BARA/VMI1 combustibles» (destino `ext::8.5.17`; evidencia «Operaciones aduaneras exceptuadas — punto 8.5.17 | excepto las opera»)
    - [Excepcion] «Operaciones aduaneras exceptuadas — punto 8.5.17» → [Excepcion] «Ventajas aduaneras — operaciones exceptuadas» (destino `ext::8.5.17`; evidencia «Operaciones aduaneras exceptuadas — punto 8.5.17 | excepto las opera»)
    - [Excepcion] «Operaciones aduaneras exceptuadas — punto 8.5.17» → [Operacion] «Seguimiento operaciones aduaneras» (destino `ext::8.5.17`; evidencia «Operaciones aduaneras exceptuadas — punto 8.5.17 | excepto las opera»)
    - [Excepcion] «Operaciones aduaneras exceptuadas — punto 8.5.17» → [Restriccion] «Seguimiento de operaciones aduaneras excepto exportaciones a Área aduanera especial» (destino `ext::8.5.17`; evidencia «Operaciones aduaneras exceptuadas — punto 8.5.17 | excepto las opera»; procedencias del nodo destino: `ext::8.5.17`, `ext::8.5.17.26`)
- d = `ext::8.5.17.26` — 35 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ext::8.5.17.26` (punto_terminal; campo `texto`):

````text
8.5.17.26. Las exportaciones de efectos personales que hacen a la profesión u oficio
de personas humanas que fijan su residencia en el exterior en la medida
que dichas operaciones hayan sido autorizadas por la Aduana.
````

  - d entra a D solo por procedencia múltiple del nodo destino (ninguna arista O → d tiene `destino` = d)
  - aristas de remisión resuelta O → d: 1
    - [Excepcion] «Operaciones aduaneras exceptuadas — punto 8.5.17» → [Restriccion] «Seguimiento de operaciones aduaneras excepto exportaciones a Área aduanera especial» (destino `ext::8.5.17`; evidencia «Operaciones aduaneras exceptuadas — punto 8.5.17 | excepto las opera»; procedencias del nodo destino: `ext::8.5.17`, `ext::8.5.17.26`)
- Preguntas EV2 que citan O o algún d: ninguna

### C32 — `ext::8.5.13.4` → {ext::6.6}

- Texto Ordenado de O: `ext`
- O = `ext::8.5.13.4` — 23 palabras
  - fragmento E0 `ext::8.5.13.4` (punto_terminal; campo `texto`):

````text
8.5.13.4. el exportador y el importador no estén vinculados en forma directa o
indirecta de acuerdo con lo previsto en el punto 6.6.
````

- d = `ext::6.6` — 44 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ext::6.6` (punto_terminal; campo `texto`):

````text
6.6. Operaciones con contrapartes vinculadas.
Se considerarán operaciones con contrapartes vinculadas a aquellas en las que participan un
residente y una contraparte que mantienen entre ellos los tipos de relaciones descriptos en el
punto 1.2.2. de las normas “Grandes exposiciones al riesgo de crédito”.
````

  - aristas de remisión resuelta O → d: 1
    - [Restriccion] «No vinculación directa o indirecta — exportador e importador» → [Operacion] «Operaciones con contrapartes vinculadas» (destino `ext::6.6`; evidencia «forma directa o indirecta de acuerdo con lo previsto en el punto 6.6»)
- Preguntas EV2 que citan O o algún d: ninguna

### C33 — `ext::9.1.8` → {ext::7.11}

- Texto Ordenado de O: `ext`
- O = `ext::9.1.8` — 22 palabras
  - fragmento E0 `ext::9.1.8` (punto_terminal; campo `texto`):

````text
9.1.8. Financiaciones asociadas a importaciones de bienes habilitadas para la aplicación de
cobros de exportaciones de bienes contempladas en el punto 7.11.
````

- d = `ext::7.11` — 4 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ext::7.11::intro` (mini_chunk, rol_bloque intro; campo `texto`):

````text
de exportaciones de bienes.
````

  - aristas de remisión resuelta O → d: 2
    - [Operacion] «Cobros de exportaciones de bienes (punto 7.11)» → [Obligacion] «Habilitación de financiaciones de importaciones para cobros» (destino `ext::7.11`; evidencia «Cobros de exportaciones de bienes (punto 7.11)»)
    - [Operacion] «Cobros de exportaciones de bienes (punto 7.11)» → [Operacion] «Financiaciones asociadas a importaciones — cobros de exportaciones» (destino `ext::7.11`; evidencia «Cobros de exportaciones de bienes (punto 7.11)»)
- Preguntas EV2 que citan O o algún d: ninguna

### C34 — `ext::10.10.1` → {ext::10.6.6}

- Texto Ordenado de O: `ext`
- O = `ext::10.10.1` — 74 palabras
  - fragmento E0 `ext::10.10.1` (punto_terminal; campo `texto`):

````text
10.10.1. Plazos para pagos diferidos de importaciones de bienes con registro de ingreso
aduanero a partir del 13/12/23.
Las entidades podrán dar acceso al mercado de cambios para cursar pagos
diferidos de importaciones de bienes con registro de ingreso aduanero a partir del
13/12/23 desde la fecha de registro de ingreso aduanero, en la medida que se
trate de operaciones no comprendidas en el punto 10.6.6. y se verifiquen los
restantes requisitos normativos aplicables.
````

- d = `ext::10.6.6` — 59 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ext::10.6.6::intro` (mini_chunk, rol_bloque intro; campo `texto`):

````text
de soja excluidos p/siembra).
Las entidades para otorgar acceso al mercado de cambios para el pago de
importaciones temporales de la posición arancelaria 1201.90.00 de la NCM (porotos
de soja excluidos p/siembra) con registro de ingreso aduanero a partir del 13/12/23,
adicionalmente a los restantes requisitos normativos aplicables, deberán verificar que
el cliente por el monto que pretende abonar:
````

  - aristas de remisión resuelta O → d: 6
    - [Obligacion] «Acceso mercado cambios — pagos diferidos importaciones» → [Obligacion] «Verificación cliente — pago importación temporal porotos» (destino `ext::10.6.6`; evidencia «la medida que se trate de operaciones no comprendidas en el punto 10.6.6. y se verifiquen los»)
    - [Obligacion] «Acceso mercado cambios — pagos diferidos importaciones» → [Operacion] «Acceso al mercado de cambios importación temporaria NCM 1201.90.00» (destino `ext::10.6.6`; evidencia «la medida que se trate de operaciones no comprendidas en el punto 10.6.6. y se verifiquen los»)
    - [Obligacion] «Acceso mercado cambios — pagos diferidos importaciones» → [Operacion] «Pago importación temporal porotos de soja (NCM 1201.90.00)» (destino `ext::10.6.6`; evidencia «la medida que se trate de operaciones no comprendidas en el punto 10.6.6. y se verifiquen los»)
    - [Restriccion] «Exclusión operaciones punto 10.6.6 — pagos diferidos» → [Obligacion] «Verificación cliente — pago importación temporal porotos» (destino `ext::10.6.6`; evidencia «Exclusión operaciones punto 10.6.6 — pagos diferidos |»)
    - [Restriccion] «Exclusión operaciones punto 10.6.6 — pagos diferidos» → [Operacion] «Acceso al mercado de cambios importación temporaria NCM 1201.90.00» (destino `ext::10.6.6`; evidencia «Exclusión operaciones punto 10.6.6 — pagos diferidos |»)
    - [Restriccion] «Exclusión operaciones punto 10.6.6 — pagos diferidos» → [Operacion] «Pago importación temporal porotos de soja (NCM 1201.90.00)» (destino `ext::10.6.6`; evidencia «Exclusión operaciones punto 10.6.6 — pagos diferidos |»)
- Preguntas EV2 que citan O o algún d: ninguna

### C35 — `ext::10.10.2.6` → {ext::7.11}

- Texto Ordenado de O: `ext`
- O = `ext::10.10.2.6` — 19 palabras
  - fragmento E0 `ext::10.10.2.6` (punto_terminal; campo `texto`):

````text
10.10.2.6. Se trata de un pago de importaciones de bienes enmarcado en el
mecanismo previsto en el punto 7.11.
````

- d = `ext::7.11` — 4 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ext::7.11::intro` (mini_chunk, rol_bloque intro; campo `texto`):

````text
de exportaciones de bienes.
````

  - aristas de remisión resuelta O → d: 2
    - [Restriccion] «Condición: pago enmarcado en mecanismo punto 7.11» → [Obligacion] «Habilitación de financiaciones de importaciones para cobros» (destino `ext::7.11`; evidencia «Condición: pago enmarcado en mecanismo punto 7.11 | Se trata de un pa»)
    - [Restriccion] «Condición: pago enmarcado en mecanismo punto 7.11» → [Operacion] «Financiaciones asociadas a importaciones — cobros de exportaciones» (destino `ext::7.11`; evidencia «Condición: pago enmarcado en mecanismo punto 7.11 | Se trata de un pa»)
- Preguntas EV2 que citan O o algún d: ninguna

### C36 — `ext::11.1.1.11` → {ext::7.11}

- Texto Ordenado de O: `ext`
- O = `ext::11.1.1.11` — 43 palabras
  - fragmento E0 `ext::11.1.1.11` (punto_terminal; campo `texto`):

````text
11.1.1.11. Emitir a pedido del importador certificaciones con el detalle
correspondiente para que la entidad encargada del “Seguimiento de
anticipos y otras financiaciones de exportación de bienes” pueda
convalidar la aplicación de divisas en el marco del mecanismo dispuesto
en el punto 7.11.
````

- d = `ext::7.11` — 4 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ext::7.11::intro` (mini_chunk, rol_bloque intro; campo `texto`):

````text
de exportaciones de bienes.
````

  - aristas de remisión resuelta O → d: 2
    - [Obligacion] «Emitir certificaciones a pedido del importador» → [Obligacion] «Habilitación de financiaciones de importaciones para cobros» (destino `ext::7.11`; evidencia «cación de divisas en el marco del mecanismo dispuesto en el punto 7.11»)
    - [Obligacion] «Emitir certificaciones a pedido del importador» → [Operacion] «Financiaciones asociadas a importaciones — cobros de exportaciones» (destino `ext::7.11`; evidencia «cación de divisas en el marco del mecanismo dispuesto en el punto 7.11»)
- Preguntas EV2 que citan O o algún d: ninguna

### C37 — `ext::13.3.4` → {ext::7.11}

- Texto Ordenado de O: `ext`
- O = `ext::13.3.4` — 19 palabras
  - fragmento E0 `ext::13.3.4` (punto_terminal; campo `texto`):

````text
13.3.4. Se trata de un pago de importaciones de servicios enmarcado en el
mecanismo previsto en el punto 7.11.
````

- d = `ext::7.11` — 4 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ext::7.11::intro` (mini_chunk, rol_bloque intro; campo `texto`):

````text
de exportaciones de bienes.
````

  - aristas de remisión resuelta O → d: 2
    - [Obligacion] «Encuadre en mecanismo punto 7.11» → [Obligacion] «Habilitación de financiaciones de importaciones para cobros» (destino `ext::7.11`; evidencia «Encuadre en mecanismo punto 7.11 | Se trata de un pa»)
    - [Obligacion] «Encuadre en mecanismo punto 7.11» → [Operacion] «Financiaciones asociadas a importaciones — cobros de exportaciones» (destino `ext::7.11`; evidencia «Encuadre en mecanismo punto 7.11 | Se trata de un pa»)
- Preguntas EV2 que citan O o algún d: ninguna

### C38 — `ext::14.3.2` → {ext::3.5}

- Texto Ordenado de O: `ext`
- O = `ext::14.3.2` — 71 palabras
  - fragmento E0 `ext::14.3.2` (punto_terminal; campo `texto`):

````text
14.3.2. Se admite en los términos previstos en el punto 7.9.5. que los fondos originados en
el cobro de exportaciones de bienes y servicios por parte de un VPU adherido, que
se encuentran alcanzados por la obligación de ingreso y liquidación en el mercado
de cambios, sean acumulados en cuentas del exterior y/o del país destinadas a
garantizar la cancelación de los vencimientos de los endeudamientos comprendidos
en el punto 3.5.
````

- d = `ext::3.5` — 61 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ext::3.5::intro` (mini_chunk, rol_bloque intro; campo `texto`):

````text
exterior.
Las entidades podrán dar acceso al mercado de cambios para realizar pagos de capital o
intereses de títulos de deuda con registro público en el exterior, otros endeudamientos
financieros con el exterior y títulos de deuda con registro público en el país denominados en
moneda extranjera íntegramente suscriptos en el exterior, en la medida que se verifiquen las
siguientes condiciones:
````

  - aristas de remisión resuelta O → d: 8
    - [Excepcion] «Acumulación de fondos para garantizar cancelación de endeudamientos» → [Obligacion] «Acceso mercado cambios pagos deuda» (destino `ext::3.5`; evidencia «e los vencimientos de los endeudamientos comprendidos en el punto 3.5»)
    - [Excepcion] «Acumulación de fondos para garantizar cancelación de endeudamientos» → [Operacion] «Endeudamientos financieros exterior» (destino `ext::3.5`; evidencia «e los vencimientos de los endeudamientos comprendidos en el punto 3.5»)
    - [Excepcion] «Acumulación de fondos para garantizar cancelación de endeudamientos» → [Operacion] «Pago títulos deuda y endeudamientos» (destino `ext::3.5`; evidencia «e los vencimientos de los endeudamientos comprendidos en el punto 3.5»)
    - [Excepcion] «Acumulación de fondos para garantizar cancelación de endeudamientos» → [Operacion] «Pago títulos deuda y endeudamientos exterior» (destino `ext::3.5`; evidencia «e los vencimientos de los endeudamientos comprendidos en el punto 3.5»)
    - [Excepcion] «Acumulación de fondos para garantizar cancelación de endeudamientos» → [Operacion] «Pagos de endeudamientos financieros» (destino `ext::3.5`; evidencia «e los vencimientos de los endeudamientos comprendidos en el punto 3.5»)
    - [Excepcion] «Acumulación de fondos para garantizar cancelación de endeudamientos» → [Operacion] «Pagos de títulos deuda exterior» (destino `ext::3.5`; evidencia «e los vencimientos de los endeudamientos comprendidos en el punto 3.5»)
    - [Excepcion] «Acumulación de fondos para garantizar cancelación de endeudamientos» → [Operacion] «Pagos intereses títulos deuda exterior» (destino `ext::3.5`; evidencia «e los vencimientos de los endeudamientos comprendidos en el punto 3.5»)
    - [Excepcion] «Acumulación de fondos para garantizar cancelación de endeudamientos» → [Operacion] «Pagos títulos deuda país moneda extranjera» (destino `ext::3.5`; evidencia «e los vencimientos de los endeudamientos comprendidos en el punto 3.5»)
- Preguntas EV2 que citan O o algún d: ninguna

### C39 — `pro::3.2.3.8` → {pro::3.1.5}

- Texto Ordenado de O: `pro`
- O = `pro::3.2.3.8` — 21 palabras
  - fragmento E0 `pro::3.2.3.8` (punto_terminal; campo `texto`):

````text
3.2.3.8. El Registro de Denuncias ante las Instancias Judiciales y/o Administrativas de
Defensa del Consumidor (RDJA) establecido en el punto 3.1.5.
````

- d = `pro::3.1.5` — 58 palabras — mismo Texto Ordenado que O
  - fragmento E0 `pro::3.1.5` (punto_terminal; campo `texto`):

````text
3.1.5. Registro de Denuncias ante las Instancias Judiciales y/o Administrativas de Defensa del
Consumidor (RDJA).
En este registro se asentarán todas las intervenciones originadas en denuncias efec-
tuadas ante instancias judiciales y/o administrativas de defensa del consumidor, identi-
ficando al usuario afectado y especificando el importe involucrado, la causal generado-
ra del evento, los productos y casas involucradas.
````

  - aristas de remisión resuelta O → d: 2
    - [Obligacion] «Registro denuncias instancias judiciales administrativas» → [Obligacion] «Registro de denuncias judiciales y administrativas» (destino `pro::3.1.5`; evidencia «trativas de Defensa del Consumidor (RDJA) establecido en el punto 3.1.5.»)
    - [Obligacion] «Registro denuncias instancias judiciales administrativas» → [Operacion] «Denuncias ante instancias judiciales y administrativas» (destino `pro::3.1.5`; evidencia «trativas de Defensa del Consumidor (RDJA) establecido en el punto 3.1.5.»)
- Preguntas EV2 que citan O o algún d: ninguna

### C40 — `ric::4.1.1.2` → {cap::6.2.1}

- Texto Ordenado de O: `ric`
- O = `ric::4.1.1.2` — 42 palabras
  - fragmento E0 `ric::4.1.1.2` (punto_terminal; campo `texto`):

````text
4.1.1.2. Código 311100/xx
Se consignará el valor de la exigencia por riesgo específico de tasa de interés para
el último día del período (n) determinada conforme a las disposiciones del punto
6.2.1. de las normas sobre “Capitales mínimos de las entidades financieras”.
````

- d = `cap::6.2.1` — 50 palabras — otro Texto Ordenado (`cap`)
  - fragmento E0 `cap::6.2.1::intro` (mini_chunk, rol_bloque intro; campo `texto`):

````text
La exigencia de capital por riesgo específico tiene por objeto proteger a la entidad ante
movimientos adversos en el precio de un título causados por factores relacionados con
su emisor. Para su cálculo, sólo se permitirá netear las posiciones opuestas respecto de
una misma especie, incluidas las posiciones en derivados.
````

  - aristas de remisión resuelta O → d: 2
    - [Obligacion] «Consignación exigencia riesgo específico tasa interés» → [Obligacion] «Cálculo de capital — riesgo específico» (destino `cap::6.2.1`; evidencia «punto 6.2.1. de las normas sobre 'Capitales mínimos de las entidades financieras»)
    - [Obligacion] «Consignación exigencia riesgo específico tasa interés» → [Operacion] «Cálculo de capital por riesgo específico» (destino `cap::6.2.1`; evidencia «punto 6.2.1. de las normas sobre 'Capitales mínimos de las entidades financieras»)
- Preguntas EV2 que citan O o algún d: ninguna

### C41 — `ric::4.1.1.7` → {cap::6.4}

- Texto Ordenado de O: `ric`
- O = `ric::4.1.1.7` — 41 palabras
  - fragmento E0 `ric::4.1.1.7` (punto_terminal; campo `texto`):

````text
4.1.1.7. Código 313000/xx
Se consignará el valor de la exigencia por riesgo de tipo de cambio para el último
día del período (n) determinada conforme a las disposiciones del punto 6.4. de las
normas sobre “Capitales mínimos de las entidades financieras”.
````

- d = `cap::6.4` — 22 palabras — otro Texto Ordenado (`cap`)
  - fragmento E0 `cap::6.4::intro` (mini_chunk, rol_bloque intro; campo `texto`):

````text
El presente punto establece el capital mínimo necesario para cubrir el riesgo de mantener po-
siciones en moneda extranjera, incluido el oro.
````

  - aristas de remisión resuelta O → d: 1
    - [Obligacion] «Consignación exigencia riesgo tipo cambio» → [Obligacion] «Capital mínimo — riesgo de tipo de cambio» (destino `cap::6.4`; evidencia «punto 6.4. de las normas sobre "Capitales mínimos de las entidades financieras»)
- Preguntas EV2 que citan O o algún d: ninguna

### C42 — `ric::10.1.2` → {ric::1.2}

- Texto Ordenado de O: `ric`
- O = `ric::10.1.2` — 43 palabras
  - fragmento E0 `ric::10.1.2` (punto_terminal; campo `texto`):

````text
10.1.2. Ratio de apalancamiento
Surgirá de aplicar la expresión prevista en el punto 1.2. de las citadas normas:
Ratio de apalancamiento = [Medida del capital / Medida de la exposición] * 100 =
[PNb / ∑ Códigos (45110000 a 45140000)] * 100
(CN1)
````

- d = `ric::1.2` — 87 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ric::1.2` (punto_terminal; campo `texto`):

````text
1.2. Los importes se registrarán en miles de pesos, sin decimales.
A los fines del redondeo de las magnitudes se incrementarán los valores en una unidad
cuando el primer dígito de las fracciones sea igual o mayor que 5, desechando estas últimas
si resultan inferiores.
Los importes en moneda extranjera se convertirán a pesos utilizando el tipo de cambio de re-
ferencia publicado por el BCRA para el dólar estadounidense, previa aplicación del tipo de
pase correspondiente para las otras monedas comunicado por la Mesa de Operaciones.
````

  - aristas de remisión resuelta O → d: 3
    - [Obligacion] «Aplicar expresión Ratio apalancamiento punto 1.2» → [Obligacion] «Redondeo de magnitudes según dígito fraccional» (destino `ric::1.2`; evidencia «Aplicar expresión Ratio apalancamiento punto 1.2 | Surgirá de aplica»)
    - [Obligacion] «Aplicar expresión Ratio apalancamiento punto 1.2» → [Obligacion] «Conversión importes moneda extranjera a pesos» (destino `ric::1.2`; evidencia «Aplicar expresión Ratio apalancamiento punto 1.2 | Surgirá de aplica»)
    - [Obligacion] «Aplicar expresión Ratio apalancamiento punto 1.2» → [Obligacion] «Registrar importes en miles de pesos sin decimales» (destino `ric::1.2`; evidencia «Aplicar expresión Ratio apalancamiento punto 1.2 | Surgirá de aplica»)
- Preguntas EV2 que citan O o algún d: ninguna

---

## REFERENCIA (no es candidato salvo que figure arriba): `ext::3.17.1.4` → {ext::3.4.1, ext::3.4.2, ext::3.4.3}

- Criterios con el D fijado por el mandato:
  - 1 (arista resuelta O→cada d): cumple — aristas por d: {'ext::3.4.1': 1, 'ext::3.4.2': 3, 'ext::3.4.3': 2}
  - 2 (|D| entre 1 y 3): cumple — |D| = 3
  - 3 (sin ancestro/descendiente en el mismo TO): cumple
  - 4 (O ≤ 80, cada d ≤ 120 palabras): cumple — {'O': 25, 'ext::3.4.1': 11, 'ext::3.4.2': 71, 'ext::3.4.3': 34}
  - 5 (ningún d con remisión saliente): cumple — puntos de D con remisión saliente: []
- D(O) completo según el grafo (todos los puntos alcanzados desde `ext::3.17.1.4`): ['ext::3.4.1', 'ext::3.4.2', 'ext::3.4.3', 'ext::9.3.12.2', 'ext::9.3.12.3'] (5 puntos)
  - `ext::9.3.12.2` (fuera del D fijado) — 71 palabras; aristas O → d:
    - [Restriccion] «Requisitos puntos 3.4.1 a 3.4.3 — utilidades dividendos» → [Obligacion] «Declaración jurada representante legal» (destino `ext::3.4.2`; procedencias del nodo destino: `ext::3.4.2`, `ext::9.3.12.2`)
  - `ext::9.3.12.3` (fuera del D fijado) — 34 palabras; aristas O → d:
    - [Restriccion] «Requisitos puntos 3.4.1 a 3.4.3 — utilidades dividendos» → [Obligacion] «Verificación de cumplimiento declaración de activos y pasivos externos» (destino `ext::3.4.3`; procedencias del nodo destino: `ext::3.4.3`, `ext::9.3.12.3`)
- Con D = D(O) completo (5 puntos) el par no pasa el criterio 2; por eso no figura entre los candidatos.
- Nota: preguntas EV2 cuyo ancla es ancestro de O en la numeración (no cuenta como cita exacta): ['EV2F-013']

- Texto Ordenado de O: `ext`
- O = `ext::3.17.1.4` — 25 palabras
  - fragmento E0 `ext::3.17.1.4` (punto_terminal; campo `texto`):

````text
3.17.1.4. Pagos de utilidades y dividendos a accionistas no residentes en la medida
que se verifiquen los requisitos previstos en los puntos 3.4.1. a 3.4.3.
````

- d = `ext::3.4.1` — 11 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ext::3.4.1` (punto_terminal; campo `texto`):

````text
3.4.1. Las utilidades y dividendos correspondan a balances cerrados y auditados.
````

  - aristas de remisión resuelta O → d: 1
    - [Restriccion] «Requisitos puntos 3.4.1 a 3.4.3 — utilidades dividendos» → [Obligacion] «Balances cerrados y auditados» (destino `ext::3.4.1`; evidencia «Requisitos puntos 3.4.1 a 3.4.3 — utilidades divide»; procedencias del nodo origen: `ext::3.17.1.4`, `ext::3.18.1.2`)
- d = `ext::3.4.2` — 71 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ext::3.4.2` (punto_terminal; campo `texto`):

````text
3.4.2. El monto total abonado por este concepto a accionistas no residentes, incluido el pago
cuyo curso se está solicitando, no supere el monto en moneda local que les
corresponda según la distribución determinada por la asamblea de accionistas.
La entidad deberá contar con una declaración jurada firmada por el representante legal
de la empresa residente o un apoderado con facultades suficientes para asumir este
compromiso en nombre de la empresa.
````

  - aristas de remisión resuelta O → d: 3
    - [Restriccion] «Requisitos puntos 3.4.1 a 3.4.3 — utilidades dividendos» → [Obligacion] «Declaración jurada representante legal» (destino `ext::3.4.2`; evidencia «Requisitos puntos 3.4.1 a 3.4.3 — utilidades divide»; procedencias del nodo origen: `ext::3.17.1.4`, `ext::3.18.1.2`; procedencias del nodo destino: `ext::3.4.2`, `ext::9.3.12.2`)
    - [Restriccion] «Requisitos puntos 3.4.1 a 3.4.3 — utilidades dividendos» → [Operacion] «Giro divisas utilidades dividendos exterior» (destino `ext::3.4.2`; evidencia «Requisitos puntos 3.4.1 a 3.4.3 — utilidades divide»; procedencias del nodo origen: `ext::3.17.1.4`, `ext::3.18.1.2`)
    - [Restriccion] «Requisitos puntos 3.4.1 a 3.4.3 — utilidades dividendos» → [Restriccion] «Monto total no supere distribución asamblea» (destino `ext::3.4.2`; evidencia «Requisitos puntos 3.4.1 a 3.4.3 — utilidades divide»; procedencias del nodo origen: `ext::3.17.1.4`, `ext::3.18.1.2`)
- d = `ext::3.4.3` — 34 palabras — mismo Texto Ordenado que O
  - fragmento E0 `ext::3.4.3` (punto_terminal; campo `texto`):

````text
3.4.3. La entidad deberá verificar que el cliente haya dado cumplimiento en caso de
corresponder, a la declaración de la última presentación vencida del “Relevamiento de
activos y pasivos externos” por las operaciones involucradas.
````

  - aristas de remisión resuelta O → d: 2
    - [Restriccion] «Requisitos puntos 3.4.1 a 3.4.3 — utilidades dividendos» → [Obligacion] «Verificación de cumplimiento declaración de activos y pasivos externos» (destino `ext::3.4.3`; evidencia «Requisitos puntos 3.4.1 a 3.4.3 — utilidades divide»; procedencias del nodo origen: `ext::3.17.1.4`, `ext::3.18.1.2`; procedencias del nodo destino: `ext::3.4.3`, `ext::9.3.12.3`)
    - [Restriccion] «Requisitos puntos 3.4.1 a 3.4.3 — utilidades dividendos» → [Operacion] «Giro de utilidades y dividendos al exterior» (destino `ext::3.4.3`; evidencia «Requisitos puntos 3.4.1 a 3.4.3 — utilidades divide»; procedencias del nodo origen: `ext::3.17.1.4`, `ext::3.18.1.2`)
- Preguntas EV2 que citan O o algún d: ninguna

