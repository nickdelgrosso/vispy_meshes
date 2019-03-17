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
vec3 camera_position = vec3(0., 0., 0.);
float spec_weight = 50.;

void main(){

    vec3 light_direction = light_position - world_position;
    float diffuse = dot(normalize(v_normal), normalize(light_direction));

    vec3 reflection_direction = reflect(light_direction, normalize(v_normal));
    float cosAngle = max(0., -dot(normalize(camera_position - world_position), reflection_direction));
    float specular = pow(cosAngle, spec_weight);


    gl_FragColor = vec4(clamp(diffuse * color + specular * color, 0, 1), 1.);
}
"""

current_shader = gloo.Program(VERT_SHADER, FRAG_SHADER)
