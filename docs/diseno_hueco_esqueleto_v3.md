# Diseño — hueco de cableado del esqueleto v3 (roles sin miembros)

**Estado: DISEÑO EN FRENO. No se ejecuta ninguna opción; la elección es
de la autora.** Origen: relevamiento U-SUJ-ROL (P3.1, P8, hueco 5).
Todos los hechos de §1 fueron re-verificados contra el repo por la
instancia del plan antes de diseñar.

## §1. Verificación de los hechos (con dos precisiones)

| hecho del informe | verificación | veredicto |
|---|---|---|
| Los 30 roles nuevos tienen `miembros_ids` vacío | 35 roles = 5 dev + 30 nuevos; **30 de 30 vacíos**; los 5 dev suman 7+2+6+1+1 = **17 miembros**, que son exactamente las 17 aristas `miembro_de` del grafo vigente | **CONFIRMADO** |
| Ninguno de los 30 está en `esquema_v2_clases.json` | el archivo tiene 65 clases + **5 roles** (los dev, con sus `miembros`); de los 30, **0 presentes** | **CONFIRMADO** |
| Ese archivo lo lee E5 | `r1_e5_esqueleto.py:3` | **CONFIRMADO** |
| Sellado desde `43f241e` | commit del 2026-07-18 | **CONFIRMADO** |
| U-CABLE-V3 no menciona esqueleto ni `miembro_de` | `docs/diseno_UCABLEV3.md`: **0 menciones** | **CONFIRMADO** |
| S15 nunca implementada; «el validador llega a S13» | S15 no existe. **PRECISIÓN 1:** el validador implementa **S1–S12**, no llega a S13 (`scripts/shapes_validator.py`) | CONFIRMADO en lo esencial; corregido el detalle |
| Una corrida v3 emitiría los roles «sin nodo de rol ni aristas» | **PRECISIÓN 2 (importante para el costo):** con el perfil v3, E2 **sí crea el nodo** de cada rol con su label correcto, porque `perfil_e1._labels_catalogo_v3` deriva los 102 ids del bloque sellado. Lo que falta es la **taxonomía**: E5 no inyectaría `miembro_de` para los 30. **Además, E5 no lo invoca el runner** (`r1_e5_esqueleto.py` es un paso aparte, corrido a mano en r1) | CONFIRMADO con corrección |

**Diagnóstico preciso:** el defecto no es «rol sin nodo», es **rol sin
taxonomía**. En el grafo escalado, `Sujeto_rol_alcance_adrei` existiría
como nodo con su label, y las normas de ese TO apuntarían a él — pero
**ninguna arista lo conectaría con las clases que lo componen**.

**Hallazgo adicional de la verificación (no está en el informe):** los
`miembros_ids` **no entran al texto del prefijo** — el bloque de
catálogo lleva solo `id — label [rol del TO x]`. Poblarlos **no cambia
el sha `35e88c2dd0a2…`** ni el hash `54a111e2175f`. Esto abarata la
opción A y evita el conflicto que se suponía con el laudo B5.4.

## §2. Qué queda roto, exactamente

La consulta por clase. Hoy, sobre el grafo vigente, «¿qué obligaciones
aplican a las entidades financieras?» alcanza las normas de Protección
de Usuarios porque `Sujeto_rol_sujeto_obligado_proteccion —miembro_de→
Sujeto_entidad_financiera` existe. En el grafo escalado sin miembros,
la misma pregunta **no alcanzaría** las normas de los 30 TOs nuevos:
sus roles son nodos aislados del árbol. El agente puede llegar a ellos
por búsqueda léxica del label, pero no por navegación taxonómica —
que es justamente el mecanismo que la tesis presenta como el aporte
del grafo frente al fragmento.

## §3. Las tres opciones, costeadas (la elección es de la autora)

### Opción A — poblar los miembros de los 30 e integrarlos al esqueleto

**Cómo se determinarían.** Mismo criterio A2 de B5.4 fase 1: cada rol
tiene ya adjudicado, con cita verbatim de su pasaje de alcance, el
colectivo que el TO declara. Poblar sus miembros es mapear ese pasaje
a ids del catálogo — el mismo acto de adjudicación que produjo los 35
mapeos a clase, aplicado ahora a los 30 roles. **Evidencia disponible:**
el `label` de cada rol conserva el colectivo («Entidades alcanzadas
(Agregación de datos sobre riesgos: D-SIB)»), y los pasajes con su
`chunk_id` están en `escalado_prep/e0_dry/`, de acceso directo. La
tabla del freno 1 los tenía consolidados, pero **no está en el repo**
(§5).

**Trabajo:** 1 sesión de ejecutor para proponer candidatos mecánicos
por rol (matcheo del pasaje contra labels y alias del catálogo, sin
LLM) + **adjudicación de la autora fila por fila** sobre 30 filas —
el mismo formato del freno 1 de B5.4. Los casos multi-sujeto
(`rrci`: EF+PSP+IMF; `ccbcra`: EF+cajas+cambiarias) requieren juicio,
no matcheo.

