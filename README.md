# 📡 Productor-Consumidor de Imágenes Satelitales

Este programa simula un sistema donde un **productor** genera imágenes satelitales y un **consumidor** las procesa. Se utilizan hilos (`threading`) y una cola (`queue.Queue`) para manejar la comunicación entre ambos.

## Cómo funciona el programa
1. **El productor** genera imágenes de manera continua y las coloca en una cola.
2. **El consumidor** toma las imágenes de la cola y las procesa con un tiempo aleatorio.
3. **El programa se ejecuta indefinidamente**, simulando el flujo de imágenes en un sistema en tiempo real.

## Cómo usarlo
1. Ejecuta el script en Python:
   python producer_consumer.py
2. Cuando el programa pregunte, introduce cuántas imágenes van a llegar al satélite.

3. Observa cómo:
📥 Las imágenes se reciben y se almacenan en la cola.
⚙️ El consumidor (equipo de analistas) toma cada imagen y la procesa.
✅ Se indica que la imagen ha sido procesada correctamente.
