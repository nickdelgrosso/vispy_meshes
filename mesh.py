import numpy as np
from vispy import io, gloo
from vispy.util import transforms as tr
from shaders import current_shader


class Mesh:

    def __init__(self, obj_filename, position, rotation, scale):
        vertices, faces, normals, texcoords = io.read_mesh(obj_filename)
        assert len(vertices[0]) == 3, "Vertices are 3D!"
        assert len(faces[0]) == 3, "Mesh must be triangulated!"
        self.vertices = vertices - np.mean(vertices, axis=0)
        self.normals = normals
        self.faces = faces
        self.position = position
        self.rotation = rotation
        self.scale = scale

        self.load()

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
    def normal_matrix(self):
        return np.linalg.inv(self.model_matrix.T)

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
        gloo.set_state(depth_test=True)
        current_shader.draw('triangles', self.index_buffer)
