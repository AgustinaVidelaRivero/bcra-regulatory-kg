# Entregable 7 — Estimación de la FASE B (llamadas y tokens, fórmula sin precios)

FASE B = correr los mismos casos del entregable 3 **de verdad** con `claude -p` y `--model`
fijo, y repetir los entregables 4 y 5 sobre esas sesiones reales. Nada de esto se ejecuta sin
autorización explícita con precios y tope.

## 1. Unidad de conteo

Una **sesión** por caso. Dentro de una sesión, cada tool call es un turno de asistente más un
turno de resultado; el contexto se reenvía completo en cada turno, así que el costo crece con
el **cuadrado** del número de tool calls, no linealmente.

Notación por sesión `s`:

- `P0` — tokens del prompt de sistema de Claude Code + definiciones de tools. **No está bajo
  control de la autora** (limitación ya declarada en A2.0-banco) y **no se puede estimar desde
  el repo**: hay que medirlo.
- `Q_s` — tokens del prompt de la pregunta del caso.
- `K_s` — tool calls de la sesión; `T_s = K_s + 1` turnos de asistente (el último es la respuesta).
- `a_i` — tokens de salida del turno `i`.
- `r_i` — tokens del resultado de la tool `i`.

## 2. Fórmula

Sin caching:

```
tokens_in(s)  = Σ_{t=1..T_s} [ P0 + Q_s + Σ_{i<t} (a_i + r_i) ]
              = T_s·(P0 + Q_s) + Σ_{i=1..T_s-1} (T_s − i)·(a_i + r_i)
tokens_out(s) = Σ_{t=1..T_s} a_t
```

Con prompt caching sobre el prefijo estable (el patrón del repo, `llm_cache` / breakpoints):

```
cache_write(s) ≈ P0 + Q_s                       (una vez por sesión)
cache_read(s)  ≈ Σ_{t=2..T_s} [ P0 + Q_s + Σ_{i<t-1}(a_i + r_i) ]
in_fresco(s)   ≈ Σ_{t=2..T_s} (a_{t-1} + r_{t-1})
```

Costo total, con `R` repeticiones (mínimo `R = 2`: la doble corrida es lo que prueba que el
transporte es reproducible, no solo la atribución):

```
costo = R · Σ_s [ precio_in·in_fresco(s) + precio_cache_write·cache_write(s)
                + precio_cache_read·cache_read(s) + precio_out·tokens_out(s) ]
```

Los precios se completan en el momento de la autorización; acá no se fija ninguno.

## 3. Entradas MEDIDAS (de la captura de la Fase A)

Comando que las reproduce:

```
python3 -c "import json,glob;\
fs=[json.load(open(p)) for p in sorted(glob.glob('data/experiment/banco_mcp/gate/corrida/trazas/GATE-*.json'))];\
print(sum(len(d['trace']['steps']) for d in fs), sum(s['output_chars'] or 0 for d in fs for s in d['trace']['steps']))"
```

| magnitud | valor medido |
|---|---|
| sesiones | 11 |
| tool calls totales `Σ K_s` | 20 |
| turnos de asistente `Σ T_s` | 31 |
| chars de resultado de tool, total | 53.091 |
| ídem, excluyendo GATE-10 (nodo grande) | 10.843 |
| chars por step (media, sin GATE-10) | 570 |

Conversión declarada: `tokens ≈ chars / 3,5` para este JSON en castellano (regla de dedo, no
medición). Con eso: `Σ r_i ≈ 15.170` tokens con GATE-10, `≈ 3.100` sin él.

## 4. Lo que la Fase B tiene que medir ANTES de correr todo

`P0` domina el costo (aparece `T_s` veces por sesión) y es desconocido. **Primer paso
obligatorio de la Fase B**: una sola sesión descartable con

```
claude -p "<prompt del caso>" --model <id fijo> --output-format json
```

y leer el bloque `usage` (`input_tokens`, `cache_creation_input_tokens`,
`cache_read_input_tokens`, `output_tokens`). Ese número reemplaza a `P0` en la fórmula y
recién ahí la estimación es un número y no una familia de curvas.

## 5. Orden de magnitud con `P0` parametrizado

Con `Q_s ≈ 300`, `a_i ≈ 300`, `Σ r_i ≈ 15.200`, `Σ T_s = 31`, `R = 2`:

| `P0` | `Σ cache_read` aprox | `Σ in_fresco` aprox | `Σ out` aprox |
|---|---|---|---|
| 3.000 | 2·20·3.300 ≈ 132.000 | 2·24.500 ≈ 49.000 | 2·9.300 ≈ 18.600 |
| 8.000 | 2·20·8.300 ≈ 332.000 | ídem | ídem |
| 15.000 | 2·20·15.300 ≈ 612.000 | ídem | ídem |

Lectura: el gasto está dominado por lecturas de caché de un prefijo que no controlamos. El
tope de USD 2 propuesto en el mandato es **coherente** con estas magnitudes para cualquier `P0`
de la tabla, pero eso solo se puede afirmar con precios a la vista; la unidad no los fija.

## 6. Riesgos de costo declarados

1. **GATE-10 (nodo grande)** aporta el 80 % de los chars de tool. En la Fase B conviene
   correrlo **una sola vez** (no `R = 2`) o reducir el relleno: su valor probatorio ya está
   obtenido offline (el derrame a disco recupera el output íntegro).
2. **Reintentos del agente**: si el modelo real navega más que la puesta en escena, `K_s` sube
   y el costo sube con `K_s²`. Mitigación: tope de tool calls por sesión declarado antes de
   correr, y corte duro.
3. **GATE-07 (sin tool calls)** no se puede forzar sin arriesgar que el modelo llame igual: se
   declara como caso *best effort*; si el modelo llama a una tool, el caso se reporta como no
   obtenido, no se edita la sesión.
