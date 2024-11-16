import pgzrun
from random import randint

WIDTH = 300
HEIGHT = 300

def draw():
    r = 255
    g = 0
    b = randint(120, 255)
    width = WIDTH
    height = HEIGHT - 200
    for loop in range(20):
        screen.clear()
        rect = ((0, 0), (width, height))
        rect.center = 150, 150
        screen.draw.rect(rect,(r,g,b))
        width = width - 10
        height = height + 10
        r = r - 10
        g = g + 20

pgzrun.go()