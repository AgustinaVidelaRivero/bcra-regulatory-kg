# U-SEG-OFICIAL — FRENO S0-5a-bis (09/10/2026)

Mandato `docs/mandatos/USEG_OFICIAL_S0-5a_reglas_de_corte_E0.md` leído en `84695b89` (`cbe0cb35…`), con las dos notas;
lista de R5-a v2 de la mesa (`5bec1dce…`, el de su manifest); y el agregado de ri_oc del 09/10/2026, con la lista de
los 88 (`cf6796e7…`). USD 0, sin API. **Nada commiteado; el parche no se aplicó al repo.** Detalle: `REPORTE_S0-5a-bis.md`;
diseño: `DISENO_S0-5a-bis.md`; censos: `censos/`.

**Antes**: HEAD `0c271468`; E0 del repo = S0-4b (`65a8c3b8…`, `94d35349…`, `ec186071…`); mi parche de S0-5a,
`c6558ea0…`; foto sha256 del repo (48.312 archivos, 15:22:15) y 2.213 `.pyc`. Después de empezar entró la tercera nota
(`be88fdf9`, 15:50; mandato `66f3549c…`): sus dos límites de `ri2_ae::14.3` están en la lista de límites. La cuarta,
sin commitear en el archivo, coincide con el agregado; no la usé como fuente.

**Dos vueltas.** La primera (R5-a por lista, la guarda de tablas y R5-f) pasó sus controles; el agregado de ri_oc llegó
al cerrarla, así que sumé R5-g y volví a correr todo con el código final. Las cifras son de la segunda.

**Parche** `parche/parche_e0_S0-5a-bis.diff` (`421ee913…`, +1.167 −23), sobre el código de S0-4b; reemplaza al de
S0-5a. Prueba en seco: rc 0, y los tres archivos finales byte a byte (`bd2190ad…`, `68bd74b5…`, `789630b5…`).

**Controles** (REPORTE §2):
- todas apagadas = S0-4b, 768 de 768;
- los 152 dos veces (prototipo con todas y código final): 768 de 768 iguales; **9.665 unidades**; manifiesto
  `176cbdc0…`;
- tanda 0: **57 de 57**, dos veces; sin la exclusión, ninguna regla la cambia; los 25 de la tanda 0 en los 152, 25 de 25;
- `selftest_e0` **188/188**; b52 39/39, b581 34/34, b582 59/59, b583 33/33;
- claves de la caché: OK, igual a `923dd900…`;
- control de continuidad: 14/14.

**Aceptación** (REPORTE §3):
1. **R5-a por lista**:
   - las 40 enteras, con el texto de S0-5a, 40 de 40;
   - `ri_rml::1.4.2`: el cierre de 1.4 va de «Para el punto 1.4.1.» a «…671000/M-TP.»;
   - los dos mixtos: el cierre, renglón por renglón, igual a la v2, y el resto del ítem igual a S0-4b;
   - las 14 que no se tocan, iguales a S0-4b, 14 de 14;
   - ningún movimiento fuera de las 43.
2. **Tablas**: las 468 siguen serializadas, con el mismo texto y en la misma unidad; la guarda no tuvo que bloquear nada.
3. **R5-a′ a R5-e**, como en S0-5a: 9 de 9 casos, 27 de 27 correctos, 9 de 9 títulos, 4 de 4 chapeaux; R5-a′, R5-b, R5-d
   y R5-e OK.
4. **R5-f**: abren los 11 rótulos de ri_ccna y `snp_cheq::3.3.6.2`, colgado de 3.3.
5. **R5-g**:
   - «3. Aclaraciones» sale de `ri_oc::S2` y las 51 unidades de 3.1 a 3.51 lo heredan;
   - con R5-g sola cambian exactamente esas 52 claves (S3 no es clave propia) y ningún otro TO;
   - los otros 87 rechazos siguen, 87 de 87.

**Censo por regla** (REPORTE §4; `censos/censo_por_regla_S0-5a-bis.md`):

| regla | TOs | creadas | quitadas | cambiadas |
|---|---|---|---|---|
| R5-a por lista | 29 | 43 | 0 | 157 |
| R5-a′ | 1 | 1 | 1 | 11 |
| R5-b | 2 | 0 | 21 | 20 |
| R5-c | 4 | 0 | 9 | 105 |
| R5-d | 2 | 17 | 1 | 11 |
| R5-e | 1 | 0 | 0 | 2 |
| R5-f | 2 | 12 | 1 | 13 |
| R5-g | 1 | 0 | 0 | 52 |
| todas | 34 | 73 | 33 | 366 |

