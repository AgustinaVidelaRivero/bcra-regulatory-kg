# Fe de erratas — causa del cero de unidades en el bloque de régimen informativo

**Qué es este documento.** El scoping de B5.6
(`data/experiment/escalado_prep/scoping_b5_6_tabular_reginf.md`, unidad U-B5.6-0)
midió el bloque de régimen informativo y encontró tres afirmaciones del repositorio
que no se sostienen contra los archivos. Los laudos firmados y los pre-registros
sellados **no se enmiendan**: se corrigen por declaración, y esta es la declaración.
El laudo `docs/laudo_ESQ-1_diseno.md` (commit `94bb7a7`) y el pre-registro
`data/experiment/esq/prerregistro_esq1.md` quedan intactos.

Toda cifra de este documento sale del scoping citado o de una verificación
independiente de mesa contra el código, indicada con archivo y línea.

**Notación:** `scoping:N` es la línea N del scoping; `§` se reserva para
secciones (del laudo, del pre-registro).

---

## (a) La causa del cero no es la estructura tabular

**Lo que decía.** El laudo ESQ-1, §D10: *«La causa no es el esquema sino la
estructura tabular de esos documentos, que la etapa E0 no procesa.»*

**Lo que dicen los archivos.** La causa proximal es la **compuerta de rol de página
de E0**. La clasificación de páginas sólo pasa a `cuerpo` **después** de haber visto
una página de índice; mientras eso no ocurre, toda página queda en `portada`:

```
elif not visto_indice:
    rol = ROL_PORTADA
else:
    rol = ROL_CUERPO
```

(`data/experiment/reextraccion_v2/e0_chunking/e0_lib.py:206-209`, verificado por
mesa; el scoping cita la rama en `:206-207` y la compuerta de `parsear_cuerpo` en
`:342-343`.)

Esos documentos no tienen página de índice, de modo que **47 de 53 TOs tienen el
100 % de sus páginas clasificadas como portada** (scoping:36, scoping:188) y **nunca
llegan** a la etapa donde una tabla podría estorbar. El obstáculo tabular es
posterior en el orden causal, y sólo puede actuar sobre documentos que ya
atravesaron la compuerta.

**Segundo modo de falla, independiente del primero.** 1 TO sí llega a tener páginas
de cuerpo y produce cero unidades igualmente, por no tener ninguna línea con formato
de sección. Es una falla distinta y necesita un remedio distinto; agruparla con las
47 anteriores oculta que son dos problemas.

**Magnitud real de lo tabular.** 12,4 % de las palabras del bloque (69.543 de
562.622, scoping:251) y **21 de 53 TOs sin ninguna tabla** (scoping:43). Es real y es
minoritario.

**Consecuencia.** La frase del laudo describe un obstáculo que existe, pero no el que
produce el cero. Quien lea sólo el laudo concluiría que construir el parser de tablas
desbloquea el bloque, y no es así.

---

## (b) Relajar el regex de índice no desbloquea el bloque

**Lo que decía.** El plan, B5.2: relajar el regex de E0 —`Sección N[.:]`, `Índice`
sin guiones con guarda— como parte del endurecimiento previo al escalado.

**Lo que dicen los archivos.** En los documentos del bloque la palabra que el regex
busca **no aparece**: no hay marcador que relajar. Peor: en un caso su única aparición
es prosa sobre *índices de actualización* —el término en su acepción económica, no
estructural—, de modo que un regex más laxo lo tomaría como marcador de índice y
produciría un falso positivo, clasificando como índice una página que no lo es.

**Consecuencia.** B5.2 sigue siendo necesaria por lo que fue escrita (paridad de E0
sobre normativa general, health-check por TO), pero **no desbloquea el bloque de
régimen informativo** y no debe listarse como si lo hiciera. Lo que desbloquea es un
modo de lectura que no exija raíz de sección.

---

## (c) El módulo de tablas no decide el destino del bloque

**Lo que decía.** El plan, B5.6: *«Módulo de tablas … decide el destino del bloque
RI.»*

**Lo que dicen los archivos.** Medido: el parser alcanza a **23 de 53 TOs** y al
**12,4 % de las palabras** del bloque (scoping:702, scoping:949). Decide el destino de
**una de las cinco familias estructurales** del bloque (scoping:47), no el del bloque.

**Lo que sí resuelve, y por lo que hay que construirlo igual.** RX-10 es un defecto de
correctitud **sobre normativa general** —dos montos invertidos verificados—, y ese
defecto vive en el grafo que la tesis entrega. El parser se justifica por sí solo,
con independencia de lo que se decida sobre el bloque de régimen informativo.

---

## Qué NO cambia

Esta corrección es sobre **el diagnóstico técnico y el orden de construcción**. No
toca nada de lo decidido:

- **La dirección sigue siendo validar el esquema sobre el corpus completo**, no sobre
  una de sus dos familias. El argumento del laudo —un test que cubre sólo la familia
  donde el esquema tiene más chance de funcionar está sesgado hacia el resultado
  cómodo— no depende de cuál sea la causa del cero.
- **El bloque debe correr su propio ciclo ESQ antes de que el esquema se congele para
  él.** Sigue vigente tal cual.
- **La decisión de alcance sigue reservada a los mentores**, y se lleva antes de
  laudar D5. Lo que cambia es la forma de la pregunta (ver plan, agenda de mentores):
  ya no es escalar o no escalar, es hasta dónde se llega, con los costos medidos.
- **ESQ-1 y ESQ-2 corren igual** sobre normativa general, en cualquier escenario.

Lo que cambia es **qué hay que construir y en qué orden**: modo de lectura sin raíz de
sección primero, parser de tablas después (por RX-10, no por el bloque), extensión del
esquema como pieza propia, y recién entonces el ciclo ESQ del bloque.

---

## Fe de erratas del pre-registro de ESQ-1 (discrepancia menor, declarada por el scoping)

El pre-registro sellado consigna **74** unidades con omisión declarada y **33** en
Capitales Mínimos. El recomputo del scoping da **75** y **34** (scoping:571). La diferencia
es **una sola unidad**, cuyo campo de omisión contiene únicamente la cadena de salto
de línea, sin texto. El scoping la descartó por vacía, adoptó 74 y declaró el
descarte.

El pre-registro **no se enmienda**. Queda declarado acá que el número es 74 bajo la
regla «se descartan las omisiones sin texto», y que el recuento crudo sin esa regla
es 75. Ninguna predicción del pre-registro depende de esa unidad: P1 fija su umbral
sobre una muestra de 20 y §4 es una observación, no una predicción.

---

## Hallazgo nuevo, que no es corrección

El scoping encontró además algo que no estaba registrado en ningún documento previo:
**el esquema vigente no puede representar el contenido del bloque, y falta en dos
lugares independientes**. Por su alcance —que excede al régimen informativo— se
registra en `docs/plan_tesis.md` como hallazgo con entrada propia, y no como nota de
esta fe de erratas.
