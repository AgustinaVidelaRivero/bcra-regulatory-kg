# Registro de generación — Tanda 0 (fase 2b)

Fecha de generación: 2026-09-27.
Salida: `preguntas_tanda0.json` (20 preguntas, ids T0F-001 a T0F-020) y `validacion.json`.

## 1. Fuentes leídas

Se leyeron exclusivamente los archivos de la carpeta `material_tanda0_preguntas/`.
No se consultó ningún repositorio, grafo, base de datos, conversación previa ni red.
El texto de cada PDF se extrajo con `pdftotext -layout pdfs/<to>.pdf -` (poppler 26.06.0).

sha256 declarados en `manifest.txt` (verificados localmente con `shasum -a 256`; todos coinciden):

```
9802d4effca8d1933e498fc01e73d4620ac5d6a01081d84a6eb34670bdf85c7f  README.md
5060a73f07b50266d2582afc0d8f49e25524658f5a8aba3e1f439546c9896a13  orden_semillado_ctacte.json
4ec76333531d7d609a3cf767acd7584ff222a4dcd62f3604fefa386b4466e1ff  orden_semillado_docvig.json
52521663ecdc46e0270fb53d90b7df9d13397140a160700b2a2146184f5449aa  orden_semillado_lingob.json
d3bd41a4d1228984e86778e0676354fdf77f09343866f118ace6fb8c3bd7d1c6  orden_semillado_pagjub.json
f3bfb86c37997a0b36c76a441bddf1eebdcc65d7662cbb2091e865d8237df026  orden_semillado_polcre.json
06969a2cafb898a7eee888fb524271947290006bc0824b4d50e62fc4bd465a3f  pdfs/ctacte.pdf
d2d8a0d39d69be8f99eac8aab243142fea370108aa15ad0db3879480f83afb61  pdfs/docvig.pdf
e3c7d7b3e689e8e9ebf67da6e3f29498718f5e4ab7bf5b56f50bc8813a6ab3b0  pdfs/lingob.pdf
908445f273415d29780d19a86e19fddb7d6d75c541b381ef66eb48776474d997  pdfs/pagjub.pdf
7b94ea5d8d5f99baacfff7787bf11f94cba23cc0d406261bdcb2764edd409b04  pdfs/polcre.pdf
4a85104353bbb97676ac000bdf38304b6bad085c7efdc0ab8309451deb6cf7de  plantilla_salida.json
cb5d98edc0dd40e37b8cc9720a7f48f119644e9c411fe0859f350765ae0a8e55  unidades_ctacte.json
34cc48a583075e2ba8e9d67c293297ef96ded3afb21f27e0852df49cb69afc2f  unidades_docvig.json
31e1953a3f51769161abf3df3142dcb6a806ed0f1cba87e7766a1fa7004b4291  unidades_lingob.json
5f1e321e2dd612d2d2b610f20435f87e14a09a91312a03fd801d599ed7a49dfc  unidades_pagjub.json
dce6fab628b909b1207de5ed106166e4a3e091df8b503703f85e83a3f99a1370  unidades_polcre.json
5a4033cfd61d695fcfd6626d58ade119c21473f72393433cca18ddcaca6bade2  validar_anclas_tanda0.py
```

sha256 del propio `manifest.txt` (no se lista a sí mismo): `b3b5a82f6a4c2f4668398a15b5665733d23bafb53224842940f5a2187f482361`.

Los índices `unidades_<to>.json` declaran `fuente_indice` = "e0_dry (PROVISIONAL ...)" en los cinco
documentos; conforme al README, la re-verificación contra el índice definitivo no corresponde a la
instancia generadora.

## 2. Procedimiento y semilla

- Procedimiento: README.md de la carpeta (EV2 §1 y §4 adaptados). Cuotas: 20 preguntas, 4 por
  documento, al menos una de varios puntos por documento, exactamente dos abstenciones en total.
- Semilla: `20260927-<to>`; orden de selección tomado de `orden_semillado_<to>.json`
  (`random.Random(f"20260927-{to}").sample(disponibles, len(disponibles))`, disponibles en el orden
  del índice). No hay territorio quemado.
- Regla aplicada: se toman las primeras unidades usables del orden como ancla principal de cada
  pregunta; para «varios puntos», la segunda ancla es la siguiente unidad usable del orden que
  efectivamente aporta el contenido que exige algún criterio (se indica cuál y por qué se saltan
  las intermedias). Una unidad consumida como segunda ancla cuenta como usada.
