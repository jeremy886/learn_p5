from p5 import *


class Particle:
    def __init__(self, start_x, start_y):
        self.pos = Vector(start_x, start_y)
        self.vel = Vector(0, 0)
        self.acc = Vector(0, 0)
        self.radius = 48 * random_uniform(0.1, 1)

    def display(self):
        fill(255, 150)
        circle(self.pos, self.radius)

    def update(self):
        self.vel += self.acc
        self.pos += self.vel
        self.acc = Vector(0, 0)
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
    global particles
    particles = []
    size(640, 360)
    no_stroke()


def mouse_pressed():
    particles.append(Particle(mouse_x, mouse_y))

def key_pressed(event):
    if event.key == " " and len(particles) > 0:
        particles.pop(0)

def draw():
    background(51)

    gravity = Vector(0, .1)
    wind = Vector(.1, 0)
    for particle in particles:
        particle.apply_force(gravity)
        if mouse_is_pressed:
            particle.apply_force(wind)

        particle.update()
        particle.check_edges()
        particle.display()


if __name__ == '__main__':
    run()