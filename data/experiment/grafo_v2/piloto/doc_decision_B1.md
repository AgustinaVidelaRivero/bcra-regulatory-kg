# Decisión del gate B1 — Piloto multi-modelo de extracción

**Decisión: la extracción v2 (subset y escalado) se realiza con `claude-haiku-4-5-20251001`.**
Fecha: 26/07/2026. Regla de decisión pre-declarada (R5, registrada antes de las corridas): *Haiku gana salvo que un modelo mayor lo domine estrictamente en ≥2 de las 3 familias de métricas con margen material, y su proyección de costo sea compatible con la política de cómputo.* Resultado: ningún modelo dominó a Haiku en ninguna familia completa. Contingencia de doble extracción: **no activada**.

## 1. Diseño del gate (resumen)

Muestra de 18 chunks (10 del bestiario de defectos conocidos, 4 de sujetos, 3 controles, 1 de fórmulas), answer key adjudicada contra los PDF y **sellada por commit (9271248) antes de toda corrida**, con acta de criterio pre-lectura para ambigüedades detectadas post-sellado. 3 modelos (Haiku 4.5 / Sonnet 4.5 / Opus 4.5, snapshots fechados) × 2 réplicas × 18 chunks = 108 llamadas, caché con namespace por modelo×réplica y assert automático de corrida fresca (6/6 pasaron). Costo real total: USD 6,49. Scoring mecánico contra la key (evidencia) + adjudicación humana final (veredictos).

## 2. Tabla adjudicada (post-clasificación de artefactos del scorer)

| Modelo · réplica | F1 contenido (hits sobre 93) | F1 emparejamientos REALES | F2 sujetos (equiv. extensional acreditada) | F2 prohibidos reales | Cuarentena (legítimas) | Sospechosas reales | F3 shapes (S12 huérfanas) | Δ entre réplicas | USD real |
|---|---|---|---|---|---|---|---|---|---|
| haiku · r1 | 42 | 0 | mejor familia | 0 | 0/0 | 0 | 0 | Δhits 10 (la mayor; concentrada en el chunk de fórmulas) | 0,390 |
| haiku · r2 | 32 | **1 (quimera 90/180 real)** | mejor familia | 0 | 1/1 | 0 | 1 | | 0,386 |
| sonnet · r1 | 37 | 0 | déficit real: colapsa enumeraciones al rol (prot::1.1, prot::2.5) | 1 (rol en enumeración) | 2/2 | 0 | 8 | Δaristas 56 | 1,175 |
| sonnet · r2 | 35 | 0 | ídem | 1 | 3/3 | 0 | 2 | | 1,108 |
| opus · r1 | 36 | 0 | paridad con haiku | 0 | 4/4 | 0 | 11 | Δnodos 4 (el más estable) | 1,724 |
| opus · r2 | 39 | 0 | paridad | 0 | 6/6 | 0 | 8 | | 1,711 |

Proyección al corpus completo (173,5 MB, método de bytes): Haiku ≈ USD 123 · Sonnet ≈ USD 361 · Opus ≈ USD 544.

## 3. Adjudicaciones registradas (con evidencia en informes/)

