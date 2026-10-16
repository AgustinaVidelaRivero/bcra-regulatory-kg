# U-SEG-OFICIAL — FRENO S2, final (15/10/2026)

Tramo 3 de S2: el re-censo de la release de E0 antes de la tanda final, con los siete agregados del «seguí» de los tramos 2 y 3 y
los cinco puntos del «seguí» del tramo 3. USD 0, sin API. **Nada commiteado, ningún mensaje de commit preparado; no escribí en la
memoria.** Escribí solo en `s2/` y en el scratchpad. Artefacto: `cifras_segmentacion_oficial.md`, §7; procedimiento:
`REPORTE_S2.md`, tramo 3.

## Paso 0 (con `$HOME` en lugar de la carpeta personal)

```
$ pwd
$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg
$ git log --format=%s -3
Mantenimiento: las anclas al codigo de la resolucion y del ensamblado, puestas al dia
Mandatos firmados: el resultado del re-sellado unico y la variante del alcance por seccion que se mide al derivar
Alcance en el mensaje del extractor: el registro de alcance de la primera tanda llega a sus documentos
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
s2
```

Los tres títulos, los pedidos y en su orden: el 83, el 82 y el de A2. `s2/` está en git, con 43 archivos y sin diferencias con
HEAD; el tramo 2 entró en `96d7d1ab`, igual a lo que entregué.

## Las salidas crudas y las copias (puntos 1 y 2)

- **Fecha:** jueves 15/10/2026, 23:25, antes del domingo 18/10, así que no regeneré nada. Controlé que las salidas sigan ahí:
  - la E0 corregida da los 768 archivos del manifiesto de S0-6b con su sha256 y 10.478 unidades (23:26:49);
  - los tres censos crudos del tramo 2 dan los sha256 de `censos_S2b.json`, `fuentes`;
  - el de sub-documentos, con las claves ordenadas, da `899db5d198d1…`.
- **El scratchpad cambió:** la sesión siguió con uno nuevo. Las salidas de los tramos 1 y 2 están en el anterior, de donde las leí
  después del control.
- **Los cinco controles por nombre** (`.env`, `.env.*`, `*.env`, `NO_ABRIR_*` y enlaces simbólicos), todos en 0:
  - la copia del tramo, a las 23:26:38;
  - la raíz mínima, a las 23:27:24;
  - la copia de la reproducción, a las 23:32:11;
  - al terminar (23:35:54), la copia, la raíz y la salida de la reproducción.
- No corrí `lote_tramo1_S2.sh` ni `lote_tramo2_S2b.sh`: sus salidas estaban y pasaron el control.

## La tanda final (punto 5; `cifras_segmentacion_oficial.md`, §7)

Cascada disjunta sobre los 152:

| motivo | TOs | unidades |
|---|--:|--:|
| tanda 0 | 5 | 671 |
| tanda 1 del tramo 1 | 20 | 3.290 |
| los de fuera del §5 sin razón vigente propia (10 no segmentables, manual y ri2_pm) | 12 | 106 |
| ri_ao, derogado (nota del 04/10/2026 al protocolo, `:432-438`) | 1 | 13 |
| los 15 de la enmienda 8 (ri_spi¹ y ri_con¹ acá) | 15 | 1.189 |
| rdbcra | 1 | 258 |
| **tanda final** | **98** | **4.951** |

- **98 TOs y 4.951 unidades: igual a la cuenta de la mesa.** La suma da 10.478.
- Por clase: normativa general, 74 TOs y 4.507 unidades; régimen informativo, 24 TOs y 444 unidades.
- Por modo: 68 `vigente`, 26 `sin_raiz` y 4 `marcadores`.

## Cobertura, ids y health-check (agregados 2 y 5; punto 4)

- **Cobertura exacta e ids sin repetir en los 98, en la E0 corregida: no hay freno.** Va una fila por TO en el §7.
- **Health-check de los 98:** de 23:28:28 a 23:30:13, rc 0.
  - No reproduce `correr_e0` en **57 de los 98**: corre `e0_lib` sin el driver de e0-r2.
  - Su propio parseo da cobertura exacta en los 98.
  - Veredictos: 71 sanos; 15 con `cid`; 7 con páginas sin sección; 3 con unidades grandes; 1 con `cid` y páginas sin sección; 1
    con páginas sin sección y unidades grandes.
  - Las señales se registran por TO y no excluyen.

## El re-censo (puntos 3 y 4 de la release; punto 3 del «seguí»)

- **Límites de sub-documento:** quedan **33 como detección, en 18 TOs** (anexo 5, parte 14, régimen 13, formulario 1).
  - 11 de ellos están en una página donde la regla A de S0-6a ya abre una división.
  - ri_sef tiene 6 más, pero está en la lista de la regla y la regla los aplica.
  - Antes eran 19 en 6 TOs de la tanda 2 y 37 en 18 de la tanda 3, con otra E0 y otra tanda 1.
- **Hallazgo 1.16:** la cifra principal es la del censo de renglones, **51 en 31 TOs**. Al lado, el detector corregido de S0-5a da 134
  en 60. Antes eran 68 en 37 de la tanda 2 y 5 en 4 de la tanda 3. Las dos van declaradas como detecciones.
- **No propongo una regla para el 1.16.** La general que ya corre es C de S0-6a. Una regla acotada pide leer cada caso para saber que
  es de bajo riesgo, y S2 no lee: si se leen y cuándo, lo decide la autora.
- **`nmaeef::2.9` y la «Sección 1.» de ri_niif:** quedaron fuera por la decisión 2 de la enmienda 8. Solo lo declaro.

¹ ri_spi y ri_con, por su razón vigente (enmienda 8, decisiones 1 y 2); en la partición legada eran no segmentables.

## Reproducción

`lote_tramo3_S2c.sh` corre primero `lote_cifras_S2b.sh` y después el health-check de la tanda final, su resumen, `tanda_final_S2.py`
y el documento. Lo corrí desde una copia nueva del repo, con `s2/` adentro, de 23:32:11 a 23:35:54, rc 0.

- **Los 15 JSON de `cifras/` y el documento: 16 de 16 iguales byte a byte.**
- Sin los JSON del tramo 3, el generador ampliado da byte a byte el documento commiteado en `96d7d1ab`. `lote_cifras_S2b.sh` sigue
  reproduciendo la versión del tramo 2.

## Repo, `.pyc` y convenciones

- Foto sha256 del repo sin `.git` antes del tramo: de 23:25:48 a 23:26:00, 50.903 entradas. La de después va en el mensaje del
  FRENO (este archivo entra en ella).
- `.pyc` fuera de `.venv/`, antes: 2.213 (286 entradas fuera de `.venv/` y `.venv-app/`).
- Grep de convenciones: `controles/grep_convenciones_S2c.txt`.

## Cierre

- **El paquete:** `revision_USEG_OFICIAL_FRENO_S2/`, en el scratchpad nuevo, con los tres tramos y su `manifest.txt`.
- **La copia permanente:** con `ditto`, a
  `~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/1bc3118a-6c01-4cc4-8819-ed4a63a41380/scratchpad/revision_USEG_OFICIAL_FRENO_S2/`.
  La verificación contra el manifiesto va en el mensaje del FRENO. La copia del FRENO S2-b sigue en la carpeta del scratchpad
  anterior (`6b38566a-…`).
- Nada commiteado, ningún mensaje de commit preparado (el commit lo arma la mesa), nada escrito en la memoria.

FRENO.
