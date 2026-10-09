# U-SEG-OFICIAL, S1-bis, punto 4 — regla del censo de renglones: la de S1 con un cambio en el hallazgo 1.16

Escrita el 08/10/2026, antes de correr el censo de S1-bis (su sha256 y su hora quedan en `sellos_S1bis.txt` y en
`censo_renglones_S1bis.json`, clave `cambio_de_s1bis`). La aplica `scripts/censo_renglones_S1bis.py` sobre la salida de
la corrida de S1-bis (`e0/`).

## La regla de S1, sin cambios

El censo de renglones y el hallazgo 1.16 siguen la regla v2 de S1, `../s1/regla_censo_renglones_S1.md`, sellada en S1
(sha256 `0b9394753b9a175b74e044f87d78ac73dbda90e8b56d7b1a3e699ad8a0e20597`, 06/10/2026 18:37:49;
`../s1/sellos_S1.txt`). Qué es un renglón, las entradas de las unidades (U, H y T), las cinco clases de cada renglón,
el texto corrido, lo que se reporta y la calibración en `pro::1.1.2.7` no cambian.

## El cambio: el prefijo de sub-documento en el id del ítem (hallazgo 1.16)

En S1 la regla busca el chunk de cada ítem de una lista con el id `<to>::<numero>` (`../s1/scripts/censo_renglones_S1.py:69`).
Con el código de E0 de S0-4 (`18d9e05`), las unidades de un sub-documento llevan el prefijo de su raíz en el id
(`e0_lib.py:2914-2917`, `_unidad`: `f"{p}::{base}"` con `p` = el prefijo de la raíz), y el prefijo queda en la sección raíz de
`estructura_<to>.json` (campo `prefijo`). Con el id de S1, ninguna lista de un sub-documento encuentra sus chunks y la
regla la saltea sin decirlo.

Cambio: el id de cada ítem es `<to>::<prefijo>::<numero>` cuando la sección raíz del nodo lleva `prefijo`, y
`<to>::<numero>` cuando no lo lleva, como en S1. Todo lo demás de la regla del hallazgo 1.16 queda igual: qué es una
lista, el corte de párrafo y el caso.

Información aparte, que no cambia la regla: se cuentan y se listan las listas con algún ítem sin chunk de ese id, que la
regla no evalúa (en S1 se salteaban sin contarse).

## Lista de la tanda 1, para la cifra aparte del hallazgo 1.16

Los 20 documentos del ejemplo del §7 del protocolo entre tandas (`docs/protocolo_entre_tandas.md:281-284`), con ri_pgn en
lugar de ri_cc (`data/experiment/catalogo_unico/registro_alcance_por_tanda.md`, decisión del 07/10/2026): ayccef, expaef,
opefci, adrei; ri_ccna, ri_pgn, ri_rml, ri_gerc; snp_cheq, ceninf, cirmo3, snp_tr; lingeef, depaho, cajasc; manori,
efemin, nmcief; ri_dcpc, ri_oc.
