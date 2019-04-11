from math import pi
from p5 import *


# Vector algebra
# https://p5.readthedocs.io/en/latest/tutorials/vector.html?highlight=mouse_x#vectors-more-algebra

w = None


class Walker:
    def __init__(self):
        self.pos = Vector(width/2, height/2)
        self.vel = Vector(0, 0)
        self.acc = Vector(0, 0)

    def display(self):
        fill(255)
        ellipse(self.pos, 48, 48)

    def update(self):
        mouse = Vector(mouse_x, mouse_y)
        # self.acc = (mouse - self.pos).normalize()  # this is not okay
        self.acc = mouse - self.pos
        # self.acc.normalize()  # this is okay
        self.acc.magnitude = .4
        # self.acc.angle = random_uniform(0, 2*pi)
        # self.acc.rotate(random_uniform(-pi, pi))
        self.vel += self.acc
        self.pos += self.vel


def setup():
    global w
    size(640, 360)
    background(51)

    w = Walker()


def draw():
    w.update()
    w.display()


if __name__ == '__main__':
    run(frame_rate=30)
