# Laudo de cierre U-B5.4 — Verificación pareada del catálogo v3, adjudicada

**Estado: FIRMADO — Agustina Videla Rivero, 06/09/2026**, con las cuatro
resoluciones de §3 asentadas en cada hallazgo y la transcripción de las
nueve fichas VERIFICADA por la autora (releídas contra el archivo; las
marcas y notas reflejan su adjudicación). Insumos: predicciones selladas por
`f19e978` (semilla `b54-pareada-v1`), corrida 34/34 (USD 0,2902 de tope
0,50; remanente 0,2098), comparación mecánica re-corrida por la instancia
del plan (25 PASA / 3 FICHA / 6 NO_CUMPLE, 0 violaciones cross-TO), y la
**adjudicación de la autora de las 9 fichas** (06/09), transcripta
verbatim en `fichas_pareada_b54.md` con registro de transcripción (las
casillas del archivo estaban vacías al recibir el mensaje de
adjudicación; la autora verifica la transcripción con esta firma). Tally
de marcas recomputado contra el archivo: **6 correcto-v3 (f. 1, 2, 3, 5,
6, 9) · 1 correcto-antes (f. 4) · 2 otro (f. 7, 8)**.

## §1. Resultado global — queda registrado así (insumo del capítulo y de tanda 1)

1. **La predicción central de A2 se cumplió entera: brazo B 8/8** — las
   ocho unidades que bajo el congelado usaban roles de TOs dev ajenos
   emitieron su id propio, y **cero** emisiones de rol cross-TO en las 34
   unidades (predicción global). El mecanismo resolvió el único defecto
   de sujetos medido en datos reales.
2. **La resolución de PSTV es correcta por primera vez en tres
   iteraciones** (f. 3 y 5): en dos lecturas ESQ había caído en ids de
   pagos; con el rol de alcance cae en el sujeto correcto.
3. **La anti-atracción del BCRA funciona** (f. 1 y 8: el regulador deja
   de figurar como sujeto alcanzado).
4. Adjudicación semántica: 6/9 mejor el v3, 1/9 mejor el antes, 2/9
   mixtas — con los dos patrones transversales de la autora que §3
   trata por separado: el mecanismo corrigió una succión (BCRA) e
   introdujo otra (el rol de alcance), y la válvula de propuestos se
   está cerrando de más (las dos pérdidas son sujetos que debían quedar
   propuestos y desaparecieron, no ids mal elegidos).

## §2. Cierre económico

USD 0,2902 real (estimación anclada 0,26–0,36; tope 0,50). Remanente
disponible para los retests de §3: USD 0,2098.

## §3. Los cuatro hallazgos, POR SEPARADO (opciones · costos · recomendación · resolución)

**H1 — Violación mecánica de la guarda del originante** (f. 2,
`cap::3.1.14::intro`: el originante de securitización emitido con el id
`Sujeto_entidad_originante` — definido para el circuito de pagos — pese a
la cláusula «NO es el originante de una securitización»). La marca semántica
correcto-v3 no lo debilita: es hallazgo de proceso — el id se usó fuera
de su definición.
- (a) **RENOMBRAR el id a dominio inequívoco de pagos**
  (`Sujeto_entidad_originante_de_transferencia`), def y guarda intactas;
  el originante de securitización pasa a resolver por la válvula.
  Costo: ~5 líneas + re-sello (sha nuevo, selftest) + retest dirigido de
  la unidad adversarial con predicción sellada (~USD 0,01).
  **Recomendación de mesa: esta** — la superficie léxica del id es el
  mecanismo de la atracción; el precedente de la escalera dice que el
  refuerzo declarativo solo no alcanza.
- (b) Reforzar la definición (segunda iteración de lenguaje). Costo
  similar; desaconsejada por ese mismo precedente.
- (c) Aceptar residuo declarado + vigilancia con tasa en tanda 1. USD 0;
  en tensión con el principio de gobierno (uso estructurado fuera de
  definición en material fresco).
- **RESOLUCIÓN DE LA AUTORA: (a) — rename a
  `Sujeto_entidad_originante_de_transferencia`.**

