import random
import os
import time

# -------------------------
# CONFIGURACIÓN
# -------------------------
tam = 6
max_turnos = 15
prof = 3

gato = [0, 0]
raton = [2, 2]

# -------------------------
# UTILIDADES
# -------------------------
def limpiar():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def mostrar_tablero():
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

# -------------------------
# MOVIMIENTOS
# -------------------------
def movimientos(posicion):
    f = posicion[0]
    c = posicion[1]

    posibles = [
        [f - 1, c],  # arriba
        [f + 1, c],  # abajo
        [f, c - 1],  # izquierda
        [f, c + 1]   # derecha
    ]

    validos = []
    for m in posibles:
        if 0 <= m[0] < tam and 0 <= m[1] < tam:
            validos.append(m)

    return validos

# -------------------------
# EVALUACIÓN
# -------------------------
def evaluar(g, r):
    distancia = abs(g[0] - r[0]) + abs(g[1] - r[1])
    return -distancia  # mejor para el gato cuanto menor la distancia

# -------------------------
# MINIMAX
# -------------------------
def minimax(g, r, profundidad, es_gato):
    if g == r:
        return 999 if es_gato else -999

    if profundidad == 0:
        return evaluar(g, r)

    if es_gato:  # GATO MAXIMIZA
        mejor = -9999
        for mov in movimientos(g):
            valor = minimax(mov, r, profundidad - 1, False)
            mejor = max(mejor, valor)
        return mejor
    else:        # RATÓN MINIMIZA
        peor = 9999
        for mov in movimientos(r):
            valor = minimax(g, mov, profundidad - 1, True)
            peor = min(peor, valor)
        return peor

# -------------------------
# MEJORES MOVIMIENTOS
# -------------------------
def mejor_movimiento_gato():
    mejor_valor = -9999
    mejor = gato.copy()

    for mov in movimientos(gato):
        valor = minimax(mov, raton, prof, False)
        if valor > mejor_valor:
            mejor_valor = valor
            mejor = mov

    return mejor

def mejor_movimiento_raton():
    peor_valor = 9999
    mejor = raton.copy()

    for mov in movimientos(raton):
        valor = minimax(gato, mov, prof, True)
        if valor < peor_valor:
            peor_valor = valor
            mejor = mov

    return mejor

# -------------------------
# BUCLE PRINCIPAL
# -------------------------
turnos = 0

while turnos < max_turnos:
    limpiar()
    mostrar_tablero()
    print(f"Turno {turnos + 1}/{max_turnos}")

    # RATÓN
    if turnos < 2:
        raton = random.choice(movimientos(raton))
    else:
        raton = mejor_movimiento_raton()

    # GATO
    gato = mejor_movimiento_gato()

    # CHEQUEO INMEDIATO DE CAPTURA
    if gato == raton:
        limpiar()
        mostrar_tablero()
        print("¡El gato atrapó al ratón!")
        break

    turnos += 1
    time.sleep(0.3)

# -------------------------
# RESULTADO FINAL
# -------------------------
if gato != raton:
    limpiar()
    mostrar_tablero()
    print(f"¡El ratón escapó después de {max_turnos} turnos!")
