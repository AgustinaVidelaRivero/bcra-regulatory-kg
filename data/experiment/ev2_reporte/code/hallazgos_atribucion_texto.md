Texto fijo incluido por `render_md` (los números salen de las tablas §1–§4 de
este mismo archivo, generadas por `atribucion_fallas.py --correr --incluir-enc
--sensibilidad-descendientes`; regla `regla_atribucion.md`, commit `40603a9`).
Nomenclatura: KG-Base (`12c226e2`) / KG-Refinado (`26fac8b4`) / KG-Reextraído (`8e2eadee`).

**H1 — Los 9-9 incorrectos NO son el mismo tipo de falla.** Sobre los pares
definitivos (§3.a, traza representativa): los 9 incorrectos de **KG-Refinado**
son 4 alcanzabilidad + 1 vista_no_consultada (5 de navegación: el ancla está y
el agente no la alcanzó u no la abrió), 2 generacion y 2 ausencia_kg (ambas
ausencias totales: `cap:5.2.1`, `cap:8.3.2`, 0/0 en §4). Los 9 de
**KG-Reextraído** son 4 ausencia_kg + 3 generacion + 1 alcanzabilidad + 1
vista_no_consultada: la mitad es "el ancla no resuelve" — y §4 muestra que 3 de
esas 4 anclas existen como sub-puntos (`cap:5.2.1` 16 descendientes, `cla:2.1`
21, `cla:3.5` 10) y la cuarta (`ric:7.2`) vive solo en un contenedor. Perfil:
KG-Refinado falla por navegación con el ancla presente; KG-Reextraído falla por
granularidad de ancla (la regla del censo la registra como ausencia) y por
generación. En las 120 trazas base (§1.b) el contraste es el mismo: incorrectos
KG-Refinado 0/3/1/2 (ausencia/alcanz./vista/generación) contra KG-Reextraído
4/0/1/3.

**H2 — KG-Base falla por navegación.** 8 de sus 17 incorrectos definitivos son
alcanzabilidad y 2 vista_no_consultada (10/17 de navegación; §3.b), más 4
ausencias totales (§4: 6 anclas de fidelidad no están en KG-Base en ninguna
forma, contra 4 en KG-Refinado y 0 totales en KG-Reextraído) y 3 generación.
En base (§1.a) KG-Base tiene 11 alcanzabilidad contra 6 y 1. Entre los
incorrectos definitivos la clase dominante es la navegación en KG-Base (10/17)
y en KG-Refinado (5/9), y la ausencia por granularidad en KG-Reextraído (4/9);
la generación no domina los incorrectos en ningún grafo (3, 2, 3). Coincide con
su recall consultada intermedio-bajo en navegabilidad y con sus 4 ausencias
totales del eje sintético.

**H3 — La generación es la clase mayoritaria de los parciales en los tres
grafos** (§1.b: 16/23, 23/30, 18/28 de los parciales base; §2.b: 37, 39, 39 de
las re-corridas parciales): cuando el agente llega al nodo-ancla, lo típico es
una respuesta parcial (tasa de criterios no cumplidos ≈ 0,48–0,59, la más baja
de las cuatro clases en cada grafo, tabla de criterios de §1), no una
incorrecta. Grounded ≠ correct sigue siendo el patrón dominante y es el mismo
en los tres grafos.

**H4 — Ausencia_kg significa cosas distintas en cada grafo.** En KG-Base y
KG-Refinado toda ancla no resuelta es ausencia total (crudo=0, desc=0: 6/6 y
4/4, §4). En KG-Reextraído 8/10 son granularidad (el punto existe solo como
sub-puntos) y 2/10 contenedor. La sensibilidad informativa de §4.b (fuera de
la regla ratificada) lo confirma: resolviendo con descendientes, las 9 trazas
base ausencia_kg de KG-Reextraído pasan a 6 generacion + 2 alcanzabilidad + 1
ausencia, mientras que las 6 de KG-Base y las 4 de KG-Refinado no se mueven.
Es coherente con la tasa de criterios no cumplidos de la clase ausencia_kg en
KG-Reextraído (0,72 base; **0,35** en las re-corridas §7, contra 0,61–0,87 en
los otros grafos): el agente encuentra el contenido en los sub-nodos aunque el
ancla exacta no exista. La clase primaria se mantiene por regla; la lectura del
mandato de la unidad anterior ("15/23 son granularidad") se replica en el eje
de fidelidad.

**H5 — Generación con abstención: el nodo-ancla consultado es cáscara.**
Generación × abstención (§1.c) = 1 / 2 / 4 en base. Los casos incorrectos de
ese cruce (EV2F-001 y EV2F-007 en ambos refinados, EV2F-011 en KG-Base,
EV2F-023 en KG-Reextraído; §3.b) son trazas en que el `ver_nodo` del ancla
devolvió un nodo con `properties` de encabezado o puntero (p. ej. `{"tipo":
"Enajenación de activos no financieros no producidos"}`; "Situaciones 13.3.1. a
13.3.9. que excepcionan…"; "deberán observar los siguientes requisitos") y el
agente, correctamente, declaró no encontrar el detalle. La regla clasifica
`generacion` porque el ancla fue consultada; el sub-diagnóstico "nodo-ancla sin
el contenido pedido" (defecto de profundidad de extracción, no de generación)
queda declarado como LIMITACIÓN de la clase y fuera del alcance de esta unidad
(`regla_atribucion.md` §7): es material para el verificador causal con laudo
humano, no para una quinta clase.

**H6 — Las re-corridas §7 replican el perfil base** (§2.a, 191 trazas):
generación 42/39/39, ausencia 8/12/18, alcanzabilidad 1/7/3,
vista_no_consultada 2/1/5. KG-Reextraído concentra las ausencias (18, todas
parciales), KG-Refinado la alcanzabilidad residual (7). No hay clase que
aparezca en las re-corridas y no en la base.

**H7 — Instrumento:** 120/120 (base) y 191/191 (§7) trazas con replay estándar
y fuerte OK (sha256 de los tres grafos verificados); doble corrida
byte-idéntica salvo `generado`; 7 re-corridas sin veredicto propio excluidas
y contadas; USD 0.
