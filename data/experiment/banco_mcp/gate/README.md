# U-A2.0-gate — Gate de trazabilidad del banco Claude Code + MCP

Pregunta de la unidad: **¿sobrevive la atribución causal de fallas (A0.2) al harness de
Claude Code?** Si no sobrevive, el head-to-head de A2 cambia de forma y hay que saberlo antes
de construir servidores MCP, índices y aislamiento.

**Veredicto: PASA CON CONDICIONES** → `veredicto_gate.md` (léelo primero).

Costo de esta fase: **USD 0**. Ninguna llamada a API. Todo es re-ejecución determinística
sobre un mini-grafo sintético propio.

## Mapa

| archivo | qué es |
|---|---|
| `veredicto_gate.md` | **entregable 6**: el veredicto y los requisitos R1..R7 para A2.0-banco |
| `inventario_campos.md` | entregable 1: qué campo alimenta cada decisión de clase y de dónde sale |
| `estimacion_faseB.md` | entregable 7: fórmula de costo de la Fase B, sin precios |
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

El paso de captura (`code/adaptador_cc.py extraer --sesion <jsonl>`) **no** es reproducible:
el jsonl de sesión vive fuera del repo y sigue creciendo mientras la sesión corre. Lo
reproducible es la rebanada, cuyo sha256 está en `sesiones/manifiesto_captura.json`.

## Qué NO es esta unidad

No construye el banco (A2.0-banco), no expone MCP, no elige modelo de embeddings (A2.0b), no
diseña ni corre evaluación (A2.1/A2.2). El material EV2 no se abre: sus trazas se usaron solo
como **formato** de referencia. El contenido del mini-grafo es inventado.
