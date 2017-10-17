#version 330

in vec2 vert;
in vec3 rgb_color;
out vec3 v_color;

void main(){
    gl_Position = vec4(vert,0.0,1.0);
    v_color = rgb_color;
}