- **Sin atribución exacta**: 14 de 472 eventos, porque dos reglas tocan la misma unidad: R5-f con R5-c en ri_ccna, y
  R5-a con R5-c en `ri_spi::C.1`.
- **Claves**: la lista de las 472, con su regla, en `censos/claves_S0-5a-bis.json`. El selftest da VEREDICTO OK, y el
  control negativo da FALLA en las dos direcciones.
- **Contra S0-5a**: 150 unidades distintas, todas explicadas: 57 revertidas a S0-4b, 76 nuevas (R5-f 24, R5-g 52) y 17
  que cambian en las dos.

**Continuidad** (REPORTE §6): 104 saltos en S0-4b, 88 ahora.
- Se cierran los 11 de ri_ccna (y los 6 de R5-d).
- 3.3.6 de snp_cheq queda (i), sin descendientes tragados.
- **Un salto nuevo, snp_cheq 3.3.6.1 (i)**: es el salto del PDF que la nota declara, visible ahora que 3.3.6.2 existe.
  Contradice la letra de «ningún salto nuevo»; lo declaro.

**Límites, caso por caso** (`censos/limites_S0-5a-bis.md`, 209 filas):
- los 3 de los mixtos, tal cual de la v2, y los 2 de la tercera nota («15.» y «16.» de `ri2_ae::14.3`, p. 29,
  `raiz_en_columna_profunda_111.9_vs_83.7`): grupo 2;
- `seggar::5.3.5` (grupo 2, PENDIENTE de la autora) y `ri_cc::R5::2.2.1.2` (sin adjudicar);
- 22 candidatos de R5-a′: la nota dice 23, pero cuenta `ri_rml::1.2.3`, que ella misma descarta;
- 88 saltos de numeración (72 para la autora y 16 (i) de información);
- 5 límites del §3;
- los 87 rechazos que R5-g no toca.

**Repo** (foto a las 20:45:03; REPORTE §10): de esta sesión, solo los 43 archivos nuevos de `s0_5/bis/`. Lo demás que
cambió lo hicieron otras sesiones y lo explican sus commits posteriores a `0c271468` o su árbol de trabajo: 222 nuevos
en `conf_matriz/` y `omisiones_cod/`, y 7 documentos de `docs/`. `.pyc`: 2.213, la misma lista. Grep de convenciones: 0
en documentos, scripts y parche; 25 en censos, todas de texto del corpus.

**Paquete** `revision_USEG_OFICIAL_FRENO_S0-5a-bis/` (85 archivos y `manifest.txt`; 162 MB): FRENO, informe y diseño;
el parche, el interruptor y el LEEME; los tres archivos finales de E0; los scripts de `s0_5/bis/` y los de `s0_5/` que
corre; los censos; las dos listas de la mesa; las fotos del repo, la atribución de los cambios ajenos y los logs; y
cuatro tar.gz de salidas de E0 (la final, las ocho reglas solas, la tanda 0, y la final de la vuelta 1). Copia
permanente con `ditto` en
`~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/0c0c6584-4c87-4d3c-b3b4-425c9ab87db2/scratchpad/revision_USEG_OFICIAL_FRENO_S0-5a-bis/`:
**85 de 85 iguales a su `manifest.txt`** (sha256 y bytes), ninguno sin listar.

**Mensaje de commit PREPARADO** (no corrido; probado en un repo descartable: `git log --oneline` muestra solo el
título; sin ids de TOs ni de unidades, sin nombres de mecanismos). Agrega solo `s0_5/bis/`:

```
git add data/experiment/segmentacion_oficial_e0r2/s0_5/bis
git commit -m "U-SEG-OFICIAL S0-5a-bis: correcciones de las reglas de corte de E0 en una copia (USD 0, sin API)" -m "Registro de S0-5a-bis: el diseño, el informe y el FRENO; el parche de E0 sobre el código vigente, para S0-5b, sin aplicar, con el interruptor de medición, que no va al repo; los scripts de la aceptación, de la diferencia contra la etapa anterior y de los límites; y los censos, los controles y la lista de límites caso por caso. La salida de E0 no entra al repo: queda en el paquete de revisión, con su manifiesto."
```
