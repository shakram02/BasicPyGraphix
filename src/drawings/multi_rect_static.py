import src.main as m
from renderres.gl_program_rotating import GlProgram
from src.helpers.misc import repeat_on_quadrants
from src.helpers.shape_helpers import Rectangle


def symmertically_distributed_rectangles(x_origin, y_origin, rect_width, rect_height):
    """
    Draws 4 rectangles in 4 quadrants given their data
    :param x_origin: x origin coordinate of rectangle
    :param y_origin: y origin coordinate of rectangle
    :param rect_width: width of the drawn rectangle
    :param rect_height: height of the drawn rectangle
    :return: list containing four rectangles distributed in the quadrants
    """
    rects = []
    for x, y in repeat_on_quadrants(x_origin, y_origin):
        r = Rectangle([x, y], rect_width, rect_height, 0.0)
        r.fill_color(0, 1, 0.0)
        rects.append(r)

    return rects


def add_shapes():
    rect_width = 0.03
    rect_height = 0.03
    rects = []
    rects += symmertically_distributed_rectangles(0.08, 0.08, rect_width, rect_height)
    rects += symmertically_distributed_rectangles(0.63, 0.08, rect_width, rect_height)
    rects += symmertically_distributed_rectangles(0.08, 0.63, rect_width, rect_height)
    r = Rectangle([0, 0], 0.7, 0.2)
    r.fill_color(1, 0, 0)

    rects += [r]
    return rects


if __name__ == "__main__":
    m.PROGRAM_INSTANCE = GlProgram(add_shapes)
    m.main()
