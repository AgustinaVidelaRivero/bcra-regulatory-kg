FIRMADO por la autora — 2026-09-30

MANDATO — U-LECTURA-LIMITA: LECTURA ASISTIDA DE LA MUESTRA SELLADA DE 30 ARISTAS `limita`.
Repo bcra-regulatory-kg. Leé CLAUDE.md antes de empezar.
- Una sola etapa, con FRENO al final: reporte corto (no más de 40 líneas) y espera de la
  revisión de la autora.
- Costo de API del repo: USD 0. Ningún script llama a la API; la lectura la hace esta
  instancia. Neo4j no se usa.

CONTEXTO. Plan, fila B2.11, unidad 4b (docs/plan_tesis.md:393), antes de L-ESQ-R2
(unidad 5, :394).
- Mide la precisión de la relación `limita` en KG-Tanda0-Desarrollo-r1: si el destino de
  cada arista, una Operacion, es el objeto del tope de la Restriccion de origen.
- `limita` pasó de 1.041 aristas en r1 a 284 en desarrollo, y es la relación del ejemplo
  del préstamo (plan, unidad 5, orientación e).

Leé completos, antes de empezar:
- la sección de la muestra en reports/u_umbral/reporte_u_umbral.md, y la medición 4 de
  reports/u_umbral/u2_muestra_trazas.md (procedimiento del sorteo);
- la planilla sellada reports/u_umbral/muestra_limita_30.csv (commit e4d053b, sha256
  8e9818173100ac880c7bdc34121a4f4e66916e42b16636421f5e4e993512b2a9). Verificá su sha al
  inicio y al cierre: la planilla no se edita;
- el precedente de lectura asistida: reports/tanda0/obs12_lectura/fila_obs12.md, sección
  «Desvío declarado».

DECISIONES YA TOMADAS. No se re-deciden.
1. Desvío declarado: la lectura la hace esta instancia de modelo y la revisa la autora;
   no es lectura humana. El resultado se rotula «lectura asistida» en todo artefacto.
   Declará el modelo y la versión de la instancia.
2. Se lee solo con lo que trae la planilla: descripción y `umbral` de la Restriccion,
   descripción de la Operacion, y texto de E0 propio y heredado. No se consultan el
   grafo, otras unidades ni EV2.
3. Regla de lectura, fija; no se ajusta después de empezar:
   - «sí»: según el texto de E0, la Operacion es el acto o la magnitud que el tope de la
     Restriccion acota;
   - «no»: el texto acota otra cosa, o la Operacion no aparece en la cláusula del tope.
     Se anota en una línea qué debería ser el destino, si el texto lo dice;
   - «no decidible»: el texto de la planilla no alcanza para decidir (por ejemplo, una
     tabla linealizada).
4. La unidad no propone cambios al pipeline ni al esquema: solo lee y cuenta.

L1 — Lectura. USD 0.
a. Copia de trabajo, nunca la planilla sellada:
   reports/u_umbral/lectura_limita/lectura_limita_30.csv. Lleva las columnas de la
   planilla más cuatro:
   - veredicto: sí, no o no decidible;
   - justificación: una o dos oraciones, con el tramo del texto de E0 que la sostiene;
   - destino_esperado: solo si el veredicto es «no»;
   - revision_autora: vacía.
b. Script de solo lectura reports/u_umbral/lectura_limita/conteo_lectura.py:
   - verifica que la copia tenga las 30 filas en el orden de la planilla y con los
     mismos ids;
   - cuenta los veredictos;
   - calcula el intervalo de Wilson al 95 % para «sí», sobre los 30 y sobre los
     decididos.
   Doble corrida byte a byte idéntica.
c. Reporte reports/u_umbral/lectura_limita/resultado_lectura_limita.md:
   - los conteos, con su comando, y el intervalo;
   - la lista de los «no» y de los «no decidible», con su justificación;
   - la sección «Desvío declarado», con el modelo y la versión.
FRENO L1: conteos, intervalo y sha256 de lo escrito. La revisión de la autora queda fuera
de la unidad: si cambia algún veredicto, lo anota en revision_autora, y la mesa registra
el resultado final.

REQUISITOS TRANSVERSALES (CLAUDE.md §4 a–j).
- Escrituras: solo reports/u_umbral/lectura_limita/ (se crea) y tu scratchpad.
  - No se editan la planilla sellada, el plan, el checklist, el tablero, el laudo, el
    backlog ni nada bajo data/experiment/.
  - Nada sellado se toca (CLAUDE.md §3).
  - No commitees.
- Python:
  - PYTHONDONTWRITEBYTECODE=1 y .venv/bin/python -B en todo Python.
  - Ningún __pycache__ ni .pyc nuevo: línea de base al inicio (conteo de .pyc) y
    control al cierre.
- Afirmaciones y citas:
  - Toda afirmación lleva path:línea o comando.
  - Los conteos se recomputan antes de escribirse (§4 i).
  - Lo que no esté en un artefacto es NO ENCONTRADO.
  - La tesis no se cita por línea de docs/tesis/main.tex; la fuente es Overleaf.
  - Los mentores solo por rol; cero nombres propios.
- Si algo de este mandato contradice un archivo del repo, mandan los archivos y se
  reporta la contradicción.
- Revisión y checkpoint:
  - Paquete de revisión revision_ULECTURA_LIMITA_L1/ con manifest.txt (sha256 y una
    línea por archivo) y nombres únicos.
  - Checkpoint checkpoint_ULECTURA_LIMITA.md en el scratchpad, actualizado al cierre y
    antes de cualquier compactación.
- Shell zsh: variables entre comillas o como arrays; ningún comentario con # dentro de
  los bloques de comandos para copiar.

CRITERIO DE ACEPTACIÓN:
- el reporte corto con las salidas pedidas;
- git status --short con solo reports/u_umbral/lectura_limita/ como nuevo;
- sha256 de muestra_limita_30.csv igual al inicio y al cierre;
- las 30 filas con veredicto y justificación, y conteos que suman 30;
- doble corrida byte a byte idéntica del script;
- el grep de convenciones, pegado aunque dé vacío.

FRENO al final de la etapa.
