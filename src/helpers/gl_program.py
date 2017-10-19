from os.path import join
from time import sleep

import ModernGL
import numpy as np


class GlProgram:
    def __init__(self, on_add_shape_ready):
        self.on_add_shape_ready = on_add_shape_ready
        self.indeces = []
        self.vertices = []
        self.colors = []

        self._vaos = []

    def set_wnd_data(self, wnd):
        self._wnd = wnd
        self._ctx = ModernGL.create_context()

        vertex_shader = self._ctx.vertex_shader(self._read_vertex_shader())
        fragment_shader = self._ctx.fragment_shader(self._read_fragment_shader())

        self._prog = self._ctx.program([vertex_shader, fragment_shader])
        self._load_render_data()

    def _load_render_data(self):
        shapes = self.on_add_shape_ready()
        for shape in shapes:
            shape_vao = self.get_vao_of_shape(shape)
            self._vaos.append(shape_vao)

        # self.mvp = self._prog.uniforms['MVP']
        width, height = self._wnd.size
        # self.mvp.value = (1, 1, 1, 1)

    def get_vao_of_shape(self, shape):
        # vertices, indices, colors, offsets = shape.unpack()
        vertices, indices, colors = shape.unpack()
        ibo = self._ctx.buffer(np.array(indices).astype('i4').tobytes())
        vbo = self._ctx.buffer(np.array(vertices).astype('f4').tobytes())
        cbo = self._ctx.buffer(np.array(colors).astype('f4').tobytes())
        # offset = self._ctx.buffer(np.array(offsets).astype('f4').tobytes())

        vao_content = [
            (vbo, '3f', ['vert']),
            (cbo, '3f', ['rgb_color']),
            # (offset, '3f/i', ['in_pos'])
        ]

        return self._ctx.vertex_array(self._prog, vao_content, ibo)

    def render(self, mode=ModernGL.TRIANGLE_FAN):
        sleep(0.032)  # 24 fps
        self._ctx.viewport = self._wnd.viewport
        self._ctx.clear(0.15, 0.15, 0.15, 1.0)

        for vao in self._vaos:
            vao.render(mode)

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
