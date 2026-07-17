# B4.3 ronda 2/3 — Regla mecánica de jerarquía para exoneraciones corregidas (s1-v0.3-dev)

Fecha: 2026-07-17. **Cambio SOLO en el recomputo/anotación de aplicar_s1** (código
determinístico del juicio) — S1_PROMPT, esquemas, ensamblado del input y fetch: INTACTOS.
Archivos tocados: s1_fuentes.py + su test. Sin commits. **Sin scoring** (prohibido
comparar contra casos_dev_v7.md).

## La regla (en el docstring del módulo, con su justificación estructural)

Cuando S1 corrige una atribución del gatillo de exoneración (sin_defecto → causa de
defecto):

- **Con patas no cubiertas en el síntoma** → `jerarquia="primaria"` y `pata=<la pata>`
  (una sola → esa; varias sin mapeo posible → el CONJUNTO con nota `mecanica_sin_mapeo`
  — el mapeo NO se inventa).
- **Sin patas (síntoma de claims)** → jerarquía acotada por la centralidad del claim
  mapeado (la lógica de R6b, reutilizando `_mapear_claim` de capa_deterministica): central
  → primaria; solo secundarios o sin mapeo → secundaria.
- `jerarquia_original` anotada en capa_s1; el voto_s1 recomputa contando estas primarias.
- Las correcciones del gatillo de CAUSAS no cambian de jerarquía por esta regla.

**Justificación estructural (espejo de R6b):** la severidad de la atribución queda acotada
por la severidad del síntoma declarado — R6b degrada primarias ligadas solo a claims
secundarios; esta regla promueve una corrección ligada a una pata no cubierta (el síntoma
más severo de completitud). Es un hecho del INPUT del instrumento, computable por código.

## pytest (verde completo: 87 = 83 previos + 4 de la regla)

```
87 passed
```

(Nota de desarrollo: el test de la promoción con 1 pata se escribió primero con una sola
rep y falló por la propia regla del protocolo — mayoría estricta ≥2 —; se corrigió el TEST
a 2 reps, no el módulo.)

## RE-CORRIDA v0.3 — SIN API (replay determinístico de las salidas congeladas de _s1c)

Mecanismo: el fetch es determinístico → las atribuciones "completo" salen en el MISMO
orden; un cliente de replay entrega las salidas LLM almacenadas en `_s1c.json` (con su
usage real) en ese orden. **Cero llamadas a la API**; salidas nuevas `_s1d.json`
(`version_capa_s1: s1-v0.3-dev`); `_s1.json`/`_s1b.json`/`_s1c.json` congeladas.

```
run_2/CQ-021: replay 0 salidas · corregidas=0
run_4/CQ-008: replay 2 salidas · corregidas=0
run_4/CQ-021: replay 3 salidas · corregidas=3
run_4/CQ-028: replay 3 salidas · corregidas=2
```

## Votos_s1 FINALES por caso (v0.3; sin scoring)

| Caso | voto_capa_d | voto_s1 v0.2 (_s1c) | **voto_s1 v0.3 (_s1d)** |
|---|---|---|---|
| run_2/CQ-021 | 2×{context_recall, completitud_kg} 3-0 | ídem | **ídem (sin cambio)** |
| run_4/CQ-008 | {context_recall, completitud_kg} 3-0 | ídem | **ídem (sin cambio)** |
| run_4/CQ-021 | **[] (clave vacía) 3-0** | [] (correcciones sin contar: jerarquía sin_par) | **{context_recall, completitud_kg} 3-0** — las 3 exoneraciones corregidas, promovidas a PRIMARIA por la regla |
| run_4/CQ-028 | {context_recall, completitud_kg} 2-1 | {noise_sensitivity, contenido_kg} 2-1 | **{noise_sensitivity, contenido_kg} 2-1 (sin cambio: gatillo de causas, la regla no aplica)** |

**Anotación verificada en r4/CQ-021** (rep 1, idéntica en las 3): `jerarquia: primaria`
(original `sin_par` preservada en capa_s1), `pata` = el CONJUNTO de las 2 patas no
cubiertas con `nota: mecanica_sin_mapeo` (el síntoma tiene 2 patas y la salida S1 no
permite mapear — no se inventó), `par_post_s1: [context_recall, completitud_kg]`,
`version: s1-v0.3-dev`.

Triage sin cambios: CQ-021 r4 sin triage; CQ-008 y CQ-028 con `fuente_no_verificable`
(el no_determinable y los fetch fallidos de siempre); r2/CQ-021 ídem (6 fetch fallidos).
Usage: el de _s1c transportado por el replay (30.143/3.434 total); cero tokens nuevos.

---

*Fin de B4.3 ronda 2/3. Regla mecánica implementada y testeada; recomputo puro sobre
salidas congeladas, cero API. Frenado para revisión.*
