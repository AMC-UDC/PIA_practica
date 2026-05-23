
from timeit import timeit
from threading import Thread
# Función que se ejecutará en paralelo
def function(n):
    pass
# Función principal para ejecutar el cálculo en paralelo usando hilos
def multi_thread(arg, iters):
    threads = [] # Lista para almacenar los hilos
    for i in range(iters): # Crear y arrancar un hilo para cada iteración
        thread = Thread(target=function, args=(arg,)) # arg-tuple de argumentos
        thread.start()
        threads.append(thread)
    # Esperar a que todos los hilos terminen
    for thread in threads:
        thread.join()
# Punto de entrada del programa
def main():
    time_threads = timeit("multi_thread(10, 5)", globals=globals(), number=1)
    print(f"Tiempo de ejecución con multi-threading: {time_threads:.4f} segundos")
if __name__ == "__main__":    main()