# Propuesta: parada ordenada del runner por SIGUSR1 (para antes de la tanda 1; sin implementar)

Problema (T2-bis): el runner no instala manejadores de señales. SIGINT levanta KeyboardInterrupt en el acto, también
dentro de la lectura HTTP, y una respuesta en curso se paga sin quedar registrada; SIGTERM y SIGUSR1 lo terminan. Un
tope de corrida menor que el del manifiesto solo se puede hacer cumplir desde afuera, con ese riesgo.

Diseño:
1. runner_corpus.py, en main y solo en corrida real: `signal.signal(signal.SIGUSR1, _pedir_parada)`, donde el
   manejador solo prende una bandera de módulo (PARADA_PEDIDA = True) y escribe una línea en el log. Un manejador que no
   levanta excepción deja que Python reanude la llamada del sistema interrumpida (PEP 475): la lectura HTTP en curso
   termina, la caché escribe la fila, el cliente escribe el usage y el guardián el presupuesto.
2. fase_e1 y fase_e3 miran la bandera al principio de cada unidad, junto al chequeo de tope que ya existe, y levantan
   Freno("parada ordenada por SIGUSR1 antes de <id>"); main ya captura Freno: persiste el estado y sale con 3. La
   unidad en curso completa todas sus llamadas (corte, reintentos por forma, ciclo del ratchet) y su registro.
3. Vigilante: manda SIGUSR1 al cruzar el umbral menos el costo máximo de una unidad (por ejemplo, un tercer escalón y
   un ciclo del ratchet), y SIGKILL solo si el proceso no termina en una gracia larga (10 min).
4. Prueba (selftest del runner): un cliente stub que, en la segunda llamada de una unidad, se manda SIGUSR1 a sí mismo;
   se espera salida 3, la unidad completa en extracciones_e1.jsonl, la siguiente sin registro, y una reanudación que
   termina la fase sin llamadas repetidas. Sin la señal, la huella de la corrida stub es la de siempre.
Costo: USD 0. No mueve claves (solo código, como la fila F20).
