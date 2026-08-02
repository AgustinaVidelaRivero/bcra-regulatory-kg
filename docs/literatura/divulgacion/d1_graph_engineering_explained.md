# d1 — "Graph Engineering explained: what it is, when to use it and when not to" (Kopadze)

**Origen:** https://x.com/AnatoliKopadze/status/2080668775796314331
**Fecha aproximada:** 2026-07-24 (según el post; ~3,7 M de reproducciones al 2026-08-02)
**Etiqueta:** divulgación — no citable; ideas rastreables a fuentes primarias.
**Nota de captura:** el texto no llegó pegado con el mandato; este archivo se construyó desde la URL de origen (navegador, 2026-08-02) como **resumen estructurado fiel** — el texto verbatim completo queda para pegado directo de la autora (sección al pie).

## Resumen estructurado (14 secciones del artículo)

1. **Origen del término.** Surge de la conversación pública sobre "loops" (un agente mejorando una cosa en repetición); lo que se popularizó después no es un loop mejor sino una red de loops que se controlan entre sí. El propio artículo reconoce que ingenieros señalaron en horas que es una idea de décadas con nombre nuevo — y lo presenta como punto a favor (patrón probado).
2. **Qué es un grafo.** Plan de trabajo dibujado: nodos = un trabajo acotado (un agente, una tarea, un input, un output), aristas = dependencia real de datos. El nodo utilizable exige un contrato: trabajo acotado, input definido, output con schema forzado (texto libre se rechaza y reintenta).
3. **Test de aristas falsas.** Para cada paso: ¿necesita realmente el resultado del anterior? Si no, la arista es falsa y los trabajos pueden correr en paralelo.
4. **Todo setup lineal ya es un grafo** (el más pobre: una cadena). Redibujar la cadena cortando aristas sin datos la colapsa a pocas dependencias reales; la latencia pasa de la suma de todos los pasos a la de la capa más lenta.
5. **El patrón que paga: el diamante** (fan out → reduce → synthesize), con reduce en código plano (sin modelo) y verificación intermedia. Incluye pseudocódigo de un market-scan: fan-out por ángulo con schema validado y modelo barato, dedupe en código, verificador escéptico por hallazgo con `freshContext: true` y modelo fuerte, síntesis final.
6. **El verificador es el truco completo.** Los modelos no detectan la mayoría de sus propios errores; el agente que hizo el trabajo nunca chequea el trabajo. El verificador va en un nodo aparte con contexto limpio ("worker y verificador jamás comparten contexto" — compartirlo es un solo loop disfrazado). Chequeo partido en tres lentes paralelas (¿correcto? ¿vigente? ¿la fuente existe y respalda?) con pase por mayoría.
7. **Dónde se rompen los grafos.** (i) Colapso de contexto en el fan-in masivo → fan-in por capas (batch → resumen por batch → síntesis sobre resúmenes, nunca la pila cruda). (ii) Independencia falsa: dos nodos que escriben el mismo archivo o pegan a la misma API comparten una arista oculta → aislar workers (worktrees) y auditar recursos compartidos, no solo datos. (iii) **Falla silenciosa de nodo → fan-in guard:** todo merge cuenta sus inputs contra los esperados y flaggea el hueco; "nunca sintetizar sobre un set parcial y llamarlo completo".
8. **Cuándo NO usar grafo:** tarea chica o aislada, se quiere aprobar cada paso, trabajo exploratorio sin plan, pasos genuinamente secuenciales. El tell es el test de aristas falsas: si no hay dos trabajos sin arista entre sí, no hay grafo que construir.
9. **Anchors (la sección que el proyecto mapea a su capa determinística).** Un grafo donde todo nodo controla a otro nodo puede ser totalmente consistente y nada verificado (los números se chequean contra un sistema que los produjo). La topología no compra verdad: hacen falta **anclas — nodos con los que no se puede discutir** (tests que corrieron de verdad, dinero que entró) — y **reglas congeladas: exactamente las que un optimizador querría aflojar para ganar se mantienen fuera de su alcance**. "El grafo es tan honesto como las cosas dentro de él que se niegan a moverse."
10. **Cómo construir uno en Claude Code** (dynamic workflows, palabra "workflow", coordinación como código que no re-gasta contexto).
11. **Cinco specs de grafo listos para pegar** (research desk, SEO, go-to-market, refactor sweep, discovery loop) — todos el mismo diamante con verificador independiente, fan-in guard y human gate.
12. **Costo y supervisión.** Un grafo cuesta mucho más que un chat; cita el caso Bun (~535 K líneas traducidas a >1 M en ~11 días, ~50 workflows, hasta 64 agentes, ~USD 165.000, con crítica pública sobre revisabilidad). Cifras de divulgación, no verificables.
13-14. **Cierre:** el grafo compra ancho, no juicio; la jugada es saber cuándo el trabajo es ancho y cuándo la respuesta era un loop.

## Ideas que este repo rastrea a fuentes primarias / a sus propios artefactos

- Anchors / reglas congeladas → ficha 08, tabla de correspondencias (capa determinística D1-D7, varas selladas, material quemado).
- Worker/verificador sin contexto compartido → ficha 08 (ceguera del juez, N=3 réplicas frescas, eval sets ciegos).
- Fan-in guard → ficha 08 (guarda de hit-rate del escalón 1b, Enmienda §8).
- Dynamic workflows / patrones de orquestación → fuentes primarias de Anthropic referenciadas en la ficha 08, crítica (a).

## Texto verbatim

No se almacena el texto completo de terceros; la fuente es la URL de origen.
