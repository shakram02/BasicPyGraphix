#version 330

in vec3 vert;
uniform float rotation;
in vec3 rgb_color;
out vec3 v_color;

void main() {

    mat3 rot = mat3(
        vec2(cos(rotation), sin(rotation)),0,
        vec2(-sin(rotation), cos(rotation)),0,
        vec2(0,0),0
    );

    gl_Position = vec4((rot * vert),1.0);
    v_color = rgb_color;
}
