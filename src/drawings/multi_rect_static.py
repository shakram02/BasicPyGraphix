from src.helpers.gl_program_static import GlProgram
from src.helpers.shape_helpers import Rectangle
import src.main as m


def add_shapes():
    r = Rectangle([0.3, 0.5], 0.33, 0.33, 0.0)
    r.fill_color(0.4, 0.0, 1.0)

    r1 = Rectangle([0.5, 0.55], 0.33, 0.33, 0.1)
    r1.fill_color(0.4, 0.0, 0.0)

    return [r, r1]


if __name__ == "__main__":
    m.PROGRAM_INSTANCE = GlProgram(add_shapes)
    m.main()
