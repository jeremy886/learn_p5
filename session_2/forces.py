from p5 import *


class Particle:
    def __init__(self):
        global width, height
        self.pos = Vector(width/2, height/2)
        self.vel = Vector(0, 0)
        self.acc = Vector(0, 0)

    def display(self):
        fill(255)
        ellipse(self.pos, 48, 48)

    def update(self):
        self.vel += self.acc
        self.pos += self.vel

    def apply_force(self, gravity):
        self.acc = gravity


def setup():
    size(640, 360)


def draw():
    background(51)

    gravity = Vector(0, 0.1)
    particle.apply_force(gravity)
    particle.update()
    particle.display()


if __name__ == '__main__':
    particle = Particle()
    run()