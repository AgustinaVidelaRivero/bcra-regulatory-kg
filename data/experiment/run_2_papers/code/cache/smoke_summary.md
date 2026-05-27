# Smoke test summary — TO_proteccion_usuarios_servicios_financieros_actual

- Chunks: 36
- Chunks productivos (con ≥1 entity tras validación): 34 (94.4%)
- Tiempo: 272.5 s
- Costo extracción base: USD 0.5425
- Costo retry: USD 0.4463 (45.1% del total)
- Costo total smoke: USD 0.9888
- % chunks con ≥1 violación 1ª pasada: 66.7%
- % chunks que dispararon retry: 66.7%
- % chunks con violaciones POST-retry (conservados con flag): 16.7%
- Violaciones por código (1ª pasada): {'V7': 7, 'V3': 46, 'V5': 15, 'V4': 27, 'V1': 1, 'V6': 2, 'V2': 1}
- Nodos: 463  |  Edges: 498  |  Densidad: 1.076
- Nodos por tipo: {'ConceptoDefinido': 55, 'SujetoRegulado': 28, 'OrganismoRegulador': 5, 'Obligacion': 176, 'NormaReferenciada': 61, 'InstrumentoFinanciero': 35, 'Umbral': 2, 'Requisito': 61, 'Operacion': 15, 'Plazo': 14, 'Procedimiento': 10, 'Sancion': 1}
- Edges por predicado: {'obligado_a': 218, 'supervisado_por': 10, 'aplica_a': 101, 'usa_concepto': 22, 'es_subtipo_de': 4, 'referencia': 17, 'involucra_instrumento': 24, 'requiere': 51, 'tiene_umbral': 2, 'condicion_de_aplicabilidad': 14, 'definido_por': 2, 'tiene_plazo': 19, 'excepcion_a': 4, 'ejecutado_por': 3, 'dirigido_a': 2, 'clasifica_a': 1, 'impuesta_por': 1, 'recae_sobre': 1, 'modifica': 2}
- Predicados sin uso: ['puede_realizar', 'requiere_autorizacion_de', 'parte_de_procedimiento', 'genera_sancion']