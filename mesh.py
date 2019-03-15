import numpy as np
from vispy import io
from vispy.util import transforms as tr
np.set_printoptions(suppress=True, precision=2)

def make_model_matrix(translate, rotation, scale):
    """
    Returns a 4x4 model matrix.

    Arguments:
        -translation: x, y, z coordintats
        -rotation: x, y, z rotations (degrees)
        -scale: x, y, z scale.

    Returns:
        -model_matrix: 4x4 array
    """
    sm = tr.scale(scale).T
    rx, ry, rz = rotation
    rzm = tr.rotate(rz, [0, 0, 1]).T
    rym = tr.rotate(ry, [0, 1, 0]).T
    rxm = tr.rotate(rx, [1, 0, 0]).T
    trm = tr.translate(translate).T
    mm = trm @ rxm @ rym @ rzm @ sm
    return mm

class Mesh:

    def __init__(self, obj_filename, position, rotation, scale):
        vertices, faces, normals, texcoords = io.read_mesh(obj_filename)
        assert len(vertices[0]) == 3, "Vertices are 3D!"
        assert len(faces[0]) == 3, "Mesh must be triangulated!"
        self.vertices = vertices
        self.faces = faces
        self._position = position
        self._rotation = rotation
        self._scale = scale
        self.model_matrix = make_model_matrix(position, rotation, scale)

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value
        self.model_matrix = make_model_matrix(self.position, self.rotation, self.scale)

    @property
    def rotation(self):
        return self._rotation

    @rotation.setter
    def rotation(self, value):
        self._rotation = value
        self.model_matrix = make_model_matrix(self.position, self.rotation, self.scale)

    @property
    def scale(self):
        return self._scale

    @scale.setter
    def scale(self, value):
        self._scale = value
        self.model_matrix = make_model_matrix(self.position, self.rotation, self.scale)


monkey = Mesh('monkey.obj', position=[10, 2, 3], rotation=[90, 45, 0], scale=[2, 2, 2])
print(monkey.model_matrix)
print(monkey.position)

mm = make_model_matrix([1, 2, 3], [90, 45, 0], [2, 2, 2])
