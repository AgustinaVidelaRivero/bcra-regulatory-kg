FIRMADO por la autora — 2026-09-27 (gate 8 de la fase 2 de B6.0; enmienda 8e13be3)

MANDATO — U-OBS12-SORTEO (GATE 8 DE LA FASE 2 DE B6.0):
scripts/muestra_aristas_obs12.py.
Repo bcra-regulatory-kg. Leé CLAUDE.md antes de empezar. Costo de API 0.

CONTEXTO (tres líneas). La enmienda al pre-registro de la tanda 0 sellada
en 8e13be3 (docs/enmienda_preregistro_tanda0_2026-09-27_observacion12.md,
sha256 cbefcb1c…) agrega la observación (12): 30 aristas de extracción del
ensamblado de la tanda 0 sola, sorteadas por regla y semilla, leídas por la
autora contra el texto del punto ancla. Su §2.2 declara el instrumento de
sorteo como PENDIENTE de A5 (gate 8); esta unidad lo escribe y lo prueba
sobre r1. La fase 2 no arranca con instrumentos PENDIENTES. Leé la enmienda
completa (§2.1, §2.2 y §2.3) antes de escribir.

DECISIONES YA TOMADAS (enmienda §2.1 y §2.2; autora 27/09). No se
re-deciden.
1. Universo = aristas de extracción según la observación (10) del
   pre-registro (A4.1): todas las aristas del kg.json menos las de
   relation == 'referencia' y menos las de rol_fuente == 'esqueleto', con
   rol_fuente leído como lo hace el comando de A4.1: e.get('rol_fuente') o,
   si no está, provenance.rol_fuente. Las 41 aristas padre_sugerido
   (rol_fuente cuarentena_flaggeada) quedan DENTRO del universo, porque
   A4.1 no las resta. Sobre r1 el universo debe dar 12.010.
2. Orden: las aristas del universo ordenadas por la tripla (source,
   relation, target) en orden lexicográfico de cadenas, con orden estable.
   Si hay triplas duplicadas, el script las cuenta y las reporta en el
   JSON (campo triplas_duplicadas); sobre r1 deben ser 0.
3. Sorteo: random.Random(semilla).sample(range(n), k) con n = tamaño del
   universo y k = 30, índices ordenados ascendentes. Semilla de la
   observación (12): 20260927 (la fase 2 la pasa por línea de comandos; el
   script no la cablea).
4. Interfaz: python3 scripts/muestra_aristas_obs12.py --kg RUTA --semilla
   ENTERO --out DIRECTORIO [--n 30] [--e0 DIRECTORIO]. --n existe porque la
   enmienda §2.2 lo declara, con default 30. --e0 es el directorio de
   salida de E0 de donde se lee el texto del punto ancla (decisión 6), con
   default data/experiment/reextraccion_v2/e0_chunking/salida_enm01 (el de
   los cinco TOs de desarrollo; la fase 2 pasa el de la tanda 0). Sin --out
   no escribe nada y frena con mensaje.
5. Salida, dos archivos en --out: (a) muestra_obs12.json con: sha256 del
   kg.json, ruta del kg tal como se pasó, semilla, n (tamaño del universo),
   k, triplas_duplicadas, total de aristas, referencia restadas, esqueleto
   restadas, los k índices, y por arista, en el orden de los índices:
   indice, source (id, type, label, properties del nodo), relation, target
   (id, type, label, properties del nodo), properties de la arista (null si
   no tiene), provenance completa y provenances completas, y texto_ancla
   (decisión 6). El JSON no lleva fecha ni hora: dos corridas con los
   mismos argumentos deben ser byte-idénticas. (b) muestra_obs12.md
   legible, con fecha, sha del grafo, semilla, n y k en el encabezado, y
   las k aristas numeradas 1..k en el orden del sorteo, cada una con
   origen, relación, destino, propiedades, provenance y el texto del punto
   ancla.
6. Texto del punto ancla: se lee de <e0>/chunks_<to>.json, la lista de
   chunks de E0 cuyo campo id coincide con provenance.chunk_id de la arista
   (verificado sobre r1: ext::8.5.17.21 existe en chunks_ext.json con
   campos id, to, archivo, unidad, titulo, texto, herencia, paginas;
   chunks_ext.json sha256 cbcd1a86…, commit d082812). texto_ancla = el
   campo texto de ese chunk; se incluye además herencia tal como está. Si
   el chunk_id no está en el archivo, o el archivo chunks_<to>.json no
   existe en --e0, texto_ancla = "NO ENCONTRADO" con el chunk_id buscado, y
   el script no frena: la ausencia se cuenta en el JSON (campo
   textos_no_encontrados) y se reporta.
