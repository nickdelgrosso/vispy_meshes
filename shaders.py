from vispy import gloo

VERT_SHADER = """
attribute vec3 vertex;
attribute vec3 normal;

uniform mat4 model_matrix;
uniform mat4 normal_matrix;
uniform mat4 projection_matrix;

varying vec3 world_position;
varying vec3 v_normal;

void main(){
    v_normal = (normal_matrix * vec4(normal, 1.)).xyz;
    world_position = (model_matrix * vec4(vertex, 1.)).xyz;
    gl_Position = projection_matrix * vec4(world_position, 1.);
}
"""

FRAG_SHADER = """
varying vec3 world_position;
varying vec3 v_normal;

vec3 color = vec3(1., 0., 0.);
vec3 light_position = vec3(1., 0., 0.);

void main(){

    vec3 light_direction = light_position - world_position;
    float diffuse = dot(normalize(v_normal), normalize(light_direction));
    gl_FragColor = vec4(diffuse * color, 1.);
}
"""

current_shader = gloo.Program(VERT_SHADER, FRAG_SHADER)
