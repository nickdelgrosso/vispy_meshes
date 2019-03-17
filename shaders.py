from vispy import gloo

VERT_SHADER = """
attribute vec3 vertex;
uniform mat4 model_matrix;
uniform mat4 projection_matrix;

varying vec3 world_position;

void main(){
    world_position = (model_matrix * vec4(vertex, 1.)).xyz;
    gl_Position = projection_matrix * vec4(world_position, 1.);
}
"""

FRAG_SHADER = """
varying vec3 world_position;

vec3 color = vec3(1., 0., 0.);

void main(){


    float diffuse = 1.;
    gl_FragColor = vec4(diffuse * color, 1.);
}
"""

current_shader = gloo.Program(VERT_SHADER, FRAG_SHADER)