- Abstenciones (2): lingob (T0F-008) y pagjub (T0F-013). Antes de redactarlas se verificó el
  silencio normativo en el texto completo del PDF (ver §6).
- Citas: copiadas literalmente del texto de `pdftotext -layout`. Los cortes de línea con guion del
  PDF se reproducen tal como quedan tras normalizar espacios (por ejemplo «re- gularizar»,
  «Valo- res S.A.»), porque el validador compara subcadenas del texto normalizado.

## 3. Orden semillado: primeras posiciones por documento, unidades usadas y descartadas

Unidades descartadas por contenido: **ninguna**. Ninguna de las unidades alcanzadas resultó
índice sin texto normativo, tabla pura ni remisión vacía, con una salvedad tratada como precisión
a subpunto (pagjub 2.8, ver §4). Las unidades de texto breve se consideraron usables porque su
texto es normativo (un documento válido listado, una buena práctica del Directorio, un contenido
obligatorio de un aviso, una obligación contractual, un motivo de rechazo).

### ctacte — Reglamentación de la cuenta corriente bancaria

| pos. | unidad | uso |
|---|---|---|
| 1 | 4.5.1 | T0F-001, ancla 1 (varios puntos) |
| 2 | 10.2.3.1 | T0F-002 (dato directo) |
| 3 | 1.5.1.12 | T0F-003 (dato directo) |
| 4 | 5.5.8 | T0F-004 (dato directo) |
| 5 | 2.3.1 | no usada: cuota del documento cubierta; no aporta el contenido exigido por T0F-001 |
| 6 | 10.2.2 | no usada: ídem |
| 7 | 5.1.1 | T0F-001, ancla 2: siguiente unidad del orden que aporta el contenido exigido por los criterios 3 y 4 (excepción al límite de endosos por depósito en Caja de Valores y cláusula «... para su negociación en mercados de valores») |
| 8 | 2.4 | no alcanzada |

### lingob — Lineamientos para el gobierno societario en entidades financieras.

| pos. | unidad | uso |
|---|---|---|
| 1 | 5.2 | T0F-005 (dato directo) |
| 2 | 5.1.2 | T0F-006 (dato directo; el ancla comprende sus subpuntos 5.1.2.1 a 5.1.2.4) |
| 3 | 7.1.10 | T0F-007, ancla 1 (varios puntos) |
| 4 | 7.1.5 | T0F-007, ancla 2: siguiente unidad usable del orden; aporta el contenido exigido por el criterio 3 (política de conducta / código de ética) |
| 5 | 2.1.2 | T0F-008 (abstención: la norma no fija periodicidad para el monitoreo del perfil de riesgo) |
| 6 | 2.4.5 | no usada: cuota cubierta |
| 7 | 2.1.5 | no alcanzada |
| 8 | 4.2.4 | no alcanzada |

### polcre — Política de crédito

| pos. | unidad | uso |
|---|---|---|
| 1 | 2.1.16 | T0F-009 (dato directo) |
| 2 | 6.2.1.5 | T0F-010 (dato directo) |
| 3 | 2.5 | T0F-011, ancla 1 (varios puntos) |
| 4 | 5.4 | T0F-012 (dato directo) |
| 5 | 1.2 | no usada: cuota cubierta; no aporta el contenido exigido por el criterio 4 de T0F-011 |
| 6 | S10 | T0F-011, ancla 2: siguiente unidad del orden que aporta el contenido exigido por el criterio 4 (depósitos de la Cuenta Especial de Regularización de Activos en monedas distintas del dólar) |
| 7 | 2.1.11 | no alcanzada |
| 8 | 6.2.2 | no alcanzada |

### pagjub — Pago de beneficios de la seg. soc. por cuenta de la Adm. Nacional de la Seguridad Social (ANSES)

| pos. | unidad | uso |
|---|---|---|
| 1 | 1.2 | T0F-013 (abstención: la norma no fija tiempo máximo de espera en caja) |
| 2 | 2.7.5 | T0F-014 (dato directo) |
| 3 | 3.2.1.1 | T0F-015, ancla 1 (varios puntos) |
| 4 | 2.8 | T0F-016 (dato directo), precisada al subpunto 2.8.1 (ver §4) |
| 5 | 2.8.1.1 | subsumida en el ancla 2.8.1 de T0F-016 (es su subpunto); no aporta el contenido exigido por el criterio 3 de T0F-015 |
| 6 | 3.2.1.3 | T0F-015, ancla 2: siguiente unidad del orden que aporta el contenido exigido por el criterio 3 (retiros de fondos de las cuentas especiales) |
| 7 | 2.10 | no alcanzada |
| 8 | 2.8.3.1 | no alcanzada |

