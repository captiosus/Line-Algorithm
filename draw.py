from display import *

def draw_line(screen, x0, y0, x1, y1, color):
    if x1 == x0:
        if y1 < y0:
            temp = y0
            y0 = y1
            y1 = temp
        while y0 <= y1:
            plot(screen, color, x1, y0)
            y0 += 1
    dx = x1 - x0
    dy = y1 - y0
    if x0 < x1:
        x = x0
        y = y0
    else:
        x = x1
        y = y1
        x1 = x0
        y1 = y0
    A = y1 - y
    B = x - x1
    if bool(dy < 0) ^ bool(dx < 0):
        if abs(dy) < abs(dx):
            #quadrant 4 and 8
            d = 2 * A - B
            while x <= x1:
                plot(screen, color, x, y)
                if (d < 0):
                    y -= 1
                    d -= 2 * B
                x += 1
                d += 2 * A
        else:
            #quadrant 3 and 7
            d = A - 2 * B
            while y >= y1:
                plot(screen, color, x, y)
                if (d > 0):
                    x += 1
                    d += 2 * A
                y -= 1
                d -= 2 * B
    else:
        if abs(dy) < abs(dx):
            #quadrant 1 and 5
            d = 2 * A + B
            while x <= x1:
                plot(screen, color, x, y)
                if (d > 0):
                    y += 1
                    d += 2 * B
                x += 1
                d += 2 * A
        else:
            #quadrant 2 and 6
            d = A + 2 * B
            while y <= y1:
                plot(screen, color, x, y)
                if (d < 0):
                    x += 1
                    d += 2 * A
                y += 1
                d += 2 * B
