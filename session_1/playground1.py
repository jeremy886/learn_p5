from p5 import *
x = 100
y = 100

xspeed = 1
yspeed = 3.3

def setup():
    size(200, 200)
    background(255)

def draw():
    global x
    global y
    global xspeed
    global yspeed

    no_stroke()
    fill(255, 10)
    rect((0, 0), width, height)

    # add the current speed to the location
    x = x + xspeed
    y = y + yspeed

    if x > width or x < 0:
        xspeed = -xspeed

    if y > height or y < 0:
        yspeed = -yspeed

    stroke(0)
    fill(175)
    circle((x, y), 16)

if __name__ == '__main__':
    run()
