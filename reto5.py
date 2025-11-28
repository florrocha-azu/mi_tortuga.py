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

































