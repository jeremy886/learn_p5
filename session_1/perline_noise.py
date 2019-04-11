from p5 import *


xoff = 0


def setup():
    size(640, 360)


def draw():
    global xoff

    background(51)

    x = noise(xoff) * width
    xoff += .01
    fill(255)
    ellipse((x, 180), 48, 48)

run()