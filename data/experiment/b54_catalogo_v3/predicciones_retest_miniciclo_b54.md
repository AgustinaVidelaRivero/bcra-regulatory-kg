# Predicciones SELLADAS de los retests del mini-ciclo — U-B5.4 laudo de cierre

**SELLADAS ANTES DE CORRER** (la constancia es el sha256 de este archivo,
reportado en el freno exprés junto con el orden de operaciones de la sesión).
Las tres direcciones vienen fijadas por el laudo de cierre FIRMADO
(`docs/laudo_B5.4_cierre_catalogo.md`, resoluciones H1a/H2a/H4a); este
documento las vuelve verificables por unidad. Prefijo bajo prueba:
v3 re-sellado `35e88c2dd0a2…`, namespace `54a111e2175f`. Tope del gasto:
remanente **USD 0,2098**. Regla del laudo: si un retest FALLA su predicción,
FRENAR sin iterar (la vuelta es con laudo).

## R1 — `cap::3.1.14::intro` (H1a: rename del id de pagos)

- El originante de securitización **NO se emite** con
  `Sujeto_entidad_originante_de_transferencia` (ni con ningún otro id del
  catálogo ajeno a su naturaleza): queda en `sujeto_propuesto` o como omisión
  declarada.
- `Sujeto_fiduciario_de_fideicomiso_financiero` **se mantiene** entre los
  sujetos emitidos.

## R2 — `ayccef::2.1` (H4a: def dirigida de sector público)

- `Sujeto_sector_publico_no_financiero` **NO se emite**.
- La cobertura del sujeto cae en `Sujeto_entidad_financiera` y/o en
  `sujeto_propuesto`.
- El BCRA **sigue fuera** de los sujetos alcanzados (no reaparece como
  sujeto de `aplica_a`).

## R3 — `cryl::1.3` (H2a: guarda del rol en el mensaje)

- `Sujeto_rol_alcance_cryl` **NO aparece en `ejecuta`**.
- `Sujeto_bcra` **conserva** sus relaciones `ejecuta`.

## Estimación anclada (previa a la corrida)

- Escritura del prefijo v3 re-sellado en namespace nuevo: ≈12.880 tokens ×
  1,25 USD/MTok ≈ **0,016** (una vez, primera llamada).
- 3 unidades con caché caliente (costos medidos de las MISMAS unidades en la
  pareada: 0,0123 + 0,0074 + 0,0087 = 0,0284; el mensaje de las tres crece
  ~30 tokens por la guarda H2a, efecto < 0,001).
- **Total estimado: USD 0,040–0,050 < tope 0,2098.** Nota (regla d): el §4
  del laudo estima «≈0,02–0,03»; la diferencia es la escritura de caché del
  prefijo NUEVO (namespace rotado por el re-sello), que esa cifra no incluye.
- Disciplina: mismo runner-patrón de la pareada (CachingClient, secuencial,
  freno duro al tope, log de usage por llamada, modelo resuelto declarado,
  cruce db==jsonl, never-pay-twice).
