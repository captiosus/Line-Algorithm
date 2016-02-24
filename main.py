from display import *
from draw import *
import random
import math

screen = new_screen()
color = [ 0, 0, 0 ]
color[RED] = random.randrange(255)
color[BLUE] = random.randrange(255)
color[GREEN] = random.randrange(255)

for y in range(0, 500, 5):
    draw_line(screen, 250, 400, 250 + int(100 * math.sinh(math.radians(y))), y, color)
    draw_line(screen, 250, 400, 250 + int(-100 * math.sinh(math.radians(y))), y, color)
    draw_line(screen, 250, 400, 250 + int(100 * math.cosh(math.radians(y))), y, color)
    draw_line(screen, 250, 400, 250 + int(-100 * math.cosh(math.radians(y))), y, color)

display(screen)
