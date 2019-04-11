from p5 import *


def setup():
    size(630, 360)


def draw():
    background(204)
    ellipse((100, 100), 48, 48)
    v = Vector(2, 5).normalize()
    print(random_uniform(-1, 1), v)


run()