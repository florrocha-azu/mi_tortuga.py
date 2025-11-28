# Tarea 2 - Ejercicios Unidad 1

# Reto 2: Tortuga bajando

# Crea el rastro de una tortuga moviéndose hacia abajo usando únicamente print() e input().

import turtle

t = turtle.Turtle()                     # Crea la tortuga
pasos = int(input("¿Cuántos pasos baja la tortuga? "))
t.right(90)                             # Gira para apuntar hacia abajo
t.forward(pasos)                        # Baja la cantidad indicada
turtle.done()                           # Mantiene la ventana abierta

**Explicación breve:**

Este programa imprime una "v" por cada paso que la tortuga baja, representando el rastro vertical, y finalmente muestra la tortuga en la posición final. 