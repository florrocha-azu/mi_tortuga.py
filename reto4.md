# Reto 4: Tortuga 
# Encapsula los comportamientos anteriores usando funciones


def adelante(n):
    print('-' * n + '> ')  # Movimiento a la derecha con la tortuga al final

def abajo(n):
    for i in range(n):
        print('|')
    print('v ')            # Movimiento hacia abajo, tortuga en la posición final

# Ejemplo: dibujar una "L" con la tortuga
adelante(5)
abajo(3)


# Breve explicacion

Estas funciones encapsulan los movimientos básicos de la tortuga:

adelante(n): Dibuja el camino horizontal con guiones y la tortuga al final.

abajo(n): Dibuja el camino vertical con barras y muestra la tortuga en la posición final.

Con este enfoque puedes componer secuencias más complejas, como una “L”, al combinar las funciones de manera sencilla, cumpliendo el comportamiento esperado mostrado en la unidad.