# U-SEG-OFICIAL — FRENO S0-6a (12/10/2026)

**Este archivo nombra unidades con error de corte y de herencia: ninguna lectura a ciegas lo abre, tampoco la de
S1-quater.**

Paso 0 (la ruta, con `$HOME` en lugar del directorio de la usuaria):

```
$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg
e4bb93ce Segmentacion oficial: las fichas de la tanda 0 de la lectura, declaradas
```

Mandato `docs/mandatos/USEG_OFICIAL_S0-6a_correccion_E0.md` leído en HEAD (`5edfd993…`, igual al del despacho) y los
cuatro archivos de `para_la_ejecutora_S0-6a/` (sha256 iguales a los del despacho). USD 0, sin API. **Nada commiteado;
el parche no se aplicó al repo.** Escribí solo `s0_6/`. Detalle: `REPORTE_S0-6a.md`; diseño: `DISENO_S0-6a.md`.

**Diseño aplicado** (DISENO, §1 y §2): las once reglas, cada una detrás de su parámetro o de una función sobre el árbol,
solo en e0-r2 y fuera de la tanda 0 por la misma lista de diez TOs (`TOS_TANDA0_SIN_S0_6`); C reemplaza a R5-a, A a
R5-a′, E a R5-g y H a R5-f en ri_ccna; R5-b a R5-e siguen. **Lo que cambió del mandato y por qué** (DISENO, §3): ajusté
C (cómo se mide la columna del texto propio de una hoja; la columna de los rótulos de los hijos por página), A («sin
número»; tres casos de un título dentro del texto de un punto) y F2 y A frente a R5-c, cada ajuste motivado por una
unidad leída en S1-ter y correcta que la primera corrida rompía (los negativos del §4). La tolerancia de C no cambió.

**Parche** `parche/parche_e0_S0-6a.diff` (`a7b7ea50…`): `e0_lib.py` `bd2190ad…` → `6dd42bf3…` (+984 −38), `correr_e0.py`
`68bd74b5…` → `cd97223a…` (+58 −8), `selftest_e0.py` `789630b5…` → `83ae5576…` (+548 −15). En seco: rc 0 y los tres
archivos finales byte a byte. **Prototipo** `parche/interruptor_prototipo_S0-6a.diff` (`f9a8240f…`, `S0_6_REGLAS` y
`S0_6_TANDA0`); no va al parche de S0-6b.

**Controles** (REPORTE, §2):
- todas apagadas = S0-5b, 768 de 768 (9.665 unidades);
- los 152: prototipo con todas, código final y otra vez el prototipo, 768 de 768 iguales; con el código del parche, dos
  veces más, 768 de 768 iguales entre sí y con el final; **10.584 unidades**; manifiesto
  `manifiestos/manifest_salida_e0_152_S0-6a.json` (formato de `s1ter/manifest_salida.json`; sha256 en el `manifest.txt`
  del paquete);
- **tanda 0: 57 de 57, dos veces** (2.439 unidades); **los 25 de la tanda 0 en los 152: 25 de 25**; el censo da 0
  cambios en la tanda 0 y **ninguna clave de la tanda 0 se mueve**;
- `selftest_e0` **239/239** (188 de S0-5b y 51 de S0-6a: legada, sintéticos, un caso positivo por regla de las 40
  filas, la fila de la tanda 0 con la exclusión apagada solo ahí, los reemplazos y 105 negativos del §4); b52 39/39, b581
  34/34, b582 59/59, b583 33/33; claves de la caché VEREDICTO OK, igual byte a byte a `923dd900…`; selftest de claves
  de S0-6a VEREDICTO OK (y FALLA con la lista perturbada); continuidad: antes 88 (igual a S0-5b), después 76, selftest
  14/14.

**Censos** (REPORTE, §4; `censos/`): la final cambia 118 TOs, 3.825 claves (1.168 creadas, 249 quitadas, 2.408
cambiadas). Todas las reglas son generales salvo **G (solo lingeef), I y K (solo ri_ccna): lingeef y ri_ccna salen de
la bolsa** de la evaluación final, y lo declaro. I no alcanza ri_iepsp ni ri_ieccm. E: de los 87 rechazos por la columna
abre 36; siguen 51 (13 por la columna, 38 por la sucesión). Reglas por lista (REPORTE, §5): E da lo de R5-g (51 de 51)
y H lo de R5-f (11 de 11); C da lo de R5-a en 30 de 43 listas; A separa el bloque de R5-a′ por sus títulos.

**Las 40 filas** (REPORTE, §3, con la tabla del §5 de la nota): 36 corregidas; **no corregida E1-008** (la numeración
del Anexo IV de nmaeef, que vuelve a empezar después de su índice, sigue sin abrirse: el texto queda como cierre de la
raíz 0 del anexo); **dudosas E2-002 en la herencia** (hereda además el texto de la raíz 0 del Anexo III) **y E2-098 en la
herencia** (C lleva al Apartado B las notas de B.1, B.2 y B.3, y B.1.28 las hereda); E2-055 (tanda 0) sigue con error en
la salida y queda corregida en el selftest.

