# U-SEG-OFICIAL — FRENO S2-a (15/10/2026)

Tramo 1 de S2: la E0 corregida, la lista de la tanda 1 y U. Despacho de S2, versión 2 (15/10/2026), con D-1 y D-2. USD 0, sin
API. **Nada commiteado, ningún mensaje de commit preparado; no escribí en la memoria.** Escribí solo en `s2/` y en el scratchpad.
Detalle, fuentes y comandos: `REPORTE_S2.md`, tramo 1.

## Paso 0 (con `$HOME` en lugar de la carpeta personal)

```
$ pwd
$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg
$ git log --format=%s -5
Evaluacion final: el numero de preguntas por potencia, el reparto si cae la tanda final y el sucesor en la tanda 1 con su tope
Segmentacion oficial: las definiciones para las cifras de la etapa siguiente, decididas, y una regla de control sellada
Calendario hacia la evaluacion final: la enmienda del protocolo firmada y las decisiones de calidad y de evaluacion
Calendario hacia la evaluacion final: la regla de caida sellada y la enmienda del protocolo, para firmar
Segmentacion oficial: la adjudicacion de la lectura de la E0 corregida, terminada, con su cifra debajo del piso
$ git status --porcelain -- data/experiment/reextraccion_v2/e0_chunking data/experiment/segmentacion_oficial_e0r2
?? data/experiment/segmentacion_oficial_e0r2/s1/e0/
?? data/experiment/segmentacion_oficial_e0r2/s1bis/e0/
?? data/experiment/segmentacion_oficial_e0r2/s1ter/e0/
$ shasum -a 256 data/experiment/reextraccion_v2/e0_chunking/e0_lib.py data/experiment/reextraccion_v2/e0_chunking/correr_e0.py data/experiment/reextraccion_v2/e0_chunking/e0_tablas.py
d89aab1a578252cd6296f03e8e8859644f008740cd493ef6d82e86c5009db298  data/experiment/reextraccion_v2/e0_chunking/e0_lib.py
78c54c4cd7dc47d592a2f9dcadc1bf97535af2d6ea0f67d67c8021010650cb5e  data/experiment/reextraccion_v2/e0_chunking/correr_e0.py
ab300a22b41f99e84ae65e8d8cd2bb5799636dffd58cfc1fda6bb3e0433bf53f  data/experiment/reextraccion_v2/e0_chunking/e0_tablas.py
$ ls data/experiment/segmentacion_oficial_e0r2
FRENO_S0-1.md
FRENO_S0-1bis.md
FRENO_S0-2.md
FRENO_S0-3.md
FRENO_S1.md
s0_1
s0_1bis
s0_2
s0_3
s0_4
s0_5
s0_6
s1
s1bis
s1quater
s1ter
```

Todo da lo esperado: el 67 entre los títulos (el último commit es posterior, `4e4f3636`), solo los tres `e0/` sin rastrear, los
sha256 del código de `2374968a` y ninguna carpeta `s2`.

## La E0 corregida (REPORTE, §1.2)

- Copia con el `rsync` de la cláusula, más `--exclude='NO_ABRIR_*'` por la cláusula de carpetas vedadas: 0 `.env`, 0 `NO_ABRIR_`
  y 0 enlaces en la copia.
- Raíz mínima con `s0_4/scripts/raiz_minima.sh`, con el código de la copia (los mismos sha256 del paso 0).
- `s0_1/scripts/correr_152.py --codigo <raíz> --salida <dir> --workers 8`: de 14:47:34 a 14:53:08, rc 0, 152 TOs, 0 con error.
- **Control** (`controles/control_e0_S2a.json`): los 768 archivos `e0/…` del manifiesto de S0-6b (`80adbd58…`) están y dan su
  sha256 y sus bytes, sin archivos de más; **152 TOs y 10.478 unidades**. OK.
- La E0 queda en el scratchpad para el tramo 2 y no va al paquete: tiene el texto de todas las unidades, es la del manifiesto de
  S0-6b y el lote la regenera en unos 6 minutos; un tar.gz `NO_ABRIR_` no se podría copiar con `ditto` (cláusula de carpetas
  vedadas). REPORTE, §1.2.

