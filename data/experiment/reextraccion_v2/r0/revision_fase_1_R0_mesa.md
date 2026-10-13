# R0, fase 1: revisión de la mesa (13/10/2026)

USD 0. La ejecutora corrió la fase 1 en la sesión `29a33b36…`, con el despacho `b1772547…` (166 renglones), de 16:49 a 17:20. Quedó en
FRENO. Esta nota revisa ese FRENO; las decisiones de la autora para la fase 2 van en el «seguí».

## El paquete

`revision_R0/` (fuera del repo, copia permanente en `fuera_del_repo/scratchpads/29a33b36…/`):
- 35 archivos, todos con el sha256 de su `manifest.txt`;
- ninguno sin listar, y ningún listado que falte.

## Lo que dejó en el repo

- **`reextraccion_v2/r0/`:** 12 archivos, iguales byte a byte a los del paquete. No hay `.pyc` ni `__pycache__`.
- **El resto del repo:** la foto de la mesa, contra la de las 16:45 (antes del despacho), da 12 archivos nuevos (esos) y ningún cambio.
  Además, falta `.claude/scheduled_tasks.lock`, que corresponde a la sesión de la mesa y no a la ejecutora.

## La sesión

Revisada en su registro, por script:
- **Herramientas:** 86 llamadas a Bash, 6 a Read, 7 a Write y 6 a Edit.
- **Lecturas con Read:** solo código: `runner_corpus.py`, `cliente_e3.py` y `ratchet_e3.py`.
- **Escrituras:** 11 en su scratchpad y 2 en `r0/`. Nada en la memoria ni en `.claude/`.
- **Esperas:** ningún `sleep` ni espera programada.
- **API:** ninguna llamada real. La corrida en seco usó un transporte simulado, sin clave.
- **Carpetas vedadas:** ninguna abierta. Las menciones de `fuera_del_repo` son exclusiones de un `grep` y texto de su FRENO.
- **Los `.env`:** el `rsync` de su copia llevó 6 `.env` y un `.env.example`.
  - Los listó por nombre y borró los 6 `.env` por nombre, sin abrirlos.
  - Ninguna salida de la sesión muestra contenido de esos archivos.
  - El `.env.example`, que está rastreado por git, quedó en su scratchpad.
  - Las copias que vengan los excluyen (cláusula de la mesa del 13/10/2026).

## El resultado, leído en sus salidas

Leído por script en `r0/controles/*.json`; no lo volví a correr.

- **El reparto de las 20:** 16 aceptadas con el intento 0, 3 que reintentan y 1 a la cola, el de la enmienda 7, §1.2.
- **La clave de E3 del runner:** es la de O3 en 20 de 20.
- **El costo:** los escenarios de la enmienda 7, §1.4 (A 0,0719, B 0,3102, C 0,7179).
- **E1 del intento 0:** en la caché, con la respuesta igual al crudo guardado, en 20 de 20.
- **La corrida en seco:** pasan 11 de 11 escenarios.
- Todo coincide con su REPORTE.
