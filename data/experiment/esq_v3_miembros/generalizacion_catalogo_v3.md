# U-ESQ-V3 — Generalización del catálogo de sujetos a TOs frescos

**Entregable nombrado de la unidad.** Se REGENERA, no se edita a mano:

```bash
cd data/experiment/esq_v3_miembros/code && python3 generalizacion_catalogo.py
```

## Qué mide

Cuántos de los **69** colectivos de alcance que nombran los 30 TOs frescos del escalado tienen **id de clase veraz** en un catálogo derivado de 5 TOs de desarrollo. «Veraz» = el id existe, es de nivel `clase`, y **no aplana** al colectivo a su clase madre: lo que sobrevive a los laudos (a) y (b).

## La cifra

# 34/69 = 49.3 %

## Las tres cifras, rotuladas

La diferencia entre ellas **es** el registro de la adjudicación.

| escenario | cifra | % | descarte | ausencia de concepto | granularidad equivocada |
|---|---:|---:|---:|---:|---:|
| base, sin ningún rescate | 33/69 | 47.8 % | 36 | 26 (72.2 %) | 10 (27.8 %) |
| ADOPTADA — convca aceptado como enumeración parcial (laudo a.2); ctacor rechazado (su re-examinación no reprodujo) **← ADOPTADA** | 34/69 | 49.3 % | 35 | 26 (74.3 %) | 9 (25.7 %) |
| contrafáctico: si ctacor hubiera sobrevivido a la verificación | 35/69 | 50.7 % | 34 | 26 (76.5 %) | 8 (23.5 %) |

### Desglose de cada escenario, con su control

**base, sin ningún rescate** — 33/69 = 47.8 %

- descarte por ausencia de concepto (sin id en el catálogo): **26**
- descarte por granularidad equivocada: **10** (8 aplanamiento rechazado + 2 candidato de nivel instancia)
- control del descarte: `26 + 8 + 2 = 36`
- control del total: `33 + 36 = 69` sobre 69 — cierra: **True**

**ADOPTADA — convca aceptado como enumeración parcial (laudo a.2); ctacor rechazado (su re-examinación no reprodujo)** — 34/69 = 49.3 %

- descarte por ausencia de concepto (sin id en el catálogo): **26**
- descarte por granularidad equivocada: **9** (7 aplanamiento rechazado + 2 candidato de nivel instancia)
- control del descarte: `26 + 7 + 2 = 35`
- control del total: `34 + 35 = 69` sobre 69 — cierra: **True**

**contrafáctico: si ctacor hubiera sobrevivido a la verificación** — 35/69 = 50.7 %

- descarte por ausencia de concepto (sin id en el catálogo): **26**
- descarte por granularidad equivocada: **8** (6 aplanamiento rechazado + 2 candidato de nivel instancia)
- control del descarte: `26 + 6 + 2 = 34`
- control del total: `35 + 34 = 69` sobre 69 — cierra: **True**

## El descarte, partido en dos (lo que la cifra tiene para decir)

Sobre la cifra adoptada, el hueco **no es homogéneo**: son dos problemas opuestos con remedios opuestos, y publicar un cubo único los esconde.

| naturaleza del hueco | n | % del descarte | remedio |
|---|---:|---:|---|
| **ausencia de concepto en el catálogo** | 26 | 74.3 % | abrir ids — mecánico, re-sello del prefijo v3 |
| **granularidad equivocada** | 9 | 25.7 % | modelado (una clase más específica, o la firma de `miembro_de`) |
| control | 35 | 100 % | `26 + 7 + 2 = 35` |

**Casi tres cuartos del hueco (74.3 %) son cobertura, no modelado.** Un catálogo derivado de 5 TOs no conoce las transportadoras de valores, las infraestructuras del mercado financiero ni las plataformas de financiamiento MiPyME sencillamente porque esos 5 TOs no las mencionan; abrirles id es trabajo mecánico. El cuarto restante es distinto: ahí el concepto existe y lo que falla es a qué granularidad se lo modeló.

## Advertencia que viaja con la cifra

**NO es comparable con el 96,9 % de cobertura del catálogo que ya está en el tramo 2 del capítulo (`main.tex:679`).** Difieren en cuatro cosas:

1. **Denominador:** 4.029 relaciones con sujeto EMITIDAS, contra 69 colectivos NOMBRADOS en cláusulas de alcance.
2. **Unidad:** una mención individual, contra un colectivo — que muchas veces es una unión de varios sujetos.
3. **Material:** desarrollo más los diez de cobertura, contra 30 TOs frescos del escalado.
4. **Y el que muerde:** el 96,9 % cuenta lo que el extractor **eligió emitir**. Un colectivo sin id puede no llegar nunca a producir una relación con sujeto y caer fuera de ese denominador — **la cifra baja puede explicar en parte por qué la alta es alta**.

**Las dos cifras no van juntas en el capítulo sin este párrafo.**

