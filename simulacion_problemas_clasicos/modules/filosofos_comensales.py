import threading
import time
import random
from rich import print

# Número de filósofos
NUM_FILOSOFOS = 5

# Inicializamos los estados para el algoritmo de Dekker
turno = 0  # Representa de quién es el turno
interes = [False] * NUM_FILOSOFOS  # Bandera de interés para cada filósofo

# Un cerrojo para evitar que dos filósofos impriman simultáneamente en la consola
cerrojo_impresion = threading.Lock()


class Filosofo(threading.Thread):
    def __init__(self, id_filosofo):
        threading.Thread.__init__(self)
        self.id_filosofo = id_filosofo

    def run(self):
        while True:
            # Pensando
            self.pensar()

            # Intentar tomar tenedores usando la exclusión mutua de Dekker
            self.tomar_tenedores()

            # Comer
            self.comer()

            # Dejar los tenedores
            self.dejar_tenedores()

    def pensar(self):
        with cerrojo_impresion:
            print(f"Filósofo {self.id_filosofo} está [blue]pensando[/blue].")
        time.sleep(random.uniform(1, 3))  # Pensar por un tiempo aleatorio

    def tomar_tenedores(self):
        global turno
        vecino_izq = (
            self.id_filosofo + NUM_FILOSOFOS - 1
        ) % NUM_FILOSOFOS  # El filósofo a la izquierda
        vecino_der = (self.id_filosofo + 1) % NUM_FILOSOFOS  # El filósofo a la derecha

        # Algoritmo de Dekker modificado para permitir acceso a los tenedores
        interes[self.id_filosofo] = True
        while (
            interes[vecino_izq] or interes[vecino_der]
        ):  # Espera activa si vecinos están interesados
            if turno != self.id_filosofo:  # Si no es su turno, cede el control
                interes[self.id_filosofo] = False
                while turno != self.id_filosofo:
                    pass  # Espera activa
                interes[self.id_filosofo] = True

        # Cuando sale del bucle, significa que puede tomar los tenedores
        with cerrojo_impresion:
            print(
                f"Filósofo {self.id_filosofo} ha tomado los [yellow]tenedores izquierdo y derecho[/yellow]."
            )

        time.sleep(1)

    def comer(self):
        with cerrojo_impresion:
            print(f"Filósofo {self.id_filosofo} está [green]comiendo[/green].")
        time.sleep(random.uniform(1, 3))  # Comer por un tiempo aleatorio

    def dejar_tenedores(self):
        global turno
        # Liberar el acceso a los tenedores
        turno = (
            self.id_filosofo + 1
        ) % NUM_FILOSOFOS  # Cambia el turno al siguiente filósofo
        interes[self.id_filosofo] = False
        with cerrojo_impresion:
            print(f"Filósofo {self.id_filosofo} ha dejado los tenedores.")

        time.sleep(1)


# Crear y empezar los hilos para cada filósofo
def ejecutar_filosofos_comensales():
    filosofos = [Filosofo(i) for i in range(NUM_FILOSOFOS)]
    for filosofo in filosofos:
        filosofo.start()

    # Unir los hilos al hilo principal
    for filosofo in filosofos:
        filosofo.join()


if __name__ == "__main__":
    ejecutar_filosofos_comensales()
