# Mandato U-UNION-ESTRECHA — una regla más estrecha para unir la Condicion de un ítem con la norma del encabezado de su lista

**FIRMADO por la autora el 07/10/2026** (firma por mensaje de la autora; versión para firmar en `9e84741`, redactada por la mesa el
07/10/2026, noche, por decisión de la autora del mismo día sobre U-DIAG-CAP3-GRAFO, `df59e79`), con sus dos decisiones al firmar. No va antes de la tanda 1: corre en paralelo con el escalado, como corrección del ensamblado. Si pasa su piso,
se aplica a todas las tandas en el próximo armado, antes de sellar el grafo de la evaluación final (el grafo evaluado de B6.3,
`docs/protocolo_dos_grafos.md`, §2). USD 0, sin API.

DE DÓNDE SALE.
- **La regla E del diagnóstico no pasó su piso.** Unía cada Excepcion o Condicion de un ítem sin vínculo con la única norma admisible del
  mini-chunk que abre su lista (`reports/u_diag_cap3_grafo/propuesta_codigo_UOMISIONES_COD_v2.md`, grupo E). Dio 35 + 61 uniones en
  `a9631a64` y, en la lectura de control de 30 (semilla 20261007), 18 correctas, 10 incorrectas y 2 dudosas: Wilson [0,423; 0,754], bajo el
  piso de 0,75 de L-ESQ-R2 §6.3. Con 30 uniones, ese piso pide 28 correctas.
- **Decisión de la autora del 07/10/2026.** La regla E no entra antes de la tanda 1 (límite declarado, `docs/insumos_escritura.md` §7,
  ítem 6). Una regla más estrecha se fija por escrito antes de medir, se mide sobre una muestra nueva y, si pasa, entra en el próximo armado.
- **Lo que NO cuenta como evidencia.** En la lectura de control, las Condicion acertaron 13 de 16 y las Excepcion 5 de 14. Esa observación
  es posterior al resultado: sugiere por dónde estrechar, pero no prueba nada. La regla nueva se mide desde cero, con semilla nueva.

LA REGLA. Se fija por escrito en U1 y se sella (sha256 y hora) antes de sortear la muestra. Propuesta de la mesa, para que U1 la precise
contra el código:
- solo Condicion de ítem sin `condicion_de` saliente;
- solo cuando el bloque que abre la lista anuncia condiciones o requisitos («las siguientes condiciones», «los siguientes requisitos»,
  «siempre que», «en tanto», o la lista de expresiones que U1 fije y la autora apruebe);
- hacia el único nodo del mini-chunk del encabezado de un tipo admisible para `condicion_de` y compatible con ese anuncio. U1 declara la
  lista cerrada de tipos destino; la propuesta es Potestad, Operacion, Obligacion o Excepcion;
- con dos o más candidatos, o sin anuncio, sin unión;
- arista derivada con `rol_fuente = union_item_encabezado`, sin las marcas de E3, todo al registro.
La Excepcion queda fuera (decisión de la autora al firmar).

ETAPAS.
- **U1. La regla y su pre-medición, sin leer** (sobre una copia).
  - Texto de la regla con sus listas cerradas, en `data/experiment/union_estrecha/regla_u1.md`, sellado.
  - Cuántas uniones daría en `a9631a64` y en `e22fae1a`, por tipo de destino y por TO, cuántas ambiguas y cuántas sin anuncio.
  - Cuántas de esas uniones estaban entre las 30 de la lectura de control del diagnóstico: se excluyen del sorteo.
  - FRENO U1: la autora aprueba el texto de la regla.
- **U2. La medición.**
  - Muestra de 30 uniones con una semilla nueva, distinta de 20261007 y de 20261008, fijada y sellada antes de sortear, sobre las uniones
    de la regla aprobada en `a9631a64`. Lista sellada antes de leer.
  - Fichas sin veredicto, con el texto del ítem y el del bloque que abre la lista.
  - Criterio de «correcta», sellado antes: la Condicion del ítem es condición de esa norma del encabezado según el texto.
  - Lectura en tres pasos: primera lectura de una **sesión aparte, que no diseñó la regla** (decisión de la autora al firmar); segunda
    a ciegas de la mesa; adjudicación de la autora.
  - Piso: al menos 28 correctas de 30 (Wilson inferior ≥ 0,75), con no decidibles declarados.
  - FRENO U2 con la cifra.
- **U3. Si pasa: la implementación**, en el ensamblado (fila F15, solo código sobre lo guardado).
  - Selftest con casos por rama.
  - Diff de los grafos r2b con la lista exacta de aristas nuevas.
  - Selftest de claves OK, sin claves movidas.
  - Nota en la tabla de reprocesamiento.
  - Entra en el próximo armado de todas las tandas, antes de sellar el grafo de la evaluación final.
  - Si no pasa, el límite declarado queda como está y la unidad cierra en U2.

CRITERIOS DE ACEPTACIÓN. Cada uno con su comando y su salida:
- la regla sellada antes del sorteo;
- la semilla y la lista selladas antes de leer;
- las tres lecturas selladas antes de comparar;
- en U3, que `kg.json` cambie solo por las uniones de la regla;
- sha256 del repo antes y después de cada corrida;
- 2.213 `.pyc`;
- grep de convenciones.

ESCRITURAS:
- `data/experiment/union_estrecha/` (se crea) y el scratchpad;
- en U3, además, `data/experiment/tanda0/code/ensamblar_tanda0.py`, su selftest y la nota de la tabla de reprocesamiento.

PROHIBIDO: el prefijo y el mensaje de E1, E3, los validadores, los grafos sellados, la API, commitear.

REQUISITOS: CLAUDE.md §4 (a a l).

CONVIVENCIA:
- U1 y U2 son de solo lectura sobre lo guardado: pueden correr en cualquier momento después de la firma.
- U3 va después de U-OMISIONES-COD, que toca el mismo archivo, y antes del armado que precede al sello del grafo de la evaluación final.

DECISIONES DE LA AUTORA AL FIRMAR (tomadas el 07/10/2026):
1. **La Excepcion queda fuera**, como propuso la mesa.
2. **La primera lectura de U2 la hace una sesión aparte, que no diseñó la regla.**

## Firma

FIRMADO por la autora el 07/10/2026 (versión para firmar en `9e84741`). Rige desde esta firma. Corre en paralelo con el escalado; U3, si
U2 pasa, después de U-OMISIONES-COD y antes del armado que precede al sello del grafo de la evaluación final.
