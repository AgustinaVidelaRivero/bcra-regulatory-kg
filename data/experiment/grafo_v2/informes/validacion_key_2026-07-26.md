# Informe — Validación de answer key (2026-07-26)

**Resultado: las 21 referencias entre corchetes se resolvieron contra `esquema_v2_clases.json` (ninguna quedó sin resolver, ninguna se inventó), todos los ids de `sujetos_esperados`/`sujetos_prohibidos` existen en el catálogo, y los 18 `chunk_id` coinciden con `muestra_piloto.json` en el mismo orden.** `answer_key.json` quedó escrito con los reemplazos; nada más se modificó (con las dos salvedades documentadas abajo, dentro del alcance del reemplazo). Sin API, sin commits. *(El informe `validacion_key_2026-07-25.md` documenta el freno previo por archivo inexistente; este lo supersede.)*

## Tabla de reemplazos completa

| Chunk | Campo | Antes | Después |
|---|---|---|---|
| capitales::9.1 | sujetos_prohibidos | `[rol CapMin para el nodo 9.2 — el texto nombra subconjunto específico]` | `Sujeto_rol_alcance_capmin` (+ aclaración movida a notas — ver salvedades) |
| capitales::12.1 | sujetos_esperados | `Sujeto_sefyc [instancia]` | `Sujeto_sefyc` |
| capitales::1.4 | sujetos_esperados | `Sujeto_sefyc [instancia]` | `Sujeto_sefyc` |
| capitales::1.4 | sujetos_esperados | `Sujeto_bcra [instancia]` | `Sujeto_bcra` |
| exterior::13.2 | sujetos_esperados | `[rol Exterior]` | `Sujeto_rol_entidad_autorizada_exterior` |
| regimen::5.1__p0 | sujetos_esperados | `[rol RegInf]` | `Sujeto_rol_entidad_comprendida_reginf` |
| proteccion::1.1 | sujetos_esperados | `[PNFC]` | `Sujeto_proveedor_no_financiero_de_credito` |
| proteccion::1.1 | sujetos_esperados | `[PSPCP]` | `Sujeto_pspcp` |
| proteccion::1.1 | sujetos_esperados | `[PSI]` | `Sujeto_psi_billetera_digital` |
| proteccion::2.5 | sujetos_esperados | `[PSPCP]` | `Sujeto_pspcp` |
| proteccion::2.5 | sujetos_esperados | `[PNFC]` | `Sujeto_proveedor_no_financiero_de_credito` |
| proteccion::2.5 | sujetos_esperados | `Sujeto_bcra [instancia]` | `Sujeto_bcra` |
| clasificacion::10.1 | sujetos_esperados | `[PNFC]` | `Sujeto_proveedor_no_financiero_de_credito` |
| clasificacion::10.1 | sujetos_prohibidos | `[rol Clasificación]` | `Sujeto_rol_obligado_a_clasificar_clasificacion` |
| exterior::1.1 | sujetos_esperados | `[rol Exterior]` | `Sujeto_rol_entidad_autorizada_exterior` |
| exterior::1.1 | sujetos_esperados | `Sujeto_bcra [instancia]` | `Sujeto_bcra` |
| regimen::10.1 | sujetos_esperados | `[rol RegInf]` | `Sujeto_rol_entidad_comprendida_reginf` |
| regimen::8.1 | sujetos_esperados | `[rol RegInf]` | `Sujeto_rol_entidad_comprendida_reginf` |
| regimen::8.1 | sujetos_esperados | `Sujeto_sefyc [instancia]` | `Sujeto_sefyc` |
| clasificacion::5.1 | sujetos_esperados | `[rol Clasificación]` | `Sujeto_rol_obligado_a_clasificar_clasificacion` |
| exterior::2.4 | sujetos_esperados | `[rol Exterior]` | `Sujeto_rol_entidad_autorizada_exterior` |

Mapa aplicado: `[PSPCP]`→`Sujeto_pspcp` · `[PSI]`→`Sujeto_psi_billetera_digital` · `[PNFC]`→`Sujeto_proveedor_no_financiero_de_credito` · `[rol Exterior]`→`Sujeto_rol_entidad_autorizada_exterior` · `[rol RegInf]`→`Sujeto_rol_entidad_comprendida_reginf` · `[rol CapMin]`→`Sujeto_rol_alcance_capmin` · `[rol Clasificación]`→`Sujeto_rol_obligado_a_clasificar_clasificacion` · `X [instancia]`→`X`.

## Dos salvedades (contenido tuyo preservado, no descartado)

1. **capitales::9.1 / sujetos_prohibidos:** la referencia traía una aclaración inline ("para el nodo 9.2 — el texto nombra subconjunto específico") que no puede vivir en un array de ids. Se reemplazó por el id exacto y la aclaración se movió al campo `notas` de esa misma entrada, marcada como movida. Si preferís descartarla, es un borrado de una frase en `notas`.
2. **regimen::8.1 / sujetos_prohibidos:** la entrada `[NOTA: para 8.1.4/8.1.5, ascender a EF o rol = pérdida del sujeto nombrado — puntuar como error de sujeto]` no es una referencia a sujeto sino una regla de puntuación. Se movió íntegra al campo `notas` de esa entrada (dejarla en el array rompería la validación de ids). Nada se perdió.

## Verificaciones (salida)

```
[OK] cero corchetes residuales en arrays de sujetos
[OK] todos los ids de sujetos_esperados/sujetos_prohibidos existen en esquema_v2_clases.json
[OK] los 18 chunk_id coinciden con muestra_piloto.json (mismo orden)
ids distintos usados en el key: 21
Referencias no resueltas: NINGUNA (no hubo que inventar nada)
```

## Git status (delta de esta unidad)

```
?? data/experiment/grafo_v2/piloto/answer_key.json   ← reemplazos aplicados
```

(Los `M` de `muestra_piloto.json` y `answer_key_TEMPLATE.json` son el swap de B1a-bis, previos a esta unidad y sin tocar acá.)

**FRENO acá.** Siguen: tu revisión de las dos salvedades, el commit de sellado del key, la confirmación de model ids, y B1b con OK explícito.
