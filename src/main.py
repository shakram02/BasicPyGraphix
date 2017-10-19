from src.helpers.gl_program import GlProgram
from src.helpers.shape_helpers import Shape, Rectangle
from src.helpers.window_creator import run_program


# def create_quad_points(x, y):
#     return [
#         x, y,
#         x, -y,
#         -x, -y,
#         -x, y
#     ]
#
#
# def create_rect(origin, width, height, z_order):
#     x_first_vert, y_first_vert = origin
#     # Starts from the top leftmost vertex
#     return [
#         x_first_vert, y_first_vert, z_order,
#
#         (x_first_vert + width), y_first_vert, z_order,
#         (x_first_vert + width), (y_first_vert - height), z_order,
#         x_first_vert, (y_first_vert - height), z_order
#     ]
#
#
# def polygon_same_color(n, r, g, b):
#     return n * [r, g, b]
#


def create_rect(width, height, z_order):
    return [
        width, height, z_order,
        width, -height, z_order,
        -width, -height, z_order,
        -width, height, z_order
    ]


def polygon_same_color(n, r, g, b):
    return n * [r, g, b]


def add_shapes():
    # Green rect
    vertices = []
    vertices.extend([
        0.0, 0.0, 0.0,
        0.03, 0.0, 0.0,
        0.03, 0.03, 0.0,
        0.0, 0.03, 0.0,
    ])

    # vertices.extend(create_rect(0.03, 0.03, 0.01))
    offsets = []
    offsets.extend(create_rect(0.1, 0.1, 0.01))
    offsets.extend(create_rect(0.7, 0.1, 0.01))
    offsets.extend(create_rect(0.1, 0.7, 0.01))

    colors = []
    colors.extend(polygon_same_color(4, 0.0, 1.0, 0.0))

    indices = [0, 1, 2, 3, 0]
    sh = Shape(vertices, indices, colors, offsets)
    # r = Rectangle([0, 0], 0.03, 0.03, 0.0)

    r = Rectangle([0.3, 0.5], 0.33, 0.33, 0.0)
    r.fill_color(0.0, 0.6, 0.3)

    s_vertices = []
    s_vertices.extend([
        0.0, 0.5,
        0.0, 0.7,
        0.5, 0.2,
        0.5, -0.2
    ])
    s_colors = []
    s_colors.extend([
        0.0, 0.0, 1.0,
        0.0, 1.0, 0.0,
        1.0, 0.0, 0.0,
        0.5, 0.0, 0.5

    ])
    s_indices = [i for i in range(len(vertices))]
    sh1 = Shape(s_vertices, s_indices, s_colors, offsets)
    return [r, sh1]


if __name__ == "__main__":
    p = GlProgram(add_shapes)
    run_program(p, size=(720, 328), title="Check")