## La lista de la tanda 1 (`lista_tanda1_S2.json`; REPORTE, §1.4)

Sale ri_oc (enmienda 8, decisión 1; 197 unidades, `sin_raiz`). Sucesor por D-1: **ri_mmsef**. ri_pgn queda por D-2; **el orden del
§7 no lo recomputé.** Clase: NG normativa general, RI régimen informativo (`inventario_tos.csv`).

| estrato | TO | clase | modo (E0 corregida) | unidades | cobertura exacta | ids repetidos | fila en el registro de alcance |
|--:|---|---|---|--:|---|--:|---|
| 1 | ayccef | NG | `vigente` | 196 | sí | 0 | no (rol en el manifiesto de los 152) |
| 1 | expaef | NG | `vigente` | 165 | sí | 0 | no (rol en el manifiesto de los 152) |
| 1 | opefci | NG | `vigente` | 74 | sí | 0 | no (rol en el manifiesto de los 152) |
| 1 | adrei | NG | `vigente` | 70 | sí | 0 | no (rol en el manifiesto de los 152) |
| 2 | ri_ccna | RI | `sin_raiz` | 169 | sí | 0 | tanda 1, `:20` |
| 2 | ri_rml | RI | `vigente` | 46 | sí | 0 | tanda 1, `:21` |
| 2 | ri_gerc | RI | `vigente` | 15 | sí | 0 | tanda 1, `:22` |
| 2 | ri_pgn | RI | `vigente` | 21 | sí | 0 | tanda 1, `:23` |
| 3 | snp_cheq | NG | `vigente` | 265 | sí | 0 | tanda 1, `:26` |
| 3 | ceninf | NG | `sin_raiz` | 39 | sí | 0 | tanda 1, `:27` |
| 3 | cirmo3 | NG | `vigente` | 256 | sí | 0 | tanda 1, `:28` |
| 3 | snp_tr | NG | `vigente` | 103 | sí | 0 | tanda 1, `:29` |
| 4 | lingeef | NG | `vigente` | 613 | sí | 0 | no (rol en el manifiesto de los 152) |
| 4 | depaho | NG | `vigente` | 442 | sí | 0 | no (rol en el manifiesto de los 152) |
| 4 | cajasc | NG | `vigente` | 287 | sí | 0 | no (rol en el manifiesto de los 152) |
| 5 | manori | NG | `vigente` | 152 | sí | 0 | tanda 1, `:30` |
| 5 | efemin | NG | `vigente` | 119 | sí | 0 | no (rol en el manifiesto de los 152) |
| 5 | nmcief | NG | `sin_raiz` | 55 | sí | 0 | tanda 1, `:31` |
| 6 | ri_dcpc | RI | `marcadores` | 75 | sí | 0 | tanda 1, `:25` |
| 6 | ri_mmsef (sucesor) | RI | `sin_raiz` | 128 | sí | 0 | solo como candidato, `:60` (no decidido) |

- Registro: 11 con fila de decisión en la tabla de la tanda 1, 8 sin fila y con `rol_alcance` en el manifiesto de los 152
  (`818c3a43`), y ri_mmsef sin una ni otra. 11 + 8 + 1 = 20.
- ri_dcpc es `marcadores` en la E0 corregida y en la partición legada: no hay nada que declarar.
- «Unidades de extracción» es lo mismo que `unidades_por_to` del manifiesto (y que `chunks` de `conteos.json`) en los 20: no declaro
  diferencia (REPORTE, §1.3).

**U = 3.290** (505 + 251 + 663 + 1.342 + 326 + 203 por estrato; NG 2.836 en 14 TOs, RI 454 en 6).
**Tope = 1,45 × 3.290 × 0,021115 = USD 100,7291.**

## Los candidatos de D-1 (REPORTE, §1.5)

