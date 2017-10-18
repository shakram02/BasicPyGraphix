from src.helpers.gl_program import GlProgram
from src.helpers.window_creator import run_program


def add_shapes():
    vertices = [
        0.0, 0.0,
        0.4, 0.4,
        0.1, 0.4,

        -0.4, -0.4,
        -0.1, -0.4,
    ]
    colors = [
        1.0, 1.0, 1.0,
        0.0, 1.0, 0.0,
        0.0, 0.0, 1.0,
        1.0, 1.0, 1.0,
        0.0, 0.0, 1.0
    ]
    indices = [0, 1, 2, 0, 3, 4]

    return indices, vertices, colors


if __name__ == "__main__":
    p = GlProgram(add_shapes)
    run_program(p, size=(468, 328), title="Check")
