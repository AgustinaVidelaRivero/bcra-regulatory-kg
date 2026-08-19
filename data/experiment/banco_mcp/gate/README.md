# U-A2.0-gate — Gate de trazabilidad del banco Claude Code + MCP

Pregunta de la unidad: **¿sobrevive la atribución causal de fallas (A0.2) al harness de
Claude Code?** Si no sobrevive, el head-to-head de A2 cambia de forma y hay que saberlo antes
de construir servidores MCP, índices y aislamiento.

**Veredicto: PASA CON CONDICIONES** → `veredicto_gate.md` (léelo primero).
Confirmado con corridas reales en la **FASE B** → `faseB_resultados.md`.

Costo: **USD 0** la fase A (todo re-ejecución determinística sobre un mini-grafo sintético
propio) y **USD 1,2983** la fase B (9 sesiones reales de `claude -p`, tope autorizado USD 2).

## Mapa

| archivo | qué es |
|---|---|
| `veredicto_gate.md` | **entregable 6**: el veredicto y los requisitos R1..R7 para A2.0-banco |
| `inventario_campos.md` | entregable 1: qué campo alimenta cada decisión de clase y de dónde sale |
| `estimacion_faseB.md` | entregable 7: fórmula de costo de la Fase B, sin precios |
| `faseB_predeclaracion.md` | lo que se fijó **antes** de correr la fase B: modelo, tope de tool calls, precios verificados, reglas de freno |
| `faseB_resultados.md` | resultados de la fase B: demostración por clase sobre sesiones reales, bordes obtenidos y no obtenidos, `P0` medido, gasto real |
| `casos_gate_faseB.json` | declaración de los 9 casos corridos en fase B (y por qué 2 no se corrieron) |
| `code/faseB_runner.py` | runner de las corridas reales, con el freno acumulado implementado |
| `code/contabilidad_faseB.py` | gasto por dos lecturas: la del CLI y la recomputada a precios oficiales |
| `sesiones_faseB/`, `corrida_faseB/` | rebanada cruda, trazas adaptadas y demostración de la fase B |
| `propuesta_plan.md` | propuesta de actualización del checkbox A2.0-gate en `docs/plan_tesis.md` |
| `casos_gate.json` | declaración de los 11 casos capturados (clase esperada + diseño) |
| `grafo_juguete.json` | mini-grafo sintético de 9 nodos (generado por `code/grafo_juguete.py`) |
| `code/grafo_juguete.py` | generador determinístico del mini-grafo |
| `code/tools_juguete.py` | **entregable 2**: tools de juguete, contratos v1 y v2 |
| `code/adaptador_cc.py` | **entregable 4**: sesión de Claude Code → traza del formato del repo |
| `code/demostracion_gate.py` | **entregable 5**: atribución por clase con el código de A0.2 importado |
| `code/medicion_transporte.py` | límites medidos del transporte (cap de stdout, derrames) |
| `sesiones/` | **entregable 3**: rebanada cruda verbatim + manifiesto + outputs derramados |
| `corrida/` | trazas adaptadas, demostración y mediciones |

## Reproducir de punta a punta (sin API, sin red)

```
python3 -B code/grafo_juguete.py --escribir grafo_juguete.json
python3 -B code/adaptador_cc.py adaptar --rebanada sesiones/rebanada_cruda.jsonl
python3 -B code/demostracion_gate.py
```

Lo mismo para la fase B (tampoco vuelve a llamar a la API):

```
python3 -B code/adaptador_cc.py adaptar --rebanada sesiones_faseB/rebanada_cruda.jsonl \
  --out corrida_faseB/trazas --casos casos_gate_faseB.json
python3 -B code/demostracion_gate.py --out corrida_faseB --casos casos_gate_faseB.json \
  --trazas corrida_faseB/trazas --rebanada sesiones_faseB/rebanada_cruda.jsonl \
  --nombre demostracion_faseB
```

El paso de captura (`code/adaptador_cc.py extraer --sesion <jsonl>`) **no** es reproducible:
el jsonl de sesión vive fuera del repo y sigue creciendo mientras la sesión corre. Lo
reproducible es la rebanada, cuyo sha256 está en `sesiones/manifiesto_captura.json`.

## Qué NO es esta unidad

No construye el banco (A2.0-banco), no expone MCP, no elige modelo de embeddings (A2.0b), no
diseña ni corre evaluación (A2.1/A2.2). El material EV2 no se abre: sus trazas se usaron solo
como **formato** de referencia. El contenido del mini-grafo es inventado.
