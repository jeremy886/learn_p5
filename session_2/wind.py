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
        # print(self.pos, self.vel)

    def apply_force(self, force):
        self.acc += force

    def check_edges(self):
        if self.pos.y > height:
            self.vel.y *= -1
            self.pos.y = height

        if self.pos.x > width:
            self.vel.x *= -1
            self.pos.x = width


def setup():
    size(640, 360)
    gravity = Vector(0, .1)
    wind = Vector(.1, 0)
    particle.apply_force(gravity)
    particle.apply_force(wind)


def draw():
    background(51)

    particle.check_edges()
    particle.update()
    particle.display()


if __name__ == '__main__':
    particle = Particle()
    run()