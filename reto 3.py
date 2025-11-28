# Tarea 2 - Ejercicios Unidad 1

# Reto 3: Tortuga gira

# Girar y dibujar usando solo print() e input().

import turtle

t = turtle.Turtle()               # Crea una tortuga
distancia1 = int(input("¿Cuántos pasos avanza la tortuga inicialmente? "))
distancia2 = int(input("¿Cuántos pasos avanza la tortuga después de girar? "))

t.forward(distancia1)             # La tortuga avanza la distancia inicial
t.right(90)                       # Gira 90 grados a la derecha
t.forward(distancia2)             # Avanza la segunda distancia formando una 'L'
turtle.done()                     # Mantiene la ventana abierta

#Explicación breve:

#El ingresa primero cuantos pasos avanza la tortuga en línea usuario recta. Luego, la tortuga gira 90 grados (a la derecha) y avanza otra distancia determinada por el usuario. Esto genera en la pantalla gráfica una trayectoria en forma de "L", mostrando la posición final de la tortuga.