import random
import os
import time

# ==============================
# CONFIGURACIÓN DEL JUEGO
# ==============================

tam = 5              # Tamaño del tablero (5x5)
max_turnos = 15      # Cantidad máxima de turnos
prof = 3             # Profundidad del algoritmo minimax

# Posiciones iniciales
gato = [0, 0]
raton = [3, 3]


# ==============================
# FUNCIONES AUXILIARES
# ==============================

def limpiar():
    """
    Limpia la consola dependiendo del sistema operativo.
    """
    if os.name == "nt":  # Windows
        os.system("cls")
    else:                # Linux / Mac
        os.system("clear")


def mostrar_tablero():
    """
    Imprime el tablero en consola mostrando:
    G = Gato
    R = Ratón
    . = Espacio vacío
    """
    for f in range(tam):
        for c in range(tam):
            if [f, c] == gato:
                print("G", end=" ")
            elif [f, c] == raton:
                print("R", end=" ")
            else:
                print(".", end=" ")
        print()
    print()


# ==============================
# LÓGICA DEL JUEGO
# ==============================

def movimientos(posicion):
    """
    Devuelve una lista con los movimientos válidos
    (arriba, abajo, izquierda, derecha)
    sin salirse del tablero.
    """

    f, c = posicion  # Extraemos fila y columna

    posibles = [
        [f - 1, c],  # Arriba
        [f + 1, c],  # Abajo
        [f, c - 1],  # Izquierda
        [f, c + 1]   # Derecha
    ]

    validos = []

    for fila, columna in posibles:
        # Verificamos que esté dentro del tablero
        if 0 <= fila < tam and 0 <= columna < tam:
            validos.append([fila, columna])

    return validos


def evaluar(g, r):
    """
    Función heurística:
    Calcula la distancia Manhattan entre gato y ratón.
    
    Mientras más cerca esté el gato,
    mejor será el puntaje.
    """

    distancia = abs(g[0] - r[0]) + abs(g[1] - r[1])

    return -distancia  # Negativo porque queremos minimizar distancia


def minimax(g, r, profundidad, es_gato):
    """
    Algoritmo Minimax:

    - El gato intenta MAXIMIZAR el puntaje.
    - El ratón intenta MINIMIZAR el puntaje.
    """

    # Caso base: el gato atrapó al ratón
    if g == r:
        return 999  # Muy bueno para el gato

    # Caso base: llegamos al límite de profundidad
    if profundidad == 0:
        return evaluar(g, r)

    # Turno del gato (MAXIMIZA)
    if es_gato:
        mejor = -9999
        for mov in movimientos(g):
            valor = minimax(mov, r, profundidad - 1, False)
            mejor = max(mejor, valor)
        return mejor

    # Turno del ratón (MINIMIZA)
    else:
        peor = 9999
        for mov in movimientos(r):
            valor = minimax(g, mov, profundidad - 1, True)
            peor = min(peor, valor)
        return peor


def mejor_movimiento_gato():
    """
    Evalúa todos los movimientos posibles del gato
    y devuelve el que tenga mejor puntuación.
    """

    mejor_valor = -9999
    mejor_mov = gato.copy()

    for mov in movimientos(gato):
        valor = minimax(mov, raton, prof, False)

        if valor > mejor_valor:
            mejor_valor = valor
            mejor_mov = mov

    return mejor_mov


def mejor_movimiento_raton():
    """
    Evalúa todos los movimientos posibles del ratón
    y devuelve el que tenga menor puntuación
    (porque el ratón quiere alejarse).
    """

    peor_valor = 9999
    mejor_mov = raton.copy()

    for mov in movimientos(raton):
        valor = minimax(gato, mov, prof, True)

        if valor < peor_valor:
            peor_valor = valor
            mejor_mov = mov

    return mejor_mov


# ==============================
# BUCLE PRINCIPAL DEL JUEGO
# ==============================

turnos = 0

while turnos < max_turnos:

    limpiar()
    mostrar_tablero()
    print(f"Turno {turnos + 1}/{max_turnos}")

    # Verificamos si el gato atrapó al ratón
    if gato == raton:
        print("¡El gato atrapó al ratón!")
        break

    # --- TURNO DEL RATÓN ---
    # Los primeros 2 turnos se mueve al azar
    if turnos < 2:
        movs = movimientos(raton)

        if movs:
            raton = random.choice(movs)
        else:
            raton = raton.copy()
    else:
        raton = mejor_movimiento_raton()

    # --- TURNO DEL GATO ---
    gato = mejor_movimiento_gato()

    turnos += 1
    time.sleep(0.3)


# ==============================
# RESULTADO FINAL
# ==============================

limpiar()
mostrar_tablero()

if gato == raton:
    print("¡El gato atrapó al ratón!")
else:
    print(f"¡El ratón escapó después de {max_turnos} turnos!")

