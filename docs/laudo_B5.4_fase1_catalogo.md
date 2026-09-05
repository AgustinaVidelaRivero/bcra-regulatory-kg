# Laudo U-B5.4 fase 1 — Mecanismo de rol, definiciones, adiciones y podas del catálogo de sujetos v3

**Estado: FIRMADO — Agustina Videla Rivero, 05/09/2026** (redactado por la
instancia del plan sobre los laudos dictados por la autora en la revisión
del freno 1, con revisión de mesa). Gobierna la fase 2 de U-B5.4, que
queda AUTORIZADA con esta firma. Insumos: paquete de
revisión del freno 1 (`revision_UB54_f1/`, 12 artefactos + manifest,
verificado por la instancia del plan contra repo y contra recomputo
propio), mandato de U-B5.4 (Rama B del laudo
`docs/laudo_B5.5_alcance_corpus_y_catalogo.md`, firmado 04/09), diseño
`docs/diseno_B5.4_catalogo_sujetos_v3.md` (sellado `74202e3`).

## F1.2 — Mecanismo de rol de alcance: OPCIÓN A2

**Se adopta A2**: id de rol nuevo SOLO donde el alcance del TO no es una
clase exacta del catálogo (**31 ids de rol nuevos**), y mapeo directo
`ROL_POR_TO` → clase existente para los **35 TOs** cuyo pasaje de alcance
nombra exactamente una o dos clases del catálogo (adjudicación fila por
fila con cita verbatim en `tabla_to_rol_post_f1.md` — esa tabla es la
guarda del mapeo). Los **2 huecos** (docvig, fimipyme) quedan **SIN rol
por defecto**: sin entrada en `ROL_POR_TO`, con la válvula
`sujeto_propuesto` abierta, y re-mirada en la tanda 1.

*Fundamento registrado*: el costo monetario no separa las opciones
(< USD 2/corrida todas); separa la **superficie de atracción**, y la
atracción entre roles es la única medida en datos reales (emisiones
cross-TO de roles dev en unidades de ESQ-2 — hallazgo del freno 1,
consistente con la tabla de U-SUJ-FREQ). A1 agregaba 35 ids que duplican
semánticamente clases existentes: 35 atractores sin ganancia, porque donde
el alcance ES la clase no hay matiz que preservar. **Constancia de mesa**:
la mesa adopta A2 cediendo su preferencia previa por A1 — el argumento de
superficie medida es superior al de homogeneidad. La **opción B** (id
deíctico resuelto en ensamblado) queda registrada como **candidata de
ensamblado post-B5.3**, fuera de esta unidad.

## F1.3 — Definiciones positivas: cobertura DIRIGIDA, 24 ids

Se adopta la cobertura dirigida de `definiciones_positivas_post_f1.md`
(24 ids: uso alto + confusiones medidas + vecindades; delta recomputado
+1.164 tokens ≈ +USD 0,75/corrida). **Cláusula**: si la verificación
pareada de la fase 3 muestra confusión en un id sin definición, se le
escribe definición en esa misma iteración, con el delta declarado.

## F1.4 — Adiciones documentales

- **ENTRAN** (evidencia citada en `adiciones_0_3_post_f1.md`): los 4
  roles del SNP (`entidad_girada` 44 menciones/4 TOs, `depositaria`,
  `receptora`, `originante` — con la guarda anti-atracción contra el
  «originante» de securitización), `banco_central_del_exterior` y `fmi`.
- **NO ENTRA `bis`**: evidencia débil declarada por el propio freno
  (1 mención como contraparte + 1 como autor de estándares + n=2 dev).
  Queda con **caso de promoción documentado** en el artefacto del
  catálogo.
- **ENMIENDA DE ALCANCE DE LA AUTORA, declarada**: se amplía la lista
  cerrada del mandato para incluir **CEC** (Cámaras Electrónicas de
  Compensación; 33 menciones / 12 TOs — la evidencia supera a ítems de la
  lista original; rige el principio de que la evidencia manda). La
  enmienda es de la autora, no del ejecutor: el ejecutor la reportó fuera
  de lista y no la agregó, que era la conducta correcta.
- **CCP: duplicado reportado, sin acción** (ya existe
  `Sujeto_entidad_de_contraparte_central`; las 41 menciones/10 TOs
  confirman demanda del id existente).

## F1.5 — Los 14 ids sin uso: 9 MANTENER / 5 RETIRAR

Se adopta la recomendación por id de `ids_sin_uso_post_f1.md`:

- **MANTENER (9)**, con **marca explícita de revisión en r2** para los dos
  débiles (`ministerio_de_economia`, `sociedad_de_proposito_especial`).
- **RETIRAR (5)**: `acreedor_del_exterior`,
  `autoridad_nacional_de_aplicacion` y las tres secretarías (energía,
  comercio, transporte — 0 menciones en los 68, verificado además por
  recomputo independiente de la instancia del plan). Cada retiro con
  **lápida** en el artefacto del catálogo v3 (id, evidencia de no-uso,
  fecha y este laudo), como todo lo que sale.

## Composición esperada del catálogo v3 (referencia; el ejecutor la recomputa)

70 vigentes − 5 retiros + 31 roles A2 + 7 adiciones (4 SNP +
banco_central_del_exterior + fmi + CEC) = **103 ids**. Regla i del
circuito: la fase 2 recomputa esta suma contra el artefacto construido y
cualquier diferencia se reporta como hallazgo, no se ajusta en silencio.

## Correcciones menores mandadas a la fase 2 (del freno de revisión)

1. **Reproducibilidad**: los scripts del paquete deben correr desde
   cualquier cwd (sin auto-referencia rota) y **sin rutas absolutas
   embebidas** (hoy llevan el nombre de usuario del filesystem); nombres
   de script consistentes entre artefactos.
2. **Atribución**: los rótulos de los artefactos distinguen «lectura del
   ejecutor» (sus recomendaciones), «verificación de la instancia del
   plan» (recomputos en disco) y «mesa revisora» (firma aparte). El
   rótulo «Lectura de la mesa» del artefacto de la pregunta central se
   corrige a «Lectura del ejecutor».
3. **Hueco fimipyme como hallazgo de pipeline**: la familia «sección del
   índice sin unidad E0» (unidad propia vacía) se asienta como ítem de
   vigilancia de la tanda 1 en el plan (lo ejecuta la instancia del plan,
   no el ejecutor), medible con el health-check de B5.2
   (`healthcheck_e0.py`).

## Efectos de la firma

1. **Fase 2 AUTORIZADA** (materialización del prefijo v3 en módulo propio
   + selftest de byte-identidad fuera del bloque de catálogo y del enum +
   predicciones de la pareada SELLADAS + estimación anclada). La fase 3
   sigue gateada al freno 2, tope USD 0,50.
2. Las fronteras del mandato siguen intactas (call-site de producción:
   B5.3; docs/tesis: U-CAP-ESQ; el cableado a producción no es de esta
   unidad).

## Firma

**Firma: Agustina Videla Rivero · Fecha: 05/09/2026.**
