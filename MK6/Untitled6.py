import os
import random
import time

def color_text(text, color = "RED"):
    """
    Takes text as string, an color as string, returns colored text, can used in terminal. 
    """
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    ORANGE = '\033[93m'
    RED = '\033[91m'
    if color == 'RED':

        return '\033[91m'+text+'\033[0m'
    elif color == 'CYAN':

        return '\033[96m'+text+'\033[0m'
    elif color == 'BLUE':

        return '\033[94m'+text+'\033[0m'
    elif color == 'GREEN':

        return '\033[92m'+text+'\033[0m'
    elif color == 'ORANGE':

        return '\033[93m'+text+'\033[0m'

print(color_text("przykładowy tekst", "RED"))


WIDTH = 20
HEIGHT = 10 

snake = [(5, 5), (5, 4), (5, 3)]
direction = "d"
food = (random.randint(0, HEIGHT-1)), random.randint(0, WIDTH-1)
superfood = (random.randint(0, (HEIGHT-1/2 )) )

def render_board(HEIGHT = HEIGHT, WIDTH = WIDTH):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if(y,x) == food:
                print(color_text("@"), end="")
            elif (x,y) in snake:
                print("#")
            else:
                print(" ", end="")
        print()

def draw():
    os.system("cls" if os.name == "nt" else "clear")

for y in range(HEIGHT):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (y, x) == food:
                print(color_text("*"), end="")
            elif (y, x) in snake:
                print("#", end="")
            else:
                print(" ", end="")
        print()

def draw():
    os.system("cls" if os.name == "nt" else "clear")
    render_board()


draw()