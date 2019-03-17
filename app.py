import numpy as np
from vispy import app, gloo
from vispy.util import transforms as tr
from mesh import Mesh
from shaders import current_shader
np.set_printoptions(suppress=True, precision=2)


# Import Mesh
monkey = Mesh('monkey.obj', position=[0, 0, -1], rotation=[0, 0, 0], scale=[.5, .5, .5])
print(monkey.model_matrix)
print(monkey.position)

projection_matrix = tr.perspective(90, 1.33, .1, 20)
current_shader['projection_matrix'] = projection_matrix

attributes = [
    ('vertex', np.float32, 3)
]
data = np.zeros(len(monkey.vertices), attributes)
data['vertex'] = monkey.vertices
vertex_buffer = gloo.VertexBuffer(data)
current_shader.bind(vertex_buffer)



index_buffer = gloo.IndexBuffer(monkey.faces)
# Make Window
canvas = app.Canvas(keys='interactive')

@canvas.connect
def on_draw(event):
    monkey.rotation[1] += .1
    current_shader['model_matrix'] = monkey.model_matrix.T
    gloo.clear([0, 0, 1])
    current_shader.draw('triangles', index_buffer)
    canvas.update()

# Show Window, Run current_shader.
canvas.show()
app.run()
