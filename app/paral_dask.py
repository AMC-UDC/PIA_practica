from timeit import timeit
from dask.distributed import Client
def calculo(n): 
    suma = 0
    for i in range(n): 
        suma += i

def single_process(counter, n_loops): 
    for _ in range(n_loops): 
        calculo(counter) 

def dask_client(counter, n_loops): 
    #client = Client(threads_per_worker=4, n_workers=1) # Configura Dask para usar 4 hilos en un solo worker - GIL!
    client = Client(processes=True, n_workers=4, threads_per_worker=1) # Configura Dask para usar 4 procesos con 1 hilo cada uno - sin GIL!

    results = [] 
    for _ in range(n_loops): 
        results.append(client.submit(calculo, counter)) 
    for result in results: 
        result.result() 

def main(): 
    t = timeit("single_process(80000000, 4)", globals=globals(), 
    number=1) 
    print(f"Tiempo de ejec. usando 1 proceso: {t:.3f}") 
    t = timeit("dask_client(80000000, 4)", globals=globals(), 
    number=1) 
    print(f"Tiempo de ejec. usando Dask remote(): {t:.3f}") 

if __name__ == "__main__": 
 main()