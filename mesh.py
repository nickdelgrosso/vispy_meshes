import numpy as np
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

print('Hello!')
mm = make_model_matrix([1, 2, 3], [90, 45, 0], [2, 2, 2])
print(mm)
