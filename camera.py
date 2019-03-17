from vispy.util import transforms as tr
from shaders import current_shader
from physical import Physical

class Camera(Physical):

    def __init__(self, position=(0., 0., 0.), rotation=(0., 0., 0.)):
        Physical.__init__(self, position, rotation)
        self.projection_matrix = tr.perspective(90, 1.33, .1, 20)

    def activate(self):
        current_shader['projection_matrix'] = self.projection_matrix
        current_shader['view_matrix'] = self.view_matrix
