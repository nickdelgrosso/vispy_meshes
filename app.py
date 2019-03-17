import numpy as np
from vispy import app, gloo
from vispy.util import transforms as tr
from mesh import Mesh
from shaders import current_shader
np.set_printoptions(suppress=True, precision=2)


# Import Mesh
monkey = Mesh('monkey.obj', position=[0, 0, -2], rotation=[0, 0, 0], scale=[1, 1, 1])

# Send projection matrix to the shader
projection_matrix = tr.perspective(90, 1.33, .1, 20)
current_shader['projection_matrix'] = projection_matrix


# Make Window
canvas = app.Canvas(keys='interactive')

@canvas.connect
def on_draw(event):
    gloo.clear([0, 0, 1])
    monkey.rotation[1] += .1
    monkey.draw()
    canvas.update()

# Show Window, Run current_shader.
canvas.show()
app.run()
