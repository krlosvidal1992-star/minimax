
🐱🐭 Juego del Gato y el Ratón con IA
Un juego de estrategia en Python donde un gato inteligente trata de atrapar a un ratón en un tablero 5x5. Ambos personajes usan el algoritmo Minimax para tomar decisiones óptimas.

🎮 Características del Juego
Tablero 5x5 con movimiento en 4 direcciones (arriba, abajo, izquierda, derecha)

IA para ambos personajes usando algoritmo Minimax

Sistema de turnos con máximo 15 movimientos

Ratón comienza aleatorio y luego se vuelve inteligente

Gato siempre inteligente persiguiendo al ratón

Visualización simple en consola

🚀 Cómo Ejecutar
Requisitos: Python 3.x instalado

Descarga el código o cópialo en un archivo llamado gato_raton.py

Ejecuta en terminal:

bash
python gato_raton.py
🎯 Objetivo del Juego
Para el gato: Atrapar al ratón moviéndose a su misma casilla

Para el ratón: Sobrevivir 15 turnos sin ser atrapado

⚙️ Configuración
Puedes modificar estas variables al inicio del código:

python
TAM = 5           # Tamaño del tablero (5x5)
MAX_TURNOS = 15   # Máximo número de turnos
PROF = 2          # Profundidad de búsqueda de la IA
gato = [0, 0]     # Posición inicial del gato
raton = [2, 2]    # Posición inicial del ratón
🧠 Cómo funciona la IA
Algoritmo Minimax:
Gato: Busca MAXIMIZAR su ventaja (acercarse al ratón)

Ratón: Busca MINIMIZAR la ventaja del gato (alejarse)

Profundidad: Mira 2 movimientos hacia adelante

Función de evaluación:
python
def evaluar(g, r):
    return - (abs(g[0] - r[0]) + abs(g[1] - r[1]))
Valores más altos (cercanos a 0) = mejor para el gato

Valores más bajos (negativos grandes) = mejor para el ratón

📊 Valores especiales
Valor	Significado
999	Gato ganó (atrapó ratón)
-999	Ratón perdió (fue atrapado)
0	Gato y ratón en misma casilla
-1 a -8	Distancia en casillas (Manhattan)
🎮 Ejemplo de partida
text
. . . . .
G . . . .
. . . . .
. . . . .
. . R . .

Turno 1/15
🔧 Estructura del Código
Funciones principales:
mostrar() - Dibuja el tablero en consola

movs(pos) - Calcula movimientos válidos desde una posición

minimax(g, r, prof, es_gato) - Algoritmo de decisión IA

mejor_mov_gato() - Decide mejor movimiento para el gato

mejor_mov_raton() - Decide mejor movimiento para el ratón

Flujo del juego:
Inicializa posiciones

Muestra tablero

Ratón se mueve (aleatorio primeros 2 turnos, luego IA)

Gato se mueve (siempre IA)

Verifica si hay captura

Repite hasta 15 turnos o captura

💡 Posibles Mejoras
Aumentar dificultad: Cambiar PROF = 3 para que piensen más movimientos adelante

Movimiento diagonal: Modificar movs() para incluir diagonales

Interfaz gráfica: Usar PyGame o tkinter para visualización

Obstáculos: Añadir paredes en el tablero

Múltiples ratones: Añadir más objetivos para el gato

🐞 Limitaciones conocidas
Solo movimiento en cruz (no diagonales)

IA puede ser lenta con profundidades mayores a 3

Interfaz solo en consola

Sin sonidos o efectos visuales avanzados

📝 Reglas de movimiento
Gato: Siempre inteligente, usa Minimax

Ratón: Primeros 2 turnos aleatorio, luego inteligente

Movimientos: Solo a posiciones adyacentes (no diagonales)

Límites: No se puede salir del tablero 5x5

🏆 Estrategias
Para el gato:
Cortar el camino del ratón

Acorralarlo en esquinas

Usar movimiento predictivo

Para el ratón:
Mantenerse alejado del gato

Evitar esquinas (menos opciones de escape)

Moverse hacia el centro cuando sea posible

🤝 Contribuir
Si quieres mejorar el juego:

Haz fork del proyecto

Crea una rama (git checkout -b mejora/feature)

Haz commit de tus cambios (git commit -m 'Añadí diagonales')

Push a la rama (git push origin mejora/feature)

Abre un Pull Request

📄 Licencia
Este proyecto es de código abierto y puede ser usado con fines educativos.

👨‍💻 Autor
Juego educativo creado para aprender algoritmos de IA y programación en Python.

¡Diviértete programando y jugando! 🎮🐱🐭
