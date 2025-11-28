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