### docvig — Documentos de identificación en vigencia

| pos. | unidad | uso |
|---|---|---|
| 1 | 1.2.2 | T0F-017, ancla 1 (varios puntos) |
| 2 | 3.1.2 | T0F-018 (dato directo) |
| 3 | 2.1.3 | T0F-019 (dato directo) |
| 4 | 1.2.3 | T0F-017, ancla 2: siguiente unidad usable del orden que aporta el contenido exigido por el criterio 2 (DNI manual o digital para el mismo grupo); 3.1.2 y 2.1.3 no lo aportan |
| 5 | 3.3.1 | T0F-020 (dato directo) |
| 6 | 2.1.1.1 | no usada: cuota cubierta |
| 7 | 2.2.3 | no alcanzada |
| 8 | 3.5 | no alcanzada |

Resolución de anclas y posición semillada según `validacion.json`:

- T0F-001 [ctacte, varios puntos]: ctacte:4.5.1 (pos. 1, exacta), ctacte:5.1.1 (pos. 7, exacta)
- T0F-002 [ctacte, dato directo]: ctacte:10.2.3.1 (pos. 2, exacta)
- T0F-003 [ctacte, dato directo]: ctacte:1.5.1.12 (pos. 3, exacta)
- T0F-004 [ctacte, dato directo]: ctacte:5.5.8 (pos. 4, exacta)
- T0F-005 [lingob, dato directo]: lingob:5.2 (pos. 1, exacta)
- T0F-006 [lingob, dato directo]: lingob:5.1.2 (pos. 2, exacta)
- T0F-007 [lingob, varios puntos]: lingob:7.1.10 (pos. 3, exacta), lingob:7.1.5 (pos. 4, exacta)
- T0F-008 [lingob, abstención]: lingob:2.1.2 (pos. 5, exacta)
- T0F-009 [polcre, dato directo]: polcre:2.1.16 (pos. 1, exacta)
- T0F-010 [polcre, dato directo]: polcre:6.2.1.5 (pos. 2, exacta)
- T0F-011 [polcre, varios puntos]: polcre:2.5 (pos. 3, exacta), polcre:S10 (pos. 6, exacta)
- T0F-012 [polcre, dato directo]: polcre:5.4 (pos. 4, exacta)
- T0F-013 [pagjub, abstención]: pagjub:1.2 (pos. 1, exacta)
- T0F-014 [pagjub, dato directo]: pagjub:2.7.5 (pos. 2, exacta)
- T0F-015 [pagjub, varios puntos]: pagjub:3.2.1.1 (pos. 3, exacta), pagjub:3.2.1.3 (pos. 6, exacta)
- T0F-016 [pagjub, dato directo]: pagjub:2.8.1 (pos. 26, exacta)
- T0F-017 [docvig, varios puntos]: docvig:1.2.2 (pos. 1, exacta), docvig:1.2.3 (pos. 4, exacta)
- T0F-018 [docvig, dato directo]: docvig:3.1.2 (pos. 2, exacta)
- T0F-019 [docvig, dato directo]: docvig:2.1.3 (pos. 3, exacta)
- T0F-020 [docvig, dato directo]: docvig:3.3.1 (pos. 5, exacta)

## 4. Precisiones a subpunto

- pagjub, unidad semillada **2.8** (pos. 4, «[bloque intro] Liquidación de la rendición de cuentas»):
  su texto propio es una sola oración introductoria («... se describen a continuación:») sin contenido
  normativo autónomo. En lugar de descartarla, el ancla se precisó al subpunto pertinente **2.8.1**
  (presentación realizada y aceptada hasta el vencimiento del período de presentación y sin
  inconsistencias), que es unidad del índice y comprende 2.8.1.1 y 2.8.1.2. Ancla final: `pagjub:2.8.1`
  (T0F-016). Unidad de origen: 2.8.
- No hubo otras precisiones. Los anclas «[bloque intro]» ctacte 4.5.1 y lingob 5.1.2 se mantuvieron en
  la unidad semillada porque el punto ancla comprende sus subpuntos y la pregunta versa sobre el
  conjunto.

## 5. Observaciones pre-declaradas

Se declaran acá, antes de cualquier evaluación, los criterios que exceden lo que la pregunta elicita
o que se apoyan en texto adyacente al punto ancla.

