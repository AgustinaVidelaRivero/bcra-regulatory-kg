# Enmienda 4 al protocolo entre tandas — cómo crece el catálogo de sujetos y cuándo se lee el alcance de un documento nuevo

**BORRADOR — PENDIENTE DE FIRMA** · Redactada: 2026-10-04.

Enmienda con fecha al protocolo entre tandas (`docs/protocolo_entre_tandas.md`, FIRMADO en `a304b89`; texto
firmado: las primeras 398 líneas, sha256 `b23d37c5396a…`). El protocolo no se edita: esta enmienda vive al lado
y se lee junto con él, con la enmienda sobre la cola humana (`8d01b04`), la enmienda 2 (`0b98045`) y la
enmienda 3 (`0cb0c70`, con su §3 en `bd77541`).

No rige hasta la firma. Se firma cuando R2 de U-RERESOL-CAT deje el script de re-resolución funcionando, con su
prueba (enmienda 2, punto 3).

---

## 0. Qué enmienda y por qué

- **Lo que dice el protocolo.** No fija cómo crece el catálogo de sujetos durante el escalado, ni cuándo se
  decide el alcance de un documento nuevo. La enmienda 2 pone una sola condición: que exista, con su prueba, el
  script que re-resuelve y rehace el grafo.
- **Lo que hay hoy.**
  - De los 157 documentos, 86 no tienen entrada de alcance (`docs/plan_tesis.md:404`). Sin entrada, el mensaje
    de E1 no lleva la línea de alcance.
  - R1 de U-RERESOL-CAT (`data/experiment/reresolucion_catalogo/freno_r1.md`, `c98093a`) diseñó dos catálogos:
    el del request, fijo por release, y el de resolución, que lee el código y puede crecer entre tandas. Con
    esa separación, un alta no cambia ningún request.
  - En el registro de KG-Tanda0-Diez-r2a hay 27 filas en cuarentena con la mención verificada, en 18 claves.
    Dos claves llegan a 2 unidades, las dos en cap; ninguna llega a 3 (`salidas/r1_medicion.json`, clave
    `frecuencias`).
- **Por qué una enmienda.** Agrega dos reglas, una con umbral, a un texto firmado. El mandato de U-RERESOL-CAT
  ya lo preveía: hasta que esta enmienda se firme, ninguna de las dos rige
  (`docs/mandatos/URERESOL_CAT_reresolucion_catalogo.md`, primera nota del 04/10/2026).

## 1. La regla de crecimiento del catálogo

1. **Dos fuentes.** Las entradas nuevas salen de:
   - el alcance de los documentos nuevos, antes de su extracción (§2);
   - la cuarentena, al cierre de cada tanda.
2. **Umbral, para la cuarentena.** Una clave es candidata cuando su mención verificada está en cuarentena en
   al menos 2 unidades distintas del registro acumulado. El número se confirma o se recalibra con el registro
   de U-REEXT-T0, antes de la firma.
3. **Lectura y aprobación.** Cada candidata se lee contra el texto (lectura asistida, declarada) y entra solo
   con la aprobación de la autora, como alias de un id que ya existe o como id nuevo con su padre.
4. **Solo al catálogo de resolución.** El catálogo del request no cambia entre tandas: ni el bloque del
   prefijo, ni el enum, ni el tool schema. Lo agregado actúa por las reglas, sobre la mención guardada; el
   modelo no lo sugiere (L-ESQ-R2 §7, `4ef7650:862-864`).
5. **Después corre el script de re-resolución** (enmienda 2): re-resuelve el registro, rehace el grafo desde el
   crudo guardado a USD 0 y lo verifica. El reporte de la tanda dice cuántas relaciones resolvió cada versión
   del catálogo.
6. **Límites.**
   - Una mención que no verifica nunca resuelve por crecimiento.
   - En la release siguiente, las ampliaciones pasan al catálogo del request.

## 2. El paso de lectura del alcance, antes de cada tanda

1. **Cuándo.** Antes de la primera extracción de cada tanda, para cada documento de la tanda que no tenga
   entrada de alcance.
2. **Cómo.** Con el método del laudo de B5.4 (`docs/laudo_B5.4_fase1_catalogo.md:15-20`, `dea56ba`): se lee el
   pasaje de alcance del documento y se cita textual.
3. **Solo clases que ya existen.** Si el pasaje nombra exactamente una o dos clases del catálogo, el documento
   recibe esa entrada de clase. Cambia solo el mensaje de sus unidades: el de toda unidad ya extraída sale
   byte a byte igual, y se controla.
4. **Si no.** Un documento sin pasaje de alcance, o que necesite un rol nuevo, entra sin línea de alcance,
   declarado. Su rol se decide en la release que corresponda. Mientras tanto, lo que el texto no identifica va
   a cuarentena, como fije la enmienda 6 a L-ESQ-R2 cuando se firme.
5. **Quién decide.** La lectura es asistida y declarada. La aprueba la autora, documento por documento, antes
   de extraer.
6. **Costo.** La lectura se hace sin API. Si una tanda la hace con la API, su tope es de USD [A FIJAR por la
   autora] por tanda, y se declara antes de correr.

## 3. Qué falta para que se pueda aplicar

- **El script de re-resolución,** con su prueba: R2 de U-RERESOL-CAT.
- **El registro de alcance por tanda.** Las entradas de clase de los documentos nuevos no pueden ir a
  `catalogo_sujetos_r2.json` sin romper sus candados. R1 propone un registro que solo agrega, leído junto con
  el de la release (`freno_r1.md`, §4). Toca `e1_extractor/prompt_r2b.py` y está sin implementar: lo hace una
  unidad a definir, antes de la tanda 1.

## 4. Qué no cambia

- El texto del protocolo, sus notas y sus enmiendas anteriores.
- El catálogo de sujetos de r2 y sus candados: esta enmienda no agrega ningún id ni ningún alcance.
- El criterio de admisión de ids de L-ESQ-R2 §7 (`4ef7650:861`).
- El laudo B5.5: ESQ-RI-3 sigue abierta y atada a la release (`docs/plan_tesis.md:695`).

## Firma

BORRADOR — PENDIENTE DE FIRMA de la autora.
