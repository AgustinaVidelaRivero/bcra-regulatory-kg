# d3 — "How to Do Graph Engineering With Opus 5 (Exact Config Inside)" (rody) + hilo (darkzodchi)

**Origen:** https://x.com/0x_rody/status/2081664256571810178 (artículo) + hilo https://x.com/zodchiii/status/2083134599832408208 (promoción con video)
**Fecha aproximada:** 2026-07-27 (artículo; ~1,3 M reproducciones) y 2026-07-31 (hilo; ~721 K), al 2026-08-02
**Etiqueta:** divulgación — no citable; ideas rastreables a fuentes primarias.
**Nota de captura:** el texto no llegó pegado con el mandato; este archivo se construyó desde las URLs de origen (navegador, 2026-08-02) como **resumen estructurado fiel** — el texto verbatim completo queda para pegado directo de la autora (sección al pie).

## Resumen estructurado del artículo

Tesis: el costo dominante de la memoria en grafo es la llamada de extracción por episodio; la economía se arregla con dos principios y una división de trabajo:

1. **División extracción/traversal.** Extracción = alto volumen, bajo juicio → effort bajo + prefijo cacheado. Traversal (responder multi-salto recorriendo el grafo) = bajo volumen, alto juicio → effort alto, con retrieval de subgrafo primero y respuestas que citan las aristas usadas. "La factura y la calidad viven en esa única decisión."
2. **Economía de extracción: prefijo estable cacheado.** El schema completo + instrucciones van primero e idénticos en cada llamada (con `cache_control`); el texto variable (episodio + timestamp) va al final. **Estable-primero, variable-al-final** es lo que mantiene cacheable el prefijo. Config de ejemplo con schema de entidades/aristas con `valid_from` (grafo temporal), resolución canónica de alias y prohibición de inventar relaciones.
3. **Batch API para backfill.** Cargar historia es el trabajo batch de manual (no urgente, alto volumen, cacheable); nunca sincrónico.
4. **Trampas enumeradas:** extracción a effort alto; sin `cache_control`; backfill sincrónico; togglear effort a mitad de sesión (el effort integra la cache key → sesiones separadas para ingesta y consulta); saltear `reference_time` (sin timestamps no hay grafo temporal, solo una ontología estática que se pudre).
5. **Wiring a Claude Code:** Graphiti como servidor MCP sobre Neo4j (Docker) como memoria persistente de sesiones, con la extracción apuntada a la config barata.
6. **Cuentas del artículo** (5.000 episodios, prefijo ~600 tokens, texto ~800: ~USD 35 naive vs ~USD 10,30 con caché+batch) — **cifras de divulgación, dependientes de precios/modelo del momento; NO entran a ningún documento formal del proyecto.** Nota registrada: una respuesta pública al post reporta que el propio modelo citado objeta el código y las cuentas del artículo — refuerza el estatus no-verificado de los números.

## El hilo (darkzodchi)

Post promocional que atribuye a "una ingeniera de Anthropic" la frase de que los equipos pasaron de loops a grafos, con un video adjunto; el propio hilo enlaza como fuente el keynote público "Code with Claude" (demo de producto), y una respuesta señala que el video no trata de grafos. Registrado como claim viral no verificable, mismo patrón que el hilo de d2.

## Ideas que este repo mapea (ver mapa de incorporación)

- **Principio general** (independiente de modelo y precios): prefijo estable cacheado con schema primero y texto variable al final + Batch API para backfill → candidato para la spec de la re-extracción única y del escalado al corpus completo. Coincide con la práctica ya usada por el proyecto (prompt caching en extracción; cf. lecciones de Runs 1-2).
- **Graphiti MCP + Neo4j como memoria de sesiones** → experimento de tooling personal post-U5, timeboxeado y gitignoreado, nunca fuente de verdad.
- Traversal que cita aristas usadas → coincide con el context-builder acotado de la ficha 08 (§V.B).

## Texto verbatim

No se almacena el texto completo de terceros; la fuente es la URL de origen.