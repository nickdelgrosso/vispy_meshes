import numpy as np
from mesh import Mesh
from vispy import app, gloo
from vispy.util import transforms as tr
np.set_printoptions(suppress=True, precision=2)

VERT_SHADER = """
attribute vec3 vertex;
uniform mat4 model_matrix;
uniform mat4 projection_matrix;
void main(){
    gl_Position = projection_matrix * model_matrix * vec4(vertex, 1.);
}
"""
FRAG_SHADER = """
void main(){
    gl_FragColor = vec4(1., 0., 0., 1.);
}
"""
program = gloo.Program(VERT_SHADER, FRAG_SHADER)
# Import Mesh
monkey = Mesh('monkey.obj', position=[0, 0, -3], rotation=[90, 45, 0], scale=[.2, .2, .2])
print(monkey.model_matrix)
print(monkey.position)

projection_matrix = tr.perspective(90, 1.33, .1, 20)
program['projection_matrix'] = projection_matrix

attributes = [
    ('vertex', np.float32, 3)
]
data = np.zeros(len(monkey.vertices), attributes)
data['vertex'] = monkey.vertices
vertex_buffer = gloo.VertexBuffer(data)
program.bind(vertex_buffer)



index_buffer = gloo.IndexBuffer(monkey.faces)
# Make Window
canvas = app.Canvas(keys='interactive')

@canvas.connect
def on_draw(event):
    monkey.rotation[1] += .1
    program['model_matrix'] = monkey.model_matrix.T
    gloo.clear([0, 0, 1])
    program.draw('triangles', index_buffer)
    canvas.update()

# Show Window, Run Program.
canvas.show()
app.run()
