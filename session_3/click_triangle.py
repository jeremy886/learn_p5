from p5 import *


def setup():
    global points
    points = []
    size(640, 360)
    no_stroke()


def mouse_pressed():
    global points
    if len(points) == 0:
        points.append((mouse_x, mouse_y))
    elif points[-1] == (mouse_x, mouse_y):
        return
    points.append((mouse_x, mouse_y))
    if len(points) >= 3:
        points = points[-3:]

def draw():
    background(51)
    if len(points) == 3:
        if key == " ":
            translate(50, 0, 0)
        triangle(points[0], points[1], points[2])



if __name__ == '__main__':
    run()