1. **Prohibido uniforme `rol_alcance_capmin` @ 9.1 (6/6 corridas) y patrón "faltante EF" en chunks de CapMin/RI: equivalencia extensional acreditada.** El rol de CapMin tiene como único miembro a EntidadFinanciera; usar uno u otro es extensionalmente idéntico. Uniforme entre modelos → impacto diferencial cero. (La key fue estricta; se registra para la key del gauntlet U5.)
2. **Déficit F2 de Sonnet: real.** En los dos chunks de enumeración explícita de sujetos, Sonnet colapsó al rol colectivo (prot::1.1: 2/10 cubiertos vs 7/10 de Haiku; prot::2.5: único modelo con el rol prohibido). Comportamiento consistente del modelo, penalizado conforme a la regla R1 de la key.
3. **Emparejamientos del scorer: 25 de 26 disparos fueron artefactos**, con tres causas verificadas por inspección de nodos (informe inspeccion_postgate): (i) nodo-tabla fiel (la tabla completa en un nodo dispara los pares cruzados por co-ocurrencia; adherencia interna verificada correcta en las 6 corridas del 12.1); (ii) substring ("vinculada" ⊂ "no vinculada"; "5"/"B" numéricos); (iii) ceguera a la negación ("NO podrá implicar mejora" dispara "emergencia↔mejora"). **El disparo restante es una quimera real** (haiku-r2, 13.2): label "90 días" sobre description del 13.2.6 (no vinculadas) + umbral "0 días" no literal — reproducción del patrón CQN2-013.
4. **Cuarentenas: 16/16 propuestas legítimas, cero evasiones de catálogo.** El patrón "la cuarentena crece con la capacidad del modelo" (0-1 / 2-3 / 4-6) es cautela, no desobediencia: los modelos mayores proponen donde el catálogo genuinamente carece de la clase.
5. **Sospechosas del verificador léxico: 30/30 falsos positivos** con cuatro causas mecánicas (coordinación "financieras **o** cambiarias" rompe la contigüidad del bigrama; singular del texto vs plural del catálogo; inferencia pre-anotada como razonable en la key [emisor de títulos]; label del catálogo ≠ calificador del texto [fiduciario, tensión pre-anotada]). **Cero errores reales de sujeto en 108 llamadas de tres modelos** — la capa de sujetos del esquema v2 (enum + reglas R1/R2 + alias) resistió bajo los tres.

## 4. Lectura R5 y decisión

F1: paridad de medias (37 / 36 / 37,5), con Haiku menos estable entre réplicas (Δ10, concentrado en fórmulas) y una quimera real en r2; sin dominación. F2: Haiku primero (Sonnet con déficit real; Opus empata). F3: mixto (Opus más estable en tamaño; 8-11 excepciones huérfanas vs 0-1 de Haiku); sin dominación estricta. **Ningún modelo domina a Haiku en ≥1 familia completa; la regla exige ≥2 → Haiku gana**, con costo 3-4,4× menor. Los defectos de capa de contenido (quimera, amputaciones uniformes del chunk largo 1.4) son independientes del modelo o varianza, y pertenecen al pipeline de refinamiento — consistente con su pre-registro como controles negativos del esquema.

## 5. Condiciones y backlog activados por esta decisión

- **Condición Bedrock (pineada en piloto_config.json, ACTIVA):** antes de la primera tanda bulk del escalado, verificar que Bedrock ofrece exactamente `claude-haiku-4-5-20251001`. Si no lo ofrece, la decisión vuelve a la mesa — no se extrae con un snapshot distinto del piloteado.
- **Backlog pre-escalado:** (i) corregir los precios hardcodeados del tracker (imprime costos de Haiku para todo modelo; detectado y compensado a mano en B1b); (ii) calibrar el verificador léxico con las dos causas nuevas de FP (coordinación con "o"; singular/plural del catálogo) — con disciplina de acta, antes del gate de U5; (iii) calibrar el scorer: chequeo de adherencia en el criterio "mismo nodo", listas de substrings mínimos, manejo de negación; (iv) actualizar el campo `estado` de piloto_config.json (quedó "PROPUESTA").
- **Para la answer key del gauntlet U5:** incorporar la cláusula "de no haber sido nominada una entidad" (Ext 11.1, diferida por acta) y revisar la exigencia EF-vs-rol en TOs de rol unipersonal.

## 6. Limitaciones declaradas

Muestra enriquecida en dificultad (mide separación en casos difíciles, no tasa media del corpus); N=18 sin potencia estadística (la regla R5 opera por dominación, no por significancia); el scoring mecánico subestima F1 en entradas compuestas (sesgo igual para los tres modelos, declarado en B1b); riesgo de anclaje del borrador en la adjudicación humana, mitigado por verificación contra PDF y actas pre-lectura.
