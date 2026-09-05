# Predicciones SELLADAS de la verificación pareada — U-B5.4 fase 2

**SELLADO en el freno 2, ANTES de toda corrida.** La fase 3 no gasta sin
autorización explícita sobre el freno 2 (tope USD 0,50). Actualiza las
predicciones propuestas del freno 1 (`diseno_pareada_post_f1.md`) a los laudos
de `docs/laudo_B5.4_fase1_catalogo.md` y al mini-laudo de la autora del
freno 2 (05/09/2026: rol de snp_cec retirado, snp_cec mapea a la clase CEC).
Prefijo bajo prueba: v3 (`29af2e29880b…`, namespace `4ed889c74cb8`);
comparación por unidad de
`sujeto_id`/`sujeto_propuesto` en `validacion.relaciones` contra la extracción
persistida del universo primario (misma capa que U-SUJ-FREQ).

**Semilla declarada para el orden aleatorizado de fichas:** `b54-pareada-v1`.

Regla de lectura: «PASA» es por unidad contra su predicción; los casos
marcados FICHA van a adjudicación de la autora en orden aleatorizado (la
predicción no se fuerza sobre juicio semántico).

## Brazo A — estabilidad de los 5 roles dev (10 unidades)

`cap::1.1`, `cap::1.2`, `cla::1.1`, `cla::1.2.1`, `pro::1.1.1`, `pro::1.1.2.7`,
`ric::1.1`, `ric::1.2`, `ext::1.2`, `ext::1.3`.
**P-A**: cada unidad conserva el rol de su TO propio (el mismo `sujeto_id` rol
que en la extracción persistida). Cero regresiones.

## Brazo B — atracción cross-TO ya observada en ESQ-2 (8 unidades)

Unidades que en el universo primario usaron el rol de un TO dev AJENO.
**P-B (laudo F1.2: los TOs con mapeo a clase predicen CLASE, no rol):**

| unidad | usó (persistido) | predicción v3 |
|---|---|---|
| `ayccef::2.9.2::intro` | `Sujeto_rol_alcance_capmin` | `Sujeto_entidad_financiera` (ayccef mapea a clase) — FICHA si el pasaje refiere genuinamente al régimen de capitales mínimos |
| `actgar::2.3.6.3` | `Sujeto_rol_entidad_autorizada_exterior` | `Sujeto_entidad_financiera` — FICHA si es referencia legítima al régimen cambiario |
| `actgar::2.7.2` | `Sujeto_rol_entidad_autorizada_exterior` | ídem actgar::2.3.6.3 |
| `expaef::5.7.1.2` | `Sujeto_rol_entidad_autorizada_exterior` | `Sujeto_entidad_financiera` — FICHA ídem |
| `expaef::5.7.1.3` | `Sujeto_rol_entidad_autorizada_exterior` | ídem |
| `lavdin::1.1.1` | `Sujeto_rol_sujeto_obligado_proteccion` | `Sujeto_rol_alcance_lavdin` (lavdin tiene rol propio v3) |
| `lavdin::1.3.3` | `Sujeto_rol_sujeto_obligado_proteccion` | `Sujeto_rol_alcance_lavdin` |
| `cryl::4.1` | `Sujeto_rol_entidad_comprendida_reginf` | `Sujeto_rol_alcance_cryl` |

**P-B-global (laudo: no-migración cross-TO de roles):** en NINGUNA unidad de
la pareada aparece un `Sujeto_rol_*` de un TO distinto del propio.

## Brazo C — `sujeto_propuesto` → adiciones F1.4 (7 unidades)

- `cap::6.2.1.1`: «Banco Central Europeo»/«Bancos centrales» →
  `Sujeto_banco_central_del_exterior`; «Fondo Monetario Internacional» →
  `Sujeto_fmi`; «Banco de Pagos Internacionales» → **SIGUE en
  `sujeto_propuesto`** (BIS no entró; su caso de promoción está en
  `catalogo_sujetos_v3.md`).
- `cryl::3.1`: «Cámaras Electrónicas de Compensación» →
  `Sujeto_camara_electronica_de_compensacion` (**la CLASE** — consistente con
  el mini-laudo del freno 2: el rol de snp_cec no existe; no hay unidades de
  snp_cec en la muestra porque ese TO no tiene extracción persistida);
  «Mercados de Valores» y «Centrales Depositarias» → SIGUEN en
  `sujeto_propuesto` (no entraron).
- `traval::1.1::intro`, `traval::2.3`, `traval::S2::cierre`: el colectivo del
  TO → `Sujeto_rol_alcance_traval`; las menciones de PSTV/TVP como subtipos
  específicos pueden seguir en `sujeto_propuesto` — FICHA en ambos sentidos
  (la guarda es: NINGUNA se fuerza a un id ajeno).
- `expaef::9.3`, `expaef::9.5.3`: «agencia complementaria de servicios
  financieros» → SIGUE en `sujeto_propuesto`; la definición de
  `Sujeto_empresa_de_servicios_complementarios` NO la atrae.

## Brazo D — anti-atracción de potestades (5 unidades; guarda (c) §0.5)

`ayccef::2.1`, `ayccef::3.1`, `ayccef::4.1`, `cryl::1.3`, `cryl::3.2::intro`.
**P-D**: las relaciones `ejecuta` de potestades del organismo conservan
`Sujeto_bcra`; ninguna migra al rol de alcance del TO ni a
`Sujeto_entidad_financiera`.

## Brazo E — controles de clase estable (3 unidades)

`actgar::1.2`, `actgar::2.2.2`, `actgar::2.4.1`.
**P-E**: `Sujeto_entidad_financiera` se conserva (actgar mapea a esa misma
clase: la línea de alcance no cambia el id).

## Brazo F — anti-atracción del id SNP nuevo (1 unidad)

`cap::3.1.14::intro` (emitió «originante»/«originante/fiduciario»,
securitización). **P-F**: NO emite `Sujeto_entidad_originante` (id del esquema
de pagos, con guarda en su `def:`); el sujeto sigue en `sujeto_propuesto`.

## Estimación anclada (tope USD 0,50)

- 34 unidades × tarifa E1 medida 0,007062 USD/unidad (banda 0,006274–0,008798;
  `resumen_escalado.md` §1) = **0,240** (banda alta 0,299).
- Escritura del prefijo v3 en namespace nuevo: 12.854 tokens ≈ **0,016**
  (claude-haiku-4-5, cache write 1,25 USD/MTok; una vez).
- Línea de alcance nueva en mensajes de TOs ESQ-2 de la muestra: < 0,01.
- Margen por reintentos/cortes (~15 %): +0,04.
- **Total estimado: USD 0,26–0,36 < 0,50.**

Mecánica de la fase 3 (tras autorización): runner y caché PROPIOS de la unidad
(`code/` + `.gitignore` de dos líneas patrón esq), lectura previa de
`docs/decisiones_caching_extraccion.md` (las cinco decisiones vinculantes),
skill llm-capture, captura del crudo íntegro, cruce db==jsonl, modelo resuelto
por llamada declarado en el reporte, never-pay-twice.