**Las leídas en S1-ter** (REPORTE, §7; `censos/control_leidas_S0-6a.{json,md}`, con texto, regla y lo juzgado): de 286,
189 iguales y 97 cambian; 27 en preguntas con fila en el TSV y **70 para la decisión de la autora**: 9 de corte juzgado
correcto (4 solo de clave por los anexos de A; `ri_ccna::D2A1P1::S0` pasa a la herencia; `gerc::2.3.2::intro` pasa a su
tabla por F2; `ri_rml::1.4.2`, `ri_rml::1.4::cierre` y `ri_oc::B.1::cierre` por C), 15 de herencia juzgada correcta y
55 de herencia no juzgada (una unidad puede estar en dos de esas cuentas: 79 menciones de 70 unidades; 36 de las 70
con C: los párrafos que C sube a la sección los heredan todas sus unidades).

**Lo que la nota deja en mis manos** (DISENO, §4): tolerancia de C 3,0 pt (`TOL_X`), fijada antes del censo; motivo de
E2-065 `raiz_en_columna_profunda_83.7_vs_76.6`, el de E; causa de J general; «Ello, siempre que…» de E1-081 en
`seguef::2.13::cierre`; la aceptación de R5-e, actualizada por K y reescrita sobre todas las unidades de los
formularios, porque A los divide en bloques. **Reemplazo por regla general en E2-007 y E2-058** (la adenda 1, §1;
DISENO, §5): R5-g y R5-c no se revierten; rigen A (E2-007) y A y D (E2-058); E da el resultado de R5-g.

**Claves** (REPORTE, §6; `censos/claves_S0-6a.json`, con la regla de cada una).

**Unidades que no son de las 40 ni de las 286 y me parecen un error de una regla** (solo id y regla; REPORTE, §11): A:
`ri_oc::SA`, `ri_oc::SB`, `ri_oc::SC::chapeau_seccion`, `ri_ccna::D1F3::Sbloque6` a `::Sbloque18`,
`ri_ccna::D1F4::Sbloque19` a `::Sbloque30`, `adfsp::A::S0::chapeau_seccion`, `ri_cc::R4::Sbloque1`; A y E:
`nmaeef::A4::S0::cierre::parte1` a `::parte6`; E: `ri_saofe::S2` a `ri_saofe::S7`; I: el rótulo de `ri_ccna::D1F4`.

**Error propio** (DISENO, §6): dos guardas de A que agregué mirando unidades no leídas; las revertí.

**Archivos `NO_ABRIR_`** (en el paquete, fuera del repo; los revisa la mesa):
- `NO_ABRIR_antes_y_despues_S0-6a.md` `b33ab31b6bc2ac038e8b8b7ee2ec2cbc23a8d2b79daf5af970201c5abbf708ad`
- `NO_ABRIR_antes_y_despues_S0-6a.jsonl` `1c7324c3f8ce7fa549a262afb3b606078cfa65f64053e63deeb00d296e320d5e`
- `NO_ABRIR_control_continuidad_despues_S0-6a.json` `f15d5bd0ab4dc66d7d1c13470181d021d408bdaac1badc05eb567a92e219328d`
- `NO_ABRIR_lista_continuidad_S0-6a.md` `a89662dd64b9b52a898059044282512e254f85f33802263cadbe0b2cde6aaa56`
- `NO_ABRIR_e0_152_S0-6a.tar.gz` `bf977cc2d9795725730ee49380401e230cd214e54e5783244b6b38a14df959fa` (la salida de los 152)
- `NO_ABRIR_tanda0_medicion_sin_exclusion_S0-6a.tar.gz` `af8602cf5274e28dbe63c1527e40f7cbf07913e7ac3905fae7c1e97d7ca4b487`

**Tabla de reprocesamiento**: fila F19d propuesta (REPORTE, §12); el parche corre 14 anclas de la tabla y deja una sin
encontrar entera (`correr_e0.py:140-210` de F19b), que corrige S0-6b.

**Paquete**: `revision_USEG_OFICIAL_FRENO_S0-6a/`, con su `manifest.txt`, copiado con `ditto` a
`~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/3affae38-5acf-4382-b2ca-6d7f152ddb34/scratchpad/revision_USEG_OFICIAL_FRENO_S0-6a/`;
la verificación de esa copia contra el `manifest.txt` va en el mensaje del FRENO.

**Mensaje de commit PREPARADO** (lo arma la mesa; no corrí ningún commit):

```
Segmentacion oficial: la correccion de E0 con reglas generales, en freno (diseno, parche, censos y controles)
```

FRENO.
