"""Memory, puzzle game of number pairs.

Exercises:

1. Center and scale the digits and/or symbols in the tiles.
2. Introduce a visual innovation to assist memory (e.g., emojis).
3. Track and display the number of taps/turns taken.
4. Detect when all tiles have been revealed.
5. Center the board on the window or make the window responsive.
"""

from random import shuffle
from turtle import *

# Lista de emojis innovadores para ayudar a la memoria (Punto 2)
emojis = ['🐶', '🐱', '🦊', '🐼', '🐨', '🦁', '🐯', '🐰', 
          '🐶', '🐱', '🦊', '🐼', '🐨', '🦁', '🐯', '🐰']

# Estado del juego: tablero de 32 elementos (16 pares)
# Cada par contiene un número (0-7) y su emoji correspondiente.
tiles = list(range(8)) * 2
shuffle(tiles)

state = {'mark': None}
hide = [True] * 32

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    end_fill()

def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    """Convert tiles index to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape('square')
    stamp()

    for count in range(32):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None:
        x, y = xy(mark)
        up()
        # Modificación 1: Centrar perfectamente los dígitos y emojis en la casilla
        # Como el cuadro es de 50x50, nos posicionamos en el centro exacto (x + 25, y + 5)
        goto(x + 25, y + 5)
        color('black')
        
        # Dibujamos tanto el número como el emoji innovador centrado
        write(f"{tiles[mark]} {emojis[mark]}", align="center", font=('Arial', 20, 'normal'))

    update()
    ontimer(draw, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()