- **T0F-001** (ctacte, varios puntos): pregunta compuesta (recaudos del girado + cómputo del endoso
  para el límite). Los criterios 1 y 2 se satisfacen con 4.5.1 (subpuntos 4.5.1.1 y 4.5.1.2); los
  criterios 3 y 4 exigen contenido de 5.1.1 (pos. 7). La cláusula citada en el criterio 4 contiene los
  tres puntos suspensivos tal como figuran en el PDF («“... para su negociación en mercados de valores”»).
- **T0F-002** y **T0F-014**: solo dos criterios, porque el texto de la unidad (10.2.3.1; 2.7.5) no
  sostiene más sin salir del punto ancla. En T0F-014 el carácter «total» del rechazo y la posibilidad
  de volver a presentar figuran en el punto 2.7 (intro, pos. 18) y no se exigen.
- **T0F-003**: la unidad 1.5.1.12 es un ítem de la lista «Obligaciones del cuentacorrentista» (1.5.1),
  encabezado que el índice no lista como unidad; el encuadre lo aporta la pregunta, no un criterio.
- **T0F-005** (lingob 5.2): el texto de `pdftotext` contiene espacios espurios dentro de algunas
  palabras de este punto («f inanciera», «hac e», «facultade s», «le gislación»); las citas se eligieron
  evitando esos fragmentos. Un criterio adicional sobre qué hace la función de cumplimiento (monitoreo
  del cumplimiento de reglas y regulaciones, reporte de desvíos) se consideró y no se incluyó por
  exceder lo que la pregunta elicita.
- **T0F-008** (lingob, abstención): el criterio 3 es negativo (no atribuir a la norma una frecuencia).
  Se anticipa la confusión posible con 2.1.1, que prevé evaluar «anualmente» el código de gobierno
  societario, y con 2.1.11/2.1.12 («con regularidad», reuniones con la Alta Gerencia y con auditores
  internos): ninguno fija periodicidad para el monitoreo del perfil de riesgo.
- **T0F-009** (polcre 2.1.16): el encuadre «aplicación de la capacidad de préstamo de depósitos en
  moneda extranjera» proviene del párrafo introductorio del punto 2.1 (unidad 2.1, pos. 19) y lo
  aporta la pregunta; los tres criterios se satisfacen con el texto de 2.1.16. No se exigen las
  condiciones generales del punto 2.2 (capacidad de pago, escenarios de tipo de cambio).
- **T0F-011** (polcre, varios puntos): los criterios 1 a 3 se satisfacen con 2.5; el criterio 4 exige
  el contenido de la Sección 10 (S10). El ejemplo «euros» de la pregunta es una instancia de «monedas
  extranjeras distintas al dólar estadounidense».
- **T0F-012** (polcre 5.4): los criterios 2 y 3 mencionan las remisiones a otras normas
  («Evaluaciones crediticias», «Afectación de activos en garantía») tal como el ancla las enuncia;
  no exigen el contenido remitido (interpretación v2).
- **T0F-013** (pagjub, abstención): el criterio 3 (horario de atención al público en general y
  horarios especiales adicionales) es contexto del mismo punto 1.2 que excede la pregunta literal
  sobre tiempo de espera; se incluye porque una respuesta completa lo menciona al explicar qué sí
  prevé el texto. La cláusula residual del punto 1.6 («regirá lo que establezca la ANSES») no se exige.
- **T0F-016** (pagjub 2.8.1): la cita del criterio 1 («El BCRA, en el mismo día de la aceptación,
  procederá a:») aparece con idéntico texto en 2.8.1 a 2.8.4; la del criterio 2 aparece igual en
  2.8.1.1 y 2.8.3.1. El ancla es 2.8.1; el validador solo verifica subcadena en el PDF.
- **T0F-017** (docvig, varios puntos): el criterio 3 cita el encabezado del punto padre 1.2 («Mayores
  de 75 años al 31.12.14 y los incapaces declarados judicialmente»), que el índice no lista como
  unidad propia (sí sus subpuntos 1.2.1 a 1.2.3). La pregunta ya enuncia el grupo; el criterio solo
  verifica que la respuesta vincule la validez con ese grupo y no con el régimen general de hasta 75
  años (1.1). La unidad 1.2.2 se consideró usable: su texto es el documento válido listado.
- **T0F-018** (docvig 3.1.2): el criterio 3 (el supuesto comprende también la resolución
  administrativa) completa lo que la pregunta, que menciona solo una resolución judicial, elicita en
  forma parcial.
