from vispy.util import transforms as tr
from shaders import current_shader


class Camera:

    def __init__(self):
        self.projection_matrix = tr.perspective(90, 1.33, .1, 20)
        self.view_matrix = tr.translate([0, 0, 0])

    def activate(self):
        current_shader['projection_matrix'] = self.projection_matrix
        current_shader['view_matrix'] = self.view_matrix
