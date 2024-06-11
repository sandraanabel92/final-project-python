import time
import logging

#Configuracion del logger.

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def timeit(func):
    #Decorador para medir el tiempo de ejecucion de una funcion
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        logging.info(f"{func.__name__} executed in {elapsed_time:.4f} seconds")
        return result
    return wrapper

def logit(func):
    #Decorador para registrar la ejecucion de una funcion.
    def wrapper(*args, **kwargs):
        logging.info(f"Corriendo {func.__name__}")
        result = func(*args, **kwargs)
        logging.info(f"Completado {func.__name__}")
