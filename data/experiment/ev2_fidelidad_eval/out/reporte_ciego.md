# Reporte CIEGO — fidelidad EV2 (120 respuestas × juez v1, N=3)

Veredictos por id OPACO. La tabla id_opaco → (pregunta, grafo) vive en
`desanonimizacion/tabla_id_opaco.json` y NO se cruza acá: el cruce
veredicto × grafo lo computa la revisión (pre-registro §3, ceguera de grafo).

## Instrumento y sellos

- `prompt_juez_v1.md`: `fd446f8e61f46033d7de9b862121c698b2c52dcc2696b7f10993f44e509f5455`
- `juez.py`: `b4a74ba536dd5938aa0935ee088e8327bbad411229679887177653a698421236`
- `mapping.py`: `c905dd1a510925bad7a324722ff593ded09a95e77629e0a7e90fa13d5f3e6660`
- `loader.py`: `5aba8b7a0aa46e8d5c4c83b33884b8cae7d0a099884a7d3bc935de4d3097af8b`
- `harness.py`: `fd267e833866f86850e43130e627b08d78e05523b97484696de0ab0c8c9fba9e`
- `judge.py`: `7169145aaeb3f2d90a7e3873964378aa6520c5688fed136cf5a79ea63b589eaa`
- `llm_cache.py`: `fc86b0e48df464d01d87aa1d8067168d2d522f66ead53f594092a16484c22752`
- `gold`: `1d58733699c325c90510e1ead5f18eac6c3cd970ee3b0ab7ff141da539162b40`

- modelo(s) observado(s): ['claude-sonnet-4-6']
- prompt sha256 observado en las respuestas del juez: ['fd446f8e61f46033d7de9b862121c698b2c52dcc2696b7f10993f44e509f5455']
- stop_reasons: {'end_turn': 360}
- semilla de orden: `juez-ev2-v1`; N=3

## Carga

- respuestas: 120 — por grafo {'run_3': 40, 'v2': 40, 'v3': 40}; 40 preguntas × {3: 40} respuestas; criterios gold 164
- flag `respondible` del agente (metadato de trazas, no viaja al juez): {'False': 36, 'True': 84}

## Corrida

- llamadas: 360 / 360
- freno por proyección: None
- gasto real (desde dbs, filas de `cache`): 360 filas, 585801 in / 172205 out → USD 4.3405
- por repetición: {1: {'filas': 120, 'in': 195267, 'out': 57017, 'usd': 1.4411}, 2: {'filas': 120, 'in': 195267, 'out': 57472, 'usd': 1.4479}, 3: {'filas': 120, 'in': 195267, 'out': 57716, 'usd': 1.4515}}
- precios (USD/MTok): {'in': 3.0, 'out': 15.0}; tope: 7.0
- cross-hits entre repeticiones: **0** (keys por db {'ev2_eval_r1.db': 120, 'ev2_eval_r2.db': 120, 'ev2_eval_r3.db': 120}; intersecciones {'ev2_eval_r1.db∩ev2_eval_r2.db': 0, 'ev2_eval_r1.db∩ev2_eval_r3.db': 0, 'ev2_eval_r2.db∩ev2_eval_r3.db': 0})
- hits por label dentro de cada db: {'ev2_eval_r1.db': {'ev2_eval_r1': 0}, 'ev2_eval_r2.db': {'ev2_eval_r2': 0}, 'ev2_eval_r3.db': {'ev2_eval_r3': 0}} (total 0); accesos por db {'ev2_eval_r1.db': 120, 'ev2_eval_r2.db': 120, 'ev2_eval_r3.db': 120}
- errores del juez (no parseable/truncado): {1: 0, 2: 0, 3: 0}; respuestas incompletas (fuera de agregados): 0 

## Distribución (ciega, sobre los agregados)

