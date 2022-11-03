# este se corre por triangulo
vertex_shader = """

#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec3 texcoords;
layout (location = 1) in vec3 normals;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;


void main()
{
    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position, 1.0);
}

"""

# este se corre por pixel
fragment_shader = """

#version 450 core

out vec4 fragColor;

void main()
{
    fragColor = vec4(1.0,1.0,1.0,1.0);
}

"""