**H2 — Atracción del rol de alcance como ejecutor** (f. 4, `cryl::1.3`:
`rol_alcance_cryl` en `ejecuta` sin apoyo en el texto — el reverso de la
anti-atracción del BCRA; n=1 en esta muestra).
- (a) **Guarda en la línea de alcance del mensaje por chunk** («el rol es
  el sujeto de `aplica_a` cuando la norma se dirige al colectivo; NO es
  ejecutor por defecto en `ejecuta`»). Toca el template del user message
  (código de la unidad, NO el prefijo → sha intacto, sin re-sello) +
  retest dirigido de `cryl::1.3` (~USD 0,01). **Recomendación de mesa:
  esta, sumada a (c)** — barata, no rota nada, y la tasa de tanda 1
  verifica si alcanzó.
- (b) Reforzar la def posicional del rol. Mismo caveat declarativo.
- (c) Solo vigilancia de tanda 1 **con tasa** (roles en `ejecuta` sin
  verbo de acción del colectivo en la unidad). USD 0; defendible con
  n=1.
- **RESOLUCIÓN DE LA AUTORA: (a) + (c) — guarda en la línea de alcance
  del mensaje Y vigilancia (7) con tasa en tanda 1.**

**H3 — La válvula de propuestos se cierra de más** (f. 7: BIS y «otros
soberanos» desaparecidos en vez de propuestos; f. 2: «inversores y
tenedores» reducido). Es pérdida de la conducta correcta ya medida
(cryl::8.1); las dos pérdidas de las nueve fichas son de este tipo.
- (a) Instrucción de válvula reforzada (línea en el bloque v3 →
  re-sello; o en el mensaje → sin re-sello). No verificable con n=2 sin
  gastar; mismo precedente declarativo.
- (b) **Vigilancia de tanda 1 con TASA y umbral pre-declarado**: tasa de
  `sujeto_propuesto` del v3 contra la línea base medida (3,1 % de las
  relaciones con sujeto, U-SUJ-FREQ); si cae por debajo del umbral que
  el mandato de tanda 1 selle, se activa el refuerzo (a) dentro de la
  ventana. USD 0 ahora, n=6.340 después. **Recomendación de mesa: esta**
  — con 6.340 unidades la tasa mide de verdad lo que n=2 solo sugiere.
  El caso de promoción de BIS ya está documentado y esta evidencia lo
  engrosa.
- **RESOLUCIÓN DE LA AUTORA: (b) — vigilancia (8) con tasa contra la
  base 3,1 % y umbral pre-declarado en el mandato de B6.1.**

**H4 — Mis-resolución puntual** (f. 8, `ayccef::2.1`:
`Sujeto_sector_publico_no_financiero` para entidades que van a operar
como entidades financieras públicas — contradice el término que
resuelve).
- (a) **Definición dirigida por la cláusula de F1.3** (firmada en el
  laudo de fase 1: «si la pareada muestra confusión en un id sin
  definición, se le escribe definición en esa misma iteración»). El caso
  la activa literalmente: def para `sector_publico_no_financiero` («NO
  incluye entidades financieras públicas ni entidades autorizadas a
  operar como tales»). Costo: líneas en el bloque v3 → re-sello
  (compartido con H1 si va (a)) + retest dirigido de `ayccef::2.1`
  (~USD 0,01). **Recomendación de mesa: esta — es la cláusula ya firmada
  aplicándose.**
- (b) Solo vigilancia. Deja la cláusula firmada sin ejecutar ante su
  primer caso.
- **RESOLUCIÓN DE LA AUTORA: (a) — definición dirigida por la cláusula
  F1.3 («mi cláusula, su primer caso»).**

## §4. Mini-ciclo consolidado (si las resoluciones activan cambios)

Si van H1(a) + H4(a) [+ H2(a)]: **UN solo re-sello** (sha nuevo, selftest
completo re-corrido con checks nuevos, composición recomputada por regla
i — el rename no cambia el conteo de 102) + **retests dirigidos** de las
unidades adversariales afectadas (`cap::3.1.14::intro`, `ayccef::2.1`
[, `cryl::1.3`]) con predicciones selladas ANTES en documento propio;
costo total ≈ USD 0,02–0,03 del remanente 0,2098; freno exprés (sha +
selftest + resultados de retests). El cierre definitivo de la unidad y su
commit ocurren sobre ese freno verificado.

