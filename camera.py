import numpy as np
from vispy.util import transforms as tr
from shaders import current_shader


class Camera:

    def __init__(self, position=(0., 0., 0.), rotation=(0., 0., 0.)):
        self.projection_matrix = tr.perspective(90, 1.33, .1, 20)
        self.position = list(position)
        self.rotation = list(rotation)
        self.scale = (1., 1., 1.)

    @property
    def model_matrix(self):
        """
        Returns a 4x4 model matrix.

        Arguments:
            -translation: x, y, z coordintats
            -rotation: x, y, z rotations (degrees)
            -scale: x, y, z scale.

        Returns:
            -model_matrix: 4x4 array
        """
        sm = tr.scale(self.scale).T
        rx, ry, rz = self.rotation
        rzm = tr.rotate(rz, [0, 0, 1]).T
        rym = tr.rotate(ry, [0, 1, 0]).T
        rxm = tr.rotate(rx, [1, 0, 0]).T
        trm = tr.translate(self.position).T
        mm = trm @ rxm @ rym @ rzm @ sm
        return mm

    @property
    def view_matrix(self):
        return np.linalg.inv(self.model_matrix)

    def activate(self):
        current_shader['projection_matrix'] = self.projection_matrix
        current_shader['view_matrix'] = self.view_matrix
