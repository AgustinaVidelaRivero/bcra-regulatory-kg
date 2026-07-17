# B4.5 — Guardas determinísticas de salida de S1 (s1-v0.3.1-dev)

Fecha: 2026-07-17. **Validación, NO iteración de juicio.** Declaración de alcance: los
cambios de esta tarea son EXACTAMENTE tres bloques en s1_fuentes.py — (1) las constantes
`S1_VERSION`/`S1_MAX_TOKENS`/`CAUSAS_VALIDAS`, (2) el bloque de validación de dominio al
final de `_llamada_s1`, (3) el filtro de `decididas` en `_voto_s1_atrib` — más los tests.
**S1_PROMPT, S1_PROMPT_EXONERACION, CAMPOS_S1/CAMPOS_S1_EXON y las funciones de ensamblado
(_prompt_s1 / _prompt_s1_exoneracion / _sintoma_para_prompt / _pasajes_para_prompt) quedan
byte-intactos de la ronda 2**; el fetch, intacto desde B4.2. Sin commits.

## 1. Validación de dominio

- **`CAUSAS_VALIDAS`** (constante, vocabulario CERRADO de causas de capa 2, copiado
  verbatim de `taxonomia.md` — defectos del grafo: líneas 44-48; defectos del agente:
  líneas 55-58; sin defecto y abstención: líneas 62-65): contenido_kg, completitud_kg,
  estructural_kg, provenance_imprecisa, alcanzabilidad_kg, navegación (ambas grafías, el
  criterio de robustez de capa_deterministica), alucinacion_agente, aplicacion_erronea,
  sin_defecto, frontera_no_determinada.
- `sintoma_del_par` contra los 3 síntomas (antes era error `sintoma_invalido`; ahora el
  tratamiento unificado de dominio).
- **Valor fuera de dominio → la muestra se anota `fuera_de_dominio` (campo + valor
  VERBATIM preservado, la salida no se reescribe) y NO vota** (tratamiento
  no_determinable).

## 2. Tope de salida

| Tope viejo | Máximo observado (v0.2 + N=3, usage real) | **Tope nuevo (2×)** |
|---|---|---|
| 2.048 | 1.184 | **2.368** |

Guarda preventiva: un JSON cortado sigue siendo formato_invalido.

## 3. pytest (verde completo: 91 = 87 previos − 1 reescrito + 5 de B4.5)

```
91 passed
```

## 4. RE-APLICACIÓN sin API — replay v0.3.1 sobre las salidas congeladas de `_s1_n3.json`

Salidas nuevas `_s1_n3_v031.json` (todas las previas congeladas). Cero llamadas API.

```
run_2/CQ-021: replay 0 salidas · voto_s1 = 2×{context_recall, completitud_kg} (3) · IGUAL
run_4/CQ-008: replay 6 salidas · voto_s1 = {context_recall, completitud_kg} (3) · IGUAL
run_4/CQ-021: replay 9 salidas · voto_s1 = {context_recall, completitud_kg} (3) · IGUAL
run_4/CQ-028: replay 9 salidas · voto_s1 = {noise_sensitivity, contenido_kg} (2) · IGUAL
```

- **La muestra con causa fuera de dominio se re-clasificó como pedido:** CQ-028
  rep2_atrib1 muestra 1 ahora lleva
  `fuera_de_dominio: [{campo: causa_confirmada_o_corregida, valor_verbatim:
  "context_recall"}]` — verbatim preservado, no vota.
- **Ningún voto final cambia** (esa muestra ya era no-decidida por su
  `coinciden=no_determinable`; la guarda formaliza el tratamiento).
- Nota de fidelidad del replay (documentada): la muestra ERROR de CQ-028 rep1 se
  re-alimentó desde su `texto_crudo` persistido (recortado a 2.000 chars al guardarse);
  el parser extrajo esta vez un sub-objeto parcial y la muestra salió
  `campos_faltantes:justificacion_breve` en vez de `json_no_parseable` — MISMO
  tratamiento (no decidida, no vota), etiqueta distinta. Limitación del replay (el crudo
  completo no se persiste), no del módulo.

---

*Fin de B4.5. Guardas de dominio y tope activas; votos del dev invariantes; vocabulario
citado de la taxonomía; cero API. Frenado para revisión.*
