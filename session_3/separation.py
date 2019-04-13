from random import randrange

from p5 import *


class Vehicle:
    def __init__(self, pos_x, pos_y, max_speed=10., max_force=0.5):
        self.pos = Vector(pos_x, pos_y)
        self.vel = Vector(0, 0)
        self.acc = Vector(0, 0)
        self.size = 12
        self.max_speed = max_speed
        self.max_force = max_force


    def apply_force(self, force):
        """
        We can use F=MA, A = Force / Mass
        """
        self.acc += force

    def separate(self, vehicles):
        """
        check near-by vehicles and find desired separation force
        """
        separation_zone = self.size * 5
        pos_diff_sum = Vector(0, 0)
        for v in vehicles:
            if v is self:  # avoid: "Vector has magnitude 0; can't normalize."
                continue
            dist_v = v.pos.dist(self.pos)
            if dist_v < separation_zone:
                pos_diff = self.pos - v.pos
                pos_diff_sum += pos_diff.normalize() / dist_v

        if len(vehicles) > 1:
            pos_diff_mean = pos_diff_sum / len(pos_diff_sum)
            desired = pos_diff_mean * self.max_speed
            steering = desired - self.vel
            steering.limit(self.max_force)
            self.apply_force(steering)

    def update(self):
        self.vel += self.acc
        self.vel.limit(self.max_speed)
        self.pos += self.vel
        self.acc = Vector(0, 0)

    def display(self):
        fill(127)
        stroke(200)
        with push_matrix():
            translate(*self.pos)
            ellipse((0, 0), self.size, self.size)

    def check_borders(self):
        if self.pos.x < -self.size:
            self.pos.x = width + self.size
        if self.pos.x > width + self.size:
            self.pos.x = -self.size
        if self.pos.y < -self.size:
            self.pos.y = height + self.size
        if self.pos.y > height + self.size:
            self.pos.y = -self.size


def setup():
    size(640, 360)

    global vehicles, width, height

    vehicles = [Vehicle(randrange(width), randrange(height)) for _ in range(75)]


def draw():
    background(51)

    global vehicles

    for v in vehicles:
        v.separate(vehicles)
        v.update()
        v.check_borders()
        v.display()


def mouse_dragged():
    global vehicles, mouse_x, mouse_y
    vehicles.append(Vehicle(mouse_x, mouse_y))


if __name__ == '__main__':
    run()