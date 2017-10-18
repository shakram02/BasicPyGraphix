from os.path import join
from time import sleep

import ModernGL
import numpy as np


class GlProgram:
    def __init__(self, on_add_shape_ready):
        self.on_add_shape_ready = on_add_shape_ready
        self._indeces = []
        self._vertices = []
        self._colors = []

        self._ibo = None
        self._vbo = None
        self._cbo = None

    def set_wnd_data(self, wnd):
        self._wnd = wnd
        self._ctx = ModernGL.create_context()

        vertex_shader = self._ctx.vertex_shader(self._read_vertex_shader())
        fragment_shader = self._ctx.fragment_shader(self._read_fragment_shader())

        self._prog = self._ctx.program([vertex_shader, fragment_shader])
        self._indeces, self._vertices, self._colors = self.on_add_shape_ready()
        self._load_render_data()

    def _load_render_data(self):
        if self._ibo is not None and self._cbo is not None and self._vbo is not None:
            self._ibo.orphan()
            self._cbo.orphan()
            self._vbo.orphan()

        self._ibo = self._ctx.buffer(np.array(self._indeces).astype('i4').tobytes())

        self._vbo = self._ctx.buffer(np.array(self._vertices).astype('f4').tobytes())
        self._cbo = self._ctx.buffer(np.array(self._colors).astype('f4').tobytes())

        vao_content = [
            (self._vbo, '2f', ['vert']),
            (self._cbo, '3f', ['rgb_color'])
        ]

        self.vao = self._ctx.vertex_array(self._prog, vao_content, self._ibo)

    # We can't add the data dynamically, because the main thread blocks on render loop
    # def add_shape(self, vertices: List[float], indeces: List[int],
    #               colors: List[int]):
    #     self._indeces += indeces
    #     self._vertices += vertices
    #     self._colors += colors
    #     self._load_render_data()

    def render(self, mode=ModernGL.TRIANGLES):
        sleep(0.032)  # 24 fps
        self._ctx.viewport = self._wnd.viewport
        self._ctx.clear(0.15, 0.15, 0.15, 1.0)

        self.vao.render(mode)

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