- veredicto por pregunta (mapping §2): **{'parcial': 63, 'incorrecto': 27, 'requiere_adjudicacion': 21, 'correcto': 9}** sobre 120
- pares (respuesta, criterio): 492 — modales {'cumplido': 198, 'no_cumplido': 272, 'dudoso': 22}; todas las reps {'cumplido': 594, 'no_cumplido': 819, 'dudoso': 63}
- no-determinismo: unánimes 483/492; no unánimes con dudoso 9; sin_consenso 0
- clasificación auxiliar (modal): {'contenido': 100, 'abstencion': 20}; todas las reps {'contenido': 300, 'abstencion': 60}; no unánime en 0 respuestas
- veredicto × clasificación auxiliar: {'contenido→parcial': 63, 'abstencion→incorrecto': 18, 'contenido→requiere_adjudicacion': 19, 'abstencion→requiere_adjudicacion': 2, 'contenido→correcto': 9, 'contenido→incorrecto': 9}
- auditoría de fragmentos (1476): {'null': 673, 'verbatim': 792, 'fuga_gold': 0, 'no_verbatim': 11}

### Fragmentos no_verbatim / fuga_gold (11)

- EV2R-bf64c7e08b c3 r1 [cumplido] no_verbatim: «Sin márgenes de variación: El crédito de riesgo (CR) se calcula como CR = V - C [...] Con márgenes de variación: El CR se define como la mayor exposición que no alcanza a activar un aumento del margen»
- EV2R-bf64c7e08b c3 r2 [cumplido] no_verbatim: «Sin márgenes de variación: El crédito de riesgo (CR) se calcula como CR = V - C [...] Con márgenes de variación: El CR se define como la mayor exposición que no alcanza a activar un aumento del margen»
- EV2R-bf64c7e08b c3 r3 [cumplido] no_verbatim: «Sin márgenes de variación: El crédito de riesgo (CR) se calcula como CR = V - C [...] Con márgenes de variación: El CR se define como la mayor exposición que no alcanza a activar un aumento del margen»
- EV2R-566d06d654 c4 r2 [no_cumplido] no_verbatim: «la información disponible en el grafo no especifica explícitamente: … (2) la identificación específica que debe utilizarse para turistas extranjeros (si es pasaporte, número de documento, u otro ident»
- EV2R-430cd763db c4 r1 [cumplido] no_verbatim: «Deben entregar a los usuarios copia íntegra de los instrumentos que suscriben al momento de solicitar productos o servicios financieros. Deben habilitar, a través del servicio de banca por Internet o,»
- EV2R-430cd763db c4 r2 [cumplido] no_verbatim: «Deben entregar a los usuarios copia íntegra de los instrumentos que suscriben al momento de solicitar productos o servicios financieros. Deben habilitar, a través del servicio de banca por Internet o,»
- EV2R-430cd763db c4 r3 [cumplido] no_verbatim: «Deben entregar a los usuarios copia íntegra de los instrumentos que suscriben al momento de solicitar productos o servicios financieros. Deben habilitar, a través del servicio de banca por Internet o,»
- EV2R-5f5d416be2 c3 r1 [no_cumplido] no_verbatim: «la información disponible en el grafo no especifica: [...] (2) la fecha exacta en que se registran estas operaciones»
- EV2R-5f5d416be2 c3 r2 [no_cumplido] no_verbatim: «la información disponible en el grafo no especifica: [...] (2) la fecha exacta en que se registran estas operaciones»
- EV2R-5f5d416be2 c3 r3 [no_cumplido] no_verbatim: «la información disponible en el grafo no especifica: [...] (2) la fecha exacta en que se registran estas operaciones»
- EV2R-5744878e5b c2 r1 [cumplido] no_verbatim: «La normativa establece que... debe considerarse la realidad económica del instrumento como criterio fundamental para esta clasificación.»

## Veredictos por id opaco

| id_opaco | K | modales por criterio | veredicto (mapping) | clasif. aux. (3 reps) | fragmentos null/verb/fuga/no_verb |
|---|---|---|---|---|---|
| EV2R-02e54578ef | 4 | dudo dudo no_c cump | requiere_adjudicacion | cont/cont/cont | 3/9/0/0 |
| EV2R-03d3f8c3cc | 5 | cump no_c no_c cump cump | parcial | cont/cont/cont | 2/13/0/0 |
| EV2R-06ecdefdcf | 3 | cump no_c cump | parcial | cont/cont/cont | 3/6/0/0 |
| EV2R-0860d0b8a5 | 4 | no_c cump no_c cump | parcial | cont/cont/cont | 3/9/0/0 |
| EV2R-0d820c5f77 | 5 | cump cump cump cump cump | correcto | cont/cont/cont | 0/15/0/0 |
| EV2R-0e7df6e78b | 4 | dudo cump cump cump | requiere_adjudicacion | cont/cont/cont | 0/12/0/0 |
| EV2R-0f4b9c4a38 | 5 | cump cump no_c no_c no_c | parcial | cont/cont/cont | 6/9/0/0 |
| EV2R-19bfa9f3d4 | 4 | cump cump cump dudo | requiere_adjudicacion | cont/cont/cont | 0/12/0/0 |
| EV2R-19e7bd328b | 3 | cump no_c no_c | parcial | cont/cont/cont | 3/6/0/0 |
| EV2R-1a818dddae | 4 | cump no_c cump cump | parcial | cont/cont/cont | 3/9/0/0 |
| EV2R-1c6a868ded | 4 | cump cump no_c no_c | parcial | cont/cont/cont | 6/6/0/0 |
| EV2R-21c1a0b617 | 5 | no_c cump cump cump cump | parcial | cont/cont/cont | 3/12/0/0 |
| EV2R-27b1161a7e | 4 | no_c cump no_c no_c | parcial | cont/cont/cont | 6/6/0/0 |
| EV2R-2a85163d83 | 5 | cump cump no_c cump cump | parcial | cont/cont/cont | 3/12/0/0 |
| EV2R-2c98b1dd2e | 4 | dudo cump no_c no_c | requiere_adjudicacion | cont/cont/cont | 3/9/0/0 |
| EV2R-2e505e4272 | 5 | cump no_c no_c no_c no_c | parcial | cont/cont/cont | 12/3/0/0 |
| EV2R-3054a3d601 | 4 | no_c cump no_c no_c | parcial | cont/cont/cont | 6/6/0/0 |
| EV2R-31c52bdce3 | 4 | no_c no_c no_c no_c | incorrecto | cont/cont/cont | 3/9/0/0 |
| EV2R-3203adb1f5 | 5 | no_c no_c no_c no_c no_c | incorrecto | cont/cont/cont | 15/0/0/0 |
| EV2R-34182f114a | 4 | no_c no_c no_c no_c | incorrecto | abst/abst/abst | 6/6/0/0 |
| EV2R-3e7ed08b34 | 4 | cump cump cump no_c | parcial | cont/cont/cont | 3/9/0/0 |
| EV2R-42b8a4d5b5 | 2 | no_c dudo | requiere_adjudicacion | cont/cont/cont | 3/3/0/0 |
| EV2R-430cd763db | 4 | no_c cump no_c cump | parcial | cont/cont/cont | 6/3/0/3 |
| EV2R-449017854e | 5 | cump cump no_c dudo cump | requiere_adjudicacion | cont/cont/cont | 3/12/0/0 |
| EV2R-4847ade754 | 4 | no_c no_c cump no_c | parcial | cont/cont/cont | 6/6/0/0 |
| EV2R-48605998a9 | 4 | dudo cump cump no_c | requiere_adjudicacion | cont/cont/cont | 3/9/0/0 |
| EV2R-49130626ed | 4 | cump cump dudo cump | requiere_adjudicacion | cont/cont/cont | 0/12/0/0 |
| EV2R-4b149f2b86 | 4 | cump cump cump no_c | parcial | cont/cont/cont | 3/9/0/0 |
| EV2R-4cfdb0d556 | 5 | no_c dudo no_c no_c no_c | requiere_adjudicacion | cont/cont/cont | 9/6/0/0 |
| EV2R-4e5a68d1e5 | 4 | no_c no_c no_c no_c | incorrecto | cont/cont/cont | 9/3/0/0 |
| EV2R-4e8b2a9f2a | 4 | cump cump cump no_c | parcial | cont/cont/cont | 0/12/0/0 |
| EV2R-4f697233b7 | 4 | cump no_c no_c cump | parcial | cont/cont/cont | 6/6/0/0 |
| EV2R-52ca117f6e | 5 | cump cump no_c no_c cump | parcial | cont/cont/cont | 6/9/0/0 |
| EV2R-533f8ed556 | 5 | no_c cump cump no_c cump | parcial | cont/cont/cont | 6/9/0/0 |
| EV2R-534c224349 | 3 | cump no_c cump | parcial | cont/cont/cont | 3/6/0/0 |
| EV2R-566d06d654 | 5 | no_c no_c no_c no_c cump | parcial | cont/cont/cont | 5/9/0/1 |
| EV2R-56a0c736b6 | 2 | no_c no_c | incorrecto | abst/abst/abst | 6/0/0/0 |
| EV2R-56fd37e775 | 3 | no_c no_c no_c | incorrecto | abst/abst/abst | 9/0/0/0 |
| EV2R-5744878e5b | 4 | cump cump no_c no_c | parcial | cont/cont/cont | 6/5/0/1 |
| EV2R-58a7e9f2a1 | 5 | no_c cump no_c no_c no_c | parcial | cont/cont/cont | 12/3/0/0 |
| EV2R-5a05f0ab37 | 4 | cump cump no_c cump | parcial | cont/cont/cont | 0/12/0/0 |
| EV2R-5c2587d1f8 | 4 | cump cump no_c no_c | parcial | cont/cont/cont | 6/6/0/0 |
| EV2R-5f1966a0ac | 4 | no_c no_c no_c no_c | incorrecto | abst/abst/abst | 12/0/0/0 |
| EV2R-5f5d416be2 | 4 | no_c no_c no_c no_c | incorrecto | cont/cont/cont | 6/3/0/3 |
| EV2R-5f7ea36818 | 5 | no_c no_c no_c no_c no_c | incorrecto | abst/abst/abst | 15/0/0/0 |
| EV2R-6139df8503 | 4 | no_c no_c no_c no_c | incorrecto | cont/cont/cont | 12/0/0/0 |
| EV2R-6759fee853 | 5 | no_c no_c no_c no_c no_c | incorrecto | abst/abst/abst | 15/0/0/0 |
| EV2R-683b69a28b | 4 | cump no_c no_c cump | parcial | cont/cont/cont | 6/6/0/0 |
| EV2R-685e394f60 | 2 | no_c no_c | incorrecto | abst/abst/abst | 3/3/0/0 |
| EV2R-69881a8dc1 | 3 | cump no_c no_c | parcial | cont/cont/cont | 6/3/0/0 |
| EV2R-69c242f6e2 | 4 | cump cump no_c no_c | parcial | cont/cont/cont | 3/9/0/0 |
| EV2R-6ab1fd5859 | 4 | cump no_c no_c no_c | parcial | cont/cont/cont | 6/6/0/0 |
| EV2R-6b605c05fc | 4 | no_c no_c cump no_c | parcial | cont/cont/cont | 9/3/0/0 |
| EV2R-6d8df11da2 | 5 | cump cump cump no_c no_c | parcial | cont/cont/cont | 3/12/0/0 |
| EV2R-6ef274ca11 | 5 | no_c cump cump cump no_c | parcial | cont/cont/cont | 6/9/0/0 |
| EV2R-71e53b8d0d | 4 | no_c no_c no_c no_c | incorrecto | abst/abst/abst | 12/0/0/0 |
| EV2R-757c889e2b | 5 | cump cump cump no_c cump | parcial | cont/cont/cont | 3/12/0/0 |
| EV2R-76c070a6f7 | 4 | cump cump no_c no_c | parcial | cont/cont/cont | 6/6/0/0 |
| EV2R-770383d684 | 4 | no_c cump dudo no_c | requiere_adjudicacion | cont/cont/cont | 6/6/0/0 |
| EV2R-788b326685 | 4 | cump no_c no_c no_c | parcial | cont/cont/cont | 6/6/0/0 |
| EV2R-78c43e95b0 | 5 | cump cump cump cump cump | correcto | cont/cont/cont | 0/15/0/0 |
| EV2R-79d7e0eae7 | 4 | no_c no_c no_c no_c | incorrecto | abst/abst/abst | 12/0/0/0 |
| EV2R-7d9c9100a7 | 4 | cump cump cump cump | correcto | cont/cont/cont | 0/12/0/0 |
| EV2R-7ec4999f79 | 4 | cump no_c cump no_c | parcial | cont/cont/cont | 6/6/0/0 |
| EV2R-7f597a860f | 2 | cump cump | correcto | cont/cont/cont | 0/6/0/0 |
| EV2R-7fd46d1c7d | 3 | dudo cump no_c | requiere_adjudicacion | cont/cont/cont | 3/6/0/0 |
| EV2R-81144122ea | 5 | no_c no_c no_c no_c no_c | incorrecto | abst/abst/abst | 15/0/0/0 |
| EV2R-817253739b | 4 | no_c no_c no_c no_c | incorrecto | abst/abst/abst | 12/0/0/0 |
| EV2R-858b027be2 | 4 | no_c cump no_c no_c | parcial | cont/cont/cont | 7/5/0/0 |
| EV2R-86092f6789 | 4 | no_c no_c no_c cump | parcial | cont/cont/cont | 3/9/0/0 |
| EV2R-87a4ca2cd5 | 4 | cump cump no_c cump | parcial | cont/cont/cont | 0/12/0/0 |
| EV2R-880b3bd1e3 | 4 | dudo no_c no_c no_c | requiere_adjudicacion | cont/cont/cont | 9/3/0/0 |
| EV2R-893f855509 | 4 | cump no_c no_c no_c | parcial | cont/cont/cont | 6/6/0/0 |
| EV2R-8cc2b9e117 | 4 | cump no_c no_c cump | parcial | cont/cont/cont | 3/9/0/0 |
| EV2R-9106789dd2 | 5 | cump cump cump cump cump | correcto | cont/cont/cont | 0/15/0/0 |
| EV2R-92a92b1a02 | 5 | no_c dudo cump no_c no_c | requiere_adjudicacion | cont/cont/cont | 9/6/0/0 |
| EV2R-9d2d578adf | 3 | no_c no_c no_c | incorrecto | abst/abst/abst | 9/0/0/0 |
| EV2R-9de0ed0463 | 5 | no_c cump no_c cump no_c | parcial | cont/cont/cont | 6/9/0/0 |
| EV2R-aa57ae7a53 | 5 | cump cump no_c no_c dudo | requiere_adjudicacion | cont/cont/cont | 3/12/0/0 |
| EV2R-ab046e2162 | 5 | cump no_c no_c no_c dudo | requiere_adjudicacion | cont/cont/cont | 10/5/0/0 |
| EV2R-ad52fab550 | 4 | no_c no_c no_c no_c | incorrecto | abst/abst/abst | 12/0/0/0 |
| EV2R-aeb1d5a938 | 2 | no_c cump | parcial | cont/cont/cont | 3/3/0/0 |
| EV2R-af7241e1b0 | 5 | cump cump no_c no_c cump | parcial | cont/cont/cont | 6/9/0/0 |
| EV2R-b018be139c | 4 | no_c cump no_c no_c | parcial | cont/cont/cont | 9/3/0/0 |
| EV2R-b11146a94b | 2 | no_c no_c | incorrecto | cont/cont/cont | 6/0/0/0 |
| EV2R-b75610d5c2 | 4 | no_c no_c no_c no_c | incorrecto | abst/abst/abst | 7/5/0/0 |
| EV2R-b9683442a7 | 3 | cump no_c no_c | parcial | cont/cont/cont | 6/3/0/0 |
| EV2R-b9757343f9 | 5 | no_c cump no_c no_c no_c | parcial | cont/cont/cont | 9/6/0/0 |
| EV2R-bb1687163d | 4 | cump cump cump cump | correcto | cont/cont/cont | 0/12/0/0 |
| EV2R-bc28232739 | 5 | no_c dudo no_c no_c no_c | requiere_adjudicacion | abst/abst/abst | 12/3/0/0 |
| EV2R-bc430de596 | 4 | cump no_c no_c cump | parcial | cont/cont/cont | 6/6/0/0 |
| EV2R-bedd1e124f | 4 | cump no_c dudo cump | requiere_adjudicacion | cont/cont/cont | 3/9/0/0 |
| EV2R-bf64c7e08b | 4 | cump no_c cump cump | parcial | cont/cont/cont | 3/6/0/3 |
| EV2R-c190e11ebd | 2 | cump cump | correcto | cont/cont/cont | 0/6/0/0 |
| EV2R-c78b3683c5 | 4 | cump no_c no_c no_c | parcial | cont/cont/cont | 9/3/0/0 |
| EV2R-c81fd13aa7 | 4 | no_c no_c no_c no_c | incorrecto | cont/cont/cont | 12/0/0/0 |
| EV2R-c822b6fb54 | 5 | dudo cump no_c cump cump | requiere_adjudicacion | cont/cont/cont | 3/12/0/0 |
| EV2R-cc098791f6 | 5 | cump cump cump cump no_c | parcial | cont/cont/cont | 0/15/0/0 |
| EV2R-cc9fe3cb38 | 4 | cump no_c no_c cump | parcial | cont/cont/cont | 3/9/0/0 |
| EV2R-ce110c1dbb | 5 | no_c no_c no_c no_c no_c | incorrecto | abst/abst/abst | 15/0/0/0 |
| EV2R-d25b8279f2 | 4 | cump no_c no_c cump | parcial | cont/cont/cont | 3/9/0/0 |
| EV2R-d4e1884cfe | 4 | cump no_c cump no_c | parcial | cont/cont/cont | 6/6/0/0 |
| EV2R-d6accbd11f | 4 | no_c no_c no_c no_c | incorrecto | abst/abst/abst | 6/6/0/0 |
| EV2R-d73c21b3c6 | 5 | cump cump cump no_c cump | parcial | cont/cont/cont | 3/12/0/0 |
| EV2R-d73e1114a9 | 4 | no_c no_c no_c dudo | requiere_adjudicacion | cont/cont/cont | 9/3/0/0 |
| EV2R-d7a1118272 | 5 | no_c no_c no_c no_c no_c | incorrecto | abst/abst/abst | 15/0/0/0 |
| EV2R-da217a3f78 | 5 | dudo no_c cump no_c no_c | requiere_adjudicacion | abst/abst/abst | 6/9/0/0 |
| EV2R-dacf6bf651 | 5 | cump cump cump cump cump | correcto | cont/cont/cont | 0/15/0/0 |
| EV2R-de775a09d6 | 4 | cump cump cump no_c | parcial | cont/cont/cont | 0/12/0/0 |
| EV2R-df1f00c307 | 2 | cump cump | correcto | cont/cont/cont | 0/6/0/0 |
| EV2R-e3a45a8998 | 4 | no_c no_c no_c no_c | incorrecto | abst/abst/abst | 12/0/0/0 |
| EV2R-e6f1e5d37c | 5 | no_c dudo cump cump cump | requiere_adjudicacion | cont/cont/cont | 3/12/0/0 |
| EV2R-ea30d82507 | 3 | cump cump no_c | parcial | cont/cont/cont | 0/9/0/0 |
| EV2R-eaad704270 | 4 | cump cump no_c cump | parcial | cont/cont/cont | 0/12/0/0 |
| EV2R-ecb344cdae | 5 | no_c no_c no_c no_c no_c | incorrecto | cont/cont/cont | 15/0/0/0 |
| EV2R-ed1d57375f | 5 | cump cump cump cump no_c | parcial | cont/cont/cont | 3/12/0/0 |
| EV2R-f6fce759e0 | 4 | cump no_c no_c no_c | parcial | cont/cont/cont | 6/6/0/0 |
| EV2R-f7cfd49676 | 2 | no_c no_c | incorrecto | cont/cont/cont | 6/0/0/0 |
| EV2R-f98cbe1614 | 5 | no_c cump no_c no_c no_c | parcial | cont/cont/cont | 9/6/0/0 |
| EV2R-face86ba48 | 4 | cump cump cump no_c | parcial | cont/cont/cont | 3/9/0/0 |

Abreviaturas: cump=cumplido, no_c=no_cumplido, dudo=dudoso, S/C=sin_consenso; abst=abstencion, cont=contenido.
