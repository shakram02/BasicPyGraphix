from os.path import join
from time import sleep

import ModernGL
import numpy as np

from src.helpers.window_creator import WindowData


class GlBaseProgram:
    def __init__(self, on_add_shape_ready):
        self.on_add_shape_ready = on_add_shape_ready
        self._vaos = []
        self._r = 0.15
        self._g = 0.15
        self._b = 0.15

    def set_wnd_data(self, wnd: WindowData):
        """
        Called by the windowing framework, all shapes must be loaded
        here
        :param wnd: window data
        """

        self._wnd = wnd
        self._ctx = ModernGL.create_context()

        self._load_shaders()
        self._load_render_data()

    def _load_shaders(self):
        vertex_shader = self._ctx.vertex_shader(self._read_vertex_shader())
        fragment_shader = self._ctx.fragment_shader(self._read_fragment_shader())

        self._prog = self._ctx.program([vertex_shader, fragment_shader])

    def _load_render_data(self):
        """
        Constructs Vertex array objects for the given shapes
        """

        shapes = self.on_add_shape_ready()
        for shape in shapes:
            shape_vao = self.get_vao_of_shape(shape)
            self._vaos.append(shape_vao)

    def get_vao_of_shape(self, shape):
        """
        Constructs buffers for a given shape, and then composes the vertex array object
        :param shape: shape object that contains vertices, colors and indecies
        :return: Vertex array object of the given shape
        """

        vertices, indices, colors = shape.unpack()
        ibo = self._ctx.buffer(np.array(indices).astype('i4').tobytes())
        vbo = self._ctx.buffer(np.array(vertices).astype('f4').tobytes())
        cbo = self._ctx.buffer(np.array(colors).astype('f4').tobytes())
        aspect_correction = self._prog.uniforms['aspect_ratio_correction']

        # aspect_correction.value = ((height / width), 1)
        aspect_correction.value = (1, 1)
        vao_content = [
            (vbo, '3f', ['vert']),
            (cbo, '3f', ['rgb_color']),
        ]

        return self._ctx.vertex_array(self._prog, vao_content, ibo)

    def render(self, mode=ModernGL.TRIANGLE_FAN):
        """
        Called by the library, rendering logic
        :param mode: Vao rendering mode, will be removed later and included in the objects
        """

        sleep(0.032)  # 24 fps
        self._ctx.viewport = self._wnd.viewport
        self._ctx.clear(self._r, self._g, self._b)

        for vao in self._vaos:
            vao.render(mode)

    def _read_vertex_shader(self) -> str:
        return self._load_shader(self._get_shader_file_path('vertex_shader.glsl'))

    def _read_fragment_shader(self) -> str:
        return self._load_shader(self._get_shader_file_path('fragment_shader.glsl'))

    @staticmethod
    def _load_shader(relative_path):
        file_desc = open(relative_path)
        shader_prog = ''.join(file_desc.readlines())
        file_desc.close()
        return shader_prog

    @staticmethod
    def _get_shader_file_path(file_name, folder_name='shaders'):
        import os
        dot_path = './'
        trials = 0

        while folder_name not in os.listdir(dot_path) and trials < 4:
            dot_path = "." + dot_path
            trials += 1

        return join(dot_path, folder_name, file_name)
