from typing import List


class Shape:
    def __init__(self, vertices, indices, colors=None, offsets=None, dimen_count=2):
        self._vertex_dimen = dimen_count
        self._vertices: List = vertices
        self._indices: List = indices
        self._offsets = offsets if not None else [0.0, 0.0]
        self._vertex_colors = colors if not None else self.get_black_fill()

    def add_copy_at(self, offset_vals):
        if isinstance(offset_vals, list):
            if len(offset_vals[0]) != self._vertex_dimen:
                raise ValueError("Invalid dimensions")

            self._offsets.extend(offset_vals)
        else:
            if len(offset_vals) != self._vertex_dimen:
                raise ValueError("Invalid dimensions")

            self._offsets.append(offset_vals)

    def add_indexed_render(self, index_points):

        if isinstance(index_points, list):
            # Check each element in array
            for point in index_points:
                if point >= len(self._vertices):
                    raise ValueError("Index out of range")

            # Add multiple points
            self._indices.extend(index_points)
        else:
            if index_points >= len(self._vertices):
                raise ValueError("Index out of range")
            # Add just one point
            self._indices.append(index_points)

    @property
    def instance_count(self):
        return len(self._offsets)

    @property
    def indices(self):
        return self._indices

    @property
    def vertices(self):
        return self._vertices

    @property
    def vertex_colors(self):
        return self._vertex_colors

    @property
    def offsets(self):
        return self._offsets

    def get_black_fill(self):
        vertex_count = len(self._vertices) // self._vertex_dimen
        channel_count = 3  # r,g,b

        return [0.0 for x in range(vertex_count * channel_count)]


class ShapeComposer:
    pass
