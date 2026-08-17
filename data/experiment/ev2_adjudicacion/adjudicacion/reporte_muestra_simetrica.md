# Muestra simétrica §6 — juez vs adjudicación humana (CIEGO)

La muestra mide la tasa de error del juez en ambas direcciones; no reemplaza el veredicto del juez en esos pares (pre-registro §6).

- fichas en la muestra: 12; adjudicadas: 12; sin adjudicar: 0
- acuerdo exacto: 11 / 12
- matriz juez × humano: {'parcial': {'parcial': 7, 'correcto': 1}, 'correcto': {'correcto': 3}, 'incorrecto': {'incorrecto': 1}}
- dirección A (juez correcto, humana ≠ correcto): {'n_juez_correcto': 3, 'errores': 0, 'tasa': 0.0}
- dirección B (juez parcial/incorrecto, humana correcto): {'n_juez_parcial_incorrecto': 9, 'errores': 1, 'tasa': 0.1111111111111111}
- desacuerdo de grado (parcial ↔ incorrecto): 0
- acuerdo por criterio (marca humana vs modal del juez): {'n_criterios': 53, 'en_acuerdo': 52, 'tasa': 0.9811320754716981}

| id_ficha | id_opaco_base | estrato | juez | humano | coincide | criterios en acuerdo |
|---|---|---|---|---|---|---|
| ADJ-1156c72a | EV2R-de775a09d6 | muestra_parcial_incorrecto | parcial | parcial | True | 4/4 |
| ADJ-182df261 | EV2R-ed1d57375f | muestra_parcial_incorrecto | parcial | correcto | False | 4/5 |
| ADJ-202e66d6 | EV2R-df1f00c307 | muestra_correcto | correcto | correcto | True | 2/2 |
| ADJ-30527501 | EV2R-7d9c9100a7 | muestra_correcto | correcto | correcto | True | 4/4 |
| ADJ-3e268220 | EV2R-9de0ed0463 | muestra_parcial_incorrecto | parcial | parcial | True | 5/5 |
| ADJ-764fb304 | EV2R-757c889e2b | muestra_parcial_incorrecto | parcial | parcial | True | 5/5 |
| ADJ-9f188992 | EV2R-d7a1118272 | muestra_parcial_incorrecto | incorrecto | incorrecto | True | 5/5 |
| ADJ-b3d2893a | EV2R-03d3f8c3cc | muestra_parcial_incorrecto | parcial | parcial | True | 5/5 |
| ADJ-d7050380 | EV2R-b9757343f9 | muestra_parcial_incorrecto | parcial | parcial | True | 5/5 |
| ADJ-f2bc991c | EV2R-0d820c5f77 | muestra_correcto | correcto | correcto | True | 5/5 |
| ADJ-f773f42b | EV2R-3054a3d601 | muestra_parcial_incorrecto | parcial | parcial | True | 4/4 |
| ADJ-f96ca183 | EV2R-5c2587d1f8 | muestra_parcial_incorrecto | parcial | parcial | True | 4/4 |
