from src.helpers.gl_program import GlProgram
from src.helpers.window_creator import run_program

if __name__ == "__main__":
    p = GlProgram()
    run_program(p, size=(468, 328), title="Check")
