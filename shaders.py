from vispy import gloo

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

current_shader = gloo.Program(VERT_SHADER, FRAG_SHADER)
