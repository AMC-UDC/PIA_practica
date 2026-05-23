
from timeit import timeit
from multiprocess import Process, Pipe
# Función que se ejecutará en paralelo
def function(n, conn):
    # Operación de ejemplo: suma de los primeros n números
    total = sum(range(n))
    conn.send(total)
    #conn.close() # Cerrar el extremo del proceso hijo
# Función principal para ejecutar el cálculo en paralelo usando procesos
def multi_process(arg, iters):
    processes = [] # Lista para almacenar los procesos
    pipes = [] # Lista para almacenar los extremos de comunicación
    results = [] # Recibir los resultados de cada proceso
    for i in range(iters): # Crear y arrancar un proceso para cada iteración
        me_conn,  other_conn = Pipe()
        processes.append(Process(target=function, args=(arg, other_conn)))
        process.start()
        processes.append(process)
        pipes.append(me_conn)
    # Esperar a que todos los procesos terminen
    for process in processes:
        process.join()
    for pipe in pipes:
        results.append(pipe.recv())
# Punto de entrada del programa
def main():
    time_processes = timeit("multi_process(10, 5)", globals=globals(), number=1)
    print(f"Tiempo de ejecución con multi-process: {time_processes:.4f} segundos")
if __name__ == "__main__":    main()