- **T0F-019** (docvig 2.1.3): el criterio 3 se apoya en el párrafo de cierre del punto 2.1 («En todos
  los casos deberá acreditarse la categoría de residencia...»), que sigue inmediatamente a 2.1.3 en el
  texto y no es un subpunto numerado de 2.1.3; la pregunta lo elicita expresamente. En el criterio 2,
  la aclaración «caso de menos de un año de otorgada la residencia» reproduce el título del punto
  2.1.2 (no es unidad del índice); una respuesta que indique que la regla cede y aplica otro punto de
  la norma satisface el criterio (interpretación v2 de remisión).
- **T0F-020** (docvig 3.3.1): sin observaciones; los tres criterios están en el texto de 3.3.1.

## 6. Verificación de los silencios normativos (abstenciones)

- lingob (T0F-008): búsqueda en el texto completo de «perfil de riesgo», «anualmente», «periódic»,
  «regularidad», «frecuencia». Las menciones de periodicidad (2.1.1 «anualmente»; 2.1.11 y 2.1.12
  «con regularidad»; 1.4.3 y 7.2.3.6 «periódicamente»/«periódica») no se refieren al monitoreo del
  perfil de riesgo por el Directorio. 2.1.2 es la única disposición sobre ese monitoreo y no fija
  periodicidad.
- pagjub (T0F-013): búsqueda en el texto completo de «espera», «minuto», «demora», «prioridad»,
  «cajas», «trato». Solo el punto 1.2 trata la atención en caja (acceso a todas las cajas, trato
  diferencial, prioridad ante no clientes); no hay tiempo máximo de espera en ningún punto.

## 7. Salida del validador (pegada íntegra)

Comando:

```
python3 validar_anclas_tanda0.py . preguntas_tanda0.json --pdfs pdfs --salida validacion.json
```

Código de salida: 0.

stdout:

```
   T0F-001 ctacte  varios puntos  apto        
   T0F-002 ctacte  dato directo   apto        
   T0F-003 ctacte  dato directo   apto        
   T0F-004 ctacte  dato directo   apto        
   T0F-005 lingob  dato directo   apto        
   T0F-006 lingob  dato directo   apto        
   T0F-007 lingob  varios puntos  apto        
   T0F-008 lingob  abstención     apto        
   T0F-009 polcre  dato directo   apto        
   T0F-010 polcre  dato directo   apto        
   T0F-011 polcre  varios puntos  apto        
   T0F-012 polcre  dato directo   apto        
   T0F-013 pagjub  abstención     apto        
   T0F-014 pagjub  dato directo   apto        
   T0F-015 pagjub  varios puntos  apto        
   T0F-016 pagjub  dato directo   apto        
   T0F-017 docvig  varios puntos  apto        
   T0F-018 docvig  dato directo   apto        
   T0F-019 docvig  dato directo   apto        
   T0F-020 docvig  dato directo   apto        
cuotas: {"total": 20, "total_esperado": 20, "abstenciones": 2, "abstenciones_esperadas": 2, "por_to": {"ctacte": {"n": 4, "varios_puntos": 1, "ok": true}, "lingob": {"n": 4, "varios_puntos": 1, "ok": true}, "polcre": {"n": 4, "varios_puntos": 1, "ok": true}, "pagjub": {"n": 4, "varios_puntos": 1, "ok": true}, "docvig": {"n": 4, "varios_puntos": 1, "ok": true}}, "ok": true}
aptas 20 / descartadas 0 / cuotas OK
```

stderr: vacío (el validador captura internamente la salida de `pdftotext`; los avisos de poppler
«Syntax Error ... insufficient arguments for Marked Content» que emite `pdftotext` al extraer algunos
PDF no afectan el texto extraído ni la verificación).

## 8. Verificación adicional de estructura

`preguntas_tanda0.json` reproduce exactamente las claves y el orden de `plantilla_salida.json` en el
nivel superior (`set`, `fecha_generacion`, `procedimiento`, `semilla`, `dosificacion`, `cuotas`,
`preguntas`) y por pregunta (`id`, `to`, `to_nombre`, `pregunta`, `tipo_previsto`, `gold.ancla`,
`gold.criterios[].{criterio, cita_textual}`). `to_nombre` es el `titulo_oficial` de cada
`unidades_<to>.json`. Ninguna pregunta contiene números de punto (el validador no emitió el aviso
`pregunta_con_numero_de_punto`).

Conteo: ctacte 4 (1 varios puntos, 3 dato directo); lingob 4 (1 varios puntos, 1 abstención, 2 dato
directo); polcre 4 (1 varios puntos, 3 dato directo); pagjub 4 (1 varios puntos, 1 abstención, 2 dato
directo); docvig 4 (1 varios puntos, 3 dato directo). Total: 13 dato directo, 5 varios puntos,
2 abstención.
