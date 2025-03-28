import threading
import queue
import time
import random

image_queue = queue.Queue()  #cola sin límite de tamaño
lock = threading.Lock()
semaphore = threading.Semaphore(1)

class Image:
    def __init__(self, id):
        self.name = f"Imagen_{id}"

    def __repr__(self):
        return self.name

def producer():
    #Genera imágenes de forma continua con llegada aleatoria
    image_id = 1

    while True:
        num_images = int(input("Introduce cuántas imágenes van a llegar al satélite: "))

        for _ in range(num_images):
            new_image = Image(image_id)

            with lock:
                image_queue.put(new_image, block=True)
                print(f"[📥] Imagen recibida: {new_image}")

            image_id += 1
            time.sleep(random.uniform(0.5, 2))

def consumer():
    while True:
        image = image_queue.get(block=True)
        print(f"[⚙️] Procesando {image}... ⏳")
        time.sleep(random.uniform(2, 5))
        print(f"[✅] Imagen procesada: {image}")

#creación de hilos
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()



"""En este código, la cola (queue.Queue()) no tiene límite de tamaño, 
lo que significa que puede almacenar una cantidad ilimitada de imágenes. 
Esto puede causar problemas de memoria si el productor es mucho más rápido que el consumidor.
Solucion : Si el número de imágenes es demasiado alto, se debería definir un tamaño máximo para la cola.
usando q.put, las imagenes esperarian antes de entrar en el buffer. 
No he querido ponerlo porque no lo explique en mi texto en el examen"""