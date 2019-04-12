from p5 import *


def Vehicle(length):
    """
    https://www.geogebra.org/classic/qns5us64
    it's shown upside down in p5. :(
    """
    st = PShape()
    with st.edit():
        st.add_vertex((0, -length*2))
        st.add_vertex((-length, length*2))
        st.add_vertex((length, length*2))
    return st

def setup():
    size(800, 600)

def draw():
    background(200)
    length = 30
    fill(128, 0, 0, 128)
    awing1 = Vehicle(length)

    fill(0, 128, 0, 128)
    awing2 = Vehicle(length)
    awing2.translate(400, 300)
    awing2.rotate(radians(90))

    awing3 = Vehicle(length)

    with push_matrix():
        translate(100, 200)
        awing4 = Vehicle(length)
        draw_shape(awing4)

    draw_shape(awing1)
    draw_shape(awing2)
    draw_shape(awing3)

if __name__ == '__main__':
    run()