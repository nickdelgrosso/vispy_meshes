import numpy as np
from mesh import Mesh
from vispy import app, gloo
np.set_printoptions(suppress=True, precision=2)

# Import Mesh
monkey = Mesh('monkey.obj', position=[10, 2, 3], rotation=[90, 45, 0], scale=[2, 2, 2])
print(monkey.model_matrix)
print(monkey.position)

# Make Window
canvas = app.Canvas(keys='interactive')

@canvas.connect
def on_draw(event):
    gloo.clear([0, 0, 1])
    canvas.update()

# Show Window, Run Program.
canvas.show()
app.run()
