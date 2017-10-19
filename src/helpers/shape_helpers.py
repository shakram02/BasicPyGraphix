from typing import List


class Shape:
    def __init__(self, vertices: List, indices: List, dimen_count=3):
        self._vertex_dimen = dimen_count
        self._vertices: List = vertices
        self._indices: List = indices
        self._vertex_colors = []

    @property
    def vertices(self):
        return self._vertices

    def unpack(self):
        return self._vertices, self._indices, self._vertex_colors

    def fill_color(self, r, g, b):
        pass

    def fill_points(self, vertex_colors):
        pass


class Rectangle(Shape):
    def __init__(self, origin, width, height, z_order):
        self._indices = [0, 1, 2, 3, 0]
        self._zorder = z_order
        self._vertices = self._create_rect_at(origin, width, height, self._zorder)

        super().__init__(self._vertices, self._indices)

    def fill_color(self, r, g, b):
        self._vertex_colors = 4 * [r, g, b]

    def fill_points(self, vertex_colors):
        self._vertex_colors = vertex_colors

    @staticmethod
    def _create_rect_at(origin, width, height, z_order):
        x_first_vert, y_first_vert = origin
        width_delta = width / 2
        height_delta = height / 2

        return [
            x_first_vert - width_delta, y_first_vert + height_delta, z_order,
            x_first_vert + width_delta, y_first_vert + height_delta, z_order,

            x_first_vert + width_delta, y_first_vert - height_delta, z_order,
            x_first_vert - width_delta, y_first_vert - height_delta, z_order
        ]

    def unpack(self):
        if len(self._vertex_colors) == 0:
            self._vertex_colors = 4 * [0.0, 1.0, 0.0]
        return self.vertices, self._indices, self._vertex_colors


class ShapeComposer:
    """
    Combines multiple shapes into one, handling:
        - vertices
        - colors
        - updating index vertices while merging
    """
    pass
