import os
import time
import random

TAM = 7
MAX_TURNOS = 25
PROF = 2

gato = [0, 0]
raton = [2, 2]

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def mostrar():
    for f in range(TAM):
        for c in range(TAM):
            if [f, c] == gato:
                print("G", end=" ")
            elif [f, c] == raton:
                print("R", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

def movs(pos):
    f, c = pos
    moves = [[f-1, c], [f+1, c], [f, c-1], [f, c+1]]
    return [m for m in moves if 0 <= m[0] < TAM and 0 <= m[1] < TAM]

def evaluar(g, r):
    return - (abs(g[0] - r[0]) + abs(g[1] - r[1]))

def minimax(g, r, prof, es_gato):
    if g == r:
        return 999 if es_gato else -999
    if prof == 0:
        return evaluar(g, r)
    
    if es_gato:
        mejor = -9999
        for mov in movs(g):
            mejor = max(mejor, minimax(mov, r, prof-1, False))
        return mejor
    else:
        peor = 9999
        for mov in movs(r):
            peor = min(peor, minimax(g, mov, prof-1, True))
        return peor

def mejor_mov_gato():
    mejor_val = -9999
    mejor_mov = gato.copy()
    for mov in movs(gato):
        val = minimax(mov, raton, PROF, False)
        if val > mejor_val:
            mejor_val = val
            mejor_mov = mov
    return mejor_mov

def mejor_mov_raton():
    peor_val = 9999
    mejor_mov = raton.copy()
    for mov in movs(raton):
        val = minimax(gato, mov, PROF, True)
        if val < peor_val:
            peor_val = val
            mejor_mov = mov
    return mejor_mov

# JUEGO DIRECTO SIN MENÚ
turnos = 0

while turnos < MAX_TURNOS:
    limpiar()
    mostrar()
    print(f"Turno {turnos+1}/{MAX_TURNOS}")
    
    if gato == raton:
        print("¡El gato atrapó al ratón!")
        break
    
    # Ratón: 2 turnos random, luego inteligente
    if turnos < 2:
        raton = random.choice(movs(raton)) if movs(raton) else raton.copy()
    else:
        raton = mejor_mov_raton()
    
    # Gato siempre inteligente
    gato = mejor_mov_gato()
    
    turnos += 1
    time.sleep(0.3)

limpiar()
mostrar()
if turnos < MAX_TURNOS:
    print("¡El gato atrapó al ratón!")
else:
    print(f"¡El ratón escapó después de {MAX_TURNOS} turnos!")