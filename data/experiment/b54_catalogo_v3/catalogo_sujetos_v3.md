# Catálogo de sujetos v3 — artefacto de U-B5.4 fase 2

Materializa el laudo de fase 1 (`docs/laudo_B5.4_fase1_catalogo.md`, FIRMADO
05/09/2026) sobre el prefijo congelado (`e69feaaa…`/`1be8304e3d77`, laudo de
esquema congelado `2593d4d` §4). Módulo:
`data/experiment/b54_catalogo_v3/code/prompt_v3_b54.py`; verificación:
`python3 data/experiment/b54_catalogo_v3/code/selftest_prompt_v3_b54.py`
(corre desde cualquier cwd; 50 checks). Costo de API de la fase: USD 0.
Incorpora la corrección del mini-laudo de la autora del freno 2 (sección
«Correcciones del freno 2», abajo).

**El cableado a producción NO es de esta unidad** (frontera B5.3): el pipeline
de producción sigue usando su prefijo; este artefacto queda sellado a la
espera de la integración post-B5.3.

## Sellos

| qué | valor |
|---|---|
| sha256 del texto del prefijo v3 | `29af2e29880b8e435cc40a93913b911ae9db9d2feab43d06c9ecfca2e3652edf` |
| hash canónico system+tools (namespace de caché) | `4ed889c74cb8` |
| base congelada (verificada por candado) | `e69feaaa04779bd6347cc9e3974d2c1749519f1230e70a0459e66f46517cd720` / `1be8304e3d77` |
| tamaño | system 25.652 → 33.278 chars; tools 7.181 → 8.999; total +9.444 chars ≈ +2.871 tokens (+28,8 %; ratio 3,29 chars/token, ancla cw ESQ-2 = 9.983) |
| costo del delta por corrida completa (6.340 unidades, claude-haiku-4-5) | cache reads +USD 1,82; write del prefijo USD 0,016 |

*(Sellos previos al mini-laudo del freno 2 —`852d247c905f…`/`f525c2923795`, 103 ids—
superseded por la corrección de abajo; constan en el paquete del freno 2.)*

## Composición (recomputada por el selftest — regla i)

**102 ids = 70 vigentes − 5 retiros + 7 adiciones + 30 roles A2** (mini-laudo
del freno 2, abajo), desglose **62 clases + 5 instancias + 35 roles**. El enum
de `sujeto_id` y el de `sujeto_propuesto_padre_sugerido` son idénticos (como
en el congelado).
Definiciones en el bloque: **30 líneas `def:`** = 24 dirigidas (laudo F1.3) +
6 posicionales de adiciones (F1.4; `Sujeto_fmi` va sin def por ser instancia
autoevidente, mismo criterio que el resto de las instancias).

## Retiros (laudo F1.5) — LÁPIDAS

Retirados del bloque de catálogo y de ambos enums el 05/09/2026 por el laudo
`docs/laudo_B5.4_fase1_catalogo.md` §F1.5. Evidencia completa:
`ids_sin_uso_post_f1.md` (paquete del freno 1). Ningún nodo de los grafos del
universo primario los referencia (0 usos medidos, U-SUJ-FREQ §2.a). Destino:
r2 si reaparece demanda documental.

| id (lápida) | evidencia de no-uso |
|---|---|
| `Sujeto_acreedor_del_exterior` | 0 usos en 2.525 unidades del universo primario, aun con su TO natural (`ext`) en dev; 1 mención léxica en los 68 (`fimipyme::3.2.2`) |
| `Sujeto_autoridad_nacional_de_aplicacion` | 0 usos; 0 menciones de «autoridad nacional de aplicación» en los 68 (las 9 de «autoridad de aplicación» genérica no son este id) |
| `Sujeto_secretaria_de_comercio` | 0 usos; 0 menciones en los 68 |
| `Sujeto_secretaria_de_energia` | 0 usos; 0 menciones en los 68 |
| `Sujeto_secretaria_de_transporte` | 0 usos; 0 menciones en los 68 |

## Mantenidos con marca de revisión en r2 (laudo F1.5)

- `Sujeto_ministerio_de_economia` — evidencia débil (7 menciones/4 TOs, casi
  todas citas de resoluciones); lo sostiene `fabcra::S1::chapeau_seccion`
  (sujeto real de la operatoria de firmas). **REVISAR EN r2.**
- `Sujeto_sociedad_de_proposito_especial` — 2 menciones (`lingeef::3.3.1.8`);
  lo sostiene el tamaño de lingeef (613 unidades). **REVISAR EN r2.**

## Adiciones (laudo F1.4)

7 entradas, cada una con su evidencia citada en `adiciones_0_3_post_f1.md`
(freno 1) y su línea en el bloque v3: `Sujeto_entidad_girada`,
`Sujeto_entidad_depositaria`, `Sujeto_entidad_originante` (con guarda
anti-atracción contra el «originante» de securitización, en su `def:`),
`Sujeto_entidad_receptora`, `Sujeto_camara_electronica_de_compensacion`
(CEC — enmienda de alcance de la autora declarada en el laudo),
`Sujeto_banco_central_del_exterior`, `Sujeto_fmi`. CCP: duplicado reportado,
sin acción (el id `Sujeto_entidad_de_contraparte_central` ya existía).

