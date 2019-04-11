from p5 import *
from random import randint


class Walker:
    def __init__(self):
        global width, height
        self.pos = Vector(width/2, height/2)

    def display(self):
        fill(255)
        ellipse(self.pos, 48, 48)

    def walk(self):
        vel = Vector(randint(-5, 5), randint(-5, 5))
        self.pos += vel


def setup():
    size(640, 360)


w = Walker()  # place w here so w can get the size of canvas

def draw():
    background(51)
    w.walk()
    w.display()


if __name__ == '__main__':
    run(frame_rate=10)