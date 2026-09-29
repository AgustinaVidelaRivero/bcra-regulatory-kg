# Tabla definitiva de las celdas C2 a C5 (anexo E5.c de U-TANDA0-2A)

Generado 2026-09-29T17:14:27. Marcas de la instancia adjudicadora (modelo), con calibración parcial de la autora, selladas en `8e0597c`; veredicto por ficha con el mapping §2 en código; pendientes del §7 re-agregados con agregar_par; doble cómputo byte-idéntico. Comando: `cierre_adj_tanda0.py --commit-marcas 8e0597c`.

## 1. C2, C3 y C4 al lado de C1

| celda | grafo, backend | n | correcto | parcial | incorrecto | Wilson 95 % correcto | Wilson 95 % incorrecto |
|---|---|---|---|---|---|---|---|
| C1 (`774acac`, citada) | r1, memoria | 40 | 6 | 26 | 8 | 0.0706–0.2907 | 0.105–0.3476 |
| C2 | r1, Neo4j | 40 | 9 | 24 | 7 | 0.1232–0.375 | 0.0875–0.3195 |
| C3 | desarrollo tanda 0, memoria | 40 | 10 | 23 | 7 | 0.1419–0.4019 | 0.0875–0.3195 |
| C4 | desarrollo tanda 0, Neo4j | 40 | 11 | 21 | 8 | 0.1611–0.4283 | 0.105–0.3476 |

Vías de los definitivos (juez_base / juez_enc / adjudicacion_base / adjudicacion_s7):
- C2: 11 / 21 / 5 / 3
- C3: 13 / 20 / 7 / 0
- C4: 14 / 20 / 5 / 1
- C5: 8 / 8 / 4 / 0

## 2. C5 aparte (no se cruza con C1 a C4)

| celda | grafo, backend | n | correcto | parcial | incorrecto | Wilson 95 % correcto | Wilson 95 % incorrecto |
|---|---|---|---|---|---|---|---|
| C5 | diez, memoria (20 preguntas nuevas) | 20 | 8 | 8 | 4 | 0.2188–0.6134 | 0.0807–0.416 |

## 3. Acuerdo entre el juez y la instancia adjudicadora en la muestra de control

Salvedad: no es una validación del juez contra lectura humana. Mide el acuerdo entre el juez y la instancia adjudicadora en la población B, y no reemplaza veredictos.

| alcance | fichas | acuerdo exacto | criterios en acuerdo | sobre-acreditación | sub-acreditación | caída de correctos |
|---|---|---|---|---|---|---|
| C2 | 4 | 4/4 | 18/18 | 0 | 0 | 0/1 |
| C3 | 4 | 4/4 | 18/18 | 0 | 0 | 0/1 |
| C4 | 4 | 4/4 | 18/18 | 0 | 0 | 0/1 |
| C2 a C4 agregada | 12 | 12/12 | 54/54 | 0 | 0 | 0/3 |
| C5 (aparte) | 2 | 1/2 | 5/6 | 0 | 1 | 0/1 |

Salvedades: muestras de 2 a 4 fichas por celda; en C5, las dos preguntas con criterios sin cita quedan fuera del marco de la muestra (anexo, decisión 2); episodios en `data/experiment/ev2_tanda0/adjudicacion/nota_episodios_adjudicacion_tanda0.md`.