**Artefactos sellados:** **ninguno, si se hace por el camino del
perfil.** Los miembros van a un artefacto nuevo (`esquema_v3_clases.json`)
que E5 lee según el perfil, igual que U-CABLE-V3 hizo con validador y
E2; `esquema_v2_clases.json` queda intacto y el grafo vigente
reproducible. Poblar además `ROL_POR_TO_V3.miembros_ids` es opcional y
**no rompe el sello** (no entra al prefijo, verificado en §1) — pero
tocaría un archivo commiteado bajo el sello de B5.4: **si se hace, se
declara como corrección post-sello con su selftest, no en silencio.**

**Costo:** USD 0 de API. **Tiempo:** 1 sesión + adjudicación de la
autora (~30 filas). **Riesgo:** bajo. **Laudo firmado a reabrir:**
ninguno, por el camino del perfil.

### Opción B — escalar con los roles sin miembros, declarándolo

**Qué queda roto:** lo de §2 — la navegación taxonómica hacia los 30
TOs nuevos. Consultas que no se podrían responder por el grafo: toda
pregunta por clase que deba alcanzar normas de esos TOs («qué le exige
la normativa a las entidades financieras» alcanzaría los 5 TOs dev y
no los 30 nuevos). Las consultas por documento y por texto siguen
funcionando.

**Efecto sobre la tesis:** la limitación cae sobre el mecanismo que el
capítulo presenta como aporte del catálogo (§3 del capítulo del
esquema: «la jerarquía del dominio es parte del recurso, consultable
con las mismas operaciones»). Declararla es honesto, pero la
declaración contradice parcialmente esa oración para la mayor parte
del corpus escalado.

**Costo:** USD 0 ahora. **Tiempo:** 0. **Artefactos sellados:**
ninguno. **Deuda:** el grafo publicado tiene 30 roles huérfanos; la
corrección posterior es una release nueva (principio 9).

### Opción C — no emitir rol para los TOs nuevos, dejar caer a clase

**Qué habría que revertir del cableado hecho:** en `perfil_e1`,
`ROL_POR_TO_V3` deja de mapear los 30 (quedan sin entrada, como los
huecos `docvig`/`fimipyme`); el mensaje por chunk pierde su línea de
alcance para esos TOs; el enum del catálogo conserva los 30 ids sin
uso o se poda —y podarlos **sí cambia el prefijo y rompe el sello**,
lo que exige re-sello y **reabrir el laudo B5.4 firmado**.

**Consecuencia medida (U-SUJ-ROL):** 90,4 % resuelto contra el
catálogo, con aplanamiento a la clase más amplia, válvula al 9,6 % y
emisiones cross-TO — es decir, **se reintroduce el defecto que la
opción A2 del laudo B5.4 fue diseñada para resolver**, y cuya
resolución la pareada midió en 8/8.

**Costo:** USD 0 de API, pero **exige reabrir un laudo firmado** si se
podan los ids. **Tiempo:** 1–2 sesiones + re-sello + laudo.

## §4. Shape S15 — evaluación independiente de la opción

**Corresponde implementarla, y la recomendación no depende de qué
opción se elija.** Fundamento: S15 («todo rol tiene `miembro_de` no
vacío, y sus miembros son clases del árbol») es exactamente la guarda
que habría convertido este hueco en un freno automático en vez de un
hallazgo de relevamiento. Con la opción A pasa a verde y protege
contra la regresión; con la B **falla por diseño**, y esa falla
declarada es una forma mucho más fuerte de documentar la limitación
que una nota en prosa; con la C queda sin objeto para los 30 pero
sigue protegiendo a los 5 dev.

**Costo:** ~½ sesión (el validador tiene 12 shapes con el patrón
hecho). **Ubicación natural:** `scripts/shapes_validator.py`, que no
es zona sellada. **Nota de alcance:** implementar S15 **no** implica
implementar S13, S14, S16 y S17 —también pendientes—; si se quiere
cerrar la serie, es otra unidad.

## §5. `tabla_to_rol_post_f1.md` — cómo se incorpora

El laudo B5.4 fase 1 la declara «la guarda del mapeo» de los 66 TOs, y
**no está en el repositorio ni en su historia** (verificado). Vivió
solo en el paquete de revisión de aquella sesión, en el scratchpad.

**Propuesta:** la reconstruye y versiona **la misma unidad que ejecute
la opción elegida**, porque es su insumo directo — la adjudicación de
miembros del rol se hace sobre esos mismos pasajes. Se regenera con el
script del freno 1 (que sí quedó en el paquete) o se rehace desde
`e0_dry`, y se versiona bajo el directorio de la unidad nueva, con nota
de que reconstruye el artefacto citado por el laudo. Si se eligiera la
opción B, se versiona igual: un laudo firmado no puede citar como
guarda un artefacto que no existe.

## §6. Corrección de `docs/plan_tesis.md:621`

Dice «31 roles + 35 mapeos»; el artefacto sellado dice **30 roles + 36
mapeos** (verificado: 35 roles totales − 5 dev = 30; 71 entradas − 35
rol = 36 clase). La fila se corrige en el pase que acompañe la decisión
de la autora. **Es corrección de registro, no de contenido:** el
mini-laudo del freno 2 de B5.4 movió `snp_cec` de rol a clase (31→30 y
35→36) y la fila del plan quedó con los números previos.

## §7. Lo que este diseño NO hace

No ejecuta ninguna opción, no toca el catálogo v3 ni artefactos
sellados, no corre el escalado, no implementa S15, no reconstruye la
tabla y no corrige la fila del plan: todo eso espera la decisión de la
autora.
