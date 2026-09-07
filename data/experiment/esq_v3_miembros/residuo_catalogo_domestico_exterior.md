# U-ESQ-V3 — RESIDUO DECLARADO: ids del catálogo v3 con definición doméstica y alias extranjeros

Hallazgo del laudo §5, a raíz del caso `ctacor`. **No se arregla en esta unidad: el prefijo v3 está sellado y abrir ids es re-sello y unidad propia.** Acá se registra, con los ids nombrados y el mecanismo por el que se propaga.

Barrido de las **67** entradas de clase e instancia del bloque sellado (los 35 roles quedan fuera: no llevan alias). **Ids con el patrón: 3.**

## El patrón

Un id cuya definición o label lo presenta como doméstico —o simplemente sin marca de extranjería— y que, **en la misma línea**, declara entre sus alias una variante «del exterior». El alias es lo que gobierna a qué id cae una mención del texto, de modo que el id cubre el doméstico y el extranjero a la vez mientras su definición dice otra cosa.

## Los ids afectados

| id | label | alias con marca de extranjería |
|---|---|---|
| `Sujeto_banco` | Bancos | Bancos del exterior; Banco del exterior |
| `Sujeto_entidad_cambiaria` | Entidades cambiarias | Entidades cambiarias del exterior; Compañía cambista del exterior |
| `Sujeto_entidad_financiera` | Entidades financieras | Entidades financieras del exterior; Entidad financiera del exterior |

## Mecanismo de propagación (por qué no es cosmético)

`miembro_de` va de clase a rol. La **regla de herencia 2** del diseño del esquema hace que un `aplica_a` hacia un rol alcance a **cada uno de sus miembros**; desde ahí la **regla 1** desciende a **toda subclase** del miembro. Un miembro con este patrón arrastra la contradicción a todo lo que herede de él: una norma de alcance doméstico termina afirmada sobre sujetos del exterior, sin que nada en el grafo lo señale.

Es exactamente el vicio que el laudo (a) manda retirar cuando se aplana a la clase madre, con la diferencia de que acá **no está en la adjudicación sino dentro del propio catálogo**: aunque cada fila se adjudique con el criterio correcto, el id adjudicado ya trae la unión.

## Alcance real dentro de esta unidad

De los ids afectados, los que efectivamente entran como miembros en la adjudicación de esta fase se listan en el reporte con su cuenta. El caso que lo destapó —`ctacor`— **no** produce arista, justamente porque «del país» resultó ser recorte real frente a un id que cubre ambos. **Este hallazgo no cambia ninguna cifra de la fase 2.**

## Ids que SÍ tienen id propio para lo extranjero (contraste, no afectados)

| id | label |
|---|---|
| `Sujeto_banco_central_del_exterior` | Bancos centrales del exterior |
| `Sujeto_fmi` | FMI (Fondo Monetario Internacional) |

## Remedio propuesto (ítem de backlog, no de esta unidad)

Ids separados para los sujetos del exterior, con su propia definición y su lugar en el árbol, y los alias extranjeros migrados a ellos. Eso **cambia el bloque de catálogo y por lo tanto el prefijo v3**, cuyo sha está sellado y candado en `perfil_e1`: es re-sello del prefijo y unidad propia, con su laudo.

