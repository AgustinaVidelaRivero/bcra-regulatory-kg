# Cifras de la cobertura de T, vuelta e: para la autora

Sacadas por `armar_cifras_e.py` de los dos JSON de `salidas_e/`, que escribieron `acuerdo_juez_cob_t.py` y `cifras_600_cob_t.py` de la vuelta c, sin cambios, sobre una copia de `lectura/`. Las reglas son las del documento de la cobertura en HEAD. Ninguna ref ni ningún texto.

## 1. El acuerdo del juez (primera nota, punto 9)

- **Acuerdan:** 93 de 100 (no acuerdan 7).
- **El juez manda a adjudicación:** 0; **deja sin consenso:** 0. Las dos cuentan como desacuerdo.
- **Kappa de Cohen** sobre las tres clases, en las que deciden los dos: 0,7469 (n = 100).
- **La distribución de las repeticiones:** unanimidad 96; 2 a 1 4.
- **Escala:** sí. La regla del punto 9: el juez escala si acuerda en al menos 84 de 100.

## 2. El orden (primera nota, punto 10)

- **Esenciales o útiles en las 100 primeras:** 100 (proporción 1,000).
- **En las 30 de control:** 30 (proporción 1,000).
- **Pasa:** no. La regla del punto 10: al menos 80 de las 100 esenciales o útiles, y más que en las 30 de control (5.5).
- La importancia, por clase: en las primeras, esencial 100; en el control, esencial 29, util 1.

## 3. El recall@10, @50 y @100 (primera nota, punto 11; el depurado, segunda nota, punto 4)

Presentes / k con Wilson al 95 %, en las 100 primeras por su posición; las parciales, aparte. El depurado saca del denominador solo las ausentes que la autora marca «no» según el pasaje; las «no decidible» quedan y se cuentan.

- **recall@10** (posiciones 1 a 10):
  - **crudo:** presentes 10 / 10 = 1,000 (Wilson al 95 %: 0,722 a 1,000); parciales, aparte, 0 / 10 = 0,000 (Wilson al 95 %: 0,000 a 0,278); ausentes 0;
  - **depurado:** presentes 10 / 10 = 1,000 (Wilson al 95 %: 0,722 a 1,000); parciales, aparte, 0 / 10 = 0,000 (Wilson al 95 %: 0,000 a 0,278); ausentes 0;
  - ausentes que salen por error del gold (la autora las marca «no» según el pasaje): 0; «no decidible», que quedan en el denominador: 0.
- **recall@50** (posiciones 1 a 50):
  - **crudo:** presentes 43 / 50 = 0,860 (Wilson al 95 %: 0,738 a 0,930); parciales, aparte, 5 / 50 = 0,100 (Wilson al 95 %: 0,043 a 0,214); ausentes 2;
  - **depurado:** presentes 43 / 50 = 0,860 (Wilson al 95 %: 0,738 a 0,930); parciales, aparte, 5 / 50 = 0,100 (Wilson al 95 %: 0,043 a 0,214); ausentes 2;
  - ausentes que salen por error del gold (la autora las marca «no» según el pasaje): 0; «no decidible», que quedan en el denominador: 0.
- **recall@100** (posiciones 1 a 100):
  - **crudo:** presentes 86 / 100 = 0,860 (Wilson al 95 %: 0,779 a 0,915); parciales, aparte, 11 / 100 = 0,110 (Wilson al 95 %: 0,063 a 0,186); ausentes 3;
  - **depurado:** presentes 86 / 100 = 0,860 (Wilson al 95 %: 0,779 a 0,915); parciales, aparte, 11 / 100 = 0,110 (Wilson al 95 %: 0,063 a 0,186); ausentes 3;
  - ausentes que salen por error del gold (la autora las marca «no» según el pasaje): 0; «no decidible», que quedan en el denominador: 0.

## 4. Si el orden no pasa: el recall sobre las esenciales, sin el orden

- **Sobre las 100 que la autora marcó esenciales:**
  - **crudo:** presentes 86 / 100 = 0,860 (Wilson al 95 %: 0,779 a 0,915); parciales, aparte, 11 / 100 = 0,110 (Wilson al 95 %: 0,063 a 0,186); ausentes 3;
  - **depurado:** presentes 86 / 100 = 0,860 (Wilson al 95 %: 0,779 a 0,915); parciales, aparte, 11 / 100 = 0,110 (Wilson al 95 %: 0,063 a 0,186); ausentes 3;
  - ausentes que salen por error del gold (la autora las marca «no» según el pasaje): 0; «no decidible», que quedan en el denominador: 0.

## 5. D-9 sobre las 30 (primera nota, punto 12), como lo da el script

- **Sorteadas:** 30; descartadas en la extracción: 0; filas de la hoja: 30.
- **No decidibles:** 0; decididas: 30; incorrectas (errores del gold): 0.
- **Cruda** (sobre las 30 decididas): presentes 22 / 30 = 0,733 (Wilson al 95 %: 0,556 a 0,858); parciales, aparte, 4 / 30 = 0,133 (Wilson al 95 %: 0,053 a 0,297); ausentes 4.
- **Depurada** (sobre las 30 correctas): presentes 22 / 30 = 0,733 (Wilson al 95 %: 0,556 a 0,858); parciales, aparte, 4 / 30 = 0,133 (Wilson al 95 %: 0,053 a 0,297); ausentes 4.
- La regla: presente = los tres expresados; parcial = sujeto y objeto expresados con el predicado parcial, o dos expresados y uno parcial; ausente = el resto (5.6; cob_v.presencia_regla). El intervalo: Wilson al 95 % (z = 1.959964).

## 6. Los sha256

- `salidas_e/acuerdo_juez_cob_t_e.json`: `ee5dcdf03795e7eed9a2e515023ac0a22d018ce6eedba3df71d908c57afe6976`
- `salidas_e/cifras_600_cob_t_e.json`: `d00c7702c1db736feddf75b4aaba0663cf1e22cfe3e6e01d7584846bc695695d`
- `armar_cifras_e.py`, el script que armó este archivo: `d2f14bf5bb0d0300d955dee5ca00e60061c1d9b8de546704d19795cf3daf8839`
- Lo que leyeron los dos scripts: la hoja de presencia `0e1cfe5ffd54cb1ebb81275c97aae5a316926b442063913e6f03e50ec2ed2837` (en el acuerdo, `0e1cfe5ffd54cb1ebb81275c97aae5a316926b442063913e6f03e50ec2ed2837`), la de importancia `7cbf988b86469bea3232ee82f57a6991d59a4422ca2ac47911ee66852be47f10`, el orden `5e852c1dd4302cd6005addd7b6e057c4f7d4990624cb65ecb6b526f6fb7743cd` y los veredictos del juez `27576f7b57c8ea61b3202dff360283a4a73dd6f1d346b633b268389458beebc3`.
