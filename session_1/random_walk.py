from p5 import *
from random import randint


class Walker:
    def __init__(self):
        global width, height
        self.x = width/2
        self.y = height/2

    def display(self):
        fill(255)
        ellipse((self.x, self.y), 48, 48)
        # print(self.x, self.y)

    def walk(self):
        self.x += randint(-5, 5)  # or random_uniform(-5, 5)
        self.y += randint(-5, 5)


def setup():
    size(640, 360)


def draw():
    background(51)
    w = Walker()
    w.walk()
    w.display()


if __name__ == '__main__':
    run(frame_rate=5)