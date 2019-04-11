from p5 import *


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
        self.acc = Vector(random_uniform(-1, 1), random_uniform(-1, 1))
        self.vel += self.acc
        self.pos += self.vel


def setup():
    global w
    size(640, 360)
    w = Walker()  # place w here so w can get the size of canvas


def draw():
    background(51)
    w.update()
    w.display()


if __name__ == '__main__':
    run(frame_rate=30)