7. Selftests, en scripts/selftest_muestra_aristas_obs12.py, solo stdlib,
   dos bloques: (i) grafo sintético mínimo escrito en el propio selftest
   (aristas de extracción, de referencia, de esqueleto y padre_sugerido;
   una tripla duplicada; un chunk_id sin texto) que verifica el universo,
   el orden, el conteo de duplicadas, el NO ENCONTRADO y la byte-identidad
   de dos corridas; (ii) corrida sobre r1
   (data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json, sha256
   0226e947…; verificalo y mostralo) con semilla 20260927 y --out
   reports/obs12_selftest_r1/: dos corridas byte-idénticas en el JSON (cmp
   y sha256), n = 12.010, 30 índices distintos, ninguna arista de la
   muestra con relation == 'referencia' ni rol_fuente == 'esqueleto', y
   textos_no_encontrados = 0.
8. Resultado esperado sobre r1, recomputado por la mesa el 27/09 con la
   regla de las decisiones 1–3: universo 12.010, triplas duplicadas 0,
   índices [115, 200, 1159, 1168, 1270, 1750, 1973, 2184, 2334, 3031,
   3215, 3913, 4162, 4792, 5095, 5131, 5754, 5920, 6626, 7628, 7971, 8111,
   8265, 8531, 8821, 10078, 10277, 10433, 10884, 11167], relaciones en la
   muestra establecida_en 11, aplica_a 8, regula 6, limita 3, exceptua 1,
   condiciona 1. Toda diferencia es HALLAZGO y FRENO: significa que el
   orden o el universo no son los de la enmienda; no se ajusta el script
   para coincidir sin reportar primero.

TAREA (una sola unidad): escribir el script de la decisión 4, su selftest
de la decisión 7, y correr el selftest completo. La corrida sobre r1 de
7 (ii) es una salida de prueba, no la muestra de la observación (12): la
muestra real se sortea en la fase 2 sobre el ensamblado de la tanda 0 sola
(enmienda §2.3, paso 4bis).

REQUISITOS TRANSVERSALES (CLAUDE.md §4 a–j).
- Escritura autorizada: scripts/muestra_aristas_obs12.py,
  scripts/selftest_muestra_aristas_obs12.py y el directorio nuevo
  reports/obs12_selftest_r1/ (con los dos archivos de salida de la corrida
  sobre r1). Nada más: ni el pre-registro, ni la enmienda, ni el plan, ni
  ningún kg.json ni archivo de E0, que son solo lectura. No commitees.
  Costo de API 0. Zonas selladas de CLAUDE.md §3 intactas.
- PYTHONDONTWRITEBYTECODE=1 en todo Python que corras; ningún __pycache__
  ni .pyc nuevo en el repo.
- Solo stdlib en los dos archivos. El script no importa nada de la suite
  de shapes ni de la regression suite.
- Toda afirmación con path:línea o comando; conteos recomputados antes de
  escribirse (§4.i); lo que no esté en un artefacto es NO ENCONTRADO, no
  se infiere.
- Cero nombres propios de personas; los mentores solo por rol.
- Paquete de revisión revision_OBS12_sorteo/ en tu scratchpad con
  manifest.txt (sha256 y una línea por archivo): los dos scripts, los dos
  archivos de salida de r1, la salida completa del selftest y el estado
  del árbol. Reporte al frenar de no más de 40 líneas.
- Si tu contexto se acerca al límite o vas a compactar, ANTES escribí en
  tu scratchpad checkpoint_OBS12.md con qué decisiones (1–8) están
  implementadas y qué corridas hiciste, y reportá la ruta.

CRITERIO DE ACEPTACIÓN, con salida en el reporte: selftest en verde con la
cuenta de casos de los dos bloques; los dos sha256 del JSON de r1 (dos
corridas) iguales, pegados, y cmp sin salida; n, triplas_duplicadas, los 30
índices y la distribución de relaciones de r1 iguales a la decisión 8;
grep -c "NO ENCONTRADO" sobre el JSON de r1 = 0; python3
scripts/muestra_aristas_obs12.py --help pegado; git status --short muestra
solo los dos scripts y reports/obs12_selftest_r1/ como no rastreados, más
adjudicar.py y reports/revision_UB21_diag/, preexistentes de otra unidad;
grep de convenciones sobre los cuatro archivos, pegado aunque dé vacío.

FRENO al terminar. La autora revisa antes de commitear; el gate 8 se
cierra en el plan con el commit.
