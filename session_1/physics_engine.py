from p5 import *


class Walker:
    def __init__(self):
        global width, height
        self.pos = Vector(width/2, 0)
        self.vel = Vector(0, 0)
        self.acc = Vector(0, 0.1)

    def display(self):
        fill(255)
        ellipse(self.pos, 48, 48)

    def update(self):
        self.vel += self.acc
        self.pos += self.vel


def setup():
    size(640, 360)


w = Walker()  # place w here so w can get the size of canvas


def draw():
    background(51)
    w.update()
    w.display()


if __name__ == '__main__':
    run()
