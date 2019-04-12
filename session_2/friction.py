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
        print(self.pos, self.vel, self.acc)
        # ellipse(self.pos, scaling_factor * self.mass**.33, scaling_factor * self.mass**.33)
        # Volume of a sphere is 4/3 * pi * r**3, so r is proportional to V**(1/3)

    def update(self):
        self.vel += self.acc
        self.pos += self.vel
        # print(self.pos, self.vel)
        self.acc = Vector(0, 0)

    def apply_force(self, gravity):
        self.acc += gravity / self.mass

    def check_edges(self):
        if self.pos.y > height:
            self.vel.y *= -.9 # damper
            self.pos.y = height

        if self.pos.x > width:
            self.vel.x *= -1
            self.pos.x = width


class Liquid:
    def __init__(self, x, y, width, height, CONSTANT):
        self.pos = Vector(x, y)
        self.width = width
        self.height = height
        self.CONSTANT = CONSTANT

    def has_contained(self, particle):
        global width, height
        return self.pos.x <= particle.pos.x <= self.pos.x + width and self.pos.y <= particle.pos.y <= self.height + height

    def compute_drag(self, particle):
        drag = -1 * particle.vel
        speed = particle.vel.magnitude
        drag.magnitude = self.CONSTANT * speed**2
        return drag

    def display(self):
        fill(50)
        rect(self.pos, self.width, self.height)

def setup():
    global particle1, particle2, liquid
    size(640, 360)
    no_stroke()
    particle1 = Particle(200, 50, 1)
    particle2 = Particle(400, 50, 2)
    liquid = Liquid(0, height/2, width, height/2, 0.05)
5

def draw():
    background(127)
    liquid.display()

    g0 = Vector(0, .05)
    wind = Vector(.1, 0)

    particle1.apply_force(g0 * particle1.mass)  # gravity force is proportional to mass
    particle2.apply_force(g0 * particle2.mass)


    if mouse_is_pressed:
        particle1.apply_force(wind)
        particle2.apply_force(wind)

    if liquid.has_contained(particle1):
        particle1.apply_force(liquid.compute_drag(particle1))
        print('particle 1 inside')

    if liquid.has_contained(particle2):
        particle2.apply_force(liquid.compute_drag(particle2))
        print('particle 2 inside')

    particle1.update()
    particle2.update()
    particle1.check_edges()
    particle2.check_edges()
    particle1.display()
    particle2.display()


if __name__ == '__main__':
    #rect_mode("CORNER")
    run()



"""
Drag

    F_d = 1/2 * p * v^2 * C_d * A
where

    F_d     is the drag force,
    p       is the density of the fluid,[11]
    v       is the speed of the object relative to the fluid,
    A       is the cross sectional area, and
    C_d     is the drag coefficient – a dimensionless number
    
Here, we simplify it to F_d = constant * v^2
"""