## §5. Efectos del cierre (cuando §4 esté en verde, o de inmediato si todo va a vigilancia)

1. Fila B5.4 del plan → CERRADA, con el resultado global de §1
   registrado (8/8, 0 cross-TO, PSTV, adjudicación 6/1/2).
2. **Vigilancias nuevas de tanda 1** (se suman a las seis vigentes, con
   tasa y muestreo a definir en el mandato de B6.1): (7) roles de
   alcance en `ejecuta` sin apoyo textual; (8) tasa de `sujeto_propuesto`
   contra la base 3,1 % con umbral pre-declarado.
3. El catálogo v3 sellado queda listo para el **cableado a producción**
   (unidad propia, post-B5.3 ya cerrada; nota de integración del campo
   `rol_id` vigente).
4. El caso de promoción de BIS se engrosa con la f. 7 (el ejecutor lo
   asienta en el artefacto del catálogo en el mini-ciclo).

## §6. Resultado del mini-ciclo y LAUDO FINAL (06/09, posterior al freno exprés)

El mini-ciclo se ejecutó (re-sello `35e88c2d…`/hash `54a111e2175f`,
selftest 57/57 desde cwd ajeno, composición 102 recomputada; retests con
predicciones selladas pre-corrida, sha `553007f5…`; USD 0,0512 — total de
la unidad **USD 0,3414 de 0,50**). Resultados: **R2 (def dirigida de
`sector_publico_no_financiero`): PASA 3/3** — la cláusula F1.3 funcionó
en su primer caso. **R1 (rename) y R3 (guarda del mensaje): FALLAN sus
predicciones**, y el ejecutor frenó sin iterar, como mandaba este laudo.

**LAUDO FINAL de los dos fallos:**

- **R1 = residuo declarado + VIGILANCIA (9)** (emisiones de
  `entidad_originante_de_transferencia` fuera del dominio de pagos, con
  muestreo y tasa en la tanda 1). Fundamento: segunda cláusula del
  principio de gobierno (error con tasa a medir), balance favorable de
  cobertura legítima (**13 menciones / 5 TOs del id `originante` en el
  censo de adiciones de fase 1** — cifra recomputada por regla i; el 44
  es de `entidad_girada`), mejora direccional medida (2→1 emisiones en
  la unidad adversarial, con la válvula recuperando los propuestos), y
  two-strikes que prohíbe la tercera iteración de lenguaje. Si la tasa
  de tanda 1 es mala, el destino es retiro a r2 con caso de promoción.
- **R3 = la guarda del mensaje SE CONSERVA** (inocua; con constancia
  honesta en el catálogo de que NO mostró efecto en el caso medido —
  tercera confirmación del patrón de la escalera) **+ la vigilancia (7)
  como instrumento**. La **cuarentena determinística en el validador**
  (flag de rol-en-`ejecuta` para revisión, no prohibición) queda
  registrada como CANDIDATA, activable solo si la tasa de tanda 1 la
  justifica, con laudo en la ventana.

**Con este laudo final, U-B5.4 CIERRA — sin más mini-ciclos.** El
catálogo v3 sellado (`35e88c2d…`/`54a111e2175f`) es el que se cablea a
producción (unidad propia).

## Firma

**Firma: Agustina Videla Rivero · Fecha: 06/09/2026** — resoluciones:
H1(a) · H2(a)+(c) · H3(b) · H4(a). El mini-ciclo de §4 queda activado
(re-sello único + 3 retests dirigidos: `cap::3.1.14::intro`,
`ayccef::2.1`, `cryl::1.3`, con predicciones selladas antes de correr,
bajo el remanente USD 0,2098); el cierre de la unidad y su commit
ocurren sobre el freno exprés verificado.

**Firma del laudo final (§6): Agustina Videla Rivero · Fecha:
06/09/2026.**
