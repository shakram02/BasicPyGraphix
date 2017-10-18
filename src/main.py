from src.helpers.gl_program import GlProgram
from src.helpers.shape_helpers import Shape
from src.helpers.window_creator import run_program


def add_shapes():
    vertices = [
        # Green rect
        -0.03, 0.03,
        0.03, 0.03,
        0.03, -0.03,
        -0.03, -0.03,
    ]
    offsets = [
        -0.1, 0.1,
        0.1, 0.1,
        0.1, -0.1,
        -0.1, -0.1,

        -0.7, 0.1,
        0.7, 0.1,
        -0.7, -0.1,
        0.7, -0.1,

        -0.1, 0.7,
        0.1, 0.7,
        0.1, -0.7,
        -0.1, -0.7
    ]
    colors = [
        0.0, 1.0, 0.0,
        0.0, 1.0, 0.0,
        0.0, 1.0, 0.0,
        0.0, 1.0, 0.0,

    ]
    indices = [0, 1, 2, 3]
    sh = Shape(vertices, indices, colors, offsets)

    return sh.vertices, sh.indices, sh.vertex_colors, sh.offsets, sh.instance_count


if __name__ == "__main__":
    p = GlProgram(add_shapes)
    run_program(p, size=(720, 328), title="Check")
