from p5 import *


class Particle:
    def __init__(self, start_x, start_y, mass):
        self.pos = Vector(start_x, start_y)
        self.vel = Vector(0, 0)
        self.acc = Vector(0, 0)
        self.mass = mass

    def display(self):
        scaling_factor = 30
        fill(255)
        circle(self.pos, scaling_factor * self.mass**.33)
        # ellipse(self.pos, scaling_factor * self.mass**.33, scaling_factor * self.mass**.33)
        # Volume of a sphere is 4/3 * pi * r**3, so r is proportional to V**(1/3)

    def update(self):
        self.vel += self.acc
        self.pos += self.vel
        # print(self.pos, self.vel)
        self.acc = Vector(0, 0)

    def apply_force(self, gravity):
        self.acc += gravity / self.mass

    def edges(self):
        if self.pos.y > height:
            self.vel.y *= -0.9  # damper
            self.pos.y = height

        if self.pos.x > width:
            self.vel.x *= -1
            self.pos.x = width


def setup():
    size(640, 360)


def draw():
    background(51)
    g0 = Vector(0, .3)
    wind = Vector(.1, 0)

    particle1.apply_force(g0 * particle1.mass)  # gravity force is proportional to mass
    particle2.apply_force(g0 * particle2.mass)

    if mouse_is_pressed:
        particle1.apply_force(wind)
        particle2.apply_force(wind)

    particle1.edges()
    particle2.edges()
    particle1.update()
    particle2.update()
    particle1.display()
    particle2.display()


if __name__ == '__main__':
    particle1 = Particle(200, 100, 1)
    particle2 = Particle(400, 100, 4)
    run()

    # In Clip 5 of Session 5, the lecturer discovered p5js couldn't keep two balls falling in sync because
    # the velos have a very tiny difference and he provided no solution. You don't observe this issue in p5py.