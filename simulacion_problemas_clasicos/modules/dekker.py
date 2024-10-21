# Importación de scripts y módulos
import time
import random
from rich import print
from threading import Thread
from simulacion_problemas_clasicos.utils import printProgressBar

# Variables globales
NUM_PROCESOS = 2
procesos_desea_entrar = [False] * NUM_PROCESOS
turno = 0


class Dekker(Thread):
    def __init__(self, id_proceso):
        Thread.__init__(self)
        self.id_proceso = id_proceso

    def run(self):
        while True:
            # Comenzamos a ejecutar el proceso
            self.ejecutar_proceso()

    def ejecutar_proceso(self):
        global turno

        # Proceso desea entrar a la región crítica
        procesos_desea_entrar[self.id_proceso] = True

        while turno != self.id_proceso:
            procesos_desea_entrar[self.id_proceso] = False
            # Por cada intento a acceder a la región crítica = 1ms
            time.sleep(1)
            procesos_desea_entrar[self.id_proceso] = True

        print(f"Proceso {self.id_proceso} accede a la región crítica")
        self.region_critica()

        # Se libera el acceso, y se cambia de proceso
        turno = (self.id_proceso + 1) % NUM_PROCESOS

        procesos_desea_entrar[self.id_proceso] = False
        print("")

        # Proceso uno hace otras tareas
        time.sleep(random.uniform(1, 5))

    def region_critica(self):
        # Se simulará segundos dependiendo del tiempo
        segundos = list(range(0, int(random.uniform(1, 5))))
        segundos_tamanio = len(segundos)

        printProgressBar(
            0, segundos_tamanio, prefix="Progreso:", suffix="Completado", length=50
        )

        for i, item in enumerate(segundos):
            # Por cada ciclo esperamos un segundo...
            time.sleep(1)
            printProgressBar(
                i + 1,
                segundos_tamanio,
                prefix="Progreso:",
                suffix="Completado",
                length=50,
            )


def ejecutar_dekker():
    # Ejecutamos los dos hilos para que intenten acceder a la región crítica al mismo tiempo
    procesos = [Dekker(i) for i in range(NUM_PROCESOS)]
    for proceso in procesos:
        proceso.start()

    # Unir los hilos al hilo principal
    for proceso in procesos:
        proceso.join()


# Con esta condición indico que SOLO se debe de ejecutar el programa desde consola
if __name__ == "__main__":
    ejecutar_dekker()
