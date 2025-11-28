# mi_tortuga.py
# Tarea 2 - Ejercicios Unidad 1

# Reto 1: Simula el comportamiento de la tortuga usando solo print() e input()

import turtle

# Pedir al usuario el valor de avance
pasos = int(input("¿Cuántos pasos debe avanzar la tortuga? "))

# Crear la tortuga y moverla
t = turtle.Turtle()
t.forward(pasos)
turtle.done()

#Explicación breve:

#Este programa pide al usuario que escriba cuántos pasos debe avanzar una tortuga. Al ingresar ese número, el programa muestra la posición inicial (que es cero), suma los pasos indicados, y finalmente muestra cómo la tortuga llega a la nueva posición. El objetivo es simular su movimiento usando solo texto.
# Reto 2: Tortuga bajando


import turtle

t = turtle.Turtle()                     # Crea la tortuga
pasos = int(input("¿Cuántos pasos baja la tortuga? "))
t.right(90)                             # Gira para apuntar hacia abajo
t.forward(pasos)                        # Baja la cantidad indicada
turtle.done()                           # Mantiene la ventana abierta

#Explicación breve

#Este programa imprime una "v" por cada paso que la tortuga baja, representando el rastro vertical, y finalmente muestra la tortuga en la posición final.

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
#Reto 4: Encapsula los comportamientos anteriores usando funciones

import turtle

t = turtle.Turtle()
t.speed(1)  # Opcional, para ver mejor

def adelante(n, paso=20, espacio=5):
    for _ in range(n):
        t.pendown()
        t.forward(paso)
        t.penup()
        t.forward(espacio)

def abajo(n, paso=20, espacio=5):
    t.right(90)
    for _ in range(n):
        t.pendown()
        t.forward(paso)
        t.penup()
        t.forward(espacio)
    t.left(90)

    import turtle
#Reto 4: Encapsula los comportamientos anteriores usando funciones
t = turtle.Turtle()
t.speed(1)  # Opcional, para ver mejor

def adelante(n, paso=20, espacio=5):
    for _ in range(n):
        t.pendown()
        t.forward(paso)
        t.penup()
        t.forward(espacio)

def abajo(n, paso=20, espacio=5):
    t.right(90)
    for _ in range(n):
        t.pendown()
        t.forward(paso)
        t.penup()
        t.forward(espacio)
    t.left(90)

# Pedir datos al usuario
pasos_derecha = int(input("¿Cuántas rayitas hacia la derecha? "))
pasos_abajo = int(input("¿Cuántas rayitas hacia abajo? "))

# Dibujar con los datos del usuario
adelante(pasos_derecha)
abajo(pasos_abajo)

turtle.done()

Creamos funciones :

adelante(t, n): mueve la tortuga t nunidades hacia adelante, que en la orientación inicial es a la derecha

abajo(t, n): gira la tortuga 90° a la derecha (queda mirando hacia abajo), avanza nunidades, y luego gira 90° a la izquierda para volver a mirar a la derecha.

Pedimos datos al usuario :

Primero cuantos pasos quiere a la derecha.

Luego cuántos pasos quiere hacia abajo.

Dibujamos la L :

Llamamos adelante(t, pasos_derecha): se dibuja el tramo horizontal.

Llamamos abajo(t, pasos_abajo): se dibuja el tramo vertical.

Juntos forman la L , pero ahora usando funciones reutilizables 

#Reto 5: La tortuga baja las escalas
import turtle

t = turtle.Turtle()
t.speed(1)

def adelante(n, paso=20, espacio=5):
    # Avanza en segmentos horizontales separados
    for _ in range(n):
        t.pendown()
        t.forward(paso)
        t.penup()
        t.forward(espacio)

def abajo(n, paso=20, espacio=5):
    # Baja en segmentos verticales separados
    t.right(90)
    for _ in range(n):
        t.pendown()
        t.forward(paso)
        t.penup()
        t.forward(espacio)
    t.left(90)

num_escalones = int(input("¿Cuántos escalones? "))

for i in range(1, num_escalones + 1):
    print(f"# Escalón {i}")
    pasos_derecha = int(input(f"Escalón {i}: ¿cuántos pasos hacia la derecha? "))
    adelante(pasos_derecha)
    pasos_abajo = int(input(f"Escalón {i}: ¿cuántos pasos hacia abajo? "))
    abajo(pasos_abajo)

turtle.done()

#Breve explicacion
Un escalón = un tramo hacia la derecha + un tramo hacia abajo.

adelante(n): dibuja n pequeños segmentos horizontales separados (simulan los pasos hacia la derecha).

abajo(n): gira la tortuga hacia abajo, dibuja n pequeños segmentos separados verticales y luego la vuelve a orientar hacia la derecha.
esto lo logre con ayuda de inteligencia artificial ya que me falta aprender mas acerca del tema muchas gracias.

