import threading
import time

# Dos 'recursos' (locks)
lock_a = threading.Lock()
lock_b = threading.Lock()

def proceso_uno():
    print("Proceso 1: Intentando adquirir lock_a...")
    lock_a.acquire()
    print("Proceso 1: Adquirió lock_a. Esperando 1 seg...")
    time.sleep(1)
    print("Proceso 1: Intentando adquirir lock_b...")
    lock_b.acquire() # <-- Se quedará esperando aquí
    print("Proceso 1: ¡Adquirió ambos!")
    lock_b.release()
    lock_a.release()

def proceso_dos():
    print("Proceso 2: Intentando adquirir lock_b...")
    lock_b.acquire()
    print("Proceso 2: Adquirió lock_b. Esperando 1 seg...")
    time.sleep(1)
    print("Proceso 2: Intentando adquirir lock_a...")
    lock_a.acquire() # <-- Se quedará esperando aquí
    print("Proceso 2: ¡Adquirió ambos!")
    lock_a.release()
    lock_b.release()

t1 = threading.Thread(target=proceso_uno)
t2 = threading.Thread(target=proceso_dos)

t1.start()
t2.start()

print("Esperando que los hilos terminen...")
t1.join()
t2.join()

print("¡Programa terminado!") # <-- Esta línea nunca se alcanzará