import numpy as np
from vispy import io, gloo
from vispy.util import transforms as tr
from shaders import current_shader
from physical import Physical

class Mesh(Physical):

    def __init__(self, obj_filename, position=(0., 0., 0.), rotation=(0., 0., 0.), scale=(1., 1., 1.), color=(1., 0., 0.)):
        Physical.__init__(self, position, rotation, scale)
        vertices, faces, normals, texcoords = io.read_mesh(obj_filename)
        assert len(vertices[0]) == 3, "Vertices are 3D!"
        assert len(faces[0]) == 3, "Mesh must be triangulated!"
        self.vertices = vertices - np.mean(vertices, axis=0)
        self.normals = normals
        self.faces = faces
        self.color = list(color)

        self.load()

    @property
    def vertex_buffer(self):
        attributes = [
            ('vertex', np.float32, 3),
            ('normal', np.float32, 3),
        ]
        data = np.zeros(len(self.vertices), attributes)
        data['vertex'] = self.vertices
        data['normal'] = self.normals
        vertex_buffer = gloo.VertexBuffer(data)
        return vertex_buffer

    @property
    def index_buffer(self):
        index_buffer = gloo.IndexBuffer(self.faces)
        return index_buffer

    def load(self):
        current_shader.bind(self.vertex_buffer)

    def draw(self):
        current_shader['model_matrix'] = self.model_matrix.T
        current_shader['normal_matrix'] = self.normal_matrix.T
        current_shader['color'] = self.color
        gloo.set_state(depth_test=True)
        current_shader.draw('triangles', self.index_buffer)
