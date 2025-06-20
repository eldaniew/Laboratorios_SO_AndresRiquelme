import time
import os

print(f"Inicio del script. PID: {os.getpid()}") # Estado: Nuevo -> Listo -> Ejecutando

try:
    # Mantener el proceso en estado de 'Ejecutando'
    print("Estado: Ejecutando (realizando cálculos...)")
    for i in range(10**9):
        _ = i * i

    # Forzar un estado 'Bloqueado' (esperando por I/O)
    print("Estado: Bloqueado (esperando entrada del usuario por 15 segundos...)")
    time.sleep(15)

except KeyboardInterrupt:
    print("\nProceso interrumpido por el usuario.")

print("Estado: Terminado") # Estado: Terminado