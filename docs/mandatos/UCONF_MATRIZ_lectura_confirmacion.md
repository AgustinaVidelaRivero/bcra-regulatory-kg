# Mandato U-CONF-MATRIZ — lectura de confirmación de la matriz ampliada (`condicion_de` → Operacion y → Potestad)

**VERSIÓN PARA FIRMAR (mesa, 09/10/2026),** con dos decisiones de la autora del 09/10/2026: el grafo (§1) y qué pasa si → Operacion no
confirma (§7). **Firma y despacho PENDIENTES de la autora.** USD 0, sin API.

## 0. Qué confirma y por qué

- **La decisión.** L-ESQ-R2 (FIRMADA, `4ef7650`), §6.3, decisión de la autora del 30/09: se ampliaron `condicion_de` → Operacion y
  `condicion_de` → Potestad.
  - → Potestad entró con un desvío declarado: 27 de 30, piso de Wilson 0,744, frente al criterio de 0,75.
- **La confirmación que pide el laudo:** «En r2b, E3 verifica cada relación nueva. Sobre el grafo re-extraído se lee una muestra de los
  dos pares, con lectura asistida y revisión de la autora. […] Si → Potestad no se confirma, se retira en el validador, en código, sin
  re-extraer».
- **Cuándo:** es requisito de B6.1, la tanda 1 (`docs/plan_tesis.md:405`, nota del 30/09, y `:409`: «Depende de 11, de la lectura de
  confirmación de la matriz posterior a 11 y del tablero»).
- **Qué se confirma:** que, en las aristas del grafo r2b (ya verificadas por E3), la Condicion es el antecedente de la Operacion o de la
  Potestad de destino, según el texto. Es la misma pregunta del estudio original, ahora sobre lo que produce el pipeline r2b.

## 1. Sobre qué grafo

**KG-Tanda0-Diez-r2b-sincola** (`e22fae1a…`, registrado en `data/experiment/neo4j/grafos.py:172`; sello `dde9f44` y `235a295`): el grafo
sin cola de la tanda 0, que es el que entra en la cadena de la evaluación. **Decisión de la autora del 09/10/2026.**
- **Población:**
  - 643 aristas `condicion_de` → Operacion;
  - 264 aristas `condicion_de` → Potestad.

  Comando: `poblacion_conf_matriz_mesa.py`, en el paquete de la mesa (`hoja_de_ruta_tanda1_mesa/conf_matriz/`); salida en
  `poblacion_conf_matriz_salida.txt`.
- **Como referencia:** en el grafo completo (`a9631a64`) son 676 y 273; en desarrollo sin cola (`2922b72d`), 546 y 237.

**El re-sellado.** Ningún ítem de U-OMISIONES-COD v7 cambia aristas `condicion_de`.
- R0 (E3-01) re-verifica 20 unidades de la tanda 0 y puede cambiar lo que E3 acepta en ellas.
- **Control después del re-sellado:** las 60 aristas leídas siguen en el grafo re-sellado, con los mismos extremos. Las que cambien se
  listan y se declaran. La cifra no se recalcula salvo que cambie el resultado del criterio.

**Solapamiento.** La etapa V del pre-registro de tripletas sortea en el grafo de desarrollo sin cola (`2922b72d`), cuyos TOs están en
diez. Si una arista leída acá cae también en la muestra de V, se declara el solapamiento; no se excluye (pre-registro, `:42`).

## 2. Criterio, sellado antes de leer

**El protocolo del 28/09/2026,** tal como está asentado en `reports/u_estudio_matriz/lectura/resultado_lectura_matriz.md` (`c671b52`,
sección «Protocolo, tal como está asentado»). Su sha256 en ese commit va al acta.
- **Correcta:** el texto del fragmento (propio y heredado de la unidad de procedencia) sostiene que el origen es condición del destino.
  Si el nodo parece mal tipado pero la relación es cierta, cuenta como correcta y se anota.
- **Incorrecta:** el texto no sostiene que la Condicion sea el antecedente del destino.
- **No decidible:** el texto no alcanza para decidir; va con su motivo.
- **El criterio, por par:** el par se confirma si el límite inferior de Wilson al 95 % de correctas / (correctas + incorrectas) es al
  menos 0,75, con las no decidibles excluidas y reportadas. Con más de 6 no decidibles, el par no se decide con esta muestra. Con 30
  decididas hacen falta 28 correctas; con 29, 27. Para otro n, el umbral se recalcula con el mismo piso.

## 3. Muestra

- **30 aristas por par,** por muestreo simple sobre la lista de aristas ordenada por (origen, destino).
- **Semillas, fijadas por la firma:** `int(sha256("U-CONF-MATRIZ|Operacion|<sha256 del texto firmado>")[:16], 16)` y la misma con
  «Potestad». El texto firmado son las líneas de este archivo anteriores a «## Firma», en el commit de la firma.
- **El acta:** la población (sus dos sha256), la hora, la muestra y su sha256, el sha256 del criterio y el del grafo. Se sella antes de
  abrir una ficha, con el patrón de `data/experiment/lectura_aceptadas/l0_sellos.py`.
- **El orden de lectura es al azar, mezclando los dos pares:** el lector no ve el par al leer.

## 4. Ficha

