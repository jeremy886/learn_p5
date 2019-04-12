from p5 import *


class Vehicle:
    def __init__(self, start_x, start_y):
        self.pos = Vector(start_x, start_y)
        self.vel = Vector(0, 0)
        self.acc = Vector(0, 0)
        self.max_speed = 5
        self.max_force = 0.5

    def seek(self, target):
        """
        Craig Reynolds:
        steering force = desired force - velocity
        """
        desired = target - self.pos
        print(target)
        desired.magnitude = self.max_speed
        steering = desired - self.vel
        steering.limit(self.max_force)
        self.apply_force(steering)

    def apply_force(self, force):
        self.acc += force

    def update(self):
        self.vel += self.acc
        self.vel.limit(self.max_speed)
        self.pos += self.vel
        self.acc = Vector(0, 0)

    def display(self):
        fill(255, 150)
        stroke(255)
        circle(self.pos, 48)

def setup():
    global vehicle
    vehicle = Vehicle(320, 180)
    size(640, 360)
    no_stroke()


def draw():
    background(51)

    target = Vector(mouse_x, mouse_y)
    vehicle.seek(target)
    vehicle.update()
    vehicle.display()


if __name__ == '__main__':
    run()
