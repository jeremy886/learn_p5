from p5 import *

class Sun:
    def __init__(self, start_x, start_y):
        self.pos = Vector(start_x, start_y)
        self.mass = 300
        self.radius = 30
        self.G = 1


    def compute_attraction(self, planet):
        pos_delta = planet.pos - self.pos
        distance = pos_delta.magnitude
        attraction = pos_delta  # it would be better to use pos_delta.normalize() in the future
        attraction.magnitude = self.G * self.mass * planet.mass / distance**2
        return attraction

    def display(self):
        # radius = 10 * self.mass**(0.33)  # if shape is proportional to the mass, it is not visually appealing.
        circle(self.pos, self.radius)


class Planet:
    def __init__(self):
        self.pos = Vector(400, 40)
        self.vel = Vector(1, 0)
        self.acc = Vector(0, 0)
        self.mass = 1
        self.radius = 10

    def apply_force(self, force):
        self.acc += force / self.mass

    def update(self):
        self.vel += self.acc
        self.pos += self.vel
        self.acc = Vector(0, 0)

    def display(self):
        # radius = 10 * self.mass**(0.33)
        fill(255, 127)
        circle(self.pos, self.radius)


def setup():
    global sun, earth
    size(640, 360)
    no_stroke()
    sun = Sun(width/2, height/2)
    earth = Planet()


def draw():
    background(51)

    force = sun.compute_attraction(earth)
    earth.apply_force(-1 * force)
    # print(force)
    earth.update()
    earth.display()
    sun.display()


if __name__ == '__main__':
    run()