- **El nodo Condicion:** tipo, etiqueta y descripción, con la descripción marcada como salida del extractor.
- **El predicado y el nodo de destino:** tipo, etiqueta y descripción, con la misma marca.
- **El texto de la unidad de procedencia de cada extremo,** propio y heredado (`e0_chunking/salida_tanda0_r2b/chunks_<to>.json`), con
  el tramo de E1 si lo hay. Si los dos extremos están en unidades distintas, van las dos.
- **Las páginas y la ruta del PDF.**
- **Sin el veredicto de E3, sin otras aristas del nodo y sin el resultado del estudio original.**

## 5. Quién lee

- **La lectura:** una sesión nueva de la mesa (lectura asistida por una instancia de modelo; desvío declarado, como el 28/09).
  - **Dónde corre:** abierta fuera del repo, con la cláusula de lecturas a ciegas de la plantilla de la mesa, porque la memoria del
    proyecto y los commits citan las cifras del estudio original.
  - **Qué hace:** lee las 60 fichas, marca cada una y sella la planilla (sha256 y hora) antes de calcular ninguna cifra.
- **La revisión:** la autora revisa todas las incorrectas y no decidibles, y 5 correctas por par, sorteadas con
  `sha256("U-CONF-MATRIZ|revision|…")`. Adjudica las que no comparta.
  - Alternativa: revisar las 60, como en el estudio original. PENDIENTE de la autora al firmar.

## 6. Etapas

- **C1. El acta y las fichas** (la sesión lectora, antes de leer): población, sorteo, acta sellada y 60 fichas con su render.
- **C2. La lectura:** la planilla sellada.
- **C3. Las cifras:** por par, correctas, incorrectas y no decidibles, Wilson, y si cumple. La lista para la autora, con cada ficha.
  FRENO.
- **C4. La revisión de la autora y su adjudicación,** y la cifra final.

## 7. Qué pasa en la ruta si no confirma

Lo que sigue lo fija la autora el 09/10/2026, antes de la lectura.

- **→ Operacion no confirma: la relación no se retira** (decisión de la autora del 09/10/2026).
  - Queda en el grafo, con su cifra declarada.
  - Los errores se clasifican. Las clases salen de las notas de C2: la sesión lectora las propone en C3 y la autora las adjudica en C4.
  - Una clase sistemática que se pueda corregir con código va al grupo 2.
- **→ Potestad no confirma: rige L-ESQ-R2 §6.3** (`4ef7650`): se retira en el validador, en código, sin re-extraer. Toca:
  - la matriz del validador r2 (`AMPLIACION_R2`);
  - S3 de los shapes;
  - la fila de la matriz en el laudo de la release r2;
  - y, si entra al re-sellado, saca del grafo de la tanda 0 las 264 aristas del sin cola (273 en el completo).
  - **Cuándo entra.** Desde el 09/10/2026 el alcance del re-sellado está congelado (decisión de la autora): no entra nada más, salvo que
    corrija un dato falso de la tanda 1 y sea barato. El retiro es código del validador, sin re-extraer. Si cabe en la excepción lo
    decide la autora con el resultado, PENDIENTE (§9):
    - o entra al re-sellado de la tanda 0 por esa excepción;
    - o rige la opción III ya decidida: desde la tanda 1, con el re-sellado después, declarado.
  - **En la tanda 1, en los dos casos,** el prefijo de E1 (congelado en la release r2) sigue pidiendo esas relaciones y el validador las
    rechaza: quedan en el registro de rechazos, declaradas. Ninguna clave de caché de E1 se mueve.
- **Ninguno se decide** (más de 6 no decidibles): una muestra complementaria de 30 del par, con otra semilla sellada. Suma un día.
- **Calendario estimado** (NO VERIFICADO): despacho lun 12/10, C1 y C2 mar 13, C3 mié 14 y la revisión de la autora mié 14/10. Llega
  antes de O2.

## 8. Escrituras y prohibiciones

**ESCRITURAS:**
- `data/experiment/conf_matriz/`, que se crea: el acta, las fichas, la planilla sellada, las cifras y los scripts;
- el scratchpad de la sesión.

**PROHIBIDO:**
- la API;
- todo otro archivo del repo;
- los grafos sellados;
- el validador y la matriz;
- el criterio una vez sellado;
- commitear.

**REQUISITOS:**
- CLAUDE.md §4 (a a l);
- la cláusula «límites medidos, caso por caso» de la plantilla de la mesa;
- los mensajes de commit sin unidades, documentos ni mecanismos;
- la tesis: la versión vigente está en Overleaf, y `docs/tesis/main.tex` no se usa como fuente sin declararlo.

## 9. Decisiones

**Ya tomadas por la autora (09/10/2026):**
- el grafo: el sin cola, `e22fae1a` (§1);
- si → Operacion no confirma, la relación no se retira: queda con su cifra declarada, los errores se clasifican, y una clase sistemática
  que se pueda corregir con código va al grupo 2 (§7). Para → Potestad rige L-ESQ-R2 §6.3.

**PENDIENTES de la autora:**
1. al firmar, la revisión: las no correctas más 5 correctas por par (recomendación de la mesa), o las 60 (§5);
2. con el resultado, si → Potestad no confirma: si su retiro entra al re-sellado de la tanda 0 por la excepción del alcance congelado, o
   rige desde la tanda 1 por la opción III (§7).

## Firma

PENDIENTE de la firma de la autora (versión para firmar del 09/10/2026).
