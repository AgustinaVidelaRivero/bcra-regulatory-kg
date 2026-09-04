# Diseño de B5.4 — Catálogo de sujetos v3, en DOS variantes (borrador de mesa)

**BORRADOR** acoplado a la disyuntiva del laudo B5.5 §3: una variante por
rama, para que ninguna espere a la otra. Lo común a ambas va primero; las
preguntas que cada variante le deja a la autora, al final de cada una.
Restricción heredada del laudo de esquema congelado (`2593d4d` §4): B5.4
integra el prefijo congelado TAL CUAL (`e69feaaa…`/`1be8304e3d77`) — el
catálogo de sujetos es la única pieza que se agrega, y su integración
produce EL prefijo de producción del escalado (una rotación declarada).

## §0. Común a las dos variantes

1. **Inventario exacto del catálogo vigente** (primera tarea de la unidad,
   $0): el catálogo vive en el tool schema y en el bloque de sujetos del
   prompt; el grep de prosa muestra 5 ids nombrados y las extracciones
   usan más — el inventario se hace contra el schema, no contra la prosa.
2. **Insumo medido, patrón U-R9-FREQ ($0)**: análisis de frecuencia de
   `sujeto_propuesto` sobre TODAS las extracciones persistidas (dev + las
   1.000+ de ESQ/3b/v2), con agrupador mecánico y criterio de corte
   sellado ANTES de mirar — es la evidencia de qué sujetos reales faltan.
   (Precedente directo: así se decidió el enum de R9, y así se rechazó su
   segunda mitad.)
   **RESULTADO (U-SUJ-FREQ, corte sellado ≥20/≥5 TOs/≥2 ESQ-2): 0 de 70
   grupos pasan — 124 propuestos sobre 4.029 relaciones (3,1 %),
   fragmentados; ni la fila laxa informativa promueve nada. Y el
   inventario contra el tool schema corrige la premisa de este diseño:
   el catálogo vigente tiene 70 ids (58 clases + 7 instancias + 5
   roles), no «5»; sin definiciones positivas (solo label/alias/nivel/
   padre); 14 ids sin uso en el universo primario; los sujetos del plan
   §0.3 aparecen con frecuencias mínimas (FMI 2, BIS 2, bancos
   centrales 3). El trabajo de B5.4 se desplaza: no es expandir por
   frecuencia — es rol_alcance por TO, definiciones positivas,
   adiciones documentales del §0.3 y decisión sobre los 14 sin uso.**
3. **Los sujetos ya identificados por el plan**: SNP (entidad girada /
   depositaria / receptora / originante — del scoping A2), bancos
   centrales, FMI, BIS, CCP.
4. **Rol de alcance por TO** (levanta la cuarentena D5): el mecanismo por
   el cual cada TO declara su sujeto por defecto, para que el vacío del
   rol deje de ser condición conocida. Diseño del mecanismo idéntico en
   ambas variantes; cambia solo la tabla TO→rol que lo puebla.
5. **Guardas anti-atracción, obligatorias** (lección de ESQ-3b y de las
   confusiones medidas — PSTV forzadas a un id ajeno; actos del BCRA
   atribuidos a la entidad): (a) definición POSITIVA por sujeto (quién
   es), no lista de patrones léxicos; (b) `sujeto_propuesto` SIGUE ABIERTO
   en producción como válvula honesta (lo que no matchea se propone, no se
   fuerza — la conducta correcta ya observada en cryl::8.1); (c) el par
   autoridad/regulado explícito (las potestades son del organismo).
6. **Verificación pre-integración**: mini-corrida pareada sobre unidades
   ya extraídas con `aplica_a`/`sujeto_propuesto` conocidos (patrón
   ESQ-3b, brazo chico), con predicciones selladas — el catálogo tampoco
   entra sin verificar. Presupuesto a fijar en el mandato (~USD 0,3–0,5).

## §A. Variante A — catálogo MÁXIMO (rama A de B5.5: corpus completo, una rotación)

Además de §0: inventario de sujetos por los GÉNEROS del índice completo
(157 TOs) — muestreo documental de los no digeribles y del bloque RI
(lectura de encabezados/alcances, $0) para candidatear sujetos que el
desarrollo nunca vio (p. ej. actores del régimen informativo, sujetos de
TOs cambiarios/no digeribles). Cada candidato entra con su evidencia
documental citada o NO entra (el principio de gobierno aplicado al
catálogo).

**Preguntas que esta variante le deja a la autora:**
- A1. ¿Techo del catálogo? (la mesa propone: sin techo numérico pero con
  la regla «cada id con ≥N apariciones documentales citadas», N a laudar).
- A2. ¿Los sujetos del bloque RI entran con evidencia solo-documental
  (sin extracción medida, porque E0 no lee ese bloque todavía) o se
  marcan como subcatálogo provisional dentro del catálogo único?
- A3. ¿La jerarquía (padre_sugerido de sujetos) se puebla ahora para todo
  el árbol o solo donde hay evidencia de uso?

## §B. Variante B — catálogo AJUSTADO a los 68 digeribles (rama B: rotación futura asumida)

Además de §0: el inventario se limita a los géneros de los 68 (normativa
general) — el análisis de `sujeto_propuesto` del §0.2 es LA fuente
principal, complementada por los sujetos del plan (§0.3) y el muestreo
documental SOLO de los 68. Los sujetos del bloque RI quedan explícitamente
FUERA, con nota de destino (ESQ-RI-3, que definirá los suyos con su propia
evidencia y rotará el prefijo como release declarada).

**Preguntas que esta variante le deja a la autora:**
- B1. El criterio de corte del análisis de `sujeto_propuesto` (mínimo de
  apariciones y de TOs para que un propuesto ascienda a id del catálogo —
  espejo del corte de U-R9-FREQ; se sella antes de mirar).
- B2. ¿Se reservan ids «paraguas» para lo que el corte no promueve (p. ej.
  un genérico por familia) o el residuo queda en `sujeto_propuesto` como
  hoy? (La mesa recuerda el precedente del cajón: `cumplimiento_normativo`
  se rechazó por eso mismo.)
- B3. Si la reunión de mentores pide el test de generalización adicional
  (TOs vírgenes), ¿esa corrida mide también sujetos y su resultado entra a
  este catálogo antes de congelarlo?

## §C. Qué es idéntico en las dos y ya puede prepararse

El mecanismo del rol de alcance (§0.4), las guardas (§0.5), el diseño de
la verificación pre-integración (§0.6) y el análisis de frecuencia (§0.2)
son independientes de la rama: pueden mandatarse apenas B5.1 libere la
parametrización, sin esperar la firma de B5.5.