**Decisión de ejecutor declarada (para revisión):** el `padre` de las 5 clases
nuevas del SNP/CEC es `Sujeto_sujeto_regulado` (son sujetos regulados por los
TOs del SNP); para CEC la sugerencia emitida por el modelo en el universo
primario era `Sujeto_estructura` (n=2, U-SUJ-FREQ) — se optó por sujeto
regulado porque `snp_cec` les impone condiciones de funcionamiento. El campo
`padre` es metadato en `ADICIONES_V3` (el bloque del prefijo agrupa por rama y
no serializa padres); la integración documental a `esquema_v2_clases.json` es
del paso de cableado post-B5.3.

## BIS — caso de promoción (laudo F1.4: NO entra)

`Sujeto_bis` NO integra el catálogo v3. Evidencia disponible al 05/09/2026:
1 mención como contraparte (`ratiofn::3.3.3.3`, activos emitidos/garantizados),
1 como autor de estándares (`pimf::1.1::intro`, CPMI/IOSCO — no es alcance),
2 emisiones de `sujeto_propuesto` en dev (`cap::6.2.1.1`, grupo `banc+pago` de
U-SUJ-FREQ). **Se promueve si**: aparece como sujeto/contraparte en ≥1 TO
adicional del corpus escalado (las emisiones de `sujeto_propuesto` de la
corrida de tandas 1–2 son la medición natural), o si la validación temporal /
r2 lo trae con evidencia de alcance. Mientras tanto: `sujeto_propuesto` con
`padre_sugerido = Sujeto_organismo_internacional` es la conducta esperada.

## Roles A2 (30) y mapeos a clase (36)

- 30 ids `Sujeto_rol_alcance_<to>` (uno por TO cuyo alcance NO es clase
  exacta), líneas al final del bloque con el patrón de los 5 roles dev.
- 36 TOs mapeados en `ROL_POR_TO_V3` directamente a su clase (26 a
  `Sujeto_entidad_financiera`; apnf, cajasc, ctacte, ctavis, fclef, fgarcp,
  pscpp, socgar a su clase propia; `snp_cec` a
  `Sujeto_camara_electronica_de_compensacion` por el mini-laudo del freno 2;
  `ri2_ci` a DOS clases — casa y agencia de cambio — con variante declarada
  de la línea de mensaje: «usá Sujeto_casa_de_cambio o
  Sujeto_agencia_de_cambio como sujeto, según corresponda»).
- `ROL_POR_TO_V3` = 71 entradas (5 dev pass-through byte-idénticas a
  producción + 66 nuevas). **docvig y fimipyme SIN entrada** (huecos del laudo
  F1.2, válvula `sujeto_propuesto` abierta, re-mirada en tanda 1).
- La guarda del mapeo es `tabla_to_rol_post_f1.md` (freno 1), fila por fila
  con cita.

## Correcciones del freno 2 — MINI-LAUDO (transcripción)

**Mini-laudo de la autora, 05/09/2026, freno 2** (revisión de mesa
coincidente):

1. **Hallazgo 1 (CEC × snp_cec): OPCIÓN (A)** — se retira
   `Sujeto_rol_alcance_snp_cec`; `snp_cec` mapea a la clase
   `Sujeto_camara_electronica_de_compensacion`. Fundamento registrado:
   aplicación del criterio A2 del laudo de fase 1 a la interacción creada por
   la propia enmienda CEC — el mismo principio rige para lo que la autora
   agrega. **No es lápida** (el rol nunca integró un catálogo sellado): es
   corrección pre-sello, con este registro.
2. **Hallazgos 2, 3 y 4: RATIFICADOS** — variante `ri2_ci` declarada y
   testeada; `fmi` sin def por criterio de instancia (cubierto por la
   cláusula de F1.3); padre `Sujeto_sujeto_regulado` con el argumento de
   infraestructura regulada que consta arriba.

Materialización de la corrección: el rol retirado está AUSENTE de todo el
prefijo v3 y de ambos enums (checks propios del selftest); composición
102 = 70 − 5 + 7 + 30, reparto `ROL_POR_TO_V3` 35 rol (5 dev + 30) / 36
clase. El registro del hallazgo original (con la composición 103 laudada en
fase 1) queda en el paquete del freno 2.

## Diferencias menores mandato/laudo ↔ materialización (regla d)

1. Hallazgo CEC×snp_cec: **RESUELTO por el mini-laudo de arriba** (opción A).
2. `ri2_ci` (mapeo a DOS clases): la línea de alcance del mensaje usa una
   variante declarada del template de producción (el template original asume
   un único id). Verificada en el selftest. **RATIFICADO (mini-laudo, freno 2).**
3. `Sujeto_fmi` entra sin línea `def:` (criterio de instancias del F1.3
   aplicado por el ejecutor; las otras 6 adiciones sí llevan def posicional).
   **RATIFICADO (mini-laudo, freno 2).**
4. Padre `Sujeto_sujeto_regulado` de las clases SNP/CEC (decisión de ejecutor
   argumentada arriba). **RATIFICADO (mini-laudo, freno 2).**
