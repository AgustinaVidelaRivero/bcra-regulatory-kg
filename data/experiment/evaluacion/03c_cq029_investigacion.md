# Investigación puntual de CQ-029 — A/B caching

4 corridas SIN cache + 4 CON cache, juzgadas individualmente. Objetivo: ¿la divergencia off-vs-on fue inestabilidad de frontera de la pregunta, o efecto del cache?

**Conclusión: ✅ INESTABILIDAD INTRÍNSECA: correctitud varía DENTRO del grupo sin cache → es no-determinismo run-to-run de la pregunta, no el cache. Equivalencia del caching sostenida para CQ-029.**

Distribución de correctitud — SIN cache: {'correcta': 3, 'parcial': 1} | CON cache: {'correcta': 2, 'incorrecta': 2}

| run | cache | correctitud | completitud | cita_doc | tools | citas |
|-----|:-----:|-------------|-------------|:--------:|------:|-------|
| off_1 | off | correcta | parcial | True | 10 | [('TO_proteccion_usuarios_servicios_financieros_actual.pdf', 'Punto 2.3. Recaudos mínimos de la relación de consumo')] |
| off_2 | off | correcta | parcial | True | 11 | [('TO_proteccion_usuarios_servicios_financieros_actual.pdf', 'Punto 2.3. Recaudos mínimos de la relación de consumo')] |
| off_3 | off | correcta | parcial | True | 9 | [('TO_proteccion_usuarios_servicios_financieros_actual.pdf', 'Punto 2.3. Recaudos mínimos de la relación de consumo')] |
| off_4 | off | parcial | parcial | True | 10 | [('TO_proteccion_usuarios_servicios_financieros_actual.pdf', 'Punto 2.3. Recaudos mínimos de la relación de consumo')] |
| on_1 | on | correcta | parcial | True | 11 | [('TO_proteccion_usuarios_servicios_financieros_actual.pdf', 'Punto 2.3. Recaudos mínimos de la relación de consumo')] |
| on_2 | on | incorrecta | parcial | True | 10 | [('TO_proteccion_usuarios_servicios_financieros_actual.pdf', 'Punto 2.3. Recaudos mínimos de la relación de consumo')] |
| on_3 | on | correcta | parcial | True | 10 | [('TO_proteccion_usuarios_servicios_financieros_actual.pdf', 'Punto 2.3. Recaudos mínimos de la relación de consumo')] |
| on_4 | on | incorrecta | parcial | True | 10 | [('TO_proteccion_usuarios_servicios_financieros_actual.pdf', 'Punto 2.3. Recaudos mínimos de la relación de consumo')] |

## Respuestas (primeros 200 chars) — para ver la variación de trayectoria

**off_1**: No, no pueden cobrarse comisiones ni cargos por operaciones realizadas por ventanilla a usuarios que sean personas humanas. Esta es una prohibición establecida en la regulación del BCRA. Según la info

**off_2**: No, no pueden cobrarse comisiones ni cargos por operaciones realizadas por ventanilla a usuarios que sean personas humanas. Esta es una prohibición establecida por el BCRA. Según la regulación, 'No po

**off_3**: No, no pueden cobrarse comisiones ni cargos por operaciones realizadas por ventanilla a usuarios que sean personas humanas. Esta es una prohibición clara establecida en la regulación del BCRA. Según l

**off_4**: No, no pueden cobrarse comisiones ni cargos por operaciones realizadas por ventanilla a usuarios que sean personas humanas. Esta es una prohibición general establecida en la regulación del BCRA. Según

**on_1**: No, no pueden cobrarse comisiones ni cargos por operaciones realizadas por ventanilla a usuarios que sean personas humanas. Esta es una prohibición clara establecida en la regulación del BCRA. Según l

**on_2**: No, no pueden cobrarse comisiones ni cargos por operaciones realizadas por ventanilla a usuarios que sean personas humanas. Esta es una prohibición absoluta establecida en la regulación del BCRA. Segú

**on_3**: No, no pueden cobrarse comisiones ni cargos por operaciones realizadas por ventanilla a usuarios que sean personas humanas. Esta es una prohibición establecida en la regulación del BCRA. Según la info

**on_4**: No, no pueden cobrarse comisiones ni cargos por operaciones realizadas por ventanilla a usuarios que sean personas humanas. Esta es una prohibición absoluta establecida en la regulación del BCRA. La l
