from os.path import join
from time import sleep

import ModernGL
import numpy as np

from src.lib.window_creator import WindowData


class GlProgram:
    def __init__(self, wnd: WindowData):
        self.wnd = wnd
        self.ctx = ModernGL.create_context()

        vertex_shader = self.ctx.vertex_shader(self._read_vertex_shader())
        fragment_shader = self.ctx.fragment_shader(self._read_fragment_shader())
        self.prog = self.ctx.program([vertex_shader, fragment_shader])
        self.load_render_data()

    def load_render_data(self):
        vertices = np.array([
            0.0, 0.0,
            0.4, 0.4,
            0.1, 0.4,

            -0.4, -0.4,
            -0.1, -0.4,
        ])

        indecies = np.array([0, 1, 2, 0, 3, 4])
        colors = np.array([
            1.0, 1.0, 1.0,
            0.0, 1.0, 0.0,
            0.0, 0.0, 1.0,
            1.0, 1.0, 1.0,
            0.0, 0.0, 1.0
        ])

        self.ibo = self.ctx.buffer(indecies.astype('i4').tobytes())
        self.vbo = self.ctx.buffer(vertices.astype('f4').tobytes())
        self.cbo = self.ctx.buffer(colors.astype('f4').tobytes())

        vao_content = [
            (self.vbo, '2f', ['vert']),
            (self.cbo, '3f', ['rgb_color'])
        ]

        self.vao = self.ctx.vertex_array(self.prog, vao_content, self.ibo)

    def render(self):
        self.ctx.viewport = self.wnd.viewport
        self.ctx.clear(0.15, 0.15, 0.15, 1.0)
        self.vao.render()
        sleep(0.032)  # 24 fps

    def _read_vertex_shader(self) -> str:
        return self._load_shader(self._get_shader_file_path('vertex_shader.glsl'))

    def _read_fragment_shader(self) -> str:
        return self._load_shader(self._get_shader_file_path('fragment_shader.glsl'))

    @staticmethod
    def _load_shader(relative_path):
        file_desc = open(relative_path)
        return ''.join(file_desc.readlines())

    @staticmethod
    def _get_shader_file_path(file_name):
        return join('.', 'shaders', file_name)
