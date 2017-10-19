from src.helpers.gl_program import GlProgram
from src.helpers.shape_helpers import Rectangle
from src.helpers.window_creator import run_program


def add_shapes():
    r = Rectangle([0.3, 0.5], 0.33, 0.33, 0.0)
    r.fill_color(0.4, 0.0, 1.0)

    return [r]


if __name__ == "__main__":
    p = GlProgram(add_shapes)
    run_program(p, size=(720, 328), title="Check")
