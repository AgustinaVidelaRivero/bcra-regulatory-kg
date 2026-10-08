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

## Notas posteriores a la firma

- **08/10/2026 — FRENO U1 revisado por la mesa sobre una copia, y decisiones de la autora.**
  - **Revisión de la mesa.** Copia sin enlaces armada desde `7788e52`; repo sin cambios fuera de `docs/` (sha256 antes y después) y 2.213
    `.pyc`; no abrí nada bajo `reports/u_diag_cap3_grafo/lecturas/` ni veredictos de la lectura de control de la regla E. Se reproduce
    todo:
    - el sello: `regla_u1.md` (`9f5028d1…`) y los cuatro archivos de código dan los sha256 de `sello_regla_u1.txt` (08:04:06); las salidas
      de la primera medición de la instancia tienen mtime 08:04:14–15. Las salidas no llevan hora propia: la única evidencia de orden son
      los mtimes;
    - la pre-medición: `comandos_u1.sh` en la copia (selftest 44/44, dos corridas iguales, los 6 archivos de `salida/` iguales byte a byte)
      y un script mío que no importa el código sellado: 165 y 161 Condicion de ítem sin `condicion_de`; 40 y 37 uniones; 82 y 80 sin
      anuncio; 25 ambiguas (17, 3 y 5); 14 y 15 sin candidato; 4 sin unidad de encabezado; destinos 21, 10 y 9 (Potestad, Operacion,
      Excepcion) en `a9631a64` y 20, 9 y 8 en `e22fae1a`; todas de ext, en 19 y 17 bloques; formas S1 26, S2 8 y N 6;
    - contra la regla E: sus 61 uniones de Condicion son las 40 más 21 sin anuncio con un solo candidato, el mismo (19 Obligacion y 2
      Potestad);
    - contra el control del diagnóstico (solo ids): de las 16 Condicion, 11 están entre las 40 y 5 quedan sin anuncio. El marco de U2,
      `salida/marco_u2_diez.json` (`69177a21…`), tiene 29 ids sin repetir, todos de ext y ninguno de los 11: 15 hacia Potestad, 8 hacia
      Operacion y 6 hacia Excepcion;
    - Wilson al 95 %: 27 de 29, 0,780; 26 de 29, 0,736; 27 es el mínimo con 29.
  - **Precisiones de la mesa, sin efecto en ninguna cifra:**
    - `freno_u1.md` se reescribió después de la foto de cierre de la instancia (08:07:30, `1aa27c3b…`; el archivo actual es `9e4c1ca9…`);
    - `regla_u1.md:83-84` dice que «si» aparece solo como «de si» (lingob::7.1): hay 5 bloques que abren lista con «si», y en la oración
      que rige la lista solo en lingob::7.1 y cap::6.8.3;
    - «24 bloques» para «en la medida que» (`:40`) se reproduce como la forma S con ese subordinante: la frase aparece en 29 bloques y en
      25 dentro de la oración que rige la lista;
    - la regla nombra «quedarán/quedan exceptuados» y el código compara por prefijo; no cambia nada en los dos grafos.
  - **Decisiones de la autora (08/10/2026):**
    1. **Aprueba el texto de la regla**, con los cuatro puntos de `regla_u1.md` §10: las listas cerradas del anuncio, con «en tanto» y
       «en la medida en que» fuera; la compatibilidad (Restriccion nunca; Obligacion fuera en la forma N; con marca de excepción, solo
       Excepcion); la Excepcion como destino; y todo el rango de `condicion_de` para contar el único candidato.
    2. **U2 se hace como censo de las 29 uniones del marco, con un piso de 27 correctas de 29** (límite inferior de Wilson 0,780 ≥ 0,75).
       Reemplaza la muestra de 30 con semilla nueva y el piso de 28 del texto firmado (`:36-42`): con esta regla, el marco no llega a 30. No
       hay sorteo. Las no decidibles se declaran y cuentan como no correctas.
    3. **Límite de la medición:** las 40 uniones de la pre-medición, y las 29 del censo, son todas de ext; U2 mide la precisión de la regla
       en ext.
    4. **Control antes de sellar el grafo evaluado:** si U2 pasa y la regla entra en U3, una muestra de las uniones de la regla en los TOs
       de la tanda 1, leída con el mismo criterio. Tamaño, semilla y piso, sellados antes de leer (plan, fila B6.3, nota del 08/10/2026).
  - **Correcciones al despacho de U1** (FRENO U1, §4, puntos 2 y 3): la firma está en `21e55a0` (`9e84741` trae la versión para firmar), y
    «sin las marcas de E3» sale del mandato (`:26`), que el despacho había omitido. Errores de la mesa, corregidos en la plantilla.
  - **Despacho de U2** preparado por la mesa: primera lectura de una sesión aparte, sobre fichas sin veredicto y con el criterio sellado
    antes de leer; FRENO U2-a sin la cifra; después, la segunda lectura a ciegas de la mesa y la adjudicación de la autora.
  - **Para U3, no para U1:** `modelos_r2.AristaR2` acepta este `rol_fuente` como texto libre (`modelos_r2.py:632`; los invariantes de
    `:650-659` corren solo para `derivada_de_procedencia`). Si U3 los quiere iguales, toca `modelos_r2.py`, fuera de sus escrituras:
    decisión de la autora cuando llegue U3.
