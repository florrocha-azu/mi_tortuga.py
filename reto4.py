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












