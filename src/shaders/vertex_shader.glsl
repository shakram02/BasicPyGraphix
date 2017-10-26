#version 330

in vec3 vert;
in vec3 in_pos;
in vec3 rgb_color;
out vec3 v_color;

void main(){
    gl_Position =  vec4(in_pos + vert,1.0);
    v_color = rgb_color;
}