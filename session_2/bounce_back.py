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
        self.acc = Vector(0, 0)

    def apply_force(self, gravity):
        self.acc += gravity

    def check_edges(self):
        if self.pos.y > height:
            self.vel.y *= -1
            self.pos.y = height


def setup():
    size(640, 360)


def draw():
    background(51)

    gravity = Vector(0, 0.1)
    particle.apply_force(gravity)
    particle.check_edges()
    particle.update()
    particle.display()


if __name__ == '__main__':
    particle = Particle()
    run(frame_rate=30)