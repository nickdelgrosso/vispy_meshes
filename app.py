from vispy import app, gloo
from mesh import Mesh
from camera import Camera


# Import Mesh
monkey = Mesh('monkey.obj', position=[0, 0, -3], rotation=[0, 0, 0], scale=[1, 1, 1])

camera = Camera()

# Make Window
canvas = app.Canvas(keys='interactive')

@canvas.connect
def on_draw(event):
    camera.activate()

    gloo.clear([0, 0, 1])
    monkey.rotation[1] += .1

    monkey.position[0] = -1.4
    monkey.color = (1., 0., 0.)
    monkey.draw()

    monkey.position[0] = 1.4
    monkey.color = (0., 1., 0.)
    monkey.draw()
    canvas.update()

# Show Window, Run current_shader.
canvas.show()
app.run()
