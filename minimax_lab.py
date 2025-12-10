import random
import os
import time

tam = 7
max_turnos = 10
prof = 4

gato = [0, 0]
raton = [2, 2]  

def limpiar(): 
    if os.name == "nt":          # Si el sistema operativo es Windows
       os.system("cls")         # Limpia la pantalla con 'cls'
    else:                        # Si NO es Windows (Linux, Mac)
       os.system("clear")       # Limpia la pantalla con 'clear'

def mostrar_tablero():   #IMPRIME EL TABLERO
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

def movimientos(posicion):   # DEVUELVE LOS MOVIMIENTOS VÁLIDOS

    # Extraigo fila (f) y columna (c) de la posición actual
    f = posicion[0]
    c = posicion[1]

    # Lista de movimientos posibles: arriba, abajo, izquierda, derecha
    movimiento = [
        [f - 1, c],   # arriba
        [f + 1, c],   # abajo
        [f, c - 1],   # izquierda
        [f, c + 1]    # derecha
    ]

    movimientos_validos = [] # Donde guardaré solo los movimientos que sí son válidos

    for m in movimiento:   # Recorro cada movimiento posible
        fila = m[0]
        columna = m[1]

        # Verifico que la fila esté dentro del tablero
        fila_valida = (fila >= 0 and fila < tam)

        # Verifico que la columna esté dentro del tablero
        columna_valida = (columna >= 0 and columna < tam)

        # Si fila y columna están dentro del tablero, lo guardo
        if fila_valida and columna_valida:
            movimientos_validos.append(m)

    return movimientos_validos


def evaluar(g, r):   # DEVUELVE LA EVALUACIÓN DE LA POSICIÓN

    gato_fila = g[0]
    gato_columna = g[1]

    raton_fila = r[0]
    raton_columna = r[1]

    diferencia_filas = abs(gato_fila - raton_fila)
    diferencia_columnas = abs(gato_columna - raton_columna)

    distancia = diferencia_filas + diferencia_columnas

    evaluacion = -distancia

    return evaluacion



def minimax(g, r, prof, es_gato): # ALGORITMO MINIMAX
    if g == r:
        return 999 if es_gato else -999
    if prof == 0:
        return evaluar(g, r)
    
    if es_gato: # GATO MAXIMIZA
        mejor = -9999
        for movimiento in movimientos(g):
            mejor = max(mejor, minimax(movimiento, r, prof-1, False))
        return mejor
    else:
        peor = 9999
        for movimiento in movimientos(r):
            peor = min(peor, minimax(g, movimiento, prof-1, True))
        return peor

def mejor_movimiento_gato(): #DEVUELVE EL MEJOR MOVIMIENTO PARA EL GATO|
    mejor_valor = -9999
    mejor_movimiento = gato.copy()
    for movimiento in movimientos(gato):
        valor = minimax(movimiento, raton, prof, False)
        if valor > mejor_valor:
            mejor_valor = valor
            mejor_movimiento = movimiento
    return mejor_movimiento

def mejor_movimiento_raton(): #DEVUELVE EL MEJOR MOVIMIENTO PARA EL RATON
    peor_valor = 9999
    mejor_movimiento = raton.copy()
    for movimiento in movimientos(raton):
        valor = minimax(gato, movimiento, prof, True)
        if valor < peor_valor:
            peor_valor = valor
            mejor_movimiento = movimiento
    return mejor_movimiento

turnos = 0


while turnos < max_turnos: #Bucle principal del juego
    limpiar()
    mostrar_tablero()
    print(f"Turno {turnos+1}/{max_turnos}")
    
    if gato == raton:
        print("¡El gato atrapó al ratón!")
        break

    # Ratón: 2 turnos random, luego inteligente
    if turnos < 2:
        raton = random.choice(movimientos(raton)) if movimientos(raton) else raton.copy()
    else:
        raton = mejor_movimiento_raton()
    
    # Gato siempre inteligente
    gato = mejor_movimiento_gato()
    
    turnos += 1
    time.sleep(0.3)

limpiar() 
mostrar_tablero()
if turnos < max_turnos:
    print("¡El gato atrapó al ratón!")
else:
    print(f"¡El ratón escapó después de {max_turnos} turnos!")