Tope de D-1: 197 + 600 = **797 unidades**. Cascada disjunta sobre los 152: 20 en la lista, 5 de la tanda 0, 14 de fuera, 2 (ri_ao y
ri_cc), 11 de la enmienda 8, 1 sin cobertura exacta (rdbcra), 0 con ids repetidos, 72 con otro modo; 152 − 125 = **27 elegibles**.
Ordenados: 1. ri_mmsef 128, 2. ri_ii_31_12_19 91, 3. cedin 66, 4. ri_sef 38, 5. seggar 36, 6. ri_secoexpo 35, 7. consyr 34, 8. ri_ot
32, 9. ri_nge 30, 10. ri_dsf 28, 11. ri_laft 26, 12. ri_tar 18, 13. ri_pspapt 16, 14. ri_iepsp 13, 15. ri_iesinap 12, 16. ri_transpa
11, 17. asomut 8, 18. micemp 8, 19. ribspc 7, 20. ri_acsf 6, 21. ri_cr 6, 22. ri_tvf 6, 23. ri_esd 5, 24. verac 5, 25. ri_ieccm 4,
26. ri_rcl 4, 27. ri_bdp 3. **Ninguno supera 797: el tope no actúa.** El primero no tiene empate.

## El comando (REPORTE, §1.6)

```
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/segmentacion_oficial_e0r2/s2/scripts/lista_tanda1_S2.py --e0 <salida de E0 de los 152> --raiz <copia del repo> --out <json>
```

De punta a punta: `zsh data/experiment/segmentacion_oficial_e0r2/s2/scripts/lote_tramo1_S2.sh <repo> <trabajo>`. La lista corrió dos
veces sobre la misma E0: iguales byte a byte (`22f33a17…`). El lote, probado de punta a punta con su propia copia y su propia corrida (14:57:05 a 15:03:57, rc 0), da el control y la lista iguales byte a byte.

## Para la mesa (REPORTE, §1.7)

1. **rdbcra** no tiene cobertura exacta en la E0 corregida (6 líneas duplicadas); en la partición legada sí. No cambia el sucesor;
   importa para la tanda final.
2. **ri_mmsef** entra sin alcance decidido (A2 de U-ALCANCE-E1). Sus detecciones de la release de E0 estaban contadas fuera de la
   tanda 1, y el re-censo del tramo 3 es sobre la tanda final: si se miden para la tanda 1, lo decide la autora.
3. **ri_spi:** las 344 unidades de la decisión 1 de la enmienda 8 incluyen las 96 de ri_spi, que el protocolo cuenta entre los 12 no
   segmentables de fuera (`:163-166`). El tramo 3 tiene que declarar con qué lectura cuenta la tanda final.
4. La enmienda 8, §8, da «unos 102,9» para la lista de trabajo; con la E0 corregida da 102,84 (U = 3.359).
5. El health-check de E0 por TO no lo corrí: el despacho no lo pide.

## Repo, `.pyc` y convenciones

- **Foto sha256 del repo, sin `.git`, antes:** 14:46:03 a 14:46:14, 50.530 entradas (7 `.env*` y 1 `NO_ABRIR_` solo por tamaño y
  fecha; 342 enlaces por su destino). La de después, en el mensaje del FRENO (este archivo entra en ella).
- **El `NO_ABRIR_` del repo**, que no abrí: `data/experiment/med_umbrales/p/lote1/freno/NO_ABRIR_marcas_ejemplos_v0_lote1_mesa.json`.
- **`.pyc` fuera de `.venv/`, antes:** 2.213. Los de después, en el mensaje del FRENO.
- **Grep de convenciones:** `controles/grep_convenciones_S2a.txt`.

## Cierre

El paquete `revision_USEG_OFICIAL_FRENO_S2/`, con su `manifest.txt`, y su copia con `ditto` a
`~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/<sesión>/scratchpad/revision_USEG_OFICIAL_FRENO_S2/`, verificada contra el
manifiesto: en el mensaje del FRENO. Nada commiteado, ningún mensaje de commit preparado (el commit lo arma la mesa), nada escrito en
la memoria.

FRENO.
