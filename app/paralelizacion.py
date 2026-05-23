"""
Plantilla sencilla de paralelizacion en Python.

Incluye dos ejemplos basicos:
1) threading: util para tareas de espera/I-O
2) multiprocessing: util para tareas de CPU

Puedes sustituir la logica interna de las funciones por la de tu prueba.
"""

import threading
import multiprocessing as mp
import time


# -----------------------------
# EJEMPLO 1: THREADING
# -----------------------------
def tarea_thread(nombre: str, segundos: float) -> None:
	"""Funcion generica para un hilo (thread)."""
	print(f"[THREAD] {nombre} inicia")

	# Simula una tarea de espera (por ejemplo, leer API, archivo, red, etc.).
	time.sleep(segundos)

	print(f"[THREAD] {nombre} termina")


def ejemplo_threading() -> None:
	"""Lanza varias tareas en hilos y espera su finalizacion."""
	print("\n=== Ejemplo threading ===")

	# Definimos una lista de trabajos genericos: (nombre, duracion)
	trabajos = [
		("tarea_A", 2),
		("tarea_B", 1),
		("tarea_C", 3),
	]

	hilos = []

	# Crear y arrancar hilos
	for nombre, segundos in trabajos:
		hilo = threading.Thread(target=tarea_thread, args=(nombre, segundos))
		hilos.append(hilo)
		hilo.start()

	# join() hace que el programa principal espere a que terminen los hilos.
	for hilo in hilos:
		hilo.join()

	print("[THREAD] Todas las tareas de threading han finalizado")


# -----------------------------
# EJEMPLO 2: MULTIPROCESSING
# -----------------------------
def tarea_cpu(numero: int) -> tuple[int, int]:
	"""Funcion generica para proceso: devuelve un resultado simple."""
	# Simulamos trabajo de CPU con un bucle.
	acumulado = 0
	for i in range(800_000):
		acumulado += (i * numero) % 11

	return numero, acumulado


def ejemplo_multiprocessing() -> None:
	"""Ejecuta tareas de CPU en paralelo usando procesos."""
	print("\n=== Ejemplo multiprocessing ===")

	datos = [1, 2, 3, 4]

	# Pool crea un conjunto de procesos para repartir trabajo.
	# with cierra el pool automaticamente al terminar.
	with mp.Pool(processes=4) as pool:
		resultados = pool.map(tarea_cpu, datos)

	# Mostramos resultados para ver que cada proceso devolvio algo.
	for numero, resultado in resultados:
		print(f"[PROC] entrada={numero} -> resultado={resultado}")

	print("[PROC] Todas las tareas de multiprocessing han finalizado")


def main() -> None:
	inicio = time.perf_counter()

	# Ejecuta ambos ejemplos.
	ejemplo_threading()
	ejemplo_multiprocessing()

	fin = time.perf_counter()
	print(f"\nTiempo total aproximado: {fin - inicio:.2f} s")


# IMPORTANTE en Windows:
# multiprocessing necesita este bloque para evitar ejecuciones recursivas.
if __name__ == "__main__":
	main()
