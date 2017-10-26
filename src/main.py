from renderres.gl_program_rotating import GlProgram
from src.helpers.shape_helpers import Rectangle
from src.helpers.window_creator import run_program

PROGRAM_INSTANCE = None


def shape_loader():
    r = Rectangle([0.0, 0.0], 0.4, 0.1, 0.0)
    return [r]


def main():
    global PROGRAM_INSTANCE
    if PROGRAM_INSTANCE is None:
        PROGRAM_INSTANCE = GlProgram(shape_loader)

    run_program(PROGRAM_INSTANCE, size=(437, 328), title="Check")


if __name__ == "__main__":
    main()
