from src.helpers.gl_program_base import GlBaseProgram


class GlProgram(GlBaseProgram):
    def __init__(self, on_add_shape_ready):
        super().__init__(on_add_shape_ready)
