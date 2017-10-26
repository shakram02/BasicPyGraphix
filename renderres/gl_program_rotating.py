from time import sleep

import ModernGL

from renderres.gl_program_base import GlBaseProgram

"""
    Program to rotate all the drawing
"""


class GlProgram(GlBaseProgram):
    def __init__(self, on_add_shape_ready):
        super().__init__(on_add_shape_ready)

    def _load_shaders(self):
        vertex_shader = self._ctx.vertex_shader(self._load_shader("rotating_shader.glsl"))
        frag_shader = self._ctx.fragment_shader(self._read_fragment_shader())

        self._prog = self._ctx.program([vertex_shader, frag_shader])
        self._rotation = self._prog.uniforms['rotation']

    def render(self, mode=ModernGL.TRIANGLE_FAN):
        self._ctx.viewport = self._wnd.viewport
        self._ctx.clear(self._r, self._g, self._b)
        self._rotation.value = self._wnd.time

        for vao in self._vaos:
            vao.render(mode)
