# llena_memoria.py
import time

print("Iniciando llenado de memoria RAM.")
print("Presiona Ctrl+C para detener el proceso manualmente.")

memoria_consumida = []
incremento_mb = 100  # Consumir 100 MB en cada paso

try:
    while True:
        # Añade un string de 1MB 100 veces para consumir 100MB
        memoria_consumida.extend([' ' * 1024 * 1024 for _ in range(incremento_mb)])
        total_mb = len(memoria_consumida)
        print(f"Memoria consumida: ~{total_mb} MB")
        time.sleep(1) # Pequeña pausa para poder observar los cambios

except MemoryError:
    print("\n¡MemoryError! La RAM física y probablemente el swap se han agotado.")
    print("El sistema debería estar muy lento o no responder.")

except KeyboardInterrupt:
    print("\nProceso detenido por el usuario.")